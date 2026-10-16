# R22 - independent code review by Codex

**Verdict: ACCEPT WITH CHANGES.** The production implementation satisfies the requested default-off objective-order change by inspection. I found no production-code defect requiring an edit. The changes required before declaring Gate 0 passed are to its comparison procedure and provenance record: explicitly permit the new DLL identity, require unchanged configuration/input identities, and bind that DLL and its complete published tree to the reviewed source.

This is a read-only review of the worktree. I did not build, test, commit, publish, modify the worktree, or run FleetPy. The test results below are inspected implementer logs, not tests executed by me.

## 1. Reviewed snapshot and evidence

Paths used below:

- `R/` = `C:/Code/RideBound-costfirst/`.
- `S/` = `E:/Code/Report_INT3508/ridebound-scratchpad/`.
- `D/` = `S/optimize/codex-debate/`.
- `A/` = `C:/RideBoundData/research/tier3-t38-v1/`.
- `H/` = `E:/Code/RideBound-deadline/`.

Branch: `research/tier3-cost-first`; HEAD: `761915cbb89d03f410cd9989ad1cf136e6234bf8`. The diff contains eight modified tracked files: three production files, three test files, and two documentation files.

The evidence refreshed during this review. ROUND22 names eight new tests and `after-test.log` (1033/1033); the final artifacts contain **nine** new tests, `after-test-final.log` (1034/1034), and `mutate-costfirst-2.log`. I reviewed the refreshed tests and logs. The three production patches are unchanged from the initially inspected patch. At the final read, the saved patch is byte-identical to the live LF-normalized Git diff. The apparent early artifact mismatch is therefore resolved, not an outstanding finding.

| Artifact | SHA-256 |
|---|---|
| Final live diff and `S/tang3/stage1b/costfirst-diff-2026-10-11.patch` | `c48042af4e7cee2db01bdee5efb804dac703d80c8c657276fc5718816e1ad690` |
| `S/tang3/stage1b/IMPLEMENTATION-REPORT.md` | `fe77dfc0a5c5d962b91836c0fef44dab47d78eecca3ad1575baa1547221217e7` |
| `S/tang3/stage1b/after-test-final.log` | `ed034fcc988d18197a7eeeb5f533af92c309f36fea4aa5e2a14e9d31fb995bdc` |
| `S/tang3/stage1b/mutate-costfirst-2.log` | `896da6e61524491a84d0ee15a09c4545f57bc15e477e57291a95c4bf3ae38b23` |

This verdict applies to that snapshot. Later source changes require an updated diff and relevant validation evidence.

## 2. Findings, ranked by severity

### F1 - P1: the cited comparator will reject a correctly equivalent rebuilt OFF runner

Locations: `S/tang3/stage1b/IMPLEMENTATION-REPORT.md:266-270`; `S/optimize/compare_equivalence.py:33-40,53-66`; `H/simulators/fleetpy-ridebound/ridebound_fleetpy/session.py:482-483`.

The report correctly says a rebuild changes `binarySha256`, but its statement that `compare_equivalence.py` ignores the relevant identity/hash fields is incomplete. The comparator removes keys ending in `Hash` or `hash`. **`binarySha256` matches neither suffix** and remains in the decoded `initializeRun.payload.manifest`. It will make the `frames` component unequal even if every fleet decision and ledger entry is equivalent. `coreCommitSha` is also preserved.

I executed only the comparator's pure `strip` function, extracted through Python AST without importing its application modules. On a copy of the archived initialization, changing only `binarySha256` changes the stripped result. This confirms the mismatch without running a simulation or altering any artifact.

**Required change:** specify and freeze a Stage-1b comparison profile that permits a difference only at `initializeRun.payload.manifest.binarySha256`, after independently checking each value against its actual DLL and complete runner-tree manifest. Use a reviewed wrapper/copy of the comparator; retain the archived comparator and transcripts. Do not waive the entire frame comparison.

### F2 - P1: blanket hash removal cannot certify the required OFF configuration equivalence

Locations: `S/optimize/compare_equivalence.py:38,47-60`; `R/tests/RideBound.Runner.Tests/Configuration/Wp4RunnerConfigurationTests.cs:680-745`.

The same suffix rule removes `policyConfigurationHash`, `scenarioContentHash`, `graphSnapshotHash`, `travelTimeSnapshotHash`, and nested snapshot hashes. These are controlled configuration/input identities, not merely run salts. The archived binding unit test is valuable but does not prove that a future Gate-0 job actually used those inputs.

