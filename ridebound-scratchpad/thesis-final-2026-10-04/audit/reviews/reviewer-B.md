# Reviewer 2 (B)

## Phạm vi và tiêu chí đánh giá

Đây là đánh giá nội bộ độc lập, với trọng tâm đã định trước là thiết kế thí nghiệm, đơn vị suy luận, giả định và tính hợp lệ kỹ thuật. Tôi đánh giá theo `COMMON-CRITERIA.md` của gói `review-packet-v1`, ở mức khóa luận cử nhân công nghệ thông tin. Năm trục của Nature Reviewer được dùng làm khung đọc; báo cáo không áp tiêu chuẩn phù hợp xuất bản của Nature.

Tôi đã đọc toàn bộ 65 trang vật lý của `thesis_draft.pdf`, toàn bộ nguồn LaTeX, năm tệp mã C# được chọn, các kế hoạch và sửa đổi tầng 2, W07X, T38, cùng các script và dữ liệu đối chiếu liên quan. Tôi đã xem riêng năm hình trong PDF. Cả 76 tệp được kê trong `MANIFEST.json` khớp SHA-256. Không có báo cáo của người đánh giá khác hoặc tổng hợp chung trong ngữ cảnh này.

Các vị trí dưới đây dùng số trang in của luận văn; số trang vật lý PDF được ghi thêm khi cần. Các đường dẫn tương đối nằm trong gói cố định. Gói chỉ chứa mã được chọn và bằng chứng trích xuất, không chứa toàn bộ bộ chạy, adapter, cấu hình hay mọi biên bản thô được dẫn. Tôi không chạy lại mô phỏng hoặc kiểm thử .NET và không truy cập các đường dẫn dữ liệu ngoài gói. Vì vậy, tôi đánh giá tính nhất quán của lập luận và bằng chứng cung cấp, không xác nhận độc lập toàn bộ quá trình thực thi.

## Đánh giá tổng thể

Khóa luận có một lõi có thể bảo vệ ở trình độ cử nhân. Ba mốc tạo một phép hạch toán rõ ràng, các chứng minh sơ cấp đúng trong giả thiết đã nêu, và thực nghiệm đo được chi phí của những cấu hình cụ thể. Giá trị đáng chú ý là phân biệt nghĩa vụ mà cổng cưỡng chế với kết quả mà khách nhìn thấy, rồi giữ cả kết quả âm của H6 và các vi phạm sau phục hồi trong lập luận.

Phạm vi khẳng định hiện tại tương đối chặt. Bản thảo không dùng Định lý 3.3 để suy ra thứ hạng dịch vụ của bộ chọn cận thị, không biến việc giữ no-op thành khả thi vật lý, và không nhận độ phủ 90% cho quần thể từ T38. Vì các kết luận đã được giới hạn như vậy, giao nhau chuyến nguồn và phụ thuộc theo ngày là giới hạn của khả năng khái quát, chưa phải bằng chứng rằng các tổng mô tả trong panel sai.

Vấn đề còn đáng kể là phần phương pháp chưa mô tả đầy đủ chính thuật toán chọn và cấu hình thực thi tạo ra các số trung tâm. Đường dẫn và băm giúp truy nguồn, nhưng chưa thay được mô tả phương pháp tự chứa trong một khóa luận về hệ thống điều phối. Tôi không xác định được một vấn đề `Blocking Yes` từ gói này. Tôi đề nghị hoàn thiện R2-M1 trước bản nộp cuối và sửa hai điểm thuật ngữ, đơn vị báo cáo bên dưới.

## Người đọc có thể quan tâm

Người nghiên cứu tối ưu điều phối và kỹ sư hệ thống vận tải có thể dùng khung bốn cổng để xác định chính xác một lời hứa đang chặn đại lượng nào. Người làm phần mềm có yêu cầu kiểm toán quyết định có thể quan tâm đến sổ cái, chứng cứ trước và sau, cùng cách ghi miễn trừ. Với người vận hành hoặc nghiên cứu hành vi hành khách, kết quả gợi ra câu hỏi thiết kế hợp đồng, nhưng chưa cung cấp một lựa chọn ngân sách đã được xác nhận là có lợi cho người dùng.

## Điểm mạnh chính

