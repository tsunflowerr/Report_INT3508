# R28 - Stage-1b harness recheck by Codex (2026-10-12)

**Verdict: NOT READY.** The original checkpoint counterexample and most specific R24 controls are repaired. However, the intermediate-digest exception does not meet the retained full validity criterion, and a checkpoint with a duplicate JSON field demonstrably passes. Freeze scope/drift handling, input-check exceptions, final AC admission and smoke evidence need further changes before seal. The approved panel, ON configuration and numerical thresholds remain intact.

I read the supplied logs rather than rerunning the suite. Additional checks were read-only Python -B probes using archived bytes, extracted functions and synthetic objects in memory. No simulation, Runner/.NET invocation, build, publish, commit, freeze, seal, install or harness edit was performed. Only this report was created, exclusively, inside codex-work.

## 1. Sources and snapshot

Citation roots:

- H/ = E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/.
- S/ = E:/Code/Report_INT3508/ridebound-scratchpad/.
- D/ = S/optimize/codex-debate/.
- R/ = C:/Code/RideBound-costfirst/.
- F/ = E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/.
- A/ = C:/RideBoundData/research/tier3-t38-v1/.

I started with H/HARNESS-FIX-REPORT-R24.md. Current hashes reproduce its reviewed snapshot and both log headers (H/HARNESS-FIX-REPORT-R24.md:16-23; H/selftest-2026-10-12-v2.log:2-8; H/selftest-2026-10-12-r24-original.log:2-8).

| Artifact under H/ | SHA-256 |
|---|---|
| compare_equivalence_stage1b-v2.py | e469cac16271a3fbcf7332a8f22590fa4328023f303ac64d9d14dc414ff99ce0 |
| run_stage1b-v2.py | f2399c4f28028e9344a139296a575f21f65d93199305b5bad083eeefe125e62a |
| test_compare_equivalence_stage1b-v2.py | fe795e0e1f501e467f04060b9a2e93eb6e5240912537cd70e10dffeb1e4d3bce |
| STAGE1B-PLAN-DRAFT-v2.md | 9f6e439b992e9c6bfc4dc8caf15cfab95c6722840001ee100bbe628974b3f2d4 |
| RUNNER-PROVENANCE-TEMPLATE-v2.md | 6193e67011ca3b606eb65ff259c64dae9b0c62b8b219a4f941638cfa093ce8e4 |
| selftest-2026-10-12-v2.log | 4cea513cfc6be5d3d4b39bb9719e8159599dada674a1e147f89b2c609db08034 |
| selftest-2026-10-12-r24-original.log | 0de0be53616754e2b052cd76cdf63a475fb90fbb08fa14cc5d67860987e0a44b |
| plan-dryrun-2026-10-12-v2.txt | 7c358a29ef4d48c83cd3c1237df0a8d6c0790899d6908d1e549c231c2b94d7bf |

The original comparator, driver, test, draft, provenance template, canonicalizer and ON WP4 hashes still match R24. My read-only Git check reproduced the production diff SHA c48042af4e7cee2db01bdee5efb804dac703d80c8c657276fc5718816e1ad690, the R22-reviewed snapshot (D/codex-work/R22-CODE-REVIEW-CODEX.md:21-28). The published v3 runner and Stage-1b output root remain absent. No real rebuilt OFF/ON trajectory or replay is available to certify.

## 2. Disposition of every R24 finding and ancillary requirement

