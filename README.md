# ⚡ 15 Second Blog

**15秒で読み切れる、かんたんな英語のHTML記事を置くところ。**

ビルドもCMSもログインも要らない。HTMLを1枚書いて、push するだけ。

## 🔗 3つの入口

**スマホからでも、この3つのURLを開けば全部見られます。**

| | 何が置いてあるか | URL |
|---|---|---|
| 🟢 **本番** | 世界に公開しているブログ。ここだけが検索に出る | https://zenmode-aki.github.io/html-works/ |
| 🟡 **本番前（記事）** | まだ出していない記事の置き場。**中身**を確かめるところ | https://zenmode-aki.github.io/html-works/staging/ |
| 🔵 **本番前（見た目）** | 次のトップページの試作。**デザイン**を確かめるところ<br>スロット／検索／日本地図・世界地図／🐧ペンゲッソの自己紹介 | https://zenmode-aki.github.io/html-works/staging/prototype-home.html |

### なぜ「本番前」が2つあるのか

**変わるタイミングが別々だから。**

```
🟡 本番前（記事）    毎朝ふえる。中身の話。「この記事、出していい？」
🔵 本番前（見た目）  たまにしか触らない。ガワの話。「このトップ、かっこいい？」
```

記事が1本ふえても見た目は変わらないし、見た目を作り直しても記事は1文字も変わらない。
**混ぜると「どっちを見ているのか」が分からなくなるので、URLごと分けてあります。**

🟡 と 🔵 はどちらも `staging/` の中。**URLを知っている人しか来られないし、検索にも出ません**
（`robots.txt` + `noindex`）。本番トップからはリンクしていません。

> 📋 **続きの作業をするときは、まず [NEXT.md](NEXT.md) を読んでください。**
> いまどうなっているか・次にやること・触ってはいけないものが全部書いてあります。

---

## 🖥 ローカルで見る（本番に出す前のもの）

Mac でこれを打つだけ。サーバが立って、ブラウザが勝手に開きます。

```bash
cd ~/Developer/html-works && ./local.sh
```

開いたら、そこから全部たどれます。直接行きたいときは：

上の3つと、同じ並びです。

| | URL |
|---|---|
| 🟢 **本番** | http://localhost:8811/index.html |
| 🟡 **本番前（記事）**（まずここ） | http://localhost:8811/staging/index.html |
| 🔵 **本番前（見た目）** | http://localhost:8811/staging/prototype-home.html |

止めるとき：

```bash
cd ~/Developer/html-works && ./local.sh stop
```

⚠️ ローカルは **自分のMacの中だけ。**スマホからは見られません。
スマホで見たいときは、push してから上の 🟢🟡🔵 のURLを開いてください。

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
| 長さ | 本文 **35〜55 words**が基本。「1分で」と言われたら **フォトストーリー（60〜180 words＋複数写真）**にする。文章を水増しせず、写真を見る時間も含めて約1分 |
| タイトル | **キャッチーにしない。**読んだだけで中身がわかる説明文にする |
| 右上 | **STAGING（本番前）／ PUBLIC（公開ずみ）**を必ず出す |
| 長さの表示 | ページ上部に `⚡ 47 words · 16 sec` を出す |
| カード | **3〜5枚**。1枚に1〜2文。フォトストーリーは写真ギャラリーを挟み、最大6枚まで |
| 見出し | **絵文字だけにしない。**英単語2〜3語のラベルを必ず付ける |
| 一覧のサムネ | **絵文字ではなく画像。**1記事1枚、正方形で生成する |
| 動き | **必ず何か動かす。**ただし大げさなアニメは作らない |
| トーン | **反転させる。**真面目な話ほどポップに、どうでもいい話ほど荘厳に |
| 画像 | **本人が渡した写真を最優先し、関連する写真はなるべく全部使う。** 必ず base64 で埋め込み、相対パスも外部URLも使わない |
| 1記事のサイズ | 通常は **400KB以内**。複数写真のフォトストーリーは **1.5MB以内** |
| 見せ方 | 文章を少なく、写真・コード風パネル・図解・控えめなアニメーションを多めにする |
| 更新ペース | 毎朝AIが下書きを作る。気が向いたときにOKを出す |
| 匿名 | 通常は本名・顔・勤務先・学校名を出さない。ただし、本人がその素材の掲載を明示した場合は、その指定範囲だけ使用してよい |

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
| 2026.08.27 | [👥 The Cultural Gap I Felt Working in Japan and the Philippines](works/japan-philippines-work/index.html) | 178 words · 59 sec |
| 2026.08.27 | [🛒 The Difference in Store Staffing Between Japan and the Philippines](works/japan-philippines-shops/index.html) | 167 words · 56 sec |
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
    毎朝 6:00   AIが昨日ぶんを全部読んで、15秒記事を作る（最大3本）
                 → staging/works/<slug>/ に置いて push
                    ↓
      あきくん   本番前のURLをスマホで開いて、気が向いたときに眺める
                 「これ出して」「ここ直して」と口で言う
                    ↓
                言われたときだけ staging/works/ → works/ へ移して push → 公開
