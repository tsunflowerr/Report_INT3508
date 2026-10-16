# Round 21B - Codex independent Stage 1a results

**Completed: P1-P4 PASS; P5 FAIL.** One v4 analyzer invocation succeeded and independently reconstructed all 102 runs: 34 C-120, 34 archived C-30 and 34 archived U. C-120 serves 2,387 requests, with 132 naive late60, 21 late120 and zero late300 completions. Its 2,366 naive timely120 completions exceed both measured baselines. Relative to C-30 it serves 49 more requests, has 7 fewer naive timely60 completions and 39 more naive timely120 completions. P5 misses its <=2 target because three cumulative-only budget-prune records occur in three distinct decisions.

Analysis completed at `2026-10-10T17:00:50.261365Z`, or 2026-10-11 00:00:50 in Asia/Bangkok. The sealed predictions and R19 extraction definitions were retained. No `claude-work/R21-*` file was read. No simulation, build, install, research-input edit or thesis edit occurred; all new files were exclusive-created in `codex-work`.

## 1. The archive-resolution correction and single execution

V3 opened `OLD / (arm + "-" + cell)` before consulting the inventory, so it selected the failed original C-30 folder. V4 selects archived transcript parents from the R15 path inventory, requires exactly the 68 unique sealed U/C-30 arm-cell identities, and requires every path to match the existing R13 transcript inventory under the archived root. C-120 folder construction is unchanged. The existing `summary.status == pass`, one-repeat, succeeded-run and full-transcript SHA-256 gates remain in place.

**Inventory clarification:** `R15-audit.json` records transcript paths but has no full-file SHA-256 fields. Its U/C-30 paths were inherited from `R13-raw-verification.json`, as `R15-audit-v2.py` and `R15-CONFIRM-CODEX.md` document. All 68 R15 paths exactly match that independently hashed R13 inventory. V4 uses R15 for folder selection and retains the original R13 full-file hash gate; it does not invent a separate R15 digest or substitute an unchecked folder.

The only affected archive path is `C:/RideBoundData/research/tier3-t38-v1/C-30-d20181114-s10-r3-w17-rerun1`. Its passing one-repeat summary and succeeded run were checked before execution; during execution its transcript matched `b9e962695169e1e48440e4796b50ad3ac96b74f8c3a2e335819f1ad70597431b`. The failed original folder was left untouched.

The complete v3 -> v4 diff is below. Reversing these two changes reproduced every byte of v3, including its line endings. Syntax compilation succeeded without importing or running either analyzer; AST comparison found changes only in `read_run` and `main`, exactly where archive resolution occurs. The forecast, completion gate, all outcome arithmetic, prediction predicates, baseline checks and exclusive-output logic are unchanged.

```diff
--- R19-stage1a-analyze-v3.py
+++ R19-stage1a-analyze-v4.py
@@ -73,7 +73,7 @@
   work-=capacity;clock=(bin_+1)*900000
  raise EvidenceError("forecast integration failed to converge")
 def read_run(arm,cell,f,old_index):
- root=(C120 if arm=="C-120" else OLD)/(arm+"-"+cell)
+ root=(C120/(arm+"-"+cell) if arm=="C-120" else pathlib.Path(old_index[(arm,cell)]["resolved_folder"]))
  summary=read_json(root/"summary.json");run=read_json(root/"run-00.json")
  require(summary["status"]=="pass" and summary["repeatCount"]==1,"invalid summary: "+str(root))
  require(run.get("status")=="succeeded","run status: "+str(root))
@@ -233,6 +233,14 @@
  FIXTURE_HASHES={x["cell"]:x["scenario_sha256"] for x in design["fixtures"]["details"]}
  inventory=read_json(H/"R13-raw-verification.json")
  old_index={(r["arm"],r["cell"]):r for r in inventory["runs"] if r["population"]=="t38" and r["arm"] in ("U","C-30")}
+ archived_paths=read_json(H/"R15-audit.json")
+ indexed=[r for r in archived_paths["runs"] if r["pop"]=="t38" and r["arm"] in ("U","C-30")]
+ require(len(indexed)==len({(r["arm"],r["cell"]) for r in indexed})==68,"R15 archived path identities/count mismatch")
+ require({(r["arm"],r["cell"]) for r in indexed}==set(old_index)=={(a,c) for a in ("U","C-30") for c in cells},"archived inventory panel mismatch")
+ for r in indexed:
+  key=(r["arm"],r["cell"]);p=pathlib.Path(r["path"])
+  require(p.is_relative_to(OLD) and p.name=="transcript-00.ndjson" and p==pathlib.Path(old_index[key]["transcript"]),"R15/R13 archived transcript path mismatch")
+  old_index[key]["resolved_folder"]=str(p.parent)
  f=factors();rows=[]
  for arm in ("C-120","C-30","U"):
   for i,cell in enumerate(cells,1):
```

