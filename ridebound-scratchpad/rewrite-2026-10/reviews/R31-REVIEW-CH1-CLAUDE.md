# R31. Chương 1 (bản v3 của Codex): người đọc ngoài ngành, giảng viên chấm, kiểm số

- **Tệp được nhận xét (chỉ đọc):** `S/optimize/codex-debate/codex-work/r30-ch1/05-chuong1-v3.tex` (273 dòng). Mọi số
  dòng "L…" dưới đây là số dòng của tệp này. Không đọc `05-chuong1.tex`, `-v2.tex`.
- **Ngữ cảnh đã đọc:** `ROUND30-CH1-WRITER.md`; `CODEX-PARALLEL-RULES.md`; `WRITING-BRIEF.md`; `OUTLINE-V2.md` §2, §5
  (Chương 1), §6; `style/STYLE-GUIDE-VI.md` (mục 0–4.5); `style/GLOSSARY-VI-v2.md`; báo cáo DACN, Chương 1 (trang PDF
  13–16, đọc bằng `pdftotext`); Chương 3 v3 (mở chương, dòng 1–40, 440–460).
- **Chỉ cho Phần 3:** `05-chuong1-NOTES.md`; sổ bằng chứng và phụ lục 1–6; `tang3/t38c120/C120-RESULTS.md`;
  Chương 4 phần A **v5-v3** (`codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex`, theo tin nhắn của điều phối viên; đã
  so với v4: các số Chương 1 dùng không đổi) và phần B v10. Mở thêm ba output gốc: `tang3/w07/analysis/q4-rider-2026-09-30.txt`,
  `optimize/report-extras/example-rider-2026-10-06.txt`, `tang3/w07/W07-REPORT.md:44-53`; và
  `codex-work/r32-bib/10-tai-lieu-draft-v2.tex`, `BIB-VERIFICATION-v2.md` để xem khóa trích dẫn đã có.
- **Đếm bằng script chỉ đọc** (`scratchpad/r31_ch1_sentlen.py`, bỏ dòng `%`, bảng, lệnh TikZ): bốn câu dài hơn 40 tiếng,
  cả bốn nằm trong đoạn đóng góp (50, 43, 52, 41 tiếng). Đoạn đóng góp dài 324 tiếng, chứa 28 cụm số (khoảng 24 con số
  khác nhau, không kể năm); OUTLINE §6.1 dự kiến 10 con số.
- **Quy ước:** câu trích bỏ `~\cite{…}`. Câu đề xuất ở Phần 1 giữ nguyên nghĩa và con số. Câu ở mục "Thay đổi xếp hạng"
  viết ở dạng dán thẳng vào LaTeX, kèm dòng `% EV:`.

## Nhận định chung (năm dòng)

1. **Số liệu sạch.** 0 số sai trong khoảng 80 số đã kiểm. Các vế bất lợi chính đã có: −96 lượt, 292 so với 289, cách đệm
   hòa ở một phút, 0/20.760 của điều phối không trần, phần cộng dồn chưa đo. Không có cụm từ cấm nào, kể cả trong dòng `%`.
2. **Chỗ hỏng lớn nhất về độ trung thực.** Câu "luật hạn chót … phá luật … ở 28 trong 34 kịch bản" (L208–209) ngụ ý
   luật C hơn luật hạn chót. Thực ra, đo bằng cùng thước, luật C cũng có khách tới muộn quá 30 giây ở 28/34 kịch bản
   (C4A-01; Ch4A v5-v3:357–358). Câu cũng không nói luật hạn chót ở đây chỉ đặt 30 giây, trong khi bài gốc dùng 900 giây.
   Thêm nữa, câu "+31 lượt" thiếu vế "−5 lượt ở ngưỡng hai phút".
3. **Khung "không nhận là mới" thiếu.** Khung chỉ có bảy mục bắt buộc của AGENTS.md cùng câu về giờ đến và kinh doanh. Nó
   thiếu lời hứa theo dự báo, mốc của Hörl–Zwick, bảo vệ từng khách, hạn chót từ lời mời, và đo/kiểm soát độ bất ổn. Nó
   cũng thiếu câu then chốt: "luật C không phục vụ nhiều hơn, không đúng giờ hơn".
4. **Người ngoài ngành không theo được.** Khoảng 15 thuật ngữ và tên riêng xuất hiện trước khi được giải thích:
   RideBound, FleetPy, trần, lời hứa đầu, luật hạn chót, sổ, tập kiểm tra chính, bị ép, (N), bản ghi chặn, cộng dồn…
   Khái niệm trung tâm, "phần tính cho điều phối", không có một ví dụ số nào.
5. **So với Hörl–Zwick chưa công bằng hẳn.** Mốc đo được ghi công đúng, nhưng chương không nói luật kiểu Hörl–Zwick chưa
   được chạy làm đối chứng. Chương cũng không nói khác biệt chỉ suy ra từ định nghĩa, và vế "không nới theo tắc đường"
   dễ được đọc thành "chặt hơn".

---

## Phần 1. Người đọc ngoài ngành

Vai: sinh viên năm cuối ngành khác, đọc Chương 1 từ đầu, chưa biết hệ thống.

**Nhận xét chung.**
- **Tiếng Anh.** Không có từ tiếng Anh trần trong câu. Chỉ có "(ride-pooling)" ở lần đầu, đúng quy tắc, và các tên
  riêng: UberX Share, MOIA Express, FleetPy, RideBound, Mt-KaRRi, Manhattan. Cái khó là **tên riêng chưa được giải
  thích**: RideBound, FleetPy và Mt-KaRRi không có một chữ nào nói chúng là gì.
- **Thuật ngữ đi trước định nghĩa.** "Sổ" xuất hiện ở L62 và L85 nhưng được định nghĩa ở L92. "Trần" xuất hiện ở L22,
  L29, L70 và L77 nhưng được định nghĩa ở L90. "Tập kiểm tra chính" xuất hiện ở L83 nhưng được định nghĩa ở L258.
  "Luật hạn chót" xuất hiện ở L124 và L208 nhưng không có định nghĩa nào trong chương.
- **Một khái niệm, nhiều tên** (trái quy tắc 11 của STYLE):
  - Phần do điều phối có sáu tên: "phần tính cho điều phối", "phần dời do điều phối", "các lần điều phối dời giờ trả",
    "độ dời giờ trả do điều phối", "trần điều phối", "các lần dời do điều phối".
  - Phần thay đổi khi giữ kế hoạch có năm tên: "phần thay đổi khi giữ kế hoạch", "phần giữ kế hoạch", "mốc giữ kế
    hoạch", "mốc tuyến cũ tính lại", "kế hoạch cũ tính lại ở cùng trạng thái".
  - Lời hứa theo dự báo có bốn tên: "lời hứa theo dự báo", "lời hứa có dự báo", "lời hứa theo hồ sơ lịch sử", "dự báo
    chính".
  - Các cặp tên khác: "tắc đường" và "giao thông"; "phá luật" và "phá lời hứa" (theo bảng thuật ngữ); "đúng giờ" và
    "không trễ quá một phút".
- **Đoạn đóng góp** (L203–216) là chỗ khó nhất: 324 tiếng, bốn câu trên 40 tiếng, khoảng 24 con số. Người đọc phải đọc
  hai lần và vẫn không giải nghĩa được "bị ép", "miễn trừ", "giả thiết (N)", "bản ghi chặn", "cộng dồn".

Tổng cộng **54 chỗ khó** (đánh số dưới đây). Với các chỗ đã có câu viết lại đầy đủ ở mục "Thay đổi xếp hạng", đề xuất
dưới đây trỏ sang đó (M1–M5, S6–S10).

### Đoạn mở chương

**1. L7–8.** «Chương này nêu vì sao giờ trả đã hứa với khách đi chung xe có thể bị dời, chia độ lệch đó thành ba phần và
chỉ ra chỗ khóa luận xử lý từng phần.»
- Vì sao: "độ lệch đó" không có tiền ngữ, vì câu chỉ vừa nói "bị dời", chưa nói lệch giữa cái gì với cái gì. "Giờ trả"
  được dùng lần đầu mà không giải thích.
- Đề xuất: «Chương này giải thích vì sao giờ trả đã hứa với khách đi chung xe, tức giờ khách được báo sẽ tới nơi, có thể
  bị dời; chia độ lệch giữa giờ tới thực tế và giờ đã hứa thành ba phần; và chỉ ra khóa luận xử lý mỗi phần ở đâu.»

### Mục 1.1

**2. L14.** «Trong dịch vụ đi chung xe (ride-pooling), bộ điều phối ghép các yêu cầu vào cùng một xe và cập nhật kế
hoạch khi có yêu cầu mới.»
- Vì sao: người ngoài ngành dễ hiểu "bộ điều phối" là người hay phòng ban. Theo bảng thuật ngữ, từ này cần tiếng Anh ở
  lần đầu.
- Đề xuất: «Trong dịch vụ đi chung xe (ride-pooling), một phần mềm gọi là bộ điều phối (dispatcher) xếp nhiều khách vào
  cùng một xe và sửa kế hoạch chạy của xe mỗi khi có yêu cầu mới.»

**3. L15–16.** «Giờ trả đã báo cho khách vì thế có thể đổi khi xe nhận thêm điểm dừng; ngay cả khi giữ nguyên kế hoạch,
thời gian đi thay đổi cũng có thể làm mốc giờ trả khác đi.»
- Vì sao:
  - "làm mốc giờ trả khác đi" là lối nói không tự nhiên.
  - Hai lẽ bị dồn vào một câu.
  - Câu sau dùng "lời hứa" mà chưa nối nó với "giờ trả đã báo".
  - "Lời hứa đầu" (L21) không được định nghĩa ở đâu trong chương.
- Đề xuất: «Vì vậy, giờ trả đã báo cho khách, gọi là lời hứa giờ trả hay gọn là lời hứa, có thể đổi vì hai lẽ. Xe có thể
  nhận thêm điểm dừng để đón, trả khách mới. Ngay cả khi xe giữ nguyên kế hoạch, đường đi nhanh hay chậm hơn lúc hứa
  cũng làm giờ tới thay đổi. Giờ trả báo lúc khách xác nhận đặt xe gọi là lời hứa đầu.»

**4. L16–17.** «Cần phân biệt hai phần này trước khi đặt giới hạn cho việc sửa lời hứa.»
- Vì sao: "hai phần này" trỏ về "hai lẽ" của câu trước, nhưng câu trước không gọi chúng là "phần".
- Đề xuất: «Muốn giới hạn việc sửa lời hứa thì trước hết phải tách được hai phần này.»

**5. L20–21.** «Khách ở hình trên trễ 307,3 giây so với lời hứa đầu: 99,1 giây là phần thay đổi khi giữ kế hoạch và
208,2 giây được tính cho điều phối.»
- Vì sao: hai khái niệm trung tâm xuất hiện ở đây nhưng chỉ được giải thích ở mục 1.2. "Được tính cho điều phối" là lối
  nói dịch.
