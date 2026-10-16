# R39 numerical checks

All checks passed. `agent-numbers-v1.py` exited 0; `agent-numbers-summary-v1.py` exited 0. The scripts read saved data only and create their own reports exclusively in this subfolder. No simulation, installation, compilation, training, test execution or source-file modification was performed. Existing interpreter: `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -I -B`.

## Reviewable artifacts

- `agent-numbers-v1.py`: inspected R37 pure probe with exclusive output names, raw morning ledger cross-checks and the new R39 checks; no imports from experimental pipeline scripts.
- `agent-numbers-extensions-v1.py`: source used to construct the additional checks in that self-contained probe.
- `agent-numbers-v1.json` and `.txt`: full output, including per-scenario source paths and raw re-counts.
- `agent-numbers-summary-v1.py`, `.json`, `.txt`: compact `dispatcher_morning` object requested by the root, fresh forecast-ledger arithmetic, ML serialization provenance and test totals.

## Changed numerical passages

| v10 passage | Check and result | Fresh R39 output anchor; source |
|---|---|---|
| 124–128 | Same 21 scenarios: Mplus-30 late60 66→2 / 1,471; V-30 66→2 / 1,470; U 129→63 / 1,512. At 17h U 28→28 / 437; C-30 0 / 418. | `agent-numbers-v1.json:forecast`; `S/optimize/test-family-a-causal-no15-2026-10-06-cells.tsv`, full-precision cell rates multiplied by each cell's served count, residual below 1e-10. U/C independently cross-checked against saved Codex per-rider records. |
| 124–128,177 | 68 late riders on 21 scenarios, 6,217.406 seconds. Components rounded to 3 decimals: 81.742 + 5,352.646 + 783.018. History share 86.09131337%→86.1%. Whole-second labels 82+5,353+783=6,218 versus total label6,217. | `agent-numbers-summary-v1.json:forecast_ledger`; same Family-A TSV ledger columns. The exact history/residual before 3-decimal rounding are5352.646482885389507/783.0175171146106613. |
| 130–132 | 21-scenario means: drop extension13.6986668251→13.7s; 7h27.7534291197→27.8s; pickup3.1816807760→3.2s. | `agent-numbers-v1.json:forecast_oracle_and_price`; same Family-A TSV extension columns. |
| 135–136 | Oracle eligible2,305, within2s2,305, over34 main scenarios; the21 active weekday scenarios have1,452. | `agent-numbers-v1.json:forecast_oracle_and_price`; Family-A TSV `oracle_n`, `oracle_ok`, interpreted by opened `forecast_family_a.py:137–138`. |
| 184–188 | Same15 completed Mplus forecast scenarios: forecast3,849/8,496 forced, unweighted scenario mean47.61589255%→47.6%; original baseline5,121/8,468, mean62.77032087%→62.8%. | `agent-numbers-v1.json:dispatcher.paired`; every matched raw NDJSON decoded with hash checks, decisions joined to distinct acknowledgements, forced iff acknowledged `certificate.body.normalOperation` is false; cross-check with BIC `ack`, `nonNormal`. |
| 184–188 | Same8 completed7h scenario IDs: baseline170/442 riders break initial drop promise by>30s, scenario mean39.0477101812%→39.0%; forecast45/439, mean10.9922458594%→11.0%. Pooled rates38.46153846% and10.25056948% differ from those means. | `agent-numbers-v1.json:morning_promise_breaks`; compact `agent-numbers-summary-v1.json:dispatcher_morning`. Fresh raw ledger initialPromise versus first alight times; each per-scenario count checked against rounded BIC `ownBreak`, same definition as opened `b_analyze.py:123,134,137`. |
| 206–211 | All25 selected ML rows have exactly one compatible late and early integer. Largest count halfwidth0.004035 atn807. C-30 reference/model0/147,0/197; U reference2/145→HGB1/145, reference1/200→HGB1/200; FREE104/807→94/807, early0/807→57/807. HGB-nostate late counts matchHGB. | `agent-numbers-v1.json:ml`; summary `ml_count_provenance`; each integer0..n enumerated against saved rate rounding tolerance0.0005 percentage points. Opened `S/optimize/codex-debate/claude-work/ml_pilot_run.py:37–42,175–176` confirms pooled percentage and 3-decimal serialization. This validates arithmetic only. |
| 217–224,269–272,295–300 | BothU/C-30 have34 scenarios and3,672 requests; served2,434/2,338, difference96;U174 exposed/max590.133→590.1s; C-30 max29.239→29.2s. The designed30s cap remains distinct from this maximum. | `agent-numbers-v1.json:cohort_totals` and `padding`; fresh reaggregation of independent Codex per-rider extraction `codex-work/R19-stage1a-analysis.json:runs[].riders`. |
| 217–224,269–272,295–300 | Padding rows reproduce all late/early/timely counts: U+30 timely60/1202,328/2,366; C-30 forecast2,328/2,338; C-30+30 timely2,336/2,338. Extension means37.1833310557 and7.3671234457, ratio5.0471980455. | `agent-numbers-v1.json:padding`, `cohort_totals.extension_ratio_upad30_c30`; saved independent per-rider extraction, strict arrival-versus-quote inequalities. These are similar extensions, not equal full promise lengths or a minimum necessary pad. |
| 286–287 | Original nonforecast obligation: forced7,710/20,103; unweighted mean41.3113664783%→41.3%. Breach289/2,338 with≥1 in28/34 scenarios. C-30 forced0/20,101 and breach0. | `agent-numbers-v1.json:main_original_obligation`; all34 IVC cache JSONs per arm freshly read, scenario count definition and all source paths in output. |
| 295–300 | Shared555/2,434 forU and313/2,338 forC-30, difference242. | `agent-numbers-v1.json:cohort_totals.shared_read_counts/shared_difference`; freshly opened saved original recomputation output `S/rewrite-2026-10/evidence/checks-addendum-1/recompute-addendum-1-2026-10-11.txt:136–140`. This is a read-and-subtract check, not a fresh raw shared-trip extraction. |
| 359–361 | C-30 forced0/20,101 and C-120 forced0/20,435; same34 main scenario cohort. | `agent-numbers-v1.json:cohort_totals.by_arm`; reaggregation of Codex saved run records; C-30 independently matched to IVC cache. |
| 376–379 | Eight snow manifests match51 main C-30 manifests on5 identity fields; runner DLL SHA256 and canonical recovery configuration binding match. Snow max absolute dispatch25.187s,601 riders,41 naive late,34 forecast late. | `agent-numbers-v1.json:identity` and `snow`; fresh raw manifest/DLL/config and snow ledger reads, with independently written historical-factor integration. |
| 381–384 | One saved full suite,9 project rows sum0 failures,1,025 passes,0 skips,total1,025, exit0, completed13/10/2026 13:42:21+07:00. LF checkout and an untracked marker were present. | `agent-numbers-v1.json:test_attempt4`; summary same key. Saved log `C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log`; `S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md:18` attempt4 plus attempt3 LF condition. No tests were run here. |

`S` means `E:/Code/Report_INT3508/ridebound-scratchpad`.

## Recommended morning wording

> Tỉ lệ khách bị nó phá lời hứa ở khung7 giờ giảm từ39,0\% xuống11,0\%, tính trung bình trên cùng8 kịch bản; tính gộp theo khách, đó là170 trong442 khi không đưa dự báo vào và45 trong439 khi có dự báo.

Add `agent-numbers-v1.json:morning_promise_breaks` to the EV comment. The two pooled fractions are separately labeled supporting counts and are not the numerators and denominators of the scenario means. Restore spaces around numerals when integrating this compact handoff wording into the thesis.

The broader 15-scenario forced-decision sentence should likewise keep47.6/62.8 explicitly as scenario means and label3,849/8,496 versus5,121/8,468 as pooled decision counts.
