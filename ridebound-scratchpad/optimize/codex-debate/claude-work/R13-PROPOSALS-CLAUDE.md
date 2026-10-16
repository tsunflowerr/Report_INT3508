# R13 proposals: Claude side (proposer)

Written 2026-10-10 by the Claude-side proposer agent, for the owner's questions O2, O3, O5 and O6
(O1 and O4 are answered in the fact pack). All facts are cited by `file:line`; numbers marked [my arithmetic] are
derived from cited numbers; UNVERIFIED marks anything I could not check.

**Inputs read.**
- The fact pack, the handoff, and the three Claude-side R13 files (papers, survey, ML data).
- Both budget-use outputs, plus the older diagnosis, screen and runtime files.
- IDEAS-CLAUDE and codex-work/IDEAS-CODEX.md (round 4), AGREED-DIRECTION, JOINT-CONCLUSIONS-2026-10-07 and
  codex-work/STRONG-BASELINE-CODEX.md.
- The FORECAST, T38 and W07X reports.
- Both claim-boundary copies. The owner's stricter copy governs.
- Dispatcher code in `C:/Code/RideBound-noworse/src` (read-only).

**Independence.** I opened no `codex-work/R13-*` file and no `r13-*` folder in codex-work, and I did not open
`ROUND13-CODEX-final-message.md`.

**What I ran and wrote.** No simulation, build, install or deletion. I wrote this file and `claude-work/r13-proposer/`,
which holds 3 read-only scripts, 3 outputs and 2 run logs.

**Short names used for anchors.** Paths in the first block are relative to
`E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/`.

| Short | Path |
|---|---|
| FP | `ROUND13-FACT-PACK.md` |
| PAP | `claude-work/R13-PAPERS-CLAUDE.md` |
| SUR | `claude-work/R13-SURVEY-CLAUDE.md` |
| MLD | `claude-work/R13-ML-DATA-CLAUDE.md` |
| S3 | `claude-work/SURVEY-S3-cap-value-and-pooling-regime.md` |
| CVP | `claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` (new) |
| TIER | `claude-work/r13-proposer/tier-budget-screen-2026-10-10.txt` (new) |
| PROBE | `claude-work/r13-proposer/probe-event-kinds-2026-10-10.txt` (new) |
| BUC | `claude-work/budget-use-check-2026-10-09.txt` |
| WBU | `claude-work/wp14r-budget-use-2026-10-10.txt` |
| LAD | `claude-work/wp14r-ladder-reanalysis-2026-10-08.txt` |
| CVPAD | `claude-work/cap-vs-pad-frontier-2026-10-07.txt` |