- Đề xuất: «Khách ở hình trên tới nơi muộn hơn lời hứa đầu 307,3 giây. Trong đó, 99,1 giây là phần giờ trả lùi lại trong
  khi xe vẫn đi theo kế hoạch cũ; 208,2 giây là phần chênh giữa kế hoạch mới mà bộ điều phối chọn và kế hoạch cũ.»

**6. L22.** «Đây là khách trễ nhất trong một kịch bản phát triển với trần 300 giây.»
- Vì sao: "kịch bản phát triển" và "trần" chưa được giải thích. Người đọc không biết "trần 300 giây" chính là luật C ở
  mức lỏng.
- Đề xuất: «Khách này trễ nhất trong một kịch bản mô phỏng dùng khi xây dựng phương pháp (ngày 13/11/2018), ở cấu hình
  cho phép bộ điều phối dời giờ trả của mỗi khách tổng cộng tới 300 giây.»

**7. L22–23.** «Khi dùng trần 30 giây, khách trễ nhất của kịch bản là một người khác, trễ 99,1 giây, trong đó 97,1 giây
thuộc phần giữ kế hoạch.»
- Vì sao: số 99,1 xuất hiện lần thứ hai với nghĩa khác. Lần đầu nó là phần giữ kế hoạch của khách ở hình trên; lần này
  nó là độ trễ của một người khác. Người đọc gần như chắc chắn nhầm. Số liệu đúng (q4-rider:3, 9).
- Đề xuất: «Nếu chỉ cho dời tổng cộng 30 giây, khách trễ nhất của cùng kịch bản là một người khác: người này tới muộn
  99,1 giây, trong đó 97,1 giây thay đổi trong khi xe giữ kế hoạch cũ. Số 99,1 giây này chỉ tình cờ trùng với phần
  tương ứng của khách ở hình trên.»

**8. Hình 1.1, L29 và L42.** «(a) Khách trễ nhất, trần 300 giây»; nhãn mốc «Tổng phần giữ kế hoạch\\99,1».
- Vì sao: "trần" chưa được giải thích. Nhãn mốc giữa là một vị trí trên trục, không phải một sự kiện. Đặt cạnh "Lời hứa
  đầu" và "Trả thực tế", hai sự kiện có thật, nó dễ được đọc thành một mốc giờ.
- Đề xuất: «(a) Khách trễ nhất khi cho dời tối đa 300 giây»; nhãn mốc giữa chỉ ghi «+99,1», vì đoạn ở trên trục đã ghi
  "Giữ kế hoạch 99,1 giây".

**9. Hình 1.1, L44.** «(b) Khách có lời hứa tính lại theo hồ sơ lịch sử»
- Vì sao: "hồ sơ lịch sử" chưa được giải thích.
- Đề xuất: «(b) Một khách khác: lời hứa tính sẵn mức tắc đường quen thuộc».

**10. Chú thích Hình 1.1, L62.** «hai đoạn là tổng các phần ghi trong sổ»
- Vì sao: "sổ" chưa được giới thiệu.
- Đề xuất: «hai đoạn là tổng các phần của khách này qua mọi lần cập nhật lời hứa».

**11. L68.** «Khách ở hình dưới đặt xe lúc 7:11:56, được đón lúc 7:22:30 và tới nơi muộn hơn lời hứa đầu 190,5 giây.»
- Vì sao: câu không nói lời hứa đầu là mấy giờ; thông tin đó chỉ có trong hình. Giờ đón 7:22:30 cách giờ đặt 634 giây,
  trong khi L252 và Ch4A v5-v3:88 ghi "đón trong vòng 600 giây kể từ lúc gọi". Người đọc kỹ sẽ vấp (xem câu hỏi bảo
  vệ 8).
- Đề xuất: «Khách ở hình dưới đặt xe lúc 7:11:56, được hứa tới nơi lúc 7:34:51 nhưng tới thật lúc 7:38:02, muộn 190,5
  giây.» Câu này bỏ giờ đón; nếu giữ giờ đón thì phải giải thích phần vượt 600 giây.

**12. L69.** «Khi tính lại lời hứa từ hồ sơ tắc đường lịch sử, độ lệch còn 17,6 giây.»
- Vì sao: "hồ sơ tắc đường lịch sử" là từ chuyên môn. Câu không nêu cái giá (lời hứa dài thêm 172,9 giây), trái quy tắc
  31 của STYLE: nói về trễ thì phải báo kèm độ dài thêm của lời hứa.
- Đề xuất: «Nếu lúc hứa, hệ thống cộng sẵn mức tắc đường quen thuộc của khung giờ này, lấy trung bình từ các ngày
  trước, thì lời hứa là 7:37:44, dài hơn 172,9 giây, và khách chỉ còn trễ 17,6 giây.»

**13. L69–70.** «Ví dụ này minh họa vai trò của dự báo, không phải phép đo tác dụng của trần.»
- Vì sao: "trần" chưa được giải thích; "phép đo tác dụng" là cụm nặng.
- Đề xuất: «Ví dụ này cho thấy dự báo giúp gì và tốn gì; nó không nói gì về giới hạn đặt cho bộ điều phối.»

**14. L73–74.** «Vấn đề giờ đến cũng xuất hiện trong nguồn hướng dẫn dịch vụ: UberX Share nêu rằng không bảo đảm giờ
đến, còn MOIA Express giới thiệu cửa sổ giờ đến ngắn hơn như một lựa chọn nâng cấp.»
- Vì sao: "nguồn hướng dẫn dịch vụ" không tự nhiên; "cửa sổ giờ đến" là từ dịch. Câu không có trích dẫn, dù khóa
  `uberxshare` và `moiaexpress` đã có (`r32-bib/10-tai-lieu-draft-v2.tex:133,140`).
- Đề xuất: S9.

**15. L74–75.** «Về phía người đi xe, khảo sát của Alonso-González và cộng sự đo giá trị của độ tin cậy trong dịch vụ đi
chung.»
- Vì sao: "giá trị của độ tin cậy" là thuật ngữ kinh tế vận tải; người đọc không biết nó nghĩa là gì.
- Đề xuất: S9.

**16. L76.** «Phân tích tổng hợp của Wardman và cộng sự đo giá trị của thời gian tới muộn theo những cách hỏi khác.»
- Vì sao: "theo những cách hỏi khác" không rõ là khác với cái gì. Câu không có con số nào, nên không cho thấy vì sao
  khách quan tâm.
- Đề xuất: S9. Có thể dùng số của sổ J23: 2,53 và 3,12.

**17. L77.** «Hai loại bằng chứng này không cho biết khách sẽ coi trọng trần điều phối của khóa luận đến mức nào.»
- Vì sao: "trần điều phối" chưa được giải thích, và là tên thứ năm cho cùng một khái niệm.
- Đề xuất: «Các nghiên cứu này nói về giờ tới nói chung; chúng không cho biết khách coi trọng giới hạn mà khóa luận đặt
  cho bộ điều phối đến mức nào.»

### Mục 1.2

**18. L83.** «Trên tập kiểm tra chính, khi điều phối không trần (vẫn khóa xe và điểm đón, trả), 134 trong 203 khách trễ
quá một phút từng có giờ trả bị điều phối dời.»
- Vì sao:
  - Ba cụm chưa được giải thích: "tập kiểm tra chính", "điều phối không trần", "khóa".
  - Ngoặc đơn liệt kê thiếu khóa giờ đón (A08).
  - Một câu chứa bốn ý.
- Đề xuất: M5, đoạn thứ hai.

**19. L84.** «Đây là giao của hai tập khách, không phải số người trễ được xác định là do điều phối.»
- Vì sao: "giao của hai tập" là lối nói toán học.
- Đề xuất: «Con số chỉ cho biết hai nhóm khách trùng nhau, không cho biết việc bị dời là nguyên nhân làm họ trễ.»

**20. L85–86.** «Theo sổ, phần tính cho điều phối bằng 73,4% tổng số giây trễ của cả 203 khách: 23.027 trên 31.353 giây,
gộp theo khách và làm tròn hai tổng tới giây.»
- Vì sao: "sổ" được dùng trước khi định nghĩa, vì định nghĩa nằm ở đoạn sau. Vế "gộp theo khách và làm tròn hai tổng tới
  giây" là ghi chú kỹ thuật; nên chuyển xuống dòng `% EV:`.
- Đề xuất: «Theo sổ theo từng khách, 23.027 trong 31.353 giây trễ của cả 203 khách, tức 73,4\%, thuộc phần tính cho điều
  phối.» Câu này cần đặt sau đoạn định nghĩa (M5).

**21. L86.** «Một khách bị dời tổng cộng 590,1 giây, gần mười phút.»
- Vì sao: không rõ khách này có nằm trong 203 khách vừa nói không. Thực ra đó là khách bị dời nhiều nhất trong 2.434
  khách được phục vụ (C20).
- Đề xuất: «Trong 2.434 khách được phục vụ, khách bị dời nhiều nhất có giờ trả bị dời tổng cộng 590,1 giây, gần 10
  phút.»

**22. L89–90.** «Phần tính cho điều phối được đo bằng cách so kế hoạch được chọn với kế hoạch cũ tính lại ở cùng trạng
thái.»
- Vì sao: đây là khái niệm trung tâm của cả khóa luận, nhưng câu dùng lối nói rút gọn ("tính lại ở cùng trạng thái") và
  không có ví dụ. DACN luôn đặt ví dụ ngay sau quy tắc (STYLE 1.4).
- Đề xuất: M5, dùng ví dụ dựng tay 9:10:00 / 9:10:40 / 9:11:10 của X3-37.

**23. L90–91.** «Luật C giới hạn tổng độ lớn của các lần dời thuộc phần này cho từng khách.»
- Vì sao: người ngoài ngành không hiểu "tổng độ lớn", tức tổng trị tuyệt đối. Câu không nói trần là bao nhiêu.
- Đề xuất: «Luật C đặt cho mỗi khách một mức tối đa, gọi là trần, cho tổng các lần dời thuộc phần này trong cả chuyến;
  dời sớm hay dời muộn đều cộng vào. Mức chính được thử là 30 giây.»

**24. L91–92.** «Phần hồ sơ tắc đường lịch sử giải thích được cộng sẵn vào lời hứa theo dự báo.»
- Vì sao: chuỗi danh từ chồng lên nhau, đọc vấp; người đọc không tìm ra chủ ngữ và động từ.
- Đề xuất: «Phần mà mức tắc đường quen thuộc của khung giờ, lấy trung bình từ các ngày trước, giải thích được thì được
  cộng sẵn vào lời hứa ngay lúc hứa; khóa luận gọi đó là lời hứa theo dự báo.»

**25. L92.** «Phần còn lại được ghi trong sổ theo từng khách để biết dự báo đang dùng chưa giải thích được bao nhiêu.»
- Vì sao: câu ổn, nhưng đây là lần đầu "sổ" được định nghĩa thật, nên cần nói rõ đó là một sổ riêng.
- Đề xuất: «Phần còn lại được ghi vào một sổ riêng của từng khách, để biết dự báo đang dùng còn bỏ sót bao nhiêu.»

