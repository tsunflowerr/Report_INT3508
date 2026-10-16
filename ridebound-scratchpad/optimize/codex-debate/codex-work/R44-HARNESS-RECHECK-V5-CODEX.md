# Round 44 - Stage 1b harness v5 convergence recheck (Codex, 2026-10-14)

**Verdict: NOT READY. One concrete P2 remains: R44-1, the R41-1/R43-1 analysis-recovery gap.**

A restart can accept a coherently replaced analysis after main results exist without a binding log. This permits analysis chosen after observing results and can change a reported scientific metric. The known-limitations entry gives a false reason for accepting that window.

R41-2 through R41-5 are FIXED for their original counterexamples. The two accepted LIMITs remain accepted. The newly supplied tested-driver snapshot explains the old self-test hash discrepancy as one diagnostic-string correction; it is no longer a P2 blocker. Lifecycle multiplicity is a separate optional P3 item, without a demonstrated complete Gate-0 or smoke bypass.

## Scope, identities and convergence rule

Aliases used in file:line citations:

- H/ = E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/
- D/ = E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/
- F/ = E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/
- A/ = C:/RideBoundData/research/tier3-t38-v1/

I read D/ROUND44-HARNESS-RECHECK-V5.md, the fix report, current v5 sources/documents, both supplied logs, the dry run, and the retained tested-driver snapshot. The convergence rule is recorded at D/DEBATE-LEDGER.md:597-600,668-670. This verdict uses its scientific-result criterion for the single P2; optional hardening and the accepted N1/R38-1 limits do not cause NOT READY.

Two independent sub-agents examined the driver recovery path and the comparator/log evidence. I checked their material conclusions against current source and independently reproduced the counterexample, its positive controls, the source-snapshot difference and the report predicates. Probes used Python -B, archived bytes, and in-memory objects. Every process launch and writer in driver probes was replaced or was unreachable because synthetic outputs were already complete. No simulation, .NET execution, build, publish, commit, freeze, seal or harness edit occurred. This exclusive-create report is the only new filesystem output.

The v5 code, test, plan, template, fix report and full-suite log have the same bytes as in R43. Current SHA-256 values:

| H/ file | SHA-256 |
|---|---|
| compare_equivalence_stage1b-v5.py | 690d1262e7a8b6f1f75a1c03b4d220c8866c4d22a37d24f9c32d4e16a2a80cd3 |
| run_stage1b-v5.py | 7d133819e0bea696d45e5a34a6f91f1569dac512d80935aae74d007503b85b76 |
| test_compare_equivalence_stage1b-v5.py | 7735deee68eb06d5cfc36cf56b5b8d320e789e5357edd40212cbf4f83db72132 |
| STAGE1B-PLAN-DRAFT-v5.md | b3458932a57715ba8a373b62f43e42ab5e3051e4f46591782dbf1b6847e5b761 |
| RUNNER-PROVENANCE-TEMPLATE-v5.md | 695f3c646f0881cce25da24e8b63d3c241b92bae476152d5273dc71cd3d92139 |
| HARNESS-FIX-REPORT-R41.md | e7a8dec3e2eb5b18acf545ed5fa3311bab394e5fc8b0cc866fe1a07ce4678427 |
| selftest-2026-10-14-v5.log | fa14a35581a93ab37e9e8172a6166e1340de3a1abcc9ee51e4a7503534c1feb5 |
| run_stage1b-v5-devlog-snapshot.txt | 449c1d630b474c2c55e8d5c6c6f1d36a14d6b50085ae4f3f7e43346a67f5edb6 |
| selftest-2026-10-14-r41-on-v4.log | 82c84fe4970728670148df8984f4cb744ab63112fa60f93adab3f959e29d418b |
| plan-dryrun-2026-10-14-v5.txt | 51320b5b56484f7199fb1a25bdaae96c3f362e7fe94a5223cb6d5fb8590f5728 |

The brief SHA-256 is e91b8f9ef7689533c3d69331c0b669827b476c977f197f1df59a265aa6e2e912.

## R41 item dispositions

