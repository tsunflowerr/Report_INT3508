# FRONT-NOTES — phần đầu khóa luận (Lời cảm ơn, Tóm tắt, Abstract, Danh mục ký hiệu và chữ viết tắt), 2026-10-14

Viết theo OUTLINE-V2 §4 và §6.3–6.4, WRITING-BRIEF, STYLE-GUIDE-VI, GLOSSARY-VI-v2, R31 M1–M4 và ràng buộc công bằng
của điều phối viên. Không sửa thư mục luận văn, không dựng PDF.

## 0. Đầu vào đã đọc

| Phần | Tệp (chỉ đọc) |
|---|---|
| Ch1 | `optimize/codex-debate/codex-work/r40-ch1-v4/05-chuong1-v4-v4.tex` (bản mới theo tin nhắn điều phối viên; thay r30 v3) |
| Ch2 | `rewrite-2026-10/drafts/06-chuong2-v6.tex` |
| Ch3 | `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex` |
| Ch4A | `codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex` |
| Ch4B | `codex-work/r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex` (bản mới; thay v10) |
| Ch5, Phụ lục | `codex-work/r31-ch5/10-chuong5-v2.tex`, `11-phuluc-v2.tex` |
| Định dạng | `ridebound/noi-dung/01-loi-cam-on.tex`, `02-tom-tat.tex`, `04-viet-tat.tex`, `main.tex` |
| Mẫu văn phong | DACN PDF tr. 4–5 (Lời cảm ơn, Tóm tắt, Abstract), đọc bằng `pdftotext -enc UTF-8` |
| Bằng chứng | `evidence/EVIDENCE-REGISTER.md`; ADDENDUM-1 (N-xx, L1a-xx), ADDENDUM-4 (C4A-xx) |

## 1. Tệp tạo mới (tạo độc quyền, không ghi đè)

- `drafts/01-loi-cam-on.tex`
- `drafts/02-tom-tat.tex` (Tóm tắt + Abstract, cùng khuôn với tệp hiện tại: `\chapter*`, `\addcontentsline`, dòng
  từ khóa, `\clearpage`)
- `drafts/04-viet-tat.tex`
- `drafts/FRONT-NOTES.md` (tệp này)

Bản nháp trung gian và script đếm nằm ở thư mục scratchpad của phiên (`.../scratchpad/front/`: `count.py`,
`tomtat-draft1..3.txt`, `alternates.txt`).

## 2. Số đếm

Cách đếm: `count.py` (scratchpad), "tiếng" = chuỗi cách nhau bởi khoảng trắng có ít nhất một chữ hoặc số (STYLE §0);
bỏ dòng `%` và lệnh LaTeX. Dòng từ khóa đếm riêng, không tính vào giới hạn.

| Phần | Đoạn 1 | Đoạn 2 | Đoạn 3 | Tổng | Giới hạn |
|---|---:|---:|---:|---:|---:|
| Tóm tắt (tiếng) | 60 | 85 | 150 | **295** | 300 |
| Abstract (từ tiếng Anh) | 47 | 75 | 132 | **254** | gương của Tóm tắt |
| Lời cảm ơn (tiếng) | 77 | 96 | — | **173** | 1 trang |
| Từ khóa / Keywords | 25 tiếng (không kể "Từ khóa:") / 13 từ | | | | |

Câu dài nhất của Tóm tắt: 40 tiếng (câu về cách đệm); không câu nào vượt 40. Lời cảm ơn: câu dài nhất 40 tiếng.
Danh mục: 6 chữ viết tắt, 24 dòng ký hiệu và tên cấu hình, ước khoảng 1 trang (chưa dựng PDF).

Lịch sử độ dài: bản nháp 1 có 358 tiếng, bản 2 có 317, bản 3 có 314, bản cuối 295.

## 3. Chọn kết quả cho Tóm tắt

**Ba kết quả có số và một câu giới hạn** (tối đa là bốn):

