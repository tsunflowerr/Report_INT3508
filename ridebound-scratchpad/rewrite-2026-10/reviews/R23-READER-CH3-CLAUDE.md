# R23: Đọc chương 3 trong vai người ngoài ngành (Claude)

- Ngày: 2026-10-11
- Bản đọc: `rewrite-2026-10/drafts/07-chuong3.tex` (663 dòng, bỏ qua các dòng `%`).
- Vai đọc: sinh viên năm cuối ngành kinh tế hoặc điện tử. Biết toán phổ thông và một ít tích phân. Chưa từng nghe về điều phối xe đi chung, chưa đọc chương 1–2.
- Cách làm: đọc tuần tự một lượt và ghi lại mọi chỗ phải dừng, phải đoán hoặc phải đọc lại. Đọc xong chương mới mở `style/GLOSSARY-VI.md` để đối chiếu (mục 4). Không đọc tài liệu nào khác, không đọc các tệp `R23-*` khác.

**Quy ước.**
- Mức độ:
  - **Nặng**: tôi không hiểu và không đoán được, phải đọc thêm vài trang hoặc vẫn không hiểu.
  - **Vừa**: tôi đoán được nhưng không chắc.
  - **Nhẹ**: tôi hiểu nhưng vấp, câu nghe lạ.
- "Dòng" là số dòng trong tệp `.tex`. Bảng, hình và công thức được đánh số theo thứ tự xuất hiện trong chương:
  - Bảng 3.1 giả mã lượt quyết định; 3.2 ví dụ ba mốc; 3.3 ràng buộc và tiêu chí; 3.4 giả mã KiểmTrần; 3.5 các luật; 3.6 giả mã dự báo; 3.7 các thành phần.
  - Hình 3.1 vòng quyết định; 3.2 ba mốc; 3.3 bản tin.
  - Công thức (3.1) ba mốc; (3.2) luật C; (3.3) đồng nhất; (3.4) kéo dãn; (3.5) ba phần.
- Câu viết lại giữ nguyên nghĩa và mọi con số. Khi cần thông tin mà chương không có, tôi để `[TÁC GIẢ ĐIỀN: …]` hoặc `[TÁC GIẢ KIỂM: …]` chứ không tự bịa. Các ví dụ tôi thêm đều ghi "ví dụ dựng tay" và không phải số đo.

---

## 0. Tóm tắt

- **Tổng: 79 chỗ khó hiểu** (Nặng 15, Vừa 49, Nhẹ 15), cộng 5 vấn đề lặp lại trong cả chương (mục 3).
- **Chỗ đầu tiên tôi bị lạc:** dòng 35, "bảng giờ đi hiện tại, được coi là giữ nguyên cho phần đường còn lại" (mục A3).
- **Chỗ đầu tiên tôi lạc hẳn, phải đoán rồi đọc tiếp:** Bảng 3.1 dòng 9–11 (tệp dòng 105–110). Ba dòng này dùng năm khái niệm chưa định nghĩa (mục A12).
- **Chỗ khó nhất chương:** dòng 422–428 về tiêu chí 3 và con số "1.000.000 phần triệu" (mục D11). Tiếp theo là dòng 436–440 về hai luật phục hồi (mục D13).
- **Phần dễ hiểu nhất:** mục 3.2 và đầu mục 3.3. Ví dụ khách A, khách B (Bảng 3.2, Hình 3.2) là chỗ tôi "vỡ ra" cả chương. Hình ảnh "ngân sách thời gian" (dòng 240–241), ví dụ "ba lần 30 giây thành 90 giây" (dòng 243–244) và ba giới hạn có ví dụ số của Nhận xét 3.1 (dòng 346–351) đều rất rõ. Đoạn "không kết luận ai có lỗi" (dòng 535–538) và mục 3.7.3 về ai đã kiểm cũng viết rõ và trung thực.
- **Vấn đề lớn nhất về cấu trúc:**
  - Mục 3.1 dùng khoảng 15 thuật ngữ trước khi định nghĩa chúng.
  - Ví dụ quan trọng nhất để hiểu "xe bị ép" (dòng 407–410) nằm tận mục 3.4.
  - Mục 3.5 và 3.6 không có ví dụ số nào.

## 1. Đọc từng mục, ngắn gọn

| Mục | Tôi hiểu được bao nhiêu | Ghi chú |
|---|---|---|
| Mở đầu (17–21) | 30% | Năm khái niệm trong một câu, không có câu chuyện nào để bám. |
| 3.1 Bài toán, lượt quyết định (27–131) | 40% | Danh sách Đầu vào/Đầu ra dễ theo. Hình 3.1 và Bảng 3.1 đầy từ chưa học. |
| 3.2 Ba mốc (135–220) | 90% | Phần tốt nhất. Chỉ vấp ở "theo cấu tạo", "vế này". |
| 3.3 Luật C (224–352) | 70% | Định nghĩa và ví dụ rõ. Bảng 3.3 (tiêu chí 3), "mười chiều cam kết" và ba giai đoạn của khách thì không. |
| 3.4 Luật đối chứng, bộ chọn (356–440) | 35% | Bảng 3.5 có nhiều tên chưa giới thiệu. Đoạn Hörl–Zwick, đoạn tiêu chí 3 và đoạn luật phục hồi rất khó. |
| 3.5 Lời hứa theo dự báo (444–510) | 50% | Hiểu ý chung. Công thức tích phân không có trực giác, không có ví dụ. "Hệ số tắc đường" chưa định nghĩa. |
| 3.6 Sổ (514–538) | 55% | Hiểu có ba phần, nhưng phải tự kiểm đại số. Không có ví dụ một dòng sổ. |
| 3.7 Cài đặt (542–662) | 65% | Dễ theo nếu chấp nhận vài từ kỹ thuật. Thông tin "mô phỏng FleetPy, dữ liệu Manhattan" đến quá muộn. |

---

## 2. Danh sách chỗ khó hiểu, theo thứ tự dòng

### Mở đầu chương

**M1. Dòng 14, 17–18, 153 (Vừa)**
- Gốc: tiêu đề "Phương pháp: luật C, lời hứa theo dự báo và sổ theo từng khách"; dòng 18 "luật C dùng phần đó để loại phương án".
- Vì sao khó: chữ "C" có ngay ở tiêu đề nhưng cả chương không nói vì sao gọi là C. Tới dòng 153 ("Luật C chỉ tính c") tôi mới đoán C lấy từ đại lượng c. Người đọc dễ nhớ tên hơn khi biết tên từ đâu ra.
- Viết lại (dòng 18): "luật C, [TÁC GIẢ KIỂM: đặt tên theo đại lượng c, tức phần dời do điều phối], dùng phần đó để loại phương án".

**M2. Dòng 17–21 (Vừa)**
- Gốc: "Chương này trình bày cách khóa luận đo phần dời giờ trả do điều phối cho từng khách, luật C dùng phần đó để loại phương án, lời hứa theo dự báo, sổ theo dõi từng khách, và cách các thành phần này được cài đặt và kiểm tra trong RideBound."
- Vì sao khó: câu mở đầu có năm khái niệm (phần dời giờ trả do điều phối, phương án, lời hứa theo dự báo, sổ, RideBound) mà chưa khái niệm nào được giải thích. Người chưa đọc chương 1–2 không có hình ảnh nào để bám. Chương có một ví dụ rất hay (khách A, khách B, dòng 164–166) nhưng ví dụ đó nằm tận mục 3.2.
- Viết lại: "Khi đặt xe đi chung, khách được báo trước giờ xe sẽ trả mình tới nơi. Khóa luận gọi giờ này là lời hứa giờ trả, gọi tắt là lời hứa. Trong chuyến đi, giờ trả có thể bị dời: một phần vì đường đông hơn dự tính, một phần vì bộ điều phối quyết định ghé đón thêm người khác. Chương này trình bày năm nội dung. Thứ nhất là cách đo riêng phần dời do điều phối cho từng khách. Thứ hai là luật C: luật dùng phần đo được để loại những cách sắp xếp chuyến (gọi là phương án) làm khách bị dời quá nhiều. Ba nội dung còn lại là lời hứa theo dự báo, sổ theo dõi từng khách, và cách các thành phần này được cài đặt, kiểm tra trong RideBound."

### Mục 3.1 Phát biểu bài toán và tổng quan hệ thống

**A1. Dòng 30 (Vừa)**
- Gốc: "Bộ điều phối của RideBound làm việc theo từng lượt quyết định (decision epoch)."
- Vì sao khó: câu không nói lượt quyết định xảy ra khi nào (định kỳ, hay mỗi khi có khách mới?). Tới Hình 3.3 (dòng 604) tôi mới biết mỗi lượt bắt đầu bằng một "lô sự kiện".
- Viết lại: "Bộ điều phối của RideBound không quyết định liên tục mà theo từng lượt quyết định (decision epoch). Mỗi lượt bắt đầu khi bộ mô phỏng gửi tới một lô sự kiện mới: yêu cầu mới, xác nhận đặt xe, tiến độ xe, đón, trả, bảng giờ đi mới. [TÁC GIẢ ĐIỀN: lô được gửi khi nào, bao lâu một lần.] Bộ điều phối xử lý xong một lô rồi mới nhận lô sau."

**A2. Dòng 33–34, lặp lại trong cả chương (Vừa)**
- Gốc: "lịch sử lời hứa của các khách đã nhận"
- Vì sao khó: tôi tự nhiên đọc "khách đã nhận" thành "khách đã nhận được (xe, tiền…)". Tới dòng 36 ("nhận hay chưa nhận từng yêu cầu mới") tôi mới hiểu "nhận" ở đây là hệ thống đồng ý chở. Cụm này lặp lại hàng chục lần trong chương.
- Viết lại: lần đầu viết "các khách đã được nhận (tức khách mà hệ thống đã đồng ý chở)". Sau đó có thể giữ "khách đã nhận".

**A3. Dòng 35 (Vừa). ĐÂY LÀ CHỖ ĐẦU TIÊN TÔI BỊ LẠC**
- Gốc: "bảng giờ đi hiện tại, được coi là giữ nguyên cho phần đường còn lại."
- Vì sao khó: "bảng giờ đi" làm tôi nghĩ tới bảng giờ tàu, giờ xe buýt (giờ khởi hành). Tôi mất một lúc mới đoán ra đây là bảng thời gian di chuyển giữa các điểm. Vế "được coi là giữ nguyên cho phần đường còn lại" cũng phải đọc hai lần. Cụm "bảng giờ đi" còn xuất hiện ở các dòng 143, 145, 158, 299, 335, 447, 463, 605, nên cần rõ ngay từ đầu.
- Viết lại: "bảng thời gian đi giữa các điểm theo tình trạng đường lúc này (gọi tắt là bảng giờ đi); bộ điều phối giả định bảng này không đổi trong suốt phần đường còn lại."

**A4. Dòng 34, 40, 261, 509 (Vừa)**
- Gốc: có bốn cách gọi khác nhau:
  - "khoảng giờ đón" (dòng 34);
  - "cửa sổ đón" (dòng 40);
  - "Khách được đón trong vòng 10 phút kể từ lúc gọi" (dòng 261);
  - "giờ đón muộn nhất" (dòng 509).
- Vì sao khó: tôi đoán bốn cách gọi này là cùng một thứ nhưng không chắc. "Cửa sổ đón" là dịch từ tiếng Anh, tự nó không cho biết nghĩa.
- Viết lại (dòng 34): "…khoảng thời gian được phép đón (gọi là cửa sổ đón; trong thực nghiệm, khách phải được đón trong vòng 10 phút kể từ lúc gọi)…". Sau đó chỉ dùng "cửa sổ đón". Ở dòng 509 viết "muộn hơn cửa sổ đón cho phép".

**A5. Dòng 38–39 (Nặng)**
- Gốc: "Đầu ra: lời hứa giờ đón, giờ trả mới hoặc thay đổi (lời hứa đầu được công bố khi khách xác nhận đặt xe) và một dòng sổ cho mỗi lần công bố (mục 3.6)."
- Vì sao khó: đây là lần đầu chữ "lời hứa" có nội dung, nhưng không có câu nào định nghĩa nó. Chữ "công bố" được dùng như một thuật ngữ: công bố cho ai, hiện lên ứng dụng hay sao? "Dòng sổ" chưa biết là gì. Phần trong ngoặc đơn chen vào giữa làm gãy câu.
- Viết lại: "Đầu ra: giờ đón và giờ trả báo cho khách, khóa luận gọi là lời hứa. Lời hứa đầu được báo khi khách xác nhận đặt xe. Mỗi lần hệ thống báo giờ mới hoặc đổi giờ cũ gọi là một lần công bố. Mỗi lần công bố được ghi thành một dòng trong sổ theo dõi khách đó (mục 3.6)."

