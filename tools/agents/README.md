# 🧑‍⚖️ 編集部のエージェント（Claude Code のサブエージェント定義・14本）

`CLAUDE.md` の「🔒 AIの絶対ルール」3（3体以上でディベートしてから決める）で使う役割の定義です。

- 2026-11-01 まで `~/vscode-html-15seconds/.claude/agents/` にだけあった（古い作業フォルダ。消すと失われるので、ここへ写した）。中のパスは本番 `/Users/akiezaki/Developer/html-works` に直してある
- **Claude Code で使うには、このフォルダの `.md` を `html-works/.claude/agents/` にコピーする**（`.claude/` は `.gitignore` に入っているので、手元の Mac ごとにコピーが要る）：

```bash
mkdir -p ~/Developer/html-works/.claude/agents && cp ~/Developer/html-works/tools/agents/pengesso-*.md ~/Developer/html-works/.claude/agents/
```

| ファイル | 役目 |
|---|---|
| `pengesso-editor-in-chief.md` | 🧑‍⚖️ 編集長。提案と反論を読み比べて、何を出すか決める |
| `pengesso-harsh-critic.md` | 🔥 遠慮なくダメ出し |
| `pengesso-keep-it-as-is.md` | 🙆 いまの形の良さを守る |
| `pengesso-contrarian.md` | 🔄 前提そのものを疑う |
| `pengesso-comedian.md` | 🤡 もっと笑えるか |
| `pengesso-rewriter-from-zero.md` | 🧱 ゼロから組み立て直す |
| `pengesso-constitution-checker.md` | 📜 ブログ憲法の番人 |
| `pengesso-primary-source-researcher.md` | 🔍 一次情報を当たる |
| `pengesso-ja-proofreader.md` | 日本語の校正 |
| `pengesso-translator.md` | 英訳（直訳のルール） |
| `pengesso-cover-artist.md` | 表紙（※ 2026-11-01 の新しい表紙のルールは `CLAUDE.md`「🖼 表紙」。こちらの定義は古い可能性がある） |
| `pengesso-ux-polisher.md` | UI/UX の実行係 |
| `pengesso-qa-verifier.md` | 検査 |
| `pengesso-publisher.md` | 公開の実行係 |