Executed from `codex-work`, **exactly once**, using one analyzer process and no analyzer workers:

```powershell
& 'E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe' -B './R19-stage1a-analyze-v4.py'
```

`R21B-v4-execution.txt` records start `2026-10-10T16:58:20.2627316Z`, end `2026-10-10T17:00:50.4302276Z`, all three `34/34` read markers, output creation and exit code **0**. Preparation and subsequent output checks did not import or invoke the analyzer again. The Round 21 refusal report and v3 remain preserved.

The full pipeline retained checks for sealed inputs, archived binary/core, seeds, canonical policy bindings, fixture and repository inventories, frame lengths/hashes, transcript stability, decision/acknowledgement equality, and terminal request/alight/ledger/publication consistency. All C-120 artifacts passed the completion gate before outcome extraction. The reconstructed U/C-30 frontier and 2,207-common baseline overlap passed their unchanged reference gates.

## 2. Sealed predictions

| Prediction | Unchanged executable predicate | Observed C-120 value | Verdict |
| --- | --- | --- | --- |
| P1 | 34 passing summaries; zero acknowledged non-normal certificates; zero served ledgers above 120,000 ms | 34/34 pass; 0 non-normal; 0 overshoot riders; maximum 118,938 ms | **PASS** |
| P2 | Served >=2,362 | 2,387; net +49 versus 2,338 C-30, exceeding the +24 target | **PASS** |
| P3 | 76 < naive late60 < 203 (77-202 inclusive) | 132 | **PASS** |
| P4 | Naive timely120 >=2,327 | 2,366 (=2,387-21) | **PASS** |
| P5 | Recorded cumulative-only drop-budget prune records <=2, with no missing/other/unclassified budget evidence | 3 records in 3 decisions; unknown/other/unclassified = 0 | **FAIL** |

P4 remains the **naive** primary specified by R19; its separately reported forecast value is not substituted. P5 is a failed numerical prediction, not a failed data-quality gate or permission to retune the target. The +49 in P2 is a net service-count change, not 49 identified C-30-rejected riders rescued.

## 3. Service-arrival-quote frontier

Every arm uses the same 3,672 requests. Lateness and earliness compare physical passenger-alight time with the first acknowledged initial quote. Timely means arrival no later than quote + threshold; rejected requests do not contribute. `causal-no15` is the unchanged, one-sided historical-factor display replay with no added padding and no redispatch. Mean extension and early fractions use each served cohort; timely fractions use all requests. Values below round percentages to three decimals and extension seconds to six; JSON preserves full precision.

| Arm / quote | Served | Late >60 s | Late >120 s | Late >300 s | Timely <=60 s / requests | Timely <=120 s / requests | Mean quote extension, s | Early >60 s / served |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U / naive | 2434 | 203 | 102 | 18 | 2231/3672 (60.757%) | 2332/3672 (63.508%) | 0.000000 | 7/2434 (0.288%) |
| C-30 / naive | 2338 | 76 | 11 | 0 | 2262/3672 (61.601%) | 2327/3672 (63.371%) | 0.000000 | 3/2338 (0.128%) |
| C-120 / naive | 2387 | 132 | 21 | 0 | 2255/3672 (61.411%) | 2366/3672 (64.434%) | 0.000000 | 1/2387 (0.042%) |
| U / causal-no15 | 2434 | 137 | 87 | 17 | 2297/3672 (62.554%) | 2347/3672 (63.916%) | 7.183331 | 8/2434 (0.329%) |
| C-30 / causal-no15 | 2338 | 10 | 0 | 0 | 2328/3672 (63.399%) | 2338/3672 (63.671%) | 7.367123 | 4/2338 (0.171%) |
| C-120 / causal-no15 | 2387 | 65 | 8 | 0 | 2322/3672 (63.235%) | 2379/3672 (64.788%) | 7.273885 | 2/2387 (0.084%) |

