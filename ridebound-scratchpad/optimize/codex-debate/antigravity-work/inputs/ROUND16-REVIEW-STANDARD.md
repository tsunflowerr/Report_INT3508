# Round 16 review standard (shared by every participant)

Judge every claim and every proposed direction as a strict reviewer at a top venue in transportation / operations
research (e.g. Transportation Research Part C/B, Transportation Science, IEEE ITSC) would. Be objective: no side gets
credit for being Claude, Codex or Antigravity. Agreement with the majority is not evidence.

## Criteria (score 1–5 each, with a one-line reason)

1. **Novelty / originality** relative to the closest prior work (name it; respect the owner's strict claim boundary).
2. **Significance**: would operators or other researchers change what they do because of this?
3. **Technical soundness**: is the mechanism correct; are the claims implied by the evidence; are confounders
   (selection, package comparisons, stability-first objective, low load, one city-wide traffic factor) handled?
4. **Experimental rigor**: strong baselines, fair comparison (same information, same quote cost), held-out data,
   enough independent units (days, events), uncertainty reported, no post-hoc tuning presented as confirmation.
5. **Reproducibility**: scripts, seeds, sealed plans, independent re-computation.
6. **Feasibility in the remaining time** (~5 weeks, unconfirmed) for an undergraduate, with tests and a separate
   worktree for any code change.

## Required output per claim / direction

- Verdict: ACCEPT / MAJOR REVISION / REJECT, with the decisive reason.
- The single most damaging reviewer question, and whether the current evidence answers it.
- Every factual statement anchored (file:line, or URL + short quote). Unverified = say so. Numbers you cannot trace must
  not be used.

## Rules of debate

- Attack arguments, not participants. Concede when the evidence is against you.
- A statement from another participant is not evidence until you have checked its anchor.
- Distinguish: measured result / first-order screen / inference / hypothesis / opinion.
