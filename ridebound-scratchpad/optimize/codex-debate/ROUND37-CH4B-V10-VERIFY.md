# Round 37 (Codex): verify Claude's revision of Chương 4 part B (v7 → v10)

First read `CODEX-PARALLEL-RULES.md` in this folder; its rules apply.

## Background

You reviewed part B v7 in `codex-work/R29-CH4B-REVIEW-CODEX.md`. A Claude reviser produced
`S/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex` from three reviews: yours, a Claude fact check
`reviews/R27-FACTCHECK-CH4B-CLAUDE.md`, and a Claude reader+lecturer review `reviews/R27-READER-LECTURER-CH4B-CLAUDE.md`.

- **Decision log:** `reviews/CH4B-REVISION-LOG.md`, 209 rows. Your R29: 16 A / 5 M / 1 R / 2 cannot check.
- **Notes:** `drafts/09-chuong4-phanB-v8-NOTES.md`, which describes v10.
- **New evidence:** `evidence/EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md` (N4B8-01…13), the errata
  `evidence/checks-ch4b-v8/ADDENDUM-6-ERRATA-2026-10-12.md`, and the script and output in `evidence/checks-ch4b-v8/`.

## Do

1. **Your R29 corrections.** For each one, mark it FIXED / PARTLY / NOT, with the v10 line. Judge the one you had
   rejected, and the two you could not check.
2. **Every new number in v10.** Verify each independently, with your own read-only probe:
   - the forecast table counts 68/22/2 of 1.471, and by window 60/17/1 of 444, 8/5/1 of 609, 0/0/0 of 418;
   - the other rules with the forecast: 66 → 2; uncapped 129 → 63 of 1.512; 28 of 437 at 17 h;
   - snow dispatch share 8,566 / 3.445,933;
   - the snow runner identity;
   - K = 2; 14 and 15 completed runs;
   - the ML counts back-calculated from 3-decimal rates: 2 → 1 of 145, 1 of 200, 0 of 147, 0 of 197, 104 → 94 of 807,
     57 early.
3. **Judge the ML back-calculation.** The reviser says you declined to do it earlier. Is a count recovered from a
   3-decimal rate with a unique rounding bound acceptable for the thesis? Under which wording?
4. **The rejected comments.** For each, give a verdict with the reason. They are:
   - CX-10: the pooled forced-decision counts 3.849/8.496 and 5.121/8.468. You reported these; check them with a script
     and say whether they should enter.
   - B47, L-02, L-04, L-15, L-23, L-26, L-27, L-31, L-33/L-52, L-34, L-40, L-50, L-60.
5. **The padding answer that now opens 4.8.** Is it fair and evidence-backed? It contrasts 37,2 vs 7,4 s, 174 riders
   moved, a maximum of 590,1 s, and 29,2 s under C. It must not imply C is better at on-time counts or at keeping the
   first promise.
6. **Regressions.** Look for any of these:
   - new overclaims;
   - broken `\ref`s against part A v4, Ch3 v4 (`codex-work/r33-ch3v4/07-chuong3-v4-v3.tex`) and Ch2 v4;
   - lost caveats;
   - forbidden words;
   - cohort labels that no longer match their denominators.
7. **Page cuts.** v10 is about 13,1 pages by the 330-words ruler, against a budget of 11. Rank the cuts listed in
   NOTES §4 by how little the argument loses.

## Output (subfolder `codex-work/r37-ch4b-verify/`)

`R37-CH4B-V10-VERIFY-CODEX.md`, containing:
- a verdict: ACCEPT / ACCEPT WITH CORRECTIONS / REJECT;
- a ranked list of corrections, with exact Vietnamese replacements.

Final message: the verdict and the top 5 corrections.
