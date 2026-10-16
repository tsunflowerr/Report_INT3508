# R13 proposals by Codex — independent, 2026-10-10

**Recommendation:** retain the cause-separated C + traffic-forecast storyline, and test **one bounded extension: P1, per-trip budget allocation**, before adding more ML. Begin with an analysis gate; if it fails, choose P0 and write up the current contribution honestly. P2 is the alternative if the committee specifically requires a pipeline algorithm improvement. The seven ranked options below are alternatives, not seven parallel work packages. The approximately five-week deadline is unconfirmed.

The companion [R13-SURVEY-CODEX.md](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md) contains all 13 supplied-paper readings, the example-thesis analysis, verified live primary quotes, product qualifications and public-data limits. No simulation or build was run in this round. No Claude R13 file was read. All new files were created exclusively inside codex-work.

## 1. Independent O1/O4 verification

**Method and denominator.** [R13-verify-raw-v3.py](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-verify-raw-v3.py) independently decodes raw NDJSON frames, verifies each decoded SHA256, reads the last runner-to-adapter checkpoint and reconstructs each initial-promise rider's ledger. It computes signed `c=p.dropEta−e.dropEta`, `S=Σ|c|`, pickup analogues and number of nonzero dispatch revisions; it cross-checks stored absolute deltas. Completed riders equal initial-promise ledgers; all requests are completed/rejected. Forced means certificate `normalOperation=false`, not a failed solver or the top-level “produced” status.

The main audit covers **196 existing runs / 389,518 verified frames**: w07 U and eight C caps, seven Mplus caps, and the 34-cell T3.8 U/C-30 test panel. A separate [extra verifier](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-verify-extra-raw.py) reads **45 runs / 106,314 verified frames** for WP14r FREE/C-120 and synthetic C-120. These are file analyses, not 241 new simulations. [Main JSON](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-raw-verification.json), [readable summary](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-raw-verification.txt), [rider rows](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-rider-budget.tsv), [corrected extra JSON](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-extra-raw-verification-v2.json). Input paths and full transcript hashes are recorded per run. Failed initial verifier drafts remain; v3 completed successfully.

**O1 — every asserted run-existence/count row.**

| Fact-pack assertion | Independent result | Verdict |
|---|---|---|
| Measured-traffic C-120 exists in w07 | 8 drained raw runs, 12/13 Nov, 07:00 window; 864 requests, 666 completed | **MATCH** |
| w07 U served 665 | 8 runs, 665/864 | **MATCH** |
| w07 C-30 served 660 | 8 runs, 660/864 | **MATCH** |
| w07 C-60 served 661 | 8 runs, 661/864 | **MATCH** |
| w07x C-90 served 664 | 8 runs, 664/864 | **MATCH** |
| w07 C-120 served 666 | 8 runs, 666/864 | **MATCH** |
| w07x C-150 served 666 | 8 runs, 666/864 | **MATCH** |
| w07x C-180 served 666 | 8 runs, 666/864 | **MATCH** |
| w07x C-240 served 665 | 8 runs, 665/864 | **MATCH** |
| w07 C-300 served 665 | 8 runs, 665/864 | **MATCH** |
| Mplus forced %, caps 30/60/90/120/150/180/240 | Mean of cell decision fractions: 58.6265 / 35.5383 / 12.9608 / 6.5718 / 6.8184 / 2.8206 / 1.6998% | **MATCH** to reported 58.6 / 35.5 / 13.0 / 6.6 / 6.8 / 2.8 / 1.7 |
| C never forced, audited w07 cap ladder | 0 in every audited C cap | **MATCH**, within this corpus |
| Full 34-cell T3.8 C-120 not present | No C-120 folders in declared `tier3-t38-v1` archive; split selects 34 test cells | **MATCH** for named archive; not a claim of universal absence elsewhere |
| Synthetic C-120: 13 runs | 13 drained raw runs, 1,404 requests, 1,205 completed | **MATCH** |
| Fixed-traffic WP14r C-120 exists | 16 drained raw runs, 1,728 requests, 1,563 completed | **MATCH** |

