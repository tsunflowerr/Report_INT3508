# CH4B — Nhật ký sửa Chương 4 phần B (mục 4.6–4.11) theo ba bản nhận xét của v7 (2026-10-12/13)

**Bản cuối dùng để ghép: `drafts/09-chuong4-phanB-v10.tex`.**
- `-v8.tex`: lượt sửa đầu; năm anchor FR trong dòng `% EV` lệch một dòng. Không dùng.
- `-v9.tex`: v8 với năm anchor đã sửa; chữ in ra giống hệt v8 (đã `diff` sau khi bỏ dòng `%`). Không dùng.
- `-v10.tex`: v9 cộng sáu chỗ sửa lời (B7, B48, B60, B83, B84 và "trên cùng 15 kịch bản"). **Bản ghép.**
- Ghi chú: `drafts/09-chuong4-phanB-v8-NOTES.md` — tên giữ theo yêu cầu đầu ra, **nội dung mô tả v10** (mục 0, độ dài
  3.483 tiếng ở mục 1, 11 nhãn ở mục 2), nên không tạo thêm `-v10-NOTES.md`.
- Sổ mới: `evidence/EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md` (N4B8-01…13) và `evidence/checks-ch4b-v8/` (script chỉ đọc
  `ch4b_v8_check.py`, output **CK8** `ch4b-v8-check-2026-10-12.txt`, errata hai anchor FR của N4B8-06).

**Đầu vào.** Bản v7 (488 dòng). Ba bản nhận xét: Codex `optimize/codex-debate/codex-work/R29-CH4B-REVIEW-CODEX.md` (**CX**),
kiểm chứng sự kiện `reviews/R27-FACTCHECK-CH4B-CLAUDE.md` (**FC**), người đọc và giảng viên
`reviews/R27-READER-LECTURER-CH4B-CLAUDE.md` (**RL**). Thêm hai sự kiện của Codex R26 (Q8 bộ chạy chiều tuyết, Q9 K = 2).

**Cách kiểm.** Không nhận một nhận xét chỉ vì người nhận xét nói vậy. Với mỗi nhận xét có tính sự kiện, tôi mở mã, script và
output được trỏ (chỉ đọc), hoặc đếm lại bằng script chỉ đọc CK8. **QĐ:** **A** = nhận; **M** = nhận có sửa (lý do kèm);
**R** = không nhận (lý do và anchor kèm); **CC** = không kiểm được. "Dòng" là dòng của v7; "Thay đổi" chỉ chỗ trong v10.
Không mô phỏng, build, cài, xóa; không ghi vào thư mục luận văn, `E:/Code/RideBound*` hay `C:/Code/*`.

---

## 1. Chỗ bất đồng và cách giải bằng bằng chứng

| # | Vấn đề | Ý kiến | Bằng chứng tôi kiểm | Kết luận |
|---|---|---|---|---|
| D1 | Tỉ lệ tới sớm của cách đệm tỉ lệ ở Bảng `bang:c4-dubao` | RL S2, B-§2.1, 2.3: "chưa được đo" (thêm vào hạn chế); FC B33, CX §2.2: đã đo, bằng 0 | `forecast_family_a.py:139-141` tính `E_pad`; CELLS lưu cột `E_pad` (cột 5); CK8:4-5: 0 khách trên 1.471, phần dư 0 | **Đã đo, 0 trên 1.471.** Ô "chưa đo" sửa thành 0; mọi đề nghị ghi "chưa đo" bị bác (N4B8-08). |
| D2 | Mức 120 giây được chọn khi nào | v7 4.11: "sau khi xem dữ liệu phát triển"; phần A v4 dòng 229-232: sau khi xem kết quả U và C-30 trên chính tập kiểm tra chính; RL M2 | `08-chuong4-phanA-v4.tex:229-232`; C4A-11; I06 | Theo phần A v4, chỉ dùng lời "dùng lại dữ liệu đã xem"; không nhắc kế hoạch hay dự đoán. |
| D3 | Câu bộ đếm tính toán ở 4.10 | RL M3 đề nghị "chênh lệch … không đến từ các giới hạn tính toán này"; FC B127/B130 "các giới hạn của bộ sinh đã kiểm"; CX §2.4: các bộ đếm không đo tác động lên kết quả | ADD1:119-122 (1 / 0 / 0 mỗi cấu hình); `CandidateModels.cs:100-118` (`IsComplete` còn gồm `OmittedRepairRequestCount`, chưa được đếm); GEN:298-345 | Theo CX: chỉ nói điều bộ đếm ghi nhận; bỏ mọi câu kết luận về nguồn gốc chênh lệch (cả câu của RL M3 vẫn là kết luận nhân quả). |
| D4 | Đoạn tiêu chí 3 (mức dùng trần 100%) nên ở 4.6 hay 4.10 | RL B73, S4, giảng viên 2.2 ý 7: chuyển lên 4.6 | `07-chuong3-v3.tex:467-468` trỏ `muc:c4-hople` để báo các số này | Giữ ở 4.10 (một câu, trỏ `muc:doichung`); chuyển đi thì chương 3 trỏ sai. |
| D5 | Tên của đệm theo tỉ lệ | v7 "đệm cùng giá"; RL S2 "đệm cùng độ dài" | Bảng thuật ngữ v2 mục B: "đệm" là cộng một khoảng cố định; FFA:15-17 (tỉ lệ k_w (P0 − t0)) | Đặt tên **đệm tỉ lệ**: nói đúng cách làm, tránh ẩn dụ "giá", không trùng "đệm đều". |
| D6 | Số đếm sau phép thử học máy | RL B42 tính ngược 104 / 94 / 57 từ tỉ lệ in; CX §3.5 chọn không suy ngược | MLT lưu tỉ lệ 3 chữ số; với n = 807, cận làm tròn 0,0040 khách < 1 nên số đếm duy nhất; CK8:58-61 (phần dư 0,0019 / 0,0006 / 0,0016) | Dùng số đếm, ghi phép suy và cận ở N4B8-03; nêu thành câu hỏi mở cho chủ sở hữu. |
| D7 | Bộ chạy của 8 lần chạy chiều tuyết | v7, phần A v4: "chưa kiểm lại"; R26 Q8: runner-tier3-v2, phục hồi không tệ hơn | CK8:65-72: 8 lần chạy tuyết và 51 thư mục C-30 của T3.8 cùng binarySha256, coreCommitSha, policyConfigurationHash; sha256 DLL khớp; `wp4-tier3-v2.json:7` | Ghi ở 4.10 (N4B8-05); bỏ lưu ý "chưa kiểm lại" ở phần B; phần A cần sửa theo (NOTES mục 8). |
| D8 | Ngân sách 11 trang | Đề bài: ≈ 11 trang theo thước 330 tiếng; NOTES v7 §9 liệt kê chỗ cắt | Script đếm (cùng cách với NOTES v7) | Đã cắt mọi chỗ NOTES v7 §9 cho phép và gộp hai bảng đệm; v10 ≈ 13,1 trang theo thước (v7 ≈ 14,0), ≈ 9,5 trang theo mật độ đo được. **Chưa đạt 11.** Cắt thêm cần chủ sở hữu chọn (NOTES mục 4). |

