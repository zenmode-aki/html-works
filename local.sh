#!/bin/bash
# 🖥 ローカル版を開く
#   使い方:  ./local.sh
#
# 本番（GitHub Pages）とは別に、自分のパソコンの中だけで見るためのもの。
# サーバを立ててからブラウザを開く。file:// で開くより崩れにくい。
set -e
cd "$(dirname "$0")"

PORT=8811
URL="http://localhost:$PORT/staging/index.html"

if [ "$1" = "stop" ]; then
  if [ -f /tmp/html-works-local.pid ] && kill "$(cat /tmp/html-works-local.pid)" 2>/dev/null; then
    rm -f /tmp/html-works-local.pid
    echo "🛑 止めました"
  else
    echo "ℹ️  動いていないみたいです"
  fi
  exit 0
fi

# もう立っているなら立て直さない
if curl -s -o /dev/null --max-time 1 "http://localhost:$PORT/"; then
  echo "✅ もう動いています"
else
  echo "🚀 サーバを立てます（止めるときは Ctrl+C、または ./local.sh stop）"
  python3 -m http.server "$PORT" >/tmp/html-works-local.log 2>&1 &
  echo $! > /tmp/html-works-local.pid
  sleep 1
fi

cat <<MSG

  🐧 本番前（staging）の入口
     $URL

  ほかの入口
     本番前の一覧      http://localhost:$PORT/staging/index.html
     トップの試作      http://localhost:$PORT/staging/prototype-home.html
     いまの本番トップ  http://localhost:$PORT/index.html

  止めるとき
     ./local.sh stop

MSG

open "$URL"