**26. Hình 1.2, L101 và L105.** «Phần hồ sơ lịch sử giải thích»; «Sổ theo từng khách: ghi và kiểm»
- Vì sao: nhãn đầu là chuỗi danh từ. Nhãn sau không nói "kiểm" cái gì.
- Đề xuất: «Phần dự báo giải thích được»; «Sổ theo từng khách: ghi phần chưa giải thích».

**27. L116.** «Phép chia này là phép tính theo mô hình.»
- Vì sao: "theo mô hình" quá ngắn; người đọc không hiểu rằng câu muốn nói "không phải phép đo nguyên nhân".
- Đề xuất: «Cách chia này là một phép tính trên mô hình mô phỏng, không phải phép đo nguyên nhân.»

**28. L120–122 (CH1).** «Phần dời do điều phối được đo trên đại lượng nào, kiểm khi nào, và trần trên phần đó giữ được
gì, không giữ được gì? … Câu hỏi này không suy ra bảo đảm giờ đến thực tế.»
- Vì sao: ba câu hỏi gộp làm một. "Câu hỏi này không suy ra" sai ngữ pháp, vì câu hỏi không suy ra được gì.
- Đề xuất: S10.

**29. L123–125 (CH2).**
- Vì sao:
  - "giữ trần" là lối nói không tự nhiên.
  - Bốn cụm chưa được giải thích: "luật hạn chót", "cách đệm lời hứa", "bộ chọn", "đúng giờ".
  - Câu dài 48 tiếng.
- Đề xuất: S10.

**30. L126–128 (CH3).**
- Vì sao: "hồ sơ tắc đường lịch sử" và "đúng giờ" chưa được giải thích. "kết quả không suy ra phản ứng của khách" không
  tự nhiên.
- Đề xuất: S10.

### Mục 1.3

**31. L135.** «Các nghiên cứu trước đã đo độ bất ổn, kiểm soát việc đổi giờ trước quyết định và đặt giới hạn theo từng
khách.»
- Vì sao: câu không nói "độ bất ổn" là của cái gì. "Kiểm soát … trước quyết định" là từ dịch của "ex-ante control".
- Đề xuất: «Các nghiên cứu trước đã đo mức giờ hứa thay đổi trong chuyến, đã chặn việc đổi giờ ngay khi chọn kế hoạch,
  và đã đặt giới hạn riêng cho từng khách.»

**32. L136.** «Bảng 1.1 đối chiếu đại lượng được xét và cách xử lý phần thay đổi khi giữ kế hoạch.»
- Đề xuất: «Bảng 1.1 so các cách đó ở hai điểm: mỗi cách giới hạn đại lượng nào, và thời gian đi thay đổi trên đường
  được tính vào hay để ra ngoài.»

**33. Chú thích Bảng 1.1, L142–143.** «Nội dung viết bằng lời; …»
- Vì sao: "Nội dung viết bằng lời" là chỉ dẫn nội bộ của đề cương ("words only") bị lọt vào chú thích.
- Đề xuất: «Chỗ đứng của khóa luận so với các cách đo và ràng buộc lời hứa. “Thời gian đi cố định” nghĩa là mô hình của
  bài được trích không có tắc đường thay đổi.»

**34. Bảng 1.1, tiêu đề cột 3, L149.** «Phần thay đổi khi giữ kế hoạch»
- Vì sao: người đọc chưa nắm khái niệm này. Ở hàng dự báo (`hu2022`), nội dung ô không khớp tiêu đề cột.
- Đề xuất: «Thời gian đi thay đổi được xử lý thế nào».

**35. Bảng 1.1, L171.** «Mt-KaRRi~\cite{laupichler2026}»
- Vì sao: tên riêng chưa được giải thích, và khác cách ghi của các hàng khác (tác giả, năm).
- Đề xuất: «Laupichler và cộng sự (2026), bộ điều phối Mt-KaRRi~\cite{laupichler2026}».

**36. L190.** «Cách đọc bảng: cùng bảo vệ lời hứa nhưng các cách giới hạn những đại lượng khác nhau.»
- Vì sao: câu thiếu chủ ngữ. "các cách giới hạn" đọc như một danh từ ghép.
- Đề xuất: «Cách đọc bảng: các cách trong bảng đều bảo vệ lời hứa với khách, nhưng mỗi cách giới hạn một đại lượng
  khác.»

**37. L191–192.** «Riêng với Hörl và Zwick, khóa luận kế thừa mốc tuyến cũ tính lại; phần làm thêm là trần điều phối
chung cho mọi khách có lời hứa, cộng qua cả chuyến và không nới theo tắc đường.»
- Vì sao: "mốc tuyến cũ tính lại" là lối nói rút gọn khó hiểu. "Không nới theo tắc đường" dễ được đọc thành "chặt hơn",
  trong khi luật C không nới chỉ vì nó không tính phần tắc đường.
- Đề xuất: M3.

### Mục 1.4

**38. L198–199.** «Hãng xe và khách biết trần tổng độ dời giờ trả do điều phối của mỗi khách, kể cả khi dự báo sai; đổi
lại có thể phục vụ ít hơn.»
- Vì sao:
  - Câu cụt, đọc như một sự kiện đã xảy ra chứ không như một mục tiêu.
  - Điều hãng xe và khách được không phải là "biết trần", mà là một giới hạn lên phần dời giờ trả.
  - "có thể phục vụ ít hơn" không có số.
  - Mục mang tên "Mục tiêu và đóng góp" nhưng không có câu "Mục tiêu".
- Đề xuất: M4.

**39. L203–204.** «Khóa luận đặc tả và cài đặt luật C trong RideBound: …»
- Vì sao: "RideBound" xuất hiện lần đầu mà không có chữ nào nói nó là gì. Câu dài 50 tiếng.
- Đề xuất: M4.

**40. L204–206.** «Mốc đo là giờ trả của kế hoạch cũ tính lại ở cùng trạng thái, kế thừa Hörl và Zwick (2022); luật C
dùng trần chung không nới theo tắc đường, cùng lời hứa theo hồ sơ lịch sử và sổ từng khách.»
- Vì sao:
  - Vế sau đọc như thể luật C "dùng" lời hứa theo dự báo và sổ.
  - Cụm "vốn đã có trong thực tiễn" bị bỏ, dù OUTLINE §6.1 dặn đây là cụm bỏ sau cùng.
  - Câu dài 43 tiếng.
- Đề xuất: M4.

**41. L206–208.** «Trên 34 kịch bản FleetPy với hệ số tắc đường toàn thành phố từ dữ liệu Manhattan (3.672 yêu cầu mỗi
cấu hình), trần 30 giây mất 96 lượt phục vụ …»
- Vì sao: câu dài 52 tiếng. "FleetPy" chưa được giải thích và không trích `engelhardt2026`; "cấu hình" chưa được giải
  thích.
- Đề xuất: M4.

**42. L208–209.** «Luật hạn chót 30 giây phục vụ cùng số lượt, nhưng tính cả giao thông nên phá luật với ít nhất một
khách ở 28 trong 34 kịch bản.»
- Vì sao:
  - Chương chưa định nghĩa "luật hạn chót".
  - "phá luật", nghĩa đen là vi phạm pháp luật, nên thay bằng "phá lời hứa" như bảng thuật ngữ.
  - "giao thông" nên thay bằng "tắc đường".
  - Về nội dung, câu không công bằng; xem Phần 2.
- Đề xuất: M1.

**43. L210.** «Luật C không tính phần này.»
- Vì sao: "phần này" trỏ về "giao thông" ở câu trước, đọc mơ hồ.
- Đề xuất: M1.

**44. L210–211.** «Luật C không bị ép (phải dùng miễn trừ) nếu giả thiết (N) ở mục 3.x được thỏa và phần trần đã dùng
không vượt giới hạn; không trần cũng có 0 trong 20.760 quyết định bị ép.»
- Vì sao: bốn thuật ngữ chưa được giải thích: "bị ép", "miễn trừ", "(N)", "phần trần đã dùng". Ký hiệu (N) có trước lời
  giải thích.
- Đề xuất: M1, viết bằng lời.

**45. L212–213.** «So với lời hứa đầu không dự báo, ở ngưỡng trễ 30 giây, luật C có 292 trong 2.338 khách được phục vụ
(12,5%), …»
- Vì sao: câu đọc được thành "luật C phục vụ 292 trong 2.338 khách", vì thiếu vị ngữ "tới muộn hơn … quá 30 giây".
- Đề xuất: M1.

**46. L213–215.** «Khi có dự báo, không trần đệm 30 giây hòa luật C ở ngưỡng một phút và hơn ở hai phút; …»
- Vì sao: lối viết điện tín. "không trần đệm 30 giây" là ký hiệu bảng ("U + đệm") được ghép thành chữ. Câu dài 41 tiếng.
- Đề xuất: S7.

**47. L215–216.** «Trong 132 lần chạy luật C đã kiểm toàn bộ bản ghi chặn, 3 trong 1.780 bản ghi chặn chỉ bị chặn do cộng
dồn, …»
- Vì sao: "bản ghi chặn" và "cộng dồn" chưa được giải thích. "Bản ghi … bị chặn" sai nghĩa: bản ghi ghi lại một phương
  án bị loại, bản thân bản ghi không bị chặn.
- Đề xuất: S7.

**48. L219.** «Kết quả chính gộp trên 3.672 yêu cầu; số không trễ gồm cả khách tới sớm:»
- Vì sao: nhãn sai một phần. Khách đi chung, khách tới sớm và độ dài thêm của lời hứa tính trên khách được phục vụ,
  không trên 3.672 yêu cầu. "số không trễ gồm cả khách tới sớm" khó hiểu.
- Đề xuất: «Kết quả chính trên 34 kịch bản, 3.672 yêu cầu mỗi cấu hình. Số lượt không trễ tính trên 3.672 yêu cầu và gồm
  cả khách tới sớm; số khách đi chung, khách tới sớm và độ dài thêm của lời hứa tính trên số khách được phục vụ.»

**49. L224–225.** «Chưa dự báo: …; đi chung 555 trong 2.434 và 313 trong 2.338 khách.»
- Vì sao: số khách đi chung không liên quan tới dự báo, nên đặt sai nhóm. Câu không nói đó là cái giá. Gạch đầu dòng
  thiếu ngưỡng hai phút (2.332 và 2.327).
- Đề xuất: «Khi chưa có dự báo: không trễ quá một phút 2.231 lượt khi không trần và 2.262 với luật C; không trễ quá hai
  phút 2.332 và 2.327. Khách đi chung giảm từ 555 trong 2.434 xuống 313 trong 2.338.»

**50. L227–228.** «Có dự báo, luật C và không trần đệm 30 giây cùng 2.328 lượt …; ở hai phút là 2.338 và 2.366. Sớm quá
một phút: 4 trong 2.338 và 44 trong 2.434 khách.»
- Vì sao: lối viết điện tín.
- Đề xuất: «Khi có dự báo, luật C và cách đệm 30 giây trên điều phối không trần cùng có 2.328 lượt không trễ quá một
  phút; ở ngưỡng hai phút là 2.338 và 2.366. Khách tới sớm quá một phút: 4 trong 2.338 và 44 trong 2.434.»

