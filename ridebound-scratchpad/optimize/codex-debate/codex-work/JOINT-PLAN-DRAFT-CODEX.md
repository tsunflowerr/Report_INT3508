# Round 5 — proposed joint plan

2026-10-07. The deliverable is **one audited service–promise frontier**, with a calibrated display rule and clearly separated contract semantics. Calibration comes first because its screen costs no dispatch jobs; the cap sweep supplies the physical-policy comparison. Forecasting and padding alone are outside the novelty claim. Primary-source checks and independently reproduced evidence are in [REVIEW-OF-CLAUDE-BY-CODEX.md](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/REVIEW-OF-CLAUDE-BY-CODEX.md).

## 1. Promise problem definition — seven sentences

1. At commitment, the rider receives the agreed pickup window and an estimated drop quote `F0=P0+b_fc+q`, where P0 is the internal first drop projection, b_fc is the documented historical-profile extension, and q is a separately recorded deliberate reserve.
2. At revision j, `v_j` is the previous internal publication, `e_j` is the kept-plan projection under current conditions, `p_j` is the chosen projection, and `x_j=e_j−v_j`, `c_j=p_j−e_j`, `z_j=p_j−v_j=x_j+c_j`.
3. The controllable commitment is a per-rider cap `C=Σ|c_j|≤β` on the specified ETA coordinate and any explicitly included dimensions, with structural pickup/ride constraints and exceptions recorded by the existing certificate machinery.
4. The drop quote F0 is an estimated service reference rather than an unconditional arrival deadline, while actual lateness `A−F0`, visible variation and the operator's accumulated C cost remain separately reported.
5. The primary replay extends only the drop quote, preserves the pickup-window contract, and uses a frozen rider-specific offset on subsequent displayed drop projections for a stable-display comparator; recomputed forecasting is a separate replay whose visible variation must be audited.
6. The identity `A−P0=b_fc+q+Σc_j+R`, with `R=A−F0−Σc_j`, is signed accounting, and R is a forecast-relative residual rather than automatically traffic or an excuse.
7. An explicit incident policy may exclude genuinely beyond-control, unanticipated events from a responsibility KPI, while all experienced lateness remains in the raw service KPI and ordinary forecast error does not become an excuse by definition.

This definition distinguishes internal P and displayed F. A future live implementation must retain both references and certify the contract it actually enforces; current Family A supplies replay-derived display/accounting, not an already integrated forecast-visible ledger ([forecast_family_a.py:84–99,134–138](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/forecast_family_a.py:84)). Signed combined accumulation reproduces Mplus; absolute combined accumulation reproduces V, subject to identical epochs and recovery rules. Keep these as comparators rather than calling either a new combined rule.

## 2. Resolution of the ranking and scope disagreement

**Accept Claude's calibration-first ranking.** The required screen reproduces, and at mean extension **90.229 s** the room policy has **48 late / 2,386 timely riders**, versus **74 / 2,360** for matched-mean uniform padding ([reproduction:14,18](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round5-reproduction-2026-10-07.txt:14)). The room policy also has greater tail extension, so this is a reason to investigate an allocation frontier, not declare a winner. Merge the rule families, include simple competing risk features, and fit chronologically.

**Accept a full-panel narrow C sweep instead of my large six-cell C/M grid.** The existing C-30 service gap is **96 riders over 34 cells**, concentrated in the later windows ([T38 report:49–52](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md:49)). A few pilot cells are useful for input/runtime checks but weak for estimating that small gain. Start with C-60/C-120 on the complete existing panel; make C-300 conditional. Withhold a new C-versus-M efficiency claim at a cap that lacks matched M results.

**Accept density before fleet-only tuning, and defer the C-30 hybrid.** That changes my round-4 ranking. Density is still a hypothesis requiring controlled geometry and demand composition. The new revision-level screen finds only **two C-30 chosen new deadline violations at S=60 s**, versus **2,712 joint reference/candidate failures** ([reproduction:58](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round5-reproduction-2026-10-07.txt:58)); that is a poor immediate use of the remaining time. A loose-C history can be screened later without authorizing a hybrid run now.

**Reject monotonicity and the universal crossover.** The development sweep is already nonmonotone ([W07X:25,28](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/w07x/W07X-REPORT.md:25)). Our in-sample matched-cost envelope places C/U at **2,338/2,335 timely for E=40 s** and **2,338/2,342 for E=50 s**, not a universal boundary at 60 s ([reproduction:44–47](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round5-reproduction-2026-10-07.txt:44)). Treat timely as reference-relative fulfillment, with tolerance and quote-cost sensitivity.

