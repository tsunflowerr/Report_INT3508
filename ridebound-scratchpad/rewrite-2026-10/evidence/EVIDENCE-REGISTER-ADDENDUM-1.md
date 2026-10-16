# EVIDENCE REGISTER — PHỤ LỤC 1 (2026-10-11)

**Vai trò.** Bổ sung cho `EVIDENCE-REGISTER.md` (không sửa tệp đó). Ghi các dòng N-01…N-15 mà `OUTLINE-V2.md` §9 yêu cầu,
các số tự tính [A] của OUTLINE-V2 và `REVIEW-DECISIONS-R20.md` (RD), các số của "câu trả lời trung thực" RD §8, và các
dòng Giai đoạn 1a (mục L) từ `tang3/t38c120/C120-RESULTS.md`. Một con số chỉ được ghi ở đây khi output của script đã
lưu cho thấy nó; nếu không, nó nằm ở mục 0 với nhãn UNVERIFIED hoặc CORRECTED.

**Cách tôi kiểm (Claude, evidence registrar, 2026-10-11).**
- `checks-addendum-1/recompute_addendum_1.py` đọc lại **136 transcript thô** (34 kịch bản × U, C-30, C-120, M⁺-30) bằng
  các bộ đọc có sẵn, không sửa: `audit_vep.load/audit`, `sweep_analyze.event_times`, `display_layer.profile/display`,
  quy tắc đệm của `cap_vs_pad_frontier.py` (D = D0 + k), `cumulative_decisive_check.analyze`; thư mục U/C-30/M⁺-30 qua
  `forecast_family_a.run_dir("test", arm, cell)` (dùng `C-30-d20181114-s10-r3-w17-rerun1`, ADD1:6), C-120 ở
  `C:/RideBoundData/research/tier3-t38c120-v1`. Hai tiến trình (tiến trình chính + 1 worker), 2 phút 17 giây, exit 0,
  stderr rỗng.
- Kiểm chéo trong cùng output: 0 lệch số đếm so với Codex A (U, C-30, M⁺-30 × ngây thơ / dự báo / dự báo + 30 s /
  dự báo + 60 s; tổng giây kéo dài lệch 0,000000 ms) (ADD1:34-64); 0 lệch so với bộ đọc độc lập của Codex v4 trên tổng
  và trên **từng khách** của 7.159 khách được phục vụ (t0, p0, A, Σ|c|, số lần dời; lệch D0 lớn nhất 0,000000 ms)
  (ADD1:66-76); 0 lệch so với TSV của Claude trên 7.159 khách được nhận (ADD1:78). TSV của Claude dùng cùng bộ đọc với
  tôi nên đó là phép tái lập; tính độc lập đến từ Codex A và Codex v4.
- `check_snow_c30.py` đọc 8 transcript chiều tuyết (một tiến trình). `derive_addendum_1.py` chỉ làm phép tính trên hai
  output của tôi. `check_anchors_addendum_1.py` kiểm 77 cặp (tệp:dòng, đoạn trích) — **77 OK, 0 FAIL** (ANC1:79) — và
  trích trang PDF bằng `pdftotext` ra stdout; `check_pdf_lot.py` trích mục lục trang 8.
- Python `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B`, `PYTHONIOENCODING=utf-8`; mọi output mở mode "x".
  Không chạy mô phỏng, không build, không cài, không xóa; chỉ ghi trong `rewrite-2026-10/evidence/checks-addendum-1/` và
  tệp này.

**Nhãn.** Như sổ chính, thêm: **VERIFIED-by-me (script)** = số in ra bởi script đã lưu từ transcript thô;
**VERIFIED-by-me (read)** = tôi đọc dòng/trang được trỏ; **CORRECTED** = số trong outline sai hoặc bị thay, giá trị đúng
ghi kèm; **SCOPE** = số đúng nhưng câu trong outline nói rộng hơn tập đã kiểm. Nhãn mẫu số như sổ chính, với "kịch bản"
thay "ô": `[gộp theo khách]`, `[TB theo kịch bản]`, `[trên yêu cầu]` (chia 3.672), `[đếm]`.

**Ràng buộc chủ sở hữu.** Không câu nào ở đây nói về kế hoạch, dự đoán hay đạt/trượt; P1–P5 của C120-RESULTS.md:28-29,
STG:81-86 và CXS:56-66 cố ý không được ghi. Tên luật trong câu: "điều phối không trần" (U), "luật C" với trần 30 / 120
giây (C-30, C-120), "luật hạn chót" (M⁺-30), "đệm 30 giây"; ký hiệu chỉ ở cột số.

## Khóa anchor mới

Đường dẫn tương đối với `E:/Code/Report_INT3508/ridebound-scratchpad/` trừ khi ghi tuyệt đối; `CK1` =
`rewrite-2026-10/evidence/checks-addendum-1/`. Các khóa khác (A, BUC, T38A, W07, CON, SNOW, DEB, XW, CW…) như sổ chính.

| Khóa | Tệp |
|---|---|
| ADD1 | `CK1/recompute-addendum-1-2026-10-11.txt` (script `CK1/recompute_addendum_1.py`; JSON `CK1/recompute-addendum-1-2026-10-11.json`) |
| SNOW1 | `CK1/check-snow-c30-2026-10-11.txt` (script `CK1/check_snow_c30.py`) |
| DER1 | `CK1/derive-addendum-1-2026-10-11.txt` (script `CK1/derive_addendum_1.py`) |
| ANC1 | `CK1/check-anchors-addendum-1-2026-10-11.txt` (script `CK1/check_anchors_addendum_1.py`) |
| LOT1 | `CK1/check-pdf-lot-2026-10-11.txt` (script `CK1/check_pdf_lot.py`) |
| STG / CW21 | `CW/r21-stage1a/stage1a-report-2026-10-10.txt` / `CW/r21-stage1a/cum-witness-check-2026-10-10.txt` |
| CXS / CXJ | `XW/R21B-STAGE1A-CODEX.md` / `XW/R19-stage1a-analysis.json` (Codex v4, bộ đọc stdlib riêng) |
| C120R | `tang3/t38c120/C120-RESULTS.md` |
| R19C | `DEB/ROUND19-CLAUDE.md` |
| TEX10 / TEX08 | `E:/Code/Report_INT3508/ridebound/noi-dung/10-tai-lieu.tex` / `08-chuong4.tex` (chỉ đọc) |
| PDF / DACN | `E:/Code/Report_INT3508/ridebound/main.pdf` (ngày tệp 30/9) / `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf` |

