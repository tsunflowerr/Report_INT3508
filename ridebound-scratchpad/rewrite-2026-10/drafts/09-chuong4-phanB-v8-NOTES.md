# 09-chuong4-phanB — NOTES của vòng sửa R27/R29 (2026-10-12)

## 0. Tệp nào là bản dùng để ghép

| Tệp | Vai trò |
|---|---|
| `drafts/09-chuong4-phanB-v7.tex` | Bản trước vòng sửa, giữ nguyên. |
| `drafts/09-chuong4-phanB-v8.tex` | Bản sửa theo ba bản nhận xét. **Không dùng:** năm anchor FR trong dòng `% EV` lệch một dòng (FR:123, 137, 156, 161-162, 165-169). |
| `drafts/09-chuong4-phanB-v9.tex` | v8 với năm anchor đã sửa (FR:124, 138, 157, 170-171, 167-169) và thêm `factor_nowcast_screen.py:21-22`; chữ in ra giống hệt v8 (đã `diff` sau khi bỏ dòng `%`). **Không dùng.** |
| **`drafts/09-chuong4-phanB-v10.tex`** | **Bản dùng để ghép.** v9 cộng sáu chỗ sửa lời mà lần đọc lại cuối cùng thấy còn thiếu (B7 đơn vị "lựa chọn"; B48 vật so "hơn cách đệm"; B60 "Bảng … cho kết quả phát lại"; "trên cùng 15 kịch bản" cho 62,8%; B83 "đồ thị rút gọn"; B84 "thời gian đi thẳng"). |

Tên tệp NOTES giữ `-v8-NOTES` theo yêu cầu đầu ra; nội dung mô tả **v10**. v8, v9, v10 đều tạo bằng ghi độc quyền (mode "x");
bản nháp trung gian làm trong scratchpad của phiên. Không ghi vào thư mục luận văn, `E:/Code/RideBound*` hay `C:/Code/*`;
không mô phỏng, build, cài, xóa.

Các tệp khác của vòng này: `reviews/CH4B-REVISION-LOG.md`; `evidence/EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md` (N4B8-01…13);
`evidence/checks-ch4b-v8/` (script `ch4b_v8_check.py`, output `ch4b-v8-check-2026-10-12.txt`, stdout/stderr, và
`ADDENDUM-6-ERRATA-2026-10-12.md` sửa hai anchor FR của N4B8-06).

Kiểm cú pháp v10 (script đọc, không biên dịch): ngoặc `{}` 211/211; mọi `\begin`/`\end` khớp (4 table, 11 tabular, 1 figure,
1 tikzpicture, 5 itemize); số `$` chẵn (24); không có "niêm phong", "dự đoán trước", "duy nhất", "tối ưu", "phải phục hồi",
"thế giới", "bao đóng", "vế cộng dồn", "núm vặn", "mong manh", "cạnh tranh", "chưa đo", "đệm cùng giá", "gây ra", "chúng
tôi". 52 dòng `% EV`. **Chưa biên dịch thử**; người ghép chạy tectonic với `--keep-logs` và xem `main.log` (tràn lề của Bảng
`bang:c4-dem` cột đầu 4,6 cm; vị trí nhãn mới "8,6 s (0,25%)" phía trên thanh tuyết).

## 1. Độ dài theo mục (v10) — thước của brief, 330 tiếng văn xuôi mỗi trang

"Tiếng" = token cách nhau bởi khoảng trắng sau khi bỏ dòng `%`, bảng, hình, lệnh LaTeX (cùng script đếm cho v7 ra 3.610,
NOTES v7 ghi 3.605). Bảng, hình ước theo số dòng in (bảng 10 dòng có chú thích ≈ 0,6 trang).

| Mục | Ngân sách (tr.) | Văn xuôi v7 | Văn xuôi v10 | Bảng, hình v10 (tr.) | Ước lượng v10 (tr.) |
|---|---:|---:|---:|---|---:|
| 4.6 Vai trò của trần | 1,2 | 396 | 350 | sàng lọc ≈ 0,6 | 1,66 |
| 4.7 Lời hứa theo dự báo | 3 | 945 | 1.009 | dự báo ≈ 0,45; hình ≈ 0,4 | 3,91 |
| 4.8 So với cách đệm | 2,75 | 739 | 671 | một bảng gộp ≈ 0,55 (v7 có hai bảng) | 2,58 |
| 4.9 Chiều tuyết | 1 | 289 | 275 | tuyết ≈ 0,55 | 1,38 |
| 4.10 Tính hợp lệ | 1,25 | 453 | 381 | — | 1,15 |
| 4.11 Thảo luận, hạn chế | 2 | 788 | 797 | — | 2,42 |
| **Tổng** | **11,2** | **3.610** | **3.483** | ≈ 2,55 (v7 ≈ 3,0) | **≈ 13,1** (v7 ≈ 14,0) |

