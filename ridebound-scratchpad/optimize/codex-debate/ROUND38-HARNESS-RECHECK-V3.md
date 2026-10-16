# Round 38: re-review of the Stage 1b harness, version 3

You reviewed this harness twice. R24 found it NOT READY. R28 (`codex-work/R28-HARNESS-RECHECK-CODEX.md`) found it NOT
READY again, with N1–N8.

**Owner decision (2026-10-12) on N1.** Gate 0 is behavioural-only and explicitly disclosed; no .NET replay tool will be
written. Do not re-argue N1 itself. Check that the disclosure and labels are honest and complete, and that nothing
else relies on full protocol validity.

## What the Claude fixer wrote

New `-v3` files in `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`. Start with
`HARNESS-FIX-REPORT-R28.md`. The v3 files are:
- `compare_equivalence_stage1b-v3.py`
- `run_stage1b-v3.py`
- `test_compare_equivalence_stage1b-v3.py`
- `STAGE1B-PLAN-DRAFT-v3.md`
- `RUNNER-PROVENANCE-TEMPLATE-v3.md`

Logs:
- `selftest-2026-10-13-v3.log`: 197 OK / 0 BAD / 1 LIMIT.
- `selftest-2026-10-13-r28-on-v2.log`: the new R28 tests run on the v2 files, 7 OK / 40 BAD, as intended.
- `plan-dryrun-2026-10-13-v3.txt`.

## Do (READ ONLY; never run jobs, .NET, publish, commit, freeze, seal, or edit the harness)

1. **N1–N8 and §5.** For each, mark it FIXED / PARTLY / NOT FIXED, with file:line. Probe the fixes the way you probed
   v2: for example, re-try your duplicate-field counterexample in memory and against the v3 parser.
2. **New ways to fail.** Look for new ways a non-equivalent run could pass the behavioural Gate 0, or an equivalent
   run could fail it. In particular, check whether the new canonical-JSON requirement could reject valid
   archived frames: run it read-only over all frames of the four archived Gate-0 references, and report the counts.
3. **The fixer's open items.**
   - Only `git` is audited among the tools found through `PATH`.
   - The steering environment depends on the shell (`GIT_EDITOR`).
   - The `<FILL>` start-rule facts. The owner says the deadline is more than two weeks after 2026-10-12; the exact
     date is unknown.
   - The main-phase analysis scripts do not exist yet.

   Say which of these must be closed before the seal, and how.
4. **Verdict.** READY TO SEAL / READY WITH CHANGES (list) / NOT READY, with findings ranked by severity and file:line.

You may re-run the pure self-test file only if it writes nothing outside the harness folder's existing log pattern.
Read-only Python `-B` probes on archived bytes are fine.

## Output

Write ONLY `codex-work/R38-HARNESS-RECHECK-V3-CODEX.md` (exclusive-create). Zero hallucination; cite file:line.

Final message: the verdict and the top findings.
