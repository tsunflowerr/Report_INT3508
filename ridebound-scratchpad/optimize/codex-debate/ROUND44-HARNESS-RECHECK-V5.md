# Round 44: re-review of the Stage 1b harness, version 5 (convergence round)

You reviewed this harness four times:
- R24: NOT READY;
- R28: NOT READY;
- R38: NOT READY;
- R41 (`codex-work/R41-HARNESS-RECHECK-V4-CODEX.md`): NOT READY, though v4 repaired the R38 counterexamples.

The Claude fixer then wrote `-v5` files in `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`:
- `compare_equivalence_stage1b-v5.py`
- `run_stage1b-v5.py`
- `test_compare_equivalence_stage1b-v5.py`
- `STAGE1B-PLAN-DRAFT-v5.md`
- `RUNNER-PROVENANCE-TEMPLATE-v5.md`
- report `HARNESS-FIX-REPORT-R41.md`

Logs:
- `selftest-2026-10-14-v5.log`: 317 OK / 0 BAD / 2 LIMIT.
- `selftest-2026-10-14-r41-on-v4.log`: the new R41 tests on v4, 4 OK / 22 BAD, as intended.
- `plan-dryrun-2026-10-14-v5.txt`.

## Convergence rule (coordinator decision, recorded in DEBATE-LEDGER)

To stop endless rounds:
- **P1/P2 findings must be fixed.** A P1/P2 finding is one that could let a non-equivalent or corrupt run pass a
  gate, or change a scientific result.
- **P3 hardening items may be accepted as known limitations.** They must be listed in the plan's "Known limitations
  accepted before seal" section, with a reason.
- **Two LIMITs are accepted:** the owner-decided N1, and R38-1. Check that both are disclosed honestly.

**Return READY TO SEAL if no P1/P2 finding remains,** even if you would still like P3 hardening; list those as
optional. Return NOT READY only for a concrete P1/P2 finding, and give a reproducible counterexample.

## Do (READ ONLY; never run jobs, .NET, publish, commit, freeze, seal, or edit the harness)

1. **R41 items.** For each, mark it FIXED / DOCUMENTED (accepted P3) / NOT FIXED, with file:line. Probe the fixes the
   way you probed v4.
2. **New P1/P2 paths.** Look for any new P1/P2 path introduced by v5.
3. **The plan's known-limitations list.** Is it complete and honest?
4. **Verdict.** READY TO SEAL / READY WITH CHANGES (list) / NOT READY, with findings ranked by severity and file:line.

## Output

Write ONLY `codex-work/R44-HARNESS-RECHECK-V5-CODEX.md` (exclusive-create). Zero hallucination; cite file:line.

Final message: the verdict and the top findings.
