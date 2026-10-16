# Round 18 from Claude: confirm or correct the round-16/17 final verdict

A Claude-side final judge (fresh context) merged rounds 16–17 into `claude-work/R17-FINAL-VERDICT.md` (and helper
outputs in `claude-work/r17-final-judge/`). Antigravity produced no output (its session opened the wrong workspace).
This is the last check before anything reaches the owner. You may read every R16/R17 file on both sides.

## Do

1. **Confirmation audit.** For every row of the verdict's confirmation table that its ranked list or the Vietnamese
   answers (section C) depend on, open the anchor and mark AGREE / WRONG (correct value + anchor) / CANNOT CHECK.
   Re-derive key numbers with your own code where cheap (existing transcripts only, ≤ 2 processes).
2. **Overclaim audit** of the ranked list and of section C against the owner's strict claim boundary
   (`E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`, READ ONLY) and against your R17 corrections
   (cumulative wording, "26% knowable", 5.66% vs 5.94%, "same riders", cost-saving denominators, Hörl & Zwick
   hard-gate distinction, recovery(b) already enabled). Give corrected Vietnamese wording where needed.
3. **Verdict:** ACCEPT / ACCEPT WITH CORRECTIONS (minimal list) / REJECT (decisive reason + alternative) on the ranked
   list, the single recommended next step, the optional extension and its job count/design. If the verdict resolved a
   disagreement between you and Claude (sequencing; 74 vs 178 jobs; primary endpoint; forecast as alternative vs
   future work), say whether you accept the resolution and why.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R18-CONFIRM-CODEX.md` (+ helper scripts in `codex-work/`). Zero hallucination; no simulations, builds or
installs. Finish with a short final message listing files and your one-line verdict.
