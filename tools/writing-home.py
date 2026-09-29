#!/usr/bin/env python3
"""
🏠 書く部屋（00_🏠 書く部屋.md）をつくる（2026-09-29 本人：「記事作成をもっと好きになれる環境を」）

  python3 tools/writing-home.py      （tools/prev-links.py が毎回最後に呼ぶ）

VS Code でいちばん上に出るファイル。**パソコンの中だけ**（.gitignore 済み。手元だけのネタ帳の題名も並ぶため）。開けば、
  ・いま何本あって、1000本まであと何本か（ゲージ）
  ・書きかけ・確認待ちの下書きが、状態の絵文字ごとに並ぶ（押すと開く）
  ・下書きサイトにある記事
  ・今日15分でできそうなこと（1つだけ）
がわかる。手で書かない（毎回作り直す）。
"""
import datetime, json, pathlib, random, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "00_🏠 書く部屋.md"
GOAL = 1000
LEGEND = [("🆕", "もらったまま"), ("✍️", "添削ずみ・確認待ち"), ("❓", "AIから質問あり"), ("⏸", "書きかけ"),
          ("🔧", "抜本的に直す（今は飛ばす）"), ("📝", "下書きサイトにある"), ("✅", "本番に公開ずみ"),
          ("🔒", "非公開にした"), ("📦", "資料・メモ")]
WAIT = ("🆕", "✍️", "❓", "⏸", "🔧")


def link(p):
    rel = p.relative_to(ROOT).as_posix()
    return "<" + rel + ">"


def main():
    works = [p.parent for p in (ROOT / "works").glob("*/index.html")]
    drafts = sorted((p.parent for p in (ROOT / "draft").glob("*/index.html")), key=lambda d: d.name)
    n, m = len(works), len(drafts)
    files = [p for p in ROOT.glob("[0-3][0-9]_*/**/*.txt") if p.is_file()]
    stat = {e: [] for e, _ in LEGEND}
    for p in files:
        mm = re.match(r"(?:\d+_)?(🆕|✍️|❓|⏸|🔧|📝|✅|🔒|📦)", p.name)
        if mm and "🇬🇧" not in p.name:
            stat[mm.group(1)].append(p)
    today = datetime.date.today()
    blocks = 40
    pub = round(n / GOAL * blocks); dr = max(0, min(blocks - pub, round(m / GOAL * blocks)))
    bar = "🟦" * pub + "🟨" * dr + "⬜" * (blocks - pub - dr)
    L = [f"# 🏠 書く部屋（{today.year}年{today.month}月{today.day}日）", "",
         "> ここは VS Code でいちばん上に出る、自分用の入口です。`python3 tools/writing-home.py` が毎回作り直すので、手で書かなくていい。", "",
         f"## 🎯 1000本まで", "", bar, "",
         f"**公開 {n}本** ＋ **下書き {m}本** ＝ {n + m}本　／　あと **{max(0, GOAL - n - m)}本**", "",
         "🟦 公開　🟨 下書きサイト　⬜ これから", "",
         "## 🌱 今日15分でできそうなこと", ""]
    pool = stat["✍️"] + stat["❓"] + stat["⏸"]
    if pool:
        random.seed(today.toordinal())
        pick = random.choice(pool)
        L += [f"- [{pick.stem}]({link(pick)}) を開いて、読み返して1文だけ直す（または「これ下書きにして」とAIに言う）", ""]
    elif drafts:
        L += [f"- 下書きサイトの1本を読んで、「本番に出して」か「ここ直して」を言う", ""]
    L += ["## ✍️ 手を動かすと進むもの", ""]
    for e, name in LEGEND:
        if e not in WAIT or not stat[e]:
            continue
        L.append(f"### {e} {name}（{len(stat[e])}）")
        L += [f"- [{p.stem}]({link(p)})" for p in sorted(stat[e], key=lambda x: x.as_posix())]
        L.append("")
    L += [f"## 📝 下書きサイト（{m}本）", "",
          "https://15-second-blog.com/draft/ で完成の形が見られる（英語と日本語だけ・検索には出ない）。", ""]
    for d in drafts:
        t = json.loads((d / "meta.json").read_text(encoding="utf-8")).get("title", d.name) if (d / "meta.json").exists() else d.name
        ja = d / "i18n" / "ja.json"
        if ja.exists():
            t = json.loads(ja.read_text(encoding="utf-8")).get("title") or t
        cover = "" if (d / "images" / "cover.jpg").exists() else " 🖼表紙まだ"
        L.append(f"- [{t}](https://15-second-blog.com/draft/{d.name}/){cover}")
    L += ["", "## 🗂 絵文字の意味", "", " ／ ".join(f"{e} {name}" for e, name in LEGEND), "",
          "## 💬 AIへの頼み方", "",
          "- 「これ下書きにして」→ 下書きサイトに HTML で出す（英日だけ・すぐ見られる）",
          "- 「本番に出して」→ 表紙を作って、英日韓中を訳して、本番へ",
          "- 「添削して」→ 原稿の上に添削、下に元のメモ。ファイル名の絵文字を ✍️ に", ""]
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"🏠 書く部屋：公開{n}・下書き{m}・書きかけ{sum(len(stat[e]) for e in WAIT)} → {OUT.name}")


if __name__ == "__main__":
    main()
