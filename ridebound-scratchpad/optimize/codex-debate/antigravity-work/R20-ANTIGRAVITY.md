# Đánh giá Đề cương Tái cấu trúc Luận văn RideBound (Vòng 20)

**Người đánh giá:** Antigravity (Gemini 3.8 Flash, high)  
**Thời điểm:** 2026-10-10  
**Tài liệu thẩm định:**
- `inputs-r20/OUTLINE-PROPOSAL-CLAUDE.md` (Đề cương đề xuất rút gọn luận văn từ 105 trang xuống ~74 trang, viết ngày 2026-10-10)
- `inputs-r20/main.pdf` (Bản luận văn hiện tại 105 trang, ngày 30/09/2026)
- `inputs-r20/23020155_TranQuangThanh_Bao cao DACN.pdf` (Báo cáo môn Dự án công nghệ 50 trang của tác giả Trần Quang Thành, ThS. Trần Mạnh Cường hướng dẫn)

---

## Phần 1. Giảng viên trong Hội đồng Chấm luận văn (UET, ngành CNTT)

Dưới góc nhìn của một giảng viên chấm phản biện tại Trường Đại học Công nghệ (ĐHQGHN), chuyên ngành Công nghệ thông tin / Hệ thống thông tin, tôi đánh giá bản đề cương tái cấu trúc luận văn `OUTLINE-PROPOSAL-CLAUDE.md` theo các tiêu chí học thuật chuẩn mực của Nhà trường.

---

### 1.1. Đánh giá tính rõ ràng của cấu trúc học thuật

1. **Bài toán (Problem): Rõ ràng, có ý nghĩa thực tiễn cao.**
   - Đề cương đã xác định chuẩn xác bài toán: Trong dịch vụ xe đi chung (ride-pooling), giờ trả khách đã hứa lúc đặt xe thường xuyên bị trôi dạt do hệ thống chèn thêm khách mới hoặc do tắc đường (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 4-6, 320`).
   - Việc mở đầu Chương 1 bằng câu chuyện của một hành khách thực tế (`rq-30b7e083c7b` ở ô `d20181115-s10-r1-w07`: đặt xe lúc 7:11:56, hứa trả lúc 7:34:51, đón lúc 7:22:30, đến nơi lúc 7:38:02, trễ +190.5 giây chủ yếu do tắc đường lúc 7:15 và 7:30; `OUTLINE-PROPOSAL-CLAUDE.md: dòng 320`) là cách đặt vấn đề rất thuyết phục, kéo bài toán từ lý thuyết trừu tượng về đúng thực tế vận hành.
2. **Khoảng trống nghiên cứu (Research Gap): Định vị hẹp, chính xác và có đạo đức học thuật.**
   - Bảng định vị Bảng 1.1 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 322`) đã phân biệt rành mạch đề tài với các công trình đi trước:
     * Fielbaum & Alonso-Mora (2020) đã đo và kiểm soát độ bất ổn ở Mục 6, nhưng chọn khung giờ thấp điểm (13:00–15:00 ngày 15/01/2013) để cố tình bỏ qua biến động giao thông (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 115, 322`).
     * Hörl & Zwick (2022, chiến lược B) cập nhật giờ trả theo tắc đường nhưng chỉ áp dụng chặn cho khách đang trên xe sắp bị vi phạm, không có ngân sách từ đầu và không có sổ cái tách nguyên nhân (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 100, 322`).
     * Schulz & Pfeiffer (2026) dùng hạn chót 900 giây tính từ lời mời đầu nhưng trên mạng đường có thời gian đi cố định, không có tắc đường (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 322`).
   - Việc kiên quyết loại bỏ các tuyên bố nhận vơ (như "lần đầu tiên phát hiện", "duy nhất", hay phủ nhận việc Fielbaum 2020 đã kiểm soát bất ổn) giúp luận văn tránh được lỗi ngụy biện học thuật nghiêm trọng.
3. **Phương pháp (Method): Ý tưởng kỹ thuật mạch lạc theo nguyên lý phân tách trách nhiệm.**
   - Phương pháp bám sát mạch truyện "ba nguyên nhân $\to$ ba chỗ xử lý" (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 4-6, 321`):
     * Do điều phối ghép thêm khách $\to$ áp trần ngân sách luật C ($\sum |c| \le B$) lọc trước bài toán quy hoạch nguyên (ILP).
     * Do tắc đường đoán trước được $\to$ cộng hồ sơ tăng trưởng lịch sử 15 phút vào lời hứa đầu.
     * Do tắc đường bất ngờ $\to$ sổ cái ba phần $v/e/p$ ghi lại minh chứng cho từng khách ($z = x + c$).
   - Về mặt kỹ thuật phần mềm, đây là thiết kế kiến trúc phân tầng kết hợp tối ưu tổ hợp rất rõ ràng.
