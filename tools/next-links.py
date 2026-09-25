#!/usr/bin/env python3
"""⏭ 全記事の「次の記事へ」を、1本の道にそろえる（2026-09-25 本人の要望：次へを押していくとループする）。

前は、記事ごとに手で「次」を決めていたので、
  ・A → B → A のようにループする
  ・どこからも「次」で来られない記事がある
  ・「次」がない記事がある
が起きていた。これからは手で決めない。この道具が並べる。

並べ方（2026-09-25 本人：マレーシアの記事の次が、いきなり名古屋の話になる。
「次の記事で書きます」と書いた記事の次には、ちゃんとその記事が来てほしい）：
  1. 記事を「章」に分ける。旅や海外は国ごと（フィリピンはバギオ → クラーク → セブの順）、
     名古屋の記事は話題（topic）ごと。暮らし（life）はトップの「部屋」ごと。
     meta.json に "chapter": "nagoya-town" のように書けば、その章に入る。
  2. 章の中では、原稿フォルダの番号（「マレーシア/記事/01_…」の 01, 02, 03…）の順に読む。
     シリーズ（Part 1・2・3、韓国の野球場のような帯）は、Part 1 → 2 → 3 の順でひとかたまり。
     かたまりどうし・番号のない記事は、書いた順（古い順）。
  3. 章どうしは、海外の章 → 国内の旅 → そのほか、の順。その中では「新しい記事がある章が先」。
  4. どうしても決めたい並びは meta.json に "follows": "<前に来る記事のslug>" と書く。
     その記事のすぐ次に置かれる（ほかのルールより強い）。
いちばん最後の記事の「次」は、トップの一覧へ。

使い方: python3 tools/next-links.py   → そのあと tools/prev-links.py → tools/i18n.py
何度走らせても同じ結果になる。記事を足したら毎回走らせる。
"""
import collections, html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"

NEXT_RE = re.compile(r'[ \t]*(?:<!-- ⚡ 次の記事へ[^\n]*-->\s*)?<a class="next"[^>]*>.*?</a>[ \t]*\n?', re.S)
CSS_MARK = "/* ⏭ 次の記事へ（tools/next-links.py） */"
CSS = CSS_MARK + """
  .next { display: flex; align-items: center; justify-content: space-between; gap: 14px;
    margin-top: 34px; min-height: 44px; padding: 20px 24px; border-radius: 28px; text-decoration: none;
    background: linear-gradient(135deg, var(--purple, #8b6de8), var(--pink, #ff6fae)); color: #fff;
    box-shadow: 0 20px 55px rgba(0,0,0,.14); transition: transform .18s ease; }
  .next:hover, .next:focus-visible { transform: translateY(-4px); }
  .next-kicker { font-size: 11.5px; font-weight: 900; letter-spacing: .18em; opacity: .82; }
  .next-title { margin-top: 4px; font-size: clamp(17px, 3vw, 21px); line-height: 1.3; }
  .next-arrow { font-size: 26px; flex: 0 0 auto; }
  @media (prefers-reduced-motion: reduce) { .next { transition: none; } }
"""


def series_key(doc):
    m = re.search(r'<nav class="part-nav"[^>]*aria-label="([^"]*)"', doc)
    if m:
        return "nav:" + m.group(1)
    m = re.search(r'<div class="series"[^>]*>([^<]*)</div>', doc)
    if m:
        return "band:" + m.group(1).strip()
    return None


# 🗺 章の分け方。ここにない場所は、その場所の名前でひとつの章になる
CHAPTER = {"baguio": "ph", "clark": "ph", "cebu": "ph", "seoul": "kr", "kl": "my",
           "bangkok": "th", "thailand": "th", "tokyo": "jp-trip", "gifu": "jp-trip", "mie": "jp-trip"}
# 同じ章の中で、どの街から読むか（住んだ順）
PLACE_RANK = {"baguio": 0, "clark": 1, "cebu": 2}
FOLDER_RE = re.compile(r"## 出どころ\s*\n+(?:[^\n]*?)([^/\n]+)/記事/(\d+)_")


ABROAD = {"ph", "kr", "my", "th"}          # 海外の章は、ひとかたまりで続けて読めるようにする
TRIPS = {"jp-trip", "home:travel"}         # その次に、国内の旅と旅のコツ


def chapter(m):
    if m.get("chapter"):                   # meta.json で章を決め打ちできる（名古屋の街の話など）
        return m["chapter"]
    place = m.get("place") or ""
    if place in CHAPTER:
        return CHAPTER[place]
    if place and place != "nagoya":
        return place
    topic = m.get("topic") or "other"
    if topic == "life":                    # 暮らしの話は数が多いので、トップの「部屋」ごとに分ける
        return "life:" + (m.get("room") or "other")
    return "home:" + topic


