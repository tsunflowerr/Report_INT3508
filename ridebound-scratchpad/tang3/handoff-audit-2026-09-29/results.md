# results

## 1. [path-convention]
In every source below, T3 means E:\Code\Report_INT3508\ridebound-scratchpad\tang3 and SW means T3\sweep.
SOURCE: Get-ChildItem of E:\Code\Report_INT3508\ridebound-scratchpad\tang3 and \sweep (listing command)

## 2. [sweep-files-inventory]
SW contains these docs: SWEEP-PLAN.md (7336 B), SWEEP-PLAN.sha256, SWEEP-AMENDMENTS.md (6416 B), SWEEP-REPORT.md (16614 B, last modified 2026-09-29 11:54). It also contains no-worse-v1-worktree-edits.patch (67705 B), the TSVs sweep-jobs-2026-09-26.tsv, sweep-paired-2026-09-26.tsv, sweep-mechanism-2026-09-26.tsv and noworse-jobs-2026-09-26.tsv, 13 .py files, and the logs\ and logs-noworse\ folders.
SOURCE: Get-ChildItem SW (command output)

## 3. [sweep-logs-inventory]
SW\logs has 168 .log files (156 sweep jobs + 12 -rerun1), 3 .out, 3 .err (all 0 bytes) and 6 .txt: noworse-aggregate-2026-09-26.txt, noworse-analyze-2026-09-26.txt, sweep-aggregate-2026-09-26.txt, sweep-predictions-2026-09-26.txt, sweep-view-2026-09-26.txt and sweep-worlds-final-2026-09-26.txt. SW\logs-noworse has 28 .log files.
SOURCE: Get-ChildItem SW\logs | Group-Object Extension; Get-ChildItem SW\logs-noworse (command output)

## 4. [plan-seal]
SWEEP-PLAN.md was sealed on 2026-09-25T09:33:58Z with SHA-256 756b65fd2b500eacfab404a031afd26cfb89b96ddc69fe0d4f134aa7a2b6423f. The current file hash is identical, so the plan was not modified after sealing.
SOURCE: SW\SWEEP-PLAN.sha256:1; Get-FileHash SW\SWEEP-PLAN.md (output 756b65fd...423f)

## 5. [plan-question]
C-x means the total decision-caused drop-time change per rider is at most x. M+-x means the drop is no later than the first promise + x, i.e. Schulz & Pfeiffer (2026) l = B + L with L = x. The two rules are compared on four aspects: service, what riders see, whether each rule's own promise holds, and recovery.
SOURCE: SW\SWEEP-PLAN.md:11-16

## 6. [plan-matrix]
The matrix has 156 jobs: 13 arms (U; C-x and Mplus-x for x in {30,60,120,300,600,900} s) x 6 worlds W0-W5 (the T3.7 pilot/worlds files) x 2 cells d20181112-s10-r1-w08 and d20181112-s10-r1-w17 (panel wp14-development-panel-v1). Each cell has 108 requests and 8 vehicles. Inputs: world v1.1 (preflight_world_v1_1.py), Runner E:\RideBoundData\research\runner-tier3-v1 (from 69512d3), WP4 configs/wp4-tier3-v1.json (commitmentRecovery forced-reference-v1 = recovery rule (a), lateBoarding record-v1). Output goes to E:\RideBoundData\research\tier3-sweep-v1\<job>.
SOURCE: SW\SWEEP-PLAN.md:18-28; SW\run_sweep.py:29-37

## 7. [plan-fairness]
Each C-x/Mplus-x config pair differs in exactly two keys: .policies[0].dropEtaDeadlineSlackMs and .policies[0].limits[drop_eta_total_ms].hardLimit. The generator log ends with 'problems: none'. Both rules reject only on exceed: C at afterValue > hardLimit (CommitmentBudgetEvaluator.cs:88), M+ at shift > slack (CommitmentLockEvaluator.cs:186-191).
SOURCE: T3\configs\make_configs_sweep.log:33-39; SW\SWEEP-PLAN.md:38-40

## 8. [plan-remaining-differences-vs-paper]
Differences from the paper that remain, applied equally to both rules: no rider-rejection model e^(-mu*RD); none of their insertion/re-optimisation, and no vehicle switching; Manhattan data instead of Hamburg; pickup windows and max ride time are present.
SOURCE: SW\SWEEP-PLAN.md:42-46; SW\SWEEP-REPORT.md:19-24

## 9. [plan-metrics]
Metrics M1-M8 and P:
- M1: completed riders out of 108.
- M2: E2 = share of riders with drop V > 60 s, and CVaR95 of V.
- M3: A = actual drop - first promised drop (mean, p95, max, share A > x = M+ promise broken, share A > 60/300/900 s). The actual drop is the simTimeMs of the batch carrying passengerAlighted.
- M4: C_r (max, share C_r > x = C promise broken).
- M5: non-normal share, forced-rider share, mean forced-fleet share.
- M6: late boardings.
- M7: share with >= 3 options after the gate.
- M8: wall time.
- P: paired comparison on common riders.
SOURCE: SW\SWEEP-PLAN.md:51-63; SW\sweep_analyze.py:6-11,108-132

