# Round 26 — Chapter 3 open technical questions

2026-10-12. This report completes the interrupted Round 26 work. The already-created trace script and its output were retained without modification. Answers use the primary code, configuration, history and run artifacts inspected in that work, plus official ETH publication sources. Missing evidence is explicitly labelled **CANNOT ANSWER**.

No simulation, build or installation was performed. The only file created in this continuation is this report, using exclusive creation inside codex-work.

## Source paths and scope

- **S**: E:/Code/Report_INT3508/ridebound-scratchpad/
- **SRC**: C:/Code/RideBound-noworse/src/
- **DOC**: E:/Code/RideBound/docs/
- **AD**: E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/
- **C120**: C:/RideBoundData/research/tier3-t38c120-v1/
- **SNOW**: C:/RideBoundData/research/tier3-forecast-v1/
- **W**: E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/

The experiment wrapper loads the preflight from RideBound-deadline: S/tang3/world/preflight_world.py:49–50,201–210. Its preflight was byte-identical to the corresponding RideBound file inspected initially, but the two adapter fleet_control.py files differed. Consequently adapter anchors below use **AD**, the actual experiment's source path. Archived runner identities are established from manifests and hashes; the current C# source was not executed.

## Q1. What triggers dispatch rounds, and how often?

**Answer:** an event clock, with several kinds of trigger and additional batches at the same simulated time. There is no single fixed dispatch period. In particular, drainStepSeconds=600 does not mean one decision every ten minutes.

The driver:

1. Calls the controller initially at t=0.
2. Groups requests by their source arrival second and submits that second's arrivals together.
3. Advances to the earliest next arrival, physical vehicle boundary, or applicable drain timer.
4. Moves vehicles to that instant, submits any arrivals there, and triggers the controller.
5. Can trigger again after immediate zero-duration physical leg closures.
6. Can trigger again after booking confirmations at the same instant.
7. Can send an additional vehicle-observation batch at that instant.
8. In the main experiment, also stops at each 900-second world-bin boundary inserted by wrapper v1.1 and inherited by v1.2.

**Primary anchors:**

| Mechanism | File:line |
| --- | --- |
| Initial call and grouping arrivals | AD/actual_fleetpy_medium_preflight.py:528–543 |
| Earliest boundary, submission and trigger | same file:575–637 |
| Immediate physical closure calls | same file:545–567 |
| Booking-confirmation microsteps | same file:379–394 |
| Batch, decision, ACK and additional observation batch | AD/ridebound_fleetpy/fleet_control.py:395–451 |
| Exact 900-second world boundaries | S/tang3/world/preflight_world_v1_1.py:40–58 |
| v1.2 inherits that boundary mechanism | S/tang3/world/preflight_world_v1_2.py:18–20 |
| eventDriver and drain parameters | S/tang3/calib/panelA/drivers/d20181114-s10-r3-w08.driver.json:9,14–15 |

After the last arrival, if requests or physical tasks remain, the code proposes a timer at current_time+600 seconds. A nearer physical/world boundary wins. Only a chosen drain timer increments drain_steps; maximumDrainSteps=24 limits those timer hits, not all rounds or a fixed total run duration. The run ends once there are no future arrivals, active requests or physical tasks. See preflight:569–581,595–636.

**Real-cell count:** the suggested d20181114-s10-r1-w08 belongs to calibration (S/tang3/t38/split-t38-v1.json:5–17); its C-120 test-run folder does not exist. The completed count uses the test cell **d20181114-s10-r3-w08**, listed at split:33.

| Quantity | Value |
| --- | --- |
| Requests | 108 |
| Event batches /decision replies /acknowledged decisions | 613 /613 /613 |
| First round | epoch 1, t=0 ms, transcript ordinal 5 |
| Last round | epoch 613, t=8,193,742 ms, transcript ordinal 1,841 |
| Distinct simulated round times | 258 |
| Adjacent rounds at identical simulated time | 355 |
| Largest interval between successive rounds | 396,672 ms =396.672 s |
| First /last request arrival | 61,000 /7,068,000 ms |
| Distinct request arrival times | 108 |

