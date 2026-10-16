# 08-chuong4-phanA — NOTES của người viết (2026-10-11)

Tệp: `drafts/08-chuong4-phanA.tex` (785 dòng). Phần A gồm `\chapter{Thực nghiệm và đánh giá}` + đoạn mở chương + Bảng
lộ trình (Bảng 4.0 của outline) và các mục 4.1–4.5. Phần B (4.6–4.11) phải nối ngay sau tệp này trong cùng
`08-chuong4.tex` (không có `\chapter` thứ hai).

Đã đọc: WRITING-BRIEF; OUTLINE-V2 (toàn bộ); REVIEW-DECISIONS-R20 (toàn bộ, gồm §8 "câu trả lời trung thực");
EVIDENCE-REGISTER (toàn bộ); EVIDENCE-REGISTER-ADDENDUM-1 (toàn bộ, mục 0 trước); `tang3/t38c120/C120-RESULTS.md`;
STYLE-GUIDE-VI; GLOSSARY-VI; `drafts/07-chuong3.tex` và NOTES của nó; `reviews/R23-FACTCHECK-CH3-CLAUDE.md` (theo
tin nhắn của coordinator); chương 4 hiện tại `TEX/08-chuong4.tex` (chỉ đọc, phần thiết lập và phần w07); `main.tex`
(preamble). Mở thêm các anchor để hiểu nghĩa (không lấy số mới từ đó): W07XM:1-16, W07X:15-70 (cơ chế D05), LAD:1-8
(tập tắc đường cố định), CAP:1-12 (tập buổi sáng), HO:225-245.

Đã chạy: chỉ các lệnh đọc (grep, sed, ls) và vài đoạn Python đọc tệp nháp qua stdin để kiểm cú pháp và đếm chữ; không
ghi tệp nào khác ngoài hai tệp này; không mô phỏng, không build, không cài, không xóa. **Chưa biên dịch thử LaTeX**
(build bị cấm); người ghép cần chạy `tectonic` một lần.

Kiểm cú pháp (script đọc): ngoặc `{}` 402/402; mọi `\begin`/`\end` khớp (13 table, 17 tabular, 1 figure,
1 tikzpicture, 3 scope); số `$` chẵn (134); 0 lỗi.

---

## 1. Độ dài theo mục so với ngân sách

"Tiếng" = token cách nhau bởi khoảng trắng, sau khi bỏ dòng `%`, lệnh LaTeX, công thức `$…$`; chữ trong bảng/hình
đếm riêng. Ước lượng trang: văn xuôi ở **480–560 tiếng/trang** (mật độ đo được của luận văn hiện tại, như yêu cầu);
bảng ước theo số dòng in (\small ≈ 0,6 cm/dòng, \footnotesize ≈ 0,5 cm/dòng ở giãn 1,5; + ≈ 2,5 cm cho tiêu đề, kẻ,
khoảng cách float; trang chữ ≈ 25,7 cm); tiêu đề chương ≈ 0,15 tr., mục ≈ 0,05, tiểu mục ≈ 0,04. Đây là ước lượng,
không phải bố cục đo.

| Mục | Ngân sách | Văn xuôi (tiếng) | Bảng/hình (dòng in → trang) | Ước lượng tổng (trang) | Theo thước 330 tiếng/trang của brief |
|---|---:|---:|---|---:|---:|
| Mở chương + Bảng lộ trình | 0,5 | 123 | lộ trình 10 dòng → 0,33 | 0,70–0,74 | ≈ 0,85 |
| 4.1 Thiết lập | 3 | 708 | tham số 12 → 0,38; tập thử 18 (fn) → 0,45; chỉ số 24 (fn) → 0,56 | 2,85–3,07 | ≈ 3,7 |
| 4.2 Kết quả chính | 3,75 | 1.071 | chính 6 → 0,24; nghĩa vụ 7 → 0,26; phân bố trễ 7 → 0,26; ngày×khung 15 → 0,45 | 3,17–3,49 | ≈ 4,5 |
| 4.3 Phần do điều phối | 2,25 | 815 | dời do điều phối 8 → 0,29 | 1,80–2,04 | ≈ 2,8 |
| 4.4 Chọn mức trần | 3 | 929 | cố định 6 → 0,24; buổi sáng 5 → 0,21; trần 120 14 → 0,42; Hình 4.x → 0,33 | 2,91–3,19 | ≈ 4,1 |
| 4.5 Vế cộng dồn | 1,25 | 657 | kiểm bản ghi 8 → 0,29 | 1,51–1,71 | ≈ 2,3 |
| **Tổng phần A** | **13,75** | **4.303** | 13 bảng + 1 hình ≈ 4,7 | **≈ 12,9–14,2** | ≈ 18,2 |

