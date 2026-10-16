# R25 — Kiểm chứng sự kiện Chương 4, phần A (Claude, 2026-10-12)

**Đối tượng:** `rewrite-2026-10/drafts/08-chuong4-phanA.tex` (785 dòng; mục mở chương, 4.1–4.5, 13 bảng, 1 hình) và
`drafts/08-chuong4-phanA-NOTES.md`.
**Căn cứ:** `evidence/EVIDENCE-REGISTER.md` (A01…K52), `EVIDENCE-REGISTER-ADDENDUM-1.md` (mục 0, N-01…N-30, L1a-01…09),
`EVIDENCE-REGISTER-ADDENDUM-2-CH3.md` (X3-xx), `tang3/t38c120/C120-RESULTS.md`, và các output gốc tôi tự mở trong phiên
này (đường dẫn tương đối với `ridebound-scratchpad/`):
`codex-work/R15-audit-summary.txt` (A), `codex-work/R16-cap-outcomes.txt` (CAP), `codex-work/R17-screen-forecast-verification.txt`
(SF), `codex-work/R18-verification.txt` (NEW), `checks-addendum-1/recompute-addendum-1-2026-10-11.txt` (ADD1) và script
`recompute_addendum_1.py`, `check-snow-c30-2026-10-11.txt` (SNOW1), `derive-addendum-1-2026-10-11.txt` (DER1),
`claude-work/r21-stage1a/stage1a-report-2026-10-10.txt` (STG), `cum-witness-check-2026-10-10.txt` (CW21),
`claude-work/budget-block-diagnosis-2026-10-07.txt` (BUD), `wp14r-ladder-reanalysis-2026-10-08.txt` (LAD) và script,
`r17-rebuttal/r17-verify-dial` (DIAL17), `r17-wp14r-check` (WP17), `r13-final-judge/cumulative-decisive-check` (FJC),
`per-run-cumulative-only-b` (FJR), `r13-proposer/cumulative-vs-perinsertion` (CVP),
`optimize/report-extras/constraints-and-pooling` (CON), `lateness-distribution` (LATE), `codex-debate/common-riders-check`
(COM) và script, `exposure-check` (EXP), `tang3/t38/T38-REPORT.md` (T38) và `t38_analyze.py`, `tang3/sweep/sweep_analyze.py`,
`SWEEP-REPORT.md` (SWEEP), `tang3/w07/W07-REPORT.md` (W07), `w07_analyze.py`, `tang3/w07x/W07X-REPORT.md` (W07X),
`w07x/analysis/mechanism-2026-10-01.txt` (W07XM), `optimize/test-snow-2026-10-06-report.txt`; mã chỉ đọc
`C:/Code/RideBound-noworse/src/` (RunnerSession.cs:1005-1028, CommitmentDecisionValidator.cs:125-146,
HardVectorCandidateAssessor.cs:79-99, 244-300); `E:/Code/Report_INT3508/ridebound/noi-dung/08-chuong4.tex:120-140` (TEX08),
`10-tai-lieu.tex` (TEX10). Bản đối chiếu nhất quán: `drafts/07-chuong3-v3.tex` và `style/GLOSSARY-VI.md`.
Không đọc `codex-work/R25-*` hay tệp `reviews/*CH4A*` nào khác. Không sửa bản nháp; không chạy mô phỏng, build, cài, xóa;
chỉ tạo tệp này.

**Nhãn.**
- **OK** (= AGREE) — câu, ô bảng hay điểm hình nói đúng điều bằng chứng nói; số tôi đã đối chiếu với output gốc.
- **WRONG** — sai so với anchor; ghi giá trị hay câu đúng và anchor.
- **OVERSTATED** — nói rộng hơn bằng chứng (phạm vi, "theo cấu tạo" bỏ giả thiết, công bố thiếu về dữ liệu đã xem).
- **LABEL** — số đúng nhưng nhãn mẫu số / cách gộp / tên gọi thiếu hoặc dễ đọc sai.
- **UNSUPPORTED** (= CANNOT CHECK) — không có dòng sổ hay output nào đỡ câu.
Theo cách chia ba của coordinator: AGREE = OK; WRONG = WRONG + OVERSTATED + LABEL; CANNOT CHECK = UNSUPPORTED.

---

## 1. Bảng kiểm từng câu, từng ô

### Mục 4.1 Thiết lập (dòng 50–214)

