# Round 27 brief for Antigravity: read Chương 2, Chương 3 and Chương 4 (both halves) as an outside reader and as a lecturer

This brief replaces round 23 (the Chương 3 draft changed since then; do not run round 23).

Reminder: in rounds 16 and 20 your own added numbers and paraphrases were often wrong (e.g. you turned "serves 96
fewer" into "keeps service equal"). This time: do NOT change any number or meaning; comment only on what you read in
`inputs-r27/`; write "chưa kiểm chứng" for anything you cannot see there. Write in natural Vietnamese.

## Inputs (folder `inputs-r27/`)

- `06-chuong2-v4.tex` — Chapter 2 (background and related work). Review it like the others. For the lecturer part,
  also ask: can you tell, in one sentence, how the thesis's rule differs from the closest earlier work?
- `07-chuong3-v3.tex` — Chapter 3 (method) of an undergraduate thesis in Vietnamese (LaTeX source; lines starting
  with `%` are hidden evidence notes, not text).
- `08-chuong4-phanA.tex` — the first half of Chapter 4 (experiments and main results, sections 4.1–4.5).
- `09-chuong4-phanB-v7.tex` — the second half of Chapter 4 (sections 4.6–4.11: forecast promise, comparison with
  padding, snow afternoon, validity checks, discussion and limitations). Treat parts A and B as one chapter.
  - For part B, also answer: after reading 4.8, can you say in one sentence why a system would need this rule if
    adding 30 seconds to every promise gives about the same number of on-time riders?
- `STYLE-GUIDE-VI.md`, `GLOSSARY-VI.md`, `WRITING-BRIEF.md` — the rules both chapters must follow.

## Task (four sections: two per chapter)

For each chapter separately:

1. **Người đọc ngoài ngành** (a final-year student of another field): go through the chapter section by section. For
   every sentence that is hard to understand, unnatural in Vietnamese, too long, uses an English word inside a
   Vietnamese sentence, or introduces a symbol before explaining it, quote the line number and the sentence and
   propose a clearer Vietnamese version WITH THE SAME MEANING AND THE SAME NUMBERS. At the end, list the 5 places where
   you got lost first.
2. **Giảng viên chấm (UET, CNTT):** for Chương 3: is the method complete and clear enough to understand and reproduce at
   a high level? For Chương 4: does each table and figure say what is compared, on which runs, and what the reader
   should conclude? Which definitions, tables or pseudo-code are confusing or missing? Which statements sound like
   overclaims (novelty, "duy nhất", "tối ưu", causal words, guarantees)? Do the two chapters use the same words for
   the same things? Quote line numbers.

## Rules (strict)

- Do NOT run terminal commands, do NOT install anything, do NOT modify any file except creating the single output
  file below. Do not open anything outside `inputs-r27/`.

## Output

One new file in this folder: `R27-ANTIGRAVITY.md`, ending with the line `END OF ANTIGRAVITY R27`.
