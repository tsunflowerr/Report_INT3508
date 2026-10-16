# R23 — Giảng viên phản biện đọc Chương 3 (bản nháp viết lại ngày 11/10/2026)

**Vai:** giảng viên trong hội đồng, nền tảng tối ưu và giao thông.

**Tài liệu đã đọc:**
- `drafts/07-chuong3.tex`, 663 dòng. Mọi số dòng dưới đây là số dòng của tệp này, trừ khi ghi khác.
- `OUTLINE-V2.md`: mục Chương 3 (dòng 161-177) và đoạn đóng góp §6 (dòng 235-313).
- Chương 3 của báo cáo DACN `23020155_TranQuangThanh_Bao cao DACN.pdf` (trang in 13-28; văn bản trích bằng pypdf).
- Để xét phần so sánh với công trình trước có công bằng không, tôi đối chiếu các dòng J01-J12, A01-A24, K02, K26, K27 của
  `evidence/EVIDENCE-REGISTER.md`. Tôi **không** mở bài gốc hay mã nguồn. Chỗ nào cần mã để quyết định, tôi ghi
  "cần kiểm mã" và không đoán.

Đánh số bảng, hình theo thứ tự trong bản nháp (khớp với `07-chuong3-NOTES.md` §9): Bảng 3.1 là giả mã một lượt, 3.2 là
ví dụ ba mốc, 3.3 là ràng buộc và tiêu chí, 3.4 là giả mã kiểm trần, 3.5 là các luật, 3.6 là giả mã dự báo, 3.7 là kiến
trúc. Hình 3.1 là vòng quyết định, 3.2 là ba mốc, 3.3 là các bản tin. Công thức (3.1)-(3.5) lần lượt là `eq:bamoc`,
`eq:luatc`, `eq:dongnhat`, `eq:keodan`, `eq:so`.

---

## 1. Đánh giá chung

**Điểm tốt, nên giữ.**
- Ba mốc $v$, $e$, $p$ và luật C được định nghĩa gọn, có ví dụ số (Bảng 3.2) và hình (Hình 3.2). Đọc xong mục 3.2-3.3,
  người ngoài có thể tự cài phép kiểm trần.
- Đẳng thức (3.3) đặt luật hạn chót, luật trần độ dời khách thấy và luật C lên cùng một trục (dòng 401-410). Đây là đoạn
  hay nhất của chương: hội đồng thấy ngay ba luật khác nhau ở đâu.
- Chương rất trung thực: $e$ không phải giờ đến thật, phép tách không phải đo nhân quả (157-161); Nhận xét đúng theo cấu
  tạo chứ không phải kết quả thực nghiệm (341); ba giới hạn của Nhận xét (346-351); hạn chót nới kiểu Hörl–Zwick cũng có
  tính chất ấy (417-418); luật hạn chót chỉ là phần hạn chót, ở 30-60 giây thay vì 900 giây (395-396); lớp dự báo hiển
  thị giờ đón muộn hơn giờ đón muộn nhất (507-509); các chương trình kiểm do Claude và Codex viết (649-651).
- Tôi không thấy chữ "mới", "duy nhất", "đầu tiên", "vượt trội", "tối ưu" (cho mức trần) hay "lợi ích kinh doanh" ở đâu
  trong chương.
- Khuôn trình bày bám đúng DACN: bảng "Nhóm / Nội dung / Vai trò", giả mã có Đầu vào/Đầu ra và cột chú thích, câu
  "Trong đó" ngay sau công thức.

**Điểm yếu chính.**
1. Bài toán chưa được phát biểu đủ để người khác làm lại: thiếu mục tiêu, mô hình quy hoạch nguyên, vòng đời của yêu cầu
   và của khách, và điều gì kích hoạt một lượt quyết định (mục 2).
2. Nhận xét 3.1 có hai giả thiết ẩn mà chứng minh dựa vào. Phép quy nạp giữ $L_r \le B$ viết quá gọn. Định nghĩa và giới
   hạn thứ ba mâu thuẫn nhau về lúc cập nhật $L_r$ (mục 3).
3. Fielbaum và Alonso-Mora (2020) hoàn toàn vắng mặt trong chương, dù chương đi khác họ ở hai điểm đo lường. Phần so với
   Hörl–Zwick bỏ mất chuyện giờ bắt buộc là ràng buộc cứng, và cụm "không nới theo tắc đường" dễ bị hiểu sai (mục 4).
4. Trong đoạn đóng góp ở OUTLINE-V2, Nhận xét 3.1 bị đẩy thành ưu thế so với luật hạn chót (mục 3.3).
5. Văn phong: đúng khuôn DACN nhưng đặc hơn nhiều. Số đo thực nghiệm và chi tiết cài đặt chen vào phần phương pháp.
   Có 13 thuật ngữ tiếng Anh trong ngoặc và nhiều cụm nội bộ (mục 6).

---

## 2. Phương pháp có đủ rõ để làm lại ở mức khái niệm không?

Phép kiểm trần (Định nghĩa 3.1, Bảng 3.4), ba mốc (3.1), cách kéo dãn lời hứa (3.4, Bảng 3.6) và công thức sổ (3.5) đủ
rõ để làm lại. Những chỗ dưới đây thì chưa.

