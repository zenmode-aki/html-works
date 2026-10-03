"""Helper for bulk article edits (scratchpad only, not part of the repo).

Usage from a python script:
    import sys; sys.path.insert(0, SCRATCH); from fix import *
    en(slug, old, new, ja=(old_ja_fragment, new_ja_fragment), keep=True)
    ja(slug, old_ja_fragment, new_ja_fragment)          # Japanese only, no key change
    title(slug, en_new=None, ja_new=None)
"""
import json, pathlib, re, html as H

ROOT = pathlib.Path("/Users/ezakimasaaki/Desktop/html-works")
MAIN = ("ko", "zh", "zh-Hant")
LOG = []


def _dir(slug):
    for base in ("works", "draft"):
        d = ROOT / base / slug
        if d.exists():
            return d
    raise SystemExit(f"no such slug {slug}")


def _langs(d):
    return sorted(p for p in (d / "i18n").glob("*.json") if not p.name.startswith("data."))


_IND = {}


def _load(p):
    t = p.read_text(encoding="utf-8")
    m = re.search(r'\n( +)"', t)
    _IND[str(p)] = (len(m.group(1)) if m else 1, t.endswith("\n"))
    return json.loads(t)


def _save(p, j):
    ind, nl = _IND.get(str(p), (1, True))
    p.write_text(json.dumps(j, ensure_ascii=False, indent=ind) + ("\n" if nl else ""), encoding="utf-8")


def _html_variants(s):
    # the page may store ’ etc. literally or as entities; try literal first, then escaped
    yield s
    yield H.escape(s, quote=False)


def en(slug, old, new, ja=None, keep=True, count=None):
    """Change an English sentence/fragment in index.html and re-key every language file.

    ja   : (old_fragment, new_fragment) applied to the Japanese value, or a full new value (str).
    keep : True  -> other languages keep their old translation under the new key (grammar-only fix)
           False -> other languages (incl. ko/zh/zh-Hant) lose the key and will be re-translated
    """
    d = _dir(slug)
    idx = d / "index.html"
    doc = idx.read_text(encoding="utf-8")
    for v in _html_variants(old):
        n = doc.count(v)
        if n:
            break
    if n == 0 and (new in doc or H.escape(new, quote=False) in doc):
        print(f"↷ {slug}: already changed: {new[:50]!r}")
        return
    if (count is None and n == 0) or (count is not None and n != count):
        raise SystemExit(f"❌ {slug}: expected {count} of {old!r} in index.html, found {n}")
    doc = doc.replace(v, new if v == old else H.escape(new, quote=False))
    idx.write_text(doc, encoding="utf-8")
    hit = 0
    for p in _langs(d):
        j = _load(p)
        t = j.get("text", {})
        nt = {}
        for k, val in t.items():
            if old in k:
                hit += 1
                k2 = k.replace(old, new)
                if p.stem == "ja" and ja is not None:
                    if isinstance(ja, str):
                        val = ja
                    else:
                        if ja[0] not in val:
                            raise SystemExit(f"❌ {slug} ja: {ja[0]!r} not in {val!r}")
                        val = val.replace(ja[0], ja[1])
                    nt[k2] = val
                elif p.stem == "ja" or keep:
                    nt[k2] = val
                # else: dropped -> re-translate later
            else:
                nt[k] = val
        j["text"] = nt
        _save(p, j)
    if not hit:
        print(f"⚠️ {slug}: {old[:50]!r} not found as a key in any i18n file (ok if it is inside a longer unit that changed before)")
    LOG.append((slug, "en", old, new))


def ja(slug, old, new):
    """Japanese translation only (no key change). Searches title and all values."""
    d = _dir(slug)
    p = d / "i18n" / "ja.json"
    j = _load(p)
    n = 0
    if old in j.get("title", ""):
        j["title"] = j["title"].replace(old, new); n += 1
    for k, v in j.get("text", {}).items():
        if old in v:
            j["text"][k] = v.replace(old, new); n += 1
    if "label" in j and old in j["label"]:
        j["label"] = j["label"].replace(old, new); n += 1
    if not n:
        if new in json.dumps(j, ensure_ascii=False):
            print(f"↷ {slug} ja: already changed: {new[:40]!r}")
            return 0
        raise SystemExit(f"❌ {slug} ja: {old!r} not found")
    _save(p, j)
    LOG.append((slug, "ja", old, new))
    return n


def title(slug, en_new=None, ja_new=None, keep=True):
    d = _dir(slug)
    if en_new and _load(d / "meta.json")["title"] == en_new:
        en_new = None
    if en_new:
        m = d / "meta.json"
        mj = _load(m)
        old = mj["title"]
        mj["title"] = en_new
        _save(m, mj)
        idx = d / "index.html"
        doc = idx.read_text(encoding="utf-8")
        oe = H.escape(old, quote=False)
        doc = doc.replace(f"<title>{old}", f"<title>{en_new}").replace(f"<title>{oe}", f"<title>{H.escape(en_new, quote=False)}")
        doc, k = re.subn(r"(<h1[^>]*>)(\s*)" + re.escape(oe if oe in doc else old), lambda mm: mm.group(1) + mm.group(2) + H.escape(en_new, quote=False), doc, count=1)
        if not k:
            raise SystemExit(f"❌ {slug}: h1 with old title not found")
        idx.write_text(doc, encoding="utf-8")
        if not keep:
            for p in _langs(d):
                if p.stem not in ("ja",):
                    j = _load(p); j.pop("title", None); _save(p, j)
    if ja_new:
        p = d / "i18n" / "ja.json"
        j = _load(p); j["title"] = ja_new; _save(p, j)
    LOG.append((slug, "title", en_new, ja_new))


def meta(slug, **kw):
    d = _dir(slug)
    m = d / "meta.json"
    mj = _load(m)
    mj.update(kw)
    _save(m, mj)
    LOG.append((slug, "meta", kw, None))