4. **Thực nghiệm và Đánh giá (Evaluation): Chặt chẽ, đa chiều, có đối chứng công bằng.**
   - Thay vì các tập dữ liệu tĩnh cũ, đề cương chuyển toàn bộ trọng tâm sang bộ thử nghiệm T3.8 gồm 34 ô kiểm trên dữ liệu Manhattan, 3.672 yêu cầu qua 5 ngày (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 352-353`).
   - Bảng đối sánh chính (Bảng 4.4, `OUTLINE-PROPOSAL-CLAUDE.md: dòng 353`) so sánh sòng phẳng giữa không trần (U), không trần có dự báo và đệm thời gian (30s, 60s), luật C-30, và luật hạn chót $M^+$-30. Đánh giá đồng thời cả hai chiều: tỷ lệ đúng hẹn, số khách phục vụ, độ dài lời hứa và tỷ lệ đến sớm.
5. **Đóng góp (Contribution): Khiêm tốn nhưng định lượng rõ ràng.**
   - Phần đóng góp (Mục 3, `OUTLINE-PROPOSAL-CLAUDE.md: dòng 450-479`) không tâng bốc thuật toán mà nêu chính xác những gì đo được: C-30 phục vụ cùng 2.338 khách như luật hạn chót $M^+$-30 nhưng đạt 0% quyết định bị ép phục hồi (so với 41.3% của $M^+$) và 0% tự phá lời hứa (so với 14.5% của $M^+$).
6. **Giới hạn (Limitations): Minh bạch, khoa học.**
   - Liệt kê đầy đủ 14 giới hạn thực nghiệm ở §4.11 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 362`): mức tải thấp (0.54 khách/xe so với 1.33 ở bài báo FleetPy 2026), thời gian dừng đón trả 0 giây, một hệ số tắc đường cho cả thành phố, 34 ô phụ thuộc từ 5 ngày, không có mô hình phản ứng/hủy chuyến của khách, và giá trị kinh tế chưa được chứng minh bằng tiền thật.

---

### 1.2. Nhận xét về Dung lượng và Phân bổ Trang (Page Budgets)

Bản đề cương rút từ 105 trang xuống 74 trang (70 trang nếu bỏ phụ lục) là hoàn toàn hợp lý với một khóa luận đại học ngành CNTT tại UET (khung thông thường 60–80 trang). Tuy nhiên, việc phân bổ trang giữa các phần cần lưu ý:

1. **Những phần quá dài cần cô đọng thêm:**
   - **Mục 4.4 "Chọn mức trần B" (3.5 trang, `OUTLINE-PROPOSAL-CLAUDE.md: dòng 355`):** Việc giữ cả bảng bậc thang WP14r (16 ô tắc đường cố định) và thang w07 (8 ô buổi sáng) cùng tỷ lệ chi phí từng bước (price per step) là hơi nặng nề. Phần này chỉ nên gói gọn trong 2.0 – 2.5 trang để tránh làm loãng trọng tâm của bộ dữ liệu chính T3.8.
   - **Mục 3.3 "Luật C" (2.5 trang, `OUTLINE-PROPOSAL-CLAUDE.md: dòng 342`):** Việc chứng minh Nhận xét 3.1 (không tự loại phương án giữ nguyên no-op) và phân tích các phản ví dụ CE-2, CE-3 nên viết cô đọng trong 1.5 trang, phần chứng minh chi tiết có thể chuyển sang Phụ lục B.
2. **Những phần quá ngắn cần làm sâu sắc hơn (Đặc thù CNTT):**
   - **Mục 3.7 "Cài đặt, kiểm thử và tái lập" (2.0 trang, `OUTLINE-PROPOSAL-CLAUDE.md: dòng 346`):** Đối với hội đồng CNTT, đây là phần thể hiện năng lực kỹ sư của sinh viên. Đề cương hiện tại chỉ dành 2 trang cho kiến trúc phần mềm, pipeline kết nối C#/.NET với FleetPy (Python), cơ chế ghi nhật ký frame với mã băm SHA-256. Nên nâng lên 2.5 – 3.0 trang, học tập phong cách của Báo cáo DACN (`23020155_TranQuangThanh_Bao cao DACN.pdf: trang 14, 27–28`) khi mô tả chi tiết pipeline, luồng xử lý và độ phức tạp tính toán.
   - **Mục 4.9 "Học máy có giúp thêm không?" (0.75 trang, `OUTLINE-PROPOSAL-CLAUDE.md: dòng 360`):** Dù kết quả học máy là âm tính (ML pilot dừng do vi phạm điều kiện chặn), việc chỉ trình bày 0.75 trang dạng chữ không bảng biểu dễ khiến hội đồng nghĩ sinh viên làm đối chứng qua loa. Cần bổ sung 1 bảng tóm tắt cấu hình các mô hình đã thử (HGB quantile, linear quantile) và kết quả đối sánh để tăng tính thuyết phục.
