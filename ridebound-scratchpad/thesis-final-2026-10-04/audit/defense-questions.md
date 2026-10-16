# Câu hỏi bảo vệ và thông tin bản cuối phải có

Các câu trả lời dưới đây là giới hạn được hỗ trợ bởi nguồn đã đọc, không phải gợi ý tăng claim. Root cần đối chiếu với bản đã render sau cùng để chắc chắn độc giả tìm được thông tin.

| # | Câu hỏi phản biện | Câu trả lời cần thể hiện trong khóa luận | Nơi phù hợp |
|---:|---|---|---|
| 1 | Điểm mới chính xác là gì khi Fielbaum đã kiểm soát bất ổn? | Không nhận khái niệm reliability, ratchet hay trade-off là mới. Phân biệt đối tượng sổ cái decision-induced, tham chiếu tuyến giữ nguyên và khung bốn cổng dưới trôi dạt. | Ch2, Ch3 |
| 2 | Elmi đã bảo đảm cho từng khách; tại sao còn cần nghiên cứu này? | Có chồng lấn thực sự. Không quảng bá per-rider guarantee là novelty. Trình bày đại lượng họ chặn, phạm vi thời gian đi của mô hình, và phạm vi hạch toán hiện tại. | Ch2 |
| 3 | Hạn chót của Schulz có phải giống trần 30 giây không? | Cùng đơn vị nhưng khác đối tượng: độ muộn so với lời hứa đầu và tổng phần do quyết định. 900 giây là giá trị tham chiếu trong nguồn; chỉ gọi 30 giây chặt hơn khi cùng dùng cổng hạn chót trên cùng hệ. Không suy ra cổng C luôn chặt hơn cổng M+. | Ch2, Ch4 |
| 4 | Mốc e thực sự có nghĩa phản thực nhân quả không? | e là phép chiếu tuyến giữ nguyên trên trạng thái mới, tính được tại quyết định. Nó gồm tiến độ và thực thi; route history ảnh hưởng state. Không nhận diện pure traffic causal effect. | Ch3 |
| 5 | Tại sao lấy trị tuyệt đối? | Đại lượng giới hạn tổng độ dịch chuyển, nên tính cả sớm lẫn muộn. Điều này có thể phạt sửa chữa có lợi; không đồng nhất mỗi giây dời với tổn hại. | Ch3 |
| 6 | Một khách bị kéo về giờ cũ có tiêu ngân sách không? | Có: v=600,e=720,p=600 cho C increment120 và visible0. Đây là hạn chế thật, chưa xuất hiện trong panel chèn thuần. | Ch3 |
| 7 | Vì sao cộng dồn thay vì chỉ so đầu và cuối? | Chuỗi có thể dao động và triệt tiêu ở hai đầu. Với chuỗi công bố liên tục, đơn điệu không giảm, tổng nhìn thấy bằng độ muộn hai đầu; không có trôi thì tổng hành vi cũng bằng chúng. Trong H6, hai thước đo nhìn thấy gần nhau ở B1 nhưng khác nhiều ở C1, chủ yếu do phần giữ tuyến. Không suy ra ưu thế đo tổn hại do điều phối. | Ch3, Ch4 |
| 8 | 89,06% có phải phần trăm giao thông còn lại11% không? | Không phải phân hoạch chính xác. Đó là tỉ số tổng phần do quyết định/tổng biến động nhìn thấy. Có cancellation khi dấu ngược nhau. | Ch3, Ch4 |
| 9 | Trần giờ trả30s mà headline tính cả giờ đón/trả có nhất quán không? | H6 cộng cả tọa độ đón/trả khi còn mở; trần 30 giây chỉ áp tổng hành vi giờ trả. Cực đại 840,910 giây của B1 vẫn là tổng hai tọa độ, không phải drop-only. Các chỉ số cổng tầng 2/T38 xét giờ trả; khóa giờ đón thuộc gói C1. | Ch4 |
| 10 | Vì sao “không làm gì” qua cổng C? | p=e nên c=0. Cần ledger trước trong trần và N: no-op qua mọi kiểm tra ngoài commitment. Chứng minh không nói cả hệ luôn chạy. | Ch3 |
| 11 | 11/20 lần dừng có bác bỏ định lý không? | Các lần đó dừng vì cửa sổ đón vật lý/domain, không vì cổng C. Phân loại lỗi và lý do no-op phải hỗ trợ distinction này. | Ch4 |
| 12 | Loại no-op có chắc không còn ứng viên nào không? | Không tự động. Bộ chọn còn có yêu cầu baseline/no-op cụ thể; các điều kiện monotone insertion và chiều drift chỉ cấp kết luận trong phạm vi đã định. | Ch3 |
| 13 | C có phục vụ nhiều hơn V theo định lý không? | Chỉ có kết quả bao hàm tập quỹ đạo dưới giả thiết H trên mọi quỹ đạo được so. H chưa được kiểm trên mọi quỹ đạo; bất đẳng thức tam giác nghiêm không tự chứng minh H sai. Bộ chọn tại từng kỷ nguyên không phải tối ưu toàn chân trời. | Ch3, Ch4 |
| 14 | 7,13pp là chi phí riêng của cumulativecap phải không? | Không; B1→C1 thay cả bundle xác nhận gồm pickup ETA lock. Thang bắt đầu từ nobudget mới giữ các khóa để xem phần do cap. | Ch4 |
| 15 | Tại sao60s phục vụ ít hơn30s? Có lỗi số liệu không? | Cùng đầu vào có trajectory divergence tất định: lựa chọn sớm ảnh hưởng trạng thái sau. Không dựng ad hoc noise floor thành kiểm định thống kê. | Ch4 |
| 16 | Không chạm search cap có chứng minh tối ưu không? | Không. Trong 40 lượt H6 gốc, không ghi nhận cạn ngân sách, chạm trần ứng viên, bỏ ứng viên khả thi do trần hay bỏ nhánh chưa khai triển. Điều đó loại giải thích cắt sớm bởi các giới hạn đã cấu hình; không chứng minh bộ sinh đầy đủ hay tối ưu toàn không gian DARP. | Ch4 |
| 17 | Recovery(b) có che vi phạm lời hứa không? | Không. Chỉ miễn chiều bị reference vi phạm và không tệ hơn, vẫn giữ kiểm tra khác; quyết định cần có certificate non-normal/breach. Same served count không làm own promise đạt. | Ch3, Ch4 |
| 18 | Vì sao recovery(a) làm V ít khách hơn rồi(b) hết chênh? | Đây là evidence về ảnh hưởng recovery trên cùng hệ; route freeze hạn chế tiếp nhận. Không nhận service superiority của C từ comparator bị freeze. | Ch4 |
| 19 | 24% và7,3% có xác nhận trên dữ liệu giữ lại chưa? | Đây là mean per-cell development W07, chỉ2ngày, overlap với khung8–10. T38 cho bằng chứng mới với scope và các giới hạn riêng; không trộn hai denominator. | Ch4 |
| 20 | T38 có phải khẳng định độc lập hoàn toàn không? | Không. Kế hoạch được ghi trước các lượt chạy T38 đích, nhưng ngưỡng chọn sau phát triển; 20 ô khung 08:00 đã xuất hiện ở tầng 2 với chế độ chạy khác, một ô hiệu chỉnh đã được xem và có 75 chuyến nguồn chung giữa hai tập. Chia giữ lại theo nhãn nhóm không bảo đảm độc lập chuyến hoặc ngày. | Ch4 |
| 21 | Mất96khách là2,6% ít hơn U hay2,6pp? | (96/3.672)×100=2,614 điểm phần trăm giảm tỉ lệ phục vụ trên toàn bộ yêu cầu; (96/2.434)×100=3,944% giảm tương đối so với số hoàn tất của U. Hai mẫu số khác nhau. | Ch4, Ch5 |
| 22 | Mean14,5% và pooled12,4% vì sao khác? | Mean là trung bình không trọng số theo 34 ô; pooled (289/2.338)×100=12,4% gộp theo khách, nên các ô có trọng số theo số khách hoàn tất. Giữ mean làm chỉ số chính theo quy tắc đã ghi, báo pooled bổ sung và luôn ghi đơn vị phân tích. | Ch4 |
| 23 | 32/34scorecoverage có nghĩa2episode phá cận252,259s không? | Không. Hai episode vượt gamma, nhưng chỉ1episode Vmax>beta+gamma. Covered scores cấp conditional inequality; không đồng nhất với actual bound failure count. | Ch4 |
| 24 | Độ phủ94,1% có đủ để quảng bá guarantee90% không? | Không: khung 07:00 chỉ phủ 7/9 ô và một ô hiệu chỉnh quyết định gamma. Cận trên Clopper–Pearson một phía 95% cho 2/34 lần vượt gamma là 17,4%, lại dựa trên các lần thử nhị thức độc lập; nó chưa hiệu chỉnh phụ thuộc giữa ô hay khác biệt khung giờ. Độ phủ quan sát không bảo đảm quần thể. | Ch4, Ch5 |
| 25 | Tại sao chỉ96nút và108khách, có gọi fullManhattan không? | Đây là metric closure nhỏ từ nhu cầu thực; tọa độ tổng hợp, không đầy đủ street network. Không chứng minh scalability/production latency. | Ch4 |
| 26 | User satisfaction hoặc phúc lợi đã được chứng minh chưa? | Chưa. Không có choice/user study; cumulative revision không tự đồng nhất economic loss. Không dùng hệ số tiền tệ UNVERIFIED làm kết luận. | Ch5 |
| 27 | Có tái gán khách sang xe khác không? | Các comparator trong scope không cho tự do tái gán. Do đó không suy ra con số attribution cho hệ reassigning. | Ch3, Ch4 |
| 28 | Bước tiếp theo nào có khả năng thay đổi kết luận? | Verifier cho time-varying contracts; larger street-network independent grouped validation; sửa current-leg semantics trước generator sửa tuyến và user study về nội dung lời hứa. | Ch5 |
| 29 | Vì sao 56 lần chạy C không phải 56 ô đầu vào độc lập? | Tổng gồm 20 lượt tĩnh, 20 lượt biến thiên trên cùng tập chính và 16 lượt biến thiên phát triển. Cấu hình hoặc chế độ thời gian đi không tạo thêm ô nhu cầu độc lập. | Ch4, mục tầng 2 |
| 30 | Thứ tự mục tiêu thực tế có giống một tổng có trọng số không? | Không. Giải lần lượt theo thứ tự từ điển, chỉ cố định tầng trước để sang tầng sau khi đã chứng minh tối ưu; nghiệm khả thi chưa chứng minh và dự phòng không được gọi tối ưu. B1 dùng (−N,T,I); C1 thêm U,R trước T khi có trần cứng hữu hạn áp dụng, với R là vector độ dời do quyết định. Khi có ứng viên miễn trừ, phục hồi tối thiểu hóa số phương án xe bị miễn trừ trước tối đa hóa N; phá hòa theo VehicleId Ordinal rồi hạng CandidateId của từng xe. | Ch3, mục bộ chọn |
| 31 | Hai tập chia không chung nhãn nhóm có chắc không chung khách không? | Không. Nối với định danh chuyến gốc trong CSV phát hiện 75 chuyến chung, trên năm ngày và 41 cặp ô. Không dùng số thứ tự dòng cục bộ làm định danh toàn cục. | Ch4, thiết kế T38 và truy nguồn |
| 32 | Đã băm mọi khung T38 và chứng minh toàn bộ chương trình đúng chưa? | Chưa. Lượt kiểm lại băm 185 điểm kiểm tra cuối và kiểm 382.006 độ dời giờ trả; phân tích độc lập đọc quyết định và xuống xe từ biên bản. Phạm vi đó không phải kiểm mọi khung thô hoặc chứng minh hình thức toàn chương trình. | Ch3, chứng cứ niêm phong; Ch4, T38 |

