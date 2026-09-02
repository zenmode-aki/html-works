# ⚡ 15 Second Blog

**15秒で読み切れる、かんたんな英語のHTML記事を置くところ。**

ビルドもCMSもログインも要らない。HTMLを1枚書いて、push するだけ。

🌏 **公開URL（本番）** → https://zenmode-aki.github.io/html-works/

---

## 🖥 ローカルで見る（本番に出す前のもの）

Mac でこれを打つだけ。サーバが立って、ブラウザが勝手に開きます。

```bash
cd ~/Developer/html-works && ./local.sh
```

開いたら、そこから全部たどれます。直接行きたいときは：

| | URL |
|---|---|
| 🖥 **ローカル版の入口**（まずここ） | http://localhost:8811/drafts/index.html |
| ⚡ トップの試作（スロット・検索・地図・ペンゲッソ） | http://localhost:8811/drafts/_prototype-home.html |
| 🌏 いまの本番トップをローカルで確認 | http://localhost:8811/index.html |

止めるとき：

```bash
cd ~/Developer/html-works && ./local.sh stop
```

⚠️ `drafts/` の中は **GitHub に上がりません**。自分のMacの中だけです。
だから上のURLは、あきくんのMacでしか開きません（世界からは見えない）。

---

## 🎯 これは何のためにあるのか

**世界のどこかにいる誰かが、たまたま15秒くれた。その15秒で驚かせて、
「こいつと話してみたいな」と思わせる。** それだけが目的。

だから基準は「正確に理解させること」ではなく、**「分かった気にさせること」**。
完璧なブログサイトより、汚くても雑でも、読んでて面白いほうが勝ち。

> 「いま、このブログを書く目的は、自分と友達になりたいって思ってもらえる人を世界から探し出すこと。
> ということは基準は、完璧なブログサイトよりも、汚くても雑でもちゃんと情報があって、
> 読んでて面白いかが大事なのかも。そんなに正確にジャッジされないからさ」

---

## 🎯 決めごと

| | |
|---|---|
| 言語 | **英語のみ。** 日本語版は作らない（素材の日本語は `source.md` に残す） |
| 長さ | 本文 **35〜55 words**（55 words ≒ 18秒）。**基本ベース。**「1分で書いて」と言われたときだけ 120〜180 words |
| タイトル | **キャッチーにしない。**読んだだけで中身がわかる説明文にする |
| 右上 | **LOCAL（下書き）／ PUBLIC（公開ずみ）**を必ず出す |
| 長さの表示 | ページ上部に `⚡ 47 words · 16 sec` を出す |
| カード | **3〜5枚**。1枚に1〜2文 |
| 見出し | **絵文字だけにしない。**英単語2〜3語のラベルを必ず付ける |
| 一覧のサムネ | **絵文字ではなく画像。**1記事1枚、正方形で生成する |
| 動き | **必ず何か動かす。**ただし大げさなアニメは作らない |
| トーン | **反転させる。**真面目な話ほどポップに、どうでもいい話ほど荘厳に |
| 画像 | **必ず base64 で埋め込む。** 相対パスも外部URLも使わない |
| 1記事のサイズ | **400KB以内**（幅1200px・quality 72 に縮小してから埋め込む） |
| 更新ペース | 毎朝AIが下書きを作る。気が向いたときにOKを出す |
| 匿名 | 本名・顔・勤務先・学校名は出さない |

---

## 🎭 中身と演出は、層が違う ← いちばん大事なルール

| 層 | どこ | 誰が書く | word数 | 「追加した文：0」の対象 |
|---|---|---|---|---|
| **中身** | `.card` の中の `<p>` | **本人だけ** | 数える | **対象** |
| **演出** | `card-label` / `h1` / `.quip` / 絵文字 / CSS / アニメ | **AI自由。ボケていい** | 数えない | 対象外 |

**事実を足すのは禁止。ツッコミを入れるのは歓迎。**

