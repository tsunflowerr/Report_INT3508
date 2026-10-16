# Round 41 - Stage 1b harness v4 recheck (Codex, 2026-10-14)

**Verdict: NOT READY.** V4 repairs the original R38 counterexamples. The main remaining blockers are the unretained identity of the main-analysis freeze and incomplete per-run outcome conservation. Align the tool exception and plan/provenance instructions before sealing. The accepted behavioural-only Gate 0 and its missing middle-decision validation are not reopened.

## 1. Scope and reviewed evidence

Aliases:

- H/ = E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/
- D/ = E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/
- F/ = E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/
- A/ = C:/RideBoundData/research/tier3-t38-v1/

The governing brief is D/ROUND41-HARNESS-RECHECK-V4.md. I read H/HARNESS-FIX-REPORT-R38.md, the five v4 artifacts and supplied self-test log, and the R38 review. Two independent sub-agents reviewed comparator and driver changes. I checked their cited source and independently reproduced the material probes reported below.

All execution was read-only Python -B: archived-byte parsing, AST-extracted definitions, fake paths/writers/workers, and the pure self-test's v3 target with no output-log argument. No FleetPy job, .NET execution, publication, commit, freeze, seal or harness edit occurred. This report is the only new filesystem output. The original R38 report and existing versions were preserved.

Reviewed SHA-256 snapshots:

| H/ file | SHA-256 |
|---|---|
| compare_equivalence_stage1b-v4.py | 5954f455712d84af15459314ced7eeccf4b591e60713bb969317969fb7f88fed |
| run_stage1b-v4.py | 5308a0b2a3b1c82b07ad4dedf9c580ff23930fa69404187685c0cfc3de230044 |
| test_compare_equivalence_stage1b-v4.py | 8f685b22737f0c6a9ee654d460af7072d25712393ff92c8423ffb4f806997869 |
| STAGE1B-PLAN-DRAFT-v4.md | 0340a7a84fc96253ae9c38494b4803bb71d10b582b333bc5f74f0152b4aaf009 |
| RUNNER-PROVENANCE-TEMPLATE-v4.md | f44f0a1dca5d01342b76d006fe6368888d9a3bd0dc814074b0a72bd449cde6f0 |
| HARNESS-FIX-REPORT-R38.md | dc5d7e1d44522606b4bb74cc1f1dd5840cafdba6ba0b3cb919257b5002d7656e |
| selftest-2026-10-13-v4.log | 98270fb626bb9ab3c67f5ee87d316f890f0a12448f0e0c0f9ea598d53e2847da |

The brief SHA-256 is ae590ad195c2451abc82ce68bb322127e061132b1d4a2b061cc9405a7f90d299. The six v3 code/plan/template/log hashes still match R38. In particular, the v4 provenance template is byte-identical to v3; its unchanged instructions matter in finding R41-5. Hashes identify the reviewed snapshot, not a published runner or a completed study.

## 2. Disposition of R38 findings and section 6

| Item | Disposition | Evidence |
|---|---|---|
| R38-1 - corrupt report digests and false artifact receipts | **PARTLY: original counterexamples FIXED; available per-run outcome checks remain incomplete** | Comparator report_problems recomputes semanticHash, checks summary receipts, requires artifactReceiptsEqual true, links manifestHash, and rebuilds publication count/digest (H/compare_equivalence_stage1b-v4.py:523-577,972-975). Root probes reject the original faults, including wrong manifest/publication values after consistently updating the aggregate receipt. Full per-run facts still accept impossible accepted/rejected report lists; see R41-2. Repeat booleans also pass (R41-3). |
| R38-2 - startup drift, worker exceptions, missing prerequisites after start | **FIXED for the reported cases** | Driver distinguishes input integrity from gates (:779-807), detects earlier outputs/logs/verdicts (:858-876), and persists startup loss (:1188-1196). Pool errors reach finish_phase through finally (:1205-1218); it releases keep-awake, performs the full post-check and guards its failures (:1058-1088). Comparator checks started state before readiness and writes failures for lost prerequisites (:1769-1822). Root probes show the v3/v4 change; supplied controls are log :239-250. |
| R38-3 - STOP/latches arriving during admission | **FIXED** | Final STOP and failure/drift-latch checks occur after the long stat/disk/AC work, before reservation (driver :976-992). Root STOP-during-scan probe: v3 admitted/reserved 410 MiB; v4 refused/reserved 0. All three negative controls and the positive are log :251-254. |
| R38-4 - nested smoke generation/pruning validation | **FIXED** | Nested generation arrays, exact fields, individual non-negative/non-boolean counters, flags, omission IDs/digests, exogenous breach ordering and breach inequality are checked before totals (comparator :1407-1463). Pruned/witness shapes are checked at :1466-1486. Root canceling -1/+1 omission probe passes v3 and rejects v4; independent loss-counter and exogenous probes agree with the frozen verifier. Supplied controls :255-274 cover negatives and complete positives. |
| R38-5 - lexical containment and executable .pth lines | **FIXED** | realpath/normpath/normcase resolution precedes containment (driver :487-499). Executable imports require the reviewed name/line hash (:502-517; allowlist :185-187), and both interpreter site directories are audited (:520-525). Root parent-traversal probe now rejects; the suite simulates a junction escape and tests the real reviewed import line (log :275-282). |
| R38 section 6 - pre-seal tools, launch environment, analysis and plan facts | **PARTLY** | Both tools and job/driver resolution contexts are checked and tool bytes are bound (:174-179,442-473,656-679). GIT_* is refused (:430-439). Main requires an analysis manifest before launch (:813-855,1191-1199). Owner facts and stricter timing are recorded in plan :32-36,260-275. The analysis identity can be replaced consistently, the System32 exception is not enforced, and the plan/receipt refer to different versions/filenames (R41-1,4,5). |

