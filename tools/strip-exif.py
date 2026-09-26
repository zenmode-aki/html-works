#!/usr/bin/env python3
"""
📍 写真から「撮った場所（GPS）」などの情報を消す（2026-09-26）

  python3 tools/strip-exif.py            全部の写真（記事に埋め込んだものも）
  python3 tools/strip-exif.py --check    消し忘れがないか見るだけ（見つかったら終了コード1）

スマホの写真には、撮った場所の緯度・経度、日時、機種が入っていることがある。
公開する写真に残っていると、家や職場の場所がわかってしまう
（2026-09-26 に、職場の近く・セブの部屋・クラークの寮の位置が入った写真が13枚見つかった）。

写真そのものは描き直さない（画質は1ミリも変わらない）。JPEG の Exif / XMP の部分と、
PNG の eXIf の部分だけを取り除く。色の情報（ICC）は残す。
"""
import base64
import pathlib
import re
import struct
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
B64 = re.compile(r'(data:image/(?:jpeg|jpg|png);base64,)([A-Za-z0-9+/=]+)')


def strip_jpeg(b: bytes) -> bytes:
    if b[:2] != b"\xff\xd8":
        return b
    out, i = [b[:2]], 2
    while i + 4 <= len(b) and b[i] == 0xFF:
        marker = b[i + 1]
        if marker == 0xDA:                      # ここから先は画像そのもの
            break
        size = struct.unpack(">H", b[i + 2:i + 4])[0]
        seg = b[i:i + 2 + size]
        body = seg[4:]
        drop = marker == 0xE1 and (body.startswith(b"Exif\x00") or body.startswith(b"http://ns.adobe.com/xap"))
        if not drop:
            out.append(seg)
        i += 2 + size
    out.append(b[i:])
    return b"".join(out)


def strip_png(b: bytes) -> bytes:
    if b[:8] != b"\x89PNG\r\n\x1a\n":
        return b
    out, i = [b[:8]], 8
    while i + 8 <= len(b):
        n = struct.unpack(">I", b[i:i + 4])[0]
        kind = b[i + 4:i + 8]
        chunk = b[i:i + 12 + n]
        if kind not in (b"eXIf",):
            out.append(chunk)
        i += 12 + n
    return b"".join(out)


def strip(b: bytes) -> bytes:
    return strip_png(strip_jpeg(b))


def main():
    check = "--check" in sys.argv
    files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split("\n")
    changed = []
    for f in files:
        p = ROOT / f
        if not f or not p.exists():
            continue
        if re.search(r"\.(jpe?g|png)$", f, re.I):
            b = p.read_bytes(); s = strip(b)
            if s != b:
                changed.append(f)
                if not check:
                    p.write_bytes(s)
        elif f.endswith(".html"):
            t = p.read_text(encoding="utf-8")
            hits = []
            def fix(m):
                try:
                    b = base64.b64decode(m.group(2))
                except Exception:
                    return m.group(0)
                s = strip(b)
                if s == b:
                    return m.group(0)
                hits.append(1)
                return m.group(1) + base64.b64encode(s).decode()
            t2 = B64.sub(fix, t)
            if hits:
                changed.append(f"{f}（埋め込み {len(hits)}枚）")
                if not check:
                    p.write_text(t2, encoding="utf-8")
    if check:
        if changed:
            print("❌ 撮った場所などの情報が残っている写真があります → python3 tools/strip-exif.py")
            for c in changed[:20]:
                print("  ", c)
            sys.exit(1)
        print("✅ 写真に撮った場所などの情報は残っていません")
    else:
        print(f"✅ 写真の情報を消したファイル: {len(changed)}")


if __name__ == "__main__":
    main()
