# Khóa luận tốt nghiệp — RideBound

**Lời hứa có biên được chứng nhận trong điều phối xe đi chung theo yêu cầu**

Trần Quang Thành — 23020155 — K68I-IT2. Viết bằng LaTeX (XeLaTeX), **102 trang A4** (build
2026-09-29). Số từ chưa đếm lại sau các lần sửa.

## Build

Dùng chung `tools/tectonic.exe` của thư mục cha:

```powershell
cd E:\Code\Report_INT3508\ridebound
..\tools\tectonic.exe -X compile main.tex --outdir . --keep-logs
```

Kết quả: `main.pdf`. Phải có `--keep-logs`: thiếu cờ này thì `main.log` cũ không được ghi lại, và
có thể che lỗi tràn lề. Sau khi build, kiểm thời điểm của `main.log`, và kiểm log không có
`Overfull` hay `undefined`.

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `main.tex` | Khung tài liệu: font, lề, định dạng chương, môi trường định lý |
| `noi-dung/00-bia.tex` | Trang bìa tiếng Việt và tiếng Anh |
| `noi-dung/01-loi-cam-on.tex` | Lời cảm ơn |
| `noi-dung/02-tom-tat.tex` | Tóm tắt + Abstract |
| `noi-dung/03-muc-luc.tex` | Mục lục, danh sách hình, danh sách bảng (tự sinh) |
| `noi-dung/04-viet-tat.tex` | Danh mục từ viết tắt và ký hiệu |
| `noi-dung/05-chuong1.tex` | Chương 1 — Đặt vấn đề |
| `noi-dung/06-chuong2.tex` | Chương 2 — Cơ sở lý thuyết |
| `noi-dung/07-chuong3.tex` | Chương 3 — Lời hứa có biên được chứng nhận (phương pháp) |
| `noi-dung/08-chuong4.tex` | Chương 4 — Thực nghiệm và đánh giá |
| `noi-dung/09-chuong5.tex` | Chương 5 — Kết luận |
| `noi-dung/10-tai-lieu.tex` | Tài liệu tham khảo |
| `hinh/` | Logo trường |

## Nguồn số liệu

Tổng cộng **1.104 lần chạy được phân tích, 68,08 GiB** (bảng `bang:quymo` của chương 4, cùng quy ước
đếm). Phần trước kế hoạch là **558 lần chạy, 33,62 GiB** trên panel đã niêm phong, phân bố như sau:

| Đợt | Lần chạy | Thư mục kết quả |
|---|---:|---|
| Panel niêm phong (B1, C1) | 60 | `E:/RideBoundData/wp9/confirmatory-h6-panela-v2` |
| Đường biên 9 cấu hình | 141 | `E:/RideBoundData/wp9/frontier-v1` |
| Cơ sở kết quả | 44 | `E:/RideBoundData/wp9/exploratory-visible-*` |
| Thí nghiệm ratchet | 80 | `E:/RideBoundData/wp14/ratchet-secondary-v1` |
| Trần cửa sổ đón | 40 | `E:/RideBoundData/wp14/wide-window-v1` |
| Trôi dạt (cửa sổ 600 s) | 46 | `E:/RideBoundData/wp14/drift-v1` |
| Trôi dạt (cửa sổ 900 s) | 15 | `E:/RideBoundData/wp14/driftwide-v1` |
| Trôi dạt mức phân số k=0,5 | 12 | `E:/RideBoundData/wp14/drift-frac-v1` |
| Mặt cong hai chiều | 80 | `E:/RideBoundData/wp14/surface-v1` |
| Đặt trước ngân sách (mức C) | 20 | `E:/RideBoundData/wp14/levelc-v1` |
| Bộ sinh biết sắp xếp lại (b4) | 20 | `E:/RideBoundData/wp9/exploratory-b4-repair-v1` |

Phần thăm dò sau kế hoạch (546 lần chạy, 34,46 GiB), đếm bằng
`ridebound-scratchpad/tang3/inventory/inventory_runs.py` (log `inventory-2026-09-29.txt`):

| Đợt | Lần chạy | Thư mục kết quả |
|---|---:|---|
| Bốn họ cổng có tiền đăng ký (Tầng 2) | 296, thêm 5 chạy lại | `E:/RideBoundData/research/deadline-v1` |
| Thí điểm của phép quét (T3.7) | 60 | `E:/RideBoundData/research/tier3-pilot-v1` |
| Quét mức lời hứa C/M⁺ | 156, thêm 12 chạy lại | `E:/RideBoundData/research/tier3-sweep-v1` |
| Luật phục hồi (b) | 28 | `C:/RideBoundData/research/tier3-sweep-noworse-v1` |
| Kiểm thế giới tắc đường | 2 + 4 | `E:/RideBoundData/research/tier3-world-smoke-v1`, `tier3-world-v11-smoke` |

Script và báo cáo của phần này nằm ở `ridebound-scratchpad/deadline/` và `ridebound-scratchpad/tang3/`.

Các script phân tích nằm trong thư mục scratchpad của phiên làm việc, gồm:
`measure_instability.py` (9 thước đo), `extract_promise_movement.py` (bóc tách ba mốc),
`frontier_table.py` (bảng đường biên), `fielbaum_measure.py` (cài đặt thước đo của văn
liệu), `measure_window.py` (phân tích cửa sổ đón), `service_quality.py` (chất lượng dịch
vụ thực tế), `run_drift.py`, `run_drift_frac.py` và `preflight_drift.py` (thí nghiệm trôi dạt),
`run_surface.py` (mặt cong hai chiều).

## Chỗ cần điền thêm

Tìm chuỗi `[chờ bổ sung]` trong `noi-dung/00-bia.tex` để điền tên cán bộ hướng dẫn.

## Ghi chú về nội dung

Báo cáo trình bày cả những hướng đã thử và bị loại bỏ (mục 4.15) cùng phần ranh giới với
công trình gần nhất (mục 4.11, bảng 4.34; số mục theo build 2026-09-29). Đây là lựa chọn có chủ ý: phần trùng lặp với
Fielbaum & Alonso-Mora (2020) là đáng kể và được ghi rõ thay vì giấu đi.
