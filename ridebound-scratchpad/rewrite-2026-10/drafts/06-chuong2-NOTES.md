# 06-chuong2 — NOTES của người viết (2026-10-12)

**Bản dùng để ghép: `drafts/06-chuong2-v4.tex`** (`\input` được trong `main.tex`; không cần gói mới). Các bản trước giữ
nguyên, không ghi đè:

| Tệp | Nội dung |
|---|---|
| `06-chuong2.tex` (v1) | Bản đầy đủ đầu tiên, 2.901 tiếng văn xuôi. |
| `06-chuong2-v2.tex` | Sửa sáu chỗ diễn đạt so với bài gốc (mục 3.1 dưới đây), cắt nhẹ. |
| `06-chuong2-v3.tex` | Rút văn xuôi xuống 2.549 tiếng cho vừa 6,5 trang (mục 1); bỏ đoạn Kovacs/Sridharan. |
| `06-chuong2-v4.tex` | Gọi Hörl–Zwick bằng "công thức 7/8" thay cho "chiến lược B/C" (OUTLINE-V2 quy tắc 6); thêm "lời hứa giờ trả (promised drop-off time)" ở đoạn mở; dùng câu chữ của outline "quay về hạn chót…"; nêu tên tác giả Mt-KaRRi. |

`06-chuong2-BIB.md` và `evidence/EVIDENCE-REGISTER-ADDENDUM-5-CH2.md` được viết khi v3 là bản mới nhất. v4 có **cùng
tập `\cite` và cùng 33 dòng `% EV`** với v3 (đã kiểm bằng `diff`), nên hai tệp đó áp dụng nguyên cho v4.

Không ghi vào thư mục luận văn, `E:/Code/RideBound*` hay `C:/Code/*`; không build, không cài, không xóa. Kiểm cú pháp
bằng `texcheck.py` (thư mục phiên): ngoặc cân, mọi môi trường đóng, số `$` chẵn, 9 nhãn không trùng. **Chưa biên dịch
thử**; người ghép cần chạy `tectonic` một lần và xem `main.log` (độ rộng hai bảng; bảng 2.2 dùng `\footnotesize`,
`\tabcolsep` 3pt, tổng cột 14,9 cm như Bảng 3.5 của Chương 3).

---

## 1. Độ dài theo mục so với ngân sách

Bộ đếm `wc_ch3_v2.py` (cùng bộ đếm của Chương 3): "tiếng" = token cách nhau bởi khoảng trắng có chữ hay số, bỏ dòng
`%`, lệnh LaTeX, công thức; chữ trong bảng đếm riêng.

| Mục | Ngân sách (OUTLINE-V2) | Văn xuôi v4 (tiếng) | Bảng / công thức v4 | Ước lượng trang v4 |
|---|---:|---:|---|---:|
| Mở chương | 0,25 | 101 | — | ≈ 0,3 (gồm tiêu đề chương) |
| 2.1 Bài toán ghép chuyến động | 2 | 642 | Bảng 2.1 (215 tiếng, 3 hàng); công thức (2.1) | ≈ 1,7–1,95 |
| 2.2 Đo lường và kiểm soát độ bất ổn | 1,25 | 598 | — | ≈ 1,1–1,25 |
| 2.3 Các dạng ràng buộc lời hứa | 1,5 | 510 | Bảng 2.2 (419 tiếng, 8 hàng) | ≈ 1,7–1,85 |
| 2.4 Dự báo thời gian đi | 1 | 448 | — | ≈ 0,8–0,95 |
| 2.5 Độ tin cậy có giá trị gì | 0,5 | 276 | chú thích chân trang 1 dòng | ≈ 0,5–0,6 |
| **Tổng** | **6,5** | **2.575** | **634** | **≈ 6,2–6,9** |

**Cách ước lượng (đã đo, chưa dựng).** Chương 2 cũ (`ridebound/noi-dung/06-chuong2.tex`) có 2.763 tiếng văn xuôi theo
cùng bộ đếm, 3 công thức trưng bày và một bảng nhỏ; nó chiếm trang PDF 26–31 của `ridebound/main.pdf` (trang 31 đầy
khoảng 80%), tức ≈ 5,8 trang. Từ đó mật độ là ≈ 480 tiếng mỗi trang nếu tính cả công thức và bảng, ≈ 550 tiếng mỗi
trang văn xuôi thuần. Với v4: 2.575 tiếng chia 480–550, cộng ≈ 1,4–1,55 trang cho hai bảng, công thức và tiêu đề,
được 6,2–6,9 trang. Cột "ước lượng trang" dùng cùng khoảng đó.

