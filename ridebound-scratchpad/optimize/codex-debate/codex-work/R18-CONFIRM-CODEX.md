# R18 — Confirmation audit of Claude's R17 final verdict

2026-10-10. **Overall verdict: ACCEPT WITH CORRECTIONS.** Keep the ranked list and rewrite-first sequencing. The single next step is the whole-thesis claim-and-results revision, **0 new simulation jobs**. Accept a staged optional mechanism study as a scheduling compromise: **108 Stage-1 jobs; 72 conditional Stage-2 jobs; 180 if both stages run**, with the endpoint, gate and wording corrections below. Incident forecasting remains future work.

The verdict is substantially more accurate than the R16 reports. It correctly accepts my R17 corrections on recovery(b), first-order screens, cumulative wording, rider sets, forecast information and Hörl–Zwick. It is not ready to send to the owner verbatim: several categorical or causal statements survived, particularly in the Vietnamese summary and the experimental kill rules.

## Scope, method and anchors

I opened ROUND18-CLAUDE.md, Claude's entire R17-FINAL-VERDICT.md, D03, the relevant source/configuration, thesis passages, both sides' cited audit outputs and debate positions. I used one new Python helper, one process, with no repository imports. It:

- re-derived the main frontier, cumulative totals, per-cell signs and cost denominators from my existing independent audit records;
- re-derived snow counts and explained/residual seconds from my existing per-rider R17 records;
- independently selected/grouped station snow dates and the ten Monday–Thursday dates in the Fielbaum–Alonso-Mora window;
- compared configuration bytes and parsed differences, searched all 11 thesis TEX files, and counted archived fixture/driver directories;
- re-decoded **all 34 archived M⁺-30 terminal checkpoints**, checking their message type, byte length and frame SHA-256, then counted typed breach records.

This is not a new 227-transcript audit or a new forecast evaluation. The source records for the arithmetic were already independently reconstructed in R15/R17. My R18 helper did not independently implement another selector or regenerate the forecast quotations. These limitations matter when claiming “two independent implementations.”

All files were exclusive-created inside codex-work. No simulation, build, installation, deletion, agent delegation or existing-file modification occurred. I did not execute any proposed experiment. I opened the current primary TLC publication page to resolve B72; no trip rows were downloaded.

Anchor keys below are relative to E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/ unless stated otherwise:

| Key | File |
|---|---|
| V | claude-work/R17-FINAL-VERDICT.md, the verdict being audited |
| A / AJ / R15 | codex-work/R15-audit-summary.txt / R15-audit.json / R15-CONFIRM-CODEX.md |
| CX17 | codex-work/R17-REBUTTAL-CODEX.md |
| NEW | codex-work/R18-verification.txt; structured counterpart R18-verification.json |
| PV / CASE / SF / META / SIZE | codex-work/R17-portfolio-verification.txt / R17-C30-sum-case.txt / R17-screen-forecast-verification.txt / R17-metadata-verification.txt / R17-data-size-verification.txt |
| CAP / WX / SCOPE | codex-work/R16-cap-outcomes.txt / R16-weather-inventory.txt / R16-scope-inventory.txt |
| WP17 / DER17 / EL17 | claude-work/r17-rebuttal/r17-wp14r-check-2026-10-10.txt / r17-derived-counts-2026-10-10.txt / r17-wp14r-elapsed-2026-10-10.txt |
| DIAL17 / CR17 / FC / EV / RV | claude-work/r17-rebuttal/r17-verify-dial-2026-10-10.txt / claude-work/R17-REBUTTAL-CLAUDE.md / R16-FORECAST-CLAUDE.md / R16-EVIDENCE-CLAUDE.md / R16-REVIEWER-CLAUDE.md |
| BUD / SHARE / EXP | claude-work/budget-block-diagnosis-2026-10-07.txt / **pooling-share-2026-10-06.txt / exposure-check-2026-10-06.txt at the debate root**, not under claude-work |
| CVP / IDN | claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt / claude-work/r16-evidence/q2-screen-identity-w07-2026-10-10.txt |
| RP / FS2 / NOAA13 / TLC | claude-work/r16-forecast/rider-nowcast-replay-2026-10-10.txt / factor-nowcast-screen-v2-2026-10-10.txt / noaa-event-days-2009-2013-2026-10-10.txt / claude-work/r13-ml-data-samples/tlc_data_reports_monthly.csv |
| HZ | claude-work/pdf/hoerl-zwick-2022.txt |
| FAM | C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/papers/Unreliability_in_ridesharing_systems_Measuring_cha.txt |
| SCRATCH / TEX | E:/Code/Report_INT3508/ridebound-scratchpad/ / E:/Code/Report_INT3508/ridebound/noi-dung/ |
| SRC | C:/Code/RideBound-noworse/src/ |
| T38 / SEL / POL | SCRATCH/tang3/t38/T38-REPORT.md / SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs / SolverBackedRidePoolingPolicy.cs in that same directory |
| SNOW / RUNTIME / validator | SCRATCH/optimize/test-snow-2026-10-06-report.txt / claude-work/RUNTIME-ESTIMATE-2026-10-07.md / SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs |
| D03 / HO | E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md / E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md |

NEW is 19 lines, one keyed JSON result per line. Its keys distinguish raw checkpoint verification from arithmetic on saved audits. Its JSON counterpart records input hashes. I preserve V's B-row numbers below. **AGREE** means the stated fact or the explicitly scoped reading is supported by the opened anchor, not that every underlying trajectory was reprocessed this round. **WRONG** identifies an incorrect value, scope or denominator. **CANNOT CHECK** identifies the unsupported part; it is not silently promoted to verified. I include all 97 rows, including the few that are not load-bearing.

## 1. Confirmation table audit

### Thesis and code: V B1–B25