- Các giả thiết (B), (N), (H) được phát biểu và giới hạn đúng chỗ. Định lý 3.6 phân biệt một quyết định với quỹ đạo dự phòng, và mục 3.5.6 giải thích khi bộ sinh chèn làm trần theo chuỗi gần trần hai đầu. Các phản ví dụ được nhận diện là ví dụ dựng, không phải quan sát thực nghiệm.
- Mã được cung cấp hỗ trợ ngữ nghĩa toán học cốt lõi. `PromiseDeltaCalculator.cs` dòng 64 đến 97 tính đúng ba cặp mốc; dòng 259 đến 262 lấy trị tuyệt đối. `CommitmentBudgetEvaluator.cs` dòng 51 đến 104 cộng vector và kiểm trần theo pha. `CommitmentDecisionValidator.cs` dòng 751 đến 817 đối chiếu miễn trừ với đúng cổng và chiều vi phạm của tuyến giữ nguyên.
- So B1/C1 được diễn giải là chi phí của cả gói. Nhánh giữ khóa nhưng bỏ trần được báo riêng, và thất bại 7,13 điểm phần trăm so với giới hạn một điểm của H6 không bị kết quả thăm dò sau đó che đi. Đây là cách báo kết quả âm có giá trị.
- T38 báo rõ 11 ô bị loại trước mô phỏng, một ô hiệu chỉnh từng được đọc, 75 chuyến nguồn chung, nhóm chia theo ngày và mẫu, cùng giới hạn của bootstrap theo ô. Số khách, tỉ lệ miễn trừ và tỉ lệ khách vượt nghĩa vụ có mẫu số và cách gộp riêng.
- Biên tất định có điều kiện được tách khỏi việc hiệu chỉnh ngưỡng. Bản thảo phân biệt đúng 32/34 ô qua điểm giữ tuyến với 33/34 ô không vượt biên nhìn thấy, đồng thời báo độ phủ 7/9 ở khung sáng sớm và việc biên không đạt mốc 120 giây.

## Major Concerns

### R2-M1

**Severity** Major

**Blocking** No

**Axis** reproducibility

**Claim pointer** Các phép so H6 và T38 đo chi phí phục vụ của những cấu hình ghép cặp đã khóa; Chương 3 được giới thiệu là nơi mô tả bộ sinh và thứ tự mục tiêu thực tế của RideBound.

**Evidence pointer** Mục 2.1.2, trang 6 (PDF trang 18), `source/noi-dung/06-chuong2.tex` dòng 52 đến 56. Mục 3.8 và 3.8.1, trang 23 đến 24, `source/noi-dung/07-chuong3.tex` dòng 547 đến 610. Mục 4.1.1 và 4.1.2, trang 25 đến 26, `source/noi-dung/08-thietlap-va-h6.tex` dòng 6 đến 61. Mục 4.7, trang 43 đến 44, `source/noi-dung/08-nguon-ketqua.tex` dòng 35 đến 55. `code/src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs` dòng 194 đến 241 và 470 đến 509 cho thấy ngoài lọc cứng còn có đại lượng xếp hạng. `plans/tang3/t38/T38-PLAN.md` dòng 64 đến 69 dẫn tới các cấu hình và driver ngoài gói.

**Concern** Bản thảo chưa trình bày đầy đủ thứ tự mục tiêu, cách tính các chi phí thứ cấp và cách phá hòa của bộ chọn đang chạy. Mục 3.8.1 mô tả thao tác chèn nhưng không có quy trình đủ rõ từ áp sự kiện, sinh ứng viên, kiểm cổng, xếp hạng, chọn đến công bố. Thiết lập cũng chưa cho quy tắc chọn 108 yêu cầu và 96 điểm từ dữ liệu nguồn, vị trí khởi tạo đội xe, thời gian dừng và cách đặt giới hạn thời gian trên xe. Những yếu tố này ảnh hưởng trực tiếp cơ hội ghép và số hoàn tất. Mục 4.7 cung cấp tên cây kết quả, nhưng chưa có bảng ghim phiên bản và cấu hình đầy đủ cho từng lớp bằng chứng, đặc biệt H6 và tầng 2 so với T38.

