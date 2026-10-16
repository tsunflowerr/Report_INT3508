# Stage 1a plan: stability-first C-120 on the 34 T3.8 test cells (config only)

Written 2026-10-10 ~22:20 by Claude (main session). Approved by the owner on 2026-10-10 ("làm cả 2 bước này luôn").
Context: `optimize/codex-debate/claude-work/R17-FINAL-VERDICT.md` A2 Stage 1a and `codex-work/R18-CONFIRM-CODEX.md`.

## What runs

- Arm: `C-120` (`tang3/configs/C-120.json`, SHA-256 ac0f97589427919c5175e9cc952849305702ced45313a5a2db88167dff030520).
  It differs from `C-30.json` only in the drop `hardLimit` (120000 instead of 30000 ms).
- Cells: the 34 T3.8 test cells of `tang3/t38/split-t38-v1.json` (`test` list), unchanged.
- Everything else exactly as T3.8: runner `C:/RideBoundData/research/runner-tier3-v2` (tree ac251ef3…), WP4
  `wp4-tier3-v2.json` (recovery (b)), world wrapper v1.2, fixtures `C:/RideBoundData/research/fixtures-panelA-v1`,
  drivers `tang3/calib/panelA/drivers`, master seed 7, one repeat, cwd `E:/Code/RideBound-deadline` (never modified,
  inventory 0da63eaf…).
- Driver: `tang3/t38c120/run_t38c120.py` (reuses `run_t38.py` unchanged, overrides only the arm list, output root,
  log folder and STOP file). Output: `C:/RideBoundData/research/tier3-t38c120-v1`. AC power only; 6 workers.

## Predictions (written before any C-120 job on these cells)

Comparators are the archived T3.8 test runs: U 2,434 served; C-30 2,338 served; naive late > 60 s vs first promise
U 203, C-30 76; timely ≤ 60 s per 3,672 requests U 2,231, C-30 2,262; at ≤ 120 s U 2,332, C-30 2,327.

- P1. Every C-120 job ends `status: pass`; 0 non-normal (forced) decisions; 0 riders with Σ|c| > 120 s.
- P2. Served ≥ 2,362 (at least 24 of the 96-rider C-30 → U gap).
- P3. Naive late > 60 s riders strictly between 76 and 203.
- P4. Timely ≤ 120 s completions ≥ 2,327 (not below C-30).
- P5. Recorded cumulative-only drop-budget prune records across the 34 runs ≤ 2.

A failed prediction is reported as failed; no re-run or retuning. Analysis reuses existing readers
(`tang3/evidence/audit_vep.py`, `optimize/codex-debate/claude-work/r13-final-judge/cumulative_decisive_check.py`
logic, `optimize/display_layer.py` causal-no15 replay) and is re-computed independently by Codex.
