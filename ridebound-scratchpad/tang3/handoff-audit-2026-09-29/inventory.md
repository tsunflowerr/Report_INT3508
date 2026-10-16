# inventory

## 1. [worktrees]
4 worktrees: E:/Code/RideBound 41a4e11 [main]; C:/Code/RideBound-noworse a90b4b7 [research/tier3-no-worse]; E:/Code/RideBound-deadline 1ce15e9 [research/tier3-failure-aware]; E:/Code/RideBound-py-baseline 8d1ea4d (detached HEAD). Main log -1: 41a4e11 'Add comprehensive tests for commitment and optimization features'.
SOURCE: cmd: git -C E:\Code\RideBound worktree list; git -C E:\Code\RideBound log -1 --oneline

## 2. [worktree C:\Code\RideBound-noworse]
Branch research/tier3-no-worse. log -5: a90b4b7 Record end-to-end A1 evidence for no-worse recovery (ADR-077, exploratory); 45f8026 Add default-off no-worse-than-reference recovery for forced vehicles (ADR-077, exploratory); 1ce15e9 Record the Tier 3 pilot (T3.5-T3.7) status and next decisions (exploratory); 69512d3 Record late boardings as observed facts behind a default-off option (ADR-076, exploratory); 8d1ea4d Add default-off forced-reference recovery for gate-rejected no-ops (ADR-075, exploratory). Status clean (0 modified, 0 untracked). 'status -sb' first line: '## research/tier3-no-worse...origin/research/tier3-no-worse'; ahead/behind vs origin = 0 0 (pushed).
SOURCE: cmd: git -C C:\Code\RideBound-noworse log --oneline -5; git --no-optional-locks -c core.autocrlf=false status -sb/--porcelain; git rev-list --left-right --count HEAD...origin/research/tier3-no-worse -> '0 0'

## 3. [worktree E:\Code\RideBound-deadline]
Branch research/tier3-failure-aware. log -5: 1ce15e9 Record the Tier 3 pilot (T3.5-T3.7) status and next decisions (exploratory); 69512d3 (ADR-076); 8d1ea4d (ADR-075); 65d867c Add an initial-promise drop ETA deadline rule and a typed no-op rejection diagnostic (ADR-074, exploratory); 41a4e11 (main tip). 'status -sb' first line: '## research/tier3-failure-aware...origin/research/tier3-failure-aware'; ahead/behind 0 0 (pushed). Porcelain shows 144 ' M' files and 0 untracked, but 'git diff --shortstat' and 'git diff --ignore-cr-at-eol --shortstat' print nothing except 'LF will be replaced by CRLF' warnings, i.e. zero content changes (EOL/stat-only dirtiness; core.autocrlf=true in that worktree). Examples: benchmarks/fixtures/wp6/e2e/tiny/paired.input.ndjson, benchmarks/scenarios/wp2-tiny/online-demo.*, simulators/ridepy-ridebound/wp10_*.py, tools/create_post_wp10_review_pdf.py.
SOURCE: cmd: git -C E:\Code\RideBound-deadline config --get core.autocrlf -> true; git --no-optional-locks status --porcelain count=144; git -c core.autocrlf=false diff --shortstat (empty); output saved C:\Users\quang\.claude\projects\e--Code-RideBound\81f0fa0b-2ed9-4b22-889e-cfc5c7ed6897\tool-results\bddcxcgce.txt:1-297

## 4. [worktree E:\Code\RideBound-py-baseline]
Detached HEAD at 8d1ea4d (ADR-075 commit). log -5: 8d1ea4d, 65d867c, 41a4e11, 38d517d, 2d6791f. Clean (0 modified, 0 untracked). 'status -sb' first line '## HEAD (no branch)'. HEAD is contained in local+remote research/tier3-failure-aware and research/tier3-no-worse.
SOURCE: cmd: git -C E:\Code\RideBound-py-baseline log --oneline -5; status -sb; branch -a --contains HEAD (tool-results bddcxcgce.txt:298-303)

