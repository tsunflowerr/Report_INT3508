# R25: đọc nửa đầu Chương 4 (mục 4.1–4.5) với hai vai, người đọc ngoài ngành và giảng viên hội đồng

- Tệp được đọc: `drafts/08-chuong4-phanA.tex`, 785 dòng, đọc hết, kể cả dòng `%` ẩn.
- Tài liệu phụ: `drafts/07-chuong3-v3.tex`, chỉ dòng 1–80 (đoạn mở chương và Bảng thuật ngữ); chương 4 của
  báo cáo mẫu `23020155_TranQuangThanh_Bao cao DACN.pdf` (trang in 29–34).
- Không đọc: `08-chuong4-phanA-NOTES.md`, `codex-work/R25-*`, các tệp `reviews/*CH4A*` khác, sổ bằng chứng.
- Quy ước: "dòng N" là số dòng trong `08-chuong4-phanA.tex`. Câu viết lại giữ nguyên nghĩa và mọi con số. Chỗ
  tác giả phải điền hoặc kiểm lại thì ghi trong ngoặc vuông `[...]`. Mọi câu khẳng định tôi đều dựa trên chữ
  có trong tệp. Khi tự suy ra từ các con số của bản nháp, tôi ghi rõ là "suy ra".
- Số bảng là thứ tự xuất hiện trong phần A: 4.1 lộ trình, 4.2 tham số, 4.3 các tập, 4.4 chỉ số, 4.5 kết quả
  chính, 4.6 nghĩa vụ, 4.7 phân bố trễ, 4.8 ngày–khung, 4.9 dời do điều phối, 4.10 tắc đường cố định, 4.11 buổi
  sáng, 4.12 trần 120 giây, 4.13 cộng dồn. Hình 4.1 là hình mức trần.

---

## PHẦN 1. Người đọc ngoài ngành

Tôi là sinh viên năm cuối, không học ngành này. Tôi đọc tuần tự và có Bảng thuật ngữ của chương 3 bên cạnh.
Bảng đó định nghĩa: lượt quyết định, phương án, phương án giữ nguyên kế hoạch, bộ sinh, bộ chọn, lời hứa,
$p_0$, khóa, trần $B$, $L_r$, quyết định bị ép, luật phục hồi, hệ số tắc đường, kịch bản. Những thuật ngữ còn
lại tôi chỉ hiểu được nếu Chương 4 giải thích.

Mỗi chỗ khó hiểu được ghi theo khuôn: **Dn, dòng.** Gốc / Vì sao khó / Viết lại.

### Mở chương và Bảng lộ trình (dòng 11–47)

**D1, dòng 15–18.** Gốc: "Các mục đi theo ba phần của độ lệch giờ trả. Phần do điều phối ở mục…; phần được
hồ sơ lịch sử giải thích, cùng cách đệm lời hứa, ở mục…; phần còn lại ở mục…"
Vì sao khó: tôi chưa biết "ba phần" là gì. "Hồ sơ lịch sử" nghe như hồ sơ bệnh án. "Đệm lời hứa" chưa được
giải thích.
Viết lại: "Giờ trả thực tế có thể lệch khỏi lời hứa vì ba nguồn. Thứ nhất, bộ điều phối ghé đón thêm khách
(phần do điều phối). Thứ hai, đường đông theo nhịp quen thuộc trong ngày mà số liệu tắc đường lịch sử dự báo
được (phần dự báo được). Thứ ba, mọi biến động khác (phần còn lại). Phần do điều phối được xét ở
mục~\ref{muc:c4-ketqua}--\ref{muc:c4-vaitro}. Phần dự báo được, cùng cách đệm lời hứa (cộng sẵn một khoảng
thời gian cố định vào giờ hứa), được xét ở mục~\ref{muc:c4-dubao} và~\ref{muc:c4-dem}. Phần còn lại được xét ở
mục~\ref{muc:c4-tuyet}." [Kiểm lại xem định nghĩa "đệm" có đúng như ở mục c4-dem không.]

**D2, dòng 31–43 (Bảng 4.1, cột "Đại lượng được đo").** Gốc: "yêu cầu bị từ chối có bản ghi chặn, vế cộng
dồn, các bộ đếm kiểm tra"; "quyết định phải phục hồi, … thứ tự tiêu chí của bộ chọn"; "ba phần của sổ".
Vì sao khó: bảng ở trang đầu chương mà có năm thuật ngữ chưa ai giải thích ("bản ghi chặn", "vế cộng dồn",
"bộ đếm kiểm tra", "quyết định phải phục hồi", "sổ").
Viết lại cột 3, giữ nguyên ý:
- CH1: "Bao nhiêu khách bị dời giờ trả vì ghép thêm khách, dời tối đa bao lâu; những yêu cầu bị từ chối vì
  vướng trần; trần có thật sự cộng các lần dời qua cả chuyến không; các phép kiểm số liệu."
- CH2: "Số lượt phục vụ; số lượt trễ và không trễ so với lời hứa đầu; số lần luật loại hết phương án của một
  xe; các mức trần; thứ tự ưu tiên của bộ chọn; lời hứa dài thêm bao nhiêu."
- CH3: "Số lượt trễ khi lời hứa có và không có dự báo; dự báo làm lời hứa dài thêm bao nhiêu; độ trễ chia
  theo ba nguồn trên ngày thường và chiều có tuyết."

### 4.1.1 Kịch bản thử (dòng 53–98)

**D3, dòng 56–57.** Gốc: "nối với bộ chạy RideBound qua bộ chuyển đổi ở mục~\ref{muc:kientruc}".
Vì sao khó: tôi không biết "bộ chạy" và "bộ chuyển đổi" là gì, và cái nào làm gì.
Viết lại: "FleetPy giả lập xe chạy và khách gọi xe. Ở mỗi lượt quyết định, nó chuyển tình trạng hiện tại sang
chương trình RideBound của khóa luận (bộ chạy) qua một lớp nối (bộ chuyển đổi, mục~\ref{muc:kientruc}) và nhận
lại quyết định."

**D4, dòng 58–60.** Gốc: "Một kịch bản (scenario) là một tổ hợp ngày, mẫu nhu cầu và khung giờ hai tiếng: 108
yêu cầu được lấy từ một mẫu 10\% số chuyến của khung đó…"
Vì sao khó: (a) Câu có từ tiếng Anh trong ngoặc, trong khi chương 3 (dòng 35) hứa "tên tiếng Anh chỉ ghi
trong bảng". (b) Không rõ "mẫu nhu cầu" là gì, và mỗi ngày có mấy mẫu. (c) Mẫu 10\% số chuyến taxi trong hai
giờ ở Manhattan có lẽ nhiều hơn 108 chuyến nhiều, vậy 108 được chọn bằng cách nào?
Viết lại: "Một kịch bản gồm một ngày, một khung giờ hai tiếng và một mẫu nhu cầu, tức một mẫu 10\% số chuyến
taxi của khung đó, có sẵn trong bộ dữ liệu [mỗi ngày có … mẫu]. Từ mẫu này lấy 108 yêu cầu [cách lấy] và phục
vụ chúng bằng 8 xe 4 chỗ."

**D5, dòng 63–64.** Gốc: "…dưới đây gọi là hệ số tắc đường đo."
Vì sao khó: "đo" đứng cuối cụm danh từ nên dễ đọc nhầm thành động từ ("hệ số tắc đường [thì] đo…").
Viết lại: "Mô phỏng không có tốc độ riêng cho từng con đường. Cứ mỗi 15 phút, mọi thời gian đi trong thành phố
được nhân với cùng một hệ số, tính từ dữ liệu chuyến taxi. Ví dụ, hệ số 1,2 làm mọi chuyến đi lâu gấp 1,2
lần. Dưới đây gọi đó là hệ số tắc đường đo được, để phân biệt với hệ số giữ cố định của tập ở
mục~\ref{muc:c4-taptu}." (Ví dụ 1,2 lấy từ Bảng thuật ngữ chương 3.)

**D6, dòng 64–65.** Gốc: "Mỗi cặp kịch bản và cấu hình chạy một lần, cho một kết quả tất định."
Vì sao khó: "tất định" là từ chuyên ngành.
Viết lại: "Mỗi kịch bản chạy một lần với mỗi cấu hình. Chạy lại cùng kịch bản với cùng cấu hình cho đúng kết
quả cũ."

**D7, dòng 65–66.** Gốc: "Ba khung giờ của cùng ngày và cùng mẫu trùng nhau 3 đến 20 trong 108 yêu cầu, nên các
kịch bản không phải các mẫu độc lập."
Vì sao khó: "trùng nhau 3 đến 20 trong 108 yêu cầu" khó hiểu. Khung 7–9 giờ và 8–10 giờ có chung giờ 8–9 nên
dễ hiểu vì sao có yêu cầu chung, nhưng khung 17 giờ thì không giao với hai khung kia.
Viết lại: "Các kịch bản cùng ngày, cùng mẫu có chung từ 3 đến 20 trong 108 yêu cầu [giải thích vì sao, nhất là
với khung 17 giờ]. Vì thế chúng không phải những phép thử độc lập với nhau."

**D8, dòng 83–84 (Bảng 4.2).** Gốc: "96 nút, là bao đóng các cặp điểm đi, điểm đến lấy từ dữ liệu Manhattan,
không phải mạng đường phố".
Vì sao khó: "bao đóng" là thuật ngữ toán.
Viết lại: "96 nút, gồm các điểm đi và điểm đến có trong dữ liệu Manhattan [và thời gian đi giữa từng cặp điểm];
đây là đồ thị rút gọn, không phải bản đồ đường phố thật." [Nếu "bao đóng" mang một nghĩa kỹ thuật khác thì
giải thích nghĩa đó bằng lời thường.]

