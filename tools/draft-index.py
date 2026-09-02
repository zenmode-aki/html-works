#!/usr/bin/env python3
"""
🖥 ローカル版の入口ページ（drafts/index.html）を作り直す

  python3 tools/draft-index.py

drafts/ にある下書きを並べて、本番トップやトップの試作にも飛べるようにする。
このファイル自体も drafts/ の中なので、GitHub には上がらない（.gitignore）。

毎朝のタスクが下書きを作ったあと、これを実行する。
"""
import html, pathlib, re, sys
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "drafts"


def read(slug_dir: pathlib.Path) -> dict:
    doc = (slug_dir / "index.html").read_text(encoding="utf-8")
    def grab(pat, default=""):
        m = re.search(pat, doc, re.S)
        return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else default
    labels = [re.sub(r"<[^>]+>", "", l).strip()
              for l in re.findall(r'class="card-label"[^>]*>(.*?)</', doc, re.S)]
    badge = grab(r'class="wc-badge"[^>]*>(.*?)</div>', "?")
    src = slug_dir / "source.md"
    where = ""
    if src.exists():
        m = re.search(r"^Slack:\s*(.+)$", src.read_text(encoding="utf-8"), re.M)
        where = m.group(1).strip() if m else ""
    return dict(
        slug=slug_dir.name,
        title=grab(r"<h1[^>]*>(.*?)</h1>", slug_dir.name),
        badge=badge, labels=labels, where=where,
        thumb=(slug_dir / "thumb.jpg").exists(),
        when=datetime.fromtimestamp(
            (slug_dir / "index.html").stat().st_mtime).strftime("%Y.%m.%d %H:%M"),
    )


def card(d: dict) -> str:
    e = html.escape
    thumb = (f'<img src="{e(d["slug"])}/thumb.jpg" alt="" />' if d["thumb"]
             else '<span class="no-thumb">🐧</span>')
    trail = (" → ".join(e(l) for l in d["labels"])) or "—"
    where = f'<div class="where">{e(d["where"])}</div>' if d["where"] else ""
    return f"""    <a class="draft" href="{e(d['slug'])}/index.html">
      <div class="thumb">{thumb}</div>
      <div>
        <div class="t">{e(d['title'])}</div>
        <div class="meta"><span>{e(d['badge'])}</span><span>作った {e(d['when'])}</span></div>
        <div class="trail">{trail}</div>
        {where}
      </div>
      <div class="go">→</div>
    </a>"""