| R41 item | Disposition | Evidence and probe result |
|---|---|---|
| R41-1: retain initial analysis identity and reviewed inventory | **NOT FIXED in full** | Substantial repair is credited: exclusive initial binding H/run_stage1b-v5.py:897-911; retained invocation SHA :894,1350-1355; manifest/file/log verification :914-965; amendment reviewer and coverage :844-890; main snapshot :981-991,1065-1073. All eight supplied R41-1 controls pass current v5 in the fresh R44 run. Output-without-log recovery remains unprotected, demonstrated in R44-1 below. |
| R41-2: impossible semantic outcome composition | **FIXED for the original counterexamples** | H/compare_equivalence_stage1b-v5.py:538-575 checks protocol uniqueness/disjointness/coverage and semantic sizes/disjointness/requestCount. Collection and actual per-run dispatch are :955-973,1043-1045. Root's consistently restamped empty accepted or rejected lists pass v4 and reject v5. Five actual archived report calibrations pass v5. Lifecycle multiplicity is the separate P3 qualification below. |
| R41-3: boolean repeat metadata | **FIXED** | _same_int excludes bool at H/compare_equivalence_stage1b-v5.py:529-531; all three repeat fields use it at :599-603. Root changed run-00.repeat, summary.runs[0].repeat and summary.repeatCount separately. Each v4 report check accepts; each v5 report check rejects. |
| R41-4: exact System32 taskkill exception | **FIXED** | H/run_stage1b-v5.py:676-710 verifies both resolver contexts, frozen bytes and the resolved declared path. The freeze writer calls the same location predicate at :1244-1252. The three supplied current-code controls pass: a consistent E:/outside/taskkill.exe rejects, declared System32 accepts, and the writer helper applies the exception case-insensitively. No tool was executed and write_freeze was not invoked. |
| R41-5: version identities, receipt name, date arithmetic and A1 records | **FIXED** | Actual v5 identities are H/STAGE1B-PLAN-DRAFT-v5.md:1-11; the runner-v3 receipt name is consistently :124-127,323-332 and H/RUNNER-PROVENANCE-TEMPLATE-v5.md:1-12,75. Calendar calculations and launch consequence are plan :47-54. Draft-source fingerprints :40-45 match measured files. All seven supplied documentation controls pass current code. The explained historical log discrepancy is a nonblocking evidence note below. |

None of these original R41 items needs a DOCUMENTED (accepted P3) disposition instead of repair: the three original P3 defects were fixed. R41-1 cannot be reclassified as accepted P3 because its remaining path can alter the analysis after observable results.

## R44-1 - P2: output can precede the first analysis anchor, allowing changed analysis on restart

**Locations:** H/run_stage1b-v5.py:243-254,914-978,1001-1009,1169-1200,1338-1355; H/STAGE1B-PLAN-DRAFT-v5.md:15-16,317-321,348-350.

The only cross-invocation anchors for the analysis binding are existing main job logs. main_log_problems checks a log's first line only if that log exists (:914-923). The held binding SHA starts as None in a new process (:894,935). When a binding exists, analysis_problems goes directly to its current manifest/file/log checks, without using existing output evidence (:973-974).

run_job starts the child at :1192-1194 and opens the exclusive log only after that child returns (:1195-1198). The producer creates its output directory and writes report/summary bytes before returning: F/actual_fleetpy_medium_preflight.py:848,723,905-906. A driver interruption or exclusive-log failure can therefore leave informative or complete output with no old binding anchor.

The existing main output counts as started (:1001-1009), but that fact does not supply its original analysis identity. If the code, manifest and binding were rewritten consistently while the driver was stopped, the next invocation passes their current consistency checks and captures the new binding SHA at :1354.

### Reproducible in-memory counterexample

This is a recovery-identity probe of actual main logic, with unrelated publication/freeze/verdict checks stubbed valid in the same manner as the supplied controls. It does not claim that a production study has run or that an existing production extractor was changed.

After importing H/test_compare_equivalence_stage1b-v5.py as t (without executing its main), the minimal probe is:

~~~python
import types

T = t.targets("v5")
c = types.SimpleNamespace(
    T=T, new_id={"ok": True, "dll": "b" * 64, "tree": "t" * 64}
)
w = t.AnalysisWorld(b"def late60(s,t): return s-t\n")
old = w.write_binding()

# Existing main output, no main log: the original analysis admits.
print(t.describe_main(t.analysis_main(c, w, main_started=True, logs={})))

# Replace analysis after output is available and restamp all local receipts.
w.set_file("extract_stage1b.py", b"def late60(s,t): return 0\n")
w.restamp()
w.write_binding()
print(t.describe_main(t.analysis_main(c, w, main_started=True, logs={})))

