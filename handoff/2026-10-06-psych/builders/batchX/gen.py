# Batch W generator: writes draft/<slug>/{index.html,source.md,meta.json,i18n/ja.json}
import html, json, pathlib, re

ROOT = pathlib.Path("/Users/ezakimasaaki/Desktop/html-works")

HEAD_CSS = r"""
  /* 🐼 元気が出る心理学シリーズ（2026-10-05）。真面目な話 → ポップに（トーン反転） */
  :root {
    --bg: %(bg)s;
    --card: rgba(255,255,255,.95);
    --text: #2f2a3a;
    --muted: %(muted)s;
    --acc: %(acc)s;
    --acc2: %(acc2)s;
    --shadow: 0 20px 55px %(shadow)s;
    --round: 28px;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; color: var(--text);
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif;
    background:
      radial-gradient(circle at 10%% 6%%, %(r1)s, transparent 26%%),
      radial-gradient(circle at 92%% 18%%, %(r2)s, transparent 28%%),
      radial-gradient(circle at 50%% 100%%, %(r3)s, transparent 36%%),
      var(--bg);
  }
  main { width: min(720px, calc(100%% - 24px)); margin: 0 auto; padding: 22px 0 70px; }

  .topbar { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
  .home { display: inline-block; min-height: 44px; padding: 12px 18px; border-radius: 999px; background: #fff; color: var(--acc);
    border: 2px solid rgba(255,255,255,.9); font-size: 14px; text-decoration: none; box-shadow: 0 6px 16px rgba(60,50,90,.10); }
  .badges { display: flex; align-items: center; gap: 8px; }
  .wc-badge { padding: 10px 16px; border-radius: 999px; background: #fff; border: 2px solid rgba(255,255,255,.9);
    color: var(--muted); font-size: 13px; letter-spacing: .04em; box-shadow: 0 6px 16px rgba(60,50,90,.08); }
  .stage { padding: 10px 13px; border-radius: 999px; font-size: 11px; font-weight: 900; letter-spacing: .12em; white-space: nowrap;
    box-shadow: 0 6px 16px rgba(60,50,90,.16); }
  .stage-public { background: #23c98a; color: #04331d; }

  .label { color: var(--acc); font-size: 13px; font-weight: 800; letter-spacing: .14em; margin-bottom: 16px; }
  .label .topic { display: inline-block; margin-right: 10px; padding: 5px 12px; border-radius: 999px; background: var(--acc); color: #fff;
    font-size: 11.5px; font-weight: 900; letter-spacing: .12em; }
  h1 { margin: 0 0 22px; color: %(h1)s; font-size: clamp(32px, 6.4vw, 56px); line-height: 1.08; letter-spacing: -.04em;
    text-wrap: balance; text-shadow: 0 4px 0 rgba(255,255,255,.75); }

  .photo { margin: 0 0 24px; overflow: hidden; background: %(photo)s; border: 7px solid rgba(255,255,255,.8); border-radius: 32px;
    box-shadow: var(--shadow); transform: rotate(-.35deg); }
  .photo img { display: block; width: 100%%; height: auto; }

  .card { position: relative; margin-top: 18px; padding: 24px 26px; background: var(--card); border: 2px solid rgba(255,255,255,.92);
    border-radius: var(--round); box-shadow: 0 12px 32px rgba(60,50,90,.09); }
  .card-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
  .card-emoji { font-size: 26px; line-height: 1; }
  .card-label { font-size: 12.5px; font-weight: 900; letter-spacing: .16em; color: var(--acc); text-transform: uppercase; }
  p { margin: 0; font-family: "Trebuchet MS", "Avenir Next Rounded", sans-serif; font-weight: 700; font-size: clamp(17px, 2.4vw, 21px); line-height: 1.72; }
  .big { font-size: clamp(23px, 4vw, 32px); font-weight: 850; line-height: 1.42; color: %(big)s;
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif; }

  /* ════ ⚡ 触って遊べる部品（共通の枠）════
     文字はぜんぶ HTML に置いて、JS は class・data-*・数字だけを変える（訳がそのまま効くように） */
  .game { margin-top: 26px; padding: 22px 16px 20px; border-radius: 30px; text-align: center; color: #fff;
    background: %(game)s; box-shadow: var(--shadow); overflow: hidden; position: relative; }
  .game-kicker { font-size: 12px; font-weight: 900; letter-spacing: .18em; opacity: .92; }
  .game-title { margin-top: 4px; font-size: clamp(21px, 4.6vw, 28px); font-weight: 900; line-height: 1.25; }
  .game-hint { margin: 6px auto 0; max-width: 440px; font-size: 14.5px; font-weight: 800; opacity: .95; line-height: 1.45; }
  .btn { display: inline-flex; align-items: center; justify-content: center; gap: 6px; min-height: 52px; padding: 10px 18px; border: 0; border-radius: 999px;
    cursor: pointer; font: inherit; font-size: 16px; font-weight: 900; line-height: 1.25; color: #2f2a3a; background: #fff;
    box-shadow: 0 6px 0 rgba(0,0,0,.18); transition: transform .08s ease, box-shadow .08s ease, opacity .2s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; }
  .btn:active { transform: translateY(5px); box-shadow: 0 1px 0 rgba(0,0,0,.18); }
  .btn:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .btn[disabled] { opacity: .45; cursor: default; }
  .btn.ghost { background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  @keyframes shake { 20%% { transform: translateX(-5px); } 40%% { transform: translateX(5px); } 60%% { transform: translateX(-3px); } 80%% { transform: translateX(2px); } }
  @keyframes boing { 0%% { transform: scale(1); } 35%% { transform: scale(1.18); } 65%% { transform: scale(.94); } 100%% { transform: scale(1); } }

  .credit { margin-top: 22px; text-align: center; font-size: 13px; font-weight: 800; color: var(--muted); }

  .next { display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-top: 34px; min-height: 44px; padding: 20px 24px;
    border-radius: var(--round); text-decoration: none; background: linear-gradient(135deg, var(--acc), var(--acc2)); color: #fff; box-shadow: var(--shadow); }
  .next-kicker { font-size: 11.5px; font-weight: 900; letter-spacing: .18em; opacity: .82; }
  .next-title { margin-top: 4px; font-size: clamp(17px, 3vw, 21px); line-height: 1.3; }
  .next-arrow { font-size: 26px; flex: 0 0 auto; }

  /* ⚡ モーションキット */
  @keyframes rise { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: none; } }
  .label { animation: rise .5s .05s both ease-out; }
  h1 { animation: rise .6s .12s both ease-out; }
  .photo { animation: rise .6s .22s both ease-out; }
  .js .card, .js .game { opacity: 0; transform: translateY(18px); transition: opacity .55s ease-out, transform .55s ease-out; }
  .js .card.in, .js .game.in { opacity: 1; transform: none; }
  @keyframes slide-in { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: none; } }
  .card.in .card-label { animation: slide-in .45s .18s both ease-out; }
  @keyframes float { from { transform: translateY(0) rotate(-3deg); } to { transform: translateY(-9px) rotate(3deg); } }
  .float { display: inline-block; animation: float 3.4s ease-in-out infinite alternate; }
  @keyframes pop { from { opacity: 0; transform: scale(.94); } to { opacity: 1; transform: none; } }
  .card.in .big { animation: pop .5s .1s both cubic-bezier(.2,1.3,.4,1); }

  @media (max-width: 600px) {
    main { width: min(100%% - 18px, 720px); padding-top: 16px; }
    .topbar { flex-wrap: nowrap; gap: 8px; }
    .badges { gap: 6px; }
    .home { padding: 12px 13px; font-size: 13px; white-space: nowrap; }
    .wc-badge { padding: 10px 11px; font-size: 12px; white-space: nowrap; }
    .stage { padding: 10px 10px; font-size: 10px; letter-spacing: .08em; }
    .photo, .card, .next { border-radius: 23px; }
    .card { padding: 20px; }
    .game { padding-left: 12px; padding-right: 12px; }
  }
  @media (max-width: 360px) {
    .topbar { flex-wrap: wrap; }
    .home { padding: 12px 11px; font-size: 12.5px; }
    .wc-badge { padding: 9px 9px; font-size: 11.5px; letter-spacing: 0; }
  }
%(extra)s
  /* ⚠️ 動きが苦手な人のための逃げ道。消さないこと */
  @media (prefers-reduced-motion: reduce) {
    html:not([data-motion="on"]) *, html:not([data-motion="on"]) *::before, html:not([data-motion="on"]) *::after {
      animation: none !important; transition: none !important;
    }
    html.js:not([data-motion="on"]) .card,
    html.js:not([data-motion="on"]) .game,
    html.js:not([data-motion="on"]) .next { opacity: 1 !important; transform: none !important; }
  }
  html[data-motion="off"] *, html[data-motion="off"] *::before, html[data-motion="off"] *::after { animation: none !important; transition: none !important; }
  html.js[data-motion="off"] .card,
  html.js[data-motion="off"] .game,
  html.js[data-motion="off"] .next { opacity: 1 !important; transform: none !important; }

  html[data-theme="dark"] .card { background: #22242f; border-color: rgba(255,255,255,.08); }
  html[data-theme="dark"] .home, html[data-theme="dark"] .wc-badge { background: #22242f; border-color: rgba(255,255,255,.1); }
  html[data-theme="dark"] h1 { color: #f4f0fa; text-shadow: none; }
  html[data-theme="dark"] .big { color: %(bigdark)s; }
  html[data-theme="dark"] .photo { background: #2a2c38; }
  html[data-theme="dark"] .game .btn:not(.ghost) { background: #2b2d3a; color: #f4f0fa; }
%(dark)s
  .next .next-title, .next .next-kicker { text-shadow: 0 1px 3px rgba(20,10,40,.28); }
"""

