# R27 — Independent fact check of Chương 4 phần B v7 (2026-10-12)

**Draft checked:** `drafts/09-chuong4-phanB-v7.tex` (488 lines; the NOTES file says 497, which is wrong). I checked only
v7; v1 to v6 were not read.

**How I checked.** I opened the original outputs, scripts and code, not just the register paraphrase. Every line number
below refers to v7. I ran two read-only scratch scripts with `python -I -B` in the session scratchpad:

- `r27_epad.py` re-reads the saved cells TSV of Family A.
- `r27_arith.py` recomputes every derived ratio and coordinate.

I ran no simulation, build or install. I wrote only this file.

**Anchor keys** follow the registers (A, NEW, PV, WP17, CASE, FR, FA, RX, SNOW, RP1, ML, MLS, ADD1, TLOG, TDIRTY …), plus:

| Key | File |
|---|---|
| Q4 | `optimize/codex-debate/claude-work/r16-evidence/q4_cost_first_reselect.py` (the code that PV re-executes) |
| R17V | `optimize/codex-debate/codex-work/R17-verify-portfolios.py` (the script that produced PV) |
| WPCHK | `optimize/codex-debate/claude-work/r17-rebuttal/r17_wp14r_check.py` (the script that produced WP17) |
| FFA | `optimize/forecast_family_a.py` |
| CELLS | `optimize/test-family-a-causal-no15-2026-10-06-cells.tsv` (saved per-cell output of FA) |
| FB | `optimize/test-family-b-2026-10-06-report.txt` |
| RXPY | `optimize/report-extras/report_extras.py` |
| MLX | `optimize/codex-debate/claude-work/ml_pilot_extract.py` |
| RPL / FNS / FNS2 | `CW/r16-forecast/rider_nowcast_replay.py`, `factor_nowcast_screen.py`, `factor_nowcast_screen_v2.py` |
| GEN / CMOD | `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs` / `CandidateModels.cs` |
| RCA | `rewrite-2026-10/evidence/checks-addendum-1/recompute_addendum_1.py` |
| CH3 / PA | `drafts/07-chuong3-v3.tex` / `drafts/08-chuong4-phanA.tex` |

---

## 1. The writer's three doubts

### (a) "Với thứ tự gốc, phép chạy lại cho đúng cả 62.837 lựa chọn đã ghi" (l. 25)

**It is a real re-solve under the original order, not only a necessary-condition check.**

- Q4 has two steps:
  - Step 1 (Q4:15-16, code Q4:131-138) re-solves each acknowledged frame with **all** recorded objective levels. It
    uses an exact dynamic program over the recorded eligible candidates and compares the result with
    `selectedCandidateIds` by set equality.
  - `validation_match` counts these matches: 12.663 / 12.525 / 12.364 / 12.325 / 12.960 (PV:2-6).
- R17V:29 asserts that the sum is 62.837. NEW:7 prints `portfolio_total_matches 62837`.
- `WPCHK` (WP17) is a different, independent DP. Its docstring says it is "necessary conditions, not a re-solve of the
  stability order" (WPCHK:12-15). That is the source of the writer's worry.

So the claim holds, but its anchor is wrong. The `% EV` line cites N4B-01/WPCHK, which is the necessary-condition script.
The correct anchor is PV:1-7 + Q4:15-19, 131-138 + NEW:7 + R17V:29. Three caveats remain:

1. **The "chạy lại" is not the production selector.** It is a Python re-implementation of the selection model, an exact
   DP, run over the recorded candidates and their recorded objective contributions. It is not the CP-SAT selector, and
   it does not regenerate the candidates.
