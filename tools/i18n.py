#!/usr/bin/env python3
"""
🌐 多言語化の道具

  python3 tools/i18n.py              全ページに訳と切り替えスクリプトを埋め込む
  python3 tools/i18n.py --check      訳が足りない文を数える（埋め込みはしない）
  python3 tools/i18n.py --todo SLUG  その記事の「まだ訳していない英文」を JSON で出す
  python3 tools/i18n.py --todo-top   トップページの「まだ訳していない英文」を出す

置き場所
  works/<slug>/i18n/<lang>.json   記事ごとの訳  {"title": "訳したタイトル", "text": {"英文": "訳"}}
  i18n/ui.<lang>.json             全記事に共通の言葉（Back / NEXT / 見出しの分類 など）と、切り替えに出す国旗
  i18n/top.<lang>.json            トップページの言葉
  i18n/top-data.<lang>.json       トップページで選んだ言語だけを読む、生成済みの訳
  tools/i18n_runtime.js           ブラウザで動く切り替えの本体

英文はそのまま残る。訳は「英文のかたまり → 訳」の対応表として、ページの中に JSON で埋め込む。
英文を書き直すと、その文の訳は外れて英語のまま表示される（--check で見つかる）。
言語を足すときは i18n/ui.<lang>.json と i18n/top.<lang>.json と works/*/i18n/<lang>.json を置き、
python3 tools/i18n.py で記事の埋め込みと i18n/top-data.<lang>.json を生成する。
"""
import hashlib, html, json, pathlib, re, sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"
I18N = ROOT / "i18n"
RUNTIME = ROOT / "tools" / "i18n_runtime.js"
START, END = "<!-- 🌐 i18n:start（python3 tools/i18n.py が作る。手で書かない） -->", "<!-- 🌐 i18n:end -->"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
INLINE = {"a", "abbr", "b", "br", "code", "em", "i", "mark", "q", "s", "small", "strong", "sub", "sup", "u", "time", "wbr"}
SKIP = {"script", "style", "noscript", "textarea", "select", "option", "template"}
ATTRS = ("placeholder", "title", "aria-label")
LETTER = re.compile(r"[A-Za-z]")


# ── ページを木にする（ブラウザと同じ見え方で「文のかたまり」を拾うため） ──
class Node:
    __slots__ = ("tag", "attrs", "kids", "parent")
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.kids, self.parent = tag, dict(attrs), [], parent


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.cur = self.root
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        if tag not in VOID:
            self.cur = n
    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, attrs, self.cur))
    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent
    def handle_data(self, data):
        self.cur.kids.append(data)


def parse(doc):
    t = Tree()
    t.feed(doc)
    return t.root


def text_of(n):
    if isinstance(n, str):
        return n
    return "".join(text_of(k) for k in n.kids)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def is_inline(n):
    """ブラウザ側と同じ。id / class 付きの要素は、JS が書き換える部品かもしれないので文に含めない"""
    return ((not isinstance(n, str)) and "class" not in n.attrs and "id" not in n.attrs
            and (n.tag in INLINE or n.tag == "span"))


def units(root):
    """ブラウザ側の walk() と同じ規則で、訳の鍵になる英文を順に集める"""
    out = []
    def walk(el):
        if isinstance(el, str) or el.tag in SKIP or el.attrs.get("translate") == "no":
            return
        for a in ATTRS:
            v = el.attrs.get(a)
            if v and LETTER.search(v):
                out.append(norm(v))
        parts, nodes, direct = [], [], False
        for c in el.kids:
            if isinstance(c, str):
                parts.append(c); nodes.append(c)
                if c.strip():
                    direct = True
            elif is_inline(c):
                parts.append(text_of(c)); nodes.append(c)
        if direct:
            k = norm("".join(parts))
            if LETTER.search(k):
                out.append(k)
        for c in el.kids:
            if isinstance(c, str):
                continue
            if direct and any(c is x for x in nodes):
                continue
            walk(c)
    body = find(root, "body") or root
    walk(body)
    return out


def find(n, tag, cls=None):
    if isinstance(n, str):
        return None
    if n.tag == tag and (cls is None or cls in n.attrs.get("class", "").split()):
        return n
    for k in n.kids:
        r = find(k, tag, cls)
        if r is not None:
            return r
    return None


