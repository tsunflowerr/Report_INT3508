# Round 17 — Codex cross-rebuttal and converged recommendation

2026-10-10. **My single recommended next step is a whole-thesis claim-and-results revision, with zero new simulation jobs.** I concede Claude reviewer's sequencing after checking the actual LaTeX and the new diagnostics. The optional research extension is a matched objective × cap study that includes a direct cumulative-versus-per-step comparison at 120 s. A multi-event forecast benchmark ranks third, as future work. This changes my R16 execution ranking; it does not turn the present evidence into an acceptable top-venue submission.

The strongest new correction to Claude is factual: **T3.8 already uses recovery (b)**. Its 34 M⁺-30 terminal ledgers contain **154 forcedNoWorse breach entries**. These are breach entries, not 154 decisions. A proposal to add the same M⁺(b) configuration as a missing 34-cell baseline is redundant (META:8; driver/config anchors below). A literal always-relaxed Hörl–Zwick deadline would be a distinct implementation and must be described as such.

## Scope and verification

I read all three permitted Claude R16 reports, their relevant scripts/outputs, ROUND16-REVIEW-STANDARD.md and my R16. The named Antigravity file **was absent when checked**; there is no Antigravity claim to evaluate. I did not read Claude R17 outputs, spawn agents, run simulations, build, install, delete, or change an existing file. All new files were exclusive-created inside codex-work. At most two Python computations ran concurrently.

Evidence labels: **M** = measured archived simulated execution; **S** = screen on recorded states/paths; **A** = arithmetic; **I** = inference; **H** = hypothesis; **O** = review/design judgment. “Measured traffic” means simulation using taxi-derived city-wide factors, not an observational experiment on a deployed operator.

The portfolio audit re-executes Claude's inspected selector implementation in one process over all 80 WP14r files. This is **audited-code reproduction**, not a second independent full-selector implementation. I additionally exhaustively enumerate the five feasible fleet combinations in the anomalous C-30 case and derive its two rider movements directly from schedules. The request/screen reader and R12 fit are independent implementations. The snow extraction independently reconstructs ledger/physical alighting inputs, while reusing the inspected forecast functions/integrator. It reads 98 measured C transcripts plus eight snow transcripts, verifies **209,056 decoded frame hashes**, and verifies measured input file hashes against my earlier inventory (SF:33; helper). The metadata audit verifies terminal checkpoint hashes in 34 M⁺ transcripts; it does not repeat their previously completed whole-file audit.

Two initial helpers failed before producing outputs: one used the wrong ancestor for the sweep tables; the other used a tail too short to contain the large terminal checkpoint. Both are preserved, with corrected v2 helpers. Only successful outputs support claims here. One exploratory process-inventory command was denied; it supplies no evidence.

Paths below are relative to optimize/codex-debate unless absolute.

| Key | File |
|---|---|
| CE / CFc / CR | claude-work/R16-EVIDENCE-CLAUDE.md / R16-FORECAST-CLAUDE.md / R16-REVIEWER-CLAUDE.md |
| E / F | claude-work/r16-evidence/ / claude-work/r16-forecast/ |
| PV / CASE | codex-work/R17-portfolio-verification.txt / R17-C30-sum-case.txt |
| SF / SFJ | codex-work/R17-screen-forecast-verification.txt / R17-screen-forecast-verification.json |
| META / SIZE | codex-work/R17-metadata-verification.txt / R17-data-size-verification.txt |
| A15 / CAP / WX | codex-work/R15-audit-summary.txt / R16-cap-outcomes.txt / R16-weather-inventory.txt |
| R16 / SCOPE | codex-work/R16-CODEX.md / R16-scope-inventory.txt |
| HZ | claude-work/pdf/hoerl-zwick-2022.txt |
| TEX | E:/Code/Report_INT3508/ridebound/noi-dung/ |
| SCRATCH | E:/Code/Report_INT3508/ridebound-scratchpad/ |
| SEL | C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs |
| LOCK / VALID | C:/Code/RideBound-noworse/src/RideBound.Domain/Commitments/CommitmentLockEvaluator.cs / RideBound.Application/Commitments/CommitmentDecisionValidator.cs |
| D03 | E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md |

## Verification table and verdicts on the disputed evidence

ACCEPT below always means the stated narrow observation or diagnostic. It does not endorse an untested policy effect.

