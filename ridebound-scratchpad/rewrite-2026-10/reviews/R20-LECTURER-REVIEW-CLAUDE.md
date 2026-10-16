# R20. Nhận xét dàn ý viết lại khóa luận (vai giảng viên trong hội đồng)

- **Người nhận xét:** Claude, trong vai một giảng viên hội đồng chấm khóa luận ngành CNTT. Tôi có nền về tối ưu và hệ thống giao thông, và chưa biết gì về đề tài trước khi đọc.
- **Ngày:** 10/10/2026.
- **Văn bản được nhận xét:** `rewrite-2026-10/OUTLINE-PROPOSAL-CLAUDE.md` (605 dòng).
- **Tài liệu đọc kèm:**
  - Luận văn hiện tại `ridebound/main.pdf` (105 trang PDF), chỉ đọc.
  - Báo cáo Dự án công nghệ `23020155_TranQuangThanh_Bao cao DACN.pdf` (50 trang).
- **Những việc tôi không làm:** không chạy mô phỏng, không sửa luận văn, không mở các tệp bằng chứng (R15, R17, R18, T38…). Mọi con số như 96, 127 hay 2.338 tôi lấy nguyên từ dàn ý. Tôi **không xác nhận** được các con số đó.

**Quy ước trích dẫn**

- `DY:n` hoặc `DY:n-m`: dòng trong dàn ý.
- `LV tr. n (PDF m)`: luận văn hiện tại, trang in n, trang PDF m.
- `DACN tr. n (PDF m)`: báo cáo Dự án công nghệ.

**Cách đọc PDF.** Công cụ Read trên máy này không hiển thị được PDF vì thiếu `pdftoppm`. Tôi trích văn bản bằng `pdftotext -layout` và ghi bốn tệp văn bản tạm vào thư mục scratchpad của phiên. Đó là tệp duy nhất tôi ghi ngoài tệp này. Trong bản trích, cột của các bảng bị xô lệch, nên tôi không nhận xét hình thức bảng của PDF. Ngoại lệ duy nhất là chỗ văn bản cho thấy lỗi rất rõ (mục 4.4, điểm 10).

**Những phần tôi đã đọc**

- Luận văn:
  - PDF 1–16: bìa, cảm ơn, tóm tắt, abstract, mục lục, danh sách hình và bảng, ký hiệu.
  - PDF 17–25: toàn bộ chương 1.
  - PDF 26–28: đầu chương 2.
  - PDF 32–38: chương 3 đến hết §3.5.4.
  - PDF 46–48: §3.6–3.7.
  - PDF 49–52: đầu chương 4.
  - PDF 93–96: §4.16 và §5.1.
  - PDF 100–103: §5.3–5.4 và đầu tài liệu tham khảo.
- DACN:
  - PDF 1–19: bìa, mục lục, chương 1, đầu chương 2.
  - PDF 27–29: §3.2–3.3, bảng ràng buộc, giả mã.
  - PDF 41–50: chương 4, chương 5, tài liệu tham khảo.

---

## 0. Mười điểm chính

1. **Đề tài hiểu được, nhưng chỉ sau khi đọc rất nhiều.** Mạch "ba phần, ba chỗ xử lý" (DY:4-6) rõ ràng. Tuy vậy, người đọc phải đi qua 270 dòng kiểm toán và hàng chục mã nội bộ (T3.8, WP14r, w07, R17, D03, Stage 1a/1b…). Bản gửi thầy hướng dẫn hoặc hội đồng cần một đoạn tiếng Việt khoảng 5 dòng nói đề tài là gì, và không được chứa mã nội bộ.
2. **Đoạn đóng góp (DY:450-478) chưa theo đúng luật mà chính dàn ý đặt ra.**
   - Đoạn dài khoảng 558 âm tiết và có khoảng 30 con số.
   - Các ký hiệu c, p, e, B, v/e/p xuất hiện trước khi được định nghĩa.
   - "Chiến lược B" của Hörl–Zwick đứng cạnh "ngân sách B" trong cùng một câu.
   - Số trung bình theo ô (41,3%) bị trộn với số đếm gộp.
   - "0,17%" không có mẫu số.
   - Bản viết lại ở mục 2.3 chỉ giữ khoảng 10 con số.
3. **Câu hỏi nguy hiểm nhất: luật C để làm gì?** Khi đã có dự báo, cách "không trần + dự báo + đệm 30 s" cho cùng 2.328 lượt đúng hẹn ở ngưỡng 60 s, và còn hơn ở ngưỡng 120 s (DY:353, DY:472-474). Dàn ý có đủ số, nhưng chưa có lập luận vì sao nhà vận hành vẫn cần luật C.
4. **Câu (2) nêu hai điểm khác chưa từng có tác dụng trên dữ liệu.** Đó là "cộng dồn" và "trị tuyệt đối hai chiều". Câu (7) cho biết phần cộng dồn chưa từng là lý do riêng của một lần chặn. Bộ sinh phương án chỉ chèn nên c ≥ 0 (DY:140), tức chiều "sớm lên" cũng không xảy ra. Nên rút hai tính chất này khỏi danh sách điểm khác.
5. **Đối chứng cần được nói thẳng.**
   - Luật hạn chót được thử ở 30 s. Mức này chặt hơn 30 lần mức 15 phút của Schulz–Pfeiffer (LV tr. 4 và 7, PDF 20 và 23).
   - Cách của Hörl–Zwick, công trình gần nhất, chưa được cài làm đối chứng (DY:372).
   - Cần nói cả hai điều trên ngay trong §4.2, và đưa đường "tỉ lệ quyết định phải phục hồi theo B" vào chính văn.
6. **Thiếu kế hoạch đánh giá độ tin cậy thống kê của kết quả chính.**
   - Thực nghiệm có 34 ô phụ thuộc nhau, 5 ngày, một hạt giống, và một số ô đã được xem trước (DY:362).
   - Nên thêm bảng hiệu số theo ngày × khung giờ.
   - Nên thêm số lượt trễ tính trên 2.207 khách được cả hai luật phục vụ.
   - Đây là phân tích lại dữ liệu cũ, không cần chạy mới, với điều kiện số liệu theo ô đã có. Điều này tôi chưa kiểm chứng.
7. **Bố cục 74 trang hợp lý, nhưng còn thiếu và còn thừa.**
   - Thiếu:
     - một mục phát biểu bài toán (đầu vào, quyết định, đầu ra);
     - hình minh họa việc chèn khách làm dời giờ trả;
     - giả mã cho trọn một chu kỳ quyết định;
     - thời gian tính và cách kiểm thử;
     - dòng "luật C" trong bảng so sánh với văn liệu.
   - Thừa:
     - §4.9 về học máy;
     - phụ lục B;
     - hai bảng so sánh công trình liên quan chồng lên nhau ở chương 1 và chương 2.
8. **Về các quyết định ở DY:556-577:**
   - Hạ định lý thành "Nhận xét" và bỏ phụ lục B.
   - Giữ bìa và abstract tiếng Anh cho đến khi kiểm được mẫu của trường. Việc này chưa kiểm chứng; báo cáo DACN có cả hai.
   - Đổi sang một tên đề tài ngắn và bỏ chữ "chứng nhận".
   - Phụ lục không quá 2 trang.
   - Viết trước bản ứng với trường hợp Stage 1b không có số liệu (bản dự phòng).
   - Gọi tên các luật bằng tiếng Việt mô tả; ký hiệu chỉ dùng trong bảng.
9. **So với báo cáo DACN.**
   - Dàn ý giữ được: bảng định vị, bảng ràng buộc, giả mã, và kết quả có mẫu số.
   - Dàn ý còn thiếu: giả mã tổng thể, bảng độ phức tạp hoặc thời gian xử lý, câu "cách đọc bảng" và quy ước dấu.
   - Không nên học theo phần tóm tắt của DACN, vì nó không có con số nào (DACN PDF 5).
10. **Hai lỗi dàn ý chưa ghi nhận.**
    - Bản hiện tại có một trang "Tài liệu tham khảo" gần như trống, sau đó là tiêu đề tiếng Anh "Bibliography" (LV PDF 102–103).
    - Ví dụ khách thật ở §1.1 minh họa cái lợi của dự báo, không minh họa luật C (DY:320).

---

## 1. Đọc dàn ý, tôi hiểu đề tài đến đâu?

### 1.1 Bài toán: hiểu được

Nói bằng lời của tôi: trong dịch vụ xe đi chung theo yêu cầu, hệ thống báo cho khách một giờ trả dự kiến. Sau đó, mỗi khi có khách mới, hệ thống liên tục sắp xếp lại lộ trình, nên giờ trả của những khách đang đi bị dời.

