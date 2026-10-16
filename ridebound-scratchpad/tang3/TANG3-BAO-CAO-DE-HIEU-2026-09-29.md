# Tầng 3 — bản dễ hiểu cho báo cáo (2026-09-29, đã soát độc lập)

<!-- GHI CHÚ NỘI BỘ, xóa khi chèn vào luận văn:
- Nguồn số liệu:
  - các bảng: sweep\SWEEP-REPORT.md §4a, §4b, §7, §8; sweep\sweep-jobs-2026-09-26.tsv; sweep\noworse-jobs-2026-09-26.tsv;
    sweep\logs\noworse-aggregate-2026-09-26.txt;
  - ví dụ khách: transcript C:\RideBoundData\research\tier3-sweep-noworse-v1\Mplus-120-W1-d20181112-s10-r1-w08 và
    E:\RideBoundData\research\tier3-sweep-v1\C-120-W1-d20181112-s10-r1-w08;
  - con số 222/220/2 khách: một agent soát độc lập đếm lại ngày 2026-09-29 bằng evidence\audit_vep.py và
    sweep_analyze.event_times trên 22 lần chạy (b). Chưa có script lưu riêng: nếu dùng trong luận văn, phải viết
    script và lưu output;
  - hệ số tắc đường: FleetPy_Manhattan\networks\Manhattan_2019_corrected\2018-11-1{2..6}_tt_factors.csv.
- Tất cả là kết quả thăm dò. -->

## Khi hệ thống không còn cách nào giữ lời hứa thì chuyện gì xảy ra?

### Vì sao cần tầng này

Ở Tầng 2, chúng tôi thấy rằng khi đường tắc, cách hứa theo hạn chót của Schulz và Pfeiffer có thể đẩy hệ thống
vào thế không còn lựa chọn nào hợp lệ: mọi cách làm đều vi phạm lời hứa, kể cả việc để xe chạy tiếp như cũ. Lúc
đó chương trình mô phỏng dừng lại. Vì vậy chúng tôi biết được luật nào làm hệ thống bế tắc, nhưng chưa biết mỗi
luật chở được bao nhiêu khách và giữ được bao nhiêu lời hứa. Tầng 3 trả lời hai câu hỏi đó.

### Hai cách hứa được so sánh

- **Cách hứa của khóa luận:** "Hệ thống sẽ không tự ý làm giờ trả của bạn xê dịch quá x giây." Ví dụ, xe đi vòng
  để ghép thêm người thì bị tính. Tắc đường thì không tính.
- **Cách hứa của Schulz và Pfeiffer:** "Bạn sẽ đến không muộn hơn giờ hẹn ban đầu quá x giây." Trễ vì bất cứ lý do
  gì cũng tính.

Ngoài ra còn một trường hợp đối chứng: hệ thống ghép khách tự do, không hứa gì.

### Chuẩn bị để đo được

Trước tiên, chúng tôi sửa hệ thống để nó không dừng khi bế tắc. Hệ thống ra quyết định điều xe nhiều lần mỗi
phút. Khi ở một lần quyết định có xe không còn lựa chọn nào giữ được lời hứa, chúng tôi gọi đó là một quyết định
**bị ép**: xe tiếp tục chạy theo kế hoạch cũ, và hệ thống ghi lại rằng nó đã thất hứa với khách nào. Khi xe đến
đón muộn hơn giờ đã hẹn, hệ thống cũng ghi nhận việc đó thay vì báo lỗi.

Tiếp theo, chúng tôi chuẩn bị sáu kiểu tắc đường:
- đường không đổi;
- tắc đường **đo thật** của ngày 12/11/2018;
- bốn kiểu **do chúng tôi tự tạo**: một cú tắc đột ngột rồi thông dần; tắc nặng và tắc nhẹ xen kẽ mỗi 15 phút;
  đường thoáng dần; tắc lệch ngẫu nhiên giữa các cặp điểm.

Các kiểu tự tạo dùng để thử những tình huống tắc bất ngờ mà dữ liệu thật không ghi lại được.