## 3. Ranked work sequence, cost, and stopping rules

All costs below are **proposed job arithmetic**, not runs already performed or elapsed-hour estimates. One job is one arm × one episode × one repeat. Numerical targets below are proposed screens to freeze before evaluation; they are not estimates of rider welfare.

### 1 — Complete the chronological calibration frontier (0 dispatch jobs; week 1)

The independent reproduction and source checks are complete. Next compare

`F0=P0+λ(D0−P0)+min(b,a·max(0,room))`

with explicit uniform, horizon-proportional and calendar/allowed-ride-time baselines. Uniform padding uses its own branch `q=b`, avoiding an ambiguous infinity-times-zero expression. Use a modest finite search: proposed `λ∈{0,1}`, `a∈{0.25,0.5,1}` and `b∈{0,15,30,60,120,180} s`, plus the explicit baseline families; disclose duplicate rules. The objective is maximum reference-relative timely completions/request at proposed mean-extension budgets **E∈{15,30,60} s**, with p90 extension, early arrivals and variation reported as additional costs.

Fit on 14 November, freeze the selected rules, and evaluate unchanged on 15 and 16 November. Report the incident day separately. Weekend forecasting is inactive under the causal source rule; report a declared fallback and optional transfer stress, rather than claiming independent weekend calibration. Do not rescale a deployment rule to the evaluation days' mean using future promises, and do not tune with their arrivals. A retrospectively cost-matched envelope is a separate descriptive result. Because these days have already informed the research, call this a **chronological backtest**, not a fresh holdout.

Compute late/early shares at proposed tolerances **30/60/120 s**, two-sided accuracy, full quote horizon, mean/p90 extension, visible variation, completion share, and common-rider outcomes. Audit quote cost for all initially promised riders, including any who do not complete; separately report the served-only version and total extension/request. Identify every denominator and report day/window summaries alongside pooled counts.

**Kill criterion:** retain a room-specific predictive claim only if the frozen rule lowers late share on both forward weekday evaluations within the declared cost constraint, improves on the simple horizon/ride-time controls, and keeps early/variation increases within proposed **1 pp** guardrails. A p90 trade-off must be disclosed; a claimed dominance is killed by a worse cost dimension. If those conditions fail, retain the descriptive calibration frontier and remove the room-specific superiority claim. Sparse independent days preclude a strong coverage guarantee even if the screen passes.

### 2 — Freeze attribution and comparability checks (0 dispatch jobs; week 1)

Use the independent [rider cache](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round5-rider-records-2026-10-07.json) and raw transcripts to audit room against horizon/allowed ride time, previous-publication accounting, source profiles, quote recipients, and common served sets. Preserve raw experienced lateness and keep forecast extension, deliberate reserve, signed dispatch revision and residual separate. Review the saved incident/event evidence before applying any responsibility exclusion.

Document fixture selection, source time windows, selected-trip duration bias, anchor configuration, measured-factor provenance, dwell behavior and assignment differences. Room is a feature, not a bound on traffic-inclusive deterioration. Screen any later hybrid at the revision level using `e≤P0+S<p`, candidate rescue, and both-fail cases; do not interpret a chosen-history screen as counterfactual routing.

**Kill criterion:** if record identities, chronology, reference semantics or cost denominators cannot be reconciled, stop the affected predictive/contract claim and repair the accounting before requesting runs. If residuals cannot be tied to explicit qualifying incidents, keep them labeled residuals rather than excusable traffic. An unchanged service count does not establish identical chosen routes or identical promise contracts.

### 3 — Validate coherent window-start calibration (18 jobs; week 2)

Use the six existing cells `d20181114-s10-r3-{w07,w08,w17}` and `d20181117-s10-r3-{w07,w08,w17}` ([split:32–34,57–59](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/split-t38-v1.json:32)). Run U/C-30/Mplus-30 with coherent window-start edge calibration: **3 arms×6 cells=18 jobs**. Preserve request identities/times, selected nodes, scenario identity, placement and capacity. Keep structural **rules** fixed, including the ride/direct-time ratio; recompute travel-time-derived numeric allowances consistently with the new direct times rather than freezing a mismatched maxRideTimeMs. Verify those invariants before any job; if a normalizer redraws demand or geometry, prepare a controlled derivative first.

Declare the primary-versus-sensitivity anchor decision in advance. Record all changes in a new local manifest and retain the old panel as the historical case. Dwell remains documented rather than silently altered in this check. A separate dwell experiment is optional only if an implementation audit finds it cheap and necessary; its cost is not hidden inside these 18 jobs.

