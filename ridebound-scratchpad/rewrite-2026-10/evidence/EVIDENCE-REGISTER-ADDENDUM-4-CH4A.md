# EVIDENCE REGISTER — PHỤ LỤC 4: CHƯƠNG 4 PHẦN A (2026-10-12)

**Vai trò.** Bổ sung cho `EVIDENCE-REGISTER.md`, `EVIDENCE-REGISTER-ADDENDUM-1.md` và `EVIDENCE-REGISTER-ADDENDUM-2-CH3.md`
(không sửa các tệp đó). Ghi các dữ kiện mà `drafts/08-chuong4-phanA-v4.tex` dùng nhưng sổ chưa có, và các chỗ sổ cũ
đặt nhãn lệch (D13, D19, GLOSSARY-VI:93). Mã C4A-xx. (Phụ lục 3 dành cho phần B của Chương 4.)

**Cách tôi kiểm (Claude, người sửa Chương 4 phần A, 2026-10-12).**
- Ba script chỉ đọc mới, lưu ở `evidence/checks-ch4a-v2/` (khóa **CK4A**), chạy bằng
  `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B -I`, mọi output mở mode "x", stderr rỗng:
  - `check_ch4a_v2.py` → `check-ch4a-v2-2026-10-12.txt`: trễ so với lời hứa đầu ở các ngưỡng 30/60/120/300 s cho U,
    C-30, M⁺-30, M⁺-60, V-30 trên 34 kịch bản chính, đọc bộ trích xuất độc lập `tang3/t38/independent/cache/` (IVC); bộ
    đọc thứ hai là TSV theo khách của Claude Giai đoạn 1a (`r21-stage1a/stage1a-2026-10-10-riders.tsv`). 32 phép đối
    chiếu với số đã có trong sổ (C01, C06, C07, N-21, C13, N-06): **0 FAIL**.
  - `ledger_share_sums.py` → `ledger-share-sums-2026-10-12.txt`: tử số, mẫu số của tỉ lệ "phần tính cho điều phối";
    3/3 tỉ lệ khớp C24, N-23.
  - `fixed_shared_counts.py` → `fixed-shared-counts-2026-10-12.txt`: số khách đi chung chính xác trên tập tắc đường cố
    định, đọc 80 transcript ở `E:/RideBoundData/wp14r/development-v6-ledger/` (kiểm mã băm từng khung như
    `audit_vep.read_frames`), cùng quy tắc với `wp14r_ladder_reanalysis.py` dòng 32-39; 5/5 cấu hình khớp số phục vụ và
    tỉ lệ đã in ở LAD.
- Các dòng còn lại: tôi mở trực tiếp, chỉ đọc, đúng dòng được trỏ trong phiên này.
- Không chạy mô phỏng, không build, không cài, không xóa; chỉ tạo tệp này và thư mục `checks-ch4a-v2/`.

**Nhãn.** Như sổ chính và phụ lục 1: **VERIFIED-by-me (script)**, **VERIFIED-by-me (read)**, **UNVERIFIED**; nhãn mẫu số
`[gộp theo khách]`, `[TB theo kịch bản]`, `[trên yêu cầu]`, `[đếm]`.

## Khóa anchor mới

Đường dẫn tương đối với `E:/Code/Report_INT3508/ridebound-scratchpad/` trừ khi ghi tuyệt đối. Các khóa khác (A, NEW, CAP,
DIAL17, WBU, CVP, CON, INV, SWEEP, W07X, W07XM, BUD, FJC, FJR, T38, C120R, ADD1, TEX08, RS, VALID, HVA, POL) như sổ chính
và hai phụ lục trước.

| Khóa | Tệp |
|---|---|
| CK4A | `rewrite-2026-10/evidence/checks-ch4a-v2/` (ba script và ba output kể trên) |
| BUDPY | `optimize/codex-debate/claude-work/budget_block_diagnosis.py` |
| IVC | `tang3/t38/independent/cache/<cấu hình>-<kịch bản>[-rerun1].json`; bộ phân tích `tang3/t38/independent/iv_analyze.py` |
| TSV | `optimize/codex-debate/claude-work/r21-stage1a/stage1a-2026-10-10-riders.tsv` |
| RW7 / RW7X | `tang3/w07/run_w07.py` / `tang3/w07x/run_w07x.py` |
| RSP | `C:/Code/RideBound-noworse/src/RideBound.Application/Scheduling/RouteScheduleProjector.cs` |