3. **Những nội dung còn thiếu cần bổ sung:**
   - **Phân tích độ phức tạp thuật toán và thời gian tính toán thực tế:** Trong Báo cáo DACN, tác giả đã trình bày rất tốt Bảng 3.9 về "Độ phức tạp của các thành phần chính trong pipeline tối ưu" (`Báo cáo DACN: trang 28`) và thời gian xử lý trung bình 953 ms (`Báo cáo DACN: trang 30`). Luận văn tốt nghiệp hiện tại rất cần một mục hoặc bảng tương tự phân tích độ phức tạp của bước lọc luật C trước ILP và thời gian tính toán thêm khi chiếu lời hứa $v/e/p$.
   - **Bảng chuẩn hóa chuyển đổi ký hiệu (Notation Mapping Table):** Như đề cương đã cảnh báo ở lỗi X2 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 233-236, 581-583`), luận văn cũ dùng $B = |p-v|$ và $\beta$ là trần, trong khi đề cương mới dùng $c = p-e$ và ngân sách $B$. Nếu không có một bảng quy ước ký hiệu rõ ràng ngay đầu Chương 3, sinh viên rất dễ bị hội đồng bắt bẻ lỗi "râu ông nọ cắm cằm bà kia".

---

### 1.3. Sáu câu hỏi Hội đồng sẽ hỏi lúc Bảo vệ (Xếp theo độ nguy hiểm giảm dần)

Dưới đây là 6 câu hỏi hóc búa nhất mà hội đồng UET chắc chắn sẽ xoáy sâu, cùng đánh giá xem đề cương đã chuẩn bị câu trả lời cho sinh viên hay chưa:

#### Câu 1 (Mức độ nguy hiểm: Cực cao — Tấn công trực diện vào tính mới của luật C)
> *"Em khẳng định đóng góp của đề tài là đề xuất ngân sách cộng dồn cho cả chuyến đi ($\sum |c| \le B$). Nhưng số liệu thực nghiệm ở Bảng 4.8 chỉ ra rằng trong suốt 98 lượt chạy trên tắc đường thật với 64.371 quyết định, cả 1.256 lần ứng viên bị chặn đều là do một bước nhảy vượt quá ngân sách ($\Delta > B$), số lần bị chặn do cộng dồn dồn tích thuần túy là 0! Nói cách khác, luật của em hoạt động không khác gì một trần khống chế từng bước riêng lẻ (per-step cap). Vậy tại sao em lại gắn chữ 'cộng dồn' vào tên đóng góp như thể nó là nhân tố tạo nên thành công thực nghiệm?"*

- **Đề cương đã chuẩn bị câu trả lời chưa?**  
  **ĐÃ CHUẨN BỊ RẤT TỐT.**  
  Đề cương đã lường trước điều này và chuẩn bị câu trả lời tại Luận điểm (7) mục 3 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 475-477`) và nội dung mục 4.5 (`dòng 356`):
  1. Thừa nhận sòng phẳng về mặt thực nghiệm: Trên tập dữ liệu tắc đường đo được, quy tắc cộng dồn chưa từng đơn độc kích hoạt một lần chặn nào.
  2. Về mặt lý thuyết hợp đồng: Định nghĩa $\sum |c| \le B$ là cam kết chặn trên cho *toàn bộ hành trình* của khách hàng, đảm bảo dù xe có đón thêm bao nhiêu người thì tổng thời gian xáo trộn không vượt quá $B$.
  3. Giải thích nguyên nhân kỹ thuật: Trong môi trường thử nghiệm hiện tại, mức tải xe còn thấp (0.54 khách/xe; `dòng 362`), chuỗi ghép ngắn, và mỗi lần dời giờ tự nhiên trong mạng đường Manhattan đã có độ lệch lớn (trung vị dời giờ của U là 108.6 s; `dòng 354`), nên một bước nhảy đã vượt quá 30 giây. Điều này không làm mất đi giá trị của ràng buộc toàn trình khi triển khai ở các hệ thống có mức tải cao hơn.

#### Câu 2 (Mức độ nguy hiểm: Rất cao — Tấn công vào hiệu quả thực tế so với giải pháp đơn giản)
> *"Tại Bảng 4.4, phương pháp không trần (U) kết hợp dự báo và đệm thêm 30 giây đạt đúng 2.328 lượt đến đúng hẹn ($\le 60$s) trên 3.672 yêu cầu—bằng chằn chặn luật C-30 có dự báo—mà lại phục vụ được 2.434 khách (nhiều hơn luật C tới 96 khách doanh thu). Thậm chí ở ngưỡng 120 giây, cách đệm còn đạt 2.366 lượt đúng hẹn, vượt trội so với 2.338 lượt của luật C. Vậy tại sao doanh nghiệp phải áp dụng thuật toán luật C phức tạp của em để rồi bị mất 96 khách, thay vì chỉ cần cộng đệm 30 giây vào giờ hẹn lúc đầu?"*