Đề tài tách độ lệch này thành ba phần:

- Phần do chính quyết định điều phối gây ra. Phần này bị chặn bằng một hạn mức cứng cho từng khách trong cả chuyến (luật C).
- Phần tắc đường đoán trước được. Phần này được đưa vào lời hứa đầu bằng dự báo.
- Phần còn lại. Phần này được ghi vào sổ theo dõi của từng khách.

Sau đó đề tài đo xem hạn mức được gì và mất gì so với không giới hạn, với luật hạn chót, và với cách đệm lời hứa.

Tôi rút ra được điều trên từ DY:4-6, DY:320-323 và DY:342. Tuy vậy, ở đầu dàn ý không có đoạn nào nói điều đó bằng tiếng Việt. Phần 2 chỉ bắt đầu từ DY:273.

### 1.2 Vì sao quan trọng: hiểu được một nửa

- **Lý do quan trọng dựa gần như hoàn toàn vào văn liệu phía cầu.** Đó là đoạn Alonso-González, Geržinič, Bansal được dùng lại (LV tr. 1–2, PDF 17–18), cộng thêm 0,5 trang ở §2.5 (DY:334).
- **Dàn ý tự cấm nói về lợi ích kinh doanh (DY:508)** và ghi "giá trị kinh doanh chưa được xác nhận" (DY:362). Như vậy đó là một lỗ hổng thật, không phải chỉ là chuyện câu chữ.
- **Gợi ý.** Dàn ý đã định thêm trang giới thiệu UberX Share vào tài liệu tham khảo (DY:198). Nếu trang đó có nói về giờ đến hứa với khách đi chung, nên dùng nó làm câu mở đầu thực tế cho §1.1. Tôi chưa đọc trang này, nên chưa kiểm chứng nội dung của nó.
- **Ví dụ mở đầu chưa đúng trọng tâm.** H1.1 kể về một khách trễ 190,5 s, và nếu hứa theo dự báo thì chỉ trễ 17,6 s (DY:320). Ví dụ này cho thấy dự báo có ích. Nhưng dự báo là thứ khóa luận nói không phải của mình (DY:498). Người đọc chưa thấy được vì sao cần luật C. Xem câu hỏi Q8 ở mục 3.

### 1.3 Đóng góp: hiểu được, nhưng phải đọc hết bảy câu

Tôi chỉ biết đóng góp thực sự là gì khi đọc đến câu (7). Ở đó mới rõ phần cộng dồn, vốn được nêu là điểm khác ở câu (2), chưa từng có tác dụng.

Câu (6) cho thấy, khi đã có dự báo, luật C hòa với cách đệm đơn giản. Như vậy, đến cuối đoạn, người đọc còn lại một đóng góp hẹp: hạn mức áp như nhau cho mọi khách, tính trên cả chuyến, đã được cài đặt và đo. Đóng góp hẹp vẫn ổn. Tôi coi đó là chấp nhận được với một khóa luận đại học; đây là ý kiến riêng của tôi, chưa kiểm chứng với quy chế của trường. Nhưng phải nói đóng góp đó ngay ở câu đầu, chứ không để người đọc tự suy ra sau bảy câu.

### 1.4 Rào cản khi đọc

- **Mã nội bộ.** Các mã T3.8, w07, WP14r (DY:352), Family A/B (DY:358), Gate 0 (DY:429), cùng các neo R17/R18/D03/BAN-GIAO ở hầu hết các dòng, chỉ người trong dự án mới hiểu.
  - Với một tài liệu làm việc thì chấp nhận được.
  - Bản đề cương gửi hội đồng phải bỏ hết các mã này.
  - Mỗi bộ thử nên có một tên tiếng Việt, ví dụ "bộ thử chính (34 ô)", "bộ chỉnh hạn mức buổi sáng (8 ô)", "bộ tắc đường cố định (16 ô)", "chiều tuyết 15/11".
- **Gọi là "ba nguyên nhân" chưa chính xác.** Phần thứ ba là phần còn lại, tức phần dư, không phải một nguyên nhân (DY:4-5, DY:321). Một người đọc kỹ sẽ bắt lỗi này. Nên đổi tên §1.2 thành "Ba phần của độ lệch giờ trả và chỗ xử lý mỗi phần".
- **Ký hiệu xuất hiện trước khi được định nghĩa.**
  - Bảng 2.2 ở chương 2 dùng đẳng thức Σ(c + x) và Σ|c + x| (DY:332), trong khi c và x đến §3.2 mới được định nghĩa (DY:341).
  - Bảng 1.1 ở chương 1 đã có max(updated, latest) và α·T_accepted + β (DY:322).
  - Ở chương 1 nên mô tả bằng lời, còn công thức để sang chương 2 hoặc 3.

---

## 2. Đoạn đóng góp (DY:450-478)

### 2.1 Nhận xét chung

- **Độ dài.** Đoạn có 7 câu đánh số và một câu để trống, khoảng 558 âm tiết. Không tính số thứ tự câu và năm, đoạn có khoảng 30 con số. Hội đồng đọc phần đóng góp trong khoảng một phút, nên 30 con số là quá nhiều.
- **Câu đầu không nói bài toán.** Câu (1) bắt đầu ngay bằng "đặc tả, cài đặt… và kiểm chứng trên bản ghi một ngân sách dời giờ trả".
- **Câu (2) liệt kê sáu điểm khác cùng lúc:**
  - mọi khách từ lúc đặt;
  - cùng ngân sách cho cả chuyến;
  - không phụ thuộc phần tắc đường;
  - trị tuyệt đối hai chiều;
  - cộng dồn;
  - sổ cái kiểm được.

  Người ngoài không biết điểm nào là chính. Như đã nói ở điểm 4 mục 0, hai trong sáu điểm chưa từng có tác dụng trên dữ liệu.
- **Đoạn vi phạm chính các luật của dàn ý.**
  - Luật 3 yêu cầu luôn ghi mẫu số và không viết "0,17%" khi không có mẫu số (DY:280-286). Câu (6) lại viết "0,17% số khách tới sớm" (DY:474).
  - Dàn ý cảnh báo việc trộn số trung bình theo ô với số gộp (DY:597-598). Câu (5) lại ghép "41,3% quyết định (trung bình theo ô)" với các số đếm gộp 2.338 và 2.332 (DY:470-471).
  - Cùng một số "0,17%" vừa là tỉ lệ tới sớm ở câu (6), vừa là tỉ lệ trễ trung bình theo ô của dự báo ở §4.7 (DY:358). Người đọc sẽ nhầm hai số này với nhau.

### 2.2 Từng câu: chỗ khó với người ngoài và cách sửa

**Câu (1), DY:453-456.**
- Chỗ khó:
  - Chưa giải thích "RideBound" là gì.
  - Chữ "luật C" không cho biết gì; C là viết tắt của "conduct", tức cơ sở hành vi ở bản cũ (LV tr. 19, PDF 35).
  - c = p − e được viết khi p chưa được định nghĩa.
  - "Kiểm chứng trên bản ghi": không rõ là bản ghi gì.
  - Câu "e là kế hoạch cũ tính lại theo tốc độ hiện tại" không khớp với chính dàn ý. Theo DY:341, e gồm cả tiến độ thực hiện. Theo luận văn, e được chiếu lại "từ vị trí thật hiện tại của xe" (LV tr. 17, PDF 33) và gồm "tiến độ thực của xe, độ trễ thực thi, cập nhật thời gian di chuyển" (LV tr. 21, PDF 37). Hơn nữa, e là một giờ, không phải một kế hoạch.
- Sửa: bỏ hết ký hiệu khỏi đoạn đóng góp. Viết thành "giờ trả nếu cứ giữ nguyên kế hoạch cũ, tính lại từ vị trí hiện tại của xe".

**Câu (2), DY:457-460.**
- Chỗ khó:
  - "Mốc e" là cách gọi nội bộ.
  - "Chiến lược B" của Hörl–Zwick và "ngân sách B" của khóa luận nằm trong cùng một câu, dùng chung một chữ B nhưng là hai thứ khác nhau.
  - "Không phụ thuộc phần tắc đường" có hai cách hiểu: hạn mức không đổi theo tắc đường, hoặc phần tắc đường không bị tính.
  - Có sáu điểm khác.
  - "Sổ cái v/e/p" là ký hiệu.
- Sửa:
  - Gọi công trình kia là "cách cập nhật giờ trả của Hörl và Zwick (2022, công thức 7)", không gọi là "chiến lược B".
  - Chỉ giữ những điểm khác thực sự có tác dụng trên dữ liệu. Xem mục 2.3.

