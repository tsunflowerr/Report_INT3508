# Round 45 - Stage 1b harness v6 targeted check (Codex, 2026-10-14)

**Verdict: READY TO SEAL. R44-1 is FIXED; no concrete P1/P2 counterexample remains in the paths reviewed.**

V6 writes an exclusive, flushed and fsynced admission anchor before a main child can produce output. Recovery refuses and persists loss for output without its anchor, or for an anchor naming another analysis binding. The original R44 counterexamples, including 68 completed outputs without anchors, now reject.

The comparator's comparison, report-validation and outcome rules are unchanged from v5. The v6 full-suite receipt matches the delivered files. One new optional P3 concerns the exit status for unfinished anchor-only jobs; it does not block this verdict under the convergence rule.

## Scope and reviewed identities

Aliases in file:line citations:

- H/ = E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/
- D/ = E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/
- F/ = E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/

I read D/ROUND45-HARNESS-CHECK-V6.md and started with H/HARNESS-FIX-REPORT-R44.md. For round-5 housekeeping I used H/HARNESS-FIX-REPORT-R41-v2.md, which explains the inaccurate older report and development capture (:12-31). The old reports and files were preserved.

Two independent sub-agents reviewed driver recovery/error paths and comparator/diff/log evidence. I checked their material conclusions against source and independently reproduced the relevant controls. All executable probes used Python -B and in-memory filesystem/process substitutes. Driver main/run_job were exercised, with actual child launches forbidden or replaced by a fake callable. The supplied logs/dry runs were read only. No job, .NET execution, build, publish, commit, freeze, seal or harness edit occurred. This exclusive-create report is the only filesystem output.

Current SHA-256 values:

| H/ file | SHA-256 |
|---|---|
| run_stage1b-v6.py | 42121e5fe9156a646360b143b9c03bc286700da9db2349df5416e698324c5deb |
| compare_equivalence_stage1b-v6.py | 4d36c470b654e3bf5a612a05125285dc709c8bd8d01b5e54798ec52fbb56862a |
| test_compare_equivalence_stage1b-v6.py | 5d863b50613b88949bba2ce5170e71005382708efc913b65ce265ea8205d3676 |
| STAGE1B-PLAN-DRAFT-v6.md | ca05821242971cc3a3fa51960d1c787e73fa395c29d1703150b13773dbfcff4a |
| RUNNER-PROVENANCE-TEMPLATE-v6.md | bad867c25be9ef3e391b60e144fdb7150c21c381631b6c21ac8970a5c5779781 |
| selftest-2026-10-14-v6.log | 94e82b14b3cd660633572fe7bc5d5cdb320bf50031f5e4a17732f3c9fb3e724f |
| selftest-2026-10-14-r44-on-v5.log | b3e50e3c310cb259fc1ab94df47c39f55cd70a08083179e7244437b32a8404e9 |
| plan-dryrun-2026-10-14-v6.txt | 7b819b38883ed30235ecce8d022a0e129ee5435ec7861d17a66ab861fe5b4be6 |
| HARNESS-FIX-REPORT-R44.md | 2e87973f942f9f63d008e52f30d1fa4c35be92e1d78a037713210d49cdd4d2f0 |
| HARNESS-FIX-REPORT-R41-v2.md | 1e6ddc1b50624298b39737d63f47c3a2489e8fa7e014494db2c81f79dba53fa2 |

The brief SHA-256 is 623edaf037ba0b598aa87f7ea25fa4b0480f6699891c865f06ba3dc2dcf9e6a0.

## R44-1 closure

**FIXED.** Exact implementation locations:

- H/run_stage1b-v6.py:979-993: logs/main/<job>.admitted is created with mode "x", contains the held binding SHA, and is written, flushed, fsynced and closed.
- H/run_stage1b-v6.py:1234-1245: anchor creation finishes before subprocess.run. OSError prevents launch and returns stopped-no-admission-anchor. Missing held binding also refuses.
- H/run_stage1b-v6.py:996-1009: every existing anchor must match the current binding; an output directory or log without an anchor is a problem; the original log-first-line check is retained.
- H/run_stage1b-v6.py:975,1392-1397: binding verification invokes these checks; startup refusal writes INPUT-DRIFT-STOP.txt.
- H/run_stage1b-v6.py:1255-1262: the post-phase check also persists analysis/anchor loss.
- H/STAGE1B-PLAN-DRAFT-v6.md:324-330,357-361: the plan describes the admission anchor and explicitly corrects v5's false pre-first-log rationale.

Root reran the supplied section F directly, importing the test definitions without executing test main or requesting an output log:

~~~python
T = t.targets(version)  # version "v5", then "v6"
c = types.SimpleNamespace(
    T=T, new_id={"ok": True, "dll": "b" * 64, "tree": "t" * 64}
)
t.r44_1(c)
~~~

The synthetic identity is only a fixture for unrelated input/verdict checks, not a published Runner. Helpers are H/test_compare_equivalence_stage1b-v6.py:2538-2587,2816-2851; the nine controls are :2854-2914.

