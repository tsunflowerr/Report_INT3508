# feasibility

## 1. [A-config-diff]
V-30 differs from C-30 (= byte copy of base wp14-c1-h6-reference-v1.json, sha256 d6124f3f…8beb) in exactly one key: .policies[0].budgetBasis decisionInduced -> customerVisible; drop_eta_total_ms hardLimit stays 30000.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\configs\make_configs_t3.log:1,4-6; V-30.json:6,23; C-30.json:6,23; make_configs_t3.py:69-83,89

## 2. [A-config-diff]
M-30 differs from C-30 in three keys: drop_eta_total_ms hardLimit removed, dropEtaDeadlineSlackMs=30000 added, dropEtaDeadlineTwoSided=true added (budgetBasis stays decisionInduced). Mplus-30 is the same minus dropEtaDeadlineTwoSided.
SOURCE: make_configs_t3.log:7-13; M-30.json:6,17-23,98-99; make_configs_t3.py:80-82,90-91

## 3. [A-config-diff]
Arm configs for V-30/60/120 and M-30/60/120 already exist in tang3/configs (written by make_configs_t3.py); the sweep generator make_configs_sweep.py only produced U, C-x, Mplus-x (x in 30..900).
SOURCE: Get-ChildItem tang3\configs output; make_configs_t3.py:86-91; make_configs_sweep.py:28-31

## 4. [A-wp4]
wp4-tier3-v2.json differs from wp4-tier3-v1.json only at commitmentRecovery forced-reference-v1 -> no-worse-than-reference-v1 (sha256 v1 d132e9d3…, v2 66e9b592…); both keep lateBoarding record-v1 and policyId ridebound-hard-vector.
SOURCE: make_wp4_v2.log:1-3; wp4-tier3-v1.json:3,7-8; wp4-tier3-v2.json:7

## 5. [A-runner-parse]
Runner maps commitmentRecovery 'no-worse-than-reference-v1' to (forcedReference=true, forcedNoWorse=true) and rejects recovery unless solver-backed C1/C2 policy.
SOURCE: C:\Code\RideBound-noworse\src\RideBound.Runner\Configuration\Wp4RunnerConfiguration.cs:51-58,331-352

## 6. [A-visible-basis]
No-worse handles the visible basis without extra code: the charged vector is Visible when policy.BudgetBasis != DecisionInduced, both for the candidate (lines 512-514) and for the kept-route reference (779-781); a budget overrun is exempted only if every budget witness has a kept-route witness on the same dimension with witness.After <= kept.After (AllowsBudget 814-817, applied at 537-539).
SOURCE: C:\Code\RideBound-noworse\src\RideBound.Application\Commitments\CommitmentDecisionValidator.cs:512-514,537-539,779-781,814-817

## 7. [A-two-sided]
Two-sided deadline: CommitmentLockEvaluator emits deadline_cap when shift > slack and, if DropEtaDeadlineTwoSided, deadline_floor when -shift > slack. No-worse AllowsLock exempts cap only if kept route also has cap and candidate DropEta <= kept DropEta; floor only if kept route also has floor and candidate DropEta >= kept DropEta; phase locks never exempted.
SOURCE: C:\Code\RideBound-noworse\src\RideBound.Domain\Commitments\CommitmentLockEvaluator.cs:14-17,186-197; CommitmentDecisionValidator.cs:802-812,475-478

## 8. [A-no-worse-scope]
IsForcedNoWorse applies only when context.ForcedNoWorse, the vehicle is named forced-reference, and candidate route != reduced route; a kept (unchanged) route stays ForcedReference; unchanged projection records ForcedReference kind.
SOURCE: CommitmentDecisionValidator.cs:418-442,607-616,722-745

## 9. [A-no-worse-scope]
Assessor re-validates every validator-rejected candidate of a forced vehicle with noWorse=true after the forced no-op is accepted; flag reaches validator from RunnerSession via SolverPolicyOptions.ForcedNoWorseRecovery.
SOURCE: C:\Code\RideBound-noworse\src\RideBound.Algorithms\Commitments\HardVectorCandidateAssessor.cs:257-319,441-456; src\RideBound.Runner\Protocol\RunnerSession.cs:970-971

