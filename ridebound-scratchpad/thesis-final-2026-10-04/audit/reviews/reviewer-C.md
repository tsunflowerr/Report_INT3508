# Reviewer 3 (C)

Báo cáo phản biện nội bộ độc lập, ngày 04/10/2026. Trọng tâm được giao là khả năng đọc, tiếng Việt, thuật ngữ, mạch lập luận và các hình, bảng. Đây là một ngữ cảnh đánh giá nội bộ, không phải danh tính của một phản biện con người.

## Phạm vi đánh giá

**Input scope** Toàn bộ `thesis_draft.pdf` gồm 65 trang vật lý, toàn bộ nguồn LaTeX trong `source`, cùng mã nguồn chọn lọc, kế hoạch, bảng dữ liệu, hồ sơ kiểm lại và các nguồn sơ cấp có trong `review-packet-v1`.

**Assessment boundary** Áp dụng `COMMON-CRITERIA.md` cho khóa luận cử nhân Công nghệ thông tin. Năm trục của Nature Reviewer được dùng để tổ chức đánh giá, không áp tiêu chuẩn phù hợp xuất bản Nature hay giới hạn độ dài của tạp chí. Tôi đã đọc toàn bộ PDF và nguồn văn bản, xem tổng thể tất cả các trang đã kết xuất, rồi xem riêng Hình 3.1, Hình 4.1 đến 4.4, Bảng 2.1, Bảng 3.1 và 3.2, Bảng 4.1 đến 4.9. Đối chiếu SHA-256 của các tệp trong gói với `MANIFEST.json` không có sai khác. Không đọc báo cáo phản biện khác, hồ sơ kiểm toán của ngữ cảnh tổng hợp hoặc bản tổng hợp.

**Shared manuscript claim summary** RideBound ghi sổ tích lũy riêng theo hành khách và chiều cam kết, phân biệt lời hứa trước, phép chiếu tuyến giữ nguyên và lời hứa mới. Cổng hành vi kiểm phần chênh giữa hai phương án tại cùng trạng thái. Bản thảo chứng minh điều kiện giữ được phương án giữ tuyến, so bốn họ cổng và đo chi phí phục vụ trong mô phỏng. Các kết luận thực nghiệm được giới hạn ở những cấu hình và panel đã chạy, với H6 không đạt tiêu chí tổng hợp và T38 chỉ cung cấp bằng chứng thăm dò.

**Visible evidence base** Các định nghĩa và chứng minh ở Chương 3, bảng và hình ở Chương 4, `PromiseDeltaCalculator.cs`, `CommitmentBudgetEvaluator.cs`, những phần liên quan của `HardVectorCandidateAssessor.cs`, các kế hoạch tầng 2 và T38, cùng các bảng từng ô và hồ sơ kiểm lại trong `evidence`. Các phép trích xuất lại không được tính là thí nghiệm độc lập mới.

**Missing materials affecting confidence** Gói này chứa đoạn mã chọn lọc và hồ sơ phân tích, không chứa toàn bộ phiên bản bộ chọn, adapter và mọi biên bản mô phỏng gốc mà các đường dẫn dẫn tới. Vì giới hạn chỉ dùng gói bất biến, tôi không chạy lại mô phỏng hoặc mở dữ liệu ngoài gói. Do đó không thể xác nhận độc lập toàn bộ thực thi, mọi bất biến vật lý hoặc thứ tự mục tiêu thực tế từ gói này. Giới hạn này không được diễn giải thành bằng chứng các kết quả đã sai.

## Đánh giá tổng thể

Khóa luận có một luận điểm kỹ thuật đủ rõ và có thể bảo vệ ở bậc đại học. Giá trị chính là định nghĩa chính xác một nghĩa vụ có thể kiểm, hiện thực sổ cái và ghi chứng cứ, rồi cho thấy nghĩa vụ ấy có chi phí và giới hạn trong mô phỏng. Bản thảo tránh đồng nhất sổ hành vi với giờ đến thực tế hoặc mức hài lòng. Việc giữ kết quả âm H6, giao nhau chuyến nguồn của T38, các lần dừng vật lý và những dự đoán sai làm phần kết luận đáng tin hơn.

