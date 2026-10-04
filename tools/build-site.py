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
    "clark":    ("Clark 🏫",        "world",  9, 32),
    "bangkok":  ("Bangkok 🛺",      "world", 11, 29),
    "thailand": ("Kanchanaburi 🚂", "world", 10, 29),
    "kl":       ("Kuala Lumpur 🇲🇾", "world", 13, 29),
    "seoul":    ("Seoul 🇰🇷",        "world",  6, 33),
    "mie":      ("Mie 🏎️",          "jp",    10,  6),
    "osaka":    ("Osaka 🏯",        "jp",    10,  5),
    "shiga":    ("Shiga 🌊",        "jp",     9,  5),
}


# 💼 職歴（JOBS）は持たない（2026-10-01 本人が決めた）
#    「働いた会社ごとに記録すると、かえって会社が特定できる。業界でまとめる。
#      会社のことと仕事の中身は書かない。業界の抽象的な話だけ書く」
#    トップの「Jobs he has had」の部屋もなくした。index.html の JOBS は空のまま作る。
JOBS = []
LEGACY_JOB_POSTS = {}


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
            "  {slug:%r, label:%r, len:%d, sec:%d, words:%d, date:%r, place:%r,\n"
            "   href:%r, thumb:%r,\n   title:%r, topic:%r%s},"
            % (m["slug"], m.get("label", ""), 15 if m.get("length") != "1min" else 60,
               max(1, m["sec"]), m["words"], m.get("date", ""), place,
               f"works/{m['slug']}/index.html",
               f"assets/thumbs/{m['slug']}.jpg",
               m.get("title", m["slug"]), m.get("topic", ""),
               # 🌐 "only": "ja" の記事は、日本語で見ている人にだけ、一覧のいちばん上に出す
               ((", only:%r" % m["only"]) if m.get("only") else "") +
               # 😊 気分で選ぶ（meta.json の "mood"）／💻 IT用語モードがある記事（works/<slug>/it.ja.json）
               ((", mood:%s" % json.dumps(m["mood"])) if m.get("mood") else "") +
               (", it:1" if (ROOT / "works" / m["slug"] / "it.ja.json").exists() else "") +
               # 🏷 タグ（meta.json の "tags"。名前と訳は i18n/tags.json）
               ((", tags:%s" % json.dumps(m["tags"])) if m.get("tags") else "")))

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

    # 🗂 ROOM_OF：meta.json の room から作る。
    #    💼 jobs の部屋はここに入れない（index.html 側で JOBS から自動で決まる）。
    #    2026-09-12：ここを手で書いていたせいで、仕事の記事31本が
    #    「Jobs he has had」から消えていたので、生成するようにした。
    room_of = {m["slug"]: m["room"] for m in sorted(items, key=lambda x: x["slug"])
               if m.get("room") and m["room"] != "jobs"}
    t, n4 = re.subn(r"(/\* ⬇️ ROOM_OF:START.*?⬇️ \*/\n)var ROOM_OF = .*?\n(/\* ⬆️ ROOM_OF:END)",
                    lambda mm: mm.group(1) + "var ROOM_OF = "
                    + json.dumps(room_of, ensure_ascii=False) + ";\n" + mm.group(2),
                    t, flags=re.S)
    if not n4:
        raise SystemExit("❌ index.html に ROOM_OF の目印が見つかりません。"
                         " /* ⬇️ ROOM_OF:START ⬇️ */ … /* ⬆️ ROOM_OF:END ⬆️ */ を消していませんか。")

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


def sitemap(items):
    """🔎 検索エンジン向けの記事の一覧（sitemap.xml）。/me/ と /goals/ は入れない（robots.txt で隠している）"""
    site = "https://15-second-blog.com/"
    newest = max((m.get("date", "") for m in items), default="")
    rows = [(site, newest), (site + "remember/", ""), (site + "stats/", "")]   # 📊 数字のページ（2026-10-04）
    rows += [(f"{site}works/{m['slug']}/", m.get("date", "")) for m in items]
    body = "".join(
        f"  <url><loc>{loc}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>\n"
        for loc, d in rows)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<!-- python3 tools/build-site.py が作る。手で書かない -->\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + '</urlset>\n')
    out = ROOT / "sitemap.xml"
    if not out.exists() or out.read_text(encoding="utf-8") != xml:
        out.write_text(xml, encoding="utf-8")
    print(f"✅ sitemap.xml  {len(rows)}ページ")