PAGE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>🖥 ローカル版の入口 — 15 Second Blog</title>
<style>
  :root {{
    --navy:#232c48; --blue:#2f56c9; --yellow:#ffc42e;
    --cream:#f6efe3; --paper:#fffdf8; --ink:#1b2138; --muted:#6d7593;
    --line:rgba(35,44,72,.11);
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--cream); color:var(--ink);
    font-family:"Arial Rounded MT Bold","Avenir Next Rounded","Hiragino Maru Gothic ProN","Trebuchet MS",sans-serif;
  }}
  .bar {{
    position:sticky; top:0; z-index:9; display:flex; align-items:center;
    justify-content:center; gap:9px; padding:9px 14px;
    background:var(--yellow); color:#4a2c00;
    font-size:11.5px; font-weight:900; letter-spacing:.14em;
  }}
  .bar .why {{ opacity:.78; letter-spacing:.02em; font-weight:700; }}
  .dot {{ width:9px; height:9px; border-radius:50%; background:#4a2c00;
         box-shadow:0 0 0 3px rgba(74,44,0,.18); }}
  main {{ width:min(880px, calc(100% - 32px)); margin:0 auto; padding:26px 0 70px; }}
  h1 {{ margin:0 0 6px; font-size:clamp(26px,4.4vw,38px); letter-spacing:-.03em; }}
  .lead {{ margin:0 0 26px; color:var(--muted); font-size:14px; line-height:1.8;
          font-family:"Trebuchet MS",sans-serif; }}
  h2 {{ margin:34px 0 14px; font-size:17px; letter-spacing:-.01em; }}
  .links {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(215px,1fr)); gap:11px; }}
  .link {{
    display:block; padding:16px 18px; border-radius:17px; text-decoration:none; color:inherit;
    background:var(--paper); border:1.5px solid var(--line);
    transition:transform .16s ease, border-color .16s ease;
  }}
  .link:hover {{ transform:translateY(-3px); border-color:var(--blue); }}
  .link b {{ display:block; font-size:14.5px; margin-bottom:5px; }}
  .link span {{ color:var(--muted); font-size:12px; font-family:"Trebuchet MS",sans-serif; }}
  .draft {{
    display:grid; grid-template-columns:64px 1fr auto; align-items:center; gap:16px;
    padding:15px 18px; border-radius:19px; text-decoration:none; color:inherit;
    background:var(--paper); border:1.5px solid var(--line); margin-bottom:11px;
    transition:transform .16s ease, border-color .16s ease;
  }}
  .draft:hover {{ transform:translateY(-3px); border-color:var(--blue); }}
  .thumb {{
    width:64px; height:64px; border-radius:17px; overflow:hidden; background:#e9e2d4;
    display:grid; place-items:center; font-size:26px;
  }}
  .thumb img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .t {{ font-size:15.5px; line-height:1.45; }}
  .meta {{ display:flex; flex-wrap:wrap; gap:6px 14px; margin-top:6px;
          color:var(--muted); font-size:12px; font-family:"Trebuchet MS",sans-serif; }}
  .trail {{ margin-top:6px; font-size:11px; font-weight:900; letter-spacing:.1em;
           color:var(--blue); text-transform:uppercase; }}
  .where {{ margin-top:5px; color:var(--muted); font-size:11.5px;
           font-family:"Trebuchet MS",sans-serif; }}
  .go {{ font-size:20px; color:var(--muted); }}
  .empty {{
    padding:34px; text-align:center; border-radius:19px; background:var(--paper);
    border:1.5px dashed var(--line); color:var(--muted); font-size:14px; line-height:1.9;
  }}
  footer {{ margin-top:40px; color:var(--muted); font-size:12px; line-height:1.9;
           font-family:"Trebuchet MS",sans-serif; }}
  code {{ background:rgba(35,44,72,.07); padding:2px 7px; border-radius:6px; font-size:12px; }}
  @media (max-width:600px) {{
    .draft {{ grid-template-columns:52px 1fr; }}
    .thumb {{ width:52px; height:52px; border-radius:14px; }}
    .go {{ display:none; }}
  }}
</style>
</head>
<body>
<div class="bar"><span class="dot"></span>LOCAL<span class="why">自分のパソコンの中だけ。世界には出ていません</span></div>
<main>
  <h1>🖥 ローカル版の入口</h1>
  <p class="lead">
    ここは下書き置き場です。ここにあるものは <b>GitHub に上がりません</b>。<br />
    気に入ったものだけ「これ出して」と言えば、本番に出ます。
  </p>

  <h2>まず行くところ</h2>
  <div class="links">
    <a class="link" href="_prototype-home.html"><b>⚡ トップの試作</b><span>スロット・検索・地図・ペンゲッソ紹介</span></a>
    <a class="link" href="../index.html"><b>🌏 いまの本番トップ</b><span>公開されているもの（ローカルで確認）</span></a>
    <a class="link" href="https://zenmode-aki.github.io/html-works/"><b>🚀 本番サイト</b><span>世界から見えているほう</span></a>
  </div>

  <h2>下書き（{n}本）</h2>
{body}

  <footer>
    このページは <code>python3 tools/draft-index.py</code> で作り直せます。<br />
    サーバを止めるときは <code>./local.sh stop</code>。
  </footer>
</main>
</body>
</html>
"""


def main():
    DRAFTS.mkdir(exist_ok=True)
    dirs = sorted((p for p in DRAFTS.iterdir()
                   if p.is_dir() and (p / "index.html").exists()),
                  key=lambda p: -(p / "index.html").stat().st_mtime)
    if dirs:
        body = "\n".join(card(read(d)) for d in dirs)
    else:
        body = ('    <div class="empty">まだ下書きはありません 🐧<br />'
                'Slackに何か書いておくと、翌朝6時にここに増えます。</div>')
    (DRAFTS / "index.html").write_text(
        PAGE.format(n=len(dirs), body=body), encoding="utf-8")
    print(f"✅ drafts/index.html を作りました（下書き {len(dirs)}本）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
