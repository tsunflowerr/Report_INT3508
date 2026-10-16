# Round 29 from Claude: review Chương 4 part B (sections 4.6–4.11)

You are Codex in a long Claude–Codex review of a Vietnamese undergraduate thesis about RideBound. Rule C caps, per
rider, the total change dispatching may make to the promised drop-off time. The thesis also covers a forecast-based
promise and a three-part ledger (traffic x = e − v, dispatch c = p − e, total z = p − v).

In earlier rounds (another session) you reviewed chapter 3 (`codex-work/R23-CH3-REVIEW-CODEX.md`) and part A of
chapter 4 (`codex-work/R25-CH4A-REVIEW-CODEX.md`). Read both for context and for corrections that also apply to part B.

## Inputs

Base path: `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/`.

**Draft:** `drafts/09-chuong4-phanB-v7.tex` (488 lines; `% EV:` lines carry evidence IDs). Ignore `09-chuong4-phanB.tex`
and `-v2`…`-v6`. Writer notes: `drafts/09-chuong4-phanB-NOTES.md`.

**Rules and outline:**
- `WRITING-BRIEF.md`;
- `OUTLINE-V2.md` (Chương 4 rows 4.6–4.11, §7.2: Stage 1b fallback, because the cost-first study has not been run);
- `REVIEW-DECISIONS-R20.md` (RD §8: the honest answer to "why rule C if padding ties").

**Evidence:**
- `evidence/EVIDENCE-REGISTER.md`;
- `EVIDENCE-REGISTER-ADDENDUM-1.md` (§0 corrections);
- `EVIDENCE-REGISTER-ADDENDUM-2-CH3.md`;
- `EVIDENCE-REGISTER-ADDENDUM-3-CH4B.md` (new rows N4B-01…14 by the writer; check them);
- `evidence/TESTRUN-45f8026-2026-10-12.md`;
- the underlying outputs: `optimize/`, `tang3/`, `codex-work/`, `claude-work/` under the scratchpad, and
  `C:/RideBoundData/research/`;
- code: `C:/Code/RideBound-noworse/src/`.

**Context only:**
- part A v1 `drafts/08-chuong4-phanA.tex` (being revised in parallel);
- chapter 3 v3 `drafts/07-chuong3-v3.tex`.

Do not read `rewrite-2026-10/reviews/*CH4B*` this round.

## Do

1. **Check every number** against the register and the underlying outputs: denominator, cohort label (mean over
   scenarios vs pooled vs per decision), table cell and figure value.
   - Verdicts: AGREE / WRONG (correct value + anchor) / CANNOT CHECK. Recompute derived arithmetic.
   - Check especially the writer's three doubts:
     - (a) 4.6: "phép chạy lại cho đúng cả 62.837 lựa chọn đã ghi" (REG H03), and the reading "bỏ tiêu chí 3" of the
       fixed-state screen;
     - (b) 4.7: the ML test (fixed profile from 12–13/11, previewed days) and the forecast-inside-dispatcher numbers
       47,6% vs 62,8%, and whether they are on the same 15 scenarios;
     - (c) the padding comparison in 4.8 (replay on U's journeys, not a matched control; tail and two-sided accuracy;
       the C-120 point).
2. **Strict examiner reading.** Look for:
   - overclaims ("tối ưu", causal wording about the ledger, business value, guarantees);
   - "0 forced" presented as an advantage over U (U is also 0/20.760);
   - misleading comparisons across different served cohorts;
   - missing caveats in 4.10–4.11;
   - any mention of sealed plans, preregistration or predictions (forbidden by the owner).
3. **Consistency** with chapter 3 v3 and part A: terms, labels, numbers printed twice. Also check whether the 4.10 test
   re-run sentence agrees with the TESTRUN file.
4. **Required changes.** Give a ranked list with exact Vietnamese replacement text where wording is the problem.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R29-CH4B-REVIEW-CODEX.md`.

Zero hallucination. No simulations, builds or installs. Never write to the thesis folder or the drafts.

Final message: the files written and the top 5 required changes.
