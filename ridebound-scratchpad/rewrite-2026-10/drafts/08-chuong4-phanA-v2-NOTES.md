# 08-chuong4-phanA — NOTES của vòng sửa R25 (2026-10-12)

## 0. Tệp nào là bản dùng để ghép

| Tệp | Vai trò |
|---|---|
| `drafts/08-chuong4-phanA.tex` | Bản 1 (2026-10-11), giữ nguyên. |
| `drafts/08-chuong4-phanA-v2.tex` | Lượt sửa đầu: áp mọi quyết định của `reviews/CH4A-REVISION-LOG.md`. Dài 5.582 tiếng văn xuôi, vượt ngân sách khoảng 2,5 trang. **Không dùng để ghép.** Trong lượt này có ba chỉnh nhỏ ngay trên chính tệp v2 trước khi đếm độ dài (phạm vi "bốn mẫu", phạm vi bộ chạy đã lưu, cách nói "2 trong 148"); sau đó không sửa v2 nữa. |
| `drafts/08-chuong4-phanA-v3.tex` | Lượt rút gọn thứ nhất (5.189 tiếng), vẫn vượt ngân sách. **Không dùng để ghép.** |
| **`drafts/08-chuong4-phanA-v4.tex`** | **Bản dùng để ghép.** Cùng mọi quyết định và con số của v2; chỉ rút gọn câu chữ, tách câu dài và cắt ba chỗ ghi ở §6. Bản nháp trung gian của v4 được làm trong thư mục scratchpad của phiên, rồi chép một lần vào dự án (không ghi đè). |

Tên tệp NOTES giữ `-v2-NOTES` theo yêu cầu đầu ra; nội dung dưới đây mô tả **v4**.

Các tệp khác tạo trong vòng này: `reviews/CH4A-REVISION-LOG.md`; `evidence/EVIDENCE-REGISTER-ADDENDUM-4-CH4A.md` (C4A-01…20);
`evidence/checks-ch4a-v2/` (ba script chỉ đọc, ba output, log stdout/stderr); `style/GLOSSARY-VI-v2.md` (bản sao bảng thuật
ngữ, sửa hai dòng 92–93). Không ghi vào thư mục luận văn, `E:/Code/RideBound*` hay `C:/Code/*`; không mô phỏng, build, cài.

Kiểm cú pháp v4 (script đọc, không biên dịch): ngoặc `{}` 395/395; mọi `\begin`/`\end` khớp (12 table, 16 tabular,
1 figure, 1 tikzpicture, 3 scope); số `$` chẵn (74); không có từ cấm ("niêm phong", "dự đoán trước", "duy nhất", "tối ưu",
"phải phục hồi", "chúng tôi"…). **Chưa biên dịch thử** (build bị cấm); người ghép cần chạy tectonic với `--keep-logs`.

## 1. Độ dài theo mục (v4) so với ngân sách

Cách đếm như NOTES bản 1: "tiếng" = token cách nhau bởi khoảng trắng sau khi bỏ dòng `%`, lệnh LaTeX và `$…$`; chữ trong
bảng, hình đếm riêng; văn xuôi 480–560 tiếng/trang; bảng ước theo số dòng in. Đây là ước lượng, không phải bố cục đo.

| Mục | Ngân sách (tr.) | Văn xuôi v1 | Văn xuôi v4 | Bảng, hình v4 | Ước lượng v4 (tr.) |
|---|---:|---:|---:|---|---:|
| Mở chương + Bảng lộ trình | 0,5 | 118 | 131 | lộ trình 10 dòng | 0,7–0,75 |
| 4.1 Thiết lập | 3 | 702 | 923 | tham số, tập thử, chỉ số | 3,25–3,55 |
| 4.2 Kết quả chính | 3,75 | 1.065 | 1.164 | chính, nghĩa vụ, phân bố trễ (bỏ bảng ngày × khung) | 2,9–3,25 |
| 4.3 Phần do điều phối | 2,25 | 802 | 733 | dời do điều phối | 1,7–1,9 |
| 4.4 Chọn mức trần | 3 | 924 | 879 | cố định, buổi sáng (6 dòng), trần 120 (16 dòng), hình | 2,95–3,2 |
| 4.5 Vế cộng dồn | 1,25 | 647 | 692 | kiểm bản ghi | 1,6–1,8 |
| **Tổng** | **13,75** | **4.258** | **4.522** | 12 bảng + 1 hình (v1: 13 + 1) | **≈ 13,0–14,4** |

