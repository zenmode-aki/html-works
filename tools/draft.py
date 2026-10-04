#!/usr/bin/env python3
"""
📝 下書きサイト（2026-09-29 本人の要望）

  https://15-second-blog.com/draft/        ← 下書きの一覧（本人が見る用。検索には出さない）
  https://15-second-blog.com/draft/<slug>/ ← 下書きの記事

  python3 tools/draft.py new <slug>          下書きを1本つくる（_template から。英日だけ）
  python3 tools/draft.py move <slug>...      本番（works/）から下書き（draft/）へ移す
  python3 tools/draft.py publish <slug>...   下書きから本番（works/）へ出す → そのあと本番のいつもの手順
  python3 tools/draft.py build               下書きの一覧・各ページ・本番トップの「もうすぐ公開」を作り直す

なぜ：本番に出すと、表紙の生成・40言語の訳・見直しで手間がかかる。
「とりあえず HTML にしてしまえば完成の形が見える」ので、まず下書きサイトに溜める。
本番のトップには「◯月◯日時点で下書き◯本」と、タイトルだけチラ見せする（読む人に期待してもらう）。

決まりごと
- 同じリポジトリの draft/ フォルダ。GitHub Pages はリポジトリ全体を配るので、URL が1つ増えるだけ
- 下書きは英語と日本語だけ（draft/<slug>/i18n/ja.json）。ほかの言語の訳ファイルがあっても消さない
- 検索に出さない：各ページに noindex、robots.txt で /draft/ を止める、sitemap にも入れない
- 下書きのページから本番の記事へのリンクは ../../works/<slug>/ に向け直す（切れないように）
- 本番トップのチラ見せには、仕事の話（topic が netops / work / bridge）のタイトルは出さない（ブログ憲法 第1条）
"""
import datetime, html, importlib.util, json, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS, DRAFT = ROOT / "works", ROOT / "draft"
GOAL = 1000
WORK_TOPICS = {"netops", "work", "bridge", "bridgese", "mcd"}
# 本番トップの「もうすぐ公開」に出す下書き（2026-09-30 本人：3本だけ・元気でくだらなくて面白いもの。公開したら次の候補に入れかえる）
PEEK_PICKS = ["luck-rises-at-24", "favorite-foreigners-2026", "oliver-burkeman-blog"]

_spec = importlib.util.spec_from_file_location("chk", ROOT / "tools" / "check.py")
chk = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(chk)

RIB_S, RIB_E = "<!-- 📝 draft-ribbon:start（tools/draft.py） -->", "<!-- 📝 draft-ribbon:end -->"
NAV_S, NAV_E = "<!-- 📝 draft-nav:start（tools/draft.py） -->", "<!-- 📝 draft-nav:end -->"
CSS_ID = "draft-css"
NOINDEX = '<meta name="robots" content="noindex, nofollow" /><!-- 📝 draft -->'
SOON_S, SOON_E = "<!-- 📝 coming-soon:start（tools/draft.py が作る。手で書かない） -->", "<!-- 📝 coming-soon:end -->"

