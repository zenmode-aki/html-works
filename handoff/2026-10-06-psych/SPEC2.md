# Part 2 addendum (read after SPEC.md — everything in SPEC.md still applies)

- Notes file for part 2 = `NOTES2.md` (not NOTES.md). Plan = `PLAN2.md` (your batch only).
- The owner said: "本当にゆっくりでいいから質を優先して" — quality over speed. Write each article with care:
  re-read your Japanese S-lines aloud in your head: do they sound like a gentle, slightly funny penguin talking to a tired friend?
  Is the English literal and simple? Does the game make the idea *felt* in under 20 seconds of tapping?
- In source.md 出どころ, say the notes are the owner's second set of notes (「本人のメモ その2（未読だった375記事の学び）」の 番号 N).
- Emoji: no human/face-of-person emoji at all (🙅 🙆 🧑 👩 👨 🙋 💁 🤷 etc.). Use penguins 🐧, animals, objects, smiley faces 😊 are OK.
- Health topics (batch T etc.): "it is said" / "a study found", never "you must", no medical advice, no exact rules presented as advice.
  Keep the numbers from the notes only when they are about a study and phrased softly.
- Heavy topics (bullying, near breaking down): gentle, warm, no jokes about the pain, no "winning" game feel; a soft calming interaction.
  It is OK to add "It is also OK to talk to a professional." (as one of the S-lines in Japanese too).
- Sentences taken from NOTES2 should be rewritten in the owner's voice, not copied. Never mention the original blog author's family.
- Before you finish each article: run the two commands and make sure `--todo` prints [] and check is ✅ except IMAGE:cover.jpg.
- If you build a generator script to make many files, put it in the scratchpad folder (next to this spec), not in the repo.

## Lessons from earlier batches (MUST follow)
- Add "DRAFT": "下書き" is no longer needed (it is now in the shared ui.ja.json). Harmless if present.
- The site runtime's emoji-pop CSS `.emo-pop:not(.emo-inline){display:inline-block}` (specificity 0,2,0) overrides weaker display rules on emoji-only elements.
  Never show/hide an emoji-only element with display; wrap it in a span with a class, or use selectors like `.game .x` with higher specificity. Same for .vs chips.
- Don't use class names `.stage` (draft badge, nowrap), `.room`, `.now` in your page.
- WebKit: `backface-visibility` flips can show the back mirrored — swap faces at mid-flip. 🌫️ looks like a gray square on iPhone; avoid.
- You may run the iPhone test: `cd P && node mtest.js shots/<batch> <slugs…>` (local server already running at :8765; needs dangerouslyDisableSandbox). It is read-only.
- Do not run git (not even git status).
Credit for NOTES3 (W X Y Z): "📚 I wrote this from my notes on books and blogs I have read." / 「📚 私が読んだ本やブログのメモから書きました。」
- FLIP CARDS (verified bug on iPhone WebKit: backs show MIRRORED through the front). If you use rotateY/rotateX flips, ALWAYS add a visibility swap:
  `.game .card-x .back { visibility:hidden; transition: transform .2s, visibility 0s linear .2s; } .game .card-x.open .back { visibility:visible; }`
  `.game .card-x .front { transition: transform .2s, visibility 0s linear .2s; } .game .card-x.open .front { visibility:hidden; }`
  Check with P/fliptest.js: `node fliptest.js shots/x <slug>=<card selector>` and look at the screenshot.
