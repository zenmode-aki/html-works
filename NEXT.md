# 📋 次にやること（Codex / ChatGPT への引き継ぎ）

最終更新：2026-09-12（クラーク・バギオシリーズを新設、公開は保留中）

**このファイルを最初に読んでください。** 続きの作業に必要なことは全部ここにあります。
ルールそのものは [PROMPT.md](PROMPT.md) と [README.md](README.md) にあります。

> 🛠 **仕事の話を書くときは [WORK.md](WORK.md) を読んでください。**
> あきくんの文体の仕様（格言を書かない／動作の具体で書く）、日本語の原稿24本、
> 生素材、NG例が全部あります。2026-09-10 に作りました。

---

## 🏫 クラーク・バギオシリーズを新設（2026-09-12・公開は保留中）

「あとで記事にするもの」フォルダの役割を、本人の指示で整理しなおした。

- **「あとで記事にするもの」＝ スマホからGitHubに下書きを置くための一時置き場だけ。**
  記事化・公開が終わったものはここから削除する。今後も本数が増えるシリーズ
  （クラーク・バギオなど）は、ここに置かず**トップレベルの独立フォルダ**にする。
- 既存の `ブリッジSE` `ネットワーク運用保守` `旅` `名古屋と家族` `勉強と資格` と同じ形
  （`情報源.txt` + `記事/連番_タイトル.txt`）で、`クラーク/` `バギオ/` を新設した。
- 「あとで記事にするもの」の中で、すでに `works/` に記事化・公開済みだった10本
  （Chiikawa、おばあちゃんの家、スプラトゥーンほか）は削除した。

### クラーク（フィリピン・クラークの語学学校で日本人マネージャーをしていた時期）

`クラーク/記事/` に12本の下書き（01〜12）がある。`tools/build-site.py` の
`JOBS` には `("clark", "🏫", "Language school", "Clark, Philippines", None)` が
すでに用意ずみ（`assets/jobs/clark.jpg` も既存）。**公開するときは**：

- topic は `ph`、`LEGACY_JOB_POSTS["clark"]` に12本のslugを追加する
  （`baguio-language-school-memories` が `LEGACY_JOB_POSTS["baguio"]` に入っているのと同じやり方）
- `PLACES` に `"clark"` の行・列を追加する（`cebu`/`baguio` の近く）
- age は 20（20歳の誕生日をクラークで祝ってもらった、という本人の話から）

### バギオ（IELTS専門の語学学校に留学していた時期。19歳前後）

`バギオ/記事/` に4本の下書き（01〜04）。既存の `baguio-language-school-memories`
（教室・卒業式の話）とは別の切り口（学校選びの理由・パラフレーズ・ヘアピン・屋上）。
公開するときは、こちらも `LEGACY_JOB_POSTS["baguio"]` に4本を足す。age は 19。

### ⏸️ 公開は保留中（2026-09-12、本人の判断）

16本のうち写真があるのは5本だけ（クラーク03・07、バギオ02・03・04）。
残り11本は表紙になる写真が無く、Higgsfield の画像生成クレジットも
今 **0**（次回リセットは **2026-09-25**）。

本人に「写真がある5本だけ先に出す／写真があれば追加で送る／
クレジット復活を待って16本まとめて出す」の3択を聞いたところ、
**「9/25のクレジット復活を待って16本まとめて公開する」を選択。**
それまでは `クラーク/` `バギオ/` の下書き（.txt・画像）はリポジトリに置いてあるだけで、
`works/` にはまだ実装しない。

**次にやること（9/25以降）：**
1. `higgsfield account status` でクレジット復活を確認
2. 写真が無い11本ぶんの表紙を `z_image` で生成（1枚0.15クレジット）
3. 16本まとめて `works/` に実装（gen.py 方式）、`tools/embed.py`、`seq` 付与
4. 上記の `LEGACY_JOB_POSTS` / `PLACES` を追加してから `tools/build-site.py`
5. `tools/check.py` → `tools/check.py --site` → push

---

## 🔢 一覧の並び順を「公開した順」に直しました（2026-09-11）

**症状：** 同じ日に何本も記事を出す日があると、トップページの一覧が
「新しい日付順」までは合っているが、**同じ日付の中がslugのアルファベット順**に
なってしまい、本人が「アップロード順になっていない」と気づいた。

**原因：** `tools/build-site.py` の並び替えが `(date, slug)` だったため、
`date` が同じ記事どうしは `slug` の文字順で決まっていた。

**直したこと：**

1. 全113本の meta.json に `"seq"` （公開した順の通し番号。1がいちばん古い）を追加した。
   git の履歴から「そのフォルダが最初にリポジトリに追加されたコミット」を
   古い方から数えて番号を振った（`tools/renumber-seq.py`）。
   同じコミットで一気に追加された記事（今日のブリッジSE19本・あとで記事10本）は、
   実際に生成した順番を手で教えて正しい順にした。
2. `tools/build-site.py` の並び替えを `(date, slug)` → `seq` だけに変更。
   `date` はもう並び順には使わず、表示用だけに残っている。
3. `tools/check.py --site` に、`seq` の無い記事を警告する項目を追加した。