**Output anchors:** C120/C-120-d20181114-s10-r3-w08/transcript-00.ndjson; W/round26-trace-rider.txt, section “Q1 REAL-CELL ROUND COUNT”; W/round26_trace_rider.py, function round_counts. All 1,846 decoded frames in that transcript passed length and SHA-256 checks. Full transcript SHA-256:

45f6ace7abe4b9c240284aef88a1e9f70a51135b89edfd867dc5e3899e62e27f

The original run-00.json reports requestCount=108 and nextEpoch=614, consistent with 613 rounds. The 471 timerTick events are not 471 post-demand drain steps: ordinary event batches also generate timer events.

**Confidence:** high for the traced implementation and cell. No universal frequency is inferred for other FleetPy controllers.

Suggested thesis text:

> Bộ chạy tiến theo đồng hồ sự kiện: yêu cầu đến, xe tới mốc vật lý và các mốc cập nhật tắc đường đều có thể gọi một lượt quyết định. Việc xác nhận đặt chuyến và cập nhật trạng thái có thể tạo thêm lượt ở cùng thời điểm mô phỏng. Sau yêu cầu cuối, bộ chạy tiếp tục cho tới khi hết yêu cầu và hành trình đang hoạt động; bước 600 giây chỉ là một mốc dự phòng của giai đoạn kết thúc, không phải chu kỳ điều phối.

## Q2. How long is a cell in simulated time?

**Answer:** the demand window is nominally 7,200 seconds, but the run ends when the selected requests and physical trips have drained. There is no constant “two hours plus 600 seconds”. A run can finish before the nominal window ends if all selected arrivals and trips have already finished.

For C-120 d20181114-s10-r3-w08:

- Start: t=0.
- Final clock: 8,193,742 ms.
- Duration: 8,193.742 s =136.5623667 minutes =2.276039444 hours.
- With the 08:00 New York window start, the end is 10:16:33.742.
- The last arrival is at t=7,068 s; another 1,125.742 simulated seconds elapse until the final round. This is observed activity after the last arrival, not a configured fixed extension.

The 34 main-panel **C-120** runs vary as follows:

| Endpoint | Cell | Final clock | Duration |
| --- | --- | ---: | --- |
| Minimum | d20181115-s10-r4-w07 | 7,081,000 ms | 118.0166667 min /1.966944444 h |
| Maximum | d20181117-s10-r3-w07 | 9,295,784 ms | 154.9297333 min /2.582162222 h |

**All 34 exact values** are retained in W/round26-trace-rider.txt, section “Q2 C-120 MAIN-PANEL SIMULATED LENGTHS”. The script reads each original run-00.json and checks its final clock against its raw final checkpoint.

**Primary anchors:** C120/C-120-<cell>/run-00.json:semantic.finalSimulationTimeMs and requestCount; the corresponding final checkpoint:payload.content.simTimeMs; AD/actual_fleetpy_medium_preflight.py:580–581,639–683 for termination and reported clock; S/tang3/world/preflight_world_v1_2.py:18–20 for the two-hour factor window and held factors during drain.

**Confidence:** high for these 34 C-120 runs. Other arms can finish at different times; this is not an arm-independent duration table.

## Q3. Trace one real rider

**Answer:** the script and its completed output already exist and were not overwritten:

- W/round26_trace_rider.py
- W/round26-trace-rider.txt

The standalone standard-library script reads primary transcripts, imports no simulator or project analyzer, and opens its output with mode x. It checked 34 final checkpoint frames and reconstructed **71,272 revisions for 2,387 riders**, checking the previous-p chain, x+c=z, all three absolute delta fields, budgetBefore/budgetAfter and the 120-second cap.

There were 103 riders with at least two revisions and some nonzero drop c; 97 had a positive dispatch move of at least one second.

**Selected rider:** rq-c48d442603e9ce8c056b029d6d50c497f4d224b8af469945692690e92a75afb0, in **d20181117-s10-r1-w17**.

