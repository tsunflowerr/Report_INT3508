# ML pilot plan v2: "better prediction or fewer changes?" (DRAFT v2, Claude, 2026-10-08; not sealed)

**Question.** Fielbaum & Alonso-Mora (2020) name two remedies for unreliable first announcements: "better predictions
or to make these changes less frequent" (local PDF text :499). This is verified, and our survey S4 found no
head-to-head test of the two. We test them on existing runs only:
- **learned prediction:** a model trained on previous trips' outcomes pads the first drop promise under free or locked
  dispatch;
- **commitment:** rule C-30 plus the frozen historical forecast display.

The comparison is made at **equal mean quote extension**.

**Not claimed:**
- that learning ETAs from trips or fleet state is new (DeeprETA, Ulmer & Thomas 2019, Hildebrandt & Ulmer 2022,
  Kim et al. 2024; survey S4);
- that rule C is new in principle (Hörl & Zwick 2022 strategy B, verified at `claude-work/pdf/hoerl-zwick-2022.txt:527-539`).

**What could be new is the measurement:** whether commitment or prediction yields better promises at the same quote
cost, separated by the ledger into its dispatch and traffic parts.

## Data

`C:/RideBoundData/research/ml-pilot-v1/riders-2026-10-08.csv`, from `ml_extract_riders.py`. All features are known at
t0, the first drop promise.

## Splits (within one policy only; never train on one arm and test on another)

**Real traffic (measured factors), arms U (LOCKS) and C-30.**
- Train on all rows with day ≤ 14/11: w07 development cells on 12–13/11, T3.8 test cells on 14/11, and T3.8
  calibration cells on 14/11.
- Test separately on 15/11 (the documented incident day) and on 16/11.
- Weekends (17–18/11) are reported separately. The forecast is inactive there, so they act as a stress test.

**Static traffic (WP14r v6), arms FREE, LOCKS, C-120, C-60, C-30.**
- Primary split: train on 12/11 (the observed holiday), test on 13/11.
- Sensitivity: 4-fold leave-one-sample-out (r1–r4) across both days.

## Methods

The promise for each rider is F = P0 + extension.

| Method | Extension |
|---|---|
| naive | 0 |
| fc (forecast only) | D0 − P0 |
| uniform pad | b |
| fc + pad | (D0 − P0) + b |
| GBM | max(0, q̂_τ(features)), predicting y = A − P0 |
| fc + GBM | (D0 − P0) + max(0, q̂_τ of y − (D0 − P0)) |
| GBM-nopool | GBM without load_t0, onboard_t0 and room_s (ablation) |

GBM is sklearn `HistGradientBoostingRegressor(loss="quantile", quantile=τ, random_state=7)` with default
hyperparameters (no tuning). Its features are: bin, minute, window, weekday flag, horizon_s, direct_s, room_s,
wait_promised_s, fc_ext_s, load_t0 and onboard_t0.

**Matched cost.** For each budget E ∈ {15, 30, 60} s, choose each method's parameter (b, or τ on the grid
0.50…0.99) on TRAIN so that the mean extension is as close as possible to E without exceeding it. Then evaluate the
frozen rule on TEST.

**Metrics on TEST.**
- Y60.
- Two-sided ±60 s accuracy.
- early60.
- Mean and p90 extension.
- Timely completions per request (served share × (1 − Y60)).
- Quantile coverage of the GBM.

## Predictions (to be sealed)

| ID | Prediction |
|---|---|
| ML1 | C-30, real traffic: fc + GBM's test Y60 is within 0.3 pp of fc-only at E = 15 and E = 30, on both test days. |
| ML2 | U (LOCKS), real traffic: GBM or fc + GBM lowers test Y60 by ≥ 1 pp against the best non-learned method at E = 30 and E = 60, on both test days. |
| ML3 | FREE, static: GBM lowers test Y60 by ≥ 3 pp against the uniform pad at E = 30 and E = 60 (13/11). |
| ML4 | At E ≤ 30 s, no learned method under FREE or LOCKS reaches C-30's test Y60 (≤ 0.5%) together with two-sided accuracy (≥ 98%). |
| ML5 | The gain in ML2 and ML3 comes from pooling features: GBM-nopool loses at least half of the gain. |

**Kill criterion.** If ML2 and ML3 both fail, then learning from previous trips adds nothing in our worlds, and we
report that.

## Honest limits

- Inspected days; few independent days.
- Arms share requests.
- Simulated worlds: one citywide factor (real traffic) or no traffic (static).
- No booking response.
- The result is an internal comparison of two remedies, not a deployment estimate.
