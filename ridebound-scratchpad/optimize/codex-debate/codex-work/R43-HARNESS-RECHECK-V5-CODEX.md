# Round 43 - Stage 1b harness v5 recheck (Codex, 2026-10-14)

**Verdict: NOT READY.** V5 repairs R41-2 through R41-5 and much of R41-1. The remaining P2 blocker is recovery when main results exist but no job log has yet anchored the original analysis binding. The supplied full-suite log also records a different driver hash from the driver delivered for review. A smaller lifecycle-multiplicity check should be corrected cheaply.

The owner-authorized behavioural Gate 0 and the two accepted test limits are retained. This review does not request .NET replay, a different experiment panel or production algorithm changes.

## 1. Scope and snapshot

Aliases:

- H/ = E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/
- D/ = E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/
- F/ = E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/
- A/ = C:/RideBoundData/research/tier3-t38-v1/

I read D/ROUND43-HARNESS-RECHECK-V5.md and began with H/HARNESS-FIX-REPORT-R41.md. Two independent sub-agents reviewed driver/binding and comparator changes. I checked their source and independently reproduced the material findings, including actual driver main/run_job paths with every worker, process and writer replaced by in-memory objects.

All executable probes used Python -B, archived bytes or in-memory state. The v4-target pure self-test was run with no output-log argument; the current v5 section-E controls were run separately, also without a file writer. No job, .NET execution, build, publish, commit, freeze, seal or harness edit occurred. This exclusively created report is the sole new filesystem output.

Current reviewed SHA-256 values:

| H/ file | SHA-256 |
|---|---|
| compare_equivalence_stage1b-v5.py | 690d1262e7a8b6f1f75a1c03b4d220c8866c4d22a37d24f9c32d4e16a2a80cd3 |
| run_stage1b-v5.py | 7d133819e0bea696d45e5a34a6f91f1569dac512d80935aae74d007503b85b76 |
| test_compare_equivalence_stage1b-v5.py | 7735deee68eb06d5cfc36cf56b5b8d320e789e5357edd40212cbf4f83db72132 |
| STAGE1B-PLAN-DRAFT-v5.md | b3458932a57715ba8a373b62f43e42ab5e3051e4f46591782dbf1b6847e5b761 |
| RUNNER-PROVENANCE-TEMPLATE-v5.md | 695f3c646f0881cce25da24e8b63d3c241b92bae476152d5273dc71cd3d92139 |
| HARNESS-FIX-REPORT-R41.md | e7a8dec3e2eb5b18acf545ed5fa3311bab394e5fc8b0cc866fe1a07ce4678427 |
| selftest-2026-10-14-v5.log | fa14a35581a93ab37e9e8172a6166e1340de3a1abcc9ee51e4a7503534c1feb5 |

The brief SHA-256 is d19b2dd829daa1b91722fb82250f947b14027f85802f5426773b8a5cde357266. The driver's current hash was already 7d133819... when this review began; the mismatch described below was not created by our probes.

## 2. R41-1 through R41-5

| Finding | Disposition | Evidence and qualification |
|---|---|---|
| R41-1 - retain initial analysis identity, review its inventory | **PARTLY** | Initial binding is exclusively created (H/run_stage1b-v5.py:897-911), its hash is held during main (:1350-1355), and main snapshots include manifest, binding and bound files (:981-991,1065-1073). The amendment must be listed and record reviewer/coverage (:844-890). Current-manifest restamping against an unchanged binding fails; a changed binding fails against the held hash or an existing log anchor (:926-965). The gap is results existing without a log anchor on process recovery (R43-1). |
| R41-2 - semantic outcome conservation | **FIXED for the requested defects** | Protocol outcomes are collected at H/compare_equivalence_stage1b-v5.py:955-973 and supplied to report validation at :1043-1045. outcome_problems :538-575 validates protocol accepted/rejected/arrived uniqueness, disjointness and coverage; semantic sizes, disjointness and requestCount coverage; and lifecycle sets/cancellation/initial-publication count. Empty, overlapping, swapped and transferred semantic outcomes reject on v5 while they pass v4. The separate lifecycle duplicate issue is R43-3. |
| R41-3 - repeat fields must be integers | **FIXED** | _same_int excludes booleans (:529-531) and is applied to run-00.repeat, summary.runs[0].repeat and summary.repeatCount (:599-603). Root probes tested each boolean separately; v4 accepts, v5 rejects. |
| R41-4 - System32 taskkill exception | **FIXED** | tool_location_problems compares the resolved path with the declared exception (:701-710); tool_problems also verifies the frozen hash (:676-698), and write_freeze calls the same location check (:1244-1252). Root wrong-but-consistent outside path rejects v5 and passes v4; the declared System32 path/hash passes v5. |
| R41-5 - version/receipt identities, arithmetic and A1 evidence | **FIXED in the plan/template** | V5 names its actual driver/comparator/test/log (plan :1-11,153-154,282-284), uses the runner-v3 receipt consistently (:124-127,323-332), and the v5 template records v5 harness identities (:1-12,75). Calendar-day convention and 21/20-day calculation are explicit (:47-54). Milestone paths/fingerprints are supplied (:40-45) and match the actual files (section 5 below). The full-suite driver's mismatched hash is a distinct evidence issue, R43-2. |

