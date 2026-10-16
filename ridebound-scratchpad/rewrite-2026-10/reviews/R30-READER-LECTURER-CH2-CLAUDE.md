# R30. Chương 2 (bản v4) dưới hai vai: người đọc ngoài ngành và giảng viên chấm

- **Tệp được đọc (chỉ đọc):** `drafts/06-chuong2-v4.tex` (266 dòng). Số dòng dưới đây là số dòng của tệp này.
- **Ngữ cảnh đã đọc:** `drafts/07-chuong3-v3.tex` dòng 1–150; `style/STYLE-GUIDE-VI.md`; `style/GLOSSARY-VI-v2.md`;
  `WRITING-BRIEF.md`; `OUTLINE-V2.md` (mục 2 và hàng Chương 2 của mục 5); báo cáo DACN, Chương 2 (trang PDF 17–24,
  đọc bằng `pdftotext`).
- **Không đọc:** sổ bằng chứng, NOTES/BIB của người viết, các bản nhận xét khác, `codex-work/`. Vì vậy mọi nhận xét về
  nội dung bài gốc chỉ dựa trên chữ trong bản thảo. Chỗ cần mở bài gốc để sửa được ghi **[kiểm với bài]**; chỗ người viết
  phải bổ sung thông tin ghi **[bổ sung: …]**. Ví dụ do người nhận xét dựng ra được ghi rõ là "ví dụ dựng tay".
- **Quy ước trích:** câu trích bỏ `~\cite{…}` cho dễ đọc. Câu đề xuất giữ nguyên nghĩa và con số của bản gốc; câu đề
  xuất trong mục "Thay đổi xếp hạng" viết ở dạng dán thẳng vào LaTeX.
- **Đếm thô bằng script** (tách câu tại dấu chấm, bỏ dòng chú thích `%`, bỏ bảng và công thức): 2.584 tiếng văn xuôi,
  574 tiếng trong hai bảng; 77 câu, trung vị 32 tiếng, 27 câu dài hơn 40 tiếng (35%). DACN: trung vị 26 tiếng, 13,8% câu
  dài hơn 40 tiếng (STYLE-GUIDE mục 0).

---

## Phần 1. Người đọc ngoài ngành

Vai: sinh viên năm cuối ngành khác, đọc lần lượt từng mục, chưa đọc Chương 1.

**Nhận xét chung trước khi vào từng câu.**
- Tiếng Anh: mọi thuật ngữ tiếng Anh đều nằm trong ngoặc ở lần đầu (14 thuật ngữ: dispatcher, DARP, decision epoch,
  request–trip–vehicle graph, integer linear program, insertion-only generator, unreliability, slack, offer,
  forecast-aware promise, TLC, travel-time factor, reliability ratio, promised drop-off time). Không có câu nào trộn tiếng
  Anh trần. Chỗ vướng là **tên riêng chưa được giải thích**: MATSim, MOIA, Mt-KaRRi, DeeprETA (mục 2.3, 2.4).
- Cái khó chính không phải tiếng Anh mà là **câu dài và thuật ngữ dùng trước khi giải thích**: "phương án", "bộ chọn",
  "thứ tự tiêu chí", "độ vòng", "giờ trả muộn nhất", "hồ sơ tắc đường", "phần khách thấy", "cộng có dấu", "tập kiểm tra
  chính", "đường đánh đổi".
- Chương không có ví dụ số nào cho phép so luật C với nghiên cứu gần nhất. DACN luôn có ví dụ ngay sau quy tắc
  (STYLE-GUIDE 1.4). Người ngoài ngành phải tự dựng ví dụ mới hiểu được Bảng 2.2.

Tổng cộng **67 chỗ khó** (đánh số dưới đây).

### Đoạn mở chương (dòng 14–18)

**1. Dòng 14–15 (46 tiếng).** «Chương này trình bày bài toán ghép chuyến động mà khóa luận dựa vào, các cách nghiên cứu
trước đã đo và ràng buộc lời hứa với khách, và những gì đã biết về dự báo thời gian đi và giá trị của độ tin cậy.»
- Vì sao: "ghép chuyến động" dễ đọc vấp thành "chuyến động"; "ràng buộc lời hứa" là cách dịch "constrain the promise";
  "độ tin cậy" chưa rõ là độ tin cậy của cái gì. Câu này là câu mở do OUTLINE quy định, nên chỉ sửa tối thiểu.
- Đề xuất: «Chương này trình bày ba nhóm kiến thức nền: bài toán ghép chuyến khi yêu cầu đến dần theo thời gian (bài
  toán động), mà khóa luận dựa vào; cách các nghiên cứu trước đo và giới hạn việc thay đổi lời hứa với khách; và những gì
  đã biết về dự báo thời gian đi cùng mức khách coi trọng sự đúng giờ.»

**2. Dòng 15–16.** «Lời hứa ở đây là giờ đón, giờ trả báo cho khách, chủ yếu là lời hứa giờ trả (promised drop-off
time).»
- Vì sao: "chủ yếu là" không cho biết khóa luận chỉ xét giờ trả hay xét cả hai.
- Đề xuất: «Lời hứa ở đây là giờ đón và giờ trả mà hệ thống báo cho khách; khóa luận tập trung vào lời hứa giờ trả
  (promised drop-off time).»

**3. Dòng 16–18.** «Mỗi mục tách phần là lý thuyết hay kết quả của người khác khỏi phần RideBound dùng lại; định nghĩa
hình thức của luật C và các luật đối chứng nằm ở Chương 3.»
- Vì sao: vế đầu phải đọc hai lần mới tách được nghĩa. "Luật C" và "luật đối chứng" xuất hiện mà chương này chưa nhắc lại
  chúng là gì; người đọc nhảy thẳng vào Chương 2 không theo được Bảng 2.2.
- Đề xuất: «Ở mỗi mục, lý thuyết và kết quả của các nghiên cứu khác được trình bày trước; đoạn cuối mục nói riêng phần
  RideBound dùng lại hay làm khác. Luật C là luật của khóa luận giới hạn tổng độ lớn phần giờ trả mà bộ điều phối dời của
  mỗi khách qua cả chuyến; định nghĩa chính xác của luật C và của các luật dùng để so sánh với nó nằm ở Chương 3.»
  (Câu định nghĩa một dòng lấy từ Chương 3, dòng 20–23.)

### Mục 2.1 (dòng 21–98)

**4. Dòng 24–25.** «một đội xe có sức chứa giới hạn chở nhiều khách cùng lúc»
- Vì sao: không rõ "sức chứa giới hạn" là của cả đội hay của từng xe.
- Đề xuất: «mỗi xe trong đội chở được nhiều khách cùng lúc, nhưng không quá số chỗ.»

**5. Dòng 26–28 (41 tiếng).** «Đây là một dạng của bài toán đưa đón theo yêu cầu (Dial-a-Ride Problem, DARP): thiết kế
các tuyến xe chi phí nhỏ nhất để chở khách chung theo nhu cầu, trong khi giữ các yêu cầu về mức dịch vụ.»
- Vì sao: "yêu cầu" vừa được định nghĩa là yêu cầu đặt xe ở câu trước, nay lại mang nghĩa "đòi hỏi"; "tuyến xe chi phí
  nhỏ nhất" là trật tự từ tiếng Anh.
- Đề xuất: «Đây là một dạng của bài toán đưa đón theo yêu cầu (Dial-a-Ride Problem, DARP): tìm các tuyến xe có tổng chi
  phí nhỏ nhất để chở chung nhiều khách theo đặt chỗ, đồng thời giữ các ràng buộc về chất lượng dịch vụ.»

**6. Dòng 28–29.** «Ở dạng động, yêu cầu chỉ được biết khi khách gửi, nên bộ điều phối giải lại bài toán ở mỗi lượt
quyết định (decision epoch) với trạng thái lúc đó.»
- Vì sao: "lượt quyết định" được giới thiệu mà không nói một lượt là gì.
- Đề xuất: «Ở dạng động, bộ điều phối chỉ biết một yêu cầu khi khách gửi nó, nên phải giải lại bài toán nhiều lần. Mỗi
  lần giải với trạng thái của đội xe lúc đó gọi là một lượt quyết định (decision epoch).»

**7. Dòng 32.** «đề xuất một cách giải theo lô cho xe đi chung có sức chứa lớn»
- Vì sao: "xe đi chung có sức chứa lớn" là dịch từng chữ "high-capacity ride-sharing".
- Đề xuất: «đề xuất một cách giải theo lô cho dịch vụ đi chung xe, kể cả khi xe có nhiều chỗ.»

**8. Dòng 33–35 (49 tiếng).** «Bước đầu nối hai yêu cầu, hay một yêu cầu với một xe, khi chúng chở chung được mà vẫn thỏa
các ràng buộc dịch vụ; từ đó dựng đồ thị yêu cầu--chuyến--xe (request--trip--vehicle graph), trong đó một chuyến là một
nhóm yêu cầu mà một xe chở được.»
- Vì sao: "Bước đầu" đọc như "ban đầu"; người ngoài ngành không hình dung "nối" là dựng cạnh của đồ thị; câu ôm hai ý.
- Đề xuất: «Thuật toán có hai bước. Bước thứ nhất dựng một đồ thị: hai yêu cầu được nối với nhau nếu một xe chở chung
  được cả hai mà vẫn thỏa các ràng buộc dịch vụ, và một yêu cầu được nối với một xe nếu xe đó phục vụ được nó. Từ đồ thị
  này, thuật toán dựng đồ thị yêu cầu–chuyến–xe (request–trip–vehicle graph); ở đây một chuyến là một nhóm yêu cầu mà
  một xe chở chung được.»

**9. Dòng 35–37.** «Một nhóm chỉ cần kiểm khi mọi nhóm con bớt đi một yêu cầu đều khả thi với cùng xe, nên các nhóm được
dựng dần theo kích thước.»
- Vì sao: đây là ý hay nhất của thuật toán nhưng được nói quá gọn; "khả thi" chưa giải thích.
- Đề xuất: «Để khỏi thử mọi nhóm, thuật toán chỉ kiểm một nhóm khi mọi nhóm con bớt đi một yêu cầu đều chở được bằng cùng
  xe đó. Ví dụ, nhóm ba yêu cầu A, B, C chỉ được kiểm khi cả ba cặp AB, AC, BC đều chở được; vì vậy các nhóm được dựng
  dần từ nhỏ đến lớn.»

**10. Dòng 40.** «Bước chọn là một quy hoạch nguyên (integer linear program).»
- Vì sao: "bước chọn" chưa được gọi tên ở trên (trên chỉ có "bước đầu"); tên Việt thiếu chữ "tuyến tính" so với tên Anh.
- Đề xuất: «Bước thứ hai, bước chọn, chọn chuyến cho từng xe bằng một bài toán quy hoạch tuyến tính nguyên (integer linear
  program).»