| # | Dòng | Chỗ thiếu hoặc mơ hồ | Cần thêm |
|---|---|---|---|
| 2.1 | 30-31, 64, 604 | Không nói điều gì kích hoạt một lượt quyết định: mỗi lô sự kiện của FleetPy, hay theo một chu kỳ cố định (bao nhiêu giây mô phỏng)? | Một câu ở 3.1.1. |
| 2.2 | 36-37 | "nhận hay chưa nhận": yêu cầu chưa nhận bị từ chối ngay hay được xét lại ở lượt sau? Chương 4 nói "bị từ chối cuối cùng", tức là có xét lại. | Một câu về vòng đời của yêu cầu. |
| 2.3 | 38-39, 229-232, 303 | Các giai đoạn của khách không được định nghĩa. "Giai đoạn đã nhận" khác "chờ đón" thế nào? Nếu "đã nhận" nằm **trước** lúc xác nhận thì $p_0$ và $L_r = 0$ (đặt "lúc xác nhận", dòng 230-231) chưa tồn tại, nhưng luật vẫn áp. Hình 3.3 có "xác nhận đặt xe": khách có thể từ chối lời mời không? | Một câu hay một sơ đồ nhỏ: gửi yêu cầu → được nhận → xác nhận (công bố $p_0$) → chờ đón → trên xe → đã trả. Ghi luật C áp từ giai đoạn nào. |
| 2.4 | 111-112, 422-423 | "Chọn cho mỗi xe đúng một phương án bằng quy hoạch nguyên" không có biến, không có ràng buộc. Thiếu ràng buộc liên kết các xe: mỗi yêu cầu mới vào nhiều nhất một xe. Không có ràng buộc này thì không cần quy hoạch nguyên. Thứ tự tiêu chí được cài bằng gì: một hàm mục tiêu có trọng số tách bậc, hay giải lần lượt từng tiêu chí? Dùng bộ giải nào của OR-Tools? | Ba dòng công thức (đề xuất ở thay đổi A6). Cần kiểm mã bộ chọn. |
| 2.5 | 97-98 | "Giữ tối đa 100 phương án": giữ theo tiêu chí nào? Phương án giữ nguyên có luôn nằm trong 100 không? "Tối đa 2 yêu cầu mới" được chọn từ mọi yêu cầu trong lô hay chỉ những yêu cầu gần? | Một câu. Điều này cũng là giả thiết của Nhận xét 3.1 (mục 3.1). |
| 2.6 | 276-277 | "Mức dùng trần lớn nhất nhỏ nhất" xuất hiện trước khi "mức dùng trần" được định nghĩa (định nghĩa ngầm ở 425-427 bằng "phần triệu"). "Tổng phần sửa lời hứa do điều phối trên từng chiều" được so thế nào? | Định nghĩa bằng công thức trong bảng (thay đổi B4). |
| 2.7 | 316-317, 518, 627 | "Mười chiều cam kết" chỉ nêu tên bốn chiều. Sáu chiều còn lại là gì, có trần không? | Liệt kê ở chú thích hay ở Phụ lục C. |
| 2.8 | 105-110, 436-440 | "Không làm vi phạm đó tệ hơn" được đo bằng gì? Luật phục hồi thứ hai thay thế hay mở rộng luật thứ nhất? Giả mã chạy cả hai (dòng 10 rồi 11), còn văn bản nói "dùng luật thứ hai". "Khóa theo giai đoạn" (439) chưa định nghĩa. | Thay đổi B6. |
| 2.9 | 105, 323-324 | "Xe bị ép" có hai định nghĩa: dòng 105 là "luật lời hứa loại cả phương án giữ nguyên", còn dòng 323 là "luật lời hứa loại **hết** phương án, kể cả phương án giữ nguyên". | Chọn một. |
| 2.10 | 237, 114-115 và 349-351 | Mâu thuẫn về lúc cập nhật $L_r$ (xem 3.2.c). | Kiểm mã rồi sửa. |
| 2.11 | 346-348 | Khi (N) không thỏa, xe "kẹt", nhưng giả mã không có nhánh xử lý. Với người làm giao thông, câu hỏi đầu tiên là: tắc đường đẩy kế hoạch giữ nguyên quá giờ đón muộn nhất hay quá giới hạn thời gian ngồi xe của một khách đã xác nhận thì sao? Ràng buộc dịch vụ có áp cho khách đã xác nhận không? Nếu có thì (N) hỏng chính vì tắc đường, đúng chỗ luật C muốn tránh. | Một đoạn ngắn: ràng buộc dịch vụ áp cho khách đã xác nhận ra sao, và hệ thống làm gì khi xe kẹt. |
| 2.12 | 114, 142, 644 | "Công bố" nghĩa là gì trong mô phỏng? 382.006 lần cập nhật giờ trả trên 185 lần chạy, tức khoảng 2.065 lần mỗi lần chạy. Hội đồng sẽ hỏi khách có bị báo lại giờ hàng chục lần không, và một lần lệch 1 mili giây có tính là "thay đổi" không. | Một câu: ngưỡng coi là thay đổi, và "công bố" là ghi vào trạng thái hay là báo cho khách. |
| 2.13 | 480-482, 508-509 | Lời hứa theo dự báo áp cho cả giờ đón lẫn giờ trả (dòng 508 nói "giờ đón hiển thị"), nhưng Bảng 3.6 chỉ nói "một lời hứa". | Ghi rõ áp cho cả hai. |
| 2.14 | 375-386, 396-397, 631, 652-653 | Các tập "tắc đường cố định", "chỉnh trần buổi sáng", "chiều tuyết", "tập kịch bản tĩnh", "15 lần chạy hiệu chỉnh" được dùng trước khi định nghĩa. | Thêm "(mô tả ở mục 4.1, Bảng 4.2)" vào chú thích Bảng 3.5. Định nghĩa "lần chạy hiệu chỉnh" một lần. |
| 2.15 | 342 và 427 | Hai đơn vị lẫn nhau: "0 quyết định bị ép trong 20.101 quyết định" và "3.506 lượt" có mức dùng trần. 3.506 là bao nhiêu phần của 20.101, và vì sao chỉ ngần ấy lượt có tiêu chí 3? "Quyết định bị ép" tính theo xe hay theo lượt? | Định nghĩa đơn vị "quyết định" và "quyết định bị ép" (Chương 4 dùng "41,3% quyết định bị ép"). |
| 2.16 | 631-633 | Thời gian chạy không ghi máy (CPU, RAM, hệ điều hành) và không nói có tính thời gian của FleetPy không. | Một mệnh đề. |

---

## 3. Nhận xét 3.1 về phương án giữ nguyên kế hoạch

### 3.1 Giả thiết

Giả thiết (N) được nêu rõ và nêu trước khi dùng (324-325). Đây là điểm tốt. Nhưng chứng minh còn dựa vào hai điều chưa
có trong (N), và (N) chứa một điều không cần giả thiết.

- **(a) Phương án giữ nguyên phải còn lại sau khi cắt còn 100 phương án.** Dòng 96 ghi "luôn dựng trước", nhưng không nói
  nó luôn được giữ khi cắt (dòng 97-98). Chữ "luôn" cũng mâu thuẫn với dòng 346-347: khi kế hoạch đang chạy đã vi phạm
  ràng buộc thì bộ sinh không dựng được nó.
- **(b) Giờ trả của phương án giữ nguyên phải được tính bằng đúng phép tính dùng cho $e$.** Câu then chốt của chứng minh
  (334-335) là "$p_r = e_r$". Đây là tính chất của cài đặt, không phải của định nghĩa. Chính chương này cho thấy $p$ và
  $e$ có thể lệch nhau 1 mili giây ở các phương án khác (220). Ví dụ ở dòng 244-245 còn đưa $L_A$ lên đúng bằng $B$. Khi
  $L_r = B$, chỉ cần lệch 1 mili giây là phương án giữ nguyên bị loại, và Nhận xét sai. Con số 0 quyết định bị ép (342)
  gợi ý rằng cài đặt thỏa điều này, nhưng chứng minh phải ghi nó thành giả thiết.
- **(c) Khóa không cần là giả thiết.** Dòng 266-267 đã nói khóa so với $e$. Phương án giữ nguyên chính là kế hoạch dùng để
  tính $e$, nên nó luôn qua khóa. Nên ghi đây là hệ quả, để (N) chỉ còn lại ràng buộc dịch vụ.

### 3.2 Chứng minh

- **(a)** Bước chính ($c = 0$ nên phép kiểm cho qua) đúng và ngắn gọn.
- **(b)** Câu cuối (337-338) là một phép quy nạp viết quá gọn, và hơi vòng. "$L_r$ chỉ tăng khi một phương án đã qua (3.2)
  được chọn" chỉ đúng nếu xe chưa từng bị ép, mà đó lại là điều Nhận xét đang chứng minh. Câu này cũng chỉ đúng nếu (N)
  thỏa ở **mọi** lượt trước. Nên tách thành một câu quy nạp riêng, có điều kiện (đề xuất ở thay đổi A2).
- **(c) Mâu thuẫn về lúc cập nhật $L_r$.** Định nghĩa 3.1 (237) viết "Khi phương án được chọn **và lời hứa mới được công
  bố**, $L_r$ được cập nhật". Dòng 14 của Bảng 3.1 (114-115) cũng chỉ cập nhật cho "khách có lời hứa mới hay thay đổi".
  Nhưng giới hạn thứ ba (349-351) lấy ví dụ $v = p = 600$, $e = 720$: lời hứa **không đổi**, vậy mà nói "vẫn bị tính"
  $|c| = 120$. Có hai khả năng, và phải kiểm mã (BUDGET, LEDGER) để biết khả năng nào đúng.
  - Nếu cài đặt cộng $|c|$ vào $L_r$ cả khi $p = v$, thì sửa dòng 237 và dòng 14 của giả mã cho khớp.
  - Nếu chỉ cộng khi lời hứa đổi, thì câu ở dòng 240 ("tổng $|c|$ ... không vượt $B$") sai trong trường hợp biên này: một
    lần sửa $|c| = 120$ giây có thể qua phép kiểm (khi còn đủ trần) mà không bị trừ vào trần. Khi đó phải viết lại giới
    hạn thứ ba thành "phép kiểm vẫn tính ...", và nói rõ chỗ hở này.