def main():
    posts = collect(ROOT / "works")
    inject(INDEX, posts)
    sitemap(posts)

    # 😊 気分のおすすめ（2026-10-03 本人の要望）：トップで気分を選んで入ってきた人に、記事のいちばん下で
    #    「同じ気分の記事をあと2本」を出す（tools/i18n_runtime.js の moodMore）。そのための小さな一覧。手で書かない
    rows = [[m["slug"], m.get("title", m["slug"]), max(1, m["sec"]), m["mood"]]
            for m in posts if m.get("mood") and not m.get("only")]
    out = ROOT / "assets" / "moods.json"
    js = json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + "\n"
    if not out.exists() or out.read_text(encoding="utf-8") != js:
        out.write_text(js, encoding="utf-8")

    missing = [m["slug"] for m in posts
               if not (ROOT / "assets" / "thumbs" / f"{m['slug']}.jpg").exists()]
    if missing:
        print(f"\n⚠️  サムネがまだ無い: {', '.join(missing)}")
        print("   python3 tools/thumbs.py  で作れます（macOSのみ）")

    # 💻 ☁️ 勉強モードの目印（2026-10-03）：<pack>.<lang>.json がある記事の <head> に
    #    <meta name="pengesso-it" content="it:en,ja gcp:en,ja net:en,ja,ko"> を入れる。ファイルを足したら自動で付く。手で書かない
    import re as _re
    for d in sorted((ROOT / "works").iterdir()):
        page = d / "index.html"
        if not page.exists():
            continue
        # 言い換えパック：💻 it ☁️ gcp 🌐 net 🖥 srv 🔐 sec 💼 biz。「net:ja,en,ko」の形で、読める言語を書く
        toks = []
        for pack in ("it", "gcp", "net", "srv", "sec", "biz", "fin", "med", "nur"):
            ls = sorted(f.name.split(".")[1] for f in d.glob(f"{pack}.*.json"))
            if ls:
                toks.append(f"{pack}:{','.join(ls)}")
        doc = page.read_text(encoding="utf-8")
        new = _re.sub(r'<meta name="pengesso-it"[^>]*>(<!--[^>]*-->)?\n?', "", doc)
        if toks:
            tag = f'<meta name="pengesso-it" content="{" ".join(toks)}">\n'
            m = _re.search(r'<meta name="viewport"[^>]*>\n', new)
            if m:
                new = new[:m.end()] + tag + new[m.end():]
        if new != doc:
            page.write_text(new, encoding="utf-8")

    # 🏷 記事の題の下のタグと、タグの名前の訳（2026-10-03）。i18n の前にやる
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import tags
        tags.main()
    except SystemExit as e:
        print(e)
    except Exception as e:
        print(f"⚠️  タグの更新に失敗しました（記事はそのまま動きます）: {e}")

    # 🔗 リンクを貼ったときのカード（OGP）も、全記事ぶん作り直す（2026-09-26）
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import ogp
        ogp.main_all()
    except Exception as e:
        print(f"⚠️  OGP の更新に失敗しました（記事はそのまま動きます）: {e}")

    # 🌐 トップの一覧のタイトルは、各記事の訳（works/<slug>/i18n/<lang>.json）から入る。
    #    一覧を作り直したら、訳の埋め込みもここで一緒にやり直す（忘れると新しい記事だけ英語になる）
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import i18n
        sys.argv = sys.argv[:1]
        i18n.main()
    except Exception as e:
        print(f"⚠️  訳の埋め込みに失敗しました（英語のページはそのまま動きます）: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