**11. Công thức (2.1), dòng 43–46.** `c_{\mathrm{ko}}` và `\quad\text{với}\quad`.
- Vì sao: "ko" đọc như cách viết tắt "không" trong tin nhắn; bài gốc viết $c_{k0}$. "với" không phải cách nói "thỏa các
  ràng buộc". Chỉ số $k$ ở đây là yêu cầu, còn công thức (3.1) ở Chương 3 dùng $k$ cho xe (xem Phần 2, mục G).
- Đề xuất: `\min \sum_{(i,j)} c_{ij}\,\epsilon_{ij} + \sum_{k} c_{k0}\,\chi_k \quad\text{thỏa}\quad …`, và trong câu
  "Trong đó": «$c_{k0}$ là một hằng số lớn, phạt mỗi yêu cầu không được phục vụ. Ký hiệu ở đây theo bài gốc.»

**12. Dòng 56–57.** «Hàm mục tiêu (2.1) đã tính thiệt hại của khách cũ, vì ghép thêm khách làm độ trễ của khách đang trên
xe tăng.»
- Vì sao: "khách cũ" là khẩu ngữ; "thiệt hại" quá nặng.
- Đề xuất: «Hàm mục tiêu (2.1) đã tính phần thiệt của các khách đang được phục vụ: khi ghép thêm khách, độ trễ của họ
  tăng nên $c_{ij}$ tăng.»

**13. Dòng 57–58 (47 tiếng).** «Tuy vậy, đó là một số hạng mềm, cộng chung trên mọi khách và đo so với chuyến đi thẳng,
không so với giờ đã báo; một khách vì thế có thể bị dời giờ trả nhiều lần, miễn là mỗi lần tổng chi phí nhỏ hơn.»
- Vì sao: "số hạng mềm" là biệt ngữ tối ưu hóa; "nhỏ hơn" không nói nhỏ hơn cái gì; vế sau là suy luận của người viết
  (dòng chú thích EV đã ghi vậy) nhưng văn bản không cho người đọc biết.
- Đề xuất: «Tuy vậy, phần thiệt này chỉ là một khoản cộng vào chi phí, không phải một điều cấm. Nó được cộng chung cho
  mọi khách và đo so với chuyến đi thẳng, không so với giờ đã báo cho khách. Suy từ định nghĩa này, một khách có thể bị
  dời giờ trả nhiều lần, miễn là mỗi lần dời cho tổng chi phí nhỏ hơn các cách gán khác.»

**14. Dòng 58–59.** «Hàm mục tiêu kiểu này không định giá việc sửa lời hứa; Fielbaum và Alonso-Mora đã đo và kiểm soát
hiện tượng đó (mục 2.2).»
- Vì sao: "định giá việc sửa lời hứa" là dịch; "hiện tượng đó" không rõ chỉ cái gì.
- Đề xuất: «Nói cách khác, hàm mục tiêu này không tính chi phí cho việc báo lại giờ trả cho khách. Fielbaum và
  Alonso-Mora đã đo và kiểm soát việc giờ đã báo bị thay đổi như vậy (mục 2.2).»

**15. Dòng 62–64 (41 tiếng).** «Với mỗi xe, bộ sinh chỉ chèn thêm (insertion-only generator) tạo phương án giữ nguyên kế
hoạch và các phương án chèn điểm đón, điểm trả của yêu cầu mới vào kế hoạch cũ, không bỏ và không đảo điểm cũ.»
- Vì sao: "phương án" và "kế hoạch" là thuật ngữ của RideBound, chưa được định nghĩa (Chương 3 mới định nghĩa).
- Đề xuất: «Với mỗi xe, bộ sinh chỉ chèn thêm (insertion-only generator) tạo ra các phương án, tức các kế hoạch (dãy
  điểm đón, điểm trả theo thứ tự) có thể chọn cho xe: một phương án giữ nguyên kế hoạch cũ, và các phương án chèn điểm
  đón, điểm trả của yêu cầu mới vào kế hoạch cũ mà không bỏ hay đổi thứ tự các điểm cũ.»

**16. Dòng 64–66.** «Bộ chọn giao mỗi xe đúng một phương án và so các phương án theo một thứ tự tiêu chí thay cho một tổng
chi phí; khách đã nhận không được chuyển sang xe khác (mục 3.1.2).»
- Vì sao: "bộ chọn", "thứ tự tiêu chí" chưa giải thích. "thay cho một tổng chi phí" lệch Bảng 3.2 của Chương 3, nơi tổng
  chi phí vẫn là tiêu chí 4. "khách đã nhận" khác "khách đã xác nhận đặt xe", mốc mà Chương 3 (dòng 78–79) dùng cho khóa.
- Đề xuất: xem thay đổi **N4** ở cuối tệp.

**17. Dòng 66.** «Bảng 2.1 ghi các ràng buộc dịch vụ cùng dạng với các bài trên.»
- Vì sao: "các bài" là khẩu ngữ; "cùng dạng" không nói bảng giúp gì.
- Đề xuất: «Bảng 2.1 đặt các ràng buộc dịch vụ trong tập thử của khóa luận cạnh cách đặt ở các nghiên cứu trên.»

**18. Bảng 2.1, dòng thứ hai (dòng 84–87).** «phần vượt thời gian đi thẳng tính theo tỉ lệ của nó» và «độ vòng tương đối
40%».
- Vì sao: cụm thứ nhất không hiểu được ("của nó" là của cái gì); "độ vòng" chưa định nghĩa ở đâu trong chương.
- Đề xuất: «phần vượt thời gian đi thẳng, tính bằng tỉ lệ so với thời gian đi thẳng» và «thời gian ngồi xe dài thêm tối
  đa 40% so với đi thẳng». Khi viết như vậy, người đọc tự so được với giá trị của khóa luận (1,5 lần, tức thêm 50%).

**19. Bảng 2.1, dòng một và ba (dòng 80–82, 89–90).** Đơn vị lẫn lộn ("2, 5 hoặc 7 phút", "480 giây", "600 giây"); ô
"4 chỗ; 8 xe mỗi kịch bản" đặt số xe vào dòng sức chứa, và "kịch bản" chưa được định nghĩa.
- Đề xuất: «8 phút (480 giây)»; «10 phút (600 giây) kể từ lúc gọi» (khớp Bảng 3.2 viết "10 phút"); ô sức chứa chỉ ghi «4
  chỗ»; số xe chuyển vào chú thích bảng hoặc bỏ.

**20. Dòng 96–97 (43 tiếng).** «Trong Bảng 2.1, độ trễ tổng của Alonso-Mora và cộng sự gồm cả thời gian chờ, còn giới hạn
của khóa luận chỉ tính thời gian ngồi trên xe; các giá trị của khóa luận chưa được hiệu chỉnh theo sở thích của khách.»
- Vì sao: hai ý trong một câu; không nói người đọc nên rút ra gì từ bảng.
- Đề xuất: «Bảng 2.1 cần đọc với hai lưu ý. Độ trễ tổng của Alonso-Mora và cộng sự gồm cả thời gian chờ, còn giới hạn của
  khóa luận chỉ tính thời gian ngồi trên xe. Các giá trị của khóa luận cũng chưa được hiệu chỉnh theo sở thích của
  khách.»

### Mục 2.2 (dòng 101–137)

**21. Dòng 104.** Mục mở thẳng bằng tên một bài, không có câu nói mục làm gì (STYLE quy tắc 2).
- Đề xuất câu mở: «Mục này trình bày hai nghiên cứu đo và giới hạn việc giờ đã báo cho khách bị thay đổi sau khi gán
  xe.»

**22. Dòng 104–106 (50 tiếng).** «Fielbaum và Alonso-Mora phân loại độ bất ổn (unreliability) của dịch vụ đi chung xe
theo nguồn: từ khách, như khách vắng mặt hay hủy chuyến, và từ hãng xe, khi cách gán yêu cầu thay đổi mỗi lần có yêu cầu
mới; họ tập trung vào nguồn thứ hai.»
- Đề xuất: «Fielbaum và Alonso-Mora chia độ bất ổn (unreliability) của dịch vụ đi chung xe theo nguồn. Nguồn từ khách
  gồm khách vắng mặt hay hủy chuyến; nguồn từ hãng xe là việc cách gán yêu cầu cho xe thay đổi mỗi khi có yêu cầu mới.
  Bài tập trung vào nguồn thứ hai.»

**23. Dòng 106–107.** «Giá trị báo ban đầu là giá trị sẽ đạt nếu lộ trình của xe không đổi kể từ lần gán thứ nhất.»
- Vì sao: "giá trị" của cái gì? Đại lượng chỉ được kể ở câu sau.
- Đề xuất: «Với mỗi khách, giá trị báo ban đầu của thời gian chờ, độ vòng và độ trễ tổng là giá trị khách sẽ có nếu lộ
  trình của xe giữ nguyên từ lần gán thứ nhất.»

**24. Dòng 107–108 (51 tiếng).** «Chỉ số của họ là hiệu giữa giá trị thực tế và giá trị báo ban đầu của thời gian chờ, độ
vòng và độ trễ tổng, với giá trị âm đặt bằng 0 để chỉ giữ phần bất lợi; họ còn đếm số lần giá trị dự kiến tăng lên.»
- Vì sao: dài; "độ vòng" chưa định nghĩa.
- Đề xuất: «Chỉ số của họ là phần giá trị thực tế vượt giá trị báo ban đầu; nếu thực tế tốt hơn thì chỉ số bằng 0, để chỉ
  giữ phần bất lợi cho khách. Họ còn đếm số lần giá trị dự kiến tăng lên.» Thêm một lần định nghĩa: «độ vòng là phần thời
  gian ngồi xe dài thêm so với đi thẳng» **[kiểm với bài]**.

**25. Dòng 111–112 (6 con số trong một câu).** «Thí nghiệm của họ dùng mạng Manhattan 4.091 nút, 9.453 cạnh, 2.000 xe 4
chỗ và 19.610 yêu cầu trong khung 13--15 giờ ngày 15/01/2013, một khung thấp điểm được chọn để bỏ qua độ bất ổn do tắc
đường.»
- Vì sao: vượt quy tắc 5 (tối đa hai số một câu); "nút", "cạnh" là từ của lý thuyết đồ thị; "bỏ qua" mơ hồ (bỏ qua hay
  tránh).
- Đề xuất: «Thí nghiệm của họ chạy trên mạng đường Manhattan gồm 4.091 nút giao và 9.453 đoạn đường, với 2.000 xe 4 chỗ.
  Nhu cầu là 19.610 yêu cầu trong khung 13–15 giờ ngày 15/01/2013; các tác giả chọn khung thấp điểm này để độ bất ổn do
  tắc đường đủ nhỏ mà bỏ qua.»

**26. Dòng 112–113.** «hơn một phần ba số yêu cầu không bị từ chối ngay gặp ít nhất một thay đổi»
- Vì sao: phủ định trong phủ định ("không hạn chế", "không bị từ chối"); "thay đổi" của cái gì.
- Đề xuất: «Khi khách được phép bị chuyển sang xe khác, hơn một phần ba số yêu cầu được nhận ở lần gán đầu gặp ít nhất
  một lần thay đổi so với giá trị báo ban đầu.»