The supplied v5 section-E results are H/selftest-2026-10-14-v5.log:309-336. They cover the intended original counterexamples, but the analysis recovery cases include a log anchor; none tests output with no log. The driver-hash mismatch limits use of that log as a receipt for the current driver.

## 3. Remaining findings, ranked

### R43-1 - P2: a restart can adopt a changed analysis after results exist but before any log anchor exists

**Locations:** H/run_stage1b-v5.py:914-923,926-978,1169-1200,1338-1355; H/STAGE1B-PLAN-DRAFT-v5.md:317-321,348-350.

The binding protects an invocation through the held SHA and protects recovery through existing job logs. However, run_job waits for the child process to finish at :1192-1194 and only then exclusively creates the log/anchor at :1195-1198. Output can exist throughout the run and after successful child completion without any anchor if the driver exits or log creation fails. The producer itself creates the output directory at F/actual_fleetpy_medium_preflight.py:848 and writes run/summary results before return (:723,905).

On a fresh invocation ANALYSIS_BINDING_SHA starts as None. If the binding exists, analysis_problems checks it without considering output evidence (:973-974). Existing output without a log supplies no old binding identity to main_log_problems. The new invocation subsequently captures the current binding's hash (:1354).

**Root reproduction, entirely in memory:**

1. Make a valid analysis-v1 manifest, amendment and binding; retain its original hash.
2. Simulate an existing main output and no log.
3. Consistently replace code, manifest and binding with analysis-v2.
4. Call the actual main() through the test's fake-world harness with main_started=True and logs={}.
5. Compare with the same world containing a log anchored to the original hash.

~~~text
output exists, no log:
  return 3; exception None; drift receipt none
  (3 is the deferred fake-job return; analysis admission succeeded)

output exists, original binding log exists:
  SystemExit; INPUT-DRIFT-STOP.txt written

held original hash in the same invocation:
  stage1b-analysis-binding.txt changed during this invocation
~~~

The latter two controls show that the new checks work; the first isolates their recovery boundary. This probe uses actual driver main logic with unrelated input/verdict checks stubbed valid, as the supplied analysis controls do (H/test_compare_equivalence_stage1b-v5.py:2526-2564).

A second root probe called actual run_job with a fake child returning zero after marking output produced, then made exclusive log creation raise OSError:

~~~text
OSError: exclusive log write failed after child completion
output=True, log=False
events: output-produced, reservation-released
~~~

No file or process was created. The control-flow ordering makes the state reachable. A process interruption before finish_phase also loses the in-memory held hash.

The plan's stated limitation at :348-350 says there is no main output before the first log. That reason is false for this implementation. A harmless pre-result rewrite limit cannot be extended to a window with observable main results. This remains R41-1's recovery-identity requirement, rather than a request to remove the accepted middle-decision or adapter-state limits.

**Required correction:** Exclusively create and flush/close an admission receipt or log header containing the binding SHA before launching each child. If this anchor cannot be written, do not launch. Recovery must refuse/persist loss for any main output lacking its admission anchor, and compare the current binding with the recorded admission identity before accepting it. Preserve the same-invocation held-hash and snapshot checks. Add the output-without-log/restart control and correct the plan's limitation explanation.

### R43-2 - P2: the full-suite log does not bind the driver delivered for review

**Locations:** H/selftest-2026-10-14-v5.log:3,337-338; H/HARNESS-FIX-REPORT-R41.md:63-69.

The log reports:

~~~text
tested run_stage1b-v5.py:
449c1d630b474c2c55e8d5c6c6f1d36a14d6b50085ae4f3f7e43346a67f5edb6
~~~

The current file's independently measured SHA-256 is:

~~~text
7d133819e0bea696d45e5a34a6f91f1569dac512d80935aae74d007503b85b76
~~~

Six of the seven tested-file header hashes match current bytes: comparator, plan, template, test, canonical helper and ON WP4. Only the driver differs. Normal LF/CRLF, final-newline and UTF-8 BOM transformations of the current driver did not reproduce the logged hash. The 449c1d63... source snapshot was not supplied, so I cannot characterize its difference or infer that it was merely a comment edit.

