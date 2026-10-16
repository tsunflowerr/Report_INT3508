# docs18

## 1. [git/worktrees]
Worktrees: E:/Code/RideBound at 41a4e11 [main]; C:/Code/RideBound-noworse at a90b4b7 [research/tier3-no-worse]; E:/Code/RideBound-deadline at 1ce15e9 [research/tier3-failure-aware]; E:/Code/RideBound-py-baseline at 8d1ea4d (detached HEAD).
SOURCE: git -C E:/Code/RideBound worktree list

## 2. [git/branches]
Every research branch is committed and pushed. Local and origin match: research/deadline-gate=65d867c (ADR-074), research/tier3-failure-aware=1ce15e9, research/tier3-no-worse=a90b4b7, main=41a4e11.
SOURCE: git -C C:/Code/RideBound-noworse branch -a -v --no-abbrev

## 3. [git/commits]
Research commit chain on tier3-no-worse since main: 65d867c (2026-09-24 22:14 ADR-074 deadline rule + typed no-op diagnostic), 8d1ea4d (2026-09-25 00:01 ADR-075 forced-reference recovery), 69512d3 (2026-09-25 00:59 ADR-076 late boardings), 1ce15e9 (2026-09-25 11:47 Tier 3 pilot T3.5-T3.7 status), 45f8026 (2026-09-26 02:55 ADR-077 no-worse recovery code), a90b4b7 (2026-09-26 04:41 ADR-077 end-to-end A1 evidence).
SOURCE: git -C C:/Code/RideBound-noworse log --oneline 41a4e11..research/tier3-no-worse; git show -s --format='%H %ad %s'

## 4. [git/status noworse]
C:/Code/RideBound-noworse working tree is clean: git status --short prints 0 lines.
SOURCE: git -C C:/Code/RideBound-noworse status --short | wc -l -> 0

## 5. [git/status deadline worktree]
E:/Code/RideBound-deadline shows 144 files as ' M'. git diff --shortstat and git diff --ignore-cr-at-eol --shortstat both print nothing apart from 'LF will be replaced by CRLF' warnings, so the changes are line-ending/stat-only with no content diff.
SOURCE: git -C E:/Code/RideBound-deadline status --short | wc -l -> 144; git diff --shortstat (empty)

## 6. [docs/18 header (noworse)]
Header line: 'Cập nhật gần nhất: 2026-08-28 (cây chính); nhánh thăm dò research/deadline-gate: 2026-09-24 (ADR-074 Proposed); nhánh thăm dò research/tier3-failure-aware: 2026-09-25 (ADR-075, ADR-076 Proposed; thí điểm T3.7 xong, cổng dừng phục hồi bị kích hoạt); nhánh thăm dò research/tier3-no-worse: 2026-09-26 (ADR-077 Proposed; 28 job đầu-cuối A1 pass)'.
SOURCE: C:\Code\RideBound-noworse\docs\18-status-and-decision-log.md:4

## 7. [docs/18 header (deadline worktree)]
The header in E:/Code/RideBound-deadline stops at research/tier3-failure-aware 2026-09-25 (ADR-075, ADR-076 Proposed; T3.7 pilot done, recovery stop gate triggered) and has no tier3-no-worse/ADR-077 part. That worktree's branch is research/tier3-failure-aware at 1ce15e9, not research/deadline-gate.
SOURCE: E:\Code\RideBound-deadline\docs\18-status-and-decision-log.md:4; git worktree list

## 8. [docs/18 §1/§5]
§1 table still shows the main-tree state: Current work package 'ADR-073 freeze v3 AUTHORIZED ... 009..012/WP15/H7 UNAUTHORIZED'. The change history says §1 and §5 of the main tree are unchanged by the research branches.
SOURCE: C:\Code\RideBound-noworse\docs\18-status-and-decision-log.md:12-13, :5218

## 9. [ADR-074 status]
Header: 'ADR-074 — 2026-09-24 — Proposed (thăm dò; nhánh research/deadline-gate; chưa commit)'. The 'chưa commit' label is stale: the change is committed as 65d867c.
SOURCE: docs/18-status-and-decision-log.md:4726; git log 65d867c

