# 📊 ペンゲッソの集計係（閲覧数・いいね・どの国から・いま読んでいる人）

記事の下の「👀 閲覧数・♡ いいね・🌏 国」と、トップの「🌍 世界の読者」の**数字の元**です。
Cloudflare Workers（無料）で動きます。**このフォルダを main に push すると、自動で公開されます**（`.github/workflows/deploy-stats.yml`）。

## 🤝 約束（画面の「この数字の数え方」にも同じことが書いてあります）

| 集める | 集めない |
|---|---|
| どの記事が・どの国から・どの言語で読まれたか | **IPアドレス**・ブラウザの名前・Cookie・名前・メール |
| いいね（ブラウザに置いたランダムなID。個人の情報なし） | 端末を追いかけるもの（フィンガープリントなど） |

- 同じ人が同じ記事を1日に何回読んでも **1回**（その日だけ使う“ごちゃまぜ値”で判定。1日たったら消える）
- 検索ロボットなどは数えない。「トラッキングしない」（Do Not Track）の人は数えない
- 運営者の端末は `?count=off` で数えなくできる
- **偽の数字は出しません。** つながっていない・まだ少ないときは、画面に何も出しません

## 🔌 つなぎかた（スマホでできます・約10分・無料）

### 1. Cloudflare の無料アカウントを作る
https://dash.cloudflare.com/sign-up （メールとパスワード。クレジットカードはいりません）

### 2. 名前を1つ決める（最初の1回だけ）
ダッシュボードの **Workers & Pages** を開くと、`○○○.workers.dev` の「○○○」を決める画面が出ます。好きな英数字でOK（例：`pengesso`）。

### 3. 合鍵（API トークン）を作る
1. 右上の人のアイコン → **My Profile** → **API Tokens** → **Create Token**
2. 「**Edit Cloudflare Workers**」の **Use template**
3. そのまま **Continue to summary** → **Create Token**
4. 出てきた長い文字列を**コピー**（**1回しか見られません**）

### 4. アカウントIDをコピーする
**Workers & Pages** の画面の右側にある **Account ID** をコピー。

### 5. GitHub に2つ登録する
https://github.com/zenmode-aki/html-works/settings/secrets/actions を開いて、**New repository secret** を2回：

| Name | Secret |
|---|---|
| `CLOUDFLARE_API_TOKEN` | 3 でコピーした文字列 |
| `CLOUDFLARE_ACCOUNT_ID` | 4 でコピーした Account ID |

### 6. 公開する
GitHub の **Actions** タブ → 左の **deploy-stats** → **Run workflow**。
緑のチェックが付いたら、ログの「つなぎ先」の行に `https://pengesso-stats.○○○.workers.dev` が出ます。

### 7. サイトにつなぐ
その URL を Claude に伝えるか、`assets/stats-config.json` を次のように直して push します：

```json
{ "enabled": true, "endpoint": "https://pengesso-stats.○○○.workers.dev", ... }
```

### 8. 自分のアクセスを数えない（大事）
**自分のスマホ・パソコンそれぞれで1回**、次のURLを開きます。自分が読んでも数字が増えなくなります。

`https://15-second-blog.com/?count=off`　（また数えたいときは `?count=on`）

## 🧪 見た目だけ先に見る
どのページでも URL の最後に `?pxdemo=1` を付けると、**「サンプル」と画面に出る**偽の数字で見た目を確認できます（本物の数字ではありません。本番の読者には出ません）。

## 💡 数字の見せかた（assets/stats-config.json）
- `minViews: 10` … 閲覧数は、10回を超えてから出す（数字が小さすぎる最初のうちは、かえって寂しく見えるため）
- `minLikes: 1` … いいねは1つから出す
- `minCountries: 3` … 国の数は、3か国から出す
- `minLive: 2` … 「いま読んでいる人」は、2人から出す

どれも**数字を盛るためではなく、小さすぎる数字を出さないための設定**です。0 にすれば、いつでも全部出ます。

## 🧰 手元でためす
```bash
cd stats-worker
npm install --no-save wrangler
npx wrangler dev --port 8799 --var DEV:1 --var DEV_COUNTRY:JP   # 手元のテスト用サーバー
node test/smoke.mjs                                             # 別のターミナルで。全部 ✅ なら正常
```
手元のページから試すとき：`http://localhost:8770/works/<記事>/index.html?pxstats=http://localhost:8799&pxmin=0`

## 🛟 困ったとき
| こうなった | こうする |
|---|---|
| Actions が `You need to register a workers.dev subdomain` で止まる | 上の **2.** をやる |
| `Authentication error` | トークンを作り直して `CLOUDFLARE_API_TOKEN` を入れ直す |
| 画面に何も出ない | `assets/stats-config.json` の `enabled` が `true` か／URL が合っているか／数字がしきい値より小さくないか |
| 無料の上限に達した | 集計係がエラーを返し、画面は数字を隠すだけ。サイトは壊れません。翌日に戻ります |

## 🏗 しくみ（エンジニア向け）
- `src/index.js` … Worker（入口。CORS・入力の確認・国の取り出し）＋ Durable Object `Stats`（SQLite。全部を1つの箱 `main` に入れるので、数がずれない）
- `POST /v1/hit` 数える ／ `POST /v1/ping` 読んでいる合図（45秒ごと）／ `POST /v1/like` いいね ／ `GET /v1/post?p=<slug>` ／ `GET /v1/stats` ／ `GET /v1/health`
- 書き込みは `ALLOWED_ORIGINS`（`wrangler.toml`）のブラウザだけ。1回線あたりの回数にも上限
- 画面側は `tools/px_runtime.js`（→ `assets/px.js`）。`tools/i18n.py` が全ページに入れる
