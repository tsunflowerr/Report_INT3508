# HƯỚNG DẪN VĂN PHONG: KHÓA LUẬN RIDEBOUND (bản viết lại, 10/2026)

Tài liệu này dùng cho người viết lại khóa luận. Nó nêu vì sao báo cáo môn Dự án công nghệ (DACN) của chính tác giả dễ
đọc, rút ra 35 quy tắc cho bản khóa luận mới, và chỉ ra 12 chỗ trong bản LaTeX hiện tại cần viết lại, kèm bản viết lại
mẫu. Thuật ngữ nằm ở tệp đi kèm `GLOSSARY-VI.md`.

---

## 0. Nguồn, cách trích, cách đo

**Mẫu văn phong.** `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`, "Hệ thống gợi ý điểm đến và tối ưu
hóa chuỗi hành trình nhóm thời gian thực", 50 trang PDF.
- "tr. N" là số trang in ở chân trang thân bài. Trang PDF = N + 12 (tr. 1 là trang PDF 13).
- Máy không có công cụ hiển thị trang PDF, nên đã đọc toàn bộ 50 trang bằng `pdftotext` của Git for Windows (in ra màn
  hình, không ghi tệp). Bản trích chữ làm mất chỉ số dưới của công thức. Vì vậy ở đây chỉ trích văn xuôi, và chỉ số
  dưới được viết bằng dấu "_" (ví dụ T_route,k).
- Mọi câu trong ngoặc «…» là nguyên văn, kể cả cách viết số kiểu Anh của DACN ("5269.3"). "[…]" là chỗ lược bớt.

**Bản khóa luận hiện tại (chỉ đọc).** `E:/Code/Report_INT3508/ridebound/main.tex` và `noi-dung/*.tex` (11 tệp). Vị trí
ghi dạng `tệp:dòng`, theo số dòng của tệp ngày 2026-10-10.

**Câu chuyện của bản mới.** Lấy từ `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md` (gọi tắt BAN-GIAO), mục 3 (một
hướng duy nhất, đóng góp được phép nhận) và mục 5 (các đính chính bắt buộc khi viết).

**Quy tắc bổ sung.** 37 quy tắc viết đã Việt hóa trong `optimize/codex-debate/codex-work/R19-SKILLS-REVIEW.md` (gọi tắt
R19). Các quy tắc này được gộp vào mục 2 với nhãn [R19-n]; chỗ khác nhau với DACN ghi ở mục 5.

**Số đo thô về độ dài.** "Tiếng" là chuỗi chữ cách nhau bởi khoảng trắng (gần bằng âm tiết). Câu được tách tại dấu . ! ? :
đứng trước chữ hoa. Chỉ tính các đoạn từ 20 tiếng trở lên. Với LaTeX, đã bỏ bảng, hình và công thức. Đây là số đo gần
đúng, chỉ dùng để so sánh hai văn bản.

| | DACN, thân bài tr. 1–36 | Khóa luận hiện tại (Tóm tắt tiếng Việt + Chương 1–5) |
|---|---|---|
| Trung vị độ dài câu | 26 tiếng | 25 tiếng |
| 10% câu dài nhất, từ | 45 tiếng | 51 tiếng |
| Tỉ lệ câu dài hơn 40 tiếng | 13,8% | 19,9%. Tóm tắt 55%, Chương 1 32%, Chương 5 32% |
| Trung vị độ dài đoạn | 82 tiếng | 81 tiếng. Tóm tắt 152, Chương 1 104, Chương 5 132 |
| Đoạn dài nhất | 343 tiếng | khoảng 600 tiếng (đoạn 3 của Tóm tắt) |

**Đọc bảng.** Độ dài trung bình của hai văn bản gần như bằng nhau. Vấn đề của bản hiện tại nằm ở ba chỗ.
- Những phần người đọc gặp đầu tiên và cuối cùng (Tóm tắt, Chương 1, Chương 5) có câu rất dài, nhồi số và lời rào đón.
- Mật độ thuật ngữ lạ và từ tiếng Anh rất cao (mục 4.0).
- In nghiêng, in đậm và gạch ngang dày đặc.

---

## 1. Báo cáo DACN dễ đọc nhờ đâu

### 1.1 Mở chương bằng câu nói chương sẽ làm gì

- tr. 13 (mở Chương 3): «Chương 3 trình bày phương pháp tối ưu của Optigo trong việc xây dựng phương án hành trình nhóm.
  Khác với cách tiếp cận chỉ lựa chọn một địa điểm hẹn dựa trên khoảng cách tới các thành viên, Optigo xem mỗi kết quả đề
  xuất như một phương án di chuyển hoàn chỉnh, bao gồm địa điểm hẹn, điểm đón, phân công ghép đón, thứ tự di chuyển và
  các chỉ số đánh giá đi kèm.»
- Cũng tr. 13, đoạn báo trước thứ tự: «Chương này bắt đầu từ quy trình tổng quát của Optigo, sau đó đi vào từng thành
  phần chính trong quá trình tối ưu. […] Cuối chương, toàn bộ quy trình được tóm tắt bằng giả mã, kèm theo phân tích độ
  phức tạp và cách lõi tối ưu được đưa vào hoạt động thực tế của hệ thống.»
- tr. 29 (mở Chương 4): «Chương này đánh giá Optigo trên 120 kịch bản gặp mặt nhóm với nhiều cấu hình khác nhau về tài
  xế, hành khách cần được đón và địa điểm ứng viên. Mục tiêu của thực nghiệm là kiểm tra xem hệ thống có tìm được phương
  án hợp lệ hay không, chi phí di chuyển có ở mức hợp lý so với các phương án so sánh hay không, và mức bất tiện giữa các
  thành viên có được phân bố công bằng hơn hay không.»

Mẫu chung: câu đầu nói chương làm gì; câu thứ hai nói chương khác cách làm thông thường ở đâu; đoạn sau liệt kê thứ tự
các mục. Mục tiêu của thực nghiệm được viết thành các câu hỏi có/không.

### 1.2 Mạch: vấn đề → hạn chế của cách đang có → cách làm của đề tài

- tr. 1, vấn đề: «Tuy nhiên, trên thực tế, cách xử lý phổ biến để chọn địa điểm vẫn là trao đổi thủ công qua nhóm chat,
  nơi mỗi người đề xuất một vài địa điểm quen thuộc, sau đó cả nhóm tự thảo luận và đánh giá xem địa điểm nào "hợp lý".
  Cách làm này tuy đơn giản nhưng hoàn toàn cảm tính và thiếu một lớp tính toán khách quan.»
- tr. 2, hạn chế của công cụ hiện có: «Các công cụ bản đồ hiện nay giải quyết tốt nhu cầu cá nhân. Người dùng có thể tìm
  quán, xem đánh giá, chọn tuyến đường và chia sẻ địa điểm. […] Tuy nhiên, các chức năng này chủ yếu hỗ trợ thao tác cộng
  tác ở tầng danh sách. Chúng chưa trực tiếp mô hình hóa vai trò di chuyển của từng thành viên, số ghế còn lại của tài xế,
  nhu cầu được đón của hành khách, giới hạn đi bộ, giới hạn vòng đường và mức bất bình đẳng trong chi phí di chuyển.»
- tr. 1, cách làm: «Từ những hạn chế đó, đề tài hướng đến việc xây dựng một giải pháp tối ưu có khả năng chuyển quá trình
  thảo luận cảm tính thành một quá trình ra quyết định dựa trên số liệu.»

Mạch này lặp lại ở cấp mục nhỏ, kèm ví dụ:
- tr. 5: «Một cách đơn giản để xác định tâm của nhóm là lấy trung bình tọa độ của các thành viên. Tuy nhiên, cách này dễ
  bị ảnh hưởng bởi các điểm ở quá xa so với phần còn lại. Chẳng hạn, nếu đa số thành viên tập trung trong một khu vực
  nhưng có một thành viên xuất phát từ vị trí rất xa, tâm trung bình có thể bị kéo lệch về phía thành viên đó. […] Để hạn
  chế vấn đề này, hệ thống sử dụng trung vị hình học có trọng số.»

Người đọc chưa biết hệ thống vẫn theo được, vì mỗi lựa chọn kỹ thuật được giới thiệu như lời đáp cho một hạn chế đã nêu
bằng ví dụ.

### 1.3 Công thức nào cũng kèm lời giải thích từng ký hiệu và lý do cần nó

- tr. 8, sau điều kiện đi vòng (6): «Trong đó, T_route,k là thời gian di chuyển khi có ghép đón, T_direct,k là thời gian
  đi thẳng đến địa điểm gặp mặt, và α > 1 là hệ số cho phép đi vòng. Điều kiện này giúp loại bỏ những phương án quá bất
  lợi cho tài xế, ngay cả khi chúng có thể thuận tiện hơn cho hành khách.»
- tr. 9, sau điều kiện đi bộ (7): «Trong đó, s là điểm đón chung, d_walk(p_i, s) là khoảng cách đi bộ từ vị trí của hành
  khách i đến điểm s, và D_max là khoảng cách đi bộ tối đa cho phép. Trong bản cài đặt hiện tại, giá trị mặc định của
  D_max là 500 m.»
