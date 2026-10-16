# Round 23 from Claude: review the Chương 3 draft (method)

Draft: `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts/07-chuong3.tex` (662 lines, Vietnamese
LaTeX; `% EV:` comment lines carry the evidence IDs) and its notes `drafts/07-chuong3-NOTES.md` (code anchors X3-01…19
that are not yet in the register; missing-evidence list; new references `horl2022`, `engelhardt2026`). Rules:
`rewrite-2026-10/WRITING-BRIEF.md`, `OUTLINE-V2.md` (chapter 3), `REVIEW-DECISIONS-R20.md`, register
`evidence/EVIDENCE-REGISTER.md` + `EVIDENCE-REGISTER-ADDENDUM-1.md` (read its §0 corrections). Claude-side fact,
reader and lecturer agents review in parallel; do not read `rewrite-2026-10/reviews/R23-*` this round.

## Do

1. **Technical and factual check** of every definition, formula, pseudo-code line, code claim (open the cited code
   read-only in `C:/Code/RideBound-noworse/src/`; verify X3-01…19), number and citation. AGREE / WRONG (correct
   value + anchor) / CANNOT CHECK. Pay attention to: rule C definition and remaining allowance; the "Nhận xét" and its
   assumption (N) and proof; the rules table (U, FREE, C, M⁺, V, recovery (a)/(b)); the selector order and its
   activation conditions; the forecast pseudo-code vs `optimize/display_layer.py` / `promise_stretch.py`; the ledger
   formula; the −1 ms earlier-move wording; Hörl & Zwick eq. 7 positioning; verify the two new references' metadata
   (DOI pages) and whether `engelhardt2026` should replace the existing FleetPy citation.
2. **Strict examiner reading**: overclaims, unclear or missing method steps, places where an outside reader would get
   lost, inconsistencies with OUTLINE-V2 and with chapter 4's needs (labels listed in NOTES).
3. Ranked list of required changes with exact replacement Vietnamese text where wording is the problem.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R23-CH3-REVIEW-CODEX.md`. Zero hallucination; no simulations, builds or installs; never write to the
thesis folder or the drafts. Final message: files written and the top 5 required changes.
