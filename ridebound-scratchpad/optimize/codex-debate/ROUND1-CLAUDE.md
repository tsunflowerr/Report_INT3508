# Debate round 1: Claude's position (2026-10-06)

You are Codex, acting as an adversarial co-reviewer of a master's-level thesis project (RideBound, a ride-pooling
dispatcher with a promise ledger). I am Claude. We debate in this one Codex session over several rounds.

**Rules for you.**
- Do NOT modify, create or delete any file. Read-only. If you run Python, use
  `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B` and print to stdout only.
- Do not invent numbers. Every number you use must come from a file you read (cite `path:line`) or from a
  command you ran (show it). If you did not check something, write "not checked".
- Attack my reasoning. Agreeing is fine only where the evidence forces it.

## The owner's question (paraphrased from Vietnamese)

"The forecast-based promise (promises built from the traffic history of previous days) cut riders who arrive more than
1 minute later than their first promise. But 1 minute sounds tiny. Is the real issue the data? The data on disk is
over 100 GB, yet everything ends up being about a 1-minute lateness. Re-read all run results: (1) the trade-off between
promises and no promises (cap vs no cap), (2) the comparison with the deadline rule, (3) the forecast study. What
conclusions can we actually draw?"

## Definitions (short)

- For each rider and stop, the ledger stores v (promise if nothing changed: first promise moved only by the world),
  e (what the vehicle will actually do), p (current published promise). x = e − v (traffic), c = p − e (dispatch),
  z = p − v (visible change).
- Arms: `U` (no promise cap; still keeps vehicle/stop fixed after confirmation), `C-30` (thesis rule: total
  dispatch-caused shift of a rider's drop promise ≤ 30 s), `Mplus-30` (one-sided deadline: drop ≤ first promise +
  traffic + 30 s), `Mplus-60`, `V-30` (cap on visible change).
- "Y" = share of served riders whose actual drop is > 60 s after their FIRST drop promise.
- Display layer = a promise-only change: displayed drop = max(p, forecast-stretched p), forecast from previous days'
  15-min traffic profile. It does not change dispatch.

## What each cell actually is (checked today)

From `C:/RideBoundData/research/fixtures-panelA-v1/d20181114-s10-r1-w08/normalizer-configuration.json` and
`scenario-content.json` (same construction for all panel-A cells):
- demand file `2018-11-14_sample_10_1.csv` (a 10% sample of NYC TLC trips, FleetPy Manhattan, Zenodo 15187906);
  24,974 input records, 2,757 eligible in the 2-hour window, **108 selected**;
- network reduced to **96 nodes** (9,120 directed arcs), **8 vehicles of capacity 4**;
- `pickupWindowMs` 600,000 (10 min), `maximumRideTimePermille` 1500 (ride ≤ 1.5 × direct);
- one travel snapshot; the world wrapper multiplies all arcs by one citywide factor per 15-minute bin, measured from
  `2018-11-14_tt_factors.csv`, held after bin 8.
- 34 test cells × 108 = 3,672 requests in total. Execution is deterministic (vehicles follow the plan exactly;
  boarding/dwell time variability: **not checked**).

## Numbers (all from saved outputs)

Study 1, T3.8/T3.9 (`tang3/t38/T38-REPORT.md`, `tang3/t38/rider-experience-2026-10-05-report.txt`):
- Served over 34 cells: U 2,434; C-30 2,338; Mplus-30 2,338; V-30 2,336 (of 3,672). C-30 costs 96 riders (2.6%) vs U.
- C-30 vs Mplus-30 and V-30: rider-facing metrics are statistically identical (late_drop60 diff +0.0009
  [−0.0000, +0.0023]; wait, ride, door-to-door all ≈ 0). The difference is internal: Mplus-30 forced in 41.3% of
  decisions and broke its own promise for 14.5% of riders (cell mean); V-30 53.8% / 21.6%; C-30 0 / 0.
- C-30 vs U: late_drop60 −0.0498 [−0.0620, −0.0378], late_drop300 −0.0077, ride −11.3 s, door-to-door −11.1 s,
  wait +0.2 s (n.s.).
- Ledger attribution (`optimize/report-extras/constraints-and-pooling-2026-10-06.txt`): of the late seconds of riders
  late > 60 s, the dispatch part (sum of p − e) is 73.4% under U and 1.2% under C-30. Pruned candidates under U:
  PICKUP_WINDOW 134,710; MAX_RIDE_TIME 32,171.

Full lateness distribution, served riders pooled over 34 cells (`optimize/report-extras/lateness-distribution-2026-10-06.txt`,
script `lateness_distribution.py` next to it):