- tr. 10, sau hệ số Gini (10): «Giá trị G = 0 cho thấy các thành viên có mức bất tiện bằng nhau. Khi G tăng, mức chênh
  lệch giữa các thành viên cũng tăng. Chỉ số này giúp hệ thống đánh giá xem chi phí di chuyển có được phân bổ tương đối
  đồng đều hay không, thay vì chỉ nhìn vào tổng chi phí của cả nhóm.»

Mẫu cố định gồm bốn bước: câu dẫn ("Điều kiện này được mô hình hóa như sau:", tr. 9); công thức; câu "Trong đó, …" giải
thích mọi ký hiệu và giá trị dùng thật; một câu nói công thức loại bỏ hay đo điều gì. Đọc giá trị biên (G = 0) giúp người
đọc hiểu nhanh công thức.

### 1.4 Ví dụ cụ thể, gần đời thường

- tr. 8: «Ví dụ, xe máy thường chỉ chở thêm được một hành khách, trong khi ô tô có thể chở nhiều người hơn tùy số ghế còn
  lại. Do đó, các phương án vượt quá số chỗ còn lại của phương tiện sẽ bị loại bỏ trước khi đánh giá và xếp hạng.»
- tr. 18: «Ví dụ, từ khoảng 50 địa điểm sơ bộ, hệ thống chỉ giữ lại khoảng 15 địa điểm có điểm chi phí lộ trình tốt hơn.»
- tr. 20–21: «Một tài xế gần hành khách A nhất có thể cũng là tài xế duy nhất có thể đón hành khách B mà không vượt thời
  gian đi vòng cho phép. Nếu A được gán trước cho tài xế đó, B có thể chỉ còn những lựa chọn kém hơn, thậm chí khiến bài
  toán trở nên không khả thi.»
- tr. 24: «Trong thực tế, một phút đi bộ hoặc chờ thường gây khó chịu hơn một phút ngồi trên xe, nên được nhân trọng số
  cao hơn.»

Ví dụ luôn đi ngay sau quy tắc mà nó minh họa, và luôn kết bằng hệ quả ("Do đó, …").

### 1.5 Bảng tóm tắt ràng buộc và tiêu chí

- tr. 15–16, câu dẫn: «Các ràng buộc cứng và tiêu chí đánh giá mềm này được tổng hợp chi tiết trong Bảng 3.1.» Bảng 3.1
  có ba cột «Nhóm | Nội dung | Vai trò trong thuật toán». Dòng ràng buộc cứng ghi «Sức chứa, phân công đã chấp nhận, giới
  hạn đi bộ, thời gian đi vòng tối đa, bao phủ mọi hành khách cần đón» và vai trò «Kiểm tra tính khả thi trước khi xếp
  hạng.»
- Bảng 3.3 (tr. 19) có ba cột «Loại điểm đón | Cách sinh | Ý nghĩa». Bảng 3.7 (tr. 25) có ba cột «Thành phần | Ý nghĩa |
  Tác động», ví dụ dòng «Thời gian đi vòng | Thời gian tài xế đi thêm so với đi thẳng. | Phạt phương án bất lợi cho tài
  xế.»

Bảng định nghĩa luôn có một cột nói **vai trò** hay **ý nghĩa**, và luôn có câu dẫn trước bảng.

### 1.6 Giả mã có chú thích tiếng Việt, sau đó là một đoạn giải thích

- Bảng 3.2 (tr. 17): «2: gán trọng số wi cho từng thành viên mi», chú thích bên phải «Theo vai trò»; «14: return x», chú
  thích «Tâm truy vấn địa điểm».
- Bảng 3.4 (tr. 20): «4: thêm đón tại cửa tại vị trí của p vào C», chú thích «Phương án gốc».
- Bảng 3.5 (tr. 22): «7: sắp xếp P theo độ tiếc nuối giảm dần», chú thích «Xét người khó trước».
- Đoạn sau giả mã nói điều cốt lõi. tr. 17: «Kết quả của bước này mới chỉ là tâm dùng để truy vấn địa điểm, chưa phải địa
  điểm cuối cùng được đề xuất cho nhóm.» tr. 22: «Thuật toán trên không lưu toàn bộ các phân công có thể có. Thay vào đó,
  hệ thống chỉ giữ một tập nhỏ các nghiệm tốt để chuyển sang bước tối ưu tuyến, qua đó vẫn duy trì được không gian lựa
  chọn nhưng kiểm soát được thời gian tính toán. Đây là điểm cân bằng giữa thuật toán tham lam quá đơn giản và vét cạn
  quá tốn kém.»

### 1.7 Đoạn kết quả nói con số nghĩa là gì

- tr. 30, đoạn hướng dẫn đọc bảng: «Khi đọc Bảng 4.1, cần phân biệt giữa nhóm chỉ số phản ánh hiệu quả và nhóm chỉ số
  phản ánh mức phân bổ bất tiện.» Đơn vị được nói trước: «Các giá trị chi phí, điểm công bằng, gánh nặng di chuyển, độ
  tiếc nuối và thời gian đi vòng được tính bằng giây; thời gian xử lý được tính bằng mili giây.»
- tr. 31: «Bảng 4.2 cho thấy Optigo có phương án công bằng hơn OR-Tools trong 95 trên 109 kịch bản so trực tiếp. Với
  PyVRP và VROOM, tỷ lệ này là 92 trên 98 kịch bản. […] Nói cách khác, xét theo giá trị trung bình, Optigo không phải đánh
  đổi bằng chi phí cao hơn để đạt điểm công bằng tốt hơn, mặc dù ở một số kịch bản riêng lẻ vẫn có thể xuất hiện đánh đổi
  cục bộ giữa chi phí và công bằng.»
- tr. 33: «Khi so với cấu hình chỉ theo chi phí, Optigo đầy đủ tăng chi phí di chuyển khoảng 1.3%, nhưng điểm công bằng
  giảm từ 867.1 xuống 826.0 giây, tương đương giảm 4.7%. […] Sự đánh đổi này cho thấy hệ thống chấp nhận một mức tăng nhỏ
  về chi phí để giảm rõ hơn gánh nặng cá nhân.»
- tr. 33: «Tỷ lệ dùng điểm đón chung trung bình khoảng 15.3%. Con số này cũng cho thấy hệ thống không mặc định yêu cầu
  mọi hành khách đi bộ tới điểm chung.»

Mẫu chung: số đếm có mẫu số ("95 trên 109"), số trước và số sau ("từ 867.1 xuống 826.0"), mức thay đổi tương đối, rồi
câu "Nói cách khác, …" hoặc "Con số này cho thấy, …".

### 1.8 Nói rõ so sánh trên tập nào, và vì sao có phép so đó

- tr. 31: «Thay vì chỉ so sánh trung bình trên toàn bộ dữ liệu, Bảng 4.2 chỉ xét những kịch bản mà cả Optigo và phương
  án cơ sở đều có kết quả hợp lệ.»
- tr. 33, lý do của các biến thể: «Các biến thể này không nhằm thay thế hệ thống chính, mà giúp làm rõ mức đóng góp của
  từng thành phần vào chất lượng phương án cuối cùng. Nếu bỏ điểm đón chung, hệ thống còn đủ linh hoạt để cân bằng giữa
  hành khách và tài xế hay không. Nếu chỉ ưu tiên chi phí, phương án có còn công bằng hay không.»

### 1.9 Đánh đổi nói bằng "đổi lại"

- tr. 9: «Có thể xem điểm đón chung là một cách dung hòa giữa sự thuận tiện của hành khách và chi phí đi vòng của tài xế:
  hành khách có thể cần đi bộ thêm một đoạn ngắn, nhưng đổi lại tài xế giảm được số điểm dừng và hạn chế thời gian đi
  vòng.»
- tr. 11: «Trong bối cảnh của Optigo, nếu chỉ tối thiểu hóa tổng thời gian di chuyển, hệ thống có thể ưu tiên một địa
  điểm thuận lợi cho đa số thành viên, nhưng lại khiến một thành viên ở xa phải chịu gánh nặng di chuyển cao hơn đáng kể.
  Ngược lại, nếu chỉ tối thiểu hóa gánh nặng cực đại, hệ thống có thể chọn một phương án có tổng chi phí cao hơn chỉ để
  giảm bất lợi cho thành viên chịu thiệt nhiều nhất.»

### 1.10 Đoạn hạn chế thẳng thắn và ngắn

- tr. 32: «Tuy vậy, không nên hiểu rằng Optigo luôn tối ưu hơn ở mọi tình huống nhỏ lẻ. Trong một số kịch bản, phương án
  cơ sở vẫn có thể tốt hơn Optigo ở một tiêu chí riêng, đặc biệt khi cấu hình điểm đón đơn giản hoặc không cần điểm đón
  chung.»
- tr. 32: «Tuy nhiên, kết quả này không có nghĩa là hệ thống đã xử lý đầy đủ mọi ràng buộc cửa sổ thời gian của bài toán
  PDPTW.»
- tr. 34: «Thực nghiệm vẫn có những giới hạn cần được nhìn nhận rõ. Các kịch bản đối sánh giúp so sánh thuật toán trong
  môi trường có kiểm soát, nhưng thời gian di chuyển ngoài thực tế còn chịu ảnh hưởng bởi giao thông, thời điểm trong
  ngày, thói quen đi lại và mức sẵn sàng đi bộ của từng người dùng.»