| Short | Absolute path |
|---|---|
| HO | `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md` |
| LATE | `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/lateness-distribution-2026-10-06.txt` |
| FR | `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md` |
| T38 | `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md` |
| SRC | `C:/Code/RideBound-noworse/src` |
| D03 | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (owner's stricter copy, read-only) |
| BNA | `E:/Code/RideBound/docs/research/ridebound-business-need-audit-2026-10-05.md` (read-only) |
| W14R | `C:/Code/RideBound-noworse/docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md` |

---

## 0. Bottom line

1. **Recommended single direction: P1.** Keep the storyline, but state its business value as *the price of a pooled
   drop-off guarantee*. The three pieces each have a job:
   - rule C caps what the operator controls;
   - the forecast puts anticipated traffic into the quote;
   - the ledger settles the rest.

   The price can be computed now from saved runs. At most 68 runs with existing configs fill the measured-traffic gaps.
2. **The central weakness is real, and a new zero-run check sharpens it (F1).** At B = 30 s, the cumulative budget
   behaves exactly like a per-insertion cap in all 7 populations checked.
   - Riders for whom only the cumulative rule would bind: 0–2 per population (CVP:5,10,15,20,25,30,35).
   - The two rules start to differ only at B ≥ 120 s, and only under free (cost-first) dispatch: 0.69–1.04% of riders
     (CVP:7,22,32).
   - **Consequence:** treat the dispatch-only charge (traffic excluded) as the working mechanism, not cumulativeness.
3. **New code fact (F3): U is not free pooling.**
   - U and C both choose with a stability-first ordered objective: dispatch-caused ETA changes are minimised before
     operational cost.
   - FREE is cost-first.
   - This is the likely reason why exposure is low and why accumulation never happens. It also gives the cleanest
     "optimise one pipeline step" proposal (P3).
4. **The price of the cap (F4) [my arithmetic]:**
   - about 0.8–1.1 riders not served per late rider avoided at 1–2-minute thresholds;
   - only about 0.20 for the step from free pooling to locks;
   - at a 5-minute threshold the cap buys almost nothing, because U already has only 0.74% of riders that late.
5. **O5: more data for ML is not worth it** as a contribution. With the forecast, 2 of 1,471 weekday riders are still
   late; the only large remainder is one snow event (MLD:284-298).

---

## 1. New zero-run facts produced for this round

### F1. When do a cumulative cap and a per-insertion cap decide differently?

Script `r13-proposer/cumulative_vs_perinsertion.py` reads the same ledger rows as `budget_use_check.py`, through the
unchanged reader `forecast_family_a.audit_vep.audit`. Output: CVP.

**Definition.** A rider is *cumulative-only* at budget B when every single dispatch change is ≤ B but their sum is > B.
Only for these riders would rule C and a per-insertion cap of the same B decide differently.

**How to read it.** These are exposure counts in arms that did *not* enforce the cap; the c1 arms enforce 30 s. Under
an enforced cap the decisions would differ, so this is a screen, not a policy result.

| Population (existing runs) | Accepted riders | Drop-exposed | Riders with ≥ 2 nonzero changes | Cumulative-only riders at B = 30 / 60 / 120 / 300 s |
|---|---|---|---|---|
| WP14r FREE `b1-ref`, 8 vehicles, fixed traffic | 1,629 | 23.82% | 50 (3.07%) | 2 / 0 / 13 / 6 (CVP:4-8) |
| WP14r LOCKS `c1-nobudget` | 1,584 | 3.91% | 3 (0.19%) | 0 / 0 / 0 / 0 (CVP:9-13) |
| T3.8 U, 8 vehicles, measured traffic | 2,434 | 7.15% | 12 (0.49%) | 0 / 0 / 4 / 0 (CVP:14-18) |
| WP9 panel B `b1` (free type), 4 vehicles, older runner | 966 | 26.92% | 38 (3.93%) | 0 / 0 / 10 / 10 (CVP:19-23) |
| WP9 panel B `c1` (C-30 + locks), 4 vehicles | 860 | 2.91% | 0 | 0 / 0 / 0 / 0 (CVP:24-28) |
| WP9 panel A `b1`, 8 vehicles | 1,735 | 23.23% | 71 (4.09%) | 0 / 1 / 12 / 18 (CVP:29-33) |
| WP9 panel A `c1`, 8 vehicles | 1,581 | 0.70% | 0 | 0 / 0 / 0 / 0 (CVP:34-38) |

**Reading.**
- **At 30 s, a dispatch move almost always exceeds 30 s in one step.** The median nonzero move under U is 108.6 s
  (HO:220). So the per-step limit is hit first, and the "cumulative" clause adds a worst-case guarantee, not a different
  decision.
- **Higher load alone does not make accumulation appear** under the stability-first dispatcher. WP9 `c1` at 4 vehicles
  has 0 of 860 riders with two changes (CVP:24). Caveat: this is the older runner.

### F2. First-order screen of a two-class promise ("express" riders keep C-30, the others are U-like)

Script `r13-proposer/tier_budget_screen.py`. It uses the same candidate source as `budget_block_diagnosis.py` and
`proportional_budget_screen.py`. Riders are drawn into the express class by a deterministic hash. The screen ignores
knock-on effects and uses C-30's own candidate set.

- 148 requests were blocked only by a co-rider's budget, through 193 rejected candidates. **Each of the 193 is blocked by
  exactly one co-rider** (TIER:1).
- How many of the 148 would have at least one passing candidate:

  | Express share | Requests with a passing candidate (of 148) | Of those, served by U |
  |---|---|---|
  | 10% | 131 | 101 |
  | 20% | 114 | 85 |
  | 30% | 99 | 72 |
  | 50% | 65 | 48 |

  Source: TIER:3-6. The end points check the script: share 0 gives 148 and share 1 gives 0 (TIER:2,7).

### F3. Code facts about the dispatcher's objective and per-rider policies (read-only)

**1. U and C use the same policy.**
- Both run `policyId` `ridebound-hard-vector` (`tang3/configs/wp4-tier3-v2.json:3`). Every arm gets the same WP4 file
  (`tang3/t38/run_t38.py:92-93`).
- U keeps zero hard limits on the vehicle, pickup-stop and drop-stop switch counts (`tang3/configs/U.json:33-40,49-51,65-66`).
  So the hard-vector objective branch is active for U as well (`SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271-272`).

**2. The hard-vector objective is ordered.** Each level is used only to break ties at the level above:
1. forced-reference count;
2. accepted-request count, maximised;
3. worst hard utilisation;
4. every decision-induced revision dimension, in vocabulary order (pickup ETA total, drop ETA total, …);
5. operational cost;
6. an ID tie-break.

Sources: `SolverBackedFleetSelection.cs:283-303,319-331,365-385`; order in `SRC/RideBound.Domain/Commitments/CommitmentDimension.cs:19-32`.

**3. My reading of what this means** (from the code, not instrumented):
- A zero hard limit sets a vehicle's worst utilisation to the maximum for any active rider
  (`SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:612-626`). So level 3 barely separates
  candidates.
- In effect, after "accept as many as possible", the next rule is "move existing riders' ETAs as little as possible".
  Cost only breaks the remaining ties.

**4. FREE is cost-first.**
- FREE (WP14r `b1-ref`) is `policyId` `rolling-cost` (`codex-work/round8-free-wp4-candidate.json:3`).
- Its objective profile is `RollingCost` (`SRC/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:287`):
  accepted count, then cost.

**5. "Hard budget + cost-first" is not available by configuration.** The fixed-freeze-horizon policy keeps the
`RollingCost` profile, but its policy provider strips every hard limit and every confirmation lock
(`SolverBackedRidePoolingPolicy.cs:308-321`; `SRC/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:97-108`).

**6. Per-rider policies already exist in the core, but not in the fixtures.**
- Each request carries its own `commitmentPolicyId` (PROBE:31).
- The core looks up the policy per request (`HardVectorCandidateAssessor.cs:565`).
- The normalizer, however, stamps one ID on every request
  (`SRC/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:448`).

**Consequence.**
- **U vs C-30** measures a hard cap added on top of a dispatcher that already minimises dispatch-caused changes first.
- **FREE vs LOCKS** mixes three changes at once: the objective, the locks and the switch-count limits
  (`AGREED-DIRECTION-2026-10-08.md:108-110`). Shared rides fall from 53.1% to 21.8% and drop exposure from 23.8% to 3.9%
  (LAD:2-3).

### F4. The price of a pooled drop-off guarantee, from existing outputs [my arithmetic]

**Definitions.**
- *Late riders at threshold T* = share late by more than T against the first promise × served riders, rounded.
- *r\** = riders not served ÷ late riders avoided, for one step of the rule.

**T3.8 (measured traffic, 34 cells, 3,672 requests).**

| Arm | Served | Mean quote extension | Late > 60 s | Late > 120 s | Late > 300 s | Early > 60 s |
|---|---|---|---|---|---|---|
| U | 2,434 | 0 | 203 (8.34%) | 102 (4.19%) | 18 (0.74%) | 0.29% |
| U + forecast | 2,434 | 7.2 s | 137 (5.63%) | 87 (3.57%) | n/a | 0.33% |
| U + forecast + 60 s pad | 2,434 | 67.2 s | 87 (3.57%) | 48 (1.97%) | n/a | 42.44% |
| U + forecast + 120 s pad | 2,434 | 127.2 s | 48 (1.97%) | 31 (1.27%) | n/a | 94.37% |
| C-30 | 2,338 | 0 | 76 (3.25%) | 11 (0.47%) | 0 | 0.13% |
| C-30 + forecast | 2,338 | 7.4 s | 10 (0.43%) | 0 | 0 | 0.17% |

Sources: LATE:3-5,10-12,24-26; CVPAD:4,12,15,17,25,33; served counts T38:46.

Price of moving from U to C-30 (96 riders not served):

| Comparison | r\* at T = 60 s | r\* at T = 120 s | r\* at T = 300 s |
|---|---|---|---|
| U → C-30, no forecast | 96/127 = **0.76** | 96/91 = **1.05** | 96/18 = 5.3 |
| Both with forecast | 96/127 = 0.76 | 96/87 = 1.10 | — |
| Padded U (forecast + 60 s) → C-30 + forecast | 96/77 = 1.25 | 96/48 = 2.0 | — |

The padded comparison has one more difference: C's quote is 60 s shorter, with 0.17% early arrivals instead of 42.4%.

**WP14r ladder (fixed traffic, so lateness = dispatch only; 16 cells).**

| Arm | Served | Late > 60 / 120 / 300 s |
|---|---|---|
| FREE | 1,629 | 274 / 164 / 21 |
| LOCKS | 1,584 | 47 / 27 / 2 |
| C-120 | 1,563 | 23 / 0 / 0 |
| C-60 | 1,540 | 0 / 0 / 0 |
| C-30 | 1,534 | 0 / 0 / 0 |

Source: LAD:2-6. The counts match CVP:6-8 and CVP:11-13.

Price of each step:

| Step | At T = 60 s | At T = 120 s | At T = 300 s |
|---|---|---|---|
| FREE → LOCKS | 45/227 = **0.20** | 45/137 = 0.33 | — |
| LOCKS → C-120 | 21/24 = 0.88 | 21/27 = **0.78** | 21/2 = 10.5 |
| C-120 → C-60 | 23/23 = 1.0 | — | — |
| C-60 → C-30 | 6 riders lost, **0** avoided | — | — |

**What this means.**
- The cheapest reliability comes from the locks plus the stability-first objective.
- The cap costs about one ride per late ride avoided.
- In fixed traffic, a cap below the guarantee threshold buys nothing at that threshold: C-60 → C-30 costs 6 riders and
  avoids none at 60 s.

  This gives a principled rule for choosing B, which until now had no anchor (HO:255-258): **B = T minus a traffic
  margin**. Here T is the threshold of the guarantee you want to offer.

### F5. Levers already shown to do nothing, or to have nothing left to win (not proposed)

- **One-sided ratchet / recovery credit.**
  - Over 683 decision-induced revisions in WP14r, 0 moved a promise earlier and 683 moved it later (W14R:103-111). The
    ratchet arm tied with C-30 (W14R:82-86).
  - In T3.8 C-30, only 4 of 33 exposed riders had a net earlier change (BUC:37).
  - So the counterexample in BNA:74-76 (ETAs v = 600, e = 720, p = 600: the rider sees no change but C charges 120 s) is
    real in principle but almost absent in practice.
- **Removing the pickup lock, or a freeze horizon, under a 30-s budget:** identical on every counter (W14R:82-86).
- **Budget-saving lookahead:** only 2 of 148 blocks came from budget already spent
  (`claude-work/budget-block-diagnosis-2026-10-07.txt:10`).
- **A cap on the number of revisions:** under every C cap no rider had more than one nonzero change (BUC:8-38), so it
  would never bind.
- **Forecast inside the dispatcher:** Family B was rejected (FR:141-146).
- **Load alone, to make accumulation appear:** see F1. WP9 `c1` at 4 vehicles has 0 riders with two changes (CVP:24).

---

## 2. Ranked proposals

**Ranking criterion.** Value against the owner's requirement (business benefit + something others would optimise + a
new method, a one-step pipeline optimisation, or a new promise form), discounted by risk to a thesis that has about
5 weeks left and is not yet edited (HO:9-11, HO:494-495).