2. **One code base, run twice.** The same Q4 code was run by Claude (R16) and re-executed by Codex (PV:1, "audited-code
   re-execution"). These are not two independent implementations (REG H03 lưu ý; R18 B50). WP17 does independently
   confirm the counterfactual counts (445 / 325 / 173 / 104) and the cost numbers.
3. **62.837 is the total over five configurations.** They are ghép tự do (FREE, 12.960), không trần (12.663), and trần
   120, 60 and 30 giây. The table shows only U and C-30 (12.663 + 12.325 = 24.988), and the sentence does not say this.

**"Bỏ tiêu chí 3" is the right reading.**

- The cost-first order keeps `forced-reference-count`, `accepted-request-count`, `operational-cost` and
  `candidate-id-rank:*` (Q4:17-19, 36; WPCHK:9-10, 32, 95).
- It drops `worst-hard-utilization-ppm` and every `revision:*` level.
- That matches Tiêu chí 3 of Bảng `bang:rangbuoc`: "Mức dùng trần lớn nhất nhỏ nhất; nếu hòa, tổng phần dời do điều
  phối nhỏ nhất, so lần lượt từng chiều" (CH3:131-132).
- Tiêu chí 1, 2, 4 and 5 are kept.

**Verdict:**

- B04 ("bỏ tiêu chí 3"): AGREE.
- B07 (62.837): LABEL. The scope is not stated and the EV anchor is wrong.
- B05 ("bộ chọn được chạy lại"): LABEL.

### (b) Machine-learning test: fixed forecast profile and previewed test days (l. 195-211)

**Neither fact is disclosed.**

1. **Fixed profile.** In the ML test, D0 uses a fixed profile from 12/11 + 13/11 (MLS:37-39; MLX:3, 11:
   `forecast_profile(["2018-11-12", "2018-11-13"], 25200)`).
   - The rest of 4.7 uses the source-day rule. Under that rule the test days 15/11 and 16/11 draw on 12, 13 and 14/11
     (FR:97-98; DISP rule).
   - So "lời hứa theo dự báo" at l. 196 is not the same promise as in the rest of 4.7.
2. **Previewed days.** "Mọi phép so dùng các ngày không dùng để học" (l. 198) is literally true (MLS:43-61). But MLS:9-10
   says "The days are retrospective: they were inspected before". The static test day 13/11 is also a development day.
3. **Where the 30 s is matched.** "cùng độ dài thêm trung bình 30 giây" (l. 197) is matched on the calibration day 14/11
   (MLS:73-80). On the test days the U control's mean extension was 37,2 s (15/11) and 31,8 s (16/11) (ML:6-7).

**Verdict:** B60 and B62 are LABEL (omission). These are the second-ranked correction.

### (c) Is 62,8 % on the same 15 scenarios as 47,6 %? (l. 188-189)

**Yes.**

- RXPY:24 builds `mp` from the Mplus-30 cells completed in Family B.
- RXPY:29 prints both `mean(v[3])` (forecast in the dispatcher, 0,476) and `mean(v[2])` (no forecast, 0,628) over the
  same `mp`, which has 15 cells.
- Cross-check from the per-window lines (RX:9-10): (8 × 0,769 + 7 × 0,466) / 15 = 0,6276 and
  (8 × 0,594 + 7 × 0,342) / 15 = 0,4764.

**Verdict:** B54 AGREE.

---

## 2. Item-by-item verdicts

Verdicts: AGREE / WRONG / OVERSTATED / LABEL (value right, scope or label wrong) / CANNOT CHECK.

### §4.6 Vai trò của trần và thứ tự ưu tiên (l. 14-73)

| ID | Line | Claim | Verdict | Correct value / note | Anchor |
|---|---|---|---|---|---|
| B01 | 17-18 | U and C-30 "dùng cùng tệp cấu hình … chỉ khác nhau ở trần giờ trả" | LABEL | They share the runner config (WP4) and the selector. They use two policy files that differ only at `/policies/0/limits/1/hardLimit` (absent vs 30000). They do not use one file. | NEW:12; A08; H01 |
| B02 | 18-19 | C − U = adding the cap with the selector unchanged, on different rider sets | AGREE | 2.207 shared riders | C04; ADD1:145 |
| B03 | 19-20 | Cost first = tiêu chí 4; stability = tiêu chí 3 | AGREE | — | CH3:129-135 |
| B04 | 23-24 | The re-run drops tiêu chí 3 | AGREE | See §1(a) | Q4:17-19; WPCHK:32, 95 |
| B05 | 24 | "bộ chọn được chạy lại trên cùng các phương án" | LABEL | The selection problem was re-solved by a separate exact DP over the recorded eligible candidates and their recorded criterion values. It was not the production CP-SAT selector. | Q4:13-19; WPCHK:10-11 |
| B06 | 24-25 | The simulation does not continue from the new choice | AGREE | — | WPCHK:1-19; H10 |
| B07 | 25 | 62.837 choices reproduced under the original order | LABEL | It is a full re-solve, not a necessary condition. The total covers **five** configurations (12.960 + 12.663 + 12.525 + 12.364 + 12.325), not the two columns shown. The EV anchor should be PV/Q4, not WPCHK. Same code run twice. | PV:1-7; Q4:15-16, 131-138; NEW:7; R17V:29 |
| B08 | 30-33 | Caption: 16 scenarios per configuration; fixed travel time; old runner; plan cost = remaining planned route duration, iterated | AGREE | — | WP17:2-23 (runs 16); B17; NEW:13; A16 |
| B09 | 40 | 1.714 / 1.715 decisions with a new request | AGREE | — | WP17:6, 20 |
| B10 | 41 | 445 (25,96 %) / 104 (6,06 %) | AGREE | 0,259627; 0,060641 | WP17:7, 21; NEW:6 |
| B11 | 45 | Cost saving on changed decisions: 7,79 / 8,00 % | AGREE | 7,7902; 8,0038 | WP17:8, 22; PV:2, 5 |
| B12 | 46 | Saving over every decision with a new request: 2,02 / 0,49 % | AGREE | 2,0226; 0,4854 | NEW:6 |
| B13 | 47 | Total saving / total chosen plan cost: 0,3069 / 0,0794 % | AGREE | 114.720.189 / 37.380.402.107; 28.288.261 / 35.606.312.123 (recomputed) | PV:2, 5; NEW:6 |
| B14 | 51 | Median extra fleet-summed drop movement: 90,8 / 12,5 s | AGREE | PV upper median 90,819 / 12,494 | WP17:8, 22 |
| B15 | 52 | Maximum 390,8 / 35,5 s | AGREE | — | WP17:8, 22; PV:2, 5 |
| B16 | 58-59 | Reading sentence (445 of 1.714; 7,79 %) | AGREE | — | as above |
| B17 | 62 | Accepted count unchanged in every decision | AGREE | "accepted changes 0" in every configuration | WP17:4-21; PV deltas |
| B18 | 62-64 | 25,96 / 18,95 / 10,08 / 6,06 % with counts | AGREE | 325/1.715 = 0,1895; 173/1.716 = 0,1008 | WP17:7, 11, 16, 21 |
| B19 | 64-66 | Different state sets, not a cap effect; only "gợi ý" | AGREE | — | K16 |
| B20 | 66 | 35,5 s over two riders, 17,77 s each | AGREE | 17.770 + 17.770 ms | CASE:4-17; PV:7; NEW:8 |
| B21 | 69-70 | The selector-order test on 34 scenarios has not been run | AGREE | No Stage 1b output under `C:/RideBoundData/research` or `E:/RideBoundData`; REG L02-L05 empty | OUTLINE §7.2 (fallback kept verbatim) |
| B22 | 70-71 | The cap and the selector cannot yet be separated | AGREE | — | H02; K18 |
| B23 | 71-72 | "Chương kết luận đặt phép thử này lên đầu các hướng phát triển" | CANNOT CHECK | Chương 5 is not written; this is a commitment for §5.3 | OUTLINE §7.2 |

### §4.7 Lời hứa theo dự báo (l. 76-212)

| ID | Line | Claim | Verdict | Correct value / note | Anchor |
|---|---|---|---|---|---|
| B24 | 79-80 | 68 → 2 late riders of 1.471 (pooled over riders) | AGREE | Recounted from CELLS: 68 and 2 of 1.471 | RP1:38-40; CELLS |
| B25 | 80-81 | 6,01 → 0,17 % (mean over scenarios) | AGREE | — | FA:8 |
| B26 | 84-85 | Replay; lateness measured against each method's own first promise | AGREE | — | FFA:8-13; F03 |
| B27 | 85-87 | Same-cost pad: a fixed share of P0 − t0, chosen per window so total extension equals the forecast's | AGREE | k_w = Σ(D0 − P0) / Σ(P0 − t0), from C-30 riders | FFA:15-17; FA:2 |
| B28 | 92-94 | Caption: 21 scenarios, 1.471 riders, means over scenarios | AGREE | — | FA:8; RX:2 |
| B29 | 101 | 6,01 / 1,94 / 0,17 | AGREE | Pooled counts are recoverable from CELLS: 68 / 22 / 2 of 1.471 | FA:8 |
| B30 | 102 | Window 7 h: 14,44 / 4,24 / 0,27 (8 scenarios) | AGREE | Pooled: 60 / 17 / 1 of 444 | FA:9 |
| B31 | 103 | Window 8 h: 1,35 / 0,86 / 0,18 | AGREE | Pooled: 8 / 5 / 1 of 609 | FA:10 |
| B32 | 104 | Window 17 h: 0 / 0 / 0 | AGREE | Pooled: 0 of 418 | FA:11 |
| B33 | 107 | Early > 60 s: 0 / **"chưa đo"** / 0,08 | **WRONG** (middle cell) | The pad's early share **was** measured. FFA:141 computes `E_pad`, and CELLS stores column `E_pad`. For C-30 on the 21 scenarios it is **0 %** (0 of 1.471; max rounding residue 0,0). The other two cells agree: 0 and 0,08 % (1 of 1.471). N4B-03's "phép đệm không tính chỉ số này" is wrong too. | FFA:139-141; CELLS col. 5; FA:8 |
| B34 | 113-114 | Reading sentence for window 7 h | AGREE | — | FA:9 |
| B35 | 117-118 | t-interval over 8 day-window clusters: [−10,54; −1,15] pp | AGREE | df = 8 − 3 = 5 | FA:33; FFA:19-20 |
| B36 | 118-119 | Forecast − pad: −1,77 pp, [−3,62; +0,07] | AGREE | — | FA:36 |
| B37 | 119 | "mong manh" | AGREE | — | FR:58-60 |
| B38 | 119-120 | Three mornings; 12/11 is a source day for every forecast | AGREE | 14 ← 12, 13; 15 and 16 ← 12, 13, 14 | FR:97-98, 171; FNS:22-23 |
| B39 | 123-124 | Deadline rule and visible-shift rule also reach 0,17 % | AGREE | — | FA:13, 23 |
| B40 | 124 | U: 9,72 → 3,90 % (mean over scenarios) | AGREE | Pooled from CELLS: 129 → 63 of 1.512 | FA:3 |
| B41 | 124-125 | U stays at 6,76 % at 17 h; C-30 is 0 % there | AGREE | — | FA:6, 11; RX:7 |
| B42 | 125-126 | "Dự báo và trần nhắm vào hai phần khác nhau" | AGREE | No causal verb | FR:86 |
| B43 | 129-130 | +13,7 s (27,8 s at 7 h) for drop; +3,2 s for pickup; mean over scenarios | AGREE | — | FA:8-9 |
| B44 | 130-131 | 7,37 s = pooled over 2.338 riders, including weekend riders with 0 | AGREE | 17.224.334,6 / 2.338 = 7.367 ms | ADD1:19; PA:604 |
| B45 | 134-135 | 2.305/2.305 within 2 s when the dispatch part is 0 | AGREE | 2.338 − 33 = 2.305 | FA:28; RX:8; FFA:131-132 |
| B46 | 135-136 | "mức 0,17 % … là mức một dự báo theo giờ trong ngày đạt được trong mô phỏng" | LABEL | The source calls it the **ceiling** ("mức trần") for this forecast type in a near-deterministic world. The draft drops the best-case framing. | FR:167-169; I02 |
| B47 | 139-141 | Figure narrative: mostly explained on weekdays, almost the reverse in snow; the remainder is not "không thể biết trước" | AGREE | — | FA:30; SNOW:10; K19 |
| B48 | 148-156 | Weekday bar: 82 / 5.353 / 783 s (1,3 / 86,1 / 12,6 %); 68 riders, 6.217 s; x = 0,1445 and 9,6145 | AGREE | Recomputed x = 0,14455 and 9,61452 | FA:30; RX:3 |
| B49 | 157-166 | Snow bar: 8,6 / 251,5 (7,3 %) / 3.185,9 s (92,5 %); 41 riders; x = 0,0273 and 0,8302 | AGREE | Recomputed 0,02734 and 0,83016; 92,45 % and 7,30 % | NEW:5; RP1:24-26; SNOW:10 |
| B50 | 175-179 | Caption: signed split of eq:so | AGREE | Weekday numbers are FFA's signed sums. In snow the HIST overshoot is 0, so the clipped and signed versions are equal. | FFA:133-137; RP1:26 |
| B51 | 186-187 | Forecast in the dispatcher: C and deadline rule at 30 s; 16 scenarios at 7 h and 8 h | AGREE | — | FR:117; FB:2-30 |
| B52 | 187-188 | 3 of 32 runs stopped "vì xe trong FleetPy tới một điểm đón muộn hơn … 1,67 hoặc 2,69 giây" | LABEL | The counts agree. But FleetPy **computed** a projected arrival past the latest pickup and stopped the run (PLAN_INFEASIBLE); no vehicle actually arrived late. | FR:120-121; RX:13-15; FB:31 |
| B53 | 188 | Luật C needed no recovery in the completed runs | AGREE | 0 non-normal in 14 C-30F runs | FR:34; FB:38 |
| B54 | 188-189 | 47,6 % vs 62,8 %, mean over 15 scenarios | AGREE | Same 15 cells; see §1(c) | RX:11; RXPY:24, 29 |
| B55 | 190 | Deadline rule's own-break share at 7 h: 39,0 → 11,0 % (8 scenarios) | AGREE | — | RX:9; FB:41 |
| B56 | 190-191 | The nghiavu number depends on the promise method | AGREE | — | FR:133 |
| B57 | 191-192 | Promise layer chosen; scope limited to the version tried | AGREE | — | FR:141-146 |
| B58 | 195 | Three fixed models; 90th percentile of per-rider lateness from features known at promise time | AGREE | Target A − D0 | MLS:26-39, 63-69 |
| B59 | 196 | "bỏ số khách khác trên xe" | LABEL | The variant drops two counts: other requests assigned to the vehicle's plan (`other_assigned`) and those already on board (`other_onboard`). | MLS:19-23, 67-68 |
| B60 | 196-197 | Control = forecast promise + uniform pad, "cùng độ dài thêm trung bình 30 giây" | LABEL | (i) The forecast here uses the **fixed 12–13/11 profile**, not the source-day rule of 4.7. (ii) The 30 s is matched on the calibration day 14/11; on the test days the control's mean extension was 37,2 / 31,8 s (U). | MLS:37-39, 73-80; MLX:3, 11; ML:6-7 |
| B61 | 197-198 | On the fixed-traffic set the control is the uniform pad | AGREE | — | MLS:80 |
| B62 | 198 | "Mọi phép so dùng các ngày không dùng để học" | LABEL (omission) | True, but the test days **were inspected before**. This must be said. | MLS:9-10, 43-61 |
| B63 | 198-205 | The four conditions | AGREE | Text matches | MLS:91-95 |
| B64 | 208 | No model met all four | AGREE | Checked every setting, including static LOCKS and C-120 | ML:4-42 |
| B65 | 208 | Under luật C, no further reduction | AGREE | +0,00 pp on both days | ML:14-15, 45-46 |
| B66 | 208-209 | U: −0,69 pp on 15/11 (145 riders) and 0 on 16/11; promises too long | AGREE | 15/11: +4,4 s mean, +21,8 s p90. 16/11: +3,8 s, +21,6 s, +2,0 pp early. | ML:6-7, 49, 51 |
| B67 | 209-211 | FREE: 12,89 → 11,65 % of 807 riders; 7,1 % early vs 0 % | AGREE | — | ML:21 |
| B68 | 211 | "Bỏ số khách trên xe không đổi kết quả nào" | OVERSTATED | Gains are identical only in the two diagnostic settings (U 15/11 +0,69; FREE +1,24). Elsewhere the variant differs: static LOCKS Y60 1,64 vs 2,02; static C-120 0,64 vs 0,51; FREE early 7,3 vs 7,1. It never changes the verdict. | ML:21, 26, 31, 67-69 |

### §4.8 So với cách đệm lời hứa (l. 215-333)

| ID | Line | Claim | Verdict | Correct value / note | Anchor |
|---|---|---|---|---|---|
| B69 | 218-219 | U + forecast + 30 s gives 2.328 not late > 60 s per 3.672, equal to C-30 + forecast | AGREE | — | ADD1:15, 19 |
| B70 | 219-220 | 2.366 vs 2.338 at 120 s | AGREE | — | ADD1:15, 19 |
| B71 | 220 | 37,2 vs 7,4 s | AGREE | Pooled 37,18 / 7,37 | ADD1:15, 19 |
| B72 | 223 | Pad = +30 s on every rider's forecast first promise; a replay | AGREE | Extension 7,18 + 30 = 37,18 | ADD1:15; ADD1 header (D = D0 + k) |
| B73 | 224-225 | U's decisions are unchanged, so this is not a matched control; 2.207 shared riders | AGREE | Padded U is correctly called a replay | C04; ADD1:145 |
| B74 | 225-226 | Three blocks of similar extension | AGREE | — | ADD1:14-26 |
| B75 | 231-233 | Caption: denominators and pooling | AGREE | — | ADD1:10-26 |
| B76 | 245 | U fc: 2.434 / 137 / 2.297 / 2.347 / 7,18 | AGREE | — | ADD1:14 |
| B77 | 246 | C-30 fc: 2.338 / 10 / 2.328 / 2.338 / 7,37 | AGREE | — | ADD1:19 |
| B78 | 247 | C-120 fc: 2.387 / 65 / 2.322 / 2.379 / 7,27 | AGREE | — | ADD1:24 |
| B79 | 251 | U fc + 30: 2.434 / 106 / 2.328 / 2.366 / 37,18 | AGREE | — | ADD1:15 |
| B80 | 252 | C-30 fc + 30: 2.338 / 2 / 2.336 / 2.338 / 37,37 | AGREE | — | ADD1:20 |
| B81 | 256 | U fc + 60: 2.434 / 87 / 2.347 / 2.386 / 67,18 | AGREE | — | ADD1:16 |
| B82 | 262-263 | Reading: 106 of 2.434 → 2.328 per 3.672 | AGREE | — | ADD1:15 |
| B83 | 266-269 | "Thứ nhất": 2.336 vs 2.328; 2.338 vs 2.366; about five times (37,18 / 7,37) | AGREE | Ratio 5,047 | ADD1:93-95 |
| B84 | 272-274 | 4/2.338 vs 44/2.434 early; within ±60 s: 2.324 vs 2.284 | AGREE | — | ADD1:84-85, 96 |
| B85 | 279-281 | Caption haiphia | AGREE | — | ADD1:84-92 |
| B86 | 293 | U fc: 8 / 2.289 / 87 / 17 / 2 | AGREE | — | ADD1:14, 86 |
| B87 | 294 | C-30 fc: 4 / 2.324 / 0 / 0 / 0 | AGREE | — | ADD1:19, 84 |
| B88 | 295 | C-120 fc: 2 / 2.320 / 8 / 0 / 0 | AGREE | — | ADD1:24, 88 |
| B89 | 296 | U fc + 30: 44 / 2.284 / 68 / 11 / 1 | AGREE | — | ADD1:15, 85 |
| B90 | 297 | C-30 fc + 30: 44 / 2.292 / 0 / 0 / 0 | AGREE | — | ADD1:20, 87 |
| B91 | 298 | U fc + 60: 1.033 / 1.314 / 48 / 8 / 1 | AGREE | — | ADD1:16, 89 |
| B92 | 304-305 | Reading: 1.033 and 1.314 | AGREE | — | ADD1:16, 89 |
| B93 | 308-309 | 68 riders late > 2 min and 1 late > 10 min, vs 0 under C | AGREE | — | ADD1:15, 19 |
| B94 | 309-310 | The 28-lượt lead comes with 96 more served | AGREE | — | ADD1:97 |
| B95 | 313-314 | Padding keeps 174 moved riders and one moved 590,1 s | AGREE | — | ADD1:104; C20 |
| B96 | 314-315 | C caps this at "nhiều nhất 29,2 giây (Bảng doidieuphoi), kể cả … cuối tuần … và ở chiều tuyết" | LABEL | 29,2 s is the maximum on the main set (and also on the weekend scenarios). The snow set is separate, with a maximum of 25,2 s, and its runner is unverified. The cited table (PA:422-436) has neither weekend nor snow values; they are in PA:453-456 (section `muc:c4-dieuphoi`). | ADD1:106, 113; N-26 (SNOW1:10); N-28 |
| B97 | 318 | Deadline rule + forecast: 2.338 served and 2.328 not late > 60 s | AGREE | — | ADD1:29 |
| B98 | 319 | Deadline rule recovers at 41,3 % of decisions (mean over scenarios) | AGREE | — | ADD1:189 |
| B99 | 319-320 | Breaks its own promise in 28/34 scenarios; C never does | AGREE | Note: the deadline rule's own promise is its non-forecast first promise + 30 s, which the replay does not change | ADD1:189, 193; N-21 |
| B100 | 323 | C-120 + forecast: 2.379 at 120 s, above the pad's 2.366 | AGREE | (At 60 s it is 2.322, below the pad's 2.328; not mentioned, but not wrong.) | ADD1:15, 24 |
| B101 | 324 | About one fifth of the pad's extension; 47 fewer served than U | AGREE | 0,1956; 2.434 − 2.387 | ADD1:98 |
| B102 | 324-325 | "một điểm đo thêm … không phải mức trần tốt nhất" | AGREE | — | K36 |
| B103 | 328-330 | Padding is competitive on the 120-s count; serves 96 more | AGREE | — | ADD1:97 |
| B104 | 330-331 | C bounds each rider's dispatch part, even without forecast; costs 96 served and 242 shared riders | AGREE | — | N-20; N-28; ADD1:140 |
| B105 | 331 | "Hai cách dùng chung được" | AGREE | The C-30 + forecast + 30 s row exists | ADD1:20 |
| B106 | 331-332 | No evidence of value; it is the operator's choice | AGREE | No business claim | D20; I10; K38 |

