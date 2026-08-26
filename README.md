# 🐧 1 Minute Blog

**1分以内で読める、かんたんな英語のHTML記事を置くところ。**

ビルドもCMSもログインも要らない。HTMLを1枚書いて、push するだけ。

🌏 **公開URL** → https://zenmode-aki.github.io/html-works/

---

## 🎯 決めごと

| | |
|---|---|
| 言語 | **英語のみ。** 日本語版は作らない（素材の日本語は `source.md` に残す） |
| 長さ | 本文 **120〜180 words**（180 words ≒ 60秒） |
| 長さの表示 | ページ上部に `⏱ 163 words · 54 sec read` を出す |
| 画像 | **必ず base64 で埋め込む。** 相対パスも外部URLも使わない |
| 1記事のサイズ | **400KB以内**（幅1200px・quality 72 に縮小してから埋め込む） |
| 更新ペース | 気づいたときに。溜まってからでいい |
| 匿名 | 本名・顔・勤務先・学校名は出さない |

---

## 📚 作品

| 日付 | タイトル | 長さ |
|---|---|---|
| 2026.08.26 | [📤 Input Metabo #3: Only Output Makes Life Roll](works/input-metabo-3/index.html) | 144 words · 48 sec |
| 2026.08.26 | [🔎 Input Metabo #2: I Looked for the Correct Answer](works/input-metabo-2/index.html) | 139 words · 46 sec |
| 2026.08.26 | [🎧 Input Metabo #1: I Knew More. I Moved Less.](works/input-metabo-1/index.html) | 146 words · 49 sec |
| 2026.08.26 | [⚾ I Played Pawapuro Again After a Long Time! 🎮](works/pawapuro/index.html) | 163 words · 54 sec |

---

## ✍️ 1本ふやす手順

```bash
cd ~/Desktop/html-works && ./new-post.sh nagoya-dome
```

1. **日本語を `works/nagoya-dome/source.md` に貼る**（音声入力そのまま。`S1.` `S2.` と番号を振る）
2. **[PROMPT.md](PROMPT.md) をAIに貼って、素材を渡す** → `index.html` を書いてもらう
3. **写真を `works/nagoya-dome/images/` に入れる**。HTMLには `src="IMAGE:photo.jpg"` と書いておく

```bash
python3 tools/embed.py nagoya-dome   # 縮小して base64 で埋め込む
python3 tools/check.py  nagoya-dome  # 「追加した文：0」を確認する
```

4. トップの `index.html` に作品カードを1つ足す（ブロックをコピーするだけ）
5. `git add -A && git commit -m "add nagoya-dome" && git push`

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

30本でも約9MB。GitHub Pages のソフト上限は1GB なので余裕がある。

手で縮小したいとき：

```bash
sips -Z 1200 --setProperty formatOptions 72 photo.jpg -o photo-small.jpg
```

---

## 🧰 中身

```
html-works/
├── index.html        トップページ（作品一覧）
├── PROMPT.md      ⭐ AIに渡すマスタープロンプト。記事を作るときはこれを貼る
├── new-post.sh       ./new-post.sh <slug> で1本生える
├── tools/
│   ├── embed.py      画像を縮小して base64 で埋め込む
│   └── check.py      納品チェック（サイズ・words・バッジ・SOURCE MAP）
├── _template/
│   ├── index.html    記事のひな形（部品が全部入っている）
│   └── source.md     素材の書き込みフォーマット
└── works/
    └── pawapuro/
        ├── index.html
        ├── source.md
        └── images/
```

### 🧩 使える部品はこれだけ

```
.wc-badge      ⏱ 163 words · 54 sec read   ← 上部。読者への親切であり、AIへの歯止め
.home          ← Back to all works
.label         ⚾ 1 MINUTE BLOG 🎮
h1             タイトル（絵文字つき）
.photo         写真（角丸・影・わずかに傾く）
.card          本文カード ← 主役。1枚に2〜4文まで
  └ .section-emoji  カードの頭の絵文字タイル
  └ .big            オチの一言（大きい文字）
.timeline      段階を見せるとき（色が自動で変わる）
.youtube-card  動画へのリンク（iframeにしない）
```

**新しい記事を作るときにやること**：`.card` をコピーして中身を差し替えるだけ。**CSSは触らなくていい。**

---

## ✅ push する前に

```bash
python3 tools/check.py
```

これが通れば push していい。見るのは6つ。

```
□ 400KB以内か
□ 画像がすべて base64 か（リンク切れの余地がないか）
□ 本文が 120〜180 words か
□ バッジの数字が本文と合っているか   ← --fix-badge で自動で直せる
□ 追加した文：0 になっているか       ← ここだけ見ればいい
□ source.md があるか
```

---

## ⛔ 触ってはいけないもの

- **記事の英文は本人のもの。AIが本文を創作・代筆しない。** 骨組み・見出し・直訳の手伝いまで
- 本名・顔写真・勤務先・学校名・健康や収入の話は載せない（**匿名でやると決めている**）
- フレームワーク・npm・ビルドを足さない（素のHTML/CSS だけ）

> 「普通に文章で書くとなんかちょっとだけしんどい気分になるんだけど、
> HTMLで書くってなると、比較的、自分の文章に嫌気がしないなと思ってて。」（2026年8月1日）

便利にしようとしてCMSを足すと、この体験が壊れる。**素のHTMLのままにしておくこと。**

---

## 🧱 手が止まったときに読むところ

> 「いま、このブログを書く目的は、自分と友達になりたいって思ってもらえる人を世界から探し出すこと。
> ということは基準は、完璧なブログサイトよりも、汚くても雑でもちゃんと情報があって、
> 読んでて面白いかが大事なのかも。そんなに正確にジャッジされないからさ」

書きたいネタのリスト → `aki-context/06_blog-concept.md`

---

## 🔀 `pengesso` との違い

`aki-os/projects/pengesso`（非公開）には、日本語＋英語の記事が10本ある。あちらは触っていない。

| | **html-works（ここ）** | pengesso |
|---|---|---|
| 長さ | 1分・120〜180 words | 長さ自由 |
| 言語 | 英語のみ | 日本語＋英語の切替 |
| 画像 | base64で自己完結 | `assets/img/` に相対パス |
| 公開 | GitHub Pages（無料・公開リポジトリ） | Vercel（非公開リポジトリのため） |
| 速さ | **気づいたら即出す** | ちゃんと書く |