- **(d)** "Nhận xét" có kèm chứng minh là chấp nhận được, vì chủ nghiên cứu đã chọn hạ từ định lý xuống. Nên giữ chứng minh
  ở dạng "Chứng minh. ... □" như hiện tại.

### 3.3 Có bị nói quá thành ưu thế không?

**Trong chương 3: không.** Chương ghi "đúng theo cấu tạo, không phải kết quả thực nghiệm" (341), nêu ba giới hạn
(346-351), và nói hạn chót nới kiểu Hörl–Zwick cũng có tính chất này (417-418). Nên thêm hai điều.
- Một câu nói thẳng rằng tính chất này và giới hạn thứ hai là hai mặt của cùng một lựa chọn: luật C không bị ép **vì** nó
  không tính phần do tắc đường, và cũng vì thế nó không giới hạn phần đó.
- Ở Bảng 3.5, cột "Khi xe bị ép" của luật C ghi "Không xảy ra theo cấu tạo". Cần thêm "khi (N) thỏa". Cũng nên để ý rằng
  hàng điều phối không trần cũng ghi "Không xảy ra" (374). Tính chất này vì vậy không riêng của luật C: điều phối không
  trần có nó, và hạn chót nới kiểu Hörl–Zwick (chưa chạy) cũng có.

**Trong đoạn đóng góp (OUTLINE-V2 dòng 247-248): có.** Câu "Luật hạn chót ... không giữ được điều nó hứa với ít nhất một
khách ở 28 trên 34 kịch bản; luật C giữ được ở mọi kịch bản, theo cấu tạo" đặt hai luật cạnh nhau như hơn kém. Hội đồng sẽ
chỉ ra bốn điều.
1. Hai luật có nghĩa vụ khác nhau. Luật C "giữ được" vì nghĩa vụ của nó không chứa phần do tắc đường.
2. "Điều nó hứa" gây hiểu nhầm, vì luật C không hứa gì với khách về giờ đến (chính chương 3, dòng 349, đã nói vậy).
3. Luật hạn chót được chạy ở 30 giây, trong môi trường tắc đường đổi theo khung 15 phút. Đó là ngoài vùng mà Schulz và
   Pfeiffer thiết kế: họ dùng thời gian đi cố định và độ chùng 900 giây (sổ bằng chứng J10).
4. Đối chứng cùng có tính chất này, tức hạn chót nới kiểu Hörl–Zwick, thì chưa được chạy.

Câu thay thế ở thay đổi A5.

---

## 4. So với các công trình trước

### 4.1 Hörl và Zwick (2022) — dòng 153-154, 413-419

**Đã làm tốt:** nói mốc $e$ lấy từ họ. Ghi $\max(p_0 + B, e)$ là "cách viết lại của khóa luận chứ không phải định nghĩa
trong bài" (416-417). Ghi tính chất chung là "suy luận, chưa được chạy" (418).

**Chưa công bằng hoặc chưa chính xác:**
- **(a) Bỏ mất ràng buộc cứng.** Dòng 414-416 chỉ nói công thức 7 "kèm phạt cho mỗi giây vượt". Theo sổ bằng chứng (J03),
  tuyến của họ phải thỏa giờ bắt buộc như ràng buộc cứng (ràng buộc 9-10), còn phạt (11) là cho việc vượt giờ gốc. Viết
  như hiện tại, người đọc sẽ hiểu họ chỉ phạt mềm và tự suy ra khác biệt "cứng hay mềm", điều mà K26 đã cấm dùng làm
  khác biệt.
- **(b) "Không nới theo tắc đường" (242, 419; OUTLINE-V2 dòng 243) dễ hiểu sai.** Dưới luật C, hạn chót thực tế của giờ
  trả là $e + (B - L_r)$, nên nó dịch theo tắc đường hoàn toàn. Thứ không đổi theo tắc đường là **phần được phép dời do
  điều phối**. Viết bằng $c$ thì rõ hơn:
  - hạn chót nới cho phép $c \le \max(p_0 + B - e,\, 0)$: phần này lớn lên khi đường thông hơn dự kiến, và về 0 khi tắc
    đường đã đẩy $e$ quá $p_0 + B$;
  - luật C cho phép $|c| \le B - L_r$, bất kể tắc đường.

  Đây vừa là khác biệt thật, vừa cho thấy rõ cái giá: khi tắc đường làm $e$ trễ xa, luật C vẫn cho dời thêm $B - L_r$.
- **(c) Câu 153-154** viết "Hörl và Zwick ... **cũng** tính lại", nghe như họ đi sau. Nên viết "đã tính lại ..., khóa luận
  dùng lại mốc này".
- **(d) Chưa nói cùng động cơ.** Theo J02, Hörl và Zwick nới hạn trả để tránh "undefined system states" khi không còn chuỗi
  trả khả thi. Đây chính là động cơ của Nhận xét 3.1. Nên thêm một câu kế thừa.
- **(e) Phạm vi áp dụng** nêu đúng ý ("một trần chung cho mọi khách đã nhận"). Có thể nói rõ hơn: họ chỉ nới cho khách
  đang trên xe sắp bị trễ (J01, J05), còn luật C áp cả cho khách chờ đón.

### 4.2 Fielbaum và Alonso-Mora (2020) — vắng mặt

Chương không có `\cite{fielbaum2020}`, dù khóa này đã có trong danh mục (`ridebound/noi-dung/10-tai-lieu.tex:13`). Đây là
thiếu sót lớn nhất của phần so sánh, vì chương 3 đi khác họ ở hai điểm đo lường mà không nói ra.
- Họ chỉ tính phần thay đổi **bất lợi** (J06). Luật C tính cả hai chiều (217-218), nhưng lý do đưa ra chỉ là lý do kỹ
  thuật.
- Họ đo từ lần gán đầu đến lúc trả, tức so điểm đầu với điểm cuối (J06). Luật C cộng từng lần sửa, nên các lần dời ngược
  chiều không triệt tiêu nhau.

Ngoài ra, chương kế thừa hai ý của họ mà không ghi nguồn:
- tách riêng phần thay đổi do nhà điều hành gây ra (J06);
- kiểm soát trước khi quyết định. Ở mục 6 bài của họ, khách đã gán không bị từ chối và thời gian chờ tối đa được giữ bằng
  giá trị đã dự báo; tỉ lệ từ chối tăng từ 34,5% lên 45,6% (J08).

Họ cũng cố ý chọn giờ thấp điểm để bỏ qua tắc đường (J07), còn khóa luận làm ngược lại. Hộp "không nhận là mới" ở
OUTLINE-V2 (dòng 297) đã ghi điều này cho chương 1, nhưng chương 3, nơi định nghĩa luật, thì im lặng. Đoạn đề xuất ở thay
đổi A1.

### 4.3 Schulz và Pfeiffer (2026) — dòng 385-386, 395-396

**Đã làm tốt:** nói chỉ mượn phần hạn chót, ở 30-60 giây thay vì 900 giây, và không tái lập thuật toán của họ.

**Còn thiếu:**
- **(a)** Họ dùng thời gian đi cố định (J10). Trong bài của họ, tắc đường không thể đẩy giờ trả vượt hạn chót. Ở khóa
  luận, độ chùng 30-60 giây cộng với hệ số tắc đường đổi theo khung 15 phút làm riêng tắc đường cũng đủ ép xe (dòng
  407-410 đã chỉ ra cơ chế này). Cần một câu nói rằng số lần luật hạn chót bị ép ở Chương 4 nói về hạn chót chặt trong
  môi trường tắc đường thay đổi, không nói về phương pháp của họ.
- **(b)** Không nói vì sao chọn 30-60 giây. Nếu lý do là để độ chùng bằng trần của luật C, hãy viết ra; hội đồng chắc chắn
  sẽ hỏi.