def order():
    posts = {}
    for d in WORKS.iterdir():
        if (d / "index.html").exists() and (d / "meta.json").exists():
            m = json.loads((d / "meta.json").read_text())
            src = (d / "source.md").read_text() if (d / "source.md").exists() else ""
            f = FOLDER_RE.search(src)
            posts[d.name] = {"seq": m.get("seq", 0), "title": m.get("title", d.name),
                             "series": series_key((d / "index.html").read_text()),
                             "folder": (f.group(1), int(f.group(2))) if f else None,
                             "chapter": chapter(m), "rank": PLACE_RANK.get(m.get("place"), 9),
                             "follows": m.get("follows")}

    # かたまり（block）を作る：シリーズ → 原稿フォルダの番号順 → 1本だけの記事
    blocks, used = [], set()
    by = {}
    for s, p in posts.items():
        if p["series"]:
            by.setdefault(("series", p["series"]), []).append(s)
    for k, ms in by.items():
        ms.sort(key=lambda x: posts[x]["seq"]); blocks.append({"posts": ms, "loose": False}); used.update(ms)
    by = {}
    for s, p in posts.items():
        if s not in used and p["folder"]:
            by.setdefault((p["chapter"], p["folder"][0]), []).append(s)
    for k, ms in by.items():
        ms.sort(key=lambda x: (posts[x]["folder"][1], posts[x]["seq"]))
        blocks.append({"posts": ms, "loose": len(ms) == 1}); used.update(ms)
    for s in posts:
        if s not in used:
            blocks.append({"posts": [s], "loose": True})

    # かたまりを章に入れる（かたまりの中でいちばん多い章。知識メタボの Part 1 だけ東京、などに引っぱられない）
    chapters = {}
    for b in blocks:
        ch = collections.Counter(posts[x]["chapter"] for x in b["posts"]).most_common(1)[0][0]
        b["key"] = (min(posts[x]["rank"] for x in b["posts"]), min(posts[x]["seq"] for x in b["posts"]))
        chapters.setdefault(ch, []).append(b)
        for x in b["posts"]:
            posts[x]["chapter"] = ch          # シリーズの途中で「話が変わります」と出さないように
    out = []
    def newest(c): return max(posts[x]["seq"] for b in chapters[c] for x in b["posts"])
    def group(c): return 0 if c in ABROAD else 1 if c in TRIPS else 2
    for c in sorted(chapters, key=lambda c: (group(c), -newest(c))):
        for b in sorted(chapters[c], key=lambda b: b["key"]):
            out.extend(b["posts"])

    # "follows" の指定は最後に反映する（指定された記事のすぐ次へ移す）
    #  A→B→C のように続けて指定しても崩れないよう、並びが変わらなくなるまでくり返す
    for _ in range(len(posts)):
        before = list(out)
        for s, p in sorted(posts.items(), key=lambda kv: kv[1]["seq"]):
            f = p["follows"]
            if f in posts and f != s and out.index(s) != out.index(f) + 1:
                out.remove(s); out.insert(out.index(f) + 1, s)
        if out == before:
            break
    return posts, out


def block(target, posts, here=None):
    if target is None:
        return ('  <a class="next" href="../../index.html">\n    <div>\n'
                '      <div class="next-kicker">NEXT · ALL POSTS</div>\n'
                '      <div class="next-title">See all 15-second posts</div>\n    </div>\n'
                '    <div class="next-arrow" aria-hidden="true">⚡</div>\n  </a>\n')
    t = html.escape(posts[target]["title"], quote=False)
    # 章が変わるところでは「話が変わります」と先に言う（2026-09-25：マレーシアの次に急に名古屋の話が来て戸惑う）
    new = here is not None and posts[here]["chapter"] != posts[target]["chapter"]
    attr = ' data-topic="new"' if new else ""
    kicker = "NEXT · NEW TOPIC" if new else "NEXT · 15 SEC"
    arrow = "🔀" if new else "⚡"
    return (f'  <a class="next" href="../{target}/index.html"{attr}>\n    <div>\n'
            f'      <div class="next-kicker">{kicker}</div>\n'
            f'      <div class="next-title">{t}</div>\n    </div>\n'
            f'    <div class="next-arrow" aria-hidden="true">{arrow}</div>\n  </a>\n')


def main():
    posts, seq = order()
    changed = 0
    for i, s in enumerate(seq):
        target = seq[i + 1] if i + 1 < len(seq) else None
        p = WORKS / s / "index.html"
        doc = p.read_text()
        new_block = block(target, posts, s)
        main_end = doc.rindex("</main>")
        m = NEXT_RE.search(doc, 0, main_end)
        if m:
            new = doc[:m.start()] + new_block + doc[m.end():]
        else:
            k = doc.find("<!-- ⏮ 前の記事へ", 0, main_end)
            at = k if k >= 0 else main_end
            new = doc[:at] + new_block + doc[at:]
        if not re.search(r"\.next\s*\{", new) and CSS_MARK not in new:
            new = new.replace("</style>", CSS + "</style>", 1)
        if new != doc:
            p.write_text(new)
            changed += 1
    print(f"⏭ 次の記事へ：{len(seq)}本を1本の道に並べた（{changed}本を書き換え）。最初は {seq[0]}、最後は {seq[-1]} → トップ")


def verify():
    """check.py から呼ぶ：ループ・行き止まり・たどり着けない記事がないか"""
    posts, _ = order()
    nx = {}
    for s in posts:
        m = re.search(r'<a class="next" href="\.\./([^/"]+)/index\.html"', (WORKS / s / "index.html").read_text())
        nx[s] = m.group(1) if m and m.group(1) != ".." else None
    problems = [f"{s}：次の記事がありません" for s in posts if s not in nx]
    heads = [s for s in posts if s not in set(nx.values())]
    if len(heads) != 1:
        problems.append(f"「次」でたどり着けない記事が {len(heads)} 本あります（1本だけのはず）: {heads[:5]}")
    seen, cur = set(), heads[0] if heads else None
    while cur and cur not in seen:
        seen.add(cur); cur = nx.get(cur)
    if cur:
        problems.append(f"ループしています：{cur} に戻ってきます")
    elif len(seen) != len(posts):
        problems.append(f"1本の道にならず、{len(posts) - len(seen)} 本がはぐれています")
    return problems


if __name__ == "__main__":
    main()
