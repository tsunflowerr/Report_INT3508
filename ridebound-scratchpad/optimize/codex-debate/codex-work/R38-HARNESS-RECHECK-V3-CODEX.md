# Round 38 - Stage 1b harness v3 recheck (Codex, 2026-10-13)

**Verdict: NOT READY.** The owner-authorized behavioural-only Gate 0 is adopted honestly, and the original duplicate-field, rank/bound, live-tree fallback and Unicode-range counterexamples are repaired. The remaining blockers are reproducible integrity and execution-control defects: unchecked run-report receipts, incomplete durable-stop coverage, STOP arriving during admission, and incomplete validation of smoke generation evidence. Close these and the pre-seal facts below before sealing.

The missing production validation of middle-decision digests is an accepted limit, not a renewed finding or a request for a .NET replay tool. This review follows D/ROUND38-HARNESS-RECHECK-V3.md:6-8,25-49 and the continuation instruction. That brief was read again before writing; no addendum was present in the 49-line version reviewed.

## 1. Scope and evidence

Path aliases used in citations:

- H/ = E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/
- D/ = E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/
- F/ = E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/
- R/ = C:/Code/RideBound-costfirst/src/
- A/ = C:/RideBoundData/research/tier3-t38-v1/

I began with H/HARNESS-FIX-REPORT-R28.md. Two independent sub-agents reviewed parser/smoke and driver/resolver behavior. I read their source anchors and independently reproduced the canonical counts, duplicate parser rejection, Unicode limit, missing-rank/negative-cost controls, omission counterexample, metadata counterexamples, startup/exception control flow, missing-freeze verdict behavior, STOP race and lexical path escape before including them here.

All executable probes were read-only Python -B with archived bytes or in-memory objects/AST-extracted definitions. Fake writers and paths kept control-flow probes entirely in memory. No job, .NET process, build, publish, commit, freeze, seal, harness edit or complete self-test rerun was performed. The sole review output is this exclusively created file. No pre-existing Round 38 report was found, so a -v2 report name was unnecessary.

Reviewed byte snapshots (full SHA-256; independently read from disk):

| H/ file | SHA-256 |
|---|---|
| compare_equivalence_stage1b-v3.py | 6c2f21195af641d29f8bee1c8c0e372bbaba6a74e3eb11e9cd90c7ff57cd7d52 |
| run_stage1b-v3.py | a5834eebf451c3da00f59fd67a15928ffe0f5ad05d4dcb31fd5d6e4a2d1f2ff2 |
| test_compare_equivalence_stage1b-v3.py | 1803d154e48e2de45cc731ba27cc8c11e9d47b68d1ad6e7cc1eebd031f8f144a |
| STAGE1B-PLAN-DRAFT-v3.md | b8fbe35c20688331c8cc198279a5aab670ca588f73bfb6d800703363228fcaf7 |
| RUNNER-PROVENANCE-TEMPLATE-v3.md | f44f0a1dca5d01342b76d006fe6368888d9a3bd0dc814074b0a72bd449cde6f0 |
| HARNESS-FIX-REPORT-R28.md | 7515d44f96a20128aa33cb918039b208a6180dd5c287639a9a2037ee4100a1ca |
| selftest-2026-10-13-v3.log | 928c5924dc8497b3864ec71f15fa7f3d2f9846bd48d01ce755f2164cdf630cde |
| selftest-2026-10-13-r28-on-v2.log | d372e58e91c1d3d29b96d442576483d5bb90f68ccc6e99c8f10560e5fb323531 |
| plan-dryrun-2026-10-13-v3.txt | 87351809a85c0f31ea88fbe1f7c0bef78a533a7e576223be6a031398a319971a |

The brief SHA-256 is b69559bebc644807c03f5468b1d95634f2d6bca78ea62d1a0d401eb7f1a33a9a. The five original and five v2 code/plan/template hashes still match the R24/R28 snapshots. Hashes identify reviewed files; they are not execution or sealing receipts.

