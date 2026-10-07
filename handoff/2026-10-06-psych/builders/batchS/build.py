#!/usr/bin/env python3
"""Batch S builder: one spec file per article (A/<slug>.txt) -> draft/<slug>/{index.html,source.md,meta.json,i18n/ja.json}.

Spec file sections start with a line '@@name'. Sections:
  meta      json object (title,label,seq,mood,tags,thumbAlt)  -- title = h1 = <title>
  ja_title  Japanese title
  ja_label  Japanese short label
  h1emoji   emoji after the h1
  section   notes section id (e.g. 1-1「…」)
  vars      CSS custom properties (inside :root)
  css       article CSS
  sents     lines 'S1 | english | japanese'
  body      HTML with {S1} placeholders (cards + game)
  ui        lines 'english ||| japanese' for every other English text node
  js        game script body (already an IIFE)
  map       SOURCE MAP lines (S1 → …)
  message   central message (ja)
  tone      tone lines (ja)
  game_ja   game description (ja)
  cover     cover prompt (English)
  combo     "使った組み合わせ" line (ja)
"""
import html, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path("/Users/ezakimasaaki/Desktop/html-works")

SKEL_HEAD = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta name="robots" content="noindex, nofollow" /><!-- 📝 draft -->
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>__TITLE__</title>
<link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="../../assets/favicon-180.png" />
<style>
  /* 🐼 元気が出る心理学シリーズ（2026-10-05）。真面目な話 → ポップに（トーン反転） */
  :root {
    --card: rgba(255,255,255,.95);
    --round: 28px;
__VARS__
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; color: var(--text);
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif;
    background:
      radial-gradient(circle at 10% 6%, var(--glow1), transparent 26%),
      radial-gradient(circle at 92% 18%, var(--glow2), transparent 28%),
      radial-gradient(circle at 50% 100%, var(--glow3), transparent 36%),
      var(--bg);
  }
  main { width: min(720px, calc(100% - 24px)); margin: 0 auto; padding: 22px 0 70px; }

  .topbar { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
  .home { display: inline-block; min-height: 44px; padding: 12px 18px; border-radius: 999px; background: #fff; color: var(--accent);
    border: 2px solid rgba(255,255,255,.9); font-size: 14px; text-decoration: none; box-shadow: 0 6px 16px rgba(60,40,90,.10); }
  .badges { display: flex; align-items: center; gap: 8px; }
  .wc-badge { padding: 10px 16px; border-radius: 999px; background: #fff; border: 2px solid rgba(255,255,255,.9);
    color: var(--muted); font-size: 13px; letter-spacing: .04em; box-shadow: 0 6px 16px rgba(60,40,90,.08); }
  .stage { padding: 10px 13px; border-radius: 999px; font-size: 11px; font-weight: 900; letter-spacing: .12em; white-space: nowrap;
    box-shadow: 0 6px 16px rgba(60,40,90,.16); }
  .stage-public { background: #23c98a; color: #04331d; }

  .label { color: var(--accent); font-size: 13px; font-weight: 800; letter-spacing: .14em; margin-bottom: 16px; }
  .label .topic { display: inline-block; margin-right: 10px; padding: 5px 12px; border-radius: 999px; background: var(--accent); color: #fff;
    font-size: 11.5px; font-weight: 900; letter-spacing: .12em; }
  h1 { margin: 0 0 22px; color: var(--h1); font-size: clamp(32px, 6.4vw, 56px); line-height: 1.08; letter-spacing: -.04em;
    text-wrap: balance; text-shadow: 0 4px 0 rgba(255,255,255,.75); }

  .photo { margin: 0 0 24px; overflow: hidden; background: var(--photo-bg); border: 7px solid rgba(255,255,255,.8); border-radius: 32px;
    box-shadow: var(--shadow); transform: rotate(-.35deg); }
  .photo img { display: block; width: 100%; height: auto; }

  .card { position: relative; margin-top: 18px; padding: 24px 26px; background: var(--card); border: 2px solid rgba(255,255,255,.92);
    border-radius: var(--round); box-shadow: 0 12px 32px rgba(60,40,90,.09); }
  .card-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
  .card-emoji { font-size: 26px; line-height: 1; }
  .card-label { font-size: 12.5px; font-weight: 900; letter-spacing: .16em; color: var(--accent); text-transform: uppercase; }
  p { margin: 0; font-family: "Trebuchet MS", "Avenir Next Rounded", sans-serif; font-size: clamp(17px, 2.4vw, 21px); line-height: 1.72; font-weight: 700; }
  .big { font-size: clamp(23px, 4vw, 32px); font-weight: 850; line-height: 1.42; color: var(--big);
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif; }

  /* ════ ⚡ 触って遊べる部品の共通の形 ════
     文字はぜんぶ HTML に置いて、JS は class / data-* / 数字 / 絵文字だけを変える（訳がそのまま効くように） */
  .game { margin-top: 26px; padding: 22px 16px 20px; border-radius: 30px; text-align: center; color: #fff;
    background: linear-gradient(150deg, var(--g1) 0%, var(--g2) 55%, var(--g3) 100%); box-shadow: var(--shadow); overflow: hidden; position: relative; }
  .game-kicker { font-size: 12px; font-weight: 900; letter-spacing: .18em; opacity: .92; }
  .game-title { margin-top: 4px; font-size: clamp(21px, 4.6vw, 28px); font-weight: 900; line-height: 1.25; text-shadow: 0 2px 0 rgba(0,0,0,.12); }
  .game-hint { margin-top: 6px; font-size: 14.5px; font-weight: 800; opacity: .95; line-height: 1.45; }
  .gbtn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 52px; padding: 12px 22px; border: 0; border-radius: 999px;
    cursor: pointer; font: inherit; font-size: 17px; font-weight: 900; line-height: 1.25; color: var(--btn-text); background: #fff;
    box-shadow: 0 6px 0 rgba(0,0,0,.16), 0 12px 22px rgba(0,0,0,.12); transition: transform .08s ease, box-shadow .08s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; max-width: 100%; }
  .gbtn:active { transform: translateY(5px); box-shadow: 0 1px 0 rgba(0,0,0,.16), 0 4px 10px rgba(0,0,0,.12); }
  .gbtn:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .gbtn.pop { background: var(--pop); color: var(--pop-text); }
  .gbtn.ghost { background: rgba(255,255,255,.2); color: #fff; box-shadow: 0 5px 0 rgba(0,0,0,.14); min-height: 48px; font-size: 15px; }
  .gbtn[disabled] { opacity: .45; cursor: default; }
  .again-row { margin-top: 14px; }
  @keyframes bounce-in { 0% { transform: scale(.4); opacity: 0; } 60% { transform: scale(1.15); opacity: 1; } 100% { transform: scale(1); } }
  @keyframes wiggle { 0%,100% { transform: rotate(0); } 25% { transform: rotate(-9deg); } 75% { transform: rotate(9deg); } }
  @keyframes shake { 20% { transform: translateX(-5px); } 40% { transform: translateX(5px); } 60% { transform: translateX(-3px); } 80% { transform: translateX(2px); } }
  @keyframes hop { 0%,100% { transform: translateY(0); } 40% { transform: translateY(-14px); } }

__CSS__

  .credit { margin-top: 22px; text-align: center; font-size: 13px; font-weight: 800; color: var(--muted); }

  .next { display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-top: 34px; min-height: 44px; padding: 20px 24px;
    border-radius: var(--round); text-decoration: none; background: linear-gradient(135deg, var(--accent), var(--accent2)); color: #fff; box-shadow: var(--shadow); }
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
    main { width: min(100% - 18px, 720px); padding-top: 16px; }
    .topbar { flex-wrap: nowrap; gap: 8px; }
    .badges { gap: 6px; }
    .home { padding: 12px 13px; font-size: 13px; white-space: nowrap; }
    .wc-badge { padding: 10px 11px; font-size: 12px; white-space: nowrap; }
    .stage { padding: 10px 10px; font-size: 10px; letter-spacing: .08em; }
    .photo, .card, .next { border-radius: 23px; }
    .card { padding: 20px; }
    .game { padding: 20px 12px 18px; border-radius: 26px; }
  }
  @media (max-width: 360px) {
    .topbar { flex-wrap: wrap; }
    .home { padding: 12px 11px; font-size: 12.5px; }
    .wc-badge { padding: 9px 9px; font-size: 11.5px; letter-spacing: 0; }
  }

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

  html[data-theme="dark"] body { background: #17181f; color: #ece8f4; }
  html[data-theme="dark"] .card { background: #22242f; border-color: rgba(255,255,255,.08); color: #ece8f4; }
  html[data-theme="dark"] .home, html[data-theme="dark"] .wc-badge { background: #22242f; border-color: rgba(255,255,255,.1); }
  html[data-theme="dark"] h1 { color: #f4f0fa; text-shadow: none; }
  html[data-theme="dark"] .big { color: var(--big-dark); }
  html[data-theme="dark"] .label { color: var(--big-dark); }
  html[data-theme="dark"] .card-label { color: var(--big-dark); }
  html[data-theme="dark"] .photo { background: #2c2e3b; }
__DARK__
  .next .next-title, .next .next-kicker { text-shadow: 0 1px 3px rgba(20,10,40,.28); }
</style>
<script>document.documentElement.className += " js";</script>
<style id="draft-css">
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
</head>
<body>
<main>
  <!-- 📝 draft-ribbon:start（tools/draft.py） -->
  <div class="draft-ribbon" translate="no">📝 DRAFT · 下書き — まだ本番に出していません · <a href="../index.html">下書き一覧</a></div>
  <!-- 📝 draft-ribbon:end -->

  <div class="topbar">
    <a class="home" href="../index.html">← Back</a>
    <div class="badges">
      <div class="wc-badge">⚡ __WORDS__ words · __SEC__ sec</div>
      <div class="stage stage-draft">DRAFT</div>
    </div>
  </div>

  <div class="label"><span class="topic">🐧 EVERYDAY LIFE</span>⚡ __SEC__ SEC</div>
  <h1>__TITLE__ <span class="float">__H1EMOJI__</span></h1>

  <figure class="photo">
    <img src="IMAGE:cover.jpg" alt="__ALT__" />
  </figure>
'''

SKEL_TAIL = r'''
  <div class="credit">📚 I learned this from the Japanese blog "Panda no Ondo".</div>


  <!-- 📝 draft-nav:start（tools/draft.py） -->
  <nav class="draft-nav" translate="no">
    <a class="draft-back" href="../index.html">📝 ← 下書き一覧 / All drafts</a>
    <a class="draft-prod" href="../../index.html">本番のサイトへ ↗</a>
  </nav>
  <!-- 📝 draft-nav:end -->
</main>

<script>
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
</script>
<script>
__JS__
</script>
</body>
</html>

<!-- SOURCE MAP
__MAP__

本文（.card の中の <p>）の英文はすべて、上のどれかのS番号から訳したものです。
S番号に対応しない英文は1つもありません。

削った文：なし
追加した文：0
整理テキスト：card-label / h1 / 遊べる部品の文字 ← 本人の素材の要約・演出（word数対象外）
-->
'''

SOURCE = '''# slug: __SLUG__ / date: 2026-10-05 / words: __WORDS__

## 出どころ

本人がメモした「パンダの温度（しあわせ心理学）」の「本人のメモ その2（未読だった375記事の学び）」の 番号 __SECTION__（2026-10-05 本人がチャットに貼った。本人：「私っぽい文章にして、15秒で読めるようにかなり分割していい。元気がない時に見たい記事。面白くて可愛く。インタラクティブに」「本当にゆっくりでいいから質を優先して」）
→ 本人の指示で、AI が本人の口調（一人称「私」・標準語）で書き直した。元のブログの著者の体験談は使っていない。

## 素材（日本語・1文ずつ S番号 を振る）

__SLINES__

## 中心メッセージ（1つだけ・1行で）

__MESSAGE__

## トーン

__TONE__

## 触って遊べるもの

__GAME__

## 画像

images/cover.jpg — __ALT__
使った組み合わせ：__COMBO__

## 表紙のプロンプト

__COVER__

## YouTube

なし

追加した文：0
'''


def sections(text):
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^@@(\w+)\s*$", line)
        if m:
            cur = m.group(1); out[cur] = []
            continue
        if cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip("\n") for k, v in out.items()}


def body_words(doc):
    body = doc.split("<body", 1)[-1]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    text = " ".join(re.findall(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I))
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def build(slug):
    s = sections((HERE / "S" / f"{slug}.txt").read_text(encoding="utf-8"))
    meta_in = json.loads(s["meta"])
    title = meta_in["title"]
    sents = []
    for line in s["sents"].splitlines():
        if not line.strip():
            continue
        sid, en, ja = [x.strip() for x in line.split("|", 2)]
        sents.append((sid, en, ja))
    body = s["body"]
    for sid, en, ja in sents:
        if "{" + sid + "}" not in body:
            raise SystemExit(f"{slug}: {sid} not used in body")
        body = body.replace("{" + sid + "}", html.escape(en, quote=False))
    if re.search(r"\{S\d+\}", body):
        raise SystemExit(f"{slug}: unknown placeholder")
    doc = (SKEL_HEAD.replace("__TITLE__", html.escape(title, quote=False))
           .replace("__VARS__", s["vars"]).replace("__CSS__", s["css"]).replace("__DARK__", s.get("dark", ""))
           .replace("__H1EMOJI__", s["h1emoji"]).replace("__ALT__", html.escape(meta_in["thumbAlt"])))
    doc = doc + "\n" + body + "\n" + SKEL_TAIL.replace("__JS__", s["js"]).replace("__MAP__", s["map"])
    n = len(body_words(doc)); sec = round(n / 3)
    doc = doc.replace("__WORDS__", str(n)).replace("__SEC__", str(sec))
    d = ROOT / "draft" / slug
    (d / "i18n").mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(doc, encoding="utf-8")

    meta = {"title": title, "label": meta_in["label"], "date": "2026-10-05", "length": "15sec",
            "thumbAlt": meta_in["thumbAlt"], "place": "nagoya", "topic": "life", "seq": meta_in["seq"],
            "room": "head", "series": "happy-psychology", "mood": meta_in["mood"], "tags": meta_in["tags"]}
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    text = {}
    for line in s["ui"].splitlines():
        if not line.strip():
            continue
        en, ja = [x.strip() for x in line.split("|||", 1)]
        text[en] = ja
    for sid, en, ja in sents:
        text[en] = ja
    sd = {sid: (en, ja) for sid, en, ja in sents}
    for inner in re.findall(r"<p\b[^>]*>(.*?)</p>", s["body"], flags=re.S):
        ids = re.findall(r"\{(S\d+)\}", inner)
        if len(ids) > 1:
            text[" ".join(sd[i][0] for i in ids)] = "".join(sd[i][1] for i in ids)
    text["DRAFT"] = "下書き"
    text["📚 I learned this from the Japanese blog \"Panda no Ondo\"."] = "📚 日本のブログ「パンダの温度」で知りました。"
    ja_doc = {"title": s["ja_title"], "label": s["ja_label"], "text": text}
    (d / "i18n" / "ja.json").write_text(json.dumps(ja_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    src = (SOURCE.replace("__SLUG__", slug).replace("__WORDS__", str(n)).replace("__SECTION__", s["section"])
           .replace("__SLINES__", "\n".join(f"{sid}. {ja}" for sid, en, ja in sents))
           .replace("__MESSAGE__", s["message"]).replace("__TONE__", s["tone"]).replace("__GAME__", s["game_ja"])
           .replace("__ALT__", meta_in["thumbAlt"]).replace("__COMBO__", s["combo"]).replace("__COVER__", s["cover"]))
    (d / "source.md").write_text(src, encoding="utf-8")

    (HERE / "js").mkdir(exist_ok=True)
    (HERE / "js" / f"{slug}.js").write_text(s["js"], encoding="utf-8")
    print(f"{slug}: {n} words, {sec} sec, {len(sents)} sentences, {len(text)} ja entries")


if __name__ == "__main__":
    for slug in sys.argv[1:]:
        build(slug)