Bản 1 theo cùng cách tính: 12,9–14,2 trang. v4 dài hơn v1 khoảng 0,1–0,2 trang ở giữa khoảng, chủ yếu do mục 4.1 (định
nghĩa cho người đọc ngoài ngành, câu về độ dài lời hứa đầu, câu thăm dò 120 giây); bỏ bảng ngày × khung bù lại khoảng 0,45
trang. Câu: 171 câu, trung vị 26 tiếng, 18 câu trên 40 tiếng, 0 câu trên 50 (v1: 162 / 27 / 19 / 1).

Nếu bản dựng thật vượt, cắt theo thứ tự (≈ 230 tiếng): ví dụ dựng tay về hai cách gộp ở 4.1.3 (≈ 35); câu độ dài lời hứa
đầu ở 4.1.3 (≈ 40); câu "Luật trần độ dời khách thấy bị ép nhiều nhất…" ở 4.2 (≈ 35); đoạn dấu vết ở tắc đường cố định và
tự tạo ở 4.5 (≈ 70); câu "Theo khung giờ…" ở 4.4 (≈ 15); cột "Đại lượng được đo" của Bảng lộ trình (≈ 0,1 tr.).

## 2. Dòng `% EV:` và sổ

86 dòng `% EV:`. Ngoài các dòng của sổ chính và hai phụ lục, v4 trỏ tới **C4A-01…C4A-20** (phụ lục 4, tệp mới). Đã thay
các anchor cũ mà kiểm chứng sự kiện R25 §3 chỉ ra: X3-18 (đã bỏ) → C4A-15 (TEX08:136-137); "R23 #105" → X3-32; "R23 #51"
→ X3-38; "R23 #57" → X3-28, X3-41; bỏ các mã RD (LR-xx, CX-xx) vì không phải dòng sổ; thêm T38:12 (C4A-17) cho câu chạy lại.
Chú thích đầu tệp nay nói X3 nằm ở phụ lục 2.

## 3. Nhãn

**Phần A định nghĩa:** `chuong:thucnghiem`, `muc:c4-thietlap`, `muc:c4-kichban`, `muc:c4-taptu`, `muc:c4-chiso`,
`muc:c4-thamdo`, `muc:c4-ketqua`, `muc:c4-dieuphoi`, `muc:c4-chontran`, `muc:c4-congdon`; bảng `bang:c4-lotrinh`,
`bang:c4-thamso`, `bang:c4-taptu`, `bang:c4-chiso`, `bang:c4-chinh`, `bang:c4-nghiavu`, `bang:c4-phanbotre`,
`bang:c4-doidieuphoi`, `bang:c4-codinh`, `bang:c4-sang`, `bang:c4-tran120`, `bang:c4-congdon`; hình `hinh:c4-tran`.
**Đã bỏ:** `bang:c4-ngaykhung` (bảng ngày × khung; không chương nào khác trỏ tới nó; Chương 3 v3 không dùng).

**Nhãn từ Chương 3 v3 (đều có):** `muc:kientruc`, `muc:bamoc`, `muc:luatc`, `muc:doichung`, `muc:dubao`, `muc:so`,
`muc:kiemtra`, `bang:rangbuoc`, `bang:luat`, `bang:kiemtran`, `eq:so`, `eq:dongnhat`, `nx:giunguyen`. Mới so với v1:
`muc:so`, `muc:kiemtra`, `bang:kiemtran`, `eq:dongnhat` (đều đã định nghĩa trong v3, đã kiểm bằng script).

**Phần B phải định nghĩa:** `muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet`, `muc:c4-hople` (và
`muc:c4-thaoluan` nếu dùng). Chương 3 v3 cũng trỏ tới `muc:c4-dubao`, `muc:c4-hople`, `muc:c4-vaitro`.
**Chương khác phải định nghĩa:** `muc:c1-cauhoi` (Chương 1), `phuluc:A`, `phuluc:C`. Khóa trích dẫn: `engelhardt2026`
(mới, metadata X3-40) và `schulz2026` (có sẵn).

## 4. Bằng chứng mới và cách tính

