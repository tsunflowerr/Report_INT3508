# CH3 — Nhật ký sửa Chương 3 theo bốn bản nhận xét R23 (2026-10-11)

**Đầu vào:** bản nháp 1 `drafts/07-chuong3.tex` (giữ nguyên) và NOTES; bốn bản nhận xét: kiểm chứng sự kiện
`reviews/R23-FACTCHECK-CH3-CLAUDE.md` (**FC**), giảng viên `reviews/R23-LECTURER-CH3-CLAUDE.md` (**LE**), người đọc
`reviews/R23-READER-CH3-CLAUDE.md` (**RD**), Codex `optimize/codex-debate/codex-work/R23-CH3-REVIEW-CODEX.md` (**CX**).
**Đầu ra:** `drafts/07-chuong3-v3.tex` (bản sửa chính thức). `drafts/07-chuong3-v2.tex` là bản trung gian (lượt rút gọn
thứ nhất, xem mục 8), không dùng để ghép. Sổ bằng chứng mới: `evidence/EVIDENCE-REGISTER-ADDENDUM-2-CH3.md` (X3-xx).

**Cách kiểm.** Một nhận xét không đúng chỉ vì người nhận xét nói vậy. Với mỗi nhận xét có tính sự kiện, tôi mở mã chỉ đọc
ở `C:/Code/RideBound-noworse/src/` (HEAD `761915c`; `git diff 45f8026 HEAD -- src tests` rỗng, tức trùng nguồn bộ chạy
lưu trữ), cấu hình `tang3/configs/`, script và output được trỏ. Anchor ghi theo khóa của sổ chính và Phụ lục 2.
**Quyết định:** **A** = nhận; **M** = nhận có sửa (lý do ghi kèm); **R** = không nhận (lý do ghi kèm). "Thay đổi" chỉ
chỗ trong v3 (mục, bảng, câu).

---

## 0. Câu hỏi then chốt: $L_r$ được cộng khi nào, nhất là khi $p = v$? (LE §3.2.c, A3)

**Trả lời từ mã:** mỗi phương án được kiểm trên một bản sao trạng thái, sổ giả định bị bỏ (HVA:144-174); chỉ quyết định
cuối của lượt, sau khi bộ kiểm chạy lại trên cả đội xe, mới đi vào trạng thái thật (RS:956-987). Ở quyết định đó, với
mỗi khách có lời hứa, `unchanged` đúng khi **cả ba** véc-tơ $x$, $c$, $z$ đều bằng 0 (VALID:562-565); nếu không, một
bản ghi sửa được thêm (VALID:567-597) và `BudgetAfter = BudgetBefore + |c|` theo cơ sở do điều phối (LEDGER:285-288).
Với $v = p = 600$, $e = 720$: $x = 120$, $c = -120$, $z = 0$, nên `unchanged` sai, bản ghi sửa được thêm với lời hứa
công bố không đổi, và $L_r$ **tăng 120 giây**. Khách được miễn trừ cũng bị cộng như mọi lần công bố (VALID:640-644).

**Hệ quả cho bản 1:** giới hạn thứ ba (CE-3) đúng; Định nghĩa 3.1 ("khi lời hứa mới được công bố") và dòng 14 của giả mã
("khách có lời hứa mới hay thay đổi") sai phạm vi. v3 sửa: Định nghĩa 3.1 cộng $|p_r - e_r|$ "với mỗi khách có lời hứa
mà phương án được chọn làm $x$, $c$ hay $z$ khác 0 … kể cả khi giờ trả công bố không đổi"; giả mã dòng 15 tương ứng;
giới hạn thứ ba nói thêm "$L_r$ tăng 120 giây dù giờ công bố không đổi". Câu "tổng $|c|$ cả chuyến không vượt $B$" giữ
được, kèm điều kiện "khi phép kiểm không được miễn cho $r$" (X3-25).

---

## 1. Chỗ các bản nhận xét bất đồng và cách giải

| # | Chủ đề | Ý kiến | Kiểm bằng chứng | Kết luận trong v3 |
|---|---|---|---|---|
| 1 | Kết thúc lần chạy (Hình 3.3) | FC #104: không có `finalizeRun`/`runSummary`, lần chạy kết thúc bằng `shutdown`, bộ chạy không trả lời. CX §3 (dòng 600–613): "ending exchange refers to finalizeRun→runSummary, not shutdown" | RS:201-214 chỉ xử lý `hello`, `initializeRun`, `eventBatch`, `decisionApplied`, `checkpoint`, `restore`; RS:177-190 `shutdown` → dừng, không trả lời; `grep finalizeRun` chỉ thấy ở `ProtocolEnvelopeCodec.cs:35-36`, PRP:114-115; RC:158-273 không gửi | FC đúng, CX sai. Hình 3.3 kết thúc bằng "kết thúc: bộ chạy dừng, không trả lời" (X3-15) |
| 2 | Số loại sự kiện | FC §2 X3-01: 14 loại | EVB:45-59 có 13 nhánh | 13 (sổ X3-01 CORRECTED); chương không nêu số |
| 3 | Cách nói về −1 ms | ADD1 §0.2: "không có tác dụng đo được"; FC #29: giữ câu nhưng thu phạm vi; LE C4/B2: "gần như không đổi kết quả"; CX §2.7: quá tuyệt đối, tổng sớm của C-30 là 4 ms đo được | ADD1:104-112 (4 cấu hình × 34 kịch bản; mỗi lần sớm đúng 1 ms) | Thu phạm vi (bốn cấu hình, 136 lần chạy) và viết "chiều sớm chưa cho thấy tác dụng đáng kể"; không nêu nguyên nhân |
| 4 | Số đo trong chương phương pháp | LE §6, C2: chuyển 3.503/3.506/3.504, 1.025, 382.006…, 13 hạng mục, thời gian chạy sang Ch. 4/Phụ lục C; OUTLINE-V2 §3.7 đòi 1.025, 382.006, 13/13, thời gian chạy ở 3.7; CX: số bão hòa "can stay" | OUTLINE-V2:176 | Theo OUTLINE cho các số kiểm tra (giữ ở 3.7.3, 3.7.2); theo LE cho số bão hòa (chuyển sang mục 4.10, chỉ giữ câu cơ chế) |
| 5 | Ô "Khi xe bị ép" của điều phối không trần | RD D4: "Không xảy ra: U không kiểm giờ trả, khóa so với mốc giữ nguyên"; CX §2.4: cần điều kiện, lỗi khác vẫn làm lượt thất bại | HVA:328-390; RS:941-947 (X3-31) | "Không bị ép khi (N) đúng" cho cả U và C |
| 6 | Phạm vi của công thức 7 (Hörl–Zwick) | LE §4.1e, REG J05: chỉ khách trên xe sắp vi phạm; HZ eq 7: "all requests that are assigned to the currently evaluated vehicle" | HZ:531-543 (văn bản chiến lược B: khách trên xe), 565-606 (công thức 7) | Viết điều cả hai đều đúng: "phần nới của họ chỉ tác dụng khi giờ cập nhật đã vượt giờ trả muộn nhất" |
| 7 | Tên sổ | RD F1: một tên; GLOSSARY: "sổ cái"; OUTLINE-V2: "sổ theo từng khách"/"sổ theo dõi từng khách" | WRITING-BRIEF: OUTLINE có hiệu lực trên GLOSSARY | Một tên "sổ theo từng khách" (cả tiêu đề mục 3.6) |
| 8 | Giải thích "vì sao" cho thứ tự tiêu chí | LE §6, B4 muốn lý do đặt "nhận nhiều yêu cầu" trước "ổn định" | Không có văn bản nêu lý do (SEL:283-303 chỉ chú thích tiêu chí 1) | Không viết lý do; câu hỏi cho chủ nghiên cứu |
| 9 | `engelhardt2026` thay `fleetpy2022`? | NOTES v1: "có thể thay"; CX §2.8: hai bài khác nhau, không ghi đè | FLEET:1-12 (10 tác giả, ETRR 2026); TEX10:57-61 (7 tác giả, arXiv 2022) | Chương 3 trích `engelhardt2026`; giữ `fleetpy2022` nếu chương khác trích, không ghi đè |
| 10 | Mô tả "khóa" có gồm điểm trả | FC #36, CX: điểm trả là trần 0, không thuộc `finalConfirmationLocks`; RD D3: viết "Khóa xe, điểm đón, điểm trả và giờ đón" | CFG C-30.json:66-67, 94-98; LOCK:42-60 | "Khóa xe, điểm đón, giờ đón; điểm trả có trần 0" |
| 11 | Mức buổi sáng của luật trần độ dời khách thấy | FC không nêu; CX §2.4: V còn chạy ở 90–240 | RW7:5; RW7X:3-4, 35-36 | Bảng 3.5 ghi 30, 90, 120, 150, 180, 240 (X3-28) |
| 12 | "Bản ghi chặn" | LE C4: đổi thành "bản ghi lý do loại"; RD C9: định nghĩa | Chương 4 phần A dùng "bản ghi chặn" (`08-chuong4-phanA.tex`) | Giữ "bản ghi chặn" để khớp Ch. 4, định nghĩa một lần "(bản ghi lý do loại phương án)" |