| R24 item | Status | Evidence and remaining limit |
|---|---|---|
| F1 - content digest validity | **PARTLY FIXED** | Manifest, initial state, decision 1, checkpoint content/state and final closure are recomputed (H/compare_equivalence_stage1b-v2.py:319-400,774-780). The original checkpoint counterexample now fails for its digest mismatch (H/selftest-2026-10-12-v2.log:90). Decisions 2..N/intermediate states remain unchecked by content; N1/N2 below prevent a full validity pass. |
| F2 - complete freeze/external execution inputs | **PARTLY FIXED** | Exact nonempty, duplicate-free inventory and tree/environment/absence checks are implemented (H/run_stage1b-v2.py:350-442). FleetPy, Python prefix, host/fxr and NETCore.App are covered (:111-124,298-316). Resolver scope and durable treatment of observed drift need N3. Historical equality is explicitly unproven; section 5 gives an acceptable limited contract. |
| F3 - global latches, malformed runs, report paths | **PARTLY FIXED** | Global phase latches/closed phases, malformed-run catch paths, bare report names and verdict-first writes are repaired (H/run_stage1b-v2.py:469-477; H/compare_equivalence_stage1b-v2.py:1243-1254,1261-1371). Input-validation exceptions still skip the verdict (N4); drift is not a durable latch (N3). |
| F4 - smoke evidence/recorded inspection | **PARTLY FIXED** | Missing evidence fails, fallback/feasible positives are included, bounds/work are reported, and main requires a hash-bound human inspection (H/compare_equivalence_stage1b-v2.py:988-1187; H/run_stage1b-v2.py:495-509,542-543). Optimal objective completeness and numeric bounds need N6. |
| F5 - AC, STOP, disk admission | **PARTLY FIXED** | Battery override refused; power wait checks STOP on return; admission reserves space under a lock and releases in finally (H/run_stage1b-v2.py:512-516,553-569,603-635,670-671). AC is not rechecked after admission queue/stat delay (N5). |
| F6 - start rules, Stage 2, H3 wording | **FIXED as plan text** | A1/deadline/weeks/amendment fields and no-start rule are present (H/STAGE1B-PLAN-DRAFT-v2.md:26-34), time-box consequence restored (:127-128,197-198), H3 replaced (:175), second-binary/120-s recheck constraints explicit (:202-209). Actual FILL facts remain unestablished and must be completed before seal. |
| Preserve original files | **FIXED/verified** | Original hashes reproduce R24; v2 files are separate (H/HARNESS-FIX-REPORT-R24.md:16-24). |
| Exact behavior/narrow DLL exception/stable hashes | **Retained correctly** | IDs, stable hashes, certificate cardinality, action multiset and ordered histories/routes/frames remain compared (H/compare_equivalence_stage1b-v2.py:507-608,711-764,846-847,897-954). No new blanket exclusion of execution diagnostics was found. |
| Separate runner/harness provenance; publish cwd | **Procedural fixes made; actual receipt pending** | Template distinguishes commits, states manual-review limits and moves Set-Location before SDK diagnostics (H/RUNNER-PROVENANCE-TEMPLATE-v2.md:3-18,24-42,72-87); driver rejects backticked placeholders (H/run_stage1b-v2.py:200-208). Actual source/build facts still require review. |
| Freeze main analysis scripts before inspecting results | **NOT FIXED as an artifact; openly deferred** | Scripts still do not exist; later amendment/freeze before first main-output inspection is promised (H/STAGE1B-PLAN-DRAFT-v2.md:192-195). This need not block a corrected Gate-0-only seal, but must be fulfilled before main analysis. |

Retain the successful fixes. No production objective-order change is requested by this review.

## 3. Remaining/new findings, ranked by severity

### N1 - P1: intermediate-digest GAP cannot satisfy the unchanged full validity gate

Locations: H/compare_equivalence_stage1b-v2.py:27-31,319-400,513-521,949-953; H/test_compare_equivalence_stage1b-v2.py:758-771; H/selftest-2026-10-12-v2.log:98.

**Answer to the brief: exact behavior alone does not close this gap under the retained R22/R24 validity contract.** It is strong behavioral evidence, but a protocol-invalid tape can have identical actions, ledgers and normalized frame content. The logged GAP accepts a consistently substituted middle decision hash. This violates the validity precondition; it does not show that a changed fleet outcome escaped the eleven comparisons (D/codex-work/R22-CODE-REVIEW-CODEX.md:173,190,200-208; D/codex-work/R24-HARNESS-REVIEW-CODEX.md:62-66).

The limitation is real. canonicalInputState contains the production pre-batch online state (R/src/RideBound.Runner/Protocol/RunnerSession.cs:768-799). CalculateDecisionHash binds that input, the previous digest, manifest digest, policy version and decision projection (R/src/RideBound.Contracts/Serialization/ProtocolHash.cs:31-67). A link check cannot establish that formula without the state. Not recreating the reducer in Python is correct; it does not establish middle-digest validity.

