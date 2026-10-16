# Round 16 fact pack (neutral; read by Claude agents, Codex and Antigravity)

Written by Claude (main session) 2026-10-10 ~16:10. Background: `ROUND13-FACT-PACK.md`, the final verdict
`claude-work/R13-FINAL-VERDICT.md`, and Codex's corrections `codex-work/R15-CONFIRM-CODEX.md` (its 8 corrections
override the verdict's wording). All paths below are under
`E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/` unless absolute.

## 0. The owner's new questions (translated faithfully)

After reading the round 13–15 result ("keep the storyline; next step = one zero-run results chapter; optional
cost-first selection study later"), the owner asked:

- **Q1.** "So your and Codex's conclusion is that there is no new direction and no optimization of any part left,
  and we should only re-optimize outputs we already ran, keeping the current promise method? Explain WHY keep this
  direction."
- **Q2.** "If we loosen the cap so that the 1,256 candidates that exceeded the budget in a single move become feasible
  at the first attempt, would that be better?"
- **Q3.** "You say the cumulative part acted in only 7 decisions in total. Doesn't that mean the cumulative part of our
  system has had no effect?"
- **Q4.** "If we switch the selection to optimize cost first, would the results be different?"
- **Q5.** "If there is a better direction for forecast + rule C, is it to optimize the days with unpredictable external
  events? How would we do that? Can we upgrade our current traffic prediction with a different approach based on this
  specific data source, while staying FAIR? If more data is needed, can we use this same city's data from earlier
  years — the data that Alonso-Mora's own system used in the 2020 paper? Is that feasible?"
- **Q6 (method).** Codex, Claude and Antigravity (Gemini 3.8 Flash, high) debate without bias, tell the truth
  objectively, and judge by the standard of a strict reviewer at an international conference / top journal.

## 1. Facts already established (with anchors)

**Rule and baselines.**
- v/e/p ledger: x = e − v (traffic), c = p − e (dispatch), z = p − v. Rule C: per rider Σ|c| ≤ B. M⁺: p − p0 ≤ B
  (deadline from first quote, traffic included). U: locks, no drop cap. FREE: `rolling-cost`, no locks.
- U and C share the stability-first ordered objective: forced-reference → accepted count → worst hard utilisation →
  decision-induced revisions → operational cost (`C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:283-303,319-331,365-368`).
  The utilisation level is saturated in 3,503/3,503 U and 3,506/3,506 C-30 T3.8 decisions
  (`claude-work/r13-final-judge/objective-levels-check-2026-10-10.txt`). FREE is cost-first. No current config gives
  "hard cap + cost-first" (fixed-freeze strips hard limits).

**The cumulative clause (Q3).** Across 98 enforced-C runs with measured traffic factors (T3.8 C-30 ×34; w07/w07x
C-30…C-300 ×64), 64,371 acknowledged decisions, all 1,256 recorded drop-budget prunings report a single increment > B;
0 cumulative-only. Fixed traffic (WP14r): 6 cumulative-only records in 4 decisions (all new requests eventually
served). Synthetic C-120: 4 records in 3 decisions (one request eventually rejected). Validator is fail-fast (first
failing rider only). Reproduced independently by Codex (`codex-work/R15-audit-summary.txt`). Under every C arm on
measured traffic, no rider had two nonzero dispatch changes; under U (T3.8) 12/2,434 riders had ≥2; under FREE (WP14r)
50/1,629 (3.07%).

**What the 1,256 are (Q2).** They are candidate records, not riders. In T3.8 C-30, 845 budget-pruned candidates;
148 requests were rejected ONLY because of a co-rider's budget (U served 116 of them); smallest overshoot median
109.6 s, p25 63.7, p75 183.6, max 524.8; first-order, a cap of 60 / 120 / 300 s would let 11 / 59 / 135 of the 148
pass (`claude-work/budget-block-diagnosis-2026-10-07.txt:1-10`). 1,186 rejections were structural (pickup window /
max ride), not budget.

**Existing cap dial (Q2), served riders:**
- w07, 8 cells 07–09 h, measured traffic, 864 requests (`tang3/w07x/W07X-REPORT.md`): U 665; C-30 660, C-60 661,
  C-90 664, C-120 666, C-150 666, C-180 666, C-240 665, C-300 665. Budget-pruned candidates fall 142 → 106 → 71 → 38 →
  26 → 18 → 6 → 4 as the cap grows, but served barely moves.
- WP14r fixed traffic, 16 cells, 1,728 requests (`claude-work/wp14r-ladder-reanalysis-2026-10-08.txt`): FREE 1,629,
  LOCKS 1,584, C-120 1,563, C-60 1,540, C-30 1,534; late > 60 s vs first promise 274 / 47 / 23 / 0 / 0.
- T3.8, 34 cells, measured traffic, 3,672 requests: U 2,434, C-30 2,338, M⁺-30 2,338, M⁺-60 2,347. No C-60/C-120 on
  this panel (the panel where C-30 loses the most: −39 riders at 08–10 h, −52 at 17–19 h, −5 at 07–09 h).

**Promise outcomes on T3.8 (Q1, Q5)** (`claude-work/cap-vs-pad-frontier-2026-10-07.txt`), per 3,672 requests:
timely (≤ 60 s late vs first displayed promise) completions: U 2,231; C-30 2,262; U+forecast 2,297; C-30+forecast
2,328; M⁺-30+forecast 2,328; U+forecast+30 s pad 2,328 (late among served 4.35% vs 0.43%; quote +37.2 s vs +7.4 s;
early > 60 s 1.81% vs 0.17%). At ≤ 120 s: padded U 2,366 vs C 2,338.

**Forecast and the unpredictable day (Q5)** (`optimize/FORECAST-REPORT.md`): forecast = historical 15-min growth
profile (mean of fit days), added to the first quote. Weekday C-30 late > 60 s 6.01% → 0.17% (21 cells; 2 of 1,471
riders remain). Snow afternoon 15 Nov (w14/w15): 7.19% → 5.94%; 92.5% of late seconds "unanticipated". A damped-trend
(Gardner & McKenzie 1985) nowcasting replay protocol exists but was never run (`codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md`;
retrospective: dates already inspected).

**Data for a better forecast (Q5)** (`claude-work/R13-ML-DATA-CLAUDE.md`):
- The simulator uses ONE city-wide 15-min travel-time factor; bundle has 15-min factors for 12–18 Nov 2018 only
  (7 days), hourly for 11–18 Nov. The factor method is published (Syed et al. 2021, supplement eq. S1: total recorded
  duration ÷ total free-flow duration of trips starting in each 15-min bin, speed filter 1–30 m/s), so it can be
  rebuilt from raw taxi trips for other weeks/years.
- NYC TLC yellow taxi trip records exist from 2009 (TLC user guide); Nov 2018 alone has 8,155,449 rows.
- The two fit days of the current forecast are unusual: 12 Nov 2018 is Veterans Day (observed holiday), 13 Nov had
  26.9 mm rain (NOAA, saved sample).
- Sep–Dec 2018 has only one weekday with ≥ 1 inch snow (15 Nov); Jul 2016–Feb 2020 has 7 weekdays with ≥ 3 inches.
- The world wrappers read factor files only from the bundle (`tang3/world/preflight_world.py:51-55,71`); simulating a
  NEW day needs a new wrapper version, new factor files and new demand files (unverified whether the preflight
  accepts them).
- Fielbaum & Alonso-Mora 2020 used the public NYC taxi trips on Manhattan's network (4,091 nodes, 9,453 edges),
  15/01/2013 13–15 h (and ten weekdays from 14/01/2013), 2,000 vehicles, ~19,610 requests, and chose the off-peak
  period precisely so that "traveling times are somewhat stable, which allows us to disregard unreliability due to
  traffic conditions" (owner PDF `C:/PDF/Paper/Unreliability_in_ridesharing_systems_Measuring_cha.pdf`, text extraction
  lines 571-576).

**Claim boundary.** The owner's stricter copy `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (READ ONLY)
forbids claiming as new: detecting unreliability, pre-decision control, the service–stability trade-off, forecast
quoting, ML ETA, per-rider/proportional limits, guarantees.

## 2. Constraints (unchanged)

Zero hallucination (cite file:line or URL + short quote; mark UNVERIFIED). No simulation runs, no builds, no installs,
no deletions. Never write to `E:/Code/RideBound`, `E:/Code/RideBound-deadline`, `C:/Code/RideBound-noworse`, the thesis
`E:/Code/Report_INT3508/ridebound/`, or the internship report at the root of `E:/Code/Report_INT3508`. Deadline
reportedly mid-November 2026 (UNCONFIRMED). The owner wants ONE storyline and at most one next step, but explicitly
asks whether a better direction exists — answer honestly, including "yes, change direction" if the evidence says so.
