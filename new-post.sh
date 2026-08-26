#!/bin/bash
# 🐧 新しい記事を1本つくる
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
  3) 写真を $DIR/images/ に入れて、HTMLには src="IMAGE:ファイル名" と書いておく
     python3 tools/embed.py $SLUG        ← 縮小して埋め込む
  4) python3 tools/check.py $SLUG        ← 「追加した文：0」を確認
  5) index.html（トップ）の一覧に1行足す
  6) git add -A && git commit -m "add $SLUG" && git push
MSG