- **(c)** Nên nói rõ chỗ kế thừa: hạn chót gắn với lời hứa đầu ($l_i = B_i + l$ ở J10).

### 4.4 Những chỗ kế thừa khác chưa ghi nguồn trong chương 3

- Bước chọn mỗi xe một phương án bằng quy hoạch nguyên là bước gán của kiến trúc yêu cầu–chuyến–xe. Nên trỏ về mục 2.1 và
  `alonsomora2017` (khóa có ở `10-tai-lieu.tex:7`). Cụm "bộ điều phối ghép chuyến thông thường" ở dòng 51 cũng cần trỏ về
  mục 2.1.
- Luật phục hồi "không tệ hơn" được OUTLINE-V2 (dòng 301) xếp vào "không nhận là mới", nhưng dòng 436-440 không nói vậy.
- Cách kéo dãn lời hứa (3.4) chính là phép tính thời gian đi phụ thuộc thời điểm, với tốc độ đổi theo từng khung, quen
  thuộc trong định tuyến phụ thuộc thời gian (ví dụ Ichoua, Gendreau và Potvin, 2003, EJOR). Bài này chưa có trong danh
  mục. Mở bài gốc trước khi trích, hoặc chỉ viết một câu không trích.

---

## 5. Câu nói quá và câu hội đồng sẽ chất vấn

### 5.1 Câu nói quá hoặc sai sắc thái

| Dòng | Câu | Vấn đề |
|---|---|---|
| 164-165 | "ghép khách B làm giờ trả của khách A lùi 70 giây" | Nhân quả, và sai ngay trong ví dụ: chỉ 30 trong 70 giây là phần dời do điều phối. Câu này mâu thuẫn với dòng 160-161. |
| 240 | "Như vậy, đến hết chuyến, tổng $\lvert c\rvert$ của mỗi khách không vượt $B$." | Khẳng định không điều kiện. Câu này chỉ đúng khi xe không bị ép, và còn phụ thuộc vào 3.2.c. |
| 96 | "luôn dựng trước" | Mâu thuẫn với 346-347. |
| 128-129 | "giữ thứ tự các điểm cũ, nên không chuyển khách đã nhận sang xe khác" | Suy luận không đúng: giữ thứ tự điểm trong một xe không kéo theo việc không chuyển xe. Lý do thật là bộ sinh không bỏ điểm cũ nào. |
| 242, 419 | "không nới theo tắc đường" | Xem 4.1.b. |
| 341 | "dữ liệu chỉ khớp với nó" | Đúng ý nhưng câu cụt. Xem thay đổi C4. |
| 509 | "phải xử lý trước khi triển khai" | Hàm ý đã có kế hoạch triển khai. Nên nói "trước khi đưa lớp dự báo vào bộ điều phối". |
| 644 | "Kiểm đặc tả" | Tên lớn hơn việc làm. Phép kiểm này chỉ tính lại $\lvert x\rvert$, $\lvert c\rvert$, $\lvert z\rvert$ từ $v$, $e$, $p$ **ghi trong cùng sổ**, nên nó kiểm sổ ghi nhất quán chứ không kiểm $e$ được tính đúng. |
| 647 | "Tính lại độc lập" | Độc lập về mã, nhưng không độc lập về đặc tả: cả hai chương trình viết từ cùng đặc tả chỉ số, và đều do mô hình ngôn ngữ viết (649-650). |
| OUTLINE 247-248 | "không giữ được điều nó hứa ... luật C giữ được ở mọi kịch bản" | Xem 3.3. |
| OUTLINE 251 | "đều ở mức trần nới rộng" | Mơ hồ. Viết "đều ở trần 120 giây". |

### 5.2 Câu hội đồng sẽ hỏi (nên có sẵn câu trả lời trong chương)

1. "Trả sớm thì khách mừng, sao lại tính vào trần?" Dòng 217-219 chỉ có lý do kỹ thuật. Fielbaum và Alonso-Mora chỉ tính
   phần bất lợi.
2. "Giờ đón bị khóa bằng đúng giờ đón khi giữ nguyên kế hoạch (265-266), vậy còn chèn được khách mới vào trước điểm đón của
   khách đang chờ không? Vì sao giờ đón có trần 0, còn giờ trả có 30 giây?" Khóa này chặt hơn trần giờ trả rất nhiều và
   có ở cả điều phối không trần lẫn luật C, nhưng chương không bàn.
3. "Biến quyết định và ràng buộc của quy hoạch nguyên là gì? Thứ tự tiêu chí được cài thế nào?" (2.4)
4. "Tắc đường đẩy kế hoạch giữ nguyên quá giờ đón muộn nhất thì (N) còn đúng không?" (2.11)
5. "Nhận xét 3.1 có tầm thường không? Luật C không bị ép vì nó không tính phần do tắc đường." (3.3)
6. "Sao không chạy hạn chót nới kiểu Hörl–Zwick? Luật hạn chót 30 giây có phải đối chứng công bằng không?" (4.1, 4.3)
7. "Nếu vế cộng dồn gần như không bao giờ là lý do loại phương án (3 bản ghi, OUTLINE dòng 250-251), thì khác biệt 'cộng
   qua cả chuyến' với Hörl–Zwick có ý nghĩa gì trên dữ liệu này?" Chương 3 nên trỏ tới mục 4.5 ngay ở dòng 419.
8. "Vì sao bỏ ngày 15/11 khỏi ngày nguồn (468)? Hệ thống thật biết ngày nào bất thường bằng cách nào?" Nên nói rõ đây là
   lựa chọn của khóa luận và hệ thống thật cần một quy tắc tự động.
9. "Khách có thật sự được báo lại giờ khoảng 2.000 lần mỗi lần chạy không?" (2.12)
10. "Vì sao không chạy lại bộ kiểm thử (641-643)?" Chạy `dotnet test` trên đúng bản mã của bộ chạy đã lưu chỉ tốn vài
    phút.
11. "Các chương trình kiểm do mô hình ngôn ngữ viết. Sinh viên đã tự kiểm tay ít nhất một khách chưa?" Nên thêm một khách
    thật, lần theo bản ghi, ở mục 3.2 hay 3.7.
12. "Thời gian chạy đo trên máy nào? Luật C chạy nhanh hơn ghép tự do có nghĩa là phép kiểm trần không tốn gì không?"
    Dòng 633 đã nói chưa đo riêng; nên thêm "không dùng các số này để so chi phí tính toán giữa các luật".

---

## 6. Văn phong so với chương 3 của báo cáo DACN

**Giống DACN (tốt):** bảng ràng buộc "Nhóm / Nội dung / Vai trò" (DACN Bảng 3.1, tr. 16); giả mã trong bảng có Đầu
vào/Đầu ra và cột chú thích (DACN Bảng 3.2, 3.4, 3.5, 3.8); "Trong đó" ngay sau công thức (bản nháp 152, 461, 527); ví dụ
dựng tay có số cụ thể.

**Khác DACN (cần sửa):**
- **Mở chương.** DACN mở bằng ý chính và lý do trước ("Khác với cách tiếp cận chỉ lựa chọn một địa điểm hẹn ..., Optigo
  xem mỗi kết quả đề xuất như một phương án di chuyển hoàn chỉnh"; "Cách tiếp cận này xuất phát từ thực tế rằng ...",
  tr. 13), rồi mới đến lộ trình. Bản nháp (17-21) chỉ có lộ trình. Người đọc đi hết 3.1 mới biết ý chính là "so với kế
  hoạch giữ nguyên".
