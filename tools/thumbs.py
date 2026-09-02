#!/usr/bin/env python3
"""
🖼 一覧サムネイルを 240px の正方形に整える

  python3 tools/thumbs.py            足りないものだけ作る
  python3 tools/thumbs.py pawapuro   1枚だけ作り直す
  python3 tools/thumbs.py --all      全部작り直す

  assets/thumbs-src/<slug>.jpg   元画像（生成物・大きい）
        ↓  240x240 · quality 72
  assets/thumbs/<slug>.jpg       トップページが参照するもの

一覧の左は絵文字ではなく **画像** にすると決めています（2026-09-02）。
絵文字だと全部同じ顔に見えてしまって、記事の中身が伝わらないため。

⚠️ base64 で index.html に埋め込むのはやめました。
   トップページを 2つのAI（Claude と ChatGPT/Codex）が触るので、
   244KB の base64 を含む HTML だと衝突が直せなくなるためです。
   記事（works/*/index.html）の中の画像は、いままで通り base64 のままです。

macOS の sips を使うのでローカル専用。GitHub Actions では走らせません。
"""
import pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "assets" / "thumbs-src"
OUT_DIR = ROOT / "assets" / "thumbs"
SIZE, QUALITY = 240, 72


def square(src: pathlib.Path, dst: pathlib.Path) -> int:
    """SIZE×SIZE の JPEG にする。

    ⚠️ -c だけを使ってはいけない。-c は「縮小」ではなく「切り抜き」なので、
       1024px の画像にいきなり -c 240 240 をかけると、真ん中の240pxだけを
       切り取ってしまい、被写体の顔が消える。
       まず短いほうの辺を SIZE まで縮めてから、-c で正方形に整える。
    """
    tmp = pathlib.Path(tempfile.mkdtemp()) / "t.jpg"
    shutil.copy(src, tmp)

    info = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(tmp)],
                          check=True, capture_output=True, text=True).stdout
    w = int(re.search(r"pixelWidth:\s*(\d+)", info).group(1))
    h = int(re.search(r"pixelHeight:\s*(\d+)", info).group(1))
    scale = SIZE / min(w, h)
    subprocess.run(["sips", "-z", str(max(SIZE, round(h * scale))),
                                 str(max(SIZE, round(w * scale))), str(tmp)],
                   check=True, capture_output=True)
    subprocess.run(["sips", "-c", str(SIZE), str(SIZE),
                    "--setProperty", "format", "jpeg",
                    "--setProperty", "formatOptions", str(QUALITY), str(tmp)],
                   check=True, capture_output=True)

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(tmp, dst)
    shutil.rmtree(tmp.parent, ignore_errors=True)
    return dst.stat().st_size


def main():
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--all" in sys.argv

    if not SRC_DIR.exists():
        print(f"❌ {SRC_DIR.relative_to(ROOT)}/ がありません")
        return 1

    srcs = sorted(p for p in SRC_DIR.iterdir()
                  if p.suffix.lower() in (".jpg", ".jpeg", ".png"))
    if only:
        srcs = [p for p in srcs if p.stem in only]
        if not srcs:
            print(f"❌ 元画像がありません: {only}")
            return 1

    made = skipped = 0
    for src in srcs:
        dst = OUT_DIR / f"{src.stem}.jpg"
        if dst.exists() and not force and dst.stat().st_mtime >= src.stat().st_mtime:
            skipped += 1
            continue
        n = square(src, dst)
        made += 1
        print(f"  🖼 {src.stem:<30} {src.stat().st_size/1024:>5.0f}KB → {n/1024:>4.0f}KB")

    print(f"\n✅ {made}枚つくりました" + (f"（{skipped}枚は最新なので飛ばしました）" if skipped else ""))
    print("   トップに反映するには python3 tools/build-site.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