| Con số mới in trong v4 | Giá trị | Nguồn |
|---|---|---|
| Khách trễ quá 30 giây so với lời hứa đầu, luật C trần 30 giây (cùng thước với luật hạn chót) | 292 / 2.338 = 12,5% gộp; 14,6% TB theo kịch bản; 28/34 kịch bản | C4A-01: `checks-ch4a-v2/check-ch4a-v2-2026-10-12.txt` (bộ đọc IVC), TSV Giai đoạn 1a, cột late30 ở ADD1:17 |
| M⁺-60 và V-30: trễ quá 60 s, không trễ quá 60 / 120 s | 79, 2.268, 2.336; 74, 2.262, 2.325 | C4A-02 (cùng output; EXP:5-6) |
| Tử số, mẫu số của "phần tính cho điều phối" | 23.027 / 31.353 s; 82 / 6.892 s; 4.836 / 12.450 s | C4A-03: `ledger-share-sums-2026-10-12.txt` |
| Tập tắc đường cố định: số khách đi chung, bị dời | 865 / 346 / 303 / 266 / 241; 388 / 62 / 41 / 20 / 6 | C4A-04: `fixed-shared-counts-2026-10-12.txt`; WBU:4-16 |
| Tập buổi sáng: C-60, C-150, C-180, C-240, C-300 | 661/47/614/659; 666/51/615/659; 665/50/615/656 | C4A-05: CAP:5,8-11; DIAL17:5,8-11 |
| Chiều tuyết: số yêu cầu | 864 (8 × 108) | C4A-06: INV:14-22 |
| Tập buổi sáng: lần chạy của các cấu hình được so | 136 trong 192 | C4A-07 |
| Tới sớm quá 60 s, lời hứa không dự báo | 7 / 3 / 1 (U / C-30 / C-120) | C4A-13 |
| Trễ lớn nhất | 660,1 s / 232,3 s | C4A-14 (CON:4,11) |
| Dùng lần đầu từ sổ có sẵn | độ dài lời hứa đầu 14,15 / 14,12 phút (B14); 1.238 yêu cầu bị từ chối khi không trần (3.672 − 2.434; CON:3); 1.075 trong 1.186 cũng bị từ chối khi không trần (D13); 61 trong 76 khách trễ ở khung 7 giờ (N-11); U 0 / 20.760 quyết định bị ép (X3-16); tới sớm có dự báo 8 / 4 / 2 (N-03, N-16, N-06) | sổ chính, phụ lục 1, 2 |

Ba script: 32 + 3 + 5 phép đối chiếu với số đã có trong sổ, **0 FAIL**.

## 5. Bằng chứng còn thiếu (không viết, hoặc viết có giới hạn)

1. **Cách lấy 108 yêu cầu từ một mẫu 10%** và vì sao khung 17 giờ có chung yêu cầu với khung 7, 8 giờ (người đọc D4, D7):
   sổ chỉ có B02, B11 ("cùng nguồn nhu cầu"); không viết cơ chế.
2. **Bằng chứng chạy lại cho đúng kết quả cũ** (giảng viên G1): không có lần chạy lại mô phỏng nào trong sổ (L1a-04 là đọc
   lại transcript). v4 chỉ nói thế giới mô phỏng không có nhiễu ngẫu nhiên (B06; RW7:6). **Với 8 lần chạy chiều tuyết, cấu
   hình thế giới chưa được mở** (chỉ đọc được log kiểm `check-runs-snow`): câu "không có nhiễu ngẫu nhiên" chưa kiểm cho tập
   này.
3. **Nguyên nhân của các lần dời sớm 1 mili giây** (C4A-19, UNVERIFIED): giữ "đúng 1 mili giây", không nêu nguyên nhân.
4. **Số khách đi chung chính xác của M⁺-60 và V-30**: chỉ có % làm tròn (EXP) → "chưa đếm" trong Bảng kết quả chính.
5. **Số kịch bản của tập kịch bản tĩnh** ("20 kịch bản" chỉ có trong OUTLINE, không có dòng sổ): không viết số.
6. **Bộ chạy, luật phục hồi của chiều tuyết**: vẫn "chưa kiểm lại" (X3-10).
7. **Giới hạn bộ sinh, bộ giải của bộ chạy cũ** (tập tắc đường cố định): chưa kiểm (C4A-18) → ghi ngoại lệ trong chú thích.
8. **Tử số theo từng kịch bản cho các tỉ lệ trung bình theo kịch bản** (Codex §5.7): có trong output gốc (T38A, W07X) nhưng
   không chép vào chương; bảng chỉ ghi rõ mẫu số và cách gộp.

## 6. Chỗ lệch so với OUTLINE-V2 và so với v2, và lý do