### §4.9 Chiều tuyết (l. 336-386)

| ID | Line | Claim | Verdict | Correct value / note | Anchor |
|---|---|---|---|---|---|
| B107 | 339-340 | 601 riders; 41 → 34 | AGREE | — | RP1:7-8; NEW:5 |
| B108 | 340-341 | 6,82 → 5,66 % pooled; 7,19 → 5,94 % mean over scenarios | AGREE | 41/601 = 6,822; 34/601 = 5,657 | SNOW:10; RP1:7-8 |
| B109 | 344 | 8 scenarios at 14 h and 15 h, C-30; runner not re-checked | AGREE | — | SNOW:2-9; X3-10 |
| B110 | 344-346 | 8,6 of 3.445,9 s to dispatch; 251,5 s explained by history | AGREE | — | NEW:5 |
| B111 | 349-350 | "trộn" = geometric mean of historical growth and recent same-day trend | AGREE | BLEND = √(HIST · MOM) | FNS:30, 146-150 |
| B112 | 350-351 | 19 uses morning data not given to the window; the post-hoc threshold rule also gives 19 | AGREE | REGB-1.1/1.2/1.3 = 19 | RP1:11, 14-16; FNS:17, 35; FNS2:8-10 |
| B113 | 356-358 | Caption: late = pooled count; extension = mean over scenarios; retrospective on a seen day | AGREE | — | RPL:1-2, 96-106 |
| B114 | 367 | Không dự báo: 41 / 0 | AGREE | — | RP1:7 |
| B115 | 368 | Lịch sử: 34 / 2,0 | AGREE | — | RP1:8 |
| B116 | 369 | Trộn trong khung: 21 / 8,5 | AGREE | — | RP1:10 |
| B117 | 370 | Trộn có buổi sáng: 19 / 9,5 | AGREE | — | RP1:11 |
| B118 | 371 | Trộn trễ một khung: 29 / 9,0 (prefix, lagged trend, current anchor) | AGREE | — | RP1:12; FNS:18-20 |
| B119 | 372 | Đệm cùng giá @ trộn trong khung: 27 / 8,3 | AGREE | — | RP1:18; RPL:12, 86-88 |
| B120 | 373 | Hệ số thật: 0 / 18,8 | AGREE | — | RP1:17 |
| B121 | 379-380 | Reading: 21 of 601, 8,5 s | AGREE | — | RP1:10 |
| B122 | 383-384 | "Theo sổ", +886,9 s (25,7 %) explained; 2.299,0 s (66,7 %) remains | LABEL | The numbers agree (25,74 %; 66,72 %). But they come from the replay's **clipped** rule (each rider's explained part is capped at their lateness less dispatch). That is not the signed sum of eq:so; BLEND-pre overshoot is 6 s. | NEW:5; RPL:14-15, 113-115; RP1:29 |
| B123 | 384 | A previewed event | AGREE | — | F13; I11 |
| B124 | 384-385 | 5 snow spells ≥ 25,4 mm in 9/2018–12/2019, including this one | AGREE | 2018-11-15; 2019-02-12; 2019-02-20; 2019-03-01..04; 2019-12-02 (Central Park, dates ≤ 2 days apart joined) | NEW:9; WX17:4-5; WX |