**A6. Dòng 40–41 (Vừa)**
- Gốc: "Ràng buộc cứng: cửa sổ đón, thời gian ngồi xe, sức chứa, các khóa và luật lời hứa (Bảng 3.3)."
- Vì sao khó: "ràng buộc cứng" (khác "mềm" ở chỗ nào?) và "các khóa" chưa được giải thích. Khóa chỉ được nói rõ ở Bảng 3.3, hai trang sau.
- Viết lại: "Ràng buộc cứng (điều kiện bắt buộc, vi phạm là bị loại ngay): cửa sổ đón, thời gian ngồi xe, sức chứa, các khóa (những phần đã hứa thì không được đổi, như xe và điểm đón) và luật lời hứa (Bảng 3.3)."

**A7. Dòng 42–43 (Vừa)**
- Gốc: "Đánh giá: lượt phục vụ, lượt trễ và tới sớm so với lời hứa đầu, độ dài thêm của lời hứa, số khách bị điều phối dời giờ trả"
- Vì sao khó: chữ "lượt" vừa được dùng cho "lượt quyết định" (dòng 30). Ở đây "lượt phục vụ", "lượt trễ" lại mang nghĩa khác (số khách hay số lần?). Tôi không hiểu "độ dài thêm của lời hứa" là gì cho tới mục 3.5.
- Viết lại: "Đánh giá: số khách được phục vụ; số khách tới nơi muộn hoặc sớm hơn lời hứa đầu; lời hứa bị kéo dài thêm bao nhiêu khi có dự báo (mục 3.5); số khách bị điều phối dời giờ trả." [TÁC GIẢ KIỂM: các chỉ số đếm theo khách hay theo yêu cầu.]

**A8. Dòng 50–53 (Nặng)**
- Gốc: "So với một bộ điều phối ghép chuyến thông thường, RideBound thêm ba việc: tính các mốc giờ trả của từng khách cho mỗi phương án (candidate plan), loại phương án vi phạm luật lời hứa trước khi gọi bộ giải (solver), và ghi sổ sau khi chọn."
- Vì sao khó:
  - "Phương án" là khái niệm trung tâm của cả chương, nhưng chỉ được "định nghĩa" bằng chữ tiếng Anh trong ngoặc.
  - Người đọc không biết bộ điều phối "thông thường" làm gì, nên không thấy ba việc được "thêm" vào đâu.
  - "Bộ giải" giải bài toán gì?
- Viết lại: "Ở mỗi lượt, một bộ điều phối ghép chuyến thông thường làm hai việc. Trước hết, nó liệt kê các cách sắp xếp lại lộ trình cho từng xe; mỗi cách gọi là một phương án (candidate plan). Sau đó, nó dùng một chương trình tối ưu, gọi là bộ giải (solver), để chọn một phương án cho mỗi xe. RideBound thêm ba việc: tính các mốc giờ trả của từng khách cho mỗi phương án; loại các phương án vi phạm luật lời hứa trước khi gọi bộ giải; và ghi sổ sau khi chọn."

**A9. Hình 3.1, dòng 64–77 (Nặng)**
- Gốc: các ô "Nhận lô sự kiện mới", "Sinh phương án chỉ chèn thêm", "Tính ba mốc giờ trả", "Loại phương án vi phạm ràng buộc, khóa hay trần", "Công bố lời hứa (lớp dự báo)". Chú thích hình có câu "Trong thực nghiệm, lớp dự báo được tính lại trên các lần chạy đã ghi".
- Vì sao khó: năm cụm trong hình chưa được định nghĩa ở chỗ này (lô sự kiện, chỉ chèn thêm, ba mốc, trần, lớp dự báo). Câu cuối của chú thích làm tôi bối rối: hình vẽ dự báo nằm trong vòng lặp, chú thích lại nói trong thực nghiệm dự báo được tính "trên các lần chạy đã ghi". Vậy dự báo có nằm trong vòng lặp hay không?
- Viết lại chú thích: "Một lượt quyết định của RideBound. Ba bước tính mốc giờ trả, loại phương án theo luật lời hứa và ghi sổ là phần thêm vào so với một bộ điều phối ghép chuyến thông thường. Các thuật ngữ trong hình được giải thích ở mục 3.2–3.6. Ô 'Công bố lời hứa (lớp dự báo)' cho biết vị trí của dự báo trong thiết kế. Trong thực nghiệm chính, lời hứa theo dự báo không được tính trong vòng này mà được tính lại sau, trên dữ liệu các lần chạy đã ghi (mục 3.5)."

**A10. Bảng 3.1, dòng 81–120 (Vừa)**
- Vì sao khó: không có câu nào hướng dẫn cách đọc giả mã. Người đọc không biết cột giữa là gì, cột phải là gì, các ký hiệu "←", P_k, π nghĩa là gì. Sinh viên kinh tế hay điện tử có thể chưa từng đọc giả mã.
- Viết lại (thêm trước bảng): "Bảng 3.1 viết các bước dưới dạng giả mã: cột giữa là việc cần làm, cột phải là ghi chú. Ký hiệu a ← b nghĩa là gán giá trị b cho a. P_k là tập phương án của xe k, π là một phương án trong tập đó."

**A11. Bảng 3.1 dòng 5, tệp dòng 97–98 (Nhẹ)**
- Gốc: "thêm vào P_k các phương án chèn tối đa 2 yêu cầu mới, giữ thứ tự các điểm cũ; giữ tối đa 100 phương án"
- Vì sao khó: hai chữ "giữ" mang hai nghĩa khác nhau trong cùng một dòng. Khi có hơn 100 phương án thì giữ những phương án nào?
- Viết lại: "thêm vào P_k các phương án chèn thêm tối đa 2 yêu cầu mới, không đảo thứ tự các điểm cũ; mỗi xe có tối đa 100 phương án [TÁC GIẢ ĐIỀN: chọn thế nào khi vượt 100]".

**A12. Bảng 3.1 dòng 9–11, tệp dòng 105–110 (Nặng). ĐÂY LÀ CHỖ ĐẦU TIÊN TÔI LẠC HẲN**
- Gốc, gồm ba dòng giả mã kèm ghi chú:
  - "nếu luật lời hứa loại cả phương án giữ nguyên kế hoạch thì", ghi chú "xe bị ép; chỉ khi mọi lỗi là lỗi hạn chót hay lỗi trần";
  - "giữ lại phương án đó làm phương án bị ép và ghi một vi phạm", ghi chú "luật phục hồi giữ nguyên kế hoạch";
  - "giữ thêm các phương án bị loại không làm vi phạm đó tệ hơn", ghi chú "luật phục hồi không tệ hơn".
- Vì sao khó: ba dòng có năm khái niệm chưa định nghĩa: xe bị ép, lỗi hạn chót, lỗi trần, vi phạm, luật phục hồi. Tôi cũng không hiểu vì sao phương án "giữ nguyên kế hoạch" lại có thể vi phạm một luật lời hứa. Câu trả lời (vì tắc đường) mãi tới dòng 407–410 mới có. Ở đây tôi phải đoán rồi đọc tiếp.
- Viết lại (thêm một đoạn ngay dưới bảng): "Dòng 9–11 xử lý một tình huống hiếm: mọi phương án của một xe, kể cả giữ nguyên kế hoạch, đều bị luật lời hứa loại. Điều này có thể xảy ra với luật hạn chót (mục 3.4), chẳng hạn khi chỉ riêng việc đường đông hơn cũng làm giờ trả vượt hạn. Khi đó ta nói xe bị ép. Trong các luật của khóa luận, chỉ luật hạn chót và luật trần độ dời khách thấy có thể làm xe bị ép (Bảng 3.5). Với luật C, Nhận xét 3.1 cho thấy điều này không xảy ra." [TÁC GIẢ KIỂM: tôi suy câu "chỉ hai luật" từ cột "Khi xe bị ép" của Bảng 3.5.]

**A13. Bảng 3.1 dòng 12, tệp dòng 111 (Vừa)**
- Gốc: "chọn cho mỗi xe đúng một phương án bằng quy hoạch nguyên"
- Vì sao khó: "quy hoạch nguyên" là thuật ngữ tối ưu; sinh viên kinh tế có thể biết quy hoạch tuyến tính, nhưng không chắc. Quan trọng hơn: nếu mỗi xe chỉ chọn một phương án, sao không để từng xe tự chọn phương án tốt nhất của mình? Chương không nói vì sao phải chọn chung cho cả đội xe. Tôi đoán là để một yêu cầu mới không bị hai xe cùng nhận.
- Viết lại: "chọn cùng lúc cho mỗi xe đúng một phương án, sao cho [TÁC GIẢ KIỂM: mỗi yêu cầu mới được nhiều nhất một xe nhận], bằng quy hoạch nguyên (một dạng bài toán tối ưu trong đó biến chỉ nhận giá trị nguyên; ở đây biến là chọn hay không chọn một phương án)".

**A14. Dòng 126–127 (Nhẹ)**
- Gốc: "Luật lời hứa là một bộ lọc cứng: phương án vi phạm bị bỏ trước khi bộ giải chạy, không bị phạt trong hàm mục tiêu."
- Vì sao khó: "bị phạt trong hàm mục tiêu" là ngôn ngữ tối ưu. Người ngoài khó hình dung câu này đang so với cách làm nào.
- Viết lại: "Luật lời hứa là một bộ lọc cứng: phương án vi phạm bị bỏ hẳn trước khi bộ giải chạy, chứ không được giữ lại kèm một điểm trừ để bộ giải tự cân nhắc."

**A15. Dòng 127–129 (Vừa)**
- Gốc: "Bộ sinh phương án chỉ chèn thêm (insertion-only candidate generator) đặt điểm đón, điểm trả của yêu cầu mới vào các cặp vị trí trong kế hoạch của xe và giữ thứ tự các điểm cũ, nên không chuyển khách đã nhận sang xe khác."
- Vì sao khó:
  - Câu dài và có một cụm tiếng Anh bốn chữ.
  - "Các cặp vị trí" quá trừu tượng; một ví dụ nhỏ sẽ làm rõ ngay.
  - Chữ "nên" làm tôi khựng: "giữ thứ tự các điểm cũ" và "không đổi xe" là hai ý khác nhau, không suy ra nhau.
- Viết lại: "Bộ sinh phương án của RideBound chỉ chèn thêm (insertion-only candidate generator). Nó đặt điểm đón và điểm trả của khách mới xen vào giữa các điểm sẵn có trong kế hoạch của một xe, không đảo thứ tự các điểm cũ. Ví dụ, kế hoạch 'trả A' có thể thành 'đón B → trả A → trả B' (Hình 3.2). Vì chỉ chèn khách mới vào kế hoạch sẵn có của từng xe, bộ sinh không bao giờ chuyển khách đã nhận sang xe khác."

**A16. Dòng 129–131 (Nặng)**
- Gốc: "Nếu luật lời hứa loại cả phương án giữ nguyên kế hoạch (keep-route option), xe bị ép (forced decision), và luật phục hồi (recovery rule) quyết định xe còn giữ những phương án nào (dòng 9--11; mục 3.4)."
- Vì sao khó: một câu có ba cụm tiếng Anh. "Xe bị ép" chỉ được gắn nhãn chứ không được giải thích: bị ép làm gì? Định nghĩa thật nằm ở dòng 323–324 ("xe bị ép và lời hứa của ít nhất một khách bị phá"), còn ví dụ nằm ở dòng 408–410.
- Viết lại: "Trong các phương án luôn có một phương án đặc biệt: xe giữ nguyên kế hoạch cũ, không nhận thêm ai (keep-route option). Một số luật lời hứa có thể loại cả phương án này, chẳng hạn khi đường đông làm giờ trả vượt mức cho phép dù xe không ghép thêm ai (ví dụ ở mục 3.4). Khi đó xe không còn cách nào giữ đúng mọi lời hứa: lời hứa của ít nhất một khách sẽ bị phá. Khóa luận gọi tình huống này là xe bị ép (forced decision). Luật phục hồi quy định xe được giữ lại những phương án nào trong tình huống đó (dòng 9–11 của Bảng 3.1; mục 3.4)." Nếu cần giữ chữ "recovery rule", nên chuyển nó vào danh mục thuật ngữ.

