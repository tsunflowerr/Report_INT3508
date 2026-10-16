# CH4A — Nhật ký sửa Chương 4 phần A theo ba bản nhận xét R25 (2026-10-12), bản v2

> **Bản v2 của nhật ký** thay `CH4A-REVISION-LOG.md` (giữ nguyên, không sửa). Nội dung các bảng giống hệt; chỉ sửa phần đếm A/M/R ở cuối mục 4 và mục 5, vốn viết lẫn lộn ở bản đầu. Số đếm dưới đây do script đếm cột QĐ của từng dòng bảng (scratchpad phiên, `count_log.py`).

**Đầu vào:** bản 1 `drafts/08-chuong4-phanA.tex` (giữ nguyên) và NOTES; ba bản nhận xét: Codex
`optimize/codex-debate/codex-work/R25-CH4A-REVIEW-CODEX.md` (**CX**), kiểm chứng sự kiện `reviews/R25-FACTCHECK-CH4A-CLAUDE.md`
(**FC**), người đọc và giảng viên `reviews/R25-READER-LECTURER-CH4A-CLAUDE.md` (**RL**).
**Đầu ra:** bản ghép **`drafts/08-chuong4-phanA-v4.tex`**; `-v2.tex` (lượt sửa đầu, dài hơn ngân sách) và `-v3.tex` (lượt rút
gọn thứ nhất) là bản trung gian, không dùng để ghép. Ghi chú: `drafts/08-chuong4-phanA-v2-NOTES.md`. Sổ mới:
`evidence/EVIDENCE-REGISTER-ADDENDUM-4-CH4A.md` (C4A-01…20) và script ở `evidence/checks-ch4a-v2/` (**CK4A**). Bảng thuật ngữ
sửa: `style/GLOSSARY-VI-v2.md`.

**Cách kiểm.** Một nhận xét không đúng chỉ vì người nhận xét nói vậy. Với mỗi nhận xét có tính sự kiện, tôi mở mã chỉ đọc
ở `C:/Code/RideBound-noworse/src/`, script và output được trỏ, hoặc tính lại bằng script chỉ đọc mới (CK4A). Anchor ghi theo
khóa của sổ chính và các phụ lục. **QĐ:** **A** = nhận; **M** = nhận có sửa (lý do ghi kèm); **R** = không nhận (lý do và
anchor ghi kèm); **CC** = không kiểm được (giữ cách viết cũ). "Thay đổi" chỉ chỗ trong v4. "Dòng" là dòng của bản 1.

---

## 0. Bốn câu hỏi được giao kiểm trước

