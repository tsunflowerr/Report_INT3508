# 07-chuong3-v3 — NOTES của người sửa (2026-10-11)

Tệp chương: `drafts/07-chuong3-v3.tex` (726 dòng; `\input` được trong `main.tex`). Bản 1 `07-chuong3.tex` giữ nguyên.
`07-chuong3-v2.tex` là bản trung gian (lượt rút gọn thứ nhất; xem `reviews/CH3-REVISION-LOG.md` mục 8), không dùng để
ghép. Lý do từng thay đổi: `reviews/CH3-REVISION-LOG.md` (214 nhận xét, 166 A / 38 M / 10 R). Sổ bằng chứng mới:
`evidence/EVIDENCE-REGISTER-ADDENDUM-2-CH3.md` (X3-01…X3-41).

Không ghi vào thư mục luận văn hay nơi khác; không chạy mô phỏng, không build LaTeX, không cài, không xóa. Kiểm cú pháp
bằng script chỉ đọc `texcheck.py` (scratchpad phiên): ngoặc `{}` cân, mọi `\begin` có `\end`, số `$` chẵn trong mọi
đoạn, 34 nhãn không trùng. **Chưa biên dịch thử**; người ghép cần chạy `tectonic` một lần.

---

## 1. Độ dài theo mục so với ngân sách

Bộ đếm `wc_ch3_v2.py` (scratchpad phiên): "tiếng" = token cách nhau bởi khoảng trắng có chữ hay số, bỏ dòng `%`, lệnh
LaTeX, công thức; chữ trong bảng/hình đếm riêng. Cùng bộ đếm cho bản 1: 3.334 tiếng văn xuôi, 1.816 tiếng bảng/hình
(NOTES v1 dùng bộ đếm khác, ghi 3.615 / 2.081; hệ số quy đổi ≈ 1,084).

| Mục | Ngân sách (OUTLINE-V2) | Văn xuôi v3 | Bảng/hình v3 | Ước lượng trang v3 |
|---|---:|---:|---:|---:|
| Mở chương | 0,25 | 164 | 0 | ≈ 0,3 |
| 3.1 Bài toán, thuật ngữ, một lượt (gồm Bảng 3.1–3.3, Hình 3.1) | 2 | 556 | 1.164 | ≈ 3,5 |
| 3.2 Ba mốc (Hình 3.2) | 1,75 | 362 | 118 | ≈ 1,2 |
| 3.3 Luật C, Nhận xét 3.1 (Bảng 3.4) | 2,5 | 708 | 146 | ≈ 1,9 |
| 3.4 Luật đối chứng, bộ chọn, phục hồi (Bảng 3.5) | 1,5 | 738 | 254 | ≈ 2,1 |
| 3.5 Lời hứa theo dự báo (Bảng 3.6) | 1,25 | 514 | 151 | ≈ 1,7 |
| 3.6 Sổ theo từng khách (Bảng 3.7) | 0,75 | 337 | 75 | ≈ 1,0 |
| 3.7 Cài đặt, kiểm thử, tái lập (Bảng 3.8, Hình 3.3) | 2,5 | 673 | 340 | ≈ 2,3 |
| Dự phòng | 0,5 | — | — | — |
| **Tổng** | **13** | **4.052** | **2.248** | **≈ 13,5–14,5** |

**Cách ước lượng.** (a) Theo cách của NOTES v1 (≈ 560 tiếng/trang văn xuôi theo bộ đếm v1, tức ≈ 517 theo bộ đếm này,
cộng diện tích từng bảng/hình: bảng thuật ngữ ≈ 0,6; bảng ràng buộc ≈ 0,55; giả mã 17 dòng ≈ 0,8; giả mã 7 dòng ≈ 0,4;
giả mã 12 dòng ≈ 0,55; bảng luật ≈ 0,6; bảng ví dụ sổ ≈ 0,25; bảng kiến trúc ≈ 0,45; mỗi hình TikZ ≈ 0,45–0,5): văn xuôi
≈ 7,8 trang + bảng/hình ≈ 5,7 trang ≈ 13,5 trang, chưa tính tiêu đề và công thức (≈ 0,6). (b) Theo mật độ đo được của cả
chương 3 cũ (481 tiếng pdftotext/trang, kể cả bảng; tiếng pdftotext ≈ 1,08 × bộ đếm này): (4.052 + 2.248) × 1,08 / 481
≈ 14,1 trang. **Kết luận: v3 vượt ngân sách 13 trang khoảng 0,5–1,5 trang** (ước lượng, chưa dựng). Mục 3.1 vượt chủ
yếu vì thêm bảng thuật ngữ (yêu cầu của người đọc) và nhận bảng ràng buộc từ 3.3 (yêu cầu của giảng viên); 3.3 và 3.2 vì
thế dưới ngân sách. Bản trung gian v2 có 4.984 / 2.382 tiếng; bản sửa đầy đủ đầu tiên có 6.129 tiếng văn xuôi.

