# Round 24 (fresh Codex session): review the Stage 1b harness before its plan is sealed

Context: you (Codex) reviewed the cost-first code change in `codex-work/R22-CODE-REVIEW-CODEX.md` (ACCEPT WITH CHANGES:
F1 binarySha256 must be the sole permitted initialization difference; F2 preserve stable config/input hashes; F3
separate runner provenance; F4 integration coverage via smokes; exact Gate-0 criterion in §5). A Claude harness
builder implemented those requirements in `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/`:
`HARNESS-REPORT.md` (start here), `compare_equivalence_stage1b.py` + `test_compare_equivalence_stage1b.py` (self-test
log `selftest-2026-10-11-final.log`: 59 OK), `run_stage1b.py` (+ `plan-dryrun-2026-10-11-final.txt`),
`wp4-tier3-v2-costfirst.json` + `make_wp4_costfirst.py` + `canonical_wp4.py`, `RUNNER-PROVENANCE-TEMPLATE.md`,
`STAGE1B-PLAN-DRAFT.md`. Nothing has been run, published or committed.

## Do (READ ONLY; never run jobs, publish, commit, or edit the harness)

1. Check that the comparator implements R22 §5 exactly: permitted difference, preserved fields, salted-ID
   normalization that keeps membership/links, exact behavioural comparisons, verdict files; look for any path that
   could let a non-equivalent run pass or an equivalent run fail. Review the self-tests' coverage (what negative case
   is missing?). You may re-run the pure self-test file only if it writes nothing outside the harness folder's
   existing log pattern — prefer reading the log.
2. Check the driver: phases, job counts (4 + 2 + 68), cell lists, runner/manifest/seal/freeze refusals, power/STOP
   safety, disk floor (C: currently ≈ 60.9 GB free; jobs ≈ 6.5–7 GB), output roots, smoke on calibration cell
   d20181114-s10-r1-w08, `main` requiring both verdict files.
3. Check the ON WP4 file and canonical SHA/bindings against your R22 values (16dcb7e3…, CF-U 90b290d7…, CF-C30
   e6b33be5…).
4. Check `STAGE1B-PLAN-DRAFT.md` against R17 A2 / R18 corrections (primary I_L identity, H6 cutoff 345 = ceil(1.10 ×
   313), service guard 2,315, Stage 2 gates) and the proposed publish command and provenance record.
5. Verdict: READY TO SEAL / READY WITH CHANGES (list) / NOT READY, findings ranked by severity with file:line.

Write ONLY `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R24-HARNESS-REVIEW-CODEX.md`
(exclusive-create). Zero hallucination; cite file:line. Final message: verdict and top findings.