**51. L233.** «Cộng dồn: 132 lần chạy gồm 98 lần cũ và 34 lần trần 120 giây; đối chứng mỗi lần một trần chưa chạy.»
- Vì sao: "lần cũ" và "đối chứng mỗi lần một trần" khó hiểu.
- Đề xuất: «Phép cộng qua cả chuyến: đã kiểm toàn bộ bản ghi của 132 lần chạy (98 lần chạy trần 30–300 giây trước đó và
  34 lần chạy trần 120 giây); luật so sánh chỉ giới hạn từng lần dời riêng lẻ chưa được chạy.»

**52. Khung, L239.** «… tương đồng tuyến, cam kết tối thiểu và nhất quán thời gian …»
- Vì sao: đây là bản dịch sát của thuật ngữ tiếng Anh; người ngoài ngành không hiểu. Các mục này bắt buộc theo AGENTS.md
  nên phải giữ.
- Đề xuất: thêm tiếng Anh ở lần đầu: «tương đồng tuyến (route similarity), cam kết tối thiểu (least commitment), nhất
  quán thời gian (time consistency)».

### Mục 1.5

**53. L255.** «tốc độ nền lấy lúc 00:00»
- Vì sao: người đọc không biết "tốc độ nền" là gì và vì sao mốc 00:00 quan trọng.
- Đề xuất: «tốc độ gốc của mọi kịch bản lấy theo hệ số lúc 0 giờ (nửa đêm)».

**54. L262.** «Dự báo chính chỉ được tính lại trên các chuyến đã ghi, không đổi quyết định điều phối.»
- Vì sao: "Dự báo chính" khó hiểu.
- Đề xuất: «Lời hứa theo dự báo chỉ được tính lại trên các lần chạy đã ghi; nó không làm thay đổi xe nào chở ai.»

### Ba câu hỏi của người đọc

**Đọc xong, có nói được trong hai câu khóa luận giải bài toán gì và đóng góp gì không?** Có, nhưng phải đọc lại đoạn đóng
góp hai lần và đoán nghĩa của khoảng mười thuật ngữ. Phần "giải bài toán gì" khá rõ nhờ Hình 1.2. Phần "đóng góp gì" bị
chìm trong 24 con số. Câu "đây không phải một thuật toán mới" (OUTLINE §0 dòng 5) không có trong chương.

Hai câu của tôi:

> Trong dịch vụ đi chung xe, mỗi lần bộ điều phối ghép thêm khách, giờ trả đã hứa với những khách đang đi có thể bị dời.
> Khóa luận đặt cho mỗi khách một trần, chẳng hạn 30 giây, cho tổng các lần dời giờ trả tính cho điều phối trong cả
> chuyến (luật C), tách riêng phần giờ trả thay đổi do thời gian đi trên đường, rồi cài luật này vào bộ điều phối
> RideBound và đo trên mô phỏng FleetPy với dữ liệu Manhattan.
>
> Đóng góp là một cam kết hẹp, kiểm được với từng khách, cùng phép đo cái giá của nó. Trên 3.672 yêu cầu, trần 30 giây
> phục vụ ít hơn 96 lượt và không đúng giờ hơn luật hạn chót hay cách đệm 30 giây có dự báo; nó chỉ khác ở chỗ giới hạn
> được phần dời của từng người, với lời hứa dài thêm ít hơn cách đệm (7,4 so với 37,2 giây).

(Mỗi đoạn trên gồm hai câu ngắn để dễ đọc; về ý, mỗi đoạn là một câu trả lời.)

**Chương có cho thấy vì sao khách hay hãng xe quan tâm không?** Chỉ một phần.
- Về phía khách, chương nêu đúng các nguồn (UberX Share, MOIA, hai nghiên cứu định giá) nhưng không đưa ra con số nào để
  người đọc thấy một phút trễ đáng bao nhiêu. Sổ đã có số: 8 phút đi thêm trung bình của UberX Share (J28); một phút tới
  muộn bằng khoảng 2,53–3,12 phút ngồi xe (J23).
- Con số gây ấn tượng nhất, một khách bị dời tổng cộng 590,1 giây, lại nằm cuối một đoạn kỹ thuật ở mục 1.2.
- Về phía hãng xe, câu duy nhất (L198–199) là câu cụt và không nói hãng xe được gì một cách cụ thể: một lời cam kết với
  từng khách, kiểm lại được bằng sổ. Câu đó cũng không nêu cái giá bằng số.
- DACN mở Chương 1 bằng một tình huống đời thường (nhóm bạn chọn chỗ hẹn qua nhóm chat, PDF tr. 13). Chương này mở bằng
  định nghĩa bộ điều phối.

**Hình 1.1 và 1.2 có giúp không?**
- **Hình 1.1(b)** giúp nhiều nhất trong chương. Nó cho thấy rõ lời hứa theo dự báo dời mốc đích ra 172,9 giây, nên độ trễ
  còn 17,6 giây. Nhưng hình không cho biết phần tính cho điều phối của khách này là bao nhiêu, nên (b) minh họa dự báo
  chứ không minh họa trần.
- **Hình 1.1(a)** chỉ là một thanh chia hai đoạn vẽ thành trục thời gian. Có ba chỗ khó:
  - Nhãn mốc giữa "Tổng phần giữ kế hoạch 99,1" là vị trí, không phải sự kiện.
  - "Trần 300 giây" chưa được giải thích.
  - Hai panel thuộc hai khách, hai ngày, hai tỉ lệ trục, nhưng không có câu nào nói rõ vì sao đặt chúng cạnh nhau.
- **Một cách khác đáng cân nhắc cho (a):** khách của tập kiểm tra chính bị bộ điều phối không trần dời hai lần, 25,844
  rồi 99,027 giây (N-27, E07). Ví dụ này cho thấy đúng điều luật C chặn, tức các lần dời cộng dồn, ngay trên tập chính.
  Muốn dùng nó thì cần thêm phần trễ của khách đó, mà sổ chưa có.
- **Hình 1.2** có ích như một bản đồ ba phần đến ba chỗ xử lý. Nhưng các ô chỉ là nhãn, và nhãn "Phần hồ sơ lịch sử giải
  thích" khó đọc (chỗ khó 26). Hình đủ dùng nếu đoạn văn trước nó có ví dụ dựng tay (M5).

---

## Phần 2. Giảng viên chấm

### 2.1 Động cơ có cụ thể không?

Cụ thể về số, chưa cụ thể về người.
- **Điểm tốt.** Hai khách thật trong mô phỏng; con số 134/203 kèm câu nói rõ đây không phải quan hệ nhân quả;
  73,4\% có tử số và mẫu số; 590,1 giây.
- **Điểm yếu.**
  - Ví dụ đầu lấy từ một kịch bản phát triển dưới chính luật C ở mức 300 giây, không lấy từ điều phối không trần trên tập
    chính. Người chấm sẽ hỏi vì sao động cơ của trần lại minh họa bằng một khách đang chịu trần.
  - Chương không có câu nêu khoảng trống: trong các cách đang có, phần dời do điều phối hoặc chỉ được đo (Fielbaum), hoặc
    chỉ được bảo đảm cho khách được chọn (Elmi), hoặc bị giới hạn chung với phần tắc đường (hạn chót). Bảng 1.1 có ý này
    nhưng văn bản không nói ra.
  - Nguồn từ phía hãng xe (UberX Share, MOIA) chưa có `\cite`.

### 2.2 Ba câu hỏi nghiên cứu

| Câu | Rõ? | Trả lời được? | Ghi chú |
|---|---|---|---|
| CH1 | Chưa: gộp ba câu, nửa đầu là câu hỏi định nghĩa ("đo trên đại lượng nào"), không phải câu hỏi thực nghiệm | Có: Chương 3 định nghĩa, mục 4.3, 4.5, 4.10 kiểm | "Câu hỏi này không suy ra …" sai ngữ pháp |
| CH2 | Ý rõ, chữ chưa rõ: "giữ trần", "đúng giờ", "luật hạn chót", "cách đệm", "bộ chọn" chưa được định nghĩa ở Chương 1 | Có, và câu trả lời gồm cả kết quả bất lợi (đệm hòa, kém ở hai phút); tốt | Vế "không xác định tác dụng riêng của bộ chọn" đúng và trung thực, nhưng người đọc không biết bộ chọn là gì |
| CH3 | Rõ vừa | Có | Nên nói "không trễ quá một phút" thay "đúng giờ" |

Cách viết CH1 và CH2 ở Chương 1 khác Bảng 4.0 của Chương 4 (Ch4A v5-v3, bảng `bang:c4-lotrinh`). Phải thống nhất một
cách viết (S10).

### 2.3 Đóng góp có hẹp và trung thực không?

Phần lớn có. Chỗ còn thiếu là phần ngụ ý.

| Kiểm | Kết quả | Dòng |
|---|---|---|
| Không nói luật C phục vụ nhiều hơn | Đạt: −96 lượt | L207 |
| Không ngụ ý luật C giữ lời hứa đầu tốt hơn luật hạn chót | **Chưa đạt**: câu 28/34 chỉ nói luật hạn chót "phá luật". Cùng thước đo, luật C cũng có khách tới muộn quá 30 giây ở 28/34 kịch bản (C4A-01; Ch4A v5-v3:357–358). Số 292/289 đến sau ba câu và câu viết dễ đọc sai | L208–213 |
| Không nói lệch so với không trần | **Chưa đạt**: nêu +31 lượt ở một phút, bỏ −5 lượt ở hai phút (2.332 → 2.327; C08). Chương 4 nêu cả hai (Ch4A v5-v3:244–245) | L208 |
| Cách đệm | Đạt: hòa ở một phút, hơn ở hai phút, 37,2 so với 7,4 giây | L213–215 |
| "0 quyết định bị ép" không thành lợi thế | Đạt một nửa: có "không trần cũng có 0 trong 20.760". Thiếu: hạn chót nới kiểu Hörl–Zwick cũng có tính chất này theo định nghĩa (A22, K02). Câu đầy thuật ngữ | L210–211 |
| Vế cộng dồn | Đạt: "đều ở trần 120 giây", "chưa được đo". Nên nói thêm "0 lần ở trần 30 giây", vì đây là một trong ba điểm khác Hörl–Zwick | L215–216 |
| Lời hứa theo dự báo là thực hành đã có | **Chưa đạt**: mất "vốn đã có trong thực tiễn" (OUTLINE §6.1), và khung cũng không nhắc | L206, L237–241 |
| "Không phải thuật toán mới" | **Thiếu** (OUTLINE §0 dòng 5) | — |
| Dữ liệu đã xem, kết quả thăm dò | **Thiếu ở Chương 1**. Chương 4 có (Ch4A v5-v3, mục `muc:c4-thamdo`; Ch4B v10:421–423). Tên "tập kiểm tra chính" khiến người chấm nghĩ đây là tập giữ lại chưa xem | L258–259 |
| Không tách được trần với bộ chọn | Chỉ có một vế trong CH2, dùng từ "bộ chọn" chưa định nghĩa; không có trong Phạm vi | L125, L261–262 |
| Không nói lợi ích kinh doanh | Đạt | L240 |

