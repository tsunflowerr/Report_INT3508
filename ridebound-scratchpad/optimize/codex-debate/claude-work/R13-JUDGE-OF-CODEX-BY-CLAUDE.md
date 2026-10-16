# R13 judge of Codex's proposals, Claude side (2026-10-10)

What I judged: `codex-work/R13-PROPOSALS-CODEX.md` (P0–P6, the O1/O4 audit, the Vietnamese O2/O3 answers and the
"weakest point" paragraph) and `codex-work/R13-SURVEY-CODEX.md`, using the rubric `ROUND13-RUBRIC.md`.
I did not read `claude-work/R13-PROPOSALS-CLAUDE.md`. No simulation, build or install was run, and nothing was written
outside `claude-work/` and my scratchpad.

Zero-run helper checks I added (scripts and outputs in `claude-work/r13-judge-claude/`; outputs opened in mode "x"):
- `screen_audit.py` → `screen-audit-2026-10-10.txt` (mean 60/120 s) and `screen_audit_b30.py` →
  `screen-audit-b30-2026-10-10.txt` (mean 30/45 s). They re-derive the proportional-budget screen from the 34 T3.8 C-30
  transcripts and add the blockers' trip lengths, witness counts, kappa normalised on all requests, and a loss side.
- `evidence_keys.py` → `evidence-keys-2026-10-10.txt` (C-30 d20181114-r1-w07) and `evidence-keys-U-w08-2026-10-10.txt`
  (U d20181115-r2-w08). They show how much candidate-generation and solver work each decision does in the thesis corpus.