### Mục 3.2 Ba mốc giờ trả

**B1. Dòng 142–152 (Nhẹ)**
- Vì sao khó: sáu chữ v, e, p, x, c, z không gợi nhớ gì. Khi đọc các mục 3.3–3.6 tôi phải lật lại danh sách này nhiều lần.
- Viết lại (thêm sau công thức 3.1): "Để dễ nhớ: v là giờ khách đang được báo; e là giờ nếu xe cứ đi như cũ; p là giờ nếu làm theo phương án mới; c là phần dời do điều phối, và luật C chỉ giới hạn c." [TÁC GIẢ KIỂM: nếu tên "C" không lấy từ c thì bỏ vế cuối.]

**B2. Dòng 152–153 (Vừa)**
- Gốc: "ở dòng sổ của lời hứa đầu, v = e = p."
- Vì sao khó: "dòng sổ" chưa được giới thiệu (phải đến mục 3.6). Câu cũng không nói vì sao ba mốc bằng nhau.
- Viết lại: "Riêng lần báo giờ đầu tiên (lời hứa đầu), sổ ghi v = e = p, nên x = c = z = 0 [TÁC GIẢ KIỂM: lý do, có phải vì chưa có lời hứa nào trước đó để so]."

**B3. Dòng 153–154 (Nhẹ)**
- Gốc: "Mốc e không phải ý mới: Hörl và Zwick cũng tính lại giờ trả trên tuyến đang gán theo giờ đi hiện tại."
- Vì sao khó: đang học định nghĩa thì câu chuyển sang chuyện "ý này có mới không", kèm tên hai tác giả người đọc chưa biết. Ý này còn lặp lại ở dòng 413–414.
- Viết lại: chuyển câu này thành chú thích chân trang, hoặc gộp vào đoạn dòng 413: "Cách tính mốc e không phải ý mới của khóa luận; Hörl và Zwick [..] cũng tính lại giờ trả như vậy (mục 3.4)."

**B4. Dòng 157–160 (Vừa)**
- Gốc: "…các sự kiện vừa xảy ra. Trong các thực nghiệm, thời gian dừng đón, trả bằng 0 giây và tắc đường là một hệ số chung cho cả thành phố theo khung 15 phút."
- Vì sao khó: câu thứ hai nhảy sang chi tiết thực nghiệm mà không nói vì sao cần biết ở đây. "Hệ số" tắc đường là gì, nhân vào cái gì? Cả chương không định nghĩa, dù mục 3.5 dựa hẳn vào khái niệm này.
- Viết lại: "…các sự kiện vừa xảy ra. Để hình dung những gì nằm trong x khi chạy thử: trong các thực nghiệm, xe dừng đón, trả mất 0 giây, và tắc đường được mô tả bằng một hệ số tắc đường chung cho cả thành phố, đổi theo từng khung 15 phút [TÁC GIẢ KIỂM: hệ số là số nhân áp lên thời gian đi; ví dụ hệ số 1,2 nghĩa là mọi chuyến đi lâu hơn 20% so với mức nền (theo GLOSSARY-VI)]."

**B5. Dòng 160–161 (Nhẹ)**
- Gốc: "Phép tách z = x + c là phép tính theo mô hình, không phải phép đo nhân quả."
- Vì sao khó: câu đúng, nhưng người đọc không biết "phép đo nhân quả" ở đây cụ thể sẽ là gì.
- Viết lại: "Phép tách z = x + c chỉ là phép trừ giữa các giờ do mô hình tính; nó không chứng minh rằng quyết định điều phối thực sự gây ra đúng c giây chậm trễ."

**B6. Dòng 164–166, Bảng 3.2, Hình 3.2 (Vừa)**
- Gốc: "ghép khách B làm giờ trả của khách A lùi 70 giây, nhưng chỉ 30 giây trong đó là phần dời do điều phối; 40 giây còn lại vẫn xảy ra nếu xe không ghép ai."
- Vì sao khó: ví dụ này rất tốt; đây là chỗ tôi hiểu ra cả chương. Có ba điểm vấp:
  - "lùi" trong tiếng Việt có thể hiểu là sớm lên hoặc muộn đi, nên mơ hồ.
  - Câu không nói vì sao có 40 giây (đường đông hơn lúc hứa?), nên con số như từ trên trời rơi xuống.
  - Bảng viết "s", văn bản viết "giây".
- Viết lại: "ghép khách B làm giờ trả của khách A muộn hơn lời hứa 70 giây, nhưng chỉ 30 giây trong đó là phần dời do điều phối; 40 giây còn lại (chẳng hạn vì đường đông hơn lúc hứa) vẫn xảy ra nếu xe không ghép ai." Trong Bảng 3.2, thống nhất đơn vị "giây".

**B7. Dòng 217–218 (Vừa)**
- Gốc: "Bộ sinh chỉ chèn thêm không bảo đảm c ≥ 0 theo cấu tạo, nên định nghĩa giữ trị tuyệt đối."
- Vì sao khó: "theo cấu tạo" dịch sát từ "by construction", nghe lạ. Người đọc thắc mắc: chèn thêm một điểm dừng thì sao giờ trả lại có thể sớm hơn? Câu không trả lời, khiến tôi nghi mình đã hiểu sai cả mục.
- Viết lại: "Cách xây dựng bộ sinh chỉ chèn thêm không bảo đảm c luôn không âm, nghĩa là không loại trừ trường hợp phương án mới cho giờ trả sớm hơn e. Vì vậy định nghĩa dùng trị tuyệt đối. [TÁC GIẢ ĐIỀN: một câu nói khi nào c có thể âm.]"

**B8. Dòng 218–220 (Vừa)**
- Gốc: "Trên các lần chạy đã có, vế này không có tác dụng đo được: ở tập kiểm tra chính (34 kịch bản, mục 4.x), mọi lần điều phối kéo giờ trả sớm hơn e chỉ sớm đúng 1 mili giây."
- Vì sao khó: "vế này" không rõ là vế nào (trị tuyệt đối hay phía sớm?). "Không có tác dụng đo được" là dịch từ "no measurable effect". "Kịch bản" và "tập kiểm tra chính" xuất hiện lần đầu mà không được giải thích.
- Viết lại: "Trên thực tế, trường hợp giờ trả sớm hơn e gần như không xuất hiện. Ở tập kiểm tra chính (34 kịch bản, mục 4.x), mỗi lần điều phối làm giờ trả sớm hơn e thì cũng chỉ sớm đúng 1 mili giây, nên việc lấy trị tuyệt đối không làm kết quả thay đổi đáng kể." Thêm chú thích chân trang ở lần đầu dùng chữ "kịch bản": "Một kịch bản là [TÁC GIẢ ĐIỀN; GLOSSARY-VI gợi ý: một tổ hợp ngày, mẫu nhu cầu và khung giờ, gồm 108 yêu cầu và 8 xe 4 chỗ], mô phỏng trên dữ liệu Manhattan (mục 3.7)."

### Mục 3.3 Luật C

**C1. Dòng 229–231 (Vừa)**
- Gốc: "Gọi B là trần (cap), tính bằng giây, p_0 là lời hứa đầu của khách r (lời hứa không dự báo công bố khi khách xác nhận đặt xe), và L_r là tổng |c| đã tính cho r kể từ p_0, với L_r = 0 lúc xác nhận."
- Vì sao khó: p_0 được định nghĩa nhưng không xuất hiện trong công thức (3.2); tôi tìm mãi xem p_0 dùng ở đâu. "Lời hứa không dự báo" là khái niệm của mục 3.5, tôi chưa học tới. Câu có ba định nghĩa nối nhau bằng dấu phẩy.
- Viết lại: "Gọi B là trần (cap), tính bằng giây. Với mỗi khách r, gọi L_r là tổng các |c| đã tính cho r từ lúc r xác nhận đặt xe; lúc xác nhận, L_r = 0." Định nghĩa p_0 có thể tách thành câu riêng: "Ký hiệu p_0 là lời hứa đầu của r, chưa cộng dự báo (mục 3.5); p_0 sẽ dùng ở mục 3.4."

**C2. Dòng 231–232 (Nặng)**
- Gốc: "Một phương án của một xe chỉ được giữ lại nếu với mọi khách r đã nhận trên xe đó, ở giai đoạn đã nhận, chờ đón hay đang trên xe,"
- Vì sao khó: "trên xe đó" ở đầu câu nghĩa là "được giao cho xe đó", còn "đang trên xe" ở cuối câu nghĩa là "đã lên xe". Cùng một chữ mà hai nghĩa. Ba giai đoạn "đã nhận", "chờ đón", "đang trên xe" không được giải thích; tôi không phân biệt được "đã nhận" với "chờ đón".
- Viết lại: "Một phương án của một xe chỉ được giữ lại nếu bất đẳng thức sau đúng với mọi khách r đã được giao cho xe đó và chưa xuống xe, tức đang ở một trong ba giai đoạn: đã nhận [TÁC GIẢ ĐIỀN: khác 'chờ đón' ở chỗ nào], chờ đón, hoặc đang ngồi trên xe:"

**C3. Dòng 242 (Nhẹ)**
- Gốc: "Mọi khách đã nhận có cùng một mức trần, mức này không nới theo tắc đường"
- Vì sao khó: tôi phải đoán "nới theo tắc đường" nghĩa là gì, và không hiểu vì sao trần lại có thể được nới.
- Viết lại: "Mọi khách đã nhận có cùng một mức trần; mức này không tăng lên khi đường đông"

**C4. Dòng 248 (Vừa)**
- Gốc: "Bảng 3.3 tổng hợp các ràng buộc cứng và thứ tự tiêu chí của bộ chọn (mục 3.4)"
- Vì sao khó: "bộ chọn" xuất hiện lần đầu, trước đó chỉ có "bộ giải". Tôi không biết hai thứ này là một hay hai. Hình 3.1 viết "Bộ giải chọn một phương án", dòng 422 lại viết "Bộ chọn phương án … giải bằng OR-Tools".
- Viết lại: "Bảng 3.3 tổng hợp các ràng buộc cứng và thứ tự tiêu chí của bộ chọn phương án, tức phần dùng bộ giải để chọn một phương án cho mỗi xe (mục 3.4)."

**C5. Chú thích Bảng 3.3, dòng 253–254 (Vừa)**
- Vì sao khó: nửa dưới bảng là năm "tiêu chí", nhưng chú thích không nói cách đọc. Tiêu chí 1 quan trọng hơn hẳn tiêu chí 2? Hay các tiêu chí được cộng điểm? Cách hiểu đúng ("chỉ khi hòa ở tiêu chí trước mới xét tiêu chí sau") nằm ở dòng 423–424, hai trang sau.
- Viết lại chú thích: "…Phần dưới: bộ chọn so các lựa chọn theo tiêu chí 1 trước; chỉ khi hai lựa chọn bằng nhau ở tiêu chí 1 mới xét tiêu chí 2, và cứ thế tới tiêu chí 5. Giá trị là cấu hình của các tập thử, không phải chuẩn ngành."

**C6. Bảng 3.3, hàng "Khóa sau xác nhận", dòng 265–267 (Vừa)**
- Gốc: "khóa so với e nên tắc đường không làm khóa bị vi phạm"
- Vì sao khó: e đã được định nghĩa là giờ trả, nhưng ở đây đang nói về giờ đón. Cụm "khóa so với e" quá cô đặc.
- Viết lại: "Giờ đón mới được so với giờ đón khi giữ nguyên kế hoạch (một mốc giống e, nhưng cho giờ đón), chứ không so với giờ đã hứa. Vì vậy riêng việc đường đông hơn không làm khóa bị vi phạm."