| B row | Status | Opened anchor and finding |
|---|---|---|
| 1 | CANNOT CHECK | NEW:15 verifies file modification timestamps: main.pdf 2026-09-29 21:19:50 UTC = 30 Sep 04:19:50 Bangkok; the four TEX files also have 30 Sep local mtimes. A modification timestamp alone does not certify the last actual build or that no later build occurred elsewhere. Replace “last built” with “the inspected files have these timestamps.” |
| 2 | AGREE | NEW:14 scans all 11 TEX files and finds 27 bibitems, no Hörl/Zwick/title/identifier hit; META:4,6 and opened TEX/10-tai-lieu.tex agree. The missing citation is real. |
| 3 | AGREE | NEW:14 finds no T3.8/2338/2434 variants searched. This verifies absence of those markers, not an exhaustive semantic proof that no related experiment is discussed. The inspected abstract/conclusion lack the later T3.8 frontier. |
| 4 | AGREE | TEX/02-tom-tat.tex:17–20,66–69 contains the quoted core-departure claim. |
| 5 | AGREE | TEX/02:22–26,71–75; 05:169–182; 09:18–25,224–231 contain the exclusivity framing. Some already scope it to four families; it must remain scoped and name the relaxed-deadline alternative. |
| 6 | AGREE | TEX/02:14–16,64–65; 05:202–217 describe monotonic cumulative accounting. Accounting/enforcement exists; marginal empirical necessity is a separate claim. |
| 7 | AGREE | TEX/05:64–69 contains “không ai tách…”. HZ:529–543 directly defeats that broad literature statement. |
| 8 | AGREE | TEX/07:292–297 proves the no-op claim with A = \|e−e\| = 0 and explicitly requires other checks to pass under assumption (N). Keep that assumption, not only the algebra. |
| 9 | AGREE | TEX/08:1340–1350,1361–1362 states 1874 /1864 /1873, 21/22 service equality and 19/22 equal actions, for the older sweep. META:7 independently recomputes the service totals and 21/22. The 19/22 action count is read from the thesis/report, not newly re-derived from raw action streams here. This is not T3.8. |
| 10 | AGREE | TEX/08:1852–1859 expressly says the 20–25 EUR/h source was not checked against the original. It cannot support an established welfare threshold. |
| 11 | AGREE | TEX/08:1894–1897 contains the quoted attribution sentence. The package confound remains, as R15:345–351 and V D17 recognize. |
| 12 | AGREE | TEX/02:46–47,97–98 uses the causal-attribution keywords. D03:222–224 requires model-projection wording. |
| 13 | AGREE | TEX/02:43,94 uses the promise-preservation sentence. It is about C's own obligation, not a common physical-arrival SLA. |
| 14 | AGREE | TEX/09:30–32 says the computable exogenous boundary is the new point. HZ has the traffic-updated old-route reference; legal responsibility is not established by this construction. |
| 15 | AGREE | TEX/09:224–231 says the preregistered measured-traffic experiment confirms the theorem at exploratory level. Say simulation with measured city-wide factors, and preserve its previewed/exploratory status. |
| 16 | AGREE | SCRATCH/tang3/t38/run_t38.py:9–12 and tang3/configs/wp4-tier3-v2.json:7 specify no-worse recovery for every arm. The driver imports run_w07; its archived runner/WP4 declarations are at run_w07.py:40–48. |
| 17 | AGREE | **NEW:17 re-decodes all 34 M⁺-30 checkpoints**, not three: 154 forcedNoWorse, 8371 forcedReference, 2538 exogenousServiceQuality entries; 2338 completed riders. These are breach entries, not decisions. All 34 checkpoint hash/length checks pass. META:8 agrees. |
| 18 | AGREE | NEW:11–12 independently hashes/parses U/C30/C60/C120. U→C30 has the sole difference /policies/0/limits/1/hardLimit absent→30000. Hash prefixes 998a0a94/d6124f3f/ac0f9758 agree. |
| 19 | AGREE | SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271–303,319–331,365–385 implements the conditional hierarchy. U is the locked hard-vector control, not FREE. |
| 20 | AGREE | SRC/.../SolverBackedRidePoolingPolicy.cs:287,322–333 starts with RollingCost and invokes AssessAndFilter for hard-vector/hybrid. Switching policy kind to rolling-cost would change the experiment's gates. |
| 21 | AGREE | Opened SRC/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:97–108 gives null hard limits and no final-confirmation locks; policy.cs:465–478 chooses the provider. R15 rows41–42 agree. Fixed-freeze is not a shortcut to hard-cap plus cost-first. |
| 22 | AGREE | NEW:2 re-sums AJ: U incumbent/bound/util-present 3503/3503/3503; C30 3506/3506/3506. This is observed utilization-level saturation, not proof every stability level is constant. |
| 23 | AGREE | NEW:16 confirms runner directory exists, 49 fixture directories and 49 driver JSON files. Existence alone is not binary/configuration equivalence or new-run readiness. |
| 24 | CANNOT CHECK | I opened R15 code/configuration rows 38–40: raw archived core 1ce15e9 and the then-audited source change 45f8026. I did not repeat current git ancestry/source-diff analysis this round. Preserve the historical audit status; do not claim today's entire source tree is certified equivalent. Gate 0 remains necessary for a rebuilt binary. |
| 25 | AGREE | Opened SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:222–239: default records the first failing rider/layer; full-witness collection is conditional. R15 row30 opens its default runner configuration. A recorded budget witness is not a complete candidate-feasibility proof. |

### Outcomes and cumulative clause: V B26–B42

| B row | Status | Opened anchor and finding |
|---|---|---|
| 26 | AGREE | A:7–9 and SCRATCH/tang3/t38/T38-REPORT.md:46,58 give U2434 / C2338 / M⁺30 2338 / M⁺60 2347 / V2336. NEW:2 re-sums the first three from AJ; NEW:17 verifies M⁺2338 directly from terminal states. |
| 27 | AGREE | NEW:2: U/C naive late60 =203/76; forecast =137/10; M⁺ forecast =10. M⁺ naive is **74**, not 76. |
| 28 | AGREE | NEW:2 subtracts late counts from service: naive timely60 =2231/2262; forecast =2297/2328; naive timely120 =2332/2327; forecast =2347/2338. |
| 29 | AGREE | NEW:2, U fc_pad30: late60 =106; timely60 =2328; timely120 =2366; extension =37.1833 s; early60 =44/2434 (1.8077%). This is first-quote replay on archived U journeys. |
| 30 | AGREE | NEW:2, C30 fc: extension =7.3671 s; early60 =4/2338 (0.1711%). This **pooled early60 fraction** differs from the weekday late60 cell mean also called 0.17% elsewhere. |
| 31 | AGREE | A:18–19; NEW:3 preserves the independently audited intersections: C/M2332 common plus 6 each; U/C2207 common plus 227/131. Equal service totals do not mean identical riders. |
| 32 | AGREE | Corrected anchor SHARE is at the debate root, :2–4: 22.8/13.4/13.1% among served. The ≈555/313 absolute values are approximations from rounded percentages, not sealed exact integer counts. Use the exact extracted baseline before sealing H6. |
| 33 | AGREE | EXP at debate root:2–3; NEW:2 reproduces 134/203,4/76,174 exposed U riders. 134/174 =77.01% is an intersection statistic, not a causal fraction. |
| 34 | AGREE | Opened T38:50–52: w08−39, w17−52, w07−5 served relative to U. |
| 35 | AGREE | T38:58–59,64: M⁺30 forced 41.3%, self-broken 14.5%, both **cell means**; C/M have 30/34 equal action sequences. Not equal sequences in every cell, and their obligations differ. |
| 36 | AGREE | NEW:4 re-derives from AJ: all 14 w08 and 11 w17 cells have U naive late60 >C30. Those 25 cells are not 25 independent dates. |
| 37 | AGREE | NEW:2 re-sums U 174 exposed /12 repeated /max590133 ms; C 33 /0 /max29239 ms. |
| 38 | AGREE | NEW:1 re-sums98 C runs, 64371 decisions,1256=845+411 recorded prunings, all classified step-fails, zero cumulative-only. B varies over the w07 arms. |
| 39 | AGREE | Opened A:3,5: fixed C60 two cumulative-reported records in one decision; C120 four in three; associated requests ultimately served. Witness counts do not establish counterfactual outcome effects. |
| 40 | AGREE | A:6,20 and R15:195–197: synthetic total6 records/5 decisions/two associated rejections before duplicate removal; distinct4/3/one associated rejection afterwards. The latter is not one causally attributable lost passenger. |
| 41 | AGREE | NEW:1 re-sums repeated=0 for served C riders in this measured-factor corpus. Scope the sentence to **nonzero dispatch changes of drop ETA**, not every revision or all 10 dimensions. |
| 42 | AGREE | CVP:5–8,17,22,32: accepted-history screens at 120 s give T38 U 4/2434; FREE 13/1629; WP9 A 12/1735, B 10/966. FREE has **two at 30 s**. This refutes “cannot be tested at 30 s” as an impossibility claim. |