DRAFT_CSS = """<style id="draft-css">
  /* 📝 下書きの印（tools/draft.py）。本番に出すと消える */
  .draft-ribbon { display: flex; align-items: center; justify-content: center; gap: 8px; flex-wrap: wrap; margin: 0 0 14px;
    padding: 9px 14px; border-radius: 14px; background: repeating-linear-gradient(135deg, #fff4c2 0 14px, #ffeaa0 14px 28px);
    color: #5b4300; font-size: 13.5px; font-weight: 900; letter-spacing: .02em; text-align: center; }
  .draft-ribbon a { color: inherit; }
  .stage-draft { background: #ffd54a !important; color: #4a3500 !important; }
  /* 2026-09-30 幅390pxで「戻る」「○ words」「DRAFT」が6pxはみ出していた → 札を少し詰めて、それでも入らなければ折り返す */
  @media (max-width: 600px) { .topbar { flex-wrap: wrap; row-gap: 8px; } .stage-draft { padding-inline: 8px !important; letter-spacing: .04em !important; } }
  .draft-nav { display: grid; gap: 12px; margin-top: 26px; }
  .draft-next { display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 18px 20px; border-radius: 22px;
    text-decoration: none; color: #3a2d00; background: #fff1b8; border: 2px dashed rgba(120,90,0,.35); font-weight: 900; }
  .draft-next small { display: block; font-size: 12px; letter-spacing: .12em; opacity: .75; }
  .draft-next span.t { display: block; font-size: 17px; line-height: 1.4; }
  .draft-next small.en { margin-top: 4px; letter-spacing: 0; font-weight: 700; }
  .draft-back { justify-self: center; display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 12px 22px;
    border-radius: 999px; background: #fff; color: #232c48; border: 2px solid rgba(35,44,72,.14); text-decoration: none; font-weight: 900; }
  .draft-prod { justify-self: center; font-size: 13px; font-weight: 700; color: inherit; opacity: .6; }
  html[data-theme="dark"] .draft-next { background: #3a3320; color: #ffe9a8; border-color: rgba(255,233,168,.3); }
  html[data-theme="dark"] .draft-back { background: #22242f; color: #f4f0fa; border-color: rgba(255,255,255,.16); }
</style>
"""