**C7. Bảng 3.3, Tiêu chí 1, dòng 273–274 (Nhẹ)**
- Gốc: "Ít phương án bị ép nhất (chỉ khi lượt đó có xe bị ép)" và cột vai trò "Chỉ chọn phương án bị ép khi xe không còn lựa chọn khác"
- Vì sao khó: không rõ "ít nhất" tính trên một xe hay trên cả đội xe. Và nếu xe đã bị ép thì nó còn "lựa chọn khác" nào?
- Viết lại: "Ít phương án bị ép nhất, tính trên cả đội xe (tiêu chí chỉ có mặt khi lượt đó có xe bị ép)"; cột vai trò: "Chỉ dùng phương án bị ép cho xe không còn phương án hợp lệ nào". [TÁC GIẢ KIỂM]

**C8. Bảng 3.3, Tiêu chí 3, dòng 276–277 (Nặng)**
- Gốc: "Mức dùng trần lớn nhất nhỏ nhất, rồi tổng phần sửa lời hứa do điều phối trên từng chiều (chỉ khi có trần cứng)"
- Vì sao khó:
  - "lớn nhất nhỏ nhất" đọc như lỗi đánh máy.
  - "chiều" chưa được định nghĩa; phải tới dòng 316 mới có "mười chiều cam kết".
  - "trần cứng" là một tên mới.
  - "phần sửa lời hứa do điều phối" là tên thứ hai của c; mục 3.2 gọi là "phần dời do điều phối".
- Viết lại: "Trước hết, chọn sao cho khách dùng trần nhiều nhất dùng ít nhất có thể (mức dùng trần là phần đã dùng chia cho trần). Nếu hòa, chọn phương án có tổng phần dời do điều phối nhỏ nhất, cộng riêng cho từng loại cam kết (mục 3.3). Tiêu chí này chỉ có mặt khi cấu hình có trần, kể cả trần 0 của khóa." [TÁC GIẢ KIỂM: "trên từng chiều" là cộng gộp các chiều, hay so lần lượt từng chiều.]

**C9. Bảng 3.4, dòng 295 và 305–307 (Nhẹ)**
- Gốc: "Đầu ra: giữ hay loại π; nếu loại, một bản ghi chặn"; dòng 8 của giả mã: "trả về giữ π", ghi chú "nếu π được chọn: L_r ← L_r + |c_r|"
- Vì sao khó: "bản ghi chặn" là tên mới và không được giải thích. Lệnh cập nhật L_r lại nằm ở cột ghi chú, nên tôi tưởng đó chỉ là lời bình chứ không phải một bước.
- Viết lại: "nếu loại, một bản ghi lý do loại (gọi là bản ghi chặn)". Ở dòng 8, cột ghi chú viết: "việc cập nhật L_r ← L_r + |c_r| chỉ làm sau, nếu π được bộ chọn chọn (Bảng 3.1, dòng 14)".

**C10. Dòng 315–317 (Nặng)**
- Gốc: "Cài đặt thực kiểm cùng lúc mười chiều cam kết của mỗi khách; trong các cấu hình luật C, giờ trả là chiều có trần dương, còn đổi xe, đổi điểm đón và đổi điểm trả có trần 0."
- Vì sao khó:
  - Câu nói "mười chiều" nhưng chỉ kể ra bốn; sáu chiều còn lại là gì?
  - "Chiều" dịch từ "dimension"; người ngoài không hình dung được "chiều cam kết" là gì.
  - "Trần dương", "trần 0" là những cách nói mới.
  - "Cài đặt thực" nghĩa là "cài đặt thật sự" hay "trong thực tế"?
  - Cụm "mười chiều cam kết" còn quay lại ở dòng 518 và 627.
- Viết lại: "Trong mã chương trình, mỗi khách có mười loại cam kết được kiểm cùng lúc, gọi là mười chiều cam kết [TÁC GIẢ ĐIỀN: liệt kê đủ mười, có thể đưa vào phụ lục]. Trong các cấu hình luật C, chỉ giờ trả được phép dời (trần B lớn hơn 0). Đổi xe, đổi điểm đón và đổi điểm trả có trần bằng 0, tức là hoàn toàn không được đổi."

**C11. Dòng 323–325 (Vừa)**
- Gốc: "Nếu luật lời hứa loại hết phương án của một xe, kể cả phương án giữ nguyên kế hoạch, xe bị ép và lời hứa của ít nhất một khách bị phá. Gọi (N) là giả thiết: …"
- Vì sao khó: đây mới là định nghĩa thật của "xe bị ép", trong khi cụm này đã được dùng từ dòng 105 và 129. Tên "(N)" không gợi nhớ gì.
- Viết lại: chuyển câu đầu lên dòng 129–131 (xem A16). Ở đây chỉ nhắc lại: "Nhắc lại: xe bị ép khi luật lời hứa loại mọi phương án của xe, kể cả giữ nguyên kế hoạch. Gọi (N) là giả thiết 'phương án giữ nguyên kế hoạch hợp lệ': ở lượt đang xét, …"

**C12. Dòng 341 (Vừa)**
- Gốc: "Nhận xét đúng theo cấu tạo, không phải kết quả thực nghiệm; dữ liệu chỉ khớp với nó."
- Vì sao khó: "đúng theo cấu tạo" là dịch sát từ tiếng Anh. "Dữ liệu chỉ khớp với nó" có thể bị hiểu thành "dữ liệu chỉ khớp với nhận xét này, mà không khớp với gì khác".
- Viết lại: "Nhận xét này đúng do chính cách đặt luật C, không cần thí nghiệm để chứng minh; số liệu chạy thử chỉ cho thấy thực tế phù hợp với nó."

**C13. Dòng 342–343, so với dòng 427–428 (Vừa)**
- Gốc: "luật C có 0 quyết định bị ép trong 20.101 quyết định với trần 30 giây và 0 trong 20.435 quyết định với trần 120 giây."
- Vì sao khó: một "quyết định" là gì: một lượt, hay một xe trong một lượt? Dòng 427 lại đếm "3.506 lượt với trần 30 giây". Tôi không biết 20.101 và 3.506 đếm hai thứ khác nhau hay cùng một thứ.
- Viết lại: "… có 0 quyết định bị ép trong 20.101 quyết định [TÁC GIẢ ĐIỀN: một quyết định là gì, ví dụ 'lựa chọn cho một xe trong một lượt'] với trần 30 giây, và 0 trong 20.435 quyết định với trần 120 giây."

**C14. Dòng 346–348 (Vừa)**
- Gốc: "nếu (N) không thỏa, chẳng hạn khi kế hoạch đang chạy đã vi phạm một ràng buộc vật lý, xe vẫn có thể kẹt, nhưng do ràng buộc khác."
- Vì sao khó: "ràng buộc vật lý" là tên mới, trong khi Bảng 3.3 gọi là "ràng buộc dịch vụ". "Kẹt" chưa được định nghĩa. "Do ràng buộc khác": khác với cái gì?
- Viết lại: "nếu (N) không thỏa, chẳng hạn khi kế hoạch đang chạy đã vi phạm một ràng buộc dịch vụ [TÁC GIẢ KIỂM: 'ràng buộc vật lý' có đúng là ràng buộc dịch vụ của Bảng 3.3 không], xe vẫn có thể kẹt, tức không còn phương án hợp lệ nào. Nhưng khi đó nguyên nhân là ràng buộc dịch vụ chứ không phải luật C."

**C15. Dòng 348–349 (Vừa)**
- Gốc: "với v = 600 và e = p = 660 (giây), phương án giữ nguyên có z = 60, nên luật C không bảo đảm giờ đến thật."
- Vì sao khó: ví dụ trước dùng giờ đồng hồ (9:10:00), ở đây lại chuyển sang "600 giây" mà không nói tính từ mốc nào. "Không bảo đảm giờ đến thật" cũng mơ hồ: có phải là không bảo đảm khách tới đúng giờ đã hứa?
- Viết lại: "với v = 600 và e = p = 660 (các giờ viết bằng số giây kể từ [TÁC GIẢ ĐIỀN: mốc nào]), phương án giữ nguyên có z = 60, nên luật C không bảo đảm khách tới đúng giờ đã hứa."

**C16. Dòng 349–351 (Vừa)**
- Gốc: "Thứ ba, một lần sửa giữ đúng lời hứa vẫn bị tính: với v = p = 600 và e = 720, phương án kéo giờ trả về 600 giây có z = 0 nhưng |c| = 120."
- Vì sao khó: "một lần sửa giữ đúng lời hứa vẫn bị tính" khó phân tích: sửa cái gì, giữ cái gì, tính vào đâu? Phải đọc ví dụ mới hiểu.
- Viết lại: "Thứ ba, ngay cả khi điều phối kéo giờ trả về đúng giờ đã hứa, phần dời đó vẫn bị trừ vào trần: với v = p = 600 và e = 720, phương án kéo giờ trả về 600 giây có z = 0 nhưng |c| = 120."

### Mục 3.4 Các luật đối chứng và bộ chọn phương án

**D1. Chú thích Bảng 3.5, dòng 364–365 (Vừa)**
- Gốc: "B là trần (với luật hạn chót là độ chùng)"
- Vì sao khó: "độ chùng" (dịch từ "slack") là từ hiếm gặp; người ngoài không hiểu.
- Viết lại: "B là trần, tính bằng giây; với luật hạn chót, B là số giây giờ trả được phép muộn hơn lời hứa đầu p_0."

**D2. Bảng 3.5, cột Ký hiệu (Nhẹ)**
- Vì sao khó: bảng không giải thích nguồn gốc các ký hiệu U, FREE, M⁺, V. M là gì, dấu + là gì, V là gì? FREE và LOCKS là chữ tiếng Anh viết hoa nằm giữa văn bản tiếng Việt.
- Viết lại: thêm vào chú thích "[TÁC GIẢ ĐIỀN: nguồn gốc ký hiệu, ví dụ M⁺ là hạn chót chỉ chặn phía muộn]". Chữ "LOCKS" nên chuyển hẳn sang phụ lục (xem D7).

**D3. Bảng 3.5, hàng U, cột Khóa, dòng 374 (Vừa)**
- Gốc: "Xe, điểm đón, giờ đón; không đổi điểm trả"
- Vì sao khó: hai vế viết theo hai kiểu khác nhau (vế đầu là danh sách, vế sau là "không đổi…"), nên tôi không chắc điểm trả có bị khóa hay không. Bảng 3.3 lại viết: "Không đổi xe, điểm đón, điểm trả; giờ đón … phải trùng giờ đón khi giữ nguyên kế hoạch".
- Viết lại: "Khóa xe, điểm đón, điểm trả và giờ đón" (viết cùng cách với Bảng 3.3).

**D4. Bảng 3.5, hàng U, cột Khi xe bị ép, dòng 374–375 (Vừa)**
- Gốc: "Không xảy ra, vì khóa so với e"
- Vì sao khó: quá cô đặc (cùng vấn đề với C6).
- Viết lại: "Không xảy ra: U không kiểm giờ trả, còn khóa giờ đón được so với mốc giữ nguyên kế hoạch, nên phương án giữ nguyên luôn qua."

**D5. Bảng 3.5, hàng FREE, dòng 378 (Nặng)**
- Gốc: "Không kiểm; chính sách chi phí cuốn chiếu mặc định"
- Vì sao khó: tôi hoàn toàn không hiểu "chính sách chi phí cuốn chiếu mặc định": cuốn chiếu là gì, mặc định của ai?
- Viết lại: "Không kiểm giờ trả; ở mỗi lượt, chọn kế hoạch có chi phí nhỏ nhất và được đổi mọi thứ" [TÁC GIẢ KIỂM: câu này lấy theo GLOSSARY-VI mục D; GLOSSARY ghi là chưa kiểm việc có cho đổi xe hay không]. Cột Khóa giữ "Không khóa".

**D6. Bảng 3.5, cột "Dùng ở tập nào" (Vừa)**
- Gốc: "Tập kiểm tra chính; tập chỉnh trần buổi sáng; tập tắc đường cố định (tên cũ LOCKS)", "chiều tuyết (30)"
- Vì sao khó: chương 3 chưa hề giới thiệu ba tập sau. "Chiều tuyết" là một tập thử hay một kiểu tắc đường?
- Viết lại: thêm vào chú thích bảng: "Các tập thử (tập kiểm tra chính, tập chỉnh trần buổi sáng, tập tắc đường cố định, tập chiều có tuyết) được mô tả ở mục 4.x." Đổi "chiều tuyết" thành "tập chiều có tuyết" [TÁC GIẢ KIỂM tên gọi].