The reported 317 OK / 0 BAD / 2 LIMIT remains evidence about the recorded tested snapshot. It does not establish that the entire suite passed on the current driver, and should not be sealed as that receipt.

**Required correction:** After closing R43-1, preserve the old log and generate a new pure-test receipt against the exact final code bytes. Its tested-file header must match the files to be sealed. Do not repair the old log by changing its header, or call the mismatch a proven benign difference without the tested source. The independent current-code section-E run below checks the new finding controls, but does not retroactively certify the whole old full-suite run.

### R43-3 - P3: lifecycle multiplicity is lost before conservation checking

**Locations:** H/compare_equivalence_stage1b-v5.py:547-557; F/actual_fleetpy_medium_verify.py:1164-1178.

Accepted, rejected and arrived IDs are checked for uniqueness. Booking, boarding and alighting lists are immediately converted to sets, so repeated lifecycle evidence is silently collapsed.

**Root predicate probe:** Reconstruct the valid U-w08 outcomes. Append the first ID again separately to bookingConfirmed, passengerBoarded or passengerAlighted. outcome_problems returns [] in all three cases; the frozen verifier's unique-string helper rejects each.

**Root archived-bundle probe:** In U-w08 transcript frame 11, the adapter eventBatch at simTime 9000, append an identical copy of its bookingConfirmed event (eventSeq 21). Canonically regenerate frame bytes/base64/length/SHA and the transcript bundle receipt. Full v5 facts returns problems=[] with 2,020 frames.

The frozen verifier explicitly requires unique IDs for those lifecycle lists. Requiring the same unique nonempty string validation before converting them to sets is a small correction; add a duplicate-lifecycle negative.

This is a per-run integrity issue. Exact Gate-0 frame comparison still detects the changed event content. The probe uses an archived OFF bundle, and does not claim a complete ON smoke passed or a different service trajectory escaped behavioural equality.

## 4. Independent fixes and calibration

### 4.1 Outcomes and repeat types

I decoded actual archived tapes into manifest identity, publication projections, event/action outcomes, decision count, final event sequence/time and fleet size, then ran the actual current v5 report_problems.

| A/ archived run | V5 report/outcome problems |
|---|---:|
| U-d20181116-s10-r1-w08 | 0 |
| U-d20181116-s10-r1-w17 | 0 |
| C-30-d20181116-s10-r1-w08 | 0 |
| C-30-d20181116-s10-r1-w17 | 0 |
| Mplus-30-d20181114-s10-r3-w07 | 0 |

The U-w08 baseline has 80 accepted, 28 rejected and 108 arrived requests. Root variants replaced either semantic outcome list with [], recalculated semanticHash and synchronized both summary receipts. V4 returns no problems; v5 reports the wrong protocol size and requestCount coverage. Independent overlap, swapped-list and one-transfer controls also reject v5 while passing v4.

Each repeat field was tested separately: run-00.repeat=false, runs[0].repeat=false and repeatCount=true. V4 accepts; v5 rejects through _same_int. An independent float repeat=0.0 control also rejects v5. The provided combined-boolean pair negative is log :325-326.

Semantic req-... IDs remain compared with protocol rq-... IDs by counts, not invented raw member equality. The new protocol collection and dispatch are comparator :955-973,1043-1045. This preserves the namespace distinction identified in R41.

### 4.2 Analysis binding and tool scope

The original R41 same-invocation manifest/code restamp is detected through the retained binding; consistently changing the binding too is detected against the held SHA. After a log is written, its original binding SHA rejects a changed current binding on resume. Amendment presence/reviewer/coverage and snapshot inventory are checked by driver :844-890,981-991,1065-1073; supplied controls :309-316 exercise those repairs.

The missing-log recovery case is the uncovered boundary described above, not failure of these controls.

For taskkill, root supplied consistent frozen/resolved paths and SHA values in both contexts:

~~~text
E:/outside/taskkill.exe:
  v4: []
  v5: explicit declared-only-System32 rejection

C:/Windows/System32/taskkill.exe:
  v5: []
~~~

The freeze writer calls the same tool_location_problems helper at driver :1252. No OS tool was executed.

## 5. Plan, provenance and milestones

Operational identities are aligned: v5 plan/header/commands, v5 template, v5 code and test names, and one RUNNER-PROVENANCE-v3.md receipt identifying the runner build rather than the harness version. The seal list is explicitly enumerated (plan :323-332), with analysis artifacts created later under section 12. The template records the actual v5 harness files (:75) and preserves the owner's no-push scope (:37). Old publish-command reconstruction remains labelled an inference (:99-112).

