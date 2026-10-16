# BẢNG THUẬT NGỮ: KHÓA LUẬN RIDEBOUND — BẢN v2 (2026-10-12)

> **Ghi chú thay đổi so với `GLOSSARY-VI.md` (bản gốc giữ nguyên, không sửa).** Bản này là bản sao, chỉ sửa hai dòng ở
> mục E, theo kiểm chứng sự kiện R25 (#50) và mã nguồn chỉ đọc `C:/Code/RideBound-noworse/src/`:
> 1. **"bị ép; quyết định bị ép"** (dòng 93 của bản gốc): bỏ "luật lời hứa loại hết phương án của một xe" và "buộc
>    xe giữ nguyên kế hoạch và ghi một lần vi phạm"; định nghĩa mới theo mã: phương án giữ nguyên bị loại, xe đi theo
>    phương án được giữ nhờ luật phục hồi, có ít nhất một khách được miễn trừ (RunnerSession.cs:1012-1027;
>    HardVectorCandidateAssessor.cs:252-300). Khớp bảng thuật ngữ Chương 3 v3 và Chương 4 phần A v4.
> 2. **"kẹt"** (dòng 92 của bản gốc): mở rộng cho khớp mã và Chương 3 v3 (xe kẹt = phương án giữ nguyên bị loại mà
>    không được miễn), vì định nghĩa cũ của "bị ép" dựa vào cách hiểu "loại hết" của dòng này.
> Mọi dòng khác giữ nguyên từng chữ, kể cả các ghi chú "chưa kiểm" và dòng về kết quả mong đợi (luật của chủ sở hữu
> vẫn cấm nhắc kế hoạch niêm phong, xem `WRITING-BRIEF.md`; dòng đó không thuộc phạm vi sửa này).


Dùng kèm `STYLE-GUIDE-VI.md`. Mỗi khái niệm chỉ có một tên (quy tắc 11).

**Cách dùng các cột.**
- Cột 1 là tên dùng trong khóa luận.
- Cột 2 là tên tiếng Anh, chỉ ghi trong ngoặc ở lần đầu thuật ngữ xuất hiện (quy tắc 10), sau đó không dùng nữa.
- Cột 4 ghi bản hiện tại đang dùng gì (`tệp:dòng` trong `E:/Code/Report_INT3508/ridebound/noi-dung/`) và nên giữ hay
  thay.

**Nguồn định nghĩa.**
- BAN-GIAO là `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md`.
- R17 là `ridebound-scratchpad/optimize/codex-debate/claude-work/R17-FINAL-VERDICT.md`.
- Chỗ ghi **chưa kiểm** là định nghĩa phải đối chiếu với script đo hoặc mã trước khi viết vào luận văn.

---

## A. Dịch vụ và các bên

| Dùng | Tiếng Anh (lần đầu) | Định nghĩa ngắn | Ghi chú |
|---|---|---|---|
| dịch vụ đi chung xe | on-demand ride-pooling | Dịch vụ gọi xe trong đó một xe chở nhiều hành khách có hành trình gần nhau. | Bản hiện tại dùng "đi chung xe theo yêu cầu" (`05-chuong1.tex:5`), "xe đi chung" (`02-tom-tat.tex:4`), "ride-pooling" ngay trong câu (`08-chuong4.tex:173`), chữ tắt ODRP (`04-viet-tat.tex:13`). Giữ "đi chung xe"; bỏ "ride-pooling" và ODRP. |
| ghép khách, ghép chuyến | pooling, insertion | Bộ điều phối cho thêm một khách mới vào kế hoạch của một xe đang chở hoặc sắp đón khách khác. | "ghép chuyến" đã dùng (`06-chuong2.tex:12`). Nói về một lần cụ thể thì dùng "ghép khách". |
| hãng xe | operator | Doanh nghiệp vận hành dịch vụ: đưa ra lời hứa với khách và chịu chi phí. | Bản hiện tại có bốn tên: "nhà điều hành" (29 lần), "nhà xe" (`08-chuong4.tex:165`), "điều phối viên" (`08-chuong4.tex:792`), "hãng gọi xe chung" (`02-tom-tat.tex:12`). Chọn "hãng xe" cho phía doanh nghiệp. "Nhà xe" thường gợi chủ xe khách liên tỉnh; "điều phối viên" là người. Bỏ cả hai. |
| bộ điều phối | dispatcher | Phần mềm, ở mỗi lượt quyết định, nhận yêu cầu mới, sinh phương án và chọn kế hoạch cho từng xe. | Đã dùng (`05-chuong1.tex:248`). Khi nói về quyết định của thuật toán thì dùng tên này, không dùng "hãng xe". |
| điều phối | dispatch | Việc gán yêu cầu cho xe và sắp thứ tự điểm dừng. | Giữ. |
| yêu cầu (đặt xe) | request | Một lần khách đặt xe, gồm điểm đón, điểm trả và thời điểm đặt. | Là đơn vị đếm, khác với "khách được phục vụ" (ví dụ 3.672 yêu cầu, 2.338 khách được phục vụ; BAN-GIAO:166). |
| hành khách, khách | rider, passenger | Người đặt xe. | Dùng "hành khách" ở lần đầu mỗi chương, sau đó "khách". |
| khách được phục vụ | served rider | Khách được nhận và chở tới nơi trong lần chạy. | Bản hiện tại: "Hành khách được phục vụ" (`08-chuong4.tex:160`), "số khách được nhận" (`08-chuong4.tex:1003`); BAN-GIAO:166 viết "Số khách được chở". **Chưa kiểm**: con số trong script là "được nhận" hay "đã chở xong". Kiểm rồi dùng đúng một tên. |
| tỉ lệ phục vụ | service rate | Số khách được phục vụ chia cho số yêu cầu. | Giữ "tỉ lệ" như bản hiện tại (DACN viết "tỷ lệ"). Lần đầu luôn ghi mẫu số. |
| khách bị từ chối | rejected request | Yêu cầu không được nhận. | Giữ cách phân biệt "phương án bị loại" với "khách bị từ chối" của `08-chuong4.tex:1583-1584`. |
| khách đi chung | shared rider | Khách có ít nhất một đoạn ngồi chung xe với khách khác. | Số liệu: U 22,8%, C-30 13,4% (BAN-GIAO:217). **Chưa kiểm** định nghĩa chính xác trong script `exposure-check`. |
| khách bị dời giờ trả | exposed rider | Khách có ít nhất một lần bộ điều phối làm đổi giờ trả. | Số liệu: U 7,1%, C-30 1,4% (BAN-GIAO:218). **Chưa kiểm** định nghĩa. |

## B. Lời hứa và cách đo thời gian

| Dùng | Tiếng Anh (lần đầu) | Định nghĩa ngắn | Ghi chú |
|---|---|---|---|
| lời hứa giờ trả (giờ trả đã hứa) | promised drop-off time | Giờ khách được báo sẽ tới nơi. | Thuật ngữ trung tâm. Bản hiện tại dùng lẫn "lời hứa", "giờ hẹn" (`05-chuong1.tex:64`), "lời hứa công bố" (`06-chuong2.tex:80`), "lời hứa đang mở" (`07-chuong3.tex:52`), "ETA" (`05-chuong1.tex:37`). Dùng "lời hứa giờ trả" ở lần đầu mỗi chương, sau đó viết gọn "lời hứa". Bỏ "ETA". |
| lời hứa giờ đón | promised pickup time | Giờ khách được báo xe sẽ tới đón. | Chỉ dùng khi thật sự nói về giờ đón; khóa luận tập trung vào giờ trả. |
| lời hứa đầu (p₀) | first promise | Giờ trả báo cho khách lúc xác nhận đặt xe. | Bản hiện tại dùng cả "lời hứa đầu" (`05-chuong1.tex:166`) lẫn "lời hứa đầu tiên" (`05-chuong1.tex:145-146`). Thống nhất "lời hứa đầu". |
| cập nhật lời hứa (lần cập nhật) | re-quote, publication | Mỗi lần hệ thống báo lại giờ trả cho khách. | Bản hiện tại dùng "lần công bố" (ví dụ `07-chuong3.tex:240`). "Cập nhật lời hứa" dễ hiểu hơn; nếu giữ "công bố" thì định nghĩa một lần. |
| độ dời; tổng độ dời | revision, shift; cumulative shift | Lượng giờ trả thay đổi giữa hai lần báo, tính bằng giây và lấy độ lớn. Tổng độ dời là tổng các lần. | Bản hiện tại có năm tên: "độ dời", "xê dịch" (`05-chuong1.tex:92`), "dịch chuyển" (`05-chuong1.tex:248`), "xáo trộn" (`05-chuong1.tex:252`), "biến động" (`08-chuong4.tex:280`). Chỉ dùng "độ dời". |
| trễ so với lời hứa đầu (trễ quá 1 phút, quá 5 phút) | lateness vs. first promise | Giờ tới nơi thật muộn hơn lời hứa đầu quá một ngưỡng. | Theo BAN-GIAO:192-196. Luôn báo kèm "tới sớm" (BAN-GIAO §5 điều 5) và ghi rõ mẫu số, cách gộp (theo khách hay trung bình theo kịch bản, §5 điều 7). Hai bảng BAN-GIAO cho luật U hai số khác nhau: 9,1% (:187) và 8,34% (:194). |
| tới sớm (tới sớm quá 1 phút) | early arrival | Giờ tới thật sớm hơn giờ đã hứa quá một ngưỡng. | BAN-GIAO:300-306. Đệm đều 120 giây làm 97% khách tới sớm: đây là lý do không chỉ báo trễ. |
| không trễ quá 1 phút; tới sát giờ hứa (trong ±60 giây) | timely (one-sided); accurate (two-sided) | Một phía: giờ tới không muộn hơn lời hứa quá 60 giây. Hai phía: giờ tới nằm trong khoảng ±60 giây quanh giờ đã hứa. | BAN-GIAO:317 dùng cả "khách đúng giờ" lẫn "tới sát giờ báo (±60 s)". Chỉ viết "đúng giờ" sau khi đã định nghĩa đó là một phía hay hai phía. Không dùng lẫn hai nghĩa. |
| độ dài lời hứa; lời hứa dài thêm | quoted duration; extension | Khoảng từ lúc đặt xe tới giờ trả đã hứa. "Dài thêm" là phần cộng thêm so với lời hứa không đệm. | BAN-GIAO:300 ("dài thêm 7,4 s"). |
| đệm (đệm đều 60 giây) | padding, buffer | Cộng một khoảng cố định vào giờ hứa cho mọi khách. | BAN-GIAO:304. Bản hiện tại viết "Đệm ETA đồng loạt" (`08-chuong4.tex:2168`); đổi thành "đệm đều". |
| lời hứa theo dự báo | forecast-aware promise | Lời hứa đầu đã cộng sẵn mức tăng tắc đường dự báo, lấy trung bình lịch sử theo khung 15 phút. | BAN-GIAO:93-94; chi tiết cách tính ở `optimize/FORECAST-REPORT.md`. Không phải ý mới (BAN-GIAO:141). Phân biệt "dự báo ở lớp hiển thị", được tính lại trên lần chạy đã ghi (họ A, đạt), với "đưa dự báo vào bộ điều phối" (họ B, bị bác; BAN-GIAO:264, :283). Không viết "dự đoán trước". |
| phá lời hứa | promise broken | Khách mà chính luật đang dùng không giữ được điều nó hứa. Với luật C: phần do điều phối vượt B. Với M⁺: giờ trả thật muộn hơn lời hứa đầu quá B. | `08-chuong4.tex:1183-1185`. Giữ thuật ngữ, và định nghĩa riêng cho từng luật trong chú thích bảng. |

## C. Nguyên nhân thay đổi lời hứa và ký hiệu

| Dùng | Tiếng Anh (lần đầu) | Định nghĩa ngắn | Ghi chú |
|---|---|---|---|
| ba nguyên nhân thay đổi lời hứa | — | (1) do điều phối: ghép thêm khách; (2) do tắc đường đoán trước được; (3) do tắc đường bất ngờ. | BAN-GIAO:90-95. Đây là trục của cả câu chuyện. |
| ba mốc v, e, p | previous; exogenous projection; proposed | v: giờ trả đã báo ở lần gần nhất. e: giờ trả tính lại nếu xe giữ nguyên kế hoạch cũ, từ vị trí và tốc độ hiện tại. p: giờ trả mới nếu chọn phương án đang xét. | Bản hiện tại gắn nhãn tiếng Anh in đậm (`07-chuong3.tex:83-86`; `04-viet-tat.tex:38-40`). Bỏ nhãn. v là "lời hứa đã công bố trước", không phải "lời hứa đầu chỉ bị dời bởi tắc đường" (BAN-GIAO §5 điều 14). |
| phần do điều phối, c = p − e | dispatch-caused change | Phần lời hứa đổi vì bộ điều phối chọn kế hoạch mới thay vì giữ kế hoạch cũ. | Bản hiện tại: "độ dời do quyết định A" (`07-chuong3.tex:92`), "phần do nhà điều hành gây ra", "cơ sở hành vi" (`07-chuong3.tex:182-186`). Dùng "phần do điều phối". |
| phần thay đổi khi giữ nguyên kế hoạch, x = e − v (phần do tắc đường) | exogenous change | Phần lời hứa đổi khi xe vẫn đi theo kế hoạch cũ nhưng được tính lại với tốc độ mới. | Bản hiện tại nhấn mạnh rằng trên tập 20 kịch bản cũ, phần này còn gồm tiến độ thực của xe và độ trễ thực thi, nên không được gọi là "tác động thuần của giao thông" (`07-chuong3.tex:267-274`). Chỉ gọi "phần do tắc đường" khi thiết lập bảo đảm xe chạy đúng kế hoạch và dừng đón trả 0 giây (BAN-GIAO:119-122, :205). Kiểm lại cho từng tập kịch bản. |
| phần khách thấy, z = p − v = x + c | rider-visible change | Tổng thay đổi mà khách nhìn thấy ở một lần cập nhật. | Bản hiện tại: "độ dời khách nhìn thấy B" (`07-chuong3.tex:94`). Dùng "phần khách thấy". |
| phần đoán trước được / phần bất ngờ | anticipated / unanticipated | Phần do tắc đường được tách thành phần mà dự báo đã tính sẵn và phần còn lại. | BAN-GIAO:268-270 (sáng ngày thường: do điều phối 1,3%, đoán trước được 86,1%, bất ngờ 12,6%). Phần "đoán trước được" phụ thuộc cách dự báo đang dùng. Phần bất ngờ không tự động được "miễn" (BAN-GIAO §5 điều 8). |
| sổ cái | ledger | Bảng ghi riêng cho từng khách: mỗi lần lời hứa đổi bao nhiêu giây, phần nào do điều phối, do tắc đường đoán trước được, do tắc đường bất ngờ. | Bản hiện tại: "sổ cái cam kết" (`05-chuong1.tex:202`). Giữ "sổ cái" và định nghĩa bằng ví dụ một dòng sổ. Kết quả lấy từ sổ cái là phép tách, không phải quan hệ nhân quả (BAN-GIAO §5 điều 6). |

## D. Các luật được so sánh

| Dùng | Tiếng Anh (lần đầu) | Định nghĩa ngắn | Ghi chú |
|---|---|---|---|
| luật; cấu hình | rule; configuration | Luật là cách bộ điều phối được phép hoặc không được phép đổi lời hứa. Cấu hình là một luật với tham số cụ thể (ví dụ C-30). | Bản hiện tại dùng "cổng", "họ cổng", "cơ sở", "chính sách" cho gần cùng ý (`07-chuong3.tex:415`, `:182`, `:320`). Chỉ dùng "chính sách tối ưu" trong phát biểu lý thuyết. |
| luật C (trần thay đổi do điều phối); C-B | dispatch-change budget | Tổng độ dời do điều phối trên giờ trả của mỗi khách không vượt B; mức đang dùng là B = 30 giây. | BAN-GIAO:91-92, :107. Bản hiện tại: "trần ngân sách cam kết β" (`04-viet-tat.tex:53`), "cổng hành vi", "lời hứa có biên được chứng nhận" (`05-chuong1.tex:202`). Dùng một ký hiệu B; bỏ β, κ, ℓ. Không nhận "trần" nói chung là ý mới: chiến lược B của Hörl và Zwick (2022) gần luật C (BAN-GIAO:145-147). |
| trần; phần trần còn lại | cap; remaining budget | B là mức tối đa của một luật. | "Ngân sách" chỉ dùng trong cụm "phần trần còn lại", nếu cần. |
| luật U | locks, no drop cap | Khóa xe, điểm đón và giờ đón khi xác nhận; không giới hạn độ dời giờ trả. | BAN-GIAO:108. Trong bậc thang cam kết, luật này được gọi là LOCKS (BAN-GIAO:236). Thống nhất gọi "luật U". |
| ghép tự do | free re-optimisation (FREE) | Không khóa gì; ở mỗi lượt quyết định, bộ điều phối được đổi mọi thứ. | BAN-GIAO:109. "FREE" chỉ dùng làm nhãn trong bảng. **Chưa kiểm** có cho đổi xe hay không: bản hiện tại ghi mọi cấu hình đều cấm chuyển khách sang xe khác (`08-chuong4.tex:128-131`). |
| hạn chót tính từ lời hứa đầu; M⁺-B | deadline from the first promise | Giờ trả mới không được muộn hơn lời hứa đầu quá B; phần do tắc đường cũng bị tính. | BAN-GIAO:110 và §5 điều 1: viết "thành phần hạn chót kiểu Schulz và Pfeiffer", không phải phương pháp của họ. Bản hiện tại: "hạn chót một chiều" (`05-chuong1.tex:220`). |
| hạn chót hai chiều; M-B | two-sided deadline | Giờ trả mới không được lệch lời hứa đầu quá B, cả sớm lẫn muộn. | `08-chuong4.tex:976-977`. Chỉ cần nếu chương thực nghiệm giữ kết quả này. |
| luật V (trần trên độ dời khách thấy); V-B | outcome cap | Tổng độ dời khách thấy không vượt B; phần do tắc đường cũng bị tính. | BAN-GIAO:111. Bản hiện tại: "cơ sở kết quả", "cổng kết quả" (`07-chuong3.tex:188-191`). |
| bậc thang cam kết | commitment ladder | Dãy luật từ lỏng tới chặt: ghép tự do → U → C-120 → C-60 → C-30. | BAN-GIAO:229-241 (đợt chạy cũ, tắc đường cố định). |
| điểm gãy | breakpoint | Mức trần mà từ đó siết thêm thì số khách giảm rõ, còn độ tin cậy tăng ít. | BAN-GIAO:241 ("giữa 60 và 120 s"). Bản hiện tại viết "Điểm gãy nằm ở 300 giây" (`08-chuong4.tex:370`), theo bộ số cũ. |
| giá của luật | cost of a rule | Số khách mất đi so với luật đối chứng, viết bằng số khách và điểm phần trăm số yêu cầu. | BAN-GIAO:180 và §5 điều 4: "96 khách, tức 2,6 điểm phần trăm số yêu cầu (3,9% số khách của U)". |

## E. Bên trong bộ điều phối

| Dùng | Tiếng Anh (lần đầu) | Định nghĩa ngắn | Ghi chú |
|---|---|---|---|
| lượt quyết định | decision epoch | Một lần bộ điều phối chạy: nhận sự kiện mới, sinh phương án, chọn kế hoạch. | Bản hiện tại: "kỷ nguyên" (19 lần, ví dụ `07-chuong3.tex:384`), "khung quyết định" (`08-chuong4.tex:1002`). Dùng "lượt quyết định". |
| phương án | candidate plan | Một kế hoạch có thể chọn cho một xe: danh sách điểm dừng theo thứ tự. | Giữ. |
| phương án giữ nguyên kế hoạch | keep-route option | Phương án xe tiếp tục kế hoạch cũ, không nhận thêm khách. | Bản hiện tại: "phương án không làm gì" (`07-chuong3.tex:193`), "no-op" (`07-chuong3.tex:203`), chỉ số "noop" (`07-chuong3.tex:497`). Thay bằng "phương án giữ nguyên kế hoạch". |
| bộ sinh phương án; chỉ chèn thêm | candidate generator; insertion-only | Phần tạo phương án bằng cách chèn cặp điểm đón–trả của khách mới vào kế hoạch đang có, giữ nguyên thứ tự các điểm cũ. | `07-chuong3.tex:726-729`. "Bộ sinh chèn thuần" (`07-chuong3.tex:574`) đổi thành "bộ sinh chỉ chèn thêm". |
| bộ chọn phương án | selector | Phần so các phương án hợp lệ theo một thứ tự tiêu chí và chọn kế hoạch cho cả đội xe. Thứ tự tiêu chí: so tiêu chí thứ nhất trước, chỉ khi hòa mới xét tiêu chí thứ hai. | Bản hiện tại: "hàm mục tiêu từ điển", "tầng", "hồ sơ mục tiêu" (`07-chuong3.tex:383`; `08-chuong4.tex:1922`, `:2108`). R17:593 dùng "bộ chọn". Giải thích "thứ tự tiêu chí" một lần bằng ví dụ. |
| ưu tiên ổn định | stability-first | Thứ tự tiêu chí trong đó các tiêu chí về mức dùng trần và số lần sửa lời hứa đứng trước chi phí vận hành. Luật U và luật C dùng chung bộ chọn này. | `08-chuong4.tex:2089-2091` liệt kê một thứ tự tầng của biến thể có cảnh báo; R17:662 ("bỏ hai tầng 'ưu tiên ổn định'"). **Chưa kiểm** thứ tự chính xác trong `SolverBackedFleetSelection.cs`. |
| ưu tiên chi phí | cost-first | Thứ tự tiêu chí bỏ các tiêu chí ổn định: số quyết định bị ép → số khách được nhận → chi phí vận hành. | R17:225. Đây mới là thí nghiệm tùy chọn, **chưa chạy**. Không viết như một kết quả. |
| bộ giải | solver | Chương trình quy hoạch nguyên (OR-Tools) chọn tổ hợp phương án cho đội xe. | Bản hiện tại có "chứng cứ solver" (`08-chuong4.tex:2111`). Dùng "bộ giải", "dữ liệu ghi của bộ giải". |
| kẹt (xe kẹt) | infeasible vehicle | Lượt quyết định mà phương án giữ nguyên kế hoạch của một xe bị loại mà không được miễn trừ (gồm cả trường hợp mọi phương án của xe đều bị loại); bộ chạy báo lỗi và lần chạy dừng. | Bản hiện tại: "vô nghiệm" (55 lần; `07-chuong3.tex:304`), "tập phương án rỗng" (`07-chuong3.tex:289`). Dùng "kẹt", giải thích ở lần đầu. **Sửa ở v2:** định nghĩa cũ ("mọi phương án … đều bị loại") hẹp hơn mã: `HardVectorCandidateAssessor.cs:328-390` cũng dừng khi chỉ phương án giữ nguyên bị loại mà phương án khác còn; sổ X3-31; Chương 3 v3, giả mã dòng 12. |
| bị ép; quyết định bị ép | forced decision | Lượt quyết định có ít nhất một xe bị ép: luật lời hứa đã loại cả phương án giữ nguyên kế hoạch của xe, và xe đi theo phương án được giữ nhờ luật phục hồi (phương án giữ nguyên, hoặc với luật không tệ hơn, một phương án đổi kế hoạch), có ít nhất một khách được miễn trừ. Không đòi mọi phương án khác bị loại. | `08-chuong4.tex:1177-1178`, `:1234`. Giữ "bị ép", định nghĩa một lần. **Sửa ở v2:** định nghĩa cũ ("loại hết phương án của một xe … buộc xe giữ nguyên kế hoạch và ghi một lần vi phạm") lệch mã. Mã (`C:/Code/RideBound-noworse/src/`): `RideBound.Runner/Protocol/RunnerSession.cs:1012-1027` (chứng chỉ "không bình thường" khi có ít nhất một miễn trừ); `RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:252-300` (phục hồi chỉ xét khi phương án giữ nguyên bị bộ kiểm loại; với luật không tệ hơn, giữ thêm phương án đổi kế hoạch); `RideBound.Application/Commitments/CommitmentDecisionValidator.cs:141-145`; `RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:443-463`. Vi phạm chỉ được ghi khi lời hứa, giai đoạn hay mã lỗi đổi (sổ X3-09b). Sổ: X3-30, X3-09, C4A-10. |
| luật phục hồi giữ nguyên kế hoạch; luật phục hồi không tệ hơn | recovery: keep route; no-worse-than-reference | Hai cách xử lý khi xe bị ép. Giữ nguyên kế hoạch: xe đi tiếp kế hoạch cũ. Không tệ hơn: xe được đổi kế hoạch nếu không vi phạm thêm luật nào và trên mỗi luật đã vi phạm không tệ hơn kế hoạch cũ. | `08-chuong4.tex:1177-1178`, `:1319-1320`. Đặt tên bằng lời thay cho "(a)", "(b)". |
| khóa (xe, điểm đón, giờ đón) | lock | Cấm đổi một thuộc tính của lời hứa sau khi khách xác nhận. | "Khóa cứng" (`07-chuong3.tex:682-683`). Giữ "khóa". |
| thời gian chờ đón tối đa (cửa sổ đón) | maximum wait (pickup window) Ω | Khách phải được đón trong vòng 600 giây (10 phút). | `08-chuong4.tex:62`; BAN-GIAO:203. **Chưa kiểm** mốc bắt đầu tính. Dùng "cửa sổ đón" sau khi đã định nghĩa. |
| giới hạn thời gian ngồi xe | maximum ride time Δ | Thời gian khách ngồi trên xe không quá 1,5 lần thời gian đi thẳng. | `08-chuong4.tex:63`; BAN-GIAO:203-204. Bản hiện tại viết "Ràng buộc thời gian trên xe". |
| điều kiện kiểm tra lúc đón | window check at boarding (domain invariant) | Quy tắc của mô hình dữ liệu: xe đến đón sau giờ đón muộn nhất đã chấp nhận thì thao tác đón bị từ chối và lần chạy dừng. | Bản hiện tại: "bất biến miền", "bất biến cửa sổ đón", "tầng miền", "bức tường" (`08-chuong4.tex:754`, `:784`, `:1686-1689`). Viết bằng lời; không dùng "bất biến". Ở các đợt chạy sau có chế độ ghi nhận đón muộn thay vì dừng (`08-chuong4.tex:2250-2251`). |

## F. Thực nghiệm và đo lường

| Dùng | Tiếng Anh (lần đầu) | Định nghĩa ngắn | Ghi chú |
|---|---|---|---|
| bộ mô phỏng FleetPy | simulator | Phần mềm mô phỏng xe chạy trên mạng đường, gửi sự kiện cho bộ điều phối và thực hiện kế hoạch được chọn. | `07-chuong3.tex:722`. |
| lần chạy (mô phỏng) | run | Một lần mô phỏng một kịch bản với một cấu hình. | Không dùng "job". |
| kịch bản (thực nghiệm) | cell, scenario | Một tổ hợp ngày, mẫu nhu cầu và khung giờ: 108 yêu cầu, 8 xe 4 chỗ, 96 điểm. | Bản hiện tại dùng "ô" (`08-chuong4.tex:45`). Đề xuất "kịch bản", như DACN ("120 kịch bản", tr. 29). Nếu giữ "ô" thì định nghĩa một lần và dùng nhất quán. "Kịch bản" không dùng cho kiểu tắc đường. |
| tập kịch bản (chính, phát triển, hiệu chỉnh, kiểm tra) | panel; development, calibration, test set | Nhóm kịch bản dùng cho một mục đích. Tập kiểm tra có 34 kịch bản, tức 3.672 yêu cầu (34 × 108). | "panel" xuất hiện 74 lần ở bản hiện tại (`08-chuong4.tex:45`); bỏ. Tập hiệu chỉnh 15 kịch bản và tập kiểm tra 34 kịch bản theo thiết kế T3.8 (ghi chép handoff). **Chưa kiểm** lại số này với `T38-REPORT.md`. |
| khung giờ | time window | 7:00–9:00, 8:00–10:00, 17:00–19:00. | Chỉ dùng "khung" cho khung giờ. Bản hiện tại dùng "khung" khoảng 124 lần với nhiều nghĩa: khung giờ, khung so sánh, khung tin, khung quyết định. |
| kiểu tắc đường; tắc đường đo thật, tắc đường tự tạo | traffic scenario; measured, synthetic | Cách hệ số tắc đường thay đổi trong một lần chạy: không đổi, một cú sốc, sốc lặp, tắc giảm dần, nhiễu theo cặp điểm, ngày đo thật. | Giữ các tên ở `08-chuong4.tex:1260-1265`. Bỏ "thế giới" (`08-chuong4.tex:1175`). |
| hệ số tắc đường | travel-time factor | Số nhân áp lên thời gian đi trong một khung 15 phút, đo từ dữ liệu taxi, riêng cho từng ngày. Hệ số 1,2 nghĩa là chuyến đi lâu hơn 20% so với mức nền. | Bản hiện tại có ba tên: "hệ số thời gian di chuyển" (`08-chuong4.tex:710-711`), "hệ số giao thông" (`08-chuong4.tex:2228`), "hệ số tắc đường" (`04-viet-tat.tex:58`). Dùng "hệ số tắc đường". Phải nêu hai giới hạn: một hệ số chung cho cả thành phố, và mức nền lấy lúc 00:00 (BAN-GIAO §5 điều 2). |
| tắc đường tăng / tắc đường giảm | adverse / favourable drift | Chiều thay đổi của hệ số tắc đường trong khung giờ. | Thay "trôi dạt" (106 lần), "trôi bất lợi", "trôi thuận lợi" (`07-chuong3.tex:566-568`). |
| hạt giống ngẫu nhiên | random seed | Số cố định để lần chạy lặp lại được đúng như cũ. | `08-chuong4.tex:65`. Định nghĩa một lần. |
| luật đối chứng | control | Luật dùng làm mốc so sánh trong cùng điều kiện. | Không dùng "nhánh điều trị" (`08-chuong4.tex:619`). Viết "cấu hình được thử". |
| kết quả mong đợi ghi trước khi chạy | preregistered prediction | Kết quả dự kiến của từng kịch bản, được ghi lại trước khi chạy để không sửa được về sau. | Thay "tiền đăng ký", "niêm phong" (`05-chuong1.tex:185-186`; 36 lần "niêm phong"). Thân bài chỉ cần một câu thường; mã băm và giờ ghi để ở phụ lục (STYLE-GUIDE mục 5.2, điểm 5). |
| thí nghiệm thăm dò | exploratory experiment | Thí nghiệm không phải kiểm định chính thức; kết quả chỉ có tính gợi ý. | Nêu một lần cho mỗi thí nghiệm. Bản hiện tại lặp 34 lần. |
| kiểm tra độc lập | independent recomputation | Tính lại kết quả bằng một chương trình viết riêng, từ dữ liệu thô. | Bản hiện tại có "Một agent kiểm độc lập" (`08-chuong4.tex:1383`). Mô tả trung thực ai hoặc cái gì đã kiểm, một lần ở mục phương pháp. Không ghi rằng một người đã xác nhận nếu chỉ có AI kiểm (R19 dòng 76). |
| tính lại trên lần chạy đã ghi | replay | Tính chỉ số mới từ dữ liệu của các lần chạy đã có, không chạy thêm mô phỏng. | Dùng cho "họ A" của lời hứa theo dự báo (BAN-GIAO:264). |
| trung vị; phân vị 90 | median; 90th percentile | Trung vị là giá trị ở giữa khi xếp từ nhỏ tới lớn. Phân vị 90 là giá trị mà 90% số quan sát không vượt. | Giải thích bằng lời ở lần đầu. |
| khoảng tin cậy 95% | 95% confidence interval | Khoảng chứa giá trị thật với độ tin cậy 95% theo phương pháp đã nêu. | Tên phương pháp (Clopper–Pearson, bootstrap) nêu ở mục phương pháp, không lặp lại. |
| ngưỡng nhiễu | noise floor | Mức chênh mà dưới đó không diễn giải được kết quả. | Bản hiện tại: "sàn nhiễu" (`08-chuong4.tex:389-391`, ±0,3 điểm phần trăm trên tập 20 kịch bản cũ). |
| đường đánh đổi | trade-off frontier | Đường nối các cấu hình theo hai chỉ số đối nghịch, ví dụ số khách và độ tin cậy. | Bản hiện tại: "đường biên" (`08-chuong4.tex:329`), "mặt cong" (`08-chuong4.tex:1624`). |
| điểm phần trăm | percentage point | Đơn vị cho chênh lệch giữa hai tỉ lệ. | Không viết "pp" (16 lần, ví dụ `08-chuong4.tex:161`) hay "điểm %" (BAN-GIAO:180). |

---

## G. Bảng thay thế nhanh

| Từ đang có (ví dụ vị trí) | Thay bằng |
|---|---|
| niêm phong (`05-chuong1.tex:186`), tiền đăng ký (`05-chuong1.tex:185`), dự đoán trước | "kết quả mong đợi được ghi lại trước khi chạy"; chi tiết để ở phụ lục |
| lời hứa có biên được chứng nhận (`05-chuong1.tex:202`; tên đề tài ở `00-bia.tex:15`) | luật C (trần thay đổi do điều phối) |
| cưỡng chế được (`05-chuong1.tex:199`) | "luôn giữ được, theo cách xây dựng luật" |
| cổng, họ cổng (`07-chuong3.tex:415`) | luật, nhóm luật |
| cơ sở hành vi / cơ sở kết quả (`07-chuong3.tex:182-191`) | luật C / luật V |
| quy trách (`05-chuong1.tex:64`) | tách nguyên nhân |
| văn liệu (`05-chuong1.tex:31`), dòng bài, trục văn liệu (`05-chuong1.tex:53`) | các nghiên cứu trước, tài liệu |
| nghĩa vụ phương tiện / kết quả (`06-chuong2.tex:162-187`) | bỏ, hoặc một câu so sánh |
| trôi dạt, thế giới trôi dạt (`05-chuong1.tex:271`) | thay đổi do tắc đường; tắc đường tăng / giảm |
| thế giới (`08-chuong4.tex:1175`) | kiểu tắc đường |
| panel (`08-chuong4.tex:45`), ô | tập kịch bản, kịch bản |
| nhánh, nhánh điều trị (`08-chuong4.tex:619`) | cấu hình, cấu hình được thử |
| kỷ nguyên (`07-chuong3.tex:384`), khung quyết định | lượt quyết định |
| phương án không làm gì, no-op, noop (`07-chuong3.tex:193`, `:203`, `:497`) | phương án giữ nguyên kế hoạch |
| vô nghiệm, tập phương án rỗng (`07-chuong3.tex:289`, `:304`) | kẹt (không còn phương án hợp lệ) |
| bất biến miền, tầng miền, bức tường (`08-chuong4.tex:754`, `:784`) | điều kiện kiểm tra của mô hình dữ liệu |
| phản thực, mốc ngoại sinh (`07-chuong3.tex:19-20`, `:317`) | giả định giữ nguyên kế hoạch; giờ trả tính lại khi giữ nguyên kế hoạch |
| hàm mục tiêu từ điển, tầng, hồ sơ mục tiêu (`08-chuong4.tex:1922`, `:2108`) | bộ chọn phương án, thứ tự tiêu chí |
| heuristic (`08-chuong4.tex:945`, `:1018`) | quy tắc kinh nghiệm |
| hậu nghiệm, hồi tố (`08-chuong4.tex:901`, `:941`) | kiểm lại trên dữ liệu đã có (sau khi đã biết kết quả) |
| ratchet (`07-chuong3.tex:689`) | bảo đảm một chiều (chỉ cho giờ đón tốt lên) |
| freeze horizon, hàng rào đóng băng (`07-chuong3.tex:685`) | khóa trong N giây trước giờ đón |
| xáo trộn, xê dịch, dịch chuyển, biến động | độ dời, tổng độ dời |
| nhà xe, điều phối viên, nhà điều hành | hãng xe (doanh nghiệp) hoặc bộ điều phối (phần mềm) |
| ETA (`05-chuong1.tex:37`, `08-chuong4.tex:2168`) | giờ đến dự kiến, lời hứa giờ trả |
| pp, điểm % | điểm phần trăm |
| CVaR (`08-chuong4.tex:253`) | trung bình của 5% (hoặc 1%) khách chịu thiệt nhiều nhất |
| frame, khung tin (`08-chuong4.tex:1190`; `07-chuong3.tex:724`) | bản tin trao đổi giữa bộ mô phỏng và bộ điều phối |
| agent (`08-chuong4.tex:1383`) | mô tả rõ người hay công cụ đã kiểm |
| solver (`08-chuong4.tex:2111`) | bộ giải |
| fixture (`08-chuong4.tex:2096`) | dữ liệu đầu vào của kịch bản |
| vector ngân sách, chính sách vector cứng (`08-chuong4.tex:2026`; `09-chuong5.tex:207`) | danh sách các trần |
| sàn nhiễu (`08-chuong4.tex:389`) | ngưỡng nhiễu |
| độ nhạy quỹ đạo (`08-chuong4.tex:377`) | "kết quả nhạy với các lựa chọn sớm" |
| ride-pooling (`08-chuong4.tex:173`) | đi chung xe |
| bắn, cắn đau, ngốn, đóng đinh, món hời tồi (`08-chuong4.tex:1689`, `:1615`, `:367`, `:1676`, `:1680`) | viết thẳng nghĩa |

## H. Chữ viết tắt

| Chữ tắt (Danh mục hiện tại, `04-viet-tat.tex:13-25`) | Đề xuất |
|---|---|
| ODRP, RTV, ILP, MPS, MRP, SLA | Bỏ. Viết bằng lời ở lần dùng: "đồ thị ba tầng yêu cầu–chuyến–xe", "quy hoạch nguyên". MPS, MRP và SLA chỉ cần nếu giữ phần hoạch định sản xuất và luật hợp đồng. |
| ETA | Bỏ; dùng "giờ đến dự kiến" hoặc "lời hứa giờ trả". |
| VOT, VOR | Bỏ; dùng "giá trị thời gian", "giá trị độ tin cậy" nếu còn giữ phần phúc lợi. |
| pp | Bỏ; viết "điểm phần trăm". |
| DARP | Giữ nếu Chương 2 cần, giới thiệu một lần: "bài toán đưa đón theo yêu cầu (Dial-a-Ride Problem, DARP)". |
| TLC | Viết đầy đủ một lần ở mục dữ liệu: "Ủy ban Taxi và Xe limousine New York (Taxi & Limousine Commission, TLC)". |
| C, U, M⁺, V, B | Không phải chữ viết tắt mà là tên luật và ký hiệu. Định nghĩa trong một bảng ở chương phương pháp và đưa vào Danh mục ký hiệu. Bỏ β, κ, ℓ (`04-viet-tat.tex:53-55`) để chỉ còn B. |