**Why it matters** Một độc giả có thể hiểu và kiểm phép cộng sổ cái, nhưng chưa thể dựng lại chính phép so dịch vụ mà chỉ dựa vào phần phương pháp. Bản thảo đã thừa nhận độ nhạy quỹ đạo và cho thấy tầng xếp hạng có thể hòa vì trần bằng không; do đó việc biết chính xác mục tiêu và cấu hình là quan trọng. Tôi không khẳng định các tài nguyên đó không tồn tại ngoài gói. Vấn đề là phương pháp của khóa luận chưa làm chúng đủ rõ và dễ truy cập. Điểm này làm yếu khả năng tái lập các kết quả trung tâm, nhưng không tự phủ định các đẳng thức, bất biến có điều kiện hoặc những tổng quan sát đã cung cấp.

**Resolution test** Bổ sung một mô tả ngắn hoặc mã giả của chu trình quyết định, thứ tự đầy đủ của các mục tiêu đang áp dụng và một bảng cấu hình cho H6, tầng 2, T38. Bảng cần nêu quy tắc chọn đầu vào, các tham số phục vụ và mô phỏng, cùng mốc hoặc băm của runner, adapter, cấu hình và dữ liệu. Đường dẫn tới hồ sơ có thể dùng để mở chi tiết, nhưng độc giả cần xác định được các khác biệt giữa các đợt từ chính bản thảo. Tiêu chí đóng vấn đề là một người đọc có đủ hồ sơ được dẫn có thể dựng cùng danh mục thí nghiệm và chạy lại phép so mà không phải tự đoán các giá trị hoặc thứ tự tối ưu.

## Minor Comments

### R2-m1

**Severity** Minor

**Blocking** No

**Axis** writing-clarity

**Claim pointer / Affected element** Chênh U trừ C trung bình và khoảng lấy lại mẫu nằm dưới “sàn năm khách” của T38.

**Evidence pointer** Mục 4.5.3, trang 37 (PDF trang 49), `source/noi-dung/08-t38.tex` dòng 102 đến 108. `plans/tang3/t38/T38-PLAN.md` dòng 136 đặt điều kiện cận trên 95% của trung bình F không vượt năm khách mỗi ô.

**Issue** Điều kiện đạt dùng một giới hạn trên cho chi phí dịch vụ, trong khi “sàn” thường chỉ giới hạn dưới. Cụm “nằm dưới sàn” có thể khiến người đọc hiểu rằng kết quả không đạt một mức tối thiểu, trái với quy tắc đã nêu.

**Required correction / Resolution test** Đổi thành “trần chi phí dịch vụ năm khách mỗi ô” hoặc một cách gọi khác thể hiện rõ điều kiện không vượt năm. Giữ nguyên số và việc ngưỡng được chọn sau phát triển. Vấn đề được đóng khi thuật ngữ và dấu bất đẳng thức của tiêu chí cùng diễn đạt một giới hạn trên.

### R2-m2

**Severity** Minor

**Blocking** No

**Axis** experimental-design

**Claim pointer / Affected element** Không có dừng do cam kết và có 14 dừng vật lý trên “toàn 56 ô C” ở tầng 2.

**Evidence pointer** Mục 4.4.1, trang 31 (PDF trang 43), `source/noi-dung/08-trongdiem-troidat.tex` dòng 38 đến 40. Mục 4.1.1 định nghĩa ô bằng ngày, mẫu nhu cầu và khung giờ. `plans/deadline/PREREGISTRATION.md` dòng 17 đến 22 và 108 đến 114 kê 20 ô đối chứng tĩnh, 20 ô chính có biến thiên và 16 ô phát triển có biến thiên.

**Issue** Con số 56 cộng các lần chạy C của nhiều chế độ thời gian đi. Hai tập 20 ô chính dùng lại cùng đơn vị ngày, mẫu và khung, nên 56 không phải số ô đầu vào khác nhau theo định nghĩa ở mục 4.1.1. Các cảnh báo về độc lập ở nơi khác là đúng, nhưng cách gọi tại câu này vẫn làm đơn vị đếm không thống nhất.

**Required correction / Resolution test** Gọi đây là 56 lần chạy C trên các tổ hợp ô và chế độ thời gian đi, rồi ghi phép cộng 20 tĩnh, 20 biến thiên ở panel chính, 16 biến thiên ở panel phát triển. Vấn đề được đóng khi người đọc phân biệt được số lần chạy theo cấu hình với số ô đầu vào riêng biệt, mà không thay đổi kết quả 0 và 14.

## Những thiếu sót kỹ thuật trung tâm