**Câu (3), DY:461-463.**
- Chỗ khó:
  - "Phép chiếu mô hình" là thuật ngữ.
  - Cụm "phần còn lại" xuất hiện hai lần với hai nghĩa: "phần trễ còn lại" và "phần còn lại" của sổ cái.
  - Câu nói sổ cái ba phần "đã có tiền lệ" nhưng không ghi tiền lệ của ai.
- Sửa: "một phép tính theo mô hình, không phải kết luận ai có lỗi". Ghi rõ tên công trình làm tiền lệ, hoặc bỏ chữ "tiền lệ" nếu không có.

**Câu (4), DY:464-467.**
- Chỗ khó:
  - Không nói "ô" là gì.
  - Chưa giải thích "phục hồi 'không tệ hơn'" và "độ dài lời hứa".
- Sửa:
  - "34 phiên mô phỏng, mỗi phiên 2 giờ với 108 yêu cầu và 8 xe". Ba con số này lấy từ DY:324 và DY:352; tôi thấy 3.672 = 34 × 108 là khớp.
  - Phần "phục hồi" để sang chương 3.

**Câu (5), DY:468-471.**
- Chỗ khó:
  - Trong một câu có 9 con số.
  - Câu không giải thích vì sao phục vụ ít hơn mà lượt đúng hẹn lại nhiều hơn. Lý do là đúng hẹn = phục vụ − trễ, và mẫu số là số yêu cầu.
  - Người ngoài không biết "quyết định phải phục hồi" là gì, cũng không biết vì sao nó xấu.
  - Con số 41,3% không có mẫu số rõ ràng: trên tổng số quyết định nào?
- Sửa: viết như ở mục 2.3. Thay 41,3% bằng số đếm "x trên y quyết định". Dàn ý hiện chưa có số gộp cho chỉ tiêu này, nên cần bổ sung.

**Câu (6), DY:472-474.**
- Chỗ khó:
  - Câu này trung thực, nhưng là câu bất lợi nhất cho khóa luận, mà lại không kèm một lời giải thích nào. Xem câu hỏi Q1.
  - "0,17%" không có mẫu số.
  - Câu không nói số lượt phục vụ của cách đệm.
- Sửa:
  - Viết "4 trên 2.338 khách" thay cho 0,17% (lấy theo DY:285).
  - Nêu số lượt phục vụ của cách đệm, và nói rõ đánh đổi giữa hai cách.

**Câu (7), DY:475-477.**
- Chỗ khó:
  - "Bản ghi chặn do ngân sách", "nhánh tương ứng" và "luật mỗi bước một trần" đều là thuật ngữ nội bộ.
  - Câu này phủ nhận ngầm câu (2).
- Sửa: "Trong 98 lần chạy, lần nào hạn mức chặn một phương án cũng là vì riêng một lần dời đã vượt hạn mức; chưa lần nào bị chặn chỉ vì cộng dồn nhiều lần dời nhỏ."

### 2.3 Bản viết lại đề xuất (khoảng 300 âm tiết, 10 con số)

> **Đóng góp của khóa luận.** Trong xe đi chung, mỗi khi hệ thống nhận thêm khách, giờ trả đã hứa với
> những khách đang đi có thể bị dời. Khóa luận chia độ lệch này thành ba phần và xử lý mỗi phần ở một chỗ.
>
> Với phần dời do chính quyết định điều phối gây ra, khóa luận đặc tả và cài đặt trong hệ điều phối
> RideBound một *hạn mức dời giờ trả* cho từng khách. Mỗi lần sửa lời hứa, hệ thống so phương án mới với
> việc cứ giữ nguyên kế hoạch cũ để biết quyết định này đẩy giờ trả của khách đi bao nhiêu. Tổng các lần
> đẩy của một khách trong cả chuyến không được vượt một hạn mức cố định, ví dụ 30 giây; phương án làm
> vượt hạn mức bị loại trước khi chọn. Việc so với kế hoạch cũ đã có ở Hörl và Zwick (2022); điều khóa
> luận làm thêm là áp cùng một hạn mức cho mọi khách, trên cả chuyến, và tính riêng phần do điều phối.
>
> Phần tắc đường đoán trước được xử lý bằng cách báo giờ theo dự báo, một cách đã có trong thực tiễn.
> Phần còn lại được ghi vào sổ theo dõi của từng khách. Cách chia ba phần là phép tính theo mô hình,
> không phải kết luận ai có lỗi.
>
> Khóa luận đo cái được và cái mất của hạn mức bằng bộ mô phỏng FleetPy, trên dữ liệu yêu cầu và tắc
> đường của Manhattan: 34 phiên, 3.672 yêu cầu, 5 ngày. Với hạn mức 30 giây, so với điều phối không giới
> hạn, hệ thống phục vụ ít hơn 96 lượt khách. Đổi lại, số khách trễ quá 1 phút giảm 127, nên số khách đến
> đúng hẹn vẫn tăng thêm 31. Luật hạn chót tính từ lời hứa đầu phục vụ cùng số khách, nhưng nhiều lần không
> còn phương án nào thỏa chính nó; hạn mức dời giờ chưa lần nào rơi vào tình huống đó. Khi đã báo giờ theo
> dự báo, cách đơn giản là cộng thêm 30 giây vào mọi lời hứa cũng cho cùng số khách đúng hẹn, nhưng lời
> hứa dài hơn và nhiều khách tới sớm hơn hẹn. Trên dữ liệu đã chạy, hạn mức chưa từng chặn một phương án
> chỉ vì cộng dồn nhiều lần dời nhỏ, nên vai trò của phần cộng dồn còn chưa được kiểm chứng.

Ngay sau đoạn này, đặt một danh sách "Kết quả chính" với đầy đủ mẫu số. Mỗi dòng có một nguồn trong bảng bằng chứng (DY:480-490):

- Phục vụ: 2.434 lượt (không giới hạn) so với 2.338 lượt (hạn mức 30 s), trên 3.672 yêu cầu.
- Trễ quá 60 s: 203 so với 76 lượt. Đúng hẹn: 2.231 so với 2.262 lượt, trên 3.672 yêu cầu. Theo DY:413-414.
- So với luật hạn chót: cùng 2.338 lượt, trong đó 2.332 lượt là khách chung. Số quyết định phải phục hồi: 0 so với **[x trên y]** quyết định. Cần số gộp; dàn ý hiện chỉ có 41,3% trung bình theo ô.
- Khi có dự báo: 2.328 lượt đúng hẹn cho cả ba cách. Độ dài thêm của lời hứa: 7,4 s so với 37,2 s. Tới sớm quá 60 s: 4 trên 2.338 khách so với **[số trên mẫu số]**.
- Cộng dồn: 98 lần chạy, 64.371 quyết định, 1.256 bản ghi chặn, 0 bản ghi chặn chỉ vì cộng dồn (DY:356).

### 2.4 Hộp "Không nhận là mới" (DY:492-513)

Sự trung thực ở đây là điểm mạnh, và tôi đánh giá cao. Tuy vậy, mười gạch đầu dòng chỉ toàn câu phủ định đọc lên có vẻ phòng thủ, và hội đồng khó thấy được phần còn lại là gì. Đề xuất đổi thành một bảng hai cột, đặt ở §1.4:

| Đã có trong văn liệu hoặc thực tiễn | Khóa luận dùng lại hay làm thêm |
|---|---|
| So với kế hoạch cũ để tách phần tắc đường (Hörl–Zwick 2022) | Dùng lại làm mốc so sánh |
| Kiểm soát trước quyết định, đánh đổi phục vụ và ổn định (Fielbaum–Alonso-Mora 2020) | Dùng lại ý; đo trên một bài toán khác |
| Bảo đảm cho từng khách (Elmi và cộng sự 2026) | Dùng lại ý |
| Hạn chót tính từ lời hứa đầu (Schulz–Pfeiffer 2026) | Cài lại phần hạn chót để làm đối chứng |
| Báo giờ theo dự báo theo giờ trong ngày | Dùng lại |
| Chèn khách động, gán lại, giới hạn ETA | Dùng lại |
| **Hạn mức chung cho mọi khách, trên cả chuyến, tính riêng phần do điều phối** | **Đặc tả, cài đặt trong hệ điều phối, đo đánh đổi** |

Các câu "không nói C phục vụ nhiều hơn…" (DY:500-513) nên chuyển sang §5.2. Ở chương 1 chỉ giữ ba câu quan trọng nhất:

- không quy trách nhân quả;
- không suy rộng;
- không gọi 30 s là tối ưu.

---

