# Round 39 (Codex): apply your R37 corrections to Chương 4 part B (v10 → v11)

First read `CODEX-PARALLEL-RULES.md` in this folder; its rules apply.

## Inputs

- **Base:** `S/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex`, with its notes `09-chuong4-phanB-v8-NOTES.md` (they
  describe v10) and the log `reviews/CH4B-REVISION-LOG.md`.
- **Your review:** `codex-work/r37-ch4b-verify/R37-CH4B-V10-VERIFY-CODEX.md`, verdict ACCEPT WITH CORRECTIONS. It gives
  exact Vietnamese replacements. Top five:
  1. separate the 30 s cap from the observed 29,2 s maximum, and restrict padding comparisons to C-30;
  2. restore the missing denominators and the 34-scenario oracle cohort;
  3. say that the ML counts are recovered from rounded rates, and remove English outside parentheses;
  4. add the verified forced-decision pools and restore aggregation labels;
  5. synchronise chapter 3's test results, part A's snow identity, and the Appendix C reference.
- **Consistency targets:**

  | Part | File |
  |---|---|
  | Part A, final | `codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex` (your R36 output); its handoff list for part B is in `08-chuong4-phanA-v5-CHANGES-v3.md` |
  | Chapter 3 | `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex` |
  | Appendices | `codex-work/r31-ch5/11-phuluc-v2.tex`, which defines `phuluc:A`, `phuluc:B`, `phuluc:C` |
  | Assembly notes | `S/rewrite-2026-10/ASSEMBLY-NOTES.md` |

- **Test re-run:** `S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md`, attempt 4: 1.025/1.025 in a single run
  on 13/10/2026.

## Do

1. Make a TARGETED revision. Apply each R37 correction, plus part A's handoff items for part B. Keep every unaffected
   sentence.
2. Also fix the two overfull boxes from the trial build: v10 lines 39–59 (29,2 pt) and 170–174 (15,8 pt). See
   `C:/RideBoundData/research/thesis-trial-build-2026-10-13/main.log`. Shrink the tables; do not change their content.
3. Re-run your read-only checks on every changed number. Check the syntax, and check that every `\ref` resolves
   against part A v5, chapter 3 v4 and the appendices v2. The build measured chapter 4 at 21 pages against 26,5, so
   cut nothing unless a reviewer asked for it.

## Output (subfolder `codex-work/r39-ch4b-v11/`)

- `09-chuong4-phanB-v11.tex`
- `09-chuong4-phanB-v11-CHANGES.md`, with one row per change: v10 line, old text, new text and evidence.

Final message: the number of changes, the words per section, and any items left for other chapters.