Chữ trong bảng/hình: 2.099 tiếng (lộ trình 203; 4.1: 723; 4.2: 441; 4.3: 135; 4.4: 487; 4.5: 110).
Câu: 153 câu, trung vị 28 tiếng (kể cả chỗ thay `\ref`), 18 câu trên 40 tiếng, 1 câu trên 50.

Lệch ngân sách: mở chương vượt ≈ 0,2 tr. (do Bảng lộ trình); 4.5 vượt ≈ 0,3–0,45 tr.; 4.3 và 4.2 dư. Bản nháp đầu dài
5.017 tiếng văn xuôi; đã cắt ba lần xuống 4.303. Nếu bản dựng thật vượt, xem mục 9.

## 2. Dòng `% EV:`

**83 dòng** bắt đầu bằng `% EV` (mở chương 2 — hai dòng "—" không có số; 4.1: 21; 4.2: 19; 4.3: 9; 4.4: 20; 4.5: 12),
mỗi đoạn có sự kiện một dòng, mỗi nhóm hàng của bảng một dòng.

Dòng sổ chính được trỏ: A06, A08, A09, A10, A11, A13, A17, A19, A21, A22, A23, A24, A28; B01, B02, B03, B05, B06,
B07, B08, B09, B10, B11, B15, B16, B17, B19, B20, B21; C01–C09, C13, C14, C20–C24, C26–C28, C30, C32; D01–D11, D13,
D14, D16, D19, D20; E01–E09; F02, F03, F06; H01, H02, H13; I05, I06, I08, I12; J10, J11, J18; K04, K05, K07–K12,
K24, K33, K36, K39, K42, K48, K49, K50, K52.
Phụ lục 1: N-03, N-04, N-05, N-06, N-07, N-08, N-09, N-10, N-11, N-15, N-16, N-20, N-21, N-22, N-23, N-24, N-26,
N-27, N-28, N-30; L1a-01…L1a-09; mục 0.3, 0.4.

**Bằng chứng ngoài sổ (đã có người kiểm, nhưng chưa thành dòng sổ — đề nghị thêm vào sổ):**
- X3-10 (run_w07.py:8; run_w07x.py:7; run_t38c120.py:3-8): tập buổi sáng và trần 120 giây dùng cùng bản chạy và luật
  phục hồi không tệ hơn như tập chính. R23 #76, #115 đánh OK. Dùng ở Bảng tập thử, cột "Bộ chạy".
- X3-18 (TEX/08-chuong4.tex:128-136): C1 của tập kịch bản tĩnh = trần 30 giây. Dùng cho "mức 30 giây là mức đã dùng
  ở tập tĩnh" (cùng K33, RD LR-31).
- R23 #51 (HO:109): ghép tự do dùng chính sách chi phí cuốn chiếu, không qua bộ kiểm cứng (anchor của K50, A17).
- R23 #105 (GEN:73-94): giới hạn 2 yêu cầu mới áp cho cả lô của lượt quyết định (A24 ghi "mỗi xe").
- R23 #41 / A23 (NEW:13): tập tắc đường cố định bật chế độ ghi đủ bản ghi, không dừng ở lỗi đầu.
- W07X:48-62 (anchor của D05): "khoảng 147 giây" (79,0 + 68,3) và mức 90 giây của ví dụ cơ chế.
- LAD:2-6 (`travelSnapshotVersion {1: 16}`): cách hiểu "tắc đường cố định" = một bảng giờ đi trong cả lần chạy.
- Phụ lục 1 mục 0.3 (`ls` tier3-t38-v1: 2 thư mục C-30 lỗi gốc) + ADD1:6: quy tắc "bản chạy lại hoàn tất thay bản hỏng".

## 3. Bằng chứng còn thiếu (nên không viết, hoặc ghi "chưa đưa vào bảng" / "chưa kiểm lại")

1. **Trễ / không trễ của M⁺-60 và V-30 trên tập chính**: sổ chỉ có số phục vụ (C01). Bảng 4.4 ghi "chưa đưa vào
   bảng" theo phương án dự phòng của outline. Nếu cần đủ bảng: đọc lại `XW/R15-audit-summary.txt` (A:8 có M⁺-30; M⁺-60,
   V-30 chưa thấy trong sổ) bằng script đã lưu.