## 3. Câu hỏi khi bảo vệ (13 câu, xếp từ nguy hiểm nhất)

Mức chuẩn bị có ba bậc:

- **Đủ**: dàn ý đã có chỗ và có nội dung để trả lời.
- **Một phần**: có số liệu nhưng thiếu lập luận, hoặc ngược lại.
- **Chưa**: chưa có chỗ trả lời.

| # | Câu hỏi (rút gọn) | Mức chuẩn bị |
|---|---|---|
| Q1 | Đệm 30 s cho cùng kết quả, vậy cần luật C làm gì? | Một phần |
| Q2 | Cộng dồn và hai chiều chưa từng có tác dụng, vậy C khác gì trần từng lần dời? | Một phần |
| Q3 | Đối chứng có công bằng không (hạn chót ở 30 s, không cài Hörl–Zwick)? | Một phần |
| Q4 | Trừ hết danh sách "không nhận là mới", phần nào là của em? | Một phần |
| Q5 | Đi chung giảm từ 22,8% xuống 13,4%; ít trễ hơn có phải chỉ vì phục vụ ít hơn? | Một phần |
| Q6 | Chênh 31 lượt trên 3.672 yêu cầu có vượt nhiễu không? | Chưa |
| Q7 | Độ tin cậy đến từ hạn mức hay từ bộ chọn ưu tiên ổn định? | Một phần (Đủ nếu Stage 1b chạy) |
| Q8 | Ví dụ mở đầu minh họa dự báo; phần do điều phối chỉ chiếm 1,3%? | Một phần |
| Q9 | Vì sao chọn B = 30 s, và chọn trên dữ liệu nào? | Một phần |
| Q10 | Cuối tuần không có dự báo, vậy 2.328 trên 34 ô được tính thế nào? | Chưa |
| Q11 | Hệ thống được cài và kiểm thử ra sao, chạy chậm đi bao nhiêu? | Chưa (thời gian), Một phần (kiến trúc) |
| Q12 | Mốc "giữ nguyên kế hoạch" có thật sự tách được phần do điều phối? | Đủ (nhưng phải sửa câu 1) |
| Q13 | Quy mô và độ thật của mô phỏng? | Đủ |

### Q1. "Đã có dự báo thì cộng thêm 30 giây là đủ. Vậy em cần luật C để làm gì?"

- **Vì sao nguy hiểm.** Đây là đối chứng đơn giản nhất và rẻ nhất để cài. Theo chính dàn ý, nó hòa với luật C ở ngưỡng 60 s (cùng 2.328 lượt) và thắng ở ngưỡng 120 s (2.366 so với 2.338) (DY:353, DY:472-474). Nếu cách đệm không làm thay đổi việc điều phối, nó có thể còn phục vụ nhiều lượt hơn luật C. Dàn ý không ghi số lượt phục vụ của cách đệm trong câu (6), nên tôi không biết. Phải xem trong Bảng 4.4.
- **Dàn ý đã có:**
  - Số liệu trong §4.2.
  - Hai điểm luật C hơn: lời hứa chỉ dài thêm 7,4 s so với 37,2 s, và ít khách tới sớm hơn.
  - Giới hạn theo cấu tạo: phần dời do điều phối của một khách tối đa 29,2 s dưới luật C, so với 590,1 s khi không giới hạn (DY:354).
- **Còn thiếu: lý do vì sao lời hứa ngắn hơn và ít tới sớm là có giá trị.**
  - §2.5 chỉ có 0,5 trang và tránh quy đổi ra tiền (DY:334).
  - DY:508 cấm nói về lợi ích kinh doanh.
  - Vì vậy, hiện khóa luận chưa có câu nào trả lời câu hỏi này.
- **Đề xuất.** Thêm khoảng 0,5 trang "Khi nào chọn hạn mức, khi nào chọn đệm" vào §4.2 hoặc §4.11, nói thẳng ba ý:
  - Trên dữ liệu này, cách đệm là một lựa chọn cạnh tranh.
  - Hạn mức cho một cam kết theo từng khách về phần dời do điều phối; cách đệm không có cam kết đó.
  - Khách có coi trọng cam kết đó không thì nằm ngoài phạm vi của khóa luận.

### Q2. "Câu (2) nói luật C cộng dồn và tính hai chiều. Câu (7) nói cộng dồn chưa từng có tác dụng, còn bộ sinh chỉ chèn nên giờ trả không bao giờ bị kéo sớm. Vậy trên thực nghiệm, luật C khác gì một trần cho từng lần dời, và khác gì Hörl–Zwick?"

- **Dàn ý đã có:**
  - §4.5 dài 1,5 trang (DY:356).
  - Câu (7).
  - Hướng phát triển (1): so sánh cộng dồn với trần từng lần (DY:372).
  - Danh sách "không khẳng định" (DY:506-507).
  - Bộ sinh chỉ chèn, nên c ≥ 0 (DY:140; LV tr. 17–18 và 30, PDF 34 và 46).
- **Còn thiếu: phần đóng góp vẫn đang "bán" hai tính chất mà dữ liệu chưa kích hoạt.**
  - Nên đưa chúng sang mục "tính chất thiết kế, chưa được dữ liệu kích hoạt".
  - Cần chuẩn bị một bảng đặt công thức 7 của Hörl–Zwick cạnh luật C, chỉ rõ điểm khác nào thực sự có tác dụng trên 34 ô.
  - Trước khi viết, cần kiểm xem trên 34 ô có lần nào c < 0 không. Nếu không có, không được nêu "hai chiều" là điểm khác.

### Q3. "Đối chứng có công bằng không?"

- **Câu hỏi đầy đủ.** "Luật hạn chót được thử ở 30 s, chặt hơn 30 lần mức 15 phút của Schulz–Pfeiffer (LV tr. 4, PDF 20). Luật đó do em tự cài, với luật phục hồi do em chọn. Cách của Hörl–Zwick không được cài làm đối chứng. Như vậy có phải em chọn sân nhà cho luật C không?"
- **Dàn ý đã có:**
  - Tỉ lệ quyết định phải phục hồi của luật hạn chót giảm khi nới B, từ 58,6% xuống 1,7% (DY:355). Số này nằm trong bảng của bộ chỉnh hạn mức.
  - Dòng M⁺-60 trong Bảng 4.4 (DY:353).
  - Câu "phần hạn chót của S&P, không phải phương pháp của họ" (DY:343).
  - Đối chứng Hörl–Zwick mới chỉ là hướng phát triển (DY:372).
- **Còn thiếu:**
  - Câu mở §4.2 cần nói thẳng rằng ở B = 30 s, luật hạn chót đang chạy xa vùng mà nó được thiết kế.
  - Đưa đường "tỉ lệ phục hồi theo B" lên hình ở chính văn.
  - Chuẩn bị câu trả lời vì sao chưa cài Hörl–Zwick (thời gian, phạm vi).

### Q4. "Trừ hết danh sách 'không nhận là mới' thì phần nào là của em?"

- **Dàn ý đã có:** hộp ở §1.4 và đoạn ở phần 3.
- **Còn thiếu:**
  - Một câu trả lời gói trong một đến hai câu.
  - Bảng "kế thừa / làm thêm" như ở mục 2.4.
  - Phần đóng góp kỹ thuật cần được nói rõ: cài trong một hệ điều phối thật nối với bộ mô phỏng, có sổ theo dõi kiểm lại được, và đo được đánh đổi.
  - Theo ý tôi, đó là đóng góp hợp lệ của một khóa luận ngành CNTT. Quy chế của trường về mức "mới" thì tôi chưa kiểm chứng.

### Q5. "Luật C phục vụ ít hơn 96 lượt, tỉ lệ đi chung giảm từ 22,8% xuống 13,4%. Với dịch vụ đi chung, mất gần nửa phần đi chung có phải là quá đắt? Và 127 lượt trễ ít hơn có phải chỉ vì phục vụ ít hơn?"

- **Dàn ý đã có:**
  - Tỉ lệ đi chung giảm từ 22,8% xuống 13,4%.
  - Tập khách được phục vụ: 2.207 khách chung, 227 khách chỉ U phục vụ, 131 khách chỉ C phục vụ.
  - Đúng hẹn tính trên 3.672 yêu cầu (DY:353).
- **Còn thiếu:**
  - Con số 22,8% xuống 13,4% chưa có trong phần đóng góp và tóm tắt, dù đây là cái giá dễ thấy nhất.
  - Dàn ý chưa định đo số lượt trễ trên 2.207 khách chung. Đó là cách tách "ít trễ vì ít phục vụ" khỏi "ít trễ nhờ luật C".
  - Đề xuất thêm chỉ tiêu này vào Bảng 4.4 hoặc phần chữ của §4.2, nếu dữ liệu theo từng khách đã có. Điều này tôi chưa kiểm chứng.