The milestone fingerprints in plan :40-45 match current files:

| D/codex-work/ source | Full measured SHA-256 |
|---|---|
| r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex | b2978f741056f3ee2e1e92a3671cd51404492374d2bfd100796417ded746306b |
| r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex | 5d4ac193aa47e7205e6d645303a68b601f702ad807d0624dc527d4a1766102c1 |

That confirms draft existence/bytes, not an independently certified milestone judgement. The plan now states that distinction explicitly.

The calendar convention is corrected (plan :47-54): November 4 minus October 14 is 21 days; minus October 15 is 20 days; November 3 minus October 14 is 20 days. The exact deadline was not supplied. Record the actual intended launch and exact deadline or a stronger conservative bound before starting; fewer than 21 days means no Stage 1b unless a genuine owner amendment is recorded. This review infers no amendment or launch authorization.

The owner-authorized behavioural Gate 0, exploratory results, historical-software limitation and format-only adapter binding are accurately retained (plan :103-108,133-142,334-360). The two accepted LIMITs remain accepted. The additional analysis explanation at :348-350 needs the concrete correction in R43-1.

## 6. Self-test evidence, including actual current v5 controls

I counted the supplied log's raw ASCII status lines: **317 OK, 0 BAD, 2 LIMIT**; summary and exit are :337-338. The single non-ASCII byte is 0x97 in the template-title preview at :333, so the file is not valid UTF-8. Counting status/header lines does not depend on that presentation byte; the original bytes and hash were preserved.

Supplied section-E counts:

| Group | Supplied v5 log | Root v4-target reproduction |
|---|---|---|
| R41-1 analysis binding | 8 OK | 1 OK, 7 BAD |
| R41-2 outcome conservation | 7 OK | 1 OK, 5 BAD |
| R41-3 strict repeat types | 2 OK | 2 BAD |
| R41-4 taskkill location | 3 OK | 1 OK, 2 BAD |
| R41-5 documentation/facts | 7 OK | 1 OK, 6 BAD |
| **Total** | **27 OK** | **4 OK, 22 BAD** |

The pure v4-target run used the actual v5 test file main(["--target", "v4"]), with stdout captured in memory and no output filename. It returned 1 after **165 seconds**. BAD means the expected repair did not exist in v4, not that a new v5 regression was observed.

The v4 total is 26 rather than 27 because the five-run outcome calibration is v5-only. The old outcome-size/boolean/wrong-taskkill controls fail for the original reasons; analysis controls show v4 neither retaining the binding nor requiring the review amendment. Documentation controls find actual old receipt/version mismatches. Their seal-list comparison also flags unexpanded v4 shorthand; this is a documentation check, not proof that those physical files were absent.

Because the supplied log's driver hash is stale, I additionally ran only section E against the **current** v5 driver/comparator/test bytes, with the normal archived context and all driver effects mocked as in the test file:

~~~python
T = test_module.targets("v5")
c = test_module.Ctx(T)
for part in (
    test_module.r41_1, test_module.r41_2_3,
    test_module.r41_4, test_module.r41_5,
):
    part(c)
~~~

The current-code run finished in **239 seconds** with **27 OK, 0 BAD, 0 LIMIT**: R41-1 8 OK, R41-2 7 OK, R41-3 2 OK, R41-4 3 OK and R41-5 7 OK. Its driver hash was 7d133819e0bea696d45e5a34a6f91f1569dac512d80935aae74d007503b85b76, with the comparator/test hashes matching the reviewed table. No BAD result occurred.

This checks the original R41 control expectations against the delivered code. It does not cover R43-1's results-without-log recovery case or R43-3's duplicate lifecycle case, and does not replace a full-suite receipt for the final repaired driver. Section-E implementations are H/test_compare_equivalence_stage1b-v5.py:2574-2786; optional file output exists only at :2823-2825 and was not invoked.

## 7. Closure before sealing

Close R43-1 with a pre-launch durable analysis anchor and recovery checks, then produce a matching final-code test receipt for R43-2. Correct the inexpensive lifecycle uniqueness check in R43-3. Preserve existing versions/reports/logs; do not edit historical hashes to make them agree.

Complete the actual publication/provenance/freeze/seal artifacts and launch-date/deadline facts only at their authorized stage. The analysis inventory and amendment still need real manual coverage review before main. No extra .NET replay or FleetPy trajectory is requested.

**NOT READY** is based on the remaining analysis-recovery and test-receipt gaps. The repaired R41 semantic/type/tool/documentation controls are credited, and the accepted behavioural criterion is not reopened. No publication, Gate-0 pass, smoke success or empirical Stage-1b result is certified here.