**Shared template.** Each proposal gives: idea, the questions it answers, who benefits, what is new and the closest
prior work, evidence in hand and evidence needed, tier and effort, a prediction with a kill result, and how it changes
the storyline.

**Effort basis.**
- A T3.8 job takes about 15 min wall, with 6 jobs in parallel (`claude-work/RUNTIME-ESTIMATE-2026-10-07.md:24-25`).
- Tool caps: 128 requests, 32 vehicles, 96 nodes (same file :40).

---

### Rank 1: P1, "The price of a pooled drop-off guarantee" (a budget dial plus guarantee framing)

**Idea.** Present rule C, the forecast and the ledger as the three pieces of an affordable pooled drop-off guarantee.
Report its price as a curve:
- riders not served per late rider avoided (r\*), as a function of the dispatch budget B and the guarantee threshold T;
- with quote length and early arrivals as a third axis;
- and choose B with the rule "the largest B whose dispatch bound plus traffic margin stays within T".

**Answers.** O2, O3, and O6 in two ways:
- a different promise form: a compensated guarantee with fault attribution;
- a one-parameter sweep of one pipeline step, which is the example thesis's pattern (PAP:141-149).

**Who benefits.**
- **Operator.** Operators already pay when a time promise breaks:
  - Lyft pays $15 / $50 on scheduled airport pickups (SUR:24-27);
  - Uber One pays $5 when the delivery estimate fixed at order time is wrong (SUR:40-44);
  - UberPOOL in 2016 gave $2 if a rider arrived later than the estimate (SUR:32-35).

  Today's pooled products do not cover the drop-off. UberX Share disclaims arrival times "because of traffic"
  (SUR:36-39), and Uber's Delayed Ride Guarantee excludes Matched Share rides (S3:49-51). In Du, Fan & Chen's model, the
  probability of a delay is a key factor in whether a paid on-time guarantee pays off (SUR:86-89). P1 measures that
  probability and its price in riders. The ledger then supports a two-layer design: riders are paid regardless of
  cause, while the operator audits by cause, as UK rail does with Delay Repay versus Schedule 8 (SUR:45-48), and as in
  the 49 CFR 37.131 analogy (FR:102-105).
- **Rider.** Lateness against the expected or timetabled time is the most heavily weighted time component, at about
  2.5–3.1 × in-vehicle time (PAP:347-348). The counter-evidence is under O3 in section 3.
- **Researcher.** A scalar to optimise and compare, r\*(B, T). It has the same shape as price-of-commitment and
  price-of-service-quality studies (SUR:177-180; PAP:450-469; PAP:537-553). It also addresses the open problem Fielbaum &
  Alonso-Mora name, "how to control it" (PAP:184-185).

**What is new, and the closest prior work.**
- **UberPOOL "Arrive by"** met a pooled drop-off guarantee by quoting the "absolute latest time" (SUR:32-35). That is the
  padding corner. Padding U to C-30 + forecast's 1-minute tail takes about 180–260 s of extra quote, and then 94.6–98.6%
  of riders arrive more than 1 minute early (CVPAD:21-22).
- **Schulz & Pfeiffer 2026** communicate a latest drop-off time, with fixed travel times and 900 s (PAP:231-252).
- **Du, Fan & Chen 2023** is analytical and about food delivery (SUR:86-89).
- **Fielbaum & Alonso-Mora 2020** measure the rejection cost of control (PAP:203-210). D03:56 forbids claiming
  pre-decision control or the service–stability trade-off as new.