---

## 2. Kiểm chứng sự kiện (FC)

| # | Dòng v1 | Nhận xét | Kiểm (anchor) | QĐ | Thay đổi trong v3 |
|---|---|---|---|---|---|
| FC1 | 50-53 (#7) | "So với bộ điều phối thông thường" không có bằng chứng | Không dòng sổ nào; J01 cho thấy mốc $e$ đã có | A | 3.1.3: "Ngoài sinh phương án và chọn, mỗi lượt có ba bước cho lời hứa…" |
| FC2 | 64-77 (#8) | Câu so sánh trong chú thích Hình 3.1; vế dự báo cần phạm vi; thiếu EV | F03, F12 | A | Chú thích mới: lời hứa $p$; $D$ tính sau khi chạy "trong các kết quả chính"; có dòng EV |
| FC3 | 100-101 (#10) | Giả mã dòng 7 sai với phương án giữ nguyên (được nới) | GEN:161-246; SQA:61-94 | A | Giả mã dòng 6–7; Bảng 3.2 cột vai trò; đoạn sau giả mã (X3-23) |
| FC4 | 126-127 (#14) | "Bộ lọc cứng … không bị phạt" sai khi xe bị ép; EV dùng K43 sai | HVA:255-326; SEL:283-295; N-21 | A | Thêm câu ngoại lệ (dòng 9–11, tiêu chí 1); EV đổi sang A06, HVA:62-66 |
| FC5 | 159-160 (#24) | Thời gian dừng 0 s chỉ kiểm 3 lần chạy | SERV:2-4 (REG B05) | M | Bỏ hẳn câu thời gian dừng khỏi Ch. 3 (giới hạn mô hình thuộc mục 4.11); giữ câu hệ số chung trong Bảng 3.1 |
| FC6 | 219-220 (#29) | Phạm vi "−1 ms" | ADD1:104-112 | A | "Ở bốn cấu hình đã kiểm … 136 lần chạy" |
| FC7 | 261-263 (#35) | Vai trò ràng buộc dịch vụ sai với phương án giữ nguyên | như FC3 | A | Bảng 3.2: "Phương án đổi kế hoạch phải thỏa chặt; phương án giữ nguyên được nới…" |
| FC8 | 315-316 (#41) | "Dừng ở khách gặp trước" không đúng cho tập tắc đường cố định | VALID:222-231; NEW:13; WP4:1-25 | A | "Ở tập kiểm tra chính và tập chỉnh trần buổi sáng, phép kiểm dừng ở khách vi phạm gặp trước" |
| FC9 | 359-360 (#51) | "Bốn luật khác chạy trên cùng bộ điều phối" sai với ghép tự do và bộ chạy cũ | HO:109; A17; B17 | A | 3.4 mở: "Trừ ghép tự do, chúng dùng cùng…; tập tắc đường cố định chạy bằng bộ chạy chưa có luật phục hồi" |
| FC10 | 395-396 (#57) | "30–60 giây" mâu thuẫn Bảng 3.5 (buổi sáng tới 300) | B15, B16, D04, X3-28 | A | Đoạn Schulz–Pfeiffer bỏ khoảng số; Bảng 3.5 liệt kê mức theo tập |
| FC11 | 413 (#62) | "Gần nhất" nói quá | J01 | A | "Tiền lệ trực tiếp" |
| FC12 | 439 (#75) | "Mỗi lần miễn được ghi thành vi phạm" sai (có khử trùng) | VALID:599-638 | A | "…trừ khi lời hứa, giai đoạn và mã lỗi không đổi so với lần trước" (X3-09b) |
| FC13 | 612-613 (#104) | Hình 3.3: `finalizeRun`/`runSummary` không được dùng | RS:177-214; RC:158-273 | A | Mũi tên cuối "kết thúc: bộ chạy dừng, không trả lời" (xem mục 1, #1) |
| FC14 | 631, 633 (#108) | "Chỉ được đo cho cả lần chạy" không có bằng chứng | Có công cụ đo vi mô chưa kiểm phạm vi | A | "Khóa luận chỉ báo thời gian của cả lần chạy"; "Chi phí riêng … không được báo" |
| FC15 | 45 (#3) | Thiếu EV cho "mỗi xe một kế hoạch" | SEL:298-303 | A | EV 3.1.2 có A14, X3-22 |
| FC16 | 111-117 (#13) | Bộ giải là CP-SAT theo mức | ORT:3, 96-125 | A | Phương trình (3.1) + "giải lần lượt"; Bảng 3.8 "CP-SAT" |
| FC17 | 129-131 (#16) | Tên "(forced decision)" gắn với "xe bị ép" | — | A | Bảng 3.1: "Quyết định bị ép (forced decision)" |
| FC18 | 265-267 (#36) | Điểm trả là trần 0 | CFG C-30.json:66-67 | A | Bảng 3.2, Bảng 3.5 |
| FC19 | 316-317 (#42) | Chỉ 4/10 chiều có trần | CFG C-30.json:7-89 | A | "Chỉ bốn chiều có trần" |
| FC20 | 378-379 (#53) | Ghi HO:109 cho "chi phí cuốn chiếu" | HO:109 | A | EV hàng FREE; cụm thay bằng "chọn theo chi phí kế hoạch ở từng lượt" (X3-38) |
| FC21 | 418-419 (#66) | Khác biệt là so với chiến lược B gốc | HZ:531-543 | M | "Luật C khác ở ba chỗ" đặt sau phần công thức 7, kèm câu phạm vi phần nới (mục 1, #6) |
| FC22 | 452-463 (#79) | Thiếu giữ khung 8 | STRETCH:7-8, 45-52; W13:51 | A | 3.5: $\tilde m_i = m_{\min(i,8)}$, đồng hồ tính từ đầu khung giờ |
| FC23 | 507-509 (#86) | "Lời hứa giờ đón đầu" | FFA:87-89, 99 | A | "giờ đón hiển thị ở lời hứa đầu" |
| FC24 | 548-549 (#95) | Anchor `.NET 10` sai tệp | csproj | A | EV X3-14 (CORRECTED) |
| FC25 | 562-576 (#98) | Bảng bỏ Infrastructure | `Runner.csproj:7` | R | Bảng ghi "thành phần chính"; Infrastructure không cần cho phương pháp |
| FC26 | 624-626 (#105) | Giới hạn 2 yêu cầu áp cho cả lô | GEN:54-96 | A | Giả mã dòng 3 "chọn tối đa 2 yêu cầu đang chờ có giờ đón muộn nhất sớm nhất" (X3-32) |
| FC27 | 626-628 (#107) | "Tỉ lệ với" → "tăng theo" | DELTA:190-215 | M | Thay bằng cách viết của CX §2.5 (không tuyến tính, chưa đo) |
| FC28 | 644-646 (#111) | "năm cấu hình" | B10 | A | 3.7.3 |
| FC29 | 648-649 (#113) | Thêm "trong phạm vi đã kiểm" | K41 | A | 3.7.3 |
| FC30 | §5 | EV sai/thiếu (K43, dòng 45, 553, đoạn không EV) | — | A | Mọi đoạn có sự kiện có `% EV:` (65 dòng) |
| FC31 | §2 cuối | Đưa (a)–(f) vào sổ | — | A | Phụ lục 2: X3-23, X3-09b, X3-15, X3-22, X3-38; LOCKS=U (NEW:11) chỉ trong EV vì chương bỏ tên LOCKS |

---

## 3. Giảng viên (LE)

| # | Mục LE | Nhận xét | Kiểm (anchor) | QĐ | Thay đổi trong v3 |
|---|---|---|---|---|---|
| LE1 | §2.1, A6 | Điều gì kích hoạt một lượt | FC:395-429 | M | Câu mở 3.1.2; chu kỳ gọi chưa kiểm nên không ghi (câu hỏi chủ nghiên cứu) |
| LE2 | §2.2, A6 | Yêu cầu chưa nhận: từ chối hay xét lại | RCP:173-226 | A | Đoạn vòng đời 3.1.1 |
| LE3 | §2.3, A7 | Giai đoạn khách; luật C áp từ đâu | VALID:272-336 | A | Đoạn vòng đời; Định nghĩa 3.1 "chờ đón hay đang trên xe" |
| LE4 | §2.4, A6 | Biến, ràng buộc liên kết, cách cài thứ tự tiêu chí, bộ giải nào | ORT:343-365, 96-125 | A | Phương trình (3.1) và câu "giải lần lượt"; CP-SAT ở Bảng 3.8 |
| LE5 | §2.5 | Giữ 100 theo gì; giữ nguyên có luôn được giữ; 2 yêu cầu chọn thế nào | RET:102-113; GEN:54-96 | A | (N) nêu "luôn giữ phương án giữ nguyên khi cắt"; giả mã dòng 3, 6 |
| LE6 | §2.6, B4 | "Mức dùng trần" chưa định nghĩa | HVA:537-636 | A | 3.4: "tỉ số lớn nhất giữa phần đã dùng và trần" |
| LE7 | §2.7, B9 | Mười chiều chỉ nêu bốn | DELTA:137-153 | A | 3.3 liệt kê đủ mười |
| LE8 | §2.8, B6 | "Không tệ hơn" đo bằng gì; luật 2 mở rộng luật 1; "khóa theo giai đoạn" | VALID:791-818; LOCK:42-60 | A | Đoạn luật phục hồi 3.4 |
| LE9 | §2.9 | Hai định nghĩa "xe bị ép" | HVA:255-326; RS:1013-1027 | A | Một định nghĩa ở Bảng 3.1, khớp mã (X3-30) |
| LE10 | §2.10, A3 | Mâu thuẫn lúc cập nhật $L_r$ | mục 0 | A | Định nghĩa 3.1, giả mã dòng 15, giới hạn thứ ba |
| LE11 | §2.11, A7 | Tắc đường đẩy kế hoạch giữ nguyên quá cửa sổ thì (N)? Xe kẹt thì sao | GEN:161-246; RED:260-282; RS:941-947 | A | Đoạn sau giả mã 3.1.3; (N)(i) chỉ còn ràng buộc cấu trúc; giới hạn thứ nhất |
| LE12 | §2.12 | "Công bố" là gì; 1 ms có tính | VALID:562-597; FC:882-893 | A | Bảng 3.1 "Công bố"; 3.6 "Không có ngưỡng … không phải số lần một ứng dụng thật báo lại" |
| LE13 | §2.13 | Dự báo áp cho cả giờ đón | DISP:3-5 | A | 3.5 câu mở; chú thích Bảng 3.6 |
| LE14 | §2.14 | Tập thử dùng trước khi định nghĩa | — | A | Chú thích Bảng 3.5 trỏ mục 4.1; "kịch bản" ở Bảng 3.1 |
| LE15 | §2.15 | Đơn vị "quyết định" | SPEC:31-34; RS:1013-1027 | A | "mỗi quyết định ứng với một lượt của cả đội xe"; 3.503… chuyển sang 4.10 |
| LE16 | §2.16, B12 | Cấu hình máy, có tính FleetPy không | EL17 chỉ có `elapsedMs` | R | Không có bằng chứng; thêm "không dùng để so chi phí tính toán"; câu hỏi chủ nghiên cứu |
| LE17 | §3.1a | Phương án giữ nguyên phải còn sau khi cắt 100 | RET:102-113; N-25 | A | Là sự kiện cài đặt, nêu ngay sau (N) |
| LE18 | §3.1b | $p = e$ là tính chất cài đặt, phải thành giả thiết | VALID:355-360, 1048-1064; HVA:144-165 | A | (N)(ii) + câu "RideBound thỏa (ii) vì…" |
| LE19 | §3.1c | Khóa không cần là giả thiết | LOCK:156-161 | A | (N) chỉ còn ràng buộc cấu trúc; câu "Khóa và các trần 0 cũng so với kế hoạch giữ nguyên" |
| LE20 | §3.2b, A2 | Quy nạp quá gọn, vòng | HVA:255-259 | A | Đoạn quy nạp riêng, có điều kiện "(N) đúng ở mọi lượt" |
| LE21 | §3.2d | Giữ "Chứng minh … □" | — | A | Giữ |
| LE22 | §3.3 | Nói thẳng tính chất và giới hạn hai là hai mặt; ô bảng thêm "(N)"; U cũng có | — | A | Câu cuối giới hạn; Bảng 3.5; "tính chất này vì vậy không riêng của luật C" |
| LE23 | §3.3, A5, §5.1 | Đoạn đóng góp ở OUTLINE §6.1 (28/34, "trần nới rộng") | — | R | Ngoài tệp Chương 3; chuyển cho người viết Chương 1 (NOTES mục 7) |
| LE24 | §4.1a, A4 | Bỏ mất ràng buộc cứng 9–10 | HZ:565-606 | A | Đoạn Hörl–Zwick |
| LE25 | §4.1b, A4 | "Không nới theo tắc đường" dễ hiểu sai | đại số trên định nghĩa | A | "phần được phép dời, $|c| \le B - L_r$, không phụ thuộc tắc đường"; $c \le \max(p_0 + B - e, 0)$ |
| LE26 | §4.1c | "cũng" → "đã … khóa luận dùng lại" | — | A | 3.2 |
| LE27 | §4.1d | Cùng động cơ | HZ:481-497 (J02) | A | "cũng là mục đích của Nhận xét 3.1" |
| LE28 | §4.1e | Phạm vi áp dụng | mục 1, #6 | M | Viết phần chắc chắn đúng |
| LE29 | §4.2, A1 | Thiếu Fielbaum và Alonso-Mora | FAM:90-94, 293-296, 948-972 | M | Đoạn ngắn ở 3.4 (chi tiết dữ liệu và mục 6 thuộc mục 2.2) + câu ở 3.2 về chiều sớm |
| LE30 | §4.3a, B5 | Thời gian đi cố định của họ; số bị ép nói về hạn chót chặt | J10 | A | Đoạn Schulz–Pfeiffer |
| LE31 | §4.3b | Vì sao 30–60 giây | SWP:15-18; D03:214-217 | M | "mỗi độ chùng bằng một mức trần của luật C trên cùng tập"; lý do sâu hơn: câu hỏi chủ nghiên cứu |
| LE32 | §4.3c | Nêu $l_i = B_i + l$ | J10 | M | "hạn chót tính từ lời hứa đầu"; không thêm công thức (trang) |
| LE33 | §4.4 | Trỏ `alonsomora2017`, mục 2.1 | HZ:341-345; J17 | A | 3.1.2 |
| LE34 | §4.4 | "Không tệ hơn" không nhận là mới | OUTLINE §6.4 | A | "chi tiết cài đặt, không phải đóng góp" |
| LE35 | §4.4 | Ichoua và cộng sự 2003 | Bài chưa mở, không có trong danh mục | R | Không trích, không viết câu văn liệu |
| LE36 | §5.1 (164-165), B1 | Câu nhân quả trong ví dụ | — | A | "ghép khách M làm A tới muộn hơn lời hứa 70 giây, nhưng chỉ 30 giây là phần dời do điều phối" |
| LE37 | §5.1 (240), B11 | Khẳng định không điều kiện | X3-25 | A | "Khi phép kiểm không được miễn cho $r$ ở lượt nào…" |
| LE38 | §5.1 (96), B10 | "luôn dựng trước" mâu thuẫn | GEN:171-182 | A | Giả mã dòng 5–6 tách trường hợp lỗi cấu trúc |
| LE39 | §5.1 (128-129), B10 | Suy luận "giữ thứ tự nên không đổi xe" sai | GEN:548-575 | A | "không bỏ, không đảo điểm cũ nào, nên…" |
| LE40 | §5.1 (341), C4 | "dữ liệu chỉ khớp" cụt | — | A | "số liệu chỉ phù hợp với nó" |
| LE41 | §5.1 (509), C10 | "trước khi triển khai" | — | A | "trước khi đưa dự báo vào bộ điều phối" |
| LE42 | §5.1 (644), B7 | "Kiểm đặc tả" lớn hơn việc làm | T38I:68 | A | "Kiểm tính nhất quán của sổ … không kiểm $e$ có được tính đúng" |
| LE43 | §5.1 (647), B7 | "Tính lại độc lập" | ADDENDUM-1:15-19 | A | "độc lập về mã nhưng dùng cùng đặc tả chỉ số"; "ít nhất hai bộ đọc viết độc lập" |
| LE44 | §5.2 Q1, B2 | Vì sao tính chiều sớm | DELTA:259-262 | A | "vì luật đo lần sửa lời hứa chứ không đo lợi hay hại" + so Fielbaum |
| LE45 | §5.2 Q2, B3 | Khóa giờ đón chặt; chèn trước điểm đón | LOCK:204-207 | M | Bảng 3.2 nói rõ "phải bằng"; hệ quả chèn trước điểm đón không viết (trang) |
| LE46 | §5.2 Q3–Q5, Q7–Q9 | IP; (N) và tắc đường; tầm thường; cộng dồn; 15/11; số lần báo | như LE4, LE11, LE22, N-15, LE12 | A | Như các dòng tương ứng; trỏ mục 4.5 cho cộng dồn |
| LE47 | §5.2 Q6 | Sao không chạy hạn chót nới; luật hạn chót công bằng? | K27 | M | "suy luận, chưa chạy"; đoạn công bằng Schulz–Pfeiffer |
| LE48 | §5.2 Q10, B7 | Chạy lại `dotnet test` | Nhiệm vụ cấm build | R | Giữ "số ghi lại lúc đó, chưa chạy lại"; câu hỏi chủ nghiên cứu |
| LE49 | §5.2 Q11, B7 | Lần tay một khách thật | Không có bản ghi đủ $v$, $e$, $p$ đã kiểm cho một khách | R | Câu hỏi chủ nghiên cứu (NOTES mục 8) |
| LE50 | §5.2 Q12 | Thời gian chạy so chi phí? | EL17 | M | "không dùng để so chi phí tính toán" |
| LE51 | §6, C1 | Mở chương bằng ý chính | — | A | Đoạn mở chương |
| LE52 | §6 | Câu "vì sao" | — | M | Có cho chiều sớm, cộng dồn (định nghĩa 90 giây), dự báo; không cho thứ tự tiêu chí (mục 1, #8) |
| LE53 | §6, C2 | Chuyển số đo | mục 1, #4 | M | Chuyển số bão hòa; giữ số OUTLINE đòi |
| LE54 | §6, C8 | Câu dài | — | A | Tách câu ở 3.4, 3.5, 3.7 |
| LE55 | §6, C3 | 13 cụm tiếng Anh | — | A | Gom vào Bảng 3.1; trong văn chỉ còn "per-rider ledger", "replay" |
| LE56 | §6, C4 | Cụm nội bộ nặng | — | A | "tệp chính sách" → "cấu hình"; "1.000.000 phần triệu" → "100%"; "bộ chạy cũ" → "bộ chạy chưa có luật phục hồi"; "hạt giống ngẫu nhiên"; "giới hạn số bước tính"; bỏ "vế này", LOCKS, B1, C1; "bản ghi chặn" giữ và định nghĩa (mục 1, #12) |
| LE57 | §6, C5 | "bảng giờ đi" | — | A | "bảng thời gian đi"/"thời gian đi" |
| LE58 | §6, C5 | Thuật ngữ không thống nhất | — | A | "cửa sổ đón" (định nghĩa một lần), "ràng buộc cấu trúc"/"ràng buộc dịch vụ" phân biệt rõ, "khách có lời hứa của xe", "Tên trong khóa luận", "bốn cấu hình khác" |
| LE59 | §6, C6 | Chuyển Bảng ràng buộc lên 3.1 | — | A | Bảng 3.2 ở 3.1.2 |
| LE60 | A8 | Ký hiệu trùng: khách B/trần B; $k$; $t$; $N$; $p_0$ thừa | — | A | Khách M; chỉ số $j$, số lần $n$; tập ngày $H$; khung $i$; $p_0$ bỏ khỏi Định nghĩa 3.1 |
| LE61 | B8 | Hình 3.1: dự báo trong vòng; thứ tự ô khác giả mã | — | A | Hình mới, ô dự báo nét đứt ngoài vòng, thứ tự khớp giả mã |
| LE62 | C7 | LOCKS, B1, C1 ra phụ lục | — | A | Bỏ khỏi chương; NOTES ghi cho Phụ lục A/C |
| LE63 | C9 | Câu về bỏ 15/11 | DISP:11 | A | "một lựa chọn của khóa luận; hệ thống thật cần quy tắc tự động" |

---

## 4. Người đọc ngoài ngành (RD)

Mọi câu viết lại của RD đã được kiểm: giữ nghĩa và số; chỗ RD để `[TÁC GIẢ ĐIỀN/KIỂM]` được trả lời bằng mã hay để lại
làm câu hỏi. Hai ví dụ số RD đề xuất (dự báo 9:00→9:21, sổ 180 = 30 + 60 + 90) **không** dùng nguyên: v3 dùng ví dụ của
tôi, tính lại bằng hàm `stretch` của dự án (X3-37; NOTES mục 4). Ví dụ dự báo của RD là đúng số học (9:21:00) nhưng
có $t$ trùng đầu khung; ví dụ mới cho $t$ giữa khung để thấy vai trò $g = 1$ ở khung hiện tại.

| # | Mục RD | Nhận xét (rút gọn) | Kiểm | QĐ | Thay đổi trong v3 |
|---|---|---|---|---|---|
| RD1 | M1 | Vì sao tên "C" | Không văn bản nào nói C lấy từ $c$; mã gọi chính sách C1/C2 (POL:139-145) | R | Không giải thích nguồn tên; câu hỏi chủ nghiên cứu |
| RD2 | M2 | Mở chương bằng câu chuyện | — | A | Đoạn mở (rút gọn) |
| RD3 | A1 | Lượt xảy ra khi nào | FC:395-429 | M | Câu kích hoạt; chu kỳ chưa kiểm |
| RD4 | A2 | "khách đã nhận" | — | M | "khách có lời hứa" + vòng đời |
| RD5 | A3 | "bảng giờ đi" | — | A | "bảng thời gian đi" |
| RD6 | A4 | Bốn tên cửa sổ đón | — | A | "cửa sổ đón (từ giờ đón sớm nhất tới giờ đón muộn nhất)" |
| RD7 | A5 | Lời hứa, công bố, dòng sổ | — | A | Bảng 3.1 |
| RD8 | A6 | Ràng buộc cứng, khóa | — | A | Bảng 3.1 (khóa); bullet "Quyết định" và chú thích Bảng 3.2 |
| RD9 | A7 | "lượt" nhiều nghĩa; độ dài thêm | — | M | Ch. 3 chỉ dùng "lượt" cho lượt quyết định; chỉ số đánh giá trỏ Ch. 4; xung đột "lượt phục vụ" ở Ch. 4 ghi cho chủ nghiên cứu |
| RD10 | A8 | "Phương án" chỉ có tiếng Anh; "thông thường" | FC1 | A | Bảng 3.1; câu "Ngoài sinh phương án và chọn…" |
| RD11 | A9 | Hình 3.1 | — | A | Hình mới (LE61) |
| RD12 | A10 | Cách đọc giả mã | — | A | Chú thích "$a \gets b$ nghĩa là gán"; $P_k$, $\pi$ ở phương trình (3.1) |
| RD13 | A11 | Hai chữ "giữ"; giữ 100 theo gì | RET:102-113 | M | Dòng 7 viết lại; nêu "luôn giữ phương án giữ nguyên"; tiêu chí xếp hạng khi cắt không viết (giới hạn chưa từng chạm, N-25) |
| RD14 | A12 | Dòng 9–11 nhiều khái niệm | — | A | Bảng 3.1 + đoạn sau giả mã có ví dụ trỏ mục 3.4 |
| RD15 | A13 | Quy hoạch nguyên; vì sao chọn chung | ORT:358-365 | A | Phương trình (3.1) |
| RD16 | A14 | "bị phạt trong hàm mục tiêu" | — | A | "không được giữ kèm một điểm trừ" |
| RD17 | A15 | Câu bộ sinh; "nên" | GEN:548-575 | M | Lập luận sửa; ví dụ chèn không thêm (Hình 3.2 đã cho) |
| RD18 | A16 | Ba cụm Anh; "bị ép" chỉ là nhãn | — | A | Bảng 3.1; đoạn sau giả mã |
| RD19 | B1 | Ký hiệu khó nhớ | — | A | "dễ nhớ, $e$ là giờ nếu xe cứ đi như cũ" |
| RD20 | B2 | Vì sao $v = e = p$ ở dòng đầu | SPEC:46; LEDGER:188-207 | A | Chú thích Bảng 3.7: "không có lời hứa trước nên sổ quy ước…" |
| RD21 | B3 | Câu Hörl–Zwick chen giữa định nghĩa | — | M | Giữ một câu ghi nguồn ở 3.2 (LE26), chi tiết ở 3.4 |
| RD22 | B4 | Câu thời gian dừng; "hệ số" chưa định nghĩa | FC5 | M | Bỏ câu thời gian dừng; định nghĩa hệ số ở Bảng 3.1 |
| RD23 | B5 | "phép đo nhân quả" | — | A | "không chứng minh quyết định điều phối thực sự gây ra đúng $c$ giây" |
| RD24 | B6 | "lùi"; 40 giây từ đâu; đơn vị | — | A | "muộn hơn"; chú thích Hình 3.2 giải thích $e$; đơn vị "giây" |
| RD25 | B7 | "theo cấu tạo"; khi nào $c < 0$ | ADD1 §0.2 cấm nêu nguyên nhân chưa kiểm | M | Giữ "không bảo đảm $c \ge 0$"; không điền nguyên nhân |
| RD26 | B8 | "vế này"; "kịch bản" | — | A | Câu mới; Bảng 3.1 |
| RD27 | C1 | $p_0$ định nghĩa mà không dùng | — | A | Bỏ khỏi Định nghĩa 3.1; ở Bảng 3.1 |
| RD28 | C2 | "trên xe" hai nghĩa; ba giai đoạn | VALID:272-281 | A | "khách có lời hứa đang được gán cho xe đó (chờ đón hay đang trên xe)" |
| RD29 | C3 | "không nới theo tắc đường" | — | M | Theo LE25 |
| RD30 | C4 | Bộ chọn và bộ giải | — | A | Bảng 3.1 |
| RD31 | C5 | Chú thích Bảng 3.3 cách đọc tiêu chí | — | A | Chú thích Bảng 3.2 |
| RD32 | C6 | "khóa so với $e$" | — | A | "Giờ đón mới phải bằng giờ đón khi giữ nguyên kế hoạch" |
| RD33 | C7 | Tiêu chí 1 | SEL:283-295 | A | "Ít phương án vi phạm được giữ lại nhất … Chỉ dùng chúng khi không còn cách khác" |
| RD34 | C8 | Tiêu chí 3; [TÁC GIẢ KIỂM] cộng gộp hay lần lượt | SEL:510-522 (một mức cho mỗi chiều) | A | "so lần lượt từng chiều cam kết" |
| RD35 | C9 | "bản ghi chặn"; cập nhật $L_r$ ở cột ghi chú | — | M | Định nghĩa "bản ghi chặn"; ghi chú "$L_r$ chỉ đổi nếu $\pi$ được chọn" |
| RD36 | C10 | Mười chiều | DELTA:137-153 | A | Liệt kê ở 3.3 |
| RD37 | C11 | Định nghĩa bị ép đến muộn; tên (N) | — | M | Định nghĩa ở Bảng 3.1; giữ tên (N) (LE đồng ý) |
| RD38 | C12 | "theo cấu tạo" | — | A | "đúng do cách đặt luật" |
| RD39 | C13 | Một quyết định là gì | SPEC:31-34 | A | LE15 |
| RD40 | C14 | "ràng buộc vật lý", "kẹt" | GEN:171-182 | A | "ràng buộc cấu trúc" với ví dụ; "xe kẹt" ở giả mã dòng 12 |
| RD41 | C15 | 600 giây tính từ mốc nào | — | A | Dùng giờ đồng hồ 9:10:00, 9:11:00, 9:12:00 (hiệu 60 và 120 giây giữ nguyên) |
| RD42 | C16 | Câu giới hạn thứ ba | — | A | Viết lại |
| RD43 | D1 | "độ chùng" | — | A | Chú thích Bảng 3.5 định nghĩa $B$ của luật hạn chót |
| RD44 | D2 | Nguồn ký hiệu U, M⁺, V | Không văn bản | R | Chú thích nói ký hiệu chỉ dùng trong bảng; câu hỏi chủ nghiên cứu |
| RD45 | D3 | Ô khóa của U | CFG C-30.json:66-67 | M | Theo mục 1, #10 |
| RD46 | D4 | Ô bị ép của U | — | M | Theo mục 1, #5 |
| RD47 | D5 | Ô FREE | HO:109 | M | "Không kiểm lời hứa; chọn theo chi phí kế hoạch ở từng lượt" (câu RD giả định "đổi mọi thứ" chưa kiểm, không dùng) |
| RD48 | D6 | Tập thử chưa giới thiệu | — | A | Chú thích Bảng 3.5 trỏ mục 4.1 |
| RD49 | D7 | Đoạn tên gọi | — | A | Bỏ LOCKS, B1, C1; viết lại đoạn Schulz–Pfeiffer |
| RD50 | D8 | Chỉ số; vì sao triệt tiêu; khi nào $v_j \ne p_{j-1}$ | LEDGER:256-269, 298-314 | A | "Trong sổ, mỗi bản ghi sửa so với lời hứa ngay trước nó" (luôn đúng, X3-33) |
| RD51 | D9 | Ví dụ quan trọng nằm xa | — | M | Trỏ tới từ 3.1.3; ví dụ giữ ở 3.4 |
| RD52 | D10 | Đoạn Hörl–Zwick khó | — | A | Viết lại (LE24–28) |
| RD53 | D11 | Tiêu chí 3 khó nhất; [TÁC GIẢ KIỂM] câu kết | HVA:612-626; SEL:319-330 (cực đại trên đội xe luôn ≥ 1.000.000 khi có chiều trần 0 được xếp hạng) | A | "luôn bằng 100% … tiêu chí 3 vì vậy chỉ tác dụng qua tổng phần dời theo từng chiều", phạm vi "các lượt đã ghi" |
| RD54 | D12 | Câu U và C | — | A | Viết lại |
| RD55 | D13 | Luật phục hồi | — | A | Viết lại, một tên mỗi luật |
| RD56 | E1 | Trực giác và ví dụ cho tích phân | — | A | Câu trực giác + ví dụ của tôi (X3-37 a) |
| RD57 | E2 | Ký hiệu $p$, $t$, $b$/$B$ | — | A | Khung $i$; $p$ được giải thích; $t$ chỉ là lúc công bố |
| RD58 | E3 | Hệ số, mức hiện tại | — | A | Bảng 3.1; câu "Mức tắc đường lúc này đã có…" |
| RD59 | E4 | max không rút ngắn | CX §2.2 | M | "bảo đảm $D \ge p$ ở cùng lần công bố, không bảo đảm $D$ tăng dần" |
| RD60 | E5 | Ngày nguồn, 15/11 | DISP:10-16, 34-52 | A | Viết lại; 21 kịch bản thuộc 14–16/11 theo quy tắc |
| RD61 | E6 | Phát lại | — | A | "xe nào chở ai giữ nguyên, chỉ giờ báo cho khách đổi" |
| RD62 | E7 | Câu xung đột giờ đón | FFA:87-89, 99 | A | Viết lại, 1.471 trước 34 |
| RD63 | F1 | Ba tên sổ | — | M | Mục 1, #7 |
| RD64 | F2 | Ví dụ một dòng sổ | — | A | Bảng 3.7 (số kiểm lại) |
| RD65 | F3 | Công thức ba phần bằng lời + ví dụ | — | A | Câu bằng lời; ví dụ 70 = 30 + 30 + 10 (X3-37 b) |
| RD66 | F4 | "tổng có dấu" | — | A | "(dời muộn dương, dời sớm âm)" |
| RD67 | F5 | "hồ sơ lịch sử" | — | A | "$f$ là phần dự báo đã cộng sẵn vào lời hứa đầu" |
| RD68 | F6 | Phần còn lại | — | A | "thay đổi khi giữ nguyên kế hoạch mà dự báo chưa tính, cộng độ lệch…" |
| RD69 | F7 | "trong mô phỏng" | — | A | "giờ trả thực tế trong mô phỏng" |
| RD70 | G1 | Ngôn ngữ kỹ sư | — | M | Rút gọn, bỏ "phụ thuộc từ ngoài vào trong" |
| RD71 | G2 | Tên Việt trong Bảng 3.8 | — | A | "Domain (tầng nghiệp vụ)"… |
| RD72 | G3 | Bối cảnh FleetPy sớm | B01 | A | Câu thứ hai của 3.1.1 |
| RD73 | G4 | "luồng vào, ra chuẩn" | — | A | "chương trình con", "đầu vào, đầu ra chuẩn" |
| RD74 | G5 | Bị động kép | RS:448-455 | A | "chỉ nhận lô mới sau khi bộ mô phỏng báo đã áp dụng quyết định trước" |
| RD75 | G6 | "hạt giống cố định 7" | — | A | "hạt giống ngẫu nhiên (số khởi tạo phần ngẫu nhiên) cố định bằng 7" |
| RD76 | G7 | Lần chạy dài bao nhiêu; vì sao C nhanh hơn | — | M | Thêm câu không dùng để so chi phí; độ dài mô phỏng chưa kiểm (câu hỏi) |
| RD77 | G8 | "năm luật"; "hiệu chỉnh" | RUN38:4-6 | A | "năm cấu hình", "15 lần chạy luật C trần 30 giây trên 15 kịch bản hiệu chỉnh" |
| RD78 | G9 | "bản chạy" | — | A | "bản bộ chạy đã biên dịch và lưu lại" |
| RD79 | G10 | "đệm" chưa định nghĩa | — | A | Câu cuối chương |
| RD80 | X1 | Thuật ngữ trước định nghĩa | — | A | Bảng 3.1 |
| RD81 | X2 | Một khái niệm nhiều tên | — | A | Một tên mỗi khái niệm (LE58) |
| RD82 | X3 | Một ký hiệu nhiều nghĩa | — | A | LE60 |
| RD83 | X4 | Tiếng Anh chen | — | A | LE55 |
| RD84 | X5 | Ví dụ số cho 3.5, 3.6 | — | A | RD56, RD64, RD65 |

---

## 5. Codex (CX)

| # | Mục CX | Nhận xét | Kiểm | QĐ | Thay đổi trong v3 |
|---|---|---|---|---|---|
| CX1 | §2.1 | Kiểm vật lý: nới cho phương án giữ nguyên, chặt cho phương án đổi | GEN:161-246; SQA:61-94 | A | Giả mã dòng 5–7; Bảng 3.2; đoạn sau giả mã |
| CX2 | §2.1 | Mỗi yêu cầu mới thuộc nhiều nhất một xe | ORT:358-365 | A | Phương trình (3.1); giả mã dòng 13 |
| CX3 | §2.1 | Khách được nhận chưa xác nhận không có lời hứa; $L = 0$ từ lúc xác nhận; phương án được xét không dùng sổ thật | VALID:272-301; HVA:144-174; RS:956-987 | A | Vòng đời 3.1.1; Định nghĩa 3.1; câu "kiểm trên bản sao của sổ" |
| CX4 | §2.1 | Thủ tục 10 bước | — | M | Gộp vào giả mã 17 dòng (Bảng 3.3) |
| CX5 | §2.1 | Kiểm lại cả đội xe; nhánh dự phòng | POL:370-401; SEL:72-137 | M | Dòng 13 "kiểm lại lựa chọn trên cả đội xe"; nhánh dự phòng không mô tả |
| CX6 | §2.1 | Ghi nhận đón muộn (`record-v1`) | WP4:8; RED:260-282 | A | Giả mã dòng 2; đoạn sau giả mã (X3-24) |
| CX7 | §2.2 | Giữ khung 8, đồng hồ tương đối | W13:51-82; STRETCH:45-52 | A | Định nghĩa $\tilde m_i$, $i(\tau)$ |
| CX8 | §2.2 | Áp riêng cho giờ đón và giờ trả | DISP:3-5 | A | 3.5 câu mở; chú thích Bảng 3.6 |
| CX9 | §2.2 | max không bảo đảm đơn điệu | DISP:60-64 | A | Câu "không bảo đảm $D$ tăng dần" |
| CX10 | §2.2 | Hình 3.1 đặt dự báo trong vòng | — | A | Ô nét đứt ngoài vòng |
| CX11 | §2.2 | Câu "lời hứa sớm hơn giờ đến thật" quá tuyệt đối | — | A | "có thể sớm hơn … khi đường đông dần" |
| CX12 | §2.2 | Cầu nối sang phép thử dự báo trong bộ điều phối, công thức $r_b$ | W13:1-26, 113-133 | M | Một câu mô tả; công thức $r_b$ và $K$ để Ch. 4 (X3-29) |
| CX13 | §2.3 | Sổ là véc-tơ mười chiều, $x$, $c$, $z$ có dấu chỉ cho giờ | DELTA:137-153 | A | 3.3 và 3.6 |
| CX14 | §2.3 | Bản ghi sửa chỉ khi có véc-tơ khác 0 | VALID:562-597 | A | 3.6 câu đầu |
| CX15 | §2.3 | Nhóm khách dùng $p_0$ không dự báo | FFA:134 | A | 3.6 |
| CX16 | §2.4 | Ô "Khi xe bị ép" của C và U cần điều kiện | — | A | Bảng 3.5 |
| CX17 | §2.4 | Phục hồi kích hoạt khi phương án giữ nguyên bị loại, không đòi mọi phương án bị loại; phân biệt các đối tượng | HVA:255-326; POL:443-463 | A | Bảng 3.1; giả mã dòng 9; luật phục hồi 3.4 |
| CX18 | §2.4 | Đoạn luật phục hồi, khử trùng vi phạm | VALID:599-638, 791-818 | A | Đoạn luật phục hồi |
| CX19 | §2.4 | Mức buổi sáng của V | RW7X:3-4, 35-36 | A | Bảng 3.5 |
| CX20 | §2.4 | Mức luật hạn chót theo tập | RW7, RW7X | A | Bảng 3.5 |
| CX21 | §2.4 | Thêm hàng hạn chót hai phía M-30 nếu Ch. 4 dùng | `08-chuong4-phanA.tex` không dùng M-30 | R | Không thêm hàng; NOTES ghi lại |
| CX22 | §2.4 | Điều kiện bật của bộ chọn; không tổng quát hóa quy ước trần 0 | SEL:271-330; HVA:554-626 | M | Tiêu chí 1 "(chỉ khi có xe bị ép)"; tiêu chí 3 "(khi có chiều mang trần)"; câu 100% giới hạn ở "các lượt đã ghi" |
| CX23 | §2.5 | Bỏ câu độ phức tạp tuyến tính | DELTA:190-215 | A | 3.7.2 viết lại |
| CX24 | §2.6 | Đưa X3 vào sổ trước khi dùng | — | A | Phụ lục 2 |
| CX25 | §2.6 | Anchor `net10.0`, FFA, TEX08:136-138 | — | A | X3-14, X3-12; X3-18 không còn dùng |
| CX26 | §2.7 | −1 ms, thời gian dừng, 13 hạng mục + 1 bất biến, độc lập bộ đọc | ADD1:104-112; T38I:82-95; ADDENDUM-1:15-19 | A | 3.2, 3.7.3 |
| CX27 | §2.8 | Trích dẫn | mục 1, #9 | A | `horl2022`, `engelhardt2026` (NOTES mục 6) |
| CX28 | §2.9 | Nhãn, đánh số, ngân sách trang chưa kiểm | — | A | NOTES mục 1, 5 |
| CX29 | §3 (600–613) | Kết thúc bằng finalizeRun→runSummary | mục 1, #1 | R | Mã cho thấy ngược lại |
| CX30 | §3 (265–267) | Điểm trả không thuộc khóa xác nhận | CFG C-30.json:94-98 | A | Bảng 3.2, 3.5 |
| CX31 | §3 (280) | Mã phương án không đủ để tái lập qua các binary | — | M | Giữ "để chạy lại cho cùng kết quả" trong ngữ cảnh cùng bộ chạy; mục Tái lập nêu điều kiện dựng lại |
| CX32 | §3 (548–552) | "không tham chiếu thư viện nào" quá rộng | csproj | A | "không tham chiếu dự án hay gói thư viện ngoài nào" |
| CX33 | §3 (431–433) | Phép so U–C giữ bộ chọn nhưng không cùng tập khách | C04 | M | Giữ câu; tập khách khác nhau thuộc Ch. 4 |
| CX34 | §4 (dòng 7–12, 2, 8) | Từng dòng giả mã | như CX1–CX5 | A | Bảng 3.3 mới |
| CX35 | §4 (Bảng 3.4 dòng 2) | Duyệt khách có lời hứa, không phải mọi khách "được nhận" | VALID:272-281 | A | "khách $r$ có lời hứa được gán cho xe $k$" |
| CX36 | §4 (Bảng 3.6 dòng 4, 7) | Hồ sơ khung 0…8, giữ đuôi ở cả hai chỉ số | W13:80-89 | A | Dòng 4, 7 |

---

## 6. Số nhận xét theo bản nhận xét

| Bản nhận xét | Số dòng ghi | A | M | R |
|---|---:|---:|---:|---:|
| FC (kiểm chứng sự kiện) | 31 | 27 | 3 | 1 |
| LE (giảng viên) | 63 | 48 | 10 | 5 |
| RD (người đọc) | 84 (79 mục + X1–X5) | 63 | 19 | 2 |
| CX (Codex) | 36 | 28 | 6 | 2 |
| **Tổng** | **214** | **166** | **38** | **10** |

Cách đếm: mỗi dòng của các bảng 2–5 là một nhận xét thực chất (nhận xét chỉ khen hay chỉ xác nhận "OK" không ghi); số
đếm do script đọc cột "QĐ" của tệp này (`count_log.py`, scratchpad phiên). Bất đồng giữa các bản nhận xét ở mục 1 được
tính trong dòng của từng bản.

## 7. Những gì v3 cố ý không làm

- Không viết nguyên nhân của các lần dời sớm 1 ms (ADD1 §0.2).
- Không viết chu kỳ gọi lượt quyết định, độ dài một lần chạy mô phỏng, cấu hình máy, lý do của thứ tự tiêu chí, nguồn gốc
  tên C/U/M⁺/V, hệ số $K$ của phép thử dự báo trong bộ điều phối: chưa có bằng chứng (NOTES mục 8).
- Không dùng "sổ cái", "duy nhất", "đầu tiên" (theo nghĩa mới), "niêm phong", "dự đoán".
- Không thêm tài liệu chưa mở (Ichoua và cộng sự 2003).

## 8. Lịch sử tệp

- `07-chuong3.tex` (v1): giữ nguyên.
- `07-chuong3-v2.tex`: tôi viết bản sửa đầy đủ đầu tiên (6.129 tiếng văn xuôi theo bộ đếm của tôi, quá dài), rồi ghi đè
  chính tệp v2 bằng lượt rút gọn thứ nhất (4.984 tiếng) **trước khi** nhận yêu cầu giữ nguyên v2. Bản 6.129 tiếng vì vậy
  không còn trên đĩa; v2 hiện là lượt rút gọn thứ nhất và được giữ nguyên từ lúc nhận yêu cầu.
- `07-chuong3-v3.tex`: bản sửa chính thức, sao từ v2 rồi rút gọn tiếp (4.052 tiếng văn xuôi, 2.248 tiếng trong bảng và
  hình).

*Hết. Viết bởi Claude (người sửa Chương 3), 2026-10-11.*
