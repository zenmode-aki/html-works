# このフォルダで AI が守ること（15秒の勉強ノート）

勉強中のことを、15秒（長くても30秒）で読めるようにメモしておくサイト。
公開先は **https://15-second-blog.com/study/**（html-works リポジトリの `study/` フォルダ。2026-11-03 から）。
aki-os の `projects/html-works/study/` にも同じものを置く（あとで html-works を片づけるため、aki-os に全部そろえておく）。

## 絶対に守ること

1. **名前（あっきー など）をサイトに書かない**（2026-11-03 本人）
2. **絵文字を使わない**（本人：「雑すぎるから」）。飾りは `images/icons/` のアイコン・タグ・色で
3. 書かないこと：会社・案件・お客さんにつながる情報／家族やパートナーの話／お金の具体的な金額／住んでいる場所がわかる情報／投資の「買い・売り」の判断／健康についての断定
4. **記事の本文は本人の言葉から作る。** 本人が書いていないネタを AI が勝手に記事にしない（2026-11-03 本人が ping の記事を「僕の文章じゃない」と消した）
5. 画像は base64 で埋め込まない。`images/` に別ファイルで置く

## トップの形

- 「IT」「自制心」「その他・興味あること（ふだんは閉じてある）」の3つの箱だけ。目次・章立ては作らない
- 分野は小さい丸いタグ。メモがある分野のタグには `on` クラスを足す
- IT の中の「AI」は押すと Anthropic・OpenAI・Google が開く
- 見た目は15秒ブログ（ペンゲッソの色：紺・青・黄・クリーム）に寄せる

## ことば（日本語・English・한국어）

- 右上のボタンで切りかわる。しくみは `assets/site.js` の `I18N`
- トップの文：HTML には日本語を書いて `data-i18n="キー"` を付け、`I18N.en` と `I18N.ko` に訳を足す
- 記事の本文：`<div class="i18n" lang="ja">…</div>`、`lang="en"`、`lang="ko"` の3つを並べる
- 日本語は関西弁。英語・韓国語はやさしい普通の言い方で

## 記事の追加手順

1. 本人がテーマと中身を言う（声のメモのこともある）
2. AI が `posts/<分野>-<英語の短い名前>.html` を作る（3か国語・15〜30秒・共通フッター `<footer id="common-footer" data-root="../"></footer>` と `<script src="../assets/site.js"></script>`）
3. AI が `index.html` のその箱の `<!-- POSTS:IT -->`（`POSTS:SELF` / `POSTS:OTHERS`）の下に `<li><a href="posts/…"><time>11/3</time><b>題</b><span class="sec">15秒</span></a></li>` を足し、「まだメモはないで。」の行を消す。タグに `on` を足す
4. 本人が見て OK なら、確認を取ってから commit・push（html-works と aki-os の両方）

分野の英語名（ファイル名用）：aws・gcp・docker・network・security・uiux・dev・salesforce・microsoft・ai-anthropic・ai-openai・ai-google・breath・money・brain・book・english・training

## フォルダ

- `index.html` … トップ
- `posts/` … 記事（1本＝1ファイル）。空のページは作らない
- `images/` … ロゴ（`logo-*.webp`）、ペンゲッソ（`pengesso.webp`）、箱のイラスト（`section-*.svg`）
- `images/icons/` … タグの小さいアイコン（Higgsfield の Recraft で作った SVG）
- `assets/style.css` … 共通の見た目／`assets/site.js` … 設定（URL）・ことば・共通フッター