# Positive detection control: retain one original log anchor.
job = T.s.jobs("main")[0][0]
print(t.describe_main(t.analysis_main(
    c, w, main_started=True,
    logs={job: "returncode=0 seconds=1 analysis-binding " + old}
)))
~~~

Both independent probes and root reproduction give:

~~~text
original binding + output + no log:
  return 3; exception None; drift receipt none

changed code + manifest + binding + output + no log:
  return 3; exception None; drift receipt none

same changed world + original binding log:
  SystemExit; INPUT-DRIFT-STOP.txt written
~~~

The first two return values are the deliberate deferred-worker result of the helper; they prove analysis admission, not simulated job completion. Helpers and their output evidence are H/test_compare_equivalence_stage1b-v5.py:2497-2564.

I strengthened the root probe by creating synthetic summary.json status-ok files for all 68 main outputs before startup, then calling actual run_job for each. The method returns immediately on nonpending output at driver :1170-1171, so no child, command or log writer is reached:

~~~text
changed analysis + all 68 completed outputs + no log:
  return 0; exception None; drift receipt none
  observed worker states: {'status-ok': 68}

same world + one original log anchor:
  SystemExit; drift receipt written

same invocation with held original binding SHA:
  ['stage1b-analysis-binding.txt changed during this invocation']
~~~

The completed-output construction is a synthetic missing-anchor state, not a claim that 68 children normally finish before any log. A single output already suffices for the smaller recovery counterexample. The old-log and held-SHA controls show that the existing guards work where an anchor is available.

I also exercised actual run_job with a fake child returning zero after producing an in-memory summary, then made open(log, "x") raise OSError:

~~~text
exclusive log write failed after child completion
output=True; log=False; state=status-ok
events=['output-produced', 'log-open-failed', 'reservation-released']
~~~

This establishes the reachable control-flow ordering without any process or file creation. A stopped invocation loses its held SHA; a post-phase check cannot preserve a held value across a later fresh process if there is no persisted anchor.

### Scientific consequence and the inaccurate limitation

For the same synthetic served=100 and timely=80 evidence, the two small extractor definitions above return late60=20 and late60=0. Both replacement bytes and receipts are accepted by the recovery path. This demonstrates the ability to change a reported scientific metric through analysis selected after results become available. It does not assert those invented extractor definitions are the real Stage-1b analysis.

The plan expressly keeps predictions so analysis cannot be tuned after the fact (:15-16). Its known limitation at :348-350 says the undetectable consistent rewrite is harmless because "no main output exists at that point." The child-before-log order disproves that premise. The harmless pre-output case may remain a documented P3 limit, but the actual output-present case meets the brief's P2 scientific-result definition.

**Required closure:** Exclusively create and durably flush/close a receipt or log header naming the admitted binding SHA before launching a main child. If that anchor cannot be created, do not launch. On recovery, any main output without a matching admission anchor must refuse and persist loss; compare the retained anchor with the current binding before adopting it. Preserve the invocation-held SHA, inventory review and stat checks. Add the missing-anchor restart negative and its old-anchor/unchanged positives, and correct plan :348-350. No extra simulation or .NET replay is needed to test this fix.

## Nonblocking findings and the R43 evidence correction

### R44-2 - P3, optional: lifecycle multiplicity collapses to sets

**Locations:** H/compare_equivalence_stage1b-v5.py:547-557; F/actual_fleetpy_medium_verify.py:1164-1178; H/STAGE1B-PLAN-DRAFT-v5.md:334-360.

The v5 check validates uniqueness for accepted, rejected and arrived protocol IDs, but immediately converts bookingConfirmed, passengerBoarded and passengerAlighted to sets. Root reconstructed the valid U-w08 outcomes and appended one existing ID to each lifecycle list in turn:

~~~text
duplicate bookingConfirmed: outcome_problems=[]
duplicate passengerBoarded: outcome_problems=[]
duplicate passengerAlighted: outcome_problems=[]
~~~

The frozen verifier requires unique strings for each list. Cheap hardening is to apply the same validation before set conversion and add these negatives. If retained under the convergence rule, list this precise set-based multiplicity limit and a reason in section 14; it is currently absent there.

This is not an independently demonstrated end-to-end P1/P2 finding. Changed lifecycle events remain in normalized frame content (:1019-1020), and exact frame comparison fails for different content (:1133-1150,1217). No complete SMOKE-PASSED control or different service trajectory passing Gate 0 was produced. I retain the prior P3 classification and do not use it to block the verdict.