**Về con số "330 words per page" của brief.** Nếu đọc 330 là số tiếng (âm tiết) thì v4 tương đương ≈ 9 trang, vượt xa;
nhưng chính chương cũ cho thấy một trang mẫu UET 13 pt, giãn 1,5 dòng chứa ≈ 480–550 tiếng. Tôi hiểu 330 là "từ" theo
nghĩa tiếng Anh (một từ tiếng Việt thường 1,3–1,6 âm tiết) và viết theo mật độ đo được. Đây là điểm tôi ít chắc nhất
(mục 7).

**Chỗ cắt nếu bản dựng thật vượt 6,5 trang** (theo thứ tự; không mất yêu cầu bắt buộc nào của outline):
1. Mục 2.3: bỏ câu Lu–Kühnel và câu Mt-KaRRi khỏi văn xuôi (Bảng 2.2 vẫn giữ hai hàng đó). ≈ 70 tiếng.
2. Mục 2.4: gộp đoạn TLC thành một câu ("Dữ liệu chuyến công khai của TLC được công bố theo tháng, thường trễ khoảng hai
   tháng."), bỏ câu suy luận. ≈ 40 tiếng.
3. Bảng 2.2: bỏ hai hàng đầu (cửa sổ đón, thời gian ngồi xe), vì đã có ở Bảng 2.1. ≈ 0,15 trang.
4. Mục 2.1: bỏ câu về cách dựng nhóm dần theo kích thước. ≈ 30 tiếng.

## 2. Nhãn

**Chương này định nghĩa (9):** `chuong:coso`; mục `muc:c2-baitoan`, `muc:c2-dolech`, `muc:c2-rangbuoc`,
`muc:c2-dubao`, `muc:c2-giatri`; công thức `eq:c2-chon`; bảng `bang:c2-dichvu` (Bảng 2.1), `bang:c2-dangrangbuoc`
(Bảng 2.2).

Bốn nhãn mà Chương 3 v3 trỏ tới đều có và nội dung khớp: `muc:c2-baitoan` (bước chọn theo lối Alonso-Mora,
`07-chuong3-v3.tex:108`), `muc:c2-rangbuoc` (Hörl–Zwick, `:450`), `muc:c2-dolech` (Fielbaum–Alonso-Mora, `:461`),
`muc:c2-dubao` (lời hứa theo dự báo là cách làm đã có, `:487`).

**Chương này cần (8), đều đã có:** `chuong:phuongphap`, `muc:baitoan-phatbieu`, `muc:bamoc`, `muc:luatc`,
`muc:doichung`, `muc:dubao` (Chương 3 v3); `chuong:thucnghiem`, `muc:c4-kichban` (Chương 4 phần A v4).

## 3. Chỗ lệch so với OUTLINE-V2 và các bản trước, kèm lý do

### 3.1 Sáu chỗ sửa diễn đạt từ v1 sang v2 (đối chiếu lại bài gốc)
1. Fielbaum–Alonso-Mora "hơn một phần ba … gặp ít nhất một thay đổi": thêm phạm vi "khi không hạn chế việc chuyển khách
   sang xe khác" (tóm tắt của bài) và đổi "xấp xỉ" thành "tương đương" ("comparable").
2. Leonardi và cộng sự: các chuyến được quan sát **trong mô phỏng VISUM**, không phải chuyến thật.
3. Chiều kéo sớm: v1 viết "hầu như không xuất hiện", sai; theo Phụ lục 1 mục 0.2, các lần đó có nhưng mỗi lần chỉ sớm
   1 ms. v2 viết đúng như vậy và giới hạn "trên tập kiểm tra chính".
4. Câu Hörl–Zwick về đánh đổi bị lặp ở 2.3 và 2.4; 2.4 chỉ còn câu nối.
5. Định nghĩa độ chùng của Elmi viết lại theo công thức 2 của bài.
6. "mức dự đoán được" đổi thành "mức dự báo được" (tránh gần với cụm bị cấm "dự đoán trước").

### 3.2 Lệch so với outline
1. **Bảng 2.1 có thêm cột "Ở một số nghiên cứu trước".** Outline chỉ đòi giá trị của tập thử. Cột này tách lý thuyết
   khỏi cấu hình của khóa luận và cho thấy mỗi bài tính từ một mốc khác (D03:252: không trích "10 phút" hay "1,5 lần"
   khi bỏ gốc thời gian). Chú thích bảng ghi "cấu hình của tập thử, không phải chuẩn ngành" như outline.
2. **Bảng 2.2 thêm hàng "Giữ giờ đón đã báo"** (Alonso-Mora: hạ giờ đón muộn nhất về giờ đón dự kiến khi đã ghép xe;
   Lu–Kühnel: đệm 2–3 phút so với giờ hẹn ban đầu). Khóa giờ đón mà cả điều phối không trần lẫn luật C dùng đã có tiền
   lệ; thiếu hàng này thì người đọc có thể hiểu khóa giờ đón là ý của khóa luận. Hai cột đổi tên cho rõ: "Gốc thời gian"
   → "So với mốc nào", "Ghi theo từng khách?" → "Ghi riêng cho từng khách?".
3. **Số hạng chi phí của khách cũ** lấy từ công thức (1) của Alonso-Mora (đã đọc) thay cho khóa `fielbaum2022scale`
   của chương cũ (tệp cục bộ là bản tiền ấn tên khác, bản in chưa mở; C2-24). Câu cũ "bị dời tích lũy tới mười bốn phút"
   không có dòng sổ nên bỏ.
4. **Elmi và cộng sự có một đoạn ở 2.2**, ngoài hàng ở Bảng 2.2: bài này kiểm soát cùng loại độ bất ổn với
   Fielbaum–Alonso-Mora, và phải được mô tả bằng lời để Bảng 2.2 đọc được.
5. **Nguồn thực hành dự báo (J35)**: dùng bài DeeprETA của nhóm Uber trên arXiv (đã đọc) thay cho trang blog DeepETA
   (đường dẫn cũ trả 404) và DoorDash (chỉ Codex kiểm). Lu–Kühnel (J22, outline xếp ở 2.4) được dùng ở 2.3 vì đó là một
   ràng buộc giờ đón.
6. **2.5 thêm Yu, Zhang và Zhou (J33)**, chỉ đọc tóm tắt; thân bài có chú thích chân trang nói rõ (STYLE quy tắc 35).
7. **Hörl–Zwick** được gọi bằng "công thức 7", "công thức 8", "ràng buộc 9--10", "công thức 11"; chữ "chiến lược B/C"
   chỉ còn trong dòng `% EV` (OUTLINE-V2 quy tắc 6, RD LR-21).
8. **Bỏ ở v3:** câu Kovacs (2014) và Sridharan và cộng sự (1987) về đánh đổi ổn định–hiệu quả ở lĩnh vực khác, để vừa
   trang; nguồn đã kiểm (C2-20, C2-21) nếu muốn lấy lại.
9. **Brief trỏ sai tệp:** `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf` là Sharif Azadeh và cộng sự (TR-B 2022),
   không phải Hörl–Zwick; tôi dùng `optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf` (C2-01).

### 3.3 Trùng với Chương 3 (để người ghép quyết)
- Bảng 2.1 và Bảng 3.2 của Chương 3 (`bang:rangbuoc`) cùng ghi 10 phút, 1,5 lần, 4 chỗ cho tập thử. Hai bảng có vai trò
  khác (2.1: so với nghiên cứu trước; 3.2: ràng buộc cứng và thứ tự tiêu chí). Có thể để Bảng 3.2 trỏ về Bảng 2.1 cho
  giá trị; tôi không sửa Chương 3.
- Mục 2.3 nói bằng lời điều mà Chương 3 viết thành công thức (`eq:dongnhat`, mục 3.4) và trỏ sang đó; không lặp định
  nghĩa, không dùng ký hiệu $v, e, p, B$ (OUTLINE-V2 quy tắc 7).

## 4. Câu là suy luận của người viết (có ghi trong dòng `% EV`)
1. 2.1: "một khách vì thế có thể bị dời giờ trả nhiều lần, miễn là mỗi lần tổng chi phí nhỏ hơn" (suy từ định nghĩa
   hàm mục tiêu, không phải kết quả đo).
2. 2.2: ví dụ "dời muộn 5 phút rồi được kéo về giờ cũ có hiệu bằng 0" (ví dụ dựng tay từ định nghĩa của bài).
3. 2.4: "Hồ sơ lập từ các ngày ngay trước … vì vậy giả định hãng xe có sẵn dữ liệu chuyến của chính mình" (suy từ độ trễ
   công bố của TLC và quy tắc ngày nguồn F02; sổ chưa có dòng nói điều này).
4. Bảng 2.2, cột "Phần do tắc đường có bị tính?" cho các hàng nghiên cứu trước: đọc từ định nghĩa ràng buộc, các bài
   không tự viết câu đó (trừ Elmi, bài nói rõ không xét giao thông).

## 5. Bằng chứng còn thiếu (nên không viết)
- Tên hội nghị của Hörl–Zwick (DataCite không ghi).
- Cách tính tệp hệ số 15 phút của FleetPy (bài chỉ mô tả hệ số theo giờ); chương chỉ nói gói dữ liệu có tệp đó.
- Con số 47,8% của Elmi (tóm tắt không rõ là giảm tương đối hay điểm phần trăm); không dùng.
- Toàn văn Yu–Zhang–Zhou; bản tạp chí của Leonardi (Transportmetrica A); toàn văn Cordeau–Laporte 2007.
- J13 Haferkamp, J14 Ackermann–Rieck, J15 Tellez, J16 "anticipatory walking", J41 Ding–Dandl–Bogenberger: chưa mở,
  không trích. STYLE quy tắc 35 đòi trích Ding và cộng sự; outline chỉ cho trích sau khi mở bài.

## 6. Câu hỏi mở cho chủ nghiên cứu
1. **Độ dài:** chấp nhận cách quy đổi ở mục 1 (≈ 480–550 tiếng mỗi trang) hay muốn đúng 330 tiếng mỗi trang? Nếu là
   330, chương phải cắt khoảng 35% và sẽ mất phần §6 của Fielbaum–Alonso-Mora hoặc Bảng 2.2.
2. Giữ chú thích "chỉ đọc phần tóm tắt" cho Yu và cộng sự, hay đọc toàn văn rồi bỏ chú thích, hay bỏ câu đó?
3. Trích Leonardi và cộng sự bản arXiv (đã đọc) hay bản tạp chí 2026 (chưa mở)?
4. Bảng 2.1 và Bảng 3.2 trùng giá trị: giữ cả hai hay để một bảng trỏ sang bảng kia?
5. Có muốn lấy lại câu Kovacs/Sridharan (v2, cuối mục 2.2)?
6. Câu suy luận về dữ liệu TLC ở 2.4 (mục 4, ý 3): giữ hay bỏ?
7. Sửa mục `alonsogonzalez2020` trong `10-tai-lieu.tex` (tác giả sai, BIB mục 1) khi ghép.

## 7. Ba điểm tôi ít chắc nhất
1. **Độ dài thật của chương** (≈ 6,2–6,9 trang): chưa dựng PDF; quy đổi "330 words" sang tiếng là cách hiểu của tôi.
2. **Các ô "Phần do tắc đường có bị tính?" và "Cộng qua cả chuyến?" của Bảng 2.2** cho nghiên cứu trước: là cách đọc
   định nghĩa của tôi, ngắn gọn hơn bài gốc; nhất là hàng Schulz–Pfeiffer ("khi thời gian đi đổi thì có") và hàng
   Hörl–Zwick ("riêng tắc đường không làm tuyến bị loại", vì giờ bắt buộc được nới tới giờ cập nhật).
3. **Câu suy luận về dữ liệu TLC** và cách đọc kết quả dự báo là "mức trần" (REG I02): câu đầu chưa có dòng sổ riêng;
   câu sau dựa vào I02 và F10, không phải một phép đo so với tắc đường theo từng đoạn đường.