- **New (narrow):** the measured price curve of a pooled drop-off guarantee across dispatch budgets and thresholds,
  under measured traffic, with liability split by cause from the v/e/p ledger, plus a rule for choosing B tied to T.

**Must NOT claim.**
- That guarantees, compensation or attribution by cause are new.
- Any effect on revenue, retention, satisfaction or labour (D03:236-237).
- Any money value (BNA:113-116).
- That C is needed for minute-scale guarantees of 5–10 min. In this regime it is not: U already has 0.74% of riders more
  than 5 min late and 0.08% more than 10 min late (LATE:5).

**Evidence in hand.**
- The F4 tables.
- The ledger split by cause (FR:72-77, :102-105).
- Served riders by B at 07–09 h (FP:76-77).
- The chronological backtest (`JOINT-CONCLUSIONS-2026-10-07.md:103-115`).

**Evidence needed.**
- **(a) T0 script.** Per rider, lateness against the first displayed promise at T ∈ {60, 120, 180, 300} s, counted two
  ways: regardless of cause, and fault-based (fault = dispatch + anticipated traffic not in the quote). Compute r\* with
  a day-cluster bootstrap.
- **(b) Optional T1 runs on the 34 T3.8 cells:**
  - **C-120:** `tang3/configs/C-120.json` exists. Measured-traffic C-120 so far exists only for 8 cells at 07–09 h
    (FP:73-78).
  - **C-0**, the UberX-Share-like end of the dial: config-only per `codex-work/STRONG-BASELINE-CODEX.md:54` and HO:488.
    `C-0.json` must be written.

**Tier and effort.**
- T0: about 10–14 h (script 6–8 h, independent re-check 2–3 h, figure 2 h).
- Optional T1: 68 runs, about 3 h wall on AC power, plus about 5 h for sealing, validity checks and analysis.

**Prediction (seal before running).**
1. C-120 on the 34 cells serves ≥ 2,386 riders, recovering at least half of the 96-rider gap. In WP14r the same step
   recovers 29 of 50 (LAD:3-6) [my arithmetic].
2. C-120 + forecast: late > 120 s against the first displayed promise ≤ 0.5% of served.
3. r\*(U → C-120, T = 120 s) is below r\*(U → C-30, T = 120 s), which is 1.05 (or 1.10 with the forecast).
4. C-0 serves fewer riders than C-30, and its late share at T = 60 s is within 0.2 pp of C-30's, because that lateness
   is driven by traffic.

**Kill.**
- C-120 recovers fewer than 24 riders, or prediction 3 fails: the measured-traffic dial has no sweet spot, and the
  chapter reports only C-30 versus U.
- Prediction 4 fails (C-0 cuts the 60-s late share by more than 1 pp): the "driven by traffic" reading is wrong.

**Storyline: extend.** The chapter list is P0's (rank 5), with these changes:
- ch. 1 opens with the guarantee gap (pickups and deliveries are guaranteed, pooled drop-offs are not);
- ch. 3 adds the guarantee definitions (paid regardless of cause vs fault-based; r\*);
- ch. 7 becomes **"The price of a pooled drop-off guarantee"**: the dial FREE / LOCKS / C-120 / C-60 / C-30 / C-0, the
  thresholds, the quote-and-early axis, and the rule for choosing B;
- ch. 8 adds the parametric business reading and the caveat that "cumulative" acts as per-insertion at 30 s (F1).

---

### Rank 2: P2, an opt-in "express" guarantee through per-rider promise classes

**Idea.** Give each rider a promise class through its `commitmentPolicyId`:
- **express** riders get rule C at 30 s plus the forecast quote, and only they are covered by the P1 guarantee;
- **standard** riders get U: locks, no drop cap.

Measure riders served and lateness per class as the express share varies.

A variant with no Domain change: three trip-length classes with B = 30 / 60 / 120 s by direct-time tercile. This
approximates the proportional budget whose first-order screen already exists: at equal mean budget it unblocks 11 → 30
requests at 60 s and 59 → 89 at 120 s (`claude-work/proportional-budget-screen-2026-10-07.txt:2-5`).

**Answers.** O6 (a different kind of promise: a menu or tier), O2, O3.

**Who benefits.**
- **Operator.**
  - MOIA already sells "a shorter arrival window" as "an optional upgrade" in ride-pooling (SUR:271-274), and offers
    "up to six different offers" with arrival times (SUR:275-278).
  - Willingness to pay for precision varies between customers; tailoring time slots gave "approximately 9% more
    shipping revenue" in home delivery (SUR:219-221).
  - Uber Priority sells speed with no guarantee (SUR:283-286). A guaranteed tier is the differentiated product.
  - The cost side, first order: at a 20% express share, 114 of the 148 budget-blocked requests get a passing candidate
    (F2).
- **Rider.**
  - Those who value punctuality get C + forecast, with 0.43% late by more than 1 minute (LATE:26).
  - The others keep U's service.
  - Alonso-González et al. suggest offering services with different levels of uncertainty to cater for different
    preferences (PAP:302).
- **Researcher.** Schmidt et al. 2026 name "dynamic settings with sequentially arriving requests and personalized
  commitments" as natural extensions (SUR:159-164).

**What is new, and the closest prior work.**
- **Lyft patent US12182741B2:** per-match limits relative to the initially quoted ETA, inside a "predictable" ride mode
  (SUR:201-204).
- **MOIA Express:** its algorithm is not public (SUR:271-274).
- **Elmi et al. 2026:** chooses which passengers to protect; only the abstract has been checked (BNA:46). D03:211-213
  states that protecting individual riders is not novel.
- **Mt-KaRRi's** α·t + β deadline and Lyft's ETA ratio cover the trip-length variant (SUR:151-158, :202).
- **New (narrow):** the measured cost curve (riders served vs express share) of an opt-in tight drop-off guarantee,
  enforced by a per-rider dispatch budget under measured traffic, with a ledger per class.

**Must NOT claim.** That tiers, selective protection, proportional limits or per-rider guarantees are new
(D03:211-213); any willingness to pay or revenue from tiers (there is no demand model).

**Evidence in hand.**
- F2 (TIER:1-7), F3 item 6, and the proportional screen.

**Evidence needed.**
- A Benchmarking-layer option that assigns `commitmentPolicyId` per request, either by a hash share or by direct-time
  class.
- A commitment config with two policies; the file format is already a list (`tang3/configs/C-30.json:3-4`).
- 34 regenerated fixtures, the equivalence gates below, and the runs.

