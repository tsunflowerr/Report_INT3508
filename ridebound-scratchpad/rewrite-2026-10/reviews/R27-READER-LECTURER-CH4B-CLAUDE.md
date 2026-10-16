# R27: Người đọc ngoài ngành và giảng viên chấm, Chương 4 phần B (mục 4.6–4.11), bản v7

**Tệp được nhận xét:** `drafts/09-chuong4-phanB-v7.tex` (488 dòng). Số dòng dưới đây là số dòng của tệp này.

**Đã đọc:**
- bản nháp v7;
- `drafts/07-chuong3-v3.tex`, chỉ dòng 1–120;
- `style/STYLE-GUIDE-VI.md`, `style/GLOSSARY-VI.md`, `WRITING-BRIEF.md`;
- mẫu DACN: qua các đoạn trích trong STYLE-GUIDE, cộng phần trích chữ tr. 31–34.

**Đọc thêm:** `drafts/08-chuong4-phanA-v4.tex` (bản ghi là "BẢN DÙNG ĐỂ GHÉP"). Tệp này chỉ dùng cho yêu cầu so thuật ngữ và số giữa phần B, phần A và Chương 3 ở Phần 2.

**Không đọc:** sổ bằng chứng, NOTES của người viết, các bản nhận xét khác, `codex-work/`. Các nhãn của Chương 3 nằm sau dòng 120 (`muc:dubao`, `eq:so`, `muc:gioihan`, `muc:kiemtra`) chưa được kiểm.

**Ghi chú ẩn `% EV`:** chỉ dùng khi ghi chú cho thấy một thông tin có trong ghi chú mà chữ in ra thiếu.

**Kiểm số học nội bộ.** Phép kiểm làm bằng `awk` và không có lỗi nào. Các phép đã kiểm:
- các tỉ lệ 445/1.714, 104/1.715, 325/1.715, 173/1.716;
- ba cách tính chi phí ở Bảng sàng lọc, chẳng hạn 7,79 × 445/1.714 = 2,02;
- 2 × 17,77 = 35,5;
- trung bình theo kịch bản ở Bảng dự báo: (8 × 14,44 + 8 × 1,35 + 5 × 0)/21 = 6,01; tương tự ra 1,94 và 0,17;
- điểm giữa hai khoảng tin cậy là −5,84 và −1,77;
- ba phần của sổ: 81,7 + 5.352,6 + 783,0 = 6.217,3 và 8,6 + 251,5 + 3.185,9 = 3.446,0;
- mọi phép trừ "phục vụ − trễ = không trễ" ở Bảng đệm;
- mọi tổng "sớm + trong ±60 + trễ quá 60 = phục vụ" ở Bảng hai phía;
- các số 2.305 = 2.338 − 33; 37,18/7,37 = 5,04; 7,27/37,18 = 0,196; 96 − 68 = 28; 2.434 − 2.387 = 47; 203 − 76 = 127; 96/127 = 0,756; 2.434 + 2.338 + 2.387 = 7.159.

---

## Phần 1. Người đọc ngoài ngành

Tôi đọc như một sinh viên năm cuối ngành khác, đã đọc Chương 3 và phần A. Mỗi mục dưới đây gồm vị trí, câu gốc, vì sao khó đọc, và câu đề xuất. Câu đề xuất giữ nguyên nghĩa và số. Dấu ★ đánh dấu chỗ tôi không hiểu được nếu không có người giải thích. Chữ trong `[…]` là chỗ tác giả phải tự điền hoặc kiểm lại, vì người đọc không đoán được.

**Tổng cộng 88 chỗ khó, trong đó 22 chỗ ★.**

### Mục 4.6: Vai trò của trần và thứ tự ưu tiên chọn phương án

**B1 (dòng 14), tên mục.**
- Câu gốc: «Vai trò của trần và thứ tự ưu tiên chọn phương án»
- Vì sao: tên mục gợi ra một kết quả đã đo, trong khi việc chính của mục là nói một phép thử chưa chạy. "Thứ tự ưu tiên" cũng khác "thứ tự tiêu chí" của Chương 3 (dòng 53) và của Bảng lộ trình ở phần A.
- Đề xuất: «Kết quả có phụ thuộc thứ tự tiêu chí của bộ chọn không?»

**B2 (dòng 17–18).**
- Câu gốc: «Điều phối không trần và luật C trần 30 giây dùng cùng tệp cấu hình và cùng bộ chọn ưu tiên ổn định, chỉ khác nhau ở trần giờ trả.»
- Vì sao: "tệp cấu hình" là chi tiết cài đặt mà người đọc không cần.
- Đề xuất: «Điều phối không trần và luật C trần 30 giây dùng cùng một bộ chọn, bộ chọn ưu tiên ổn định; hai cấu hình chỉ khác nhau ở trần giờ trả.»

**B3 (dòng 18–19).**
- Câu gốc: «Chênh lệch giữa chúng ở các mục trước vì vậy là chênh lệch khi thêm trần mà giữ nguyên bộ chọn, trên hai tập khách khác nhau.»
- Vì sao: cụm cuối câu treo lơ lửng, không rõ bổ nghĩa cho từ nào.
- Đề xuất: «Vì vậy chênh lệch giữa hai cấu hình ở các mục trước là chênh lệch khi thêm trần và giữ nguyên bộ chọn. Hai cấu hình phục vụ hai nhóm khách không hoàn toàn trùng nhau.»

**B4 ★ (dòng 19–20).**
- Câu gốc: «Câu hỏi còn mở là đánh đổi này có còn khi bộ chọn ưu tiên chi phí kế hoạch (tiêu chí 4) thay vì ổn định (tiêu chí 3 ở Bảng…) hay không.»
- Vì sao:
  - mục này chưa nêu "đánh đổi này" là đánh đổi gì;
  - "chi phí kế hoạch" được dùng trước khi định nghĩa (định nghĩa nằm ở chú thích bảng, dòng 32–33);
  - người đọc phải lật lại Chương 3 để biết tiêu chí 3 và 4 là gì.
- Đề xuất: «Câu hỏi còn mở: nếu bộ chọn bỏ tiêu chí ổn định (tiêu chí 3 ở Bảng~\ref{bang:rangbuoc}) để xét ngay chi phí kế hoạch (tiêu chí 4, tức thời lượng còn lại của các tuyến dự kiến), thì đánh đổi giữa số lượt phục vụ và số lượt trễ ở mục~\ref{muc:c4-ketqua} có còn không?»

**B5 (dòng 23).**
- Câu gốc: «Bằng chứng hiện có là một phép sàng lọc trên tập tắc đường cố định»
- Vì sao: "phép sàng lọc" chưa được định nghĩa, và người ngoài ngành hiểu "sàng lọc" là lọc bớt.
- Đề xuất: «Bằng chứng hiện có chỉ là một phép tính lại nhanh trên các lượt quyết định đã ghi của tập tắc đường cố định, dưới đây gọi là phép sàng lọc (Bảng~\ref{bang:c4-sangloc}).»

**B6 ★ (dòng 23–25).**
- Câu gốc: «…bộ chọn được chạy lại trên cùng các phương án nhưng bỏ tiêu chí 3, và mô phỏng không chạy tiếp từ lựa chọn mới.»
- Vì sao: vế sau nghe như dịch máy, và người đọc không hiểu hệ quả của nó.
- Đề xuất: «Ở mỗi lượt, bộ chọn được chạy lại trên đúng các phương án của lượt đó nhưng bỏ tiêu chí 3. Lựa chọn mới chỉ được ghi lại để so; nó không được đưa trở lại mô phỏng, nên các lượt sau vẫn đi theo lựa chọn cũ.»

**B7 ★ (dòng 25).**
- Câu gốc: «Với thứ tự gốc, phép chạy lại cho đúng cả 62.837 lựa chọn đã ghi.»
- Vì sao:
  - câu không nói mục đích, mà mục đích là kiểm tra cách chạy lại;
  - đơn vị không rõ: 62.837 "lựa chọn" chênh xa 1.714 lượt trong bảng;
  - ghi chú ẩn cho biết đây là tổng của năm cấu hình, nhưng chữ in ra không nói.
- Đề xuất: «Để kiểm tra cách chạy lại, bộ chọn với thứ tự tiêu chí gốc được chạy trước; nó cho lại đúng cả 62.837 lựa chọn đã ghi, cộng trên năm cấu hình của tập [một "lựa chọn" là phương án của một xe ở một lượt, hay là gì khác].»

**B8 ★ (dòng 30–33), chú thích Bảng sàng lọc.**
- Câu gốc: «…thời gian đi không đổi, bộ chạy cũ, nên không chuyển sang tập kiểm tra chính […] tính lặp qua các lượt, không phải chi phí vận hành.»
- Vì sao:
  - chú thích dài khoảng 60 tiếng;
  - "không chuyển sang" là dịch từ "do not transfer";
  - không hiểu "tính lặp qua các lượt" nghĩa là gì;
  - không nhắc lại U và C-30 là gì (quy tắc 12).
- Đề xuất: «Phép sàng lọc bỏ tiêu chí ổn định của bộ chọn trên tập tắc đường cố định (16 kịch bản mỗi cấu hình, bộ chạy cũ). U: điều phối không trần; C-30: luật C trần 30 giây. Mỗi cột dùng các lượt quyết định đã ghi của chính cấu hình đó, nên hai cột là hai tập tình huống khác nhau. Chi phí kế hoạch là thời lượng còn lại của các tuyến dự kiến, không phải chi phí vận hành. Kết quả không dùng thay cho tập kiểm tra chính.» [Nếu "tính lặp qua các lượt" có nghĩa riêng thì thêm một câu giải thích.]

**B9 ★ (dòng 44–47), ba cách tính chi phí.**
- Vì sao:
  - người đọc không biết dòng 2 và dòng 3 khác nhau ở đâu, và nên tin dòng nào;
  - số 0,3069 và 0,0794 có bốn chữ số thập phân, lệch với các dòng khác (quy tắc 27).
- Đề xuất nhãn dòng 3: «Phần giảm tính trên tổng chi phí kế hoạch của mọi lượt quyết định, kể cả lượt không có yêu cầu mới», với hai số 0,31 và 0,08. Thêm một câu kết luận sau bảng (xem M4).

**B10 ★ (dòng 50), nhãn khối dưới của bảng.**
- Câu gốc: «Tổng dời giờ trả do điều phối tăng thêm trên đội xe, ở các lượt đổi lựa chọn (s)»
- Vì sao: một chuỗi danh từ dài, khó tách nghĩa.
- Đề xuất: «Phần dời giờ trả do điều phối tăng thêm, cộng trên mọi khách của đội xe, ở các lượt đổi lựa chọn (s)»

**B11 (dòng 62).**
- Câu gốc: «Số yêu cầu được nhận không đổi ở lượt nào.»
- Vì sao: trật tự từ lạ.
- Đề xuất: «Ở mọi lượt, bỏ tiêu chí 3 không làm đổi số yêu cầu được nhận.»

**B12 (dòng 62–64).**
- Vì sao: 445/1.714 và 104/1.715 xuất hiện lần thứ ba (trong bảng, trong câu đọc bảng và ở đây). Quy tắc 20 bảo không trình bày một dữ liệu ba lần.
- Đề xuất: đưa C-60 và C-120 thành hai cột của bảng, rồi rút đoạn thành: «Tỉ lệ lượt đổi lựa chọn giảm dần khi trần chặt hơn: 25,96\% khi không trần, 18,95\% (325 trong 1.715) với trần 120 giây, 10,08\% (173 trong 1.716) với trần 60 giây và 6,06\% với trần 30 giây.»