**D7. Dòng 395–398 (Vừa)**
- Gốc: "Luật hạn chót chỉ mượn phần hạn chót của Schulz và Pfeiffer, ở mức 30--60 giây thay vì 900 giây, không tái lập thuật toán của họ. Trên tập tắc đường cố định, điều phối không trần mang tên cũ LOCKS và chạy bằng bộ chạy cũ không có luật phục hồi. Phụ lục A gọi cấu hình không khóa, không trần của tập kịch bản tĩnh là B1, và cấu hình có khóa cùng trần 30 giây là C1."
- Vì sao khó: đoạn này chủ yếu ghi tên gọi. Nó đưa vào bảy tên mới mà người đọc không dùng ngay:
  - Schulz và Pfeiffer, nhưng "phần hạn chót" của họ chưa được giới thiệu;
  - LOCKS;
  - "bộ chạy cũ", trong khi "bộ chạy" chưa được định nghĩa (phải tới Bảng 3.7);
  - "tập kịch bản tĩnh";
  - B1 và C1.
- Viết lại câu đầu: "Luật hạn chót chỉ mượn ý 'hạn chót tính từ lời hứa đầu' trong nghiên cứu của Schulz và Pfeiffer [..], với mức 30–60 giây thay vì 900 giây như trong bài của họ; khóa luận không tái lập thuật toán của họ." Hai câu sau chuyển thành chú thích chân trang, hoặc chuyển sang phần mô tả tập thử ở chương 4 hay Phụ lục A.

**D8. Dòng 401–405, công thức (3.3) (Vừa)**
- Gốc: "Khi mỗi lần cập nhật so với lời hứa ngay trước nó (v_t = p_{t−1}), sau k lần cập nhật ∑(x_t + c_t) = ∑z_t = p_k − p_0."
- Vì sao khó:
  - (a) Chữ k trước đó là số hiệu xe (xe k, P_k), giờ lại là số lần cập nhật.
  - (b) Chữ t ở đây là số thứ tự lần cập nhật, nhưng ở mục 3.5 t lại là "lúc công bố".
  - (c) Câu không giải thích vì sao tổng bằng p_k − p_0.
  - (d) Theo định nghĩa của v ở mục 3.2 ("giờ trả đã công bố cho khách ở lần gần nhất"), tôi tưởng v_t = p_{t−1} luôn đúng. Vậy khi nào nó sai, mà câu phải mở đầu bằng "Khi…"?
- Viết lại: "Đánh số các lần cập nhật lời hứa của một khách là 1, 2, …, n. Nếu mỗi lần cập nhật được so với đúng lời hứa ngay trước nó (v_i = p_{i−1}) [TÁC GIẢ ĐIỀN: khi nào điều kiện này không đúng], thì z_i = p_i − p_{i−1}. Cộng tất cả lại, các giờ ở giữa triệt tiêu nhau, chỉ còn giờ cuối trừ giờ đầu: ∑(x_i + c_i) = ∑ z_i = p_n − p_0." Ở đây chỉ đổi ký hiệu, không đổi con số nào.

**D9. Dòng 407–410 (Vừa, nhưng rất quan trọng)**
- Gốc: "Vì vậy riêng tắc đường có thể làm hai luật đầu loại phương án giữ nguyên: ở Bảng 3.2, nếu 9:10:00 là lời hứa đầu, phương án giữ nguyên có e − p_0 = |z| = 40 giây, vượt trần 30 giây của cả hai luật, dù c = 0."
- Vì sao khó: phải dò lại câu trước mới biết "hai luật đầu" là luật hạn chót và luật trần độ dời khách thấy. Đây là ví dụ quan trọng nhất để hiểu vì sao "xe bị ép" xảy ra và luật C khác các luật kia ở đâu. Nhưng nó nằm ở cuối chương, sau khi cụm "xe bị ép" đã được dùng năm, sáu lần.
- Viết lại: "Vì vậy, chỉ riêng việc đường đông hơn cũng đủ làm luật hạn chót và luật trần độ dời khách thấy loại phương án giữ nguyên kế hoạch, còn luật C thì không. Ví dụ ở Bảng 3.2: nếu 9:10:00 là lời hứa đầu, phương án giữ nguyên có e − p_0 = |z| = 40 giây, vượt trần 30 giây của cả hai luật kia, dù c = 0." Nên nhắc tới ví dụ này ngay ở dòng 129–131 (xem A16).

**D10. Dòng 413–419 (Nặng)**
- Gốc: "Công thức 7 của họ đặt giờ trả bắt buộc của khách trên xe đang xét bằng giá trị lớn hơn giữa giờ cập nhật và giờ trả muộn nhất, kèm phạt cho mỗi giây vượt giờ trả muộn nhất. Với giờ trả muộn nhất là p_0 + B, đó là hạn chót nới max(p_0 + B, e), một cách viết lại của khóa luận chứ không phải định nghĩa trong bài. Hạn chót nới này cũng có tính chất của Nhận xét 3.1 vì phương án giữ nguyên có p = e; đây là suy luận, chưa được chạy."
- Vì sao khó: câu đầu có ba khái niệm mới (giờ trả bắt buộc, giờ cập nhật, giờ trả muộn nhất). Sau đó còn "hạn chót nới", "một cách viết lại của khóa luận chứ không phải định nghĩa trong bài", "chưa được chạy". Đọc ba lần tôi vẫn chỉ nắm được đại ý "cách của họ gần giống, nhưng khác ba điểm".
- Viết lại: "Cách đo gần nhất là của Hörl và Zwick [..]. Ở mỗi lượt quyết định, họ tính lại giờ trả trên tuyến đang chạy theo giờ đi hiện tại; đó chính là mốc e. Trong công thức 7 của họ, giờ trả mà xe phải đạt được đặt bằng giờ muộn hơn trong hai giờ: giờ vừa tính lại và giờ trả muộn nhất cho phép. Mỗi giây vượt giờ trả muộn nhất bị phạt. Nếu lấy giờ trả muộn nhất là p_0 + B, quy tắc này tương đương một hạn chót được nới theo tắc đường, max(p_0 + B, e). Đây là cách khóa luận viết lại, không phải định nghĩa trong bài của họ. Vì phương án giữ nguyên có p = e, hạn chót nới này cũng không bao giờ loại phương án giữ nguyên, giống Nhận xét 3.1; đây là suy luận, chưa được kiểm bằng chạy thử. Luật C khác cách của họ ở ba chỗ: …"

**D11. Dòng 422–428 (Nặng). ĐÂY LÀ CHỖ KHÓ NHẤT CHƯƠNG**
- Gốc: "Tiêu chí 3 bật cả khi chỉ có các trần 0 của khóa, nên có ở cả điều phối không trần; phần đầu của nó không phân biệt phương án vì chiều có trần 0 luôn được tính là đã dùng hết. Trên tập kiểm tra chính, mức này bằng 1.000.000 phần triệu ở mọi lượt có mức này: 3.503 lượt khi không trần, 3.506 lượt với trần 30 giây và 3.504 lượt với trần 120 giây."
- Vì sao khó:
  - Tôi vấp ở hầu hết các cụm: "bật" (như bật công tắc?), "phần đầu của nó", "chiều có trần 0 luôn được tính là đã dùng hết", "1.000.000 phần triệu" (tức 100%, sao không viết 100%?), "ở mọi lượt có mức này".
  - Đoạn văn cũng không nói kết luận: vậy trên thực tế tiêu chí 3 làm gì?
- Viết lại: "Tiêu chí 3 có mặt cả ở điều phối không trần, vì khóa được cài như những trần bằng 0. Nhưng phần đầu của tiêu chí này (mức dùng trần lớn nhất) không giúp phân biệt các phương án. Lý do: một loại cam kết có trần 0 luôn được tính là đã dùng hết trần, nên mức dùng trần lớn nhất luôn bằng 100% (bộ chọn ghi là 1.000.000 phần triệu). Trên tập kiểm tra chính, điều này đúng ở mọi lượt có tính tiêu chí 3: 3.503 lượt khi không trần, 3.506 lượt với trần 30 giây và 3.504 lượt với trần 120 giây. Như vậy, trên thực tế tiêu chí 3 chỉ còn tác dụng qua phần thứ hai, tức tổng phần dời do điều phối." [TÁC GIẢ KIỂM: câu cuối, và nghĩa chính xác của cụm "mọi lượt có mức này".]

**D12. Dòng 431–433 (Vừa)**
- Gốc: "Điều phối không trần và luật C dùng cùng tệp chính sách và cùng bộ chọn, chỉ khác ở trần giờ trả; hiệu giữa chúng là phép so của việc thêm trần khi giữ nguyên bộ chọn. Kết quả có còn khi bộ chọn ưu tiên chi phí hay không thì chưa được kiểm (mục 4.x)."
- Vì sao khó: câu "hiệu giữa chúng là phép so của việc thêm trần khi giữ nguyên bộ chọn" nghe như dịch máy. "Tệp chính sách" là tên mới. "Bộ chọn ưu tiên chi phí" chưa được định nghĩa.
- Viết lại: "Điều phối không trần và luật C dùng cùng tệp cấu hình (tệp chính sách) và cùng bộ chọn, chỉ khác nhau ở trần giờ trả. Vì vậy, chênh lệch kết quả giữa hai cấu hình cho biết tác dụng của riêng việc thêm trần, khi bộ chọn giữ nguyên. Khóa luận chưa kiểm kết quả này có còn đúng không nếu bộ chọn ưu tiên chi phí, tức [TÁC GIẢ KIỂM: bỏ tiêu chí 3 để chi phí được xét ngay sau số yêu cầu được nhận, theo GLOSSARY-VI] (mục 4.x)."

**D13. Dòng 436–440 (Nặng)**
- Gốc: "Có hai luật phục hồi. Luật giữ nguyên kế hoạch giữ phương án giữ nguyên làm phương án bị ép và ghi một vi phạm, nếu mọi lỗi của nó là lỗi hạn chót hay lỗi trần. Luật không tệ hơn kế hoạch giữ còn giữ, trên xe đã bị ép, các phương án mắc cùng lỗi nhưng không làm lỗi đó tệ hơn, để xe vẫn nhận được khách mới; khóa xe và khóa theo giai đoạn không bao giờ được miễn, và mỗi lần miễn được ghi thành vi phạm."
- Vì sao khó:
  - Câu thứ hai có chữ "giữ" ba lần với hai nghĩa.
  - Câu thứ ba tôi không phân tích được ngữ pháp. Đúng ra "không tệ hơn kế hoạch giữ" là tên luật và "còn giữ" là động từ, nhưng đọc liền một mạch thì câu thành vô nghĩa.
  - "Khóa theo giai đoạn" và "miễn" là khái niệm mới.
  - Tên luật phục hồi được viết bốn kiểu trong chương: "luật phục hồi giữ nguyên kế hoạch / không tệ hơn" (dòng 107–110), "Phục hồi không tệ hơn" (Bảng 3.5), "Luật không tệ hơn kế hoạch giữ" (dòng 437), "luật phục hồi không tệ hơn" (dòng 641).
- Viết lại: "Có hai luật phục hồi, dùng khi xe bị ép.
  - (1) Luật phục hồi giữ nguyên kế hoạch: nếu mọi lỗi của phương án giữ nguyên kế hoạch đều là lỗi hạn chót hoặc lỗi trần, xe được đi tiếp kế hoạch cũ như một phương án bị ép, và hệ thống ghi lại một vi phạm.
  - (2) Luật phục hồi không tệ hơn: ngoài kế hoạch cũ, xe bị ép còn được chọn những phương án mắc cùng loại lỗi nhưng không làm lỗi đó nặng hơn so với kế hoạch cũ; nhờ vậy xe vẫn nhận được khách mới. Ở luật này, khóa xe và khóa theo giai đoạn [TÁC GIẢ ĐIỀN: khóa theo giai đoạn là gì] không bao giờ được bỏ qua, và mỗi lần một lỗi được bỏ qua đều được ghi thành vi phạm.

  Tập kiểm tra chính và tập chỉnh trần buổi sáng dùng luật thứ hai cho mọi cấu hình."

### Mục 3.5 Lời hứa theo dự báo

