#!/usr/bin/env python3
"""
🗺 本物の地図データから、正確でクリックできる SVG を作る。

  入力  Natural Earth（パブリックドメイン。権利表記もいらない）
          ne50.json        … 国の形
          ne10_admin1.json … 日本の47都道府県の形
  出力  _maps.js         … アジアと日本、2枚ぶんの SVG パスと街の座標

なぜ画像生成をやめたか：
  絵で地図を作ると「日本と韓国の位置がぐちゃぐちゃ」になるし、
  絵の上のどこを押したかを正確に判定できない。
  本物の座標から作れば、形も位置も正しいし、県ごとに押せる。
  色鉛筆っぽさは、SVGフィルタ（紙のざらつき＋線のゆらぎ）で後からかける。
"""
import json, math, pathlib

import os
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
# Natural Earth の元データの置き場。50MB近いのでリポジトリには入れない。
#   NE_DIR=~/Downloads python3 tools/make-maps.py  のように渡せる
SRC = pathlib.Path(os.environ.get("NE_DIR", "/private/tmp/claude-501"
      "/-Users-akiezaki-Developer-html-works"
      "/b432b9f1-3762-44df-9d01-5981f2665aad/scratchpad")).expanduser()

# ── あきくんが実際に行った場所（本人が挙げたもの）──────────────
# 札を出す向き（dx, dy, 揃え）。これが無いと名古屋・岐阜・三重・大阪の名前が団子になる
NUDGE = {
    "tokyo":  (18, 6, "start"), "nagoya": (16, 30, "start"), "gifu": (10, -20, "start"),
    "mie":    (16, 70, "start"), "osaka":  (-20, -16, "end"),
    "seoul":  (-18, 4, "end"),  "bangkok": (-18, 4, "end"),
    "kanchana": (-18, -18, "end"), "baguio": (18, -6, "start"),
    "clark":  (18, 14, "start"), "cebu": (18, 8, "start"), "kl": (-18, 16, "end"),
}
# 端に近い国は、札を内側に向ける。外に向けると地図の枠で切れる
MARK_NUDGE = {"jp": (-18, 30, "end"), "kr": (-18, 2, "end"), "th": (18, 4, "start"),
              "ph": (18, 6, "start"), "my": (18, 14, "start")}

CITIES = [
    # key,        表示名,           日本語,        lat,      lon,     国, 記事のplace
    ("tokyo",     "Tokyo",         "東京",      35.6895, 139.6917, "jp", "tokyo"),
    ("osaka",     "Osaka",         "大阪",      34.6937, 135.5023, "jp", "osaka"),
    ("gifu",      "Gifu",          "岐阜",      35.4233, 136.7606, "jp", "gifu"),
    ("mie",       "Mie",           "三重",      34.7185, 136.5056, "jp", "mie"),
    ("nagoya",    "Nagoya",        "名古屋",    35.1815, 136.9066, "jp", "nagoya"),
    ("seoul",     "Seoul",         "ソウル",    37.5665, 126.9780, "kr", "seoul"),
    ("bangkok",   "Bangkok",       "バンコク",  13.7563, 100.5018, "th", "bangkok"),
    ("kanchana",  "Kanchanaburi",  "カンチャナブリ", 14.0227, 99.5328, "th", "thailand"),
    ("baguio",    "Baguio",        "バギオ",    16.4023, 120.5960, "ph", "baguio"),
    ("clark",     "Clark",         "クラーク",  15.1450, 120.5887, "ph", "clark"),
    ("cebu",      "Cebu",          "セブ",      10.3157, 123.8854, "ph", "cebu"),
    ("kl",        "Kuala Lumpur",  "クアラルンプール", 3.1390, 101.6869, "my", "kl"),
]

FOCUS_COUNTRIES = {"Japan": "jp", "South Korea": "kr", "Thailand": "th",
                   "Philippines": "ph", "Malaysia": "my"}

# アジアの地図では、街を全部出すと名前が重なって読めない
# （東京・名古屋・三重・大阪が団子になる）。だから国に1つだけ札を立てて、
# 街はその国を押したあとに出す。日本を押すと都道府県の地図にひらく。
COUNTRY_MARKS = [
    ("jp", "Japan",       "日本",         36.3, 139.4),
    ("kr", "South Korea", "韓国",         37.0, 127.6),
    ("th", "Thailand",    "タイ",         15.4, 101.0),
    ("ph", "Philippines", "フィリピン",   12.6, 122.6),
    ("my", "Malaysia",    "マレーシア",    3.9, 102.3),
]
# 愛知＝名古屋。都道府県は本人が挙げた5つを光らせる
FOCUS_PREF = {"Tokyo": "tokyo", "Ōsaka": "osaka", "Gifu": "gifu",
              "Mie": "mie", "Aichi": "nagoya"}