1. **Cái giá và điều luật C cho:** ít hơn 96 lượt phục vụ trên 3.672 yêu cầu; tổng phần dời tính cho điều phối của
   mỗi khách không quá 29,2 giây, so với 174 trong 2.434 khách bị dời, nhiều nhất 590,1 giây, khi không trần.
2. **So với luật hạn chót (ràng buộc công bằng):** cùng 2.338 lượt; 292 và 289 khách tới sau hạn "lời hứa đầu + 30
   giây".
3. **So với cách đệm:** hòa 2.328 lượt không trễ quá một phút trên 3.672 yêu cầu; đệm hơn ở hai phút (2.366 so với
   2.338); lời hứa dài thêm 37,2 thay vì 7,4 giây.
4. **Giới hạn:** kết quả thăm dò, chỉ áp cho mô phỏng tải thấp đã dùng.

**Đã bỏ khỏi Tóm tắt, và vì sao.** Bốn ứng viên của OUTLINE §4 cộng phần bắt buộc của ràng buộc công bằng (292/289;
29,2 so với 590,1 giây) không vừa 300 tiếng: các bản nháp có 314–358 tiếng.
- **+31 lượt không trễ quá một phút.** Theo R31 M4, phải đi cùng vế "−5 lượt ở hai phút" (2.332 → 2.327). Cặp này
  thêm khoảng 29 tiếng và dễ bị đọc thành "luật C đúng giờ hơn", điều ràng buộc công bằng cấm ngụ ý.
- **Điểm trần 120 giây** (2.387 lượt; 2.366 lượt không trễ quá hai phút). Bỏ vì giới hạn độ dài; Ch1, Ch4A, Ch5 có đủ.
- **Phần cộng dồn** (3 trong 1.780 bản ghi, đều ở trần 120 giây). Bỏ vì giới hạn độ dài.

**Câu thay thế đã đếm sẵn** (mỗi câu muốn thêm thì phải bớt chừng ấy tiếng ở chỗ khác):

| Câu | Tiếng | EV |
|---|---:|---|
| Phép cộng qua cả chuyến chỉ là lý do riêng của 3 trong 1.780 bản ghi loại phương án, đều ở trần 120 giây; tác dụng của nó chưa được đo. | 31 | N-15; N-08; E01; E09 |
| Trần 120 giây là một điểm đo thêm: 2.387 lượt phục vụ và 2.366 lượt không trễ quá hai phút trên 3.672 yêu cầu. | 24 | N-06; L1a-02; K36 |
| So với điều phối không trần, số lượt không trễ quá một phút tăng 31 nhưng số lượt không trễ quá hai phút giảm 5, trên 3.672 yêu cầu. | 29 | C08 |

Gợi ý nếu chủ nghiên cứu muốn có câu cộng dồn: bỏ câu giới hạn hiện tại (16 tiếng) và rút đoạn 2 khoảng 15 tiếng; khi
đó vế "thăm dò, tải thấp" phải chuyển vào đoạn 2.

## 4. Kiểm ràng buộc công bằng

| Yêu cầu | Cách đáp ứng (câu trong Tóm tắt) |
|---|---|
| Không ngụ ý luật C giữ lời hứa đầu tốt hơn luật hạn chót | "Về giờ tới, luật C không hơn luật hạn chót 30 giây tính từ lời hứa đầu: cùng phục vụ 2.338 lượt, có 292 và 289 khách tới sau hạn đó." (292 là của luật C, nhiều hơn 289) |
| Không ngụ ý luật C phục vụ nhiều hơn | "phục vụ ít hơn điều phối không trần 96 lượt"; "cùng phục vụ 2.338 lượt" với luật hạn chót |
| Đệm hòa ở một phút, hơn ở hai phút | "cũng có 2.328 lượt … bằng luật C, và hơn ở hai phút (2.366 so với 2.338)" |
| Điều luật C cho | Giới hạn theo từng khách: "không quá 29,2 giây; khi không trần, 174 trong 2.434 khách bị dời, nhiều nhất 590,1 giây"; lời hứa ngắn hơn: "37,2 thay vì 7,4 giây" |
| Cái giá | "ít hơn … 96 lượt trên 3.672 yêu cầu" |
| Không gọi là mới | Mốc đo "đã có ở Hörl và Zwick"; lời hứa theo dự báo "vốn đã có"; động từ "đặc tả và cài đặt" |
| Không nhân quả cho sổ | "phần tính cho điều phối" (không "gây ra"); sổ chỉ được nêu tên |
| Không nói lợi ích kinh doanh, không "tối ưu" | Không có |
| Không nói kế hoạch ghi trước, dự đoán | Không có, kể cả trong dòng `%` |

