# Luận văn Phạm Xuân Bách 2024: đối chiếu sau khi đọc đủ

Đã đọc text đủ65 trang PDF, gồm phụ lục cơ sở dữ liệu. Đã xem ảnh các trang25,30,36,42,47–49. Số trang dưới đây là trang PDF.

## Điều có thể kế thừa ở mức ý tưởng

Prophet có nguồn gốc từ Tong et al.2018/2022 (tham khảo9–10). Tiền xử lý các yêu cầu dự đoán thành tuyến hướng dẫn, rồi chèn yêu cầu thực; các stop giả định không chiếm ghế và deadline được nới vô hạn trong giai đoạn online (trang33). Tận dụng waiting slack, dùng bảng khoảng cách tra cứu và phép quét tuyến tính đã là prior art. Prune Prophet thêm giới hạn đầu/cuối vị trí chèn bằng tìm kiếm nhị phân (trang42); tác giả nói rõ cắt tỉa tham lam có thể mất tối ưu.

## Giới hạn cần giữ khi so sánh

- Dự đoán được tạo từ một phần yêu cầu ban đầu (trang22,45), không có đánh giá mô hình forecast độc lập. Tỷ lệ25% là điều kiện mô phỏng được đặt, không chứng minh chất lượng dự báo triển khai.
- Mô hình có deadline và capacity, nhưng không có cumulative commitment ledger, lifecycle-specific freeze hay active-leg contract như RideBound. Bằng chứng O(n) của mô hình đơn giản không chuyển nguyên sang core hiện tại.
- Basic feasibility pseudocode trang25 dùng `expected < late -> false`, trong khi phần giải thích nói loại arrival quá trễ. Linear/Prophet trang30/36 cập nhật best ở trường hợp i=j mà không in điều kiện feasibility. Đây là mâu thuẫn/thiếu sót của bản trình bày; chưa đọc implementation tương ứng nên không kết luận code sai.
- Binary search theo deadline từng stop cần tính đơn điệu; deadline gốc nói chung không đơn điệu theo thứ tự route. Deadline prefix/suffix đã chuẩn hóa có thể tạo điều kiện khác, nhưng không được tự gán nó cho pseudocode. Không dùng Prune Prophet làm exact comparator nếu chưa kiểm định với exhaustive insertion.
- Trang48, biểu đồ ở50 yêu cầu cho Prophet10 xe, Basic17, Linear19; prose viết9 xe và Linear17. Ở100 yêu cầu hình cho Prophet19, prose18. Trục số xe tới21 dù đề mục nói tối đa20. Nên dùng raw output nếu muốn số chính xác, không trộn prose và figure.
- Figure4.8 trang49 ghi đơn vị giây nhưng ordinate tới240,000. Chưa xác minh đó là giây, mili giây hay tổng thời gian khác. Không chuyển thành latency claim.
- Non-sharing mỗi request một phương tiện không phải đối chứng đội taxi tái sử dụng xe tuần tự. Vì vậy18 xe/100 yêu cầu không tự chứng minh giảm82% fleet so với dịch vụ gọi xe hiện hành.

Kết luận cho thiết kế: dùng Prophet/Prune Prophet để xác định thuật toán đã có và điều kiện của chúng; không mượn số cải thiện hoặc tính tối ưu chưa xác minh. So sánh RideBound nên dùng cùng stream, travel model, fleet, service limits và causal information.
