#!/bin/zsh
# usage: dl.sh slug=url_suffix ...  (url suffix after the cloudfront user path)
P=/private/tmp/claude-501/-Users-ezakimasaaki-Desktop-html-works/4b2d5142-57b6-4f0c-bf5e-1c46457b715b/scratchpad/psych
U=https://d8j0ntlcm91z4.cloudfront.net/user_3HlRdlUC3T5anmt1JdUaDB8ZK10
for a in "$@"; do s=${a%%=*}; f=${a#*=}; curl -sL "$U/$f" -o $P/cv/$s.png; done
cd $P/cv && ls *.png | head -20