### 2.4 So với Hörl và Zwick (2022) có công bằng không?

Công bằng ở phần ghi công, chưa công bằng ở phần nêu khác biệt.

- **Đúng.** Chương ghi rõ mốc "kế hoạch cũ tính lại" là của Hörl và Zwick (L205, L191); dùng "công thức 7"; không nói
  "cổng cứng thay vì phạt" (K26); có câu "tác dụng thực nghiệm riêng của việc cộng dồn còn chưa được đo".
- **Thiếu hoặc lệch.**
  1. Chương không nói **luật kiểu Hörl–Zwick chưa được chạy làm đối chứng**. Chương 4 B v10:445–446 nói điều này. Người
     chấm đọc Chương 1 sẽ tưởng khác biệt đã được đo.
  2. Ba khác biệt ("trần chung, cộng qua cả chuyến, không nới theo tắc đường") là **suy luận từ hai định nghĩa** (J05
     ghi "VERIFIED-by-Codex R18, suy luận"). Chương không gắn nhãn này.
  3. "Không nới theo tắc đường" (L159, L191) dễ được đọc thành "chặt hơn". Đúng ra: luật C không tính phần tắc đường nên
     không cần nới; còn cách của hai tác giả dùng giờ tính lại làm cận dưới cho khách trên xe sắp trễ (công thức 7, C2-04).
     Hai cách nhắm hai mục đích khác nhau. Chương 3 v3 (dòng 451–452) đã viết đúng: mục đích của hai tác giả, tránh tình
     huống không còn thứ tự trả khả thi, cũng là mục đích của Nhận xét 3.1.
  4. Ô bảng của Hörl–Zwick không nói phần nới **chỉ áp cho khách trên xe sắp trễ** và có phạt (11). Thiếu chi tiết này,
     vế "trần chung cho mọi khách" của khóa luận trông như một cải tiến.
  5. Vế cộng dồn, một trong ba khác biệt, **chưa lần nào là lý do riêng để loại phương án ở trần 30 giây** trên các lần
     chạy đã kiểm: 845 + 411 bản ghi ở E01, 163 ở N-26, đều 0. Chương chỉ nói "đều ở trần 120 giây".
  6. Thiết lập của hai tác giả là nhu cầu thật của MOIA ở Hamburg với tốc độ từ dữ liệu GPS của TomTom (C2-05). Thiết lập
     đó khác hẳn hệ số chung toàn thành phố của khóa luận. Không nên để người đọc nghĩ khóa luận được kiểm trong điều
     kiện sát thực tế hơn.

### 2.5 Khung "không nhận là mới" có đủ không?

Chưa. Khung (L237–241) chỉ có bảy mục của AGENTS.md cùng câu về giờ đến, kinh doanh và hài lòng. So với OUTLINE §6.4 và
STYLE quy tắc 34, khung thiếu:
- **Các ý đã có trước:**
  - Mốc giờ trả cập nhật theo tắc đường và việc nới hạn trả dựa trên mốc đó (Hörl–Zwick).
  - Đo độ bất ổn của lời hứa, kiểm soát trước quyết định, và đánh đổi giữa phục vụ và ổn định (Fielbaum–Alonso-Mora;
    J38 ghi rõ đây là tiền lệ).
  - Bảo vệ hay bảo đảm theo từng khách (Elmi).
  - Hạn chót tính từ lời mời (Schulz–Pfeiffer).
  - **Lời hứa theo dự báo và dự báo giờ đến** (J35, C2-15). Đây là thiếu sót nặng nhất, vì khóa luận dùng chính thứ này
    và đoạn đóng góp đặt nó cạnh luật C.
- **Các điều không khẳng định** (OUTLINE §6.4 "Bốn điều"):
  - Luật C không phục vụ nhiều hơn và không đúng giờ hơn: bằng luật hạn chót; hòa rồi kém cách đệm. **Đây chính là ràng
    buộc mà đề bài nhấn mạnh.**
  - Sổ không kết luận ai có lỗi; phần còn lại không phải phần "không thể biết trước". Ý này có ở L116 nhưng không có trong
    khung.
  - Không suy rộng sang thành phố, mức tải hay mạng đường khác; không mức trần nào tốt nhất.
- Dòng "Phần khóa luận làm".

Lý do Codex đưa ra (NOTES §6 ý 6: "đã có ở Bảng 1.1") chỉ đúng một phần. Bảng 1.1 không có các điều không khẳng định, và
không đánh dấu lời hứa theo dự báo là ý đã có. Mục "luật phục hồi không tệ hơn" của OUTLINE dựa trên J16, vẫn UNVERIFIED,
nên **không** thêm vào khung.

### 2.6 Nói quá và từ cấm

- **"duy nhất", "đầu tiên", "tối ưu", "vượt trội":** không có. "Mức trần tốt nhất" chỉ xuất hiện ở dạng phủ định (L125).
- **Từ chỉ nhân quả:** không có "gây ra". "Bị điều phối dời" (L83) và "phần dời do điều phối" (L120) mô tả lần $c \neq 0$
  và là tên trong bảng thuật ngữ, không phải phép chia của sổ, nên chấp nhận được. L84 và L116 đã rào đúng.
- **Bảo đảm:** "kể cả khi dự báo sai" (L198) đúng theo cách xây dựng (N-28: cuối tuần không có dự báo, lớn nhất 29,2
  giây), nhưng nên thêm "theo cách xây dựng luật". "Không bị ép … nếu (N)" có điều kiện; đạt.
- **Lợi ích kinh doanh:** không có.
- **Nói quá ngầm** (cần sửa):
  - L208–209: 28/34 ngụ ý luật C hơn luật hạn chót, trong khi luật C cũng 28/34.
  - L208: chỉ nêu +31, bỏ −5.
  - L159, L191: "không nới theo tắc đường" đọc thành chặt hơn.
  - L205–206: lời hứa theo dự báo không được đánh dấu là đã có.
  - L219: nhãn "gộp trên 3.672 yêu cầu" sai cho bốn số.
  - L198: "biết trần" ngụ ý hãng xe đã thông báo trần cho khách; khóa luận không thử việc thông báo.
- **Kế hoạch ghi trước, đăng ký trước, dự đoán:** không có, cả ở thân bài lẫn ở 35 dòng `% EV:`. Đã tìm bằng `grep -i`
  theo cụm tiếng Việt và tiếng Anh của bảng từ cấm trong WRITING-BRIEF. Dòng `%` L24 có tên tệp `q4-rider-2026-09-30.txt`
  (tệp mô tả sau khi xem); đây là anchor, không phải lời trong luận văn. Có thể thay bằng khóa `Q4R` của NOTES cho sạch,
  nhưng không bắt buộc.

### 2.7 Tám câu hỏi tôi sẽ hỏi khi bảo vệ

1. Luật C và luật hạn chót 30 giây cùng phục vụ 2.338 lượt. Số khách tới muộn hơn lời hứa đầu quá 30 giây là 292 so với
   289, mỗi luật ở 28 trong 34 kịch bản. Vậy với một khách đang ngồi trên xe, luật C hơn ở điểm nào? Lời hứa "chỉ phần do
   điều phối" có nghĩa gì với một khách vẫn tới muộn?
2. Khi có dự báo, đệm 30 giây trên điều phối không trần hòa luật C ở ngưỡng một phút, hơn ở ngưỡng hai phút, và phục vụ
   thêm 96 lượt. Một hãng xe thực dụng sẽ chọn đệm. Trong tình huống nào luật C đáng cái giá 96 lượt và 242 khách đi
   chung? Có bằng chứng nào rằng khách coi trọng lời hứa ngắn hơn 30 giây (7,4 so với 37,2 giây)?
3. Ba điểm khác Hörl–Zwick chỉ suy từ định nghĩa. Luật kiểu Hörl–Zwick chưa được chạy, và vế cộng dồn chưa lần nào là
   lý do riêng ở trần 30 giây. Bằng chứng thực nghiệm nào cho thấy ba điểm này quan trọng?
4. Luật C và điều phối không trần dùng chung bộ chọn ưu tiên ổn định, và phép thử ưu tiên chi phí chưa chạy. Làm sao
   biết 127 lượt trễ ít hơn đến từ trần chứ không từ bộ chọn?
5. Vì sao chọn 30 giây? Nếu đó không phải ngưỡng cảm nhận hay chuẩn ngành, và mức 120 giây được chọn sau khi xem tập kiểm
   tra chính, thì "tập kiểm tra" còn là kiểm tra theo nghĩa nào?
6. Mỗi kịch bản có 8 xe cho 108 yêu cầu; ngay cả khi không trần, chỉ 2.434 trong 3.672 yêu cầu được phục vụ (66,3\%,
   [A] từ C01). Tải là 0,535 khách trên mỗi xe, so với khoảng 1,33 ở nghiên cứu điển hình của FleetPy. Thời gian dừng là
   0 giây, tắc đường là một hệ số chung. Cái giá 96 lượt sẽ ra sao ở tải thật?
7. Mốc "giữ kế hoạch cũ, tính lại theo tốc độ hiện tại" có hợp lý để làm phép so không, khi nếu không ghép khách thì các
   quyết định sau cũng khác? Vì sao gọi là "phần tính cho điều phối" mà không nói là phần do điều phối gây ra? Bốn khách
   bị kéo sớm đúng 1 mili giây nghĩa là gì?
8. Khách ở Hình 1.1(b) đặt xe lúc 7:11:56 và được đón lúc 7:22:30, tức sau 634 giây, trong khi mục Phạm vi ghi "đón
   trong vòng 600 giây kể từ lúc gọi". Ràng buộc cửa sổ đón được xử lý thế nào khi tắc đường làm xe tới muộn? Điều đó có
   làm đổi số lượt phục vụ không? Theo X3-23 và X3-24, lần đón muộn được ghi lại thay vì dừng lần chạy, nhưng chương
   không nói điều này.

---

## Phần 3. Kiểm số

Anchor ghi theo sổ (ID) và theo chương 4: "4A" là `r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex`, "4B" là
`09-chuong4-phanB-v10.tex`. Tôi đã so 4A v5-v3 với v4: các số Chương 1 dùng không đổi.
- **Không có số WRONG.**
- **Có ba chỗ số đúng nhưng khung hay nhãn sai**, đánh dấu ⚠.
- **CANNOT CHECK: không có.** Mọi số đều truy được tới một dòng sổ hay một output gốc mà tôi đã mở.