## 2. Disposition of R28 N1-N8 and section 5

FIXED below refers to the requested correction under the amended criterion. PARTLY distinguishes a repaired original counterexample from an incomplete wider guarantee.

| Item | Disposition | Evidence and remaining qualification |
|---|---|---|
| N1 - middle-decision validity and misleading positives | **FIXED as the owner-authorized contract amendment** | Behavioural verdict names and disclosure are H/compare_equivalence_stage1b-v3.py:97-104; every Gate-0 verdict/report receives the disclosure at :1524-1531,1585-1593. Pair output identifies the unvalidated middle decision/state hashes at :1046-1050. Driver uses the amended word/names at H/run_stage1b-v3.py:118-119,687-700. Plan explicitly amends the old criterion, states that an invalid tape could pass, and requires exploratory reporting at H/STAGE1B-PLAN-DRAFT-v3.md:110-119,225-226,244-245. Smoke also carries the digest limitation (:158-159; comparator :1378-1380,1529-1531). Synthetic positives are labelled validity-limited normalization fixtures (test :7-10,345-348; v3 log :46). The accepted limitation remains; it is not claimed fixed technically. |
| N2 - duplicate JSON fields | **FIXED** | Recursive duplicate rejection and strict protocol-number parsing at H/compare_equivalence_stage1b-v3.py:196-244; strict bundle/report parsing :548-550; main frame loop :770-790. Repeating the final checkpointHash at U-w08 frame 2019, with refreshed frame length/SHA, raises DuplicateField. The rebuilt-bundle pair control fails (test :1449-1455; v3 log :167). Canonical compatibility counts are in section 3. |
| N3 - resolver closure and durable drift | **PARTLY** | Git tree, PATH/PATHEXT/GIT_* and distutils steering are covered (driver :133-151,379-445,446-571). Admission drift now writes a persistent stop (:798-802), and normal phase completion includes full verification (:874-880,984-989). Startup drift and exceptional phase exits still bypass persistence/post-verification (finding R38-2). Lexical .pth containment remains defective (R38-5), and bare taskkill is outside the declared tool audit (section 6). The stat-only interval limitation is accurately disclosed in plan :78-82. |
| N4 - frozen-input exceptions escaping the verdict | **PARTLY** | The original ready/started exception controls are repaired: guarded identity :1497-1511, input check :1566-1575, evaluation :1578-1593 write a failed verdict first. Driver groups checks with _guard at :661-684. However, disappearance of the freeze/seal/runner manifest after jobs have started is still treated as initial not-readiness and writes no verdict (:1556-1562; driver readiness :649-658). This is an unclosed boundary in the broader after-start guarantee; see R38-2. |
| N5 - AC lost after waiting/queueing; multiple drivers | **FIXED for the R28 findings** | AC is rechecked after the stat/disk scan immediately before reservation (driver :803-809); an OS instance lock is acquired for run (:820-837,966). The source and v3 log :194-196 support the intended repairs. The distinct STOP-after-scan problem remains R38-3. The unavoidable instant between a final check and process creation is already disclosed (fix report :160-161); this review does not demand atomic power/process creation. |
| N6 - missing optimal ranks and invalid objective bounds | **PARTLY** | Original missing-all-ranks and negative-cost probes now fail: expected ranks :1120-1127,1189-1193, complete optimal lists :1246-1257, and numeric/sense/gap/proof checks :1276-1297. Budgets are enforced at :1113-1117,1139-1142,1178-1180. Generation's nested omissions/loss evidence is still incompletely validated (R38-4). Forced-level activation is observable only when a certificate witness exposes it; section 5 states the limit. |
| N7 - live old-tree failure hidden by fallback | **FIXED** | Test Ctx saves the live identity, records a BAD result before manifest-only fallback, and R1 tests the live result (H/test_compare_equivalence_stage1b-v3.py:397-420,564-565). The injected failing live identity is exercised at :1745-1754 and recorded in v3 log :209. A manifest-only fallback supports unrelated synthetic controls; it no longer turns a failed live verification into suite success. |
| N8 - Unicode fallback skips integer range | **FIXED** | The complete validating walk precedes writer selection (comparator :292-329). Root probes: U+E000 key with 9007199254740992 rejects; with 9007199254740991 accepts. Source test :1765-1776 and v3 log :210-211 agree. |
| R28 section 5 - historical external-software baseline wording | **FIXED as disclosure** | Plan :51-54,66-88 adopts the limitation paragraph, preserves configuration/fixture/transcript identities, disclaims historical software equality, limits Gate-0 compatibility to four pairs, and describes CF-versus-archived-SF results as exploratory with composition/guards/cell-day patterns. The following clarification correctly applies the owner amendment to the paragraph's words "valid evidence". Technical resolver closure remains N3, rather than being established by the paragraph. |

