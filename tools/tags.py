#!/usr/bin/env python3
"""
🏷 記事のタグ（2026-10-03 本人の要望）

  python3 tools/tags.py          全記事のタグを入れ直す（何度走らせても同じ結果）
  python3 tools/tags.py --check  meta.json のタグが i18n/tags.json にあるかだけ確かめる

  i18n/tags.json                 タグの一覧（絵文字・40言語の名前）。新しいタグはここに足す
  works/<slug>/meta.json "tags"  その記事のタグ（10個くらいまで。国・街 → 話題の順）

やること
  1. 記事の題（h1）のすぐ下に、タグのボタンを並べる（<!-- 🏷 タグ --> の目印の中。手で書かない）
     押すとトップの一覧が、そのタグの記事だけになる（index.html?tag=<id>#posts）
  2. タグの名前の訳を i18n/ui.<lang>.json と i18n/top.<lang>.json に入れる（40言語）
  3. トップページの TAGS（名前と絵文字）を書き直す

いつもの手順では build-site.py のあと、i18n.py の前に走らせる（build-site.py が呼ぶ）
"""
import json, pathlib, re, sys, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
VOCAB = I18N / "tags.json"
START, END = "<!-- 🏷 タグ（tools/tags.py） -->", "<!-- /🏷 -->"
BLOCK_RE = re.compile(r"\n?[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)

CSS = (
    "<style id=\"post-tags-css\">"
    ".post-tags{display:flex;flex-wrap:wrap;gap:6px;margin:-4px 0 18px}"
    ".post-tags a{display:inline-flex;align-items:center;padding:6px 11px;border-radius:999px;background:#fff;"
    "border:1.5px solid rgba(35,44,72,.12);color:#3a3550;font-size:12.5px;font-weight:800;line-height:1.2;text-decoration:none;"
    "transition:transform .15s,border-color .15s}"
    ".post-tags a:hover{transform:translateY(-1px);border-color:#8b6de8}"
    ".post-tags a.place{background:#f3effc}"
    "html[data-theme=\"dark\"] .post-tags a{background:#22242f;border-color:#33364a;color:#e6e2ff}"
    "html[data-theme=\"dark\"] .post-tags a.place{background:#2a2540}"
    "@media (prefers-reduced-motion:reduce){.post-tags a{transition:none}}"
    "</style>"
)


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def save_json(p, d):
    raw = p.read_text(encoding="utf-8")
    m = re.search(r'\n( +)"', raw)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=len(m.group(1)) if m else None) +
                 ("\n" if raw.endswith("\n") else ""), encoding="utf-8")


def label(t, lang="en"):
    return f"{t['e']} {t.get(lang) or t['en']}"


def main():
    vocab = load(VOCAB)["tags"]
    slugs = sorted(p.parent.name for p in (ROOT / "works").glob("*/meta.json"))
    bad = []
    for s in slugs:
        for t in load(ROOT / "works" / s / "meta.json").get("tags", []):
            if t not in vocab:
                bad.append((s, t))
    if bad:
        raise SystemExit("❌ i18n/tags.json にないタグ: " + ", ".join(f"{s}:{t}" for s, t in bad))
    if "--check" in sys.argv:
        print(f"✅ タグ OK（{len(vocab)}種類）")
        return

    # 1. 記事の題の下に並べる
    n = 0
    for s in slugs:
        page = ROOT / "works" / s / "index.html"
        if not page.exists():
            continue
        tags = load(ROOT / "works" / s / "meta.json").get("tags", [])
        doc = page.read_text(encoding="utf-8")
        new = BLOCK_RE.sub("\n", doc)
        if tags:
            place = ' class="place"'
            links = "".join(
                f'<a href="../../index.html?tag={t}#posts"{place if vocab[t].get("group") == "place" else ""}>'
                f'{html.escape(label(vocab[t]))}</a>' for t in tags)
            block = f'  {START}\n  {CSS}<nav class="post-tags" aria-label="Tags">{links}</nav>\n  {END}\n'
            m = re.search(r"</h1>[ \t]*\n", new)
            if not m:
                continue
            new = new[:m.end()] + block + new[m.end():]
        if new != doc:
            page.write_text(new, encoding="utf-8")
            n += 1

    # 2. 名前の訳（記事は ui、トップは top）
    for p in sorted(I18N.glob("ui.*.json")):
        lang = p.name.split(".", 1)[1].rsplit(".", 1)[0]
        for kind in ("ui", "top"):
            f = I18N / f"{kind}.{lang}.json"
            if not f.exists():
                continue
            d = load(f)
            dic = d.setdefault("dict", {})
            dic["Tags"] = {"ja": "タグ", "ko": "태그", "zh": "标签", "zh-Hant": "標籤"}.get(lang, dic.get("Tags", "Tags"))
            for t in vocab.values():
                if t.get(lang):
                    dic[label(t)] = label(t, lang)
                    if kind == "top":
                        dic[t["en"]] = t[lang]
            save_json(f, d)

    # 3. トップの TAGS
    top = ROOT / "index.html"
    doc = top.read_text(encoding="utf-8")
    js = "var TAGS = " + json.dumps({k: {"e": v["e"], "en": v["en"], "g": v.get("group", "topic")} for k, v in vocab.items()},
                                    ensure_ascii=False) + ";"
    new, k = re.subn(r"(/\* ⬇️ TAGS:START ⬇️ \*/\n).*?(\n/\* ⬆️ TAGS:END ⬆️ \*/)", lambda m: m.group(1) + js + m.group(2), doc, flags=re.S)
    if k and new != doc:
        top.write_text(new, encoding="utf-8")
    print(f"🏷 タグ：{len(vocab)}種類・{n}本の記事を更新")


if __name__ == "__main__":
    main()