- **Câu "vì sao".** DACN mở mỗi mục bằng lý do cần bước đó (3.3, tr. 16: "Nếu tâm tìm kiếm bị lệch, hệ thống có thể bỏ sót
  các địa điểm tốt ..."). Bản nháp làm tốt ở 138-140 và 447-448. Còn thiếu ở ba chỗ: vì sao cộng qua cả chuyến (242-244
  chỉ có ví dụ), vì sao tính cả chiều sớm (217-219), vì sao bộ chọn đặt "nhận nhiều yêu cầu" trước "ổn định" (Bảng 3.3).
- **Số đo trong chương phương pháp.** Chương 3 của DACN gần như chỉ có số minh họa (50 → 15 địa điểm, tr. 18; $s = 9$ cho
  4.608 trạng thái, tr. 23). Bản nháp có hơn 20 số đo thực nghiệm: 1 ms (220); 20.101 và 20.435 (342-343); 3.503, 3.506,
  3.504 (427-428); 21/34 và 13 (469-470); 34/1.471 (508); 730, 667, 641 (632-633); 1.025/1.025 (642); 382.006, 185, 170,
  15 (644-645); 13 hạng mục (647). Nên giữ những số cần để định nghĩa (21/34 kịch bản có dự báo) và một số kiểm chứng
  (0 quyết định bị ép). Phần còn lại chuyển sang mục 4.10 hay Phụ lục C.
- **Độ dài câu.** Câu của DACN thường mang một ý. Bản nháp có nhiều câu 3-4 vế nối bằng dấu chấm phẩy: 395-398, 424-428,
  436-440, 505-510, 644-646. Các câu viết lại ở thay đổi C8.
- **Thuật ngữ tiếng Anh.** Bản nháp có 13 cụm trong ngoặc: decision epoch, candidate plan, solver, insertion-only candidate
  generator, keep-route option, forced decision, recovery rule, cap, selector, lexicographic order, forecast-aware promise,
  replay, per-rider ledger. DACN dùng ít, và chủ yếu là tên thuật toán đã có trong tài liệu (open-path TSP, Held–Karp,
  2-opt). Nên giữ những cụm người đọc cần để tra tài liệu (decision epoch, insertion, lexicographic order). Các cụm còn lại
  đưa vào Danh mục ký hiệu và chữ viết tắt.
- **Cụm nội bộ, nặng hơn mức cần:** "mười chiều cam kết" (316, 518, 627), "tệp chính sách" (431), "chính sách chi phí
  cuốn chiếu mặc định" (378), "khóa theo giai đoạn" (439), "1.000.000 phần triệu" (426), "bản ghi chặn" (295, 315), "bộ
  chạy cũ" (397, 632, 653), "hạt giống cố định 7" (625), "giới hạn khối lượng" (624), "phép so của việc thêm trần" (432),
  "vế này" (219), "LOCKS", "B1", "C1" (396-398).
- **"Bảng giờ đi"** (35, 144-145, 299-301, 335) dễ bị đọc thành bảng giờ khởi hành. Nên dùng "bảng thời gian đi", cho
  khớp với "thời gian đi thẳng" ở dòng 261.
- **Thuật ngữ không thống nhất:**
  - "khoảng giờ đón" (34), "cửa sổ đón" (40, 100) và "giờ đón muộn nhất" (509) cho cùng một thứ;
  - "ràng buộc vật lý" (347) và "ràng buộc dịch vụ" (100, 261, 325);
  - "khách đã nhận trên xe" (102, 231, 269, 294, 298, 330, 335) dùng cả cho khách đang chờ đón, tức chưa "trên xe". Nên
    viết "khách đã nhận được gán cho xe".
- **Chỗ đặt bảng.** DACN đặt bảng ràng buộc ở mục mô hình bài toán (3.2.2, tr. 15-16), sau đoạn giải thích ràng buộc cứng
  và tiêu chí mềm. Bản nháp đặt Bảng 3.3 ở mục 3.3 (luật C), trước khi bộ chọn được giải thích ở 3.4, trong khi 3.1.1 đã
  trỏ tới nó (41). Nên chuyển Bảng 3.3 lên 3.1.1.

---

## 7. Danh sách thay đổi, xếp theo mức quan trọng

### Mức A — phải sửa (ảnh hưởng tính đúng hoặc tính công bằng)

**A1. Thêm Fielbaum và Alonso-Mora (sau dòng 419; một mệnh đề ở 217-219).** Đề xuất:
> Ý tách riêng phần thay đổi do nhà điều hành gây ra và kiểm soát nó trước khi quyết định đã có ở Fielbaum và
> Alonso-Mora~\cite{fielbaum2020}. Họ đo, cho từng khách, thời gian dự báo thay đổi bao nhiêu từ lần gán đầu tới lúc
> trả, chỉ tính phần thay đổi bất lợi, và chọn khung giờ thấp điểm để có thể bỏ qua tắc đường. Ở mục 6 của bài, họ thử
> không cho từ chối khách đã gán và giữ thời gian chờ tối đa bằng giá trị đã dự báo; tỉ lệ từ chối tăng lên. Khóa luận
> kế thừa hai ý này. Luật C khác ở cách đo: mỗi lần sửa được so với mốc $e$ chứ không so điểm đầu với điểm cuối, nên hai
> lần dời ngược chiều không triệt tiêu nhau; chiều sớm cũng được tính; và đại lượng bị giới hạn là giờ trả chứ không
> phải thời gian chờ.

(Các chi tiết lấy từ J06-J08 của sổ bằng chứng. Mở lại bài để ghi số mục, số trang trước khi nộp.)

**A2. Sửa giả thiết (N) và chứng minh (324-338).** Thay 324-325 bằng:
> Gọi \textbf{(N)} là giả thiết sau, áp cho lượt đang xét: (i) bộ sinh dựng được phương án giữ nguyên kế hoạch, và phương
> án này còn lại sau khi cắt còn tối đa 100 phương án; (ii) phương án đó thỏa các ràng buộc dịch vụ; (iii) giờ trả của
> từng khách theo phương án đó được tính bằng đúng phép tính dùng cho mốc $e$ (cùng trạng thái, cùng bảng thời gian đi,
> cùng cách làm tròn). Các khóa không cần đưa vào giả thiết: khóa so với chính kế hoạch giữ nguyên, nên phương án này
> luôn qua.

Thay chứng minh (334-338) bằng:
> \textit{Chứng minh.} Theo (N)(iii), với mọi khách $r$ được gán cho xe, $p_r = e_r$, nên
> $L_r + |p_r - e_r| = L_r \le B$ và phép kiểm~\eqref{eq:luatc} cho qua. Theo (N)(i)-(ii), và vì khóa luôn qua, phương
> án cũng qua mọi kiểm tra khác. \hfill$\square$
>
> Điều kiện $L_r \le B$ không phải giả thiết thêm nếu (N) đúng ở mọi lượt kể từ khi khách $r$ xác nhận đặt xe. Lúc xác
> nhận, $L_r = 0$. Ở mỗi lượt sau đó, theo Nhận xét, xe không bị ép, nên phương án được chọn đã qua~\eqref{eq:luatc} và
> $L_r$ mới vẫn không vượt $B$.

**A3. Giải quyết mâu thuẫn về lúc cập nhật $L_r$ (237; dòng 14 của Bảng 3.1; 349-351).** Kiểm mã, rồi chọn một trong hai
cách.
- Nếu cài đặt cộng $|c|$ cả khi lời hứa không đổi, sửa dòng 237:
  > Sau mỗi lượt, với mỗi khách $r$ được gán cho xe, $L_r$ được cộng thêm $|p_r - e_r|$ của phương án được chọn, kể cả
  > khi giờ trả công bố không đổi.

  Và dòng 14 của Bảng 3.1: "với mỗi khách đã nhận trên các xe: cập nhật $L_r$; nếu lời hứa đổi thì công bố và ghi một
  dòng sổ".