**Tier and effort.** T2, with C# changes only in `RideBound.Benchmarking`; Domain and Application stay unchanged. It
needs a separate worktree from `C:/Code/RideBound-noworse` and `dotnet test RideBound.slnx`. About 25–35 h:
- normalizer option and tests: 8–12 h;
- fixtures: 3–4 h;
- runs: 2–4 smoke runs plus 34 at a 20% express share (plus 34 at 50%, optional), about 1.5–3 h wall;
- analysis: 6–8 h.

Not yet verified: that the runner's config loader accepts more than one policy, and that the preflight's provenance
check accepts re-normalised fixtures.

**Prediction.**
1. Equivalence gate: on 2 smoke cells, share 0 reproduces U's fleet-action digests and share 1 reproduces C-30's.
2. At a 20% express share, served ≥ 2,386, recovering at least half of the gap. The first-order screen predicts more;
   the knock-on effects are unknown.
3. Express riders: 0 budget overshoots (true by construction). Late by more than 1 min against the first promise:
   ≤ 4.25% without the forecast (C-30's 3.25% + 1 pp) and ≤ 1.0% with it.
4. Standard riders: late by more than 1 min within ±1.5 pp of U's 8.34%.

**Kill.** Prediction 1 fails (the implementation is invalid), the served gain is below 24 riders, or express riders'
late > 1 min exceeds 4.25%. In the last case, mixing classes harms the protected riders and the tier story fails.

**Storyline: extend.** P1's guarantee becomes an opt-in product. Chapter 7 gains a section "Who gets the guarantee: an
express tier".

---

### Rank 3: P3, "Spend the budget": cost-first selection under the hard per-rider budget

**Idea.** Change one step of the dispatcher, the selection objective. Today it is stability-first and ordered (F3). Make
it cost-first, and keep C's hard budget as the only stability constraint.

Optionally, replace the stability levels with a single weighted level, cost + λ·Σ|c|, and sweep λ ∈ {0, 1, 4, ∞}.

Measure: sharing, riders served, vehicle time per served rider, budget use and lateness.

**Answers.**
- O6: it optimises one algorithm in our pipeline and gives a trade-off curve, as in the example thesis.
- O2: operator efficiency.
- The central weakness: cost-first dispatch is the regime in which the cumulative clause actually binds (F1).

**Who benefits.**
- **Operator.** Sharing is where the operator gains: users carry the diseconomies of scale, operators capture the
  economies (PAP:479-481). FREE shares 53.1% of served riders against LOCKS' 21.8%, and serves 94.3% against 91.7%
  (LAD:2-3). If the hard cap alone already protects riders, the objective's stability tie-breaking may be costing
  sharing for nothing.
- **Rider.** The bound B still holds by construction: 0 overshoots so far (BUC:37; WBU:10).
- **Researcher.** The order and weights of the objective are a standard optimisation axis. Ardali & Knapp 2026 report
  stability as its own axis and find that "No single method was best" (SUR:187-190). Our own rolling-penalty baseline
  B2 already exists (`SolverBackedFleetSelection.cs:307-318`).

**What is new, and the closest prior work.**
- Weighted penalties for disruption are prior work: Timefold's soft penalties for replanning (BNA:41), Hörl & Zwick's
  per-second penalty (SUR:144-149), and assignment costs that include riders already on board (PAP:485).
- The service–stability trade-off is not new (D03:56).
- **New (narrow):** evidence on whether, in this pipeline, the hard per-rider budget can replace the ordered stability
  objective, and the first runs in which the cumulative clause actually binds.

**Must NOT claim.** A new objective or method in general; any welfare result.

**Evidence in hand.**
- F3 (code) and F1 (the cumulative clause binds only under free-type dispatch at B ≥ 120 s).
- The ladder (LAD:2-6).
- Inconclusive: removing the pickup lock changed nothing, but that was tested only *under* a 30-s cap (W14R:82-86).

**Evidence needed.**
- A new objective-profile option, a runner build, a copy of the harness, and the runs.
- An operator-cost metric, such as vehicle busy time or distance. It would come from `vehicleAdvanced` positions plus
  `travelTimesUpdated` arcs (PROBE:12,19,25-26). Whether that extraction works is not yet verified.

**Tier and effort.** T2, in `RideBound.Algorithms/Policies`; Domain and Application stay unchanged. It needs a new
worktree from `C:/Code/RideBound-noworse` and `dotnet test RideBound.slnx`.
- The harness runs a prebuilt runner (`tang3/w07/run_w07.py:40`) and checks the repository inventory of its working
  folder (`tang3/pilot/run_pilot.py:27`; `run_w07.py:46`). New runs therefore need their own worktree and inventory
  hash, and never `E:/Code/RideBound-deadline`.
- Effort: about 35–45 h.
- Runs: 2 smoke runs plus 102 (U-cf, C-120-cf and C-30-cf × 34 cells; "cf" = cost-first), plus 34 stability-first C-120
  runs shared with P1. About 4.5–6 h wall.

**Prediction.**
1. U-cf shared share ≥ U + 10 pp, i.e. from 22.8% to at least 32.8% (`pooling-share-2026-10-06.txt:2`, in the codex-debate root).
2. C-120-cf shared share ≥ stability-first C-120 + 5 pp, with served ≥ C-120 − 1%.
3. Under C-120-cf, cumulative-only binding events ≥ 0.2% of riders. Every stability-first arm so far has 0.
4. 0 budget overshoots.

**Kill.**
- U-cf shares less than U + 3 pp: the objective is not the lever. Stop and report.
- C-120-cf serves fewer than C-120 − 3%: choosing the cheapest option first blocks later riders.

**Storyline: extend.** It adds one "algorithm" chapter, **"Selection objective under the cap: the cap as the only
stability mechanism"**, between the results and the discussion.

---

### Rank 4: P4, load stress test at 4 vehicles (does the price explode?)

**Idea.** Rerun the ladder with half the fleet on the 12 preselected cells of the agreed Stage 2, with FREE, LOCKS, C-30
and C-120 (`AGREED-DIRECTION-2026-10-08.md:39-44`). Then measure:
- r\* and the served cost at higher load;
- whether accumulation appears.

**Answers.** O2 (does the business price hold under load?) and the committee's low-load attack (FP:54-56).

**Who benefits.**
- **Operator:** a price that holds across load levels.
- **Researcher:** external validity.
- **The thesis defence.**

**What is new, and the closest prior work.** Nothing new in concept.
- Unreliability worsens when vehicles are more loaded (PAP:482-483).
- In WP9 panel B, free-type `b1` serves 966 against `c1`'s 860, but on the older runner and as a whole policy package
  (`claude-work/fleet-size-wp9-check-2026-10-07.txt:4-5`).

**Must NOT claim.** City-scale validity.

**Evidence in hand.** CVP:19-28 (at 4 vehicles, `b1` has 3.93% of riders with two changes, `c1` has 0) and
`fleet-size-wp9-check-2026-10-07.txt:2-5`.

**Evidence needed.**
- 4-vehicle fixtures from the prebuilt normalizer DLL, run with `--repository` pointed at a staging folder; no build is
  needed (`AGREED-DIRECTION-2026-10-08.md:112-114`).
- The FREE WP4 config (`codex-work/round8-free-wp4-candidate.json:3`).
- 48 runs.

**Tier and effort.** T1, about 12–16 h. 4-vehicle 108-request runs have a median wall time of 283 s
(`RUNTIME-ESTIMATE-2026-10-07.md:14`), so all 48 take under 1 h wall at 6 in parallel. FREE's run time is not yet
verified.

**Prediction.**
1. The served loss from LOCKS to C-30 is ≤ 8% of LOCKS' served riders. At 8 vehicles it is 3.2% in WP14r [my arithmetic
   from LAD:3,6] and 3.9% in T3.8.