**27. Dòng 113–114.** «khi thời gian chờ của một khách tăng, phần tăng tương đương thời gian chờ trung bình của cả hệ
thống.»
- Đề xuất: «Với những khách bị tăng thời gian chờ, mức tăng xấp xỉ bằng thời gian chờ trung bình của cả hệ thống.»

**28. Dòng 117.** «Ở mục 6 của bài, họ kiểm soát độ bất ổn ngay trong quyết định.»
- Vì sao: "ngay trong quyết định" không rõ nghĩa.
- Đề xuất: «Ở mục 6 của bài, các tác giả đưa việc kiểm soát độ bất ổn vào chính bước gán xe, tức chặn trước khi quyết
  định thay vì chỉ đo sau đó.»

**29. Dòng 117–120 (56 tiếng, 4 con số).** «Trong kịch bản kiểm soát hoàn toàn, … chi phí trung bình của khách theo mô hình
tăng từ 9,56 lên 11,6.»
- Vì sao: "kịch bản" ở Chương 3 là "một ngày, một mẫu nhu cầu, một khung 2 giờ"; ở đây lại là mức kiểm soát. Không rõ
  đơn vị của 9,56 và 11,6.
- Đề xuất: xem thay đổi **N3**.

**30. Dòng 120–121.** «Kịch bản trung gian chỉ cấm từ chối khách đã nhận: tỉ lệ từ chối còn 31,2%, …»
- Vì sao: "còn" gợi là giảm, nhưng không nói giảm so với gì; người đọc phải tự nhớ 34,5% ở câu trước.
- Đề xuất: xem **N3**.

**31. Dòng 121.** «và để ngỏ câu hỏi kiểm soát độ bất ổn mà không tăng từ chối.»
- Đề xuất: «và để ngỏ câu hỏi làm sao kiểm soát độ bất ổn mà không làm tăng số yêu cầu bị từ chối.»

**32. Dòng 124.** «Elmi và cộng sự tiếp tục hướng này theo từng khách.»
- Đề xuất: «Elmi và cộng sự tiếp tục hướng này, nhưng đặt mức kiểm soát riêng cho từng khách.»

**33. Dòng 124–126.** «Độ chùng (slack) của một khách là hiệu giữa thời gian chờ tối đa, hay độ trễ tối đa, và giá trị dự
kiến lúc gán; đó là phần còn cho phép thay đổi về sau.»
- Vì sao: "hay" đọc được thành "tức là" hoặc "hoặc".
- Đề xuất: xem **N5**.

**34. Dòng 126–127.** «Khách có điểm khả năng đi chung thấp nhận độ chùng 0, …»
- Vì sao: không biết điểm này tính thế nào; bài được mô tả quá gọn để hiểu họ đã làm gì.
- Đề xuất: xem **N5** (cần **[bổ sung: cách tính điểm, một câu]**).

**35. Dòng 127–128.** «Ở cùng tỉ lệ từ chối 29% với cách siết đều cho mọi khách, cách này bảo đảm chuyến không đổi giờ
cho 83,9% số khách ngay lúc gán.»
- Vì sao: không biết cách siết đều cho kết quả bao nhiêu, nên không thấy được 83,9% là tốt hay không.
- Đề xuất: xem **N5**.

**36. Dòng 128.** «thời gian đi trên mỗi cạnh không đổi» → «thời gian đi trên mỗi đoạn đường không đổi».

**37. Dòng 131–132 (51 tiếng).** «Thước đo của Fielbaum và Alonso-Mora so giá trị cuối với giá trị báo ban đầu, nên một
khách bị dời muộn 5 phút rồi được kéo về giờ cũ có hiệu bằng 0, dù đã nhận hai lần thay đổi; số lần tăng được đếm nhưng
không mang độ lớn.»
- Vì sao: ví dụ tốt nhưng không được báo là ví dụ; "không mang độ lớn" là dịch.
- Đề xuất: «Thước đo của Fielbaum và Alonso-Mora so giá trị cuối với giá trị báo ban đầu. Ví dụ, một khách bị dời muộn 5
  phút rồi được kéo về giờ cũ có hiệu bằng 0, dù đã nhận hai lần thay đổi. Chỉ số đếm số lần tăng có ghi nhận lần dời
  muộn đó, nhưng không cho biết nó lớn bao nhiêu.»

**38. Dòng 132–134 (45 tiếng).** «Khóa luận kế thừa ý tách phần thay đổi do quyết định của hãng xe và kiểm soát nó trước khi
quyết định, nhưng đo từng lần sửa so với giờ trả khi giữ nguyên kế hoạch và cộng độ lớn qua cả chuyến.»
- Vì sao: dài; "phần thay đổi do quyết định của hãng xe" khác tên "phần dời do điều phối" của Chương 3 (GLOSSARY: nói về
  quyết định của thuật toán thì dùng "bộ điều phối", không dùng "hãng xe").
- Đề xuất: «Khóa luận kế thừa hai ý của bài: tách riêng phần thay đổi do điều phối, và kiểm soát phần đó trước khi ra
  quyết định. Khóa luận khác ở cách đo: mỗi lần sửa lời hứa được so với giờ trả khi xe giữ nguyên kế hoạch, và độ lớn
  các lần sửa được cộng qua cả chuyến (mục 3.2).»

**39. Dòng 134–136.** «Trên tập kiểm tra chính, mỗi lần điều phối kéo giờ trả sớm hơn chỉ sớm 1 mili giây, nên khác biệt
này nằm ở định nghĩa, chưa thấy ở kết quả.»
- Vì sao: câu khó nhất chương. "Tập kiểm tra chính" chưa định nghĩa; "khác biệt này" không rõ là khác biệt nào; vì sao
  một quyết định điều phối lại dời giờ đúng 1 mili giây; và đây là kết quả của Chương 4 đặt vào chương cơ sở.
- Đề xuất: xem thay đổi **B5**.

### Mục 2.3 (dòng 140–212)

**40. Dòng 143–144.** «các nghiên cứu trước còn ràng buộc chính lời hứa với khách»
- Đề xuất: «một số nghiên cứu còn đặt giới hạn trực tiếp lên giờ đã báo cho khách».

**41. Dòng 144.** «Nhiều cách giữ một giờ đã báo.»
- Vì sao: câu cụt, không rõ chủ ngữ.
- Đề xuất: «Phần lớn các cách này giữ cố định một giờ đã báo.»

**42. Dòng 144–146 (60 tiếng tính cả câu Lu–Kühnel).** «Alonso-Mora và cộng sự hạ giờ đón muộn nhất về giờ đón dự kiến khi
yêu cầu được ghép xe, và chỉ chuyển yêu cầu sang xe khác nếu thời gian chờ không tăng»
- Vì sao: "giờ đón muộn nhất" chưa định nghĩa.
- Đề xuất: «Trong hệ của Alonso-Mora và cộng sự, mỗi yêu cầu có một giờ đón muộn nhất, bằng giờ gọi xe cộng cửa sổ đón.
  Khi yêu cầu được ghép xe, giờ đón muộn nhất được hạ xuống bằng giờ đón dự kiến lúc đó, và yêu cầu chỉ được chuyển sang
  xe khác nếu thời gian chờ không tăng.» (Định nghĩa suy từ dòng "Cửa sổ đón" của Bảng 2.1.)

**43. Dòng 146–147.** «Lu và Kühnel cho giờ đón muộn hơn giờ hẹn ban đầu nhiều nhất một khoảng đệm, gợi ý 2--3 phút để
chừa cho tắc đường.»
- Vì sao: bài được mô tả quá gọn: không biết họ nghiên cứu loại dịch vụ nào, thí nghiệm gì.
- Đề xuất: «Lu và Kühnel, khi nghiên cứu **[bổ sung: loại dịch vụ hay bài toán]**, cho phép giờ đón thực tế muộn hơn giờ
  hẹn ban đầu nhiều nhất một khoảng đệm; các tác giả gợi ý đệm 2–3 phút để chừa cho tắc đường.»

**44. Dòng 147–149 (đơn vị lẫn, "quét").** «Schulz và Pfeiffer đặt hạn chót trả bằng giờ trả trong lời mời (offer) cộng
một độ chùng, mặc định 900 giây, và thấy 10--15 phút là đánh đổi hợp lý khi quét độ chùng tới 30 phút.»
- Vì sao: "lời mời" là gì trong mô hình của họ; "quét" là biệt ngữ; "đánh đổi hợp lý" giữa hai đại lượng nào; 900 giây và
  10–15 phút khó so.
- Đề xuất: «Trong mô hình của Schulz và Pfeiffer, hệ thống gửi cho khách một lời mời (offer) có giờ trả dự kiến. Khi
  khách nhận lời, hạn chót trả bằng giờ trả trong lời mời cộng một độ chùng, mặc định 900 giây (15 phút). Khi thử các mức
  độ chùng tới 30 phút, các tác giả thấy mức 10–15 phút cho đánh đổi hợp lý giữa **[bổ sung: hai chỉ số]**.»

**45. Dòng 149–150.** «Bộ điều phối Mt-KaRRi của Laupichler và cộng sự giới hạn thời gian chuyến ở 1,4 lần thời gian chuyến
đã báo lúc khách chấp nhận, cộng 10 phút.»
- Vì sao: "Mt-KaRRi" chưa giải thích; "thời gian chuyến" tính từ lúc gọi hay từ lúc lên xe; dễ đọc nhầm thành 1,4 lần của
  (thời gian đã báo cộng 10 phút).
- Đề xuất: «Bộ điều phối Mt-KaRRi của Laupichler và cộng sự, **[bổ sung: một cụm nói Mt-KaRRi giải bài toán gì]**, giới
  hạn thời gian chuyến của mỗi khách ở mức 1,4 lần thời gian chuyến đã báo lúc khách chấp nhận, rồi cộng thêm 10 phút. Ví
  dụ, chuyến đã báo 20 phút thì không được kéo dài quá 1,4 × 20 + 10 = 38 phút.» (Ví dụ dựng tay.)

**46. Dòng 153–154.** «trong mô phỏng MATSim với nhu cầu thật của MOIA ở Hamburg»
- Đề xuất: «trong bộ mô phỏng giao thông MATSim, với nhu cầu lấy từ dịch vụ đi chung xe MOIA ở Hamburg».

**47. Dòng 154–155.** «họ duyệt lại tuyến đang gán theo thời gian đi hiện tại để có giờ trả cập nhật.»
- Đề xuất: «họ tính lại giờ trả dọc theo tuyến đang gán bằng thời gian đi hiện tại; kết quả gọi là giờ trả cập nhật.»

**48. Dòng 155–157 (64 tiếng).** «Theo công thức 7 của bài, giờ trả bắt buộc … bằng giá trị lớn hơn giữa giờ trả cập nhật và
giờ trả muộn nhất; tuyến phải thỏa giờ bắt buộc như ràng buộc cứng (ràng buộc 9--10), còn mỗi giây vượt giờ trả muộn nhất
gốc bị phạt trong hàm mục tiêu (công thức 11).»
- Vì sao: ba tên mới trong một câu ("giờ trả bắt buộc", "giờ trả muộn nhất", "giờ trả muộn nhất gốc"); "giờ trả muộn
  nhất" chưa định nghĩa; số hiệu công thức của bài khác vô nghĩa với người đọc.