## 2. Codex R29 (CX)

| ID | Mục CX | Dòng v7 | Nhận xét | Bằng chứng đã kiểm | QĐ | Thay đổi trong v10 |
|---|---|---|---|---|---|---|
| CX-01 | §2.1 | 195-211 | Học máy: 30 s là mục tiêu chỉnh trên tập hiệu chỉnh, không phải độ dài thêm trên ngày kiểm; hồ sơ cố định 12–13/11; ngày kiểm đã xem; bỏ **hai** biến trạng thái; "không đổi kết quả nào" sai | MLS:9-10, 19-23, 37-39, 71-82; ML:3,6-7; MLT dòng 5, 10 (37,219 / 31,772 s), 61-64 (sớm 7,063 / 7,311%) | M | Đoạn học máy viết lại với cả bốn ý, lời ngắn hơn đề xuất; 37,2 / 31,8 s để ở EV và Phụ lục C; câu cuối thu về "không đổi số khách trễ ở hai phép so này" (N4B8-04). |
| CX-02 | §2.2 | 106-107 | Ô "chưa đo" sai: `E_pad` = 0 | D1 | A | Dòng tới sớm của Bảng `bang:c4-dubao`: 0 / 0 / 1 trên 1.471 (N4B8-01, N4B8-08). |
| CX-03 | §2.3 | 383-386 | Số 886,9 s / 2.299,0 s là của cách cộng có giới hạn, khác `eq:so` | RPL:14-15, 113-114; RP1:26 (lịch sử phần vượt 0), 29 (trộn có buổi sáng phần vượt 6 s) | M | Đoạn cuối 4.9 nêu cách cộng có giới hạn bằng lời ngắn hơn đề xuất (N4B8-07); không in các số có dấu 893,3 / 2.292,6 vì tôi không tính lại. |
| CX-04 | §2.4 | 397-402 | Thu hẹp kết luận "giới hạn tính toán không cắt kết quả" | D3 | M | 4.10 đoạn 2: chỉ báo bộ đếm; nêu những giới hạn chưa đọc, kể cả tập tắc đường cố định (thêm so với đề xuất, C4A-18); giữ ý chỉ chèn thêm (N4B8-13). |
| CX-05 | §2.5 | 318-321 | Tách nghĩa vụ gốc của luật hạn chót khỏi chỉ số phát lại | ADD1:29; N-21 (phá hứa = A − p₀ > 30 s, lời hứa không dự báo) | A | 4.8 đoạn luật hạn chót: phát lại không đổi lần chạy, nghĩa vụ tính từ lời hứa đầu không dự báo. |
| CX-06 | §2.6 | 415-418; Ch3 705-706 | Đồng bộ câu kiểm thử ở chương 3 | TR; TLOG:43-105; TDIRTY | A | 4.10 còn một vế câu (chi tiết sang Phụ lục C); câu thay cho chương 3 ở NOTES mục 7. |
| CX-07 | §2.7 | 482-484 | "30–60 giây" chỉ đúng cho tập chính; tập buổi sáng tới 300 giây | `07-chuong3-v3.tex` Bảng `bang:luat` (luật hạn chót buổi sáng tám mức); X3-28 | A | 4.11 "Phạm vi kết luận": 30 và 60 giây ở tập chính, 30–300 giây ở tập buổi sáng; mặc định 900 giây. |
| CX-08 | §2.8 | 92-94 | Chú thích phải nói rõ trung bình không trọng số theo kịch bản | FA:8; FFA:225 | M | Chú thích Bảng `bang:c4-dubao` tách khối số đếm gộp và dòng "trung bình theo kịch bản, mỗi kịch bản tính như nhau". |
| CX-09 | §2.8 | 186-192 | Nêu cách đưa dự báo vào bộ điều phối (K = 2) và 14 / 15 lần chạy hoàn tất | RF:9,72; `configs/forecast-k2-2018-11-14.json`:1; PFW:85-89; FR:117,124,138; RX:11-12; R26 Q9 | A | Đoạn "Đưa dự báo vào bộ điều phối": K = 2 nói bằng lời (khung hiện tại và khung kế tiếp), 14 / 15 lần chạy, "trên cùng 15 kịch bản" (N4B8-06). |
| CX-10 | §2.8 | 188-189 | Có thể thêm số gộp 3.849 / 8.496 và 5.121 / 8.468 | Không kiểm (BIC chưa mở trong vòng này) | R | Không thêm: chưa tự kiểm (luật chủ sở hữu: số mới phải kiểm bằng script); giữ nhãn "trung bình theo kịch bản"; ghi thành câu hỏi mở. |
| CX-11 | §3.1 | 22-25 | 62.837 dựa vào Q4/PV (giải lại đủ thứ tự), không phải WPCHK; câu thay thế đề xuất | Q4:10-19, 128-142; PV:1-7; WPCHK:12-15 | M | 4.6 đoạn 2: "một chương trình viết riêng giải lại… Với thứ tự gốc… cho đúng lựa chọn đã ghi ở mọi lượt quyết định của năm cấu hình"; số 62.837 và anchor đúng ở EV (N4B8-10). |
| CX-12 | §3.1 | 25 | 62.837 là tổng năm cấu hình; cùng mã chạy hai lần | PV:2-6; R17V:29 | A | Phạm vi "năm cấu hình" trong câu; "không phải hai bản cài đặt độc lập" trong EV. |
| CX-13 | §3.2 | 101-104 | Số đếm theo khung lấy được từ CELLS | CK8:4-11 | A | Khối số đếm của Bảng `bang:c4-dubao` (N4B8-01). |
| CX-14 | §3.3 | 182 | Dòng EV "81,7 + 5.352,6 + 783,0 = 6.217,4" sai phép cộng | FA:30 | A | EV dưới hình ghi 81,742 + 5.352,646 + 783,018 = 6.217,406 (N4B8-11). |
| CX-15 | §3.4 | 187-188 | Viết "FleetPy tính xe tới…" | RX:13-15; FR:120-121 | A | "FleetPy tính rằng xe sẽ tới điểm đón muộn hơn giờ đón muộn nhất chưa tới 3 giây". |
| CX-16 | §3.4 | N4B-07 | Tỉ lệ khung 8 giờ là 8,4%, không phải 8,3% | Không in trong v10 | A | Ghi ở phụ lục 6, mục "Dòng cũ cần sửa". |
| CX-17 | §3.5 | 208-210 | Thêm n = 200 cho 16/11 và n của luật C | CK8:44-57 | A | "(145 khách)", "(200 khách)", "(147 và 197 khách)". |
| CX-18 | §3.6 | 328-333 | Không mở rộng câu "chọn trần hay đệm" sang mọi mức | — | A | Giữ câu ở đúng hai cấu hình đã so; "đây là lựa chọn của hãng xe". |
| CX-19 | §3.8 | 428-432 | Bốn ngưỡng trễ là trên hai nhóm khách khác nhau | N-24; C04 | A | 4.11 đoạn 1: "trên hai nhóm khách khác nhau". |
| CX-20 | §3.8 | 458-461 | Ngày kiểm học máy đã xem phải nói tại chỗ | MLS:9-10 | A | Đoạn học máy và 4.11 "dùng lại dữ liệu đã xem". |
| CX-21 | §4 | ADD3 | Sửa N4B-01/02/03/07/08, F09, F15, K34 | Các anchor trên | A | Phụ lục 6, mục "Dòng cũ cần sửa". REG A24 ("mỗi xe"): phần B dùng đúng "mỗi lượt", không cần sửa văn bản. |
| CX-22 | §5 | NOTES | NOTES ghi 497 dòng, thực tế 488 | `wc -l` | A | NOTES mới mô tả v10. |
| CX-23 | §5 | 71-72 | Chương 5 có đặt phép thử ưu tiên chi phí lên đầu không | Chương 5 chưa viết | CC | Giữ câu ở 4.6; NOTES mục 9 ý 7. |
| CX-24 | §6 | — | Số trang, va chạm bảng hình chưa kiểm được | Không build | CC | Ước lượng ở NOTES mục 1; người ghép build với `--keep-logs`. |

