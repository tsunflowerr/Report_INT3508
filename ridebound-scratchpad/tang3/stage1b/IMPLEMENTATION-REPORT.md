# Stage 1b — cost-first selection order option (ADR-078, Proposed) — implementation report

Date: 2026-10-10/11. Implementer: Claude (Stage 1b, owner-approved scope). Nothing was committed, pushed or published.

## 1. Worktree

- Path: `C:/Code/RideBound-costfirst`
- Branch: `research/tier3-cost-first`, created from `761915c` (HEAD of `research/tier3-no-worse`) with
  `git -C C:/Code/RideBound-noworse -c core.autocrlf=false -c core.eol=lf worktree add -b research/tier3-cost-first C:/Code/RideBound-costfirst 761915c`.
- Right after creation `git status` was clean. A byte check of all 1,714 tracked files against their `HEAD` blobs found
  0 mismatches (no CRLF conversion). Every edited file is still LF-only, without a BOM.
- Not touched: `E:/Code/RideBound`, `E:/Code/RideBound-deadline`, and the working files of `C:/Code/RideBound-noworse`.
  The only change in `C:/Code/RideBound-noworse` is the worktree/branch registration that `git worktree add` creates.
- Uncommitted changes: 3 production files, 3 test files, 2 docs (see §5).

## 2. Baseline (before any change)

The full baseline log is in `baseline-test.log` in this folder. The run was on AC power (BatteryStatus 2, 100 %).

| Test project | Passed | Failed | Skipped | Total |
|---|---:|---:|---:|---:|
| RideBound.ArchitectureTests | 10 | 0 | 0 | 10 |
| RideBound.Domain.Tests | 191 | 0 | 0 | 191 |
| RideBound.Contracts.Tests | 138 | 0 | 0 | 138 |
| RideBound.Application.Tests | 108 | 0 | 0 | 108 |
| RideBound.Benchmarking.Contracts.Tests | 82 | 0 | 0 | 82 |
| RideBound.Solvers.OrTools.Tests | 14 | 0 | 0 | 14 |
| RideBound.Algorithms.Tests | 201 | 0 | 0 | 201 |
| RideBound.Runner.Tests | 133 | 0 | 0 | 133 |
| RideBound.Benchmarking.Tests | 147 | **1** | 0 | 148 |
| **Total** | **1024** | **1** | **0** | **1025** |

The total of 1025 matches the last count recorded in ADR-077 (`docs/18`, "1025/1025"). The one failure is the known
`StrictBagItBundleTests.Source_inventory_binds_dirty_worktree_files_not_only_base_commit`, which fails on
`Assert.True` at `tests/RideBound.Benchmarking.Tests/StrictBagItBundleTests.cs:32`. That test expects
`GitDirty == true`, so it fails on a clean tree. It is recorded here, not "fixed". The drain test
(`PublicDerivativeMechanicalDrainConversationTests`) passed.

## 3. Design (file:line refer to the modified worktree unless marked `@761915c`)

### 3.1 What exists today
- `SolverBackedFleetSelection.cs@761915c:276-295` — the `forced-reference-count` level is added first only when a
  HardVector/SoftHardHybrid candidate `IsForcedReference`.
- `@761915c:297-303` — `accepted-request-count` (maximize).
- `@761915c:319-331` — `case HardVector when hardTreatmentActive:` adds `worst-hard-utilization-ppm`
  (min-max), then `AddRevisionObjectives` (10 `revision:*` levels, one for each dimension of
  `CommitmentDimensionVocabulary.Ordered`, `src/RideBound.Domain/Commitments/CommitmentDimension.cs:19-32`).
- `@761915c:365-385` — `operational-cost`, then one `candidate-id-rank:<vehicle>` level per vehicle.
- `SolverBackedRidePoolingPolicy.cs@761915c:322-353` — C1/C2 run the hard assessor
  (`AssessAndFilter(... requireSafetyNoOp: true, forcedReferenceRecovery, forcedNoWorse)`) and choose the `HardVector`
  profile. B1 `rolling-cost` skips this whole block, so moving to B1 would drop the hard assessment and the forced
  level. This is why the profile and the policy kind are not touched.
- The WP4 binding (`src/RideBound.Contracts/Protocol/Wp4PolicyConfigurationBinding.cs:31-45`) hashes the two
  canonical configuration hashes. The WP4 content hash is the SHA-256 of the canonical JSON
  (`Wp4RunnerConfiguration.cs:245-248`). A configuration without the new key therefore has the same bytes and the same
  binding by construction. A test pins this against archived values (§4, test 8).