**新しい記事を作るときにやること：** meta.json に `"seq"` を1つ足すだけでいい。
値は「そのときの既存の最大値 + 1」。`tools/renumber-seq.py` を毎回動かす必要はない
（あれは初回の一括計算・すでに終わっている）。

```bash
python3 -c "
import json, pathlib
m = max(json.loads((p/'meta.json').read_text())['seq']
        for p in pathlib.Path('works').iterdir() if (p/'meta.json').exists())
print('次の記事の seq は', m + 1)
"
```

⚠️ CI（GitHub Actions）は浅いclone（直近のコミットしか持っていない）なので、
`tools/build-site.py` がビルド時に `git log` を読みに行く作りにはできない。
だから `seq` は毎回 git を読みに行かず、**meta.json に焼き込んだ値**を使う。

---

## 📁「あとで記事にするもの」10本を公開しました（2026-09-11）

`あとで記事にするもの/` フォルダに溜まっていた9つの下書きを、10本の記事にした
（岐阜の話は「ドライブ→到着→茶碗蒸し」で3本に分かれるため）。

| slug | topic | 内容 |
|---|---|---|
| `chiikawa-before-you-visit` | travel | ちいかわの話。本人がすでに英語で書いていた原稿をそのまま使用 |
| `grandmothers-house-in-gifu` | life | 岐阜のおばあちゃんの家（写真3枚） |
| `splatoon-favorite-weapon` | life | スプラトゥーンのローラー武器 |
| `cebu-condo-poolside` | ph | セブのコンドミニアムのプールサイド（写真4枚） |
| `freezing-not-fleeing` | life | 不安になると逃げるのではなくフリーズしている、という気づき |
| `mario-kart-any-age` | life | マリオカート、バイク派 |
| `gifu-drive-service-areas` | life | 岐阜への道中、高速道路のサービスエリア（写真5枚） |
| `chawanmushi-first-time` | life | おばあちゃんの家で初めての茶碗蒸し |
| `kanayama-station-ceiling` | life | 金山駅の天井、アジア大会仕様 |
| `rain-sound-feature` | life | iPhoneの「雨の音」機能 |

**`あとで記事にするもの/` フォルダの中身は削除していません。** 他のシリーズ
（ネットワーク運用保守・ブリッジSE）と同じく、素材の原本として残してある。

### 判断したこと

- **Chiikawaの記事**：用意された画像3枚は使わなかった。公式イラスト2枚
  （`©nagano / chiikawa committee`）は著作権リスク、お店の棚の写真は
  小さい丸顔グッズが密集する構図で集合体恐怖症に触れる可能性があったため。
  生成した表紙も、背景の棚が並んで見えたのでトリミングして安全側に倒した
- **岐阜ドライブの記事**：母のパニック障害への言及は、本人が自分の言葉で書いて
  保存していた内容なので、誇張せずそのまま使用した
- **セブ島のプールサイド**は、ブリッジSEの時期の記事として `tools/build-site.py` の
  `LEGACY_JOB_POSTS["cebu"]` にも足した（仕事ページにも並ぶ）

### 道具

汎用の記事生成スクリプト（本文の途中に何枚でも写真を挟める版）をscratchpadに作った。
`mk3.py`（ブリッジSE用）と違い、`gen.py` は spec の `blocks` に card / photo / map /
youtube / iconrow を好きな順番で並べられる。5枚の実写真＋カードが混ざる
フォトストーリーは、こちらのほうが作りやすい。

### 画像

Higgsfield のクレジットはこれで **使い切った（0credits）**。次のリセットは毎月25日。
9枚を z_image で生成（岐阜ドライブの表紙だけ、すでに用意されていた生成画像を再利用）。

---

## 1. いまどうなっているか

### 入口は1つだけです

| | URL | 中身 |
|---|---|---|
| 🟢 **ブログ** | https://zenmode-aki.github.io/html-works/ | 🐧ペンゲッソの自己紹介＋記事42本 |

**2026-09-04 に、本番前（staging/）と `pengesso.html` をなくしました。**

やったこと：

- `staging/works/` の10本を `works/` へ移した（`japanese-subway-smell` は本番に同じものがあったので捨てた）
- 昔の `staging/prototype-home.html`（🔵見た目の試作）を、そのまま **`index.html`**（本番トップ）にした
- 昔の `index.html`（記事のグリッド）と `pengesso.html` は消した
- `promote.sh` / `demote.sh` / `tools/publish-pengesso.py` も消した（行き先が1つなので要らない）

理由は本人の言葉のまま：**「URLとかサイトが多すぎて、自分が管理できなくなってきた」**
（MacBook・スマホ・複数のAIから触っていて、どれが最新か分からなくなった）。

**もう本番前を作り直さないでください。** 書いたらそのまま `works/` に置いて push＝公開。
直したいところは**出したあとに**直します。

**同じリポジトリ・同じブランチ（main）です。** ChatGPT/Codex も Claude も、
main に commit & push するだけ。ブランチを分ける必要はありません。

### 📸 写真は「もらった分＋生成1枚」（2026-09-06）

あきくんが写真を添付したら、**その写真は必ず記事に入れます。**落としません。
それとは**別に**、表紙用の生成画像を必ず1枚作ります。

