# R13 final verdict (final judge, Claude side), 2026-10-10

**Scope.** Final judgement of the round-13/14 Claude-vs-Codex review for the RideBound thesis (UET/VNU, author Trần
Quang Thành; deadline reportedly mid-November 2026, UNCONFIRMED). Sections A, B, D and E are in English; section C is
in Vietnamese for the owner.

**What I read.**
- In full: `ROUND13-FACT-PACK.md`, `ROUND13-RUBRIC.md`, the 2026-10-09 handoff, both proposal files, both
  cross-judgements, `FORECAST-REPORT.md`, `T38-REPORT.md`, `W07X-REPORT.md`, and both budget-use outputs.
  Also the cap-vs-pad, lateness, ladder, cumulative-vs-per-insertion, tier-screen, screen-audit and evidence-keys
  outputs, Codex's raw-verification text and witnesses JSON, and the owner's stricter claim boundary
  `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (read only).
- Targeted lines only: the cited code in `C:/Code/RideBound-noworse/src`, the configs in `tang3/configs/`, the
  example thesis and the owner's papers (text extractions), `R13-PAPERS-CLAUDE.md:90-150`,
  `R13-ML-DATA-CLAUDE.md:136-160,255-298` and `AGREED-DIRECTION-2026-10-08.md`.
- Not opened: `R13-SURVEY-CLAUDE.md`, `R13-SURVEY-CODEX.md`. Where I depend on them, I either re-fetched the primary
  source myself or mark the claim UNCONFIRMED.

**What I ran.** Five small read-only scripts over existing transcripts, with
`E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B` and `PYTHONIOENCODING=utf-8`. Outputs were opened in mode
"x", and scripts and outputs are in `claude-work/r13-final-judge/` (listed in the appendix). I ran no simulation,
build, install or deletion, and wrote nothing outside that folder and this file.

Short anchors used below:

| Key | Path |
|---|---|
| FJ | `claude-work/r13-final-judge/` (my new outputs) |
| PAD | `claude-work/cap-vs-pad-frontier-2026-10-07.txt` |
| LATE | `optimize/report-extras/lateness-distribution-2026-10-06.txt` |
| BUC / WBU | `claude-work/budget-use-check-2026-10-09.txt` / `claude-work/wp14r-budget-use-2026-10-10.txt` |
| CVP | `claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` |
| LAD | `claude-work/wp14r-ladder-reanalysis-2026-10-08.txt` |
| T38 / W07X / FR | the T3.8, w07x and forecast reports |
| D03E | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (owner's stricter copy) |
| SRC | `C:/Code/RideBound-noworse/src/` |
| CP / CXP | Claude / Codex R13 proposals |
| CJ / XJ | Claude's judgement of Codex / Codex's judgement of Claude (R14) |

---

## 0. Bottom line

1. **One storyline, kept.** A pooled rider's promised drop-off time drifts for three causes. Each cause is handled in
   its own place:
   - the dispatch part is capped (rule C);
   - anticipated traffic goes into the first quote (the forecast);
   - the rest is recorded (the ledger).

   Both judges agree on this backbone. So do I.
2. **New decisive fact (this round, zero runs).** On measured traffic, the cumulative clause of rule C never decided
   anything:
   - The data: 98 enforced-C runs, 64,371 decisions and 1,256 candidates rejected by the budget
     (FJ/cumulative-decisive-check:4-30).
   - Every one of those candidates already exceeded B in a single dispatch move.
   - So a per-step dispatch-only cap of the same B would have admitted exactly the same candidates.
   - Elsewhere the clause decided at most 7 decisions: 4 on fixed traffic and 3 in one synthetic world. It changed
     at most 1 final rejection (FJ/per-run-cumulative-only-b:2-7).

   The working ingredient is **charging only the dispatch part** (traffic split off by the v/e/p ledger). The
   cumulative definition is a guarantee over the whole trip that this regime never exercised.
3. **Recommended next step (exactly one): item A1.** Write the results chapter around one corrected
   frontier table. It covers served riders, on-time completions per request, late and early riders, quote length,
   shared rides, and forced or self-broken promises. The deadline rule M⁺ is the central comparator. It also reports
   the cumulative audit. Tier T0, 0 runs.
4. **Optional extension (at most one): item A2.** Cost-first selection under unchanged hard gates (Claude P3, made
   minimal). It is the only "optimise one pipeline step" study that tests the committee's strongest attack. Start it
   only if the deadline is confirmed and A1 is drafted.
5. **No ML chapter, no new promise form, no allocation study before the deadline.**

---

## A. Final list (ranked, at most 5)

### A1. RECOMMENDED NEXT STEP: "What a dispatch-only promise buys and costs". One results chapter, zero runs

**Idea (one sentence).** Re-present the existing results as one service / reliability / quote frontier. It covers
U, C-30, M⁺-30 and V-30, each with and without the forecast, plus padded U, and the WP14r ladder. The deadline rule
M⁺ is the main comparator, and the chapter adds the new audit showing that rule C acted as a per-step dispatch-only
cap.

**Owner questions answered.** O1, O2, O3, O4, and O6 ("keep the direction, but tell it correctly").

**What goes in it (all numbers already exist and are verified in section B).**

1. **Frontier table, T3.8: 34 cells, 3,672 requests.**

   | Arm | Served | Late > 60 s (riders) | On-time completions at > 60 s | On-time at > 120 s | Early > 60 s | Quote extension | Forced decisions |
   |---|---|---|---|---|---|---|---|
   | U | 2,434 | 203 | 2,231 | 2,332 | 0.29% | 0 | 0% |
   | U + forecast | 2,434 | 137 | 2,297 | 2,347 | 0.33% | 7.2 s | 0% |
   | U + forecast + 60 s pad | 2,434 | 87 | 2,347 | 2,386 | 42.44% | 67.2 s | 0% |
   | C-30 | 2,338 | 76 | 2,262 | 2,327 | 0.13% | 0 | 0% |
   | C-30 + forecast | 2,338 | 10 | 2,328 | 2,338 | 0.17% | 7.4 s | 0% |
   | M⁺-30 | 2,338 | 74 | 2,264 | 2,327 | 0.13% | 0 | 41.3% |
   | M⁺-30 + forecast | 2,338 | 10 | 2,328 | 2,338 | 0.17% | 7.3 s | (not replayed) |

   - Source: PAD:4,12,15,25,33,46,54 and T38:58.
   - The on-time column at > 120 s is my arithmetic: served × (1 − Y120) from the same PAD rows.
   - The M⁺-30 + forecast row is a promise-only replay of the same trajectories, so the forced share is not
     re-measured there.

   Add the rows that keep the cost visible:
   - Shared rides: U 22.8%, C-30 13.4% (codex-debate `pooling-share-2026-10-06.txt:2-3`).
   - Served sets differ: 227 riders served only by U, 131 only by C-30 (FJ/served-overlap-check:3).
   - Self-broken promises: M⁺-30 14.5% as a cell mean, 12.4% pooled by rider; C-30 0 (T38:59,111).
2. **Cause table.**
   - Under U, 134 of the 203 riders late by more than 60 s had been drop-exposed by dispatch. Under C-30 it is 4 of
     76 (codex-debate `exposure-check-2026-10-06.txt:2-3`).
   - The three-part ledger split comes from FR:72-75 (weekday) and FR:103-104 (snow).
3. **Hypothetical compensation exposure** (Codex P5, merged), with every money parameter left symbolic.
   - The rule: "pay if the drop-off is more than T later than the first shown promise, whatever the cause".
   - The table counts liabilities per 100 requests:

   | T | U | C-30 | C-30 + forecast |
   |---|---|---|---|
   | 1 min | 5.5 | 2.1 | 0.27 |
   | 2 min | 2.8 | 0.30 | 0 |
   | 5 min | 0.49 | 0 | 0 |
   | 10 min | ≈ 0.05 | 0 | 0 |

   Source: my arithmetic from LATE:5,12,26.

   The reading: at industry-like thresholds of 10 min (Lyft, section B), exposure is almost nil even without a cap. A
   cap matters only for a tight guarantee of 1–2 min.
4. **The cumulative audit** (new, FJ/cumulative-decisive-check), with its scope stated:
   - 0 of 1,256 budget rejections on measured traffic were cumulative-only;
   - fixed traffic: 6 cumulative-only candidates in 4 of 37,214 decisions, none ending in a rejection;
   - synthetic W4 ("pairwise noise"): 4 unique candidates in 3 decisions, at most 1 final rejection.

   It sits next to the exposure screen of uncapped arms (CVP:5,7,17): WP14r FREE has 2 cumulative-only riders at 30 s
   and 13 at 120 s; T3.8 U has 4 at 120 s.
5. **WP14r ladder** (fixed traffic) as the "price per step" table:

   | Step | Riders lost | Late > 60 s riders avoided | Ratio |
   |---|---|---|---|
   | FREE → LOCKS | 45 | 227 | 0.20 |
   | LOCKS → C-120 | 21 | 24 | 0.88 |
   | C-120 → C-60 | 23 | 23 | 1.0 |
   | C-60 → C-30 | 6 | 0 | — |

   Source: LAD:2-6. These are cohort-level ratios, not per-rider rescues.
6. **Rewritten contribution paragraph and limitations.** List the limitations explicitly:
   - H6 negative, −7.13 pp (D03E:238);
   - 0.54 riders per vehicle against ≈ 1.33 in the FleetPy paper;
   - 0 s dwell and one city-wide traffic factor;
   - the forecast gain is not specific to C (FR:65);
   - 34/1,471 forecast pickup displays later than the latest pickup (FR:70).

**What is genuinely new, against the closest prior work.**

| Closest prior work | What it already covers |
|---|---|
| Fielbaum & Alonso-Mora 2020 | Measure unreliability and control it before the decision. Full control raises rejections from 34.5% to 45.6%. D03E:54-56 forbids claiming detection, pre-decision control or the service–stability trade-off as new. |
| Schulz & Pfeiffer 2026 | Drop deadline counted from the first offer (900 s, fixed travel times; D03E:214-217). |
| Hörl & Zwick 2022, strategy B | On-board riders who would otherwise violate their constraints must not be dropped later than "the absolute minimum, given current traffic conditions". That is a per-step, dispatch-only bound at 0 s for riders already late. `claude-work/pdf/hoerl-zwick-2022.txt:529-541`. |
| UberX Share | "additional pickups won't increase your estimated arrival time" (fetched). |
| Forecast-based quoting | Prior work in general. |

- **New (narrow).** On one simulator, one served set and measured traffic factors, the cause-separated
  (dispatch-only) promise contract:
  - serves the same riders as a first-offer deadline: 2,338 = 2,338, with 2,332 riders in common;
  - is never forced (0% against 41.3%) and never breaks its own promise (0 against 14.5%);
  - reaches the same on-time count once a simple forecast is added (2,328 = 2,328).

  It is also the measured finding that the cumulative clause is inert in this regime.
- **Must not claim.**
  - That the trade-off, the control, dispatch-only bounds per step, forecast quoting, guarantees or per-rider
    limits are new.
  - That the cumulative clause improves any outcome.
  - Any satisfaction, revenue or retention effect (D03E:236-245).

**Value, with evidence.**
- **Operator.**
  - An enforceable and auditable promise: 0 forced decisions, 0 self-broken promises.
  - Fewer pooling-caused late riders: late riders who were also dispatch-exposed fall from 134 to 4.
  - Counter-evidence: −96 served riders (2.6 pp of requests) and pooling falls from 22.8% to 13.4%.
  - On-time completions per request are nearly unchanged: 2,262 against 2,231 at 60 s, and 2,327 against 2,332 at
    120 s. So C converts late riders into up-front rejections at about 0.76 rejections per late rider avoided, at
    1 min.
  - Business value is **unconfirmed** (D03E:241-245).
- **Rider.**
  - Lateness against a scheduled time is weighted 2.53 to 3.12 times in-vehicle time in the Wardman et al. 2026
    meta-analysis rows. This is cross-context, not pooled.
  - Counter-evidence: a pooled stated-preference survey (N = 1,006) finds a reliability ratio of about 0.5.
  - Thresholds in practice are in minutes, and the gains here are mostly under 2 minutes.
- **Researcher.** A reusable instrument: the v/e/p ledger, the certificate, the cause split and one frontier with a
  deadline comparator. Others can plug in a different dispatcher and compare on the same table.

**Tier, effort, runs.** T0. About 14–20 h of analysis and writing (my estimate): a consolidation script of 4–6 h, the
exposure and cause tables 3–4 h, chapter text 6–8 h, and one independent re-check round by Codex. **0 new runs.**

**Falsifiable checks (seal before the independent re-check; these are reproduction targets, since the outcomes have
already been seen).**
- **R-a.** An independent reader (Codex, own code) finds, across the 98 measured-traffic C runs, 0 cumulative-only
  budget rejections out of 1,256. On WP14r it finds 6 cumulative-only candidates in 4 decisions.
  - **Kill:** any cumulative-only rejection on measured traffic. Then the sentence "rule C acted as a per-step
    dispatch-only cap on measured traffic" is replaced by the exact count, and the framing is reopened.
- **R-b.** The consolidated table reproduces, within ±1 rider:
  - served 2,434 / 2,338 / 2,338;
  - on-time completions at > 60 s of 2,231 / 2,262 / 2,297 / 2,328 / 2,328 / 2,347;
  - the 227 / 131 served-set split.
  - **Kill:** any mismatch. Stop writing that table until the cause is found.

**Risks.**
- Reads as "nothing new". Mitigate by stating the dispatch-only result against M⁺, which is a real measured
  separation (W07X:54-59 shows the exact mechanism).
- Over-reading r\* as a price per rescued rider: it is a cohort ratio.

### A2. OPTIONAL EXTENSION: cost-first selection under unchanged hard gates (Claude P3, minimal form)

**Idea (one sentence).** Change one pipeline step, the fleet-selection objective. Keep forced-reference priority,
then accepted-request count, then go straight to operational cost. Drop the revision-ordering levels, but keep the
same hard budget, locks, zero switch limits and recovery. Then measure whether the cap alone delivers C's
reliability while pooling recovers.

**Owner questions.**
- O6: the example-thesis pattern of one swapped component with served / cost / sharing curves. Verified: the example
  thesis compares served requests, taxis, cost per served request and total time for 200 requests and 21 taxis
  (`codex-work/r13-paper-text/21020283-3476 (1).txt:159-162,1914-1915`).
- O2: operator efficiency.
- The committee attack: "is your reliability from the cap or from a conservative dispatcher?"

**Why this, verified in code and records.**
- U and C share the hard-vector objective. Both run `ridebound-hard-vector` (tang3/configs/wp4-tier3-v2.json:3), and
  the U and C-30 configs differ only in the drop `hardLimit` (diff of U.json against C-30.json).
- The order of levels is fixed in code (SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs):
  1. forced-reference count (:283-295);
  2. accepted-request count (:297-303);
  3. worst hard utilisation, then the ten revision dimensions (:319-331, with the order at
     SRC/RideBound.Domain/Commitments/CommitmentDimension.cs:19-32);
  4. operational cost (:365-368).
- The utilisation level never discriminates. Its proven best bound is 1,000,000 ppm in 3,503 of 3,503 U decisions
  and 3,506 of 3,506 C-30 decisions (FJ/objective-levels-check:3,7). The reason is that zero limits saturate it
  (SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:612-626).
- So after "accept as many as possible", the dispatcher minimises pickup-ETA and then drop-ETA revisions before cost.
- FREE runs `rolling-cost`, confirmed in the archived WP14r transcript manifest (FJ/probe-wp14r-FREE:4).
- No configuration gives "cap plus cost-first". The fixed-freeze provider sets `hardLimit: null` and no final locks
  (SRC/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:97-108;
  SRC/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:465-474).
- Candidate retention never truncated in T3.8: 0 caps applied, 0 omitted by cap, 0 budgets exhausted
  (FJ/objective-levels-check:5,9). A selection-only change therefore sees the full candidate set, which answers
  Codex's retention concern for this panel.

**New against prior work.** Weighted, ordered and lexicographic objectives are known (D03E:177), and so are soft
replanning penalties and the trade-off (D03E:56). New (narrow): a same-gate ablation in this pipeline. It asks whether
the hard dispatch-only budget can replace the ordered stability objective, and whether accumulation then starts to
bind. **Must not claim:** a new objective or method, or any welfare result.

**Value.**
- **Operator:** possibly more pooling at the same guarantee. WP14r FREE shares 53.1% against LOCKS 21.8% (LAD:2-3),
  but that is a package comparison (AGREED-DIRECTION:104-110).
- **Rider:** the bound holds by construction, but total lateness and waits may worsen.
- **Researcher:** isolates a mechanism the committee will ask about.

**Tier, effort, runs.**
- T2, in `RideBound.Algorithms/Policies` plus a runner config field. Domain and Application stay unchanged.
- It needs a new worktree from `C:/Code/RideBound-noworse` (never `E:/Code/RideBound` or `E:/Code/RideBound-deadline`),
  `dotnet test RideBound.slnx`, a copied harness with its own inventory hash, and docs/18 and docs/19 updates in that
  research repo.
- Effort about 25–35 h (my estimate).
- Runs:
  - Gate 0: 4 equivalence runs;
  - smoke: 2 runs;
  - main: 68 runs, U-cf and C-30-cf × 34 T3.8 cells. That is about 3 h wall at 6 in parallel, using the T3.8
    precedent of 170 jobs in about 7 h (`claude-work/RUNTIME-ESTIMATE-2026-10-07.md:24-25`). The cost-first run time
    is UNCONFIRMED.
- Run on AC power only.

**Sealed-style predictions and kill rules (to be sealed before Gate 0, not run now).**
- **Gate 0.**
  - With the new option OFF, the rebuilt runner must reproduce the archived T3.8 U and C-30 runs on 2 cells (one w08,
    one w17): the same fleet actions and final ledger, using the FORECAST E1/E2 comparison method (FR:23-27).
  - Why this matters: the archived T3.8 binary reports core commit `1ce15e9` (FJ/probe-t38-C30:3), and one later
    `src/` commit exists before HEAD `761915c` (`45f8026`, ADR-077).
  - **Kill:** a mismatch. Stop, or ask the owner to approve 68 control re-runs.
- **P2.1 (the lever).** U-cf shared-ride share ≥ 32.8%, i.e. U's 22.8% + 10 pp. **Kill:** below 25.8% (+3 pp). The
  objective is not the lever; report it and stop.
- **P2.2 (the cap alone protects).** C-30-cf has:
  - late > 60 s against the first promise ≤ 4.25% (C-30's 3.25% + 1 pp);
  - 0 budget overshoots and 0 forced decisions.

  **Kill of the claim "the cap alone suffices":** above 4.25%. Then the ordered objective is doing real reliability
  work, and the thesis must say so.
- **P2.3 (service).** C-30-cf serves ≥ 2,315 (C-30 − 1%), and its absolute shared completions exceed C-30's (about
  313 = 13.4% × 2,338). **Kill:** fewer than 2,315 served. Cost-first blocks later riders.
- **P2.4 (accumulation).** C-30-cf has ≥ 1 cumulative-only budget rejection, measured by the same audit script.
  **Kill of the hypothesis "cost-first makes accumulation bind":** 0. The thesis then says the clause stays inert even
  under cost-first at 30 s.

**Risks.**
- Deadline: T2 work with the thesis not yet edited.
- Gate 0 may fail because of binary drift.
- Realised vehicle distance or busy time as an operator-cost metric is UNCONFIRMED (Codex: field presence is not
  extraction). Use served riders, shared completions and shared passenger-minutes, which existing scripts already
  compute.
- Time-box it to one week. If it is not on track, drop it with no loss to A1.

### A3. Conditional (T1, not recommended unless asked): complete the measured-traffic dial with C-120 and C-0 on the 34 T3.8 cells

**Idea.** Add C-120 (config exists: `tang3/configs/C-120.json`) and C-0, the UberX-Share-like end of the dial
(config-only, `codex-work/STRONG-BASELINE-CODEX.md:54`), to the main panel. Then the B-dial is measured where C-30
actually loses riders: −39 at 08–10 h and −52 at 17–19 h, against −5 at 07–09 h (T38:49-52).

**Owner questions.** O1 (it is only partly run) and O4 (budget use at 120 s on the full panel).

**New against prior work.** Nothing conceptually new. Caps have already been swept at least six times (handoff §4.4).
This item was agreed on 10-08 and then dropped in round 9 because the WP14r ladder exists.

**Value.** A defensible answer to "why 30 s?" on measured traffic, where today only fixed traffic (WP14r) and 8
morning cells exist.

**Tier, effort, runs.** T1. Write C-0.json, seal, smoke, then 68 runs (34 C-120 + 34 C-0, about 3 h wall) and
analysis with A1's scripts. About 10–12 h.

**Predictions and kill (to seal).**
- C-120 serves ≥ 2,386, recovering at least half of the 96-rider gap. WP14r recovered 29 of 50 (LAD:3-6).
- C-120 + forecast: late > 120 s ≤ 0.5%.
- C-120 has ≤ 2 cumulative-only rejections over 34 cells (w07 C-120: 0; WP14r C-120: 4 in 12,525 decisions).
- C-0 serves 2,280–2,338, with late > 60 s within ±0.3 pp of C-30's 3.25%.
- **Kill:** C-120 recovers fewer than 24 riders. There is no measured-traffic sweet spot, and the thesis reports only
  C-30 against U.

**Risk.** It reopens a branch the owner closed; it is low novelty.

### A4. Fallback: finish the current bounded thesis (C-P0 + X-P0)

**Idea.** Write the agreed storyline with the corrected wording of section D and no new analysis.

**Owner question.** O6, "keep the current direction".

**Novelty.** As permitted (fact pack l.65-69), with the A1 caveat that "cumulative" is not an empirical driver.

**Value.** Zero new risk. But O2 gets only a qualitative answer.

**Tier and runs.** No tier, 0 runs. Corrections and consistency checks still take time; Codex estimates 16–24 h
(CXP:115).

**Prediction.** None. **Risk:** presenting completion of the thesis as proof of business value.

### A5. Future work only: who gets how much allowance (Claude P2 express classes + Codex P1 proportional budgets)

**Idea.** Give riders different dispatch budgets, by class or in proportion to trip length.

**Questions.** O6 ("a different kind of promise").

**Why only future work.**
- The first-order screens are upper bounds, because fail-fast witnesses report one blocker per candidate
  (`claude-work/r13-judge-claude/screen-audit-2026-10-10.txt:13`).
- Proportional against uniform at the same mean: +19 requests (0.52 pp) at 60 s and +30 (0.82 pp) at 120 s
  (screen-audit:17,21); about +5 (0.14 pp) at 30 s (`screen-audit-b30-2026-10-10.txt:19`).
- At a 20% express share, the screen counts 114 of the 148 budget-blocked requests as having a passing candidate.
  These are candidates, not completions (`r13-proposer/tier-budget-screen-2026-10-10.txt:4`).
- Novelty collisions:
  - Molenbruch argues for limits proportional to direct ride time (owner PDF extraction lines 145-149);
  - Lyft US12182741B2 rejects matches that "increase an ETA ratio … by a ratio of 0.25" (fetched);
  - Mt-KaRRi's α·T + β (owner note `E:/Code/RideBound/docs/research/wp15-…-2026-08-28.md:139-140`);
  - protecting individual riders is not novel (D03E:211-213);
  - MOIA sells "a shorter arrival window" as "an optional upgrade" (fetched).

**Tier.** T2 in Benchmarking (the per-request policy machinery exists, and the loader accepts a policy list:
SRC/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs:84-93), plus 34–68 runs.

**Prediction and kill (if ever run).** Kill if proportional-mean-60 recovers fewer than 19 requests over uniform-60,
the first-order bound.

**Risk.** Weeks spent on a sub-1-pp effect.

**Not in the list, with the reason.**
- **ML or more data (O5).** Weekday headroom is 2 of 1,471 riders, and snow is one event.
- **Codex P2, speed-up.** No hotspot: the solver uses at most 66–68 µs against about 1.3 s of wall time per decision.
- **Arrival-window promise.** Only the dispatch part is bounded, and MOIA already sells shorter windows.
- **Compensation as its own chapter.** Merged into A1 as one table.
- **Gardner–McKenzie forecast challenger.** At most a sealed appendix; its weekday headroom is at most 2 riders.
- **Pricing in vehicles.** Average productivity is not marginal productivity.
- **4-vehicle stress.** Partly covered by the existing WP9 panel B. At 4 vehicles the free-type arm serves 966 and
  C-30 + locks serves 860 (−11%), against −8.9% for panel A at 8 vehicles
  (`claude-work/fleet-size-wp9-check-2026-10-07.txt` and CVP:19-38, older runner, package comparison).

---

## B. Confirmation table

Status: VERIFIED (I opened the file or URL and saw it), UNCONFIRMED (I could not confirm it myself), WRONG (contradicted;
the correction is given).

### B1. Results and counts

| # | Fact | Anchor I opened | Status |
|---|---|---|---|
| 1 | T3.8 served: U 2,434, C-30 2,338, M⁺-30 2,338, V-30 2,336, M⁺-60 2,347 | T38:46 | VERIFIED |
| 2 | Forced decisions: C-30 0%, M⁺-30 41.3%, M⁺-60 22.5%, V-30 53.8%. Self-broken promises: 0 / 14.5% / 4.2% / 21.6% | T38:58-59 | VERIFIED |
| 3 | The self-broken shares are cell means; pooled by rider, M⁺-30 is 12.4% and M⁺-60 3.4% | T38:111 | VERIFIED |
| 4 | C-30 and M⁺-30 have the same fleet-action sequence in 30 of 34 cells | T38:64 | VERIFIED |
| 5 | Served sets: U ∩ C-30 = 2,207, U-only 227, C-only 131. C-30 ∩ M⁺-30 = 2,332, 6 and 6 | FJ/served-overlap-check:2-4 | VERIFIED (recomputed this round) |
| 6 | Late > 1/2/5/10 min: U 8.34 / 4.19 / 0.74 / 0.08% (max 11.00 min); C-30 3.25 / 0.47 / 0 / 0 (max 3.87); C-30 + forecast 0.43 / 0 / 0 / 0 (max 1.90) | LATE:4-5,11-12,25-26 | VERIFIED |
| 7 | U naive: timely > 60 s 2,231; U + forecast: Y60 5.63%, Y120 3.57%, ext 7.2 s, early 0.33%, timely 2,297; U + forecast + 60 s: Y60 3.57%, Y120 1.97%, early 42.44%, ext 67.2 s, timely 2,347 | PAD:4,12,15 | VERIFIED |
| 8 | C-30 naive: timely 2,262, early 0.13%. C-30 + forecast: Y60 0.43%, Y120 0, early 0.17%, ext 7.4 s, timely 2,328 | PAD:25,33 | VERIFIED |
| 9 | M⁺-30: naive timely 2,264 (Y60 3.17%); with forecast 2,328, ext 7.3 s | PAD:46,54 | VERIFIED. C and M⁺ have the same on-time count with the forecast (Codex judge, XJ:366) |
| 10 | Timely at > 120 s: U 2,332, C-30 2,327, U + forecast 2,347, C-30 + forecast 2,338 | my arithmetic from PAD:4,25,12,33 | VERIFIED arithmetic (Codex's −9 at 120 s, XJ:147, matches) |
| 11 | Shared rides: U 22.8%, C-30 13.4%, M⁺-30 13.1% | `pooling-share-2026-10-06.txt:2-4` | VERIFIED |
| 12 | Riders late > 60 s who were also drop-exposed: U 134/203, C-30 4/76 | `exposure-check-2026-10-06.txt:2-3` | VERIFIED |
| 13 | T3.8 U nonzero dispatch revisions: 187, median 108.6 s | `optimize/report-extras/constraints-and-pooling-2026-10-06.txt:6` | VERIFIED |
| 14 | WP14r ladder: served 1,629 / 1,584 / 1,563 / 1,540 / 1,534; shared 53.1 / 21.8 / 19.4 / 17.3 / 15.7%; exposed 23.8 / 3.9 / 2.6 / 1.3 / 0.4%; late > 60 s 16.82 / 2.97 / 1.47 / 0 / 0% | LAD:2-6 | VERIFIED |
| 15 | WP14r: three ablation factors are inert (freeze, ratchet, pickup lock); decision-induced revisions are 0 earlier and 683 later | `C:/Code/RideBound-noworse/docs/benchmarking/wp14r-013-…-2026-09-05.md:82-86,103-111` | VERIFIED |
| 16 | w07/w07x served (864 requests): U 665, C-30 660, C-60 661, C-90 664, C-120/150/180 666, C-240/300 665. M⁺ forced 58.6 / 35.5 / 13.0 / 6.6 / 6.8 / 2.8 / 1.7% | W07X:22-29; `codex-work/R13-raw-verification.txt:6-21` | VERIFIED |
| 17 | w07x mechanism: traffic 79.0 s + dispatch 68.3 s = 147 s > 90 s, so M⁺ blocks and C accepts. Each divergence is +1 rider | W07X:54-62 | VERIFIED |
| 18 | T3.8 C-30 cost by window: 08–10 h −39, 17–19 h −52, 07–09 h −5 | T38:49-52 | VERIFIED |
| 19 | Occupancy: 0.535 riders per vehicle (U); load 0.814 | `claude-work/load-and-occupancy-2026-10-07.txt:2` | VERIFIED |
| 20 | The FleetPy paper reports ≈ 1.33 on the same data | handoff:206 only | UNCONFIRMED by me (I did not open the PDF) |

### B2. Budget use and the cumulative clause

| # | Fact | Anchor I opened | Status |
|---|---|---|---|
| 21 | Budget use, w07 C-120: 9 of 666 exposed, mean 56.2 s, max 96.7 s; 0 riders at ≥ 90% of B; 0 with ≥ 2 changes; C-150 and C-180 identical | BUC:17,20,23; `codex-work/R13-raw-verification.txt:6-8,22-23` | VERIFIED |
| 22 | Budget use, T3.8 C-30: 33 exposed, mean 10.9 s, max 29.2 s, 4 riders at ≥ 90%, 0 with ≥ 2 changes. T3.8 U: 174 exposed, 12 with ≥ 2 changes, max 3 | BUC:34,37 | VERIFIED. The "median" column is the nearest-rank p50 (rubric correction) |
| 23 | WP14r C-120: 41 of 1,563 exposed, mean 62.3 s, max 119.6 s, 3 riders at ≥ 90%, ≥ 2 changes 0.06% (1 rider), max 2 | WBU:10 | VERIFIED |
| 24 | Cumulative-only riders in uncapped arms: WP14r FREE 2 / 0 / 13 / 6 at 30 / 60 / 120 / 300 s; T3.8 U 4 at 120 s; WP9 panel A b1 1 at 60 s | CVP:5-8,17,31 | VERIFIED |
| 25 | Witnesses: FREE 91.010 + 117.780 = 208.790 s; WP14r C-120 25.661 + 5.924 = 31.585 s; synthetic 81.952 + 10.017 = 91.969 s | `codex-work/R13-cumulative-witnesses.json:8-39` | VERIFIED |
| 26 | **New.** Measured-traffic C runs (T3.8 C-30 × 34; w07/w07x C-30…C-300 × 8 each): 64,371 acknowledged decisions; 1,256 budget-rejected candidates (845 T3.8 + 411 w07/w07x), all "per-step also"; 0 cumulative-only | FJ/cumulative-decisive-check:4-30 | VERIFIED (my script; independent re-check pending, see A1 R-a) |
| 27 | **New.** WP14r: C-30 848 rejections, 0 cumulative-only; C-60 2 cumulative-only in 1 decision; C-120 4 in 3 decisions; 0 of those requests finally rejected. Example: a rider with 51.755 s already spent and a new 80.304 s move gives 132.059 > 120 s | FJ/cumulative-decisive-check:31-45; FJ/per-run-cumulative-only-b:2-4 | VERIFIED |
| 28 | **New.** Synthetic C-120: 6 cumulative-only candidates, but `W4-…-w08` and its `-rerun1` duplicate each other. Unique: 4 candidates in 3 decisions, 1 request finally rejected (an upper bound) | FJ/per-run-cumulative-only-b:5-7 | VERIFIED |
| 29 | Witness fields are before / delta / after / limit, and the evaluator emits a witness only when after > hardLimit | SRC/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs:6-12 (record fields), :88-98 (`afterValue > hardLimit`) | VERIFIED |
| 30 | Recorded witnesses are fail-fast: only the first failing request is reported | SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:222-231 | VERIFIED. This makes cumulative-only counts upper bounds; it cannot hide a per-step violation |
| 31 | Every validation failure is recorded and every pruned candidate is written to the transcript | HardVectorCandidateAssessor.cs:175-190; SRC/RideBound.Runner/Protocol/SolverExecutionEvidenceMapper.cs:46-55 | VERIFIED |
| 32 | Inference: a per-step dispatch-only cap of the same B would have reproduced the T3.8 C-30 trajectories exactly | rows 26, 31, 35 plus a deterministic solver (seed 7, wp4-tier3-v2.json:23) | UNCONFIRMED (inference; for w07 the saturation part was not checked) |

### B3. Code and configuration

| # | Fact | Anchor I opened | Status |
|---|---|---|---|
| 33 | Ordered objective: forced reference, accepted count, [hard-vector: worst utilisation + revision dimensions], operational cost, id rank | SolverBackedFleetSelection.cs:271-303,319-331,365-385 and :510-522; CommitmentDimension.cs:19-32 | VERIFIED |
| 34 | A zero hard limit sets the vehicle's worst utilisation to 1,000,000 ppm | HardVectorCandidateAssessor.cs:612-626 | VERIFIED |
| 35 | The utilisation level is saturated in every T3.8 decision where it appears: best bound 1e6 in 3,503/3,503 (U) and 3,506/3,506 (C-30). Retention: 0 caps applied, 0 omitted by cap, 0 budgets exhausted | FJ/objective-levels-check:3,5,7,9 | VERIFIED |
| 36 | U and C-30 configs differ only in the drop hardLimit 30000; C-120 = 120000; M⁺-30 = no drop hardLimit + dropEtaDeadlineSlackMs 30000 | diff of tang3/configs/U.json, C-30.json, C-120.json, Mplus-30.json (run this round) | VERIFIED |
| 37 | WP4 config: `ridebound-hard-vector`, retention `service-set-stability-portfolio-v1`, at most 2 new requests per vehicle, seed 7 | tang3/configs/wp4-tier3-v2.json:3,10-15,23 | VERIFIED |
| 38 | Archived T3.8 manifest: policyId ridebound-hard-vector, core 1ce15e9, binary a631038b… | FJ/probe-t38-C30:2-4 | VERIFIED |
| 39 | Archived WP14r FREE manifest: policyId rolling-cost, core 38d517d | FJ/probe-wp14r-FREE:3-4 | VERIFIED |
| 40 | 1ce15e9 is an ancestor of HEAD 761915c; `src/` commit 45f8026 (ADR-077) lies between them | `git log 1ce15e9..761915c -- src/` (read-only, this round) | VERIFIED |
| 41 | FREE's objective is cost-first (`RollingCost`) | SolverBackedRidePoolingPolicy.cs:287 | VERIFIED |
| 42 | The fixed-freeze provider strips hard limits and final locks | CommitmentCandidateAssessor.cs:97-108; SolverBackedRidePoolingPolicy.cs:465-474 | VERIFIED |
| 43 | Per-request policy lookup; the normalizer stamps one policy ID; the loader takes a list | HardVectorCandidateAssessor.cs:565-568; FleetPyManhattanNormalizer.cs:448; CommitmentPolicyConfiguration.cs:84-93 | VERIFIED |
| 44 | Fleet placement is ranked by HMAC over artifact SHA, ScenarioId and node, then the first VehicleCount are taken | FleetPyManhattanNormalizer.cs:461-476 | VERIFIED. Nesting holds only if ScenarioId is unchanged (Codex) |
| 45 | Solver work per decision: at most 66 µs (C-30 cell) and 68 µs (U cell); 0 omitted candidates. Median wall time 1.33 s per decision (108 requests, 8 vehicles) | `claude-work/r13-judge-claude/evidence-keys-2026-10-10.txt:9,11`; `evidence-keys-U-w08-2026-10-10.txt:9,11`; `RUNTIME-ESTIMATE-2026-10-07.md:14` | VERIFIED |
| 46 | T3.8: 6 jobs in parallel, about 15 min per job | `RUNTIME-ESTIMATE-2026-10-07.md:24-25` | VERIFIED (estimate basis) |
| 47 | Normalizer caps: 128 requests, 32 vehicles, 96 nodes | `RUNTIME-ESTIMATE-2026-10-07.md:40` (cites FleetPyManhattanNormalizer.cs:326-328) | VERIFIED as cited; I did not open :326-328 |
| 48 | C-0 is config-only and forbids improvements as well | `codex-work/STRONG-BASELINE-CODEX.md:54` | VERIFIED |

### B4. Forecast, data and screens

| # | Fact | Anchor I opened | Status |
|---|---|---|---|
| 49 | Family A (21 cells, cell mean): Y 6.01% → 0.17%; U 9.72% → 3.90%; ext 13.7 s; 34/1,471 pickup displays exceed the latest pickup | FR:42,67-70,83-84 | VERIFIED |
| 50 | Forecast gain is not specific to C: M⁺-30 and V-30 also reach 0.17% | FR:65 | VERIFIED |
| 51 | Snow: 7.19% → 5.94%; 92.5% of late seconds unanticipated | FR:103-104 | VERIFIED |
| 52 | 0.17% is the mean over 21 active cells; over all 34 cells it is 0.51% | D03E:267-268 | VERIFIED |
| 53 | Weekday headroom: 2 of 1,471 riders late with the forecast, 68 without; snow 34 of 601 | `R13-ML-DATA-CLAUDE.md:284-298` | VERIFIED |
| 54 | One weekday with ≥ 1 in of snow in Sep–Dec 2018 (15 Nov) | `claude-work/r13-ml-data-samples/noaa-event-days-2026-10-09.txt:2-3` | VERIFIED |
| 55 | Public trip data: yellow 2018-11 has 8,155,449 rows; FHV 2018-11 has `SR_Flag`; HVFHV starts 2019-02; no verified schema holds a quoted ETA | `R13-ML-DATA-CLAUDE.md:136-139,255-262` | VERIFIED (Claude's file; the rows themselves were not opened by me) |
| 56 | Example rider rq-30b7e083c7b (cell d20181115-s10-r1-w07): booked 7:11:56, promise 7:34:51, alighted 7:38:02, +190.5 s late; with the forecast, +17.6 s | `optimize/report-extras/example-rider-2026-10-06.txt:2-3,60` | VERIFIED |
| 57 | Proportional screen: 11 → 30 passing at a mean of 60 s, 59 → 89 at 120 s; gain 0.52 / 0.82 pp; at 30 s, +5 to +6 (0.14–0.16 pp) | `claude-work/proportional-budget-screen-2026-10-07.txt:2-5`; screen-audit:17,21; screen-audit-b30:17,19 | VERIFIED |
| 58 | Express screen at a 20% share: 114 of 148 requests have a passing candidate | `r13-proposer/tier-budget-screen-2026-10-10.txt:4` | VERIFIED |
| 59 | Budget-block diagnosis: 148 requests blocked only by the budget; U served 116 of them; median overshoot 109.6 s; 2 of 148 blockers had spent budget earlier | `claude-work/budget-block-diagnosis-2026-10-07.txt:2-10` | VERIFIED. Row 26 adds that those 2 also exceeded 30 s in one step |
| 60 | WP9 panel B (4 vehicles, older runner): b1 966, c1 860 served; panel A b1 1,735, c1 1,581 accepted | `claude-work/fleet-size-wp9-check-2026-10-07.txt:4-5`; CVP:19,24,29,34 | VERIFIED |
| 61 | H6 negative: −7.13 pp | D03E:238 | VERIFIED |

### B5. Literature, products and claim boundary

| # | Fact | Anchor I opened | Status |
|---|---|---|---|
| 62 | Fielbaum & Alonso-Mora: "how to control it" is named the most relevant open question; rejection rises from 34.5% to 45.6% under full control | owner-PDF extraction line 1038; Table 5 at lines 942-944 is misaligned | "how to control it" VERIFIED; the row assignment of the percentages follows Codex's PDFium reading (XJ:94) and the Claude judge (CJ:74), not my own extraction |
| 63 | Hörl & Zwick B: on-board riders "not dropped off later than what is the absolute minimum, given current traffic conditions" when they would otherwise violate; plus a penalty per second of violation | `claude-work/pdf/hoerl-zwick-2022.txt:529-541` | VERIFIED |
| 64 | Wardman: MeanLate rows 2.53 (15 observations, 2 studies) and 3.12 (66 observations, 27 studies) | owner-PDF extraction `1-s2.0-S0965856426000662-main.txt:613-617` | VERIFIED |
| 65 | Pooled stated preference: N = 1,006; reliability ratio "around 0.5" | `Value_of_time_and_reliability…txt:25-30,606` | VERIFIED |
| 66 | Molenbruch: a fixed maximum "seems counterintuitive"; uses each trip's direct ride time | `OperationalEffects…txt:145-149` | VERIFIED |
| 67 | Example thesis: figures 4.5–4.8 show served, taxis, cost per served request and total time for 200 requests; 21 taxis; 25% prediction accuracy | `codex-work/r13-paper-text/21020283-3476 (1).txt:159-162,1846,1914-1915` | VERIFIED |
| 68 | UberX Share: "help make sure any additional pickups won't increase your estimated arrival time"; "we cannot guarantee arrival times"; "designed to add 8 minutes to your trip on average" | https://www.uber.com/us/en/ride/uberx-share/ (fetched) | VERIFIED |
| 69 | MOIA: "We will give you a shorter arrival window before you book"; "As an optional upgrade…"; "up to six offers" | https://ride.moia.io/en/express (fetched) | VERIFIED |
| 70 | Lyft: driver more than 10 min after the scheduled pickup gives "$15 in Lyft Credits"; not matched after 10 min gives $50; "applies to rides to the airport"; airport pickups excluded | https://help.lyft.com/hc/en-us/all/articles/115013078668 (fetched) | VERIFIED |
| 71 | Lyft US12182741B2: "reject matches that would add a detour greater than X minutes (e.g., 5 minutes)… increase an ETA ratio by Z (e.g., by a ratio of 0.25)" | https://patents.google.com/patent/US12182741B2/en (fetched) | VERIFIED |
| 72 | Mt-KaRRi α·T + β latest arrival relative to the accepted trip time | the arXiv abstract (fetched) does not contain it; the owner's note quotes the PDF (`wp15-…-2026-08-28.md:139-140`) | VERIFIED via the owner's note only; not in the abstract |
| 73 | One-minute wait-estimate changes had no net abandonment effect (Yu, Zhang & Zhou) | INFORMS page returned 403 | UNCONFIRMED by me (Codex reports it, XJ:99) |
| 74 | D03E:56 forbids claiming unreliability detection, pre-decision control or the service–stability trade-off as new. D03E:211-213 says individual protection is not novel. D03E:236-245: no satisfaction or revenue claims; incremental value unconfirmed | D03E:56,211-213,236-245 | VERIFIED |
| 75 | The owner's note distinguishes RideBound from Mt-KaRRi by its "cumulative budget across the whole promise chain" | `E:/Code/RideBound/docs/research/wp15-…-2026-08-28.md:168-171` | VERIFIED. Per row 26 this is a specification difference, not a measured one |

### B6. Corrections to earlier claims

| # | Claim | Status | Correction and anchor |
|---|---|---|---|
| W1 | CP:62-66: the cumulative cap behaves "exactly" like a per-insertion cap in all 7 populations, and differs only at B ≥ 120 s under free dispatch | WRONG as worded (Codex XJ:68) | In uncapped exposure screens: FREE 2 at 30 s, WP9 A 1 at 60 s, U 4 at 120 s (CVP:5,17,31). In enforced measured C runs, 0 cumulative-only rejections (row 26) |
| W2 | CP:248-249: no rider had more than one nonzero change under any C cap | WRONG outside the measured arms | WP14r C-120 max 2 (WBU:10); synthetic 2 riders (witnesses JSON) |
| W3 | Brief: Claude judge "solver ≤ 68 µs" | VERIFIED | 66 µs (C-30 cell) and 68 µs (U cell) (row 45) |
| W4 | CXP:85: aim for ≥ 1 pp more served with proportional budgets | WRONG as a reachable aim | The first-order upper bound is 0.52 / 0.82 pp (row 57) |
| W5 | CP:604-605: a window is "pooling-proof by construction" | WRONG for terminal arrival | Arrival − first shown promise = Σc + (Σx − forecast allowance). C bounds only Σc (XJ:129,275; the algebra follows from fact pack l.31-36) |

---

## C. Trả lời các câu hỏi của chủ nghiên cứu (O1–O6)

Viết ngắn và dễ hiểu. Mỗi câu có một ví dụ thật lấy từ hệ thống. Con số nào cũng đã kiểm ở mục B.

Một vài tên gọi dùng bên dưới:
- **"Không trần"** là cách điều phối hiện tại (nhánh U). Nó vẫn khóa xe và giờ đón khi khách đặt, nhưng không giới
  hạn việc dời giờ trả.
- **"Luật hạn chót"** là M⁺: giờ trả không được muộn hơn lời hứa đầu quá B giây, tính cả phần do kẹt xe.
- **"Luật C"** chỉ tính phần do hệ thống ghép thêm khách gây ra.

### O1. "C-120 trên tắc đường thật: hình như mình chạy rồi?"

Đúng là đã chạy, nhưng mới một phần.
- **Đã có:** 8 ô buổi sáng 7–9 giờ, ngày 12 và 13/11/2018, tắc đường lấy từ số liệu thật. Có đủ các mức 30, 60, 90,
  120, 150, 180, 240 và 300 giây.
- **Kết quả:** trên 864 yêu cầu, luật C-120 chở 666 khách. Không trần chở 665, còn luật C-30 chở 660. Buổi sáng này
  gần như không mất khách.
- **Chưa có:** C-120 trên 34 ô chính. Mà đó lại là chỗ luật C-30 mất khách nhiều nhất: khung 8 giờ mất 39 khách,
  khung 17 giờ mất 52 khách, còn khung 7 giờ chỉ mất 5.
- **Có thêm:** C-120 trên tắc đường cố định (16 ô) và trên các "thế giới tắc đường tự tạo" (13 lần chạy).

### O2. "Nếu khóa luận chỉ có luật C, phía doanh nghiệp được gì? Người khác có muốn tối ưu nó không?"

**Ví dụ thật.** Ngày 12/11, mẫu 1, khoảng 7:51 sáng:
- Một khách đang trên xe đã trễ 79 giây vì kẹt xe.
- Hệ thống muốn đón thêm một khách mới, việc này làm khách cũ trễ thêm 68 giây.
- Luật hạn chót cộng cả hai, ra 147 giây, vượt mức 90 giây, nên không nhận khách mới.
- Luật C chỉ tính 68 giây do hệ thống gây ra, nên nhận.

Đó chính là chỗ khác nhau giữa hai luật.

**Doanh nghiệp được gì:**
- **Một lời hứa luôn giữ được.** Luật C chỉ tính phần do chính doanh nghiệp gây ra. Trên 34 ô, luật C-30 không lần
  nào phải phá luật của mình. Luật hạn chót cùng mức 30 giây chở đúng bằng số khách (2.338 so với 2.338), nhưng
  41,3% quyết định của nó bị ép phải phá luật.
- **Gần như hết cảnh khách trễ vì bị ghép thêm.** Với không trần, có 203 khách tới trễ quá 1 phút, và 134 người trong
  số đó từng bị hệ thống dời giờ. Với luật C-30, có 76 khách trễ, và chỉ 4 người từng bị dời. 72 người còn lại trễ
  thuần vì kẹt xe.
- **Biết rõ ai gây ra trễ:** phần do hệ thống, phần kẹt xe đoán trước được, phần bất ngờ. Sổ ghi lại cho từng khách.

**Cái giá phải trả:**
- Chở ít hơn không trần 96 khách, tức 2,6 điểm phần trăm số yêu cầu.
- Tỉ lệ khách đi chung giảm từ 22,8% xuống 13,4%.
- Tính trên cùng 3.672 yêu cầu, số khách tới nơi không trễ quá 1 phút gần như bằng nhau: luật C-30 có 2.262, không
  trần có 2.231. Nghĩa là luật C đổi "khách bị trễ" thành "khách bị từ chối ngay từ đầu", khoảng 0,76 khách bị từ chối
  cho mỗi khách tránh được trễ.

**Có lợi về tiền không? Chưa chứng minh được.**
- Luật C chỉ có lời khi một lần thất hứa làm doanh nghiệp tốn hơn một chuyến bị mất, chẳng hạn khi có cam kết bồi
  thường.
- Ngoài đời, ngưỡng bồi thường tính bằng phút. Ví dụ Lyft trả 15 đô tín dụng khi tài xế đến đón muộn quá 10 phút,
  chỉ với chuyến đặt trước đi ra sân bay.
- Trong mô phỏng của ta, kể cả không trần cũng chỉ khoảng 2 khách trên 2.434 trễ quá 10 phút. Vậy luật C chỉ đáng giá
  khi doanh nghiệp muốn hứa rất chặt, cỡ 1–2 phút.

**Người nghiên cứu có muốn tối ưu không?**
- Họ sẽ không tối ưu con số "tổng số giây bị dời", vì khách không nhìn thấy nó.
- Họ có thể muốn tối ưu **đường đánh đổi**: chở được bao nhiêu khách, bao nhiêu khách tới đúng giờ, và lời hứa dài
  bao nhiêu, khi hệ thống chỉ được dời giờ khách tối đa B giây.
- Fielbaum và Alonso-Mora (2020) gọi "làm sao kiểm soát nó" là câu hỏi mở quan trọng nhất. Nhưng chính bài đó đã có
  một cách kiểm soát, nên ta không được nói đánh đổi này là mới.

**Phát hiện mới của phiên này (rất quan trọng khi bảo vệ):**
- Phần "cộng dồn" của luật C chưa bao giờ có tác dụng trên tắc đường thật.
- Trong 98 lần chạy có luật C (64.371 quyết định), có 1.256 cách ghép bị chặn vì ngân sách. Cả 1.256 đều bị chặn vì
  ngay một lần dời đã vượt mức. Không cách ghép nào bị chặn chỉ vì cộng nhiều lần nhỏ lại.
- Lý do: mỗi lần hệ thống định dời giờ một khách thì lần dời đó thường đã lớn sẵn. Với không trần, trung vị là
  108,6 giây.
- Vậy cái làm nên khác biệt là **"chỉ tính phần do hệ thống"**, không phải "cộng dồn". Cộng dồn là lời bảo đảm cho cả
  chuyến đi, nhưng trong mô phỏng này nó chưa từng phải dùng tới.

### O3. "Thêm hứa theo dự báo thì sao? Khách quan tâm gì? Có thật sự là đóng góp không?"

**Ví dụ thật.** Ô ngày 15/11, mẫu 1, khung 7 giờ:
- Khách đặt xe lúc 7:11:56 và được hứa trả lúc 7:34:51.
- Khách tới nơi lúc 7:38:02, tức trễ 190,5 giây, chủ yếu vì kẹt xe.
- Nếu hứa theo dự báo, giờ hứa sẽ là 7:37:44, chỉ lệch 17,6 giây.

**Kết quả trên 34 ô, gộp theo khách:**

| Cách làm | Trễ quá 1 phút | Trễ lâu nhất |
|---|---|---|
| Không trần | 8,34% | 11 phút |
| Luật C-30 | 3,25% | 3,9 phút |
| Luật C-30 + dự báo | 0,43% (10 khách trên 2.338) | 1,9 phút |

Khi thêm dự báo, lời hứa chỉ dài thêm trung bình 7,4 giây, và chỉ 0,17% khách tới sớm quá 1 phút.

**So với cách "hứa dài ra cho chắc":**
- Không trần, có dự báo và đệm thêm 60 giây thì có 2.347 khách tới đúng giờ, nhỉnh hơn 2.328 của luật C-30 có dự
  báo.
- Nhưng khi đó 42% khách tới sớm quá 1 phút, và lời hứa dài hơn khoảng 1 phút. Lời hứa như vậy không còn chính xác.

**Điều phải nói thẳng:**
- Dự báo giúp luật hạn chót y hệt luật C: luật hạn chót có dự báo cũng có 2.328 khách đúng giờ. Vậy điểm riêng của
  luật C không phải "nhiều khách đúng giờ hơn", mà là "không bao giờ phải phá luật".
- Chiều tuyết 15/11, dự báo gần như vô dụng: trễ chỉ giảm từ 7,19% xuống 5,94%, và 92,5% số giây trễ là bất ngờ.
  Phần này sổ ghi lại, không coi là "được miễn trách".

**Khách quan tâm gì? Nói được thật:**
- **Bằng chứng ủng hộ.** Tổng hợp nhiều nghiên cứu về giao thông (Wardman và cộng sự, 2026): một phút trễ so với giờ
  dự kiến bị coi nặng bằng 2,5 đến 3,1 phút ngồi trên xe.
- **Bằng chứng ngược.** Khảo sát 1.006 người ở Hà Lan về xe đi chung: độ tin cậy chỉ được coi trọng bằng khoảng một
  nửa thời gian đi.
- Ngưỡng ngoài đời tính bằng phút, còn phần lợi của ta phần lớn dưới 2 phút.
- **Nên nói:** khách quan tâm việc tới trễ so với giờ được hứa, tính bằng phút. Hệ thống làm giờ hứa sát thực tế hơn
  nhiều mà lời hứa gần như không dài thêm.
- **Không được nói:** khách hài lòng hơn hay đi nhiều hơn. Mô phỏng không có phản ứng của khách: không hủy chuyến,
  không bỏ đi.

**Có phải đóng góp thật không? Có, nhưng hẹp.** Đóng góp gồm:
- một luật hứa tách được "lỗi của mình" khỏi "lỗi của kẹt xe", được cài đặt và có máy kiểm chứng;
- phép đo cho thấy, so với luật hạn chót, nó chở đúng bằng số khách mà không bao giờ bị ép phá luật;
- luật này và dự báo bổ sung cho nhau;
- phát hiện trung thực rằng phần "cộng dồn" không có tác dụng trong vùng thí nghiệm này.

Đây không phải một thuật toán mới, và lợi ích tiền bạc chưa được chứng minh. Với khóa luận đại học thì như vậy là đủ:
khóa luận mẫu năm 2024 của UET cũng chỉ là "hệ thống + một thuật toán có sẵn + một chỉnh sửa nhỏ + thí nghiệm có đánh
đổi rõ".

### O4. "Nới luật C lên 120 giây thì mỗi khách dùng bao nhiêu ngân sách?"

**Tắc đường thật, 8 ô buổi sáng:**
- 666 khách, chỉ 9 người (1,35%) bị hệ thống dời giờ trả.
- Mỗi người bị dời dùng trung bình 56,2 giây, nhiều nhất 96,7 giây (81% ngân sách).
- Không ai dùng tới 90% ngân sách, và không ai bị dời hai lần.
- Mức 150 và 180 giây cho kết quả y hệt mức 120.

**Tắc đường cố định, 16 ô:**
- 1.563 khách, 41 người bị dời (2,6%). Trung bình 62,3 giây, nhiều nhất 119,6 giây.
- 3 người dùng từ 90% ngân sách trở lên.
- Đúng 1 người bị dời hai lần: 25,7 giây rồi 5,9 giây, tổng 31,6 giây.
- Phần cộng dồn chỉ chặn 4 cách ghép trong 3 quyết định. Cả 3 khách mới đó cuối cùng vẫn được chở.

Kết luận: ngân sách 120 giây gần như không bao giờ bị dùng hết.

### O5. "Học máy: có tìm thêm được dữ liệu để học không?"

Có dữ liệu, nhưng nó không giúp được khóa luận.
- **Có:**
  - chuyến taxi vàng New York tháng 11/2018, khoảng 8,16 triệu chuyến;
  - chuyến xe công nghệ tháng 11/2018 có cờ "đi chung";
  - dữ liệu chi tiết hơn từ tháng 2/2019.
- **Nhưng:** không bộ nào có "giờ đã hứa với khách". Vậy không học được đúng thứ ta cần.
- **Trong mô phỏng:** ngày thường, khi đã có dự báo, chỉ còn 2 trên 1.471 khách trễ quá 1 phút. Một mô hình hoàn hảo
  cũng chỉ bớt được 2 người.
- Chỗ còn nhiều trễ là chiều tuyết 15/11 (34 trên 601 khách). Nhưng cả tháng 9 đến tháng 12/2018 chỉ có đúng một ngày
  thường có tuyết từ 1 inch trở lên. Một sự kiện thì không đủ để kết luận.

**Kết luận:** không làm chương học máy, chỉ ghi vào hướng phát triển.

### O6. "Có hướng nào tốt hơn không? Giữ hướng cũ, hay hứa một kiểu khác?"

**Giữ hướng hiện tại, chỉ kể lại cho đúng.**

**Một bước tiếp theo (không chạy thêm):** viết chương kết quả quanh một bảng duy nhất. Bảng ghi, trên cùng số yêu
cầu:
- bao nhiêu khách được chở;
- bao nhiêu khách tới đúng giờ, bao nhiêu khách trễ, bao nhiêu khách tới sớm;
- lời hứa dài thêm bao nhiêu;
- bao nhiêu khách đi chung;
- bao nhiêu lần luật phải phá lời hứa.

Bảng so không trần, luật C, luật hạn chót, mỗi luật có và không có dự báo. Thêm phát hiện "cộng dồn chưa từng có tác
dụng". Codex kiểm lại độc lập trước khi đưa vào luận văn.

**Không đổi sang kiểu lời hứa khác**, như khung giờ, gói "nhanh" hay bồi thường:
- MOIA đã bán "khung giờ tới ngắn hơn" như một gói nâng cấp tùy chọn.
- Chia ngân sách theo độ dài chuyến chỉ cứu thêm tối đa 0,5–0,8 điểm phần trăm số yêu cầu, và ý này đã có trong bài
  của Molenbruch.

**Chỉ khi hạn nộp đã xác nhận và chương kết quả đã viết xong mới làm thêm.** Khi đó đổi đúng một bước của bộ điều phối,
giống cách khóa luận mẫu 2024 đổi một bước chèn khách rồi vẽ số khách, số xe, chi phí:
- Hiện bộ điều phối, sau khi "nhận nhiều khách nhất", sẽ ưu tiên "ít dời giờ khách cũ nhất" trước, rồi mới tới "rẻ
  nhất".
- Thử cho nó ưu tiên "rẻ nhất" ngay, vẫn giữ nguyên luật C.
- Nếu lúc đó khách vẫn đúng giờ mà đi chung nhiều hơn, thì luật C tự nó đủ để giữ lời hứa. Nếu không, ta biết sự ổn
  định đến từ cách chọn phương án, và phải nói rõ như vậy.
- Việc này cần sửa mã, chạy kiểm thử và khoảng 70 lần chạy. Nếu không kịp thì bỏ, không ảnh hưởng gì phần chính.

---

## D. Overclaims that must never appear in the thesis, with corrected wording

| # | Never write | Write instead (anchor) |
|---|---|---|
| D1 | "The cumulative budget is what makes rule C work / better than per-step limits (e.g. Mt-KaRRi)." | "On measured traffic, every budget rejection exceeded B in a single move, so rule C acted as a per-step cap on the dispatch part. The working ingredient is charging only the dispatch part. The cumulative definition guarantees the bound over the whole trip but was not exercised (FJ/cumulative-decisive-check:4-30)." |
| D2 | "Rule C serves more riders than the deadline rule." | "C-30 and M⁺-30 serve the same number (2,338 each; 2,332 in common) and differ in obligation: 0% against 41.3% forced decisions (T38:46,58; FJ/served-overlap:4)." |
| D3 | "Rule C (with forecast) gives more on-time arrivals." | "With the forecast, C-30 and M⁺-30 have the same 2,328 on-time completions at > 60 s; against U, on-time completions per request are similar (2,262 vs 2,231 at 60 s; 2,327 vs 2,332 at 120 s) while late riders fall from 203 to 76 (PAD)." |
| D4 | "C costs 0.76 riders per rider rescued." | "Across the two cohorts, there were 96 fewer served riders and 127 fewer riders late by more than 60 s. The served sets differ (227 U-only, 131 C-only), so this is a cohort ratio, not a per-rider effect." |
| D5 | "30 s is below what riders notice." | Withdrawn (handoff §5 item 3). "30 s is one point on the trade-off curve; the break point lies between 60 and 120 s on fixed traffic (LAD)." |
| D6 | "B = T − traffic margin guarantees arrival within T." / "The window is pooling-proof." | "Lateness against the first shown promise equals Σc + (traffic residual beyond the forecast). C bounds only Σc ≤ B; the residual is measured, not bounded." |
| D7 | "Business benefit / revenue / retention / satisfaction is shown." | "Incremental practical value is unconfirmed; a buyer needs a concrete operator problem, cost and threshold (D03E:241-245)." |
| D8 | "Forecast-based promising is our method / works because of C." | "Forecast quoting is prior practice; here a simple historical profile helps all rules equally (M⁺ and V also reach 0.17%; FR:65)." |
| D9 | "Late riders fell to 0.17%." (unscoped) | "0.17% is the mean over 21 forecast cells; 0.51% over all 34 cells; 0.43% pooled by rider (D03E:267-268; LATE:26)." |
| D10 | "The deadline rule breaks 14.5% of promises." (unqualified) | "14.5% is a cell mean (12.4% pooled by rider) and depends on the optimistic first quote; with a forecast-aware dispatcher it still had 47.6% forced decisions (T38:111; FR:133-134)." |
| D11 | "Industry does not guarantee pooled drop-offs." / "Uber excludes Share from its guarantee." | "The checked UberX Share page says 'we cannot guarantee arrival times'; Uber's delayed-ride guarantee is a driver payment (XJ:103). No claim of universal absence." |
| D12 | "Lyft pays $15 when rides are late." | "Lyft gives $15 in Lyft Credits when the driver arrives more than 10 min after a scheduled pickup, for qualified rides to the airport (fetched)." |
| D13 | "Per-rider / proportional budgets / express tiers are new." | Prior: Molenbruch; Lyft US12182741B2; Mt-KaRRi; D03E:211-213; MOIA Express. |
| D14 | "No rider under rule C was ever moved twice." | "None in the measured C arms; WP14r C-120 had one (25.661 + 5.924 s) and the synthetic C-120 runs had two (WBU:10; witnesses JSON)." |
| D15 | "Median budget use was …" (from BUC) | "Nearest-rank p50 …" (rubric). |
| D16 | "C is needed for 5–10-minute guarantees." | "In this low-load simulation, U already has 0.74% > 5 min and 0.08% > 10 min (LATE:5)." |
| D17 | "Measured traffic" read as real trips | "Simulated execution with city-wide traffic factors derived from measured data (one factor for the whole city)." |
| D18 | "U is free pooling." | "U keeps locks and the stability-first ordered objective; FREE → LOCKS is a package comparison (SolverBackedFleetSelection.cs:319-331; AGREED-DIRECTION:104-110)." |
| D19 | "Unlike Hörl & Zwick, our rule is cumulative." (as the main distinction) | "Unlike Hörl & Zwick B, the bound applies to every rider from booking, with a tolerance B and a per-rider ledger and certificate, and it is compared with a deadline rule under measured traffic factors." |
| D20 | "More data / ML would improve" or "cannot improve" | "On weekdays at most 2 of 1,471 late riders remain with the forecast; the large remainder is one snow afternoon (R13-ML-DATA:284-298)." |
| D21 | "The cumulative clause never matters anywhere." | "Not on measured traffic; on fixed and synthetic traffic it decided at most 7 decisions and at most 1 final rejection (FJ/per-run-cumulative-only-b)." |

---

## E. Remaining disagreement, and what evidence would settle it

1. **Whether any T2 extension (A2) should be attempted before the deadline.**
   - The positions:
     - Codex prefers P3 as a conditional (XJ:5,402).
     - The Claude proposer offered P2 or P3, "never both" (CP:798-804).
     - The Claude judge did not see P3.
   - My verdict: A2 only under two conditions, the deadline confirmed and A1 drafted.
   - **Settles it:** the owner's confirmed deadline and the supervisor's view (the supervisor's name is still
     unknown).
2. **Per-step against cumulative trajectory identity.**
   - Feasibility identity on every recorded measured decision is VERIFIED (rows 26, 30-31).
   - Trajectory identity is an inference that rests on determinism and on utilisation saturation, which was checked
     on T3.8 only.
   - **Settles it:** Codex's independent re-implementation of the audit (A1 R-a), plus the saturation check on
     w07/w07x. A per-step policy run would be definitive but is not proposed.
3. **The operator-cost metric for A2.**
   - Whether realised vehicle distance or busy time can be extracted from transcripts is UNCONFIRMED (XJ:195).
   - **Settles it:** a T0 extraction check on one transcript before sealing A2. Otherwise use served riders, shared
     completions and shared passenger-minutes only.
4. **Gate 0 feasibility of A2.**
   - The current HEAD differs from the archived T3.8 binary's commit by one `src/` commit (row 40).
   - **Settles it:** the 4-run equivalence gate.
5. **The weight of rider evidence.**
   - Wardman's 2.5–3.1 against a pooled reliability ratio of about 0.5.
   - Yu, Zhang & Zhou (UNCONFIRMED by me).
   - Neither measures this ledger. **Settles it:** a rider study, outside this thesis. Present both sides, as in C/O3.

---

## Appendix: files written this round (all in `claude-work/r13-final-judge/`, outputs opened with mode "x")

| Script | Output | Purpose |
|---|---|---|
| `probe_structure.py` | `probe-t38-C30-2026-10-10.txt`, `probe-wp14r-FREE-2026-10-10.txt` | manifest policy IDs, commits, witness fields |
| `probe_selection.py` | `probe-selection-t38-U-2026-10-10.txt` (1 byte: the probe found no match; kept) | first look at the selection evidence; superseded by an inline print |
| `cumulative_decisive_check.py` | `cumulative-decisive-check-2026-10-10.txt`; logs `run-cumulative-decisive.std*.txt` (first attempt failed on `-rerun1` folders, kept) and `run-cumulative-decisive-b.std*.txt` | candidate-level test of the cumulative clause, 159 runs |
| `per_run_cumulative_only.py` | `per-run-cumulative-only-b-2026-10-10.txt`; `per-run-cumulative-only-2026-10-10.txt` is a kept syntax-error log of an inline attempt | per-run breakdown and duplicate removal |
| `objective_levels_check.py` | `objective-levels-check-2026-10-10.txt`; logs `run-objective-levels.std*.txt` | saturation of the utilisation level; candidate truncation |
| `served_overlap_check.py` | `served-overlap-check-2026-10-10.txt` | U / C-30 / M⁺-30 served-set overlap |

Power was on battery at 86% for these short reads (about 5 min of CPU in total; no long job). There were no
simulations, builds, installs or deletions. No file outside this folder and this verdict was written.