| Claim | Check and result | Verdict |
|---|---|---|
| All WP14r archived selections reproduce, 62,837/62,837 | Re-executed all five arms: 12,663 + 12,525 + 12,364 + 12,325 + 12,960 matches, zero mismatches (PV:2–6). Source hierarchy agrees with SEL:271–331,365–385. | ACCEPT, S reconstruction. |
| U-gated cost-first changes 445 decisions, 26.0%, saves 7.8%, median extra 90.8 s | 445/1,714 = 25.963%; conditional mean saving 7.7902%; extra fleet-sum upper-median 90.819 s. Acceptance count never changes at these fixed states (PV:2). | ACCEPT with denominator, conditioning and fleet-sum qualifications. |
| C-30-gated changes 104, 6.1%, maximum 35.5 s | 104/1,715 = 6.064%; maximum extra fleet sum 35.540 s. Exhaustive enumeration matches both original and cost-first choices (PV:5,7; CASE:1 onward). | ACCEPT; no per-rider cap violation. |
| FREE has 401 promise-changing decisions; at most 76 break counted LOCKS gates | Reproduction: 76 pre-boarding pickup changes, 325 drop-only decisions, no vehicle/stop switches; LOCKS control has zero counted gate changes (PV:8–9). | ACCEPT as this classifier's path-local decomposition, not an isolated policy treatment effect. |
| 1,256 prunes correspond to 973 request–run pairs, 807 served anyway | Independent reader: 971 decisions, 973 pairs, completed807/rejected166; T3.8 alone643 pairs,495 completed,148 rejected (SF:2–11). | ACCEPT, M. |
| Larger-cap screen: B60/120/300 pass11/59/135; late60 costs5/51/123, late1200/6/79 | Independent arithmetic reproduces those values (SF:12,14,18). They count witness crossing occurrences from separate candidate screens, not jointly simulated acceptances or automatically distinct harmed riders. At B120,59 occurrences involve58 distinct blocking rider–run pairs; at B300,135 involve123 (same anchors). | ACCEPT arithmetic; MAJOR REVISION for policy/rider-cost interpretation. |
| w07 B120 gains17, loses11 | Independent terminal-lifecycle join reproduces17/11 (SF:26); six of those17 gains were screen-predicted (E/q2-screen-identity-w07-2026-10-10.txt:5). My R16 independently measured666 vs660 served (CAP:4,7). | ACCEPT, M; weak screen calibration. |
| Snow ledger: about26% further “knowable”,67% “not knowable” | Independently reproduced total3445.933s, dispatch8.566s, HIST explained251.496s, prefix blend1138.355s. Increment886.858s =25.736%; residual2299.012s =66.717% (SF:29). | ACCEPT numbers; REJECT the information-theoretic interpretation. |
| Snow late34→19 under regime gate,34→29 with latency | Reproduced HIST34, gate1.3/prefix blend19, BLEND-L1 29, strict in-window blend21; extension cell means1.975/9.498/8.991/8.481s (SF:28). | ACCEPT exploratory replay; latency/gate wording must change. |
| R12 fit α1/β0/φ.8 gives null | Independent36-triple fit,80 one-step targets: SSE0.0118126096, triple(1,0,.8), exactly matches inspected fit (SF:27). Algebra below gives DT=HIST12 under R12's fixed vintage. | ACCEPT; withdraw running that protocol as a promising test. |
| NOAA snow starts13:44 | First Nov15 Central Park present-weather row containing SN is13:44 (SF:30; F/noaa-lcd-centralpark-2018-11-15-16.csv). | ACCEPT as first snow report at this station in this saved file, not exact city-wide onset or data delivery time. |
| Official2013 parquet has zones, no coordinates | Fresh closed-range footer reads reproduce Jan/Nov schemas and14,776,617/14,388,451 rows; zone IDs, no lat/lon (META:2–3). | ACCEPT for the two inspected current official files; full-year row quality remains unverified. |
| Data sizes | Fresh44 HEAD requests give5,354,364,554bytes =5.354GB for2016-07…2020-02 (SIZE:2). Saved earlier-year metadata sums given below (SF:31). | ACCEPT metadata arithmetic, not bulk-download/pipeline certification. |
| HZ eq7 is prior for the traffic-updated reference | Read HZ:529–543,567–606: max(updated,latest), routing constraints and original-deadline penalties. | ACCEPT; it defeats originality of that reference alone. |
| Thesis never cites HZ | Search all11 TEX files for author names, title and repository identifier returns no matches (META:4,6); bibliography inspected. | ACCEPT for the current scanned thesis sources. |
| Recovery(b) equals C service in21/22 | Recompute saved treatment tables: (b)1874,(a)1864,C1873,21/22 equal (META:7; SF:32; TEX/08-chuong4.tex:1361–1362). | ACCEPT table-level reproduction; 19/22 action identity is reported, not independently recomputed this round. |
| M⁺(b) is missing from T3.8 | Driver says(b) for every arm; wp4 config selects it;34 M⁺-30 checkpoints contain154 forcedNoWorse entries and one policy hash (META:8; SCRATCH/tang3/t38/run_t38.py:10–12,99–114; tang3/w07/run_w07.py:44–48; tang3/configs/wp4-tier3-v2.json:7). | REJECT. A literal HZ-style rule is a different proposed arm. |

## Q1 and Q4 — What the objective evidence changes

**Concede:** CE supplies substantially better evidence than the FREE/LOCKS package comparison alone. The fixed-state selector reproduces perfectly; under U gates dropping stability levels changes about a quarter of new-request decisions, while under C30 only about6% change. This strengthens the reason to test objective × cap, but lowers my confidence that **C30** alone will produce a large service/sharing improvement (PV:2,5). My R16≥10% absolute shared-completion target remains an optional decision threshold, not an estimate warranted by these screens.

