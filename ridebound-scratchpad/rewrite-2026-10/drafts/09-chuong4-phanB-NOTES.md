# 09-chuong4-phanB — NOTES của người viết (2026-10-12)

**Bản nộp: `drafts/09-chuong4-phanB-v7.tex`** (497 dòng). Phần B gồm các mục 4.6–4.11, nối ngay sau
`08-chuong4-phanA.tex` trong cùng `08-chuong4.tex` (không có `\chapter` mới).

Đã đọc theo thứ tự của brief: WRITING-BRIEF; OUTLINE-V2 (§2, §5 Chương 4, §7.2, §8, §9); REVIEW-DECISIONS-R20 (toàn bộ, gồm
§8); STYLE-GUIDE-VI; GLOSSARY-VI; EVIDENCE-REGISTER (toàn bộ); ADDENDUM-1 (mục 0 trước); ADDENDUM-2-CH3; C120-RESULTS;
phần A và NOTES của nó; chương 3 v3; R25-CH4A-REVIEW-CODEX (toàn bộ, §5–§7 kỹ). Đọc thêm phần cuối của
`reviews/R25-READER-LECTURER-CH4A-CLAUDE.md` (G1–G6, các ý về câu hỏi đệm) và tệp mới
`evidence/TESTRUN-45f8026-2026-10-12.md` (xuất hiện trong lúc làm việc). Mẫu DACN không mở lại: STYLE-GUIDE đã trích đủ.

Đã chạy: chỉ lệnh đọc (`cat`, `grep`, `sed`, `ls`, `diff`) và một script đếm chữ, kiểm ngoặc chỉ đọc trong scratchpad
phiên (`count_ch4b.py`). Không mô phỏng, không build, không cài, không xóa. **Chưa biên dịch thử LaTeX** (build bị cấm);
người ghép cần chạy `tectonic` một lần.

---

## 1. Các tệp đã tạo và vì sao có nhiều bản

Mạng bị ngắt giữa chừng; khi tiếp tục, chưa có tệp đầu ra nào. Theo yêu cầu "không ghi đè, viết bản mới có hậu tố",
mỗi lần sửa tôi tạo một tệp mới. Không bản cũ nào bị sửa hay xóa.

| Tệp | Tiếng văn xuôi | Vì sao không dùng |
|---|---:|---|
| `09-chuong4-phanB.tex` (bản 1) | 4.778 | Vượt ngân sách xa; 36 câu trên 40 tiếng |
| `09-chuong4-phanB-v2.tex` | 3.949 | Vẫn vượt; 16 câu trên 40 tiếng |
| `09-chuong4-phanB-v3.tex` | 3.729 | Vẫn vượt; 17 câu trên 40 tiếng |
| `09-chuong4-phanB-v4.tex` | 3.475 | **Sai một ý** ở 4.11: kể "không lượt quyết định nào phải phục hồi" là điều luật C đổi được so với điều phối không trần, trong khi điều phối không trần cũng 0 trong 20.760 lượt (X3-16; chương 3 `nx:giunguyen` nói tính chất này không riêng của luật C) |
| `09-chuong4-phanB-v5.tex` | 3.541 | Mất hai tham chiếu bảng (`bang:c4-sangloc`, `bang:c4-dubao`) khi cắt; Bảng 4.11, 4.13–4.15 có thể tràn lề 16 cm; chú giải hình chồng chữ |
| `09-chuong4-phanB-v6.tex` | 3.570 | Hai tỉ lệ của phép sàng lọc (18,95%, 10,08%) mất số đếm; thiếu nhãn "gộp theo khách" ở phép thử học máy; 25,7% chưa ghi mẫu số |
| **`09-chuong4-phanB-v7.tex`** | **3.605** | **Bản nộp.** Khác v6 đúng sáu chỗ (xem `diff`): số đếm 445/1.714, 325/1.715, 173/1.716, 104/1.715; "mức 0,17% của 21 kịch bản"; "(gộp theo khách)"; "25,7% của 3.445,9 giây"; tham chiếu `bang:c4-phanbotre` ở 4.11; dòng đầu tệp |
| `evidence/EVIDENCE-REGISTER-ADDENDUM-3-CH4B.md` | — | 14 dòng N4B-01…N4B-14. Phần đầu tệp ghi "bản nộp v6"; v7 dùng đúng các mã đó, không thêm dữ kiện mới |
| `09-chuong4-phanB-NOTES.md` | — | Tệp này |

