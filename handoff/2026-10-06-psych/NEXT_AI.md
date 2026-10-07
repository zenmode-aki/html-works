# 🤖 次のAIへ（2026-10-07・途中の作業ぜんぶ）

まず読む：`CLAUDE.md`（ブログ憲法がいちばん上）→ このフォルダの `HANDOFF.md` → `SPEC.md` `SPEC2.md`

## 途中だったこと（止まった理由：API の使用上限。中身はそのまま draft/ に入っている）
| バッチ | seq | 状態 |
|---|---|---|
| A〜W（①②③の一部） | 286–521 | 本文は完成。A〜G・K は表紙つきで下書きサイトに公開ずみ |
| 表紙まだ | H I J L M N O P Q R S T U V W | 本文は完成。表紙だけ（`COVERS.md` の手順、`prompts.py`→生成→`dl.sh`→`setcover.sh`） |
| X Y Z（③） | 522–551 | 書いている途中で停止。各記事の `--todo` と `check.py --draft` と iPhone テストで確かめて仕上げる |
| BK1〜BK4（④バークマン） | 552–590 | 同上。BK4 は「dailyish のカードのラベルを直す → iPhone テスト」の途中 |
| 本番に出しかけた5本 | — | 下書きに戻した（nothing-is-a-given・give-your-anger-a-score は14言語の訳あり、ほか3本は ja だけ） |

## 本人の最新の指示（2026-10-06）
- 表紙のペンギンの絵があまり好きじゃない → デザインを少し変えたい
- 下書きの記事は気に入っている → **本番に出してよい**。訳は **日本語・英語・韓国語の3つだけ**。言い換えパックは今は作らない
- 質問せず、AI の判断で進めてよい（削除だけは確認）

## 見つけたバグ（直し方は SPEC2.md の最後）
- 裏返すカードが iPhone Safari で鏡文字になる → 半分回ったところで visibility を入れかえる（13本直した。③④の書きかけは未確認）
- iPhone テストで「element is not stable」は、ボタンがずっと揺れているだけ（バグではない）

## 手順の早見
- 下書き一覧を作り直す：`python3 tools/draft.py build`
- 本番へ：`python3 tools/draft.py publish <slug>` → ko の訳 → `build-site.py` → `next-links.py` → `prev-links.py` → `i18n.py` → `furigana.py` → `check.py --site` → push（`git add` は自分のファイルだけ名前で）
