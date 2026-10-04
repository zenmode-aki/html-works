/* 📊 ペンゲッソの集計係
   数えるもの：閲覧数（同じ人の同じ記事は1日1回）・いいね（1人1回）・どの国から・いま読んでいる人・人気の記事
   保存しないもの：IPアドレス・User-Agent（ブラウザの名前）・Cookie・名前・メール。国の2文字コードだけ使う
   （「同じ人か」の判定には、IP＋ブラウザ＋その日の日付＋秘密の種をまぜた“ごちゃまぜ値”を使い、
     それも1日たったら消す。種は最初に1回、ここで自動でつくる）

   置き場所：Cloudflare Workers（無料）＋ Durable Object の SQLite。全部1つの箱（"main"）に入れるので、数がずれない */
import { DurableObject } from "cloudflare:workers";

const DAY_MS = 86400000;
const LIVE_MS = 100000;                       // この時間内に合図があった人を「いま読んでいる」とする
const MAX_SLUGS = 3000;                       // 変な記事名で表を膨らまされないための上限
const SLUG_RE = /^(?:_home|[a-z0-9][a-z0-9-]{0,89})$/;
const VID_RE = /^[A-Za-z0-9_-]{16,64}$/;
const LANG_RE = /^[a-z]{2,3}(?:-[A-Za-z]{2,4})?$/;
const REFS = new Set(["direct", "google", "bing", "yahoo", "x", "facebook", "instagram", "line", "youtube", "github", "reddit", "hatena", "other"]);
const BOT_RE = /bot|crawl|spider|slurp|facebookexternalhit|preview|headless|lighthouse|pingdom|uptime|monitor|scanner|curl\/|wget\/|python|node-fetch|axios|go-http|okhttp|java\/|libwww|httpclient|postman|gptbot|claude|bytespider/i;

const num = (x) => (typeof x === "number" && isFinite(x) ? x : 0);