- Nếu không, sửa giới hạn thứ ba:
  > Thứ ba, phép kiểm vẫn tính cả lần sửa đưa giờ trả về đúng lời hứa: với $v = p = 600$ và $e = 720$, phương án kéo giờ
  > trả về 600 giây có $z = 0$ nhưng $|c| = 120$, nên bị loại nếu $L_r + 120 > B$.

  Đồng thời sửa dòng 240 cho đúng với trường hợp biên này.

**A4. Viết lại đoạn so với Hörl–Zwick (413-419).** Đề xuất:
> Gần nhất với cách đo này là Hörl và Zwick~\cite{horl2022}. Ở mỗi lượt quyết định, họ duyệt tuyến đang gán theo thời
> gian đi hiện tại để có giờ trả cập nhật, tức mốc $e$. Công thức 7 của họ đặt giờ trả bắt buộc của khách trên xe đang
> xét bằng giá trị lớn hơn giữa giờ cập nhật và giờ trả muộn nhất. Tuyến mới phải thỏa giờ bắt buộc này như một ràng buộc
> cứng (ràng buộc 9-10), và mỗi giây vượt giờ trả muộn nhất gốc bị phạt (công thức 11). Mục đích của họ là tránh trạng
> thái không còn thứ tự trả khách nào khả thi, cũng là mục đích của Nhận xét~\ref{nx:giunguyen}. Nếu đặt giờ trả muộn
> nhất là $p_0 + B$, ta có hạn chót nới $p \le \max(p_0 + B, e)$. Đây là cách viết lại của khóa luận, không phải định
> nghĩa trong bài. Viết theo phần dời do điều phối, hạn chót nới cho phép $c \le \max(p_0 + B - e, 0)$: phần này lớn lên
> khi đường thông hơn dự kiến, và về 0 khi tắc đường đã đẩy $e$ quá $p_0 + B$. Luật C cho phép $|c| \le B - L_r$, bất kể
> tắc đường. Vì phương án giữ nguyên có $p = e$, hạn chót nới cũng có tính chất của Nhận xét~\ref{nx:giunguyen}; đây là
> suy luận, chưa được chạy. Tóm lại, luật C khác ở ba chỗ: cùng một trần cho mọi khách đã nhận, kể cả khách chờ đón;
> phần được phép dời không phụ thuộc tắc đường; và phần dời được cộng qua cả chuyến (mục 4.5 cho thấy vế cộng dồn hiếm khi
> là lý do loại phương án; chương 4 chưa có nhãn cho mục này, người ghép thêm `\ref` sau).

Đồng thời đổi dòng 153-154:
> Mốc $e$ không phải ý của khóa luận: Hörl và Zwick~\cite{horl2022} đã tính lại giờ trả trên tuyến đang gán theo thời
> gian đi hiện tại ở mỗi lượt quyết định, và khóa luận dùng lại mốc này.

Và dòng 242: "mức này không nới theo tắc đường" → "phần được phép dời không phụ thuộc tắc đường".

**A5. Bỏ khung "ưu thế" trong đoạn đóng góp (OUTLINE-V2 dòng 247-248).** Đề xuất (độ dài gần như cũ):
> Luật hạn chót 30 giây tính từ lời hứa đầu phục vụ cùng số lượt, nhưng vì tính cả phần do tắc đường nên ở 28 trên 34
> kịch bản nó phải phá chính luật của mình với ít nhất một khách; luật C không tính phần đó nên không gặp trường hợp này.

Đổi dòng 243 thành "phần được phép dời không phụ thuộc tắc đường", và dòng 251 "đều ở mức trần nới rộng" thành "đều ở
trần 120 giây".

**A6. Bổ sung phát biểu bài toán (30-44) và mô hình chọn (111, 422-423).**
- Thêm vào danh sách ở 3.1.1:
  > \item \textbf{Mục tiêu:} theo thứ tự tiêu chí ở Bảng~\ref{bang:rangbuoc}: ít xe bị ép nhất, nhận nhiều yêu cầu mới
  > nhất, ít sửa lời hứa nhất, rồi tổng thời lượng tuyến nhỏ nhất.
- Thêm câu kích hoạt và vòng đời (điền chỗ trong ngoặc vuông từ mã hoặc cấu hình):
  > Một lượt quyết định bắt đầu khi bộ mô phỏng gửi một lô sự kiện [mỗi … giây mô phỏng]. Yêu cầu không được nhận ở một
  > lượt thì [được xét lại ở các lượt sau cho tới khi … / bị từ chối ngay].
- Thêm sau dòng 423 (kiểm mã bộ chọn rồi điền ngoặc vuông):
  > Gọi $y_{k\pi} \in \{0, 1\}$ bằng 1 nếu xe $k$ chọn phương án $\pi \in P_k$. Bộ giải tìm $y$ sao cho
  > $\sum_{\pi \in P_k} y_{k\pi} = 1$ với mọi xe $k$, và $\sum_{k} \sum_{\pi \in P_k:\, j \in \pi} y_{k\pi} \le 1$ với mọi
  > yêu cầu mới $j$, tức mỗi yêu cầu mới được nhận vào nhiều nhất một xe. Thứ tự tiêu chí được cài bằng [một hàm mục tiêu
  > có trọng số tách bậc / giải lần lượt từng tiêu chí], với bộ giải [tên] của OR-Tools.
- Dòng 97-98: thêm tiêu chí giữ 100 phương án, và ghi rằng phương án giữ nguyên luôn được giữ (nếu đúng).

**A7. Vòng đời của khách, và trường hợp (N) hỏng vì tắc đường (231-232, 346-348).** Thêm vào 3.1.1:
> Mỗi khách đi qua các giai đoạn: gửi yêu cầu; được bộ điều phối nhận vào kế hoạch của một xe; xác nhận đặt xe, lúc đó
> lời hứa đầu $p_0$ được công bố; chờ đón; trên xe; đã trả. Luật C áp từ [giai đoạn …] tới lúc trả.

Thêm sau giới hạn thứ nhất (348):
> Khi tắc đường làm kế hoạch giữ nguyên vượt giờ đón muộn nhất hay giới hạn thời gian ngồi xe của một khách đã xác nhận,
> hệ thống [giữ kế hoạch và ghi nhận vi phạm / …].

(Kiểm cấu hình xử lý đón muộn trước khi viết. NOTES §5 ghi chế độ `lateBoarding` chưa có trong sổ.)

**A8. Gỡ các ký hiệu trùng.**
- Khách B và trần $B$ nằm trong cùng một câu (244: "với ... $B = 30$ giây, phương án ghép B"). Đổi khách B thành "khách
  M" (khách mới) ở 164-166, 171-213, 244-245. Câu 244-245 thành:
  > Ở Bảng~\ref{bang:vidu-bamoc}, với $L_A = 0$ và $B = 30$ giây, phương án ghép khách M có $|c| = 30$ giây, đúng bằng
  > trần, nên vẫn được giữ; sau lượt này, phần trần còn lại của A bằng 0.
- $k$ vừa là xe (Bảng 3.1, 3.4) vừa là số lần cập nhật (3.3). $t$ vừa là chỉ số lần cập nhật (3.3, 3.5) vừa là thời điểm
  công bố (3.4, Bảng 3.6). Đổi chỉ số lần cập nhật thành $j$ và số lần thành $n$:
  $\sum_{j=1}^{n} (x_j + c_j) = \sum_{j=1}^{n} z_j = p_n - p_0$; $\rho = a - p_n$; $q = \sum_j c_j$.
- "$N$" là tập ngày nguồn (Bảng 3.6, dòng 2) và "(N)" là giả thiết. Đổi tập ngày thành $H$.
- Định nghĩa 3.1 (229-230) đặt tên $p_0$ nhưng không dùng. Viết "kể từ lúc công bố lời hứa đầu" và bỏ $p_0$ khỏi định
  nghĩa (đã định nghĩa ở chỗ khác), hoặc chuyển định nghĩa $p_0$ lên 3.2.