### Cap dials, screens and objective: V B43–B57

| B row | Status | Opened anchor and finding |
|---|---|---|
| 43 | AGREE | CAP:3–11 and DIAL17: C30→C120 served 660→666; late60 47→51; late120 2→7; timely60 613→615; timely120 658→659. U has 665/50/9/615/656 respectively. |
| 44 | AGREE | CAP:2 and the causal-no15 active=0 rows confirm the primary causal replay is inactive on Nov12/13. Claude's separately reported loo-no15 column uses different information. |
| 45 | AGREE | WP17:2,5,9,14,19, FREE/LOCKS/C120/C60/C30: service 1629/1584/1563/1540/1534; late60 274/47/23/0/0; timely120 1465/1557/1563/1540/1534. |
| 46 | AGREE | SF:2–11: 971 distinct run-decisions, 973 request–run pairs, 807 completed, 166 rejected; T38 has 643 pairs, 495 completed, 148 rejected. These are different counting units. |
| 47 | AGREE | BUD:2–9: 148 rejected requests with recorded budget-pruned options; 116 served under U; 1186 other rejections. Recorded overshoot median 109.6 s, p25 63.7, p75 183.6, max 524.8; screened passes 11/59/135. “Budget-blocked/structural-only” are **record-based path classifications**, not proof of a unique causal reason for every refusal. |
| 48 | AGREE | SF:12,14,18: 5/51/123 late60 crossing occurrences, 0/6/79 late120; B120's 59 passes involve 58 distinct blocking rider–run pairs. The screen adds absolute witness movement to realized lateness; these are not signed joint policy outcomes. |
| 49 | AGREE | IDN:5; SF:26 gives 6 screened passes, 17 gained, 11 lost, net+6. The six screened IDs are among the 17 gains; 11 gains and 11 losses are missed. Matching net+6 is weak calibration. |
| 50 | AGREE | NEW:7 adds 12663+12525+12364+12325+12960=62837 reproductions. R17 used audited-code re-execution plus independent enumeration of the five feasible combinations in the special case. Do not call the whole selector implementation independently reproduced twice. |
| 51 | AGREE | NEW:6: 445/1714=25.9627%; 104/1715=6.0641%; zero accepted-count changes at frozen states. Final accepted totals on changed trajectories remain unknown. |
| 52 | WRONG | Values round correctly, but 0.307/.079% needs a **cost-weighted denominator**, not a mean of frame percentages. NEW:6: LOCKS 114720189/37380402107=0.306899%; C30 28288261/35606312123=0.079447%. Conditional mean percentages 7.7902/8.0038; equal-weight means across new-request frames 2.02255/.48536%. These are distinct estimands. |
| 53 | AGREE | PV:2,5; NEW:8: median fleet-summed added movement 90.819 s under LOCKS,12.494 s under C30; C30 max 35.540 s =two 17770 ms changes. LOCKS max 390.812 s. Attach “max35.5” explicitly to C30; it is not a per-rider push. |
| 54 | AGREE | PV:8: FREE GATE 76 /RANK 325 /NONE 12559; 33555.398/(14953.481+33555.398)=69.17%. Pickup-gate classification is an upper bound before a pickup ETA lock exists. It is a local decomposition, not 81% of terminal FREE–LOCKS service/late/pooling gaps. |
| 55 | AGREE | NEW:11 confirms four commitment-config byte identities. NEW:13 confirms recovery, lateBoarding, skipConstantObjectiveLevels and evidence-profile differences; **policyVersion also differs**. Core 38d517d versus 1ce15e9 is recorded in opened R15 rows 38–40/AJ. None establishes rebuilt compatibility or transfer of effect sizes to T38. |
| 56 | AGREE | EL17:2–6: rounded median seconds FREE 730 /LOCKS 667 /C30 641, over 16 archived jobs each. Future T38 cost-first runtime is unconfirmed. |
| 57 | AGREE | RUNTIME-ESTIMATE-2026-10-07.md:24–25 gives historical 170 jobs/about 7 h at six parallel/about 15 min per job. NEW:18's 4.5 h/3 h extrapolation is arithmetic, not measured Stage 1/2 completion time. |

### Forecast/data, boundary and positions: V B58–B85