PROD_BLOCKS = [  # 本番の道具が入れる「次・前・こちらもどうぞ・一覧に戻る」は、下書きでは外す
    re.compile(r'\n?[ \t]*<a class="next"[^>]*>.*?</a>\n?', re.S),
    re.compile(r"\n?[ \t]*<!-- ⏮ 前の記事へ.*?<!-- /⏮ -->\n?", re.S),
    re.compile(r"\n?[ \t]*<!-- ✨ こちらもどうぞ.*?<!-- /✨ -->\n?", re.S),
    re.compile(r"\n?[ \t]*<!-- 📚 一覧に戻る.*?<!-- /📚 -->\n?", re.S),
]
CSS = """<style id="draft-css">
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


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def mv(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if git("mv", str(src), str(dst)).returncode != 0:
        shutil.move(str(src), str(dst))


def load(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def slugs(d):
    return sorted(p.parent.name for p in d.glob("*/index.html"))


# ── 1本の下書きページを整える ─────────────────────────────
def to_draft_page(slug, doc, drafts, works, nxt):
    for rx in PROD_BLOCKS:
        doc = rx.sub("\n", doc)
    # 前の印を消すとき、行頭の空白も一緒に消す（残すと build のたびに空白が2つずつ増えていた・2026-09-30）
    doc = re.sub(r"[ \t]*" + re.escape(RIB_S) + r".*?" + re.escape(RIB_E) + r"\n?", "", doc, flags=re.S)
    doc = re.sub(r"(<main[^>]*>\n)[ \t]+\n", r"\1", doc, count=1)
    doc = re.sub(r"\n?[ \t]*" + re.escape(NAV_S) + r".*?" + re.escape(NAV_E) + r"\n?", "\n", doc, flags=re.S)
    doc = re.sub(r'<style id="draft-css">.*?</style>\n?', "", doc, flags=re.S)
    doc = doc.replace(NOINDEX + "\n", "")
    # トップへの道は、下書きの一覧へ
    doc = doc.replace('href="../../index.html#posts"', 'href="../index.html"').replace('href="../../index.html"', 'href="../index.html"')
    # ほかの記事へのリンク：下書きどうしはそのまま、本番の記事は ../../works/ へ
    def fix(m):
        s = m.group(2)
        if s in works and s not in drafts:
            return f'{m.group(1)}../../works/{s}/'
        return m.group(0)
    doc = re.sub(r'(href=")\.\./([a-z0-9-]+)/', fix, doc)
    doc = doc.replace('<div class="stage stage-public">PUBLIC</div>', '<div class="stage stage-draft">DRAFT</div>')
    doc = doc.replace(f"https://15-second-blog.com/works/{slug}/", f"https://15-second-blog.com/draft/{slug}/")
    doc = doc.replace("<head>", "<head>\n" + NOINDEX, 1)
    doc = doc.replace("</head>", CSS + "</head>", 1)
    rib = (f"  {RIB_S}\n  <div class=\"draft-ribbon\" translate=\"no\">📝 DRAFT · 下書き — まだ本番に出していません · "
           f"<a href=\"../index.html\">下書き一覧</a></div>\n  {RIB_E}\n")
    doc = re.sub(r"(<main[^>]*>\n?)", lambda m: m.group(1) + rib, doc, count=1)
    nav = [f"  {NAV_S}", '  <nav class="draft-nav" translate="no">']
    if nxt:
        en = load(DRAFT / nxt / "meta.json").get("title", nxt)
        ja = load(DRAFT / nxt / "i18n" / "ja.json").get("title") or en
        nav.append(f'    <a class="draft-next" href="../{nxt}/index.html"><span><small>NEXT DRAFT · 次の下書き</small>'
                   f'<span class="t">{html.escape(ja)}</span><small class="en">{html.escape(en)}</small></span><span aria-hidden="true">📝</span></a>')
    nav += ['    <a class="draft-back" href="../index.html">📝 ← 下書き一覧 / All drafts</a>',
            '    <a class="draft-prod" href="../../index.html">本番のサイトへ ↗</a>',
            "  </nav>", f"  {NAV_E}"]
    i = doc.rfind("</main>")
    return doc[:i] + "\n".join(nav) + "\n" + doc[i:]


def from_draft_page(slug, doc):
    """本番に戻すときに、下書きの印を外す（次・前・一覧に戻るは本番の道具が入れ直す）"""
    doc = re.sub(r"\n?[ \t]*" + re.escape(RIB_S) + r".*?" + re.escape(RIB_E) + r"\n?", "\n", doc, flags=re.S)
    doc = re.sub(r"\n?[ \t]*" + re.escape(NAV_S) + r".*?" + re.escape(NAV_E) + r"\n?", "\n", doc, flags=re.S)
    doc = re.sub(r'<style id="draft-css">.*?</style>\n?', "", doc, flags=re.S)
    doc = doc.replace("\n" + NOINDEX, "").replace(NOINDEX, "")
    doc = doc.replace('href="../index.html"', 'href="../../index.html"')
    doc = doc.replace('href="../../works/', 'href="../')
    doc = doc.replace('<div class="stage stage-draft">DRAFT</div>', '<div class="stage stage-public">PUBLIC</div>')
    doc = doc.replace(f"https://15-second-blog.com/draft/{slug}/", f"https://15-second-blog.com/works/{slug}/")
    return doc


# 🗂 下書きの一覧を「どうすれば出せるか」で分けて見せる（2026-10-03 の全体見直し・HANDOFF_2026-10-03.md の D）。
#    ここに無い下書きは、仕事の話（WORK_TOPICS）なら「💼 仕事の話」、それ以外は「🗂 そのほか」に入る。
#    出したら一覧から自然に消えるので、ここは消さなくてよい
GROUPS = [
    ("fix", "✏️ 少し直せば出せる", "本人に1つ確かめるか、仕事の言葉を消せば出せるもの",
     ["oliver-burkeman-blog", "favorite-foreigners-2026", "luck-rises-at-24", "sunway-college-visit",
      "baguio-strictest-school", "cabbage-and-black-pepper", "chu-shortcut-explain-simply", "chat-first-then-talk",
      "tidying-messy-notes-is-fun", "just-read-the-table-of-contents", "read-from-the-left", "boodle-fight-lunch",
      "no-public-scolding", "standing-desk-conversations"]),
    ("industry", "🏭 業界の話として出せそう", "会社が分からない、業界の一般的な話。続けて出さない・シリーズでつなげない",
     ["windows-update-day-slows-network", "faults-come-after-the-lightning", "radio-only-reaches-the-pole",
      "spare-machine-needs-config", "one-loose-plank-leaks-everything", "windows-shortcuts-i-learned", "why-not-japan",
      "en-to-jp-harder", "get-a-stamp", "trust-the-buffer", "countryside-internet-thanks", "maybe-a-mouse-chewed-it"]),
    ("work", "💼 仕事の話（業界の話に書き直してから）", "ブログ憲法 第1条：会社と仕事の中身は書かない。多くはこのまま置いておく", None),
    ("other", "🗂 そのほか", "", None),
    ("no", "🔒 出さない", "第1条・第2条に近いもの、または本人の判断待ち",
     ["a-note-for-japanese-readers", "big-company-harassment-transparency", "nice-escalation-sticker",
      "writing-the-outage-notice", "quiet-until-the-alarm", "three-monitors-twelve-screens", "minutes-in-one-minute",
      "gifts-from-students", "the-boss-looked-out-for-me", "subic-bay-and-clark-airport"]),
]

SHORT = {"fix": "✏️ 少し直す", "industry": "🏭 業界の話", "work": "💼 仕事の話", "other": "🗂 そのほか", "no": "🔒 出さない"}


def group_of(x):
    for key, _, _, slugs_ in GROUPS:
        if slugs_ and x["slug"] in slugs_:
            return key
    return "work" if x["topic"] in WORK_TOPICS else "other"


# ── 一覧に出す情報 ───────────────────────────────────
def info(slug):
    d = DRAFT / slug
    m = load(d / "meta.json")
    doc = (d / "index.html").read_text(encoding="utf-8")
    words = len(chk.body_words(doc))
    t = {"en": m.get("title", slug)}
    for l in ("ja", "ko", "zh", "zh-Hant"):
        x = load(d / "i18n" / f"{l}.json").get("title")
        if x:
            t[l] = x
    imgs = {p.name for p in (d / "images").glob("*")} if (d / "images").exists() else set()
    return {"slug": slug, "t": t, "date": m.get("date", ""), "seq": m.get("seq", 0), "topic": m.get("topic", ""),
            "words": words, "sec": max(1, round(words / (chk.WPM / 60))),
            "cover": "cover.jpg" in imgs, "thumb": (ROOT / "assets" / "thumbs" / f"{slug}.jpg").exists()}


def order(infos):
    return sorted(infos, key=lambda x: (x["date"], x["seq"]), reverse=True)


def index_html(infos, today, published):
    n = len(infos)
    cards = {}
    for x in infos:
        img = (f'<img src="../assets/thumbs/{x["slug"]}.jpg" alt="" loading="lazy">' if x["thumb"] else '<span>📝</span>')
        chips = [f'⚡ {x["words"]}語 · 約{x["sec"]}秒']
        if not x["cover"]:
            chips.append("🖼 表紙まだ")
        ja = f'<div class="ja">{html.escape(x["t"]["ja"])}</div>' if x["t"].get("ja") else '<div class="ja none">（日本語タイトルまだ）</div>'
        cards.setdefault(group_of(x), []).append(
            f'<a class="card" href="{x["slug"]}/index.html"><div class="th">{img}</div><div class="tx">{ja}'
            f'<div class="en">{html.escape(x["t"]["en"])}</div><div class="meta">{html.escape(x["date"])} · '
            + " · ".join(chips) + "</div></div></a>")
    secs, jump = [], []
    for key, title, note, _ in GROUPS:
        cs = cards.get(key)
        if not cs:
            continue
        jump.append(f'<a href="#g-{key}">{SHORT.get(key, title)} {len(cs)}</a>')
        secs.append(f'  <section class="grp" id="g-{key}">\n    <h2>{title} <small>{len(cs)}本</small></h2>\n'
                    + (f'    <p class="note">{note}</p>\n' if note else "")
                    + '    <div class="grid">\n' + "\n".join("      " + c for c in cs) + "\n    </div>\n  </section>")
    pub_pct = min(100, published / GOAL * 100)
    dr_pct = min(100 - pub_pct, n / GOAL * 100)
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="noindex, nofollow" />
<title>📝 下書き · Pengesso</title>
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png" />
<!-- 📝 このページは tools/draft.py build が作る。手で書かない -->
<style>
  :root {{ --bg: #fffaf0; --ink: #2d2a3a; --muted: #7a7288; --card: #fff; --line: rgba(45,42,58,.1); --pub: #5b7cfa; --dr: #ffc94a; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: radial-gradient(circle at 10% 0%, #fff0b8, transparent 32%), radial-gradient(circle at 95% 10%, #e6ecff, transparent 30%), var(--bg);
    color: var(--ink); font-family: "Hiragino Sans", "Hiragino Kaku Gothic ProN", system-ui, sans-serif; font-weight: 700; }}
  main {{ width: min(880px, calc(100% - 32px)); margin: 0 auto; padding: 26px 0 60px; }}
  h1 {{ margin: 6px 0 4px; font-size: clamp(28px, 6vw, 44px); font-weight: 900; letter-spacing: -.02em; }}
  .lead {{ margin: 0 0 18px; color: var(--muted); font-size: 14.5px; line-height: 1.7; }}
  .top a {{ color: var(--muted); font-size: 13.5px; }}
  .goal {{ padding: 18px 20px; border-radius: 22px; background: var(--card); border: 1.5px solid var(--line); margin-bottom: 20px; }}
  .goal b {{ font-size: 22px; }}
  .bar {{ display: flex; height: 16px; border-radius: 999px; overflow: hidden; background: rgba(45,42,58,.08); margin: 10px 0 8px; }}
  .bar .p {{ background: var(--pub); width: {pub_pct:.2f}%; }}
  .bar .d {{ background: repeating-linear-gradient(135deg, #ffc94a 0 8px, #ffdb7a 8px 16px); width: {dr_pct:.2f}%; }}
  .legend {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 13px; color: var(--muted); }}
  .legend i {{ display: inline-block; width: 12px; height: 12px; border-radius: 4px; vertical-align: -1px; margin-right: 5px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }}
  .card {{ display: flex; gap: 12px; padding: 12px; border-radius: 18px; background: var(--card); border: 1.5px solid var(--line);
    color: inherit; text-decoration: none; transition: transform .15s ease, box-shadow .15s ease; }}
  .card:hover, .card:focus-visible {{ transform: translateY(-2px); box-shadow: 0 10px 22px -12px rgba(45,42,58,.4); }}
  .card:focus-visible {{ outline: 3px solid #8b6de8; outline-offset: 2px; }}
  .th {{ flex: none; width: 72px; height: 72px; border-radius: 14px; overflow: hidden; background: #fff4c9; display: grid; place-items: center; font-size: 28px; }}
  .th img {{ width: 100%; height: 100%; object-fit: cover; }}
  .tx {{ min-width: 0; }}
  .ja {{ font-size: 15px; font-weight: 900; line-height: 1.45; }}
  .ja.none {{ color: var(--muted); font-weight: 700; }}
  .en {{ margin-top: 3px; font-size: 12.5px; color: var(--muted); line-height: 1.4; }}
  .meta {{ margin-top: 6px; font-size: 11.5px; color: var(--muted); }}
  .jump {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 8px; }}
  .jump a {{ padding: 8px 14px; border-radius: 999px; background: var(--card); border: 1.5px solid var(--line); color: inherit; text-decoration: none; font-size: 13.5px; }}
  .grp {{ margin-top: 26px; scroll-margin-top: 12px; }}
  .grp h2 {{ margin: 0 0 4px; font-size: 20px; font-weight: 900; }}
  .grp h2 small {{ font-size: 13px; color: var(--muted); }}
  .grp .note {{ margin: 0 0 12px; font-size: 13px; color: var(--muted); line-height: 1.6; }}
  .how {{ margin-top: 26px; padding: 16px 18px; border-radius: 18px; background: #fff; border: 1.5px dashed var(--line); font-size: 13.5px; line-height: 1.8; color: var(--muted); }}
  .how code {{ background: #f3f0fa; padding: 1px 6px; border-radius: 6px; color: var(--ink); }}
  @media (prefers-reduced-motion: reduce) {{ html:not([data-motion="on"]) .card {{ transition: none; }} }}
  html[data-motion="off"] .card {{ transition: none; }}
</style>
</head>
<body>
<main>
  <div class="top"><a href="../index.html">← 本番のサイト（15-second-blog.com）</a></div>
  <h1>📝 下書き <span style="font-size:.5em">{n}本</span></h1>
  <p class="lead">{today.year}年{today.month}月{today.day}日時点。ここは、まだ本番に出していない記事の置き場です（英語と日本語だけ）。<br>
  完成の形を見ながら直して、「本番に出して」で公開します。検索には出ません。</p>
  <section class="goal">
    <div>🎯 1000本まで：公開 <b>{published}</b> ＋ 下書き <b>{n}</b> ＝ {published + n}本</div>
    <div class="bar" role="img" aria-label="公開{published}本・下書き{n}本・目標1000本"><div class="p"></div><div class="d"></div></div>
    <div class="legend"><span><i style="background:var(--pub)"></i>公開 {published}</span><span><i style="background:var(--dr)"></i>下書き {n}</span><span>あと {max(0, GOAL - published - n)}本</span></div>
  </section>
  <nav class="jump" aria-label="下書きの種類">{" ".join(jump)}</nav>
{chr(10).join(secs) if secs else '<p>下書きはまだありません。</p>'}
  <div class="how">
    💡 <b>AIへの頼み方</b><br>
    「下書きにして」→ <code>python3 tools/draft.py new &lt;slug&gt;</code> で作って push（英日だけ・表紙はあとでいい）<br>
    「本番に出して」→ <code>python3 tools/draft.py publish &lt;slug&gt;</code> → 表紙の生成・英日韓中の訳・いつもの手順で push<br>
    本番から下書きに戻す → <code>python3 tools/draft.py move &lt;slug&gt;</code>
  </div>
</main>
</body>
</html>
"""


