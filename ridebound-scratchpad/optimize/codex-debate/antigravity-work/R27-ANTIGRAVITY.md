# BÁO CÁO PHẢN BIỆN ANTIGRAVITY VÒNG 27 (R27)
**Các chương thẩm định:** Chương 2 (`06-chuong2-v4.tex`), Chương 3 (`07-chuong3-v3.tex`), Chương 4 Phần A (`08-chuong4-phanA.tex`) và Chương 4 Phần B (`09-chuong4-phanB-v7.tex`).  
**Tài liệu đối chiếu:** `GLOSSARY-VI.md`, `STYLE-GUIDE-VI.md`, `WRITING-BRIEF.md`.  
**Phương thức thực hiện:** Kết hợp hai tác tử chuyên trách: (1) Người đọc ngoài ngành (sinh viên năm cuối ngành kỹ thuật khác), (2) Giảng viên phản biện (Khoa CNTT, UET - ĐHQGHN).

---

# PHẦN 1: BÁO CÁO CỦA NGƯỜI ĐỌC NGOÀI NGÀNH

## 1. Trả lời hai câu hỏi trọng tâm của Brief
- **Câu hỏi Chương 2 (Khác biệt cốt lõi của Luật C so với công trình trước):**  
  Khác với Schulz & Pfeiffer (2026) cố định hạn chót một chiều từ lời hứa đầu khiến tắc đường dễ làm vỡ hạn, và khác với Hörl & Zwick (2022) nới hạn theo thời gian cập nhật nhưng chỉ phạt phần trễ trong hàm mục tiêu, Luật C đo riêng phần giờ trả bị dời do thuật toán điều phối ghép thêm khách (so với khi xe giữ nguyên lộ trình cũ), áp một trần cố định không tự nới khi đường tắc và cộng dồn độ dời này qua cả hành trình cho từng hành khách.
- **Câu hỏi Chương 4 Mục 4.8 (Vì sao cần Luật C nếu đệm 30 giây cho số khách đúng giờ tương đương?):**  
  Hệ thống cần Luật C vì cách đệm 30 giây chỉ là kéo dài lời hứa trên giấy tờ (làm lời hứa dài thêm gấp 5 lần và khiến 44 khách tới sớm hơn 1 phút) mà không hề ngăn được bộ điều phối làm dời giờ trả của khách (vẫn để 174 khách bị dời giờ, có người bị dời tới 590,1 giây), trong khi Luật C can thiệp trực tiếp vào thuật toán để bảo đảm không hành khách nào bị dời giờ trả quá 30 giây do ghép chuyến.

## 2. Năm điểm dễ bị "lạc" và khó nắm bắt nhất đối với người ngoài ngành
1. **Ý nghĩa của ba mốc giờ trả ($v, e, p$) và phần dời do điều phối ($c = p - e$):** Dễ nhầm $e$ là giờ thực tế xe sẽ đến ngoài đường, hoặc nhầm $c$ là số giây khách bị muộn ngoài đời. Cần nhấn mạnh $e$ chỉ là giờ ước tính nội bộ của mô hình máy tính nếu xe đi tiếp lộ trình cũ với tốc độ hiện tại, và $c$ là độ dời trên máy tính tại cùng một thời điểm giữa hai phương án.
2. **Sự tách biệt giữa "nghĩa vụ của luật" (phá lời hứa / bị ép) và "tỉ lệ đúng giờ ngoài đời":** Luật hạn chót bị "phá lời hứa" 14,5% và "bị ép" 41,3% còn Luật C là 0%, nhưng số khách trễ thực tế ngoài đời của hai luật lại gần như y hệt nhau (74 so với 76 khách). Nguyên nhân là luật hạn chót cam kết giờ tuyệt đối (đường tắc là vỡ hứa), còn Luật C chỉ cam kết không dời quá 30 giây do ghép khách.
3. **Cơ chế "phát lại" (replay) lời hứa theo dự báo và cách đệm:** Cần giải thích rõ xe đã chạy xong trong mô phỏng và lưu lộ trình vào tệp nhật ký; việc "phát lại" chỉ là lấy tệp đó ra tính lại con số giờ hiển thị trên ứng dụng ảo để thống kê, hoàn toàn không làm xe chạy khác đi.
4. **Vế "cộng dồn" ($\sum |c| \le B$) hầu như không có tác dụng trong thực nghiệm:** Trong toàn bộ 98 lần chạy cũ, không có lần nào việc cộng dồn là lý do loại phương án (mọi phương án bị chặn đều vượt 30 giây ngay trong một lần dời duy nhất); chỉ khi nới trần lên 120 giây mới xuất hiện 3 bản ghi hiếm hoi. Người đọc ngoài ngành sẽ băn khoăn tại sao phải thiết kế công thức cộng dồn phức tạp nếu luật chỉ hoạt động như một cái trần chặn từng bước riêng lẻ.
5. **Quy mô mẫu và tập kịch bản thay đổi liên tục:** Dữ liệu chuyển đổi giữa 4 tập kịch bản khác nhau (Tập chính 34 kịch bản — 3.672 yêu cầu; Tập sáng 8 kịch bản — 864 yêu cầu; Tập cố định 16 kịch bản — 1.728 yêu cầu; Chiều tuyết 8 kịch bản — 601 khách), lúc gộp theo khách, lúc lấy trung bình theo kịch bản.