```
写真1枚もらった記事 = 🐧 生成した表紙 1枚 ＋ 📷 もらった写真 1枚 = 2枚
```

### 🚀 「ブログ作って」＝ push まで（2026-09-06）

記事を頼まれたら、**公開するところまでが1回の作業**です。
「出していいですか？」と聞かない。下書きで止めない。出したあとに直します。
止めてほしいときは、あきくんのほうから「今回は出さないで」と言います。

### ⚠️ index.html の `POSTS` と `PLACES` だけは手で書かないでください

`index.html` は**手で書いて育てるページ**です。見た目・スロット・ペンゲッソ紹介・
地図の形は、直接編集して大丈夫。

でも記事の一覧だけは `works/<slug>/meta.json` から**差し込み**ます。

```
/* ⬇️ POSTS:START  ⬇️ */ … /* ⬆️ POSTS:END  ⬆️ */
/* ⬇️ PLACES:START ⬇️ */ … /* ⬆️ PLACES:END ⬆️ */
```

```bash
python3 tools/build-site.py     # この2か所を差し込み直す
```

2026-09-02 に実際に衝突が起きました（ChatGPT側とClaude側が同じ日に index.html を
触った）。**この差し込み方式を崩さないでください。**
新しい土地の記事を作るときは、`tools/build-site.py` の `PLACES` に足すこと
（足さないと build が止まります）。

### 道具

```bash
python3 tools/check.py              # 記事を検査
python3 tools/check.py --site       # サイト全体（バッジ・noindex・meta・サムネ・死んだリンク）
python3 tools/check.py --fix-badge  # ワード数バッジを直す
python3 tools/build-site.py         # index.html の記事一覧を差し込み直す
python3 tools/thumbs.py             # assets/thumbs-src/ → assets/thumbs/（macOS専用）
python3 tools/embed.py <slug>       # 記事の中の画像を base64 で埋め込む
python3 tools/components.py         # 地図・動画・スライドの部品を全記事に配る
./local.sh                          # ローカルでサーバを立てて開く
```

**push すると GitHub Actions が自動で検査します**（`.github/workflows/check.yml`）。
記事・サイト全体・トップの一覧が最新かを見て、崩れていれば赤くなります。
Claude と Codex のどちらが push しても同じ基準で止まります。

**push する前に必ず `python3 tools/check.py` と `--site` を通すこと。**

---

## 2. すぐやってほしいこと（優先順）

### ✅ ①名古屋駅の記事の写真（解決ずみ・2026-09-12確認）

Slackの三省堂書店の写真は結局使わず、生成イラスト
（`sleeping-dormouse.jpg` ／「誰も急いでいない、居眠りしているネズミさえも」）で解決していた。
`works/nagoya-station-bookshop/index.html` に画像・figcaptionとも実装ずみ。
このTODOは完了として消してよい。

### ② 記事の中にも画像を足す ✅ 13本は済み

**あとから足した13本には入れました。**これから作る記事も同じようにしてください。

- Higgsfield（`generate_image`、model `recraft_v4_1`）で作る。**クレジットは気にしなくていい**
- ルールは [PROMPT.md](PROMPT.md) の「画像を生成するときの世界観」
  - 人間を出さない／末尾に `No humans, no text, no lettering.`
  - **主役は「ゆるふわなペンギン」で固定**（2026-09-03に本人が決め直した）。
    タコやトカゲに変えない。変えていいのは**毛糸の質感と場面だけ**
  - **表紙（1枚目）は必ず生成画像。**本人の写真は2枚目以降
  - **ネットで拾った写真は貼らない**（権利が分からないので）
- 本文の画像は `images/` に置いて `IMAGE:xxx.jpg` と書き、`tools/embed.py` で base64 に
  （記事の中の画像は base64 のままにする。トップのサムネだけがファイル参照）

**いま使ったペンギンの「質感 × 場面」（重複させない）**

```
ふわふわ羊毛 × スーツケースの横   （thailand-first-trip 表紙）
モヘア       × 小さな木の橋の上   （thailand-first-trip 本文）
シェニール   × ネオンの中でカップ （khaosan-road-chaos）
ループヤーン × ノートの上に座る   （baguio-language-school）
アルパカ     × 平らな湖の島       （burnham-park-flat-walk）
フェルト     × 山を見下ろす手すり （mochi-cafe-baguio）
手編みニット × 眼鏡と新聞（老人風）（tokyo-yakult-tsubakuro）
```

**2026-08 までの11本は、まだ動物がバラバラ**（フクロウ・タコ・カピバラなど）。
気が向いたらペンギンに揃え直せますが、急ぎではありません。

⚠️ Higgsfield は稀に無害な絵を NSFW と誤判定します。落ちたら言い回しを変えて再送すれば通ります。

### ③ ~~ペンゲッソのページに記事を出す~~ ✅ 済み

`build-site.py` が `meta.json` から `var POSTS` を差し込みます。
2026-09-04 にそのページが本番トップ（`index.html`）そのものになりました。

### ③-2 ペンゲッソをもっと作り込む 🔴 ← いまここ

2026-09-03 に本人が言ったこと：

