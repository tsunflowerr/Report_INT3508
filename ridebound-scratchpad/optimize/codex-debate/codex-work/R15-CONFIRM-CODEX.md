# Round 15 — Codex confirmation of the final verdict

2026-10-10. **Verdict: ACCEPT WITH CORRECTIONS.** Keep A1 as the single next step: consolidate the existing service/reliability/quote results, with M⁺ as a central comparator. Keep A2 as at most one optional, time-boxed selection-objective experiment after A1 is drafted and the deadline is confirmed. The corrections below change the evidence and wording, not that ordering. A3 remains conditional on a separate owner request; A4 is the fallback; A5 remains future work.

The most consequential corrections are: include the 30-second padded-U comparison; distinguish recorded cumulative-only witnesses from counterfactual effects; remove causal and unconditional-guarantee language; stop treating candidate screens as trajectory-wide upper bounds; and correct the interpretation of deterministic solver time. These are necessary before section C reaches the owner.

## Scope and anchors

I opened all 75 numbered confirmation rows' relevant anchors and all five earlier-claim corrections. AGREE means the observed fact is supported, subject to the stated scope; it does not validate an associated business interpretation. WRONG identifies a contradicted number or unsupported interpretation. CANNOT CHECK preserves a genuinely untested claim. Future thresholds and effort estimates are plans, not results.

I wrote an independent reader, R15-audit-v2.py, and ran it on **227 existing transcripts**: the final judge's 159 C-run files, plus 34 T3.8 U and 34 M⁺-30 files. It checks decoded frame lengths and SHA-256 hashes, classifies acknowledged budget-prune witnesses, reconstructs final ledger usage and served-set overlap, reads selection bounds/retention diagnostics, and independently integrates the chronological forecast for first quotes and counts arrivals. It imports no Claude analysis code. The factor source and rule match display_layer.py:36-72 and promise_stretch.py:29-68, but the integration/counting is my own implementation. It uses the successful U/C paths indexed in my R13 audit; M⁺ uses the owner's documented successful-rerun convention (tang3/t38/t38_calibrate.py:43-48).

The successful audit validated **458,477 decoded frames**. It independently reproduces 98 measured C runs / 64,371 acknowledged decisions / 1,256 step-failing drop-budget records, zero cumulative-only measured-C records, the fixed-traffic 6 records in 4 decisions, the deduplicated synthetic 4 records in 3 decisions, and all three arms' required forecast/padding counts. The synthetic w08 rerun duplicates the completed rider IDs, action fingerprint, ledger statistics and witness classification; it is retained for reproducibility but not counted as an independent case.

No simulation, build, solution test, shared installation or existing-file modification occurred. R15-audit.py was an initial attempt, stopped before producing outputs because its first-quote timestamp lookup used the wrong nesting; it is preserved. The successful v2 reads publishedPromise.publishedAtMs. All output creation uses mode x inside codex-work.

Short keys below expand to these files. Paths are relative to E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate unless absolute.

| Key | File |
|---|---|
| V | claude-work/R13-FINAL-VERDICT.md |
| A | codex-work/R15-audit-summary.txt |
| AJ | codex-work/R15-audit.json |
| FJ | claude-work/r13-final-judge/ (the filename follows this prefix) |
| T38 | E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md |
| W07X | E:/Code/Report_INT3508/ridebound-scratchpad/tang3/w07x/W07X-REPORT.md |
| FR | E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md |
| PAD | claude-work/cap-vs-pad-frontier-2026-10-07.txt |
| LATE | E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/lateness-distribution-2026-10-06.txt |
| BUC / WBU | claude-work/budget-use-check-2026-10-09.txt / claude-work/wp14r-budget-use-2026-10-10.txt |
| CVP | claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt |
| LAD / BUD | claude-work/wp14r-ladder-reanalysis-2026-10-08.txt / claude-work/budget-block-diagnosis-2026-10-07.txt |
| SHARE / EXP | pooling-share-2026-10-06.txt / exposure-check-2026-10-06.txt |
| CON / EXAMPLE | E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/constraints-and-pooling-2026-10-06.txt / example-rider-2026-10-06.txt in that same folder |
| RUNTIME | claude-work/RUNTIME-ESTIMATE-2026-10-07.md |
| RAW / WIT | codex-work/R13-raw-verification.txt / codex-work/R13-cumulative-witnesses.json |
| MLD / SAMPLES | claude-work/R13-ML-DATA-CLAUDE.md / claude-work/r13-ml-data-samples/ |
| SCREEN / SCREEN30 | claude-work/r13-judge-claude/screen-audit-2026-10-10.txt / screen-audit-b30-2026-10-10.txt in the same folder |
| PROP / TIER | claude-work/proportional-budget-screen-2026-10-07.txt / claude-work/r13-proposer/tier-budget-screen-2026-10-10.txt |
| W14 | C:/Code/RideBound-noworse/docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md |
| SRC | C:/Code/RideBound-noworse/src/ |
| CONFIG | E:/Code/Report_INT3508/ridebound-scratchpad/tang3/configs/ |
| D03 | E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md |
| WP15 | E:/Code/RideBound/docs/research/wp15-commitment-design-new-paper-evidence-2026-08-28.md |
| PT | codex-work/r13-paper-text/ |
| HZW / FLEET | claude-work/pdf/hoerl-zwick-2022.txt / claude-work/pdf/fleetpy-etrr-2026.txt |
| FP / OWN | ROUND13-FACT-PACK.md / codex-work/R13-PROPOSALS-CODEX.md |

## 1. Confirmation table audit

Each numbered row below corresponds to section B of V, preserving its original number.

### B1 — Results and counts

