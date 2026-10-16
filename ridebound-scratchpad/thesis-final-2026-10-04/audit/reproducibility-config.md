# Verified experimental configuration and provenance

Read-only audit, 2026-10-05. This work reads supplied sources, fixtures, recorded initialization frames and published binaries; it does not build the research code or run an experiment. Full paths, file lengths, SHA-256 values, hash status, per-cell input hashes and initial fleet positions are in `reproducibility-config.json`. All hashes below are abbreviated for navigation; the JSON retains complete identities.

## Configuration suitable for a self-contained thesis table

| Item | Verified setting | Scope and interpretation |
|---|---|---|
| Source | FleetPy Manhattan input dataset, Zenodo 15187906, source archive `FleetPy_Manhattan.zip`, CC-BY-4.0 | Uses demand CSV `2018-11-<day>_sample_10_<r>.csv`, source directed network and daily travel factors. These are source samples; our 108-row derivative is a further deterministic restricted selection. |
| Cells | H6: 14–18 November 2018, four source samples/day, 08:00–10:00; Tier 2 development: 12–13 November, four samples/day, 08:00–10:00 or 17:00–19:00; T38: 49 available cells over 14–18 November and 07:00–09:00, 08:00–10:00, 17:00–19:00 | 20 H6, 16 Tier 2 development, 49 T38 fixture folders inspected directly. T38 uses 15 calibration and 34 test episodes. Local timezone is America/New_York. |
| Requests | 108/cell; party size 1 | Exact input cardinality. Arrival timestamps retain source spacing, shifted to the beginning of the cell. No uniform resampling of timestamps. |
| Network | Exactly 96 selected nodes and 9,120 directed arcs in every inspected fixture | Node cap is 96, and all 85 inspected fixtures attain it. Each arc is a shortest-path cost through the original directed source graph, whose paths may traverse source nodes outside the selected pool. No reverse or Euclidean travel-time imputation. |
| Coordinates and distance | Materialized node coordinates `(1000×index, 0)`; arc distance `10×travelTimeSeconds` synthetic metres | Time metric closure, not a faithful street geometry. Original source distances do not become the materialized physical distance. |
| Initial fleet | 8 vehicles, 4 seats each, initially empty, no accepted/onboard requests, empty route, at eight distinct selected nodes; SOC=1 | Initial locations are deterministic domain-separated HMAC ranks over selected source nodes, not depot-based or uniformly random positions. Same cell has the same initialized fleet across policy arms. Different scenario IDs/windows can change locations. |
| Pickup window | Earliest pickup = arrival; latest pickup = arrival + 600,000 ms | Fixed ten-minute physical input window; later observed late-board handling is version-specific, as described below. |
| Maximum ride | `roundTiesToEven(1.5 × static direct shortest-path travel time)` in integer ms | Rounded from the fixture's initial snapshot. It is not recalculated whenever traffic changes. For an onboard rider, the validator measures elapsed/projected ride from actual pickup. |
| Boarding/alighting dwell | **0 ms** for newly inserted pickup and drop stops; FleetPy constant boarding time **0 s** | There is a general stop-duration mechanism and possible waiting, but this experiment does not configure a fixed nonzero boarding/alighting dwell. |
| Horizon and drain | Source arrival window 7,200 s; fixture drain allowance another 7,200 s; event-driven clock | Driver drain timers: 600 s, maximum 24 steps. These timer controls are distinct from the fixture's four-hour horizon-plus-drain bound. |
| Candidate/solver controls | Up to 100 retained candidates/vehicle, up to 2 newly inserted requests/vehicle; earliest-feasible schedule; generation/validation 10,000 work units each; solver 100,000 work units; deterministic time 1,000,000 µs | Google OR-Tools 9.15.6755; exact-small mode false; service-set-stability-portfolio-v1 retention. These controls are common to the inspected H6 audited and T38 WP4 configurations. |
| Seeds and simulation | Runner master seed 7, solver random seed 7; one measured episode per arm/cell; FleetPy 1.0.2 at `053aa9d4fcfde91c5d303435d5748f9206c071b0` | Settings and repeat executions do not create independent sample units. Offers are immediately confirmed by the synthetic event driver, not observed passenger decisions. |

## Exact selection and normalization recipe

