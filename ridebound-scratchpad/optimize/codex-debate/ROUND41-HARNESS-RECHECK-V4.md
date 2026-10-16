# Round 41 (Codex): re-review of the Stage 1b harness, version 4

You reviewed this harness three times: R24 (NOT READY), R28 (NOT READY), and R38 (`codex-work/R38-HARNESS-RECHECK-V3-CODEX.md`, NOT READY).

## Background and Context

In R38, you confirmed:
- The owner-authorized behavioural-only Gate 0 is sound, honest, and properly disclosed.
- All 8,485 archived frames decode canonically without any rejection.
- Repaired earlier counterexamples (duplicate fields, ranks/bounds, live-tree fallback, Unicode range).

Your R38 blockers were:
1. **R38-1 (P2):** Positive pair carrying corrupt run-report digests or false artifact receipts.
2. **R38-2 (P2):** Start-up integrity drift or worker exceptions bypassing durable stop and post-phase verification.
3. **R38-3 (P2):** STOP created during the long stat scan before admission.
4. **R38-4 (P2):** Incomplete validation of smoke generation evidence (omissions counts, vehicle losses, exogenous breaches).
5. **R38-5 (P3):** Lexical `.pth` path containment escaping tree via relative paths/junctions.
6. **Section 6:** Pre-seal facts (tool audits for git/taskkill, CreateProcess resolution, launch environment `GIT_*` unsetting, analysis freeze requirement before main phase, and plan facts with owner decisions of 2026-10-13).

## What the Fixer Wrote in Version 4

The `-v4` files are in `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`:
- `compare_equivalence_stage1b-v4.py`
- `run_stage1b-v4.py`
- `test_compare_equivalence_stage1b-v4.py`
- `STAGE1B-PLAN-DRAFT-v4.md`
- `RUNNER-PROVENANCE-TEMPLATE-v4.md`
- `HARNESS-FIX-REPORT-R38.md`
- `selftest-2026-10-13-v4.log`

## Do (READ ONLY; never run jobs, .NET, publish, commit, freeze, seal, or edit harness files)

1. **Verify R38-1 through R38-5 and Section 6.** For each finding, mark it FIXED / PARTLY / NOT FIXED with file:line.
2. **Run your own read-only probes** using Python `-B` on in-memory objects or archived bytes, exactly as in R38.
3. **Check the self-test log** `selftest-2026-10-13-v4.log` and verify that the new finding controls pass on v4 and fail on v3.
4. **Verdict:** READY TO SEAL / READY WITH CHANGES (list) / NOT READY.

## Output

Write ONLY `codex-work/R41-HARNESS-RECHECK-V4-CODEX.md` (exclusive create). Cite exact file:line.

Final message: the verdict and top findings.
