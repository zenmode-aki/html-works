#!/usr/bin/env python3
"""
🏗 トップページを作り直す（本番と本番前の両方）

  python3 tools/build-site.py

    works/<slug>/meta.json          → index.html          （本番）
    staging/works/<slug>/meta.json  → staging/index.html  （本番前）

**トップページは手で編集しない。** ここで作り直す。
Claude と ChatGPT/Codex の両方が同じリポジトリを触るので、
244KBのHTMLを手で編集すると直しようのない衝突になるため。

words と sec は meta.json に書かない。記事HTMLから毎回数える
（tools/check.py の body_words を使う）ので、数字がズレることが原理的に起きない。

sips を使わない純Pythonなので、GitHub Actions（Ubuntu）でも動く。
サムネ画像そのものを作るのは tools/thumbs.py（macOS専用）の担当。
"""
import html as H
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("chk", ROOT / "tools" / "check.py")
_chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_chk)


def collect(base: pathlib.Path):
    """<base>/<slug>/meta.json を読んで、日付の新しい順に並べる。"""
    out = []
    if not base.exists():
        return out
    for d in sorted(base.iterdir()):
        meta = d / "meta.json"
        idx = d / "index.html"
        if not (d.is_dir() and meta.exists() and idx.exists()):
            continue
        m = json.loads(meta.read_text(encoding="utf-8"))
        m["slug"] = d.name
        n = len(_chk.body_words(idx.read_text(encoding="utf-8")))
        m["words"] = n
        m["sec"] = round(n / (_chk.WPM / 60))
        out.append(m)
    return sorted(out, key=lambda m: (m.get("date", ""), m["slug"]), reverse=True)


def card(m: dict, asset_prefix: str) -> str:
    e = H.escape
    icon = "⏱" if m.get("length") == "1min" else "⚡"
    unit = f"{m['words']} words · {m['sec']} sec"
    return f"""
    <a class="work" href="works/{e(m['slug'])}/index.html">
      <div class="work-thumb">
        <img src="{asset_prefix}assets/thumbs/{e(m['slug'])}.jpg" alt="{e(m.get('thumbAlt',''))}" decoding="async" />
      </div>
      <div>
        <div class="work-label">{e(m.get('label',''))}</div>
        <div class="work-title">{e(m.get('title', m['slug']))}</div>
        <div class="work-meta">{e(m.get('date','').replace('-','.'))} · {icon} {unit}</div>
      </div>
    </a>"""


def grid(items, asset_prefix, empty_msg):
    if not items:
        return f'\n    <div class="empty">{empty_msg}</div>\n'
    return "\n" + "\n".join(card(m, asset_prefix) for m in items) + "\n"