1. Reject malformed demand rows, missing/duplicate source request IDs, invalid times, rows outside `[windowStart, windowEnd)`, invalid/equal endpoint IDs, and endpoints absent from or outside the same directed strongly connected component.
2. Count eligible rows by **unordered** endpoint pair. Seed the node pool with the pair of maximum count; ties use a domain-separated HMAC rank and then numeric endpoint IDs. Extend to the 96-node cap by maximum additional eligible-row coverage with existing pool nodes; break ties by endpoint frequency, then HMAC node rank, then numeric node ID. Only nodes in the seed's directed strongly connected component are candidates.
3. Independently rank eligible rows by HMAC-SHA256 over source archive hash, demand member path and source record ordinal, with domain `RideBound.Wp6.SourceSelection.v1`. Retain the first 108 whose endpoints both lie in the locked node pool. This is **not** a simple uniform sample of all eligible taxi trips. A pool that cannot supply 108 is a normalization failure.
4. Selection and pseudonymization keys are SHA-256 of the respective UTF-8 labels. Request IDs use a separate domain. Seconds become integer milliseconds using ties-to-even rounding. Preserve event order by arrival time, source ordinal, then pseudonymous request ID.
5. Scale original directed edge travel times by the daily factor at source `simulation_time=0` and round to integer ms; form directed shortest-path closure on the selected nodes. Every inspected normalizer config has `travelFactorAtSeconds=0`, including new T38 windows.
6. Rank selected nodes using `RideBound.Wp6.FleetPlacement.v1`, the selection key, archive hash, **scenario ID** and numeric source node ID; place `veh-000` through `veh-007` at the first eight distinct ranks.

For the 40 attempted extra T38 windows, only `source.node-cap-prevents-target` is retried, with selection and pseudonymization labels suffixed `-retry1`, `-retry2`, then `-retry3`. Eleven cells remain excluded after all four attempts: 15 November 17h r1–r4; 17 November 07h r1, r2, r4; 18 November 07h r1–r4. Twenty existing 08h fixtures plus 29 successful extra fixtures yield 49. This rule concerns input construction, not outcome-based run selection. Partition source-trip overlap is audited separately in `evidence-audit.md`.

## Execution versions must remain distinct

| Family | Travel information and clock | Gate/recovery and execution handling |
|---|---|---|
| H6 original and later `-v2` re-execution | One static initial travel snapshot, no measured-day factor updates | B1 `rolling-cost`; C1 hard conduct budget plus confirmation locks. Original sealed verdict belongs to H6 v5; v6 changed entered-edge adapter mapping and source-seal construction and re-executed the design. **The Runner DLL is identical across v5/v6.** |
| Tier 2 | Network-wide factor `(f(day, time)/f(day, windowStart))^k`, k=0 or 1; updates at the first existing decision trigger at/after each 900-s boundary; last measured factor held during drain | `conduct-30`, visible cap and one-/two-sided deadline arms use the deadline Runner. No no-worse recovery or `lateBoarding: record-v1` configured. Commitment rejection and physical `window-wall` remain separate outcomes. |
| T38 | Measured-day/window world, exponent 1, sigma=0, shockRate=0, worldSeed=101. Wrapper v1.2 inherits v1.1 clock stops exactly at each 900-s bin and validates day/window; measured terminal ratio held during drain | All five arms use Runner tier3-v2 and WP4 `commitmentRecovery: no-worse-than-reference-v1`, `lateBoarding: record-v1`. Adapter drops the original-window-anchored drop latest-arrival check in this mode; actual-pickup-plus-max-trip remains. Observed late boarding is recorded. Completed execution therefore does not assert every original physical window stayed satisfied. |

U/C/M+/V in T38 retain confirmation locks `[vehicle,pickupStop,pickupEta]`; U removes the tested temporal cap but is not a fully unconstrained policy. C-30 charges `decisionInduced` drop movement; M+-30/60 sets `dropEtaDeadlineSlackMs`; V-30 charges `customerVisible` drop movement. Tier 2 `visible-30.json` and T38 `V-30.json` have different byte hashes but their parsed JSON objects are equal. A shared adapter ID/version does not establish identical adapter source bytes.

## Verified hashes and provenance status