**Chỗ cắt nếu bản dựng thật vượt 13 trang** (theo thứ tự đề nghị; không mất yêu cầu bắt buộc nào của bốn bản nhận xét):
1. Bỏ Bảng 3.4 (giả mã kiểm trần): nội dung đã có ở Định nghĩa 3.1, Bảng 3.3 dòng 8 và đoạn mười chiều. Tiết kiệm
   ≈ 0,4 trang. (Bảng này do coordinator yêu cầu ở bản 1, nên cần đồng ý.)
2. Chuyển 3.7.2 đoạn thời gian chạy và chi tiết số của 3.7.3 (382.006 / 185 / 170 / 15; 13 hạng mục) sang Phụ lục C,
   giữ một câu tóm tắt (giảng viên C2). ≈ 0,3 trang. (OUTLINE-V2 §3.7 đặt chúng ở 3.7.)
3. Thu Hình 3.3 còn phần chào hỏi và vòng lặp; ba mũi tên cuối nêu bằng một câu. ≈ 0,15 trang.
4. Bỏ Bảng 3.6 (giả mã dự báo): công thức~(3.6), câu trực giác và ví dụ đã đủ để làm lại. ≈ 0,55 trang. (OUTLINE-V2 có
   "Giải thuật 3.2", nên cần đồng ý.)

## 2. Dòng `% EV:` và dòng sổ được dùng

- **65 dòng** `% EV` (mỗi đoạn có sự kiện một dòng; mỗi nhóm dòng bảng/giả mã một dòng).
- Sổ chính: A01–A02, A04–A10, A12–A14, A16–A19, A21–A25, A27–A28; B01–B03, B06, B10, B15–B17, B20; C04, C19; D04; E01,
  E08; F01–F04, F06, F07, F09, F10, F12; H01, H02, H13; I01, I09, I13; J01–J03, J05–J08, J10, J11, J17, J18, J35; K02,
  K04, K05, K18, K19, K26, K27, K30, K32, K41, K43, K50.
- Phụ lục 1: N-05 (CORRECTED), N-07, N-15, N-16, N-21, N-25, N-26, N-28, L1a-01; mục 0.1–0.2; dòng 15–19 (độc lập bộ
  đọc).
- Phụ lục 2: X3-01…X3-41 (trừ X3-08, X3-18). Mọi X3 của bản 1 đã kiểm lại; ba anchor sửa (X3-01, X3-14, X3-15).

## 3. Nhãn

**Chương này định nghĩa (34):** `chuong:phuongphap`; mục `muc:baitoan`, `muc:thuatngu`, `muc:baitoan-phatbieu`,
`muc:luotquyetdinh`, `muc:bamoc`, `muc:luatc`, `muc:giunguyen`, `muc:doichung`, `muc:dubao`, `muc:so`, `muc:caidat`,
`muc:kientruc`, `muc:gioihan`, `muc:kiemtra`; `dn:luatc`, `nx:giunguyen`; công thức `eq:chon`, `eq:bamoc`, `eq:luatc`,
`eq:dongnhat`, `eq:keodan`, `eq:so`; bảng `bang:thuatngu`, `bang:rangbuoc`, `bang:luotquyetdinh`, `bang:kiemtran`,
`bang:luat`, `bang:dubao`, `bang:vidu-so`, `bang:kientruc`; hình `hinh:vongquyetdinh`, `hinh:bamoc`, `hinh:bantin`.
Mọi nhãn mà `08-chuong4-phanA.tex` trỏ sang Chương 3 (`muc:kientruc`, `muc:bamoc`, `muc:luatc`, `muc:doichung`,
`muc:dubao`, `bang:rangbuoc`, `bang:luat`, `eq:so`, `nx:giunguyen`) đều còn. Nhãn của bản 1 đã bỏ: `bang:vidu-bamoc`
(không chương nào trỏ tới).

**Chương này cần (11):**