**B13 (dòng 64–65).**
- Câu gốc: «Mỗi tỉ lệ đo trên trạng thái của chính cấu hình, nên đây không phải tác động của trần trên cùng một trạng thái.»
- Vì sao: câu trừu tượng.
- Đề xuất: «Mỗi tỉ lệ được đo trên các lượt quyết định của chính cấu hình đó, và các cấu hình gặp những tình huống khác nhau. Vì vậy không thể nói trần làm giảm số lần đổi lựa chọn.»

**B14 (dòng 66).**
- Câu gốc: «Dưới trần 30 giây, lượt có tổng dời tăng thêm lớn nhất, 35,5 giây, chia cho hai khách, mỗi khách 17,77 giây.»
- Vì sao: "chia cho" nghe như phép chia.
- Đề xuất: «Dưới trần 30 giây, lượt có phần dời tăng thêm lớn nhất (35,5 giây) gồm hai khách, mỗi khách bị dời thêm 17,77 giây.»

**B15 ★ (dòng 69–70).**
- Câu gốc: «Phép thử đổi thứ tự ưu tiên … chưa được chạy; bằng chứng hiện có là phép sàng lọc trên trạng thái cố định ở trên, vốn không cho biết kết quả phục vụ và đúng giờ trên quỹ đạo.»
- Vì sao:
  - câu dài khoảng 45 tiếng;
  - "quỹ đạo" chưa được định nghĩa;
  - "trạng thái cố định" dễ lẫn với "tập tắc đường cố định".
- Đề xuất: «Phép thử đổi thứ tự tiêu chí của bộ chọn trên 34 kịch bản của tập kiểm tra chính chưa được chạy. Phép sàng lọc ở trên chỉ xét từng lượt riêng lẻ, nên không cho biết số lượt phục vụ và số lượt đúng giờ khi cả lần chạy đi theo lựa chọn mới.»

**B16 ★ (dòng 71).**
- Câu gốc: «Khóa luận vì vậy chưa tách được phần của trần và phần của bộ chọn trong độ tin cậy đã đo.»
- Vì sao: "độ tin cậy" chưa được định nghĩa (phần A dùng "đúng giờ"); "tách phần" mơ hồ.
- Đề xuất: «Vì vậy chưa biết khoảng cách giữa điều phối không trần và luật C về số lượt trễ có giữ nguyên khi cả hai dùng bộ chọn ưu tiên chi phí hay không.»

### Mục 4.7: Lời hứa theo dự báo

**B17 (dòng 79–81).**
- Vì sao: mục mở bằng số trước khi nói "dự báo" là dự báo cái gì. Chữ "(gộp theo khách)" lại gắn với số đếm chứ không gắn với tỉ lệ.
- Đề xuất: «Lời hứa theo dự báo cộng sẵn vào lời hứa đầu mức tắc đường thường gặp của khung giờ, lấy từ hồ sơ tắc đường lịch sử (mục~\ref{muc:dubao}). Trên 21 kịch bản ngày thường có dự báo, với luật C trần 30 giây, số khách tới muộn hơn lời hứa đầu quá một phút giảm từ 68 xuống 2 trong 1.471 khách được phục vụ. Tính trung bình theo kịch bản, tỉ lệ này giảm từ 6,01\% xuống 0,17\%.»

**B18 (dòng 84–85).**
- Câu gốc: «…trễ được so với lời hứa đầu của chính cách hứa.»
- Vì sao: "cách hứa" là từ mới, dùng 9 lần trong phần B mà chưa được định nghĩa.
- Đề xuất: «Mỗi cách tính lời hứa đầu, gọi tắt là cách hứa, được đánh giá so với lời hứa đầu do chính nó đưa ra.»

**B19 ★ (dòng 85–87).**
- Câu gốc: «Đối chứng thứ hai là \emph{đệm cùng giá}: mỗi lời hứa đầu được kéo dài một tỉ lệ cố định của thời gian còn lại tới giờ trả…»
- Vì sao:
  - câu không nói đối chứng thứ nhất là gì;
  - "cùng giá" là ẩn dụ (ở đây "giá" là tổng độ dài thêm);
  - "thời gian còn lại" không rõ tính từ lúc nào;
  - đây là đệm theo tỉ lệ, khác "đệm" mà phần A định nghĩa (cộng một khoảng cố định, phần A dòng 15–16).
- Đề xuất: «Có hai đối chứng. Thứ nhất là lời hứa không dự báo. Thứ hai là đệm cùng độ dài: mỗi lời hứa đầu được kéo dài thêm một tỉ lệ cố định của khoảng từ lúc hứa tới giờ trả đã hứa. Khác cách đệm ở mục~\ref{muc:c4-dem}, phần cộng thêm ở đây tỉ lệ với độ dài chuyến. Tỉ lệ được chọn riêng cho từng khung giờ sao cho tổng phần kéo dài bằng của lời hứa theo dự báo [tỉ lệ được chọn trên chính 21 kịch bản này hay trên các ngày khác].»

**B20 ★ (dòng 117–118).**
- Câu gốc: «Khoảng tin cậy 95\% của chênh lệch dự báo trừ không dự báo, tính theo phân phối $t$ trên 8 cụm ngày và khung giờ, là từ …»
- Vì sao:
  - câu dài khoảng 40 tiếng;
  - "$t$" và "cụm" chưa được giải thích;
  - không có giá trị chênh lệch (−5,84 = 0,17 − 6,01, đúng là điểm giữa khoảng).
- Đề xuất: «Chênh lệch giữa có dự báo và không dự báo là −5,84 điểm phần trăm. Để tính khoảng tin cậy 95\%, 21 kịch bản được gom thành 8 nhóm theo ngày và khung giờ, mỗi nhóm là một quan sát; theo phân phối Student, khoảng tin cậy là từ −10,54 đến −1,15 điểm phần trăm.»

**B21 ★ (dòng 118–119).**
- Câu gốc: «…khoảng chạy từ −3,62 đến +0,07, tức chạm 0. Lợi thế so với cách đệm này vì vậy còn mong manh.»
- Vì sao:
  - "chạm 0" sai nghĩa: +0,07 lớn hơn 0, nên khoảng *chứa* 0;
  - "mong manh" là từ văn chương;
  - câu ngầm coi như lợi thế đã có.
- Đề xuất: «…khoảng tin cậy từ −3,62 đến +0,07 điểm phần trăm, tức có chứa 0. Vì vậy chưa thể nói lời hứa theo dự báo tốt hơn cách đệm cùng độ dài.»

**B22 ★ (dòng 119–120).**
- Câu gốc: «Kết quả cũng chỉ dựa trên ba buổi sáng, và ngày 12/11 là ngày nguồn của mọi dự báo.»
- Vì sao:
  - "ba buổi sáng" nghe như mâu thuẫn với "21 kịch bản";
  - "ngày nguồn" chưa được định nghĩa;
  - dòng 368 lại viết "các ngày nguồn", ở số nhiều.
- Đề xuất: «Toàn bộ mức giảm nằm ở khung 7 và 8 giờ của ba ngày 14–16/11, vì ở khung 17 giờ cả ba cách hứa đều có 0\% khách trễ. Ngoài ra, mọi hồ sơ dự báo đều dựng từ dữ liệu có ngày 12/11 [một ngày nguồn hay nhiều ngày].»

**B23 (dòng 123–124).**
- Câu gốc: «…cùng ở mức 30 giây, cũng xuống 0,17\%»
- Vì sao: thiếu mức xuất phát của phép giảm.
- Đề xuất: «…cũng còn 0,17\% khi có dự báo (từ […]\% và […]\% khi không dự báo)».

**B24 (dòng 126).**
- Câu gốc: «Dự báo và trần nhắm vào hai phần khác nhau của độ lệch giờ trả.»
- Vì sao: câu không nói hai phần đó là gì.
- Đề xuất: «Dự báo nhắm vào phần tắc đường đoán trước được, còn trần nhắm vào phần dời do điều phối.»

**B25 (dòng 129–130).**
- Câu gốc: «lời hứa trả dài thêm … và lời hứa đón 3,2 giây»
- Vì sao: hai thuật ngữ bị rút gọn.
- Đề xuất: «lời hứa giờ trả dài thêm trung bình 13,7 giây (khung 7 giờ: 27,8 giây) và lời hứa giờ đón dài thêm 3,2 giây».

**B26 (dòng 130–132).**
- Câu gốc: «Con số 7,37 giây ở Bảng… khác: đó là …»
- Đề xuất: «Con số này khác 7,37 giây ở Bảng~\ref{bang:c4-tran120}, vì 7,37 giây là trung bình gộp trên cả 2.338 khách của 34 kịch bản, kể cả khách cuối tuần không có dự báo (dài thêm 0 giây).»

**B27 (dòng 134).**
- Câu gốc: «Kết quả này dựa trên một thế giới gần như tất định.»
- Vì sao: Bảng thuật ngữ (mục G) đã loại "thế giới"; "tất định" là thuật ngữ chưa giải thích.
- Đề xuất: «Mô phỏng ở đây gần như không có yếu tố ngẫu nhiên.»

**B28 ★ (dòng 134–135).**
- Câu gốc: «Với luật C, kéo dãn lời hứa theo hệ số tắc đường thật cho giờ trả khớp trong vòng 2 giây với mọi khách không bị điều phối dời…»
- Vì sao: người đọc không biết "hệ số thật" là hệ số chỉ biết được sau khi chạy.
- Đề xuất: «Với luật C, nếu biết trước hệ số tắc đường sẽ xảy ra và kéo dài lời hứa theo đúng hệ số đó, giờ trả thực tế khớp lời hứa trong vòng 2 giây ở cả 2.305 khách không bị điều phối dời (34 kịch bản).»

**B29 (dòng 139–141).**
- Câu gốc: «…phần lớn được hồ sơ lịch sử giải thích, còn ở chiều tuyết … thì gần như ngược lại. Phần thứ hai phụ thuộc dự báo đang dùng…»
- Vì sao: "ngược lại" mơ hồ, và "phần thứ hai" bắt người đọc tự đếm.
- Đề xuất: «Theo sổ, ở ngày thường 86,1\% số giây trễ thuộc phần hồ sơ lịch sử tính trước được và 12,6\% là phần còn lại; ở chiều tuyết (mục~\ref{muc:c4-tuyet}), chỉ 7,3\% thuộc phần hồ sơ lịch sử và 92,5\% là phần còn lại. Phần hồ sơ lịch sử phụ thuộc dự báo đang dùng; phần còn lại chỉ là phần dự báo này chưa giải thích được, không phải phần không ai biết trước được.»

**B30 (dòng 175), chú thích hình.**
- Câu gốc: «Ba phần của số giây trễ theo sổ theo từng khách»
- Vì sao: hai chữ "theo" đi liền nhau.
- Đề xuất: «Tổng số giây trễ chia thành ba phần theo sổ của từng khách (công thức~\eqref{eq:so})…»