**Ngân sách 11 trang chưa đạt theo thước của brief** (vượt ≈ 2 trang). Theo mật độ đo được mà phần A dùng (480–560 tiếng
mỗi trang), v10 ≈ 9,5 trang. Phần lớn chỗ vượt nằm ở các bổ sung mà nhận xét đòi (mô tả đúng phép thử học máy, nghĩa vụ
gốc của luật hạn chót, cách cộng có giới hạn ở chiều tuyết, thu hẹp câu giới hạn tính toán, câu trả lời về cách đệm, số đếm
thay tỉ lệ). Các chỗ cắt đã làm ở mục 3. Danh sách cắt thêm để tới ≈ 11 trang (≈ 600 tiếng), cần chủ sở hữu chọn, ở mục 4.

Câu: 145 câu, trung vị 25 tiếng; 3 câu 41–43 tiếng (câu dẫn ba mô hình học máy, câu "khi nào chọn đệm", câu bộ chạy chiều
tuyết).

## 2. Nhãn

**Định nghĩa (11):** `muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet`, `muc:c4-hople`, `muc:c4-thaoluan`;
`bang:c4-sangloc`, `bang:c4-dubao`, `bang:c4-dem`, `bang:c4-tuyet`; `hinh:c4-so`.
**Đã bỏ:** `bang:c4-haiphia` (gộp vào `bang:c4-dem`; `grep` trên chương 3 v3 và phần A v4: không nơi nào trỏ tới nhãn này).
**Trỏ ra ngoài (đều có):** chương 3 v3: `bang:rangbuoc`, `muc:dubao`, `eq:so`, `muc:gioihan`, `muc:kiemtra`,
`muc:doichung`, `nx:giunguyen`; phần A v4: `bang:c4-tran120`, `bang:c4-nghiavu`, `bang:c4-phanbotre`, `muc:c4-dieuphoi`
(chỉ trong dòng EV), `muc:c4-congdon`; ngoài chương: `phuluc:C` (phần A cũng dùng; phụ lục phải định nghĩa).
**Trích dẫn:** `engelhardt2026`, `horl2022` (khóa mới, metadata ở REG X3-40; phải thêm vào `10-tai-lieu.tex`), `schulz2026`.

## 3. Thay đổi chính so với v7 và các chỗ cắt

1. **4.6:** "chưa được chạy" lên đoạn đầu; phép sàng lọc được mô tả là chương trình viết riêng giải lại trên phương án đã
   ghi; 62.837 có phạm vi "năm cấu hình" (số chuyển sang EV) và anchor đúng (Q4/PV, không phải WPCHK); câu kết luận 0,31% /
   0,08%; "số yêu cầu được nhận không đổi" giải thích theo thứ tự tiêu chí; bỏ tỉ lệ ở trần 120, 60 giây (cắt theo NOTES v7
   §9; số còn ở EV và mục 6 dưới đây). Tên mục đổi "thứ tự ưu tiên chọn phương án" → "thứ tự tiêu chí của bộ chọn".
2. **4.7:** Bảng `bang:c4-dubao` viết lại: khối số đếm gộp (68 / 22 / 2 trên 1.471; theo khung; tới sớm 0 / 0 / 1) và một
   dòng trung bình theo kịch bản; ô "chưa đo" sửa thành 0. "Đệm cùng giá" đổi thành **đệm tỉ lệ** (tránh ẩn dụ "giá" và
   phân biệt với "đệm" cộng hằng số của bảng thuật ngữ). Khoảng tin cậy viết "có chứa 0", bỏ "mong manh". Đoạn "không riêng
   luật C" dùng số đếm (66 → 2; 129 → 63 trên 1.512; 28 trên 437 ở khung 17 giờ). Đoạn "thế giới gần như tất định" viết
   lại. Phép thử đưa dự báo vào bộ điều phối: K = 2 mô tả bằng lời, 14 / 15 lần chạy hoàn tất, "FleetPy tính rằng xe sẽ
   tới…", "bị ép". Học máy: hồ sơ cố định 12–13/11, mục tiêu 30 giây chỉnh trên ngày hiệu chỉnh, ngày kiểm đã xem trước,
   bỏ **hai** biến trạng thái xe, số đếm 104 → 94 / 807, 57 tới sớm, 1 trong 2 khách trễ.