REVEAL = """<script>
(function () {
  var items = [].slice.call(document.querySelectorAll('.card, .game, .next'));
  function showAll() { items.forEach(function (el) { el.classList.add('in'); }); }
  if (!('IntersectionObserver' in window)) { showAll(); return; }
  var seen = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); seen.unobserve(e.target); } });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  items.forEach(function (el) { seen.observe(el); });
  setTimeout(function () { if (!document.querySelector('.card.in, .next.in')) showAll(); }, 1600);
})();
</script>"""

CREDIT_EN = '📚 I wrote this from my notes on books and blogs I have read.'
CREDIT_JA = '📚 私が読んだ本やブログのメモから書きました。'
CARDNO = ["1枚目", "2枚目", "3枚目", "4枚目", "5枚目", "6枚目"]


def words_of(htmltext):
    t = re.sub(r"<[^>]+>", " ", htmltext)
    t = html.unescape(t)
    return [w for w in t.split() if re.search(r"[A-Za-z0-9]", w)]


def build(d):
    slug = d["slug"]
    out = ROOT / "draft" / slug
    (out / "i18n").mkdir(parents=True, exist_ok=True)
    # ---- cards
    s_no = 0
    smap, slines, cards_html, ja_text = [], [], [], {}
    nwords = 0
    for i, c in enumerate(d["cards"]):
        sents = c["s"]  # list of (en, ja)
        en = " ".join(e for e, _ in sents)
        nos = []
        for e, j in sents:
            s_no += 1
            nos.append(s_no)
            slines.append(f"S{s_no}. {j}")
            smap.append(f"S{s_no} → 使った（{CARDNO[i]}のカード{'・.big' if c.get('big') else ''}）")
        nwords += len(words_of(en))
        ja_text[html.unescape(re.sub(r'<[^>]+>', '', en))] = "".join(j for _, j in sents)
        ja_text[c["label"][0]] = c["label"][1]
        pcls = ' class="big"' if c.get("big") else ""
        extra = ("\n    " + c["extra"]) if c.get("extra") else ""
        cards_html.append(f"""  <section class="card">
    <div class="card-head">
      <span class="card-emoji" aria-hidden="true">{c['emoji']}</span>
      <span class="card-label">{c['label'][0]}</span>
    </div>
    <p{pcls}>{html.escape(en, quote=False)}</p>{extra}
  </section>
""")
    sec = round(nwords / 3)
    body = ""
    for i, ch in enumerate(cards_html):
        body += "\n" + ch
        if i + 1 == d["game_after"]:
            body += "\n  <!-- ⚡ 触って遊べる部品：" + d["game_note"] + " -->\n" + d["game_html"].strip("\n") + "\n"
    css = HEAD_CSS % dict(d["pal"], extra=d["css"], dark=d["dark"])
    title = d["title"][0]
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta name="robots" content="noindex, nofollow" /><!-- 📝 draft -->
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{html.escape(title, quote=False)}</title>
<link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="../../assets/favicon-180.png" />
<style>{css}</style>
<script>document.documentElement.className += " js";</script>
{DRAFT_CSS}</head>
<body>
<main>
  <!-- 📝 draft-ribbon:start（tools/draft.py） -->
  <div class="draft-ribbon" translate="no">📝 DRAFT · 下書き — まだ本番に出していません · <a href="../index.html">下書き一覧</a></div>
  <!-- 📝 draft-ribbon:end -->

  <div class="topbar">
    <a class="home" href="../index.html">← Back</a>
    <div class="badges">
      <div class="wc-badge">⚡ {nwords} words · {sec} sec</div>
      <div class="stage stage-draft">DRAFT</div>
    </div>
  </div>

  <div class="label"><span class="topic">🐧 EVERYDAY LIFE</span>⚡ {sec} SEC</div>
  <h1>{html.escape(title, quote=False)} <span class="float">{d['h1_emoji']}</span></h1>

  <figure class="photo">
    <img src="IMAGE:cover.jpg" alt="{html.escape(d['alt'])}" />
  </figure>
{body}
  <div class="credit">{html.escape(CREDIT_EN, quote=False)}</div>

  <!-- 📝 draft-nav:start（tools/draft.py） -->
  <nav class="draft-nav" translate="no">
    <a class="draft-back" href="../index.html">📝 ← 下書き一覧 / All drafts</a>
    <a class="draft-prod" href="../../index.html">本番のサイトへ ↗</a>
  </nav>
  <!-- 📝 draft-nav:end -->