Bản 1 đến bản 7 có cùng số liệu, cùng nhãn, cùng bảng và hình (trừ cách xuống dòng tiêu đề cột từ v6); chỉ lời văn khác.

## 2. Độ dài theo mục so với ngân sách (bản v7)

"Tiếng" = token cách nhau bởi khoảng trắng, sau khi bỏ dòng `%`, bảng, hình, lệnh LaTeX. Bảng và hình ước theo số dòng in
(như phần A). Hai thước:
- **thước của brief:** 330 tiếng văn xuôi mỗi trang;
- **mật độ đo được** của luận văn hiện tại mà phần A dùng (480–560 tiếng/trang; ở đây lấy 500).

| Mục | Ngân sách (tr.) | Văn xuôi (tiếng) | Bảng, hình (tr.) | Ước lượng theo thước brief | Ước lượng theo mật độ đo |
|---|---:|---:|---|---:|---:|
| 4.6 Vai trò của trần | 1,2 | 396 | Bảng 4.11 ≈ 0,50 | 1,75 | 1,34 |
| 4.7 Lời hứa theo dự báo | 3 | 942 | Bảng 4.12 ≈ 0,35; Hình ≈ 0,35 | 3,60 | 2,63 |
| 4.8 So với cách đệm | 2,75 | 738 | Bảng 4.13 ≈ 0,50; Bảng 4.14 ≈ 0,45 | 3,24 | 2,48 |
| 4.9 Chiều tuyết | 1 | 288 | Bảng 4.15 ≈ 0,50 | 1,42 | 1,13 |
| 4.10 Tính hợp lệ | 1,25 | 452 | — | 1,42 | 0,95 |
| 4.11 Thảo luận, hạn chế | 2 | 789 | — | 2,44 | 1,63 |
| **Tổng** | **11,2** | **3.605** | ≈ 2,65 | **≈ 13,9** | **≈ 10,2** |

Theo thước của brief, phần B vượt khoảng 2,7 trang (≈ 24%); theo mật độ đo được, nó nằm dưới ngân sách. Đây là ước lượng,
không phải bố cục đo. Danh sách cắt ở mục 9 bớt được khoảng 550 tiếng (≈ 1,7 trang theo thước brief) mà không mất ý bắt
buộc nào của outline.

Câu: 157 câu, trung vị 23 tiếng; 2 "câu" trên 40 tiếng: câu dự phòng bắt buộc của OUTLINE §7.2 (47 tiếng, giữ nguyên văn)
và danh sách bốn điều kiện của phép thử học máy (máy đếm cả danh sách là một câu).

Dòng `% EV:`: 56 (4.6: 8; 4.7: 15; 4.8: 15; 4.9: 6; 4.10: 6; 4.11: 6), mỗi đoạn có sự kiện một dòng, mỗi nhóm hàng bảng
một dòng.

## 3. Nhãn

**Phần B định nghĩa** (đều có tiền tố `c4-`, không trùng nhãn của phần A hay chương 3):
- Mục: `muc:c4-vaitro` (4.6), `muc:c4-dubao` (4.7), `muc:c4-dem` (4.8), `muc:c4-tuyet` (4.9), `muc:c4-hople` (4.10),
  `muc:c4-thaoluan` (4.11).
- Bảng: `bang:c4-sangloc` (sàng lọc bộ chọn, "Bảng 4.11" của outline), `bang:c4-dubao` (dự báo trên 21 kịch bản, 4.12),
  `bang:c4-dem` (các cách hứa, 4.13), `bang:c4-haiphia` (hai phía và phần đuôi, 4.14), `bang:c4-tuyet` (chiều tuyết, 4.15).
  Chương 3 đã có `bang:dubao` (giả mã), nên bảng của 4.7 là `bang:c4-dubao`.
- Hình: `hinh:c4-so` (H4.3 của outline, sổ ba phần ngày thường và chiều tuyết).

**Nhãn ngoài phần B được tham chiếu (đã có):** chương 3: `bang:rangbuoc`, `muc:dubao`, `eq:so`, `muc:gioihan`,
`muc:kiemtra`; phần A: `bang:c4-tran120`, `bang:c4-nghiavu`, `bang:c4-doidieuphoi`, `bang:c4-phanbotre`,
`muc:c4-congdon`.

