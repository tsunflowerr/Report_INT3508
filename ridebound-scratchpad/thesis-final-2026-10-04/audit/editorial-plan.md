# Kế hoạch biên tập và sổ thuật ngữ

Đã đọc toàn bộ bản gốc trước khi biên tập. Bản PDF gốc có 105 trang. Bản gốc và toàn bộ dữ liệu nghiên cứu được giữ nguyên; bản làm việc nằm trong thư mục source cạnh hồ sơ này. Bản băm gốc ở original-hashes.csv.

Lập luận giữ lại: RideBound cung cấp sổ cái theo hành khách cho biến động do quyết định, chứng minh tính giữ được của phương án giữ tuyến dưới các giả thiết rõ ràng, và đo chi phí dịch vụ cùng giới hạn của lời hứa trong thực nghiệm ghép cặp nhỏ. Kết quả về hành vi không phải bảo đảm mọi biến động khách nhìn thấy, và không phải bằng chứng cải thiện hài lòng hay phúc lợi.

| RQ | Chương phương pháp | Bằng chứng chính |
|---|---|---|
| RQ1. Đại lượng nào có thể ghi sổ và kiểm trước quyết định? | Ba mốc, vector ngân sách, chứng cứ quyết định | Biên bản H6, kiểm mã và đối chiếu delta |
| RQ2. Kiểm soát biến động đánh đổi bao nhiêu dịch vụ? | Cổng cứng và các cấu hình cùng bộ sinh | H6 chính, thang ngân sách và cửa sổ phụ |
| RQ3. Trôi dạt và phục hồi thay đổi tính khả thi cùng ý nghĩa lời hứa ra sao? | Bốn họ cổng, giả thiết N/H, hai luật phục hồi | Tầng2 có niêm phong; W07/W07X phát triển; T38 thăm dò có chia tập |

| Thuật ngữ chuẩn | Định nghĩa và quy tắc |
|---|---|
| đi chung xe theo yêu cầu | on-demand ride-pooling; dùng tiếng Việt sau định nghĩa |
| ô thực nghiệm | một bộ ngày, mẫu nhu cầu, khung giờ; không gọi các lần quyết định là mẫu độc lập |
| phương án giữ tuyến | no-op; chiếu tuyến cũ trên cùng trạng thái hiện tại |
| phần thay đổi khi giữ tuyến | x=e-v; không đồng nhất với giao thông thuần hoặc nhiễu độc lập |
| phần do quyết định | c=p-e, độ lớn A=abs(c); phép đối chiếu trong mô hình, không ước lượng tác động nhân quả tổng thể |
| biến động nhìn thấy | z=p-v, độ lớn B=abs(z) |
| C, X, V | tổng A, abs(x), B trên cùng chuỗi công bố |
| M+ và M | cực đại muộn một chiều và lệch hai chiều so với lời hứa đầu |
| trần beta | giới hạn mỗi khách mỗi chiều, không lấy trung bình thay cho trần |
| quyết định có miễn trừ | non-normal; ghi vi phạm, không gọi đã giữ lời hứa gốc |
| điểm phần trăm | chênh tỉ lệ có cùng mẫu số; phân biệt phần trăm tương đối |

Quy trình Nature Writing áp dụng cho bản thảo thuật toán, đích khóa luận thông thường, các mục mở đầu/văn liệu/phương pháp/kết quả/thảo luận/kết luận; tiếng Việt theo yêu cầu người dùng. Figure tiếp tục workflow Python/matplotlib có sẵn, xuất vector, kiểm hình ở kích thước cuối. Không áp các hạn mức tạp chí Nature vào khóa luận.

Phân bổ dự kiến: front matter khoảng11; Ch1 khoảng5–6; Ch2 khoảng6–7; Ch3 khoảng14–15; Ch4 khoảng27–29; Ch5 khoảng4; references khoảng3–4. Điều chỉnh theo bản biên dịch, không thu nhỏ font/lề/giãn dòng.

Loại hoặc rút: lặp số liệu giữa Ch1/3/4/5; tương đồng luật nghĩa vụ chưa đủ nguồn; phép quy đổi total variation sang phúc lợi; mô hình độc lập hành khách (1-p)^n; sàn ±0.3pp không phải ngưỡng suy luận thống kê; lịch sử thử nghiệm không thay đổi kết luận. Giữ các kết quả âm và các giả thiết làm thay đổi cách đọc.

Hồ sơ trước phản biện gồm audit bằng chứng và trích dẫn. Ba reviewer cuối sẽ nhận cùng bản thảo đóng băng trong ba context mới, không đọc báo cáo của nhau.