---

## 0. Số trong outline tôi KHÔNG xác nhận được hoặc thấy SAI (đọc trước)

| # | Chỗ trong OUTLINE-V2 / RD | Giá trị trong outline | Kết quả | Giá trị / cách viết đúng | Bằng chứng |
|---|---|---|---|---|---|
| 0.1 | N-05 (OUTLINE §9); RD LR-04 | "C-30 earlier total ≤ ≈ 0,56 s" (suy từ làm tròn, [A]) | **CORRECTED.** Cận đúng nhưng rất lỏng | Tổng phần dời sớm của C-30 là **4 ms = 0,004 s**: 4 khách, mỗi khách đúng một lần c = −1 ms; (Σ\|c\| − Σc)/2 = (359.173 − 359.165)/2 = 4 ms | ADD1:106-107,112 |
| 0.2 | OUTLINE §3.2 ("so 'bộ sinh chỉ chèn thêm' does not imply c ≥ 0 when travel times vary"); RD CX-54, LR-04, §7 hàng "Hai chiều" ("the data show earlier changes") | 2 / 174 (U), 4 / 33 (C-30), 3 / 103 (C-120) khách có tổng dời mang dấu âm | Số đếm **VERIFIED**; nhưng **mọi** lần dời sớm hơn do điều phối trên 34 kịch bản đều đúng −1 ms (U 3 lần ở 3 khách, 2 khách có tổng âm; C-30 4; C-120 3; M⁺-30 4). Không lần dời sớm nào lớn hơn 1 ms | Viết: "c ≥ 0 không được bảo đảm theo cấu tạo; trên các lần chạy đã có, mọi lần dời sớm hơn chỉ là 1 ms, nên vế giá trị tuyệt đối thuộc định nghĩa và không có tác dụng đo được ở đây". Không nêu nguyên nhân của −1 ms (làm tròn mili giây chỉ là giả thuyết, chưa kiểm) | ADD1:104-111,115 |
| 0.3 | OUTLINE §6.3 dòng 5, §6.2 hàng "3", §6.1 câu cuối, N-15 | "trên 132 lần chạy dùng hệ số tắc đường đo, 3 trong 1.780 bản ghi chặn chỉ do cộng dồn" | Số **VERIFIED** cho tập đã kiểm (98 lần chạy cũ + 34 lần chạy trần 120 giây). **SCOPE:** còn lần chạy luật C khác trên hệ số đo nằm ngoài tập đó: 8 lần C-30 chiều tuyết (tôi đã đọc: 163 bản ghi, đều một lần dời vượt trần, 0 chỉ do cộng dồn), 15 lần C-30 hiệu chỉnh của T3.8 và 16 thư mục C-30F (dự báo trong bộ điều phối) — tôi **không** đọc | "trên 132 lần chạy có luật C đã được kiểm toàn bộ bản ghi chặn (98 lần chạy cũ và 34 lần chạy trần 120 giây)"; hoặc kể cả chiều tuyết: **140 lần chạy, 1.943 bản ghi, 3 chỉ do cộng dồn**. Không viết "mọi lần chạy dùng hệ số tắc đường đo" | ADD1:132-133; SNOW1:10; DER1:6; `ls` tier3-t38-v1 (51 thư mục C-30 = 34 + 15 + 2 bản lỗi gốc), tier3-forecast-v1 (16 C-30F) |
| 0.4 | RD §8 mục 4 | "The bound held … on the snow afternoon (dispatch 8,6 of 3.445,9 late seconds, REG F13)" | Anchor sai chỗ: F13 là phần điều phối của khách trễ, không phải trần theo từng khách. Câu thì **đúng** theo kiểm mới | "Trên 8 kịch bản chiều tuyết (601 khách), tổng dời do điều phối lớn nhất của một khách là 25,2 giây; 0 khách vượt trần" | SNOW1:10 (xem N-26) |
| 0.5 | — | — | **UNVERIFIED:** không có số nào trong các mục được giao (N-01…N-15, ba mục [A], câu trả lời RD §8, §7.1) | — | — |

Ngoài phạm vi phụ lục này (vẫn chỉ dựa vào dòng của sổ chính, tôi không chạy lại): Bảng 4.5 phần M⁺-60 (22,5% / 4,2% /
22; gộp 3,4%) và V-30 (53,8% / 21,6% / 34) — REG C13; chờ / ngồi xe của khách chung — C05; ví dụ cơ chế và 148 / 116 /
1.186 / 109,6 s — các dòng D; Bảng 4.9a/b — D01–D09; sàng lọc bộ chọn — H; dự báo 21 kịch bản và chiều tuyết — F (trừ các
số 34 kịch bản đã chạy lại ở đây); kiểm thử và 382.006 lần sửa — A26–A28. Phụ lục này không xác nhận cũng không bác các số đó.

---

## M. Các dòng N (OUTLINE-V2 §9) và số bổ sung