Using the same pure-function probe, changing any one of the four initialization configuration/input hashes leaves `strip` unchanged. This demonstrates a blind spot in that comparison component; it does not establish that every possible changed-input run would also pass the other components.

**Required change:** require exact controlled hash equality and actual input-byte verification separately, or preserve those fields in the Stage-1b normalization. Especially, require the archived C30/U binding in the actual initialization; explicitly writing `stability-first` is a failure of the OFF configuration gate even if decisions happen to match. Section 5 gives the complete criterion.

### F3 - P2: freeze a separate source-to-runner provenance record

Locations: `S/tang3/stage1b/IMPLEMENTATION-REPORT.md:263-275`; `H/simulators/fleetpy-ridebound/ridebound_fleetpy/session.py:140-156,339-340,482-483`; `S/tang3/t38/run_t38.py:90-103,125-128`.

The report already identifies this open issue correctly. `coreCommitSha` is the HEAD of the repository root used by the harness; it does not identify the source used to publish an externally supplied Runner DLL. All four inspected references name `1ce15e92d2c1459d4254bbbcd581529197257fb2`, while the runner under review is based on `761915c` in another worktree.

**Required change:** for the proposed criterion, preserve the frozen harness root, inventory, adapter and wrappers, and retain its archived `coreCommitSha`. Add an external provenance receipt with the eventual runner-source commit, base commit, reviewed diff identity, publish command/toolchain, DLL SHA, and full runner-tree TSV/hash. Verify the tree before jobs. Record the harness commit and runner-source commit as separate facts. Do not present the initialization's harness commit as the new runner's source commit. Freeze any alternative root/provenance policy before execution rather than broadening exclusions after a failure.

### F4 - P3: the new tests do not exercise the actual bounded RunnerSession/OR-Tools/adapter path

Locations: `R/tests/RideBound.Algorithms.Tests/Policies/SolverBackedFleetSelectionTests.cs:730,796`; `R/tests/RideBound.Algorithms.Tests/Oracle/ExactSmallCommitmentDifferentialTests.cs:385-396,1581-1594,1618-1629`; `S/tang3/stage1b/IMPLEMENTATION-REPORT.md:329`.

The selector tests use an exact test solver. The differential tests use an enumerator and `ExactSmall` generation. They establish meaningful ranking and safety properties but do not demonstrate the real OR-Tools work-budget path, diagnostic encoding through RunnerSession, retained candidate generation under the Tier-3 settings, or adapter acceptance of the cost-first configuration.

**Recommendation within the existing job plan:** use the two planned ON smokes to verify those integration boundaries and correct initialization bindings, alongside the four OFF jobs. Inspect solver status, execution path, bounds and omission evidence. A focused cost-first exhausted-budget/fallback test would be useful if that path is a material concern. This is a coverage limit, not an observed implementation failure or a demand for extra simulation jobs.

## 3. Production diff verification

I read every production hunk and followed its consumers. The substantive ranking edit is one additional guard on the existing HardVector stability case.

