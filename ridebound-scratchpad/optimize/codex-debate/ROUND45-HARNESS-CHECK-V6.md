# Round 45: targeted check of the Stage 1b harness, version 6

R44 (`codex-work/R44-HARNESS-RECHECK-V5-CODEX.md`) found ONE remaining P2 (R44-1): a restart could accept changed
analysis code after main outputs existed but before a binding log existed, and the plan misdescribed that window.

The Claude fixer wrote `-v6` copies of all five harness files in
`E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`. Start with `HARNESS-FIX-REPORT-R44.md`.

**What the fixer reports.**
- Before any main job launches, a durable `logs/main/<job>.admitted` file is written and synced, holding the hash of
  the analysis binding.
- On restart, any main output or log without a matching admission refuses the run and writes `INPUT-DRIFT-STOP.txt`.
- The plan text is corrected (§12, §14).
- The v6 comparator differs from v5 only in which driver it loads.

**Logs.**
- `selftest-2026-10-14-r44-on-v5.log`: 2 OK / 7 BAD. Your counterexamples reproduce on v5, including the
  68-complete-outputs case.
- `selftest-2026-10-14-v6.log`: 326 OK / 0 BAD / 2 LIMIT.
- `plan-dryrun-2026-10-14-v6.txt`.

**Housekeeping.** `HARNESS-FIX-REPORT-R41.md` was written by an unidentified agent and has inaccuracies.
`HARNESS-FIX-REPORT-R41-v2.md` is the fixer's corrected version; use it.

## Convergence rule (unchanged)

Return READY TO SEAL unless a concrete P1/P2 counterexample remains. A P1/P2 finding is one that could let a
non-equivalent or corrupt run pass a gate, or change a scientific result. P3 items go into the plan's known-limitations
list.

## Do (READ ONLY)

1. Verify that R44-1 is closed. Re-try your R44 counterexamples against v6, using in-memory or temp-dir probes only.
2. Check that the v6 diff introduces no new P1/P2. In particular, check the comparator's claim to be "the same as v5
   except for the driver it loads".
3. Give the verdict, with findings ranked and file:line.

Never run jobs, .NET, publish, commit, freeze or seal, and never edit the harness.

## Output

Write ONLY `codex-work/R45-HARNESS-CHECK-V6-CODEX.md` (exclusive-create).

Final message: the verdict and the findings.
