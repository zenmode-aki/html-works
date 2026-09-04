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
    "cebu":     ("Cebu 🌴",         "world", 11, 32),
    "baguio":   ("Baguio ⛰️",       "world", 10, 32),
    "bangkok":  ("Bangkok 🛺",      "world", 11, 29),
    "thailand": ("Kanchanaburi 🚂", "world", 10, 29),
}


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
            "   href:%r, thumb:%r,\n   title:%r},"
            % (m["slug"], m.get("label", ""), 15 if m.get("length") != "1min" else 60,
               m["words"], m.get("date", ""), int(m.get("age", 22)), place,
               f"works/{m['slug']}/index.html",
               f"assets/thumbs/{m['slug']}.jpg",
               m.get("title", m["slug"])))

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