| Requirement / changed path | Verification | Assessment |
|---|---|---|
| New enum and selector default | `R/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:18-27,83-94`: new order enum; omitted argument is `StabilityFirst`. | Meets OFF default. |
| Public selector validation | Same file `:106-117`: undefined order rejected; CostFirst requires HardVector. Existing per-candidate C1/C2 assessment check remains at `:284-296`. | No silent profile downgrade or assessment bypass. |
| Forced-reference level and activation | Same file `:304-323`: unchanged activation requires C1/C2 and at least one candidate whose assessment is forced; minimizes forced count before acceptance. | Preserved, including the activation condition. |
| Accepted-request priority | Same file `:325-331`: unchanged maximize/sum of each candidate's new-request count. | Preserved. |
| Intended removed levels | Same file `:347-362`: HardVector adds worst-utilization and all ten ordered revision dimensions only when hard treatment is active and order is StabilityFirst. CostFirst skips that case. | Removes exactly the intended stability ranking; no weighted-cost substitute. |
| Operational cost and ties | Same file `:397-417`: unchanged operational-cost min/sum, then one ordinal candidate-ID rank per ordinal vehicle. Option contributions are built from the retained level list at `:419-432`. | Preserved values, senses, aggregation and deterministic ties. |
| Descriptive selected-plan measures | Same file `:478-509`: HardVector mapping still reports revision and worst utilization under active hard treatment, even when they were not ranking objectives. | Correct distinction between ranking and reporting. |
| Policy-options default/guards | `R/src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:87-102,161-170,200-205`: get-only option, default StabilityFirst, undefined values rejected, CostFirst restricted to C1. | No mutable bypass. |
| Generator, retention and accounting | Same file `:287-309,378-404`: generation receives the same generation options; new order first influences selection after generation, filtering and accounting. | Unchanged at the same decision state. Future trajectories may differ after an ON selection. |
| HardVector profile, assessor and recovery (b) | Same file `:344-374`: existing hard assessment remains, with the same safety-no-op, forced recovery and no-worse flags; C1 still selects HardVector. | Preserved. |
| Full validator and option propagation | Same file `:392-408`: same full-fleet validator, policies, physical/commitment validators, forced vehicles and no-worse flag; only order is added to Select. | Gates and locks remain in force. |
| Evidence snapshot and fallback consumers | Same file `:428-437` captures the actual problem. `R/src/RideBound.Algorithms/Policies/RollingCostDecisionModels.cs:110-245` validates the portfolio/solution without imposing the old HardVector level count. `R/src/RideBound.Application/Optimization/CandidateSelectionExecution.cs:287-315,434-443` retains validated fallback behavior and reads the problem's own objective levels when comparing greedy choices. | No discovered fixed-level assumption broken by the shorter list. Exact optimality is not promised for a fallback. |
| WP4 allowlist/literals/parsing | `R/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:46,69-74,374-388`: optional field; exact two string literals; absence is StabilityFirst; CostFirst requires solver-backed C1. `Text` at `:746-758` rejects empty/whitespace/non-string values. | No coercion or silent fallback from an invalid value. Canonical JSON validation also precedes parsing. |
| Run-seed option reconstruction | Same file `:228-237,430-439`: both construction sites pass the order. `R/src/RideBound.Runner/Protocol/RunnerSession.cs:897-904` uses either the reconstructed or stored options. | Both Runner option paths retain it. |
| Canonical bytes and binding | WP4 Decode `:245-249` hashes canonical input before reading the optional field; no default key is inserted. Binding `:189-195` is unchanged; `R/src/RideBound.Contracts/Protocol/Wp4PolicyConfigurationBinding.cs:19-43` still hashes domain + commitment digest bytes + WP4 digest bytes. | Absent-key bytes/hash/binding preserved. Explicit StabilityFirst is a distinct configuration identity. |
| Late boarding and final validation | WP4 `:363-372` is unchanged. RunnerSession `:956-971` still performs final commitment validation with the existing no-worse setting. Adapter service-bound handling remains `H/.../session.py:159-169`. | No new order branch changes late boarding or validation. |
| RollingCost / RevisionPenalty / SoftHardHybrid | Selector's existing RevisionPenalty and SoftHardHybrid cases `:335-345,364-394` are unchanged. CostFirst is rejected at parser, options and public selector boundaries. | Existing OFF paths retain their hierarchy. Explicit StabilityFirst is accepted as the harmless default order; this does not add CostFirst to those profiles. |

For U without applicable hard limits, StabilityFirst already omits utilization/revision. CostFirst has the same level list there. Forced treatment can still activate through a deadline/recovery condition; it is not conditioned on the presence of a budget limit and remains retained.

The no-worse utilization exemption still affects assessment, but its ranking effect disappears when that entire level is skipped. A forced vehicle can consequently choose a cheaper no-worse changed route even if it brings other riders closer to their caps. That follows from the authorized objective-order change; it is not removal of their gates. This limitation and the restriction to the same retained portfolio are correctly documented at `R/docs/18-status-and-decision-log.md:5222-5228`. Cost-first is not an exhaustive search over omitted candidates.

No missing production validation or silent OFF behavior change was found. This is a source-review conclusion, not empirical certification of all rebuilt-run behavior.

## 4. Tests, mutation evidence and remaining coverage

The originally requested eight tests are present. The refreshed ninth test is also reviewed.

