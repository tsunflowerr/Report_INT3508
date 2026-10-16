# Stage 1a results: stability-first C-120 on the 34 T3.8 test cells

Two independent analyses agree on every number below:
- Claude: `optimize/codex-debate/claude-work/R21-STAGE1A-CLAUDE.md`, raw `claude-work/r21-stage1a/stage1a-report-2026-10-10.txt`
  (reproduced all 14 archived U / C-30 baselines first).
- Codex: `optimize/codex-debate/codex-work/R19-stage1a-analysis.md` (+ `.json`), report `codex-work/R21B-STAGE1A-CODEX.md`
  (analyzer v4; audited 102 runs: 34 C-120 + archived U and C-30). Codex's first attempt (R21) refused because it opened
  a failed original C-30 folder instead of the passing rerun; v4 fixed only the folder resolution.

Runs: 34/34 `status: pass`, 2026-10-10 22:12–23:48, `C:/RideBoundData/research/tier3-t38c120-v1`.

| Arm / quote | Served | Late > 60 s | Late > 120 s | Late > 300 s | Timely ≤ 60 s / 3,672 | Timely ≤ 120 s / 3,672 | Mean extension | Early > 60 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C-120 naive | 2,387 | 132 | 21 | 0 | 2,255 | 2,366 | 0 s | 1 |
| C-120 forecast (causal-no15) | 2,387 | 65 | 8 | 0 | 2,322 | 2,379 | 7.27 s | 2 |
| C-30 naive | 2,338 | 76 | 11 | 0 | 2,262 | 2,327 | 0 s | 3 |
| C-30 forecast | 2,338 | 10 | 0 | 0 | 2,328 | 2,338 | 7.37 s | 4 |
| U naive | 2,434 | 203 | 102 | 18 | 2,231 | 2,332 | 0 s | 7 |
| U forecast | 2,434 | 137 | 87 | 17 | 2,297 | 2,347 | 7.18 s | 8 |

Other C-120 facts: 0 non-normal (forced) decisions; 0 riders with Σ|c| > 120 s (max 118.9 s); 103 drop-exposed riders
(4.32%), none with ≥ 2 nonzero changes; Σ|c| among exposed mean 55.5 s, p50 62.5 s, p90 104.9 s; 524 recorded
drop-budget prune records = 521 single-step + 3 cumulative-only (w08 cells d20181114-r3, d20181115-r1, d20181118-r3; 2 of
the 3 new requests ended not accepted; fail-fast witnesses, not an outcome effect); shared rides 428 (17.93% of served)
vs C-30 313 (13.39%) and U 555 (22.80%); served-set overlap C-120/C-30 2,266 common, 121 only C-120, 72 only C-30;
C-120/U 2,271 / 116 / 163. Per window, C-120 serves +4 (w07), +26 (w08), +19 (w17) over C-30.

Sealed predictions (`C120-PLAN.md`): P1 PASS, P2 PASS (2,387 ≥ 2,362), P3 PASS (76 < 132 < 203), P4 PASS (2,366 ≥ 2,327),
P5 FAIL (3 cumulative-only records > 2). Internal record only; the thesis does not discuss predictions.