Locations: `C:/RideBoundData/research/tier3-w07-v1`, `tier3-w07x-v1`, `tier3-t38-v1`; `E:/RideBoundData/research/tier3-sweep-v1`; `E:/RideBoundData/wp14r/development-v6-ledger`. The declared experiments/configurations establish “measured traffic”; it is **simulated execution with measured-derived profiles**, not observed real pooled journeys. Current inspected source is not automatically identical to saved historical binaries. Main verifier saves initialization-manifest hashes; raw manifests preserve binary/configuration identifiers.

**O4 — every budget-use row.** Time values below are seconds among **S>0** riders; quantiles use nearest-rank `sorted[ceil(q*n)-1]`. Exposure/near-cap/multiple counts use all completed riders. All counts and unrounded data are in the linked main JSON/TSV.

| Population / arm | Riders | S>0 (# / %) | Mean / nearest-rank p50 / max S | ≥90% B | ≥2 nonzero c | Verdict against fact-pack |
|---|---:|---:|---:|---:|---:|---|
| w07 U | 665 | 11 / 1.65% | 74.7 / 68.3 / 208.2 | — | 0 | **MATCH** |
| w07 C-30 | 660 | 2 / 0.30% | 6.0 / 2.0 / 10.0 | 0 | 0 | Counts/mean/max **MATCH**; “median” **MISMATCH** under ordinary median, **MATCH** as nearest-rank p50 |
| w07 C-60 | 661 | 3 / 0.45% | 18.0 / 10.0 / 41.9 | 0 | 0 | **MATCH** |
| w07 C-90 | 664 | 7 / 1.05% | 49.7 / 68.3 / 86.9 | 1 | 0 | **MATCH** |
| w07 C-120 | 666 | 9 / 1.35% | 56.2 / 68.3 / 96.7 | 0 | 0 | **MATCH** |
| w07 C-150 | 666 | 9 / 1.35% | Identical rider budget vectors to C-120 | 0 | 0 | **MATCH** |
| w07 C-180 | 666 | 9 / 1.35% | Identical rider budget vectors to C-120 | 0 | 0 | **MATCH** |
| w07 C-240 | 665 | 11 / 1.65% | Identical rider budget vectors to U | 0 | 0 | **MATCH** |
| w07 C-300 | 665 | 11 / 1.65% | Identical rider budget vectors to U | 0 | 0 | **MATCH** |
| T3.8 U | 2,434 | 174 / 7.15% | 137.7 / 117.0 / 590.1; p90 260.7 | — | 12 (0.49%); max 3 | Counts/mean/max/p90 **MATCH**; “median” **MISMATCH** under ordinary median, **MATCH** as nearest-rank p50 |
| T3.8 C-30 | 2,338 | 33 / 1.41% | 10.9 / 8.3 / 29.2 | 4 (0.17%) | 0 | **MATCH** |
| Pickup dispatch budget | Every rider in every arm audited for this table has S_pickup=0 | | | | | **MATCH** |
| T3.8 U would exceed B=30/60/120/300 | 5.9162 / 5.3410 / 3.5333 / 0.4930% | | | | | **MATCH** to 5.92 / 5.34 / 3.53 / 0.49 |

Quantile correction is material at small n: w07 C-30 has exactly **1.974 and 10.048 seconds**; conventional median = **6.011**, not 1.974. T3.8 U's conventional median = **117.4215**, nearest-rank p50 = **116.975**; rounded to one decimal these are 117.4 and 117.0. Relabel the column “nearest-rank p50” rather than silently redefining median. Grouped “identical” rows were tested using matching (cell, rider ID) and **exact millisecond S/drop, S/pickup, change-count vectors**; all four comparisons match. This is not a claim of byte-identical transcripts/routes.

At C-120 on measured w07, 657/666 riders spend zero; exposed mean spending is 56.18 s; maximum 96.738 s uses 80.6% of B. Nobody reaches 90%. At C-150/180 the observed budget distribution does not change. At C-240/300 it matches U. Thus wider bounds are mostly inactive on this panel, and service is not monotone (666 at 120 versus 665 at 240). These eight morning cells cannot answer C-120's effect on all other T3.8 windows.

**An additional finding, with scope separated.** The fact-pack's “cumulative rarely exercised” conclusion holds strongly for measured w07/T3.8 C, but “never under any C anywhere” would be false. The extra raw audit finds:

| Saved corpus / arm | Served / exposed | ≥2 changes | Max changes | Interpretation |
|---|---:|---:|---:|---|
| WP14r C-120 | 1,563 / 41 | 1 | 2 | Accumulation exercised, rarely |
| WP14r FREE | 1,629 / 388 | 50 | 3 | 13 riders pass every individual 120-s step but exceed 120 s cumulatively |
| Synthetic C-120 | 1,205 / 28 | 2 | 2 | Additional cumulative examples; synthetic, not full measured panel |

[Exact witnesses](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-cumulative-witnesses.json): WP14r FREE rider `rq-1c726f7b…` has positive c=91.010 +117.780 = **208.790 s**; each step individually ≤120 s. A C-120 WP14r rider has 25.661 +5.924 =31.585 s; a synthetic C-120 example has 81.952 +10.017 =91.969 s. These establish a mechanism distinction and show accumulation is sometimes used. They **do not** establish how a single-step-only policy would dispatch, what it would serve, or a causal business advantage over that policy. Exact policy ablation requires different trajectories, hence new future runs.

The original extra JSON's field `nonzero_traffic_entries` was overly named: it counts **nonzero exogenous ledger differences x**, including static timing/rounding effects. [v2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-extra-raw-verification-v2.json) corrects that name without rereading/replacing inputs. WP14r fixed traffic can have sub-second negative x; the [earlier raw audit:7](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round9-ladder-reproduction-2026-10-08.txt:7) and [snapshot audit:84](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round9-static-snapshot-verification-2026-10-08.txt:84) establish this. Do not turn the x count into a claim of congestion updates.

## 2. Seven directions, ranked

Effort estimates are planning judgments, not measured execution times or guarantees. All numerical success/kill thresholds below are proposed **decision criteria**, not achieved results or unseen-outcome preregistrations. Any future selection must freeze fit/calibration/test choices before new results. T0=existing-record analysis; T1=existing-code/config runs; T2=core implementation + meaningful tests; T3=new data pipeline. **Runs executed now: zero.** Future counts mean new simulation trajectories; repeated microbenchmarks and model fits are identified separately.

### Rank 1 — P1: allocate dispatch-change budgets by trip length, measure the frontier

**Idea / questions:** replace one global B with a frozen per-rider allowance based on prequote direct-trip time, while preserving Σ|c| accounting; answer O2/O3/O4/O6.

**Beneficiary and evidence:** operator seeks more feasible/served requests at a documented reliability cost; rider gets an explicit relative burden limit. Molenbruch's relative ride-time service limits and cost curves motivate this axis, and Schulz/Pfeiffer links relative detour to modeled offer acceptance ([survey A/C](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md)). No measured customer preference for this particular budget exists.

**New versus closest prior:** relative detour budgets are old. The candidate extension is allocating **dispatch-change** allowance on a per-rider cumulative ledger with traffic separation, and testing it at comparable offered budgets. Do not claim new proportional service limits, fairness superiority, profit or a recovered customer merely because a saved candidate passes.

**Already / needed:** [budget diagnosis:1](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/budget-block-diagnosis-2026-10-07.txt:1), [first-order proportional screen:1](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/proportional-budget-screen-2026-10-07.txt:1) reports 30 versus 11 passing requests at mean60, 89 versus59 at mean120; this uses current served-cohort mean direct time and ignores cascades. Main raw audit demonstrates C-120 morning headroom. Need an independently reconstructed screen from candidate witnesses, then a real per-rider-budget contract, full trajectory comparison and common-rider plus all-request outcome reporting.

**Feasibility:** T0 gate **8–12 h, 0 runs**; T2 implementation/tests **24–40 h**; T1 confirmatory pilot **16–24 h, 32 future runs** (uniform60 and a proportional-mean60 policy ×16 held-out cells; reuse an archived control only if its scenario/runner/configuration match), optionally **68 additional runs** for those two policies over the full34 panel only if the pilot clears. Budget rule example: B_i=clip(k·direct_i, lower, upper), fixed at first confirmation using available routing information. Choose k/clips on earlier fit cells; define offered budget for all requests before service selection. Report test mean mismatch; do not normalize on future served outcomes or claim equal-cost comparison when observed offered means differ materially.

**Prediction / kill:** aim for ≥1 percentage point more of all requests served than a uniform comparator with test offered-mean budget within5%, while increasing common-rider late>60s by ≤0.5 pp, zero C certificate breaches, and explicitly reporting long-trip burden tails. Kill the claimed improvement if any gate fails, if benefit vanishes after proper mean/cohort matching, or if reconstruction shows the screen was an artifact. These margins are design choices; sensitivity curves must accompany them.

**Storyline:** **extend** the current C+forecast+ledger story with choosing who receives how much controlled dispatch flexibility. Do not spend five weeks on a learned allocator or price/demand model.

### Rank 2 — P2: optimize repeated candidate schedule/commitment evaluation

**Idea / questions:** reuse only a proven unchanged prefix and recompute the affected suffix of nearby insertion candidates, accelerating evaluation while preserving full-validator results; answer O2/O6 in the example-thesis style.

**Beneficiary and evidence:** operator/researcher gains lower decision CPU/latency or more candidates within a compute budget. The example thesis compares pruning/response time with service, and Schulz/Pfeiffer explicitly reduces offer-computation effort ([survey A](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md)). This is a computational benefit; increased revenue is unmeasured.

**New versus closest prior:** Gschwind/Drexl already optimizes exact insertion feasibility. Current RideBound already has exact same-state/route cache reuse: [ForwardSlackProfileCache:477](C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/ForwardSlackProfile.cs:477), [evaluation/cache use:709](C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs:709). A new contribution would be a verified **incremental adaptation for this commitment model**, measured against the current cached implementation. No “first cache,” no unproved constant-time test, no imported 3.8× speed claim. The travel contract need not satisfy triangle inequality.

**Already / needed:** source above, archived decision/candidate/ledger records, [claim boundary:95](C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md:95). Need a profiler, replayable evaluation fixtures, dependency/invalidation rules for frozen prefix, travel snapshot, vehicle progress, time windows/dwell and policy state, and differential validation against the complete evaluator. Historical binaries must be pinned for the baseline.

**Feasibility:** T0 profiling/replay selection **8–12 h, 0 simulations**; T2 implementation/differential tests and microbenchmarks **32–56 h, 0 simulations**; T1 operational confirmation **8–16 h, 16 future runs**. Microbenchmarks use ~20 repeated process measurements per frozen workload, same hardware, warmup/counters; these are not additional dispatch simulations. Instrumentation/build/testing would occur only in later authorized implementation work, never this round.

**Prediction / kill:** proceed only if the targeted work is ≥20% of decision CPU and repeated compatible subroutes exist. Target ≥25% lower paired median decision CPU and no worse p95, with **zero** feasibility/promise/certificate/output-decision differences under an exhaustive candidate budget. Fixed wall-clock search is a separate trade-off experiment, where routes may differ but C must still hold. Kill on any unexplained differential mismatch, absent hotspot, or <10% end-to-end gain. If the small corpus is too cheap, do not advertise production throughput.

**Storyline:** **extend** C+forecast by making certified pooling computationally cheaper; alternative to P1, not a mandatory second project.

### Rank 3 — P0: keep the current storyline unchanged

**Idea / questions:** retain the existing cumulative C, simple traffic-aware quote and cause ledger, with tighter empirical/novelty boundaries; answer O2/O3/O6.

**Beneficiary and evidence:** operator gets enforceable dispatch self-restraint and auditable causes; researcher gets a reproducible separation experiment; rider-facing benefit is measured promise lateness among served simulated riders. External reliability relevance is supported by Fielbaum/Alonso-Mora, DoorDash and pooled stated preference ([survey B/C](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md)).

**New versus closest prior:** narrowly the path-dependent cause-separated budget/certificate and its implementation/evaluation. Not insertion, time consistency, forecast ETA or demonstrated profit. This is an honest undergraduate systems/research contribution, not proof of industry-optimality.

**Already / needed:** main/extra raw audits, [Round12 fact audit](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md), [forecast report:37](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md:37), and [claim boundary](C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md). Need publication-quality definitions, all-request service cost, common-rider comparisons, the accumulation witnesses and limitations; no new experiment is required for descriptive claims.

**Feasibility:** T0 **16–24 h, 0 future runs**, plus thesis writing time outside these analytical estimates. This is the safest deadline fallback.

**Prediction / kill:** independent final checks retain zero audited C breaches/forced decisions and the documented coverage/reliability trade-off. Kill strong cumulative-effect or business-profit claims now: measured C does not exercise repeated spending, no user model exists. If certificate semantics or ledger reconstruction fail, repair the core claim before submission; writing alone cannot fix it.

**Storyline:** **unchanged**, with honest wording and no new method branch.

### Rank 4 — P3: promise a frozen arrival window rather than one exact minute

**Idea / questions:** quote a calibrated arrival interval, retain C for controlled dispatch movement of its anchor/endpoints, and measure window width versus misses and service; answer O2/O3/O6 with a genuinely different promised object.

**Beneficiary and evidence:** rider can plan using disclosed uncertainty; operator can expose uncertainty and price operational flexibility. These are design hypotheses supported by Rauh/Schulz window models, pooled distribution-valuing stated preferences, and Uber/DoorDash quantile work ([survey A/B8/D](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md)); acceptance of our windows is unmeasured.

**New versus closest prior:** windows/quantiles/CQR are established. Potential contribution is a frozen uncertainty statement combined with the separately certified dispatch budget, tested against equal-width or equal-upper-end controls. Not a new conformal method or guaranteed conditional coverage in snow.

**Already / needed:** archived C-30 initial quotes/arrivals, [chronological input/calibration protocol](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md), CQR primary theorem in survey D. Need calibration on earlier distinct days, record no-peeking, early/late miss rates, mean/p90 width, subgroup coverage and warnings when the forecast regime shifts. Replay is an interface comparison; enforcing interval endpoints in dispatch changes trajectories and needs separate validation. Existing pickup-display feasibility conflicts must be repaired before operational claims.

**Feasibility:** T0 interval replay **16–24 h, 0 simulations**; optional T2 interval contract **24–40 h** plus T1 **8–12 h, 16 future runs**. Eight traffic days restrict calibration credibility; a many-week human/data validation would be T3 and is outside this minimal option.

**Prediction / kill:** at the same upper-end quote extension, aim for ≥90% held-out arrival coverage with mean width ≤60s and no subgroup below80%, while reporting both early/late misses. Kill if attaining coverage needs much wider offers than a constant-window baseline, or interval miss rates grow in incidents without a disclosed warning. Thresholds are exploratory; correlated-day data cannot establish a universal90% guarantee.

**Storyline:** **replace the point-promise presentation**, retain C+traffic separation underneath. This is a larger product/concept change than P1.

### Rank 5 — P4: execute the already specified damped-forecast challenger

**Idea / questions:** compare a causally observed damped residual trend with the existing historical congestion shape at matched quote/early-arrival cost; answer O3/O6.

**Beneficiary and evidence:** operator/rider may gain more reliable first quotes in changing traffic, an established forecasting goal (survey B4/D); no gain is assumed. Normal-day headroom is already small.

**New versus closest prior:** Gardner–McKenzie damped trend and live-corrected history are prior; the contribution would be a null/positive adaptation study under controlled C. Do not call it new ML or unseen-outcome preregistration.

**Already / needed:** [exact Round12 protocol](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md), [snapshot-only spot check](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round12-snapshot-proxy-check.txt:1), [forecast headroom/caveats](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:43). Need full-panel information gates and one fixed chronological calibration; do not feed latent current/future factor files to the online challenger.

**Feasibility:** T0 **12–20 h, 0 simulation runs**, 36 small parameter fits per the existing protocol. No change to dispatch trajectories.

**Prediction / kill:** use the existing protocol's thresholds/guardrails unchanged; an incident benefit of ≥1 pp late>60s would be interesting only if its quote-cost/early-arrival guardrails pass. Kill superiority if historical baseline remains tied/better or input/provenance gates fail. Do not retune after seeing the snow result.

**Storyline:** **extend** the forecast evaluation, leaving core C and promises unchanged. Low expected novelty; economical auxiliary experiment.

### Rank 6 — P5: make a promise with a priced compensation exposure

**Idea / questions:** evaluate an arrival or pickup deadline plus a hypothetical future-use credit, using the ledger for audit but charging the rider-facing miss independently of who caused it; answer O2/O3/O6.

**Beneficiary and evidence:** operator can quantify credit liability; rider gets an explicit remedy. Via field experiments support targeted future credit after long **waits**, not long travel; Lyft/Grubhub show current qualified guarantees ([survey B2/D](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md)). This is stronger evidence for pickup than for our tiny drop drift.

**New versus closest prior:** compensated guarantees and proactive credits are old. New work would only be a liability/service/quote frontier under C and forecast with auditable eligibility. Do not claim optimal pricing, increased retention, realized credit redemption or profitability without offer/request/use behavior.

**Already / needed:** saved first quotes/arrivals and cause ledger; current pickup locks; primary policy qualifications in survey D. Need freeze a clear deadline/miss rule (e.g. >60s) and credit schedule, report face-value credits per100 requests and per100 served, missed-pickup/drop distinctions, quoted-duration cost and refused demand. Treat nominal credit exposure as a bound, not cash expense; no actual credits are issued.

**Feasibility:** T0 liability replay **12–20 h, 0 runs**; making a deadline influence acceptance/dispatch would require T2 **24–40 h** and T1 **16 future runs**. Human conversion/retention validation is a separate unavailable project.

**Prediction / kill:** ask whether C+forecast reduces nominal credit exposure by ≥25% versus uniform padding at equal mean quote extension, after displaying all-request service differences. Kill the business-profit conclusion without behavioral data regardless of this result; kill the operational comparison if gains come only from later deadlines or rejecting riders.

**Storyline:** **extend** the same reliability story with an explicit liability consequence; use pickup as a separate product comparison, not a disguised claim that drop-C improves pickup.

### Rank 7 — P6: add a many-week public-trip duration benchmark

**Idea / questions:** train a small chronological pooled-duration quantile model on NYC HVFHV and compare against OD/time-bin empirical quantiles; answer O5/O3/O6.

**Beneficiary and evidence:** researcher/operator gains a better tested auxiliary timing distribution if it transfers; exact public schema and limits are in [survey E](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md). More calendar weeks can improve evaluation diversity, not necessarily model quality.

**New versus closest prior:** public-trip ETA/quantile modeling is established (Uber/DoorDash, survey D). Potential contribution is an honest external timing/transfer audit of the simple forecast. Not a directly learned C budget, promise-error predictor, real dispatch-policy evaluation, or recovered Manhattan factor series.

**Already / needed:** verified dictionary/download links; metadata/sample 403s explicitly recorded; only eight FleetPy factor days currently in hand ([Round12 F4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:43)). Need target-year schema/precision/missingness checks, lawful public-file retrieval, deduplication, causal feature definitions and train/calibration/test weeks. For 2018 use taxi duration/demand data; HVFHV begins later, so report temporal/domain shift.

**Feasibility:** T3 **40–64 h, 0 simulation runs**, approximately **6 offline model fits** (baseline and simple quantile learner across three chronological folds), initially 8–12 weeks if resources permit. Converting predictions into live routing/certification would add T2 and new trajectories; excluded from this option.

**Prediction / kill:** target ≥10% lower held-out pinball loss versus empirical-quantile baseline with comparable calibration on shared-intent trips. Kill direct thesis integration if historical fields are missing, gains use post-outcome sharing/distance, or no validated mapping to the simulator's factor exists. An external duration result can remain an appendix without expanding the core thesis.

**Storyline:** **extend only as an auxiliary benchmark**; replacing the current story with public-data ML risks the deadline and the novelty boundary.

## 3. Trả lời trực tiếp O2 và O3

**Nếu chỉ có luật C, nhà vận hành được gì?** Họ có một giới hạn kiểm tra được cho phần thay đổi lời hứa do chính quyết định điều phối gây ra. Có thể chọn mức B và biết mình đánh đổi bao nhiêu khách được chở để giảm phần bất ổn đó. Trên 34 ô T3.8, C-30 chở 2.338 thay vì 2.434 khách: mất 96 khách, tức 2,61 điểm phần trăm trên toàn bộ 3.672 yêu cầu. C không có quyết định bị ép trong dữ liệu kiểm tra. Đây là lợi ích về kiểm soát và kiểm toán chất lượng dịch vụ; chưa phải bằng chứng tăng doanh thu, giảm hủy chuyến hay tăng giữ chân khách. [Số liệu gốc kiểm lại](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-raw-verification.json); [so sánh các luật, handoff:166](E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md:166).

**Người nghiên cứu có muốn tối ưu không?** Có lý do rõ để nghiên cứu đường đánh đổi giữa chất lượng lời hứa, số khách phục vụ và chi phí tính toán. Fielbaum/Alonso-Mora đã làm điều này với bất ổn do hệ thống; DoorDash cũng kiểm soát độ ổn định ETA. Nhưng không thể nói cộng đồng đã chấp nhận đúng Σ|c| là mục tiêu tốt nhất. Đặc biệt, luật cộng trị tuyệt đối cả thay đổi sớm lẫn muộn; cần giải thích vì sao “sớm hơn” cũng tiêu ngân sách, thay vì mặc nhiên coi hai phía gây hại như nhau. [Nguồn và giới hạn, survey B4/C](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md).

**Thêm dự báo thì được gì?** C xử lý phần do điều phối; dự báo xử lý tắc đường có thể dự đoán để lời hứa đầu thực tế hơn. Bảng đã lưu trên 34 ô báo tỷ lệ trễ hơn lời hứa đầu trên một phút: U 8,34%, C-30 3,25%, C-30+dự báo 0,43%. Dự báo này chủ yếu sửa lời hứa hiển thị, không làm xe đi nhanh hơn. Vì vậy phải báo cả mức lời hứa dài thêm, tới sớm và số khách bị từ chối. Không được coi giảm “trễ so với giờ báo” là giảm thời gian di chuyển thực tế. [Bảng nguồn:194](E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md:194); [đối chứng cùng giá và chi phí lời hứa:37](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md:37). Với tuyết bất ngờ, kết quả yếu hơn; dự báo không thành bảo đảm tới đúng giờ.

**Khách quan tâm điều gì có thể nói chắc?** Bằng chứng cho thấy thời gian chờ, độ tin cậy của thời gian đi và giá tiền ảnh hưởng lựa chọn; một số biện pháp bù cho chờ lâu có tác dụng trong thí nghiệm Via. Chưa có bằng chứng khách quan tâm việc hệ thống “tiêu 30 giây ngân sách” hay chấp nhận trễ do giao thông vì đã phân loại nguyên nhân. Với khách, đến muộn vẫn là đến muộn. Vì vậy nên trình bày kết quả bằng giờ đến thực, sai số với lời hứa đầu, số lần thay đổi đáng kể, độ dài lời hứa và khả năng được phục vụ; ledger giải thích và kiểm soát phía sau. Việc đọc ledger thành trải nghiệm khách là một suy luận thiết kế cần kiểm chứng, không phải kết quả khảo sát. [Survey B1/B2/B8/D](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R13-SURVEY-CODEX.md).

**Có phải đóng góp thật không?** Có, ở mức một cơ chế cộng dồn có tách nguyên nhân, thực hiện và kiểm chứng được, cùng phép đo đánh đổi có thể tái lập. Đóng góp hẹp hơn “thuật toán đầu tiên đảm bảo độ tin cậy”. Các ví dụ mới cho thấy cộng dồn khác giới hạn từng lần về mặt cơ chế; chúng chưa chứng minh lợi ích vận hành riêng của cộng dồn. Đây là nhận định đánh giá về phạm vi đóng góp, dựa trên kiểm tra và đối chiếu prior work ở trên.

**Điểm yếu hội đồng dễ đánh nhất:** “Trong thí nghiệm chính, mỗi khách dưới C bị đổi do điều phối nhiều nhất một lần. Vậy vì sao cần cộng dồn? Độ tin cậy tốt có phải do ghép ít hơn, từ chối nhiều hơn, dùng mô phỏng gần tất định và báo giờ muộn hơn? Doanh nghiệp có lời không?” Câu trả lời phải thừa nhận chưa có thí nghiệm chính tách được lợi ích cộng dồn, chưa có mô hình phản ứng khách/doanh thu, và chỉ có một tuần giao thông với ít ô độc lập. Nêu rõ các giả định dừng đón trả bằng 0, hệ số giao thông chung, sai lệch chọn chuyến và nhóm khách được phục vụ. Forecast display còn có 34/1.471 lời hứa đón vượt hạn đón cũ, nên chưa sẵn sàng tuyên bố triển khai. [Round12 F1/F2/F4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md); [forecast feasibility:68](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md:68).

**Lựa chọn của tôi:** giữ một câu chuyện: kiểm soát phần lời hứa mình gây ra, dự báo phần có thể biết trước, đo phần còn lại và giá phải trả. Nếu cần thêm một cải tiến, thử P1 có cổng dừng rõ ràng; nếu không vượt cổng, P0 vẫn là lựa chọn có căn cứ. Không cần biến khóa luận thành một dự án ML lớn để chứng minh rằng đóng góp hiện tại có giá trị.