## 3. Rà soát chi tiết từng câu và đề xuất viết lại (giữ nguyên nghĩa và số liệu)

### Chương 2: `06-chuong2-v4.tex`
- **Dòng 26–28:**
  - *Nguyên văn:* "Đây là một dạng của bài toán đưa đón theo yêu cầu (Dial-a-Ride Problem, DARP): thiết kế các tuyến xe chi phí nhỏ nhất để chở khách chung theo nhu cầu, trong khi giữ các yêu cầu về mức dịch vụ~\cite{molenbruch2017}."
  - *Lý do:* Cụm "trong khi giữ các yêu cầu về mức dịch vụ" nghe gượng gạo, mang hơi hướng dịch máy.
  - *Đề xuất:* "Đây là một dạng của bài toán đưa đón theo yêu cầu (Dial-a-Ride Problem, DARP): thiết kế các tuyến xe có chi phí thấp nhất để chở chung hành khách theo nhu cầu, đồng thời bảo đảm các tiêu chuẩn về chất lượng dịch vụ~\cite{molenbruch2017}."
- **Dòng 32–37:**
  - *Nguyên văn:* "Bước đầu nối hai yêu cầu, hay một yêu cầu với một xe, khi chúng chở chung được mà vẫn thỏa các ràng buộc dịch vụ; từ đó dựng đồ thị yêu cầu--chuyến--xe (request--trip--vehicle graph), trong đó một chuyến là một nhóm yêu cầu mà một xe chở được. Một nhóm chỉ cần kiểm khi mọi nhóm con bớt đi một yêu cầu đều khả thi với cùng xe, nên các nhóm được dựng dần theo kích thước."
  - *Lý do:* Câu đầu dài (43 từ). Cụm "mọi nhóm con bớt đi một yêu cầu đều khả thi với cùng xe" trừu tượng đối với người ngoài ngành CNTT/toán rời rạc.
  - *Đề xuất:* "Bước đầu tiên là ghép đôi hai yêu cầu, hoặc ghép một yêu cầu với một xe, nếu xe có thể chở chung mà vẫn thỏa mãn các ràng buộc dịch vụ. Từ các liên kết này, hệ thống dựng đồ thị yêu cầu--chuyến--xe (request--trip--vehicle graph), trong đó mỗi chuyến là một nhóm yêu cầu mà một xe chở được. Thuật toán mở rộng dần kích thước nhóm: một nhóm lớn chỉ cần kiểm tra tính khả thi nếu mọi nhóm con nhỏ hơn của nó (bớt đi một yêu cầu) đều đã khả thi với xe đó."
- **Dòng 56–59:**
  - *Nguyên văn:* "Tuy vậy, đó là một số hạng mềm, cộng chung trên mọi khách và đo so với chuyến đi thẳng, không so với giờ đã báo; một khách vì thế có thể bị dời giờ trả nhiều lần, miễn là mỗi lần tổng chi phí nhỏ hơn."
  - *Lý do:* Thuật ngữ "số hạng mềm" chưa được giải thích; câu ghép nhiều vế phụ.
  - *Đề xuất:* "Tuy nhiên, đây chỉ là một đại lượng phạt mềm (cho phép vi phạm nhưng tính thêm chi phí), được cộng dồn trên toàn bộ hành khách và đo so với chuyến đi thẳng chứ không đo so với giờ đã hẹn trước. Do đó, một hành khách có thể bị dời giờ trả nhiều lần, miễn là mỗi lần điều chỉnh đều làm tổng chi phí của cả hệ thống giảm xuống."