## 3. Kiểm chứng sự kiện R27 (FC)

| ID | Mục FC | Dòng v7 | Nhận xét (nhãn FC) | Bằng chứng đã kiểm | QĐ | Thay đổi trong v10 |
|---|---|---|---|---|---|---|
| FC-01 | B01 | 17-18 | "cùng tệp cấu hình" sai: hai tệp chính sách chỉ khác trần (LABEL) | NEW:12; H01 | A | "hai tệp chính sách cam kết của chúng chỉ khác nhau ở trần giờ trả". |
| FC-02 | B05 | 24 | "bộ chọn được chạy lại" là quy hoạch động viết riêng, không phải bộ giải thật (LABEL) | Q4:10-19 | A | "một chương trình viết riêng giải lại bài toán chọn trên đúng các phương án đã ghi". |
| FC-03 | B07 | 25 | 62.837: phạm vi năm cấu hình, anchor sai (LABEL) | PV:1-7; Q4:131-138; NEW:7 | M | Phạm vi trong câu, số và anchor ở EV (cắt chữ vì ngân sách). |
| FC-04 | B23 | 71-72 | Chương 5 đặt phép thử lên đầu (CANNOT CHECK) | — | CC | Giữ; NOTES mục 9. |
| FC-05 | B33 | 107 | Ô "chưa đo" (WRONG) | D1 | A | 0 / 0 / 1 trên 1.471. |
| FC-06 | B46 | 135-136 | Nguồn gọi 0,17% là mức tốt nhất cho loại dự báo này (LABEL) | FR:167-169; I02 | M | "đạt được trong điều kiện thuận lợi cho dự báo theo giờ trong ngày, không phải hiệu quả ngoài đời"; tránh chữ "mức trần" vì trùng tên trần của luật C. |
| FC-07 | B52 | 187-188 | Xe không thật tới muộn; FleetPy tính rồi dừng (LABEL) | FR:120-121; RX:13-15 | A | "FleetPy tính rằng xe sẽ tới…". |
| FC-08 | B59 | 196 | Biến thể bỏ hai biến trạng thái (LABEL) | MLS:19-23, 67-68 | A | "(số khách khác đã gán và đang trên xe)". |
| FC-09 | B60 | 196-197 | Hồ sơ cố định; 30 s là mục tiêu hiệu chỉnh (LABEL) | MLS:37-39, 71-82; ML:6-7 | M | Cả hai ý trong văn bản; số 37,2 / 31,8 s ở EV. |
| FC-10 | B62 | 198 | Ngày kiểm đã xem trước (LABEL, thiếu) | MLS:9-10 | A | "các ngày đã được xem trước". |
| FC-11 | B68 | 211 | "không đổi kết quả nào" nói quá (OVERSTATED) | ML:21, 26, 31, 67-69; CK8:60-61 | M | "không đổi số khách trễ ở hai phép so này". |
| FC-12 | B96 | 314-315 | 29,2 s là của tập chính; chiều tuyết 25,2 s; bảng trỏ sai (LABEL) | ADD1:106, 113; N-26; N-28 | M | Câu ở đoạn đầu 4.8 chỉ còn tập chính và cuối tuần; bỏ chiều tuyết và tham chiếu bảng sai. |
| FC-13 | B122 | 383 | "Theo sổ" nhưng số là của cách cộng có giới hạn (LABEL) | RPL:14-15 | A | Như CX-03. |
| FC-14 | B127 | 397 | Chỉ ba bộ đếm của bộ sinh được kiểm (OVERSTATED) | D3 | M | Theo lời của CX (câu thay của FC "không cắt kết quả" vẫn kết luận về kết quả). |
| FC-15 | B130 | 400-401 | Câu K34 phải thu hẹp (LABEL) | D3 | M | Bỏ hẳn câu thay vì sửa chữ. |
| FC-16 | B135 | 413-414 | Không phải mọi số được hai bộ đọc tính lại; số khách đi chung chỉ một quy tắc (OVERSTATED) | ADD1:33-78; N-09 | M | "Các số đếm chính…; riêng số khách đi chung chỉ được một quy tắc đếm"; bỏ danh sách chỉ số vì ngân sách. |
| FC-17 | B144 | 430-431 | Trần 120 giây "ở giữa" chỉ về số phục vụ (LABEL) | L1a-02; ADD1:197 | M | Bỏ câu khỏi 4.11; so hai phía của trần 120 giây ở 4.8. |
| FC-18 | B155 | 463-464 | 165 / 196 s là trên 49 kịch bản (LABEL) | SEL6:1-4 | A | "Ở 49 kịch bản dựng từ dữ liệu thật". |
| FC-19 | §3 | — | Thêm khóa `engelhardt2026`, `horl2022` vào `10-tai-lieu.tex` | X3-40 | A | NOTES mục 2 (việc của người ghép). |
| FC-20 | §5 | ADD3 | N4B-01 anchor | Q4, PV | A | N4B8-10. |
| FC-21 | §5 | ADD3 | N4B-03 sai vế cuối | D1 | A | N4B8-08. |
| FC-22 | §5 | NOTES v7 §6 | Số đếm gộp có trong CELLS | CK8:4-11 | A | N4B8-01, Bảng `bang:c4-dubao`. |
| FC-23 | §5 | ADD3 | N4B-08 thiếu hồ sơ cố định | MLS:37-39 | A | N4B8-04. |
| FC-24 | §5 | NOTES v7 | Số dòng 497 sai | — | A | NOTES mới. |
| FC-25 | §5 | ADD3 | Đầu tệp ghi "bản nộp v6" | — | A | Ghi nhận; không sửa được tệp cũ. |
| FC-26 | §7.17 | 101-104 | Thêm số đếm gộp vào Bảng dự báo | CK8:4-11 | A | Đã thêm. |
| FC-27 | §7.17 | 323-324 | Nêu cả ngưỡng một phút của trần 120 giây | N-06; N-16 | A | "nhưng 2.322 lượt ở ngưỡng một phút, ít hơn 2.328". |
| FC-AG | §2 | toàn bộ | 142 mục AGREE | Đọc lại các anchor khi dùng | — | Giữ nguyên số; không tính vào A/M/R. |