| B row | Status | Opened anchor and finding |
|---|---|---|
| 58 | AGREE | NEW:5 recomputes NAIVE 41 /HIST 34 /BLEND-in 21 /prefix-gate 19 /BLEND-L1 29 from 601 saved rider records. RP:7–20 reports equal-cost pad 27. That row is PAD@REGB-1.2; 1.2/1.3 select the same snow prefix method here, not separately frozen pad experiments. |
| 59 | AGREE | NEW:5: 34/601=5.65724% pooled. RP:6–8 labels 5.94% HIST and 7.19% naive as cell means. Pooled naive 41/601=6.82%, not 7.19%. |
| 60 | AGREE | NEW:5: total 3445.933 s; dispatch 8.566; HIST 251.496; prefix 1138.355; additional 886.858=25.736%; residual 2299.012=66.717%. Residual subtracts dispatch and the method's clipped explanation; it is not irreducible uncertainty. |
| 61 | AGREE | NEW:5 selects the minimum of my R17 independent 36-grid fit: α=1, β=0, φ=.8; 80 targets; SSE 0.0118126096. Initial trend 0 **and α1** make the residual multiplier 1. β0 alone does not imply HIST for every α. |
| 62 | AGREE | FS2:219–223: snow minimum 1.323; weekday maximum 1.244. Threshold 1.3 was chosen after inspection; REGB uses prefix information (opened factor_nowcast_screen_v2.py:weight). |
| 63 | AGREE | RP:39–40: 2/1471 in 21 selected weekday cells. Not a global headroom ceiling or a pooled 0.17% late rate. |
| 64 | AGREE | SCRATCH/optimize/test-snow-2026-10-06-report.txt:10 gives late120 .0069; opened family_snow.py:32–37 averages cell fractions. It is a **naive cell mean**; not all snow lateness lies between 60–120 s. |
| 65 | AGREE | SF:30 contains the saved Central Park SN row at 13:44. It is the first matching row in that extraction, not exact city-wide onset, feed delivery time or an archived forecast vintage. |
| 66 | AGREE | **NEW:9 independently groups** SNOW ≥25.4 mm dates at most two days apart: Nov15; Feb12; Feb20; Mar1–4; Dec2. Five test spells, four after excluding the inspected Nov2018 event. These proxies do not prove independence or traffic disruption. |
| 67 | AGREE | META:2–3 verifies Jan/Nov2013 footers: zone IDs, no lat/lon;14776617/14388451 rows. Scope to **two tested files**, not all 2013 schemas or row quality. |
| 68 | AGREE | SIZE:2 gives 5354364554 bytes =5.354364554 decimal GB for 44 months; SF:31 gives2013 total 2143914255 bytes =2.143914255 GB. Metadata sizes do not establish decoded storage, transfer or rebuild costs. |
| 69 | AGREE | TLC:1,552,556,860: the field is Trips Per Day. Nov2013 yellow 479527; Nov2018 yellow 271501; FHV–HighVolume 691379. Missing 2013 FHV reporting does not establish zero ride-hail. |
| 70 | AGREE | **NEW:10 independently counts** six Mon–Fri 2013 dates≥1 inch and two≥3 inches (Feb8, Mar8). FAM:577–579 excludes Fridays: ten Mon–Thu dates extend through Jan29, not Jan25. NEW:10 checks all ten, including Jan28/29, with SNOW 0. Holidays were not removed from the year count. |
| 71 | AGREE | FAM:571–584: 4091 nodes/9453 edges; Jan15 13–15 h; ten Mon–Thu dates from Jan14; traffic-disregard motivation; 19610 requests after passenger-count filtering. This chosen benchmark is not an incident-forecast dataset. Full 2013 is a separate question. |
| 72 | AGREE | Current primary [TLC trip-record page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), publication paragraph, checked 2026-10-10: monthly releases typically lag two months. A live/operator feed is an additional assumption, not supplied by this archive. |
| 73 | CANNOT CHECK | Not load-bearing. I do not certify every content claim in FC's three-paper literature table in R18. CX17:113 identifies what was checked at primary level in R17 and its limits. Familiar forecast components and D03's restrictions are not a certificate of exhaustive literature priority. |
| 74 | AGREE | HZ:507,529–543,567–569: old-route traffic update, max(updated,latest), motivation avoiding undefined states. The first-offer substitution max(p0+B,e) is an explicit inference/variant, not the paper's literal promise definition. |
| 75 | AGREE | HZ:575–606: hard required-time constraints(9–10) plus original-time penalties(11). “Hard gate rather than penalty” does not distinguish C from HZ. |
| 76 | AGREE | D03:211–217: Elmi per-rider guarantees are prior; S&P uses 900 s slack in the inspected setting. C30 is much tighter; same-core comparators do not reproduce those full algorithms. |
| 77 | AGREE | D03:54–56: unreliability detection, pre-decision control and service–stability trade-offs are prior. |
| 78 | AGREE | D03:236–245 permits specification, implementation, audited obligations and bounded trade-offs. Incremental practical value is unconfirmed. No satisfaction, revenue, profit or operator-demand claim follows from C. |
| 79 | AGREE | Opened HO:145–147,396 names HZ-B as close prior and requires citation. |
| 80 | AGREE | R15:335,349: 74 is the described **future** 2×2 minimum, not measured execution cost; the cap dial was not an automatically authorized simultaneous project. Combining it within one optional study is a scheduling proposal. |
| 81 | AGREE | CX17:153–188,211: rewrite first, 178 minimum jobs, 70–110 h opinion estimate. NEW:18 confirms the arithmetic; staging explicitly changes that proposal. |
| 82 | AGREE | CR17:314–324,351–386: 2×2 first, 74 jobs, 30–50 h; stable-C120 34 jobs; mandatory rewrite in parallel/as fallback. These are proposals, not executed work. |
| 83 | AGREE | RV:524–538: A1+ first, zero runs; optional work after draft/deadline. Calling M⁺(b) identical to literal HZ remains wrong. |
| 84 | AGREE | Current antigravity-work file listing contains ANTIGRAVITY-BRIEF.md and no result. No third review is available to count as agreement. The folder alone does not prove why its session failed. |
| 85 | CANNOT CHECK | HO:494–495 explicitly says mid-November needs confirmation. No owner/supervisor deadline or institutional standard is confirmed here. Time boxes, effort and degree-pass forecasts remain conditional opinions. |

### Earlier statements rejected by the judge: V B86–B97

Here AGREE means I agree with the judge's correction, not with the original statement.

| B row | Status | Opened anchor and finding |
|---|---|---|
| 86 | AGREE | EV:27 is ambiguous in its summary; its table is per differing frame. CASE and NEW:8 give 35.54 s across two riders, 17.77 s each. Reject a per-rider 35.5 s interpretation. |
| 87 | AGREE | EV:27 omits conditioning. NEW:6 gives 7.79% conditional mean and .3069% ratio of summed plan costs under LOCKS. Neither is realized operating-cost saving. |
| 88 | AGREE | FC:39–42 assigns an unsupported knowable/unknowable interpretation. NEW:5 measures a method-dependent retrospective residual. |
| 89 | AGREE | FC:43–51 and forecast information rules: 19 requires undelivered prefix/post-hoc gate; strict in-window 21; lagged trend 29 still has the exact current anchor. Fully realistic latency is not established. |
| 90 | AGREE | FC:33–35 and SNOW:10: naive>120 s cell mean .69% contradicts “whole headroom” in60–120 s even here. No conclusion about all future storms. |
| 91 | AGREE | FC:70 and the TLC rows do not support zero 2013 ride-hail. |
| 92 | AGREE | RV:157 and HZ:575–606 contradict the hard-versus-penalty distinction. |
| 93 | AGREE | RV:184–186,388–395; driver/config and NEW:17 contradict the missing(b) premise. Identical M⁺(b) rerun is redundant; literal always-relaxed HZ is distinct. |
| 94 | AGREE | RV:493; CAP shows C120 666>U 665, refuting 96 as a monotone recovery bound. A prediction interval is not a mathematical ceiling. |
| 95 | AGREE | RV:501–503 /EV:281; A classifies recorded witnesses. Counts do not bound unrun trajectories or identify causally lost service. |
| 96 | AGREE | EV:213–216: 2327+59−6=2380 is arithmetic over incompatible marginal screens, not a policy estimate. Fail-fast evidence and identity mismatches prevent summation. |
| 97 | AGREE | Opened claude-work/R13-FINAL-VERDICT.md:51–58;R15:87–93 preserves the correction. Recorded single-step-failing budget witnesses remain failing under an equal-B per-step check, but “exactly the same candidates/trajectories” is unproved with incomplete witnesses and no per-step run. |

## 2. Overclaim audit and required changes

D03 permits the implemented and audited combination without establishing global priority, causal identification, external effectiveness or business value (D03:1–12,136–147,211–245,260–269). Keep the contribution at that level. The measured drop-budget results do not demonstrate empirical value for every dimension of the wider framework.

### Corrections affecting the ranked list