- tr. 35: «Vì vậy, các kết quả này nên được xem là bằng chứng định lượng ban đầu cho thiết kế thuật toán, thay vì một kết
  luận tuyệt đối cho mọi tình huống sử dụng trong thực tế.»

Mỗi giới hạn chỉ nói một lần, ngay sau kết quả mà nó giới hạn hoặc trong mục thảo luận cuối chương. Mỗi giới hạn chỉ
dài một hai câu.

### 1.11 Câu chuyển tiếp giữa các mục

- tr. 2: «Để làm rõ hơn tính cấp thiết của đề tài, phần tiếp theo phân tích các hạn chế của những phương pháp và công cụ
  hỗ trợ hiện tại.»
- tr. 6: «Sau khi mô hình hóa tâm tìm kiếm bằng trung vị hình học có trọng số, vấn đề còn lại là tìm nghiệm cho hàm mục
  tiêu đã xây dựng.»
- tr. 7: «Khi trong nhóm có thành viên cần được đón, bài toán không chỉ dừng lại ở việc chọn địa điểm gặp mặt.»
- tr. 20: «Khi các điểm đón khả thi đã được sinh ra, hệ thống cần xác định hành khách nào sẽ đi cùng tài xế nào.»
- tr. 28: «Chương 4 sẽ tiếp tục trình bày cách cài đặt, kiểm thử và đánh giá các thành phần đó.»

### 1.12 Thuật ngữ: tiếng Việt trước, tiếng Anh trong ngoặc một lần

- tr. 7: «Bài toán định tuyến phương tiện, hay Vehicle Routing Problem-VRP [7], là bài toán lập lộ trình cho nhiều phương
  tiện để phục vụ một nhóm điểm cần đi qua với tổng chi phí di chuyển nhỏ nhất.»
- tr. 12: «Tập các phương án không bị bất kỳ phương án nào khác thống trị tạo thành biên Pareto (Pareto Frontier) [12].»
- tr. 10: «Gánh nặng cá nhân lớn nhất (Max Member Burden) được xác định bởi:»

### 1.13 Các nét khác nên học

- **Nhãn đầu đoạn kết bằng dấu hai chấm** cho các đoạn có vai trò rõ: «Hạn chế của các phương pháp hiện tại:» (tr. 2),
  «Nhu cầu thực tiễn:», «Phạm vi đề tài:» (tr. 3), «Mục tiêu chính:», «Đóng góp khoa học và kỹ thuật:» (tr. 3).
- **Phạm vi viết thành gạch đầu dòng có nhãn**, ví dụ tr. 3: «Quy mô nhóm: Hệ thống được thiết kế tối ưu cho các nhóm từ
  2 đến 8 thành viên - quy mô phổ biến nhất của các buổi tụ tập bạn bè, đồng nghiệp và gia đình nhỏ.»
- **Kết luận mở bằng một câu tóm cả đề tài**, tr. 35: «Báo cáo này đã trình bày thiết kế và đánh giá Optigo, một hệ thống
  hỗ trợ lựa chọn điểm gặp và tối ưu chuỗi di chuyển cho nhóm nhỏ trong bối cảnh có nhiều khác biệt về vị trí xuất phát,
  phương tiện và nhu cầu ghép đón.» Tiếp theo là câu nói trọng tâm bằng chuỗi câu hỏi đời thường: «[…] ai tự đi, ai cần
  được đón, tài xế nào nhận hành khách nào, nên dừng ở đâu, […]».
- **Hướng phát triển đánh số "Thứ nhất / Thứ hai / Thứ ba"**, mỗi hướng một câu (tr. 36).
- **Chủ ngữ là đối tượng, không phải người viết.** Trong thân bài (tr. 1–36), "hệ thống" xuất hiện 94 lần, "đề tài" 11
  lần, "báo cáo" 6 lần. "Chúng tôi", "chúng ta" và "em" không xuất hiện lần nào. "Em" chỉ có ở Lời cảm ơn.
- **Phân bổ trang** (theo Mục lục): Chương 1 tr. 1–4, Chương 2 tr. 5–12, Chương 3 tr. 13–28, Chương 4 tr. 29–34,
  Chương 5 tr. 35–36. Chương phương pháp dài nhất; chương mở đầu và chương kết luận ngắn.

### 1.14 Chỗ DACN chưa tốt: không bắt chước

- **Trộn tiếng Anh vào câu**: «Pipeline xử lý tổng quát» (tiêu đề 3.1.3, tr. 14); «Đây là open-path TSP» (tr. 22); «dùng
  branch-and-bound có cắt tỉa» (tr. 21); «hạt giống (seed)» (tr. 23); «Ffair gom các penalty công bằng» (tr. 25);
  «thường là top 3» (tr. 26). Giả mã Bảng 3.5 có dòng «Require: drivers, pending passengers, accepted assignments và địa
  điểm» (tr. 22).
- **Giới thiệu tên Việt nhưng sau đó quay lại tên Anh**: «Mức thiệt tương đối lớn nhất (Worst Regret)» (tr. 11), rồi
  tr. 11–12 vẫn viết «Worst Regret»; tr. 15 và 26 lại dùng «độ tiếc nuối lớn nhất». Một khái niệm có ba tên.
- **Số viết kiểu Anh**: «9.9 thành viên, 3.1 tài xế» (tr. 29), «5269.3» (tr. 30). Bản khóa luận hiện tại đã viết đúng
  kiểu Việt ("$80{,}32\%$", `08-chuong4.tex:161`); giữ cách đó.
- **Hai thứ cùng được gọi là "quan trọng nhất"**: «Đây là kết quả quan trọng nhất của phần thực nghiệm» (tr. 31) và
  «Đây là phần kết quả quan trọng nhất vì DARP-MP gần với mục tiêu thiết kế của Optigo» (tr. 32).

---

## 2. Ba mươi lăm quy tắc cho khóa luận mới

### A. Chương, mục, đoạn, câu

Ký hiệu [R19-n] ghi quy tắc thứ n trong bản chắt lọc của Codex (`optimize/codex-debate/codex-work/R19-SKILLS-REVIEW.md`)
đã được gộp vào đây. Mục 5 ghi những chỗ hai nguồn khác nhau và cách đã chọn.

1. **Mở chương** bằng một hai đoạn nói chương trả lời câu hỏi gì và đi theo thứ tự nào (mục 1.1). Chương nào cũng phải
   phục vụ câu chuyện chính; bỏ phần chỉ làm tăng số trang [R19-5]. Không mở chương bằng bảng "lộ trình khẳng định"
   như `08-chuong4.tex:3-36`.
2. **Mở mục lớn** bằng một câu nói mục làm gì hoặc vì sao cần. Khi mạch chuyển ý, kết thúc mục bằng một câu nối sang mục
   sau (mục 1.11).
3. **Mỗi ý lớn đi theo mạch**: vấn đề → cách đơn giản hoặc cách đang có → vì sao chưa đủ, kèm ví dụ → cách của khóa luận
   (mục 1.2). Giải thích yêu cầu, chuyến xe, giới hạn và đầu ra bằng lời thường trước khi đưa mô hình, để người học
   tin học chưa biết hệ thống vẫn theo được [R19-6].
4. **Một đoạn một ý.** Câu đầu đoạn nói ý đó, các câu sau đưa căn cứ. Câu cuối chỉ thêm hệ quả hoặc nối ý, không nhắc lại
   câu đầu [R19-19, R19-20]. Mỗi đoạn thường dài 3–6 câu, khoảng 60–150 tiếng. Đây là mức tham khảo theo DACN, không
   phải hạn ngạch: tách đoạn khi đổi ý (ví dụ từ quan sát sang diễn giải), không tách chỉ vì đủ số tiếng.
5. **Câu dài 20–30 tiếng**; câu dài hơn 40 tiếng thì tách đôi. Một câu chứa nhiều nhất hai con số, trừ câu so sánh hai
   luật trên cùng một chỉ số. Đặt chủ ngữ gần động từ [R19-21]. Khi trong đoạn có nhiều luật hay nhiều kết quả, nói rõ
   "điều này", "nó" chỉ cái gì bằng cách nhắc lại tên: "luật C", "kết quả này" [R19-22].
6. **Không chèn ý phụ** bằng gạch ngang dài "---" giữa câu hay ngoặc đơn dài; viết thành câu riêng. Gạch nối vẫn dùng
   cho khoảng giá trị và khung giờ (7:00–9:00, 30–120 giây). Ngoặc đơn chỉ dùng cho đơn vị, ký hiệu, tham chiếu bảng và
   tiếng Anh ở lần đầu.
7. **Nhấn mạnh tiết chế, định dạng theo ngữ nghĩa.** In nghiêng chỉ dùng cho thuật ngữ ở lần định nghĩa. In đậm chỉ dùng
   cho nhãn đầu đoạn và tiêu đề cột. Mỗi chương có nhiều nhất một hộp ghi nhớ (`khungy`), dành cho kết luận chính của
   chương. Không ép xuống dòng, thu phông hay đổi lề cho đủ trang; dùng đúng môi trường của mẫu UET [R19-1, R19-36].