**B31 (dòng 186–188).**
- Câu gốc: «Có 3 trong 32 lần chạy dừng, vì xe trong FleetPy tới một điểm đón muộn hơn giờ đón muộn nhất 1,67 hoặc 2,69 giây.»
- Vì sao: có ba lần chạy nhưng chỉ hai con số, và câu không nói cái gì làm lần chạy dừng.
- Đề xuất: «3 trong 32 lần chạy bị dừng giữa chừng: một xe tới điểm đón muộn hơn giờ đón muộn nhất 1,67 hoặc 2,69 giây [lần nào số nào], và điều kiện kiểm tra lúc đón của FleetPy dừng lần chạy.»

**B32 (dòng 188).**
- Câu gốc: «Ở các lần chạy xong, luật C không phải phục hồi lần nào.»
- Vì sao: "phải phục hồi" khác thuật ngữ "bị ép" của phần A (Bảng nghĩa vụ, Bảng chỉ số) và của Bảng thuật ngữ.
- Đề xuất: «Ở các lần chạy hoàn tất, luật C không có quyết định nào bị ép.»

**B33 (dòng 188–190).**
- Câu gốc: «Luật hạn chót vẫn phải phục hồi ở 47,6\% … (trung bình trên 15 kịch bản).»
- Vì sao: con số 15 khác 16 mà không có lời giải thích.
- Đề xuất: «Luật hạn chót vẫn bị ép ở 47,6\% lượt quyết định, so với 62,8\% khi không đưa dự báo vào (trung bình theo kịch bản, trên 15 kịch bản [vì sao không phải 16]).»

**B34 (dòng 191–192).**
- Câu gốc: «Cách triển khai được chọn là lớp lời hứa; kết luận này chỉ áp cho cách đưa dự báo vào đã thử.»
- Vì sao: "lớp lời hứa" chưa được định nghĩa, và câu không nêu lý do chọn.
- Đề xuất: «Vì vậy khóa luận chỉ dùng dự báo ở bước báo giờ cho khách, không đưa vào bộ điều phối. Kết luận này chỉ đúng với cách đưa dự báo vào bộ điều phối đã thử ở đây.»

**B35 ★ (dòng 195).**
- Câu gốc: «Ba mô hình cố định ước lượng phân vị 90 của độ trễ từng khách từ các đặc trưng có lúc hứa.»
- Vì sao:
  - "cố định" mang nghĩa thứ ba trong phần B (đã có "tập cố định", "trạng thái cố định");
  - "phân vị 90" chưa được giải thích (Bảng thuật ngữ F đòi giải thích ở lần đầu);
  - "đặc trưng có lúc hứa" nghe như dịch máy.
- Đề xuất: «Khóa luận thử ba mô hình học máy, huấn luyện một lần rồi giữ nguyên, để ước lượng phân vị 90 của độ trễ từng khách, tức mức trễ mà 90\% khách giống khách đó không vượt quá. Mô hình chỉ dùng thông tin đã có ở thời điểm hứa.»

**B36 (dòng 196–197).**
- Câu gốc: «Đó là cây tăng cường độ dốc (gradient boosting), cùng mô hình ấy nhưng bỏ số khách khác trên xe…»
- Vì sao: "cây tăng cường độ dốc" là dịch từng chữ, ít gặp; "bỏ số khách" dễ hiểu nhầm thành bỏ khách.
- Đề xuất: «Ba mô hình là: cây quyết định tăng cường theo gradient (gradient boosting); cùng mô hình ấy nhưng không dùng thông tin số khách khác trên xe; và hồi quy phân vị tuyến tính.»

**B37 ★ (dòng 197–198).**
- Câu gốc: «Đối chứng là lời hứa theo dự báo cộng một khoảng đệm đều, cùng độ dài thêm trung bình 30 giây; trên tập tắc đường cố định là đệm đều.»
- Vì sao: đây là câu khó nhất của mục. "Cùng" với cái gì? Vế sau lặp lại "đệm đều" mà không nói khác gì.
- Đề xuất: «Mỗi mô hình được so với một đối chứng đơn giản: cộng cùng một khoảng vào lời hứa của mọi khách, sao cho lời hứa dài thêm trung bình 30 giây. Trên các ngày có dự báo, khoảng này cộng vào lời hứa theo dự báo; trên tập tắc đường cố định, nơi không có dự báo, nó cộng vào lời hứa đầu.» [Kiểm lại xem đúng ý chưa.]

**B38 (dòng 198).**
- Câu gốc: «Mọi phép so dùng các ngày không dùng để học.»
- Vì sao: "học" là khẩu ngữ, và câu lặp chữ "dùng".
- Đề xuất: «Mọi phép so đều làm trên những ngày không dùng để huấn luyện mô hình.»

**B39 (dòng 202–203).**
- Câu gốc: «không quá 1 giây so với đối chứng»; «không quá 15 giây so với đối chứng»
- Vì sao: dịch từ "within … of".
- Đề xuất: «không vượt đối chứng quá 1 giây»; «không vượt đối chứng quá 15 giây».

**B40 (dòng 208).**
- Câu gốc: «Với luật C có dự báo, mô hình không giảm thêm tỉ lệ trễ.»
- Vì sao: dùng số ít trong khi có ba mô hình.
- Đề xuất: «Với luật C có dự báo, không mô hình nào giảm thêm tỉ lệ trễ.»

**B41 (dòng 208–210).**
- Câu gốc: «…mức giảm là 0,69 điểm phần trăm ở ngày 15/11 (145 khách) và 0 ở ngày 16/11, kèm lời hứa dài quá mức cho phép.»
- Vì sao: 0,69 điểm phần trăm của 145 khách đúng bằng 1 khách, nói số khách dễ hiểu hơn. "Mức cho phép" không nói là điều kiện nào.
- Đề xuất: «Với điều phối không trần, mô hình chỉ bớt được 1 trong 145 khách trễ ở ngày 15/11 (0,69 điểm phần trăm) và không bớt khách nào ở ngày 16/11, trong khi lời hứa dài thêm vượt giới hạn ở điều kiện [thứ hai hoặc thứ ba].»

**B42 (dòng 210–211).**
- Câu gốc: «…tỉ lệ trễ giảm từ 12,89\% xuống 11,65\% trên 807 khách (gộp theo khách), nhưng 7,1\% khách tới sớm quá một phút, so với 0\% khi đệm đều.»
- Vì sao: thiếu số đếm (quy tắc 24).
- Đề xuất: «…số khách trễ giảm từ 104 xuống 94 trong 807 khách (12,89\% xuống 11,65\%), nhưng 57 khách (7,1\%) tới sớm quá một phút, so với 0 khách khi đệm đều.»
- Ghi chú: 104, 94 và 57 tính ngược từ tỉ lệ × 807; tác giả đối chiếu với output.

**B43 (dòng 211).**
- Câu gốc: «Bỏ số khách trên xe không đổi kết quả nào.»
- Đề xuất: «Mô hình không dùng số khách trên xe cho cùng các kết luận trên.»

### Mục 4.8: So với cách đệm lời hứa

**B44 (dòng 218–219).**
- Câu gốc: «…bằng luật C trần 30 giây.»
- Vì sao: không rõ là luật C nào.
- Đề xuất: «…bằng luật C trần 30 giây có dự báo và không đệm.»

**B45 (dòng 224–225).**
- Câu gốc: «…nên đây không phải đối chứng ghép cặp với luật C; hai bên chỉ chung 2.207 khách.»
- Vì sao: "đối chứng ghép cặp" là thuật ngữ thống kê chưa giải thích.
- Đề xuất: «Đệm không đổi quyết định nào: điều phối không trần vẫn phục vụ đúng những khách đó, với đúng giờ trả thực tế đó. Vì vậy cách đệm và luật C được so trên hai nhóm khách khác nhau, chỉ chung 2.207 khách, không phải trên cùng một nhóm.»

**B46 (dòng 225–226).**
- Câu gốc: «Bảng… xếp các cách hứa thành ba khối có độ dài thêm gần bằng nhau.»
- Vì sao: dễ hiểu nhầm thành ba khối bằng nhau.
- Đề xuất: «Bảng… chia các cách hứa thành ba khối; trong mỗi khối, lời hứa dài thêm gần bằng nhau (khoảng 7, 37 và 67 giây).»

**B47 (dòng 266), nhãn đầu đoạn.**
- Câu gốc: «Vai trò của từng thành phần.»
- Vì sao: không nói thành phần nào. Nội dung thật là bốn điều đọc được từ hai bảng.
- Đề xuất: «Bốn điều đọc được từ hai bảng.»

**B48 (dòng 266–267).**
- Câu gốc: «Thứ nhất, ở độ dài thêm gần bằng nhau, luật C hơn ở ngưỡng một phút và kém ở ngưỡng hai phút.»
- Vì sao: không rõ hơn, kém về chỉ số nào và so với ai.
- Đề xuất: «Thứ nhất, khi lời hứa dài thêm gần bằng nhau, luật C có nhiều lượt không trễ quá một phút hơn điều phối không trần, nhưng ít lượt không trễ quá hai phút hơn.»

**B49 (dòng 268–269).**
- Câu gốc: «Cách đệm chỉ bằng luật C ở ngưỡng một phút khi lời hứa dài thêm khoảng năm lần…»
- Vì sao: "chỉ bằng … khi" đọc được theo hai nghĩa.
- Đề xuất: «Muốn bằng luật C ở ngưỡng một phút, cách đệm phải làm lời hứa dài thêm gấp khoảng năm lần (37,18 so với 7,37 giây).»

**B50 (dòng 273).**
- Câu gốc: «với cách đệm 30 giây là 44 trong 2.434 khách»
- Đề xuất: «với điều phối không trần đệm 30 giây là 44 trong 2.434 khách».

**B51 ★ (dòng 309–310).**
- Câu gốc: «Lợi thế 28 lượt của cách đệm ở ngưỡng hai phút đi cùng 96 lượt phục vụ nhiều hơn, không phải ít khách trễ hơn.»
- Vì sao: câu quá nén; người đọc phải tự làm phép trừ.
- Đề xuất: «Cách đệm có nhiều hơn 28 lượt không trễ quá hai phút chỉ vì nó phục vụ nhiều hơn 96 lượt: nó có 68 khách trễ quá hai phút, còn luật C không có khách nào (96 − 68 = 28).»

**B52 (dòng 313–314).**
- Câu gốc: «…và một khách bị dời 590,1 giây.»
- Đề xuất: «…và một khách bị dời tổng cộng 590,1 giây (gần 10 phút).»

**B53 (dòng 318–320).**
- Câu gốc: «Khác biệt là luật hạn chót phải phục hồi ở 41,3\% lượt quyết định… còn luật C không lần nào.»
- Vì sao: "phải phục hồi" khác "bị ép"; câu dài khoảng 40 tiếng.
- Đề xuất: «Khác biệt nằm ở việc giữ lời hứa của chính mình. Luật hạn chót bị ép ở 41,3\% lượt quyết định (trung bình theo kịch bản) và phá lời hứa của chính nó ở 28 trong 34 kịch bản; luật C không có quyết định nào bị ép và không phá lời hứa ở kịch bản nào (Bảng~\ref{bang:c4-nghiavu}).»

**B54 (dòng 323).**
- Câu gốc: «Trần cũng là một núm vặn.»
- Vì sao: ẩn dụ khẩu ngữ (quy tắc 14).
- Đề xuất: «Mức trần cũng là một tham số chỉnh được.»

**B55 (dòng 324).**
- Câu gốc: «Lời hứa của nó chỉ dài thêm khoảng một phần năm của cách đệm…»
- Vì sao: chữ "nó" nằm xa tên mà nó chỉ.
- Đề xuất: «Lời hứa của trần 120 giây chỉ dài thêm 7,27 giây, khoảng một phần năm mức 37,18 giây của cách đệm, và trần 120 giây phục vụ ít hơn điều phối không trần 47 lượt.»