async function sha(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

function ipPrefix(ip) {
  // IPv6 は先頭64ビットだけ（同じ家の端末が別人に見えないように）
  if (ip && ip.includes(":")) return ip.split(":").slice(0, 4).join(":");
  return ip || "";
}

function deviceOf(ua) {
  if (/ipad|tablet/i.test(ua)) return "tablet";
  if (/mobi|iphone|android/i.test(ua)) return "phone";
  return "desktop";
}

export class Stats extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;
    this.live = new Map();       // vh -> { slug, cc, ts }（保存しない。いま読んでいる人だけ）
    this.rl = new Map();         // ih -> { n, t }（1時間あたりの回数の上限）
    this.memo = new Map();       // 重い集計を少しのあいだ使いまわす
    this.tz = (parseFloat(env.SITE_TZ_HOURS) || 0) * 3600000;
    this.cleanedDay = "";
    ctx.blockConcurrencyWhile(async () => { this.migrate(); });
  }

  dayOf(ms) { return new Date(ms + this.tz).toISOString().slice(0, 10); }

  migrate() {
    const q = (s) => this.sql.exec(s);
    q("CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS seen(day TEXT, vh TEXT, slug TEXT, PRIMARY KEY(day, vh, slug)) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS d_slug(day TEXT, slug TEXT, n INTEGER NOT NULL, PRIMARY KEY(day, slug)) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS t_slug(slug TEXT PRIMARY KEY, n INTEGER NOT NULL) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS t_slug_cc(slug TEXT, cc TEXT, n INTEGER NOT NULL, PRIMARY KEY(slug, cc)) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS t_kv(k TEXT PRIMARY KEY, n INTEGER NOT NULL) WITHOUT ROWID");   // lang:ja / ref:line / dev:phone
    q("CREATE TABLE IF NOT EXISTS likes(slug TEXT, vid TEXT, cc TEXT, ts INTEGER, PRIMARY KEY(slug, vid)) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS t_like(slug TEXT PRIMARY KEY, n INTEGER NOT NULL) WITHOUT ROWID");
    q("CREATE TABLE IF NOT EXISTS rl_like(day TEXT, ih TEXT, n INTEGER NOT NULL, PRIMARY KEY(day, ih)) WITHOUT ROWID");
    // 💬 コメント（2026-10-05）。st: wait（3日待ち）→ ok（そのまま）/ soft（AIがやさしく言い換えた）/ inbox（ご主人だけが読む）/ no（出さない）
    q(`CREATE TABLE IF NOT EXISTS comments(id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT NOT NULL, vid TEXT NOT NULL,
        nick TEXT, home TEXT, cc TEXT, lang TEXT, kind TEXT, body TEXT NOT NULL, ts INTEGER NOT NULL,
        st TEXT NOT NULL DEFAULT 'wait', shown TEXT, why TEXT, done INTEGER, seen INTEGER DEFAULT 0)`);
    q("CREATE INDEX IF NOT EXISTS comments_slug ON comments(slug, st)");
    q("CREATE INDEX IF NOT EXISTS comments_st ON comments(st, ts)");
    q("CREATE TABLE IF NOT EXISTS rl_cm(day TEXT, ih TEXT, n INTEGER NOT NULL, PRIMARY KEY(day, ih)) WITHOUT ROWID");
    const has = this.sql.exec("SELECT v FROM meta WHERE k='secret'").toArray();
    if (!has.length) {
      const seed = [...crypto.getRandomValues(new Uint8Array(32))].map((b) => b.toString(16).padStart(2, "0")).join("");
      this.sql.exec("INSERT INTO meta(k,v) VALUES('secret',?)", seed);
      this.sql.exec("INSERT OR IGNORE INTO meta(k,v) VALUES('since',?)", this.dayOf(Date.now()));
    }
    this.secret = this.sql.exec("SELECT v FROM meta WHERE k='secret'").one().v;
  }

  upsert(table, keyCols, keyVals, by = 1) {
    const cols = keyCols.join(",");
    const qs = keyCols.map(() => "?").join(",");
    this.sql.exec(
      `INSERT INTO ${table}(${cols},n) VALUES(${qs},?) ON CONFLICT(${cols}) DO UPDATE SET n=n+excluded.n`,
      ...keyVals, by
    );
  }

  memoGet(key, ttl, fn) {
    const now = Date.now(), m = this.memo.get(key);
    if (m && now - m.t < ttl) return m.v;
    const v = fn();
    this.memo.set(key, { t: now, v });
    if (this.memo.size > 400) { for (const [k, x] of this.memo) if (now - x.t > ttl) this.memo.delete(k); }
    return v;
  }

  /* ── 古いものを消す（1日に1回） ── */
  clean(day) {
    if (this.cleanedDay === day) return;
    this.cleanedDay = day;
    this.sql.exec("DELETE FROM seen WHERE day < ?", day);          // 「同じ人か」の判定は、その日のうちだけ
    this.sql.exec("DELETE FROM rl_like WHERE day < ?", day);
    this.sql.exec("DELETE FROM rl_cm WHERE day < ?", day);
    const old = this.dayOf(Date.now() - 400 * DAY_MS);
    this.sql.exec("DELETE FROM d_slug WHERE day < ?", old);
  }

  pruneLive(now) {
    for (const [k, x] of this.live) if (now - x.ts > LIVE_MS * 3) this.live.delete(k);
    if (this.rl.size > 20000) this.rl.clear();
  }

  liveNow(now, slug) {
    let all = 0, here = 0;
    const cc = new Map();
    for (const x of this.live.values()) {
      if (now - x.ts > LIVE_MS) continue;
      all++;
      if (slug && x.slug === slug) here++;
      if (x.cc && x.cc !== "ZZ") cc.set(x.cc, (cc.get(x.cc) || 0) + 1);
    }
    return { n: all, here, cc: [...cc.entries()].sort((a, b) => b[1] - a[1]).slice(0, 12) };
  }

  /* ── 1つの記事の数字 ── */
  postStats(slug, vid) {
    const now = Date.now();
    const d7 = this.dayOf(now - 6 * DAY_MS);
    const one = (sql, ...b) => { const r = this.sql.exec(sql, ...b).toArray(); return r.length ? r[0] : null; };
    const v = num((one("SELECT n FROM t_slug WHERE slug=?", slug) || {}).n);
    const v7 = num((one("SELECT SUM(n) s FROM d_slug WHERE slug=? AND day>=?", slug, d7) || {}).s);
    const lk = num((one("SELECT n FROM t_like WHERE slug=?", slug) || {}).n);
    const cc = this.sql.exec("SELECT cc, n FROM t_slug_cc WHERE slug=? AND cc!='ZZ' ORDER BY n DESC LIMIT 12", slug).toArray().map((r) => [r.cc, r.n]);
    const nc = num((one("SELECT COUNT(*) c FROM t_slug_cc WHERE slug=? AND cc!='ZZ'", slug) || {}).c);
    const liked = vid ? !!one("SELECT 1 x FROM likes WHERE slug=? AND vid=?", slug, vid) : false;
    return { p: slug, v, v7, l: lk, lk: liked, nc, cc, live: this.liveNow(now, slug) };
  }

  /* ── サイト全体の数字 ── */
  siteStats() {
    return this.memoGet("site", 60000, () => {
      const now = Date.now(), today = this.dayOf(now), d7 = this.dayOf(now - 6 * DAY_MS);
      const one = (sql, ...b) => { const r = this.sql.exec(sql, ...b).toArray(); return r.length ? r[0] : null; };
      const all = (sql, ...b) => this.sql.exec(sql, ...b).toArray();
      const kv = (pre) => all("SELECT k, n FROM t_kv WHERE k LIKE ? ORDER BY n DESC", pre + ":%").map((r) => [r.k.slice(pre.length + 1), r.n]);
      const cc = all("SELECT cc, SUM(n) n FROM t_slug_cc WHERE cc!='ZZ' GROUP BY cc ORDER BY n DESC LIMIT 80").map((r) => [r.cc, r.n]);
      return {
        since: (one("SELECT v FROM meta WHERE k='since'") || {}).v || today,
        v: num((one("SELECT SUM(n) s FROM t_slug") || {}).s),
        vt: num((one("SELECT SUM(n) s FROM d_slug WHERE day=?", today) || {}).s),
        v7: num((one("SELECT SUM(n) s FROM d_slug WHERE day>=?", d7) || {}).s),
        l: num((one("SELECT SUM(n) s FROM t_like") || {}).s),
        nc: num((one("SELECT COUNT(DISTINCT cc) c FROM t_slug_cc WHERE cc!='ZZ'") || {}).c),
        cc,
        top7: all("SELECT slug, SUM(n) n FROM d_slug WHERE day>=? AND slug!='_home' GROUP BY slug ORDER BY n DESC LIMIT 20", d7).map((r) => [r.slug, r.n]),
        topAll: all("SELECT slug, n FROM t_slug WHERE slug!='_home' ORDER BY n DESC LIMIT 20").map((r) => [r.slug, r.n]),
        topLiked: all("SELECT slug, n FROM t_like WHERE n>0 ORDER BY n DESC LIMIT 20").map((r) => [r.slug, r.n]),
        per: all("SELECT s.slug AS slug, s.n AS v, COALESCE(l.n, 0) AS l FROM t_slug s LEFT JOIN t_like l ON l.slug = s.slug WHERE s.slug != '_home' ORDER BY s.n DESC LIMIT 1000").map((r) => [r.slug, r.v, r.l]),
        lang: kv("lang"), ref: kv("ref"), dev: kv("dev"),
        // 📈 日ごとの閲覧（30日ぶん。/stats/ のグラフ用）
        days: all("SELECT day, SUM(n) n FROM d_slug WHERE day>=? GROUP BY day ORDER BY day", this.dayOf(now - 29 * DAY_MS)).map((r) => [r.day, r.n]),
        gen: Math.floor(now / 1000),
      };
    });
  }

  /* ── 1ページを開いた（数える）。同じ人の同じ記事は、その日のうち1回だけ ── */
  async hit(a) {
    const now = Date.now(), day = this.dayOf(now);
    const bot = a.bot || !a.ua || BOT_RE.test(a.ua);
    const vh = (await sha(this.secret + "|" + day + "|" + ipPrefix(a.ip) + "|" + a.ua)).slice(0, 24);
    const ih = (await sha(this.secret + "|ip|" + ipPrefix(a.ip))).slice(0, 16);
    const vid = a.vid && VID_RE.test(a.vid) ? a.vid : "";
    if (!this.allow(ih, now, 3000)) return { ok: 0 };
    this.clean(day);
    let isNew = false;
    if (!bot) {
      const seen = this.sql.exec("SELECT 1 x FROM seen WHERE day=? AND vh=? AND slug=?", day, vh, a.slug).toArray().length;
      if (!seen) {
        const known = this.sql.exec("SELECT 1 x FROM t_slug WHERE slug=?", a.slug).toArray().length;
        const room = known || num(this.sql.exec("SELECT COUNT(*) c FROM t_slug").one().c) < MAX_SLUGS;
        if (room) {
          this.sql.exec("INSERT INTO seen(day,vh,slug) VALUES(?,?,?)", day, vh, a.slug);
          this.upsert("d_slug", ["day", "slug"], [day, a.slug]);
          this.upsert("t_slug", ["slug"], [a.slug]);
          this.upsert("t_slug_cc", ["slug", "cc"], [a.slug, a.cc]);
          if (a.lang && LANG_RE.test(a.lang)) this.upsert("t_kv", ["k"], ["lang:" + a.lang.toLowerCase()]);
          this.upsert("t_kv", ["k"], ["dev:" + deviceOf(a.ua)]);
          this.upsert("t_kv", ["k"], ["ref:" + (REFS.has(a.ref) ? a.ref : "other")]);
          isNew = true;
        }
      }
      this.live.set(vh, { slug: a.slug, cc: a.cc, ts: now });
      this.pruneLive(now);
    }
    const post = this.postStats(a.slug, vid);
    return { ok: 1, n: isNew ? 1 : 0, post };
  }

  /* ── 読んでいる合図（45秒ごと）。数は増やさない ── */
  async ping(a) {
    const now = Date.now(), day = this.dayOf(now);
    const bot = a.bot || !a.ua || BOT_RE.test(a.ua);
    const vh = (await sha(this.secret + "|" + day + "|" + ipPrefix(a.ip) + "|" + a.ua)).slice(0, 24);
    const ih = (await sha(this.secret + "|ip|" + ipPrefix(a.ip))).slice(0, 16);
    if (!this.allow(ih, now, 3000)) return { ok: 0 };
    if (!bot) this.live.set(vh, { slug: a.slug, cc: a.cc, ts: now });
    return { ok: 1, live: this.liveNow(now, a.slug) };
  }

  allow(ih, now, perHour) {
    const r = this.rl.get(ih);
    if (!r || now - r.t > 3600000) { this.rl.set(ih, { n: 1, t: now }); return true; }
    r.n++;
    return r.n <= perHour;
  }

  /* ── いいね（1人1回・取り消せる）。同じ回線から1日に押せる回数にも上限 ── */
  async like(a) {
    const now = Date.now(), day = this.dayOf(now);
    if (a.bot || !a.ua || BOT_RE.test(a.ua)) return { ok: 0 };
    if (!VID_RE.test(a.vid || "")) return { ok: 0, e: "vid" };
    const ih = (await sha(this.secret + "|ip|" + ipPrefix(a.ip))).slice(0, 16);
    this.clean(day);
    const used = num((this.sql.exec("SELECT n FROM rl_like WHERE day=? AND ih=?", day, ih).toArray()[0] || {}).n);
    if (used >= 80) return { ok: 0, e: "limit" };
    this.upsert("rl_like", ["day", "ih"], [day, ih]);
    const had = this.sql.exec("SELECT 1 x FROM likes WHERE slug=? AND vid=?", a.slug, a.vid).toArray().length;
    if (a.on && !had) {
      this.sql.exec("INSERT INTO likes(slug,vid,cc,ts) VALUES(?,?,?,?)", a.slug, a.vid, a.cc, now);
      this.upsert("t_like", ["slug"], [a.slug], 1);
    } else if (!a.on && had) {
      this.sql.exec("DELETE FROM likes WHERE slug=? AND vid=?", a.slug, a.vid);
      this.upsert("t_like", ["slug"], [a.slug], -1);
    }
    this.memo.delete("site");
    return { ok: 1, post: this.postStats(a.slug, a.vid) };
  }

  async post(a) {
    const vid = a.vid && VID_RE.test(a.vid) ? a.vid : "";
    const base = this.memoGet("post:" + a.slug, 15000, () => this.postStats(a.slug, ""));
    if (!vid) return { ok: 1, post: base };
    const liked = !!this.sql.exec("SELECT 1 x FROM likes WHERE slug=? AND vid=?", a.slug, vid).toArray().length;
    return { ok: 1, post: { ...base, lk: liked, live: this.liveNow(Date.now(), a.slug) } };
  }

  async stats() {
    const s = this.siteStats();
    const inbox = num((this.sql.exec("SELECT COUNT(*) c FROM comments WHERE st='inbox' AND seen=0").toArray()[0] || {}).c);
    const cm = num((this.sql.exec("SELECT COUNT(*) c FROM comments WHERE st IN ('ok','soft')").toArray()[0] || {}).c);
    return { ok: 1, site: { ...s, cm, inbox: inbox ? 1 : 0, live: this.liveNow(Date.now(), "") } };
  }

  /* ───────── 💬 コメント ─────────
     ・書いたコメントは、すぐには出さない。3日おいてから AI が読む（勢いで書いたものを、そのまま出さないため）
     ・AI の判断：そのまま出す（ok）／やさしい言い方に直して出す（soft）／ご主人への質問・お願いは、ご主人だけが読む（inbox）／出さない（no）
     ・「ご主人へ」を選んで書いたものは、待たずにご主人の受け箱へ（みんなには見えない）
     ・書いた人は、自分のコメントがいまどうなっているかを見られる（同じ端末の vid で） */
  async commentAdd(a) {
    const now = Date.now(), day = this.dayOf(now);
    if (a.bot || !a.ua || BOT_RE.test(a.ua)) return { ok: 0, e: "bot" };
    if (!VID_RE.test(a.vid || "")) return { ok: 0, e: "vid" };
    const ih = (await sha(this.secret + "|ip|" + ipPrefix(a.ip))).slice(0, 16);
    this.clean(day);
    const used = num((this.sql.exec("SELECT n FROM rl_cm WHERE day=? AND ih=?", day, ih).toArray()[0] || {}).n);
    if (used >= 8) return { ok: 0, e: "limit" };
    const mine = num((this.sql.exec("SELECT COUNT(*) c FROM comments WHERE slug=? AND vid=? AND ts>?", a.slug, a.vid, now - DAY_MS).toArray()[0] || {}).c);
    if (mine >= 3) return { ok: 0, e: "limit" };
    const total = num(this.sql.exec("SELECT COUNT(*) c FROM comments WHERE st='wait'").one().c);
    if (total >= 5000) return { ok: 0, e: "busy" };
    this.upsert("rl_cm", ["day", "ih"], [day, ih]);
    const kind = a.kind === "q" ? "q" : "c";
    const st = kind === "q" ? "inbox" : "wait";
    this.sql.exec("INSERT INTO comments(slug,vid,nick,home,cc,lang,kind,body,ts,st,done) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
      a.slug, a.vid, a.nick, a.home, a.cc, a.lang, kind, a.body, now, st, kind === "q" ? now : null);
    return { ok: 1, st, list: this.commentList(a.slug, a.vid) };
  }

  commentList(slug, vid) {
    const pub = this.sql.exec("SELECT id, nick, home, lang, shown, st, done FROM comments WHERE slug=? AND st IN ('ok','soft') ORDER BY done DESC LIMIT 100", slug).toArray()
      .map((r) => ({ id: r.id, n: r.nick || "", h: r.home || "", l: r.lang || "", t: r.shown || "", soft: r.st === "soft" ? 1 : 0, at: r.done }));
    const mine = vid ? this.sql.exec("SELECT id, kind, body, st, ts FROM comments WHERE slug=? AND vid=? ORDER BY ts DESC LIMIT 20", slug, vid).toArray()
      .map((r) => ({ id: r.id, k: r.kind, t: r.body, st: r.st === "soft" ? "ok" : r.st === "no" ? "wait" : r.st === "err" ? "wait" : r.st, at: r.ts })) : [];
    // 出さないと決めたものも、書いた人には「待っている」と見せる（何度も書き直してすり抜けようとさせない）
    return { pub, mine, hold: 3 };
  }

  async comments(a) { return { ok: 1, ...this.commentList(a.slug, VID_RE.test(a.vid || "") ? a.vid : "") }; }

  /* 3日たったコメントを AI が読む（1時間に1回、cron から） */
  async moderate(force) {
    const now = Date.now();
    const due = this.sql.exec("SELECT id, slug, nick, lang, body FROM comments WHERE st IN ('wait','err') AND ts<? ORDER BY ts LIMIT 25",
      force ? now : now - 3 * DAY_MS).toArray();
    let n = 0;
    for (const c of due) {
      const d = await judge(this.env, c);
      if (!d) { this.sql.exec("UPDATE comments SET st='err' WHERE id=?", c.id); continue; }
      this.sql.exec("UPDATE comments SET st=?, shown=?, why=?, done=? WHERE id=?", d.st, d.text, d.why, now, c.id);
      n++;
    }
    return { ok: 1, n, left: due.length - n };
  }

  /* ご主人の受け箱（合言葉つき） */
  async admin(a) {
    if (a.op === "list") {
      const rows = this.sql.exec("SELECT id, slug, nick, home, cc, lang, kind, body, ts, st, shown, why, done, seen FROM comments ORDER BY ts DESC LIMIT 300").toArray();
      return { ok: 1, rows };
    }
    const id = Number(a.id) || 0;
    if (a.op === "seen") this.sql.exec("UPDATE comments SET seen=1 WHERE id=?", id);
    else if (a.op === "hide") this.sql.exec("UPDATE comments SET st='no', why='ご主人が非表示にした', done=? WHERE id=?", Date.now(), id);
    else if (a.op === "show") this.sql.exec("UPDATE comments SET st='ok', shown=COALESCE(shown, body), why='ご主人が公開した', done=? WHERE id=?", Date.now(), id);
    else if (a.op === "delete") this.sql.exec("DELETE FROM comments WHERE id=?", id);
    else if (a.op === "run") return this.moderate(true);
    else return { ok: 0, e: "op" };
    return { ok: 1 };
  }
}