| # | Dòng | Câu / ô (rút gọn) | EV của bản nháp | Kết luận | Sửa / anchor đã mở |
|---|---|---|---|---|---|
| 1 | 56-57 | FleetPy 1.0.2, dữ liệu chuẩn Manhattan, nối bộ chạy qua bộ chuyển đổi | B01 | OK | B01; X3-15 |
| 2 | 57-58 | Nhu cầu từ chuyến taxi New York tuần 11–18/11/2018 | B02, J18 | OK | J18 (FLEET:360-364) |
| 3 | 58-60 | Kịch bản = ngày × mẫu × khung 2 giờ; 108 yêu cầu từ mẫu 10%; 8 xe 4 chỗ | B02, B03 | OK | B02, B03 |
| 4 | 63-64 | Hệ số chung toàn thành phố, khung 15 phút, từ dữ liệu taxi, không phải tốc độ từng đoạn | B06, K49 | OK | B06 |
| 5 | 65 | Mỗi cặp kịch bản–cấu hình chạy một lần, kết quả tất định | B11 | OK | B11; T38:90 ("không có ngẫu nhiên") |
| 6 | 65-66 | Ba khung cùng ngày, cùng mẫu trùng 3–20/108 yêu cầu; không độc lập | B11, I05 | OK | T38:93 |
| 7 | 79-80 | Khung 7–9, 8–10, 17–19 giờ; chiều tuyết 14–16, 15–17 giờ | B08, B20 | OK | C03; B20; SNOW1:2-9 (w14, w15) |
| 8 | 81 | Yêu cầu: 108 mỗi kịch bản (tập chính, buổi sáng, tắc đường cố định) | B02, B20 | OK | 3.672 = 34 × 108; 864 = 8 × 108; 1.728 = 16 × 108 (B09, B15, B17) |
| 9 | 81 | … áp cả cho chiều tuyết (bảng là "tham số chung") | B20 | UNSUPPORTED | SNOW1 và báo cáo tuyết chỉ có số được nhận / phục vụ (601), không có số yêu cầu mỗi kịch bản. Hoặc kiểm, hoặc ghi "chiều tuyết: chưa kiểm số yêu cầu" |
| 10 | 82 | 8 xe, 4 chỗ | B03 | OK | — |
| 11 | 83-84 | 96 nút, bao đóng cặp đi–đến, không phải mạng đường phố | B03, K48 | OK | — |
| 12 | 85-86 | Đón trong 600 s; ngồi xe ≤ 1,5 lần đi thẳng | B03 | OK | (Chương 3 v3 ghi "10 phút"; cùng giá trị) |
| 13 | 87 | Dừng đón, trả 0 s (kiểm 3 lần chạy mẫu) | B05 | OK | — |
| 14 | 88-89 | Tắc đường "theo khung 15 phút", nền lấy lúc 00:00 "cho mọi kịch bản" — trong bảng mang tiêu đề "tham số chung của một kịch bản thử" | B06, B07 | OVERSTATED | Đúng cho tập chính, buổi sáng, chiều tuyết; **không** đúng cho tập tắc đường cố định (hệ số không đổi trong lần chạy, chính Bảng tập thử dòng 127-128; LAD:2-6). Sửa tiêu đề "Tham số chung của các tập dùng hệ số tắc đường đo" hoặc thêm "(trừ tập tắc đường cố định)" |
| 15 | 90 | Tối đa 100 phương án mỗi xe; mỗi lượt xét tối đa 2 yêu cầu mới (tập chính, buổi sáng, trần 120 s) | A24, R23 #105 | OK | A24 (WP4:9-23); X3-32 (GEN:54-96). Nên trỏ X3-32 thay "R23 #105" |
| 16 | 90-91 | … cùng giới hạn cho tập tắc đường cố định (bộ chạy cũ, cấu hình `wp14-development-v1`) | — | UNSUPPORTED | NEW:13 cho thấy cấu hình WP14 khác ở `policyVersion`, `solverExecution`, `solverExecutionEvidenceProfile`; giới hạn bộ sinh của nó chưa ai kiểm. Gộp vào sửa của #14 |
| 17 | 91 | OR-Tools 9.15, hạt giống 7 | A24 | OK | X3-17 |
| 18 | 103-104 | 34 trong 49 kịch bản 14–18/11; 15 hiệu chỉnh, chia theo (ngày, mẫu) | B08 | OK | B08 (SPLIT) |
| 19 | 105 | 14–16/11 ngày thường, 17–18/11 cuối tuần | B21 | OK | B21 (11/11/2018 là Chủ nhật ⇒ 14/11 thứ Tư … 18/11 Chủ nhật) |
| 20 | 120 | Tập chính: 34 kịch bản, 3.672 yêu cầu, 14–18/11; khung 7/8/17 giờ có 9/14/11 | B09 | OK | B09; ADD1:150-160 |
| 21 | 121 | Cấu hình tập chính U, C-30, C-120, M⁺-30, M⁺-60, V-30 | B10, L1a-01 | OK | T38:46; C120R:10 |
| 22 | 121 | Bản lưu trữ, luật phục hồi không tệ hơn | A19, A28, X3-10 | OK | — |
| 23 | 122 | 170 (năm cấu hình) và 34 (C-120) lần chạy | B10, L1a-01 | OK | 170 = 34 × 5 |
| 24 | 124 | Buổi sáng: 8 kịch bản, 864 yêu cầu, 12–13/11, khung 7 giờ | B15 | OK | — |
| 25 | 124-125 | U; C và M⁺ ở 30–300 s | B15, B16 | OK | X3-28; W07X:20-29 |
| 26 | 125 | Bộ chạy "như tập chính" | X3-10 | OK | X3-10 (RW7:1-8; RW7X:6-8) |
| 27 | 125 | 88 và 104 lần chạy | B15, B16 | OK | 88 = 11 cấu hình × 8; 104 = 13 × 8 |
| 28 | 127 | Tắc đường cố định: 16 kịch bản, 1.728 yêu cầu, 12–13/11, khung 8 và 17 giờ | B17 | OK | LAD:2-6 (w08 8, w17 8) |
| 29 | 127-128 | "hệ số không đổi trong lần chạy" | LAD:2-6 | OK | LAD:2-6 `travelSnapshotVersion {1: 16}` (một bảng giờ đi suốt lần chạy, script dòng 22); B17. Chưa thành dòng sổ — đề nghị registrar thêm |
| 30 | 128 | FREE, U, C-30, C-60, C-120 | B17 | OK | X3-19 (LOCKS = `c1-nobudget` = U) |
| 31 | 128 | Bản cũ, không có luật phục hồi | B17 | OK | NEW:13 (`commitmentRecovery` vắng) |
| 32 | 128 | 16 lần chạy mỗi cấu hình | H13 | OK | LAD:2-6; WP17:2-19 |
| 33 | 130-131 | Chiều tuyết: 8 kịch bản, 601 lượt phục vụ, khung 14 và 15 giờ, C-30, bộ chạy chưa kiểm, 8 lần chạy | B20, N-26 | OK | SNOW1:2-10 (86+74+80+75+75+66+85+60 = 601); X3-10 lưu ý |
| 34 | 137-138 | U, M⁺, V dùng cùng bộ sinh, bộ kiểm, bộ chọn với C; U chỉ khác C-30 ở trần giờ trả | A08, H01 | OK | NEW:12 (`/policies/0/limits/1/hardLimit`); A09, A11 |
| 35 | 139 | Ghép tự do: chính sách chi phí cuốn chiếu mặc định, không qua bộ kiểm cứng | A17, K50, R23 #51 | OK | X3-38 (lưu ý: đọc trên mã hiện tại; FREE chạy bằng bộ chạy cũ). Nên trỏ X3-38 thay "R23 #51" |
| 36 | 143-144 | Lần chạy hỏng được thay bằng bản chạy lại hoàn tất | ADD1:6, mục 0.3 | OK | T38:12, 94 ("Phân tích dùng các job chạy lại"); ADD1:6; TEX08:121-123 |
| 37 | 144 | Kho có 1.991 bản ghi lần chạy | B19 | OK | — |
| 38 | 151-153 | Đúng giờ so với lời hứa đầu, chỉ trên khách được phục vụ; báo kèm 120 s vì hai ngưỡng cho kết luận ngược | C06, C08, C10 | OK | Tập chính: C−U = +31 ở 60 s, −5 ở 120 s (ADD1:12,17) |
| 39 | 153-155 | Định nghĩa gộp theo khách, trung bình theo kịch bản, chênh lệch | C27, K24 | OK | — |
| 40 | 158-159 | Phát lại: quyết định giữ nguyên, "chỉ lời hứa đầu được thay bằng lời hứa theo dự báo" | C09, F03 | WRONG (nhỏ) | Phép phát lại tính $D = \max(p, S)$ cho **mọi** lời hứa đón và trả đã công bố (X3-11; F01; DISP:1-8); các chỉ số của chương chỉ dùng lời hứa giờ trả đầu $D_0$. Sửa: "chỉ giờ báo cho khách đổi; các chỉ số dùng lời hứa giờ trả đầu $D_0$" (khớp Chương 3 v3 dòng 552-553) |
| 41 | 159-160 | Dự báo chỉ ở 21 kịch bản ngày thường; 13 kịch bản cuối tuần giữ lời hứa không dự báo | C09, F02, N-28 | OK | ADD1:5-8 (`forecast-active cells 21`); ADD1:113-114 |
| 42 | 160-161 | 12–13/11 không có dự báo | D02, F02 | OK | CAP:2; DIAL17:3-11 (`active 0`) |
| 43 | 175-176 | Bảng chỉ số — Lượt phục vụ: đếm trên số yêu cầu | C01 | OK | — |
| 44 | 177-178 | Trễ quá $T$: $a - D_0 > T$ (so sánh chặt), $T$ = 60/120/300/600 s | C06, C08 | OK | `sweep_analyze.py:107,128-129` (`a > t*1000`); ADD1:11-31 |
| 45 | 179-180 | Không trễ quá $T$ = phục vụ − trễ; chia số yêu cầu; bị từ chối không tính đúng giờ | C08 | OK | DIALPY:8-9; ADD1:11 |
| 46 | 181-182 | Tới sớm quá 60 s: $a - D_0 < -60$ | N-04 | OK | ADD1:92 |
| 47 | 183 | Lời hứa dài thêm $D_0 - p_0$, trung bình gộp theo khách được phục vụ | F06, N-06 | OK | ADD1:14,19,24 (`ext_sum_ms / served`) |
| 48 | 184-185 | Đi chung: có khách khác trên cùng xe trong [đón, trả) | N-09 | OK | STG §5; cùng quy tắc ở LAD (script dòng 39), nên Bảng tắc đường cố định dùng cùng định nghĩa |
| 49 | 186-187 | Bị điều phối dời giờ trả: ≥ 1 lần dời khác 0; độ dời $\sum|c|$ | C20, N-07 | OK | — |
| 50 | 188-190 | "Quyết định phải phục hồi: lượt quyết định mà luật lời hứa **loại hết phương án của một xe**, kể cả phương án giữ nguyên" | C13, A11 | WRONG | Theo mã và sổ, đơn vị là lượt quyết định được xác nhận có chứng chỉ "không bình thường": ít nhất một khách được miễn trừ vì **phương án giữ nguyên** của một xe bị cổng hạn chót / trần loại rồi được giữ nhờ luật phục hồi (X3-30; RunnerSession.cs:1012-1027; CommitmentDecisionValidator.cs:141-145; HardVectorCandidateAssessor.cs:252-300). Phục hồi "không đòi mọi phương án khác bị loại" (X3-09). Định nghĩa "loại hết" chép từ GLOSSARY-VI:93, vốn cũng lệch mã. Đồng thời **tên** lệch Chương 3 v3 (xem K-1). Sửa: "Lượt quyết định có xe bị ép: luật lời hứa loại cả phương án giữ nguyên của xe và xe đi theo phương án được miễn trừ (mục doichung)" |
| 51 | 191-193 | Phá lời hứa: C $\sum|c| > B$; hạn chót $a - p_0 > B$; V $\sum|z| > B$ | N-21, A11 | OK | `sweep_analyze.py:107,129-132` (`x_ms = level*1000`, nên M⁺-60 dùng 60 s); `t38_analyze.py:94-95,191-194` và `w07_analyze.py:46-56` (V = tổng $|z|$ > 30 s) |
| 52 | 189-193 | Gộp: trung bình theo kịch bản; số gộp ghi riêng | C13 | OK | — |
| 53 | 205-206 | Trần chính 30 s là mức đã dùng cho cấu hình có trần ở tập kịch bản tĩnh | K33, X3-18 | OK | TEX08:136-137 ("C1 … trần 30 giây cho tổng độ dời giờ trả"). **X3-18 đã bị bỏ khỏi sổ** (ADDENDUM-2:89): cần trỏ TEX08 trực tiếp hoặc nhờ registrar thêm dòng |
| 54 | 206 | Giữ nguyên cho tập chính, không chỉnh theo kết quả tập này | B10 | OK | T38:3-6 (cấu hình cố định trước job đầu); không nhắc kế hoạch — đúng luật chủ sở hữu |
| 55 | 207-208 | 30 s không phải ngưỡng cảm nhận hay chuẩn ngành | K52, D20 | OK | — |
| 56 | 211-213 | Ngưỡng, cách chia chọn sau khi xem dữ liệu phát triển; một kịch bản đã xem khi chạy thử | I06, B08 | OK | T38:8, 95 |
| 57 | 211-212 | "**mức thử 120 giây** được chọn sau khi đã xem dữ liệu của **các tập phát triển**" | I06, B10 | OVERSTATED | Thiếu công bố: mức 120 s được chọn **sau khi đã xem kết quả U và C-30 trên chính tập kiểm tra chính** và sau các phép sàng lọc ở 120 s trên tập đó: D14/SF:14 (59/148 yêu cầu bị từ chối của C-30 ở T3.8), E06/CVP:14-18 (4/2.434 khách U của T3.8), K42 ("120 s là mức thử được chọn"), H12 lưu ý ("trên panel đã xem"); C-120 chạy ngày 10/10 (C120R:10), sau T3.8 (2/10, T38:6). Sửa: "…mức thử 120 giây được chọn sau khi đã xem dữ liệu các tập phát triển và kết quả của điều phối không trần, trần 30 giây trên chính tập kiểm tra chính" |