**Ai tham chiếu nhãn của phần B:** `muc:c4-vaitro` (chương 3 dòng 471; phần A dòng 16, 37, 783), `muc:c4-dubao` (chương 3
dòng 557; phần A 17, 42, 356), `muc:c4-dem` (phần A 17, 37, 613), `muc:c4-tuyet` (phần A 18, 42), `muc:c4-hople` (chương 3
dòng 468, 689; phần A 32), `muc:c4-thaoluan` (chỉ trong phần B).

**Lời hứa mà chương 3 đặt cho `muc:c4-hople` đã được giữ:** mức dùng trần lớn nhất bằng 100% ở các lượt đã ghi (chương 3
dòng 467-468) và các bộ đếm cho biết giới hạn có cắt bớt phương án hay không (chương 3 dòng 689).

**Trích dẫn:** `engelhardt2026`, `horl2022`, `schulz2026` (đều đã dùng ở chương 3; hai khóa đầu là khóa mới do người viết
chương 3 đề xuất, metadata ở ADDENDUM-2 X3-40). Không thêm tài liệu mới.

Số bảng in dự kiến: phần A có 13 bảng (4.1–4.13) và Hình 4.1, nên các bảng của phần B in thành 4.14–4.18 và hình thành
Hình 4.2 (đánh số tự động).

## 4. Bảng, hình và nguồn dữ liệu (siêu dữ liệu theo OUTLINE §2 quy tắc 9)

| Nhãn | Cấu hình | Kịch bản | Đơn vị, mẫu số, cách gộp | So sánh | Dòng sổ | Output |
|---|---|---|---|---|---|---|
| `bang:c4-sangloc` | U (LOCKS), C-30; tỉ lệ đổi của C-120, C-60 ở văn xuôi | Tập tắc đường cố định, 16 kịch bản mỗi cấu hình | Lượt quyết định được xác nhận có yêu cầu mới; ba ước lượng chi phí; dời thêm cộng trên đội xe (s) | Hai tập trạng thái khác nhau | H03–H06, K15–K17, N4B-01, N4B-02 | WP17; PV; NEW:6; CASE |
| `bang:c4-dubao` | C-30 | 21 kịch bản ngày thường có dự báo (khung 7 / 8 / 17 giờ: 8 / 8 / 5) | `[TB theo kịch bản]`; trễ "> 60 s", sớm "< −60 s" | Không dự báo / đệm cùng giá / dự báo | F04, N4B-03 | FR:40-46; FA:8-11 |
| `hinh:c4-so` | C-30 | 21 kịch bản ngày thường; 8 kịch bản chiều tuyết | Giây trễ của khách có a − p₀ > 60 s; 100% mỗi thanh | Ba phần của sổ | F09, F13, N4B-05 | FA:30; RX:3; NEW:5; RP1:24-26; SNOW:10 |
| `bang:c4-dem` | U, C-30, C-120 có dự báo; U, C-30 có dự báo + 30 s; U có dự báo + 60 s | 34 kịch bản, 3.672 yêu cầu mỗi cấu hình | `[đếm]`; "không trễ quá" `[trên yêu cầu]`; dài thêm `[gộp theo khách]` | Ba khối theo độ dài thêm | C09–C11, N-02, N-03, N-06, N-16 | ADD1:12-26; A:7,9 |
| `bang:c4-haiphia` | Như trên (6 hàng) | 34 kịch bản | `[đếm]` trong số khách được phục vụ; ±60 s `[trên yêu cầu]` | Hai phía, phần đuôi | N-01–N-04, N4B-09 | ADD1:14-26, 84-89; A:7,9 |
| `bang:c4-tuyet` | C-30, 7 cách hứa | 8 kịch bản chiều tuyết, 601 khách | Khách trễ `[đếm]`; dài thêm `[TB theo kịch bản]` | Các cách phát lại | F14, N4B-06 | RP1:6-20; NEW:5 |