| # | Câu hỏi | Kiểm (anchor) | Kết luận và thay đổi |
|---|---|---|---|
| Q1 | Định nghĩa "quyết định phải phục hồi" / "bị ép" (FC #50, K-1; CX §5.1; RL D23) | RS:1012-1027 (`normalOperation = breachWitnesses.Length == 0`); RS:1097-1108 (witness lấy từ `ForcedExemptions`); VALID:141-145 ("a decision with any exemption is not normal operation"); HVA:244-300 (phục hồi chỉ xét khi phương án giữ nguyên bị bộ kiểm loại; với luật không tệ hơn giữ thêm phương án đổi kế hoạch); POL:443-463 | Định nghĩa của bản 1 và GLOSSARY-VI:93 ("loại hết phương án của một xe") sai. Dùng tên "quyết định bị ép" của Chương 3 v3 và định nghĩa: lượt quyết định có ít nhất một xe bị ép, tức luật lời hứa đã loại cả phương án giữ nguyên kế hoạch và xe đi theo phương án được giữ nhờ luật phục hồi, có ít nhất một khách được miễn trừ (C4A-10). Bảng chỉ số, Bảng nghĩa vụ, 4.2–4.4 đổi tên. Bảng thuật ngữ sửa ở `style/GLOSSARY-VI-v2.md` (dòng 92–93), bản gốc không đụng. |
| Q2 | Câu hỏi đệm đặt ở đâu (RL G4, G6 #1 muốn trả lời ngay trong 4.2; OUTLINE đặt ở 4.8) | OUTLINE-V2:197 (4.8); RD §8; C10, K06, K51 | Theo OUTLINE, không chuyển phân tích 4.8 sang phần A. Câu mở 4.2 sắp lại: điều luật C giữ được (29,2 so với 590,1 giây; 0 so với 18 lượt trễ quá 5 phút) → cái giá (−96 lượt, −242 khách đi chung) → số lượt đúng giờ, đổi chiều theo ngưỡng (+31 ở 60 s, −5 ở 120 s). Thêm một câu trỏ: "khi có dự báo, cộng thêm 30 giây vào mọi lời hứa của điều phối không trần cũng cho 2.328 lượt không trễ quá một phút, bằng luật C có dự báo; vì vậy khóa luận không dùng chỉ số này làm lý do chọn luật C". |
| Q3 | Công bố về mức 120 giây (FC #57, #176; RL D26) | T38:5 (tập chính chạy 1–2/10); BUD (07/10; sàng lọc 120 s trên C-30 của tập chính, D14); CVP:14-18 (10/10; sàng lọc 120 s trên U của tập chính, E06); C120R:10 (C-120 chạy 10/10 22:12–23:48); K42 | Đúng: mức 120 giây được chọn sau khi đã xem kết quả U và C-30 trên chính tập kiểm tra chính và các phép sàng lọc ở 120 giây. 4.1.4 viết bằng lời dùng lại dữ liệu đã xem; 4.4 nhắc lại một câu. Không có chữ nào về kế hoạch, mã băm, dự đoán (C4A-11). |
| Q4 | Hai phỏng đoán của người đọc: 109,6 s là phần vượt quá 30 s hay cả lần dời (D47, G6 #8b); bốn lần dời 1 ms có phải nhiễu (D42, G6 #8c) | BUDPY:22,35-42,49-52 (`o = max(after − limit)`; ngưỡng "overshoot ≤ 90 s (would pass a cap of 120 s)"); BUD:6-10. RSP:56-150; ADD1:104-112; ADDENDUM-1 mục 0.2 | (a) **Người đọc đúng:** 109,6 giây là phần vượt quá 30 giây; tổng dời ≈ 139,6 giây (C4A-09). v4: "mức vượt nhỏ nhất, tức phần vượt quá 30 giây". (b) **CC:** sổ xác nhận mỗi lần dời sớm đúng −1 ms, nhưng nguyên nhân không kiểm được: phần làm tròn duy nhất trong bộ chiếu lịch (cạnh đang đi, `DivideRoundUp`) như nhau cho $e$ và $p$; giả thuyết làm tròn từng cung của bao đóng chưa kiểm (C4A-19). Giữ "đúng 1 mili giây", không nêu nguyên nhân; giữ 33 khách theo định nghĩa (mọi lần dời khác 0), câu đã nói 29 khách bị dời muộn đi. |

## 1. Chỗ các bản nhận xét bất đồng và cách giải

| # | Chủ đề | Ý kiến | Kiểm bằng chứng | Kết luận trong v4 |
|---|---|---|---|---|
| 1 | Câu đệm trong 4.2 | RL: thêm cả đoạn đệm vào 4.2; CX §6: phần A không cần lặp bảng đệm; OUTLINE: 4.8 | OUTLINE-V2:191,197 | Như Q2: sắp lại câu mở, một câu trỏ có một con số. |
| 2 | "Khách đang trên xe" trong ví dụ cơ chế | CX §5.6 viết lại vẫn dùng "khách trên xe"; FC #124: không có ở anchor gốc | W07X:54 ("khách đang có"); W07XM:6 (không ghi giai đoạn) | FC đúng. Viết "một khách", giờ trả "đang hứa" đã lùi 79,0 giây (C4A-12). |
| 3 | Hàng M⁺-60, V-30 của Bảng 4.4 | CX: giữ "chưa đưa vào bảng" được phép; RL D30: điền hoặc bỏ; FC #64: EXP có trễ quá 60 s | CK4A check: 79 / 11 và 74 / 11; EXP:5-6; CX §3 tính độc lập cùng số | Điền trễ và không trễ (C4A-02); đi chung "chưa đếm". |
| 4 | Bảng ngày × khung | RL G6 #13: chuyển sang phụ lục; CX, FC: đúng từng ô; OUTLINE: Bảng 4.7 có phương án dự phòng bằng lời | ADD1:167-186; OUTLINE-V2:191 | Bỏ khỏi thân bài vì ngân sách trang; giữ đoạn tóm tắt theo kịch bản và khung (N-22); câu hỏi mở cho chủ sở hữu về Phụ lục C. |
| 5 | Dãy tỉ lệ bị ép của luật hạn chót ở tập buổi sáng | RL D53: đưa vào bảng; OUTLINE §2 quy tắc 3: trung bình theo kịch bản không chung khối với số gộp | OUTLINE-V2:60-61; D04 | Không đưa vào bảng; nêu đầu, giữa, cuối dãy bằng "giảm từ … xuống …" (dãy không đơn điệu, CX §3). |

---

## 2. Codex (CX)

| ID | Dòng | Nhận xét | Kiểm (anchor) | QĐ | Thay đổi trong v4 |
|---|---|---|---|---|---|
| CX1 | 308-311; 188-190 | Nhận xét giữ nguyên cần điều kiện (N) và $0 \le L_r \le B$; định nghĩa bộ đếm phục hồi theo chứng chỉ | Chương 3 v3:356-375; A22; RS:1012-1027; X3-16 | A | 4.2: "Đây là điều Nhận xét cho trước dưới giả thiết (N), không phải phát hiện thực nghiệm…; điều phối không trần cũng có 0 trong 20.760 quyết định bị ép, và nhận xét không bảo đảm giờ trả thực tế". Bảng chỉ số: định nghĩa "quyết định bị ép" theo Q1, mẫu số là lượt quyết định được xác nhận, trung bình theo kịch bản. Văn bản thay thế dài của CX được rút gọn, giữ đủ ý. |
| CX2 | 469-474 | Bỏ "1.186 … chỉ có lý do cấu trúc" | BUDPY:29-44 (nhóm còn lại = không có bản ghi chặn được ghi); BUD:4-5 | A | 4.3: "1.186 yêu cầu còn lại không có bản ghi chặn nào được ghi, và điều phối không trần cũng từ chối 1.075 yêu cầu trong số này; điều đó không chứng minh chúng bị từ chối chỉ vì ràng buộc dịch vụ". Sổ D13 cần sửa (phụ lục 4). |
| CX3 | 477-481 | "2 trong 148" là số theo bản ghi được chọn của từng yêu cầu, không phải số khách | BUDPY:22,35-42,51-52 | A | 4.3: "phép phân tích chọn bản ghi có mức vượt nhỏ nhất … Chỉ ở 2 trong 148 bản ghi được chọn, khách nêu trong bản ghi đã dùng một phần trần trước đó". Sổ D19 cần sửa. |
| CX4 | 526-528 | Tách đổi chính sách (FREE → U) khỏi đổi trần; không gọi "điểm gãy" một ngưỡng chưa đo | X3-38; A17; K50; NEW:13; WP17 | A | 4.4: đoạn tập tắc đường cố định viết lại; "giữa hai mức đã chạy 60 và 120 giây, số lượt trễ tăng từ 0 lên 23". |
| CX5 | 124-126 | Dòng tập buổi sáng: "88 và 104" đếm cả cấu hình không liệt kê | RW7:5,33-34; RW7X:3-5,35-36 (17 × 8 = 136; 88 + 104 = 192) | A | Bảng tập thử: "136 (trong 192 lần chạy đã lưu)"; mức liệt kê đủ "30, 60, 90, 120, 150, 180, 240 và 300 giây" (C4A-07). Câu giải thích riêng của CX gộp vào ô bảng để giữ ngân sách. |
| CX6 | 459-466 | Ví dụ cơ chế là giờ trả dự kiến, không phải trễ đã xảy ra | W07XM:6,11,16; W07X:54 | M | Nhận ý chính; không dùng "khách trên xe" của văn bản CX (FC #124 đúng). 4.3: "giờ trả đang hứa của một khách đã lùi 79,0 giây…"; "Đây là phép tính trên giờ trả dự kiến của mô hình". |
| CX7 | 151-152; 283-285; 434; 503-504 | Báo tỉ lệ đủ mẫu số: câu mẫu số "không trễ"; chú thích trung bình theo kịch bản; tử số, mẫu số của tỉ lệ sổ; số đếm của tập tắc đường cố định; tử số theo kịch bản của tỉ lệ buổi sáng | ADD1; CK4A ledger-share-sums (23.027,239 / 31.353,407 …, khớp CX); CK4A fixed-shared-counts (865 …); WBU:4-16 (388 …) | M | Nhận: câu mẫu số ở 4.1.3; chú thích Bảng nghĩa vụ; tổng giây ở chú thích Bảng dời do điều phối (C4A-03); Bảng tắc đường cố định ghi số đếm và % (C4A-04). Không nhận phần "đưa tử số, mẫu số từng kịch bản vào phụ lục" cho tỉ lệ buổi sáng: phụ lục do chủ sở hữu giới hạn ≤ 3 trang; tỉ lệ đã ghi rõ "trung bình theo kịch bản" (output gốc W07X:20-29). |
| CX8 | 726-727; 770-771 | Chú thích bảng cộng dồn ghi phạm vi đã kiểm; ghi "sau khi bỏ bản chạy trùng" | ADDENDUM-1 mục 0.3; A:6,20; FJR:5-7 | A | Chú thích "… trên 140 lần chạy … đã được kiểm, thuộc bốn nhóm dưới đây"; câu tự tạo "sau khi bỏ bản chạy trùng, có 4 bản ghi trong 3 lượt quyết định". |
| CX9 | 143-145; 105; NOTES:59-69 | Mọi dữ kiện cần dòng sổ; ghi ngày cho 1.991; sửa A24, D13, D19 | INV:1 (08/10); X3-32; BUDPY | M | Thêm phụ lục 4 (20 dòng); "Bản kiểm kê ngày 08/10/2026 ghi 1.991 bản ghi lần chạy"; EV dùng X3-32 thay A24 "mỗi xe"; danh sách dòng sổ cần sửa ở cuối phụ lục 4. Câu "không dùng để tính các kết quả chính" của CX đổi thành "dành cho một phép hiệu chỉnh không dùng trong khóa luận" vì 15 kịch bản này không cho số nào của chương (chỉ được nhắc là chưa kiểm ở 4.5). |
| CX10 | 704-706; 686-692 | Thu hẹp câu "không mức trần nào tốt hơn ở mọi tiêu chí"; chú thích hình nói đường nối chỉ để theo dõi | D10; D03; L1a-09 | A | Mở 4.4: "Trong ba điểm đã đo trên tập kiểm tra chính, không điểm nào tốt nhất ở mọi chỉ số"; đoạn cuối 4.4 nêu đúng ba chênh lệch và "chỉ là một điểm đo thêm". Chú thích hình: "chỉ giúp theo dõi các điểm đã đo và không biểu diễn kết quả ở các mức chưa chạy". |
| CX11 | §3 (247-248) | Giá trị tính mới cho M⁺-60, V-30 | CK4A check (tính lại độc lập, khớp) | A | Bảng 4.4 điền (C4A-02). |
| CX12 | §4 (hình, khung b) | Khung (b) chỉ có bốn điểm | CAP:5,8-11; DIAL17:5,8-11 | A | Khung (b) và Bảng buổi sáng đủ tám mức (C4A-05). |
| CX13 | §6 | Bàn giao câu trả lời đệm cho phần B | PAD; A:7-9; ADD1 | A | Ghi ở NOTES §7 cho người viết phần B; phần A chỉ một câu trỏ (Q2). |
| CX14 | §7 | A24 "2 yêu cầu mới mỗi xe" sai; giới hạn áp cho cả lô | GEN:54-96 (X3-32) | A | Bảng tham số giữ "mỗi lượt quyết định xét tối đa 2 yêu cầu mới"; EV đổi sang X3-32; báo registrar. |
| CX15 | §2 (105) | "không dùng ở đây" quá rộng | Chương 3 v3 3.7 (382.006 lần sửa gồm 15 lần chạy hiệu chỉnh) | M | Xem CX9. |
| CX16 | §2 (143-146) | 1.991 không phải số hiện tại của kho | INV:1 | A | Xem CX9 (ghi ngày). |

**Codex:** 16 dòng — **A 12, M 4, R 0.**

---

## 3. Kiểm chứng sự kiện (FC)

| ID | Dòng | Nhận xét | Kiểm (anchor) | QĐ | Thay đổi trong v4 |
|---|---|---|---|---|---|
| FC#9 | 81 | 108 yêu cầu mỗi kịch bản chưa kiểm cho chiều tuyết | INV:14-15,17-22 ({108: 1} mỗi thư mục; được nhận 86…60 = 601) | A | Bảng tập thử: chiều tuyết "8 kịch bản, 864 yêu cầu" (C4A-06). |
| FC#14 | 88-89 | Bảng tham số "chung" sai cho tập tắc đường cố định | LAD:2-6; NEW:13 | A | Chú thích Bảng tham số: tập tắc đường cố định khác ở dòng tắc đường, bộ chạy cũ. |
| FC#15 | 90 (EV) | Trỏ X3-32 thay "R23 #105" | ADDENDUM-2 X3-32 | A | EV sửa. |
| FC#16 | 90-91 | Giới hạn bộ sinh của bộ chạy cũ chưa kiểm | NEW:13 (khác `policyVersion`, `solverExecution…`) | A | Chú thích: "có giới hạn bộ sinh và bộ giải chưa được kiểm lại" (C4A-18). |
| FC#35 | 139 (EV) | Trỏ X3-38 thay "R23 #51" | ADDENDUM-2 X3-38 | A | EV sửa; câu FREE giữ "chính sách chi phí cuốn chiếu mặc định" ở v2, v4 rút còn "không khóa gì và không qua bộ kiểm cam kết" (HO:109; A17; K50). |
| FC#40 | 158-159 | Phát lại đổi mọi giờ báo cho khách, chỉ số dùng $D_0$ | X3-11 (DISP:1-8); Chương 3 v3:552-553 | A | 4.1.3: "chỉ các giờ báo cho khách được tính lại theo dự báo, và các chỉ số dùng $D_0$". |
| FC#50 | 188-190 | Định nghĩa "phải phục hồi" sai mã; tên lệch Chương 3 | Q1 | A | Xem Q1. |
| FC#53 | 209 (EV) | X3-18 đã bỏ khỏi sổ | TEX08:136-137 (đã mở: "C1 … trần 30 giây cho tổng độ dời giờ trả") | A | EV → C4A-15. |
| FC#57 | 211-212 | Công bố thiếu: 120 giây chọn sau khi xem tập chính | Q3 | A | Xem Q3. |
| FC#64 | 247-248 | EXP có trễ quá 60 s của M⁺-60, V-30 | EXP:5-6; CK4A | A | Xem CX11. |
| FC#75 | 270-271 | Thêm "trung bình" cho chờ +0,5 s, ngồi −10,5 s | COM:2-3; `common_riders_check.py:29` | M | Nhận ở v2; v4 cắt cả câu vì ngân sách (NOTES §6 ý 7, có thể khôi phục với chữ "trung bình"). |
| FC#87 | 308-310 | "Đúng theo cấu tạo … luôn qua" bỏ giả thiết (N); U cũng 0/20.760 | Chương 3 v3:362-375; X3-16 | A | Xem CX1. |
| FC#90 | 313-315 | 36,5 / 75,6 / 1,0 / 5,0% là trung bình theo kịch bản, đặt ngay sau "Tính gộp" | ADD1:190,192 | A | 4.2 ghi "với trung bình theo kịch bản …" và "(cũng trung bình theo kịch bản)". |
| FC#91 | 315 | Câu 60 s chỉ đúng ở mức toàn tập | C13; T38:111 | A | "các tỉ lệ toàn tập giảm nhưng không về 0". |
| FC#120 | 453 | Vế "không có dự báo" không phải phép thử độc lập (dự báo chỉ phát lại) | F03; Chương 3 v3:552-553 | A | 4.3: "Giới hạn này không dựa vào dự báo, vì dự báo không đi vào bộ điều phối. Ở 13 kịch bản cuối tuần …". |
| FC#123 | 459-461 | 79,0 s là giờ trả đang hứa đã lùi, không phải khách đã tới muộn | W07XM:6 | A | Xem CX6. |
| FC#124 | 459-460 | "Đang trên xe" không có ở anchor gốc | W07X:54; W07XM:6 | A | Bỏ "đang trên xe". |
| FC#173 | 686-692 | CAP có đủ số cho các mức còn lại | CAP:5,8-11 | A | Xem CX12. |
| FC#176 | 704-705 | Như #57 ở 4.4 | Q3 | A | Đoạn cuối 4.4: "mức 120 giây được chọn sau khi đã xem tập kiểm tra chính". |
| FC#178 | 713-714 | "98 lần chạy cũ" trùng chữ "bộ chạy cũ" | A19; X3-10; NEW:1 | A | 4.5: "98 lần chạy trần 30–300 giây của tập kiểm tra chính và tập buổi sáng". |
| FC#186 | 726-727 | Tiêu đề bảng cộng dồn đọc như mọi lần chạy | ADDENDUM-1 mục 0.3 | A | Xem CX8. |
| FC#189 | 755-756 | Thiếu 12 lần chạy luật C trên thế giới đo thật của phép quét | SWEEP:13,70; B18; NEW:1 (`by_arm`) | A | 4.5: "… và 12 lần chạy luật C dùng hệ số đo được của một phép quét trước đó" (C4A-08); báo registrar sửa ADDENDUM-1 mục 0.3. |
| FC K-1…K-4 | — | Trùng #50, #87, #40, #178 | — | A | Như trên. |
| FC K-6 | — | `muc:c1-cauhoi`, `phuluc:A`, `phuluc:C`, `engelhardt2026` chưa có ở đâu | grep nhãn (script `labels.py` trong scratchpad phiên) | M | Không sửa được trong phần A; ghi ở NOTES §3, §8 cho người ghép. |
| FC K-11 | 58 | "(scenario)" trong câu | Chương 3 v3:35, 67 | A | Bỏ "(scenario)". |
| FC §3 | — | EV thiếu ở câu dẫn; anchor cũ (X3-18, R23 #…, RD …); thêm T38:12,94 | ADDENDUM-2; T38:12 | A | EV cho câu dẫn tập tắc đường cố định; anchor cũ thay; câu chạy lại trỏ C4A-17 (T38:12). |
| FC-OK | — | 187 mục AGREE, không con số nào sai | — | A | Giữ nguyên mọi số; chỉ đổi định nghĩa, phạm vi, nhãn. |

**Kiểm chứng sự kiện:** 27 dòng — **A 25, M 2, R 0.** (14 mục WRONG/OVERSTATED/LABEL/UNSUPPORTED: 13 A, 1 M; M còn lại là K-6, nhãn ngoài chương.)

---

## 4. Người đọc ngoài ngành và giảng viên (RL)

### 4.1 Người đọc (D1–D64)

| ID | Dòng | Nhận xét | Kiểm (anchor) | QĐ | Thay đổi trong v4 |
|---|---|---|---|---|---|
| D1 | 15-18 | Giải thích "ba phần", "hồ sơ lịch sử", "đệm" | OUTLINE §2 quy tắc 1 ("ba phần", không "nguyên nhân"); Chương 3 v3:589-590 | M | Mở chương: định nghĩa đệm; phần thứ nhất "gắn với việc ghép thêm khách"; trỏ `muc:so`. Không dùng "ba nguồn" như bản viết lại (OUTLINE cấm cách nói nhân quả). |
| D2 | 31-43 | Cột 3 Bảng lộ trình nhiều thuật ngữ chưa giải thích | — | M | Cột 3 viết lại bằng lời ("yêu cầu bị từ chối có phương án bị trần chặn; phép cộng các lần dời qua cả chuyến"). Giữ "quyết định bị ép" (tên Chương 3) thay cho "số lần luật loại hết phương án" của người đọc (sai theo Q1). |
| D3 | 56-57 | Bộ chạy, bộ chuyển đổi là gì | X3-15; X3-21 | A | Câu đầu 4.1.1. |
| D4 | 58-60 | Bỏ "(scenario)"; "mẫu" là gì; 108 lấy thế nào | B08 (mẫu r1–r4); J18 (mẫu 10% của một ngày); B02 | M | Bỏ tiếng Anh; "một trong bốn mẫu nhu cầu của ngày đó, mỗi mẫu gồm 10% số chuyến của ngày". **R** phần cách lấy 108 yêu cầu: không có dòng sổ (NOTES §5 ý 1). |
| D5 | 63-64 | "hệ số tắc đường đo" dễ đọc nhầm | — | M | "hệ số tắc đường đo được". Ví dụ 1,2 không thêm (Bảng thuật ngữ Chương 3 đã có). |
| D6 | 64-65 | "tất định" khó hiểu | B06 (sigma = shockRate = 0); B11 | M | "Thế giới mô phỏng không có nhiễu ngẫu nhiên, nên mỗi cặp … chạy một lần và cho một kết quả". Không viết "chạy lại cho đúng kết quả cũ": không có lần chạy lại mô phỏng nào trong sổ. |
| D7 | 65-66 | Diễn đạt trùng 3–20 yêu cầu; vì sao khung 17 giờ cũng trùng | B11; T38:93 ("cùng nguồn nhu cầu") | M | Diễn đạt lại "có chung 3 đến 20 trong 108 yêu cầu". **R** phần giải thích cơ chế: sổ không có. |
| D8 | 83-84 | "bao đóng" | PREF:22-26; B03; K48 | A | "96 nút là các điểm đi, điểm đến …; mỗi cặp nút có sẵn một thời gian đi. Đây là đồ thị rút gọn, không phải mạng đường phố". |
| D9 | 87 | Đã kiểm gì với dừng 0 giây | B05 | A | "0 giây: xe không mất thời gian khi khách lên, xuống (kiểm trên 3 lần chạy mẫu)". |
| D10 | 88-89 | "mức nền" | B07 | A | "tốc độ gốc của mọi kịch bản lấy theo hệ số lúc 00:00" (phỏng đoán của người đọc khớp B07). |
| D11 | 91 | "hạt giống" khó hiểu | Chương 3 v3:688 ("hạt giống ngẫu nhiên (số khởi tạo phần ngẫu nhiên)") | R | Đã định nghĩa ở Chương 3 v3; chỉ thêm "bằng 7". |
| D12 | 103-105 | "dựng được", "chia theo cặp", "hiệu chỉnh cái gì" | B08; SPLIT; C17 | A | "chia theo cặp ngày và mẫu để ba khung giờ của một cặp nằm cùng một phía … 15 kịch bản dành cho một phép hiệu chỉnh không dùng trong khóa luận". |
| D13 | 115-132 | Bộ chạy "bản lưu trữ / bản cũ"; "88 và 104"; dòng tuyết ghi lượt phục vụ | X3-10; NEW:13; C4A-07; C4A-06 | M | Câu giải thích bản đã lưu, bản cũ; "136 (trong 192 lần chạy đã lưu)"; tuyết "864 yêu cầu". Không đổi tên cột thành "Phiên bản bộ chạy" (câu giải thích đủ). |
| D14 | 137-140 | Danh sách ký hiệu U, C-$B$, M⁺-$B$, V-30, FREE | OUTLINE §1 ("symbols only in tables"); Chương 3 v3 Bảng luat | M | Ký hiệu giải nghĩa trong chú thích Bảng tập thử, không lập danh sách trong văn xuôi; bỏ "chi phí cuốn chiếu" khỏi văn xuôi v4. |
| D15 | 143-145 | Bao nhiêu lần chạy hỏng | T38:12; ADD1:6 | A | "(một lần ở tập kiểm tra chính)" (C4A-17). |
| D16 | 151 | Câu "chỉ trên khách được phục vụ" mâu thuẫn với "chia cho số yêu cầu" | ADD1:10-31 | A | Xem CX7. |
| D17 | 152-153 | "có phép so" là phép so nào | C08 | M | v2 có ví dụ +31 / −5; v4 trỏ sang `muc:c4-ketqua`, nơi câu mở nêu đúng phép so đó (tránh lặp, giữ ngân sách). |
| D18 | 153-155 | Ví dụ cho hai cách gộp | số học | A | Ví dụ dựng tay 5/10 và 5/90 → 10% và 27,8%. |
| D19 | 158-161 | "phép phát lại" là gì | F03; X3-11 | A | Xem FC#40. |
| D20 | 166-167 | "so sánh chặt" | `sweep_analyze.py`:107,128-129 | A | "``Quá'' nghĩa là lớn hơn hẳn: trễ đúng 60 giây không tính". |
| D21 | 175-176 | "đếm trên số yêu cầu" | C01 | A | "Số đếm; chia cho số yêu cầu thì ra tỉ lệ phục vụ". |
| D22 | 186, 191 | $c$, $z$ chưa định nghĩa trong chương | Chương 3 v3 eq:bamoc | A | Chú thích Bảng chỉ số nhắc lại $c$, $z$ và trỏ `muc:bamoc`. |
| D23 | 188-190 | Hai tên cho cùng khái niệm | Q1 | A | Xem Q1. |
| D24 | 191-193 | "chính luật" nghe như dịch máy | GLOSSARY-VI mục B ("phá lời hứa") | M | Giữ thuật ngữ "phá lời hứa" của bảng thuật ngữ; hàng và cột đổi thành "Khách bị phá lời hứa", định nghĩa "Khách mà luật đang dùng không giữ được điều nó hứa". |
| D-c1 | 4.1.3 | Một câu phân biệt khách, yêu cầu, lượt | — | A | "Một lượt phục vụ là một yêu cầu, tức một khách, được nhận và chở tới nơi". |
| D25 | 205-206 | "tập kịch bản tĩnh" không có trong Bảng 4.3 | K29; C4A-15 | M | "tập kịch bản tĩnh của đợt thử trước, nơi thời gian đi không đổi (Phụ lục A)". Không ghi "20 kịch bản" (không có dòng sổ). |
| D26 | 211-212 | "tập phát triển" chưa định nghĩa | T38:8; Q3 | A | "sau khi đã xem tập buổi sáng và các đợt chạy thử trước đó", và câu công bố 120 giây. |
| D27 | 220-222 | Chữ "nên" gây khựng | C02; C06; C08 | A | Câu mở 4.2 sắp lại (Q2); giải thích "vì phục vụ bớt 96 lượt nhưng trễ bớt 127 lượt". |
| D28 | 225-226 | "phần hạn chót" là phần nào | J10; A09 | A | "giờ trả mới không được muộn hơn lời hứa đầu quá 30 hoặc 60 giây, thay vì 900 giây của họ". |
| D29 | 234-241 | "tính trên 3.672" cho cột số đếm | — | A | Chú thích: "số lượt phục vụ không trễ quá ngưỡng; chia cho 3.672 thì ra tỉ lệ trên yêu cầu". |
| D30 | 247-248 | "chưa đưa vào bảng" trông dở dang | Bất đồng #3 | M | Điền trễ, không trễ; "chưa đếm" chỉ ở cột đi chung. |
| D31 | 258-259 | Lẫn "điểm phần trăm" và "%" | C02 | A | "tỉ lệ phục vụ giảm 2,6 điểm phần trăm (96 trên 3.672 yêu cầu), tức ít hơn 3,9% số lượt của điều phối không trần (96 trên 2.434)". |
| D32 | 265-266 | Công thức dấu âm lồng nhau | — | A | "127 − 96 = 31". |
| D33 | 270-271 | Chủ ngữ sai; trung bình hay trung vị; "tập khách hình thành sau khi áp luật" | COM:2-3 | M | Sửa ở v2; v4 cắt câu vì ngân sách (NOTES §6 ý 7). |
| D34 | 274-278 | "không phải cùng mọi khách"; "nghĩa vụ" trừu tượng | K07 | A | "không hoàn toàn cùng những khách"; "mỗi luật có giữ được điều chính nó hứa hay không". |
| D35 | 308-311 | "đúng theo cấu tạo" cần ví dụ | Chương 3 v3:446-447 (ví dụ 40 giây) | M | "không phải phát hiện thực nghiệm" + trỏ ví dụ 40 giây đã có ở Chương 3 thay cho ví dụ mới (giữ ngân sách). |
| D36 | 314-315 | 1,0% và 5,0% của chỉ số nào | ADD1:190,192 | A | "chỉ 5 trong 11 kịch bản có khách bị phá, với 1,0% và 5,0% (cũng trung bình theo kịch bản)". |
| D37 | 318-320 | Diễn đạt trừu tượng | C13; K05 | A | Đoạn viết lại kèm số so được (C4A-01). |
| D38 | 343 | 11 phút và 3,87 phút khác độ chính xác | CON:4,11 | A | "Trễ lớn nhất (s)": 660,1 và 232,3 (C4A-14). |
| D39 | 354-356 | Viết "họ trễ vì đường đông hơn lúc hứa…" | K39; C21 | M | Nhận "nhắm tới phần đoán được của loại trễ này". **R** câu nguyên nhân: K39 cấm "trễ thuần vì kẹt xe"; sổ chỉ cho biết không có lần dời do điều phối được ghi. |
| D40 | 364-366 | "không ít hơn" so với cái gì | N-22 | A | Bảng bị bỏ (bất đồng #4); câu văn ghi "bằng hoặc nhiều hơn". |
| D41 | 434 | Nhãn dòng khó đọc nhất | C24; C4A-03 | A | "Phần tính cho điều phối trong tổng giây trễ của các khách trễ quá 60 s (%)", định nghĩa và tổng giây ở chú thích. |
| D42 | 445-446 | 1 ms có thật không; 33 có nên là 29 | Q4 (b) | CC | Giữ "đúng 1 mili giây" và 33 theo định nghĩa (C4A-19). |
| D43 | 447-450 | "giao của hai tập", "hai phần kia của sổ" | C21; C24 | A | "con số chỉ cho biết hai nhóm trùng nhau, không cho biết việc bị dời là nguyên nhân của độ trễ". |
| D44 | 453 | "ngày có sự kiện" mơ hồ; "trần vẫn giữ" | N-28; N-26 | A | Xem FC#120; "chiều tuyết (bộ chạy chưa kiểm lại)". |
| D45 | 459-466 | Ví dụ quá dày, chia bước | W07XM:6 | M | Chia bước; **R** "khách đang ngồi trên xe" (FC#124). |
| D46 | 469-474 | Định nghĩa bản ghi chặn; "lý do cấu trúc" | X3-05; BUDPY | M | Thêm câu định nghĩa; bỏ "lý do cấu trúc" (CX2). **R** "[các ràng buộc khác, ví dụ …]": phép phân tích không xác lập lý do. |
| D47 | 477-482 | Bốn thuật ngữ mới; 109,6 s là gì | Q4 (a) | A | Viết lại bằng lời; "tức phần vượt quá 30 giây"; hai lẽ của lời rào. |
| D48 | 489 | "đơn điệu" | — | A | Câu mở 4.4 mới. |
| D49 | 494-495 | Ba câu hỏi nào | — | A | Câu nêu việc của từng tập. |
| D50 | 498-499 | Câu dẫn bảng | — | A | "xếp các cấu hình từ lỏng nhất (ghép tự do) tới chặt nhất (trần 30 giây)". |
| D51 | 527-528 | "bộ chạy cũ" | NEW:13 | A | Giải thích ở 4.1.2. |
| D52 | 560-561 | "cận trên" | K12 | A | "không phải mức phục vụ cao nhất có thể đạt, chỉ là một điểm đo". |
| D53 | 566-568 | Bảy số ghép bảy mức | D04 | M | Bất đồng #5. |
| D54 | 609-613 | "điểm đầu mút"; tách phần dự báo | L1a-09 | A | "nhiều hơn cả trần 30 giây lẫn điều phối không trần"; câu dự báo riêng. |
| D55 | 616 | "90% trần" | N-07 | A | "9 khách bị dời từ 108 giây trở lên (90% của trần)". |
| D56 | 621 | "chung, riêng" | N-10 | A | "2.266 khách được cả hai mức trần phục vụ, 121 khách chỉ được trần 120 giây và 72 khách chỉ được trần 30 giây phục vụ". |
| D57 | 629-694 | Nhãn trục dọc cả ba khung; chú thích nói ngưỡng 120 s đổi chiều | STYLE quy tắc 22 ("Chú thích không thêm kết luận mà hình không thể hiện") | M | Thêm nhãn trục dọc cho (b), (c). **R** câu kết luận trong chú thích (hình chỉ vẽ ngưỡng 60 s); văn xuôi sau hình nêu điều đó. |
| D58 | 704-706 | "phép dò tìm" mơ hồ | K36 | A | "trần 120 giây chỉ là một điểm đo thêm trên đường đánh đổi"; câu mở 4.4 nói không điểm nào tốt nhất. |
| D59 | 713-715 | Không biết mục trả lời câu hỏi gì, tốt hay xấu | E01; N-08 | A | Câu mở 4.5: câu hỏi và câu trả lời bằng lời ("hiếm khi chỉ riêng phép cộng ấy làm một phương án bị loại"). |
| D60 | 718-722 | Ví dụ ở quá xa định nghĩa | N-27 | A | Ví dụ 25,844 + 99,027 = 124,871 giây ngay sau định nghĩa. |
| D61 | 753-757 | "được xác nhận"; "đưa dự báo vào bộ điều phối" | X3-13; F12 | A | "được xác nhận" định nghĩa ở Bảng chỉ số ("đã được bộ mô phỏng xác nhận áp dụng"); "16 lần chạy trong đó bộ điều phối dùng dự báo khi quyết định (khác phép phát lại)". |
| D62 | 768-771 | "hai chỗ có dấu vết"; kiểu tắc đường tự tạo là tập nào | FJC:46; FJR:5-7; SWEEP:8-14 | M | "bản ghi chỉ do cộng dồn còn có ở hai nơi"; tự tạo = "phép quét trước đó" (C4A-08). Không thêm phép quét vào Bảng tập thử: chương không lấy kết quả từ nó, chỉ nêu phạm vi. |
| D63 | 774-780 | Nhiều thuật ngữ khó | E06; E08; E09 | A | Viết lại bằng lời ("Tính thử cả hai cách …", "Phép tính thử không cho biết kết quả nếu chạy thật …"). |
| D64 | 782 | "ưu tiên ổn định" | A14; X3-07 | A | "tức bộ chọn xét mức dùng trần và phần dời trước chi phí kế hoạch (Bảng rangbuoc)". |
| D-c2 | chung | Bảng dùng "s", văn dùng "giây" | STYLE quy tắc 26 | R | Giữ quy ước: bảng ghi "s" ở tiêu đề, văn xuôi viết "giây". |

### 4.2 Bốn câu người đọc không tóm được

| ID | Câu hỏi | QĐ | Thay đổi |
|---|---|---|---|
| RQ1 | Cần luật C làm gì nếu đệm cũng cho số lượt đúng giờ tương tự | M | Q2. |
| RQ2 | Dự báo tác dụng tới đâu (76 → 10) | M | Chú thích Bảng trần 120 nói khối dưới là phát lại và trỏ `muc:c4-dubao`; **R** bàn trong phần A (OUTLINE: 4.7). |
| RQ3 | Vì sao điều phối không trần cũng từ chối 1.238 yêu cầu | A | Mở 4.3: số yêu cầu bị từ chối "tăng từ 1.238 lên 1.334"; đoạn từ chối nêu điều phối không trần cũng từ chối 1.075 trong 1.186. |
| RQ4 | Bốn khách bị dời 1 ms có thật không | CC | Q4 (b). |

### 4.3 Giảng viên (G1–G6)

| ID | Nhận xét | Kiểm | QĐ | Thay đổi |
|---|---|---|---|---|
| G1-d1 | Cách lấy 108 yêu cầu; "mẫu" | B02; B08 | M | Như D4. |
| G1-d2 | Vì sao 49 kịch bản, luật chia 34/15 | B08; SPLIT | A | Như D12. |
| G1-d3 | Ba nguồn số liệu ngoài bốn tập | K29; F12; FJC:46 | M | "kết quả của chương chỉ lấy từ bốn tập …; các đợt chạy khác chỉ được nhắc khi nêu phạm vi kiểm tra"; tập tĩnh nêu ở 4.1.4 kèm phụ lục. |
| G1-d4 | Chiều tuyết: số yêu cầu, bộ chạy chưa kiểm | INV; X3-10 | A | 864 yêu cầu; lưu ý "bộ chạy chưa kiểm lại" ở 4.1.2, 4.3 và Bảng cộng dồn (EV). |
| G1-r1 | "88 và 104" | RW7; RW7X | A | CX5. |
| G1-r2 | Độ nhạy hạt giống; bằng chứng "tất định" | B11; L1a-04 | R | Không có lần chạy lại mô phỏng nào trong sổ; không viết. Ghi cho 4.11 (NOTES §7) và câu hỏi mở. |
| G1-r3 | Ba phiên bản bộ chạy | NEW:13; X3-10 | A | Không đổi (bản 1 đã nói không cộng gộp); thêm câu giải thích bản đã lưu, bản cũ. |
| G1-m1 | $c$, $z$ | — | A | D22. |
| G1-m2 | $p_0$ tính thế nào; so độ dài lời hứa đầu U và C-30 | A13; A05; B14 (BURD:5,11) | A | Đoạn mới ở 4.1.3: 14,15 so với 14,12 phút, "nên luật C không hứa xa hơn điều phối không trần". |
| G1-m3 | Chỉ số tới sớm định nghĩa nhưng không dùng | C4A-13; N-16 | A | Hai dòng "Lượt tới sớm quá 60 s" ở Bảng trần 120 (7/3/1; 8/4/2) và câu đọc bảng. |
| G1-m4 | Dừng 0 giây vào phần hạn chế | B05 | A | Bàn giao cho 4.11 (NOTES §7). |
| G1-s1 | "tính trên 3.672" cho cột số đếm | — | A | D29. |
| G1-s2 | Độ dài thêm có gồm khách cuối tuần (bằng 0) | ADD1:14,19,24 (`ext_sum / served`) | A | Chú thích Bảng trần 120 và Bảng chỉ số: "kể cả khách không có dự báo / khách cuối tuần có độ dài thêm bằng 0". |
| G1-s3 | 38,35% cạnh 12,4% làm tròn khác nhau | STYLE quy tắc 27 | A | "38,4%". |
| G1-t | Nêu +31 = 0,84% số yêu cầu | — | R | Câu mở đã nêu +31 và −5 kèm số tuyệt đối; thêm một tỉ lệ nữa không đổi kết luận, tốn chỗ. |
| G2-4.2 | Câu mở nhấn con số yếu nhất | Q2 | A | Q2. |
| G2-4.3 | Câu mở chỉ nói "chặn gì" | D13; C01 | A | Thêm câu cái giá (1.238 → 1.334; 148 có phương án bị trần chặn). |
| G2-4.4 | Kết luận ở cuối mục | — | A | Đưa lên đầu. |
| G2-4.5 | Không có kết luận bằng lời | — | A | D59. |
| G3-c1 | "Cái giá của trần là … 1.334" gợi nhân quả | C01; D13 | A | RQ3. |
| G3-c2 | "Trần vẫn giữ …" như độ bền | F03 | A | FC#120. |
| G3-c3 | "Phần trễ này là phần mà dự báo nhắm tới" | K39 | A | "nhắm tới phần đoán được của loại trễ này". |
| G3-m1 | "mọi ngưỡng" | N-24 | A | "cả bốn ngưỡng đã đo, từ 1 tới 10 phút". |
| G3-m2 | "mọi mức" | D04 | A | "Ở cả tám mức". |
| G3-u | "hai điểm đầu mút" | K12 | A | D54. |
| G3-h1 | "U phục vụ 116 trong 148" dễ đọc thành mất 116 khách | D13; K10 | M | Đoạn ngay sau có lời rào "Không thể kết luận …" và câu bản ghi chặn không phải khách; không thêm câu riêng (ngân sách). |
| G3-h2 | 7,27 so với 7,37 giây trên hai tập khách | N-10 | A | "trên hai tập khách khác nhau". |
| G3-f | Bảng nghĩa vụ so không cân: đánh dấu 0 theo định nghĩa; số so được | N-21; CK4A | A | Chú thích: "các số 0 là điều Nhận xét cho trước dưới giả thiết (N)"; đoạn số so được 292 so với 289 (C4A-01). Kết quả xác nhận phỏng đoán của giảng viên: hai luật để khách trễ gần như ngang nhau. |
| G4 | Phần A chưa trả lời câu hỏi đệm | Q2 | M | Q2. |
| G6-1 | Trả lời câu hỏi đệm trong phần A, đổi trọng tâm câu mở | Q2 | M | Q2 (đổi trọng tâm: A; đoạn đệm đầy đủ: R, để 4.8). |
| G6-2 | Bảng 4.6 so cân | G3-f | A | G3-f. |
| G6-3 | Điền hoặc bỏ hai dòng; bình V-30 | C4A-02; A11; A12 | M | Điền; một câu "Luật trần độ dời khách thấy bị ép nhiều nhất, phù hợp với định nghĩa …" (không nhân quả). |
| G6-4 | Đối chiếu phạm vi dữ liệu, số lần chạy | — | A | CX5, G1-d3, G1-d4. |
| G6-5 | Bổ sung thiết lập để chạy lại | — | M | Nhận: mẫu, cách chia, độ dài $p_0$, dừng 0 giây (sang 4.11). Không viết: cách lấy 108 yêu cầu, bằng chứng chạy lại (không có dòng sổ). |
| G6-6 | Khung "Ký hiệu và thuật ngữ của chương" | STYLE quy tắc 7 (một hộp mỗi chương, dành cho kết luận chính) | M | Không thêm hộp (ngân sách, quy tắc 7); ký hiệu ở chú thích Bảng tập thử, thuật ngữ định nghĩa ở lần đầu; "bị ép" thống nhất. |
| G6-7 | Kết luận 4.4 lên đầu; dãy bảy tỉ lệ vào bảng; Bảng 4.11 đủ tám mức | D04; C4A-05 | M | Kết luận lên đầu (A); bảng buổi sáng đủ tám mức (A); dãy tỉ lệ không vào bảng (bất đồng #5). |
| G6-8 | (a) dòng 469; (b) 109,6 s; (c) 1 ms | Q4 | M | (a) A; (b) A; (c) CC. |
| G6-9 | Kết luận bằng lời cho 4.5 | — | A | D59. Câu "trần từng lần cũng chặn gần như cùng phương án" có ở v2, cắt ở v4 (ngân sách); đoạn định nghĩa vẫn nói luật mỗi lần một trần chưa chạy. |
| G6-10 | "mọi"; khung 7 giờ; 61/76 ở khung 7 giờ | N-11; N-22 | A | "ở khung 7 giờ, luật C ít hơn ở 3 kịch bản và bằng ở 6"; "61 người thuộc khung 7 giờ". |
| G6-11 | Chú thích khối có dự báo | ADD1 | A | G1-s2, RQ2. |
| G6-12 | Viết lại các câu khó; bỏ "(scenario)" | — | A | D-items; FC K-11. |
| G6-13 | Giảm tải bảng; nhãn trục; chú thích 120 s | — | M | Bảng ngày × khung bỏ khỏi thân bài (bất đồng #4); nhãn trục thêm; câu chú thích 120 s không nhận (D57). |

**Người đọc:** 70 dòng (D1–D64, D-c1, D-c2, RQ1–RQ4) — **A 44, M 22, R 2, CC 2.** **Giảng viên:** 42 dòng — **A 29, M 11, R 2.**

---

## 5. Đếm theo người nhận xét

Đếm từng dòng của các bảng trên, mỗi dòng một quyết định (dòng gộp "FC K-1…K-4" tính một; 187 mục AGREE của kiểm chứng sự
kiện gộp thành dòng "FC-OK").

| Người nhận xét | Số dòng | A | M | R | CC |
|---|---:|---:|---:|---:|---:|
| Codex (CX1–CX16) | 16 | 12 | 4 | 0 | 0 |
| Kiểm chứng sự kiện (FC) | 27 | 25 | 2 | 0 | 0 |
| Người đọc (D1–D64, D-c1, D-c2, RQ1–RQ4) | 70 | 44 | 22 | 2 | 2 |
| Giảng viên (G1–G6) | 42 | 29 | 11 | 2 | 0 |
| **Tổng** | **155** | **110** | **39** | **4** | **2** |

Dòng M: CX6, CX7, CX9, CX15; FC#75, FC K-6; D1, D2, D4–D7, D13, D14, D17, D24, D25, D30, D33, D35, D39, D45, D46, D53,
D57, D62, RQ1, RQ2; G1-d1, G1-d3, G3-h1, G4, G6-1, G6-3, G6-5, G6-6, G6-7, G6-8, G6-13.
Dòng R: D11, D-c2, G1-r2, G1-t. Dòng CC: D42, RQ4.

## 6. Các nhận xét không nhận (R), lý do và anchor

1. **D11** (giải thích lại "hạt giống ngẫu nhiên"): đã định nghĩa ở Chương 3 v3:688.
2. **D-c2** (đổi "s"/"giây"): STYLE quy tắc 26 quy định "s" trong bảng, "giây" trong văn.
3. **G1-r2** (nói đã chạy lại những lần nào và ra đúng số cũ): không có lần chạy lại mô phỏng nào trong sổ (L1a-04 chỉ đọc lại
   transcript; B11 chỉ nói mỗi tổ hợp một lần chạy tất định) — không thể viết khi chưa có bằng chứng.
4. **G1-t** (thêm +31 = 0,84% số yêu cầu): câu mở đã nêu +31 và −5 bằng số đếm; con số thêm không đổi kết luận, tốn chỗ.

Các phần không nhận bên trong một dòng M (lý do ghi ở dòng đó): cách lấy 108 yêu cầu và cơ chế trùng yêu cầu giữa các khung
(D4, D7: không có dòng sổ); câu nguyên nhân "họ trễ vì đường đông" (D39: K39, C21); "khách đang ngồi trên xe" (D45, CX6:
W07X:54, W07XM:6); "[các ràng buộc khác]" (D46: BUDPY:29-44); câu kết luận trong chú thích hình (D57: STYLE quy tắc 22); dãy
tỉ lệ trung bình theo kịch bản trong bảng số gộp (D53: OUTLINE §2 quy tắc 3); hộp ký hiệu riêng (G6-6: STYLE quy tắc 7, ngân
sách); đoạn đệm đầy đủ trong 4.2 (G4, G6-1: OUTLINE-V2:197); tử số theo kịch bản trong phụ lục (CX7: phụ lục ≤ 3 trang);
bàn kết quả dự báo 76 → 10 trong phần A (RQ2: OUTLINE 4.7).

## 7. Không kiểm được (CC)

- **D42 / RQ4 / G6-8c:** nguyên nhân của bốn lần dời sớm đúng 1 mili giây. Mã cho thấy phần làm tròn ở cạnh đang đi như nhau
  cho $e$ và $p$ (RSP:80-90); giả thuyết làm tròn từng cung chưa kiểm trên bốn trường hợp. Giữ cách viết cũ (C4A-19).

## 8. Số mới thêm vào chương (đều có script hoặc dòng đọc, và dòng sổ C4A)

C-30 trễ quá 30 giây 292 / 2.338 (12,5%; TB theo kịch bản 14,6%; 28 kịch bản) so với M⁺-30 289 (C4A-01); M⁺-60, V-30 trễ
và không trễ (C4A-02); tử số, mẫu số tỉ lệ sổ (C4A-03); số đi chung và bị dời của tập tắc đường cố định (C4A-04); năm mức
buổi sáng còn thiếu (C4A-05); 864 yêu cầu chiều tuyết (C4A-06); 136 trong 192 lần chạy (C4A-07); tới sớm 7 / 3 / 1 (C4A-13);
trễ lớn nhất 660,1 / 232,3 giây (C4A-14). Dùng lần đầu từ sổ có sẵn: B14 (14,15 / 14,12 phút), D13 (1.075), N-11 (61/76),
X3-16 (0 / 20.760), N-16 (8 / 4 / 2).

*Hết. Viết bởi Claude (người sửa Chương 4 phần A), 2026-10-12.*