29,2 giây là giá trị đo được trên tập chính (tối đa trên 2.338 khách được phục vụ). Tóm tắt không viết "bảo đảm":
Ch3 và Ch4B v11 nói giới hạn 30 giây được giữ dưới giả thiết (N).

## 5. Mọi con số và bằng chứng

Áp cho cả Tóm tắt và Abstract (Abstract dùng cùng số, viết kiểu Anh: 3,672; 29.2). Dòng `% EV:` có trong tệp.

| Số trong Tóm tắt | Nghĩa, mẫu số, cách gộp | EV | Chỗ trong chương |
|---|---|---|---|
| 34 kịch bản | Tập kiểm tra chính | B09 | Ch4A v5-v3:106-125 |
| 30 giây (trần) | Trần của C-30 | A06 | Ch3 Bảng luat |
| 96 lượt; 3.672 yêu cầu | 2.434 − 2.338 lượt phục vụ `[đếm]`; 3.672 = 34 × 108 | C01; C02; B09 | Ch4A:242-245 |
| 29,2 giây | Tổng \|c\| lớn nhất của một khách dưới C-30, trên 2.338 khách được phục vụ (29,239 s); 0 khách vượt trần, 0/34 kịch bản | C20; N-23; N-21 | Ch4A:242, 406 |
| 174 trong 2.434 | Khách bị điều phối dời giờ trả ít nhất một lần khi không trần `[gộp theo khách]` (7,15%) | C20; N-23 | Ch4A:407 |
| 590,1 giây | Tổng \|c\| lớn nhất của một khách khi không trần (590,133 s) | C20; N-23 | Ch4A:242, 407; Ch4B v11:229 |
| 30 giây (hạn chót) | Độ chùng của luật hạn chót M⁺-30 | A09; N-21 | Ch3 Bảng luat; Ch4A:252-254 |
| 2.338 lượt (cả hai luật) | Lượt phục vụ của C-30 và M⁺-30 trên 3.672 yêu cầu | C01 | Ch4A:276-277 |
| 292 và 289 | Khách được phục vụ có a − p₀ > 30.000 ms, trên 2.338 mỗi luật `[gộp theo khách]` (12,49% / 12,36%); mỗi luật 28/34 kịch bản | C4A-01; N-21 | Ch4A:355-358 |
| 2.328 lượt; 3.672 yêu cầu | Không trễ quá 60 s khi có dự báo: U + dự báo + đệm 30 s = C-30 + dự báo `[trên yêu cầu]` | C10; N-16 | Ch4B v11:226-227 |
| 2.366 so với 2.338 | Không trễ quá 120 s: U + dự báo + đệm 30 s so với C-30 + dự báo `[trên yêu cầu]` | C10; N-16 | Ch4B v11:227 |
| 37,2 thay vì 7,4 giây | Lời hứa dài thêm trung bình `[gộp theo khách]`: 37,1833 s trên 2.434 và 7,3671 s trên 2.338 khách được phục vụ | C10; N-16; N-18 | Ch4B v11:228 |
| (không số) "đã có ở Hörl và Zwick" | Mốc giờ trả của tuyến cũ tính lại | J01; J03 | Ch3:259-261 |
| (không số) "vốn đã có" | Lời hứa theo dự báo là thực hành đã có | J35; K37 | Ch2 v6:232-237 |
| (không số) "thăm dò", "tải thấp" | Dữ liệu đã xem; 0,535 khách trên xe khi không trần | I05; I06; C4A-11; B12 | Ch4A:231-235; Ch4B v11 mục thaoluan |

