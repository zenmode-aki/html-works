# 🐼 引き継ぎ（2026-10-06）：メモ4つ → 触って遊べる15秒記事（約300本）

別のアカウントで続けるためのメモ。計画・メモ・道具は、このフォルダにぜんぶある。

## 何をしているか
- 本人が貼ったメモ4つを、1本1つの考えに分けて下書き（`draft/<slug>/`）にした。どの記事にも押して遊べるミニゲーム（スマホ向け）
  - ① パンダの温度 → `NOTES.md` / `PLAN.md`（seq 286–401）
  - ② 未読375記事の学び → `NOTES2.md` / `PLAN2.md`（402–511）
  - ③ 幸せに生きるための考え方 → `NOTES3.md` / `PLAN3.md`（512–551）。クレジットは「📚 I wrote this from my notes on books and blogs I have read.」
  - ④ オリバー・バークマン18本 → `NOTES4.md` / `PLAN4.md`（552–590、シリーズ `burkeman-notes`）
- 書き方のルールは `SPEC.md` ＋ `SPEC2.md`（最後の「Lessons」は必ず守る：裏返すカードの鏡文字・`.emo-pop` の display・クラス名 `.stage/.room/.now` を使わない など）

## いまの状態
- ✅ 表紙つきで下書きサイトに出ているもの：約150本（コミット cd8dde8fd とこのコミット）
- ⏳ 表紙がまだ（`IMAGE:cover.jpg` が残っている → 一覧に出ない）：約150本
  - seq 512–590（③④）は、書いている途中で止まった（API の上限）。**中身の確認がまだ**：`python3 tools/i18n.py --draft --todo <slug>` が `[]`、`python3 tools/check.py --draft --fix-badge <slug>` が IMAGE 以外 ✅ か、ゲームが最後まで動くか
- 本番に出しかけた5本（you-are-loved-for-your-flaws・say-this-is-interesting・the-magic-words-who-cares・nothing-is-a-given・give-your-anger-a-score）は、訳が途中だったので下書きに戻した（2本は14言語の訳あり）

## 本人の最新の希望（2026-10-06）
1. **表紙のペンギンの絵があまり好きじゃない** → デザインを少し変えたい（`COVERS.md` と各 source.md の「表紙のプロンプト」を見直す）
2. **下書きの記事は気に入っている → 本番に出してよい**。訳は**日本語・英語・韓国語の3つだけ**でいい。言い換えパック（it/gcp など）は今は作らなくていい
3. 重い処理はトークンの多い別アカウントで

## 道具（このフォルダ）
- `mtest.js`：iPhone（WebKit）で開いて、はみ出し・エラー・小さいボタンを確かめる（`node mtest.js <出力先> <slug>…`、`python3 -m http.server 8765` をリポジトリで動かしておく）
- `fliptest.js`：裏返すカードを押してスクショ（鏡文字の確認）
- `prompts.py` / `dl.sh` / `setcover.sh`：表紙（Higgsfield gpt_image_2_5、4:3）を作って置く
- `scan.py`：憲法の言葉（会社・上司など）と人の絵文字を探す
- `QUEUE.md`：夜の作業の記録