Mọi lời hứa trong mỗi lần chạy đều được dựng lại từ dữ liệu gốc để kiểm tra. Ở giai đoạn thử nghiệm trước đó, một
chương trình kiểm tra viết độc lập tính lại các con số từ dữ liệu gốc. Nó tìm ra một chỗ sai, và chỗ đó đã được
sửa. Các lần chạy ở đây dùng lại chính công cụ kiểm tra đã được đối chiếu ấy.

Mỗi **kịch bản** là hai giờ cao điểm của ngày 12/11 (8:00–10:00 hoặc 17:00–19:00), với 108 khách và 8 xe. Khách
lấy từ các chuyến taxi thật ở Manhattan. Mạng đường là bảng thời gian đi giữa 96 điểm chọn sẵn, không phải bản đồ
phố đầy đủ.

### So sánh ở nhiều mức hứa, từ 30 giây đến 15 phút (156 lần chạy)

Chính bài báo dùng mức 15 phút, nên chúng tôi so ở sáu mức: 30 giây, 1, 2, 5, 10 và 15 phút. Để công bằng:
- hai cách hứa dùng chung mọi thứ khác, chỉ khác đúng phần luật hứa;
- cả hai chỉ cấm một lựa chọn khi nó vượt hẳn mức cho phép;
- hạn chót được tính từ giờ hẹn ban đầu, đúng như bài báo.

Chúng tôi cũng viết trước bảy dự đoán và khóa lại trước khi chạy. Năm dự đoán đúng.

**Tắc đường đo thật** (2 kịch bản, 216 khách; nếu không hứa gì, hệ thống chở được 192 người)

| Mức hứa | Khách chở được (khóa luận / bài báo) | Khóa luận thất hứa | Bài báo thất hứa |
|---|---|---|---|
| 30 giây | 189 / 189 | 0% | 1,1% |
| 1 phút | 190 / 190 | 0% | 0% |
| 2 phút | 190 / 191 | 0% | 0% |
| 5 phút | 192 / 192 | 0% | 0% |
| 10 và 15 phút | 192 / 192 | 0% | 0% |

**Tắc đường tự tạo** (6 lượt chạy = 2 kịch bản × 3 kiểu: một cú tắc, tắc xen kẽ, tắc lệch ngẫu nhiên; 648 khách;
nếu không hứa gì, hệ thống chở được 523 người)

| Mức hứa | Khách chở được (khóa luận / bài báo) | Khóa luận thất hứa | Bài báo thất hứa |
|---|---|---|---|
| 30 giây | 508 / 503 | 0% | 18,8% |
| 1 phút | 509 / 503 | 0% | 14,7% |
| 2 phút | 513 / 513 | 0% | 10,1% |
| 5 phút | 522 / 524 | 0% | 1,0% |
| 10 và 15 phút | 523 / 523 | 0% | 0% |

**Theo từng kiểu tắc đường** (mỗi kiểu chạy trên 2 kịch bản, 216 khách)

| Kiểu tắc đường | Không hứa gì chở được | Bài báo thất hứa ở mức 30 giây / 1 / 2 / 5 phút |
|---|---|---|
| Đường không đổi | 201 | 0 / 0 / 0 / 0% |
| Một cú tắc đột ngột (tự tạo) | 167 | 12 / 12 / 8 / 3% |
| Tắc nặng, nhẹ xen kẽ (tự tạo) | 166 | 29 / 25 / 21 / 0% |
| Đường thoáng dần (tự tạo) | 215 | 0 / 0 / 0 / 0% |
| Tắc lệch ngẫu nhiên (tự tạo) | 190 | 15 / 7 / 1 / 0% |
| Ngày thật 12/11 | 192 | 1 / 0 / 0 / 0% |

**Tắc đường thật.** Hai cách hứa gần như không khác nhau. Số khách chênh nhau nhiều nhất một người. Cách hứa của
bài báo chỉ thất hứa ở mức 30 giây: 1,1% khách tính trên cả hai kịch bản, gồm 2,2% vào buổi sáng và không có vào
buổi tối.