The selected history has **15 revisions**, a shortest history among the meaningful positive-move candidates under the script's selection rule. This is longer than a three-row illustrative example, but no recorded revision was hidden to make it appear simpler. There is one dispatch move, **14.920 seconds**.

**Primary anchor:** C120/C-120-d20181117-s10-r1-w17/transcript-00.ndjson, final checkpoint ordinal 1,716; then payload.content.onlineState.commitmentLedger for the full request ID above, entries. Checkpoint frame SHA-256:

c96a9801c9785f781196a84907bcb1a848b60515c565a4d4472eeea37615fdfc

The output includes every row's simulated publication time, epoch, event sequence, promise version, v/e/p, signed x/c/z, running allowance use and remaining allowance, both in exact milliseconds and in seconds.

Complete drop history in seconds (ETAs relative to the 17:00 scenario start):

| Entry | t | v | e | p | x | c | z | Running Σabs(c) | Remaining |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Initial | 1925.000 | 2626.044 | 2626.044 | 2626.044 | 0 | 0 | 0 | 0 | 120.000 |
| 1 | 2003.000 | 2626.044 | 2626.283 | 2641.203 | +0.239 | +14.920 | +15.159 | 14.920 | 105.080 |
| 2 | 2024.822 | 2641.203 | 2641.012 | 2641.012 | −0.191 | 0 | −0.191 | 14.920 | 105.080 |
| 3 | 2061.753 | 2641.012 | 2641.063 | 2641.063 | +0.051 | 0 | +0.051 | 14.920 | 105.080 |
| 4 | 2139.559 | 2641.063 | 2641.107 | 2641.107 | +0.044 | 0 | +0.044 | 14.920 | 105.080 |
| 5 | 2172.938 | 2641.107 | 2641.038 | 2641.038 | −0.069 | 0 | −0.069 | 14.920 | 105.080 |
| 6 | 2210.888 | 2641.038 | 2640.964 | 2640.964 | −0.074 | 0 | −0.074 | 14.920 | 105.080 |
| 7 | 2215.200 | 2640.964 | 2640.981 | 2640.981 | +0.017 | 0 | +0.017 | 14.920 | 105.080 |
| 8 | 2266.000 | 2640.981 | 2641.126 | 2641.126 | +0.145 | 0 | +0.145 | 14.920 | 105.080 |
| 9 | 2333.000 | 2641.126 | 2641.003 | 2641.003 | −0.123 | 0 | −0.123 | 14.920 | 105.080 |
| 10 | 2389.880 | 2641.003 | 2640.963 | 2640.963 | −0.040 | 0 | −0.040 | 14.920 | 105.080 |
| 11 | 2451.000 | 2640.963 | 2641.070 | 2641.070 | +0.107 | 0 | +0.107 | 14.920 | 105.080 |
| 12 | 2478.000 | 2641.070 | 2641.204 | 2641.204 | +0.134 | 0 | +0.134 | 14.920 | 105.080 |
| 13 | 2494.000 | 2641.204 | 2641.135 | 2641.135 | −0.069 | 0 | −0.069 | 14.920 | 105.080 |
| 14 | 2603.011 | 2641.135 | 2641.176 | 2641.176 | +0.041 | 0 | +0.041 | 14.920 | 105.080 |
| 15 | 2640.963 | 2641.176 | 2640.963 | 2640.963 | −0.213 | 0 | −0.213 | 14.920 | 105.080 |

For revision 1, t=17:33:23.000, v=17:43:46.044, e=17:43:46.283 and p=17:44:01.203. The ledger spends 14.920 seconds and retains 105.080 seconds. All later c values are zero, so later reference ETA changes spend no additional drop allowance. Negative x here is not negative dispatch c or proof of a particular physical traffic cause.

**Published p unchanged but allowance grew:** no drop entry with p=v and c≠0 was found among those 71,272 revisions in the 34 main C-120 ledgers. **CANNOT PROVIDE an observed example from this panel.** This scoped negative result does not prove impossibility in other configurations.

**Confidence:** high for the full printed history and this scoped search. The initial promise is shown separately and is not counted as a revision.

