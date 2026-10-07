# 🐼 "Happy psychology" draft series — build spec (read fully before writing)

Repo: /Users/ezakimasaaki/Desktop/html-works  (public blog "15 Second Blog" by a penguin persona, ペンゲッソ)
You create NEW DRAFT articles in `draft/<slug>/`. Each article = one small idea, readable in ~15–20 seconds,
with ONE playful tap interaction (mini game). Smartphone first (iPhone ~390px wide).

The owner pasted their study notes on a Japanese psychology blog ("パンダの温度（しあわせ心理学）").
Notes file: `NOTES.md` (same folder as this spec). Your assigned articles are listed in `PLAN.md` (your batch only).
The owner said: rewrite in my voice, split a lot (15-second blog), cute & funny, for days when you have no energy,
make each article interactive (tap → something changes, game feel), smartphone first. General talk is fine;
use the owner's world for examples only if natural — don't force it.

## Golden reference — copy its structure
`draft/say-yes-in-a-flash/` (index.html, source.md, meta.json, i18n/ja.json). It passes all checks and was tested on iPhone.
Copy its <head>/CSS skeleton (topbar, label, h1, photo, cards, game, credit, next, motion kit, reduced-motion,
dark mode lines) and change colors/game per article. Read it completely before starting.

## Absolute content rules (blog constitution — higher than everything)
1. NEVER write about the owner's company, job content, workplace, coworkers, clients. No work examples at all
   (generic "a boss" in a neutral example is OK; never "at my job…").
2. Don't hurt or mock anyone. No real private people. Generic names only when needed (Tanaka-san etc.) — prefer none.
3. NO romance at all (the persona never does romance; no hinting). Skip any dating/couple content.
4. Do NOT reuse the original blogger's personal anecdotes (things like "the author's son…", "the author's wife…",
   "the author chipped a tooth", "the author's acquaintance…"). They are someone else's life. Turn them into general
   or hypothetical examples ("For example, if…") or drop them.
5. Never invent facts about the owner's life ("Yesterday I…", "My boss said…"). Hypothetical "for example" is fine.
   Owner context you MAY use for hypothetical examples: studied English at language schools in the Philippines
   (Baguio, Clark), travels (Korea, Malaysia, Thailand), lives around Nagoya, Japan, loves productivity books
   (Oliver Burkeman), self-described perfectionist, studies Google Cloud, likes coffee shops, baseball in Korea.
   Use these lightly; most examples can just be everyday life (convenience store, train, friends, cafe, school).