**Tọa độ của `hinh:c4-so`** (tính tay, thanh dài 11 cm): ngày thường, tổng 6.217,4 s (FA:30): điều phối 81,7 / 6.217,4 × 11
= 0,1445 cm; hồ sơ lịch sử 5.352,6 / 6.217,4 × 11 = 9,4700 cm (ranh giới 9,6145); còn lại 783,0 / 6.217,4 × 11 = 1,3853 cm.
Chiều tuyết, tổng 3.445,933 s (NEW:5): điều phối 8,566 / 3.445,933 × 11 = 0,0273 cm; hồ sơ lịch sử 251,496 / 3.445,933 × 11
= 0,8028 cm (ranh giới 0,8302); còn lại 10,1698 cm. Nhãn phần trăm trên hình lấy nguyên từ output (RX:3: 1,3 / 86,1 /
12,6%; RP1:26: 7,3%; SNOW:10: 92,5%), không tự tính. Bề rộng hình ≈ 3,6 cm nhãn trái + 11,7 cm ≈ 15,3 cm (vừa lề 16 cm).
Thanh tô đen, xám nhạt, trắng có viền để in đen trắng vẫn đọc được.

## 5. Dòng sổ mới (tệp `evidence/EVIDENCE-REGISTER-ADDENDUM-3-CH4B.md`)

| ID | Nội dung ngắn |
|---|---|
| N4B-01 | Cách làm của phép sàng lọc ưu tiên chi phí (thứ tự tiêu chí, phương án đã ghi, không chạy tiếp) |
| N4B-02 | Số lượt quyết định theo cấu hình trên tập tắc đường cố định, tổng 62.837 |
| N4B-03 | Định nghĩa đệm cùng giá (P0 + k_w(P0 − t0)); cột đệm 1,94 / 4,24 / 0,86 / 0%; sớm 0 → 0,08% |
| N4B-04 | Khoảng lấy mẫu lặp của chênh dự báo − đệm, từng buổi sáng, bỏ từng ngày (chỉ bản 1–3) |
| N4B-05 | Sổ chiều tuyết 8,6 / 251,5 / 3.185,9 trên 3.445,9 s |
| N4B-06 | Định nghĩa và độ dài thêm của các cách phát lại chiều tuyết |
| N4B-07 | Đưa dự báo vào bộ điều phối: 3 lần dừng (1,67 và 2,69 s), 47,6 so với 62,8%, 39,0 → 11,0% |
| N4B-08 | Phép thử học máy: đặc trưng, mô hình, đối chứng, chia ngày, bốn điều kiện, n và các điều kiện không thỏa |
| N4B-09 | Hai phía và phần đuôi của sáu cách hứa có dự báo (thêm trễ quá 600 s, hàng đệm 60 s) |
| N4B-10 | Độ dài thêm 7,18 / 7,37 / 7,27 s chia cho mọi khách, kể cả khách cuối tuần có phần dài thêm 0 |
| N4B-11 | Nghĩa của ba bộ đếm của bộ sinh (đọc mã) |
| N4B-12 | Tệp chính sách giống từng byte giữa hai tập; thiết lập bộ chạy khác |
| N4B-13 | Chạy lại kiểm thử ngày 12/10/2026: 1.024/1.025, kiểm thử còn lại đạt khi có tệp chưa ghi nhận |
| N4B-14 | Đối chiếu từng khách trên 7.159 khách của U, C-30, C-120 |

Các số khác của phần B đều đã có trong sổ chính hoặc phụ lục 1, 2 (mã ở các dòng `% EV:`).

## 6. Bằng chứng còn thiếu (nên không viết, hoặc chỉ viết dạng trung bình theo kịch bản)

1. **Phép thử đổi thứ tự ưu tiên của bộ chọn trên 34 kịch bản chính (Giai đoạn 1b):** chưa chạy. Mục 4.6 dùng bản dự phòng
   của OUTLINE §7.2; REG L02–L05 vẫn trống.
2. **Số đếm gộp sau các tỉ lệ trung bình theo kịch bản** không có trong output đã lưu, nên chỉ in tỉ lệ kèm nhãn "trung bình
   theo kịch bản": cột "đệm cùng giá" và các hàng theo khung của Bảng 4.12; 9,72% → 3,90% và 6,76% của điều phối không trần
   (FA:3,6); 47,6% / 62,8% phải phục hồi và 39,0% → 11,0% phá lời hứa của luật hạn chót khi đưa dự báo vào bộ điều phối
   (RX:9,11); 7,19% → 5,94% của chiều tuyết (có số gộp 41 → 34 trên 601 đi kèm). Riêng 6,01% → 0,17% có số gộp 68 → 2
   trên 1.471.
