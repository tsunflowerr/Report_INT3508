# DRAFT (not sealed): learning promise error from previous trips. Zero-run pilot plan (Claude, 2026-10-08)

## Owner's question

Industry ETA systems learn from the times of previous trips (ML), not from "previous congested days". Can we exploit
this, and does it give anything other systems do not?

## What our world allows

**In the simulation.** Travel time is the base edges × one citywide factor per 15-min bin. Execution is deterministic
with 0 s dwell. So, at the moment a promise is made, there are only two sources of later arrival error:
1. **The traffic path after the promise.** It depends on time of day and day type. The historical-average display
   already models this.
2. **Later dispatch changes (pooling),** which depend on the policy.

A model learned from previous trips therefore cannot learn per-road or per-area traffic, because the world has none.
What it **can** learn is the pooling-induced drift, and a smoother version of the traffic shape.

**Hypothesis H-ML: "commitment makes promise error learnable from simple inputs".**
- Under C-30, the remaining error is anticipated traffic, which the historical profile already covers. Learning adds
  nothing.
- Under LOCKS and FREE, the error is dominated by pooling. A learned model with pooling features beats profile plus
  uniform padding, but still cannot match C-30's accuracy at short quotes.

## Data

All runs already exist (see `data-inventory-by-experiment-2026-10-08.txt`).

**Real-traffic data (measured citywide factors).**
- T3.8: test arms U (LOCKS) and C-30, 34 cells, days 14–18/11; plus 15 C-30 calibration cells.
- w07: 8 development cells on 12–13/11, with arms U and C-30…300.

Split chronologically by day:
- train on 12–14/11;
- test separately on 15/11 (the incident day) and 16/11;
- weekends are reported separately or excluded.

**Static-traffic data.**
- WP14r v6: FREE (b1-ref), LOCKS, C-120, C-60 and C-30 on 16 cells.
- No traffic, so the error is pure dispatch.
- Split by leaving cells out, grouped by (day, sample).

## Model

**Target.** y = A − P0: actual drop time minus the first drop promise, in seconds.

**Features available at the moment of the first promise.**
- window and 15-min bin;
- weekday or weekend;
- forecast extension D0 − P0;
- horizon P0 − t0;
- direct time (maxRide/1.5);
- room;
- promised wait;
- vehicle load at t0 (other riders assigned or on board at t0);
- number of the vehicle's remaining stops at t0, if recoverable.

**Learners.**
- sklearn `HistGradientBoostingRegressor(loss="quantile")`, with the quantile chosen so that the mean extension on
  the training data equals a budget E;
- a linear quantile regression as a control.

**Promise.** F = P0 + max(0, q̂(features)). Variant: F = D0 + max(0, q̂ of the residual after D0).

**Baselines, compared at matched mean extension E ∈ {15, 30, 60} s on the training data:** naive, forecast display,
uniform pad, forecast + uniform pad.

**Metrics.** On test: Y60, two-sided ±60 s, early60, mean and p90 extension, timely completions per request.

## Draft predictions (to be sealed after Codex review)

| ID | Prediction |
|---|---|
| ML1 | C-30, real traffic: the learned model's test Y60 is within 0.3 pp of forecast-only at matched extension. |
| ML2 | U (LOCKS), real traffic: the learned model lowers Y60 by ≥ 1 pp against the best baseline at matched extension, on both test days. |
| ML3 | FREE, static: the learned model lowers Y60 by ≥ 3 pp against a uniform pad at matched extension (base 16.8%). |
| ML4 | No learned model under FREE or LOCKS reaches C-30's test Y60 and two-sided accuracy at ≤ 30 s mean extension. |

**Kill criterion.** If ML2 and ML3 both fail, then learning from previous trips adds nothing in our worlds, and the
thesis says so.

## Caveats

- These days were already inspected.
- Few independent days.
- Arms share requests, so do not train on one arm and test on another as if the data were independent.
- The worlds are simplified, so any gain is an upper bound for "pooling-drift learnability", not real-world ETA
  accuracy.