ASIA = dict(lon=(93.0, 148.0), lat=(-4.0, 47.5))
# 大きい地図＝行った5県が読める範囲。北海道と沖縄はここには入らない
JAPAN = dict(lon=(129.0, 142.6), lat=(30.6, 41.9))
# 左上に出す小さい日本ぜんぶ。北海道も沖縄もここに出る。
# 「いま中部あたりを見てますよ」を四角で示すためのもの
JPALL = dict(lon=(125.5, 147.0), lat=(23.5, 46.2))
FAR = ("Hokkaidō", "Okinawa")   # ミニ地図で少しだけ色を変える（まだ記事が無い場所）


def merc(lon, lat):
    """メルカトル。狭い範囲なら形がいちばん見慣れた形になる。"""
    lat = max(min(lat, 84.0), -84.0)
    return lon, -math.degrees(math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)))


def frame(box, width=1000.0):
    x0, y1 = merc(box["lon"][0], box["lat"][0])
    x1, y0 = merc(box["lon"][1], box["lat"][1])
    sx = width / (x1 - x0)
    h = (y1 - y0) * sx

    def to(lon, lat):
        x, y = merc(lon, lat)
        return (x - x0) * sx, (y - y0) * sx
    return to, width, h


def simplify(pts, tol):
    """ダグラス・ポイカー。形を保ったまま点を減らす"""
    if len(pts) < 3:
        return pts
    ax, ay = pts[0]
    bx, by = pts[-1]
    dx, dy = bx - ax, by - ay
    n = math.hypot(dx, dy)
    far, di = 0.0, 0
    for i in range(1, len(pts) - 1):
        px, py = pts[i]
        d = (abs(dx * (ay - py) - (ax - px) * dy) / n) if n else math.hypot(px - ax, py - ay)
        if d > far:
            far, di = d, i
    if far <= tol:
        return [pts[0], pts[-1]]
    return simplify(pts[:di + 1], tol)[:-1] + simplify(pts[di:], tol)


def rings(geom):
    t = geom["type"]
    if t == "Polygon":
        return [geom["coordinates"][0]]
    if t == "MultiPolygon":
        return [p[0] for p in geom["coordinates"]]
    return []


def path_of(geom, to, box, tol, min_area):
    """見えている範囲のリングだけを SVG パスにする"""
    out = []
    lo0, lo1 = box["lon"]
    la0, la1 = box["lat"]
    for ring in rings(geom):
        lons = [c[0] for c in ring]
        lats = [c[1] for c in ring]
        if max(lons) < lo0 - 2 or min(lons) > lo1 + 2:
            continue
        if max(lats) < la0 - 2 or min(lats) > la1 + 2:
            continue
        pts = simplify([to(c[0], c[1]) for c in ring], tol)
        if len(pts) < 4:
            continue
        a = abs(sum(pts[i][0] * pts[i - 1][1] - pts[i - 1][0] * pts[i][1]
                    for i in range(len(pts)))) / 2
        if a < min_area:
            continue
        out.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z")
    return "".join(out)


def build_asia():
    ne = json.loads((SRC / "ne50.json").read_text())
    to, w, h = frame(ASIA)
    focus, other = [], []
    for f in ne["features"]:
        p = f["properties"]
        name = p.get("NAME_EN") or p.get("NAME") or ""
        d = path_of(f["geometry"], to, ASIA, tol=0.7, min_area=1.2)
        if not d:
            continue
        code = FOCUS_COUNTRIES.get(name)
        (focus if code else other).append({"d": d, "code": code or "", "name": name})
    return {"w": round(w), "h": round(h), "focus": focus, "other": other,
            "marks": [{"c": c, "n": n, "j": j, "x": round(to(lo, la)[0], 1),
                       "y": round(to(lo, la)[1], 1), "dx": MARK_NUDGE[c][0],
                       "dy": MARK_NUDGE[c][1], "a": MARK_NUDGE[c][2]}
                      for c, n, j, la, lo in COUNTRY_MARKS],
            "cities": [{"k": k, "n": n, "j": j, "x": round(to(lo, la)[0], 1),
                        "y": round(to(lo, la)[1], 1), "c": c, "p": pl,
                        "dx": NUDGE[k][0], "dy": NUDGE[k][1], "a": NUDGE[k][2]}
                       for k, n, j, la, lo, c, pl in CITIES]}