| Test (live file:line) | What it pins | Limit |
|---|---|---|
| Selector `Stability_first_keeps_the_exact_hard_vector_level_list_and_is_the_default`, `R/tests/RideBound.Algorithms.Tests/Policies/SolverBackedFleetSelectionTests.cs:521` | Exact 16 names/order; default equals explicit StabilityFirst levels and contributions; expected stable selection. | One discriminating synthetic portfolio, not archived-run replay. |
| `Cost_first_drops_only_the_utilization_and_revision_levels`, same file `:548` | Exact five-level CF list; every retained level and each option's contribution equals the corresponding SF entry; same options; cheaper selection; descriptive revision/utilization retained. | Forced vehicle has only its forced option, so this fixture alone does not test forced avoidance against a viable alternative. |
| `Cost_first_keeps_the_forced_level_condition_and_equals_stability_first_without_hard_limits`, `:602` | Forced level absent when no assessment is forced; no-hard-limit order/selection equality. | Does not cover every deadline/recovery state. |
| `Cost_first_is_rejected_outside_the_hard_vector_profile`, `:638` | RollingCost, RevisionPenalty, SoftHardHybrid rejected; undefined order rejected. | Static API boundary coverage. |
| `Cost_first_policy_options_are_valid_only_for_C1_and_default_to_stability_first`, `:666` | Default order, valid C1+no-worse combination, invalid policy/order guards. | No full run. |
| `Cost_first_C1_ranks_the_same_gated_candidates_by_cost_and_picks_a_cheaper_plan`, `R/tests/RideBound.Algorithms.Tests/Oracle/ExactSmallCommitmentDifferentialTests.cs:373` | 64 exact-small seeds; same eligible IDs, prune ID/code pairs and forced vehicles; same accepted counts; CF cost <= SF; independent C1 comparison; Runner-like validation; at least one strictly cheaper plan with a real stability trade-off. | No-worse flag is off here; prune payload details are not all compared. Exact enumeration gives no budgeted-solver cost guarantee. |
| Added ninth: `Cost_first_under_no_worse_recovery_keeps_the_forced_treatment_and_the_no_worse_gate`, same file `:1376` | Active hard treatment plus recovery (b); same options; retained forced level; CF has no stability levels; serves new rider; passes no-worse validation; forced breach projections are no later than reference. | Both orders select the same plan in this state. It covers invariants, not a changed ranking during recovery. |
| `Selection_objective_order_is_optional_stability_first_and_cost_first_only_for_C1`, `R/tests/RideBound.Runner.Tests/Configuration/Wp4RunnerConfigurationTests.cs:545` | Parsing, default, seeded reconstruction, unchanged policy/budgets/recovery/generation; distinct declared-key hashes; invalid values; B1/C2 rejection. | Null/object/array/whitespace and all non-C1 config variants are not each separate test cases, though the inspected shared validation handles them. |
| `A_configuration_without_the_order_key_keeps_the_archived_tier3_bindings`, same file `:680` | Literal historical canonical WP4 hash; literal commitment and combined binding hashes for C30/U/C120; absence stays StabilityFirst; CF has a different hash. | Configuration identity test; does not replay decisions or prove Gate-0 jobs consumed those files. C120 value is derived relative to these T3.8 references. |

### Independent check of the archived constants

I parsed the embedded literal at `Wp4RunnerConfigurationTests.cs:650-676` and the actual scratchpad WP4 file. Their canonical bytes are equal. The JSON here uses plain ASCII keys/values and integer/boolean values; sorted compact JSON matches the inspected canonical writer's rules for these documents. I independently applied the binding's domain-separated formula.

WP4 v2 file SHA-256:

`66e9b59249d9491d520f3ed592e8c878a0d3b100e39432d5f4b73321617b4518`

Canonical WP4 v2 SHA-256:

`fb2813c4036d309490e12df77e37de1683b92b92a9ebdd71e16cad35d50ecd42`

| Arm | Canonical commitment SHA-256 | Combined OFF binding |
|---|---|---|
| C30 | `f07395f5f2c967e0d89cceb4a55b23c4f896971db071d8c7876f05e20ef09884` | `a2f11a3ada0773f9b30b85c56c935058e2e931f13c907f46b2ddfff8c1285f1c` |
| U | `7fc79a433abe1796830ecceeac280da0e0af3871daf268dda8d6fc93b270370d` | `251b331eb56fe870e734d651bf6937e95304919ed92967b2f3b0d0b9da1ac346` |
| C120 | `8dc9350b1d6b656b30d37ad23bac0dc4e4188f222427be47d6b007e060f2a5a2` | `a9ac58b33558c6ec2d604ee7fe3e7fdb02deaecfd866ea73282b911326ed9010` |