2. Under C-30, riders with two or more nonzero changes ≤ 0.1%.
3. FREE: ≥ 35% shared and ≥ 15% drop-exposed (`AGREED-DIRECTION-2026-10-08.md:47-56`).

**Kill.** Prediction 1 fails: "C stays cheap under load" is false. Report it as a limitation, and quote P1's price per
load level.

**Storyline: extend** (a robustness section in ch. 7 or ch. 8).

---

### Rank 5: P0, keep the current storyline unchanged (honest baseline)

**Idea.** Write the thesis exactly as agreed (HO:88-135; `AGREED-DIRECTION-2026-10-08.md:6-11`):
- C + forecast + the three-part ledger;
- the permitted contribution (FP:65-69);
- no new analysis or runs;
- pending item 1 of the handoff, the Gardner–McKenzie replay, stays optional (HO:482-487).

**Answers.** O6, "keep the current direction".

**Who benefits.**
- **The owner:** all remaining time goes to writing, with zero new risk.
- **Researchers:** results that are already sealed and cross-checked (T38:97-106; FR:179-195).

**What is new, and what must not be claimed.**
- New: as permitted (FP:65-69).
- Must not claim anything in FP:58-63, D03:56 or D03:236-237.
- Given F1, the text should not lean on "cumulative" as the distinctive feature at B = 30 s.

**Evidence.** In hand: everything in HO §4. Needed: none.

**Tier and effort.** No tier: 0 h of analysis and 0 runs.

**Prediction and kill.** No new prediction.

**Risk.**
- O2 ("what does the operator gain?") gets only a qualitative answer, while BNA:62-65 records that no checked source
  confirms a buyer's need for C.
- The cumulative weakness stays open.

**Chapter list (the baseline every other proposal edits).**
1. Introduction: promises drift for three causes; motivation; a narrow statement of contributions.
2. Related work and claim boundary: Fielbaum & Alonso-Mora 2020; Schulz & Pfeiffer 2026; Hörl & Zwick 2022; Mt-KaRRi;
   Elmi 2026; forecast-based quoting; value of reliability.
3. Method: the RideBound pipeline (insertion, locks, stability-first selection), the v/e/p ledger, rule C, deadline M⁺,
   rule V, the forecast promise layer, and the three-part ledger.
4. Experimental design: FleetPy Manhattan, measured traffic factors, T3.8 and WP14r, sealing, metrics, limitations.
5. Results 1: C vs deadline vs U (riders served, forced decisions, broken promises, lateness).
6. Results 2: forecast promise and ledger (Family A, the snow afternoon, cap vs padding, backtest).
7. Results 3: the budget frontier (WP14r, w07 / w07x) and the negative ML pilot.
8. Discussion: limitations (low load, 0 s dwell, one city-wide traffic factor, the cumulative clause rarely active) and
   the claim boundary.
9. Conclusion and future work.

**Why rank 5.** P1 dominates it: P1 is P0 plus about 2 days of zero-run analysis.

---

### Rank 6: P5, a "pooling-proof arrival window"

**Idea.** Show the promise as a short window [F0 − 30 s, F0 + B]. By construction of C, pooling can never push the rider
past the upper end; only traffic the forecast missed can. Evaluate coverage against window width, versus calibrated
windows of equal width built on U + forecast.

**Answers.** O6 (a different promise form) and O3.

**Who benefits.**
- **Rider.** People prefer forecasts "as precise as warranted by the information available, but not more precise": a
  narrow range beats both a point and a wide range (SUR:246-248).
- **Operator.** MOIA already quotes arrival windows and sells shorter ones (SUR:271-274).

**What is new, and the closest prior work.**
- Amazon SPEEDY: narrower slots gave "+17 bps in units" (SUR:93-96).
- UncertBAT: conformal arrival windows for buses (SUR:232-235).
- Bharti et al. 2026: windows revised only near their start (SUR:228-231).
- Rauh 2025: appointment ranges (PAP:419-439).
- **New (narrow):** the window width is tied to the dispatch budget, which makes it pooling-proof by construction.

**Must NOT claim.** That window promises or conformal windows are new. Wide intervals can read as uncertainty
(SUR:250-253).

**Evidence in hand.** In the chronological backtest, the share of riders arriving within ±60 s of the promise on
15 / 16 Nov is 100% / 99.7% for C-30 + forecast against 96.9% / 94.6% for U + forecast
(`claude-work/calib-backtest-2026-10-07.txt:4,38`).

**Evidence needed.** A T0 replay with `display_layer` on existing transcripts: U and C-30 from T3.8; C-60, C-120 and
C-300 from w07.

**Tier and effort.** T0, 6–8 h, 0 runs.

**Prediction.** On the 15–16 Nov weekday cells, the 60-s window [F0 − 30, F0 + 30] contains ≥ 99% of C-30 + forecast
arrivals. The best 60-s window around U + forecast, with its offset fitted on 14 Nov only, contains ≤ 95%.

**Kill.** The gap is under 1 pp: the cap is not needed for a window promise.

**Storyline: extend** (a display section in ch. 6). It overlaps P1, so the thesis should pick one display form.