この線は `tools/check.py` が機械的に守っている（`<p>` の中身しか数えない）。
だからAIは、中身に手を出さずに、演出だけで思いきり遊べる。

---

## 📚 作品

### ⚡ 15 SECOND

（ここに新しい記事が増えていく）

### 📖 THE 1-MINUTE ARCHIVE

2026年8月に「1分ブログ」として書いた10本。**本人の英文なので書き換えない。**
`tools/check.py` の `LEGACY` に入っていて、当時のルール（120〜180 words）で判定される。

| 日付 | タイトル | 長さ |
|---|---|---|
| 2026.08.28 | [🌀 Stop Overthinking Practice](works/stop-overthinking-practice/index.html) | 178 words · 59 sec |
| 2026.08.27 | [👥 Japan × Philippines #2: The Working Side](works/japan-philippines-work/index.html) | 170 words · 57 sec |
| 2026.08.27 | [🛒 Japan × Philippines #1: Inside the Store](works/japan-philippines-shops/index.html) | 171 words · 57 sec |
| 2026.08.27 | [✂️ Perfectionism #3: Choose 3 Things to Leave Behind First](works/perfectionist-3/index.html) | 179 words · 60 sec |
| 2026.08.27 | [🌀 Perfectionism #2: Preparation Never Becomes Perfect](works/perfectionist-2/index.html) | 143 words · 48 sec |
| 2026.08.27 | [🧩 Perfectionism #1: Why Perfectionists Love Starting](works/perfectionist-1/index.html) | 161 words · 54 sec |
| 2026.08.26 | [📤 Knowledge Metabo #3: Only Output Makes Life Roll](works/knowledge-metabo-3/index.html) | 144 words · 48 sec |
| 2026.08.26 | [🔎 Knowledge Metabo #2: I Looked for the Correct Answer](works/knowledge-metabo-2/index.html) | 139 words · 46 sec |
| 2026.08.26 | [🎧 Knowledge Metabo #1: I Knew More. I Moved Less.](works/knowledge-metabo-1/index.html) | 146 words · 49 sec |
| 2026.08.26 | [⚾ I Played Pawapuro Again After a Long Time! 🎮](works/pawapuro/index.html) | 163 words · 54 sec |

---

## 🤖 いつもの流れ：Slackに書くだけ

**0→1はAIがやる。あきくんはダメ出しするだけ。**

```
    いつでも   Slackの好きなチャンネルに、思ったことをポンと書く
                 （#today- 以外の12チャンネルを見ている）
                    ↓
    毎朝 6:00   AIが昨日ぶんを全部読んで、15秒記事の下書きを作る（最大3本）
                 → drafts/<slug>/ に置く。**GitHubには上げない**
                    ↓
      あきくん   drafts/index.html を開いて、気が向いたときに眺める
                 「これ出して」「ここ直して」と口で言う
                    ↓
                言われたときだけ works/ へ移して push → 公開
```

**承認ボタンのようなものは作らない。** 👍を押す作業が増えるだけなので、
2026-09-02 に本人がその案を却下した。**押す作業を増やさないこと。**

### 🚦 LOCAL と PUBLIC

いま見ているのが下書きか本番か、**記事の右上に必ず出る。**

| | 意味 | 場所 |
|---|---|---|
| 🟡 **LOCAL** | 下書き。自分のパソコンの中だけ。世界には出ていない | `drafts/` |
| 🟢 **PUBLIC** | 世界に公開されている | `works/` |

公開するときに `LOCAL` → `PUBLIC` に書き換える。

### スケジュールタスク

| taskId | 時刻 | 何をするか |
|---|---|---|
| `blog-morning-cook` | 毎朝 6:00 | Slack12chを読む → `drafts/` に下書きを作る。**push もSlack投稿もしない** |

⚠️ **Claude Codeアプリが開いている間だけ動く。** 閉じていたら次に開いたときにまとめて走る。

止めたいとき・時間を変えたいとき：Claude Codeに「朝のブログ生成を止めて」と言えばいい。

---

## ✍️ 手で1本ふやす手順

AIに任せず、自分で書きたいときはこっち。

```bash
cd ~/Developer/html-works && ./new-post.sh nagoya-dome
```

1. **日本語を `works/nagoya-dome/source.md` に貼る**（音声入力そのまま。`S1.` `S2.` と番号を振る）
2. **[PROMPT.md](PROMPT.md) をAIに貼って、素材を渡す** → `index.html` を書いてもらう
3. **写真を `works/nagoya-dome/images/` に入れる**。HTMLには `src="IMAGE:photo.jpg"` と書いておく

```bash
python3 tools/embed.py nagoya-dome   # 縮小して base64 で埋め込む
python3 tools/check.py  nagoya-dome  # 「追加した文：0」を確認する
```

4. **一覧用のサムネ画像を1枚つくる**（正方形・被写体は中央に大きく）
   `assets/thumbs-src/nagoya-dome.jpg` に置く

```bash
python3 tools/thumbs.py nagoya-dome  # 240px正方形にして base64 で埋め込む
```

5. トップの `index.html` の `⚡ 15 SECOND` セクションに作品カードを1つ足す
   （サムネは `<img src="THUMB:nagoya-dome" alt="...">` と書くだけ）
6. ひとつ前の記事の末尾の `Next ⚡` を、この記事に向ける
7. `git add -A && git commit -m "add nagoya-dome" && git push`

---

## 🔍 なぜ `source.md` を分けるのか

`index.html` は画像込みで数百KBある。**これをAIに渡して「直して」とは頼めない。**

```
source.md   ← 日本語の原本。AIに渡すのはこっち
index.html  ← 出力物。ブラウザで開くためのもの
images/     ← 縮小する前の画像の原本
```

将来「30本たまったから一箇所にまとめ直したい」となったとき、
**`source.md` を30枚渡せば、そこから作り直せる。** これがこの構成のいちばんの理由。

Slackから自動生成したものは、`## 出どころ` に **permalink** が残る。
「これ何の話だっけ」となったら、元の独り言まで辿れる。

---

## 📸 なぜ base64 で埋め込むのか

**「スマホで見れないんだけど」を絶対に起こさないため。**

相対パス（`assets/photo.jpg`）は、フォルダ構成を変えた瞬間に壊れる。
つまり**将来まとめ直すときに、一番壊れる**。自己完結したHTMLなら、コピーするだけで動く。

重さの問題は縮小で解決している：

```
pawapuro:  708KB  →  317KB
           ↑ 元は 1536px・511KB の写真1枚で 98.5% を占めていた
           幅1200px・quality 72 に縮小 → 230KB → base64で307KB
```

15秒記事は写真が1枚なので、もっと軽くなる。GitHub Pages のソフト上限は1GB。

手で縮小したいとき：

```bash
sips -Z 1200 --setProperty formatOptions 72 photo.jpg -o photo-small.jpg
```

---

## 🧰 中身

```
html-works/
├── index.html        トップページ（⚡15秒 と 📖1分アーカイブ の2セクション）
├── PROMPT.md      ⭐ AIに渡すマスタープロンプト。記事を作るときはこれを貼る
├── new-post.sh       ./new-post.sh <slug> で1本生える
├── .gitignore        drafts/ と .blog-queue/ を push しないための蓋
├── assets/
│   └── thumbs-src/   一覧サムネの元画像（生成物）。埋め込みに使う原本
├── tools/
│   ├── embed.py      記事の画像を縮小して base64 で埋め込む
│   ├── thumbs.py     一覧サムネを240px正方形にして base64 で埋め込む
│   └── check.py      納品チェック（サイズ・words・ラベル・動き・SOURCE MAP）
├── _template/
│   ├── index.html    記事のひな形（部品とモーションキットが全部入っている）
│   └── source.md     素材の書き込みフォーマット
├── drafts/        🔒 AIが毎朝作る下書き。gitに乗らない
├── .blog-queue/   🔒 どのSlackメッセージまで記事にしたかの記録。gitに乗らない
└── works/
    └── pawapuro/
        ├── index.html
        ├── source.md
        └── images/
```

### 🧩 使える部品

```
.wc-badge      ⚡ 47 words · 16 sec       ← 上部。読者への親切であり、AIへの歯止め
.home          ← Back to all works
.label         ⚡ 15 SECOND BLOG ⚡
h1             タイトル（AIが自由に付けていい）
.photo         写真（角丸・影・わずかに傾く）
.card          本文カード ← 主役。3〜5枚。1枚に1〜2文
  └ .card-head    見出し行
      ├ .card-emoji   絵文字
      └ .card-label   ⭐ 英単語2〜3語。必須。絵文字だけは禁止
  └ .big          オチの一言（本人の言葉）
  └ .quip         ⭐ AIのボケ。1記事に2個まで。word数に入らない
.timeline      段階を見せるとき（色が自動で変わる）
.next          ⚡ 次の記事へ直行するボタン
.youtube-card  動画へのリンク（iframeにしない）
.float         包んだ絵文字がゆっくり揺れる
```

**新しい記事を作るときにやること**：`.card` をコピーして中身を差し替えるだけ。
**モーションキットのCSSは触らなくていい。**

---

## ✅ push する前に

```bash
python3 tools/check.py
```

これが通れば push していい。見るのは9つ。

```
□ 400KB以内か
□ 画像がすべて base64 か（リンク切れの余地がないか）
□ 本文が 35〜55 words か
□ バッジの数字が本文と合っているか      ← --fix-badge で自動で直せる
□ 追加した文：0 になっているか          ← ここだけ見ればいい
□ source.md があるか
□ カードの数だけ card-label があるか（2〜3語か）
□ .quip が2個以内か
□ prefers-reduced-motion があるか
```

---

## ⛔ 触ってはいけないもの

- **記事の `<p>` は本人のもの。AIが体験・感想・事実を創作しない。**
  ただし `card-label` `.quip` `h1` 絵文字 CSS アニメはAIが自由に作っていい
- **1分ブログ時代の10本を書き換えない。**本人が書いた英文。`LEGACY` で守っている
- 本名・顔写真・勤務先・学校名・健康や収入の話は載せない（**匿名でやると決めている**）
  ← Slackから自動生成するので、ここが今までより危ない。迷ったら落とす
- **フレームワーク・npm・ビルドを足さない**（素のHTML/CSS だけ）
  JavaScriptは、モーションキットの IntersectionObserver だけ許可。外部ライブラリは禁止
- `prefers-reduced-motion` のブロックを消さない
- `drafts/` を push しない（`.gitignore` で蓋をしてあるが、`git add -A` の中身は毎回見る）

> 「普通に文章で書くとなんかちょっとだけしんどい気分になるんだけど、
> HTMLで書くってなると、比較的、自分の文章に嫌気がしないなと思ってて。」（2026年8月1日）

便利にしようとしてCMSを足すと、この体験が壊れる。**素のHTMLのままにしておくこと。**

---

## 🔀 `pengesso` との違い

`aki-os/projects/pengesso`（非公開）には、日本語＋英語の記事が10本ある。あちらは触っていない。

| | **html-works（ここ）** | pengesso |
|---|---|---|
| 長さ | 15秒・35〜55 words | 長さ自由 |
| 言語 | 英語のみ | 日本語＋英語の切替 |
| 画像 | base64で自己完結 | `assets/img/` に相対パス |
| 公開 | GitHub Pages（無料・公開リポジトリ） | Vercel（非公開リポジトリのため） |
| 速さ | **Slackに書けば翌朝できてる** | ちゃんと書く |
