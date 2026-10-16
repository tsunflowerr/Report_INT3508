# Round 19 from Claude: verify Antigravity, audit the running Stage 1a, prepare for the thesis rewrite

The owner approved both steps of the R17/R18 list: (1) rewrite the whole thesis (~70–79 pages) and (2) run the staged
optimal study (Stage 1a stable-C120 now; Stage 1b cost-first 2×2 next; Stage 2 only if its gates pass). All three
models (Codex, Claude, Antigravity) must review each other, and every comment must itself be checked.

## Tasks

1. **Verify Antigravity's round-16 answer**: `antigravity-work/R16-ANTIGRAVITY.md` (Gemini 3.8 Flash; it read only the
   files in `antigravity-work/inputs/`). For every factual claim, number, code citation and literature claim: AGREE /
   WRONG (correct value + anchor) / CANNOT CHECK. Flag its proposals that contradict established round 16–18 findings
   (e.g. it recommends a damped-trend nowcasting replay as a "fair viable approach", although the Round-12 fit
   degenerates to the historical profile; it hypothesizes ≥ +10 pp sharing for cost-first). Say which of its points add
   something new and correct. A Claude-side checker is doing the same in parallel; do not read
   `claude-work/R19-*` in this round.
2. **Audit Stage 1a before its results arrive**: plan `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38c120/C120-PLAN.md`
   (sealed `C120-PLAN.sha256`, launched 2026-10-10 22:12 local), driver `run_t38c120.py` (it overrides only the arm,
   config hash, output root, logs and STOP of the unchanged `tang3/t38/run_t38.py`). Check that the design matches
   R17/R18 Stage 1a (same runner v2, WP4 v2 with recovery (b), world v1.2, fixtures, seed, cwd) and that the
   predictions are well defined. Do not touch the running jobs, the output folder or `E:/Code/RideBound-deadline`.
3. **Prepare the independent Stage 1a analysis script** (do not run it until the 34 runs exist under
   `C:/RideBoundData/research/tier3-t38c120-v1`): served, forced/non-normal decisions, Σ|c| overshoots, naive late >
   60/120/300 s vs first promise, timely ≤ 60/120 s per 3,672 requests, causal-no15 forecast replay of the same, served-set
   overlap with C-30 and U, drop-exposed riders, riders with ≥ 2 nonzero changes, recorded cumulative-only prune
   records. If the runs are already complete when you get here, run it and report.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R19-CODEX.md` (+ scripts). Zero hallucination; no simulations, builds or installs into shared environments.
Final message: files written and a one-paragraph summary.
