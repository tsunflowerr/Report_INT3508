# EVIDENCE REGISTER — PHỤ LỤC 6: CHƯƠNG 4 PHẦN B, BẢN v8 (2026-10-12)

**Vai trò.** Bổ sung cho `EVIDENCE-REGISTER.md` và các phụ lục 1–4 (không sửa các tệp đó). Ghi các dữ kiện mà
`drafts/09-chuong4-phanB-v8.tex` dùng nhưng sổ chưa có, và các chỗ sửa dòng cũ mà ba bản nhận xét R27/R29 chỉ ra và tôi đã
kiểm lại. Không có phụ lục 5 trong thư mục `evidence/` lúc tôi làm việc; số 6 theo yêu cầu đề bài.

**Cách tôi kiểm (Claude, người sửa Chương 4 phần B, 2026-10-12).**
- Một script chỉ đọc, `evidence/checks-ch4b-v8/ch4b_v8_check.py`, chạy một lần bằng
  `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -I -B`; output mở mode "x":
  `evidence/checks-ch4b-v8/ch4b-v8-check-2026-10-12.txt` (gọi tắt **CK8**), stdout giống hệt output, stderr rỗng, exit 0.
  Script đọc: tệp ô của Họ A (`optimize/test-family-a-causal-no15-2026-10-06-cells.tsv`, gọi tắt **CELLS**), bảng dòng
  của phép thử học máy A1 (`optimize/codex-debate/claude-work/ml-pilot-rows-a1-2026-10-08.tsv`, **MLT**), khung
  `initializeRun` (thứ tự 3) của `transcript-00.ndjson` ở 8 thư mục chiều tuyết (`C:/RideBoundData/research/tier3-forecast-v1`)
  và 51 thư mục `C-30-*` của `C:/RideBoundData/research/tier3-t38-v1`, sha256 của
  `C:/RideBoundData/research/runner-tier3-v2/RideBound.Runner.dll`, và dòng `commitmentRecovery` của
  `tang3/configs/wp4-tier3-v2.json`. Không mô phỏng, không học mô hình, không build, không cài, không xóa.
- Mở trực tiếp (chỉ đọc) các mã và output được trỏ ở cột Anchor; số dòng là số dòng tôi thấy trong phiên này.
- Phép tính một bước ghi nhãn [A].

**Khóa anchor mới.** Đường dẫn tương đối với `E:/Code/Report_INT3508/ridebound-scratchpad/` trừ khi ghi tuyệt đối.

| Khóa | Tệp |
|---|---|
| CK8 | `rewrite-2026-10/evidence/checks-ch4b-v8/ch4b-v8-check-2026-10-12.txt` (script `ch4b_v8_check.py` cùng thư mục) |
| CELLS | `optimize/test-family-a-causal-no15-2026-10-06-cells.tsv` (output đã lưu của `optimize/forecast_family_a.py`, khóa FFA) |
| MLT | `optimize/codex-debate/claude-work/ml-pilot-rows-a1-2026-10-08.tsv` (CSV dù đuôi .tsv) |
| Q4 | `optimize/codex-debate/claude-work/r16-evidence/q4_cost_first_reselect.py` |
| RF | `optimize/run_forecast.py` |
| PFW | `tang3/world/preflight_world_v1_3.py` |
| FNS | `optimize/codex-debate/claude-work/r16-forecast/factor_nowcast_screen.py` |
| RPL | `optimize/codex-debate/claude-work/r16-forecast/rider_nowcast_replay.py` |
| WX | `optimize/codex-debate/codex-work/R16-weather-inventory.txt` |
| R26 | `optimize/codex-debate/codex-work/R26-CH3-OPEN-QUESTIONS-CODEX.md` (Q8, Q9) |
| CMOD | `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/CandidateModels.cs` |

**Ràng buộc chủ sở hữu.** Các tệp nguồn có nhãn "sealed", "predictions", "PASS", "KILL"; tôi chỉ lấy số đo và định nghĩa.