3. **Tỉ lệ tới sớm của đệm cùng giá** (Bảng 4.12): output không tính; bảng ghi "chưa đo".
4. **Số đếm sau 12,89% / 11,65% / 7,1% của phép thử học máy** (n = 807): output chỉ in tỉ lệ; không suy ngược số đếm từ
   tỉ lệ đã làm tròn.
5. **Độ dài thêm gộp theo khách trên riêng 21 kịch bản ngày thường** (sẽ là 17.224.334,6 ms / 1.471 ≈ 11,7 s): chưa có
   output nào in; văn bản chỉ dùng 13,7 s (trung bình theo kịch bản) và 7,37 s (gộp trên 34 kịch bản).
6. **Chi phí của phép sàng lọc ở trần 120 và 60 giây** có trong NEW:6 nhưng không có dòng sổ cho phần chi phí; không dùng.
7. **Bộ chạy và luật phục hồi của 8 lần chạy chiều tuyết:** chưa kiểm (giữ "chưa được kiểm lại" như phần A).
8. **Bộ đếm `OmittedRepairRequestCount`** của bộ sinh không được các audit đếm; câu "chưa lần nào bỏ sót phương án" ở 4.10
   chỉ nói về giới hạn 100 phương án và giới hạn khối lượng.
9. **Giả thuyết về tải cao hơn** ở 4.11: không có bằng chứng; câu được gắn nhãn "giả thuyết chưa kiểm" (RD LR-34).
10. **Hình H4.1** (đường đánh đổi theo độ dài thêm): không vẽ (mục 7).
11. **So sánh học máy với "đệm đều" không dự báo** cho điều phối không trần (HGB giảm 8,28 điểm, ML:48): có trong output
    nhưng không dùng, vì phần lớn mức giảm đó là của dự báo (mô hình có đặc trưng "phần kéo dài của dự báo"); câu chỉ báo
    phép so với "dự báo + đệm đều". Ghi ở N4B-08.
12. **Quan hệ giữa bộ chạy của phép thử học máy và lời hứa dự báo dùng trong đó** (hồ sơ cố định 12–13/11, MLS:37-39, khác
    quy tắc ngày nguồn của mục 4.7): không nêu trong văn bản để giữ ngắn.

## 7. Chỗ lệch so với OUTLINE-V2 và lý do

1. **4.6 dùng bản dự phòng** (Giai đoạn 1b chưa chạy), cộng phép sàng lọc như outline. Bảng 4.11 chỉ có hai cột U và
   C-30 (outline chỉ đòi hai cột này cho ba ước lượng chi phí); tỉ lệ đổi của trần 120 và 60 giây ở văn xuôi, kèm số đếm.
   Bỏ khỏi bảng hai hàng "chỉ phá hòa" (12 / 9, REG H07) và "dời thêm ít nhất một khách đang có" (426 / 81, REG H09) để
   giữ trang; số còn trong sổ.
2. **Bảng 4.12** thêm hàng "tới sớm quá 60 s"; không có hàng U (số của U nằm ở văn xuôi), vì cột đệm của U dùng tỉ lệ đệm
   tính trên khách của luật C (FFA:15-17) và cần giải thích thêm.
3. **4.7 chỉ báo khoảng tin cậy theo phân phối t** (cả hai phép so), bỏ khoảng lấy mẫu lặp để giữ trang; thêm một câu về
   ba buổi sáng và ngày nguồn 12/11 (REG F11). Không nói 12/11 là ngày nghỉ (REG B21: chưa kiểm).
4. **H4.3** vẽ bằng TikZ thường (hai thanh ngang chồng), không dùng pgfplots, để không đổi preamble (như phần A).
5. **H4.1 không vẽ.** Bảng 4.13 và 4.14 đã chứa cùng các điểm; vẽ thêm hình là trình bày một dữ liệu hai lần (STYLE quy
   tắc 20) và tốn ≈ 0,4 trang khi phần B đã vượt thước của brief.