# ── 本番トップの「もうすぐ公開」 ─────────────────────────
def coming_soon(infos, today):
    peek = [x for x in order(infos) if x["topic"] not in WORK_TOPICS]
    # 2026-09-30 本人：チラ見せは3本だけ。元気でくだらなくて面白いタイトルを手で選ぶ（PEEK_PICKS）
    by = {x["slug"]: x for x in peek}
    picked = [by[s] for s in PEEK_PICKS if s in by]
    if len(picked) < 3:
        picked += [x for x in peek if x not in picked][:3 - len(picked)]
    data = {"asOf": today.isoformat(), "n": len(infos),
            "peek": [x["t"] for x in picked[:3]]}
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f"""    {SOON_S}
    <style>
      /* 📝 もうすぐ公開（2026-09-29 本人：下書きの本数と、タイトルのチラ見せで期待してもらう） */
      #goalBar {{ display: flex; }}
      .goal-draft {{ height: 100%; width: 0; background: repeating-linear-gradient(135deg, #ffc94a 0 7px, #ffdf85 7px 14px);
        transition: width 1.1s cubic-bezier(.22,1,.36,1) .5s; }}
      .soon {{ margin-top: 16px; padding: 14px 14px 12px; border-radius: 20px; background: #fff8dc; border: 2px dashed rgba(170,120,0,.28); }}
      .soon-head {{ display: flex; align-items: baseline; justify-content: space-between; gap: 6px 12px; flex-wrap: wrap; }}
      .soon-title {{ font-size: 15.5px; font-weight: 900; color: #6b4b00; }}
      .soon-count {{ font-size: 13px; font-weight: 800; color: #8a6a1a; }}
      .soon-peek {{ margin: 10px 0 2px; font-size: 12.5px; font-weight: 900; color: #8a6a1a; letter-spacing: .04em; }}
      .soon-list {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0; padding: 0; list-style: none; }}
      .soon-list li {{ position: relative; max-width: 100%; padding: 8px 12px 8px 34px; border-radius: 16px 16px 16px 4px; background: #fff;
        border: 1.5px solid rgba(170,120,0,.18); font-size: 13.5px; font-weight: 800; line-height: 1.45; color: #3d3320;
        opacity: 0; transform: translateY(6px) scale(.97); transition: opacity .4s ease, transform .4s ease; }}
      .soon-list li::before {{ content: "🐧"; position: absolute; left: 9px; top: 7px; font-size: 16px; }}
      .soon.in .soon-list li {{ opacity: 1; transform: none; }}
      .soon-more {{ margin: 8px 0 0; font-size: 12.5px; font-weight: 800; color: #8a6a1a; }}
      html[data-theme="dark"] .soon {{ background: #2e2a1c; border-color: rgba(255,220,130,.25); }}
      html[data-theme="dark"] .soon-list li {{ background: #22242f; color: #f4f0fa; border-color: rgba(255,255,255,.12); }}
      html[data-theme="dark"] :is(.soon-title,.soon-count,.soon-peek,.soon-more) {{ color: #ffe39a; }}
      @media (prefers-reduced-motion: reduce) {{ html:not([data-motion="on"]) .soon-list li {{ opacity: 1; transform: none; transition: none; }} html:not([data-motion="on"]) .goal-draft {{ transition: none; }} }}
      html[data-motion="off"] .soon-list li {{ opacity: 1; transform: none; transition: none; }} html[data-motion="off"] .goal-draft {{ transition: none; }}
    </style>
    <div class="soon" id="soon" translate="no"></div>
    <script>
    (function () {{
      var D = {payload};
      var box = document.getElementById('soon'), bar = document.getElementById('goalBar');
      if (!box || !D.n) {{ if (box) box.remove(); return; }}
      var L = (window.PENGESSO_LANG || 'en'), key = L === 'zh-Hant' ? 'zh-Hant' : (L in {{ja:1, ko:1, zh:1}} ? L : 'en');
      var d = D.asOf.split('-'), y = +d[0], m = +d[1], dd = +d[2];
      var MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
      var W = {{
        en: ['📝 Coming soon', 'As of ' + MON[m - 1] + ' ' + dd + ', ' + y + ', <b>' + D.n + ' drafts</b> are waiting', 'A peek at the titles 👀', 'and more…'],
        ja: ['📝 もうすぐ公開', y + '年' + m + '月' + dd + '日時点で、下書きが<b>' + D.n + '本</b>たまっています', 'タイトルだけチラ見せ 👀', 'ほかにも…'],
        ko: ['📝 곧 공개', y + '년 ' + m + '월 ' + dd + '일 기준, 초안 <b>' + D.n + '개</b>가 기다리고 있어요', '제목만 살짝 👀', '그리고 더…'],
        zh: ['📝 即将发布', '截至' + y + '年' + m + '月' + dd + '日，有<b>' + D.n + '篇</b>草稿在等待', '偷看一下标题 👀', '还有更多…'],
        'zh-Hant': ['📝 即將發布', '截至' + y + '年' + m + '月' + dd + '日，有<b>' + D.n + '篇</b>草稿在等待', '偷看一下標題 👀', '還有更多…']
      }}[key];
      var show = D.peek.slice(0, 3);
      function esc(s) {{ return String(s).replace(/[&<>"]/g, function (c) {{ return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]; }}); }}
      box.innerHTML = '<div class="soon-head"><div class="soon-title">' + W[0] + '</div><div class="soon-count">' + W[1] + '</div></div>' +
        '<p class="soon-peek">' + W[2] + '</p><ul class="soon-list">' +
        show.map(function (t) {{ return '<li>' + esc(t[key] || t.en) + '</li>'; }}).join('') + '</ul>' +
        (D.n > show.length ? '<p class="soon-more">' + W[3] + '</p>' : '');
      /* ゲージ：公開の青のうしろに、下書きの黄色いしましまを足す */
      if (bar) {{
        var seg = document.createElement('div'); seg.className = 'goal-draft'; bar.appendChild(seg);
        var w = Math.min(100, D.n / (window.GOAL || 1000) * 100);
        var go = function () {{ seg.style.width = w + '%'; box.classList.add('in'); }};
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {{ go(); return; }}
        var io = new IntersectionObserver(function (es) {{ if (es[0].isIntersecting) {{ io.disconnect(); requestAnimationFrame(go); }} }}, {{ threshold: 0.4 }});
        io.observe(box);
      }} else box.classList.add('in');
    }})();
    </script>
    {SOON_E}
"""