- Đề xuất: xem thay đổi **B1**.

**49. Dòng 157–159 (51 tiếng).** «Xe vẫn được đón thêm khách, miễn là khách trên xe không bị trả muộn hơn mức sớm nhất có thể
với tắc đường hiện tại, nên thuật toán không rơi vào tình huống hết thứ tự trả khách khả thi»
- Vì sao: câu này nói hạn được nới tới "mức sớm nhất có thể", còn câu trước nói tới "giờ trả cập nhật" trên tuyến đang
  gán. Hai mốc này khác nhau; người đọc không biết mốc nào đúng. "Hết thứ tự trả khách khả thi" là dịch. Vế "nên …" là
  quan hệ nhân quả không ghi là của tác giả.
- Đề xuất: xem **B1**.

**50. Dòng 159–160.** «Khi thời gian đi bị ước lượng thấp, hãng xe phải chọn giữa từ chối khách đã nhận và trả khách muộn
hơn giờ đã báo; với thời gian đi thực tế, tác động này nhỏ.»
- Vì sao: "với thời gian đi thực tế" không rõ (ước lượng đúng? dữ liệu thật?); "tác động này" là tác động nào.
- Đề xuất: xem **B1**.

**51. Bảng 2.2, tiêu đề cột 5 và 6 (dòng 173–174).** «Cộng qua cả chuyến?», «Ghi riêng cho từng khách?»
- Vì sao: dòng 208 nói cộng có dấu các lần thay đổi thì ra hạn chót tính từ lời hứa đầu, tức hạn chót cũng là một kiểu
  "cộng qua cả chuyến"; vậy mà cột 5 ghi "Không" cho Schulz–Pfeiffer. Dòng Elmi mang tên "Bảo đảm theo từng khách" nhưng
  cột 6 lại ghi "Không". Người đọc thấy bảng tự mâu thuẫn.
- Đề xuất: xem thay đổi **B3**.

**52. Bảng 2.2, dòng Hörl–Zwick (dòng 188–190).** Tên dòng mang ba số hiệu công thức; ô "Áp cho ai" trộn "ai" với "khi
nào".
- Đề xuất: xem **B3**.

**53. Dòng 206–208 (58 tiếng).** «Luật C dùng lại mốc giờ trả cập nhật của Hörl và Zwick nhưng giới hạn một đại lượng khác:
…, không nới theo tắc đường, và ghi vào sổ theo từng khách.»
- Vì sao: năm ý trong một câu; "không nới theo tắc đường" mâu thuẫn bề ngoài với vế trước (mốc so sánh của luật C có đổi
  theo tắc đường; cái không đổi là trần).
- Đề xuất: xem thay đổi **B2**.

**54. Dòng 208–209.** «Cộng có dấu cả phần dời do điều phối lẫn phần thay đổi khi giữ nguyên kế hoạch thì quay về hạn chót
tính từ lời hứa đầu; cộng độ lớn phần khách thấy thì là luật trần độ dời khách thấy.»
- Vì sao: "cộng có dấu", "phần khách thấy", "quay về" chưa giải thích; người ngoài ngành không theo được.
- Đề xuất: xem **B2**.

### Mục 2.4 (dòng 215–244)

**55. Dòng 218–220 (46 tiếng).** «Hörl và Zwick xét đúng tình huống ước lượng thấp này, với tốc độ cập nhật mỗi 60 phút từ dữ
liệu định vị.»
- Vì sao: "tốc độ cập nhật" đọc được thành "tần suất cập nhật".
- Đề xuất: «Khi đường đông dần, giờ tính theo cách này sớm hơn giờ xe thực sự tới, dù xe giữ nguyên kế hoạch. Hörl và
  Zwick xét đúng tình huống ước lượng thấp này: trong mô phỏng của họ, tốc độ đi trên mạng đường chỉ được cập nhật mỗi 60
  phút từ dữ liệu định vị.»

**56. Dòng 223.** «Dự báo giờ đến từ dữ liệu là thực hành của các nền tảng gọi xe.»
- Vì sao: "là thực hành của" là dịch "is the practice of"; câu khái quát cho "các nền tảng" trong khi chỉ trích một hãng.
- Đề xuất: «Dự báo giờ đến từ dữ liệu đã được dùng trong vận hành, ví dụ ở Uber.»

**57. Dòng 223–226 (72 tiếng, câu dài nhất chương).** «Uber dùng giờ đến dự kiến … và giờ hiển thị cho khách có thể cần một
phân vị thay cho giá trị trung bình.»
- Vì sao: ba ý trong một câu; "phân vị" chưa giải thích.
- Đề xuất: «Hãng dùng giờ đến dự kiến để tính giá cước, ước lượng giờ đón, giờ trả và ghép khách với tài xế. Mô hình học
  sâu DeeprETA của hãng không tính giờ đến từ đầu mà hiệu chỉnh giờ đến do bộ tìm đường tính, dựa trên thời điểm trong
  ngày, ngày trong tuần, tốc độ thời gian thực và tốc độ lịch sử. Các tác giả cũng lưu ý rằng giờ hiển thị cho khách có
  thể cần lấy theo một phân vị, tức một mức mà phần lớn các chuyến không vượt, thay cho giá trị trung bình.»

**58. Dòng 226–228 (46 tiếng).** «Leonardi và cộng sự học từ một số chuyến đã quan sát trong mô phỏng một khoảng thời gian
chuyến đúng trong hơn 90% số lần, và đề xuất lấy mức dự báo được làm tiêu chí định cỡ dịch vụ đáp ứng theo nhu cầu.»
- Vì sao: câu "đọc vấp" (dễ hiểu thành "trong mô phỏng một khoảng"); "định cỡ dịch vụ đáp ứng theo nhu cầu" là dịch.
- Đề xuất: «Leonardi và cộng sự dùng một số chuyến đã quan sát trong mô phỏng để học ra một khoảng thời gian chuyến;
  khoảng này chứa thời gian chuyến thật trong hơn 90% số lần. Các tác giả đề xuất dùng mức dự báo được của thời gian
  chuyến làm một tiêu chí khi định quy mô dịch vụ xe theo yêu cầu.»

**59. Dòng 232–233.** «hồ sơ tắc đường của các ngày đã qua»
- Vì sao: "hồ sơ" thường nghĩa là giấy tờ; thuật ngữ chưa định nghĩa; "hệ số tắc đường" chỉ được giới thiệu ở dòng 241.
- Đề xuất: «Một dự báo dùng cho lời hứa chỉ được dùng thông tin đã có lúc hứa: hồ sơ tắc đường, tức mức tắc đường theo
  từng khung giờ của các ngày đã qua, và mức tắc đường đo được lúc hứa.»

**60. Dòng 234–235.** «Hồ sơ lập từ các ngày ngay trước, như ở mục 3.5, vì vậy giả định hãng xe có sẵn dữ liệu chuyến của
chính mình.»
- Vì sao: chủ ngữ bị đảo (hồ sơ "giả định"); câu là suy luận của người viết nhưng viết như hệ quả tất yếu.
- Đề xuất: xem thay đổi **N2**.

**61. Dòng 238–240 (51 tiếng).** «Bài hiệu chỉnh thời gian đi bằng cách so thời lượng chuyến được ghi với thời gian đi đường
nhanh nhất theo tốc độ tối đa cho phép, mỗi giờ trong ngày một hệ số nhân; gói dữ liệu còn có tệp hệ số theo khung 15
phút cho từng ngày.»
- Vì sao: "Bài" là bài nào (câu trước nói "bộ dữ liệu"); câu dài.
- Đề xuất: «Để hiệu chỉnh thời gian đi, các tác giả FleetPy so thời lượng chuyến ghi trong dữ liệu taxi với thời gian đi
  theo đường nhanh nhất ở tốc độ tối đa cho phép, và suy ra một hệ số nhân cho mỗi giờ trong ngày. Gói dữ liệu còn kèm một
  tệp hệ số theo khung 15 phút cho từng ngày.»

**62. Dòng 242–244.** «… nên được đọc như mức trần cho loại dự báo theo giờ trong ngày, không phải hiệu quả ngoài đời.»
- Vì sao: "mức trần" ở đây là "cận trên", nhưng trong cả khóa luận "trần" là trần B của luật C. Người đọc sẽ hiểu nhầm.
  Ngoài ra "cận trên" là một khẳng định chưa được chứng minh.
- Đề xuất: xem thay đổi **B4**.

### Mục 2.5 (dòng 248–264)

**63. Dòng 251.** «Các nghiên cứu về giá trị thời gian cho thấy khách coi việc tới muộn nặng hơn thời gian ngồi xe.»
- Vì sao: "khách" gợi khách đi chung xe, trong khi các nghiên cứu này nói về người đi lại nói chung.
- Đề xuất: «Các nghiên cứu về giá trị thời gian cho thấy người đi lại coi một phút tới muộn nặng hơn một phút ngồi xe.»

**64. Dòng 251–253 (51 tiếng, 6 con số).** «Phân tích tổng hợp của Wardman và cộng sự cho mỗi phút tới đích muộn … một hệ số
trung bình 2,53 lần phút ngồi xe (15 quan sát, 2 nghiên cứu) hoặc 3,12 lần (66 quan sát, 27 nghiên cứu), tùy cách hỏi.»
- Vì sao: "cho … một hệ số" là cấu trúc dịch; "tùy cách hỏi" không nói hai cách hỏi là gì.
- Đề xuất: «Theo phân tích tổng hợp của Wardman và cộng sự, một phút tới đích muộn so với giờ biểu hay giờ dự kiến được
  coi nặng bằng trung bình 2,53 phút ngồi xe (15 quan sát từ 2 nghiên cứu) hoặc 3,12 phút ngồi xe (66 quan sát từ 27
  nghiên cứu), tùy cách hỏi **[bổ sung: tên hai cách hỏi]**.»

**65. Dòng 253–256 (64 tiếng).** «Với dịch vụ đi chung xe, Alonso-González và cộng sự khảo sát 1.006 người ở Hà Lan và thấy
tỉ số giữa giá trị độ tin cậy và giá trị thời gian (reliability ratio) khoảng 0,5; một khoản trễ nhỏ không báo trước được
định giá thấp hơn thời gian đã báo, và người trả lời không được đặt vào tình huống tới muộn.»
- Vì sao: "giá trị độ tin cậy" chưa định nghĩa; "được định giá thấp hơn thời gian đã báo" nghe ngược trực giác nếu không
  giải thích; vế cuối là giới hạn của khảo sát nhưng đọc như một kết quả.
- Đề xuất: «Riêng với dịch vụ đi chung xe, Alonso-González và cộng sự khảo sát 1.006 người ở Hà Lan. Họ đo giá trị độ tin
  cậy, tức **[bổ sung: định nghĩa một câu theo bài]**, và thấy tỉ số giữa giá trị này và giá trị thời gian (reliability
  ratio) khoảng 0,5: một khoản trễ nhỏ không báo trước bị coi nhẹ hơn cùng khoảng thời gian đã được báo trước. Bảng hỏi
  của họ không đặt người trả lời vào tình huống tới muộn.»