| Nhãn | Mục | Tình trạng |
|---|---|---|
| `chuong:thucnghiem`, `muc:c4-thietlap`, `muc:c4-congdon` | Ch. 4, 4.1, 4.5 | Đã có trong `08-chuong4-phanA.tex` |
| `muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-hople` | 4.6, 4.7, 4.10 | Phần B của Ch. 4 phải định nghĩa (NOTES phần A §4 đã ghi) |
| `muc:c2-baitoan` | 2.1 (bài toán ghép chuyến, yêu cầu–chuyến–xe) | Chương 2 chưa viết; tên đề nghị |
| `muc:c2-dolech` | 2.2 (đo và kiểm soát độ bất ổn) | như trên |
| `muc:c2-rangbuoc` | 2.3 (các dạng ràng buộc lời hứa) | như trên |
| `muc:c2-dubao` | 2.4 (dự báo thời gian đi) | như trên (bản 1 đã dùng) |
| `phuluc:C` | Phụ lục C (tái lập) | chưa có |

`phuluc:A`, `phuluc:B` của bản 1 không còn được Chương 3 dùng. Ánh xạ tên cũ (LOCKS = điều phối không trần trên tập tắc
đường cố định; B1, C1 của tập kịch bản tĩnh; REG B17, TEX08:128-138) chuyển cho Phụ lục A/C.

## 4. Số học của các ví dụ dựng tay

Tính lại bằng `check_examples_ch3.py` (gọi đúng `promise_stretch.stretch` của dự án) → `check_examples_ch3.txt`
(scratchpad phiên; sổ X3-37).

**Lời hứa theo dự báo (mục 3.5).** Kịch bản khung 8:00–10:00, nên đồng hồ tương đối bắt đầu 8:00 và khung 15 phút chứa
9:05 là $i = 4$ (9:00–9:15); khung kế là $i = 5$. $t$ = 9:05:00 ($3.900$ s), $p$ = 9:25:00 ($5.100$ s), $p - t = 1.200$ s.
Hồ sơ giả định $m_4 = 1{,}25$, $m_5 = 1{,}50$ → $g = 1$ trong khung 4, $g = 1{,}50 / 1{,}25 = 1{,}2$ trong khung 5.
Khung 4 còn $h = 600$ s, phủ $600 / 1 = 600$ s quãng đường; còn $W = 600$. Khung 5: $h/g = 900 / 1{,}2 = 750 \ge 600$
→ $S = 9{:}15{:}00 + 600 \times 1{,}2 = 9{:}15{:}00 + 720$ s $= 9{:}27{:}00$. $D = \max(9{:}25{:}00; 9{:}27{:}00) =
9{:}27{:}00$, dài thêm 120 s. Kiểm tích phân: $600/1 + 720/1{,}2 = 1.200 = p - t$. Script in: `S = 9:27:00 ; D = 9:27:00
; extension = 120.0 s`.

**Sổ của khách A (mục 3.6, Bảng 3.7).** Bản ghi đầu 8:50:00: $v = e = p$ = 9:10:00, mọi độ lớn 0, $L = 0$. Bản ghi sửa
9:00:00: $v$ = 9:10:00, $e$ = 9:10:40, $p$ = 9:11:10 → $x = 40$, $c = 30$, $z = 70 = x + c$; $L = 0 + |c| = 30 = B$
(qua vì dấu $\le$). Ba phần: $p_0$ = 9:10:00, $D_0$ = 9:10:30 ($f = 30$), $a$ = 9:11:10, $p_n$ = 9:11:10 ($\rho = 0$);
$a - p_0 = 70$; $q = 30$; phần còn lại $= a - D_0 - q = 40 - 30 = 10$; $70 = 30 + 30 + 10$. Kiểm bằng đẳng thức
(3.4): $\sum x + \rho - f = 40 + 0 - 30 = 10$. A có $a - p_0 = 70 > 60$ nên thuộc nhóm được cộng ở Ch. 4.

**Hai giới hạn của Nhận xét 3.1.** Thứ hai: $v$ = 9:10:00, $e = p$ = 9:11:00 → $c = 0$, $z = 60$ s. Thứ ba: $v = p$ =
9:10:00, $e$ = 9:12:00 → $z = 0$, $|c| = 120$ s, và theo X3-25 $L_r$ tăng 120 s. Đây là ví dụ 600/660/720 giây của bản
1 viết lại bằng giờ đồng hồ (hiệu 60 và 120 s giữ nguyên).