3. **4.8:** câu trả lời thẳng (M1) ở đoạn đầu; "Thứ tư" gộp vào đoạn đầu; **hai bảng gộp thành một** (`bang:c4-dem` có cột tới
   sớm; số phục vụ vào nhãn hàng; ±60 giây và phần đuôi 68 / 11 / 1 chuyển vào văn xuôi) — tiết kiệm ≈ 0,45 trang; đoạn luật
   hạn chót tách nghĩa vụ gốc (lời hứa không dự báo) khỏi chỉ số phát lại; đoạn trần 120 giây nêu cả hai ngưỡng; bỏ "núm vặn",
   "cạnh tranh".
4. **4.9:** đổi "dự báo lịch sử" → "lời hứa theo dự báo"; định nghĩa "trộn"; đánh dấu hai hàng có buổi sáng chỉ để tham khảo;
   nêu cách cộng có giới hạn (khác `eq:so`); trạm Central Park (NOAA); bỏ câu "quy tắc có ngưỡng".
5. **4.10:** gọi đúng là phép kiểm cài đặt khớp Nhận xét; câu bộ đếm thu hẹp (bỏ "phản ánh tác động của cả gói cam kết");
   bỏ đoạn tệp chính sách giống từng byte (NOTES v7 §9); kiểm thử chạy lại còn một câu, chi tiết sang Phụ lục C; thêm câu bộ
   chạy chiều tuyết đã kiểm (mới, N4B8-05).
6. **4.11:** mức 120 giây theo phần A v4 (chọn sau khi xem kết quả không trần và trần 30 giây trên chính tập kiểm tra chính,
   chỉ lời dùng lại dữ liệu); thêm ngày kiểm học máy đã xem; hệ quả của thời gian dừng 0 giây; câu giả thuyết gộp tải cao và
   thời gian dừng; luật hạn chót 30/60 giây ở tập chính và 30–300 giây ở tập buổi sáng; bỏ câu "trần 120 giây là một điểm ở
   giữa" (sai một nửa, R27 B144); 49 kịch bản cho trung vị 165 / 196 giây.

## 4. Cắt thêm nếu chủ sở hữu muốn đạt ≈ 11 trang theo thước brief (≈ 600 tiếng)

Theo thứ tự ít mất nhất trước:
1. 4.11: bỏ gạch đầu dòng dùng lại dữ liệu, thay bằng trỏ `muc:c4-thamdo` của phần A (≈ 45); gộp "Tích hợp" vào "Mô hình"
   (≈ 25); bỏ vế gán lại xe (≈ 15); bỏ câu giả thuyết (≈ 30).
2. 4.7: chuyển chi tiết phép thử học máy (đặc trưng, chia ngày, cách chỉnh) sang Phụ lục C, giữ ba câu (≈ 170); rút đoạn đưa
   dự báo vào bộ điều phối còn hai câu (≈ 80); bỏ câu "ba buổi sáng đã xem trước" (4.11 đã nói) (≈ 25).
3. 4.8: bỏ đoạn trần 120 giây (hàng của nó còn trong bảng) (≈ 45).
4. 4.9: bỏ câu định nghĩa "trộn" (cột thông tin của bảng đã nói) (≈ 35).
5. 4.10: bỏ câu mức dùng trần 100% nếu chương 3 dòng 467-468 tự ghi số 3.503 / 3.506 / 3.504 (≈ 30).
6. 4.6: bỏ câu "số yêu cầu được nhận không đổi" và câu 35,5 giây (≈ 40; mất câu trả lời cho câu hỏi 2 của giảng viên).

## 5. Bằng chứng mới (phụ lục 6) và cách kiểm