The format-only checkpointBindingHash check is an allowed limit from R38, not an unfinished request for an invented preimage. Comparator :10-12,575-577 states it precisely; log :237 records a consistently rehashed false binding as LIMIT. Its preimage includes unavailable physical adapter state (F/ridebound_fleetpy/fleet_control.py:1004-1035). H/HARNESS-FIX-REPORT-R38.md:29 should say "format and enclosing receipt" rather than implying full validation of that value.

The owner-authorized behavioural criterion, exploratory reporting and historical-software limitation remain explicit in H/STAGE1B-PLAN-DRAFT-v4.md:50-53,65-87,109-118,224-225,240-244. No production replay or additional simulation is required by this review.

## 3. Independent probes

### 3.1 Report receipts and archived calibration

I decoded actual archived transcripts to collect initialized manifestHash, promisePublished receipt projections, requestArrived identities, decision count, last event sequence/time and final fleet. I passed those arguments and the unchanged run-00/summary objects to the actual v4 report_problems.

| A/ run | Report-receipt problems |
|---|---:|
| U-d20181116-s10-r1-w08 | 0 |
| U-d20181116-s10-r1-w17 | 0 |
| C-30-d20181116-s10-r1-w08 | 0 |
| C-30-d20181116-s10-r1-w17 | 0 |
| Mplus-30-d20181114-s10-r3-w07 | 0 |

Thus the new report checks do not reject these archived positives. The supplied full facts calibration agrees (log :238); this lightweight independent calibration does not authenticate the opaque middle-decision digests.

On U-w08:

- semanticHash = 64 "f" characters rejects with incorrect hash and summary-receipt errors.
- semantic.manifestHash = 64 "f", with a freshly recomputed semanticHash and matching summary receipts, rejects the initialized-manifest link.
- semantic.publicationDigest = 64 "f", consistently rehashed, rejects the publication receipt link.
- artifactReceiptsEqual false rejects.
- An empty semantic accepted list or rejected list, consistently rehashed, returns no report problems (R41-2).
- Boolean repeat metadata returns no report problems (R41-3).

For the last two cases I also rebuilt actual run-00/summary bundle lengths and SHA-256 values, ran full facts and pair_report, and obtained:

~~~text
baseline: problems=[]
empty accepted list: facts.problems=[]
pair: false; only runSemantic differs (acceptedRequestIds)
boolean repeat metadata: facts.problems=[]
pair: true; all eleven components equal
~~~

Both copies use the archived manifest identity in this parser-only probe. It isolates artifact checking; it is not a claim that a new runner publication was verified.

### 3.2 Driver controls, v3 versus v4

AST-extracted main/Admission definitions ran with fake paths, processes and workers.

| Probe | v3 result | v4 result |
|---|---|---|
| Startup integrity loss with prior study output | SystemExit; no drift writer call | SystemExit; record_input_drift called with startup evidence |
| Worker OSError | Keep-awake released; post-check skipped | Futures canceled; keep-awake released; post-check called; original OSError preserved |
| STOP set by stat_drift during the scan | Admitted; 410 MiB reserved | Deferred STOP; 0 reserved |
| .pth ../../../../outside from E:/frozen/python/Lib/site-packages | No problem | Rejected; resolves to e:/outside |