The ratio-based allowance is derived from factor-scaled direct time ([normalizer:427–445](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:427)). A prebuilt normalizer was located but not executed or provenance-checked; its output follows `--repository/benchmarks/...` ([Program.cs:91–103](E:/Code/RideBound-deadline/tools/RideBound.Wp6Normalize/Program.cs:91)). Stage the required source-identity files and a writable cache inside codex-work, verify binary/source identity, and audit derived fixture invariants before requesting dispatch jobs.

**Kill criterion:** stop generalizing the old numerical frontier if corrected calibration changes the contract ordering or exceeds proposed sensitivity bounds of **1 pp in completion share or 1 pp in late share**. This kills transfer from the old case, not the mathematical C/M/V distinction. If the selected optimizer is outside the three pilot arms, validate that winner on the same cells for **6 additional jobs**, unless it is already in the corrected full-panel sweep below.

### 4 — Complete the narrow cap/pad frontier (weeks 2–3)

Use the same frozen runner/wrappers, recovery policy and selected fixtures; change only the specified C cap. Seal predictions and the calibration-selection procedure before execution. For new cap outputs, process training-day results first, freeze any fitted display parameters, then evaluate later-day results without refitting. The full-panel frontier is an internal model comparison; reusing familiar episodes does not make a new population holdout.

| Input decision | Initial C-60/C-120 stage | Conditional C-300 addition | Cache qualification |
|---|---:|---:|---|
| Retain original input calibration | **68 new jobs** | **34 new jobs** | Existing U/C-30 are controls; existing Mplus-60 permits that matched comparison. |
| Adopt corrected calibration | **136 jobs total** for U/C-30/C-60/C-120 | **34 additional jobs** | The anchor pilot supplies 12 U/C-30 jobs, leaving **124** after that pilot; its 6 Mplus-30 pilot jobs are outside this four-arm total. Expanded four-C-plus-U core is **170 jobs total**, before M comparators. |

The original-world narrow core therefore costs **18 anchor jobs + 68 cap jobs = 86**, or **120** with C-300; add the winner's 6-job anchor check if needed. Under corrected calibration, the initial anchor-plus-core cost is **18+124=142**, or **176** with C-300. These are alternative cache outcomes, not costs to add together.

Run C-300 only if at least one initial cap recovers a proposed **24 completions** relative to C-30 but the service/quote-cost frontier remains unresolved. The development behavior does not justify a monotonicity prediction. For a new family-comparison claim, matched Mplus-120 costs **34** jobs, and matched Mplus-300 another **34**; corrected inputs also require new matched Mplus-60 (**34**) because its old cache is invalid. Defer these additions unless that comparison is necessary to the intended claim. A chosen-history screen alone cannot prove two absent policy runs would coincide.

**Prediction to seal:** at least one initial C cap recovers **24 completions** versus C-30 and produces a nondominated point in timely service, mean/p90 quote cost, visible variation and overrides. For tail scoring, report raw and displayed late120 separately; do not switch the reference after seeing results.

**Kill criterion:** retire individual dominated/infeasible candidates; retire the expanded cap-tuning direction if no tested candidate meets that service-recovery screen or if all apparent gains disappear under cost/variation/override guardrails. Failure of C-120 alone does not imply every cap is useless. Publish the negative range result and preserve the existing contract-accountability result; do not keep expanding caps to obtain a preferred answer.

### 5 — Conditional matched-density pilot (12 jobs; week 4)

Only after the core is interpretable, build one proposed scale level **270 requests / 20 vehicles** on the same six cells and run U plus the selected C contract: **1 level×2 arms×6 cells=12 jobs**. Fix the service-node pool and nest demand identities/time distribution and vehicle placements. Compare trip composition and normalized work load; matching request/vehicle counts alone is insufficient. Reuse baseline controls only when the complete input hashes match; if the selected C baseline is missing, add **6** jobs. A second scale level would add another **12**, but is outside the initial approval request.

**Feasibility gate before this optional stage:** the current normalizer caps requests at **128**, vehicles at **32**, and nodes at **96** ([normalizer:326–328](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:326)). The proposed density level needs an audited local scaffold extension plus downstream runner/wrapper limit checks. The 12 jobs cover only a validated fixture/run design, not that development. If this cannot be completed within the week-4 allowance, defer density runs and retain small-scale generalization as a limitation; do not let scaffold work consume the thesis core or substitute a trivial scale increment and call it validation.

Use a prebuilt normalizer where possible. Any copied build, intermediate artifacts, caches, fixtures, logs and outputs must remain inside codex-work; the suggested default build in another worktree is outside current permission. If controlled nested demand cannot supply the proposed request count within fixed nodes, stop this design rather than substituting changed geography and calling it density-only.