6. **Bảng 4.13** thêm dòng U + dự báo + 60 s và C-120 + dự báo (outline liệt kê cả hai); tách cột "tới sớm" sang Bảng 4.14
   để giữ ≤ 6 cột. Ba dòng không đệm lặp lại khối dự báo của Bảng `bang:c4-tran120` ở phần A; giữ vì phép so "cùng độ dài
   thêm" cần chúng nằm cạnh các dòng đệm (câu hỏi mở 3).
7. **Bảng 4.14** mở rộng từ 2 dòng (outline) thành 6 dòng, thêm tới sớm và ±60 s, để trả lời ý "hai phía" của RD §8 trong
   một bảng.
8. **"Vai trò của từng thành phần"** là nhãn đậm đầu đoạn trong 4.8, không phải tiêu đề tiểu mục.
9. **Bảng 4.15** thêm hàng "hệ số thật" (0 khách trễ, 18,8 s) và cột độ dài thêm (STYLE quy tắc 31: luôn báo độ dài thêm
   khi báo trễ).
10. **4.9** nói "giai đoạn 9/2018–12/2019 chỉ có 5 đợt tuyết", không dùng chữ "giai đoạn kiểm đề xuất" để tránh mọi ngôn
    ngữ kế hoạch.
11. **4.10** thêm hai dữ kiện ngoài outline: tệp chính sách giống từng byte giữa hai tập (N4B-12, giải thích vì sao phép sàng
    lọc của 4.6 không chuyển sang tập chính) và lần chạy lại kiểm thử ngày 12/10/2026 (N4B-13). Bỏ câu "cấu hình U và C-30
    chỉ khác trần" khỏi 4.10 vì 4.6 đã nói.
12. **4.11** viết câu hợp đồng giả định bằng ngưỡng ký hiệu k > 0,756 m (REG C29, K35) thay vì bảng số lượt bồi thường (đã
    có ở Bảng `bang:c4-phanbotre` của phần A). Đoạn cho hãng xe không kể "không phải phục hồi" là lợi thế so với điều phối
    không trần (sửa lỗi của v4).
13. **4.7 thêm đoạn ngắn** về việc dự báo trong bộ điều phối làm giảm tỉ lệ phá lời hứa của luật hạn chót (REG C14 lưu ý):
    nó cho thấy con số 14,5% / 36,5% của Bảng `bang:c4-nghiavu` phụ thuộc cách hứa, một ý công bằng với luật hạn chót.
14. **Thứ tự trong 4.8** theo RD §8 nhưng gộp ý 4 (giới hạn theo từng khách) với việc giới hạn vẫn giữ ở cuối tuần và
    chiều tuyết, và chỉ trỏ về phần A thay vì in lại 29,2 / 116,5 / 25,2 giây.
15. **Không câu nào** nói về kế hoạch ghi trước, dự đoán hay đạt/trượt; các nhãn "A1 PASS", "ML1 TRUE", "KILL" của output
    nguồn không được dùng; bốn điều kiện của phép thử học máy được nêu mà không nói chúng được đặt khi nào.

## 8. Ghi chú cho người ghép và cho các chương khác

- **Chương 3, `muc:kiemtra`** (dòng 705-706: "1.025 trên 1.025… chưa chạy lại khi viết khóa luận") nay lệch với 4.10, nơi
  báo lần chạy lại ngày 12/10/2026 (1.024/1.025, kiểm thử còn lại đạt khi có tệp chưa ghi nhận; N4B-13). Đề nghị sửa
  câu ở chương 3 theo câu được phép trong `TESTRUN-45f8026-2026-10-12.md`, hoặc bỏ câu ở 4.10 nếu chương 3 đã nói.
