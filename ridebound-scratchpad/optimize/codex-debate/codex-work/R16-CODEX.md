# Round 16 — Codex independent review and proposed next step

2026-10-10. **Q1: Yes, a better research direction exists than only reorganizing the existing results.** I now rank a bounded **selection-objective × cap experiment** ahead of the zero-run chapter, if the remaining time supports one engineering study. Keep C + traffic-aware quoting + the ledger as the experimental backbone; change the research question to whether the dispatch budget remains useful when the dispatcher prioritizes cost over stability, and whether relaxing it buys useful service. This promotes the former optional cost-first study into the main research test. It is not evidence that cost-first is already a better algorithm. The zero-run chapter remains the completion fallback.

**Strict-venue verdict on the current evidence: REJECT as a top-venue research submission in its present form; a bounded undergraduate systems thesis remains defensible.** That is my review judgment, not an institutional decision. The problem is limited demonstrated incremental significance and weak regime and generalization evidence, not a failure of the audited arithmetic. Details and the three most damaging questions appear below.

## Scope, independence and evidence

I read ROUND16-FACT-PACK.md and ROUND16-REVIEW-STANDARD.md first. I did not open Claude's R16/r16 files or antigravity-work, and used no subagents. I read only earlier allowed evidence, code and primary sources. No simulation, build, install, deletion or existing-file edit occurred.

This round's new computation:
- R16-cap-outcomes-v2.py independently reads all **72 existing w07 U/C transcripts**, verifies their whole-file and decoded-frame hashes (**149934 frames**), and reconstructs physical alighting minus first published drop quote, service and ledger usage. R15's independently derived pruning classification is joined explicitly; it is not recomputed by this helper.
- R16-weather-inventory.py independently inventories the existing Central Park daily NOAA CSV for a specified chronological split. It supplies evaluation strata, not quote-time weather features or traffic observations.
- The first cap helper is preserved: it failed because it assumed messageType was the first envelope key. v2 correctly handles the preceding epochId. No failed-helper output is used.

Measured means simulated execution with measured city-wide traffic factors. A screen is a calculation on recorded paths/candidates. Predictions and numerical success thresholds below are **design hypotheses**, not observed results or unseen-outcome preregistrations. Engineering-hour estimates are my judgment, not benchmark measurements. The reported five-week deadline remains UNVERIFIED (FACT:99-101).

Paths below are relative to E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate unless absolute.

| Key | Path |
|---|---|
| FACT / STANDARD | ROUND16-FACT-PACK.md / ROUND16-REVIEW-STANDARD.md |
| CAP / CAPJ | codex-work/R16-cap-outcomes.txt / codex-work/R16-cap-outcomes.json |
| WX / SCOPE | codex-work/R16-weather-inventory.txt / codex-work/R16-scope-inventory.txt |
| A15 / R15 | codex-work/R15-audit-summary.txt / codex-work/R15-CONFIRM-CODEX.md |
| SRC | C:/Code/RideBound-noworse/src/ |
| SELECT | SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs |
| D03 | E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md |
| W07X | E:/Code/Report_INT3508/ridebound-scratchpad/tang3/w07x/W07X-REPORT.md |
| FR | E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md |
| DISPLAY | E:/Code/Report_INT3508/ridebound-scratchpad/optimize/display_layer.py |
| LAD | claude-work/wp14r-ladder-reanalysis-2026-10-08.txt |
| BUD / CVP | claude-work/budget-block-diagnosis-2026-10-07.txt / claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt |
| PAD | claude-work/cap-vs-pad-frontier-2026-10-07.txt |
| REPLAY / SNAP | codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md / codex-work/round12-snapshot-proxy-check.txt |
| S1 | claude-work/r13-ml-data-samples/syed2021_DataSheet1_section1_excerpt.txt |
| FA | codex-work/r13-paper-text/Unreliability_in_ridesharing_systems_Measuring_cha.txt |
| WORLD | E:/Code/Report_INT3508/ridebound-scratchpad/tang3/world/preflight_world.py |
| MLD / SAMPLES | claude-work/R13-ML-DATA-CLAUDE.md / claude-work/r13-ml-data-samples/ |
| OWN | codex-work/R13-PROPOSALS-CODEX.md |

## Q1 — Why retain the backbone, and what should actually change?

The owner's interpretation “nothing left to optimize” does not follow from R15. R15 retained a conditional cost-first experiment and explicitly deferred unprofiled evaluation acceleration, allocation and larger forecasting/data studies. It did not establish their impossibility (R15 sections 3–4; OWN:75-103,121-184).

**My ranking changes under the requested research standard.** In R15 I prioritized safe consolidation and made the experiment optional after chapter drafting. For a strict research reviewer, consolidation cannot answer the strongest mechanism question: is the low dispatch movement mostly an effect of stability-first selection rather than incremental value of the hard gate? Source SELECT:297-331,365-368 gives that concern a concrete mechanism; the FREE/LOCKS package changes sharing from 53.1% to 21.8% (LAD:2-3). I now prefer testing that mechanism, with a relaxed-cap arm, before treating the story as scientifically finished. This is a change of research priority, not a newly verified treatment effect.

Retaining C as a controlled component is justified because its ledger/gate can be specified and checked independently of exogenous ETA movement, and existing runs exhibit real bounded trade-offs (A15:3-9; W07X:54-62). It is a useful experimental control. It is not justified by established profit, rider demand for 30 s, superior common arrival outcomes or novelty of reliability control: those are withheld by D03:54-56,211-225,236-245,260-269.

There is also a credible alternative research direction: **incident-adaptive forecasting tested on many historical event days**, using a realistic information cutoff and equal quote cost. The new NOAA inventory makes a multi-incident benchmark concrete rather than speculative (WX:6-7). But factor reconstruction, observation-lag validation and weather-vintage integration make it a larger data project. I rank it second for this deadline. Choose it instead of the selection study if forecasting becomes the owner's central scientific objective; do not run both as parallel thesis extensions.