## 10. [plan-no-do]
Section 7 of the plan forbids:
- changing metrics or predictions after running;
- picking one x level to claim 'better';
- calling a 1-2 rider difference an effect (one episode per cell, noise of about +/-2 riders);
- using panel A.
Recovery rule (b) may be built only if (a) decides the result, and then as its own ADR and a separate run.
SOURCE: SW\SWEEP-PLAN.md:84-91

## 11. [predictions-sealed-text]
Sealed predictions:
- D1: in W0, C-x and M+-x accept the same riders at every x, both cells.
- D2: at x=900, C-900, M+-900 and U accept the same riders in every (world, cell).
- D3: C-x has 0 non-normal decisions and 0 forced breaches.
- D4: M+-x is forced at x=30 in W1, W2, W4 and W5 (both cells), never in W0/W3, and never at x >= 600.
- D5: at x=30, C-30 >= M+-30 in >= 6/8 drift cells.
- D6: in W3, M+-x >= C-x at every x, both cells.
- D7: at x <= 120 in W1, W2, W4, W5, M+ share A > x is > 0 and <= C's share A > x in >= 6/8 cells, for each x.
SOURCE: SW\SWEEP-PLAN.md:74-82

## 12. [predictions-scored-log]
Scoring log (sweep-predictions-2026-09-26.txt):
- D1 HELD, 12/12.
- D2 HELD, 12/12.
- D3 HELD, 0/72.
- D4 NOT HELD: x=30 forced > 0 in 7/8 (zero at W5 w17); W0/W3 zero True; x >= 600 zero True.
- D5 HELD, 6/8: W1w08 82/82, W1w17 79/80, W2w08 85/83, W2w17 79/77, W4w08 94/95, W4w17 89/86, W5w08 90/90, W5w17 99/99.
- D6 HELD, 12/12.
- D7 NOT HELD: x=30 M+ A>x > 0 in 7/8 and M+ <= C in 5/8; x=60 6/8 and 5/8; x=120 6/8 and 7/8.
SOURCE: SW\logs\sweep-predictions-2026-09-26.txt:1-7 (produced by SW\sweep_predictions.py)

## 13. [predictions-report-table]
Report table:
- D1 Đúng 12/12.
- D2 Đúng 12/12.
- D3 Đúng 0/72 job.
- D4 Sai 7/8: W5 tối is not forced ('vì ngày đo thật buổi tối giao thông giảm'); the other two clauses are true.
- D5 Đúng, vừa đủ 6/8.
- D6 Đúng 12/12, every pair equal.
- D7 Sai: 5/8, 5/8, 7/8.
SOURCE: SW\SWEEP-REPORT.md:38-46

## 14. [validity]
Validity:
- 156/156 rows are state status-pass with audit ok.
- 12 outputs are -rerun1 (all W4): Mplus-60/C-120/Mplus-120/C-300/Mplus-300/C-600/Mplus-600/C-900/Mplus-900 at w08, and U/C-30/Mplus-30 at w17.
- There is one sourceScenarioSha256 per cell.
- The world check covered 156 logs with 0 problems.
SOURCE: python read of SW\sweep-jobs-2026-09-26.tsv (Counter {('status-pass','ok'):156}, rerun outputs list); SW\logs\sweep-worlds-final-2026-09-26.txt:1-2 (from sweep_worlds.py)

## 15. [driver-runs]
Run history:
- The main driver finished 156/156 at 32221 s.
- Jobs 109-120 ended exists-no-summary: the 9 W4-w08 jobs from Mplus-60 to Mplus-900, plus C-30, Mplus-30 and U at W4-w17.
- The rerun driver found 12 inventory-drift failures and 0 other failures; 12/12 passed by 2233 s.
- The no-worse driver ran 28 jobs (22 treatment, 6 control), 28/28 pass by 5255 s.
- The sum of wallSeconds over the 156 sweep jobs is 188914 s.
SOURCE: SW\logs\driver-run-1.out:109-120,156; SW\logs\rerun-driver-1.out:1-25; SW\logs\noworse-driver-1.out:1,30-57; python sum of wallSeconds in sweep-jobs TSV

## 16. [sweep-aggregate-table-raw]
sweep-aggregate log. U completed 715 over the drift cells and 1131 over all cells. Each row lists x | drift completed C M+ | all-cell completed C M+ | C own break | M+ own break | C by M+ rule | M+ by C rule | M+ forced breaches | nonNorm | frozen | E2 C M+:
- x=30: 697 692 | 1104 1099 | 0.000 0.144 | 0.135 0.000 | 2123 0.281 0.094 | 0.198 0.187
- x=60: 699 693 | 1108 1102 | 0.000 0.110 | 0.108 0.001 | 1623 0.217 0.070 | 0.205 0.199
- x=120: 703 704 | 1112 1113 | 0.000 0.076 | 0.081 0.004 | 1243 0.129 0.056 | 0.216 0.212
- x=300: 714 716 | 1130 1132 | 0.000 0.007 | 0.008 0.000 | 194 0.039 0.009 | 0.227 0.222
- x=600 and x=900: 715 715 | 1131 1131 | all zeros | 0.227 0.227
SOURCE: SW\logs\sweep-aggregate-2026-09-26.txt:1-8 (produced by SW\sweep_aggregate.py)