**66. Dòng 256–258 (47 tiếng).** «Trong một thí nghiệm thực địa trên 1.425.745 chuyến, Yu và cộng sự thấy cả độ lớn của thời
gian chờ báo ban đầu lẫn số lần cập nhật đều ảnh hưởng tới việc khách bỏ yêu cầu.»
- Vì sao: không biết thí nghiệm ở nền tảng nào, nước nào; "số lần cập nhật" của cái gì.
- Đề xuất: «Theo phần tóm tắt, Yu và cộng sự làm một thí nghiệm thực địa trên 1.425.745 chuyến **[bổ sung: nền tảng, nơi,
  nếu tóm tắt có]**, và thấy cả thời gian chờ được báo lúc đầu lẫn số lần thông tin này được cập nhật đều ảnh hưởng tới
  việc khách hủy yêu cầu.»

**67. Dòng 262–264 (51 tiếng).** «Không kết quả nào cho một giá tiền của trần 30 giây trên phần dời giờ trả do điều phối, và
chưa có chuẩn ngành cho loại trần này; vì vậy khóa luận coi mỗi mức trần là một điểm trên đường đánh đổi, không phải
ngưỡng khách cảm nhận được.»
- Vì sao: "trần 30 giây" xuất hiện lần đầu trong chương mà không giới thiệu; "đường đánh đổi" chưa định nghĩa; "chưa có
  chuẩn ngành" là khẳng định về sự vắng mặt, cần giới hạn phạm vi.
- Đề xuất: xem thay đổi **N2**.

### Năm câu tóm tắt điều người đọc ngoài ngành học được

1. Trong dịch vụ đi chung xe, bộ điều phối giải lại bài toán gán xe theo từng lượt; cách kinh điển của Alonso-Mora và cộng
   sự chọn chuyến bằng quy hoạch nguyên và tính thiệt của khách đang trên xe chỉ như một khoản chi phí so với chuyến đi
   thẳng, nên giờ trả đã báo vẫn có thể bị dời nhiều lần.
2. Fielbaum và Alonso-Mora đo phần giờ đã báo bị làm xấu đi do cách gán xe thay đổi, và cho thấy chặn nó ngay khi gán làm
   tỉ lệ từ chối tăng từ 34,5% lên 45,6%; Elmi và cộng sự chọn một số khách để bảo đảm không đổi giờ.
3. Các nghiên cứu khác giới hạn chính giờ đã báo: giữ giờ đón (Alonso-Mora, Lu–Kühnel), hạn chót trả bằng giờ trong lời
   mời cộng 900 giây (Schulz–Pfeiffer), 1,4 lần thời gian chuyến đã báo cộng 10 phút (Mt-KaRRi), và hạn trả được nới theo
   giờ trả cập nhật khi tắc đường (Hörl–Zwick).
4. Luật C của khóa luận cộng độ lớn các lần bộ điều phối dời giờ trả, so với giờ trả nếu xe giữ nguyên kế hoạch, qua cả
   chuyến, và giữ tổng đó dưới một trần chung cho mỗi khách, nên phần do tắc đường không bị tính vào trần.
5. Lời hứa theo dự báo không phải ý mới (Uber, Leonardi và cộng sự), dữ liệu FleetPy chỉ có một hệ số tắc đường chung cho
   cả thành phố, và các nghiên cứu về giá trị độ tin cậy không cho biết trần 30 giây đáng giá bao nhiêu với khách.

### Những gì người đọc chưa hiểu được

- Hạn trả được nới của Hörl và Zwick là **giờ trả cập nhật trên tuyến đang gán** (dòng 155–156) hay **mức sớm nhất có thể
  với tắc đường hiện tại** (dòng 158)? Từ đó, trong tình huống cụ thể nào luật C và cách của Hörl–Zwick cho quyết định
  khác nhau? Chương không có ví dụ.
- "Giờ trả muộn nhất" là gì và lớn cỡ nào (suy từ độ trễ tối đa?).
- Điểm "khả năng đi chung" của Elmi và cộng sự tính thế nào; cách "siết đều" cho bao nhiêu phần trăm khách không đổi giờ.
- Mt-KaRRi, MOIA, MATSim là gì; Lu và Kühnel nghiên cứu hệ thống nào.
- Đơn vị của chi phí 9,56 và 11,6 trong bài của Fielbaum và Alonso-Mora.
- "1 mili giây" nghĩa là gì, vì sao một quyết định điều phối lại dời giờ trả đúng 1 mili giây, và vì sao điều đó làm khác
  biệt giữa hai cách đo "chưa thấy ở kết quả".
- Vì sao cộng có dấu hai phần thì "quay về" hạn chót tính từ lời hứa đầu.
- "Mức trần" ở dòng 243 là trần B hay cận trên.
- Hai "cách hỏi" của Wardman; định nghĩa "giá trị độ tin cậy" của Alonso-González.
- "Đánh đổi hợp lý" của Schulz và Pfeiffer là giữa hai chỉ số nào.
- Vì sao cửa sổ đón của khóa luận (10 phút) rộng hơn mọi giá trị trong Bảng 2.1 (2–8 phút).

### Có giải thích được trong một câu luật C khác nghiên cứu gần nhất ở đâu không?

Được, nhưng chỉ sau khi đọc chéo Bảng 2.2 với đoạn dòng 206–211 và tự suy ra; chương chưa có sẵn câu nào như vậy, và mô
tả Hörl–Zwick còn chỗ mâu thuẫn (dòng 156 với dòng 158). Câu người đọc tự viết được:

> Hörl và Zwick (công thức 7) và Schulz và Pfeiffer giới hạn chính giờ trả so với một hạn (giờ trả muộn nhất, được nới
> theo giờ trả cập nhật khi tắc đường đã vượt nó; hay giờ trả trong lời mời cộng 900 giây), nên bộ điều phối được dời giờ
> trả tới sát hạn và tắc đường cũng làm hẹp khoảng còn lại; luật C thì không đặt hạn cho giờ trả mà cộng độ lớn mọi lần
> bộ điều phối dời giờ trả so với giờ trả khi xe giữ nguyên kế hoạch, qua cả chuyến, và giữ tổng đó dưới một trần nhỏ cố
> định cho mỗi khách, nên phần do tắc đường không tiêu vào trần.

(Vế "bộ điều phối được dời giờ trả tới sát hạn" và "tắc đường làm hẹp khoảng còn lại" là người nhận xét đọc ra từ mô tả
công thức 7 ở dòng 155–157, chưa kiểm với bài.)

---

## Phần 2. Giảng viên chấm

### A. Công trình liên quan có công bằng và cụ thể không

| Công trình | Chương nói gì | Đánh giá |
|---|---|---|
| Alonso-Mora và cộng sự 2017 | Lô 30 giây, đồ thị yêu cầu–chuyến–xe, quy hoạch nguyên, chi phí tính cả khách đang trên xe; giữ giờ đón (2.3) | Cụ thể, công bằng. Dòng 58–59 nói chung "không định giá việc sửa lời hứa", trong khi mục 2.3 cho thấy họ có giữ giờ đón. Nên nói rõ "giờ trả". |
| Molenbruch và cộng sự 2017 | Định nghĩa DARP; giới hạn thời gian ngồi xe theo tỉ lệ | Đủ cho vai trò định nghĩa; ô trong Bảng 2.1 khó hiểu (mục 18). |
| Fielbaum và Alonso-Mora 2020 | Phân loại nguồn, chỉ số, dữ liệu, hơn một phần ba, mục 6 với số | Phần cụ thể nhất chương. Lời phê "thước đo đầu–cuối bỏ sót lần dời rồi kéo về" công bằng vì đã nhắc họ có đếm số lần tăng. Thiếu đơn vị của 9,56 và 11,6. |
| Elmi và cộng sự 2026 | Độ chùng, điểm đi chung, 29%, 83,9%, thời gian đi cố định | **Chưa đủ để hiểu họ làm gì**: không định nghĩa điểm, không có con số của cách so sánh. Ô "Ghi riêng cho từng khách? Không" chưa công bằng với một cách mà chính tên dòng là "Bảo đảm theo từng khách". |
| Lu và Kühnel 2024 | Đệm giờ đón 2–3 phút | Quá ngắn; chỉ là nhãn. |
| Schulz và Pfeiffer 2026 | Hạn chót = lời mời + 900 giây; 10–15 phút hợp lý | Cụ thể. Ô bảng "khi thời gian đi đổi thì có" là suy luận về bài của họ (xem E). Chương chưa nói luật hạn chót dùng làm đối chứng chỉ lấy phần hạn chót, ở mức trần nhỏ hơn nhiều (OUTLINE mục 3.4 ghi 30–60 giây thay cho 900 giây). |
| Laupichler và cộng sự 2026 (Mt-KaRRi) | 1,4 lần + 10 phút | Quá ngắn; tên chưa giải thích. |
| Hörl và Zwick 2022 | Công thức 7, 8, ràng buộc 9–10, phạt 11; MATSim, MOIA; tốc độ cập nhật mỗi 60 phút; kết luận về ước lượng thấp | Chi tiết về công thức nhất nhưng **tự mâu thuẫn** (dòng 156 với 158) và gần như không có kết quả định lượng; câu kết "tác động này nhỏ" không rõ điều kiện. Vì đây là công trình gần nhất, đây là lỗi nặng nhất của chương. |
| FleetPy (Engelhardt và cộng sự 2026) | Dùng thuật toán Alonso-Mora; tuần dữ liệu; hệ số theo giờ và theo 15 phút | Đủ. |
| Hu và cộng sự 2022 (DeeprETA) | Công dụng, đặc trưng, phân vị | Cụ thể; câu quá dài. |
| Leonardi và cộng sự 2024 | Khoảng đúng hơn 90%; tiêu chí định quy mô | Cụ thể nhưng câu khó đọc; không rõ "chuyến quan sát trong mô phỏng" là dữ liệu thật hay mô phỏng. |
| TLC | Công bố theo tháng, trễ khoảng hai tháng | Có nguồn (theo ghi chú của người viết, trang TLC đọc 2026-10-12) nhưng cần ghi ngày truy cập; trang hiện nay không chứng minh lịch công bố năm 2018. |
| Wardman và cộng sự 2026 | 2,53 và 3,12 | Cụ thể; thiếu tên hai cách hỏi. |
| Alonso-González và cộng sự 2020 | 1.006 người, tỉ số khoảng 0,5 | Cụ thể; thiếu định nghĩa giá trị độ tin cậy. |
| Yu và cộng sự 2022 | 1.425.745 chuyến; chỉ đọc tóm tắt | Trung thực (có chú thích), nhưng mỏng. Hoặc đọc toàn văn, hoặc giữ đúng lời tóm tắt và ghi "theo tóm tắt". |

Nhận xét chung: phần lớn công trình được kể bằng việc họ đã làm và con số, không chỉ bằng nhãn. Ba chỗ còn ở mức nhãn: Lu
và Kühnel, Mt-KaRRi, điểm đi chung của Elmi. Một chỗ sai lệch nội tại: Hörl và Zwick.