**Ví dụ ba mốc (Hình 3.2).** Giữ nguyên số của bản 1 (9:10:00 / 9:10:40 / 9:11:10; 40 + 30 = 70 s); khách B đổi tên
thành khách M để không trùng trần $B$.

Ví dụ của người đọc (9:00 → 9:21, và 180 = 30 + 60 + 90) đúng số học nhưng không dùng: ví dụ dự báo của v3 đặt $t$ giữa
khung để thấy $g = 1$ ở khung hiện tại, và ví dụ sổ dùng lại khách A để cả chương có một nhân vật.

## 5. Tài liệu tham khảo

Khóa đã có trong `ridebound/noi-dung/10-tai-lieu.tex`: `alonsomora2017` (dòng 7), `fielbaum2020` (dòng 13),
`ortools` (dòng 93), `schulz2026` (dòng 116). Khóa mới cần thêm (metadata kiểm ở X3-40):

```tex
\bibitem{horl2022}
S.~Hörl and F.~Zwick.
\newblock Traffic uncertainty in on-demand high-capacity ride-pooling.
\newblock Conference paper, ETH Zurich Research Collection, 2022.
\newblock \url{https://doi.org/10.3929/ethz-b-000561639}

\bibitem{engelhardt2026}
R.~Engelhardt, F.~Dandl, A.~A.~Syed, C.~Ding, S.~Alvarez-Ossorio Martinez, Y.~Zhang, H.~Hamdy,
J.~Brodersen, Z.~Chen, and K.~Bogenberger.
\newblock FleetPy: an open source simulator for reproducible research on mobility-on-demand services.
\newblock \emph{European Transport Research Review}, 18:52, 2026.
\newblock \url{https://doi.org/10.1186/s12544-026-00823-3}
```

- `horl2022`: tác giả, tên bài, năm, DOI, loại "Conference Paper" — PDF trích (HZ:1-20); DataCite theo Codex R23. Tên hội
  nghị chưa kiểm (có thể TRB 2022): không ghi.
- `engelhardt2026` **không thay** `fleetpy2022`: hai bài khác nhau (ETRR 2026, mười tác giả; arXiv 2207.14246, bảy tác
  giả). Chương 3 chỉ trích `engelhardt2026` (bài nói rõ dùng FleetPy 1.0.2, FLEET:474). Giữ `fleetpy2022` nếu chương khác
  trích, không sửa tác giả hay năm của nó. "article 52", số 1, ngày 15/07/2026 chỉ Codex kiểm (Crossref).
- Không thêm Ichoua và cộng sự (2003): bài chưa mở.

## 6. Mẫu LaTeX

- Môi trường `nhanxet` vẫn định nghĩa có điều kiện ở đầu tệp; nên chuyển lên `main.tex` sau `dinhnghia`.
- Chứng minh viết tay "*Chứng minh.* … □" (mẫu chưa đổi `\proofname`).
- Chỉ dùng gói và thư viện TikZ đã nạp (`arrows.meta`, `positioning`); không cần pgfplots.
- Thứ tự float trong nguồn: Bảng 3.1 thuật ngữ; Bảng 3.2 ràng buộc và tiêu chí; Hình 3.1 vòng quyết định; Bảng 3.3 giả mã
  một lượt; Hình 3.2 ba mốc; Bảng 3.4 giả mã kiểm trần; Bảng 3.5 các cấu hình; Bảng 3.6 giả mã dự báo; Bảng 3.7 ví dụ sổ;
  Bảng 3.8 kiến trúc; Hình 3.3 bản tin. Các chương khác phải trỏ bằng nhãn, không bằng số.

## 7. Chỗ lệch so với OUTLINE-V2 và lý do

1. **Bỏ "Bảng 3.1 = ví dụ 9:10"**: cùng một ví dụ đang có ở ba dạng (bảng, hình, câu văn), trái STYLE quy tắc 20 và CX §2.9.
   Giữ Hình 3.2 (bắt buộc) và đưa dạng bảng vào ví dụ sổ (Bảng 3.7), nơi người đọc cần nó.
2. **Bảng ràng buộc và thứ tự tiêu chí chuyển từ 3.3 lên 3.1.2** (LE C6, như DACN 3.2.2).
3. **Thêm bảng thuật ngữ ở 3.1.1** (RD X1); tên tiếng Anh gom vào bảng (LE C3).
4. **Tiêu đề 3.6 "Sổ theo từng khách"** thay "Sổ theo dõi từng khách", để một khái niệm một tên (RD F1).
5. **Câu độ phức tạp** của OUTLINE ("budget check loops over riders × 10 dimensions") được giữ nhưng thêm vế đếm đảo thứ tự
   theo cặp, nên không còn ngụ ý tuyến tính (CX §2.5).