8. **Tóm tắt** viết sau cùng, khi thân bài đã ổn định [R19-4]. Dài khoảng 250–300 tiếng, gồm ba đoạn: vấn đề; cách làm;
   kết quả chính. Phần kết quả có tối đa bốn con số; số nào cũng có mẫu số và phải khớp thân bài. Kèm một câu giới hạn.

### B. Thuật ngữ, ngôn ngữ, xưng hô

9. **Không có từ tiếng Anh trong câu tiếng Việt** [R19-27]. Tiếng Anh chỉ được xuất hiện ở bốn chỗ: trong ngoặc ở lần
   đầu một thuật ngữ; trong tên riêng (FleetPy, OR-Tools, Manhattan); trong tên bài ở danh mục tài liệu; trong tên hàm
   của giả mã. Không chuyển máy móc ngữ pháp tiếng Anh (thì, sở hữu cách, tính từ ghép) sang câu Việt [R19-24].
10. **Giới thiệu thuật ngữ theo mẫu**: tên tiếng Việt (tiếng Anh: …) + định nghĩa một câu + ví dụ. Sau đó chỉ dùng tên
    tiếng Việt (mục 1.12).
11. **Một khái niệm một tên**, theo `GLOSSARY-VI.md`. Không đổi tên giữa chừng cho đỡ lặp [R19-23]. Ví dụ, bản hiện
    tại có năm tên cho cùng một ý: "độ dời", "xê dịch", "xáo trộn", "dịch chuyển", "biến động".
12. **Chữ viết tắt** chỉ giữ chữ thật cần, định nghĩa ở lần đầu và đưa vào Danh mục. Tên các luật (C, U, M⁺, V, ghép tự
    do) được định nghĩa trong một bảng ở chương phương pháp. Chú thích của mỗi bảng kết quả nhắc lại nghĩa bằng lời.
13. **Không đưa vào thân bài**: tên lớp, tên hàm, trường dữ liệu, mã lỗi, tên cấu hình nội bộ (nobudget, b4, dl-120) và
    lịch sử thao tác (máy tính ngủ, chạy lại, ngày dựng bộ chạy, mã băm, giờ ghi kế hoạch). Lịch sử để trong hồ sơ nội
    bộ hoặc phụ lục [R19-18]. Tuy vậy, mục thiết lập thực nghiệm phải đủ để người khác đánh giá lại: dữ liệu, cách chọn
    mẫu, phiên bản phần mềm, cấu hình, cách so và cách tính chỉ số [R19-17]. Trong bảng, dùng tên đọc được, ví dụ "trần
    300 giây".
14. **Không dùng ẩn dụ khẩu ngữ hay từ dịch máy**: "bắn", "cắn đau", "ngốn", "đóng đinh", "món hời tồi", "mất trắng",
    "sụp", "hàng xóm gần nhất", "cấu hình điều trị", "thế giới trôi dạt". Viết thẳng nghĩa, giọng kỹ thuật trung tính,
    không thêm cảm xúc hay lời bình cá nhân [R19-24].
15. **Không dùng các từ đã bị loại**: "niêm phong", "tiền đăng ký" hay "preregistration", "dự đoán trước", "lời hứa có
    biên được chứng nhận", "cưỡng chế được", "văn liệu", "dòng bài", "quy trách", "nghĩa vụ phương tiện / kết quả".
    Thay nhãn bằng mô tả việc đã làm (`GLOSSARY-VI.md`, mục G).
16. **Chủ ngữ không xưng ngôi.** Như DACN (thân bài không có "chúng tôi", "chúng ta" hay "em" lần nào), chủ ngữ là đối
    tượng: "hệ thống", "bộ điều phối", "luật C", "thí nghiệm", "khóa luận", "đề tài", "chương này". Khi cần nói việc tác
    giả đã làm, viết "Khóa luận chạy lại …" hoặc dùng câu bị động tự nhiên ("… được ghi lại trước khi chạy"). Không dùng
    "chúng tôi" trong thân bài. "Em" chỉ dùng trong Lời cảm ơn. Bản hiện tại dùng "chúng tôi" khoảng 29 lần; thay hết.

### C. Công thức, ví dụ, bảng, giả mã, hình

17. **Công thức** đi theo bốn bước: câu dẫn → công thức đánh số → câu "Trong đó, …" giải thích mọi ký hiệu kèm đơn vị →
    một câu nói công thức dùng để làm gì (mục 1.3). Ký hiệu nào cũng được định nghĩa ở lần đầu xuất hiện, kèm miền giá
    trị [R19-7].
18. **Ít công thức.** Chỉ giữ công thức người đọc cần để hiểu các luật và cách đo. Chứng minh và mệnh đề phụ đưa sang
    phụ lục. Thân bài giữ phát biểu và một ví dụ số.
19. **Khái niệm khó nào cũng có ví dụ số cụ thể.** Ưu tiên một khách thật trong mô phỏng, có output gốc đi kèm (mẫu ở
    mục 3.3).
20. **Bảng.** Chỉ lập bảng khi bảng giúp hiểu hơn câu văn; vài số đơn giản thì viết trong câu, và không trình bày cùng
    một dữ liệu dưới ba dạng [R19-28]. Câu dẫn nói bảng trả lời câu hỏi gì. Bảng định nghĩa có cột "Ý nghĩa" hoặc "Vai
    trò" (mục 1.5). Bảng kết quả ghi đơn vị và mẫu số trong tiêu đề, không quá sáu cột, không ghép "a / b / c" vào một
    ô. Ô chưa đo ghi "chưa đo" hoặc "không áp dụng", không ghi 0 [R19-33]. Sau bảng có đoạn đọc bảng (mục 1.7).
21. **Giả mã.** Mọi dòng mô tả và chú thích viết bằng tiếng Việt (mục 1.6). Sau giả mã có một đoạn nói điều cốt lõi.
22. **Hình, chú thích, tham chiếu.**
    - Chú thích hình và bảng tự đủ nghĩa: chỉ đọc chú thích cũng biết đang so cái gì, trên tập nào, theo đơn vị nào. Chú
      thích không thêm kết luận mà hình không thể hiện [R19-30].
    - Hình ghi rõ trục, đơn vị, và ý nghĩa của thanh sai số nếu có [R19-31]. Phân biệt các nhóm bằng cả màu lẫn kiểu nét
      hoặc ký hiệu, để in đen trắng vẫn đọc được [R19-32]. Biểu đồ xuất dạng véc-tơ (PDF) [R19-37].
    - Hình, bảng, mục, công thức đều tham chiếu bằng `\ref`, không gõ số tay [R19-35]. Bản hiện tại còn gõ tay, ví dụ
      "công thức (2.5)" (`05-chuong1.tex:100`), "mục 2.4" (`07-chuong3.tex:185`), "mục 4.6" (`07-chuong3.tex:756`), "mục
      5.2" (`08-chuong4.tex:1703`).

### D. Số liệu

23. **Số viết kiểu Việt**: dấu phẩy cho phần thập phân, dấu chấm cho hàng nghìn (7,13; 3.672). Trong LaTeX dùng
    `$7{,}13$` như bản hiện tại.
24. **Mỗi tỉ lệ ở lần đầu kèm số đếm và mẫu số** [R19-15], ví dụ "2.338 khách được phục vụ trên 3.672 yêu cầu". Nói rõ đơn vị đếm
    (yêu cầu, khách, lần chạy, lượt quyết định, phương án, kịch bản) và không trộn các đơn vị. Ví dụ: 1.256 phương án bị
    loại không phải là 1.256 khách (`R17-FINAL-VERDICT.md:618`).
25. **Chênh lệch giữa hai tỉ lệ viết "điểm phần trăm"**, không viết "pp" hay "điểm %". Kèm số tuyệt đối, và tỉ lệ tương
    đối khi cần: "ít hơn 96 khách, tức 2,6 điểm phần trăm số yêu cầu (3,9% số khách của luật U)" (BAN-GIAO §5 điều 4).
26. **Đơn vị thời gian.** Thân bài viết "30 giây", "2 phút". Trong bảng dùng "s" và ghi đơn vị ở tiêu đề cột. Số giây lớn
    quy ra phút ở lần đầu, ví dụ "590 giây (gần 10 phút)".
27. **Làm tròn và nguồn gốc số liệu.** Thân bài làm tròn tỉ lệ đến một chữ số thập phân (hai chữ số nếu dưới 1%); bảng
    giữ số đầy đủ. Con số nào đưa vào luận văn cũng phải có script và output lưu lại (quy tắc của chủ nghiên cứu,
    BAN-GIAO:45). Mỗi hình, bảng và khẳng định thực chất truy được về tệp dữ liệu, mã tạo và output trong hồ sơ nội bộ
    [R19-9, R19-29]. Không tự điền số, cấu hình, nguồn hay trích dẫn còn thiếu; chỗ chưa kiểm ghi "chưa kiểm" trong hồ
    sơ, không đưa vào bản nộp [R19-8].
28. **Đoạn kết quả** đi theo thứ tự: con số → so với cái gì → nghĩa là gì với hành khách hoặc hãng xe → giới hạn nếu có
    (mục 1.7).

### E. So sánh, đánh đổi, giới hạn, khẳng định, trích dẫn