**The new positive fixtures are still partially rebuilt.** rebuild updates decision 1, its ACK/next link, initial/final state endpoints, manifest and checkpoint; it does not recompute decisions 2..N (H/test_compare_equivalence_stage1b-v2.py:323-348). P2v changes the manifest DLL (:423-426), changing the manifest and first decision digests while later decision digests are retained. The production formula binds the new manifest/previous digest at every step. P3v likewise retains arbitrary remapped middle values. Therefore "valid rebuilt run" and "protocol-valid" overstate the positives (:324,727-728,756-757; H/selftest-2026-10-12-v2.log:46-47,89,97). The GAP mutation is applied to that partially rebuilt base, not an independently validated complete v3 tape.

**Required:** add production .NET replay/validation, specified in section 4, before the combined GATE0 PASSED verdict. Retain behavioral comparison as a separate component. Relabel the synthetic positives as validity-limited until a complete production-validated trace exists. A renamed behavioral-only gate could use the current middle checks, but that would amend the criterion; the draft still claims exact R22 compliance (H/STAGE1B-PLAN-DRAFT-v2.md:94,107-115). I do not approve silently weakening it.

### N2 - P1: duplicate JSON fields are discarded before verification; confirmed false pass

Locations: H/compare_equivalence_stage1b-v2.py:455-457,498-500,677-689; R/src/RideBound.Contracts/Protocol/ProtocolPayloadValidation.cs:69-88; R/src/RideBound.Contracts/Protocol/CheckpointMessages.cs:75-81.

Default json.loads retains the last duplicate-key value. Digest reconstruction then operates on the lossy object. Transport receipts do not restore the discarded field.

**Read-only counterexample:** I duplicated the existing checkpointHash field, with the same value twice, in the archived U-w08 final checkpoint (frame 2019), then refreshed that frame's SHA/length and the bundle receipt. Comparison against the original returned:

~~~text
DUPLICATE_CHECKPOINT_HASH_PAIR_PASS True problems []
CHECKPOINT_FRAME 2019
All eleven components identical
~~~

The probe used archived identity constants for both in-memory copies; it did not authenticate or execute a new runner. The C# checkpoint payload calls ValidateObject, which rejects that duplicate-field shape. It is malformed protocol evidence, not an allowed salt or valid transport-format variation.

**Required:** recursively reject duplicate fields in transcript records, protocol envelopes and artifact metadata. Apply raw protocol canonical-number/schema checks before parsing loses information; summary/resource schemas need their own appropriate rules. Add fresh-receipt duplicate negatives at envelope and nested checkpoint/decision paths, plus ordinary valid-encoding positives. Preserve exact comparisons.

### N3 - P2: broader freeze still lacks resolver closure and durable drift handling

Locations: H/run_stage1b-v2.py:111-124,298-316,338-341,428-441,572-600,607-631,739-756; H/HARNESS-FIX-REPORT-R24.md:169-177.

- **Resolution is not closed.** PATH is omitted. My pure probe changed PATH between X:/tool-v1 and X:/tool-v2; frozen_env remained identical. Jobs/readiness resolve bare git through that path (H/run_stage1b-v2.py:250; F/actual_fleetpy_medium_preflight.py:727-752). A frozen PYTHONPATH/PYTHONHOME value also does not freeze referenced external contents. The actual interpreter's Lib/site-packages/distutils-precedence.pth:1 reads SETUPTOOLS_USE_DISTUTILS, an import-steering variable outside the selected prefixes. These are coverage limits, not proof that an actual job used a wrong module. The supplied dry run has an empty selected environment (H/plan-dryrun-2026-10-12-v2.txt:17,39,129).
- **Per-job checks are metadata checks.** They compare size/mtime and selected added paths (H/run_stage1b-v2.py:581-600), with full hashing before phases and at comparison. The disclosed optimization detects ordinary edits but does not authenticate every completed job's runtime bytes throughout execution. A final hash check observes the tree only at that time. No main comparator/full post-phase check is implemented in the current driver (:703-756; H/STAGE1B-PLAN-DRAFT-v2.md:192-195).
- **Observed drift is transient.** Admission.halted exists only in memory. A new run invocation creates a new object. My probe first returned deferred-input-drift; after restoring the stubbed condition, a new Admission admitted the next job. This path writes no failure file (H/run_stage1b-v2.py:607-631,742,752-756). Previously completed outputs can remain while an observed provenance failure is forgotten; restoring bytes does not establish what an already-running job read.