- **Dòng 131–136:**
  - *Nguyên văn:* "Thước đo của Fielbaum và Alonso-Mora so giá trị cuối với giá trị báo ban đầu, nên một khách bị dời muộn 5 phút rồi được kéo về giờ cũ có hiệu bằng 0, dù đã nhận hai lần thay đổi; số lần tăng được đếm nhưng không mang độ lớn. Khóa luận kế thừa ý tách phần thay đổi do quyết định của hãng xe và kiểm soát nó trước khi quyết định, nhưng đo từng lần sửa so với giờ trả khi giữ nguyên kế hoạch và cộng độ lớn qua cả chuyến (mục~\ref{muc:bamoc})."
  - *Lý do:* Hai câu dài liên tiếp (> 45 từ), dồn nén nhiều ý tương phản.
  - *Đề xuất:* "Thước đo của Fielbaum và Alonso-Mora chỉ so sánh giá trị cuối cùng với giờ báo ban đầu. Vì vậy, nếu một khách bị dời muộn 5 phút rồi sau đó được kéo về giờ cũ thì độ lệch bằng 0, dù thực tế hành khách đã trải qua hai lần thay đổi giờ hẹn; cách làm này có đếm số lần tăng nhưng không ghi nhận độ lớn của từng lần. Khóa luận kế thừa ý tưởng tách riêng phần thay đổi do hãng xe và chủ động kiểm soát nó trước khi ra quyết định. Điểm khác biệt là khóa luận đo từng lần điều chỉnh so với giờ trả khi giữ nguyên lộ trình, đồng thời cộng dồn độ lớn của các lần đổi này trong suốt cả chuyến đi (mục~\ref{muc:bamoc})."
- **Dòng 206–211:**
  - *Nguyên văn:* "Luật C dùng lại mốc giờ trả cập nhật của Hörl và Zwick nhưng giới hạn một đại lượng khác: phần dời do điều phối so với mốc đó, cộng độ lớn qua cả chuyến, với cùng một trần cho mọi khách đã xác nhận, không nới theo tắc đường, và ghi vào sổ theo từng khách (mục~\ref{muc:luatc})."
  - *Lý do:* Câu dài 52 từ, liệt kê 5 đặc điểm phân biệt khiến người đọc khó nắm ý.
  - *Đề xuất:* "Luật C kế thừa mốc giờ trả cập nhật của Hörl và Zwick nhưng giới hạn một đại lượng khác. Đại lượng này là phần giờ trả bị dời do điều phối so với mốc cập nhật, được cộng dồn độ lớn trong suốt chuyến đi. Luật áp dụng cùng một mức trần cho mọi khách đã xác nhận, không tự động nới lỏng khi đường tắc, và ghi nhận chi tiết vào sổ theo dõi của từng người (mục~\ref{muc:luatc})."

### Chương 3: `07-chuong3-v3.tex`
- **Dòng 135–136 (Bảng 3.2):**
  - *Nguyên văn:* "Mức dùng trần lớn nhất nhỏ nhất; nếu hòa, tổng phần dời do điều phối nhỏ nhất, so lần lượt từng chiều cam kết (khi có chiều mang trần)"
  - *Lý do:* Cụm "Mức dùng trần lớn nhất nhỏ nhất" (min-max) rất dễ gây lú lẫn.
  - *Đề xuất:* "Ưu tiên phương án có mức sử dụng trần tối đa là nhỏ nhất; nếu hòa nhau, ưu tiên phương án có tổng độ dời do điều phối nhỏ nhất, so sánh lần lượt theo từng chiều cam kết (nếu chiều đó có đặt trần)."
- **Dòng 227–230:**
  - *Nguyên văn:* "Phần nới ở dòng 6 giúp xe không kẹt vì tắc đường; mỗi lần vượt, và mỗi lần khách thực tế lên xe muộn hơn giờ đón muộn nhất, được ghi lại thay vì làm dừng lần chạy, nên cửa sổ đón là điều kiện kiểm phương án, không phải bảo đảm đúng hạn."
  - *Lý do:* Cụm "điều kiện kiểm phương án, không phải bảo đảm đúng hạn" trừu tượng.
  - *Đề xuất:* "Quy định nới lỏng ở dòng 6 giúp xe không bị bế tắc khi đường tắc. Thay vì dừng lần chạy mô phỏng, hệ thống chỉ ghi nhận lại các lần vượt thời gian và các lần khách lên xe muộn hơn giờ hẹn tối đa. Do đó, cửa sổ đón chỉ đóng vai trò là điều kiện để sàng lọc phương án lúc lập kế hoạch, chứ không phải là cam kết chắc chắn xe sẽ đến đúng giờ ngoài thực tế."