| ID | Nội dung | Kiểm bằng |
|---|---|---|
| N4B8-01 | Số đếm gộp sau Bảng `bang:c4-dubao` (68 / 22 / 2; 60 / 17 / 1; 8 / 5 / 1; 0 / 0 / 0; sớm 0 / 0 / 1) | script, CK8:4-11 |
| N4B8-02 | U 129 → 63 / 1.512; khung 17 giờ 28 / 437; M⁺-30 66 → 2 / 1.471; V-30 66 → 2 / 1.470 | script, CK8:12-28 |
| N4B8-03 | Số đếm học máy: 2 → 1 / 145; 1 → 1 / 200; 0 / 147, 0 / 197; 104 → 94 / 807; sớm 57 và 59 | script (suy từ tỉ lệ 3 chữ số, có cận) |
| N4B8-04 | Hồ sơ cố định 12–13/11; chỉnh trên tập hiệu chỉnh; 37,2 / 31,8 s; hai biến trạng thái; ngày đã xem | đọc MLS, ML, MLT |
| N4B8-05 | Bộ chạy, cấu hình, luật phục hồi của 8 lần chạy chiều tuyết = các lần chạy C-30 của tập chính | script (khung khởi tạo, sha256 DLL), R26 Q8 |
| N4B8-06 | K = 2; hoàn tất 14 (C) / 15 (luật hạn chót) | đọc RF, PFW, cấu hình, FR, RX; R26 Q9 |
| N4B8-07 | Cách cộng có giới hạn ở phát lại chiều tuyết | đọc RPL:14-15, 113-114; RP1:26, 29 |
| N4B8-08 | Sửa N4B-03: đệm tỉ lệ có đo tới sớm (0 / 1.471) | đọc FFA:139-141; script |
| N4B8-09 | Bảng tuyết: không cách nào có khách tới sớm | đọc RP1:7-20 [A] |
| N4B8-10 | 62.837: giải lại đủ thứ tự bằng Q4; số yêu cầu nhận không đổi theo cách đặt thứ tự | đọc Q4, PV |
| N4B8-11 | Sửa phép cộng của F09 (6.217,406 s) | đọc FA:30 |
| N4B8-12 | 0,25% phần điều phối ở chiều tuyết | [A] |
| N4B8-13 | Thu hẹp K34 | đọc ADD1, CMOD, GEN |

## 6. Chuyển sang Phụ lục C (liệt kê cho người viết phụ lục; bản v10 chỉ còn một vế câu)

1. **Chạy lại kiểm thử ngày 12/10/2026** (TR; TLOG; TDIRTY): commit nguồn 45f80261; bản sao mới; .NET SDK 10.0.301, Windows
   11; lần 1–2 (xuống dòng CRLF) 1.020 / 1.025 với 5 lỗi môi trường; lần 3 (`core.autocrlf=false`, `core.eol=lf`) 1.024 /
   1.025; kiểm thử còn lại (`StrictBagItBundleTests…dirty_worktree…`) đòi cây làm việc có tệp chưa ghi nhận, đạt 1/1 khi
   chạy riêng với một tệp đánh dấu. Ghi rõ: phép chạy lại không chứng minh bản dựng lại giống hệt bản bộ chạy đã lưu. Không
   viết như một lần chạy "1.025 / 1.025 đều đạt" (Codex R29 §2.6).
2. **Danh tính bộ chạy chiều tuyết** (N4B8-05): binarySha256, coreCommitSha, policyConfigurationHash, dòng 7 của WP4.
3. **Phép thử đưa dự báo vào bộ điều phối**: lớp bọc v1.3; công thức r_b = (m(b) + m(b+1)) / (2 m(b)); ba lần dừng
   (d20181116-s10-r1-w08 cả hai luật, 1,67 s; d20181114-s10-r3-w08 luật C, 2,69 s); khung 8 giờ 8,4% → 3,7% (Codex R29,
   chưa kiểm lại); số gộp 3.849 / 8.496 và 5.121 / 8.468 (Codex R29, **tôi chưa kiểm**).
4. **Phép thử học máy**: đặc trưng, siêu tham số, chia ngày, công thức F = D0 + ρ·max(0, ŵ), đối chứng D0 + (E − mean δ),
   độ dài thêm trên ngày kiểm (37,2 / 31,8 s), chênh lệch theo từng điều kiện (+4,4 / +3,8 s; +21,8 / +21,7 s; sớm +2,0 điểm).
5. **Phép sàng lọc**: tỉ lệ đổi ở trần 120 và 60 giây (325 / 1.715; 173 / 1.716); thành phần của 62.837; H07, H09.
6. **Phần đuôi đầy đủ của sáu cách hứa có dự báo** (bảng `bang:c4-haiphia` của v7, N4B-09): tới sớm, ±60 s, trễ quá 120 / 300 /
   600 s cho mọi hàng.
7. **Sổ chiều tuyết theo phần có dấu** (Codex R29 §2.3: 893,3 s / 25,9% và 2.292,6 s / 66,5%) — chưa kiểm lại, chỉ đưa vào
   nếu có script.

## 7. Chương 3 v3 cần sửa (tôi không sửa)