**D9, dòng 87.** Gốc: "0 giây (kiểm trên 3 lần chạy mẫu)".
Vì sao khó: không rõ đã kiểm điều gì.
Viết lại: "0 giây: xe không mất thời gian khi khách lên, xuống [đã kiểm … trên 3 lần chạy mẫu]."

**D10, dòng 88–89.** Gốc: "mức nền lấy lúc 00:00 cho mọi kịch bản".
Vì sao khó: "mức nền" là gì, và để làm gì?
Viết lại: "[Hệ số lúc 00:00 được dùng làm mức gốc cho mọi kịch bản; hệ số các khung khác tính so với mức này.]"
(Tôi đoán nghĩa này, tác giả cần kiểm.)

**D11, dòng 91.** Gốc: "hạt giống ngẫu nhiên cố định 7".
Vì sao khó: "hạt giống" dịch sát nghĩa nên khó hiểu.
Viết lại: "giá trị khởi tạo bộ sinh số ngẫu nhiên cố định bằng 7, để mỗi lần chạy lại cho cùng kết quả".

### 4.1.2 Các tập kịch bản (dòng 100–146)

**D12, dòng 103–105.** Gốc: "34 trong 49 kịch bản dựng được từ các ngày 14--18/11/2018; 15 kịch bản còn lại, chia
theo cặp ngày và mẫu, dành cho hiệu chỉnh và không dùng ở đây."
Vì sao khó: "dựng được", "chia theo cặp ngày và mẫu" và "hiệu chỉnh [cái gì]" đều chưa rõ.
Viết lại: "Từ các ngày 14--18/11/2018 dựng được 49 kịch bản. Các kịch bản được chia theo từng cặp (ngày, mẫu),
nên mọi kịch bản cùng ngày, cùng mẫu rơi vào cùng một phía. 15 kịch bản được để riêng cho việc hiệu chỉnh
[cái gì] và không dùng trong chương này; 34 kịch bản còn lại là tập kiểm tra chính."

**D13, dòng 115–132 (Bảng 4.3, các tập).** Gốc: cột "Bộ chạy" ghi "Bản lưu trữ, luật phục hồi không tệ hơn",
"Như tập chính", "Bản cũ, không có luật phục hồi", "Chưa kiểm lại"; cột "Lần chạy" ghi "88 và 104"; dòng chiều
tuyết ghi "601 lượt phục vụ".
Vì sao khó: (a) Tôi không biết "bản lưu trữ" và "bản cũ" khác nhau ra sao, và "luật phục hồi không tệ hơn" là
gì. (b) "88 và 104" không nói con số nào ứng với cấu hình nào. (c) Ba dòng trên ghi số yêu cầu, riêng dòng chiều
tuyết ghi số lượt phục vụ, nên tôi không so được với các dòng khác.
Viết lại: đổi tên cột thành "Phiên bản bộ chạy" và thêm một câu dưới bảng: "Bản lưu trữ là [ …]; luật phục hồi
'không tệ hơn' nghĩa là [một câu nhắc từ chương 3]; bản cũ là [ …]." Ghi "88 (… ) và 104 (… )". Dòng chiều tuyết
ghi "8 kịch bản, 864 yêu cầu (601 lượt phục vụ dưới C-30)".

**D14, dòng 137–140.** Gốc: "Điều phối không trần, luật hạn chót và luật trần độ dời khách thấy dùng cùng bộ
sinh, bộ kiểm và bộ chọn với luật C… Ghép tự do dùng chính sách chi phí cuốn chiếu mặc định, không qua bộ
kiểm cứng."
Vì sao khó: từ đây trở đi các bảng chỉ dùng ký hiệu U, C-30, M$^{+}$-30, V-30, FREE, nhưng không câu nào trong
Chương 4 nói ký hiệu nào ứng với luật nào. Chỉ có câu "Ký hiệu cấu hình theo Bảng~\ref{bang:luat}" (dòng 110)
bảo tôi lật lại chương 3. "Chi phí cuốn chiếu", "bộ kiểm cứng" và "trần độ dời khách thấy" đều khó hiểu.
Viết lại, dạng danh sách:
"Các cấu hình được so và ký hiệu trong bảng:
- U: điều phối không trần. Giống luật C trần 30 giây ở mọi điểm, trừ việc không có trần giờ trả.
- C-$B$: luật C với trần $B$ giây; ví dụ C-30 là trần 30 giây.
- M$^{+}$-$B$: luật hạn chót $B$ giây. Luật loại phương án làm giờ trả muộn hơn lời hứa đầu quá $B$ giây.
- V-30: luật trần độ dời khách thấy 30 giây. Luật giới hạn tổng độ thay đổi của giờ trả được báo cho khách [kiểm
  lại theo chương 3].
- FREE: ghép tự do. Ở mỗi lượt, chọn phương án có chi phí thấp nhất (chính sách chi phí cuốn chiếu mặc định)
  và không kiểm lời hứa nào [kiểm lại].
U, C, M$^{+}$ và V dùng chung bộ sinh phương án, bộ kiểm và bộ chọn."

**D15, dòng 143–145.** Gốc: "lần chạy hỏng được thay bằng bản chạy lại hoàn tất".
Ý hiểu được. Nên ghi thêm có bao nhiêu lần chạy hỏng (một con số), để người đọc khỏi phải đoán.

### 4.1.3 Chỉ số (dòng 148–200)

**D16, dòng 151.** Gốc: "Chỉ số đúng giờ tính so với lời hứa đầu và chỉ trên khách được phục vụ".
Vì sao khó: câu này mâu thuẫn bề ngoài với Bảng 4.4 (dòng 179–180). Theo bảng đó, chỉ số "Không trễ quá $T$"
được "chia cho số yêu cầu", tức tính trên cả yêu cầu bị từ chối.
Viết lại: "Độ trễ chỉ đo được ở khách được phục vụ, và luôn so với lời hứa đầu. Riêng chỉ số 'không trễ quá
$T$' lấy mẫu số là toàn bộ yêu cầu, để yêu cầu bị từ chối không được tính là đúng giờ."

**D17, dòng 152–153.** Gốc: "ngưỡng 120 giây được báo kèm vì có phép so mà hai ngưỡng cho kết luận ngược
nhau."
Vì sao khó: "có phép so" là phép so nào?
Viết lại: "Ngưỡng 120 giây được báo kèm vì có phép so đổi kết luận khi đổi ngưỡng. Ví dụ, luật C trần 30 giây
có nhiều hơn điều phối không trần 31 lượt không trễ quá 60 giây, nhưng ít hơn 5 lượt không trễ quá 120 giây
(mục~\ref{muc:c4-ketqua})."

**D18, dòng 153–155.** Gốc: "Tỉ lệ \emph{gộp theo khách} chia tổng số khách thỏa điều kiện cho tổng số khách được
phục vụ; \emph{trung bình theo kịch bản} là trung bình không trọng số của tỉ lệ từng kịch bản."
Vì sao khó: chỉ có định nghĩa, không có ví dụ. "Không trọng số" là thuật ngữ thống kê.
Viết lại, thêm một ví dụ giả định ghi rõ là ví dụ: "Ví dụ, kịch bản A có 5 trong 10 khách thỏa điều kiện,
kịch bản B có 5 trong 90. Gộp theo khách cho 10/100 = 10\%. Trung bình theo kịch bản cho (50\% + 5,6\%)/2 =
27,8\%, vì mỗi kịch bản được tính nặng như nhau dù đông hay vắng khách."

**D19, dòng 158–161.** Gốc: "Kết quả 'có dự báo' là phép phát lại trên các lần chạy đã ghi".
Vì sao khó: "phép phát lại" là gì?
Viết lại: "Kết quả 'có dự báo' không đến từ lần chạy mới. Ta lấy lại đúng các lần chạy đã ghi, giữ nguyên mọi
quyết định điều phối, chỉ thay lời hứa đầu bằng lời hứa tính theo dự báo, rồi đo lại độ trễ (phát lại). Vì
vậy bộ điều phối không hề 'biết' về dự báo."

**D20, dòng 166–167 (chú thích Bảng 4.4).** Gốc: "so sánh 'quá' là so sánh chặt."
Vì sao khó: "so sánh chặt" là thuật ngữ toán.
Viết lại: "'Trễ quá 60 giây' nghĩa là trễ hơn hẳn 60 giây; trễ đúng 60 giây thì không tính."

**D21, dòng 175–176.** Gốc: "Lượt phục vụ | Yêu cầu được nhận và chở tới nơi | Đếm trên số yêu cầu".
Vì sao khó: "đếm trên số yêu cầu" khó hiểu, vì một số đếm thì không cần mẫu số.
Viết lại: cột mẫu số ghi "Số đếm; tỉ lệ phục vụ = lượt phục vụ / số yêu cầu".

**D22, dòng 186 và 191.** Gốc: "độ dời là $\sum|c|$"; "luật trần độ dời khách thấy: $\sum|z| > B$".
Vì sao khó: Chương 4 không định nghĩa $c$ và $z$, Bảng thuật ngữ chương 3 cũng không có.
Viết lại, thêm vào chú thích bảng: "$c$ là một lần dời giờ trả do điều phối, tính bằng giây (dương là muộn đi);
$z$ là [một lần thay đổi giờ trả mà khách được báo, theo chương 3]."