I found no downstream claim in the reviewed plan/verdict paths that a behavioural pass proves full middle-decision protocol validity. The historical "New in v2" discussion and "Unchanged from v1" text in comparator :24-51 are historical descriptions; the governing v3 disclosure and plan amendment are explicit.

## 3. Canonical-JSON compatibility and repaired counterexamples

I ran the actual v3 decode_record and decode_frame over every record/frame of all four archived references, without rewriting them. Each raw transcript SHA-256 matched H/compare_equivalence_stage1b-v3.py:138-143.

| Archived A/ reference | Records checked | Canonical records accepted | Canonical frames accepted | Rejections |
|---|---:|---:|---:|---:|
| U-d20181116-s10-r1-w08 | 2,020 | 2,020 | 2,020 | 0 |
| U-d20181116-s10-r1-w17 | 2,284 | 2,284 | 2,284 | 0 |
| C-30-d20181116-s10-r1-w08 | 2,035 | 2,035 | 2,035 | 0 |
| C-30-d20181116-s10-r1-w17 | 2,146 | 2,146 | 2,146 | 0 |
| **Total** | **8,485** | **8,485** | **8,485** | **0** |

Thus the new canonical requirement causes no false rejection of these frozen Gate-0 references. It does reject whitespace/reordered-key encodings that decode to the same object; that is an intentional artifact-contract check, already required by the frozen verifier (F/actual_fleetpy_medium_verify.py:839-846,879-883), not an added behavioural comparison of transport bytes. It does not prove compatibility for arbitrary future protocol extensions.

Probe core, executed against the v3 module:

~~~python
for name, (expected_sha, expected_count) in ce.REFERENCE_TRANSCRIPTS.items():
    raw = (archive / name / "transcript-00.ndjson").read_bytes()
    lines = raw.decode("utf-8").splitlines()
    for line in lines:
        record = ce.decode_record(line)
        ce.decode_frame(record)
    assert len(lines) == expected_count
    assert hashlib.sha256(raw).hexdigest() == expected_sha
~~~

For N2 I repeated the exact duplicate-value counterexample. U-w08 frame 2019 is the final checkpoint: duplicate the existing checkpointHash property with its same value, refresh frameBase64/frameLengthBytes/frameSha256, and rebuild the bundle receipts. The strict parser rejects before the repeated property can be collapsed. This is not rejection because the raw frame receipt was stale. Nested action/envelope/record and summary/bundle duplicates also have explicit controls (test :1456-1503; v3 log :168-176).

For N6 I used the archived U-w08 epoch-3 decision, simTime 9000, whose diagnostics include stability levels. Removing worst-hard-utilization-ppm and revision:* from both primary/final diagnostics and reindexing gives a CF-shaped predicate fixture with zero v3 problems; the frozen audited-evidence verifier also accepts this baseline as version 1.1.0. Removing all candidate ranks then produces two "optimal level list is not complete" errors. Setting cost incumbent/bestBound to -1 produces two "not canonical non-negative integers" errors. These are evidence-predicate probes, not production CF trajectories. The source/log additionally cover wrong vehicle/order, boolean index, wrong gap/side and exceeded budget (v3 log :197-208).