## 17. [report-s4-aggregate]
Report §4 over the 8 drift cells (U 715/864). Columns: served C/M+ | C broken | M+ broken | C by M+ rule | M+ forced | M+ frozen | E2 C/M+:
- x=30: 697/692 | 0% | 14.4% | 13.5% | 28.1% | 9.4% | 19.8%/18.7%
- x=60: 699/693 | 0 | 11.0 | 10.8 | 21.7 | 7.0 | 20.5/19.9
- x=120: 703/704 | 0 | 7.6 | 8.1 | 12.9 | 5.6 | 21.6/21.2
- x=300: 714/716 | 0 | 0.7 | 0.8 | 3.9 | 0.9 | 22.7/22.2
- x=600 and 900: 715/715, all 0, E2 22.7/22.7
The C and M+ rider sets are identical in 6/12, 7/12, 6/12, 11/12, 12/12 and 12/12 cells for x = 30...900. This matches the log exactly.
SOURCE: SW\SWEEP-REPORT.md:48-65; SW\logs\sweep-view-2026-09-26.txt:111-117

## 18. [report-s4a-real-vs-synthetic]
Report §4a (added 2026-09-29): real = W5 (216 requests, U 192); synthetic = W1, W2, W4 (648 requests, U 523). Columns: real served C/M+ | real M+ broken | real M+ forced | synthetic served C/M+ | synthetic M+ broken | synthetic C by M+ rule | synthetic M+ forced:
- x=30: 189/189 | 1.1% | 11.9% | 508/503 | 18.8% | 17.7% | 33.5%
- x=60: 190/190 | 0 | 0 | 509/503 | 14.7 | 14.4 | 28.9
- x=120: 190/191 | 0 | 0 | 513/513 | 10.1 | 10.8 | 17.2
- x=300: 192/192 | 0 | 0 | 522/524 | 1.0 | 1.0 | 5.2
- x=600 and 900: 192/192 | 0 | 0 | 523/523 | 0 | 0 | 0
Rule (b) on the synthetic group, C/(a)/(b): 508/503/508, 509/503/509, 513/513/514, 522/524/522. The report says the thesis tables bang:quet and bang:quetb use this split.
SOURCE: SW\SWEEP-REPORT.md:67-88 (script split_noworse.py; no saved output log). I recomputed it by hand from sweep-view log values and noworse-analyze counts: every cell matches.

## 19. [report-s4b-per-world]
Report §4b (per_world.py). Columns: world | U | M+(a) broken at 30/60/120/300 s | served at 30 s C/(a)/(b):
- W0: 201 | 0/0/0/0 | 192/192/192
- W1: 167 | 12.3/12.3/7.8/3.0% | 161/162/161
- W2: 166 | 28.8/25.2/21.4/0% | 164/160/164
- W3: 215 | 0/0/0/0 | 215/215/215
- W4: 190 | 15.3/6.6/1.1/0% | 183/181/183
- W5: 192 | 1.1/0/0/0% | 189/189/189
C broken is 0% everywhere. Burden: 22 treatment jobs, 15528 decisions, about 3789 non-normal (24%), 224 riders with a forced breach out of 1874 served, i.e. about 17 forced decisions per late rider.
SOURCE: SW\SWEEP-REPORT.md:90-107 (script SW\per_world.py, no saved log). I recomputed the per-world values from the sweep-view log, and the burden numbers by python from noworse-jobs TSV: decisions 15528, nonNormal x decisions = 3789.0 (0.244), ridersWithAnyForcedBreach 224, completed (b) 1874.

## 20. [per-cell-sweep-view]
Per-cell completed C/M+ at x=30. W0: 97/97 and 95/95. W1: 82/82 and 79/80. W2: 85/83 and 79/77. W3: 108/108 and 107/107. W4: 94/95 and 89/86. W5: 90/90 and 99/99. U completed per cell (w08/w17): W0 102/99, W1 87/80, W2 87/79, W3 108/107, W4 96/94, W5 92/100. M+ forced breaches at x=30: W1 162/217, W2 419/527, W4 463/243, W5 92/0. U maxA per cell: W1w17 409 s and W1w08 363 s.
SOURCE: SW\logs\sweep-view-2026-09-26.txt:3-109 (produced by SW\show_sweep.py)