## Q4. Origin of C, U, M⁺, V and FREE

**Answer:** operational mappings are verifiable, but the inspected primary docs, comments and history do not give explicit naming/coinage reasons. Do not invent acronym expansions.

| Label | Verified operational mapping | Primary anchor | Naming reason |
| --- | --- | --- | --- |
| C | Cumulative drop allowance on decision-induced revisions | S/tang3/configs/C-30.json:6,17–23; DOC/08-algorithms-baselines-and-solver.md:28 identifies canonical C1 as ridebound-hard-vector | **CANNOT ANSWER** why the letter C was chosen |
| U | Drop limit lacks hardLimit; decision-induced basis and other locks remain | S/tang3/configs/U.json:6,16–23,34; compare C-30 hardLimit=30000 | **CANNOT ANSWER** its intended literal expansion; operationally uncapped, not physically unconstrained |
| M⁺ /Mplus | One-sided deadline slack relative to the first drop promise | S/tang3/configs/Mplus-30.json:16–23,98, dropEtaDeadlineSlackMs=30000; historical W07X document:43–44 | **CANNOT ANSWER** why M or “plus” was selected as the name |
| V | Customer-visible cumulative budget basis | S/tang3/configs/V-30.json:6,17–23, customerVisible; historical W07X document:43 defines V_r=Σabs(z) | Operational mapping verified; **CANNOT ANSWER** an explicit letter-origin reason |
| FREE | Thesis shorthand for B1 rolling-cost/free pooling, with physical service checks | DOC/08-algorithms-baselines-and-solver.md:23,35–43; DOC/18-status-and-decision-log.md:15–16 | **CANNOT ANSWER** who coined the literal FREE alias or why |

History inspected:

- git log --all --reverse -S Mplus -- docs first found **aa98fa57a41e91d8532543922b802aeda4b5f052**, 2026-10-01.
- git show aa98fa5:docs/benchmarking/tier3-w07x/W07X-PLAN.md:14–18 already refers to earlier C/Mplus experiments; 32–34 gives configuration mappings and 43–44 the obligations.
- **323a8d91cc8d7a15587b04b597dc4f7a6fb5f822**, 2026-10-01, docs/benchmarking/tier3-t38/T38-PLAN.md:67–68 lists U/C/Mplus/V.
- Canonical C1/C2 identities are documented at DOC/08:28–29 and DOC/18:5559–5568.
- A literal-word git history search for FREE in docs returned no matches. A substring search had matched FREEZE; that result was discarded.

The earliest committed Mplus occurrence found is not proof of first coinage, since it explicitly refers to previous experiments. No reason tying M to an author's surname was established.

**Confidence:** high for configuration meanings; limited for historical completeness. **CANNOT ANSWER** the requested naming rationale from the inspected sources.

## Q5. Why accepted count before stability?

**Answer:** the hierarchy is explicitly specified and implemented. **CANNOT ANSWER** the author's reason for placing accepted count above stability; no explicit rationale was located in the inspected design, ADR and source history.

DOC/08-algorithms-baselines-and-solver.md:136–144 states:

> “Tối đa accepted count.”
> “Giữ accepted count tối ưu, tối thiểu worst budget utilization.”

This means stability is optimized among solutions tied on accepted count. The same document:148–151 explicitly recommends multi-pass solving “để dễ audit”; that explains the solve method, not the service/stability ordering.

SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:

- 285–294: optional forced-reference-count.
- 297–303: maximize accepted-request-count.
- 319–329: worst-hard-utilization followed by revision objectives.
- Operational cost and candidate-ID ranks come later; ID ranks at 371–384.

There is a written reason for **forced recovery before acceptance**, in the comment at 285–287:

> “It ranks before accepting new riders, so it is selected only for a vehicle with no alternative that avoids it.”

That does not explain acceptance before stability.

The accepted-before-utilization order is also present in historical commit **44ef6a7cacdc58e7c6c0576430fcd7bb02e76c7a** (2026-08-05), SolverBackedFleetSelection.cs:270,294; and commit **38d517d**, the same file:280,304. DOC/18:5564–5567 records accepted/worst-utilization/revision/cost/ID order, without the requested motivation.