**B56 (dòng 328–329).**
- Câu gốc: «…là lựa chọn cạnh tranh.»
- Vì sao: dịch từ "competitive option".
- Đề xuất: «…đệm trên điều phối không trần không kém luật C, và còn phục vụ thêm 96 lượt.»

**B57 (dòng 330–331).**
- Câu gốc: «…thì luật C cho điều đó; đổi lại là 96 lượt phục vụ và 242 khách đi chung.»
- Vì sao: "cho điều đó" là khẩu ngữ, và "đổi lại là 96 lượt" đọc như được thêm 96 lượt.
- Đề xuất: «Nếu hãng xe cần giới hạn phần dời giờ trả do ghép thêm khách cho từng người, kể cả khi không có dự báo, thì luật C làm được điều này theo cách xây dựng luật; đổi lại, luật C phục vụ ít hơn 96 lượt và có ít hơn 242 khách đi chung.»

**B58 (dòng 331).**
- Câu gốc: «Hai cách dùng chung được.»
- Vì sao: câu không dẫn số liệu.
- Đề xuất: «Hai cách cũng dùng chung được: luật C có dự báo cộng đệm 30 giây cho 2.336 lượt không trễ quá một phút và 2.338 lượt không trễ quá hai phút (Bảng~\ref{bang:c4-dem}).»

### Mục 4.9: Khi dự báo không đủ: chiều tuyết 15/11/2018

**B59 (dòng 339–340).**
- Câu gốc: «…dự báo lịch sử chỉ giảm số khách…»
- Vì sao: "dự báo lịch sử" là tên thứ tư cho cùng một thứ. Mục cũng chưa nói "chiều tuyết" là gì.
- Đề xuất mở mục: «Chiều 15/11/2018 có một trận tuyết lớn [nơi đo, nguồn]. Trên 601 khách được phục vụ của 8 kịch bản chiều hôm đó, lời hứa theo dự báo chỉ giảm số khách tới muộn hơn lời hứa đầu quá một phút từ 41 xuống 34.»

**B60 (dòng 349).**
- Câu gốc: «Bảng… phát lại thêm vài cách hứa dùng thông tin cùng ngày.»
- Vì sao: bảng không tự "phát lại".
- Đề xuất: «Bảng… cho kết quả phát lại của vài cách hứa có dùng thêm thông tin của chính ngày tuyết.»

**B61 (dòng 349–350).**
- Câu gốc: «Các cách ``trộn'' lấy trung bình nhân giữa mức tăng theo hồ sơ lịch sử và xu hướng tăng gần nhất của hệ số tắc đường trong ngày.»
- Vì sao: không rõ "xu hướng tăng gần nhất" được đo thế nào.
- Đề xuất: «Các cách ``trộn'' lấy trung bình nhân của hai mức tăng: mức tăng theo hồ sơ lịch sử, và mức tăng của hệ số tắc đường trong các khung 15 phút vừa qua của chính ngày đó.» [Kiểm lại xem đúng ý chưa.]

**B62 ★ (dòng 350–351).**
- Câu gốc: «Con số 19 dùng dữ liệu buổi sáng không được giao cho khung này, và một quy tắc có ngưỡng chọn sau khi xem dữ liệu cũng cho con số đó.»
- Vì sao:
  - số 19 được nhắc trước khi người đọc thấy bảng;
  - "không được giao" nghe như dịch máy;
  - câu không nói hệ quả.
- Đề xuất: «Hàng ``trộn có buổi sáng'' (19 khách trễ) dùng cả hệ số tắc đường buổi sáng cùng ngày, là dữ liệu mà thiết kế thử không cho cách hứa của khung chiều dùng. Một quy tắc có ngưỡng chọn sau khi xem dữ liệu cũng cho đúng 19. Vì vậy con số 19 không được coi là kết quả của một cách hứa dùng được.»

**B63 ★ (dòng 370–371), hai hàng của bảng tuyết.**
- Câu gốc: «không được giao cho khung này»; «mức hiện tại vẫn lấy đúng»
- Vì sao: cả hai không đọc được.
- Đề xuất:
  - «Thêm hệ số cùng ngày từ 6 giờ; thiết kế không cho khung chiều dùng dữ liệu này»;
  - «Như hàng trên, nhưng mức tăng gần nhất chỉ lấy từ các khung đã kết thúc; hệ số của khung hiện tại vẫn dùng giá trị đúng» [kiểm lại].

**B64 (dòng 358), chú thích bảng tuyết.**
- Câu gốc: «trên ngày đã được xem»
- Đề xuất: «trên chính ngày đã được xem trước khi thiết kế các cách hứa này».

**B65 (dòng 383).**
- Câu gốc: «Theo sổ, mô hình có dữ liệu buổi sáng giải thích thêm 886,9 giây…»
- Vì sao: "mô hình có dữ liệu buổi sáng" là tên khác của hàng "trộn có buổi sáng", và câu không nhắc cách này dùng dữ liệu không được phép.
- Đề xuất: «Theo sổ, ngay cả cách ``trộn có buổi sáng'', vốn dùng dữ liệu không được phép, cũng chỉ giải thích thêm 886,9 giây, tức 25,7\% của 3.445,9 giây trễ; 2.299,0 giây (66,7\%) vẫn chưa được giải thích bằng các cách đã thử.»

**B66 (dòng 384).**
- Câu gốc: «Đây là một sự kiện đã xem trước.»
- Vì sao: câu mơ hồ.
- Đề xuất: «Chiều tuyết đã được xem trước khi thiết kế các cách hứa trên, nên mọi con số ở Bảng~\ref{bang:c4-tuyet} là kết quả trên dữ liệu đã xem, không phải phép thử độc lập.»

**B67 (dòng 384–385).**
- Câu gốc: «Giai đoạn 9/2018--12/2019 chỉ có 5 đợt tuyết từ 25,4 mm trở lên, kể cả đợt này, nên một phép kiểm dự báo cho ngày có sự kiện cần nhiều sự kiện độc lập hơn.»
- Vì sao: câu dài khoảng 40 tiếng, "ngày có sự kiện" mơ hồ, và không nói nơi đo.
- Đề xuất: «Từ 9/2018 đến 12/2019 chỉ có 5 đợt tuyết từ 25,4 mm trở lên, kể cả đợt này [nơi đo]. Muốn kiểm một cách hứa cho những ngày bất thường như vậy cần thêm nhiều đợt khác, chưa dùng khi thiết kế.»

### Mục 4.10: Kiểm tra tính hợp lệ của kết quả

**B68 (dòng 392–394).**
- Câu gốc: «Không có lượt quyết định nào phải phục hồi, 0 trong 20.101 và 0 trong 20.435 lượt.»
- Vì sao: "phải phục hồi" khác "bị ép", và câu không nói số nào thuộc cấu hình nào.
- Đề xuất: «Không lượt quyết định nào bị ép: 0 trong 20.101 lượt với trần 30 giây và 0 trong 20.435 lượt với trần 120 giây.» (Xem thêm M3.)

**B69 (dòng 397).**
- Câu gốc: «Giới hạn tính toán không cắt kết quả trên tập này.»
- Vì sao: "cắt" là dịch từ "truncate".
- Đề xuất: «Trên tập kiểm tra chính, các giới hạn tính toán của bộ sinh không làm mất phương án nào.»

**B70 (dòng 398–399).**
- Câu gốc: «giới hạn khối lượng khám phá»
- Vì sao: cụm này không được định nghĩa ở đâu trong phần A, phần B hay Chương 3 dòng 1–120.
- Đề xuất: «giới hạn khối lượng khám phá (số [bước/phép chèn] tối đa bộ sinh được thử ở mỗi lượt)».

**B71 ★ (dòng 399–400).**
- Câu gốc: «Giới hạn 2 yêu cầu mới mỗi lượt chỉ một lần để một yêu cầu sang lượt sau, trong 34 lần chạy của mỗi cấu hình.»
- Vì sao: câu không đọc được; "chỉ một lần" là cho mỗi cấu hình hay cho tổng cộng?
- Đề xuất: «Giới hạn 2 yêu cầu mới mỗi lượt chỉ phải dời một yêu cầu sang lượt sau đúng một lần, tính trên cả 34 lần chạy của mỗi cấu hình.»

**B72 ★ (dòng 400–401).**
- Câu gốc: «Chênh lệch giữa các cấu hình vì vậy phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán.»
- Vì sao: "gói cam kết" là từ mới, và câu nói quá (xem Phần 2).
- Đề xuất: «Vì vậy chênh lệch giữa các cấu hình không đến từ các giới hạn tính toán này.»

**B73 ★ (dòng 404–406).**
- Câu gốc: «Phần đầu của tiêu chí 3 không phân biệt phương án: … mức dùng trần lớn nhất đều bằng 100\%. Lý do là đổi xe, đổi điểm đón và đổi điểm trả có trần 0, nên tiêu chí 3 chỉ tác dụng qua tổng phần dời theo từng chiều.»
- Vì sao:
  - người đọc chưa biết tiêu chí 3 gồm hai phần, nên không theo được đoạn này;
  - "chiều" đứng một mình dễ hiểu là phương hướng;
  - 3.503 lượt chênh hẳn 1.714 lượt ở mục 4.6, mà không nói đây là tập khác.
- Đề xuất: «Tiêu chí 3 so hai thứ theo thứ tự: mức dùng trần lớn nhất, rồi tổng phần dời theo từng chiều cam kết. Trên tập kiểm tra chính, thứ thứ nhất không phân biệt được phương án nào: ở mọi lượt có ghi tiêu chí này (3.503 lượt khi không trần, 3.506 với trần 30 giây, 3.504 với trần 120 giây), mức dùng trần lớn nhất đều là 100\%. Lý do là các chiều đổi xe, đổi điểm đón và đổi điểm trả có trần bằng 0. Trên thực tế, tiêu chí 3 chỉ có tác dụng qua tổng phần dời.»
- Ghi chú: tác giả kiểm lại cách tính mức dùng khi trần bằng 0. Đoạn này nên chuyển lên mục 4.6.

**B74 (dòng 409–410).**
- Câu gốc: «…giống từng byte giữa hai tập kiểm tra chính và tắc đường cố định. Hai tập khác nhau ở thiết lập bộ chạy, như luật phục hồi và phiên bản chính sách.»
- Vì sao:
  - câu sau có vẻ mâu thuẫn câu trước: tệp giống hệt nhau mà "phiên bản chính sách" lại khác;
  - thiếu chữ "tập" trước "tắc đường cố định";
  - không nói vì sao phép kiểm này quan trọng.
- Đề xuất: «Tệp mô tả luật cam kết của điều phối không trần và của luật C trần 30, 120 giây giống hệt nhau đến từng byte ở tập kiểm tra chính và tập tắc đường cố định, nên hai tập dùng cùng các luật. Hai tập chỉ khác nhau ở thiết lập của bộ chạy, như có hay không luật phục hồi.» [Nếu "phiên bản chính sách" là một thiết lập riêng của bộ chạy thì đặt tên khác.]