The independent archived evidence calibration found 671, 759, 676 and 713 decisions respectively: 2,819 total, zero decision_evidence problems with cost-first ordering disabled. H/selftest-2026-10-13-v3.log:39-42,81-85,154 supplies the corresponding artifact/digest/evidence controls. This calibration does not prove complete validity of future CF evidence.

## 4. Remaining findings, ranked

### R38-1 - P2: a positive pair can carry corrupt run-report digests or a false artifact-receipt claim

**Locations:** H/compare_equivalence_stage1b-v3.py:548-573,925-936,1018-1025,1028-1050. The derived semantic fields are skipped from comparison at :931-932, but neither their own checks nor the root semanticHash/summary agreement are verified. Only report status is checked.

**Reproduction:** Load the archived U-w08 bundle as an identical-copy pair. For each separate in-memory variant, modify just one run-00 field, then regenerate that file's bundle length/SHA:

- semanticHash = 64 "f" characters;
- semantic.manifestHash = 64 "f" characters;
- semantic.checkpointBindingHash = 64 "f" characters;
- semantic.publicationDigest = 64 "f" characters;
- artifactReceiptsEqual = false.

For every variant, facts.problems = [], all eleven comparison components remain equal, and pair_report returns true. The transcript is untouched. The probe uses the archived manifest identity for both copies to isolate the report-check behavior; it is not a forged publication receipt or a claim that a real new runner was verified. A second independent probe changing the four digest fields together also passed.

Raw cross-run aggregate digest equality is intentionally waived. **Own artifact integrity is still required** by D/codex-work/R22-CODE-REVIEW-CODEX.md:194 and retained by the amended plan's preconditions (H/STAGE1B-PLAN-DRAFT-v3.md:132-139). The owner waived production validation of middle-decision digests, not the recomputable report receipt or artifact-drift flag.

The producer computes semanticHash from a domain plus canonical semantic data (F/actual_fleetpy_medium_preflight.py:660-694). The frozen verifier checks that hash, summary/run agreement and artifactReceiptsEqual, and reconstructs the publication digest (F/actual_fleetpy_medium_verify.py:1148-1163,1206-1210,1321-1338). Those checks can be made without replaying .NET or reconstructing the hidden pre-batch online state.

**Required correction:** Verify each report's recomputable semanticHash, its equality to the summary receipt, artifactReceiptsEqual is true, and available manifest/publication/counter links. Continue excluding salted raw digests from cross-run equality. Check the type/format of any binding whose complete adapter-state preimage is unavailable, and describe its validation limit rather than claiming reconstruction. The checkpointBindingHash includes physical adapter state (F/ridebound_fleetpy/fleet_control.py:1004-1035), so this finding does not demand an invented offline preimage.

Add separate fresh-bundle negative controls and repair normalization positives' own report receipts when their transcript-derived metadata changes. A validity-limited positive may retain the disclosed opaque middle hashes; it should not silently retain other inconsistent, recomputable metadata.

### R38-2 - P2: some after-start integrity failures leave no durable stop, and worker errors skip the post-phase check

**Locations:** H/run_stage1b-v3.py:649-658,966-969,975-989; H/compare_equivalence_stage1b-v3.py:1556-1562.

Three root-reproduced cases:

1. AST-extract driver main and inject frozen_input_problems returning an observed "frozen input changed or missing" problem. Run mode raises SystemExit at :969 with zero record_input_drift calls. This also applies on a later invocation after earlier jobs exist; the branch does not inspect that history. Restoring the bytes permits a fresh check without a persisted observation.
2. Inject a future whose result() raises OSError. The executor exits and keep-awake cleanup executes, but post_phase_problems at :984 is never reached. Probe calls were only awake(true), awake(false). A process-launch or exclusive-log-write error can reach this path (run_job :863-870). The main phase then lacks its promised post-phase full integrity check.
3. In the comparator, supply a started job directory and a missing-freeze readiness result. main raises "refused, not ready (no verdict written)" with writes = []. Actual readiness checks only existence of runner manifest, seal and freeze (:649-658), and occur before the started-state branch. Deleting one after execution is consequently handled like never having initialized the study.

Admission drift and normal completion persistence are fixed (:798-802,874-880); these uncovered paths make the plan's durable-stop/after-start promises incomplete (plan :78-82,148-151,255-256). Existing N4 controls stub readiness to success (test :1161-1162), so they cannot expose case 3.

**Required correction:** Distinguish never-started missing prerequisites from loss/unreadability of sealed inputs after the study has begun. Persist observed integrity failures in the latter case, recording frozen expectations where available. Put full post-phase verification in guaranteed cleanup after attempted work, including worker exceptions and partial/deferred phases; preserve the original error and prevent a clean completion claim if verification fails. Do not turn ordinary pre-start missing artifacts or power/disk deferral into invented drift. Add controls for missing freeze/seal/manifest after start, startup drift after earlier outputs, and a worker exception followed by a failing full post-check.

### R38-3 - P2: STOP set during the long stat scan can still admit a new job

**Locations:** H/run_stage1b-v3.py:788-809,854-865.

Admission checks STOP at :792 and the failure/drift latches at :794. It then scans every frozen file/tree (:798; stat_drift :764-774), checks disk, and rechecks only AC at :806 before reservation. Those scans can be lengthy.

**Root probe:** Make stat_drift set the fake STOP flag and return no drift, with AC true and ample disk. Admission.admit returns None, STOP is true, and reserved becomes 410 MiB. The caller then proceeds to subprocess.run. No actual process was launched in this probe.

**Required correction:** Recheck STOP and the global failure/drift latches after the long scan/disk work, alongside the final AC check and immediately before reserving/launching. Add a control for STOP arriving during the scan (and the corresponding latch case). This closes a material check-to-launch delay; the disclosed unavoidable last-instant race is a separate limit.

### R38-4 - P2: smoke generation evidence accepts impossible individual omission counts

**Locations:** H/compare_equivalence_stage1b-v3.py:1104-1132,1153-1157. Most nested loss/omission fields are not validated; omission counts are merely summed (:1119) and their saturation flags checked (:1128-1130).

**Root probe:** Begin with the accepted CF-shaped epoch-3 predicate fixture from section 3. Append two complete generation omission objects, each with code WORK_BUDGET, a valid 64-hex stableDigest and countWasSaturated false; set their counts to -1 and +1. Their sum is zero, so selection totals still agree. V3 decision_evidence returns []. The frozen audited-evidence verifier rejects exactly this input with:

~~~text
RuntimeError: epoch 3 solver evidence.generation.omissions[0].count must be a non-negative integer
~~~

The verifier requires nested fields and validates individual counts/types at F/actual_fleetpy_medium_verify.py:228-306. The proposed smoke contract promises complete generation evidence and auditable accounting (plan :160-168). Validating only an aggregate is insufficient.

This is a demonstrated smoke predicate acceptance, not a claim that a rebuilt complete smoke bundle was passed. A Gate-0 pair would still detect this changed diagnostic content against its untouched reference.

**Required correction:** Validate every nested generation loss/omission object's required/optional fields, array shape, individual numeric types/ranges, boolean fields, IDs and digest forms before totals; apply the same discipline to the remaining generation/pruning evidence promised by the plan. Reuse the frozen verifier's reviewed evidence checks where appropriate, adding the stricter CF-specific rules. Include a canceling-negative-count control and valid complete positives.