### Mức B — nên sửa (rõ ràng hơn, hội đồng sẽ hỏi)

**B1. Câu nhân quả trong ví dụ (164-166).**
> Bảng~\ref{bang:vidu-bamoc} và Hình~\ref{hinh:bamoc} là một ví dụ dựng tay: sau khi ghép khách M, giờ trả của khách A
> muộn hơn lời hứa 70 giây; trong đó chỉ 30 giây là phần dời do điều phối, còn 40 giây là phần vẫn có nếu xe không ghép
> thêm ai.

**B2. Lý do tính cả chiều sớm (217-220).**
> Phần dời do điều phối được tính theo độ lớn: kéo giờ trả sớm hơn $e$ hay đẩy muộn hơn $e$ 20 giây đều tính 20 giây.
> Đây là lựa chọn của khóa luận: lời hứa bị sửa theo chiều nào cũng là một lần sửa. Fielbaum và Alonso-Mora chỉ tính phần
> bất lợi. Khóa luận không chứng minh được $c \ge 0$ cho bộ sinh chỉ chèn thêm, nên định nghĩa giữ trị tuyệt đối. Trên các
> lần chạy, việc tính cả chiều sớm gần như không đổi kết quả: ở tập kiểm tra chính, mọi lần điều phối kéo giờ trả sớm hơn
> $e$ chỉ sớm 1 mili giây (chưa rõ nguyên nhân).

(Nếu tác giả có lý do khác cho chiều sớm, thay câu thứ hai bằng lý do đó.)

**B3. Bàn về khóa giờ đón (sau Bảng 3.3 hoặc sau 131).**
> Khóa giờ đón chặt hơn trần giờ trả nhiều: giờ đón của khách đã xác nhận phải trùng đúng giờ đón khi giữ nguyên kế
> hoạch, nên một yêu cầu mới chỉ chèn được vào trước điểm đón của khách đang chờ nếu không làm giờ đón đó thay đổi. Khóa
> này có ở cả điều phối không trần lẫn luật C, nên chênh lệch giữa hai cấu hình không đến từ khóa.

Thêm một câu nói vì sao giờ đón có trần 0 còn giờ trả có trần dương.

**B4. Tiêu chí 3 của bộ chọn (Bảng 3.3 dòng 276-277; 424-428).** Trong bảng:
> Tiêu chí 3 — Ít sửa lời hứa nhất: trước hết so mức dùng trần lớn nhất trên các khách, $\max_r (L_r + |c_r|)/B$; nếu
> hòa, so tổng phần sửa lời hứa do điều phối, lần lượt theo từng chiều (chỉ có khi cấu hình có trần cứng).

(Kiểm lại công thức với mã bộ chọn.) Thay 424-428 bằng:
> Trong cài đặt, phần đầu của tiêu chí 3 không phân biệt được phương án nào, vì các chiều có trần 0 của khóa luôn được
> tính là đã dùng hết trần. Vì vậy tiêu chí 3 thực chất so tổng phần sửa lời hứa do điều phối, ở cả điều phối không trần
> lẫn luật C. Nói cách khác, điều phối không trần cũng ưu tiên ít sửa lời hứa, sau khi đã nhận nhiều yêu cầu nhất (số
> liệu kiểm ở mục~\ref{muc:c4-hople}).

Thêm một câu "vì sao": vì sao đặt nhận yêu cầu trước ổn định.

**B5. Công bằng với Schulz và Pfeiffer (sau 396).**
> Schulz và Pfeiffer dùng thời gian đi cố định và độ chùng mặc định 900 giây, nên trong bài của họ, tắc đường không thể
> đẩy giờ trả vượt hạn chót. Ở khóa luận, với độ chùng 30-60 giây và hệ số tắc đường đổi theo khung 15 phút, riêng tắc
> đường đã có thể làm luật hạn chót loại phương án giữ nguyên (xem~\eqref{eq:dongnhat}). Vì vậy số lần luật hạn chót bị
> ép ở Chương~\ref{chuong:thucnghiem} nói về hạn chót chặt trong môi trường tắc đường thay đổi, không nói về phương pháp
> của họ. [Lý do chọn 30-60 giây: …]

**B6. Luật phục hồi (105-110, 436-440).**
- Viết rõ: "Luật thứ hai mở rộng luật thứ nhất: ...".
- Định nghĩa "không tệ hơn": "phương án $\pi$ không tệ hơn phương án giữ nguyên ở một lỗi nếu [mức vượt của $\pi$ ở lỗi đó
  không lớn hơn mức vượt của phương án giữ nguyên]". Kiểm với mã HVA.
- Định nghĩa "khóa theo giai đoạn".
- Thêm câu: "Hai luật phục hồi là chi tiết cài đặt để so các luật trên cùng một bộ điều phối, không phải đóng góp của khóa
  luận."
- Thống nhất định nghĩa "xe bị ép" giữa dòng 105 và 323. Sửa chú thích ở dòng 105-106, vì hiện nó trộn điều kiện bị ép với
  điều kiện được phục hồi.

**B7. Mục kiểm tra kết quả (641-655).**
- Đổi tên mục thứ hai:
  > \item \textbf{Kiểm tính nhất quán của sổ:} ở cả 382.006 lần cập nhật giờ trả của 185 lần chạy, $|x|$, $|c|$, $|z|$
  > tính lại từ ba mốc $v$, $e$, $p$ ghi trong sổ khớp đúng các trường độ lớn trong sổ. Phép kiểm này cho biết sổ được
  > ghi nhất quán; nó không kiểm $e$ có được tính đúng hay không.
- Mục thứ ba: "một chương trình viết riêng (độc lập về mã, nhưng dùng cùng đặc tả chỉ số) ...".
- Mục thứ nhất: chạy lại `dotnet test` trên đúng bản mã của bộ chạy đã lưu và ghi số mới, kèm mã phiên bản. Nếu không chạy
  lại thì bỏ mục này.
- Mục tái lập (652-654): nói đã kiểm tương đương hay chưa. "Phải cho đúng kết quả cũ" là quy tắc, chưa phải kết quả.
- Nên thêm một khách thật được lần tay từ bản ghi, để trả lời câu hỏi 5.2.11.

**B8. Hình 3.1 (64-77).**
- Ô "Công bố lời hứa (lớp dự báo)" làm người đọc tưởng lớp dự báo nằm trong vòng lặp. Giả mã ở Bảng 3.1 không có lớp này,
  và chú thích nói nó được tính sau. Tách thành một ô nét đứt bên ngoài vòng: "Lớp dự báo (tính lại sau, trên bản ghi)".
- Thứ tự ô khác giả mã: hình tính ba mốc trước rồi mới loại theo ràng buộc, còn giả mã kiểm ràng buộc dịch vụ trước (dòng
  7) rồi mới tính ba mốc (dòng 8). Sửa hình cho khớp: sinh phương án → loại theo ràng buộc dịch vụ → tính ba mốc → loại
  theo khóa và trần → bộ giải → công bố → ghi sổ.

**B9. Mười chiều cam kết (315-317).**
> Phép kiểm dừng ở khách vượt trần gặp đầu tiên, nên mỗi bản ghi chỉ nêu một lý do loại phương án. Ngoài giờ trả, cài
> đặt còn theo dõi riêng chín thuộc tính khác của lời hứa (gọi chung là mười chiều cam kết, liệt kê ở Phụ lục C). Trong
> các cấu hình được dùng, giờ trả có trần dương; đổi xe, đổi điểm đón và đổi điểm trả có trần 0; [các chiều còn lại …].