STYLE = """
  :root {
    --navy:#232c48; --blue:#2f56c9; --blue-2:#567cf0; --yellow:#ffc42e;
    --cream:#f6efe3; --paper:#fffdf8; --ink:#1b2138; --muted:#6d7593;
    --line:rgba(35,44,72,.11);
  }
  * { box-sizing: border-box; }
  body {
    margin:0; background:var(--cream); color:var(--ink);
    font-family:"Arial Rounded MT Bold","Avenir Next Rounded","Trebuchet MS",sans-serif;
    -webkit-font-smoothing:antialiased;
  }
  main { width:min(920px, calc(100% - 26px)); margin:0 auto; padding:30px 0 70px; }

  .stage-bar {
    position:sticky; top:0; z-index:9; display:flex; align-items:center;
    justify-content:center; gap:9px; padding:9px 14px;
    font-size:11.5px; font-weight:900; letter-spacing:.14em;
  }
  .stage-bar .why { opacity:.78; letter-spacing:.02em; font-weight:700; }
  .stage-dot { width:9px; height:9px; border-radius:50%; flex:0 0 auto; }
  .bar-staging { background:var(--yellow); color:#4a2c00; }
  .bar-staging .stage-dot { background:#4a2c00; box-shadow:0 0 0 3px rgba(74,44,0,.18); }

  .label { color:var(--blue); font-size:13px; font-weight:900; letter-spacing:.16em; margin-bottom:14px; }
  h1 { margin:0 0 16px; font-size:clamp(34px,7vw,62px); line-height:1.05; letter-spacing:-.045em;
       text-wrap:balance; text-shadow:0 4px 0 rgba(255,255,255,.7); }
  .intro { margin:0 0 30px; padding:20px 22px; background:var(--paper);
           border:1.5px solid var(--line); border-radius:22px;
           font-size:clamp(15px,2.1vw,17.5px); font-weight:700; line-height:1.75; }

  .section-head { display:flex; align-items:baseline; gap:12px; flex-wrap:wrap; margin:40px 0 16px; }
  .section-head h2 { margin:0; font-size:clamp(19px,3vw,25px); letter-spacing:-.02em; }
  .section-note { color:var(--muted); font-size:13px; font-weight:700; }

  .grid { display:grid; gap:13px; }
  .work {
    display:grid; grid-template-columns:66px 1fr; align-items:center; gap:18px;
    padding:17px 20px; text-decoration:none; color:inherit;
    background:var(--paper); border:1.5px solid var(--line); border-radius:24px;
  }
  .work-thumb { width:66px; height:66px; overflow:hidden; border-radius:20px; background:#e9e2d4;
                border:2px solid rgba(255,255,255,.9); box-shadow:0 6px 16px rgba(35,44,72,.13);
                transition:transform .25s ease; }
  .work-thumb img { display:block; width:100%; height:100%; object-fit:cover; }
  .work:hover .work-thumb { transform:rotate(-4deg) scale(1.06); }
  .work-label { font-size:11.5px; font-weight:900; letter-spacing:.16em; color:var(--blue);
                text-transform:uppercase; margin-bottom:5px; }
  .work-title { font-size:clamp(16px,2.4vw,21px); line-height:1.38; }
  .work-meta  { margin-top:7px; color:var(--muted); font-size:12.5px; font-weight:700; }
  .archive .work { opacity:.84; }
  .archive .work:hover { opacity:1; }
  .empty { padding:30px; text-align:center; border-radius:22px; background:var(--paper);
           border:1.5px dashed var(--line); color:var(--muted); font-size:14px; font-weight:700; }

  footer { margin-top:44px; text-align:center; color:var(--muted); font-size:12.5px;
           font-weight:700; line-height:1.9; }
  footer a { color:var(--blue); }

  @keyframes rise { from { opacity:0; transform:translateY(16px); } to { opacity:1; transform:none; } }
  .label { animation:rise .5s .05s both ease-out; }
  h1     { animation:rise .6s .12s both ease-out; }
  .intro { animation:rise .6s .22s both ease-out; }
  /* .js が付いているときだけ隠す。JSが動かない環境では最初から見えている */
  .js .work { opacity:0; transform:translateY(18px);
              transition:opacity .5s ease-out, transform .5s ease-out, box-shadow .18s ease; }
  .js .work.in { opacity:1; transform:none; }
  .work.in:hover { transform:translateY(-4px); box-shadow:0 20px 44px rgba(35,44,72,.16); }
  @keyframes float { from { transform:translateY(0) rotate(-4deg); } to { transform:translateY(-9px) rotate(4deg); } }
  .float { display:inline-block; animation:float 3.4s ease-in-out infinite alternate; }

  @media (max-width:600px) {
    .work { grid-template-columns:52px 1fr; gap:14px; padding:15px 16px; border-radius:20px; }
    .work-thumb { width:52px; height:52px; border-radius:16px; }
  }
  /* 動きが苦手な人のための逃げ道。消さないこと */
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation:none !important; transition:none !important;
      opacity:1 !important; transform:none !important; }
  }
"""