| Row | Status | Opened evidence and finding |
|---|---|---|
| 1 | AGREE | T38:46 gives U/C30/M⁺30/V30/M⁺60 = 2434/2338/2338/2336/2347. A:7-9 independently reconstructs the first three. |
| 2 | AGREE, scoped | T38:58-59 gives forced 0/41.3/22.5/53.8% and self-broken 0/14.5/4.2/21.6%. These are cell means and different rules' own obligations, not a common arrival SLA. |
| 3 | AGREE | T38:111 explicitly gives pooled M⁺30/M⁺60 self-broken shares 12.4/3.4%, versus cell means 14.5/4.2%. |
| 4 | AGREE | T38:64 reports 30/34 identical C30/M⁺30 fleet-action sequences; it does not say all 34 are identical. |
| 5 | AGREE | FJ/served-overlap-check-2026-10-10.txt:2-4; independently A:18-19: U/C common 2207, only 227/131; C/M⁺ common 2332, only 6/6. Same number served is not the same served set. |
| 6 | AGREE | LATE:4-5,11-12,25-26 verifies the percentages/maxima. A:7,9 independently reproduces integer late counts U 203/102/18/2 and C 76/11/0/0; forecast C 10/0/0/0. |
| 7 | AGREE | PAD:4,12,15 verifies all stated U and +60-pad figures. A:9 reconstructs timely 2231/2297/2347, forecast late60/120=137/87, +60=87/48. The missing +30 comparator is addressed below. |
| 8 | AGREE | PAD:25,33; A:7: C naive 2262 timely, forecast 2328, forecast late60/120=10/0, four early>60. Quoted percentages/extensions round consistently. |
| 9 | AGREE | PAD:46,54; A:8: M⁺ naive2264 timely, forecast2328, extension about 7.3s. This is display replay, not rerun forecast-aware dispatch. |
| 10 | AGREE | PAD:4,12,25,33; A:7,9: timely120 U 2332, C 2327, U+forecast 2347, C+forecast 2338. Thus C is -5 without forecast and -9 with forecast at this threshold. |
| 11 | AGREE | SHARE:2-4 gives shared 22.8/13.4/13.1%. Shared fractions need absolute shared completions and service counts alongside them. |
| 12 | AGREE as an intersection | EXP:2-3 gives 134/203 and 4/76; A:7,9 independently reproduces both. These are late-and-dispatch-exposed counts, not counts causally made late by pooling. |
| 13 | AGREE | CON:6 gives187 nonzero revisions and conventional per-revision median108.6s. This is a different population/statistic from BUC's rider-level nearest-rank p50. |
| 14 | AGREE | LAD:2-6 verifies all five served/shared/exposed/late60 rows. A:3-5 independently checks the three enforced-C served totals. |
| 15 | AGREE, corpus-specific | W14:82-86 reports identical six arms and the three inert ablations; :103-111 reports683 later, zero earlier decision-induced changes across160 bundles. Not a general property of all RideBound updates. |
| 16 | AGREE | W07X:22-29 and RAW:6-21 give the stated C service ladder and M⁺ forced cell means. A:10-17 independently reconstructs all eight C totals. |
| 17 | AGREE, local model example | W07X:54-62 gives79.0+68.3≈147.3s, exceeding90 and120; each named divergence admits one extra request under C. Projection attribution is not complete real-world causal identification (D03:222-224). |
| 18 | AGREE | T38:49-52 gives service gaps39/52/5 in w08/w17/w07. |
| 19 | AGREE | claude-work/load-and-occupancy-2026-10-07.txt:2 gives U mean occupancy .535, load .814. It includes idle time in the two-hour window. |
| 20 | AGREE, now checked at primary level | FLEET:421-449,472-478 and the primary fleetpy-etrr-2026.pdf, PDFp11, give approximately 1.33 occupants for AM,180 vehicles,21400 sampled requests on12 Nov, full-day simulation and30s boarding/alighting. This supports a descriptive load limitation, not a matched benchmark or a causal explanation of the difference. |

### B2 — Budget use and accumulation

| Row | Status | Opened evidence and finding |
|---|---|---|
| 21 | AGREE | BUC:17,20,23; RAW:6-8,22-23; A:10-12: C120/150/180 each 666 served, 9 exposed, mean56.180s, max96.738s, zero repeated/near90%-of-cap riders. RAW's vector identity concerns served IDs and budget vectors; do not infer every protocol frame is identical. |
| 22 | AGREE | BUC:34,37; A:7,9: C30 has33 exposed, zero repeated, max29.2s and four near90%; U 174 exposed/12 repeated. The column labeled median in BUC remains nearest-rank p50. |
| 23 | AGREE | WBU:10; A:3: WP14r C120 1563 served, 41 exposed, mean62.3s, max119.6s, three near90%, one repeated. |
| 24 | AGREE as observed-path screens | CVP:5-8,17,31 verifies2/0/13/6 FREE riders and U4 at120, WP9 A 1 at60. These screens neither predict accepted C trajectories nor bound the effect of a new policy. |
| 25 | AGREE | WIT:8-39 gives91.010+117.780=208.790;25.661+5.924=31.585;81.952+10.017=91.969s. These are accepted histories, distinct from rejected-candidate witnesses. |
| 26 | AGREE, independently reproduced | FJ/cumulative-decisive-check-2026-10-10.txt:4-30; A:7,10-17:98 measured C files, 64371 acknowledged decisions,1256 drop-budget prune records=845+411. Every recorded drop-budget prune reports delta>B; zero cumulative-only, missing-witness, other-budget or unclassified records in this sample. |
| 27 | AGREE, witness counts only | FJ/cumulative-decisive-check-2026-10-10.txt:31-45; A:3-5: fixed C30 has848 step-failing records; C60 two cumulative-reported records in one decision; C120 four in three. None of their associated new requests finally ends rejected. 51.755+80.304=132.059>120 is correct. |
| 28 | AGREE, with deduplication and causal limit | FJ/per-run-cumulative-only-b-2026-10-10.txt:5-7; AJ's synthetic runs reproduce 6 records/5 decisions/two associated rejections before removing the w08 rerun. Distinct cases have 4 records/3 decisions/one associated final rejection. This is not a bound on global counterfactual service loss. |
| 29 | AGREE | SRC/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs:6-12,86-98 defines before/delta/after/limit and emits a budget witness when after>limit; AJ checks before+delta=after. |
| 30 | AGREE for the default evidence profile | SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:222-239 is fail-fast unless full collection is requested. SRC/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:165-174 and CONFIG/wp4-tier3-v2.json:1-25 confirm full collection is not enabled. Possible cumulative-only witnesses are upper bounds on newly feasible recorded candidates, not on eventual policy effects. |
| 31 | AGREE within the recorded assessment pipeline | SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:175-190 records assessed failures; SRC/RideBound.Runner/Protocol/SolverExecutionEvidenceMapper.cs:46-55 exports that prune collection. This is not a claim to enumerate all possible routes or every counterfactual state. |
| 32 | CANNOT CHECK exact counterfactual trajectories | The proposed per-step policy was not run or implemented. Rows26/35 substantiate witness classification and observed objective saturation, not an unconditional trajectory-equivalence claim. Preserve V:427's UNCONFIRMED status everywhere, including the bottom line. |