**Tắc đường tự tạo.** Khác biệt lộ rõ ở nhóm này. Cách hứa của bài báo thất hứa với 10 đến 19% khách ở các mức
từ 30 giây đến 2 phút, còn cách hứa của khóa luận không thất hứa lần nào.

Cần nói rõ các cú tắc tự tạo đột ngột hơn ngày thật. Ở kiểu một cú tắc đột ngột, thời gian đi tăng 60% chỉ trong
15 phút. Trong dữ liệu thật, bước tăng lớn nhất giữa hai mốc 15 phút là khoảng 16%. Dữ liệu thật cũng có lúc tăng
tới 29–50% trong một giờ, nhưng không có bước nhảy 60% chỉ trong 15 phút như vậy.

**Cách so công bằng.** Con số "khóa luận thất hứa 0%" là điều phải đúng theo thiết kế, vì khóa luận chỉ hứa phần
mà hệ thống tự gây ra. Muốn so công bằng thì phải chấm cả hai cách bằng cùng một thước. Chấm bằng thước của bài
báo, tức "đến muộn hơn giờ hẹn ban đầu quá 30 giây":
- **Tắc đường thật:** khách của cả hai cách đều là 1,1%.
- **Tắc đường tự tạo:** khách của khóa luận là 17,7%. Khách của bài báo là 18,4% với cách xử lý bế tắc mới (mục
  dưới), hoặc 18,8% với cách cũ như trong bảng.

Tức là chuyến đi của khách gần như giống hệt nhau. Chỗ khác nhau là lời hứa có đúng hay không.

### Sửa cách xử lý bế tắc cho công bằng (28 lần chạy)

**Cách cũ:** xe bị bế tắc không được nhận thêm khách cho tới khi trả xong người đang trễ, như bị "đứng hình". Như
vậy có thể phạt oan cách hứa của bài báo.

**Cách mới:** xe vẫn được nhận thêm khách, miễn là tuyến mới không làm vỡ thêm lời hứa nào khác, và không làm
người đang trễ trễ thêm. Cách mới được thêm **sau khi** đã khóa dự đoán, nên kết quả chỉ để mô tả.

Chúng tôi chạy lại 22 lần có xảy ra bế tắc, và 6 lần đối chứng không có bế tắc. Sáu lần đối chứng cho kết quả
giống hệt trước, đúng như dự kiến.

- **Tắc đường thật:** cách mới không đổi số khách. Chỉ một kịch bản thật từng xảy ra bế tắc, và ở đó số khách vốn
  đã bằng nhau.
- **Tắc đường tự tạo:** số khách của cách hứa bài báo trở về ngang với khóa luận: 508 so với 508 ở mức 30 giây, 509
  so với 509 ở mức 1 phút. Ở mức 2 phút là 514 so với 513.
- **Tổng trên 22 lần chạy có bế tắc:** cách hứa của bài báo chở 1.864 khách với cách cũ, 1.874 với cách mới;
  khóa luận chở 1.873. Ở 19 trên 22 lần, cách mới và khóa luận đưa ra đúng cùng từng quyết định.
- **Không phải lúc nào cũng tăng:** cách mới không luôn chở nhiều hơn cách cũ. Ví dụ một kịch bản buổi tối ở mức
  2 phút: cách cũ 82 khách, cách mới 79, bằng đúng khóa luận.

Điều này **gợi ý** rằng khoảng chênh nhỏ trước đó đến từ cách xử lý bế tắc cũ, không phải từ bản thân cách hứa.
Mỗi kịch bản mới chạy một lần, nên chênh lệch 1–2 khách chưa nói được là do ngẫu nhiên hay không.

**Gánh bế tắc.** Trong 22 lần chạy này, 24% số lần quyết định là quyết định bị ép. Con số này nghe lớn, nhưng tất
cả chỉ do 224 khách trễ, trên 1.874 khách được chở. Từ lúc lời hứa của một khách không còn giữ được cho tới khi
khách đó xuống xe, mọi lần quyết định đều bị đánh dấu. Tính bình quân, khoảng 17 lần quyết định bị đánh dấu cho mỗi
khách trễ.