Mạch từ câu hỏi nghiên cứu đến định nghĩa, thực nghiệm và kết luận tương đối nhất quán. Ví dụ ba mốc và phản ví dụ sửa chữa có lợi giúp người đọc hiểu cả ý nghĩa lẫn giới hạn của phép đo. Điểm còn yếu đáng kể là bản thảo mô tả cổng kỹ hơn bộ chọn thực sự đứng phía sau các con số. Những sửa nhỏ về tên gọi và ngôn ngữ cũng cần làm để người đọc ngoài chuyên ngành không nhầm dự báo giữ tuyến với một thành phần ngoại sinh độc lập, hoặc biến động thông báo với kết quả chuyến đi.

## Người đọc quan tâm và lý do

Sinh viên và giảng viên về thuật toán, tối ưu tổ hợp và kỹ nghệ phần mềm có thể quan tâm đến cách nối ràng buộc toán học với một sổ cái và chứng cứ thực thi. Người thiết kế hệ điều phối đi chung xe có thể dùng khung này để phân biệt nghĩa vụ, vi phạm và phục hồi. Nhà nghiên cứu vận tải hoặc tương tác người dùng có thể quan tâm đến câu hỏi hệ thống nên hứa điều gì, nhưng bản thảo chưa cung cấp bằng chứng về lựa chọn dịch vụ hoặc hài lòng để chuyển trực tiếp kết quả thành khuyến nghị cho hành khách.

## Điểm mạnh chính

- RQ1, RQ2 và RQ3 được trả lời lại theo cùng cấu trúc ở Chương 4 và 5. Giả thiết ngân sách trước quyết định và các kiểm tra khác được tách rõ ở mục 3.5.3.
- Phạm vi chứng nhận được định nghĩa ngay trong mục 3.7.1. Nó không bị trình bày như chứng minh hình thức tính đúng toàn bộ chương trình hoặc bảo đảm giờ đến thực tế.
- Phản ví dụ `v = 600`, `e = 720`, `p = 600` ở mục 3.3.1 công bố một nhược điểm thực của sổ đối xứng. Bản thảo cũng phân biệt tối ưu toàn quỹ đạo với lựa chọn cận thị tại từng kỷ nguyên.
- Các hình chính dùng đơn vị và chú giải rõ. Hình 3.1 được ghi là ví dụ dựng. Hình 4.1 nói rõ đường chỉ nối cấu hình. Hình 4.3 và 4.4 tách chênh phục vụ, điểm giữ tuyến và biến động nhìn thấy. Bảng 4.5 cảnh báo các luật có nghĩa vụ riêng.
- Mẫu số, cách gộp, kết quả âm H6 và giới hạn suy luận của T38 đều được báo gần nơi trình bày kết quả. Không cần thêm kết quả lớn hơn hoặc bằng chứng hài lòng để công nhận đóng góp kỹ thuật hẹp hiện tại.
- PDF giữ bố cục và cỡ chữ thân bài nhất quán. Nguồn đặt Times New Roman 13 pt, giãn dòng một rưỡi, lề trái 3 cm và các lề còn lại 2 cm. Bản 65 trang đáp ứng trần 80 trang; không có lý do học thuật để kéo dài chỉ nhằm đạt khoảng độ dài ưu tiên.

## Major Concerns

### R3-M1 [reproducibility]

**Severity** Major

**Blocking** No

**Axis** Tính vững kỹ thuật và khả năng đọc phương pháp

**Claim pointer** Mục 2.1.2 hẹn rằng Chương 3 sẽ mô tả bộ sinh và thứ tự mục tiêu thực tế của RideBound, với ưu tiên số khách nhận trước chi phí. Mục 4.3.2 dùng tính cận thị của bộ chọn để giải thích việc số khách không đơn điệu theo trần.

**Evidence pointer** Mục 2.1.2, trang in 6, trang PDF 18, `source/noi-dung/06-chuong2.tex`, dòng 54 và 55. Mục 3.8 và 3.8.1, trang in 23 và 24, trang PDF 35 và 36. Bảng 3.2 chỉ nêu thành phần Algorithms có “hồ sơ mục tiêu”. Mục 4.6.3, trang in 43, trang PDF 55, `source/noi-dung/08-kiemtra-phu.tex`, dòng 145 đến 151, nói đến tầng mức sử dụng ngân sách và những tầng xếp hạng khác. Đoạn mã `HardVectorCandidateAssessor.cs` định nghĩa `WorstHardUtilizationPartsPerMillion`, `DecisionInducedRevision`, `WarningExcess` và `IsForcedReference` trong kết quả đánh giá ứng viên.