## 5. [research root E:]
E:\RideBoundData\research top level (name / subdirs / size GB / files): deadline-v1 301 / 12.839 / 932; deadline-v1-pilot 1 / 0.060 / 4; pdf-20260820 1 / 0.025 / 18; pdf-20260823-post-h6 1 / 0.005 / 18; pdf-20260824-wp14 0 / 0.007 / 11; pdf-20260826-wp14r-benchmark-methodology 0 / 0.001 / 3; pdf-20260828-wp14r-freeze-v2-methodology 1 / 0.006 / 13; pdf-20260828-wp15-commitment-design 0 / 0.022 / 170; runner-deadline-v1 1 / 0.323 / 429; runner-tier3-v1 1 / 0.323 / 429; tier3-pilot-v1 60 / 4.824 / 240; tier3-sweep-v1 168 / 14.086 / 648; tier3-world-smoke-v1 2 / 0.143 / 8; tier3-world-v11-smoke 4 / 0.312 / 16.
SOURCE: cmd: Get-ChildItem E:\RideBoundData\research (subdir counts); bash du -sk + find -type f per dir

## 6. [research root C:]
C:\RideBoundData\research top level: runner-tier3-v2 (1 subdir 'runtimes', 0.323 GB, 429 files); tier3-sweep-noworse-v1 (28 subdirs, 2.258 GB, 112 files). Nothing else.
SOURCE: cmd: Get-ChildItem C:\RideBoundData\research; du -sk

## 7. [runners]
Three published runner dirs, each = RideBound.Runner.exe/.dll + Algorithms/Application/Contracts/Domain/Infrastructure/Solvers.OrTools dll+pdb + Google.OrTools.dll + Google.Protobuf.dll + runtimes/{linux-arm64,linux-x64,osx-arm64,osx-x64,win-x64}: E:\RideBoundData\research\runner-deadline-v1 (built 2026-09-24 10:04, Tier 2), E:\RideBoundData\research\runner-tier3-v1 (built 2026-09-25 01:05), C:\RideBoundData\research\runner-tier3-v2 (built 2026-09-26 02:55).
SOURCE: cmd: Get-ChildItem on each runner dir (LastWriteTime of RideBound.Runner.dll)

## 8. [runner manifests]
Tree-hash header lines: E:\Code\Report_INT3508\ridebound-scratchpad\deadline\runner-deadline-v1.sha256.tsv:1 '# tree-sha256 8fa5dd288b0ae603dc2c044825f8089116f59953c768442eabfb5d8ca261cda8 files 429'; ...\tang3\runner-tier3-v1.sha256.tsv:1 '# tree-sha256 5049f6d390a8be2b482d3f05214cd3103953d7570a852446f7c8bdb94852c5cb files 429'; ...\tang3\runner-tier3-v2.sha256.tsv:1 '# tree-sha256 ac251ef32a4865ea3bd3d8d87b4b1bcaccc4462a9b80160b4d205b8d474cff3f files 429'. Each file has 430 lines (header + 429 'path<TAB>sha256<TAB>bytes').
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\deadline\runner-deadline-v1.sha256.tsv:1; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\runner-tier3-v1.sha256.tsv:1; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\runner-tier3-v2.sha256.tsv:1

## 9. [runner key DLL hashes]
RideBound.Runner.dll sha256: deadline-v1 8b00dfbfd461ae0d8d91ee55c1095af4310efc678908ab9b2e70ff534c0cb067 (192000 B); tier3-v1 6a469784f7e17b0818743edc65ccd146714eef1dd9923ff637cdb0df649cc319 (197120 B); tier3-v2 a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac (198144 B). RideBound.Application.dll: deadline-v1 fdbe2a20...b392b8; tier3-v1 ff09af4d...610f93; tier3-v2 3d0489cf...2922f3. RideBound.Algorithms.dll: deadline-v1 63f87073...a490a93; tier3-v1 24d570b5...9aa8c; tier3-v2 3adb65de...611fe.
SOURCE: runner-deadline-v1.sha256.tsv:4,6,15; runner-tier3-v1.sha256.tsv:4,6,15; runner-tier3-v2.sha256.tsv:4,6,15

## 10. [runner integrity verification]
runner_manifest.py verify: runner-tier3-v1 -> 'OK tree-sha256 5049f6d3... files 429' (exit 0); runner-tier3-v2 -> 'OK tree-sha256 ac251ef3... files 429' (exit 0); runner-deadline-v1 -> 'MISMATCH tree-sha256 602387fe0ed4f9858240b1d510985d26c46a92e5e7aa6cfbd46c84bc1da022fe files 429' (exit 1) but a per-file comparison found 429 manifest entries = 429 files and 0 per-file differences (sha256+bytes), so only the header tree-hash definition differs; runner_manifest.py:4-6 notes the Tier 2 file does not state its own tree definition.
SOURCE: cmd: python -B E:\Code\Report_INT3508\ridebound-scratchpad\tang3\runner_manifest.py verify <dir> <tsv> (3 runs); PowerShell Get-FileHash comparison -> 'per-file differences=0'; runner_manifest.py:1-6

