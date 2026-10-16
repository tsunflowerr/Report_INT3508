No blocking error found. The new analysis strengthens the descriptive case, but “fewer insertions” and “traffic-only floor” still go beyond what it measures. No files were changed.

**Script check.** The signed `c != 0` test is correct: it excludes initial promises and flags any dispatch-induced ETA change, including advances. Testing individual revisions avoids cancellation between positive and negative changes. The underlying audit verifies the exact integer decomposition. [exposure_check.py:25](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/exposure_check.py:25), [audit_vep.py:106](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/evidence/audit_vep.py:106).

The overlap union is also correct. It clips positive same-vehicle overlaps to each rider’s onboard interval, merges them, and counts each rider’s shared time once. Summing across riders intentionally counts passenger-time rather than vehicle-time. [exposure_check.py:36](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/exposure_check.py:36).

One robustness issue remains: pickup exposure ignores the audit’s `closed` flag. For reuse, exclude pickup revisions published after boarding. This does not affect these runs, whose pickup dispatch changes are absent. [audit_vep.py:118](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/evidence/audit_vep.py:118).

The independent read-only ledger check reproduced served and exposure counts. Independent reproduction of every Y and shared-minute total is **not checked**; their definitions and computation were inspected.

**R1′ survives as a descriptive decomposition.** I would accept:

> Under U, nonzero dispatch-induced drop revisions affect relatively few served riders, but lateness is concentrated among them: 174 exposed riders account for 134 of the 203 late riders. Unexposed lateness is similar across arms. These results locate the observed errors without establishing why exposure is scarce.

[exposure-check-2026-10-06.txt:2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/exposure-check-2026-10-06.txt:2).

Replace “traffic-only floor, and the caps do not change it” with **“observed lateness among riders without recorded dispatch-induced drop changes.”** Served and unexposed groups differ between policies; initial itineraries, first promises and exposure to traffic ramps can also differ. Similar conditional percentages do not establish an invariant floor.

**R2′ needs narrower wording.** I would accept:

> Every tested cap reduces the share of served riders with nonzero dispatch-induced drop revisions and reduces total shared passenger-time relative to U. This is consistent with restricting later pooling changes as an important mechanism. The summaries do not count insertions or establish complete mediation. C-30 maintains its dispatch-change contract without overrides in these runs; realized sharing is broadly similar among capped arms.

A rider-level flag does not count insertion events, and some insertions can leave the drop ETA unchanged. Total shared passenger-minutes also depend on service volume and trip duration. Report their share of total onboard passenger-minutes alongside the absolute total.

“C does not pool more” should become **“no material pooling advantage is established”**: C exceeds Mplus-30 slightly on both reported sharing measures, while remaining below Mplus-60. [exposure-check-2026-10-06.txt:3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/exposure-check-2026-10-06.txt:3).

**Experiments, ranked by expected marginal value.** Intervention runtimes are **not checked**, so this ranking uses added jobs and implementation burden rather than a fabricated hour estimate.

Use the existing `d20181114-s10-r3` and `d20181117-s10-r3` cells in each listed window. These provide contrasting weekday/weekend anchoring directions and are already in the test split. [split-t38-v1.json:32](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/split-t38-v1.json:32), [:57](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/split-t38-v1.json:57).

1. **Conservative pooling comparator — highest value per added job.** Add U with vehicle capacity **1**, retaining the existing anchoring, fleet locations, demand, locks and constraints. Compare against saved U, C-30 and Mplus-30. This requires **6 planned new jobs**, as counted by the read-only design command. Capacity is already a normalizer parameter. [Program.cs:199](E:/Code/RideBound-deadline/tools/RideBound.Wp6Normalize/Program.cs:199).

   **Prediction to seal:** reducing capacity reduces dispatch exposure and lateness relative to existing U; C-30 retains more timely completions than the conservative comparator. Measure exposure rather than assuming it vanishes.

   **Claim-changing result:** if capacity-one U achieves comparable promise reliability with at least as many timely completions and no greater operating burden, withdraw any suggested advantage over simple pooling restriction. Report timely completions per offered request, coverage, common-rider journey times and vehicle operating measures where available. This tests the trade-off, not complete mediation.

2. **Correct absolute traffic anchoring — robustness priority.** Regenerate those same fixtures with `travelFactorAtSeconds = sourceWindowStartSeconds`; run U, C-30 and Mplus-30. Reuse the saved original-anchor runs as controls: **18 planned new jobs**. Preserve selected requests, node pool and initial fleet positions. Preserve scenario identity because it affects fleet placement. [Program.cs:195](E:/Code/RideBound-deadline/tools/RideBound.Wp6Normalize/Program.cs:195), [FleetPyManhattanNormalizer.cs:466](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:466).

   **Prediction to seal:** lengthening understated weekday travel times increases U’s positive lateness or dispatch exposure; shortening overstated weekend times produces the opposite direction. C-30 retains its no-override result among completed runs.

   **Claim-changing result:** materially different tails, service losses or integration failures require narrowing numerical claims to the original anchoring. Stable comparisons strengthen robustness within this selected demand. Regenerate valid manifests and audit preserved inputs before running.

## Joint conclusions

1. **SUPPORTED:** First promises incorporate initial planned burden; selection favors shorter modeled trips.
2. **SUPPORTED:** Capped runs improve measured postpromise reliability while reducing service coverage, dispatch-change exposure and shared passenger-time.
3. **SUPPORTED:** C-30 modestly shortens common riders’ journeys and maintains its own dispatch-change contract without overrides. Competing guarantees differ.
4. **SUPPORTED:** Display forecasting improves promise calibration with vehicle actions fixed; the anticipated ledger component is forecast-relative.
5. **WEAK:** Reduced later pooling explains most of the improvement; unexposed lateness is an invariant traffic floor; the causes of scarce exposure can be ranked.
6. **UNSUPPORTED:** Human harm or commercial benefits are demonstrated, or reliability improves at comparable pooling efficiency.

## Remaining disagreements

- **Mediation:** establish which accepted or rejected insertions explain the changed errors.
- **Efficiency:** test whether C-30 beats a simple conservative comparator on timely service and operating burden.
- **Generalization:** correct anchoring first; broader density and selection claims still require controlled evidence.

These are limitations on interpretation, not reasons to reject the saved descriptive results.