> 「ぺんげっその説明あたりはもっと画像生成とかアニメーションを本気で実装したいね」
> 「まずはちゃんと文章量を減らしたい。ボケよりもちゃんとわかりやすく短く伝える方が優先」

- [x] 文章を 359 → 195 words に圧縮した
- [x] メーターのカウントアップ、カードのずらし出しを追加した
- [x] スマホで横に崩れないようにした（375pxで確認ずみ）
- [x] 試作ではなく、**これが本番トップになった**（2026-09-04）
- [ ] **生成画像をペンゲッソ紹介の中に入れる**（いまは絵文字だけ）
- [ ] もっとアニメーションを増やす（本人いわく「本気で実装したい」）

直す場所は `index.html` の `<section class="about" id="about">` 以下です。
**そこは手で編集していい。**差し込み口（`POSTS` / `PLACES`）にだけ触らないこと。

---

## 2.5 目標ページ `goals/` 🧭

`https://zenmode-aki.github.io/html-works/goals/` — **あきくん自身のためのページ**です。読者向けではありません。

- **中身を書き換えるのは、HTMLの上のほうにある `<script id="data">` のJSONブロックだけ。** CSS・JSは触らない
- 日付は今日から自動計算する（`あと何日` を手で書かない）
- ⏱ バッジは `#fast`（上半分）の文字数だけを数えて秒に直す。**60秒を超えると赤くなる** ＝ 何かを下半分に送る合図
- トップからはリンクしない。検索に出さないのは `robots.txt` の `Disallow: /goals/` でやっている
- **匿名ルールをここにも適用する。** 会社名・通院・家族の詳細は書かない。詳細は非公開リポジトリ `aki-os` 側

---

## 3. 参加型にする（読者から意見をもらう）💬

あきくんがいちばんやりたいこと。**「助けてと言えるようになりたい」の記事**を
きっかけに、**読者からアイデアを借りる**形にしたい。

> 「作りたいものがあって、そのアイディアを誰かから借りるみたいな感じにしたくて、
> 要するにこれを、ブログを読んでる人を参加型にできたらいいなと思ってて」

**必ず「運用主が承認したものだけ載る」形にすること。** 直接書き込める形にはしない。

### 手段の比較

GitHub Pages は静的サイトなのでサーバがありません。だから外の仕組みが要ります。

| # | やり方 | 読者のハードル | 世界観 | 費用 | 手間 |
|---|---|---|---|---|---|
| **A** | **フォームサービス**（Formspree / Basin など） | ⭐ 低い。その場で書ける | ⭐ 自分でデザインできる | 無料枠あり | 中 |
| **B** | Googleフォームへリンク | 低い | ✕ Googleの見た目になる | 無料 | ⭐ 一番小さい |
| **C** | メール（`mailto:`） | ✕ 高い。メールは書かれない | ⭐ 崩れない | 無料 | ⭐ 一番小さい |
| **D** | giscus / utterances（GitHub Issues） | ✕✕ GitHubアカウントが要る | △ | 無料 | 小 |
| **E** | Cloudflare Workers で自作 | ⭐ 低い | ⭐⭐ 完全自由 | 無料枠あり | ✕ 大きい |

**おすすめは A。** 見た目を自分で作れて、読者は1クリックで書けて、承認フローを挟める。
まず **B か C で1本試して、反応があってから A に上げる**のが安全（作りすぎない）。

あきくんが最初に考えていた「Pengesso専用のメールアドレスを作る」は C です。
**世界観としては最高**（ペンギンにメールを出す、という体）だけど、
**メールは本当に書かれません。**そこだけ気をつけてください。

### 承認して載せるまでの流れ（どの手段でも共通）

```
読者が書く
   ↓
あきくんに届く（メール / Slack / スプレッドシート）
   ↓
あきくんが「これ載せて」と言う
   ↓
works/<slug>/comments.json に1件足す
   ↓
python3 tools/build-site.py  →  記事のHTMLに焼き込まれる
   ↓
push  →  公開
```

`comments.json` の形（案）：

```json
[
  { "name": "someone", "from": "🇧🇷 Brazil", "date": "2026-09-10",
    "text": "I just say sorry first, then ask. It works.",
    "reply": "That is cheating. I will try it. 🐧" }
]
```

- **`reply` は、あきくんが書いた、または掲載を明示承認した返事だけを入れる。**AIが勝手に一言を足さない
- 静的HTMLに焼き込むので、サーバもJSも要らない。この repo の思想と合う
- スパムは承認前に落ちるので、サイトには一切出ない

### 記事の形の案

「質問記事」というジャンルを作る。15秒ブログと相性がいい：

```
⚡ 15 seconds to ask you something

<本文：あきくんの悩み。いつも通り35〜55 words>

💬 HOW DO YOU DO IT?
   [ Tell Pengesso ]   ← フォームへ

📮 ANSWERS FROM THE INTERNET
   <承認されたコメントが並ぶ。それぞれにペンゲッソの返事>
```

**答えるほうも15秒で書ける短さにする。**長い入力欄を出さない（1〜2文だけ）。
サイト全体のルール（15秒）と揃えると、参加のハードルが下がります。

---

## 4. まだ手をつけていないこと