- **Chương 5, §5.3** phải đặt phép thử đổi thứ tự ưu tiên của bộ chọn lên đầu các hướng phát triển (4.6 viết "chương kết
  luận đặt phép thử này lên đầu các hướng phát triển"; không dùng `\ref` vì nhãn chương 5 chưa có).
- **Phần A, Bảng `bang:c4-tran120`** và Bảng `bang:c4-dem` của phần B cùng in ba dòng "có dự báo, không đệm". Nếu cần bớt
  trang, có thể bỏ khối "lời hứa đầu theo dự báo" ở bảng của phần A và trỏ sang `bang:c4-dem`.
- **Thuật ngữ:** phần B dùng "lượt quyết định phải phục hồi" như phần A (chương 3 gọi là "quyết định bị ép"); "đệm cùng
  giá" (đệm tỉ lệ, 4.7 và 4.9) khác "đệm 30 giây" (cộng hằng số, 4.8); cả hai được định nghĩa tại chỗ.

## 9. Có thể cắt nếu bản dựng vượt (≈ 550 tiếng)

- 4.7: câu liệt kê ba mô hình học máy (≈ 40); chi tiết 1,67 / 2,69 giây và 62,8% của đoạn đưa dự báo vào bộ điều phối
  (≈ 35); gộp đoạn "thế giới gần như tất định" vào đoạn giá của dự báo (≈ 25).
- 4.8: đoạn "trần cũng là một núm vặn" (≈ 60; điểm trần 120 giây đã có ở phần A, 4.4); câu cách đọc Bảng 4.14 nếu giữ
  câu "thứ hai" làm câu đọc bảng (≈ 30).
- 4.10: đoạn tệp chính sách giống từng byte (≈ 45); câu chạy lại kiểm thử nếu chương 3 đã sửa (≈ 55).
- 4.11: câu giả thuyết tải cao (≈ 30); gộp hai ý của nhóm "Tích hợp" (≈ 40); rút đoạn hợp đồng giả định (≈ 40).
- 4.6: các tỉ lệ đổi ở trần 120 và 60 giây (≈ 30); câu tái lập 62.837 lựa chọn (≈ 20).
- 4.9: câu cách đọc Bảng 4.15 nếu được phép dùng câu "con số 19…" làm câu đọc bảng (≈ 30).

## 10. Câu hỏi mở

1. Chấp nhận ≈ 13,9 trang theo thước 330 tiếng/trang của brief (≈ 10,2 trang theo mật độ đo được), hay cắt thêm theo mục 9?
2. Có sửa câu kiểm thử ở chương 3 (mục 8) không?
3. Giữ hay bỏ khối "có dự báo" ở Bảng `bang:c4-tran120` của phần A khi Bảng `bang:c4-dem` đã có cùng ba dòng?
4. Registrar có muốn thêm số đếm gộp cho các tỉ lệ trung bình theo kịch bản ở mục 6, ý 2 (cần một script đọc lại transcript,
   không phải mô phỏng)?
5. Nhãn chương 5 (`chuong:ketluan`?) để 4.6 và 4.11 có thể dùng `\ref` thay cho "chương kết luận".

## 11. Ba điểm tôi kém chắc chắn nhất

1. **Câu "với thứ tự gốc, phép chạy lại cho đúng cả 62.837 lựa chọn đã ghi" (4.6).** REG H03 ghi "tái lập đúng"; nhưng
   phép kiểm của WP17 là điều kiện cần (lựa chọn đã ghi khả thi, cùng số yêu cầu nhận, không kém về mọi tiêu chí đã ghi;
   WPCHK:12-15), còn PV là chạy lại bằng chính mã đã kiểm. Nếu người chấm hiểu "cho đúng" là một phép giải lại độc lập
   theo đủ thứ tự ổn định, câu này nói hơi quá. Cách đọc "bỏ tiêu chí 3" cũng dựa trên việc tôi đối chiếu tên các mức mục
   tiêu (WPCHK:32) với tiêu chí 3 ở Bảng `bang:rangbuoc` của chương 3.
2. **Ngân sách trang.** Tôi không biên dịch được, nên không biết bản v7 thật sự dài bao nhiêu; hai thước cho ≈ 10,2 và
   ≈ 13,9 trang.
3. **Đoạn học máy và đoạn đưa dự báo vào bộ điều phối (4.7).** Tôi viết đối chứng là "lời hứa theo dự báo cộng đệm đều";
   phép thử học máy dùng một hồ sơ dự báo cố định 12–13/11 (MLS:37-39), khác quy tắc ngày nguồn của phần còn lại của 4.7,
   và các ngày kiểm đã được xem trước. Ở đoạn đưa dự báo vào bộ điều phối, tôi hiểu 62,8% là cùng 15 kịch bản khi không đưa
   dự báo vào (RX:11 "naive 0.628"); output không nói rõ hơn.

*Hết NOTES. Viết bởi Claude (người viết Chương 4 phần B), 2026-10-12.*