**B75 (dòng 413–414).**
- Câu gốc: «Các số của tập kiểm tra chính được ít nhất hai bộ đọc viết độc lập tính lại từ bản ghi thô và khớp trong phạm vi đã kiểm.»
- Vì sao: "bộ đọc" chưa được định nghĩa, câu bị động dài, và "trong phạm vi đã kiểm" mơ hồ.
- Đề xuất: «Các số của tập kiểm tra chính được tính lại từ bản ghi thô bằng ít nhất hai chương trình đọc dữ liệu viết riêng [ai viết], và hai bên khớp nhau ở mọi số đã so.»

**B76 ★ (dòng 415–417).**
- Câu gốc: «Khi chạy lại ngày 12/10/2026 … với kiểu xuống dòng LF … Kiểm thử còn lại đòi cây làm việc có tệp chưa được ghi nhận…»
- Vì sao: đây là lịch sử thao tác cùng thuật ngữ git, trái quy tắc 13. Người ngoài ngành không hiểu.
- Đề xuất: «Bộ kiểm thử tự động chạy trên đúng mã nguồn đã dựng bộ chạy cho 1.024 trong 1.025 kiểm thử đạt; kiểm thử còn lại cần một điều kiện riêng của kho mã và đạt khi chạy riêng trong điều kiện đó (Phụ lục~\ref{phuluc:C}).» Ngày chạy và kiểu xuống dòng chuyển vào phụ lục.

### Mục 4.11: Thảo luận và hạn chế

**B77 (dòng 428).**
- Câu gốc: «…là một bảng các điểm đánh đổi…»
- Đề xuất: «…là các điểm trên một đường đánh đổi để hãng xe tự chọn, không phải một khuyến nghị.»

**B78 (dòng 429).**
- Câu gốc: «…mất 96 lượt phục vụ và 242 khách đi chung.»
- Vì sao: "mất khách đi chung" đọc như khách bỏ đi.
- Đề xuất: «…phục vụ ít hơn 96 lượt và có ít hơn 242 khách đi chung.»

**B79 (dòng 434).**
- Câu gốc: «Một phép tính giả định cho thấy cách đọc bảng này.»
- Vì sao: dịch máy, và "bảng này" không rõ là bảng nào.
- Đề xuất: «Có thể đọc các điểm đánh đổi này bằng một phép tính hòa vốn giả định.»

**B80 (dòng 435–436).**
- Vì sao: câu dài khoảng 40 tiếng, lồng ba điều kiện.
- Đề xuất: «Luật C phục vụ ít hơn 96 lượt và có ít hơn 127 lượt trễ. Nếu bỏ qua mọi yếu tố khác, theo phép tính này luật C chỉ có lợi hơn khi $k > 0{,}756\,m$, tức $k/m > 96/127$.»

**B81 (dòng 437–438).**
- Câu gốc: «…mỗi lần ghép thêm chạm tới nhiều khách hơn…»
- Đề xuất: «…mỗi lần ghép thêm ảnh hưởng tới nhiều khách trên xe hơn, nên trần có thể chặn nhiều phương án hơn và làm mất nhiều lượt phục vụ hơn.» Chuyển câu này sang gạch đầu dòng "Tải thấp".

**B82 (dòng 446–447).**
- Câu gốc: «Thế giới vì vậy gần như tất định, và mức trễ còn lại sau dự báo không chuyển sang mạng có tắc đường riêng trên từng đoạn đường.»
- Vì sao: "thế giới" đã bị loại; "không chuyển sang" nghe như dịch máy.
- Đề xuất: «Vì vậy mô phỏng gần như không có yếu tố ngẫu nhiên, và mức trễ còn lại sau dự báo (0,17\% ở mục~\ref{muc:c4-dubao}) không dùng được cho một mạng đường mà mỗi đoạn có mức tắc riêng.»

**B83 (dòng 449).**
- Câu gốc: «đồ thị là bao đóng 96 nút»
- Vì sao: "bao đóng" là thuật ngữ toán chưa giải thích; phần A gọi là "đồ thị rút gọn".
- Đề xuất: «đồ thị là đồ thị rút gọn 96 nút, mỗi cặp nút có sẵn một thời gian đi, không phải mạng đường phố».

**B84 (dòng 463–464).**
- Câu gốc: «…ngắn hơn tập đủ điều kiện (trung vị đi thẳng 165 so với 196 giây)»
- Đề xuất: «…ngắn hơn mọi chuyến đủ điều kiện chọn (trung vị thời gian đi thẳng 165 so với 196 giây)».

**B85 (dòng 470).**
- Câu gốc: «…còn phép kiểm khả thi vẫn dùng giờ không dự báo…»
- Vì sao: "phép kiểm khả thi" chưa được định nghĩa.
- Đề xuất: «…còn bộ điều phối vẫn kiểm giờ đón bằng giờ không dự báo…»

**B86 (dòng 479).**
- Câu gốc: «…chưa được chạy trên quỹ đạo…»
- Đề xuất: «…chưa được chạy thành lần mô phỏng đầy đủ…»

**B87 (dòng 480–481).**
- Câu gốc: «…vế cộng dồn…»
- Vì sao: phần A gọi là "phần cộng dồn".
- Đề xuất: «…phần cộng dồn…»

**B88 (dòng 482–483).**
- Câu gốc: «Luật hạn chót chỉ là phần hạn chót…»; «hạn chót nới kiểu Hörl và Zwick»
- Vì sao: câu đầu nghe như lặp; cụm sau chưa được giải thích trong chương.
- Đề xuất: «Luật hạn chót ở đây chỉ mượn phần hạn chót của Schulz và Pfeiffer~\cite{schulz2026}, ở mức 30–60 giây thay vì 900 giây của họ; cách nới hạn chót của Hörl và Zwick~\cite{horl2022} [dẫn mục ở Chương 2] chưa được chạy.»

### Năm câu tóm tắt điều tôi học được

1. Khi tính lại trên các lượt đã ghi của tập tắc đường cố định, bỏ tiêu chí ổn định làm lựa chọn đổi ở 26\% lượt nếu không có trần, nhưng chỉ ở 6\% lượt với trần 30 giây. Phép chạy đầy đủ với bộ chọn ưu tiên chi phí chưa được làm, nên chưa biết đánh đổi của luật C có còn hay không.
2. Cộng sẵn mức tắc đường thường gặp vào lời hứa đầu giúp luật C giảm số khách trễ quá một phút ở 21 kịch bản ngày thường từ 68 xuống 2 trong 1.471 khách, và lời hứa chỉ dài thêm khoảng 13,7 giây. Tuy vậy, một cách đệm tỉ lệ có cùng độ dài cho kết quả chưa phân biệt được, và mô phỏng gần như không có yếu tố ngẫu nhiên.
3. Cộng 30 giây vào mọi lời hứa của điều phối không trần cho cùng 2.328 lượt không trễ quá một phút như luật C. Đổi lại, lời hứa dài gấp năm, nhiều khách tới sớm hơn (44 so với 4), và vẫn còn 68 khách trễ quá hai phút cùng 174 khách bị điều phối dời giờ trả. Luật C giữ phần dời này dưới 30 giây cho mọi khách, nhưng phục vụ ít hơn 96 lượt.
4. Ở chiều tuyết 15/11/2018, dự báo lịch sử chỉ bớt được 7 trong 41 khách trễ. Dùng thêm dữ liệu cùng ngày giúp được phần nào, nhưng con số tốt nhất lại dùng dữ liệu không được phép, và khoảng hai phần ba số giây trễ vẫn chưa được giải thích.
5. Các phép kiểm cho thấy cài đặt giữ đúng trần, giới hạn tính toán không làm mất phương án, và số liệu được tính lại độc lập. Nhưng mọi kết quả chỉ là thăm dò trên một mô phỏng tải thấp, mỗi kịch bản chạy một lần, và giá trị của chúng với khách hay hãng xe chưa được đo.

### Những điều tôi không tự tìm ra được

**Mục 4.6**
- 62.837 "lựa chọn" là gì: của một xe hay một lượt, của hai hay năm cấu hình.
- Vì sao bảng có ba cách tính chi phí, và nên tin cách nào. "Tính lặp qua các lượt" nghĩa là gì.
- Vì sao số yêu cầu được nhận không đổi. Đây là kết quả đo được, hay là hệ quả của thứ tự tiêu chí?

**Mục 4.7**
- "Đệm cùng giá" lấy tỉ lệ trên ngày nào. Vì sao tỉ lệ tới sớm của nó "chưa đo".
- 8 "cụm" là những cụm nào.
- Một hay nhiều "ngày nguồn".
- Vì sao "đưa dự báo vào bộ điều phối" tính trên 15 kịch bản chứ không phải 16. "Lớp lời hứa" là gì.
- Mô hình học máy được thử trên ngày nào và bao nhiêu khách khi dùng luật C. Câu về đối chứng "cùng độ dài thêm trung bình 30 giây" nghĩa là gì.

**Mục 4.8**
- Trên 2.207 khách được cả hai bên phục vụ, cách đệm và luật C khác nhau thế nào về số khách trễ quá hai phút. Mục chỉ so hai nhóm khác nhau.

**Mục 4.9**
- "Không được giao cho khung này" và "mức hiện tại vẫn lấy đúng" nghĩa là gì.
- "Quy tắc có ngưỡng" nằm ở đâu, vì bảng không có hàng nào như vậy.

**Mục 4.10**
- "Giới hạn khối lượng khám phá" là gì. "Gói cam kết" là gì.
- Tệp chính sách giống hệt nhau đến từng byte mà vẫn khác "phiên bản chính sách" là thế nào.
- Ai viết hai "bộ đọc", và chúng độc lập đến mức nào.
- Mục 4.11 nói bộ chạy dựng lại có thể khác bản lưu trữ. Vậy kiểm thử chạy trên mã dựng lại chứng minh được gì cho bản đã sinh ra số liệu?

**Mục 4.11**
- Thời gian dừng 0 giây và đồ thị "bao đóng" làm lệch kết luận nào, và lệch theo chiều nào.
- Mức 120 giây được chọn sau khi xem dữ liệu phát triển (mục 4.11) hay sau khi xem chính tập kiểm tra chính (phần A, dòng 230–231)?

### Câu hỏi về cách đệm: vì sao cần luật C nếu cộng 30 giây vào mọi lời hứa cho số khách đúng giờ gần bằng?

Đọc xong mục 4.8, tôi trả lời được trong một câu:

> **Cộng 30 giây chỉ làm lời hứa dài ra để che độ trễ khi đếm gộp, chứ không ngăn bộ điều phối dời giờ trả của từng khách khi ghép thêm người: với đệm 30 giây vẫn có 174 khách bị dời, một người gần 10 phút, và 68 khách trễ quá hai phút. Luật C giữ phần dời này dưới 30 giây cho mọi khách, kể cả khi không có dự báo, với lời hứa ngắn gấp năm lần; cái giá là ít hơn 96 lượt phục vụ.**

Tôi phải tự ghép câu này từ bốn ý "Thứ nhất…Thứ tư" (dòng 266–316) và đoạn cuối mục. Mục chưa có câu nào nói thẳng như vậy, và đoạn cuối lại kết bằng "đây là lựa chọn của hãng xe". Vì vậy đây là thay đổi bắt buộc M1.

---

## Phần 2. Giảng viên chấm (UET, CNTT)

### 2.1. Bảng và hình: so gì, trên lần chạy nào, kết luận gì

