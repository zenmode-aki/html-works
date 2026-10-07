# Batch Z generator: shared page skeleton (copied from draft/say-yes-in-a-flash) + per-article parts.
import json, os, re

REPO = '/Users/ezakimasaaki/Desktop/html-works'
CREDIT_EN = '📚 I wrote this from my notes on books and blogs I have read.'
CREDIT_JA = '📚 私が読んだ本やブログのメモから書きました。'

HEAD_CSS = r'''
  :root {
    --bg: %(bg)s;
    --card: rgba(255,255,255,.95);
    --text: #2f2a3a;
    --muted: #776f86;
    --c1: %(c1)s;
    --c2: %(c2)s;
    --sun: %(sun)s;
    --c1d: %(c1d)s;
    --game: %(game)s;
    --shadow: 0 20px 55px rgba(70,60,120,.16);
    --round: 28px;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; color: var(--text);
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif;
    background:
      radial-gradient(circle at 10%% 6%%, %(glow1)s, transparent 26%%),
      radial-gradient(circle at 92%% 18%%, %(glow2)s, transparent 28%%),
      radial-gradient(circle at 50%% 100%%, %(glow3)s, transparent 36%%),
      var(--bg);
  }
  main { width: min(720px, calc(100%% - 24px)); margin: 0 auto; padding: 22px 0 70px; }

  .topbar { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
  .home { display: inline-block; min-height: 44px; padding: 12px 18px; border-radius: 999px; background: #fff; color: var(--c1d);
    border: 2px solid rgba(255,255,255,.9); font-size: 14px; text-decoration: none; box-shadow: 0 6px 16px rgba(70,60,120,.10); }
  .badges { display: flex; align-items: center; gap: 8px; }
  .wc-badge { padding: 10px 16px; border-radius: 999px; background: #fff; border: 2px solid rgba(255,255,255,.9);
    color: var(--muted); font-size: 13px; letter-spacing: .04em; box-shadow: 0 6px 16px rgba(70,60,120,.08); }
  .stage { padding: 10px 13px; border-radius: 999px; font-size: 11px; font-weight: 900; letter-spacing: .12em; white-space: nowrap;
    box-shadow: 0 6px 16px rgba(70,60,120,.16); }
  .stage-public { background: #23c98a; color: #04331d; }

  .label { color: var(--c1d); font-size: 13px; font-weight: 800; letter-spacing: .14em; margin-bottom: 16px; }
  .label .topic { display: inline-block; margin-right: 10px; padding: 5px 12px; border-radius: 999px; background: var(--c1d); color: #fff;
    font-size: 11.5px; font-weight: 900; letter-spacing: .12em; }
  h1 { margin: 0 0 22px; color: #2a2440; font-size: clamp(32px, 6.4vw, 56px); line-height: 1.08; letter-spacing: -.04em;
    text-wrap: balance; text-shadow: 0 4px 0 rgba(255,255,255,.75); }

  .photo { margin: 0 0 24px; overflow: hidden; background: %(photobg)s; border: 7px solid rgba(255,255,255,.8); border-radius: 32px;
    box-shadow: var(--shadow); transform: rotate(-.35deg); }
  .photo img { display: block; width: 100%%; height: auto; }

  .card { position: relative; margin-top: 18px; padding: 24px 26px; background: var(--card); border: 2px solid rgba(255,255,255,.92);
    border-radius: var(--round); box-shadow: 0 12px 32px rgba(70,60,120,.09); }
  .card-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
  .card-emoji { font-size: 26px; line-height: 1; }
  .card-label { font-size: 12.5px; font-weight: 900; letter-spacing: .16em; color: var(--c1d); text-transform: uppercase; }
  p { margin: 0; font-family: "Trebuchet MS", "Avenir Next Rounded", sans-serif; font-size: clamp(17px, 2.4vw, 21px); line-height: 1.72; font-weight: 700; }
  p + p { margin-top: 10px; }
  .big { font-size: clamp(23px, 4vw, 32px); font-weight: 900; line-height: 1.42; color: var(--c1d);
    font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", sans-serif; }

  /* ════ ⚡ 触って遊べる部品の共通（文字は HTML。JS は class・data・数字・絵文字だけ）════ */
  .game { margin-top: 26px; padding: 22px 16px 20px; border-radius: 30px; text-align: center; color: #fff;
    background: var(--game); box-shadow: var(--shadow); overflow: hidden; position: relative; }
  .game-kicker { font-size: 12px; font-weight: 900; letter-spacing: .18em; opacity: .92; }
  .game-title { margin-top: 4px; font-size: clamp(21px, 4.6vw, 28px); font-weight: 900; line-height: 1.25; }
  .game-hint { margin-top: 6px; font-size: 15px; font-weight: 800; opacity: .95; line-height: 1.45; }
  .gbtn { display: inline-flex; align-items: center; justify-content: center; min-height: 56px; padding: 12px 22px; border: 0; border-radius: 999px;
    font: inherit; font-size: 18px; font-weight: 900; color: #2b2100; background: var(--sun); cursor: pointer;
    box-shadow: 0 6px 0 rgba(0,0,0,.2), 0 12px 22px rgba(0,0,0,.14); transition: transform .08s ease, box-shadow .08s ease, opacity .2s;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; line-height: 1.25; }
  .gbtn:active { transform: translateY(4px); box-shadow: 0 2px 0 rgba(0,0,0,.2), 0 5px 10px rgba(0,0,0,.14); }
  .gbtn:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .gbtn.ghost { background: rgba(255,255,255,.94); color: var(--c1d); font-size: 16px; min-height: 50px; }
  .gbtn[disabled] { opacity: .45; cursor: default; }
  .gbtn.wide { width: min(340px, 100%%); }
  .g-row { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 14px; }
  .msg { margin-top: 14px; min-height: 52px; font-size: 17px; font-weight: 900; line-height: 1.45; }
  .msg > div { display: none; }
  @keyframes shake { 20%% { transform: translateX(-5px); } 40%% { transform: translateX(5px); } 60%% { transform: translateX(-3px); } 80%% { transform: translateX(2px); } }
  @keyframes popin { from { opacity: 0; transform: scale(.8); } to { opacity: 1; transform: none; } }
  .msg > div { animation: popin .35s cubic-bezier(.2,1.4,.4,1) both; }

%(extra_css)s

  .credit { margin-top: 22px; text-align: center; font-size: 13px; font-weight: 800; color: var(--muted); }

  .next { display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-top: 34px; min-height: 44px; padding: 20px 24px;
    border-radius: var(--round); text-decoration: none; background: linear-gradient(135deg, var(--c1), var(--c2)); color: #fff; box-shadow: var(--shadow); }
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

  html[data-theme="dark"] .card { background: #22242f; border-color: rgba(255,255,255,.08); }
  html[data-theme="dark"] .home, html[data-theme="dark"] .wc-badge { background: #22242f; border-color: rgba(255,255,255,.1); }
  html[data-theme="dark"] h1 { color: #f4f0fa; text-shadow: none; }
  html[data-theme="dark"] .big { color: %(c1l)s; }
  html[data-theme="dark"] .gbtn.ghost { background: #2a2c38; color: #f4f0fa; }
%(dark_css)s
  .next .next-title, .next .next-kicker { text-shadow: 0 1px 3px rgba(20,10,40,.28); }
'''

