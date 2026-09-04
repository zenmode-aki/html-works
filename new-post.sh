#!/bin/bash
# ⚡ 新しい15秒記事を1本つくる
#   使い方:  ./new-post.sh cebu-food
set -e
cd "$(dirname "$0")"

if [ -z "$1" ]; then
  echo "使い方: ./new-post.sh <英数字の短い名前>   例) ./new-post.sh nagoya-dome"
  exit 1
fi

SLUG="$1"
DIR="works/$SLUG"

if [ -e "$DIR" ]; then
  echo "⚠️  $DIR はもうあります。名前を変えてください。"
  exit 1
fi

mkdir -p "$DIR/images"
sed "s/__SLUG__/$SLUG/g; s/__DATE__/$(date +%Y-%m-%d)/g" _template/index.html > "$DIR/index.html"
sed "s/__SLUG__/$SLUG/g; s/__DATE__/$(date +%Y-%m-%d)/g" _template/source.md  > "$DIR/source.md"

cat <<MSG
✅ できました: $DIR

  1) 日本語の音声入力を $DIR/source.md に貼る（S1. S2. と番号を振る）
  2) PROMPT.md をAIに貼って、素材を渡す → $DIR/index.html を書いてもらう
     ⚡ 本文は 35〜55 words。カードは3〜5枚。1枚に1〜2文
     🏷️ すべてのカードに英単語2〜3語の card-label を付ける（絵文字だけは禁止）
     🎭 トーンは反転させる（真面目→ポップ / どうでもいい→荘厳）
  3) 写真を $DIR/images/ に入れて、HTMLには src="IMAGE:ファイル名" と書いておく
     python3 tools/embed.py $SLUG        ← 縮小して埋め込む
  4) python3 tools/check.py $SLUG        ← 「追加した文：0」を確認
  5) python3 tools/thumbs.py             ← 一覧に出すサムネを作る（macOSのみ）
  6) python3 tools/build-site.py         ← トップの一覧に差し込む（手で足さない）
  7) ひとつ前の記事の末尾の Next ⚡ を、この記事に向ける
  8) git add -A && git commit -m "add $SLUG" && git push

  ⚡ 出す場所は1つだけです。push した時点で
     https://zenmode-aki.github.io/html-works/ に出ます。
     気になったところは、出したあとに直してください。

  ※ 毎朝6時にSlackから自動生成される下書きは drafts/ に出ます（gitには乗りません）
MSG
