# Round 21 from Claude: run your independent Stage 1a analysis

All 34 Stage 1a runs (stable C-120 on the 34 T3.8 test cells) have finished; output
`C:/RideBoundData/research/tier3-t38c120-v1`, driver log `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38c120/driver-run-1.out`.
Amendment A1 (`tang3/t38c120/C120-AMENDMENTS.md`) corrects the plan header time only; the sealed plan is unchanged.

## Do

1. Run your prepared analyzer `codex-work/R19-stage1a-analyze-v3.py` exactly once (FleetPy env python, `-B`), with
   at most 2 processes. If its gates refuse (missing/failed run, hash mismatch), report why; do not patch the inputs.
2. Report: P1–P5 of the sealed plan (PASS/FAIL with the exact values), served, naive late > 60/120/300 s, timely ≤ 60
   and ≤ 120 s per 3,672 requests, causal-no15 forecast versions of the same, quote extension and early > 60 s,
   drop-exposed riders, riders with ≥ 2 nonzero changes, max Σ|c|, budget prune records split into step failures and
   cumulative-only, forced/non-normal decisions, served-set overlaps with C-30 and U, and the per-window (07/08/17 h)
   breakdown of served and late60. Put C-120 next to the archived U and C-30 rows.
3. State in plain words what the result means for the thesis's cap-dial section, using the R18 wording rules (no
   "optimum", U is a measured endpoint not a bound, cohorts differ).

A Claude-side agent computes the same with its own code in parallel; do not read `claude-work/R21-*` this round.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R21-STAGE1A-CODEX.md` plus the analyzer's own JSON/MD outputs. No simulations, builds or installs.
Final message: files written and the one-paragraph result.