DRAFT_CSS = r'''<style id="draft-css">
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
</style>'''

REVEAL_JS = r'''<script>
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
</script>'''

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def tr_markup(html, table):
    """{{en|ja}} -> en, and record ja."""
    def rep(m):
        en, ja = m.group(1), m.group(2)
        table[en] = ja
        return en
    return re.sub(r'\{\{(.+?)\|(.+?)\}\}', rep, html, flags=re.S)

def build(a):
    slug = a['slug']; d = os.path.join(REPO, 'draft', slug)
    os.makedirs(os.path.join(d, 'i18n'), exist_ok=True)
    ja = {}
    # cards
    S = a['S']  # list of (ja, en)
    parts = []; smap = []; cardno = 0
    for item in a['layout']:
        if item == 'GAME':
            parts.append('  <!-- ⚡ 触って遊べる部品：' + a['game_name'] + ' -->\n' + tr_markup(a['game_html'], ja))
            continue
        emoji, lab_en, lab_ja, sids, extra = item
        cardno += 1
        ja[lab_en] = lab_ja
        ps = []
        for sid in sids:
            big = sid.startswith('!'); n = int(sid.strip('!'))
            jtxt, etxt = S[n - 1]
            ja[etxt] = jtxt
            ps.append('    <p%s>%s</p>' % (' class="big"' if big else '', esc(etxt)))
            smap.append('S%d → 使った（%d枚目のカード%s）' % (n, cardno, '・.big' if big else ''))
        ex = tr_markup(extra, ja) if extra else ''
        parts.append('''  <section class="card">
    <div class="card-head">
      <span class="card-emoji" aria-hidden="true">%s</span>
      <span class="card-label">%s</span>
    </div>
%s%s
  </section>''' % (emoji, lab_en, '\n'.join(ps), ('\n' + ex) if ex else ''))
    smap.sort(key=lambda s: int(s.split(' ')[0][1:]))
    ja['⚡ TRY IT'] = '⚡ やってみよう'
    ja[CREDIT_EN] = CREDIT_JA
    css = HEAD_CSS % dict(a['pal'], extra_css=a['game_css'], dark_css=a.get('dark_css', ''))
    js = tr_markup(a['game_js'], ja)
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta name="robots" content="noindex, nofollow" /><!-- 📝 draft -->
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>%(title)s</title>
<link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="../../assets/favicon-180.png" />
<style>
  /* 🐼 元気が出る心理学シリーズ（その3・2026-10-05）。真面目な話 → ポップに（トーン反転） */%(css)s</style>
