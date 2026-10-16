The selection bias is verified. Reduced pooling accompanies the reliability gain, but its causal contribution—and your ranking of explanations—remains unresolved. No files were changed.

**D2: I accept the addendum’s substantive result.** I read the analysis script and verified its ordinal mapping and graph construction without rerunning its file-writing entry point.

For `d20181114-s10-r1-w08`, the prescribed read-only Python command reproduced:

```text
ordinal 20862: request_id=3791876, rq_time=32631, start=173, end=565
fixture: arrivalTimeMs=3831000, origin=node-000173, destination=node-000565
requests=108; selected frame rows=108; eligible frame rows=2757
selected-request mapping mismatches=0
```

The zero-based ordinal convention agrees with [StrictCsv.cs:46](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/StrictCsv.cs:46). The script computes directed shortest paths through the **full base network**, consistent with the normalizer’s graph traversal; the selected service nodes do not restrict intermediate road nodes. See [selection_length_check.py:13](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/selection_length_check.py:13) and [DirectedTravelGraph.cs:82](E:/Code/RideBound-deadline/src/RideBound.Benchmarking/Normalization/DirectedTravelGraph.cs:82). Duplicate directed edges, which could invalidate the sparse-matrix construction by summing parallel weights, were absent.

The saved distributions support your conclusion:

| Base direct travel time | Selected | Eligible |
|---|---:|---:|
| Mean | 179.9 s | 229.4 s |
| Median | 165 s | 196 s |
| p90 | 303 s | 429 s |

Selected medians are lower in **49/49 fixtures**. [selection-length-check-2026-10-06.txt:2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/selection-length-check-2026-10-06.txt:2), [:3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/selection-length-check-2026-10-06.txt:3), [:4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/selection-length-check-2026-10-06.txt:4).

Two qualifications matter. These are modeled **base-network durations**, not observed trip durations; “free flow” calibration is **not checked**. Aggregated counts include repeated request appearances across fixtures and overlapping windows. Exact sample size and subset membership establish the sampling fraction, while statistical representativeness is **not checked**. The addendum’s approximate window fraction applies to the matched source CSV, not automatically all Manhattan trips.

**R1 — PARTLY.** Your baseline explanation is supported: much of the journey is already inside the first promise. But the asserted order of importance is unproved.

B3 measures actual onboard overlap. It does **not** measure exposure to later insertions. Another rider can be inserted, collected and dropped **before this rider boards**, delaying this rider’s pickup and drop without any shared onboard interval. Therefore “never shared” does not imply “never affected by pooling decisions.” The overlap definition is explicit in [pooling_share.py:20](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/pooling_share.py:20).

Nor do fleet, request and node counts alone establish low effective density. Arrival timing, geographical concentration, trip duration, compatible directions, vehicle locks, search strategy and constraints determine matching opportunities. Your newly verified preference for shorter trips can itself reduce the time available for onboard overlap.

Is **22.8%** low? It is substantially below a published high-pooling simulation. Alonso-Mora et al. report approximately **90%** shared rides, with a comparable denominator: passengers who shared divided by picked-up passengers. See [local primary text:597](E:/RideBoundData/literature-survey-2026-10-06/text/alonso-mora-pnas2017-author-corrected.txt:597) and [:538](E:/RideBoundData/literature-survey-2026-10-06/text/alonso-mora-pnas2017-author-corrected.txt:538). Their fleet, constraints, assignment method and rebalancing differ, so this establishes a comparison with that simulation rather than an industry norm. [Author-corrected primary paper](https://autonomousrobots.nl/assets/files/publications/17-alonsomora-ridesharing-pnas.pdf).

A verified commercial-service match-rate benchmark is **not checked**. The Chicago rates in your source collection are explicitly marked as an unopened third-party snippet and should not become evidence through repetition. [SOURCES-2026-10-05.md:532](E:/Code/Report_INT3508/ridebound-scratchpad/business-need/SOURCES-2026-10-05.md:532).

Finally, B1 supports a narrow statement: arithmetic rescaling of existing errors leaves the capped tail small. It cannot establish that anchoring is causally secondary. Correcting travel times could change vehicle availability, traffic-bin crossings, feasibility, first promises and later insertion decisions. Multiplying recorded lateness preserves all those decisions. [burden_and_rescale.py:5](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/burden_and_rescale.py:5).

Your stated weekday anchoring ranges also omit the broader values for the later weekday shown in [factor-anchor-check-2026-10-06.txt:7](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/factor-anchor-check-2026-10-06.txt:7).

**R2 — PARTLY.** “Pool less” is a credible mechanism, and it exposes a substantial efficiency trade-off. Similar outcomes under competing rules do not establish that trade-off as necessary or desirable.

There are two factual corrections:

- C-30 and Mplus-30 have **similar**, rather than identical, shared-rider rates: **13.4% and 13.1%**. [pooling-share-2026-10-06.txt:3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/pooling-share-2026-10-06.txt:3).
- V-30’s pooling rate is **not checked** by this analysis: the script processes only U, C-30 and Mplus-30. V-30 also serves **2,336**, versus **2,338** under C-30 and Mplus-30. [pooling_share.py:10](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/pooling_share.py:10), [T38-REPORT.md:46](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md:46).

The important unresolved question is whether the cap preserves more useful pooling than a simpler conservative policy at comparable reliability and coverage. Matching Mplus’s pooling rate does not answer that.

**D3: B3 changes the interpretation, not the measured conclusion.** C-30 improves simulated postpromise reliability **while reducing realized sharing and service coverage**. The common-rider ride reduction of **10.507 seconds** remains supported. [common-riders-check-2026-10-06.txt:3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/common-riders-check-2026-10-06.txt:3).

That common-rider result rejects a purely served-set-composition explanation. It remains compatible with improvement mediated by less pooling. Claiming “just less pooling” requires evidence about which later insertions disappeared and whose delays they would have caused. Merely conditioning on whether riders ultimately shared would be insufficient, because sharing is itself affected by the policy.

## Proposed joint conclusions

1. **SUPPORTED:** The first-promise metric measures subsequent promise error and excludes waiting and detours already promised. Experimental selection consistently favors shorter modeled trips.
2. **SUPPORTED:** Against U, C-30 improves measured promise fidelity and modestly shortens common riders’ journeys, with lower service coverage and realized sharing.
3. **SUPPORTED:** C-30 and the tested fixed deadline have similar rider outcomes under different contracts. C-30 avoids overrides in these runs; this does not establish a stronger arrival-time guarantee.
4. **SUPPORTED:** Display forecasting improves promise calibration without moving vehicles. The ledger’s anticipated component depends on the forecast.
5. **WEAK:** Reduced pooling explains most of the reliability improvement; low demand density is its main cause; anchoring is secondary.
6. **UNSUPPORTED:** These results demonstrate human harm reduction, commercial benefits, or reliability gains at comparable pooling efficiency.

## Disagreements that remain

- **Ranking the causes of small lateness.** Settle with measured insertion opportunities and controlled comparisons varying selection, demand intensity and travel-time anchoring.
- **Whether improvement is entirely mediated by less pooling.** Settle with common-rider insertion histories, shared duration or distance, and a comparator achieving similar pooling exposure and coverage.
- **Whether the efficiency sacrifice is justified.** Settle with a frontier reporting reliability, completed requests, shared passenger-distance and vehicle operating cost.
- **Whether V-30 supports the same mechanism claim.** Settle by computing its overlap and insertion-exposure metrics directly; the current pooling analysis excludes it.