Acceptance maximization operates after feasibility and hard commitment filtering; it does not permit violating a hard cap to serve another request. “Service-first among feasible candidates” describes its semantics, not a demonstrated business or user-value rationale.

**Confidence:** high for ordering and conditional semantics; **CANNOT ANSWER** its design motivation.

## Q6. What elapsedMs measures; recorded OS/machine information

**Answer:** experiment elapsed fields measure whole-run wall-clock or supervision duration, not just a RideBound decision call. They include FleetPy execution and waiting for runner calls. They are distinct from simulated clock time, and their boundaries differ by artifact.

| Field | Primary boundary | Interpretation |
| --- | --- | --- |
| WP14 fresh-job elapsedMs | AD/wp14_run_matrix.py:266,321–352 | Full external preflight, simulator and runner calls, output work, then bundle verification and binding checks |
| WP14 reusedVerified elapsedMs | same file:266–274 | Re-verification of an existing bundle; not a new simulation runtime |
| WP14R attempt-terminal.json.elapsedMs | AD/wp14r_scientific_protocol.py:801–803,824; wp14r_attempt_ledger.py:795–797 | Last verified process-journal monotonicElapsedMs, spanning the supervised child run; later independent bundle verification excluded because elapsed is read before it at 824–829 |
| Main C-120 resources.wallMilliseconds | AD/actual_fleetpy_medium_preflight.py:427,695–712 | From before initialization through simulation, decisions, transcript/checkpoint work, close/receipt checks and temporary cleanup; not named elapsedMs |
| semantic.finalSimulationTimeMs | same file:680–683 | Simulated clock, not elapsed wall time |

Concrete primary artifacts:

- E:/RideBoundData/wp14r/development-v6-ledger/w14-d20181112-s10-r1-w08-c1-h6ref-s7/attempt-01/attempt-terminal.json has **elapsedMs=607000**.
- Its process.log:605 records childExit at **monotonicElapsedMs=607000**. Journal timing starts at AD/wp14r_supervised_process.py:297 and is calculated at 329–330; child exit is appended at 979–985.
- C120/C-120-d20181114-s10-r3-w08/run-00.json has **wallMilliseconds=1004311** and **finalSimulationTimeMs=8193742**: approximately 16.74 wall minutes versus 136.56 simulated minutes.

The same WP14R process.log, **line 1**, records platform **Windows**, executable path/hash, environment binding, working directory and hostFingerprintSha256:

efebacc06c704d767ea59df7788ff107e2737c65dba1ae67506054abd53c6f81

AD/wp14r_supervised_process.py:585–595 constructs that fingerprint from platform, release, machine architecture, hashed node name and Python version. Lines 691–704 emit the fingerprint and readable platform. The detailed identity is hashed rather than printed as a hardware specification.

The inspected initializeRun manifests record simulator/core/binary/configuration/seed identities but no readable CPU-model/RAM specification. **CANNOT RECOVER a full historical CPU/RAM/OS-release specification from the inspected manifest/log fields alone.** The present machine was not substituted for the historical run host.

**Confidence:** high for the metric boundaries and recorded Windows platform; incomplete for historical hardware. No per-decision latency was measured in this work.

## Q7. Cause of the earlier −1 ms moves

**Answer: CANNOT ANSWER the cause of those particular recorded −1 ms dispatch changes.** Quantization code exists, but its existence does not establish that it caused the observed sign and magnitude.

Verified mechanisms:

| Mechanism | Primary anchor |
| --- | --- |
| Seconds to integer milliseconds using Decimal and ROUND_HALF_EVEN | AD/ridebound_fleetpy/mapping.py:82–104 |
| Closure-check routing times converted using Python round | AD/actual_fleetpy_medium_preflight.py:440–443 |
| Remaining edge-progress time rounded upward by integer division | SRC/RideBound.Application/Scheduling/RouteScheduleProjector.cs:69–88,168–169 |
| Pairwise differences between previous, exogenous and proposed projections | SRC/RideBound.Application/Promises/PromiseDeltaCalculator.cs:64–97 |