**Bảng sàng lọc (`bang:c4-sangloc`, dòng 28–56)**
- So gì: U với C-30 khi bỏ tiêu chí 3.
- Lần chạy: tập tắc đường cố định, 16 kịch bản, bộ chạy cũ.
- Kết luận: chỉ đọc một ô (7,79\%). Câu kết luận nằm ở dòng 65 ("chỉ gợi ý…").
- Thiếu:
  - Đoạn văn không nói khối chi phí nghĩa là gì cho câu hỏi chính. Tính trên toàn bộ chi phí, phần giảm chỉ là 0,31\% và 0,08\%, nhưng câu đọc bảng chỉ nêu con số lớn nhất.
  - C-60 và C-120 có trong lời văn nhưng không có trong bảng.
  - Chú thích không định nghĩa U và C-30.
  - Hai ô có bốn chữ số thập phân.
  - Bộ chạy cũ của tập này "có giới hạn bộ sinh và bộ giải chưa được kiểm lại" (phần A, dòng 74–75). Mục 4.6 không nhắc điều đó.

**Bảng dự báo (`bang:c4-dubao`, dòng 90–111)**
- So gì: ba cách hứa của C-30.
- Lần chạy: 21 kịch bản ngày thường, cùng 1.471 khách. Đây là phép so trên cùng một nhóm khách, rất tốt.
- Kết luận: có đoạn về khoảng tin cậy.
- Thiếu:
  - Chỉ có trung bình theo kịch bản. Không có số đếm cho cột đệm (quy tắc 24).
  - Tỉ lệ tới sớm của cột đệm ghi "chưa đo", trong khi quy tắc 31 đòi luôn báo trễ kèm tới sớm. Đây là phép so then chốt "dự báo hay chỉ là đệm?", mà một vế còn thiếu.
  - Việc 34 trong 1.471 khách được báo giờ đón muộn hơn giờ đón muộn nhất chỉ được nêu ở mục 4.11, không đặt cạnh kết quả.

**Hình sổ (`hinh:c4-so`, dòng 144–181)**
- So gì: ba phần của số giây trễ.
- Lần chạy: 68 khách ngày thường và 41 khách chiều tuyết.
- Đánh giá:
  - Chú thích tự đủ nghĩa, in đen trắng vẫn đọc được, và có câu "không phải phần không thể biết trước". Tốt.
  - Lời văn diễn giải bằng chữ "ngược lại" thay vì dẫn số.
  - Nhãn của thanh chiều tuyết không có phần trăm cho 8,6 giây (0,25\%).

**Bảng đệm (`bang:c4-dem`, dòng 229–260)**
- So gì: các cách hứa có dự báo, chia ba khối theo độ dài thêm.
- Lần chạy: tập kiểm tra chính, số đếm gộp.
- Thiếu:
  - Chú thích không có câu cảnh báo "hai nhóm khách khác nhau, không ghép cặp". Câu này chỉ có ở dòng 224–225.
  - Không định nghĩa U, C-30, C-120.
  - Dòng 318 so với "luật hạn chót 30 giây có dự báo", nhưng số của cấu hình này không có trong bảng nào.

**Bảng hai phía (`bang:c4-haiphia`, dòng 277–301)**
- Lần chạy: cùng các lần chạy với Bảng đệm.
- Đánh giá:
  - Chú thích ghi đủ mẫu số. Mọi hàng cộng khớp số khách phục vụ.
  - Kết luận rải ra ở "Thứ hai" và "Thứ ba".
  - Không có cột "trễ quá 60 s", nên người đọc phải nhìn sang Bảng đệm.

**Bảng tuyết (`bang:c4-tuyet`, dòng 354–376)**
- So gì: bảy cách hứa.
- Lần chạy: 8 kịch bản, 601 khách, trên ngày đã xem. Đây là phép so trên cùng một nhóm khách.
- Thiếu:
  - Trong cùng một bảng, cột trễ là số gộp, còn cột dài thêm là trung bình theo kịch bản. Hai cách gộp trộn lẫn.
  - Không có cột tới sớm (quy tắc 31).
  - Hàng dùng dữ liệu không được phép ("trộn có buổi sáng") không được đánh dấu trong bảng.
  - "Đệm cùng giá" được chỉnh trên chính ngày tuyết.
  - "Quy tắc có ngưỡng" (dòng 351) không có trong bảng.

**Nhận xét chung:** mọi bảng đều có câu "Cách đọc bảng" như DACN. Tuy vậy, câu đọc bảng chỉ đọc một ô, không nói *nên kết luận gì*. DACN (tr. 31) viết "Nói cách khác, …", và phần B nên thêm câu như vậy cho Bảng sàng lọc, Bảng dự báo và Bảng tuyết.

### 2.2. Các phép kiểm ở mục 4.10 có thuyết phục không?

Thuyết phục một phần.

**Điểm mạnh**
- Số liệu được tính lại từ bản ghi thô và khớp đến từng khách (7.159 khách).
- Các giới hạn tính toán được kiểm trên đúng tập chính, và giới hạn 2 yêu cầu chỉ phải dời một yêu cầu.
- Tệp luật của hai tập giống hệt nhau.
- Câu cuối mục nói thẳng rằng các phép kiểm không cho biết mô phỏng giống thực tế đến đâu.

**Điểm yếu**
1. Câu "không khách nào vượt trần, 0 quyết định bị ép" (dòng 392–394) được trình bày như một phép kiểm kết quả. Thật ra phần A (dòng 327–329) đã nói đây là điều Nhận xét cho trước dưới giả thiết (N). Ở mục 4.10, phải gọi đúng tên: đây là phép kiểm cài đặt.
2. Phép sàng lọc ở mục 4.6 và các số của chiều tuyết chạy trên những bộ chạy *chưa được kiểm lại* (phần A, dòng 74–75 và 134–135). Mục 4.10 không có phép kiểm nào cho hai bộ chạy này, và cũng không nói điều đó ngay trong mục.
3. Mục 4.10 không kiểm phép phát lại dự báo, phép đệm, hay đường đi của mô hình học máy. Đây lại là các con số của mục 4.7–4.9.
4. Kiểm thử tự động chạy trên mã dựng lại, nhưng dòng 472 nói bộ chạy dựng lại "có thể khác bản lưu trữ". Vậy kiểm thử không chứng minh rằng bản đã sinh ra số liệu là đúng. Hai câu này cần được nối với nhau.
5. "Hai bộ đọc viết độc lập": phải nói ai viết, và độc lập ở mức nào. Bảng thuật ngữ, mục F, dòng 116 dặn mô tả trung thực ai hoặc công cụ nào đã kiểm.
6. Không có phép kiểm độ nhạy theo hạt giống của bộ giải. Phần A ghi hạt giống cố định bằng 7, và mỗi kịch bản chạy một lần.
7. Đoạn về tiêu chí 3 (dòng 404–406) là một phát hiện về bộ chọn, không phải phép kiểm. Đoạn này quan trọng cho mục 4.6: "ưu tiên ổn định" trên thực tế chỉ còn là "ưu tiên tổng phần dời". Nên chuyển lên mục 4.6.

### 2.3. Hạn chế ở mục 4.11: có đủ "chưa làm → kết luận nào bị ảnh hưởng" không?

| Gạch đầu dòng | Chưa làm | Kết luận bị ảnh hưởng | Đánh giá |
|---|---|---|---|
| FleetPy (dòng 445) | không thử ngoài đời | mọi kết quả | đủ, nhưng chung chung |
| Hệ số chung cả thành phố (dòng 446–447) | chưa thử tắc đường theo từng đoạn | mức trễ sau dự báo | đủ; nên nêu rõ số 0,17\% |
| Dừng đón trả 0 giây, đồ thị 96 nút (dòng 448–450) | chưa chạy với 30 giây | "Độ dài chuyến và độ lệch giờ trả chưa tính các yếu tố này" | **thiếu**: không nói kết luận nào (phần dời do điều phối, cái giá 96 lượt) chỉ đúng với dừng 0 giây |
| Không có phản ứng của khách, không gán lại xe (dòng 451–452) | có | số lượt phục vụ, cái giá của trần | đủ |
| 34 kịch bản phụ thuộc nhau (dòng 458–459) | có | các phép đếm theo kịch bản | đủ. Nhưng mục 4.7 lại tính khoảng tin cậy t trên 8 nhóm; cần một câu nói khoảng tin cậy này cũng chỉ là mô tả |
| Chọn sau khi xem dữ liệu (dòng 460–461) | có | "mọi kết quả là thăm dò" | **sai so với phần A**: phần A (dòng 230–231) nói mức 120 giây được chọn sau khi xem *chính tập kiểm tra chính*; mục 4.11 lại viết "dữ liệu phát triển". Bản 4.11 nói nhẹ đi |
| Tải thấp (dòng 462–464) | có | tải cao, chuyến dài | đủ |
| Giờ đón hiển thị không khả thi (dòng 470–471) | chưa sửa | **thiếu**: không nói các số có dự báo ở mục 4.7–4.8 bị ảnh hưởng | |
| Bộ chạy dựng lại, chiều tuyết (dòng 472–473) | có | số chiều tuyết, việc tái lập | đủ |
| Bộ chọn ưu tiên chi phí, luật mỗi lần một trần (dòng 479–481) | có | có | đủ |
| Luật hạn chót (dòng 482–484) | có | có | đủ |
| Mức 30 giây (dòng 485–486) | có | có | đủ |

**Còn thiếu hẳn**
- Đệm cùng độ dài chưa được đo tỉ lệ tới sớm, và đã được chỉnh trên chính các ngày thử. Kết luận bị ảnh hưởng: lợi thế của dự báo so với đệm.
- Mọi dự báo đều dựng từ dữ liệu có ngày 12/11. Kết luận bị ảnh hưởng: tính tổng quát của mức 0,17\%.
- Các phép so U với C đều trên hai nhóm khách khác nhau, chưa có phép so trên 2.207 khách chung.
- Ngưỡng của bốn điều kiện học máy (1 giây, 15 giây, 1 điểm phần trăm) được chọn khi nào và dựa vào đâu.

**Đánh giá chung:** phần hạn chế trung thực và cụ thể hơn nhiều so với bản hiện tại của khóa luận. Có ba gạch đầu dòng thiếu vế "kết luận nào bị ảnh hưởng", và có một chỗ lệch với phần A.

### 2.4. Mục 4.6 có nói rõ phép thử thứ tự bộ chọn chưa được chạy không?

Có nói, nhưng muộn.
- Câu "chưa được chạy" chỉ xuất hiện ở đoạn cuối (dòng 69), sau hai đoạn và một bảng.
- Tên mục ("Vai trò của trần và…") và đoạn mở ("Bằng chứng hiện có là…") làm người đọc nghĩ đã có kết quả.
- Mục 4.11 (dòng 479) và Chương kết luận có nhắc lại. Tốt.

Cần đưa "chưa được chạy" lên đoạn đầu, và định nghĩa "phép sàng lọc" để không ai nhầm nó với phép thử (thay đổi M4).

### 2.5. Chỗ nói quá

