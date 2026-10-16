# Round 29 — Codex review of Chapter 4, part B v7

**Verdict: ACCEPT WITH REQUIRED CORRECTIONS; do not integrate v7 unchanged.** The fixed-state screen, main padding tables, forecast means, C-120 point, and observed cap/recovery counts are supported. The substantive errors are the ML comparison's description, a falsely missing early-arrival result, the undisclosed change from signed to clipped snow accounting, and overbroad interpretation of computational counters. The deadline paragraph also needs to distinguish its original obligation from a replayed forecast quote.

## 1. Scope, method and anchors

Reviewed on 12/10/2026. Draft line numbers refer to the **488 physical lines** of `rewrite-2026-10/drafts/09-chuong4-phanB-v7.tex`, not earlier versions. Read the writer's NOTES, R23 and R25 context, WRITING-BRIEF, relevant OUTLINE-V2 rows and §7.2, RD §8, the register and Addendum 1 §0 corrections, Addenda 2/3, TESTRUN, and the saved evidence/code below. No `rewrite-2026-10/reviews/*CH4B*` file was read.

No simulations, builds, installations, test runs, model fitting, thesis edits, draft edits, or register edits were performed. This review is the only new file. All writes were inside `codex-work`; the review was exclusive-created.

**Fresh arithmetic in this round:** all six rows of both padding tables from the independent Codex saved per-rider extraction; fixed-screen ratios and cost estimands from saved decision details; forecast means/counts and both cluster-t intervals from the full-precision cells TSV; figure sums/shares/coordinates; paired dispatcher-forecast counts from the independent B extraction; differences/ratios/profit threshold. I also read the eight saved snow transcripts through the existing reader, with bytecode writes disabled, and recomputed historical/prefix signed and clipped sums. This was retrospective transcript analysis, not a simulation. ML metrics were checked against the corrected A1 report and detailed saved table; no learner was rerun.

**AGREE** = supported within its specified cohort and aggregation. **WRONG** includes a false definition or materially overstated scope even when the integer is right. **CANNOT CHECK** = evidence unavailable or outside this round's verification boundary. Agreement with a saved extraction is not a new independent full-transcript audit of every experiment.

Paths are relative to **S = `E:/Code/Report_INT3508/ridebound-scratchpad/`**, except absolute SRC/TRLOG paths. For JSON/TSV, named keys/columns and scenario IDs are the anchors.

| Key | File |
| --- | --- |
| REG / ADD / ADD2 / ADD3 | `rewrite-2026-10/evidence/EVIDENCE-REGISTER.md` / `EVIDENCE-REGISTER-ADDENDUM-1.md` / `EVIDENCE-REGISTER-ADDENDUM-2-CH3.md` / `EVIDENCE-REGISTER-ADDENDUM-3-CH4B.md` |
| RD / OUT | `rewrite-2026-10/REVIEW-DECISIONS-R20.md` / `OUTLINE-V2.md` |
| Q4 | `optimize/codex-debate/claude-work/r16-evidence/q4_cost_first_reselect.py` |
| WPCHK / WP17 / WPJ | `optimize/codex-debate/claude-work/r17-rebuttal/r17_wp14r_check.py` / `r17-wp14r-check-2026-10-10.txt` / corresponding `.json` |
| PV / PVJ / PVS / CASE / NEW | `optimize/codex-debate/codex-work/R17-portfolio-verification.txt` / corresponding `.json` / `R17-verify-portfolios.py` / `R17-C30-sum-case.txt` / `R18-verification.txt` |
| FA / FAT / FFA / FR / RX | `optimize/test-family-a-causal-no15-2026-10-06-report.txt` / corresponding `-cells.tsv` / `forecast_family_a.py` / `FORECAST-REPORT.md` / `report-extras/report-extras-2026-10-06.txt` |
| FB / FBS / RXS | `optimize/test-family-b-2026-10-06-report.txt` / `forecast_family_b.py` / `report-extras/report_extras.py` |
| BI / BIC | `optimize/independent-B/b_results.json` / `b_cells.tsv` |
| RP1 / RPL / FNS / FNS2 | `optimize/codex-debate/claude-work/r16-forecast/rider-nowcast-replay-2026-10-10.txt` / `rider_nowcast_replay.py` / `factor_nowcast_screen.py` / `factor_nowcast_screen_v2.py` |
| ML / MLT / MLS / MLR / MLE | `optimize/codex-debate/claude-work/ml-pilot-report-a1-2026-10-08.txt` / `ml-pilot-rows-a1-2026-10-08.tsv` (CSV despite suffix) / `ML-PILOT-SEALED.md` / `ml_pilot_run.py` / `ml_pilot_extract.py` |
| CXJ / ADD1 / ADDJ / SNOW1 | `optimize/codex-debate/codex-work/R19-stage1a-analysis.json`; `rewrite-2026-10/evidence/checks-addendum-1/recompute-addendum-1-2026-10-11.txt` / corresponding `.json` / `check-snow-c30-2026-10-11.txt` |
| SRC / GEN / CMOD / SEL / HVA | `C:/Code/RideBound-noworse/src/`; `RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs` / `CandidateModels.cs`; `RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs`; `RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs` under SRC |
| TR / TLOG / TDIRTY | `rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md`; `C:/RideBoundData/research/testrun-45f8026-eollf-2026-10-12.log` / `testrun-45f8026-eollf-dirtycheck-2026-10-12.log` |

## 2. Ranked required changes — exact Vietnamese replacement text

### 1. Correct the ML cost comparison, forecast vintage, preview caveat and ablation scope

**Lines 195–211; NOTES §6 item 12 and §11 item 3; ADD3 N4B-08.**

**WRONG:** “cùng độ dài thêm trung bình 30 giây” describes the test comparison inaccurately. Thirty seconds is a calibration target. The calibration mean historical extension is approximately 23,13 s, and the frozen forecast-plus-uniform control adds `E − mean(delta_cal)` to D0. On U's test days its actual mean extension is **37,219 s** (15/11) and **31,772 s** (16/11); the full model's means are **41,624 / 35,565 s**. There is no test rescaling. Sources: MLS:71–86; MLR:68–98; MLT rows `measured, U, test15/test16, all, E=30`.

The fixed profile uses **12–13/11 for all measured-traffic rows**, including fit/calibration rows; it is not the date-dependent source rule of the preceding forecast analysis. The test days were already inspected. “Ngày không dùng để học” is true for the fit split, but does not imply an untouched temporal holdout or that every historical-profile feature in the training rows obeys chronological source exclusion. Sources: MLS:9–10,37–61; MLE:11–28,50. NOTES deliberately omitting this distinction for length is not acceptable in an examiner-facing method description.

**WRONG:** “Bỏ số khách trên xe không đổi kết quả nào.” The ablation removes **both** other-assigned and other-onboard counts. It keeps the reported E=30 lateness gain for U and static FREE, but changes other metrics. Static FREE has early60 **7,063% vs 7,311%**, symmetric accuracy **81,289% vs 81,041%**, and p90 extension **62,536 vs 65,508 s**. U 15/11 has mean extension **41,624 vs 41,743 s**. These are actual differences, not identical results. Sources: MLS:19–23,65–69; MLR:30; MLT corresponding HGB/HGB-nostate rows. At static LOCKS E=30 even Y60 differs (2,02% vs 1,64% in ML).

Replace lines 195–199 with:

> Ba mô hình cố định ước lượng phân vị 90 của phần trễ còn lại sau dự báo: cây tăng cường độ dốc, cùng mô hình ấy nhưng bỏ hai biến trạng thái xe, và hồi quy phân vị tuyến tính. Hai biến trạng thái là số khách khác đã gán cho xe và số khách khác đang trên xe. Phép thử dùng một hồ sơ dự báo cố định từ ngày 12--13/11, khác quy tắc chọn ngày nguồn của phân tích trên. Với giao thông đo, mô hình học trên 12--13/11, hiệu chỉnh trên 14/11 và kiểm riêng từng ngày 15, 16/11 ở khung 7 giờ; các ngày kiểm đã được xem trước. Với tắc đường cố định, mô hình học trên các mẫu 1--3 của 12/11, hiệu chỉnh trên mẫu 4 và kiểm trên 13/11. Đối chứng là dự báo cộng đệm đều; ở tập tắc đường cố định, đối chứng này trùng đệm đều. Mức dài thêm mục tiêu 30 giây được đặt trên tập hiệu chỉnh, rồi giữ nguyên quy tắc khi kiểm; độ dài thêm thực tế trên ngày kiểm có thể khác 30 giây. Mô hình chỉ được coi là tốt hơn khi thỏa cả bốn điều kiện sau.

Retain the four existing conditions. Replace the opening of line 208 with:

> Trong phép so ở mức mục tiêu 30 giây này, không mô hình nào thỏa đủ bốn điều kiện.

Keep the verified gain/early figures, add **200 khách** after 16/11, and replace the last sentence of line 211 with:

> Ở các phép so của điều phối không trần và ghép tự do trên tập tắc đường cố định, bỏ hai biến trạng thái xe không đổi mức giảm tỉ lệ trễ được báo ở mức mục tiêu 30 giây; các chỉ số tới sớm và độ dài lời hứa vẫn có thể khác nhau.

This reports a limited negative finding, not evidence that ML or vehicle information is generally useless. Retarget EV to G02/G03/G05–G09 and the corrected N4B-08; no discussion of internal prediction/plan labels belongs in the thesis.

### 2. Replace the falsely missing early-arrival cell with the measured zero

**Line 106, `bang:c4-dubao`; ADD3 N4B-03; NOTES §6 item 3.**

**WRONG:** “chưa đo” and “phép đệm không tính chỉ số này.” FFA:141 explicitly computes `E_pad`, and FAT saves that column. For all **21 active C-30 scenarios it is exactly 0**. The pooled count is **0/1.471**; the unweighted scenario mean is also **0%**. Forecast early60 is 1/1.471 pooled, with an unweighted mean 0,0768049% → 0,08%.

Replace the row exactly with:

~~~tex
Tới sớm quá 60 s, cả 21 kịch bản & 0 & 0 & 0,08\\
~~~

Correct N4B-03 and NOTES §6 item 3 before using that row. The source is FAT's `arm=C-30`, dates 14–16/11, `E_pad` column, supported by FFA:110–142. The human-readable report's omission of the column is not absence of measurement.

### 3. Identify the clipped accounting in the snow follow-up

**Lines 383–385; REG F15 and ADD3's snow-method coverage.**

**AGREE** for the existing clipped-analysis numbers, **WRONG** if “Theo sổ” identifies them with Chapter 3's signed identity. RPL:14–15,113–115 replaces f for each selected rider by `max(0, min(D − P0, A − P0 − q))`. Chapter 3 `eq:so` uses the uncut signed f = D0 − p0. These coincide for the historical snow forecast, as N4B-05 correctly notes, but **not for BLEND-pre**.

Fresh read-only recomputation on the eight snow transcripts gives, for the same 41 naive-late riders:

| BLEND-pre measure | Seconds |
| --- | ---: |
| Uncut extension sum f | 1.144,761843 |
| Clipped explained sum | 1.138,354743 |
| Amount clipped | 6,407100 |
| Signed residual under `eq:so` | 2.292,605157 |
| Clipped residual used in RP1/NEW | 2.299,012257 |

The printed **886,9 s / 25,7% extra** and **2.299,0 s / 66,7% remaining** belong to the clipped rule. Under the uncut identity they would instead be **893,3 s / 25,9%** and **2.292,6 s / 66,5%**. Do not silently substitute one convention for the other. The historical bars in the figure remain correct.

To preserve the registered numbers, replace the first sentence of lines 383–384 with:

> Phép phát lại bổ sung giới hạn phần kéo dài của dự báo ở từng khách trong khoảng từ 0 đến phần trễ còn lại sau khi trừ phần tính cho điều phối; cách cộng này khác phần có dấu trong công thức~\eqref{eq:so}. Theo cách cộng có giới hạn đó, mô hình có dữ liệu buổi sáng giải thích thêm 886,9 giây, tức 25,7\% của 3.445,9 giây trễ, còn 2.299,0 giây (66,7\%) chưa được giải thích bằng các cách đã thử.

Keep the existing previewed-event and few-independent-events caveats. Register the clipping definition with RPL:14–15,113–115; F15 already supplies its numerical outputs.

### 4. Narrow the computational-limit claim to the counters actually checked

**Lines 397–402; ADD3 N4B-11; REG K34.**

**AGREE:** for each of U/C-30/C-120/M⁺-30, omitted-new-request total = 1; candidate-cap application/omitted-by-cap/work-exhausted counters = 0. **WRONG as a general conclusion:** “Giới hạn tính toán không cắt kết quả” and “chênh lệch ... không phải của giới hạn tính toán.” A queued request was deferred in each arm; equal omission totals do not prove identical affected requests/states or zero effect on outcomes. These counters also do not establish the effect of all solver/validation limits or all ungenerated plans. CMOD:100–118 has additional completeness conditions, and N4B-11 explicitly acknowledges that the repair-omission counter was not audited. The insertion-only search remains a restriction even without a 100-candidate/work-cap hit.

Replace lines 397–401 with:

> Trên 34 lần chạy của mỗi cấu hình được kiểm — điều phối không trần, luật C trần 30 và 120 giây, và luật hạn chót 30 giây — các bộ đếm được đọc không ghi nhận phương án bị bỏ vì giới hạn 100 phương án mỗi xe hay nhánh khám phá bị bỏ vì giới hạn khối lượng. Giới hạn 2 yêu cầu mới trong một lượt để lại tổng cộng một yêu cầu sang lượt sau ở mỗi cấu hình. Các số này không đo tác động của mọi giới hạn tính toán lên kết quả. Bộ sinh vẫn chỉ chèn yêu cầu mới vào kế hoạch đang có, nên không xét mọi cách điều phối (mục~\ref{muc:gioihan}).

Source: ADD1:119–122; GEN:54–95,298–345; CMOD:100–118; Codex R15-audit.py:76–79. This is a qualification of K34 itself: that registered shorthand is broader than its evidence. No new run is needed to make the claim honest.

### 5. Keep the original deadline obligation distinct from the forecast display metric

**Lines 318–321, with lines 186–192 as context.**

The numbers **2.338 / 2.328**, **41,3%**, and **28/34** are individually **AGREE**, but their juxtaposition after “luật hạn chót ... có dự báo” can falsely suggest all describe obligation checking against D0. Main-table forecasting is quote replay. The archived deadline gate still uses **p0 + 30 s**, with p0 the first nonforecast promise. Its 28/34 scenarios and 289/2.338 late30 riders belong to that obligation; ADD N-21 says so explicitly. For reference, the existing FAT `late30_disp` gives **86/2.338 in 22/34 scenarios** against the replayed D0 + 30 s. Those are different measurements, not replacements for the core's recorded obligation breaches.

Replace lines 318–320 with:

> Khi phát lại cùng lớp lời hứa theo dự báo, luật hạn chót 30 giây và luật C trần 30 giây đều có 2.338 lượt phục vụ và 2.328 lượt không trễ quá một phút. Phép phát lại không đổi cổng hạn chót của những lần chạy đã có: nghĩa vụ của luật hạn chót vẫn tính từ lời hứa đầu không dự báo. Theo nghĩa vụ đó, luật hạn chót phải phục hồi ở 41,3\% lượt quyết định (trung bình theo kịch bản) và có ít nhất một khách trễ quá hạn ở 28 trong 34 kịch bản; luật C không có lượt phục hồi hay khách vượt trần (Bảng~\ref{bang:c4-nghiavu}).

Sources: ADD N-16/N-21; ADD1:29,119–122,189–193; FAT `late30_naive` vs `late30_disp`; Chapter 3's p0/D0 definitions. The separate in-dispatcher forecast experiment changes the plans and initial core promises and must retain its own completed-scenario population.

### 6. Synchronize Chapter 3's historical test sentence with the documented rerun

**Part B 415–418 is AGREE; Chapter 3 v3 705–706 is stale.** It still says 1.025/1.025 was historical and not rerun during thesis writing. TLOG:43,48,60,63,80,85,87,92,105 sums to **1.024 passed / 1.025 total** on the clean LF clone; the named remaining test fails at lines 93–100. TDIRTY records one untracked marker and **1/1 passed** on the separate retry. Part B accurately distinguishes these two executions and is more precise than TR's compressed allowed wording. There is no need to change it to claim a single full-suite 1.025/1.025 run.

Replace the Chapter 3 item with:

> \item \textbf{Kiểm thử phần mềm:} khi chạy lại ngày 12/10/2026 trên đúng mã nguồn đã dựng bộ chạy, với kiểu xuống dòng LF, 1.024 trong 1.025 kiểm thử tự động đạt. Kiểm thử còn lại đòi cây làm việc có tệp chưa được ghi nhận, và đạt khi chạy riêng với một tệp như vậy.

Use the same registered N4B-13 anchor in both places, or keep the detail only in Chapter 3 and refer to it from Part B. This review did not rerun tests.

### 7. Limit the 30–60-second literature comparison to the main set

**Lines 482–484.** The cited paper's default **900 s** is AGREE. “Ở 30--60 giây” is inaccurate as a description of the entire thesis: the morning deadline arms also run through **300 s** (Chapter 3 v3's configuration table; R23/R25 corrections). The unrun relaxed-deadline and non-reproduction caveats are correct.

Replace the item with:

> \item Luật hạn chót chỉ mượn thành phần hạn chót của Schulz và Pfeiffer~\cite{schulz2026}; tập kiểm tra chính dùng 30 và 60 giây, còn tập chỉnh trần buổi sáng dùng các mức từ 30 đến 300 giây, thay vì mức mặc định 900 giây của bài đó. Hạn chót nới kiểu Hörl và Zwick~\cite{horl2022} chưa được chạy. Các phép so không tái lập phương pháp của các tác giả đó.

### 8. Finish denominator reporting and identify the dispatcher-forecast implementation

The draft usually labels aggregation correctly. Under the writing brief's literal count-and-denominator rule, a scenario mean still needs its definition/per-scenario count support; **do not relabel it as a pooled percentage**. NOTES §6 claiming these counts are absent from saved outputs is too strong: FAT saves full-precision rates and served counts, and BIC saves acknowledged and non-normal counts. Section 3 below gives usable counts.

Add after the forecast-table caption or immediately before the table:

> Mỗi tỉ lệ trong bảng là trung bình không trọng số của tỉ lệ từng kịch bản; mẫu số của từng kịch bản là số khách được phục vụ. Số đếm gộp theo khách được báo riêng và không thay cho trung bình theo kịch bản.

For the in-dispatcher paragraph, make its first two sentences explicit:

> Phép thử dùng lớp bọc v1.3 với hai khung dự báo, trên 16 kịch bản khung 7 và 8 giờ cho mỗi luật C và luật hạn chót 30 giây. Có 3 trong 32 lần chạy dừng; các số sau chỉ dùng 14 lần chạy hoàn tất của luật C và 15 lần chạy hoàn tất của luật hạn chót.

Then retain 1,67/2,69 s, the paired 47,6%/62,8% means, and the 39,0%/11,0% eight-scenario means. `optimize/run_forecast.py`:9,65–72 binds Family B to forecast-k2 configs; FR:117 and FBS:1 also specify K=2. Extend N4B-07/X3-29 with that checked setting. A compact optional addition for recovery counts is:

> Trên 15 kịch bản ghép theo cùng mã kịch bản, số gộp là 3.849 lượt phục hồi trong 8.496 lượt quyết định khi đưa dự báo vào, so với 5.121 trong 8.468 lượt khi không đưa vào; hai tỉ lệ gộp này khác các trung bình 47,6\% và 62,8\%.

For C's completed runs the available count is **0/7.839 acknowledged decisions in 14 scenarios**. Register newly used counts before inserting them in the thesis; their BIC anchors and calculation are supplied here.

## 3. Numerical audit

### 3.1 Section 4.6 — every screen number and the 62.837 claim

| Draft lines | Quantity | Verdict / checked result |
| --- | --- | --- |
| 16–20 | U/C-30 same WP4, same selector; only the drop cap differs; criteria 3/4 | **AGREE**, REG A08/H01, NEW:12; Chapter 3 `bang:rangbuoc` and X3-07. “Same runner configuration” is distinct from “same commitment-policy JSON.” |
| 22–25 | Fixed states, same saved eligible candidates, remove criterion 3; 62.837 original selections reproduced | **AGREE**, with provenance explained below. |
| 29–30 | 16 fixed-traffic scenarios per arm | **AGREE**, WP17/PV arm rows. |
| 39–40 | 1.714/1.715 new-request decision frames; 445/104 changes | **AGREE**, WP17:6–8,20–22; WPJ `LOCKS/C-30.counts`. The count is at least one new request *considered*, not requests accepted or a count of arriving requests. |
| 40;57–59 | 25,96 / 18,95 / 10,08 / 6,06% | **AGREE**: 445/1.714 = 25,962660%; 325/1.715 = 18,950437%; 173/1.716 = 10,081585%; 104/1.715 = 6,064140%. Separate state populations. |
| 44 | Conditional cost reduction 7,79 / 8,00% | **AGREE**, WPJ details: 7,790232 / 8,003756%. Denominators 445/104 differing frames, including cost ties. |
| 45 | Mean reduction over all new-request frames 2,02 / 0,49% | **AGREE**: 7,790232×445/1.714 = 2,022551%; 8,003756×104/1.715 = 0,485359%. |
| 46 | Ratio of summed costs 0,3069 / 0,0794% | **AGREE**: 114.720.189 / 37.380.402.107 ×100 = 0,306899%; 28.288.261 / 35.606.312.123 ×100 = 0,079447%. Denominator is summed selected plan cost over all 12.663/12.325 acknowledged frames, not actual operating cost. |
| 50–51 | Extra fleet-summed drop movement median 90,8/12,5 s, max 390,8/35,5 s | **AGREE**, WPJ details. Standard medians 90,819 / 12,4935 s; max 390,812 / 35,54 s. PV's upper median is 12,494 s; both round to 12,5. |
| 62 | C-30 largest case 35,5 s across two riders, 17,77 s each | **AGREE**, CASE `per_rider.delta` = 17.770 ms twice; sum 35.540 ms. It is not 35,5 s per rider. |
| 65–69 | 34-scenario cost-first trajectory study not run | **AGREE as the supplied experiment status**, OUT §7.2 fallback and REG L's missing result rows. Code/worktrees can exist without a completed audited study; do not inherit H12's older “not implemented/not approved” status. Chapter 5's actual ordering is **CANNOT CHECK** because its new draft was not supplied. |