Neither alternative is a guaranteed top-venue contribution. Replacing C with an arrival window, using an older famous dataset, or naming a standard forecast method would not itself supply originality or business significance (D03:56,211-217,236-245; OWN:121-157).

**Claim verdict: MAJOR REVISION.** The existing backbone can support a bounded thesis, but “the method is useful enough that only presentation remains” is unsupported. **Most damaging question:** what changes when the conservative objective is removed while every hard gate stays fixed? **Current evidence:** no matched answer; FREE changes the locks too.

## Q2 — Would loosening the cap improve the outcome?

### What the 1256 records do and do not mean

They are pruning records from 98 runs at multiple caps and different evolving states, not 1256 different riders or feasible assignments waiting to be accepted (A15:7,10-17). Removing the recorded budget blocker does not establish complete feasibility: the default validator is fail-fast, the candidate may have another blocked co-rider/physical constraint, and fleet selection may prefer another candidate (R15 rows 29-31; SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:222-239).

For one reported witness at a frozen state, raising B to at least before + delta removes that particular budget failure. For the measured records, delta itself already exceeds the old B. A proposal to remove all such failures across saved states is not a single trajectory-preserving change: later schedules, riders and candidate generation can change.

The T3.8 request-level screen is narrower than the full candidate collection:

| On the recorded C30 paths | Reported request identities passing the budget screen |
|---|---:|
| Raise to 60 s | 11 / 148 |
| Raise to 120 s | 59 / 148 |
| Raise to 300 s | 135 / 148 |

BUD:2-10 gives these counts, 116 of the 148 served by U, and a median smallest overshoot of 109.6 s above the 30 s cap. Thus the median best reported witness needs about 139.6 s, not merely 60 s. These are possible releases of reported blockers, not predicted completions or global upper bounds. BUD:4-5 also reports 1186 structurally attributed rejections on the observed paths. Loosening C does not directly remove those structural gates.

### Direct evidence: the eight measured morning cells

All cells are 12/13 Nov, 07–09 h, 864 requests. They are development cells, entirely distinct by date from the 34 T3.8 test cells (14–18 Nov), not eight completed C120 cells within that main panel (SCOPE:3-4). The current causal-no15 display rule is **inactive** on both dates because fewer than two earlier source days exist (DISPLAY:10-16,34-64). Consequently the existing “with forecast” display equals the original quote for every arm here. This is not evidence about a newly trained multi-year forecast.

| Cap | Served | Late >60 s, naive AND current forecast | Y60 served % | Late >120 s | Timely60 | Exposed riders | Mean / max budget used by exposed riders, s | Budget prunes / cumulative-only |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 660 | 47 | 7.12 | 2 | 613 | 2 | 6.0 / 10.0 | 142 / 0 |
| 60 | 661 | 47 | 7.11 | 2 | 614 | 3 | 18.0 / 41.9 | 106 / 0 |
| 90 | 664 | 50 | 7.53 | 4 | 614 | 7 | 49.7 / 86.9 | 71 / 0 |
| 120 | 666 | 51 | 7.66 | 7 | 615 | 9 | 56.2 / 96.7 | 38 / 0 |
| 150 | 666 | 51 | 7.66 | 7 | 615 | 9 | 56.2 / 96.7 | 26 / 0 |
| 180 | 666 | 51 | 7.66 | 7 | 615 | 9 | 56.2 / 96.7 | 18 / 0 |
| 240 | 665 | 50 | 7.52 | 9 | 615 | 11 | 74.7 / 208.2 | 6 / 0 |
| 300 | 665 | 50 | 7.52 | 9 | 615 | 11 | 74.7 / 208.2 | 4 / 0 |
| U, no drop cap | 665 | 50 | 7.52 | 9 | 615 | 11 | 74.7 / 208.2 | not audited here |

Source: CAP:3-11; means are CAPJ's S_sum_ms / exposed / 1000. Every C/U arm here has zero repeated nonzero drop-dispatch changes. Thus C30→C120 buys six served riders but also four additional late60 completions, leaving two additional timely60 completions. C120→C300 loses one served rider; no monotonic service law is established by a looser online cap.

These physical alighting metrics are not the W07X table's own-contract violation percentage or E2 variation measure. For example, W07X:25's 1.2% is the cell-mean A>120 statistic, not the new rider-pooled Y60 of 7.66%.

### Direct evidence: fixed traffic

| Arm, 1728 requests | Served | Late >60 s | Late >120 s | Timely60 | Exposed | Mean / max S among exposed, s | Possible cumulative-only prune records / decisions |
|---|---:|---:|---:|---:|---:|---:|---:|
| C30 | 1534 | 0 | 0 | 1534 | 6 | 13.9 / 27.6 | 0 / 0 |
| C60 | 1540 | 0 | 0 | 1540 | 20 | 35.8 / 57.1 | 2 / 1 |
| C120 | 1563 | 23 | 0 | 1540 | 41 | 62.3 / 119.6 | 4 / 3 |
| LOCKS, no drop cap | 1584 | 47 | 27 | 1537 | 62 | not recomputed here | not an enforced-C audit |
| FREE, different objective AND locks | 1629 | 274 | 164 | 1355 | 388 | not recomputed here | not an enforced-C audit |

Sources: LAD:2-6; the integer tail counts also match CVP:5-12's fixed-world endpoint/exposure thresholds. C ledger statistics and witness counts are independently audited at A15:3-5; means use its exposed-rider sums. All new requests associated with the six possible cumulative-only fixed records eventually completed.