| Control | V5 root reproduction | V6 root reproduction |
|---|---|---|
| Original analysis, main output, no log or admission anchor | Admitted; no drift | SystemExit; drift written |
| Analysis/code/manifest/binding replaced consistently after output, no log/anchor | Admitted; no drift | SystemExit; drift written |
| Same replacement with original admission anchor, no log | Admitted; no drift | SystemExit; drift written |
| Unchanged analysis, output, matching admission anchor, no log | Admitted, deferred-worker return 3 | Admitted, deferred-worker return 3 |
| Replaced analysis with original log and admission anchor | SystemExit; drift written | SystemExit; drift written |
| All 68 outputs complete, no anchors/logs, changed analysis | Return 0; no drift | SystemExit; drift written |
| Actual run_job anchor-before-child ordering | Fake child sees no anchor | Fake child sees held-SHA anchor |
| Exclusive anchor creation fails | Fake child still called | No child call |
| Corrected plan rationale and lifecycle disclosure | Absent | Present |

Fresh section-F totals: **v5 2 OK / 7 BAD; v6 9 OK / 0 BAD.** BAD on v5 is the expected reproduction of the missing fix.

Root also reran the retained R41 analysis-binding (8), tool-scope (3) and documentation (7) controls on v6. Together with section F, this gave **27 OK, 0 BAD, 0 LIMIT**. Same-invocation restamping still produces durable drift; amendment coverage, retained inventory, System32 taskkill scope, version/receipt identities and seal-list alignment still pass.

Additional direct recovery controls:

~~~text
all 68 complete outputs + all matching anchors:
  return 0; exception None; drift receipt none; no child attempted

output + malformed anchor:
  SystemExit; drift receipt written
~~~

These confirm that the stronger guard retains a valid completed-output positive and rejects malformed admission evidence. No real output bundle or empirical result was created.

### Prelaunch synchronization and failure ordering

The supplied fake writer has no fileno, so its section-F ordering control does not exercise fsync. I added an in-memory handle with fileno and a mocked os.fsync, then called actual run_job. Observed order:

~~~text
exclusive open -> write -> flush -> fileno -> fsync -> close
-> fake child -> log open -> reservation release
~~~

| Injected failure | Child calls | Reservation after return |
|---|---:|---:|
| Anchor exclusive open | 0 | 0 |
| Anchor write | 0 | 0 |
| Anchor flush | 0 | 0 |
| Anchor fsync | 0 | 0 |
| Anchor close | 0 | 0 |
| No held analysis binding | 0 | 0 |

Each anchor failure returned stopped-no-admission-anchor. A separate log-open failure after the fake child retained the already written/synced admission anchor and released the reservation. The source's finally release is H/run_stage1b-v6.py:1250-1251.

This tests the control-flow ordering and error behavior. It does not claim a physical power-loss experiment or authentication against deliberate rewriting of every local receipt.

## V5-to-v6 diff and regression assessment

The comparator's functional claim is verified. Whole-file text also updates documentation, usage examples and the emitted version name:

- H/compare_equivalence_stage1b-v6.py:1-4,92-97: module explanation and usage names.
- H/compare_equivalence_stage1b-v6.py:123-124: DRIVER_FILE / DRIVER_MODULE point to v6.
- H/compare_equivalence_stage1b-v6.py:1810: report header names the v6 comparator.

I excluded only the module docstring and normalized these exact three strings in the remaining v6 source:

~~~text
run_stage1b-v6.py -> run_stage1b-v5.py
run_stage1b_v6 -> run_stage1b_v5
compare_equivalence_stage1b-v6.py -> compare_equivalence_stage1b-v5.py
~~~

The remaining source bytes are identical to v5, SHA-256:
81decc89611b317d3a175fee0ab193ec2e21e3ac6281877b5a8ecf4017d6c2a6.

Thus no equivalence, digest, smoke, outcome-conservation or report-validation rule changed. The driver-binding change is appropriate: H/run_stage1b-v6.py:149,231-235 loads the v6 comparator and seals v6 files; the comparator now checks the corresponding driver/seal requirements.

The driver's functional diff is the new anchor functions, their use by the binding checker, refusal to relaunch an anchor-only pending job, and the anchor write before the child. Other changes are version identities and diagnostics. Existing startup/post-phase persistence and held-binding guards remain. I found no new concrete P1/P2 in these changes.

The test diff adds v6 targets, section F, anchor/completed-output fixture support, flush support, and matching anchors to the old resume controls. Version-condition extensions retain the existing Git/tool/environment checks for v6. Sections A-E remain in the full v6 path (H/test_compare_equivalence_stage1b-v6.py:2934-2948). Only F runs when the new test targets v5. Optional file output remains explicit at :2953-2955 and was not used.

## Ranked remaining finding

### R45-1 - P3, optional: an unfinished anchor-only job can leave main returning zero

