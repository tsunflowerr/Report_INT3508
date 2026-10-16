# Round 37 — verification of Chapter 4 part B v10

**Verdict: ACCEPT WITH CORRECTIONS.** All new numbers required by the brief are reproduced. The ML integer recovery is valid for these rows and can remain with explicit derived-count provenance. Do not integrate v10 unchanged: its padding argument overstates the designed bound and the scope of one comparison, several cohort/aggregation labels were shortened away, and the supplied Chapter 3 and Part A still conflict with the corrected evidence. The 11-page ruler budget also remains unmet.

Reviewed 13/10/2026. Physical line numbers refer to the 450-line `drafts/09-chuong4-phanB-v10.tex`. Other versions are named explicitly. No draft, thesis, source-code or register file was changed. All new files were created exclusively in `codex-work/r37-ch4b-verify/`; files from the interrupted attempt were preserved.

## 1. Ranked corrections, with exact Vietnamese replacements

### 1. Repair the padding argument's bound, comparison scope and necessity claim

**v10:217–227 is substantially fair**, but 220–222 incorrectly attaches the observed maximum 29,2 seconds to the construction of a 30-second cap. Also, 269–271 compares extensions as if they were equal full promise lengths, and says padding *must* add approximately five times as much. The data establish the displayed rows and their ratio, not a minimum necessary padding. Finally, 295–299 says padding is “không kém luật C” without identifying C-30, although C-120 has 2.379 timely120 versus padded U's 2.366.

Replace **220–222**, starting with “Nhưng đệm…”, with:

> Nhưng đệm không đổi quyết định điều phối: vẫn có 174 khách bị điều phối dời giờ trả, với tổng độ dời lớn nhất là 590,1 giây (gần 10 phút). Luật C trần 30 giây giới hạn tổng độ dời do điều phối của mỗi khách ở 30 giây dưới giả thiết (N); trên 34 kịch bản của tập kiểm tra chính, mức lớn nhất đo được là 29,2 giây, kể cả ở các kịch bản cuối tuần không có dự báo. Đổi lại, luật C phục vụ ít hơn 96 lượt.

Replace **269–271** with:

> \textbf{Vai trò của từng thành phần.} Thứ nhất, ở mức kéo dài lời hứa gần bằng nhau, luật C trần 30 giây hơn cách đệm ở ngưỡng một phút và kém ở ngưỡng hai phút: khi cùng đệm 30 giây, hai bên có 2.336 so với 2.328 lượt và 2.338 so với 2.366 lượt. Ở hàng đệm 30 giây, điều phối không trần đạt cùng 2.328 lượt không trễ quá một phút như luật C có dự báo không đệm, với lời hứa dài thêm trung bình 37,18 so với 7,37 giây, tức khoảng năm lần.

Replace **295–299**, retaining the existing bold lead-in, with:

> Nếu hãng xe chỉ tính số lượt không trễ quá hai phút và chấp nhận lời hứa dài hơn cùng nhiều khách tới sớm hơn, điều phối không trần có dự báo và đệm 30 giây đạt 2.366 lượt, so với 2.338 lượt của luật C trần 30 giây có dự báo, trên 3.672 yêu cầu; điều phối không trần cũng phục vụ thêm 96 lượt. Nếu cần giới hạn tổng độ dời do điều phối của từng khách, kể cả khi không có dự báo, luật C trần 30 giây làm được điều này dưới giả thiết (N), đổi lại 96 lượt phục vụ và 242 khách đi chung. Hai cách dùng chung được; chọn cách nào là quyết định của hãng xe, không phải kết luận của thực nghiệm.

Keep EV C20/N-23/N-28/A06/A22/K05, N-16/N-17/N-18/N-19/N-20 and the different-cohort caveat at 225–227. Add the saved `verify-numbers-v2.json:padding` anchor. These replacements do not guarantee arrival relative to the first promise.

### 2. Restore visible denominators and the 34-scenario oracle cohort

**124–128:** the EV knows that M⁺-30 has 1.471 served riders and V-30 has 1.470, but the new prose gives both as 66 → 2 without either denominator. The 17-hour comparison similarly loses 437 versus 418. Hidden EV text is not a substitute for the owner's printed denominator requirement.

Replace **124–127** with:

> Lợi ích không riêng của luật C. Trên cùng 21 kịch bản, khi có dự báo, luật hạn chót 30 giây giảm từ 66 xuống 2 khách trễ trong 1.471 khách được phục vụ; luật trần độ dời khách thấy 30 giây cũng giảm từ 66 xuống 2 trong 1.470 khách. Điều phối không trần giảm từ 129 xuống 63 trong 1.512 khách. Riêng khung 17 giờ, 28 khách trễ trong 437 khách của điều phối không trần không đổi, còn luật C có 0 trong 418 khách. Theo sổ, 86,1\% số giây trễ của 68 khách trễ khi không dự báo thuộc phần được hồ sơ lịch sử giải thích (Hình~\ref{hinh:c4-so}); dự báo và trần nhắm vào hai phần khác nhau của sổ.

**135–136:** the 2.305 oracle-fit riders belong to all 34 main scenarios, not the preceding 21-scenario/1.471-rider cohort. Replace only that oracle sentence with:

> Trên cả 34 kịch bản, với luật C, kéo dài lời hứa theo đúng hệ số sẽ xảy ra cho giờ trả khớp trong vòng 2 giây ở cả 2.305 khách không bị điều phối dời.

Keep EV N4B8-02/F09/F10 and the current simulation and pickup-check caveats. Optionally begin 130 with “Trên 21 kịch bản này,” to make the 13,7-second scenario mean equally explicit.

### 3. Identify recovered ML counts as a derivation, and remove English outside parentheses

**206–211:** retain the numbers; the independent integer-compatibility probe confirms them. Insert after “Không mô hình nào thỏa đủ bốn điều kiện.”:

> Các số đếm sau được suy từ tỉ lệ gộp theo khách đã làm tròn đến ba chữ số thập phân trong bảng kết quả; với mẫu số tương ứng, mỗi tỉ lệ chỉ ứng với một số nguyên.

Add `verify-numbers-v2.json:ml` and `ml_pilot_run.py:37–42,175–176` to EV 211. The rounding proof can stay in the evidence notes or appendix; it need not expand the running text further. Do not describe these as a fresh direct count from per-rider model predictions.

At **191–192**, replace:

> Đó là cây quyết định tăng cường theo gradient (gradient boosting)

with:

> Đó là mô hình cây quyết định tăng cường (gradient boosting)

The English term then appears only in its permitted first-use parentheses. Keep the fixed 12–13/11 profile, calibration-target distinction, previewed days, two removed state features and four comparison conditions.

For **N4B8-03/NOTES**, supersede the generic “bound < 1 therefore unique” argument with this exact evidence-note wording:

> Với từng dòng được dùng, phép kiểm xét mọi số nguyên từ 0 đến số khách và chỉ tìm được một số phù hợp với sai số làm tròn 0,0005 điểm phần trăm. Cận sai số của số đếm lớn nhất là 0,004035 khách ở mẫu số 807. Điều kiện cận nhỏ hơn 1, xét riêng, không đủ để kết luận về số nguyên phù hợp.

### 4. Include verified pooled forced-decision counts and restore the 41,3% estimand

**CX-10, 184–188:** the rejection's stated reason was lack of a fresh check. That reason is now resolved: a separately written streaming decoder recounts acknowledged decision hashes and non-normal certificates in all 15 completed M⁺ forecast runs and their same-ID baselines, reproducing both BIC integers. The counts **should enter**, preferably as one compact body sentence; per-run support can go to Appendix C when it exists.

Insert after the current sentence reporting 47,6% versus 62,8%:

> Tính gộp trên cùng 15 kịch bản, đó là 3.849 trong 8.496 lượt quyết định khi đưa dự báo vào, so với 5.121 trong 8.468 lượt khi không đưa vào; các tỉ lệ 47,6\% và 62,8\% ở trên là trung bình theo kịch bản.

EV: `verify-numbers-v2.json:dispatcher.paired.Mplus-30F/Mplus-30`; BIC `ack`, `nonNormal`, matched `cell` values. Do not treat those counts as the numerators of the scenario means.

**286–287:** “41,3% lượt quyết định” lost its visible aggregation label. Replace those lines with:

> Theo nghĩa vụ đó, tính trung bình theo kịch bản, nó bị ép ở 41,3\% lượt quyết định; tính gộp là 7.710 trong 20.103 lượt. Luật hạn chót có khách trễ quá hạn 30 giây ở 28 trong 34 kịch bản, còn luật C không có quyết định bị ép hay khách vượt trần (Bảng~\ref{bang:c4-nghiavu}).

EV: N-21/C13/X3-16. The preceding sentence correctly retains the original nonforecast obligation; keep it.

### 5. Synchronize the assembled chapters and resolve the appendix reference

**Ch3 `r33-ch3v4/07-chuong3-v4-v3.tex:723–724`:** the supplied latest draft says all 1.025 passed in a rerun with LF plus an untracked file. The saved logs instead show a clean 1.024/1.025 execution and a separate 1/1 retry. Part B 381–384 is correct. Replace the Ch3 item with:

> \item \textbf{Kiểm thử phần mềm:} khi chạy lại ngày 12/10/2026 trên đúng mã nguồn đã dựng bộ chạy, với kiểu xuống dòng LF, 1.024 trong 1.025 kiểm thử tự động đạt. Kiểm thử còn lại đòi cây làm việc có tệp chưa được ghi nhận, và đạt khi chạy riêng với một tệp như vậy.

Retain EV N4B-13 and the two log anchors. Do not claim that one full-suite run passed 1.025/1.025.

**The same Ch3:706–707:** replace the sentence beginning “Vì vậy bộ sinh…” with:

> Vì vậy bộ sinh không xét hết mọi phương án; mục~\ref{muc:c4-hople} báo các bộ đếm đã đọc của bộ sinh. Các số này không đo mọi giới hạn của bước sinh, kiểm và giải.

Retain the following sentence about checking ten dimensions and stop-order inversions.

**Part A v4:135–136,142–145,435–438:** snow identity is now established, so its three old caveats contradict Part B 376–379. Change the snow row's runner cell **“Chưa kiểm lại” → “Như tập chính”**. Replace the first two sentences at 141–143 with:

> Bản đã lưu là bản bộ chạy biên dịch và lưu lại, dùng chung cho tập kiểm tra chính, tập buổi sáng, các lần chạy trần 120 giây và chiều tuyết; bản cũ chưa có luật phục hồi (mục~\ref{muc:doichung}, \ref{muc:kiemtra}).

At 435–436 remove only “(bộ chạy chưa kiểm lại)”. Replace the obsolete X3-10 snow qualifiers in these EV lines with N4B8-05 plus `verify-numbers-v2.json:identity`. The fixed-traffic old runner caveat remains necessary.

**Part B:382, `phuluc:C`:** this label is not defined in the prescribed chapter set, the rewrite .tex tree or current thesis content. ASSEMBLY-NOTES already identifies it as a pending appendix. It is an inherited assembly dependency, not a newly broken chapter ref. Until an evidence-backed appendix is actually present, remove the exact substring **“ (Phụ lục~\ref{phuluc:C})”** from this sentence. Restore the reference after its target exists. Apply the same integration discipline to appendix pointers elsewhere; do not invent an appendix definition merely to silence the missing ref.

### 6. Remove the unverifiable assertion about Chapter 5's ordering

**71–73/CX-23:** no rewritten Chapter 5 is present in the checked draft directory. The direction is allowed, but the claim that another chapter already places it first remains unverified. Replace the second sentence with:

> Khóa luận vì vậy chưa tách được phần của trần và phần của bộ chọn; phép thử này là một hướng phát triển còn mở.

This resolves the body claim without fabricating Chapter 5 content. Keep H02/H10/K18/I12.

### 7. Meet the 11-page ruler budget without removing interpretive safeguards

NOTES' 3.483 prose tokens plus 2,55 table/figure pages give about **13,10 pages** under the required 330-token ruler. Reaching 11 with the same graphical allowance requires about **695 prose tokens**, before any additions above. All listed NOTES §4 savings total only **540**, implying about **11,47 pages**, even if every cut were made. The alternative 480–560-token density does not replace the specified ruler. Use the ranked cuts in §7 below; recount after revision. Actual rendered pages remain unverified because builds are prohibited.

Useful exact replacements for safe shortening:

For **408–411**, retain only:

> \item Thời gian dừng đón, trả bằng 0 giây (kiểm trên 3 lần chạy mẫu), so với 30 giây mỗi khách trong nghiên cứu điển hình của FleetPy~\cite{engelhardt2026}, và đồ thị rút gọn chỉ có 96 nút. Phần dời do điều phối và cái giá 96 lượt vì vậy chỉ áp cho thiết lập này.

For **421–423**, after confirming Part A's `muc:c4-thamdo` target, use:

> \item Cách dùng lại tập kiểm tra chính được nêu ở mục~\ref{muc:c4-thamdo}. Chiều tuyết và các ngày kiểm học máy cũng đã được xem, nên các kết quả này là thăm dò.

Do not erase the local shared-source/three-morning CI caveat at 121, the no-reassignment limit at 412–413, or the two-rider explanation of 35,5 seconds at 68–69.

### 8. Record the limits of numerical validation and missing seed sensitivity

The rejected requests L-23/L-26 do not require inventing positive validation or running prohibited experiments. They do justify concise statements of what remains untested.

At the end of the validation discussion, add:

> Phép kiểm số đếm học máy chỉ đối chiếu số học của bảng kết quả; nó không kiểm lại quá trình học hay dự đoán của mô hình.

EV: `verify-numbers-v2.py` section C; `ml_pilot_run.py:37–42,175–176`. Main forecast and padding arithmetic now have independent per-rider cross-checks; do not repeat the stale blanket claim that none of these paths has been checked.

After **419–420**, add:

> Chưa kiểm độ nhạy theo hạt giống của bộ giải, nên chưa biết các chênh lệch có giữ nguyên khi đổi hạt giống.

EV: Ch3 `muc:gioihan` fixed seed 7; B09/B11 and the stated one-run design. This names an absent experiment and its consequence, not a result from one.

### 9. Make the lower clipping bound explicit

**347–348/CX-03 is substantively fixed.** For a precise definition, replace only the second sentence with:

> Phần kéo dài của mỗi khách được chặn trong khoảng từ 0 đến phần trễ còn lại sau khi trừ phần tính cho điều phối.

The 886,9/25,7% and 2.299,0/66,7% values continue to describe that clipped convention, not the signed Ch3 identity. No need to replace them with the signed alternatives.

### 10. Correct the figure's rounding comment

**EV 177:** the full-precision sum is correct, but the comment attaches a 0,1-second rounding discrepancy to whole-second figure labels. The visible labels are 82 + 5.353 + 783 = 6.218 versus the total label 6.217: the gap is 1 second. Replace the final parenthetical clause with:

> các nhãn làm tròn đến giây độc lập, nên tổng ba nhãn là 6.218 s, lệch 1 s so với nhãn tổng 6.217 s

The 0,1-second discrepancy belongs to the separate one-decimal register sum. This is an EV-comment repair; the figure's component evidence remains valid.