---

### Rank 7: P6, price the promise in vehicles

**Idea.** Express C's cost in the example thesis's unit, taxis needed (PAP:98-103): how many extra vehicles let C-30
serve as many riders as U. This is the resource-augmentation idea.

**Answers.** O2 (in units an operator knows) and O6 (the example thesis's metric).

**Who benefits.** The operator, because fleet is a familiar cost unit. Researchers, through the price-of-commitment
method (Bent & Van Hentenryck; SUR:177-180).

**What is new, and what must not be claimed.** Nothing new: fleet sizing is standard (`codex-work/IDEAS-CODEX.md:74-82`).
Do not claim a fleet-sizing method, and do not convert it to money.

**Evidence in hand: T0 arithmetic only** [my arithmetic].
- U serves 2,434 / (34 × 8) ≈ 8.9 riders per vehicle per cell.
- C-30's gap of 2.8 riders per cell is therefore about 0.32 of a vehicle per 8, or 3.9% of the fleet. This uses average
  productivity, not marginal productivity.
- Even U rejects 1,238 of 3,672 requests (T38:46). And 1,186 of C-30's 1,334 rejections are structural
  (`claude-work/budget-block-diagnosis-2026-10-07.txt:2-5`). Fleet size is the binding resource.

**Evidence needed.** Fixtures with 9 and 10 vehicles. Whether the vehicles' start positions nest (the first 8 the same as
today) is not yet verified. Then 68 runs.

**Tier and effort.** T1, 12–16 h, 68 runs (about 3 h wall).

**Prediction.** C-30 with 9 vehicles serves ≥ 2,434.

**Kill.** C-30 needs 10 or more vehicles, i.e. its cost is ≥ 25% of the fleet.

**Storyline: extend** (one figure in ch. 7).

---

### Rank 8: P7, multi-week traffic data for the forecast and for ML

**Idea.**
- Rebuild the 15-minute Manhattan traffic factor from NYC TLC yellow-taxi trips for Sep–Dec 2018, using Syed et al.'s
  method.
- Replace the 2-day forecast history with a multi-week profile.
- Optionally, test on unseen days.

**Answers.** O5.

**Who benefits.** Researchers get a more defensible forecast history: 12 Nov was a federal holiday and 13 Nov had
26.9 mm of rain (MLD:23-25). Operators and riders gain nothing measurable in this simulator.

**What is new, and the closest prior work.** Nothing.
- Historical-average profiles are standard; Google uses 17 weeks (`codex-work/STRONG-BASELINE-CODEX.md:18`).
- ML for ETAs, and learning pooled outcomes from FleetPy, are prior work (FP:58-61).

**Evidence in hand.**
- Headroom: with the forecast, 2 of 1,471 weekday riders are late, against 68 without it (MLD:284-291).
- The snow afternoon: 34 of 601 late, and it is a single event (MLD:293-298).
- None of the verified ride-hailing datasets has a quoted ETA (MLD:259-262).
- pyarrow is missing from both environments (MLD:243-245).

**Tier and effort.**
- T3: 1–1.5 weeks for the multi-week profile (MLD:371-373), plus an install the owner must approve.
- 0 runs for the replay. Unseen days add 1–2 weeks, and the input path is not yet verified (MLD:377-384).

**Prediction.** The multi-week profile lowers the held-out 30-minute error in predicted traffic growth against the
2-day history, but cannot bring weekday late riders below 2 of 1,471.

**Kill.** The validation gate fails: the median |relative error| of the rebuilt 12–18 Nov factors exceeds 3%
(MLD:239-241).

**Storyline: unchanged** (a robustness appendix). Not recommended within 5 weeks.

---

## 3. Direct answers, in plain English

### (O2) What does rule C alone give the operator, and would others optimise it?

**What it gives.** A promise the operator can always keep: *"riders added after you booked will never move your drop-off
by more than B in total."*
- It held for every rider in every run: 0 overshoots (BUC:8-38; WBU:10-17).
- It never forced the dispatcher to break a promise. The deadline counted from the first quote had to recover in 41.3% of
  decisions, at the same 2,338 riders served (T38:46,55-60).
- Pooling-caused tail lateness disappears: riders more than 5 min late fall from 0.74% to 0, and more than 2 min from
  4.19% to 0.47% (LATE:5,12).

**What it costs.**
- 96 riders, which is 2.6 pp of requests or 3.9% of U's served riders, at 8 vehicles (FP:41).
- Per late rider avoided: about 0.8 riders not served at a 1-minute threshold and about 1.1 at 2 minutes; at a 5-minute
  threshold about 5 (F4).
- The cheap reliability comes earlier: the locks plus the stability-first objective cost about 0.2 riders per late rider
  avoided (WP14r, F4).

**The honest business sentence.** Rule C makes a tight (1–2 min) pooled drop-off guarantee possible, at about one ride
given up per late ride avoided. It pays only if a payout plus the retention value of a kept promise is worth more than
about one ride's margin, and this thesis measures neither (BNA:113-116). For 5–10-minute guarantees, U is already nearly
safe in this low-load simulation.

**Would researchers optimise it?**
- Not Σ|c| itself. That is an internal control and audit quantity; riders feel lateness against the promise
  (SUR:337-342).
- What they would optimise is the price curve: riders served vs guarantee liability vs quote length, with B, a per-rider
  B_i (P2) or the selection objective (P3) as the decision variables.
- Both are named open problems: Fielbaum & Alonso-Mora's "how to control it" (PAP:184-185) and Schmidt et al.'s
  "personalized commitments" (SUR:159-164).

### (O3) What does the forecast add? What can honestly be said about what riders care about?

**What the forecast adds for the operator.**
- At a 1-minute threshold, late riders fall from 203 (U) to 10 (C-30 + forecast), out of about 2,400 served.
- The quote is only 7.4 s longer, and only 0.17% arrive more than 1 minute early (CVPAD:4,33).
- The forecast also helps U (137 late). The two pieces remove different causes (FR:79-86), and the forecast's gain is
  not unique to C (FR:65).
- On the snow afternoon the forecast barely helps: 7.19% → 5.94%, with 92.5% of late seconds unanticipated (FR:102-104).
  This is where the ledger keeps a guarantee fair: under a fault-based rule, unanticipated traffic is excused.

