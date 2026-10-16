# Round 14: judgment of Claude's Round 13 proposals

Written by Codex, 2026-10-10. English judgment under ROUND13-RUBRIC.md.

**Recommendation:** keep Claude P1 as a descriptive service/reliability/quote frontier, with hypothetical compensation exposure as an interpretation. The strongest optional algorithm study is P3, changing selection priorities while retaining the same commitment gates. P2, heterogeneous rider budgets, is the next alternative. Choose at most one implementation extension. Neither the present results nor the product survey establishes that RideBound makes a compensated guarantee profitable or establishes a population arrival guarantee.

I read Claude's proposal and relevant evidence, the fact pack, my own R13 proposals, the agreed direction, the stricter owner boundary, cited source/configuration files, saved helper outputs and public sources. I did **not** read Claude's judgment of my proposals. No simulation, build or installation was performed. The new helper reads existing transcripts and prints results; it writes nothing when executed. This report is exclusively created.

## 1. Evidence conventions and source keys

VERIFIED means I opened the source and observed the stated fact. It does not mean the proposed effect has been demonstrated. UNVERIFIED means I could not verify the underlying claim, even where Claude's account is readable. WRONG means the statement is contradicted or its asserted interpretation does not follow; the correction and anchor are supplied. Proposed success thresholds and hours are planning judgments, never achieved results.

Paths below are relative to E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate unless an absolute path is specified. References such as CP:271 are file:line anchors using these explicit keys.

| Key | File |
|---|---|
| CP | claude-work/R13-PROPOSALS-CLAUDE.md |
| PAP | claude-work/R13-PAPERS-CLAUDE.md |
| SUR | claude-work/R13-SURVEY-CLAUDE.md |
| MLD | claude-work/R13-ML-DATA-CLAUDE.md |
| FP | ROUND13-FACT-PACK.md |
| CVP | claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt |
| TIER | claude-work/r13-proposer/tier-budget-screen-2026-10-10.txt |
| WBU | claude-work/wp14r-budget-use-2026-10-10.txt |
| LAD | claude-work/wp14r-ladder-reanalysis-2026-10-08.txt |
| PAD | claude-work/cap-vs-pad-frontier-2026-10-07.txt |
| BUD | claude-work/budget-block-diagnosis-2026-10-07.txt |
| PROP | claude-work/proportional-budget-screen-2026-10-07.txt |
| BACK | claude-work/calib-backtest-2026-10-07.txt |
| RUNTIME | claude-work/RUNTIME-ESTIMATE-2026-10-07.md |
| AG | AGREED-DIRECTION-2026-10-08.md |
| OWN | codex-work/R13-PROPOSALS-CODEX.md |
| VERIFY | codex-work/R14-verify.py |
| WIT | codex-work/R13-cumulative-witnesses.json |
| RAW | codex-work/R13-raw-verification.txt |
| EXTRA | codex-work/R13-extra-raw-verification-v2.json |
| S3 | claude-work/SURVEY-S3-cap-value-and-pooling-regime.md |
| D03 | E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md |
| HO | E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md |
| LATE | E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/lateness-distribution-2026-10-06.txt |
| W14 | C:/Code/RideBound-noworse/docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md |
| CONFIG | E:/Code/Report_INT3508/ridebound-scratchpad/tang3/configs/ |
| SRC | C:/Code/RideBound-noworse/src/ |
| PT | codex-work/r13-paper-text/ |
| SAMPLES | claude-work/r13-ml-data-samples/ |

**Governing boundary, VERIFIED:** D03:54-56 recognizes Fielbaum/Alonso-Mora's pre-decision control and forbids claiming detection of unreliability, pre-decision control or the service-stability tradeoff as new. D03:211-217 recognizes selected-rider protection and Schulz/Pfeiffer's first-offer deadline. D03:222-225 restricts causal attribution and population inference. D03:236-265 forbids converting lower C into demonstrated satisfaction, real lateness, revenue or labor benefits. These restrictions apply to every score below.

## 2. Independent checks shared across proposals

### 2.1 Existing-run reconstruction

I executed VERIFY, a new analysis-only reader, on the **68 existing T3.8 U/C-30 transcripts** already indexed in the R13 raw audit. It decoded the frames, read final ledgers and candidate-pruning evidence, and independently recomputed:

| Check | Status | Observed result and anchor |
|---|---|---|
| T3.8 U exposure | VERIFIED | 2,434 riders; 174 exposed; 12 with at least two nonzero dispatch changes. VERIFY:8,26-33; agrees with CVP:14. |
| T3.8 C-30 exposure | VERIFIED | 2,338 riders; 33 exposed; zero with repeated nonzero dispatch changes. Same reader; agrees with RAW's T3.8 C-30 summary and CP:242. |
| Cumulative-only screen under stability-first U | VERIFIED | Four U riders have each individual change <=120 s but cumulative use >120 s. VERIFY:30-33; CVP:17. Example: d20181114-s10-r3-w08, rider rq-7cfd6335300df902a18021e43c851939ee2979b40bb3460c319f59ff30396d0d, changes 25.844 + 99.027 = **124.871 s**. |
| Two-class screen | VERIFIED | 148 rejected request identities; 193 candidate records; each has exactly one distinct blocking rider. VERIFY:14-24,39-42; TIER:1. |
| Screen by express hash share | VERIFIED | Share 0/.1/.2/.3/.5/1 gives 148/131/114/99/65/0 passing requests; U served 116/101/85/72/48/0 of them. VERIFY:39-42; TIER:2-7. These are candidate screens, not policy completions. |
| Weekday forecast headroom | VERIFIED | 21 C-30 cells, 1,471 served, 2 late>60 s with forecast versus 68 without. VERIFY:43-45 independently sums the existing cell TSV; MLD:284-287. |

This reader uses the R13 raw audit's selected successful transcript paths and U completed-rider TSV. It does not redo the entire frame-hash audit; that was done in R13 (RAW:1-3). It does not create new policy trajectories.

**Three necessary corrections to F1/F5:**

1. **WRONG:** CP:62-66 says exact equivalence at 30 s in all seven populations and differences only at B>=120 under free dispatch. Its own CVP contradicts this: WP14r FREE has **2** cumulative-only riders at B=30 (CVP:5); WP9 panel A b1 has **1** at B=60 (CVP:31); T3.8 stability-first U has **4** at B=120 (CVP:17), independently reproduced above. Say "rare on these observed paths," not "exactly equivalent" or "only under free dispatch."
2. **WRONG as a universal claim:** CP:248-249 says every C cap gives at most one nonzero change. WBU:10 explicitly reports a WP14r C-120 maximum of two. WIT:2-14 identifies that rider's 25.661 + 5.924 = 31.585 s; EXTRA also records two repeatedly changed synthetic C-120 riders. The measured morning C arms and full T3.8 C-30 do have zero repeated spending; do not extend that statement to all C populations.
3. **WRONG inference:** an observed-path screen is neither a policy-equivalence proof nor a general upper bound on how frequently accumulation would bind after a policy change. The accepted sets, schedules and candidate histories can change. CP:93-94 and :839 correctly acknowledge this limitation; its stronger conclusions need the same qualification.

### 2.2 Code verification and historical provenance

