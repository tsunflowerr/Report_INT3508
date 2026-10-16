# Round 28: re-review of the Stage 1b harness after the fixes for your R24 findings

You reviewed the harness in `codex-work/R24-HARNESS-REVIEW-CODEX.md` and judged it NOT READY. A Claude fixer has
written new `-v2` files in `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`. The originals are
untouched.

Start with `HARNESS-FIX-REPORT-R24.md`: it maps each finding to a test, a fix and a result, with file:line.

## Files to read

- `compare_equivalence_stage1b-v2.py` and `test_compare_equivalence_stage1b-v2.py`
- `run_stage1b-v2.py`
- `STAGE1B-PLAN-DRAFT-v2.md`
- `RUNNER-PROVENANCE-TEMPLATE-v2.md`

## Logs to read

- `selftest-2026-10-12-v2.log`: 148 OK / 0 BAD / 1 GAP.
- `selftest-2026-10-12-r24-original.log`: the new tests run on the original files, 16 OK / 49 BAD.
- `plan-dryrun-2026-10-12-v2.txt`

## Do (READ ONLY; never run jobs, publish, commit, freeze, seal, or edit the harness)

1. For each R24 finding (F1–F6 and anything else you listed), say whether it is FIXED, PARTLY FIXED or NOT FIXED, with
   file:line evidence. Look for regressions and for new ways a non-equivalent run could pass Gate 0, or an equivalent
   run could fail it.
2. **The F1 gap.** The digests of decisions 2..N cannot be recomputed from a transcript, because they need the Runner's
   internal state before each batch. They are checked by links and content equality only.
   - Is that acceptable for Gate 0, given that the behavioural comparisons are exact?
   - Or must Gate 0 replay the transcript through the frozen v3 Runner (a .NET run)? If so, say exactly what that
     replay must check.
3. Check that the R24 tests really fail on the original files for the right reason. Use the log, plus the tests'
   code.
4. **Freeze scope.** The freeze now includes the FleetPy tree, the job interpreter environment, dotnet host/fxr and the
   runtimes, and the steering environment variables.
   - Is it complete?
   - Is "bound from freeze time only" (no archived baseline from the original T3.8 runs) acceptable? If it is, give
     the wording the plan should use.
5. **Plan.** Check the `<FILL>` start-rule items and the Stage 2 sentences against R17 A2 / R18.
6. **Verdict:** READY TO SEAL / READY WITH CHANGES (list) / NOT READY. Rank the findings by severity, with file:line.

You may re-run the pure self-test file only if it writes nothing outside the harness folder's existing log pattern.
Prefer reading the logs.

## Output

Write ONLY `codex-work/R28-HARNESS-RECHECK-CODEX.md` (exclusive-create). Zero hallucination; cite file:line.

Final message: the verdict and the top findings.