- **Dòng 287–291:**
  - *Nguyên văn:* "Bộ sinh chỉ chèn thêm không bảo đảm $c \ge 0$, nhưng ở bốn cấu hình đã kiểm của tập kiểm tra chính (điều phối không trần, luật C trần 30 và 120 giây, luật hạn chót 30 giây; 136 lần chạy), mỗi lần kéo giờ trả sớm hơn $e$ chỉ sớm 1 mili giây; chiều sớm chưa cho thấy tác dụng đáng kể."
  - *Lý do:* Chèn nhiều thông tin ngoặc đơn làm đứt đoạn mạch câu (56 từ).
  - *Đề xuất:* "Bộ sinh chỉ chèn thêm không đảm bảo $c \ge 0$. Tuy nhiên, khi kiểm tra 4 cấu hình trên tập kiểm tra chính (gồm điều phối không trần, luật C trần 30 và 120 giây, luật hạn chót 30 giây qua 136 lần chạy), mỗi lần xe kéo giờ trả sớm hơn $e$ thì mức sớm hơn chỉ đúng 1 mili giây. Vì vậy, việc can thiệp ở chiều đón/trả sớm chưa đem lại tác dụng rõ rệt."
- **Dòng 507–514:**
  - *Nguyên văn:* "Theo tốc độ lúc công bố, xe cần thêm $p - t$ giây; trong khung chậm hơn khung hiện tại $g$ lần, mỗi giây đồng hồ chỉ đi được $1/g$ giây quãng đường đó. Mức tắc đường lúc này đã có trong thời gian đi đang dùng, nên $g = 1$ ở khung hiện tại; các ngày khác chỉ cho biết khung sau chậm hay nhanh hơn bao nhiêu lần."
  - *Lý do:* "Mỗi giây đồng hồ chỉ đi được $1/g$ giây quãng đường đó" gây bối rối về thứ nguyên vật lý.
  - *Đề xuất:* "Theo tốc độ tại thời điểm công bố, xe cần thêm $p - t$ giây di chuyển. Khi chuyển sang khung giờ đường đông hơn gấp $g$ lần, mỗi giây trôi qua trên đồng hồ thực tế xe chỉ đi được lượng quãng đường tương đương với $1/g$ giây chạy ở tốc độ ban đầu. Vì mức độ tắc đường hiện tại đã được phản ánh trong thời gian đi đang dùng nên ta đặt $g = 1$ cho khung hiện tại; dữ liệu từ các ngày lịch sử chỉ dùng để tính xem các khung giờ tiếp theo sẽ chạy nhanh hay chậm hơn bao nhiêu lần."

### Chương 4: `08-chuong4-phanA.tex` và `09-chuong4-phanB-v7.tex`
- **Dòng 265–273 (Chương 4A):**
  - *Nguyên văn:* "Với 2.207 khách chung, luật C chờ lâu hơn 0,5 giây và ngồi xe ngắn hơn 10,5 giây, nhưng đây là tập khách hình thành sau khi áp luật, không phải một phép so ngẫu nhiên."
  - *Lý do:* Thuật ngữ thống kê ("tập khách hình thành sau khi áp luật") cần diễn giải trực quan hơn.
  - *Đề xuất:* "Xét riêng 2.207 khách chung này, hành khách dùng luật C phải chờ xe lâu hơn 0,5 giây nhưng thời gian ngồi trên xe ngắn hơn 10,5 giây. Tuy nhiên, nhóm khách này được hình thành sau khi thuật toán đã can thiệp nhận/từ chối chuyến chứ không phải là mẫu chọn ngẫu nhiên độc lập, nên con số chênh lệch chỉ mang tính mô tả tham khảo."