The repository C30 reference and scratchpad C30 file are byte-identical. I decoded initialization in all available `A/C-30-*` and `A/U-*` transcripts: 51/51 C30 initializations carry the C30 binding above; 34/34 U initializations carry the U binding. These counts include the available C30 rerun directory; they are archive initialization counts, not a count of unique successful panel cells. The four Gate-0 references are separately verified below.

Pinning independent archived literals avoids the weak test pattern of comparing two results produced only by the new implementation. The test is strong for the absent-key binding requirement.

### Logs and mutations

`baseline-test.log` records 1024 passed, one failed, total 1025. The failure is the existing clean-tree-sensitive `StrictBagItBundleTests.Source_inventory_binds_dirty_worktree_files_not_only_base_commit`; its unconditional `Assert.True(inventory.GitDirty)` is at `R/tests/RideBound.Benchmarking.Tests/StrictBagItBundleTests.cs:32`. It passes with this dirty worktree. That is an environmental precondition of the existing test, not a cost-first fix.

`after-test.log` records 1033 passed. The refreshed `after-test-final.log:21-64` records nine project totals summing to **1034/1034**, exit 0: Algorithms 208 and Runner 135, respectively +7 and +2 versus baseline. I verified the arithmetic and logs; I did not rerun them.

Both mutation logs record seven killed mutants. Final `mutate-costfirst-2.log:1-36` shows named test failures for:

1. CF ignored in the selector switch.
2. Forced level incorrectly removed in CF.
3. Decide fails to pass the order.
4. Seeded options drop the order.
5. Parser maps CF to SF.
6. Parser admits CF to other solver policies.
7. Operational-cost level incorrectly removed in CF.

The harness requires one exact replacement anchor and restores the original bytes in a finally block with a SHA check (`mutate_costfirst.py:55-59,72-74`). Its generic killed criterion is any nonzero exit (`:67`), which could misclassify infrastructure/compile failures in another run. Here the provided logs show completed test counts and concrete xUnit failures, so the reported kills have substantive evidence.

The mutation set does not separately perturb accepted-count values/order, candidate-ID tie values/order, OFF defaults, binding-domain construction, or no-worse rejection itself. Retained-level contribution equality already provides useful protection for the first two. Mutation kills are evidence for these seven faults, not a coverage percentage for every possible defect.

Useful remaining coverage includes a deliberate CF forced-vs-unforced priority competition, an acceptance-vs-cheaper-no-op competition, an equal-cost tie, bounded/fallback execution, emitted evidence, and a discriminating cheaper plan under no-worse recovery. These are recommendations; existing static preservation plus the meaningful tests support accepting the production change. The required real-run equivalence evidence remains pending.

## 5. Exact Gate-0 criterion for the four OFF jobs

This preserves the R17/R18 panel: `D/claude-work/R17-FINAL-VERDICT.md:223,259` and `D/codex-work/R18-CONFIRM-CODEX.md:225-230`. Compare each newly built OFF run with the corresponding archived run, using U/C30 x the two cells below. Do not compare U with C30 as an equivalence pair.

| Archived reference directory under A/ | Frames, including initialization/checkpoints | Verified transcript SHA-256 |
|---|---:|---|
| `U-d20181116-s10-r1-w08` | 2020 | `c82d27969f6e8b8be34606a4496f2599772a0016e9eddf0f1f0bc6a261921740` |
| `U-d20181116-s10-r1-w17` | 2284 | `6ec5242cb60356759d1da6c38d295cebc138397fe3c254e6126a56f56780f2e1` |
| `C-30-d20181116-s10-r1-w08` | 2035 | `42ba5f1aab73d363d1c8a355d1646e8bb71bae7a6b5a0cda50be8448fc45272b` |
| `C-30-d20181116-s10-r1-w17` | 2146 | `371565dd40299e7755aaafefeebb4481bfdcdcb379b7d8d892099bbb4607ebbc` |

For these references, I verified all bundle-manifest file lengths/SHA-256 values, every transcript frame SHA/length and contiguous ordinals beginning at 1. Summary status is pass and run status is succeeded for all four. These checks validate the reference artifacts' transport integrity; they are not a new four-pair Gate-0 comparison.