The initializeRun manifest declares roundTiesToEven for source time conversion. No inspected code comment identifies the particular −1 ms records as rounding error or tie handling.

The pre-round routing values and the selected/reference route calculation for a specific negative-c decision were not reconstructed. Already-integer v/e/p cannot distinguish the originating rounding, geometry, edge-progress or projection mechanism. Consequently no such explanation is asserted.

Safe thesis wording:

> Trên các bản ghi đã kiểm, các lần dời sớm do điều phối chỉ có độ lớn 1 mili giây. Mã có các phép chuyển đổi và làm tròn thời gian, nhưng chưa lần được nguyên nhân của các bản ghi này; vì vậy chưa quy chúng cho sai số làm tròn.

**Confidence:** high for the cited mechanisms; **CANNOT ANSWER** their causal link to those observed moves. The observed range is not extended to unaudited runs.

## Q8. Snow-run build and recovery rule

**Answer:** all eight snow runs used archived **runner-tier3-v2** and **no-worse-than-reference-v1** recovery. The manifest identifies the binary and binds the configuration; it does not contain a separately named recovery field.

For each SNOW/C-30-d20181115-s10-r{1,2,3,4}-w{14,15}/transcript-00.ndjson, initializeRun at line/ordinal 3 records the same:

| Manifest field | Value |
| --- | --- |
| binarySha256 | a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac |
| coreCommitSha | 1ce15e92d2c1459d4254bbbcd581529197257fb2 |
| policyId | ridebound-hard-vector |
| policyVersion | tier3-exploratory-v1 |
| policyConfigurationHash | a2f11a3ada0773f9b30b85c56c935058e2e931f13c907f46b2ddfff8c1285f1c |
| Simulator /seed | FleetPy 1.0.2 /7 |

The SHA-256 of C:/RideBoundData/research/runner-tier3-v2/RideBound.Runner.dll was recomputed and matches the binary hash above. S/tang3/w07/run_w07.py:40–43 names that directory and WP4 v2; S/optimize/run_forecast.py:73–74,94–102 passes them for the snow jobs. The eight corresponding forecast logs at S/optimize/forecast-logs, line 4, report **forecast off**.

Recovery is established by the canonical input binding:

| Input | Canonical SHA-256 |
| --- | --- |
| S/tang3/configs/C-30.json | f07395f5f2c967e0d89cceb4a55b23c4f896971db071d8c7876f05e20ef09884 |
| S/tang3/configs/wp4-tier3-v2.json | fb2813c4036d309490e12df77e37de1683b92b92a9ebdd71e16cad35d50ecd42 |

WP4 v2 **line 7** specifies commitmentRecovery=no-worse-than-reference-v1. Independently calculating SHA256(domain + raw commitment digest + raw WP4 digest), using domain RideBound.Wp4RunnerConfigurationBinding.v1 followed by a NUL byte, reproduces **each of the eight** policyConfigurationHash values.

Primary binding anchors: AD/ridebound_fleetpy/mapping.py:150–158; AD/ridebound_fleetpy/session.py:339,355–363,443; SRC/RideBound.Contracts/Protocol/Wp4PolicyConfigurationBinding.cs:19–44; SRC/RideBound.Runner/Program.cs:111–116; SRC/RideBound.Runner/Protocol/RunnerSession.cs:301–309 rejects mismatch.

Recovery semantics: SRC/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:54–58 allows a forced vehicle to select a changed route that worsens none of the reference route's gate overruns. This differs from the old no-recovery fixed-factor runner.

**Confidence:** high: all eight manifests checked, DLL hash checked, canonical policy binding recomputed.

## Q9. K values in the in-dispatcher forecast test

**Answer:** K is horizonBins, not B. Main enabled configurations use **K=2**; the sham uses **K=1**; OFF has no configured K.