Giảng viên có thể hỏi thêm vì sao không có các hướng như ổn định kế hoạch khi tối ưu cuốn chiếu, hay phạt độ khác biệt giữa
tuyến mới và tuyến cũ. Khóa luận không nhận các ý đó là mới, nhưng chương không nói đã tìm tài liệu thế nào và vì sao
chọn các bài này (xem câu hỏi 8).

### B. Định vị và tuyên bố mới

- **Không có tuyên bố mới quá mức.** Không có "duy nhất", "đầu tiên" trong văn xuôi (đã tìm bằng grep). Dòng 210–211 và
  228–229 nói rõ bảo vệ từng khách, giới hạn giờ đến, chèn khách động, chuyển xe và lời hứa theo dự báo đều đã có.
- **Phạm vi hẹp, nhưng phần "khác ở đâu" chỉ nằm ở hai cột cuối Bảng 2.2 và một câu 58 tiếng (dòng 206–208).** Người chấm
  phải tự rút ra. Nên có một câu định vị có giới hạn phạm vi, dạng: «Trong các nghiên cứu ở Bảng 2.2, không ràng buộc nào
  cộng độ lớn phần dời do điều phối qua cả chuyến cho từng khách; khóa luận đặc tả, cài đặt và đo một ràng buộc như vậy.»
  Câu này chỉ nói về các bài trong bảng, không nói "chưa ai làm".
- "Gần luật C nhất" (dòng 153) là một đánh giá; nên giới hạn: «Trong các nghiên cứu ở Bảng 2.2, gần luật C nhất là …».
- "Luật C dùng lại mốc giờ trả cập nhật của Hörl và Zwick" (dòng 206) chỉ đúng nếu mốc của họ là giờ trả trên tuyến đang
  gán. Nếu dòng 158 mới đúng ("mức sớm nhất có thể"), câu định vị phải sửa theo.

### C. Bảng 2.1 và Bảng 2.2

