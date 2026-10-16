# Việc B: khung 7:00–9:00, chỉ tắc đường đo thật — báo cáo (THĂM DÒ)

- **Kế hoạch:** `W07-PLAN.md`, niêm phong 2026-09-29T14:32:27Z (`W07-PLAN.sha256`), trước mọi lần chạy trên ô w07.
- **Sửa đổi sau niêm phong:** `W07-AMENDMENTS.md` A1 (một lần đọc nguồn điện làm driver hoãn 72 job; đã chạy lại bằng
  `relaunch_until_done.py`, driver không đổi).
- **Chạy thử wrapper v1.2:** `../world/run_world_v12_smoke.py`, PASS (`../world/logs/v12-smoke-check-2026-09-29.txt`).
- **Chạy:** 88 job, 23:26 ngày 29/09 tới 04:07 ngày 30/09, cắm sạc, output `C:\RideBoundData\research\tier3-w07-v1\`.
  88/88 `status: pass`; mỗi job đúng một log và một thư mục output.
- **Phân tích:** `w07_analyze.py` → `analysis/full-2026-09-30-report.txt`, `-jobs.tsv`; gộp `w07_aggregate.py` →
  `analysis/aggregate-2026-09-30.txt`; chẩn đoán Q4 `w07_q4_rider.py` → `analysis/q4-rider-2026-09-30.txt`.
- 8 ô phát triển, mỗi ô một episode; 1 khách ≈ 0,9% một ô. Không có khoảng tin cậy.

## 1. Hợp lệ

- 0 vấn đề: audit v/e/p `ok` ở cả 88; mọi log có dòng `version=v1.2` và dòng kiểm ngày đúng ngày của ô; mọi mốc đổi đúng
  `bin × 900 s`; **mọi hệ số in ra khớp f(07:00 + b × 900 s)/f(07:00) của chính ngày của ô** (tính lại từ tệp hệ số); một hash
  kịch bản mỗi ô; một inventory `0da63eaf…4cbe`.
- Tất định: `C-30` ô 12/11 mẫu 1 trùng 718/718 quyết định với job chạy thử `v12-C-30-W5` (cùng cấu hình, khác nhãn).

## 2. Dự đoán đã niêm phong: 6/7 đúng

| # | Kết quả |
|---|---|
| Q1 | **Đúng.** 0/32 job `C-x` có quyết định non-normal |
| Q2 | **Đúng.** `Mplus-30` bị ép ở 8/8 ô |
| Q3 (chính) | **Đúng, mạnh hơn dự đoán.** Lời hứa `Mplus-60` bị phá ở **8/8** ô (dự đoán ≥ 4/8): 8,0 / 6,1 / 4,1 / 2,3% (12/11 mẫu 1–4) và 11,8 / 7,7 / 6,0 / 12,0% (13/11 mẫu 1–4); trung bình 7,3% |
| Q4 | **Sai.** `Mplus-300` không bị ép và không trễ quá 300 s ở 7/8 ô, không phải 8/8. Ở `d20181113-s10-r1-w07`, một khách trễ 307,3 s so với lời hứa đầu, ở cả `C-300` và `Mplus-300` (cùng chuyến đi); `Mplus-300` bị ép ở 13,6% quyết định của ô ấy |
| Q5 | **Đúng.** \|phục vụ `C-x` − `Mplus-x`\| ≤ 2 ở 8/8 ô với mọi x; chênh 0 ở 30, 60, 300 s và tối đa 1 ở 120 s |
| Q6 | **Đúng.** `V-30` bị ép ở 8/8 ô và phục vụ đúng như `C-30` ở 8/8 |
| Q7 | **Đúng.** `C-30` ≤ `U` ở 7/8 ô (ô 13/11 mẫu 3: 83 so với 82) |

## 3. Kết quả gộp trên 8 ô (864 yêu cầu; `analysis/aggregate-2026-09-30.txt`)

| x | Phục vụ `C` / `M⁺` | Lời hứa `M⁺` bị phá (A > x) | `C` chấm theo luật `M⁺` | Lời hứa `C` bị phá | `M⁺` bị ép | Cùng quyết định |
|---|---|---|---|---|---|---|
| 30 | 660 / 660 | 24,0% | 24,0% | 0% | 58,6% | 8/8 ô |
| 60 | 661 / 661 | 7,3% | 7,3% | 0% | 35,5% | 8/8 ô |
| 120 | 666 / 664 | 0,9% | 1,2% | 0% | 6,6% | 6/8 ô |
| 300 | 665 / 665 | 0,2% | 0,2% | 0% | 1,7% | 8/8 ô |

- `U` phục vụ 665. `V-30` và `M-30` phục vụ 660, cùng từng quyết định với `C-30` ở 8/8 ô.
- `V-30` phá lời hứa của chính nó (tổng độ dời khách thấy > 30 s) với 29,2% khách (18,1–44,1% tùy ô) và bị ép ở 63,2% quyết định.
- So với khung 8:00–10:00 cùng ngày 12/11 (phép quét): `M⁺` phá hứa 2,2% ở 30 s và 0% từ 60 s; khách trễ nhất 35,2 s.
  Ở 7:00–9:00, dưới `C-30`, khách trễ nhất 88–194 s tùy ô, và không khách nào đến sớm hơn lời hứa đầu quá 30 s.

## 4. Mô tả thêm sau khi xem (không phải dự đoán): khách làm Q4 sai

`analysis/q4-rider-2026-09-30.txt`, ô `d20181113-s10-r1-w07`:
- Dưới `C-300` (và `Mplus-300`, cùng chuyến đi), khách trễ nhất có A = 307,3 s = 99,1 s do tắc đường (tổng x) + 208,2 s do chính bộ
  điều phối (tổng c), trong phần 300 s mà cả hai luật cho phép. Tức lời hứa kiểu hạn chót bị phá vì điều phối tiêu gần hết phần
  cho phép, rồi tắc đường cộng thêm.
- Một khách khác trễ 227,5 s **chỉ** vì tắc đường (tổng c = 0).
- Dưới `C-30`, cùng ô, khách trễ nhất 99,1 s, gần như toàn bộ do tắc đường (97,1 s).
- Vậy cơ sở của Q4 ("trôi của mỗi khách cỡ tới 100 s") sai: trôi thật có thể tới gần 4 phút cho một khách có chuyến đi dài.

## 5. Đọc đúng tầm

- **Câu của luận văn cũ "trên tắc đường thật, từ 1 phút không luật nào phá lời hứa" chỉ đúng sau cao điểm.** Ở khung tắc tăng
  nhanh nhất, hạn chót 1 phút bị phá với 7,3% khách, ở cả 8 ô, trên dữ liệu thật hoàn toàn (không nhiễu tự tạo).
- **Hai luật vẫn chở đúng như nhau.** Khác biệt chỉ ở lời hứa: cùng những chuyến đi, luật hạn chót (và luật theo giờ khách thấy)
  hứa điều mà tắc đường làm cho không giữ được, và phải phục hồi ở 36–59% quyết định ở mức 30–60 s; luật `C` hứa phần do điều
  phối và giữ được theo cấu tạo. Đây cùng kết luận với phép quét và Việc A, nay trên dữ liệu thật.
- **Không được nói:** "`C` phục vụ nhiều hơn"; "0% phá hứa của `C`" như phát hiện; "xác nhận"; "trên mạng đường Manhattan".
- **Chỗ yếu:** 8 ô của 2 ngày (thứ Hai, thứ Ba), thuộc panel phát triển; mỗi ô trùng 7–15/108 khách với ô w08 đã xem; mỗi ô một
  episode; một dự đoán sai (Q4); sự cố nguồn điện A1 (không ảnh hưởng tới job nào đã chạy).

## 6. Kiểm độc lập (2026-09-30, `independent/RESULT.md`)

Một agent kiểm độc lập viết mã riêng, không dùng module nào của scratchpad, và tính lại 7 khẳng định từ 88 bản ghi thô.
Cả 182.917 khung dữ liệu khớp mã kiểm `frameSha256`. **7/7 khớp:**
1. 88/88 `pass`, cùng inventory; một hash kịch bản mỗi ô, 8 ô có 8 hash khác nhau.
2. Mọi log có đúng một dòng `version=v1.2` và một dòng kiểm ngày đúng; cả 803 dòng mốc có t = 900·b; hệ số in ra lệch tệp
   hệ số tối đa 0,00005.
3. Số khách phục vụ của cả 88 job khớp bảng.
4. 0 quyết định non-normal ở 32 job `C-x`; `Mplus-30` 268–498 và `V-30` 336–534 quyết định non-normal mỗi ô; `Mplus-300` 82
   quyết định ở ô 13/11 mẫu 1 và 0 ở các ô khác.
5. `Mplus-60` phá hứa 7/87, 5/82, 4/97, 2/87, 8/68, 5/65, 5/83, 11/92 khách, trung bình 0,0725; `Mplus-30` trung bình 0,2404;
   trễ lớn nhất dưới `C-30` 109,1 / 102,9 / 99,7 / 148,7 / 99,1 / 194,0 / 88,2 / 106,3 s.
6. `Mplus-x` cùng chuỗi hành động với `C-x` ở 8/8 ô với x = 30, 60, 300 và 6/8 với x = 120; `V-30` = `C-30` ở 8/8.
7. Ô 13/11 mẫu 1: khách trễ 307,313 s ở cả `C-300` và `Mplus-300`, và là khách duy nhất vượt 300 s.

Ghi chú của agent (không đổi kết luận nào): khách trễ 307 s cũng trễ đúng như vậy dưới `U`; `M-30` có số quyết định non-normal
bằng `Mplus-30` ở cả 8 ô và cùng chuỗi hành động với `C-30`; `Mplus-120` cũng bị ép ở 3 ô (12/11 mẫu 4, 13/11 mẫu 1 và 2);
trung bình 7,3% là làm tròn của 7,25%.