### §4.10 Kiểm tra tính hợp lệ (l. 389-422)

| ID | Line | Claim | Verdict | Correct value / note | Anchor |
|---|---|---|---|---|---|
| B125 | 392-393 | No rider over the cap; maxima 29,2 / 118,9 s | AGREE | 29.239 / 118.938 ms | ADD1:106, 108, 193 |
| B126 | 393-394 | 0 of 20.101 and 0 of 20.435 decisions recovered | AGREE | Not framed as an advantage over U | ADD1:120-121 |
| B127 | 397 | "Giới hạn tính toán không cắt kết quả trên tập này" | OVERSTATED | Only three **generator** counters were audited: candidate cap, exploration work cap and request bound. Not audited: the repair-request cap (`OmittedRepairRequestCount`), and the work and time limits of the check step and the CP-SAT solver. CH3:687-689 itself says sinh, kiểm and giải all have limits. | RCA:129-132; R15-audit.py:76-79; CMOD:68-82; GEN:288-297; X3-17 |
| B128 | 397-399 | Four configurations; 100-candidate cap and exploration cap never omitted a candidate | AGREE | cap_applied 0, omitted_by_cap 0, work_exhausted 0 | ADD1:119-122; GEN:298-322 |
| B129 | 399-400 | The 2-request bound deferred one request once per configuration over 34 runs | AGREE | omitted_requests = 1 (sum of `omittedRequestCount`) | ADD1:119-122; GEN:54-95; RCA:132 |
| B130 | 400-401 | "…phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán" | LABEL | This is the approved K34 wording, but given B127 it must read "các giới hạn của bộ sinh đã kiểm". | K34; as B127 |
| B131 | 401 | Generator not exhaustive; insertion only | AGREE | — | X3-03 |
| B132 | 404-406 | Head of tiêu chí 3 saturated at 100 % in 3.503 / 3.506 / 3.504 decisions | AGREE | util_present = incumbent_1e6 = bound_1e6 | ADD1:119-121 |
| B133 | 406 | Because the vehicle, pickup and drop switches have cap 0 | AGREE | — | A07; X3-07 |
| B134 | 409-410 | Policy files byte-identical between the two sets; runner settings differ | AGREE | The main-set C-120 hash ac0f9758… equals the WP14 hash | NEW:11, 13; run_t38c120.py:21 |
| B135 | 413-414 | "Các số của tập kiểm tra chính được ít nhất hai bộ đọc viết độc lập tính lại" | OVERSTATED | True for the main counts (served, late, timely, extension, exposure). Not every number: the shared-rider counts 555 / 313 / 428 were counted by one rule only ("Codex không đếm lại chỉ số này"), and the deadline rule was checked only against Codex A. CH3:711 says "các số đếm chính". | ADD1:33-78; N-09 lưu ý |
| B136 | 414-415 | Per-rider match on 7.159 riders | AGREE | 2.434 + 2.338 + 2.387 | ADD1:76 |
| B137 | 415 | `muc:kiemtra` reports 382.006 revision records | AGREE | — | CH3:707 |
| B138 | 415-417 | Re-run on 12/10/2026, LF line endings: 1.024/1.025 passed; the remaining test passes alone with an untracked file | AGREE | 10 + 138 + 191 + 108 + 82 + 14 + 201 + 133 + 147 = 1.024; dirty run 1/1. **Conflicts with CH3:705-706** ("chưa chạy lại"). "đúng mã nguồn" rests on A28; the core commit is only Codex-checked (I13). | TLOG:1-4, 43-105; TDIRTY:1-7; TR:12-17 |
| B139 | 420-421 | The checks show numbers match the records, not realism | AGREE | — | I01; K41 |