### Q6. "Chênh 31 lượt đúng hẹn trên 3.672 yêu cầu (0,84 điểm phần trăm) có vượt nhiễu không? 34 ô không độc lập, 5 ngày, một hạt giống, có ô đã được xem trước."

- **Dàn ý đã có:**
  - Một dòng trong phần hạn chế (DY:362).
  - Tách theo khung giờ: −39, −52, −5 (DY:353).
  - Sàn nhiễu ±0,3 điểm phần trăm, nhưng chỉ cho bộ thử tĩnh và đặt ở phụ lục A (DY:382).
- **Còn thiếu: chưa có chỗ cho phân tích độ vững của kết quả chính.**
  - Đề xuất một bảng nhỏ, khoảng 0,5 trang, theo 5 ngày × 3 khung giờ. Mỗi ô của bảng ghi hiệu C − U về đúng hẹn và về trễ.
  - Ghi thêm số ô mà ở đó C không thua U.
  - Phải giải thích "ô đã được xem trước" là những ô nào và vì sao được xem trước.
  - Bảng này không cần chạy thêm, với điều kiện kết quả theo ô đã có.

### Q7. "Độ tin cậy đến từ hạn mức hay từ bộ chọn ưu tiên ổn định?"

- **Dàn ý đã có:** §4.6 dài 2,5 trang, phép sàng lọc trên trạng thái cố định, chỗ dành cho Stage 1b và bản dự phòng (DY:357, DY:429-441).
- **Câu trả lời mạnh nhất đang bị giấu ở DY:342:** cấu hình U và C-30 "chỉ khác nhau ở hardLimit 30000". Nghĩa là hai luật dùng chung bộ chọn, nên hiệu giữa C và U là do hạn mức gây ra, với bộ chọn được giữ nguyên.
  - Nên đưa câu này lên làm câu mở đầu §4.6.
  - Phần còn mở chỉ là: kết quả có còn đúng với bộ chọn ưu tiên chi phí hay không.

### Q8. "Ví dụ mở đầu cho thấy dự báo có ích, mà dự báo không phải của em. Phần do điều phối chỉ chiếm 1,3% số giây trễ ngày thường. Vậy luật C đang giải một vấn đề nhỏ?"

- **Dàn ý đã có:**
  - H1.1 (DY:320).
  - Ví dụ một quyết định thật ở §4.3: 79,0 s do tắc đường cộng 68,3 s do điều phối, tổng 147 s, lớn hơn 90 s (DY:354).
  - Con số 1,3 / 86,1 / 12,6% ở H4.3 (DY:358).
- **Còn thiếu:**
  - Dàn ý không nói ba con số 1,3 / 86,1 / 12,6% đo dưới luật nào. Nếu đo dưới luật C thì 1,3% là kết quả của chính luật C, không thể dùng làm động lực.
  - Để làm động lực, nên dùng số khi không giới hạn. DY:354 cho biết trong 203 lượt trễ quá 60 s khi không giới hạn, 134 lượt thuộc nhóm "bị điều phối dời". Cần định nghĩa rõ "bị điều phối dời".
  - H1.1 nên chọn một khách mà phần do điều phối nhìn thấy được, hoặc vẽ đủ ba phần trên cùng một khách.

### Q9. "Vì sao B = 30 s? Chọn trên dữ liệu nào?"

- **Dàn ý đã có:** §4.4 coi B như một núm vặn và không gọi mức nào là "tối ưu". Dàn ý cũng nói 30 s không phải ngưỡng cảm nhận của khách (DY:355, DY:511). Stage 1a đang chờ (DY:410-427).
- **Còn thiếu: trình tự thời gian.**
  - Mức 30 s được chọn trước hay sau khi xem 34 ô thử?
  - Bộ chỉnh hạn mức chạy ngày 12–13/11, còn bộ thử chính chạy ngày 14–18/11 (DY:352). Nếu chọn B trên các ngày tách riêng, đó là một điểm mạnh, cần nói ra.
  - Nếu không chọn như vậy, phải nói thật.

### Q10. "Dự báo không có ngày nguồn cho cuối tuần, kết quả dự báo chỉ tính trên 21 ô ngày thường. Vậy con số 2.328 trên 34 ô ở câu (6) tính dự báo cho 13 ô còn lại như thế nào?"

- **Căn cứ.** Câu hỏi đặt ra từ DY:344 ("no source day at weekends") và DY:358 ("21 weekday cells").
- **Mức chuẩn bị: Chưa.** Dàn ý không nói rõ. Có thể cuối tuần dùng giờ báo không dự báo, nhưng tôi không biết. Đây là chỗ dễ bị coi là mâu thuẫn số liệu. Cần một câu chú thích dưới Bảng 4.4 và ở §4.7.

### Q11. "Hệ thống em cài gồm những gì, kiểm thử thế nào, và luật C làm mỗi lần quyết định chậm đi bao nhiêu?"

- **Dàn ý đã có:**
  - §3.7 dài 2 trang: bảng kiến trúc, bộ sinh chèn, bản ghi và mã băm, tính lại độc lập (DY:346).
  - Số dòng mã chưa được xác nhận (DY:596).
  - Lỗi "chín dự án" nhưng bảng chỉ có bảy dòng (DY:244). Bản trích của Bảng 3.6 cũng chỉ có bảy tên thành phần (LV tr. 31, PDF 47).
- **Còn thiếu:**
  - Thời gian tính cho mỗi chu kỳ quyết định, có và không có hạn mức. Tôi chưa kiểm được nhật ký chạy có lưu thời gian hay không.
  - Số lượng và loại kiểm thử.
  - Sơ đồ trao đổi giữa RideBound và FleetPy. Bản cũ chỉ có một câu: "giao thức nhị phân có kiểm tra băm ở từng khung tin" (LV tr. 30, PDF 46).
  - Với ngành CNTT, hội đồng gần như chắc chắn sẽ hỏi câu này.

### Q12. "Mốc 'giữ nguyên kế hoạch cũ' có thật sự tách được phần do điều phối không, khi nó gồm cả tiến độ thực của xe?"

- **Dàn ý đã có:**
  - §3.2 nói rõ e gồm tiến độ thực hiện (DY:341).
  - §3.6 nói đây là phép chiếu mô hình (DY:345).
  - Danh sách "không quy trách nhân quả" (DY:505).
  - Bản cũ có một đoạn tốt về việc "không được gọi d là tác động thuần của giao thông" (LV tr. 21, PDF 37).
- **Mức chuẩn bị: Đủ.** Chỉ cần sửa câu (1) như ở mục 2.2.

### Q13. "Quy mô và độ thật của mô phỏng?"

- **Câu hỏi đầy đủ.** "8 xe, 108 yêu cầu mỗi ô, trung bình 0,54 khách trên xe so với khoảng 1,33 trong FleetPy 2026, mạng là bao đóng 96 điểm, một hệ số tắc đường cho cả thành phố, thời gian dừng đỗ 0 s. Kết luận có còn đúng khi xe đông khách hơn?"
- **Dàn ý đã có:** §1.5, §4.11 và hướng phát triển (4) (DY:324, DY:362, DY:372). Bản cũ có lý do chọn quy mô nhỏ: so sánh có kiểm soát (LV tr. 8, PDF 24).
- **Mức chuẩn bị: Đủ ở mức nêu hạn chế.** Nên thêm một câu nói hướng ảnh hưởng dự đoán khi tải cao, và ghi rõ đó chỉ là giả thuyết.

---

## 4. Bố cục và số trang

### 4.1 So sánh phân bổ trang

| Phần | Bản hiện tại (105 tr.) | Dàn ý (74 tr.) | DACN (50 tr.) |
|---|---:|---:|---:|
| Trang đầu (bìa đến ký hiệu) | 16 | 10 | 12 (PDF 1–12) |
| Ch.1 Đặt vấn đề | 9 | 7 | 4 (tr. 1–4) |
| Ch.2 Cơ sở lý thuyết | 6 | 6 | 8 (tr. 5–12) |
| Ch.3 Phương pháp | 17 | 12 | 16 (tr. 13–28) |
| Ch.4 Thực nghiệm | 46 | 27 | 6 (tr. 29–34) |
| Ch.5 Kết luận | 7 | 4 | 2 (tr. 35–36) |
| Tài liệu tham khảo | 4 | 4 | 2 (tr. 37–38) |
| Phụ lục | 0 | 4 | 0 |
| Tỉ trọng Ch.4 trong phần thân (Ch.1–5) | 54% | 48% | 17% |
| Tỉ trọng Ch.3 trong phần thân | 20% | 21% | 44% |
| Số bảng / số hình | 48 / 2 (PDF 12–14) | khoảng 18 / khoảng 9 (DY:313) | 13 / 3 (PDF 10–11) |