2. **Tập buổi sáng ở các mức 60, 150, 180, 240, 300 giây**: số trễ quá 60 s / không trễ quá 60 s / 120 s có trong
   CAP:4-11 (chính anchor của D01, D02) nhưng dòng D02 không chép lại. Vì quy tắc "chỉ số có trong dòng sổ", Bảng
   buổi sáng chỉ có 4 mức (U, C-30, C-90, C-120) và Hình (b) chỉ vẽ 4 điểm; số phục vụ các mức còn lại ở văn xuôi (D01).
   Đề nghị registrar thêm một dòng D-mới từ CAP:4-11 để bảng và hình đủ 9 điểm.
3. **Tổng số bản ghi chặn trên tập tắc đường cố định và kiểu tắc đường tự tạo**: sổ chỉ có số bản ghi chỉ do cộng dồn
   (E03, E04). Vì vậy Bảng 4.10 chỉ có khối hệ số đo (4 dòng + cộng); hai tập kia nói bằng văn xuôi.
4. **Số lượt quyết định theo từng nhóm của 98 lần chạy cũ**: sổ chỉ có tổng 64.371 (E01); 20.101 (C-30) chỉ có ở
   X3-16/STG:43, không dùng. Bảng 4.10 không có cột quyết định.
5. **Bộ chạy và luật phục hồi của 8 lần chạy chiều tuyết**: chưa kiểm (NOTES chương 3 §5); Bảng tập thử ghi "Chưa kiểm
   lại".
6. **Số gộp phải phục hồi / phá hứa của M⁺-60 và V-30** (chỉ có trung bình theo kịch bản và 3,4% gộp phá hứa của M⁺-60
   trong C13, không kèm số đếm): chỉ báo trung bình theo kịch bản trong Bảng 4.5; số gộp chỉ báo cho M⁺-30 (N-21).
7. **Trễ lớn nhất và tới sớm của trần 120 giây khi không dự báo** ngoài số đếm (early60 = 1 có ở N-06 nhưng không dùng):
   không đưa vào.
8. **Nghĩa của "lý do cấu trúc"** cho 1.186 yêu cầu bị từ chối (D13): sổ không định nghĩa; văn bản giữ đúng chữ của sổ.
9. **Thứ trong tuần** của 14–18/11/2018 suy từ B21 (11/11 là Chủ nhật); ngày nghỉ bù 12/11 vẫn UNVERIFIED (không dùng).
10. **Trung vị mỗi lần dời của trần 120 giây (62,5 s)**: N-23 ghi "trung vị 62,5 s"; vì không khách nào bị dời từ hai
    lần (N-07), trung vị theo lần bằng trung vị theo khách (62,54 s). Số lần dời của trần 120 giây (103) không ghi riêng
    trong sổ nên không in.

Số tự tính [A] trong văn bản (đều là phép tính một bước trên số trong sổ, ghi ở đây để checker xem lại): 2.338 − 76 =
2.262 (= C08); +31 = −96 − (−127) (RD CX-08); "dao động trong 6 lượt" = 666 − 660 (D01); "khoảng 147 giây" (W07X §4);
tọa độ hình (mục 5). Không có tỉ lệ mới nào do tôi tính.

## 4. Nhãn

**Phần A định nghĩa:** `chuong:thucnghiem`, `muc:c4-thietlap`, `muc:c4-kichban`, `muc:c4-taptu`, `muc:c4-chiso`,
`muc:c4-thamdo`, `muc:c4-ketqua`, `muc:c4-dieuphoi`, `muc:c4-chontran`, `muc:c4-congdon`; bảng `bang:c4-lotrinh`,
`bang:c4-thamso`, `bang:c4-taptu`, `bang:c4-chiso`, `bang:c4-chinh`, `bang:c4-nghiavu`, `bang:c4-phanbotre`,
`bang:c4-ngaykhung`, `bang:c4-doidieuphoi`, `bang:c4-codinh`, `bang:c4-sang`, `bang:c4-tran120`, `bang:c4-congdon`;
hình `hinh:c4-tran`.
Chương 3 cần và phần A đã định nghĩa: `chuong:thucnghiem`, `muc:c4-thietlap`.

