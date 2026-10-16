# Evidence audit of the final thesis

Audit date: 2026-10-04. Scope: the revised thesis, supplied plans and code, recorded transcripts, fixture selections and generated recheck artifacts. This is a read-only audit of experiments. No runner or simulator experiment was launched, no frozen environment was changed, and no research data, failed-run folder or repository configuration was removed.

The reporting audit used `nature-statistics/SKILL.md` from `../nature-skills-audit-2026-10-04/skills/`, with `statistical-reporting.md`, `common-failure-modes.md`, `figure-statistics.md` and `reviewer-checklist.md`. Primary evidence is the supplied plans, raw records and code. Reproducing calculations is distinguished from independent experimental replication.

## Verdict and evidence classification

The principal numerical claims are reproducible at their recorded denominators. H6 fails its frozen service criterion; later exploratory experiments do not reverse that result. Tier 2 supports a distinction between commitment-caused rejection and physical failure. W07 and T38 support a difference in the obligation recorded and the need for non-normal recovery, while completed service can remain close. T38 provides an observed coverage result and a conditional deterministic inequality; it does not establish a population 90% coverage guarantee.

| Family | Reporting unit and replication | Classification and permitted use |
|---|---|---|
| Definitions and no-op/visible-bound results | Decision or rider history, under stated assumptions | Analytic or mechanical statements; observed zeros do not establish novelty or unconditional system feasibility |
| H6, Panel A | 20 matched day/sample cells, 108 arrivals per cell; five shared travel-day realizations | Frozen finite-panel confirmatory comparison. Exact totals and negative service verdict; no population confidence interval |
| Budget/window sensitivity | Same 20 cells, multiple settings | Supplementary descriptive analysis; settings and solver seeds are not independent units |
| Tier 2 | 20 main cells and 16 development cells, eight per morning/evening window | Exploratory controlled experiment with predictions sealed before targeted arms; reference/control trajectories already available |
| W07/W07X | Eight development cells from two days, one episode per setting/cell | Exploratory development evidence; W07X levels selected after W07; unsuccessful predictions and reused runs retained |
| T38 | 15 calibration episodes in six groups; 34 test episodes in 14 groups, shared across five policies; five source days | Exploratory plan fixed before targeted execution. Group labels are disjoint but original trips are not; nominal cell bootstrap and binomial summaries remain descriptive |

`claim-evidence-matrix.csv` maps central claims to classifications, source files/code, numerators, denominators, reporting units and caveats. It separates analytic statements and mechanical invariants from comparative empirical results.

## Source map and reproduced facts

`S` below means `E:/Code/Report_INT3508/ridebound-scratchpad`; `A` means `S/thesis-final-2026-10-04/audit`. The frozen no-worse source is `C:/Code/RideBound-noworse` at `24aa747147d49db79675d170829e6f3bf3afc3cc`; T38 executed the published runner at `C:/RideBoundData/research/runner-tier3-v2`. The current `E:/Code/RideBound-deadline` checkout is a later research branch and must not be substituted for the frozen no-worse implementation.

### H6: the negative service result remains primary

Raw sources are `E:/RideBoundData/wp9/confirmatory-h6-panela-v2/p-<cell>-{b1,c1}-tight-s7/transcript-00.ndjson` and the corresponding `run-00.json`. The frozen report is `E:/Code/RideBound/docs/benchmarking/wp9-confirmatory-result-2026-08-23.md`, with H6 freeze `84f6eff31addbdd12349a19201d79c872fbd05aaf5e0aa45dd73aee6d5c3dee2`.

`recheck_h6_frontier.py` decodes final checkpoints for nine arms on all 20 cells, checks their frame hashes, and compares publication counts and accepted cardinalities with the run record. Separate raw-action extraction uses `S/welfare/extract_promise_movement.py` and the 40 primary transcripts. `h6-raw-movement-recheck.json` records exact agreement with the existing per-run cache; the totals also agree with checkpoint-derived sums in `h6-frontier-recheck.json`.