計画は `~/.claude/plans/` にありますが、要点はここに写しておきます。

- [x] ~~`promote.sh` / `demote.sh`~~ 🗑 2026-09-04 に削除。行き先が1つなので要らなくなった
- [x] ~~GitHub Actions~~ ✅ できました。実際に緑になっています
- [x] ~~`check.py --site`~~ ✅ できました。さっそく本物の抜けを4件見つけました
      （記事を書き直すときにバッジを落としやすいので、この検査は残しておいてください）
- [ ] 🔴 **毎朝のタスクの書き先を直す** — `~/.claude/scheduled-tasks/blog-morning-cook/SKILL.md`
      が `staging/works/` に書くようになっているなら、`works/` に直すこと。
      **staging/ はもう存在しないので、直さないと毎朝こけます**
      （あきくんの希望：Claude と Codex の両方で、1日2回まわしたい）
- [x] ~~README の古い記述~~ ✅ 直しました
- [x] ~~`_template/index.html` のバッジ~~ ✅ `stage-public` / `PUBLIC` に直しました
- [ ] **2026-08 の11本にも本文画像を足す**（本文に画像があるのは、あとから足した13本）
- [ ] 昔の `pengesso.html` を開くと 404 になります。困るようなら
      `pengesso.html` に「`/` へ飛ぶだけ」の1行HTMLを置けば直せます（いまは置いていない）

---

## 5. 触ってはいけないもの

- **記事内の文章。** あきくんの言葉です。AIが事実・体験・教訓・小言・ツッコミを足さない
  （`card-label` / `h1` も素材だけから整理・英訳する。AIが自由に作れるのは絵文字 / 画像 / CSS / アニメ）
- **`tools/check.py` の `LEGACY` に入っている10本の本文**（2026-08 の「1分ブログ」時代）
- **`index.html` の `POSTS` / `PLACES` を手で編集すること**（必ず `build-site.py` で差し込む）
- **本番前（staging/）を作り直すこと。** 2026-09-04 にあきくんがやめると決めています
  （「URLが多すぎて管理できない」）。**出す場所は1つだけ**
- **承認していないコメントをサイトに出すこと**
- **匿名ルール**：本名・顔・勤務先・学校名・健康状態・収入の額・家族の特定情報は、
  本人が掲載を明示した範囲以外は落とす。顔写真や学校名を本人が明示して使うよう頼んだ場合は、
  その素材だけ使用できる。そこから別の個人情報を推測して足してはいけない
- **承認ボタンのようなUIを足すこと**。2026-09-02 にあきくんが却下しています
  （「👍を押す作業が増えるだけでめんどくさい」）

---

## 6. あきくんが言っていたこと（判断に迷ったとき用）

- **このブログの本当の目的は「あとから自分が思い出すこと」。** 読者のためではない
- **SNSが怖い。**「いいねを押されるのがめちゃくちゃ怖い」。
  だから**いいね・フォロワー数・閲覧数のようなものは絶対に付けない**
- 何を喋るにも長くなるので、**15秒という制約をわざとかけている**
- 書いているのは**ペンゲッソというペンギン**。飼い主（あきくん）に向けて書いている設定。
  ただし、本人が言っていない台詞や小言をAIが追加しない
- 15秒は基本。**「これは1分で書いて」と言われたときは**、文章を水増しせず、
  60〜180 words＋複数写真のフォトストーリーにする
- 2026-09-02 以降は、本人提供の写真をなるべく多く使い、文章を少なめにして、
  コード風パネル・図解・控えめなアニメーションを増やす
- **画像生成のクレジットは気にしなくていい。**ただしフォーマット化した量産はいちばん嫌がる

---

## 🛠 ネットワーク運用保守シリーズ 32本を出しました（2026-09-10）

`ネットワーク運用保守/記事/*.txt` の日本語を英訳して公開しました。
**1ファイル = 1記事**、**素材の文は1つも落としていません。**

### ⛔ このとき、語数の制限をやめました

最初は PROMPT.md の「35〜55 words」に合わせて文を削り、収まらない3本を
Part に割って36本にして出しました。**これは間違いでした。** あきくんの言葉：

> 「その記事に入ってる文章は、その文章量でいいと思ったから僕がそうやって決めてるわけで、
> 勝手にワード数だけで勝手に決めたりしないで。」
> 「勝手にはしょったりしないでほしい。」

なので次の3つを直しました。

1. **`PROMPT.md` §4 を「長さは、素材が決める」に書き換え**（35〜55 words の廃止、
   語数のための Part 分割の禁止、カード枚数の自由化）
2. **`tools/check.py` から語数の合否判定を削除**（数えて表示するだけ。バッジは実測値の目安）
3. **32本ぜんぶを、素材の全文で作り直し**（16番・25番・43番の Part 分割も1本に統合）

本文の合計は **1683 words → 3520 words** になりました。

### 覚えておくこと

**長さで本人の文を削らない。長い素材は長い記事になるだけでいい。**
Part に割るのは、あきくんが「これは分けて」と言ったときだけ。

### ⚠️ 2か所だけ、確認待ちで外してあります

長さの都合ではなく、`情報源.txt` の「出さない＝体制人数」に当たるためです。
**戻してよければ言ってください。**