Số trang của dàn ý cộng lại đúng 74 (DY:27-37). Phần cộng của chương 4 cũng khớp: 26,5 trang, còn 0,5 trang dự phòng (DY:364).

### 4.2 Nhận xét từng chương

- **Trang đầu, 10 trang (DY:303-314).** Hợp lý. Chuyện bìa và lời cam đoan xem ở mục 5.
- **Chương 1, 7 trang.**
  - §1.3 dành 2 trang cho vị trí so với các công trình gần nhất, trong khi chương 2 còn 3 trang nữa (§2.2–2.3). Hai phần trùng nhau. Đề xuất §1.3 còn khoảng 1,25 trang, dùng một bảng ngắn và không có công thức.
  - Chưa có câu hỏi nghiên cứu. DACN có mục "Mục tiêu chính" (DACN tr. 3, PDF 15). Đề xuất ghi ba câu hỏi ở §1.4:
    1. Hạn mức được gì và mất gì so với không giới hạn, với hạn chót, với đệm?
    2. Nới hạn mức thì được thêm gì?
    3. Phần tắc đường đoán trước được và phần còn lại lớn cỡ nào?
  - Phạm vi chỉ được 0,5 trang chung với cấu trúc báo cáo (DY:324). Như vậy là chật. Nên tăng lên 0,75 trang và viết phạm vi bằng gạch đầu dòng như DACN tr. 3.
- **Chương 2, 6 trang.**
  - Tổng số trang ổn.
  - Đã nêu ở mục 1.4: Bảng 2.2 dùng ký hiệu của chương 3 (DY:332).
  - Bảng 2.2 cần thêm một dòng "Hạn mức dời giờ (khóa luận)" với cùng các cột, để hội đồng thấy khác biệt ngay trong một bảng. Hiện bảng chỉ có các dòng của văn liệu.
- **Chương 3, 12 trang.**
  - Với một khóa luận CNTT mà hệ thống là sản phẩm chính, 12 trang là hơi mỏng. DACN dành 16 trang cho chương phương pháp.
  - §3.7 (cài đặt) chỉ có 2 trang (DY:346).
  - Thiếu mục phát biểu bài toán. Xem mục 4.4.
- **Chương 4, 27 trang.**
  - Tổng số trang hợp lý cho một khóa luận mà đóng góp chính là đo đánh đổi.
  - Có 11 mục, mỗi mục 0,75 đến 5 trang, nên chương bị vụn. Đề xuất gom theo câu hỏi nghiên cứu:
    - Câu hỏi 1 (phần do điều phối): §4.2–4.6.
    - Câu hỏi 2 (phần tắc đường đoán trước): §4.7.
    - Câu hỏi 3 (phần còn lại): §4.8.
  - Đầu chương nên có một bảng nhỏ "câu hỏi → mục → bảng". Bảng lộ trình cũ bị bỏ vì chứa câu nói quá (DY:147), nhưng một bản đã làm sạch vẫn rất có ích cho hội đồng.
- **Chương 5, 4 trang.** Hợp lý. §5.2 (hạn chế) trùng với §4.11, nên chỉ cần 0,5 trang trỏ về §4.11, cộng phần nói về chỗ trùng với văn liệu.
- **Tài liệu tham khảo.** Xem điểm 10 ở mục 4.4.
- **Phụ lục, 4 trang.** Nên giảm xuống không quá 2 trang. Xem mục 5, quyết định 5.

### 4.3 Những phần thừa

1. **§4.9 về học máy (0,75 trang, DY:360).** Đây là một hướng phụ, có kết quả âm. Người đọc sẽ thắc mắc vì sao lại có học máy. Chỉ nên giữ 2–3 dòng trong §4.11.
2. **§4.8 về chiều tuyết (1,5 trang, DY:359).** Nên giữ vì đây là hạn chế trung thực. Nhưng sáu biến thể chạy lại (41, 34, 21, 19, 29, 27) phần lớn là phân tích sau sự việc. Nên giảm còn khoảng 1 trang, giữ 2–3 dòng.
3. **Phụ lục B (1,5 trang, DY:383).** Nhận xét 3.1 đã nằm trong chính văn. Phụ lục B chỉ giữ lại khung bốn họ cổng, mà dàn ý đã gọi khung này là "lỗi thời" (DY:135), và thí nghiệm đi kèm khung đó đã bị cắt (DY:157).
4. **Hai bảng so sánh công trình liên quan.** Bảng 1.1 (DY:322) và Bảng 2.2 (DY:332) có các cột gần giống nhau. Nên giữ một bảng ngắn ở chương 1 và một bảng đầy đủ ở chương 2, hoặc gộp thành một.
5. **Bảng 4.4 có 10 dòng × 8 cột (DY:353, DY:521-524).** Bảng quá rộng cho khổ A4 với cỡ chữ 13. Bảng này còn trộn cả ba phần ngay ở §4.2, trước khi §4.7 trình bày dự báo, nên trái với luật 1 (DY:277). Đề xuất tách thành hai bảng:
   - 4.4a ở §4.2, không có dự báo: U, C-30, M⁺-30, V-30, M⁺-60.
   - 4.4b ở §4.7, có dự báo và đệm: U + dự báo, + đệm 30 s, + đệm 60 s, C-30 + dự báo, M⁺-30 + dự báo.

### 4.4 Những phần thiếu

1. **Phát biểu bài toán: đầu vào, quyết định, đầu ra.**
   - DACN có §3.2.1 "Đầu vào, đầu ra và biểu diễn phương án" (DACN tr. 15, PDF 27).
   - Dàn ý có bài toán chuẩn ở §2.1 và bảng ràng buộc ở §3.3, nhưng không có chỗ nói gọn: trong mỗi chu kỳ, hệ thống nhận gì, quyết định gì, công bố gì, ràng buộc nào là cứng, và đánh giá bằng chỉ tiêu nào.
   - Đề xuất thêm khoảng 0,5 trang ở đầu §3.2.
2. **Hình minh họa bài toán.**
   - Dàn ý có H1.1 (dòng thời gian của một khách), H1.2 (ba phần → ba chỗ) và H3.1 (vòng quyết định).
   - Chưa có hình cho chính hiện tượng: một xe đang chở khách A, nhận thêm khách B, lộ trình đổi, và giờ trả của A bị dời. Với người ngoài, đây là hình quan trọng nhất.
   - H3.2 (mũi tên x, c, z trên trục thời gian) đang chỉ là tùy chọn (DY:341). Nên chuyển thành bắt buộc, và có thể ghép chung với hình chèn khách.
3. **Giả mã cho trọn một chu kỳ quyết định.**
   - Dàn ý có Giải thuật 3.1 (kiểm hạn mức) và 3.2 (lời hứa theo dự báo) (DY:342, DY:344).
   - DACN có giả mã tổng thể "OptimizeGroupJourney" (DACN Bảng 3.8). Dàn ý chưa có giả mã tương đương. Một giả mã như vậy gồm các bước: nhận sự kiện → sinh phương án → tính v, e, p → lọc theo hạn mức → giải bài toán quy hoạch nguyên → công bố → cập nhật sổ.
   - Luật phục hồi "không tệ hơn tham chiếu" của luật hạn chót cũng nên có vài dòng giả mã. Đây là chi tiết khó hiểu nhất đối với hội đồng.
4. **Độ phức tạp và thời gian tính.** DACN có Bảng 3.9 về độ phức tạp và cột "Xử lý TB" (DACN tr. 28 và 30). Dàn ý không có cả hai. Tôi đã tìm từ khóa runtime, độ phức tạp, thời gian xử lý trong dàn ý và không thấy.
5. **Phần cài đặt hệ thống.** Nên tăng lên khoảng 3 trang, gồm:
   - sơ đồ thành phần;
   - luồng của một lần quyết định giữa FleetPy và RideBound;
   - cách kiểm thử các bất biến;
   - thời gian tính.
   Khi đưa số dòng mã vào, phải đếm lại (DY:596).
6. **Độ vững của kết quả chính:** bảng theo ngày × khung giờ, và số trễ trên tập khách chung (Q5, Q6).
7. **Quy ước dấu và câu "cách đọc bảng".**
   - Dàn ý viết "C vs U (−96, −127, +31)" (DY:353) nhưng không nói hiệu được tính theo chiều nào.
   - DACN có câu mẫu: "giá trị âm nghĩa là Optigo có tổng chi phí thấp hơn" (DACN tr. 31, PDF 43).
