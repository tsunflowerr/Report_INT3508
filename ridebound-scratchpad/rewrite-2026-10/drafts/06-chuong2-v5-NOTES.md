# 06-chuong2 v5/v6 — NOTES của người sửa (2026-10-13)

**Bản dùng để ghép: `drafts/06-chuong2-v6.tex`** (`\input` được trong `main.tex`; không cần gói mới, `aligned` có sẵn
trong `amsmath`). Tên tệp này theo yêu cầu đầu ra (`-v5-NOTES`), nhưng **nội dung mô tả v6**.

| Tệp | Nội dung |
|---|---|
| `06-chuong2-v4.tex` | Bản được nhận xét (Codex R35, Claude R30). Giữ nguyên. |
| `06-chuong2-v5.tex` | Lượt sửa đủ mọi nhận xét; 3.396 tiếng (+5,8% so với v4), vượt hạn 5%. Không dùng. |
| `06-chuong2-v6.tex` | v5 rút năm câu, không đổi sự kiện nào (diff ở `reviews/CH2-REVISION-LOG.md`, đầu tệp). 3.358 tiếng (+4,6%). **Bản ghép.** |

Lý do từng thay đổi: `reviews/CH2-REVISION-LOG.md` (166 hàng: 156 mục Codex, 10 mục B/N của R30; 11 chỗ bất đồng D1–D11
được giải bằng nguồn). Không ghi vào thư mục luận văn, `E:/Code/RideBound*` hay `C:/Code/*`; không build, không mô phỏng,
không cài, không xóa. Kiểm cú pháp bằng `texcheck.py` (thư mục phiên): ngoặc cân, mọi môi trường đóng, số `$` chẵn, 9
nhãn không trùng. **Chưa biên dịch thử.**

---

## 1. Độ dài theo mục

Bộ đếm `wc_ch3_v2.py` (cùng bộ đếm của v4): "tiếng" = token cách nhau bởi khoảng trắng có chữ hay số; bỏ dòng `%`, lệnh
LaTeX, công thức; chữ trong bảng đếm riêng.

| Mục | Ngân sách (OUTLINE-V2) | v4 văn xuôi | v6 văn xuôi | v4 bảng | v6 bảng |
|---|---:|---:|---:|---:|---:|
| Mở chương | 0,25 | 101 | 106 | — | — |
| 2.1 Bài toán ghép chuyến động | 2 | 642 | 623 | 215 (Bảng 2.1) | 225 |
| 2.2 Đo lường và kiểm soát độ bất ổn | 1,25 | 598 | 590 | — | — |
| 2.3 Các dạng ràng buộc lời hứa | 1,5 | 510 | 632 | 419 (Bảng 2.2, 8 hàng) | 384 (7 hàng) |
| 2.4 Dự báo thời gian đi | 1 | 448 | 485 | — | — |
| 2.5 Độ tin cậy có giá trị gì | 0,5 | 276 | 313 | — | — |
| **Tổng** | **6,5** | **2.575** | **2.749** | **634** | **609** |

Tổng v4 3.209 → v6 3.358, **+4,6%** (văn xuôi +6,8%, bảng −3,9%). Bản dựng thử 13/10 đo v4 là 7 trang (trang 10–16
của `main.xdv`). Ước lượng v6 theo tỉ lệ chữ: ≈ 7,3 trang; công thức (2.1) nay chiếm ba dòng thay cho một (thêm ≈ 2
dòng), Bảng 2.2 bớt một hàng (bớt ≈ 3 dòng). Mục 2.3 dài hơn ngân sách vì có đoạn Hörl–Zwick viết lại và ví dụ dựng
tay; mục 2.1, 2.2 ngắn lại để bù.