| # | Dòng | Số trong chương | Kết luận | Anchor |
|---|---|---|---|---|
| 1 | L21, L38–43 | 307,3 = 99,1 + 208,2 giây | AGREE | D06; N-30; q4-rider:9 (rq-a019727097c: sum x 99,1 + sum c 208,2); W07-REPORT:48–50 |
| 2 | L22, L29 | trần 300 giây (C-300) | AGREE | q4-rider:8; D06 |
| 3 | L22–23 | trần 30 giây: khách khác, 99,1 giây, trong đó 97,1 | AGREE | N-30; q4-rider:3 (rq-f33d8bc2f39: 97,1 + 2,0) |
| 4 | L62 | 13/11/2018, khung 7:00–9:00 | AGREE | D06 (d20181113-s10-r1-w07); B15 |
| 5 | L54, L56, L58 | 7:34:51; 7:37:44; 7:38:02 | AGREE | C31; EXAMPLE:3, 60 |
| 6 | L53, L56, L58, L59, L68–69 | 172,9; 190,5; 17,6 giây | AGREE | C31; EXAMPLE:60 |
| 7 | L68 | 7:11:56; 7:22:30 | AGREE (số) | EXAMPLE:2. Ghi chú: 7:22:30 − 7:11:56 = 634 giây > 600 giây [A]; xem câu hỏi bảo vệ 8 |
| 8 | L63 | 15/11/2018, cùng khung | AGREE | C31 (d20181115-s10-r1-w07) |
| 9 | TikZ L30–59 | tọa độ: (a) 0,0310 cm/giây; (b) 0,0460 cm/giây | AGREE | [A]: 0,6 + 99,1 × 0,0310 = 3,673; 0,6 + 307,3 × 0,0310 = 10,127; 0,6 + 172,9 × 0,0460 = 8,553; 0,6 + 190,5 × 0,0460 = 9,363 (khớp tới 0,002 cm) |
| 10 | L75–76 | Alonso-González 2020; Wardman 2026 | AGREE | C2-18; C2-17 |
| 11 | L83 | 134 trong 203 khách | AGREE | C21; N-23; 4A:429 |
| 12 | L85 | 73,4\% | AGREE | C24; C4A-03; 4A:430, 443 |
| 13 | L85–86 | 23.027 trên 31.353 giây | AGREE | C4A-03 (23.027,239 / 31.353,407); 4A:416. [A] 23.027,239 / 31.353,407 = 0,7344 |
| 14 | L86 | 590,1 giây, gần mười phút | AGREE | C20; N-23; 4A:242, 407, 426; 4B:220 |
| 15 | Bảng 1.1 | 2020, 2022, 2026, 2026; công thức 7 | AGREE | J06; X3-40; C2-07; C2-08; C2-09; J03; C2-04 |
| 16 | L206–207 | 34 kịch bản; 3.672 yêu cầu | AGREE | B09; 4A:125, 241 |
| 17 | L207 | trần 30 giây mất 96 lượt | AGREE | C02; 4A:243–244 |
| 18 | L208 | +31 lượt không trễ quá một phút | AGREE ⚠ thiếu vế −5 ở hai phút | C08 (2.262 − 2.231); 4A:244–245 |
| 19 | L208–209 | luật hạn chót 30 giây phục vụ cùng số lượt | AGREE | C01 (2.338); 4A:277, 302 |
| 20 | L209 | 28 trong 34 kịch bản | AGREE (số) ⚠ khung | N-21; C13; 4A:327, 336. Cùng thước, luật C cũng 28/34: C4A-01; 4A:357–358 |
| 21 | L211 | 0 trong 20.760 quyết định bị ép (không trần) | AGREE | X3-16; 4A:343; 4B:360–361 |
| 22 | L212 | 292 trong 2.338 (12,5\%) | AGREE ⚠ câu đọc được thành "phục vụ 292" | C4A-01 (12,49\%); 4A:357 |
| 23 | L213 | 289 trong 2.338 (12,4\%) | AGREE | N-21 (12,36\%); 4A:327, 347, 357 |
| 24 | L212 | ngưỡng 30 giây, lời hứa đầu không dự báo | AGREE | C4A-01 (A − p₀ > 30.000 ms) |
| 25 | L213–214 | đệm 30 giây hòa ở một phút, hơn ở hai phút | AGREE | C10; N-16 (2.328 = 2.328; 2.366 > 2.338); 4B:217–218 |
| 26 | L214 | 37,2 thay vì 7,4 giây | AGREE | C10; N-16 (37,18 / 7,37); N-18; 4B:219, 254, 249 |
| 27 | L214–215 | gộp trên 2.434 và 2.338 khách | AGREE | N-16; N4B-10 |
| 28 | L215 | 132 lần chạy | AGREE | N-15; 4A:754 |
| 29 | L215 | 3 trong 1.780 bản ghi | AGREE | N-15; N-08; 4A:739, 754 |
| 30 | L216 | đều ở trần 120 giây | AGREE | N-08; L1a-06; 4A:711, 739 |
| 31 | L219 | "gộp trên 3.672 yêu cầu" | ⚠ nhãn sai cho các số 32 (đi chung), 35 (sớm), 37 (dài thêm) | N-09, N-16 tính trên khách được phục vụ |
| 32 | L222 | 2.434; 2.338; 2.338; 2.332 lượt chung | AGREE | C01; C04; 4A:275–277, 302 |
| 33 | L224 | 2.231; 2.262 | AGREE | C08; 4A:244, 275–276 |
| 34 | L225 | 555 trong 2.434; 313 trong 2.338 | AGREE | N-09; 4A:275–276 |
| 35 | L227–228 | 2.328 (cả hai); 2.338 và 2.366 | AGREE | C10; N-16; 4B:249, 254 |
| 36 | L228 | sớm quá một phút 4 trong 2.338; 44 trong 2.434 | AGREE | N-16; N4B-09; 4B:249, 254 |
| 37 | L230 | trần 120 giây: 2.387 lượt | AGREE | N-06; L1a-02; 4A:580 |
| 38 | L230 | 2.255; 2.366 | AGREE | N-06; 4A:585–586 |
| 39 | L230–231 | 2.322; 2.379 | AGREE | N-06; L1a-03; 4A:593–594 |
| 40 | L231 | 7,3 giây trên 2.387 khách | AGREE | N-06 (7,274); 4A:595 (7,27) |
| 41 | L233 | 132 = 98 + 34 | AGREE | E01 (98 = 34 + 64); N-15; 4A:736–739 |
| 42 | L249 | FleetPy 1.0.2 | AGREE | B01; X3-40; 4A:58 |
| 43 | L250 | 96 nút; thời gian đi cho từng cặp | AGREE | B03; K48; 4A:86 |
| 44 | L252 | 108 yêu cầu; 8 xe 4 chỗ | AGREE | B02; B03; 4A:62, 85 |
| 45 | L252–253 | 600 giây kể từ lúc gọi; 1,5 lần | AGREE | B03; C2-22; 4A:88 |
| 46 | L255 | khung 15 phút; 00:00 | AGREE | B06; B07; 4A:65, 91–92 |
| 47 | L258 | 34 kịch bản; năm ngày 14–18/11/2018 | AGREE | B08; B09; 4A:106, 125 |
| 48 | L73–74 | UberX Share không bảo đảm giờ đến; MOIA Express có khoảng giờ đến ngắn hơn, là lựa chọn nâng cấp | AGREE (định tính) | J28; J31; `r32-bib/BIB-VERIFICATION-v2.md`:53, 66 |
| 49 | Bảng 1.1 | Fielbaum: thấp điểm, kiểm soát giờ chờ; Elmi, Mt-KaRRi: thời gian đi cố định trên mỗi cạnh; Schulz–Pfeiffer: hạn neo vào lời mời, thời gian đi cho trước; DeeprETA: dữ liệu thời gian thực và lịch sử | AGREE (định tính) | J07; J08; C2-06; C2-08; C2-09; C2-07; C2-15 |

Hai chỗ thiếu số (không phải sai): Chương 1 không trích `engelhardt2026` cho FleetPy (L206, L249), và không trích
`uberxshare`, `moiaexpress` (L73–74).

---

## Thay đổi xếp hạng

Mỗi đoạn là văn bản thay thế dán thẳng vào tệp. M là bắt buộc, S là nên làm. Số dòng là số dòng của `05-chuong1-v3.tex`.

**Về trang.** Các thay đổi M1–M5 và S6–S9 làm văn xuôi dài thêm khoảng 800 tiếng (ước lượng thô, chưa dựng PDF), nên
Chương 1 sẽ vượt khoảng một trang so với 7 trang. Đề xuất bù như sau:
- Bỏ danh sách năm dòng kết quả ở L219–235. Mọi số của nó, trừ dòng trần 120 giây, nay đã nằm trong văn bản. Nếu cần giữ
  dòng trần 120 giây, đưa nó thành một câu ở cuối M4.
- Bỏ các cụm "Các mục … trả lời" trong CH1–CH3, vì Bảng 4.0 đã làm việc này.
- Nếu vẫn vượt, xin chủ nghiên cứu duyệt 8 trang cho Chương 1.

### Bắt buộc

**M1. Viết lại phần so với luật hạn chót cho công bằng.** Thay từ L208 «Luật hạn chót 30 giây phục vụ cùng số lượt, …»
tới hết L213 «… gộp theo khách.» (giữ câu «Khi có dự báo, …» cho S7).

```latex
Luật hạn chót không cho giờ trả mới muộn hơn lời hứa đầu quá 30 giây; nó mượn phần hạn chót của Schulz và
Pfeiffer~\cite{schulz2026}, nhưng ở mức chặt hơn nhiều so với 900 giây của bài gốc. Luật này cũng phục vụ 2.338
lượt. Đo bằng chính thước của nó, tức số khách tới muộn hơn lời hứa đầu không dự báo quá 30 giây, luật C có 292 và
luật hạn chót có 289 trong 2.338 khách được phục vụ (12,5\% và 12,4\%, gộp theo khách); mỗi luật đều có khách như vậy
ở 28 trong 34 kịch bản. Hai luật khác nhau ở điều chúng hứa. Luật hạn chót hứa cả phần thay đổi khi giữ nguyên kế
hoạch, nên ở 28 kịch bản đó nó không giữ được lời hứa của chính nó với ít nhất một khách. Luật C chỉ hứa phần tính
cho điều phối, nên theo cách xây dựng luôn giữ được trần của mọi khách, miễn là phương án giữ nguyên kế hoạch luôn
được sinh ra và qua mọi phép kiểm khác (giả thiết (N), mục~\ref{muc:giunguyen}). Đây không phải ưu thế về đúng giờ,
cũng không riêng luật C: điều phối không trần cũng không lần nào phải dùng luật phục hồi (0 trong 20.760 quyết
định), và theo định nghĩa, một hạn chót được nới theo kiểu Hörl và Zwick cũng có tính chất này (suy luận, chưa chạy).
% EV: A09; J10; J11; C01; C4A-01 (C-30 292/2.338 = 12,49%, 28/34); N-21 (M⁺-30 289/2.338 = 12,36%, 28/34); A22; K02; K05; X3-16; X3-30; 4A-v5-v3:252-253,326-327,357-358
```

**M2. Làm đủ khung "không nhận là mới".** Thay L237–241.