### §4.11 Thảo luận và hạn chế (l. 425-488)

| ID | Line | Claim | Verdict | Correct value / note | Anchor |
|---|---|---|---|---|---|
| B140 | 428 | A table of trade-off points, not a recommendation | AGREE | — | I10 |
| B141 | 429 | 96 served and 242 shared riders lost | AGREE | — | ADD1:12, 17, 140 |
| B142 | 429-430 | Each rider's dispatch part ≤ 30 s | AGREE | — | A06; ADD1:106 |
| B143 | 430 | Fewer late at all four thresholds | AGREE | 203 / 102 / 18 / 2 vs 76 / 11 / 0 / 0 | ADD1:12, 17; PA:330-341 |
| B144 | 430-431 | "Trần 120 giây là một điểm ở giữa" | LABEL | It is between only in served (2.387). At the 120-s threshold it is above both: 2.366 vs 2.332 and 2.327. | L1a-02; ADD1:197 |
| B145 | 431 | Padding serves more with longer promises | AGREE | — | ADD1:15 |
| B146 | 434-436 | k > 0,756 m (96/127) | AGREE | 0,7559; symbolic; different cohorts stated | C29; ADD1:186 |
| B147 | 437-438 | Higher-load hypothesis | AGREE | Labelled "giả thuyết chưa kiểm" | OUTLINE 4.11 |
| B148 | 445 | One simulator | AGREE | — | I01 |
| B149 | 446-447 | City-wide factor, 15-min bins, base at 00:00; near-deterministic | AGREE | — | B06; B07; F10 |
| B150 | 448-450 | Dwell 0 s (3 runs) vs 30 s in FleetPy; 96-node closure | AGREE | — | SERV:2-4; FLEET:423-424; B03 |
| B151 | 451-452 | No rider response; no reassignment | AGREE | — | I07; X3-39 |
| B152 | 458-459 | 34 dependent scenarios over 5 days, one run each | AGREE | — | B09; B11 |
| B153 | 460-461 | Thresholds, splits and 120 s chosen after seeing development data; exploratory | AGREE | — | I06; K42 |
| B154 | 462-463 | 0,535 riders on board including idle (U) vs about 1,33 (180 vehicles, 21.400 requests) | AGREE | — | LOAD:2; FLEET:447-449; J18 |
| B155 | 463-464 | Selected trips shorter: median 165 vs 196 s | LABEL | The values agree, but they are over the **49** panel-A fixtures (34 test + 15 calibration), not the 34-scenario main set the bullet is about | SEL6:1-4; B13 |
| B156 | 470-471 | 34 of 1.471 riders shown a pickup time after the latest pickup | AGREE | — | RX:2; FR:70 |
| B157 | 472-473 | A rebuilt runner may differ; the snow runner is unverified | AGREE | — | I13; X3-10 |
| B158 | 479-481 | Cost-first selector not run; per-step cap not implemented | AGREE | — | H12; E09 |
| B159 | 482-484 | Deadline component at 30–60 s vs 900 s; Hörl–Zwick relaxed deadline not run | AGREE | — | J10; J11; K27 |
| B160 | 485-486 | 30 s is not a perception threshold; no willingness-to-pay data; no level called best | AGREE | — | D20; K52; K36 |