29. **So sánh** phải nói rõ so với luật nào, trên tập kịch bản nào, trong cùng điều kiện gì (mục 1.8). Chương nghiên
    cứu liên quan xếp theo cách tiếp cận (giới hạn khi chèn khách, hạn chót, hứa theo dự báo, …), so giả định, mục tiêu
    và điều kiện đánh giá; không nối các bản tóm tắt từng bài [R19-3].
30. **Đánh đổi** viết theo mẫu "được …, đổi lại …", và có số ở cả hai vế (mục 1.9).
31. **Khi nói về trễ hay đúng giờ**, luôn báo kèm tỉ lệ tới sớm và độ dài thêm của lời hứa (BAN-GIAO §5 điều 5). Lời hứa
    dài thì hết trễ, nhưng khi đó lời hứa mất nghĩa.
32. **Giới hạn: nói một lần, nhưng không xóa.**
    - Trong thân bài, mỗi kết quả chỉ có một câu giới hạn ngắn, đặt ngay sau kết quả. Không lặp cùng một lời rào ở mọi
      đoạn.
    - Không xóa một điều kiện thật chỉ để câu nghe mạnh hơn ("trên các kịch bản đã chạy", "trong mô phỏng"). Rút gọn
      thì phải giữ nguyên số liệu, phủ định và điều kiện [R19-11, R19-26].
    - Kết luận chỉ áp cho môi trường đã đánh giá: mô phỏng FleetPy, dữ liệu Manhattan, quy mô 108 yêu cầu và 8 xe. Không
      suy ra hiệu quả vận hành thật ở mọi thành phố [R19-16].
    - Giữ kết quả âm tính hoặc chưa kết luận được nếu chúng thay đổi phạm vi kết luận, ví dụ dự báo đưa vào bộ điều phối
      bị bác, học máy không cải thiện [R19-14].
    - Giới hạn chung gom vào một mục cuối chương thực nghiệm và một mục trong kết luận. Mỗi giới hạn một đoạn ngắn: điều
      gì chưa làm → ảnh hưởng tới kết luận nào (mục 1.10).
33. **Không viết quan hệ nhân quả** khi dữ liệu chỉ cho phép phân rã hoặc thấy hai đại lượng cùng thay đổi [R19-13].
    Viết "theo sổ cái, phần do điều phối bằng 73,4% …", không viết "điều phối gây ra 73,4% …" (BAN-GIAO §5 điều 6).
    Động từ phải tương xứng với bằng chứng: "quan sát", "ước lượng", "đo được" cho kết quả mô phỏng; "chứng minh" chỉ
    dùng cho định lý [R19-12]. Lời giải thích chưa kiểm phải ghi rõ "một cách giải thích khả dĩ, chưa kiểm riêng".
34. **Không tự khen** [R19-25]. Không dùng "duy nhất", "đầu tiên", "bền nhất", "quan trọng nhất", "vượt trội", "đột
    phá", "hóa ra", "đáng chú ý là" khi không có phép so đi kèm. Không gọi là mới những gì
    `docs/03-related-work-and-claim-boundary.md` và BAN-GIAO §3 ghi là đã có: chèn động, giới hạn giờ đến, gán lại,
    tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, hài lòng của khách, hứa theo dự báo, học máy đoán giờ đến.
    Nêu một đóng góp trung tâm, đúng phạm vi "Đóng góp được phép nhận" (BAN-GIAO:124-135) [R19-2].
35. **Trích dẫn.**
    - Số [n] đặt ngay sau tên tác giả hoặc sau ý vay mượn. Hai tác giả viết "Fielbaum và Alonso-Mora [n]"; từ ba tác giả
      viết "Elmi và cộng sự [n]".
    - Câu trích tiếng Anh thì dịch sang tiếng Việt trong câu. Nguyên văn để ở chú thích, kèm mục hoặc trang của bài.
    - Chỉ trích điều đã đọc toàn văn; nếu mới đọc phần tóm tắt thì ghi rõ. Mở đúng đoạn, trang hay bảng ủng hộ câu đang
      viết: nguồn tồn tại và DOI đúng chưa chứng minh nguồn nói điều đó [R19-10].
    - Kiểm tác giả, năm, tên bài, phiên bản và DOI ngay khi thêm nguồn; ưu tiên bản đã công bố hơn bản tiền ấn [R19-34].
    - Phải trích Hörl và Zwick (2022), Leonardi và cộng sự (2024), Ding và cộng sự (BAN-GIAO §5 điều 13).
    - Danh mục tài liệu chia hai phần "Tiếng Việt" và "Tiếng Anh" như DACN (tr. 37).

---

## 3. Ba đoạn mẫu cho RideBound, viết theo lối DACN

Các số dưới đây chép từ BAN-GIAO. Trước khi đưa vào luận văn phải đối chiếu với output gốc và kiểm lại mẫu số (quy tắc
27). Ba đoạn chỉ minh họa cách viết, không phải văn bản chốt.

### 3.1 Mở bài: vấn đề → hạn chế → cách làm

> Trong dịch vụ đi chung xe, hệ thống báo cho mỗi hành khách một giờ trả ngay khi xác nhận chuyến. Sau đó, giờ này có
> thể đổi vì ba lý do: bộ điều phối ghép thêm khách vào xe, tắc đường tăng theo quy luật quen thuộc của giờ cao điểm, và
> tắc đường bất ngờ. Các hệ thống điều phối kinh điển, như của Alonso-Mora và cộng sự [1], chỉ giới hạn thời gian chờ và
> độ trễ tối đa của từng khách. Trong giới hạn đó, giờ đã báo có thể đổi nhiều lần. Một số công trình gần đây đã đặt
> giới hạn trực tiếp lên lời hứa (mục 1.3). Khóa luận xử lý mỗi lý do ở một chỗ riêng: luật C giới hạn tổng thay đổi do
> điều phối trên giờ trả của từng khách; lời hứa theo dự báo cộng sẵn mức tắc đường thường gặp vào giờ hứa đầu; sổ cái
> ghi lại phần thay đổi còn lại cho từng khách.

Nguồn ý: BAN-GIAO:90-95; `05-chuong1.tex:25-27` (hệ kinh điển giới hạn thời gian chờ Ω và độ trễ Δ);
`05-chuong1.tex:115-148` (các công trình gần đây).

### 3.2 Đoạn kết quả: số, so với gì, nghĩa là gì

> Trên 3.672 yêu cầu của 34 kịch bản kiểm tra, luật U chở được 2.434 khách, còn luật C với trần 30 giây chở được 2.338
> khách. Như vậy, luật C mất 96 khách, tức 2,6 điểm phần trăm số yêu cầu (3,9% số khách của luật U). Đổi lại, tỉ lệ khách
> tới nơi muộn hơn lời hứa đầu quá 1 phút giảm từ 8,34% xuống 3,25%. Với luật C, tỉ lệ khách tới sớm quá 1 phút chỉ là
> 0,13%. Không khách nào của luật C trễ quá 5 phút, trong khi với luật U tỉ lệ này là 0,74%.

Nguồn số: BAN-GIAO:166, :180, :192-196, :302. **Phải kiểm trước khi dùng.** BAN-GIAO có hai con số khác nhau cho "trễ
quá 1 phút" của luật U: 9,1% ở dòng :187 và 8,34% ở dòng :194, theo hai cách tính khác nhau. Phải ghi rõ mẫu số và cách
gộp (theo khách hay trung bình theo kịch bản; BAN-GIAO §5 điều 7), và không trộn hai bảng trong cùng một câu.

### 3.3 Ví dụ một khách thật trong mô phỏng

> Ví dụ, trong mô phỏng ngày 15/11/2018, một hành khách đặt xe lúc 7:11:56 và được báo sẽ tới nơi lúc 7:34:51. Xe đón
> khách lúc 7:22:30 và trả khách lúc 7:38:02, muộn 190,5 giây so với lời hứa. Phần trễ này đến từ tắc đường tăng lúc 7:15
> và 7:30. Nếu lúc hứa hệ thống cộng sẵn mức tăng tắc đường thường gặp của khung giờ này, giờ hứa sẽ là 7:37:44, chỉ lệch
> 17,6 giây so với giờ tới thật.

Nguồn: BAN-GIAO:290-294, dẫn tới `optimize/report-extras/example-rider-2026-10-06.txt`, kịch bản d20181115-s10-r1-w07.

---

## 4. Bản hiện tại vi phạm ở đâu: 12 ví dụ và bản viết lại

### 4.0 Bức tranh chung (đếm bằng grep, phần tiếng Việt của Tóm tắt và Chương 1–5)

- **Thuật ngữ lạ, lặp nhiều**: "trôi dạt" 106 lần; "panel" 74; "cổng" 65; "vô nghiệm" 55; "bất biến" 42; "niêm phong"
  36; "thăm dò" 34; "văn liệu" 31; "kỷ nguyên" 19; "ratchet" 19; "noop" 19 (chỉ số trong công thức); "pp" 16 (đều ở
  Chương 4); "tiền đăng ký" 12; "cưỡng chế" 13; "quy trách" 11; "CVaR" 6.