```latex
\begin{khungy}
\textbf{Khóa luận không nhận là mới.} Các ý sau đã có trong nghiên cứu trước hoặc trong thực tiễn: tính lại giờ trả
theo tuyến cũ với tốc độ hiện tại và nới hạn trả dựa trên giờ đó (Hörl và Zwick~\cite{horl2022}); đo mức thay đổi
của giờ hứa, chặn việc đổi giờ ngay khi chọn kế hoạch và đánh đổi giữa số khách phục vụ với độ ổn định (Fielbaum và
Alonso-Mora~\cite{fielbaum2020}); bảo vệ riêng từng khách (Elmi và cộng sự~\cite{elmi2026}); hạn chót tính từ giờ
trong lời mời khách đã nhận (Schulz và Pfeiffer~\cite{schulz2026}); lời hứa và dự báo giờ đến dựa trên
dữ liệu~\cite{hu2022}; chèn khách động, giới hạn giờ đến, gán lại xe, tương đồng tuyến (route similarity), cam kết tối
thiểu (least commitment), nhất quán thời gian (time consistency) và mức hài lòng của khách.

\textbf{Khóa luận không khẳng định} rằng luật C phục vụ nhiều hơn hay đúng giờ hơn: nó phục vụ bằng luật hạn chót, và
so với cách đệm 30 giây có dự báo, nó hòa ở ngưỡng một phút, kém ở ngưỡng hai phút. Luật C không bảo đảm giờ tới thực
tế; nó chỉ giới hạn phần tính cho điều phối. Sổ theo từng khách là phép tính trên mô hình, không cho biết ai có lỗi,
và phần còn lại không phải phần không thể biết trước. Kết quả không suy ra cho thành phố, mức tải hay mạng đường
khác; không mức trần nào được gọi là tốt nhất; khóa luận không xác nhận lợi ích kinh doanh hay mức hài lòng.

\textbf{Phần khóa luận làm:} đặc tả, cài đặt và kiểm một trần chung cho mọi khách đã có lời hứa trên tổng phần dời
giờ trả tính cho điều phối trong cả chuyến, kèm sổ theo từng khách; đo đánh đổi giữa số lượt phục vụ, số lượt không
trễ và độ dài lời hứa.
\end{khungy}
% EV: J38; J01; J03; C2-04; J06-J09; C2-06; C2-08; J10; C2-07; J35; C2-15; C01; C10; K05; K06; K19; K36; K38; I07; I10; D03:153-164
```

**M3. So với Hörl–Zwick cho công bằng.** Thay hàng Hörl–Zwick của Bảng 1.1 (L156–159) và đoạn cách đọc bảng (L190–192).

```latex
Hörl và Zwick (2022)~\cite{horl2022}
& Tính lại giờ trả theo tuyến cũ với tốc độ hiện tại; với khách trên xe sắp trễ, hạn trả được thay bằng giờ tính lại
nếu giờ này muộn hơn (công thức 7), kèm phạt phần vượt hạn gốc
& Hạn được nới theo giờ tính lại dưới tắc đường hiện tại
& Dùng cùng mốc để đo phần tính cho điều phối; luật kiểu này chưa được chạy làm đối chứng\\
% EV: J01; J03; C2-04; J05; K27; 4B-v10:445-446
```

```latex
Cách đọc bảng: các cách trong bảng đều bảo vệ lời hứa với khách, nhưng mỗi cách giới hạn một đại lượng khác. Tiền
lệ trực tiếp là Hörl và Zwick: khóa luận dùng lại cách tính giờ trả theo tuyến cũ với tốc độ hiện tại. Theo định
nghĩa, luật C khác ở ba điểm: một trần như nhau cho mọi khách đã có lời hứa, không chỉ cho khách trên xe sắp trễ; trần
chỉ tính phần tính cho điều phối nên không phải nới khi tắc đường; và các lần dời được cộng qua cả chuyến. Ba điểm
này suy từ hai định nghĩa, chưa phải kết quả so sánh: luật kiểu Hörl và Zwick chưa được chạy trên cùng các kịch bản,
và trên các lần chạy đã kiểm, phép cộng qua cả chuyến chưa lần nào là lý do riêng để loại một phương án ở trần 30
giây. Hai tác giả thử nghiệm trên nhu cầu thật của MOIA ở Hamburg, với tốc độ lấy từ dữ liệu GPS của TomTom, một
thiết lập khác hẳn thiết lập của khóa luận.
% EV: J01; J03; J05 (suy luận từ hai định nghĩa); C2-04; C2-05; K27; E01 (845 + 411 bản ghi, 0 chỉ do cộng dồn); N-26 (chiều tuyết 163, 0); N-08; 4B-v10:445-446; 4A-v5-v3:736-739
```

**M4. Nêu mục tiêu, nói RideBound và FleetPy là gì, đưa lại vế bất lợi.** Thay L198–199 và phần đầu đoạn đóng góp, từ
L202 «\noindent\textbf{Đóng góp …}» tới L208 «… so với lời hứa đầu không dự báo.». Phần còn lại của đoạn đã được M1 và
S7 thay.

```latex
\noindent\textbf{Mục tiêu.} Khóa luận nhắm tới một cam kết hẹp mà hãng xe có thể đưa ra và kiểm lại với từng khách:
kể từ lúc khách xác nhận đặt xe, tổng các lần bộ điều phối dời giờ trả của khách đó không vượt một mức cố định, ví dụ
30 giây, theo cách xây dựng luật, dù dự báo tắc đường đúng hay sai. Cam kết này không phải bảo đảm giờ tới: khách vẫn
có thể tới muộn khi đường chậm hơn lúc hứa. Cái giá của nó được đo bằng số lượt phục vụ và số khách đi chung.
% EV: A06; A13; X3-20; A22; N-28 (cuối tuần không dự báo, lớn nhất 29,2 s); F03; X3-11; K05; C02; N-20

\noindent\textbf{Đóng góp của khóa luận.} Khóa luận đặc tả và cài đặt luật C trong RideBound, bộ điều phối dùng
trong khóa luận (mục~\ref{muc:kientruc}). Với mỗi khách đã xác nhận đặt xe, tổng các lần dời giờ trả tính cho điều
phối trong cả chuyến, dời sớm hay muộn đều cộng, không được vượt một trần cố định; phương án làm vượt trần bị loại.
Mỗi lần dời được đo so với giờ trả nếu xe giữ kế hoạch cũ, tính lại theo thời gian đi hiện tại; mốc này đã có ở Hörl
và Zwick~\cite{horl2022}. Luật C đi cùng lời hứa theo dự báo, vốn đã có trong thực tiễn, và một sổ chia độ trễ theo
từng khách. Đây không phải một thuật toán mới, mà là một cam kết được đặc tả, cài đặt, kiểm và đo cái giá. Phép đo
dùng bộ mô phỏng mã nguồn mở FleetPy~\cite{engelhardt2026} với hệ số tắc đường chung cho cả thành phố lấy từ dữ liệu
Manhattan, trên 34 kịch bản, 3.672 yêu cầu. Với trần 30 giây, luật C phục vụ ít hơn điều phối không trần 96 lượt.
Số lượt không trễ quá một phút so với lời hứa đầu tăng 31, từ 2.231 lên 2.262, nhưng số lượt không trễ quá hai phút
giảm 5, từ 2.332 xuống 2.327.
% EV: A06; A13; K43; A01; A02; X3-27; J01; J03; C2-04; J35; C2-15; F09; X3-12; OUTLINE §0 dòng 5; B01; X3-40; B06; K49; B09; C02; C08 (2.231/2.262; 2.332/2.327); 4A-v5-v3:241-245
```

**M5. Định nghĩa ba phần bằng một ví dụ trước khi dùng số; dời đoạn số động cơ ra sau.** Thay L83–92 bằng hai đoạn dưới
đây theo thứ tự: đoạn định nghĩa, rồi Hình 1.2 (giữ nguyên, chỉ sửa nhãn theo chỗ khó 26), rồi đoạn số. Giữ L116–117 sau
đoạn số.

```latex
Khóa luận chia độ lệch giữa giờ tới thực tế và lời hứa đầu thành ba phần (Hình~\ref{hinh:c1-baphan}). Phần thứ
nhất là phần tính cho điều phối. Mỗi lần bộ điều phối đổi kế hoạch của một xe, hệ thống tính cho từng khách trên
xe hai giờ trả, với cùng vị trí xe và cùng thời gian đi hiện tại: giờ trả nếu xe giữ kế hoạch cũ, và giờ trả theo kế
hoạch mới. Hiệu của hai giờ này là phần tính cho điều phối. Ví dụ dựng tay: lời hứa đang là 9:10:00; nếu giữ kế
hoạch cũ, khách tới lúc 9:10:40; theo kế hoạch mới có thêm một khách, khách tới lúc 9:11:10. Khi đó 40 giây thuộc
phần thay đổi khi giữ nguyên kế hoạch và 30 giây thuộc phần tính cho điều phối. Luật C đặt cho mỗi khách một mức tối
đa, gọi là trần, cho tổng các lần dời thuộc phần này trong cả chuyến; dời sớm hay dời muộn đều cộng vào. Phần thứ
hai là phần mà mức tắc đường quen thuộc của khung giờ, lấy trung bình từ các ngày trước, giải thích được; phần này
được cộng sẵn vào lời hứa ngay lúc hứa, gọi là lời hứa theo dự báo. Phần thứ ba là phần còn lại; nó được ghi vào sổ
riêng của từng khách, gọi là sổ theo từng khách, để biết dự báo đang dùng còn bỏ sót bao nhiêu.
% EV: A01; A02; X3-27; X3-37 (ví dụ dựng tay x = 40, c = 30, z = 70); A06; F01; F02; F09; X3-12; K04
```

```latex
Các số dưới đây cho thấy phần thứ nhất lớn đến đâu khi không có trần. Trên tập kiểm tra chính
(mục~\ref{muc:c1-phamvi}), khi bộ điều phối không bị giới hạn phần dời giờ trả nhưng vẫn không được đổi xe, điểm
đón, điểm trả và giờ đón đã hứa, có 203 khách tới muộn hơn lời hứa đầu quá một phút. 134 người trong số đó từng bị
bộ điều phối dời giờ trả; con số chỉ cho biết hai nhóm trùng nhau, không cho biết việc bị dời là nguyên nhân làm họ
trễ. Theo sổ theo từng khách, 23.027 trong 31.353 giây trễ của cả 203 khách, tức 73,4\%, thuộc phần tính cho điều
phối. Trong 2.434 khách được phục vụ, khách bị dời nhiều nhất có giờ trả bị dời tổng cộng 590,1 giây, gần 10 phút.
% EV: B09; A07; A08; C06; C21; C24; C4A-03 (23.027,239 / 31.353,407 s); C20; 4A-v5-v3:416,429-430,443
```

### Nên làm

**S6. Phạm vi: nói rõ dữ liệu đã xem, tải thấp, và trần chưa tách khỏi bộ chọn.** Thay hai gạch đầu dòng «Dữ liệu kiểm
tra» và «Ngoài phạm vi» (L258–263), và thêm một gạch đầu dòng ở giữa.