### Mục 4.2 Kết quả chính (dòng 217–403)

| # | Dòng | Câu / ô (rút gọn) | EV | Kết luận | Sửa / anchor đã mở |
|---|---|---|---|---|---|
| 58 | 220-222 | 3.672 yêu cầu; C-30 phục vụ 2.338, ít hơn U 96; trễ quá 60 s 203 → 76; không trễ 2.231 → 2.262 | C01, C02, C06, C08 | OK | ADD1:12,17; A:7,9 |
| 59 | 225-226 | Hạn chót chỉ mượn của Schulz–Pfeiffer, 30 và 60 s thay 900 s | J10, J11 | OK | — |
| 60 | 226-227 | Cùng bộ chạy, bộ sinh, bộ chọn, luật phục hồi không tệ hơn | A09, A19 | OK | — |
| 61 | 243 | Bảng chính, hàng U: 2.434 / 203 / 2.231 / 2.332 / 555 | C01, C06, C08, N-09 | OK | ADD1:12,136; A:9 |
| 62 | 244 | Hàng C-30: 2.338 / 76 / 2.262 / 2.327 / 313 | idem | OK | ADD1:17,137; A:7 |
| 63 | 245 | Hàng M⁺-30: 2.338 / 74 / 2.264 / 2.327 / 307 | idem | OK | ADD1:27,139; A:8 |
| 64 | 247-248 | M⁺-60 2.347; V-30 2.336 (các ô khác "chưa đưa vào bảng") | C01 | OK | T38:46,57. Ghi chú: EXP:5-6 có trễ quá 60 s của M⁺-60 (79) và V-30 (74) nếu muốn điền một cột (chưa có dòng sổ, chưa có không trễ quá 120 s) |
| 65 | 233-235 | Tiêu đề: gộp mọi kịch bản; "không trễ quá" trên 3.672 yêu cầu | — | OK | — |
| 66 | 254-255 | 2.338 − 76 = 2.262 | C08 | OK | số học |
| 67 | 258-259 | −96 = 2,61 điểm % số yêu cầu = 3,94% số lượt của U | C02 | OK | tính lại: 96/3.672 = 2,614 điểm %; 96/2.434 = 3,944% |
| 68 | 259-260 | 8 giờ 1.014 → 975; 17 giờ 904 → 852; 7 giờ −5 | C03 | OK | ADD1:150-159; T38:50-52 |
| 69 | 260-261 | Đi chung 555 → 313; 22,80% → 13,39% gộp theo khách | N-09 | OK | ADD1:136-137 (tính lại 555/2.434 = 22,80%; 313/2.338 = 13,39%) |
| 70 | 261-262 | Không có bằng chứng về giá trị của chuyến đi chung | N-20 | OK | — |
| 71 | 265-266 | Trễ giảm 127; không trễ tăng 31; +31 = −96 − (−127) | C06, C08 | OK | ADD1:186 |
| 72 | 266-267 | Ở 120 s U có 2.332, hơn C 5 lượt | C08 | OK | 2.332 − 2.327 = 5 |
| 73 | 267-268 | 2.207 chung, 227 chỉ U, 131 chỉ C | C04 | OK | A:18; ADD1:145 (2.207 + 227 = 2.434; 2.207 + 131 = 2.338) |
| 74 | 268-269 | 31 lượt là chênh hai tổng, không phải 31 khách cụ thể | C04 | OK | — |
| 75 | 269-270 | Với 2.207 khách chung, "luật C chờ lâu hơn 0,5 giây và ngồi xe ngắn hơn 10,5 giây" | C05 | LABEL | Là **trung bình** theo khách chung: COM:2-3 (+0,522 s; −10,507 s), `common_riders_check.py:29` (`st.mean`). Thêm "trung bình". (Có thể thêm: ngồi ngắn hơn ở 229, dài hơn ở 68 khách, COM:3) |
| 76 | 270-271 | Tập khách hình thành sau khi áp luật, không phải phép so ngẫu nhiên | C05 | OK | — |
| 77 | 274-275 | Cùng 2.338 lượt; 2.332 chung, mỗi bên 6 riêng; 76 so với 74 | C01, C04, K07 | OK | A:19; ADD1:146 |
| 78 | 275-276 | M⁺-60 2.347; V-30 2.336 | C01 | OK | T38:46 |
| 79 | 276-277 | Số phục vụ các luật lời hứa gần như ngang nhau | C32 | OK | C16; T38:82-84 |
| 80 | 294 | Bảng nghĩa vụ, C-30: 0 / 0 / 0 | C13, N-21 | OK | T38:58-60; ADD1:6,193 |
| 81 | 295 | M⁺-30: 41,3 / 14,5 / 28 | C13 | OK | T38:58-60; ADD1:189 (41,31 / 14,48 / 28) |
| 82 | 296 | M⁺-60: 22,5 / 4,2 / 22 | C13 | OK | T38:58-60 |
| 83 | 297 | V-30: 53,8 / 21,6 / 34 | C13 | OK | T38:58-60 |
| 84 | 283-285 | Tiêu đề: hai cột tỉ lệ trung bình theo kịch bản; cột cuối đếm kịch bản | C13 | OK | `t38_analyze.py:190-208` (mean over cells) |
| 85 | 303-305 | Cách đọc: M⁺-30 TB mỗi kịch bản 41,3% phải phục hồi, 14,5% tới muộn quá 30 s; 28/34 kịch bản | C13, N-21 | OK | — |
| 86 | 308 | C: 0 quyết định phải phục hồi, 0 khách vượt trần, ở cả 34 kịch bản | N-21 | OK | ADD1:6 (0/20.101), ADD1:193 |
| 87 | 308-310 | "Điều này **đúng theo cấu tạo**: phương án giữ nguyên … **luôn** qua luật C" | A22 | OVERSTATED | Nhận xét của Chương 3 v3 (dòng 362-366) chỉ đúng **dưới giả thiết (N)** và $0 \le L_r \le B$; A22 cũng ghi "dưới giả thiết các kiểm tra khác đều qua". Chương 3 v3 dòng 372-375 còn nói tính chất này **không riêng luật C** (U cũng không bao giờ bị ép: ADD1:5, 0/20.760). Sửa: "…đúng theo cấu tạo, dưới giả thiết (N) của Nhận xét …; điều phối không trần cũng có 0 trong 20.760 quyết định bị ép" |
| 88 | 310-311 | Hạn chót so với lời hứa đầu nên riêng $x$ có thể loại cả phương án giữ nguyên | A10 | OK | — |
| 89 | 311-313 | Gộp: 7.710/20.103 (38,35%); 289/2.338 (12,4%) | N-21 | OK | ADD1:189 (tính lại 38,353%; 12,361%) |
| 90 | 313-315 | Khung 7 giờ: 9/9 kịch bản, "trung bình 36,5% … 75,6%"; 17 giờ: 5/11, "1,0% và 5,0%" — ngay sau câu "Tính gộp, …" | N-21, C14 | LABEL | Các tỉ lệ này là **trung bình theo kịch bản** (ADD1:190,192); đặt ngay sau "Tính gộp" nên dễ đọc là gộp. Số gộp: 7 giờ 181/509 = 35,56% khách, 3.447/4.564 = 75,53% quyết định; 17 giờ 8/852 = 0,94%, 328/7.163 = 4,58% (ADD1:190,192). Ghi "trung bình theo kịch bản" |
| 91 | 315 | Ở 60 s các tỉ lệ giảm nhưng không về 0 | C13 | OK | Đúng ở mức toàn tập (22,5% / 4,2% TB theo kịch bản; 3,4% gộp phá hứa, T38:111). Số theo khung giờ ở 60 s không có trong sổ — câu chỉ nên nói về mức toàn tập |
| 92 | 318-320 | Bảng không so hai chuẩn đúng giờ; mỗi luật giữ điều nó hứa | C13, K05 | OK | — |
| 93 | 323 | Trễ giảm "ở mọi ngưỡng" | N-24 | OK | Đúng cho 4 ngưỡng trong bảng |
| 94 | 338-341 | Phân bố trễ: 203 / 102 / 18 / 2 và 76 / 11 / 0 / 0 | N-24, C07 | OK | ADD1:12,17; A:7,9 |
| 95 | 338-341 | Trên 100 yêu cầu: 5,53 / 2,78 / 0,49 / 0,05 và 2,07 / 0,30 / 0 / 0 | N-24, C28 | OK | tính lại /36,72: 5,528; 2,778; 0,490; 0,054; 2,070; 0,300 |
| 96 | 343 | Trễ lớn nhất 11 phút (U), 3,87 phút (C-30) | C26 | OK | CON:4,11 (+660,1 s; +232,3 s); LATE:4,11 |
| 97 | 349-350 | Cách đọc: 18 lượt quá 5 phút = 0,49/100 yêu cầu | N-24 | OK | — |
| 98 | 353-354 | U: 2 lượt quá 10 phút, trễ nhất ≈ 11 phút; C: 0 quá 5 phút, 3,87 phút | N-24, C26 | OK | — |
| 99 | 354-355 | 72 trong 76 khách C trễ không có lần dời do điều phối được ghi | C21, K39 | OK | A:7 `late60_and_exposed` 4; đúng câu của K39 |
| 100 | 355-356 | Phần trễ này là phần lời hứa theo dự báo nhắm tới | K39 | OK | Trỏ tiếp; C09 (76 → 10) đỡ |
| 101 | 374-386 | Bảng ngày × khung: 13 hàng × 5 ô (kịch bản, Δphục vụ, Δtrễ, Δkhông trễ, số kịch bản C không kém) | N-22 | OK | ADD1:173-185, từng ô khớp. Tính lại: số kịch bản theo khung 9/14/11; mọi hàng thỏa Δkhông trễ = Δphục vụ − Δtrễ |
| 102 | 388 | Hàng cộng: 34 / −96 / −127 / +31 / 29 | N-22 | OK | ADD1:186; tôi cộng lại cả bốn cột từ 13 hàng |
| 103 | 394-395 | Cách đọc 16/11, 17 giờ: −11, −21, +10; 2/3 | N-22 | OK | ADD1:180 |
| 104 | 398-401 | 34/34 kịch bản C không nhiều trễ hơn; 29/34 không ít đúng giờ hơn; 25/25 ở 8 và 17 giờ; 7 giờ 3 hơn, 6 bằng | N-22, C30 | OK | ADD1:167-169,186; NEW:4 |
| 105 | 401-403 | 34 kịch bản thuộc 5 ngày, không độc lập; mô tả | I05, B11 | OK | — |

