# Kiểm định tính mới của precision-deadline dispatch — 20/09/2026

## Quyết định

Có cơ sở vận hành và có thể xây prototype, nhưng CHƯA đủ bằng chứng để chọn thiết kế hiện tại làm đóng góp thuật toán mới. Không nên triển khai lớn trước khi vượt qua kiểm định dưới đây. Đánh giá này hạ mức ưu tiên của đề xuất trong HUONG-MO-RONG-CLAUDE-2026-09-20.md; tài liệu trước được giữ nguyên như snapshot lịch sử.

Không tìm được một bài đã xác nhận trùng toàn bộ đặc tả không đồng nghĩa chứng minh tính mới. Những thành phần quan trọng nhất đều có tiền lệ gần. Đây là lượt tìm kiếm có mục tiêu và truy vết tài liệu tham khảo, không phải systematic review đầy đủ hay chứng nhận novelty.

## Đặc tả đang kiểm định

Khi nhận khách, hứa khoảng giờ trả I0=[L0,U0], hạn công bố chính xác hơn tau=L0-h không được dời, và bề rộng cuối Wf. Đến tau phải công bố khoảng con của mọi khoảng đã hứa, rộng không quá Wf. Điều phối online giữ pickup lock, năng lực xe, thứ tự pickup-before-drop, trạng thái xe đang chạy và khả thi đồng thời của các khách đã nhận. Không hủy khách cũ để cứu cam kết; giữ một kế hoạch hoàn tất khả thi làm dự phòng. Chọn vị trí khoảng thu hẹp có thể dùng nhu cầu tương lai lấy mẫu.

## Công trình gần nhất và mức kiểm tra

### Çelik et al., 2026 — Is Waiting Worth It? The Value of Delaying Time Window Assignment in Vehicle Routing Problems

DOI: https://doi.org/10.1016/j.trb.2025.103381
Nguồn tác giả: https://research.tue.nl/en/publications/is-waiting-worth-it-the-value-of-delaying-time-window-assignment--2/
Preprint: https://research.tue.nl/files/343516638/ssrn-5004663_1_.pdf

Đã kiểm abstract nguồn trường đại học và đoạn mô hình preprint được máy tìm kiếm lập chỉ mục. Request đến trong giai đoạn đặt trước; nhà cung cấp chọn gán cửa sổ ngay hoặc trì hoãn trong giai đoạn đó. Cửa sổ đã truyền đạt không đổi; vi phạm khi phục vụ chịu phạt. Có rollout và multiple-scenario approach. Trùng mạnh với quyết định khi nào cam kết để đổi lấy linh hoạt định tuyến. Khác biệt còn lại cần kiểm ở final text: chưa xác nhận nghĩa vụ thu hẹp một khoảng đã công bố, deadline từng khách trong lúc xe đang chạy. Final PDF trả 403; thesis timeout. Không tuyên bố đã đọc toàn văn final hay xem ràng buộc mềm của preprint là đã kiểm trực tiếp bản cuối.

### Johnn et al., 2021 — The Home Service Assignment, Routing, and Appointment Scheduling (H-SARA) problem with Uncertainties

Primary preprint: https://optimization-online.org/wp-content/uploads/2021/07/8479.pdf

Đã tải PDF 21 trang, đọc thiết kế hai giai đoạn và §4.4, đặc biệt trang 15–16. Sau khi biết hủy lịch, thuật toán sửa tuyến và công bố cửa sổ hẹp hơn, có mục tiêu đặt trong cửa sổ ban đầu. Công thức phạt arrival nằm ngoài khoảng cũ; không được diễn giải là chứng minh containment cứng của toàn bộ cửa sổ mới. Trùng rõ ý rộng trước/hẹp sau và mục tiêu nesting; đây không phải phát minh của RideBound. Khác với admission online trong khi đang chuyên chở khách.

### Bekker, Bharti, Levering, Mandjes, 2026 — A framework for window design in delivery schedules

Primary preprint: https://arxiv.org/abs/2601.19601
HTML: https://arxiv.org/html/2601.19601v1

Đã tải PDF 26 trang, đọc phần mô hình liên quan và §6, Algorithm 1 trang 17–18. DWOS tính lại cửa sổ theo thông tin hành trình; truyền một lần khi thời gian tới đầu cửa sổ cập nhật nhỏ hơn/ngang ngưỡng T. Tuyến đã cho, chi phí cân bằng độ rộng và sai lệch. Cửa sổ có thể dịch chuyển; ngưỡng kích hoạt không phải bảo đảm báo trước ít nhất h hay hạn cố định neo vào khoảng ban đầu. Trùng cập nhật chính xác hơn và thời điểm truyền đạt; chưa trùng toàn bộ hợp đồng đề xuất. Là preprint, không gọi là bài đã phản biện.

### Paradiso, Roberti, Ulmer, 2025 — Lookahead scenario relaxation for dynamic time window assignment in service routing

DOI: https://doi.org/10.1016/j.trb.2024.103137
Primary full text: https://www.research.unipd.it/retrieve/7404cd4d-161a-4cd8-9577-ea1517147529/1-s2.0-S0191261524002613-main.pdf

Đã đọc abstract, introduction và phần liên quan của toàn văn qua web. Gán cửa sổ cứng cho request dịch vụ ngày hôm sau, chỉ nhận nếu tồn tại tuyến tôn trọng khách cũ; chọn cửa sổ bằng kịch bản tương lai và relaxation giải qua column generation. Trùng trực tiếp mục tiêu giữ khả năng nhận nhu cầu tương lai khi chọn cửa sổ. Không thể nhận novelty cho future-option window placement nói chung. Không xác nhận cơ chế thu hẹp bắt buộc trong lúc thực thi. Download cục bộ bị 403 dù văn bản web đọc được.