8. **Định nghĩa giả thiết (N) ngay tại Nhận xét 3.1.** Ở bản cũ, (N) được nhắc tới ở LV tr. 22 (PDF 38) và định nghĩa ở §3.5.5. Mục §3.5.5 bị cắt, nên (N) phải được định nghĩa lại ở §3.3 (DY:342).
9. **Ngôi viết.**
   - Bản cũ dùng "chúng tôi" (LV tr. 2 và 4, PDF 18 và 20), trong khi lời cảm ơn dùng "em".
   - DACN dùng cách viết trung tính: "đề tài", "hệ thống", "báo cáo".
   - Nên thống nhất một cách. Quy định của trường về ngôi viết thì tôi chưa kiểm chứng.
10. **Lỗi trình bày ở tài liệu tham khảo.**
    - Trang PDF 102 (tr. 86) chỉ có tiêu đề "Tài liệu tham khảo".
    - Danh mục thật bắt đầu ở PDF 103 với tiêu đề tiếng Anh "Bibliography".
    - Dàn ý chưa ghi lỗi này (DY:180-200 chỉ bàn về nội dung). Sửa lỗi này có thể tiết kiệm khoảng 1 trang.
    - DACN chia danh mục thành "Tiếng Việt" và "Tiếng Anh" (DACN PDF 49). Có nên chia như vậy không phải kiểm mẫu của trường; tôi chưa kiểm chứng.

### 4.5 Đề xuất phân bổ lại, vẫn khoảng 73–74 trang

| Mục | Dàn ý | Đề xuất | Chênh |
|---|---:|---:|---:|
| §1.3 Công trình gần nhất | 2 | 1,25 | −0,75 |
| §1.5 Phạm vi và cấu trúc | 0,5 | 0,75 | +0,25 |
| §3.1 Tổng quan (thêm giả mã một chu kỳ) | 1,5 | 2 | +0,5 |
| §3.2 (thêm phát biểu bài toán) | 2 | 2,5 | +0,5 |
| §3.7 Cài đặt, kiểm thử, thời gian tính | 2 | 3 | +1 |
| §4.2 (tách bảng, thêm 0,5 trang độ vững, dùng 0,5 trang dự phòng) | 5 | 5 | 0 |
| §4.8 Chiều tuyết | 1,5 | 1 | −0,5 |
| §4.9 Học máy (chuyển vào §4.11) | 0,75 | 0,25 | −0,5 |
| §5.2 Hạn chế (trỏ về §4.11) | 1 | 0,5 | −0,5 |
| Phụ lục B | 1,5 | 0 | −1,5 |
| Bìa: thêm bìa lót nếu mẫu trường giống DACN (chưa kiểm chứng) | 2 | 3 | +1 |
| **Tổng chênh** | | | **−1** |

---

## 5. Các quyết định ở DY:556-577

**1. Định lý (DY:558-560). Khuyên chọn (b) nhưng bỏ phụ lục B: gọi là "Nhận xét 3.1" và chứng minh trong vài dòng.**
- Tính chất "luật C không bao giờ loại phương án giữ nguyên" đúng theo cấu tạo, vì phần dời của phương án giữ nguyên bằng 0. Hạn chót nới kiểu Hörl–Zwick cũng có tính chất này (DY:342, DY:502-503).
- Một người có nền tối ưu sẽ hỏi ngay "định lý này có tầm thường không". Gọi là "Nhận xét" thì tránh được câu đó mà vẫn giữ được tính chặt chẽ.
- Không nên giữ phụ lục B. Phụ lục vẫn là một phần của khóa luận, vẫn có thể bị hỏi. Trong khi đó, thí nghiệm đi kèm khung bốn họ cổng đã bị cắt (DY:157). Đừng để trong phụ lục một thứ mà em không muốn bị hỏi.
- Phần đáng giữ của khung cũ là bảng "mỗi luật kiểm cái gì và hỏng khi nào". Bảng này đặt ở §3.4 (DY:135, DY:343).
- Đây là ý kiến về thông lệ học thuật nói chung. Trường có ưu tiên dạng định lý hay không thì tôi chưa kiểm chứng.

**2. Tên giảng viên hướng dẫn (DY:562-563).** Đồng ý: không điền tên ThS. Trần Mạnh Cường, vì đó là giảng viên của môn DACN (DACN PDF 2–3). Tuy vậy, khóa luận chưa có tên giảng viên hướng dẫn thì không thể nộp. Đây là việc phải giải quyết trước tiên, theo quyết định giao đề tài chính thức.

**3. Bìa tiếng Anh và Abstract (DY:564-565). Khuyên giữ cả hai cho đến khi kiểm được mẫu chính thức.**
- Căn cứ duy nhất tôi có là báo cáo DACN của chính sinh viên, cùng trường. Báo cáo đó có:
  - bìa ngoài tiếng Việt không ghi giảng viên hướng dẫn (PDF 1);
  - bìa lót tiếng Việt có giảng viên hướng dẫn (PDF 2);
  - bìa tiếng Anh (PDF 3);
  - Abstract (PDF 6).
- Bản luận văn hiện tại chỉ có một bìa tiếng Việt và một bìa tiếng Anh (LV PDF 1–2).
- Bỏ một trang mà mẫu bắt buộc thì tệ hơn nhiều so với tốn thêm 2 trang trong mức trần 79 trang. Abstract nên dịch đúng phần tóm tắt mới và không dài quá một trang.
- Cả DACN lẫn luận văn hiện tại đều không có trang "Lời cam đoan". Mẫu khóa luận có bắt buộc trang này không thì tôi chưa kiểm chứng. Nên hỏi giáo vụ khoa hoặc lấy mẫu chính thức.
- Mẫu khóa luận có giống mẫu báo cáo môn học không cũng chưa kiểm chứng.

**4. Tên đề tài (DY:566-569). Khuyên đổi sang một tên ngắn, nêu bài toán trước, không có "chứng nhận".**
- Tên hiện tại "Lời hứa có biên được chứng nhận…" (16 âm tiết) là dịch sát từ "certified bounded":
  - "Có biên" khó hiểu.
  - "Chứng nhận" gợi ý có bên thứ ba cấp chứng nhận, trong khi phần niêm phong và chứng cứ đã bị bỏ.
- Tên thay thế mà dàn ý đề xuất dài 26 âm tiết. Nó liệt kê cả hai thành phần không phải của khóa luận (dự báo, sổ cái), dễ kéo hội đồng hỏi vào đúng chỗ yếu, và có thuật ngữ "sổ cái".
- Gợi ý (đều khoảng 17–18 âm tiết):
  - "Giới hạn việc dời giờ trả do điều phối trong dịch vụ xe đi chung theo yêu cầu"
  - "Hạn mức dời giờ trả cho từng hành khách trong điều phối xe đi chung theo yêu cầu"
  - "Giữ giờ trả đã hứa với hành khách trong điều phối xe đi chung theo yêu cầu"
- Việc đổi tên đề tài sau khi đã đăng ký có được phép không, và hạn chót đổi là khi nào, thì tôi chưa kiểm chứng. Cần hỏi giảng viên hướng dẫn và khoa trước khi viết lại bìa.

**5. Phụ lục (DY:570). Khuyên có phụ lục, nhưng không quá 2 trang.**
- **Phụ lục C** (kiểm kê lần chạy, nơi lưu kết quả): nên giữ, vì phục vụ việc tái lập.
- **Phụ lục A** (bộ thử tĩnh): chỉ giữ nếu các số đã được gắn lại vào script tạo ra chúng. Dàn ý tự ghi rằng các số này chưa được kiểm lại ở các vòng 13–18 (DY:594-595).
- **Phụ lục B:** bỏ, như ở quyết định 1.
- Trường có cho phép phụ lục không, và phụ lục có tính vào giới hạn số trang không, thì tôi chưa kiểm chứng.

**6. Stage 1b (DY:571-572). Khuyên đặt một hạn chốt cứng, và viết trước bản dự phòng.**
- Q7 là điểm yếu thật về cách hiểu nhân quả của kết quả chính. Stage 1b là phép thử trực tiếp cho điểm này. Nếu kịp thì nên chạy.
- Stage 1b cần viết thêm code, qua bước kiểm tương đương và được chủ đề tài duyệt (DY:429). Đừng để nó kéo lùi cả khóa luận.
- Viết chương 4 theo bản dự phòng trước (DY:440-441), có số thì nâng cấp sau. Không đưa kết quả chạy dở vào luận văn.
- Stage 1a cũng làm như vậy (DY:426-427).
- Hạn nộp giữa tháng 11 là thông tin chưa kiểm chứng (DY:572).