## 11. [runner -> output root mapping]
run_deadline.py: REPO E:/Code/RideBound-deadline, RUNNER runner-deadline-v1, OUT_ROOT deadline-v1. run_pilot.py: REPO E:/Code/RideBound-deadline, RUNNER runner-tier3-v1, OUT_ROOT tier3-pilot-v1, WP4 configs/wp4-tier3-v1.json. run_sweep.py: uses run_pilot.RUNNER (runner-tier3-v1) and run_pilot.WP4, OUT_ROOT tier3-sweep-v1. run_noworse.py: RUNNER C:/RideBoundData/research/runner-tier3-v2, WP4 wp4-tier3-v2.json (commitmentRecovery: no-worse-than-reference-v1), OUT_ROOT C:/RideBoundData/research/tier3-sweep-noworse-v1, cwd run_pilot.REPO (E:/Code/RideBound-deadline), labels '<job>-nw'. run_world_smoke.py: runner-tier3-v1, wp4-tier3-v1.json, OUT_ROOT tier3-world-smoke-v1. run_world_v11_smoke.py: OUT_ROOT tier3-world-v11-smoke via run_pilot.command.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\deadline\run_deadline.py:38,41,45; ...\tang3\pilot\run_pilot.py:27,30,32,37; ...\tang3\sweep\run_sweep.py:5,29,101; ...\tang3\sweep\run_noworse.py:1-9,26-29,72; ...\tang3\world\run_world_smoke.py:28,30,33; ...\tang3\world\run_world_v11_smoke.py:33,50

## 12. [tier3-pilot-v1 outputs]
60 run dirs = arms {C-30, M-30, Mplus-30, U, V-30} x worlds W0..W5 x cells {d20181112-s10-r1-w08, d20181112-s10-r1-w17}; all 60 have 4 files and summary status=pass; all share repositoryInventorySha256 9a003f4360ab1d84022410e72f9ce8309d0ac58669dc3c022fae0489a9601498; written 2026-09-25 08:00-11:13.
SOURCE: cmd: Get-ChildItem E:\RideBoundData\research\tier3-pilot-v1 + summary.json status/inventory tally

## 13. [tier3-sweep-v1 outputs]
168 dirs = 13 arms {C-30,C-60,C-120,C-300,C-600,C-900,Mplus-30,Mplus-60,Mplus-120,Mplus-300,Mplus-600,Mplus-900,U} x W0..W5 x {w08,w17} = 156 primary + 12 '-rerun1'. 156 summaries status=pass; 12 original W4 dirs have only run-00.json + transcript-00.ndjson (no summary/bundle-manifest): C-120-W4-w08, C-30-W4-w17, C-300-W4-w08, C-600-W4-w08, C-900-W4-w08, Mplus-120-W4-w08, Mplus-30-W4-w17, Mplus-300-W4-w08, Mplus-60-W4-w08, Mplus-600-W4-w08, Mplus-900-W4-w08, U-W4-w17; each has a complete '-rerun1' sibling with summary. repositoryInventorySha256 0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe for all 156 summaries. Newest file 2026-09-26 02:10.
SOURCE: cmd: Get-ChildItem E:\RideBoundData\research\tier3-sweep-v1 grouping + summary.json tally

## 14. [tier3-sweep-noworse-v1 outputs]
28 dirs on C:, all 4 files, summary status=pass=28, labels end '-nw', inventory sha 0da63eaf... (same as sweep). Dirs: C-30-W2/W4 x {w08,w17} (4 controls); Mplus-120 W1/W2/W4 x2; Mplus-30 W1/W2/W4 x2 + W5-w08; Mplus-300 W1 x2 + W2-w08; Mplus-60 W1/W2/W4 x2; Mplus-900-W2-w08; Mplus-900-W4-w17. Written 2026-09-26 03:13-04:23.
SOURCE: cmd: Get-ChildItem C:\RideBoundData\research\tier3-sweep-noworse-v1; sample summary C:\RideBoundData\research\tier3-sweep-noworse-v1\Mplus-30-W1-d20181112-s10-r1-w08\summary.json

