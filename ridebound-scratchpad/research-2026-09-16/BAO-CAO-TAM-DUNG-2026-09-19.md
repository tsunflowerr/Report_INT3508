# RideBound — báo cáo phân tích và mốc tạm dừng 19/09/2026

Tạm dừng theo yêu cầu người dùng để chờ có thêm token. Chưa đạt mục tiêu tìm được một thuật toán khác biệt có bằng chứng cải thiện. Các kết quả dưới đây đã làm rõ đối thủ, sửa một số suy luận và loại bớt hướng đầu tư yếu. Chưa chạy một phương pháp mới trong closed-loop để chứng minh tăng phục vụ.

## 1. Đã đọc và kiểm tra đến đâu

- Đã đọc toàn bộ `E:\Code\Report_INT3508\RIDEBOUND-BAN-GIAO-CONTEXT.md`.
- Đã đọc văn bản toàn bộ 13 PDF gốc trong `C:\PDF\Paper`, tổng 324 trang, kể cả phụ lục. Đã kiểm tra hình/bảng/thuật toán được chọn; không tuyên bố đã kiểm hình từng trang.
- Có 195 file trong phạm vi docs đã lập inventory. Bản đọc đã loại các đoạn trùng hoàn toàn nhưng giữ ánh xạ về dòng nguồn. Đã đọc liên tục chunk 001–041/175, bao gồm toàn bộ tài liệu gốc 00–22 và một phần JSON bằng chứng. Đây không phải tỷ lệ số file đã đọc; còn 134 chunk trong chuỗi, ngoài các tài liệu đã đọc riêng trước đó. Chưa đọc hết docs.
- Đã đối chiếu các đường thuật toán liên quan: sinh candidate, physical validator, hard commitment/ledger, C1 objective, lựa chọn fleet, codec/reducer/Runner. Chưa tuyên bố audit toàn bộ mã nguồn.
- Đã tự phân tích 80 run cũ; kiểm toàn bộ 4.285 epoch có pending trong 40 run E1 panel A bằng duyệt fleet assignment.
- Đã đọc thêm GTS 2012, prompt-confirmation 2026, toàn văn HTML anticipatory routing 2022, toàn văn PDF shareability shadows 2026. Đến lúc dừng, đã đọc đủ văn bản 35 trang multiple-plan DARP 2025 từ PDF cũ có SHA khớp inventory. Tám trang đã render nhưng CHƯA xem ảnh trong đợt này; không ghi chúng là đã visual-QA.

## 2. Đối thủ gần nhất và ranh giới khác biệt