| 記事 | 外したもの |
|---|---|
| `big-company-felt-like-school` | S2「社員数1000名ほど」（「創業40年以上」は残した） |
| `i-am-a-temp-worker` | S3「1班から6班くらいまで」（「9割」は残した） |

前回まとめてしまっていた「自殺をほのめかす投稿」「JR」「班長やグループ長」
「機器名6つ」「担当3つ」は、**すべて本人の言葉のまま戻しました。**

### 画像

- 表紙は32本ぶん生成（ペンギン固定・質感15種類を順に回す）
- **43番の写真4枚は、1本の記事に全部入っています**（フォトストーリー扱い・上限1.5MB）
- 25番の画像は Teams のアイコンで 148x148 しかないため、引き伸ばさず
  Teams の話をしているカードの中に実寸で置いています（落としてはいない）

### 出した32本

| slug | 素材 | タイトル |
|---|---|---|
| `nice-escalation-sticker` | 8文 | I got a sticker for asking a question that turned out to be a fault |
| `chat-first-then-talk` | 4文 | I cannot talk and think at the same time, so I send a chat first |
| `chu-shortcut-explain-simply` | 2文 | I typed 2 letters into my dictionary to ask for a simple explanation |
| `three-monitors-twelve-screens` | 6文 | I have 3 monitors on my desk and about 12 more on the wall |
| `fax-to-the-police-station` | 5文 | When a cable hangs down from a pole, I fax the police station |
| `map-under-the-cash-register` | 6文 | I draw a map so the field worker can find the box under the register |
| `spare-machine-needs-config` | 5文 | A spare machine does not work until someone puts the config in |
| `veteran-works-through-break` | 6文 | The veteran on my team keeps working through the whole break |
| `faults-come-after-the-lightning` | 4文 | Faults usually happen when the machines come back up after lightning |
| `shakuyou-borrow-the-line` | 4文 | Everyone at work asks if I got the shakuyou, which means borrowing a line |
| `writing-the-outage-notice` | 5文 | Writing the outage notice on our website is also part of my job |
| `everyone-writes-the-timeline` | 7文 | After a big fault everyone writes down what they did at what minute |
| `nothing-goes-home-with-me` | 6文 | I cannot take a single page of work material home with me |
| `i-only-cover-the-middle` | 5文 | In a phone network my part is sometimes only the middle |
| `questions-at-1pm-and-530pm` | 8文 | I send all my questions at 1pm and 5:30pm using a scheduled message |
| `big-company-felt-like-school` | 5文 | My first big company felt like school, where I traced a way already decided |
| `search-before-you-think` | 6文 | When I do not know something, I search the old records before I think |
| `police-ask-who-this-is` | 7文 | The police call us to ask who is behind an IP address |
| `maybe-a-mouse-chewed-it` | 7文 | We look at the papers and guess that maybe a mouse chewed the cable |
| `sending-people-to-the-site` | 4文 | Network operations also means sending a real person out to the site |
| `double-check-every-15-minutes` | 4文 | I say please double check about once every 15 minutes |
| `20-hours-in-the-office` | 4文 | A night shift can leave me in the office for about 20 hours |
| `i-am-a-temp-worker` | 4文 | I am a temp worker doing exactly the same work as permanent staff |
| `one-second-stops-a-factory` | 3文 | My customers are companies, and 1 second of downtime can stop a factory |
| `windows-update-day-slows-network` | 4文 | The network gets tight on Windows Update day every month |
| `70-percent-company-rules` | 3文 | 70% of what I had to learn was company rules, not network knowledge |
| `same-building-strangers` | 4文 | In a big company the same building is full of people I do not know |
| `too-many-departments-to-ask` | 5文 | The departments are split so finely that I have to check who to ask |
| `half-doing-half-recording` | 6文 | About half of my job is doing the work and half is recording it |
| `10-minutes-finding-passwords` | 4文 | 5 or 10 minutes melt away just finding the right password |
| `one-loose-plank-leaks-everything` | 4文 | One loose plank makes the whole barrel leak, they taught me in training |
| `walked-to-work-through-the-flood` | 12文 | I walked to work through a road that had turned into a river |

**添削するときは `works/<slug>/source.md` を渡してください**（index.html は出力物です）。

---

## 🔧 添削・サイト機能まとめ（2026-09-11・ブリッジSE19本のあと）

### ✏️ 添削（本人の言葉に忠実に直した）

| 記事 | 直したこと |
|---|---|
| `20-hours-in-the-office` | 愚痴のオチ → 「12時を過ぎると元気が湧いてくる」という体の不思議さのオチに変えた |
| `same-building-strangers` | 「不満」→「驚き」の言い方に変えた |
| `too-many-departments-to-ask` | 具体的な担当名（公共サービス・金融など）を消して「営業部を例にとると」に変えた |
| `10-minutes-finding-passwords` | 「大企業だと」→「運用保守の仕事だと」に変えた |
| `walked-to-work-through-the-flood` | 時計の写真を「洪水が引いていた」の文の直後に移動。「排水システムがいいなら、そもそも冠水しなかったのでは」というツッコミのカードを追加 |
| `turn-off-everything-else` | 「今に集中しようとはしない」→「集中しようと考えすぎると力む。だから逆に今以外を電源オフにする」という逆転の発想の説明に変えた |
| `ai-can-translate` | （前回すでに直した）クラウド・インフラの話を削除 |