**Concern** Bản thảo cho biết cổng loại phương án và bộ chọn tối ưu tại từng kỷ nguyên, nhưng không phát biểu đủ hàm chi phí, thứ tự các tầng mục tiêu thực dùng, cách tổng hợp điểm giữa xe và cách phá hòa. Những tầng xếp hạng được nhắc ở phần phục hồi và phép thử cảnh báo chưa có một định nghĩa phương pháp tập trung. Công thức (2.1) được nói rõ chỉ là mô hình nền, nên không thể dùng nó lấp khoảng trống này. Người đọc hiểu vì sao một ứng viên bị cổng loại nhưng chưa biết chính xác vì sao một ứng viên còn lại được chọn.

**Why it matters** Chi phí phục vụ và sự không đơn điệu là kết quả của cả cổng, bộ sinh và bộ chọn trên các quỹ đạo khác nhau. Thiếu mô tả bộ chọn làm yếu khả năng tái lập và đánh giá đóng góp hiện thực, dù không bác bỏ bất biến sổ cái hay các tổng mô tả đã ghi. Vì vậy đây là sửa lớn về phương pháp, nhưng không phải điều kiện chặn toàn bộ luận điểm trung tâm.

**Resolution test** Chương 3 cần có một giả mã vòng quyết định và một bảng hoặc vector thứ tự mục tiêu của bộ chọn thực dùng, nêu định nghĩa chi phí, điểm xếp hạng, cách phá hòa và tác động của miễn trừ. Nếu các đợt dùng hồ sơ khác nhau, chỉ rõ hồ sơ theo đợt và phiên bản đã ghim. Một người đọc phải có thể lấy một ví dụ ứng viên nhỏ, xác định tập qua cổng và dự đoán thứ tự ưu tiên phù hợp với bộ chạy, mà không phải suy đoán từ phần kết quả. Việc bổ sung này không mặc nhiên đòi chạy một thí nghiệm mới.

## Minor Comments

### R3-m1 [writing-clarity]

**Severity** Minor

**Blocking** No

**Claim pointer** Mục 3.3.1 gọi mốc `e` bằng nhãn tiếng Anh `exogenous`, còn mục 3.5.1 gọi việc cộng `|p-v|` là “cơ sở kết quả”.

**Affected element** Tên hai đối tượng trung tâm trong diễn giải ba mốc

**Evidence pointer** Mục 3.3.1, trang in 12, trang PDF 24, `source/noi-dung/07-chuong3.tex`, dòng 62. Định nghĩa 3.2, trang in 14, trang PDF 26. Mục 3.5.3, trang in 15, trang PDF 27, nói rõ phần giữ tuyến không được giả định độc lập với chính sách. Mục 4.1.3, trang in 26, trang PDF 38, phân biệt biến động thông báo với giờ trả thật.

**Issue** `Exogenous` dễ gợi nghĩa ngoại sinh độc lập, trong khi bản thảo đã bác bỏ cách hiểu đó. “Kết quả” cũng dễ được hiểu là giờ thực hiện cuối chuyến, dù đại lượng đang ghi sổ là biến động giữa hai thông báo dự báo. Các định nghĩa và giới hạn trong thân bài đủ rõ nên đây là vấn đề tên gọi, không phải một kết luận nhân quả sai.

**Required correction** Dùng “mốc chiếu giữ tuyến” làm tên chính của `e`, với tên trường mã nguồn được ghi riêng khi cần truy nguyên. Với `B` hoặc cổng `V`, ưu tiên “cơ sở biến động thông báo nhìn thấy”, hoặc ghi ngay cạnh tên “cơ sở kết quả” rằng kết quả ở đây là thông báo dự báo. Giữ nguyên các định danh trong mã khi trích dẫn.

**Resolution test** Chỉ đọc định nghĩa ba mốc và Bảng 3.1, người đọc phải phân biệt được phần giữ tuyến, thay đổi thông báo và thời gian thực hiện, không cần đến phần giới hạn ở cuối chương.

### R3-m2 [writing-clarity]

**Severity** Minor

**Blocking** No

**Claim pointer** Danh mục từ viết tắt và phần phương pháp được dùng để giúp người đọc hiểu thiết lập và chứng cứ thực thi.

**Affected element** Thuật ngữ tiếng Anh và nhãn chứng minh chưa được giải thích đồng đều

**Evidence pointer** Danh mục từ viết tắt, trang PDF 11 và 12. Mục 4.1.1, trang in 25, trang PDF 37, dùng “ảnh chụp” thời gian đi. Mục 4.4.2, trang in 32, trang PDF 44, dùng `episode`. Mục 4.5.4 và 4.5.6, trang in 38 và 40, trang PDF 50 và 52, dùng `SLA` và “băm inventory”. Các chứng minh ở trang in 16 đến 21 có nhãn `Proof.`; `source/main.tex` chưa đặt nhãn chứng minh tiếng Việt.