C30→C60 adds six served with no late60; C60→C120 adds 23 served and 23 late60, so timely60 stays 1540. At the 120 s threshold C120 has 1563 timely completions. “Better” therefore depends on the requested endpoint. No forecast-on-fixed-world outcome is reported in LAD. Under a declared correct constant-growth profile, a display stretch would be zero; that is a mathematical limiting case, not a performed forecast comparison. Applying a varying real-day historical profile to the fixed world would be a different experiment.

### The actual full-panel relaxed endpoint is already available: U

U/C30 differ only by the drop hardLimit in the audited configuration (R15 row36; SELECT:319-331). Disabling that cap, while keeping the existing locks and stability-first objective, is the relevant observed relaxed endpoint. It is not FREE.

| T3.8, 3672 requests | Served | Late60 naive / forecast | Timely60 naive / forecast | Timely120 naive / forecast | Forecast quote extension | Exposed / repeated / max S |
|---|---:|---:|---:|---:|---:|---:|
| C30 | 2338 | 76 / 10 | 2262 / 2328 | 2327 / 2338 | 7.4 s | 33 / 0 / 29.2 s |
| U | 2434 | 203 / 137 | 2231 / 2297 | 2332 / 2347 | 7.2 s | 174 / 12 / 590.1 s |

Independent source A15:7,9; original PAD:4,12,25,33. Removing the cap buys 96 served, but produces 127 more late60 completions both with and without the existing forecast and 31 fewer timely60 completions. It produces five more timely120 without forecast and nine more with forecast. U+forecast+30 s padding produces 2328 timely60 and 2366 timely120, at a 37.2 s quote extension and 1.81% early60 versus C's 7.4 s/.17% (PAD:14,33; R15 section 2). C is not Pareto-dominant.

### Exactly what is missing for C60/C120 on T3.8

No matched 34-cell C60 or C120 trajectory exists in the verified inventory (FACT:58-61; R15 scope and A15 groups). Neither w07's two development days nor fixed traffic estimates the absent afternoon/08–10 h response.

To answer it empirically needs: a pinned runner/configuration and matched 34-cell requests/worlds; full trajectory results for each requested cap; the same quote-time forecast information/rule on each arm; first-promise alighting errors and all-request timely counts; initial promise horizons, quote extensions and early errors; served-set overlap and common-rider outcomes; absolute sharing and operating-cost extraction; acknowledged pruning witnesses plus accepted ledger histories; retention/solver diagnostics and date/source-group uncertainty. Larger caps also change who is served, so a served-only lateness percentage is insufficient. Existing C60/C120 configs are a feasibility aid, not missing outcomes.

**Claim verdict: MAJOR REVISION.** Loosening improves service in some measured comparisons, but no uniform benefit or T3.8 optimum is established. **Most damaging question:** at equal quote cost, does a relaxed cap improve timely completions per request enough to justify its extra dispatch movement? **Current evidence:** mixed endpoints above; the finite relaxed main-panel arms are missing.

## Q3 — Has accumulation had essentially no empirical effect?

**Yes, in the main measured-traffic thesis experiments, its demonstrated incremental effect is effectively absent.** Zero of 1256 recorded measured-C prunes requires prior spending to explain the reported failure; all final measured-C ledgers have zero riders with two nonzero drop-dispatch changes (A15:7,10-17). The full-trip cumulative contract is still implemented, but that is not a demonstrated cumulative-versus-per-step advantage.

Do not say “it changed only seven decisions in total” as a counterfactual upper bound. Fixed/synthetic evidence contains six/four possible cumulative-only records in four/three recorded decisions after duplicate removal; one associated synthetic new request eventually ends rejected. Those are observed witnesses/lifecycles, not effects of disabling the clause (R15 correction 1; A15:3-6,20).

The exact local condition is S_before>0, delta≤B and S_before+delta>B. Along a fixed uncapped rider history, potential disagreement occurs for max(delta_i)≤B<sum(delta_i); this is an algebraic screen, not a policy-effect theorem.

| Proposed regime | Why it could exercise the clause | What is actually established |
|---|---|---|
| More offered load / more insertion opportunities | More chances to revise the same retained rider | Not sufficient: severe load can instead cause structural rejection. A matched same-gate cost-first high-load C run is absent. |
| Cost-first selection | Removes revision penalties that may prevent repeated small changes | Source mechanism exists; no current same-gate cost-first configuration/run (SELECT:319-331; R15 section 4). |
| Longer accepted trips | More time for later compatible requests and revisits | Opportunity hypothesis; duration alone need not create changes. No controlled duration intervention has been checked. |
| Larger B | Allows an earlier change to survive, potentially leaving insufficient remaining allowance later | Nonmonotonic: a huge B never binds. C240/C300 morning arms still have zero repeats/cumulative-only records (CAP:10-11). |

**Existing runs already demonstrate the condition, sparsely:** WP14r C60/C120 and synthetic pairwise-noise C120 have recorded possible cumulative-only prunes (A15:3-6; deduplicated synthetic counts in R15). WP14r FREE has 50/1629 repeated histories and 13 rider histories whose sum exceeds 120 while no single move does; LOCKS has only three repeated histories (CVP:5-12). The older four-vehicle FREE-type WP9 panel has 38/966 repeated and ten cumulative-only rider screens at 120 (CVP:19-23). These show plausible regimes and accepted-path witnesses, not a matched effect of cumulative C. No existing run combines the proposed cost-first selector with unchanged C hard gates.

**Claim verdict: REJECT an empirical necessity/superiority claim; ACCEPT the bounded specification and witness finding.** **Most damaging question:** which outcomes would change under an otherwise identical per-step rule? **Current evidence:** not answered by a matched trajectory experiment. The thesis should withdraw this headline rather than manufacture a regime to make its preferred rule win.

## Q4 — What would cost-first selection most likely change?

