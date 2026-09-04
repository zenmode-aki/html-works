#!/bin/bash
# 🖥 ローカルで見る
#   使い方:  ./local.sh
#
# 本番（GitHub Pages）に出す前に、自分のパソコンの中だけで見るためのもの。
# サーバを立ててからブラウザを開く。file:// で開くより崩れにくい。
set -e
cd "$(dirname "$0")"

PORT=8811
URL="http://localhost:$PORT/index.html"

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

  🐧 トップ（ここだけ）
     $URL

  自分用のページ
     🧭 Remember  http://localhost:$PORT/remember/index.html
     🎯 Goals     http://localhost:$PORT/goals/index.html
     🙋 Me        http://localhost:$PORT/me/index.html

  止めるとき
     ./local.sh stop

MSG

open "$URL"