1. **Mở mục 4.2** không dùng câu trả lời mẫu của OUTLINE (bắt đầu bằng +31 lượt đúng giờ); theo quyết định về câu hỏi đệm,
   câu mở nêu trước điều luật C giữ được (giới hạn theo từng khách 29,2 so với 590,1 giây; 0 so với 18 lượt trễ quá 5 phút),
   rồi cái giá (−96 lượt, −242 khách đi chung), rồi số lượt đúng giờ như chỉ số phụ đổi chiều theo ngưỡng. Thêm **một câu
   trỏ tới** `muc:c4-dem` với một con số (2.328 bằng 2.328 khi có dự báo và đệm 30 giây). Phân tích đầy đủ vẫn ở 4.8.
2. **Bảng 4.7 (ngày × khung) bị bỏ khỏi thân bài** để giữ ngân sách; giữ đoạn tóm tắt (34/34, 29/34, 25/25, 3 + 6). Dữ
   liệu đầy đủ ở ADDENDUM-1 (N-22) nếu chủ sở hữu muốn đưa sang Phụ lục C.
3. **Bảng 4.4**: M⁺-60, V-30 có số trễ và không trễ (C4A-02); cột đi chung "chưa đếm".
4. **Bảng 4.9b**: đủ tám mức (C4A-05); các mức trùng mọi số đếm gộp một dòng; Hình (b) vẽ đủ tám mức. Tỉ lệ bị ép của luật
   hạn chót ở tập buổi sáng (trung bình theo kịch bản) không đưa vào bảng (OUTLINE §2 quy tắc 3: không chung khối với số gộp);
   v4 chỉ nêu đầu, giữa, cuối dãy (58,6 → 6,6 → 1,7%).