| Verdict location | Problem | Correction |
|---|---|---|
| V:205, “Accumulation cannot be tested at B = 30 s” | CVP reports two cumulative-only accepted histories under FREE at 30 s. Sparse exposure is not impossibility. | “Recorded exposure is sparse at 30 s and larger at 120 s on several uncapped paths; 120 s is the chosen test budget.” |
| V:120–127,463–465; D11 | “Same allowance B” can imply a fresh B each epoch; “never exercised” can imply accumulation was not enforced. D11 also says physical-arrival results are the same. | B is an **all-trip** absolute dispatch budget; remaining allowance is B minus prior spending. No recorded failure in the measured-factor corpus needed prior spending to explain its budget error. C/M have equal aggregate service and forecast timely60, not identical journeys or every arrival metric: naive late60 C76/M74 (NEW:2). |
| V:347–349 and §0 Q2 | “All feasible endpoint is U” / approximately 555 s can imply policy equivalence. | U is the measured removal-of-drop-cap reference. About 554.8 s clears the **reported selected budget thresholds** for the 148 recorded rejected requests; it does not certify hidden failures, admission of all 148, or equivalence to U. Even U's observed maximum S, 590.133 s, exceeds 554.8 s. |
| V:393–394, §C Q4 | “Over all frames” obscures three different cost statistics. | Conditional mean percentage changes: 7.79/8.00%; mean percentage change over new-request frames: 2.02/.49%; ratio of summed repeated-plan costs: .3069/.0794%. None is a realized operating-cost or profit result. |
| V:400,668 | “The cap restricts what CF can change by 4×” / “the cap itself blocked most changes” can imply a matched causal comparison. | These are 26.0% versus 6.1% **on different archived state populations**. They suggest constrained opportunity, not an isolated 4× causal effect of adding C. |
| V:603–604,724 | “Core firm” and “independent down to each rider” are too broad. | Independently reconstructed archived outcomes agree in the stated corpus. Full selector re-execution reused audited code; the forecast screen reused specified quotation functions. Mechanical evidence is strong; external validity and institutional acceptance remain unconfirmed. |
| V:601–602 | “None makes the new part bigger” precludes useful future research. | Algorithmic components are prior. A matched experiment may add **new bounded empirical knowledge**; its novelty and significance are not guaranteed. |
| V:439, §E6 | Full 2013 “usable only” as an ablation / at least ten independent snow spells can sound like established scientific requirements. | Extra-history ablation is the recommended conservative **design choice**, not the only possible data use. Ten is a design minimum, not a power or independence theorem. My earlier minimum included rain proxies; five snow spells is a valid concern but does not count all incident types. |
| V B67,711 | Two checked 2013 schemas are generalized to the entire year. | “The inspected Jan/Nov 2013 official files have zone IDs without coordinates; other months and row quality have not been independently verified.” |
| V:243 | HO's “No work approved” becomes “owner must approve every run.” | HO records no authorization at that handoff. R18 authorizes only an audit. Future authorization should concern the concrete protocol and budget; HO does not demand a separate permission question for each job. |
| V B1 and A1 deadline risk | File mtimes become proof of the last build; zero jobs becomes proof of low overall deadline risk. | Report inspected mtimes. Revision removes simulation risk; total writing/supervisor effort and deadline remain unconfirmed. |
| V:770 | CX17:125 is cited alongside the source of the “same riders” error. | CX17:125 is **my correction of Claude's wording**, not my assertion that the sets are identical. Preserve that attribution. |

### Corrections to predictions and kill interpretations

I accept the predictions as previewed-panel design choices, labelled H. Several failed targets currently lead to conclusions they cannot support:

- **a1:** Below 2362 means the registered recovery target of +24 at C120 was missed. It does not show that cap level is “not the main lever” for other B or contexts. The 2434 upper endpoint is a prediction, not a bound; w07 already violates U as a service ceiling.
- **a3:** At most 2332 means this C120 point does not beat **both** observed naive timely120 endpoints. It may still beat C30 (2327), and it does not rule out other interior points. Never infer an optimum.
- **H2:** Failure of exposed ≥261 **and** late60 ≥243 means the chosen materiality prediction failed. It does not show selector invariance, absence of a confounder, or small effects on every metric. Large pooling/service changes could occur without 40 extra late completions.
- **H3:** Passing the late-fraction guards shows those fractions were retained under the changed selector. It does not prove “the cap alone suffices” or that C guarantees physical arrivals. Locks, recovery, generation, traffic and quote profiles remain shared.
- **H4:** DiD <40 is not evidence of objective independence. A negative DiD can itself be an interaction; a small nonzero interaction still fails the +40 target. Report the estimate, per-cell/day contrasts and uncertainty. State which materiality target was missed.
- **H6:** Failure to gain 10% does not imply “does not buy pooling”: a 5% gain would miss H6 but be positive. Set the integer cutoff to ceil(1.10 × the **exact** stable-C30 shared-completion count), not a number derived from rounded 13.4%. The 345 target is illustrative until the exact baseline is extracted and frozen.
- **H7:** Fewer than ten cumulative-only completed CF-U histories is a resource-allocation stop rule. It does not bound rejected-candidate witnesses or prove that C120/per-step paths cannot diverge. H2+H7 may gate Stage 2 for scheduling; the gate is not empirical proof of insignificance.
- **H8/H9:** Report any distinct cumulative-only decision and any per-step S >120 history even if the ≥5 target fails. Zero cases means no demonstrated difference in this tested design, not general uselessness. Larger outcome gaps must be reported with their sign and service composition; they do not automatically establish practical benefit.

These corrections require no additional simulation jobs. They change what the study may conclude.

## 3. Verdicts and accepted resolutions

| Object | Verdict | Reason / accepted resolution |
|---|---|---|
| Ranked list of at most three | **ACCEPT WITH CORRECTIONS** | Rewrite first; one optional staged mechanism study; forecasting as future work. Remove the categorical/causal wording above. No substitute research branch is needed to fix this verdict. |
| Single recommended next step | **ACCEPT** | Whole-thesis bounded revision, zero new jobs. Abstract/introduction/conclusion misposition the closest prior and omit the later frontier. Revision is mandatory regardless of a new experiment. I accept the sequencing resolution and retain my R17 ranking. |
| Optional extension/design | **ACCEPT WITH CORRECTIONS** | Staging defers per-step engineering while preserving the direct matched comparison if Stage 2 runs. Correct endpoint interpretation, service/quote guards and post-build rechecks. This is proposed work, not implemented or authorized work. |
| Job count | **ACCEPT** | NEW:18: 34+(4+2+68)=108; Stage 2=68+2+2=72; both=180. Seventy-four covers Stage 1b only; 178 was my one-build minimum; 180 adds two OFF rechecks after a second build. These are different plans, not inconsistent arithmetic. |
| Primary endpoint resolution | **ACCEPT WITH CORRECTIONS** | Accept model-experiment reliability interaction as primary and move my ≥10% sharing target to key secondary. The fixed-state C30 opportunity is modest and uncertain. Late60 DiD must show service composition; it is not pure causal blame or proof that the cap alone preserves arrivals. |
| Forecast alternative versus future work | **ACCEPT** | R17 already changed my ranking. One inspected scalar-factor storm, oracle current anchors, prefix mismatch and an open multi-year/as-of pipeline do not justify replacing the completion step before an unconfirmed deadline. |
| Current strict top-venue core | **REJECT, unchanged reviewer opinion** | Closest prior covers key reference/control ideas; superiority and business value are unconfirmed; few previewed days, one traffic factor and one incident limit rigor. Revision improves accuracy; it is not itself new top-venue research. Degree/conference acceptance is not certified. |

### Staging instead of my R17 front-loaded 178-job plan

Keep one optional study, after the A1 milestone and deadline confirmation:

1. **Stage 1a:** 34 stable-C120 jobs using the hashed archived runner, configuration, fixtures, worlds and harness contract. No rebuilt binary is needed. “No Gate 0” means no new-build equivalence jobs, not permission to skip binary-tree, inventory, argument, seed and configuration checks. Record the copied harness hash and manifests.
2. **Stage 1b:** Four OFF equivalence jobs (U/C30 × one w08/one w17); two ON smokes; 68 main CF-U/CF-C30 jobs. Preserve forced avoidance, accepted-count priority, gates, locks, recovery(b), generation/work/retention budgets and ties. Skip only the intended stability ranking. Source feasibility is not completed implementation.
3. **Stage 2, conditional:** 34 CF-cumulative120 +34 CF-per-step120, two ON smokes, two OFF rechecks after the second build. Retain cumulative S for audit but disable its enforcement consistently across assessor, decision validator, certificates and breach semantics in the per-step arm. Freeze exact recheck arms, cells and reference artifacts before building; exercise the changed 120 s path against available controls. If validation needs additional jobs, disclose them before approval; 180 is the specified minimum, not a guarantee against infrastructure or compatibility failures.

All Stage-2 arms must use the same second binary; only budget mode changes for the direct cumulative/per-step comparison. Compare manifests explicitly when combining stages. Meaningful unit/differential checks required by C:/Code/RideBound-noworse/AGENTS.md are future engineering work, not hidden simulation jobs. None was run in R18.

Stop on equivalence failure. There is no silently substituted control panel or uncounted retry allowance in the stated budget.

My argument for the direct comparison still holds: **without Stage 2, the thesis cannot claim an empirical cumulative-versus-per-step outcome effect.** It may report the Stage-1 history screen and say the policy comparison was deferred. Staging is acceptable because that missing result is optional; witness-only evidence cannot replace it.

### Primary endpoint and guards

Retain the pooled naive late60 interaction as a **model-experiment contrast**:

    I_L = (L_CF,U − L_CF,C30) − (L_SF,U − L_SF,C30)
        = (L_CF,U − L_CF,C30) − 127.

Use the same 3672-request panel, common naive-quote construction, and unchanged gates, locks, recovery and generation settings. L counts late **completed** rider–runs. Rejected requests are absent from L; served sets can change.

For each arm, timely60 = served − late60, so:

    I_L = I_served − I_timely60.

This identity is NEW:19. Late-count interaction alone therefore cannot isolate arrival quality from service selection. Report the three request outcomes—timely completion, late completion and rejection—their full 2×2 contrasts, shared served-set diagnostics, and paired per-cell/day results. Common-served strata are post-treatment populations, not randomized causal estimands.

Keep timely60/120 per request, service totals, late fractions, quote extension, early-arrival cost and sharing mandatory beside the primary. Preserve the predeclared service-retention/quote-cost guards before labelling a lower late count an improvement; the 99% service guard must not disappear when H6 fails. Describe trade-offs instead of claiming that the cap alone preserves reliability. Padded U is a descriptive frontier, not a matched objective control.

Five days and dependent cells do not supply 34 independent replicates. Uncertainty estimates with five day clusters are fragile; report the observed paired pattern without new-day/population guarantees. Do not retune B, load, forecast or endpoints after seeing results.

I accept the sharing-priority revision. The 7.79/8.00% conditional plan-cost reductions did not establish realized efficiency gains; the C30 ratio of summed plan-cost reduction is only .0794%. A 10% absolute-sharing gain with a service guard remains a useful secondary hypothesis, not an extrapolated result.

### Timing and future forecasting

The judge's three-week/two-week/one-week time boxes are reasonable **scheduling choices**, not verified feasibility. Stage 1a 2–4 h, Stage 1b 25–43 h, Stage 2 22–44 h and the historical 4.5 h/3 h compute extrapolations remain opinions or arithmetic. Cost-first T38 runtime was not measured.

I accept the event-count concern without changing a rain-inclusive incident benchmark into a snow-only benchmark. NEW:9 confirms five snow proxy spells in my proposed test period, including the inspected storm. More coverage or narrower claims are necessary for snow-specific generality. Rain/other strata should be defined on calibration and reported separately. “Ten independent snow spells” is not a universal power condition; 18 heavy-snow weekdays across winters do not automatically mean 18 independent events.

The future protocol must separate the reconstructed full-duration target from causal observations: completed trips plus delivery times, weather issue/availability vintages and features available when quoting. Freeze chronological fit/calibration/test and quote-cost budgets; exclude the inspected Nov12–18 bundle week from confirmatory scores. Full 2013 history may be an extra-history ablation with explicit year/domain shift. The off-peak FAM subset does not answer incident forecasting. R18 has not built or validated that pipeline.

## 4. Corrected Vietnamese wording for section C

These replacements retain the storyline without promising novelty, practical value or institutional acceptance.

### Opening and Câu 1

> Giữ hướng hiện tại để hoàn thành một luận văn có phạm vi rõ. Việc tiếp theo duy nhất là viết lại các tuyên bố và kết quả trên toàn luận văn, chưa chạy thêm mô phỏng. Sau khi phần này được soạn và hạn nộp được xác nhận, có thể làm một nghiên cứu cơ chế tùy chọn: đổi thứ tự ưu tiên của bộ chọn trong khi giữ nguyên các cổng và đối chiếu các mức trần.
>
> Vẫn còn câu hỏi nghiên cứu chưa trả lời: đổi bộ chọn có thay đổi đánh đổi phục vụ–giờ đến không; nới trần trên 34 ô chính có lợi ở ngưỡng nào; và dự báo có cải thiện trên nhiều sự kiện độc lập không. Các thành phần kỹ thuật đã có tiền lệ, nhưng phép so phù hợp vẫn có thể bổ sung hiểu biết thực nghiệm mới. Chưa có kết quả bảo đảm các hướng này tốt hơn.
>
> Bằng chứng mạnh hiện có là cơ chế đã được hiện thực, sổ cái kiểm được, và số liệu đã được dựng lại trong phạm vi đã kiểm. Điều đó chưa xác nhận ưu thế vận hành, tác động nhân quả hay giá trị doanh nghiệp. Hörl và Zwick đã dùng giờ trả cập nhật trên tuyến cũ theo giao thông; luận văn phải trích và đối chiếu cơ chế này.
>
> Trên 3672 yêu cầu của 34 ô đã xem trước, C30 có dự báo và U có dự báo cộng thêm 30 s cùng có 2328 lượt đến không trễ quá 60 s. C30 phục vụ 2338 lượt, còn U phục vụ 2434. Độ kéo dài báo giờ trung bình là 7.37 s so với 37.18 s. Số lượt đến sớm hơn báo giờ quá 60 s là 4/2338 (0.171%) so với 44/2434 (1.808%). Ở ngưỡng 120 s, U có dự báo cộng 30 s có 2366 lượt kịp ngưỡng, còn C30 có 2338. Đây là các điểm đánh đổi đã đo, không phải ưu thế chung của C.
>
> C30 và M⁺30 đã dùng phục hồi(b) cùng phục vụ 2338 lượt và cùng có 2328 lượt kịp ngưỡng 60 s khi phát lại dự báo. Có 2332 lượt chung, mỗi nhánh có 6 lượt riêng. Không gọi đó là “cùng mọi khách” hay “cùng mọi giờ đến”.

Anchors: NEW:2–3,17; HZ:529–588; D03:222–245; T38:46,64.

### Câu 2