## 10. [A-tests]
Unit tests exist for visible basis and two-sided floor under no-worse: No_worse_recovery_under_the_visible_basis_allows_no_more_than_the_kept_overrun (line 421) and No_worse_recovery_under_a_two_sided_deadline_compares_on_the_floor_side (line 472); plus keeps/rejects/never-exempt/unchanged/collect-all/named-vehicle tests at 351,379,400,455,507,537.
SOURCE: C:\Code\RideBound-noworse\tests\RideBound.Application.Tests\Commitments\CommitmentDeadlineValidatorTests.cs:351,379,400,421-452,455,472-504,507,537

## 11. [A-tests]
ADR-077 records untested cases: two late riders on one vehicle; phase lock plus deadline; multi-dimension budget; C2 under no-worse; the 'reference is null' branch. End-to-end A1 evidence covered only Mplus-x treatment and C-30/Mplus-900 controls (22+6 jobs), i.e. neither visible basis nor floor side was exercised end-to-end.
SOURCE: C:\Code\RideBound-noworse\docs\18-status-and-decision-log.md:5110-5121,5133-5134; tang3\sweep\SWEEP-AMENDMENTS.md:35-38

## 12. [A-motivation]
In the T3.7 pilot (forced-reference-v1) V-30 and M-30 recovered at the majority of decisions in 5/12 episodes each; gate 'recovery does not swallow most of the trajectory' FAILED for V-30 and M-30.
SOURCE: tang3\T3.7-BAO-CAO-THI-DIEM.md:21,212; tang3\pilot\independent\RESULT.md:52-57

## 13. [A-treatment-set]
Pilot (a) forcedBreaches for V-30: W0 0/0, W1 372/381, W2 628/674, W3 132/333, W4 618/578, W5 325/228 (w08/w17); M-30: W0 0/0, W1 374/375, W2 610/662, W3 137/267, W4 476/325, W5 206/182. So forced>0 in 10/12 episodes per arm; W0 (both cells) is the natural no-forced control.
SOURCE: tang3\pilot\pilot-table-final-2026-09-25.tsv, column forcedBreaches (Select-String ^(V-30|M-30|C-30) output)

## 14. [A-comparability]
Pilot V-30/M-30 outputs are not a valid (a) baseline for a new (b) run: pilot used world wrapper v1 (preflight_world.py), runner-tier3-v1, repository inventory 9a003f43…(60/60 jobs); sweep and no-worse runs used wrapper v1.1 and inventory 0da63eaf…(sweep 156/156, no-worse 28/28). The sweep table contains no V- or M- arms (families U 12, C 72, Mplus 72). Only one V-30 v1.1 (a) run exists: tier3-world-v11-smoke\v11-V-30-W4.
SOURCE: run_pilot.py:34; run_sweep.py:31,34; summary.json repositoryInventorySha256 grouping command output; Import-Csv sweep-jobs-2026-09-26.tsv group-by-family output; SWEEP-REPORT.md:32; Get-ChildItem tier3-world-v11-smoke

## 15. [A-comparability]
World switch timing alone (v1 vs v1.1) changed the C-30 minus V-30 gap in W4 morning from +4 to +2 riders, same magnitude as the effects.
SOURCE: tang3\world\README.md:112-117

## 16. [A-launch]
Job launch pattern: PYTHON E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B <preflight wrapper> --label --fleetpy-root E:/RideBoundData/wp7/FleetPy-1.0.2 --runner-root --dotnet 'C:/Program Files/dotnet/dotnet.exe' --commitment-config configs/<arm>.json --wp4-config --scenario/--derivative-manifest/--normalization-report/--selection-frame <fixture>/... --driver benchmarks/scenarios/wp14-development/<cell>.driver.json --output --repeats 1 --master-seed 7; cwd E:/Code/RideBound-deadline; env RB_WORLD_CONFIG=<world json>, PYTHONDONTWRITEBYTECODE=1, PYTHONIOENCODING=utf-8.
SOURCE: tang3\pilot\run_pilot.py:27-45,100-118,128-133