**E1. Dòng 450–461, công thức (3.4) (Nặng)**
- Gốc: "Với lúc công bố t và lời hứa không dự báo p, lời hứa kéo dài S là nghiệm của ∫_t^S dτ/g(τ) = p − t, …"
- Vì sao khó: tôi biết tích phân, nhưng không hiểu vì sao phương trình lại có dạng này. Tích phân của 1/g nghĩa là gì ngoài đời? Mục 3.5 không có ví dụ số nào, trong khi mục 3.2 có một ví dụ rất tốt. Một đoạn văn đưa ra chín ký hiệu mới: t, p, S, D, g, τ, b, b_0, m.
- Viết lại: thêm sau công thức một đoạn giải thích trực giác và một ví dụ dựng tay.
  - Trực giác: "Theo tốc độ hiện tại, xe cần p − t giây nữa để tới nơi. Nếu trong một khung 15 phút sau đó đường chậm hơn hiện tại g lần, thì mỗi giây đồng hồ trong khung đó xe chỉ đi được một quãng bằng 1/g giây theo tốc độ hiện tại. S là thời điểm xe đi hết quãng đường 'p − t giây theo tốc độ hiện tại' đó."
  - Ví dụ dựng tay, không phải số đo: "Lời hứa được công bố lúc t = 9:00:00, lời hứa không dự báo là p = 9:20:00, tức còn 1.200 giây. Khung 9:00–9:15 là khung hiện tại (g = 1). Giả sử các ngày nguồn cho thấy khung 9:15–9:30 chậm hơn khung hiện tại 20% (g = 1,2). Trong khung đầu, xe đi được 900 giây quãng đường. 300 giây quãng đường còn lại mất 300 × 1,2 = 360 giây, nên S = 9:21:00. Lời hứa hiển thị là D = max(9:20:00, 9:21:00) = 9:21:00, dài thêm 60 giây."
  - Tôi đã chạy tay ví dụ này theo giả mã Bảng 3.6: dòng 9–10 cho S = 9:15:00 + 300 × 1,2 = 9:21:00.

**E2. Mục 3.5, trùng ký hiệu (Vừa)**
- Vì sao khó:
  - p ở mục 3.2 là "giờ trả nếu chọn phương án đang xét", ở đây lại là "lời hứa không dự báo".
  - t ở công thức (3.3) là số thứ tự lần cập nhật, ở đây lại là "lúc công bố".
  - b (khung 15 phút) và B (trần) chỉ khác nhau ở chữ hoa. Lần đọc đầu tôi đã nhầm m(b) thành "mức theo trần B".
- Viết lại: thêm một câu: "Ở mục này, p vẫn là giờ trả của phương án đã chọn như ở mục 3.2, nhưng chưa cộng dự báo; ta gọi nó là lời hứa không dự báo." Nên đổi ký hiệu khung 15 phút thành một chữ khác, không trùng với B và h.

**E3. Dòng 461–463 (Nặng)**
- Gốc: "m(b) là trung bình hệ số tắc đường ở khung 15 phút b trên các ngày nguồn, b(τ) là khung chứa thời điểm τ, và b_0 = b(t): mức hiện tại lấy từ bảng giờ đi đang dùng, còn từ các ngày khác chỉ lấy hình dạng tăng, giảm."
- Vì sao khó:
  - Chương chưa bao giờ định nghĩa "hệ số tắc đường"; tôi phải đoán là "đường chậm hơn mức nền bao nhiêu lần".
  - "Ngày nguồn" đến đoạn sau mới được định nghĩa.
  - Vế "mức hiện tại lấy từ bảng giờ đi đang dùng, còn từ các ngày khác chỉ lấy hình dạng tăng, giảm" là ý quan trọng nhất của công thức, nhưng viết quá cô đặc. Tôi chỉ hiểu sau khi tự làm ví dụ ở E1.
- Viết lại: "Trong đó, hệ số tắc đường của một khung 15 phút cho biết đi lại trong khung đó chậm hơn mức nền bao nhiêu lần [TÁC GIẢ KIỂM]. m(b) là trung bình hệ số này ở khung b trên các ngày nguồn (định nghĩa ở đoạn sau); b(τ) là khung chứa thời điểm τ; b_0 = b(t) là khung hiện tại. Ý của công thức: mức tắc đường lúc này đã có sẵn trong bảng giờ đi đang dùng, nên trong khung hiện tại g = 1. Các ngày trước chỉ được dùng để biết các khung sau sẽ chậm hơn hay nhanh hơn khung hiện tại bao nhiêu lần, tức tỉ số m(b(τ))/m(b_0)."

**E4. Dòng 463–464 (Nhẹ)**
- Gốc: "Phép lấy max làm lời hứa không bao giờ bị rút ngắn"
- Viết lại: "Phép lấy max làm lời hứa không bao giờ bị rút ngắn: nếu dự báo cho thấy đường sắp thông hơn (S sớm hơn p), hệ thống vẫn giữ p."

**E5. Dòng 467–471 (Vừa)**
- Gốc: "Ngày nguồn là các ngày cùng loại (ngày thường hay cuối tuần) trước ngày của kịch bản, không gồm ngày có tuyết 15/11/2018, và cần ít nhất 2 ngày; vì vậy trong dữ liệu 12--18/11/2018 chỉ các ngày 14, 15 và 16/11 có dự báo."
- Vì sao khó:
  - (a) Đến đây tôi mới biết dữ liệu là của năm 2018, nhưng không biết dữ liệu ở đâu; Manhattan chỉ được nói ở dòng 582.
  - (b) Câu có vẻ mâu thuẫn: ngày 15/11 bị loại khỏi ngày nguồn nhưng lại "có dự báo". Tôi phải nghĩ một lúc mới hiểu: 15/11 không được dùng để dự báo cho ngày khác, nhưng chính nó vẫn được dự báo từ các ngày trước.
  - (c) 21 + 13 = 34, vậy tập kiểm tra chính không có ngày 12 và 13/11? Chương không nói.
- Viết lại: "Ngày nguồn của một kịch bản là các ngày cùng loại (ngày thường hay cuối tuần) diễn ra trước ngày của kịch bản đó; cần ít nhất 2 ngày nguồn. Ngày 15/11/2018 có tuyết nên không được dùng làm ngày nguồn cho ngày khác, nhưng các kịch bản của chính ngày 15/11 vẫn được dự báo từ những ngày trước nó. Vì vậy, trong dữ liệu Manhattan từ 12 đến 18/11/2018 (mục 3.7), chỉ các ngày 14, 15 và 16/11 có dự báo. Trên tập kiểm tra chính, 21 trong 34 kịch bản (thuộc các ngày 14–16/11) có dự báo; 13 kịch bản ngày 17 và 18/11 giữ lời hứa không dự báo." [TÁC GIẢ KIỂM: cả 21 kịch bản có đúng thuộc 14–16/11 không.]

**E6. Dòng 505–506 (Vừa)**
- Gốc: "Trong thực nghiệm, lời hứa theo dự báo được tính lại trên các lần chạy đã ghi, gọi là phát lại (replay): quyết định điều phối không đổi, chỉ lời hứa đổi."
- Vì sao khó: tôi không hiểu "tính lại trên các lần chạy đã ghi" cho tới khi đọc vế sau. Điều này có nghĩa là trong thí nghiệm chính, dự báo không ảnh hưởng tới việc xe chở ai. Đó là thông tin rất quan trọng nhưng được nói rất nhẹ.
- Viết lại: "Trong thực nghiệm chính, khóa luận không chạy lại mô phỏng với dự báo. Thay vào đó, khóa luận lấy dữ liệu đã ghi của các lần chạy có sẵn rồi tính lại lời hứa hiển thị cho từng khách theo công thức trên; cách làm này gọi là phát lại (replay). Vì vậy quyết định điều phối (xe nào chở ai, theo thứ tự nào) giữ nguyên, chỉ giờ báo cho khách thay đổi."

**E7. Dòng 507–510 (Vừa)**
- Gốc: "Còn một chỗ chưa khớp: phép kiểm khả thi vẫn dùng giờ không dự báo, nên dưới luật C với trần 30 giây, 34 trong 1.471 khách được phục vụ của 21 kịch bản có dự báo có lời hứa giờ đón hiển thị muộn hơn giờ đón muộn nhất; chỗ này phải xử lý trước khi triển khai."
- Vì sao khó:
  - Câu dài khoảng 55 chữ.
  - Cả mục chỉ nói dự báo kéo dài giờ trả, đột nhiên ở đây xuất hiện "lời hứa giờ đón hiển thị". Vậy giờ đón cũng bị kéo dài?
  - "Giờ đón muộn nhất" là tên thứ tư của cửa sổ đón.
  - Con số 34 (khách) trùng với con số 34 (kịch bản) ở câu trên, dễ đọc nhầm.
- Viết lại: "Cách làm này còn một chỗ chưa khớp. Dự báo cũng kéo dài lời hứa giờ đón [TÁC GIẢ KIỂM], nhưng phép kiểm khả thi của bộ điều phối vẫn dùng giờ chưa có dự báo. Hệ quả là dưới luật C với trần 30 giây, trong 1.471 khách được phục vụ của 21 kịch bản có dự báo, có 34 khách được báo giờ đón muộn hơn giờ đón muộn nhất cho phép, tức nằm ngoài cửa sổ đón. Chỗ này phải được xử lý trước khi đưa vào dùng thật."

### Mục 3.6 Sổ theo dõi từng khách

**F1. Tiêu đề chương (dòng 14), dòng 18, 514, 517 (Vừa)**
- Vì sao khó: cùng một thứ có ba tên: "sổ theo từng khách" (tiêu đề chương, dòng 517), "sổ theo dõi từng khách" (dòng 18 và tiêu đề mục 3.6), và "sổ" (rải rác). GLOSSARY-VI lại dùng "sổ cái". Đề bài hỏi tôi về "sổ cái ba phần", nhưng cụm này không có trong chương. Tôi phải tự ghép chữ "sổ" ở đoạn đầu mục 3.6 với cụm "chia … thành ba phần" ở dòng 520 mới đoán ra.
- Viết lại: chọn một tên, ví dụ "sổ theo dõi từng khách" hoặc "sổ cái" theo GLOSSARY, rồi dùng nhất quán. Nếu phép chia ba phần có tên riêng thì đặt tên ở dòng 520, ví dụ "phép tách ba phần của sổ".

**F2. Dòng 517–519 (Vừa)**
- Gốc: "mỗi khách có một dòng cho lời hứa đầu và một dòng cho mỗi lần cập nhật, gồm v, e, p, các độ lớn |x|, |c|, |z| trên mười chiều cam kết và phần trần đã dùng L"
- Vì sao khó: không có ví dụ nào cho thấy một dòng sổ trông ra sao, và "mười chiều cam kết" vẫn chưa được liệt kê.
- Viết lại: thêm một bảng nhỏ làm ví dụ dựng tay. Bảng dùng lại khách A ở Bảng 3.2, giả sử 9:10:00 là lời hứa đầu như dòng 409, và chỉ ghi chiều giờ trả:

  | Dòng sổ | Thời điểm | v | e | p | \|x\| | \|c\| | \|z\| | L |
  |---|---|---|---|---|---|---|---|---|
  | 1 (lời hứa đầu) | lúc A xác nhận | 9:10:00 | 9:10:00 | 9:10:00 | 0 | 0 | 0 | 0 |
  | 2 (ghép B) | 9:00 | 9:10:00 | 9:10:40 | 9:11:10 | 40 | 30 | 70 | 30 |

  Bảng này khớp với dòng 244–245 ("phần trần còn lại của A bằng 0" khi B = 30).

**F3. Dòng 520–524, công thức (3.5) (Nặng)**
- Gốc: "a − p_0 = q + f + (a − D_0 − q), q = ∑c_t, f = D_0 − p_0."
- Vì sao khó: công thức đứng trước, tên ba phần mãi tới dòng 527–529 mới có. Không có câu nào nói đây là một đẳng thức hiển nhiên (cộng ba phần lại thì q và D_0 triệt tiêu), cũng không có ví dụ số. Tôi phải tự kiểm đại số mới tin.
- Viết lại:
  - Trước công thức, viết bằng lời: "độ trễ so với lời hứa đầu = phần tính cho điều phối + phần dự báo đã cộng sẵn + phần còn lại".
  - Sau công thức, thêm ví dụ dựng tay: "Ví dụ: p_0 = 9:10:00; lời hứa đầu có dự báo D_0 = 9:11:00, nên f = 60 giây; tổng các c là q = 30 giây; khách tới lúc a = 9:13:00. Độ trễ 180 giây được tách thành 30 + 60 + 90: 30 giây tính cho điều phối, 60 giây dự báo đã báo trước, 90 giây còn lại là phần dự báo chưa giải thích được."