| Dòng | Câu | Vấn đề | Sửa |
|---|---|---|---|
| 400–401 | «…phản ánh tác động của cả gói cam kết» | Động từ nhân quả. Loại trừ được giới hạn tính toán không biến chênh lệch thành "tác động" của luật, vì hai nhóm khách khác nhau và các quyết định phụ thuộc nhau theo đường đi | M3 |
| 392–394 | «không khách nào vượt trần… không có lượt … phải phục hồi» | Trình bày như phép kiểm kết quả, trong khi đây là hệ quả của cách xây dựng luật (phần A, dòng 327–329) | M3 |
| 330–331 | «luật C cho điều đó» | Đọc như một bảo đảm về giờ trả thực tế. Thật ra luật C giới hạn phần dời trên giờ trả dự kiến của mô hình; phần A, dòng 330 nói "nhận xét không bảo đảm giờ trả thực tế" | thêm «theo cách xây dựng luật» (B57) |
| 314–315 | «…kể cả … ở chiều tuyết» | Bộ chạy chiều tuyết chưa được kiểm lại; câu không mang lưu ý đó | thêm «(bộ chạy chưa kiểm lại)» |
| 119 | «Lợi thế so với cách đệm này vì vậy còn mong manh» | Khoảng tin cậy chứa 0 thì chưa có lợi thế nào được xác lập | M5 |
| 139–140, 345, 383 | «được hồ sơ lịch sử giải thích», «giải thích thêm» | Ranh giới với quy tắc 33 (động từ nhân quả cho phép tách sổ). Chú thích hình đã rào đúng; trong thân bài nên viết «theo sổ, … thuộc phần hồ sơ lịch sử» | S1 |
| 435–436 | «luật C chỉ có lợi hơn … khi $k > 0{,}756\,m$» | Giá trị kinh doanh. Đã có rào ("giả định", "không có giá trị thật"), nhưng phép tính bỏ qua tới sớm, độ dài lời hứa và khách đi chung. Nên thêm «theo phép tính này» và nêu các yếu tố bị bỏ qua | B80 |
| 62 | «Số yêu cầu được nhận không đổi ở lượt nào» | Viết như một phát hiện. Nếu tiêu chí "số yêu cầu được nhận" đứng trước tiêu chí 3, đây là hệ quả của thứ tự tiêu chí | thêm một mệnh đề giải thích |

**Không thấy:** "tối ưu", "duy nhất", "đầu tiên", "vượt trội", hay khẳng định về sự hài lòng của khách. Các câu "không đo giá trị" (dòng 332, 431, 485–486) đúng chỗ.

### 2.6. So hai nhóm khách khác nhau như thể cùng một nhóm

| Dòng | Câu | Nhận xét |
|---|---|---|
| 218–219 | «cũng cho 2.328 … bằng luật C» | Câu mở mục nói "bằng", còn lời cảnh báo "không ghép cặp" đến sau một đoạn. Nên đưa cảnh báo vào cùng đoạn và vào chú thích bảng |
| 308–310 | «68 khách vẫn trễ quá hai phút … luật C không có khách nào» | Hai nhóm khác nhau: trong 68 khách có thể có khách mà luật C không phục vụ. Cần phép so trên 2.207 khách chung, hoặc một câu nhắc |
| 266–270 | «luật C hơn … kém …» | Hai nhóm khác nhau, không nhắc |
| 429–430 | «số lượt trễ thấp hơn ở cả bốn ngưỡng» | Số trên 100 yêu cầu (phần A) giúp so trên cùng mẫu số, nhưng tập khách vẫn khác. Nên thêm «trên hai nhóm khách khác nhau» |
| 188–189 | luật hạn chót 47,6\% so với 62,8\% | Hai đường chạy khác nhau trên 15 kịch bản. Chấp nhận được, nhưng nên nói đây là hai lần chạy khác nhau |
| 323–325 | C-120 so với đệm 30 giây | Đã có "trên một tập khách khác". Tốt |
| 62–65 | tỉ lệ đổi lựa chọn giữa các mức trần | Đã có câu cảnh báo. Tốt |
| Bảng dự báo, Bảng tuyết | — | Đây là phép so trên cùng một nhóm khách; nên nói rõ "cùng 1.471 khách", "cùng 601 khách" như một điểm mạnh |

### 2.7. Thuật ngữ không thống nhất giữa phần B, phần A và Chương 3

| Phần B (dòng) | Phần A, Chương 3, Bảng thuật ngữ | Đề xuất |
|---|---|---|
| "phải phục hồi" (188, 189, 319, 393) | "bị ép", "quyết định bị ép" (phần A, Bảng chỉ số; Bảng nghĩa vụ; Bảng thuật ngữ E) | "bị ép" |
| "thứ tự ưu tiên chọn phương án", "thứ tự ưu tiên của bộ chọn" (14, 69) | "thứ tự tiêu chí" (Chương 3 dòng 53; phần A, bảng lộ trình) | "thứ tự tiêu chí" |
| "đệm" theo tỉ lệ ("đệm cùng giá", 86) | "đệm" là cộng một khoảng cố định (phần A, dòng 15–16; Bảng thuật ngữ B) | đổi tên thành "đệm cùng độ dài" và nói rõ đây là đệm theo tỉ lệ |
| "đệm đều" (197, 211) và "cách đệm" (4.8) | "đệm đều" (Bảng thuật ngữ) | giữ, nhưng 4.8 nên viết "đệm đều 30 giây" ở lần đầu |
| "thế giới … tất định" (134, 446) | Bảng thuật ngữ mục G loại "thế giới". Phần A dòng 66 cũng dùng "Thế giới mô phỏng", nên cả hai phần cùng phải sửa | "mô phỏng gần như không có yếu tố ngẫu nhiên" |
| "bao đóng 96 nút" (449) | "đồ thị rút gọn" (phần A, Bảng tham số) | "đồ thị rút gọn" |
| "vế cộng dồn" (480) | "phần cộng dồn" (phần A, mục 4.5) | "phần cộng dồn" |
| "lời hứa trả", "lời hứa đón" (130) | "lời hứa giờ trả", "lời hứa giờ đón" | dùng tên đầy đủ |
| "dự báo lịch sử" (339), "dự báo theo giờ trong ngày" (136), "mô hình có dữ liệu buổi sáng" (383) | "lời hứa theo dự báo", "hồ sơ tắc đường lịch sử" | hai tên này, cộng với tên hàng trong bảng |
| "độ tin cậy" (71) | "đúng giờ", "không trễ quá" (phần A) | "số lượt đúng giờ" |
| "quỹ đạo" (71, 479) | phần A cũng dùng (dòng 745, 756) mà không định nghĩa | định nghĩa một lần ("cả lần chạy, trong đó mỗi quyết định ảnh hưởng tới các lượt sau") hoặc bỏ |
| "phép sàng lọc" (23, 69) | phần A dòng 231 cũng dùng mà không định nghĩa | định nghĩa ở mục 4.6 |
| "ngày nguồn" (120) và "các ngày nguồn" (368) | — | một định nghĩa, một dạng số |
| "phép kiểm khả thi" (470) | "điều kiện kiểm tra lúc đón" (Bảng thuật ngữ E), "bộ kiểm" (phần A) | "bộ điều phối vẫn kiểm giờ đón…" |
| "gói cam kết" (400), "giới hạn khối lượng khám phá" (398), "bộ đọc" (413), "tập đủ điều kiện" (463) | không có ở đâu | bỏ hoặc định nghĩa |
| "chi phí kế hoạch" (19, 32) | phần A dòng 762 thống nhất; Bảng thuật ngữ E ghi "chi phí vận hành" cho bộ chọn ưu tiên chi phí | giữ "chi phí kế hoạch" (phần B nói rõ không phải chi phí vận hành); cần đối chiếu tên tiêu chí 4 trong Bảng ràng buộc của Chương 3 (sau dòng 120, chưa đọc) |
| "34 kịch bản chính" (69) | "tập kiểm tra chính" | "34 kịch bản của tập kiểm tra chính" |
| "sổ" (139, 345, 383) | "sổ theo từng khách" (Chương 3 dòng 24; phần A) | giữ; Bảng thuật ngữ ghi "sổ cái" là bản cũ |

### 2.8. Mười câu tôi sẽ hỏi khi bảo vệ

1. **Vì sao chưa chạy phép thử bộ chọn ưu tiên chi phí trên 34 kịch bản, và phép sàng lọc trả lời được bao nhiêu phần của câu hỏi chính?**
   *Trả lời một phần.* Văn bản nói chưa chạy (dòng 69) và nói phép sàng lọc không cho biết kết quả trên cả lần chạy (dòng 70), nhưng không nói vì sao chưa chạy.
2. **Số yêu cầu được nhận không đổi khi bỏ tiêu chí 3 là kết quả đo được, hay là hệ quả của việc tiêu chí "số yêu cầu được nhận" đứng trước tiêu chí 3?**
   *Chưa trả lời.*
3. **Trên 2.207 khách được cả cách đệm 30 giây và luật C phục vụ, mỗi bên có bao nhiêu khách trễ quá một phút, quá hai phút và tới sớm?**
   *Chưa trả lời.* Mục 4.8 chỉ so hai nhóm khác nhau (dòng 224–225).
4. **Tỉ lệ của "đệm cùng giá" được chỉnh trên ngày nào? Tỉ lệ tới sớm của nó là bao nhiêu? Nếu dự báo không hơn đệm, dự báo đóng góp gì?**
   *Trả lời một phần.* Có nói khoảng tin cậy chứa 0 (dòng 118–119); tỉ lệ tới sớm "chưa đo"; ngày chỉnh không được nói.
5. **Khoảng tin cậy t trên 8 nhóm có hợp lệ không, khi các nhóm dùng chung ngày nguồn 12/11 và mục 4.11 nói các phép đếm "không phải kiểm định"?**
   *Trả lời một phần* (dòng 117–120, 458–459). Hai chỗ chưa được nối với nhau.
6. **34 trong 1.471 khách được báo giờ đón muộn hơn giờ đón muộn nhất. Nếu sửa phép kiểm giờ đón, các số 0,17\% và 2.328 còn giữ được không?**
   *Chưa trả lời.* Hạn chế được nêu ở dòng 470–471 nhưng không nói ảnh hưởng.
7. **Mức 120 giây được chọn khi nào? Mục 4.11 nói sau khi xem dữ liệu phát triển, phần A nói sau khi xem chính tập kiểm tra chính.**
   *Trả lời mâu thuẫn nhau* (dòng 460 so với phần A dòng 230–231).
8. **Ai viết hai bộ đọc "độc lập"? Kiểm thử trên mã dựng lại chứng minh được gì cho bản bộ chạy đã sinh ra số liệu, khi dòng 472 nói hai bản có thể khác nhau?**
   *Trả lời một phần* (dòng 413–417, 472).
9. **Với thời gian dừng 30 giây và tải khoảng 1,33 khách mỗi xe như nghiên cứu điển hình của FleetPy, cái giá 96 lượt của luật C sẽ thay đổi thế nào? Đã chạy thử nhỏ chưa?**
   *Trả lời một phần.* Chỉ có giả thuyết chưa kiểm (dòng 437–438) và hạn chế (dòng 448–450, 462–464); không có số liệu.
10. **Nếu đệm cho cùng số lượt đúng giờ, và luật hạn chót có cùng số lượt phục vụ lẫn số lượt không trễ, thì luật C cho hành khách điều gì mà họ cảm nhận được, và có bằng chứng nào cho thấy điều đó đáng 96 lượt phục vụ?**
    *Trả lời một phần.*
    - Phần có trả lời: luật C giới hạn phần dời do điều phối của từng khách (dòng 313–315) và giữ được lời hứa của chính nó (dòng 318–320).
    - Phần chưa có: văn bản tự nhận không có bằng chứng về giá trị (dòng 332, 431, 485–486). Câu trả lời trung thực sẵn có, nhưng hội đồng sẽ hỏi tiếp về giá trị.