/* ───────── 🤖 AI がコメントを読む（Cloudflare Workers AI・無料枠） ───────── */
const JUDGE_PROMPT = `You moderate reader comments on "15-second blog", a friendly personal blog written by Pengesso, a felt penguin, on behalf of his owner (a Japanese man).
Read ONE comment and decide:
- "publish": friendly or neutral, safe to show as written.
- "soften": the idea is fine but the tone is rude, harsh, sarcastic or too strong. Rewrite it kindly in the SAME language as the comment, keeping the meaning and the writer's voice, max 2 sentences longer than needed. Never add new facts.
- "owner": the comment is mainly a question or a request to the owner or Pengesso (e.g. "where is this cafe?", "please write about…", "can I contact you?"), or it shares personal details. Only the owner will read it.
- "reject": spam, ads, links to sell something, sexual content, hate, threats, personal attacks, private information about any person, or anything that names or guesses the owner's employer, workplace or job details.
Return JSON only: {"decision": "...", "text": "<the text to publish: same as the comment for publish, the kind rewrite for soften, empty otherwise>", "reason": "<short reason in Japanese>"}`;

async function judge(env, c) {
  if (/https?:\/\/|www\.|\.com\b|@[a-z0-9_]{3,}/i.test(c.body)) return { st: "inbox", text: null, why: "リンク・連絡先があるので、ご主人だけに" };
  if (!env.AI) return null;
  const schema = {
    type: "object",
    properties: { decision: { type: "string", enum: ["publish", "soften", "owner", "reject"] }, text: { type: "string" }, reason: { type: "string" } },
    required: ["decision", "text", "reason"],
  };
  const messages = [
    { role: "system", content: JUDGE_PROMPT },
    { role: "user", content: "Post: " + c.slug + "\nComment (" + (c.lang || "?") + "):\n" + c.body },
  ];
  for (const model of ["@cf/meta/llama-3.3-70b-instruct-fp8-fast", "@cf/meta/llama-3.1-8b-instruct-fast"]) {
    try {
      const r = await env.AI.run(model, { messages, response_format: { type: "json_schema", json_schema: schema }, max_tokens: 600 });
      let o = r && r.response;
      if (typeof o === "string") o = JSON.parse(o.slice(o.indexOf("{"), o.lastIndexOf("}") + 1));
      if (!o || !o.decision) continue;
      const why = String(o.reason || "").slice(0, 200);
      const text = String(o.text || "").trim().slice(0, 800);
      if (o.decision === "publish") return { st: "ok", text: c.body, why };
      if (o.decision === "soften" && text) return { st: "soft", text, why };
      if (o.decision === "owner") return { st: "inbox", text: null, why };
      if (o.decision === "reject") return { st: "no", text: null, why };
    } catch (e) { /* 次のモデルで試す */ }
  }
  return null;
}