**The 35.54-second case is fully explained.** In WP14r Nov13/r4/w17, decision hash1db8297a…f35826, the recorded fleet plan has zero incumbent drop movement; the cost-first plan has35,540ms. Two incumbents each move **17,770ms**, from6,373,237→6,391,007 and6,477,873→6,495,643. Their sums match the objective contribution. Five feasible fleet combinations exhaustively reproduce both choices (PV:7; CASE). B limits each rider's cumulative absolute movement; the selection objective sums movement across riders. “Each push≤35.5s” must read “each changed decision's additional aggregate incumbent movement≤35.5s.” It is not evidence that a rider exceeds30s.

**The cost percentage needs its conditioning.** The7.79% U result is mean relative saving **only where the selection differs**. Summed cost reductions divided by repeated selected-plan-cost totals across all acknowledged frames are0.3069% for U and0.0794% for C30 (PV:2,5; E/q4-cost-first-reselect-2026-10-10.txt:8,35). Remaining-plan costs are counted repeatedly through time; neither percentage is realized operating-cost saving, vehicle-km reduction, revenue or profit. My optional study must measure realized fleet work/cost consistently before making an operator-benefit claim.

**FREE/LOCKS decomposition:**325/401 =81.05% of promise-changing FREE decisions have only counted drop changes; their33,555.398s are69.17% of FREE's48,508.879 drop seconds (A fromPV:8). This is strong evidence that ranking can explain much of the local difference. It does **not** identify81% of the actual service, lateness or pooling gap as caused by ranking. The classifier is not a complete counterfactual gate run, its pre-boarding check overcounts potential pickup locks before WaitingPickup, and the paths already differ (LOCK:42–58,72; CE:383–400). “Mostly ranking” is a plausible mechanism inference, not a measured decomposition of final outcomes. Preserve my R16 package-confounding warning.

**Concede on thesis priority:** the actual abstract/introduction/conclusion still sell broad novelty and exclusive no-empty-set claims (TEX/02-tom-tat.tex:17–26,66–76; 05-chuong1.tex:64–69,169–182; 09-chuong5.tex:18–32,224–231). HZ was already known to my review; what I underweighted was the unfinished thesis's exposure to this prior and the required cross-chapter rewrite. A new experiment cannot repair those claims by itself. This justifies reversing my R16 immediate ordering, while retaining objective × cap as the best **optional research extension** (O).

Do not accept “only A2′ could produce any non-definitional result” as a theorem. A fair forecast or load comparison could produce an empirical result too. A2′ is the most relevant bounded mechanism test here, given the existing controls and missing trajectory comparisons (R16, proposed directions; CR:359–456). None guarantees top-venue acceptance.

## Q2 and Q3 — Cap value and accumulation

**Concede all verified measured ladders.** My R16 naive w07 totals match Claude: C30→U gives+5 served,+3 late60,+7 late120; C30→C120 gives+6 served,+4 late60,+5 late120,+2 timely60,+1 timely120 (CAP:3–7). These are eight Nov12/13 morning cells, outside the Nov14–18 main panel. Claude's w07 forecast columns deliberately use noncausal loo-no15; my primary-causal forecast remains inactive there. They do not disagree numerically when the information rule is held fixed (CE:78–80; R16 scope; SCRATCH/optimize/display_layer.py:10–16).

The fixed WP14r ladder remains C30/60/120 service1534/1540/1563, late60 0/0/23; C60→C120 adds23 served and23 late60, but no late120 (A15:3–5; CE:145–154). The T3.8 C60/C120 stable trajectories are still missing; the screen is a reason to measure them, not a substitute.

**The973/807 result is useful.** 807/973 =82.94% of touched request–run pairs complete in their original run. Candidate prunes are not lost customers, and repeated requests across arms are not independent people. The148 T3.8 rejected requests carrying a budget-pruned candidate are a path-specific category. “Structural-only” means no such recorded budget candidate for the rejected request; it does not prove that a larger-cap trajectory could never serve it (SF:2,11; E/q2_budget_screen.py docstring; R15 correction4).

**The co-rider screen is deliberately incomplete.** It tests reported after≤B and adds the positive budget delta to the co-rider's realized C30 lateness. The source explicitly acknowledges fail-fast omitted riders; VALID:222–239 confirms that only the first failing request/layer need be reported. Thus passing all *reported* witnesses is not certifying candidate eligibility. Separate hypothetical acceptances also cannot be combined into one fleet trajectory. Counts5/51/123 and0/6/79 are reproduced **crossing occurrences**, not a jointly realized service-versus-harm frontier (SF:12,14,18). The duplicate blocking rider–run pairs at B120/B300 reinforce that distinction. Addition of an absolute movement to lateness also assumes a later push; without signed candidate projections it is a screen convention, not a general identity (E/q2_budget_screen.py:docstring and base/new calculation).