**Required:** freeze the effective resolver policy/resolved tools, including PATH/Git; audit or reject redirects outside declared trees, or freeze those contents. Preserve the full FleetPy/Python/.NET manifests. Persist observed input/environment drift as a global stop receipt rather than an ordinary battery/disk deferral. Bind full post-phase verification to main as well as controls, and describe the stat-based between-check limitation precisely. This does not require freezing the whole OS; it requires closing the declared dependency/resolver scope.

Historical equality is a separate issue that can be accepted with section 5's bounded contract.

### N4 - P2: frozen-input exceptions still skip the failure verdict

Locations: H/compare_equivalence_stage1b-v2.py:1327-1329,1354-1362,1369-1371; H/run_stage1b-v2.py:212-238,350-442,531-537.

Run-artifact evaluation is caught, but runner identity loading and frozen_input_problems are outside those catch blocks. A frozen WP4 changed to malformed JSON raises during canonical parsing rather than returning its hash-mismatch problem; unreadable tree files can raise during full hashing. Evaluation/verdict writing is never reached.

A pure invocation of extracted main with ready/started synthetic prerequisites and an injected input-check ValueError confirmed:

~~~text
FROZEN_INPUT_EXCEPTION_ESCAPES ValueError writes []
~~~

This contradicts the fix report's post-start input-drift failure rule (H/HARNESS-FIX-REPORT-R24.md:105-107). The malformed-summary test covers a different, repaired path.

**Required:** after establishing ready/started status, convert inability to validate frozen inputs/runner identities into an explicit persisted phase failure. Keep genuinely unstarted/unsealed refusal distinct. Failure receipts should record frozen expected identities when live identities are unreadable. Add started-run corrupt-config/unreadable-tree tests.

### N5 - P2: AC can be lost during admission queue/stat checks without another power check

Locations: H/run_stage1b-v2.py:553-569,603-631,653-666.

The strict power-wait fix is correct. A worker can then wait for Admission's lock while other workers scan tens of thousands of files. Admission checks STOP, latches, stats and disk, but never AC. A pure probe with ac_only=False still returned None (admitted). This queue/stat interval is more than the small unavoidable interval after a final check.

**Required:** recheck ac_only after potentially long admission checks and immediately before launch/reservation; defer/release if power is lost. Test AC loss after the power wait or while queued. The STOP fixes and mutex reservation/finally release are sound within one driver invocation; reservations are process-local, so concurrent driver instances should be refused or explicitly prohibited.

### N6 - P2: optimal smoke evidence can omit all tie objectives or contain invalid bounds

Locations: H/compare_equivalence_stage1b-v2.py:967-985,1048-1072,1099-1120; R/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:397-416; R/src/RideBound.Application/Optimization/CandidateSelectionSolver.cs:118-150.

The order checker accepts prefixes for all statuses. Optimal requires only bounds through operational-cost with the listed levels proven; it does not require the candidate-rank suffix. Numeric types/ranges, sense direction and exact gap arithmetic are not fully validated.

Using the same kind of archived decision rewritten to the CF list as the suite's fixture (H/test_compare_equivalence_stage1b-v2.py:1207-1218), I confirmed:

~~~text
CF_EVIDENCE_BASE_PROBLEMS []
OPTIMAL_MISSING_ALL_CANDIDATE_RANKS []
NEGATIVE_OPTIMAL_COST_BOUND []
~~~

The second variant keeps accepted count/cost only in both optimal diagnostics. The third sets cost incumbent and best bound to -1 in both. Both report no evidence problems. The selector adds a rank per ordered vehicle set; OR-Tools reports every level before returning optimal, including constants (R/src/RideBound.Solvers.OrTools/OrToolsCandidateSelectionSolver.cs:30-63,280-318). ObjectiveSolveBound.Create rejects negative values.

The synthetic prefix positives also need their numeric invariants rebuilt: they change isProvenOptimal/bestBound without consistently updating gap fields (H/test_compare_equivalence_stage1b-v2.py:1257-1259,1285-1293). They establish shape handling, not complete diagnostics validity.