- **Dòng 477–483 (Chương 4A):**
  - *Nguyên văn:* "Vì bộ kiểm dừng ở lỗi gặp trước và quỹ đạo sẽ đổi khi trần đổi, điều đó không có nghĩa 59 yêu cầu sẽ được phục vụ; mục~\ref{muc:c4-chontran} cho kết quả chạy thật ở mức này. Các phân loại trong mục này dựa vào bản ghi dừng ở lỗi gặp trước, nên không chứng minh một yêu cầu bị từ chối chỉ vì trần."
  - *Lý do:* Cơ chế "dừng ở lỗi gặp trước" (short-circuiting) là khái niệm lập trình cần được làm rõ hệ quả đối với số liệu thống kê.
  - *Đề xuất:* "Do thuật toán kiểm tra sẽ dừng ngay khi phát hiện lỗi vi phạm đầu tiên (thay vì liệt kê toàn bộ các lỗi), đồng thời lộ trình của xe sẽ thay đổi khi mức trần thay đổi, nên con số này không đồng nghĩa với việc 59 yêu cầu trên chắc chắn sẽ được phục vụ; kết quả mô phỏng thực tế ở mức trần này được trình bày ở mục~\ref{muc:c4-chontran}. Các phân loại ở đây phụ thuộc vào cơ chế dừng sớm khi gặp lỗi đầu tiên, do đó chưa đủ để khẳng định một yêu cầu bị từ chối hoàn toàn chỉ vì chạm trần thời gian."
- **Dòng 69–73 (Chương 4B):**
  - *Nguyên văn:* "Phép thử đổi thứ tự ưu tiên của bộ chọn trên 34 kịch bản chính chưa được chạy; bằng chứng hiện có là phép sàng lọc trên trạng thái cố định ở trên, vốn không cho biết kết quả phục vụ và đúng giờ trên quỹ đạo. Khóa luận vì vậy chưa tách được phần của trần và phần của bộ chọn trong độ tin cậy đã đo. Chương kết luận đặt phép thử này lên đầu các hướng phát triển."
  - *Lý do:* "Trên quỹ đạo" (on trajectory) là thuật ngữ hẹp, cần nói rõ là chạy động theo thời gian thực.
  - *Đề xuất:* "Thí nghiệm thay đổi thứ tự ưu tiên của bộ chọn trên 34 kịch bản chính hiện chưa được thực hiện; bằng chứng duy nhất hiện có mới là phép sàng lọc tĩnh trên các trạng thái đã ghi nhận, vốn không phản ánh được kết quả phục vụ và độ đúng giờ khi xe chạy động theo thời gian thực. Vì vậy, khóa luận chưa thể tách bạch phần đóng góp của mức trần với phần đóng góp của bộ chọn trong kết quả độ tin cậy. Đề tài đặt phép thử này làm ưu tiên hàng đầu trong các hướng phát triển tiếp theo."
- **Dòng 218–221 (Chương 4B):**
  - *Nguyên văn:* "Khi có dự báo, cộng thêm 30 giây vào mọi lời hứa của điều phối không trần cũng cho 2.328 lượt không trễ quá một phút trên 3.672 yêu cầu, bằng luật C trần 30 giây. Ở ngưỡng hai phút, cách đệm cho 2.366 lượt, so với 2.338 của luật C. Đổi lại, lời hứa dài thêm trung bình 37,2 giây thay vì 7,4 giây."
  - *Lý do:* So sánh cốt lõi nhưng câu mở đầu quá dài, dồn dập các cặp số.
  - *Đề xuất:* "Khi đã có dự báo, nếu ta cộng thêm 30 giây vào mọi lời hứa của cấu hình không trần thì cũng đạt được 2.328 lượt không trễ quá một phút (trên 3.672 yêu cầu), ngang bằng với kết quả của luật C trần 30 giây. Thậm chí ở ngưỡng hai phút, cách đệm này còn đạt 2.366 lượt kịp giờ, vượt qua mức 2.338 lượt của luật C. Tuy nhiên, cái giá phải trả là lời hứa bị kéo dài thêm trung bình 37,2 giây thay vì chỉ 7,4 giây như ở luật C."

---

# PHẦN 2: BÁO CÁO CỦA GIẢNG VIÊN CHẤM KHÓA LUẬN (KHOA CNTT, UET - ĐHQGHN)

## 1. Đánh giá tính chặt chẽ học thuật, ranh giới đóng góp và khả năng tái lập
- **Chương 2 (Cơ sở lý thuyết):**
  - Khảo cứu công trình liên quan rất đầy đủ và trung thực, xác định chính xác ranh giới đóng góp (không nhận thừa các kỹ thuật đã có như DARP, RTV, chèn động, ETA hay lý thuyết độ bất ổn).
  - Bảng 2.1 và 2.2 được xây dựng công phu, định vị sắc bén Luật C so với các mô hình trước.