**Issue** Khóa luận có danh mục ký hiệu tốt, nhưng một số thuật ngữ lặp lại như panel, runner, adapter chưa có tương đương tiếng Việt tập trung. “Ảnh chụp” chưa nói rõ là dữ liệu thời gian đi được cố định từ một mốc, còn `inventory` không cho người đọc biết đối tượng nào được băm. `Proof.` làm nhãn chứng minh thiếu thống nhất với các nhãn Định lý, Mệnh đề và Hệ quả.

**Required correction** Giải thích ngắn các thuật ngữ thường dùng ở lần xuất hiện đầu hoặc trong danh mục, dùng nhất quán “tập ô thực nghiệm”, “bộ chạy” và “bộ chuyển đổi” khi phù hợp. Nêu rõ đối tượng của băm inventory; mở rộng SLA ở lần dùng đầu. Đổi nhãn chứng minh thành “Chứng minh”.

**Resolution test** Một người đọc Công nghệ thông tin chưa dùng FleetPy phải xác định được một ô thực nghiệm là gì, phần mềm nào ra quyết định và dữ liệu nào được băm. Kiểm PDF sau chỉnh sửa phải có nhãn chứng minh tiếng Việt thống nhất.

### R3-m3 [figures-and-tables]

**Severity** Minor

**Blocking** No

**Claim pointer** Bảng 4.9 giữ tên tệp để người đọc tìm đúng hồ sơ và tái tính kết quả.

**Affected element** Dàn trang tên tệp trong bảng truy nguồn

**Evidence pointer** Bảng 4.9, trang in 44, trang PDF 56, và `source/noi-dung/08-nguon-ketqua.tex`. Quan sát PDF cho thấy `service-budget-per-cell.csv` bị xuống dòng trong phần `service`, tên `W07X-REPORT.md` bị tách giữa ký tự của mã W07X và `check_trip_overlap.py` bị tách giữa phần `overlap`.

**Issue** Bảng vẫn đọc được, nhưng các tên định danh dài bị ngắt ở vị trí làm việc dò tệp chậm và dễ chép thiếu ký tự. Đây là một vấn đề khả năng đọc của chính bảng được dùng làm cầu nối đến chứng cứ, không phải bằng chứng nguồn dữ liệu bị thiếu hay tên tệp đã sai.

**Required correction** Dàn lại cột truy nguồn, cho tên tệp chiếm dòng riêng hoặc dùng mã hồ sơ ngắn nối với một danh sách đường dẫn đầy đủ. Ưu tiên ngắt ở dấu phân cách có sẵn và giữ các mã như W07X liền nhau. Không chèn dấu nối mới vào tên tệp.

**Resolution test** Từ PDF, người đọc phải chép đúng tên mỗi tệp và tìm được mục tương ứng trong danh sách nguồn mà không phải đoán cách nối các mảnh định danh.

### R3-m4 [writing-clarity]

**Severity** Minor

**Blocking** No

**Claim pointer** Hai trang bìa trình bày bản khóa luận tốt nghiệp cùng thông tin sinh viên và người hướng dẫn.

**Affected element** Trường người hướng dẫn còn là chỗ giữ chỗ

**Evidence pointer** Trang PDF 1 có `[chờ bổ sung]`, trang PDF 2 có `[to be filled]`; `source/noi-dung/00-bia.tex`.

**Issue** Thông tin bìa chưa hoàn tất. Điều này không ảnh hưởng luận điểm nghiên cứu, nhưng bản PDF chưa sẵn sàng để nộp nguyên trạng.

**Required correction** Điền thông tin người hướng dẫn đã được xác nhận và kiểm tra tính nhất quán giữa bìa tiếng Việt và tiếng Anh. Không tự suy đoán tên hoặc học hàm.

**Resolution test** Hai trang bìa không còn chỗ giữ chỗ và ghi cùng một người hướng dẫn với thông tin đã được tác giả xác nhận.

## Những thiếu sót kỹ thuật trung tâm cần giải quyết

Không xác định một thiếu sót `Blocking Yes` từ các tài liệu đã đọc. R3-M1 cần được xử lý để phần phương pháp đủ cụ thể cho đánh giá và tái lập. Không có cơ sở yêu cầu tác giả biến các chứng minh sơ cấp thành lý thuyết sâu hơn, biến T38 thành một bảo đảm xác suất đã xác lập, hoặc chứng minh hài lòng người dùng để bảo vệ đóng góp kỹ thuật hiện tại.