## 2. Every R29 correction: FIXED / PARTLY / NOT

These rows use the 24 CX identifiers of CH4B-REVISION-LOG. “FIXED” judges the underlying R29 correction, not verbatim adoption; a separately identified new regression can still remain. The two NOT/CANNOT CHECK rows are evidentiary limits, not failed numerical checks.

| R29 row | Status | v10 lines and judgment |
|---|---|---|
| CX-01 ML calibration, profile, preview, ablation | FIXED | 190–204,206–211: target 30 on calibration, fixed 12–13 profile, viewed days, two removed features, unchanged **late count** only. New English-word issue and count provenance require §1.3. |
| CX-02 pad early count | FIXED | 104–106: 0/0/1 on 1.471; independently reproduced. |
| CX-03 clipped snow split | FIXED | 347–352 distinguishes clipping from `eq:so`; explicit lower bound is minor precision, §1.9. |
| CX-04 computational counters | FIXED in B | 364–368 narrows to checked counters and names uncovered limits. Ch3 remains broader, §1.5. |
| CX-05 original obligation/display | PARTLY | 284–288 separates them correctly but drops visible scenario-mean label for 41,3%, §1.4. |
| CX-06 Ch3 test synchronization | PARTLY | B 381–384 is correct; latest Ch3 723–724 conflates separate executions, §1.5. |
| CX-07 deadline range | FIXED | 444–450: main 30/60, morning 30–300, cited default 900; unrun relaxed deadline caveat retained. |
| CX-08 scenario mean definition | FIXED | 90–92,108: separate pooled block, unweighted scenario mean. |
| CX-09 forecast implementation and completed cohorts | FIXED | 181–188: current and next bin, 3/32 stops, 14/15 completions, baseline same 15 IDs. |
| CX-10 pooled forced counts | NOT in v10; now verified | 184–188 omits them. Reconsider the reviser's rejection; §1.4 gives supported insertion. |
| CX-11 full-order re-solve evidence | FIXED | 25–29 cites actual Q4/PV full-order re-solve, not WPCHK's necessary-condition-only test. |
| CX-12 five-arm/independence scope | FIXED | 27–29: five configurations; EV includes FREE, 62.837 and same code twice, not two independent implementations. |
| CX-13 window counts | FIXED | 100–106: all three windows, served denominators and early counts. |
| CX-14 rounded sum | FIXED underlying arithmetic | EV 177 corrects full-precision sum; its added whole-label rounding note needs §1.10. |
| CX-15 projected failed pickup | FIXED | 183 says FleetPy calculated a future pickup, not an observed failed-run arrival. |
| CX-16 8,3 → 8,4 rounding | FIXED by corrective record | Neither value is printed in B; EV 188 points to corrected evidence. ADD6's “Dòng cũ cần sửa” corrects N4B-07; do not re-import 8,3. |
| CX-17 ML denominators | FIXED | 206–211 includes 145,200,147,197,807. Integer recovery independently established below. |
| CX-18 limit cap/pad choice scope | PARTLY | 295–299 loses C-30/pad30 scope; C-120 counterexample already at 290–292, §1.1. |
| CX-19 four thresholds/different cohorts | FIXED | 390–394 explicitly states different groups. |
| CX-20 local ML preview | FIXED | 195–196 and 421–423 both state viewed test days. |
| CX-21 register repair | FIXED by additive supersession | EV 29,106,177,188,204,352,368 uses N4B8 corrective evidence; ADD6 supersedes old rows. New ML-bound wording and EV rounding correction still needed. |
| CX-22 NOTES bookkeeping | FIXED | Header and NOTES identify v10; actual line count 450, not old 497 claim. |
| CX-23 Chapter 5 ordering | NOT — CANNOT CHECK | 71–73 retains assertion; no rewritten Ch5 found. Remove assertion with §1.6. |
| CX-24 pagination/layout | NOT — CANNOT CHECK | NOTES openly admits unmet ruler budget; no build/render allowed, §1.7. |

The log's 16 A / 5 M / 1 R / 2 CC is a revision-decision inventory, not an independently established count of fully repaired findings. CX-10 was an **optional addition in R29**, not a count that Codex had rejected; R is the reviser's decision to defer it for lack of checking.

## 3. Independent verification of every new number

The root's saved probe is **`verify-numbers-v2.py` → `verify-numbers-v2.txt` and `.json`**, run with `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -I -B`. All assertions passed. It imports no experiment reader or model and launches no simulation/build/test/fit.

Three evidence levels are deliberately distinguished:

- Full-precision Family-A cell shares are inverted per cell with Decimal and checked against integer counts; U/C are also recounted from the previously independent Codex per-rider extraction, with an independently recomputed C proportional-pad coefficient.
- ML counts are mathematical recovery from the saved rounded result table, after checking its actual metric and serialization code; no model is refitted and no individual prediction file is recounted.
- Snow ledger and dispatcher forced counts are freshly read from raw NDJSON by a separately written streaming decoder. Frame hashes, acknowledgements and recorded certificates are checked. Snow forecasting uses a separately written historical-factor integrator over the saved factor CSVs.

### 3.1 Forecast counts

