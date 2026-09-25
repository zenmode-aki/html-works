# 🌐 タスク：ブログを40言語に対応させる

> このファイルは、Codex など **Claude 以外のAIに渡すための指示書**です。
> 作業を始める前に、**`AGENTS.md`（または `CLAUDE.md`）と `README.md` の「🌐 表示言語の切り替え」を必ず読んでください。**
> 書いた日：2026-09-25

---

## 0. ゴール

LinkedIn などで世界中から読者が来る前に、**40言語で読めるブログ**にする。
ただし「言語を選ぶところで挫折する」ようなメニューにはしない。**ほとんどの人は、メニューを触らずに自分の言語で読める**のが理想。

## 1. 完了時の状態

- 本文は**英語**。訳は「英文 → 訳」の対応表で、1ページの中で文だけ差し替える（ページを言語ごとに複製しない。写真が base64 で入っていて、複製すると容量が倍になるため）
- 現在ある言語：**en（元）/ ja / ko / zh / zh-Hant とフェーズBの23言語、フェーズCの8言語、フェーズDのRTL 4言語**。計40言語、記事は全177本
- ファイルの置き場所

```
works/<slug>/i18n/<lang>.json   記事ごとの訳  {"title": "訳したタイトル", "text": {"英文": "訳"}}
i18n/ui.<lang>.json             全記事に共通の言葉・言語名・注意書き（ko を見本にする）
i18n/top.<lang>.json            トップページの言葉
tools/i18n_runtime.js           ブラウザで動く切り替えの本体
tools/i18n.py                   上の訳と本体を、各ページに埋め込む
```

- 使うコマンド

```bash
python3 tools/i18n.py --todo <slug> <lang>   # その記事の「まだ訳していない英文」を出す
python3 tools/i18n.py --todo-top <lang>      # トップページの「まだ訳していない英文」を出す
python3 tools/i18n.py --check                # 訳の抜けを数える（埋め込みはしない）
python3 tools/i18n.py                        # 全ページに埋め込む
python3 tools/check.py --site                # サイト全体のチェック（1ページ1MB以内など）
```

## 2. フェーズの進捗

**フェーズの順に進める。前のフェーズが本番に出るまで、次に行かない。**

| フェーズ | 言語（コード） | 注意すること |
|---|---|---|
| **A. 土台づくり** | ✅ 完了 | 検索欄なし、既存の地球儀・小旗・A〜Zジャンプを維持。トップ本文訳は選択時に読み込む |
| **B. 左から書く・ふつうの文字** | ✅ 完了・全177記事 | es, fr, de, pt, it, nl, pl, sv, nb, da, fi, cs, ro, ru, uk, tr, el, id, ms, vi, fil, ceb, sw |
| **C. タイ文字・インドの文字** | ✅ 完了・全177記事 | th, hi, bn, ta, te, mr, pa, ne。言語選択時に太字フォントを読み込む |
| **D. 右から書く言語** | ✅ 完了・全177記事 | ar, fa, ur, he。RTLレイアウトと360px表示を確認 |

## 3. フェーズA：言語メニューを作り直す（いちばん大事）

全言語を旗つきで並べると長くなる。**一覧は名前で探せる形にし、ボタンには小さな旗を重ねて「いろいろな言語で読める」と見せる。** 2026-09-25 の本人の希望に合わせ、既存ボタンのデザインは保つ。

### 3-1. 基本は自動で決める

- 今の `pick()` と同じく、ブラウザの言語（`navigator.languages`）で自動で決める。**9割の人はメニューを開かない**のが目標
- 地域つきのコード（`pt-BR`, `es-MX`, `fil-PH`, `nb-NO`, `no` など）も正しく拾う。`no`（ノルウェー語）は `nb` に、`tl`（タガログ語）は `fil` に寄せる

### 3-2. メニューを開いたら、こう見せる

```
[ C ][ E ][ J ][ K ] …         ← 英語名の頭文字ボタン。いちばん上
─────────────────────
 Español            Spanish    ← その人の端末の言語（あれば）
 English
 日本語             Japanese
─────────────────────
 العربية            Arabic     ← ここから全部。英語名のABC順
 বাংলা              Bengali
 Čeština            Czech
 Dansk              Danish
 Deutsch            German
 …
```

- **言語名は、その言語自身で書く**（「スペイン語」ではなく `Español`）。右に英語名を小さく、薄めの色で添える
- 並び順は**英語名のABC順**
- いちばん上に「たぶんこれ」を最大3つ：**端末の言語・English・日本語**（重複は1つにまとめる）
- **検索欄は置かない**（2026-09-25 本人：スマホだとキーボードが勝手に出てじゃま）。代わりに**英語名の頭文字 A〜Z のボタン**を上に並べ、押すとその文字の最初の言語まで一覧がスクロールし、その文字の言語に色がつく。言語のある文字だけボタンにする
- メニューを開いたとき、入力欄やボタンに自動でフォーカスしない
- ボタンは地球マーク＋現在の言語名＋代表的な言語の小さな旗を重ねて表示する（例：🇺🇸 🇯🇵 🇰🇷 🇨🇳）。今の色・丸み・配置の雰囲気を保つ
- 旗はボタンの小さな表示だけに使う。一覧では国旗を並べず、言語自身の名前と英語名で選ぶ
- `i18n/ui.<lang>.json` に `name`（言語自身の名前）、`englishName`（英語名）、`aliases`（端末言語の判定用）、`flag` を用意する
- スマホ（幅360px）で、メニューが画面からはみ出さないこと。長いときはメニューの中だけスクロール
- キーボードでも使えること（Tab・矢印・Enter・Esc）