### R38-5 - P3: lexical .pth containment admits paths that escape a frozen root

**Locations:** H/run_stage1b-v3.py:416-435; freeze accepts this audit at :893 and freeze verification uses it at :560.

**Root probe:** With site E:/frozen/python/Lib/site-packages and root E:/frozen/python, the .pth path line ../../../../outside is accepted: pth_redirect_problems returns []. Its lexical path starts within the root, but pathlib.Path.resolve() yields E:/outside. _inside compares PurePosixPath ancestry without resolving "..".

This is a prospective audit defect. The actual supplied environment currently has only the reviewed distutils import line and reports a clean audit (dry-run :21-23; fix report :158-159,178). I did not establish that an outside directory exists or that any current job loaded external modules.

**Required correction:** Normalize/resolve candidates and roots, including relevant junction/symlink destinations, before containment. Audit executable .pth import lines explicitly rather than assuming any such line necessarily loads only frozen code (:426-431). Add traversal and valid in-tree controls. This can be repaired within the declared software scope; it does not require freezing the entire OS.

## 5. Honest limits and retained design

The N6 forced-objective limit is real and disclosed (H/HARNESS-FIX-REPORT-R28.md:162-163). Production activates forced-reference-count if any candidate has the forced assessment (R/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:304-322). Certificate witnesses describe selected forced exemptions (R/RideBound.Runner/Protocol/RunnerSession.cs:1090-1107). Comparator :1143-1146,1194-1196 infers activation from those witnesses, so it cannot establish activation when an unselected candidate was forced. The plan's smoke wording is qualified to the witnessed case (:164-167). Keep that qualification in reports; never claim independent proof of every hidden forced-objective activation. This is not a request to change the production evidence format or add replay jobs.

The plan retains the intended design: four OFF pairs, two calibration smokes, 68 main jobs and 35 distinct cells (plan :44-49; driver :165-170). OFF uses the original absent-key WP4, ON adds the cost-first value, and configuration bindings remain the decisive arm identity (plan :46-48,62-64). Solver evidence supports that identity rather than replacing it. Six workers, seed 7 and one repeat remain stated (:69-70).

The primary interaction identity, service-composition interpretation and H6 thresholds are retained (plan :184-191,203-208); H3 no longer attributes any threshold miss automatically to the selector. Stage 2 remains H2 AND H7 plus two weeks, 72 jobs sharing the second binary, changed 120-s OFF rechecks, consistent per-step semantics and no empirical cumulative/per-step outcome claim without that stage (:232-245). No extra stage or simulation is requested here.

Runner source provenance stays separate from harness coreCommitSha; manual review is still required (H/RUNNER-PROVENANCE-TEMPLATE-v3.md:9-18,26-42,72-74). The old publish-command reconstruction is explicitly an inference (:94-107). None of those template expectations is a completed build receipt.

## 6. Fixer's open items: what must close before the seal