> 1256 là số bản ghi phương án bị chặn do ngân sách giờ trả, không phải 1256 khách. Chúng xuất hiện trong 971 quyết định của 98 lần chạy; 973 cặp yêu cầu–lần chạy liên quan có 807 cặp cuối cùng vẫn được phục vụ.
>
> Trên 34 ô T3.8 C30, có 148 yêu cầu cuối cùng bị từ chối và có ít nhất một phương án mang dấu vết bị chặn do ngân sách của khách khác. Khoảng 555 s sẽ làm các ngưỡng ngân sách được ghi cho ít nhất một phương án của mỗi yêu cầu này qua phép sàng lọc. Do bộ kiểm tra dừng ở lỗi đầu và quỹ đạo sau sẽ đổi, điều đó không bảo đảm cả 148 yêu cầu trở nên hợp lệ hoặc được phục vụ. Không gọi 148 là số từ chối đã chứng minh chỉ do trần.
>
> Bỏ trần giờ trả trên 34 ô đã đo cho thêm 96 lượt phục vụ, thêm 127 lượt trễ quá 60 s và giảm 31 lượt kịp ngưỡng 60 s, với cùng cách báo giờ tương ứng. Đây là một điểm đối chứng đã đo, không phải cận trên cho mọi trần hữu hạn.
>
> Nới C30 lên C120 trên 8 ô sáng đã đo cho thêm 6 lượt phục vụ, thêm 4 lượt trễ quá 60 s, **thêm 2 lượt kịp ngưỡng 60 s** và thêm 1 lượt kịp ngưỡng 120 s. Trên 16 ô giao thông cố định, C120 thêm 29 lượt phục vụ và 23 lượt trễ quá 60 s, nên thêm 6 lượt kịp ngưỡng 60 s. Vì vậy không kết luận nới trần chỉ có lợi ở ngưỡng 2 phút. Có lợi hay không phụ thuộc tiêu chí, giá của lời hứa và điểm đánh đổi.
>
> Ở sàng lọc cố định trên 148 yêu cầu, B120 cho 59 yêu cầu qua ngưỡng được ghi và tạo 51 lần vượt ngưỡng trễ 60 s theo cách tính của màn sàng lọc. Đây là các lần xuất hiện của witness, không phải 51 người được chứng minh bị làm trễ, và không cộng các trường hợp thành một quỹ đạo chạy thật.
>
> C120 trên 34 ô chính còn thiếu. Có thể chạy 34 job cấu hình trong nghiên cứu tùy chọn sau khi sửa bản thảo, nếu có thời gian và được cho phép. Một điểm mới không xác định mức trần tối ưu.

Anchors: SF:2–18,26; CAP:3–7; WP17:9,19; BUD:2–9; validator:222–239.

### Câu 3

Replace the bullet “all exceeded 30 s”; retain the correctly scoped formal paragraph:

> Trong 98 lần chạy cưỡng chế C dùng hệ số giao thông toàn thành phố lấy từ dữ liệu đo (64371 quyết định được xác nhận), cả 1256 bản ghi chặn do ngân sách giờ trả đều ghi nhận một độ dời tuyệt đối do điều phối vượt **B của nhánh tương ứng**. Không phải tất cả nhánh đều có B =30 s: bộ này còn gồm C60 đến C300.
>
> Không bản ghi nào cần phần ngân sách đã dùng trước đó để giải thích lỗi ngân sách được ghi. Không khách đã phục vụ nào dưới C trong bộ này có hơn một lần dời giờ trả khác 0 do điều phối. Vì vậy phần cộng dồn chưa là lý do riêng cần thiết cho một lỗi ngân sách được ghi nhận.
>
> Chưa cài đặt và chạy nhánh mỗi bước một trần, nên chưa biết bỏ cộng dồn có giữ nguyên quỹ đạo hoặc kết quả không. Bốn quyết định ở giao thông cố định và ba quyết định ở thế giới giả lập là dấu vết được ghi sau bỏ bản chạy lặp, không phải cận trên cho tác dụng hoặc số khách mất do cộng dồn.
>
> Cộng dồn vẫn xác định một nghĩa vụ khác: mỗi bước ≤30 s có thể cho ba bước tổng 90 s; luật tổng ≤30 s không cho phép lịch sử ấy. B là tổng ngân sách cả chuyến, không phải mỗi thời điểm được cấp lại B. Trong quỹ đạo không trần đã đo, có 12/2434 khách T3.8 được dời giờ trả khác 0 nhiều lần; dấu vết này chưa chứng minh lợi ích đầu ra của C.

Anchors: NEW:1–2; A:3–6,20; R15:87–93; CVP:17.

### Câu 4

> Trên trạng thái đã ghi của WP14r giao thông cố định, thay ưu tiên ổn định bằng ưu tiên chi phí, vẫn giữ số yêu cầu nhận và các cổng tương ứng, đổi lựa chọn ở 445/1714 quyết định có yêu cầu mới dưới LOCKS không trần (25.96%) và 104/1715 dưới C30 (6.06%). Đây là hai tập trạng thái khác nhau, chưa phải phép so quỹ đạo chỉ khác một yếu tố.
>
> Ở các quyết định đổi lựa chọn, trung bình phần trăm giảm chi phí kế hoạch là 7.79% và 8.00%. Nếu tính trung bình phần trăm trên mọi quyết định có yêu cầu mới, các số là 2.02% và 0.49%. Nếu lấy tổng giảm chi phí kế hoạch chia tổng chi phí kế hoạch đã chọn trên mọi frame được xác nhận, các số là 0.3069% và 0.0794%. Chi phí kế hoạch còn lại được tính lặp qua thời gian; không suy ra tiền xăng, chi phí vận hành thực hay lợi nhuận.
>
> Kết quả gợi ý rằng dưới các cổng C30, bộ chọn có ít cơ hội đổi hơn trên những trạng thái đã kiểm. Chưa biết quỹ đạo mới sẽ thay đổi phục vụ, ghép chuyến và giờ đến bao nhiêu.
>
> Phần 2×2 cần 68 job chính mới và 6 job kiểm tra, tổng 74. Thêm 34 job stable-C120 thành 108 cho Giai đoạn 1. Nếu đạt ngưỡng đã chọn và còn thời gian, Giai đoạn 2 thêm 72 job để so CF-C120 cộng dồn với CF mỗi bước 120 s, tổng 180 nếu làm cả hai.
>
> Nếu C30 giữ được đánh đổi giờ đến–phục vụ khi đổi thứ tự ưu tiên, đó là bằng chứng cơ chế trong cấu hình mô hình này. Không kết luận “chính trần, không phải bộ chọn, giữ mọi lời hứa” hoặc C tự bảo đảm giờ đến thực. Nếu dự đoán lớn không đạt, báo giá trị và chiều thay đổi; không biến việc không đạt ngưỡng thành chứng minh không có tác động.

Anchors: NEW:6–8,18–19; PV:2,5; SEL:271–385; R15:349–351.

### Câu 5