**Required:** distinguish complete optimal lists from supported feasible/budget prefixes. Verify rank membership/ordinal order and forced-level presence when activation is established. Validate canonical integer/boolean types, nonnegative ranges, sense/gap arithmetic and counters against frozen budgets. Preserve supported fallback/empty-bound reasons and add these negatives. No additional simulation cells are needed.

### N7 - P3: self-test fallback can hide failed live runner-tree verification

Locations: H/test_compare_equivalence_stage1b-v2.py:384-387,526-528.

Ctx replaces a failed runner_identity_from_disk result with the manifest checked against its own lines. R1 then tests the replacement and can report "archived tree == manifest" despite live verification failure. The log does not establish that this branch actually occurred; I am not alleging current v2-tree corruption.

**Required:** retain/report the live failure as BAD before using a manifest-only identity for unrelated synthetic controls. Production Gate 0 independently checks the actual tree, so this is an evidence/test defect, not a demonstrated production-tree bypass.

### N8 - P3: Unicode canonical fallback skips the integer-range check

Locations: H/compare_equivalence_stage1b-v2.py:211-235; H/canonical_wp4.py:94-119; R/src/RideBound.Contracts/Serialization/CanonicalJson.cs:178-197.

A key at/above U+E000 returns the slow writer before finishing validation. That helper writes integers without checking their range. My probe with key U+E000 and value 9007199254740992 serialized successfully; the maximum is 9007199254740991. Tests separately cover Unicode fallback and range rejection, not their combination (H/test_compare_equivalence_stage1b-v2.py:712-726).

**Required:** finish validation before selecting the writer, or use a fully validating writer, and add the mixed Unicode/range negative. Current archived ASCII documents do not demonstrate a false rejection from this issue; it is a real helper-contract hole.

## 4. Required .NET replay: exact checks

**Yes: require production .NET replay/validation for a full Gate-0 pass.** Review/freeze the validator and receipt requirement before the four OFF jobs; generate their actual receipts afterwards. Nothing in this review authorizes or executes .NET.

1. **Bind tape and execution.** Hash transcript/bundle, verify the v3 runner DLL/tree, OFF WP4 with the key absent, matching arm commitment config, runtime and resolver/environment. Use the adapter's real startup arguments: --mode commitment --policy-config <arm> --wp4-config <OFF> --solver-seed-source manifest-master-seed and the same line limit (F/ridebound_fleetpy/session.py:355-368). Preserve recorded run/scenario IDs, seed, epoch/event sequence, simulation time and payloads.
2. **Replay all four new OFF tapes through frozen v3.** Send every adapter-to-runner frame in order, including negotiation, initialization, batches, ACKs, checkpoint request and shutdown. Consume exactly the recorded corresponding runner-response sequence. Do not substitute recorded decisions for generated Runner responses.
3. **Require exact unnormalized response content.** Strictly parse both sides and compare every raw field value, including every digest, publication/breach ID, certificate, route, solver bound/work/path and counter/time. Within a tape/replay, initialization and identities are the same; there is no reason to rename hashes. Valid encoding/transport differences need not fail when decoded content is exact. Byte equality is a convenient stronger check with identical codecs, but R22 excludes transport/wall-resource equality (D/codex-work/R22-CODE-REVIEW-CODEX.md:194).
4. **Require complete protocol closure.** Production must accept every batch/ACK and validate pre/post-state, commitments/recovery/certificates. Final full state, both ledgers, checkpoint digest and epoch/eventSeq/time boundary must match. Reject errors, timeout, missing/extra responses, truncation or prefix-only pass; require normal termination. Production hashing then covers every pre-batch state (R/src/RideBound.Runner/Protocol/RunnerSession.cs:532-559,562-565,651-673,768-799).
5. **Establish archive validity too.** R22 applies the precondition to both sides. Replay the four references through frozen v2/configs in the documented validation environment, or validate their whole state/digest chain with a reviewed .NET checker using the production codecs/reducer. Feeding a v2 initialization to another binary is not historical-binary verification. A current-environment mismatch must be reported/stopped, never normalized away or repaired in the reference.
6. **Persist/gate on receipts.** Bind validator hash/version, command/config/environment/runtime, DLL/tree, tape/bundle hashes, frame/decision/checkpoint counts, full coverage and first mismatch. Receipts for the actual four pairs are required before GATE0-PASSED.txt. Wrong/missing/partial receipt or mismatch is a durable failure. Recheck frozen inputs before/after replay.
7. **Test the validator.** Use genuinely production-valid positives. Wrong first/middle digest with consistent ACK/next links, wrong intermediate state, duplicate fields and missing/extra responses must fail for intended reasons. Partial synthetic positives remain normalization tests, not whole-chain validity proof.