- **Chương 3 (Phương pháp):**
  - Khung phương pháp rõ ràng, biểu đồ giao thức JSON lines và giả mã mạch lạc, có thể tái lập ở mức trừu tượng cao.
  - **Bốn điểm nghẽn/khiếm khuyết mô hình hóa trong Chương 3:**
    1. *Tiêu chí 3 của Bộ chọn bị vô hiệu hóa một nửa:* Do các phương án đổi xe/đón/trả mang trần bằng 0, mức dùng trần tối đa luôn đạt 100% ở mọi lượt (`07-chuong3-v3.tex:346-350`), khiến vế "tối thiểu hóa mức dùng trần lớn nhất" hoàn toàn mất tác dụng lọc, chỉ còn vế sau hoạt động.
    2. *Xử lý dấu của $c$ không đồng nhất:* Luật C kiểm tra độ lớn $|c|$, trong khi công thức Sổ cái (3.5) lại dùng tổng đại số có dấu ($q = \sum c_j$), tạo ra độ vênh giữa cơ chế kiểm soát trực tuyến và phân tích hậu nghiệm.
    3. *Lời hứa theo dự báo $D$ mâu thuẫn với Cửa sổ đón:* Việc tính $D$ ngoài luồng (replay) dẫn đến 34 khách nhận giờ đón hiển thị muộn hơn cả giờ đón muộn nhất cho phép của hệ thống (`07-chuong3-v3.tex:554-556`).
    4. *Nhận xét 3.1 phụ thuộc vào Giả thiết lý tưởng (N):* Nhận xét khẳng định Luật C không bao giờ loại phương án giữ nguyên kế hoạch chỉ bảo đảm khi dwell time = 0 và thế giới không có trễ thực thi.
- **Chương 4 (Thực nghiệm):**
  - Thể hiện tính kỷ luật khoa học cao: không che giấu kết quả âm tính, thừa nhận thẳng thắn các giới hạn. Thuật ngữ giữa các chương cơ bản nhất quán.

## 2. Phát hiện các lỗi học thuật, ngụy biện nhân quả và lỗi văn bản
1. **Tuyên bố tuyệt đối hóa:** Câu "Điều này đúng theo cấu tạo: phương án giữ nguyên kế hoạch... luôn qua luật C" (`08-chuong4-phanA.tex:308-310`) là vượt quá bằng chứng thực nghiệm vì nó phụ thuộc vào Giả thiết (N) trên môi trường mô phỏng.
2. **Ngụy biện bù trừ nhân quả số học:** Viết đẳng thức $+31 = -96 - (-127)$ (`08-chuong4-phanA.tex:265-266`) tạo cảm giác như có sự bù trừ nhân quả cơ học trực tiếp giữa số khách mất đi và số khách hết trễ, dù hai cấu hình phục vụ hai tập khách khác nhau.
3. **Thiên vị chọn mẫu (Selection Bias):**
   - Bảng 4.5: So sánh số khách đi chung giữa U (555) và C-30 (313) mà không tách bạch phần giảm do Luật C từ chối bớt khách (làm giảm mật độ mạng lưới).
   - Bảng 4.7: So sánh trễ tối đa (U 11 phút vs C-30 3,87 phút) có rủi ro chọn mẫu thuận lợi: khách trễ 11 phút ở U có thể chính là khách mà C-30 đã từ chối nhận từ đầu. Cần phân tích trên tập 2.207 khách chung.
   - Bảng 4.14: So sánh trung bình % giảm chi phí giữa U và C-30 trên hai tập trạng thái đã phân kỳ quỹ đạo.
4. **Kiểm tra từ cấm và lỗi soạn thảo bảng:**
   - Hoàn toàn **KHÔNG** vi phạm các từ cấm ("niêm phong", "đăng ký trước", "dự đoán trước", "duy nhất", "đột phá").
   - **Lỗi cần sửa ngay:** Bảng 4.5 còn hai ô ghi `\multicolumn{4}{c}{chưa đưa vào bảng}`; Bảng 4.15 còn một ô ghi `chưa đo`. Cần điền số liệu hoặc loại bỏ các dòng này trước khi nộp bản chính thức.

## 3. Mười câu hỏi phản biện cốt tử của Hội đồng chấm