> Dự báo cho ngày có sự kiện là một hướng nghiên cứu thật, hiện để ở việc tương lai. Trong phát lại buổi chiều tuyết đã xem, phần dời do điều phối trong sổ cái của 41 lượt trễ theo báo giờ ngây thơ là 8.566 s trên 3445.933 s. Phát lại chỉ đổi mốc báo giờ, không thay tuyến đã chạy hoặc sổ cái C. Điều này không chứng minh mọi cải tiến dự báo hoặc mọi sự kiện đều không ảnh hưởng đến điều phối/C.
>
> Trên 601 lượt đã phục vụ, HIST có 34 lượt trễ quá 60 s. BLEND chỉ dùng các snapshot trong khung mô phỏng cho 21 lượt; đây không phải kết quả của cổng chuyển chế độ 1.3. Prefix BLEND/cổng 1.3 cho 19 nhưng dùng thêm prefix từ 06h ngoài dữ liệu Runner của khung 14h/15h, và ngưỡng được chọn sau khi xem số liệu. BLEND-L1 cho 29: chỉ phần xu hướng bị lùi một bin, mốc neo vẫn là snapshot hiện tại chính xác của mô phỏng. Cả 21 lẫn 29 chưa xác nhận một nguồn dữ liệu thực có độ trễ và nhân quả đầy đủ.
>
> 34/601 là 5.66% gộp. Số 5.94% là trung bình tỉ lệ của 8 ô; không dùng hai mẫu số thay nhau. Mô hình prefix đã thử giải thích thêm 886.858 s so với HIST, bằng 25.74% tổng giây trễ trong nhóm 41 lượt được chọn hậu nghiệm theo độ trễ ngây thơ. Phần còn lại sau trừ dispatch và lời giải thích prefix là 2299.012 s (66.72%). Không gọi 26% là giới hạn phần biết trước được, hoặc 67% là không thể biết.
>
> Giao thức damped-trend vòng 12 đã khớp α=1, β=0, φ=.8, với xu hướng khởi tạo 0; trong dạng đã chỉ định nó cho hệ số hiệu chỉnh dư bằng 1. Không chạy lại giao thức ấy như một cải tiến hứa hẹn. Không suy ra mọi mô hình xu hướng đều vô ích.
>
> Phép so công bằng cần dựng và kiểm mục tiêu hệ số theo công thức nguồn, tách mục tiêu hậu nghiệm khỏi quan sát chỉ từ chuyến đã hoàn tất và đã gửi về; thời tiết dùng đúng thời điểm phát hành/sẵn có. Chia học/hiệu chỉnh/kiểm theo thời gian, có baseline lịch sử và persistence mạnh ở cùng giá báo giờ, bất định theo sự kiện, không chấm xác nhận trên tuần 12–18/11 đã xem.
>
> Giai đoạn 9/2018–12/2019 có 5 đợt theo proxy tuyết ≥1 inch và quy tắc ghép ngày đã chọn; một đợt đã xem. Đó là cảnh báo cho suy rộng về tuyết. Số sự kiện mưa hoặc loại khác phải được kiểm riêng, không lấy số ngày làm số sự kiện độc lập. Ước tính 80–140 h, cộng thêm nếu cần thời tiết có vintage, vẫn chưa xác nhận bằng triển khai.
>
> Fielbaum–Alonso-Mora chọn Jan15/2013 13–15h và mười ngày Mon–Thu từ Jan14 với mục tiêu bỏ qua bất ổn do giao thông; subset đó không trả lời câu hỏi dự báo sự kiện. Cả năm 2013 là nguồn khác có thể thử làm lịch sử bổ sung. Metadata nén khoảng 2.144 GB; hai tệp chính thức Jan/Nov2013 đã kiểm có mã vùng, không có tọa độ. Hai ngày Mon–Fri tuyết ≥3 inch là Feb8 và Mar8. Có đổi miền dữ liệu: taxi vàng 479527 chuyến/ngày ở Nov2013 so với 271501 ở Nov2018. Thử thêm lịch sử với year/domain effect và baseline cùng dữ liệu; không hứa pipeline đã khả thi chỉ từ metadata.

Anchors: NEW:5,9–10; RP:6–40; META:2–3; TLC:1,556,860; FAM:571–584; claude-work/r16-forecast/factor_nowcast_screen.py:14–27; D03:222–269.

### Reviewer verdict in Vietnamese

> Theo chuẩn phản biện nghiêm của tạp chí hàng đầu, lõi hiện tại vẫn chưa đủ: định vị mới hẹp, chưa có phép so cơ chế bộ chọn–trần, số ngày/sự kiện ít và giá trị vận hành chưa xác nhận. Đây là đánh giá của người phản biện, không phải quyết định của hội đồng/tạp chí.
>
> Luận văn có thể được trình bày trung thực quanh đặc tả, hiện thực, kiểm nghĩa vụ và đánh đổi đã đo sau khi sửa lớn. Việc có đáp ứng yêu cầu bảo vệ hay không còn do chủ nghiên cứu/người hướng dẫn/hội đồng xác nhận. Không hứa một thí nghiệm tùy chọn sẽ đủ để đăng bài.

## 5. Minimal corrections before owner handoff

The detailed tables are the audit trail. Claude's verdict needs these five groups of changes:

1. **Repair Q2/Q3 scope:** 148 record-associated rejections, rather than cap-caused riders; approximately 555 s only clears reported witnesses; U is not an upper bound; all 1256 exceed branch-specific B, not always 30 s; loosening can increase timely60 at a one-minute threshold.
2. **Repair guard/kill interpretations:** Sparse 30 s exposure is not impossibility; missed materiality targets are not invariance or insignificance proofs; primary DiD must show service/rejection composition and preserve quote/service guards.
3. **Repair outcome/information language:** Equal aggregates, not identical riders/all arrivals; B is an all-trip ledger budget; forecast residual is not a knowability limit; 21 is in-window blend, 19 prefix/post-hoc, 29 lagged trend with oracle anchor; pooled 5.66% differs from the 5.94% cell mean.
4. **Make cost and provenance precise:** Three cost denominators; repeated plan cost is not realized saving; no hard-versus-penalty novelty; M⁺ already used(b), literal HZ is distinct; two 2013 footers are not all months; file mtimes are not certified build history; correct SHARE/EXP paths and the attribution of my rider-set correction.
5. **Retain and label the staged budget:** 108 plus conditional 72 =180 minimum planned jobs; specify post-build rechecks; preserve previewed hypotheses and future implementation/authorization status. Deadline, effort and degree acceptance remain unconfirmed. Forecasting stays future work.

These are report/protocol corrections, not work I executed outside codex-work.

## 6. Final ranked list and files

1. **Now:** Whole-thesis bounded claim/results revision; zero new simulation jobs.
2. **At most one optional study afterward:** Staged objective × cap mechanism study; 108 jobs plus 72 conditional jobs, 180 minimum if both stages run.
3. **Future work:** Causal multi-event incident forecasting. A literal HZ baseline is also future work, not another immediate project.

Exclusive-created files:

- R18-CONFIRM-CODEX.md — this report.
- R18-verify.py — arithmetic, configuration, weather and archived-checkpoint helper.
- R18-verification.json — structured results and input hashes.
- R18-verification.txt — keyed 19-line verification output.

**One-line verdict: ACCEPT WITH CORRECTIONS — rewrite first (0 jobs); accept the staged 108+72 optional study with bounded endpoint/gate interpretation; keep incident forecasting as future work.**