### 🐛 バグ修正

`sakura-english-mixed-language` の表示崩れは、`<a class="next">` の中に紛れ込んだ
**制御文字（`\x02`）が原因**だった。全記事をスキャンして、この1本だけだったことを確認して直した。

### 🖱 スライドに ◀ ▶ ボタンを追加

「写真をスライドさせるのはマウスだと難しいから」という要望で、
`tools/components.py` に `inject_arrows()` を追加。**実際にスライド（`.slides-track`）がある
記事だけ**を判定して足す（`khaosan-road-chaos` と `tokyo-yakult-tsubakuro` の2本）。

⚠️ 最初のガード条件が甘くて全102本に入ってしまった事故があった。
`.slides-track` という文字列は CSS の中にも出てくるので、**HTML内に実際の
`<div class="slides-track">` があるかで判定し直す必要がある。** 次に似た部品を足すときも注意。

### 🎨 `khaosan-road-chaos` の配色を明るくした

このタイ記事だけ `_template` を使わない独自のダークネイビー配色（`#0c1020`）だった。
本人が「デザインが好きじゃない」と言ったので、暖色系の明るい配色（`#fff4e2`）に総入れ替えした。
アコーディオンのように色を1か所ずつ潰していく必要があるので、次に似た独自デザインの
記事を直すときは、`:root` だけでなく `.hero`・`figcaption`・`.route`・`.codeblock`・`.maplink`
などダークな背景色がベタ書きされている箇所を全部洗い出すこと。

### 🕶 favicon を追加した

トップページと全102本の記事の `<head>` に、ペンゲッソがサングラスをかけた顔の
favicon を追加した（`assets/favicon.png` / `favicon-32.png` / `favicon-180.png`）。
生成は z_image。`_template/index.html` にも入れたので、**新しく作る記事には
自動で入る。** 新しいトップページを作るときは `assets/favicon-32.png`
（32x32）と `favicon-180.png`（apple-touch-icon）を参照すること。

### 🏷 一覧に「どの仕事の話か」のバッジを追加

「仕事の内容が記事の一覧の中に入っているとタイトルが意味わからなすぎる」という指摘。
`tools/build-site.py` の POSTS に `topic` を足し、トップページの `drawFeed()` で
`topic` が `netops` か `bridge` の記事だけに、小さな色つきバッジ（🛠 Network Ops /
🌉 Bridge SE）を出すようにした。他のtopic（ph/travel/study/ai/blog/life）には出していない
（本人の要望が「仕事に関する記事」だったため、スコープを絞った）。

### 🎧 新しい記事を1本書いた

`yonezu-kenshi-raven` — 米津玄師「烏」を聴いて感じたことの記事。topic は `life`。
歌詞の引用2つは日本の著作権法32条の引用の範囲で扱い、`.lyric` の見た目で本文と
区別し、アーティスト名を必ず添えた。Spotifyへのリンクは iframe にせず、
YouTubeカードと同じ考え方で「カード＋リンク」（`.spotify-card`）にしてある。

### 💳 Higgsfield クレジット

このセッションで favicon 1枚・記事画像1枚を追加生成した。残り **1.2クレジット**。
リセットは**毎月25日**（前回の付与記録が 2026-08-25 の270クレジットだったところから逆算）。

---

## 🌉 ブリッジSEシリーズ 19本を出しました（2026-09-11）

`ブリッジSE/記事/*.txt` の日本語を英訳して公開しました。
**1ファイル = 1記事**、**素材の文は1つも落としていません。**

### カテゴリーの出しかた

| topic | バッジ | 本数 | 中身 |
|---|---|---|---|
| `bridge` | 🌉 BRIDGE ENGINEER | 14 | 仕事そのものの話 |
| `ph` | 🇵🇭 LIVING IN THE PHILIPPINES | 5 | セブでの暮らしの話 |

セブ暮らしの5本は、読者向けには 🇵🇭 のバッジを出しつつ、
`tools/build-site.py` の `LEGACY_JOB_POSTS["cebu"]` に足して、
💻 Bridge engineer の仕事にも並ぶようにしてあります
（暮らしていた時期がそのままブリッジSEの時期なので）。

### 出した19本