**Writer's doubt (a): resolve it without weakening a supported result.**

WPCHK:12–15,84–107 only tests necessary conditions, exactly as the writer noticed. **That script alone does not establish exact reproduction of the full stability order.** However, Q4:14–19,60–86,133–138 really re-solves all recorded objective levels and compares selected candidate IDs. PVS:8–29 re-executes that audited implementation; PV/PVJ record matches 12.663 + 12.525 + 12.364 + 12.325 + 12.960 = **62.837**. Q4 handles maximum levels by threshold filtering, then lexicographic sum levels. Thus the v7 sentence is supported by PV/Q4, not by WPCHK's weaker test. It is not a second independent full-order selector implementation. PVS's independent exhaustive enumeration covers the special C-30 case, not all 62.837 frames.

“Bỏ tiêu chí 3” is **AGREE** relative to Chapter 3's grouped criterion: Q4:141 retains forced-count if present, accepted-count, operational-cost and candidate-ID ranking; it drops worst-hard-utilization and all `revision:*` levels. It keeps the eligibility gates. The fixed old runner need not actually have a forced-count level. It is not a switch to unconstrained RollingCost/FREE.

A clearer, optional replacement for lines 22–25 is:

> Ở mỗi lượt quyết định đã ghi, phép sàng lọc chọn lại trên cùng tập phương án đủ điều kiện, bỏ mức dùng trần và các mức phần dời của tiêu chí 3, còn giữ các tiêu chí nhận yêu cầu, chi phí và phá hòa. Trạng thái không được chạy tiếp từ lựa chọn mới. Phép giải lại theo đầy đủ thứ tự gốc tái lập đúng 62.837 tập phương án đã chọn, bằng mã đã được kiểm lại; đây không phải hai bản cài đặt độc lập.

Retain H03/PV and add the Q4:133–138 provenance to N4B-01/02. No mandatory change to the verified screen counts is required.

### 3.2 Section 4.7 — forecast table, prose and inference

Every percentage in `bang:c4-dubao` is an **unweighted scenario mean**. None is the pooled fraction of all 1.471 served riders.

| Table row | Scenarios / served | No forecast / equal-cost pad / forecast, % | Verdict |
| --- | --- | --- | --- |
| All active weekdays | 21 / 1.471 | 6,01 / 1,94 / 0,17 | **AGREE**, full-precision FAT means 6,013604 / 1,943985 / 0,169344%. |
| 7-hour window | 8 / 444 | 14,44 / 4,24 / 0,27 | **AGREE**, FAT means 14,436144 / 4,239103 / 0,265957%. |
| 8-hour window | 8 / 609 | 1,35 / 0,86 / 0,18 | **AGREE**, FAT means 1,349567 / 0,863856 / 0,178571%. |
| 17-hour window | 5 / 418 | 0 / 0 / 0 | **AGREE**, all three counts/rates are zero in these five scenarios. |
| Early >60 s, all active weekdays | 21 / 1.471 | 0 / **0** / 0,08 | No-forecast/forecast **AGREE**; printed pad “chưa đo” **WRONG**. See required change 2. |

FAT stores rates at full precision, with `served` in every row. Multiplying each saved rate by its row's served count reproduces integer counts (not inversion of a rounded printed percentage). These are the counts supporting the table; early-pad and early-naive are zero throughout:

| Scenario (prefix `d201811`) | Served | Late60 naive | Late60 pad | Late60 forecast | Early60 forecast |
| --- | ---: | ---: | ---: | ---: | ---: |
| 14-s10-r3-w07 | 47 | 8 | 4 | 1 | 0 |
| 14-s10-r4-w07 | 53 | 6 | 1 | 0 | 0 |
| 15-s10-r1-w07 | 44 | 10 | 4 | 0 | 0 |
| 15-s10-r2-w07 | 58 | 12 | 4 | 0 | 0 |
| 15-s10-r4-w07 | 45 | 10 | 2 | 0 | 0 |
| 16-s10-r1-w07 | 67 | 3 | 0 | 0 | 0 |
| 16-s10-r2-w07 | 62 | 6 | 1 | 0 | 1 |
| 16-s10-r4-w07 | 68 | 5 | 1 | 0 | 0 |
| 14-s10-r3-w08 | 73 | 2 | 1 | 0 | 0 |
| 14-s10-r4-w08 | 87 | 0 | 0 | 0 | 0 |
| 15-s10-r1-w08 | 70 | 1 | 1 | 0 | 0 |
| 15-s10-r2-w08 | 80 | 1 | 0 | 0 | 0 |
| 15-s10-r4-w08 | 79 | 1 | 0 | 0 | 0 |
| 16-s10-r1-w08 | 81 | 1 | 1 | 0 | 0 |
| 16-s10-r2-w08 | 70 | 1 | 1 | 1 | 0 |
| 16-s10-r4-w08 | 69 | 1 | 1 | 0 | 0 |
| 14-s10-r3-w17 | 90 | 0 | 0 | 0 | 0 |
| 14-s10-r4-w17 | 89 | 0 | 0 | 0 | 0 |
| 16-s10-r1-w17 | 87 | 0 | 0 | 0 | 0 |
| 16-s10-r2-w17 | 82 | 0 | 0 | 0 | 0 |
| 16-s10-r4-w17 | 70 | 0 | 0 | 0 | 0 |
| **Pooled totals (not scenario means)** | **1.471** | **68** | **22** | **2** | **1** |

Thus the prose's **68 → 2 on 1.471** is AGREE, REG F17/RP1 and FAT. Window counts are 60/17/1 late riders on 444 at w07, 8/5/1 on 609 at w08, 0/0/0 on 418 at w17. These should accompany, rather than replace, their scenario-mean percentages if supplied in the evidence appendix.

| Draft lines | Number / meaning | Verdict / source |
| --- | --- | --- |
| 79–82 | Equal-cost padding is proportional to remaining time; fixed coefficient by window | **AGREE**, FFA:15–17,139–141. `k_w` = summed forecast extension / summed original remaining horizon on C-30's active weekday riders; coefficients 0,0336953615 / 0,0098641664 / 0,0001443233. Total added time matches by window; not identical rider-level quotes. This is a different pad from the fixed +30 s of §4.8. |
| 117–123 | 95% intervals; 8 day-window clusters; −10,54 to −1,15 pp; −1,77 pp and −3,62 to +0,07 pp | **AGREE**, fresh replication of FFA:168–190 on FAT. There are 3 window strata and df = 8−3 = 5. Exact dY −5,844260 pp, CI [−10,542053; −1,146466]; exact dPad −1,774640 pp, CI [−3,619793; +0,070512]. The code uses t critical value 2,571. Neither interval is independent unseen-day validation; window overlaps/day dependence remain limitations. |
| 122–123 | Three mornings, 12/11 a source for every main forecast | **AGREE**, active days 14/15/16; FR:94–99 and the source rule. The draft wisely does not assert an unverified holiday status. |
| 125–129 | M⁺-30 and V-30 also 0,17%; U 9,72% → 3,90%; U w17 6,76% unchanged; C w17 0 | **AGREE**, FAT means/FA:3,6,13,23. Fresh active U means 9,715645% → 3,898539%, pooled 129→63 on **1.512**; M⁺ 66→2 on **1.471**; V 66→2 on **1.470**. These arms do not all share C's served denominator. |
| 131–134 | 13,7 s drop extension; w07 27,8 s; 3,2 s pickup extension | **AGREE**, FAT unweighted means 13,698667 / 27,753429 / 3,181681 s. |
| 133–134 | 7,37 s over 2.338 served riders /34 scenarios, weekend extension 0 | **AGREE**, CXJ riders and ADD1/ADD3 N4B-10. Exact mean 7,367123 s. This differs from both the 13,7 s scenario mean and approximately 11,709269 s pooled over the 1.471 active riders. |
| 137–140 | True-factor stretching within 2 s for 2.305/2.305 riders with zero dispatch component, across 34 scenarios | **AGREE**, FA:28/RX:8/FAT oracle columns. It is oracle evidence in this near-deterministic simulator, not forecast deployment performance or an arrival guarantee. |