The w07 check has six screen-predicted additions at120s, **17 actual additions and11 losses**. A coincident net+6 conceals11 unpredicted gains and11 losses; prediction of net counts does not validate individual-level policy outcomes. Its+1 timely120 against screen arithmetic+3 is further warning (SF:21,26; E/q2-screen-identity-w07-2026-10-10.txt:5; CAP:4,7). In particular2327+59−6=2380 is arithmetic over incompatible marginal screens, **not a policy estimate or bound**. CE marks it arithmetic; I would omit it from a headline frontier.

**Reject CR's “at most96 recovered” bound.** The96 is the current U-minus-C30 aggregate gap, not a global optimum or a bound for every finite B. On the independently measured w07 paths, C120 serves666 while U serves665 (CAP:3,7). Changing feasible alternatives changes later states; broader action sets under a local objective do not guarantee monotonic terminal throughput. Likewise no finite B is proven “essentially U” by inspecting old U spending or old C30 witnesses alone (CR:487–496). My R16 monotonicity warning survives.

**Accumulation:** agree that no recorded measured budget failure required prior spending. Keep the exact statement in R15:195–197. Reject “behaviourally inert” or “never changed a decision” as a proven policy equivalence: a counterfactual per-step trajectory was not run, and fail-fast witnesses do not describe all otherwise-feasible candidates. Recorded possible cumulative witnesses in four fixed decisions plus three distinct synthetic decisions are not a global seven-decision bound, nor evidence that accumulation caused one rejection (A15:3–6; R15:195–197). CR:501–503 repeats those overclaims.

CE's repeated-change and exposure tables support a **hypothesis** that cost-first and B≈120 increase opportunity for accumulation, not “it would matter only” in that range (CE:230–288,293–299). The archived cost-first exposure screens at120s have roughly7–10 cumulative-only exposed riders per1000 (CE:246–257; its saved MC output is inspected, not independently recomputed here); the enforced policy may prevent early changes and eliminate those later states. Do not predict “≥3 prunes per1000 served” by equating candidate records with riders. Count distinct affected decisions and rider–run pairs separately, and use the direct per-step comparison before claiming outcome value.

## Q5 — What the snow replay proves and does not prove

**Concede the damped-trend null; change my proposal.** My independent fit findsα=1,β=0,φ=.8 on the prescribed80 targets. Starting v=0, β=0 leaves v=0; α=1 gives l=r_current. The future residual correction exp(l−r_current) is1, so the fitted R12 method equals its fixed Nov12/13 historical profile (SF:27; codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md:17–30; F/factor_nowcast_screen.py:dt_filter,fit_dt,method_weight). Phi is selected by the tie rule, not identified evidence for0.8. **Beta0 alone would not imply this for alpha<1.** Also R12's HIST12 is not the expanding three-source causal-no15 profile for Nov15/16; Claude's DT-on-HIST screen equals that screen's HIST because both use the same profile. I withdraw running the old protocol as a promising new forecast experiment and do not tune it on snow to evade the null.

**Concede the replay numbers; reject the availability labels.** On601 saved snow journeys, HIST has34 late60, strict in-window BLEND21, prefix BLEND/gate19, lagged-trend BLEND29 (SF:28). The late percentages in Claude's table are **cell means**:34/601 is5.66%, whereas the reported5.94% is the average of eight cell rates. Do not mix denominators. All are first-quote replays on existing physical outcomes; no dispatch trajectory or acceptance decision changes.

Using the41 naive-late riders, prefix BLEND/gate adds886.858 explained seconds above HIST,25.736% of3445.933; strict in-window BLEND adds821.367s,23.836%; lagged-trend BLEND adds273.471s,7.936%. Prefix residual is2299.012s,66.717% (A fromSF:29). These are **method-dependent retrospective explained/residual quantities**. They are not a maximal predictable component, a lower bound on irreducible uncertainty, or an identified weather-vs-unknowable decomposition. More accurate methods, other prefix features or simply longer quotes can change them. The explanation clips against observed lateness and examines a cohort selected by realized naive lateness. It is diagnostic, not a common-cost causal attribution study.

The19-rider result uses same-day factors from06:00 and an absolute f/m gate; the Runner's14/15h windows did not deliver that morning prefix. The strict in-window result is21. Threshold1.3 was selected after seeing separation1.244/1.323 (CFc:49–51,186–189; F/factor_nowcast_screen.py information rules; F/factor_nowcast_screen_v2.py:weight). Thus “26% knowable from delivered snapshots” combines an expanded information set with post-hoc tuning. Use “this retrospective prefix model explains about26% more of the naive-late cohort's seconds” instead.

**29 is not a full realistic-latency experiment.** The reproduced29 comes from BLEND-L1, not an independently evaluated “regime gate with one-bin latency” arm. Its trend uses k0−1/k0−2, but the anchor and naive remaining ETA still use the **exact current simulator snapshot**. REGB has no L1 branch in the inspected implementation (F/factor_nowcast_screen.py information rules and method_weight; F/factor_nowcast_screen_v2.py:weight; SF:28). Moreover a bin constructed from completed durations of trips starting in b is not necessarily finalized after one bin, or even two. A fixed lag alone is no proof of causality. A realistic benchmark needs per-trip completion plus assumed/observed delivery times, and weather issue/availability times, as specified in my R16 Q5. Its live feed is an explicit deployment assumption; the [TLC archive](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) publishes monthly with a typical two-month delay.

