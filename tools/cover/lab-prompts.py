# 試作の棚（lab/）の表紙を Higgsfield で作り直すための指示文を作る（2026-10-09）
# 本人：「ペンギンがどうしても大きすぎて幼稚すぎて嫌」
# → 主役は記事の「もの」。ペンゲッソ（紺・青い帽子・サングラスのぬいぐるみ）は小さく、端に。大人っぽい写真の静物。
#
# usage: python3 tools/cover/lab-prompts.py            → tools/cover/lab-prompts.json を作り直す
#        python3 tools/cover/lab-prompts.py <slug...>  → その記事の指示文を表示する
#
# 生成のめやす：model nano_banana_2（または nano_banana_pro）、aspect_ratio 4:3、
#   image_references に tools/cover/pengesso.png（本家ペンゲッソの見た目をそろえるため）
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "tools/cover/lab-prompts.json"

PENGESSO = ("a small navy-blue plush penguin with a blue cap and dark sunglasses "
            "(the same character as the reference image), taking up only about one tenth of the frame, "
            "placed off to one side")
STYLE = ("Calm, grown-up editorial still-life photograph. The object is the clear main subject. "
         "Muted, natural colors, soft window daylight, simple uncluttered background with plenty of empty space. "
         "Shot on a 50mm lens, shallow depth of field, real materials. "
         "Not cartoonish, not childish, no big eyes, no chubby mascot. "
         "No humans, no hands, no text, no lettering, no mesh, no grids, no clusters of small holes or dots.")


def old_prompt(slug):
    t = (ROOT / "lab" / slug / "source.md").read_text()
    m = re.search(r"## 表紙のプロンプト\s*\n+(.*?)(\n## |\Z)", t, re.S)
    if not m:
        return ""
    p = re.sub(r"^```\w*\n|```$", "", m.group(1).strip()).strip()
    return " ".join(p.split())


def convert(p):
    p = re.sub(r"\([^)]*\)", "", p)                                   # (no rings … on the belly)
    p = re.sub(r"Realistic 3D render.*$", "", p)                       # 古い仕上げの言葉は捨てる
    # 「An extremely cute, chubby round penguin …（体の説明）…,」→ 小さなペンゲッソ
    p = re.sub(r"^An? (extremely )?cute,? (chubby )?(round )?penguin", "PENG", p)
    p = re.sub(r"PENG(,? (with a gentle face|made|built|crafted|knitted|sculpted)[^,]*,)*", "PENG,", p)
    p = re.sub(r"\b(and )?a plain (white )?belly,?", "", p)
    p = re.sub(r"\b(extremely |very |super )?(cute|chubby|adorable|tiny|little|fluffy|round)\b,? ?", "", p)
    p = re.sub(r"\b(bright|vivid|neon|candy)[- ]", "soft ", p, flags=re.I)
    p = re.sub(r"\bwith (big |wide |sparkling )*(curious |happy |shiny )*eyes,?", "", p)
    p = re.sub(r"\s+,", ",", re.sub(r"\s{2,}", " ", p)).strip()
    p = p.replace("PENG,", PENGESSO + ",", 1).replace("PENG", PENGESSO, 1)
    if PENGESSO not in p:
        p = p + " Next to it, " + PENGESSO + "."
    return p[:1].upper() + p[1:] + " " + STYLE


def main(argv):
    slugs = argv or sorted(d.name for d in (ROOT / "lab").iterdir() if (d / "source.md").exists())
    rows = []
    for s in slugs:
        o = old_prompt(s)
        if not o:                                                      # 指示文がない記事は、題名から
            t = json.loads((ROOT / "lab" / s / "meta.json").read_text()).get("title", s)
            o = f"One simple everyday object that shows the idea \"{t}\". Soft pastel background."
        rows.append({"slug": s, "prompt": convert(o)})
    if argv:
        for r in rows:
            print(f"■ {r['slug']}\n{r['prompt']}\n")
    else:
        OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n")
        empty = [r["slug"] for r in rows if not r["prompt"]]
        print(f"🖼 {len(rows)}本 → {OUT.relative_to(ROOT)}（指示文なし：{len(empty)}本 {empty[:5]}）")


if __name__ == "__main__":
    main(sys.argv[1:])
