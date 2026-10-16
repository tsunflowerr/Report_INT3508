# Round 17 from Claude: cross-rebuttal

The independence rule of round 16 is lifted. Read the other debaters' round-16 work and rebut it under
`ROUND16-REVIEW-STANDARD.md`. A Claude-side rebuttal agent is doing the same to your R16 in parallel; do not read its
output (`claude-work/R17-*`) in this round.

## Read

- Claude R16: `claude-work/R16-EVIDENCE-CLAUDE.md` (+ `claude-work/r16-evidence/`), `claude-work/R16-FORECAST-CLAUDE.md`
  (+ `claude-work/r16-forecast/`), `claude-work/R16-REVIEWER-CLAUDE.md`.
- Antigravity R16, if present: `antigravity-work/R16-ANTIGRAVITY.md` (Gemini 3.8 Flash). Treat every claim in it as
  unverified until you check its anchor; the owner warned it may be less reliable.
- Your own `codex-work/R16-CODEX.md`.

## Do

1. **Verify** the numbers and code/literature claims in the Claude and Antigravity R16 files that bear on Q1–Q5,
   especially:
   - Claude evidence Q4: the first-order cost-first re-selection on WP14r (62,837/62,837 reproduced; 445 changed
     decisions = 26.0% under U's gates, cost −7.8%, extra drop push median 90.8 s; 104 = 6.1% under C-30's gates, "each
     push ≤ 35.5 s" — explain how a push can exceed the 30 s cap if it does), and the FREE vs LOCKS decomposition
     (401 promise-changing FREE decisions, ≤ 76 break a LOCKS gate).
   - Claude evidence Q2: the 973 request–run pairs (807 served anyway), the 148 screen with co-rider lateness cost
     (5/51/123 late > 60 s, 0/6/79 late > 120 s at B = 60/120/300), and the w07 screen calibration (17 gained, 11 lost).
   - Claude forecast: the snow-day split (≈26% knowable from delivered snapshots, ≈67% not), the regime gate 34 → 19
     (threshold chosen after seeing data) and 34 → 29 with one-bin latency, the claim that the Round-12 damped-trend fit
     degenerates to alpha 1.0 / beta 0 / phi 0.8, the NOAA timing (snow from 13:44), the 2013 TLC schema correction
     (zone IDs only in current official 2013 files), and the data sizes.
   - Claude reviewer: Hörl & Zwick 2022 eq. 7 `max(t_updated, t_latest)` as prior work for the dispatch-only idea; the
     claim that the thesis LaTeX never cites it; the recovery-(b) deadline rule matching C in 21/22 runs.
2. **Rebut** wherever you disagree, and **concede** where they are right. State which of your R16 rankings or
   numbers change.
3. **Converge**: give ONE ranked list (at most 3 items) of what the owner should do next, with the single recommended
   next step, its decisive experiment (arms, panel, number of jobs), sealed-style predictions and kill rules, and the
   effort. If you and Claude still disagree, state the disagreement precisely and what evidence would settle it.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R17-REBUTTAL-CODEX.md` (+ helper scripts in `codex-work/`). Zero hallucination; no simulations, builds or
installs. The laptop may be on battery: keep any computation light (≤ 2 processes). Finish with a short final message
listing files and your final ranked list.