Lời cảm ơn không có số. Danh mục chỉ có các mức ví dụ trong định nghĩa (C-30, C-120; T = 30, 60, 120, 300, 600 giây),
lấy từ Ch3 Bảng luat và Ch4A Bảng c4-chiso.

## 6. Ký hiệu và chương dùng lần đầu

Chương 1 không có ký hiệu toán học nào; Chương 2 chỉ có ký hiệu riêng của công thức Alonso-Mora (eq:c2-chon). Mọi
ký hiệu chính xuất hiện lần đầu ở Chương 3, trừ $T$ và đơn vị "s" (Chương 4). Số dòng theo tệp ở mục 0, không kể dòng
`%`.

| Ký hiệu | Nghĩa (theo Danh mục) | Lần đầu | Ghi chú |
|---|---|---|---|
| $r$ | Một khách đã có lời hứa | Ch3:61 (Bảng thuatngu, trong $L_r$) | |
| $B$ | Trần (giây) | Ch3:61 | Ch4A dùng thêm cho luật hạn chót |
| $L_r$ (gọn $L$) | Phần trần đã dùng | Ch3:61 | Phụ lục dùng thêm $L^{\mathrm{V}}$ |
| $p_0$ | Lời hứa đầu không dự báo | Ch3:55 | |
| $v$, $e$, $p$ | Ba mốc giờ trả | Ch3:175 (Hình vongquyetdinh) | **Định nghĩa ở Ch3:247-256, sau lần dùng đầu** |
| $D$ | Lời hứa theo dự báo | Ch3:182, 186 (Hình vongquyetdinh) | **Định nghĩa ở mục dubao (Ch3:494+)** |
| $x$, $c$, $z$ | Ba hiệu | Ch3:222 (giả mã dòng 15) | **Định nghĩa ở eq:bamoc (Ch3:256)** |
| $p_n$; $j$, $n$ | Lời hứa cuối; chỉ số lần cập nhật | Ch3:452 (eq:dongnhat) | |
| $D_0$ | Lời hứa đầu theo dự báo | Ch3:563 | |
| $a$ | Giờ trả thực tế | Ch3:606-612 (eq:so) | **Ch3:194 đã dùng $a$ với nghĩa khác** (chú thích giả mã "$a \gets b$") |
| $q$, $f$ | Tổng có dấu của $c$; phần dự báo | Ch3:606-614 (eq:so) | |
| $\rho$ | $a - p_n$ | Ch3:615 | Chỉ dùng một lần |
| (N) | Giả thiết của Nhận xét giunguyen | Ch3:366 | Ch1 v4 mô tả bằng lời, không dùng ký hiệu |
| $T$ | Ngưỡng trễ | Ch4A:194 (Bảng c4-chiso) | |
| U, FREE, C-$B$, M$^{+}$-$B$, V-$B$ | Tên cấu hình | Ch3:422-435 (Bảng luat) | Ch4A Bảng c4-taptu nhắc lại |
| s | Giây, trong bảng | Ch4A:272 | |

**Ký hiệu cục bộ, không đưa vào Danh mục** (mỗi ký hiệu được giải thích ngay cạnh công thức; Danh mục có một câu nói
điều này):
- Ch2 eq:c2-chon: $\epsilon_{ij}$, $\chi_k$, $c_{ij}$, $c_{ko}$, $T_i$, $i$, $j$, $k$.
- Ch3 eq:chon: $y_{k\pi}$, $P_k$, $\pi$, $k$ (xe), $u$.
- Ch3 eq:keodan và Bảng dubao: $t$, $S$, $\tau$, $i(\tau)$, $m_i$, $\tilde m_i$, $g$, $H$, $W$, $h$, $i_0$, $d$; $K$
  (số khung lấy trung bình, Ch3:568).
- Ch4B v11:413-416: $k$ (chi phí mỗi lượt trễ), $m$ (biên lợi nhuận mỗi chuyến).
- Phụ lục: $L^{\mathrm{V}}$, $w$.