| Claim | Status | Opened source and correction/limit |
|---|---|---|
| U/C share the hard-vector policy | VERIFIED | CONFIG/wp4-tier3-v2.json:3 says ridebound-hard-vector; tang3/t38/run_t38.py:92-93 passes the same WP4 file for each arm. CONFIG/U.json:33-40,49-51,65-71 retains zero switch limits. |
| Hard-vector selection puts stability before operating cost | VERIFIED | SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271-272,283-303,319-331,365-385: applicable hard treatment activates worst-utilization and ordered revision levels before operational cost; forced-reference priority is conditional on its presence. Dimension order is SRC/RideBound.Domain/Commitments/CommitmentDimension.cs:19-32. |
| Zero limits can saturate worst utilization | VERIFIED, conditional | SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:612-626 sets utilization to one million for an applicable zero limit with zero usage. This does not prove that level is inactive in every fleet choice: vehicles without applicable active histories and exceptional recovery cases differ. CP:150-155 is an interpretation, not an instrumented decomposition of decisions. |
| FREE is cost-first; fixed-freeze is not hard-C plus cost-first | VERIFIED | SRC/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:287-321 and :465-478; SRC/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:97-108 strips hard limits and final confirmation locks for the mechanism provider. The existing hard-vector arm adds revision priorities. |
| Per-request policy lookup exists | VERIFIED | HardVectorCandidateAssessor.cs:565-570; FleetPyManhattanNormalizer.cs:433-449 stamps the one configured ID onto each request. |
| Multiple configured policies can be decoded | VERIFIED in current source | SRC/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs:84-92 enumerates the policy array, rejecting an empty array rather than requiring one member. This resolves one of CP:421's unknowns at the source level; it does not verify fixture provenance or the deployed binary end to end. |
| Placement can be nested when adding vehicles | VERIFIED, conditional | FleetPyManhattanNormalizer.cs:461-487 ranks selected nodes using artifact SHA, selection key and **ScenarioId**, then takes VehicleCount. The first eight are preserved only if those inputs and selected nodes stay fixed. Giving the larger fleet a new ScenarioId can change placements. |

I also inspected an archived U initializeRun frame: it reports core commit **1ce15e92d2c1459d4254bbbcd581529197257fb2**, binary SHA **a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac**, and hard-vector policy. Source checkout HEAD is **761915cbb89d03f410cd9989ad1cf136e6234bf8**. Read-only git comparison found no difference in SolverBackedFleetSelection.cs between that historical commit and the current file. Other relevant files have changed, so I opened historical source as well: HardVectorCandidateAssessor.cs at that commit:528-541 retains the zero-limit saturation; SolverBackedRidePoolingPolicy.cs:307-335 retains hard assessment/profile selection. The frame is in C:/RideBoundData/research/tier3-t38-v1/U-d20181114-s10-r3-w08/transcript-00.ndjson, initializeRun.

Thus Claude's **objective hierarchy diagnosis is well supported**, including historical source. Its claimed explanation of the magnitude of sharing/exposure differences remains a hypothesis. FREE-to-LOCKS also changes gates and locks (AG:104-110). Candidate retention is another relevant shared component: CONFIG/wp4-tier3-v2.json:10-15 limits candidates and uses a service-set/stability portfolio. Changing only final selection need not expose all cost-efficient alternatives.

### 2.3 Consequential external claims checked against primary sources

These are common checks supporting the proposal-specific tables. Quotes are deliberately short; source interpretation is explicit.

