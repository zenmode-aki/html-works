# 🤖 次のAIへ（2026-10-09・クラウドのセッションからローカルへの引き継ぎ）

まず読む：`CLAUDE.md`（ブログ憲法がいちばん上）→ このファイル → `BACKLOG.md` の「🔥 2026-10-08」

## 🟢 今の状態
- 全部 commit・push 済み（main と `claude/malaysia-trip-blog-ozk5kr` は同じ）。途中のままのファイルはない
- `python3 tools/check.py --site` ✅ / `python3 tools/check.py --lab` ✅ / `python3 tools/mobile-check.py` ✅（12本）/ `python3 tools/strip-exif.py --check` ✅
- 予約（Routine）は全部消化・削除ずみ。動いているエージェントもいない

## ✅ このセッションでやったこと（古い順）
1. 下書き seq 522〜590 の仕上げ → 下書きを日・英・韓で本番へ（言い換えパックなし）
2. 言い換えパックを 💻 it と 💼 biz だけに。gcp/net/srv/sec/fin/med/nur は `archive/rewording-packs/` へ（README つき）
3. 新しい表紙の道具 `tools/cover/make-cover.py`（ペンゲッソ＋考えごとの吹き出し＋Fluent 3D 絵文字）。表紙がなかった152本に付けた → **本人「雑」**。Higgsfield で作り直したい
4. スマホの見やすさ：勉強バーを390pxで1行・押しにくい小さなボタンを40px・トップの「だれ？」をスマホでは折りたたみ・トップの勉強の説明は語学だけ（押して試せるカード）
5. 公開ずみの191本すべてに「言葉なしで押して遊べる部品」（`<section class="toy">`）。仕様は `TOY_SPEC.md`
6. 記事のいちばん下に「🗺 次はどこへ？」の地図（`tools/i18n_runtime.js` の `jumpMap`）
   - 2026-10-09 にトップと同じ**色鉛筆の地図**に変えた。形は `assets/maps.json`（`build-site.py` がトップ index.html の MAPS から写す）。日本を押すと日本地図（県）、フィリピンは街が開く
   - スマホでスクロールするたびに描き直していたバグを直した（幅が変わったときだけ描き直す）
7. いいね：運営者の端末（`?count=off`）で押すと説明が出ていた → その端末では手元だけのいいねにした（`tools/px_runtime.js` の `toggleLike`）
8. 一気に作った306本（心理学・バークマン）を **`lab/`（🧪 試作の棚）** へしまった。道具 `tools/lab.py move|publish|build`、`i18n.py --lab`、`check.py --lab`、`furigana.py --lab`（今回追加）。404.html が古い URL を /lab/ へ。robots.txt で Disallow
9. 306本の**文章を全部書き直した**（人の名前・本の名前・元記事のリンクを消す／80〜130語／「よくある場面→言いたいこと→なぜ→たとえば→今日からできること→まとめ」）。仕様は `LAB_REWRITE_SPEC.md`。`source.md` の出どころに「2026-10-08 本人の指示で…書き直した」
10. 306本の**題名を敬語から普通の見出し**に（ja.json の `"title"`）。例：「〜意味が変わります」→「〜で意味が変わる」
11. CI の赤（`assets/thumbs-src` の616枚に画像の情報が残っていた）→ `strip-exif.py` で消した
12. トップのいちばん下の「🧪 試作の棚」の入口を、読める濃さ・押せる大きさに（本人「スマホで lab が読めない」への手当て）

## ⏸ やっていない・途中のこと
- **スマホで lab/ が読めない件**：クラウドの Chrome（iPhone幅）では一覧・記事とも読めた。本物の Safari では未確認。本人に `https://15-second-blog.com/lab/?debug=1` の画面の写真をもらう。
  ローカル（Mac）なら Safari の「開発 → レスポンシブデザインモード」や、iPhone をつないで Web インスペクタで見られる
- **表紙（Higgsfield）**：コネクタはつながったが、**画像を作る道具がない**（一覧・残高を見るだけ。残り 636 クレジット・starter）。
  ローカルの Claude Code で画像を作れる Higgsfield の MCP がつながるなら、そこで作る。プロンプトの形は `handoff/2026-10-06-psych/COVERS.md`・`prompts.py` が参考
- 前のふわふわペンギンの表紙が付いた約150本を作り直すか → **上書きなので本人の OK が要る**
- 試作の棚から本番に戻す記事を選ぶ（本人が読んでから）→ `python3 tools/lab.py publish <slug>` → 14言語の訳 → いつもの手順
- 💻 IT 用語パックの中身は GCP の言葉が多いまま（作り直すか本人に）
- 5本ほど 130 語を少しこえている lab 記事がある（131〜134語）。気になれば削る
- lab 記事の `series` に `burkeman-notes` という中の名前が残っている（画面には出ない）

## 🧰 ローカルで動かすときのメモ
- テスト用の小さなスクリプトは `scripts/`（クラウドのパスが入っているので、playwright の場所・出力先は直して使う）
  - `mtest-lab.js <出力先> <slug...>`：lab 記事をスマホ幅で開いて、はみ出し・JSエラー・ボタンの大きさ・遊びを押して確かめる
  - `mtest-works.js`：同じことを works の記事で（toy 用）
  - `jumpmap-shot.js <出力先> <slug> <lang>`：記事の下の地図を撮る
  - `toyword.py`：toy の中に英字が入っていないか
  - `sips`：Linux 用の sips の代わり（Mac では不要）
- ローカルサーバー：`python3 -m http.server 8765`（リポジトリの直下で）
- いつもの手順：`build-site.py → next-links.py → prev-links.py → i18n.py → furigana.py → check.py --site`。lab は `lab.py build` だけでいい（i18n --lab と furigana --lab も呼ぶ）
