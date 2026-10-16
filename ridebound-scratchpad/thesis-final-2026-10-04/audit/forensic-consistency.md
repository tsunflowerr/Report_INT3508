# Kiểm tra nhất quán sau phản biện độc lập

Ngày 2026-10-05. Ba báo cáo đã đóng băng trước lượt kiểm này; SHA-256 được kiểm lại và lưu trong `reviews/frozen-reports.json`. Đây là lớp kiểm biên tập theo Nature Reviewer `forensic-consistency-audit.md`, không phải phản biện thứ tư và không tạo đồng thuận giả. Không sửa hoặc đưa kết quả này ngược vào các báo cáo độc lập.

`final_forensic.py` đọc dữ liệu đã kiểm và thực hiện 123 phép kiểm tất định: tổng từng ô H6, tỉ số hai tổng, chi phí phục vụ theo hai cửa sổ, tổng từng nhánh T38, trung bình không trọng số và tỉ lệ gộp, ngưỡng hiệu chỉnh, hai loại độ phủ, độ vượt 233 ms, giao nhau nguồn, trung bình W07, số dự đoán mạnh tầng 2 và băm báo cáo. Tất cả qua. Script không chạy lại mô phỏng. Kết quả chi tiết, nguồn, đơn vị, giá trị và kỳ vọng nằm trong `forensic-consistency.json`.

| Mã | Trạng thái và phép kiểm | Kết quả, tác động và cách xử lý | Trùng phản biện |
|---|---|---|---|
| AUD-01 | passed; H6 tổng 20 ô và tỉ số gộp | 89,0600% và 1,3718%; giảm 154/2160 = 7,1296 điểm phần trăm. H6 FAIL theo tiêu chí một điểm được giữ trong tóm tắt, kết quả và kết luận. | Không tạo concern; ba báo cáo đều nhận giới hạn đã công bố |
| AUD-02 | passed; trung bình ô so với tỉ lệ gộp | W07 24,04%/7,25% là trung bình tám ô. T38 M+-30 14,48% theo 34 ô khác 289/2338 = 12,36% theo khách. Không đổi mẫu số. | Các báo cáo đã kiểm giới hạn đơn vị |
| AUD-03 | passed; biên và độ phủ | k=15, gamma=222.259 ms; beta+gamma=252.259 ms. Điểm phủ 32/34, biên nhìn thấy thực 33/34. Chỉ một ô vượt biên thực 233 ms. Không gọi 94,1% là bảo đảm quần thể. | Giới hạn đã công bố |
| AUD-04 | passed; nguồn và phụ thuộc | 75 chuyến nguồn chung, cộng theo năm ngày 29+9+13+12+12. Chia nhãn nhóm không bảo đảm độc lập. Chẩn đoán cũ 43 dòng địa phương là định danh sai, không được trích. | Giới hạn đã công bố |
| AUD-05 | aggregation_ambiguity, corrected; 56 lượt C | Đơn vị gọi “ô” trước sửa gộp 20 tĩnh+20 biến thiên trên cùng đầu vào+16 phát triển. Sửa thành 56 lần chạy, giữ 0 dừng cam kết và 14 dừng vật lý. | Reviewer B, R2-m2; không đồng thuận đa reviewer |
| AUD-06 | provenance_gap, addressed by method revision | Cổng không đủ mô tả bộ chọn. Kiểm mã thực và cấu hình đã ghim để bổ sung thứ tự mục tiêu, phép gộp, phá hòa, chi phí và tham số đầu vào. Không suy từ tên trường hay nhận mã hiện tại là runner lịch sử. | Đồng thuận A/B/C trên M1 |
| AUD-07 | passed; phạm vi kiểm toàn vẹn | 185 điểm kiểm tra cuối và 382.006 độ dời giờ trả T38. Không nhận mọi khung T38 đã được băm; W07X có phạm vi kiểm riêng. Băm không tạo mẫu mới hay chứng minh chương trình đúng hình thức. | Giới hạn đã công bố |
| AUD-08 | unresolved_input_needed; bìa | Tên và học hàm người hướng dẫn chưa được tác giả cung cấp. Giữ chỗ rõ ràng, không đoán tên. Cần điền trước nộp chính thức; không ảnh hưởng kết quả khoa học. | Đồng thuận A/C, R1-m3/R3-m4 |

Các phép so nguyên tắc, phép dựng phản ví dụ và bất đẳng thức được đọc riêng ở Chương 3. Tam giác nghiêm A+d>B không tự chứng minh A>B; không dùng số hàng tam giác nghiêm làm số vi phạm giả thiết H. H phải được nhận là điều kiện chưa kiểm trên toàn bộ quỹ đạo, không phải sự kiện đã chứng minh đúng hoặc sai ở mọi quỹ đạo thực nghiệm.

Lượt kiểm cuối quét mọi token số trong toàn PDF vào `all-numbers-final-pdf.csv`. Bảng `numerical-consistency.csv` và JSON cùng tên ánh xạ từng thước đo trung tâm tới tất cả vị trí xuất hiện cùng ngữ cảnh trang; số trong ví dụ dựng, trích văn liệu, tỉ lệ gộp và trung bình ô được đọc theo định nghĩa riêng. Các tham số phát triển không được nâng thành ngưỡng vận hành đã xác nhận.

Không thêm kiểm định, p-value, khoảng suy luận quần thể hoặc dữ liệu mới. Không có mâu thuẫn số học trung tâm còn tồn tại; hạn chế phụ thuộc nguồn, phạm vi mô phỏng và thông tin bìa được giữ minh bạch.