<script>document.documentElement.className += " js";</script>
%(draftcss)s
</head>
<body>
<main>
  <!-- 📝 draft-ribbon:start（tools/draft.py） -->
  <div class="draft-ribbon" translate="no">📝 DRAFT · 下書き — まだ本番に出していません · <a href="../index.html">下書き一覧</a></div>
  <!-- 📝 draft-ribbon:end -->

  <div class="topbar">
    <a class="home" href="../index.html">← Back</a>
    <div class="badges">
      <div class="wc-badge">⚡ 0 words · 0 sec</div>
      <div class="stage stage-draft">DRAFT</div>
    </div>
  </div>

  <div class="label"><span class="topic">🐧 EVERYDAY LIFE</span>⚡ 15 SEC</div>
  <h1>%(title)s <span class="float">%(h1e)s</span></h1>

  <figure class="photo">
    <img src="IMAGE:cover.jpg" alt="%(alt)s" />
  </figure>

%(body)s

  <div class="credit">%(credit)s</div>
</main>

%(reveal)s
<script>
%(js)s
</script>
</body>
</html>

<!-- SOURCE MAP
%(smap)s

本文（.card の中の <p>）の英文はすべて、上のどれかのS番号から訳したものです。
S番号に対応しない英文は1つもありません。

削った文：なし
追加した文：0
整理テキスト：card-label %(nlab)d個 / h1 / %(gname)sの文字 ← 本人の素材の要約・演出（word数対象外）
-->
''' % dict(title=esc(a['title_en']), css=css, draftcss=DRAFT_CSS, h1e=a['h1e'], alt=esc(a['alt']),
           body='\n\n'.join(parts), credit=esc(CREDIT_EN), reveal=REVEAL_JS, js=js,
           smap='\n'.join(smap), nlab=cardno, gname=a['game_name'])
    open(os.path.join(d, 'index.html'), 'w').write(html)
    jaj = {'title': a['title_ja'], 'label': a['label_ja'], 'text': ja}
    open(os.path.join(d, 'i18n', 'ja.json'), 'w').write(json.dumps(jaj, ensure_ascii=False, indent=2) + '\n')
    meta = {'title': a['title_en'], 'label': a['label_en'], 'date': '2026-10-05', 'length': '15sec', 'thumbAlt': a['alt'],
            'place': 'nagoya', 'topic': 'life', 'seq': a['seq'], 'room': 'head', 'series': 'happy-psychology',
            'mood': a['mood'], 'tags': a['tags']}
    open(os.path.join(d, 'meta.json'), 'w').write(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    src = '''# slug: %(slug)s / date: 2026-10-05 / words: 0

## 出どころ

本人のメモ その3（幸せに生きるための考え方）の「%(sec)s」（2026-10-05 本人がチャットに貼った。本人の要望：本人の口調で、15秒で読めるようにかなり分割していい・元気がない時に見たい記事・面白くて可愛く・インタラクティブに・スマホファースト。「本当にゆっくりでいいから質を優先して」）
→ 本人の指示で、AI が本人の口調（一人称「私」・標準語）で書き直した。元のブログや本の著者の体験談は使っていない。例は仕事以外のもの（%(exkind)s）にした（ブログ憲法 第1条）。

## 素材（日本語・1文ずつ S番号 を振る）

%(slines)s

## 中心メッセージ（1つだけ・1行で）

%(core)s

## トーン

素材の重さ：真面目（%(weight)s）
→ 見せ方：ポップに（%(look)s）

## 触って遊べるもの

%(gamedesc)s

## 表紙のプロンプト

%(prompt)s

## 画像

images/cover.jpg — %(alt)s
使った組み合わせ：%(combo)s

## YouTube

なし

追加した文：0
''' % dict(slug=slug, sec=a['sec'], exkind=a['exkind'], slines='\n'.join('S%d. %s' % (i + 1, s[0]) for i, s in enumerate(S)),
           core=a['core'], weight=a['weight'], look=a['look'], gamedesc=a['gamedesc'], prompt=a['prompt'], alt=a['alt'], combo=a['combo'])
    open(os.path.join(d, 'source.md'), 'w').write(src)
    words = sum(len(e.split()) for _, e in S)
    print(slug, 'words', words)