### Dalmeijer, Spliet, Wagelmans, 2019 — Dynamic Time Window Adjustment

Primary working paper: https://repub.eur.nl/pub/116533/EI2019-22.pdf

Đã đọc abstract và phần đầu mô hình qua web. Điều chỉnh cửa sổ động theo tiến độ tuyến và thời gian đi bất định, với các kiểu biến đổi và utility khách hàng. Tuyến cố định. Chặn claim rộng rằng dynamic window adjustment là mới; không dùng việc chỉ đọc đầu mô hình để khẳng định tất cả trường hợp bài này không xử lý.

### Yu, Shen, Badri Koohi, Seada, 2023 — Time window optimization for attended home service delivery under multiple sources of uncertainties

DOI: https://doi.org/10.1016/j.cor.2022.106045
Primary publisher: https://www.sciencedirect.com/science/article/pii/S0305054822002751

Đã kiểm abstract/introduction publisher. Kết hợp định tuyến và thiết kế cửa sổ với bất định, có cập nhật cho yêu cầu mới theo rolling horizon. Vì vậy chỉ chuyển từ static sang online joint routing/window optimization không đủ làm khác biệt. Chưa đọc toàn bộ ràng buộc cập nhật; không kết luận loại trừ bài này ở mức model.

## Kết luận về khả thi

1. Với thời gian đi xác định, giữ lịch dự phòng hoàn tất mọi khách có thể bảo đảm thu hẹp đúng hạn: đến hạn chọn khoảng con chứa giờ đến của lịch đó. Với điểm đến xác định và Wf>0 việc chọn khoảng luôn có thể làm nếu điểm nằm trong khoảng cũ. Chính sự đơn giản này làm chứng minh bảo toàn khả thi hiện tại yếu về đóng góp khoa học: nó chưa vượt xa nguyên tắc giữ incumbent khả thi.
2. Với arrival band [a,b], cần b-a<=Wf và tồn tại x thuộc [max(L,b-Wf),min(a,U-Wf)]. Nếu tập rỗng thì không thể thực hiện lời hứa. Bất định không bị chặn không cho phép hứa tuyệt đối một khoảng hữu hạn. Phải xác định rõ robust bounds hoặc mức xác suất; không được đổi giữa hai loại bảo đảm khi báo cáo.
3. Thu hẹp càng sớm/càng hẹp càng giảm khả năng nhận khách sau đó. Khách phải chấp nhận ít chính xác hơn trước hạn. Đó là chi phí dịch vụ thực, dù UI gửi ít thông báo hơn.
4. Probe trước chỉ thấy 3 cơ hội chèn dưới một hợp đồng giả định nới drop interval; chưa thực thi nghĩa vụ thu hẹp, chưa chứng minh tăng completed trips, và nới budget đơn giản có thể giải thích toàn bộ kết quả. Không dùng probe này làm bằng chứng novelty hoặc hiệu quả vòng kín.

## Phần còn có thể thành nghiên cứu

Ứng viên hẹp: điều phối pickup/drop online có nghĩa vụ thông tin cứng theo từng khách, trong khi tuyến đang thực thi, với admission bảo toàn khả thi đồng thời. Đây mới là giả thuyết khoảng trống; chưa là đóng góp đã được xác lập.

Muốn thành đóng góp phương pháp cần một kết quả mạnh hơn thêm ledger/timer hoặc ghép các thuật toán cũ, chẳng hạn điều kiện kiểm tra nhanh được chứng minh đúng cho một lớp bài toán rõ ràng, hoặc thuật toán rút ngắn đáng kể thời gian xử lý mà giữ cùng bảo đảm. Không gọi việc lấy interval sweep chuẩn và gán tên mới là thuật toán mới.

## Cổng quyết định trước triển khai lớn

- Định nghĩa model đủ chính xác để so sánh với sáu công trình trên; đối chiếu full model của Çelik final và Yu trước khi claim khoảng trống.
- Chứng minh một kết quả không tầm thường; giải thích vì sao hard-window routing cộng một timer không đã đủ cho phần kết quả đó.
- So với immediate narrow, fixed wide, simple deadline refinement, simple budget relaxation và lookahead window selection. Cùng phạm vi tìm tuyến, compute budget và điều kiện thực thi. Các policy không cùng chất lượng thông tin phải so trên đường đánh đổi thay vì chỉ acceptance.
- Đo completed service, vi phạm cam kết, tỷ lệ công bố đúng hạn, bề rộng theo thời gian, độ trễ quyết định p95 và chi phí. Có thể dùng diện tích bề rộng theo thời gian làm chỉ báo nghiên cứu, không đồng nhất với hài lòng người dùng đã được xác thực.
- Nếu thắng chỉ nhờ cửa sổ rộng hơn hoặc mất ưu thế trước baseline timer đơn giản, loại claim thuật toán mới. Nếu không có lợi ích ở cùng chất lượng cam kết, dừng nhánh thay vì mở rộng benchmark vô hạn.

## Phạm vi lượt search và provenance

Các cụm truy vấn: dynamic time window adjustment; window refinement advance notice; delayed time window assignment cutoff; nested time windows routing deadline; ride pooling time window notification; dial-a-ride time windows narrowing; ride-sharing commitment time windows refinement. Truy vết references từ Bekker et al. 2026 phát hiện Çelik, Dalmeijer, Yu và nhóm time-window assignment. Kết quả không liên quan và secondary summaries không dùng để xác lập novelty.

Local PDFs/extractions/download status trong novelty-audit-2026-09-20/. Tải/xuất text không đồng nghĩa đã đọc hết. Không sửa mã, không chạy benchmark mới, không đổi trạng thái work package của RideBound. Báo cáo này là quyết định nghiên cứu ngoài repo.