The pool probe checks guaranteed cleanup and error propagation, rather than launching a child. The supplied test separately makes that post-check fail and verifies its persisted receipt (test :2071-2084; log :242-244).

A distinct root probe verified analysis v1, then changed the analysis bytes and the current manifest consistently to v2 within the same fake main invocation:

~~~text
analysis_problems("main") before: []
post_phase_problems("main") after: []
drift receipts: []
tracked paths with unrelated inputs removed:
  STAGE1B-PLAN.sha256
  stage1b-input-freeze.sha256
  runner-tier3-v3.sha256.tsv
~~~

The analysis manifest and code were absent from the phase snapshot. Details and the correction are R41-1.

### 3.3 Smoke evidence

The accepted predicate baseline is the archived U-w08 epoch-3 decision at simTime 9000, with stability objectives removed from both diagnostics and remaining level indices reindexed. V4 reports no evidence problems. This is a CF-shaped normalization fixture, not a production CF trajectory.

Appending complete omission objects with counts -1 and +1 leaves their aggregate unchanged. V3 decision_evidence returns []; v4 reports generation.omissions[0].count is not a non-negative integer. Independent probes also varied a negative evaluatedCandidatePathCount, boolean retainedCandidateCount and exogenous amount below its contract: v3 accepted; v4 rejected. The exact checks are comparator :1423-1458 and frozen verifier F/actual_fleetpy_medium_verify.py:228-347.

## 4. Supplied log and new controls against v3

I independently counted H/selftest-2026-10-13-v4.log: **290 OK, 0 BAD, 2 LIMIT**. Header :2-9 matches the reviewed file hashes; summary :308 matches those counts. The two limits are the accepted middle-decision digest case and the format-only checkpoint binding case. The v4 target was not rerun wholesale; its controls were inspected and the material repairs independently probed.

No separate new-controls-on-v3 log was supplied in H/. To complete the requested check, I imported the unchanged v4 test file and executed:

~~~python
with contextlib.redirect_stdout(io.StringIO()):
    result = test_module.main(["--target", "v3"])
~~~

No output filename was passed. Test :2467-2469 writes only if that optional argument exists; all driver simulations use fake paths/writers/jobs (e.g. :2008-2045). The run completed in **508 seconds**, returned **1**, and reported **17 OK, 63 BAD, 1 LIMIT**. These BAD results are expected reproductions of the old defects.

| New control group | Supplied v4 target | Root v3-target reproduction |
|---|---|---|
| R38-1 report receipts | 24 OK, 1 LIMIT | 3 OK, 20 BAD, 1 LIMIT |
| R38-2 persistence/cleanup | 12 OK | 5 OK, 7 BAD |
| R38-3 admission | 4 OK | 1 OK, 3 BAD |
| R38-4 nested evidence | 20 OK | 4 OK, 16 BAD |
| R38-5 resolved paths/imports | 8 OK | 3 OK, 4 BAD |
| R38-T tool/environment scope | 13 OK | 1 OK, 4 BAD |
| R38-A analysis gate | 7 OK | 4 BAD |
| R38-P plan wording | 5 OK | 5 BAD |

Totals differ because the test skips some v4-only calibration/feature-specific checks when their new functions are absent on v3. This is visible in test :2376-2413 and version-specific branches; it is not evidence of unreported v3 passes.

Examples show failure for the intended reason:

- V3 returns pair PASS for wrong report semanticHash/manifestHash and false receipt variants with fresh bundle receipts; v4 log :215-227 rejects them. Consistent aggregate-hash negatives ensure the manifest/publication checks are not masked by a stale aggregate receipt.
- V3 startup drift has no receipt; worker errors show only one freeze check and skip post-verification. V4 log :239-248 persists/checks them.
- V3 reserves 410 MiB after STOP, failure or drift latch appears during the scan. V4 log :251-254 reserves zero for the negatives.
- V3 accepts negative nested counters while the frozen verifier rejects them. V4 log :255-274 agrees with the verifier.
- V3 accepts parent traversal/unreviewed imports; v4 log :275-281 rejects.
- V3 has only git, lacks the CreateProcess resolver and analysis gate, and has old plan text. Those feature/adoption controls appropriately fail; they are not protocol-validity evidence.

The pure suite verifies its enumerated expectations. It does not cover the consistent analysis-manifest replacement, per-run outcome conservation, strict repeat types, or wrong-but-consistently-frozen taskkill location identified below.

## 5. Remaining findings, ranked

### R41-1 - P2: the initial main-analysis identity is not retained

**Locations:** H/run_stage1b-v4.py:813-855,922-928,1058-1065,1188-1200.