## 4. Người đọc ngoài ngành và giảng viên R27 (RL)

### 4.1 Các chỗ khó B1–B88

| ID | Dòng v7 | Nhận xét (rút gọn) | Bằng chứng / căn cứ | QĐ | Thay đổi trong v10 |
|---|---|---|---|---|---|
| B1 | 14 | Tên mục gợi kết quả đã đo; "thứ tự ưu tiên" ≠ "thứ tự tiêu chí" | OUTLINE-V2:195; Ch3:53 | M | "Vai trò của trần và thứ tự tiêu chí của bộ chọn"; "chưa được chạy" ở đoạn đầu. |
| B2 | 17-18 | Bỏ "tệp cấu hình" | NEW:12 | M | Giữ hai tệp chính sách vì đó là sự kiện đúng (FC-01). |
| B3 | 18-19 | Cụm cuối treo | Phần A v4:761-763 đã nói ý này | M | Bỏ câu; phần A đã nêu. |
| B4 | 19-20 | Nêu rõ đánh đổi nào, tiêu chí 3, 4 | Bảng `bang:rangbuoc` | M | "đánh đổi giữa số lượt phục vụ và số lượt trễ"; định nghĩa chi phí kế hoạch ở chú thích bảng. |
| B5 | 23 | Định nghĩa "phép sàng lọc" | — | M | "phép sàng lọc" kèm mô tả ngay câu sau. |
| B6 | 23-25 | Lựa chọn mới không quay lại mô phỏng | WPCHK:1-19 | A | "các lượt sau vẫn đi theo lựa chọn cũ". |
| B7 | 25 | Mục đích và đơn vị của 62.837 | Q4, PV | M | "cho đúng lựa chọn đã ghi ở mọi lượt quyết định của năm cấu hình"; số ở EV. |
| B8 | 30-33 | Chú thích dài, "không chuyển sang", "tính lặp" | — | M | Định nghĩa U, C-30; "không suy ra cho tập kiểm tra chính"; bỏ "tính lặp". |
| B9 | 44-47 | Ba cách tính chi phí; bốn chữ số thập phân | STYLE quy tắc 27 (bảng giữ số đầy đủ) | M | Nhãn dòng 3 viết lại; câu kết luận 0,31% / 0,08%; giữ 0,3069 / 0,0794 trong bảng. |
| B10 | 50 | Nhãn khối dưới khó đọc | — | A | "Phần dời giờ trả do điều phối tăng thêm, cộng trên mọi khách của đội xe…". |
| B11 | 62 | Trật tự từ lạ | Q4:17-19 | M | Câu mới có lý do theo thứ tự tiêu chí. |
| B12 | 62-64 | Đưa C-60, C-120 vào bảng | Chi phí của hai mức không có dòng sổ (NOTES v7 §6.6) | M | Bỏ hai tỉ lệ khỏi thân bài (cắt theo NOTES v7 §9); không thêm cột. |
| B13 | 64-65 | Câu trừu tượng | — | A | "Hai cột đo trên hai tập tình huống khác nhau…". |
| B14 | 66 | "chia cho" dễ hiểu nhầm | CASE | A | "là tổng của hai khách, mỗi khách 17,77 giây". |
| B15 | 69-70 | Câu dài, "quỹ đạo" | — | A | "khi cả lần chạy đi theo lựa chọn mới". |
| B16 | 71 | "độ tin cậy" chưa định nghĩa | — | M | "chưa tách được phần của trần và phần của bộ chọn"; bỏ "độ tin cậy". |
| B17 | 79-81 | Định nghĩa dự báo trước số | — | M | Giữ câu trả lời trước (OUTLINE §2 quy tắc 2), câu sau trỏ `muc:dubao`. |
| B18 | 84-85 | "cách hứa" chưa định nghĩa | — | M | Nghĩa rõ qua câu "mỗi cách hứa được so với lời hứa đầu của chính nó" và chú thích bảng. |
| B19 | 85-87 | "đệm cùng giá" | D5 | M | "đệm tỉ lệ", định nghĩa, nói tỉ lệ chọn trên chính các khách này. |
| B20 | 117-118 | Thiếu giá trị chênh lệch; "cụm" | FA:33 | A | "giảm 5,84 điểm phần trăm"; "gom 21 kịch bản thành 8 nhóm theo ngày và khung giờ". |
| B21 | 118-119 | "chạm 0", "mong manh" | FA:36 | A | "tức có chứa 0: chưa thể nói dự báo tốt hơn cách đệm này". |
| B22 | 119-120 | "ba buổi sáng", "ngày nguồn" | Ch3:546-549 định nghĩa ngày nguồn | M | "ba buổi sáng đã được xem trước"; "các ngày nguồn" (số nhiều, như chương 3). |
| B23 | 123-124 | Thiếu mức xuất phát | CK8:20, 28 | A | "giảm từ 66 xuống 2 khách trễ". |
| B24 | 126 | "hai phần" là gì | eq:so | M | "hai phần khác nhau của sổ" + câu 86,1% thuộc phần được hồ sơ lịch sử giải thích (tên của chương 3). |
| B25 | 129-130 | "lời hứa trả/đón" | — | A | "lời hứa giờ trả", "lời hứa giờ đón". |
| B26 | 130-132 | Câu 7,37 s | Chú thích `bang:c4-tran120` phần A đã giải thích | M | Thay bằng 76 → 10 trên 2.338 ở 34 kịch bản. |
| B27 | 134 | "thế giới", "tất định" | Bảng thuật ngữ mục G | M | "Tắc đường là một hệ số chung cho cả thành phố"; 4.11 "gần như không có yếu tố ngẫu nhiên". |
| B28 | 134-135 | "hệ số thật" | — | A | "nếu kéo dài lời hứa theo đúng hệ số sẽ xảy ra". |
| B29 | 139-141 | Dùng số thay "ngược lại" | FA:30; RP1:26 | A | 86,1% ở 4.7; 7,3% trên hình; 8,6 / 251,5 s ở 4.9. |
| B30 | 175 | Hai chữ "theo" | — | A | "Số giây trễ chia thành ba phần theo sổ của từng khách". |
| B31 | 186-188 | Lần nào số nào; vì sao dừng | RX:13-15 | M | "FleetPy tính rằng xe sẽ tới … chưa tới 3 giây"; chi tiết từng lần sang Phụ lục C. |
| B32 | 188 | "phải phục hồi" → "bị ép" | Bảng thuật ngữ v2 mục E | A | "không có quyết định bị ép". |
| B33 | 188-190 | Vì sao 15 | FR:124; RX:11 | A | "Ở 15 lần chạy hoàn tất của luật hạn chót". |
| B34 | 191-192 | "lớp lời hứa" | — | M | "Khóa luận chỉ dùng dự báo ở lời hứa báo cho khách". |
| B35 | 195 | "cố định", "phân vị 90" | — | A | "học một lần rồi giữ nguyên"; "(mức mà 90% khách giống vậy không vượt)". |
| B36 | 196-197 | Tên mô hình; "bỏ số khách" | MLS:65-69 | M | "cây quyết định tăng cường theo gradient (gradient boosting)"; "bỏ hai biến trạng thái xe". |
| B37 | 197-198 | Đối chứng khó hiểu | MLS:71-82 | A | Mô tả đối chứng và cách chỉnh như RL đề xuất, có sửa theo CX-01. |
| B38 | 198 | "học" khẩu ngữ | — | M | Câu thay bằng "các ngày đã được xem trước"; giữ "học một lần" (thuật ngữ thường dùng). |
| B39 | 202-203 | "không quá … so với" | — | M | "không hơn quá 1 giây", "không hơn quá 15 giây" (sau "so với đối chứng" ở câu dẫn). |
| B40 | 208 | Số ít "mô hình" | — | A | "đối chứng và mô hình đều không có khách trễ". |
| B41 | 208-210 | Nói bằng số khách; điều kiện nào | CK8:39-46 | A | "bớt 1 trong 2 khách trễ"; "không thỏa điều kiện thứ hai, thứ ba". |
| B42 | 210-211 | Thiếu số đếm | CK8:58-61; D6 | A | 104 → 94 trong 807; 57 khách tới sớm. |
| B43 | 211 | Câu thay về số khách trên xe | CX-01 | M | "Bỏ hai biến trạng thái xe không đổi số khách trễ ở hai phép so này". |
| B44 | 218-219 | Luật C nào | — | A | "luật C trần 30 giây có dự báo". |
| B45 | 224-225 | "đối chứng ghép cặp" | — | A | "hai bên được so trên hai nhóm khách khác nhau, chỉ chung 2.207 khách". |
| B46 | 225-226 | "ba khối bằng nhau" | — | A | "ba khối có lời hứa dài thêm gần bằng nhau". |
| B47 | 266 | Đổi nhãn "Vai trò của từng thành phần" | OUTLINE-V2:197 yêu cầu nhãn này | R | Giữ nhãn theo outline; các đoạn "Thứ nhất…" nói rõ thành phần. |
| B48 | 266-267 | Hơn, kém ai | — | A | "luật C hơn cách đệm ở ngưỡng một phút và kém ở ngưỡng hai phút" (v10). |
| B49 | 268-269 | "chỉ bằng … khi" | N-18 | A | "Muốn bằng luật C…, cách đệm phải làm lời hứa dài thêm gấp khoảng năm lần". |
| B50 | 273 | Ghi rõ cấu hình | — | A | "với cách đệm 30 giây". |
| B51 | 309-310 | Câu quá nén | N-19 | A | "Cách đệm hơn 28 lượt ở ngưỡng hai phút vì phục vụ nhiều hơn 96 lượt, không phải vì ít khách trễ hơn". |
| B52 | 313-314 | Quy ra phút | — | A | "590,1 giây (gần 10 phút)". |
| B53 | 318-320 | "bị ép"; câu dài | CX-05 | A | Đoạn luật hạn chót tách hai câu, dùng "bị ép". |
| B54 | 323 | "núm vặn" | STYLE quy tắc 14 | A | Bỏ. |
| B55 | 324 | "nó" xa | — | A | "với lời hứa chỉ dài thêm 7,27 giây". |
| B56 | 328-329 | "lựa chọn cạnh tranh" | — | A | "không kém luật C, lại phục vụ thêm 96 lượt". |
| B57 | 330-331 | "cho điều đó"; "đổi lại là 96 lượt" | A06; K05 | A | "theo cách xây dựng luật" (đoạn đầu 4.8); "đổi lại 96 lượt phục vụ và 242 khách đi chung". |
| B58 | 331 | Dẫn số cho "dùng chung được" | N-02 | M | Câu giữ, số ở hàng "C-30, dự báo, đệm 30 s" của bảng (không lặp vì ngân sách). |
| B59 | 339-340 | "dự báo lịch sử"; chưa nói chiều tuyết là gì | Phần A Bảng `bang:c4-taptu` | M | "lời hứa theo dự báo"; định nghĩa tập ở phần A. |
| B60 | 349 | "Bảng … phát lại" | — | A | "Bảng … cho kết quả phát lại" (v10). |
| B61 | 349-350 | "xu hướng tăng gần nhất" | FNS:28-29 | A | "mức tăng của hệ số cùng ngày từ khung 15 phút trước sang khung hiện tại". |
| B62 | 350-351 | Con số 19 và "không được giao" | FNS:14-20 | M | Đánh dấu "chỉ để tham khảo" ở chú thích và cột thông tin; bỏ câu quy tắc có ngưỡng. |
| B63 | 370-371 | Hai hàng bảng khó đọc | FNS:17-20 | A | Viết lại cả hai hàng; hàng trễ một khung ghi rõ "có buổi sáng". |
| B64 | 358 | "ngày đã được xem" | — | A | "trên một ngày đã được xem trước khi thiết kế các cách này". |
| B65 | 383 | Tên khác của hàng; dữ liệu không được phép | RPL:14-15 | M | "cách trộn có buổi sáng" + cách cộng có giới hạn (CX-03). |
| B66 | 384 | "sự kiện đã xem trước" mơ hồ | — | M | Ý chuyển vào chú thích bảng và 4.11. |
| B67 | 384-385 | Nơi đo; câu dài | WX:2 (NOAA, trạm Central Park) | A | "Theo trạm Central Park (NOAA)…"; tách câu. |
| B68 | 392-394 | "phải phục hồi"; số nào của ai | X3-16 | A | "0 trong 20.101 và 0 trong 20.435 lượt", "bị ép". |
| B69 | 397 | "cắt" | — | A | Bỏ. |
| B70 | 398-399 | "giới hạn khối lượng khám phá" | GEN:236-246, 298-312 | A | "giới hạn số bước tìm cách chèn". |
| B71 | 399-400 | "chỉ một lần" mơ hồ | ADD1:119-122 | A | "chỉ để một yêu cầu sang lượt sau ở mỗi cấu hình". |
| B72 | 400-401 | "gói cam kết"; nói quá | D3 | M | Bỏ câu; không dùng câu thay của RL vì vẫn kết luận nhân quả. |
| B73 | 404-406 | Tiêu chí 3 hai phần; nên chuyển lên 4.6 | D4 | M | Một câu ở 4.10, trỏ `muc:doichung`; không chuyển. |
| B74 | 409-410 | Byte và phiên bản chính sách | NEW:13 | A | Bỏ đoạn (cắt theo NOTES v7 §9). |
| B75 | 413-414 | "bộ đọc"; ai viết | Ch3:711-714 | M | "chương trình đọc dữ liệu viết riêng" + trỏ `muc:kiemtra` (chương 3 nêu Claude và Codex). |
| B76 | 415-417 | Lịch sử thao tác, thuật ngữ git | STYLE quy tắc 13 | A | Một vế câu; chi tiết sang Phụ lục C. |
| B77 | 428 | "bảng các điểm" | — | A | "các điểm trên một đường đánh đổi". |
| B78 | 429 | "mất khách đi chung" | — | A | "phục vụ ít hơn 96 lượt và có ít hơn 242 khách đi chung". |
| B79 | 434 | Câu dẫn dịch máy | — | M | "Một phép tính hòa vốn giả định cho thấy cách đọc các điểm này". |
| B80 | 435-436 | Câu dài | C29 | A | Tách: định nghĩa k, m; rồi ngưỡng. |
| B81 | 437-438 | "chạm tới"; chuyển sang tải thấp | — | M | Gộp vào gạch đầu dòng thời gian dừng, nêu cả tải cao. |
| B82 | 446-447 | "thế giới"; "không chuyển sang" | — | A | "gần như không có yếu tố ngẫu nhiên"; "không cho biết hiệu quả khi vận hành thật". |
| B83 | 449 | "bao đóng" | Phần A Bảng `bang:c4-thamso` | A | "đồ thị rút gọn chỉ có 96 nút" (v10). |
| B84 | 463-464 | "tập đủ điều kiện" | SEL6:1-4 | A | "mọi chuyến đủ điều kiện (trung vị thời gian đi thẳng…)" (v10). |
| B85 | 470 | "phép kiểm khả thi" | — | A | "Bộ điều phối vẫn kiểm giờ đón bằng giờ không dự báo". |
| B86 | 479 | "trên quỹ đạo" | — | A | "chưa được chạy thành lần mô phỏng đầy đủ". |
| B87 | 480-481 | "vế cộng dồn" | Phần A mục 4.5 | A | "phần cộng dồn". |
| B88 | 482-483 | "chỉ là phần hạn chót"; Hörl–Zwick chưa giải thích | Ch3:450-458 | M | "chỉ mượn thành phần hạn chót…"; trỏ `muc:doichung`; dải 30–300 giây theo CX-07. |