**Bảng 2.1.** Cấu trúc tốt, đúng mẫu DACN (có cột "Ý nghĩa"), chú thích trung thực ("không phải chuẩn ngành", "không so
trực tiếp được"). Cần sửa: đơn vị lẫn phút và giây; ô Molenbruch khó hiểu; "độ vòng tương đối 40%" chưa định nghĩa; "8 xe
mỗi kịch bản" không phải sức chứa; "phương án" trong chú thích là thuật ngữ của RideBound, không phải của các bài trước.
Đoạn đọc bảng (dòng 96–97) không nói điều người đọc nên thấy. Một điều người chấm sẽ thấy ngay: cửa sổ đón 10 phút rộng
hơn mọi giá trị đã trích (2–8 phút).

**Bảng 2.2.** Ý tưởng so sánh theo năm câu hỏi tốt và đúng quy tắc 29 (xếp theo cách tiếp cận). Vấn đề:
1. Tiêu đề cột 5 "Cộng qua cả chuyến?" mâu thuẫn với dòng 208 (cộng có dấu thì ra hạn chót); chú thích phải gỡ bằng một
   định nghĩa riêng cho chữ "Không".
2. Tiêu đề cột 6 "Ghi riêng cho từng khách?" mâu thuẫn với dòng "Bảo đảm theo từng khách" (Elmi).
3. Ô Schulz–Pfeiffer cột 3 là suy luận của người viết, không đánh dấu.
4. Tên dòng Hörl–Zwick mang số hiệu công thức; ô "Áp cho ai" trộn "khi nào".
5. Giá trị mức giới hạn đặt không thống nhất: 900 giây ở cột 2 cho Schulz–Pfeiffer, 1,4 lần + 10 phút ở cột 2 cho Mt-KaRRi,
   nhưng dòng luật C không ghi mức trần.
6. Sáu cột chữ dài ở cỡ `\footnotesize` với cột rộng 2,3–2,7 cm sẽ rất chật; ô dài nhất khoảng 20 tiếng.
7. Không có câu đọc bảng ngay sau bảng (quy tắc 20).
8. Bảng thiếu cách kiểm soát ở mục 6 của Fielbaum và Alonso-Mora (giữ thời gian chờ không vượt giá trị dự kiến), dù đó
   cũng là một dạng ràng buộc lời hứa. OUTLINE không đòi dòng này; có thể thêm hoặc nói một câu vì sao bỏ.

### D. Lý thuyết có được tách khỏi phần RideBound dùng không

Phần lớn có. Mục 2.1 (dòng 62–66 và Bảng 2.1), 2.2 (dòng 131–136), 2.3 (dòng 206–211), 2.5 (dòng 261–264) đều để phần
RideBound ở cuối mục. Ba chỗ chưa tách:
- Dòng 134–136 đưa một kết quả của Chương 4 (1 mili giây) vào chương cơ sở.
- Dòng 232 nêu một quy tắc thiết kế của RideBound ("chỉ được dùng thông tin có trước lúc hứa") như một nguyên lý chung;
  nên viết «Trong khóa luận, dự báo dùng cho lời hứa chỉ dùng …».
- Mục 2.4, đoạn dòng 238–244 trộn mô tả dữ liệu FleetPy với cách khóa luận dùng nó và lời cảnh báo về kết quả Chương 4.
  Nên tách thành câu về FleetPy rồi một câu bắt đầu bằng «Khóa luận dùng …».

### E. Suy luận của người viết trình bày như sự thật

| Dòng | Câu | Vì sao | Sửa |
|---|---|---|---|
| 57–58 | «một khách vì thế có thể bị dời giờ trả nhiều lần» | Chú thích EV ghi là suy luận từ định nghĩa; văn bản không nói vậy | Mở bằng «Suy từ định nghĩa này, …» (mục 13) |
| 135–136 | «nên khác biệt này nằm ở định nghĩa, chưa thấy ở kết quả» | Suy từ một kết quả Chương 4 | Thay đổi B5 |
| 158 | «nên thuật toán không rơi vào tình huống hết thứ tự trả khách khả thi» | Quan hệ nhân quả không gắn với tác giả | Thay đổi B1 («theo các tác giả, …») |
| 185 | Ô bảng «khi thời gian đi đổi thì có» (Schulz–Pfeiffer) | Bài dùng thời gian đi cho trước; vế sau là suy luận | Thay đổi B3 («(suy từ định nghĩa)») |
| 189 | Ô bảng «nên riêng tắc đường không làm tuyến bị loại» | Đọc ra từ công thức, chưa rõ là lời của bài hay của người viết | Ghi «(đọc từ công thức 7)» hoặc trích trang |
| 223 | «Dự báo giờ đến từ dữ liệu là thực hành của các nền tảng gọi xe» | Khái quát cho "các nền tảng" từ một hãng | Mục 56 |
| 233–234 | «được công bố theo tháng, thường trễ khoảng hai tháng» (TLC; chính người viết đã đánh dấu) | Có nguồn là trang TLC, nhưng trang đọc năm 2026 không chứng minh lịch năm 2018; "thường" là lời rào không có nguồn | Thay đổi N2: ghi ngày truy cập, bỏ "thường" |
| 234–235 | «… vì vậy giả định hãng xe có sẵn dữ liệu chuyến của chính mình» | Suy luận của người viết (EV ghi rõ) viết như hệ quả | Thay đổi N2: «khóa luận giả định …» |
| 242–244 | «nên được đọc như mức trần cho loại dự báo theo giờ trong ngày» | "Cận trên" chưa được chứng minh; có lý do để nghĩ kết quả lạc quan, không phải là cận trên | Thay đổi B4 |
| 262–263 | «chưa có chuẩn ngành cho loại trần này» | Khẳng định về sự vắng mặt, không có phạm vi tìm | Thay đổi N2: «khóa luận chưa tìm thấy …» |

### F. "Duy nhất", "đầu tiên", từ nhân quả và từ bảo đảm

- "Duy nhất", "đầu tiên": không có trong văn xuôi.
- So sánh nhất mang tính đánh giá: «Gần luật C nhất» (dòng 153); nên giới hạn phạm vi (mục B).
- Từ bảo đảm: «bảo đảm» ở dòng 126, 127 và tên dòng Bảng 2.2 đều nói về cách của Elmi và cộng sự, đúng chủ thể, và dòng 128
  đã nêu điều kiện (thời gian đi không đổi). Không có câu nào bảo đảm thay cho luật C. Tốt.
- Từ nhân quả: dòng 158 «nên thuật toán không rơi vào …» (chưa gắn tác giả); dòng 189 «nên riêng tắc đường không làm tuyến
  bị loại»; dòng 257 «ảnh hưởng tới việc khách bỏ yêu cầu» (lấy từ tóm tắt, nên ghi «theo tóm tắt»); dòng 56 «vì ghép
  thêm khách làm độ trễ … tăng» (đúng theo định nghĩa, chấp nhận được).

### G. Thuật ngữ lệch Chương 3

| Chương 2 | Chương 3 (dòng 1–150) | Sửa |
|---|---|---|
| Công thức (2.1): $k$ là yêu cầu, $j$ là xe | Công thức (3.1): $k$ là xe, $u$ là yêu cầu mới | Ghi «ký hiệu theo bài gốc» ở 2.1, hoặc đổi chỉ số ở 2.1 |
| «khách đã nhận không được chuyển sang xe khác» (dòng 65) | Khóa áp từ lúc khách **xác nhận đặt xe** (dòng 78–79); "được nhận" là lúc khách được mời, chưa có lời hứa | «Khách đã xác nhận đặt xe không bị chuyển sang xe khác» |
| «thay cho một tổng chi phí» (dòng 65) | Bảng 3.2: tổng chi phí kế hoạch là tiêu chí 4 | «tổng chi phí chỉ là một tiêu chí xếp sau» |
| «kịch bản kiểm soát hoàn toàn», «kịch bản trung gian» (dòng 117, 120) | Kịch bản = một ngày, một mẫu nhu cầu, một khung 2 giờ | «mức kiểm soát …» |
| «phần thay đổi do quyết định của hãng xe» (dòng 133) | «phần dời do điều phối» | Dùng tên của Chương 3 |
| «mức trần» = cận trên (dòng 243) | «Trần $B$» | Bỏ chữ "trần" ở nghĩa cận trên |
| «600 giây kể từ lúc gọi» (Bảng 2.1) | «Đón trong vòng 10 phút kể từ lúc gọi» (Bảng 3.2) | «10 phút (600 giây)» |
| «quy hoạch nguyên (integer linear program)» | «quy hoạch nguyên» | Cả hai chương nên là «quy hoạch tuyến tính nguyên» nếu giữ tên Anh này |
| «độ trễ» (độ trễ so với đi thẳng, theo Alonso-Mora) | Các chương sau dùng «trễ» so với lời hứa đầu | Thêm một câu ở dòng 51–52: «độ trễ theo nghĩa này khác với trễ so với lời hứa ở Chương 4» |
| «hạn chót tính từ lời hứa đầu» (dòng 209) | OUTLINE quy định tên trong văn xuôi là «luật hạn chót» | Kiểm với tên ở Bảng 3.3 và dùng một tên |

### H. Độ dài (ước lượng, cần đo trên PDF)

Theo mức 330 tiếng một trang của WRITING-BRIEF, 2.584 tiếng văn xuôi tương đương khoảng 7,8 trang, chưa kể hai bảng (khoảng
1,5 trang) và một công thức. Ngân sách của OUTLINE là 6,5 trang. Chênh lớn nhất ở mục 2.2 (598 tiếng so với ngân sách 1,25
trang, khoảng 410 tiếng), 2.4 (448 so với khoảng 330) và 2.5 (276 so với khoảng 165). Ghi chú đầu tệp nói bản 3 đã rút cho
vừa 6,5 trang; nếu người viết đã đo trên PDF thì bỏ qua mục này. Các đề xuất tách câu ở Phần 1 làm văn bản dài thêm chút
ít; chỗ có thể cắt mà không mất ý: chi tiết mạng đường của Fielbaum và Alonso-Mora (số nút, số đoạn đường), số hiệu công
thức của Hörl và Zwick trong bảng, và câu về DeeprETA dùng những đặc trưng nào.

### I. Tám câu hỏi giảng viên sẽ hỏi

1. Hạn trả được nới của Hörl và Zwick bằng giờ trả cập nhật trên tuyến đang gán hay bằng giờ trả sớm nhất có thể? Cho một
   ví dụ số trong đó luật C và công thức 7 của họ chọn khác nhau. Với khách đã trễ quá giờ trả muộn nhất, hạn của họ có
   tương đương luật C với trần 0 không?
2. Vì sao phần dời do điều phối phải so với giờ trả khi giữ nguyên kế hoạch, thay vì so với lời hứa đã báo gần nhất? Vì sao
   cộng độ lớn, tức tính cả lần kéo giờ trả về sớm? Chính chương nói các lần kéo sớm chỉ là 1 mili giây; vậy cộng dồn độ
   lớn đem lại gì so với giới hạn từng lần?
3. Elmi và cộng sự đặt độ chùng riêng cho từng khách. Luật C có khác gì một độ chùng 30 giây cho mọi khách, ngoài cách ghi
   sổ? Vì sao Bảng 2.2 ghi "Không" ở cột "Ghi riêng cho từng khách" cho một dòng tên là "Bảo đảm theo từng khách"?
4. Luật hạn chót dùng làm đối chứng có phải là phương pháp của Schulz và Pfeiffer không? Họ dùng độ chùng 900 giây và thấy
   10–15 phút hợp lý; so một luật hạn chót 30–60 giây với luật C có công bằng không?
5. Cửa sổ đón của khóa luận là 10 phút, rộng hơn mọi giá trị trong Bảng 2.1 (2–8 phút). Vì sao chọn mức này, và nó ảnh
   hưởng thế nào tới giá của trần?
6. Hệ số tắc đường chung cho cả thành phố, không nhiễu ngẫu nhiên: vì sao chấp nhận được, và vì sao gọi kết quả dự báo là
   "mức trần"? Đã thử thêm nhiễu chưa?
7. Theo Alonso-González và cộng sự, khoản trễ nhỏ không báo trước bị coi nhẹ (tỉ số khoảng 0,5). Vậy trần 30 giây có nghĩa
   gì với khách? Vì sao trích Yu và cộng sự khi chỉ đọc tóm tắt?
8. Các bài trong chương được tìm và chọn thế nào (từ khóa, cơ sở dữ liệu, thời điểm)? Vì sao không bàn các hướng ổn định kế
   hoạch khi tối ưu cuốn chiếu hay phạt khác biệt giữa tuyến mới và tuyến cũ?

---

## Thay đổi xếp hạng

Ký hiệu: **B** = bắt buộc, **N** = nên. Văn bản thay thế viết ở dạng dán vào LaTeX. Chỗ **[kiểm với bài]** và
**[bổ sung: …]** người viết phải điền từ nguồn trước khi dán; không được tự đoán.

### B1. Viết lại đoạn Hörl và Zwick (dòng 153–160)

Lý do: công trình gần nhất được mô tả tự mâu thuẫn (dòng 156 nói hạn nới tới "giờ trả cập nhật", dòng 158 nói "mức sớm nhất
có thể"), ba tên mới trong một câu 64 tiếng, "giờ trả muộn nhất" chưa định nghĩa, quan hệ nhân quả không gắn tác giả, câu
kết mơ hồ. Ghi chú cho người viết: lập luận "luôn còn ít nhất một thứ tự trả khách" chỉ hiển nhiên đúng nếu hạn được nới tới
giờ trả trên tuyến đang gán (vì tuyến đang gán luôn thỏa hạn đó); với "mức sớm nhất có thể" thì không hiển nhiên khi xe chở
nhiều khách. Đây là suy luận của người nhận xét; hãy mở bài, tr. 7–8 để chọn.

Thay toàn bộ dòng 153–160 bằng:

```
Trong các nghiên cứu ở Bảng~\ref{bang:c2-dangrangbuoc}, gần luật C nhất là cách Hörl và Zwick~\cite{horl2022} xử lý
thời gian đi thay đổi. Họ thử cách này trong bộ mô phỏng giao thông MATSim, với nhu cầu lấy từ dịch vụ đi chung xe MOIA
ở Hamburg. Mỗi khách có một giờ trả muộn nhất, tức giờ trả không được vượt khi khách được nhận [kiểm với bài: cách tính].
Ở đầu mỗi lượt, họ tính lại giờ trả dọc theo tuyến đang gán bằng thời gian đi hiện tại; kết quả gọi là giờ trả cập nhật.
Theo công thức 7 của bài, hạn trả của mỗi khách trên xe đang xét là giờ muộn hơn trong hai giờ: giờ trả muộn nhất và giờ
trả cập nhật. Tuyến mới phải thỏa hạn này như một ràng buộc cứng, còn mỗi giây trả muộn hơn giờ trả muộn nhất ban đầu bị
phạt trong hàm mục tiêu. Xe vẫn được đón thêm khách, miễn là giờ trả mới của khách trên xe không vượt hạn đó; theo các
tác giả, nhờ hạn được nới như vậy, bài toán luôn còn ít nhất một thứ tự trả khách thỏa ràng buộc. Giờ đón được xử lý
tương tự (công thức 8). Bài kết luận rằng khi thời gian đi bị ước lượng thấp, hãng xe phải chọn giữa từ chối khách đã
nhận và trả khách muộn hơn giờ đã báo; còn khi [kiểm với bài, tr. 14: điều kiện], ảnh hưởng này nhỏ.
```

Nếu bài nói hạn được nới tới "giờ trả sớm nhất có thể với tắc đường hiện tại" thì thay cụm «giờ trả cập nhật» trong câu
công thức 7 bằng cụm đó, và sửa theo dòng 206 (B2) cùng dòng Hörl–Zwick của Bảng 2.2 (B3).

### B2. Viết lại đoạn định vị luật C (dòng 206–211)

Lý do: đây là câu trả lời cho "khóa luận khác ở đâu", hiện là một câu 58 tiếng năm ý và một câu dùng ba thuật ngữ chưa giải
thích; "không nới theo tắc đường" mâu thuẫn bề ngoài với mốc so sánh có đổi theo tắc đường. Câu "trong phần còn lại …" đọc
ra từ công thức 7 như mô tả ở B1; kiểm lại khi kiểm B1.

Thay dòng 206–211 bằng:

```
Luật C dùng lại ý giờ trả cập nhật của Hörl và Zwick: mốc so sánh là giờ trả nếu xe giữ nguyên kế hoạch, tính lại ở mỗi
lượt. Chỗ khác là đại lượng bị giới hạn. Hörl và Zwick giới hạn chính giờ trả và nới hạn khi tắc đường đã đẩy giờ cập
nhật quá giờ trả muộn nhất; trong khoảng còn lại tới giờ trả muộn nhất, bộ điều phối vẫn được dời giờ trả để ghép khách.
Luật C không đặt hạn cho giờ trả mà cộng độ lớn mọi lần bộ điều phối dời giờ trả so với mốc đó, qua cả chuyến, và giữ
tổng này dưới cùng một trần cho mọi khách đã xác nhận đặt xe. Phần do tắc đường không bị tính vào trần, nên trần không
đổi khi đường đông lên; phần trần đã dùng được ghi vào sổ của từng khách (mục~\ref{muc:luatc}).

Hai cách cộng khác cho ra hai luật dùng để so sánh (mục~\ref{muc:doichung}). Nếu cộng cả phần dời do điều phối lẫn phần
thay đổi khi xe giữ nguyên kế hoạch, và để các lần dời sớm, dời muộn bù trừ nhau, thì tổng bằng giờ trả mới trừ lời hứa
đầu; giới hạn tổng này chính là một hạn chót tính từ lời hứa đầu. Nếu cộng độ lớn mọi thay đổi khách thấy, gồm cả phần do
tắc đường, thì được luật trần độ dời khách thấy. Bảo vệ từng khách, giới hạn giờ đến, chèn khách động và chuyển khách
sang xe khác đều đã có ở các nghiên cứu trên, nên khóa luận không nhận các ý đó là mới.
```

### B3. Sửa Bảng 2.2 cho khỏi tự mâu thuẫn và công bằng với Elmi và cộng sự (dòng 165–204)

Lý do: tiêu đề cột 5 mâu thuẫn với dòng 208; tiêu đề cột 6 mâu thuẫn với tên dòng Elmi; ô Schulz–Pfeiffer là suy luận
không đánh dấu; tên dòng Hörl–Zwick mang số hiệu công thức; không có câu đọc bảng.

- Tiêu đề cột 5: `\textbf{Cộng độ lớn các lần sửa qua cả chuyến?}`
- Tiêu đề cột 6: `\textbf{Có sổ ghi phần đã dùng của từng khách?}`
- Chú thích bảng, thay câu thứ hai: «"Không" ở cột năm nghĩa là ràng buộc so một giờ với một mốc; các lần sửa sớm, muộn có
  thể bù trừ nhau.»
- Dòng Schulz–Pfeiffer, cột 3: `Bài dùng thời gian đi cho trước, nên không xét; nếu thời gian đi đổi, phần do tắc đường
  sẽ bị tính (suy từ định nghĩa)`
- Dòng Hörl–Zwick, cột 1: `Hạn trả được nới theo giờ trả cập nhật~\cite{horl2022}`; cột 4: `Khách trên xe đang xét`;
  cột 3: `Hạn được nới tới giờ cập nhật khi giờ này đã vượt hạn, nên riêng tắc đường không làm tuyến bị loại (đọc từ
  công thức 7)`
- Dòng Elmi, cột 6: `Không; mỗi khách có độ chùng riêng, so với một giới hạn cố định`
- Dòng luật C, cột 2: `Giờ trả nếu xe giữ nguyên kế hoạch, tính lại ở mỗi lượt; trần chung, ví dụ 30 giây`
- Thêm ngay sau bảng một câu đọc bảng: «Ở ba cột đầu, luật C gần nhất với hạn trả được nới của Hörl và Zwick: cả hai so
  với giờ trả tính lại ở mỗi lượt và không để riêng tắc đường làm tuyến bị loại. Chỗ khác nằm ở hai cột cuối: luật C cộng
  độ lớn các lần dời do điều phối qua cả chuyến và ghi phần đã dùng vào sổ của từng khách.»

### B4. Bỏ "mức trần" ở dòng 242–244

Lý do: "trần" là trần B của luật C trong cả khóa luận; ở đây lại mang nghĩa cận trên, và "cận trên" là khẳng định chưa
được chứng minh. Có lý do để nghĩ kết quả lạc quan, nhưng không đủ để gọi là cận trên.

Thay dòng 242–244 («Vì cả thành phố … không phải hiệu quả ngoài đời.») bằng:

```
Vì cả thành phố dùng một hệ số và mô phỏng không có nhiễu ngẫu nhiên, thời gian đi trong mô phỏng có thể dễ dự báo hơn
ngoài đời. Kết quả của lời hứa theo dự báo ở Chương~\ref{chuong:thucnghiem} vì vậy có thể lạc quan hơn khi áp dụng thật,
và không được đọc như hiệu quả ngoài đời.
```

### B5. Viết lại câu "1 mili giây" (dòng 134–136)

Lý do: câu khó nhất chương với người đọc ngoài ngành; dùng "tập kiểm tra chính" chưa định nghĩa; "khác biệt này" không rõ;
đưa kết quả Chương 4 vào chương cơ sở mà không giải thích vì sao một lần dời lại đúng 1 mili giây. Trước khi dán, người viết
kiểm hai điều: (a) "mỗi lần" có đúng cho mọi luật trên tập kiểm tra chính không; (b) 1 mili giây có phải do làm tròn
số không; nếu có, nói rõ ở Chương 3 hoặc 4.

Thay dòng 134–136 («Trên tập kiểm tra chính … chưa thấy ở kết quả.») bằng:

```
Trên tập kiểm tra chính (Chương~\ref{chuong:thucnghiem}), mỗi lần điều phối kéo giờ trả sớm hơn chỉ sớm 1 mili giây, nên
tình huống dời muộn rồi kéo về như ví dụ trên gần như không xảy ra. Vì vậy, khác biệt giữa hai cách đo hiện mới nằm ở
định nghĩa, chưa thể hiện trong kết quả.
```

### N1. Thêm một ví dụ dựng tay sau đoạn B2

Lý do: người đọc ngoài ngành chỉ hiểu được Bảng 2.2 khi có một khách cụ thể; DACN luôn có ví dụ ngay sau quy tắc. Ví dụ
dưới đây do người nhận xét dựng, dùng đúng các định nghĩa trong chính chương (công thức 7 như mô tả ở B1; hạn chót tính từ
lời hứa đầu; luật C). Giờ chọn khác ví dụ 9:10 của Chương 3 để khỏi lẫn. Có thể đổi lấy việc cắt số hiệu công thức và chi
tiết mạng đường ở mục 2.2 cho đủ trang.

```
Ví dụ dựng tay sau cho thấy chỗ khác nhau. Khách A được hứa trả lúc 8:30:00, giờ trả muộn nhất là 8:35:00. Ở một lượt,
tắc đường làm giờ trả khi giữ nguyên kế hoạch thành 8:32:00, và ghép khách B làm giờ trả của A thành 8:32:20. Ở lượt sau,
giờ trả khi giữ nguyên là 8:32:20, và ghép thêm khách C làm giờ trả thành 8:32:40. Với hạn trả được nới của Hörl và Zwick,
hạn của A vẫn là 8:35:00, nên cả hai lần ghép đều hợp lệ. Với hạn chót bằng lời hứa đầu cộng 30 giây, hạn là 8:30:30, nên
ngay ở lượt đầu mọi phương án, kể cả giữ nguyên kế hoạch, đều vượt hạn chỉ vì tắc đường. Với luật C trần 30 giây, lần
ghép B dùng 20 giây của trần; lần ghép C cần thêm 20 giây, tổng 40 giây vượt trần nên phương án này bị loại. Hai phút do
tắc đường không bị tính vào trần.
```

### N2. Đánh dấu các suy luận còn lại (dòng 233–235 và 262–264)

Lý do: câu TLC có nguồn nhưng thiếu ngày truy cập và có lời rào "thường" không có nguồn; câu tiếp theo là suy luận của
người viết viết như hệ quả; "chưa có chuẩn ngành" là khẳng định về sự vắng mặt.

Thay dòng 233–235 («Dữ liệu chuyến công khai … của chính mình.») bằng:

```
Theo trang dữ liệu của Ủy ban Taxi và Xe limousine New York (Taxi \& Limousine Commission, TLC), truy cập ngày
12/10/2026, dữ liệu chuyến công khai được công bố theo tháng, trễ khoảng hai tháng~\cite{tlc}. Vì dữ liệu công khai đến
muộn như vậy, cách lập hồ sơ từ các ngày ngay trước ở mục~\ref{muc:dubao} chỉ dùng được nếu hãng xe có dữ liệu chuyến
của chính mình; khóa luận giả định điều này.
```

Thay dòng 262–264 («Không kết quả nào … ngưỡng khách cảm nhận được.») bằng:

```
Không kết quả nào trong ba kết quả trên cho phép quy trần 30 giây, mức trần chính của khóa luận cho phần dời giờ trả do
điều phối, ra thành tiền, và khóa luận chưa tìm thấy chuẩn ngành nào cho loại trần này. Vì vậy, mỗi mức trần được coi là
một điểm trên đường đánh đổi giữa số khách được phục vụ và độ ổn định của lời hứa, không phải ngưỡng mà khách cảm nhận
được.
```

Đồng thời sửa dòng 57–58 theo mục 13 của Phần 1 (mở bằng «Suy từ định nghĩa này, …»).

### N3. Đoạn mục 6 của Fielbaum và Alonso-Mora (dòng 117–121)

Lý do: "kịch bản" trùng nghĩa với "kịch bản" của Chương 3; câu 56 tiếng bốn con số; "còn 31,2%" không nói so với gì; thiếu
đơn vị của chi phí.

Thay dòng 117–121 bằng:

```
Ở mục 6 của bài, các tác giả đưa việc kiểm soát độ bất ổn vào chính bước gán xe. Ở mức kiểm soát hoàn toàn, khách đã được
gán không bị từ chối về sau, và thời gian chờ của khách không được vượt giá trị dự kiến lúc gán. Đổi lại, tỉ lệ yêu cầu
bị từ chối tăng từ 34,5\% lên 45,6\%, và chi phí trung bình của mỗi khách, tính theo hàm chi phí của bài, tăng từ 9,56
lên 11,6 [bổ sung: đơn vị]. Ở mức trung gian, bộ điều phối chỉ bị cấm từ chối khách đã nhận. Tỉ lệ từ chối khi đó là
31,2\%, thấp hơn mức 34,5\% khi không kiểm soát, nhưng thời gian chờ và độ vòng của khách được nhận tăng khoảng 50\%. Các
tác giả kết luận có đánh đổi giữa độ tin cậy và các chỉ số chất lượng khác, và để ngỏ câu hỏi làm sao kiểm soát độ bất
ổn mà không làm tăng số yêu cầu bị từ chối.
```

### N4. Mục 2.1: ký hiệu công thức và đoạn RideBound (dòng 40–53 và 62–66)

Lý do: `c_{\mathrm{ko}}` đọc như "ko" trong tin nhắn; "với" không phải cách nói "thỏa"; chỉ số $k$ lệch Chương 3; "bước chọn",
"phương án", "bộ chọn", "thứ tự tiêu chí" dùng trước khi giải thích; "thay cho một tổng chi phí" lệch Bảng 3.2; "khách đã
nhận" lệch mốc "xác nhận đặt xe" của Chương 3.

- Dòng 40: `Bước thứ hai, bước chọn, chọn chuyến cho từng xe bằng một bài toán quy hoạch tuyến tính nguyên (integer linear
  program).`
- Công thức (2.1): thay `c_{\mathrm{ko}}` bằng `c_{k0}` (cả trong câu "Trong đó") và `\quad\text{với}\quad` bằng
  `\quad\text{thỏa}\quad`. Cuối câu "Trong đó" thêm: `Ký hiệu ở đây theo bài gốc; Chương~\ref{chuong:phuongphap} dùng
  ký hiệu riêng.`
- Thay dòng 62–66 bằng:

```
RideBound giữ bước chọn theo lối này nhưng không dựng đồ thị yêu cầu--chuyến--xe. Với mỗi xe, bộ sinh chỉ chèn thêm
(insertion-only generator) tạo ra các phương án, tức các kế hoạch (dãy điểm đón, điểm trả theo thứ tự) có thể chọn cho
xe: một phương án giữ nguyên kế hoạch cũ, và các phương án chèn điểm đón, điểm trả của yêu cầu mới vào kế hoạch cũ mà
không bỏ hay đổi thứ tự các điểm cũ. Bộ chọn (selector) chọn cho mỗi xe đúng một phương án. Bộ chọn không gộp mọi thứ vào
một tổng chi phí mà so các tiêu chí theo thứ tự: chỉ khi hai phương án hòa ở tiêu chí trước mới xét tiêu chí sau, và tổng
chi phí là một tiêu chí xếp sau (mục~\ref{muc:baitoan-phatbieu}). Khách đã xác nhận đặt xe không bị chuyển sang xe khác.
Bảng~\ref{bang:c2-dichvu} đặt các ràng buộc dịch vụ trong tập thử của khóa luận cạnh cách đặt ở các nghiên cứu trên.
```

### N5. Đoạn Elmi và cộng sự (dòng 124–128)

Lý do: một trong bốn công trình gần nhất nhưng điểm "khả năng đi chung" không được định nghĩa và phép so 83,9% không có vế
đối; người đọc không biết họ đã làm gì. Hai chỗ **[bổ sung]** phải lấy từ bài (tr. 12–13 theo ghi chú EV), không được
đoán.

Thay dòng 124–128 bằng:

```
Elmi và cộng sự~\cite{elmi2026} tiếp tục hướng này, nhưng đặt mức kiểm soát riêng cho từng khách. Độ chùng (slack) của
một khách là khoảng còn lại giữa giới hạn và giá trị dự kiến lúc gán, tính riêng cho thời gian chờ và cho độ trễ; đó là
phần mà về sau bộ điều phối còn được phép làm xấu đi. Bài tính cho mỗi khách một điểm khả năng đi chung [bổ sung: cách
tính, một câu]. Khách có điểm thấp nhận độ chùng 0, tức được bảo đảm không bị đổi giờ; khách khác giữ toàn bộ độ chùng.
So với cách siết độ chùng đều cho mọi khách, ở cùng tỉ lệ từ chối 29\%, cách chọn theo điểm bảo đảm ngay lúc gán rằng
83,9\% số khách không bị đổi giờ [bổ sung: con số tương ứng của cách siết đều]. Bài giả định thời gian đi trên mỗi đoạn
đường không đổi và không xét độ bất ổn do giao thông.
```