**What riders care about: evidence for.**
- Lateness against the expected time is weighted 2.5–3.1 × in-vehicle time (PAP:347-348, :624).
- Mean delay is rated 3.7 × travel time (SUR:112-115).
- A pooling-caused wider arrival window is felt as almost twice as bad as waiting (S3:44-45).
- Lack of trust in reliability is a barrier to adopting pooled rides (SUR:116-119), and lateness pushes riders out of
  sharing (SUR:120-123).

**Evidence against.**
- In a pooled-service stated-preference study, reliability is valued at about half of time, and small unannounced
  delays weigh *less* than announced time (PAP:285-286, :294).
- Stated tolerances are in minutes, with a median of 4–6 min (S3:101).
- Changing the first waiting-time estimate by ±1 min had no effect on abandonment (SUR:63).
- Klinkhardt et al. find riders prefer slightly longer quotes with early arrivals (SUR:113). That favours padding. Padded
  U matches C-30 + forecast in on-time riders (2,347 vs 2,328 per 3,672), but with quotes about 60 s longer and 42% of
  riders arriving more than 1 minute early (CVPAD:15,33).

**So, honestly:**
- Riders care about minutes of lateness against the quote.
- C + forecast's advantage is accuracy with short quotes, not more on-time riders.
- Claim no value for the seconds-level gains, and no satisfaction effect (D03:236-237).

**Is it a contribution?** A useful but narrow one: a clean division of labour (cap / forecast / ledger) with measured
complementarity. It is not a new method.

### (O5) Is more data for ML worth it?

More data exists: NYC TLC trips with second-level times, and 2019+ high-volume ride-hailing trips with shared-ride flags
(MLD:16-18,139). But no verified ride-hailing dataset has a quoted ETA (MLD:259-262). In this simulator, more training
data cannot buy a measurable gain:
- on weekdays, 2 of 1,471 riders are still late with the forecast (MLD:284-291);
- the large remainder (34 of 601) is a single snow afternoon (MLD:293-298).

**Recommendation:** no ML work package before the deadline. If time is left, the multi-week profile (P7) is robustness
evidence for the forecast, not an ML contribution.

### (O6) My single recommended direction

**P1.** Same storyline, reframed as *the price of a pooled drop-off guarantee*.
- It answers the operator question with numbers in rider units, without inventing money values.
- It turns "why 30 s?" into a rule: B = T minus a traffic margin.
- It makes the thesis a one-step sweep like the example thesis (PAP:141-149).
- It needs only T0 work plus up to 68 runs with existing configs (C-120, C-0).

If the owner wants one more experiment, add only one of these two:
- **P2 (express tier)** if the owner prefers a "different promise" chapter. Lower risk: the core already handles one
  policy per rider (F3), the first-order screen is strong (F2), and MOIA Express is a close real-world precedent.
- **P3 (cost-first objective)** if the owner prefers an "algorithm optimisation" chapter. It is scientifically more
  interesting and repairs the cumulative weakness, but it is riskier.

Never do both before the deadline.

### The weakest point a committee would attack, and the honest defence

**The attack.** "Your distinctive mechanism, the cumulative per-rider budget, never acts in your runs."
- At B = 30 s it behaves exactly like a 30-s per-insertion cap: 0–2 cumulative-only riders per population (F1).
- Per-insertion caps relative to the quoted ETA are prior art:
  - the Via patent's 10-minute threshold (SUR:209-212);
  - Lyft's per-match limits (SUR:201-204);
  - Hörl & Zwick's strategy B (SUR:144-149).
- Your U baseline already minimises dispatch-caused changes before cost (F3). So you compare against a conservative
  dispatcher, at about 0.54 riders per vehicle (FP:54). What is left?

**The defence.**
1. **Concede and narrow.** The working mechanism is *charging only the dispatch part*, with traffic separated by the
   v/e/p ledger. That is why C, unlike the deadline, is never forced (0% vs 41.3%) while serving exactly the same riders
   (T38:43-46,58-59). This result does not depend on cumulativeness.
2. **The cumulative definition is a contract property.** It is what makes the stated bound hold over the whole trip, for
   any number of insertions. We measured when it starts to matter: at B ≥ 120 s under free dispatch, for 0.7–1.0% of
   riders (F1). P3 or P4 tests that regime directly.
3. **Against Hörl & Zwick B:**
   - it covers all riders, not only those about to be late;
   - it is a hard cap, not a soft penalty;
   - it comes with a per-rider ledger;
   - it is evaluated against a deadline rule under measured traffic.
4. **Low load and the conservative U are stated as limitations**, with the denser WP14r / WP9 free arms as the
   comparison. P1's price curve is quoted only for the regimes measured.

The defence does *not* rescue a claim that the business value is shown (BNA:62-65; D03:241-242). P1 makes that claim
parametric instead.

---

## 4. Not verified, or limits of this file

- **F1 and F2 are screens in arms without the cap**, apart from the WP9 `c1` arms. Decisions under an enforced cap would
  differ. WP9 used an older runner.
- **F3 item 3** is my reading of the code. I did not instrument a run to confirm which objective level breaks ties.
- **P2:** that the runner loads more than one commitment policy, and that re-normalised fixtures pass the preflight
  provenance check. Not verified.
- **P3:** that vehicle distance or busy time can be extracted from transcripts; and the runner rebuild and harness
  re-pointing effort. Not verified.
- **P6:** that 9- and 10-vehicle fixtures keep the first 8 vehicles' start positions. Not verified.
- **All r\* values** compare different served sets (227 riders served only under U, 131 only under C-30; HO:181). They
  ignore rider responses such as cancellation or abandonment.
- **Effort figures** are my estimates. Run-time figures are extrapolated from the medians in `RUNTIME-ESTIMATE-2026-10-07.md`.

## Appendix: helper files (all in `claude-work/r13-proposer/`, outputs opened with mode "x")

| Script | Output | Runtime |
|---|---|---|
| `cumulative_vs_perinsertion.py` | `cumulative-vs-perinsertion-2026-10-10.txt` | 157 s; log `run.stderr.txt` |
| `tier_budget_screen.py` | `tier-budget-screen-2026-10-10.txt` | — |
| `probe_event_kinds.py` (one T3.8 C-30 transcript) | `probe-event-kinds-2026-10-10.txt` | — |

- **Python:** `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B`, with `PYTHONIOENCODING=utf-8`.
- **Inputs:** existing transcripts under `C:/RideBoundData/research/tier3-t38-v1`,
  `E:/RideBoundData/wp14r/development-v6-ledger` and `E:/RideBoundData/wp9/confirmatory-h6-panel{a,b}-v2`. All were read
  only.
- **Power:** checked before running (BatteryStatus 2, plugged in).