**Chỗ cắt nếu bản dựng thật vượt 7 trang** (theo thứ tự, không mất sự kiện nào mà nhận xét đòi):
1. Mục 2.5: bỏ vế cách đo độ tin cậy của Alonso-González ("đo độ tin cậy qua độ dao động … giờ được báo"). ≈ 25 tiếng.
2. Mục 2.4: bỏ vế phân vị của DeeprETA. ≈ 20 tiếng.
3. Mục 2.3: rút ví dụ dựng tay còn vế ngược lại (8:36:00), vì vế thuận đã nói bằng câu "chỉ được nới khi…". ≈ 50 tiếng.
4. Mục 2.1: bỏ câu "Hörl và Zwick và bộ mô phỏng FleetPy đều dùng thuật toán này" (Chương 3 không trỏ tới câu này). ≈ 15 tiếng.

## 2. Nhãn

**Chương này định nghĩa (9), như v4:** `chuong:coso`; `muc:c2-baitoan`, `muc:c2-dolech`, `muc:c2-rangbuoc`,
`muc:c2-dubao`, `muc:c2-giatri`; `eq:c2-chon`; `bang:c2-dichvu` (Bảng 2.1), `bang:c2-dangrangbuoc` (Bảng 2.2).

**Chương này cần (8), đều có:** `chuong:phuongphap`, `muc:baitoan-phatbieu`, `muc:bamoc`, `muc:luatc`, `muc:doichung`,
`muc:dubao` (Chương 3, `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex`); `chuong:thucnghiem`, `muc:c4-kichban` (Chương 4
phần A v4). `muc:c2-rangbuoc` không còn được trỏ trong Chương 2 nhưng Chương 3 dòng 460 trỏ tới.