**D23, dòng 188–190.** Gốc: "Quyết định phải phục hồi".
Vì sao khó: Bảng thuật ngữ chương 3 (dòng 63–64) gọi cùng khái niệm này là "quyết định bị ép (forced decision)".
Hai tên khác nhau làm tôi tưởng đó là hai thứ khác nhau.
Viết lại: dùng một tên thống nhất ở cả hai chương. Nếu giữ "quyết định phải phục hồi" thì sửa Bảng thuật ngữ
chương 3 cho khớp.

**D24, dòng 191–193 và tiêu đề cột dòng 291.** Gốc: "Khách bị chính luật phá lời hứa".
Vì sao khó: "chính luật" nghe như dịch máy.
Viết lại: "Khách mà luật không giữ được điều nó hứa".

**Chung cho cả mục 4.1.3.** Bản nháp dùng "khách", "yêu cầu" và "lượt" thay cho nhau. Nên thêm một câu: "Mỗi
yêu cầu là một khách. Một lượt phục vụ là một yêu cầu được chở tới nơi. Một lượt trễ là một khách được phục
vụ nhưng tới muộn."

### 4.1.4 Mức trần 30 giây (dòng 202–214)

**D25, dòng 205–206.** Gốc: "là mức đã dùng cho cấu hình có trần ở tập kịch bản tĩnh trước đó (Phụ lục~\ref{phuluc:A})".
Vì sao khó: "tập kịch bản tĩnh" không có trong bốn tập của Bảng 4.3.
Viết lại: "Trần chính 30 giây là mức đã dùng trong một đợt thử trước, trên một bộ kịch bản [tĩnh nghĩa là gì]
(Phụ lục~\ref{phuluc:A}). Mức này được giữ nguyên cho tập kiểm tra chính và không chỉnh lại sau khi thấy kết
quả."

**D26, dòng 211–212.** Gốc: "được chọn sau khi đã xem dữ liệu của các tập phát triển".
Vì sao khó: "tập phát triển" chưa được định nghĩa. Bảng 4.3 chỉ có "tập kiểm tra chính", "tập chỉnh trần buổi
sáng", "tập tắc đường cố định" và "chiều tuyết".
Viết lại: "…sau khi đã xem kết quả của [tên các tập cụ thể]".

### 4.2 Kết quả chính (dòng 217–403)

**D27, dòng 220–222.** Gốc: "Số lượt trễ quá một phút … giảm từ 203 xuống 76, nên số lượt không trễ quá một phút
tăng từ 2.231 lên 2.262."
Vì sao khó: chữ "nên" làm tôi khựng lại. Số lượt phục vụ cũng giảm, vậy vì sao số lượt đúng giờ lại tăng? Ý
"trễ giảm nhiều hơn phục vụ giảm" chỉ xuất hiện ở dòng 265.
Viết lại: "Luật C phục vụ ít hơn 96 lượt, nhưng số lượt trễ quá một phút giảm nhiều hơn, từ 203 xuống 76 (bớt
127). Vì vậy, số khách vừa được phục vụ vừa không trễ quá một phút tăng từ 2.231 lên 2.262 (thêm 31)."

**D28, dòng 225–226.** Gốc: "Luật hạn chót ở đây chỉ mượn phần hạn chót của Schulz và Pfeiffer".
Vì sao khó: tôi không biết "phần hạn chót" là phần nào.
Viết lại: "Luật hạn chót lấy một ý từ Schulz và Pfeiffer: không cho giờ trả muộn hơn lời hứa đầu quá một mức cố
định. Họ dùng mức 900 giây; ở đây dùng 30 và 60 giây để so được với trần của luật C."

**D29, dòng 234–235 và 240–241 (Bảng 4.5).** Gốc: "hai cột 'không trễ quá' tính trên 3.672 yêu cầu".
Vì sao khó: hai cột đó là số đếm (2.231, 2.262), không phải tỉ lệ. "Tính trên" khiến tôi đi tìm dấu \%.
Viết lại: "Hai cột 'không trễ quá' là số đếm. Muốn ra tỉ lệ thì chia cho 3.672 yêu cầu."

**D30, dòng 247–248.** Gốc: "M$^{+}$-60 & 2.347 & chưa đưa vào bảng"; "V-30 & 2.336 & chưa đưa vào bảng".
Vì sao khó: bảng trông như bản nháp chưa xong. Người đọc sẽ hỏi số đâu.
Viết lại: điền đủ bốn cột, hoặc bỏ hai dòng này và ghi hai số phục vụ trong lời (dòng 275–276 đã có hai số
đó).

**D31, dòng 258–259.** Gốc: "Mức giảm 96 lượt bằng 2,61 điểm phần trăm số yêu cầu, hay 3,94\% số lượt của điều
phối không trần."
Vì sao khó: "điểm phần trăm" và "\%" xuất hiện cạnh nhau, dễ lẫn.
Viết lại: "Bớt 96 lượt nghĩa là tỉ lệ yêu cầu được phục vụ giảm 2,61 điểm phần trăm (96 trên 3.672 yêu cầu);
so với số lượt của điều phối không trần thì ít hơn 3,94\% (96 trên 2.434)."

**D32, dòng 265–266.** Gốc: "$+31 = -96 - (-127)$".
Vì sao khó: công thức có dấu âm lồng nhau đặt giữa câu văn.
Viết lại: "phục vụ bớt 96 lượt nhưng trễ bớt 127 lượt, nên số lượt không trễ thêm 127 $-$ 96 = 31."

**D33, dòng 270–271.** Gốc: "Với 2.207 khách chung, luật C chờ lâu hơn 0,5 giây và ngồi xe ngắn hơn 10,5 giây,
nhưng đây là tập khách hình thành sau khi áp luật, không phải một phép so ngẫu nhiên."
Vì sao khó: (a) Chủ ngữ sai: luật không chờ, khách mới chờ. (b) Không rõ 0,5 giây là trung bình hay trung vị.
(c) "Tập khách hình thành sau khi áp luật" khó hiểu.
Viết lại: "Xét riêng 2.207 khách được cả hai cấu hình phục vụ, dưới luật C mỗi khách [trung bình] chờ đón lâu
hơn 0,5 giây và ngồi xe ít hơn 10,5 giây. Nhưng nhóm này hình thành từ việc mỗi cấu hình tự chọn phục vụ ai,
chứ không được chọn ngẫu nhiên từ trước, nên không thể coi hai con số này là tác động của luật C lên cùng một
nhóm khách."

**D34, dòng 274–278.** Gốc: "…nhưng không phải cùng mọi khách…"; "chỗ khác nhau là mỗi luật có giữ được nghĩa
vụ của chính nó hay không".
Vì sao khó: "không phải cùng mọi khách" nghe như dịch máy. "Nghĩa vụ" quá trừu tượng.
Viết lại: "…nhưng không hoàn toàn là cùng những khách…"; "chỗ khác nhau là mỗi luật có giữ được đúng điều
chính nó hứa với khách hay không".

**D35, dòng 308–311.** Gốc: "Điều này đúng theo cấu tạo… Luật hạn chót so giờ trả mới với lời hứa đầu, nên
riêng phần thay đổi khi giữ nguyên kế hoạch cũng có thể làm nó loại cả phương án giữ nguyên."
Vì sao khó: "đúng theo cấu tạo" và "phần thay đổi khi giữ nguyên kế hoạch" lần đầu xuất hiện mà không có ví dụ.
Câu này lại là chỗ quan trọng nhất của mục.
Viết lại, thêm ví dụ ghi rõ là ví dụ: "Con số 0 này có sẵn từ cách định nghĩa luật, không phải phát hiện của
thực nghiệm. Nếu xe cứ đi tiếp kế hoạch cũ, không ghép thêm ai, thì phần dời do điều phối bằng 0, nên dưới luật
C luôn còn ít nhất phương án đó để chọn. Luật hạn chót thì khác. Ví dụ, giả sử chỉ vì đường đông hơn lúc hứa,
một khách đã muộn hơn lời hứa đầu 40 giây dù xe vẫn đi đúng kế hoạch cũ. Với hạn chót 30 giây, chính phương án
đi tiếp cũng vi phạm, nên luật loại hết phương án của xe đó và bộ điều phối phải dùng luật phục hồi."

**D36, dòng 314–315.** Gốc: "ở khung 17 giờ chỉ 5 trong 11 kịch bản, với 1,0\% và 5,0\%."
Vì sao khó: phải đọc ngược lên câu trước mới biết hai con số ứng với chỉ số nào.
Viết lại: "ở khung 17 giờ, chỉ 5 trong 11 kịch bản có khách bị phá lời hứa; trung bình 1,0\% khách bị phá và
5,0\% lượt quyết định phải phục hồi."

**D37, dòng 318–320.** Gốc: "Bảng~\ref{bang:c4-nghiavu} không so hai chuẩn đúng giờ…"
Vì sao khó: ý rất quan trọng nhưng diễn đạt trừu tượng.
Viết lại: "Cần đọc Bảng~\ref{bang:c4-nghiavu} cho đúng. Luật C chỉ hứa rằng phần trễ do ghép thêm khách không
quá 30 giây. Luật hạn chót hứa rằng toàn bộ độ trễ so với lời hứa đầu không quá 30 giây, một lời hứa lớn hơn.
Bảng cho biết luật nào giữ được điều mình hứa, không cho biết luật nào làm khách đúng giờ hơn."