```latex
\item \textbf{Dữ liệu kiểm tra:} tập chính gồm 34 kịch bản của năm ngày 14--18/11/2018; dự báo chỉ có ở 21 kịch bản
ngày thường. Các khung giờ và mẫu nhu cầu có phần chồng nhau, nên không phải 34 quan sát độc lập. Ngưỡng phân tích
được chọn sau khi đã xem dữ liệu của các đợt chạy trước, và mức trần 120 giây được chọn sau khi đã xem kết quả trên
chính tập này, nên mọi kết quả là thăm dò.
% EV: B08; B09; B11; I05; C09; F02; I06; C4A-11; 4A-v5-v3 mục muc:c4-thamdo
\item \textbf{Tải và thời gian dừng:} khi không trần, trung bình 0,535 khách trên mỗi xe kể cả lúc xe rỗi, thấp hơn
nhiều mức khoảng 1,33 trong nghiên cứu điển hình của FleetPy; thời gian dừng đón, trả bằng 0 giây. Kết quả không suy
ra cho tải cao hơn.
% EV: B12 (LOAD:2-3; FLEET:447-449); B05 (kiểm trên 3 lần chạy mẫu)
\item \textbf{Ngoài phạm vi:} không có mô hình khách hủy chuyến hay từ chối lời mời; không chuyển khách đã nhận sang
xe khác; không kiểm khả năng mở rộng sang mạng lớn hoặc hiệu quả kinh doanh. Luật C và điều phối không trần dùng
chung một cách chọn phương án ưu tiên ổn định; phép thử đổi sang cách chọn ưu tiên chi phí chưa được chạy, nên chưa
tách được phần của trần với phần của cách chọn. Lời hứa theo dự báo chỉ được tính lại trên các lần chạy đã ghi; nó
không làm thay đổi xe nào chở ai.
% EV: I07; X3-39; B04; I01; I10; H01; H02; H12; 4B-v10:19-22,71-73; F03; X3-12
```

**S7. Câu đệm và câu cộng dồn viết bằng lời, thêm "0 lần ở trần 30 giây".** Thay từ L213 «Khi có dự báo, …» tới hết
L216.

```latex
Khi lời hứa tính theo dự báo, chỉ cần cộng thêm 30 giây vào mọi lời hứa của điều phối không trần là có cùng 2.328
lượt không trễ quá một phút như luật C, và nhiều hơn ở ngưỡng hai phút (2.366 so với 2.338, trên 3.672 yêu cầu).
Đổi lại, lời hứa dài thêm trung bình 37,2 giây thay vì 7,4 giây (gộp trên 2.434 và 2.338 khách được phục vụ), và
cách đệm không giới hạn phần dời của từng khách. Phép cộng các lần dời qua cả chuyến hiếm khi là lý do riêng để loại
một phương án: trên 132 lần chạy luật C đã kiểm toàn bộ bản ghi, chỉ 3 trong 1.780 lần loại phương án được ghi lại
xảy ra vì phép cộng này, cả ba ở trần 120 giây, không lần nào ở trần 30 giây. Tác dụng của phép cộng lên kết quả
chưa được đo.
% EV: C10; N-16; N-18; K06; K51; C20 (đệm không đổi quyết định: 174 khách vẫn bị dời, 4B-v10:219-220); N-15; N-08; E01; E09; 4A-v5-v3:736-739,754
```

**S8. Ví dụ ở mục 1.1: định nghĩa lời hứa đầu, bỏ "kịch bản phát triển" và "trần" chưa giải thích, gỡ hai số 99,1.**
Thay L14–17, L20–23, L68–70. Sửa nhãn hình: L29 thành «(a) Khách trễ nhất khi cho dời tối đa 300 giây»; L42 thành
«+99,1»; L44 thành «(b) Một khách khác: lời hứa tính sẵn mức tắc đường quen thuộc». Trong chú thích L62, thay «hai đoạn
là tổng các phần ghi trong sổ» bằng «hai đoạn là tổng các phần của khách này qua mọi lần cập nhật lời hứa».

```latex
Trong dịch vụ đi chung xe (ride-pooling), một phần mềm gọi là bộ điều phối (dispatcher) xếp nhiều khách vào cùng một
xe và sửa kế hoạch chạy của xe mỗi khi có yêu cầu mới. Vì vậy, giờ trả đã báo cho khách, gọi là lời hứa giờ trả hay
gọn là lời hứa, có thể đổi vì hai lẽ. Xe có thể nhận thêm điểm dừng để đón, trả khách mới. Ngay cả khi xe giữ nguyên
kế hoạch, đường đi nhanh hay chậm hơn lúc hứa cũng làm giờ tới thay đổi. Giờ trả báo lúc khách xác nhận đặt xe gọi là
lời hứa đầu. Muốn giới hạn việc sửa lời hứa thì trước hết phải tách được hai phần này.
% EV: J17; A01; A02; A13; J01; J06
```

```latex
Hai khách trong bản ghi mô phỏng ở Hình~\ref{hinh:c1-loihua} cho thấy sự khác nhau đó. Khách ở hình trên thuộc một
kịch bản dùng khi xây dựng phương pháp (ngày 13/11/2018), ở cấu hình cho phép bộ điều phối dời giờ trả của mỗi khách
tổng cộng tới 300 giây. Đây là khách trễ nhất của kịch bản: tới nơi muộn hơn lời hứa đầu 307,3 giây, gồm 99,1 giây
thay đổi trong khi xe giữ kế hoạch cũ và 208,2 giây chênh lệch giữa kế hoạch mới mà bộ điều phối chọn và kế hoạch
cũ. Nếu chỉ cho dời tổng cộng 30 giây, khách trễ nhất của cùng kịch bản là một người khác, tới muộn 99,1 giây, trong
đó 97,1 giây thay đổi trong khi xe giữ kế hoạch cũ. Số 99,1 giây này chỉ tình cờ trùng với phần tương ứng của khách
ở hình trên.
% EV: D06; N-30; W07:48-53; q4-rider-2026-09-30.txt:3,9 (khách cực đại của hai cấu hình khác nhau)
```

```latex
Khách ở hình dưới đặt xe lúc 7:11:56, được hứa tới nơi lúc 7:34:51 nhưng tới thật lúc 7:38:02, muộn 190,5 giây.
Nếu lúc hứa, hệ thống cộng sẵn mức tắc đường quen thuộc của khung giờ này, lấy trung bình từ các ngày trước, thì lời
hứa là 7:37:44, dài hơn 172,9 giây, và khách chỉ còn trễ 17,6 giây. Ví dụ này cho thấy dự báo giúp gì và tốn gì; nó
không nói gì về giới hạn đặt cho bộ điều phối.
% EV: C31; EXAMPLE:1-3,60-61; F01; F02; REVIEW-DECISIONS-R20 LR-15
```

**S9. Nguồn từ hãng xe và từ người đi xe: thêm trích dẫn và con số.** Thay L73–77. Khóa `uberxshare` và `moiaexpress` đã
có trong `r32-bib/10-tai-lieu-draft-v2.tex:133,140`.

```latex
Các hãng xe cũng nói rõ giờ tới của xe đi chung khó giữ. Trang giới thiệu UberX Share cho biết đi chung mất thêm
trung bình 8 phút và hãng không bảo đảm giờ tới~\cite{uberxshare}; MOIA giới thiệu gói Express, với khoảng giờ tới
hẹp hơn, như một lựa chọn nâng cấp có trả thêm~\cite{moiaexpress}. Về phía người đi xe, khảo sát 1.006 người ở Hà
Lan của Alonso-González và cộng sự~\cite{alonsogonzalez2020} cho thấy người dùng dịch vụ đi chung có tính tới độ ổn
định của thời gian đi khi chọn dịch vụ. Tổng hợp nhiều nghiên cứu về đi lại của Wardman và cộng
sự~\cite{wardman2026} cho thấy một phút tới muộn so với giờ dự kiến được tính nặng bằng khoảng 2,53 đến 3,12 phút ngồi
trên xe, tùy cách hỏi. Các nghiên cứu này nói về giờ tới nói chung; chúng không cho biết khách coi trọng giới hạn mà
khóa luận đặt cho bộ điều phối đến mức nào.
% EV: J28; J31; r32-bib/BIB-VERIFICATION-v2.md:53,66 (MOIA: optional paid upgrade, shorter arrival window; UberX Share: 8 phút trung bình, không bảo đảm giờ tới); J24; C2-18; J23; C2-17; I07; I10
```

**S10. Ba câu hỏi nghiên cứu: mỗi câu một ý, định nghĩa từ khó ngay trong câu, sửa "câu hỏi không suy ra".** Thay L120–128.
Cần sửa Bảng 4.0 (4A-v5-v3, `bang:c4-lotrinh`) theo cùng cách viết.

```latex
\item[CH1.] Phần dời giờ trả tính cho điều phối được đo thế nào và kiểm vào lúc nào; một trần trên phần này giữ được
gì cho khách và không giữ được gì? Mục~\ref{muc:luatc} nêu luật; các mục~\ref{muc:c4-dieuphoi},
\ref{muc:c4-congdon} và~\ref{muc:c4-hople} kiểm nó. Câu trả lời không bao gồm bảo đảm về giờ tới thực tế.
\item[CH2.] Trên các tập kịch bản đã chạy, khi áp trần, số lượt phục vụ, số lượt không trễ quá một và hai phút, và độ
dài lời hứa thay đổi thế nào so với ba cách khác: điều phối không trần; luật hạn chót, tức không cho giờ trả muộn hơn
lời hứa đầu quá một mức cố định; và cách đệm, tức cộng thêm một khoảng cố định vào mọi lời hứa? Các
mục~\ref{muc:c4-ketqua}, \ref{muc:c4-chontran}, \ref{muc:c4-vaitro} và~\ref{muc:c4-dem} trả lời. Kết quả không tách
được phần của trần với phần của cách chọn phương án, và không chỉ ra mức trần tốt nhất.
\item[CH3.] Khi lời hứa tính sẵn mức tắc đường quen thuộc của khung giờ, số lượt không trễ quá một phút thay đổi thế
nào, và phần trễ nào dự báo này vẫn chưa giải thích được? Các mục~\ref{muc:dubao}, \ref{muc:so}, \ref{muc:c4-dubao}
và~\ref{muc:c4-tuyet} trả lời. Kết quả không cho biết khách sẽ phản ứng ra sao.
% EV: OUTLINE-V2 cuối §1.2; K05; K19; H02; I07; 4A-v5-v3 bang:c4-lotrinh
```

### Sửa nhỏ, không xếp hạng

- Thống nhất tên gọi theo bảng thuật ngữ:
  - "phần tính cho điều phối" (bỏ "trần điều phối", "độ dời … do điều phối");
  - "phần thay đổi khi giữ nguyên kế hoạch";
  - "luật hạn chót" (bỏ "hạn chót" trần ở L213, L222);
  - "điều phối không trần" ở lần đầu mỗi đoạn;
  - "tắc đường" (bỏ "giao thông" ở L153, L158, L159);
  - "phá lời hứa" (bỏ "phá luật").
- Các chỗ 31–36, 48–54 ở Phần 1. Phần lớn chỉ cần thay một cụm.
- L171: ghi hàng Mt-KaRRi theo mẫu tác giả, năm. Chú thích Bảng 1.1: bỏ "Nội dung viết bằng lời".
- Sau khi ghép, dựng PDF để đo số trang thật. NOTES §7 của Codex đã nêu đúng rằng chưa có bản dựng.