**Có thể hỏi thêm:** ngưỡng 1 giây, 15 giây và 1 điểm phần trăm của mô hình học máy được chọn khi nào? Vì sao 3 lần chạy dừng do lệch 1,67 hoặc 2,69 giây không được xử lý bằng một khoảng dung sai, rồi mới kết luận bỏ cách đưa dự báo vào bộ điều phối?

---

## Danh sách thay đổi theo thứ tự ưu tiên

### Bắt buộc (5)

**M1. Mục 4.8: trả lời ngay câu "vì sao cần luật C nếu đệm cho số lượt đúng giờ bằng nhau".**

Chèn sau dòng 220, trước «Đệm 30 giây ở đây là…»:

> Hai cách cho hai thứ khác nhau. Đệm làm lời hứa dài ra nên bớt lượt trễ khi đếm gộp, nhưng không đổi quyết định điều phối: với đệm 30 giây vẫn có 174 khách bị điều phối dời giờ trả, một người tổng cộng 590,1 giây, và 68 khách trễ quá hai phút. Luật C giữ phần dời do điều phối của mọi khách dưới trần, lớn nhất 29,2 giây, kể cả khi không có dự báo, với lời hứa chỉ dài thêm 7,37 giây; đổi lại, nó phục vụ ít hơn 96 lượt.

Thêm hai chỗ sửa:
- Dòng 266: đổi nhãn «Vai trò của từng thành phần.» thành «Bốn điều đọc được từ hai bảng.»
- Cuối chú thích Bảng~\ref{bang:c4-dem}: thêm «Đệm không đổi quyết định điều phối, nên các dòng của U và của C là hai nhóm khách khác nhau (chung 2.207 khách).»

**M2. Mục 4.11, dòng 460–461: sửa chỗ lệch với phần A về mức 120 giây.**

Thay bằng:

> Ngưỡng phân tích và cách chia tập được chọn sau khi đã xem tập buổi sáng và các đợt chạy thử trước đó; mức 120 giây được chọn sau khi đã xem kết quả của điều phối không trần và luật C trần 30 giây trên chính tập kiểm tra chính (mục~\ref{muc:c4-thamdo}); chiều tuyết là sự kiện đã xem. Mọi kết quả vì vậy là thăm dò, và các số của trần 120 giây không phải phép thử trên dữ liệu chưa xem.

**M3. Mục 4.10: bỏ chỗ nói quá và gọi đúng tên phép kiểm cài đặt.**

Thay dòng 392–394 bằng:

> Trên 34 kịch bản của tập kiểm tra chính, cài đặt khớp với Nhận xét~\ref{nx:giunguyen}: không khách nào vượt trần, tổng dời do điều phối lớn nhất của một khách là 29,2 giây với trần 30 giây và 118,9 giây với trần 120 giây; không lượt quyết định nào bị ép, 0 trong 20.101 và 0 trong 20.435 lượt. Đây là phép kiểm cài đặt, không phải kết quả thực nghiệm: dưới giả thiết (N), Nhận xét đã cho trước các số 0 này.

Thay dòng 400–401 bằng:

> Vì vậy chênh lệch giữa các cấu hình không đến từ các giới hạn tính toán này.

**M4. Mục 4.6: nói "chưa chạy" ngay đầu mục, định nghĩa phép sàng lọc, và nêu kết luận của bảng.**

Thay dòng 17–25 bằng:

> Điều phối không trần và luật C trần 30 giây dùng cùng một bộ chọn, bộ chọn ưu tiên ổn định, và chỉ khác nhau ở trần giờ trả. Vì vậy chênh lệch giữa hai cấu hình ở các mục trước là chênh lệch khi thêm trần và giữ nguyên bộ chọn, trên hai nhóm khách không hoàn toàn trùng nhau. Câu hỏi còn mở: nếu bộ chọn bỏ tiêu chí ổn định (tiêu chí 3 ở Bảng~\ref{bang:rangbuoc}) để xét ngay chi phí kế hoạch (tiêu chí 4), thì đánh đổi giữa số lượt phục vụ và số lượt trễ có còn không? Phép thử trả lời câu hỏi này trên 34 kịch bản của tập kiểm tra chính chưa được chạy.
>
> Mục này chỉ có một phép tính lại nhanh, gọi là phép sàng lọc, trên tập tắc đường cố định (Bảng~\ref{bang:c4-sangloc}). Ở mỗi lượt quyết định đã ghi, bộ chọn được chạy lại trên đúng các phương án của lượt đó nhưng bỏ tiêu chí 3. Lựa chọn mới chỉ được ghi lại để so, không được đưa trở lại mô phỏng, nên các lượt sau vẫn đi theo lựa chọn cũ. Để kiểm tra cách chạy lại, bộ chọn với thứ tự tiêu chí gốc được chạy trước và cho lại đúng cả 62.837 lựa chọn đã ghi của năm cấu hình.

Hai chỗ sửa thêm:
- Sau câu đọc bảng (dòng 59), thêm: «Tính trên toàn bộ chi phí kế hoạch của mọi lượt, phần giảm chỉ là 0,31\% khi không trần và 0,08\% với trần 30 giây.»
- Thay dòng 69–72 bằng: «Vì phép sàng lọc chỉ xét từng lượt riêng lẻ, nó không cho biết số lượt phục vụ và số lượt đúng giờ khi cả lần chạy đi theo lựa chọn mới. Vì vậy chưa biết khoảng cách giữa điều phối không trần và luật C có giữ nguyên khi cả hai dùng bộ chọn ưu tiên chi phí hay không. Chương kết luận đặt phép thử này lên đầu các hướng phát triển.»

**M5. Mục 4.7: sửa cách nói về khoảng tin cậy và đặt lưu ý giờ đón cạnh kết quả.**

Thay dòng 117–120 bằng:

> Chênh lệch giữa có dự báo và không dự báo là −5,84 điểm phần trăm. Khi gom 21 kịch bản thành 8 nhóm theo ngày và khung giờ, mỗi nhóm là một quan sát, khoảng tin cậy 95\% theo phân phối Student là từ −10,54 đến −1,15 điểm phần trăm. Với có dự báo trừ đệm cùng giá, chênh lệch là −1,77 điểm phần trăm, khoảng tin cậy từ −3,62 đến +0,07, tức có chứa 0, nên chưa thể nói lời hứa theo dự báo tốt hơn cách đệm này. Toàn bộ mức giảm nằm ở khung 7 và 8 giờ của ba ngày 14–16/11, và ngày 12/11 là ngày nguồn của mọi dự báo.

Sau dòng 136, thêm:

> Lời hứa theo dự báo được tính sau khi chạy, còn bộ điều phối vẫn kiểm giờ đón bằng giờ không dự báo, nên với luật C trần 30 giây, 34 trong 1.471 khách được báo giờ đón muộn hơn giờ đón muộn nhất. Các con số có dự báo của mục này và mục~\ref{muc:c4-dem} chưa tính tới việc sửa chỗ chưa khớp này.

### Nên sửa (5)

**S1. Thống nhất thuật ngữ** (bảng ở mục 2.7). Các chỗ thay chính xác:
- "phải phục hồi" thành "bị ép", ở dòng 188 (B32), 188–189 (B33), 319 (B53) và 393 (B68).
- «Kết quả này dựa trên một thế giới gần như tất định.» thành «Mô phỏng ở đây gần như không có yếu tố ngẫu nhiên.»
- «Thế giới vì vậy gần như tất định» thành «Vì vậy mô phỏng gần như không có yếu tố ngẫu nhiên».
- «bao đóng 96 nút» thành «đồ thị rút gọn 96 nút».
- «vế cộng dồn» thành «phần cộng dồn».
- «lời hứa trả / lời hứa đón» thành «lời hứa giờ trả / lời hứa giờ đón».
- «thứ tự ưu tiên» thành «thứ tự tiêu chí».
- «dự báo lịch sử» thành «lời hứa theo dự báo».
- «được hồ sơ lịch sử giải thích» (thân bài) thành «theo sổ, thuộc phần hồ sơ lịch sử».
- Thêm «U: điều phối không trần; C-$B$: luật C trần $B$ giây» vào chú thích các Bảng sàng lọc, đệm và hai phía.

**S2. Đổi tên và định nghĩa lại "đệm cùng giá".**
- Thay dòng 85–87 bằng câu ở B19.
- Đổi "Đệm cùng giá" thành "Đệm cùng độ dài" ở tiêu đề cột Bảng dự báo, ở dòng 118 và ở hàng Bảng tuyết.
- Thêm vào chú thích Bảng dự báo: «Tỉ lệ của đệm cùng độ dài được chỉnh trên [các ngày …]; tỉ lệ tới sớm của nó chưa được đo.»

**S3. Mục 4.9: làm rõ hàng dùng dữ liệu không được phép.**
- Thay dòng 350–351 bằng câu ở B62, dòng 383–384 bằng câu ở B65 và B66, hai hàng của bảng bằng câu ở B63.
- Đánh dấu hàng "Trộn có buổi sáng" trong bảng bằng một chú thích: «dùng dữ liệu thiết kế thử không cho phép; chỉ để tham khảo».
- Đưa "quy tắc có ngưỡng" vào bảng, hoặc bỏ khỏi lời văn.

**S4. Mục 4.10: bỏ lịch sử thao tác, định nghĩa từ mới, chuyển đoạn tiêu chí 3.**
- Thay dòng 415–417 bằng câu ở B76; ngày chạy và kiểu xuống dòng chuyển vào phụ lục.
- Thay dòng 413–414 bằng câu ở B75, ghi rõ ai viết các chương trình đọc.
- Định nghĩa "giới hạn khối lượng khám phá" (B70).
- Sửa chỗ mâu thuẫn byte và phiên bản (B74).
- Chuyển đoạn dòng 404–406, viết lại như ở B73, lên mục 4.6, ngay sau Bảng sàng lọc.

**S5. Mục 4.11: điền vế "kết luận nào bị ảnh hưởng" và thêm hai hạn chế còn thiếu.**

Thay gạch đầu dòng ở dòng 448–450 bằng:

> Thời gian dừng đón, trả bằng 0 giây (kiểm trên 3 lần chạy mẫu), trong khi nghiên cứu điển hình của FleetPy dùng 30 giây mỗi khách~\cite{engelhardt2026}; đồ thị là đồ thị rút gọn 96 nút, không phải mạng đường phố. Với thời gian dừng 30 giây, mỗi lần ghép thêm khách có thể dời giờ trả của khách trên xe nhiều hơn, và trần có thể chặn nhiều phương án hơn. Điều này chưa được chạy, nên các số về phần dời do điều phối và cái giá 96 lượt phục vụ chỉ áp cho thời gian dừng 0 giây.

Thêm vào cuối gạch đầu dòng ở dòng 470–471:

> Các số có dự báo ở mục~\ref{muc:c4-dubao} và~\ref{muc:c4-dem} chưa tính tới việc sửa này.

Thêm vào nhóm "Dữ liệu và thiết kế thực nghiệm":

> Đệm cùng độ dài chưa được đo tỉ lệ tới sớm, và mọi hồ sơ dự báo đều dựng từ dữ liệu có ngày 12/11. Vì vậy lợi thế của lời hứa theo dự báo so với cách đệm này chưa được xác lập, và mức 0,17\% chưa được kiểm trên dự báo dựng từ ngày khác.