| ID | Câu có thể dùng trong luận văn | Số chính xác | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| N-01 | Khi có dự báo, trong số khách được phục vụ, cách đệm 30 giây trên điều phối không trần có 68 / 11 / 1 khách trễ quá 120 / 300 / 600 giây so với lời hứa, còn luật C trần 30 giây có dự báo có 0 / 0 / 0. | U + dự báo + 30 s: 68 / 11 / 1 trên 2.434; C-30 + dự báo: 0 / 0 / 0 trên 2.338 `[đếm]` | ADD1:15,19,81; A:7,9 | VERIFIED-by-me (script; khớp Codex A) | Đệm U là phát lại lời hứa trên quỹ đạo của U, không phải đối chứng ghép cặp; hai tập khách khác nhau. |
| N-02 | Nếu đệm thêm 30 giây cho cả luật C có dự báo, luật C còn 2 khách trễ quá một phút và có 44 khách tới sớm quá một phút trong 2.338 khách, với lời hứa dài thêm trung bình 37,37 giây. | phục vụ 2.338; trễ60 2; sớm60 44; kéo dài 87.364.334,6 ms / 2.338 = 37,367 s `[gộp theo khách]`; không trễ quá 60 / 120 s: 2.336 / 2.338 `[trên yêu cầu]` | ADD1:20,82; A:7 | VERIFIED-by-me (script) | Phát lại lớp lời hứa. |
| N-03 | Điều phối không trần có dự báo, không đệm, có 137 khách trễ quá một phút, 87 trễ quá hai phút và 8 tới sớm quá một phút trong 2.434 khách; lời hứa dài thêm trung bình 7,18 giây. | trễ60 137; trễ120 87; trễ300 17; sớm60 8; kéo dài 7,183 s; không trễ quá 60 / 120 s: 2.297 / 2.347 | ADD1:14,83; A:9; STG:32; CXS:77 | VERIFIED-by-me (script; 3 bộ đọc khớp) | — |
| N-04 | Tính trên 3.672 yêu cầu, số lượt tới trong khoảng ±60 giây quanh lời hứa là 2.324 cho luật C trần 30 giây có dự báo và 2.284 cho cách đệm 30 giây trên điều phối không trần có dự báo. | C-30 + dự báo 2.324 (63,29%); U + dự báo + 30 s 2.284 (62,20%); U + dự báo 2.289 (62,34%); C-30 + dự báo + 30 s 2.292 (62,42%); C-120 + dự báo 2.320 (63,18%) `[trên yêu cầu]` | ADD1:84-92 | VERIFIED-by-me (script) | Đếm trực tiếp −60 s ≤ A − D ≤ 60 s bằng phục vụ − trễ60 − sớm60 ở mọi cấu hình (ADD1:92): trễ (> 60 s) và sớm (< −60 s) rời nhau theo định nghĩa. Yêu cầu bị từ chối không được tính; số phục vụ khác nhau 96 lượt. |
| N-05 | Trên 34 kịch bản, tổng dời giờ trả do điều phối mang dấu âm ở 2 trong 174 khách bị dời khi không trần, 4 trong 33 với trần 30 giây và 3 trong 103 với trần 120 giây; mỗi lần dời sớm hơn này đúng 1 mili giây. | U 2/174 (3 khách có một bước −1 ms); C-30 4/33, tổng phần sớm 4 ms; C-120 3/103, 3 ms; M⁺-30 4/29, 4 ms | ADD1:104-112; BUC:34,37; STG:37-39 | VERIFIED-by-me (số đếm); **CORRECTED** (cận ≈ 0,56 s → 0,004 s) | Xem 0.1, 0.2. Không dùng để nói vế "hai chiều" có tác dụng đo được. |
| N-06 | Trên 34 kịch bản chính, luật C với trần 120 giây phục vụ 2.387 lượt; 132 / 21 / 0 lượt trễ quá 60 / 120 / 300 giây; 2.255 lượt không trễ quá một phút và 2.366 không trễ quá hai phút; khi có dự báo là 65 / 8 lượt trễ, 2.322 và 2.379 lượt không trễ, lời hứa dài thêm 7,27 giây. | phục vụ 2.387; sớm60 1 (dự báo: 2); dự báo: trễ60 65, trễ120 8, kéo dài 17.362.762,5 ms / 2.387 = 7,274 s `[gộp theo khách]`; timely `[trên yêu cầu]` | ADD1:7,22,24,196-200; STG:29,34; CXS:76,79; C120R:14-15 | VERIFIED-by-me (script; khớp Codex v4 từng khách) | Không gọi là tối ưu (REG K36). |
| N-07 | Dưới trần 120 giây, 103 trong 2.387 khách (4,32%) có giờ trả bị điều phối dời, không ai bị dời từ hai lần, tổng dời lớn nhất của một khách là 118,9 giây, 9 khách dùng từ 90% trần trở lên, 0 khách vượt trần và 0 trong 20.435 quyết định bị ép. | bị dời 103; ≥ 2 lần 0; lớn nhất 118,938 s; ≥ 0,9 B: 9; ≥ 0,5 B: 54; vượt 0; ép 0 / 20.435; Σ\|c\| của khách bị dời: TB 55,50 s, trung vị 62,54 s, p90 104,87 s (thứ hạng gần nhất) | ADD1:7,108,121; STG:39,44; CXS:89 | VERIFIED-by-me (script; 3 bộ đọc) | Mẫu số: khách được nhận (ở đây = khách được phục vụ, 2.387). |
| N-08 | Trên 34 lần chạy trần 120 giây, 524 bản ghi chặn do trần gồm 521 bản ghi có một lần dời vượt 120 giây và 3 bản ghi chỉ do cộng dồn, ở 3 quyết định khác nhau; trong 3 yêu cầu mới liên quan, 2 cuối cùng không được nhận dưới trần 120 giây (một trong hai cũng không được nhận dưới trần 30 giây) và 1 được phục vụ. | 524 = 521 + 3; giới hạn ghi trong bản ghi 120.000 ms cho cả 524; yêu cầu rq-ebccd435e2…: C-120 bị từ chối / C-30 và U phục vụ; rq-fe75a63d2e…: phục vụ ở cả ba; rq-3e35891595…: C-120 và C-30 bị từ chối / U phục vụ | ADD1:127-130; STG:44-47; CW21:2-7; CXS:91,95-101 | VERIFIED-by-me (script; quy tắc riêng + `cumulative_decisive_check` + Codex) | Theo bản ghi, kiểu dừng ở lỗi đầu; không chứng minh cộng dồn làm mất yêu cầu; nhánh mỗi lần một trần chưa chạy (REG E09). |
| N-09 | Số khách đi chung là 555 trong 2.434 (22,80%) khi không trần, 313 trong 2.338 (13,39%) với trần 30 giây và 428 trong 2.387 (17,93%) với trần 120 giây. | `[gộp theo khách]`; trên yêu cầu 15,11% / 8,52% / 11,66%; M⁺-30 307 / 2.338 (13,13%) | ADD1:136-139; STG:50-52 | VERIFIED-by-me (script; cùng quy tắc với STG) | Đi chung = có khách khác trên cùng xe với khoảng [giờ đón thực tế, A) chồng nhau. Thay số "≈" của REG C25. Codex không đếm lại chỉ số này. |
| N-10 | Hai tập khách được phục vụ khác nhau: trần 120 giây và trần 30 giây chung 2.266 lượt, 121 lượt chỉ có ở trần 120 giây (93 trong đó cũng được phục vụ khi không trần) và 72 chỉ có ở trần 30 giây; trần 120 giây và không trần chung 2.271, riêng 116 và 163. | 2.266 / 121 / 72; 2.271 / 116 / 163; 93 / 121; U–C-30 2.207 / 227 / 131; C-30–M⁺-30 2.332 / 6 / 6 | ADD1:143-147; STG:55-58; CXS:109-111 | VERIFIED-by-me (script; 3 bộ đọc) | Đếm theo (kịch bản, mã yêu cầu). Không viết "lấy lại 49 trong 96 lượt". |
| N-11 | Theo khung giờ, trần 120 giây phục vụ 515 / 1.001 / 871 lượt so với 511 / 975 / 852 của trần 30 giây ở khung 7 / 8 / 17 giờ, với 63 / 49 / 20 so với 61 / 15 / 0 lượt trễ quá một phút; so từng kịch bản, trần 120 giây phục vụ nhiều hơn ở 23, bằng ở 8 và ít hơn ở 3 kịch bản. | chênh C-120 − C-30: phục vụ +4 / +26 / +19; trễ60 +2 / +34 / +20; không trễ quá 60 s +2 / −8 / −1; kịch bản 9 / 14 / 11, yêu cầu 972 / 1.512 / 1.188 | ADD1:150-162; DER1:2-5; STG:61-72; CXS:119-127 | VERIFIED-by-me (script) | 34 kịch bản không độc lập (5 ngày). |
| N-12 | Bản luận văn hiện tại in một trang chỉ có tiêu đề "Tài liệu tham khảo" rồi trang sau mới bắt đầu bằng "Bibliography"; danh sách bảng bắt đầu ở trang xii; ở tập kịch bản tĩnh, 774 trong 1.581 khách được phục vụ (48,96%) bị độ đo điểm cuối chấm 0 dù thực tế bị dời. | TEX10:1 `\chapter*{Tài liệu tham khảo}`, TEX10:4 `\begin{thebibliography}`; PDF tr. 102: 2 dòng ("Tài liệu tham khảo", "86"); tr. 103 mở bằng "Bibliography"; Danh sách hình vẽ x, Danh sách bảng xii, Danh mục từ viết tắt xiii; 774 / 1.581 = 48,96%; 663 / 1.735 = 38,21% | ANC1:75-78,80,82-83; LOT1:2-4; TEX08:160,1728 | VERIFIED-by-me (read, pdftotext) | main.pdf có ngày tệp 30/9; nếu dựng lại thì kiểm lại số trang. Mẫu số 1.735 / 1.581 (TEX08:160) khớp với 38,2% / 49,0% ở TEX08:1728. |
| N-13 | Báo cáo DACN có hai bìa tiếng Việt (bìa 2 ghi cán bộ hướng dẫn), một bìa tiếng Anh, lời cảm ơn, Tóm tắt và Abstract ở sáu trang đầu. | tr. 1, 2 bìa Việt; tr. 3 bìa Anh; tr. 4 Lời cảm ơn; tr. 5 Tóm tắt; tr. 6 Abstract | ANC1:84-89 | VERIFIED-by-me (read, pdftotext) | Mẫu khung của khóa luận UET vẫn UNVERIFIED. |
| N-14 | Chủ sở hữu đã duyệt nghiên cứu theo giai đoạn, gồm cả Giai đoạn 1b. | R19C:3-4 "The owner approved both steps … Stage 1b cost-first 2×2 next" | ANC1:61-62 | VERIFIED-by-me (read) | Chỉ là lời ghi trong đề bài vòng 19 do Claude viết; tôi không thấy văn bản của chính chủ sở hữu. |
| N-15 | Trên 132 lần chạy có luật C đã được kiểm toàn bộ bản ghi chặn (98 lần chạy cũ và 34 lần chạy trần 120 giây), 3 trong 1.780 bản ghi chặn do trần chỉ do cộng dồn, cả ba ở trần 120 giây. | 98 = 34 + 64 lần chạy, 1.256 = 845 + 411 bản ghi, 0 chỉ do cộng dồn; + 34 lần chạy, 524 bản ghi, 3 → 132 / 1.780 / 3; kể cả 8 lần chạy chiều tuyết: 140 / 1.943 / 3 | ADD1:132-133; A:7,10-17; DER1:6; SNOW1:10 | VERIFIED-by-me (script) + **SCOPE** | Xem 0.3. C-30 đếm lại 845 = A:7. |
| N-16 | Bảng so khi có dự báo (gộp, trên 3.672 yêu cầu): không trần; trần 30 giây; trần 120 giây; không trần + đệm 30 giây; trần 30 giây + đệm 30 giây; không trần + đệm 60 giây. | phục vụ / trễ60 / không trễ quá 60 s / không trễ quá 120 s / sớm60 / kéo dài (s): U 2.434 / 137 / 2.297 / 2.347 / 8 / 7,18; C-30 2.338 / 10 / 2.328 / 2.338 / 4 / 7,37; C-120 2.387 / 65 / 2.322 / 2.379 / 2 / 7,27; U + 30 2.434 / 106 / 2.328 / 2.366 / 44 / 37,18; C-30 + 30 2.338 / 2 / 2.336 / 2.338 / 44 / 37,37; U + 60 2.434 / 87 / 2.347 / 2.386 / 1.033 / 67,18 | ADD1:14-16,19-20,24 | VERIFIED-by-me (script; U, C-30 khớp A; C-120 khớp CXS) | Dữ liệu cho Bảng 4.13. Dự báo chỉ hoạt động ở 21 / 34 kịch bản (ADD1:5-8); kịch bản cuối tuần giữ lời hứa ngây thơ. M⁺-30 + dự báo: 2.338 / 10 / 2.328 / 2.338 / 4 / 7,34 (ADD1:29). |
| N-17 | Khi cùng độ dài lời hứa, luật C trần 30 giây hơn ở ngưỡng một phút và kém ở ngưỡng hai phút: không đệm, 2.328 so với 2.297 và 2.338 so với 2.347; cùng đệm 30 giây, 2.336 so với 2.328 và 2.338 so với 2.366 lượt trên 3.672 yêu cầu. | kéo dài 7,37 vs 7,18 s (không đệm); 37,37 vs 37,18 s (đệm 30 s) | ADD1:93-94 | VERIFIED-by-me (script) | Phục vụ khác nhau 96 lượt; phát lại lời hứa. |
| N-18 | Cách đệm 30 giây trên điều phối không trần kéo dài lời hứa trung bình 37,18 giây, gấp 5,05 lần mức 7,37 giây của luật C có dự báo; trần 120 giây có dự báo kéo dài 7,27 giây, bằng 0,196 lần mức của cách đệm, và phục vụ ít hơn điều phối không trần 47 lượt. | 37,1833 / 7,3671 = 5,0472; 7,2739 / 37,1833 = 0,1956; 2.434 − 2.387 = 47 | ADD1:95,98 | VERIFIED-by-me (script) | "Khoảng năm lần", "khoảng một phần năm". |
| N-19 | Lợi thế 28 lượt của cách đệm 30 giây ở ngưỡng hai phút (2.366 so với 2.338) đi cùng 96 lượt phục vụ nhiều hơn, không phải ít khách trễ hơn: số khách trễ quá hai phút là 68 so với 0. | 2.366 − 2.338 = 28; 2.434 − 2.338 = 96; trễ120 68 vs 0 | ADD1:97 | VERIFIED-by-me (script) | — |
| N-20 | Luật C trần 30 giây có ít hơn 242 khách đi chung so với điều phối không trần (313 so với 555). | 555 − 313 = 242 `[đếm]` | ADD1:136-137,140 | VERIFIED-by-me (script) | Không có bằng chứng về giá trị của 242 khách này với khách hay hãng (REG D20, I07, I10). |
| N-21 | Theo nghĩa vụ của chính nó, luật hạn chót 30 giây có ít nhất một khách tới muộn hơn lời hứa đầu quá 30 giây ở 28 trong 34 kịch bản và bị ép ở 7.710 trong 20.103 quyết định; luật C trần 30 giây không phá trần ở kịch bản nào và không bị ép lần nào. | M⁺-30: phá hứa `[TB theo kịch bản]` 14,48%, `[gộp theo khách]` 289 / 2.338 = 12,36%; bị ép `[TB theo kịch bản]` 41,31%, gộp 7.710 / 20.103 = 38,35%; khung 7 giờ 9 / 9 kịch bản, 36,53%, ép 75,62% (gộp 3.447 / 4.564 = 75,53%); khung 8 giờ 14 / 14, 10,87%, 47,79%; khung 17 giờ 5 / 11, 1,04%, 4,99%; C-30: 0 / 34 kịch bản, 0 quyết định bị ép | ADD1:8,189-193; T38A:76-77,83 | VERIFIED-by-me (script; khớp T38A) | Phá hứa của M⁺-30 = khách được phục vụ có A − p₀ > 30 s (định nghĩa của `sweep_analyze` mà T38A dùng); C-30 = khách có Σ\|c\| > 30 s. Số gộp 38,35% là số LR-24 cần, trước đây chưa có. 299 khách có bản ghi forcedReference (ADD1:8) là một đếm khác. Luật hạn chót ở đây chỉ là phần hạn chót, ở 30 s thay vì 900 s (REG J10, J11). |
| N-22 | So từng kịch bản, luật C trần 30 giây không có nhiều khách trễ quá một phút hơn điều phối không trần ở cả 34 kịch bản và có ít nhất bằng số lượt không trễ quá một phút ở 29 trong 34 kịch bản; ở khung 8 và 17 giờ, điều phối không trần nhiều khách trễ hơn ở cả 25 kịch bản, ở khung 7 giờ nhiều hơn ở 3 và bằng ở 6. | tổng C − U: trễ60 −127, không trễ quá 60 s +31; bảng theo ngày × khung ở dưới | ADD1:167-186 | VERIFIED-by-me (script) | Dữ liệu cho Bảng 4.7 (lời hứa ngây thơ); khớp REG C30. Tập khách khác nhau; 34 kịch bản thuộc 5 ngày. |
| N-23 | Khi không trần, 174 khách bị điều phối dời giờ trả, 12 khách từ hai lần, tổng lớn nhất 590,1 giây, trung vị mỗi lần dời 108,6 giây; với trần 30 giây là 33 khách, 0, 29,2 giây và 8,3 giây; trong số khách trễ quá một phút, số khách từng bị dời là 134 / 203 và 4 / 76, và phần tính cho điều phối là 73,4% và 1,2% số giây trễ của họ. | U: 174 (7,15%); 187 lần dời; S lớn nhất 590,133 s; C-30: 33 (1,41%); 33 lần; 29,239 s; C-120: 103; 0; 118,938 s; trung vị 62,5 s; trễ60 ∧ bị dời 60 / 132; phần điều phối 38,8% | ADD1:104-108; A:7,9; CON:5-6,12-13 | VERIFIED-by-me (script) | Dữ liệu cho Bảng 4.8. Giao của hai tập, không phải tỉ lệ nhân quả (REG C21). Cột C-120 là mới, không có trong outline. |
| N-24 | Tính trên 100 yêu cầu, số lượt trễ quá 1 / 2 / 5 / 10 phút so với lời hứa đầu là 5,53 / 2,78 / 0,49 / 0,05 khi không trần và 2,07 / 0,30 / 0 / 0 với trần 30 giây. | trễ60 / 120 / 300 / 600: 203 / 102 / 18 / 2 và 76 / 11 / 0 / 0 trên 3.672; C-30 có dự báo 0,27 trễ60 / 100 yêu cầu | ADD1:12,17,101 | VERIFIED-by-me (script) | Khớp REG C28; dữ liệu cho Bảng 4.6. |
| N-25 | Ở cả bốn cấu hình, bộ sinh không áp giới hạn số phương án (0 lần), không bỏ phương án vì giới hạn (0), không hết ngân sách tính toán (0) và bỏ đúng 1 yêu cầu; mức dùng trần lớn nhất luôn bão hòa ở 1.000.000 ppm. | U / C-30 / C-120 / M⁺-30: bỏ yêu cầu 1 / 1 / 1 / 1; bão hòa 3.503 / 3.503, 3.506 / 3.506, 3.504 / 3.504, 3.506 / 3.506 quyết định có mức này | ADD1:119-122; A:7-9 | VERIFIED-by-me (script; U, C-30, M⁺-30 khớp A) | Cột C-120 là mới (bổ sung REG A15, A24). Bộ sinh có giới hạn, không vét cạn. |
| N-26 | Trên 8 kịch bản chiều tuyết 15/11/2018 (601 khách), luật C trần 30 giây có 8 khách bị điều phối dời, tổng dời lớn nhất của một khách là 25,2 giây, 0 khách vượt trần, 0 quyết định bị ép; 163 bản ghi chặn đều do một lần dời vượt trần. | 601 / 601 phục vụ; bị dời 8; ≥ 2 lần 0; lớn nhất 25,187 s; vượt 0; ép 0 / 5.067; bản ghi 163, chỉ do cộng dồn 0 | SNOW1:2-10 | VERIFIED-by-me (script) | Thay anchor F13 cho RD §8 mục 4 (xem 0.4). |
| N-27 | Hai trong ba bản ghi chỉ do cộng dồn dưới trần 120 giây có khách bị chạm trần là khách mà, khi không trần, bị điều phối dời hai lần đúng bằng hai lượng đó: 25,844 + 99,027 = 124,871 giây và 105,508 + 99,301 = 204,809 giây. | kịch bản d20181114-s10-r3-w08, rq-7cfd633530…: U [25.844, 99.027] ms; C-120 trước 25.844 + bước 99.027 = 124.871 > 120.000; d20181118-s10-r3-w08, rq-7f2c511678…: U [105.508, 99.301]; C-120 105.508 + 99.301 = 204.809 | ADD1:115-116,128,130; CW21:2,6 | VERIFIED-by-me (script) | Khớp 13 ký tự đầu của mã yêu cầu trong cùng kịch bản. Ví dụ U này là ví dụ của REG E07. Mô tả bản ghi, không phải quan hệ nhân quả. |
| N-28 | Ở 13 kịch bản cuối tuần, nơi không có dự báo, tổng dời do điều phối lớn nhất của một khách là 29,2 giây với trần 30 giây và 116,5 giây với trần 120 giây. | C-30 29,239 s; C-120 116,542 s; 13 kịch bản cuối tuần = 13 kịch bản không có dự báo | ADD1:113-114 | VERIFIED-by-me (script) | Trần giữ không cần dự báo đúng. |
| N-29 | Nếu đệm thêm 30 giây cho trần 120 giây có dự báo, có 2.360 lượt không trễ quá một phút và 2.385 lượt không trễ quá hai phút trên 3.672 yêu cầu, 44 khách tới sớm quá một phút, lời hứa dài thêm 37,27 giây. | C-120 + dự báo + 30 s: trễ60 27; trễ120 2; sớm60 44; kéo dài 37,274 s | ADD1:25 | VERIFIED-by-me (script) | Điểm mới, không có trong outline; phát lại lời hứa, chỉ thêm nếu cần. |
| N-30 | Ở kịch bản phát triển d20181113-s10-r1-w07, với trần lỏng 300 giây, khách trễ nhất trễ 307,3 giây gồm 99,1 giây phần thay đổi khi giữ kế hoạch và 208,2 giây phần do điều phối; dưới trần 30 giây, khách trễ nhất trễ 99,1 giây, trong đó 97,1 giây là phần thay đổi khi giữ kế hoạch. | 307,3 = 99,1 + 208,2 s; 99,1 s (97,1 s) | W07:49,53; ANC1:68-69 | VERIFIED-by-me (read) | Bổ sung REG D06 (D06 thiếu vế trần 30 giây). Không chạy lại. Mô tả sau khi xem. |