**D38, dòng 343.** Gốc: "Trễ lớn nhất & 11 phút & 3,87 phút".
Vì sao khó: hai số có độ chính xác khác nhau, một số tròn và một số có hai chữ số lẻ. Tôi không biết 11 phút có
được làm tròn hay không.
Viết lại: ghi cùng đơn vị và cùng độ chính xác, ví dụ "[… ] giây" cho cả hai, hoặc "khoảng 11 phút" và "khoảng
3,9 phút".

**D39, dòng 354–356.** Gốc: "…72 người không có lần dời giờ trả do điều phối nào được ghi. Phần trễ này là phần
mà lời hứa theo dự báo nhắm tới."
Viết lại: "72 trong 76 khách còn trễ quá một phút dưới luật C chưa từng bị điều phối dời giờ trả. Họ trễ vì
đường đông hơn lúc hứa hoặc xe đi chậm hơn dự kiến, và đó là loại trễ mà lời hứa theo dự báo
(mục~\ref{muc:c4-dubao}) tìm cách giảm." (Cách diễn đạt "đường đông hơn lúc hứa hay xe đi nhanh, chậm hơn dự
kiến" lấy từ đoạn mở chương 3.)

**D40, dòng 364–366 (chú thích Bảng 4.8).** Gốc: "Cột cuối là số kịch bản mà luật C có số lượt không trễ quá 60
giây không ít hơn."
Vì sao khó: "không ít hơn" so với cái gì? Tên cột "Kịch bản C không kém" cũng mơ hồ.
Viết lại: "Cột cuối đếm số kịch bản mà luật C có số lượt không trễ quá 60 giây bằng hoặc nhiều hơn điều phối
không trần."

### 4.3 Phần do điều phối (dòng 406–483)

**D41, dòng 434 (Bảng 4.9).** Gốc: "Theo sổ: phần tính cho điều phối trong số giây trễ của khách trễ quá 60 s
(\%)".
Vì sao khó: đây là nhãn dòng khó đọc nhất chương. "Sổ" và "phần tính cho" đều chưa được giải thích trong Chương 4.
Viết lại: "Tỉ lệ số giây trễ mà sổ theo từng khách quy cho điều phối, tính trên các khách trễ quá 60 s (\%)".

**D42, dòng 445–446.** Gốc: "4 người còn lại có giờ trả bị kéo sớm hơn, mỗi người đúng 1 mili giây."
Vì sao khó: tôi tự hỏi 1 mili giây có thật hay là sai số làm tròn của máy. Nếu là sai số thì con số 33 khách
"bị dời" (dòng 409, 428) có nên là 29 không?
Viết lại: "[Bốn lần dời này chỉ là sai số làm tròn / là thật vì …]; không tính chúng thì dưới trần 30 giây có
29 khách bị dời."

**D43, dòng 447–450.** Gốc: "…con số này là giao của hai tập khách, không phải tỉ lệ nhân quả. Theo sổ theo
từng khách…, phần tính cho điều phối bằng 73,4\%… gần như toàn bộ số giây trễ còn lại nằm ở hai phần kia của sổ."
Vì sao khó: "giao của hai tập", "phần tính cho" và "hai phần kia của sổ" đều là ngôn ngữ toán hoặc thuật ngữ
chưa giải thích.
Viết lại: "134 khách này vừa trễ quá một phút vừa từng bị dời; con số không nói rằng việc bị dời là nguyên nhân
khiến họ trễ. Cộng số giây trễ của 203 khách đó lại thì sổ theo từng khách (công thức~\eqref{eq:so}) quy 73,4\%
cho các lần dời do điều phối. Dưới trần 30 giây, tỉ lệ này chỉ còn 1,2\%. Nghĩa là dưới trần 30 giây, gần như
mọi giây trễ còn lại đến từ hai nguồn kia: nhịp tắc đường quen thuộc và phần biến động còn lại."

**D44, dòng 453.** Gốc: "Trần vẫn giữ ở những kịch bản không có dự báo và ở ngày có sự kiện."
Vì sao khó: "ngày có sự kiện" mơ hồ (sự kiện gì?). "Trần vẫn giữ" nghe như có lúc trần không giữ.
Viết lại: "Luật C vẫn không để khách nào bị dời quá trần ở 13 kịch bản cuối tuần (không có dự báo) và ở chiều
có tuyết 15/11/2018."

**D45, dòng 459–466 (ví dụ 79,0 + 68,3 giây).** Vì sao khó: đây là ví dụ hay nhất chương, nhưng một câu chứa ba
khái niệm và bốn con số.
Viết lại, chia bước: "Một ví dụ trên tập chỉnh trần buổi sáng cho thấy hai luật khác nhau ở đâu. Một khách
đang ngồi trên xe. Dù xe chỉ đi tiếp kế hoạch cũ, giờ trả của khách đã muộn hơn lời hứa đầu 79,0 giây; chưa có
lần dời nào do điều phối. Bộ điều phối xét ghép thêm một khách mới, việc này làm giờ trả của khách cũ muộn thêm
68,3 giây. Với mức 90 giây, luật hạn chót nhìn tổng 79,0 + 68,3, khoảng 147 giây, vượt 90 nên loại phương án.
Luật C chỉ nhìn phần do điều phối, 68,3 giây, dưới 90 nên cho qua. Trên tập này, hai luật cho kết quả khác nhau
ở đúng ba chỗ, đều ở mức 90 hoặc 120 giây và đều cùng kiểu: phần thay đổi khi đi tiếp kế hoạch cũ 61--79 giây,
phần do điều phối 61--68 giây. Mỗi chỗ, luật C nhận thêm đúng một khách. Đây là phép tính theo mô hình tại cùng
một thời điểm, không phải phép đo nhân quả."

**D46, dòng 469–474.** Gốc: "…có ít nhất một phương án mang bản ghi chặn do trần giờ trả của một khách đã
nhận…"; "chỉ có lý do cấu trúc"; "Bản ghi chặn cũng không phải là khách".
Vì sao khó: "bản ghi chặn" được dùng dày đặc từ đây tới hết mục 4.5 mà chưa có định nghĩa. "Lý do cấu trúc" cũng
vậy.
Viết lại, thêm một câu định nghĩa trước: "Mỗi khi luật C loại một phương án vì phương án đó làm một khách đã
nhận bị dời quá trần, bộ kiểm ghi lại một bản ghi chặn: phương án nào, khách nào, vượt bao nhiêu." Sau đó: "1.186
yêu cầu bị từ chối còn lại không có bản ghi chặn nào; chúng bị loại vì [các ràng buộc khác, ví dụ …]." Câu cuối:
"Số bản ghi chặn không bằng số người bị ảnh hưởng: 845 bản ghi của trần 30 giây trên tập chính thuộc về 643 yêu
cầu (một yêu cầu có thể bị chặn ở nhiều phương án), và 495 yêu cầu trong số đó cuối cùng vẫn được phục vụ bằng
phương án khác."

**D47, dòng 477–482.** Gốc: "mức vượt trần nhỏ nhất được ghi có trung vị 109,6 giây"; "Chỉ 2 trong 148 khách
chặn đã dùng phần trần trước đó"; "ngưỡng được ghi của 59 trong 148 yêu cầu qua được phép sàng lọc"; "bộ kiểm
dừng ở lỗi gặp trước và quỹ đạo sẽ đổi".
Vì sao khó: bốn thuật ngữ mới trong một đoạn ("khách chặn", "sàng lọc", "lỗi gặp trước", "quỹ đạo"). Ngoài ra
tôi không biết 109,6 giây là phần vượt quá 30 giây hay là cả lần dời (xem G7 ở Phần 2).
Viết lại: "Với mỗi yêu cầu trong 148 yêu cầu đó, lấy phương án bị chặn có mức vượt nhỏ nhất. Mức vượt [quá 30
giây] này có trung vị 109,6 giây, lớn nhất 524,8 giây. Khách đã nhận gây ra việc chặn hầu như chưa bị dời lần
nào: chỉ 2 trong 148 người đã dùng một phần trần trước đó, và ở cả 148 yêu cầu, riêng lần dời mới đã vượt 30
giây. Nếu trần là 120 giây, mức ghi được của 59 trong 148 yêu cầu sẽ lọt dưới trần. Nhưng không thể kết luận 59
yêu cầu đó sẽ được phục vụ, vì hai lẽ. Bộ kiểm dừng ngay ở vi phạm đầu tiên nó gặp, nên có thể còn vi phạm khác
chưa được ghi. Và khi đổi trần thì các quyết định trước đó cũng đổi, nên tình huống về sau không còn như cũ.
Kết quả chạy thật ở trần 120 giây có ở mục~\ref{muc:c4-chontran}."

### 4.4 Chọn mức trần (dòng 486–707)

**D48, dòng 489.** Gốc: "Nới trần không cho một đường đơn điệu."
Vì sao khó: "đơn điệu" là thuật ngữ toán.
Viết lại: "Nới trần không làm mọi chỉ số cùng tốt lên hay cùng xấu đi."

**D49, dòng 494–495.** Gốc: "Mức trần được đo trên ba tập, mỗi tập một câu hỏi…"
Vì sao khó: câu không nói đó là ba câu hỏi nào.
Viết lại: "Mức trần được đo trên ba tập, mỗi tập trả lời một câu hỏi riêng. Tập tắc đường cố định hỏi: khi tắc
đường không đổi, trần làm gì? Tập buổi sáng dò nhiều mức trần trên cùng 8 kịch bản. Tập kiểm tra chính hỏi: thêm
mức 120 giây thì sao? Kết quả các tập không được cộng gộp."