| Quantity | B1 | C1 | Definition |
|---|---:|---:|---|
| Arrivals | 2,160 | 2,160 | 20 cells × 108 |
| Completed | 1,735 | 1,581 | Final lifecycle; accepted cardinalities agree in these completed runs |
| Decision-induced movement | 74,443,002 ms | 128,020 ms | Open pickup and drop coordinates, pooled over rider histories |
| Rider-visible movement | 83,587,440 ms | 9,332,101 ms | Same coordinate/history scope |
| Retained-route movement | 9,202,610 ms | 9,204,481 ms | Model projection with route retained, including progress/execution effects |
| Decision/visible ratio | 89.0600334213% | 1.3718239869% | Ratio of pooled sums, not mean rider fractions or causal attribution |
| Publications | 54,311 | 45,542 | Counts agree with run fields |

Completion loss is `154/2160 × 100 = 7.1296296296` percentage points. C1 completes 73.1944444444% versus B1's 80.3240740741%; delta is −7.1296 pp, outside the frozen −1.00 pp criterion: **FAIL**. The mechanical burden criterion passes. Aggregate burden decreases by approximately 99.8280%, conditional on performed service work and the full C1 bundle, including the pickup lock. It is not equal work with fewer revisions, an observed user benefit, or the isolated effect of the 30-second drop cap.

At the 600-second pickup window, `nobudget` retains confirmation locks and serves 1,655. B1→`nobudget` loses 80 and `nobudget`→C1 loses 74, a descriptive bundle split. The 60-second arm serves 1,579, two fewer than 30-second C1: deterministic trajectories can diverge; this is not an independent noise estimate. At 900 seconds B1/C1 serve 1,938/1,753, a loss of `185/2160 = 8.5648148148 pp`. Widening that window does not remove the measured cost. A separate fresh check decoded and hashed the final checkpoints of all 120 runs at 900 seconds and asserted that lifecycle-completed counts equal the accepted-count fields used by `recheck_wide_service.py`, in 120/120 cases. The six totals are 1,938/1,837/1,835/1,794/1,761/1,753 for B1/`nobudget`/300/120/60/30 seconds.

The signed relation is `z=c+x`. After absolute values and history sums, only `V<=C+X` is generally valid. The ratios are not additive percentages of a causal traffic/policy partition. The retained-route projection is a local auditable reference, not an identified full traffic effect.

### Tier 2: commitment rejection and physical failure

Sources are `S/deadline/{PREREGISTRATION.md,PREREGISTRATION.sha256,predictions.csv,classify.py,analyze.py,AMENDMENTS.md}` and `E:/RideBoundData/research/deadline-v1/<job>/`. The classifier uses exact source messages and the rejection reason cited for the safety no-op. Host failures are replaced through `effective_output` under the recorded amendments.

Direct reclassification of the 20 main `k=1` cells gives M+-30: 19 `commitment-all-rejected/deadline-late`, one `window-wall`; C-30: zero commitment failures, 11 `window-wall`, nine completed. **19/20 versus 0/20** refers to commitment-caused failure. It does not mean C completes 20/20. The no-op result assumes a valid prior ledger and non-commitment feasibility of the retained route.

Re-reduction of the full prediction table gives strong predictions **98/102** on the main panel, **31/32** in development morning, and **40/40** in evening. Weak predictions are respectively **17/18**, **8/8** and none: combined **25/26**. There are 120 main and 80 development planned rows. Weak cases are separate by the fixed rule, not silently discarded. Policy/cell pairs share cells and are not independent binomial trials.

The final development figure has **eight cells per window**, with commitment-failure counts C/M+/M/V at 30 seconds: morning **0/4/4/8**, evening **0/0/7/8**. An initial revised caption incorrectly associated it with the main 20-cell failure counts; the final source moves the figure beside the development comparison and identifies its actual denominator. The original script's `p=0.0000` for 19/0 discordance is rounded, not a probability of exactly zero; it should not support population inference.

### W07/W07X: means, pooled riders and negative predictions

Sources are `S/tang3/w07/{W07-PLAN.md,W07-REPORT.md,w07_analyze.py,w07_aggregate.py,independent/RESULT.md}` and `C:/RideBoundData/research/tier3-w07-v1`. W07X uses the corresponding plan/report/independent extraction under `S/tang3/w07x`, new raw data at `C:/RideBoundData/research/tier3-w07x-v1`, and explicitly reused W07 runs.

Separate arithmetic from `w07-per-cell-own-promise.csv` gives:

- M+-30 mean own-deadline violation **24.0369809412%**; pooled **156/660 = 23.6363636364%**.
- M+-60 mean **7.2504664502%**; pooled **47/661 = 7.1104387292%**.

24.04% and 7.25% are **unweighted means of eight cell shares**. Calling 7.25% the fraction of all 661 riders would be incorrect. At 30, 60 and 300 seconds C/M+ have identical fleet-action sequences in eight of eight cells; at 120 seconds six of eight match. Their obligations differ: zero conduct-cap violation does not imply zero actual lateness.

W07 has one unsuccessful prediction (Q4); W07X has two (R2, R4). W07X service differences occur only at 90 seconds in one cell and 120 seconds in two cells, one completion each. Settings ≥150 seconds do not establish service superiority. These are development results from two days with source-trip overlap across already viewed windows.

### T38: completed service and obligation-specific fractions

Sources are `S/tang3/t38/{T38-PLAN.md,T38-PLAN.sha256,split-t38-v1.json,GAMMA-t38-v1.json,T38-AMENDMENTS.md,T38-REPORT.md}`, execution/calibration/analysis scripts and independent extractor/analyzer. Raw data are `C:/RideBoundData/research/tier3-t38-v1/<arm>-<cell>/transcript-00.ndjson`. Two interrupted original folders remain; successful `-rerun1` folders replace one calibration and one test job under the recorded infrastructure rule. The second failure was a response timeout; heavy machine load was recorded context, not an established cause.

`recheck_t38.py` checks all **185 successful final checkpoints**: 15 C-30 calibration runs and 34×5 test runs. It hashes each final checkpoint frame and requires exact cache equality for lifecycle and rider histories. It recomputes **382,006 drop revisions** from v/e/p against ledger delta fields, with zero mismatches, then reconstructs gamma, violations and per-cell metrics. Completed counts come from final lifecycle; `summary.json` has no second independently measured served field.

| Test policy | Completed / 3,672 arrivals | Mean forced share | Mean own-promise violation | Pooled own violation |
|---|---:|---:|---:|---:|
| U | 2,434 | 0% | No own cap | Not an efficacy endpoint |
| C-30 | 2,338 | 0% | 0% | 0/2,338 |
| M+-30 | 2,338 | 41.3113664783% | 14.4796344231% | 289/2,338 = 12.3609923011% |
| M+-60 | 2,347 | 22.5276954608% | 4.2313124769% | 79/2,347 = 3.3659991478% |
| V-30 | 2,336 | 53.7757771138% | 21.5767164437% | 456/2,336 = 19.5205479452% |

Each mean is unweighted across 34 test episodes. Forced share uses acknowledged decisions within each episode. Own-promise violation uses promised/completed riders; all promised riders alight in these completed runs. Its endpoints are C>30 s, actual drop minus initial promise>30/60 s for M+, and visible total variation>30 s for V. These are different obligations. U has no own cap; its zero forced fraction is not a promise guarantee.

C−M+-30 has mean zero and range −2…+1 per episode; C−V-30 mean is `2/34=0.0588235294`, with the same range. U−C totals 96, mean 2.8235294118 and range −4…+9. The all-demand difference is **96/3672×100=2.6143790850 pp**; relative reduction from U completions is **96/2434×100=3.9441248973%**. They have different denominators.

The preserved paired cell bootstrap uses 10,000 draws, `random.Random(20261002)`, shared 34-index draws, and sorted zero-based indices 249 and 9,750. Reported intervals reproduce C−M+ [−0.1471,+0.1176], C−V [−0.1176,+0.2059], U−C [+1.7941,+3.8235] customers per episode. They do not adjust shared-day/trip dependence or demonstrate population equivalence. Shared E2 difference is `0.057829712000906926−0.056973108922087685=0.000856603078819241` in fraction units, or 0.0856603079 pp; its rounded interval is [−0.0082,+0.2218] pp. No new hypothesis test was invented.

### T38: gamma, coverage and dependence

There are 15 calibration scores. Alpha=1/10 gives `k=ceil(16×0.9)=15`; gamma is the **largest** calibration score, **222,259 ms**, from `d20181114-s10-r2-w07`. Beta+gamma is **252,259 ms**: below the exploratory 300,000-ms usefulness threshold but above the 120,000-ms reference. The 300-second threshold and acceptance margins were chosen after development results.