def find_all(n, tag, cls=None, acc=None):
    acc = [] if acc is None else acc
    if isinstance(n, str):
        return acc
    if n.tag == tag and (cls is None or cls in n.attrs.get("class", "").split()):
        acc.append(n)
    for k in n.kids:
        find_all(k, tag, cls, acc)
    return acc


def direct_text(n):
    """h1 のように、飾り（🐧）を除いた地の文だけ"""
    return norm("".join(text_of(c) for c in n.kids if isinstance(c, str) or is_inline(c)))


def fp(s):
    """英文の短い指紋。ブラウザ側 fp() と同じ（UTF-16 の1単位ずつ FNV-1a 32bit → 36進数）"""
    h = 0x811c9dc5
    b = s.encode("utf-16-le")
    for i in range(0, len(b), 2):
        h ^= b[i] | (b[i + 1] << 8)
        h = (h * 16777619) & 0xFFFFFFFF
    n, out = h, ""
    while True:
        n, r = divmod(n, 36)
        out = "0123456789abcdefghijklmnopqrstuvwxyz"[r] + out
        if n == 0:
            return out


def minify(js):
    """コメントと行頭の空白だけ削る（ページを軽くするため。中身は変えない）"""
    js = re.sub(r"/\*[\s\S]*?\*/", "", js)
    return "\n".join(l.strip() for l in js.splitlines() if l.strip())


def pack(d, keys=None):
    """{英文: 訳} → {指紋: 訳}。keys を渡すと、そのページに出てくる英文だけに絞る"""
    out = {}
    for k, v in d.items():
        if keys is not None and k not in keys:
            continue
        out[fp(k)] = v
    return out


def strip_block(doc):
    return re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", doc, flags=re.S)


# ── 言語ごとのデータ ──────────────────────────────
def langs_available():
    return sorted(p.stem.split(".", 1)[1] for p in I18N.glob("ui.*.json"))


