#!/bin/zsh
# usage: ds.sh sheetname slug=file ...
P=/private/tmp/claude-501/-Users-ezakimasaaki-Desktop-html-works/4b2d5142-57b6-4f0c-bf5e-1c46457b715b/scratchpad/psych
n=$1; shift
$P/dl.sh "$@" >/dev/null
cd $P/cv; L=(); for a in "$@"; do L+=(${a%%=*}.png); done
python3 ../sheet.py ../sheet_$n.jpg $L
