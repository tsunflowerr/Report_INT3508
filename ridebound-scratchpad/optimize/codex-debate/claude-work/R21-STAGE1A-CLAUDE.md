# R21 Stage 1a: C-120 on the 34 T3.8 test cells, Claude's independent analysis

Written 2026-10-10 (~23:58 local) by a Claude analyst. Codex's `codex-work/R21-*` files were not read.
Plan: `tang3/t38c120/C120-PLAN.md` (sealed; amendment A1 fixes only the header time). Zero-run: no simulations were
run, and nothing under `C:/RideBoundData/research/*` or any repository was written.

Sources. Every number below comes from the files in `claude-work/r21-stage1a/`:
- `extract_stage1a.py` reads the 102 transcripts (U and C-30 via `forecast_family_a.run_dir("test", arm, cell)`, C-120 from
  `C:/RideBoundData/research/tier3-t38c120-v1/C-120-<cell>`). It reuses `audit_vep.load/audit`,
  `sweep_analyze.event_times`, the `display_layer` causal-no15 display exactly as `cap_vs_pad_frontier.py` applies it
  (D0 = `display(t0, p0, profile)` on the first drop promise), and `cumulative_decisive_check.analyze` for the
  prune-record classes. Its outputs are `stage1a-2026-10-10-riders.tsv` (7,159 accepted riders) and
  `stage1a-2026-10-10-runs.json` (102 runs).
- `report_stage1a.py` produces `stage1a-report-2026-10-10.txt`, cited below as **rep:N** (line N).
- `check_cum_witness.py` produces `cum-witness-check-2026-10-10.txt`, cited below as **cw:N**.
- Percentiles use the nearest-rank rule (`budget_use_check.q`). Shared ride means another served rider was on board
  the same vehicle at an overlapping time (the `q2_cap_dial.py` rule).

## 0. Validity and baseline reproduction

- All 34 runs in each arm have summary status `pass` and run-00 status `succeeded`, and all use the same inventory
  `0da63eaf…`. Each arm has 3,672 requests. Served rows equal lifecycle `completed` (U 2,434, C-30 2,338,
  C-120 2,387). No rider alighted without a promise. The causal-no15 forecast is active in 21 cells. My own prune
  classification matches `cumulative_decisive_check.analyze` in every run. All C-120 drop witnesses carry limit
  120000 ms (524 records); all C-30 witnesses carry 30000 ms (845 records) (rep:4-6).
- All 14 baselines from the brief reproduce exactly (rep:9-23): served 2,434 / 2,338; naive late > 60 s 203 / 76;
  late > 120 s 102 / 11; timely ≤ 60 s 2,231 / 2,262; timely ≤ 120 s 2,332 / 2,327; forecast late60 137 / 10;
  forecast timely60 2,297 / 2,328.
- Earlier outputs also reproduce: drop-exposed 174 / 33, C-30 S ≥ 0.9 B = 4, U max S 590.1 s, C-30 per-step-also 845,
  shared 22.80% / 13.39%, mean forecast extension 7.2 / 7.4 s (rep:76-79).

## 1. Outcomes vs the FIRST drop promise (3,672 requests per arm)

| arm | served (per req) | naive late > 60 s | late > 120 s | late > 300 s | early > 60 s | timely ≤ 60 s (per req) | timely ≤ 120 s (per req) |
|---|---|---|---|---|---|---|---|
| U | 2,434 (66.29%) | 203 (8.34%) | 102 (4.19%) | 18 (0.74%) | 7 (0.29%) | 2,231 (60.76%) | 2,332 (63.51%) |
| C-30 | 2,338 (63.67%) | 76 (3.25%) | 11 (0.47%) | 0 | 3 (0.13%) | 2,262 (61.60%) | 2,327 (63.37%) |
| **C-120** | **2,387 (65.01%)** | **132 (5.53%)** | **21 (0.88%)** | **0** | **1 (0.04%)** | **2,255 (61.41%)** | **2,366 (64.43%)** |

Late shares are per served rider (rep:27-29).

Forecast quote (causal-no15; naive in the 13 inactive cells) (rep:32-34):

| arm | fc late > 60 s | fc late > 120 s | fc late > 300 s | fc early > 60 s | fc timely ≤ 60 s (per req) | fc timely ≤ 120 s (per req) | mean quote extension |
|---|---|---|---|---|---|---|---|
| U | 137 (5.63%) | 87 (3.57%) | 17 | 8 (0.33%) | 2,297 (62.55%) | 2,347 (63.92%) | 7.18 s |
| C-30 | 10 (0.43%) | 0 | 0 | 4 (0.17%) | 2,328 (63.40%) | 2,338 (63.67%) | 7.37 s |
| **C-120** | **65 (2.72%)** | **8 (0.34%)** | **0** | **2 (0.08%)** | **2,322 (63.24%)** | **2,379 (64.79%)** | **7.27 s** |

## 2. Dispatch changes of the drop promise (accepted riders; S = Σ|c|) (rep:37-39)

| arm | accepted | drop-exposed | riders with ≥ 2 nonzero c | S among exposed: mean / p50 / p90 / max | S ≥ 0.9 B | S > B (overshoot) |
|---|---|---|---|---|---|---|
| U | 2,434 | 174 (7.15%) | 12 (max k 3) | 137.7 / 117.0 / 260.7 / 590.1 s | (no B) S ≥ 108 s: 96; S > 120 s: 86 | n/a |
| C-30 | 2,338 | 33 (1.41%) | 0 | 10.9 / 8.3 / 28.0 / 29.2 s | 4 (≥ 27 s) | 0 |
| **C-120** | 2,387 | **103 (4.32%)** | **0** | **55.5 / 62.5 / 104.9 / 118.9 s** | **9 (≥ 108 s)** | **0** (also 0 at +1 ms tolerance) |