Sau sửa hậu phản biện, các câu 1–32 được đối chiếu với văn bản và trang PDF cuối.
Đây là hồ sơ nội bộ; không thêm FAQ vào khóa luận và không tăng độ mạnh của kết luận.

## Vị trí trong bản PDF cuối

Bản 68 trang, SHA-256 `e7a4712663ad2167f2bbbffd7330fa0c64a580964cff558b3d3dc2ecba14454c`.
Các vị trí dưới là trang vật lý của PDF. Từ trang vật lý13 trở đi, số in trên
trang bằng số vật lý trừ12. Mỗi câu được kiểm theo định nghĩa/giới hạn trong nội
dung, không đòi một FAQ nguyên văn trong khóa luận.

| Câu | Trang vật lý chứa căn cứ | Đối chiếu |
|---:|---|---|
| 1 | 18–22, 24–26 | PASS: tiền lệ kiểm soát trước quyết định và đối tượng ghi sổ riêng. |
| 2 | 19–20 | PASS: ordinary slack/khách được chọn, không nhận per-rider là mới. |
| 3 | 19, 30–32, 42 | PASS: hạn chót900giây thuộc thiết lập văn liệu; cổng hiện tại khác đại lượng. |
| 4 | 24–25, 35 | PASS: phép chiếu tại trạng thái hiện tại, phụ thuộc lịch sử chính sách. |
| 5 | 24–25, 33, 65 | PASS: trị tuyệt đối và khả năng phạt sửa chữa có lợi. |
| 6 | 24–25 | PASS: ví dụ dựng600/720/600 có phần hành vi120 và nhìn thấy0. |
| 7 | 33, 57–58 | PASS: chuỗi so hai đầu, điều kiện đơn điệu và phân biệt các nhánh. |
| 8 | 27–28, 43–44 | PASS: tỉ số hai tổng, triệt tiêu dấu và giới hạn nhân quả. |
| 9 | 41, 43–44, 57 | PASS: headline hai chiều; trần giờ trả và thước đo cực trị ghi riêng. |
| 10 | 27–31 | PASS: điều kiện ngân sách trước và giả thiếtN. |
| 11 | 47–49 | PASS: dừng vật lý11/20 được tách khỏi dừng do cam kết. |
| 12 | 27–32, 48–49 | PASS: không suy vô nghiệm toàn danh mục chỉ từ việc no-op bị loại. |
| 13 | 28–30, 44 | PASS: H có điều kiện; tam giác nghiêm khác vi phạmH; không tối ưu toàn chân trời. |
| 14 | 44–47 | PASS: gói khóa+trần; thang giữ khóa từ nhánh không trần. |
| 15 | 45–47 | PASS: số30/60khớp, quỹ đạo tất định có thể đổi chiều kết quả. |
| 16 | 58–59 | PASS: không chạm giới hạn không chứng minh completeness/toàn cục. |
| 17 | 34–35, 49–50 | PASS: ngoại lệ theo chiều/tham chiếu vẫn ghi vi phạm. |
| 18 | 49–50 | PASS: hai quy tắc phục hồi và giới hạn suy luận ưu thế phục vụ. |
| 19 | 50 | PASS: trung bình tám ô phát triển, phân biệt tỉ lệ gộp. |
| 20 | 51–52, 61–62 | PASS: niêm phong cục bộ, dữ liệu từng thấy, chọn sau phát triển và phụ thuộc. |
| 21 | 53, 63 | PASS:96/3672điểm phần trăm khác96/2434phần trăm tương đối. |
| 22 | 53–54 | PASS: mean34ô khác289/2338khách, giữ cách gộp đã quy định. |
| 23 | 54–56 | PASS:32/34điểm khác33/34biên thực; độ vượt0,233giây. |
| 24 | 54–56, 64–65 | PASS:7/9buổi sáng, CP danh nghĩa và điều kiện trao đổi/phụ thuộc. |
| 25 | 39–42, 61–62 | PASS:96nút/108yêu cầu/mạng bao đóng/tọa độ tổng hợp, không fullManhattan. |
| 26 | 61, 65 | PASS: chưa đo lựa chọn, hài lòng hoặc phúc lợi. |
| 27 | 33–34, 39–42 | PASS: khóa xác nhận và bộ sinh không tái gán tự do. |
| 28 | 65 | PASS: kiểm chứng, môi trường độc lập, ngữ nghĩa chặng và nghiên cứu người dùng. |
| 29 | 47–48 | PASS:20tĩnh+20biến thiên+16phát triển là56lượt chạy. |
| 30 | 36–38 | PASS: thứ tự đa tầng, chứng minh tối ưu trước khóa, phá hòa và tầngF. |
| 31 | 51–52, 60 | PASS: nối CSV gốc cho75chuyến; không dùng ordinal địa phương. |
| 32 | 38, 56, 60 | PASS:185checkpoint/382006độ dời, không nhận mọi rawframe hoặc chứng minh chương trình. |

Đã kiểm khoa học đủ 32 câu ngày 05/10/2026 với nguồn phương pháp, cấu hình niêm phong và chứng cứ kiểm lại. Các câu 3, 7, 9, 16, 20–22, 24 và 30 đã được làm chính xác hơn. Câu 13 phân biệt đúng giả thiết H với bất đẳng thức tam giác; câu 20 và 31 không coi 75 chuyến nguồn giao nhau hoặc nhóm giữ lại là mẫu độc lập. Không còn điểm khoa học chưa giải quyết trong hồ sơ này; ánh xạ trang PDF cuối do root bổ sung sau biên dịch.