### Mục 4.3 Phần do điều phối (dòng 406–483)

| # | Dòng | Câu / ô (rút gọn) | EV | Kết luận | Sửa / anchor đã mở |
|---|---|---|---|---|---|
| 106 | 409-411 | 33/2.338 bị dời, mỗi khách ≤ 29,2 s; U 174/2.434, một khách 590,1 s (gần 10 phút) | C20, N-23 | OK | ADD1:104,106 (590.133 ms = 9,84 phút) |
| 107 | 428 | Bị dời: 174 (7,15%) / 33 (1,41%) / 103 (4,32%) | C20, N-07 | OK | tính lại 7,149 / 1,411 / 4,315% trên 2.434 / 2.338 / 2.387 |
| 108 | 429 | Dời từ hai lần: 12 / 0 / 0 | C20, N-07 | OK | ADD1:104,106,108 (`k2`) |
| 109 | 430 | Tổng dời lớn nhất: 590,1 / 29,2 / 118,9 s | C20, N-07 | OK | ADD1 (`S_max_ms` 590.133 / 29.239 / 118.938) |
| 110 | 431 | Trung vị mỗi lần dời: 108,6 / 8,3 / 62,5 s | C22, N-23 | OK | ADD1 (`change_median_s` 108,636 / 8,295 / 62,544; số lần 187 / 33 / 103); CON:6,13 |
| 111 | 433 | Trễ quá 60 s từng bị dời: 134/203; 4/76; 60/132 | C21, N-23 | OK | ADD1:104,106,108 |
| 112 | 434 | Phần tính cho điều phối: 73,4 / 1,2 / 38,8% | C24, N-23 | OK | ADD1 `ledger_dispatch_share_late60` 0,7344 / 0,0119 / 0,3884; công thức = $\sum c$ có dấu / $\sum (a - p_0)$ trên khách có $a - p_0 > 60$ s (`recompute_addendum_1.py:460`), đúng $q$ của eq:so; CON:5,12 |
| 113 | 419-421 | Tiêu đề: mẫu số dòng đầu là khách được phục vụ; độ dời = tổng $|c|$ | — | OK | — |
| 114 | 440-442 | Cách đọc hàng U | C20 | OK | — |
| 115 | 444-445 | Dưới 30 s mỗi khách bị dời đúng một lần, trung vị 8,3 s; U 108,6 s trên 187 lần | C22, E02 | OK | ADD1:104,106 (`maxk 1`, `changes 187`) |
| 116 | 445-446 | 29 dời muộn; 4 kéo sớm, mỗi người đúng 1 ms | C23, N-05 | OK | ADD1:106-107 (`net_positive 29`, 4 × [−1]) |
| 117 | 446-448 | 134/203, giao hai tập, không nhân quả | C21 | OK | — |
| 118 | 448-449 | Theo eq:so, phần điều phối 73,4% / 1,2% | C24 | OK | xem #112 |
| 119 | 449-450 | Dưới 30 s gần như toàn bộ số giây trễ nằm ở hai phần kia | C24 | OK | 98,8% |
| 120 | 453 | "Trần vẫn giữ ở kịch bản không có dự báo và ở ngày có sự kiện" | N-28, N-26 | OK | Số đúng. Lưu ý cách đặt câu: dự báo chỉ là phát lại, không vào bộ điều phối (F03; Chương 3 v3 dòng 552-553), nên vế "không có dự báo" không phải phép thử độc lập; vế chiều tuyết mới có thông tin |
| 121 | 454-455 | Cuối tuần: lớn nhất 29,2 s (trần 30) và 116,5 s (trần 120) | N-28 | OK | ADD1:113-114 |
| 122 | 455-456 | Tuyết: 8/601 bị dời, lớn nhất 25,2 s, 0 vượt, 0 phải phục hồi trong 5.067 | N-26 | OK | SNOW1:10 |
| 123 | 459-461 | Một khách "đã muộn hơn lời hứa đầu 79,0 s", hoàn toàn do $x$; $c$ trước đó 0 | D05 | OK | W07XM:6 (`sum x 79.0, sum c 0.0, p_last − p_first 79.0`). Lời khuyên chữ: đây là **giờ trả đang hứa** đã lùi 79,0 s so với lời hứa đầu, không phải khách đã tới muộn |
| 124 | 459-460 | Khách đó "đang trên xe" | D05 | UNSUPPORTED | Chỉ dòng sổ D05 viết "đang trên xe"; anchor gốc W07X:54 ghi "khách đang có", W07XM:6 không ghi giai đoạn. Sửa "một khách đã nhận" hoặc kiểm giai đoạn trong transcript |
| 125 | 461-462 | Phương án ghép thêm dời khách 68,3 s | D05 | OK | W07XM:6 ($c$ = 68,3 s; $x$ = 0,1 s) |
| 126 | 462-463 | Ở 90 s, hạn chót loại vì muộn ≈ 147 s | D05 | OK | W07X:54; 79,0 + 0,1 + 68,3 = 147,4 s |
| 127 | 463 | C cho qua vì 68,3 s | D05 | OK | $L = 0$, 68,3 ≤ 90 |
| 128 | 463-465 | Ba chỗ tách ở 90 và 120 s; $x$ 61–79 s, $c$ 61–68 s | D05 | OK | W07X:54-59; W07XM:2-16 (60,9 + 61,2 s) |
| 129 | 465 | Mỗi lần C nhận thêm đúng một khách | D05 | OK | W07X:62 |
| 130 | 466 | Theo mô hình tại cùng trạng thái, không nhân quả | K04 | OK | — |
| 131 | 469-472 | 1.334 bị từ chối; 148 có bản ghi chặn; U phục vụ 116; 1.186 chỉ lý do cấu trúc | D13, K10 | OK | BUD:2-5 (148 = 32 + 116; 1.186 = 1.075 + 111); ADD1:6 (1.334); 148 + 1.186 = 1.334 |
| 132 | 472-474 | 845 bản ghi ở 643 yêu cầu; 495 cuối cùng được phục vụ | D16, E01 | OK | SF:2 (records 845, pairs 643, completed 495, rejected 148) |
| 133 | 477-478 | Mức vượt nhỏ nhất: trung vị 109,6 s, lớn nhất 524,8 s | D14 | OK | BUD:6 |
| 134 | 478-479 | 2/148 khách chặn đã dùng trần trước đó; cả 148 có một lần dời đơn lẻ vượt 30 s | D19 | OK | BUD:10; FJC:4-6 (C-30 `per-step-also 845`) |
| 135 | 479-480 | Ở 120 s, 59/148 qua sàng lọc | D14 | OK | BUD:8; SF:14 |
| 136 | 480-483 | Dừng ở lỗi đầu; không có nghĩa 59 được phục vụ; không chứng minh "chỉ vì trần" | K11, I08 | OK | — |

