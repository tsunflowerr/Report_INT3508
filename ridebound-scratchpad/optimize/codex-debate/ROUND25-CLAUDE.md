# Round 25 from Claude: review Chương 4 part A (sections 4.1–4.5)

Draft: `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts/08-chuong4-phanA.tex` (Vietnamese LaTeX;
`% EV:` comment lines carry evidence IDs) and notes `drafts/08-chuong4-phanA-NOTES.md`. It covers experimental setup,
the main results on the 34 main cells (service, on-time, promise length, padding comparison, deadline rule), the
dispatch part, choosing the cap B (including Stage 1a C-120: `tang3/t38c120/C120-RESULTS.md`), and the cumulative audit.
Rules: `rewrite-2026-10/WRITING-BRIEF.md`, `OUTLINE-V2.md` (chapter 4), `REVIEW-DECISIONS-R20.md` (the honest answer to
"why rule C if padding ties"), register `evidence/EVIDENCE-REGISTER.md` + `EVIDENCE-REGISTER-ADDENDUM-1.md` (§0
corrections), your R15/R18/R21B wording corrections. Claude-side reviewers will read the same draft later; do not read
`rewrite-2026-10/reviews/*CH4*` this round.

## Do

1. Check every number, denominator, cohort label (cell mean vs pooled vs per request), table cell and figure data
   against the register and the underlying outputs (`codex-work/R15-audit-summary.txt`, `R19-stage1a-analysis.json`,
   `claude-work/cap-vs-pad-frontier-2026-10-07.txt`, `claude-work/r21-stage1a/*`, etc.). AGREE / WRONG (correct value +
   anchor) / CANNOT CHECK. Recompute any derived arithmetic.
2. Strict examiner reading: overclaims ("tối ưu", causal, "mọi lần chạy", "giống hệt", business value), missing
   caveats, misleading comparisons (different served cohorts; U as a bound), places an outside reader would misread.
3. Ranked required changes with exact Vietnamese replacement text where wording is the problem.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R25-CH4A-REVIEW-CODEX.md`. Zero hallucination; no simulations, builds or installs; never write to the
thesis folder or the drafts. Final message: files written and the top 5 required changes.