Short paths used below: `CW` = `.../codex-debate/codex-work/`, `CL` = `.../codex-debate/claude-work/`,
`J` = `CL/r13-judge-claude/`, `NW` = `C:/Code/RideBound-noworse/`, `HO` = `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md`,
`FR` = `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md`, `D03E` = the owner's newer
`E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (read only).

---

## 1. Step 1: verification table

Verdicts: VERIFIED (I opened the file or URL and saw it), UNVERIFIED (I could not open it), WRONG (contradicted; the
correct value and its anchor are given).

### 1a. Codex's independent O1/O4 audit (background to every proposal)

| # | Codex claim | Anchor I opened | Verdict | Note |
|---|---|---|---|---|
| 1 | Main audit: 196 runs, 389,518 verified frames | `CW/R13-raw-verification.txt:3` | VERIFIED | |
| 2 | w07 served: U 665, C-30 660, C-60 661, C-90 664, C-120/150/180 666, C-240/300 665, all of 864 | `CW/R13-raw-verification.txt:6-13,21` | VERIFIED | Matches the fact pack §2. |
| 3 | Mplus forced 58.6/35.5/13.0/6.6/6.8/2.8/1.7% | `CW/R13-raw-verification.txt:14-20` (`forced_cell_mean_percent`) | VERIFIED | |
| 4 | T3.8 C-30: 33 exposed, mean 10.9, max 29.2 s, 4 riders ≥90% of B, 0 with ≥2 changes; U: 174 exposed, 12 with ≥2, max 3 | `CW/R13-raw-verification.txt:4-5` | VERIFIED | |
| 5 | Median correction: w07 C-30 riders 1.974 and 10.048 s, conventional median 6.011 s | `CW/R13-raw-verification.txt:10` | VERIFIED | Already accepted in the rubric. |
| 6 | C-120 = C-150 = C-180 and U = C-240 = C-300 as exact rider vectors | `CW/R13-raw-verification.txt:22-25` | VERIFIED | |
| 7 | WP14r FREE: 1,629 served, 388 exposed, 50 with ≥2 changes, max 3, **13 riders pass every 120-s step but exceed 120 s in total**; WP14r C-120: 1,563/41/1/2; synthetic C-120: 1,205/28/2/2 | `CW/R13-extra-raw-verification-v2.json` (`summary`); cross-check `CL/wp14r-budget-use-2026-10-10.txt:4,10` (388 exposed; ≥2 changes = 3.07% of 1,629 = 50; C-120 41 exposed, 0.06% ≈ 1) | VERIFIED | A real finding the fact pack lacked: "rarely exercised" holds, but not "never anywhere". |
| 8 | Witnesses: 91.010 + 117.780 = 208.790 s; 25.661 + 5.924 = 31.585 s; 81.952 + 10.017 = 91.969 s | `CW/R13-cumulative-witnesses.json:8-39` | VERIFIED | |
| 9 | No C-120 folder in the T3.8 archive | `CW/R13-raw-verification.txt:26` | VERIFIED | Scoped to the named archive, as Codex says. |

### 1b. P1: per-trip budget allocation

| # | Codex claim | Anchor I opened | Verdict | Note |
|---|---|---|---|---|
| 10 | Screen: 30 vs 11 passing at mean 60 s; 89 vs 59 at mean 120 s | `CL/proportional-budget-screen-2026-10-07.txt:2-5`; re-derived in `J/screen-audit-2026-10-10.txt:17,21` | VERIFIED | Reproduced exactly. |
| 11 | The screen uses the served-cohort mean direct time and ignores cascades | `CL/proportional_budget_screen.py:4-6,38,42` | VERIFIED | The served-vs-all choice barely matters: with kappa set on all 3,672 requests (mean 434.2 s vs 423.8 s) the counts are 30 and 88 (`J/screen-audit-2026-10-10.txt:5-6,19,23`). |
| 12 | 148 budget-only blocks; U served 116; median overshoot 110 s; 2/148 blockers had spent budget before | `CL/budget-block-diagnosis-2026-10-07.txt:2-10` | VERIFIED | |
| 13 | Molenbruch: relative ride-time limits, 78 combinations | `CW/r13-paper-text/OperationalEffects…txt:61-63` | VERIFIED | The same paper argues **exactly P1's rationale** (lines 155-161): a fixed maximum for all users "seems counterintuitive. It implies that a detour of a certain length might be feasible for a short trip, but not for a longer one … Therefore, this study takes into account the direct ride time of each individual trip." Codex cites the paper as "motivation", not as the collision it is. |
| 14 | Schulz/Pfeiffer tie acceptance to detour relative to direct time | `CW/r13-paper-text/s00291-026-00847-0.txt:23-24` | VERIFIED | The acceptance model is assumed, not measured. |
| 15 | Implicit: the ≥1 pp served gain over a uniform comparator at the same mean is a reasonable aim | `J/screen-audit-2026-10-10.txt:17,21`; `J/screen-audit-b30-2026-10-10.txt:17-24` | **WRONG** | The screen's own first-order **upper bound** is below the target. Proportional minus uniform: +19 requests (0.52 pp of 3,672) at mean 60 s, +30 (0.82 pp) at mean 120 s. At the thesis's operating point (mean 30 s) it is +6, −1 on the loss side, so net ≈ +5 (0.14 pp). The total U−C-30 gap is 96 (2.61 pp). Codex quotes the counts but never converts them to pp. |
| 16 | "Need … a real per-rider-budget contract"; T2 24–40 h | `NW/src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:241-247` (policy looked up per request from `request.CommitmentPolicyId`); `NW/src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:565-568`; `NW/src/RideBound.Contracts/Protocol/OnlineEventModels.cs:70` (per-request field); `NW/src/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs:84-89,151` (a `policies[]` array); `NW/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:448` (today one `configuration.CommitmentPolicyId` for every request) | **WRONG (overstated)** | The per-rider contract already exists. Each request names its own policy, and the catalogue can hold many. Binned, or even per-rider, budgets need a multi-policy config plus a per-request assignment in the Benchmarking normalizer and new fixtures. No Domain/Application change is needed. It still needs a worktree, regenerated fixtures and `dotnet test`. I did not verify a multi-policy run end to end. |
| 17 | `direct = maxRideTimeMs / 1.5` (used by the screen) | `NW/.../FleetPyManhattanNormalizer.cs:428-445` (`maxRide = direct × MaximumRideTimePermille/1000`, ties-to-even); `HO:204` ("1,5 lần đi thẳng") | VERIFIED | Exact up to rounding. |

### 1c. P2: incremental candidate evaluation

| # | Codex claim | Anchor I opened | Verdict | Note |
|---|---|---|---|---|
| 18 | Exact cache exists, `ForwardSlackProfile.cs:477` | `NW/src/RideBound.Algorithms/Candidates/ForwardSlackProfile.cs:477-535` (`ForwardSlackProfileCache`, `GetOrBuild`) | VERIFIED | |
| 19 | Evaluation/cache use, `InsertionCandidateGenerator.cs:709` | `NW/.../InsertionCandidateGenerator.cs:706-717` (`EvaluateRoute` signature), cache lookup at `:770-776` | VERIFIED (line approximate) | The cache call is at :770, not :709. |
| 20 | Claim boundary forbids importing the 3.8× figure and the full constant-time test | `NW/docs/03-related-work-and-claim-boundary.md:95` | VERIFIED | |
| 21 | Gschwind/Drexl: "exact amortized constant-time algorithm" | Publisher page returned 403. Substance confirmed in `NW/docs/03…:95` and `NW/docs/21-paper-to-design-evidence.md:462` | UNVERIFIED wording; substance VERIFIED | |
| 22 | The example thesis compares processing time with service ("thời gian xử lý"); 25% prediction accuracy is assumed | `CW/r13-paper-text/21020283-3476 (1).txt:1935-1937, 1977-1990` | VERIFIED | Supports P2's *style* match to O6. |
| 23 | Implicit precondition: a hotspot may exist ("proceed only if ≥20% of decision CPU") | `J/evidence-keys-2026-10-10.txt`: 455 decisions, generation work 7,697 units in total (max 78), validation 4,279 (max 18), solver deterministic time 10,329 µs in total (max 66 µs), **0 omitted candidates**; `J/evidence-keys-U-w08-2026-10-10.txt`: 694 decisions, 10,612 units (max 80), 0 omitted; wall 565,955 ms and 900,783 ms (`run-00.json`) | **Contradicted by existing records** (Codex left it open) | About 15–17 generation units per decision, against a cap of 10,000 (`tang3/configs/wp4-tier3-v2.json`) and the 468 units that a 2-incumbent micro-benchmark spends (`NW/docs/benchmarking/wp7-015-…-2026-08-17.md:80-85`). Wall time is about 1.2–1.3 s per decision, so the targeted stage is very unlikely to be ≥20% of it. Inference: the time goes elsewhere (simulator, protocol, hashing), but I did not profile that. |
| 24 | Implicit: no prior speed work, "need a profiler" | `NW/docs/benchmarking/wp7-015-hot-path-and-semantics-closure-evidence-2026-08-17.md:32-74` (ADR-039: cache key was the bottleneck; generator −23…−39%); `NW/docs/benchmarking/post-wp10-exact-reuse-optimization-2026-08-23.md:41-49,82-90` (ADR-052: harness `tools/RideBound.CandidateHotPathBenchmark`; end-to-end "mixed/noisy") | **Missed by Codex** | Two exact-reuse passes and a benchmark harness already exist. |

### 1d. P0 and the O2/O3 answers

| # | Codex claim | Anchor | Verdict | Note |
|---|---|---|---|---|
| 25 | C-30 2,338 vs U 2,434: −96 = 2.61 pp of 3,672; 0 forced | `HO:166,172,180` | VERIFIED | 96/3,672 = 2.614%. |
| 26 | Late >1 min: U 8.34%, C-30 3.25%, C-30+forecast 0.43% | `HO:194-196`; `CL/cap-vs-pad-frontier-2026-10-07.txt:4,25,33` | VERIFIED | Pooled by rider, correctly labelled "34 ô". |
| 27 | 34/1,471 forecast pickup displays exceed the old latest pickup (cited `FR:68`) | `FR:70` | VERIFIED (line 70, not 68) | |
| 28 | Matched-cost comparison (cited `FR:37`) | `FR:40-42` | VERIFIED (line approximate) | |
| 29 | Fielbaum/Alonso-Mora Table 5: rejected 34.5% base, 31.2% intermediate, 45.6% fully controlled; user cost 9.56 → 11.6 | `pdftotext -layout` of `C:/PDF/Paper/Unreliability_in_ridesharing_systems_Measuring_cha.pdf` p. 17 | VERIFIED | The extracted table is misaligned; Codex's row assignment is the consistent reading. |
| 30 | UberX Share: "we cannot guarantee arrival times"; additional pickups "won't increase your estimated arrival time" | https://www.uber.com/us/en/ride/uberx-share/ (fetched): "(note: because of traffic and other possible delays, we cannot guarantee arrival times)." | VERIFIED | |
| 31 | Schmidt et al. 2026: "An ambitious commitment attracts higher demand than a conservative one" | https://arxiv.org/abs/2609.11950 (fetched) | VERIFIED | Model-derived. |
| 32 | DoorDash: "customers don't see large changes in their ETAs" | careersatdoordash.com returned 403 | UNVERIFIED | Not central. |

### 1e. P3, P4, P5, P6

| # | Codex claim | Anchor | Verdict | Note |
|---|---|---|---|---|
| 33 | P3: CQR Theorem 1 assumes exchangeability | https://arxiv.org/pdf/1905.03222 p. 5: "Theorem 1. If (Xi, Yi), i = 1, . . . , n + 1 are exchangeable, then the prediction interval … satisfies P{Yn+1 ∈ C(Xn+1)} ≥ 1 − α." | VERIFIED | Marginal coverage only, as Codex says. |
| 34 | P3: Uber DeepETA "a specific quantile of the ETA distribution" | Uber DeepETA blog (fetched): "Other use cases may call for a specific quantile of the ETA distribution." | VERIFIED | |
| 35 | P3: Rauh appointment ranges; Schulz/Pfeiffer window-length trade-off | `CW/r13-paper-text/s00291-025-00812-3.txt:24-27`; `…s00291-026-00847-0.txt:35-38` | VERIFIED | |
| 36 | P3: "pooled distribution-valuing stated preferences" support windows | `CW/R13-SURVEY-CODEX.md:25` (Codex's own note: "attributes are time distributions, not quote-revision ledgers") | VERIFIED source, **misapplied** | Alonso-González values reliability, not window promises. |
| 37 | P4: 36 parameter candidates; sealed thresholds weekday ≤0.2 pp, incident ≥1 pp | `CW/ROUND12-REPLAY-PROTOCOL-CODEX.md:28,48-50` | VERIFIED | |
| 38 | P4: snow 7.19% → 5.94%, 92.5% unanticipated | `CW/ROUND12-FACTS-CODEX.md:43`; `HO:270` | VERIFIED | |
| 39 | P5: Via/Cohen: "works well for long waiting times but not for long travel times" | Authors' PDF (https://maxccohen.github.io/Frustration-Based-Promotions.pdf), abstract, text extracted by pdftotext | VERIFIED | Negative for a drop-time product, as Codex says. |
| 40 | P5: Lyft "$15 in Lyft Credits"; airport pickups excluded | https://help.lyft.com/hc/en-us/all/articles/115013078668 (fetched): "If your driver arrives more than 10 minutes after your scheduled pickup time … you'll automatically receive $15 in Lyft Credits."; "Scheduled rides for airport pickups are excluded from this offer." | VERIFIED | The threshold is **10 minutes** (see the P5 critique). |
| 41 | P5: Grubhub "latest estimated delivery time range presented to you post-checkout"; at least $5 | `CW/R13-public-grubhub-terms-clean.txt:22-25` | VERIFIED | The remedy is a "GHG Perk … at least $5 in value", and the terms exclude "cash, payment method credit, refunds". Calling it "future-use credit" is a paraphrase. |
| 42 | P5 prediction: C+forecast cuts nominal credit exposure by ≥25% vs uniform padding at equal extension | `CL/cap-vs-pad-frontier-2026-10-07.txt:25,26,33` (C-30 Y60: naive 3.25%, pad 15 s 1.84%, forecast 0.43% at 7.4 s) | Already determined by existing data | At a >60-s rule the reduction is about 77–87%, already known, so this "prediction" is not a test. |
| 43 | P6: HVFHV fields; starts 2019; Chicago times rounded to 15 min; Yellow Oct–Nov 2018 links | `CL/R13-ML-DATA-CLAUDE.md:136,139,180` | VERIFIED | Codex missed FHV 2018-11 with `SR_Flag` (`R13-ML-DATA-CLAUDE.md:138`). |

### 1f. Closest prior for P1 that Codex did not cite (checked by me)

| Source | Anchor | Verdict | Collision |
|---|---|---|---|
| Mt-KaRRi (Laupichler et al. 2026, arXiv 2605.11798) | arXiv PDF text: "If I increases the trip time of r′ to more than α·T + β … then I is infeasible. Thus, every rider is guaranteed a latest possible arrival time relative to the trip time they originally accepted." α = 1.4, β = 10 min. The owner's note `E:/Code/RideBound/docs/research/wp15-commitment-design-new-paper-evidence-2026-08-28.md:130-171` already discusses it. | VERIFIED | A per-rider bound that is proportional to trip time. |
| Lyft US12182741B2 | https://patents.google.com/patent/US12182741B2/en (fetched): "may reject matches that would increase an ETA ratio" (example 0.25), "reject matches that would add a detour greater than X minutes" | VERIFIED | A per-match limit as a ratio of the initially quoted ETA. |
| Elmi et al. 2026 | `D03E:211-213` ("cơ chế bảo đảm cho khách được chọn … Bảo vệ từng khách hoặc bảo đảm ETA riêng lẻ không phải novelty") | VERIFIED (boundary text) | Differentiated per-customer guarantees are already in the strict boundary. |

---

## 2. What my zero-run checks add (central to the P1 and P2 verdicts)

**P1 screen, `J/screen-audit*.txt`:**
1. **The blockers are long-trip riders.** The 145 distinct co-riders whose budget blocked a request average 633.9 s of
   direct time (median 565.2 s), against 423.8 s for served riders (`J/screen-audit-2026-10-10.txt:6,8`). Proportional
   allocation wins at first order because it gives exactly these riders about 1.5× B. For 57.5% of riders the budget
   falls below the uniform B (line 10).
2. **The screen is optimistic because the recorded evidence is fail-fast.** All 193 budget-pruned candidate rows carry
   exactly one witness (`J/screen-audit-2026-10-10.txt:13`). The validator stops at the first failing request:
   `NW/src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:222-231` ("the first failing request … are
   the only ones ever reported"). Full collection needs the `retained-portfolio-full-witness-v1` profile
   (`NW/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:28-29,171-174`). The T3.8 config
   `tang3/configs/wp4-tier3-v2.json` has no such profile. Witnesses are also emitted only for riders over the limit
   (`NW/src/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs:86-98`). So co-riders who are hidden, or who were
   under 30 s, are never tested against their *smaller* proportional budgets. Every count in the screen is an upper bound.
3. **The loss side is near zero at first order.** No C-30 rider's realised S exceeds kappa·direct at mean 60/120, and 1
   rider does at mean 30/45 (`J/screen-audit-2026-10-10.txt:18,22`; `J/screen-audit-b30-2026-10-10.txt:18,22`). My worry
   about new blocks did not materialise in realised insertions.
4. **Budget level beats allocation.** Raising a uniform B from 60 to 120 s unblocks +48 (11 → 59). Reallocating at a
   fixed mean of 60 s unblocks +19 (`J/screen-audit-2026-10-10.txt:17,21`). On w07 mornings a uniform C-120 already
   serves 666 ≥ U's 665 (`CW/R13-raw-verification.txt:6,21`), so those cells have no service headroom left for
   allocation.

**P2 workload, `J/evidence-keys*.txt`:** see row 23. In the thesis regime (about 0.54 riders per vehicle,
`CL/load-and-occupancy-2026-10-07.txt:2`), candidate search is tiny and never truncated. There is nothing to speed up,
and no "more candidates within a compute budget" to unlock.

---

## 3. Step 2: scores (1–5)

Criteria: Op = operator value, Rid = rider value, Res = research value, Nov = novelty within the strict boundary,
Fea = feasibility in ~5 weeks, Evi = evidence strength and falsifiability, Fit = fit to one storyline.

| Proposal | Op | Rid | Res | Nov | Fea | Evi | Fit | Sum |
|---|---|---|---|---|---|---|---|---|
| P0 keep current storyline | 3 | 3 | 3 | 2 | 5 | 3 | 5 | **24** |
| P1 per-trip budget allocation | 2 | 2 | 2 | 1 | 4 | 3 | 4 | 18 |
| P4 damped-forecast challenger | 2 | 2 | 2 | 1 | 5 | 2 | 4 | 18 |
| P3 frozen arrival window | 2 | 2 | 3 | 2 | 4 | 2 | 2 | 17 |
| P5 priced compensation | 2 | 2 | 1 | 1 | 5 | 1 | 3 | 15 |
| P2 incremental candidate evaluation | 1 | 1 | 2 | 1 | 2 | 3 | 2 | 12 |
| P6 HVFHV duration benchmark | 1 | 1 | 2 | 1 | 2 | 3 | 1 | 11 |

One-line justification per score:

**P0.**
- Op 3: compared with a deadline at equal service (2,338 = 2,338), C is never forced (0% vs 41.3%) and breaks no
  rider's promise (0 vs 14.5%) (`HO:166,172-174`). It costs 2.61 pp against U. There is no revenue evidence
  (`D03E:236-237`).
- Rid 3: late >1 min falls 8.34 → 3.25 → 0.43% and the maximum 11 → 3.9 → 1.9 min (`HO:194-196`). Riders served on
  time per request rise: U 60.76% vs C-30 61.60%, and with forecast 62.55% vs 63.40% (`CL/cap-vs-pad…:4,12,25,33`).
  Counter-evidence: riders do not value S itself, and Cohen finds no benefit from compensating travel-time frustration.
- Res 3: a reusable instrument (ledger, certificate, cause split). Schmidt et al. name "personalized commitments" as
  open (`CL/R13-SURVEY-CLAUDE.md:162-163`).
- Nov 2: a narrow combination only. Hörl & Zwick B, the UberX Share statement and Mt-KaRRi sit close.
- Fea 5: T0 only, 0 runs.
- Evi 3: sealed plans, cross-checked and replicated. But the cumulative part is unexercised on the main panel, there is
  one week of traffic, and H6 is negative.
- Fit 5: it is the storyline.

**P1.**
- Op 2: first-order upper bound +0.52 pp (mean 60), +0.82 pp (mean 120), ≈ +0.14 pp at mean 30; the total ceiling is
  2.61 pp (§2).
- Rid 2: moves dispatch drift onto long-trip riders (blockers 634 s vs 424 s). No rider evidence favours relative
  budgets; Schulz/Pfeiffer's acceptance curve is assumed.
- Res 2: a parametrisation study of an existing constraint.
- Nov 1: Molenbruch's own argument (row 13), Mt-KaRRi α·T + β, the Lyft ETA ratio and Elmi guarantees (§1f). What
  remains new is rule C itself.
- Fea 4: the per-request policy machinery exists (row 16). 32 runs ≈ 1.5 h at about 15 min per job with 6 in parallel
  (`CL/RUNTIME-ESTIMATE-2026-10-07.md:24-25`). It still needs a worktree, regenerated fixtures and `dotnet test`.
- Evi 3: explicit kill gates (good), but the target exceeds its own optimistic bound and the "16 held-out cells" panel
  is not defined.
- Fit 4: extends rule C cleanly.

**P4.**
- Op 2 and Rid 2: weekday headroom is ≤0.17 pp (`FR:42`).
- Res 2: a null-or-positive adaptation study.
- Nov 1: Gardner–McKenzie is established.
- Fea 5: the protocol is ready (row 37).
- Evi 2: the incident claim rests on one snow afternoon (15 Nov, w14/w15), whose historical-method outcome
  (7.19 → 5.94%) is already known.
- Fit 4: stays inside the forecast part.

**P3.**
- Op 2: Codex cites no pooled-window operator evidence. MOIA sells "a shorter arrival window" as an upgrade
  (`CL/R13-SURVEY-CLAUDE.md:271-273`), but Codex did not use it.
- Rid 2: the cited evidence is misapplied (row 36). Lab evidence on intervals is mixed
  (`CL/R13-SURVEY-CLAUDE.md:242-253`).
- Res 3: a calibrated window under a certified dispatch budget would be a reusable benchmark.
- Nov 2: CQR exists; quantile windows from critical fractiles (Hosseini et al., arXiv 2508.01032,
  `E:/Code/RideBound/docs/research/wp15-…-2026-08-28.md:57-114`); conformal bus windows
  (`CL/R13-SURVEY-CLAUDE.md:232-235`).
- Fea 4: the T0 replay needs no runs.
- Evi 2: on weekdays C-30 + forecast already lands within ±60 s for 99.4% of riders (`CL/cap-vs-pad…:33`), with MAE
  7.0 s (`FR:48`). The coverage and width targets would be met trivially; only the snow afternoon can discriminate.
- Fit 2: it changes the promised object (Codex says so).

**P5.**
- Op 2: business-legible, but at an industry-like threshold (Lyft: 10 min) C arms have zero exposure (max 3.9 min) and
  U 0.08% (`HO:194-195`). At >60 s it is just Y60 times dollars.
- Rid 2: Cohen's result is negative for travel time.
- Res 1: a unit conversion.
- Nov 1: compensated guarantees are long established.
- Fea 5: T0.
- Evi 1: the ≥25% target is already met in existing data (row 42).
- Fit 3: framing, not mechanism.

**P2.**
- Op 1: no hotspot in the thesis corpus and 0 omitted candidates (row 23).
- Rid 1: zero output change by design.
- Res 2: engineering on a well-studied topic (Savelsbergh slack, Gschwind–Drexl, Schulz–Pfeiffer precomputation).
- Nov 1: incremental slack and precomputation have precedent (`D03E:175-177`).
- Fea 2: 48–84 h of certified-validator surgery after two prior passes (row 24).
- Evi 3: Codex's gates are falsifiable, and existing data predict the first gate fails.
- Fit 2: a second, compute-only storyline.

**P6.**
- Op 1 and Rid 1: no promise label (row 43).
- Res 2: duration-quantile benchmarks are common.
- Nov 1.
- Fea 2: a T3 pipeline (40–64 h); HVFHV starts 2019 while the simulator's traffic is November 2018.
- Evi 3: a clear pinball target with chronological folds.
- Fit 1: a side branch.

---

## 4. Step 3: verdicts

| Proposal | Verdict | One-line reason | Biggest single risk |
|---|---|---|---|
| P0 | **KEEP** | Cheapest, best evidenced, and Codex's honest wording plus the new accumulation witnesses improve it | The committee asks "why cumulative?": no main-panel rider has ≥2 dispatch changes, and the preregistered H6 lost 7.13 pp |
| P1 | **MERGE-WITH(P0)**, as a T0 sensitivity section only | The corrected screen gives ≤0.5–0.8 pp at first order and no novelty. Start T2/T1 only if the owner accepts a frontier-style target well below 1 pp | Weeks spent chasing a sub-1-pp effect that cascades can erase |
| P2 | **REJECT** | No hotspot and no truncated search in the thesis corpus; two prior exact-reuse passes exist; no rider or business link | 50–80 h of certified-validator changes for an unmeasurable gain |
| P3 | **REJECT** (future work) | Changes the promised object late; no weekday headroom; the signal rests on one snow afternoon | Re-founding the thesis five weeks before the deadline |
| P4 | **MERGE-WITH(P0)**, optional sealed appendix | Cheap and ready (the handoff's pending item, `HO:482-487`), but not headline material | Inference from one incident |
| P5 | **MERGE-WITH(P0)**, one framing paragraph or table, no work package | Puts the existing lateness result in operator currency | Being read as a revenue or retention claim |
| P6 | **REJECT** (answer O5 in text) | T3, off-storyline, no promise labels | Domain shift (2019+ HVFHV against 2018 traffic) and deadline |

**Codex's top 3, ranked by me:** (1) P0, including Codex's O1/O4 audit and the 13-rider accumulation witness; (2) P1,
as a corrected T0 sensitivity analysis; (3) P4, as a sealed appendix. Codex over-ranked P2 (Codex #2, my #6).
P5 is worth one paragraph inside P0.

---

## 5. What Codex missed (anchored)

1. **The P1 screen's own bound is below P1's target** (row 15). At the thesis operating point, B = 30, proportional
   allocation is null (+6/−1).
2. **The screen is an upper bound because of fail-fast witnesses** (§2 item 2). Codex flagged cascades and
   normalisation, but not this. Normalisation turns out to be immaterial (30 → 30, 89 → 88).
3. **The blockers are long-trip riders** (634 s vs 424 s). P1 is effectively "give long trips a bigger B". The
   matching rider-side guardrail is per-trip-length lateness, not a common-rider average.
4. **Per-request policy IDs already exist** (row 16). P1 needs no Domain/Application change.
5. **P1 novelty collisions:** Molenbruch's explicit argument in the owner's own PDF, Mt-KaRRi, Lyft US12182741B2 and
   Elmi (§1f). Under the strict boundary the "candidate extension" is rule C with a known parametrisation.
6. **P2:** two prior optimisation passes and an existing harness (row 24), and the thesis-corpus work counts (row 23).
   This could have been checked at T0 before ranking P2 second.
7. **P3's closest prior is already in the owner's repository:** Hosseini, Rostami & Araghi (arXiv 2508.01032).
   Window bounds are quantiles set by penalty ratios, and the owner listed it as "Trục B … chưa từng thử"
   (`E:/Code/RideBound/docs/research/wp15-…-2026-08-28.md:57-114,219`). A real operator also sells pooled arrival
   windows (MOIA Express, `CL/R13-SURVEY-CLAUDE.md:271-273`).
8. **O2's strongest operator answer is absent:** at equal service, the deadline rule M⁺-30 is forced in 41.3% of
   decisions and breaks 14.5% of riders' promises, while C breaks none (`HO:166,172-174`). Also absent is the joint
   metric "served and on time per request", where C-30 beats U with and without forecast (`CL/cap-vs-pad…:4,12,25,33`).
9. **The weakest-point paragraph omits three things:**
   - the preregistered **H6 negative result**: −7.13 pp, 1,735 → 1,581 of 2,160
     (`E:/Code/RideBound/docs/19-requirement-traceability.md:697,712`; `D03E:238-239`, which also says T38 shows no
     advantage on the common E2 metric);
   - the forecast gain is **not specific to C**: Mplus and V also reach 0.17% (`FR:65`; `HO:281`);
   - occupancy is **0.54 riders per vehicle vs about 1.33** in the FleetPy paper (`HO:206`).
10. **O5:** NYC FHV November 2018 records exist with `SR_Flag` for shared trips, in the same month as the FleetPy
    traffic days. The real HVFHV shared share in Nov 2018 was 23.2% (`CL/R13-ML-DATA-CLAUDE.md:138,159`), a useful
    external check of the simulation's low pooling.
11. **New idea, one line:** price C in fleet units. Ask how many extra vehicles let C-30 serve as many riders as U.
    It is T1 by my reading (fleet size is an input to fixture generation; the normalizer caps it at 32 vehicles,
    `CL/RUNTIME-ESTIMATE-2026-10-07.md:39-40`; I did not check the fixture builder). It
    answers O2 in operator currency, and Schulz/Pfeiffer use the same framing ("decide on the required number of
    vehicles to reach this service level", `CW/r13-paper-text/s00291-026-00847-0.txt:34-35`). It needs new runs, so it
    must be sealed first.

---

## 6. Overclaims and errors to remove before showing the owner

1. **P1's "≥1 pp more of all requests served" as the aim.** Restate it against the screen's first-order upper bound:
   0.52 pp (mean 60), 0.82 pp (mean 120), ≈ 0.14 pp (mean 30).
2. **P1's "new versus closest prior" wording.** Say instead: a parametrisation study of rule C. Proportional per-rider
   limits are prior (Molenbruch 2015, Mt-KaRRi 2026, Lyft US12182741B2, Elmi 2026 in `D03E:211-213`).
3. **P1 "rider gets an explicit relative burden limit".** Riders never see the budget; this rider value is asserted,
   not measured.
4. **P1 "need a real per-rider-budget contract" and the 24–40 h T2 estimate.** The contract exists (row 16). The work
   is Benchmarking-level plus fixtures and tests.
5. **P2 "lower decision CPU/latency or more candidates within a compute budget".** Unsupported in the thesis corpus:
   0 omitted candidates and ≤80 generation units per decision (row 23). Also replace "need a profiler" with "an
   existing harness" (row 24).
6. **P3 using Alonso-González as rider evidence for windows** (row 36).
7. **P5's ≥25% exposure reduction presented as a prediction.** It is already implied by existing data (row 42). With a
   real-world 10-minute threshold, exposure in C arms is zero.
8. **Minor anchors:** `InsertionCandidateGenerator.cs:709` → `:770`; `FR:68` → `:70`; `FR:37` → `:40-42`. Grubhub's
   remedy is a "GHG Perk", not credit.
9. **Note: nothing to fix.** Codex unpacked the pypdfium2/Pillow wheels into `codex-work`
   (`CW/R13-pdf-render-dependencies.json`), not into any shared environment. No breach of the round's write rules.

---

## 7. Are Codex's O2/O3 answers and "weakest point" accurate and complete?

**Accurate.** Every number I checked matches its source (rows 25–28, 30–31), including the cost of C (−96 riders,
2.61 pp), the lateness ladder, and the caveats that the forecast changes the display, not the vehicles (consistent
with `CL/cap_vs_pad_frontier.py:9`), that snow is weak, and that rider-side value of S is unproven.

Codex's point that Σ|c| also charges *earlier* changes is correct and matches `D03E:237`. Its framing ("kiểm soát và
kiểm toán chất lượng dịch vụ; chưa phải bằng chứng tăng doanh thu") respects `D03E:236-246`.

**Incomplete.**
- O2 omits the deadline comparison and the joint on-time-served-per-request metric (§5 item 8).
- O3 states the rider-facing outcomes correctly but gives no quantitative rider valuation of lateness against the shown
  time.
- The weakest-point paragraph omits H6, the fact that the forecast gain is not specific to C, and the low occupancy
  (§5 item 9).

None of these is a factual error; all are omissions a committee could exploit.