## 10. [ADR-074 option keys/defaults]
CommitmentPolicy adds DropEtaDeadlineSlack (Duration?, default null) and DropEtaDeadlineTwoSided (default false; true without slack is rejected). Config keys: dropEtaDeadlineSlackMs (positive integer) and dropEtaDeadlineTwoSided (boolean). When both keys are absent the rule is off and config bytes/hash are unchanged.
SOURCE: docs/18-status-and-decision-log.md:4738-4741; src/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs:29-30,170-185; src/RideBound.Domain/Commitments/CommitmentPolicy.cs:139,198-213

## 11. [ADR-074 semantics]
The lock evaluator emits witness deadline_cap when p − p0 > ℓ and, when two-sided, deadline_floor when p0 − p > ℓ. p0 is the FIRST promise (Entries[0]), so drift alone can trip the rule, even on the no-op. Deadline witnesses are appended after lock witnesses. The code is COMMITMENT_DEADLINE_EXCEEDED at stage Lock. Only SolverBackedRidePoolingPolicy sets requireSafetyNoOp, which gives COMMITMENT_SAFETY_NOOP_REJECTED plus 'No-op rejection:'. B1–B4 never receive a deadline (MechanismCommitmentPolicyProvider).
SOURCE: docs/18-status-and-decision-log.md:4742-4758

## 12. [ADR-074 tests]
Debug 963/963 (log after-review-fix-2.log). A later run gave 962/963, with only drain medium failing on resource.cpu-time-exceeded as in the baseline. +12 tests (Domain 3, Application 2, Algorithms 4, Runner 3). Two mutations were caught. Two independent review rounds; round 2 found no P0/P1.
SOURCE: docs/18-status-and-decision-log.md:4760-4769; docs/19-requirement-traceability.md:701