**F4. Dòng 527–529 (Vừa)**
- Gốc: "q là phần tính cho điều phối, một tổng có dấu, khác với ∑|c| mà luật C giới hạn (dưới luật C, |q| ≤ ∑|c| ≤ B)"
- Vì sao khó: người ngoài không chắc "tổng có dấu" nghĩa là gì (cộng cả số âm?). Phần trong ngoặc đơn chen vào giữa một câu dài.
- Viết lại: "q là phần tính cho điều phối: cộng các c giữ nguyên dấu (dời muộn tính dương, dời sớm tính âm), nên khác với ∑|c| mà luật C giới hạn. Vì vậy, dưới luật C, |q| ≤ ∑|c| ≤ B."

**F5. Dòng 529 (Vừa)**
- Gốc: "f là phần được hồ sơ lịch sử giải thích, bằng 0 khi không có dự báo"
- Vì sao khó: "hồ sơ lịch sử" là tên mới và không được nối với mục 3.5, nơi gọi là "các ngày nguồn" và m(b).
- Viết lại: "f = D_0 − p_0 là phần mà dự báo theo các ngày trước (mục 3.5) đã cộng sẵn vào lời hứa đầu; khóa luận gọi đây là phần được hồ sơ lịch sử giải thích. Khi không có dự báo, f = 0."

**F6. Dòng 529–531 (Vừa)**
- Gốc: "Khi chuỗi cập nhật liên tục, theo (3.3) phần còn lại bằng ∑x_t + ρ − f, với ρ = a − p_k là độ lệch giữa giờ trả thật và lời hứa cuối p_k."
- Vì sao khó: "chuỗi cập nhật liên tục" là cách gọi thứ hai cho điều kiện ở dòng 401 ("mỗi lần cập nhật so với lời hứa ngay trước nó"), và người đọc không chắc hai cách gọi là một. Chữ k lại trùng với số hiệu xe.
- Viết lại: "Khi mỗi lần cập nhật được so với đúng lời hứa ngay trước nó (điều kiện của công thức (3.3)), phần còn lại bằng tổng các x cộng ρ rồi trừ f, trong đó ρ = a − p_n là chênh lệch giữa giờ trả thật và lời hứa cuối cùng p_n. Nói cách khác, phần còn lại gồm những thay đổi khi giữ nguyên kế hoạch mà dự báo chưa tính tới, cộng với độ lệch giữa giờ trả thật và lời hứa cuối." [TÁC GIẢ KIỂM câu "nói cách khác".]

**F7. Dòng 527 (Nhẹ)**
- Gốc: "a là giờ trả thực tế"
- Vì sao khó: người ngoài dễ hiểu là giờ ngoài đời, trong khi ở đây là giờ trong mô phỏng.
- Viết lại: "a là giờ trả thực tế trong mô phỏng"

### Mục 3.7 Cài đặt, kiểm thử và tái lập

**G1. Dòng 548–552 (Nhẹ)**
- Gốc: "chia thành các dự án theo tầng, phụ thuộc từ ngoài vào trong … Tầng nghiệp vụ (Domain) không tham chiếu dự án hay thư viện nào"
- Vì sao khó: "dự án theo tầng", "phụ thuộc từ ngoài vào trong", "tham chiếu" là ngôn ngữ của kỹ sư phần mềm. Sinh viên điện tử có thể đoán được, sinh viên kinh tế thì khó.
- Viết lại: "Mã RideBound viết bằng C# trên .NET 10 và chia thành nhiều phần nhỏ (gọi là dự án) xếp theo tầng: tầng ngoài được dùng mã của tầng trong, còn tầng trong không dùng gì của tầng ngoài (Bảng 3.7). Tầng nghiệp vụ (Domain) không dùng dự án hay thư viện nào khác; …"

**G2. Bảng 3.7, dòng 564–575 (Vừa)**
- Vì sao khó: tên các thành phần đều bằng tiếng Anh (Domain, Application, Algorithms, Contracts, Runner, Benchmarking) và không kèm tên tiếng Việt. Văn bản gọi Runner là "bộ chạy" (dòng 397, 583) nhưng không nói hai tên này là một. Tôi gặp "bộ chạy cũ" ở dòng 397 mà không biết bộ chạy là gì.
- Viết lại: ở cột thành phần, ghi kèm tên tiếng Việt: "Runner (bộ chạy)", "Domain (tầng nghiệp vụ)", "Application (tầng ứng dụng)", "Algorithms (thuật toán)", "Contracts (định dạng bản tin)", "Benchmarking (chuẩn bị dữ liệu thử)". Ở lần đầu nhắc "bộ chạy" (dòng 397), thêm "(chương trình nhận sự kiện và trả quyết định, mục 3.7)".

**G3. Dòng 582 (Vừa)**
- Gốc: "Bộ mô phỏng là FleetPy 1.0.2 với bộ dữ liệu chuẩn Manhattan."
- Vì sao khó: gần cuối chương tôi mới biết mọi thứ chạy trong mô phỏng, trên dữ liệu Manhattan. Trước đó tôi đã gặp "kịch bản", "15/11/2018", "ngày có tuyết", "tập tắc đường cố định" mà không biết bối cảnh.
- Viết lại: thêm một câu ở cuối mục 3.1.1: "Mọi thực nghiệm chạy trên bộ mô phỏng FleetPy với bộ dữ liệu chuẩn Manhattan, tuần 12–18/11/2018 (mục 3.7). Bộ mô phỏng đóng vai thế giới thật: nó gửi sự kiện cho bộ điều phối và thực hiện kế hoạch được chọn."

**G4. Dòng 583–585 (Nhẹ)**
- Gốc: "nó khởi động bộ chạy RideBound như một tiến trình con và trao đổi qua luồng vào, ra chuẩn, mỗi bản tin một dòng JSON"
- Vì sao khó: "luồng vào, ra chuẩn" là dịch từ "standard input/output" và nghe rất lạ. "Tiến trình con" và "JSON" không được giải thích.
- Viết lại: "nó chạy bộ chạy RideBound như một chương trình con, và hai bên nhắn tin cho nhau qua đầu vào, đầu ra chuẩn của chương trình (stdin, stdout); mỗi bản tin là một dòng văn bản theo định dạng JSON (Hình 3.3)."

**G5. Dòng 585–586 (Vừa)**
- Gốc: "Bộ chạy từ chối lô sự kiện mới khi quyết định trước chưa được báo đã áp dụng, nên các quyết định được áp dụng đúng thứ tự."
- Vì sao khó: cụm "chưa được báo đã áp dụng" có hai động từ bị động đứng liền nhau, rất khó đọc.
- Viết lại: "Bộ chạy không nhận lô sự kiện mới cho tới khi bộ mô phỏng báo rằng quyết định trước đã được áp dụng; nhờ vậy các quyết định được áp dụng đúng thứ tự."

**G6. Dòng 624–626 (Vừa)**
- Gốc: "cùng các giới hạn khối lượng cho bước sinh, bước kiểm và bộ giải (OR-Tools 9.15, hạt giống cố định 7), nên không vét cạn"
- Vì sao khó: "hạt giống cố định 7" là dịch từng chữ "fixed seed 7"; người ngoài sẽ hỏi hạt giống gì. "Giới hạn khối lượng" mơ hồ. "Không vét cạn" quá ngắn để hiểu.
- Viết lại: "cùng các giới hạn về lượng tính toán cho bước sinh, bước kiểm và bộ giải. Bộ giải là OR-Tools 9.15, với hạt giống ngẫu nhiên (con số khởi tạo phần ngẫu nhiên của bộ giải) cố định bằng 7 để chạy lại cho cùng kết quả. Vì có các giới hạn này, bộ sinh không xét hết mọi phương án có thể."

**G7. Dòng 631–633 (Nhẹ)**
- Gốc: "trung vị là 730 giây với ghép tự do, 667 giây với điều phối không trần và 641 giây với luật C trần 30 giây."
- Vì sao khó: tôi không biết một lần chạy mô phỏng tương ứng bao nhiêu giờ hoạt động thật, nên không biết 641 giây là nhanh hay chậm. Tôi cũng tò mò vì sao thêm phép kiểm trần mà chương trình lại chạy nhanh hơn, nhưng không có câu nào bình luận.
- Viết lại: thêm "[TÁC GIẢ ĐIỀN: một lần chạy mô phỏng bao nhiêu giờ hoạt động]". Nếu biết lý do chạy nhanh hơn thì nêu; nếu không thì ghi "chưa phân tích".

**G8. Dòng 644–646 (Vừa)**
- Gốc: "ở cả 382.006 lần cập nhật giờ trả của 185 lần chạy (170 lần chạy của năm luật trên tập kiểm tra chính và 15 lần chạy hiệu chỉnh cùng đợt)"
- Vì sao khó: 170 = 34 × 5. Nhưng Bảng 3.5 cho thấy trên tập kiểm tra chính có bốn luật (U, C, M⁺, V) với sáu cấu hình (U; C-30, C-120; M⁺-30, M⁺-60; V-30). Tôi không khớp được "năm luật" với bảng. "Lần chạy hiệu chỉnh" cũng chưa được giải thích.
- Viết lại: "… (170 lần chạy của năm cấu hình [TÁC GIẢ KIỂM: liệt kê ra, ví dụ U, C-30, M⁺-30, M⁺-60, V-30] trên 34 kịch bản của tập kiểm tra chính, và 15 lần chạy trên tập hiệu chỉnh [TÁC GIẢ KIỂM] trong cùng đợt)".

**G9. Dòng 652–653 (Nhẹ)**
- Gốc: "dùng cùng một bản chạy đã lưu trữ"
- Vì sao khó: "bản chạy" dễ bị hiểu nhầm thành "lần chạy".
- Viết lại: "dùng cùng một bản chương trình đã biên dịch và lưu lại"

**G10. Dòng 661–662 (Vừa)**
- Gốc: "so với điều phối không trần, luật hạn chót và cách đệm lời hứa."
- Vì sao khó: "đệm lời hứa" chưa từng xuất hiện trong chương 3; câu kết lại giới thiệu thêm một đối chứng mới.
- Viết lại: "… và cách đệm lời hứa, tức cộng thêm một khoảng cố định vào giờ hứa cho mọi khách (mục 4.x)."

---

## 3. Năm vấn đề lặp lại trong cả chương

**X1. Dùng thuật ngữ trước khi định nghĩa.** Chương dùng nhiều thuật ngữ trước khi giải thích; phần lớn rơi vào mục 3.1:

| Thuật ngữ | Dùng lần đầu (dòng) | Được giải thích ở (dòng) |
|---|---|---|
| dòng sổ, sổ | 39 | 517 |
| khóa | 40 | 265 (Bảng 3.3) |
| phương án | 52 (chỉ có chữ Anh) | không có câu định nghĩa tiếng Việt |
| lô sự kiện | 64 (Hình 3.1) | 604 (Hình 3.3) |
| ba mốc | 66 | 141–146 |
| trần | 67 | 229 |
| xe bị ép | 105 | 323 |
| lỗi hạn chót, luật hạn chót | 106 | 385 (Bảng 3.5) |
| luật phục hồi | 107 | 436 |
| hệ số tắc đường | 160 | không có |
| kịch bản, tập kiểm tra chính | 219 | không có trong chương |
| lời hứa không dự báo | 229 | 450 |
| bộ chọn | 248 | 422 |
| chiều (cam kết) | 277 | 316 (chỉ kể 4/10) |
| bộ chạy | 397 | 572 (chỉ có tên "Runner") |
| đệm lời hứa | 662 | không có |

Đề xuất: ở đầu mục 3.1, thêm một "bảng thuật ngữ nhanh" khoảng 10 dòng, mỗi thuật ngữ một câu giải thích. Đồng thời mở chương bằng câu chuyện ở M2 và câu bối cảnh ở G3.