6. Don't attribute quotes to living celebrities (e.g. Tamori). Say the idea in general words instead.
   Established research is fine if stated carefully ("a study found…", "Benjamin Franklin…", "Robert Axelrod's
   computer tournament", "Adam Grant's research", "Richard Wiseman's research on luck", "the Harvard study of adult
   development", "mere exposure effect"). No medical/financial advice; health tips are soft ("it is said…").
7. First person in Japanese is 「私」 (never 僕). Standard Japanese (no Kansai dialect). Polite-casual です/ます like
   the reference. Cute, light, a little funny.

## Text rules
- source.md: Japanese "素材" sentences S1…Sn written in the owner's voice (this is the master text).
  Note in 出どころ that the AI rewrote the owner's notes on the owner's instruction (copy the reference wording,
  change the section number). End with `追加した文：0`.
- Body English = literal, 1 Japanese sentence = 1 English sentence, same order, junior-high vocabulary (Eiken 3),
  simple S-V-O sentences, numbers as digits ("2 seconds", "3rd"). Not fancy English.
- Length: body (<p> text inside .card) **35–65 English words** total (≈12–22 sec). 3–5 cards, 1–2 sentences each.
  One central message per article. The last or key line may use `<p class="big">`.
- h1 title = plain descriptive sentence saying the point (no question, no pun), 6–14 words. Japanese title in ja.json.
- card-label: exactly 2–3 English words, unique within article, summarizing the card (e.g. "The Rule", "Try This").
  Every .card with a <p> needs .card-head with .card-emoji + .card-label.
- Every English text node on the page (labels, game UI, buttons, results, credit) MUST have a Japanese entry in
  `i18n/ja.json` ("title", "label", "text": {english: japanese}). The Japanese for body sentences = the source.md S-lines.
- Credit line (exact): `<div class="credit">📚 I learned this from the Japanese blog "Panda no Ondo".</div>`
  → ja: `📚 日本のブログ「パンダの温度」で知りました。`
- SOURCE MAP comment at the very end of index.html exactly like the reference (each S → card, `追加した文：0`).
- Label line: `<div class="label"><span class="topic">🐧 EVERYDAY LIFE</span>⚡ N SEC</div>` where N = the sec on the badge.

## The interaction (the most important part — make it delightful)
- One `<section class="game …">` per article, placed between cards (usually after card 2 or 3), styled as a bold
  colorful panel (gradient, big rounded corners). Kicker "⚡ TRY IT" (ja "⚡ やってみよう") + a short title.
- Must be themed to the article's idea and make the idea *felt*. Tap-first: buttons ≥ 48px tall, big friendly.
  Immediate visible feedback with animation (bounce, flip, fill, shake, color change, emoji change), a clear end state
  ("result" message), and a reset/try-again button. Light game feel: score, meter, stars, level, timer, combo.
- Vary mechanics across your batch — don't repeat the same mechanic twice in your batch. Menu:
  reaction timer · tap-to-fill meter · flip cards / reveal · 2–3 choice quiz with reactions · before/after toggle ·
  tap-to-sort into two bins · clicker/combo counter · spinner/roulette · guided timer/breathing · +/- stepper calculator
  (no keyboard input) · "pop the bad thoughts" bubbles · stamp calendar · slot/shuffle · pick-a-card · level ladder.
  Avoid drag-only interactions; avoid text inputs (keyboard covers the screen on phones).
- **i18n rule:** ALL words shown must be static HTML. JS may only change classes / data-attributes / hidden /
  style / emoji characters / numbers (digits only, inside an element that has a class). Show/hide prepared message
  elements with CSS based on data-* state (see `.game[data-s=…]` in the reference). Never build sentences in JS.
  Elements WITHOUT class/id (b, i, span, em, strong) are merged into the parent sentence for translation — give a
  class to any span you need translated separately, or to number spans.
- Celebrate with `if (window.pengessoPop) window.pengessoPop(x, y, ['🐧','✨',…], 16)` (x,y = viewport px).
  Use penguin/objects emoji, no human-face emoji (🙋 etc.).
- localStorage only inside try/catch, key prefix `pengesso-<slug>-`.
- No external libraries, no fetch, no iframes. Vanilla JS inside `<script>` at end of body, wrapped in an IIFE.
- Motion: `.js .game` starts hidden like cards; add `.game` to BOTH reduced-motion selector lists (like reference).
  Continuous animations must stop under reduced motion (the reference's global block already does that).
- Dark mode: for every light/white background you add, add a `html[data-theme="dark"] …` rule.
- No horizontal overflow at 375px. Test mentally: long Japanese strings must wrap (no `white-space:nowrap` on text).

## Visual design
- Each article: its own color palette (pop/bright — these topics are "serious" so show them POP). Thick fonts only
  (font-weight ≥ 700; never thin). Use emoji, CSS diagrams, comparison chips (.vs), timelines where helpful.
- Cover: keep `<figure class="photo"><img src="IMAGE:cover.jpg" alt="…English description…" /></figure>` right after h1.
  The orchestrator generates the image later from your prompt. (check.py will report IMAGE:cover.jpg missing — that's expected.)

## Files per article (draft/<slug>/)
- Create with: `python3 tools/draft.py new <slug>` (creates folder from template), then overwrite files.
- index.html, source.md (incl. `## 触って遊べるもの` describing the game, and `## 表紙のプロンプト` with ONE English
  image prompt), meta.json, i18n/ja.json.
- meta.json: like the reference; use the seq given in PLAN.md; "date": "2026-10-05"; "series": "happy-psychology";
  "mood": ["lift"] (+ optionally one of "think","laugh","energy","learn"); "tags": ["psychology", + 1–3 of:
  friends, feelings, mindset, happiness, productivity, money, sleep, health, rest, tips, books, fitness, walking,
  study, mistakes, school, english, family]; "room": "head"; "topic": "life"; "place": "nagoya";
  "label": 1–3 word English short label; "thumbAlt" = same as cover alt.
- 🆕 2026-10-07 COVER DESIGN CHANGED: covers are no longer AI-generated. Run `python3 tools/cover/make-cover.py <slug> <one emoji> '<accent hex>' [--flip]` (the real Pengesso plush + a thought bubble with one Fluent 3D emoji). The old prompt rules below are kept only for reference.
- (old) Cover prompt rules: hero is an "extremely cute, chubby round penguin" with gentle face and plain belly (no rings or
  patterns on belly, never pink penguin), texture = choose a different one per article from: soft felted wool, plush toy
  corduroy and felt, crocheted amigurumi yarn, matte plastic model kit, low-poly 3D wood and paper, layered cut paper
  diorama, hand-embroidered felt, brushed mohair, chenille yarn, boucle wool, alpaca wool. Include ONE realistic object
  that shows the topic. Bright simple background with depth (no clutter, no repeated small objects/holes/grids — the
  owner has trypophobia; no glass/stained glass; no scary; if a computer appears it's a Mac). End with:
  "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered
  composition. No humans, no text, no lettering."

## Commands you may run (ONLY these; you share the repo with other agents working in parallel)
- `python3 tools/draft.py new <slug>`
- `python3 tools/i18n.py --draft --todo <slug>` → must print `[]` (every string translated). Read-only.
- `python3 tools/check.py --draft --fix-badge <slug>` → everything ✅ except the IMAGE:cover.jpg line.
  (--fix-badge writes the word badge; then update the "⚡ N SEC" label to match.)
- `node -e` / python one-off syntax checks of your inline JS are fine (e.g. extract the script and run `node --check`).
- DO NOT run: git anything, `tools/draft.py build`, `tools/i18n.py` without --todo, build-site, or touch files outside
  your own draft/<slug>/ folders. Do not edit tools/ or other articles.

## Report back (final message)
For each slug: title (en + ja), word count/sec, the game in one line, the cover prompt is in source.md (yes/no),
todo=[] (yes/no), check OK except cover (yes/no). Mention anything you were unsure about (constitution, facts).