- Score coverage: **32/34 = 94.1176470588%**. Exceeding scores are 252,492 ms (`d20181114-s10-r3-w07`) and 226,400 ms (`d20181115-s10-r2-w07`). Morning coverage is 7/9 versus 14/14 and 11/11 in the other windows.
- Actual visible-bound coverage: **33/34 = 97.0588235294%**. Only the first episode exceeds beta+gamma, by **233 ms**. The two events must remain separate.
- In the 32 score-covered episodes, largest observed V is 216,005 ms; no rider violates the conditional inequality.
- Maximum C across all 49 C-30 episodes is 29,239 ms, below 30,000 ms. All 49 have zero non-normal decisions. This checks the conduct obligation, not punctuality or all original physical constraints.

The split has disjoint day/sample group labels but overlapping taxi trips. `check_trip_overlap.py` reads fixture selections and source CSV `(sourceLocalDate,request_id)`, checking equal `rq_time/start/end`. It covers 20 source CSVs and all 49×108 selections. There are **1,574 unique calibration trips**, **3,505 unique test trips**, and **75 original source-trip IDs shared across partitions**, in 41 nonzero episode pairs. Daily overlaps on 14–18 November are 29,9,13,12,12.

The old **43** came from a day-plus-row-ordinal diagnostic. It is invalid because ordinals are local to each sample CSV. `t38-source-row-overlap.json` is marked `INVALID_IDENTIFIER_DIAGNOSTIC_DO_NOT_CITE` and superseded by `t38-actual-trip-id-overlap.json`.

The triangle inequality does not require independence. Population conformal interpretation requires joint exchangeability of calibration/new scores, not established here. Shared days/time coefficients, overlapping windows/trips, window mixture differences, prior exposure and 11 normalization exclusions limit interpretation. Nominal one-sided 95% Clopper–Pearson upper score-violation fraction for 2/34 is **0.1738113065**, approximately 17.4%, under independent binomial trials; it is not a dependence-adjusted population bound. `0.9^15=0.2058911321` is an ideal iid continuous-score illustration, not a demonstrated panel distribution. Observed coverage above 90% gives no guarantee for a new day, a time window or deployment riders.

### Timestamp and sealing provenance

| Item | Hash / commit | Recorded time |
|---|---|---|
| Tier 2 seal | Plan `8eb6a68594e11c9cde55ef07812a1b95adc614d1b930b18a8cdfbbbb669cd451`; predictions `6c5451a0e9ab61a0c4b12da48c6dd517623dfdb35aff7fa73494a79dacb6f981` | Seal 2026-09-24T06:03:52Z records zero targeted-arm outputs; controls/reference already viewed |
| T38 plan | `78954a15201bc8225a7513401b9a3c8f31a9016baa6820ef6de987c9033f8a60`; commit `323a8d91cc8d7a15587b04b597dc4f7a6fb5f822` | Seal 2026-09-30T23:44:04Z; commit 23:44:19Z |
| First calibration transcript | `C-30-d20181114-s10-r1-w07/transcript-00.ndjson` | CreationTimeUtc 2026-09-30T23:44:50.5561757Z |
| Split | `b72ac0f731fa7425891f364f0976054ae172a3117a507155ebe7e5c122ea03f1` | In plan commit |
| Gamma | `2bdd3b0e83a6cd3d09550a4551f063101c68a97b783fe49a8729f1ace9f198cd`; commit `19517b0ca1518df2e16fd84a58f1b53a9978f2e7` | 2026-10-01T16:11:26Z |
| First test transcript | `U-d20181114-s10-r3-w07/transcript-00.ndjson` | CreationTimeUtc 2026-10-01T16:12:19.2894086Z |

Hashes match source bytes. Local commit clocks and filesystem creation times corroborate order; remote push times were not independently established. Scratchpad files are not a separate Git repository. Committed T38 receipts are in `C:/Code/RideBound-noworse/docs/benchmarking/tier3-t38`; related Git object history also contains these commits. Sealing does not upgrade the exploratory design's inferential status.

## Independent checking and remaining integrity scope