In C-120, 54 riders used at least half of B. Every exposed rider was served.

## 3. Budget prune records and forced decisions (acknowledged decisions; recorded first-failing witness) (rep:42-47)

| arm | budget-pruned candidates | single-step (delta > B) | cumulative-only (before > 0, delta ≤ B < after) | non-normal (forced) decisions | forced-breach riders | acknowledged decisions |
|---|---|---|---|---|---|---|
| U | 0 | 0 | 0 | 0 | 0 | 20,760 |
| C-30 | 845 | 845 | 0 | 0 | 0 | 20,101 |
| **C-120** | **524** | **521** | **3** | **0** | **0** | 20,435 |

The 3 C-120 cumulative-only records each come from a different run, each in its own decision (rep:44-47, cw:2-7):

| run | before + delta = after (limit 120 s) | witness rider's final Σ\|c\| (k) | new request: C-120 / C-30 / U |
|---|---|---|---|
| d20181114-s10-r3-w08 | 25.8 + 99.0 = 124.9 s | 25.8 s (1) | not accepted / served / served |
| d20181115-s10-r1-w08 | 58.9 + 91.6 = 150.5 s | 58.9 s (1) | served / served / served |
| d20181118-s10-r3-w08 | 105.5 + 99.3 = 204.8 s | 105.5 s (1) | not accepted / not accepted / U served |

Caveat (`cumulative_decisive_check.py` docstring). The validator stops at the first failing rider, so these are
recorded witnesses: an upper bound on the decisions a per-step cap could have changed. This analysis does not show
that the cumulative clause caused either rejection. For comparison, the earlier check found 0 such records in T3.8
C-30 and in the w07/w07x C-30…C-300 measured runs (`r13-final-judge/cumulative-decisive-check-2026-10-10.txt:4-30`).
Cumulative-only records did appear before, but only in fixed-traffic WP14r C-60/C-120 runs and synthetic C-120
worlds (same file, lines 34-48).

## 4. Shared rides, served-set overlap, per window

- **Shared completions** (rep:50-52): U 555 (22.80% of served); C-30 313 (13.39%); **C-120 428 (17.93%)**.
- **Served-set overlap** (rep:55-58):

  | pair | common | only first | only second |
  |---|---|---|---|
  | C-120 vs C-30 | 2,266 | 121 | 72 |
  | C-120 vs U | 2,271 | 116 | 163 |
  | U vs C-30 | 2,207 | 227 | 131 |

  U also served 93 of the 121 C-120-only riders (vs C-30).
- **Per cell served** (rep:72-73): C-120 serves more than C-30 in 23 cells, the same in 8 and fewer in 3. Against U it
  serves more in 5 cells, the same in 11 and fewer in 18.
- **Per window** (rep:61-69; window requests w07 972, w08 1,512, w17 1,188):

  | window | served U / C-30 / C-120 | naive late > 60 s U / C-30 / C-120 | timely ≤ 60 s U / C-30 / C-120 |
  |---|---|---|---|
  | w07 | 516 / 511 / 515 | 70 / 61 / 63 | 446 / 450 / 452 |
  | w08 | 1,014 / 975 / 1,001 | 67 / 15 / 49 | 947 / 960 / 952 |
  | w17 | 904 / 852 / 871 | 66 / 0 / 20 | 838 / 852 / 851 |

## 5. Predictions P1–P5 (evaluated exactly as written in C120-PLAN.md) (rep:82-86)

| | prediction | value | verdict |
|---|---|---|---|
| P1 | all jobs pass; 0 non-normal decisions; 0 riders with Σ\|c\| > 120 s | 34/34 pass; 0; 0 (max 118.9 s) | **PASS** |
| P2 | served ≥ 2,362 | 2,387 (49 of the 96-rider gap) | **PASS** |
| P3 | 76 < naive late > 60 s < 203 | 132 | **PASS** |
| P4 | timely ≤ 120 s ≥ 2,327 | 2,366 | **PASS** |
| P5 | recorded cumulative-only drop-budget prune records ≤ 2 | 3 | **FAIL** |

## Plain-English reading

1. Allowing 120 s instead of 30 s per rider served 2,387 of 3,672 requests: 49 more than C-30 and 47 fewer than U. U is the measured no-budget run on these cells, not an upper bound.
2. Lateness against the first promise rose with the larger budget: 132 riders were late by more than 60 s (C-30 76, U 203) and 21 by more than 120 s (C-30 11, U 102). No rider was late by more than 300 s.
3. Timely completions per request: within 60 s, C-120 has 2,255 (C-30 2,262, U 2,231); within 120 s, it has 2,366, the most of the three (C-30 2,327, U 2,332). With the forecast quote, the 60 s count is 2,322 (C-30 2,328, U 2,297).
4. The budget held: 34/34 runs passed, there were 0 forced decisions, 0 riders went over 120 s (max 118.9 s) and no rider had two drop changes. 103 riders (4.32%) had a drop change, against 33 for C-30 and 174 for U.
5. P5 failed. Three prune records were rejected by the cumulative clause alone (the limit was ≤ 2). These records are upper bounds from first-failing witnesses, not proof that the clause changed an outcome. In two of the three cases the new request ended not accepted.
6. The cohorts differ. C-120 and C-30 share 2,266 served riders, with 121 and 72 unique to each, so their per-rider rates describe different rider sets. Shared rides (17.93%) fall between C-30 and U, and the extra service comes from w08 (+26) and w17 (+19), with w07 almost unchanged (+4).
