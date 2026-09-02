#!/bin/bash
# 🟢 本番前 → 本番 に出す
#   使い方:  ./promote.sh nagoya-station-bookshop
#
#   staging/works/<slug>/  →  works/<slug>/
#
# 記事は ../../index.html で自分のトップに戻る作りなので、
# 階層が同じ本番へは「移動するだけ」で中身を直す必要がありません。
# ここでやるのはバッジと noindex とトップの作り直しだけです。
#
# push はしません。中身を見てから自分で push してください。
set -e
cd "$(dirname "$0")"

SLUG="$1"
if [ -z "$SLUG" ]; then
  echo "使い方: ./promote.sh <slug>"
  echo ""
  echo "いま本番前にあるもの:"
  ls staging/works 2>/dev/null | sed 's/^/  🟡 /' || echo "  （ありません）"
  exit 1
fi

SRC="staging/works/$SLUG"
DST="works/$SLUG"

[ -d "$SRC" ] || { echo "❌ $SRC がありません"; exit 1; }
[ -e "$DST" ] && { echo "❌ $DST がもうあります。先に確認してください"; exit 1; }

echo "🟡 → 🟢  $SLUG を本番に出します"

# 1. 移動（git に履歴を残す）
git mv "$SRC" "$DST" 2>/dev/null || mv "$SRC" "$DST"
echo "  ✅ $SRC → $DST"

# 2. バッジを PUBLIC に／3. noindex を外す
python3 - "$DST" <<'PY'
import pathlib, re, sys
p = pathlib.Path(sys.argv[1]) / "index.html"
t = p.read_text(encoding="utf-8")
before = t

# ⚠️ stage-staging / stage-public を狙う。
#    素の class="stage" は本文のタイムライン（🧸 Kindergarten など）で使っているので触らない
t = t.replace('class="stage stage-staging">STAGING', 'class="stage stage-public">PUBLIC')
t = re.sub(r'\s*<meta name="robots" content="noindex[^"]*"\s*/?>\n?', '\n', t, count=1)

if t == before:
    print("  ⚠️  バッジと noindex が見つかりませんでした。手で確認してください")
else:
    p.write_text(t, encoding="utf-8")
    print("  ✅ STAGING → PUBLIC / noindex を外した")
PY

# 4. トップを作り直す（本番と本番前の両方）
python3 tools/build-site.py | sed 's/^/  /'

# 5. 検査
echo ""
if python3 tools/check.py "$SLUG" > /tmp/promote-check.txt 2>&1; then
  echo "✅ 検査を通りました"
else
  echo "❌ 検査に落ちました。中身を直してください："
  sed 's/^/  /' /tmp/promote-check.txt
  exit 1
fi

cat <<MSG

  🟢 本番に出しました: works/$SLUG

  この後：
    git status --short          ← 中身を目で見る
    git add -A
    git commit -m "publish $SLUG"
    git push origin main

  取り消したいとき：
    ./demote.sh $SLUG

MSG