### B3 — Code/configuration

| Row | Status | Opened evidence and finding |
|---|---|---|
| 33 | AGREE, conditional levels | SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271-303,319-331,365-385,510-522 and SRC/RideBound.Domain/Commitments/CommitmentDimension.cs:19-32 reproduce the hierarchy. Forced/worst-utilization levels appear only when their activation conditions hold. |
| 34 | AGREE | SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:612-626 saturates an applicable zero limit at1e6 when its usage is zero; nonzero usage fails. |
| 35 | AGREE, observed states only | FJ/objective-levels-check-2026-10-10.txt:3,5,7,9; A:7,9 independently gives U 3503/3503 and C 3506/3506 incumbent/best-bound saturation when a new request is considered and this level exists. Cap applications, omitted-by-cap and exhausted work are zero. Each arm nevertheless reports one omitted request. Future cost-first states can have different diagnostics. |
| 36 | AGREE | Parsed CONFIG/U.json and C-30.json recursively: their sole value difference is /policies/0/limits/1/hardLimit absent→30000. C120 sets120000; Mplus30 has no drop hard cap and slack30000 at:98. |
| 37 | AGREE | CONFIG/wp4-tier3-v2.json:3,10-15,23 gives hard-vector, max100 candidates, max2 new requests, seed7 and retention token service-set-stability-portfolio-v1. These bounds restrict the generator even when cap counters stay zero. |
| 38 | AGREE | FJ/probe-t38-C30-2026-10-10.txt:2-4 and independently read raw initializeRun metadata give hard-vector/core1ce15e92…/binarya631038b…. AJ preserves the manifest core/policy. |
| 39 | AGREE | FJ/probe-wp14r-FREE-2026-10-10.txt:2-4; I independently opened a FREE raw initializeRun: rolling-cost/core38d517d8…/binary17a9dfcf…. |
| 40 | AGREE | Read-only git merge-base confirms ancestry; git log 1ce15e9..761915c -- src/ returns only45f8026, ADR-077 default-off forced-vehicle recovery. This does not replace a rebuilt-runner equivalence check. |
| 41 | AGREE | SRC/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:287-321 starts RollingCost; fixed-freeze does not switch to a hard-vector objective. |
| 42 | AGREE | SRC/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:97-108 creates null hard limits/no final-confirmation locks; policy.cs:465-478 selects that provider. |
| 43 | AGREE | HardVectorCandidateAssessor.cs:565-570, SRC/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:433-449, SRC/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs:84-94 verify lookup, one stamped ID, and a nonempty policy list. Mixed-policy fixture/binary behavior remains prospective. |
| 44 | AGREE, all ranking inputs fixed | FleetPyManhattanNormalizer.cs:461-476 includes selection key, artifact SHA, ScenarioId and node. Same ScenarioId alone is insufficient: selected-node set and all other ranking inputs must also stay fixed for nesting. |
| 45 | WRONG as a runtime/hotspot statement | Evidence-keys outputs:9 record consumedDeterministicTimeMicros maxima66/68, not elapsed µs. SRC/RideBound.Solvers.OrTools/OrToolsCandidateSelectionSolver.cs:149-154,462-473 converts response.DeterministicTime. WallTimeMilliseconds is a separate property (SRC/RideBound.Application/Optimization/CandidateSelectionSolver.cs:178-183), omitted by the transcript mapper:572-583. RUNTIME:15, not:14, gives 918/692≈1.33s of whole-job wall per decision, not a median measured decision latency. |
| 46 | AGREE as historical runtime basis | RUNTIME:24-25 reports six parallel jobs,170 jobs/about7h, about15min/job. It does not verify cost-first runtime. |
| 47 | AGREE, now directly checked | FleetPyManhattanNormalizer.cs:322-328 rejects requestTarget>128, vehicles>32, nodes>96. |
| 48 | AGREE | codex-work/STRONG-BASELINE-CODEX.md:54 and the absolute budget rule: C0 forbids improvements as well as delays; it is not a reproduction of Uber's undisclosed optimizer. |

### B4 — Forecast/data/screens

| Row | Status | Opened evidence and finding |
|---|---|---|
| 49 | AGREE with denominators | FR:42,67-70,83-84 verifies6.01→.17%, U9.72→3.90%,13.7s quote extension as cell means, and34/1471 displayed pickup-window conflicts. These differ from all34 rider-pooled values. |
| 50 | AGREE | FR:65 gives M⁺/V .17% on the21 active cells too; forecast gain is not specific to C. |
| 51 | AGREE, one incident | FR:103-104 and optimize/test-snow-2026-10-06-report.txt:10 give7.19→5.94% cell means and92.5% model-attributed unanticipated late seconds. Not a universal failure rate. |
| 52 | AGREE | D03:267-269 distinguishes active-cell mean.17%, all34 mean.51%, and the no-population-guarantee boundary; LATE:26 gives rider-pooled.43%. |
| 53 | AGREE, fixed sample | MLD:284-298; independently summed the existing weekday TSV:21 cells,1471 riders,2 forecast-late versus68 naive. Saved snow rows imply34/601 versus41. Two is headroom for this fixed-sample late60 count, not for all prediction metrics or future days. |
| 54 | AGREE as saved station/sample evidence | SAMPLES/noaa-event-days-2026-10-09.txt:1-3 gives one Mon–Fri >=1-inch-snow day in Sep–Dec2018,15 Nov; also nine rain>=20mm days without that snow threshold. This is not absence of other traffic shocks. |
| 55 | AGREE, schema scope | MLD:136-139,259-262 and SAMPLES/parquet-footer-probe-2026-10-09.txt:1 verify yellow8155449 rows, FHV SR_Flag and HVFHV Feb2019 start. The negative ETA statement is restricted to the inspected schemas. SR_Flag can include unmatched shared requests. No millions of trip rows were decoded here. |
| 56 | AGREE | EXAMPLE:2-3,60 verifies the rounded clock times and exact190.5s/17.6s deviations. Subtracting displayed whole-second labels alone would give rounded results. |
| 57 | AGREE on arithmetic; no policy bound | PROP:2-5, SCREEN:17,21, SCREEN30:17,19 give11→30,59→89, and+5/+6 screened request identities. 19/3672=.5174pp,30/3672=.8170pp. These are differences between partial screens on C30 paths, not upper bounds on recovered completions. |
| 58 | AGREE as a screen | TIER:4 gives 114/148, 85 also served by U. Independently reproduced in Round14 with R14-verify.py:39-42. Not114 actual extra completions. |
| 59 | AGREE with category wording | BUD:2-10 gives 148 requests with recorded budget blocks,116 U-served, median smallest overshoot109.6s, two with prior use. “Only by budget” describes observed pruning attribution; changing trajectories could change structural/search limitations too. |
| 60 | AGREE | CVP:19,24,29,34 gives matched20-cell4-vehicle 966/860 and 8-vehicle 1735/1581; fleet-size-wp9-check:4-5 corroborates the4-vehicle pair. Its8-vehicle rows:2-3 use different25/30-cell cohorts and must not be substituted. |
| 61 | AGREE | D03:238 records H6 -7.13pp and explicitly withholds general superiority. |

