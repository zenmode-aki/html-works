# 📋 次にやること（Codex / ChatGPT への引き継ぎ）

最終更新：2026-09-02（Claude側の作業ぶん）

**このファイルを最初に読んでください。** 続きの作業に必要なことは全部ここにあります。
ルールそのものは [PROMPT.md](PROMPT.md) と [README.md](README.md) にあります。

---

## 1. いまどうなっているか

### 2段階になりました

| | URL | 中身 |
|---|---|---|
| 🟢 **本番** | https://zenmode-aki.github.io/html-works/ | `works/` の11本 |
| 🟡 **本番前** | https://zenmode-aki.github.io/html-works/staging/ | `staging/works/` の7本 |

**同じリポジトリ・同じブランチ（main）です。** ChatGPT/Codex も Claude も、
main に commit & push するだけ。ブランチを分ける必要はありません。

本番前は `robots.txt` と `noindex` で検索から外してあります。
本番トップからリンクもしていないので、URLを知っている人しか来ません。

### 記事は「移動するだけ」で本番に出せます

記事は `../../index.html` で自分のトップに戻る作りなので、階層が同じなら
中身を1文字も直さずに移動できます。

```
staging/works/<slug>/  →  works/<slug>/     これだけで本番に出る
```

移動したあとにやることは3つ：
1. 記事の中の `stage-staging` → `stage-public`、表示も `STAGING` → `PUBLIC`
2. `<meta name="robots" content="noindex, nofollow" />` の行を消す
3. `python3 tools/build-site.py`

### ⚠️ トップページ（index.html）は手で編集しないでください

`works/<slug>/meta.json` から**生成**します。

```bash
python3 tools/build-site.py     # index.html と staging/index.html を作り直す
```

2026-09-02 に実際に衝突が起きました（ChatGPT側とClaude側が同じ日に index.html を
触った）。base64 を埋め込むのをやめて 244KB → 12KB にしたので、いまは
「生成し直す」だけで解決します。**この方式を崩さないでください。**

### 道具

```bash
python3 tools/check.py              # 本番の記事を検査
python3 tools/check.py --staging    # 本番前の記事を検査
python3 tools/check.py --fix-badge  # ワード数バッジを直す
python3 tools/build-site.py         # トップを両方つくり直す
python3 tools/thumbs.py             # assets/thumbs-src/ → assets/thumbs/（macOS専用）
python3 tools/embed.py <slug>       # 記事の中の画像を base64 で埋め込む
./local.sh                          # ローカルでサーバを立てて本番前を開く
```

**push する前に必ず `python3 tools/check.py` と `--staging` の両方を通すこと。**

---

## 2. すぐやってほしいこと（優先順）

### ① 名古屋駅の記事に写真を入れる 🔴

`staging/works/nagoya-station-bookshop/` には、いま**写真が入っていません**。

あきくんが Slack #サプライズ雑談 に貼った本屋（三省堂書店）の店内写真を
使いたいのですが、**Slackのファイルは認証が要るので自動で取れませんでした。**

やること：
1. あきくんから画像をもらう（Slackから保存してもらう）
2. `staging/works/nagoya-station-bookshop/images/sanseido.png` に置く
3. 記事の `<h1>` の直後に写真を戻す：

```html
  <figure class="photo">
    <img src="IMAGE:sanseido.png" alt="A wide bookshop floor with long low shelves of magazines and books" />
    <figcaption>📚 The eighth floor. Nobody is in a hurry here.</figcaption>
  </figure>
```

4. `python3 tools/embed.py` は `works/` しか見ないので、**staging 用に対応させるか**、
   一時的に `works/` へ移してから戻すこと（`tools/embed.py:57` の `ROOT / "works"`）

> 恒久対策：Slack画像を自動で取る方法を決める必要があります。
> 候補は「あきくんが Slack に貼るときに、同時に Google Drive にも入れる」
> （Drive の MCP は繋がっていて読める）。

### ② 記事の中にも画像を足す 🟡

いま画像は**一覧のサムネだけ**です。あきくんの希望は
**「1記事に最低1枚は本文にも画像を入れたい」**。

- Higgsfield（`generate_image`、model `recraft_v4_1`）で作る。**クレジットは気にしなくていい**
- ルールは [PROMPT.md](PROMPT.md) の「画像を生成するときの世界観」
  - 人間を出さない／末尾に `No humans, no text, no lettering.`
  - **直近3記事と同じ「動物 × 質感」を使わない**（`source.md` の「使った組み合わせ」を見る）
- 本文の画像は `images/` に置いて `IMAGE:xxx.jpg` と書き、`tools/embed.py` で base64 に
  （記事の中の画像は base64 のままにする。トップのサムネだけがファイル参照）