**Đã bỏ so với Danh mục cũ:** β, κ, ℓ (GLOSSARY mục H); $d$, $A$, $E$, $M$, $M^{+}$ (dạng đại lượng), $D^{+}$, $C$,
$X$, $V$ (dạng tổng), $\Omega$, $\Delta$, $k$ (số mũ khuếch đại): không còn trong các chương.

## 7. Chữ viết tắt và chương dùng lần đầu

| Chữ tắt | Lần đầu | Ghi chú |
|---|---|---|
| CH1–CH3 | Ch1 v4:147 | Nhãn câu hỏi nghiên cứu |
| DARP | Ch2 v6:29 | Định nghĩa tại chỗ |
| TLC | Ch2 v6:249 | Định nghĩa tại chỗ |
| JSON | Ch3:666 | Không định nghĩa tại chỗ |
| LF | Ch3:724 | Cũng ở Ch4B v11:399, Phụ lục:119 |
| NOAA | Ch4B v11:364 | **Không viết đầy đủ ở chương** |

**Đã bỏ:** ODRP, RTV, MPS, MRP, VOT, VOR, pp (GLOSSARY mục H); ILP (Ch2 v6 viết "quy hoạch nguyên (integer linear
program)", không dùng chữ tắt); ETA, SLA (không còn trong chương).
**Không đưa vào vì là tên riêng hay tên sản phẩm:** RideBound, FleetPy, OR-Tools, CP-SAT, C\#, .NET, MATSim, DeeprETA,
MOIA, UberX Share, TomTom, Mt-KaRRi.

## 8. Vấn đề thấy trong các chương (không sửa; ghi để xử lý khi ghép)

1. **Ch3, ký hiệu dùng trước khi định nghĩa.** $v$, $e$, $p$ (Ch3:175), $D$, $S$ (Ch3:182, 186), $x$, $c$, $z$, $L_r$
   (giả mã, Ch3:222) xuất hiện ở mục 3.1.3, trước mục bamoc (Ch3:244-256) và mục dubao. Đề xuất: thêm "ký hiệu ở
   mục~\ref{muc:bamoc}" vào chú thích Hình vongquyetdinh và tiêu đề Bảng luotquyetdinh.
2. **Ch3:194, $a$ trùng nghĩa.** Chú thích "$a \gets b$ nghĩa là gán $b$ cho $a$" dùng $a$, trong khi $a$ là giờ trả
   thực tế ở eq:so. Đề xuất: "dấu $\gets$ nghĩa là gán giá trị bên phải cho biến bên trái".
3. **Trùng ký hiệu giữa các chương** (đều được định nghĩa tại chỗ nên không sai, nhưng dễ nhầm): $k$ là yêu cầu (Ch2),
   xe (Ch3), chi phí mỗi lượt trễ (Ch4B); $c_{ij}$ là chi phí chuyến (Ch2) còn $c$ là phần dời do điều phối (Ch3);
   $m$ (Ch4B) và $m_i$ (Ch3); $T_i$ (Ch2) và $T$ (Ch4A); $i$, $j$ ở Ch2 và Ch3. Đề xuất nhẹ nhất: đổi $k$, $m$ ở phép
   hòa vốn của Ch4B sang hai ký hiệu chưa dùng ở Ch3; chủ nghiên cứu chọn tên.
4. **Ch4B v11:364, NOAA chưa viết đầy đủ** ở lần dùng đầu (STYLE quy tắc 12). Danh mục nay có NOAA.
5. **Phụ lục r31 v2:87, 92 dùng tên nội bộ** LOCKS, B1, C1 cạnh U, FREE, C-$B$. "C1" dễ lẫn với "luật C", "B1" với
   trần $B$. Danh mục không đưa các tên này vào.
6. **JSON (Ch3:666)** không được viết đầy đủ tại chỗ; Danh mục có.

## 9. Phép kiểm đã chạy