The new gate checks the current analysis manifest against the current files. It does not bind the manifest digest at first main start, and frozen_paths includes neither that manifest nor its listed code. The post-phase check rereads the same mutable manifest.

**Root reproduction:** Use a one-file analysis manifest for analysis-v1, verify it before main, then change the file to analysis-v2 and update its manifest hash consistently. The actual analysis checker still returns []; actual post_phase_problems("main") returns []; no drift writer is called. The three remaining snapshot paths in the isolated probe are the plan seal, general input freeze and runner manifest. This is a same-invocation observation, not merely a historical resealing scenario.

A hash list checking itself against current files proves current consistency; it does not retain the analysis selected before main results became available. The plan promises a frozen analysis and no retuning after results (H/STAGE1B-PLAN-DRAFT-v4.md:220-225,265-267). The test covers code changing while its manifest stays fixed (:2398-2400), but not code and manifest changing together.

**Required correction:** At the first main admission, bind the reviewed analysis manifest digest and the expected inventory in an immutable amendment/run receipt. Verify that original identity on resume, during main admission and after main. Include the analysis manifest and listed files in the phase snapshot; compare the post-phase manifest with the phase's starting identity, so a restamp after the final job is detected too. Retain the existing ordinary-edit/stat limitation honestly. The scripts may still be supplied after the initial seal, before main; this does not demand another simulation or an earlier publication.

The manifest also accepts any nonempty file list rather than requiring the promised extractor/report/dependencies. Manual inventory review must establish coverage before first main admission; the mechanical check should retain that reviewed inventory.

### R41-2 - P2: per-run report checks accept impossible outcome composition

**Locations:** H/compare_equivalence_stage1b-v4.py:567-574,972-975; smoke consumes facts at :1589-1594.

Accepted/rejected lists are checked only for sorted unique nonempty strings, not disjointness, conserved size or agreement with available action counts. U-w08 has 80 accepted, 28 rejected and 108 arrived requests. Replacing either semantic list with [] and updating semanticHash/summary receipts consistently produces no report problems. A full rebuilt-bundle probe with acceptedRequestIds=[] gives facts.problems=[].

The pair does correctly reject that changed list through runSemantic. **This is a per-run integrity gap used by smoke, not a demonstrated Gate-0 behavioural mismatch passing all eleven components.** No complete synthetic ON smoke was claimed to pass.

The frozen verifier already requires available conservation checks (F/actual_fleetpy_medium_verify.py:1180-1205); the producer checks disjoint outcomes covering all requests before storing them (:642-645,666-667 in F/actual_fleetpy_medium_preflight.py).

**Required correction:** Collect protocol accepted/rejected counts and enforce corresponding semantic list sizes, disjointness and union size equal to requestCount, with the available lifecycle conservation checks. Semantic IDs are FleetPy req-... values while transcript actions use rq-... protocol IDs. Do not invent raw set equality across those namespaces. Add empty/overlapping-list negatives with consistently refreshed receipts and valid archived positives.

### R41-3 - P3: boolean repeat fields pass as integers

**Location:** H/compare_equivalence_stage1b-v4.py:543-546; correct helper _same_int at :518-520.

A root rebuilt-bundle probe sets run-00.repeat=false, summary.runs[0].repeat=false and summary.repeatCount=true. Facts has no problems, and an archived identical-copy pair passes all eleven components. Python equality makes false equal to 0 and true equal to 1; those fields are outside the compared behavioral components.

This is malformed receipt acceptance, with unchanged service behavior. Use _same_int for all three checks and include a boolean negative alongside the valid numeric positive.

### R41-4 - P3: the taskkill exception does not enforce the declared System32 path

**Locations:** H/run_stage1b-v4.py:175-179,656-679,1098-1105; plan :263; fix report :48.

The freeze now binds taskkill's path/hash and verifies job/driver resolution. However, exemption is by tool name: tool_problems skips root containment for any taskkill path, and write_freeze does likewise. Neither requires the System32 executable declared by the plan/fix report.

**Root probe:** Freeze git at E:/frozen/git/git.exe and taskkill at E:/outside/taskkill.exe with consistent SHA values; make both resolver contexts return those same paths. tool_problems returns []. This demonstrates an exception-policy mismatch, not evidence that the current real tool is wrong.

**Required correction:** Require the declared system executable path and its frozen hash, or explicitly review and document another precisely scoped path. Preserve the exception's honest OS-component limit; there is no need to freeze the entire operating system.