## 21. [report-s5-mechanism]
Report §5: in cells where the two rider sets differ, most riders served by only one rule are not blocked directly by the other rule. Example W1 w17 x=30: 7 riders are served only under M+, and 2 of them had candidates pruned by C's cap. The TSV row is W1 w17 30: onlyM 7, onlyC 6, onlyM_blockedByCBudget 2, onlyM_otherCodesOnly 5, onlyC_blockedByMDeadline 2, onlyC_otherCodesOnly 4. The TSV has 18 rows, matching the non-identical pairs (6+5+6+1).
SOURCE: SW\SWEEP-REPORT.md:109-115; SW\sweep-mechanism-2026-09-26.tsv:1-19 (produced by SW\sweep_mechanism.py)

## 22. [report-s6-interpretation]
Report §6 interpretation:
- No traffic: the two rules are identical (D1).
- At 15 min and at x >= 600 s: both rules equal U (D2).
- At tight x (30-120 s): served counts differ by at most 6/864; C's promise always holds; M+'s promise is broken for 7.6-14.4% of riders; on M+'s own metric M+ is not consistently better (13.5% C vs 14.4% M+ at 30 s); M+ carries a recovery burden of 13-28% forced decisions and 5.6-9.4% frozen fleet.
- Defensible claim: no difference in service; the rules differ in whether the promise holds and in recovery burden.
SOURCE: SW\SWEEP-REPORT.md:117-134

## 23. [noworse-A1-trigger]
Amendment A1 was written after 108/156 jobs had finished. Rule (b) is triggered when M+-x has forced breaches and its completed set differs from C-x. Observed: W2 w08 had 366-419 forced breaches at x <= 120 and served 83 vs C's 85; W2 w17 had 492-527 and 77 vs 79. W1 w08 had forced breaches but identical sets. W1 w17 had forced breaches and different sets, but M+ served more there.
SOURCE: SW\SWEEP-AMENDMENTS.md:6-16; SW\logs\sweep-view-2026-09-26.txt:41-52

## 24. [noworse-implementation]
Rule (b) implementation:
- Code: ADR-077, commit 45f8026 on branch research/tier3-no-worse, worktree C:\Code\RideBound-noworse.
- Runner v2: C:\RideBoundData\research\runner-tier3-v2, manifest tree-sha256 ac251ef32a4865ea3bd3d8d87b4b1bcaccc4462a9b80160b4d205b8d474cff3f, 429 files. The v1 manifest tree is 5049f6d390a8...852c5cb, also 429 files.
- WP4 v2 differs from v1 only in commitmentRecovery: forced-reference-v1 -> no-worse-than-reference-v1.
- Output root: C:/RideBoundData/research/tier3-sweep-noworse-v1.
SOURCE: SW\SWEEP-AMENDMENTS.md:27-38; T3\runner-tier3-v2.sha256.tsv:1; T3\runner-tier3-v1.sha256.tsv:1; T3\configs\make_wp4_v2.log:1-3; SW\run_noworse.py:26-28

## 25. [git-worktrees]
Worktrees:
- E:/Code/RideBound 41a4e11 [main]; its last commit is 2026-09-04 'Add comprehensive tests for commitment and optimization features'.
- C:/Code/RideBound-noworse a90b4b7 [research/tier3-no-worse]. a90b4b7 'Record end-to-end A1 evidence for no-worse recovery (ADR-077, exploratory)' sits on top of 45f8026, and the branch tracks origin/research/tier3-no-worse at a90b4b7.
- E:/Code/RideBound-deadline 1ce15e9 [research/tier3-failure-aware].
- E:/Code/RideBound-py-baseline 8d1ea4d (detached).
SOURCE: git -C E:\Code\RideBound worktree list; git -C E:\Code\RideBound log -1; git -C C:\Code\RideBound-noworse log --oneline -6 and branch -vv --contains 45f8026

## 26. [noworse-jobs]
No-worse jobs: 22 treatments, i.e. every Mplus-x with forced > 0 in the sweep. That is x=30 in 7 cells (all drift cells except W5 w17), x=60 in 6 (W1, W2, W4), x=120 in 6 (W1, W2, W4), and x=300 in 3 (W1 w08, W1 w17, W2 w08). There are 6 controls: C-30 in W2 and W4 (both cells), Mplus-900-W2-w08 and Mplus-900-W4-w17. All 6 controls have identical fleet actions to (a): 707/707, 660/660, 771/771, 728/728, 720/720, 764/764.
SOURCE: SW\logs\noworse-analyze-2026-09-26.txt:1-28; SW\run_noworse.py:30-39; python read of noworse-jobs TSV (controlSameFleetActions, controlDecisions)

## 27. [noworse-per-job]
Per treatment, completed (b)/(a)/C, noWorseDecisions:
- x=120: W1w08 85/85/85 0; W1w17 79/82/79 1; W2w08 85/83/85 3; W2w17 79/77/79 4; W4w08 94/94/93 0; W4w17 92/92/92 0.
- x=30: W1w08 82/82/82 0; W1w17 79/80/79 1; W2w08 85/83/85 4; W2w17 79/77/79 4; W4w08 94/95/94 10; W4w17 89/86/89 5; W5w08 90/90/90 1.
- x=300: W1w08 87/87/87 0; W1w17 80/82/80 1; W2w08 86/86/86 0.
- x=60: W1w08 82/82/82 0; W1w17 79/81/79 1; W2w08 85/83/85 4; W2w17 79/77/79 4; W4w08 94/93/94 4; W4w17 90/87/90 2.
SOURCE: SW\logs\noworse-analyze-2026-09-26.txt:1-22 (produced by SW\noworse_analyze.py)