## 15. [Tier-2 deadline-v1 outputs]
301 dirs; 165 with summary status=pass, 136 without summary (each of those has failure-00.json + transcript-00.ndjson). Per arm total/summary/failure: conduct-30-k1 36/22/14; ctl-conduct-k0 20/20/0; ctl-visible-k0 20/16/4; dl-120-k0 20/20/0; dl-120-k1 41/17/24; dl2-30-k1 16/4/12; dl-30-k0 20/20/0; dl-30-k1 36/11/25; dl-60-k0 20/20/0; dl-60-k1 36/15/21; visible-30-k1 36/0/36. Days d20181112..d20181118; reps r1..r4; 5 '-rerun1' dirs. deadline-v1-pilot: 1 dir ctl-conduct-k0-d20181114-s10-r1-s7 (pass). Newest write 2026-09-24 21:01.
SOURCE: cmd: Get-ChildItem E:\RideBoundData\research\deadline-v1 grouped by arm prefix, Test-Path summary.json/failure-00.json

## 16. [world smoke outputs]
tier3-world-smoke-v1: world-a, world-b (both pass). tier3-world-v11-smoke: v11-C-30-W4, v11-leak-a, v11-leak-b, v11-V-30-W4 (all pass).
SOURCE: cmd: Get-ChildItem on both dirs + summary.json status tally

## 17. [output bundle format]
Each complete run dir holds bundle-manifest.json (bundleType 'ridebound-wp7-actual-fleetpy-medium-v1'), run-00.json (~5.4 KB), summary.json (~0.6 KB), transcript-00.ndjson (65-96 MB); sourceScenarioContentSha256 9f9c177d806875eba9edb8f247405317fa809347bb6f3957818ee225c0147cd4 in pilot, sweep and noworse samples.
SOURCE: E:\RideBoundData\research\tier3-pilot-v1\C-30-W0-d20181112-s10-r1-w08\bundle-manifest.json:1, summary.json:1; E:\RideBoundData\research\tier3-sweep-v1\C-900-W2-d20181112-s10-r1-w08\summary.json:1

## 18. [disk]
C: used 170.52 GB, free 103.76 GB. E: used 158.85 GB, free 41.83 GB.
SOURCE: cmd: Get-PSDrive -PSProvider FileSystem

## 19. [tang3 configs]
E:\Code\Report_INT3508\ridebound-scratchpad\tang3\configs contains: C-30, C-60, C-120, C-300, C-600, C-900 .json; Mplus-30, Mplus-60, Mplus-120, Mplus-300, Mplus-600, Mplus-900 .json; M-30, M-60, M-120 .json; V-30, V-60, V-120 .json; U.json; wp4-tier3-v1.json (848 B); wp4-tier3-v2.json (855 B); generators make_configs_t3.py/.log, make_configs_sweep.py/.log, make_wp4_v2.py/.log.
SOURCE: cmd: Get-ChildItem E:\Code\Report_INT3508\ridebound-scratchpad\tang3\configs