| v10 location / cohort | No forecast / proportional pad / forecast | Denominator | Result |
|---|---|---:|---|
| 100, C-30 all active weekdays | 68 / 22 / 2 | 1.471, 21 scenarios | VERIFIED |
| 101, C-30 7 h | 60 / 17 / 1 | 444, 8 scenarios | VERIFIED |
| 102, C-30 8 h | 8 / 5 / 1 | 609, 8 scenarios | VERIFIED |
| 103, C-30 17 h | 0 / 0 / 0 | 418, 5 scenarios | VERIFIED |
| 105, C-30 early60 all active weekdays | 0 / 0 / 1 | 1.471 | VERIFIED |
| 124–125, M⁺-30 | 66 → 2 | 1.471 | VERIFIED; denominator missing from prose |
| 124–125, V-30 | 66 → 2 | 1.470 | VERIFIED; different denominator missing |
| 125, U | 129 → 63 | 1.512 | VERIFIED |
| 125–126, U 17 h | 28 → 28 | 437 | VERIFIED; denominator missing |
| 126, C-30 17 h | 0 → 0 | 418 | VERIFIED; denominator missing |

Independent per-rider proportional-pad coefficients are 0,033695361515 / 0,009864166374 / 0,000144323318 for 7/8/17 h, yielding exactly 17/5/0 late riders. The table's scenario means remain 6,013604% / 1,943985% / 0,169344%; they are not 68/1.471,22/1.471,2/1.471 expressed as percentages.

Sources: `S/optimize/test-family-a-causal-no15-2026-10-06-cells.tsv`, `forecast_family_a.py:110–141`, and `codex-work/R19-stage1a-analysis.json:runs[].riders`; probe JSON `forecast`, `padding`. S means `E:/Code/Report_INT3508/ridebound-scratchpad`.

### 3.2 Snow share and runner identity

Fresh raw reads of all eight snow runs give 601 served, 41 naive-late and 34 historical-forecast-late riders; scenario means are 7,188012% and 5,937271%. The selected 41 riders' sums are:

| Quantity | Recomputed value |
|---|---:|
| Total naive lateness | 3.445,933 s |
| Signed dispatch component | 8,566 s |
| Historical extension | 251,496483206 s |
| Residual | 3.185,870516794 s |
| Dispatch share | 0,248582895% → **0,25%** |
| Maximum absolute dispatch movement, all 601 | 25,187 s |

Thus the new figure label at 159 and EV 178 are correct. No late-cohort sum is used to prove the per-rider bound.

All eight snow manifests and all **51 C-30 folders** in the main run directory have the same five identity fields. The 51 are directory inventory, not a claim of 51 main test scenarios: the registered split is 34 test + 15 calibration + 2 original failure folders.

| Field | Independently checked value |
|---|---|
| `binarySha256` | `a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac` |
| `coreCommitSha` | `1ce15e92d2c1459d4254bbbcd581529197257fb2` |
| `policyId` | `ridebound-hard-vector` |
| `policyVersion` | `tier3-exploratory-v1` |
| `policyConfigurationHash` | `a2f11a3ada0773f9b30b85c56c935058e2e931f13c907f46b2ddfff8c1285f1c` |
| Recovery | `no-worse-than-reference-v1` |

The current archived `runner-tier3-v2/RideBound.Runner.dll` hash matches `binarySha256`. Canonicalizing C-30.json and wp4-tier3-v2.json, then hashing the domain-separated pair of raw digests under the opened `Wp4PolicyConfigurationBinding.cs` specification, independently reproduces the recorded binding. This is stronger than merely observing two equal unverified manifest strings. It supports B 376–379/N4B8-05 and removal of the obsolete Part A snow caveat. It does not establish equivalence of a newly rebuilt binary or real-world validity.

### 3.3 K, completed runs and CX-10

The three dated forecast config files each specify `horizonBins:2`; `run_forecast.py:70–72` binds the tested jobs to them. The opened wrapper `preflight_world_v1_3.py:85–89` averages the **current and next** profile bins and divides by the current one. K is 2; it is not two future bins after the current one.

The completion census independently gives **C-30F 14/16 and M⁺-30F 15/16**, hence 29/32 complete and three stops. Raw acknowledged-certificate recounts match every selected BIC row:

| Matched cohort | Forced / acknowledged | Scenario-mean forced rate |
|---|---:|---:|
| C-30F, its 14 completed scenarios | 0 / 7.839 | 0% |
| C-30 baseline, those same 14 IDs | 0 / 7.845 | 0% |
| M⁺-30F, its 15 completed scenarios | **3.849 / 8.496** | 47,61589255% → 47,6% |
| M⁺-30 baseline, those same 15 IDs | **5.121 / 8.468** | 62,77032087% → 62,8% |

The pooled M⁺ fractions are about 45,30% and 60,47%, respectively; these are different estimands. Keeping the displayed means and adding their separately labeled pooled counts is correct. `verify-numbers-v2.json:dispatcher` contains the matched per-run counts and config values; `S/optimize/independent-B/b_cells.tsv` supplies the cross-check, not the sole basis of the raw recount.

### 3.4 ML integer counts