## 17. [A-launch]
run_sweep.command swaps the preflight to world/preflight_world_v1_1.py and output root E:/RideBoundData/research/tier3-sweep-v1; run_noworse.command further swaps --label to <job>-nw, --runner-root C:/RideBoundData/research/runner-tier3-v2, --wp4-config configs/wp4-tier3-v2.json, --output C:/RideBoundData/research/tier3-sweep-noworse-v1/<job>.
SOURCE: tang3\sweep\run_sweep.py:29-32,63-68; tang3\sweep\run_noworse.py:26-29,52-58

## 18. [A-launch]
Safety: WORKERS=6 (ThreadPoolExecutor); job skipped if output dir exists; STOP file (sweep/STOP for sweep and no-worse, pilot/STOP for pilot) defers new jobs; may_start_job requires AC line or RB_ALLOW_BATTERY_MIN_PERCENT; keep_awake uses SetThreadExecutionState(ES_CONTINUOUS|ES_SYSTEM_REQUIRED) around the pool; logs opened with mode 'x'; missing-input check for runner dll, WP4, configs, worlds, fixtures before run.
SOURCE: run_pilot.py:40-42,73-87,121-137,151-172; run_sweep.py:32,71-86,101-121; run_noworse.py:61-77,91-107

## 19. [A-launch]
run_noworse.jobs selects treatment from the sweep table (family == Mplus and M5_forcedBreaches > 0) plus fixed CONTROLS; this cannot select V/M arms, so a V/M driver needs its own job list.
SOURCE: run_noworse.py:30-39

## 20. [A-launch]
Current state: runner-tier3-v2 dll present at C:\RideBoundData\research\runner-tier3-v2; runner-tier3-v1 dll present at E:\RideBoundData\research\runner-tier3-v1; no STOP file in sweep/ or pilot/.
SOURCE: Test-Path command output (True, True, False, False)

## 21. [A-cost]
No-worse jobs took 836-1216 s each (returncode 0, 28/28); each output is 77-92 MB, 2.26 GB total for 28 jobs. Pilot V-30/M-30 wallSeconds 965-1598 s.
SOURCE: first lines of tang3\sweep\logs-noworse\*.log; size command on C:\RideBoundData\research\tier3-sweep-noworse-v1; pilot-table-final-2026-09-25.tsv wallSeconds

## 22. [A-cost]
Free space now: C: 103.8 GB, E: 41.8 GB (policy floor E >= 40 GB, C >= 50 GB), so new outputs should go to C: as the no-worse runs did.
SOURCE: Get-PSDrive command output; SWEEP-AMENDMENTS.md:37

## 23. [A-analysis-tools]
sweep_analyze.job_row is generic (family = arm prefix, level = int suffix) but its paired section hardcodes C-x vs Mplus-x; noworse_analyze.py hardcodes run_noworse.jobs and C_M1 from C-<level>; forced_details() and pilot_analyze.fleet_decisions are reusable for V/M.
SOURCE: tang3\sweep\sweep_analyze.py:37,80,178-188; tang3\sweep\noworse_analyze.py:25-44,58-80

## 24. [A-integrity]
Preflight hashes the Git-visible inventory of E:/Code/RideBound-deadline (git ls-files --cached --others --exclude-standard, on-disk bytes) before and after each job and fails with 'repository content inventory drifted' if it changes; an optional --expected-repository-inventory-sha256 fails fast at start. The drivers do not pass it today.
SOURCE: E:\Code\RideBound-deadline\simulators\fleetpy-ridebound\actual_fleetpy_medium_preflight.py:740-782,836-846,872-884,934; run_pilot.py:100-118