- Tìm cụm từ cấm (duy nhất, đầu tiên, tối ưu, vượt trội, đột phá, niêm phong, tiền đăng ký, dự đoán, mã băm, chúng
  tôi, quy trách, gây ra, chứng nhận, văn liệu, panel, kỷ nguyên, trôi dạt, ngân sách; tiếng Anh: preregist, sealed,
  predict, optimal, novel, unique) trên ba tệp `.tex`, kể cả dòng `%`: không còn chỗ nào (đã sửa một dòng `%` ở
  `04-viet-tat.tex` có "đầu tiên" và tên chữ tắt đã bỏ).
- "Em" chỉ có trong Lời cảm ơn; Tóm tắt và Danh mục không có.
- Lời cảm ơn không có số lần chạy, không có câu về các hướng đã bỏ; tên giảng viên là chỗ trống đúng chuỗi
  `[Tên giảng viên hướng dẫn — chờ bổ sung]`; không dùng "thầy" hay "cô" cho người hướng dẫn vì chưa biết.
- Mọi nhãn được tham chiếu đều có trong chương đang ghép: `muc:c1-cauhoi` (Ch1 v4:91), `eq:c2-chon` (Ch2 v6:50),
  `eq:chon`, `muc:bamoc`, `nx:giunguyen`, `bang:luat`, `muc:dubao`, `eq:keodan` (Ch3), `bang:c4-chiso` (Ch4A:185),
  `phuluc:C` (Phụ lục:60).
- Chưa dựng PDF (theo yêu cầu). Các gói cần (`longtable`, `booktabs`, `amsmath` cho `\eqref`) đã có trong `main.tex`.

## 10. Câu hỏi cho chủ nghiên cứu

1. **Tên giảng viên hướng dẫn.** Lời cảm ơn để `[Tên giảng viên hướng dẫn — chờ bổ sung]` (hai bìa cũng chờ, OUTLINE
   §1). Khi có tên, cho biết nên viết "thầy" hay "cô" và học hàm, học vị. Câu thứ hai của đoạn 1 tả loại góp ý nhận
   được (đặt mỗi con số cạnh câu hỏi và phép so của nó), phỏng theo bản cũ; xin xác nhận đúng với thực tế hoặc thay.
2. **Trang "Lời cam đoan".** Mẫu khóa luận của Trường Đại học Công nghệ có bắt buộc không (CHƯA KIỂM)? Nếu có, thêm 1
   trang. Tệp này không viết lời cam đoan vì đó là lời của chính sinh viên và phải ký.
3. **Bìa phụ.** DACN có hai bìa tiếng Việt (N-13). Mẫu khóa luận có cần bìa phụ không (CHƯA KIỂM)? Nếu có, thêm 1 trang.
4. **Khai báo dùng công cụ AI.** Trường, khoa hay giảng viên có yêu cầu nêu việc dùng công cụ AI khi viết, phân tích hay
   kiểm số không (CHƯA KIỂM)? Nếu có: đặt ở Lời cam đoan, một trang riêng hay Phụ lục C; và nên nói rõ phép "kiểm độc
   lập" ở Ch3 mục kiemtra và Ch4B mục hople do người hay do công cụ thực hiện (GLOSSARY F, dòng "kiểm tra độc lập").
5. **Ba kết quả trong Tóm tắt.** Giữ lựa chọn ở mục 3, hay đổi sang một trong ba câu thay thế (cộng dồn, trần 120 giây,
   +31/−5)?
6. **Dòng từ khóa.** Giữ như khuôn hiện tại hay bỏ như DACN (DACN không có từ khóa)?
7. **Hörl và Zwick trong Tóm tắt.** Đang nêu tên, không `\cite`, không năm. Giữ, thêm trích dẫn, hay bỏ tên?
8. **Tên danh mục.** Đề bài ghi "Danh mục ký hiệu và chữ viết tắt"; bản cũ ghi "Danh mục từ viết tắt và ký hiệu". Tên
   tệp giữ `04-viet-tat` nên `main.tex` không phải sửa.
9. **Trùng ký hiệu $k$, $m$ ở phép hòa vốn của Ch4B** (mục 8 ý 3): có đổi tên không?