### 3.2 Change (3 production files; 65 added code lines + 12 comment lines, by `git diff` excluding blank and `//` lines)
1. `src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs`
   - `:18-27` new `enum SolverBackedSelectionObjectiveOrder { StabilityFirst, CostFirst }`.
   - `:93-94` new optional parameter `objectiveOrder = StabilityFirst` on `SolverBackedFleetSelector.Select`.
   - `:106-117` guards: an undefined value throws `ArgumentOutOfRangeException`; `CostFirst` with any profile other
     than `HardVector` throws `ArgumentException`.
   - `:124` passes the order on; `:234` is the new `Create` parameter.
   - `:347-352` the only behavioural change: the HardVector case becomes
     `when hardTreatmentActive && objectiveOrder == StabilityFirst`. Under cost-first no case of the `switch` matches,
     so the utilization level and the 10 revision levels are skipped. The forced level (`:311`), the accepted level,
     `operational-cost` (`:397-400`) and the id ranks (`:402-417`) are built exactly as before.
   - `Map()` is unchanged, so a cost-first `FleetSelection` still reports `WorstHardUtilizationPartsPerMillion` and
     `DecisionInducedRevision` (descriptive only; nothing in the Runner reads them).
2. `src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs`
   - `:87-88` new constructor parameter `selectionObjectiveOrder = StabilityFirst` on
     `SolverBackedRidePoolingPolicyOptions`.
   - `:92-102` validation: undefined → `ArgumentOutOfRangeException`; `CostFirst` with any kind other than
     `RideBoundHardVector` → `ArgumentException` (C2 is excluded).
   - `:170` and `:200-205` the property `SelectionObjectiveOrder`.
   - `:408` `Decide` passes it to the selector.
   - Hard assessor, gates, `FullFleetValidator`, forced/no-worse recovery, generation and accounting are untouched.
3. `src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs`
   - `:46` `"selectionObjectiveOrder"` added to the allowed root fields.
   - `:69-74` constants `stability-first` / `cost-first`.
   - `:374-381` parsing: absent → `StabilityFirst`; `"stability-first"` → `StabilityFirst`; `"cost-first"` →
     `CostFirst`; anything else → `InvalidDataException("Unknown selectionObjectiveOrder.")`. A non-string or empty
     value is rejected by the existing `Text()` helper (`:746-758`).
   - `:383-388` `cost-first` without `solverExecution` or with a policy other than `ridebound-hard-vector` →
     `InvalidDataException`.
   - `:439` the order goes into the options; `:237` `CreateSolverPolicyOptionsForRun` (manifest-seed mode) preserves it.
- Domain, Application, Contracts, the solver adapter and the FleetPy adapter: unchanged. The adapter reads only
  `lateBoarding` from the WP4 file (`simulators/fleetpy-ridebound/ridebound_fleetpy/session.py:159-169`). It hashes the
  file canonically (`mapping.py:150-158`) and has no root-key allow-list, so it accepts the new key without a change.

### 3.3 Effective objective order in decision evidence
- No new field. When `emitSolverExecutionEvidence: true` (as in `wp4-tier3-v2.json`), every decision already records the
  level names in `solver.executionEvidence.selection.{primary,final}SolverDiagnostics.objectiveBounds[].objectiveName`
  (`src/RideBound.Runner/Protocol/SolverExecutionEvidenceMapper.cs:574-602`, the name at `:590`).
- Checked on the archived `C:/RideBoundData/research/tier3-t38-v1/C-30-d20181114-s10-r1-w07/transcript-00.ndjson`:
  - 425/455 decisions list 21 levels: accepted, utilization, 10 revision, cost, and 8 vehicle ranks.
  - 30/455 decisions list 10 levels: accepted, cost, and 8 ranks. These are the decisions without an applicable hard
    limit.
  - Under cost-first every decision will show the short list (plus `forced-reference-count` when that level is active).
- The run itself is identified by `policyConfigurationHash` in `initializeRun`, which binds the WP4 bytes that contain
  the key.
- Why no new field: the solver-evidence object has a fixed field set (`src/RideBound.Contracts/Protocol/DecisionMessages.cs:167-175`,
  enforced at `:844-851`). Adding a field means changing the decision codec and the evidence version, which is outside
  this narrow change.
- Limitation: within one decision, the cost-first level list looks the same as a stability-first decision that has no
  applicable hard limit. The run-level configuration hash resolves this. `objectiveBounds` can also be cut short when
  the solver budget runs out.