Naive late60 fractions among served riders are U 8.340%, C-30 3.251% and C-120 5.530%; causal-no15 fractions are 5.629%, 0.428% and 2.723%, respectively. The C-120 replay has 65 late60 and 8 late120 completions, hence 2,322 timely60 and 2,379 timely120. Its mean extension is 7.273884592652162 s. These replay changes do not alter which requests are served.

## 4. Ledger exposure, enforcement and cumulative witnesses

| Arm | Acknowledged decisions | Forced/non-normal | Drop-exposed served riders | Served riders with >=2 nonzero changes | Maximum sum of absolute dispatch changes, ms | Served cap overshoot riders | Step-failure prune records | Cumulative-only prune records |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U | 20760 | 0 | 174 | 12 | 590133 (590.133 s) | N/A: no drop cap | 0 | 0 |
| C-30 | 20101 | 0 | 33 | 0 | 29239 (29.239 s) | 0 | 845 | 0 |
| C-120 | 20435 | 0 | 103 | 0 | 118938 (118.938 s) | 0 | 521 | 3 |

A drop-exposed rider has positive final sum of absolute model dispatch changes. Both C arms have **zero** served histories with at least two nonzero drop changes. C-120 nevertheless has three candidate records proposing a further change against previously spent allowance; they were pruned, so their absence from accepted repeated-change histories is consistent with enforcement. Budget-prune totals are C-30 845 and C-120 524 (=521 step failures +3 cumulative-only); U has none. Missing, other-budget and unclassified budget records are zero. Counts concern acknowledged candidate records, not numbers of lost riders.

All decisions have status `produced`; all acknowledged certificates report normal operation. Typed incident entries are separately counted as `exogenousServiceQuality`: U 3,408, C-30 2,488 and C-120 2,548; no other incident kinds were present. These entries are distinct from non-normal decision counts and do not identify complete real-world physical causes.

| Cell | Decision hash prefix | Prior spend, ms | Proposed delta, ms | Proposed total, ms | Cap, ms | Associated new request final lifecycle |
| --- | --- | --- | --- | --- | --- | --- |
| d20181114-s10-r3-w08 | `97e7a540d994...` | 25844 | 99027 | 124871 | 120000 | rejected |
| d20181115-s10-r1-w08 | `5b2ca6ae8c49...` | 58874 | 91584 | 150458 | 120000 | completed |
| d20181118-s10-r3-w08 | `c9fb376c2f42...` | 105508 | 99301 | 204809 | 120000 | rejected |

All three occur at 08 h, on Nov 14, 15 and 18, in three distinct decisions/candidates with three distinct associated new requests. One associated request ultimately completes; two are finally rejected. The complete decision, candidate, budgeted-rider, vehicle and new-request IDs and witness records are retained in the analysis JSON under each run's `cumulative_only_records`. The final lifecycle association does **not** establish that two rejections were caused solely by cumulative enforcement or that the completed request was served through this pruned candidate.

This new measured-factor C-120 panel supplies three recorded failures whose reported drop increment passes an equal-120 s step check but whose cumulative total fails. The prior zero-record finding remains true for its older audited corpus. Neither the new records nor zero repeated accepted histories prove an empirical cumulative-versus-per-step outcome effect: no per-step arm was run, fail-fast evidence does not enumerate every blocker, and later trajectories may differ.

## 5. Served-set overlaps