---

## Các dòng mới

| ID | Câu có thể dùng trong luận văn | Số chính xác | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| N4B8-01 | Trên 21 kịch bản ngày thường có dự báo, khách của luật C trần 30 giây tới muộn hơn lời hứa đầu quá 60 giây là 68 khi không dự báo, 22 khi đệm tỉ lệ và 2 khi có dự báo, trong 1.471 khách được phục vụ; theo khung 7 / 8 / 17 giờ là 60 / 17 / 1 trên 444, 8 / 5 / 1 trên 609 và 0 / 0 / 0 trên 418. Khách tới sớm quá 60 giây là 0 / 0 / 1 trên 1.471. | `[đếm]`; trung bình theo kịch bản tính lại 6,0136 / 1,9440 / 0,1693% (khớp FA:8), sớm 0 / 0 / 0,0768% | CK8:4-11; CELLS (cột `served`, `Y_naive`, `Y_pad`, `Y_disp`, `E_naive`, `E_pad`, `E_disp`, hàng `C-30`, ngày 14–16/11); FFA:110-141 (share = số khách / served; `Y_pad`, `E_pad` ở dòng 140-141) | VERIFIED-by-me (script) | Số đếm = share × served từng kịch bản; phần dư lớn nhất 0 (CK8:4,6,8,10). Khớp R27 kiểm chứng §5 và Codex R29 §3.2. Dùng cho Bảng `bang:c4-dubao`. |
| N4B8-02 | Với lời hứa theo dự báo trên cùng 21 kịch bản, luật hạn chót 30 giây giảm từ 66 xuống 2 khách trễ quá 60 giây trên 1.471 khách, luật trần độ dời khách thấy 30 giây từ 66 xuống 2 trên 1.470, điều phối không trần từ 129 xuống 63 trên 1.512; ở khung 17 giờ, điều phối không trần có 28 trên 437 trước và sau dự báo, luật C có 0 trên 418. | `[đếm]`; trung bình theo kịch bản U 9,7156 → 3,8985% (khớp FA:3, REG F08), khung 17 giờ 6,7621% (RX:7) | CK8:10,12,18,20,28 | VERIFIED-by-me (script) | Mẫu số khác nhau giữa các luật (1.471 / 1.470 / 1.512). Thay các tỉ lệ trung bình theo kịch bản ở đoạn "lợi ích không riêng của luật C". |
| N4B8-03 | Trong phép thử học máy ở mức 30 giây: với điều phối không trần, đối chứng (lời hứa theo dự báo cộng đệm đều) có 2 trong 145 khách trễ quá 60 giây ở ngày 15/11, mô hình cây tăng cường có 1; ngày 16/11 cả hai có 1 trong 200. Với luật C trần 30 giây, cả đối chứng lẫn ba mô hình có 0 trong 147 và 0 trong 197. Với ghép tự do trên tập tắc đường cố định ngày 13/11, đối chứng đệm đều có 104 trong 807 khách trễ và 0 tới sớm quá 60 giây; mô hình cây tăng cường có 94 khách trễ và 57 tới sớm; mô hình bỏ hai biến trạng thái xe có 94 khách trễ và 59 tới sớm. | `[gộp theo khách]` trên n khách của ngày kiểm; tỉ lệ in ở MLT với 3 chữ số thập phân | CK8:39-41, 44-46, 49-52, 54-56, 58-61; MLT dòng 4-13 (U), 61-65 (FREE), các dòng C-30 tương ứng; ML:6-7, 14-15, 21 | VERIFIED-by-me (script; suy số đếm từ tỉ lệ 3 chữ số) | Phép suy: k = round(rate × n / 100), chấp nhận khi phần dư ≤ 0,0005 × n / 100 (nhỏ hơn 1 nên k là duy nhất); mọi dòng dùng đều "OK" (phần dư lớn nhất 0,0019 với cận 0,0040 ở n = 807). Codex R29 §3.5 chọn không suy ngược; tôi suy với cận chặt nói trên, xem câu hỏi mở ở NOTES. |
| N4B8-04 | Phép thử học máy dùng một hồ sơ dự báo cố định của ngày 12 và 13/11 (không theo quy tắc ngày nguồn của phần còn lại); mô hình và đối chứng được chỉnh trên tập hiệu chỉnh để độ dài thêm trung bình so với lời hứa không dự báo bằng E (30 giây là mức chính), rồi giữ nguyên khi kiểm; trên ngày kiểm, đối chứng của điều phối không trần dài thêm 37,2 giây (15/11) và 31,8 giây (16/11). Mô hình "bỏ trạng thái xe" bỏ hai biến: số khách khác đã gán cho xe và số khách khác đang trên xe. Các ngày kiểm đã được xem trước. | 37,219 / 31,772 s; cal mean δ 23,13 s | `optimize/codex-debate/claude-work/ML-PILOT-SEALED.md` (MLS):9-10, 19-23, 37-39, 41-61, 63-69, 71-82, 91-95; ML:3,6-7; MLT dòng 5, 10 | VERIFIED-by-me (read) | Bổ sung REG G01–G03 và sửa cách diễn đạt của N4B-08 ("cùng độ dài thêm trung bình 30 giây" là mục tiêu trên tập hiệu chỉnh, không phải độ dài thêm trên ngày kiểm). Phần đệm của mô hình: F = D0 + ρ·max(0, ước lượng) (MLS:74-75). |
| N4B8-05 | Tám lần chạy luật C trần 30 giây của chiều tuyết 15/11/2018 dùng cùng bản bộ chạy đã lưu và cùng cấu hình (kể cả luật phục hồi không tệ hơn) với các lần chạy luật C trần 30 giây của tập kiểm tra chính. | binarySha256 a631038b…5fac; coreCommitSha 1ce15e92…7fb2; policyVersion tier3-exploratory-v1; policyConfigurationHash a2f11a3a…5f1c, ở cả 8 lần chạy tuyết và 51 thư mục C-30 của T3.8; sha256 của `runner-tier3-v2/RideBound.Runner.dll` = binarySha256 | CK8:65-72; R26 Q8 (dòng 253-281: hash cấu hình gắn tệp chính sách và tệp WP4); `tang3/configs/wp4-tier3-v2.json`:7 | VERIFIED-by-me (script) + VERIFIED-by-Codex R26 (phép tính lại hash cấu hình) | Thay lưu ý "bộ chạy chiều tuyết chưa kiểm lại" của X3-10, C4A-06, N-26 và phần A v4 (Bảng `bang:c4-taptu`, dòng 142, 435). 51 thư mục = 34 kịch bản kiểm tra + 15 hiệu chỉnh + 2 bản lỗi gốc (ADDENDUM-1 mục 0.3); cả 51 cùng một bộ năm giá trị. Tôi không tự tính lại hash cấu hình; sự trùng của giá trị đã ghi đủ cho câu "cùng cấu hình". |
| N4B8-06 | Trong phép thử đưa dự báo vào bộ điều phối, thời gian đi gửi cho bộ điều phối ở khung b được nhân với trung bình hệ số dự báo của khung b và khung kế tiếp chia cho hệ số của khung b (K = 2). Luật C hoàn tất 14 lần chạy, luật hạn chót 15; 47,6% và 62,8% là trung bình trên cùng 15 kịch bản của luật hạn chót. | K = 2; `horizonBins: 2` | RF:9, 72; `optimize/configs/forecast-k2-2018-11-14.json`:1 (và 15, 16); PFW:85-89; FR:117 ("K = 2"), 123 (15 ô Mplus-30F chạy xong), 137 (14 ô C-30F chạy xong); RX:11-12; R26 Q9 | VERIFIED-by-me (read) + VERIFIED-by-Codex R26 | Thay lưu ý "giá trị K chưa kiểm" của X3-29. Lần dừng: 1,67 s và 2,69 s (RX:13-15), đều dưới 3 giây. |
| N4B8-07 | Phép phát lại chiều tuyết tách số giây trễ theo cách cộng có giới hạn: phần được giải thích của mỗi khách là phần kéo dài của lời hứa, chặn trong khoảng từ 0 tới phần trễ còn lại sau khi trừ phần tính cho điều phối. Với cách trộn có buổi sáng, phần vượt bị chặn là 6 giây; với hồ sơ lịch sử là 0, nên ở hồ sơ lịch sử cách cộng này trùng phần có dấu của công thức sổ. | explained = Σ max(0, min(D − P0, A − P0 − dispatch)) | RPL:14-15, 113-114; RP1:26 (HIST overshoot 0), 29 (BLEND-pre overshoot 6) | VERIFIED-by-me (code read) | Bổ sung REG F15: 886,9 s (25,7%) và 2.299,0 s (66,7%) là số của cách cộng có giới hạn. Theo Codex R29 §2.3, phần có dấu sẽ cho 893,3 s / 25,9% và 2.292,6 s / 66,5%; tôi không tính lại các số đó và bản v8 không in chúng. |
| N4B8-08 | (Sửa N4B-03.) Tỉ lệ tới sớm quá 60 giây của đệm tỉ lệ có được tính và lưu: 0 trên 1.471 khách ở 21 kịch bản (0% trung bình theo kịch bản). | 0 / 1.471 | FFA:139-141 (`E_pad`); CELLS cột 5; CK8:4-5 | VERIFIED-by-me (code read + script) | Câu "phép đệm không tính chỉ số này" của N4B-03 và ô "chưa đo" của v7 là sai. |
| N4B8-09 | Ở mọi cách hứa của bảng chiều tuyết (không dự báo, hồ sơ lịch sử, ba cách trộn, đệm tỉ lệ, hệ số thật), không khách nào tới sớm quá 60 giây. | E60 0,00% trung bình theo kịch bản ở mọi hàng ⇒ 0 khách ở mọi kịch bản [A] | RP1:7-8, 10-12, 17-18 | VERIFIED-by-me (read) | Một trung bình không âm bằng 0 chỉ khi mọi kịch bản bằng 0. Thay cho cột "tới sớm" mà giảng viên R27 §2.1 đề nghị. |
| N4B8-10 | Phép sàng lọc giải lại bài toán chọn bằng một chương trình viết riêng (quy hoạch động chính xác trên các phương án và giá trị tiêu chí đã ghi, không phải bộ giải của bộ chạy); với thứ tự gốc nó cho đúng mọi lựa chọn đã ghi của năm cấu hình (62.837). Trong thứ tự ưu tiên chi phí, các mức số phương án bị ép, số yêu cầu được nhận, chi phí kế hoạch và thứ hạng mã được giữ, còn mức dùng trần và mọi mức phần dời bị bỏ; vì số yêu cầu được nhận đứng trước các mức bị bỏ trong cả hai thứ tự, số yêu cầu được nhận không đổi theo cách đặt thứ tự. | 12.663 + 12.525 + 12.364 + 12.325 + 12.960 = 62.837 [A]; accepted_changes 0 ở mọi cấu hình | Q4:10-19 (bước 1 giải lại đủ mọi mức rồi so `selectedCandidateIds`, bước 2 thứ tự ưu tiên chi phí), 128-142; PV:1-7 (`validation_match`, `accepted_changes` 0); NEW:7 | VERIFIED-by-me (code read + read) | Sửa anchor của câu 62.837 (trước trỏ WPCHK, vốn chỉ kiểm điều kiện cần, WPCHK:12-15). Cùng mã Q4 chạy hai lần (Claude R16, Codex R17), không phải hai bản cài đặt độc lập (REG H03 lưu ý). |
| N4B8-11 | (Sửa REG F09, chỉ phép cộng.) Sổ ngày thường của 68 khách: 81,742 + 5.352,646 + 783,018 = 6.217,406 giây; tổng của ba số đã làm tròn một chữ số (81,7 + 5.352,6 + 783,0) là 6.217,3, khác 6.217,4 do làm tròn độc lập. | 6.217,406 s | FA:30; CELLS (cột `ledger_*`, C-30, 21 kịch bản), theo Codex R29 §3.3 | VERIFIED-by-me (read FA:30) | Nhãn trên hình (82 / 5.353 / 783 s; 6.217 s) không đổi; chỉ dòng EV và F09 sửa. |
| N4B8-12 | Ở chiều tuyết, phần tính cho điều phối là 0,25% số giây trễ của 41 khách. | 8,566 / 3.445,933 = 0,2486% [A] | NEW:5 (qua N4B-05) | [A] | Nhãn mới trên thanh tuyết của hình `hinh:c4-so`. |
| N4B8-13 | (Thu hẹp REG K34.) Các bộ đếm đã đọc chỉ cho biết: ở 34 lần chạy mỗi cấu hình (không trần, trần 30 và 120 giây, luật hạn chót 30 giây), không phương án nào bị bỏ vì giới hạn 100 phương án mỗi xe hay giới hạn khối lượng khám phá, và giới hạn 2 yêu cầu mới mỗi lượt để lại tổng 1 yêu cầu ở mỗi cấu hình. Chúng không đo giới hạn của bước kiểm, của bộ giải, bộ đếm `OmittedRepairRequestCount` hay bất kỳ bộ đếm nào ở tập tắc đường cố định, nên không cho phép câu "chênh lệch phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán". | 1 / 0 / 0 mỗi cấu hình (N-25) | ADD1:119-122; CMOD:68-82, 100-118 (`IsComplete` gồm cả `OmittedRepairRequestCount`); GEN:236-246, 298-345; C4A-18 | VERIFIED-by-me (code read) | Theo Codex R29 §2.4 và kiểm chứng R27 B127, B130. Không thêm số mới. |