```

**承認ボタンのようなものは作らない。** 👍を押す作業が増えるだけなので、
2026-09-02 に本人がその案を却下した。**押す作業を増やさないこと。**

### 🚦 STAGING と PUBLIC

いま見ているのが本番前か本番か、**記事の右上に必ず出る。**

| | 意味 | 場所 |
|---|---|---|
| 🟡 **STAGING** | 本番前。URLを知っている人だけ。検索には出ない | `staging/works/` |
| 🟢 **PUBLIC** | 世界に公開されている | `works/` |

公開するときに `STAGING` → `PUBLIC` に書き換える。

### スケジュールタスク

| taskId | 時刻 | 何をするか |
|---|---|---|
| `blog-morning-cook` | 毎朝 6:00 | Slack12chを読む → `staging/works/` に記事を作る。**本番（works/）には触らない** |

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
├── NEXT.md        📋 次にやること。続きをやる人はまずここ
├── assets/
│   └── thumbs-src/   一覧サムネの元画像（生成物）。埋め込みに使う原本
├── tools/
│   ├── embed.py      記事の画像を縮小して base64 で埋め込む
│   ├── thumbs.py     一覧サムネを240px正方形の画像ファイルにする
│   ├── build-site.py ⭐ トップを生成する（本番と本番前の両方）
│   └── check.py      納品チェック（サイズ・words・ラベル・動き・SOURCE MAP）
├── _template/
│   ├── index.html    記事のひな形（部品とモーションキットが全部入っている）
│   └── source.md     素材の書き込みフォーマット
├── staging/       本番前。gitに乗る（URLを知っている人だけ・検索には出ない）
│   ├── index.html         🟡 本番前（記事）の一覧。build-site.py の生成物
│   ├── works/<slug>/      🟡 本番前の記事そのもの
│   └── prototype-home.html 🔵 本番前（見た目）。次のトップの試作。手で書いている
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
□ 通常記事は400KB以内、複数写真のフォトストーリーは1.5MB以内か
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
- 本名・顔写真・勤務先・学校名・健康や収入の話は、本人の明示的な掲載指示がない限り載せない。
  明示された場合も、その素材と指定範囲を越えて個人情報を追加しない
- **フレームワーク・npm・ビルドを足さない**（素のHTML/CSS だけ）
  JavaScriptは、モーションキットの IntersectionObserver だけ許可。外部ライブラリは禁止
- `prefers-reduced-motion` のブロックを消さない
- **トップページ（index.html）を手で編集しない。**`python3 tools/build-site.py` で生成する
  （2026-09-02 に ChatGPT側とClaude側で実際に衝突した。生成方式にして解決した）

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