This validates recorded inputs in the Runner; it is not another FleetPy trajectory. Disclose the .NET validation implementation/runtime/authorization before seal. Production reducer/codecs in .NET avoid the prohibited Python algorithm reimplementation (R/AGENTS.md:24-25).

## 5. Freeze scope and historical-baseline wording

**Complete? No, as an unqualified execution-input contract.** Exact inventory verification is good, and formerly missing FleetPy code including NetworkBasic is covered. All installed NETCore.App versions and host/fxr are appropriate for framework-dependent DLL execution; an SDK need not be frozen merely to execute the published DLL. Resolver closure and N3/N4 remain.

**Acceptable from freeze time only? Yes, as an explicit exploratory-design limitation, not proof of historical equality or clean selector isolation over all 34 cells.** No archived byte-level external-software baseline was supplied. I have not proved none exists anywhere; the fixer's search is reported in H/HARNESS-FIX-REPORT-R24.md:169-177. Labels/install dates/four OFF pairs do not establish old runtime bytes or exclude effects elsewhere.

Replace unqualified "same inputs"/"unchanged from T3.8" wording (H/STAGE1B-PLAN-DRAFT-v2.md:48-49,62-73), retaining verified fixture/config/input identities, with:

> Stage 1b uses the execution software, resolved tools and steering environment recorded in the input freeze. They are fixed from freeze time and shared by all new OFF, smoke and main jobs. The archived SF-U/SF-C30 controls retain their recorded configuration, fixture and transcript identities. No archived byte-level baseline was located for their external FleetPy/Python/.NET execution environment, so historical software equality is unverified. Gate 0 requires valid evidence and exact behavioral reproduction on the four specified arm-cell pairs; a pass establishes compatibility on those pairs, not equivalence on every main-panel cell or absence of runtime confounding. CF-versus-archived-SF results are reported as exploratory model-experiment contrasts with this provenance limitation, alongside service composition, guards and cell/day patterns.

Adopt/freeze this clarification explicitly before execution. It does not waive known input/config/hash mismatches or protocol validity, and does not automatically add jobs. Stronger software-isolated attribution would require separately scoped stronger control/baseline evidence.

## 6. Do the R24 tests fail on originals for the right reasons?

**Mostly yes, for the specific controls reported.** I independently counted original 16 OK/49 BAD and v2 148 OK/0 BAD/1 GAP, and verified header hashes. Suite PASS with GAP is not complete Gate-0 validity (H/test_compare_equivalence_stage1b-v2.py:63-73,1408-1413).

| Group | Original log | Assessment |
|---|---|---|
| F1 | H/selftest-2026-10-12-r24-original.log:10-18 | Mutations consistently alter digests/references and refresh transport receipts (H/test_compare_equivalence_stage1b-v2.py:727-757). v1 PASS is the content-validity defect, not stale transport checksums. Positive labels still need N1's qualification. |
| F2 | H/selftest-2026-10-12-r24-original.log:19-28 | World supplies files, required inventory, external tree, environment and absent path; v1 checks only listed entries (H/test_compare_equivalence_stage1b-v2.py:779-846,863-902). Malformed-line ValueError is a genuine escape. |
| F3 | H/selftest-2026-10-12-r24-original.log:29-37,45-53 | Unrelated input checks are stubbed valid; real latch/admission logic and comparator main run with fake directories/writer (H/test_compare_equivalence_stage1b-v2.py:921-970,1113-1180). Positives establish admissible cases. |
| F4 | H/selftest-2026-10-12-r24-original.log:38-39,54-70 | Archived decision is rewritten to CF levels; individual missing blocks/accounting/path/bounds/detail defects are varied (H/test_compare_equivalence_stage1b-v2.py:1207-1337). Existing forbidden-level/order negatives correctly succeed even on v1. |
| F5 | H/selftest-2026-10-12-r24-original.log:40-45 | Real wait/launch logic is exercised with fake power, clock, processes and logs (H/test_compare_equivalence_stage1b-v2.py:988-1108). Nested calls model overlapping reservations, not separate processes or post-wait AC loss. |
| F6 | H/selftest-2026-10-12-r24-original.log:71-75 | These are text-presence checks (H/test_compare_equivalence_stage1b-v2.py:1352-1367), not milestone/deadline evidence; actual v2 text contains the intended changes. |