---

## 3. Cross-references and citations

**Labels and references.**

- Part B defines 12 labels: 6 `muc:`, 5 `bang:` and `hinh:c4-so`. None collides with CH3 v3 or PA v1 (grep count 0
  for each).
- The draft uses 19 distinct `\ref`/`\eqref` targets and all resolve:
  - In CH3: `bang:rangbuoc` (115), `muc:dubao` (484), `eq:so` (593), `muc:gioihan` (685), `muc:kiemtra` (701).
  - In PA: `bang:c4-tran120` (579), `bang:c4-nghiavu` (286), `bang:c4-doidieuphoi` (422), `bang:c4-phanbotre` (330),
    `muc:c4-congdon` (711).
  - The other 9 are defined in part B.
- Incoming references from CH3 and PA to `muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet` and
  `muc:c4-hople` all resolve to part B.
- Only one reference has a content mismatch: B96 points to `bang:c4-doidieuphoi` for the weekend and snow values, which
  are not in that table.

**Citations.**

- `schulz2026` exists in `10-tai-lieu.tex` (line 116, Schulz & Pfeiffer, OR Spectrum 48:541–586).
- `engelhardt2026` and `horl2022` are **NEW**. They are not in `10-tai-lieu.tex`. Their metadata is proposed in
  `07-chuong3-v3-NOTES.md` (lines 119-139) and REG X3-40, and they must be added before the build.