## 25. [A-integrity]
E:\Code\RideBound-deadline HEAD 1ce15e9 and it has 144 'M' entries in git status, all with mtime 2026-09-24T00:04:05 (before pilot/sweep), so they are part of the hashed state 0da63eaf…; they must not be touched.
SOURCE: git -C E:\Code\RideBound-deadline log -1 and status --short + LastWriteTime command output

## 26. [A-steps]
Concrete steps A: (1) write a new driver mirroring run_noworse.py with jobs arms {V-30, M-30} x worlds W0-W5 x cells d20181112-s10-r1-w08/w17, in TWO variants under wrapper v1.1: (a) runner-tier3-v1 + wp4-tier3-v1, (b) runner-tier3-v2 + wp4-tier3-v2, new OUT_ROOTs on C:, new log dirs, new labels; (2) seal a plan/prediction file (as SWEEP-PLAN.sha256) before any job; (3) optionally pass --expected-repository-inventory-sha256 0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe; (4) 48 jobs ~ 48 x ~1100 s / 6 workers ~ 2.5 h, ~4 GB on C:; (5) analyze with sweep_analyze.job_row, pair against C-30 from tier3-sweep-v1 (same wrapper and inventory), W0 (b) fleet actions must equal (a), count forcedNoWorse witnesses/breaches, v/e/p audit; (6) independent re-check and report both (a) and (b).
SOURCE: derived from run_noworse.py:26-107, run_sweep.py:29-86, pilot-table forcedBreaches, SWEEP-AMENDMENTS.md:17-23 (A1 method), noworse log durations

## 27. [B-panel]
Development grid wp14-development-panel-v1: 16 cells, days 2018-11-12/13, sample_10_1..4, windows w08 28800-36000 and w17 61200-68400, travelFactorAtSeconds 0, requestTarget 108, vehicleCount 8, maximumNodeCount 96, capacity 4, pickupWindowMs 600000, maximumRideTimePermille 1500, drainDurationMs 7200000, WP14 selection/pseudonymization labels, policy wp6-synthetic-policy-overlay-v1.
SOURCE: E:\Code\RideBound-deadline\benchmarks\scenarios\wp14-development\grid-v1.json:2-22,90-91; docs\benchmarking\wp14-004-development-panel-2026-08-24.md:16-26

## 28. [B-panel]
grid-v1.json is pinned: its sha256 1741f8e7…c20e5 is recorded in the wp14-004 evidence summary and freeze tooling reads it; a w07 grid must be a new manifest file with a new gridId, not an edit of grid-v1.json.
SOURCE: docs\benchmarking\evidence\wp14-004-development-panel-v1-summary.json (gridManifestSha256); simulators\fleetpy-ridebound\wp14_freeze.py:298,339

## 29. [B-normalizer]
Cells are materialized by tools/RideBound.Wp6Normalize: 'normalize --cache <abs> --repository <root> --accept-license CC-BY-4.0 --grid <manifest>'; for each cell it calls FleetPyManhattanNormalizer with the cell's window/target fields and writes 7 files into <repository>/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/<gridId>/<cellId>, refusing to overwrite different bytes. Documented invocation form: dotnet run --project tools/RideBound.Wp6Normalize -c Release -- normalize --cache E:\RideBoundData\wp6 --repository ... .
SOURCE: E:\Code\RideBound-deadline\tools\RideBound.Wp6Normalize\Program.cs:11-13,57-126,182-206,255-281,322-378; docs\benchmarking\wp6-012-public-medium-evidence-2026-08-12.md:62-70,103; docs\benchmarking\wp6-013-adversarial-closure-evidence-2026-08-12.md:89

## 30. [B-normalizer]
A 25200-32400 window passes the normalizer's configuration validation (start >= 0, end > start, end <= 86400); requests outside [start,end) are excluded as source.outside-window.
SOURCE: src\RideBound.Benchmarking\Normalization\FleetPyManhattanNormalizer.cs:333-338,575-609

