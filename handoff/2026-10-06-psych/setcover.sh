#!/bin/zsh
# usage: setcover.sh slug (uses P/cv/<slug>.png)
set -e
P=/private/tmp/claude-501/-Users-ezakimasaaki-Desktop-html-works/4b2d5142-57b6-4f0c-bf5e-1c46457b715b/scratchpad/psych
cd /Users/ezakimasaaki/Desktop/html-works
s=$1
mkdir -p draft/$s/images
sips -s format jpeg -s formatOptions 92 $P/cv/$s.png --out draft/$s/images/cover.jpg >/dev/null
python3 tools/embed.py --draft $s >/dev/null
cp draft/$s/images/cover.jpg assets/thumbs-src/$s.jpg
python3 tools/thumbs.py $s >/dev/null
grep -q 'IMAGE:cover.jpg' draft/$s/index.html && echo "❌ $s still IMAGE" || echo "✓ $s"
mkdir -p $P/cv/done; mv $P/cv/$s.png $P/cv/done/; rm -f $P/cv/$s.sm.jpg