5. **Bảng 4.9a**: thêm số đếm cho hai cột tỉ lệ (C4A-04).
6. **Bảng 4.9c**: thêm hai dòng "tới sớm quá 60 s" (STYLE quy tắc 31).
7. **Cắt so với v2 vì ngân sách** (có thể khôi phục nếu bản dựng còn chỗ): câu chờ, ngồi xe của 2.207 khách chung (C05;
   ≈ 45 tiếng); ví dụ trần 300 giây, 307,3 = 99,1 + 208,2 giây (N-30; ≈ 35 tiếng); dãy đủ bảy tỉ lệ bị ép của luật hạn
   chót; số theo khung giờ của trần 120 giây (+26/+34 ở khung 8 giờ, +19/+20 ở khung 17 giờ; còn câu "dồn vào khung 8 và 17
   giờ"); khoảng 61–79 / 61–68 giây của ba chỗ tách luật ở ví dụ cơ chế; câu "theo các bản ghi, một trần cho từng lần dời
   cũng sẽ chặn gần như mọi phương án…" ở 4.5.
8. **Thuật ngữ**: "quyết định bị ép" thay "quyết định phải phục hồi" (khớp Chương 3 v3 và bảng thuật ngữ); định nghĩa theo mã
   (C4A-10). "Hệ số tắc đường đo được" thay "hệ số tắc đường đo". "Khách bị phá lời hứa" thay "khách bị chính luật phá lời
   hứa". Ký hiệu cấu hình (U, C-$B$, M⁺-$B$, V-30, FREE) được giải nghĩa trong chú thích Bảng tập thử, không thành danh sách
   trong văn xuôi (OUTLINE: ký hiệu chỉ trong bảng).

## 7. Ghi chú cho người viết phần B

- **Tên và định nghĩa:** dùng "quyết định bị ép" (không dùng "phải phục hồi"): lượt quyết định có ít nhất một xe bị ép,
  tức luật lời hứa đã loại cả phương án giữ nguyên kế hoạch và xe đi theo phương án được giữ nhờ luật phục hồi, có ít nhất
  một khách được miễn trừ; không đòi mọi phương án khác bị loại (C4A-10; `style/GLOSSARY-VI-v2.md`). Dùng "hệ số tắc đường
  đo được". "Khách bị phá lời hứa".
- **Số đã in ở phần A, phần B chỉ cần trỏ:** Bảng 4.4 (U, C-30, M⁺-30, M⁺-60, V-30, không dự báo); Bảng nghĩa vụ; phân bố
  trễ (trễ lớn nhất 660,1 / 232,3 s); phần dời do điều phối U / C-30 / C-120 kèm tử số, mẫu số của tỉ lệ sổ; Bảng trần 120
  (khối có dự báo: trễ quá 60 s 137 / 10 / 65; tới sớm 8 / 4 / 2; không trễ 2.297 / 2.328 / 2.322 và 2.347 / 2.338 / 2.379;
  dài thêm 7,18 / 7,37 / 7,27 s); cuối tuần 29,2 / 116,5 s; chiều tuyết 8/601, 25,2 s, 0/5.067; C-30 trễ quá 30 giây 292 /
  2.338 (C4A-01); độ dài lời hứa đầu 14,15 / 14,12 phút (B14).
- **Phần A đã nói về đệm đúng một câu** (mục 4.2): khi có dự báo, U + đệm 30 giây cũng cho 2.328 lượt không trễ quá một phút,
  bằng luật C có dự báo, nên khóa luận không dùng chỉ số này làm lý do chọn luật C. Mục 4.8 phải đưa câu trả lời đầy đủ theo
  RD §8 và bảng của Codex R25 §6 (cùng độ dài lời hứa, hai phía, phần đuôi 68 / 11 / 1 so với 0 / 0 / 0, giới hạn theo từng
  khách 590,1 so với 29,2 giây, cái giá 96 lượt và 242 khách đi chung; đệm U là phát lại trên quỹ đạo của U).
- **Khối "có dự báo" của Bảng trần 120 trỏ sang `muc:c4-dubao`**: 4.7 cần bàn 76 → 10 lượt trễ của luật C là kết quả phát
  lại (người đọc hỏi).
- **Cho 4.10–4.11:** thời gian dừng 0 giây (B05) và không có bằng chứng chạy lại mô phỏng cho đúng kết quả cũ thuộc phần hạn
  chế; giới hạn 2 yêu cầu mới áp cho cả lô của lượt, không phải "mỗi xe" (X3-32; sổ A24 sai chữ); 12 lần chạy luật C của
  phép quét trên hệ số đo được chưa kiểm bản ghi chặn (C4A-08); nguyên nhân −1 ms chưa kiểm (C4A-19).
- **Đã bỏ** `bang:c4-ngaykhung`; đừng trỏ tới nó.
- Phần A chưa nói về: 0,17% (K24), 13,7 s, 3,2 s, 34/1.471, Họ B, học máy, sổ ba phần ngày thường / chiều tuyết, sàng lọc
  bộ chọn, bộ đếm hợp lệ (N-25), 382.006 lần sửa.

## 8. Câu hỏi mở cho chủ sở hữu

1. **Bản ghép là `-v4.tex`** (v2, v3 là lượt trung gian). Xác nhận dùng v4.
2. **Bảng ngày × khung**: bỏ hẳn, hay đưa sang Phụ lục C (dữ liệu có sẵn ở N-22)?
3. **Ba chỗ cắt vì ngân sách** (§6 ý 7: khách chung chờ +0,5 s / ngồi −10,5 s; ví dụ trần 300 giây; dãy đủ bảy tỉ lệ bị ép):
   khôi phục nếu bản dựng thật còn chỗ?
4. **Độ dài thật**: ước lượng 13,0–14,4 trang chưa phải bố cục đo; cần một lần build để biết có phải cắt tiếp (§1) không.
5. **Một câu về đệm ở 4.2 có kèm một con số (2.328)**: chấp nhận, hay chỉ trỏ sang 4.8 không kèm số?
6. **Nguyên nhân −1 ms**: giữ "chưa kiểm", hay cho phép một phép đọc transcript chỉ đọc để kiểm giả thuyết làm tròn mili giây
   trên từng cung (C4A-19)?
7. **Chiều tuyết**: bộ chạy và cấu hình thế giới vẫn chưa kiểm; có cần kiểm trước khi nộp không?
8. **Registrar**: cập nhật D13, D19, A24, ADDENDUM-1 mục 0.3 và nhận `style/GLOSSARY-VI-v2.md` thay bản cũ? (Phụ lục 4,
   mục "Dòng của sổ cũ cần cập nhật".)
9. **Nhãn ngoài chương**: `muc:c1-cauhoi` (Chương 1), `phuluc:A` (nếu Phụ lục A bị bỏ, câu ở `muc:c4-thamdo` phải đổi thành
   "tập kịch bản tĩnh của đợt thử trước" không kèm tham chiếu), `phuluc:C`.
10. **Bảng lộ trình** ở đầu chương: giữ (OUTLINE Bảng 4.0) hay bỏ cột thứ ba để lấy lại ≈ 0,1 trang?