## 31. [B-node-pool]
The 96-node pool is chosen per cell from the eligible (in-window) demand: seed pair = most frequent OD pair, then greedy marginal coverage with HMAC tie-breaks; the 108 requests are the HMAC-ranked eligible records with both endpoints in the pool. Failure codes: source.insufficient-eligible-records and source.node-cap-prevents-target. So coverage for a new window is unknown until the normalizer runs.
SOURCE: FleetPyManhattanNormalizer.cs:104-125,647-757

## 32. [B-node-pool]
Selection rank HMAC(key,'RideBound.Wp6.SourceSelection.v1', artifactSha, demandMemberPath, ordinal) does not depend on the window, so with the same WP14 selection label the 08:00-09:00 requests have identical ranks in w07 and w08 cells of the same sample file.
SOURCE: FleetPyManhattanNormalizer.cs:627-631,653-663

## 33. [B-demand-counts]
Raw request rows in 07:00-09:00: 2018-11-12 r1..r4 = 2073, 2057, 1981, 1995; 2018-11-13 r1..r4 = 2886, 2674, 2736, 2759. Rows in the shared 08:00-09:00 hour: 1121,1084,1062,1153 (11-12) and 1518,1390,1417,1433 (11-13). For w08 the recorded eligibleRecordCount equals the raw window count for all 8 cells (e.g. 2286, 2175, 2167, 2256, 2767, 2640, 2755, 2702).
SOURCE: Import-Csv count command over E:\RideBoundData\wp6\extracted\sha256\d9\d9e86f33…\FleetPy_Manhattan\demand\Manhattan_2018\matched\Manhattan_2019_corrected\2018-11-1{2,3}_sample_10_{1..4}.csv; wp14-004-development-panel-v1-summary.json developmentCells

## 34. [B-traffic]
Measured factor ratio to window start (15-min rows): 2018-11-12 w07 rises to 1.478 (base 2.167 at 25200), w08 max 1.176, w17 falls to 0.837; 2018-11-13 w07 rises to 1.544 (base 2.516), w08 max 1.154, w17 falls to 0.868. A row exists exactly at 25200 on both days.
SOURCE: Import-Csv ratio command over ...\networks\Manhattan_2019_corrected\2018-11-1{2,3}_tt_factors.csv; SWEEP-REPORT.md:197-213

## 35. [B-fixtures-location]
Development fixtures live git-tracked inside the worktree: E:\Code\RideBound-deadline\benchmarks\fixtures\wp6\public\fleetpy-manhattan-v1\wp14-development-panel-v1\<cell>\ (7 files each); E:\RideBoundData contains only run outputs with these cell names (deadline-v1, tier3-pilot-v1, ...), not fixtures. Drivers are in benchmarks\scenarios\wp14-development\<cell>.driver.json.
SOURCE: git -C E:\Code\RideBound-deadline ls-files output; Get-ChildItem -Recurse -Depth 5 on E:\RideBoundData output; run_pilot.py:38-39