## 28. [noworse-totals]
Totals over the 22 treatments: served (b) 1874, (a) 1864, C 1873; (b) equals C in 21/22. There are 49 decisions with a forcedNoWorse witness and 50 forcedNoWorse breaches, against 5155 forcedReference breaches. Mean own-break A > x is (b) 0.1216 vs (a) 0.1226, reported as 12.2% vs 12.3%. Mean share C_r > x under M+(b) is 0.00149, reported as 0.15%.
SOURCE: python read of SW\noworse-jobs-2026-09-26.tsv (command output); SW\SWEEP-AMENDMENTS.md:44-48; SW\SWEEP-REPORT.md:147-151,168-179

## 29. [noworse-aggregate-table]
noworse aggregate over the 8 drift cells. Columns: x | completed C / M+(a) / M+(b) | M+(b) same decisions as C | M+(b) own break | M+(b) nonNorm | M+(b) frozen:
- x=30: 697/692/697 | 7/8 | 0.141 | 0.295 | 0.094
- x=60: 699/693/699 | 8/8 | 0.108 | 0.192 | 0.070
- x=120: 703/704/705 | 5/8 | 0.078 | 0.136 | 0.058
- x=300: 714/716/714 | 8/8 | 0.008 | 0.040 | 0.009
- x=600 and 900: 715/715/715 | 8/8 | 0 | 0 | 0
Report §7.1 reproduces this table, and adds the column 'C chấm theo luật M⁺' = 13.5/10.8/8.1/0.8/0/0%.
SOURCE: SW\logs\noworse-aggregate-2026-09-26.txt:1-7 (produced by SW\noworse_aggregate.py); SW\SWEEP-REPORT.md:159-166

## 30. [noworse-interpretation]
Report §7.2 interpretation:
- The service gap of (a) is a consequence of the recovery rule, not of the deadline rule (x=30: 697 = 697 vs (a) 692).
- At x=60, M+(b) and C make the same decisions in 8/8 cells, yet M+ records broken promises for 10.8% of riders and 19.2% non-normal decisions, while C keeps 100%.
- The three jobs that differ from C, as (b)/(a)/C: Mplus-120-W4-w08 94/94/93; Mplus-120-W4-w17 92/92/92 (same count, different actions); Mplus-30-W4-w17 89/86/89.
- (b) does not always raise service over (a): Mplus-120-W1-w17 has (a) 82 and (b) 79 = C.
SOURCE: SW\SWEEP-REPORT.md:168-190

## 31. [incident-A2]
Incident A2 (2026-09-25, about 23:03-23:16 local): code for (b) was edited inside the sweep worktree E:\Code\RideBound-deadline (8 src files, 5 tests files). Jobs failed with 'RuntimeError: repository content inventory drifted during the matrix run' (actual_fleetpy_medium_preflight.py:881) and had no summary.json. Response: the edits were saved to no-worse-v1-worktree-edits.patch (67,705 B), and the 13 files were restored byte-exact to 1ce15e9 (13/13 git hash-object matches). The 12 failed jobs were rerun into -rerun1 and no failed directory was deleted. The plan was to develop (b) only in a separate worktree after the sweep.
SOURCE: SW\SWEEP-AMENDMENTS.md:52-82; SW\rerun_failed.py:20,24-36; patch size from Get-ChildItem SW (67705)

## 32. [sweep-worktree-state-now]
E:\Code\RideBound-deadline is at HEAD 1ce15e9. git status --short lists 144 'M' entries with LF->CRLF warnings, but git diff --shortstat (with and without --ignore-cr-at-eol) is empty, so there is no content difference.
SOURCE: git -C E:\Code\RideBound-deadline log --oneline -3; status --short; diff --shortstat (command outputs)

## 33. [limitations-s8]
Report §8 limitations:
- One episode per cell, development cells only, no confidence intervals. W1-W4 are synthetic and W5 is the real day.
- W5 (12 Nov): the factor rises up to 17.6% in the morning window (2.797 at 08:00 -> 3.289 at 09:15) and falls 16% in the evening window (3.194 at 17:00 -> 2.673 at 19:00). M+ breaks its promise only at x=30 in the morning (2.2%, equal to C scored by the M+ rule), and 0% from x >= 60.
- M+(a) at x=60, per world (w08/w17): W1 12.2/12.3%, W2 20.5/29.9%, W4 7.5/5.7%, W5 0/0%.
- Hamburg data (CC BY 4.0) not run: it needs a preflight change because op_max_wait_time is fixed at 600 s, plus a converter and a rider-choice model.
- The windows run were already past the fast-rise phase: 7-9h on 12-16 Nov peaks +47-66% vs 8-10h +15-23%; max 15-min step 8.3-16.2% vs 3.7-7.1%; 7-9h demand 2396-2724 vs 2458-2757; coverage of the 96 nodes not checked.
- Per-rider drift on the real day: morning 2.2% > 30 s, 0% > 60 s, max 35.2 s; evening 0%, max 7.7 s. Synthetic: 12-32% > 30 s in W1/W2, up to 6-7 min in W1.
- The 7-9h window was not run. Panel A cell d20181114-s10-r1 was already seen in the T3.5/T3.6 smoke.
SOURCE: SW\SWEEP-REPORT.md:192-214