Không có concern `Blocking Yes` được xác định từ vật liệu cung cấp. R2-M1 là thiếu sót đáng kể về mô tả và tái lập phương pháp cần khắc phục trong bản cuối. Tôi không thấy lỗi toán học làm hỏng Định lý 3.6 dưới (B), (N), hoặc biên tất định V không vượt C cộng X trên cùng chuỗi được đo.

Một bảo đảm xác suất ngoài mẫu, kết luận tương đương trong quần thể, tính đúng của mọi hợp đồng động trong toàn bộ chương trình, hoặc lợi ích người dùng vẫn chưa được thiết lập. Bản thảo hiện đã nhận các giới hạn này và không dùng chúng làm kết luận trung tâm. Không cần biến một hạn chế đã được thu hẹp đúng thành yêu cầu làm thêm một nghiên cứu khác để bảo vệ khóa luận hiện tại.

## Đánh giá theo năm trục

| Trục | Đánh giá ở mức khóa luận cử nhân |
|---|---|
| Tính mới | Đóng góp mô hình hóa và hiện thực có thể bảo vệ. Bản thảo phân biệt đúng sổ hành vi có mốc giữ tuyến với hạn chót và tổng biến động nhìn thấy, đồng thời nhận tiền lệ của nhiều thành phần. Những bất đẳng thức sơ cấp không bị quảng bá thành phát hiện toán học lớn. |
| Ý nghĩa khoa học | Có ích cho câu hỏi thiết kế và kiểm toán hợp đồng điều phối. Chi phí đo được và kết quả âm H6 có ý nghĩa trong phạm vi mô phỏng đã khóa. Chưa có cơ sở định giá lợi ích người dùng hoặc chọn trần tối ưu cho vận hành. |
| Độc giả liên ngành | Liên quan tới tối ưu vận tải, kỹ thuật phần mềm và thiết kế dịch vụ có cam kết. Việc phân biệt hành vi có thể cưỡng chế với kết quả chịu trôi dạt có thể hiểu ngoài chuyên ngành điều phối. |
| Độ vững kỹ thuật | Lõi toán học hợp lệ có điều kiện; so sánh mô tả được giới hạn đúng và báo các thất bại. T38 hỗ trợ tần suất quan sát trên panel, không tạo bảo đảm ngoài mẫu. Điểm yếu còn lại là hồ sơ phương pháp trong bản thảo chưa đủ tự chứa theo R2-M1; xác nhận đầu cuối toàn bộ mã không đánh giá được từ phần mã chọn. |
| Dễ đọc với người ngoài chuyên môn | Ví dụ ba mốc, danh mục ký hiệu và hình ghép cặp hỗ trợ tốt. Số và mẫu số quan trọng được giải thích. Một bảng cấu hình và quy trình quyết định sẽ giúp người đọc nối lý thuyết với hệ thực thi; R2-m1 và R2-m2 sửa hai điểm dễ gây hiểu sai tại chỗ. |

## Mức sẵn sàng cho bảo vệ cử nhân

Tôi ủng hộ đưa khóa luận tới bảo vệ sau khi bổ sung phương pháp theo R2-M1 và sửa các điểm nhỏ đã nêu. Lõi đóng góp không phụ thuộc việc H6 phải đạt hoặc việc T38 phải trở thành một bảo đảm conformal cho quần thể. Tác giả cần trình bày được chính xác mục tiêu của bộ chọn, cấu hình tạo ra giá dịch vụ, và khác biệt giữa tuân thủ cổng hành vi, miễn trừ cam kết, quy tắc đón muộn và khả thi vật lý. Bản hiện tại có cơ sở cho một khóa luận kỹ thuật có giới hạn rõ, nhưng phần phương pháp còn cần hoàn thiện trước khi coi là bản nộp cuối.

## Những khẳng định chưa được xác nhận

Không xác nhận bảo đảm giờ đến thực tế, độ phủ 90% cho ngày mới, lợi ích hài lòng hoặc phúc lợi, thứ hạng so với toàn bộ thuật toán của nghiên cứu gốc, hay tính đúng của toàn bộ hệ thực thi. Kiểm băm và tái tính từ cùng biên bản củng cố truy nguồn và trích xuất; chúng không tạo thêm thí nghiệm độc lập. Những ranh giới này phù hợp với cách kết luận hiện tại của luận văn.