- **Đề cương đã chuẩn bị câu trả lời chưa?**  
  **ĐÃ CHUẨN BỊ RẤT TỐT.**  
  Đề cương đã chủ động đưa hàng so sánh này vào Bảng 4.4 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 353`) và Luận điểm (6) mục 3 (`dòng 472-474`):
  1. Đệm lời hứa 30s đạt được số lượt đúng hẹn bằng cách kéo giãn giờ hẹn của toàn bộ khách hàng: Lời hứa dài thêm trung bình 37.2 giây (gấp 5 lần mức 7.4 giây của C-30).
  2. Đệm giờ làm méo mó trải nghiệm: 1.81% khách đến sớm hơn 1 phút (so với chỉ 0.17% của C-30), làm mất đi tính chính xác của giờ hẹn.
  3. Quan trọng nhất: Trong số 2.434 khách được chở của phương án đệm, vẫn có tới 106 khách bị trễ hẹn $> 60$s (tỷ lệ trễ 4.35%), trong khi luật C-30 chỉ có đúng 10 khách trễ (tỷ lệ trễ chỉ 0.43%). Luật C bảo vệ uy tín dịch vụ bằng cách triệt tiêu các ca trễ nặng do ghép xe, chứ không "lừa dối" chỉ số bằng cách nói vống giờ hẹn lên.

#### Câu 3 (Mức độ nguy hiểm: Cao — Tấn công vào bản chất thuật toán và biến gây nhiễu)
> *"Thuật toán điều phối của em dùng bộ chọn đa mức ưu tiên (lexicographic selection): sau khi nhận tối đa khách, hệ thống ưu tiên giảm thiểu thay đổi giờ đón/trả (stability-first), rồi mới xét đến chi phí xe chạy. Liệu kết quả giờ hẹn ổn định của em thực chất là do bộ chọn này quá 'bảo thủ' giữ nguyên lịch trình cũ, hay thực sự là nhờ trần cứng của luật C?"*

- **Đề cương đã chuẩn bị câu trả lời chưa?**  
  **CHUẨN BỊ MỘT PHẦN (Đang chờ thực nghiệm Stage 1b).**  
  Đề cương dành trọn Mục 4.6 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 357, 429-442`) để đối diện trực tiếp với nghi vấn này:
  1. Bằng chứng hiện có (sàng lọc trạng thái cố định): Khi giữ nguyên các ứng viên, bộ chọn chi phí chỉ đổi 6.1% quyết định dưới C-30, so với 26.0% dưới U (`dòng 357`). Mức độ bão hòa utilization đạt 1.000.000 ppm ở 3.506/3.506 quyết định (`dòng 357`).
  2. Kế hoạch dứt điểm: Thử nghiệm Stage 1b (thiết kế 2x2 giữa stability-first và cost-first trên 34 ô; `dòng 429-436`) sẽ trả lời dứt khoát câu hỏi này. Nếu Stage 1b không kịp chạy, đề cương đã chuẩn bị phương án dự phòng (fallback ở dòng 440-441): thừa nhận rõ đây là giới hạn của trạng thái cố định và không bao giờ khẳng định "chính trần chứ không phải bộ chọn giữ lời hứa".

#### Câu 4 (Mức độ nguy hiểm: Cao — Tấn công vào sự khác biệt với luật hạn chót $M^+$ trong văn liệu)
> *"Tại Bảng 4.4, luật C-30 và luật hạn chót $M^+$-30 (Schulz & Pfeiffer 2026) phục vụ đúng 2.338 khách như nhau, trùng nhau tới 2.332 khách. Khi có dự báo, cả hai đều đạt đúng 2.328 lượt đúng hẹn. Vậy luật C có ưu thế kỹ thuật gì thực chất so với luật hạn chót đã có sẵn trong sách báo?"*