**いま使った組み合わせ（重複させない）**

```
本番: owl×clay / octopus×felt / capybara×plush / duck×cut-paper /
      squirrel×amigurumi / hedgehog×wet-clay / kitten×low-poly /
      otter×stained-glass / parakeet×bento / sloth×matte-plastic / turtle×amigurumi
本番前: mouse×carved-wood / bear×papier-mache / rabbit×porcelain /
        frog×blown-glass / snail×pressed-flowers / fox×wire / panda×needle-felt
```

まだ使っていない質感：マジパン、砂、木彫り彩色、ステンシル、刺し子、陶器の絵付け、
レゴ風ブロック、フェルトボール、羊毛のドライフラワー など。

### ③ ペンゲッソのプロトタイプに、本番前の記事を出す 🟡

`staging/prototype-home.html` が新しいトップページの試作です
（スロット・検索・地図・ペンゲッソ紹介が入っている）。

**いまは記事リストが JavaScript にベタ書き**（`var POSTS = [...]`）なので、
実際の記事と連動していません。あきくんの希望は
**「ここに本番前の記事を載せたい」**。

やり方の案：
- `tools/build-site.py` に「プロトタイプ用の JSON も吐く」処理を足す
  → `staging/posts.json` を作って、プロトタイプが `fetch()` で読む
- `meta.json` には `place` と `age` が入っているので、地図と年齢の絞り込みに使える
- ⚠️ `file://` で開くと `fetch()` は失敗するので、`./local.sh`（HTTPサーバ）前提にするか、
  JSONをHTMLに埋め込む形にする

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

- **`reply` はペンゲッソの返事。**ここでボケられる
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

- [ ] **`promote.sh` / `demote.sh`** — 本番前↔本番の移動を1コマンドに
      （いまは手作業：フォルダ移動 → バッジ → noindex削除 → build-site.py → check.py）
- [ ] **GitHub Actions** — push のたびに `check.py` を自動で走らせる。
      `build-site.py` を走らせて `git diff --exit-code` でトップの作り忘れも検出する。
      ⚠️ `sips` は Ubuntu に無いので `thumbs.py` は CI で走らせないこと
- [ ] **`check.py --site`** — 不変条件の検査
      （`works/` は全部 PUBLIC、`staging/works/` は全部 STAGING、
       本番トップが staging へリンクしていない、meta.json とサムネが揃っている）
- [ ] **毎朝のタスクの更新** — `~/.claude/scheduled-tasks/blog-morning-cook/SKILL.md` は
      まだ `drafts/` を見ています。`staging/works/` に書くよう直す必要があります
      （あきくんの希望：Claude と Codex の両方で、1日2回まわしたい）
- [ ] **README の古い記述** — `drafts/` の説明が残っています。`staging/` に直す
- [ ] **`_template/index.html`** — バッジがまだ `stage-local` / `LOCAL` です

---

## 5. 触ってはいけないもの

- **記事の `<p>` の中の英文。** あきくんの言葉です。AIが事実・体験・教訓を足さない
  （`card-label` / `.quip` / `h1` / 絵文字 / CSS / アニメは AI が自由に作っていい）
- **`tools/check.py` の `LEGACY` に入っている10本の本文**（2026-08 の「1分ブログ」時代）
- **トップページを手で編集すること**（必ず `build-site.py` で生成）
- **承認していないコメントをサイトに出すこと**
- **匿名ルール**：本名・顔・勤務先・学校名・健康状態・収入の額・家族の特定情報。
  迷ったら落とす。2026-09-02 は `#make-today-amazing` を丸ごと落としました
  （心療内科と大学の話が混ざっていたため）
- **承認ボタンのようなUIを足すこと**。2026-09-02 にあきくんが却下しています
  （「👍を押す作業が増えるだけでめんどくさい」）

---

## 6. あきくんが言っていたこと（判断に迷ったとき用）

- **このブログの本当の目的は「あとから自分が思い出すこと」。** 読者のためではない
- **SNSが怖い。**「いいねを押されるのがめちゃくちゃ怖い」。
  だから**いいね・フォロワー数・閲覧数のようなものは絶対に付けない**
- 何を喋るにも長くなるので、**15秒という制約をわざとかけている**
- 書いているのは**ペンゲッソというペンギン**。飼い主（あきくん）に向けて書いている設定。
  **ここはボケていい**
- 15秒は基本。**「これは1分で書いて」と言われたときだけ** 120〜180 words にする
- **画像生成のクレジットは気にしなくていい。**ただしフォーマット化した量産はいちばん嫌がる