def build():
    drafts, works = set(slugs(DRAFT)), set(slugs(WORKS))
    infos = order([info(s) for s in drafts])
    seq = [x["slug"] for x in infos]
    for i, s in enumerate(seq):
        p = DRAFT / s / "index.html"
        doc = p.read_text(encoding="utf-8")
        new = to_draft_page(s, doc, drafts, works, seq[i + 1] if i + 1 < len(seq) else None)
        if new != doc:
            p.write_text(new, encoding="utf-8")
    # 下書きの訳は日本語だけ（英語は本文そのもの）
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "i18n.py"), "--draft"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout, r.stderr); raise SystemExit("❌ 下書きの訳の埋め込みに失敗")
    today = datetime.date.today()
    DRAFT.mkdir(exist_ok=True)
    (DRAFT / "index.html").write_text(index_html(infos, today, len(works)), encoding="utf-8")
    # 404.html が「いま書き直しています」と出すための一覧（下書きの slug だけ）
    (DRAFT / "slugs.json").write_text(json.dumps(sorted(drafts)) + "\n", encoding="utf-8")
    top = ROOT / "index.html"
    doc = top.read_text(encoding="utf-8")
    doc = re.sub(r"\n?[ \t]*" + re.escape(SOON_S) + r".*?" + re.escape(SOON_E) + r"\n?", "\n", doc, flags=re.S)
    anchor = '<p class="goal-note" id="goalNote"></p>\n'
    if anchor not in doc:
        raise SystemExit("❌ index.html に goal-note が見つかりません")
    doc = doc.replace(anchor, anchor + coming_soon(infos, today), 1)
    top.write_text(doc, encoding="utf-8")
    print(f"📝 下書き：{len(infos)}本（{today.isoformat()} 時点）→ draft/index.html と、本番トップの「もうすぐ公開」を作り直した")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 1
    cmd, rest = a[0], a[1:]
    if cmd == "move":
        for s in rest:
            if not (WORKS / s).exists():
                raise SystemExit(f"❌ works/{s} がありません")
            mv(WORKS / s, DRAFT / s)
            print(f"📝 works/{s} → draft/{s}")
        build()
    elif cmd == "publish":
        for s in rest:
            if not (DRAFT / s).exists():
                raise SystemExit(f"❌ draft/{s} がありません")
            p = DRAFT / s / "index.html"
            p.write_text(from_draft_page(s, p.read_text(encoding="utf-8")), encoding="utf-8")
            mv(DRAFT / s, WORKS / s)
            print(f"🚀 draft/{s} → works/{s}（このあと：表紙・英日韓中の訳・build-site ほかいつもの手順）")
        build()
    elif cmd == "new":
        s = rest[0]
        if (DRAFT / s).exists() or (WORKS / s).exists():
            raise SystemExit(f"❌ {s} はもうあります")
        d = DRAFT / s; (d / "images").mkdir(parents=True)
        today = datetime.date.today().isoformat()
        for f in ("index.html", "source.md"):
            (d / f).write_text((ROOT / "_template" / f).read_text(encoding="utf-8").replace("__SLUG__", s).replace("__DATE__", today), encoding="utf-8")
        (d / "meta.json").write_text(json.dumps({"title": s, "label": s, "date": today, "length": "15sec", "thumbAlt": "", "place": "nagoya", "topic": "life"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"📝 draft/{s} をつくった（本文を書いたら python3 tools/draft.py build）")
    elif cmd == "build":
        build()
    else:
        print(__doc__); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
