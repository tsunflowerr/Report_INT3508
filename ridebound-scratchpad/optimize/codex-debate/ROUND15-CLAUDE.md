# Round 15 from Claude: confirm or correct the final judge's verdict

A Claude-side final judge (fresh context) merged both sides' proposals and both cross-judgements into
`claude-work/R13-FINAL-VERDICT.md`. Your job is the last confirmation pass before anything reaches the owner. You may
now read every R13/R14 file on both sides, including `claude-work/R13-JUDGE-OF-CODEX-BY-CLAUDE.md` and
`claude-work/r13-final-judge/*`.

## Do

1. **Confirmation table audit.** For every row of the final judge's confirmation table that its recommendation or the
   Vietnamese answers depend on, open the anchor and mark AGREE / WRONG (with the correct value and anchor) /
   CANNOT CHECK. Re-derive the key numbers with your own code where feasible (existing transcripts only).
2. **Overclaim audit.** Flag any sentence in the final list or in the Vietnamese owner answers (section C) that
   overstates novelty against the owner's stricter claim boundary
   (`E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`, READ ONLY), business value, rider value, or
   generality beyond the measured regime. Give the corrected wording.
3. **Verdict.** Say whether you ACCEPT the final ranked list and its single recommended next step (and optional
   extension), ACCEPT WITH CORRECTIONS (list them, minimal), or REJECT (with the decisive reason and your alternative).
   If the final judge introduced a new idea, check its feasibility in the code (`C:/Code/RideBound-noworse/src/`,
   read-only) and data.
4. One extra check: the Claude-side main session confirmed in
   `claude-work/cap-vs-pad-frontier-2026-10-07.txt` that U+forecast+30 s pad (line 15), C-30+forecast (line 33) and
   Mplus-30+forecast (line 54) all give 2,328 timely completions per 3,672 requests, with Y60 4.35% / 0.43% / 0.43%,
   quote extension 37.2 / 7.4 / 7.3 s and early60 1.81% / 0.17% / 0.17%. Confirm or correct, and say whether the final
   verdict states this trade-off honestly.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R15-CONFIRM-CODEX.md`, plus any helper scripts in `codex-work/`.

Rules: zero hallucination, cite file:line or URL + quote; no simulations, no builds, no installs into shared
environments. Finish with a short final message listing the files written and your one-line verdict.
