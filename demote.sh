#!/bin/bash
# 🟡 本番 → 本番前 に引っ込める（promote.sh の逆）
#   使い方:  ./demote.sh nagoya-station-bookshop
#
#   works/<slug>/  →  staging/works/<slug>/
#
# 出したあとで「やっぱり下げたい」となったとき用。
# 記事そのものは消しません。本番前に戻すだけです。
set -e
cd "$(dirname "$0")"

SLUG="$1"
if [ -z "$SLUG" ]; then
  echo "使い方: ./demote.sh <slug>"
  echo ""
  echo "いま本番にあるもの:"
  ls works 2>/dev/null | sed 's/^/  🟢 /' || echo "  （ありません）"
  exit 1
fi

SRC="works/$SLUG"
DST="staging/works/$SLUG"

[ -d "$SRC" ] || { echo "❌ $SRC がありません"; exit 1; }
[ -e "$DST" ] && { echo "❌ $DST がもうあります。先に確認してください"; exit 1; }

echo "🟢 → 🟡  $SLUG を本番前に下げます"

mkdir -p staging/works
git mv "$SRC" "$DST" 2>/dev/null || mv "$SRC" "$DST"
echo "  ✅ $SRC → $DST"

python3 - "$DST" <<'PY'
import pathlib, sys
p = pathlib.Path(sys.argv[1]) / "index.html"
t = p.read_text(encoding="utf-8")

t = t.replace('class="stage stage-public">PUBLIC', 'class="stage stage-staging">STAGING')

# noindex を入れ直す（無いときだけ）
if 'name="robots"' not in t:
    t = t.replace('<meta name="viewport"',
                  '<meta name="robots" content="noindex, nofollow" />\n<meta name="viewport"', 1)

p.write_text(t, encoding="utf-8")
print("  ✅ PUBLIC → STAGING / noindex を入れ直した")
PY

python3 tools/build-site.py | sed 's/^/  /'

echo ""
if python3 tools/check.py --staging "$SLUG" > /tmp/demote-check.txt 2>&1; then
  echo "✅ 検査を通りました"
else
  echo "❌ 検査に落ちました："
  sed 's/^/  /' /tmp/demote-check.txt
  exit 1
fi

cat <<MSG

  🟡 本番前に戻しました: staging/works/$SLUG

  この後：
    git add -A && git commit -m "unpublish $SLUG" && git push origin main

MSG
