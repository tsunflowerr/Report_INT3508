# Round 46 (Codex): review the Stage 1b analysis scripts before they are frozen

**Status.** Stage 1b is sealed. `tang3/stage1b/harness/STAGE1B-PLAN.md` = plan v7 with the runner values filled in, and
`STAGE1B-PLAN.sha256` was written 2026-10-14 13:27. Gate 0 is running. The main phase (68 jobs) needs the analysis
freeze `stage1b-analysis-freeze.sha256` BEFORE any main job (plan §8, §12). A Claude agent wrote the analysis scripts.
Review them before the coordinator freezes them.

## Files (harness folder `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`, READ ONLY)

- `extract_stage1b.py`
- `report_stage1b.py`
- `test_analysis_stage1b.py`
- `analysis-selftest-2026-10-14.log`: 192/192
- `STAGE1B-ANALYSIS-AMENDMENT.md`: a draft; its `inventory-reviewed-by:` line is still a placeholder

The plan definitions they implement are in §1, §5, §6, §7 and §12 of `STAGE1B-PLAN.md`.

**Writer's claims to check:**
- B1: SF used as both selectors gives I_L = I_served = I_timely60 = 0 in 34/34 cells.
- B3: Stage 1a C-120 numbers reproduce, and the per-run numbers equal your `codex-work/R19-stage1a-analysis.json` on
  102 runs × 18 quantities.
- The read and import closure is enforced by an audit hook.

**Writer's open questions:**
1. "Median initial promised ride time" is implemented as p0 − t0, nearest-rank, over accepted riders.
2. H1 forced/no-worse records are counted as non-normal decisions + non-exogenous breach kinds + ledger mismatches.
3. No CI; leave-one-day-out is reported instead.
4. No override exists for stop receipts.
5. Served = completed AND alighted. Edge cases count as not served; a served rider without a drop promise stops the
   analysis.

## Do (READ ONLY; no jobs, no edits; read-only Python `-B` probes are fine)

1. **Definitions.** Check every plan definition against the code: served, A, p0, L/T, I_L/I_served/I_timely60 and the
   identity, the SF constants, cell/day handling, G0, H1–H7, the guards in §7 and the binding logic of §12.
   Cite file:line for any mismatch.
2. **Open questions.** Answer the writer's 5 questions against the plan and R16/R17/R18. Give the reading the plan
   supports.
3. **Write a failure scenario for any of these:**
   - the scripts could compute something different from the plan;
   - they could silently accept a wrong, missing or foreign run;
   - they could be changed after the freeze without detection.
4. **Inventory.** Is the proposed freeze inventory complete? It is: extract, report, `runner-tier3-v3.sha256.tsv`, the
   amendment, the test and the self-test log.
5. **Verdict.** FREEZE AS IS / FREEZE AFTER CHANGES (list) / DO NOT FREEZE, with the findings ranked.

## Output

Write ONLY `codex-work/R46-ANALYSIS-REVIEW-CODEX.md` (exclusive-create). Zero hallucination; cite file:line.

Final message: the verdict and the top findings.