- **Đề cương đã chuẩn bị câu trả lời chưa?**  
  **ĐÃ CHUẨN BỊ RẤT TỐT.**  
  Được chuẩn bị tại Bảng 4.4 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 353`) và Luận điểm (5) mục 3 (`dòng 470-471`):
  1. Khác biệt nằm ở **tính khả thi và sự lành mạnh của cam kết**: Luật hạn chót $M^+$ gộp cả tắc đường vào lời hứa, nên khi gặp tắc đường bất khả kháng, hệ thống bị rơi vào thế bế tắc: 41.3% quyết định của $M^+$ bị ép phải kích hoạt cơ chế phá luật (forced recovery), và 14.5% khách bị chính hệ thống thất hứa (`dòng 353, 470-471`).
  2. Ngược lại, luật C bóc tách phần tắc đường ra sổ cái, chỉ ràng buộc phần do thuật toán gây ra, do đó đạt **0% quyết định bị ép và 0% tự phá vỡ cam kết** (`dòng 353, 470`). Một hệ thống cam kết mà phải tự phá luật ở 41.3% số lần ra quyết định là một hệ thống không thể đưa vào hợp đồng dịch vụ thực tế.

#### Câu 5 (Mức độ nguy hiểm: Trung bình — Tấn công vào tính giá trị của mô phỏng)
> *"Toàn bộ thực nghiệm chạy trên mô phỏng FleetPy với mạng đường Manhattan, chỉ dùng duy nhất 1 hệ số tắc đường cho toàn thành phố mỗi 15 phút, thời gian dừng đón trả là 0 giây, và tốc độ nền lấy cố định lúc nửa đêm (00:00). Những giả định này có quá xa rời thực tế giao thông đô thị không?"*

- **Đề cương đã chuẩn bị câu trả lời chưa?**  
  **ĐÃ CHUẨN BỊ RẤT TỐT.**  
  Đề cương xử lý vấn đề này bằng thái độ trung thực khoa học mẫu mực: Liệt kê toàn bộ các yếu tố này thành các giới hạn nghiên cứu chính thức ở §4.11 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 362`) và §5.2 (`dòng 371`), đồng thời lập hộp cảnh báo "Không suy rộng" ở Mục 3 (`dòng 510`). Tác giả xác định rõ đây là mô hình đối sánh cơ chế có kiểm soát (controlled benchmarking), đóng vai trò bước đệm định lượng trước khi triển khai trên dữ liệu vi mô.

#### Câu 6 (Mức độ nguy hiểm: Trung bình — Tấn công vào khả năng xử lý thời tiết bất thường)
> *"Trong buổi chiều tuyết rơi ngày 15/11/2018 (Bảng 4.11), tỷ lệ trễ của hệ thống chỉ giảm nhẹ từ 7.19% xuống 5.94%, và có tới 92.5% số giây trễ là do tắc đường bất ngờ ngoài tầm dự báo. Vậy hệ thống của em có thực sự giúp ích gì được cho khách hàng trong những ngày thời tiết cực đoan như vậy không?"*

- **Đề cương đã chuẩn bị câu trả lời chưa?**  
  **ĐÃ CHUẨN BỊ RẤT TỐT.**  
  Được làm rõ tại §4.8 (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 359`):
  1. Thừa nhận thẳng thắn: Không thuật toán dự báo nào có thể đoán định chính xác một trận bão tuyết bất thường chỉ xảy ra 1 lần trong 4 tháng nếu chỉ dùng dữ liệu lịch sử thông thường (`dòng 359`).
  2. Giá trị của hệ thống trong tình huống này nằm ở **sổ cái minh bạch $v/e/p$**: Thay vì đổ vấy cho việc ghép xe, sổ cái chứng minh rõ ràng 92.5% thời gian trễ là do thiên tai ngoại cảnh ($x$), trong khi phần trễ do thuật toán điều phối ($c$) chỉ chiếm 8.6 giây trên tổng số 3.445.9 giây trễ (`dòng 359`). Hệ thống cung cấp bằng chứng giải trình kiểm toán được (auditable certificate) cho cả khách hàng và tài xế.

---

## Phần 2. Người đọc Ngoài ngành (Sinh viên năm cuối ngành khác)

Dưới góc nhìn của một sinh viên năm cuối khối ngành kinh tế, kỹ thuật khác hoặc khoa học tự nhiên—người có tư duy logic tốt nhưng không chuyên sâu về thuật toán tối ưu vận tải—tôi đọc Mục 3 (Tuyên bố đóng góp) và hệ thống tiêu đề của đề cương.

---

### 2.1. Các câu, thuật ngữ khó hiểu và phân tích nguyên nhân

1. **Thuật ngữ "ngân sách dời giờ trả cho từng khách (luật C)"** (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 453-454`):
   - *Khó hiểu:* Người ngoài ngành nghe chữ "ngân sách" (budget) sẽ nghĩ ngay đến tiền bạc hoặc chi phí tài chính. Họ không hiểu tại sao "dời giờ trả" lại có ngân sách.
   - *Bản chất:* Đây là **quỹ thời gian tối đa** (tính bằng giây) mà hệ thống cho phép mình làm chậm trễ chuyến đi của một khách hàng khi tiện đường đón thêm khách khác.