**Phần B phải định nghĩa** (phần A và chương 3 tham chiếu):
- `muc:c4-vaitro` (4.6 Vai trò của trần và thứ tự ưu tiên chọn phương án) — chương 3 và phần A (mở chương, Bảng lộ trình,
  câu nối cuối 4.5).
- `muc:c4-dubao` (4.7 Lời hứa theo dự báo) — chương 3 và phần A (mở chương, Bảng lộ trình, cuối 4.2 phân bố trễ).
- `muc:c4-dem` (4.8 So với cách đệm lời hứa) — phần A (mở chương, Bảng lộ trình, 4.4).
- `muc:c4-tuyet` (4.9 Chiều tuyết 15/11/2018) — phần A (mở chương, Bảng lộ trình).
- `muc:c4-hople` (4.10 Kiểm tra tính hợp lệ) — chương 3 và phần A (Bảng lộ trình).
- (`muc:c4-thaoluan` cho 4.11 — không được phần A tham chiếu; đề nghị dùng tên này.)

**Nhãn ngoài chương 4 mà phần A dùng:** từ chương 3 (đã có): `muc:kientruc`, `muc:bamoc`, `muc:luatc`, `muc:doichung`,
`muc:dubao`, `bang:rangbuoc`, `bang:luat`, `eq:so`, `nx:giunguyen`. Từ chương 1 (chưa có): `muc:c1-cauhoi` (mục có ba
câu hỏi nghiên cứu CH1–CH3, cuối §1.2). Phụ lục: `phuluc:A` (tập kịch bản tĩnh; nếu Phụ lục A bị bỏ, sửa câu ở
`muc:c4-thamdo` thành "tập kịch bản tĩnh dùng trước đó" không kèm tham chiếu), `phuluc:C`.

Trích dẫn: `engelhardt2026` (khóa mới do người viết chương 3 đề xuất; metadata ở NOTES chương 3 §6) và `schulz2026`
(có sẵn). Không thêm tài liệu mới.

## 5. Hình mới và nguồn dữ liệu

**`hinh:c4-tran` (H4.2 của outline)** — TikZ thường (không dùng pgfplots, không thêm gói; `regular polygon` và `diamond`
của thư viện `shapes.geometric` đã nạp trong `main.tex`). Ba khung, mỗi khung một tập, trục ngang = lượt phục vụ, trục
dọc = lượt trễ quá 60 s so với lời hứa đầu không dự báo; các mức của một tập nối theo thứ tự trần tăng; các tập không
nối với nhau; trần 120 giây của tập chính là hình thoi đen.

| Khung | Điểm (phục vụ, trễ quá 60 s) | Nguồn | Phép đổi tọa độ (cm) |
|---|---|---|---|
| (a) tắc đường cố định | C-30 (1.534, 0); C-60 (1.540, 0); C-120 (1.563, 23); U (1.584, 47); FREE (1.629, 274) ngoài khung | D09 | x = (phục vụ − 1530) × 0,06; y = trễ × 0,05 |
| (b) buổi sáng | C-30 (660, 47); C-90 (664, 50); C-120 (666, 51); U (665, 50) | D01, D02 | x = (phục vụ − 658) × 0,36; y = trễ × 0,05 |
| (c) tập chính | C-30 (2.338, 76); C-120 (2.387, 132); U (2.434, 203) | C01, C06, N-06 | x = (phục vụ − 2320) × 0,03; y = trễ × 0,0125 |

Tọa độ đã tính tay và kiểm lại: (a) 0,24/0; 0,60/0; 1,98/1,15; 3,24/2,35. (b) 0,72/2,35; 2,16/2,50; 2,88/2,55;
2,52/2,50. (c) 0,54/0,95; 2,01/1,65; 3,42/2,54 (2,5375). Bề rộng hình ≈ 15,6 cm (vừa lề 16 cm).

## 6. Sửa theo phụ lục 1 (mục 0) và theo kiểm chứng chương 3 (R23)

- **0.1 / 0.2 (−1 ms):** 4.3 viết "4 người còn lại có giờ trả bị kéo sớm hơn, mỗi người đúng 1 mili giây"; không nêu
  nguyên nhân, không nói vế hai chiều có tác dụng. Phạm vi: chỉ U, C-30, C-120, M⁺-30 trên 34 kịch bản (dòng EV ghi rõ).