All rows below are at calibration target E=30, `window=all`, in the corrected A1 table. `fc+uniform` is the measured-traffic control; uniform and fc+uniform coincide for static FREE. Do not accidentally use the measured-traffic `uniform` rows as the forecast-plus-pad comparator.

| Cohort / method | Printed late60 rate (%) | Recovered late count | Early count where relevant |
|---|---:|---:|---:|
| U 15/11, forecast + uniform pad | 1,379 | 2 / 145 | 0 / 145 |
| U 15/11, full tree model | 0,690 | 1 / 145 | 1 / 145 |
| U 16/11, forecast + uniform pad | 0,500 | 1 / 200 | 1 / 200 |
| U 16/11, full tree model | 0,500 | 1 / 200 | 5 / 200 |
| C-30 15/11, control and all three models | 0 | 0 / 147 | varies by model/date |
| C-30 16/11, control and all three models | 0 | 0 / 197 | varies by model/date |
| Static FREE 13/11, uniform pad | 12,887 | 104 / 807 | 0 / 807 |
| Static FREE 13/11, full tree model | 11,648 | 94 / 807 | **57 / 807** (7,063%) |
| Static FREE 13/11, two-state-feature ablation | 11,648 | 94 / 807 | 59 / 807 (7,311%) |

The requested 2→1/145,1/200,0/147,0/197,104→94/807 and 57 early are all **VERIFIED AS DERIVED COUNTS**. The ablation still changes early arrivals and extensions; B's narrowed “không đổi số khách trễ” is acceptable for the named U/FREE comparisons, not a general statement about all metrics or all arms.

## 4. Judgment on back-calculation and the previous R29 wording

**Accept it with explicit provenance.** Source code `ml_pilot_run.py:37–42` computes 100 × integer count / n; lines 175–176 serialize rates using `round(...,3)`. For printed percentage r, any compatible count k must satisfy:

`|100 k / n − r| ≤ 0,0005`, equivalently `|k − n r / 100| ≤ 0,0005 n / 100`.

The probe enumerates **every** integer 0…n in that interval and finds exactly one in each used row. At n=145/200/147/197/807, the radii are 0,000725/0,001000/0,000735/0,000985/0,004035 counts. The largest interval width is 0,00807, far below one count. Values stored as 0,69 or 0,5 are still outputs of the same three-decimal rounding code; trailing zeros are only formatting.

The reviser's general “n < 200.000”/“radius < 1 therefore unique” shortcut is not a valid general criterion: an interval with radius below 1 can contain two integers. A width below 1 (e.g. n < 100.000 under this bound), plus finding a compatible integer, is sufficient; explicit enumeration is better here. No row is near a tie-boundary ambiguity.

R29's blanket sentence that exact model-count numerators remained unavailable from the corrected table alone was **too strong**. That round did not test integer inversion. It was a conservative verification choice, not a prohibition, and this source-backed arithmetic resolves it. The derived counts do not validate feature extraction, fitting, predictions or unseen-day performance. §1.3 gives acceptable thesis wording without implying a new raw prediction recount.

## 5. Every rejected comment: verdict and reason

| Comment | R37 judgment |
|---|---|
| **CX-10** | **REVERSE THE DEFERRED REJECTION.** Both pools independently checked against raw certificates; enter with separate aggregation label, §1.4. R29 itself offered them as optional. |
| **B47** | **UPHOLD.** OUTLINE-V2:197 explicitly requests “vai trò của từng thành phần”. Keep that lead-in; the alternative four-part heading is also obsolete after v10 merges one part into the opening. |
| **L-02** | **UPHOLD FOR THIS BODY.** C-60/C-120 screen rates were removed from body as well as absent from the two-column table. The cited evidence does not supply registered complete cost rows for an expanded table. Do not invent them; omission is defensible scope/page control, not proof those quantities could never be computed. |
| **L-04** | **UPHOLD.** The style rule keeps table precision while prose rounds. Table 50 has 0,3069/0,0794; 61–64 interprets 0,31/0,08. |
| **L-15** | **UPHOLD WITH EXISTING CAPTION.** Pooled late counts and mean scenario extension measure different things and may share a table when each aggregation is identified. Snow caption 318–320 does so. No need to fabricate a pooled extension column. |
| **L-23** | **PARTLY REVERSE.** Lack of a positive independent check is a reason to state its scope, not reject the limitation. R37 now checks main replay/pad arithmetic with independent per-rider extraction and fresh snow historical replay; integer recovery does not independently validate the learned-model pipeline. Use §1.8, not a blanket claim of either full validation or no validation. |
| **L-26** | **REVERSE FOR A LIMITATION; UPHOLD AGAINST INVENTED RESULTS.** No seed-sensitivity runs are available and simulations are prohibited. State the missing sensitivity and affected conclusion, §1.8. One run per scenario and a fixed seed do not establish seed robustness. |
| **L-27** | **UPHOLD AS OPTIONAL ORGANIZATION.** Latest Ch3 477–481 already interprets saturation and points to B 370–372 for the counts. Relocation is possible only with synchronized counts and a direct reference; avoid circular references if cutting B. |
| **L-31** | **UPHOLD REJECTION OF ITS PREMISE.** Proportional pad early60 was measured, and is 0/1.471; this is freshly reproduced. Do not add “not measured” as a limitation. |
| **L-33/L-52** | **REVERSE THE NO-OUTPUT OBJECTION; OPTIONAL BODY INSERTION.** A permitted read-only probe now provides the 2.207-common-rider comparison below. It is descriptive on the served intersection, not a causal matched control. The correctly labeled all-request totals remain useful; the new numbers can live in evidence/appendix to protect the budget. |
| **L-34** | **UPHOLD.** BRIEF-CH4B-WRITER:29–30 explicitly says state the four conditions without saying when they were set. Preserve actual calibration and preview caveats, but do not import prohibited plan/timing narrative. |
| **L-40** | **UPHOLD.** “Theo sổ” and the forecast-dependent explanation name an accounting component consistent with Ch3. Figure 171–174 states the residual is not inherently unknowable; clipped snow wording now distinguishes its convention. No causal attribution is established or needed. |
| **L-50** | **UPHOLD.** Evidence supplies no reason why the cost-first trajectory experiment was not run. State absence and what cannot be concluded; do not invent workload/deadline explanations. |
| **L-60** | **UPHOLD AGAINST A TOLERANCE RESULT.** No tolerance variant was run. The three failures are of the particular tested implementation; 187 correctly limits that conclusion. A tolerance sensitivity can be future work, without an invented outcome or a general verdict against all dispatcher forecasts. |

