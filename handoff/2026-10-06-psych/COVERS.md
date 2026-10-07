# 🆕 2026-10-07：表紙のデザインを変えた

画像生成AIのふわふわペンギンをやめて、**本家ペンゲッソ（紺・青い帽子・サングラス）＋考えごとの吹き出し（立体の絵文字1つ）**にした。
作り方：`python3 tools/cover/make-cover.py <slug> <絵文字> '<色>' [--flip]`（くわしくはファイルの先頭）。下の古い手順は参考に残す。

---

# Cover job (draft articles). Folder P = this folder.
For each slug you are given:
1. Prompt: `cd /Users/ezakimasaaki/Desktop/html-works && python3 P/prompts.py <slugs…>` prints the English prompt from draft/<slug>/source.md (## 表紙のプロンプト).
   Clean it: remove "(no rings or patterns on the belly)" style parentheses and quotes; make sure it ends with
   "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering."
   Avoid in prompts: mesh/grids/nets/microphone grilles, many small repeated holes or dots, clusters (owner has trypophobia), glass, stained glass, scary things, people.
2. Generate with Higgsfield `generate_image_batch` — model "gpt_image_2_5", aspect_ratio "4:3", quality "medium".
   The backend allows ~4 concurrent jobs: submit 4 at a time, then `jobs_wait` until terminal, then the next 4. A 429 = just resubmit that item after the current ones finish.
   Do NOT call show_generation_by_ids (no widgets needed).
3. Download: `P/dl.sh <slug>=<file name after the cloudfront user path> …` (dl.sh joins it with https://d8j0ntlcm91z4.cloudfront.net/user_3HlRdlUC3T5anmt1JdUaDB8ZK10/). Needs network: run Bash with dangerouslyDisableSandbox.
4. Review: `cd P/cv && python3 ../sheet.py ../sheet_<name>.jpg <slug>.png …` then Read the sheet image. Reject and regenerate (with a fixed prompt) if: not a cute chubby penguin, pink penguin, rings/patterns on belly, text/letters, humans, creepy look, mesh/grid/holes/dense repeated small objects, glass, the object does not fit the article.
5. Apply accepted ones: `P/setcover.sh <slug>` (converts, embeds into the draft page, makes the thumbnail, moves the png to cv/done/). It prints ✓.
Don't run git or any builds. Report: list of slugs done, any that failed.