SCRIPT = """
(function () {
  var items = [].slice.call(document.querySelectorAll('.work'));
  function showAll() { items.forEach(function (el) { el.classList.add('in'); }); }
  if (!('IntersectionObserver' in window)) { showAll(); return; }
  var seen = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); seen.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  items.forEach(function (el) { seen.observe(el); });
  setTimeout(function () { if (!document.querySelector('.work.in')) showAll(); }, 1600);
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
{robots}<title>{title}</title>
<!-- ⚠️ このファイルは python3 tools/build-site.py が作ります。手で編集しないでください。 -->
<style>{style}</style>
<script>document.documentElement.className += " js";</script>
</head>
<body>
{bar}<main>

  <div class="label">{kicker}</div>
  <h1>{h1}</h1>

  <p class="intro">{intro}</p>
{sections}
  <footer>{footer}</footer>

</main>
<script>{script}</script>
</body>
</html>
"""


def build_production(items):
    fresh = [m for m in items if m.get("length") != "1min"]
    old = [m for m in items if m.get("length") == "1min"]
    sections = f"""
  <div class="section-head">
    <h2>⚡ 15 Second</h2>
    <span class="section-note">35–55 words. Blink and it's over.</span>
  </div>
  <div class="grid">{grid(fresh, "", "Nothing here yet 🐧")}  </div>

  <div class="section-head">
    <h2>📖 The 1-Minute Archive</h2>
    <span class="section-note">2026.08 · back when these were a whole minute long.</span>
  </div>
  <div class="grid archive">{grid(old, "", "Nothing here yet 🐧")}  </div>
"""
    return PAGE.format(
        robots="", title="15 Second Blog ⚡", style=STYLE, bar="", script=SCRIPT,
        kicker="⚡ 15 SECOND BLOG ⚡",
        h1='Things I noticed <span class="float">🐧</span>',
        intro=("Short posts in easy English. 🌏<br />"
               "Most posts take about <b>15 seconds</b> to read — the word count is written "
               "at the top of each page, so you know before you start. ⚡"),
        sections=sections,
        footer=("🐧 Made with plain HTML. No build, no login, no tracking.<br />"
                "Each page is a single self-contained file."))


def build_staging(items):
    sections = f"""
  <div class="section-head">
    <h2>🟡 Waiting</h2>
    <span class="section-note">まだ本番に出していないもの。「これ出して」と言えば本番へ。</span>
  </div>
  <div class="grid">{grid(items, "../", "本番前の記事はいまありません 🐧")}  </div>
"""
    bar = ('<div class="stage-bar bar-staging"><span class="stage-dot"></span>STAGING'
           '<span class="why">本番前。検索には出ません</span></div>\n')
    return PAGE.format(
        robots='<meta name="robots" content="noindex, nofollow" />\n',
        title="🟡 STAGING — 15 Second Blog", style=STYLE, bar=bar, script=SCRIPT,
        kicker="🟡 STAGING · 本番前",
        h1='Not out yet <span class="float">🐧</span>',
        intro=("ここは<b>本番前</b>です。スマホからも ChatGPT/Codex からも見られますが、"
               "トップからはリンクしていないし、検索にも出ません。<br />"
               "気に入ったものだけ「これ出して」と言えば "
               "<a href=\"../index.html\">本番</a> に移ります。"),
        sections=sections,
        footer=('🟡 STAGING · <a href="../index.html">本番トップを見る</a> · '
                '<a href="https://zenmode-aki.github.io/html-works/">公開サイト</a><br />'
                'このページは python3 tools/build-site.py が作っています。'))


def main():
    prod = collect(ROOT / "works")
    stag = collect(ROOT / "staging" / "works")

    (ROOT / "index.html").write_text(build_production(prod), encoding="utf-8")
    (ROOT / "staging").mkdir(exist_ok=True)
    (ROOT / "staging" / "index.html").write_text(build_staging(stag), encoding="utf-8")

    size = (ROOT / "index.html").stat().st_size
    print(f"✅ index.html          本番 {len(prod)}本  ({size/1024:.0f}KB)")
    print(f"✅ staging/index.html  本番前 {len(stag)}本")

    missing = [m["slug"] for m in prod + stag
               if not (ROOT / "assets" / "thumbs" / f"{m['slug']}.jpg").exists()]
    if missing:
        print(f"\n⚠️  サムネがまだ無い: {', '.join(missing)}")
        print("   python3 tools/thumbs.py  で作れます（macOSのみ）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
