# Errata cho EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md (2026-10-12)

Tệp phụ lục 6 không được ghi đè, nên chỗ sửa ghi ở đây. Tôi kiểm lại bằng `grep -n` trên
`optimize/FORECAST-REPORT.md` (FR) sau khi đã tạo phụ lục 6 và bản `drafts/09-chuong4-phanB-v8.tex`.

| Dòng | Đang ghi | Đúng | Bằng chứng |
|---|---|---|---|
| N4B8-06, cột Anchor | FR:123 (15 ô Mplus-30F chạy xong) | **FR:124** | `grep -n "15 ô mà Mplus"` → dòng 124 |
| N4B8-06, cột Anchor | FR:137 (14 ô C-30F chạy xong) | **FR:138** | `grep -n "14 ô chạy xong"` → dòng 138 |

Các anchor FR khác trong phụ lục 6 đúng (FR:117 "K = 2"). Các dòng `% EV` của bản v8 có cùng lỗi lệch một dòng ở năm
chỗ (FR:123, 137, 156, 161-162, 165-169); bản `drafts/09-chuong4-phanB-v9.tex` sửa chúng thành FR:124, 138, 157,
170-171, 167-169 và thêm `factor_nowcast_screen.py:21-22` cho quy tắc ngày nguồn. Văn bản in ra của v9 giống hệt v8.