**Cross-chapter conflict.** CH3:705-706 says "1.025 trên 1.025 … chưa chạy lại khi viết khóa luận". §4.10 (l. 415-417)
reports the 12/10/2026 re-run (1.024/1.025, plus 1/1 separately). One of the two must change; the proposed CH3 text is
item 9 of §6.

## 4. Point-3 checks (comparisons)

| Check | Result |
|---|---|
| Different served cohorts | Stated where it matters: l. 19, 225 (2.207 shared), 325, 436. |
| Padded U as replay, not matched control | Stated explicitly at l. 223-225. OK. |
| "0 decisions forced" as an advantage of C over U | **Not present.** Every "không phải phục hồi" is either C vs the deadline rule (l. 188, 319-320) or a validity statement (l. 393-394). l. 428-431 deliberately omits it. OK. |
| Causal wording about the ledger split | None. The draft uses "tính cho điều phối", "được hồ sơ lịch sử giải thích" and "phần còn lại … không phải phần không thể biết trước". OK. |
| "tối ưu" / business value | No "tối ưu". "tốt nhất" appears only negated (l. 325, 486). k and m are symbolic, and l. 332 and 431 disclaim value. OK. |
| Sealed plans, preregistration, predictions | None found by grep: niêm phong / dự đoán / đăng ký / ghi trước / đạt-trượt. The four ML conditions are given without saying when they were set. OK. |

## 5. Register and notes issues

- **N4B-01 (lưu ý).** It describes PV as only "chạy lại bằng mã đã kiểm". In fact PV is Q4's **full lexicographic re-solve
  under the recorded order** (Q4:15-16, 131-138). The 62.837 claim should be anchored there, not at WPCHK.
- **N4B-03.** "phép đệm không tính chỉ số này" is wrong. `E_pad` is computed (FFA:141) and saved (CELLS). The value is 0 %
  for C-30 on 21 scenarios.
- **NOTES §6 item 2.** The claim that pooled counts behind the scenario-mean rates are not in saved outputs is only
  partly true. CELLS stores each cell's share and served count, and share × served is an exact integer (max residue 0,0).
  For C-30 on 21 scenarios:

  | Window | Riders | Không dự báo | Đệm cùng giá | Dự báo |
  |---|---:|---:|---:|---:|
  | All 21 scenarios | 1.471 | 68 | 22 | 2 |
  | 7 h | 444 | 60 | 17 | 1 |
  | 8 h | 609 | 8 | 5 | 1 |
  | 17 h | 418 | 0 | 0 | 0 |

  U on 21 scenarios: 129 → 63 late riders of 1.512. These counts can be added to Bảng `bang:c4-dubao` as derived values
  (my arithmetic on a saved output), if a register row is added first.
- **N4B-08.** It omits the fixed 12–13/11 profile (MLS:37-39; MLX:11). NOTES §6 item 12 mentions it but chose to leave it
  out of the text; see B60.
- **NOTES line count.** 497 is wrong; the file has 488 lines.
- **ADDENDUM-3 header.** It still says "bản nộp v6". This is cosmetic.

## 6. Summary count (160 items)

| Verdict | Count | IDs |
|---|---:|---|
| AGREE | 142 | all others |
| WRONG | 1 | B33 |
| OVERSTATED | 3 | B68, B127, B135 |
| LABEL | 13 | B01, B05, B07, B46, B52, B59, B60, B62, B96, B122, B130, B144, B155 |
| CANNOT CHECK | 1 | B23 |

References: 19/19 resolve. Citations: 1 exists, 2 are new and must be added (`engelhardt2026`, `horl2022`).

## 7. Required corrections, ranked, with replacement text

**1. B33 (WRONG), l. 107.** Replace the row with:
```
Tới sớm quá 60 s, cả 21 kịch bản & 0 & 0 & 0,08\\
```
and change its EV line to:
```
% EV: FA:8 (E naive 0, disp 0,0008); FFA:139-141 + CELLS cột E_pad (đệm cùng giá: 0 trên 1.471 khách)
```

**2. B60 and B62 (doubt b), l. 196-198.** Replace "Đối chứng là lời hứa theo dự báo … không dùng để học." with:
> Đối chứng là lời hứa theo dự báo cộng một khoảng đệm đều, chỉnh trên ngày hiệu chỉnh 14/11 để độ dài thêm trung bình
> bằng 30 giây như các mô hình; trên tập tắc đường cố định là đệm đều. Trong phép thử này, lời hứa theo dự báo dùng một
> hồ sơ tắc đường cố định của ngày 12 và 13/11, không theo quy tắc ngày nguồn ở trên. Mọi phép so dùng các ngày không
> dùng để học, nhưng các ngày này đã được xem trước.

EV: add `MLS:9-10, 37-39, 73-80; ml_pilot_extract.py:3, 11`.

**3. B127 and B130 (OVERSTATED), l. 397 and 400-401.**
- Replace "Giới hạn tính toán không cắt kết quả trên tập này." with:
  > Các giới hạn của bộ sinh phương án không cắt kết quả trên tập này.
- Replace "Chênh lệch giữa các cấu hình … không phải của giới hạn tính toán." with:
  > Chênh lệch giữa các cấu hình vì vậy phản ánh tác động của cả gói cam kết, không phải của các giới hạn của bộ sinh đã
  > kiểm. Giới hạn số yêu cầu sửa lại của mỗi xe và giới hạn khối lượng của bước kiểm và của bộ giải không được đếm.