**Bốn nhãn Chương 3 trỏ tới, nội dung vẫn khớp:** `muc:c2-baitoan` (bước chọn theo lối Alonso-Mora, r33:118);
`muc:c2-rangbuoc` (Hörl–Zwick; r33:460–468 nói công thức 7, ràng buộc 9–10, phạt 11, "phần nới của họ chỉ tác dụng khi
giờ cập nhật đã vượt giờ trả muộn nhất", đúng như v6 dòng 157–171); `muc:c2-dolech` (r33:471); `muc:c2-dubao`
(r33:497, lời hứa theo dự báo là cách làm đã có).

**Dòng `% EV`:** v6 có 32 dòng bắt đầu bằng `% EV` (một dòng cho mỗi đoạn có sự kiện, một dòng cho mỗi nhóm hàng
bảng), cộng một dòng ở khối chú thích đầu tệp có chứa chuỗi này. (Ghi chú v4 nói 33; Codex E05 đếm lại là 31.)

## 3. Tài liệu tham khảo

**Tập `\cite` không đổi so với v4: 15 khóa**, đều đã có siêu dữ liệu kiểm ở `06-chuong2-BIB.md` (Codex M01–M15 xác nhận
độc lập): `alonsogonzalez2020`, `alonsomora2017`, `elmi2026`, `engelhardt2026`, `fielbaum2020`, `horl2022`, `hu2022`,
`laupichler2026`, `leonardi2024`, `lu2024`, `molenbruch2017`, `schulz2026`, `tlc`, `wardman2026`, `yu2022`.
**Khóa mới: không. Khóa bỏ: không.** Chín khóa mới cần thêm khi ghép vẫn như BIB mục 1 (`engelhardt2026`, `horl2022`,
`hu2022`, `laupichler2026`, `leonardi2024`, `lu2024`, `molenbruch2017`, `wardman2026`, `yu2022`).

**Chỉnh sửa / ghi thêm:**
- `alonsogonzalez2020`: mục trong `10-tai-lieu.tex` cũ sai tác giả; dùng danh sách M. J. Alonso-González, N. van Oort,
  O. Cats, S. Hoogendoorn-Lanser, S. Hoogendoorn (BIB mục 1; Codex M02; AGZ PDF tr. 1). Sửa khi ghép.
- `hu2022` (DeeprETA): bản arXiv 2206.02127v1 có **9 trang**, không phải 3 như phụ lục 5 (C2-15) ghi. Tôi kiểm bằng
  `pdftotext`: trang 9 có chữ (hình 10), trang 10 rỗng. Vị trí trích (tr. 1, 3) không đổi. Phụ lục 5 là đầu vào chỉ đọc
  nên không sửa ở đó.
- `leonardi2024`, `lu2024`: theo Codex M09, M10 có bản tạp chí muộn hơn (Leonardi và cộng sự, Transportmetrica A, 2026,
  doi 10.1080/23249935.2026.2650136, tên có đổi; Lu và Kühnel, Case Studies on Transport Policy 21 (2025) 101499, doi
  10.1016/j.cstp.2025.101499). **Tôi chưa mở hai bản này**, nên vẫn trích bản đã đọc (STYLE quy tắc 35 ưu tiên bản đã
  công bố: câu hỏi mở 2).
- `tlc`: ngày truy cập 12/10/2026 ở mục tài liệu; thân bài không ghi ngày (RL N2, xem nhật ký D9).
- `yu2022`: thân bài nay viết "Theo phần tóm tắt, …"; chú thích chân trang của v4 được bỏ vì trùng ý.

## 4. Sửa lỗi dàn trang của bản dựng thử 13/10

- **Công thức `eq:c2-chon` (tràn 80,5 pt):** tách thành ba dòng bằng `aligned` (dòng mục tiêu; "thỏa" + ràng buộc xe;
  ràng buộc yêu cầu), nghĩa không đổi; một số hiệu (2.1) cho cả khối.
- **Bảng 2.1 (tràn 1,9 pt):** cột 3 hẹp từ 5,9 xuống 5,7 cm. Bề rộng chữ của mẫu là 21 − 3 − 2 = 16 cm (`main.tex` dòng
  28); bảng nay 14,6 cm cột + 3 × 12 pt khoảng cách ≈ 15,87 cm. Trước là ≈ 16,07 cm, khớp mức tràn 1,9 pt đo được.
- **Bảng 2.2:** tổng cột vẫn 14,9 cm với `\tabcolsep` 3 pt (≈ 15,96 cm), như v4, vốn không tràn ở bản dựng thử.

## 5. Chỗ lệch so với OUTLINE-V2 và v4, kèm lý do

1. **Bảng 2.2 bỏ hàng "Cửa sổ đón; giới hạn ngồi xe".** Outline liệt kê hai hàng này; chúng đã có ở Bảng 2.1. Thay bằng
   một câu trong chú thích Bảng 2.2 ("không tách nguồn, nên phần do tắc đường bị tính"). Lý do: ngân sách trang, và
   Codex T202/T205 cho thấy ô "Có" của hai hàng này cần giải thích dài.
2. **Cột cuối Bảng 2.2 là "Dữ liệu giữ riêng cho từng khách"**, không phải "Ghi theo từng khách?" của outline: cột 5
   ("Cộng độ lớn các lần dời qua cả chuyến?") đã trả lời câu về sổ cộng dồn; cột 6 cho thấy mỗi bài trước cũng giữ dữ
   liệu riêng cho từng khách (hạn chót, độ chùng, giờ cập nhật), để không ô nào phủ nhận điều đó (nhật ký D4).
3. **Hàng "Giữ giờ đón đã báo" thêm `fielbaum2020`**: mức kiểm soát hoàn toàn của họ hạ thời gian chờ tối đa về giá trị
   dự kiến (FAM tr. 17), cùng dạng với Alonso-Mora (R30 mục C.8).
4. **Lu–Kühnel và Mt-KaRRi** chỉ còn một vế liệt kê trong văn xuôi; con số và mốc ở Bảng 2.2 (cách cắt 1 của NOTES v4).
5. **Ví dụ dựng tay so công thức 7 với luật C** (R30 N1) ở mục 2.3, có cả vế ngược lại (công thức 7 chặt hơn khi giờ cập
   nhật đã vượt hạn). Ví dụ dùng giờ 8:30, khác ví dụ 9:10 của Chương 3.
6. **Câu "1 mili giây" rời Chương 2**; Chương 3 v4 (r33 dòng 297–300) đã nêu đúng phạm vi (nhật ký D5).
7. **Kết luận của Hörl–Zwick** chuyển từ mục 2.3 sang câu mở mục 2.4, kèm điều kiện "với tốc độ thực đổi theo giờ".
8. **Đoạn mở** có định nghĩa một câu của luật C (R30 mục 3), lấy theo Chương 3 dòng 18–25.

## 6. Câu hỏi mở cho chủ nghiên cứu

1. **Tỉ lệ lấy từ bài khác không kèm số đếm.** Quy tắc "mọi tỉ lệ kèm số đếm và mẫu số" được viết cho kết quả của khóa
   luận; các bài không công bố số đếm. v6 giữ các tỉ lệ mang lập luận, ghi nguồn và cách gộp: Fielbaum–Alonso-Mora
   "hơn một phần ba" (tóm tắt), 34,5% / 45,6% / 31,2% ("theo bảng 5 của bài"); Elmi 29,1% / 29,2% / 83,9% ("trung bình
   trên 10 ngày"). Không gắn mẫu số 19.610 vào bảng 5 vì bài ghi tỉ lệ phục vụ cơ sở 66,5% (tr. 9), không khớp 100% −
   34,5%, nên chưa chắc cùng lần chạy. Codex đề nghị thay bằng mô tả định tính (C4, C8). Chủ nghiên cứu chọn: giữ như v6
   hay thay định tính?
2. Trích bản tạp chí của Lu–Kühnel (2025) và Leonardi và cộng sự (2026) thay cho bản tiền ấn? Cần mở hai bản đó trước.
3. Đồng ý bỏ hai hàng đầu của Bảng 2.2 (mục 5, ý 1)?
4. Schulz và Pfeiffer gọi l là "maximum time shift"; v4, v6 và Chương 3 (r33 dòng 443) đều gọi là "độ chùng", trùng tên
   với độ chùng (slack) của Elmi. Giữ cho thống nhất với Chương 3, hay đổi cả hai chương thành "khoảng dời tối đa"?
5. Yu và cộng sự vẫn chỉ đọc tóm tắt; đọc toàn văn hay giữ câu "Theo phần tóm tắt"?
6. Lấy lại câu Kovacs/Sridharan (bỏ từ v3)? v6 không có chỗ.

## 7. Câu là suy luận của người viết (ghi rõ trong câu và trong dòng `% EV`)

1. Mục 2.3, ví dụ dựng tay (áp đúng công thức 7, 10 của Hörl–Zwick và định nghĩa luật C).
2. Bảng 2.2, cột 3 cho các hàng nghiên cứu trước và câu chú thích về Bảng 2.1: cách khóa luận đọc định nghĩa ràng
   buộc; chú thích Bảng 2.2 nói rõ điều này.
3. Mục 2.4: "thời gian đi trong mô phỏng có thể dễ dự báo hơn ngoài đời", "có thể lạc quan hơn khi áp dụng thật" (dựa
   vào I02, F10; viết bằng "có thể").
4. Mục 2.4: dữ liệu kịp thời của hãng xe là **giả định** của khóa luận, chưa kiểm (nói trong câu).
5. Mục 2.2: ví dụ khách bị dời 5 phút rồi kéo về (dựng tay từ định nghĩa của Fielbaum–Alonso-Mora).

Câu suy luận của v4 "một khách có thể bị dời giờ trả nhiều lần, miễn là mỗi lần tổng chi phí nhỏ hơn" đã bỏ (Codex F18);
câu thay "ngoài độ trễ tối đa, bài không đặt trần riêng lên tổng độ lớn các lần dời" là đọc trực tiếp công thức (1) và
giải thuật 1 của Alonso-Mora.

## 8. Bằng chứng còn thiếu (nên không viết)

- Tên hội nghị của Hörl–Zwick (DataCite không ghi).
- Cách tính tệp hệ số 15 phút của FleetPy (bài chỉ mô tả hệ số theo giờ).
- Toàn văn Yu và cộng sự; bản tạp chí của Leonardi và cộng sự, Lu và Kühnel.
- Số đếm đứng sau các tỉ lệ của Fielbaum–Alonso-Mora và Elmi (mục 6, ý 1).
- Đã giải, chưa dùng: 47,8% của Elmi là **điểm phần trăm** (63,17% → 15,39%, "absolute reduction", tr. 18).