## 4. Tests added (9)

Algorithms, `tests/RideBound.Algorithms.Tests/Policies/SolverBackedFleetSelectionTests.cs` (5). The fixture
`ForcedAndTwoPricedInsertions` has vehicle 1 with only its forced no-op, and vehicle 2 with two insertions: 30 % at
cost 20, or 80 % at cost 10.
1. `Stability_first_keeps_the_exact_hard_vector_level_list_and_is_the_default` covers requirement (a). It pins the exact
   16-name list `forced-reference-count, accepted-request-count, worst-hard-utilization-ppm, revision:pickup_eta_total_ms
   … revision:pre_pickup_inserted_stop_count, operational-cost, candidate-id-rank:vehicle-1, candidate-id-rank:vehicle-2`.
   It also checks that the default call and the explicit `StabilityFirst` call give identical levels and contributions,
   and that the selection is `v2-low`.
2. `Cost_first_drops_only_the_utilization_and_revision_levels` covers requirement (b). The list is exactly
   `forced-reference-count, accepted-request-count, operational-cost, candidate-id-rank:vehicle-1,
   candidate-id-rank:vehicle-2`. Every kept level is equal (name, sense and aggregation) to the stability-first level,
   the options are the same, and each option contributes the same value on every kept level (added after the review).
   Cost-first picks `v2-high` (cost 10 versus 20) with the same accepted count, and still
   reports utilization 800000 and the revision.
3. `Cost_first_keeps_the_forced_level_condition_and_equals_stability_first_without_hard_limits`: without a forced
   option the first level is `accepted-request-count`. Without hard limits the two orders give the same levels and the
   same selection.
4. `Cost_first_is_rejected_outside_the_hard_vector_profile`: RollingCost, RevisionPenalty and SoftHardHybrid raise
   `ArgumentException`; an undefined enum value raises `ArgumentOutOfRangeException`.
5. `Cost_first_policy_options_are_valid_only_for_C1_and_default_to_stability_first`.

Algorithms, `tests/RideBound.Algorithms.Tests/Oracle/ExactSmallCommitmentDifferentialTests.cs` (2)
6. `Cost_first_C1_ranks_the_same_gated_candidates_by_cost_and_picks_a_cheaper_plan` covers requirement (e) end to end
   below the Runner (`SolverBackedRidePoolingPolicy.Decide` with the real generator, hard assessor, validator and an
   exact enumerating solver, forced-reference recovery on). Over 64 published exact-small seeds it checks that:
   - both orders see the same option ids and the same pruned `(candidateId, code)` witnesses, with the same forced
     vehicles (identical gates);
   - cost-first has no utilization or revision level;
   - the accepted counts are equal, cost-first cost ≤ stability-first cost, and stability-first stays C1-optimal;
   - the cost-first decision passes `CommitmentDecisionValidator` the way the Runner calls it.

   At least one seed must be strictly cheaper; 8/64 seeds were. In each of them, stability-first is strictly better on
   utilization or revision (`CompareC1(stable, cheap) < 0`). This replaced an always-true check after the review.
7. `Cost_first_under_no_worse_recovery_keeps_the_forced_treatment_and_the_no_worse_gate` was added after the review.
   It uses cost-first with recovery rule (b) (`no-worse-than-reference-v1`), as in the Tier-3 config. The state is the
   one from the existing zero-limit ranking test: every candidate breaks a deadline 1 ms before the kept drop, and a zero
   vehicle-switch limit keeps the hard treatment active. It checks that:
   - the same options reach the solver;
   - level 0 is `forced-reference-count`; stability-first has the utilization level and cost-first has no utilization
     or revision level;
   - vehicle 1 is still forced, the new rider is still served (not the no-op), and the accepted counts are equal;
   - the cost-first decision passes the validator with `ForcedNoWorse` the way the Runner calls it, and no breach
     delays the drop beyond the kept route.

   Honest limit: a temporary probe (reverted) showed that both orders pick the same plan in this state (cost 360, 3
   options). The test therefore checks invariants under cost-first + no-worse; it does not show a ranking difference
   there.