**Dữ liệu cho Bảng 4.7** (N-22; luật C trần 30 giây trừ điều phối không trần, lời hứa ngây thơ, cộng trên các kịch bản
của nhóm; ADD1:173-186).

| Ngày | Khung | Kịch bản | Trễ60 U / C / C−U | Không trễ quá 60 s U / C / C−U | Phục vụ U / C / C−U | Kịch bản C trễ ≤ U | Kịch bản C không trễ ≥ U |
|---|---|---:|---|---|---|---:|---:|
| 14/11 | 7 h | 2 | 14 / 14 / 0 | 86 / 86 / 0 | 100 / 100 / 0 | 2/2 | 2/2 |
| 14/11 | 8 h | 2 | 9 / 2 / −7 | 155 / 158 / +3 | 164 / 160 / −4 | 2/2 | 2/2 |
| 14/11 | 17 h | 2 | 7 / 0 / −7 | 180 / 179 / −1 | 187 / 179 / −8 | 2/2 | 1/2 |
| 15/11 | 7 h | 3 | 34 / 32 / −2 | 111 / 115 / +4 | 145 / 147 / +2 | 3/3 | 3/3 |
| 15/11 | 8 h | 3 | 13 / 3 / −10 | 224 / 226 / +2 | 237 / 229 / −8 | 3/3 | 3/3 |
| 16/11 | 7 h | 3 | 15 / 14 / −1 | 185 / 183 / −2 | 200 / 197 / −3 | 3/3 | 2/3 |
| 16/11 | 8 h | 3 | 16 / 3 / −13 | 213 / 217 / +4 | 229 / 220 / −9 | 3/3 | 3/3 |
| 16/11 | 17 h | 3 | 21 / 0 / −21 | 229 / 239 / +10 | 250 / 239 / −11 | 3/3 | 2/3 |
| 17/11 | 7 h | 1 | 7 / 1 / −6 | 64 / 66 / +2 | 71 / 67 / −4 | 1/1 | 1/1 |
| 17/11 | 8 h | 3 | 11 / 4 / −7 | 179 / 184 / +5 | 190 / 188 / −2 | 3/3 | 3/3 |
| 17/11 | 17 h | 3 | 18 / 0 / −18 | 210 / 209 / −1 | 228 / 209 / −19 | 3/3 | 2/3 |
| 18/11 | 8 h | 3 | 18 / 3 / −15 | 176 / 175 / −1 | 194 / 178 / −16 | 3/3 | 2/3 |
| 18/11 | 17 h | 3 | 20 / 0 / −20 | 219 / 225 / +6 | 239 / 225 / −14 | 3/3 | 3/3 |
| **Tổng** | | **34** | **−127** | **+31** | **−96** | **34/34** | **29/34** |

