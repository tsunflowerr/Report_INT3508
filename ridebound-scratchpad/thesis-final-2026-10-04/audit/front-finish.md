# Kiểm phần đầu và tài liệu tham khảo

Ngày biên tập: 04/10/2026. Chỉ sửa `02-tom-tat.tex`, `04-viet-tat.tex`,
`10-tai-lieu.tex` trong bản làm việc. Đã đọc bản gốc của ba tệp; bản gốc được giữ.
Đã đọc Chương 1, 2, 3, 5, phần thiết lập/H6 mới và audit văn liệu trước khi viết.

## Tóm tắt

Đếm theo đơn vị ngăn bởi khoảng trắng trong thân bài, bỏ tiêu đề và dòng từ khóa;
biểu thức toán giữ như trong TeX: tiếng Việt **768 → 393**, tiếng Anh **591 → 274**.
Tiếng Việt nằm trong mục tiêu 250–400 đơn vị. Đây không phải bộ tách từ tiếng Việt.
Giữ bản dịch tiếng Anh vì mẫu gốc đã có bản dịch.

Tóm tắt đi theo chuỗi vấn đề → cơ chế → kết quả âm H6 → giới hạn → ý nghĩa thiết kế.
Chỉ giữ các số xác định kết luận chính: 89,06% → 1,37%, 7,13 điểm phần trăm,
và trần cấu hình 30 giây. Không liệt kê tổng lượt chạy, dung lượng, số dòng mã hoặc
số kiểm thử. Chưa gán lợi ích hài lòng, phúc lợi, tác động nhân quả hay giờ đến thực tế.

| Phát biểu | Bằng chứng trong bản làm việc | Phạm vi |
|---|---|---|
| Hạch toán ba mốc và sổ cái theo khách | Chương 3, định nghĩa ba mốc và sổ cái | Chênh phương án tại cùng trạng thái; không nhận diện tác động nhân quả thuần |
| Cổng hành vi giữ tuyến | Định lý giữ tuyến/bốn họ cổng | Ngân sách trước hợp lệ và tuyến giữ nguyên qua các kiểm tra khác |
| Tỉ số 89,06% → 1,37% | Bảng `bang:quytrach` trong `08-thietlap-va-h6.tex` | Tỉ số hai tổng trên panel chính; không phải phân rã nhân quả |
| Chi phí 7,13 điểm; H6 không đạt | Phần RQ2/tiêu chí H6 | Cả gói C1, không chỉ trần giờ trả |
| Biên nhìn thấy cần dự phòng | Chương 3 và T38 | Có điều kiện; phụ thuộc nhóm và chuyến nguồn giao nhau, không bảo đảm xác suất quần thể |

## Thuật ngữ và ký hiệu

| Dạng khóa | Ý nghĩa | Phân biệt đã giữ |
|---|---|---|
| `v`, `e`, `p` | Lời hứa trước, phép chiếu giữ tuyến, lời hứa đề xuất | `e` không là tác động thuần của giao thông |
| `C`, `X`, `V` | Tổng hành vi, tổng thay đổi giữ tuyến, tổng nhìn thấy | `V` ở mô hình gán Chương 2 còn là tập xe; quy ước được ghi rõ |
| `M+`, `M` | Muộn cực đại, độ lệch hai chiều cực đại | Khác tổng biến thiên qua toàn chuỗi |
| H6, T38 | Phép so chính và phép kiểm thăm dò cuối | Không nâng T38 thành xác nhận quần thể |

Danh mục được nén thành hai bảng, giữ cỡ chữ kế thừa. Bỏ các mục không dùng trong thân
bài: ODRP, VRP, RTV, ILP, MRP, MPS, SLA, VOT, VOR. Bổ sung NDJSON, SHA-256,
RQ, B1/C1/U và ký hiệu ngưỡng T38. Mục tiêu không quá hai trang phải được xác nhận
trên bản PDF cuối, không suy từ mã TeX.

## Tài liệu tham khảo và toàn vẹn trích dẫn

Nhập bản ghi đã xác minh từ `audit/corrected-bibliography.tex`, giữ **23 mục** đang dùng
hoặc được người biên tập chính xác nhận sẽ dùng. Chuẩn hóa khóa conformal thành
`angelopoulos2023` theo yêu cầu; DOI 10.1561/2200000101. Bỏ 10 mục chưa được trích:
`toth2014`, `groer2009`, `blackburn1986`, `agatz2012`, `ortools`, `li2025`,
`zalesak2025`, `agarwal2019`, `chen2018`, `borodin1992`.

Không có khóa mục tài liệu trùng. Dùng tiêu đề tự sinh của `thebibliography` với
`bibname` đã đặt ở `main.tex`, bỏ `chapter*` lặp; có đúng một lệnh đưa vào mục lục.

Kiểm regex toàn bộ TeX lúc hoàn tất tệp này: 22 khóa trích dẫn đang hiện diện, 23 khóa
tài liệu. Hai điểm phối hợp đã báo cho người biên tập chính:

- `08-thietlap-va-h6.tex` dùng `nyctlc`, cần đổi thành khóa đã xác minh `tlc`.
- `angelopoulos2023` đã có trong danh mục và sẽ được người biên tập chính thêm vào T38.

Sau hai chỉnh sửa đó, danh mục dự kiến không thiếu mục và không có mục chưa trích.
Chưa tuyên bố đã biên dịch hoặc kiểm hình thức PDF; bước này do đợt QA bản tổng hợp
thực hiện. Không có thay đổi mã RideBound trong tiểu tác vụ này.