**Prediction to seal:** realized sharing and dispatch-exposed share both increase; proposed useful-effect screens are **5 pp sharing** and **2 pp exposure**, reported with completion cost and window differences. **Kill criterion:** if those screens fail under the matched input invariants, withdraw the claim that this density change explains low pooling or amplifies the cap's usefulness. If geometry/composition cannot be matched, label the pilot a broader scale stress and do not claim causal density isolation. Fleet-only and hybrid runs are deferred beyond the core plan.

### 6 — Freeze results and prepare owner-reviewed thesis material (0 dispatch jobs; weeks 4–5)

Complete independent metric checks, all failed predictions, limitations, the contract-comparison table and the single service–quote frontier. Prepare reviewable thesis-change drafts inside codex-work. Allow the final week for owner review, revisions and documentation rather than adding mechanisms. **Kill criterion:** any unsupported novelty, causal attribution, forecast guarantee or welfare language is removed before a thesis-edit approval request.

## 4. Execution and approval constraints

The owner approves **every dispatch-run batch and every thesis edit**. Before asking for a run batch, prepare its exact local manifest, input hashes, job list/count, predictions, analysis procedure, stopping rule and estimated duration based on measured pilot scheduling. Seal that concrete plan with a local hash before its first run. This draft is not a run authorization or a completed seal.

Runs start only on AC power and stop/defer according to the existing power/STOP behavior. Use the existing runner and wrappers through adapted local orchestration; the old drivers' default output roots must not be used unchanged ([run_t38.py:53,84–103](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/run_t38.py:53)). Keep outputs and logs inside codex-work and create them exclusively; use Python `-B` and avoid import-time-writing config generators. Cache reuse requires identical fixture, world, policy, runner, seed and recovery inputs. No elapsed-hour promise follows from multiplying old job counts by an average without accounting for concurrency and larger fixtures.

## 5. Claims for the owner

| Claim now | Status | Evidence / permitted wording |
|---|---|---|
| C, Mplus and V enforce different accounting contracts | **SUPPORTED** | Signed increments telescope; C and V accumulate different absolute deltas. State evaluation and recovery qualifications, as checked in the review. |
| Current C-30 preserves operator accountability at a real service cost in the inspected panel | **SUPPORTED, model-specific** | Existing report shows the service gap and absence of non-normal C operation; comparator forced-operation behavior differs ([T38:46–64](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md:46)). This is not a guarantee against traffic lateness. |
| Room stratifies observed exposure and naive lateness | **SUPPORTED, descriptive** | All required buckets reproduce ([reproduction:7–10](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round5-reproduction-2026-10-07.txt:7)). It is known at the initial commitment/publication but not a traffic-inclusive delay bound. |
| Room padding improves the in-sample mean-cost/late-count trade-off | **SUPPORTED, qualified** | Matched-mean comparison reproduces, with a worse p90 extension ([reproduction:14,18](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round5-reproduction-2026-10-07.txt:14)). No held-out or business-optimal claim follows. |
| Display replay improves reference-relative fulfillment without faster vehicles | **SUPPORTED** | Fixed arrival times are rescored against changed promises; required results reproduce. The original forecast population/weighting differs from this full-panel pooled frontier. |
| Room adds predictive value beyond horizon, direct time and calendar | **WEAK / untested** | Needs chronological comparison with simpler controls; few independent days and prior inspection limit inference. |
| A particular cap is optimal, or the cap/pad crossover is universal | **UNSUPPORTED** | Incomplete cap grid, selected rule families, different served sets, tolerance sensitivity and absent booking response. |
| Scale/density alone explains the original sharing rate | **UNSUPPORTED as causal** | Literature supports a hypothesis; spatial/time support, selection and load are not matched. |
| Forecast residual equals legally excusable traffic | **UNSUPPORTED** | Residual accounting and incident-based responsibility are different definitions. |
| Forecasting, padding, ETA postprocessing, or the combined V/M rule is novel | **UNSUPPORTED** | Verified prior art and exact existing-arm equivalences are recorded in the cross-review. |
| The exact ledger/certificate/optimization combination is globally new | **WEAK candidate only** | This survey does not establish exhaustive prior-art absence. Describe implemented semantics and evidence instead of claiming “first”. |

The plan can unlock **a chronologically backtested promise-allocation frontier**, **a selected cap/display point within a measured model**, **sensitivity to coherent traffic calibration**, and—if the controlled pilot succeeds—**a scale-dependent operating range**. Strong external predictive, welfare or deployment claims would need new independent data and additional modeling beyond this five-week core.
