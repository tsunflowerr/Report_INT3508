# R19 independent Stage 1a results

2026-10-10T17:00:50.261365+00:00

{
  "P1": {
    "pass_": true,
    "all_summaries_pass": true,
    "non_normal": 0,
    "overshoots": 0
  },
  "P2": {
    "pass_": true,
    "value": 2387,
    "threshold": 2362
  },
  "P3": {
    "pass_": true,
    "value": 132,
    "strict_bounds": [
      76,
      203
    ]
  },
  "P4": {
    "pass_": true,
    "value": 2366,
    "threshold": 2327
  },
  "P5": {
    "pass_": false,
    "value": 3,
    "threshold": 2,
    "unclassified_or_other_budget": 0
  }
}

| Arm | Served | Forced/non-normal | Overshoot riders | Drop-exposed | >=2 changes | Recorded cumulative-only |
|---|---:|---:|---:|---:|---:|---:|
| C-120 | 2387 | 0 | 0 | 103 | 0 | 3 |
| C-30 | 2338 | 0 | 0 | 33 | 0 | 0 |
| U | 2434 | 0 | 0 | 174 | 12 | 0 |

| Arm / quote | Late>60 | Late>120 | Late>300 | Timely60 / 3672 | Timely120 / 3672 | Mean extension s | Early>60 |
|---|---:|---:|---:|---:|---:|---:|---:|
| C-120 / naive | 132 | 21 | 0 | 2255/3672 | 2366/3672 | 0.0 | 1 |
| C-120 / causal-no15 | 65 | 8 | 0 | 2322/3672 | 2379/3672 | 7.273884592652162 | 2 |
| C-30 / naive | 76 | 11 | 0 | 2262/3672 | 2327/3672 | 0.0 | 3 |
| C-30 / causal-no15 | 10 | 0 | 0 | 2328/3672 | 2338/3672 | 7.3671234456626165 | 4 |
| U / naive | 203 | 102 | 18 | 2231/3672 | 2332/3672 | 0.0 | 7 |
| U / causal-no15 | 137 | 87 | 17 | 2297/3672 | 2347/3672 | 7.183331055723637 | 8 |

Served-set overlaps: [{"left": "C-120", "right": "C-30", "common": 2266, "left_only": 121, "right_only": 72}, {"left": "C-120", "right": "U", "common": 2271, "left_only": 116, "right_only": 163}, {"left": "C-30", "right": "U", "common": 2207, "left_only": 131, "right_only": 227}]

forecast is frozen display replay, no redispatch
recorded fail-fast witnesses do not enumerate all blockers or counterfactual routes
model projection attribution is not complete real-world causal identification
34 cells are dependent across five dates; no population guarantee
non-normal decisions are certificate counts; incident entries are reported separately