The accounting language at 142–145 is appropriately model-relative; it does not claim causal blame or an unforeseeable residual. Its exact figure audit follows.

### 3.3 Figure `hinh:c4-so` — all numerical labels and coordinates

Fresh FAT sums and the snow transcript replay give:

| Cohort | Selected riders / scenarios | Total late seconds | Dispatch q | Historical extension f | Signed residual | Shares % |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Active weekday C-30 | 68 /21 | 6.217,406000 | 81,742000 | 5.352,646483 | 783,017517 | 1,314728 /86,091313 /12,593958 |
| Snow C-30 | 41 /8 | 3.445,933000 | 8,566000 | 251,496483 | 3.185,870517 | 0,248583 /7,298357 /92,453060 |

**AGREE** for the figure's printed weekday **82 /5.353 /783 s**, **1,3 /86,1 /12,6%**, and total **6.217 s**; and snow **8,6 /251,5 /3.185,9 /3.445,9 s**, **7,3 /92,5%**. These are independently rounded values, so their printed sum need not equal the independently rounded total. Both cohorts use **A−p0>60 s with nonforecast p0**, exactly as Chapter 3 v3 states; they are not the 2 and 34 riders still late after the historical display.

The 11 cm bar's exact boundaries from unrounded numbers are weekday **0,144620 /9,614665 cm** and snow approximately **0,027344 /0,830163 cm**. The drawn weekday **0,1445 /9,6145** and snow **0,0273 /0,8302** use rounded inputs and differ by less than 0,0002 cm. **AGREE as harmless drawing precision.** Label-placement coordinates, rectangle heights, x/y units and color values are layout parameters, not measurements.

**WRONG as exact arithmetic in the EV comment and REG F09:** `81,7 + 5.352,6 + 783,0 = 6.217,4` at line 182. The left side is **6.217,3**, because the terms were rounded separately. Correct that comment/registered equality, without changing the independently correct body labels. Exact replacement:

~~~tex
% EV (ngày thường): F09; FAT (C-30, 21 kịch bản): 81,742 + 5.352,646483 + 783,017517 = 6.217,406 s; nhãn trên hình làm tròn độc lập; RX:3 (1,3 / 86,1 / 12,6%).
~~~

Keep the historical ledger figure. The clipping correction in required change 3 concerns the later **prefix** analysis, not these bars. Rendered width, label collisions and float placement are **CANNOT CHECK** under the no-build instruction.

### 3.4 Dispatcher forecasting — writer's doubt (b), scenario matching and every number

**AGREE:** the 47,6% and 62,8% are on the **same 15 scenario IDs**, selected by completion of **Mplus-30F**. FBS:119–120 builds each pair from the same cell; 151–158 restricts the deadline analysis to its completed cells. RXS:22–29 takes both means from that same map. Independent BI `chainM_forced` contains the unrounded means **0,476158925508 /0,627703208748**. It is not 47,6% on 15 compared with the main 41,3% on 34, nor a comparison on all 16 original cells.

The one excluded deadline scenario is **d20181116-s10-r1-w08**. C additionally excludes **d20181114-s10-r3-w08**, so its completed population is **14**, not 15. C's zero recovery cannot be asserted for its two stopped runs. The draft's “ở các lần chạy xong” is correct; make the 14/15 counts visible as proposed above.

| Item | Checked value | Verdict / anchor |
| --- | --- | --- |
| Original design | 16 scenarios ×2 arms =32 runs, windows 7/8 | **AGREE**, FBS:41–43 and FR:117. |
| Completed/failed | 29 completed, 3 stopped; C 14/16, M⁺ 15/16 | **AGREE**, BI `failed`, FB completion rows. |
| Failures | C/M⁺ at 16-r1-w08: 1,67 s each; C at 14-r3-w08: 2,69 s | **AGREE**, RX:13–15/FR:120–121. These are FleetPy plan feasibility checks of predicted stop arrival versus latest pickup, not proof that a stopped trip actually completed a late pickup. Prefer “FleetPy tính xe tới ...” if editing the sentence. |
| C completed recovery | 0/7.839 decisions in 14 runs | **AGREE**, BIC integer columns `ack`, `nonNormal`. |
| M⁺ completed recovery | Mean 47,615893% vs62,770321%; pooled 3.849/8.496 vs5.121/8.468 | **AGREE**, BI and fresh BIC sums on the 15 matched cells. The two runs in a pair can have different decision totals and served riders. |
| M⁺ w07 own breach | Mean 39,047710% →10,992246% on 8 scenarios | **AGREE**, BI `Mplus_w07`. Each is relative to that run's own first core promise +30 s; served cohorts differ. |
| M⁺ w08 own breach (not printed in v7) | 8,357825% →3,670633% on 7 scenarios | ADD3 N4B-07's **8,3% is WRONG at one decimal** against independent full precision: correct **8,4%**. RX derives means from per-cell values already rounded to three decimals, which yielded 8,3; BI provides the more precise result. V7 does not print this figure, so no v7 body cell changes for it. |
| Deployment scope | v1.3, K=2; recommends promise replay over this dispatcher transformation | **AGREE**, FR:117/141–146; `run_forecast.py`:9,65–72; X3-29. The pickup conflict in §4.11 still prevents claiming the replay layer is production-ready. |

The wording “Cách triển khai được chọn” should be read as the experimental choice, not a completed operational deployment. The scope caveat at 191–192 is valuable and should remain.

### 3.5 ML — every printed number, controls and scope

| Draft value/claim | Verdict / verified detail |
| --- | --- |
| 3 fixed models, quantile 90 | **AGREE**, MLS:63–69; MLR model definitions. The ablation removes two features, not just onboard count. |
| Mean/p90/early guards 1 s /15 s /1 percentage point; four conditions | **AGREE**, MLS:91–95, MLR:45–47. p90 uses nearest rank in MLR:37–42. These are design criteria, not industry thresholds. |
| “same mean 30 s” on test days | **WRONG**, target set on calibration; required change 1. On static FREE the uniform extension is30, but measured-traffic control test means are37,219/31,772. |
| No model satisfies all four at E=30 | **AGREE** for saved pilot/cohorts: evaluating every E=30/all-window MLT model against the corresponding uniform/fc+uniform controls yields zero qualifying comparisons. Not a claim about all model families or unseen data. |
| C-30 with forecast: no extra late60 reduction | **AGREE**, ML:14–15/45–47; 147 riders on 15/11,197 on 16/11; control/model late60 all0 at E=30. |
| U gain0,69 pp on 15/11,145 riders | **AGREE**, MLT Y60 1,379%→0,690% (printed ML 1,38→0,69); extension37,219→41,624 s, p90 76,409→98,192 s. Both mean/p90 guards fail. |
| U gain0 on 16/11 | **AGREE**, n=200, control/model Y60 0,50%. Mean extension31,772→35,565 s; p90 64,156→85,835 s; early60 0,5→2,5%. Add the missing n. |
| Static FREE 12,89→11,65%,807 riders | **AGREE**, MLT values12,887→11,648%; at E=30/13/11, pooled by rider over both fixed-traffic windows. |
| Static FREE early7,1% vs0% uniform | **AGREE**, MLT7,063% vs0%; p90 62,536 vs30 s also fails the guard. The corrected A1 result is used; do not restore the obsolete6,9%. |
| “ablation changes no result” | **WRONG**, required change 1 gives direct counterexamples. The scoped equality of the reported U/FREE lateness gains is supported. |