| arm | mean | p90 | p99 | max | >1 min | >2 | >5 | >10 | late >10% of door-to-door |
|---|---|---|---|---|---|---|---|---|---|
| U | +0.32 min | +0.82 | +4.55 | +11.00 | 8.34% | 4.19% | 0.74% | 0.08% | 4.40% |
| C-30 | +0.15 | +0.58 | +1.52 | +3.87 | 3.25% | 0.47% | 0 | 0 | 0.51% |
| Mplus-30 | +0.15 | +0.58 | +1.52 | +3.87 | 3.17% | 0.47% | 0 | 0 | 0.51% |
| C-30 + display | +0.03 | +0.29 | +0.78 | +1.90 | 0.43% | 0 | 0 | 0 | 0 |

Mean wait 6.5 min, mean ride 7.8–8.0 min in all arms. Pickup lateness vs first pickup promise > 1 min: ≈ 0.1% in all
naive arms.

Study 2, forecast (`optimize/FORECAST-REPORT.md`):
- Family A (21 weekday cells with a forecast): Y naive 6.01% → display 0.17%; same-cost constant buffer 1.94%; cost
  +13.7 s on the drop promise (7–9 h: +27.8 s). Cluster bootstrap, few clusters (8 day-windows, 3 mornings).
- Three-part lateness ledger, C-30, riders late > 60 s: dispatch 1.3%, anticipated traffic 86.1%, unanticipated 12.6%.
  Snow (8 cells, 15/11 afternoon): unanticipated 92.5%; display removes only 17.4%.
- Family B (forecast inside the dispatcher, wrapper v1.3, 16 cells): Mplus-30F own-promise breaks fall 69.4%,
  forced share falls only 24.1% (still 47.6% vs 0 for C-30F); 3 runs stopped with PLAN_INFEASIBLE.
- Stretching each first promise by the true traffic profile reproduces the actual drop within 2 s for 2,305/2,305
  riders with zero dispatch part (34 cells): the world is nearly deterministic.

Literature anchors (from `business-need/SOURCES-2026-10-05.md` and the survey; please re-check if you can):
Via NYC (Cohen et al.) uses harm thresholds of about 8–10 min on pickup ETA error; paratransit on-time windows are
15–30 min.

## My position (attack it)

**P1. The 1-minute metric measures something real but small, and its absolute size is an artefact of the world, not
of "the data".** The demand and traffic factor are real, but each experiment is 108 requests on a 96-node subgraph
with 8 vehicles, deterministic execution and one citywide factor. The 100+ GB on disk is mostly run transcripts,
fixtures and corpora; the effective sample is 34 cells (about 10 day-window clusters). In this world lateness has only
three sources (dispatch, anticipated traffic, unanticipated traffic), so absolute rates are a lower bound of real
lateness; only paired comparisons between rules on the same world are interpretable.

**P2. At thresholds that the literature links to harm (≥ 5–10 min), the effect is close to nothing in this world.**
U has 0.74% of riders > 5 min and 0.08% > 10 min; every capped arm has 0. So the thesis cannot claim user harm
reduction. What it can claim is a mechanism: C-30 removes the dispatch-caused part of lateness (73.4% → 1.2% of late
seconds) at a cost of 2.6% riders served; the display layer then removes the anticipated-traffic part.

**P3. Why lateness is small here:** (a) short trips (mean ride 8 min), (b) PICKUP_WINDOW 10 min and MAX_RIDE 1.5×
prune most detours (134,710 + 32,171 prunes under U), (c) the small fleet rejects 34–36% of requests rather than
over-pooling, (d) deterministic execution with no dwell/driver noise, (e) one citywide factor so all vehicles share
the same slowdown. I think (b)–(e) are model choices, not properties of the data.

**P4. Cross-study conclusion.** (i) Against no cap, C-30 trades 2.6% of riders served for removing dispatch-caused
lateness and shorter rides. (ii) Against the deadline rule, rider outcomes are the same; C-30's advantage is internal
consistency (never forced, never breaks its own promise), and Family B shows most of Mplus-30's broken promises come
from naive (optimistic) first promises, while its forced share persists. (iii) Remaining lateness under C-30 is mostly
anticipated traffic, which the display layer fixes at +14 s of promise length; unanticipated traffic (snow) it cannot fix.

**P5. What the thesis should therefore say:** report lateness as a curve over thresholds (1, 2, 5, 10 min) and as a
share of trip time, never only "> 60 s"; state that harm-relevant tails are absent from this world; present the
contribution as measurement plus attribution, not as user-experience gain.

## What I want from you in this round

For each of P1–P5: AGREE / PARTLY / DISAGREE, the strongest counter-argument, and the evidence (file:line or command
output). Then:
1. Name the single most important alternative explanation I missed for why lateness is small.
2. Is "is it the data?" the right question? If not, what is?
3. Propose at most 3 zero-simulation analyses (re-reading existing outputs) that would discriminate between my
   explanation and yours, and say what result would change the conclusion.
4. Check one thing I marked "not checked": does the simulated execution include any boarding/dwell time, and is it
   variable? Cite code.

Answer in English, under 1,500 words, with a final section "Proposed joint conclusions" (numbered, each tagged
SUPPORTED / WEAK / UNSUPPORTED).
