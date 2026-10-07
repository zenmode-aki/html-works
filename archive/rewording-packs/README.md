# 🗄 しまってある言い換えパック（2026-10-07）

本人：「技術の用語の言い換えは一旦いらない。IT用語と社会人のビジネス用語の2つだけでいい。医療用語もいらない。GCPも消して、今後使うかもしれないから、いい感じのところに保存しておいて」

- 画面に出す言い換えは **💻 it** と **💼 biz** の2つだけにした（`tools/i18n_runtime.js` の `PACK_ORDER`、`tools/build-site.py` のパックの一覧）
- ここにしまったもの：`gcp`（Google Cloud）・`net`（ネットワーク）・`srv`（サーバー）・`sec`（セキュリティ）・`fin`（金融）・`med`（医療）・`nur`（看護）
- ファイル名は `<パック>/<記事のslug>.<言語>.json`（もとは `works/<slug>/<パック>.<言語>.json`）。中身は1文字も変えていない
- `gcp/gcp-mark.png` は、もと `assets/gcp-mark.png`（Google Cloud のマーク）

## 戻すとき
1. `git mv archive/rewording-packs/<パック>/<slug>.<言語>.json works/<slug>/<パック>.<言語>.json`（全部なら for 文で）
2. `tools/build-site.py` のパックの一覧と、`tools/i18n_runtime.js` の `PACK_ORDER` にパック名を足す（gcp はマークも `assets/` に戻す）
3. `python3 tools/build-site.py` → `python3 tools/i18n.py` → `python3 tools/check.py --site`