## Dòng cũ cần sửa (tôi không sửa các tệp đó)

| Dòng | Sửa |
|---|---|
| N4B-01 | Phép tái lập 62.837 dựa vào Q4/PV (giải lại đủ thứ tự), không phải WPCHK; xem N4B8-10. |
| N4B-03 | Bỏ vế "phép đệm không tính chỉ số này"; xem N4B8-08. |
| N4B-07 | Tỉ lệ phá lời hứa của luật hạn chót ở khung 8 giờ là 8,4% (Codex R29 §3.4, từ BI độ chính xác đầy đủ 8,357825%), không phải 8,3% (RX làm tròn từng ô trước khi lấy trung bình). Bản v8 không in số này. Thêm K = 2 (N4B8-06) và số lần chạy hoàn tất 14 / 15. |
| N4B-08 | "Cùng độ dài thêm trung bình 30 giây" là mục tiêu trên tập hiệu chỉnh; bỏ hai biến trạng thái xe, không phải một; xem N4B8-04. |
| F09 | Phép cộng làm tròn; xem N4B8-11. |
| F15 | Ghi rõ cách cộng có giới hạn; xem N4B8-07. |
| X3-10, C4A-06, N-26 | Bộ chạy chiều tuyết đã kiểm: xem N4B8-05. |
| X3-29 | K = 2: xem N4B8-06. |
| K34 | Thu hẹp như N4B8-13. |

## Tổng hợp

| Nhóm | Số dòng | VERIFIED-by-me (script) | VERIFIED-by-me (read / code read) | [A] |
|---|---:|---:|---:|---:|
| N4B8-01…N4B8-13 | 13 | 5 (01, 02, 03, 05, 08 một phần) | 7 (04, 06, 07, 09, 10, 11, 13) | 1 (12) |

*Hết phụ lục 6. Viết bởi Claude (người sửa Chương 4 phần B), 2026-10-12. Chỉ tạo tệp này và thư mục
`evidence/checks-ch4b-v8/`.*