- **0.3 (phạm vi cộng dồn):** câu trả lời 4.5 nói "98 lần chạy cũ" và "34 lần chạy trần 120 giây"; đoạn phạm vi ghi
  132 lần chạy / 1.780 bản ghi, hay 140 / 1.943 kể cả chiều tuyết, và nêu 15 lần chạy hiệu chỉnh + 16 lần chạy C-30F
  chưa kiểm; có câu "kết quả không áp cho mọi lần chạy". Không có chữ "mọi lần chạy" theo nghĩa khẳng định.
- **0.4:** câu "trần giữ trên chiều tuyết" dùng N-26 (25,2 giây, 8/601, 0/5.067), không dùng F13.
- **R23 #57:** luật hạn chót 30–60 giây trên tập chính, 30–300 giây trên tập buổi sáng (4.2 và Bảng tập thử nói đúng
  từng tập).
- **R23 #51:** ghép tự do dùng chính sách chi phí cuốn chiếu; 4.1 không nói "năm luật cùng một bộ điều phối".
- **R23 #10, #35:** phần A không nói ràng buộc dịch vụ loại phương án giữ nguyên; Bảng tham số chỉ ghi giá trị cấu hình.
- **R23 #24:** "0 giây (kiểm trên 3 lần chạy mẫu)".
- **R23 #41:** chỉ tập tắc đường cố định được nói là "ghi đủ mọi bản ghi"; các tập khác "dừng ở lỗi gặp trước".
- **R23 #105:** "mỗi lượt quyết định xét tối đa 2 yêu cầu mới".
- **R23 #111:** "170 (năm cấu hình)".

## 7. Chỗ lệch so với OUTLINE-V2 và lý do

1. **Bảng 4.0 (lộ trình)** có ba cột Câu hỏi / Mục / Đại lượng được đo; không trỏ tới bảng của phần B để tránh phụ thuộc
   nhãn bảng chưa có. Số bảng in sẽ là 4.1 cho bảng này (đánh số tự động); "Bảng 4.0…4.10" của outline thành 4.1…4.13.
2. **Bảng 4.4**: hàng M⁺-60, V-30 ghi "chưa đưa vào bảng" (phương án dự phòng của outline).
3. **Bảng 4.7 (ngày × khung)**: không viết script mới; dùng dữ liệu N-22 của phụ lục 1 (đã tính bằng script, khớp C30).
   Bỏ cột "kịch bản C trễ ≤ U" (luôn 34/34) và nói trong văn bản; giữ ≤ 6 cột.
4. **Bảng 4.8** thêm cột trần 120 giây (N-23) để mục 4.4 dùng lại, không lặp số ở Bảng 4.9c.
5. **Bảng 4.9b** chỉ 4 mức (xem mục 3, ý 2); tỉ lệ phải phục hồi của luật hạn chót ở mọi mức (trung bình theo kịch bản)
   để ở văn xuôi, không chung khối với số đếm gộp.
6. **Bảng 4.9c** dựng lại thành hàng = chỉ số, cột = U / C-30 / C-120, vì STYLE quy tắc 20 cấm ghép "a / b / c" trong
   một ô (bảng mẫu của outline §7.1 có ô "203 / 102 / 18"); các dòng phần dời do điều phối chuyển sang Bảng 4.8.
7. **H4.2** vẽ "lượt trễ quá 60 s theo lượt phục vụ" cho từng tập (đường đánh đổi), thay vì "phục vụ và trễ theo B":
   cùng dữ liệu, một hình thay hai, đọc được ngay chỗ điều phối không trần không phải cận trên (khung b). Dùng TikZ thay
   pgfplots để không đổi preamble.
8. **Bảng 4.10** chỉ khối hệ số đo (4 dòng + cộng); dấu vết ở tắc đường cố định và tự tạo nói bằng lời (mục 3, ý 3–4).
9. **Thêm vào 4.3** đoạn "trần vẫn giữ ở kịch bản không có dự báo và ở ngày có sự kiện" (N-28, N-26): đây là ý 4 của
   "câu trả lời trung thực" RD §8, với anchor đã sửa (phụ lục 1, 0.4).
10. **"Quyết định phải phục hồi"** dùng cho quyết định bị ép (theo yêu cầu của coordinator), định nghĩa trong Bảng chỉ số
    và nối với "xe bị ép" của chương 3 qua `muc:doichung`.
11. **Đoạn tùy chọn về tập kịch bản tĩnh ở 4.3** (≤ 0,25 tr.) không viết: Phụ lục A còn có điều kiện, số chưa được neo lại.
12. **4.1 không có bảng số lần chạy riêng**: số lần chạy nằm ở cột cuối Bảng tập thử; quy tắc đếm một câu, chi tiết ở
    Phụ lục C.