The proposed order is still forced-reference avoidance → maximum new accepted requests → cost → deterministic tie levels. “Cost-first” means cost first **after those priorities**, not sacrificing safety or immediate accepted count for price. Do not merely switch the enum to RollingCost: SELECT:276-280 would lose the hard-profile forced-reference treatment. Keep the hard assessment/profile and add a narrow objective-order option (SELECT:271-331,365-385).

| Statement | Evidence class |
|---|---|
| At a frozen state, exact cost optimization over the same feasible portfolio with the same forced/accepted priorities cannot cost more than the stability-selected feasible solution with those priorities. | Conditional optimization argument. Requires optimal solver passes, equal portfolio and comparable cost units; not verified for every bounded run. |
| Stability-selected U/C may favor separate low-revision routes over cheap pooled insertions. | Code-based mechanism inference, SELECT:319-331 before :365-368. |
| Sharing and the number of dispatch-exposed/repeated riders will probably rise. | My prediction, supported directionally but not quantitatively by LAD:2-3 and CVP:5-12. |
| Served count or realized fleet operating cost must improve. | Unsupported. Changed schedules affect future feasibility, and Schedule.OperationalCost is not an audited realized distance/profit measure. |
| C's ledger must still respect B if the new selector preserves and correctly applies all hard gates. | Contract expectation under the existing validity assumptions, not a physical arrival guarantee. |
| Lateness vs first displayed quote could worsen even without C overshoots. | Mechanism hypothesis: cohort, route horizon and traffic residual change. D03:236-239 already separates C from arrivals. |

The strongest package evidence is FREE→LOCKS on fixed traffic: −45 served, −227 late60 completions and −31.3 pp sharing, before any drop budget is added (LAD:2-3). LOCKS→C30 then loses another 50 served and removes 47 late60 completions (LAD:3,6). The package therefore plausibly matters greatly. It cannot isolate cost ordering because locks, reassignment/final-confirmation behavior and historical code differ (R15 rows39-42; D03:217).

Most likely outcome: cost-first exposes a different service/sharing/revision frontier, with more opportunities to spend C and potentially worse forecast-residual arrival errors. How large, whether service improves, and whether accumulation finally binds are UNVERIFIED. Initial quote horizon must be reported alongside extension: a longer original route can make lateness look smaller without a faster trip.

**Claim verdict: ACCEPT as a testable mechanism hypothesis; REJECT “already known to be better”.** **Most damaging question:** does a matched objective-only intervention improve absolute shared completions or realized operating cost without merely rejecting riders or lengthening their initial promise? **Current evidence:** no such matched intervention exists.

## Q5 — A fair incident-forecasting study is feasible, but it needs a different evaluation design

**Answer:** optimize adaptation after evidence of a regime change and uncertainty disclosure, not an assumed ability to foresee every surprise. A delivered traffic prefix can inform new quotes after a shock starts; it cannot encode an unobserved future shock. Weather forecasts issued before the quote could help anticipation, but final daily snow/rain totals cannot. FR:102-104's snow result shows a weakness of this particular historical profile, not irreducible unpredictability for every input/model.

### Two observation contracts must be kept separate

| Contract | Allowed at quote time | Forbidden or unverified |
|---|---|---|
| Existing simulator replay | Initial current-snapshot ETA/plan; routing snapshots delivered before publication in source order; fully completed earlier training days; calendar/clock. Estimate q from the delivered matrices, under the full-panel proxy/availability gate. | Reading the current/future world factor CSV as an online feature; later snapshots/plans/actual alighting; a same-day prefix that the episode never delivered. |
| Realistic historical taxi-feed benchmark | Assume a live feed with only trips completed and delivered by t, with a registered assumed ingest lag (primary15 min; 0/30 min sensitivity, not claimed measured feed latency); lagged partial-bin summaries, counts and missingness; calendar; archived weather observations/forecasts whose availability can be established. | Full duration of a trip still in progress; final starting-bin factor f_b at bin start; same-day final weather; matched-sharing/outcome fields; pretending public monthly TLC files were a live feed. |

