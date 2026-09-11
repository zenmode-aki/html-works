#!/usr/bin/env python3
"""
🏗 トップページに記事の一覧を差し込む

  python3 tools/build-site.py

    works/<slug>/meta.json  →  index.html の POSTS と PLACES

index.html は**手で書いて育てるページ**です（見た目・スロット・地図）。
このスクリプトが書き換えるのは、下の2か所にはさまれた中身だけ。

    /* ⬇️ POSTS:START  ⬇️ */ … /* ⬆️ POSTS:END  ⬆️ */
    /* ⬇️ PLACES:START ⬇️ */ … /* ⬆️ PLACES:END ⬆️ */

**この2か所を手で編集しない。** ここで作り直す。
Claude と ChatGPT/Codex の両方が同じリポジトリを触るので、
記事が増えるたびに一覧を手で書き足すと、必ず食い違うため。

words と sec は meta.json に書かない。記事HTMLから毎回数える
（tools/check.py の body_words を使う）ので、数字がズレることが原理的に起きない。

sips を使わない純Pythonなので、GitHub Actions（Ubuntu）でも動く。
サムネ画像そのものを作るのは tools/thumbs.py（macOS専用）の担当。
"""
import importlib.util
import json
import re
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

_spec = importlib.util.spec_from_file_location("chk", ROOT / "tools" / "check.py")
_chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_chk)


# 🗺 記事の「どこの話か」。ドットマップの何行目・何列目に印を出すかもここで決める。
#    meta.json の place がここに無いと build が止まるので、新しい土地は必ず足すこと。
PLACES = {
    "nagoya":   ("Nagoya 🏯",       "jp",    9,  6),
    "tokyo":    ("Tokyo 🗼",        "jp",    7,  8),
    "gifu":     ("Gifu 🌿",         "jp",    8,  6),
    "cebu":     ("Cebu 🌴",         "world", 11, 32),
    "baguio":   ("Baguio ⛰️",       "world", 10, 32),
    "bangkok":  ("Bangkok 🛺",      "world", 11, 29),
    "thailand": ("Kanchanaburi 🚂", "world", 10, 29),
}


# 💼 これまでに就いた仕事。左は index.html の JOBS の k と assets/jobs/<k>.jpg に対応。
#    posts は **meta.json の topic から自動で入る**（2026-09-11）。
#    手で記事名を書き足さない。書き足すと必ず古くなる。
#    topic が None の仕事（mcd / clark）は、記事がまだ無いので空のまま。
JOBS = [
    ("mcd",    "🍔", "Fast-food crew",    "Japan",                None),
    ("baguio", "🎒", "English student",   "Baguio, Philippines",  None),
    ("clark",  "🏫", "Language school",   "Clark, Philippines",   None),
    ("cebu",   "💻", "Bridge engineer",   "Cebu, Philippines",    "bridge"),
    ("netops", "🛠", "Network operations", "Japan",               "netops"),
]

# 手で仕事に割り当てておくぶん。足すのは次の2つの場合だけ。
#   1. topic が無かった時代の記事
#   2. **バッジの topic と、働いていた場所が食い違う記事**
#      セブ暮らしの記事は読者向けには 🇵🇭 LIVING IN THE PHILIPPINES を出したいが、
#      その暮らしはブリッジSEの時期そのものなので、cebu の仕事にも並べたい。
#      topic を "bridge" に変えると badge が仕事の話に見えてしまうので、ここで足す。
# それ以外の新しい記事は meta.json の topic で自動的に入るので、書き足さないこと。
LEGACY_JOB_POSTS = {
    "baguio": ["baguio-language-school-memories"],
    "cebu":   ["japan-philippines-work", "japan-philippines-shops",
               "no-public-scolding", "walking-on-the-7th-floor",
               "concierge-downstairs", "my-room-on-video", "120-eggs",
               "cebu-condo-poolside", "boodle-fight-lunch"],
}


def collect(base: pathlib.Path):
    """<base>/<slug>/meta.json を読んで、公開した順（新しい→古い）に並べる。

    並び順は meta.json の "seq" だけを見る。"date" は同じ日に何本も
    出す日が普通にあるので、並び順には使えない
    （2026-09-11 に、同じ日付の記事がslugのアルファベット順になってしまい、
    本人が「アップロード順になっていない」と指摘して直した）。

    "seq" は「そのファイルを最初に追加したコミット」を古い方から数えた通し番号。
    一度 tools/renumber-seq.py で全記事に割り振ったら、あとは新しい記事を
    足すたびに、そのときの最大値+1 を書くだけでいい。
    """
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
    # ⚠️ seq が無い記事は「一番新しい」ものとして扱う（気づきやすいよう先頭に出す）。
    #    tools/check.py --site が seq の無い記事を警告するので、見つけたら足すこと。
    return sorted(out, key=lambda m: (m.get("seq", 1 << 30), m.get("date", ""), m["slug"]), reverse=True)