Các giới hạn đã được tác giả công bố vẫn phải giữ nguyên khi bảo vệ. Các tổng H6 là mô tả trên panel cố định; chi phí 7,13 điểm phần trăm thuộc cả gói C1. T38 có 75 chuyến nguồn chung và phụ thuộc giữa các ô, nên các khoảng lấy lại mẫu và độ phủ không chứng minh tương đương hoặc bảo đảm 90% trong quần thể. Cổng hành vi giữ sổ riêng không đồng nghĩa khách đến đúng giờ. Đây là ranh giới của kết luận hiện tại, không được biến thành những phát biểu mạnh hơn trong thuyết trình.

## Đánh giá theo năm trục

| Trục | Đánh giá ở trình độ cử nhân |
|---|---|
| Originality | Có đóng góp về tổ hợp mô hình, sổ cái, hiện thực và chứng cứ. Chương 1 và 2 giới hạn tính mới hợp lý, thừa nhận kiểm soát trước quyết định và bảo vệ từng khách đã có tiền lệ. Gói không đủ để chứng nhận quyền ưu tiên trên toàn bộ văn liệu, nhưng khóa luận không cần tuyên bố quyền ưu tiên đó. |
| Scientific importance | Kết quả có ý nghĩa cụ thể cho việc thiết kế một hợp đồng điều phối có thể kiểm và hiểu giá phục vụ của nó. Tầm quan trọng nằm ở sự rõ nghĩa và khả năng kiểm tra, chưa ở cải thiện hiệu quả vận hành hay phúc lợi đã chứng minh. Điều này phù hợp một khóa luận đại học. |
| Interdisciplinary readership | Có thể nối thuật toán, kỹ nghệ phần mềm và vận tải qua câu hỏi lời hứa nên giới hạn đại lượng nào. Liên hệ đến hành vi người dùng còn là động lực nghiên cứu, chưa là kết quả thực nghiệm. |
| Technical soundness | Các điều kiện của bất biến giữ tuyến, tính không cộng của trị tuyệt đối và khác biệt giữa các ngưỡng được phát biểu cẩn thận. Bản thảo báo đúng mức thăm dò và hạn chế thống kê. Khoảng trống phương pháp đáng kể là bộ chọn thực dùng ở R3-M1. Không thể kiểm toàn bộ mã và dữ liệu thô ngoài gói. |
| Readability for nonspecialists | Người đọc có nền tảng Công nghệ thông tin theo được câu hỏi và phép đối chiếu ba mốc. Hình và chú thích nhìn chung rõ. Các tên gọi ở R3-m1 và những thuật ngữ ở R3-m2 làm việc đọc của người ngoài nhóm triển khai khó hơn cần thiết; bảng truy nguồn còn cần chỉnh cục bộ. |

## Mức sẵn sàng cho bảo vệ đại học

Tôi ủng hộ đưa khóa luận đến bảo vệ sau khi bổ sung mô tả bộ chọn ở R3-M1 và hoàn tất những sửa nhỏ đã nêu. Luận điểm hẹp hiện tại có cơ sở lý thuyết, hiện thực và bằng chứng mô tả đủ đáng kể cho bậc cử nhân. Một thí nghiệm mới trên quần thể độc lập sẽ cần cho bảo đảm hoặc khuyến nghị vận hành mạnh hơn, nhưng không phải điều kiện bắt buộc để giữ các kết luận hẹp hiện đang viết.

## Rủi ro và điều chưa được xác lập

Khóa luận chưa xác lập hài lòng, phúc lợi, giờ đến thực tế trên đội xe thật, ưu thế số khách của cổng hành vi so với mọi cổng khác hoặc độ phủ phân phối tự do cho ngày mới. Bản thảo hiện đã nói rõ các giới hạn này. Kiểm lại từ cùng biên bản và kiểm SHA-256 hỗ trợ tính nhất quán của chứng cứ, không tạo thêm quan sát độc lập hoặc kiểm chứng toàn bộ mô hình giao thông. Những điều này cần được trình bày nhất quán trong bản cuối và khi bảo vệ.

## Ghi nhận hoàn tất

Báo cáo này được hoàn tất từ một ngữ cảnh độc lập và đóng băng trước mọi so sánh giữa các phản biện. Không có nội dung từ một phản biện khác hoặc từ bản tổng hợp được sử dụng.