---

## C4A. Dữ kiện cho Chương 4 phần A

| ID | Câu có thể dùng trong luận văn | Số chính xác | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| C4A-01 | Đo bằng thước của luật hạn chót (tới muộn hơn lời hứa đầu không dự báo quá 30 giây), luật C trần 30 giây có 292 trong 2.338 khách được phục vụ, gần bằng 289 khách của luật hạn chót 30 giây. | C-30: 292 / 2.338 = 12,49% `[gộp theo khách]`, 14,59% `[TB theo kịch bản]`, 28/34 kịch bản; M⁺-30: 289 / 2.338 = 12,36%, 14,48%, 28/34 (tái lập N-21); U: 428 / 2.434 = 17,58%, 19,61%, 34/34; M⁺-60: 302 / 2.347; V-30: 289 / 2.336; C-120 (TSV): 355 / 2.387 | CK4A check (mục U, C-30, Mplus-30 và các dòng đối chiếu); ADD1:12,17,22,27 (cột late30: 428, 292, 355, 289) | VERIFIED-by-me (script; hai bộ đọc IVC và TSV khớp; khớp cột late30 của ADD1) | Cùng quy tắc "phá lời hứa" của luật hạn chót: khách được phục vụ có A − p₀ > 30.000 ms, mẫu số là khách được phục vụ (`iv_analyze.py` mục 6; `sweep_analyze.py`:107,128-132). Hai tập khách khác nhau 6 khách mỗi bên (C04). Số mới so với sổ: C-30, U, M⁺-60, V-30 ở ngưỡng 30 s. |
| C4A-02 | Trên tập kiểm tra chính, luật hạn chót 60 giây có 79 lượt trễ quá một phút, luật trần độ dời khách thấy 30 giây có 74. | M⁺-60: trễ quá 60 / 120 s 79 / 11; không trễ quá 60 / 120 s 2.268 / 2.336 `[trên yêu cầu]`; V-30: 74 / 11; 2.262 / 2.325 | CK4A check (mục Mplus-60, V-30); EXP:5-6 (trễ quá 60 s 79, 74) | VERIFIED-by-me (script; khớp EXP và số Codex R25 §3 tính độc lập) | Khách đi chung của hai cấu hình này chưa đếm chính xác (EXP:5-6 chỉ có 14,1% / 12,9% làm tròn), nên bảng ghi "chưa đếm". |
| C4A-03 | Tỉ lệ "phần tính cho điều phối" trong số giây trễ của khách trễ quá 60 giây là tổng có dấu của các lần dời do điều phối chia cho tổng số giây trễ của chính nhóm khách đó. | U: 23.027,239 / 31.353,407 s (73,4%; 203 khách); C-30: 81,742 / 6.891,526 s (1,2%; 76); C-120: 4.836,281 / 12.450,223 s (38,8%; 132) | CK4A ledger-share-sums (3/3 OK so với C24, N-23) | VERIFIED-by-me (script, bộ đọc TSV; cùng số với Codex R25 §3) | Định nghĩa như `recompute_addendum_1.py` (`ledger_dispatch_share_late60`) và công thức eq:so của Chương 3; q = Σc có dấu, không phải Σ\|c\|. |
| C4A-04 | Trên tập tắc đường cố định, số khách đi chung là 865 / 346 / 303 / 266 / 241 và số khách bị điều phối dời giờ trả là 388 / 62 / 41 / 20 / 6 với ghép tự do, điều phối không trần, trần 120, 60 và 30 giây. | Đi chung trên phục vụ 1.629 / 1.584 / 1.563 / 1.540 / 1.534: 53,1 / 21,8 / 19,4 / 17,3 / 15,7% `[gộp theo khách]`; bị dời 23,8 / 3,9 / 2,6 / 1,3 / 0,4% | CK4A fixed-shared-counts (đi chung, 5/5 OK so với LAD:2-6); WBU:4,7,10,13,16 (bị dời); CVP:4,9 và A:3-5 (cùng số bị dời) | VERIFIED-by-me (script cho đi chung; read cho bị dời) | Tử số chính xác cho các tỉ lệ làm tròn của D08 (Codex R25 §3 và §5.7 đòi số đếm). Bộ chạy cũ (B17, I12). |
| C4A-05 | Trên tập chỉnh trần buổi sáng, trần 60 giây phục vụ 661 lượt; trần 150 và 180 giây cho đúng các số của trần 120 giây; trần 240 và 300 giây cho đúng các số của điều phối không trần. | C-60: 661 / 47 / 614 / 659; C-150 = C-180 = C-120: 666 / 51 / 615 / 659; C-240 = C-300 = U: 665 / 50 / 615 / 656 (phục vụ / trễ quá 60 s / không trễ quá 60 s / không trễ quá 120 s, trên 864 yêu cầu) | CAP:5,7-11; DIAL17:5,7-11 | VERIFIED-by-me (read; hai bộ đọc độc lập khớp) | Mở rộng D02 (vốn chỉ có U, C-30, C-90, C-120). Dự báo không hoạt động ở 12–13/11 (CAP:2). |
| C4A-06 | Mỗi kịch bản chiều tuyết có 108 yêu cầu, tổng 864 yêu cầu; 601 khách được nhận. | 8 × 108 = 864; được nhận 86 + 75 + 74 + 66 + 80 + 85 + 75 + 60 = 601 | INV:14-15,17-22 (cột requests {108: 1} cho mỗi thư mục C-30-d20181115-s10-r{1..4}-w{14,15}) | VERIFIED-by-me (read) | Khép FC #9 (R25). Bộ chạy của tập này vẫn chưa kiểm (X3-10). |
| C4A-07 | Ở tập chỉnh trần buổi sáng, các cấu hình được so trong chương (điều phối không trần, luật C và luật hạn chót ở tám mức) ứng với 136 trong 192 lần chạy đã lưu. | 17 cấu hình × 8 kịch bản = 136; 88 + 104 = 192; 56 lần còn lại là V-30, M-30 (w07) và V-90, V-120, V-150, V-180, V-240 (w07x) | RW7:5,33-34; RW7X:3-5,35-36; B15; B16 | VERIFIED-by-me (read) | Codex R25 thay đổi 5. |
| C4A-08 | Phép quét trước đó (tier3-sweep-v1) có 12 lần chạy luật C dùng hệ số đo được chưa nằm trong tập đã kiểm bản ghi chặn; các bản ghi chỉ do cộng dồn trên "kiểu tắc đường tự tạo" cũng thuộc phép quét này. | C-x, x = 30, 60, 120, 300, 600, 900 s, trên thế giới đo thật W5, 2 kịch bản: 6 × 2 = 12; thế giới tự tạo C-120: 13 lần chạy kể cả một bản lặp | SWEEP:8-14,67-73; NEW:1 (`by_arm` chỉ có t38 và w07); FJC:46-54; FJR:5-7 | VERIFIED-by-me (read) | Khép FC #189. Phép quét dùng bộ chạy `runner-tier3-v1` (SWEEP:14). ADDENDUM-1 mục 0.3 thiếu 12 lần chạy này. |
| C4A-09 | Trong phép phân tích các yêu cầu bị từ chối dưới trần 30 giây: "mức vượt" là phần vượt quá 30 giây; nhóm 1.186 yêu cầu là nhóm không có bản ghi chặn do trần được ghi, không phải nhóm đã chứng minh chỉ có lý do cấu trúc; "2 trong 148" đếm theo bản ghi có mức vượt nhỏ nhất của từng yêu cầu. | mức vượt = max(after − limit) trên các bản ghi chặn của phương án; limit = 30.000 ms nên trung vị 109,6 s ứng với tổng dời ≈ 139,6 s; 2/148 = số yêu cầu có bản ghi được chọn mang một khách với `before` > 0 | BUDPY:1-7,22,29-44,49-52; BUD:2-10 | VERIFIED-by-me (read mã) | Sửa nhãn D13 ("chỉ có lý do cấu trúc") và D19 ("khách chặn") của sổ chính. Xác nhận phỏng đoán của người đọc R25 (D47, G6.8b): 109,6 s là phần vượt, không phải cả lần dời. |
| C4A-10 | Một quyết định bị ép khi có ít nhất một xe bị ép: luật lời hứa đã loại cả phương án giữ nguyên kế hoạch của xe, và xe đi theo phương án được giữ nhờ luật phục hồi, có ít nhất một khách được miễn trừ; điều này không đòi mọi phương án khác bị loại. | — | RS:1012-1027 (chứng chỉ `normalOperation` = không có witness miễn trừ), RS:1097-1108; VALID:141-145 ("a decision with any exemption is not normal operation"); HVA:244-300; POL:443-463 (`SelectedForcedVehicles`) | VERIFIED-by-me (read mã) | Thay định nghĩa "loại hết phương án của một xe" của GLOSSARY-VI:93 (xem `style/GLOSSARY-VI-v2.md`). Cùng nội dung X3-30, X3-09. |
| C4A-11 | Mức thử 120 giây trên tập kiểm tra chính được chọn sau khi đã xem kết quả của điều phối không trần và luật C trần 30 giây trên chính tập này, kể cả các phép sàng lọc ở 120 giây. | tập chính chạy 1–2/10/2026 (T38:5); sàng lọc bản ghi chặn ở 120 s trên C-30 của tập chính, tệp ngày 07/10 (BUD:8, D14); sàng lọc cộng dồn với mỗi lần ở 120 s trên U của tập chính, tệp ngày 10/10 (CVP:14-18, E06); trần 120 giây chạy 10/10, 22:12–23:48 (C120R:10) | T38:5; BUD; CVP:14-18; C120R:10; K42 | VERIFIED-by-me (read) | Khép FC #57, #176. Chỉ viết bằng lời "dùng lại dữ liệu đã xem"; không trỏ tới văn bản kế hoạch (luật của chủ sở hữu). |
| C4A-12 | Trong ví dụ cơ chế trên tập buổi sáng, 79,0 giây là độ lùi của giờ trả đang hứa so với lời hứa đầu, không phải độ trễ đã xảy ra; giai đoạn của khách (chờ đón hay trên xe) không được ghi. | trước quyết định: Σx = 79,0 s, Σc = 0, p_cuối − p_đầu = 79,0 s; quyết định: x = 0,1 s, c = 68,3 s; 79,0 + 0,1 + 68,3 = 147,4 s | W07XM:2-16; W07X:48-62 ("khách đang có") | VERIFIED-by-me (read) | Khép FC #123, #124 và Codex R25 thay đổi 6. |
| C4A-13 | Với lời hứa đầu không dự báo, số lượt tới sớm quá 60 giây trên tập chính là 7 khi không trần, 3 với trần 30 giây và 1 với trần 120 giây. | U 7 / 2.434; C-30 3 / 2.338; C-120 1 / 2.387; M⁺-30 3 / 2.338 `[đếm]` | ADD1:12,17,22,27 (cột early60); C120R:14,16,18; DIAL17:12-13 | VERIFIED-by-me (read; ba output khớp) | Số có dự báo 8 / 4 / 2 là N-03, N-16, N-06. |
| C4A-14 | Lượt trễ nhất so với lời hứa đầu muộn 660,1 giây khi không trần và 232,3 giây với trần 30 giây. | +660,1 s; +232,3 s | CON:4,11 | VERIFIED-by-me (read) | Dạng giây của C26 ("11 phút", "3,87 phút"); trả lời người đọc D38 về độ chính xác. |
| C4A-15 | Ở tập kịch bản tĩnh của đợt thử trước, cấu hình có trần dùng trần 30 giây cho tổng độ dời giờ trả. | 30 s | TEX08:136-137 ("Cấu hình C1 là cấu hình cam kết đầy đủ: trần 30 giây cho tổng độ dời giờ trả, khóa cứng xe và hai điểm dừng, giờ đón cố định từ lúc xác nhận") | VERIFIED-by-me (read, chỉ đọc thư mục luận văn) | Thay X3-18 đã bỏ khỏi phụ lục 2 (FC #53). C1 là cả gói cam kết, không chỉ trần (K33). |
| C4A-16 | (không dùng; để trống giữ thứ tự mã) | — | — | — | — |
| C4A-17 | Ở đợt chạy tập chính, hai lần chạy hỏng vì lỗi hạ tầng được chạy lại một lần, một ở tập hiệu chỉnh và một ở tập kiểm tra chính; phân tích dùng bản chạy lại. | 2; bản dùng: `C-30-d20181114-s10-r3-w17-rerun1` (tập kiểm tra) | T38:12, 94; ADD1:6; ADDENDUM-1 mục 0.3 | VERIFIED-by-me (read) | Trả lời người đọc D15. |
| C4A-18 | Tập tắc đường cố định chạy bằng bộ chạy và cấu hình khác tập chính; giới hạn bộ sinh và bộ giải của bộ chạy đó chưa được kiểm lại. | khác biệt cấu hình: không có `commitmentRecovery`, không có `lateBoarding`, `policyVersion` wp14-development-v1, `solverExecution.skipConstantObjectiveLevels`, `solverExecutionEvidenceProfile` ghi đủ bản ghi | NEW:13 | VERIFIED-by-me (read) | Khép FC #14, #16: chú thích Bảng tham số ghi ngoại lệ thay vì nói "chung". |
| C4A-19 | Nguyên nhân của các lần dời sớm đúng 1 mili giây: chưa kiểm. | — | RSP:56-150 (phần còn lại của cạnh đang đi được làm tròn lên như nhau cho e và p; thời gian mỗi cung là số nguyên mili giây); ADDENDUM-1 mục 0.2 | UNVERIFIED (nguyên nhân) | Giả thuyết khả dĩ: làm tròn mili giây trên từng cung của bao đóng 96 nút có thể làm bất đẳng thức tam giác lệch 1 ms; chưa kiểm trên bốn trường hợp. Luận văn giữ "đúng 1 mili giây", không nêu nguyên nhân (người đọc D42, G6.8c). |
| C4A-20 | Bản kiểm kê ngày 08/10/2026 ghi 1.991 bản ghi lần chạy. | 1.991 | INV:1 (tệp `data-inventory-summary-2026-10-08.txt`) | VERIFIED-by-me (read) | Codex R25 thay đổi 9: ghi ngày; con số hiện tại của kho (sau 34 lần chạy trần 120 giây) chưa kiểm kê lại. |

## Dòng của sổ cũ cần cập nhật (tôi KHÔNG sửa các tệp đó)

- **D13** → bỏ chữ "chỉ có lý do cấu trúc" cho nhóm 1.186; viết "không có bản ghi chặn do trần được ghi" (C4A-09).
- **D19** → "2/148 bản ghi được chọn (một bản ghi mỗi yêu cầu)", không phải "2/148 khách chặn" (C4A-09).
- **A24** → "2 yêu cầu mới mỗi lượt (cho cả lô)", không phải "mỗi xe" (X3-32; Codex R25 §7).
- **ADDENDUM-1 mục 0.3** → thêm 12 lần chạy luật C của phép quét trên thế giới đo thật W5 vào danh sách chưa kiểm (C4A-08).
- **GLOSSARY-VI:93** → định nghĩa "bị ép" theo C4A-10 (bản sửa ở `style/GLOSSARY-VI-v2.md`).
- **D04** → các tỉ lệ bị ép của luật hạn chót không đơn điệu (6,6% ở 120 s, 6,8% ở 150 s); chỉ viết "giảm từ … xuống …".

## Tổng hợp

| Mục | Số dòng | VERIFIED-by-me (script) | VERIFIED-by-me (read) | UNVERIFIED | Để trống |
|---|---:|---:|---:|---:|---:|
| C4A | 20 | 4 (C4A-01, -02, -03, -04 phần đi chung) | 14 | 1 (C4A-19) | 1 (C4A-16) |

*Hết phụ lục 4. Viết bởi Claude (người sửa Chương 4 phần A), 2026-10-12. Chỉ tạo tệp này và thư mục `checks-ch4a-v2/`.*