### 3-3. トップページを軽くする

- 今は**トップページに全言語の訳を埋め込んでいて**、言語が増えると重くなる
- トップページだけ、**選んだ言語の訳を後から読み込む**形にする（`i18n/top-data.<lang>.json` を公開フォルダに置いて `fetch`）。読み込むまでは英語のまま表示されていればよい
- 記事ページは1言語あたり約2KBなので、**今までどおり埋め込みでよい**（40言語でも+70KB程度）
- 1ページ1MB以内のルール（`tools/check.py`）を必ず守る

## 4. 翻訳のルール

- **必ず、公開中の英語本文から訳す。** 日本語訳や韓国語訳からの二次翻訳は禁止
- **直訳でいい。こなれさせない。** 英語の1文 = 訳の1文。まとめない・分けない・順番を変えない。やさしい単語で
- **英語の本文・日本語訳は1文字も変えない**（このタスクは訳を足すだけ）
- 固有名詞（Pengesso、地名、アプリ名）は、既存の `ko.json` / `zh.json` を見て、その言語での自然な書き方にそろえる
- 数字はアラビア数字のまま（`8th floor` → `8階` のように数字を残す）
- 絵文字・HTMLタグ（`<b>` など）は、元の英文にあるものをそのまま残す
- 1言語が終わったら `python3 tools/i18n.py --check` で**抜けが0**になっていることを確かめる

### 注意書き（全部の新しい言語に出す）

運営者は英語と日本語しか読めない。なので `i18n/ui.<lang>.json` に `"unverified": true` と `"notice"` を書く（`ui.ko.json` と同じ形）。
`notice` の元の英文は次のとおり。これを各言語に訳す：

> 🐧 This page was translated by AI. The owner of this site can only read English and Japanese, so he could not check if the translation is right. If you find something strange, please tell us at **pengesso@gmail.com**!

**右から書く言語（ar / fa / ur / he）だけ**、上の文のあとに次の1文を足す：

> This site was made by someone who reads from left to right, so some parts may look a little broken. If it is hard to read, you can switch to English from the 🌐 menu.

## 5. フォント（フェーズC）

- 本人は**細い文字が大嫌い**。どの言語も**太字（700以上）**で出す。細いウェイト（300〜400）や細身の書体は選ばない
- 端末にフォントがない言語だけ、`i18n_runtime.js` の `SOFT` に Google Fonts を足す（今は ja: Zen Maru Gothic、ko: Jua）
  - th: `Noto Sans Thai`／hi・mr・ne: `Noto Sans Devanagari`／bn: `Noto Sans Bengali`／ta: `Noto Sans Tamil`／te: `Noto Sans Telugu`／pa: `Noto Sans Gurmukhi`／ar・fa・ur: `Noto Naskh Arabic` か `Noto Sans Arabic`（ur は `Noto Nastaliq Urdu` も候補）／he: `Noto Sans Hebrew`
  - どれも `wght@700` 以上で読み込む。**その言語を選んだときだけ**読み込む

## 6. 右から書く言語（フェーズD）

- その言語のときは `<html dir="rtl" lang="ar">` にする
- 左右が決め打ちの CSS（`margin-left`、`left: 15px`、`text-align: left` など）を、`margin-inline-start`・`inset-inline-start`・`text-align: start` などに置き換えていく
- **反転させないもの**：地図・写真・グラフ・コード風パネル・数字・英語のまま残る文
- 言語メニュー・「← Back」の矢印・ページ送り（← Previous / Next →）は向きを反転させる
- 完ぺきでなくていい。**文字が重ならない・はみ出さない・読める**ところまで。崩れが残るところは注意書き（§4）でカバーする
- 確認は `?lang=ar` をつけて、トップ・記事数本・スマホ幅（360px）で見る

## 7. 何人かのAIで並行して進めるとき

同じ作業フォルダで、ほかのAIも動いています。ぶつからないように：

- **翻訳係**：1人1言語。触ってよいのは `works/*/i18n/<自分の言語>.json`・`i18n/ui.<自分の言語>.json`・`i18n/top.<自分の言語>.json` **だけ**。`python3 tools/i18n.py`（埋め込み）は流さない
- **まとめ係**：1人だけ。翻訳が終わった言語の JSON を確認して、`python3 tools/i18n.py` → `python3 tools/check.py --site` → commit → push
- `index.html` と `tools/` を直すのは、フェーズA・C・Dの担当1人だけ
- **commit するときは `git add` で自分のファイルだけを名前で指定する。** `git add -A` や `git add .` は、ほかのAIの途中の作業まで本番に出してしまうので禁止
- ファイル・記事の**削除**はしない。必要なら本人（あきくん）に聞く

## 8. モデルの使い分け（本人の方針）

- **英語と日本語は、いちばん良いモデル（Claude Opus）で。**このタスクでは英語・日本語は触らない
- それ以外の言語の訳は、**Codex など安いモデルで回してよい**

## 9. 完了後に保つこと

- `README.md`・`CLAUDE.md`・`AGENTS.md` は現在40言語、全177記事の対応状況を記載する
- 翻訳追加時は公開中の英語本文から直接訳し、`python3 tools/i18n.py --check` と `python3 tools/check.py --site` を確認する
- 画面に訳が反映されることを `python3 tools/i18n-audit.py --all-langs` で確認する
- commit・push するとすぐ本番に出る。ほかの作業を含めず、対象ファイルだけ名前で追加する
