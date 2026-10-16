# Round 43 (Codex): re-review of the Stage 1b harness, version 5

You reviewed this harness four times: R24 (NOT READY), R28 (NOT READY), R38 (NOT READY), and R41 (`codex-work/R41-HARNESS-RECHECK-V4-CODEX.md`, NOT READY).

## Background and Context

In R41, you confirmed:
- Fixed from R38: R38-2 (startup drift, durable stop, post-phase verification), R38-3 (STOP admission race), R38-4 (nested smoke evidence counters, losses, exogenous breaches), R38-5 (lexical `.pth` path containment and imports allowlist), and settled launch environment.
- The owner-authorized behavioural-only Gate 0 and the two test limits (N1-LIMIT and R38-1-LIMIT) remain accepted and properly disclosed.

Your R41 blockers were:
1. **R41-1 (P2):** Retain initial main-analysis identity (bind analysis manifest digest at first main admission into phase snapshot and receipt; require explicit reviewed amendment record `STAGE1B-ANALYSIS-AMENDMENT.md` before main launch).
2. **R41-2 (P2):** Enforce per-run outcome conservation in report checks (enforce disjointness of `acceptedRequestIds` and `rejectedRequestIds`, union equals `requestCount`, and individual list lengths match protocol outcomes).
3. **R41-3 (P3):** Enforce strict integer types for `repeat` and `repeatCount` via `_same_int` helper (reject raw booleans `true`/`false`).
4. **R41-4 (P3):** Scope taskkill exception strictly to declared `System32/taskkill.exe` path and frozen hash (reject non-System32 paths like `E:/outside/taskkill.exe`).
5. **R41-5 (P3):** Align plan draft v5, provenance template v5, and driver required receipts consistently to v5 identities; correct 21-calendar-day arithmetic note (2026-10-14 to 2026-11-04 is 21 days); attach A1 milestone draft hashes.

## What the Fixer Wrote in Version 5

The `-v5` files are in `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`:
- `compare_equivalence_stage1b-v5.py`
- `run_stage1b-v5.py`
- `test_compare_equivalence_stage1b-v5.py`
- `STAGE1B-PLAN-DRAFT-v5.md`
- `RUNNER-PROVENANCE-TEMPLATE-v5.md`
- `HARNESS-FIX-REPORT-R41.md`
- `selftest-2026-10-14-v5.log` (317 OK, 0 BAD, 2 LIMIT; exit 0)

All earlier versions (`-v4`, `-v3`, `-v2`, originals) are preserved unchanged.

## Do (READ ONLY; never run jobs, .NET, publish, commit, freeze, seal, or edit harness files)

1. **Verify R41-1 through R41-5.** For each finding, mark it FIXED / PARTLY / NOT FIXED with file:line.
2. **Run your own read-only probes** using Python `-B` on in-memory objects or archived bytes, exactly as in R41.
3. **Check the self-test log** `selftest-2026-10-14-v5.log` and verify that the new finding controls pass on v5 and fail on v4.
4. **Verdict:** READY TO SEAL / READY WITH CHANGES (list) / NOT READY.

## Output

Write ONLY `codex-work/R43-HARNESS-RECHECK-V5-CODEX.md` (exclusive create). Cite exact file:line.