13. **Ví dụ 307,3 = 99,1 + 208,2 giây (N-30)** chỉ giữ vế trần 300 giây ở 4.4 (vế trần 30 giây đã dùng ở H1.1 chương 1).
14. Không có câu nào về kế hoạch, mã băm, dự đoán, "kết quả mong đợi ghi trước khi chạy" (owner override); tính thăm dò
    nói bằng việc dùng lại dữ liệu đã xem (I06).

**Các ý của "câu trả lời trung thực" (RD §8) nằm ở phần A:** không bao giờ phải phục hồi so với luật hạn chót (4.2,
Bảng nghĩa vụ); giới hạn theo từng khách không cần dự báo đúng (4.3); trần là núm vặn, điểm trần 120 giây có dự báo
2.322 / 2.379 ở 7,27 giây (4.4, Bảng trần 120). **Để phần B (4.8):** so cùng độ dài lời hứa, độ chính xác hai phía
(N-04), phần đuôi (N-01), so điểm trần 120 giây với đệm 30 giây (N-18); 4.4 chỉ trỏ sang `muc:c4-dem`, không nêu số đệm.

## 8. Ghi chú cho người viết phần B (tránh lặp)

- Đã in ở phần A, phần B chỉ cần trỏ: các số không dự báo của U / C-30 / M⁺-30 (Bảng 4.4); phân bố trễ (Bảng 4.6); số
  có dự báo của U / C-30 / C-120 (Bảng trần 120: 137/10/65 trễ; 2.297/2.328/2.322; 2.347/2.338/2.379; 7,18/7,37/7,27 s);
  phần dời do điều phối U / C-30 / C-120 (Bảng 4.8); 29,2 s / 116,5 s ở cuối tuần và 25,2 s chiều tuyết (4.3).
- Phần A đã định nghĩa "gộp theo khách", "trung bình theo kịch bản", "hệ số tắc đường đo", "quyết định phải phục hồi",
  "phát lại", và nêu rằng dự báo chỉ có ở 21/34 kịch bản và không có ở 12–13/11.
- Phần A chưa nói về: 0,17% (K24), 13,7 s, 3,2 s, 34/1.471, Họ B, học máy, đệm, sổ ba phần ngày thường / chiều tuyết,
  sàng lọc bộ chọn, bộ đếm hợp lệ (N-25), 382.006 lần sửa.

## 9. Có thể cắt nếu bản dựng vượt ngân sách (≈ 350 tiếng)

- 4.2: câu về khách chung (chờ +0,5 s, ngồi −10,5 s) (≈ 30 tiếng); đoạn "Bảng nghĩa vụ không so hai chuẩn…" gộp vào
  đoạn trước (≈ 20).
- 4.3: câu "Bảng~… so phần dời…" (≈ 20); trong đoạn từ chối, câu 845/643/495 (≈ 35) nếu 4.5 giữ câu tương đương.
- 4.4: câu N-30 về trần 300 giây (≈ 35); câu theo khung giờ và theo kịch bản của trần 120 giây (≈ 55).
- 4.5: đoạn dấu vết ở tắc đường cố định / tự tạo (≈ 60); câu sàng lọc E06 (≈ 45).
- Mở chương: có thể bỏ cột "Đại lượng được đo" của Bảng lộ trình (≈ 0,1 tr.).

## 10. Câu hỏi mở

1. Nhãn chương 1 cho ba câu hỏi nghiên cứu: tôi dùng `muc:c1-cauhoi`; người viết chương 1 cần định nghĩa đúng tên này.
2. Có giữ Bảng lộ trình (Bảng 4.1 khi in) không, khi nó làm mở chương vượt ≈ 0,2 trang?
3. Registrar có thêm dòng sổ cho CAP:4-11 (mục 3, ý 2) và cho M⁺-60 / V-30 trên tập chính (ý 1) không? Nếu có, Bảng 4.4,
   Bảng buổi sáng và khung (b) của hình có thể đủ hàng mà không đổi văn bản.
4. "Tập tắc đường cố định" có nghĩa là một bảng giờ đi duy nhất trong cả lần chạy (LAD `travelSnapshotVersion {1: 16}`)
   — cần registrar xác nhận câu "hệ số không đổi trong lần chạy" ở Bảng tập thử.