### R44-3 - P3 evidence note: the supplied log used a driver with one older diagnostic string

**Locations:** H/selftest-2026-10-14-v5.log:3,337-338; H/run_stage1b-v5-devlog-snapshot.txt:857; H/run_stage1b-v5.py:857.

R43 could not characterize the stale driver hash because the tested source was missing. It is now supplied. Its measured SHA-256 equals the log's 449c1d63...f5edb6 identity exactly. The whole-source diff against current 7d133819...b85b76 consists of this sole change:

~~~text
tested snapshot, line 857:
  amendment before any main job starts; plan section 13)

current driver, line 857:
  amendment before any main job starts; plan v5 section 12)
~~~

Replacing precisely that diagnostic substring makes the complete snapshot text equal to the current source. This is neither whitespace nor a comment change; it changes only a refusal message when the analysis freeze is absent. No condition, action, accepted run or scientific computation changes. ASTs differ because the string constant differs, so I do not claim byte/AST identity.

This new evidence retires R43-2 as a P2 blocker under the convergence rule. The log is accurately evidence for its recorded tested snapshot, with the diagnostic-only difference disclosed; it is not a receipt for identical current-driver bytes. Preserve it and the tested snapshot. Record the correction in final provenance, or produce a new matching pure-test receipt after the required driver repair. A matching final-code receipt should accompany that repair; the old explained discrepancy alone does not make v5 NOT READY.

## Fix probes and supplied test evidence

I independently counted raw status prefixes in the supplied logs:

| Evidence | Result | Qualification |
|---|---|---|
| H/selftest-2026-10-14-v5.log:337-338 | 317 OK, 0 BAD, 2 LIMIT; exit=0 | Six tested-file entries match current bytes; the driver entry matches the retained snapshot, with its sole diagnostic correction verified. |
| H/selftest-2026-10-14-r41-on-v4.log:39 | 4 OK, 22 BAD, 0 LIMIT | Every tested-file header matches its current archived target; expected old-version repair failures. |
| Fresh R44 narrow current-v5 controls | 18 OK, 0 BAD, 0 LIMIT | Actual supplied r41_1 (8), r41_4 (3), r41_5 (7), using a minimal synthetic context. |
| Fresh R44 archived report calibration | 5 passes | Direct current report_problems with outcomes reconstructed from archived tapes. |
| Fresh R44 separate outcome/repeat negatives | 5 detections on v5, 5 acceptances on v4 | Two empty semantic lists with consistent refreshed receipts; three boolean fields changed individually. |

The seven tested-file header entries are log :2-8. The exact source diff explains the driver entry; I did not rerun the full suite in R44.

The self-test's v5 section E is :309-336, and the source controls are H/test_compare_equivalence_stage1b-v5.py:2574-2786. R43 independently ran all 27 section-E controls on the delivered 7d133819... driver with no BAD result (D/codex-work/R43-HARNESS-RECHECK-V5-CODEX.md:194-216); those same byte identities remain. R44 uses that retained evidence plus the fresh narrower probes; I did not rerun the 1,688-second full suite.

The newly supplied v4-target log records the original defects: restamped analysis admitted (:11-13), empty/overlapping/swapped/transferred outcomes accepted (:20-24), and boolean repeat metadata accepted (:27-28). R41-1-h at :18 is a TypeError from v4's old zero-argument frozen_paths signature, an interface mismatch; that individual BAD is not an additional scientific-result counterexample. V4 has 26 section-E cases because the new five-run outcome calibration applies only to v5.

Fresh direct archived report calibration:

| A/ archived run | Current v5 report/outcome problems |
|---|---:|
| U-d20181116-s10-r1-w08 | 0 |
| U-d20181116-s10-r1-w17 | 0 |
| C-30-d20181116-s10-r1-w08 | 0 |
| C-30-d20181116-s10-r1-w17 | 0 |
| Mplus-30-d20181114-s10-r3-w07 | 0 |

U-w08 has 80 accepted, 28 rejected and 108 arrived protocol requests. Empty accepted or rejected semantic lists, with regenerated semanticHash and synchronized summary receipts, give no v4 report problems but v5 size/coverage errors. Each individual boolean gives the appropriate v5 repeat/summary error. Semantic req-... and protocol rq-... IDs are correctly compared by size across their namespaces, without invented raw member equality.