**D50, dòng 498–499.** Gốc: "Bảng~\ref{bang:c4-codinh} cho thang từ ghép tự do tới trần 30 giây khi thời gian đi
không đổi."
Viết lại: "Bảng~\ref{bang:c4-codinh} xếp các cấu hình từ lỏng nhất (ghép tự do) tới chặt nhất (trần 30 giây),
khi hệ số tắc đường giữ cố định suốt lần chạy."

**D51, dòng 527–528.** Gốc: "Điểm gãy nằm giữa 60 và 120 giây… Tập này chạy bằng bộ chạy cũ không có luật phục
hồi, nên các con số không chuyển sang tập kiểm tra chính."
Vì sao khó: "bộ chạy cũ" vẫn chưa được giải thích (xem D13).
Viết lại: chỉ cần giải thích "bộ chạy cũ" một lần ở Bảng 4.3 rồi dùng lại.

**D52, dòng 560–561.** Gốc: "nên điều phối không trần là một điểm đo, không phải cận trên."
Vì sao khó: "cận trên" là thuật ngữ toán.
Viết lại: "nên không thể coi điều phối không trần là mức phục vụ cao nhất có thể đạt; nó chỉ là một cấu hình
được đo như các cấu hình khác."

**D53, dòng 566–568.** Gốc: "58,6; 35,5; 13,0; 6,6; 6,8; 2,8 và 1,7\% ở các mức 30, 60, 90, 120, 150, 180 và
240--300 giây".
Vì sao khó: bảy con số ghép với bảy mức trong một câu, tôi phải đếm ngón tay để ghép.
Viết lại: chuyển thành một dòng trong Bảng~\ref{bang:c4-sang} hoặc một bảng nhỏ hai dòng (mức trần; \% quyết
định phải phục hồi).

**D54, dòng 609–613.** Gốc: "…và ở ngưỡng này cao hơn cả hai điểm đầu mút đã đo."
Vì sao khó: "điểm đầu mút" là thuật ngữ toán. Cả đoạn có 10 con số.
Viết lại: "…ở ngưỡng hai phút, trần 120 giây có nhiều lượt không trễ hơn cả trần 30 giây lẫn điều phối không
trần." Tách phần "khi có dự báo" thành câu riêng.

**D55, dòng 616.** Gốc: "9 khách dùng từ 90\% trần trở lên".
Viết lại: "9 khách bị dời gần chạm trần, từ 108 giây trở lên (90\% của 120 giây)".

**D56, dòng 621.** Gốc: "chung 2.266 lượt, riêng 121 và 72 lượt".
Viết lại: "2.266 khách được cả hai mức trần phục vụ; 121 khách chỉ được trần 120 giây phục vụ, 72 khách chỉ
được trần 30 giây phục vụ."

**D57, Hình 4.1 (dòng 629–694).** Cách vẽ ba khung với ba thang riêng đã được chú thích rõ. Nhưng chỉ khung (a)
có nhãn trục dọc, và hình chỉ vẽ ngưỡng 60 giây. Đọc riêng hình, tôi sẽ nghĩ trần 120 giây chỉ có hại, trong khi
lời văn nói ở ngưỡng 120 giây nó tốt nhất trên cả ba tập.
Đề xuất: ghi nhãn trục dọc cho cả ba khung, hoặc ghi một lần chung. Thêm một câu vào chú thích: "Ở ngưỡng 120
giây, trần 120 giây không kém trần 30 giây ở cả ba tập (xem lời văn)."

**D58, dòng 704–706.** Gốc: "…không phải kết quả của một phép dò tìm."
Vì sao khó: "phép dò tìm" mơ hồ.
Viết lại: "…nên không thể nói 120 giây là mức trần tốt nhất. Đó chỉ là một điểm đo thêm, cho thấy một cách
đánh đổi khác giữa số lượt phục vụ và số lượt trễ."

### 4.5 Phần cộng dồn (dòng 710–784)

**D59, dòng 713–715.** Gốc: "…cả 1.256 bản ghi chặn do trần đều có một lần dời đơn lẻ đã vượt trần…; 3 trong 524
bản ghi chỉ vượt trần khi cộng thêm phần trần đã dùng trước đó."
Vì sao khó: tôi đọc hết đoạn mà không biết mục này trả lời câu hỏi gì, và kết luận là tốt hay xấu.
Viết lại, đặt câu hỏi và câu trả lời lên đầu: "Luật C cộng mọi lần dời của một khách qua cả chuyến rồi mới so
với trần. Vậy có khi nào chính phép cộng này là lý do duy nhất để chặn một phương án không? Trong các lần chạy
đã kiểm thì gần như không. Trong 98 lần chạy cũ dùng hệ số tắc đường đo được, cả 1.256 bản ghi chặn đều có một
lần dời đơn lẻ đã tự vượt trần. Trên 34 lần chạy trần 120 giây của tập kiểm tra chính, chỉ 3 trong 524 bản ghi
là vượt trần do cộng dồn."

**D60, dòng 718–722.** Gốc: "Một bản ghi chặn là \emph{chỉ do cộng dồn} khi lần dời mới không vượt $B$ nhưng
phần đã dùng $L_r$ cộng lần dời mới thì vượt…"
Vì sao khó: định nghĩa bằng ký hiệu, còn ví dụ thì ở tận dòng 760.
Viết lại: đưa ví dụ lên ngay sau định nghĩa: "Ví dụ, với trần 120 giây, một khách đã dùng 25,844 giây của trần,
và phương án mới sẽ dời giờ trả của khách thêm 99,027 giây. Mỗi phần đều dưới 120 giây, nhưng tổng 124,871 giây
vượt trần, nên đây là một bản ghi chỉ do cộng dồn."

**D61, dòng 753–757.** Gốc: "98 lần chạy cũ với 64.371 lượt quyết định được xác nhận"; "16 lần chạy đưa dự báo
vào bộ điều phối chưa được kiểm".
Vì sao khó: "được xác nhận" là xác nhận cái gì? "Đưa dự báo vào bộ điều phối" là một loại lần chạy chưa từng
được nhắc tới. Trước đó (dòng 158–161) tôi được bảo rằng dự báo chỉ được phát lại.
Viết lại: "…64.371 lượt quyết định [đã được kiểm lại rằng …]"; "16 lần chạy trong đó bộ điều phối dùng dự báo
khi quyết định (khác với phép phát lại ở mục~\ref{muc:c4-chiso}) chưa được kiểm."

**D62, dòng 768–771.** Gốc: "Ngoài hệ số đo còn hai chỗ có dấu vết… nơi bộ kiểm ghi đủ mọi bản ghi thay vì dừng
ở lỗi gặp trước… Ở một kiểu tắc đường tự tạo…"
Vì sao khó: "hai chỗ có dấu vết" nghe như dịch máy. "Kiểu tắc đường tự tạo" là tập nào, vì nó không có trong
Bảng 4.3?
Viết lại: "Ngoài các lần chạy dùng hệ số tắc đường đo được, còn hai nơi thấy bản ghi chỉ do cộng dồn. Trên tập
tắc đường cố định, nơi bộ kiểm ghi mọi vi phạm thay vì dừng ở vi phạm đầu tiên, có 2 bản ghi như vậy ở trần 60
giây và 4 ở trần 120 giây; mọi yêu cầu mới liên quan vẫn được phục vụ. Trên [tên tập dùng một kiểu tắc đường tự
tạo, cần thêm vào Bảng 4.3] có 4 bản ghi ở trần 120 giây, với 1 yêu cầu liên quan bị từ chối."

**D63, dòng 774–780.** Gốc: "Theo định nghĩa, vế cộng dồn vẫn là một nghĩa vụ khác… Chấm lại các quỹ đạo không
trần đã ghi, hai cách tính chỉ khác nhau ở 4 trong 2.434 khách… Phép sàng lọc này không cho biết quỹ đạo của một
luật khác sẽ ra sao."
Vì sao khó: "vế", "nghĩa vụ", "chấm lại", "quỹ đạo", "sàng lọc" đều khó hiểu.
Viết lại: "Về định nghĩa, luật C vẫn khác luật 'mỗi lần dời không quá 30 giây'. Luật sau cho phép một khách bị
dời ba lần, tổng 90 giây; luật C với trần 30 giây thì không. Nhưng trong số liệu, khác biệt này hiếm khi xảy ra.
Khi không trần, chỉ 12 trong 2.434 khách bị dời từ hai lần (Bảng~\ref{bang:c4-doidieuphoi}). Lấy các lần chạy
không trần đã ghi và tính thử cả hai luật cho từng khách, thì hai luật cho kết luận khác nhau ở 4 trong 2.434
khách với trần 120 giây, và ở 0 khách với trần 30, 60 hoặc 300 giây. Phép tính thử này không cho biết nếu chạy
thật với luật kia thì kết quả ra sao, vì khi đó các quyết định sẽ khác. Luật 'mỗi lần dời một trần' chưa được
cài đặt và chưa chạy, nên chưa biết bỏ phần cộng dồn có làm đổi kết quả hay không."

**D64, dòng 782.** Gốc: "khi giữ nguyên bộ chọn ưu tiên ổn định".
Vì sao khó: "ưu tiên ổn định" chưa được giải thích.
Viết lại: "khi giữ nguyên bộ chọn [xếp tiêu chí … lên đầu]".