I do not fabricate raw model-count numerators by inverting MLT's rounded rates. The counts of test riders are present; exact prediction-count support would need the matching saved A1 per-rider predictions, which I did not locate/use. The older Codex round11 quote file predates the A1 static calibration purge and is not an adequate substitute. This is an evidence-reporting limit, not permission to retrain models during this round.

### 3.6 Section 4.8 — all cells of both tables

All six rows below were freshly recomputed from **CXJ `runs[].riders`**, using `arrival`, `forecast_quote`, `P0`, and the constant added pad. They agree with ADD1/ADDJ and N4B-09. Late thresholds are strict `>T`; early60 is `<−60 s`; within60 is `abs(error)≤60 s`. Counts concern each arm's served cohort; timely/within successes use the common **3.672 input requests** denominator when turned into a rate. Extension is pooled over that row's served riders, including inactive weekends.

| Row | Served | Late60 | Timely60 | Timely120 | Mean added seconds |
| --- | ---: | ---: | ---: | ---: | ---: |
| U +forecast | 2.434 | 137 | 2.297 | 2.347 | 7,183331 →7,18 |
| C-30 +forecast | 2.338 | 10 | 2.328 | 2.338 | 7,367123 →7,37 |
| C-120 +forecast | 2.387 | 65 | 2.322 | 2.379 | 7,273885 →7,27 |
| U +forecast +30 s | 2.434 | 106 | 2.328 | 2.366 | 37,183331 →37,18 |
| C-30 +forecast +30 s | 2.338 | 2 | 2.336 | 2.338 | 37,367123 →37,37 |
| U +forecast +60 s | 2.434 | 87 | 2.347 | 2.386 | 67,183331 →67,18 |

**AGREE for every cell** of `bang:c4-dem` (245–256), including the rounded37,2/7,4 in its opening prose.

| Row | Early60 | Within±60 s | Late120 | Late300 | Late600 |
| --- | ---: | ---: | ---: | ---: | ---: |
| U +forecast | 8 | 2.289 | 87 | 17 | 2 |
| C-30 +forecast | 4 | 2.324 | 0 | 0 | 0 |
| C-120 +forecast | 2 | 2.320 | 8 | 0 | 0 |
| U +forecast +30 s | 44 | 2.284 | 68 | 11 | 1 |
| C-30 +forecast +30 s | 44 | 2.292 | 0 | 0 | 0 |
| U +forecast +60 s | 1.033 | 1.314 | 48 | 8 | 1 |

**AGREE for every cell** of `bang:c4-haiphia` (293–298). Within60 = served−late60−early60 also agrees with the direct absolute-error count in all six rows. Serving more people can increase timely count while leaving a worse tail among those served; the two tables correctly show both quantities.

| Prose numbers / lines | Verdict / arithmetic and cohort |
| --- | --- |
| 218–220;262–264 | **AGREE**: padded U timely60 2.434−106=2.328, tying C-30; timely1202.434−68=2.366 vs2.338. |
| 223–227 | **AGREE**: U replay preserves dispatch/cohort/arrival; U/C-30 common2.207 (U-only227, C-only131). It is not a matched common-cohort intervention. |
| 266–270 | **AGREE**: similar mean *extension*, not identical horizons/quotes; no-pad timely60 advantage31, timely120 disadvantage9; when both add30, advantage8/disadvantage28. 37,183331/7,367123=**5,047198**. “Lời hứa dài thêm ... năm lần” refers to extension, not entire trip duration. |
| 272–275 | **AGREE**: early4/2.338 vs44/2.434; within2.324 vs2.284 (difference40). |
| 304–306 | **AGREE**: +60 padded U early1.033/2.434 and within1.314/3.672. |
| 308–311 | **AGREE**: late12068/2.434 vs0/2.338; late6001/2.434; timely120lead28 = extra96 served − extra68 late. Not28 riders “saved” on a common cohort. |
| 313–316 | **AGREE**: unchanged U174 exposed riders/max590,133→590,1 s; C max29,239→29,2 s. Weekend max29,239 and snow max25,187 s,0 overshoots, support the bound outside active forecasting (ADD N-26/N-28; SNOW1:10). F13's8,6 late-cohort dispatch seconds alone would not prove that bound. |
| 318–321 | **AGREE numbers**, but original-obligation/display scope must be clarified; required change 5. |
| 323–326 | **AGREE**: C-120 timely1202.379 beats +30 padded U2.366 by13; extension ratio7,273885/37,183331=**0,195622**; served deficit2.434−2.387=**47**. It has a different served set and is not an optimum or a domination result across all measures. |
| 328–333 | **AGREE as conditional reading of measured points**: relative to C-30, U serves96 more and has242 more shared completions (555−313). Both pads/caps can be combined. Operator preferences/value are unmeasured. Avoid extending this choice statement to every cap or every padding level. |

**Writer's doubt (c):** the v7 padding argument is substantively correct and satisfies the honest answer in RD §8. Keep its explicit U-journey replay caveat, nearly-equal mean-extension wording, two-sided counts, served-tail counts, and C-120 point. Do not claim padding changes U's ledger, that U is an upper bound, that every metric favors C, or that the96/242 trade-off has established business value.

### 3.7 Section 4.9 — snow numbers and information limits

| Draft item | Verdict / source |
| --- | --- |
| 339–342:601 served,41→34 late60,6,82→5,66% pooled | **AGREE**:41/601×100=6,821963%;34/601×100=5,657238%. The 601 are served riders, not all input requests. |
| 340–341:7,19→5,94% scenario means | **AGREE**, BI snow7,188012/5,937271%; RP1:7–8. Eight scenarios in a single event. |
| 344–347:8 scenarios, w14/w15, date15/11/2018;3.445,9 total,8,6 dispatch,251,5 historical seconds | **AGREE**, snow raw replay/BI/SNOW1; same 41 naive-late riders as the lower figure bar. “Runner not rechecked” honestly marks an identity/equivalence gap. |
| 349–352:geometric blending,19 uses undelivered morning history; post hoc regime gate also19 | **AGREE**, FNS:12–30,126–154; FNS2:6–13,32–40; RPL; RP1 REGB rows. The plain BLEND-pre method does not itself require the regime threshold: the sentence correctly says a separate threshold rule also yields19. |
| 383–386:extra886,9 s/25,7%; remainder2.299,0 s/66,7% | **AGREE as clipped analysis**, **WRONG as an unqualified use of the signed Ch3 ledger**; required change 3. |
| 384–386:09/2018–12/2019,5 snow spells≥25,4 mm including this event | **AGREE for the registered weather screen**, NEW:9/WX17:4–5. It groups qualifying days separated by at most2 days, using the Central Park weather proxy. The five groups are15/11/2018;12/02/2019;20/02/2019;01–04/03/2019;02/12/2019. This is not evidence of five independent congestion shocks or all conceivable disruptive events. |

Every cell of `bang:c4-tuyet`:

| Method | Pooled late60 /601 | Scenario-mean extension s | Verdict |
| --- | ---: | ---: | --- |
| No forecast | 41 | 0 | **AGREE** |
| Historical | 34 | 1,975469→2,0 | **AGREE** |
| In-window blend | 21 | 8,480617→8,5 | **AGREE** |
| Blend with morning prefix | 19 | 9,498492→9,5 | **AGREE** |
| One-bin-lag trend, exact current anchor | 29 | 8,991093→9,0 | **AGREE** |
| Same-event equal-cost pad (in-window blend target) | 27 | 8,3 | **AGREE**, RP1:19; RPL:12–13,78–88,96–106. Same pooled quote-extension budget need not produce the same unweighted mean as the blend's8,5 s. |
| True factors | 0 | 18,767955→18,8 | **AGREE**, oracle; future information is unavailable at promise time. |

The fifth row is a sensitivity check of the trend, **not a realistic latency experiment for the entire feed**, since it retains an exact current anchor. The 27-rider pad coefficient is set from promises on the very snow population; it is not an independently calibrated event-day control. Both caveats are already visible in the table. The all-zero snow early rates for these selected methods are supported by RP1 but are not a guarantee for other variants.

### 3.8 Sections 4.10–4.11 — every diagnostic and limitation number

| Draft lines / item | Verdict / anchor |
| --- | --- |
| 392–395:34 scenarios; cap30/120; max29,2/118,9 s;0/20.101 and0/20.435 recovery | **AGREE**, CXJ totals/ADD1:120–121. Maxima29,239 and118,938 s;0 observed overshoots. U also0/20.760, so these zeros are not a measured advantage over U. |
| 397–402:four arms;100 candidates per vehicle;2 new requests per batch; one omitted request per arm | **AGREE counts/units**, ADD1:119–122; GEN54–95. No zero impact on outcomes follows from these counters; required change 4. |
| 404–407:criterion3 worst utilization100%;3.503/3.506/3.504 recorded levels | **AGREE**, ADDJ `objective`/ADD1:119–121; HVA:612–626 zero-cap convention. Denominators are decisions with that objective recorded, not all acknowledged decisions. The zero vehicle/pickup-stop/drop-stop caps contribute the saturation; later revision objectives still rank choices. |
| 409–411:policy files byte-identical between main/fixed sets; runner settings differ | **AGREE**, NEW:11/13; recovery, late-boarding mode, policyVersion, constant-level skipping and solver evidence differ. Same policy file does not imply same executed experiment. Not a new hash computation this round. |
| 413–418:7.159 matched riders,382.006 revision records,1.024/1.025 tests and separate remaining pass | **AGREE**,7.159=2.434+2.338+2.387; ADD1:66–78 checked t0/P0/A/absolute dispatch/change count/D0.382.006 is the earlier185-run revision-field audit, not a claim about every field of these later102 U/C30/C120 runs. Tests are supported by logs, not executed here. |
| 428–432:96 fewer served,242 fewer shared,30-s bound; four lateness thresholds; C-120 intermediate point | **AGREE within the main panel**, CXJ/ADD N-20/N-24 and R25. The four thresholds are60/120/300/600 s against the first nonforecast promise; raw late counts203/102/18/2 vs76/11/0/0. They concern different served cohorts. No business value is asserted. |
| 434–439:127 fewer late,96 fewer served, k>0,756m | **AGREE as hypothetical arithmetic**:−96m+127k>0 iff k>(96/127)m=0,755905512m. This is not a measured financial result, common-rider effect or recommendation. Keep the no-real-k/m and different-cohort caveats. Higher-load sentence is explicitly an untested hypothesis, not evidence. |
| 445–450:one simulator;15-minute common factor;00:00 anchor; dwell0 s in3 sampled runs;30 s/passenger in FleetPy paper;96-node closure | **AGREE at stated scope**, REG B01/B03/B05–B07; `service-duration-check-2026-10-06.txt`:2–4; extracted `fleetpy-etrr-2026.txt`:423–424. Dwell verification is sampled, not an audit of every run; the wording correctly says so. |
| 451–452:no rider-response model, no incumbent vehicle reassignment | **AGREE**, REG I07; X3-39 structural retention. Service counts do not model abandonment. |
| 458–461:34 dependent scenarios,5 days, one run each; threshold/split/120 selected after preview; exploratory | **AGREE**, REG B09/B11/I05/I06. This limitation also applies to ML's previewed test days, which must be mentioned locally; a day split alone does not remove that caveat. |
| 462–464:0,535 riders including idle vs≈1,33;180 vehicles/21.400 requests; median165 vs196 s | **AGREE**, saved LOAD:2 and SEL6:2–4; FleetPy primary extracted text:433–449,474–478. These are different systems/setup/averaging contexts, not a controlled load effect or a scaling result. The short-trip medians pool the49 constructed fixtures, not just34 test cells. |
| 470–471:34/1.471 displayed pickups beyond latest pickup | **AGREE**, FAT `pick_after_window` sum/RX:2/F07. It is a conflict in the first displayed pickup quote, not34 observed late-boardings or34 predicted lost riders. |
| 472–473:rebuilt runner needs equivalence; snow runner not rechecked | **AGREE as limitations/process requirement**, REG A28/I13, X3-10. A successful unit-test rerun alone does not prove binary equivalence with the archive. |
| 479–481:cost-first/per-step arms not run; effects not separated | **AGREE**, OUT fallback/REG E09/H02. The empirical rarity of cumulative-only records elsewhere does not establish counterfactual trajectory equality. |
| 482–486:30–60 vs900 s; relaxed deadline unrun;30 not a perception/industry threshold | Default900 and the caveats **AGREE**, primary Schulz/Pfeiffer extracted text:1203–1206; whole-thesis30–60 scope **WRONG**, required change 7. |

## 4. Audit of all fourteen N4B additions

| Row | Verdict | What to retain/correct |
| --- | --- | --- |
| N4B-01 | **AGREE for its stated weaker check and cost-first method; incomplete provenance for exact replay** | WPCHK's independent full-vector comparison is necessary only. Add Q4:133–138/PVS:8–29 as the actual full-order re-solve supporting H03. Grouped criterion3 is indeed what is removed. |
| N4B-02 | **AGREE** |12.960+12.663+12.525+12.364+12.325=62.837 acknowledged portfolio frames; five arms×16 scenarios. Include FREE in the scope of the total even though the main screen table shows U/C30 only. |
| N4B-03 | **WRONG in the last clause only** | Formula, k values, late means, and0→0,08 early means agree. `E_pad` was calculated and saved: correct missing-pad claim to0% over21 C30 scenarios, pooled0/1.471. |
| N4B-04 | **AGREE from saved FA/FR outputs** |Bootstrap interval[−2,83;−0,68], per-morning−13,1/−21,9/−7,2 and leave-one-day−6,25/−3,54/−8,21 match; not used by v7. This round did not rerun bootstrap draws. |
| N4B-05 | **AGREE** |Snow historical sums 3.445,933=8,566+251,496483+3.185,870517; overshoot0 explains equality of clipped/signed convention **for HIST**. Do not extend that equality to BLEND-pre. |
| N4B-06 | **AGREE for seven table methods/counts/extensions** |Keep retrospective/prefix/lag/current-anchor/same-event-padding caveats. Add the clipped definition when citing the later prefix ledger result. |
| N4B-07 | **AGREE with one numeric correction and clearer scope** |Same 15 deadline scenarios confirmed; C zero only14 completed;29/32 and failure details match. Independent full-precision w08 own-break8,357825% rounds to**8,4%, not8,3%**. Add K=2 from run_forecast.py:65–72. V7 does not print the faulty8,3. |
| N4B-08 | **AGREE for underlying split/model/metric facts; qualify use in body** |Fixed12–13 profile and preview caveats are material. Target E=30 is calibrated, not an exact test mean. Two-state-feature removal does not imply identical metrics. Use corrected A1 static calibration data; avoid obsolete6,9%. |
| N4B-09 | **AGREE** |Every listed early/within/tail count matches fresh CXJ arithmetic, including +60 padded U. |
| N4B-10 | **AGREE** |Extension sums divided by 2.434/2.338/2.387;13 inactive weekend scenarios contribute0. Distinguish21-scenario means and ML's separate profile/calibrated controls. |
| N4B-11 | **AGREE for the named counters, not all-limit impact** |New-request omissions are deferred pending requests; candidate/work counters have the stated meanings. Unchecked repair counter and insertion-only search prevent a blanket completeness/causal conclusion. |
| N4B-12 | **AGREE as a read of saved Codex byte comparison** |Four policy files match; runner configurations differ. No independent current sha calculation was performed here. |
| N4B-13 | **AGREE** |10+138+191+108+82+14+201+133+147=1.024 pass; total1.025; separate remaining test1/1 pass. Dirty retry log alone omits filter name; TR identifies it. Do not describe one all-green full-suite execution. |
| N4B-14 | **AGREE** |7.159 matched served riders; zero mismatches in t0, P0, A, S, k; D0 difference0 in saved comparison. “Independent” comes from Codex's separately written readers, not the additional same-reader Claude TSV replay. |

