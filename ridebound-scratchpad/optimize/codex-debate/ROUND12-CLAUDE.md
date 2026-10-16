# Round 12 (2026-10-09): strong published baselines, and two fact checks

The owner wants the thesis compared against a **stronger baseline taken from a published paper and implementable in
the same system**, so the comparison is fair. They also note that we have not really discussed **traffic forecasting
methods** themselves. Effort is now **xhigh** (not ultra).

Same rules:
- write only in `codex-work/`;
- read anything; web allowed;
- zero hallucination: cite `file:line`, or a URL with a verbatim quote and page;
- outputs in mode "x";
- no simulation runs.

## Owner questions to answer with evidence

**Q2. Under rule C, are riders really rarely charged extra time when new riders are inserted?** Claude's facts:

| Source | Statistic | Value |
|---|---|---|
| T3.8 C-30 (`exposure-check-2026-10-06.txt`) | drop-exposed (any nonzero dispatch c) | 1.4% (33/2,338) |
| T3.8 C-30 (`report-extras/constraints-and-pooling-2026-10-06.txt`) | nonzero dispatch revisions | 33; median 8.3 s, p90 28.0 s, max 29.2 s |
| T3.8 U, same two files | drop-exposed | 7.1% |
| T3.8 U, same two files | nonzero dispatch revisions | 187; median 108.6 s |
| `budget-block-diagnosis-2026-10-07.txt` | rejections blocked only by the budget | 148 (U served 116 of them); overshoot median 110 s |
| WP14r | exposure, FREE vs C-30 | 23.8% vs 0.4% |

**Q3. How exactly is the first promise computed, and is the low lateness "the data"?** Claude's reading:
- The first promise is the projected schedule of the chosen plan
  (`C:/Code/RideBound-noworse/src/RideBound.Application/Scheduling/RouteScheduleProjector.cs:103-141`, and
  `GetServiceStart` at :151-166).
- The projection starts from the vehicle's current position and walks the remaining stops in planned order. It uses
  the **current** travel-time snapshot. Service start is max(arrival, earliest pickup) for pickups. Service duration
  is 0.
- `PromiseProjector.cs:63-131` takes the pickup and drop service starts as the promise.
- The simulator then executes the same plan deterministically. So the error comes only from later traffic change and
  later dispatch change; there is no dwell, driver or GPS noise.

Please verify or correct both readings.

## Main task: strong baseline(s) → `codex-work/STRONG-BASELINE-CODEX.md` (≤ 1,500 words)

### A. Traffic and ETA prediction for the promise's traffic part

Survey, from primary sources, standard **short-term traffic or travel-time forecasting baselines** that can be applied
to our signal: one citywide 15-min travel-time factor series, 8 days (11–18/11/2018, 96 bins/day; 11/11 hourly only).
Candidates:
- seasonal naive;
- historical average (our current method);
- (seasonal) ARIMA, e.g. Williams & Hoel 2003;
- exponential smoothing;
- Kalman-filter or real-time-corrected historical profiles;
- k-NN pattern matching;
- gradient boosting;
- LSTM or graph models.

For each, give: the paper, what it forecasts, the data it needs, whether it is fair and feasible with 8 days, and its
expected strength. Include our earlier factor-level error table (`optimize/forecast-predictability-2026-10-06.txt`).
Also state the **headroom**: on weekdays the oracle-stretch already reproduces arrivals (1,452/1,452 within 2 s;
FORECAST-REPORT:77), and the historical profile gives late60 0.17% vs about 0% for the oracle. The incident day
(snow, 15/11) is where the headroom is large.

### B. Promise and dispatch rules from papers that are implementable in our runner

Map these to our arms or configs:
- Schulz & Pfeiffer 2026 deadline (= our Mplus?);
- Hörl & Zwick 2022 strategy B;
- Fielbaum & Alonso-Mora 2020 controlled scenarios;
- Alonso-Mora 2017 latest-pickup tightening;
- UberX Share "added pickups won't increase your estimated arrival time";
- any other strong rule you find.

For each, say whether it is **already** represented (cite the config and code), implementable by configuration only,
or needs core code.

### C. Recommend ONE fair strong-baseline comparison

Prefer zero-run, i.e. replay of existing runs. Give the exact method, the fairness conditions (same information at
promise time, chronological fit, matched quote cost), the predictions you would seal, and what result would matter for
the thesis.

Finish with a short message listing the files you wrote.