## 20. [tang3 tree (depth 2)]
tang3/: configs/ (above); evidence/ {independent/ (3 entries), audit_vep.py, choice_metrics.py, METRICS-SPEC.md, README.md, smoke-world-a/b.rows.tsv + .summary.json}; oracle/ {accounting.py, mutate_oracle.py, README.md, test_accounting.py}; pilot/ {independent/ (7), logs/ (65), worlds/ (7), per_rider_c.py, pilot-frozen-2026-09-25.tsv, pilot-paired-C30-V30-2026-09-25.tsv, pilot-table-final-2026-09-25.tsv, pilot_analyze.py, pilot_frozen.py, pilot_lateness_vs_initial.py, pilot_paired.py, pilot_worlds.py, run_pilot.py, show_table.py, STOP.cleared-2026-09-25T0215, tier2_switch_lag.py}; sweep/ {logs/ (180), logs-noworse/ (28), no-worse-v1-worktree-edits.patch, noworse-jobs-2026-09-26.tsv, noworse_aggregate.py, noworse_analyze.py, per_world.py, rerun_failed.py, run_noworse.py, run_sweep.py, show_sweep.py, split_noworse.py, SWEEP-AMENDMENTS.md, sweep-jobs-2026-09-26.tsv, sweep-mechanism-2026-09-26.tsv, sweep-paired-2026-09-26.tsv, SWEEP-PLAN.md, SWEEP-PLAN.sha256, SWEEP-REPORT.md, sweep_aggregate.py, sweep_analyze.py, sweep_mechanism.py, sweep_predictions.py, sweep_worlds.py, test_sweep_analyze.py, why_similar.py}; world/ {logs/ (9), smoke/ (2), inspect_smoke.py, mutate_preflight_world.py, mutate_preflight_world_v1_1.py, mutate_world.py, preflight_world.py, preflight_world_v1_1.py, README.md, run_world_smoke.py, run_world_v11_smoke.py, smoke_counts.py, test_preflight_world.py, test_preflight_world_v1_1.py, test_world_v1.py, world_v1.py}; root files inspect_checkpoint.py, runner-tier3-v1.sha256.tsv, runner-tier3-v2.sha256.tsv, runner_manifest.py, T3.1-KHOA-CAU-HOI.md, T3.4-GHI-CHU-THIET-KE.md, T3.7-BAO-CAO-THI-DIEM.md, T3.7-KE-HOACH-THI-DIEM.md.
SOURCE: cmd: Get-ChildItem E:\Code\Report_INT3508\ridebound-scratchpad\tang3 (depth 2)

## 21. [most recent tang3 activity]
Newest writes under tang3: sweep\SWEEP-REPORT.md 2026-09-29 11:54:58 (16614 B); sweep\why_similar.py 2026-09-29 11:52:10; sweep\per_world.py 2026-09-29 01:26:18; sweep\split_noworse.py 2026-09-29 01:11:01; then sweep\SWEEP-AMENDMENTS.md 2026-09-26 04:35:33. No research output root has files newer than 2026-09-26 04:23.
SOURCE: cmd: Get-ChildItem tang3 -Recurse sorted by LastWriteTime; newest-file scan of each research root

## 22. [seal files]
SWEEP-PLAN.sha256:1 '756b65fd2b500eacfab404a031afd26cfb89b96ddc69fe0d4f134aa7a2b6423f  SWEEP-PLAN.md  sealed 2026-09-25T09:33:58Z (before any sweep job)'. deadline\PREREGISTRATION.sha256:1 '# sealed 2026-09-24T06:03:52Z UTC; predicted-arm outputs present at sealing: 0' (L2-L11 hash PREREGISTRATION.md, predictions.csv, run_deadline.py, classify.py, holdout_predict.py, analyze.py, figure_families.py, test_classify.py, test_predict.py, preflight_drift_v2.py). deadline\amendment-A2.sha256:1 '# amendment A2 stamped 2026-09-24T09:37:42Z; rerun outputs present: 0 []'. deadline\t112\T112-PREREGISTRATION.sha256:1-2 f96d8051... T112-PREREGISTRATION.md, 2026-09-24T01:31:21Z.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-PLAN.sha256:1; E:\Code\Report_INT3508\ridebound-scratchpad\deadline\PREREGISTRATION.sha256:1-11; ...\deadline\amendment-A2.sha256:1-6; ...\deadline\t112\T112-PREREGISTRATION.sha256:1-2