The main search order in :442-459 agrees with Microsoft's [CreateProcessW documentation](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw): for an extensionless bare command, application directory and parent current directory precede system/Windows directories and PATH; .exe is appended. The code uses SYSTEMROOT for Windows-directory paths rather than native directory queries, so it remains a model under the current environment assumptions. No actual resolver mismatch was demonstrated. The name-only exception above is the concrete defect.

### R41-5 - P3: the v4 plan and provenance instructions identify different artifacts

**Locations:** H/STAGE1B-PLAN-DRAFT-v4.md:1-7,70,102,106,129-130,170,271-275; H/RUNNER-PROVENANCE-TEMPLATE-v4.md:1-5,14,42,67,70; driver :126,200-204.

The v4 plan still calls itself draft v3, cites the R28 fix report, and points several execution/verification references to the v3 driver/comparator/log. It instructs a v3 provenance copy at :102 but lists RUNNER-PROVENANCE-v4.md in the seal at :273. The actual v4 driver and SEALED_REQUIRED expect RUNNER-PROVENANCE-v3.md.

The v4 template is a byte-copy of v3 and asks for the SHA values of run_stage1b-v3.py and compare_equivalence_stage1b-v3.py at :70. That conflicts with the fix report's statement that it was updated for v4 (H/HARNESS-FIX-REPORT-R38.md:20). Following the v4 plan's seal list literally leaves the driver's required receipt uncovered; following the template records old harness identities.

**Required correction:** Choose a single receipt filename consistently and update its content to the reviewed v4 harness identities. Runner build v3 is a valid independent naming choice; renaming the runner is unnecessary. Update all plan/template execution references and the plan's version/history, while preserving old files. Regenerate documentation-presence controls to check those actual identities rather than only phrases.

## 6. Pre-seal facts and timing

The newer owner record does supersede R38's weaker two-week information. D/DEBATE-LEDGER.md:493-497 records a deadline after 2026-11-03, with no exact date, and conditional permission for the cost-first worktree commit and runner v3 publication, **no push**, after readiness. The plan records that decision and an A1 milestone assertion (H/STAGE1B-PLAN-DRAFT-v4.md:32-34). Attach the milestone's actual record/source to the sealed facts; this review does not certify its specific timestamp from a text-presence test.

Correct the calculation at plan :35. Date subtraction gives:

~~~text
2026-10-14 -> 2026-11-03: 20 days
2026-10-14 -> 2026-11-04: 21 days
2026-10-15 -> 2026-11-04: 20 days
~~~

Interpreting "after November 3" as a deadline date of November 4 or later establishes a conservative 21-calendar-day lower bound on October 14, not necessarily more than 21 days. It does not establish the three-week rule for a later launch. Before starting, record the intended launch and confirmed deadline/lower bound using the agreed date/time convention; if the conservative bound is below 21 days, obtain a stronger deadline fact or do not start. No amendment to the rule is inferred here. The test at :2424-2425 checks text presence, not this arithmetic.

The settled fresh Windows PowerShell environment with GIT_* unset is both documented (:260-263) and checked by forbidden_env (:430-439), with steering values/absences frozen. This part is fixed. The same recorded environment is required across freeze/run/verdict commands; fresh-shell wording alone does not replace byte/environment verification.

The analysis gate is appropriately stricter than the older plan: no main job may start before the manifest exists and verifies. Missing scripts therefore remain a future main-phase prerequisite, not an automatic reason to execute or a demand that they exist before the first Gate-0/smoke-only seal. Close R41-1 and manually review the complete analysis inventory before main. Align plan :220-223 with :265-267 so the execution timing is unambiguous.

Read-only checks still found no runner-tier3-v3 tree, tier3-stage1b-v1 output root, filled final plan/provenance, general input freeze, seal or analysis freeze. Those future publication/sealing artifacts are prerequisites, not evidence that a completed study failed. This review authorizes none of those mutations.

## 7. Required closure

Before sealing, close R41-2/3 and align R41-4/5 plus the launch facts. Establish the analysis-identity mechanism of R41-1 and its required amendment/receipt before any main launch. Add focused negative/positive controls for the new gaps; retain the verified original fixes and earlier versions.

The 4 OFF / 2 smoke / 68 main design, configuration bindings, primary interaction identity, composition/guard interpretation, exploratory limitations and Stage-2 conditions remain in the plan. No configuration change, .NET replay or expanded simulation panel is requested.

**NOT READY** reflects the remaining P2 integrity/freeze gaps, not the accepted behavioural criterion or the two disclosed test limits. Nothing in this report certifies publication, a Gate-0 pass, smoke success or empirical Stage-1b results.
