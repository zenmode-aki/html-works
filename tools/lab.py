#!/usr/bin/env python3
"""
🧪 試作の棚（2026-10-08 本人の要望）

本人：「一気に出した記事は、ちょっと適当に作ったもの、みたいなフォルダの中に入れて、隠しファイルみたいにしておいてほしい。
      本番に乗っけててもいいけど、すごい下までスクロールしないと見れない、みたいな感じに。
      それ以外は普通のブログとして、これまでの記事をちゃんとやってほしい」

  https://15-second-blog.com/lab/          ← 試作の一覧（トップのいちばん下の小さなリンクからだけ行ける。検索には出さない）
  https://15-second-blog.com/lab/<slug>/   ← 試作の記事

  python3 tools/lab.py move <slug>...      本番（works/）から試作の棚（lab/）へ移す
  python3 tools/lab.py publish <slug>...   試作の棚から本番（works/）へ戻す（文章と表紙を直してから）→ そのあと本番のいつもの手順
  python3 tools/lab.py build               試作の一覧・各ページを作り直す（i18n.py --lab も呼ぶ）

決まりごと
- 本番の一覧・地図・タグ・「次の記事」「こちらもどうぞ」・気分のおすすめには出ない（道具はみんな works/ だけを見るので、移すだけで外れる）
- 訳は日本語と韓国語だけ（lab/<slug>/i18n/ja.json・ko.json）。ほかの言語の訳ファイルがあっても消さない
- 検索に出さない：各ページに noindex、robots.txt で /lab/ を止める、sitemap にも入れない
- 古い URL（/works/<slug>/）で来た人は、404.html が /lab/<slug>/ へ連れていく（lab/slugs.json を見る）
- 中身の直し方（○○が言った、をやめる・文章をていねいに・表紙を作り直す）は BACKLOG.md の「🧪 試作の棚」
"""
import html, importlib.util, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS, LAB = ROOT / "works", ROOT / "lab"

_spec = importlib.util.spec_from_file_location("draft", ROOT / "tools" / "draft.py")
dr = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(dr)

RIB_S, RIB_E = "<!-- 🧪 lab-ribbon:start（tools/lab.py） -->", "<!-- 🧪 lab-ribbon:end -->"
NAV_S, NAV_E = "<!-- 🧪 lab-nav:start（tools/lab.py） -->", "<!-- 🧪 lab-nav:end -->"
NOINDEX = '<meta name="robots" content="noindex, nofollow" /><!-- 🧪 lab -->'
CSS = """<style id="lab-css">
  /* 🧪 試作の棚の印（tools/lab.py）。本番に戻すと消える */
  .lab-ribbon { display: flex; align-items: center; justify-content: center; gap: 6px 10px; flex-wrap: wrap; margin: 0 0 14px;
    padding: 10px 14px; border-radius: 14px; background: #eef2f7; border: 1.5px dashed rgba(60,80,110,.28);
    color: #3c4a60; font-size: 13px; font-weight: 800; line-height: 1.5; text-align: center; }
  .lab-ribbon a { color: inherit; }
  .stage-lab { background: #dfe6ef !important; color: #34445c !important; }
  @media (max-width: 600px) { .topbar { flex-wrap: wrap; row-gap: 8px; } .stage-lab { padding-inline: 8px !important; letter-spacing: .04em !important; } }
  .lab-nav { display: grid; gap: 12px; margin-top: 26px; }
  .lab-next { display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 18px 20px; border-radius: 22px;
    text-decoration: none; color: #2c3a50; background: #eef2f7; border: 2px dashed rgba(60,80,110,.25); font-weight: 900; }
  .lab-next small { display: block; font-size: 12px; letter-spacing: .12em; opacity: .75; }
  .lab-next span.t { display: block; font-size: 17px; line-height: 1.4; }
  .lab-back { justify-self: center; display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 12px 22px;
    border-radius: 999px; background: #fff; color: #232c48; border: 2px solid rgba(35,44,72,.14); text-decoration: none; font-weight: 900; }
  .lab-topics { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; justify-content: center; font-size: 13px; font-weight: 900; }
  .lab-topics a { display: inline-flex; align-items: center; min-height: 44px; padding: 8px 14px; border-radius: 999px; background: #fff;
    border: 2px solid rgba(60,80,110,.18); color: #2c3a50; text-decoration: none; }
  html[data-theme="dark"] .lab-topics a { background: #22242f; color: #f4f0fa; border-color: rgba(255,255,255,.16); }
  .lab-home { justify-self: center; font-size: 13px; font-weight: 700; color: inherit; opacity: .6; }
  html[data-theme="dark"] .lab-ribbon, html[data-theme="dark"] .lab-next { background: #252b36; color: #d6deea; border-color: rgba(214,222,234,.25); }
  html[data-theme="dark"] .lab-back { background: #22242f; color: #f4f0fa; border-color: rgba(255,255,255,.16); }
</style>
"""