### 4.2 Thay đổi bắt buộc M1–M5 và nên sửa S1–S5

| ID | Nhận xét | Bằng chứng / căn cứ | QĐ | Thay đổi trong v10 |
|---|---|---|---|---|
| M1 | Trả lời thẳng "vì sao cần luật C nếu đệm cho cùng số đúng giờ" | C10; C20; N-23; N-28; phần A v4:246-247 | A | Đoạn đầu 4.8: "Hai cách này cho hai thứ khác nhau…" (đệm kéo dài lời hứa, không đổi quyết định: 174 khách, 590,1 s; luật C giới hạn ở 29,2 s theo cách xây dựng luật, kể cả cuối tuần; đổi lại 96 lượt). Không kể "0 quyết định bị ép" là lợi thế so với U. Chú thích bảng cảnh báo nhóm khách khác nhau. |
| M2 | Mức 120 giây khớp phần A | D2 | A | Gạch đầu dòng "dùng lại dữ liệu đã xem" ở 4.11. |
| M3 | Gọi đúng phép kiểm cài đặt; bỏ câu nói quá | Ch3 `nx:giunguyen` và đoạn sau; X3-16; D3 | M | Đoạn đầu 4.10 như đề xuất (kèm U 0 / 20.760); câu thay về giới hạn tính toán không dùng (D3). |
| M4 | "Chưa chạy" lên đầu 4.6; định nghĩa sàng lọc; câu kết luận | OUTLINE §7.2 | M | Đoạn đầu 4.6 kết bằng "chưa được chạy trên tập kiểm tra chính"; đoạn 2 mô tả phép sàng lọc; câu 0,31% / 0,08%; lời ngắn hơn đề xuất. |
| M5 | Khoảng tin cậy; lưu ý giờ đón cạnh kết quả | FA:33,36; F07 | M | Khoảng tin cậy sửa như đề xuất (gọn hơn); 4.7 có một câu trỏ, đầy đủ ở 4.11 (tránh lặp, STYLE quy tắc 32). |
| S1 | Thống nhất thuật ngữ | Bảng thuật ngữ v2; chương 3 `eq:so` | M | Đổi "bị ép", "thế giới", "bao đóng", "vế cộng dồn", "lời hứa giờ trả/đón", "thứ tự tiêu chí", "dự báo lịch sử"; thêm chú giải U, C-B ở chú thích bảng. **Không** đổi "được hồ sơ lịch sử giải thích" vì đó là tên phần sổ ở chương 3 (một khái niệm một tên). |
| S2 | Đổi tên, định nghĩa đệm; ghi "chưa đo" | D1, D5 | M | Đổi tên thành "đệm tỉ lệ" và định nghĩa; **bác** vế "tỉ lệ tới sớm chưa được đo" (đã đo, 0). |
| S3 | Làm rõ hàng dùng dữ liệu không được phép | FNS:14-20 | M | Chú thích và hàng bảng; bỏ quy tắc có ngưỡng. |
| S4 | 4.10: bỏ lịch sử, định nghĩa từ, chuyển đoạn tiêu chí 3 | D4; TR | M | Lịch sử sang Phụ lục C; định nghĩa giới hạn bước; ai viết → `muc:kiemtra`; bỏ đoạn byte; tiêu chí 3 ở lại 4.10. |
| S5 | 4.11: vế "kết luận bị ảnh hưởng"; hai hạn chế thiếu | B05; F07; F11 | M | Thời gian dừng → phần dời và cái giá 96 lượt chỉ áp cho thiết lập này; giờ đón → số có dự báo chưa tính việc sửa; ngày 12/11 nêu ở 4.7; **bác** vế "đệm chưa đo tới sớm" (D1). |