This editing pass re-reduced H6 raw extraction against checkpoint and per-arm totals, reclassified the 20-cell Tier 2 contrast from failure files, parsed every prediction row, recomputed W07 mean versus pooled fractions, checked T38 episode totals and bound exceptions, and validated plan/split/gamma hashes and chronology. Existing recheck scripts were reviewed and arithmetic was separately reduced instead of copying rounded manuscript tables.

Historical T38 `iv_extract.py` reads decisions, acknowledgements and alight events from full raw transcripts, and v/e/p from the final checkpoint. `iv_analyze.py` computes endpoints without the experimenter's analysis modules. It does **not** hash every raw frame or independently compare every ledger publication with every raw promise action. Current `recheck_t38.py` adds checkpoint hashes and exact cache/history equality, but inherits cached alight/decision extraction for actual lateness and forced shares. Therefore 185 hashed checkpoints and 382,006 checked drop revisions are not an exhaustive T38 frame-hash or ledger/action integrity sweep. W07X's historical independent audit explicitly performs frame hashing and ledger/action sequence comparisons over 184 runs; its scope cannot be transferred to T38.

Provenance and numerical checks do not establish user satisfaction, full causal attribution, deployment SLA, city-wide road fidelity, global DARP optimality or representative success in a second simulator. RidePy's canonical capability result is distinct from its failed representative subset. The network is a 96-node metric closure with synthetic coordinates, with network-wide time factors. No-worse recovery and late-boarding allowances belong to a particular execution version. Comparators instantiate gate forms in a shared system, not complete algorithms from cited papers.

## Reproduction

Use the existing frozen Python without package installation:

```powershell
& 'E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe' -B 'E:/Code/Report_INT3508/ridebound-scratchpad/thesis-final-2026-10-04/audit/recheck_h6_frontier.py'
& 'E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe' -B 'E:/Code/Report_INT3508/ridebound-scratchpad/thesis-final-2026-10-04/audit/recheck_wide_service.py'
& 'E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe' -B 'E:/Code/Report_INT3508/ridebound-scratchpad/thesis-final-2026-10-04/audit/recheck_t38.py'
& 'E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe' -B 'E:/Code/Report_INT3508/ridebound-scratchpad/thesis-final-2026-10-04/audit/check_trip_overlap.py'
```

These write only recheck outputs in the final thesis audit directory and read original data. `build_verified_figures.py` reproduces four quantitative vector figures from audited CSV/JSON, at designed 160-mm width with panel alignment checks. `mechanism_figure.py` produces the illustrative three-anchor schematic. Neither launches experiments.

Figure sources: `service_budget_final.pdf`→`service-budget-summary.csv` (20 cells per setting/window); `tier2_gates_final.pdf`→`tier2-gates-figure-data.csv` (eight development cells/window); `t38_paired_final.pdf`→34 test episodes in `t38-per-episode-figure-data.csv`; `t38_scores_final.pdf`→49 C-30 episodes in that CSV; `co-che-ba-moc.pdf`→illustrative definitions. Figures are descriptive; no invented interval or p-value is added.

## Remaining limitations and editorial checks

- **P0 inference, addressed by wording:** no population equivalence, independent calibration/test sample or 90% coverage guarantee from T38; retain the 75-trip overlap and shared-day dependence locally.
- **P0 primary result, preserved:** H6 service FAIL is not rescued by changed endpoints, recovery, windows or exploratory thresholds.
- **P1 integrity scope:** distinguish raw independent event extraction from checkpoint/delta verification; do not say all T38 frames were hashed.
- **P1 figure denominator, corrected in final source:** the Tier 2 final figure is 16 development cells, eight per window, not 20 main cells or physical failure types.
- **P1 aggregation:** W07/T38 mean shares differ from pooled rider/decision shares; report units and strict thresholds beside results.
- **P1 history:** retain failed folders and amendments; a timeout under load is not a proven overload mechanism. Controls, development exposure and exclusions remain disclosed.
- **P2 reproducibility:** exhaustive raw alight/ack rechecking would require a fresh extractor cache or new raw integrity audit, which is not claimed here.

No missing sample size or statistical test was invented. Population claims would need new independent grouped validation and repaired split design. This audit makes no implementation/status change in the independent RideBound repository.
