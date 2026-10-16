# ML pilot: "better prediction or fewer changes?" SEALED plan (2026-10-08)

**Basis.**
- Codex's "Exact sealed version I would accept" (`codex-work/ML-PILOT-REVIEW-CODEX.md` §"Exact sealed version"),
  adopted unchanged.
- `claude-work/ML-PILOT-PLAN-V2.md`.
- Concrete lists below.

**Scope.** A zero-run replay of existing runs. No simulation and no installs; the env is
`C:/RideBoundData/envs/ml-v1`, pinned sklearn 1.7.2. The days are retrospective: they were inspected before.

## Population and causal features

**Population and cohorts.**
- One effective run per cell (`forecast_family_a.run_dir` for T3.8; the w07 and WP14r folders have no retries).
- Every first-published drop promise is included. In all 179 runs accepted = completed (Codex
  `round10b-csv-inventory-crosscheck.json`), so the label cohort equals the promise cohort.

**Causal state** comes from the first published promise itself. `publishedPromise.projection.serviceOrder` is the
vehicle's remaining plan at publication.
- `other_assigned` = distinct other requestIds in serviceOrder.
- `other_onboard` = other requestIds that have a drop stop but no pickup stop in serviceOrder, i.e. already on board.
- The vehicle is `projection.vehicleId`.
- No future event, final assignment or ledger total is used as a feature.

**Base features.**

| feature | definition |
|---|---|
| clock_min | (window start s + t0 / 1000) / 60 |
| horizon_s | P0 − t0 |
| pick_s | first pickup promise − t0 |
| fc_ext_s | D0 − P0 |
| maxride_s | maxRideTimeMs / 1000 |
| room_s | P_pick0 + maxRide − P0 |

**Target and display.** The target is A − D0, in seconds. D0 is the historical display with a **fixed profile vintage
from 12/11 + 13/11** (`promise_stretch.v13.forecast_profile(["2018-11-12", "2018-11-13"], 25200)`), applied with
`display_layer.display`. In static WP14r, D0 = P0.

## Splits (never across arms or worlds)

**Measured traffic, arms U and C-30 (window w07).**

| role | runs | day |
|---|---|---|
| fit | `tier3-w07-v1/{arm}-d2018111{2,3}-s10-r{1,2,3,4}-w07` | 12/11, 13/11 |
| calibration | T3.8 test `d20181114-s10-r{3,4}-w07` | 14/11 |
| test | T3.8 test `d20181115-s10-r{1,2,4}-w07` | 15/11 |
| test | T3.8 test `d20181116-s10-r{1,2,4}-w07` | 16/11 |

The two test days are reported separately.

**Static traffic, WP14r v6.**
- Arms: FREE = `b1-ref`, LOCKS = `c1-nobudget`, C-120 = `c1-budget120`, C-60 = `c1-budget60`, C-30 = `c1-h6ref`.

| role | runs |
|---|---|
| fit | day 12/11, r1–r3, w08 and w17 |
| calibration | day 12/11, r4, w08 and w17 |
| test | day 13/11, r1–r4, w08 and w17 |

## Learners (fixed; no search)

1. **HGB (primary).** `HistGradientBoostingRegressor(loss="quantile", quantile=0.90, learning_rate=0.05,
   max_iter=100, max_leaf_nodes=7, min_samples_leaf=20, l2_regularization=1.0, random_state=7, early_stopping=False)`
   on the base features plus `other_assigned` and `other_onboard`.
2. **HGB-nostate.** The same learner without the two state counts.
3. **LinQR.** `StandardScaler` + `QuantileRegressor(quantile=0.90, alpha=1.0, solver="highs")` on all features.

## Matched quote cost

The rule is set on the calibration first promises, for E ∈ {15, 30, 60} s; E = 30 is primary.
- Let δ = D0 − P0 and w = max(0, predicted residual).
- Set ρ = (E − mean δ) / mean w, and quote F = D0 + ρ·w.
- If E < mean δ, the budget is infeasible. If mean w = 0, F = D0 + (E − mean δ).

**Controls.**
- **uniform:** P0 + E.
- **fc+uniform:** D0 + (E − mean δ). In static worlds this equals uniform.

**Test metrics.** Rules are frozen before any test label is read; there is no test rescaling.
- Y60: A − F > 60 s.
- early60: A − F < −60 s.
- Symmetric accuracy: |A − F| ≤ 60 s.
- Mean extension (F − P0) and p90 extension (nearest rank, ceil(0.9n)).
- Mean horizon (F − t0).
- Counts.
- Common-completed cohorts are supplementary.

**A learner WINS against a control** only if, at the same E, on the same test cohort, all four hold:
1. its Y60 is lower;
2. its mean extension ≤ the control's + 1 s;
3. its p90 extension ≤ the control's + 15 s;
4. its early60 ≤ the control's + 1 pp.

## Predictions (Codex wording)

| ID | Prediction |
|---|---|
| ML1 | C-30, measured: the HGB gain in Y60 over fc+uniform is < 1 pp on each test date (15/11, 16/11) at E = 30. This is a descriptive low-opportunity hypothesis. |
| ML2 | U, measured: HGB lowers Y60 by ≥ 1 pp against both uniform and fc+uniform, on both test dates, at E = 30, subject to the WIN guards. |
| ML3 | Static FREE: HGB lowers Y60 by ≥ 3 pp against uniform on 13/11 at E = 30, with a positive gain in each window (w08, w17), subject to the guards. |
| ML4 | None of HGB, HGB-nostate and LinQR, under static FREE/LOCKS or measured U, jointly matches same-world C-30 fc+uniform at E = 30 in both Y60 (≤) and symmetric accuracy (≥). Checked on each measured test date and static 13/11, on own cohorts, with common-completed cohorts reported. |
| ML5 | For each ML2 or ML3 setting with G_full > 0, where G = Y60(control) − Y60(model) against fc+uniform (uniform in static): G_full − G_nostate ≥ G_full / 2. This is a diagnostic, not causal attribution. |

## Kill criteria

- Invalid timing or provenance stops the pilot before fitting.
- If ML2 and ML3 both fail, stop expanding this learner family and report "no demonstrated gain in this pilot".
- A failure on the incident date never licenses changing the split.

**Outputs.**
- Data: `C:/RideBoundData/research/ml-pilot-v1/riders-causal-<date>.csv`.
- Scripts and reports: `claude-work/ml_pilot_*`.
- Every file is created exclusively (mode "x").