**NOAA and “unpredictable.”** Central Park's first saved snow report at13:44 is verified; LCD times are local standard time (SF:30; F/noaa_lcd_documentation.txt:10). It supports a retrospective event chronology, not a weather feature known to the operator at13:44. Publication latency, revisions and archived forecast vintages remain unverified. A poor morning forecast does not imply all contemporaneous forecasts were unusable. Nor does a single station prove weather provided no useful lead on the buildup elsewhere. CFc's weather-or-unknowable proportions and “(c) plausibly larger” remain hypotheses, not measured quantities (CFc:120–128,230–245).

“Whole headroom sits in60–120s” is too strong even on the saved afternoon: the report itself gives0.69% naive >120s (CFc:33–35). And this simulator does not constrain *all future storms* to that band; a city-wide factor can rise much more. Keep the observation about this one replay, not CFc:433–434's structural bound. The2/1471 weekday residual is the forecast-active subset, not a universal headroom bound (SF/Claude replay; R16 main-panel totals).

**Data and prior work.** Fresh official Jan/Nov2013 schemas have zones, not coordinates; the correction resolves my R16 “unverified” rather than contradicting a GPS assertion I had made (META:2–3; R16 Q5). Azure coordinate column presence is not proof of non-null historical row values. No row sample was decoded here.

Metadata arithmetic:2009/2010 each5.717/5.655GB;2013 total2.143914GB;2009–2013 total17.907910GB;2014+2015+2016H1 total5.142339GB. Add freshly checked2016Jul–2020Feb5.354365GB gives2014Jan–2020Feb10.496703GB (SF:31; SIZE:2). These decimal compressed sizes reproduce Claude's approximations. Downloads, decoded storage, filtering, random zone-node assignment and factor fidelity remain unvalidated. The original factor formula sums full trip durations for pickup-bin cohorts; reproducing that *target* and producing a causal *observation* are separate tasks (claude-work/r13-ml-data-samples/syed2021_DataSheet1_section1_excerpt.txt:12–18; R16 Q5).

Fielbaum/Alonso-Mora's selected Jan2013 off-peak subset intentionally suppresses traffic uncertainty; **full2013 history** can still add event data (codex-work/r13-paper-text/Unreliability_in_ridesharing_systems_Measuring_cha.txt:592–605). Reject blanket “2013 is the wrong data” arguments that conflate those sets. Yellow trips/day479,527→271,501 is in the saved official monthly table (claude-work/r13-ml-data-samples/tlc_data_reports_monthly.csv:860,556). It warns of sampling shift, but does not measure forecast-transfer loss. “Ride-hail rose from0” is not established by absent2013 reporting; the verified2018 figure691,379 is for FHV–High Volume (same table:552).

