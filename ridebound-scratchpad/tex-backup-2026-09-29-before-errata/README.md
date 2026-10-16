# Khóa luận tốt nghiệp — RideBound

**Lời hứa có biên được chứng nhận trong điều phối xe đi chung theo yêu cầu**

Trần Quang Thành — 23020155 — K68I-IT2. Viết bằng LaTeX (XeLaTeX), **66 trang A4**,
khoảng 28.000 từ.

## Build

Dùng chung `tools/tectonic.exe` của thư mục cha:

```powershell
cd E:\Code\Report_INT3508\ridebound
..\tools\tectonic.exe -X compile main.tex --outdir .
```

Kết quả: `main.pdf`.

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

Mọi con số trong chương 4 đều trích từ kết quả thực nghiệm đã niêm phong. Tổng cộng
**558 lần chạy, 33,62 GB**, phân bố như sau:

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

Các script phân tích nằm trong thư mục scratchpad của phiên làm việc, gồm:
`measure_instability.py` (9 thước đo), `extract_promise_movement.py` (bóc tách ba mốc),
`frontier_table.py` (bảng đường biên), `fielbaum_measure.py` (cài đặt thước đo của văn
liệu), `measure_window.py` (phân tích cửa sổ đón), `service_quality.py` (chất lượng dịch
vụ thực tế), `run_drift.py`, `run_drift_frac.py` và `preflight_drift.py` (thí nghiệm trôi dạt),
`run_surface.py` (mặt cong hai chiều).

## Chỗ cần điền thêm

Tìm chuỗi `[chờ bổ sung]` trong `noi-dung/00-bia.tex` để điền tên cán bộ hướng dẫn.

## Ghi chú về nội dung

Báo cáo trình bày cả những hướng đã thử và bị loại bỏ (mục 4.12) cùng phần ranh giới với
công trình gần nhất (mục 4.8, bảng 4.16). Đây là lựa chọn có chủ ý: phần trùng lặp với
Fielbaum & Alonso-Mora (2020) là đáng kể và được ghi rõ thay vì giấu đi.
