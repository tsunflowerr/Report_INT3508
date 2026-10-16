# Round 21 — Codex Stage 1a execution and refusal report

**Result: analysis refused; P1–P5 remain unevaluated.** The prepared analyzer was executed exactly once with FleetPy Python and `-B`, using one analysis process. It passed the all-34 C-120 completion gate and read all 34 C-120 transcripts, then exited with code 1 while opening the first archived C-30 summary. It produced neither of its JSON/Markdown outputs. No input, analyzer, simulation, build or installation was changed, and no second analyzer invocation occurred. No `claude-work/R21-*` file was read.

Command, executed from `codex-work`:

```powershell
& 'E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe' -B '.\R19-stage1a-analyze-v3.py'
```

Final output:

```text
C-120 independently read 34/34
[Errno 2] No such file or directory: 'C:\\RideBoundData\\research\\tier3-t38-v1\\C-30-d20181114-s10-r3-w17\\summary.json'
```

The prepared analyzer has an archive-path bug. In `read_run`, it constructs `OLD / (arm + '-' + cell)` before reading the archive index. For this cell, that unsuffixed folder contains `failure-00.json` and a 66,502,768-byte transcript, with no `summary.json` or `run-00.json`. The failure record states `status: failed`, `failureType: AdapterFailure`, and `RBWP7_RUNNER_RESPONSE_TIMEOUT at $runner: checkpoint`.

The existing independent inventory [R13-raw-verification.json](R13-raw-verification.json) explicitly selects the completed archived folder:

```text
C:/RideBoundData/research/tier3-t38-v1/C-30-d20181114-s10-r3-w17-rerun1
```

Read-only diagnosis of that existing folder confirms `summary.status = pass`, `repeatCount = 1`, `run.status = succeeded`, and 108 semantic requests. Its full transcript SHA-256 is `b9e962695169e1e48440e4796b50ad3ac96b74f8c3a2e335819f1ad70597431b`, exactly matching the prior independent inventory. The passing archived baseline is available; the analyzer ignored its indexed folder. No folder substitution, input patch, source patch or rerun was performed.

A read-only metadata check after refusal found:

| Arm / location checked | Cells | Passing summaries | One-repeat summaries | Run artifacts present | Transcripts present |
|---|---:|---:|---:|---:|---:|
| C-120, sealed output folders | 34 | 34 | 34 | 34 | 34 |
| C-30, analyzer's unsuffixed folders | 34 | 33 | 33 | 33 | 34 |
| U, analyzer's unsuffixed folders | 34 | 34 | 34 | 34 | 34 |
| C-30, indexed replacement for the one affected cell | 1 | 1 | 1 | 1 | 1 |

These are artifact/completion checks. They supply no C-120 pooled outcome values. The analyzer accumulates results in memory and writes only after all 102 runs, baseline reconstruction and overlaps pass; its computed C-120 rows were not exported when the exception terminated execution.

| Sealed prediction | Exact predicate retained from R19 | Round 21 status / observed value |
|---|---|---|
| P1 | 34 passing summaries; 0 acknowledged non-normal decisions; 0 served riders with sum of absolute dispatch changes above 120,000 ms | **NOT EVALUATED overall.** Passing summaries = 34/34; the other two pooled values were not exported. |
| P2 | Served at least 2,362 | **NOT EVALUATED.** C-120 served total unavailable. |
| P3 | 76 < naive late60 < 203, hence integer range 77–202 | **NOT EVALUATED.** C-120 late60 unavailable. |
| P4 | Naive timely120 at least 2,327 | **NOT EVALUATED.** C-120 timely120 unavailable; forecast cannot replace this primary. |
| P5 | Recorded cumulative-only drop-budget prune records at most 2, with no missing/other/unclassified budget evidence | **NOT EVALUATED.** C-120 prune classification unavailable. |

The pipeline failure is recorded separately from prediction verdicts. Assigning PASS or FAIL to the remaining predicates would invent values.

The following U/C-30 rows are **previously verified archived reference values**, retained from [R19-verification.json](R19-verification.json), `frontier`; they were not freshly reconstructed by the aborted Round 21 invocation. Forecast means the causal-no15 replay, with no added padding. C-120 is shown as unavailable rather than inferred.

| Arm / quote | Served | Late >60 s | Late >120 s | Late >300 s | Timely <=60 s / 3,672 | Timely <=120 s / 3,672 | Mean quote extension, s | Early >60 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| U / naive | 2,434 | 203 | 102 | 18 | 2,231/3,672 | 2,332/3,672 | 0 | 7/2,434 |
| C-30 / naive | 2,338 | 76 | 11 | 0 | 2,262/3,672 | 2,327/3,672 | 0 | 3/2,338 |
| C-120 / naive | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |
| U / causal-no15 | 2,434 | 137 | 87 | 17 | 2,297/3,672 | 2,347/3,672 | 7.183331055723637 | 8/2,434 |
| C-30 / causal-no15 | 2,338 | 10 | 0 | 0 | 2,328/3,672 | 2,338/3,672 | 7.3671234456626165 | 4/2,338 |
| C-120 / causal-no15 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |

Mean extension and early-arrival fractions use the served cohort; timely counts use all 3,672 requests. Previously verified C-30/U served-set overlap is 2,207 common rider–cell pairs, 131 C-30-only and 227 U-only. Both C-120 overlaps remain unavailable. C-120 drop-exposed riders, riders with at least two nonzero changes, maximum sum of absolute changes, step-failure versus cumulative-only prune records, forced/non-normal decisions, and the 07/08/17 h served/late60 breakdown remain unreported because the required full analysis did not finish. No partial C-120 frontier is substituted.

For the thesis's cap-dial section, this round establishes that all 34 C-120 runs completed and that the independent outcome analysis needs its archive-path selection corrected in a future attempt. It supplies no verified C-120 service–arrival point and settles none of P1–P5 overall. Retain the archived trade-offs: U serves 96 more requests than C-30 but has 127 more naive late60 completions and 31 fewer naive timely60 completions; causal-no15 C-30 has 31 more timely60 completions than causal-no15 U. U is a measured endpoint, not a bound on finite-cap outcomes. The served cohorts differ, so these aggregate differences do not identify particular riders rescued or made late. The 120 s cap concerns charged model dispatch changes, and completion alone does not establish its physical-arrival performance or the empirical effect of cumulative enforcement.

Provenance checked this round:

- Analyzer SHA-256: `74447319935aad42c205a9b3ade24ba212e699658a0f2d4e24bde34d4e510705`, matching [R19-config-binding-check.json](R19-config-binding-check.json).
- Sealed plan SHA-256: `cb6da66288b6d3b4a96271b27fc7047843c4e35f260f02ce4c559672bc6fd046`, unchanged and matching its seal.
- Amendment A1 SHA-256: `fcfb9d6f72a32d3ad50aa4d6e7d1bd4d52e6e6ae9d838bc9472650442c0e6a3b`; it corrects the plan header time only.
- Completed driver-log SHA-256: `2289014d6bfe48e6892da29d5eef6ca20baf860212c151c54e4db8e3f7b5b58d`; its last record is `status-pass (34/34)`.

Only this report was exclusive-created inside `codex-work`. `R19-stage1a-analysis.json` and `R19-stage1a-analysis.md` remain absent because the analyzer refused before output creation. A future corrected attempt should resolve archived arm folders through the existing independent inventory while retaining the summary, transcript hash and outcome gates; the exact-once instruction is exhausted for this round.
