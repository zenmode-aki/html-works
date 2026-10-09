# 👆 Add one "tap toy" to published articles (works/<slug>/index.html)

Repo: /home/user/html-works — a public blog ("15 Second Blog", penguin persona Pengesso). Smartphone first (iPhone ~390px).
The owner wants every article to have something you can TAP and play with (not just scroll). Most published articles have none.
Your job: for each slug in your list, add ONE small, themed, delightful tap toy that makes the article's idea or scene *felt*.

## The hard rule: NO WORDS
The site shows each page in 40 languages by swapping text nodes. New words would stay English in 39 languages.
So the toy must use ONLY emoji, digits, and symbols (→ × + = % ! ? / ✓ etc.). **No Latin/Japanese/any letters** in any visible text
you add, and none in aria-label/title/alt either (use emoji there, e.g. aria-label="🥚"). Class names / ids / JS are fine.
Numbers must be digits inside an element that has a class (e.g. <span class="toy-n">0</span>).

## Constitution (higher than everything)
Do not add facts, opinions, names, company/work details, or people. The toy only plays with what the article already says.
No human/person emoji (🏃 🙋 👩 🧑 👨 👍 👋 ✋ 💪 🤝 etc.), no romance, nothing scary, no clusters of many tiny holes/dots (owner has
trypophobia — e.g. no 🍓-seed grids, honeycomb, bubble clusters, dense dot grids). Smiley faces 😊 and animals/objects are OK.
If the article is about work (IT ops, office), keep the toy about generic objects only (☕ 📞 🖥️), never about the company.

## Ideas (vary the mechanic across your batch; pick what fits the article)
tap counter that fills a meter (🥚 ×120 → 🧺) · tap to cook/boil/grow (🥚→🍳) · before/after toggle (🌧️↔☀️) · tap to pop floating emoji ·
flip/reveal tiles · tiny slot/spinner of the article's things · stamp calendar (tap days ✓) · thermometer/stepper with + / − ·
map/route with dots you tap in order (few dots, not a grid) · reaction timer (⏱️ 0.42) · "feed the penguin" 🐧+🍜 · sort into 2 bins by tapping.
It should take 5–20 seconds, give immediate animated feedback (bounce, wiggle, fill, color), and have a clear end state (e.g. 🎉 + a
celebration via `if (window.pengessoPop) window.pengessoPop(x, y, ['🐧','✨','🥚'], 16)` with viewport px) and a reset button "↺".

## Where and how
- Insert ONE block inside <main>, right AFTER the last content `.card`/body content and BEFORE the "next" link (`<a class="next"`),
  the credit line, or the generated blocks (`<!-- ✨`, `<!-- 📚`, `part-nav`, `.post-bottom` …). Never inside generated blocks
  (anything between markers like `<!-- 🌐 i18n:start`…`end -->`, `<!-- ⬇️ OGP`, `<!-- 🏷 タグ`, `<!-- ✨`, `<!-- 📚`, `draft-nav`).
- Block shape:
  ```html
  <style>
  .toy{…scoped styles only, all selectors start with .toy…}
  </style>
  <section class="toy" aria-label="👆🥚">
    <div class="toy-kick" aria-hidden="true">👆</div>
    … your emoji/digit UI, buttons are <button type="button" class="toy-…" aria-label="🥚">🥚</button> …
  </section>
  <script>
  (function () { … vanilla JS, no libraries, no fetch … })();
  </script>
  ```
- Look: a bold colorful rounded panel matching the article's colors (read its :root CSS variables), thick fonts only
  (font-weight ≥ 700), buttons ≥ 48px tall/wide, emoji big (32–64px). Must not overflow at 360px width.
- Dark mode: for every light background you set, add `html[data-theme="dark"] .toy…` with a dark version.
- Motion: do NOT hide the toy initially (no opacity:0 reveal). Continuous animations must stop under
  `@media (prefers-reduced-motion: reduce) { html:not([data-motion="on"]) .toy … { animation:none } }` and `html[data-motion="off"] .toy … { animation:none }`.
  Taps may still change state instantly under reduced motion.
- Emoji-only elements: the site runtime has a rule `.emo-pop:not(.emo-inline){display:inline-block}` (specificity 0,2,0) that may
  override your display rules on elements whose only content is emoji. Do not show/hide emoji-only elements with `display`; use
  `visibility`, `opacity`, `hidden` on a wrapper with a class, or selectors with higher specificity (e.g. `.toy .toy-x.toy-x`).
- Don't use class names `.stage`, `.room`, `.now`, `.game`, `.card` for your toy.
- JS: wrap in an IIFE, `'use strict'` optional, guard every query. localStorage only inside try/catch with key prefix `pengesso-toy-<slug>-`.
  NEVER write the two characters `*` followed by `/` anywhere except to close a real comment (the site minifier strips comments; prefer `//` comments or none).
- Keep the rest of the page byte-for-byte unchanged.

## Check each article (must pass before you move on)
1. `python3 tools/check.py <slug>` → no new ❌ (compare with before you edited if needed).
2. Extract your script and `node --check` it.
3. Phone test (server already running at http://localhost:8765):
   `node /tmp/claude-0/-home-user-html-works/c6848cc4-4856-5650-8300-223a7a324c4c/scratchpad/mt/mtest-works.js <outdir in your own scratch folder> <slug>`
   → JSON line: overflow false, errors [], buttons ≥1, small [] (all ≥40px). It writes screenshots `<slug>-0..3.png` and `-ja.png`
   of the toy: LOOK at at least the -0 and -2 screenshots with the Read tool and fix anything ugly or broken.
4. `grep -n '[A-Za-z]' ` on your visible text should find nothing (only in class names/JS).

## Do NOT
run git, run tools/i18n.py, build-site.py, next-links.py, prev-links.py, draft.py, or edit any file except `works/<slug>/index.html`
for slugs in your list. Put your own helper files in a folder named after your batch inside
/tmp/claude-0/-home-user-html-works/c6848cc4-4856-5650-8300-223a7a324c4c/scratchpad/toys/ (other agents share the scratchpad).

## Report (final message, short)
For each slug: the toy in one line (emoji + mechanic), and test result OK / problem.

## Resume-safety (added)
- Finish and save ONE slug completely (edit + checks) before starting the next, so progress survives if you are stopped.
- Skip any slug whose works/<slug>/index.html already contains `class="toy"` (another run already did it).
- Keep your helper files only in your own subfolder of scratchpad/toys/<batch>/ (other agents share the scratchpad; never use bare names like build.py in the scratchpad root).