Runner, `tests/RideBound.Runner.Tests/Configuration/Wp4RunnerConfigurationTests.cs` (2)
8. `Selection_objective_order_is_optional_stability_first_and_cost_first_only_for_C1` covers requirement (c):
   - absent → StabilityFirst, in both `SolverPolicyOptions` and `CreateSolverPolicyOptionsForRun(19)`;
   - `"stability-first"` → StabilityFirst; `"cost-first"` → CostFirst, in both places;
   - policy, kind, budgets, recovery and generation are equal to the absent case;
   - declaring the key changes the content hash;
   - the invalid values `"cost-first-v2"`, `""`, `true` and `1` give `InvalidDataException` naming the key;
   - `cost-first` with B1 `rolling-cost`, and with C2 (`wp9-fleetpy-soft-hard-hybrid-audited-v1.json`), gives
     `InvalidDataException`.
9. `A_configuration_without_the_order_key_keeps_the_archived_tier3_bindings` covers requirement (d). The test embeds
   the text of `tang3/configs/wp4-tier3-v2.json` (file SHA-256 `66e9b592…4518`). It pins:
   - the canonical WP4 hash `fb2813c4…cd42`;
   - the commitment hash and binding for each case:

     | Case | Commitment config | Commitment hash | Binding | Source of the binding value |
     |---|---|---|---|---|
     | C-30 | repository file `benchmarks/configurations/wp14-c1-h6-reference-v1.json`, byte-identical to `tang3/configs/C-30.json` (both SHA-256 `d6124f3f…8beb`) | `f07395f5…9884` | `a2f11a3a…5f1c` | archived |
     | U | same file with the drop hard limit removed | `7fc79a43…370d` | `251b331e…c346` | archived |
     | C-120 | same file with the drop hard limit set to 120 s | `8dc9350b…a5a2` | `a9ac58b3…9010` | Codex R19 derivation only |

   - the same WP4 with `cost-first` has a different content hash.

   Where the archived values come from: I decoded `initializeRun` in every archived T3.8 transcript.
   `policyConfigurationHash` is `a2f11a3a…` in 51/51 `C-30-*` runs and `251b331e…` in 34/34 `U-*` runs. The adapter's
   own `wp4_policy_binding_hash` on the scratchpad files gives the same three bindings.

### Mutation check (`mutate_costfirst.py`)
Each mutant was applied alone, the targeted tests were run, and the exact bytes were restored and checked by SHA-256.
The check ran twice: before the review fixes (`mutate-costfirst.log`) and after them (`mutate-costfirst-2.log`).
All 7 mutants were killed both times. The killers in the final run:

| Mutant | Killed by |
|---|---|
| M1: cost-first ignored | tests 2, 6 and 7 |
| M2: cost-first also drops the forced level | tests 2 and 7 |
| M3: `Decide` does not pass the order | tests 6 and 7 |
| M4: `CreateSolverPolicyOptionsForRun` drops the order | test 8 |
| M5: the parser maps cost-first to stability-first | tests 8 and 9 |
| M6: the parser accepts cost-first for every solver policy | test 8 |
| M7: cost-first also drops `operational-cost` | tests 2 and 3 |

## 5. `git diff --stat` (uncommitted, `-c core.autocrlf=false`)

```
 docs/18-status-and-decision-log.md                 |  87 +++++++-
 docs/19-requirement-traceability.md                |  16 ++
 .../Policies/SolverBackedFleetSelection.cs         |  40 +++-
 .../Policies/SolverBackedRidePoolingPolicy.cs      |  27 ++-
 .../Configuration/Wp4RunnerConfiguration.cs        |  32 ++-
 .../ExactSmallCommitmentDifferentialTests.cs       | 145 +++++++++++-
 .../Policies/SolverBackedFleetSelectionTests.cs    | 242 ++++++++++++++++++++-
 .../Configuration/Wp4RunnerConfigurationTests.cs   | 221 +++++++++++++++++++
 8 files changed, 796 insertions(+), 14 deletions(-)
```

The full diff, docs included, is in `costfirst-diff-2026-10-11.patch` in this folder (1,035 lines, SHA-256
`c48042af4e7cee2db01bdee5efb804dac703d80c8c657276fc5718816e1ad690`). The production part is copied verbatim in
Appendix A; I checked that it is identical to the current `git diff -- src`.

Docs (in the worktree only):
- `docs/18`: one header line (new branch/date); a new section "ADR-078 — 2026-10-11 — Proposed (thăm dò …)" after
  ADR-077 (Context, Decision, Alternatives, Evidence, Consequences); a change-history entry at the top of §9. It makes no
  claim of benefit, and §1 and §5 of the main tree are unchanged.
- `docs/19`: new §33 "ADR-078 traceability", with 8 rows.

## 6. After the change

`dotnet test RideBound.slnx`, final run after the review fixes, full log `after-test-final.log`, on AC power:

| Test project | Passed | Failed | Skipped | Total | Δ vs baseline |
|---|---:|---:|---:|---:|---|
| RideBound.ArchitectureTests | 10 | 0 | 0 | 10 | — |
| RideBound.Domain.Tests | 191 | 0 | 0 | 191 | — |
| RideBound.Contracts.Tests | 138 | 0 | 0 | 138 | — |
| RideBound.Application.Tests | 108 | 0 | 0 | 108 | — |
| RideBound.Benchmarking.Contracts.Tests | 82 | 0 | 0 | 82 | — |
| RideBound.Solvers.OrTools.Tests | 14 | 0 | 0 | 14 | — |
| RideBound.Algorithms.Tests | 208 | 0 | 0 | 208 | +7 new |
| RideBound.Runner.Tests | 135 | 0 | 0 | 135 | +2 new |
| RideBound.Benchmarking.Tests | 148 | 0 | 0 | 148 | StrictBagIt now passes |
| **Total** | **1034** | **0** | **0** | **1034** | 1025 old + 9 new |

An earlier full run, before the review fixes (log `after-test.log`), gave 1033/1033 with 8 new tests. The final run
above came after the extra test and the two strengthened assertions; the only later edits were to docs.

`StrictBagItBundleTests` passes now only because the worktree is dirty (uncommitted edits), which is its documented
precondition. This is not a fix, and the test will fail again on a clean checkout of the branch.

## 7. Failures during the work and their causes
- In the first run of the new end-to-end test, a comparison of `PrunedCandidates` failed. Those records hold
  collection members that compare by reference, so the records were unequal even with equal content. The test now
  compares `(CandidateId, Code)` tuples. This was a test bug; production was not affected.
- `DeterministicCandidateSelectionExecutionBudget` is a class, not a record, so I compare its fields instead of the
  object. I found this before running.
- The first independent review sub-agent stopped on an API session limit and never reported; it was restarted. See §9.
  My own session was also interrupted once by the same limit and resumed. No work was lost: the worktree state was
  checked before continuing.
- Two temporary probes were made in the test file to read values (the 8/64 count, and the no-worse costs). Each was
  reverted, and the file was byte-compared with its backup (`cmp`).
- No production test failed at any point.

## 8. Gate-0 equivalence runs — blockers and open questions
Blockers (owner decisions):
1. **No Runner contains this change.** No publish was allowed. The archived runs used
   `C:/RideBoundData/research/runner-tier3-v2`, which was published from `45f8026` with a clean tree. Gate-0 needs a new
   Runner published from this branch, and per the earlier practice that means a commit first. Both need owner approval.
2. **A new Runner changes `binarySha256`.** The adapter writes `binarySha256` (the SHA-256 of the Runner DLL,
   `session.py:483`) into `initializeRun`. The transcripts therefore cannot be byte-identical to the archived ones even
   with the option off. The gate has to compare decisions with identity/hash fields ignored, as
   `optimize/compare_equivalence.py` does. `policyConfigurationHash` itself stays identical when the key is absent
   (test 9).
3. **`coreCommitSha` follows the repository root, not the Runner.** It is `git rev-parse HEAD` of
   `ridebound_repository_root` (`session.py:140-156`, `:340`). The T3.8 driver passes `E:/Code/RideBound-deadline` (HEAD
   `1ce15e9`, as the archived manifests show), with an expected inventory hash. If Gate-0 reuses that driver unchanged,
   the manifest will name `1ce15e9` while the Runner comes from `research/tier3-cost-first`. The owner should decide how
   the Runner provenance is recorded: which repository root, and which runner manifest (TSV) to keep.

Things the Gate-0 configs must respect:
4. Use `wp4-tier3-v2.json` unchanged, **without** the key. Writing `"selectionObjectiveOrder": "stability-first"`
   changes the content hash and therefore `policyConfigurationHash`.
5. Only C-30 and U have archived bindings (T3.8). C-120 `a9ac58b3…` is a Codex derivation that this test reproduces, but
   it has no archived run to compare against.
6. The cost-first arm needs a new WP4 file outside the repository: `wp4-tier3-v2.json` plus one key, made the same way
   as `make_wp4_v2.py`. It does not exist yet.

