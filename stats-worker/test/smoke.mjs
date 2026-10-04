// 集計係のかんたんなテスト。使い方：
//   1) cd stats-worker && npx wrangler dev --port 8799 --var DEV:1 --var DEV_COUNTRY:JP
//   2) 別のターミナルで  node test/smoke.mjs  （BASE=http://localhost:8799 が初期値）
const BASE = process.env.BASE || "http://localhost:8799";
const ORIGIN = "http://localhost:8765";
const UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1";
let fails = 0;
const ok = (c, m) => { console.log((c ? "✅ " : "❌ ") + m); if (!c) fails++; };

async function call(method, path, body, o = {}) {
  const headers = { Origin: o.origin ?? ORIGIN, "User-Agent": o.ua ?? UA, "CF-Connecting-IP": o.ip ?? "203.0.113.5" };
  if (body) headers["Content-Type"] = "text/plain;charset=UTF-8";
  const r = await fetch(BASE + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
  let j = null; try { j = await r.json(); } catch (e) {}
  return { s: r.status, j, h: r.headers };
}

const slug = "t-" + Date.now();
const vid = "v" + "a1b2c3d4".repeat(5);       // 41文字
const h = await call("GET", "/v1/health");
ok(h.s === 200 && h.j.ok === 1, "health");

const s0 = (await call("GET", "/v1/stats")).j.site;
let r = await call("POST", "/v1/hit", { p: slug, l: "ja", r: "line", v: vid });
ok(r.s === 200 && r.j.ok === 1 && r.j.n === 1, "1人目の閲覧は数える");
ok(r.j.post.v === 1 && r.j.post.l === 0 && r.j.post.lk === false, "閲覧1・いいね0");
ok(JSON.stringify(r.j.post.cc) === '[["JP",1]]', "国は JP");
ok(r.j.post.live.here === 1, "いま読んでいる人は1人（自分）");
ok(r.h.get("access-control-allow-origin") === ORIGIN, "CORS で読める");

r = await call("POST", "/v1/hit", { p: slug, l: "ja" });
ok(r.j.n === 0 && r.j.post.v === 1, "同じ人の同じ記事は数えない");

r = await call("POST", "/v1/hit", { p: slug, l: "en", r: "x" }, { ip: "198.51.100.7" });
ok(r.j.n === 1 && r.j.post.v === 2, "別の人は数える");

r = await call("POST", "/v1/hit", { p: slug }, { ip: "198.51.100.8", ua: "Googlebot/2.1 (+http://www.google.com/bot.html)" });
ok(r.j.n === 0 && r.j.post.v === 2, "ボットは数えない");

r = await call("POST", "/v1/hit", { p: "Bad Slug!" });
ok(r.s === 400, "変な記事名ははじく");
r = await call("POST", "/v1/hit", { p: slug }, { origin: "https://evil.example" });
ok(r.s === 403, "知らない場所からの書き込みは断る");

r = await call("POST", "/v1/like", { p: slug, v: vid, on: true });
ok(r.j.ok === 1 && r.j.post.l === 1 && r.j.post.lk === true, "いいね +1");
r = await call("POST", "/v1/like", { p: slug, v: vid, on: true });
ok(r.j.post.l === 1, "同じ人が2回押しても1つ");
r = await call("GET", `/v1/post?p=${slug}&v=${vid}`);
ok(r.j.post.lk === true && r.j.post.l === 1, "自分がいいね済みだと分かる");
r = await call("GET", `/v1/post?p=${slug}`);
ok(r.j.post.lk === false, "ほかの人には「いいね済み」と出ない");
r = await call("POST", "/v1/like", { p: slug, v: vid, on: false });
ok(r.j.post.l === 0 && r.j.post.lk === false, "取り消すと -1");
r = await call("POST", "/v1/like", { p: slug, v: "short", on: true });
ok(r.j.ok === 0, "短すぎる ID は断る");

r = await call("POST", "/v1/ping", { p: slug });
ok(r.j.ok === 1 && r.j.live.here >= 1, "ping で、いま読んでいる人が出る");

const s1 = (await call("GET", "/v1/stats")).j.site;
ok(s1.v >= s0.v + 2 || s1.gen === s0.gen, "全体の閲覧数が増える（60秒のキャッシュ中は同じ）");
ok(Array.isArray(s1.cc) && Array.isArray(s1.lang) && Array.isArray(s1.ref) && Array.isArray(s1.dev), "全体の国・言語・流入元・端末が出る");

// いいねの上限（同じ回線から1日80回まで）
let limited = false;
for (let i = 0; i < 90 && !limited; i++) {
  const x = await call("POST", "/v1/like", { p: slug, v: "w" + String(i).padStart(20, "0"), on: true }, { ip: "192.0.2.99" });
  if (x.j.e === "limit") limited = true;
}
ok(limited, "同じ回線からのいいねの連打は止まる");

// 💬 コメント：すぐには出ない・書いた人には「待っている」と見える・「ご主人へ」は受け箱へ・ロボットの入れ物は捨てる
r = await call("POST", "/v1/comment", { p: slug, v: vid, n: "ぺん", h: "JP", l: "ja", t: "おもしろかったです！", k: "c" });
ok(r.j.ok === 1 && r.j.st === "wait", "コメントは3日待ち");
ok(r.j.list.pub.length === 0 && r.j.list.mine.length === 1 && r.j.list.mine[0].st === "wait", "みんなにはまだ見えない・自分には見える");
r = await call("POST", "/v1/comment", { p: slug, v: vid, n: "ぺん", h: "JP", l: "ja", t: "このお店はどこですか？", k: "q" });
ok(r.j.ok === 1 && r.j.st === "inbox", "ご主人への質問は受け箱へ");
r = await call("POST", "/v1/comment", { p: slug, v: vid, t: "spam", hp: "x" });
ok(r.j.ok === 1 && (await call("GET", "/v1/comments?p=" + slug + "&v=" + vid)).j.mine.length === 2, "ロボットの入れ物に入ったものは保存しない");
r = await call("POST", "/v1/comment", { p: slug, v: vid, t: "x" });
ok(r.j.ok === 0 && r.j.e === "short", "短すぎるものは受け取らない");
r = await call("POST", "/v1/comment", { p: slug, v: vid, t: "hello" }, { origin: "https://evil.example" });
ok(r.s === 403, "ほかのサイトからは書けない");
r = await call("GET", "/v1/admin");
ok(r.s === 403, "合言葉なしでは受け箱は見えない");
console.log(fails ? `\n❌ ${fails} 件失敗` : "\n✅ ぜんぶ通りました");
process.exit(fails ? 1 : 0);