def load(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def article_info(slug):
    """その記事の英語の h1・<title>・次の記事の行き先"""
    doc = strip_block((WORKS / slug / "index.html").read_text(encoding="utf-8"))
    root = parse(re.sub(r'src="data:[^"]*"', 'src=""', doc))
    h1 = find(root, "h1")
    title = find(root, "title")
    nxt = find(root, "a", "next")
    nxt_slug = None
    if nxt is not None:
        m = re.search(r"\.\./([^/]+)/index\.html", nxt.attrs.get("href", ""))
        nxt_slug = m.group(1) if m else None
    nt = find(nxt, "div", "next-title") if nxt is not None else None
    prv = find(root, "a", "prev")          # ⏮ tools/prev-links.py が入れる「前の記事へ」
    prv_slug = None
    if prv is not None:
        m = re.search(r"\.\./([^/]+)/index\.html", prv.attrs.get("href", ""))
        prv_slug = m.group(1) if m else None
    pt = find(prv, "div", "prev-title") if prv is not None else None
    meta = load(WORKS / slug / "meta.json")
    return {
        "doc": doc, "root": root,
        "h1": direct_text(h1) if h1 is not None else None,
        "title": norm(text_of(title)) if title is not None else None,
        "meta_title": meta.get("title"),
        "next_slug": nxt_slug,
        "next_title": norm(text_of(nt)) if nt is not None else None,
        "prev_slug": prv_slug,
        "prev_title": norm(text_of(pt)) if pt is not None else None,
    }


def article_dict(slug, lang, info, titles):
    tr = load(WORKS / slug / "i18n" / f"{lang}.json")
    d = dict(tr.get("text", {}))
    t = tr.get("title")
    if t:
        for k in (info["h1"], info["title"], info["meta_title"]):
            if k:
                d[k] = t
    if info["next_slug"] and info["next_title"] and titles.get(info["next_slug"]):
        d[info["next_title"]] = titles[info["next_slug"]]
    if info["prev_slug"] and info["prev_title"] and titles.get(info["prev_slug"]):
        d[info["prev_title"]] = titles[info["prev_slug"]]
    return d


def all_titles(lang):
    out = {}
    for p in WORKS.glob(f"*/i18n/{lang}.json"):
        t = load(p).get("title")
        if t:
            out[p.parent.parent.name] = t
    return out


def ui_meta(ui):
    """切り替えメニューと注意書きに必要な、本文以外の小さな情報"""
    return {"name": ui.get("name"), "englishName": ui.get("englishName"),
            "aliases": ui.get("aliases", []), "flag": ui.get("flag"),
            "patterns": ui.get("patterns", []),
            "unverified": ui.get("unverified", False),
            "notice": ui.get("notice"), "noticeDismiss": ui.get("noticeDismiss")}


def json_asset(data):
    return (json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def block(data):
    js = minify(RUNTIME.read_text(encoding="utf-8"))
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return (f"{START}\n<script type=\"application/json\" id=\"i18n-data\">{payload}</script>\n"
            f"<script>\n{js}</script>\n{END}\n")


def inject(path, data):
    doc = strip_block(path.read_text(encoding="utf-8"))
    # <head> に置く：言語をページのスクリプトより先に決めたいので（トップの「日本語だけの記事」）。
    # 訳す処理そのものは、ページを読み終わってから（DOMContentLoaded）動く
    i = doc.find("</head>")
    if i < 0:
        raise SystemExit(f"❌ {path} に </head> がありません")
    new = doc[:i] + block(data) + doc[i:]
    if new != path.read_text(encoding="utf-8"):
        path.write_text(new, encoding="utf-8")
        return True
    return False


def missing(keys, d, patterns):
    pats = [re.compile(p[0]) for p in patterns]
    def ok(k):
        if k in d or any(p.search(k) for p in pats):
            return True
        m = re.match(r"^(.*\D)\s+(\d+)$", k)
        if m and LETTER.search(m.group(1)) and ok(m.group(1)):
            return True
        if " · " in k:
            return all((not LETTER.search(x)) or ok(x) for x in k.split(" · "))
        return False
    seen, out = set(), []
    for k in keys:
        if k not in seen and not ok(k):
            seen.add(k); out.append(k)
    return out


def top_labels(lang, slugs, d):
    """🏷 トップの一覧に出る各記事の短いラベル（meta.json の label）。
    2026-09-25：タイトルしか自動で入っておらず、ラベルが英語のまま残っても --check が気づかなかった。
    訳は works/<slug>/i18n/<lang>.json の "label"（なければ i18n/top.<lang>.json の dict）に置く。
    返り値：まだ訳のないラベルの英文"""
    miss = []
    for s in slugs:
        label = load(WORKS / s / "meta.json").get("label")
        if not label:
            continue
        t = load(WORKS / s / "i18n" / f"{lang}.json").get("label")
        if t:
            d[label] = t
        if label not in d:
            miss.append(label)
    return miss


def build_all():
    """全ページぶんの埋め込みデータと、訳の抜けを計算する（書き込みはしない）"""
    langs = langs_available()
    slugs = sorted(p.parent.name for p in WORKS.glob("*/index.html"))
    uis = {l: load(I18N / f"ui.{l}.json") for l in langs}
    tops = {l: load(I18N / f"top.{l}.json") for l in langs}
    titles = {l: all_titles(l) for l in langs}
    pages, report, infos = [], [], {s: article_info(s) for s in slugs}

    for slug in slugs:
        info = infos[slug]
        data = {"langs": {}}
        for l in langs:
            if not (WORKS / slug / "i18n" / f"{l}.json").exists():
                report.append((slug, l, ["（訳のファイルがまだありません）"]))
                continue
            d = dict(uis[l].get("dict", {}))
            d.update(article_dict(slug, l, info, titles[l]))
            ks = units(info["root"])
            used = set(ks) | {info["title"]} | set(p for k in ks for p in k.split(" · "))
            data["langs"][l] = {"name": uis[l].get("name", l),
                                "englishName": uis[l].get("englishName"),
                                "aliases": uis[l].get("aliases", []), "flag": uis[l].get("flag"),
                                "dict": pack(d, used), "patterns": uis[l].get("patterns", []),
                                "unverified": uis[l].get("unverified", False),
                                "notice": uis[l].get("notice"), "noticeDismiss": uis[l].get("noticeDismiss")}
            miss = missing(ks, d, uis[l].get("patterns", []))
            if miss:
                report.append((slug, l, miss))
        pages.append((WORKS / slug / "index.html", data))

    # トップページ：記事のタイトルとラベルは各記事の訳から自動で入る（ラベルは "label"。top_labels を見る）
    top = ROOT / "index.html"
    tdata = {"lazyTop": True, "langs": {}}
    top_assets = {}
    for l in langs:
        if not tops[l]:
            continue
        d = dict(tops[l].get("dict", {}))
        for s in slugs:
            t = titles[l].get(s)
            if t and infos[s]["meta_title"]:
                d[infos[s]["meta_title"]] = t
        label_miss = top_labels(l, slugs, d)
        tdata["langs"][l] = {**ui_meta(uis[l]), "name": uis[l].get("name", l), "dict": {}}
        top_assets[I18N / f"top-data.{l}.json"] = {
            "dict": pack(d), "patterns": tops[l].get("patterns", [])}
        # 🔄 2026-09-25：訳のファイルはブラウザに10分ほど残る。文を直した直後に古い訳を読んで
        #    英語が混ざらないよう、中身が変わったら URL も変わるように版の印（ハッシュ）を付ける
        tdata["langs"][l]["v"] = hashlib.sha1(json_asset(top_assets[I18N / f"top-data.{l}.json"])).hexdigest()[:10]
        miss = missing(units(parse(strip_block(top.read_text(encoding="utf-8")))), d, tops[l].get("patterns", [])) + label_miss
        if miss:
            report.append(("(トップページ)", l, miss))
    pages.append((top, tdata))
    return langs, titles, pages, report, top_assets


def status():
    """check.py --site から呼ぶ。(訳の抜け, 埋め込みや生成データが古いページ) を返す"""
    langs, titles, pages, report, top_assets = build_all()
    stale = []
    for path, data in pages:
        doc = path.read_text(encoding="utf-8")
        i = doc.find(START)
        cur = doc[i:doc.find(END) + len(END) + 1] if i >= 0 else ""
        if cur != block(data):
            stale.append(path.parent.name if path.name == "index.html" and path.parent != ROOT else "index.html")
    for path, data in top_assets.items():
        if not path.exists() or path.read_bytes() != json_asset(data):
            stale.append(path.relative_to(ROOT).as_posix())
    return langs, report, stale


def main():
    args = sys.argv[1:]
    langs = langs_available()
    uis = {l: load(I18N / f"ui.{l}.json") for l in langs}
    tops = {l: load(I18N / f"top.{l}.json") for l in langs}

    if args[:1] == ["--todo"]:
        titles = {l: all_titles(l) for l in langs}
        slug = args[1]; lang = args[2] if len(args) > 2 else "ja"
        info = article_info(slug)
        d = article_dict(slug, lang, info, titles[lang]); d.update(uis[lang].get("dict", {}))
        todo = missing(units(info["root"]), d, uis[lang].get("patterns", []))
        print(json.dumps(todo, ensure_ascii=False, indent=1))
        return 0

    if args[:1] == ["--todo-top"]:
        titles = {l: all_titles(l) for l in langs}
        lang = args[1] if len(args) > 1 else "ja"
        doc = strip_block((ROOT / "index.html").read_text(encoding="utf-8"))
        d = dict(tops[lang].get("dict", {}))
        for s in sorted(p.parent.name for p in WORKS.glob("*/index.html")):
            info = article_info(s)
            t = titles[lang].get(s)
            if t and info["meta_title"]:
                d[info["meta_title"]] = t
        slugs = sorted(p.parent.name for p in WORKS.glob("*/index.html"))
        label_miss = top_labels(lang, slugs, d)
        todo = missing(units(parse(doc)), d, tops[lang].get("patterns", [])) + label_miss
        print(json.dumps(todo, ensure_ascii=False, indent=1))
        return 0

    check_only = "--check" in args
    langs, titles, pages, report, top_assets = build_all()
    changed = 0
    assets_changed = 0
    if not check_only:
        for path, data in pages:
            if inject(path, data):
                changed += 1
        for path, data in top_assets.items():
            output = json_asset(data)
            if not path.exists() or path.read_bytes() != output:
                path.write_bytes(output)
                assets_changed += 1

    done = {l: len(titles[l]) for l in langs}
    print(f"🌐 言語: en + {', '.join(langs) or '（なし）'}   訳のある記事: {done}   書き換えたページ: {changed}   トップ訳データ: {assets_changed}件更新")
    if report:
        print(f"⚠️  訳が足りないページ: {len(report)}（その文は英語のまま表示されます）")
        for slug, l, miss in report[:40]:
            print(f"   {slug} [{l}] {len(miss)}文  例: {miss[0][:70]}")
    else:
        print("✅ 訳の抜けはありません")
    return 1 if (check_only and report) else 0


if __name__ == "__main__":
    sys.exit(main())