- **Một vai, nhiều tên**: "nhà điều hành" 29 lần, "bộ điều phối" 15, "nhà xe" 6, "điều phối viên" 1.
- **Một từ, nhiều nghĩa**: "khung" khoảng 124 lần, dùng cho khung giờ, khung so sánh, khung tin, khung quyết định.
- **Nhấn mạnh dày đặc** ở Chương 1–5: `\emph` 309 lần, `\textbf` 354 lần (283 lần ở Chương 4), gạch ngang dài "---" 247
  lần.
- **Lịch sử thao tác trong thân bài** (vi phạm quy tắc 13):
  - `08-chuong4.tex:612-615` (bộ chạy dựng ngày 22/8, tính năng vào mã ngày 4/9);
  - `08-chuong4.tex:1025-1028` (năm lần chạy hỏng vì máy tính ngủ);
  - `08-chuong4.tex:1189-1190` ("trùng từng frame").
- **Số liệu không khớp** (phát hiện khi đọc, cần sửa dù không phải chuyện văn phong):
  - Tóm tắt (`02-tom-tat.tex:28`) và Chương 5 (`09-chuong5.tex:34`) ghi "546 lần chạy thăm dò sau đó".
  - Bảng `bang:quymo` ghi "Cộng, thăm dò sau đó: 685" (`08-chuong4.tex:109`). Các dòng của bảng cộng lại đúng 685.
  - Lời cảm ơn ghi "hơn năm trăm lần chạy mô phỏng" (`01-loi-cam-on.tex:16`), trong khi bảng ghi tổng 1.243.

### 4.1 Tóm tắt nhồi số và nhãn: `02-tom-tat.tex:27-43`

**Nguyên văn (lược bớt):** «Phần thực nghiệm dùng dữ liệu chuyến đi công khai của Manhattan và nền mô phỏng FleetPy, gồm
558 lần chạy trên một panel 20 ô đã niêm phong, cùng 546 lần chạy thăm dò sau đó. […] Một thí nghiệm thăm dò có tiền đăng
ký kiểm thêm hai họ hạn chót, với dự đoán theo từng ô niêm phong trước khi chạy các nhánh được dự đoán: dự đoán đúng ở
$98/102$ cặp trên panel chính và ở $31/32$, $40/40$ cặp trên khung sáng và khung tối của một tập giữ lại; […]»

**Vấn đề:** một đoạn khoảng 600 tiếng với hơn 20 con số; nhãn "panel", "niêm phong", "tiền đăng ký", "nhánh", "họ hạn
chót"; số 546 không khớp bảng. Vi phạm quy tắc 4, 5, 8, 9, 15, 24.

**Viết lại (giữ ba con số chính của chính đoạn này):**
> Thực nghiệm dùng dữ liệu chuyến taxi công khai của Manhattan và bộ mô phỏng FleetPy. Khi bộ điều phối không bị giới
> hạn, phần độ dời do chính nó gây ra bằng 89,06% tổng độ dời giờ hẹn mà hành khách thấy. Trần 30 giây cho phần này đưa
> tỉ lệ đó xuống 1,37%, đổi lại tỉ lệ khách được phục vụ giảm 7,13 điểm phần trăm. Khi đưa tắc đường đo thật vào mô
> phỏng, luật tính theo độ dời khách thấy bị kẹt ở 19 trên 20 kịch bản. Luật chỉ tính phần do điều phối không lần nào bị
> chính nó làm kẹt, dù 11 kịch bản vẫn dừng vì điều kiện kiểm tra giờ đón của mô hình. Các kết quả có tắc đường là kết
> quả thăm dò.

**Ghi chú:** bản mới sẽ có kết quả khác (luật C, dự báo, sổ cái). Đoạn này chỉ minh họa hình thức. Không bỏ câu "11 kịch
bản vẫn dừng", vì bỏ nó thì kết quả bị nói quá.

### 4.2 Biệt ngữ khi nêu hạn chế: `05-chuong1.tex:53-56`

**Nguyên văn:** «Để xác định chính xác chỗ đứng của khóa luận, chúng tôi đã khảo sát mười bốn trục văn liệu liên quan. Từ
đó rút ra bốn hạn chế mang tính hệ thống của dòng bài điều phối kinh điển, không phải những thiếu sót ngẫu nhiên của một
bài cụ thể; các ngoại lệ gần đây được bàn riêng ở mục \ref{muc:chodung}.»

**Vấn đề:** "trục văn liệu", "dòng bài"; câu phòng thủ ("không phải những thiếu sót ngẫu nhiên"). Vi phạm quy tắc 14, 15.

**Viết lại:**
> Khi nhìn từ phía lời hứa với hành khách, các hệ thống điều phối đi chung xe kinh điển có chung bốn hạn chế. Mục này nêu
> từng hạn chế kèm một ví dụ. Các công trình gần đây đã khắc phục một phần được bàn riêng ở mục 1.3.

### 4.3 Lời rào về chính bài viết: `05-chuong1.tex:87-88`

**Nguyên văn:** «Trước khi trình bày đóng góp, cần nói rõ ranh giới với ba công trình gần nhất, vì phần chồng lấn là đáng
kể và việc giấu nó đi sẽ chỉ làm người đọc tự phát hiện ra ở chương sau.»

**Vấn đề:** câu nói về động cơ của người viết, không đưa thông tin. Vi phạm quy tắc 2, 34.

**Viết lại:**
> Bốn công trình gần nhất với khóa luận là Hörl và Zwick [n], Fielbaum và Alonso-Mora [n], Elmi và cộng sự [n], và Schulz
> và Pfeiffer [n]. Với mỗi công trình, mục này nêu điều khóa luận kế thừa và điều khóa luận làm khác.

**Ghi chú:** bản hiện tại chưa trích Hörl và Zwick (2022), trong khi chiến lược B của bài này gần với luật C
(BAN-GIAO:145-147, §5 điều 13).

### 4.4 Trích tiếng Anh giữa câu, chi tiết ngày tháng: `05-chuong1.tex:123-126`

**Nguyên văn:** «Họ viết rằng một lời bảo đảm như vậy ``would not be possible if even a single change were allowed''. Mạng
của họ có thời gian đi trên mỗi cung cố định, nên không có phần trôi dạt nào để tách khỏi phần do quyết định. Bài được
nhận ngày 16/1/2026, chấp nhận ngày 24/7/2026 và công bố trực tuyến ngày 4/8/2026; hai công trình được thực hiện song
song.»

**Vấn đề:** câu tiếng Anh nằm giữa câu tiếng Việt; "trôi dạt", "phần do quyết định"; ngày nhận, ngày chấp nhận không giúp
người đọc. Vi phạm quy tắc 9, 13, 35.

**Viết lại:**
> Các tác giả nhận xét rằng không thể có lời bảo đảm như vậy nếu cho phép dù chỉ một lần thay đổi.¹ Trong mô hình của họ,
> thời gian đi trên mỗi đoạn đường là cố định, nên không có phần thay đổi do tắc đường cần tách khỏi phần do điều phối.
>
> ¹ Nguyên văn: "would not be possible if even a single change were allowed" (Elmi và cộng sự [n], mục …). Hai công
> trình được thực hiện song song; bài của Elmi và cộng sự công bố trực tuyến ngày 4/8/2026.

### 4.5 "Niêm phong", "tiền đăng ký": `05-chuong1.tex:184-188`

**Nguyên văn:** «Và phần đối chiếu là một thí nghiệm \emph{thăm dò có tiền đăng ký} (mục \ref{muc:tang2}): dự đoán theo
từng ô được niêm phong trước khi chạy các nhánh được dự đoán, đúng ở $98/102$ cặp trên panel chính và ở $31/32$, $40/40$
cặp trên một tập giữ lại chưa từng dùng để dựng quy tắc dự đoán; các lần chạy có trôi dạt không qua bộ kiểm chứng của dự
án.»

**Vấn đề:** dùng nhãn thay cho mô tả việc đã làm; "ô", "panel", "nhánh"; một câu bốn ý. Vi phạm quy tắc 5, 9, 15.

**Viết lại:**
> Phần đối chiếu với mô phỏng là một thí nghiệm thăm dò. Kết quả mong đợi của từng kịch bản được ghi lại trước khi chạy
> (bản ghi để ở Phụ lục C). Kết quả mong đợi khớp ở 98 trên 102 cặp so sánh của
> tập kịch bản chính. Trên một tập kịch bản riêng, chưa dùng khi lập quy tắc, kết quả khớp 31 trên 32 cặp buổi sáng và
> 40 trên 40 cặp buổi tối. Các lần chạy có tắc đường chưa qua bộ kiểm tra tự động của dự án.

### 4.6 Nhãn tiếng Anh cho ba mốc: `07-chuong3.tex:82-87` (và `04-viet-tat.tex:38-46`)

**Nguyên văn:** «$v$ --- \textbf{previous}: lời hứa đã công bố lần gần nhất cho hành khách; $e$ --- \textbf{exogenous}:
chính kế hoạch đó, chiếu lại từ vị trí thật hiện tại của xe. […] $p$ --- \textbf{proposed}: lời hứa mà phương án đang xét
sẽ tạo ra.» Danh mục ký hiệu còn ghi «(\emph{conduct}, \texttt{decisionInduced})», «(\emph{outcome},
\texttt{customerVisible})».

**Vấn đề:** nhãn tiếng Anh in đậm; tên biến trong mã ở Danh mục ký hiệu. Vi phạm quy tắc 9, 13.