### B5 — Literature/products/boundary

| Row | Status | Opened evidence and finding |
|---|---|---|
| 62 | AGREE | PT/Unreliability_in_ridesharing_systems_Measuring_cha.txt:994-1018,1077-1078; Table5 mapping was directly checked on the primary PDFp17 in Round14: base34.5%, full45.6%. Section6 already controls unreliability; the open question is not evidence that control itself is new. |
| 63 | AGREE, reference-projection scope | HZW:529-543 updates the assigned route's expected drop time for on-board riders otherwise violating bounds, then penalizes excess. “Absolute minimum” is the paper's phrase; it does not prove global optimal arrival or a traffic-proof guarantee. |
| 64 | AGREE | PT/1-s2.0-S0965856426000662-main.txt:637-640 gives MeanLate-Distn2.53 (15 observations,2 studies), MeanLate-X/Y3.12 (66,27). Different mean-lateness constructs, not this ledger's WTP. |
| 65 | AGREE, different construct | PT/Value_of_time_and_reliability_for_urban_pooled_on-.txt:30-35 gives N1006/RR≈.5; :899-903 says no desired arrival/lateness situation was presented. It is not direct counterevidence about the utility of one minute late against a promise. |
| 66 | AGREE, ride-time prior | PT/OperationalEffectsofServiceLevelVariations-publication151005.txt:154-164 uses fractional excess of direct ride time. It does not implement a cumulative dispatch-revision allowance. |
| 67 | AGREE on what the thesis reports | PT/21020283-3476 (1).txt:159-162,1846,1913-1915 verifies figures,200 requests/21 taxis and the stated25% prediction setup. One example thesis does not certify this thesis's adequacy or establish a university-wide standard. |
| 68 | AGREE, product statement only | [UberX Share](https://www.uber.com/us/en/ride/uberx-share/): “we cannot guarantee arrival times”; page also gives8-minute average added travel and the additional-pickup ETA design goal. No underlying optimizer or C ledger is verified. |
| 69 | AGREE | [MOIA Express](https://ride.moia.io/en/express): “shorter arrival window”; optional upgrade and up to six offers. No compensated SLA or WTP for a30s budget follows. |
| 70 | AGREE, qualified pickup policy | [Lyft help](https://help.lyft.com/hc/en-us/all/articles/115013078668): “Get $15 Lyft Credits”; driver10min late/$50 unmatched and qualified airport-bound scheduled rides, airport-origin exclusions. This is pickup, not drop-off, and future-use credit, not cash profit evidence. |
| 71 | AGREE, description not legal analysis | [US12182741B2](https://patents.google.com/patent/US12182741B2/en): “total ETA minutes initially quoted”; illustrative5min detour/7min pickup/.25 ETA ratio and individualized constraints. The ratio is anchored to the original quote, not necessarily a per-increment limit. |
| 72 | AGREE, now direct primary check | [Mt-KaRRi full paper](https://arxiv.org/pdf/2605.11798), PDFp5: “trip time they originally accepted”; constraint alpha*T_accepted+beta. It is not a reset allowance for each new revision. |
| 73 | AGREE, now opened successfully | [Yu/Zhang/Zhou publisher abstract](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4448): “magnitude effect” is offset by the “update-frequency effect” for one-minute WTI changes. N1425745, pre-match virtual waiting; this is not drop-C or proof that sub-minute promise changes never matter. |
| 74 | AGREE | D03:54-56,211-225,236-245,267-269 governs every interpretation: no broad novelty, satisfaction/revenue/labor, complete traffic causality or population SLA. |
| 75 | AGREE as a specification distinction; correct the prior's label | WP15:168-171 distinguishes the cumulative whole-chain ledger. Its “budget each time” description must not be taken as an incremental cap: the primary Mt-KaRRi rule retains the original accepted-time anchor. No empirical advantage of accumulation is established here. |

### B6 — Earlier-claim corrections

| Row | Status | Confirmation/correction |
|---|---|---|
| W1 | AGREE | CVP:5,17,31 and row26 support the final judge's correction: rare uncapped path-screen differences coexist with zero recorded cumulative-only measured-C prunes. |
| W2 | WRONG for distinct synthetic cases; WP14r agrees | WBU:10 verifies one repeated WP14r C120 rider. The13-file synthetic tally counts the successful w08 run and its rerun twice; after case deduplication there is one repeated rider, not two independent riders/cases. This also narrows my R13/R14 synthetic wording. AJ's per-run ledgers and duplicate checks supply the correction. |
| W3 | WRONG if µs means elapsed solver time | Same correction as row45:66/68 are recorded deterministic-work micro-units. They do not measure elapsed CPU or end-to-end evaluation time. |
| W4 | WRONG as a global impossibility correction | The19/30 first-order screen differences do not prove a >=1pp policy target unreachable. With different allowance assignments, schedules and later candidate sets change. The target was ambitious and unsubstantiated; withdraw it as a justified expectation, without claiming a proven ceiling. SCREEN:13-22; OWN:81-85 explicitly requires a trajectory comparison and labels its margins as design choices. |
| W5 | AGREE | FP:31-36 yields A-F0=sum(c)+(sum(x)-a0) with terminal closure; C bounds sum|c|, not forecast/execution residual. D03:222-225 applies. |

## 2. Required extra check: the missing 30-second padded-U row

**AGREE on all requested values; correct the line anchor.** U + forecast + 30 s padding is PAD:14, not :15; :15 is the 60 s pad. C and M⁺ are PAD:33 and :54. My independent integration and arrival counts are A:7-9 and R15-audit-v2.py:14-27,112-118.

| Arm, same 3672 requested trips | Served | Late >60 s | Timely ≤60 s / requests | Y60 among served | Mean quote extension | Early >60 s | Timely ≤120 s |
|---|---:|---:|---:|---:|---:|---:|---:|
| U + forecast + 30 s pad | 2434 | 106 | 2328 / 3672 = 63.40% | 4.35% | 37.2 s | 44 / 2434 = 1.81% | 2366 |
| C-30 + forecast | 2338 | 10 | 2328 / 3672 = 63.40% | 0.43% | 7.4 s | 4 / 2338 = 0.17% | 2338 |
| M⁺-30 + forecast | 2338 | 10 | 2328 / 3672 = 63.40% | 0.43% | 7.3 s | 4 / 2338 = 0.17% | 2338 |

Timely means completed with arrival no more than the stated threshold after the first displayed drop quote; rejected requests are not timely completions. Y60 and early60 use served-rider denominators. The forecast/pad changes the first displayed quote on existing trajectories, not vehicle speed or the dispatch acceptance set.

**The final verdict does not present this trade-off fully enough.** Its A1 table (V:88-101) and Vietnamese O3 (V:587-590) show only the 60 s pad, with 42.44% early arrivals and a 67.2 s extension. Those figures are correct, but omit the closer counterexample: a 30 s pad already ties C/M⁺ on timely60 per requested trip with just 1.81% early60. Calling padding generally inaccurate from the 60 s example alone is unbalanced. Include both pad rows.

The corrected comparison is: C + forecast uses a quote about 29.8 s shorter and has 40 fewer early60 completions than U + forecast + 30 s padding, while serving 96 fewer riders and producing the same 2328 timely60 completions. At 120 s, padded U produces 2366 timely completions, 28 more than C/M⁺. Thus C has a sharper displayed quote and lower served-rider lateness; it does not dominate service or every timely-completion threshold. The differing served sets prevent interpreting the 96 as identified rescued riders. C and M⁺ tie these arrival counts while enforcing different obligations.

Suggested Vietnamese replacement for V:587-594:

> Không trần + dự báo + đệm 30 giây cũng đạt 2.328 lượt hoàn thành không trễ quá một phút, trên cùng 3.672 yêu cầu. Cách này chở 2.434 khách thay vì 2.338, nhưng lời hứa dài thêm 37,2 giây thay vì 7,4 giây; tỷ lệ tới sớm quá một phút là 1,81% thay vì 0,17%. Nếu cho phép trễ hai phút, cách đệm đạt 2.366 lượt hoàn thành đúng ngưỡng, còn C và luật hạn chót đều đạt 2.338. Luật C có lời hứa sát hơn và ít khách được chở bị trễ hơn; nó không hơn ở mọi chỉ tiêu. Luật hạn chót + dự báo đạt cùng kết quả đến nơi với C, nhưng nghĩa vụ được kiểm tra của hai luật khác nhau.

The sentence about the 60 s pad can remain after this comparison, with its scope explicit.

## 3. Overclaim corrections required before giving section C to the owner

These are eight groups of necessary edits, not eight additional projects. Much of V's section D is already appropriately cautious, but its corrections must also govern A and C.

### Correction 1 — Narrow the cumulative finding to recorded evidence

**Affected:** V:51-61,79-80,126-132,166,195-198,319,332,561-568,613,662-663; D1:685 and D21:705; E:719-724.

Replace “never decided anything”, “admitted exactly the same candidates”, “decided at most 7 decisions / changed at most 1 final rejection”, and “the working ingredient is …” as settled causal findings with:

> Across 98 enforced-C runs with measured traffic factors, all 1256 recorded drop-budget pruning records report a single dispatch increment exceeding B. None requires prior spending to explain the reported failure. This is consistent with a per-step explanation of these observed budget failures. A cumulative-versus-per-step counterfactual trajectory comparison has not been implemented or run. Across fixed traffic, six possible cumulative-only pruning records occur in four decisions; in the deduplicated synthetic cases, four occur in three decisions. All associated new requests in the fixed cases are eventually served; one in the synthetic cases is eventually rejected. These are recorded witnesses and lifecycle associations, not measured global policy effects.

A:3-7,10-17 reproduces the counts. A:20 and AJ's per-run fields confirm the synthetic duplicate. The evidence is fail-fast (row30), so a positive witness can conceal another blocker. Conversely, changing a gate can change later schedules and candidate populations. Seven recorded decisions is not an upper bound on eventual counterfactual decision changes; one associated final rejection is not an upper bound on counterfactual service change.

The new saturation check also agrees on all eight measured w07 C levels (A:10-17), strengthening the same-state inference. It does not implement and independently compare every assessment/objective field of a proposed per-step policy, so row32 remains CANNOT CHECK. D21 should say “no observed cumulative-only measured-C pruning record”, rather than “not on measured traffic” without qualification. In A3:319, name WP14r's four as pruning records in three decisions, not four rejected requests.

Correct Vietnamese text for O2/O6:

> Trong 98 lần chạy mô phỏng với hệ số giao thông lấy từ dữ liệu đo, cả 1.256 bản ghi chặn do ngân sách đều có một lần thay đổi vượt B. Không bản ghi nào cần phần đã dùng trước đó để giải thích việc bị chặn. Đây là kết quả về các phương án đã được xét; chưa chạy đối chứng bỏ phần cộng dồn, nên chưa kết luận toàn bộ quỹ đạo sẽ giống nhau. Phần cộng dồn vẫn là một quy tắc được cài đặt và kiểm tra cho cả chuỗi thay đổi, nhưng dữ liệu này chưa chứng minh lợi ích tăng thêm của nó.

The U median 108.6 s (CON:6) is a descriptive observation on another revision population, not by itself the cause of inertness in all C decisions.

### Correction 2 — Separate model attribution, obligation compliance and arrivals

**Affected:** V:44-48,107-110,160-179,212-215,241-254,279-284; C:507,522-537,542-544,594,610-613,675-676.

“Serves the same riders” is WRONG: it serves the same number, with 2332 common and six unique to each arm (A:19). “Fewer pooling-caused late riders” is stronger than the measured intersection. “72 purely traffic-late riders” and “knows who caused delay” overstate the v/e/p model projection. C also charges absolute dispatch changes, including some ETA restorations (D03:236-239); it is not exclusively a charge for adding a pooled rider.

Use:

> On the 34 tested T3.8 cells, C-30 and M⁺-30 each serve 2338 riders, 2332 in common. C has zero recorded forced decisions and zero breaches of its own dispatch-budget obligation; M⁺ has 41.3% forced decisions as a cell mean under its different deadline obligation. This is not a common arrival-SLA comparison. Under U, 134 of 203 late60 riders were also dispatch-exposed; under C, four of 76 were. The other 72 had no recorded nonzero drop-ETA dispatch change in the model ledger. These associations do not identify whether pooling caused each rider to be late.

D03:222-225 explicitly limits the projection's causal meaning; :236-245 says C can be zero while a rider is late and withholds business/arrival superiority. “Always kept” or “never forced” must be qualified by the tested cells and the contract assumptions. The guarantee is a bound on the counted dispatch movement under the contract, not an unconditional physical arrival guarantee.

Use in Vietnamese:

> Luật C cho một giới hạn kiểm tra được đối với phần thay đổi lời hứa do quyết định điều phối trong mô hình. Trên 34 ô đã kiểm tra, không có quyết định bị ép hay vi phạm nghĩa vụ C được ghi nhận. Sổ tách các thành phần theo phép chiếu mô hình; nó không xác định đầy đủ trách nhiệm nhân quả ngoài đời. Trong 76 khách trễ của C-30, 72 người không có thay đổi giờ trả do điều phối được ghi nhận, chứ chưa chứng minh tất cả đều trễ thuần vì kẹt xe.

Apply D4's own correction (V:688) to O2:542-544: there are 96 fewer served and 127 fewer late60 completions across different cohorts, ratio .756; no identified one-for-one conversion from late riders to up-front rejects. Also use common ≤threshold arrival outcomes alongside each rule's own compliance measure.

For A2, replace “cap alone suffices” with “the modified selection policy preserves the stated aggregate outcome thresholds under the same gates”. A failed aggregate lateness threshold would show a changed-policy outcome, not isolate an individual-rider causal effect of the ordered objective. Gates, locks, recovery, traffic and service selection still matter.

### Correction 3 — Keep business value symbolic, not a necessary profitability rule

**Affected:** V:124-125,173-188,250-254; C:546-557.

The final verdict correctly says profit is unconfirmed, but “only profitable when a broken promise costs more than a lost trip” does not follow. A symbolic comparison is:

> Delta profit = m × Delta served − q × Delta qualifying late completions − Delta operating cost + Delta retention value.

Here m and q, the causal response and all additional terms are unknown. Even the simplified cohort-count illustration U versus C has Delta served = −96 and Delta late60 = −127, giving q/m > 96/127 ≈ .756 if every other term is fixed at zero, not a necessary q/m > 1. This is sensitivity arithmetic, not estimated ROI, a real compensation contract, or identified rider effects.

Use:

> The measured trade-off can parameterize a hypothetical liability calculation. It does not establish profitability or willingness to buy C. In these cells, the count differences are larger at one-to-two-minute thresholds and small at five-to-ten-minute thresholds. Other audit, contractual, customer or operational benefits have not been measured.

Lyft's checked policy is qualified airport-bound scheduled pickup credit, not an industry-wide drop-off threshold ([Lyft policy](https://help.lyft.com/hc/en-us/all/articles/115013078668): “Get $15 Lyft Credits”). D03:241-245,260-265 forbids inferring ROI or retention.

Use in Vietnamese:

> Chưa đo được lợi ích về tiền. Trong các ô đã đọc, chênh lệch số lượt trễ lớn hơn ở ngưỡng một đến hai phút và rất nhỏ ở ngưỡng năm đến mười phút. Có thể tính một bảng chi phí giả định, nhưng còn thiếu biên lợi nhuận mỗi chuyến, chi phí vận hành, bồi thường và phản ứng của khách. Ví dụ Lyft là tín dụng cho một số chuyến đón đặt trước đi ra sân bay, không phải chuẩn bồi thường giờ trả cho mọi dịch vụ.

Delete “researchers will not optimize total changed seconds because riders cannot see it” (V:555). Researchers can study enforceability, allocation, auditing and computation even when an internal quantity is not shown. Whether this particular quantity predicts rider utility remains unconfirmed.

### Correction 4 — Remove global ceilings derived from partial candidate screens

**Affected:** V:348-367,494,667-668.

The arithmetic is correct: 19/3672 = .5174 pp and 30/3672 = .8170 pp. Its interpretation as a trajectory-wide bound is not. SCREEN:13-22 and SCREEN30:17-22 examine recorded candidates on selected C30 paths with one reported blocker and hidden co-rider/structural blockers. Proportional versus uniform screen cardinality differences are not a mathematical upper bound on later recovered completions after changing allocations and dispatch decisions.

Use:

> Partial observed-path screens show 19 and 30 more passing request identities under the stated proportional rules than the corresponding uniform screens. They do not predict recovered completions or prove a global sub-one-percentage-point ceiling. The evidence is weak motivation relative to implementation effort, so allocation remains future work.

A5's “kill if fewer than 19, the first-order bound” is a discretionary empirical target, not a theorem; remove the asserted bound. Molenbruch supplies prior fractional direct-ride-time limits (PT/OperationalEffectsofServiceLevelVariations-publication151005.txt:154-164), not this exact cumulative dispatch-change allowance. Per-rider/proportional limits are old; an implementation distinction is not broad novelty.

Use in Vietnamese:

> Các phép sàng lọc trên quỹ đạo đã lưu cho thấy chênh lệch khoảng 0,5–0,8 điểm phần trăm về số yêu cầu có phương án vượt qua phần kiểm tra đó. Đây chưa phải số khách được cứu, cũng không phải trần lợi ích của một chính sách chạy đầy đủ. Ý tưởng phân bổ theo thời gian đi trực tiếp đã có tiền lệ; chưa nên mở nhánh này trước hạn nộp.

I withdraw my OWN:85 ≥1 pp target as an evidence-backed expectation. I do not replace it with an unproved impossibility claim.

### Correction 5 — Correct solver timing and the reason to defer my speed proposal

**Affected:** V:67,371,445,493.

“66–68 µs” is not elapsed solver time. Row45 identifies the source conversion of response.DeterministicTime to consumedDeterministicTimeMicros and the separate wall-time property. The official [OR-Tools response documentation](https://or-tools.github.io/docs/dotnet/classGoogle_1_1OrTools_1_1Sat_1_1CpSolverResponse.html) distinguishes DeterministicTime from WallTime, which it describes as “time counted from the beginning of the Solve() call”.

RUNTIME:15's 918/692≈1.33 s is whole-job wall time divided by decision count; it is not median actual decision latency. Neither measure profiles candidate generation, scheduling or commitment evaluation, the target of my OWN:89-103 proposal. RUNTIME:26-34's earlier generator microbenchmarks demonstrate possible work cost, not a current T3.8 hotspot.

Use:

> The archived solver evidence does not establish an elapsed-time hotspot. The proposed evaluator optimization also lacks a current profile showing material end-to-end benefit. Defer it because its profiling, differential-validation and implementation effort is less directly justified than A1/A2 at this deadline.

Keep the deferral. Do not say no hotspot exists or no pipeline optimization is possible. A2 is the preferred mechanism study here, not the only possible pipeline study.

### Correction 6 — Do not conflate rider-reliability constructs or certify thesis adequacy

**Affected:** V:182-186,598-617,732-735.

The Wardman mean-lateness coefficients 2.53/3.12 and pooled survey reliability ratio ≈.5 are different quantities. The pooled experiment describes variation in travel time without a desired arrival/lateness scenario (PT/Value_of_time_and_reliability_for_urban_pooled_on-.txt:899-903); it is not a direct contradictory estimate of the utility of one minute late against a promised arrival. Present both constructs, without converting the pooled ratio into “late minutes matter half as much”.

Use:

> Prior evidence supports interest in timing reliability, with substantial variation by construct and context. Mean lateness against an arrival target and variability of pooled travel time are not interchangeable. Neither study measures willingness to pay for this 30 s dispatch ledger or satisfaction from its forecast replay.

Yu/Zhang/Zhou can now be marked directly checked at its [publisher abstract](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4448): “magnitude effect” and “update-frequency effect” offset for the one-minute virtual-wait intervention. It concerns pre-match waiting, not a drop guarantee or proof of no sub-minute rider value.

Use in Vietnamese:

> Nghiên cứu trước cho thấy khách có thể coi trọng độ tin cậy, nhưng các số đang trích đo những thứ khác nhau: trễ so với giờ mong muốn và độ biến động của thời gian đi chung. Chúng chưa đo giá trị của ngân sách C 30 giây. Trong mô phỏng này, dự báo làm giờ báo đầu sát thời điểm đến hơn với mức kéo dài nhỏ; chưa chứng minh khách hài lòng, hủy ít hơn hoặc quay lại nhiều hơn.

The example UET thesis supports an example of scope/structure, not “this is enough for a UET undergraduate thesis”. Replace V:615-617 with: “This is a plausible bounded systems-and-evaluation scope, subject to the supervisor's and committee's requirements.” No institutional acceptance has been verified.

### Correction 7 — Restrict the data/ML conclusion to the inspected schemas and fixed sample

**Affected:** V:370,374,637-648,670; D20:704.

“No data can help the thesis” and “no dataset has promised times, so we cannot learn what we need” are too broad. The inspected public schemas lack rider promise labels (MLD:136-139,259-262), but trip-duration/demand models can be trained without such labels. They would not directly learn a promise-error target or this C obligation; transfer to the simulator would require validation.

The 2/1471 weekday forecast-late count (MLD:284-298) bounds improvement only in that particular fixed-cohort, fixed-threshold miss count if all other outcomes stay fixed. It does not bound gains in calibration, quote length, another threshold, future dates, different service selection or incident prediction. SAMPLES/noaa-event-days-2026-10-09.txt:1-3's one weekday with ≥1-inch snow is not evidence that no other incidents exist; the same saved file lists rain events.

Use:

> Available public trip data can support an auxiliary duration benchmark, but the inspected schemas do not supply promise labels or a validated simulator mapping. The current weekday miss count is already small and incident evaluation rests mainly on one snow afternoon. Defer a full ML chapter because of effort, uncertain transfer and the deadline, not because useful learning is impossible.

Use in Vietnamese:

> Có thể học thời gian chuyến đi từ dữ liệu công khai, nhưng các schema đã kiểm tra không có giờ hứa với khách và chưa có phép chuyển đã kiểm chứng sang mô phỏng này. Trên mẫu ngày thường hiện tại chỉ còn hai lượt trễ quá một phút sau dự báo; đó là giới hạn của chỉ tiêu trên mẫu này, không phải giới hạn của mọi mô hình hoặc ngày mới. Chưa nên làm chương học máy trước hạn nộp.

### Correction 8 — Retain only the strict novelty and generality boundary

**Affected:** V:150-171,245-254,341-365,609-617; D1, D14, D19-D21.

Use a contribution statement consistent with D03:54-56,175-181,211-225,236-245:

> This work specifies, implements and audits a per-rider cumulative absolute dispatch-change budget, with a same-state model projection separating it from exogenous ETA movement. It measures the resulting service/quote/compliance trade-offs against different obligation forms on one simulator with measured city-wide traffic factors. Existing work already measures and controls unreliability, protects individual riders, uses deadline and detour limits, penalizes replanning and forecasts quoted times. The additional empirical advantage of accumulation, business value, rider response and population arrival guarantees remain unconfirmed.

Distinguish the Mt-KaRRi primary accepted-trip anchor from a reset per-increment budget (row72/75); do not use an inaccurate prior label to create novelty. Qualify the Hörl/Zwick comparison by its tested on-board violation handling and model route reference, rather than implying no earlier dispatch-only controls. V:166's inertness is the observed witness result, not a general theorem.

Correct D14 (V:698) to one repeated rider in the distinct synthetic cases, plus the identical successful rerun; WP14r still has one. All measured C final ledgers in this audit have zero repeated nonzero drop-dispatch changes. “Measured traffic” means simulated trips using measured city-wide factors, not real executed RideBound rides or independent population samples.

## 4. Decision on the ranked list and optional new selection idea

**ACCEPT WITH CORRECTIONS.** No substitute research branch is necessary.

| Item | Decision |
|---|---|
| A1, T0 consolidation | ACCEPT after the eight wording/evidence corrections above, especially both U-pad rows and common endpoint/served-set reporting. Exactly one recommended next step; zero new simulation runs. |
| A2, selection-objective ablation | ACCEPT as at most one conditional optional extension after A1 is drafted and the deadline is confirmed. Feasible in source, not already implemented or validated. |
| A3, C120/C0 dial | Keep lower ranked and conditional on a separate owner request. It reopens a closed branch; do not execute alongside A2 as another default extension. |
| A4, bounded current thesis | ACCEPT as fallback if consolidation/extension effort cannot fit. Use the corrected contribution wording. |
| A5, allocation | ACCEPT as future work due to weak direct outcome evidence, old proportional-limit concepts and effort; remove the purported global screen ceiling. |

### A2 source feasibility and safeguards

I checked SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:10-16,271-303,319-331,365-385 against its current source. The mechanism exists: the selector conditionally prioritizes forced-reference avoidance, then maximizes accepted requests, then applies utilization/revision levels for HardVector, then operational cost and deterministic tie levels.

**A minimal Algorithms/Runner option is plausible. Merely switching the profile to RollingCost is not sufficient.** Forced-reference treatment at :276-280 is conditional on HardVector or SoftHardHybrid. A naïve profile switch would silently lose that priority. Keep the hard assessor, hard profile and gate/recovery behavior; explicitly skip only the intended soft ranking levels while preserving forced-reference, accepted-request count, cost and deterministic tie handling. Domain/Application changes are not inherently needed, but the final diff and tests would determine that. This is a source feasibility judgment, not completed implementation.

The data needed for service, sharing, first quotes/arrivals, hard-budget witnesses and solver-generation diagnostics exists in the audited transcripts. Realized fleet distance/busy-time extraction remains UNCONFIRMED (V:294-296,725-728). The candidate Schedule.OperationalCost field (:367-368) alone does not establish realized business cost; retain the proposed T0 extraction gate before promising an operator-efficiency result.

No-cap-truncation counters on old states do not guarantee an exhaustive route search or future cost-first candidate set. Max candidates/new requests/search work and retention remain bounded (row37), each T3.8 arm has one omitted request (row35), and a new selection sequence changes future generation states. Retain and report those diagnostics in any future experiment.

The minimum described plan is **74 future jobs**, not a verified execution cost: four OFF-option equivalence jobs, two smoke jobs, 68 main jobs. The cited 170-job runtime is historical; cost-first elapsed time is unknown. HEAD versus archived binary drift is real (row40), so do not reuse archived controls after a failed equivalence gate. These future build/test/worktree/harness steps are not authorized for execution by this read/audit round, and none was performed.

A2 tests the interaction between a selection objective and unchanged hard gates; it cannot establish that C alone controls physical arrival, that the gate alone explains every baseline difference, or that hypothetical increased pooling is profitable. Its success/kill thresholds are previewed-panel design choices, not an unseen holdout preregistration. Keep the one-week time box and drop it if it threatens A1.

### Changes to my own earlier positions

- My R13 P1 allocation proposal drops from the leading extension to future work. Withdraw the ≥1 pp expected benefit; retain the distinction between a partial screen and a full trajectory result.
- My R13 P2 evaluator-speed proposal remains technically possible but deferred. Its explicit profiling gate (OWN:97-101) has not been satisfied; the deterministic-time error does not justify promoting it.
- Keep R13 P0's bounded C + forecast + ledger contribution; A1 is the useful concrete writing/analysis step. No demonstrated cumulative advantage, profit or rider satisfaction.
- Keep R13 P3 arrival windows outside the deadline scope; C controls a component of movement, not guaranteed terminal interval coverage.
- Keep R13 P4 damped forecast and P6 public-data ML as auxiliary/future ideas, without claiming that the current two weekday misses bound every possible timing benefit.
- Merge R13 P5's hypothetical compensation arithmetic into A1; do not present a new compensated product or profit estimate.
- Correct my earlier R13/R14 synthetic accepted-history language: one repeated rider in distinct cases, duplicated by the w08 rerun. The unique cumulative-prune and lifecycle counts are those stated in section 3.

## 5. Files and verification record

All new files are inside the authorized codex-work directory and were exclusive-created. The report does not edit Claude's verdict or any existing source, output, policy or thesis file.

| New file | Purpose |
|---|---|
| R15-CONFIRM-CODEX.md | This confirmation, required extra comparison, corrected owner wording and ranked-list verdict. |
| R15-audit.py | Preserved stopped first reader; wrong timestamp nesting, no audit outputs produced. |
| R15-audit-v2.py | Successful independent existing-transcript audit, using only Python standard-library readers and the existing environment. |
| R15-audit.json | Per-run/group evidence, source transcript paths, hashes of action sequences, witness details and duplicate checks. |
| R15-audit-summary.txt | Compact independently reproduced counts, cited as A:3-20. |

The successful audit exits zero after reading all 227 files. The report's 75 numbered B rows and five W rows cover the confirmation table. Counts, bounds, quote integration and duplicate checks are independently derived; literature/code/results outside those checks are source verification as indicated in the individual rows. No simulation, build, new installation or existing-file modification was performed.

**Final decision: ACCEPT WITH CORRECTIONS — retain A1 as the single next step and A2 as the sole conditional optional extension; correct the claims before handing the Vietnamese answers to the owner.**
