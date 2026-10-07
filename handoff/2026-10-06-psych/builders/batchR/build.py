#!/usr/bin/env python3
"""Batch R builder: R/<slug>.txt -> draft/<slug>/{index.html,source.md,meta.json,i18n/ja.json}

Sections ('@@name' lines):
  meta     json (title,label,seq,mood,tags,thumbAlt)
  ja_title / ja_label / h1emoji / section (e.g. 73「カーネギーの70枚のカード」)
  vars     CSS custom props (inside :root)
  css      article CSS
  dark     extra dark-mode CSS
  sents    'S1 | english | japanese'
  body     HTML with {S1} placeholders
  ui       'english ||| japanese'
  js       game script (IIFE)
  map      SOURCE MAP lines
  message / tone / game_ja / cover / combo
"""
import html, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path("/Users/ezakimasaaki/Desktop/html-works")

HEAD = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta name="robots" content="noindex, nofollow" /><!-- 📝 draft -->
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>__TITLE__</title>
<link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="../../assets/favicon-180.png" />
<style>
  /* 🐼 元気が出る心理学シリーズ その2（2026-10-05）。__TONE__ */
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
  .home { display: inline-block; min-height: 44px; padding: 12px 18px; border-radius: 999px; background: #fff; color: var(--a);
    border: 2px solid rgba(255,255,255,.9); font-size: 14px; text-decoration: none; box-shadow: 0 6px 16px rgba(60,50,90,.10); }
  .badges { display: flex; align-items: center; gap: 8px; }
  .wc-badge { padding: 10px 16px; border-radius: 999px; background: #fff; border: 2px solid rgba(255,255,255,.9);
    color: var(--muted); font-size: 13px; letter-spacing: .04em; box-shadow: 0 6px 16px rgba(60,50,90,.08); }
  .stage { padding: 10px 13px; border-radius: 999px; font-size: 11px; font-weight: 900; letter-spacing: .12em; white-space: nowrap;
    box-shadow: 0 6px 16px rgba(60,50,90,.16); }
  .stage-public { background: #23c98a; color: #04331d; }

  .label { color: var(--a); font-size: 13px; font-weight: 800; letter-spacing: .14em; margin-bottom: 16px; }
  .label .topic { display: inline-block; margin-right: 10px; padding: 5px 12px; border-radius: 999px; background: var(--a); color: #fff;
    font-size: 11.5px; font-weight: 900; letter-spacing: .12em; }
  h1 { margin: 0 0 22px; color: var(--ink); font-size: clamp(32px, 6.4vw, 56px); line-height: 1.08; letter-spacing: -.04em;
    text-wrap: balance; text-shadow: 0 4px 0 rgba(255,255,255,.75); }

  .photo { margin: 0 0 24px; overflow: hidden; background: var(--photo); border: 7px solid rgba(255,255,255,.8); border-radius: 32px;
    box-shadow: var(--shadow); transform: rotate(-.35deg); }
  .photo img { display: block; width: 100%; height: auto; }

  .card { position: relative; margin-top: 18px; padding: 24px 26px; background: var(--card); border: 2px solid rgba(255,255,255,.92);
    border-radius: var(--round); box-shadow: 0 12px 32px rgba(60,50,90,.09); }
  .card-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
  .card-emoji { font-size: 26px; line-height: 1; }
  .card-label { font-size: 12.5px; font-weight: 900; letter-spacing: .16em; color: var(--a); text-transform: uppercase; }
  p { margin: 0; font-family: "Trebuchet MS", "Avenir Next Rounded", sans-serif; font-size: clamp(17px, 2.4vw, 21px); line-height: 1.72; font-weight: 700; }
  p + p { margin-top: 8px; }
  .big { font-size: clamp(23px, 4vw, 32px); font-weight: 850; line-height: 1.42; color: var(--bigc);
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif; }

  /* ════ ⚡ 触って遊べる部品（共通）════
     文字はぜんぶ HTML に置いて、JS は class・data-*・数字・絵文字だけを変える（訳がそのまま効くように） */
  .game { position: relative; overflow: hidden; margin-top: 26px; padding: 22px 16px 20px; border-radius: 30px; text-align: center; color: #fff;
    background: linear-gradient(150deg, var(--g1) 0%, var(--g2) 55%, var(--g3) 100%); box-shadow: var(--shadow); }
  .game-kicker { font-size: 12px; font-weight: 900; letter-spacing: .18em; opacity: .92; }
  .game-title { margin-top: 4px; font-size: clamp(21px, 4.6vw, 28px); font-weight: 900; line-height: 1.25; }
  .game-sub { margin: 6px auto 0; max-width: 440px; font-size: 14.5px; font-weight: 800; line-height: 1.5; opacity: .95; }
  .gbtn { display: inline-flex; align-items: center; justify-content: center; gap: 6px; min-height: 56px; padding: 12px 18px; border: 0; border-radius: 999px;
    cursor: pointer; font: inherit; font-size: 17px; font-weight: 900; line-height: 1.25; color: var(--btnink); background: #fff;
    box-shadow: 0 7px 0 var(--btnshadow), 0 14px 24px rgba(0,0,0,.16); transition: transform .08s ease, box-shadow .08s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; }
  .gbtn:active { transform: translateY(6px); box-shadow: 0 1px 0 var(--btnshadow), 0 5px 12px rgba(0,0,0,.16); }
  .gbtn:focus-visible, .again:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .gbtn[disabled] { opacity: .45; cursor: default; }
  .again { display: inline-flex; align-items: center; justify-content: center; min-height: 48px; margin-top: 14px; padding: 10px 22px; border-radius: 999px;
    border: 2px solid rgba(255,255,255,.7); background: rgba(255,255,255,.16); color: #fff; font: inherit; font-size: 15px; font-weight: 900; cursor: pointer;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
  .gmeter { position: relative; height: 16px; margin: 14px auto 0; max-width: 380px; border-radius: 999px; background: rgba(255,255,255,.25); overflow: hidden; }
  .gmeter i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #fff; transition: width .45s cubic-bezier(.2,1.2,.4,1); }
  .gmeter-label { display: flex; justify-content: space-between; gap: 8px; max-width: 380px; margin: 5px auto 0; font-size: 12px; font-weight: 900; opacity: .9; }
  @keyframes shake { 20% { transform: translateX(-5px); } 40% { transform: translateX(5px); } 60% { transform: translateX(-3px); } 80% { transform: translateX(2px); } }
  @keyframes boing { 0% { transform: scale(1); } 35% { transform: scale(1.22) rotate(-4deg); } 70% { transform: scale(.94) rotate(2deg); } 100% { transform: scale(1); } }
  @keyframes popin { from { opacity: 0; transform: scale(.7); } to { opacity: 1; transform: none; } }
  .shake { animation: shake .4s ease; }
  .boing { animation: boing .45s ease; }

__CSS__

  .credit { margin-top: 22px; text-align: center; font-size: 13px; font-weight: 800; color: var(--muted); }

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
    .photo, .card { border-radius: 23px; }
    .card { padding: 20px; }
    .game { padding: 20px 12px 18px; border-radius: 26px; }
  }
  @media (max-width: 360px) {
    .topbar { flex-wrap: wrap; }
    .home { padding: 12px 11px; font-size: 12.5px; }
    .wc-badge { padding: 9px 9px; font-size: 11.5px; letter-spacing: 0; }
    .gbtn { font-size: 15.5px; padding: 12px 14px; }
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

  html[data-theme="dark"] .card { background: #22242f; border-color: rgba(255,255,255,.08); }
  html[data-theme="dark"] .home, html[data-theme="dark"] .wc-badge { background: #22242f; border-color: rgba(255,255,255,.1); }
  html[data-theme="dark"] h1 { color: #f4f0fa; text-shadow: none; }
  html[data-theme="dark"] .big { color: var(--bigdark); }
  html[data-theme="dark"] .photo { background: #2a2c38; }
  html[data-theme="dark"] .gbtn { background: #f1edf7; }
__DARK__
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
__BODY__
  <div class="credit">📚 I learned this from the Japanese blog "Panda no Ondo".</div>
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

SOURCE = '''# slug: {slug} / date: 2026-10-05 / words: {words}

## 出どころ

本人がメモした「パンダの温度（しあわせ心理学）」の「本人のメモ その2（未読だった375記事の学び）」の {section}（2026-10-05 本人がチャットに貼った。本人：「元気がない時に見たい記事。面白くて可愛く。インタラクティブに」「本当にゆっくりでいいから質を優先して」）
→ 本人の指示で、AI が本人の口調（一人称「私」・標準語）で書き直した。元のブログの著者の体験談は使っていない。

## 素材（日本語・1文ずつ S番号 を振る）

{sents}

## 中心メッセージ（1つだけ・1行で）

{message}

## トーン

{tone}

## 触って遊べるもの

{game_ja}

## 表紙のプロンプト

{cover}

## 画像

images/cover.jpg — {alt}
使った組み合わせ：{combo}

## YouTube

なし

追加した文：0
'''


def sections(text):
    out, cur = {}, None
    for line in text.split("\n"):
        m = re.match(r"^@@(\w+)\s*$", line)
        if m:
            cur = m.group(1); out[cur] = []
        elif cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip("\n") for k, v in out.items()}


def words_of(htmldoc):
    body = htmldoc.split("<body", 1)[-1]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    text = " ".join(re.findall(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I))
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def build(path):
    slug = path.stem
    s = sections(path.read_text(encoding="utf-8"))
    meta = json.loads(s["meta"])
    sents = []
    for line in s["sents"].splitlines():
        if not line.strip():
            continue
        k, en, ja = [x.strip() for x in line.split("|", 2)]
        sents.append((k, en, ja))
    body = s["body"]
    for k, en, ja in sents:
        if "{" + k + "}" not in body:
            sys.exit(f"{slug}: {k} not used in body")
        body = body.replace("{" + k + "}", html.escape(en, quote=False))
    if re.search(r"\{S\d+\}", body):
        sys.exit(f"{slug}: unknown placeholder")
    ui = []
    for line in s.get("ui", "").splitlines():
        if not line.strip():
            continue
        en, ja = [x.strip() for x in line.split("|||", 1)]
        ui.append((en, ja))
    doc = HEAD
    rep = {
        "__TITLE__": html.escape(meta["title"], quote=False),
        "__TONE__": s["tone"].splitlines()[-1].strip(),
        "__VARS__": "\n".join("    " + l.strip() for l in s["vars"].splitlines() if l.strip()),
        "__CSS__": s["css"],
        "__DARK__": s.get("dark", ""),
        "__H1EMOJI__": s["h1emoji"].strip(),
        "__ALT__": html.escape(meta["thumbAlt"]),
        "__BODY__": "\n" + body + "\n",
        "__JS__": s["js"],
        "__MAP__": s["map"],
    }
    for k, v in rep.items():
        doc = doc.replace(k, v)
    n = len(words_of(doc))
    sec = round(n / 3)
    doc = doc.replace("__WORDS__", str(n)).replace("__SEC__", str(sec))

    d = ROOT / "draft" / slug
    (d / "i18n").mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(doc, encoding="utf-8")

    text = {}
    labels = re.findall(r'class="card-label"[^>]*>(.*?)</', body)
    for k, en, ja in sents:
        text[en] = ja
    for en, ja in ui:
        if en in text and text[en] != ja:
            sys.exit(f"{slug}: dup ui {en}")
        text[en] = ja
    text["⚡ TRY IT"] = "⚡ やってみよう"
    text["DRAFT"] = "下書き"
    text['📚 I learned this from the Japanese blog "Panda no Ondo".'] = "📚 日本のブログ「パンダの温度」で知りました。"
    for l in labels:
        if html.unescape(l) not in text:
            sys.exit(f"{slug}: label without ja: {l}")
    ja = {"title": s["ja_title"].strip(), "label": s["ja_label"].strip(), "text": text}
    (d / "i18n" / "ja.json").write_text(json.dumps(ja, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    m = {"title": meta["title"], "label": meta["label"], "date": "2026-10-05", "length": "15sec",
         "thumbAlt": meta["thumbAlt"], "place": "nagoya", "topic": "life", "seq": meta["seq"], "room": "head",
         "series": "happy-psychology", "mood": meta["mood"], "tags": meta["tags"]}
    (d / "meta.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    src = SOURCE.format(slug=slug, words=n, section=s["section"].strip(),
                        sents="\n".join(f"{k}. {ja}" for k, en, ja in sents),
                        message=s["message"].strip(), tone=s["tone"].strip(), game_ja=s["game_ja"].strip(),
                        cover=s["cover"].strip(), alt=meta["thumbAlt"], combo=s["combo"].strip())
    (d / "source.md").write_text(src, encoding="utf-8")

    # js syntax file
    (HERE / "js").mkdir(exist_ok=True)
    (HERE / "js" / f"{slug}.js").write_text(s["js"], encoding="utf-8")
    title_words = len(meta["title"].split())
    print(f"{slug}: {n} words / {sec} sec / title {title_words} words / labels {labels}")


if __name__ == "__main__":
    targets = sys.argv[1:] or [p.stem for p in sorted((HERE / "R").glob("*.txt"))]
    for t in targets:
        build(HERE / "R" / f"{t}.txt")