## 34. [limitations-verification]
Checks against source data:
- The 12 Nov factor CSV confirms 28800 -> 2.79695, 33300 -> 3.28940, 61200 -> 3.19413, 68400 -> 2.67299.
- My recomputation over 12-16 Nov gives a 7-9h peak rise of 0.478/0.544/0.656/0.652/0.469 with max step 0.106/0.134/0.162/0.126/0.083, and an 8-10h peak of 0.176/0.154/0.173/0.231/0.232 with max step 0.071/0.037/0.052/0.063/0.048. The 17-19h peak rise is only 0.000-0.030.
- C-30 maxA from the paired TSV: W5 w08 35161 ms and W5 w17 7680 ms.
SOURCE: Select-String on E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33.../Manhattan_2019_corrected/2018-11-12_tt_factors.csv; python recomputation (read-only) of *_tt_factors.csv; SW\sweep-paired-2026-09-26.tsv:62,68

## 35. [script-map]
Which script produced which output:
- sweep_analyze.py (M1-M8 per job, paired P) -> sweep-jobs-2026-09-26.tsv and sweep-paired-2026-09-26.tsv.
- show_sweep.py -> logs/sweep-view-2026-09-26.txt.
- sweep_aggregate.py -> logs/sweep-aggregate (report §4).
- sweep_predictions.py -> logs/sweep-predictions (§3).
- sweep_worlds.py (validity checks 1, 3, 4) -> logs/sweep-worlds-final.
- sweep_mechanism.py -> sweep-mechanism TSV (§5).
- noworse_analyze.py -> noworse-jobs TSV and logs/noworse-analyze.
- noworse_aggregate.py -> logs/noworse-aggregate (§7.1).
- split_noworse.py -> §4a (no saved log).
- per_world.py -> §4b (no saved log).
- why_similar.py -> §8 'why similar' (no saved log).
- run_sweep.py -> logs/driver-run-1.out.
- rerun_failed.py -> logs/rerun-driver-1.out.
- run_noworse.py -> logs/noworse-driver-1.out.
- test_sweep_analyze.py: 14 checks of sweep_analyze on pilot outputs.
SOURCE: docstrings SW\sweep_analyze.py:1-13, show_sweep.py:1-6, sweep_aggregate.py:1-7, sweep_predictions.py:1-5, sweep_worlds.py:1-8, sweep_mechanism.py:1-12, noworse_analyze.py:1-10, noworse_aggregate.py:1-7, split_noworse.py:1-2, per_world.py:1-3, why_similar.py:1-6, run_sweep.py:1-12, rerun_failed.py:1-8, run_noworse.py:1-11, test_sweep_analyze.py:1-4,81; output formats match e.g. show_sweep.py:13,29 and sweep_aggregate.py:21-23

## 36. [py-purposes]
One-line purpose of each .py:
- run_sweep.py: drives the 156-job sweep (world v1.1, runner-tier3-v1, AC power only, STOP file, never overwrites).
- rerun_failed.py: reruns only the inventory-drift failures into -rerun1.
- run_noworse.py: drives the 22 treatments + 6 controls with runner-tier3-v2 and wp4-tier3-v2.
- sweep_analyze.py: metrics M1-M8 and the paired table.
- show_sweep.py: compact per-cell view.
- sweep_aggregate.py: per-level totals over the drift cells.
- sweep_predictions.py: scores D1-D7 literally.
- sweep_worlds.py: world and scenario validity checks.
- sweep_mechanism.py: prune codes for riders served by only one rule.
- noworse_analyze.py: sweep metrics for the no-worse runs, plus forced-breach kinds and the control check.
- noworse_aggregate.py: M+(b) per level vs C and M+(a).
- split_noworse.py: splits M+(b) into real (W5) vs synthetic (W1, W2, W4) and checks that identical decisions give identical A>x.
- per_world.py: per-world served and break shares.
- why_similar.py: factor-file rises, exogenous drift of C-30 riders, decision structure.
- test_sweep_analyze.py: tests for sweep_analyze.
SOURCE: docstrings (same lines as script-map)