### Vì sao cách hứa của bài báo thất hứa

Trong 222 khách bị thất hứa ở 22 lần chạy có bế tắc:
- 220 người không bị hệ thống làm trễ giây nào;
- 2 người còn lại bị hệ thống làm trễ tối đa khoảng 9 giây.

Gần như toàn bộ phần trễ là do đường tắc thêm **sau khi** khách đã đặt xe và được hứa giờ. Hệ thống không thể biết
trước điều đó, vì nó chỉ dự báo theo tình trạng đường hiện tại.

**Ví dụ thật:** mức hứa 2 phút, kiểu một cú tắc đột ngột, buổi sáng. Giờ tính từ đầu khung.
- Phút 25:54, khách đặt xe. Theo đường lúc đó, hệ thống hứa trả lúc 36:58, nên hạn chót là 38:58.
- Phút 30:00, cú tắc đến. Khách lên xe lúc 32:32, và đến nơi lúc 41:09: trễ 251 giây so với lời hứa đầu.
- Phần do hệ thống gây ra: 0 giây.
- Cùng khách đó dưới luật của khóa luận: cũng đến lúc 41:09, và lời hứa của khóa luận vẫn giữ được.

### Kết luận

Theo định lý, và trong cả 72 lần chạy với luật của khóa luận, cách hứa này chưa lần nào đẩy hệ thống vào bế tắc.
Nó luôn giữ được lời hứa của nó, và chở được số khách ngang với cách hứa của Schulz và Pfeiffer.

Hai cách khác nhau rõ khi đường tắc thêm đột ngột: lúc đó lời hứa về giờ đến bị phá vì những điều nằm ngoài tầm
tay, còn lời hứa về việc hệ thống tự làm thì vẫn giữ được. Với tắc đường thật ở hai khung giờ đã chạy, hai cách
chỉ khác chút ít ở mức hứa 30 giây. Từ mức 1 phút trở lên, không cách nào thất hứa.

### Những điều cần lưu ý

- Mới chạy trên hai kịch bản của một ngày, mỗi kịch bản một lần, nên chưa biết các chênh lệch 1–2 khách có phải do
  ngẫu nhiên hay không.
- Bốn trong sáu kiểu tắc đường là tự tạo, và đột ngột hơn tắc đường thật.
- Hai khung giờ đã chạy (8–10h và 17–19h) đều là lúc tắc đường đã qua đoạn tăng nhanh.
  - Trong dữ liệu thật của các ngày 12–16/11, khung 7–9h tăng tới 47–66%, còn khung 8–10h chỉ tăng 15–23%.
  - Riêng ngày 12/11 là 48% so với 18%.
  - Khung 7–9h chưa được chạy.
- Chúng tôi chỉ so **cách hứa**, không so toàn bộ hệ thống của bài báo:
  - không có mô hình khách tự chọn nhận hay từ chối chuyến, và không có thuật toán ghép khách riêng của họ;
  - hệ thống của chúng tôi có giới hạn thời gian chờ đón và thời gian ngồi xe, và không cho đổi xe;
  - dữ liệu Hamburg mà bài báo dùng chưa được chạy; chỉ có dữ liệu Manhattan.
- Mạng đường là bảng thời gian đi giữa 96 điểm chọn sẵn, không phải bản đồ phố đầy đủ. Trừ kiểu tắc lệch ngẫu
  nhiên, tắc đường là một hệ số chung cho cả thành phố, đổi mỗi 15 phút.
- Bộ kiểm tra chính thức của dự án chưa hỗ trợ tắc đường thay đổi. Vì vậy các lần chạy này chưa được nó kiểm, và
  được xem là kết quả thăm dò. Tất cả các lần chạy đều hoàn tất bình thường.
- Còn chưa làm:
  - so lại với cách hứa theo giờ trên ứng dụng, dùng cách xử lý bế tắc mới;
  - chạy khung 7–9h chỉ dùng dữ liệu thật;
  - tính xem lời hứa được giữ trong bao nhiêu phần trăm trường hợp, có kiểm chứng trên dữ liệu mới;
  - chạy xác nhận chính thức.