def build_japan():
    a1 = json.loads((SRC / "ne10_admin1.json").read_text())
    to, w, h = frame(JAPAN)
    focus, other = [], []
    for f in a1["features"]:
        p = f["properties"]
        if p.get("admin") != "Japan":
            continue
        name = p.get("name") or ""
        # 北海道と沖縄は行った5県から遠すぎて、入れると中央が豆粒になる。
        # かわりに左上のミニ地図（build_jpmini）に必ず出す。
        if name in FAR:
            continue
        d = path_of(f["geometry"], to, JAPAN, tol=0.45, min_area=0.8)
        if not d:
            continue
        row = {"d": d, "code": FOCUS_PREF.get(name, ""), "name": name,
               "ja": p.get("name_ja", "")}
        (focus if row["code"] else other).append(row)
    return {"w": round(w), "h": round(h), "focus": focus, "other": other,
            # 県庁所在地の黒点はもう出さない（あきくんの指示）。
            # 名前だけを県の上に置いて、押すのは県のかたち本体にする
            "cities": [{"k": k, "n": n, "j": j, "x": round(to(lo, la)[0], 1),
                        "y": round(to(lo, la)[1], 1), "c": c, "p": pl,
                        "dx": NUDGE[k][0], "dy": NUDGE[k][1], "a": NUDGE[k][2]}
                       for k, n, j, la, lo, c, pl in CITIES if c == "jp"]}


def build_jpmini():
    """左上に出す、日本ぜんぶの小さい地図。

    北海道と沖縄はここに必ず出す。大きい地図で「いまどこを見ているか」を
    四角で重ねるので、中部にズームしていることが一目で分かる。
    """
    a1 = json.loads((SRC / "ne10_admin1.json").read_text())
    to, w, h = frame(JPALL, width=300.0)
    land, far = [], []
    for f in a1["features"]:
        p = f["properties"]
        if p.get("admin") != "Japan":
            continue
        d = path_of(f["geometry"], to, JPALL, tol=0.9, min_area=1.2)
        if not d:
            continue
        (far if (p.get("name") or "") in FAR else land).append(d)
    x0, y1 = to(JAPAN["lon"][0], JAPAN["lat"][0])
    x1, y0 = to(JAPAN["lon"][1], JAPAN["lat"][1])
    return {"w": round(w), "h": round(h),
            "land": "".join(land), "far": "".join(far),
            "view": {"x": round(x0, 1), "y": round(y0, 1),
                     "w": round(x1 - x0, 1), "h": round(y1 - y0, 1)}}


maps = {"asia": build_asia(), "japan": build_japan(), "jpmini": build_jpmini()}
out = ("/* \U0001f5fa 本物の地図。Natural Earth（パブリックドメイン）から\n"
       "   tools/make-maps.py が焼き込んだもの。手で編集しない。\n"
       "   色鉛筆っぽさは SVG フィルタ（線のゆらぎ＋紙のざらつき）で後からかけている。 */\n"
       "var MAPS = " + json.dumps(maps, ensure_ascii=False, separators=(",", ":")) + ";")

# トップページの目印にはさまれた中身だけを書き替える
idx = ROOT / "index.html"
src = before = idx.read_text(encoding="utf-8")
import re as _re
src, n = _re.subn(r"(/\* ⬇️ MAPS:START[^\n]*\*/\n).*?(\n/\* ⬆️ MAPS:END ⬆️ \*/)",
                  lambda m: m.group(1) + out + m.group(2), src, flags=_re.S)
if not n:
    raise SystemExit("❌ index.html に MAPS:START / MAPS:END の目印がありません")
if src != before:
    idx.write_text(src, encoding="utf-8")

for k, m in maps.items():
    if k == "jpmini":
        print(f"✅ {k}: {m['w']}×{m['h']}  日本ぜんぶ（北海道・沖縄こみ）")
        continue
    print(f"✅ {k}: {m['w']}×{m['h']}  ぬる形 {len(m['focus'])}  背景 {len(m['other'])}  街 {len(m['cities'])}")
print(f"   index.html に差し込みました（地図データ {len(out)/1024:.0f}KB）")