**Elmi, Moylan, Alonso-Mora & Fielbaum (2026), Improving ridepooling reliability using shareability shadows**, DOI [10.1016/j.trc.2026.105897](https://doi.org/10.1016/j.trc.2026.105897), là va chạm trực tiếp đáng kể. Bài đã chọn một nhóm hành khách để bảo đảm không tăng thời gian dự báo, dựa trên khả năng còn ghép thêm chuyến. Do đó, chỉ thêm score shareability rồi bảo vệ chọn lọc chưa tạo ra khác biệt mới.

Trong so sánh của chính bài, tỷ lệ bị từ chối gần nhau (29,09% và 29,21%); tỷ lệ khách bị tăng dự báo tổng delay giảm từ 63,17% xuống 15,39%. Nhưng ở nhóm thực sự bị tăng, mức tăng trung bình từ 0,84 lên 3,74 phút và số lần tăng trung bình từ 1,05 lên 1,80. Đây là phân phối lại gánh nặng đáng nghiên cứu, không phải mọi khách cùng tốt hơn. Tác giả đã nêu equity, magnitude và repeated updates trong hướng tiếp theo; không được nhận riêng việc chỉ ra các điểm đó làm novelty. Không so trực tiếp các tỷ lệ này với RideBound vì khác dữ liệu, hợp đồng và vận hành.

**Ackermann & Rieck (2025), Multiple plan approach for a dynamic dial-a-ride problem**, DOI [10.1007/s00291-025-00809-y](https://doi.org/10.1007/s00291-025-00809-y), đã có pool nhiều kế hoạch, bảo toàn tương thích với hành động đã thực hiện, time-based consensus, repair, các score slack, dự báo và độ phủ có xét chồng lấn giữa xe. Bài báo cáo hai extension dự báo/coverage không cải thiện MPA; coverage đắt hơn hơn 100 lần so với distance evaluation trong implementation của họ. Không suy ra mọi dự báo vô ích, nhưng không thể gọi các tên cơ chế này là mới.

Đọc toàn văn còn cho thấy: early-visits chỉ có lợi khi kết hợp phù hợp với scheduling; modified dynamic wait làm thay đổi kết quả mạnh. Dữ liệu bài là Euclidean tổng hợp, nhiều chuyến đặt trước 30–90 phút, khác RideBound. Repair mạnh hơn hoặc tối ưu distance lâu hơn đôi khi làm tổng phục vụ xấu hơn. Vì vậy, mở rộng tập lựa chọn tại cùng state không tự bảo đảm tốt hơn trong cả quá trình online.

Schulz–Pfeiffer 2026 đã có future potential và precomputed reinsertion; GTS 2012 đã có conflict-guided repair; anticipatory routing 2022 và prompt-confirmation 2026 đã có nhu cầu giả định/học giá trị tương lai. Generic lookahead, repair, RL, least commitment hoặc giới hạn ETA không đủ làm đóng góp mới.

## 3. Ba kết quả quan trọng về RideBound hiện tại

### Cơ sở toán học trong bàn giao cần sửa

Với `A=|p-e|`, `d=|e-v|`, `B=|p-v|`, tổng quát chỉ có `|A-d| ≤ B ≤ A+d`. Đẳng thức `B=A+d` cần hai biến thiên cùng chiều. Đã tìm thấy phản ví dụ ngay trong transcript: 20 run H6 B1 có tổng `A+d-B=58.172 ms` và 255 tọa độ publication có `B<A`. Chênh nhỏ sau tổng hợp không biến đẳng thức thành định lý. Docs/04 đã có cảnh báo đúng; vấn đề nằm ở diễn giải bàn giao và các hệ quả suy quá rộng.

### C1 vẫn có lựa chọn, nhưng một tầng objective không phân biệt được chúng

Trong E1 panel A, C1 có 1.045/1.571 epoch đang nhận được khách có nhiều fleet assignment cùng acceptance tối đa, khoảng 66,5%. Không gian thay ranking thực sự tồn tại; không phải đa số quyết định nhận khách chỉ có no-op.

Tuy nhiên, ở 2.123 epoch có objective worst utilization, giá trị fleet max là hằng số giữa các assignment tối đa acceptance. Nguyên nhân: hard limit 0/usage 0 đóng góp 1.000.000 ppm. Docs/18 ghi đây là quyết định implementation có chủ ý; docs/07 mô tả khác. Vì vậy không thể giải thích kết quả hiện tại bằng việc C1 đang sử dụng tốt một ranking reserve liên tục. Thử cách chuẩn hóa khác là đối chứng cần có, nhưng chưa đủ thành thuật toán mới.

### Chưa có bằng chứng rằng giữ reserve/coverage sẽ tăng phục vụ

Fixture nhỏ qua core gốc chứng minh hai tuyến cùng cost và tổng ETA usage vẫn có future feasibility khác nhau: 9/80 fixture có cặp như vậy. Đây là witness cho hạn chế của hai scalar, không phải bằng chứng hiệu quả thực tế.

Khi chuyển sang 20 state thật, dùng tối đa 12 loại OD/service từ lịch sử trước quyết định và 69 accepting assignments: union coverage chỉ phân biệt 1/16 epoch đủ điều kiện; C1 đã chọn tốt nhất. Score matching từng cặp mẫu phân biệt 3 epoch, C1 cũng đã tốt nhất cả 3. Chưa có state nào chứng minh score mới tốt hơn C1 trong phép thử này. Mẫu nhỏ, lấy từ đầu một run, cùng physical time; chưa bác bỏ mọi lookahead.

## 4. Kết quả âm mạnh nhất: repair tại thời điểm bị từ chối

Đã replay một run bằng đúng Runner E1, khớp 750 phản hồi canonical byte-exact và lấy đủ 16 state bị từ chối. Repair một waiting pair không cứu được state nào. Sau đó mở rộng duyệt toàn bộ hoán vị suffix khách cũ và mọi vị trí chèn pickup/drop khách mới trên từng xe; suffix thực dài tối đa 4 stop.

- 4.153 route được xét.
- Chỉ 9 route qua vật lý; cả 9 vẫn giữ thứ tự khách cũ.
- Không route nào qua toàn bộ hợp đồng.
- 7 candidate-level budget witnesses đều có ngân sách đã tiêu trước đó bằng 0; lần chèn đòi thêm khoảng 72–258 giây, vượt trần 30 giây. Hai witness còn lại là phase lock khi pickup trễ thêm.

Vì thế, trên các state và route family này, “tìm thứ tự kỹ hơn” hoặc “tiết kiệm ngân sách trước đó” không giải quyết được blocker đã quan sát. Đây không phải 7 khách riêng biệt, không phải chứng minh DARP vô nghiệm, không bao gồm đổi xe, thay quyết định quá khứ hay tối ưu mọi lịch chờ. Không nên đầu tư một ma trận lớn cho repair này khi chưa có positive witness ở operating point khác.

## 5. Hướng còn mở — chưa phải khuyến nghị triển khai

Hướng còn có lý do để kiểm tra là **chọn quyết định sớm sao cho giữ được khả năng phục vụ tương lai dưới cam kết đã mở**, đồng thời kiểm soát việc dồn biến động lên một nhóm hành khách. Muốn thành đóng góp, cần một phương pháp cụ thể và bằng chứng vượt đối chứng mạnh; không chỉ đổi metric, thêm tên RL hoặc nới hợp đồng.

Hướng này đang yếu ở bằng chứng thực nghiệm: score đơn giản đã thử chưa vượt C1. Nếu tiếp tục, trước hết phải tìm được trường hợp dữ liệu phát triển mà quyết định thay thế có giá trị thực; nếu không có, dừng hướng đó. Một hướng contract khác cần mô tả rõ lợi ích nào được mua bằng việc thay lời hứa nào; không gọi đó là tăng hiệu quả miễn phí.

## 6. Mốc tiếp tục và bảo toàn

1. Tiếp tục docs từ `docs-reading/chunk-042.txt`; không đọc lại các đoạn đã ghi nhận chỉ vì đổi phiên.
2. Hoàn tất kiểm ảnh multiple-plan PDF đã render tại `renders/16-page-{11,14,16,21,24,28,29,30}.png`; đặc biệt Eq.(1), pseudocode và bảng kết quả. Text Eq.(1) có dấu hiệu không khớp diễn giải, chưa kết luận khi chưa nhìn ảnh.
3. Hoàn tất những nguồn gần còn thiếu và đối chiếu baseline mạnh (distance + early visits, idle-time, potential, utilization sửa chuẩn hóa).
4. Chỉ mở thử nghiệm lớn khi một phép thử nhỏ trên trạng thái thật cho thấy candidate khác có ích, với cùng hợp đồng và compute budget. H6 đã xem không dùng chọn tham số rồi gọi là holdout.

Không sửa RideBound source/config/raw artifacts. Git status vẫn đúng hai thay đổi có sẵn: file WP14R benchmark ngày 05/09 bị sửa và `Kết quả benchmark.md` chưa tracked. Mọi probe/ghi chép mới nằm ngoài repo RideBound. Không có tiến trình benchmark đang chạy ở mốc dừng.

Tệp chi tiết: `RESEARCH-STATUS.md`, `IDEA-FALSIFICATION.md`, `READING-LEDGER.md`, `SHAREABILITY-SHADOWS-18-NOTES.md`, `DOCS-READING-CORRECTIONS.md`; kết quả máy đọc trong `evidence-audit.json`, `portfolio-choice-audit.json`, `pair-competition-analysis.json`, `repair-probe-analysis.json`, `all-order-probe-analysis.json`. Progress đọc: `docs-reading-progress.json`.