(Cột "Phục vụ" tổng −96 là 2.338 − 2.434, ADD1:12,17; các cột khác ADD1:186.)

---

## L. Kết quả Giai đoạn 1a (trần 120 giây, 34 kịch bản chính) — lấp chỗ L01

Mỗi dòng có anchor tới C120-RESULTS.md (C120R), hai phân tích độc lập (STG của Claude, CXS/CXJ của Codex v4) và lần đọc
lại của tôi (ADD1). Không ghi kế hoạch, dự đoán hay P1–P5 (C120R:28-29) theo yêu cầu chủ sở hữu.

| ID | Câu có thể dùng trong luận văn | Số chính xác | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| L1a-01 | Luật C với trần 120 giây đã được chạy trên 34 kịch bản chính, mỗi kịch bản một lần, cả 34 lần chạy hoàn tất hợp lệ. | 34 / 34 `status: pass`, repeatCount 1, run-00 succeeded; 2026-10-10 22:12–23:48; 3.672 yêu cầu; 2.387 hoàn tất, 1.285 bị từ chối | C120R:10; STG:6; ADD1:7 | VERIFIED-by-me (script + read) | Lấp L01 và thay D12 ("chưa chạy"). |
| L1a-02 | Với lời hứa đầu không dự báo, trần 120 giây phục vụ 2.387 lượt, có 132 / 21 / 0 lượt trễ quá 60 / 120 / 300 giây và 1 lượt tới sớm quá 60 giây; 2.255 và 2.366 lượt không trễ quá một và hai phút trên 3.672 yêu cầu. | trễ60 5,53% `[gộp theo khách]`; 61,41% / 64,43% `[trên yêu cầu]` | C120R:14; STG:29; CXS:76; ADD1:22 | VERIFIED-by-me (script; 3 bộ đọc) | 2.366 nhiều hơn U (2.332) và C-30 (2.327) (ADD1:197); không trần không phải cận trên (REG K12). |
| L1a-03 | Với lời hứa theo dự báo, trần 120 giây có 65 / 8 / 0 lượt trễ quá 60 / 120 / 300 giây, 2 lượt tới sớm quá 60 giây, 2.322 và 2.379 lượt không trễ quá một và hai phút, lời hứa dài thêm trung bình 7,27 giây. | 2,72% `[gộp theo khách]`; 63,24% / 64,79% `[trên yêu cầu]`; 7,274 s | C120R:15; STG:34; CXS:79; ADD1:24 | VERIFIED-by-me (script; 3 bộ đọc) | Dự báo hoạt động ở 21 / 34 kịch bản. |
| L1a-04 | Các số gốc của điều phối không trần và trần 30 giây được tái lập đúng từ các lần chạy đã lưu trước khi so với trần 120 giây. | U 2.434 / 203 / 102 / 18, 2.231 / 2.332, dự báo 137 / 87 / 17, 2.297 / 2.347, 7,18 s; C-30 2.338 / 76 / 11 / 0, 2.262 / 2.327, dự báo 10 / 0 / 0, 2.328 / 2.338, 7,37 s | C120R:16-19; STG:9-23; ADD1:12,14,17,19,34-64 | VERIFIED-by-me (script; khớp A) | Tái lập trên cùng transcript, không phải chạy lại mô phỏng. |
| L1a-05 | Dưới trần 120 giây, 103 khách (4,32%) bị điều phối dời giờ trả, không ai từ hai lần; tổng dời của khách bị dời trung bình 55,5 giây, trung vị 62,5 giây, p90 104,9 giây, lớn nhất 118,9 giây; 0 khách vượt trần và 0 quyết định bị ép. | 103 / 2.387; 0; 55,50 / 62,54 / 104,87 / 118,938 s; vượt 0; ép 0 / 20.435 | C120R:21-22; STG:39,44; CXS:89; ADD1:108,121 | VERIFIED-by-me (script; 3 bộ đọc) | = N-07. |
| L1a-06 | Trên 34 lần chạy trần 120 giây có 524 bản ghi chặn do trần: 521 do một lần dời vượt trần và 3 chỉ do cộng dồn, ở 3 kịch bản khung 8 giờ (14, 15 và 18/11); 2 trong 3 yêu cầu mới liên quan cuối cùng không được nhận. | 524 = 521 + 3; d20181114-s10-r3-w08, d20181115-s10-r1-w08, d20181118-s10-r3-w08 | C120R:22-24; STG:44-47; CW21:2-7; CXS:91,95-101; ADD1:127-130 | VERIFIED-by-me (script; 3 bộ đọc) | = N-08; bản ghi dừng ở lỗi đầu, không phải tác dụng lên kết quả. |
| L1a-07 | Trần 120 giây có 428 khách đi chung trong 2.387 khách được phục vụ (17,93%), so với 313 (13,39%) ở trần 30 giây và 555 (22,80%) khi không trần. | `[gộp theo khách]` | C120R:24-25; STG:50-52; ADD1:136-138 | VERIFIED-by-me (script; cùng quy tắc với STG) | = N-09. |
| L1a-08 | Tập khách được phục vụ dưới trần 120 giây không chứa tập của trần 30 giây: chung 2.266, riêng 121 và 72; so với không trần chung 2.271, riêng 116 và 163. | 2.266 / 121 / 72; 2.271 / 116 / 163 | C120R:25-26; STG:55-56; CXS:109-111; ADD1:143-144 | VERIFIED-by-me (script; 3 bộ đọc) | = N-10. |
| L1a-09 | So với trần 30 giây, trần 120 giây phục vụ thêm 4 / 26 / 19 lượt ở khung 7 / 8 / 17 giờ; tổng cộng thêm 49 lượt phục vụ, thêm 56 lượt trễ quá một phút, ít hơn 7 lượt không trễ quá một phút và thêm 39 lượt không trễ quá hai phút; khi có dự báo, ít hơn 6 và thêm 41 lượt. | +4 / +26 / +19; +49; +56; −7; +39; dự báo −6 / +41 | C120R:26; STG:61-69; CXS:119-127; ADD1:196; DER1:2-4 | VERIFIED-by-me (script) | = N-11 và OUTLINE §7.1. Tập khách khác nhau (L1a-08). |

