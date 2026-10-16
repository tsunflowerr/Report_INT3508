# Round 20 from Claude: review the thesis rewrite outline and contribution statement

The owner approved rewriting the whole thesis (Vietnamese, ~70–79 pages, style of his project report
`C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`). A Claude structure editor wrote
`E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/OUTLINE-PROPOSAL-CLAUDE.md` (audit of the current
105-page thesis, a 74-page outline with page budgets and evidence keys, a Vietnamese contribution statement, risks).
Your distilled writing rules `codex-work/R19-SKILLS-REVIEW.md` apply. A Claude "lecturer" agent and Antigravity review
the same outline in parallel; do not read `claude-work/R20-*` or `antigravity-work/R20-*` this round.

Owner rules for the text: every factual sentence backed by verified evidence (code location, saved output, primary
source) — code is not pasted; no talk of sealing, preregistration or "predicted before running"; no "only/first", no
causal claims the data cannot support; Vietnamese only (no English inside sentences), little jargon, academic but easy
for outsiders; concise; contributions must be understandable and show their value.

## Do

1. **Adversarial review of the contribution statement** (outline §3, sentences 1–8 and the "not claimed" list):
   check every number and anchor (AGREE / WRONG / CANNOT CHECK), find any sentence a strict examiner could falsify or
   call an overclaim against `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (READ ONLY), Hörl & Zwick
   2022, Fielbaum & Alonso-Mora 2020, Schulz & Pfeiffer 2026; propose corrected Vietnamese wording.
2. **Structure review**: does the outline answer what a UET committee expects (problem, gap, method, evaluation,
   limitations), keep one storyline, and fit 70–79 pages? Which sections are too long/short, missing or redundant?
   Are the evidence keys (§2.10) correct and sufficient for each section? Is anything from the current thesis cut that
   an examiner would need (e.g. the theorem as a remark)?
3. **Check the audit of the current thesis** (§1): spot-check at least 15 file:line claims about the current LaTeX in
   `E:/Code/Report_INT3508/ridebound/noi-dung/*.tex` (READ ONLY).
4. **Recommend decisions** on the owner-only items (§4.3: theorem chapter, English cover/abstract, title, appendix,
   Stage 1b inclusion, rule names), with reasons.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R20-OUTLINE-REVIEW-CODEX.md`. Zero hallucination; no simulations, builds or installs; never write to the
thesis folder. Final message: files written and the 5 most important changes you require.