| Artifact | SHA-256 prefix | Status |
|---|---|---|
| Source ZIP, 408,878,341 bytes | `d9e86f33645e5eec…` | Recomputed whole file; matches registered source identity. |
| Framed five-file normalizer source | `34517a832014c78a…` | Independently recomputed; matches every inspected fixture. |
| H6 `freeze-receipt-v5.json` in **E:/Code/RideBound** | `84f6eff31addbdd1…` | Recomputed receipt bytes. Current C checkout copy has different bytes and is not a substitute. |
| H6 `freeze-receipt-v6.json` in E checkout | `e7bc41be2d3c4305…` | Recomputed receipt bytes; explicitly supersedes v5. |
| H6 DLL / 429-file publish tree | `8445f05399dcdab8…` / `81c021ddb5dd9a27…` | Both recomputed from `E:/RideBoundData/wp9/runner/h6-confirmatory-v1`; match v5 and v6 Runner pins. |
| H6 v5/v6 adapter tree seals | `7fc7e1b8f84ff777…` / `ca81bd3f1e1a053c…` | **Recorded receipt fields only** in this audit. v5 included compiled bytecode; its historical adapter seal cannot be reconstructed from source commits. |
| Tier 2 DLL / 429-file publish tree | `8b00dfbfd461ae0d…` / `8fa5dd288b0ae603…` | DLL recomputed; all 429 file hashes/lengths match saved manifest. Historical tree hash includes final LF. |
| T38 DLL / 429-file publish tree | `a631038b6ea4850f…` / `ac251ef32a4865ea…` | Independently recomputed from `C:/RideBoundData/research/runner-tier3-v2`; match saved manifest. This later tree algorithm omits final LF. |
| H6 C1 WP4 / T38 WP4 | `abfd1c608e3c0e43…` / `66e9b59249d9491d…` | Recomputed configuration files; recovery and late-board fields differ. |
| C-30 / M+-30 / M+-60 / V-30 / U | `d6124f3f964d8385…` / `cc7d7838836137f4…` / `f8d4c74913224cdf…` / `2462484ab8d7e61e…` / `998a0a94e7865c3b…` | Recomputed T38 configuration files; match pinned driver values. |
| T38 split / gamma | `b72ac0f731fa7425…` / `2bdd3b0e83a6cd3d…` | Recomputed current bytes; match sealed values. |

Raw sampled `initializeRun` frames were individually hash-checked. They report H6 original core commit `e584a66a…`, H6 v2 `38d517d8…`, Tier 2 `41a4e11e…`, T38 `1ce15e92…`. T38's recorded repository inventory is `0da63eaf…`; the later preserved no-worse source checkout is `24aa7471…`. These fields describe different boundaries, and a Git HEAD alone is not a replacement for the published binary/configuration identity. This audit does not claim a full transcript integrity sweep or independent simulator replication.

## Source locations and checks

Key code references are in `C:/Code/RideBound-noworse`: `FleetPyManhattanNormalizer.cs` lines 580–638 (eligibility), 650–763 (selection), 423–451 (request constraints), 461–488 (fleet), 375–399 (closure), 1055–1118 (rounding/HMAC); `tools/RideBound.Wp6Normalize/Program.cs` lines 182–206 (keys); `InsertionCandidateGenerator.cs` lines 520–531 (zero dwell); `actual_fleetpy_medium_preflight.py` lines 114–141 (synthetic network), 235–241 (boarding), 459–479 (initial fleet); `ridebound_fleetpy/fleet_control.py` lines 948–989 (ride constraints/late-board mode). The JSON stores absolute file paths and byte hashes for these sources.

Wrapper and preparation references under `E:/Code/Report_INT3508/ridebound-scratchpad`: `deadline/preflight_drift_v2.py` lines 58–87 and 112–130; `tang3/world/preflight_world_v1_1.py` lines 1–22 and 44–64; `preflight_world_v1_2.py` lines 1–24 and 39–66; `tang3/calib/panelA/normalize_panelA.py` lines 1–8, 29–44, 62–75; `prepare_panelA.py` lines 1–14, 41–44, 95–111; `tang3/t38/run_t38.py` lines 1–13, 38–57, 86–114. Published tree algorithms are in `tang3/runner_manifest.py` and the H6 builder.

Direct assertions pass for all 20 H6, 16 Tier 2 development and 49 T38 fixtures: 108 requests, exactly 96 nodes/9,120 arcs, party size one, 600-s window, rounded 1.5×static-direct maximum ride, eight initially empty four-seat vehicles, exact HMAC placement and matching scenario/driver content hashes. This includes all 5,292 T38 requests. The audit hashes 37 distinct extracted source files and the full source ZIP. No research code change occurred, so no research test/build or new experiment was required.