### 4.3 Phần 2 của giảng viên

| ID | Mục RL | Nhận xét | Bằng chứng / căn cứ | QĐ | Thay đổi / lý do |
|---|---|---|---|---|---|
| L-01 | 2.1 sàng lọc | Không có câu kết luận cho khối chi phí | H05 | A | Câu 0,31% / 0,08%. |
| L-02 | 2.1 sàng lọc | C-60, C-120 không có trong bảng | Chi phí của hai mức không có dòng sổ | R | Không thêm số chưa đăng ký; bỏ cả hai tỉ lệ khỏi thân bài (Phụ lục C). |
| L-03 | 2.1 sàng lọc | Chú thích không định nghĩa U, C-30 | STYLE quy tắc 12 | A | Thêm. |
| L-04 | 2.1 sàng lọc | Bốn chữ số thập phân | STYLE quy tắc 27 | R | Bảng giữ số đầy đủ; thân bài làm tròn 0,31 / 0,08. |
| L-05 | 2.1 sàng lọc | Không nhắc giới hạn bộ chạy cũ chưa kiểm | C4A-18 | M | Chú thích "bộ chạy cũ"; 4.10 nói bộ đếm ở tập tắc đường cố định chưa được đọc. |
| L-06 | 2.1 dự báo | Chỉ trung bình theo kịch bản | CK8:4-11 | A | Khối số đếm. |
| L-07 | 2.1 dự báo | Ô tới sớm "chưa đo" | D1 | A | 0. |
| L-08 | 2.1 dự báo | Lưu ý giờ đón không đặt cạnh kết quả | F07 | M | Câu trỏ ở 4.7, đầy đủ ở 4.11. |
| L-09 | 2.1 hình | Lời văn dùng "ngược lại" | — | A | Số trong lời văn. |
| L-10 | 2.1 hình | Thanh tuyết thiếu % của 8,6 s | [A] 8,566 / 3.445,933 | A | "8,6 s (0,25%)", đặt phía trên thanh để đường dẫn không cắt chữ (N4B8-12). |
| L-11 | 2.1 đệm | Chú thích thiếu cảnh báo nhóm khách | C04 | A | Thêm. |
| L-12 | 2.1 đệm | U, C-30, C-120 chưa định nghĩa | — | A | Thêm. |
| L-13 | 2.1 đệm | Số của luật hạn chót có dự báo không ở bảng nào | ADD1:29 | M | Số ở văn xuôi (2.338 / 2.328); nghĩa vụ trỏ Bảng `bang:c4-nghiavu`; không thêm hàng vì ngân sách. |
| L-14 | 2.1 hai phía | Kết luận rải rác; thiếu cột trễ 60 s | — | M | Gộp hai bảng thành một (cột tới sớm); ±60 s và phần đuôi vào văn xuôi. |
| L-15 | 2.1 tuyết | Cột số gộp và cột trung bình theo kịch bản trong một bảng | RP1:6-20 chỉ in độ dài thêm trung bình theo kịch bản | R | Số gộp của độ dài thêm không có trong output đã lưu; chú thích ghi cách gộp của từng cột. |
| L-16 | 2.1 tuyết | Không có cột tới sớm | RP1:7-20 (E60 0,00%) | M | Câu trong chú thích: không cách nào có khách tới sớm (N4B8-09). |
| L-17 | 2.1 tuyết | Hàng dùng dữ liệu không được phép chưa đánh dấu | — | A | Đánh dấu. |
| L-18 | 2.1 tuyết | Đệm chỉnh trên chính ngày tuyết | FNS2:10-11 | A | Ghi ở hàng "Đệm tỉ lệ". |
| L-19 | 2.1 tuyết | "Quy tắc có ngưỡng" không có trong bảng | — | A | Bỏ khỏi lời văn. |
| L-20 | 2.1 chung | Câu "nói cách khác" sau bảng | — | M | Thêm cho bảng sàng lọc; các bảng khác đã có đoạn kết luận ngay sau. |
| L-21 | 2.2 ý 1 | Số 0 là hệ quả của Nhận xét | Ch3 `nx:giunguyen` | A | "Đây là phép kiểm cài đặt…". |
| L-22 | 2.2 ý 2 | Bộ chạy tập cố định và chiều tuyết chưa kiểm, không nói ở 4.10 | D7; C4A-18 | M | Chiều tuyết đã kiểm và nói ở 4.10; tập cố định ghi "chưa bộ đếm nào được đọc". |
| L-23 | 2.2 ý 3 | 4.10 không kiểm phép phát lại, phép đệm, đường đi học máy | Không có phép kiểm độc lập riêng cho ba đường này trong sổ | R | Không viết điều không có bằng chứng; ghi thành câu hỏi mở (NOTES mục 9 ý 6). |
| L-24 | 2.2 ý 4 | Kiểm thử trên mã dựng lại không chứng minh bản lưu trữ | I13 | A | Gạch đầu dòng "Tích hợp" ở 4.11; Phụ lục C. |
| L-25 | 2.2 ý 5 | Ai viết hai bộ đọc | Ch3:711-714 | A | Trỏ `muc:kiemtra`. |
| L-26 | 2.2 ý 6 | Không có độ nhạy theo hạt giống | Không có lần chạy nào như vậy; không được chạy mô phỏng | R | Không có bằng chứng để viết; câu hỏi mở (NOTES mục 9 ý 5). |
| L-27 | 2.2 ý 7 | Chuyển đoạn tiêu chí 3 lên 4.6 | D4 | R | Chương 3 dòng 467-468 trỏ `muc:c4-hople`. |
| L-28 | 2.3 | Thời gian dừng: kết luận nào bị ảnh hưởng | B05 | A | Thêm. |
| L-29 | 2.3 | Lệch với phần A về 120 giây | D2 | A | Sửa. |
| L-30 | 2.3 | Giờ đón: số có dự báo bị ảnh hưởng | F07 | A | Thêm. |
| L-31 | 2.3 | Đệm chưa đo tới sớm | D1 | R | Đã đo: 0 trên 1.471 (FFA:139-141; CK8:4). |
| L-32 | 2.3 | Mọi dự báo có ngày 12/11 | F11; FNS:21-22 | A | Câu ở 4.7. |
| L-33 | 2.3 | Chưa so trên 2.207 khách chung | Không có output đã lưu cho phép so này | R | Không thêm số chưa kiểm; câu hỏi mở (NOTES mục 9 ý 4). |
| L-34 | 2.3 | Ngưỡng của bốn điều kiện học máy chọn khi nào | `BRIEF-CH4B-WRITER.md`:29-30 ("state the four conditions … without saying when they were set") | R | Luật chủ sở hữu. |
| L-35 | 2.5 | "phản ánh tác động của cả gói cam kết" | D3 | A | Bỏ. |
| L-36 | 2.5 | Số 0 trình bày như kết quả | Ch3 `nx:giunguyen` | A | Như L-21. |
| L-37 | 2.5 | "luật C cho điều đó" đọc như bảo đảm giờ trả | A22; K05 | A | "theo cách xây dựng luật" (giới hạn phần dời của mô hình). |
| L-38 | 2.5 | Giới hạn ở chiều tuyết với bộ chạy chưa kiểm | D7 | A | Bỏ chiều tuyết khỏi câu đó; bộ chạy nay đã kiểm. |
| L-39 | 2.5 | "mong manh" | FA:36 | A | Bỏ. |
| L-40 | 2.5 | "được hồ sơ lịch sử giải thích" gần động từ nhân quả | Ch3:589-608 (tên phần sổ; chú thích "phụ thuộc dự báo đang dùng") | R | Giữ tên của chương 3; câu luôn mở bằng "Theo sổ". |
| L-41 | 2.5 | Phép tính k > 0,756 m bỏ qua các yếu tố khác | C29 | A | "Phép tính bỏ qua mọi yếu tố khác và so hai nhóm khách khác nhau". |
| L-42 | 2.5 | "số yêu cầu được nhận không đổi" là hệ quả của thứ tự | Q4:17-19; PV `accepted_changes` 0 | A | "đúng theo cách đặt thứ tự". |
| L-43 | 2.6 | Cảnh báo nhóm khách đến muộn | C04 | A | Đoạn 2 của 4.8 và chú thích bảng. |
| L-44 | 2.6 | 68 khách trễ quá hai phút trên hai nhóm khác nhau | C04 | M | Cảnh báo một lần ở đoạn 2 và chú thích (STYLE quy tắc 32), không lặp mỗi câu. |
| L-45 | 2.6 | "hơn / kém" không nhắc nhóm khác nhau | C04 | M | Như L-44. |
| L-46 | 2.6 | Bốn ngưỡng trễ ở 4.11 | C04 | A | "trên hai nhóm khách khác nhau". |
| L-47 | 2.6 | 47,6% so với 62,8% là hai lần chạy khác nhau | RX:11 | A | "ở các lần chạy không đưa dự báo vào trên cùng 15 kịch bản" (v10). |
| L-48 | 2.6 | Bảng dự báo, bảng tuyết so trên cùng nhóm khách là điểm mạnh | — | M | Chú thích nêu nhóm khách (1.471, 601); không thêm lời tự khen. |
| L-49 | 2.7 | Bảng thuật ngữ không thống nhất | Như S1 | M | Như S1 và các dòng B. |
| L-50 | 2.8 Q1 | Vì sao chưa chạy phép thử ưu tiên chi phí | Sổ không ghi lý do; OUTLINE §10 ý 4 (chủ sở hữu đặt hạn) | R | Không viết lý do không có bằng chứng; văn bản nói rõ "chưa được chạy" và hệ quả. |
| L-51 | 2.8 Q2 | Số yêu cầu được nhận không đổi do thứ tự? | Như L-42 | A | Trả lời ở 4.6. |
| L-52 | 2.8 Q3 | So trên 2.207 khách chung | Như L-33 | R | Câu hỏi mở. |
| L-53 | 2.8 Q4 | Đệm tỉ lệ chỉnh trên ngày nào; tới sớm | FFA:15-17; D1 | A | "trên chính các khách này"; tới sớm 0. |
| L-54 | 2.8 Q5 | Khoảng t có hợp lệ khi các nhóm chung ngày nguồn | FR:170-171 | M | "Các khoảng chỉ dựa trên ba buổi sáng đã được xem trước, và mọi hồ sơ dự báo đều có ngày 12/11". |
| L-55 | 2.8 Q6 | Sửa phép kiểm giờ đón thì 0,17% và 2.328 còn không | F07 | M | Nói rõ "chưa tính việc sửa phép kiểm này"; không đoán hướng thay đổi. |
| L-56 | 2.8 Q7 | 120 giây chọn khi nào | D2 | A | Như M2. |
| L-57 | 2.8 Q8 | Ai viết bộ đọc; kiểm thử chứng minh gì | Ch3:711-714; I13 | A | Như L-24, L-25. |
| L-58 | 2.8 Q9 | Dừng 30 s, tải 1,33 thì cái giá đổi thế nào | Không có lần chạy | M | Câu giả thuyết chưa kiểm ở 4.11. |
| L-59 | 2.8 Q10 | Luật C cho khách điều gì | C20; RD §8 | A | Đoạn đầu 4.8; giá trị chưa đo nói ở 4.11. |
| L-60 | 2.8 thêm | Ba lần dừng có nên xử lý bằng dung sai | Không có lần chạy với dung sai; không được chạy mô phỏng | R | Ngoài phạm vi bằng chứng; ghi kết luận "chỉ áp cho cách đã thử". |