Rebuilt negative variants additionally require intended failure messages and no masking digest fault (H/test_compare_equivalence_stage1b-v2.py:395-417,582-601; H/selftest-2026-10-12-v2.log:50-65,69,73). Endpoint formulas reproduce all four references (:81-85); 2,819 archived Gate-0 decisions satisfy evidence rules with CF order disabled (:154). Those are meaningful checks, not real future-CF or full intermediate-state verification.

Missing negatives: duplicate fields, corrupt frozen-input exceptions, AC loss at admission, optimal missing tie ranks/invalid numeric bounds, transient drift restart, combined Unicode/range rejection and honest live-tree verification failure. Repair them and regenerate the logs after the fixes.

## 7. Plan, provenance and retained design

A1 milestone record, confirmed deadline, time remaining/amendment and no-start consequence match the requested structure (H/STAGE1B-PLAN-DRAFT-v2.md:26-34; D/claude-work/R17-FINAL-VERDICT.md:280-288; D/codex-work/R18-CONFIRM-CODEX.md:222). Fill actual facts and "none" or a genuine amendment reference before seal; a presence test/file hash cannot establish them. Requiring three weeks specifically at Stage-1b start is a conservative application of R17's Stage-1 start rule; any different continuation timing needs documentation.

Stage 2 correctly requires H2 AND H7 plus two weeks remaining; 34+34+2+2=72, all arms share the second binary, rechecks exercise 120 s, per-step semantics align, arms/cells/references are frozen, and extra validation is disclosed before approval. No empirical cumulative-versus-per-step outcome claim without Stage 2 (H/STAGE1B-PLAN-DRAFT-v2.md:202-209; D/codex-work/R18-CONFIRM-CODEX.md:226-232). Primary I_L=I_served-I_timely60, H6 cutoff 345 and service guard 2315 remain correct; H3 over-attribution is removed (H/STAGE1B-PLAN-DRAFT-v2.md:155-162,175-179).

Driver panel/arguments remain 4 OFF, 2 calibration smokes and 68 test jobs, with 35 distinct cells (H/run_stage1b-v2.py:93-96,138-185; H/plan-dryrun-2026-10-12-v2.txt:2-6,25-27,115,123). Main requires both verdicts plus inspection, tied to the verified runner (H/run_stage1b-v2.py:480-509,539-543). Output reuse guards, exclusive logs/verdicts and keep-awake cleanup remain (:641-672,743-755; H/compare_equivalence_stage1b-v2.py:1237-1240,1370-1371). Missing future runner/receipt/freeze/seal artifacts are prerequisites, not passes.

Unchanged ON canonical SHA is 16dcb7e3337763aab7889f7528365dced2aa49028db6dbf390f8b3dce79b3140; CF-U binding 90b290d7e63f6885ac8e93e18017d55dddc54c27a05d8476a65dcf7d802e2df5; CF-C30 binding e6b33be5649dc2b1208b42b90cef227d00721cba59e4340fdbc4e96f21796f76 (H/selftest-2026-10-12-v2.log:10-20; D/codex-work/R22-CODE-REVIEW-CODEX.md:236-238). No config edit or additional simulation panel is requested.

Provenance separates runner source from harness commit and now runs SDK diagnostics from the source cwd (H/RUNNER-PROVENANCE-TEMPLATE-v2.md:9-15,26-42,72-87). Old publish command remains an explicitly labelled inference; new publish/test/toolchain/tree receipts remain future evidence (:94-107). Placeholder rejection aids completeness, not source-to-binary proof; manually review recorded facts before seal.

**Next sealing review:** close N1/N2, repair N3-N6, correct N7/N8 and regenerate meaningful pure controls; freeze replay code/receipt requirements and historical-baseline wording; complete actual plan/provenance facts at their authorized stage. Preserve originals and the reviewed production snapshot. Nothing in the supplied logs or this report certifies Gate 0, either smoke, publication or executed study results.
