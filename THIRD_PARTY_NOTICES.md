# 🙏 使わせてもらっている部品

このブログは「外の部品を足さない」のが決まりですが、次のものだけ、ライセンスを守って入れています。

## BudouX（日本語の見出しを文節で折り返す）

- 場所：`tools/ja_phrase_model.json`（日本語モデル）、`tools/ja_phrase.js`（計算のしかた）→ `assets/ja-phrase.js`
- © 2021 Google LLC
- Apache License, Version 2.0 — https://www.apache.org/licenses/LICENSE-2.0
- もと：https://github.com/google/budoux （npm の `budoux` 0.9.3 の `src/data/models/ja.ts` と `src/parser.ts` を、そのまま写して動くようにしたもの。改変：JavaScript（ES5）に書き直し、見出しに `<wbr>` を入れる部分を足した）

## Fluent Emoji（表紙の吹き出しの中の立体の絵文字）

- 場所：表紙の画像（`draft/*/images/cover.jpg`・`works/*/images/cover.jpg` のうち 2026-10-07 以降に `tools/cover/make-cover.py` で作ったもの）。絵文字の画像そのものは git に入れていない（`tools/cover/emo/` は作るときだけ取ってくる）
- © Microsoft Corporation
- MIT License — https://github.com/microsoft/fluentui-emoji/blob/main/LICENSE