### 5.1 Preconditions for each pair

Both runs must complete successfully, contain a valid final checkpoint, and pass transcript/audit consistency checks. Verify raw frame checksums, lengths, directions and contiguous record ordinals; verify each bundle against its own manifest. Each run must have internally consistent ACK/decision links and publication/breach references. `audit_vep.py:45-65,68-126` checks frame hashes and publication/ledger consistency, but it does not by itself check every transport/protocol identity relationship.

Use the unchanged v2 WP4 **with the key absent**, the unchanged matching commitment file, original fixtures/derivative artifacts, driver, measured-day world, seed 7, one repeat, same simulator/runtime/adapter/wrappers, same budgets, retention, booking-confirmation trigger, recovery (b), and late-boarding setting. Check actual file bytes against frozen file hashes, including inputs outside the transcript. Configuration validation and byte equality are separate from behavioral equality.

The harness root for this criterion stays H/ at archived commit `1ce15e92d2c1459d4254bbbcd581529197257fb2` with archived inventory identity `0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe`. Record the rebuilt runner provenance separately as in F3. All four OFF jobs and subsequent matched Stage-1b arms use the same newly published runner tree.

### 5.2 Fields to match or normalize

| Field / object | Rule |
|---|---|
| Initialization `policyConfigurationHash` | Must equal the archived binding for the arm, as listed in section 4. Recompute from actual canonical WP4/commitment bytes. Never waive it in an OFF job. |
| Initialization `scenarioContentHash`, `graphSnapshotHash`, `travelTimeSnapshotHash` | Must match the corresponding reference exactly. Require source-scenario/artifact identities to match separately as well. |
| Event travel snapshots' `snapshotHash`, final state's `travelTimes.snapshotHash`, `expectedInitialTravelTimeSnapshotHash` | Must match exactly at the corresponding position; underlying snapshots/events must also match. These are stable inputs/content, not excluded salts. |
| `coreCommitSha`, adapter/simulator IDs, versions and upstream commit, protocol/schema versions, policy ID/version, seed, cost-unit and conversions, negotiated capabilities | Must match exactly under the frozen-root criterion. |
| `initializeRun.payload.manifest.binarySha256` | Sole permitted runner-provenance difference in decoded initialization. Old value must verify against the archived DLL; new value against the frozen new DLL/tree. Replace only this path with a common comparison token after verification. All four new jobs must agree on the new value. |
| Envelope `runId`, publication/breach identifiers | Raw values may differ as run salts. Preserve counts and logical reference relationships. Map publications to stable request/history-entry identities and breaches to their logical incident records, or validate links per run and compare the complete corresponding records without raw ID text. No arbitrary ID/type removal. |
| `publicationIds` in certificates | Compare normalized membership/cardinality after mapping IDs; raw salted order may differ. Do not let removal of the whole field hide missing/extra references. |
| Manifest/state/decision/checkpoint hashes derived from salted identities or changed manifest binary identity | Raw digest equality is not required. Require each run's digest/ACK/chain relationships to be valid and its underlying normalized content to compare equal. This covers `manifestHash`, state hashes, input/proposed state hashes, `stateBeforeHash/stateAfterHash`, `decisionHash/previousDecisionHash`, and `checkpointHash`. |
| All other decoded fields | Must match exactly. In particular do not ignore request/vehicle/candidate/stop IDs, event sequence/epoch, simulation time, promises, revision amounts, certificates, breach reasons/projections, pruning, generation loss, solver status/bounds/work or execution path. Unclassified hash fields require review before adding an exception. |
| Decision `actions` | Canonically sort normalized actions and compare as a multiset, retaining duplicates. This follows the existing comparator's salted action-order treatment. |
| Route/service order, event order, ledger/history order, frame order | Preserve order and require equality. Do not sort route sequences or use aggregate counts as a substitute. |
| Output labels/paths, wall time/CPU/RSS, transport frameBase64/length/SHA, aggregate salted semantic digests | Not cross-run behavioral equality fields. Verify each artifact's own integrity; compare semantic content and statuses separately. Record resource measurements without demanding equal wall-clock usage. Do not extend this exclusion to simulation times or deterministic solver accounting. |

The four inspected initialization manifests all use archived DLL SHA `a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac`. That old identity does not become an allowed value for the new DLL; each is checked against its own frozen artifact.