**Chung.** Bảng dùng "s", lời văn dùng "giây". Nên chọn một cách, hoặc ghi một lần "s là giây".

**Tổng số chỗ khó hiểu:** 64 chỗ có số (D1–D64), cộng 2 ghi chú chung (mục 4.1.3 và cuối mục 4.5).

### Tóm tắt 5 câu: điều tôi hiểu được

1. Trên 34 kịch bản mô phỏng ở Manhattan (3.672 yêu cầu, 8 xe), luật C với trần 30 giây phục vụ 2.338 lượt,
   ít hơn điều phối không trần 96 lượt, và số khách đi chung giảm từ 555 xuống 313.
2. Đổi lại, số lượt tới muộn hơn lời hứa đầu quá một phút giảm từ 203 xuống 76. Không lượt nào trễ quá 5 phút
   (so với 18), và khách trễ nhất muộn 3,87 phút thay vì khoảng 11 phút. Nhưng nếu đếm số khách vừa được phục
   vụ vừa không trễ, luật C chỉ hơn 31 lượt ở ngưỡng một phút và kém 5 lượt ở ngưỡng hai phút.
3. Luật C không bao giờ để khách nào bị điều phối dời quá trần và không bao giờ phải phục hồi; điều này có sẵn
   từ cách định nghĩa luật. Luật hạn chót 30 giây phục vụ bằng số lượt nhưng phải phục hồi ở 38,35\% lượt
   quyết định và không giữ được lời hứa với 12,4\% khách. Hai luật hứa hai điều khác nhau, nên đây không phải
   phép so ai đúng giờ hơn.
4. Không có mức trần tốt nhất. Trần 120 giây phục vụ nhiều hơn trần 30 giây 49 lượt và có nhiều lượt không trễ
   quá hai phút nhất (2.366), nhưng thêm 56 lượt trễ quá một phút.
5. Phần "cộng dồn" là điều phân biệt luật C với một trần cho từng lần dời. Phần này chỉ là lý do chặn duy nhất ở
   3 trong 1.943 bản ghi đã kiểm, và luật không cộng dồn chưa được chạy để so.

**Những chỗ tôi không tóm được, tức chỗ chương còn chưa rõ:**
- Vì sao cần luật C, nếu một cách đơn giản hơn là đệm thêm vào lời hứa cũng cho số lượt đúng giờ tương tự?
  Phần A chỉ hẹn sang mục~\ref{muc:c4-dem} (dòng 613) mà không cho một con số nào về cách đệm.
- Dự báo có tác dụng lớn đến đâu? Bảng 4.12 (dòng 596) cho thấy khi có dự báo, số lượt trễ quá 60 giây của
  luật C giảm từ 76 xuống 10, nhưng lời văn của phần A không bình một câu nào về con số này.
- Vì sao ngay cả điều phối không trần cũng từ chối 1.238 trong 3.672 yêu cầu (suy ra: 3.672 $-$ 2.434)? Phần
  A không giải thích, nên người đọc dễ hiểu nhầm rằng mọi yêu cầu bị từ chối là do trần.
- Bốn khách "bị dời 1 mili giây" (dòng 446) có thật sự bị dời không?

---

## PHẦN 2. Giảng viên hội đồng

### G1. Các thí nghiệm có đủ rõ không?

| Hạng mục | Phần A đã có | Còn thiếu hoặc chưa khớp |
|---|---|---|
| Tập dữ liệu | Bốn tập ở Bảng 4.3 (dòng 108–135); ngày, khung giờ, số kịch bản, số yêu cầu; nói thẳng rằng tắc đường là hệ số chung cho cả thành phố (63–64); nói các kịch bản không độc lập (65–66). | (1) Cách lấy 108 yêu cầu từ mẫu 10\%; "mẫu" là gì, mỗi ngày mấy mẫu (58–60). (2) Vì sao có 49 kịch bản, luật chia 34/15 (103–105). (3) Phần A dùng ít nhất ba nguồn số liệu ngoài bốn tập này, dù dòng 144–145 viết "chương này chỉ dùng các tập ở Bảng 4.3": "tập kịch bản tĩnh" (205), "16 lần chạy đưa dự báo vào bộ điều phối" (755), "một kiểu tắc đường tự tạo" (770). (4) Chiều tuyết ghi số lượt phục vụ (601) thay vì số yêu cầu, và bộ chạy "Chưa kiểm lại", nhưng số liệu chiều tuyết vẫn được dùng ở dòng 453–456 và Bảng 4.13 (dòng 740) mà lời văn không kèm lưu ý nào. |
| Số lần chạy | Mỗi cặp kịch bản–cấu hình chạy một lần (64–65); 170 + 34 lần (122); 16 lần mỗi cấu hình (128); 8 lần (131). | (1) "88 và 104" lần chạy của tập buổi sáng (125) không khớp với những gì được báo. Lời văn kể 8 mức C (531–532) và 8 mức M$^{+}$ (566–567) cộng U, tức (8 + 8 + 1) × 8 = 136 lần (suy ra). Bảng 4.13 ghi 64 lần cho C (736). Vậy 192 $-$ 136 = 56 lần còn lại là gì? (2) Không có kiểm tra độ nhạy theo giá trị khởi tạo ngẫu nhiên (cố định 7, dòng 91). Câu "kết quả tất định" (65) cần nói đã chạy lại những lần nào và ra đúng số cũ hay chưa. (3) Các tập dùng ba phiên bản bộ chạy khác nhau; bản nháp có nói các tập không được cộng gộp (494, 528), như vậy là tốt. |
| Chỉ số | Bảng 4.4 (164–200) có cột "Mẫu số, cách gộp" và "Vì sao đo", rất tốt. | (1) $c$ và $z$ chưa được định nghĩa. (2) Không nói lời hứa đầu $p_0$ được tính theo thời gian đi nào, và có khác nhau giữa các cấu hình hay không. Nếu $p_0$ phụ thuộc kế hoạch lúc khách xác nhận thì cấu hình nào hứa "xa" hơn sẽ ít trễ hơn. Cần một dòng so độ dài lời hứa đầu (ví dụ $p_0$ trừ giờ gọi) giữa U và C-30. (3) Chỉ số "Tới sớm quá 60 giây" (181) được định nghĩa nhưng phần A không dùng. (4) Thời gian dừng đón, trả bằng 0 giây (87) là giả định lạc quan; cần nhắc ở phần hạn chế. |
| Mẫu số | Phần lớn đã ghi rõ: 3.672 yêu cầu, khách được phục vụ, trung bình theo kịch bản hay gộp. | (1) Chú thích Bảng 4.5 và 4.12 viết "tính trên 3.672 yêu cầu" cho các cột là số đếm (234, 577). (2) "Lời hứa dài thêm, trung bình gộp theo khách" (599): mẫu số có gồm khách của 13 kịch bản cuối tuần, nơi $D_0 = p_0$ nên phần dài thêm bằng 0, không? Nếu có thì 7,18–7,37 giây là số bị pha loãng. (3) Bảng 4.6 đặt số trung bình theo kịch bản (41,3\%) cạnh số gộp (38,35\%) cho cùng một đại lượng; lời văn có giải thích, nhưng nên làm tròn cùng một kiểu (38,35\% so với 12,4\%). |
| Thống kê | Nói rõ kết quả là thăm dò (211–213); các phép đếm theo kịch bản là mô tả, không phải kiểm định (401–402). | Tốt. Nên nói thêm ngay ở đoạn mở mục 4.2 rằng chênh lệch +31 bằng 0,84\% số yêu cầu (suy ra: 31/3.672) và đổi dấu ở ngưỡng 120 giây. |

**Kiểm số học.** Tôi đã tính lại và thấy khớp: các hàng Bảng 4.5 (phục vụ $-$ trễ = không trễ); mọi hàng và
dòng "Cộng" của Bảng 4.8 ($-96$, $-127$, $+31$, 34, 29), kể cả số kịch bản theo khung (9, 14, 11) và theo nhóm ngày
(21 ngày thường, 13 cuối tuần); các tỉ lệ 2,61; 3,94; 22,80; 13,39; 38,35; 12,36; 7,15; 1,41; 4,32; số trên 100
yêu cầu ở Bảng 4.7; các chênh lệch +49/+56/$-7$/+39 và $-6$/+41 (609–612); +6/+4/+2 (561); +6, +2, $-7$ (702); các
tổng 140/1.943 và 132/1.780 (743, 753); 148 + 1.186 = 1.334 và 495 + 148 = 643 (469–474); và tọa độ cả ba khung
Hình 4.1. Hai chỗ chưa khớp nằm ở G7 và mục 4 của G6.

### G2. Mỗi mục kết quả có trả lời thẳng câu hỏi trước khi vào bảng không?