### Mục 4.4 Chọn mức trần (dòng 486–706)

| # | Dòng | Câu / ô (rút gọn) | EV | Kết luận | Sửa / anchor đã mở |
|---|---|---|---|---|---|
| 137 | 489-491 | C-120 phục vụ 2.387, giữa 2.338 và 2.434; 2.366 không trễ quá 2 phút > 2.327, 2.332 | N-06, L1a-02 | OK | ADD1:22,197; C120R:14 |
| 138 | 512 | Tắc đường cố định, FREE: 1.629 / 274 / 1.465 / 53,1 / 23,8 | D08, D09 | OK | WP17:2; LAD:2 |
| 139 | 513 | U: 1.584 / 47 / 1.557 / 21,8 / 3,9 | D08, D09 | OK | WP17:5; LAD:3 |
| 140 | 514 | C-120: 1.563 / 23 / 1.563 / 19,4 / 2,6 | D08, D09 | OK | WP17:9; LAD:4; A:3 (41/1.563 = 2,62%) |
| 141 | 515 | C-60: 1.540 / 0 / 1.540 / 17,3 / 1,3 | D08, D09 | OK | WP17:14; LAD:5 |
| 142 | 516 | C-30: 1.534 / 0 / 1.534 / 15,7 / 0,4 | D08, D09 | OK | WP17:19; LAD:6 |
| 143 | 503-504 | Tiêu đề: 16 kịch bản, 1.728 yêu cầu, bộ chạy cũ; ba cột đếm, hai cột gộp theo khách | D08 | OK | LAD script dòng 45 (chia cho served) |
| 144 | 522-523 | Cách đọc hàng C-120 | D08, D09 | OK | — |
| 145 | 526-527 | 1.629 → 1.534 phục vụ; 274 → 0 trễ; điểm gãy 60–120 s: 0 → 23 | D09, D11 | OK | dãy đơn điệu: 1.629, 1.584, 1.563, 1.540, 1.534; 274, 47, 23, 0, 0 |
| 146 | 527-528 | Bộ chạy cũ, không chuyển sang tập chính | B17, I12 | OK | — |
| 147 | 531-532 | 864 yêu cầu; phục vụ 660 / 661 / 664 / 666 (120–180) / 665 (240, 300, U); dao động 6 | D01 | OK | W07X:22-29; CAP:3-11; DIAL17:3-11 |
| 148 | 547 | Buổi sáng, U: 665 / 50 / 615 / 656 | D02 | OK | CAP:3; DIAL17:3 |
| 149 | 548 | C-30: 660 / 47 / 613 / 658 | D02 | OK | CAP:4; DIAL17:4 |
| 150 | 549 | C-90: 664 / 50 / 614 / 660 | D02 | OK | CAP:6; DIAL17:6 |
| 151 | 550 | C-120: 666 / 51 / 615 / 659 | D02 | OK | CAP:7; DIAL17:7 |
| 152 | 538-539 | Tiêu đề: 8 kịch bản khung 7 giờ 12–13/11, không dự báo | D01, D02 | OK | — |
| 153 | 556-557 | Cách đọc hàng C-120 | D01, D02 | OK | — |
| 154 | 560 | C-120 hơn U một lượt; U là điểm đo, không phải cận trên | D01, K12 | OK | — |
| 155 | 561-562 | 30 → 120 s: +6 phục vụ, +4 trễ, +2 không trễ quá 60 s | D03 | OK | CAP:4,7 |
| 156 | 562-563 | Một kịch bản, trần 300 s: trễ nhất 307,3 s, 208,2 s do điều phối | N-30, D06 | OK | W07:49 |
| 157 | 566-568 | Hạn chót phải phục hồi (TB theo kịch bản) 58,6 / 35,5 / 13,0 / 6,6 / 6,8 / 2,8 / 1,7%; C luôn 0% | D04 | OK | W07X:22-29; W07:34-39 |
| 158 | 568 | Hai luật phục vụ chênh ≤ 2 lượt ở mọi mức | D04 | OK | W07X:22-29 (lớn nhất 666/664 ở 120 s) |
| 159 | 586-592 | Bảng trần 120, khối không dự báo: 7 hàng × 3 cột (phục vụ, trễ 60/120/300, không trễ 60/120, đi chung) | L1a-02, L1a-04, N-06, N-09 | OK | ADD1:12,17,22,136-138; C120R:14,16,18; STG §2 |
| 160 | 596-599 | Khối có dự báo: trễ 60 s 137/10/65; không trễ 2.297/2.328/2.322; 2.347/2.338/2.379; dài thêm 7,18/7,37/7,27 s | L1a-03, N-16 | OK | ADD1:14,19,24; C120R:15,17,19 |
| 161 | 576-578 | Tiêu đề: phát lại; dự báo chỉ ở 21 kịch bản | C09 | OK | — |
| 162 | 605-606 | Cách đọc: 2.387, 132, 2.255 | N-06 | OK | — |
| 163 | 609-611 | +49 phục vụ, +56 trễ, −7 không trễ 60 s, +39 không trễ 120 s; cao hơn cả hai đầu mút | L1a-09 | OK | ADD1:196-197 (tính lại 2.387−2.338; 132−76; 2.255−2.262; 2.366−2.327) |
| 164 | 611-613 | Có dự báo: 2.322 và 2.379; −6 và +41; 7,27 so với 7,37 s | L1a-03, L1a-09 | OK | ADD1:196 |
| 165 | 616-618 | 9 khách ≥ 90% trần; 0 vượt; 0 phải phục hồi trong 20.435 | N-07, L1a-05 | OK | ADD1:7,108,121 |
| 166 | 621-622 | 2.266 chung, 121 / 72 riêng; 93/121 cũng được U phục vụ | N-10 | OK | ADD1:143,147 (2.266 + 121 = 2.387; 2.266 + 72 = 2.338) |
| 167 | 622-623 | 49 là chênh hai tổng, không phải "49 trong 96" | N-10 | OK | — |
| 168 | 623-625 | 8 giờ 1.001 vs 975, trễ 49 vs 15; 17 giờ 871 vs 852, 20 vs 0 | N-11 | OK | ADD1:155-160 |
| 169 | 625-626 | Theo kịch bản: hơn 23, bằng 8, kém 3 | N-11 | OK | ADD1:162 |
| 170 | 637-653 | Hình (a): C-30 (0,24; 0), C-60 (0,60; 0), C-120 (1,98; 1,15), U (3,24; 2,35); vạch 1.530…1.590, 0…60 | D09 | OK | tính lại: (1.534−1.530)×0,06 = 0,24; 10×0,06 = 0,60; 33×0,06 = 1,98; 54×0,06 = 3,24; 23×0,05 = 1,15; 47×0,05 = 2,35; vạch 20×0,06 = 1,2 |
| 171 | 654-669 | Hình (b): C-30 (0,72; 2,35), C-90 (2,16; 2,50), C-120 (2,88; 2,55), U (2,52; 2,50) | D01, D02 | OK | 2×0,36; 6×0,36; 8×0,36; 7×0,36; 47/50/51/50 × 0,05 |
| 172 | 670-684 | Hình (c): C-30 (0,54; 0,95), C-120 (2,01; 1,65), U (3,42; 2,54) | C01, C06, N-06 | OK | 18×0,03; 67×0,03; 114×0,03; 76/132/203 × 0,0125 = 0,95 / 1,65 / 2,5375 |
| 173 | 686-692 | Chú thích hình: FREE (1.629; 274) ngoài khung; (b) chỉ vẽ mức có trong Bảng | D09 | OK | Ghi chú: CAP:5,8-11 có đủ số cho C-60 (661; 47), C-150/180 (666; 51), C-240/300 (665; 50); nếu registrar thêm dòng thì (b) vẽ được đủ 9 điểm |
| 174 | 701-703 | Cả ba tập: 30 → 120 s thêm phục vụ và thêm trễ; không trễ 60 s +6 / +2 / −7; ở 120 s không kém ở cả ba | D10, D03, L1a-09 | OK | WP17:9,19 (+29 / +23 / +6; 120 s: 1.563 vs 1.534); CAP:4,7 (+6 / +4 / +2; 659 vs 658); ADD1:196 (+49 / +56 / −7; +39) |
| 175 | 704 | Không mức trần nào tốt hơn ở mọi tiêu chí | K36 | OK | — |
| 176 | 704-705 | "mức 120 giây được chọn sau khi xem **các tập phát triển**" | I06, K42 | OVERSTATED | Như #57: phải nói thêm đã xem kết quả U, C-30 và phép sàng lọc 120 s trên chính tập kiểm tra chính (D14, E06, K42, H12) |
| 177 | 705-706 | Một điểm đo thêm, không phải kết quả dò tìm | K36 | OK | — |