## 37. [tsv-purposes]
TSVs:
- sweep-jobs-2026-09-26.tsv: 156 rows, one per job (36 columns incl. M1-M7, decisions, output, scenarioSha256, wallSeconds).
- sweep-paired-2026-09-26.tsv: 72 rows (world x cell x level) comparing C vs M+ sets, common riders and sameAsU.
- sweep-mechanism-2026-09-26.tsv: 18 rows for the differing pairs.
- noworse-jobs-2026-09-26.tsv: 28 rows, rule (b) metrics plus a_*, C_M1_completed, breach kinds and control checks.
SOURCE: python header read of sweep-jobs TSV; SW\sweep-paired-2026-09-26.tsv:1-73; SW\sweep-mechanism-2026-09-26.tsv:1-19; SW\noworse-jobs-2026-09-26.tsv:1-29

## 38. [M5-column-semantics]
The M5_forcedBreaches column counts only breaches of kind forcedReference. In the (b) runs it therefore excludes the 50 forcedNoWorse breaches: noworse TSV M5 total 5155, so the true forced total in (b) is 5205. 'M+ bị ép (tỉ lệ quyết định)' in the report is M5_nonNormalShare, i.e. nonNormalCertificates / decisionsAcknowledged.
SOURCE: SW\sweep_analyze.py:119,121; SW\noworse_analyze.py:42-43; python sums of noworse TSV

## 39. [pilot-T3.7]
The T3.7 pilot report (no README exists in T3\pilot; the report is T3\T3.7-BAO-CAO-THI-DIEM.md):
- Run: 60/60 pass, 5 arms (U, C-30, V-30, M+-30, M-30) x 6 worlds x 2 cells, world v1, runner-tier3-v1, 11,469 s.
- H1 held: C-30 had 0 recovery in 12/12 and max decision-caused drop change 19.1 s.
- C-30 >= V-30 in 12/12, greater in 9/12, by 1-10 riders.
- The stop gate was triggered: V-30 and M-30 recover on the majority of decisions in 5/12 episodes, M+-30 in 2/12. Recovery options (a), (b) and (c) were left to the owner.
- World-switch lag of up to 265 s over all bins (149 s over common bins) and cross-arm skew up to 131 s led to world v1.1.
- Panel A cell d20181114-s10-r1 was seen in the smoke.
SOURCE: T3\T3.7-BAO-CAO-THI-DIEM.md:10-31,37-42,146-151,205-246

## 40. [pilot-table]
Pilot (world v1) served counts for U / C-30 / V-30 / M+-30 / M-30:
- Morning (sáng): W0 102/97/97/97/97, W1 87/82/80/82/79, W2 85/86/79/85/79, W3 108 all, W4 96/94/90/92/92, W5 92/90/87/90/89.
- Evening (tối): W0 99/95/95/95/95, W1 83/81/78/81/78, W2 79/79/69/78/69, W3 107/107/103/107/102, W4 92/87/86/86/85, W5 100/99/97/99/97.
SOURCE: T3\T3.7-BAO-CAO-THI-DIEM.md:120-133

## 41. [world-README]
World v1 is f(od,b) = base(b)*exp(L(od,b))*(1+S(od,b)) with 900 s bins, keyed SHA-256 common random numbers, FIFO integration and a 'current conditions' forecast, on a 96-node OD closure (not a street network). v1.1 (preflight_world_v1_1.py) wraps _next_physical_boundary so every arm switches exactly at bin x 900 s. Checks: 14 tests with 0 failures, 5/5 mutants caught; the v1.1 smoke passed 4/4 with a leakage check PASS (961 frames byte-identical). Runner v1 was published from 69512d3 with tree 5049f6d3...52c5cb and 429 files.
SOURCE: T3\world\README.md:5-16,68-69,92-110