## 5. Đếm theo người nhận xét

| Người nhận xét | Số dòng | A | M | R | CC |
|---|---:|---:|---:|---:|---:|
| Codex R29 (CX-01…24) | 24 | 16 | 5 | 1 | 2 |
| Kiểm chứng sự kiện R27 (FC-01…27; 142 mục AGREE giữ nguyên, không tính) | 27 | 17 | 9 | 0 | 1 |
| Người đọc, giảng viên R27: B1–B88 | 88 | 52 | 35 | 1 | 0 |
| Người đọc, giảng viên R27: M1–M5, S1–S5 | 10 | 2 | 8 | 0 | 0 |
| Người đọc, giảng viên R27: phần 2 (L-01…60) | 60 | 33 | 14 | 13 | 0 |
| **Người đọc, giảng viên R27, cộng** | **158** | **87** | **57** | **14** | **0** |
| **Tổng** | **209** | **120** | **71** | **15** | **3** |

Hai vế bị bác bên trong các dòng M (không tính vào cột R): vế "tỉ lệ tới sớm của đệm chưa được đo" trong S2 và S5 (D1), và
câu thay "chênh lệch … không đến từ các giới hạn tính toán này" trong M3 (D3).

## 6. Các nhận xét bị bác và lý do

| ID | Lý do (anchor) |
|---|---|
| CX-10 | Số gộp lượt bị ép 3.849 / 8.496 và 5.121 / 8.468 chưa được tôi kiểm bằng script; giữ "trung bình theo kịch bản". |
| B47 | OUTLINE-V2:197 yêu cầu nhãn "vai trò của từng thành phần". |
| L-02 | Chi phí của phép sàng lọc ở trần 60, 120 giây không có dòng sổ (NOTES v7 §6.6). |
| L-04 | STYLE quy tắc 27: bảng giữ số đầy đủ. |
| L-15 | Độ dài thêm gộp theo khách của các cách hứa chiều tuyết không có trong output đã lưu (RP1:6-20); chú thích ghi cách gộp từng cột. |
| L-23 | Không có phép kiểm độc lập riêng cho phát lại, đệm, học máy trong sổ; không viết điều không có bằng chứng. |
| L-26 | Không có lần chạy độ nhạy theo hạt giống; không được chạy mô phỏng. |
| L-27 | Chương 3 v3 dòng 467-468 trỏ `muc:c4-hople` cho các số này. |
| L-31 | Đã đo: `forecast_family_a.py:139-141`, CELLS cột `E_pad`, CK8:4 (0 trên 1.471). |
| L-33, L-52 | Không có output đã lưu cho phép so trên 2.207 khách chung. |
| L-34 | `BRIEF-CH4B-WRITER.md`:29-30: nêu bốn điều kiện mà không nói chúng được đặt khi nào. |
| L-40 | Chương 3 `eq:so` đặt tên "phần được hồ sơ lịch sử giải thích"; quy tắc một khái niệm một tên. |
| L-50 | Sổ không ghi lý do chưa chạy; không viết lý do không có bằng chứng. |
| L-60 | Không có lần chạy với dung sai; ngoài phạm vi bằng chứng. |