def inject(page: pathlib.Path, items):
    """トップページの POSTS と PLACES を書き直す。"""
    rows, used = [], set()
    for m in items:
        place = m.get("place", "nagoya")
        if place not in PLACES:
            raise SystemExit(
                f"❌ {m['slug']}: meta.json の place \"{place}\" が tools/build-site.py の "
                f"PLACES にありません。地図に出す行・列を決めて足してください。")
        used.add(place)
        rows.append(
            "  {slug:%r, label:%r, len:%d, words:%d, date:%r, age:%d, place:%r,\n"
            "   href:%r, thumb:%r,\n   title:%r, topic:%r},"
            % (m["slug"], m.get("label", ""), 15 if m.get("length") != "1min" else 60,
               m["words"], m.get("date", ""), int(m.get("age", 22)), place,
               f"works/{m['slug']}/index.html",
               f"assets/thumbs/{m['slug']}.jpg",
               m.get("title", m["slug"]), m.get("topic", "")))

    places = "\n".join(
        "  %s: {name:%r, map:%r, row:%d, col:%d}," % (k, *PLACES[k])
        for k in PLACES if k in used)

    t = before = page.read_text(encoding="utf-8")
    t, n1 = re.subn(r"(/\* ⬇️ POSTS:START.*?⬇️ \*/\n)var POSTS = .*?\n(/\* ⬆️ POSTS:END)",
                    lambda mm: mm.group(1) + "var POSTS = [\n" + "\n".join(rows) + "\n];\n" + mm.group(2),
                    t, flags=re.S)
    t, n2 = re.subn(r"(/\* ⬇️ PLACES:START ⬇️ \*/\n)var PLACES = .*?\n(/\* ⬆️ PLACES:END)",
                    lambda mm: mm.group(1) + "var PLACES = {\n" + places + "\n};\n" + mm.group(2),
                    t, flags=re.S)

    # 💼 JOBS：meta.json の topic から、その仕事の記事を自動で入れる
    by_topic = {}
    for m in items:
        by_topic.setdefault(m.get("topic"), []).append(m["slug"])
    jobs = []
    for k, e, en, where, topic in JOBS:
        posts = list(LEGACY_JOB_POSTS.get(k, []))
        posts += [sl for sl in by_topic.get(topic, []) if sl not in posts]
        jobs.append("  {k:%r, e:%r, en:%r, where:%r, posts:%r}," % (k, e, en, where, posts))
    t, n3 = re.subn(r"(/\* ⬇️ JOBS:START.*?⬇️ \*/\n)var JOBS = .*?\n(/\* ⬆️ JOBS:END)",
                    lambda mm: mm.group(1) + "var JOBS = [\n" + "\n".join(jobs) + "\n];\n" + mm.group(2),
                    t, flags=re.S)
    if not n3:
        raise SystemExit("❌ index.html に JOBS の目印が見つかりません。"
                         " /* ⬇️ JOBS:START ⬇️ */ … /* ⬆️ JOBS:END ⬆️ */ を消していませんか。")

    if not (n1 and n2):
        raise SystemExit(
            f"❌ {page.name} に POSTS / PLACES の目印が見つかりません。\n"
            f"   /* ⬇️ POSTS:START ⬇️ */ … /* ⬆️ POSTS:END ⬆️ */ を消していませんか。")
    if t != before:
        page.write_text(t, encoding="utf-8")
    print(f"✅ {page.relative_to(ROOT)}  記事 {len(rows)}本を差し込みました "
          f"({len(t)/1024:.0f}KB)")


def main():
    posts = collect(ROOT / "works")
    inject(INDEX, posts)

    missing = [m["slug"] for m in posts
               if not (ROOT / "assets" / "thumbs" / f"{m['slug']}.jpg").exists()]
    if missing:
        print(f"\n⚠️  サムネがまだ無い: {', '.join(missing)}")
        print("   python3 tools/thumbs.py  で作れます（macOSのみ）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