1. **Khoảng cách mô phỏng - thực tế (Sim-to-Real Gap) và giả định dừng 0 giây:** Dwell time = 0 giây và hệ số tắc đường đồng nhất toàn thành phố cập nhật 15 phút một lần. Trong đô thị thực tế có độ trễ dừng xe và ùn tắc cục bộ, liệu Nhận xét 3.1 ($c = 0$ khi giữ nguyên) có còn đúng, hay xe bị trễ thực thi khiến phương án giữ nguyên vẫn vi phạm trần?  
   *(Tình trạng: CHƯA TRẢ LỜI ĐƯỢC / CÒN SƠ HỞ).*
2. **Tính kinh tế khi đánh đổi khách đi chung:** Luật C-30 làm mất 96 lượt phục vụ và giảm tới 43,6% khách đi chung (từ 555 xuống 313). Ride-pooling sống nhờ tối ưu hóa ghế trống. Liệu việc hy sinh gần một nửa khách đi chung chỉ để giảm trễ cho 127 khách có làm phá sản mô hình kinh doanh của hãng xe?  
   *(Tình trạng: ĐÃ TRẢ LỜI MỘT PHẦN qua mô hình ngưỡng hòa vốn $k > 0,756m$, nhưng chưa có số liệu thực tế về $k$ và $m$).*
3. **Sự cần thiết của Luật C so với Đệm đều 30 giây (Padding):** Tại sao phải duy trì hệ thống sổ cái và ràng buộc phức tạp, trong khi chỉ cần đệm thêm 30 giây vào lời hứa của U là đạt số khách đúng giờ tương đương (2.328 khách) mà chở thêm được 96 chuyến?  
   *(Tình trạng: ĐÃ TRẢ LỜI RẤT TỐT ở Mục 4.8: Đệm 30s kéo dài lời hứa gấp 5 lần, làm 44 khách tới sớm vô ích, và không khống chế được rủi ro đuôi — vẫn có khách bị dời 590s và trễ trên 10 phút, trong khi Luật C bảo vệ trần từng cá nhân).*
4. **Bản chất kế toán mô hình vs. Quy kết nhân quả của Sổ cái:** Phân rã sổ cái là một đồng nhất thức đại số. Làm sao chứng minh kết luận "điều phối chỉ đóng góp 1,2% số giây trễ ở C-30 so với 73,4% ở U" là quan hệ nhân quả vật lý, chứ không phải quy ước số học do cách chọn mốc $e$?  
   *(Tình trạng: ĐÃ TRẢ LỜI ĐƯỢC ở góc độ ranh giới: tác giả khẳng định ngay từ đầu đây là phân rã theo mô hình, không nhận diện nhân quả).*
5. **Vế tích lũy cả chuyến ($\sum |c| \le B$) hầu như không có tác dụng:** Bảng 4.13 cho thấy trên 140 lần chạy, chỉ có 3 bản ghi ở C-120 bị chặn do cộng dồn, còn ở C-30 là 0! Phải chăng cơ chế tích lũy cả chuyến trên thực tế vô dụng, và Luật C chỉ là trần từng bước ($|c| \le B$)?  
   *(Tình trạng: ĐÃ THỪA NHẬN SỐ LIỆU NHƯNG CHƯA CÓ ĐỐI CHỨNG THỰC NGHIỆM: chưa chạy kiểm chứng luật chỉ chặn từng bước để chứng minh có phân kỳ quỹ đạo hay không).*
6. **Thiên vị chọn mẫu khi so sánh độ trễ cực đại:** Trễ tối đa của C-30 thấp hơn U (3,87 phút vs 11 phút) có phải đơn giản là vì C-30 đã từ chối phục vụ những ca khó nhất ngay từ đầu?  
   *(Tình trạng: CHƯA TRẢ LỜI ĐẦY ĐỦ: chưa phân tích đối chứng trễ tối đa trên tập giao 2.207 khách chung).*
7. **Mâu thuẫn trong Tiêu chí 3 của Bộ chọn:** Tại sao đưa vào quy tắc "tối thiểu hóa mức dùng trần lớn nhất" khi mức dùng trần luôn bằng 100% ở mọi lượt? Tiêu chí bị vô hiệu hóa có ảnh hưởng đến bộ giải CP-SAT không?  
   *(Tình trạng: CHƯA TRẢ LỜI ĐƯỢC / LỖ HỔNG THIẾT KẾ MÔ HÌNH).*