The v5 log contains one non-UTF-8 byte, 0x97 in its template-title preview at :333. Raw hashes/status-prefix counts are unaffected; decoding that presentation line with cp1252 avoids pretending the log is valid UTF-8. This formatting detail does not demonstrate a gate or scientific-result failure.

## Known-limitations completeness and honesty

**The list is not completely honest/complete as written.** Both accepted LIMITs are accurately disclosed. The analysis entry gives a false safety premise, and the optional lifecycle multiplicity limit is absent.

| Section-14 item | Assessment |
|---|---|
| Middle-decision digests, plan :338-339 | **DOCUMENTED, accepted N1.** Owner-decided behavioural Gate 0 is explicit at :133-142,159-162. Link/content checks are not misrepresented as production .NET digest validation; protocol-invalid identical behaviour can pass. No replay request is reopened. |
| checkpointBindingHash, plan :340-341 | **DOCUMENTED, accepted R38-1.** Format and enclosing semantic receipt only, also :164-165. Comparator :632-634 describes precisely this coverage. It is distinct from recomputable Runner checkpointHash. No unavailable adapter-state preimage is invented. |
| Forced-objective activation, plan :342-344 | **DOCUMENTED.** Witness inference cannot prove unselected-candidate activation; unavailable production evidence is disclosed. |
| Stat checks, plan :345-347 | **DOCUMENTED.** Size/mtime checks do not authenticate running-job bytes; full phase checks remain. This accepted ordinary-edit limitation is not reopened. |
| Analysis before first log, plan :348-350 | **NOT FIXED / inaccurately justified.** Main output can exist before the first log; see the single P2 above. |
| Manual analysis coverage, plan :351-352 | **DOCUMENTED.** Review is a human prerequisite, with named coverage record retained; mechanical hashes do not certify completeness. |
| taskkill OS dependencies and resolver model, plan :353-356 | **DOCUMENTED.** Exact executable/path enforcement is fixed; out-of-scope OS loading and SYSTEMROOT model are disclosed. No actual resolver mismatch was reproduced. |
| Historical execution software, plan :357-358 | **DOCUMENTED.** Unverified archived baseline and exploratory interpretation are explicit also at :103-108. |
| Owner A1/deadline facts, plan :359-360 | **DOCUMENTED.** Draft byte evidence is distinguished from the owner's milestone judgement and the unknown exact deadline. |
| Lifecycle multiplicity | **Optional P3, not yet listed.** Describe the actual set-based limitation and reason if retained, or fix cheaply; no additional P2 verdict is based on it. |

The actual draft fingerprints match plan :40-45:

- D/codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex:
  b2978f741056f3ee2e1e92a3671cd51404492374d2bfd100796417ded746306b.
- D/codex-work/r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex:
  5d4ac193aa47e7205e6d645303a68b601f702ad807d0624dc527d4a1766102c1.

The plan correctly records 21 / 20 / 20 calendar days and requires the actual launch/deadline fact before starting (:47-54). Draft existence does not mechanically certify the owner's milestone judgement. Neither the dry run nor this review authorizes publication or execution.

The supplied dry run has 4 Gate-0, 2 smoke and 68 main pending jobs (H/plan-dryrun-2026-10-14-v5.txt:6,35,131), with expected uncreated runner/seal/freeze/verdict/inspection/analysis prerequisites (:8-10,37-40,133-139). It also honestly flags GIT_EDITOR as forbidden (:21-22,150-151). These are setup/environment prerequisites to complete at the authorized stage, not new code defects or evidence of a failed completed study.

## Closure and final verdict

Fix the pre-launch/recovery analysis anchor in R44-1, correct its plan rationale, and produce pure-test evidence for the resulting final source bytes. The original R41 fixes and the two accepted limits are credited. R44-2 is optional P3 hardening/documentation; R44-3's diagnostic-only difference is now understood and is not a P2 blocker.

No additional concrete P1/P2 was found in the comparator/tool/documentation paths probed. This is bounded review evidence, not an empirical Gate-0 pass, smoke verdict or Stage-1b result.

R38, R41 and R43 reports were preserved byte-for-byte. In particular R43 remains 19,448 bytes, SHA-256 abb7a34214450fe0bc968c5d26952655623ed06861e6b800ca6898c4ad9b54ae; its evidence classification is updated here without rewriting that historical report.

**NOT READY is based solely on the reproducible P2 scientific-analysis recovery path.**
