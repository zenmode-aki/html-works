#!/usr/bin/env python3
"""
🐧 画像を縮小して index.html に base64 で埋め込む

  python3 tools/embed.py pawapuro

HTML側にこう書いておくだけ：
  <img src="IMAGE:switch.jpg" alt="...">
        ↑ images/switch.jpg を 幅1200px・quality 72 に縮小して base64 で埋め込みます

チャットAIに数百KBのbase64を書かせると必ず途中で壊れるので、
埋め込みはこのスクリプトの仕事にしてあります。
何度実行しても結果は同じです（埋め込み済みのものは飛ばします）。
"""
import base64, mimetypes, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIDTH, QUALITY = 1200, 72


def shrink(src: pathlib.Path, out_dir: pathlib.Path) -> pathlib.Path:
    """幅1200px以内・JPEG q72 に縮小する（macOSの sips を使用）。"""
    dst = out_dir / (src.stem + ".jpg")
    if src.suffix.lower() == ".png":
        # 小さいPNGはsipsで再保存すると、数KBのロゴが数十〜数百KBへ
        # 逆に膨らむことがある。幅上限内なら元データをそのまま使う。
        dst = out_dir / (src.stem + ".png")
        shutil.copy(src, dst)
        info = subprocess.run(["sips", "-g", "pixelWidth", str(dst)],
                              check=True, capture_output=True, text=True).stdout
        match = re.search(r"pixelWidth:\s*(\d+)", info)
        if match and int(match.group(1)) > WIDTH:
            subprocess.run(["sips", "-Z", str(WIDTH), str(dst)],
                           check=True, capture_output=True)
        return dst
    shutil.copy(src, dst)
    subprocess.run(["sips", "-Z", str(WIDTH),
                    "--setProperty", "format", "jpeg",
                    "--setProperty", "formatOptions", str(QUALITY), str(dst)],
                   check=True, capture_output=True)
    return dst


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    work = ROOT / "works" / sys.argv[1]
    idx = work / "index.html"
    if not idx.exists():
        print(f"❌ {idx} がありません")
        return 1

    doc = idx.read_text(encoding="utf-8")
    placeholders = re.findall(r'src="IMAGE:([^"]+)"', doc)
    if not placeholders:
        print("ℹ️  IMAGE: の指定がありません（もう埋め込み済みかもしれません）")
        return 0

    tmp = pathlib.Path(tempfile.mkdtemp())
    total_before = 0
    for fname in dict.fromkeys(placeholders):
        src = work / "images" / fname
        if not src.exists():
            print(f"❌ images/{fname} がありません")
            return 1
        small = shrink(src, tmp)
        raw = small.read_bytes()
        mime = mimetypes.guess_type(small.name)[0] or "image/jpeg"
        uri = f"data:{mime};base64,{base64.b64encode(raw).decode()}"
        doc = doc.replace(f'src="IMAGE:{fname}"', f'src="{uri}"')
        total_before += src.stat().st_size
        print(f"  📸 {fname}: {src.stat().st_size/1024:.0f}KB "
              f"→ 縮小 {len(raw)/1024:.0f}KB → 埋め込み {len(uri)/1024:.0f}KB")

    idx.write_text(doc, encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    size = len(doc.encode())
    print(f"\n✅ {idx.relative_to(ROOT)} = {size/1024:.0f}KB", end="")
    print("  ⚠️ 400KBを超えています。画像を減らしてください。" if size > 400 * 1024 else " / 400KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
