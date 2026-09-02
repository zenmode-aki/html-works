#!/usr/bin/env python3
"""
⚡ トップページの一覧サムネイルを、正方形に縮小して base64 で埋め込む

  python3 tools/thumbs.py            全部やる
  python3 tools/thumbs.py pawapuro   1本だけ

トップの index.html にこう書いておくだけ：
  <img src="THUMB:pawapuro" alt="...">
        ↑ assets/thumbs-src/pawapuro.png を 240x240・quality 72 に縮めて埋め込みます

一覧の左側は絵文字ではなく **画像** にする、と決めています（2026-09-02）。
絵文字だと全部同じ顔に見えてしまって、記事の中身が伝わらないため。

元画像（Higgsfieldの生成物・数MB）は assets/thumbs-src/ に置いておく。
ここは重いので、公開には使いません。使うのは埋め込まれた base64 のほうです。

何度実行しても結果は同じです（埋め込み済みのものは飛ばします）。
"""
import base64, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "assets" / "thumbs-src"
INDEX = ROOT / "index.html"
SIZE, QUALITY = 240, 72          # 66pxで表示するので、3倍でも足りる


def square(src: pathlib.Path, out_dir: pathlib.Path) -> bytes:
    """SIZE×SIZE の JPEG にする（macOSの sips を使用）。

    ⚠️ -c だけを使ってはいけない。-c は「縮小」ではなく「切り抜き」なので、
       1024pxの画像にいきなり -c 240 240 をかけると、真ん中の240pxだけを
       切り取ってしまい、被写体の顔が消える。
       まず -Z で短辺を SIZE まで縮めてから、-c で正方形に整える。
    """
    dst = out_dir / (src.stem + ".jpg")
    shutil.copy(src, dst)

    info = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(dst)],
                          check=True, capture_output=True, text=True).stdout
    w = int(re.search(r"pixelWidth:\s*(\d+)", info).group(1))
    h = int(re.search(r"pixelHeight:\s*(\d+)", info).group(1))

    # 短いほうの辺が SIZE になるまで縮める（切り抜いても隙間が出ないように）
    scale = SIZE / min(w, h)
    subprocess.run(["sips", "-z", str(max(SIZE, round(h * scale))),
                                 str(max(SIZE, round(w * scale))), str(dst)],
                   check=True, capture_output=True)
    # そのうえで中央を正方形に切る
    subprocess.run(["sips", "-c", str(SIZE), str(SIZE),
                    "--setProperty", "format", "jpeg",
                    "--setProperty", "formatOptions", str(QUALITY), str(dst)],
                   check=True, capture_output=True)
    return dst.read_bytes()


def main():
    only = sys.argv[1:]
    if not INDEX.exists():
        print(f"❌ {INDEX} がありません")
        return 1

    doc = INDEX.read_text(encoding="utf-8")
    slugs = re.findall(r'src="THUMB:([^"]+)"', doc)
    if only:
        slugs = [s for s in slugs if s in only]
    if not slugs:
        print("ℹ️  THUMB: の指定がありません（もう埋め込み済みかもしれません）")
        return 0

    tmp = pathlib.Path(tempfile.mkdtemp())
    embedded = 0
    for slug in dict.fromkeys(slugs):
        src = next((SRC_DIR / f"{slug}{e}" for e in (".png", ".jpg", ".jpeg")
                    if (SRC_DIR / f"{slug}{e}").exists()), None)
        if src is None:
            print(f"❌ assets/thumbs-src/{slug}.png がありません")
            shutil.rmtree(tmp, ignore_errors=True)
            return 1
        raw = square(src, tmp)
        uri = f"data:image/jpeg;base64,{base64.b64encode(raw).decode()}"
        doc = doc.replace(f'src="THUMB:{slug}"', f'src="{uri}"')
        embedded += len(uri)
        print(f"  🖼  {slug}: {src.stat().st_size/1024:.0f}KB "
              f"→ {SIZE}px {len(raw)/1024:.0f}KB → 埋め込み {len(uri)/1024:.0f}KB")

    INDEX.write_text(doc, encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    size = len(doc.encode())
    print(f"\n✅ index.html = {size/1024:.0f}KB（サムネ {len(dict.fromkeys(slugs))}枚）")
    if size > 900 * 1024:
        print("⚠️  トップが重くなってきました。古い記事のサムネを減らすことを考えてください。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