/* ───────── 入口（Worker）：CORS・入力の確認・国の取り出し ───────── */
function json(body, status, headers) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8", ...headers } });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
    const dev = env.DEV === "1";
    const okOrigin = allowed.includes(origin) || (dev && /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin));
    const base = { Vary: "Origin", "X-Content-Type-Options": "nosniff" };
    if (okOrigin) {
      base["Access-Control-Allow-Origin"] = origin;
      base["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS";
      base["Access-Control-Allow-Headers"] = "content-type, x-admin-key";
      base["Access-Control-Max-Age"] = "86400";
    }
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: base });

    const path = url.pathname.replace(/\/+$/, "");
    if (path === "/v1/health") return json({ ok: 1 }, 200, { ...base, "Cache-Control": "no-store" });

    const country = (dev && env.DEV_COUNTRY) || (request.cf && request.cf.country) || "";
    const cc = /^[A-Z]{2}$/.test(country) && country !== "XX" && country !== "T1" ? country : "ZZ";
    const ua = request.headers.get("User-Agent") || "";
    const ip = request.headers.get("CF-Connecting-IP") || request.headers.get("X-Forwarded-For") || "";
    const stub = env.STATS.get(env.STATS.idFromName("main"), { locationHint: "apac" });

    try {
      if (request.method === "GET" && path === "/v1/stats") {
        const r = await stub.stats();
        return json(r, 200, { ...base, "Cache-Control": "public, max-age=60" });
      }
      if (request.method === "GET" && path === "/v1/post") {
        const slug = url.searchParams.get("p") || "";
        if (!SLUG_RE.test(slug)) return json({ ok: 0, e: "slug" }, 400, base);
        const r = await stub.post({ slug, vid: url.searchParams.get("v") || "" });
        return json(r, 200, { ...base, "Cache-Control": "private, max-age=10" });
      }
      if (request.method === "POST" && (path === "/v1/hit" || path === "/v1/ping" || path === "/v1/like")) {
        if (!okOrigin) return json({ ok: 0, e: "origin" }, 403, base);
        const raw = (await request.text()).slice(0, 2000);
        let b = {};
        try { b = JSON.parse(raw); } catch (e) { return json({ ok: 0, e: "json" }, 400, base); }
        const slug = String(b.p || "");
        if (!SLUG_RE.test(slug)) return json({ ok: 0, e: "slug" }, 400, base);
        const a = { slug, cc, ua, ip, bot: false, vid: typeof b.v === "string" ? b.v : "", lang: typeof b.l === "string" ? b.l : "", ref: typeof b.r === "string" ? b.r : "", on: b.on === true };
        const r = path === "/v1/hit" ? await stub.hit(a) : path === "/v1/ping" ? await stub.ping(a) : await stub.like(a);
        return json(r, 200, { ...base, "Cache-Control": "no-store" });
      }
      if (request.method === "GET" && path === "/v1/comments") {
        const slug = url.searchParams.get("p") || "";
        if (!SLUG_RE.test(slug)) return json({ ok: 0, e: "slug" }, 400, base);
        const r = await stub.comments({ slug, vid: url.searchParams.get("v") || "" });
        return json(r, 200, { ...base, "Cache-Control": "private, max-age=15" });
      }
      if (request.method === "POST" && path === "/v1/comment") {
        if (!okOrigin) return json({ ok: 0, e: "origin" }, 403, base);
        const raw = (await request.text()).slice(0, 6000);
        let b = {};
        try { b = JSON.parse(raw); } catch (e) { return json({ ok: 0, e: "json" }, 400, base); }
        const slug = String(b.p || "");
        if (!SLUG_RE.test(slug)) return json({ ok: 0, e: "slug" }, 400, base);
        if (b.hp) return json({ ok: 1, st: "wait", list: { pub: [], mine: [], hold: 3 } }, 200, base);   // 🍯 ロボットの入れ物には、成功したふりだけ
        const clean = (s, n) => String(s || "").replace(/[\u0000-\u0008\u000b-\u001f\u007f‪-‮⁦-⁩]/g, "").trim().slice(0, n);
        const body = clean(b.t, 1000).replace(/\n{3,}/g, "\n\n");
        if (body.length < 2) return json({ ok: 0, e: "short" }, 400, base);
        const home = /^[A-Z]{2}$/.test(String(b.h || "")) ? String(b.h) : "";
        const lang = typeof b.l === "string" && LANG_RE.test(b.l) ? b.l : "";
        const r = await stub.commentAdd({ slug, vid: typeof b.v === "string" ? b.v : "", ua, ip, cc, nick: clean(b.n, 24), home, lang, kind: b.k === "q" ? "q" : "c", body });
        return json(r, 200, { ...base, "Cache-Control": "no-store" });
      }
      if (path === "/v1/admin") {
        const key = request.headers.get("x-admin-key") || "";
        if (!env.ADMIN_KEY || key.length < 16 || !(await same(key, env.ADMIN_KEY))) return json({ ok: 0, e: "key" }, 403, { ...base, "Cache-Control": "no-store" });
        let b = {};
        if (request.method === "POST") { try { b = JSON.parse((await request.text()).slice(0, 2000)); } catch (e) { b = {}; } }
        else b = { op: "list" };
        const r = await stub.admin(b);
        return json(r, 200, { ...base, "Cache-Control": "no-store" });
      }
      return json({ ok: 0, e: "not found" }, 404, base);
    } catch (e) {
      // 保存先の上限などで失敗しても、読む人の画面は壊さない
      return json({ ok: 0, e: "busy" }, 200, { ...base, "Cache-Control": "no-store" });
    }
  },

  // ⏰ 1時間に1回：3日たったコメントを AI が読む
  async scheduled(event, env, ctx) {
    const stub = env.STATS.get(env.STATS.idFromName("main"), { locationHint: "apac" });
    ctx.waitUntil(stub.moderate(false));
  },
};

// 合言葉を、かかった時間で当てられないようにくらべる
async function same(a, b) {
  const [x, y] = await Promise.all([sha("k|" + a), sha("k|" + b)]);
  let d = 0;
  for (let i = 0; i < x.length; i++) d |= x.charCodeAt(i) ^ y.charCodeAt(i);
  return d === 0;
}