Concede that my proposed methods are established components, not methodological novelty. Gardner–McKenzie1985 supplies damped trend (F/gardner_mckenzie_1985.txt:39–46); [Cetin & Comert's primary author record](https://profiles.ncat.edu/en/publications/short-term-traffic-flow-prediction-with-regime-switching-models-5/) describes change detection and adaptive traffic forecasts; [Donovan & Work](https://arxiv.org/abs/1507.06011) studies NYC taxi-derived extreme-event resilience. This supports downgrading a generic scalar forecast pivot. It does not prove every conceivable empirical benchmark is unpublishable. “No method component is new” is the relevant boundary; blanket exhaustive novelty claims are unnecessary. I did not newly verify every peripheral literature entry in CFc §2; no conclusion here depends on those entries.

## Closest prior work and the actual thesis

**HZ strategy B is a decisive prior.** Eq7 sets the required drop time to max(updated,latest) for requests assigned to the evaluated vehicle. The old route is reprojected under current travel times; at-risk riders may not receive additional dispatch delay. With a first-offer deadline substituted for latest, p≤max(p0+B,e) admits p=e. This defeats novelty of the updated reference and of the no-op argument alone (HZ:529–543,567–579). It does not implement C's all-trip sum of absolute revisions.

Two corrections to CR:
- HZ has **routing constraints using the relaxed required times**, plus penalties for violating the original deadlines. “Hard gate rather than penalty” is not a clean distinguishing novelty claim (HZ:575–606).
- Recovery(b) is analogous, not identical: it only activates for forced vehicles and allows no-worse changes on already-violated gates; HZ's threshold is updated each epoch. The theory does not make the empirical21/22 table a general equivalence proof. Most importantly, T3.8 already enabled(b), as its driver/config and154 actual forcedNoWorse entries show (META:7–8; TEX/08:1319–1326). SEL's generic comment about a kept forced option does not override those data.

The broad “C never empties the choice set” claim must be scoped to the stated commitment construction/assumptions, and it must name relaxed-deadline alternatives. It is not uniqueness among all possible rules or proof that every physical/structural feasibility problem disappears. Likewise forecasts, control of instability, business significance and legal attribution are restricted by D03:54–56,211–245,260–269.

I accept CR's call to revise abstract, motivation, theory positioning, results and conclusion. I would **not copy its18 replacements mechanically**: T2/T3 need the qualified HZ distinction above; T4 must say “no recorded failure required accumulation,” not assert unrun equivalence; T17 should say equal aggregate service, not identical rider sets. My R15 set audit already shows2332 common C/M⁺ served riders with six unique to each (A15:19). CR's Q-C wording “same riders” is false (CR:254).

I agree with the bounded undergraduate framing; an institutional pass/accept decision is **unverified**, and CR's conditional “pass” should remain a reviewer opinion, not an assurance (CR:289–292). Current top-venue verdict remains **REJECT**.

## Strict-review scores and decisive questions

Scores1–5 are judgments under the shared standard. Future directions are scored as designs, not successful experiments. The unchanged current-core scores are2/2/3/2/4/4, with feasibility4 only for bounded completion (R16 strict review; limitations above).

| Evidence/claim group | Novelty | Significance | Soundness | Rigor | Reproducibility | Feasibility | Verdict and single damaging question |
|---|---|---|---|---|---|---|---|
| Current thesis core |2: HZ/Fielbaum limit originality |2: no operator need validated |3: audited contract, projected attribution |2: dependent small panel, narrow world |4: pinned data and audits |4: completion uses existing evidence | REJECT at strict venue. What changes practice beyond existing relaxed deadlines? Unanswered. |
| CE cap/screen analysis |2: diagnostic, established trade-off |3: distinguishes prunes from lost customers |3: arithmetic correct, incomplete counterfactuals |2: tiny calibration, no changed trajectories |4: independently reproduced narrow counts |4: completed offline audit | ACCEPT observations; MAJOR REVISION effects. Can all screened additions coexist, and what later riders are displaced? Unanswered. |
| CE objective reconstruction |2: known lexicographic mechanisms |3: directly diagnoses a confounder |4: exact archived reproduction |2: fixed-state, older fixed traffic |4: reproducible, plus independent special case |4: completed screen | ACCEPT S; MAJOR REVISION outcome claims. Does the changed objective improve realized fleet outcomes? Unanswered. |
| CFc incident result |1: classical forecast components |2: one model episode |3: exact replay, overclaimed information split |1: post-hoc gate, one event |4: reconstructed input/outputs |2: multi-year expansion competes with writing | ACCEPT replay; REJECT unknowability claim. What survives unseen storms and genuinely delayed observations at equal quote cost? Unanswered. |
| CR prior/rewrite argument |2: positioning rather than new method |3: removes exposed thesis claims |4: HZ and text verified, baseline omission corrected |3: anchored critique, several extrapolations removed |4: searchable sources and metadata |4: no new data required | ACCEPT qualified rewrite recommendation. Does the claimed difference survive HZ and the already-enabled recovery(b)? Partly answered, against broad novelty. |

## Changes to my R16

1. **Reverse immediate ranking:** whole-thesis consolidation moves3→1; objective×cap moves1→2 as the only optional extension; multi-event forecasting moves2→3/future work. Actual thesis exposure and the modest C30 fixed-state opportunity drive this change. Scientific questions remain open.
2. **Keep all independently measured R16 cap/service/arrival numbers.** No R16 measured table is numerically retracted. Claude's noncausal w07 forecast column is a different rule.
3. **Withdraw the old R12 fitted replay as a promising optimization test.** Retain it only as a negative/null baseline; broaden forecasts only through honest multi-event training, not snow retuning.
4. **Replace the191-job plan:** defer the48-job offered-load add-on. If accumulation is claimed, include the direct120s per-step arm in the main mechanism study instead. New optional budget below is178 jobs.
5. **Correct the proposed forecasting evaluation:** exclude the already-inspected Nov12–18,2018 bundle week from confirmatory test scores, even if using my chronological split. Keep it for reconstruction validation and labelled transfer replay. Preserve the completion-plus-delivery observation rule; one/two-bin finalized-factor lag is insufficient.
6. **Resolve2013 schema uncertainty for the two inspected files**; retain row-quality and domain-transfer gates. Keep my independent weather inventory:2019 alone contains seven≥1-inch snow dates, four proxy spells (WX:7). Do not confuse one bundled incident with all available incident history.
7. **Lower confidence in the C30 sharing target**, and withdraw any suggestion that a positive cumulative witness alone establishes cumulative outcome value. No new service, cost, forecast or profit benefit has been demonstrated this round.

## One ranked list of what the owner should do next

### 1. Recommended next step: revise the entire thesis around the bounded empirical comparison

**Verdict: ACCEPT for completion; REJECT as sufficient new top-venue research by itself.** Restore consistency across abstract/introduction/theory/results/conclusion/bibliography, cite HZ alongside Fielbaum/Alonso-Mora and Schulz/Pfeiffer, demote exclusivity and by-construction claims, add the actual C/M⁺/U/forecast/padding frontier, state recorded cumulative inactivity, and separate model attribution from causal identification. Treat the incident replay as exploratory; avoid “67% unknowable.”

**Decisive existing-evidence audit, zero new jobs:** the34 archived contexts, U/C30/M⁺30, common naive and unchanged causal-no15 quote replays, and predeclared+30/+60 pad display points. These are archived physical policies and offline displays, not six newly run dispatch arms. Existing principal targets: U2434/C2338/M⁺2338 served; forecast late60137/10/10; timely602297/2328/2328; padded-U+30 timely602328 and timely1202366, versus C+forecast2338 timely120 (A15:7–9; R15:167–177). Report sets, denominators and quote extension/early costs. This is a reproducibility/claim-consistency check, not an unseen performance experiment.

**Sealed-style predictions/kill rules:** exact audited counts reproduce; draft correctly names the already-enabled(b); every headline has an identified population and baseline. Kill an unsupported assertion rather than invent a new novelty/result to preserve it. Contract correctness is retained; superiority, causal blame, empirical cumulative necessity and business value stay withdrawn absent new evidence.

**Effort (O):**24–40 focused hours for evidence/text consistency and cross-chapter restructuring, plus remaining writing/supervisor review. This revises my R16's16–24h analysis estimate upward because the task is broader than one results chapter. Deadline and committee requirements remain unconfirmed. No authorized external thesis file is edited in this round.

**Scores:** novelty1(known bounded evaluation), significance2(diagnostic value), soundness4(anchored scoped claims), rigor2(existing narrow sample), reproducibility4(audited corpus), feasibility4(no new pipeline). **Damaging question:** why should a reviewer/operator care about this ledger over existing control? The rewrite can honestly define its scope; it cannot supply the missing practical significance.

### 2. One optional extension: matched objective × cap, with direct accumulation ablation

**Verdict: ACCEPT as a time-boxed design; MAJOR REVISION for any benefit claim until executed.** Do this only after a reviewable rewrite exists and the actual schedule supports it. Do not launch a density sweep, new promise product and forecast project alongside it.

**Arms/panel/jobs:** seven arms on all34 existing8-vehicle contexts:
- stability-first U, cumulativeC30, cumulativeC120;
- cost-first U, cumulativeC30, cumulativeC120;
- cost-first **per-step120**, retaining the cumulative ledger for reporting but using delta≤120s for the tested drop gate.

StableU/C30 archives supply two controls **only after equivalence passes**. Five new arms×34 =170 main jobs. Add four separate OFF-option equivalence jobs (U/C30 on one w08 and one w17 archived context), and four ON smoke jobs (cost-first U/C30/cumulative120/per-step120): **178 new jobs minimum**. Unit/differential checks are additional engineering checks, not hidden simulation jobs. If archived equivalence fails, stop; the178 budget is not permission to silently reuse mismatched controls or run an uncounted replacement panel. C120-stable is included because CR's102-job design otherwise cannot isolate cap relaxation from objective change.

Preserve forced avoidance, accepted-count priority, gates, locks, recovery(b), generation/retention settings, seeds and tie handling; skip only utilization/revision ranking. RollingCost alone changes forced treatment (SEL:276–331). For the per-step arm, explicitly align assessor, decision validation, certificates and breach semantics while retaining S as an audit statistic; a runner still enforcing the cumulative contract would invalidate the ablation. Use a separate future worktree and meaningful boundary/differential tests. Record full commitment witnesses, solver statuses/bounds and generation/retention omissions. Future candidate pools may diverge with state despite identical settings.

Use common physical completion and realized fleet work/cost, **absolute shared completions**, first-quote late60/120, timely completions per requested trip, quote horizons, extension/early errors, repeated changes and distinct cumulative-only decisions/rider–run pairs. Include the existing M⁺(b) and padded-U frontiers as descriptive reference rows, not unmatched cost-first treatment controls. Keep forecasts frozen. Pair by date/source/context; these previewed dates do not become independent unseen events merely because the new policies were not run.

**Sealed-style H predictions/design thresholds:**
- U-cost-first has more shared completions and drop movement than stableU; C30-cost-first retains the service/sharing target from my R16:≥10% more absolute shared completions while serving≥99% as many as stableC30. This target now has lower confidence; report a null without changing it.
- StableC120 recovers≥24 of the current96 aggregate service gap; no monotonicity or per-rider “recovery” guarantee is asserted.
- C120-cost-first shows at least one distinct cumulative-only decision; its per-step counterpart produces some completed rider with S>120s. This is a falsifiable mechanism hypothesis, not a7–10/1000 policy-effect estimate.
- Every cumulative arm has zero verified S overshoot. Any empirical claim that accumulation improves outcomes additionally requires a predeclared common-outcome comparison against per-step120; one witness alone is insufficient.

**Kill rules:** OFF/config mismatch or invalid per-step semantics stops the study; unextractable realized cost kills cost-benefit claims; missed service/sharing target kills the targeted optimization claim. Zero cumulative-only evidence and no S>120 under per-step mean no demonstrated need for accumulation in this tested design. Different decisions without meaningful common-outcome benefit are a mechanism diagnostic, not superiority. Failed uncertainty/cost guards or a result achieved by wider first quotes kills an arrival-improvement claim. Do not search new B/load values after a null and describe them as confirmation.

**Effort (O):**70–110h including both semantic options, tests/equivalence and analysis, plus writing; runtime remains unverified. My old60–90h estimate did not include a direct per-step implementation. Historical15min/job is only a precedent, not a runtime forecast. **Scores:**2/3/3/3/3/2: known components; useful confounder test; two implementations need validation; matched planned comparisons but few independent dates; reproduction depends on future work; substantial schedule risk. **Damaging question:** does accumulation change a useful common outcome after controlling the selector? The added per-step arm can answer on this panel; present evidence cannot.

### 3. Future work: many-event causal incident forecast benchmark

**Verdict: MAJOR REVISION until target and information gates pass.** A generic time-series model or more years alone adds no novelty. Keep it as future work rather than replace the thesis now.

**Decisive experiment:** no initial simulator jobs. Rebuild/validate the factor target; construct separately delayed completed-trip observations; fit2016Jul–2017Dec, calibrate2018Jan–Aug, test2018Sep–2019Dec excluding the inspected bundle week. Compare strong same-data calendar history, persistence, damped residual and one frozen regime/analog candidate, with a2013-extra-history ablation if justified. Final daily weather is strata only; predictor weather needs verified issue/availability times. Use day/event blocks and fixed calibration quote-cost budgets, disclose test cost drift, and keep the seen snow replay a transfer diagnostic (R16 Q5; WX; factor-definition anchor above).

**Sealed-style H/kill:** event-macro30/60min log-factor MAE improves≥10% over history and persistence, ordinary-day loss worsens≤2%; at calibratedE30 quote budget, event late60 improves≥1pp with mean/p90 extension guards1/15s and early60 guard1pp. Kill on leakage, failed target mapping, insufficient independent events after QA, no gain beyond seen Nov15, or failed quote-cost guards. Ten proxy spells is only a design minimum, not guaranteed power or independence. More event forecasts cannot alone establish new C dispatch outcomes.

**Effort (O):**retain my80–140h estimate for an honest target/as-of pipeline and analysis; weather-vintage integration may add20–50h. Claude's35–50h is an optimistic narrower offline-proxy estimate, not a verified schedule for the full availability design (CFc:436–443). **Scores:**1/2/3/2/3/1: classical methods; modest present operator evidence; target/as-of design is essential; multiple unseen events planned but not built; pipeline not certified; weakest remaining-time fit. **Damaging question:** does the gain survive genuinely available observations and equal quote cost on unseen storms? No current answer.

## Remaining disagreements and what would settle them

There is substantial convergence on the rewrite-first sequence, the narrow current contribution, C120 in an optional mechanism study, no new promise object, and the need for honest multi-event data before forecast generalization.

The remaining disagreements are precise:
- **Information split:** I reject treating2299 residual seconds as67% intrinsically unknowable. Settle predictive headroom with frozen models on independent events and explicit as-of feeds; an irreducible/causal weather split needs stronger assumptions than a residual ledger.
- **Objective significance:** CE's local screen strongly suggests a ranking mechanism; it does not apportion terminal FREE/LOCKS outcomes. The matched178-job optional study supplies changed trajectories, with actual work/cost and the per-step comparison.
- **Cumulative equivalence:** no recorded measured failure requires past spending, but behavior/outcome identity is unrun. The direct matched per-step arm settles the tested design, not every possible regime.
- **Closest baseline:** existing T3.8 is recovery(b), now verified. If Claude instead wants literal p≤max(p0+B,e) at every epoch, supply that exact distinct rule and compare it; do not count existing M⁺(b) as missing.
- **Significance standard:** neither a successful bounded extension nor polished engineering guarantees a strict-venue accept. Operator need, generalization and institutional thesis criteria remain unverified.

**Final ranking:** (1) whole-thesis bounded rewrite now,0 new jobs; (2) at most one matched objective/cap/per-step study,178-job minimum if schedule permits; (3) causal multi-event forecasting as future work.

## New files and completion checks

Exclusive-created inside codex-work:
- R17-REBUTTAL-CODEX.md — this deliverable.
- R17-verify-portfolios.py; R17-portfolio-verification.json; R17-portfolio-verification.txt.
- R17-C30-sum-case.txt.
- R17-verify-screens-forecast.py — preserved failed helper.
- R17-verify-screens-forecast-v2.py; R17-screen-forecast-verification.json; R17-screen-forecast-verification.txt.
- R17-verify-metadata.py — preserved failed helper.
- R17-verify-metadata-v2.py; R17-metadata-verification.txt.
- R17-verify-data-sizes.py; R17-data-size-verification.txt.

All successful helpers exited0. No simulations, builds, installs or changes to existing files were performed. HTTP requests retrieved footers/HEAD metadata only. Literature web fetch failures for HZ were handled by reading the permitted saved primary-paper text; no unavailable web content is treated as verified.
