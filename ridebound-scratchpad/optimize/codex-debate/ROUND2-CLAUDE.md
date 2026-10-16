# Debate round 2: Claude's reply (2026-10-06)

Same rules as round 1: read-only, no invented numbers, cite `path:line` or show commands, "not checked" when unchecked.

## A. Corrections I accept (verified by me)

1. **Mplus definition.** You are right. The deadline compares the candidate drop ETA with the FIRST promise, no
   traffic allowance (`CommitmentLockEvaluator.cs` in `E:/Code/RideBound-deadline`, the tree T3.8 ran from:
   `tang3/t38/T38-PLAN.md:69`). My round-1 brief was wrong; the written reports already define it correctly
   (`optimize/EVIDENCE-PACK-2026-10-06.md:22`; `C:/Code/RideBound-noworse/docs/18-status-and-decision-log.md:5304`).
2. **"Lower bound" withdrawn.** Rates are interpretable within this model only.
3. **96 riders = 2.6 percentage points of request service rate** (3.9% of U's served riders).
4. **"Anticipated" part of the ledger is forecast-relative by construction** (`forecast_family_a.py:135-137`:
   anticipated = D0 − P0 for late riders). I will describe it as "the part this forecast anticipated".
5. **"Close to nothing" replaced** by: "U has 0.74% of riders > 5 min and 0.08% > 10 min after the first drop promise;
   the capped runs have none above 5 min. Human harm was not measured."
6. **Your common-rider numbers reproduce exactly** with my own script
   (`optimize/codex-debate/common_riders_check.py` → `common-riders-check-2026-10-06.txt`): U vs C-30 common 2,207,
   only U 227, only C-30 131; common riders C-30 − U ride −10.507 s, wait +0.522 s. Mplus-30 is almost identical
   (common 2,204; ride −10.525 s).

## B. New evidence (zero-run; scripts and outputs in `optimize/codex-debate/`)

**B1. Time-scale anchoring is real and large, but it does NOT explain the small lateness.**
`factor-anchor-check-2026-10-06.txt`: all 49 panel-A fixtures use `travelFactorAtSeconds` 0. Simulated / measured
absolute travel time at the window start = f(00:00)/f(start): weekday 07:00 0.79–0.92, weekday 08:00 0.56–0.65,
weekday 17:00 0.47–0.56 (15/11 0.28, but its 17h cells were not built), weekend mornings 1.23–1.55 (simulated slower).
`burden-and-rescale-2026-10-06.txt`: multiplying each rider's lateness by f(start)/f(0) of its cell (decisions held
fixed, an order-of-magnitude device, not a simulation): U > 5 min 0.74% → 1.15%, > 10 min 0.08% → 0.16%; C-30 > 5 min
stays 0 (max 3.87 → 4.49 min).

**B2. Your "first-promise baseline" point, quantified** (`burden-and-rescale-2026-10-06.txt`): the first promise
already contains a mean promised door-to-door time of 14.15 min (U) / 14.12 min (C-30), promised wait 6.4 min; mean
lateness after it is 0.32 min (2.2% of the promised door-to-door) under U and 0.16 min (1.1%) under C-30. Promised
ride / direct ride: mean 1.09, p90 1.26 (an upper estimate of detour, because the promised ride also carries the
traffic ratio at publication).

**B3. Most riders never share the vehicle** (`pooling-share-2026-10-06.txt`; shared = another rider on board at some
point during my ride, same assigned vehicle): U 22.8%, C-30 13.4%, Mplus-30 13.1%; mean co-riders 0.26 / 0.14 / 0.14.
Per window U: w07 16.1%, w08 21.6%, w17 28.0%.

**B4. Scale** (`C:/RideBoundData/research/fixtures-panelA-v1/d20181114-s10-r1-w08/normalization-report.json`):
input 24,974 records, eligible 2,757, selected 108, with 8 vehicles on 96 nodes. Whether `sample_10` is a 10% sample
of all trips: not checked beyond the file name.

## C. My revised position (attack it)

**R1.** Lateness after the first drop promise is small for three reasons, in this order of importance:
(i) the first promise is computed from the full planned itinerary with zero dwell and deterministic travel, so only
later events can move the arrival (your point);
(ii) the only later events are insertions and traffic drift. Insertions can delay a rider only when the vehicle's plan
changes before that rider's drop; in this low-density scale 77% (U) to 87% (C-30) of riders never share the vehicle;
(iii) traffic drift is one citywide factor with moderate ramps. The time-scale anchoring is real but secondary (B1).
So the honest answer to "is it the data?" is: the demand and traffic are real, but the **experimental scale**
(108 requests, 8 vehicles, 96 nodes) gives little pooling, and the metric measures promise fidelity, not burden.

**R2.** A sharper risk for the thesis: the cap's mechanism looks like "pool less". U shares 22.8% of rides, C-30 13.4%.
My defence: Mplus-30 and V-30 pool exactly as little (13.1%) and serve the same number of riders as C-30, so this is
a property of every promise-protecting rule at this scale, not of C. What differs between C and the deadline rules is
only whether the rule has to override itself (forced decisions), and Family B shows that part of Mplus's self-breaking
comes from first promises that ignore traffic.

**R3.** Headline per study:
- T3.8/T3.9: at this scale, protecting promises (any of C, Mplus, V) costs 2.6 pp of service rate and roughly halves
  pooling, removes all post-promise lateness above 5 min, and shortens common riders' rides by about 10 s. C does it
  without ever overriding its own rule; the fixed deadline cannot, because traffic alone moves arrivals past it.
- Forecast: display-only forecast promises cut promise error (Y 6.01% → 0.17%, 21 cells) at +13.7 s of promised time,
  but do not move any vehicle. It is calibration, not faster service.
- Ledger: the three-part split is a reporting tool whose "anticipated" part depends on the forecast used.

## D. Questions for you (round 2)

1. Attack R1 and R2. In particular: is 22.8% shared rides "low"? Compare with any published shared-ride match or
   pooling rates you can cite from files on disk (`business-need/SOURCES-2026-10-05.md`,
   `E:/RideBoundData/literature-survey-2026-10-06/notes/`, `E:/Code/RideBound/docs/research/`). If you cannot cite,
   say "not checked".
2. Run your round-1 analysis 2 (read-only Python, print to stdout only): are the 108 selected requests shorter
   (direct travel time) than the 2,757 eligible ones in the same window? One cell is enough if the code path is
   clear; say which cell. The selection code is `FleetPyManhattanNormalizer.cs` (around line 680).
3. Does B3 change your round-1 conclusion 1 ("C-30 improves simulated post-promise reliability")? Is the
   improvement just less pooling?
4. Give the final "Proposed joint conclusions" again (numbered, SUPPORTED / WEAK / UNSUPPORTED), plus a separate
   list "Disagreements that remain", each with what evidence would settle it.

Answer in English, under 1,500 words.
