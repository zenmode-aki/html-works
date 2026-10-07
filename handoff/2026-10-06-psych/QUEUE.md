# 🌙 Overnight run (2026-10-05 night). The user is ASLEEP and said: never ask questions, never stop, keep going after compaction.
# Agent limit = 20 concurrent. Launch the next waiting batch whenever an agent completes.
# Prompt template: "Read P/SPEC.md, P/SPEC2.md, P/<NOTES>, P/<PLAN> (your batch only), and draft/say-yes-in-a-flash/. Build all articles of Batch X..."
running wave1: A–K (PLAN.md + NOTES.md)
running wave2: L M N O P Q R S T (PLAN2.md + NOTES2.md)
launched later: U(resumed) V W
waiting (in this order):
  (U V done-launched)
  X Y Z    → PLAN3.md + NOTES3.md
  BK1 BK2 BK3 BK4 → PLAN4.md + NOTES4.md (Burkeman: its own header rules in PLAN4.md override credit/series/tags)
after each batch completes: QA (todo [], check, constitution, node mtest.js iPhone test, look at screenshots),
  covers (Higgsfield gpt_image_2_5 4:3 medium, ≤12 per batch) → images/cover.jpg → embed.py --draft → thumbs → draft.py build
  → commit own files by name → fetch/merge → push. Then publish the best few to production (14 priority langs etc).
final: report in Japanese + 2–3 BACKLOG reminders; update BACKLOG.md/CLAUDE.md about the series.
covers done: batch K (6)
## 22:45 state: API 529 overload when ~20 agents ran. Now keep ≤12 agents running.
stopped (resume later, one by one as others finish): I N O Q R S T U
running: A C D G (resumed) F H J L M P V W
waiting new: X Y Z BK1 BK2 BK3 BK4
covers done: K(6) B(all but play-by-play) E(louder, stand-tall)
## 23:30 done: A B C D E F G H I J K L M N O P Q R (covers done: A B C D E F G K)
running: S V W ; resumed T U ; launching X Y Z BK1-4 ; cover agent → P H I J L M N O Q R
## 22:20 pushed cd8dde8fd: 81 drafts with covers (A–G,K + pilot). Flip-card mirror bug fixed (13 drafts).
done writing: A–W except U. running: U X Y Z BK1-4 + cover agent (queue P H I J L M N O Q R S V W T)
NOTES3 credit = "📚 I wrote this from my notes on books and blogs I have read." (W fixed)
next: when covers land → build, mtest, commit. then publish best ~5 to production.