| Configuration | K | Primary anchors |
| --- | --- | --- |
| S1 Mplus-30F smoke, d20181112-s10-r1-w07 | 2 | S/optimize/run_forecast.py:67; forecast-check-k2.json:1; corresponding S/optimize/forecast-logs/*-S1.log:4 |
| E1 Mplus-30 OFF, d20181115-s10-r4-w08 | OFF /not applicable | run_forecast.py:68,133–136; corresponding log:4 |
| E2 C-30 sham, d20181115-s10-r2-w07 | 1 | run_forecast.py:69; configs/forecast-k1-2018-11-15.json:1; corresponding log:4 |
| Tier1 C-30F and Mplus-30F, eight weekday w07 cells per arm | 2 | run_forecast.py:52,70–72; dated K=2 configs and all associated logs:4 |
| Tier2 C-30F and Mplus-30F, eight weekday w08 cells per arm | 2 | run_forecast.py:53,70–72; dated K=2 configs and all associated logs:4 |
| Eight snow C-30 runs | OFF /not applicable | run_forecast.py:73–74; all eight logs:4 |

All dates' main enabled files are S/optimize/configs/forecast-k2-2018-11-{14,15,16}.json, each line 1. Logs show the selected configuration and horizonBins, including runs that subsequently failed. A later failure does not change the configured K.

S/tang3/world/preflight_world_v1_3.py:85–89 averages K successive profile values starting with the **current** bin, then divides by the current profile value. K=2 therefore includes the current and next 15-minute bin, not two future bins after the current bin. K=1 explicitly returns ratio=1.0 at 86–87.

Without RB_FORECAST_CONFIG, lines 147–172 leave the forecast disabled and print “[forecast] off”. OFF is not K=0: the permitted configured range is 1–8, lines 99–101.

**Confidence:** high for the values and their actual log correspondence.

## Q10. Hörl & Zwick 2022 reference and strategy B

**Answer:** the venue is the **101st Annual Meeting of the Transportation Research Board (TRB 2022), Washington, D.C., January 2022**. Strategy B is **equation (7)** on numbered manuscript page 8.

Verified reference:

Hörl, Sebastian, and Felix Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling.* Paper presented at the 101st Annual Meeting of the Transportation Research Board (TRB 2022), Washington, D.C., January 2022. ETH Zurich Research Collection; IVT entry AB1659. DOI: **10.3929/ethz-b-000561639**.

Official primary sources:

- [ETH IVT publication list](https://www.ivt.ethz.ch/en/vpl/publications/working-papers.html), **AB1659**: authors, title, year, venue, location and month.
- [ETH deposited paper](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/561639/ab1659.pdf?isAllowed=y&sequence=1): repository cover gives the authors, title, 2022, Conference Paper resource type and permanent DOI.
- Its numbered page 8 (PDF index 8) states strategy B in equation (7): required drop-off time=max(updated drop-off time, latest drop-off time). Pickup relaxation belongs separately to strategy C, equation (8); constraints are (9)–(10).

**Pages:** the deposited paper has **numbered manuscript pages 1–16**, or **17 PDF pages including the repository cover**. **CANNOT ANSWER an officially assigned conference-proceedings pagination** from the accessible metadata. Do not invent a journal volume, issue or proceedings page range. “16 pp.” can describe this deposited manuscript if needed.

The title page's submission date, 27 October 2021, does not override the repository publication year and verified 2022 conference record.

The DOI landing page and DataCite API could not be fetched during the investigation. The answer is grounded in the accessible official institutional publication page and deposited PDF, not a third-party citation. An ETH link pointing to a different handle was not substituted for this DOI.

**Confidence:** high for authors, title, venue, year, DOI and equation number; high for manuscript length; **CANNOT ANSWER** proceedings-assigned pagination.

Suggested Vietnamese venue line:

> Bài báo tại Hội nghị thường niên lần thứ 101 của Transportation Research Board (TRB 2022), Washington, D.C., tháng 1 năm 2022; ETH Zurich Research Collection, DOI:10.3929/ethz-b-000561639.

This establishes the venue omitted in Chapter 3's notes. It does not connect the RideBound label C to the paper's strategy C.