## 13. [ADR-074 limitations]
Known limits: (1) on the solver-backed path only already-broken runs change their message; labels can flip between commitment-all-rejected/* and all-rejected/non-commitment. (2) The typed code does not reach artifacts (INTERNAL_ERROR + message), so classification is text-based. (3) Deadline prunes must be counted by scanning commitmentWitnesses, not code. wp14_frontier_analyze.py and wp14_mechanism_probe.py silently ignore the new code, and wp13_recorded_witness_relaxation.py rejects it: do not use these tools on deadline output. (4) The deadline also applies on the OnlineCommitment path without WP4 (untested); every Tier-2 run passes --wp4-config. (5) The deadline witness carries no magnitude (ℓ, p0, p). (6) Drift runs fail the project verifier (it needs exactly one snapshot), so all Tier-2 results are labelled exploratory.
SOURCE: docs/18-status-and-decision-log.md:4771-4786

## 14. [ADR-074 Tier-2 results]
Runner E:\RideBoundData\research\runner-deadline-v1 (tree SHA-256 8fa5dd28…61cda8); output E:\RideBoundData\research\deadline-v1 (301 dirs). Controls 40/40 (36 completed cells identical per decision to wp14/drift-v1; 4 known outcome-gate infeasible cells). 0/56 behaviour-gate runs infeasible due to commitment. Sealed predictions correct: 98/102 main panel, 31/32 held-out light, 40/40 dark. Light k=1: one-sided deadline 30/60/120 s infeasible 19/13/3 of 20 cells; k=0: 0/60. Dark held-out: one-sided 0/8, two-sided 7/8, outcome gate 8/8. All 90 commitment-infeasible runs quote the no-op's own reason. The secondary prediction ('one-sided deadline serves more riders as congestion falls') was NOT observed (1/8 cells, +1 rider). predictions.csv SHA 6c5451a0…, sealed 06:03:52Z.
SOURCE: docs/18-status-and-decision-log.md:4788-4801; docs/19-requirement-traceability.md:703-705

## 15. [ADR-074 claim boundary]
No novelty is claimed for the deadline: Schulz and Pfeiffer (2026) already have an enforceable deadline measured from the first promise. The ADR also does not claim the mechanism beats Schulz & Pfeiffer.
SOURCE: docs/18-status-and-decision-log.md:4734-4735, :4801

## 16. [ADR-075 status]
Header: 'ADR-075 — 2026-09-24 — Proposed (thăm dò; nhánh research/tier3-failure-aware; chưa commit)'. The 'chưa commit' label is stale: the change is committed as 8d1ea4d.
SOURCE: docs/18-status-and-decision-log.md:4803; git log 8d1ea4d

## 17. [ADR-075 option key/default]
New optional WP4 key commitmentRecovery ∈ {fail-closed, forced-reference-v1}. When absent it is fail-closed and bytes/hash of old configs are unchanged. The key is valid only for solver-backed C1/C2. The owner chose 'Giữ tuyến + ghi vi phạm' on 2026-09-24.
SOURCE: docs/18-status-and-decision-log.md:4808-4812, :4848-4850; src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:48-52,331-352

## 18. [ADR-075 semantics]
Adds Domain breach kind CommitmentBreachKind.ForcedReference; its codes are a subset of {COMMITMENT_BUDGET_EXCEEDED, COMMITMENT_DEADLINE_EXCEEDED}, and a phase lock is deliberately excluded. Application adds CommitmentValidationContext.ForcedReferenceVehicles (default null): exemptions apply only when the candidate route is semantically equal to the reduced route. The ledger still charges and is never reset. A breach is recorded as an event: on a promise revision, a phase change, the first forced breach, or a code-set change. Algorithms adds a first solver level 'forced-reference-count' (MinSum) and gives the forced no-op utilization 0. The certificate has normalOperation=false with a witness stage=forcedReference. It also fixes two places that passed non-taxonomy codes to ErrorPayloadCodec.Encode (now INTERNAL_ERROR/failSession).
SOURCE: docs/18-status-and-decision-log.md:4814-4859

## 19. [ADR-075 tests]
Debug 993/993 = 963 + 30 tests (Domain 5, Application 8, Algorithms 11, Runner 6). Six mutations, all caught. Two independent review rounds, no blocker; should-fix items fixed.
SOURCE: docs/18-status-and-decision-log.md:4861-4898; docs/19-requirement-traceability.md:726

## 20. [ADR-075 limitations]
Known limits: recovery exists only on solver-backed C1/C2 (not RideBoundHardVectorPolicy, CommitSoftHardHybridPolicy or B1–B4). It applies only to the deadline and budget gates; physical errors, config errors and phase locks stay fail-closed. The vehicle is 'frozen' once a rider exceeds a cap or is late: every insertion is rejected until the rider leaves the phase, is dropped, or favourable drift brings the drop back in time. The two-sided floor is the exception. BreachCount (MechanicalMetricCalculator.cs:268-271) is always 0 under recovery, so use NonNormalCertificateCount, certificate witnesses or the incident ledger; T3.6 must add a separate column. The evidence portfolio does not mark forced options, so WP13/WP14 tools must not be used on recovery output. Reported utilization is 0 for a forced vehicle. The record does not store the basis. No OR-Tools real-solver test, no skipConstantObjectiveLevels test, and no golden hash for C1 with recovery off. Fix 6 changes behaviour even with recovery off (host no longer exits with code 3).
SOURCE: docs/18-status-and-decision-log.md:4900-4943

## 21. [ADR-076 status]
Header: 'ADR-076 — 2026-09-25 — Proposed (thăm dò; nhánh research/tier3-failure-aware; chưa commit)'. The 'chưa commit' label is stale: the change is committed as 69512d3.
SOURCE: docs/18-status-and-decision-log.md:4945; git log 69512d3

## 22. [ADR-076 option key/default]
Optional WP4 key lateBoarding ∈ {reject, record-v1}. When absent it is reject and bytes/hash are unchanged. The key applies to ALL policies, and arms of a comparison must share the same value AND the same config bytes: an explicit 'reject' behaves the same but hashes differently. The FleetPy adapter reads the same key. Under record-v1, _fleetpy_stop drops only the drop point's latest-arrival bound.
SOURCE: docs/18-status-and-decision-log.md:4967-4978, :5049-5051; src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:60-64,354-363

## 23. [ADR-076 semantics]
RideRequest.Board/Rehydrate take allowLatePickup (default false). A late boarding records ObservedLatePickup in a separate LatePickups list of the incident ledger, at most one per rider. The original window is kept. Early boarding is still rejected.
SOURCE: docs/18-status-and-decision-log.md:4958-4966

## 24. [ADR-076 tests]
.NET 1005/1005 = 993 + 12 tests (Domain 5, Application 3, Runner 4). Python 443 tests: 437 pass and 6 freeze tests fail, with identical messages on the clean pre-T3.4 checkout 8d1ea4d (E:\Code\RideBound-py-baseline). Six new Python tests pass. Two mutations caught. Two review rounds, no blocker.
SOURCE: docs/18-status-and-decision-log.md:4997-5031; docs/19-requirement-traceability.md:743

## 25. [ADR-076 limitations]
Known limits: do not mix results of the two lateBoarding values, and do not compare directly with Tier-2 cells that died on window-wall. FleetPy still checks latest pickup and max trip for plans sent to it. Remaining death path after an in-batch cancellation, the resent no-op: RBWP7_FLEETPY_PLAN_INFEASIBLE, untested. Do not add the predicted pickup-window exogenous breach and the actual LatePickups together; T3.6 must count them separately. The adapter shifts the WP9 v6 adapterPackageTreeSealSha256, so WP9/H6 reproduction must use the main-tree adapter. No metric reads LatePickups yet (T3.6 must add a column). A max-ride-time overrun at drop is not recorded anywhere.
SOURCE: docs/18-status-and-decision-log.md:5033-5058

## 26. [ADR-077 status]
Header: 'ADR-077 — 2026-09-26 — Proposed (thăm dò; nhánh research/tier3-no-worse)'. It is committed: code in 45f8026, A1 evidence in a90b4b7.
SOURCE: docs/18-status-and-decision-log.md:5060; git log

## 27. [ADR-077 context]
In the C vs M⁺ sweep (tang3/sweep, 156 jobs, exploratory), M⁺ was forced in 28% of decisions at x = 30 s. On average 9.4% of the fleet was frozen (14–18.5% at W2), and at W2 M⁺ served 2 fewer riders than C. Sources: tang3/sweep/logs/sweep-aggregate-2026-09-26.txt and sweep-jobs-2026-09-26.tsv (columns M5_nonNormalShare, M5_meanForcedFleetShare). The activation criterion is in tang3/sweep/SWEEP-AMENDMENTS.md A1.
SOURCE: docs/18-status-and-decision-log.md:5062-5070

## 28. [ADR-077 option key/default]
Adds WP4 key value commitmentRecovery: "no-worse-than-reference-v1", default off, extending forced-reference-v1. The config decode maps fail-closed→(false,false), forced-reference-v1→(true,false), no-worse-than-reference-v1→(true,true); absent→(false,false). Anything other than solver-backed C1/C2 throws InvalidDataException.
SOURCE: docs/18-status-and-decision-log.md:5072-5073; src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:54-58,331-352

## 29. [ADR-077 rule]
On a forced vehicle, every option the validator rejected is re-checked. A rider's gate failure is exempted only if the kept route (the exogenous forecast) has the SAME failure and the option is no worse on it: upper deadline, drop ≤ the kept drop; lower deadline, drop ≥ the kept drop; budget dimension, total-after ≤ the kept total-after. Phase locks and vehicle locks are never exempted. Riders the kept route does not violate must pass normally. A changed-route exemption is recorded as the new breach kind ForcedNoWorse (checkpoint "forcedNoWorse", certificate stage forcedNoWorse). In this mode utilization ranking skips only (rider, dimension) pairs where an exempted rider is over the cap. forced-reference-v1 is byte-identical in behaviour and messages.
SOURCE: docs/18-status-and-decision-log.md:5074-5086; src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:797-818

## 30. [ADR-077 alternatives rejected]
Rejected: (a) accept only changed routes that keep the forced rider's forecast unchanged. This is void because ServiceOrder contains all remaining stops (PromiseProjector.cs:36), so every insertion changes the forecast. (b) Re-anchor the late rider's deadline to the kept-route time. This breaks the promise without a record.
SOURCE: docs/18-status-and-decision-log.md:5088-5091

## 31. [ADR-077 tests]
dotnet test RideBound.slnx: 1025/1025 = 1005 + 20 new tests (Domain 4, Application 8, Algorithms 5, Runner 3). The test names were found: Domain OperationalIncidentLedgerTests.cs:349,374,390,403. Application CommitmentDeadlineValidatorTests.cs:351,379,400,421,455,472,507,537. Algorithms ExactSmallCommitmentDifferentialTests.cs:1166,1205,1247,1303,1341. Runner OnlineStateCheckpointCodecTests.cs:279 and Wp4RunnerIntegrationTests.cs:723,760. Two independent review rounds, no blocker. Three mutations were caught: rank like the kept route, rank the over-cap dimension, invert the floor side.
SOURCE: docs/18-status-and-decision-log.md:5094-5109, :5169; docs/19-requirement-traceability.md:774; grep of tests

## 32. [ADR-077 A1 end-to-end]
Runner C:\RideBoundData\research\runner-tier3-v2 was published from 45f8026 with a clean tree (tree ac251ef3…cff3f, 429 files). WP4 v2 differs from v1 only in commitmentRecovery. 28 FleetPy medium jobs: 22 M⁺-x arms that had forced decisions in the sweep, plus 6 controls (4 C-30, 2 M⁺-900). Results: 28/28 status pass, v/e/p audit correct. 49 decisions carry a forcedNoWorse witness. The final checkpoint has 50 ForcedNoWorse and 5155 ForcedReference breaches. 6/6 controls have fleet action sequences identical to Runner v1. Riders served on the 22 treatment jobs: no-worse 1874, forced-reference-v1 1864, C 1873. No-worse equals C on 21/22 jobs and has the same action sequence as C on 19/22. Sources: tang3/sweep/SWEEP-REPORT.md §7, logs/noworse-analyze-2026-09-26.txt, logs/noworse-aggregate-2026-09-26.txt. The change history reads this as: the sweep's rider-count gap came from the recovery rule, while the promise-keeping difference remains.
SOURCE: docs/18-status-and-decision-log.md:5110-5121, :5171-5173; docs/19-requirement-traceability.md:775; ls confirmed the listed files and the runner dir exist

## 33. [ADR-077 limitations / not yet tested ('chưa kiểm')]
Exploratory; the default and forced-reference-v1 are unchanged. The Runner path where a changed route is selected has NO fixed in-repo integration test: the two-vehicle fixture always has an empty vehicle. It was exercised only by the 22 A1 FleetPy jobs, which are outside dotnet test. Restoring a checkpoint with ForcedNoWorse in the Runner is checked only at codec level. ForcedNoWorse records are not one per no-worse decision: all-zero deltas record nothing new, and an unchanged forecast records ForcedReference. To count 'forced vehicle still serves', count the forcedNoWorse certificate stage, not the record kind. Not yet tested: two late riders on one vehicle; phase lock + deadline; multi-dimension budget; C2 under no-worse; the 'reference is null' branch. 'Worse' can still happen on dimensions the gate does not measure (e.g. an unconstrained rider's pickup time). The forced-reference-count level still ranks before riders accepted, and a no-worse option counts 1 like a forced no-op. Extra validation work is not added to validationWorkUnits. Phase-lock/vehicle-lock non-exemption (the `_ => false` in AllowsLock) has no fixed test, only review.
SOURCE: docs/18-status-and-decision-log.md:5123-5137; docs/19-requirement-traceability.md:770, :776

## 34. [ADR-077 visible (customerVisible) basis support]
Supported explicitly. The Application test No_worse_recovery_under_the_visible_basis_allows_no_more_than_the_kept_overrun builds a policy with CommitmentBudgetBasis.CustomerVisible, a 400 ms DropEtaTotalMs cap and 500 ms drift. A changed route that keeps the drop is exempted as ForcedNoWorse with code BudgetExceeded and AttemptedBudgetAfter.DropEtaTotalMs = 500. A route adding 300 ms (800 ms) stays rejected with BudgetExceeded. In the implementation, KeptRouteReference charges the kept route with DecisionInduced or Visible deltas according to policy.BudgetBasis, and AllowsBudget requires the same dimension with witness.After ≤ the kept After. ADR text lists 'cơ sở nhìn thấy' among the Application tests, and the Domain invariant is 'ngân sách tính theo cơ sở của chính sách'. The Domain test No_worse_breach_rejects_foreign_codes_and_a_charge_outside_both_bases also exists.
SOURCE: tests/RideBound.Application.Tests/Commitments/CommitmentDeadlineValidatorTests.cs:420-452; src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:779-788,814-817; docs/18-status-and-decision-log.md:5083,5096-5097; tests/RideBound.Domain.Tests/Incidents/OperationalIncidentLedgerTests.cs:390

## 35. [ADR-077 two-sided deadline support]
Supported explicitly. Rule text: 'hạn chót dưới: giờ trả ≥ giờ trả của tuyến giữ'. The code maps DeadlineFloorRule to: the kept route also has a floor witness AND candidate.DropEta ≥ kept.DropEta. The test No_worse_recovery_under_a_two_sided_deadline_compares_on_the_floor_side uses Policy(slack: 400, twoSided: true), a first promise of 1700 ms and a kept route of 1200 ms. Keeping 1200 ms is exempted as ForcedNoWorse (DeadlineExceeded). 1250 ms (still under the 1300 floor but closer) is exempted as ForcedNoWorse with a published DropEta of 1250. 1500 ms is inside the window and needs no exemption. The ADR lists 'cận dưới hai chiều' among the tests, and a mutation inverting the floor side was caught.
SOURCE: docs/18-status-and-decision-log.md:5078, :5098, :5109; src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:808-810; tests/RideBound.Application.Tests/Commitments/CommitmentDeadlineValidatorTests.cs:471-504

## 36. [ADR-077 end-to-end arm coverage]
The A1 end-to-end runs listed in ADR-077 name only the M⁺-x arms (22), C-30 (4) and M⁺-900 (2). No two-sided (M) or V arm is named under no-worse in A1.
SOURCE: docs/18-status-and-decision-log.md:5113

## 37. [Tier 3 T3.5–T3.7 pilot (change history 2026-09-25)]
Runner E:\RideBoundData\research\runner-tier3-v1 from 69512d3. Pilot of 60 jobs = 5 arms (U, C-30, V-30, M⁺-30, M-30) × 2 dev cells d20181112-s10-r1-w08/w17 × 6 worlds; 60/60 pass, audit 60/60. H1 held 12/12: C-30 had no recovery decisions, with a max per-rider dispatch deviation of 19.1 s. C-30 served ≥ V-30 in 12/12 episodes, a gap of 0–10 riders out of 108. The STOP GATE was triggered: V-30 and M-30 recovered in the majority of decisions in 5/12 episodes each (frozen vehicles, up to 30% of the fleet on average), so the owner must fix the recovery rule before the confirmatory comparison. World finding: the frame and the Tier-2 drift factor were applied only at the first trigger after the boundary; wrapper v1.1 inserts frame starts into the event clock, and its end-to-end smoke PASSED. Panel A cell d20181114-s10-r1 was already seen in the T3.5/T3.6 smoke and must be declared at the T3.8 split. Report: tang3/T3.7-BAO-CAO-THI-DIEM.md.
SOURCE: docs/18-status-and-decision-log.md:5174-5196; docs/19-requirement-traceability.md:746-759

## 38. [docs/19 §30 continuation gate P6]
Gate P6: audit PASSED; mechanism PASSED; recovery NOT PASSED (V-30/M-30 5/12, M⁺-30 2/12 episodes with > 50% non-normal decisions). Known limits: one episode per cell; frozen vehicles; thin post-gate insertion choice (0.7–3.3% per vehicle under C-30); Panel A cell d20181114-s10-r1 already seen.
SOURCE: docs/19-requirement-traceability.md:758-759

## 39. [docs/19 sections present]
§27 ADR-074 (lines 687-705), §28 ADR-075 (707-727), §29 ADR-076 (729-744), §30 Tier 3 T3.5–T3.7 (746-759), §31 ADR-077 (761-776). §31 is the last section. §27–§29 still say 'chưa commit', and §27 names branch research/deadline-gate.
SOURCE: docs/19-requirement-traceability.md:687,689,707,709,729,731,746,761

## 40. [Authorization boundary]
Every research ADR states it does NOT authorize RB-WP14R-009..012, WP15 or H7. All results carry the exploratory label (thăm dò).
SOURCE: docs/18-status-and-decision-log.md:4733, :4812, :4955; docs/19-requirement-traceability.md:689,709,731,749,763

## 41. [Required updates for new Tier-3 runs]
Per AGENTS.md, any task that changes status, contracts, claims, baselines, metrics or next actions must update docs/18, the relevant decision entry and docs/19. On this branch that means: docs/18 header line 4 (branch/date/status); the Evidence of ADR-077 (or a new ADR-078+ for a new rule or key); a new top entry in docs/18 §9 Change history; and docs/19 §31 (or a new §32) rows. Run dotnet test RideBound.slnx for any code change (current baseline 1025/1025).
SOURCE: e:\Code\RideBound\AGENTS.md (Repository guidance + Verification baseline); docs/18-status-and-decision-log.md:4, :5163-5173; docs/19-requirement-traceability.md:761-776

## 42. [Measurement rules future Tier-3 analysis must obey (from ADR consequences)]
(1) Count violations with NonNormalCertificateCount, certificate witnesses or the incident ledger, not BreachCount (always 0). (2) Count 'forced vehicle still serves' by the forcedNoWorse certificate stage, not the ForcedNoWorse record kind. (3) Count predicted exogenous pickup-window breaches and actual LatePickups separately; never add them. (4) Arms of one comparison share the same lateBoarding value and identical WP4 config bytes. (5) Do not use WP13/WP14 tools (wp14_frontier_analyze.py, wp14_mechanism_probe.py, wp13_recorded_witness_relaxation.py, level-by-position readers) on deadline or recovery output. (6) Compare controls by labels, not text or candidate id. (7) Declare the seen Panel A cell d20181114-s10-r1 at the T3.8 split. (8) The owner must fix the recovery rule before the confirmatory comparison.
SOURCE: docs/18-status-and-decision-log.md:4772-4782, :4905-4907, :4927-4930, :5035-5036, :5043-5045, :5049-5051, :5132, :5186-5188, :5194

# UNVERIFIED
- Whether the 'V' arm (V-30 in the T3.7 pilot) is the customerVisible-basis arm. docs/18 and docs/19 in this slice do not define the arm letters U/C/V/M⁺/M.
- Whether the owner formally fixed no-worse-than-reference-v1 as THE recovery rule for the confirmatory comparison (T3.8). ADR-077 stays 'Proposed' and no text in the slice records an acceptance.
- Contents of tang3/sweep/SWEEP-REPORT.md §7, SWEEP-AMENDMENTS.md A1 and the noworse-* logs. I confirmed the files exist but did not read them; the numbers reported come from the docs/18 ADR-077 text.
- Whether any Tier-3 run happened after 2026-09-26 (e.g. an M⁺(b) visible-basis run mentioned in user memory). No entry in docs/18 §9 or docs/19 on this branch covers it.
- The exact Python test command and count for the noworse branch. ADR-077 reports only .NET 1025/1025; no Python count is given for ADR-077.
- Whether docs/18 §5 'Next action' on the noworse branch has any research next-steps. Only the change-history note that §1/§5 of the main tree are unchanged was read (line 5218).
# WARNINGS
- ADR-074/075/076 headers in docs/18 (lines 4726, 4803, 4945) and docs/19 §27–§29 (lines 689, 709, 731) still say 'chưa commit', but they are committed and pushed (65d867c, 8d1ea4d, 69512d3). A future docs update should correct these labels.
- The docs/18 header in E:/Code/RideBound-deadline predates ADR-077. That worktree is on research/tier3-failure-aware at 1ce15e9, not research/deadline-gate. The authoritative docs for continuing work are in C:/Code/RideBound-noworse (research/tier3-no-worse, a90b4b7).
- E:/Code/RideBound-deadline shows 144 ' M' files that are line-ending-only; git diff is empty. Do not treat them as real changes, and do not reset or clean them (user constraint: never delete or clean).
- ADR-077's changed-route Runner path has no fixed in-repo integration test. Evidence is only the 22 A1 FleetPy jobs outside dotnet test, so a code change there cannot be regression-checked by dotnet test alone.
- The ADR-077 A1 runs cover only M⁺ and C arms. Two-sided (M) and visible-basis behaviour under no-worse is backed only by unit tests, not end-to-end runs.
- The T3.7 stop gate (recovery NOT PASSED) was the reason for ADR-077. The docs record no re-run of the full pilot or sweep gate criteria under no-worse, only the 28-job A1.