2. **Biểu thức "$c = p - e$, với $e$ là kế hoạch cũ tính lại theo tốc độ hiện tại"** (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 454-455`):
   - *Khó hiểu:* Đưa công thức ký hiệu toán học $c, p, e$ vào câu tuyên bố đóng góp khiến người đọc bị ngợp. Cụm từ "kế hoạch cũ tính lại theo tốc độ hiện tại" rất trừu tượng.
   - *Bản chất:* Khi đường bị kẹt, xe tự nhiên đi chậm lại khiến giờ đến nơi bị muộn đi một cách khách quan (gọi là mốc $e$). Nếu hệ thống còn đón thêm người mới khiến giờ đến bị muộn thêm nữa thành giờ $p$, thì **khoảng trễ phát sinh thêm do đón người ($p - e$)** chính là lỗi riêng của hệ thống điều phối.
3. **Cụm từ "tính trị tuyệt đối theo cả hai chiều"** (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 459`):
   - *Khó hiểu:* Người đọc dễ liên tưởng đến "chiều đi và chiều về" của chuyến xe.
   - *Bản chất:* Nghĩa là dù hệ thống làm khách đến **muộn hơn hay đến sớm hơn** so với lịch trình dự kiến thì độ lệch thời gian đó đều bị trừ vào quỹ thời gian cam kết ($|c|$), vì đến lệch giờ quá nhiều theo hướng nào cũng gây phiền toái.
4. **Cụm từ "phép chiếu mô hình"** (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 462`):
   - *Khó hiểu:* Dịch thô từ chữ "model projection". Người ngoài ngành sẽ nghĩ đến máy chiếu hoặc phép chiếu hình học không gian.
   - *Bản chất:* Đây là phép **tính toán phân tích dựa trên mô phỏng** để bóc tách xem trong tổng số phút trễ của khách, bao nhiêu phút là do đường kẹt và bao nhiêu phút là do hệ thống đón thêm người.
5. **Cụm từ "quyết định phải phục hồi (forced decision)"** (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 470-471`):
   - *Khó hiểu:* Từ "phục hồi" nghe như cấp cứu y tế hoặc khôi phục dữ liệu máy tính bị hỏng.
   - *Bản chất:* Đó là tình huống kẹt xe nặng đến mức nếu giữ đúng lời hứa ban đầu thì xe không tài nào chạy kịp, buộc thuật toán phải **chấp nhận phá vỡ cam kết** để chuyến xe có thể tiếp tục.
6. **Sự rối rắm giữa các tỷ lệ phần trăm:**
   - Người đọc rất dễ hoa mắt khi đọc thấy các con số: "0.17%", "0.43%", "3.25%", "8.34%" (`OUTLINE-PROPOSAL-CLAUDE.md: dòng 280-286, 468-474`).
   - *Cần làm rõ:* Phải luôn nói rõ mẫu số: Tính trên **tổng số chuyến khách đặt** (3.672 yêu cầu) hay tính trên **số khách thực tế được đón lên xe** (2.338 người).

---

### 2.2. Viết lại Mục 3 (Tuyên bố đóng góp) bằng Tiếng Việt tự nhiên, chuẩn mực

Dưới đây là bản viết lại toàn bộ **Mục 3 (Tuyên bố đóng góp của khóa luận)**. Bản viết này diễn đạt bằng ngôn ngữ khoa học sáng rõ, dễ hiểu cho mọi người đọc có học thức, nhưng bảo lưu **chính xác 100% bản chất kỹ thuật và các số liệu thực nghiệm**:

---