The first contract is supported by WORLD:13-20 and REPLAY:9-13; SNAP:2-5 checks snapshot availability on one run only. Full-panel gate status remains UNVERIFIED. The second is a proposed backtest assumption, not evidence that an operator has that live feed. TLC records are collected completed trips, per the [TLC user guide](https://www.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf), “each taxi and for-hire vehicle trip completed”.

The key target-availability problem follows directly from S1:12-16:

    f_b = sum(actual duration_i) / sum(pinned free-flow duration_i),
          over filtered Manhattan trips with pickup in bin b.

Many such trips finish after the bin. Even f_(b−1) is not safely observable by the next bin unless all required outcomes have arrived. **A fixed one- or two-bin shift is not a complete leakage solution.** Build each as-of observation from trips satisfying dropoff + declared delivery lag ≤ t; make the completed-sample count/age and censoring limitation explicit. Do not provide unseen-trip censoring labels. Pending-trip counts/elapsed times are allowed only under a separately declared started-trip feed; eventual durations are never allowed. A completed-trip proxy is not the same quantity as the final starting-bin target. That mismatch must be modeled and reported. Exact simulator snapshots are available within that simulator's contract but are more informative than this realistic historical feed.

### Rebuild the target carefully, before fitting a learner

Use raw TLC yellow trips with both endpoints in Manhattan, the same pinned free-flow network/table, zone-to-node mapping and fixed randomization as the declared reconstruction. Filter invalid times/locations and implement the declared speed filter. Syed et al.'s primary [methods](https://www.frontiersin.org/journals/future-transportation/articles/10.3389/ffutr.2021.681451/full), §5.2, says “speeds below 1 m/s or above 30 m/s”; S1:12-18 supplies the duration-weighted ratio and warns about high-demand-area weighting.

The original speed-distance definition and exact historical random mapping are UNVERIFIED (MLD:101-106). Reconstructed factors must therefore initially be called **Syed-style proxies**, not exact bundle reproduction. Compare the rebuilt 12–18 Nov 2018 series with the published series; inspect bin alignment, filtering, weighting and routing denominator. Set reproduction tolerances before comparing forecasts. If correspondence is poor, the offline forecasting benchmark may still stand on its own declared proxy, but current-simulator transfer claims fail. Freeze manifests, timezone/DST exclusions, deduplication and missing-bin rules; do not silently create 96 observations on ambiguous clock-change days.

A second sensitivity target should retain valid very slow trips: excluding speeds below 1 m/s can also remove genuine severe-congestion observations. This is a possible selection bias inferred from the filter, not a verified error in the authors' data. It matters precisely when the proposed application is incident forecasting. Also report target uncertainty and sensitivity to trip/demand mix; a city-wide taxi-weighted factor is not an exogenous, spatially uniform causal measurement of every road.

### Explicit chronological train/calibration/test plan

Proposed and not fitted here:

| Split | Dates / use |
|---|---|
| Fit | 1 July 2016–31 December 2017. Fit seasonal profiles, online residual/analog parameters and regime thresholds using rolling-origin folds inside this period. |
| Calibration | 1 January–31 August 2018. Freeze quote-cost scaling and any widening rule. Do not choose a method after seeing held-out incident errors. |
| Primary offline test | Every eligible date 1 September 2018–31 December 2019, separated into year/season/day-type and weather strata. Parameters/history library remain frozen; only the specified causal within-day observation state updates. |
| Existing simulator transfer diagnostic | The available November 2018 C/U/M⁺ journeys, with their actual delivered-snapshot information and window resets. This is retrospective: those outcomes have been inspected. It is not a new independent incident sample. |

All algorithm variants receive the same allowed history and prefix. Do not use the legacy 12/13 Nov profile to predict September/October 2018: that would use future training days. Retain it only as a later-November legacy diagnostic; the proper main baseline is a stronger historical calendar/profile model trained from the same earlier data bank.

**More than one incident test day is concretely possible offline.** My independent station inventory finds:

| Test period | Weather-flagged dates, all calendar days | Flagged weekdays | Proxy event spells | Snow ≥1 inch dates |
|---|---:|---:|---:|---:|
| Sep–Dec 2018 | 14 | 10 | 11 | 1 |
| Full 2019 | 30 | 21 | 25 | 7 |

Source WX:3,6-7; flags are snow ≥25.4 mm OR rain ≥20 mm. Spells merge flagged dates ≤2 calendar days apart. The seven 2019 snow dates are Feb12, Feb20, Mar1–4 and Dec2, with four snow-containing proxy spells. These are **weather opportunities, not proven traffic incidents or 36 statistically independent storms**. Reconstruct the associated traffic series; report all dates and failures, not just days where a model wins. Daily labels can define evaluation strata after the day; they are not inputs at quotation. Use week/event blocks for uncertainty and report per-event effects. Inventory counts precede schema/DST/coverage filters.

This answers the one-incident limitation without a new fleet simulation: an offline factor-forecast benchmark on many days measures forecast transfer. It does not measure rider service or C compliance on those days. New simulator days would additionally require factor/demand artifacts, a separately versioned wrapper, fixture/information validation and new trajectories; WORLD:51-55,67-93 hard-codes the existing factor root. E:/Code/Report_INT3508/ridebound-scratchpad/tang3/world/preflight_world_v1_3.py:143-152 checks measured-world compatibility. Acceptance of arbitrary new demand/factor artifacts remains UNVERIFIED. Do not replace this with silently copying files into immutable bundles.

### Minimal models and the fairest comparison

Use a small registered model set, not a search for whatever wins 15 Nov:

1. **Strong historical baseline and persistence.** Calendar/season/day-type shape using the same earlier years; current observed condition held flat is a separate baseline.
2. **Damped residual trend.** Published recurrence, adapted to observed log residuals around the historical shape (REPLAY:17-30). Fit its small parameter set only by rolling-origin training. Do not extend the optimistic exact-factor momentum diagnostic into a real-time claim.
3. **Analog-prefix or regime-gated adaptation.** Match current allowed prefix/count/missingness to completed historical-day prefixes constructed with the same observation contract. Neighbor future profiles are legitimate training targets; a current test day's future profile is forbidden. Fix neighbor count and regime threshold on training folds. Blend/widen only under that registered rule.

Weather conditioning is an optional feature ablation within the third method, enabled only if issue/availability timestamps for observations or forecasts are verified. If they cannot be recovered, omit weather inputs. A method using completed daily snow as an oracle can be displayed only as a nondeployable diagnostic, never the main win.

For each method, freeze the first quote; later observations cannot retroactively repair it. In the existing replay, use the same piecewise quote conversion and fixed end-of-window/drain convention (REPLAY:26,34). In the offline benchmark, use 15/30/60-minute factor forecasts and a predeclared fixed-horizon transformation to quote errors. The latter is a factor-derived proxy, not actual pooled rider arrivals. Use current-ETA horizons derived without future duration labels, for example a fixed registered set of 5/10/20/30 minutes; do not choose a horizon from a trip's eventual duration. For a declared current horizon H and observable level f_obs(t), define common free-flow work H/f_obs(t); integrate the held-out f(s) only to create the retrospective target, and each method's forecast to create its frozen quote. This is a model-based factor transformation, not measured real-trip travel time. A real taxi-duration secondary score may be added with its separate dwell/route/demand confounders; it must not be mislabeled a C simulation result.

**Equal quote cost:** choose budgets E={0,15,30,60} seconds on calibration. Freeze any one-sided scaling/widening coefficients before test; give a fixed-pad control the same calibration budget. If a method has zero positive calibration extension, use the registered uniform-pad fallback and label it degenerate. Report test mean and p90 extension globally and by incident/nonincident group. Do not normalize using test arrivals or silently rescale each test day to make costs match. A test-cost drift is a disclosed mismatch; a deployment gain is not established merely by retrospective interpolation of a frontier.

Primary scores: macro per-event/day 15/30/60-minute log-factor MAE and forecast bias; for the matched quotation comparison, late>60/120, early>60, symmetric ±60 accuracy, mean/p90 extension and initial promised horizon. Report proper quantile score/calibration if a quantile/widening model is used. Count all first quotes for cost, completed riders for arrival errors, and timely completions per requested trip for dispatcher comparisons. Report event onset versus post-detection performance and detection delay. Few events, repeated source trips and overlapping windows are not independent samples (REPLAY:38,46-54). Predeclare the primary model/contrast and horizon; adjust confirmatory intervals for the multiple registered comparisons and label the remaining model/budget curves descriptive. Do not choose the test winner and call its unadjusted interval confirmatory.

### The owner's 2013 proposal

**Technically plausible as additional raw history; not the best primary source for this goal.** The current [TLC archive](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) lists “2013” and January yellow records; that verifies an archive link, not successful bulk retrieval or target-year schema/precision. No 2013 trip file was downloaded or decoded this round.

Fielbaum/Alonso-Mora's selected study window was 15 Jan 2013, 13–15 h, with ten comparison weekdays, 2000 vehicles and 19610 requests after capacity filtering (FA:592-605). They explicitly selected off-peak to “disregard unreliability due to traffic conditions” (FA:594-596; [primary paper](https://pure.tudelft.nl/ws/portalfiles/portal/84615509/1_s2.0_S0968090X2030735X_main.pdf), §5). That dataset selection isolates dispatch instability; it was not a training corpus for incident traffic prediction. Using only their chosen two-hour window would select away the variation we need.

Using the **full** 2013 TLC year is different and can supply durations/calendars for a declared reconstruction. Transfer 2013→2018 must validate location/schema changes, route/free-flow normalization, demand mix, season and congestion-level shift. Same city does not mean same distribution or an unchanged network. Prefer the closer 2016–17 fit period, and treat 2013 as a separate extra-history ablation: does adding it beat the closer-years model on later held-out events at equal cost? Kill its claimed value if it worsens transfer. Missing promised-time labels prevent directly learning promise error/C, but do not prevent learning trip durations or the factor proxy.

**Effort estimate:** snapshot-only replay/inputs on existing days, 12–20 h plus full-panel provenance checks, but still one known incident; multi-year target/causal-observation pipeline and simple benchmark, roughly 80–140 h; verified historical weather-vintage features, another 20–50 h if obtainable; new measured simulator days, at least a separate wrapper/demand validation stage whose effort is UNVERIFIED. These are estimates, not permission to run them now. Bulk data size, exact rebuild fidelity and retrieval feasibility have not been independently measured here.

**Claim verdict: MAJOR REVISION toward a fair multi-event study; REJECT one-day/oracle-factor proof of superiority.** **Most damaging question:** can the gain survive honest observation delay, a strong same-data baseline and matched quote cost on several held-out events? **Current evidence:** not yet; the data inventory makes the experiment plausible.

## Three directions, ranked — alternatives, not three simultaneous work packages

### 1. Recommended research step: selection objective × cap, with a small offered-load check

**Verdict: ACCEPT as the next bounded experiment; any improvement/general-necessity claim remains MAJOR REVISION pending results.** This is one experiment on one storyline, not a new promise product.

**Novelty:** Fielbaum already controls instability and trades service for stability (D03:54-56); ordered objectives and soft stability penalties are known (D03:175-181). The potential contribution is a matched mechanism result for this cause-separated gate, under a less conservative objective and a relaxed allowance. Not a new optimizer, first reliability control, profit result or demonstrated advantage of accumulation.

**Decisive experiment, all future work:** two objective orders, existing stability-first and minimal cost-first, × three drop-cap settings U/30/120, retaining all other gates/locks/recovery, generation/retention settings, seeds and information rules. Actual future candidate sets can differ once selection changes trajectories. Main panel: 34 matched existing 8-vehicle contexts. Only stability-first U/C30 archives exist there; therefore four arms need 136 new main jobs. Gate0 requires four OFF-option equivalence jobs on the archived U/C30 w08/w17 cases; three ON smoke jobs cover U/30/120. Minimum **143 jobs**, contingent on matching the archived controls. No default continuation after a mismatch.

For the stricter mechanism/general-regime interpretation, add a small predeclared four-vehicle offered-load check: eight source contexts selected by an input-only rule: every main-panel date with both w08/w17, lowest common available replica. This yields day14/r3, day16/r1, day17/r1, day18/r2, each at w08/w17 (SCOPE:5-13), all six treatments, **48 additional jobs**, hence **191 total** if both stages pass. Keep demand, selected nodes and fleet-ranking inputs fixed; take the first four/eight ranked vehicles, as source SRC/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:461-476 permits. Rebuild/hash fixtures rather than compare unrelated old WP9 cells. Verify increased realized exposure/occupancy: four vehicles increases offered load, but rejection can prevent a truly busy accepted-rider regime. New fixture/harness validity is not certified yet.

Implement only the selector-order option in a separate authorized worktree; preserve hard-profile forced treatment and the normal hard assessor (SELECT:276-331). Run relevant differential/unit/solution checks later; none is built now. Require generation/retention counts and solver statuses/bounds, since the old zero cap-truncation counters do not promise future exhaustive search (R15 rows35,37). Extract realized cost before advertising it; otherwise restrict the outcome claim to service, absolute sharing and reliability. Present naive and the unchanged causal forecast replay, with horizons, extensions and fixed predeclared pad points; no forecast retuning inside this experiment. Replay does not change physical trajectories or retroactively certify displayed ETA movement under the internal C contract. Report the objective-by-cap interaction, per-date/source-group paired effects and uncertainty; these are new policy outcomes on previewed contexts, not new independent days or a population guarantee.

**Sealed-style predictions, explicitly my hypotheses/design thresholds:**
- The primary C30 cost-first contrast increases **absolute shared completions by ≥10%** relative to matched stability-first C30, while serving ≥99% as many. C120 and offered-load effects are secondary; report every arm, not only the best cap. This is an operationally meaningful target, not an estimate from FREE's package gap.
- Stability-first C120 recovers ≥24 of the current 96 C30/U served gap on the 34 cells. Report naive/forecast timely counts and quote costs; no claim that the eight morning cells predict this magnitude.
- Every C run has zero verified budget overshoot. Any new forced/recovery behavior must be explained; a contract failure kills the implementation claim.
- Accumulation is a measured secondary outcome, not a promised positive finding. Register counts of repeated accepted changes and full-witness cumulative-only candidates. A positive witness still does not measure a cumulative-versus-per-step trajectory effect.

**Kill rules:** gate/config/portfolio mismatch; claimed cost gain without an extractable matching cost metric; fewer than the service/sharing targets; an apparent reliability win explained by larger initial quote horizons/padding; no exposure in the offered-load check. A null cost-first result means this objective swap did not produce the targeted improvement. Zero cumulative-only witnesses means keep the cumulative-advantage claim withdrawn; do not tune B/load until it binds. If empirical cumulative necessity is later claimed, an explicit matched per-step policy ablation is still required, with contract/ledger semantics checked; its implementation is not included in these job counts.

**Effort:** my estimate 60–90 h for option/tests, equivalence, fixture/harness checks and outcome analysis, plus thesis writing. Roughly one-to-two focused weeks; actual schedule/runtime is UNVERIFIED. Historical 15 min/job, six-way parallelism (claude-work/RUNTIME-ESTIMATE-2026-10-07.md:24-25) is only a runtime precedent; cost-first may be harder. The deadline must support this time box.

**Storyline:** extends and sharpens C + forecast + ledger; replaces the research emphasis “demonstrate C's usefulness under stability-first only”. **Most damaging question:** is there useful hard-cap value when conservative ranking no longer protects riders for free? Current evidence does not answer it. This is why it ranks first.

### 2. Alternative: causal incident-adaptive quotation on a many-event factor benchmark

**Verdict: MAJOR REVISION until target reconstruction and information availability pass.** Choose this instead of direction1 if the central aim becomes forecasting.

**Novelty:** Syed supplies the factor proxy; historical/adaptive forecasts, Gardner–McKenzie damped trend and forecast quoting are prior (S1:12-18; REPLAY:7,17-30; D03:54-56,175-181,211-217). Potential contribution is an honest incident-transfer result under matched information/quote cost and explicit simulator-versus-realistic-feed limits. Merely using ML, more years or weather is not original.

**Decisive experiment:** Q5's chronological benchmark and fixed calibration-cost frontiers, with strong same-data history/persistence baselines, causal delayed observations, incident/day blocks and the 2013-added-history ablation. Existing C/U/M⁺ replay is a transfer diagnostic; many-event factor results alone cannot establish new C-policy outcomes. No fleet simulation is required for the first stage.

**Sealed-style hypothesis:** relative event-macro log-factor MAE improves ≥10% over both strong history and persistence, at 30 and 60 min, with ordinary-day loss worsening ≤2%. At E=30 s, the factor-derived quote comparison improves late60 by ≥1 pp on event strata, test mean extension within1 s, p90 extension within15 s and early60 within1 pp of the matched baseline. For a C replay, those quotation thresholds must be checked again on actual completed journeys; proxy performance is insufficient.

**Kill:** any future/as-of/weather-vintage leak; unvalidated simulator mapping; fewer than ten usable proxy event spells after data QA, or gains restricted to the already inspected Nov15 event; missing cost guards; superiority unsupported by event-block uncertainty. Ten is a design minimum, not a theorem that ten events suffice. Adding 2013 must improve the frozen later-year comparison to justify its inclusion.

**Effort:** roughly 80–140 h without weather-vintage integration, larger with it (Q5); substantial deadline risk. **Storyline:** extends traffic-aware quoting while retaining C as a controlled fixed dispatch backbone; it replaces the primary experimental focus, not the definition of C. **Most damaging question:** is the apparent prediction gain just finalized factor/weather leakage or more generous promises? Current evidence has no fair multi-event answer.

### 3. Completion fallback: bounded specification/evaluation thesis

**Verdict: ACCEPT for the proposed bounded completion scope; REJECT as a sufficient new top-venue contribution by itself.**

**Novelty:** specification/implementation of this projection-based ledger/certificate and reproducible bounded comparisons. Do not claim novel control, ETA learning, cumulative empirical superiority, business value or a common arrival SLA (D03:54-56,211-225,236-269).

**Decisive evidence:** existing audited raw results, honest C/M⁺/U/+30/+60 padding frontiers, served-set overlap, cumulative witness audit, H6 negative and the one-incident/low-load limitations (A15; R15 sections1-3; FR:58-70,102-104). No new simulation is necessary for those descriptive statements.

**Sealed-style reproduction target/kill:** exact served/late/timely/ledger counts and input hashes reproduce; kill any stronger thesis statement if it relies on a failed audit, omitted close baseline, causal blame attribution or cumulative-necessity inference. This is a reproduction target, not a new performance prediction.

**Effort:** my estimate 16–24 h analysis/claim consistency plus remaining thesis writing; no new runs. **Storyline:** retained, claims narrowed. **Most damaging question:** who changes their practice because of this specific ledger rather than known deadline/soft-control methods? Current evidence does not identify that operator need.

**Exactly one recommended next step:** time-box direction1's semantics/equivalence gate and the paired objective × cap study. Direction2 is an alternative, direction3 the fallback. Do not launch all three. If the actual deadline cannot fit direction1, choose direction3 explicitly instead of calling completion an optimization breakthrough.

## Strict review of the current core

Scores are my judgment of the **audited core as it stands**, not of future promised experiments. No weighted average substitutes for the decisive novelty/significance problem.

| Criterion, 1–5 | Score | Reason / anchor |
|---|---:|---|
| Novelty/originality | 2 | A specific ledger/gate implementation is distinguishable; detection/control/trade-offs/ETA prediction are established, and accumulation has no demonstrated main-regime advantage (D03:54-56,211-217; A15:7,10-17). |
| Significance | 2 | Auditable self-restraint is plausible, but no buyer cost/problem, profit or rider-response validation; arrival frontier is mixed and pooling/service fall (D03:236-245; PAD:14,25,33; pooling-share-2026-10-06.txt:2-3). |
| Technical soundness | 3 | Ledger reconstruction and enforcement are strongly audited; projection attribution is model-dependent and neither residual arrivals nor empirical incremental accumulation are established (A15; D03:222-239; R15 corrections1-2). |
| Experimental rigor | 2 | Stronger matched objective controls, finite main-panel cap dial, independent unseen event days and credible clustered inference are missing; forecast A3 cluster-t crosses zero (FR:58-60; W07X:71-72; FACT:58-61). |
| Reproducibility | 4 | Pinned transcripts, hashes/seeds/protocols and independent re-computation are strong; extension pipelines, current binary equivalence and realistic predictor availability are not yet certified (CAPJ; R15 rows38-40; REPLAY:9-13,38). |
| Remaining-time feasibility | 4 for bounded completion | Most core evidence exists; writing still takes time and deadline/supervisor requirements are unverified. This does not rate the two larger extensions as equally feasible (FACT:99-101; OWN:113-117). |

**Overall recommendation: REJECT at the stipulated strict international research standard in present form.** A major empirical redesign could justify resubmission, but successful engineering tests alone would not guarantee significance or originality. This assessment does not imply failure of an undergraduate thesis; local assessment criteria have not been checked.

### Verdicts on the main claims

| Claim | Verdict | Single damaging question | Answered now? |
|---|---|---|---|
| The defined dispatch ledger/gate is implemented and can be audited in the tested corpus. | ACCEPT, within assumptions | Do records/actions/witnesses actually obey the stated contract? | Substantially yes: A15/CAPJ audits; not a population arrival guarantee. |
| C usefully distinguishes controllable dispatch movement from model traffic projection. | MAJOR REVISION for practical significance | Does that distinction change an operator outcome versus strong matched alternatives? | Limited model example, no validated buyer outcome (W07X:54-62; D03:241-245). |
| Accumulation drives the main measured improvement. | REJECT | What changes versus a per-step rule? | No matched outcome evidence; zero recorded measured cumulative-only prunes. |
| C is generally better for arrivals/service than M⁺ or padded U. | REJECT | Does it dominate at a common SLA/quote cost and all-request denominator? | No: same C/M⁺ timely60, padded-U tie and higher timely120 (PAD:14,33,54). |
| The historical display layer improves errors in these recorded weekday journeys. | ACCEPT as descriptive result; MAJOR REVISION for generalization | Is it robust on honest unseen incident days at equal cost? | No; one incident, previewed dates and fragile A3 inference (FR:38,58-60,102-104). |
| Lower C or better forecast increases profit/satisfaction/retention. | REJECT | Where are behavior/cost/contract data? | Absent from the evidence; D03:236-245,260-265. |

### Three most damaging reviewer questions

1. **What incremental value remains after controlling the stability objective, locks, quote horizon and cap level?** Current FREE/LOCKS packages and the two-arm U/C comparison do not isolate every mechanism. Direction1 directly attacks this gap.
2. **Why is cumulative accounting a meaningful contribution if the main C regime never exercises repeated spending, and where does it outperform a matched per-step/deadline policy on common outcomes?** Current evidence answers implementation and rare witnesses, not superiority. Withdraw the empirical cumulative headline unless a matched ablation supports it.
3. **Would the result survive more independent event days, realistic observation latency, higher offered load and non-scalar traffic?** Current days/source groups are dependent, low-load/zero-dwell/scalar modeling is narrow, H6 is negative, and a snow replay does not establish general robustness (D03:222-245; FR:102-104; R15 rows19-20). Q5 improves the data test; it cannot alone validate a new dispatcher or spatial world.

## Files and remaining limits

Exclusive-created this round, all inside codex-work:
- R16-CODEX.md — this report.
- R16-cap-outcomes.py — preserved failed initial parser.
- R16-cap-outcomes-v2.py — successful independent 72-transcript reader.
- R16-cap-outcomes.json and R16-cap-outcomes.txt — first-quote arrivals, ledger usage, source hashes and explicit prior pruning join.
- R16-weather-inventory.py and R16-weather-inventory.txt — independent inventory of saved weather labels for proposed splits.
- R16-scope-inventory.txt — verified disjoint date sets and the input-only proposed offered-load context selection.

The successful reader finishes with exit0 and all 72 file/frame hash checks passing. The weather inventory finishes with exit0. No new forecasts were fitted, no new raw TLC trips were downloaded, and no future simulation, build or worktree operation was executed. Bulk/schema/weather-vintage/fixture-transfer gates remain unverified where stated.

My answer to Q1 is therefore a qualified but definite **yes to changing the research priority**: conduct one bounded mechanism experiment instead of treating output consolidation as the remaining research. Retain the validated components as controls, withdraw unsupported cumulative/business/general superiority claims, and use the existing-results thesis as an explicit fallback.
