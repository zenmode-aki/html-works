#!/usr/bin/env python3
"""
🐧 本番の pengesso.html を、本番前の試作から作り直す

  python3 tools/publish-pengesso.py

    staging/prototype-home.html  →  pengesso.html

なぜ道具にしたか：
  2026-09-03 に、試作のほうだけ文章を短く直して、本番のコピーを直し忘れた。
  同じ内容の2ファイルを手で揃えるのは必ず失敗する。**片方から作る**ことにした。

やっていること（この3つだけ）：
  1. staging/ の中から見るので ../assets/ になっている参照を assets/ に直す
  2. 記事へのリンクを ../works/ から works/ に直す
  3. 🟡 STAGING のバーを 🟢 PUBLIC に変える

記事の一覧そのものは build-site.py が meta.json から差し込むので、ここでは触らない。
必ず publish-pengesso.py → build-site.py の順で走らせること。
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "staging" / "prototype-home.html"
DST = ROOT / "pengesso.html"

STAGING_BAR = """<div class="stage-bar">
  <span class="stage-dot" aria-hidden="true"></span>STAGING
  <span class="why">見た目の試作。ここで作って、よければ pengesso.html へ</span>
</div>"""

PUBLIC_BAR = """<div class="stage-bar stage-bar-public">
  <span class="stage-dot" aria-hidden="true"></span>PUBLIC
  <span class="why">Unfinished on purpose. That is the rule. 🐧</span>
</div>"""


def main():
    if not SRC.exists():
        sys.exit(f"❌ {SRC} がありません")
    t = SRC.read_text(encoding="utf-8")

    # 1. 画像・2. リンク（staging/ の1つ下から、ルートから見た形へ）
    t = t.replace('src="../assets/', 'src="assets/')
    t = t.replace("'../assets/", "'assets/")
    t = t.replace("'../works/", "'works/")

    # 3. バッジ
    if STAGING_BAR not in t:
        sys.exit("❌ STAGING のバーが見つかりません。試作のほうを直してから、もう一度実行してください")
    t = t.replace(STAGING_BAR, PUBLIC_BAR, 1)
    t = t.replace("  .stage-bar .why {",
                  "  .stage-bar-public { background: #23c98a; color: #04331d; }\n  .stage-bar .why {", 1)

    t = t.replace("<title>15 Seconds — Pengesso (local prototype)</title>",
                  "<title>Pengesso — the penguin who runs this blog</title>")

    left = [s for s in ("../assets/", "../works/") if s in t]
    if left:
        sys.exit(f"❌ 直しきれていない参照が残っています: {left}")

    DST.write_text(t, encoding="utf-8")
    print(f"✅ pengesso.html を作り直しました（{len(t)/1024:.0f}KB）")
    print("   このあと必ず: python3 tools/build-site.py")


if __name__ == "__main__":
    main()