Báo cáo mẫu (trang 30–33) mở mỗi mục bằng mục đích và cách đọc bảng ("Để xem kết quả có phụ thuộc vào một nguồn
dữ liệu riêng hay không, Bảng 4.3 tách riêng…"; "Khi đọc Bảng 4.1, cần phân biệt…"), giải thích các cột trước
bảng, rồi nêu kết quả bằng câu ngắn kèm một câu "không nên hiểu rằng…". Bản nháp mở bằng câu trả lời có số, tức
còn thẳng hơn mẫu, nên giữ cách đó. Tuy vậy, không phải mục nào cũng làm được:

| Mục | Câu mở | Đánh giá |
|---|---|---|
| 4.2 (220–222) | Nêu ngay: phục vụ $-96$, trễ 203 → 76, không trễ 2.231 → 2.262. | Có câu trả lời, nhưng đặt trọng tâm sai: câu đầu tiên quảng bá "+31 lượt đúng giờ", là con số yếu nhất (đổi dấu ở 120 giây, và đệm lời hứa có thể đạt được, xem G4). |
| 4.3 (409–411) | 33 khách bị dời, nhiều nhất 29,2 giây, so với 174 khách và 590,1 giây. | Tốt. Tiêu đề hỏi "chặn gì và mất gì" nhưng câu mở chỉ nói phần "chặn gì"; phần "mất gì" đến tận dòng 469. |
| 4.4 (489–491) | "Nới trần không cho một đường đơn điệu", kèm số của trần 120 giây. | Chưa trả lời câu hỏi của mục ("chọn mức nào?"). Kết luận thật nằm ở dòng 704: "Không mức trần nào tốt hơn ở mọi tiêu chí". |
| 4.5 (713–715) | Hai con số kiểm toán. | Có số nhưng không có kết luận bằng lời. Người đọc không biết đây là tin tốt hay xấu cho luật C (xem D59). |

Các đoạn "Cách đọc bảng" (8 lần) theo đúng tinh thần báo cáo mẫu, nên giữ. Bảng 4.8 thì cần giải thích cột cuối
trước bảng (D40).

### G3. Các câu nói quá

Tôi đã rà các loại câu được yêu cầu kiểm.

- **"Tối ưu":** không có. Tốt.
- **Nhân quả:** bản nháp rất cẩn thận (271, 447–448, 466, 482, 764–765, 778–779). Còn ba chỗ:
  - Dòng 469: "Cái giá của trần là các yêu cầu không được nhận. Dưới trần 30 giây, 1.334 yêu cầu bị từ chối."
    Đọc liền hai câu, người ta hiểu 1.334 là cái giá của trần. Thực ra điều phối không trần cũng từ chối 1.238
    yêu cầu (suy ra: 3.672 $-$ 2.434). Thay bằng: "Dưới trần 30 giây, 1.334 yêu cầu bị từ chối, nhiều hơn điều
    phối không trần 96. Chỉ 148 trong 1.334 yêu cầu đó có bản ghi chặn do trần; …"
  - Dòng 453: "Trần vẫn giữ ở những kịch bản không có dự báo và ở ngày có sự kiện" được trình bày như bằng
    chứng về độ bền. Nhưng trần luôn giữ theo cấu tạo (dòng 309), nên điều câu này thật sự cho thấy là cài đặt
    đúng. Thay bằng: "Các bộ đếm xác nhận cài đặt giữ đúng trần cả ở 13 kịch bản cuối tuần (không có dự báo) và
    ở 8 kịch bản chiều tuyết 15/11/2018 [bộ chạy của tập này chưa được kiểm lại]: …"
  - Dòng 355–356: "Phần trễ này là phần mà lời hứa theo dự báo nhắm tới." Dự báo chỉ nhắm tới phần đoán được
    của nó. Thay bằng: "Lời hứa theo dự báo (mục~\ref{muc:c4-dubao}) nhắm tới phần đoán được của loại trễ này."
- **"Mọi":**
  - Dòng 323: "số lượt trễ giảm ở mọi ngưỡng" → "ở cả bốn ngưỡng đã đo (1, 2, 5 và 10 phút)".
  - Dòng 568: "Ở mọi mức, hai luật phục vụ chênh nhau không quá 2 lượt" → "Ở cả tám mức đã chạy (30–300 giây), …".
  - Các chỗ "mọi" khác (56, 88, 720, 769) có phạm vi rõ, chấp nhận được.
- **Lợi ích kinh doanh:** không có câu nói quá. Dòng 261–262 ("Khóa luận không có bằng chứng về giá trị của các
  chuyến đi chung…") là mẫu tốt. Nên dùng cùng giọng đó khi nói về giá trị của trần (xem G4).
- **Coi U là giới hạn trên:** không có. Dòng 560–561 chủ động bác điều đó, tốt. Dòng 611 dùng "hai điểm đầu
  mút"; nên đổi thành "cả trần 30 giây lẫn điều phối không trần" để tránh gợi ý U là mút trên.
- **Coi hai tập khách là cùng người:** đã xử lý tốt ở 267–271, 274–275, 621–623. Còn hai chỗ nên nói thêm:
  - Dòng 471 ("điều phối không trần phục vụ 116 trong 148 yêu cầu này") dễ bị đọc thành "luật C làm mất 116
    khách". Chỉ cần dẫn chiếu sang lời cảnh báo ở 480–482, đặt ngay sau câu đó.
  - Dòng 612 so "lời hứa dài thêm" 7,27 với 7,37 giây trên hai tập khách khác nhau. Nên ghi "(trên hai tập khách
    được phục vụ khác nhau)".
- **Phép so không cân (quan trọng):** Bảng 4.6 đặt hàng C-30 với "0 / 0 / 0" cạnh M$^{+}$-30 với "41,3 / 14,5 /
  28". Ba số 0 của C-30 có sẵn theo cấu tạo. Lời văn có nói (309, 318–320), nhưng người đọc lướt bảng sẽ thấy
  "luật C thắng tuyệt đối". Cần hai sửa:
  - Đánh dấu hàng C-30 là "0 (theo định nghĩa)".
  - Thêm số so được với nhau: tỉ lệ khách dưới C-30 trễ quá 30 giây so với lời hứa đầu, tức cùng thước đo
    "phá lời hứa" của M$^{+}$-30. Phần A không có số này, cần lấy từ dữ liệu. Nếu số này gần 14,5\% thì phải nói
    thẳng rằng hai luật để khách trễ như nhau, chỉ khác ở chỗ ai hứa điều mình giữ được.

### G4. Câu hỏi "cần luật C để làm gì khi đệm 30 giây cũng đạt cùng số lượt đúng giờ?"

**Kết luận: phần A chưa trả lời câu hỏi này, và cách mở mục 4.2 còn làm câu hỏi gay gắt hơn.**

- Phần A nêu cách đệm như một đối chứng (dòng 15, 36, 183) nhưng không cho một con số nào về nó. Chỗ duy nhất
  chạm tới là câu hẹn ở dòng 613 ("Mục~\ref{muc:c4-dem} đặt điểm này cạnh cách đệm lời hứa").
- Ghi chú ẩn ở dòng 156 (`C10 (đệm hòa ở 60 s, hơn ở 120 s)`) cho thấy tác giả biết rằng đệm hòa ở ngưỡng
  60 giây và hơn ở ngưỡng 120 giây. Ghi chú không nói hơn ai; theo câu hỏi được giao thì tôi hiểu là so với luật
  C. Vậy mà câu đầu tiên của mục kết quả chính (220–222) và đoạn
  265–266 lại lấy "+31 lượt không trễ quá một phút" làm lợi ích chính của luật C. Hội đồng đọc phần B sẽ thấy
  ngay lợi ích ấy có thể có mà không cần luật C.
- Câu trả lời trung thực đã có sẵn chất liệu trong phần A, chỉ chưa được nối với câu hỏi đệm:
  - (a) Giới hạn cho từng khách về phần dời do ghép thêm: 33 khách bị dời, nhiều nhất 29,2 giây, so với 174
    khách và 590,1 giây (Bảng 4.9).
  - (b) Đuôi trễ: 0 so với 18 lượt trễ quá 5 phút; khách trễ nhất muộn 3,87 phút so với khoảng 11 phút (Bảng
    4.7).
  - (c) Cái giá: $-96$ lượt phục vụ và $-242$ khách đi chung (suy ra: 555 $-$ 313).
- Một điều phải cẩn thận: "0 quyết định phải phục hồi" là ưu thế so với luật hạn chót, **không phải** so với
  cách đệm. Đệm không có luật lời hứa, nên cũng không bao giờ phải phục hồi. Không được dùng điểm này để trả lời
  câu hỏi đệm.
- Đề xuất thêm một đoạn ở cuối mục 4.2, ngay sau dòng 403. Các chỗ trong ngoặc vuông phải điền từ mục c4-dem và
  kiểm điều kiện "đệm giữ nguyên quyết định điều phối của U":

> "Nếu chỉ cần thêm lượt không trễ quá một phút thì có một cách rẻ hơn luật C: giữ điều phối không trần và đệm
> thêm 30 giây vào lời hứa. Mục~\ref{muc:c4-dem} cho thấy cách này đạt [ … ] lượt không trễ quá 60 giây, [bằng]
> luật C, mà không bớt lượt phục vụ nào. Vì vậy khóa luận không biện minh luật C bằng số lượt đúng giờ. Điều đệm
> không làm được là giới hạn phần dời do điều phối của từng khách. Đệm không đổi quyết định điều phối, nên vẫn có
> 174 khách bị dời giờ trả và một khách bị dời 590,1 giây; dưới luật C, 33 khách bị dời, nhiều nhất 29,2 giây.
> Đệm cũng chỉ lùi mọi lời hứa đi 30 giây, nên khách trễ nhất khi không trần (khoảng 11 phút) vẫn trễ khoảng
> 10,5 phút; dưới luật C, khách trễ nhất muộn 3,87 phút. Đổi lại, luật C mất 96 lượt phục vụ và 242 khách đi
> chung. Khóa luận không đo được khách hay hãng xe coi trọng giới hạn cho từng khách tới mức nào, nên chọn luật C
> hay cách đệm là một lựa chọn chính sách, không phải kết luận của thực nghiệm."

Đồng thời sửa câu mở mục 4.2 (dòng 220–222) để thứ tự là: điều luật C giữ được → cái giá → số lượt đúng giờ
như một chỉ số phụ, nhạy với ngưỡng. Xem thay đổi số 1 ở G6.

### G5. Những điểm mạnh nên giữ

- Mỗi bảng chính có đoạn "Cách đọc bảng" bằng một ví dụ cụ thể.
- Nói thẳng các giới hạn: kết quả thăm dò (211–213); kịch bản không độc lập (65–66, 401–402); số liệu từ ghi
  chép dừng ở lỗi đầu tiên nên "không chứng minh" (482, 764–765); luật mỗi lần một trần chưa chạy (778–779).
- Tách rõ chênh lệch giữa hai tổng với khách cụ thể (268–269, 622–623).
- Ví dụ 79,0 + 68,3 giây (459–466) cho thấy đúng chỗ luật C khác luật hạn chót. Đó là ví dụ đắt giá nhất chương.

### G6. Danh sách thay đổi, xếp theo mức quan trọng

1. **[Bắt buộc] Trả lời câu hỏi đệm ngay trong phần A, và đổi trọng tâm câu mở mục 4.2** (220–222, 265–271,
   613). Thêm đoạn đề xuất ở G4. Thay câu mở bằng: "Trên 3.672 yêu cầu của tập kiểm tra chính, luật C với trần 30
   giây giữ phần dời giờ trả do điều phối của mọi khách dưới 30 giây (nhiều nhất 29,2 giây, so với 590,1 giây khi
   không trần), và không lượt nào trễ quá 5 phút so với lời hứa đầu (so với 18). Cái giá là 96 lượt phục vụ (2.338
   so với 2.434) và 242 khách đi chung. Số lượt không trễ quá một phút tăng 31 (từ 2.231 lên 2.262), nhưng ở
   ngưỡng hai phút thì giảm 5 (từ 2.332 xuống 2.327)."
2. **[Bắt buộc] Làm cho Bảng 4.6 so cân** (283–320). Ghi "0 (theo định nghĩa)" ở hàng C-30, và thêm một cột hoặc
   một câu nêu tỉ lệ khách dưới C-30 trễ quá 30 giây so với lời hứa đầu, tức cùng thước đo "phá lời hứa" của
   M$^{+}$-30. Thêm câu: "Về độ đúng giờ, luật C không hơn luật hạn chót (76 so với 74 lượt trễ quá một phút); điều
   luật C hơn là nó chỉ hứa phần mà bộ điều phối kiểm soát được, nên luôn giữ được lời hứa đó."
3. **[Bắt buộc] Điền hoặc bỏ hai dòng "chưa đưa vào bảng"** (247–248). Thêm một câu giải thích vì sao V-30 tệ
   nhất ở Bảng 4.6: 53,8\% quyết định phải phục hồi, 21,6\% khách bị phá lời hứa, cả 34 kịch bản. Hiện phần A
   không bình một chữ nào về dòng này.
4. **[Bắt buộc] Đối chiếu phạm vi dữ liệu và số lần chạy.** (a) Giải thích "88 và 104" (125) sao cho khớp với 8
   mức C, 8 mức M$^{+}$ và U trên 8 kịch bản, và với 64 lần chạy C ở Bảng 4.13 (736). (b) Thêm vào Bảng 4.3, hoặc
   bỏ khỏi phần A, ba nguồn ngoài bảng: "tập kịch bản tĩnh" (205), "16 lần chạy đưa dự báo vào bộ điều phối" (755),
   "kiểu tắc đường tự tạo" (770). Nếu không, dòng 144–145 ("chỉ dùng các tập ở Bảng 4.3") sai. (c) Kèm lưu ý "bộ
   chạy chưa kiểm lại" mỗi khi dùng số chiều tuyết (453–456, 740).
5. **[Bắt buộc] Bổ sung thiết lập để người khác chạy lại được:** cách lấy 108 yêu cầu và "mẫu" là gì (58–60); luật
   chia 34/15 (103–105); vì sao các khung có chung 3–20 yêu cầu (65–66); $p_0$ được tính theo thời gian đi nào và
   có khác giữa các cấu hình không, kèm một dòng so độ dài lời hứa đầu giữa U và C-30; bằng chứng cho câu "tất
   định" (đã chạy lại những lần nào); giả định dừng 0 giây (87) đưa vào phần hạn chế.
6. **[Nên] Thêm một khung "Ký hiệu và thuật ngữ của chương" ở mục 4.1.3.** Khung gồm: các ký hiệu U, C-$B$,
   M$^{+}$-$B$, V-30, FREE (D14); $c$, $z$, $L_r$, $B$; "phần thay đổi khi giữ nguyên kế hoạch"; "sổ theo từng
   khách"; "bản ghi chặn"; "dừng ở vi phạm đầu tiên"; "luật phục hồi không tệ hơn"; "bộ chạy cũ, bản lưu trữ";
   "bộ chọn ưu tiên ổn định". Thống nhất "quyết định phải phục hồi" với "quyết định bị ép" của Bảng thuật ngữ
   chương 3 (dòng 63–64 của 07-chuong3-v3.tex).
7. **[Nên] Đưa kết luận của mục 4.4 lên đầu mục** (489, 704). Câu mở thay thế: "Không có mức trần tốt nhất. Trên
   tập kiểm tra chính, trần 30 giây cho ít lượt trễ quá một phút nhất (76), còn trần 120 giây cho nhiều lượt
   không trễ quá hai phút nhất (2.366, so với 2.327 và 2.332). Chọn mức nào tùy hãng xe coi trọng ngưỡng nào;
   thực nghiệm không trả lời được điều đó." Chuyển chuỗi bảy tỉ lệ (566–568) vào bảng. Bảng 4.11 (536–553) chỉ có
   4 trong 8 mức dù số phục vụ của cả 8 mức đã có (531–532): điền đủ, hoặc nói vì sao thiếu số trễ.
8. **[Nên] Sửa hai chỗ số dễ gây hiểu sai ở mục 4.3.**
   - (a) Dòng 469: dùng câu thay thế ở G3.
   - (b) Dòng 477–479: nói rõ 109,6 giây là phần vượt quá 30 giây hay cả lần dời. Lập luận: nếu đó là cả lần dời,
     thì vì 146 trong 148 khách chặn chưa dùng phần trần nào, trung vị 109,6 < 120 kéo theo ít nhất 74 trong 148
     yêu cầu lọt dưới trần 120 giây, chứ không phải 59. Vậy nhiều khả năng đây là phần vượt, và câu văn phải nói
     như thế.
   - (c) Dòng 445–446: bốn lần dời "đúng 1 mili giây". Nói rõ đó là sai số làm tròn hay dời thật. Nếu là sai số
     thì báo 29 khách và tính lại trung vị 8,3 giây không kể bốn lần này.
9. **[Nên] Viết kết luận bằng lời cho mục 4.5** (713–715). Dùng câu ở D59, cộng thêm: "Nói cách khác, trong các lần
   chạy đã kiểm, luật C chặn gần như cùng những phương án mà một trần cho từng lần dời sẽ chặn. Phần cộng dồn, điều
   phân biệt luật C về định nghĩa, chưa được thấy là có tác dụng đáng kể, và luật không cộng dồn chưa được chạy để
   so." Câu này không phủ nhận luật C. Nó báo đúng điều số liệu cho thấy, và chặn trước câu hỏi "phần cộng dồn có
   cần không?".
10. **[Nên] Chỉnh các câu "mọi" và khung giờ.** Đổi "mọi ngưỡng" (323) thành "cả bốn ngưỡng đã đo". Thêm phạm vi cho
    "mọi mức" (568). Ở dòng 398–402, nói thẳng điều bảng cho thấy: ở khung 7 giờ, luật C gần như không đổi số lượt
    trễ (hơn ở 3, bằng ở 6 trong 9 kịch bản). Suy ra từ dòng 624: 61 trong 76 lượt trễ còn lại của C-30 nằm ở khung
    7 giờ (76 $-$ 15 $-$ 0). Đây chính là chỗ cần dự báo, và nên nói ra để nối sang mục~\ref{muc:c4-dubao}.
11. **[Nên] Chú thích cho khối "có dự báo" trong Bảng 4.12** (595–600). Ghi rõ mẫu số của "lời hứa dài thêm" có
    gồm khách cuối tuần (dài thêm bằng 0) hay không. Thêm một câu rằng 76 → 10 lượt trễ của C-30 là kết quả phát
    lại, bàn ở mục~\ref{muc:c4-dubao}, để người đọc không tưởng đó là kết quả điều phối có dự báo.
12. **[Nên] Viết lại các câu khó trong Phần 1** cho người ngoài ngành. Ưu tiên: D1, D14, D18, D19, D35, D41, D43,
    D45, D46, D47, D63. Bỏ "(scenario)" ở dòng 58 cho đúng quy ước của chương 3.
13. **[Có thể] Giảm tải bảng.** Phần A có 13 bảng và 1 hình trong 5 mục, nhiều đoạn chứa 6–10 con số. Có thể chuyển
    Bảng 4.8 (theo ngày, khung) sang phụ lục và giữ câu tóm tắt 29/34 cùng phép đếm theo khung ở dòng 398–402. Ở
    Hình 4.1, thêm nhãn trục dọc cho cả ba khung, và ghi trong chú thích rằng ở ngưỡng 120 giây kết luận đổi chiều
    (D57).