Open questions (not blockers):
7. Under cost-first, the ADR-077 rule that skips exempted over-cap dimensions in the utilization ranking has no effect,
   because there is no utilization level (`HardVectorCandidateAssessor` still computes it; nothing ranks it).
   - Effect, as the reviewer put it: a forced vehicle may pick the cheapest no-worse changed route, even one that moves
     riders who were not exempted closer to their caps.
   - The no-worse gate and every cap are still enforced by the validator.
   - This follows from requirement 2 and is written into ADR-078 Consequences. The owner should confirm it is intended
     for the Tier-3 arm, which uses rule (b).
   - Related: ranking happens only over the candidates that retention kept. With `service-set-stability-portfolio-v1`,
     the result reads as "cost-first ranking over the same retained portfolio".
8. ADR-077's note that `forced-reference-count` ranks before the accepted count still holds under cost-first. That
   level is kept on purpose.
9. The production change is 65 added code lines, a little above the ~40–60 estimate. The extra lines are the
   defensive guards at both the options and the selector level, and I kept them because `Select` is public.
10. The Python adapter suite was not run, because the adapter is unchanged. No FleetPy simulation was run.

## 9. Independent review

A fresh-context general-purpose sub-agent did a read-only review. It edited nothing; it built the project and ran the
three affected test classes (17/17 and 54/54 at that time). An earlier reviewer sub-agent had died on an API limit
before reporting.

**Verdict: Approve. No BLOCKER.**

What it confirmed:
- (a) Default behaviour is unchanged on every path. This includes the fallback paths in `CandidateSelectionExecution.cs`,
  which read `problem.ObjectiveLevels`, and both RunnerSession option paths. No existing config can hash differently:
  the hash is taken over the canonical input before parsing, and the new key was rejected before this change.
- (b) Cost-first removes exactly the utilization level and the 10 revision levels. The policy kind and the profile stay
  HardVector. The only constructions of the options in `src/` and `tools/` are the two in `Wp4RunnerConfiguration`.
- (d) None of the new tests is vacuous; every `Replace` anchor occurs exactly once.
- The embedded WP4 text matches `wp4-tier3-v2.json` key for key.
- It decoded the archived bindings independently: C-30 is `a2f11a3a…` in 51/51 runs and U is `251b331e…` in 34/34.
- C-30 is byte-identical to `wp14-c1-h6-reference-v1.json`. U and C-120 differ only in the drop hard limit.

Findings and what I did:

| Finding | Kind | Action |
|---|---|---|
| No test for cost-first + no-worse recovery (the Tier-3 combination). The no-worse utilization ranking (`HardVectorCandidateAssessor.cs` `rankNonExempt`) no longer has an effect. Safety is unaffected, since the gate is enforced in `CommitmentDecisionValidator`. | SHOULD-FIX | **Done.** Added test 7 and wrote the effect into ADR-078 Consequences and §8 item 7. |
| The cost-first check in the options constructor runs before the policy-kind check, so an undefined kind together with cost-first throws `ArgumentException`. This matches the neighbouring no-worse check. | NIT | Kept as is, for consistency. |
| Portfolio evidence writes `objectiveProfile: "hardVector"` for both orders. | NIT | Documented in ADR-078 Consequences. No code change: a new profile value would change the evidence contract. |
| Test 2 did not compare the per-option contributions on the kept levels. | NIT | **Done.** |
| The `NotEqual(candidateId)` check in test 6 was always true. | NIT | **Done.** Replaced by `CompareC1(stable, cheap) < 0`. |
| No RunnerSession + OR-Tools test runs cost-first. The chain is covered piece by piece. | NIT | Not added. Open: the end-to-end FleetPy run will be the first real exercise. |
| Results should read as "ranking over the same retained portfolio". | NIT | Documented in ADR-078 and §8 item 7. |
| A static field sits mid-class. | NIT | Left as is (style only). |

## Appendix A — production diff (verbatim `git -c core.autocrlf=false diff -- src`)

