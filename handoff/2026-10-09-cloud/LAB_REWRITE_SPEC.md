# ✍️ Rewrite the "lab" articles (lab/<slug>/) — read fully before starting

Repo: /home/user/html-works — public blog "15 Second Blog" (penguin persona Pengesso writes for his owner).
These 306 articles were written too fast by AI from the owner's reading notes. The owner read them and said (2026-10-08):

> 「○○が言った」（オリバー・バークマンが言った、まこなり社長が言った…）は入れなくていい。エッセンスだけ。
> 日本語が変だし、分かりづらい。もう少しだけ長く、ちゃんと説明してほしい。もっと分かりやすい文章にしてほしい。

Your job: for each slug in your list, rewrite the article text so it is clear, natural and helpful, then update every file
so the page stays correct in Japanese, English and Korean. Quality over speed. One slug at a time, fully finished, then the next.

## Absolute rules (blog constitution — above everything)
1. Never write about the owner's company, job content, coworkers, clients. No work examples ("at work", "my boss", meetings,
   reports to a client…). Use everyday life: study, cafes, trains, friends, cooking, travel (Philippines/Korea/Malaysia),
   convenience stores, hobbies, rooms, sleep.
2. Don't hurt or mock anyone. No real private people. No romance.
3. **NO names of people or sources anywhere in the article**: no Oliver Burkeman, no 社長 / CEO / YouTuber names, no
   "Panda no Ondo", no book or blog titles, no famous people as authorities (Darwin, Poincaré, Franklin, Harvard study,
   "a researcher named…"). If a research finding is essential, say it softly and generically ("〜と言われています").
   Remove "Read the original (English)" links and any URL to the source.
4. Never invent facts about the owner's life ("昨日私は…"). Use "たとえば〜" hypotheticals instead.
5. Japanese: first person 「私」, standard Japanese (no Kansai), polite です/ます, warm and plain. No odd phrases,
   no literal-translation feel, no slangy "刺さった", no overuse of 体言止め, no word play that needs explaining.
6. No human/person emoji (🏃🙋👩🧑👨👍👋✋💪🤝 etc.). Objects, animals, 🐧, smiley faces are OK.

## What a good article looks like now
- One central message, said plainly in the title (h1). The title is a normal sentence, not a riddle.
- Body = **4–6 cards, 7–11 Japanese sentences, about 70–120 English words** (before it was 35–65 — make it a little
  longer by *explaining*, not padding). A good flow:
  1. よくある場面・悩み（読者が「あるある」と思う）
  2. 言いたいこと（本質）を、はっきり1文で
  3. なぜそうなのか（理由を、ちゃんと説明する。1〜2文）
  4. 身近なたとえ・例（「たとえば、〜」）
  5. 今日からできる小さなこと
  6. ひとことのまとめ（`<p class="big">` にしてよい）
- Each sentence short and clear (one idea per sentence). A middle-school student should understand it.
- card-label: 2–3 English words, unique in the article (e.g. "The Point", "Why", "For Example", "Try This").
  Every card keeps `.card-head` with `.card-emoji` + `.card-label`.
- Keep the existing mini game (the `<section class="game …">`) and its JS working. Only change game text if it names a
  person/source or no longer matches the new message. All words shown must stay static HTML (JS only toggles
  classes/data-attributes/digits) — same as before.
- Credit line at the bottom: replace whatever is there with exactly
  `<div class="credit">📚 I wrote this from my reading notes.</div>`  → ja `📚 読書メモをもとに書きました。`
  → ko `📚 독서 메모를 바탕으로 썼어요.`  Delete any "Read the original" link/button.

## Files to update per slug (lab/<slug>/)
1. `source.md`: rewrite the `## 素材` S-lines (S1…Sn = the new Japanese sentences, this is the master text),
   `## 中心メッセージ`. In `## 出どころ`, keep it short: 「本人の読書メモ（2026-10-05）から。2026-10-08 本人の指示で、人の名前・出典を消して書き直した。」
   Remove the original URL. Keep 触って遊べるもの / 表紙のプロンプト / 画像 sections as they are.