EV: add `CandidateModels.cs:68-82; recompute_addendum_1.py:129-132; X3-17`.

**4. B07 and B05 (doubt a), l. 23-25.** Replace from "Ở mỗi lượt quyết định đã ghi" to "62.837 lựa chọn đã ghi." with:
> Ở mỗi lượt quyết định đã ghi, bài toán chọn được giải lại bằng một chương trình viết riêng, trên chính các phương án
> và giá trị tiêu chí đã ghi, nhưng bỏ tiêu chí 3; mô phỏng không chạy tiếp từ lựa chọn mới. Với thứ tự gốc, chương
> trình này cho đúng cả 62.837 lựa chọn đã ghi của năm cấu hình trên tập này (ghép tự do, không trần và trần 120, 60,
> 30 giây).

EV line 26 becomes:
```
% EV: N4B-01; N4B-02; H03 (PV:1-7; q4_cost_first_reselect.py:15-19, 131-138; NEW:7; R17-verify-portfolios.py:29; cùng mã chạy hai lần, không phải hai bản hiện thực độc lập; WPCHK:12-15 chỉ kiểm điều kiện cần); H10
```

**5. B135 (OVERSTATED), l. 413-414.** Replace "Các số của tập kiểm tra chính được ít nhất hai bộ đọc viết độc lập tính
lại từ bản ghi thô và khớp trong phạm vi đã kiểm." with:
> Các số đếm chính của tập kiểm tra chính (phục vụ, trễ, không trễ, độ dài thêm của lời hứa, dời do điều phối) được ít
> nhất hai bộ đọc viết độc lập tính lại từ bản ghi thô và khớp trong phạm vi đã kiểm; số khách đi chung chỉ được một quy
> tắc đếm.

**6. B68 (OVERSTATED), l. 211.** Replace "Bỏ số khách trên xe không đổi kết quả nào." with:
> Bỏ hai biến trạng thái xe không làm mô hình nào thỏa đủ bốn điều kiện; với điều phối không trần ngày 15/11 và với ghép
> tự do, mức giảm tỉ lệ trễ không đổi.

**7. B96 (LABEL), l. 314-315.** Replace "Luật C trần 30 giây giới hạn phần này … và ở chiều tuyết." with:
> Luật C trần 30 giây giới hạn phần này của mỗi khách: nhiều nhất 29,2 giây trên tập kiểm tra chính, kể cả ở 13 kịch
> bản cuối tuần không có dự báo, và 25,2 giây ở chiều tuyết (mục~\ref{muc:c4-dieuphoi}).

**8. B01 (LABEL), l. 17-18.** Replace the first sentence with:
> Điều phối không trần và luật C trần 30 giây dùng cùng tệp cấu hình bộ chạy và cùng bộ chọn ưu tiên ổn định; hai tệp
> chính sách cam kết của chúng chỉ khác nhau ở trần giờ trả.

**9. B138 cross-chapter.** Update CH3:705-706 to match §4.10; the alternative is to drop l. 415-417. Proposed CH3 text:
> \textbf{Kiểm thử phần mềm:} khi chạy lại ngày 12/10/2026 trên đúng mã nguồn đã dựng bộ chạy (kiểu xuống dòng LF),
> 1.024 trong 1.025 kiểm thử tự động đạt; kiểm thử còn lại đòi cây làm việc có tệp chưa được ghi nhận và đạt khi chạy
> riêng với một tệp như vậy.

**10. B46 (LABEL), l. 135-136.** Replace "Vì vậy mức 0,17\% … không phải hiệu quả ngoài đời." with:
> Vì vậy mức 0,17\% của 21 kịch bản là mức tốt nhất mà một dự báo theo giờ trong ngày có thể đạt trong mô phỏng gần như
> tất định này, không phải hiệu quả ngoài đời.

**11. B144 (LABEL), l. 430-431.** Replace "Trần 120 giây là một điểm ở giữa;" with:
> Trần 120 giây nằm giữa về số lượt phục vụ nhưng có nhiều lượt không trễ quá hai phút nhất trong ba cấu hình;

**12. B122 (LABEL), l. 383.** Replace "Theo sổ, mô hình có dữ liệu buổi sáng" with:
> Theo phép phát lại (phần được giải thích của mỗi khách không vượt độ trễ của khách đó), mô hình có dữ liệu buổi sáng

Add `RPL:14-15` to the EV line.

**13. B52 (LABEL), l. 187-188.** Replace "vì xe trong FleetPy tới một điểm đón muộn hơn giờ đón muộn nhất 1,67 hoặc 2,69
giây" with:
> vì FleetPy tính rằng xe sẽ tới một điểm đón muộn hơn giờ đón muộn nhất 1,67 hoặc 2,69 giây và dừng lần chạy

**14. B59 (LABEL), l. 196.** Replace "cùng mô hình ấy nhưng bỏ số khách khác trên xe" with:
> cùng mô hình ấy nhưng bỏ hai biến trạng thái xe (số khách khác đã gán cho xe và số khách đang trên xe)

**15. B155 (LABEL), l. 463-464.** Replace "Các chuyến được chọn cũng ngắn hơn tập đủ điều kiện (trung vị đi thẳng 165 so
với 196 giây)." with:
> Ở cả 49 kịch bản dựng từ dữ liệu thật, các chuyến được chọn ngắn hơn tập đủ điều kiện (trung vị đi thẳng 165 so với
> 196 giây).

**16. Bibliography.** Add `\bibitem{engelhardt2026}` and `\bibitem{horl2022}` to `10-tai-lieu.tex` using the metadata in
REG X3-40 and `07-chuong3-v3-NOTES.md`.

**17. Optional (no error).**
- Add the pooled counts from CELLS (§5) to Bảng `bang:c4-dubao`. Add a register row first.
- At l. 323-324, also say that at the 60-s threshold C-120 + forecast (2.322) is below the 30-s pad (2.328), so the
  "núm vặn" point is not presented one-sidedly.

*End of R27. Written by Claude (independent fact checker), 2026-10-12. Only this file was created.*