### Mục 4.5 Vế cộng dồn (dòng 710–784)

| # | Dòng | Câu / ô (rút gọn) | EV | Kết luận | Sửa / anchor đã mở |
|---|---|---|---|---|---|
| 178 | 713-714 | "98 lần chạy **cũ**" có C trên hệ số đo: 1.256 bản ghi, đều một lần dời vượt trần của chính cấu hình | E01, K09 | LABEL | Số đúng: NEW:1 (`runs 98, records 1256, step_fails 1256, cumulative_only 0`). Nhưng chữ "cũ" trùng với "bộ chạy cũ / bản cũ" của tập tắc đường cố định (Bảng tập thử dòng 128), trong khi 98 lần chạy này dùng **bản lưu trữ có luật phục hồi** (A19, X3-10). Đổi "98 lần chạy đã có trước trần 120 giây" hoặc "98 lần chạy trần 30–300 giây" |
| 179 | 714-715 | 34 lần chạy trần 120 s: 3/524 chỉ vượt khi cộng phần đã dùng | N-08, L1a-06 | OK | ADD1:127; STG §4 |
| 180 | 718-720 | Định nghĩa "chỉ do cộng dồn" | A06, E05 | OK | FJC:42 (51,755 + 80,304 = 132,059 s) |
| 181 | 735 | Bảng: tập chính trần 30 s — 34 / 845 / 0 / 0 | E01, E02 | OK | A:7; NEW:1 |
| 182 | 736 | Buổi sáng 30–300 s — 64 / 411 / 0 / 0 | E01, E02 | OK | A:10-17 (142 + 106 + 71 + 38 + 26 + 18 + 6 + 4 = 411; `repeated` 0 ở cả 8 cấu hình); 64 = 8 × 8 |
| 183 | 738 | Tập chính trần 120 s — 34 / 524 / 3 / 0 | N-08, N-07 | OK | ADD1:108,127 |
| 184 | 740 | Chiều tuyết trần 30 s — 8 / 163 / 0 / 0 | N-26 | OK | SNOW1:10 |
| 185 | 743 | Cộng 140 / 1.943 / 3 / 0 | N-15 | OK | tính lại 34 + 64 + 34 + 8 = 140; 845 + 411 + 524 + 163 = 1.943; DER1:6 |
| 186 | 726-727 | Tiêu đề: "Kiểm toàn bộ bản ghi chặn … **trên các lần chạy có luật C dùng hệ số tắc đường đo**" | N-15 | OVERSTATED | Đọc như mọi lần chạy C trên hệ số đo; thực ra chỉ 140 lần chạy đã kiểm (ADDENDUM-1 mục 0.3; xem #189). Sửa: "…trên 140 lần chạy có luật C dùng hệ số tắc đường đo đã được kiểm" |
| 187 | 749-750 | Cách đọc hàng trần 120 s | N-08, N-07 | OK | — |
| 188 | 753-755 | 132 lần chạy, 1.780 bản ghi (98 với 64.371 quyết định + 34); 140 / 1.943 kể cả tuyết | N-15, E01 | OK | NEW:1 (`acknowledged 64371`); tính lại 20.101 + (5.545 × 3 + 5.540 × 2 + 5.510 + 5.515 + 5.530) = 20.101 + 44.270 = 64.371 (A:7,10-17) |
| 189 | 755-756 | "**15 lần chạy hiệu chỉnh và 16 lần chạy đưa dự báo vào bộ điều phối** chưa được kiểm" | 0.3 | WRONG | Danh sách thiếu: phép quét `tier3-sweep-v1` có các nhánh C-x (x = 30, 60, 120, 300, 600, 900) trên thế giới đo thật W5, 2 kịch bản mỗi nhánh = **12 lần chạy C trên hệ số đo** (SWEEP:13, 66-73; B18), không nằm trong tập đã kiểm (NEW:1 chỉ có t38 và w07; A:3-6 chỉ có tắc đường cố định và tự tạo). Kết luận "không áp cho mọi lần chạy" vẫn đúng. Sửa: "15 lần chạy hiệu chỉnh, 16 lần chạy đưa dự báo vào bộ điều phối và 12 lần chạy C của phép quét trước trên thế giới đo chưa được kiểm" (ADDENDUM-1 mục 0.3 có cùng chỗ thiếu — báo registrar) |
| 190 | 759 | Ba bản ghi ở ba kịch bản khung 8 giờ (14, 15, 18/11), 3 quyết định | L1a-06, N-08 | OK | ADD1:128-130; CW21:2-7 |
| 191 | 760-761 | 25,844 + 99,027 = 124,871 s > 120 s; mỗi phần < 120 s | N-27 | OK | ADD1:128; STG §4 |
| 192 | 761-762 | Khi không trần, chính khách này bị dời hai lần đúng hai lượng ấy | N-27, E07 | OK | ADD1:115-116 (cùng kịch bản, cùng mã yêu cầu `rq-7cfd633530`) |
| 193 | 762-763 | 2 không được nhận dưới 120 s (1 cũng không dưới 30 s), 1 được phục vụ | N-08 | OK | ADD1:128-130; CW21:3,5,7 |
| 194 | 763-765 | Không chứng minh cộng dồn làm mất hai yêu cầu | A23, I08 | OK | — |
| 195 | 768-770 | Tắc đường cố định ghi đủ bản ghi; 2 ở 60 s, 4 ở 120 s; mọi yêu cầu mới vẫn được phục vụ | E03, A23 | OK | NEW:13 (`solverExecutionEvidenceProfile` chỉ ở WP14); FJC:34-45; FJR:2-4. Sổ E03 ghi "có thể chỉ do cộng dồn"; bản nháp gọi là "dấu vết" nên chấp nhận được |
| 196 | 770-771 | Tắc đường tự tạo: 4 bản ghi ở 120 s, 1 yêu cầu bị từ chối | E04 | OK | FJR:5-7 (bỏ bản lặp `-rerun1`: 4 bản ghi, 3 quyết định, 1 từ chối) |
| 197 | 774-775 | "Mỗi lần ≤ 30 s" cho ba lần tổng 90 s; luật C thì không | E08 | OK | — |
| 198 | 775-776 | U: 12/2.434 khách dời từ hai lần | C20 | OK | — |
| 199 | 776-777 | Chấm lại quỹ đạo U: khác ở 4/2.434 tại 120 s, 0 tại 30, 60, 300 s | E06 | OK | CVP:14-18; tôi đếm lại từ 12 khách ở ADD1:115: tại 120 s đúng 4 khách ([25,8; 99,0], [105,5; 99,3], [55,3; 21,7; 67,4], [11,3; 120,0]); tại 30/60/300 s là 0 |
| 200 | 777-779 | Sàng lọc không dự đoán quỹ đạo; luật mỗi lần một trần chưa cài, chưa chạy | E09, K08 | OK | — |
| 201 | 782-783 | Các mục trên giữ nguyên bộ chọn ưu tiên ổn định | H01 | OK | — |

---

## 2. Nhất quán với Chương 3 v3 (tên, ký hiệu, nhãn)

| # | Chỗ | Kết luận | Chi tiết |
|---|---|---|---|
| K-1 | Thuật ngữ "quyết định phải phục hồi" (trên 9 dòng của phần A, gồm Bảng chỉ số, Bảng nghĩa vụ, các dòng 303-317, 456, 566-568, 617) | WRONG (nhất quán) — đã tính ở #50 | Chương 3 v3 dùng "bị ép" trên 15 dòng (bảng thuật ngữ dòng 63; giả mã dòng 204; dòng 378-380; Bảng luat cột "Khi xe bị ép") và GLOSSARY-VI:93 ghi "Giữ 'bị ép', định nghĩa một lần". Phần A không dùng "bị ép" lần nào. Chọn một tên cho cả hai chương |
| K-2 | Dòng 308-310 "theo cấu tạo … luôn qua" | OVERSTATED — đã tính ở #87 | Chương 3 v3 đặt giả thiết (N) và nói tính chất không riêng luật C |
| K-3 | Dòng 158-159 "chỉ lời hứa đầu được thay" | WRONG — đã tính ở #40 | Chương 3 v3 dòng 552-553: "chỉ giờ báo cho khách đổi" |
| K-4 | "98 lần chạy cũ" vs "bộ chạy cũ" | LABEL — đã tính ở #178 | — |
| K-5 | Nhãn chương 3 mà phần A dùng | OK | Đều có trong v3: `muc:kientruc` (616), `muc:bamoc` (234), `muc:luatc` (295), `muc:doichung` (393), `muc:dubao` (484), `bang:rangbuoc` (115), `bang:luat` (404), `eq:so` (593), `nx:giunguyen` (363). Chương 3 v3 trỏ `muc:c4-thietlap` (403), `muc:c4-congdon` (458): phần A định nghĩa cả hai. `muc:c4-dubao`, `muc:c4-hople`, `muc:c4-vaitro` chờ phần B |
| K-6 | Nhãn chưa có ở đâu | (biên dịch) | `muc:c1-cauhoi`, `phuluc:A`, `phuluc:C` chưa được định nghĩa trong `noi-dung/` hay bản nháp nào; `engelhardt2026` chưa có trong TEX10 (khóa mới, metadata X3-40); `schulz2026` có (TEX10:116) |
| K-7 | Ký hiệu $a$, $p_0$, $D_0$, $L_r$, $B$, $x$, $c$, $z$, $q$ | OK | Khớp eq:bamoc, Định nghĩa luatc, eq:so của v3 |
| K-8 | Tập và mức của từng luật (Bảng tập thử vs Bảng luat của v3 dòng 412-427) | OK | C: chính (30, 120), sáng (8 mức), cố định (30, 60, 120), tuyết (30); M⁺: chính (30, 60), sáng (8 mức); V: chính (30); U: chính, sáng, cố định |
| K-9 | −1 ms (dòng 445-446) vs v3 dòng 288-290 | OK | Cùng phạm vi bốn cấu hình, 136 lần chạy |
| K-10 | 0/20.101 và 0/20.435 (v3 dòng 378-380) vs phần A dòng 308, 617 | OK | — |
| K-11 | "kịch bản (scenario)" ghi tiếng Anh ở dòng 58 | (văn phong) | Chương 3 v3 đã dùng "Kịch bản" trong bảng thuật ngữ, không kèm tiếng Anh; nếu theo luật "tiếng Anh một lần ở lần đầu", lần đầu nằm ở Chương 3 |

---

## 3. Dòng `% EV:` và đoạn không có EV

- Đoạn có câu nhưng không có `% EV:` ngay sau: dòng 359-360 (câu dẫn bảng), 414-415 (câu dẫn bảng), 498-499 (có
  dữ kiện "khi thời gian đi không đổi" — EV nằm ở bảng sau, B17), 571-572 (câu dẫn bảng). Không đoạn nào trong số này
  nêu số; chỉ 498-499 nêu một dữ kiện, đã được EV của Bảng tắc đường cố định đỡ.
- EV trỏ tới mã không còn / không phải dòng sổ: `X3-18` (dòng 209) đã bị bỏ (ADDENDUM-2:89) → trỏ TEX08:136-137;
  `R23 #105` (98) → X3-32; `R23 #51` (141) → X3-38; `R23 #57` (229, 569) → X3-28 / X3-41; `RD LR-31`, `RD CX-07`,
  `LR-05`, `CX-08` không phải dòng sổ. Chú thích đầu tệp (dòng 6-7) nói X3 "chưa có trong sổ" — nay đã có ADDENDUM-2.
- EV dòng 146 (bản chạy lại) nên thêm T38:12, 94.
- `LAD:2-6` (dòng 129) là anchor thật nhưng chưa là dòng sổ (NOTES câu hỏi 4) — tôi đã mở và xác nhận (#29).

---

## 4. Tổng hợp

| Nhãn | Số mục (201) |
|---|---:|
| OK (AGREE) | 187 |
| WRONG | 3 (#40, #50, #189) |
| OVERSTATED | 5 (#14, #57, #87, #176, #186) |
| LABEL | 3 (#75, #90, #178) |
| UNSUPPORTED (CANNOT CHECK) | 3 (#9, #16, #124) |

Theo cách chia ba của coordinator: **AGREE 187 / WRONG 11 / CANNOT CHECK 3**. (Mục K-1…K-4 của §2 trùng với các mục
đã đếm; K-6, K-11 là biên dịch / văn phong, không đếm.)

Mọi con số đếm, tỉ lệ, chênh lệch, tọa độ hình và tổng cộng trong 13 bảng và 1 hình đều khớp output gốc; tôi không tìm
thấy con số nào sai. Các lỗi đều nằm ở định nghĩa, phạm vi, nhãn và công bố.

## 5. Mười sửa quan trọng nhất

1. **#50 / K-1 — định nghĩa và tên "quyết định phải phục hồi".** Sai so với mã (X3-30, X3-09): điều kiện là phương án
   giữ nguyên bị loại và có khách được miễn trừ, không phải "loại hết phương án của một xe". Tên lệch Chương 3 v3 và
   GLOSSARY ("bị ép"). Thống nhất tên; sửa định nghĩa ở Bảng chỉ số (và báo người giữ GLOSSARY:93).
2. **#57, #176 — công bố về mức 120 s.** Mức này được chọn sau khi đã xem kết quả U, C-30 và phép sàng lọc ở 120 s
   trên chính tập kiểm tra chính (D14, E06, K42, H12), không chỉ "các tập phát triển".
3. **#189 — phạm vi kiểm vế cộng dồn.** Ngoài 15 lần chạy hiệu chỉnh và 16 lần chạy C-30F, còn 12 lần chạy C-x trên
   thế giới đo W5 của phép quét (SWEEP:13, 66-73) chưa kiểm. Báo cả registrar (ADDENDUM-1 mục 0.3).
4. **#186 — tiêu đề Bảng kiểm bản ghi chặn** đọc như "mọi lần chạy C trên hệ số đo"; ghi "140 lần chạy đã kiểm".
5. **#87 — "đúng theo cấu tạo … luôn qua luật C"** bỏ giả thiết (N); thêm (N) và nói U cũng 0/20.760 bị ép (Chương 3 v3
   dòng 372-375).
6. **#90 — nhãn trung bình theo kịch bản** cho 36,5% / 75,6% / 1,0% / 5,0% ngay sau "Tính gộp"; số gộp là 35,56% /
   75,53% / 0,94% / 4,58% (ADD1:190,192).
7. **#75 — "chờ lâu hơn 0,5 s, ngồi xe ngắn hơn 10,5 s"** là trung bình trên 2.207 khách chung (COM:2-3); thêm
   "trung bình".
8. **#40 — phát lại** thay mọi lời hứa hiển thị, không chỉ lời hứa đầu (X3-11); các chỉ số chỉ dùng $D_0$.
9. **#124 — "đang trên xe"** trong ví dụ 79,0 + 68,3 s không có ở anchor gốc (W07X:54 "khách đang có"); đổi "đã nhận".
   Kèm #123: nói "giờ trả đang hứa đã lùi 79,0 s", không phải khách đã tới muộn.
10. **#14, #16, #9 — Bảng tham số "chung"**: hệ số theo khung 15 phút không đúng cho tập tắc đường cố định; giới hạn bộ
    sinh của bộ chạy cũ chưa kiểm; 108 yêu cầu mỗi kịch bản chưa kiểm cho chiều tuyết. Thu hẹp tiêu đề hoặc ghi ngoại lệ.

Thêm (nhỏ): #178 đổi "98 lần chạy cũ"; §3 cập nhật EV (X3-18 đã bỏ; R23 #… → X3-32 / X3-38 / X3-28).

*Hết. Claude (fact checker), 2026-10-12. Chỉ tạo tệp này.*