**Viết lại:**
> Ở mỗi lượt quyết định, với mỗi khách đã có lời hứa, hệ thống so ba mốc giờ trả:
> - v: giờ trả đã báo cho khách ở lần gần nhất;
> - e: giờ trả tính lại nếu xe giữ nguyên kế hoạch cũ, xuất phát từ vị trí hiện tại với tốc độ hiện tại;
> - p: giờ trả mới nếu chọn phương án đang xét.
>
> Hiệu e − v là phần thay đổi khi giữ nguyên kế hoạch, hiệu p − e là phần do điều phối, và hiệu p − v là phần khách thấy.

**Ghi chú:** chỉ gọi e − v là "phần do tắc đường" khi thiết lập bảo đảm xe chạy đúng kế hoạch và dừng đón trả 0 giây
(BAN-GIAO:119-122). Bản hiện tại nói rõ rằng trên tập 20 kịch bản cũ, phần này còn gồm tiến độ thực của xe và độ trễ
thực thi (`07-chuong3.tex:267-274`). v là "lời hứa đã công bố trước", không phải "lời hứa đầu chỉ bị dời bởi tắc đường"
(BAN-GIAO §5 điều 14).

### 4.7 Tên lớp và hàm trong thân bài: `07-chuong3.tex:103-106`

**Nguyên văn:** «Cài đặt tính $A = |p - e|$ theo đúng trị tuyệt đối (\texttt{PromiseDeltaCalculator}, hàm
\texttt{AbsoluteDifference}): một quyết định kéo lời hứa \emph{sớm} hơn mốc không-làm-gì cũng bị tính phí bằng đúng độ
lệch đó, giống hệt một quyết định đẩy muộn. Không có quy ước một chiều nào trong mã.»

**Vấn đề:** tên lớp, tên hàm; "mốc không-làm-gì"; "tính phí". Vi phạm quy tắc 13, 19.

**Viết lại:**
> Phần do điều phối được tính theo độ lớn, không theo chiều. Kéo giờ trả sớm hơn 20 giây hay đẩy muộn hơn 20 giây đều
> làm tổng độ dời do điều phối của khách tăng 20 giây.¹
>
> ¹ Cách tính nằm trong lớp `PromiseDeltaCalculator` (Phụ lục B).

### 4.8 Lời rào nối tiếp và chữ "duy nhất": `07-chuong3.tex:534-542`

**Nguyên văn (lược bớt):** «Câu phát biểu chính xác là: \emph{cổng hành vi không bao giờ là nguyên nhân khiến tập phương
án rỗng}. Nói chặt hơn, phần (a) chứng minh rằng cổng $C$ không bao giờ loại phương án không làm gì; ``không bao giờ là
nguyên nhân'' là cách diễn đạt điều đó: […] Câu ``hệ thống dùng cổng hành vi không bao giờ kẹt'' là \emph{sai} --- 11 trên
20 ô ở trên là phản ví dụ. Tính ``duy nhất'' cũng phải đọc đúng phạm vi. […]»

**Vấn đề:** cùng một ý được nói lại ba lần, lần sau lại rào lần trước; "cổng", "tập phương án rỗng", "phương án không làm
gì". Vi phạm quy tắc 11, 15, 32, 34.

**Viết lại:**
> Luật C không bao giờ loại phương án giữ nguyên kế hoạch, vì phương án này không thêm độ dời do điều phối nào. Vì vậy,
> nếu một xe hết phương án hợp lệ thì nguyên nhân nằm ở một điều kiện khác, không ở luật C. Điều này không có nghĩa là
> hệ thống dùng luật C không bao giờ dừng: dưới tắc đường đo thật buổi sáng, 11 trên 20 kịch bản vẫn dừng vì điều kiện
> kiểm tra giờ đón (mục 4.x).

### 4.9 Từ tiếng Anh, lời rào trong ngoặc, động từ nhân quả: `08-chuong4.tex:173-178`

**Nguyên văn:** «Con số $89{,}06\%$ là kết quả chính của mục này. Nó nói rằng trong một hệ ride-pooling tối ưu liên tục
theo lối kinh điển, phần do hệ thống tự tạo ra \emph{bằng} gần chín phần mười lượng bất định mà hành khách trải nghiệm về
giờ giấc (một tỉ số, xem cách phát biểu ở cuối mục này). Và vì bộ sinh phương án chỉ chèn thêm, toàn bộ 74.443 giây đó là
dịch chuyển theo hướng xấu đi --- không có lần nào tốt lên.»

**Vấn đề:** "ride-pooling"; ngoặc đơn chỉ người đọc tới chỗ khác; "lượng bất định", "dịch chuyển". Vi phạm quy tắc 6, 9,
11, 33.

**Viết lại:**
> Với luật không giới hạn (B1), tổng độ dời do điều phối là 74.443 giây, bằng 89,06% tổng độ dời giờ hẹn mà hành khách
> thấy (83.587 giây, Bảng 4.x). Đây là tỉ số giữa hai tổng, không phải phép đo nhân quả. Vì bộ sinh phương án chỉ chèn
> thêm điểm dừng, lần dời nào do điều phối cũng làm giờ trả muộn đi.

**Ghi chú:** 74.443 và 83.587 lấy từ chính bảng `bang:quytrach` (`08-chuong4.tex:164-165`). Cách nói "bằng … một tỉ số"
theo đúng lưu ý của bản hiện tại ở `08-chuong4.tex:324-327`.

### 4.10 Tên cấu hình nội bộ, "pp", "ngốn": `08-chuong4.tex:366-368`

**Nguyên văn:** «\textbf{Phần đắt nhất là quyết định cam kết chút nào đó.} Bước từ B1 sang nobudget --- chỉ khóa danh tính
xe và hai điểm dừng, chưa hứa một chữ nào về thời gian --- đã ngốn $3{,}70$ điểm phần trăm, tức hơn nửa tổng chi phí
$7{,}13$ pp.»

**Vấn đề:** tên cấu hình "nobudget"; "pp"; "ngốn"; câu nhãn khó hiểu ("cam kết chút nào đó"). Vi phạm quy tắc 13, 14, 25.

**Viết lại:**
> **Phần lớn cái giá nằm ở bước đầu tiên.** Chỉ cần khóa xe và hai điểm dừng sau khi xác nhận, chưa đặt trần nào cho giờ
> trả, tỉ lệ phục vụ đã giảm 3,70 điểm phần trăm so với B1. Mức này bằng hơn một nửa mức giảm 7,13 điểm phần trăm của
> cấu hình chặt nhất (trần 30 giây).

Trong bảng `bang:thang1`, đổi tên dòng "nobudget" thành "Chỉ khóa xe và điểm dừng", "budget300" thành "Trần 300 giây".

### 4.11 Ẩn dụ khẩu ngữ, giải thích nhân quả chưa kiểm: `08-chuong4.tex:1612-1615`, `1676-1680`, `1688-1689`

**Nguyên văn:**
- «Cơ chế tương đối rõ: cửa sổ rộng hơn cho bộ tối ưu nhiều lựa chọn hơn, nên cũng nhiều cơ hội dời lời hứa hơn, và trần
  vì thế cắn đau hơn.»
- «Phép đo chất lượng dịch vụ đóng đinh thêm một điểm nữa. […] Với hệ số định giá ở mục 2.5, đây là một món hời tồi, và
  hướng nới cửa sổ đồng loạt bị loại bỏ.»
- «Đây là bất biến \emph{miền} chứ không phải chính sách --- nó bắn bất kể cơ sở tính nào đang dùng, bất kể nguyên nhân
  gì.»

**Vấn đề:** "cắn đau", "đóng đinh", "món hời tồi", "bắn"; câu đầu khẳng định cơ chế ("tương đối rõ") khi chưa có thí
nghiệm tách riêng. Vi phạm quy tắc 14, 15, 33.

**Viết lại:**
> Một cách giải thích khả dĩ, chưa được kiểm riêng: cửa sổ đón rộng hơn cho bộ điều phối nhiều phương án hơn, nên có nhiều
> phương án muốn dời lời hứa hơn; trần chặn các phương án đó, vì vậy số khách mất đi tăng lên.
>
> Kết quả về thời gian chờ cũng không ủng hộ việc nới cửa sổ: […]. Với các hệ số định giá ở mục 2.5, cái giá này lớn hơn
> lợi ích, nên khóa luận không theo hướng nới cửa sổ cho mọi khách.
>
> Đây là một điều kiện kiểm tra của mô hình dữ liệu, không phải một luật điều phối. Điều kiện này báo lỗi với mọi luật,
> bất kể vì sao xe đến muộn.

### 4.12 Tự đánh giá, so sánh lạc đề: `09-chuong5.tex:62`, `09-chuong5.tex:215-216`, `06-chuong2.tex:164-166`

**Nguyên văn:**
- «Ngoài ra, khóa luận ghi nhận bốn kết quả phụ mà chúng tôi cho là đáng chú ý.»
- «Đóng góp mà chúng tôi tin là bền nhất của khóa luận không phải một con số cụ thể, mà là một cách đặt vấn đề.»
- «Phân biệt giữa hai cơ sở tính sổ cái […] hóa ra trùng với một phân biệt cổ điển trong luật nghĩa vụ, và việc nêu nó ra
  giúp kết quả kỹ thuật có chỗ đứng khái niệm rõ ràng hơn.»