> ### Đóng góp cốt lõi của khóa luận
> 
> **1. Xây dựng cơ chế cam kết giờ đến đích có kiểm soát (Luật C):**  
> Khóa luận thiết kế và cài đặt vào hệ thống điều phối xe đi chung RideBound một quy tắc kiểm soát thời gian: mỗi hành khách khi đặt xe được cấp một **quỹ thời gian chệch giờ tối đa là $B$ giây** cho toàn bộ chuyến đi. Tại mỗi thời điểm hệ thống muốn ghép thêm khách mới, phần thời gian bị trễ phát sinh thuần túy do quyết định ghép xe được tách riêng khỏi ảnh hưởng của kẹt xe. Bất kỳ phương án ghép khách nào làm tổng thời gian trễ do điều phối vượt quá hạn mức $B$ đều bị hệ thống loại bỏ ngay từ đầu.
> 
> **2. Kế thừa và mở rộng ranh giới nghiên cứu:**  
> Cách xác định mốc thời gian của đề tài kế thừa ý tưởng từ Chiến lược B của Hörl và Zwick (2022)—vốn cập nhật giờ trả khách theo tình hình giao thông trên tuyến đường cũ. Khóa luận mở rộng thành một cam kết hoàn chỉnh: áp dụng thống nhất mức ngân sách $B$ cho mọi hành khách ngay từ lúc đặt xe, tính toán độc lập với mức độ tắc đường, kiểm soát độ lệch thời gian theo cả hai hướng (đến muộn hơn hoặc sớm hơn), và cộng dồn qua tất cả các lần ghép khách vào một **sổ cái điện tử minh bạch** cho từng người.
> 
> **3. Phối hợp đồng bộ ba giải pháp cho ba nguyên nhân trôi dạt giờ hẹn:**  
> Quy tắc kiểm soát trên được kết hợp chặt chẽ với hai cơ chế bổ trợ:  
> - *Hứa giờ theo dự báo:* Sử dụng dữ liệu lịch sử giao thông theo từng khung 15 phút để đưa độ trễ dự kiến vào ngay khung giờ hứa lúc đầu.  
> - *Sổ cái bóc tách nguyên nhân:* Sử dụng mô hình toán học để chia rành mạch tổng thời gian trễ của khách thành ba phần: phần do hệ thống ghép thêm người, phần do tắc đường đã dự báo trước, và phần do ùn tắc bất ngờ phát sinh trên đường.
> 
> **4. Đánh giá thực nghiệm quy mô lớn và đa chiều:**  
> Khóa luận đo lường sự đánh đổi giữa ba yếu tố: số khách phục vụ được, tỷ lệ khách đến đúng hẹn và độ dài của khoảng thời gian hứa hẹn. Thực nghiệm được thực hiện trên nền tảng mô phỏng FleetPy với dữ liệu giao thông thực tế tại khu vực Manhattan (New York), gồm **34 kịch bản thử nghiệm với 3.672 yêu cầu đặt xe trong 5 ngày**. Phương pháp đề xuất được đối sánh trực tiếp với ba giải pháp:  
> (a) Điều phối tự do không giới hạn trần giờ trả;  
> (b) Luật hạn chót cứng tính từ lời hứa ban đầu (theo hướng tiếp cận của Schulz và Pfeiffer, 2026);  
> (c) Phương pháp nới rộng (đệm thêm) thời gian hứa hẹn ngay từ đầu.
> 
> **5. Giữ vững cam kết mà không làm giảm số lượng phục vụ (khi $B = 30$ giây):**  
> - So với phương án điều phối tự do, luật C phục vụ ít hơn 96 khách (tương đương 2,6% tổng số yêu cầu), nhưng giảm được 127 chuyến trễ quá 1 phút và tăng thêm 31 chuyến hoàn thành đúng hẹn trên cùng 3.672 yêu cầu.  
> - So với luật hạn chót cứng cùng mức 30 giây, luật C phục vụ **chính xác cùng số lượng 2.338 khách** (trong đó có 2.332 khách trùng nhau). Tuy nhiên, luật hạn chót bị rơi vào tình trạng bất khả thi và buộc phải tự phá vỡ cam kết ở 41,3% số quyết định, trong khi **luật C đạt tỷ lệ 0% quyết định bị ép và 0% tự phá vỡ cam kết**.
> 
> **6. Vượt trội về độ chính xác so với giải pháp đệm giờ:**  
> Khi tích hợp thêm dự báo giao thông, cả luật C và luật hạn chót đều đạt 2.328 chuyến hoàn thành đúng hẹn (không trễ quá 1 phút). Cách làm đơn giản là lấy phương án tự do rồi đệm thêm 30 giây cũng đạt được 2.328 chuyến đúng hẹn này, thậm chí nhỉnh hơn ở ngưỡng trễ 2 phút (2.366 so với 2.338 chuyến). Đổi lại, giải pháp đệm giờ khiến lời hứa bị kéo dài thêm trung bình tới 37,2 giây (so với chỉ 7,4 giây của luật C), làm 1,81% khách đến sớm hơn 1 phút một cách không cần thiết (so với 0.17% của luật C), và vẫn để 106 khách thực tế bị trễ hẹn (so với chỉ 10 khách của luật C).
> 
> **7. Phát hiện thực nghiệm trung thực về cơ chế cộng dồn:**  
> Kiểm tra toàn bộ 98 lượt chạy mô phỏng có áp dụng luật C cho thấy: toàn bộ 1.256 trường hợp ứng viên ghép xe bị loại bỏ đều là do một lần ghép đơn lẻ làm trễ vượt quá ngưỡng $B$. Trong điều kiện thực nghiệm này, cơ chế cộng dồn dồn tích chưa từng là nguyên nhân đơn độc kích hoạt việc từ chối ghép xe. Khóa luận ghi nhận đây là đặc điểm của tập dữ liệu thử nghiệm và không khẳng định cơ chế cộng dồn mang lại ưu thế thực nghiệm vượt trội so với việc khống chế từng bước riêng lẻ.

