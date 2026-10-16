# Round 34 (Codex, parallel): verify the revised Chương 4 part A (v4)

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

You reviewed part A v1 in `codex-work/R25-CH4A-REVIEW-CODEX.md`. A Claude reviser produced
`S/rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex` from three reviews: yours, a Claude fact check
(`reviews/R25-FACTCHECK-CH4A-CLAUDE.md`), and a Claude reader+lecturer review
(`reviews/R25-READER-LECTURER-CH4A-CLAUDE.md`).

Its decisions are in `reviews/CH4A-REVISION-LOG-v2.md`. Use v2 of the log; v1 has muddled counts. Its new evidence is
in `evidence/EVIDENCE-REGISTER-ADDENDUM-4-CH4A.md` (rows C4A-01…20) and `evidence/checks-ch4a-v2/` (three scripts and
their outputs).

## Do

1. **Your ten R25 changes.** For each, say whether it is FIXED, PARTLY or NOT, with the v4 line number.
2. **Every new number in v4.** Verify each one independently, with your own read-only probe where possible:

   | Topic | Values |
   |---|---|
   | Riders more than 30 s late against the first promise | C-30: 292 of 2.338; the deadline rule: 289 |
   | M⁺-60 / V-30 | 79 / 74 late over 60 s, with their timely counts |
   | Dispatch-share totals (s) | 23.027/31.353, 82/6.892, 4.836/12.450 |
   | Fixed-traffic shared riders | 865/346/303/266/241 |
   | Fixed-traffic moved riders | 388/62/41/20/6 |
   | Morning cap levels | the full ladder |
   | Snow requests | 864 |
   | Morning runs | 136 of 192 archived |
   | Early arrivals over 60 s | 7/3/1 |
   | Worst lateness (s) | 660,1 and 232,3 |
   | First-promise length (min) | 14,15 vs 14,12 |

   Also check B14 (1.075), N-11 (61 of 76) and X3-16 (0 of 20.760). Mark each AGREE, WRONG (with the correct value and
   an anchor) or CANNOT CHECK.
3. **The rejected comments.** Spot-check them: D11, D-c2, G1-r2, G1-t, and the partially declined items. Was each
   rejection justified?
4. **Regressions.** Look for new overclaims, broken `\ref`s, a lost caveat, a cohort label that no longer matches its
   denominator, or a forbidden word.
   - The "quyết định bị ép" definition must match the code: `RunnerSession.cs:1012-1027` and
     `HardVectorCandidateAssessor.cs:252-300`, both under `C:/Code/RideBound-noworse/src/`.
   - The disclosure that the 120 s level was chosen after the main-set results were seen must use data-reuse wording
     only.
5. **Consistency with part B** (`09-chuong4-phanB-v7.tex`). List every number or term that differs.

## Output (subfolder `codex-work/r34-ch4a-verify/`)

`R34-CH4A-V4-VERIFY-CODEX.md`, with:
- a verdict: ACCEPT / ACCEPT WITH CORRECTIONS / REJECT;
- a ranked list of corrections, with exact Vietnamese replacements.

Final message: the verdict and the top 5 corrections.