2. `index.html`:
   - `<h1>` (keep the floating emoji span if there is one), `<title>`, `<meta name="description">`/og description if present
     (they must be English and match the new h1/first sentence).
   - The body cards (English = literal translation of the Japanese: 1 Japanese sentence = 1 English sentence, same order,
     junior-high vocabulary, simple S-V-O, numbers as digits).
   - The SOURCE MAP comment at the end (S → card) and `追加した文：0`.
   - Do NOT touch anything between generated markers (`<!-- 🌐 i18n:start` … `i18n:end -->`, `<!-- 🧪 lab-…`,
     `<!-- 🏷 タグ`, `<!-- ⬇️ OGP`), the head/topbar structure, CSS of other parts, or the reduced-motion blocks — except:
     if you add a NEW class that starts hidden (opacity:0) you must add it to that page's reduced-motion selector lists
     like the existing ones. Easiest: reuse the existing `.card` markup so nothing new needs adding.
3. `meta.json`: `"title"` (= new English h1 without emoji), `"label"` (1–3 words) if it no longer fits, `"thumbAlt"` unchanged.
4. `i18n/ja.json`: `"title"` (Japanese title), `"label"`, and `"text"`: every English string on the page → Japanese.
   Body sentences' Japanese = your S-lines exactly. Remove keys whose English no longer exists on the page.
5. `i18n/ko.json`: same keys, Korean translated **from the English** (literal, 해요체, 저 for "I").

## Checks for each slug (all must pass before moving on)
- `python3 tools/i18n.py --lab --todo <slug> ja` → `[]`  and  `python3 tools/i18n.py --lab --todo <slug> ko` → `[]`
- `python3 tools/check.py --lab --fix-badge <slug>` → all ✅. Then make the `⚡ N SEC` in `.label` equal to the badge's sec.
- Grep the page + ja.json + ko.json for names: `grep -niE "burkeman|バークマン|버크먼|panda|パンダの温度|社長|darwin|ダーウィン|poincar|ポアンカレ|harvard|ハーバード|oliverburkeman" lab/<slug>/index.html lab/<slug>/i18n/ja.json lab/<slug>/i18n/ko.json lab/<slug>/source.md`
  → nothing (except inside generated i18n blocks you did not write — regenerate is done later by the orchestrator).
  (A panda as an animal in a game is fine, e.g. 🐼, but not the blog name.)
- Extract the inline script and run `node --check` on it if you touched the game.
- Phone test (server at http://localhost:8765 is running; if not, start `python3 -m http.server 8765` in the repo in the background):
  `node /tmp/claude-0/-home-user-html-works/c6848cc4-4856-5650-8300-223a7a324c4c/scratchpad/mt/mtest-lab.js <your scratch dir>/shots <slug>`
  → overflow false, errors []. (It loads the page as served; i18n data blocks are rebuilt later, so a Japanese
  screenshot may still show old Japanese — that is expected.)
- Read your Japanese S-lines once more as a reader: is it natural? is the reason explained? would a tired person
  understand it in one reading? If not, fix it.

## Do NOT
- run git, `tools/lab.py`, `tools/i18n.py` without `--todo`, build-site, or edit files outside `lab/<slug>/` for your slugs.
- change the slug or folder names, delete files, or touch other articles.
- Keep your own helper files in scratchpad/rewrite/<your batch>/ (other agents share the scratchpad; never use bare names
  in the scratchpad root).

## Resume-safety
- Finish ONE slug completely before the next. If `lab/<slug>/source.md` already contains `2026-10-08 本人の指示で`
  the slug was already rewritten by an earlier run — skip it.

## Report (final message, short)
A table: slug | new Japanese title | words/sec | OK or problem.

## Notes from the pilot (2026-10-08) — the pilot output is the reference
- GOOD EXAMPLES (read these first and match their quality and flow): lab/three-or-four-hours-is-enough, lab/just-say-oh-hi,
  lab/nothing-is-a-given (source.md S-lines + index.html). 6 cards, ~9 sentences, one `<p>` per sentence, last line `.big`.
- Word target: 80–130 English words.
- If the article also has translations in other languages (zh, es, …), leave those files alone (they are updated later).
- Swap any hand/person emoji you find (🙏 → 💛 etc.) everywhere it appears (h1 float, cards, game, JS pop lists).
- Never run git, not even `git checkout`. Keep a backup copy of the slug folder in your scratch folder before editing.