### 5.3 Required behavioral equality

After the above checks/normalization, **all** of the following must be exactly equal in every pair:

1. The complete ordered `fleet_decisions` list, including each integer simulation time and fleet-action fingerprint (`pilot_analyze.py:36-54`).
2. Every signed v/e/p audit row, including request, coordinate, revision sequence/kind/time, v/e/p, signed differences and closure flag (`audit_vep.py:84-123`).
3. The completed served set and each passenger-alighted time; also lifecycle outcomes and boarding times as contained in the matched event/state content.
4. Every decoded frame, its direction and position, including objective diagnostics and checkpoints, after the narrow normalization above.
5. The complete final online state, commitment ledger and incident ledger after the same normalization. The final checkpoint is already included in frame equality; report ledger equality explicitly for the R17/R18 gate.

There is no rounding, epsilon, differing-decision allowance, partial-prefix pass, or wall-time substitution for these behavioral checks. If any pair fails, report the first difference and stop Stage-1b progression under the stated plan. A missing/failing job is not an equivalence pass.

### 5.4 How to use the existing comparator safely

Retain `compare_equivalence.py`'s five comparison components (`:47-75`). A reviewed Stage-1b wrapper can:

- Perform all frozen-input and provenance checks before normalization.
- In decoded frame copies, replace the verified initialization DLL SHA at its exact path with one common token.
- Preserve/recheck the stable hashes currently lost by suffix stripping.
- Normalize salted identity references while preserving membership and record content.
- Run the same five exact comparisons, with explicit final-ledger reporting.

Calling the existing comparator unchanged will produce the F1 failure. Ignoring its entire `frames` result would lose important OFF regression checks. A blanket additional removal of all SHA/commit fields would also lose controlled provenance/input checks.

Before jobs, verify the new comparison profile with in-memory positive/negative controls: an identical copy passes; only the permitted DLL identity difference passes after provenance verification; a changed policy/config/input hash, one decision time, one route stop/order, one ledger value, one alight time, or a missing publication reference fails. The current self-test covers decision/alight times and U-vs-C30 only (`compare_equivalence.py:86-109`), so it does not establish the rebuild exception or stable-hash checks. These are comparator checks, not extra FleetPy jobs.

## 6. Cost-first configuration and interpretation

The ON WP4 must be the v2 document plus exactly:

```json
"selectionObjectiveOrder": "cost-first"
```

Removing that single property must restore identical canonical v2 bytes. Preserve every other property and arm commitment configuration. Do not use explicit StabilityFirst in OFF jobs.

For a document with exactly that one addition, I independently derive:

- Canonical CF WP4 SHA: `16dcb7e3337763aab7889f7528365dced2aa49028db6dbf390f8b3dce79b3140`.
- CF-U binding: `90b290d7e63f6885ac8e93e18017d55dddc54c27a05d8476a65dcf7d802e2df5`.
- CF-C30 binding: `e6b33be5649dc2b1208b42b90cef227d00721cba59e4340fdbc4e96f21796f76`.

These are derived expectations, not receipts from published/ON runs. Whitespace can change a file SHA without changing its canonical hash, so freeze the eventual physical file separately.

The order cannot always be identified from one diagnostic level list: unbounded SF has the same short list, and exhausted-budget diagnostics can omit levels (`R/docs/18-status-and-decision-log.md:5219-5221`). Identify the run through its verified configuration binding; use objective diagnostics as supporting evidence. No new evidence profile is required.

An exact CF optimum over the same eligible portfolio and leading objectives cannot cost more than the exact SF solution. The tested 64 seeds support that local property. A real bounded solver, fallback, retained portfolio, and later diverging trajectory do not imply lower realized episode cost, identical service, or better arrival outcomes. The implementation and documentation appropriately make no benefit claim.

## 7. Acceptance conditions

1. Correct the Gate-0 comparison specification for F1/F2 and validate the narrow profile before running the four OFF jobs.
2. Freeze and verify separate harness and rebuilt-runner provenance as in F3.
3. Require all four paired OFF comparisons to pass the exact criterion before advancing the authorized Stage-1b study; use the two already planned ON smokes for actual integration evidence.

No production-code edit is requested by this review. The refreshed nine tests and seven targeted mutation kills are credible evidence for the implemented source change. Gate 0 and ON simulation validation remain pending; this verdict does not certify them as passed.