## 23. [deadline scratchpad]
E:\Code\Report_INT3508\ridebound-scratchpad\deadline contains configs/ (conduct-30, dl-120, dl-30, dl-60, dl2-30, visible-30 .json + make_configs.py/.log), logs/ (pilot/, runs/, many *.log/*.start), t112/, tex-drafts/ (ch3-hocong.tex, ch4-hauNghiem.tex, ch4-tang2-thietke.tex, insert_after_label.py, tier0.diff), plus AMENDMENTS.md, analysis-2026-09-24-final.txt, analyze.py, BASELINE-2026-09-24.md, classify.py, clopper_pearson.py, compare_controls.py, compare_k1.py, figure_families.py, holdout_predict.py, HOST_FAILURES.txt, PREREGISTRATION.md/.sha256, predictions.csv, predictions-v0-BUGGY-tau-inf.csv, run_deadline.py, runner-deadline-v1.sha256.tsv, STOP.done-20260924T120108Z, tests.
SOURCE: cmd: Get-ChildItem E:\Code\Report_INT3508\ridebound-scratchpad\deadline

## 24. [scratchpad root]
E:\Code\Report_INT3508\ridebound-scratchpad top-level dirs: b4, calib, claude-measurements-2026-09, conduct-outcome-plan-2026-09-22, deadline, drift, env, formcmp, frontier, levelc, measure, report, research-2026-09-16, salvage, session-2026-09-23-archive, survey, tang3, tex-backup-2026-09-23-before-T0.2, welfare, window; files bo-sung-bao-cao.md, CONTEXT-handoff.md, flexslots.txt, salvage.py.
SOURCE: cmd: Get-ChildItem E:\Code\Report_INT3508\ridebound-scratchpad

## 25. [Hamburg data]
C:\Users\quang\Downloads\data top level: Instances/ (900 .txt files, 0 subdirs; names like Dynamic_n100_k10_0.txt .. Dynamic_n750_k8_l90_9.txt), readme.txt (3268 B), _distances.txt (98732 B); total 902 files, 8,086,694 bytes; all dated 2026-09-25 15:42.
SOURCE: cmd: Get-ChildItem C:\Users\quang\Downloads\data (+ Instances extension/name sample)

## 26. [FleetPy dataset]
E:\RideBoundData\wp6\extracted\sha256\d9\d9e86f...599e\FleetPy_Manhattan top level: demand/ (Manhattan_2018/), networks/ (Manhattan_2019_corrected/), zones/ (Manhattan_corrected_12min_max, Manhattan_corrected_6min_max, Manhattan_corrected_8min_max, Manhattan_Taxi_Zones), README_Manhattan.md (3320 B); 335 files, 1,022,750,557 bytes; dated 2026-08-09 22:08.
SOURCE: cmd: Get-ChildItem on FleetPy_Manhattan root and second level

## 27. [repo used by runs]
Pilot, sweep and noworse jobs run with cwd E:/Code/RideBound-deadline (fixtures REPO/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1, drivers REPO/benchmarks/scenarios/wp14-development); Python E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe; FleetPy E:/RideBoundData/wp7/FleetPy-1.0.2.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\pilot\run_pilot.py:27-39; ...\tang3\sweep\run_noworse.py:72

# UNVERIFIED
- Meaning of failure-00.json in the 136 incomplete deadline-v1 dirs (expected rejected runs, or host failures). Contents not read; HOST_FAILURES.txt (241 B) not read.
- Why the 12 original tier3-sweep-v1 W4 runs have no summary.json (crash, interruption, or host failure). Only the file inventory was checked; SWEEP-AMENDMENTS.md and the logs were not read.
- Which commit/source tree built runner-tier3-v1 and runner-tier3-v2 (assumed deadline branch 1ce15e9 and noworse branch a90b4b7/45f8026, not verified from the manifests).
- The exact commitmentRecovery and other fields in wp4-tier3-v1.json vs wp4-tier3-v2.json beyond the docstring in run_noworse.py:3. The config JSON contents were not read.
- Contents of SWEEP-REPORT.md, which was modified today (2026-09-29 11:54), and of why_similar.py, per_world.py and split_noworse.py (modified 2026-09-29). Probably the other session's recent work. Not read.
- Whether the Hamburg instances (C:\Users\quang\Downloads\data) have been adapted or run anywhere. None of the research output roots are named for Hamburg.
# WARNINGS
- E: free space is 41.83 GB, only just above the 40 GB floor in the disk policy. New large outputs should go to C: (103.76 GB free), as run_noworse.py already does (run_noworse.py:9,26).
- The E:\Code\RideBound-deadline worktree shows 144 modified files in git status, but content diff is empty (CRLF/LF stat-only, core.autocrlf=true). Do not commit or 'fix' these. The Pilot, sweep and noworse runs use this worktree as cwd.
- The runner-deadline-v1 manifest header tree hash (8fa5dd28...) does not match the runner_manifest.py definition (it computes 602387fe...). All 429 per-file sha256/byte entries match exactly, so the difference is in the header definition, not in the runner files.
- 12 tier3-sweep-v1 dirs without a summary still exist alongside their '-rerun1' replacements. An analysis that globs every dir needs to skip them, or use the rerun1 dirs.
- tang3/sweep was modified today (2026-09-29 11:52-11:54), possibly by the concurrent measurement session. Re-check before relying on SWEEP-REPORT.md contents.
- Main repo tree E:\Code\RideBound was not inspected beyond worktree list and log -1, as instructed.