**Vấn đề:** người viết tự chấm điểm ("đáng chú ý", "bền nhất"); "hóa ra"; một mục về luật dân sự lạc khỏi câu chuyện
chính. Vi phạm quy tắc 15, 16, 34.

**Viết lại:**
> Ngoài ba kết quả chính, thực nghiệm còn cho bốn kết quả phụ.
>
> Khóa luận đã trình bày luật C, một trần cho tổng thay đổi do điều phối trên giờ trả của từng khách, cùng sổ cái tách
> nguyên nhân thay đổi lời hứa. Hai cơ chế này được đánh giá trên mô phỏng FleetPy với dữ liệu chuyến taxi của Manhattan.

Phần so sánh với luật nghĩa vụ: nếu giữ, rút thành một câu so sánh trong Chương 2, không dành cả một mục.

### 4.13 Những điều bản hiện tại làm tốt: nên giữ

- `05-chuong1.tex:21-24`: ví dụ «xe sẽ đón bạn lúc 9 giờ 10», rồi «9 giờ 13, rồi 9 giờ 11, rồi 9 giờ 16». Cụ thể, đúng
  lối DACN.
- `07-chuong3.tex:121-149`: ví dụ ba mốc với bảng nhỏ 9:10:00 / 9:10:40 / 9:11:10 và phép tính 30 giây so với 70 giây.
  Đây là mẫu tốt cho quy tắc 19.
- `08-chuong4.tex:222-226`: «Ba điều đọc được từ bảng này. Thứ nhất, …». Đoạn đọc bảng đúng quy tắc 20 và 28.
- `08-chuong4.tex:1583-1588`: phân biệt «phương án bị loại» với «hành khách bị từ chối». Đúng quy tắc 24.
- `08-chuong4.tex:1260-1265`: tên kiểu tắc đường dễ hiểu («Một cú sốc», «Sốc lặp», «Tắc giảm dần», «Ngày đo thật
  12/11»).
- `08-chuong4.tex:1080`: «Kết quả trên không được đọc là cơ chế của khóa luận tốt hơn cơ chế của họ.» Giới hạn nói trong
  một câu, đúng quy tắc 32.
- Cách viết số kiểu Việt trong LaTeX, ví dụ `$80{,}32\%$` (`08-chuong4.tex:161`).

---

## 5. Đối chiếu với 37 quy tắc R19 của Codex

Nguồn: `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R19-SKILLS-REVIEW.md`, bảng "37
quy tắc đã chắt lọc" (dòng 26–64), rút từ sáu kho kỹ năng viết trên GitHub. Cả 37 quy tắc đều đã được gộp vào 35 quy tắc
ở mục 2; không quy tắc nào bị bỏ hẳn.

### 5.1 Quy tắc R19 nằm ở đâu trong hướng dẫn này

| R19 | Nội dung ngắn | Quy tắc ở mục 2 |
|---|---|---|
| 1 | Theo mẫu đã chọn (UET/VNU) | 7 |
| 2 | Một đóng góp trung tâm, có phạm vi | 34 |
| 3 | Nghiên cứu liên quan xếp theo cách tiếp cận | 29 |
| 4 | Viết tóm tắt sau cùng | 8 |
| 5 | Chương nào cũng phục vụ lập luận chung | 1 |
| 6 | Giải thích cho người học tin học chưa biết hệ thống | 3 |
| 7 | Định nghĩa ký hiệu ở lần đầu | 17 |
| 8 | Không tự điền dữ kiện thiếu | 27 |
| 9 | Khẳng định gắn với bằng chứng | 27 |
| 10 | Mở đúng đoạn nguồn ủng hộ câu viết | 35 |
| 11 | Giữ điều kiện bất định có căn cứ | 32 |
| 12 | Động từ tương xứng với bằng chứng | 33 |
| 13 | Không suy nhân quả từ hai đại lượng cùng thay đổi | 33 |
| 14 | Giữ kết quả âm tính quan trọng | 32 |
| 15 | Đơn vị, mẫu số, tập đánh giá | 24 |
| 16 | Kết luận chỉ áp cho môi trường đã đánh giá | 32 |
| 17 | Phương pháp đủ để đánh giá lại | 13 |
| 18 | Lịch sử lựa chọn để trong hồ sơ nội bộ | 13, bản viết lại 4.5 |
| 19, 20 | Một đoạn một ý, ý chính đầu đoạn | 4 |
| 21, 22 | Chủ ngữ gần động từ; rõ đại từ | 5, 16 |
| 23 | Một khái niệm một thuật ngữ | 11 |
| 24 | Giọng kỹ thuật trung tính | 9, 14 |
| 25 | Bỏ lời tán dương | 34 |
| 26 | Rút gọn mà giữ nội dung có căn cứ | 32 |
| 27 | Câu giải thích hoàn toàn bằng tiếng Việt | 9 |
| 28 | Chỉ lập bảng hay hình khi cần | 20 |
| 29 | Hình, bảng truy được về dữ liệu | 27 |
| 30, 31, 32 | Chú thích tự đủ nghĩa; trục, đơn vị; in đen trắng đọc được | 22 |
| 33 | Ô thiếu không ghi 0 | 20 |
| 34 | Kiểm thông tin thư mục | 35 |
| 35 | Tham chiếu bằng `\ref` | 22 |
| 36 | Định dạng theo ngữ nghĩa LaTeX | 7 |
| 37 | Hình dạng véc-tơ | 22 |

### 5.2 Chỗ hai nguồn khác nhau, và cách đã chọn

Nguyên tắc chung: khi R19 và DACN khác nhau về độ tự nhiên của câu tiếng Việt, theo DACN. Khi R19 nói về tính trung thực
của bằng chứng, theo R19.

1. **Xưng hô.** R19-21 chỉ dặn "không biến mọi câu thành 'chúng tôi'", tức vẫn cho phép đôi khi dùng. Thân bài DACN không
   dùng "chúng tôi" lần nào, và chủ nghiên cứu muốn chủ ngữ không xưng ngôi. **Chọn DACN**: thân bài không dùng "chúng
   tôi" (quy tắc 16).
2. **Độ dài đoạn.** R19-19 dặn không chia đoạn theo số chữ cố định. Hướng dẫn này đưa mức 60–150 tiếng lấy từ DACN.
   **Dung hòa**: con số chỉ là mức tham khảo; tách đoạn theo ý (quy tắc 4).
3. **Lời rào đón.** R19-11 và R19-26 dặn không xóa điều kiện có căn cứ. Chủ nghiên cứu lại không muốn rào đón dài, và
   DACN nêu giới hạn một hai câu (mục 1.10). **Dung hòa**: giữ mọi điều kiện thật, nhưng nói mỗi điều kiện một lần, đúng
   chỗ (quy tắc 32).
4. **Gạch ngang dài.** R19 (phần nhận xét kho humanizer, dòng 102) cho rằng cấm mọi gạch dài không phải quy tắc khoa học
   phổ quát. DACN dùng gạch trong cụm ghép ("hành khách–tài xế", tr. 20) và khoảng số. Văn xuôi của DACN cũng có hai chỗ
   dùng gạch để chèn ý: «2 đến 8 thành viên - quy mô phổ biến nhất» (tr. 3) và chú thích Hình 2.1 (tr. 12). Bản hiện tại
   dùng "---" 247 lần ở Chương 1–5. **Chọn**: giữ quy tắc 6 như một lựa chọn để dễ đọc cho riêng khóa luận này, không
   coi là luật chung. Gạch nối cho khoảng giá trị vẫn dùng bình thường.
5. **Thứ tự viết trước rồi chạy (trước gọi là "tiền đăng ký").** R19-18 dặn để lịch sử trong hồ sơ nội bộ, không kể
   chuyện tiền đăng ký trong thân bài. R19 dòng 66 thêm rằng yêu cầu này "không cho phép giấu giới hạn phương pháp".
   Việc kết quả mong đợi được ghi trước hay sau khi chạy làm thay đổi cách đọc kết quả. **Dung hòa**: trong mục thiết lập
   thực nghiệm, viết một câu thường ("Kết quả mong đợi được ghi lại trước khi chạy"). Thời điểm, mã băm và bản ghi đưa
   vào phụ lục. Không dùng chữ "niêm phong" hay "tiền đăng ký" (quy tắc 13, 15; bản viết lại 4.5).
6. **Mức chi tiết của phương pháp.** R19-17 đòi đủ chi tiết để đánh giá lại, còn quy tắc 13 cấm tên lớp và lịch sử thao
   tác trong thân bài. **Dung hòa**: thân bài nêu dữ liệu, phiên bản, cấu hình và cách tính bằng lời; tên mã và đường dẫn
   để ở phụ lục.
7. **Văn bản nguồn của R19** là quy tắc viết tiếng Anh cho bài báo. Bản thân R19 đã ghi rằng các quy tắc về thì, sở hữu
   cách, viết tắt và chỉ tiêu số trích dẫn không chuyển nguyên sang tiếng Việt (R19 dòng 82, 90, 108). Hướng dẫn này
   không lấy các chỉ tiêu đó.