---

### 2.3. Viết lại Tiêu đề các Chương và Mục cho Tự nhiên và Chuyên nghiệp

Hệ thống tiêu đề trong đề cương (`OUTLINE-PROPOSAL-CLAUDE.md: §2.3–§2.7`) đã rất tốt về mặt cấu trúc logic, nhưng một số đề mục cần được mài giũa lại câu chữ tiếng Việt để trang trọng, giàu tính học thuật và tự nhiên hơn:

| Vị trí | Tiêu đề cũ trong đề cương | Tiêu đề đề xuất viết lại (Chuẩn học thuật & Tự nhiên) |
|---|---|---|
| **Chương 1** | **Đặt vấn đề** | **Chương 1. Đặt vấn đề và Động lực nghiên cứu** |
| §1.1 | Bối cảnh: lời hứa giờ trả trong xe đi chung | §1.1. Bài toán cam kết thời gian đến đích trong dịch vụ xe đi chung |
| §1.2 | Ba nguyên nhân làm lời hứa lệch và chỗ xử lý mỗi nguyên nhân | §1.2. Phân tích các nguyên nhân gây sai lệch thời gian hẹn và định hướng giải pháp |
| §1.3 | Các công trình gần nhất và chỗ đứng của khóa luận | §1.3. Tổng quan các nghiên cứu liên quan và định vị đóng góp của đề tài |
| **Chương 2** | **Cơ sở lý thuyết** | **Chương 2. Cơ sở lý thuyết và Mô hình bài toán** |
| §2.2 | Lời hứa công bố và độ bất ổn: đo và kiểm soát | §2.2. Đo lường và kiểm soát độ bất ổn của thời gian cam kết |
| §2.3 | Các dạng nghĩa vụ lời hứa | §2.3. Các mô hình ràng buộc thời gian hẹn trong vận tải chia sẻ |
| **Chương 3** | **Phương pháp: luật C, hứa theo dự báo và sổ cái theo từng khách** | **Chương 3. Phương pháp kiểm soát thời gian cam kết và Bóc tách nguyên nhân** |
| §3.2 | Lời hứa và ba mốc v, e, p | §3.2. Mô hình biểu diễn thời gian cam kết và các mốc trạng thái $v, e, p$ |
| §3.3 | Luật C: ngân sách dời giờ trả do điều phối cho từng khách | §3.3. Cơ chế Luật C: Kiểm soát trần thay đổi thời gian điều phối cho từng hành khách |
| §3.4 | Các luật đối chứng và bộ chọn phương án | §3.4. Các phương pháp đối chứng và thuật toán lựa chọn phương án đa mức ưu tiên |
| §3.7 | Cài đặt, kiểm thử và tái lập | §3.7. Thiết kế kiến trúc hệ thống, kiểm thử và quy trình tái lập kết quả |
| **Chương 4** | **Thực nghiệm và đánh giá** | **Chương 4. Thực nghiệm, Đánh giá và Phân tích kết quả** |
| §4.3 | Phần do điều phối: luật C chặn được gì và mất gì | §4.3. Phân tích tác động của Luật C đối với các quyết định ghép xe |
| §4.4 | Chọn mức trần B | §4.4. Đánh giá sự đánh đổi khi thay đổi ngưỡng ngân sách cam kết $B$ |
| §4.5 | Phần cộng dồn của luật C: kiểm toàn bộ bản ghi | §4.5. Phân tích vai trò thực nghiệm của cơ chế cộng dồn ngân sách |
| §4.6 | Độ tin cậy đến từ trần hay từ bộ chọn ổn định? | §4.6. Phân tích vai trò của trần cam kết và thuật toán lựa chọn phương án |
| §4.8 | Khi dự báo không đủ: buổi chiều tuyết 15/11/2018 | §4.8. Đánh giá khả năng thích ứng trong điều kiện thời tiết bất thường |
| §4.9 | Học máy có giúp thêm không? | §4.9. Thử nghiệm mở rộng với các mô hình học máy dự báo thời gian |
| §4.10 | Kiểm tra tính hợp lệ của kết quả | §4.10. Kiểm chứng tính toàn vẹn và độ tin cậy của kết quả thực nghiệm |
| §4.11 | Thảo luận và hạn chế của thực nghiệm | §4.11. Thảo luận kết quả và các giới hạn của mô hình thực nghiệm |
| **Chương 5** | **Kết luận** | **Chương 5. Kết luận và Hướng phát triển** |
| §5.1 | Tổng kết theo ba nguyên nhân | §5.1. Tổng kết các kết quả đạt được theo ba nhóm nguyên nhân |

---

END OF ANTIGRAVITY R20