6. **Số bão hòa 3.503 / 3.506 / 3.504** chuyển sang mục 4.10 (LE C2); 3.4 chỉ giữ câu cơ chế.
7. **Tên LOCKS, B1, C1** bỏ khỏi chương (LE C7).
8. **Đoạn đóng góp OUTLINE §6.1** (câu "28 trên 34 … luật C giữ được ở mọi kịch bản, theo cấu tạo" và "đều ở mức trần nới
   rộng") ngoài phạm vi tệp này; giảng viên (A5) đề nghị: "Luật hạn chót 30 giây tính từ lời hứa đầu phục vụ cùng số lượt,
   nhưng vì tính cả phần do tắc đường nên ở 28 trên 34 kịch bản nó phải phá chính luật của mình với ít nhất một khách; luật
   C không tính phần đó nên không gặp trường hợp này", và "đều ở trần 120 giây". Chuyển cho người viết Chương 1.
9. **Cho người viết Chương 4:** (a) Ch. 3 giữ "bản ghi chặn" như phần A; (b) phần A không dùng hạn chót hai phía M-30 nên
   Bảng 3.5 không có hàng này; nếu phần B dùng, thêm một hàng $|p - p_0| \le B$ (LOCK:186-197); (c) Ch. 3 dùng "khách được
   phục vụ", Ch. 4 dùng "lượt phục vụ": chủ nghiên cứu chọn một.

## 8. Câu hỏi mở cho chủ nghiên cứu

1. **Trang:** bản dựng thật có vượt 13 trang không? Nếu vượt, đồng ý cắt theo mục 1 (thứ tự 1 → 4)?
2. **Chu kỳ gọi lượt quyết định** (bao nhiêu giây mô phỏng một lần FleetPy gọi bước điều phối) chưa kiểm. Tệp driver ghi
   `eventDriver: exact-source-arrival-event-clock-v1`, `drainStepSeconds: 600`; nếu muốn nêu, cần mở mã bộ chạy FleetPy của
   dự án để xác nhận nghĩa (giảng viên §2.1).
3. **Nguồn gốc tên** C, U, M⁺, V: không có văn bản; mã gọi chính sách C1/C2. Giữ không giải thích, hay chủ nghiên cứu cung
   cấp lý do?
4. **Lý do thứ tự tiêu chí** (nhận nhiều yêu cầu trước ổn định) chưa có văn bản (giảng viên §6, B4).
5. **Chạy lại `dotnet test`** trên đúng mã của bộ chạy lưu trữ trước khi nộp (giảng viên Q10)? Nhiệm vụ này cấm build.
6. **Lần tay một khách thật** từ bản ghi (giảng viên Q11): cần một script chỉ đọc in $v$, $e$, $p$ của một lần sửa thật;
   chưa làm.
7. **Thời gian chạy**: máy, hệ điều hành, và `elapsedMs` có gồm thời gian FleetPy không (giảng viên §2.16, B12).
8. **Khóa giờ đón chặt**: có muốn thêm một câu nói hệ quả "chỉ chèn được trước điểm đón của khách đang chờ nếu giờ đón của
   khách đó không đổi" (giảng viên Q2, B3)? Câu này suy ra từ LOCK:204-207 và PROJ (giờ đón = max(giờ tới, giờ đón sớm
   nhất)), chưa có ví dụ trong dữ liệu.
9. **Nêu tên "Claude và Codex"** ở 3.7.3 (câu hỏi của bản 1) vẫn để ngỏ.
10. **Phụ lục C** nên định nghĩa "15 kịch bản hiệu chỉnh" và ánh xạ LOCKS/B1/C1.

## 9. Bằng chứng còn thiếu (nên không viết)

- Chu kỳ lượt quyết định; độ dài một lần chạy mô phỏng tính bằng giờ hoạt động.
- Nguyên nhân các lần dời sớm 1 ms (Phụ lục 1, 0.2).
- Bộ chạy và luật phục hồi của 8 lần chạy chiều tuyết.
- Giá trị $K$ của từng cấu hình trong phép thử dự báo trong bộ điều phối (X3-29).
- Tên hội nghị của Hörl–Zwick.
- Cấu hình máy của các số thời gian chạy.
- Một khách thật có đủ $v$, $e$, $p$ của một lần sửa đã được lần tay.