**Registrar corrections required before integration:** N4B-03 (available early-pad result); N4B-07 (8,4% w08 precision, completed subsets, K=2); N4B-01/02 (strong replay provenance); F09 (rounded equality); F15/N4B-06 (clipped convention). Extend N4B-08's body guidance to explicitly distinguish calibration target and test mean. REG A24's older “2 requests per vehicle” should follow X3-32's corrected batch-wide rule; Part B itself already uses the right unit. K34's all-computation causal shorthand should be narrowed as in required change 4. Do not copy older REG H12 approval/implementation status into the fallback.

## 5. Strict examiner assessment and cross-chapter consistency

- **No forbidden plan/preregistration/prediction language was found in the v7 thesis body or its EV comments.** Internal labels in source reports are evidence metadata, not material to import. The draft avoids optimum/uniqueness/firstness, business satisfaction/revenue claims, and claims that a forecast residual is intrinsically unforeseeable.
- **Zero recovery is not offered as an advantage over U in v7's operator trade-off paragraph.** The v4 error is corrected. U also has0/20.760. Preserve that distinction when shortening the text. The C/M⁺ contrast measures different obligations; required change 5 prevents the forecast-display ambiguity.
- **Ledger causality:** the signed identities are accounting in the given model. The figure's “phần tính cho điều phối” and “hồ sơ lịch sử giải thích” are acceptable. §4.9 must disclose clipping so it does not silently change Chapter 3's definition. No claim that traffic alone physically caused all residual delay is justified.
- **Guarantees:** no new unconditional arrival-time guarantee is needed. C bounds the dispatch ledger under its enforcement assumptions; it does not bound real arrival lateness or guarantee physical feasibility. §4.10 correctly distinguishes archive fidelity from real-world validity; only the computational-impact paragraph overstates its evidence.
- **Different cohorts:** §4.8 correctly identifies2.207 common U/C30 riders, and all padding/tail/accuracy cells use their own served populations. The C120 point is correctly called a further measured point. Forecast-inside-dispatcher own-break comparisons likewise use each run's own promises and cohorts, even though the scenario IDs are paired.
- **Section 4.11 caveats retained:** single simulator/common factor/00:00 anchor, zero sampled dwell,96-node closure, no reaction/reassignment,5 dependent days, preview, low occupancy/short trips, pickup-display conflict, archive equivalence, snow identity, cost-first/per-step/unrun-relaxed-deadline limits, and no established value of B. Add local ML vintage/preview qualification and narrow the deadline-level range; no additional business claims should be inserted.

Cross-checks against **Chapter 3 v3 and supplied Part A v1**:

| Item | Status |
| --- | --- |
| p0 vsD0, q signed vsabsolute C budget | Part B's main figure agrees with Ch3 `eq:so`/late-cohort definition; prefix clipped analysis needs required change 3. |
| Criterion3 grouping and saturation | Consistent with Ch3 table/text and X3-07; cost-first screen drops the whole stability group, not its hard gates.3.503/3.506/3.504 objective denominators match ADD1. |
| Main served/forecast/extension rows repeated in Part A `bang:c4-tran120` | All three rows match:U 2.434/2.297/2.347/7,18; C-30 2.338/2.328/2.338/7,37; C-120 2.387/2.322/2.379/7,27. These means are pooled over 34 scenarios, not the 21-scenario 13,7. |
| Dispatch maxima/snow bound |29,239/118,938 main;25,187 snow; weekend29,239/116,542. Consistent with Part A and ADD corrected§0.4. |
| Recovery labels | “Lượt quyết định phải phục hồi” refers to acknowledged non-normal certificates; Ch3's “bị ép” is the same measured status. Keep Part A R25's corrected definition, not “all candidates eliminated.” |
| Tests | Part B correct; Ch3 “chưa chạy lại” must be updated. The older R23 instruction to keep the historical-only sentence is superseded by these new logs. |
| Deadline cap range | Part B's generic30–60 formulation conflicts with Ch3's morning levels through300; required change 7. |
| Labels/references |12 unique labels in Part B (6 sections,5 tables,1 figure); no duplicate labels across Ch3/Part A/Part B; every Part B `ref`/`eqref` resolves in those supplied drafts. Final assembled citation keys/layout still require integration verification. |
| Tables/figures numbered twice in NOTES |Use labels, not outline's stale4.11–4.15/H4.3 numbers. Part A has13 tables and1 figure, so these would follow as4.14–4.18 and4.2 before revisions. NOTES header says497 lines but actual v7 has488; correct bookkeeping. |
| Chapter5 future-direction claim |Fallback is authorized and correctly used; whether Ch5 actually puts cost-first first is **CANNOT CHECK** without its rewritten draft. |

The Stage 1b fallback must stay. No unused forecasts, cost-first outcomes, per-step outcomes, or business-valued cap should be invented to fill its slot. No new experiment is required for the wording repairs in this review.

## 6. What remains CANNOT CHECK

Actual pagination, page budget, table/figure collisions, compiled cross-reference/citation resolution, and assembled thesis layout remain unverified because builds/renders are prohibited. NOTES' approximately10,2 versus13,9 pages are estimates, not measured layout; its4.6 page budget1,2 differs from OUT's written fallback budget0,8 and requires coordination when assembling.

I did not freshly recompute every main raw transcript, fit an ML model, rerun tests, recheck the snow runner's binary equivalence, or establish any unseen-day/real-world/business effect. The per-rider/table/cluster arithmetic above is independently calculated from saved full-precision evidence except where explicitly labelled as a source-read check. ML exact model-count numerators remain unavailable from the corrected saved metric table alone. Neither agreeing readers nor the successful dirty-tree retry proves operational validity.

**Top five required changes:** (1) accurate ML calibration target, fixed forecast vintage, preview caveat and ablation scope; (2) equal-cost-pad early result is0%, not missing; (3) disclose clipped snow accounting versus the signed ledger; (4) narrow the computational-limit conclusion to recorded counters; (5) separate the original deadline obligation from the forecast display metric. Also synchronize Ch3's test sentence, narrow30–60 to the main set, and correct the minor register/EV rounding issues specified above.