def load(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def slugs(d):
    return sorted(p.parent.name for p in d.glob("*/index.html"))


def strip_marks(doc):
    doc = re.sub(r"[ \t]*" + re.escape(RIB_S) + r".*?" + re.escape(RIB_E) + r"\n?", "", doc, flags=re.S)
    doc = re.sub(r"\n?[ \t]*" + re.escape(NAV_S) + r".*?" + re.escape(NAV_E) + r"\n?", "\n", doc, flags=re.S)
    doc = re.sub(r'<style id="lab-css">.*?</style>\n?', "", doc, flags=re.S)
    return doc.replace("\n" + NOINDEX, "").replace(NOINDEX, "")


def to_lab_page(slug, doc, labs, works, nxt):
    for rx in dr.PROD_BLOCKS:            # 本番の「次・前・こちらもどうぞ・一覧に戻る」は外す
        doc = rx.sub("\n", doc)
    doc = strip_marks(doc)
    doc = re.sub(r"(<main[^>]*>\n)[ \t]+\n", r"\1", doc, count=1)
    doc = doc.replace('href="../../index.html#posts"', 'href="../index.html"').replace('href="../../index.html"', 'href="../index.html"')
    def fix(m):                          # 本番の記事へのリンクは ../../works/ へ
        s = m.group(2)
        return f"{m.group(1)}../../works/{s}/" if s in works and s not in labs else m.group(0)
    doc = re.sub(r'(href=")\.\./([a-z0-9-]+)/', fix, doc)
    doc = doc.replace('<div class="stage stage-public">PUBLIC</div>', '<div class="stage stage-lab" translate="no">LAB</div>')
    doc = doc.replace(f"https://15-second-blog.com/works/{slug}/", f"https://15-second-blog.com/lab/{slug}/")
    doc = doc.replace("<head>", "<head>\n" + NOINDEX, 1)
    doc = doc.replace("</head>", CSS + "</head>", 1)
    rib = (f"  {RIB_S}\n  <div class=\"lab-ribbon\" translate=\"no\">🧪 LAB · 試作 — AIが読書メモから一気に作った記事です。"
           f"本番の一覧には出していません · <a href=\"../index.html\">試作の一覧</a></div>\n  {RIB_E}\n")
    doc = re.sub(r"(<main[^>]*>\n?)", lambda m: m.group(1) + rib, doc, count=1)
    nav = [f"  {NAV_S}", '  <nav class="lab-nav" translate="no">']
    if nxt:
        en = load(LAB / nxt / "meta.json").get("title", nxt)
        ja = load(LAB / nxt / "i18n" / "ja.json").get("title") or en
        nav.append(f'    <a class="lab-next" href="../{nxt}/index.html"><span><small>NEXT · 次の試作</small>'
                   f'<span class="t">{html.escape(ja)}</span></span><span aria-hidden="true">🧪</span></a>')
    tags = load(LAB / slug / "meta.json").get("tags", [])
    tl = [t for t in TOPICS if t[0] in tags][:4]
    if tl:   # 🗺 読み終えたら、同じテーマの地図へ（2026-10-08 本人）
        nav.append('    <div class="lab-topics"><span>🗺 同じテーマを読む：</span>' + "".join(
            f'<a href="../index.html#t={k}">{e} {n}</a>' for k, e, n in tl) + '<a href="../index.html#map">🗺 テーマの地図</a></div>')
    nav += ['    <a class="lab-back" href="../index.html">🧪 ← 試作の一覧 / All lab posts</a>',
            '    <a class="lab-home" href="../../index.html">ブログのトップへ ↗</a>',
            "  </nav>", f"  {NAV_E}"]
    i = doc.rfind("</main>")
    return doc[:i] + "\n".join(nav) + "\n" + doc[i:]


def from_lab_page(slug, doc):
    doc = strip_marks(doc)
    doc = doc.replace('href="../index.html"', 'href="../../index.html"').replace('href="../../works/', 'href="../')
    doc = doc.replace('<div class="stage stage-lab" translate="no">LAB</div>', '<div class="stage stage-public">PUBLIC</div>')
    return doc.replace(f"https://15-second-blog.com/lab/{slug}/", f"https://15-second-blog.com/works/{slug}/")


# 🗺 テーマの地図（2026-10-08 本人：「読み終えるごとに地図を出して、好きな記事に飛べるように」）。試作は場所がないので、テーマで
TOPICS = [("feelings", "🫧", "気持ち"), ("friends", "💬", "人づきあい"), ("happiness", "😊", "しあわせ"), ("mindset", "💭", "考え方"),
          ("productivity", "✅", "やること・時間"), ("rest", "🛋️", "休む"), ("mistakes", "😅", "失敗"), ("study", "📚", "勉強"),
          ("sleep", "😴", "眠り"), ("health", "🍵", "体"), ("walking", "👟", "歩く"), ("family", "🏠", "家族"), ("money", "💴", "お金"),
          ("books", "📖", "本のメモ"), ("tips", "💡", "小さなコツ")]

SERIES = [("happy-psychology", "🐼 しあわせ心理学のメモから"), ("time-and-life-notes", "📘 時間と生き方の本のメモから"), ("", "🗂 そのほか")]


def index_html(rows):
    secs = []
    for key, title in SERIES:
        rs = [r for r in rows if (r["series"] if r["series"] in dict(SERIES) else "") == key]
        if not rs:
            continue
        cards = "\n".join(
            f'      <a class="card" data-t="{" ".join(r["tags"])}" href="{r["slug"]}/index.html"><img src="../assets/thumbs/{r["slug"]}.jpg" alt="" loading="lazy">'
            f'<div><div class="ja">{html.escape(r["ja"])}</div><div class="en">{html.escape(r["en"])}</div></div></a>' for r in rs)
        secs.append(f'  <section>\n    <h2>{title} <small>{len(rs)}本</small></h2>\n    <div class="grid">\n{cards}\n    </div>\n  </section>')
    cnt = {k: sum(1 for r in rows if k in r["tags"]) for k, _, _ in TOPICS}
    tmap = "".join(f'<button type="button" class="tp" data-k="{k}" style="--s:{min(1.6, .9 + cnt[k] / 120):.2f}">'
                   f'<span class="e">{e}</span><span class="n">{n}</span><b>{cnt[k]}</b></button>'
                   for k, e, n in sorted(TOPICS, key=lambda t: -cnt[t[0]]) if cnt[k])
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="noindex, nofollow" />
<title>🧪 試作の棚 · Pengesso</title>
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png" />
<!-- 🧪 このページは tools/lab.py build が作る。手で書かない -->
<style>
  :root {{ --bg: #f5f7fa; --ink: #2a3140; --muted: #6b7486; --card: #fff; --line: rgba(42,49,64,.1); }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--bg); color: var(--ink); font-family: "Hiragino Sans", "Hiragino Kaku Gothic ProN", system-ui, sans-serif; font-weight: 700; }}
  main {{ width: min(880px, calc(100% - 32px)); margin: 0 auto; padding: 26px 0 60px; }}
  h1 {{ margin: 6px 0 6px; font-size: clamp(26px, 6vw, 40px); font-weight: 900; }}
  .lead {{ margin: 0 0 20px; color: var(--muted); font-size: 14.5px; line-height: 1.8; }}
  .top a {{ color: var(--muted); font-size: 13.5px; }}
  h2 {{ margin: 26px 0 10px; font-size: 19px; font-weight: 900; }} h2 small {{ font-size: 13px; color: var(--muted); }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 10px; }}
  .card {{ display: flex; gap: 12px; align-items: center; padding: 10px; border-radius: 16px; background: var(--card); border: 1.5px solid var(--line); color: inherit; text-decoration: none; }}
  .card img {{ flex: none; width: 64px; height: 64px; border-radius: 12px; object-fit: cover; background: #e9edf3; }}
  .ja {{ font-size: 14.5px; font-weight: 900; line-height: 1.45; }}
  .en {{ margin-top: 3px; font-size: 12px; color: var(--muted); line-height: 1.4; }}
  .map {{ margin: 0 0 8px; padding: 16px 12px; border-radius: 24px; background: linear-gradient(160deg, #eaf0ff, #fff4e8); scroll-margin-top: 12px; }}
  .map h2 {{ margin: 0 0 4px; }} .map p {{ margin: 0 0 12px; color: var(--muted); font-size: 13px; }}
  .tps {{ display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }}
  .tp {{ display: inline-flex; align-items: center; gap: 6px; min-height: 44px; padding: 8px 14px; border-radius: 999px; border: 2px solid rgba(42,49,64,.1);
    background: #fff; color: var(--ink); font: inherit; font-size: calc(13px * var(--s)); font-weight: 900; cursor: pointer;
    animation: tpIn .5s cubic-bezier(.2,1.5,.4,1) both; box-shadow: 0 6px 14px rgba(42,49,64,.08); }}
  .tp .e {{ font-size: 1.3em; }} .tp b {{ font-size: .75em; color: var(--muted); }}
  .tp[aria-pressed="true"] {{ background: #2a3140; color: #fff; }} .tp[aria-pressed="true"] b {{ color: #cfd6e4; }}
  .tps .tp:nth-child(2n) {{ animation-delay: .06s; }} .tps .tp:nth-child(3n) {{ animation-delay: .12s; }}
  @keyframes tpIn {{ from {{ opacity: 0; transform: scale(.6); }} to {{ opacity: 1; transform: none; }} }}
  .card[hidden], section[hidden] {{ display: none; }}
  @media (prefers-reduced-motion: reduce) {{ html:not([data-motion="on"]) .tp {{ animation: none; }} }}
  html[data-motion="off"] .tp {{ animation: none; }}
</style>
</head>
<body>
<main>
  <div class="top"><a href="../index.html">← ブログのトップ（15-second-blog.com）</a></div>
  <h1>🧪 試作の棚 <span style="font-size:.5em">{len(rows)}本</span></h1>
  <p class="lead">ここは、AIが読書メモやブログのメモから一気に作った記事の置き場です。本番の一覧には出していません。<br>
  これから少しずつ、文章と表紙をていねいに直して、良くなったものから本番に戻します。検索には出ません。</p>
  <section class="map" id="map">
    <h2>🗺 テーマの地図</h2>
    <p>気になるテーマを押すと、その記事だけになります。もう一度押すと、ぜんぶに戻ります。</p>
    <div class="tps">{tmap}</div>
  </section>
{chr(10).join(secs)}
</main>
<script>
(function () {{
  var on = null, tps = [].slice.call(document.querySelectorAll('.tp'));
  function paint() {{
    tps.forEach(function (b) {{ b.setAttribute('aria-pressed', b.dataset.k === on ? 'true' : 'false'); }});
    [].forEach.call(document.querySelectorAll('.card'), function (c) {{ c.hidden = !!on && (' ' + c.dataset.t + ' ').indexOf(' ' + on + ' ') < 0; }});
    [].forEach.call(document.querySelectorAll('main > section:not(.map)'), function (s) {{ s.hidden = !s.querySelector('.card:not([hidden])'); }});
  }}
  tps.forEach(function (b) {{ b.addEventListener('click', function () {{ on = on === b.dataset.k ? null : b.dataset.k; paint();
    var f = document.querySelector('main > section:not(.map):not([hidden])'); if (on && f) f.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}); }});
  var h = (location.hash.match(/^#t=([a-z-]+)/) || [])[1]; if (h) {{ on = h; paint(); }}
}})();
</script>
</body>
</html>
"""


def build():
    labs, works = slugs(LAB), set(slugs(WORKS))
    rows = []
    for s in labs:
        m = load(LAB / s / "meta.json")
        rows.append({"slug": s, "series": m.get("series", ""), "seq": m.get("seq", 0), "en": m.get("title", s), "tags": m.get("tags", []),
                     "ja": load(LAB / s / "i18n" / "ja.json").get("title") or m.get("title", s)})
    rows.sort(key=lambda r: (r["series"], r["seq"]))
    seq = [r["slug"] for r in rows]
    for i, s in enumerate(seq):
        p = LAB / s / "index.html"
        doc = p.read_text(encoding="utf-8")
        new = to_lab_page(s, doc, set(labs), works, seq[i + 1] if i + 1 < len(seq) else None)
        if new != doc:
            p.write_text(new, encoding="utf-8")
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "i18n.py"), "--lab"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:]); raise SystemExit("❌ 試作の訳の埋め込みに失敗")
    subprocess.run([sys.executable, str(ROOT / "tools" / "furigana.py"), "--lab"], cwd=ROOT, capture_output=True, text=True)   # 英語のページの「日本語を学ぶ」のふりがな
    LAB.mkdir(exist_ok=True)
    (LAB / "index.html").write_text(index_html(rows), encoding="utf-8")
    (LAB / "slugs.json").write_text(json.dumps(sorted(labs)) + "\n", encoding="utf-8")
    print(f"🧪 試作の棚：{len(labs)}本 → lab/index.html を作り直した")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 1
    cmd, rest = a[0], a[1:]
    if cmd == "move":
        for s in rest:
            if not (WORKS / s).exists():
                raise SystemExit(f"❌ works/{s} がありません")
            dr.mv(WORKS / s, LAB / s)
        print(f"🧪 {len(rest)}本 works/ → lab/")
        build()
    elif cmd == "publish":
        for s in rest:
            p = LAB / s / "index.html"
            p.write_text(from_lab_page(s, p.read_text(encoding="utf-8")), encoding="utf-8")
            dr.mv(LAB / s, WORKS / s)
            print(f"🚀 lab/{s} → works/{s}（このあと：build-site ほか本番のいつもの手順）")
        build()
    elif cmd == "build":
        build()
    else:
        print(__doc__); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