### The now-available common-rider probe

`verify-supplement.py` independently joins the saved Codex per-rider records by `(scenario, request)` and applies the 30-second pad to U's forecast quotes. Results:

| On the same 2.207 served riders | U forecast + pad30 | C-30 forecast |
|---|---:|---:|
| Late beyond 60 s | 94 | 9 |
| Late beyond 120 s | 59 | 0 |
| Early beyond 60 s | 40 | 4 |
| Not late beyond 60 s | 2.113 | 2.198 |
| Not late beyond 120 s | 2.148 | 2.207 |

Saved in `verify-supplement.json:common_served_cohort`. These use each method's own first forecast/padded promise and its own archived journey, despite the common request IDs. Restricting to an intersection selected by both policies removes unmatched service counts from this description; it does not establish an intervention effect or erase the operator-level trade-off.

If used, the exact compact Vietnamese text is:

> Chỉ xét 2.207 khách được cả hai cấu hình phục vụ, điều phối không trần có dự báo và đệm 30 giây có 94 khách trễ quá một phút, 59 quá hai phút và 40 tới sớm quá một phút; luật C trần 30 giây có dự báo lần lượt có 9, 0 và 4. Đây là mô tả trên nhóm khách chung, không phải phép so ghép cặp về tác động của luật.

Register that derivation with the saved script/output before importing it. Its presence is optional; the correction to the no-evidence rationale is not.

## 6. Padding fairness and regression results

The opening honestly reports the **one-minute tie** 2.328 versus 2.328 and **two-minute advantage of padded U** 2.366 versus 2.338, all on 3.672 input requests. Independent saved per-rider arithmetic gives:

| Quantity | U forecast + pad30 | C-30 forecast |
|---|---:|---:|
| Served | 2.434 | 2.338 |
| Mean quote extension | 37,183331 s | 7,367123 s |
| Exposed to nonzero dispatch movement | 174 | 33 |
| Maximum absolute cumulative dispatch movement | 590,133 s | 29,239 s |
| Late60 / late120 | 106 / 68 | 10 / 0 |
| Early60 | 44 | 4 |

Padding leaves U's dispatch decisions, served riders and physical arrivals unchanged. The paragraph uses added promise duration, not total trip length. The bound concerns dispatch accounting; neither padding nor C guarantees actual arrival at the original first promise. This is an evidence-backed answer to “why C if padding ties?”, once §1.1 separates 30-second construction from observed 29,2 and limits the choice claim to C-30. The later C-120 point remains important evidence against a universal claim about “luật C”.

**New overclaims/regressions identified:** designed 29,2 bound; exact full-promise equality; minimum necessary fivefold padding; all-C choice statement; lost 41,3 scenario-mean label; lost M⁺/V/17 h denominators; lost 34-scenario scope for 2.305; English “gradient”; one misleading EV rounding note. §1 supplies replacements.

**References:** the root's `verify-supplement.py` independently confirms the agents' ref scan: 24 visible ref/eqref occurrences, 11 distinct B labels, no duplicate labels across B v10/A v4/latest r33 Ch3/Ch2 v4. All resolve except `phuluc:C` at B 382. Removed `bang:c4-haiphia` has no inbound occurrence in those latest other chapters. Ch2 v4 introduces no broken B reference. This is source-level verification, not compiled reference/citation validation.

**Language:** no prohibited novelty/cap-optimality or sealed-plan phrases found in the visible B body. The English gradient issue is real. Technical filenames/field names remain hidden evidence anchors, not terminology to introduce into running Vietnamese sentences.