| ID | Status | Primary evidence observed; implication |
|---|---|---|
| E1: Fielbaum/Alonso-Mora control and freeze cost | VERIFIED | Opened C:/PDF/Paper/Unreliability_in_ridesharing_systems_Measuring_cha.pdf, PDF p17, Section 6/Table 5, directly with PDFium. Base: wait/detour/rejection/user cost **1.01/.65/34.5%/9.56**; intermediate **1.51/1.01/31.2%/10.3**; fully controlled **.77/.94/45.6%/11.6**. Rejection difference is **11.1 pp**. Text allows reassignment with equal/earlier pickup. This is pickup-reference tightening plus non-rejection, not a frozen route or a drop-off cumulative ledger. PT/Unreliability_in_ridesharing_systems_Measuring_cha.txt:975-1018. |
| E2: Schulz/Pfeiffer promises | VERIFIED | Opened C:/PDF/Paper/s00291-026-00847-0.pdf and its extraction. Offer deadline is offered arrival plus allowance; both scheduled and latest arrival communicated. Default **900 s**; modeled acceptance parameter **.5**. PT/s00291-026-00847-0.txt:487-492,600-614,1240-1253. These are strong prior work for allowance-versus-service, not a full replicated RideBound comparator. |
| E3: Wardman lateness multipliers | VERIFIED with scope correction | Primary owner PDF 1-s2.0-S0965856426000662-main.pdf; PT/same-name.txt:176-184,607-642: mean late-time multipliers **2.53** (15 observations, 2 studies) and **3.12** (66 observations, 27 studies); separate spread RR **.93**. These are different constructs and cross-context summaries. "2.5-3.1 times" is supported as a descriptive mean range, not the value of C or a pooled-drop 30-s WTP parameter. |
| E4: pooled reliability counterevidence | VERIFIED | Primary Value_of_time_and_reliability_for_urban_pooled_on-.pdf, p1: Dutch stated preference **N=1,006**, in-vehicle VOT **7.88-10.80 EUR/h**, reliability ratio about **.5**. PT/same-name.txt:667 discusses smaller systematic unannounced-time coefficients; :901 states the experiment did not present lateness against a desired arrival. Do not equate this RR with E3's mean-lateness multiplier. |
| E5: Klinkhardt mean delay and buffers | VERIFIED | [Author-hosted full paper](https://publikationen.bibliothek.kit.edu/1000194388/183382050), abstract and Section 4.3: **859** respondents, scheduled public-transport mean-delay coefficient about **3.7** times travel time. Conclusion favors slightly longer on-demand quotes with early arrivals. The scope is scheduled transit/first-last-mile SP, not direct proof for RideBound's drop revisions. |
| E6: wait information field experiment | VERIFIED, abstract | [Yu/Zhang/Zhou publisher abstract](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4448): **1,425,745** rides; one-minute initial-WTI changes had no net abandonment effect because magnitude and update-frequency effects offset; larger pessimistic comparisons report **6.2/14.1/19.6%** increases. Initial WTI and update frequency are coupled here. This is pre-match waiting information, not an independent intervention reducing drop-C or evidence that under-one-minute effects are absent generally. |
| E7: Lyft credits | VERIFIED, qualified primary terms | codex-work/R13-public-lyft-help-clean.txt:31-43,96 and [Lyft help](https://help.lyft.com/hc/en-us/all/articles/115013078668): qualified scheduled rides **to** approved airports; driver >10-min late gives **$15** Lyft Cash; no driver match after 10 min gives **$50**; additional alternate-ride reimbursement is conditional and capped. Airport-origin pickups are excluded. The launch URL intermittently failed on live recheck; these retained primary terms were opened. S3:55's $20 secondary report must not override them. |
| E8: Uber One promise | VERIFIED, dated/regional | [2021 issuer announcement](https://investor.uber.com/news-events/news/press-release-details/2021/Uber-Introduces-Uber-One-A-New-Membership-Program-Bringing-Together-the-Best-of-Uber/default.aspx) says eligible deliveries receive **$5** Uber Cash if latest estimate is wrong. [Ecuador primary page](https://www.uber.com/ec/en/uber-one/) specifies the estimate is determined when the order is placed. This verifies a dated/regional delivery precedent, not current universal pooling coverage. |
| E9: UberPOOL Arrive-by | UNVERIFIED at primary-source level | CP:302-304 relies on [PCWorld's 2016 report](https://www.pcworld.com/article/415144/uberpool-guarantees-youll-arrive-on-time-or-get-a-small-portion-of-your-money-back.html), quoted in SUR:32-35. I did not locate/open a primary Uber policy for the $2/latest-time claim. Also, "absolute latest" wording does not identify the matching algorithm or prove it used only padding. Keep as explicitly attributed historical secondary evidence, or remove from the main novelty argument. |
| E10: UberX Share / driver delay guarantee | VERIFIED facts; WRONG rider interpretation | [UberX Share](https://www.uber.com/us/en/ride/uberx-share/) aims to avoid ETA increases from additional pickups, states **8 min average** additional time and says "we cannot guarantee arrival times". [Delayed Ride Guarantee](https://www.uber.com/us/en/blog/delay-ride-guarantee/) says "What this means for drivers" and is a **driver payment** adjustment after a ride is >=5 min longer than estimated; Matched Share is excluded. Its exclusion is not evidence about rider compensation. CP:289-291 and SUR:336 must separate those subjects. |
| E11: MOIA Express/menu | VERIFIED | [MOIA Express](https://ride.moia.io/en/express) says "shorter arrival window before you book", optional upgrade, more direct routing and up to six offers. This is a real promise-precision product precedent. It does not establish a compensated guarantee, a C ledger or WTP for seconds. |
| E12: patent descriptions | VERIFIED, not legal claim analysis | [Lyft US12182741B2](https://patents.google.com/patent/US12182741B2/en) describes individualized predictable-mode constraints, illustrative detour/pickup limits **5/7 min** and initial-quote ETA ratio **.25**. [Transit Labs US10248913B1](https://patents.google.com/patent/US10248913B1/en) describes rider tolerances and summed drop violations **across riders**, including traffic/co-rider causes. [Via US11674811B2](https://patents.google.com/patent/US11674811B2/en) describes diverting subsequent assignments if estimated delay exceeds **10 min**. Initial-quote/net-delay checks applied at each match are not necessarily bounds on each increment c_j; none of these inspected descriptions establishes a cumulative sum of absolute dispatch revisions. No patent validity/infringement conclusion is drawn. |
| E13: Mt-KaRRi | VERIFIED; accumulation inference unsupported | [Full 2026 preprint](https://arxiv.org/pdf/2605.11798), PDF p5 and Appendix B: trip bound **alpha*T_accepted+beta**, selected alpha **1.4**, beta **10 min**, pickup allowance **10 min**. PDF p22 reports almost two thirds of **urban-rural/rural-urban** rides have additional detour after accepting. This does not mean two thirds have multiple revisions or cumulative-only binding, and does not establish our city's dense-regime mechanism. |
| E14: personalized commitments / routing stability | VERIFIED | [Schmidt et al.](https://arxiv.org/pdf/2609.11950), conclusion, explicitly names dynamic personalized commitments as an extension; its present model is single vehicle/common destination/static interaction, with homogeneous-customer assumptions in experiments. [Ardali/Knapp abstract](https://arxiv.org/abs/2608.13799) reports no single method wins all efficiency/responsiveness/stability/computation axes. Neither measures RideBound's operator payoff. |
| E15: precision revenue and sharper slots | VERIFIED with interpretation correction | [Amorim et al. publisher abstract](https://pubsonline.informs.org/doi/10.1287/mnsc.2020.01274) describes **potential** approximately **9%** shipping revenue from tailoring slots, not a measured 9% uplift in pooling. [Amazon SPEEDY](https://www.amazon.science/publications/speedy-framework-for-sharpening-promise-time-estimates-in-sub-same-day-delivery) reports a **21-day A/B test** and "+17 bps in units". Different domains; no transferable revenue coefficient. |
| E16: additional citations carrying P1/P5/P6 weight | UNVERIFIED at primary-source level | Du/Fan/Chen primary publisher page and attempted full-PDF retrieval did not yield an observed full primary argument; metadata supports only an analytical delivery model (SUR:86-89). Primary URLs for Horl/Zwick's full strategy text, UncertBAT, Du/Budescu's financial-forecast preference and Bent/Van Hentenryck timed out/failed during this check. Claude's quoted passages remain readable at SUR:144-150,177-180,232-248, but I do not promote them to newly verified primary evidence. Financial-forecast preferences would in any case be indirect rider evidence. |

For E1-E4 I reopened the primary PDFs/extractions, not merely Claude's summaries. Publisher DOI pages for E1-E4 were inaccessible, so the owner's full PDFs supplied primary verification. Reported experiments are kept distinct from stated preferences, product descriptions and modeled effects.

## 3. Proposal judgments

Scores are 1-5, with 5 strongest. Ranking below is a decision judgment balancing scientific value and deadline risk; it is not the sum of equally weighted scores. Every proposal has at least three substantive checks. Future run counts are trajectories, not simulations executed this round. T2 implementation must use a separate worktree and pass dotnet test RideBound.slnx; no such work is authorized or performed by this judgment.

### Claude P1: price of a pooled drop-off guarantee

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| T3.8 served gap and tails | VERIFIED | U/C served **2,434/2,338**, gap **96**. LATE:3-5,10-12,24-26 gives >60 s **203/76/10** for U/C/C+forecast and >120 s **102/11/0**; integer counts are arithmetic from the pooled shares. PAD:4,12,15,17,25,33 supplies U+forecast **137/87**, 60-s padded U+forecast **87/48**, and 120-s padded **48/31**. |
| Quote and early-arrival comparisons | VERIFIED | PAD:12,15,17,33: U+forecast extension **7.2 s**, C+forecast **7.4 s**, U+forecast+60 **67.2 s**; early>60 shares **.33/.17/42.44%** respectively. CP:205's 60-s quote difference is rounded: **59.8 s**. |
| r* arithmetic | VERIFIED, aggregate interpretation | No forecast: **96/(203-76)=.756**, **96/(102-11)=1.055**, **96/18=5.333**. Forecast both arms: **96/(137-10)=.756**, **96/87=1.103**. Padded forecast U versus forecast C: **96/77=1.247**, **96/48=2**. These reproduce CP:199-203. |
| WP14r ladder | VERIFIED | LAD:2-6 and W14:76-80: served **1629/1584/1563/1540/1534**, >60 counts **274/47/23/0/0**, >120 **164/27/0/0/0**, >300 **21/2/0/0/0**. CP:223-226 ratios **.20/.33/.88/.78/10.5/1** and six lost with zero >60 reduction follow. |
| Different served sets | VERIFIED; strong causal reading WRONG | CP:847 and HO:181 disclose **227 U-only/131 C-only**. "Late riders avoided" is the difference in late counts among differently selected cohorts, not 127 matched individual rescues. FREE-to-LOCKS is also a package comparison (AG:109-110). |
| Business/novelty precedents | VERIFIED / UNVERIFIED as above | E1-E8, E10-E15 support general relevance and prior work. E9 and E16 remain primary-unverified. The driver guarantee cannot motivate rider reimbursement. D03:56,236-265 precludes a general new guarantee/ROI claim. |
| B=T minus traffic margin implies guarantee | WRONG without conditions | From FP:31-36, with F0=p0+a0, terminal ledger closure gives A-F0=sum(c)+(sum(x)-a0). Therefore A-F0<=B+R, with R=sum(x)-a0. A finite observed/estimated margin for R is not an all-future-world bound; regime shift and clock/execution residuals must be accounted for. D03:222-225,267-269 expressly withholds population coverage. |
| Prospective thresholds and kill rules | VERIFIED as proposal text; outcomes UNVERIFIED | CP:340-350 predicts C-120 served >=2,386, forecast late>120 <=.5%, lower r* than C-30, and a C-0/C-30 late>60 difference <=.2 pp. It kills below 24 recovered or no r* improvement. No full-panel C-120/C-0 results establish these. A >1 pp C-0 difference could also reflect selection, route/traffic exposure and recovery; it would not by itself identify a traffic-only causal effect. |
| Feasibility and missing cap | VERIFIED availability; estimates unverified | CONFIG/C-120.json exists; RAW and FP:73-78 confirm **8 measured morning cells**, not the full34 C-120 panel. CP:335-350 proposes T0 **10-14 h**, optional **68** C-120/C-0 runs. Runtime estimate is extrapolation (RUNTIME:24-25), and C-0 configuration/smoke validity remains prospective. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 3 | A quantified service/nominal-liability frontier is usable; profits, redemption costs and retained demand remain unmeasured. |
| Rider value | 3 | E3-E6 support reliability relevance with mixed constructs; shorter quotes and padding counterevidence must accompany served-only tails. |
| Research value | 4 | The cause-separated frontier and comparable baselines are reusable even if the proposed sweet spot fails. |
| Novelty within boundary | 2 | Guarantees and service-stability curves are prior; only this cause-ledger evaluation and conditional budget-allocation rule remain narrow additions. |
| Feasibility in ~5 weeks | 5 | T0 is small and can stop before optional 68 T1 runs; preserve writing time and label all hours/runtime as estimates. |
| Evidence/falsifiability | 3 | Clear recovery/tail predictions exist, but thresholds are post-preview and few day clusters cannot justify a population SLA. |
| One-storyline fit | 5 | It reorganizes the current cap/forecast/ledger results around one explicit outcome frontier. |

**Step 3: KEEP, revised.** Keep the descriptive frontier; replace "affordable guaranteed arrival" with "measured service cost and hypothetical compensation exposure under an explicit miss rule." **Biggest risk:** turning a retrospective low-load tradeoff into an asserted economically viable or population-safe guarantee.

Required design repair: report completions, reliable completions per all requests, common-rider changes, quote duration and absolute shared completions together. For example, with forecasts, reliable >60-s-threshold completions are **2297 U versus 2328 C** (+31), but at >120 s they are **2347 versus 2338** (-9), arithmetic from PAD:12,33. Padded U+forecast+60 yields **2347** timely at >60 s versus C's **2328**, with a roughly 60-s longer quote (PAD:15). This makes the opportunity cost visible.

The optional economic reading may write DeltaProfit = m*DeltaServed - q*DeltaLate - DeltaOperatingCost + DeltaRetentionValue, explicitly treating every coefficient/behavioral term as unknown. The r* cutoff q/m is valid only under a homogeneous-margin, constant-liability toy model with other terms held equal; it is not a measured business break-even. Day-cluster bootstrap is useful sensitivity analysis, but does not manufacture independent traffic incidents or reliable confidence intervals from very few days.

### Claude P2: express guarantee / per-rider classes

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| 20% screen gives 114 passing requests | VERIFIED | Independent reconstruction in Section 2.1; **85** of these were completed by U. This is not a lower bound, expectation or proof of 114 recovered completions. TIER:4; VERIFY:39-42. |
| Existing core can select policies per request | VERIFIED | Current hard assessment lookup and request field; Section 2.2. Current loader accepts a policy list (CommitmentPolicyConfiguration.cs:84-92), resolving the source-level list-loader unknown. |
| Normalizer and fixture changes | VERIFIED need; end-to-end UNVERIFIED | FleetPyManhattanNormalizer.cs:448 currently stamps one policy. Regenerated mixed-ID fixtures, actual binary loading, provenance/preflight compatibility and equivalence remain untested (CP:409-425). |
| Trip-length variant screen | VERIFIED reported arithmetic | PROP:1-5 shows uniform/proportional passing requests **11/30 at60**, **59/89 at120**, calibrated on served-cohort mean direct time **423.8 s**. It is not an equal offered-budget policy experiment. Three terciles with 30/60/120 budgets are a different allocation and must not inherit those gains. |
| MOIA / precision heterogeneity / prior protection | VERIFIED, limited | E11, E12, E15 and D03:211-213: precision tiers and selective protection already exist. Approximately 9% is modeled potential shipping revenue, not observed pooling tier income. |
| Current .43% tail transfers to express riders | WRONG if treated as a result | LATE:26 verifies C-30+forecast on **all-C** trajectories. Mixed policies change routes and externalities; P2's per-class **1%/4.25%** thresholds are proposed tests, not established performance. CP:428-433 does recognize this test. |
| Standard riders keep U's service; opt-in | UNVERIFIED / unsupported as stated | CP:386's literal service assurance is not implied by standard budgets: protected co-riders constrain standard assignments. Hash membership is an exogenous class experiment, not observed rider opt-in, price choice or uptake. |
| Remaining class predictions and kills | VERIFIED as proposal text; outcomes UNVERIFIED | CP:425-433 requires share0/share1 action-digest equivalence on two smoke cells, >=2,386 served at20% express, zero budget breaches, and standard-rider late>60 within1.5 pp of U's 8.34%. It kills below 24 recovered or express late>60 above 4.25%. These are falsifiable operational targets, not results or causal rider-value evidence. |
| Tier/run plan | VERIFIED as proposal | CP:414-433: T2 **25-35 h**, **2-4 smoke +34** runs at20%, optional34 at50%, separate worktree and solution tests. Zero/one-share action equivalence is a good implementation gate; class assignment must occur before the simulated policy outcome. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 3 | MOIA supports a precision product and the screen supports a candidate lever; uptake, price and recovered service are unknown. |
| Rider value | 3 | Preference heterogeneity is plausible, but class externalities and standard-rider degradation need direct reporting. |
| Research value | 4 | Per-class service/quote/error curves make a useful allocation benchmark. |
| Novelty within boundary | 2 | Tiers, ratios and individualized protection are prior; measured cumulative-ledger allocation is the remaining contribution. |
| Feasibility in ~5 weeks | 3 | T2 25-35 h plus smoke/full runs is plausible but provenance and end-to-end mixed-policy loading are unresolved. |
| Evidence/falsifiability | 3 | Endpoint equivalence and explicit tail kills are good; one deterministic hash and first-order candidates do not establish robust tier gains. |
| One-storyline fit | 4 | It extends the same promise ledger, provided product pricing/demand modeling is excluded. |

**Step 3: KEEP as an alternative to P3; MERGE the trip-length variant with Codex P1.** Test an exogenously assigned promise class, freeze actual assignment shares and offer-time budget rules, and report both classes' all-request outcomes. **Biggest risk:** interpreting candidate passes or random class membership as extra customers choosing/paying for Express.

A moderate set of predeclared assignment seeds or hash sensitivity checks would improve falsifiability; do not pick the seed with best completions. They add runs and must be budgeted explicitly, rather than silently expanding CP's run estimate.

### Claude P3: cost-first selection under C

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| U/C prioritize revision measures before cost | VERIFIED | Source and historical commit checks in Section 2.2 substantiate F3; magnitude of the causal effect is not instrumented. |
| FREE/LOCKS differences show recoverable efficiency | VERIFIED numbers; causal interpretation UNVERIFIED | LAD:2-3 gives **53.1/21.8%** shared and **1629/1584** served. AG:109-110 identifies simultaneous objective/lock changes. These differences cannot be assigned to final selection alone. |
| New objective is needed; rolling penalty baseline exists | VERIFIED | SolverBackedFleetSelection.cs:307-331 distinguishes RevisionPenalty and hard-vector profiles. Fixed-freeze does not provide hard-C plus cost-first (Section 2.2). Existing B2 is an ordered revision objective, not automatically cost+lambda*sum|c|. |
| C can be the only stability constraint | WRONG literally | CP:443 must say "remove soft stability selection priorities while retaining the same hard budget **and locks**." U/C configurations retain switch/confirmation gates; removing those too would confound the objective ablation. |
| Cumulative-only events occur only under free arms >=120 | WRONG | Section 2.1, CVP:5,17,31. Four U riders satisfy the cumulative-only120 screen, and FREE has two at30. Do not motivate P3 with a universal exclusivity claim. |
| P3's .2% cumulative-only prediction | WRONG if defined as accepted over-budget riders | CP:495's event must mean a **rejected candidate** whose incremental charge passes the per-step cap but whose prior use plus new charge exceeds B. Accepted C trajectories cannot show sum|c|>B absent a breach. Report affected incumbent riders and incoming requests with an explicit denominator; do not recycle F1's post-trip exposure test as a positive C result. |
| Operating-cost extraction | UNVERIFIED | CP:480-481 cites event kinds/position/snapshot fields in r13-proposer/probe-event-kinds-2026-10-10.txt:25-26; field presence does not validate driven distance/busy time reconstruction. Candidate abstract cost is not automatically realized fleet cost. |
| Sharing/service predictions and kills | VERIFIED as proposal text; outcomes UNVERIFIED | CP:493-500 targets U-cf shared>=32.8% (22.8+10 pp), C-120-cf shared>=C-120+5 pp with served>=99% of control, and zero breaches. It kills at U sharing gain<3 pp or C-120 service loss>3%. Shared percentage must be paired with absolute shared completions and realized operating effort. |
| Worktree/harness and workload | VERIFIED as plan, not runtime | tang3/w07/run_w07.py:40-46 pins a prebuilt runner/inventory; pilot/run_pilot.py:27 identifies the old harness repository. CP:483-500 budgets **35-45 h**, **2+102** cost-first runs plus **34** stability-first C-120 shared with P1. A copied harness and separate worktree/tests are necessary; source mismatch checks above show why. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 3 | It targets sharing/service/operating effort directly, but efficient fleet use and downstream service gains are still hypotheses. |
| Rider value | 2 | Hard C survives, but total lateness, pickup waits, standard constraints and traffic exposure can worsen. |
| Research value | 5 | It isolates whether final selection priorities suppress budget use, a consequential mechanism question in this pipeline. |
| Novelty within boundary | 2 | Weighted/ordered objectives and stability tradeoffs are prior; controlled same-gate evidence is the narrow contribution. |
| Feasibility in ~5 weeks | 3 | T2 35-45 h and up to 138 jobs including shared C-120/control runs fit only with a small gate and protected writing time. |
| Evidence/falsifiability | 3 | Good sharing/service kill criteria, but fixed candidate retention and the undefined cumulative-binding metric need repair first. |
| One-storyline fit | 4 | One selection component changes under the same cap; the optional lambda sweep should be omitted initially. |

**Step 3: KEEP as the preferred optional algorithm study.** First verify a meaningful realized-cost metric and unchanged candidate/gate semantics; try the minimal cost-first hierarchy, preserving forced-safety and accepted-count priority. **Biggest risk:** a supposed objective ablation actually changes feasible/retained candidate sets, or improves shared percentage while reducing absolute service.

Do not launch all 102 jobs before a small sealed pilot shows the intended selection difference. Compare matching budgets and the same binary across objective arms. Account for retention/work caps and fallback paths. A positive .2% count alone does not show a cumulative cap's service/reliability advantage over a per-step cap; that requires a separate matched enforcement comparator, which is extra T2/T1 work and should be optional.

### Claude P4: four-vehicle load stress

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| Preselected load panel and 48 jobs | VERIFIED | AG:39-43 specifies **12** cells (14/16/17 Nov, selected replicates in w08/w17), four policies, **48** jobs. Keep those choices fixed. |
| Historical four-vehicle counts | VERIFIED saved evidence | CVP:19-28: b1 **966**, c1 **860** accepted, b1 **38/966=3.93%** repeated changes, c1 zero. claude-work/fleet-size-wp9-check-2026-10-07.txt:4-5 confirms counts; these use an older runner and package policies, not the proposed isolated comparison. |
| Baseline C cost at 8 vehicles | VERIFIED arithmetic | WP14r LOCKS-to-C30 **50/1584=3.16%**, rounded3.2%; T3.8 U-to-C30 **96/2434=3.94%**. LAD:3,6; FP:41. |
| Config-only normalizer/nesting | VERIFIED option; deployment UNVERIFIED | AG:112-114 describes staging with prebuilt DLL. Section 2.2 gives conditional nested placement. Fixture equality, actual DLL/provenance and smoke behavior must be checked prospectively. |
| 283s median implies under 1 h | VERIFIED median; wall forecast UNVERIFIED | RUNTIME:14 lists **283 s** for108 requests/four vehicles, across confounded historical experiments. Arithmetic 48*283/6 is about **38 min**; FREE timing, tail runtimes and concurrency conditions are not established. CP:538-539 acknowledges this. |
| Full stress targets | VERIFIED as proposal text; outcomes UNVERIFIED | CP:542-548 targets LOCKS-to-C30 served loss<=8%, C30 repeatedly changed share<=.1%, FREE shared>=35% and drop-exposed>=15%. Failure of the8% criterion is its kill. Retain the sealed12-cell choices; these thresholds do not establish transfer beyond the tested load/graph. |
| "Price holds under load" | UNVERIFIED hypothesis | CP:541-548's <=8% served-loss and sharing/exposure thresholds are proposed; only three calendar days are included, not city-scale external validity. E13 does not prove repeated-budget use in this panel. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 2 | It tests sensitivity of the measured service cost; it does not identify real operator fleet economics. |
| Rider value | 2 | Lateness/common-rider burden must accompany load and service, not only sharing/exposure. |
| Research value | 4 | A sealed stress panel answers a real validity concern and can falsify a cheap-cap narrative. |
| Novelty within boundary | 1 | Load robustness is an evaluation extension, not a new method. |
| Feasibility in ~5 weeks | 4 | T1 12-16 h and 48 jobs avoids core changes, subject to fixture/runner smoke checks. |
| Evidence/falsifiability | 3 | Preselected cells and explicit kills are good; old-runner evidence and three-day dependence limit conclusions. |
| One-storyline fit | 5 | It belongs in the same frontier's robustness subsection. |

**Step 3: MERGE-WITH(P1).** Use as the first optional robustness panel after the cap selection/smoke gate, not a standalone new thesis direction. **Biggest risk:** claiming density transfer from a small restricted graph with different fleet placement or changed fixture requests.

### Claude P0: unchanged storyline

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| Existing core/results suffice for bounded descriptive claims | VERIFIED | FP:31-49,65-69, RAW and the forecast/late outputs document the current cap, quote and ledger story; D03:241-245 explicitly describes its limited protected value. |
| No new novelty claim needed | VERIFIED | D03:56,211-225,236-269; E1/E2 restrict any claim of being first to control instability or protect an offered deadline. |
| Cumulative feature not empirically central at30 | VERIFIED, qualified | Full T3.8 C30 has zero repeated nonzero changes (Section 2.1); this does not imply all cap levels/populations lack repeated spending. CP:571 and FP:94 need that scope. |
| Zero extra runs / zero analysis time | VERIFIED run-free option; zero effort WRONG if literal | CP:559,575 proposes no new analysis or runs. Necessary claim/cohort/metric edits and final consistency checks still take work; OWN:113-117 estimates **16-24 h** T0 plus writing time. Those hours are estimates, not measured. |
| No further evidence required | WRONG for stronger owner-value claims | CP:573 is true only for retaining descriptive claims. D03:241-245 states incremental practical value is unconfirmed and needs an operator problem/cost/acceptable threshold; writing cannot supply that missing evidence. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 2 | It provides enforceable restraint/audit, but the owner's practical-benefit question remains only partly answered. |
| Rider value | 2 | Simulated served-rider lateness exists; no preference or behavior validation for this C contract exists. |
| Research value | 3 | A reproducible verified system/negative-result story remains a legitimate undergraduate contribution. |
| Novelty within boundary | 2 | Only the cause-separated cumulative contract/certificate and its bounded evaluation survive prior work. |
| Feasibility in ~5 weeks | 5 | Zero new runs or builds; allow explicit editing/checking and thesis-writing time. |
| Evidence/falsifiability | 3 | Existing audits are strong for their corpus, but there is no new prediction or independent validation environment. |
| One-storyline fit | 5 | This is the current storyline with corrected boundaries. |

**Step 3: MERGE-WITH(P1) as its fallback.** If any new gate fails or time is short, finish the existing bounded story without promising a new sweet spot. **Biggest risk:** presenting completion of the thesis as fulfillment of a stronger unmeasured business-value requirement.

### Claude P5: pooling-proof arrival window

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| C alone ensures actual arrival inside [F0-30,F0+B] | WRONG unconditionally | CP:604-605 conflates controlled dispatch movement with terminal arrival. The Section3/P1 equation gives A-F0=sum(c)+R. C bounds the first term, not R; positive residual forecast error can breach the upper endpoint and negative residual error can breach the lower one. |
| ±60s backtest coverage | VERIFIED | BACK:4,38 gives C **100/99.7%**, U **96.9/94.6%** on 15/16 Nov. These describe **120-s-wide** intervals, not CP:634's60-s window. |
| Proposed 99% coverage in 60-s window | WRONG as an inference from the cited backtest; prospective target UNVERIFIED | BACK:38 gives C Y30 **1.60%** of376 and **.91%** of656: about **6+6=12** late>30 riders. Thus the same chronological forecast's ±30 coverage is at most **1020/1032=98.84%**, even before early misses. If a different F0 is intended, define it and test it; the cited result does not support the existing99% claim. |
| Real short-window products and prior windows | VERIFIED / UNVERIFIED | E11 verifies MOIA; E15 verifies SPEEDY +17bps. E16 leaves UncertBAT and financial-forecast preference primary-unverified here. Bharti et al.'s [primary abstract](https://arxiv.org/abs/2601.19601) verifies threshold-triggered updates in a delivery/appointment model, not a pooling guarantee. Rauh's appointment ranges in PAP:419-439 concern another domain. |
| Comparison and kill target | VERIFIED as proposal text; outcome UNVERIFIED | CP:635-637 targets best60-s U forecast window coverage<=95%, with offset fitted on14 Nov only, and kills a C-U coverage gap<1 pp. This comparison has not been executed here and must use the same forecast/reference and interval width before interpreting any cap advantage. |
| T0 replay scope and cost | VERIFIED as proposal | CP:629-637 proposes **6-8 h**, zero new runs, replaying U/C30 T3.8 and morning higher caps. Actual calibration/comparable-width controls, early misses and timestamp convention remain work, not established results. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 2 | A disclosed precision frontier is interpretable, but no uptake/cost benefit follows from merely drawing a window. |
| Rider value | 2 | MOIA motivates the format; financial/weather or delivery studies do not validate this window's rider value. |
| Research value | 3 | Equal-width/upper-end comparisons are useful if residual uncertainty and both tails are explicit. |
| Novelty within boundary | 2 | Windows/calibration are prior; budget plus uncertainty accounting is a narrow presentation/evaluation adaptation. |
| Feasibility in ~5 weeks | 4 | T0 zero-run replay is cheap; repairing the advertised guarantee and credible calibration may exceed 6-8 h. |
| Evidence/falsifiability | 2 | The stated construction proof fails and its cited120-s coverage does not substantiate the60-s prediction. |
| One-storyline fit | 3 | It can be a display alternative in P1, but should not create a second promise/guarantee chapter. |

**Step 3: MERGE-WITH(P1), after rewriting.** Call it a calibrated arrival window with separately bounded dispatch movement; report coverage/width and upper/lower misses. **Biggest risk:** an empirically calibrated or forecast-dependent interval is advertised as guaranteed by C.

Reject the phrase "pooling-proof by construction" for terminal arrivals. A provable dispatch-only statement can still be shown separately, conditional on a specified reference/forecast path; it is not the complete rider-facing SLA.

### Claude P6: price in vehicles

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| Average-productivity arithmetic | VERIFIED, descriptive only | **2434/(34*8)=8.95** completed riders per vehicle-cell; **96/34=2.82** gap per cell; ratio is **.316 vehicles per cell**, or **3.94%** of8. CP:657-659 explicitly uses average, not marginal, productivity. |
| Structural rejections imply fleet is the binding resource | WRONG as identification | BUD:2-5 gives **1186** structural-only C rejections and **148** budget-blocked. "Structural" combines non-budget feasibility/candidate restrictions; it does not isolate fleet scarcity from windows, max-ride bounds, graph selection or search caps. |
| Nine/ten vehicles preserve first 8 | VERIFIED conditional source, not fixtures | Section2.2: selected nodes/ScenarioId/keys must remain fixed. CP:663's unverified nesting is resolvable as a source condition; proposed fixtures have not been generated/validated. |
| Nine vehicles match U; failure implies >=25% cost | UNVERIFIED prediction; lower-bound interpretation too strong | CP:668-670 proposes >=2434 with9. **9/8-1=12.5%**, **10/8-1=25%**. Failure at9 establishes failure in the tested heuristic/placements, not an optimal minimum fleet or general business cost. No10-vehicle outcome exists here. |
| Resource-augmentation precedent | UNVERIFIED primary this round | E16 records failed Bent/Van Hentenryck opening. PAP:98-103 discusses established system metrics; it does not establish this fleet-sizing prediction or a new method. |
|68 runs and12-16h | VERIFIED plan; runtime unverified | CP:663-670 budgets two fleet sizes over 34 cells, T1 **68** runs, **12-16 h**. Existing8-vehicle runtime cannot guarantee9/10-vehicle wall time (RUNTIME:14-25). |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 2 | Vehicle units are familiar, but capacity productivity, labor cost and an optimal fleet requirement are unmeasured. |
| Rider value | 1 | More fleet may help availability, but this experiment supplies no distinctive preference/reliability evidence. |
| Research value | 3 | Resource sensitivity is reusable as a descriptive stress comparison. |
| Novelty within boundary | 1 | Fleet augmentation is established and does not add a new promise-control mechanism. |
| Feasibility in ~5 weeks | 3 | T1 68 jobs plus fixture/provenance gates is plausible but competes directly with stronger cap/objective work. |
| Evidence/falsifiability | 2 | Average productivity is not a marginal prediction and the proposed kill should not imply optimality. |
| One-storyline fit | 4 | One fleet-sensitivity figure can support P1, if it is explicitly heuristic- and placement-specific. |

**Step 3: REJECT as a separate work package; optional merge into P1/P4 robustness if resources remain.** Do not prioritize 68 jobs to test an unsupported average-productivity extrapolation. **Biggest risk:** presenting heuristic failure at 9 vehicles as a lower bound on the operator's fleet cost.

### Claude P7: multi-week traffic profile / ML

**Step 1: verification**

| Central claim | Status | Check/correction |
|---|---|---|
| Public monthly data volume/schema | VERIFIED saved metadata, not rows | SAMPLES/parquet-footer-probe-2026-10-09.txt:1 records Nov2018 yellow **117,170,616 bytes**, **8,155,449 rows**,19 fields including pickup/drop datetimes and zone IDs; MLD:136,219-224 gives Sep-Dec about **.48GB**. I opened the probe output, not millions of trip rows. Logical timestamp resolution and row quality remain unverified (MLD:447). |
| Factor derivation is documented | VERIFIED source excerpt; exact rebuild UNVERIFIED | SAMPLES/syed2021_DataSheet1_section1_excerpt.txt and MLD:72-107 describe duration/free-flow sums for trips beginning in a15-min bin, random zone-to-node assignment and speed filtering. The precise speed-filter distance definition is unresolved; median relative error<=3% is a proposed gate, not achieved reconstruction. |
| Only 8 days / 2-day vintage | VERIFIED with correction | MLD:43-50 and factor inventory distinguish **7** daily15-min profiles,12-18 Nov, from **8** hourly days including warm-up11 Nov. CP:681 refers to12/13 Nov forecast history, not a many-week fit. |
| Headroom counts | VERIFIED / scope correction | Independently recomputed weekday **2/1471** vs68. MLD:293-298 and saved snow report describe **34/601** versus41 and **92.5%** unanticipated late seconds. Those counts identify small weekday Y60 headroom and one afternoon incident, not impossibility of improving MAE, quote length, calibration or future-event lateness. |
| No quoted ETA in verified trip schemas | VERIFIED scoped negative | Opened TLC footer/schema evidence and Meituan documentation; MLD:259-262 correctly restricts the statement to verified TLC/Chicago sources. SAMPLES/meituan_tsl_background_20240321.txt:193-202 explicitly defines a promised delivery Unix time. This does not prove no public pooling promise dataset exists. |
| Weather limits | VERIFIED saved NOAA output; inference limited | SAMPLES/noaa-event-days-2026-10-09.txt:2-4 has **one weekday >=1-inch snow** in Sep-Dec2018,15 Nov; :7-8 identifies **16** such weekdays and **7 >=3-inch** weekdays in Jul2016-Feb2020. Absence of another heavy-snow test does not eliminate non-snow incident or forecast-error evaluation. |
| Install/effort/input changes | VERIFIED disclosed gap; estimates unverified | MLD:243-245 reports missing parquet engines in shared environments; CP:699-706 proposes T3 **1-1.5 weeks**, zero simulation replay, extra **1-2 weeks** for unseen worlds with unverified wrapper input path. A separate isolated data environment is possible; shared-install approval is not an intrinsic scientific requirement. No installation was performed. |
| "Cannot bring weekday late below 2" | WRONG as a literal impossibility | Existing 2 late gives an upper bound of **2 eliminated events**, not a floor of2. A new model could yield0/1; whether that is statistically persuasive is a different question. CP:703-704/MLD:287 must distinguish a small effect from an impossible one. |

**Step 2: scores**

| Criterion | Score | One-line justification |
|---|---:|---|
| Operator value | 1 | No measured operational gain; data preparation chiefly changes confidence in the forecast evaluation. |
| Rider value | 1 | New rows provide no promise labels or behavioral validation for RideBound's riders. |
| Research value | 3 | More independent chronology and factor reconstruction could improve external validity if leakage gates pass. |
| Novelty within boundary | 1 | Historical profiles/ML ETA are established; this is robustness work, not a new forecasting method. |
| Feasibility in ~5 weeks | 1 | T3 1-1.5 weeks plus potentially1-2 weeks of world-generation work would consume much of the unconfirmed deadline. |
| Evidence/falsifiability | 2 | A reconstruction gate is useful, but current days are previewed and a snow-only gain still has one event cluster. |
| One-storyline fit | 2 | A narrow appendix fits; the full data/world pipeline risks becoming a separate thesis. |

**Step 3: REJECT as a deadline work package.** Retain the schema/headroom/causality findings as limitations and future work, without the absolute no-improvement assertion. **Biggest risk:** a large data pipeline produces a better off-target predictor but no validated link to the simulator or C contribution.

## 4. Claude's top three, misses and removals

### Top three

1. **P1, corrected empirical frontier.** Best immediate answer to the owner's operator/research question per unit of additional effort. The existing negative and opportunity-cost results remain reportable even if no sweet spot appears.
2. **P3, controlled objective experiment.** Strongest optional pipeline optimization: it asks whether unnecessary selection conservatism suppresses efficiency under the same hard promises. Source verification supports the premise; the effect and useful candidate diversity remain to be tested.
3. **P2, exogenous promise classes.** Strong product precedent and a reproduced first-order screen. It follows P3 because "opt-in guarantee" and pricing are unsupported, but it remains a viable alternative rather than a second simultaneous project.

P0 is the safest fallback. P4 is a useful robustness component of P1. P5/P6/P7 should not become competing standalone directions. The scores assess evidence available now; they are not predictions that P3 will outperform P2.

### What Claude missed that I would add

- **A common-objective comparison with the deadline gate.** P1's guaranteed-arrival interpretation should retain Mplus as a central comparator, not just quote its forced rate. PAD:33,54 shows C30+forecast and Mplus30+forecast both **2328 timely** at >60 s and near-equal quote extensions. The contribution is obligation semantics/recovery behavior, not a unique end-to-end arrival advantage. D03:214-225,238-239 requires this distinction.
- **Reliable completions per request and absolute shared completions.** P1's gain is +31 at 60 s with forecast, but -9 at 120 s, before padding; percentages alone hide rejected demand. P3/P4 must measure absolute productive sharing, as AG:57 already requires, not only shared fractions. Anchors PAD:12,33 and AG:57.
- **A candidate-level accumulation witness and an explicit optional per-step comparator.** The exposed-path screen cannot demonstrate the cumulative clause's treatment effect. P3 must log which candidate is rejected because prior spending matters. If a cumulative-versus-per-step policy claim is needed, isolate that gate on matching objectives/candidates; label extra implementation/runs rather than pretending it is already proved. VERIFY:30-33 and CP:90-94.
- **A source-level resolution of feasibility unknowns.** The loader already decodes multiple policy records; placement is deterministically nested only when ScenarioId and the other ranking inputs remain fixed. Section2.2 replaces vague unknowns with precise smoke conditions.
- **Candidate-retention and compute-budget controls.** CONFIG/wp4-tier3-v2.json:10-15 restricts retained candidates. If stability-aware retention discards cost-efficient choices, changing final selection alone cannot recover them; test this before scaling P3.
- **Computational efficiency as a fallback optimization axis.** My Codex P2 proposes verified affected-suffix evaluation beyond current same-state cache, with profiling/differential gates (OWN:89-103). It needs no new product demand model. Keep it below the closer objective/allocation studies, and abandon it if the hotspot/gain is absent.

### Overclaims to remove before showing the owner

| Remove/rewrite | Correct statement and anchor |
|---|---|
| Exact per-insertion equivalence at30; differences only free and >=120 | Rare path-screen differences; FREE has 2 at30, WP9 has 1 at60, U has 4 at120. CVP:5,17,31; Section2.1. |
| Every C cap has at most one revision | True for specified measured morning C arms/full T3.8 C30, false for WP14r/synthetic C120. WBU:10; WIT:2-14; EXTRA. |
| Industry does not guarantee pooled drop-offs today | Checked UberX Share disclaims arrival guarantees; the survey cannot establish a universal market absence. E9-E11; CP:289. |
| Matched Share exclusion is rider-guarantee evidence | It belongs to driver remuneration. E10. |
| Lyft pays cash / any airport pickup / automatically up to100 | Qualified future-use Lyft Cash for airport-bound scheduled rides, with conditional additional reimbursement. E7. |
| UberPOOL's guarantee proves a padding-only algorithm | Historical secondary reporting identifies latest-time wording; algorithm attribution is not established. E9. |
| 2.5-3.1 /3.7 /RR .5 are interchangeable C valuations | Mean lateness, spread and displacement are distinct, with different populations; none monetizes the C ledger. E3-E6. |
| Mt-KaRRi's two-thirds result proves accumulation is common | It measures additional detour in particular OD categories, not multiple revisions/cumulative-only decisions. E13. |
| r* means one rider rescued costs .8-1.1 other rides; guarantees are affordable | It is an aggregate ratio on selected cohorts; profitability and SLA coverage are unconfirmed. CP:847; D03:241-269; Section3/P1. |
| B=T minus a traffic margin guarantees arrival | Conditional residual-budget relation, subject to calibrated uncertainty and model/execution assumptions. Section3/P1. |
| C is the only stability constraint in P3 | Retain the same hard C, locks, safety/recovery and service-count priority while changing selection cost priority. Section3/P3. |
| Hash share is opt-in; standard riders retain U's outcomes | It is assigned-class operational evidence; actual choice/demand and class externalities remain unknown. Section3/P2. |
| A 60-s interval inherits ±60-s99.7-100% coverage | ±60 is 120-s width; the cited ±30 late counts already limit two-day coverage to at most 98.84%. BACK:38. |
| Structural rejection establishes fleet scarcity / .32 vehicles is the marginal cost | These are heterogeneous structural causes and an average-productivity analogy, not identified fleet need. BUD:2-5; Section3/P6. |
| More training data cannot improve lateness or below 2 is impossible | At most2 weekday Y60 events remain in this fixed corpus; small headroom limits persuasive gain, not all error metrics or all future regimes. MLD:284-298; Section3/P7. |
| Keeping the story requires zero effort | No new trajectories are needed; corrections, common-cohort reporting and writing still require time. OWN:113-117. |
| Fielbaum's open problem makes our control/tradeoff new | Section6 already implements control/tradeoffs; the stricter boundary explicitly excludes that novelty. E1; D03:54-56. |

## 5. Cross-side comparison

Here C-Pn means Claude's original ID in CP; X-Pn means my original Codex ID in OWN. This is **one ranked list of eight merged items covering all fifteen original proposals**. It is a menu, not an instruction to execute eight projects.

| Rank | Merged direction and every original ID mapped here | Judgment and reason |
|---|---|---|
| 1 | **Empirical service/reliability/quote frontier with nominal compensation interpretation:** C-P1 + X-P5 | KEEP the T0 analysis as the preferred main refinement. Claude's r* arithmetic gives my nominal-credit exposure idea a clearer service opportunity cost. Preserve monetary parameters as hypothetical and retain Mplus/common-rider controls. Sources CP:271-357; OWN:153-167; Section3/P1. |
| 2 | **Selection objective under unchanged hard gates:** C-P3 | Preferred conditional T2 algorithm extension. It is more directly tied to the mechanism than either more data or product menu changes. Start with a small objective/candidate/metric gate, not the full matrix or lambda sweep. CP:440-503; Section2.2/3/P3. |
| 3 | **Who receives how much dispatch allowance:** C-P2 + X-P1 | MERGE the class and proportional variants as alternative allocation rules; test one frozen rule initially, not two products plus a learner. MOIA/individualized constraints narrow novelty; ensure offered-budget fairness and class tails. CP:361-436; OWN:73-87. |
| 4 | **Finish the present bounded thesis:** C-P0 + X-P0 | KEEP as the fallback when extension gates/time fail. Both proposals now need the same objective, cumulative-scope and buyer-value corrections. CP:554-598; OWN:105-119. |
| 5 | **Load/fleet robustness of the same frontier:** C-P4 + C-P6 | MERGE four-vehicle stress into rank 1; defer nine/ten-vehicle resource pricing. This is a robustness figure, not a second novelty claim. Preselected12-cell load panel is better motivated than average-productivity fleet extrapolation. CP:507-550,643-672. |
| 6 | **Affected-suffix evaluation efficiency:** X-P2 | KEEP only as an alternative optimization if profiling identifies substantial redundant work; exact outputs and current cache baseline must match. It offers computational value but needs 32-56 h T2 and weaker direct evidence about the owner's promise-value question. OWN:89-103. |
| 7 | **Calibrated window display plus separately certified dispatch movement:** C-P5 + X-P3 | MERGE into an optional display subsection of rank 1. Withdraw unconditional endpoint/pooling-proof language; require equal-width/upper-end controls and both tails. Existing backtest does not substantiate the tighter window. CP:602-639; OWN:121-135. |
| 8 | **Forecast/data robustness, explicitly deferred:** C-P7 + X-P4 + X-P6 | No standalone ML/data chapter before the deadline. Distinguish X-P4's small existing-input damped replay from C-P7's factor reconstruction and X-P6's external duration benchmark; only the first remains an economical optional appendix. New public duration work is least connected to the simulator. CP:676-709; OWN:137-183; MLD:321-408. |

**Accounting check:** Claude P0-P7 appear exactly once; Codex P0-P6 appear exactly once. Duplicate merging does not change their original IDs or conceal rejected branches.

### Which of my R13 proposals I now withdraw or change

- **X-P1 proportional budgets: change and demote from my original first choice to rank 3.** Merge with C-P2. Claude's objective diagnosis means proportional allocation must be compared on a fixed objective and offered, pre-service budget distribution. Existing mean423.8 uses a selected served cohort (PROP:1); it cannot normalize future test budgets without selection bias. Keep the cumulative cause ledger, but do not advertise proportionality/individual protection as novel (E12/E13; D03:211-213).
- **X-P2 suffix evaluation: keep, lower priority.** It remains a conditional speed hypothesis beyond existing same-state caching, not a proven production gain. Objective selection has a closer connection to why measured C is little used. The original profiling/differential kill gates stand (OWN:95-101).
- **X-P0 unchanged story: keep as fallback, correct its broad wording.** OWN:117's "measured C does not exercise repeated spending" must be restricted to its named morning/full-C30 corpus; WP14r/synthetic C120 counterexamples already appear in my R13 evidence. Also add stability-first baseline and same-endpoint deadline comparisons.
- **X-P3 frozen window: merge and narrow.** Keep the calibrated uncertainty hypothesis, withdraw any automatic guarantee from C, and report residual error and early misses. My original90%/60-s exploratory target is not an industry SLA or independent-day coverage theorem (OWN:127-133).
- **X-P4 damped forecast: retain only as a small optional retrospective falsification replay, not a contribution requirement.** Claude's reproduced2/1471 weekday residual reinforces my low-headroom caveat. Keep the existing input-causality/quote-cost gates and do not retune around 15 Nov (OWN:139-149).
- **X-P5 compensation exposure: withdraw as a separate direction and merge into C-P1.** Claude's r* provides useful service units; my original remedy-regardless-of-cause and nominal-credit-versus-profit limits remain necessary. Do not import the driver guarantee or assume redemption/retention values (OWN:155-165; E10).
- **X-P6 many-week duration benchmark: withdraw from this deadline's recommended work packages.** Claude's factor-method documentation makes an eventual same-domain factor rebuild more relevant than my HVFHV duration appendix. Public duration labels cannot isolate post-promise dispatch changes and the simulator erases OD-level traffic detail (MLD:323-324,394-405). More data availability is not a contribution or an established transfer path.

## 6. Concrete stopping rules for the owner-facing recommendation

Finish the current thesis with the corrected rank 1 frontier and rank 4 fallback. If the owner requires an additional component optimization and time permits, choose **either rank 2 objective selection or rank 3 allowance allocation**, following a small sealed feasibility/metric gate in a separate worktree with solution tests. Both should report failed hypotheses honestly. Do not add a new demand model, learn a pricing policy, reconstruct many years of traffic and redesign promise windows concurrently.

All proposed success margins are decision rules informed by already inspected outcomes, not unseen-result preregistration. New runs, tests/builds and new data processing need a separate authorized implementation turn. No success, profit, customer uptake or population guarantee is asserted by this judgment.

Files created for Round14: R14-verify.py; R14-JUDGE-OF-CLAUDE-BY-CODEX.md. The helper only reads existing data when run; existing R13/source/Claude files were not modified.