```diff
diff --git a/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs b/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs
index dfc062e..ab8096c 100644
--- a/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs
+++ b/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs
@@ -15,6 +15,17 @@ public enum SolverBackedObjectiveProfile
     SoftHardHybrid,
 }
 
+/// <summary>
+/// ADR-078 (exploratory, off by default). Order of the C1 ranking levels after the
+/// accepted-request count. Cost-first skips the worst-hard-utilization and revision levels;
+/// gates, locks and recovery act before ranking and are unchanged.
+/// </summary>
+public enum SolverBackedSelectionObjectiveOrder
+{
+    StabilityFirst,
+    CostFirst,
+}
+
 public interface IFleetSelectionValidator
 {
     CandidateSelectionValidationResult Validate(FleetSelection selection);
@@ -78,7 +89,9 @@ public sealed class SolverBackedFleetSelector
         IReadOnlyDictionary<string, CandidateCommitmentAssessment>?
             revisionAssessments = null,
         IReadOnlyDictionary<string, HardVectorCandidateAssessment>?
-            hardAssessments = null)
+            hardAssessments = null,
+        SolverBackedSelectionObjectiveOrder objectiveOrder =
+            SolverBackedSelectionObjectiveOrder.StabilityFirst)
     {
         ArgumentNullException.ThrowIfNull(candidateSets);
         ArgumentNullException.ThrowIfNull(executionBudget);
@@ -90,11 +103,25 @@ public sealed class SolverBackedFleetSelector
             throw new ArgumentOutOfRangeException(nameof(objectiveProfile));
         }
 
+        if (!Enum.IsDefined(objectiveOrder))
+        {
+            throw new ArgumentOutOfRangeException(nameof(objectiveOrder));
+        }
+
+        if (objectiveOrder == SolverBackedSelectionObjectiveOrder.CostFirst
+            && objectiveProfile != SolverBackedObjectiveProfile.HardVector)
+        {
+            throw new ArgumentException(
+                "The cost-first objective order is only defined for the C1 hard-vector profile.",
+                nameof(objectiveOrder));
+        }
+
         var mapping = SelectionModelMapping.Create(
             candidateSets,
             objectiveProfile,
             revisionAssessments,
-            hardAssessments);
+            hardAssessments,
+            objectiveOrder);
 
         if (mapping.Witness is not null)
         {
@@ -203,7 +230,8 @@ public sealed class SolverBackedFleetSelector
             IReadOnlyDictionary<string, CandidateCommitmentAssessment>?
                 revisionAssessments,
             IReadOnlyDictionary<string, HardVectorCandidateAssessment>?
-                hardAssessments)
+                hardAssessments,
+            SolverBackedSelectionObjectiveOrder objectiveOrder)
         {
             var orderedSets = candidateSets
                 .OrderBy(value => value.VehicleId.Value, StringComparer.Ordinal)
@@ -316,8 +344,12 @@ public sealed class SolverBackedFleetSelector
                             .DecisionInducedRevision,
                         "revision");
                     break;
+                // Cost-first (ADR-078) matches no case here, so operational cost follows the
+                // accepted-request count directly; the forced level above is unchanged.
                 case SolverBackedObjectiveProfile.HardVector
-                    when hardTreatmentActive:
+                    when hardTreatmentActive
+                        && objectiveOrder
+                            == SolverBackedSelectionObjectiveOrder.StabilityFirst:
                     objectives.Add(
                         MinMaximum(
                             "worst-hard-utilization-ppm",
diff --git a/src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs b/src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs
index 4c10a27..ef819ff 100644
--- a/src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs
+++ b/src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs
@@ -83,10 +83,24 @@ public sealed record SolverBackedRidePoolingPolicyOptions
         int maximumRepairRequestsConsideredPerVehicle = 0,
         bool captureCandidatePortfolioEvidence = false,
         bool forcedReferenceRecovery = false,
-        bool forcedNoWorseRecovery = false)
+        bool forcedNoWorseRecovery = false,
+        SolverBackedSelectionObjectiveOrder selectionObjectiveOrder =
+            SolverBackedSelectionObjectiveOrder.StabilityFirst)
     {
         ArgumentNullException.ThrowIfNull(executionBudget);
 
+        if (!Enum.IsDefined(selectionObjectiveOrder))
+        {
+            throw new ArgumentOutOfRangeException(nameof(selectionObjectiveOrder));
+        }
+
+        if (selectionObjectiveOrder == SolverBackedSelectionObjectiveOrder.CostFirst
+            && policyKind != RidePoolingPolicyKind.RideBoundHardVector)
+        {
+            throw new ArgumentException(
+                "The cost-first selection order is only valid for the C1 policy.");
+        }
+
         if (forcedNoWorseRecovery && !forcedReferenceRecovery)
         {
             throw new ArgumentException(
@@ -153,6 +167,7 @@ public sealed record SolverBackedRidePoolingPolicyOptions
         CaptureCandidatePortfolioEvidence = captureCandidatePortfolioEvidence;
         ForcedReferenceRecovery = forcedReferenceRecovery;
         ForcedNoWorseRecovery = forcedNoWorseRecovery;
+        SelectionObjectiveOrder = selectionObjectiveOrder;
     }
 
     public RidePoolingPolicyKind PolicyKind { get; }
@@ -181,6 +196,13 @@ public sealed record SolverBackedRidePoolingPolicyOptions
     /// kept route's gate overruns worse, so it can still serve a new rider.
     /// </summary>
     public bool ForcedNoWorseRecovery { get; }
+
+    /// <summary>
+    /// Exploratory (ADR-078, stability-first by default). Cost-first ranks a C1 selection by
+    /// operational cost right after the accepted-request count; the hard assessment, gates,
+    /// locks and recovery are unchanged.
+    /// </summary>
+    public SolverBackedSelectionObjectiveOrder SelectionObjectiveOrder { get; }
 }
 
 public sealed record SolverBackedPolicyDecision(
@@ -382,7 +404,8 @@ public sealed class SolverBackedRidePoolingPolicy
             accounting.Value!,
             validator,
             revisionAssessments,
-            hardAssessments);
+            hardAssessments,
+            policyOptions.SelectionObjectiveOrder);
 
         if (!selected.IsSuccess)
         {
diff --git a/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs b/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs
index 1cf9820..46cea74 100644
--- a/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs
+++ b/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs
@@ -42,7 +42,8 @@ public sealed class Wp4RunnerConfiguration : ICommitmentWarningProfileProvider
         "emitSolverExecutionEvidence",
         "solverExecutionEvidenceProfile",
         "commitmentRecovery",
-        "lateBoarding");
+        "lateBoarding",
+        "selectionObjectiveOrder");
 
     /// <summary>
     /// ADR-075 (exploratory). Optional; omitted means fail-closed, so every
@@ -64,6 +65,13 @@ public sealed class Wp4RunnerConfiguration : ICommitmentWarningProfileProvider
     /// </summary>
     public const string RecordLateBoarding = "record-v1";
     public const string RejectLateBoarding = "reject";
+
+    /// <summary>
+    /// ADR-078 (exploratory). Optional; omitted means stability-first, so every configuration
+    /// written before it keeps its content hash and its behaviour. `cost-first` is C1 only.
+    /// </summary>
+    public const string StabilityFirstSelectionOrder = "stability-first";
+    public const string CostFirstSelectionOrder = "cost-first";
     private static readonly IReadOnlySet<string> GenerationRequiredFields = Fields(
         "maximumCandidatesPerVehicle",
         "maximumNewRequestsPerVehicle",
@@ -225,7 +233,8 @@ public sealed class Wp4RunnerConfiguration : ICommitmentWarningProfileProvider
             source.MaximumRepairRequestsConsideredPerVehicle,
             source.CaptureCandidatePortfolioEvidence,
             source.ForcedReferenceRecovery,
-            source.ForcedNoWorseRecovery);
+            source.ForcedNoWorseRecovery,
+            source.SelectionObjectiveOrder);
     }
 
     public static Wp4RunnerConfiguration Decode(
@@ -362,6 +371,22 @@ public sealed class Wp4RunnerConfiguration : ICommitmentWarningProfileProvider
             }
             : false;
 
+        var selectionObjectiveOrder = root.TryGetProperty("selectionObjectiveOrder", out _)
+            ? Text(root, "selectionObjectiveOrder") switch
+            {
+                StabilityFirstSelectionOrder => SolverBackedSelectionObjectiveOrder.StabilityFirst,
+                CostFirstSelectionOrder => SolverBackedSelectionObjectiveOrder.CostFirst,
+                _ => throw new InvalidDataException("Unknown selectionObjectiveOrder."),
+            }
+            : SolverBackedSelectionObjectiveOrder.StabilityFirst;
+
+        if (selectionObjectiveOrder == SolverBackedSelectionObjectiveOrder.CostFirst
+            && (!hasSolver || policyKind != RidePoolingPolicyKind.RideBoundHardVector))
+        {
+            throw new InvalidDataException(
+                "selectionObjectiveOrder 'cost-first' requires the solver-backed C1 policy.");
+        }
+
         SolverBackedRidePoolingPolicyOptions? solverOptions = null;
         MultiplePlanPoolOptions? multipleOptions = null;
         var warningProfiles = Array.Empty<CommitmentWarningProfile>();
@@ -410,7 +435,8 @@ public sealed class Wp4RunnerConfiguration : ICommitmentWarningProfileProvider
                 repairCap,
                 solverExecutionEvidenceProfile is not null,
                 forcedReferenceRecovery,
-                forcedNoWorseRecovery);
+                forcedNoWorseRecovery,
+                selectionObjectiveOrder);
         }
 
         if (hasMultiple)
```