| Left arm | Right arm | Common rider-cell pairs | Left only | Right only |
| --- | --- | --- | --- | --- |
| C-120 | C-30 | 2266 | 121 | 72 |
| C-120 | U | 2271 | 116 | 163 |
| C-30 | U | 2207 | 131 | 227 |

C-120 versus C-30 changes the cohort by 121 C-120-only and 72 C-30-only pairs, yielding net +49. C-120 versus U has 116 C-120-only and 163 U-only pairs, yielding net -47. Neither comparison is a nested served set. Counts use `(cell, requestId)` identities; raw request IDs reused across cells are not collapsed. Common-served groups would also be post-treatment populations, not randomized causal strata.

## 6. Per-window served / late60 / timely60

| Window | Arm | Cells | Requests | Served | Naive late60 | Naive timely60 / window requests | Causal-no15 late60 | Causal-no15 timely60 / window requests |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 07 h | U | 9 | 972 | 516 | 70 | 446/972 | 11 | 505/972 |
| 07 h | C-30 | 9 | 972 | 511 | 61 | 450/972 | 2 | 509/972 |
| 07 h | C-120 | 9 | 972 | 515 | 63 | 452/972 | 5 | 510/972 |
| 08 h | U | 14 | 1512 | 1014 | 67 | 947/1512 | 60 | 954/1512 |
| 08 h | C-30 | 14 | 1512 | 975 | 15 | 960/1512 | 8 | 967/1512 |
| 08 h | C-120 | 14 | 1512 | 1001 | 49 | 952/1512 | 40 | 961/1512 |
| 17 h | U | 11 | 1188 | 904 | 66 | 838/1188 | 66 | 838/1188 |
| 17 h | C-30 | 11 | 1188 | 852 | 0 | 852/1188 | 0 | 852/1188 |
| 17 h | C-120 | 11 | 1188 | 871 | 20 | 851/1188 | 20 | 851/1188 |

The window request denominators are 972, 1,512 and 1,188, summing to 3,672 per arm. Each arm's window counts sum exactly to its pooled totals. Relative to C-30, C-120 naive timely60 changes by +2 at 07 h, -8 at 08 h and -1 at 17 h; the forecast changes are +1, -6 and -1. The pooled comparison therefore does not describe identical effects in every window.

For an additional paired-date check, the following are **C-120 minus C-30**, using naive quotes:

| Date | Served difference | Late60 difference | Timely60 difference | Timely120 difference |
| --- | --- | --- | --- | --- |
| 2018-11-14 | 4 | 7 | -3 | 3 |
| 2018-11-15 | 13 | 8 | 5 | 13 |
| 2018-11-16 | 7 | 9 | -2 | 5 |
| 2018-11-17 | 13 | 16 | -3 | 11 |
| 2018-11-18 | 12 | 16 | -4 | 7 |

At cell level, C-120 versus C-30 service rises in 23 cells, falls in 3 and ties in 8. Naive timely120 rises in 21 cells, falls in 4 and ties in 9. Versus U, naive timely120 rises in 15 cells, falls in 7 and ties in 12; C-120 service exceeds U in 5 cells. These are observed paired patterns, not 34 independent replications. The five dates and dependent cells give no new-date or population guarantee.

## 7. Reading for the thesis cap-dial section

On this fixed stability-first panel, raising the all-trip dispatch cap from 30 to 120 s trades fewer rejections for more late completions at the one-minute threshold. C-120 adds 49 services (1.334 percentage points of 3,672 requests, or 51.042% of the **aggregate** 96-count C-30/U gap), while naive late60 rises by 56 and naive timely60 falls by 7. Rejections fall from 1,334 to 1,285. The identity +49 = +56 -7 makes service selection part of the arrival-count comparison; it does not identify individual riders made late by the treatment.

At the two-minute threshold, C-120 has 2,366 naive timely completions: +39 versus C-30 and +34 versus U. With causal-no15 it has 2,379 timely120: +41 and +32. At one minute the forecast yields 2,322 timely completions: -6 versus C-30 but +25 versus U. Thus this tested cap gives a useful two-minute pooled point while C-30 retains more one-minute timely completions. Quote extension and early-arrival counts belong beside those outcomes; the small mean-extension difference between differing served cohorts is not a demonstrated operating-cost saving.