**B10. Dòng 127-129 và dòng 96.**
> Bộ sinh phương án chỉ chèn thêm đặt điểm đón và điểm trả của yêu cầu mới vào các cặp vị trí trong kế hoạch của xe, và
> không bỏ hay đổi thứ tự điểm cũ nào; vì vậy khách đã nhận không bị chuyển sang xe khác.

Đổi chú thích dòng 4 của Bảng 3.1, "luôn dựng trước", thành "dựng trước tiên".

**B11. Dòng 240.**
> Như vậy, khi xe không bị ép, tổng $|c|$ của mỗi khách tính đến hết chuyến không vượt $B$.

**B12. Thời gian chạy (631-633).** Thêm cấu hình máy, có tính FleetPy hay không, và câu "không dùng các số này để so chi
phí tính toán giữa các luật".

### Mức C — văn phong

**C1. Mở chương theo kiểu DACN (chèn trước dòng 17).**
> Ý chính của chương là chỉ giới hạn phần giờ trả bị dời do chính quyết định của bộ điều phối, không giới hạn phần thay
> đổi do đường đông hay xe chạy nhanh, chậm hơn dự kiến. Để tách hai phần này, ở mỗi lượt quyết định hệ thống tính hai
> giờ trả cho mỗi khách: giờ trả nếu xe giữ nguyên kế hoạch cũ, và giờ trả nếu chọn phương án mới. Hiệu của hai giờ này
> là phần dời do điều phối. Luật C cộng phần này qua cả chuyến và loại phương án làm tổng vượt một trần. Phần thay đổi
> theo nhịp tắc đường quen thuộc trong ngày được đưa trước vào lời hứa đầu bằng dự báo lịch sử; phần chưa giải thích được
> ghi lại trong sổ theo từng khách.

**C2. Chuyển số đo sang Chương 4 hoặc Phụ lục C:** 427-428 (3.503/3.506/3.504), 642 (1.025), 644-645 (chi tiết 185/170/15
đưa vào Phụ lục C), 647 (13 hạng mục). Giữ 469-470 (định nghĩa kịch bản nào có dự báo), 342-343 (một câu kiểm chứng) và
508 (giới hạn đã biết, nhưng viết lại theo C8).

**C3. Thuật ngữ tiếng Anh:** giữ decision epoch, insertion, lexicographic order; đưa mười cụm còn lại vào Danh mục ký hiệu
và chữ viết tắt.

**C4. Thay cụm nặng:**
- 341: "dữ liệu chỉ khớp với nó" → "số liệu chạy thử chỉ khớp với nó".
- 219: "vế này không có tác dụng đo được" → "việc tính cả chiều sớm gần như không đổi kết quả".
- 426: "1.000.000 phần triệu" → "mức dùng 100%".
- 431: "tệp chính sách" → "cấu hình".
- 432: "hiệu giữa chúng là phép so của việc thêm trần khi giữ nguyên bộ chọn" → "vì vậy chênh lệch giữa hai cấu hình là
  phần đi kèm việc thêm trần, khi bộ chọn giữ nguyên".
- 378: "chính sách chi phí cuốn chiếu mặc định" → giải thích bằng một câu, hoặc "bộ chọn mặc định chỉ xét chi phí tuyến"
  (kiểm lại cho đúng).
- 397, 632, 653: "bộ chạy cũ" → "phiên bản bộ chạy trước khi có luật phục hồi".
- 625: "hạt giống cố định 7" → "hạt giống ngẫu nhiên cố định".
- 624: "giới hạn khối lượng" → "giới hạn số bước tính".
- "bản ghi chặn" → "bản ghi lý do loại".

**C5. Thống nhất thuật ngữ:**
- "cửa sổ đón" thay cho "khoảng giờ đón" (34);
- "ràng buộc dịch vụ" thay cho "ràng buộc vật lý" (347);
- "bảng thời gian đi" thay cho "bảng giờ đi";
- "khách đã nhận được gán cho xe" thay cho "khách đã nhận trên xe";
- "Tên trong khóa luận" thay cho "Tên trong bài" (371);
- "bốn cấu hình khác" thay cho "bốn luật khác" (359), vì điều phối không trần và ghép tự do không phải luật lời hứa;
- ô "Khóa" của hàng điều phối không trần (374): "Khóa xe, điểm đón, điểm trả và giờ đón";
- 147: "Ba hiệu sau được tính bằng giây (sổ lưu tới mili giây)";
- 531-532: ghi rõ "trễ hơn $p_0$ quá 60 giây" (hiện có thể hiểu là $p_0$ hay $D_0$).

**C6. Chuyển Bảng 3.3 lên 3.1.1,** kèm một đoạn ngắn phân biệt ràng buộc cứng với thứ tự tiêu chí, như DACN 3.2.2.

**C7. Đưa LOCKS, B1, C1 (396-398) vào chú thích chân trang hoặc Phụ lục C.** Trong văn bản chỉ dùng tên tiếng Việt.

**C8. Tách câu dài.** Dòng 505-510:
> Trong thực nghiệm, lời hứa theo dự báo được tính lại trên các lần chạy đã ghi; cách làm này gọi là phát lại. Quyết
> định điều phối giữ nguyên, chỉ lời hứa thay đổi. Ký hiệu $D_0$ là lời hứa đầu có dự báo; phần lời hứa dài thêm
> $D_0 - p_0$ là cái giá của dự báo. Cách làm này còn một chỗ chưa khớp: phép kiểm khả thi vẫn dùng giờ không dự báo.
> Vì vậy, dưới luật C với trần 30 giây, 34 trong 1.471 khách được phục vụ ở 21 kịch bản có dự báo được hiển thị giờ đón
> muộn hơn giờ đón muộn nhất của họ. Chỗ này cần sửa trước khi đưa lớp dự báo vào bộ điều phối; mục~\ref{muc:c4-dubao}
> trình bày một phép thử theo hướng đó.

Dòng 431-433:
> Điều phối không trần và luật C dùng cùng cấu hình và cùng bộ chọn, chỉ khác ở trần giờ trả. Vì vậy, chênh lệch giữa
> hai cấu hình ở Chương~\ref{chuong:thucnghiem} là phần đi kèm việc thêm trần khi bộ chọn giữ nguyên. Khóa luận chưa kiểm
> chênh lệch này có còn khi bộ chọn ưu tiên chi phí hay không (mục~\ref{muc:c4-vaitro}).

**C9. Thêm câu về ngày nguồn (sau 470):**
> Việc bỏ ngày 15/11 là lựa chọn của khóa luận vì ngày đó có tuyết; một hệ thống thật cần một quy tắc tự động để nhận ra
> ngày bất thường.

**C10. Dòng 509:** "phải xử lý trước khi triển khai" → "cần sửa trước khi đưa lớp dự báo vào bộ điều phối" (đã gộp vào
C8).

---

## 8. Tóm tắt cho tác giả

Chương 3 đúng hướng và trung thực. Phần cốt lõi (ba mốc, luật C, đẳng thức nối ba luật) đủ rõ để người khác làm lại.
Trước khi nộp, cần sửa bốn việc:
1. Đưa Fielbaum và Alonso-Mora vào, nói rõ kế thừa gì và khác gì.
2. Làm chặt Nhận xét 3.1: hai giả thiết ẩn, phép quy nạp, và mâu thuẫn về lúc cập nhật $L_r$.
3. Viết lại phần so với Hörl–Zwick bằng phần được phép dời $c$, kèm ràng buộc cứng của họ.
4. Bổ sung mô hình chọn và vòng đời của khách vào phát biểu bài toán.

Về văn phong, chỉ cần làm theo DACN ở ba điểm: mở chương bằng ý chính, mở mỗi mục bằng câu "vì sao", và để số đo ở
Chương 4.
