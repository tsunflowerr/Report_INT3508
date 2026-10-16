# Round 22 from Claude: independent code review of the Stage 1b cost-first option

A Claude implementer added a default-off `selectionObjectiveOrder` option (stability-first | cost-first) in the
uncommitted worktree `C:/Code/RideBound-costfirst` (branch `research/tier3-cost-first` from 761915c). Report:
`E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/IMPLEMENTATION-REPORT.md`; diff
`tang3/stage1b/costfirst-diff-2026-10-11.patch`; test logs `baseline-test.log` (1024/1025, known StrictBagIt clean-tree
failure) and `after-test.log` (1033/1033); mutation log `mutate-costfirst.log`. Nothing is committed or published.

## Do (READ ONLY on the worktree; never build, test, commit or edit there)

1. Review the production diff line by line against R17/R18 Stage 1b requirements: cost-first keeps forced-reference
   (with its activation condition), accepted-request count, operational cost and candidate-id tie levels, and skips
   only worst-hard-utilization and the revision levels; HardVector profile, hard assessor, gates, locks, recovery (b),
   late boarding, generation/retention unchanged; absent key → byte-identical canonical WP4 config and binding.
   Look for any path where the option silently changes OFF behaviour, any missing validation, and anything in
   SoftHardHybrid/RollingCost that the change touches.
2. Review the 8 new tests and the mutation check: do they pin the requirements (especially OFF equivalence of the
   binding hash against archived values)? What is untested?
3. Review the Gate-0 plan implications in §8 of the report (new runner binary SHA; coreCommitSha follows the repository
   root E:/Code/RideBound-deadline; WP4 for the cost-first arm = v2 + one key). Propose the exact equivalence criterion
   for the 4 OFF jobs (which fields to ignore, which must match) based on `optimize/compare_equivalence.py`.
4. Verdict: ACCEPT / ACCEPT WITH CHANGES (list) / REJECT, plus findings ranked by severity with file:line.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R22-CODE-REVIEW-CODEX.md`. Zero hallucination; cite file:line. Final message: verdict and top findings.