| slug | topic | タイトル |
|---|---|---|
| `why-not-japan` | bridge | The work went overseas because it cost less, so I sat in the middle |
| `ai-can-translate` | bridge | AI can translate, so I decided to go towards technology instead |
| `cant-explain` | bridge | If I did not understand it myself, I could not explain it |
| `en-to-jp-harder` | bridge | English into Japanese was much harder than Japanese into English |
| `skill-over-language` | bridge | Technical skill mattered far more than language skill |
| `engineers-30-min` | bridge | An engineer's 30 minutes is time the client is paying for |
| `translate-back` | bridge | After translating into Japanese, I translated it back into English to check |
| `not-i-can-do-it` | bridge | I tried not to say we can do it too easily |
| `get-a-stamp` | bridge | After talking, I typed the same thing into chat and waited for a stamp |
| `trust-the-buffer` | bridge | I decided to follow the buffer the PM made without complaining |
| `only-japanese-person` | bridge | The projects where I was the only Japanese person were the most rewarding |
| `that-email` | bridge | The client's thank you email was the happiest moment I had at work |
| `after-the-meeting` | bridge | The moment a meeting ended was when I felt the most relief |
| `minutes-in-one-minute` | bridge | People were surprised when I made the meeting minutes in 1 minute |
| `no-public-scolding` | ph | In the Philippines, scolding someone in front of others is a taboo |
| `walking-on-the-7th-floor` | ph | When I could not sleep, I walked round and round the 7th floor |
| `concierge-downstairs` | ph | There was a concierge on the ground floor of my building in Cebu |
| `my-room-on-video` | ph | I filmed the inside of my studio room right before I moved out |
| `120-eggs` | ph | When I lived in Cebu, my fridge was always full of eggs |

### 🚧 まだ出していないもの

**`ブリッジSE/記事/23_セブで暮らしてた、平日の夜.txt` は骨組みのままです。**
「仕事が終わって、まず何をしてた?／ごはんは?／洗濯は?／何時に寝てた?」が空欄。
あきくんの記憶が入ったら記事にできます。

### 画像について（⚠️ ここは今回だけ違う）

**生成モデルを `nano_banana_2`（2クレジット）から `z_image`（0.15クレジット）に変えました。**
残高が 7.65 クレジットしかなく、37枚だと `nano_banana_2` では 74 クレジット必要だったためです。

`z_image` でも「リアル・3D寄り・お腹は無地・人間なし」は問題なく出せています。
**クレジットが戻ったら、好みに合わない絵だけ `nano_banana_2` で作り直せば済みます。**

```bash
higgsfield generate cost z_image --prompt "test"   # 0.15 クレジット
```

- 3本だけ、本人の YouTube 動画をカード＋リンクで入れています（§14／iframeにしない）
- `120-eggs` は本人の冷蔵庫の写真があるので、生成は表紙1枚だけ（§12「写真が優先」）。
  **卵を大量に並べた絵はわざと作っていません**（集合体恐怖症への配慮／§12）
- `120-eggs` の地図は OpenStreetMap。Googleマップは iframe で埋め込めないのでリンクだけ

---

## 🖼 画像まわりの宿題（2026-09-11 にルールが変わった）

本人の指示で3つ変えた（[PROMPT.md §12](PROMPT.md) / [§4](PROMPT.md) / [README.md](README.md)）。
**ルールは直したが、既存の74本はまだ作り直していない。** 手が空いたら順に直す。

### 1. ガラスっぽい画像をやめる

`stained glass` を質感リストから削除した。以下の3本が該当するので**表紙を作り直す**。

- `20-hours-in-the-office`
- `faults-come-after-the-lightning`
- `sakura-english-mixed-language`

### 2. 生成画像を1記事2枚にする

いまはどの記事も表紙1枚だけ。2枚目（記事の真ん中あたり）を足していく。

- 2枚目は**ペンギンでなくてよい**。記事に出てくるモノ・場面をリアルに描いてよい
- オチ（`.big`）の直前には置かない
- 本人の写真が2枚以上ある記事（43番など）は、生成は表紙1枚のままでよい
- テンプレートに `IMAGE:scene.jpg` の置き場所を用意してある

### 3. 分けるときは前の記事へのリンクを置く

`.prev`（BEFORE THIS）の CSS と HTML をテンプレートに入れてある。
いま Part に分かれている記事は無いので、既存記事の修正は不要。

### 画像生成の環境（2026-09-10 に用意した）

Higgsfield CLI が入っていて認証も通っている。

```bash
higgsfield account status                     # 残クレジット
higgsfield generate create nano_banana_2 --prompt "..." --wait --wait-timeout 8m
```

1枚2クレジット。出てきたURLを curl で落として `sips` で縮めてから `images/` に置き、
`python3 tools/embed.py <slug>` で base64 に埋め込む。

---

## ✅ トップの地図：Japan をクリックしたときの動き（2026-09-11 に実装ずみ）

### 直した内容

世界地図で `Japan` をクリックすると、**いきなり日本の記事一覧までスクロール**していた。
本人の指示で、**まず都道府県の日本地図を出して、そこで止まる**ようにした。

> 「世界地図から日本をクリックすると、いきなり記事一覧に行っちゃうから、それが嫌なの。それだけ」

```
before  世界地図 →[Japan]→ 記事一覧までスクロール
after   世界地図 →[Japan]→ 日本地図がふわっと出る（ここで止まる）
                 →[県]→ 記事一覧までスクロール
```

### どこを触ったか（index.html）

- `openCountry('jp')` の最後を `goToPosts()` → `goToMap()` に変更
- `goToMap()` を新設（`.map-stage` を画面の中央に収める）
- `.map2.just-opened svg.main` に `map-in` のアニメーションを追加
  （0.42秒でふわっと。`prefers-reduced-motion` のときは動かない）
- 県をクリックしたときは、今までどおり記事一覧へスクロールする