</main>

{REVEAL}
<script>
/* ⚡ {d['game_note']}：JS は class・data-*・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
{d['js'].strip()}
</script>
</body>
</html>

<!-- SOURCE MAP
{chr(10).join(smap)}

本文（.card の中の <p>）の英文はすべて、上のどれかのS番号から訳したものです。
S番号に対応しない英文は1つもありません。

削った文：なし
追加した文：0
整理テキスト：card-label {len(d['cards'])}個 / h1 / 遊べる部品の文字 ← 本人の素材の要約・演出（word数対象外）
-->
"""
    (out / "index.html").write_text(page, encoding="utf-8")

    src = f"""# slug: {slug} / date: 2026-10-05 / words: {nwords}

## 出どころ

本人のメモ その3（幸せに生きるための考え方）の「{d['section']}」（2026-10-05 本人がチャットに貼った。本人の要望：本人の口調で、15秒で読めるようにかなり分割していい・元気がない時に見たい記事・面白くて可愛く・インタラクティブに・スマホファースト。「本当にゆっくりでいいから質を優先して」）
→ 本人の指示で、AI が本人の口調（一人称「私」・標準語）で書き直した。元の本やブログの著者の体験談は使っていない。

## 素材（日本語・1文ずつ S番号 を振る）

{chr(10).join(slines)}

## 中心メッセージ（1つだけ・1行で）

{d['message']}

## トーン

{d['tone']}

## 触って遊べるもの

{d['game_ja']}

## 表紙のプロンプト

{d['prompt']}

## 画像

images/cover.jpg — {d['alt']}
使った組み合わせ：{d['combo']}

## YouTube

なし

追加した文：0
"""
    (out / "source.md").write_text(src, encoding="utf-8")

    meta = {
        "title": title, "label": d["label"][0], "date": "2026-10-05", "length": "15sec",
        "thumbAlt": d["alt"], "place": "nagoya", "topic": "life", "seq": d["seq"], "room": "head",
        "series": "happy-psychology", "mood": d["mood"], "tags": d["tags"],
    }
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    text = {}
    text.update(ja_text)
    text["⚡ TRY IT"] = "⚡ やってみよう"
    text.update(d["ja"])
    text[CREDIT_EN] = CREDIT_JA
    ja = {"title": d["title"][1], "label": d["label"][1], "text": text}
    (out / "i18n" / "ja.json").write_text(json.dumps(ja, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # remove template leftovers
    print(f"{slug}: {nwords} words, {sec} sec")