**Caveats retained:** different cohorts/2.207 overlap, quote replay, inactive weekend forecast, three viewed mornings/shared source 12/11, negative ML comparison, completed-run restriction, snow morning-prefix/current-anchor/same-day-pad/oracle information limits, clipped split, generator coverage limits, sampled zero dwell, low load/short selected trips, no rider response or incumbent reassignment, five dependent days/previewed results, pickup-display conflict, archive-rebuild equivalence, unrun cost-first/per-step/relaxed-deadline comparisons and no measured user/business value. The snow identity caveat is legitimately resolved, not silently suppressed; Part A must catch up.

## 7. Rank the NOTES §4 cuts by least loss

Split the bundled NOTES items: their deletions have very different costs to the argument. Approximate savings are the NOTES estimates, not measurements of a typeset PDF.

| Rank | Listed cut | Judgment |
|---:|---|---|
| 1 | §4.1, remove untested hypothesis, about 30 tokens | Safest. Keep actual model limits and the explicit setup scope; exact replacement in §1.7. |
| 2 | §4.1, merge Integration into Model, about 25 | Safe structural economy **while keeping both pickup-display and rebuilt-runner limits**. Update 402's four-group introduction if group count changes. |
| 3 | §4.5, remove saturation sentence, about 30 | Conditional: put exact 3.503/3.506/3.504 counts in Ch3 and fix its reference first. Ch3 currently points here; delete now and their numerical support disappears. |
| 4 | §4.2, shorten dispatcher forecast, about 80 | Preserve K=2/current+next, 3/32 failures, 14/15 complete, same-15 baseline, mean versus pool and implementation-only conclusion. Move individual failures/details only to an actually existing appendix. |
| 5 | §4.2, move ML details, about 170 | Conditional on actual Appendix C. Retain locally fixed 12–13 profile, target 30 on calibration, viewed test days, four conditions or exact appendix pointer, derived-count provenance and negative result. |
| 6 | §4.3, remove C-120 paragraph, about 45 | Prefer compress, not erase: keep a sentence that the 120-second point differs by threshold and served cohort. It prevents the C-30 comparison becoming a general domination claim. |
| 7 | §4.4, remove blend definition, about 35 | Shorten instead: “Cách trộn dùng trung bình nhân của dự báo lịch sử và mức tăng tắc đường cùng ngày.” The input column alone does not define the combination rule. |
| 8 | §4.1, replace data-reuse bullet with Part A ref, about 45 | Conditional: keep the local snow/ML preview limitation. Part A's main-set reuse description does not automatically cover those experiments. Exact replacement in §1.7. |
| 9 | §4.6, remove accepted-count and 35,5 explanation, about 40 | Low priority. The hierarchy explanation answers the examiner; **never remove the two-rider 17,77 + 17,77 explanation while retaining the 35,5 table cell**. |
| 10 | §4.2, remove local three-morning caveat, about 25 | Do not cut as listed. Keep 121's local preview/shared-source limitation on those confidence intervals. |
| 11 | §4.1, remove no-reassignment clause, about 15 | Do not cut. It limits applicability of the cap's service cost independently of customer response. |

Even all nominal cuts sum to 540, leaving approximately 11,47 ruler pages. Safer cuts save less. Further compression or smaller tables is necessary to meet 11 under this ruler; a layout build cannot be claimed in this round. The instructed output is a verification report, so these are reviewable edits for the reviser, not unauthorized writes to the draft directory.

## 8. Evidence, reproducibility and remaining limits

Authoritative brief and CODEX-PARALLEL-RULES were re-read on resume; no new addendum appeared. Owner writing rules, corrected glossary, Addendum 1 §0, R29, revision log, both R27 reviews, NOTES, Addendum 6 and its errata informed the review. Two inherited-effort subagents supplied textual audits and ref scans. Their files were reviewed and material findings checked against the actual drafts/logs; root independently performed the numeric probes and final ref/common-cohort checks. Their numerical claims were not adopted without the root's probes.

Saved root artifacts:

- `verify-numbers-v2.py`, `.txt`, `.json`: successful required-number probes, own raw snow/forced readers, config binding, ML rounding enumeration and independent saved per-rider pad checks.
- `verify-supplement.py`, `.txt`, `.json`: source hashes/line counts, independent latest ref audit, common-served-cohort counts, Chapter 5 inventory and page-ruler arithmetic.
- `PROBE-RUN-NOTES.md`: interrupted/initial probe record; original scripts and source-inspection output preserved.

Source anchors for the two test executions were also directly read: `C:/RideBoundData/research/testrun-45f8026-eollf-2026-10-12.log` and `testrun-45f8026-eollf-dirtycheck-2026-10-12.log`. The clean-log passing counts sum to 1.024 of 1.025, with one named dirty-worktree test failing; the separate log records an untracked marker and 1/1 passed. No tests were executed here.

**Still cannot check:** actual pagination, float collisions/overfull boxes, assembled citation resolution, unseen Chapter 5 ordering, newly rebuilt-runner equivalence, full learned-model pipeline correctness, alternative solver seeds and real-world/customer/business effects. No such outcome is implied by successful saved-data arithmetic. The old R29 uncertainty about integer recovery and the snow binary/recovery identity is resolved within the precise scopes above.

**Integration priority:** repair the padding claims; restore cohort labels; disclose ML count derivation; add separately labeled verified decision pools; synchronize Ch3/Part A and the appendix dependency. Then shorten while retaining the numerical and applicability caveats.