**X2. Một khái niệm có nhiều tên.**
- c: "phần dời do điều phối" (152) và "phần sửa lời hứa do điều phối" (276).
- cửa sổ đón: bốn tên (A4).
- sổ: ba tên (F1).
- luật phục hồi: bốn cách viết (D13).
- "ràng buộc dịch vụ" (261) và "ràng buộc vật lý" (347).
- "bộ giải" và "bộ chọn" (C4).
- "trần", "trần cứng" (277), "trần dương" (317).
- "công bố" (38, 237, 450) và "cập nhật" (402, 518).
- Chữ "lượt" có ba nghĩa: lượt quyết định, lượt phục vụ, lượt trễ (A7).
- Chữ "khung" có hai nghĩa: khung 15 phút, và khung nét đứt trong Hình 3.3 (dòng 616).
- Bảng 3.5 gọi cả năm cách làm là "luật", nhưng dòng 401 lại nói "Ba luật lời hứa". Người đọc cần được biết U và FREE là "luật" nhưng không phải "luật lời hứa".

**X3. Một ký hiệu có nhiều nghĩa.**
- k: số hiệu xe (dòng 95, 293), rồi số lần cập nhật (402, 530).
- t: thời điểm công bố (450–453, 480–489), và chỉ số lần cập nhật (402–404, 522).
- p: giờ trả theo phương án (145), và lời hứa không dự báo (450).
- b (khung 15 phút) và B (trần) chỉ khác chữ hoa.
- Đơn vị viết lẫn "s" và "giây".

**X4. Chữ tiếng Anh chen vào.** Chương có 14 cụm tiếng Anh trong ngoặc:
- decision epoch (30), candidate plan (52), solver (52);
- insertion-only candidate generator (127), keep-route option (129), forced decision (130), recovery rule (130);
- cap (229), selector (422), lexicographic order (423);
- forecast-aware promise (448), replay (505), per-rider ledger (517);
- Domain, Application (549–550).

Ngoài ra còn các nhãn FREE, LOCKS và tên dự án trong Bảng 3.7. Các cụm này đều đúng quy tắc "chỉ ghi ở lần đầu", nhưng dòng 129–131 có ba cụm trong một câu và dòng 422–423 có hai cụm. Đề xuất: mỗi câu tối đa một cụm tiếng Anh; chuyển phần lớn vào danh mục thuật ngữ.

**X5. Mục 3.5 và 3.6 thiếu ví dụ số.** Mục 3.2 cho thấy ví dụ dựng tay là thứ giúp người ngoài hiểu nhanh nhất. Khách A đã được dùng lại ở mục 3.3 (dòng 244) và 3.4 (dòng 409). Đề xuất: tiếp tục dùng khách A cho mục 3.5 (xem E1) và 3.6 (xem F2, F3), để cả chương có một nhân vật xuyên suốt.

---

## 4. Đối chiếu với `style/GLOSSARY-VI.md`, đọc sau khi đọc xong chương

| Thuật ngữ | Chương 3 đang dùng | GLOSSARY-VI | Nhận xét |
|---|---|---|---|
| sổ | "sổ theo từng khách", "sổ theo dõi từng khách", "sổ" | "sổ cái"; yêu cầu "định nghĩa bằng ví dụ một dòng sổ" | Lệch tên. Chương chưa có ví dụ dòng sổ (F1, F2). |
| lời hứa giờ trả | Không dùng cụm này lần nào | Dùng ở lần đầu mỗi chương, sau đó viết "lời hứa" | Cần thêm ở dòng 17 hoặc 38 (M2, A5). |
| công bố / cập nhật | "công bố", không được định nghĩa | Nếu giữ "công bố" thì phải định nghĩa một lần | Định nghĩa ở A5. |
| c | "phần dời do điều phối", có chỗ viết "phần sửa lời hứa do điều phối" | "phần do điều phối" | Lệch nhẹ. Chọn một tên. |
| luật U | "Điều phối không trần", ký hiệu U chỉ dùng trong bảng | "luật U" | Chương chọn tên khác; được, nhưng cần khớp với chương 4. |
| hệ số tắc đường | Dùng nhưng không định nghĩa | Có định nghĩa và ví dụ "1,2 = lâu hơn 20%" | Nên đưa định nghĩa này vào chương (B4, E3). |
| hạt giống ngẫu nhiên | "hạt giống cố định 7" | "hạt giống ngẫu nhiên", định nghĩa một lần | Sửa theo G6. |
| kẹt | Dùng một lần (347), không giải thích | "Giải thích ở lần đầu" | Sửa theo C14. |
| kịch bản | Không định nghĩa | Có định nghĩa (108 yêu cầu, 8 xe 4 chỗ…) | Thêm chú thích (B8). |
| thứ tự tiêu chí | Giải thích bằng lời ở dòng 423 | "Giải thích một lần bằng ví dụ" | Chưa có ví dụ; ít nhất sửa chú thích Bảng 3.3 (C5). |
| ưu tiên chi phí | Dùng ở dòng 432, không định nghĩa | Có định nghĩa (đánh dấu "chưa chạy") | Sửa theo D12. |
| ba phần của sổ | "phần tính cho điều phối", "phần được hồ sơ lịch sử giải thích", "phần còn lại" | "do điều phối", "đoán trước được", "bất ngờ" | Chương cố ý tránh chữ "bất ngờ" (dòng 537–538), cách này hợp lý; nhưng GLOSSARY nên cập nhật cho khớp với chương. |
| lớp dự báo | "lớp dự báo" (Hình 3.1) | "dự báo ở lớp hiển thị" | Chưa được định nghĩa trong chương (A9). |
| đệm | Dùng một lần (662) | "đệm đều", có định nghĩa | Thêm định nghĩa (G10). |
| cửa sổ đón | Bốn tên, không có định nghĩa | "thời gian chờ đón tối đa (cửa sổ đón)", dùng "cửa sổ đón" sau khi đã định nghĩa | Sửa theo A4. |
| luật phục hồi | Bốn cách viết | Tên gọn, định nghĩa rõ hơn chương ("không vi phạm thêm luật nào và trên mỗi luật đã vi phạm không tệ hơn kế hoạch cũ") | Dùng định nghĩa của GLOSSARY (D13). |

---

## 5. Giải thích lại cho bạn tôi bằng 5 câu

1. Khi bạn đặt xe đi chung, ứng dụng báo trước giờ bạn tới nơi. Trong lúc đi, giờ đó có thể bị dời vì đường đông hơn dự tính, hoặc vì hệ thống quyết định ghé đón thêm người khác. Phần bị dời do việc ghé đón thêm gọi là "phần dời do điều phối" (c), và được đo bằng cách so giờ trả theo kế hoạch mới với giờ trả nếu xe cứ chạy như cũ.
2. Luật C cấp cho mỗi khách một "ngân sách" cố định cho cả chuyến, ví dụ B = 30 giây. Mỗi lần hệ thống muốn ghép thêm người, nó cộng độ lớn phần dời do điều phối vào phần bạn đã dùng; nếu tổng vượt 30 giây, phương án ghép đó bị loại ngay, trước khi bộ giải chọn.
3. Vì luật C không tính phần dời do tắc đường, phương án "cứ chạy như cũ" luôn có phần dời do điều phối bằng 0, nên không bao giờ bị luật C loại (miễn là phương án đó vẫn qua các ràng buộc khác). Nhờ vậy, xe không bao giờ bị dồn vào thế buộc phải phá lời hứa vì luật này, khác với luật hạn chót: với luật hạn chót, chỉ riêng tắc đường cũng có thể làm phương án chạy như cũ bị loại.
4. Lời hứa theo dự báo nghĩa là hệ thống không báo giờ theo tốc độ đường hiện tại, mà xem các ngày cùng loại trước đó: trong các khung 15 phút sắp tới, đường thường đông lên bao nhiêu so với bây giờ, rồi kéo dài giờ hứa tương ứng (không bao giờ rút ngắn). Trong thực nghiệm chính, phần này được tính lại trên dữ liệu các lần chạy đã ghi, nên không làm thay đổi việc xe nào chở ai.
5. Sổ theo từng khách ghi một dòng cho lời hứa đầu và một dòng cho mỗi lần đổi giờ: giờ đã báo, giờ nếu chạy như cũ, giờ theo phương án mới, và phần trần đã dùng. Sau khi chạy xong, độ trễ của mỗi khách so với lời hứa đầu được tách thành ba phần: phần tính cho điều phối (q, cộng giữ dấu các c), phần dự báo đã cộng sẵn (f = D_0 − p_0), và phần còn lại mà dự báo chưa giải thích được.

### Những chỗ tôi không viết được, hoặc phải đoán

- **Vì sao gọi là "C".** Tôi đoán C lấy từ chữ c, nhưng chương không nói (M1).
- **"Hệ số tắc đường" cụ thể là gì.** Câu 4 của tôi dùng cụm "đông lên bao nhiêu" vì chương không định nghĩa hệ số này (B4, E3). Nếu bạn tôi hỏi "đông lên bao nhiêu là tính thế nào", tôi không trả lời được.
- **"Sổ cái ba phần".** Chương không có cụm này; tôi phải tự ghép "sổ" với "ba phần" (F1). Với phần thứ ba, tôi chỉ nói được "phần dự báo chưa giải thích được". Tôi không lấy được ví dụ cụ thể từ chương, và công thức "∑x + ρ − f" tôi phải tự suy ra (F3, F6).
- **Luật C kiểm những gì ngoài giờ trả.** Tôi không kể được "mười chiều cam kết" là mười thứ gì (C10).
- **Ba giai đoạn của khách.** Tôi không giải thích được "đã nhận" khác "chờ đón" ở chỗ nào (C2).
- **Dự báo có thay đổi quyết định hay không.** Hình 3.1 làm tôi nghĩ là có; dòng 505–506 nói là không, trong thực nghiệm chính. Tôi viết câu 4 theo dòng 505–506, nhưng vẫn không chắc vì mục 4.x có "đưa dự báo vào bộ điều phối" (A9, E6).

---

## 6. Năm chỗ cần sửa nhất

1. **Mục 3.1 dùng khoảng 15 thuật ngữ trước khi định nghĩa** (X1; các mục A5, A8, A9, A12).
   - Mở chương bằng ba câu chuyện đời thường (M2).
   - Thêm câu bối cảnh "mô phỏng FleetPy, dữ liệu Manhattan 12–18/11/2018" (G3).
   - Thêm bảng thuật ngữ nhanh ở đầu mục 3.1.
   - Định nghĩa "phương án" bằng tiếng Việt (A8).
2. **"Xe bị ép" và hai luật phục hồi** (A12, A16, C11, D9, D13).
   - Đưa định nghĩa "xe bị ép" và ví dụ 40 giây do tắc đường (dòng 407–410) lên chỗ dùng đầu tiên (dòng 129–131).
   - Viết lại đoạn dòng 436–440, hiện không phân tích được ngữ pháp.
   - Thống nhất tên luật phục hồi (bốn cách viết thành một).
3. **Tiêu chí 3 của bộ chọn** (C8, D11).
   - Viết lại hàng Tiêu chí 3 ở Bảng 3.3 và đoạn dòng 422–428.
   - Viết "100%" thay cho "1.000.000 phần triệu" (có thể giữ con số gốc trong ngoặc).
   - Nói rõ hệ quả: trên thực tế, tiêu chí 3 chỉ còn tác dụng qua phần tổng phần dời.
   - Giải thích cách đọc thứ tự tiêu chí ngay trong chú thích Bảng 3.3 (C5).
4. **Lời hứa theo dự báo** (E1, E3, E6, A9).
   - Thêm một đoạn trực giác và ví dụ số (9:00 → 9:21) cho công thức (3.4).
   - Định nghĩa "hệ số tắc đường".
   - Nói thẳng rằng thực nghiệm chính dùng phát lại nên không đổi quyết định điều phối, và sửa chú thích Hình 3.1 cho khớp.
5. **Sổ và phép tách ba phần** (F1–F5).
   - Thống nhất một tên cho sổ.
   - Thêm ví dụ một dòng sổ (khách A) và ví dụ số cho công thức (3.5) (180 = 30 + 60 + 90).
   - Giải thích "tổng có dấu" và "hồ sơ lịch sử".

Các chỗ quan trọng ngay sau năm chỗ trên:
- "mười chiều cam kết" chưa được liệt kê (C10);
- trùng ký hiệu k, t, p, b/B (X3, D8, E2);
- "kịch bản" chưa được định nghĩa (B8);
- con số "năm luật" ở dòng 644 không khớp với Bảng 3.5 (G8).
