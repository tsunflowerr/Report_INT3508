# Round 19 — Codex independent verification and Stage 1a audit

2026-10-10. **Antigravity verdict: MAJOR REVISION. Stage 1a design: ACCEPT WITH QUALIFICATIONS. Stage 1a outcomes: NOT READY at the recorded check.** Keep the owner-approved rewrite and staged study. The139 claim groups contain83 AGREE,39 WRONG and17 CANNOT CHECK verdicts. Antigravity mostly copies correct archived counts, but its causal explanations, cumulative-equivalence claim, commercial claims and damped-trend recommendation are not justified.

This round reads no `claude-work/R19-*`. No simulation, build, installation, job control, shared-environment write or thesis change occurred. All new files are exclusive-created in `codex-work`. The Stage 1a analyzer has not been executed or imported. Its syntax and isolated forecast/completion-gate functions were checked separately without reading C-120 outcomes.

## Evidence and interpretation

AG line numbers refer to `antigravity-work/R16-ANTIGRAVITY.md`. Repeated assertions are covered by the same numbered audit row; the table names their repeated locations. AGREE verifies the stated fact with the scope given here. WRONG covers contradicted values and interpretations that the cited evidence does not establish. CANNOT CHECK identifies unknown facts, untested hypotheses, subjective ratings and effort estimates; it is not evidence of impossibility.

Paths below are relative to `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate` unless absolute:

| Key | Source |
|---|---|
| CX | `codex-work/R15-CONFIRM-CODEX.md` |
| A / AJ | `codex-work/R15-audit-summary.txt` / `R15-audit.json` |
| V | `antigravity-work/inputs/R13-FINAL-VERDICT.md` |
| FP / RS / BG | `antigravity-work/inputs/ROUND16-FACT-PACK.md`, `ROUND16-REVIEW-STANDARD.md`, `BAN-GIAO-PHIEN-2026-10-09.md` |
| N / NJ | `codex-work/R19-verification.txt` / `R19-verification.json` |
| SF | `codex-work/R17-screen-forecast-verification.txt`; detailed records in the adjacent JSON |
| R18 | `codex-work/R18-CONFIRM-CODEX.md`; supporting `R18-verification.txt/json` |
| PROTO | `codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md` |
| SRC | `C:/Code/RideBound-noworse/src` |
| D03 | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` |
| HZ | `claude-work/pdf/hoerl-zwick-2022.txt` |
| FAM | `codex-work/r13-paper-text/Unreliability_in_ridesharing_systems_Measuring_cha.txt` |
| FLEET | `claude-work/pdf/fleetpy-etrr-2026.txt` |
| T38 | `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md` |
| OPT | `E:/Code/Report_INT3508/ridebound-scratchpad/optimize` |
| T | `E:/Code/Report_INT3508/ridebound-scratchpad/tang3` |
| BUD / LAD / LOAD | `claude-work/budget-block-diagnosis-2026-10-07.txt`, `wp14r-ladder-reanalysis-2026-10-08.txt`, `load-and-occupancy-2026-10-07.txt` |
| SAMPLES | `claude-work/r13-ml-data-samples` |

I re-opened Antigravity's five input files and the material cited below. Its V and CX copies are byte-identical to the corresponding debate originals (N:1). BG's copied content was read; its original location was not independently established. N records hashes of the reviewed answer, inputs, execution sources, runner tree and all 34 fixtures. Existing independent raw audits are retained as evidence; this report does not falsely call their arithmetic a new simulation or claim to re-read all 227 transcripts this round.

## 1. Antigravity claim-by-claim verification

### Framing, rule, outcomes and rejected alternatives

| ID | AG lines / claim | Verdict | Checked value, correction and anchor |
|---|---|---|---|
| A01 | 3: Gemini 3.8 Flash, high; read-only input scope | CANNOT CHECK | Reviewer identity and actual access history are supplied metadata, not independently attested. The answer cites D03 and code outside its declared input directory; those references can be inherited from inputs and do not prove direct access. |
| A02 | 4–7: date, author/context, FleetPy/Manhattan November 2018 study; strict venue standard | AGREE | Date matches this round; BG and FP describe the study. RS:3–17 specifies strict transportation/OR review. This is the requested review lens, not evidence of publication or institutional acceptance. |
| A03 | 8–14: mandatory input anchors | AGREE | All five copied files exist; N:1 records identical V/CX copies. D03 exists and was opened separately by this checker. Citation presence is not proof Antigravity opened D03. |
| A04 | 20: ACCEPT WITH MAJOR REVISION | CANNOT CHECK | Reviewer opinion. I agree with major revision as a debate response; strict-venue acceptance of the thesis remains unestablished. |
| A05 | 21,72,353: “over 1,991 runs”; later “1,991 complete” | AGREE | BG:463–465 reports an inventory of 1,991, with Codex finding 17 additional runs and 40 FleetPy calibration runs. Do not equate this inventory with 1,991 independent tests of the central claim or a single homogeneous dataset. |
| A06 | 21: LaTeX unedited since September 30 | AGREE | BG:71 states this; R18-verification.txt:15 independently records sampled source mtimes around September 30 local. This establishes sampled file age, not a full edit-history/build audit. |
| A07 | 21,42,51,72,350–366: mid-November deadline, five weeks, guaranteed incompletion/rejection | CANNOT CHECK | FP's constraints and RS:16 explicitly say UNCONFIRMED. Five weeks is a rough conditional estimate; deadline, supervisor acceptance and inevitable failure are not established. The owner has now approved both steps (Round19 brief). |
| A08 | 23,365: zero-run consolidation first | AGREE | A1 can synthesize existing verified evidence without simulation. R17/R18 retain the rewrite as the main delivery. No claim that writing itself has already been completed. |
| A09 | 23,256–288,356: optional ~74-job cost-first study | AGREE | 4 OFF + 2 smoke + 68 main = 74 for Stage1b. It is not the whole current study: approved Stage1a34 + Stage1b74 =108; conditional Stage2 adds72, total180 if both stages execute (R18-verification.txt:18). |
| A10 | 25–30: measured/screen/inference/hypothesis/opinion definitions | AGREE | Useful distinctions, consistent with RS:27–31. They must govern the content; several later “inferences” are untested forecasts. |
| A11 | 37: unreliability/control/trade-off and per-rider constraints already prior | AGREE | D03:54–56,211–220; CX:138–148,323. No broad novelty for detecting instability, pre-decision control, first-offer deadlines or individualized ride-time limits. |
| A12 | 37: forecast/ML ETA and commercial guarantees forbidden as broad novelty | AGREE | D03:236–245,260–269 and CX:299–323 constrain those claims. Novelty and demonstrated business value are separate questions. |
| A13 | 38–41: actionable value, confounders, fair information, reproducibility criteria | AGREE | These are appropriate review questions (RS:7–17), not evidence that RideBound has satisfied them. Multi-agent agreement alone does not validate a result. |
| A14 | 51,68: no viable alternative; every alternative empirically falsified/exhausted | WRONG | R17/R18 identify a plausible objective experiment and a future multi-event forecast study. Failure of one pilot and sparse screens do not exhaust methods. Correct claim: prioritize a bounded rewrite/study given effort and unresolved transfer. CX:299–309; R18's staged recommendation. |
| A15 | 55–58: x=e−v, c=p−e, z=p−v=x+c | AGREE | FP:31–32; ledger model and CX:161. They are same-state model projections, not complete causal identification of real-world traffic. D03:222–224. |
| A16 | 60,163: Rule C bounds sum of absolute dispatch changes by B | AGREE | FP:31–32; CX:90 and ledger audit A:3–17. The guarantee concerns its charged model dimension, subject to forced/recovery behavior; it is not a bound on actual arrival minus first quote. |
| A17 | 61,67: forecast integrated into initial offer | AGREE | OPT/display_layer.py:1–19,36–72 describes the displayed first-quote replay. It did not redispatch the archived trips or prove a deployed booking system. CX:65. |
| A18 | 62,318,321,367: shocks logged/attributed through ledger | AGREE | Typed exogenous/recovery records exist; R18-verification.txt:17 verifies Mplus incidents separately. Correct scope is model attribution. Do not infer that every residual is unforeseeable or that the certificate explains all physical causes. |
| A19 | 64–65,227,331: 34 cells, 3,672 requests; C30=Mplus30=2,338; common2,332 | AGREE | A:7–8,19; N:8–9. Equal counts coexist with six unique served riders on each side. |
| A20 | 66,216,227,239,331: Mplus forced41.3%, self-broken14.5%; pooled12.4% | AGREE | T38:58–59,111 and CX:58–59. 41.3/14.5 are cell means; 12.4 is pooled by rider. These are the rule's own compliance measures, not a common arrival SLA or dispatch-only breach rate. |
| A21 | 23,66,233–238,331: C30/U zero forced and own self-broken rates | AGREE | T38:58–59; CX:58; measured C ledgers A:7,9. “Own self-broken” for uncapped U is not an arrival guarantee: U still has203 naive late60 completions. |
| A22 | 67,238: C forecast2328 timely60,10/2338 late=.43%, naive3.25%, +7.4s,4 early=.17% | AGREE | N:8 recomputes 7.367123s extension, .427716% late, .171086% early; CX:64,170. These are pooled all34 outcomes. “Negligible” quote cost needs an operator preference; no such preference is verified. |
| A23 | 69,334: weekday2/1471 forecast-late riders | AGREE | CX:124,305; OPT/FORECAST-REPORT.md's weekday section. Only a fixed-cohort threshold headroom; not a ceiling on weather, quote sharpness or future-date improvement. |
| A24 | 69: ML2/3/5 fail, vehicle state adds no value | AGREE | BG:334–339 reports the fixed pilot/amendment outcomes; BG:341–349 limits their interpretation. Correct scope: these models/features and this sample, not all ML or all fleet state. |
| A25 | 70: proportional screen differences19/30 =.52/.82pp | AGREE | CX:128,253:19/3672=.517429pp;30/3672=.8170pp. They are partial candidate-screen cardinality differences. |
| A26 | 70: those differences establish an upper policy benefit | WRONG | CX:249–265 explicitly rejects a trajectory-wide ceiling. A changed policy changes later schedules/candidates and hidden blockers; screens do not identify final added completions. |
| A27 | 70: Molenbruch, Lyft patent, Mt-KaRRi already individualized/proportional constraints | AGREE | CX:142,147–148; Molenbruch primary text:154–164 uses fractional excess of direct ride time. Mt-KaRRi and patent anchor constraints to accepted/original trip ETA; neither is this exact cumulative dispatch ledger. |
| A28 | 71,348: 66–68 deterministic micro-units, not elapsed solver latency | AGREE | CX:111,267–279; SRC/RideBound.Solvers.OrTools/OrToolsCandidateSelectionSolver.cs:149–154,462–473. These recorded maxima do not prove evaluator/generator optimization exhausted. |
| A29 | 71: zero candidate truncation | AGREE | Objective-levels-check-2026-10-10.txt:5,9; CX:101. Cap/omitted-by-cap/work-exhaustion counters are zero in inspected U/C runs, while each reports one omitted request and generator limits remain100 candidates/2 new riders. |
| A30 | 72: pivot “academic suicide”; strict chapter deadline | CANNOT CHECK | Strategic opinion, not a measured fact or institutional standard. Replace certainty with a concrete writing/time-box decision. |

### Cap, accumulation, load and source code

| ID | AG lines / claim | Verdict | Checked value, correction and anchor |
|---|---|---|---|
| A31 | 79,101: loosening destroys reliability and necessarily gives negligible service gains | WRONG | Larger B weakens the dispatch allowance and can worsen a chosen arrival threshold. It does not destroy its stated B-bound. T38 C120 had not yet finished at the recorded check, so its actual net service gain is unknown. Report the tested ladders and a hypothesis (N:10; LAD:2–6). |
| A32 | 83,116–120,248,332:98 measured C runs,64371 decisions,1256 prunes,all increments>B,zero cumulative-only/repeated | AGREE | N:7 re-sums AJ:98/64371/1256/1256/0/0. These are recorded acknowledged prune records and final served ledgers, not all potential routes/counterfactual states. |
| A33 | 82–84: records are not lost riders; T38 has845,148 budget-blocked,116 U-served | AGREE | A:7; BUD:2–5,10; CX:130.148 describes observed rejected-request attribution and116 cross-arm identities, not identified recoverable riders. |
| A34 | 85:1186 structural-only rejects | AGREE | BUD:4–5 gives1075+111=1186; with148 totals1334=3672−2338. |
| A35 | 85: those1186 are completely unaffected by a changed cap | WRONG |111 of the structural-only C30-rejected requests are served by U (BUD:5). Classification at the recorded C30 states does not imply invariance under a changed trajectory. CX:130,197. |
| A36 | 87–91: overshoot p25/median/p75/max63.7/109.6/183.6/524.8s | AGREE | BUD:6; CX:130. This is the smallest recorded overshoot per blocked request, not the uncapped per-revision median. |
| A37 | 93–95: B60/120/300 screens11/59/135, .30/1.61/3.68pp | AGREE | BUD:7–9; SF SCREEN rows. Exact fractions=.299565/1.606754/3.676471pp of3672. “Admits” means the reported witness passes a first-order screen, not simulated completion. |
| A38 | 97–100: w07 eight cells864 requests; B30/60/90/120/150/180/240/300 prune142/106/71/38/26/18/6/4 | AGREE | N:10 and A's eight w07 rows independently retain the full ladder. |
| A39 | 99: w07 served660/661/664/666/666/666/665/665 | AGREE | Same N:10 rows; not monotone at larger caps. |
| A40 | 100: tenfold cap eliminates97% of records, gains5 (.58pp) | AGREE |(142−4)/142=97.1831%;665−660=5;5/864=.578704pp. No identified one-to-one correspondence between removed prunes and gained riders. |
| A41 | 102–105: WP14r16 cells1728;1534→1540→1563→1584 and late60 0→0→23→47 | AGREE | LAD:2–6; A:3–5 verifies enforced-C served totals.6/23/21 service increments and0/23/24 lateness increments follow. “1:1 penalty” is aggregate arithmetic across different cohorts, not matched-rider causality. |
| A42 | 106: cap120–300 permits single-step changes exceeding2–5min | WRONG | A normally enforced120s/300s absolute cap does not permit a single charged step exceeding120s/300s. It permits at most the remaining allowance. Actual lateness can exceed it through traffic/execution residuals. FP:31–32; CX:161. |
| A43 | 106: a tight1–2min arrival guarantee then ceases | WRONG | Rule C never supplied a1–2min actual-arrival guarantee even at30s. The guarantee is cumulative charged dispatch change; distinguish the empirical arrival frontier. D03:236–239; CX:161,225. |
| A44 | 106: Lyft10min is an industry drop-off liability threshold | WRONG | It is a qualified scheduled airport-bound PICKUP credit policy, not a general drop guarantee or industry standard (CX:146,241). Rechecked at [Lyft's scheduled rides page](https://help.lyft.com/hc/en-us/all/articles/115013078668), “On-Time Pickup Promise” section. |
| A45 | 106: uncapped U .08% >10min | AGREE | A:9/N:8:2/2434=.0821693% against the naive first drop quote. Comparing that arrival count with Lyft pickup terms does not establish liability or business value. |
| A46 | 113,124,227,332: cumulative clause proved inert/equivalent to per-step | WRONG | Correct finding:zero recorded cumulative-only measured-C prunes and zero repeated nonzero changes in final served ledgers. No per-step counterfactual was implemented/run; default evidence is fail-fast. CX:91–93,189–206. |
| A47 | 122: WP14r37214 decisions;6 cumulative records in4 decisions,2/1 at60 and4/3 at120; all associated requests served | AGREE | A:3–5:12525+12325+12364=37214; CX:88. This37214 denominator is those48 audited C30/C60/C120 runs, not all160 WP14r bundles or just16 cells. |
| A48 | 123: deduplicated synthetic4 records3 decisions≤1 finally rejected | AGREE | CX:89,325 and AJ.synthetic_duplicate:identical w08 rerun removed. One associated final rejection is observed, not a causal or counterfactual service bound. |
| A49 | 124: charging c rather than x is the proved active ingredient | WRONG | It is a specification distinction and plausible mechanism. The recorded audit alone does not isolate every contribution of gates, recovery, locks and selection. CX:193–199,225; D03:222–224. |
| A50 | 127: cumulative-only requires prior spend and another increment each≤B whose total>B | AGREE | CommitmentBudgetEvaluator before+delta=after. More precise:prior absolute spend>0, new delta≤B, after>B. Equality delta=B is allowed in the single-step comparison; “all increments strictly<B” is unnecessarily restrictive. |
| A51 | 127–138: higher load, larger budget, cost-first, dwell would activate it | CANNOT CHECK | Plausible mechanisms, not sufficient conditions. They may change detours/service and still produce zero cumulative-only records. R17/R18 propose tests; none guarantees activation. |
| A52 | 129: U occupancy .535, load .814; FleetPy benchmark~1.33 | AGREE | LOAD:2; FLEET:421–449,472–478. Ours includes idle time in two-hour windows; FleetPy uses180 four-seat vehicles/full-day21400 sampled requests/30s boarding and alighting. These are descriptive, unmatched regimes. |
| A53 | 130:6–8passenger vans/airport chains;15+15+10=40>30 | AGREE | The arithmetic is correct as a hypothetical example. Those fleets/routes were not measured here and their efficacy is CANNOT CHECK (A51). |
| A54 | 132: U nonzero-revision median108.6s | AGREE | CX:69; OPT/report-extras/constraints-and-pooling-2026-10-06.txt:6.187 revision events, a different denominator from148 blocked requests. It does not imply all typical/feasible insertions exceed30s. |
| A55 | 133:51.8+80.3=132.1>120; FREE50/1629=3.07% repeated | AGREE | CX:88 exact51.755+80.304=132.059s; FP:44–45 and CX:85. A rejected candidate witness differs from an accepted rider history. |
| A56 | 135,147–153: forced→accepted→worst util/revisions→cost→ID hierarchy | AGREE | SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271–303,319–331,365–385 was re-opened. Forced priority requires the hard/hybrid profile and a forced candidate; hard-vector utilization/revisions require an applicable hard limit. It is not an unconditional five-level chain in every decision. |
| A57 | 151:3503/3503U and3506/3506C saturated at1e6 | AGREE | N:7–8 uses AJ; objective-levels-check:3,7 and CX:101 restrict the denominator to new-request-considered decisions where the level exists. Total U/C decisions20760/20101; new-considered3641/3644. |
| A58 | 151: ten revision dimensions include pickup/drop ETA | AGREE | CX:99; FleetSelection.cs:510–522 and CommitmentDimension.cs:19–32. Those dimensions do not all have hard limits in this config. |
| A59 | 136,145,158–161: stability rejects almost all pooling; cost-first definitely changes behavior/uses slack/minimizes miles | WRONG | Ranking preference follows source; “rejects” conflates ranking and hard feasibility. Both U/C use stability-first, so their22.8→13.4 difference is not isolated objective attribution. Cost-first can select the same incumbent, and abstract Schedule.OperationalCost is not proved fleet mileage. CX:341–345. |
| A60 | 152: operational cost=travel time/distance | WRONG | Source:367–368 minimizes Schedule.OperationalCost; raw manifest identifies abstract-generalized-cost-v1. Realized fleet distance/busy-time extraction remains unconfirmed. CX:345; AG itself admits this at167. |
| A61 | 154,274–281: implement accepted-count→cost, preserve forced priority and hard gates | AGREE | This is a coherent proposed code ablation, not a current config. Explicitly skip both utilization and revision soft levels if that is the sealed definition; preserve assessors/locks/recovery/retention/ties. CX:343. |
| A62 | 154: retained hard gate written as one-step abs(c)≤B | WRONG | The retained existing gate must stay sum abs(c)≤B. A per-step gate is a separate Stage2 treatment; writing the weaker formula silently changes the experiment. FP:31–32; R18 staged design. |
| A63 | 154,166: FREE/rolling-cost removes limits/locks/recovery | WRONG | FREE's fixed-freeze assessor removes limits/locks (CX:108). Merely switching objective profile to RollingCost does not by itself rewrite every config limit or erase the recovery option; it can bypass hard assessment and lose conditional forced priority. Correct warning:profile switching alone is not hard-cap-preserving. Policy.cs:287,322–333,465–478; FleetSelection.cs:276–280; CX:343. |
| A64 | 158: U22.8% vs C13.4% sharing | AGREE | CX:67; pooled sharing metrics retained in T38 evidence. Also report served counts and absolute shared completions. This is a gate/package contrast under the same ordered selector. |
| A65 | 159: FREE53.1% vs LOCKS21.8% in WP14r | AGREE | LAD:2–3; V:251 labels the package comparison. It does not predict an identical hard-gate cost-first outcome. |
| A66 | 159: C30-cf≥+10pp attributed to P2.1/V277 | WRONG | V:277 predicts U-cf≥32.8%=22.8+10pp, not C30-cf+10pp. AG later uses the U version (284), contradicting its earlier C version. Both numerical expectations lack an empirical objective-only basis. R17/R18 replace the rationale; thresholds are design choices. |
| A67 | 161,163–164: accumulation may rise; drop budget remains; waits may worsen | AGREE | As hypotheses plus a conditional gate property. More pooling/revisions, pickup volatility and realized lateness must be measured; no assured mileage benefit or empirical activation. |
| A68 | 167: realized distance/busy-time extraction unconfirmed | AGREE | CX:345; V:294–296. Do not substitute repeatedly summed remaining-plan operational costs for realized cost. |

### Forecast, data and literature

| ID | AG lines / claim | Verdict | Checked value, correction and anchor |
|---|---|---|---|
| A69 | 174: 2013/multi-year options fundamentally misread prior work and unviable | WRONG | Deferring a full pipeline is reasonable; impossibility is not established. A paper's constant-traffic experiment does not remove traffic/weather information from the original TLC records. R18-verification.txt:10 and CX:299–309. |
| A70 | 178: Fielbaum/Alonso-Mora15Jan2013 13–15 off-peak, traffic treated stable | AGREE | FAM section5, re-opened this round:one-time experiment15Jan, daily experiment ten Mon–Thu dates starting14Jan. The input's “owner PDF lines571–576” belongs to a different extraction; cite section5/PDFp9 rather than portable line numbers. |
| A71 | 179: dataset excluded traffic shocks, zero adverse weather, no gridlock training signal | WRONG | FAM assumes stable off-peak travel for its model; that is not a weather exclusion test on the whole public dataset. R18-verification.txt:10 records six2013 weekdays≥1inch snow and two≥3inches, plus rain on several sampled January dates. Signal/transfer feasibility remains unvalidated. |
| A72 | 179: “pre-ride-hailing era”2013 vs2018 | CANNOT CHECK | A historical-period label is not an established schema or forecast-transfer barrier. The relevant checked barriers are coverage, spatial/timestamp schemas, labels and simulator mapping. |
| A73 | 181: Nov2018 yellow8,155,449 rows; millions over years | AGREE | FP:78, V:460; SAMPLES/parquet-footer-probe-2026-10-09.txt. Metadata count, not a downloaded/trained multi-year benchmark. |
| A74 | 183,334: public Yellow/FHV/HVFHV schemas lack promise labels | AGREE | CX:126,303; inspected TLC dictionary files in SAMPLES. Restrict “none” to inspected public schemas, not all possible internal/licensed data; no promise labels does not rule out auxiliary traffic-duration prediction. |
| A75 | 184: one city-wide15min factor;15min files12–18Nov only | AGREE | FP:74–75; SAMPLES/factor-inventory-2026-10-09.txt; T/world/preflight_world.py:51–71. Hourly11–18Nov also exists; no15min11Nov factor is supplied by the current bundle. |
| A76 | 185: Sep–Dec2018 one weekday≥1inch; Jul2016–Feb2020 seven≥3inches | AGREE | SAMPLES/noaa-event-days-2026-10-09.txt:2,7:Central Park daily proxy, Mon–Fri with holidays included. These are station-days, not citywide incident onset observations or independent severe-delay events. |
| A77 | 185,334: only seven weather events; statistically inadequate for every complex ML study | WRONG | Same saved table lists49≥20mm rain weekdays in2016-07..2020-02 and16≥1inch snow weekdays. Seven pertains only to the selected≥3inch snow threshold. Small independent-event coverage is a concern; no architecture-independent statistical impossibility follows. |
| A78 | 186: wrapper reads bundle factors only; new day needs new data/wrapper checks | AGREE | T/world/preflight_world.py:51–71; CX:127. This is a current implementation restriction; a versioned research wrapper is possible. |
| A79 | 186: new-day work necessarily >80–120h and severe corruption risk | CANNOT CHECK | Effort/risk forecast, not measured fact. R17/R18 distinguish a zero-run predictor replay from a full new-day dispatch simulation and propose80–140h forecast work plus20–50h vintage work, all estimates. No installations or modifications are needed to state this distinction. |
| A80 | 186,309: Syed2021 method versus static historical shape | AGREE | SAMPLES/syed2021_DataSheet1_section1_excerpt.txt gives factor construction Eq.S1 (recorded durations/free-flow durations,15min bins). A fixed historical-growth forecast cannot respond to a new shock's unobserved future path. It is our quoting baseline, not evidence Syed tested this exact dynamic nowcaster. |
| A81 | 190–197: prior-day histories, delivered current/past traffic and alerts only; no future outcomes; two-sided quote frontier | AGREE | PROTO:9–40; display_layer.py:12–19,36–72. Availability means delivered at quotation time, not merely a historical timestamp. Exact current simulator factors and post-hoc weather prefixes are not automatically available to a real operator. |
| A82 | 198–200,298,312: Gardner/McKenzie1985 damped exponential smoothing | AGREE | [Primary paper](https://www.bauer.uh.edu/egardner/3301H%20Operations%20Management/ESG%20Publications/1985%20Forecasting%20trends.pdf), printedp1238 Eq4–6, re-opened online; classical level/trend/damping method. Its traffic/log-residual use is our adaptation, not a published RideBound experiment. |
| A83 | 199–201,306–319,360,367: this damped-trend replay is a viable new decisive next step | WRONG | SF “R12 FIT”:36-grid/80 correlated targets selects alpha1,beta0,phi.8,SSE.011812609599550359,zero initial trend. It yields no residual trend correction and reproduces HIST for the same profile vintage. Repeating the sealed-style fit cannot establish the advertised new gain. R17/R18 already demote it to a documented negative diagnostic/future alternative. |
| A84 | 200: snow starts13:00 and observed last15–30min divergence proves real-time feasibility | CANNOT CHECK | “e.g.” is an illustration. SF NOAA FIRST SNOW ROW is13:44 Central Park; it is not citywide onset or delivery evidence. A profile factor with a timestamp is not proof it was observable then. |
| A85 | 201,319: T0 replay over existing trips,0 simulations | AGREE | The proposed operation type is display-only replay. No runtime/effort or fairness outcome is established by the0-run count. |
| A86 | 207: Antigravity brief27–28 requires top3 | CANNOT CHECK | No ANTIGRAVITY-BRIEF.md is among the five supplied input files; its exact cited content/access was not independently verified. RS supports the six criteria, not this exact external pinpoint. |
| A87 | 226: Fielbaum prior pre-decision unreliability control; Schulz/Pfeiffer first-offer bounds | AGREE | D03:54–56,214–217; CX:138,323. Prior deadline design is not the entire Mplus implementation or a full published-algorithm replication. |
| A88 | 226: HZ B is per-step0s for onboard riders violating deadline | AGREE | HZ:529–543,567–606:required deadline=max(updated old-route projection, original latest); additional delay over the updated reference is0 when the original limit is already violated. Nonviolating riders retain slack; Eq11 penalties remain. This is conditional onboard recovery, not a general zero absolute-change ledger. |
| A89 | 227,272,310: first empirical demonstration/genuine novelty of specific causal ledger/ablation/nowcasting | CANNOT CHECK | No exhaustive precedence study establishes “first.” An application-specific specification/audit and mechanism experiment may be contributions. HZ already uses traffic-updated route references; Gardner is classical; evidence of unique practical value is absent. D03:54–56,211–245. |
| A90 | 271: Schulz/Pfeiffer explicitly studied lexicographic vs weighted objectives | CANNOT CHECK | AG's line gives no primary pinpoint. D03 validates its deadline constraint, not that objective comparison. An attempted publisher DOI open failed; no invented confirmation. |
| A91 | 300–302:5/5 soundness, held-out snow/Nov16, zero leakage, sealed deterministic protocol | WRONG | Calendar separation is not untouched validation:dates/outcomes were already examined and PROTO is retrospective. Exact snapshot availability and vintage matching remain qualified. BG:358–362 says protocol unsealed/unrun; PROTO:28,36–40 discloses fitting/dependence. Ratings alone are subjective (A101 below). |
| A92 | 312–313,321: execute sealed R12; calibrate alpha,phi on Nov11–14 | WRONG | PROTO:28 fits alpha,beta,phi on Nov12/13 only,36 triples/80 targets; calibration quotations Nov14 are separate.11Nov15min factor is absent; changing the training vintage/parameters is a new protocol, not execution of this one. A supplied seal proving preregistration was not verified. |
| A93 | 314: snow8cells601 riders; Nov16w07/w08 holdout431 | AGREE | N:11 and SF reconstruct601; PROTO:36 names Nov16w07/w08 replicas1,2,4 and CX's prior forecast audit records431. These cohorts overlap dates/source trips;431 is not431 independent events. |
| A94 | 315: matching historical mean extension+13.7s for snow test | WRONG | N:11 reconstructs snow HIST extension1.975468738s as mean of8cells,1.928784329s pooled. OPT/FORECAST-REPORT.md:68's13.7s belongs to the21 active weekday cells. Match extensions within the stated cohort and weighting. |
| A95 | 317: snow baseline5.94%, target4.94%; weekday.17+.2=.37 | AGREE | Arithmetic is correct for those cell-mean rates. N:11:5.937271% snow cell mean versus34/601=5.657238% pooled. A hypothesis using those thresholds must keep its aggregation fixed.0.37% is a target, not a measured result. |
| A96 | 317–318:≥1pp improvement, kill<.5pp or early>5% | CANNOT CHECK | Design thresholds, not forecasts supported by the fit. They leave an intermediate .5–1pp zone and do not prove a general weather/gridlock mechanism. Same-vintage degenerate DT predicts no change (A83). |
| A97 | 318,321: failure establishes unforecastable shock/cannot be eliminated by quoting algorithms | WRONG | Failure of one fitted method establishes failure of that method under the given information/cohort. R17 snow prefix screens yield different residual decompositions; no information-theoretic impossibility. CX:305–309; R18-verification.txt:5. |
| A98 | 321: Nov15 genuinely zero-shot, no post-hoc framing | WRONG | Pre-event parameter-fit dates alone do not erase prior inspection of the test afternoon, method/threshold selection, or undelivered prefix data. Call it retrospective replay; future untouched multi-event/vintage data would be needed for stronger validation. PROTO:28,38–40; R17/R18. |

### Direction scores, consolidated table, predictions and closing roadmap

| ID | AG lines / claim | Verdict | Checked value, correction and anchor |
|---|---|---|---|
| A99 | 213–224: A1 itself produces an archival/publishable chapter and supplies operator value | CANNOT CHECK | A bounded synthesis is worthwhile; publishability and operator adoption cannot be certified from table construction. D03:236–245. Scope now includes the approved whole-thesis rewrite, not only a chapter. |
| A100 | 217: “100% verified” from458477 frames/227 transcripts | WRONG | CX:11–15 verifies the counts and an explicit set of checks. Hashes and reader agreement do not prove100% mathematical, causal, external-validity or reviewer soundness. Correct description:independent audit of227 transcripts/458477 decoded frames with the stated checks. |
| A101 | 214–220,259–265,297–303: six ratings per direction | CANNOT CHECK | Subjective scores: A1=(3,4,5,5,5,5), A2=(3,4,4,4,4,3), A3=(3,3,5,5,5,5), ordered novelty/significance/soundness/rigor/reproducibility/feasibility. The numbers are faithfully quoted; 5/5 for A3 is not an empirical certification and conflicts with A83/A91–98. |
| A102 | 220,250:14–20h writing;265,288:25–35h code;303,319:10–14h forecast | CANNOT CHECK | Time estimates, not observed timings. A whole70–79page rewrite is a different scope from the original A1 chapter. Do not commit to completion based on these estimates. |
| A103 | 223,268,306: A1 ACCEPT; A2 conditional ACCEPT; A3 excellent appendix ACCEPT | CANNOT CHECK | Review judgments. My recommendation:accept corrected synthesis and approved staged experiment; reject repeating the degenerate R12 method as a new confirmatory rescue. Preserve its negative diagnostic in the thesis. |
| A104 | 233: U table2434,203,8.34%,2231/3672=60.76%,2332 timely120,early.29%,extension0 | AGREE | N:8 / A:9:7 early;203/2434=8.340181%;2231/3672=60.757081%;7/2434=.287592%. |
| A105 | 234: U+fc2434,137,5.63%,2297=62.55%,2347,early.33%,+7.2s | AGREE | N:8:8 early,extension7.183331s;2297/3672=62.554466%. |
| A106 | 235: U+fc+30 counts2434/106/2328/2366,4.35%,63.40%,early44=1.81%,+37.2s | AGREE | N:8;2328/3672=63.398693%;106/2434=4.354971%;extension37.183331s. |
| A107 | 236: U+fc+60 counts2434/87/2347/2386,3.57%,63.92%,early1033=42.44%,+67.2s | AGREE | N:8:extension67.183331s;2347/3672=63.916122%;87/2434=3.574363%. |
| A108 | 237: C30 counts2338/76/2262/2327,3.25%,61.60%,early.13%,extension0 | AGREE | N:8:3 early,2262/3672=61.601307%;76/2338=3.250642%. |
| A109 | 238: C30+fc2338/10/2328/2338,.43%,63.40%,4 early=.17%,+7.4s | AGREE | Same checked values A22/N:8. |
| A110 | 239: Mplus2338/74/2264/2327,3.17%,61.66%,early.13%,extension0 | AGREE | N:8:3 early,74/2338=3.165098%;2264/3672=61.655773%. |
| A111 | 240: Mplus+fc2338/10/2328/2338,.43%,63.40%,4 early,.17%,+7.3s | AGREE | N:8:7.340496s extension. Arrival replay is measured; displayed-first-promise deadline compliance was not re-evaluated. Its “unreplayed” compliance columns correctly avoid inventing that result. |
| A112 | 233–240: U/C own compliance zero; Mplus41.3/14.5; percentages mix denominators | AGREE | Values checked in A20/A21. Label cell means versus pooled served-rate and common-request denominator explicitly. Forecast rows inherit archived dispatch; they are not newly forced-free operational experiments. |
| A113 | 244: U/C2207 common,227Uonly131Conly; C/M2332common6each | AGREE | N:9, A:18–19. Identity is keyed by cell and request. Same served totals do not mean the same riders or universal dominance. |
| A114 | 245: liability table thresholds1/2/5/10min | AGREE | V:115–121 proposes symbolic threshold sensitivity, not measured monetary loss. Include service, denominators and quote costs; no causal credit/retention claim follows. CX:227–247. |
| A115 | 248–249: exact±0 agreement prediction but kill only discrepancy>1 | WRONG | Numerically, ±0 means exact agreement; a1-rider discrepancy also requires resolution. Any mismatch in a deterministic count is an audit discrepancy, not acceptable sampling tolerance. New valid evidence must be reported, not suppressed to preserve old predictions. |
| A116 | 252,333: U-pad quote~5x,early rate~10x C;106vs10 late,96 more served | AGREE | N:8:37.183331/7.367123≈5.047;1.807724/.171086≈10.566. Ratios are approximate and denominators differ. U-pad has28 more timely120,2366vs2338. |
| A117 | 252,333: C protects brand; padding degrades trust/artificially inflates ratio | WRONG | Different quote sharpness is measured; brand/trust/retention utility is not. Padding is a disclosed valid frontier comparator. Do not call a transparently stated same-threshold count artificial. CX:177,236–245; D03:236–265. |
| A118 | 264–265,288:34 scenarios,6 workers,~3–4h runtime;74jobs | AGREE | Historical scaling basis exists:170jobs≈7h;74/170×7≈3.05h (CX:112; V:263–267). Actual rebuilt/cost-first runtime and25–35h development remain CANNOT CHECK. |
| A119 | 280–283:4OFF,2smoke,68main; OFF equality on2cells | AGREE | V:263–276 and approved Stage1b. OFF U/C30 × one w08 and one w17 gives4. Equality requires actions, final ledgers and relevant execution identity; failure must stop/report before main jobs. |
| A120 | 284: U-cf target≥32.8%,kill<25.8%; failure proves objective not lever | WRONG | +10pp/+3pp arithmetic is correct and V:277–278 indeed proposes it. These are unsupported discretionary targets. Missing one target does not prove invariance or no objective effect; report counts, interactions and service composition. R17/R18 replace the inference. |
| A121 | 285: Ccf≤4.25%late within1pp of3.25%;0forced | AGREE | As a proposed aggregate target, with3.25 rounded and its served denominator. It is not an existing result; preserve zero budget overshoots too (V:279–281). |
| A122 | 285: exceeding4.25% proves selector essential / cap alone insufficient | WRONG | It demonstrates the changed policy missed an aggregate threshold. Gates, traffic, recovery and differing served sets remain; no individual causal attribution or total-arrival guarantee is isolated. CX:225 explicitly replaces this inference. |
| A123 | 286:≥2315 within1% of2338 | AGREE | ceil(.99×2338)=2315. This is a chosen service guard, not predicted success. AG omits V:285–286's absolute shared-completion guard; current staged gates must govern instead. |
| A124 | 286: fewer served proves cost-first blocks later riders | WRONG | Lower aggregate service needs cell/request trajectories to diagnose. It may reflect a changed service allocation/search trajectory, not a universally proved blocking mechanism. |
| A125 | 287: cumulative-only target≥1 and zero kill | AGREE | A falsifiable recorded-witness hypothesis. Correct failed-hypothesis wording:zero observed records in these runs. It does not prove cumulative clause redundant under cost-first generally or that larger B would be inert. |
| A126 | 290: c≤B and worse pickups directly prove holistic objective value | WRONG | Use sum abs(c)≤B. Changed pickup distributions under matched treatments are informative, but practical holistic value needs a stated service preference and common outcomes; it is not directly proved by volatility alone. |
| A127 | 331 R1 defense: equal service establishes superior contractual integrity/causal mechanism | WRONG | Counts/compliance are supported (A19–21); own obligations differ. Say “C enforces its dispatch-budget contract while Mplus invokes exceptions under its deadline rule.” Do not equate own-rule breach rates with a common SLA or prove the causal mechanism from the equality. CX:207–225. |
| A128 | 332 R2: report0 recorded cumulative-only, but precise higher-load conditions required | WRONG | Reporting0 is correct (A32); theoretical guarantee remains. Higher load/cost-first/large B are candidate mechanisms, not necessary/sufficient empirically established conditions. A50–51; CX:189–206. |
| A129 | 334 R4: weekday small headroom justifies rejecting all weather ML | WRONG | Fixed weekday2/1471 is not a bound for incidents, quote sharpness, thresholds or new data. Scope the negative pilot and deadline decision; distinguish snow threshold counts from all weather (A23–24,A76–77). |
| A130 | 335 R5:203→76 late and134→4 “eliminates pooling-induced exposure” | WRONG |203/76 are naive late60 counts;134/4 are late AND dispatch-exposed intersections. Total exposed riders174/33, and repeated12/0 (AJ, N:8; CX:68,83). Four is not zero; the intersection is not identified pooling-caused lateness. |
| A131 | 335: A2 will prove hard cap alone maintains reliability | WRONG | The matched2×2 studies objective×cap interactions under the retained package, not a standalone cap guarantee on arrivals. Include common-request timeliness, rejections, served overlap and uncertainty; R18 Stage1b. |
| A132 | 342–348: eight mandatory CX correction groups; bullets cover six | AGREE | CX sections at189,207,227,249,267,281,299,315 are eight. Six bullets are a non-exhaustive subset; explicitly retain construct/thesis-adequacy and data/ML/novelty limits rather than claiming the list fully implements all eight. |
| A133 | 343–348: no measured cumulative performance, no more than Mplus, noROI, include30/60padding, no screen ceiling, no elapsedµs | AGREE | Correct restatements of CX's eight groups. AG's earlier prose violates several; they must apply to its own answers as well as the thesis. |
| A134 | 353: “0 Thesis Results Drafted” | WRONG | Existing thesis chapter4 contains results and a296-run table (ridebound/noi-dung/08-chuong4.tex:74–106,140 onward). Correct claim:current audited T38/Mplus/frontier and claim corrections are not fully integrated; existing text is stale/overclaiming. R18-verification.txt:14–15. |
| A135 | 354–366: deadline confirmation/A1 text before any study,7day time-box,week2A2/week3DT | WRONG | This earlier optional ordering is superseded by the owner's explicit Round19 approval and already-running Stage1a. Retain a writing time-box and gates; no renewed owner approval is required. Future DT is not a new viable repeat (A83). |
| A136 | 355: A4 fallback refinement0runs | AGREE | A writing-only fallback is feasible as a task type. No guarantee of thesis adequacy or completion time; source V and CX:3. |
| A137 | 357: diagram asks Gate0 only after “execute74runs” | WRONG | Gate0 must precede smoke/main; otherwise its stopping protection is meaningless. AG's prose280–283 has the correct order. Follow that order and the updated staged plan. |
| A138 | 361: week4–5 compile/supervisor/defense | CANNOT CHECK | Scheduling opinion conditional on an unconfirmed deadline and supervisor availability. No build was run this round. |
| A139 | 365–367: one results chapter/optional snow replay completes scientific task | WRONG | R17/R18 source audit requires a whole-thesis claim revision:abstract, theory, related work, methods, results and conclusion. A single chapter cannot fix inconsistent novelty/guarantee language elsewhere. Owner approved~70–79page rewrite; this round audits and prepares analysis only. |

The table covers factual claims, numerical values, source citations, hypotheses and score-based assertions throughout AG:1–371; repeated numbers are cross-referenced rather than counted as additional independent evidence. Direct quoted owner questions are treated as the supplied debate context, not newly verified measurements.

### What adds something new and correct

Antigravity adds **no independently established empirical result**:it was restricted to the input pack and supplies no new reader/output. Useful parts of its presentation are the explicit taxonomy, the concise three-direction comparison and its insistence on the two-sided quote frontier. These are correct organizational additions. Its pickup-volatility warning is useful as a proposed measurement, but was already implicit in the source hierarchy and prior objective-study discussion. The15+15+10s example correctly illustrates accumulation.

The most consequential corrections are:

1. A zero recorded cumulative-only count is not a proven per-step-equivalent counterfactual.
2. Keep own-rule compliance separate from actual-arrival lateness; there is no30s dispatch-ledger guarantee on total arrival error.
3. Treat cost-first sharing/service/wait changes as hypotheses. The≥+10pp expectation has no objective-only evidentiary basis, and AG alternates between U and C as its target.
4. The R12 parameter fit already selects the historical-equivalent adaptation; do not sell its repetition as a fresh fair rescue. A different future method/vintage/event set would be a new study.
5. Correct the2013 weather impossibility, snow-event denominator,13.7s cohort, commercial claims and “0 results drafted.”

My own earlier errors remain withdrawn:the≥1pp proportional-policy benefit is not an evidence-backed expectation; sparse screens are not impossibility bounds; evaluator speed is unprofiled; a missing Mplus(b) baseline was a mistaken premise because T38 already uses recovery(b). No old proposal is revived by Antigravity's agreement. R17/R18 supersede my earlier experiment-first sequencing.

## 2. Independent audit of running Stage 1a

**Design judgment: ACCEPT WITH QUALIFICATIONS.** This is the approved configuration-only stable-C120 step. It preserves the archived execution path rather than rebuilding a different runner. It does not answer the objective interaction or cumulative-versus-per-step question by itself.

| Check | Verdict | Verified evidence |
|---|---|---|
| Plan content seal | AGREE | N:2:actual and expected SHA256 both `cb6da66288b6d3b4a96271b27fc7047843c4e35f260f02ce4c559672bc6fd046`. The plan bytes currently match the seal. |
| Prior-to-first-job sealing | CANNOT CHECK | Plan:3 says~22:20; filesystem plan mtime15:12:26.317043Z and seal15:12:47.815085Z correspond to22:12 local. Brief says launched22:12; no second-resolved launch provenance was checked. The heading is inconsistent with its mtime. A matching SHA does not timestamp execution or independently prove pre-job sealing. Do not retroactively alter the sealed plan. |
| Driver's effective changes | AGREE | T/t38c120/run_t38c120.py:23–27 sets PHASES(c120,C120,unchanged test tuple), adds C120 config hash, changes OUT_ROOT,LOG_ROOT,STOP_FILE; adds a seal guard before run. It calls unchanged imported t.main(). No selection/world/seed/cwd override. |
| Parent driver unchanged relative to an archived source version | CANNOT CHECK | The current parent is reused and hashed in NJ.inputs. Read-only git status lists these driver files as untracked, so HEAD cannot certify byte equality to the historical launch. Runner/config/fixtures are independently matched below. This limitation is not evidence that the parent was changed. |
| C30→C120 sole config difference | AGREE | N:3:only `/policies/0/limits/1/hardLimit`,30000→120000. C120 file SHA `ac0f97589427919c5175e9cc952849305702ced45313a5a2db88167dff030520`; C30 `d6124f3f964d8385db381d53b75c142cf2ac870b22823d6675325c3808808beb`. |
| Same34 test cells | AGREE | Split SHA `b72ac0f731fa7425891f364f0976054ae172a3117a507155ebe7e5c122ea03f1`; N:6 independently validates all34 unique keys,108requests each,total3672. Windows:9w07,14w08,11w17. |
| Runner v2 | AGREE | Independently recomputed429-file tree hash `ac251ef32a4865ea3bd3d8d87b4b1bcaccc4462a9b80160b4d205b8d474cff3f` (N:5), equals run_w07.py's declared tree. Later source HEAD is irrelevant to this unchanged archived binary; no new build or OFF gate is needed for Stage1a alone. |
| WP4v2 / recovery(b) | AGREE | N:4:WP4 SHA `66e9b59249d9491d520f3ed592e8c878a0d3b100e39432d5f4b73321617b4518`; policy hard-vector,booking-confirmation,no-worse-than-reference-v1,lateBoarding record-v1,seed7,retention service-set-stability-portfolio-v1,max100candidates/max2new. Mplus(b) was already in T38, not an absent baseline (R17:5; R18-verification.txt:17). |
| World wrapper v1.2 | AGREE | T/w07/run_w07.py:40 and T/t38/run_t38.py command use the same PREFLIGHT. Wrapper independently guards measured day/window. All34 worlds are sigma=shockRate=0,exponent1 and match scenario local dates/windows (NJ.fixtures). WorldSeed101 is separate from master/solver seed7. |
| Fixtures/drivers | AGREE | Read all34 source scenarios, derivative manifests, normalization reports, selection frames and drivers; driver-declared source SHA matches each scenario.8vehicles/108requests/96nodes/9120directed arcs per scenario; correct America/New_York windows (NJ.fixtures.details). This is the archived panel, not a new sample. |
| Master seed / repeats / workers | AGREE | Parent command explicitly --master-seed7,--repeats1; imported run_pilot.WORKERS=6 and WP4solver seed7. Identical seed does not turn the34 dependent cells into independent replications. |
| Cwd and inventory | AGREE on declared command | Parent subprocess uses run_pilot.REPO=`E:/Code/RideBound-deadline`; command passes inventory `0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe`. I did not access/modify that repository. The future analyzer checks each completed summary's reported inventory; actual process cwd was not independently inspected. |
| Output/log/STOP isolation | AGREE | C120 root `C:/RideBoundData/research/tier3-t38c120-v1`; own log root and STOP. Existing output/log state is skipped, logs use mode x. No output, STOP, log, process or power setting was changed by this audit. |
| AC-only claim | AGREE with qualification | Parent uses may_start_job and power waits; run_pilot.py:75 onward allows an owner-set RB_ALLOW_BATTERY_MIN_PERCENT override. Without checking that environment, “unconditional AC only” is not proved. No process/environment inspection or alteration was performed. |
| c120 phase and gamma | AGREE | Parent gamma requirement applies only to phase=="test"; the new phase is"c120". C-only120 has no fitted V-threshold, so this bypass does not change the treatment. The inherited w07 input checks still add dependencies, not a different objective. |
| R17/R18 staging | AGREE |34stableC120 runs are Stage1a; Stage1b is OFF4+ON2+CFU/CFC30×34=74. Stage2 cumulative120/per-step120×34+ON2+OFF2=72 only after its gates. Owner approval already exists; no new simulation was launched here. |

### Predicates fixed before outcome analysis

The sealed numbers remain unchanged. The following are extraction definitions, not tuning:

| Prediction | Executable predicate | Interpretation |
|---|---|---|
| P1 | all34 completed summaries pass AND zero acknowledged certificate.body.normalOperation=false AND zero final served-ledger absolute-drop-spend>120000ms | Technical summary pass is distinct from service success. Incident breach entries are counted separately from decisions. The data-quality gate refuses a failed/incomplete run; a failed summary is reported as a P1/data-quality failure, not silently replaced. |
| P2 | totalserved≥2362 | A net gain≥24 over2338,25% of the96-count gap. It does not identify24 particular C30-rejected riders rescued; served-overlap output supplies identity changes. |
| P3 |76<naive late60<203, integers77..202 | Strict inequality; compare actual passengerAlighted time against the first acknowledged initialPromise drop ETA. No latest-quote substitution. |
| P4 | naive timely120=served−naive late120≥2327 | Plan:20–21 gives naive comparators, so this is the predeclared interpretation of its unlabeled P4. Also report the separately labeled causal-no15 result; do not change the primary to forecast afterward. |
| P5 | total recorded cumulative-only drop-budget prune records≤2 | Candidate-record count, not decisions/new riders/final rejections. Each reported drop witness has after=before+delta>limit with delta≤limit and before>0; records with any reported single increment>limit are step failures. Missing/other/unclassifiable budget evidence makes the predicate unverifiable instead of silently counting0. |

All five are well-defined under those definitions. They are hypotheses/design targets, not findings derived from the C30 screen. P2/P3/P4 need no assumed monotone trajectory or matching served set. P5 is deliberately about the **recorded** fail-fast evidence, not a theorem about all candidate blockers.

The archived baselines independently retained by N:8 are U2434/C302338; naive late60/120/300 U203/102/18,C76/11/0; timely60/120 U2231/2332,C2262/2327. Forecast replay U137/87/17 late,C10/0/0; timely U2297/2347,C2328/2338. These numbers define comparisons; the current C120 outcome has not been inferred from them.

## 3. Independent analysis script and readiness

Use **`R19-stage1a-analyze-v3.py`**. The earlier versions are preserved; v2 pins all three historical factor SHA256 values and v3 also checks each arm's exact canonical commitment/WP4 binding. None of the three analysis mains was run.

The future invocation, **only after all34 runs complete**, is:

```powershell
& 'E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe' -B './R19-stage1a-analyze-v3.py'
```

No runner/simulation command is contained in this script. It imports only Python standard-library modules, processes one run at a time, and writes only mode-x `R19-stage1a-analysis.json` and `R19-stage1a-analysis.md` beside itself. Existing result files cause refusal; incomplete inputs create no analysis output. It never writes to the input/output research roots.

Its execution order is:

1. Verify the fixed split and check **all34** C120 summary/run/transcript artifacts before extracting any outcome. Require pass,one repeat and nonempty artifacts. Missing/failed/incomplete evidence stops analysis; it does not run a partial frontier or wait/control jobs.
2. Match the seal and recorded source hashes, runner/config/world/fixture inputs. Hash each completed transcript, each decoded frame and its byte length; require increasing ordinals and exact decision/acknowledgement identity equality. Refuse input files that change during the read.
3. Validate expected binary/core/seed/policy/version, source fixture and reported repository inventory. Preserve each manifest, including its canonical policyConfigurationHash; require the exact independently derived arm binding and consistency across C120 runs. The C120 binding is `a9ac58b33558c6ec2d604ee7fe3e7fdb02deaecfd866ea73282b911326ed9010`. This is SHA256 of the domain bytes plus canonical commitment/WP4 digest bytes, not the whitespace-sensitive config-file SHA (SRC/RideBound.Contracts/Protocol/Wp4PolicyConfigurationBinding.cs:18–42; `R19-config-binding-check.json`). The derivation reproduces both archived U/C30 initialize hashes.
4. Recover final completed/rejected state and physical alights. Require108 terminal requests per run, equality of completed/alighted/ledger sets and acknowledged publication identity/projection consistency. Read each first initialPromise timestamp and ETA from publishedPromise, not a nonexistent top-level timestamp.
5. Recompute signed p−e for each revision, absolute deltas and cumulative before/after spend; report budget overshoots rather than assert them away. Count drop-exposed riders and riders with≥2 nonzero changes; keep typed incident entries separate from non-normal certificates.
6. Recompute late>60/120/300 and timely≤60/120 relative to first quotes. For forecast use an independently implemented piecewise inverse-work integration with causal-no15 sources:14←12/13;15/16←12/13/14;weekend17/18 inactive. Current-bin multiplier1,mean historical growth thereafter,hold from bin8,one-sided max(original,stretched). No future scenario factor, arrival or vehicle state enters a quote.
7. Re-read the34 archived C30 and34U transcripts, compare their full-file SHA256 values with the prior independent inventory, verify known baseline frontier and2207-common/131C-only/227U-only overlap. Compute C120/C30 and C120/U overlaps with(cell,request) keys. This is independent extraction, not importing Claude's analysis readers.
8. Classify only acknowledged drop-budget prune records and preserve cumulative witnesses, decision IDs, candidate IDs,new requests and final lifecycle association. Export per-run and per-rider evidence, pooled counts, common-request rates, quote extension/early arrivals, exact predictions and input hashes.

The source does not assert zero budget spend overshoots or zero forced decisions before measuring them; either can fail P1. “Cumulative-only” remains a reported-witness classification. Another hidden fail-fast blocker or later trajectory change is not ruled out.

### Checks actually performed

`R19-check-analyzer.py` parses/compiles the whole v2 source **without executing/importing it**, then extracts only its forecast and completion-gate functions from the AST. Synthetic completion metadata verifies a full34-run gate and refusal for a missing summary,failed summary,two repeats,empty transcript and missing run artifact. No C120 data is read by these checks.

The forecast was checked against an independently implemented inverse-integral oracle using bisection:300 cases across all five scenario days,three windows,bin boundaries,zero/positive duration and drain behavior. Maximum difference was1.862645149230957e−9ms; all checks passed (`R19-analyzer-checks.json`). These are numerical/unit checks, not traffic simulations.

A separate schema compatibility probe on **one archived C30 baseline** confirms acknowledgement identities, boolean certificates, prune collection, completed/alighted/ledger set equality, acknowledged promise projections and absolute/cumulative ledger fields (`R19-schema-check.json`). It does not execute the Stage1a analyzer or read C120 outcomes. V3's full source was also syntax-compiled without execution. AST comparison proves its forecast and completion-gate functions are identical to the tested v2 functions; the added binding check was independently derived and matched to archived U/C30 initialize metadata (`R19-config-binding-check.json`). The complete102-run pipeline therefore remains unexecuted; syntax/isolated checks do not pretend to be a completed raw C120 audit.

### Completion status and pending results

At N:13–14's first recorded check,2026-10-10T15:20:06.948840Z(22:20 local), six directories existed without summaries and28 were absent. At the later read-only check, **2026-10-10T15:34:29.7625654Z(22:34 local),5 summaries passed,6 directories had no summary and23 directories were absent** (`R19-final-completion-gate.json`).

Thus not all34 completed runs exist. No partial C120 service/reliability/prune outcome was extracted, and the independent analysis was **not run**. P1–P5 and C120 overlap/forecast results remain pending. The five passing summaries alone do not settle any full-panel prediction. This is a completed audit/preparation deliverable, not a claim that the ongoing experiment has finished.

## 4. What should enter the approved rewrite

The rewrite should present a bounded specification/implementation/audit and a service–arrival–quote frontier. Retain Mplus as a central comparator with recovery(b) already enabled; show both30s and60s U padding. Explain that the cause-separated ledger charges model dispatch changes while traffic/execution residuals can still cause lateness. Report zero **recorded** cumulative-only measured-C prunes in the prior sample and distinguish sparse fixed/synthetic witnesses from demonstrated service benefit.

Integrate Stage1a as its sealed hypotheses and pending/observed results without retroactive retuning. Stage1b tests the matched objective×cap interaction; the current cost-first expectation is not≥+10pp sharing. A failed service/arrival guard is a changed-policy outcome, not proof of global impossibility. Stage2 directly tests cumulative versus per-step at120 only after its gates and fresh OFF checks.

Document R12's degenerate fit as a negative diagnostic, not an unrun “excellent” rescue promised for week3. A future multi-event,delivery-vintage-correct forecast comparison can remain future work. Correct novelty, real-world causal identification, institutional acceptance, ROI/retention and total-arrival guarantee language throughout the thesis. Do not erase existing results by saying none were drafted.

## Files and preservation

| File | Purpose / state |
|---|---|
| `R19-CODEX.md` | This139-row claim/citation review, design audit and analysis readiness report. |
| `R19-stage1a-analyze-v3.py` | Preferred independent full-panel analyzer; factor pins and exact arm binding checks; prepared,syntax/function-checked,not executed. |
| `R19-stage1a-analyze-v2.py` | Preserved intermediate analyzer with factor hash pins; isolated functions checked,analysis main not executed. |
| `R19-stage1a-analyze.py` | Initial analyzer version; preserved,not executed; superseded by v2's factor hash pins. |
| `R19-check-analyzer.py`, `R19-analyzer-checks.json` | Successful isolated syntax/forecast/completion-gate checks. |
| `R19-schema-check.json` | Successful schema check on one archived C30 transcript. |
| `R19-config-binding-check.json` | Independent canonical binding calculation, archived U/C30 matches, v3 syntax and tested-function AST identity. |
| `R19-verify-v3.py`, `R19-verification.json`, `R19-verification.txt` | Successful independent provenance/design checks and existing-audit arithmetic. |
| `R19-verify.py`, `R19-verify-v2.py` | Preserved failed attempts; first looked for BG at an unverified original path,second encountered seven-digit ISO fraction parsing. Neither produced verification outputs. V3 handles the copied BG as supplied and parses the scenario's19-character timestamp prefix. |
| `R19-final-completion-gate.json` | Later read-only34-cell completeness snapshot. |

All creation used CreateNew/mode x; no existing file was overwritten or deleted. No study approval was requested again. All required work for this round's audit/preparation is delivered; full Stage1a outcome analysis is correctly deferred until the required runs complete.