**Locations:** H/run_stage1b-v6.py:1219-1220,1417,1425; H/STAGE1B-PLAN-DRAFT-v6.md:329-330.

run_job correctly avoids automatically relaunching an existing admission anchor without output, returning anchor-exists-pending. The deferred counter recognizes deferred/stopped prefixes and log-exists-pending, but omits this new label. If all other jobs are complete, main can return 0 with one job still pending owner review.

Root reproduction, using the actual main and actual run_job through the supplied in-memory helper:

~~~python
T = t.targets("v6")
c = types.SimpleNamespace(
    T=T, new_id={"ok": True, "dll": "b" * 64, "tree": "t" * 64}
)
w = t.AnalysisWorld()
held = w.write_binding()
names = [job[0] for job in T.s.jobs("main")]
st = t.analysis_main(
    c, w,
    anchors={name: "analysis-binding " + held for name in names},
    completed=names[1:],  # first job has an anchor but no output
    run_job="real",      # any child attempt raises; none was attempted
)
print(t.describe_main(st))
~~~

~~~text
one anchor-only job + 67 complete outputs:
  return 0; exception None; drift receipt none
~~~

An all-68-anchor-only probe likewise returned 0. The job labels still identify the unfinished work, no new child launches, and no output/report is fabricated. This is an operational exit-status defect; no complete gate bypass or changed scientific result was demonstrated. It remains P3 and does not block READY TO SEAL.

Optional cheap fix: count anchor-exists-pending with log-exists-pending at :1417, giving the usual deferred return 3. If retained, add an explicit section-14 note that zero exit status can accompany anchor-only owner-review work, with the reason that anchors prevent duplicate launch and completion is judged from per-job outputs/states. The plan already requires owner review of such anchors (:329-330), but does not disclose this specific zero-status behavior. No harness edit was made in this review.

## Test receipts, disclosures and setup facts

Root independently parsed status lines and checked all seven tested-file hashes plus the frozen verifier helper hash for each supplied receipt below. All eight headers match current bytes. All three logs decode as valid UTF-8.

| Supplied evidence | Count / source |
|---|---|
| H/selftest-2026-10-14-v6.log | 326 OK / 0 BAD / 2 LIMIT; summary :347; new section F :337-346 |
| H/selftest-2026-10-14-r44-on-v5.log | 2 OK / 7 BAD / 0 LIMIT; controls and summary :11-20 |
| H/selftest-2026-10-14-v5-rerun.log | 317 OK / 0 BAD / 2 LIMIT; summary :337; delivered-v5 headers match |

I did not rerun the long full suite. The new targeted root controls and synchronization probes above supplement the matching supplied full-suite receipt. The corrected R41-v2 report is credited for explaining the development capture rather than changing its historical bytes.

The two accepted LIMITs remain explicitly disclosed at H/STAGE1B-PLAN-DRAFT-v6.md:347-350 and H/selftest-2026-10-14-v6.log:99,237. N1 is owner-decided behavioural equivalence with middle-decision digests checked for links/content, not production .NET replay validity. R38-1 is the unavailable physical-adapter preimage of checkpointBindingHash, whose format/enclosing semantic receipt can be checked. Neither is reopened.

The plan's corrected pre-first-admission window (:357-361) is consistent with the new ordering: no harness-launched main child starts before its anchor. Coordinated forgery of every local receipt is honestly scoped out (:362-365). Lifecycle multiplicity remains the accepted optional P3 and is now listed with its narrow reason (:366-369). Exact Gate-0 frame comparison still rejects changed events; no complete smoke bypass was demonstrated. The new status-only P3 should be added there if retained.

The v6 seal list matches the actual driver, and the provenance template still correctly uses RUNNER-PROVENANCE-v3.md for the Runner build while naming v6 harness artifacts (plan :334-341; H/RUNNER-PROVENANCE-TEMPLATE-v6.md:1-13,76). Readiness does not fill publication, provenance, freeze, seal or analysis-amendment records.

The supplied dry run records 4 / 2 / 68 pending jobs (H/plan-dryrun-2026-10-14-v6.txt:6,35,131), expected missing prerequisites (:8-10,37-40,133-139), and the forbidden GIT_EDITOR of the fixer's shell (:22,52,151). These are setup facts, not code failures. Use the required launch environment at the authorized stage.

The launch date must still meet the plan's 21-calendar-day rule with the confirmed deadline/lower bound (H/STAGE1B-PLAN-DRAFT-v6.md:49-56). A later launch cannot infer 21 remaining days merely from "after 2026-11-03." This verdict does not amend that rule or authorize any action prohibited by the read-only brief.

R44's report remains 22,532 bytes, SHA-256 cc305a74558216bd1d787c7525269c0b5e01b92cf73e67de1482c8dbb2ba435a. The five reviewed v5 harness files also retain their R44 fingerprints.

**READY TO SEAL under the convergence rule. R44-1 is closed; R45-1 is optional P3 hardening/disclosure.**