| Open item | Before initial seal? | Required closure |
|---|---|---|
| Only git audited through PATH | **Yes: close the audit scope or record a precise scoped exception.** | REQUIRED_TOOLS is only git (driver :144). I verified another reachable bare command: Windows taskkill at F/ridebound_fleetpy/runner_client.py:532-542, called by shutdown timeout/failure paths :267-278. Audit the actual wrapper/adapter/runtime call graph, record tool resolution and bytes for reached external tools, and bind their resolver context. For taskkill, an explicit OS cleanup-tool exception is reasonable if its scope/limitations are documented; otherwise bind its resolved executable narrowly. Freezing every PATH directory or the whole OS is unnecessary. Current statements must distinguish deterministic execution software from excluded OS cleanup facilities. |
| Shell-dependent GIT_EDITOR | **Yes: settle and record the launch environment. The existing comparison mechanism is repaired.** | GIT_* is frozen (driver :140,379-385), and PATH/PATHEXT are recorded. The dry-run actually recorded GIT_EDITOR (:20,144). Choose the intended values/absences before freeze and ensure run/verdict invocations reproduce them. They may come from different shells if the recorded environment is equal. "Same shell" alone is insufficient if its environment changes; a different shell is not automatically wrong. Also audit settings consumed by any newly identified resolver/tool. |
| A1 / deadline / time remaining <FILL> facts | **Yes.** | Plan :29-37 requires an A1 record, confirmed deadline, and at least three weeks at Stage-1b start or an explicit owner-authorized amendment. The brief establishes only more than two weeks after 2026-10-12 (D/ROUND38-HARNESS-RECHECK-V3.md:35-36). That does not establish three weeks, the exact deadline, A1 completion or time left at the actual start. Record those facts and a calculation for the planned start, or the genuine amendment reference. If neither rule nor amendment is met, do not start. This review does not infer an amendment or fill invented dates. |
| Main-phase analysis scripts absent | **Not inherently before the initial seal under the retained plan. Their timing obligation must be explicit and honored.** | Plan :219-224 permits adapted extract/report code to be frozen by a hashed amendment before the first main output is opened. Missing scripts therefore need not block a Gate-0/smoke-only start once all other prerequisites are met. Develop/verify/freeze the CF extraction, reporting, interaction identity, guards and cell/day handling before main output inspection; preferably do this before main execution so the sequence is unambiguous. Do not open main results first and then choose code. If this cannot be assured, finish the scripts before sealing. |

Additionally, repair R38-1 through R38-5, regenerate focused pure controls and preserve reviewed originals. Complete actual runner/provenance, freeze and seal receipts only at their separately authorized stage. The driver rejects unfilled provenance mechanically, but an actual source-to-binary fact still needs manual review (plan :100-108; provenance :6-7,14-18).

## 7. Assessment of the supplied tests and dry run

I independently counted the log prefixes: v3 is **197 OK / 0 BAD / 1 LIMIT**; R28-on-v2 is **7 OK / 40 BAD / 0 LIMIT**. Their header hashes match the reviewed files. The final summary lines are H/selftest-2026-10-13-v3.log:212 and H/selftest-2026-10-13-r28-on-v2.log:58.

The negative reproduction controls fail on v2 for the stated defects, rather than stale frame receipts: duplicate variants refresh receipts, N4 injects exceptions behind successful readiness, N5 moves AC loss to admission, N6 varies list/numeric invariants, and N8 combines Unicode with the oversized integer (test :1437-1503,1583-1613,1616-1743,1765-1776; v2 reproduction log :15-57). N1 failures are adoption/disclosure checks, not new proof of an invalid hash. N6-l checks budget declaration equality; it is not another numeric counterexample.

The suite's PASS is valid for its enumerated expectations, with its one accepted LIMIT. It does not cover the new after-start missing-prerequisite/worker/STOP/metadata/omission/traversal cases above. Its original N4 readiness stub explains that coverage boundary.

The dry run enumerates 4 / 2 / 68 pending jobs and the expected missing runner manifest, seal, freeze and downstream verdict/inspection prerequisites (dry-run :2-12,30-38,129-136). A dry-run exit 0 means planning completed; it is not permission to execute or a gate pass. Read-only existence checks during this review still found no runner-tier3-v3 tree or tier3-stage1b-v1 output root; no actual final plan/seal/freeze/provenance/verdict artifact was found in H/. These absent future artifacts are prerequisites, not fabricated failures of a completed study.

**Sealing decision:** NOT READY because of R38-1 through R38-4, plus resolver closure R38-5 and the actual pre-seal facts/environment scope. The accepted N1 limitation and the properly disclosed historical baseline limit do not need to be re-litigated. After targeted repairs and reviewed receipts, reassess the amended behavioural harness; this report certifies no publication, Gate-0 pass, smoke pass or empirical Stage-1b result.