1. **Dòng 705-706** (`muc:kiemtra`, kiểm thử phần mềm): thay "1.025 trên 1.025 … chưa chạy lại khi viết khóa luận" bằng: «Kiểm
   thử phần mềm: chạy lại ngày 12/10/2026 trên đúng mã nguồn đã dựng bộ chạy, 1.024 trong 1.025 kiểm thử tự động đạt; kiểm thử
   còn lại đạt khi chạy riêng trong điều kiện nó đòi (Phụ lục~\ref{phuluc:C}).» EV: N4B-13. Phần B v10 dùng cùng câu.
2. **Dòng 457**: "vế cộng dồn" → "phần cộng dồn" (khớp tên mục 4.5 của phần A và phần B).
3. **Dòng 689**: "các bộ đếm cho biết giới hạn có cắt bớt phương án hay không" → "các bộ đếm của bộ sinh" (khớp câu đã thu hẹp
   ở 4.10; giới hạn của bước kiểm và bộ giải chưa được đếm).
4. **Dòng 556-557** (tùy chọn): thêm "nhân thời gian đi với mức tăng dự báo trung bình của khung hiện tại và khung kế tiếp" (K =
   2, N4B8-06) và cập nhật lưu ý "giá trị K chưa kiểm" của X3-29.
5. Dòng 467-468 trỏ `muc:c4-hople` cho số lượt có mức dùng trần 100%: v10 vẫn giữ các số đó ở 4.10 — không cần sửa.

## 8. Phần A v4 cần sửa (tôi không sửa)

1. **Bộ chạy chiều tuyết đã kiểm** (N4B8-05): Bảng `bang:c4-taptu`, hàng chiều tuyết, cột "Bộ chạy": "Chưa kiểm lại" → "Như
   tập chính"; dòng 142 bỏ câu "Số của chiều tuyết mang lưu ý bộ chạy chưa được kiểm lại"; dòng 435 bỏ "(bộ chạy chưa kiểm
   lại)"; EV X3-10 → N4B8-05. Nếu không sửa, phần A và phần B mâu thuẫn.
2. **Dòng 66** "Thế giới mô phỏng không có nhiễu ngẫu nhiên": bảng thuật ngữ loại "thế giới" → "Mô phỏng không có nhiễu
   ngẫu nhiên".
3. **Dòng 231** "kể cả các phép sàng lọc ở 120 giây": phần B dùng "phép sàng lọc" cho phép tính lại bộ chọn ở 4.6; nên đổi
   chữ ở phần A thành "các phép tính thử ở 120 giây" để một tên chỉ một việc.
4. Câu trỏ của phần A về cách đệm (dòng 246-247) khớp đoạn đầu 4.8 (2.328 = 2.328; không dùng chỉ số này làm lý do chọn luật C).

## 9. Câu hỏi mở cho chủ sở hữu

1. **Ngân sách trang:** v10 ≈ 13,1 trang theo thước brief (≈ 9,5 theo mật độ đo được). Cắt thêm theo mục 4 không?
2. **Số đếm học máy suy từ tỉ lệ 3 chữ số** (N4B8-03): phép suy có cận chặt (phần dư ≤ 0,0005 × n / 100, nên số đếm là duy
   nhất), nhưng Codex R29 chọn không suy ngược. Chấp nhận, hay cần tìm tệp dự đoán theo từng khách?
3. **Bộ chạy chiều tuyết:** đồng ý cập nhật phần A, X3-10, C4A-06, N-26 theo N4B8-05?
4. **So trên 2.207 khách chung** (câu hỏi 3 của giảng viên): cần một script chỉ đọc trên CXJ để đếm trễ quá 60 / 120 giây và
   tới sớm của cách đệm và luật C trên cùng nhóm khách. Làm không?
5. **Độ nhạy theo hạt giống bộ giải** (giảng viên 2.2 ý 6): không có bằng chứng; thêm một gạch đầu dòng hạn chế không?
6. **Phép phát lại, phép đệm, đường đi học máy chưa được kiểm độc lập ở 4.10** (giảng viên 2.2 ý 3): ghi thành hạn chế, hay để
   người kiểm số liệu làm một vòng riêng?
7. **Chương 5** phải đặt phép thử ưu tiên chi phí lên đầu các hướng phát triển (câu ở 4.6); nhãn chương 5 chưa có nên chưa
   dùng `\ref`.
8. Số gộp lượt bị ép của phép thử đưa dự báo vào bộ điều phối (3.849 / 8.496; 5.121 / 8.468, Codex R29) chưa được tôi kiểm;
   có cần một script trên `optimize/independent-B/b_cells.tsv` không?

*Hết NOTES. Viết bởi Claude (người sửa Chương 4 phần B), 2026-10-12.*
