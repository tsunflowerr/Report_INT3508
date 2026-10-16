No files were changed.

First, correct the comparator: **the tested Mplus rule uses a fixed first-promise deadline, without a traffic allowance.** The code explicitly says traffic drift alone can violate it, and compares candidate drop time with the initial promise. Your definition “first promise + traffic + slack” describes a different rule. See [CommitmentLockEvaluator.cs:156](E:/Code/RideBound-deadline/src/RideBound.Domain/Commitments/CommitmentLockEvaluator.cs:156) and [CommitmentDecisionValidator.cs:387](E:/Code/RideBound-deadline/src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:387).

**P1 — PARTLY.** The simplified world limits generalization, but two conclusions overreach.

First, missing execution noise does not mathematically make these lateness rates a **lower bound** for reality. Different demand, routing, forecasting and admission decisions could move rates either way. Second, “world versus data” is an artificial separation: the normalizer chooses a coverage-oriented node pool and retains requests within it, producing experimental demand conditional on that construction. See [FleetPyManhattanNormalizer.cs:680](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:680).

Absolute results remain interpretable **within this model**; paired comparisons also inherit its limitations. Your explanation of disk usage is **not checked**.

**P2 — PARTLY.** Harm reduction is unproved, but “close to nothing” is a value judgment unsupported by these results.

U has positive severe tails: **0.74% above five minutes and 0.08% above ten minutes**. Those tails disappear in the reported capped runs. That is a measured change, even if uncommon. See [lateness-distribution-2026-10-06.txt:5](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/lateness-distribution-2026-10-06.txt:5) and [:12](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/lateness-distribution-2026-10-06.txt:12).

More importantly, Cohen’s thresholds select substantial **pickup ETA errors** for compensation experiments. They do not establish the minimum harmful error, or a threshold transferable to first **drop** promises. The defensible statement is “human harm was not measured.” [Cohen et al., primary paper](https://maxccohen.github.io/Frustration-Based-Promotions.pdf).

**P3 — PARTLY.** Zero dwell and deterministic execution are supported. The causal importance of your other explanations is not established.

Pruning totals count recorded candidate failures across decisions; they do not identify unique affected riders or demonstrate how much delay each constraint prevented. See [constraints_and_pooling.py:45](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/constraints_and_pooling.py:45).

You also missed a travel-time scale choice: the inspected morning fixture uses the **midnight traffic factor**, while the wrapper applies traffic changes relative to the **demand-window start**. This can compress morning travel durations relative to the source’s absolute traffic scale. Initial anchoring is intentional; its aggregate contribution to small lateness is **not checked**. Evidence: [fixture configuration:1](C:/RideBoundData/research/fixtures-panelA-v1/d20181114-s10-r3-w08/normalizer-configuration.json:1), [normalizer scaling:818](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:818), [preflight_world.py:83](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/world/preflight_world.py:83).

**P4 — PARTLY.** The measured trade-off stands, with important qualifications.

- C-30 loses **96 completed riders**, or **2.6 percentage points of the request service rate**. That is not a relative percentage of U’s served riders. See [T38-REPORT.md:49](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md:49).
- Served-set composition does not fully explain shorter rides. My read-only Python command, shown in the tool trace and run with the prescribed interpreter, produced:

  ```text
  U/C common served: 2207 only U: 227 only C: 131
  Common-rider mean ride seconds C-minus-U: -10.507
  ```

  This supports a modest physical improvement among common riders, while showing that the net service loss hides substantial substitution.
- “Never breaks its own promise” compares **different guarantees**: C’s dispatch-change budget versus Mplus’s fixed arrival deadline. The analysis explicitly scores these separately. See [sweep_analyze.py:129](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/sweep/sweep_analyze.py:129).
- Family B alone cannot attribute its improvement to optimistic promises: actions changed in every completed forecast-versus-naive pair. Fixed-run display replay provides cleaner evidence for the reference-time explanation. See [test-family-b report:40](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/test-family-b-2026-10-06-report.txt:40).
- Display reduces **promise error** while arrival times stay fixed. Its “anticipated traffic” component is defined as the promise extension, rather than independently identified physical delay. See [forecast_family_a.py:116](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/forecast_family_a.py:116) and [:134](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/forecast_family_a.py:134). Operational cost also includes displayed pickup promises exceeding pickup deadlines, documented in [FORECAST-REPORT.md:70](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md:70).

**P5 — PARTLY.** Report threshold curves and relative errors. But replace “harm-relevant tails are absent” with “the reported capped runs have no drop-promise errors above the stated larger thresholds.”

“Measurement plus attribution, not user-experience gain” is too restrictive. **Simulated promise fidelity and journey-time improvements** are supported; satisfaction, retention and real-world harm reduction are unmeasured.

The single most important missed explanation is **the first-promise baseline**. Waiting and pooling detours already scheduled at acceptance are incorporated into that promise. A slow itinerary can therefore have tiny promise error. The first promise comes from the candidate route schedule, and lateness subtracts that promise from actual arrival. See [PromiseProjector.cs:123](E:/Code/RideBound-deadline/src/RideBound.Application/Promises/PromiseProjector.cs:123) and [lateness_distribution.py:24](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/lateness_distribution.py:24). Moreover, most U riders have no subsequent dispatch-induced drop change. See [constraints-and-pooling report:7](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/report-extras/constraints-and-pooling-2026-10-06.txt:7).

“Is it the data?” is therefore incomplete. Ask: **Which burden does this metric measure, which riders and replanning opportunities enter it, and what travel-time scale generates its seconds?**

Three analyses using existing outputs would discriminate between explanations:

1. **Decompose initial itineraries and later revisions.** Separate promised waiting, initial detours, traffic exposure and subsequent dispatch changes. Large initial burdens with few revisions support my baseline explanation. Frequent replanning with consistently tiny increments would strengthen your constraint-suppression explanation.
2. **Audit normalization and temporal scaling.** Compare selected versus eligible direct-trip durations, and fixture-factor timestamps versus window-start factors. Representative trip lengths and correctly aligned absolute times would weaken the selection/scale explanation; compressed morning times would require revising the interpretation of “short trips.”
3. **Extend the matched-rider and fixed-run forecast analyses.** Report common/U-only/C-only riders, timely completions per request, and promise-only deadline breaches with actions fixed. Persistent physical improvements support an operational benefit; improvements confined to changed references support forecast calibration rather than faster service.

Boarding/dwell is **zero and invariant** in these runs. Candidate pickup and drop stops use `Duration(0)`; the adapter passes that duration directly to FleetPy. Constant boarding time is explicitly zero, and additional boarding time defaults to zero. See [InsertionCandidateGenerator.cs:520](E:/Code/RideBound-deadline/src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs:520), [fleet_control.py:946](E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/ridebound_fleetpy/fleet_control.py:946), [preflight.py:241](E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py:241), and [FleetControlBase.py:157](E:/RideBoundData/wp7/FleetPy-1.0.2/src/fleetctrl/FleetControlBase.py:157).

## Proposed joint conclusions

1. **SUPPORTED:** C-30 improves simulated postpromise reliability and modestly shortens common riders’ journeys, while reducing service coverage.
2. **SUPPORTED:** The tested fixed deadline experiences traffic-induced recovery pressure; C maintains its dispatch-change contract. These guarantees differ.
3. **SUPPORTED:** Forecast display improves promise accuracy without accelerating trips.
4. **WEAK:** Constraints, short trips and simplified execution explain the magnitude; their relative contributions remain unresolved.
5. **UNSUPPORTED:** These rates bound real-world lateness from below, establish a universal harm threshold, or demonstrate satisfaction or retention gains.