# UNVERIFIED
- '12/12 -rerun1 jobs frame-identical to the failed partial runs' (SW\SWEEP-REPORT.md:31, SW\SWEEP-AMENDMENTS.md:80): no script or saved text log for this check exists in T3 outside per-job .log files (grep for '0da63eaf|trùng từng frame' matched only the two docs).
- '156/156 share repository inventory 0da63eaf…' (SW\SWEEP-REPORT.md:32): not in sweep-jobs TSV columns and no saved evidence file in T3.
- .NET 1025/1025 and two rounds of independent review with no blocker for ADR-077 (SW\SWEEP-AMENDMENTS.md:31): not checked (repo docs and tests not read).
- Runner v2 'publish từ 45f8026 với cây sạch' (SW\SWEEP-AMENDMENTS.md:32): only the manifest tree hash was checked.
- Which 3 treatment jobs differ in fleet actions from C (Mplus-120-W4-w08, Mplus-120-W4-w17, Mplus-30-W4-w17; SW\SWEEP-REPORT.md:170-173): the per-level counts 7/8, 8/8, 5/8, 8/8 in the noworse-aggregate log are consistent with 19/22, but no saved log lists the per-job identities.
- The per-cell check 'wherever (b) makes the same decisions as C, A>x equals C's, no mismatch' (SW\SWEEP-REPORT.md:88): produced by split_noworse.py but no saved output.
- 7-9h vs 8-10h demand counts 2,396-2,724 vs 2,458-2,757 requests in a sample_10_1 file (SW\SWEEP-REPORT.md:209): not recomputed; the demand file was not read.
- SWEEP-REPORT §5 claim that the other 5 of 7 riders were pruned 'chỉ vì cửa sổ đón hoặc thời gian đi tối đa': the TSV does not record which codes applied.
- That thesis tables bang:quet / bang:quetb use the §4a split (SW\SWEEP-REPORT.md:73): the thesis source was not read.
- Plan D2 basis figures from pilot v1 (max A under U 498.7 s, max per-rider C 331.9 s; SW\SWEEP-PLAN.md:77): the source script output (pilot_lateness_vs_initial.py) was not read.
- ADR-077 text and RideBound docs/18 status entries: not read (outside this slice and the main-tree restriction).
# WARNINGS
- D7 reporting is incomplete. The report says only 'Sai: 5/8, 5/8, 7/8' (SW\SWEEP-REPORT.md:46), which are the 'M+ <= C' counts. The sealed D7 also requires M+ A>x > 0 in all 8 drift cells, and that clause failed as well: 7/8, 6/8, 6/8 (SW\logs\sweep-predictions-2026-09-26.txt:7; sweep_predictions.py:64). At x=120 the '<=' clause passed (7/8 >= 6), so the x=120 failure comes only from the '>0' clause (both W5 cells are 0). The report does not say this.
- Overstatement: §6.3 says the small service gap at tight levels 'biến mất' with rule (b), and §7.2.1 says 'M⁺ phục vụ đúng như C' (SW\SWEEP-REPORT.md:130,184-185). At x=120, M+(b) = 705 vs C = 703 (SW\logs\noworse-aggregate-2026-09-26.txt:4). Exact equality holds only at x = 30, 60, 300 and >= 600.
- §5 mechanism wording goes beyond the data. sweep_mechanism.py computes onlyM_otherCodesOnly = onlyM - blockedByCBudget (sweep_mechanism.py:88). That includes riders with no prune code at all, so '5 riders excluded only by pickup window or max ride time' (SW\SWEEP-REPORT.md:112-113) is not established by the saved TSV.
- §8 cites why_similar.py for figures the saved script does not compute. The report attributes to it the 7-9h peak rise of 47-66%, the max 15-min step of 8.3-16.2% vs 3.7-7.1%, and the demand counts (SW\SWEEP-REPORT.md:205-211). The saved why_similar.py part A computes only the 60/120-min max rise at any start and the 08-10 / 17-19 window peaks (why_similar.py:31-37). My independent recomputation confirms the factor numbers are correct; the demand counts remain unverified.
- No saved output logs exist for split_noworse.py (§4a), per_world.py (§4b) or why_similar.py (§8). Every §4a and §4b number was recomputed here from the saved TSVs and logs and matches.
- Mixed bases can confuse a reader. The §4b burden paragraph (15,528 decisions, 3,789 non-normal = 24%) is pooled over the 22 rule-(b) treatment jobs, while the §4b table's promise-break columns are rule (a), and §4's 'bị ép 28,1%' is a mean over 8 cells for rule (a) at x=30 (SW\SWEEP-REPORT.md:92,104-107,54).
- §4a says 'Nhóm thật: không đổi gì' under rule (b) (SW\SWEEP-REPORT.md:86). Served count and A>x are unchanged (90; 0.0222), but the non-normal share of Mplus-30-W5-w08 changed from 0.238 (a) to 0.2324 (b) (sweep-view line 95; noworse TSV line 14).
- In (b) runs, M5_forcedBreaches counts only forcedReference (sweep_analyze.py:121), so 'M+ forced breaches' totals from that column understate the forced total by the 50 forcedNoWorse breaches (5155 vs 5205).
- T3\world\README.md is stale. Line 3 says 'logic xong, chưa tích hợp' and line 75 says v1.1 is 'CHƯA dùng cho run nào', but the sweep ran entirely on v1.1 (SW\SWEEP-PLAN.md:25; run_sweep.py:31).
- The noworse worktree HEAD is a90b4b7, one commit after 45f8026 (the commit the amendments name for Runner v2). The newer commit only records A1 evidence, per its message. Keep this in mind when citing commits.
- The sweep worktree E:\Code\RideBound-deadline shows 144 'M' entries in git status, but the content diff is empty (line-ending normalization only). Do not treat it as dirty content, and do not 'clean' it.
- There is no pilot README; the pilot report is T3\T3.7-BAO-CAO-THI-DIEM.md. The pilot used world v1, not v1.1, so pilot served counts (e.g. M+-30 W4 sáng 92) differ from sweep counts (Mplus-30 W4 w08 95). They must not be mixed.
- Hamburg data has not been run, and neither has the 7-9h window (SW\SWEEP-REPORT.md:203-213). No result in these files proves any '> X%' advantage in served riders. The defended claim is 'no service difference; C always keeps its promise (0% broken); M+ breaks it for 7.6-14.4% (all 8 drift cells) or 10.1-18.8% (synthetic only) at x = 30-120 s, with 13-28% forced decisions'.