8. **Mất đồng bộ giữa Lời hứa dự báo và Cửa sổ đón (34 khách bị đón muộn):** Tại sao hệ thống lại đưa ra lời hứa giờ đón hiển thị muộn hơn cả mốc đón muộn nhất cho phép của hệ thống?  
   *(Tình trạng: ĐÃ THỪA NHẬN LỖI KỸ THUẬT nhưng chưa sửa trong bộ điều phối).*
9. **Tính công bằng khi so sánh với Schulz & Pfeiffer (2026):** Schulz & Pfeiffer dùng độ chùng 900 giây, việc ép độ chùng xuống 30 giây trong môi trường tắc đường biến thiên mạnh có phải là phép so sánh bất công nhằm hạ thấp công trình đối chứng?  
   *(Tình trạng: ĐÃ TRẢ LỜI ĐƯỢC: tác giả nêu rõ chỉ mượn thành phần hạn chót một chiều ở cùng mức trần để kiểm tra tính tương thích với tắc đường, không đại diện cho toàn bộ giải pháp của họ).*
10. **Tác động của Trần Luật C vs Bộ chọn ưu tiên ổn định:** Ưu thế của Luật C đến từ bản thân trần $B$ hay từ Bộ chọn từ điển ưu tiên ổn định trước chi phí? Nếu dùng bộ chọn ưu tiên chi phí (cost-first), Luật C có còn tốt không?  
    *(Tình trạng: CHƯA TRẢ LỜI ĐƯỢC: thí nghiệm cost-first trên 34 kịch bản chính chưa được chạy, kết quả còn bỏ ngỏ).*

---

# PHẦN 3: ĐỐI CHIẾU VÀ ĐỒNG THUẬN GIỮA HAI BÊN NHẬN XÉT

| Vấn đề | Người đọc ngoài ngành | Giảng viên phản biện UET | Hướng xử lý cho bản thảo cuối |
|---|---|---|---|
| **Câu hỏi Mục 4.8 (Cách đệm)** | Đệm 30s chỉ kéo dài lời hứa trên giấy tờ, không ngăn được điều phối dời giờ khách | Đệm 30s kéo dài lời hứa gấp 5 lần, làm 44 khách tới sớm vô ích và không triệt tiêu rủi ro đuôi (vẫn dời 590s) | **Đồng thuận tuyệt đối:** Đưa câu trả lời tổng hợp sắc sảo này lên ngay đầu Mục 4.8 |
| **Vế cộng dồn $\sum \|c\| \le B$** | Khó hiểu tại sao thiết kế phức tạp khi chỉ có 3 bản ghi chặn ở 120s và 0 ở 30s | Đặt nghi vấn về sự cần thiết thực tế, yêu cầu so sánh với luật chỉ chặn từng bước | Nêu thẳng thắn trong Mục 4.5 và 4.11 rằng trên thực nghiệm trần từng bước đã đủ chặn phần lớn |
| **Ba mốc $v, e, p$ và Sổ cái** | Dễ hiểu lầm $e$ và $c$ là số liệu vật lý thực tế ngoài đường | Nhấn mạnh tính chất kế toán mô hình (model projection), cấm quy kết nhân quả | Bổ sung câu giải thích trực quan ở Chương 3.3 và Chương 4.3 |
| **Thiên vị chọn mẫu (Bảng 4.5, 4.7)** | Cảm thấy các bảng so sánh khó theo dõi vì mẫu số khác nhau | Chỉ rõ lỗi Selection Bias khi so sánh khách chung, khách đi chung và trễ tối đa | Thêm ghi chú thận trọng dưới Bảng 4.5 và Bảng 4.7, tránh kết luận nhân quả |
| **Tiêu chí 3 của Bộ chọn** | Cụm từ "Mức dùng trần lớn nhất nhỏ nhất" gây lú lẫn | Chỉ ra lỗi mô hình hóa khi tiêu chí bị vô hiệu hóa 100% | Viết lại câu định nghĩa cho sáng nghĩa và thừa nhận hạn chế ở Chương 3.2 |
| **Lỗi bảng nháp** | — | Yêu cầu xóa bỏ các ô `chưa đưa vào bảng` (Bảng 4.5) và `chưa đo` (Bảng 4.15) | Cập nhật số liệu thực tế đã có hoặc xóa các dòng chưa hoàn thiện |

END OF ANTIGRAVITY R27