**7. Cách gọi tên các luật (DY:573-574). Khuyên dùng tên tiếng Việt mô tả trong phần chữ, ký hiệu chỉ dùng trong bảng.**

| Ký hiệu (chỉ dùng trong bảng) | Tên trong phần chữ |
|---|---|
| U | điều phối không hạn mức (vẫn khóa xe và điểm dừng) |
| FREE | ghép tự do (không khóa, ưu tiên chi phí) |
| C-30 | hạn mức dời giờ 30 giây |
| M⁺-30 | luật hạn chót 30 giây |
| V-30 | luật theo giờ khách thấy 30 giây |
| U + dự báo + đệm 30 s | cộng thêm 30 giây vào lời hứa |

- Lý do:
  - Chữ C trùng với c thường, là phần dời có dấu.
  - Chữ B trùng với "chiến lược B" của Hörl–Zwick.
  - Ở phụ lục A còn có B1 và C1 của bộ thử tĩnh.
- Bảng 3.3 (DY:343) nên có thêm một cột "tên gọi trong bài" như trên.
- Câu đầu tiên dùng mỗi tên trong phần chữ nên ghi ký hiệu trong ngoặc.

**8–10. Các quyết định còn lại.**
- **Quy ước đếm lần chạy (DY:575):** đồng ý đếm "số lần chạy dùng trong khóa luận, theo bộ thử", và chỉ đưa vào một bảng ở phụ lục C. Không cộng lẫn các bộ thử trong phần tóm tắt, vì bản cũ có ba con số khác nhau (DY:228-232).
- **Thống kê "trễ quá 1 phút" (DY:576):** đồng ý chọn một định nghĩa (DY:260) và ghi định nghĩa đó dưới mỗi bảng.
- **Biên γ (DY:577):** không đưa vào, vì nó không nằm trong mạch chính.

---

## 6. So với báo cáo Dự án công nghệ (văn phong mà sinh viên muốn theo)

| Đặc điểm của DACN | Vị trí trong DACN | Dàn ý | Đánh giá |
|---|---|---|---|
| Mở đầu bằng một tình huống đời thường, câu ngắn | tr. 1 (PDF 13) | §1.1 kể về một khách thật, có H1.1 (DY:320) | Giữ được, và tốt hơn vì dùng dữ liệu thật. Nhưng ví dụ chưa minh họa luật C (Q8) |
| Hình quy trình ngay ở chương 1 | Hình 1.1, tr. 2 | H1.2 (DY:321) | Giữ được |
| Bảng định vị so với các nhóm giải pháp | Bảng 1.1, tr. 2 | Bảng 1.1 (DY:322) | Giữ được. Nên bỏ công thức và thêm một dòng hoặc một cột cho khóa luận |
| Phạm vi đề tài bằng gạch đầu dòng | tr. 3 | §1.5, 0,5 trang (DY:324) | Giữ một phần, còn chật |
| Mục tiêu và đóng góp bằng gạch đầu dòng ngắn | tr. 3–4 | Đoạn 7 câu, khoảng 30 con số (DY:450-478) | **Chưa giữ được.** Xem mục 2 |
| Bảng ràng buộc cứng và tiêu chí mềm | Bảng 3.1, tr. 16 | Bảng 3.2 (DY:342) | Giữ được, tốt |
| Đầu vào, đầu ra, biểu diễn phương án | §3.2.1, tr. 15 | Không có mục riêng | Thiếu (mục 4.4, điểm 1) |
| Giả mã dạng Require/Ensure, nhiều thuật toán | Bảng 3.2, 3.4, 3.5, 3.8 | Giải thuật 3.1, 3.2 (DY:342, DY:344) | Giữ một phần. Thiếu giả mã tổng thể |
| Bảng độ phức tạp | Bảng 3.9, tr. 28 | Không có | Thiếu |
| Giải thích từng chỉ tiêu và lý do chọn | §4.1, tr. 29–30 | Bảng 4.3 thuật ngữ, luật 6 (DY:292-300, DY:352) | Giữ được. Nên thêm "vì sao đo cái này" |
| Ghi đơn vị, ghi quy ước dấu | tr. 30–31 | Luật mẫu số (DY:280-286) | Giữ một phần. Thiếu quy ước dấu |
| Câu "Khi đọc Bảng 4.1, cần phân biệt…" | tr. 30 | Luật "trả lời trước" (DY:278-279) | Giữ một phần. Nên thêm câu cách đọc dưới mỗi bảng lớn |
| So sánh từng cặp trên cùng kịch bản | Bảng 4.2, tr. 31 | Tập khách chung 2.207 và 2.332 (DY:353) | Giữ được, và tốt hơn DACN |
| Tách kết quả theo nguồn dữ liệu | §4.4, tr. 32 | Tách theo khung giờ (DY:353) | Giữ được. Nên thêm tách theo ngày |
| Vai trò của từng thành phần (ablation) | §4.5, tr. 33 | Các dòng có hoặc không có dự báo, có hoặc không có đệm (DY:353, DY:358) | Có nhưng chưa gọi tên. Nên gọi rõ là "vai trò từng thành phần" |
| Thời gian xử lý | Cột "Xử lý TB", Bảng 4.1 | Không có | Thiếu |
| Thảo luận và giới hạn cuối chương | §4.6, tr. 34 | §4.11 (DY:362) | Giữ được |
| Tóm tắt có con số | **Không có**: chỉ viết "giảm đáng kể" (PDF 5) | Không quá 300 chữ, có 4–5 con số kèm mẫu số (DY:310) | Dàn ý tốt hơn. **Đừng theo DACN ở điểm này** |
| Giọng văn tự khen | Có, ví dụ "Đây là kết quả quan trọng nhất" (tr. 31) | Luật 4 cấm (DY:287-289) | Dàn ý tốt hơn |

**Kết luận về văn phong.** Trên giấy, dàn ý đã chép lại được những gì tốt nhất của DACN:

- bảng định vị;
- bảng ràng buộc;
- giả mã;
- trả lời trước rồi mới đưa bảng;
- đếm có mẫu số.

Chỗ lệch nằm ở đoạn văn duy nhất đã được viết thành câu, tức đoạn đóng góp. Đoạn này chưa theo văn phong DACN, cũng chưa theo luật của chính dàn ý. Các chương sẽ được viết theo cách của đoạn đó. Vì vậy nên sửa đoạn này trước, rồi dùng nó làm mẫu cho người viết từng chương.

---

## 7. Kết luận của người nhận xét

**Đánh giá chung.** Tôi đồng ý cho viết theo dàn ý này.

- Mạch lập luận chỉ có một hướng.
- Các câu nói quá của bản cũ đã được rà và cắt có hệ thống. Ví dụ: niêm phong, tiền đăng ký, "chỉ/duy nhất", và khung luật nghĩa vụ (DY:202-260).
- Các luật về mẫu số và từ ngữ bị cấm rõ ràng.
- Chỗ để trống cho các thí nghiệm đang chờ đều có bản dự phòng.

Đó là những điểm mà một hội đồng khó tính sẽ đánh giá cao.

**Bốn việc cần làm trước khi viết các chương:**

1. Viết lại đoạn đóng góp theo mục 2.3. Rút "cộng dồn" và "hai chiều" khỏi danh sách điểm khác. Ghi mẫu số cho mọi con số.
2. Chuẩn bị câu trả lời cho Q1 (đệm), Q3 (đối chứng) và Q5 (giảm đi chung, trễ trên tập khách chung), và dành chỗ cho chúng trong §4.2.
3. Thêm vào chương 3: phát biểu bài toán, giả mã một chu kỳ quyết định, hình chèn khách, và 3 trang về cài đặt có thời gian tính.
4. Thêm phân tích độ vững theo ngày × khung giờ cho kết quả chính (Q6). Trước đó phải kiểm xem số liệu theo ô đã có hay chưa.

**Những việc cần hỏi trường hoặc khoa (chưa kiểm chứng):**

- mẫu bìa: có bìa lót không, có bìa tiếng Anh không;
- có bắt buộc trang lời cam đoan không;
- có được đổi tên đề tài không, và hạn đổi;
- có bắt buộc Abstract không;
- phụ lục có tính vào giới hạn số trang không;
- có chia tài liệu tham khảo theo ngôn ngữ không;
- quy định về ngôi viết.

*Hết nhận xét. Tệp này do Claude viết ngày 10/10/2026 trong vai giảng viên hội đồng. Tôi không chạy mô phỏng và không sửa luận văn.*