U remains a **measured removal-of-drop-cap endpoint**, not a service bound for finite caps. The different served sets, cell-level reversals and untested cap levels prevent a general ranking. The budget limits charged model dispatch changes; zero overshoot and non-normal decisions do not make the 120 s cap a physical-arrival guarantee. Its 21 naive arrivals later than quote +120 s remain compatible with that narrower ledger guarantee.

P5 changes the mechanism wording: cumulative-only reported witnesses now occur on the measured-factor panel, although they are sparse and no served C-120 history has repeated nonzero changes. Report the three records and the failed <=2 prediction explicitly. The empirical effect of disabling accumulation still requires the matched per-step comparison described in R18; this round does not replace it, establish trajectory equivalence, or attribute a service gain/loss to accumulation alone. No objective-interaction or later-stage experiment was performed or launched here.

## 8. Provenance, outputs and verification limits

The sealed plan SHA-256 remains `cb6da66288b6d3b4a96271b27fc7047843c4e35f260f02ce4c559672bc6fd046`; C-120 canonical commitment/WP4 binding remains `a9ac58b33558c6ec2d604ee7fe3e7fdb02deaecfd866ea73282b911326ed9010`. Amendment A1 corrects the supplied plan-header time only. No endpoint, factor profile, split or input hash was retuned after seeing these results. All 102 full-transcript hashes, decoded-frame checks and per-run manifests are in `R19-stage1a-analysis.json`; R15/R13 input file hashes are also recorded there.

| File | SHA-256 |
| --- | --- |
| `R19-stage1a-analyze-v3.py` | `74447319935aad42c205a9b3ade24ba212e699658a0f2d4e24bde34d4e510705` |
| `R19-stage1a-analyze-v4.py` | `55341d5fcaa943021ecb6b91aff1368ea6b2b4016c1177ada358a5470761ed64` |
| `R15-audit.json` | `cd243d063bf3df9ac63223556cdd28a281e70aebde121ca644d15302240962fa` |
| `R13-raw-verification.json` | `d8f2adb5d43394079af9616f21123d5febe6d635a9bbf848d6190d20fee361e3` |
| `R19-stage1a-analysis.json` | `a7d4520f26793cf320db98d941ff9ee5533457bf592bfa78708082da9bb1b77d` |
| `R19-stage1a-analysis.md` | `47ee4012bc851c1ca2632d60da53703809233769ca78e6e0322912a0ecdf1161` |
| `R21B-v4-execution.txt` | `865f991c301b816d058b948f7cca7af0124b83a2e9d9f8207e3a693613fe36ec` |

After the successful single analyzer run, a separate read-only check re-summed the exported rider records for every arm/quote: all late60/120/300, timely counts, early60, quote-extension sums, drop-exposed counts, repeated-change counts and maximum dispatch spending reproduced the pooled totals. Window sums, witness arithmetic and execution markers were checked as well. This verifies internal exported arithmetic; it is not a second transcript extraction or an independent new forecast evaluation.

| Exclusive-created file | Purpose |
| --- | --- |
| `R19-stage1a-analyze-v4.py` | Archive resolver correction only; v3 preserved |
| `R19-stage1a-analysis.json` | Full 102-run evidence, per-rider outcomes, witnesses, hashes and predictions |
| `R19-stage1a-analysis.md` | Unchanged analyzer-generated compact results |
| `R21B-v4-execution.txt` | Single-invocation command, progress, timestamps and exit status |
| `R21B-STAGE1A-CODEX.md` | This report, exact diff, complete requested comparison and bounded interpretation |

Existing reports, analyzers, inventories and research inputs were neither overwritten nor deleted. R21's refusal remains part of the audit trail; the completed Round 21B evidence now supplies the previously pending full-panel outcome values. The forecast remains a frozen display replay, recorded fail-fast witnesses remain incomplete counterfactual evidence, and model attribution remains narrower than real-world causal identification.