## 36. [B-fixtures-location]
The preflight accepts scenario/driver paths outside the repository (it only checks the driver's sourceScenarioContentSha256 and declared cardinality); precedent: window/run_window.py uses E:/RideBoundData/wp14/wide-window-fixture and 40/40 wide-window-v1 jobs have status pass.
SOURCE: actual_fleetpy_medium_preflight.py:801-835; ridebound-scratchpad\window\run_window.py:47,108-121; summary.json status count command on E:\RideBoundData\wp14\wide-window-v1

## 37. [B-driver]
Driver files differ per cell only in scenarioId, sourceScenarioContentSha256 and sourceScenarioHash; expectedRequestCount 108, expectedVehicleCount 8, expectedNodeCount 96, expectedDirectedArcCount 9120 are fixed. No driver generator was found in the repo (the string exact-source-arrival-event-clock-v1 appears only in driver JSONs).
SOURCE: benchmarks\scenarios\wp14-development\d20181112-s10-r1-w08.driver.json:3-5,30-33; d20181112-s10-r1-w17.driver.json:3-5; Grep result

## 38. [B-normalizer-identity]
normalizerSourceSha256 (34517a83…4d90 in the w08 fixture) hashes the 5 files in src/RideBound.Benchmarking/Normalization of the --repository tree; no commit between 1ce15e9 and a90b4b7 touched Normalization, tools/RideBound.Wp6Normalize or simulators, and C:\Code\RideBound-noworse git status is clean.
SOURCE: src\RideBound.Benchmarking\Normalization\FleetPyNormalizerSourceIdentity.cs:9-43; fixture normalization-report.json; git log 1ce15e9..a90b4b7 -- paths (empty output); git status of noworse (empty)

## 39. [B-audit]
Leakage audit tool wp14_development_panel_audit.py compares a development grid vs frozen grids on 7 axes (demandMemberPath, travelFactorMemberPath, sourceLocalDate, sourceWindow=date+start-end, scenarioId, cellId, scenarioHash); it requires generated fixtures under <repository>/benchmarks/fixtures/.../<gridId>/<cell>; invocation --repository --development --frozen (repeatable) --output (exclusive create). Original frozen grids: wp9-confirmatory/grid-v2.json (wp9-confirmatory-fixed-panel-v2) and grid-v3-veh4.json.
SOURCE: simulators\fleetpy-ridebound\wp14_development_panel_audit.py:27-35,52-94,97-125,166-183; benchmarks\scenarios\wp9-confirmatory\grid-v2.json:2, grid-v3-veh4.json:2; wp14-004 doc:45-65

## 40. [B-audit]
The existing audit does not compare development cells with each other, so w07 vs w08 overlap (same demandMemberPath, overlapping hour 08:00-09:00, possibly identical selected requests) would pass it; an extra internal-overlap check is needed.
SOURCE: wp14_development_panel_audit.py:97-125; FleetPyManhattanNormalizer.cs:653-663

## 41. [B-world]
W5 world files: sigma 0, shockRate 0, base {day, exponent 1, windowStart}; W5-w08.json and W5-w17.json both hard-code day 2018-11-12. With sigma 0 and shockRate 0 the factor is exactly base(b), anchored so bin 0 = 1.
SOURCE: tang3\pilot\worlds\W5-w08.json, W5-w17.json (Get-Content output); tang3\world\world_v1.py:64,71,79-81,115-120

## 42. [B-world]
windowStart 25200 does NOT work unchanged: preflight_world.py ALLOWED_WINDOW_STARTS = (28800, 61200) and measured_base raises SystemExit('unsupported window start') otherwise; preflight_world_v1_1.py calls preflight_world.load_world and inherits the restriction. Other checks would pass (factor row at the window start exists; 24 bins).
SOURCE: tang3\world\preflight_world.py:56-57,67-93,108-111; tang3\world\preflight_world_v1_1.py:36,66

## 43. [B-world]
run_pilot.world_file picks W5 by window only (W5-<cell[-3:]>.json), so any d20181113 cell would get the 2018-11-12 factors; w07 needs its own W5 files per (day, window) and a new world_file.
SOURCE: run_pilot.py:49-51; W5-w08.json content

## 44. [B-world-leak]
World wrappers were leak-checked by an end-to-end smoke: two worlds identical to bin 3 must give byte-identical frames before 3600 s (v1: 1051 frames; v1.1: 961 frames, first diff at 3,600,000 ms, PASS). A new wrapper version for 25200 would need the same smoke plus unit/mutation tests like test_preflight_world_v1_1.py (14 checks) and mutate_preflight_world_v1_1.py (5/5).
SOURCE: tang3\world\README.md:51-58,97-111

## 45. [B-prior]
The 07:00-09:00 window has not been run; SWEEP-REPORT says 'two rules equal on real traffic' holds only for the two windows run, and 96-node coverage for 7-9h is unchecked.
SOURCE: tang3\sweep\SWEEP-REPORT.md:205-213

## 46. [B-steps]
Concrete steps B: (1) new grid manifest (new gridId) with 8 cells d2018111{2,3}-s10-r{1..4}-w07, sourceWindowStartSeconds 25200, End 32400, other fields copied from grid-v1.json; decide whether to reuse WP14 selection/pseudonymization labels; (2) run Wp6Normalize --grid from a worktree other than E:\Code\RideBound-deadline (e.g. a clean one) with --cache E:\RideBoundData\wp6; confirm per cell requestCount 108, nodeCount 96, directedArcCount 9120 and normalizerSourceSha256 34517a83…; (3) place fixtures and hand-written drivers (w08 template + 3 changed fields) outside the deadline worktree; (4) rerun wp14_development_panel_audit.py vs grid-v2.json and grid-v3-veh4.json with --output to a new receipt, plus a new w07-vs-wp14-development-panel-v1 overlap check on selected ordinals (selection-frame.json) and time overlap; (5) new world wrapper (v1.2) that allows 25200 without editing preflight_world.py, tests + mutation + leak smoke; W5 files per (day, window); (6) driver for W5-only jobs on the 8 w07 cells for the chosen arms.
SOURCE: derived from Program.cs:57-126, grid-v1.json, wp14_development_panel_audit.py:166-183, preflight_world.py:56-70, run_pilot.py:49-51, README.md:92-111

## 47. [C-calibration]
No conformal/calibration/gamma code exists: grep (?i)conformal|calibrat found no *.py in E:\Code\Report_INT3508\ridebound-scratchpad and no *.py/*.cs in E:\Code\RideBound-deadline or C:\Code\RideBound-noworse; (?i)\bgamma\b|γ found nothing in scratchpad *.py.
SOURCE: Grep calls (No files found / No matches)

## 48. [C-design]
H3/RQ-T3b design text only: for a frozen C policy, episode-level conformal gamma with P(V_T <= beta + gamma) >= 1 - alpha on a test set, useful only if beta + gamma < a pre-fixed threshold (proposed half the 90th percentile of V_r under U on development); episode = (day, demand sample, window, world seed); alpha and usefulness threshold still owner decisions. H3 not measured in pilot, belongs to T3.8.
SOURCE: tang3\T3.1-KHOA-CAU-HOI.md:29-31,39,57-59,91,95; tang3\T3.7-BAO-CAO-THI-DIEM.md:202

## 49. [C-design]
Split rule: selection/calibration/test (T3.8, T3.9) must use other episodes (different world seed, preferably different cell), fixed in pre-registration after the pilot; Panel A (days 14-18) not to be touched; the Panel A cell d20181114-s10-r1 was seen in T3.5/T3.6 smoke and must be excluded from test or declared.
SOURCE: tang3\T3.7-KE-HOACH-THI-DIEM.md:9-12; tang3\T3.7-BAO-CAO-THI-DIEM.md:239-246

## 50. [C-data]
Per-rider drop V = sum |z_t| (z = p - v) and E2/CVaR95 are specified and computed per episode by existing tools (METRICS-SPEC, sweep_analyze job_row columns M2_E2, M2_cvar95V_ms); Tier-3 pilot and sweep used only cells d20181112-s10-r1-w08/w17, so r2-r4 and 2018-11-13 development cells are unused by Tier 3.
SOURCE: tang3\evidence\METRICS-SPEC.md:48-60,75-76,84-85; sweep-jobs-2026-09-26.tsv header; run_pilot.py:45; run_sweep.py:35

## 51. [C-data]
Tier 2 runs (E:\RideBoundData\research\deadline-v1) already used all 16 development cells (6 runs each) and Panel A cells d20181114..18-s10-r1..4 (10-11 runs each).
SOURCE: Get-ChildItem E:\RideBoundData\research\deadline-v1 grouped by cell (command output)

## 52. [C-steps]
Concrete steps C: owner fixes V_T definition, alpha, usefulness threshold and split before any calibration data; freeze C (config + runner + wrapper); generate calibration and test episodes on distinct world seeds and cells (development cells other than d20181112-s10-r1, or new w07 cells); write conformal quantile code (split-conformal over episode scores) with tests and an independent verifier; report coverage and usefulness separately without trimming gamma.
SOURCE: derived from T3.1-KHOA-CAU-HOI.md:29-31,57-59,95 and T3.7-KE-HOACH-THI-DIEM.md:11-12,72-84

# UNVERIFIED
- Whether each w07 cell reaches 108 selected requests inside a 96-node pool (source.node-cap-prevents-target possible); only raw in-window counts (1981-2886) were computed.
- Whether all raw w07 rows are eligible (strongly connected endpoints); for w08 eligible == raw, so it is likely but not computed for w07.
- Whether Wp6Normalize needs network access when the verified archive is already in E:\RideBoundData\wp6 (VerifiedDatasetDownloader.AcquireAsync not read).
- Whether running the normalizer from another worktree reproduces normalizerSourceSha256 34517a83…; expected because no commits touched Normalization after 76aafae, but the hash was not recomputed.
- Whether dotnet build output (bin/obj) of the worktree used is git-ignored and so outside the preflight inventory; .gitignore not read.
- Whether E:\Code\RideBound-deadline inventory still equals 0da63eaf… today; not recomputed (could be checked read-only via _repository_inventory_sha256 logic, actual_fleetpy_medium_preflight.py:740-782).
- Whether a new wrapper that reassigns preflight_world.ALLOWED_WINDOW_STARTS before load_world is enough; inferred from measured_base reading the module global at call time (preflight_world.py:69), not tested.
- Whether V-30/M-30 no-worse runs pass end-to-end; visible basis and floor side were never exercised by the A1 FleetPy jobs.
- Whether keep_awake (ES_SYSTEM_REQUIRED) prevents sleep on lid close or on the power plan's hibernate settings.
- Exact definition of V_T (episode score) for H3: T3.1 names it but does not define it (max, quantile or sum of per-rider V).
# WARNINGS
- E: has 41.8 GB free against a 40 GB floor; put all new outputs on C: (103.8 GB free), as run_noworse.py did.
- Never edit, build, or write fixtures inside E:\Code\RideBound-deadline while jobs run: the preflight fails with inventory drift (SWEEP-AMENDMENTS.md A2, 12 jobs lost once). Wp6Normalize writes into <--repository>/benchmarks/fixtures, so running it against that worktree would change the inventory away from 0da63eaf….
- Do not reuse pilot V-30/M-30 outputs as the (a) baseline: different wrapper (v1), runner v1 and inventory 9a003f…; a fair (a) vs (b) needs both reruns under wrapper v1.1.
- preflight_world.py:56 rejects windowStart 25200; preflight_world.py and preflight_world_v1_1.py must stay unmodified because the pilot and sweep ran on them; add a new wrapper version instead.
- run_pilot.world_file maps W5 by window only; W5 JSONs hard-code day 2018-11-12; using 2018-11-13 cells with it would silently apply the wrong day's traffic.
- w07 cells share demand files with w08 cells and overlap 08:00-09:00 (about half the w07 rows); with the same WP14 selection label the same requests can be selected in both, so w07 is not independent of seen w08 cells for a test split.
- Do not edit benchmarks/scenarios/wp14-development/grid-v1.json; its hash is pinned in wp14-004 evidence and freeze tooling.
- Tier 2 already ran on Panel A days 14-18 (deadline-v1), while the Tier-3 plan says Panel A must not be touched; the owner must decide what counts as seen for T3.8.
- The Runner client has a 60 s response timeout; do not run dotnet build/test concurrently with jobs (SWEEP-AMENDMENTS.md:24-25).
- ADR-077 has no test for multi-dimension budgets; V-30 has four hard limits (drop 30000 plus three zero structural limits), and AllowsBudget must allow every witness, so V under no-worse hits a path that is covered only by the single-dimension unit test.