---

## Dòng của sổ chính cần cập nhật (tôi KHÔNG sửa sổ chính)

- **L01** → lấp bởi N-06…N-11 / L1a-01…L1a-09. **D12** → trần 120 giây đã chạy trên 34 kịch bản (L1a-01).
- **E01 / I17 / K08** → "0 bản ghi chỉ do cộng dồn" chỉ đúng cho 98 lần chạy cũ; Giai đoạn 1a thêm 3 (N-08); phạm vi theo
  0.3 (chiều tuyết 0 / 163; 15 lần chạy hiệu chỉnh và các lần chạy C-30F chưa kiểm).
- **C25** → số đếm chính xác N-09. **C23** → 4 lần dời sớm hơn của C-30 mỗi lần đúng 1 ms (N-05).
- **A15 / A24** → thêm C-120: bão hòa 3.504 / 3.504, bỏ 1 yêu cầu (N-25). **C13** → thêm số gộp bị ép 7.710 / 20.103 =
  38,35% (N-21). **E07** → ví dụ U là cùng khách với bản ghi cộng dồn thứ nhất của C-120 (N-27). **D06** → thêm vế trần
  30 giây (N-30). Anchor của RD §8 mục 4 → SNOW1 thay F13 (N-26).

## Tổng hợp

| Mục | Số dòng | VERIFIED-by-me (script) | VERIFIED-by-me (read) | CORRECTED / SCOPE | UNVERIFIED |
|---|---:|---:|---:|---:|---:|
| N (N-01…N-30) | 30 | 26 | 4 (N-12, N-13, N-14, N-30) | N-05 (CORRECTED, số đếm vẫn VERIFIED), N-15 (SCOPE) | 0 |
| L (L1a-01…L1a-09) | 9 | 9 | — | 0 | 0 |
| **Tổng** | **39** | **35** | **4** | **2 (gắn trên dòng đã tính)** | **0** |

Mục 0 có 4 phát hiện: 0.1 sửa một số (≈ 0,56 s → 0,004 s), 0.2 sửa cách diễn giải, 0.3 sửa phạm vi câu, 0.4 sửa anchor.

*Hết phụ lục 1. Viết bởi Claude (evidence registrar), 2026-10-11. Chỉ tệp này và thư mục `checks-addendum-1/` được tạo.*