## 7. Số mới in trong v10 và nguồn

| Số | Nguồn |
|---|---|
| 68 / 22 / 2 trên 1.471; 60 / 17 / 1 trên 444; 8 / 5 / 1 trên 609; 0 / 0 / 0 trên 418; tới sớm 0 / 0 / 1 | N4B8-01; CK8:4-11 (CELLS) |
| 66 → 2 (luật hạn chót, luật trần độ dời khách thấy); 129 → 63 trên 1.512; 28 trên 437 ở khung 17 giờ | N4B8-02; CK8:12-28 |
| 1 trong 2 khách trễ (145 khách); 1 và 1 (200 khách); 0 (147, 197 khách); 104 → 94 trên 807; 57 tới sớm | N4B8-03; CK8:39-61 (MLT, suy có cận) |
| Bộ chạy, cấu hình, luật phục hồi của 8 lần chạy chiều tuyết giống tập chính | N4B8-05; CK8:65-72; R26 Q8 |
| K = 2 (khung hiện tại và khung kế tiếp); 14 và 15 lần chạy hoàn tất | N4B8-06; RF:9,72; PFW:85-89; FR:117,124,138; R26 Q9 |
| 0,25% phần điều phối ở chiều tuyết | N4B8-12 [A] |
| Không cách hứa nào ở chiều tuyết có khách tới sớm | N4B8-09; RP1:7-20 [A] |

*Hết nhật ký. Viết bởi Claude (người sửa Chương 4 phần B), 2026-10-13. Chỉ tạo tệp này trong `reviews/`.*
