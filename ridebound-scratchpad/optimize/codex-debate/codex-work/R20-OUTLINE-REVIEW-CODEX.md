# R20 — Phản biện dàn ý viết lại khóa luận

Ngày kiểm: 10/10/2026. Đối tượng: OUTLINE-PROPOSAL-CLAUDE.md, đặc biệt các mục 1, 2.10, 3 và 4.3.

**Kết luận: dùng dàn ý sau khi sửa.** Đóng góp có thể bảo vệ là đặc tả, cài đặt và kiểm tra một ngân sách dời giờ trả theo từng khách, rồi đo các đánh đổi trong môi trường mô phỏng đã nêu. Cần sửa điều kiện bảo đảm, cách gọi ba phần của sổ cái, phạm vi 98 lần chạy, mẫu số của dự báo và hồ sơ nguồn trước khi giao cho người viết. Chưa có căn cứ nâng thành ưu thế phổ quát, hiệu quả kinh doanh hoặc phép đối chiếu toàn thuật toán của công trình khác.

Tôi đọc mã và kết quả đã lưu; đối chiếu trực tiếp LaTeX; đọc phần đầu và mục lục của báo cáo mẫu bằng trích xuất PDF. Tôi không chạy mô phỏng, biên dịch, cài đặt hoặc sửa khóa luận; không đọc các tệp R20 của hai phía còn lại. Việc đọc PDF ở đây kiểm nội dung và cấu trúc, chưa xác nhận cách dàn trang của bản viết lại. Các dự toán trang dưới đây là đề nghị biên tập.

## 1. Quy ước và nguồn đã mở

Trong báo cáo này, ba trạng thái có nghĩa:

| Trạng thái | Nghĩa |
|---|---|
| AGREE | Bằng chứng đã mở hỗ trợ mệnh đề trong phạm vi ghi ở dòng đó. |
| WRONG | Câu sai, thiếu điều kiện làm đổi nghĩa hoặc dùng sai phạm vi/mẫu số. |
| CANNOT CHECK | Chưa có bằng chứng đủ cho mệnh đề; không được tự điền. |

Đường dẫn rút gọn:

| Mã | Tệp gốc |
|---|---|
| O | E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/OUTLINE-PROPOSAL-CLAUDE.md |
| T | E:/Code/Report_INT3508/ridebound/noi-dung/ |
| S | E:/Code/Report_INT3508/ridebound-scratchpad/ |
| D | S/optimize/codex-debate/ |
| SRC | C:/Code/RideBound-noworse/src/ |
| A | D/codex-work/R15-audit-summary.txt |
| R15 | D/codex-work/R15-CONFIRM-CODEX.md |
| R18 | D/codex-work/R18-CONFIRM-CODEX.md |
| FP | D/ROUND16-FACT-PACK.md |
| FR | S/optimize/FORECAST-REPORT.md |
| T38 | S/tang3/t38/T38-REPORT.md |
| D03 | E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md |
| HZ | D/claude-work/pdf/hoerl-zwick-2022.txt |
| FAM | D/codex-work/r13-paper-text/Unreliability_in_ridesharing_systems_Measuring_cha.txt |
| SEL | SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs |
| BE | SRC/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs |
| DV | SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs |
| ML | D/claude-work/ml-pilot-report-a1-2026-10-08.txt |

R19-SKILLS-REVIEW.md:28–64 được áp dụng: một đóng góp trung tâm, giữ kết quả bất lợi, định nghĩa ký hiệu, nối khẳng định với nguồn, thống nhất thuật ngữ và giữ đúng mẫu số. Các mã trên phục vụ hồ sơ biên tập. Thân khóa luận dùng trích dẫn, công thức và tham chiếu hình/bảng bình thường.

Các nguồn sơ cấp đối chiếu thêm:

- [Fielbaum và Alonso-Mora](https://autonomousrobots.nl/assets/files/publications/20-Fielbaum-TRC.pdf), mục 6 và Bảng 5, trang PDF 17.
- [Schulz và Pfeiffer](https://link.springer.com/content/pdf/10.1007/s00291-026-00847-0.pdf), trang PDF 8–10 và 22.
- [Hồ sơ ETH của Hörl và Zwick](https://www.research-collection.ethz.ch/bitstreams/e0796b23-e061-4f00-a96a-1cb6b44ccb0f/download): kết quả tìm xác nhận bản hội nghị năm 2022; mở toàn văn trực tuyến lỗi. Nội dung phương trình được kiểm trên bản toàn văn HZ đã lưu, dòng 529–606. Không dùng các kết quả tìm về bài dự báo nhu cầu của Zwick–Axhausen thay cho bài này.

## 2. Kiểm từng mệnh đề của tám câu đóng góp

Một câu dài được tách thành nhiều mệnh đề để tránh việc số đúng che lời giải thích sai.

| Câu | Mệnh đề/số cần kiểm | Trạng thái | Bằng chứng và sửa bắt buộc |
|---|---|---|---|
| 1a | Đặc tả, cài đặt ngân sách theo từng khách trong RideBound | AGREE | BE:41–104 kiểm ngân sách trước + phần tăng; cấu hình S/tang3/configs/C-30.json đặt trần giờ trả 30.000 ms theo các giai đoạn đã nhận, chờ đón, trên xe. |
| 1b | c = p − e; ngân sách cộng trị tuyệt đối qua các lần sửa | AGREE | FP:31–33; S/tang3/evidence/audit_vep.py:106–123 kiểm các mốc và độ lớn; R18:181 xác nhận ngân sách cả chuyến. Không thay tổng trị tuyệt đối bằng tổng có dấu. |
| 1c | Tổng qua cả chuyến không vượt B; phương án vi phạm bị loại | WRONG | Là nghĩa vụ của các phương án đi qua kiểm ngân sách thông thường, với trạng thái trước hợp lệ. BE:80–98 còn kiểm giai đoạn áp dụng; hệ có cơ chế phục hồi. Việc không có vượt trần trong tập đã kiểm không phải bảo đảm mọi trạng thái vật lý luôn có nghiệm. Nêu điều kiện và tách cơ chế phục hồi. |
| 2a | Mốc tuyến cũ cập nhật có tiền lệ ở chiến lược B | AGREE | HZ:529–543,567–588 có mốc cập nhật, công thức (7) và ràng buộc định tuyến. Đây là quan hệ về cách xây mốc; không khẳng định đã kế thừa mã của bài. |
| 2b | “Mọi khách từ lúc đặt” là phạm vi chính xác của C | WRONG | Yêu cầu chưa được nhận chưa có sổ lời hứa đang áp luật; BE:107–114 và cấu hình quy định giai đoạn đã nhận/chờ đón/trên xe. Sửa thành “từng khách đã được nhận, từ lời hứa đầu của chuyến”. Không dùng phạm vi này để khẳng định khác hẳn mọi cách áp dụng của HZ. |
| 2c | “Không phụ thuộc phần tắc đường” | WRONG | C không cộng trực tiếp x = e − v vào ngân sách. Tuy nhiên c được tính từ kế hoạch dưới thời gian đi hiện tại; không có bất biến nói c độc lập với giao thông. e còn gồm tiến độ thực thi. D03:222–224; O:341 đã ghi đúng điều này. |
| 2d | Hai chiều, cộng dồn, kiểm theo từng khách là đại lượng đang xét | AGREE | FP:31; R18:181,301–307. Gọi đây là đặc tả của phương pháp; không suy quyền ưu tiên từ tổ hợp tính chất. D03:5–9. |
| 3a | Hồ sơ theo khung 15 phút dùng cho báo giờ đầu | AGREE | S/optimize/display_layer.py:36–64 và promise_stretch.py:29–52; FR:36–70. Chỉ báo giờ được phát lại; tuyến đã chạy không đổi. |
| 3b | Gọi một phần là “tắc đường đoán trước được” | WRONG | Mức giải thích phụ thuộc mô hình đã thử và dữ liệu nguồn. FR:72–75 là tên trong báo cáo cũ, không chứng minh khả năng biết trước nói chung. Đổi thành “phần được hồ sơ lịch sử giải thích”. |
| 3c | Hai thành phần ghép vào C đều “đã có tiền lệ” | CANNOT CHECK | Dự báo thời gian đi có nguồn đã lưu: D/claude-work/pdf/leonardi-2024.txt:18–19. Nhưng bảng neo câu 3 không nêu nguồn sơ cấp cho đúng tổ hợp “báo giờ đầu + sổ ba phần”. Bỏ khẳng định tiền lệ của cả sổ ba phần, hoặc bổ sung nguồn đúng mệnh đề. Có thể viết đây là hai thành phần được dùng trong khóa luận mà không nhận chúng là mới. |
| 4a | 34 ô, 3.672 yêu cầu, 5 ngày, hệ số toàn thành phố, FleetPy | AGREE | T38:29–33,46; S/tang3/t38/run_t38.py:3–10; A:7–9 có 34 lần chạy và 3.672 yêu cầu mỗi nhánh. Ghi rõ ô là tổ hợp ngày, mẫu chuyến và khung giờ; 34 ô không phải 34 ngày độc lập. |
| 4b | C so với U, M⁺ và đệm báo giờ | AGREE | A:7–9; kết quả đệm thuộc phát lại mốc báo giờ trên các tuyến của U. U vẫn giữ các khóa đang xét. |
| 4c | M⁺ là thành phần hạn chót kiểu Schulz–Pfeiffer, có phục hồi | AGREE | D03:214–217; bài sơ cấp đặt hạn chót sau chấp nhận đề nghị và dùng độ chùng 900 s. Thêm rõ: M⁺ là cài đặt đối chứng trên RideBound; phục hồi là của hệ thử; không tái lập toàn thuật toán hay thiết lập tham số của bài. |
| 5a | C phục vụ ít hơn 96; 2,6 điểm phần trăm | AGREE | A:7,9: 2.338 so với 2.434; 96/3.672 × 100 = 2,6144 điểm phần trăm. |
| 5b | Ít hơn 127 trễ; thêm 31 đúng hẹn ở ngưỡng 60 s | AGREE | 203 − 76 = 127; 2.262 − 2.231 = 31. Đồng nhất thức: Δ đúng hẹn = Δ phục vụ − Δ trễ = −96 − (−127). Hai nhánh phục vụ những tập khách khác nhau; không diễn giải thành 127 khách cụ thể được cứu trễ. |
| 5c | C/M⁺ cùng phục vụ 2.338; có 2.332 lượt chung | AGREE | A:7–8,19. Mỗi nhánh còn sáu lượt riêng; trễ không dự báo là 76 so với 74. Không nói “cùng mọi khách” hoặc “mọi chỉ tiêu giống nhau”. |
| 5d | C không phục hồi; M⁺ 41,3% | AGREE | T38:47,58,111; cột 41,3% là trung bình không trọng số của tỷ lệ quyết định bị ép ở 34 ô. Định nghĩa “phục hồi” theo quyết định có trạng thái bất thường được ghi, không phải mọi lần cập nhật tuyến. Chưa đưa 41,3% thành tỷ lệ gộp trên toàn bộ quyết định. |
| 6a | C/M⁺ dự báo cùng 2.328; U dự báo + đệm 30 s cũng 2.328 | AGREE | A:7–9: 2.338 − 10 = 2.328; 2.434 − 106 = 2.328. Toàn bộ 34 ô, lời hứa đầu của đúng lớp báo giờ được so. |
| 6b | Ngưỡng 120 s: 2.366 so với 2.338 | AGREE | A:9: 2.434 − 68; A:7–8: không có lượt trễ quá 120 s sau dự báo. Đây là ngưỡng đánh giá khác ngưỡng 60 s. |
| 6c | Dài thêm 37,2 s so với 7,4 s | AGREE | Từ tổng độ dài thêm / số lượt phục vụ trong A:9 và A:7: 37,1833 và 7,3671 s. M⁺ là 7,3405 s. Nêu đây là trung bình gộp theo khách trên 34 ô; không ghép với 13,7 s của nhóm 21 ô. |
| 6d | Đến sớm 1,81% so với 0,17% | AGREE | A:9: 44/2.434 = 1,8077%; A:7–8: 4/2.338 = 0,1711%. Câu gốc thiếu mẫu số, trái chính O:512. Ghi cả phân số; 0,17% này là đến sớm, khác tỷ lệ trễ trung bình 21 ô cũng làm tròn 0,17%. |
| 7a | “Toàn bộ 98 lần chạy có áp luật C” | WRONG | Đúng là 98 lần chạy của hai nhóm dùng hệ số giao thông đo: 34 ở T3.8 và 64 ở thang trần w07. Không phải mọi lần chạy C của dự án. R15:87–89; A:3–5 còn có nhóm giao thông cố định. |
| 7b | 1.256 bản ghi; một lần dời vượt B của đúng nhánh | AGREE | R15:87; A:7,10–17: 845 + 411. Có 64.371 quyết định được xác nhận; B có nhiều mức, không phải tất cả đều 30 s. Đây là bản ghi chặn ứng viên, không phải 1.256 khách bị từ chối. |
| 7c | Chưa có bản ghi phải dùng tích lũy trước để giải thích lỗi | AGREE | R18:301–305, với phạm vi hai nhóm trên. DV:222–239 có cơ chế dừng kiểm sớm; không suy ra đã nhìn mọi lỗi có thể xảy ra trên mọi ứng viên. |
| 7d | Chưa chạy đối chứng mỗi bước một trần | AGREE | R15:93; R18:305. Không biến không có lỗi riêng được ghi thành kết luận cộng dồn vô ích hoặc hai quỹ đạo tương đương. |
| 8 | Kết quả mới từ hai giai đoạn nghiên cứu | CANNOT CHECK | Chỗ trống không phải kết quả. Khi kiểm thư mục giai đoạn 1a, có 27 tệp summary.json trong 33 thư mục nhánh; chưa đủ bộ 34 ô và chưa có kiểm độc lập trọn bộ trong lượt này. Không lấy sự tồn tại thư mục làm nghiệm thu. Xóa câu 8 ở bản hiện tại. |

### 2.1. Kiểm độ đủ và đúng của các neo cho từng câu

| Câu | Neo trong O:484–490 | Kết luận về neo |
|---|---|---|
| 1 | “R17 FP:31–33; R18:181; SEL; CommitmentBudgetEvaluator.cs” | WRONG về độ rõ đường dẫn. FP là tệp riêng, không phải dòng 31–33 của R17. Bổ sung đường dẫn BE đầy đủ, hàm tạo độ dời và cấu hình giai đoạn; BE kiểm độ dời đã được cung cấp, không tự định nghĩa c. |
| 2 | HZ:529–541,567–569; R17 R6; BAN-GIAO; R13 D19 | AGREE cho tiền lệ mốc tuyến cũ; CANNOT CHECK cho khẳng định ưu tiên toàn văn liệu. Neo HZ chưa bao gồm ràng buộc (9)–(10); thêm HZ:575–588 và chỉ đúng bản hội nghị 2022. |
| 3 | FR; D03:222–224 | AGREE cho mô tả nội bộ và giới hạn phép chiếu; CANNOT CHECK cho tiền lệ của toàn bộ sổ ba phần. Cần mã tính sổ: forecast_family_a.py:63–100,134–138. |
| 4 | T38:46; RUN38:9 | AGREE cho tổng phục vụ/cơ chế thế giới; chưa đủ cho cả số ô, số yêu cầu, năm ngày và lời so bài 2026. Thêm A:7–9, RUN38:3–10 và bài sơ cấp trang PDF 8–10,22. |
| 5 | A:7–9,18–19; T38:58; DIAL17:12–13 | AGREE cho các số đã kiểm. Thêm T38:111 và định nghĩa tử/mẫu của tỷ lệ phục hồi. |
| 6 | A:7,9; R15:167–171 | AGREE cho C/U; thiếu A:8 cho M⁺ và thiếu công thức lấy trung bình độ dài thêm. Bổ sung như các dòng 6a–6d trên. |
| 7 | A:3–17; R18:301–305 | AGREE nếu dùng đúng phạm vi đã sửa. A:3–5 là nhóm giao thông cố định; không cộng vào 98. Dùng R15:87 làm neo số quyết định và R15:91 cho giới hạn bản ghi. |
| 8 | Chưa có neo kết quả | CANNOT CHECK. Không dùng tệp kế hoạch làm nguồn kết quả. |

### 2.2. Câu chữ tiếng Việt thay thế

Các đoạn đánh số dưới đây thay cho câu 1–7; câu 8 chưa đưa vào bản viết hiện tại. Đây là câu chữ đề nghị để đưa vào khóa luận, còn các bảng kiểm ở trên ở lại hồ sơ biên tập.

**(1)** Khóa luận đặc tả và cài đặt trong RideBound một ngân sách dời lời hứa giờ trả cho từng khách đã được nhận. Tại mỗi lần công bố lại, phần tính cho quyết định điều phối là c = p − e, trong đó e là giờ trả của kế hoạch cũ được tính lại từ trạng thái hiện tại. Các phương án thông thường được chấp nhận phải thỏa tổng |c| của khách trong cả chuyến không vượt ngân sách B.

**(2)** Cách dùng mốc tuyến cũ cập nhật có tiền lệ ở Hörl và Zwick (2022). Đại lượng được kiểm trong luật C là tổng độ dời tuyệt đối theo cả hai chiều; phần x = e − v không được cộng trực tiếp vào ngân sách này. Sổ các mốc v, e, p cho phép kiểm lại từng lần công bố.

**(3)** Khóa luận bổ sung một lớp báo giờ dựa trên hồ sơ giao thông lịch sử theo khung 15 phút và một sổ tổng hợp theo từng khách. Sổ ghi phần tính cho điều phối, phần được hồ sơ lịch sử giải thích và phần còn lại; cách chia này phụ thuộc mô hình dùng để tính.

**(4)** Khóa luận đánh giá các đánh đổi giữa phục vụ, đến đúng hẹn và độ dài thêm của lời hứa trên 34 ô mô phỏng FleetPy, gồm 3.672 yêu cầu trong năm ngày và dùng hệ số giao thông toàn thành phố lấy từ dữ liệu Manhattan. Các đối chứng gồm điều phối giữ khóa nhưng bỏ trần giờ trả, luật hạn chót từ lời hứa đầu và các cách đệm mốc báo giờ. Luật hạn chót dùng cùng hệ thử và cơ chế phục hồi; phép so này không tái lập toàn thuật toán của Schulz và Pfeiffer (2026).

**(5)** Khi chưa thêm dự báo, luật C với B = 30 giây phục vụ 2.338 lượt, ít hơn đối chứng không trần 96 lượt, tương đương 2,6 điểm phần trăm trên 3.672 yêu cầu. Số lượt trễ quá 60 giây giảm từ 203 xuống 76, còn số lượt đến không trễ quá 60 giây tăng từ 2.231 lên 2.262. Luật hạn chót cùng mức cũng phục vụ 2.338 lượt, với 2.332 lượt chung; tỷ lệ quyết định phải dùng phục hồi trung bình theo 34 ô là 41,3%, so với 0% của C.

**(6)** Trên toàn bộ 34 ô, sau khi thêm dự báo, C và luật hạn chót cùng có 2.328 lượt đến không trễ quá 60 giây. Đối chứng không trần có dự báo và đệm 30 giây cũng đạt 2.328 lượt, đồng thời đạt 2.366 lượt ở ngưỡng 120 giây, so với 2.338 lượt của C. Đối chứng này kéo dài lời hứa trung bình 37,2 giây và có 44/2.434 khách đến sớm quá 60 giây; các số tương ứng của C là 7,4 giây và 4/2.338 khách.

**(7)** Trong 98 lần chạy C của hai nhóm dùng hệ số giao thông đo, gồm 64.371 quyết định được xác nhận, cả 1.256 bản ghi chặn do ngân sách giờ trả đều ghi một độ dời vượt B của nhánh tương ứng. Trong tập này, chưa có bản ghi cần mức tiêu trước đó để giải thích lỗi ngân sách được ghi. Khóa luận chưa có đối chứng quỹ đạo với luật mỗi bước một trần.

Phần nêu đóng góp ở Chương 1 nên rút các đoạn trên thành ba ý: nghĩa vụ và cách kiểm; phép đo đánh đổi; sổ và giới hạn. Bảng số đầy đủ đặt tại Chương 4. Giữ các câu định lượng 5–6 trong tóm tắt hoặc cuối mục đóng góp khi đủ chỗ; không cần lặp chúng ở cả bối cảnh, mục tiêu và phạm vi.
## 3. Kiểm danh sách điều không khẳng định

| Mục trong O:493–513 | Trạng thái | Cách giữ hoặc sửa |
|---|---|---|
| Mốc cập nhật và “việc tách phần tắc đường” ở HZ | WRONG nếu “tách” được hiểu là phân rã đầy đủ nguyên nhân | Ghi “mốc tuyến cũ cập nhật theo giao thông và cách nới hạn dựa trên mốc đó”; HZ:529–588 không phải sổ quy trách nhân quả. |
| Kiểm soát trước quyết định và đánh đổi phục vụ–ổn định ở FAM | AGREE | D03:54–56; nguồn sơ cấp mục 6, Bảng 5 xác nhận. Không viết họ thuần đo sau chuyến. |
| Bảo vệ từng khách ở Elmi | AGREE trong ranh giới đã kiểm | D03:211–213 hỗ trợ việc không nhận là mới. Tôi không kiểm lại toàn thuật toán Elmi ở vòng này; không thêm khẳng định về cùng loại ngân sách hoặc cùng bảo đảm. |
| Hạn chót từ đề nghị đầu ở Schulz–Pfeiffer | AGREE | Nguồn sơ cấp trang PDF 8–10,22; giữ khác biệt độ chùng 900 s và khác hệ thống. |
| Báo giờ theo dự báo và dự báo theo giờ trong ngày | AGREE về việc không nhận là mới; CANNOT CHECK nguồn cho toàn bộ cách ghép đang mô tả | Leonardi:18–19 hỗ trợ dự báo thời gian chuyến theo thời điểm trong ngày, chưa đủ thay cho nguồn mô tả đúng lớp báo giờ này. Dùng như giới hạn đóng góp, không viết rằng đã tái lập phương pháp của nguồn. |
| Chèn động, gán lại, giới hạn giờ đến | AGREE | D03:5–9. Bảng quy tắc phải tách tiền lệ với tính năng thật sự có trong các nhánh đang chạy. |
| Không nhận C hơn mọi đối chứng về phục vụ/đúng hẹn; C 76, M⁺ 74 | AGREE | A:7–9,19; đệm U hòa ở 60 s và hơn ở 120 s. Phải để thông tin bất lợi này ở thân bài. |
| Không tự loại phương án giữ nguyên không phải ưu thế riêng | AGREE với điều kiện toán học | T/07-chuong3.tex:292–297; biến thể hạn chót max(p₀ + B, e) có p = e thỏa hạn ngay. Đây là suy luận về biến thể được viết ra, chưa là kết quả chạy toàn thuật toán HZ. |
| Không dùng cổng cứng/phạt mềm làm khác biệt với HZ | AGREE | HZ:575–588 có cả ràng buộc và phạt. |
| Không quy trách nhân quả hoặc miễn trách phần dư | AGREE | D03:222–224,236–245. Cũng sửa sơ đồ Chương 1, tên cột và chú thích hình, không để lời phủ định ở một hộp trong khi thân bài tiếp tục dùng “nguyên nhân”. |
| Không kết luận cộng dồn cần thiết/vô dụng hoặc không đổi quyết định | AGREE | R18:301–307. Dấu vết tại nhóm giao thông cố định và giả lập phải được giữ bên cạnh kết quả 98 lần chạy. |
| Không suy kinh doanh, hài lòng, giữ khách; chi phí kế hoạch khác chi phí thực | AGREE | D03:236–245; R18:315. |
| Không suy rộng; 34 ô phụ thuộc theo ngày | AGREE | RUN38:3–6; D03:224–225; năm ngày là giới hạn rõ của tập này. |
| Không gọi 30/120 s tối ưu hoặc ngưỡng cảm nhận | AGREE | D03:259–260; R18:182. |
| Ghi mẫu số của 0,17%; không gọi phần dư tuyết không thể biết trước | AGREE | FR:42; A:7; R18:329–331. Đây là yêu cầu bắt buộc, không phải chú thích tùy chọn. |
| “Các mô hình đã thử không giúp thêm” | WRONG nếu giữ nguyên như kết luận chung | ML:21 có giảm trễ 12,89% → 11,65% nhưng tỷ lệ đến sớm 7,1%. Viết “trong thí điểm, phương án học máy chưa đồng thời đạt mức cải thiện và các điều kiện về báo giờ được chọn”; không phủ nhận mọi cải thiện đã đo. |

**Hộp ngắn đề nghị cho mục 1.4:**

> Khóa luận không nhận việc kiểm soát trước quyết định, bảo vệ từng khách, dùng mốc tuyến cũ cập nhật hoặc đặt hạn chót từ lời hứa đầu là mới. Đóng góp được đánh giá ở đặc tả ngân sách, cài đặt kiểm tra và phép đo các đánh đổi trong hệ thử. C không bảo đảm giờ đến thực tế nằm trong B giây kể từ lời hứa đầu; phần dời của mô hình và phần dư không xác định trách nhiệm pháp lý. Kết quả không xác nhận ưu thế ở mọi chỉ tiêu, mức ngân sách tối ưu, tác dụng kinh doanh hoặc hiệu quả trên môi trường khác.

Các giới hạn về cộng dồn, bộ chọn, dữ liệu dự báo và học máy vẫn cần nằm ở đúng mục thực nghiệm. Không dồn toàn bộ danh sách dài vào hộp đóng góp.

## 4. Cấu trúc và mạch lập luận

### 4.1. Có đủ chức năng của một khóa luận, nhưng chưa có căn cứ về quy định riêng của UET

Dàn ý đã có bài toán, văn liệu gần, phương pháp, cài đặt, đánh giá và hạn chế. Điều này đáp ứng các chức năng học thuật cần xem xét trong yêu cầu vòng 20. Tôi không biến nhận xét ấy thành xác nhận một quy chế UET chưa được mở.

Báo cáo mẫu PDF có 50 trang vật lý; trang 1–3 gồm hai bìa tiếng Việt và một bìa tiếng Anh, trang 5–6 là tóm tắt Việt/Anh, trang 7–9 là mục lục. Nó có năm chương và bảng giả mã/ràng buộc, phù hợp cách trình bày phương pháp mà dàn ý đề nghị. Tệp mẫu là báo cáo môn học, không xác nhận tên người hướng dẫn hay yêu cầu bìa của khóa luận. Tôi đã kiểm nội dung trích xuất; chưa dùng nó để xác nhận phông, giãn dòng hoặc độ cao bảng mới.

Mạch nên là **kiểm soát phần dời do quyết định, báo giờ dựa trên dự báo, và kiểm lại kết quả theo khách**. Không gọi ba hạng kế toán là ba nguyên nhân được nhận diện. Bỏ quy tắc O:277 bắt mọi mục mở đầu bằng một trong ba nguyên nhân; phần thiết lập, kiểm tính hợp lệ và nghiên cứu liên quan không có chức năng đó.

Nên nêu ba câu hỏi ở cuối mục 1.2 và nối chúng với phần đánh giá:

| Câu hỏi nghiên cứu đề nghị | Phần trả lời | Điều không suy ra |
|---|---|---|
| Ngân sách tính trên đại lượng nào, kiểm khi nào, bảo vệ được gì? | 3.2–3.4; 4.3,4.5,4.10 | Không suy từ giữ ngân sách sang bảo đảm giờ đến thực. |
| Trong tập đã đo, giữ ngân sách đổi phục vụ, đúng hẹn và độ dài lời hứa thế nào? | 4.2,4.4,4.6 | Không suy từ hai tập trạng thái lưu khác nhau sang tác dụng riêng của bộ chọn. |
| Đổi mốc báo giờ theo hồ sơ lịch sử làm thay đổi đánh giá đến đúng hẹn thế nào, và còn giới hạn gì? | 3.5–3.6; 4.7–4.9 | Không suy khả năng biết trước của phần dư hoặc thay đổi hành vi khách. |

Đóng góp dễ hiểu nhất là một nghĩa vụ kiểm được và một phép đo cái giá của nghĩa vụ ấy. Dự báo và sổ giúp làm rõ giới hạn của nghĩa vụ. Không đặt ba thành phần thành ba phát minh ngang nhau.

### 4.2. Các chỗ phải sửa, giữ hoặc cắt

| Vị trí | Đề nghị | Lý do và neo |
|---|---|---|
| 1.1 | Giữ khách mô phỏng rq-30b7e083c7b nhưng gọi rõ là khách trong bản ghi mô phỏng | S/optimize/report-extras/example-rider-2026-10-06.txt:1–3,60 xác nhận mốc và +190,5/+17,6 s. Không phải khảo sát một khách vận hành thật. Mốc đồng hồ làm tròn tới giây nên ghi độ trễ từ thời gian gốc. |
| 1.2 | Thay “ba nguyên nhân” bằng “ba phần của phép phân tích”; đưa hai tỷ lệ giải thích vào Chương 4 | 86,1% thuộc nhóm được chọn vì trễ hơn báo giờ không dự báo, không phải mọi khách; 92,5% phụ thuộc hồ sơ HIST. FR:72–75,103–104. Không lấy chúng làm sự thật về khả năng biết trước ở phần đặt vấn đề. |
| 1.3 / 2.2–2.3 | Chương 1 có bảng định vị ngắn; Chương 2 giải thích các đại lượng | Tránh hai bảng gần giống nhau và ba lần kể cùng văn liệu. Phải còn FAM mục 6, HZ và hình thức hạn chót. |
| 2.1 | Giữ kiến trúc ghép yêu cầu–chuyến–xe và bài toán chọn; phân biệt nền lý thuyết với cài đặt đang dùng | Dàn ý không nên làm người đọc tưởng mọi phiên bản FleetPy đều dùng đúng bộ sinh và thứ tự mục tiêu của RideBound. Các trần vật lý là cấu hình của tập thử, không phải chuẩn ngành. D03:249–260. |
| 2.4 / 3.5 | Tăng khoảng nửa trang cho định nghĩa báo giờ/dữ liệu | Cần thời điểm có dữ liệu, ngày nguồn, khung 15 phút, neo hiện tại, giữ mức sau khung, xử lý cuối tuần và trường hợp không đủ ngày nguồn. display_layer.py:36–64; promise_stretch.py:29–52. |
| 3.3 | Giữ nhận xét phương án giữ nguyên, hai phản ví dụ và giới hạn của tính khả thi | Đây là phần hội đồng cần để hiểu vì sao C khác một hạn chót. Không giữ 11 trang lý thuyết; cũng không cắt sạch điều kiện (N). |
| 3.4 | Bảng quy tắc thêm các cột: tập thử, giai đoạn áp dụng, khóa, thứ tự mục tiêu, phục hồi | U/LOCKS và FREE khác cả khóa và thứ tự mục tiêu. Tên “không trần” không thể tự đại diện toàn cấu hình. SEL:271–385; FP:31–33. |
| 3.4 | Viết thứ tự mục tiêu với điều kiện kích hoạt | Thứ tự đã liệt kê là khung. Mục tiêu tránh phương án phục hồi và mức sử dụng giới hạn xuất hiện khi điều kiện tương ứng đúng; SEL:271–280,319–331. Không nói mọi nhánh luôn có mọi tầng. |
| 3.6 | Sửa công thức, tách tổng có dấu với ngân sách trị tuyệt đối | Xem mục 4.3 dưới đây. Công thức hiện tại thiếu phân biệt báo giờ gốc/dự báo và phần khép cuối chuyến. |
| 3.7 | Giữ sơ đồ cài đặt và quy trình kiểm, bỏ đếm dòng nếu không cần | Thêm một đoạn về phạm vi bộ sinh, hạn mức và thời gian xử lý nếu có số đã kiểm. Không đặt số thời gian hoặc độ phức tạp cài đặt chưa có nguồn. |
| 4.2 | Giữ bảng chính, tách tỷ lệ gộp và trung bình ô thành hai khối | Bảng 10 hàng × 8 cột cộng biểu đồ đang nặng. Mọi hàng cần cùng định nghĩa lời hứa đầu/ngưỡng. Hàng V/M⁺60 thiếu chỉ tiêu thì để dấu “chưa đưa vào bảng”, không điền 0. |
| 4.2 | Bỏ cột “lượt phải bồi thường” | Chưa có hợp đồng bồi thường cho giờ trả. Có thể ghi “lượt vượt ngưỡng trên 100 yêu cầu”; nếu muốn tiền, đặt giả định bồi hoàn riêng và không diễn đạt là nghĩa vụ thật. D03:262–265. |
| 4.3 | Giữ ví dụ cơ chế và chẩn đoán 148 yêu cầu; ghi rõ giới hạn bản ghi | Bản chặn không liệt kê mọi phương án hay chứng minh tăng B sẽ phục vụ thêm đúng số được sàng lọc. DV:222–239; R18:182. |
| 4.4 | Giữ thang trần WP14r và w07 như hai tập khác nhau | Các điểm đo không có nghĩa đường phục vụ luôn tăng đơn điệu theo B. R16-cap-outcomes.txt:3–11 có C120 phục vụ 666 nhưng C300/U 665. Không gọi U là cận trên. |
| 4.5 | Giữ kết quả tích lũy âm, kèm dấu vết khác tập | 98 lần chạy giới hạn như câu 7; nhóm cố định có sáu bản ghi ở bốn quyết định, giả lập sau bỏ trùng có bốn bản ghi ở ba quyết định. R15:88–89. |
| 4.6 | Đổi tiêu đề thành “Vai trò của ngân sách và thứ tự ưu tiên chọn phương án” | Câu hỏi cũ gợi một kết luận phân tách nguyên nhân mà phép kiểm trạng thái cố định chưa trả lời. 445/1.714 và 104/1.715 thuộc hai quần thể trạng thái; 35,54 s là tổng trên hai khách, không vượt trần một khách. R18:313–317; PV:7. |
| 4.7 | Tách nhóm 21 ô khỏi bảng toàn bộ 34 ô | 6,01/1,94/0,17% và +13,7 s thuộc 21 ô; 10/2.338 và +7,4 s thuộc 34 ô. Không đặt 10/2.338 làm tỷ lệ gộp của chính 21 ô. FR:40–70; A:7. |
| 4.7 | Giữ ba lần dừng ở dự báo trong bộ điều phối | 3/32 nhánh dừng; 47,6% tính ở 15 ô M⁺ chạy xong. Không viết dự báo trong bộ điều phối đã được bác bỏ cho mọi cách cài đặt. FR:119–146. |
| 4.8 | Giữ bằng chứng tuyết và hai dòng về tính sẵn có của dữ liệu | R18:329–331 đã phân biệt dữ liệu trước khung không được chuyển vào Runner, ngưỡng chọn sau xem số liệu, và mốc neo hiện tại chính xác. Phát lại lớp báo giờ không đổi tuyến. |
| 4.9 | Sửa tỷ lệ đến sớm của FREE: 7,1%, không phải 6,9% | ML:21 ghi 7,1%; 6,9% ở ML:25 là LOCKS tại mức đệm khác. Neo ML:45–64 trong O không chứa con số này. Không dùng kết luận “không giúp thêm” cho mọi tập/tiêu chí. |
| 4.10 | Thay “tìm kiếm không bị cắt” bằng kết quả từng bộ đếm và phạm vi bộ sinh | A:7,9 có không áp trần giữ lại, không hết công việc, nhưng mỗi nhánh có một yêu cầu bị bỏ; cài đặt hữu hạn không đồng nghĩa tìm mọi tuyến toán học. |
| 4.11 / 5.2 | Hạn chế chi tiết ở 4.11; Chương 5 tổng hợp ngắn | Tránh lặp cả danh sách. So 0,54 với khoảng 1,33 chưa cùng điều kiện; không dùng nó làm phép kiểm định trực tiếp tải thấp. Tách mô hình, dữ liệu, tích hợp và khái quát hóa. |
| 5.3 | Rút từ 1,5 xuống khoảng một trang | Nêu câu hỏi và bằng chứng cần để trả lời; bỏ ước lượng 80–140 giờ nếu chưa có căn cứ. Không đặt định mức công việc thành kết quả nghiên cứu. |
| Phụ lục A | Giữ số cũ sau kiểm nguồn gốc hoặc ghi rõ chưa dùng làm số chính | Trích lại bảng LaTeX không tự kiểm được kết quả đã lưu của tháng 9. “49% khách bị sửa” cần sửa mẫu số; xem bảng kiểm LaTeX. |
| Phụ lục B | Rút còn nhận xét và phản ví dụ cần thiết | 1,5 trang không đủ định lý, hai hệ quả và sáu phản ví dụ với giải thích. Ưu tiên điều kiện, chứng minh ngắn và bảng đối chứng; bỏ lớp suy luận không dùng. |

### 4.3. Phần toán học và định nghĩa phải giữ

**Nhận xét phương án giữ nguyên.** Gọi L là mức tiêu trước lần sửa. Giả sử 0 ≤ L ≤ B, phương án giữ nguyên được sinh và còn thỏa các ràng buộc ngoài ngân sách. Khi ấy p = e, c = 0, nên mức tiêu sau vẫn bằng L; riêng cổng C không loại phương án đó. Nhận xét không bảo đảm một tuyến đã vi phạm cửa sổ đón còn khả thi. Cách nới hạn d = max(p₀ + B, e) cũng nhận p = e theo cấu tạo. Cần giữ hai điều kiện đầu trong thân bài; nguồn T/07-chuong3.tex:193–203,292–297.

**Các đối chứng.** M⁺ kiểm p − p₀ ≤ B theo hạn chót một chiều; V kiểm tổng |pₜ − vₜ| qua các lần công bố. Có Σ(cₜ + xₜ) = pₖ − p₀ khi vₜ = pₜ₋₁ và chuỗi công bố liên tục; bản thân tổng không phải “luật hạn chót” cho đến khi đặt điều kiện ≤ B tại từng thời điểm. Nêu giả thiết chuỗi, điểm khởi đầu và xử lý đóng chuyến. Không dùng từ “cộng cả hai phần” để làm mất khác biệt giữa tổng có dấu và tổng trị tuyệt đối.

**Sổ ba phần.** Đặt a là giờ trả thực tế, p₀ là báo giờ đầu chưa dự báo, D₀ là báo giờ đầu sau dự báo, f = D₀ − p₀ và q = Σcₜ. Định nghĩa đang dùng trong mã cho đẳng thức:

a − p₀ = q + f + (a − D₀ − q).

Ba cột báo cáo được tính như vậy trên nhóm khách có a − p₀ > 60 s; forecast_family_a.py:91,134–138. Với độ trễ so báo giờ dự báo:

a − D₀ = q + (Σxₜ + ρ − f), trong đó ρ = a − pₖ.

Nếu pₖ = a thì ρ = 0. Không bỏ ρ trước khi chứng minh cách khép sổ bảo đảm điều đó ở tập đang dùng. Công thức O:345 cần viết rõ “lời hứa đầu” là D₀ hay p₀. Đặc biệt q = Σcₜ khác mức tiêu Σ|cₜ|. Phần f là độ nới báo giờ của mô hình, không phải lượng tắc đường được nhận diện nhân quả.

**Giới hạn đối với dời sớm.** Giữ trị tuyệt đối trong luật và phản ví dụ sửa khôi phục lời hứa. T/07-chuong3.tex:728–737 ghi bộ sinh chèn và số đếm dời sớm bằng 0 trong phạm vi đang bàn; điều này chưa đủ để viết c ≥ 0 cho mọi hệ điều phối, mọi khóa và mọi cách xử lý chờ. Không cắt mất ý nghĩa hai chiều để thuận tiện hóa kết quả.

### 4.4. Ngân sách trang

Phép cộng 74 trang của O:27–37 đúng về số học. Tổng các mục Chương 4 là 26,5 trang, đã chừa 0,5 trang. Tuy nhiên “70 trang nếu bỏ phụ lục” phụ thuộc vẫn giữ toàn bộ 10 trang đầu và các chỗ dành cho kết quả chưa có; không phải cận dưới chắc chắn của bản nộp.

Đề nghị giữ phụ lục ngắn và cân lại như sau:

| Phần | Dự toán đề nghị | Thay đổi |
|---|---:|---|
| Phần đầu | 9 | Hai bìa Việt, cảm ơn, tóm tắt, mục lục, danh sách hình/bảng, ký hiệu; thay đổi theo mẫu chính thức nếu có. |
| Chương 1 | 7 | Ba câu hỏi; định vị và đóng góp ngắn; không lặp bảng số. |
| Chương 2 | 6,5 | Thêm chỗ giải thích báo giờ và gốc thời gian của các nghĩa vụ. |
| Chương 3 | 12,5 | Giữ điều kiện toán học, sổ khép và cài đặt; bỏ đếm dòng không cần thiết. |
| Chương 4 | 27 | Có chỗ cho giai đoạn 1a và 1b nếu đủ bằng chứng; rút khi chưa có kết quả. |
| Chương 5 | 3 | Tổng kết khoảng 1,5; hạn chế khoảng 0,5; hướng phát triển khoảng 1. |
| Tài liệu tham khảo | 4 | Theo nguồn thực sự được trích; không ép đủ số mục. |
| Phụ lục | 4 | A khoảng 1,5; B khoảng 1,5; C khoảng 1 cho tập thử và hồ sơ tái lập. |
| **Tổng dự toán** | **73** | Còn khoảng cho bìa/tóm tắt theo quy định và kết quả bổ sung. |

Nếu giai đoạn 1b chưa có kết quả, thay phần 1,5 trang bằng đoạn khoảng 0,3 trang như O:440–441; nếu giai đoạn 1a chưa nghiệm thu, bỏ chỗ số mới khoảng một trang. Tổng dự toán khi cả hai chỗ rút lại khoảng 71 trang. Bìa/tóm tắt Anh, nếu có yêu cầu chính thức, có thể thêm khoảng hai trang. Không tăng chữ hoặc thu phông để đạt mốc. Số trang thật phải được kiểm sau dàn trang; vòng này không biên dịch bản mới.

Không thể suy độ cao bảng “0,6 trang” hoặc tổng sai số ±2 trang từ nội dung trích xuất PDF. Đây là dự đoán bố cục, không phải số đã xác minh. Giữ tối đa một bảng số và một hình bổ sung cho mỗi kết quả chính khi chúng có vai trò khác nhau.

## 5. Kiểm các khóa bằng chứng ở mục 2.10

Các khóa hiện hữu ích nhưng **chưa đủ để giao thẳng cho người viết**. Chúng trộn nguồn tính số, bản tóm tắt, LaTeX cũ và kết quả chưa có. Phải bổ sung đường dẫn, phạm vi, định nghĩa chỉ tiêu và cách gộp cho từng bảng.

| Khóa | Trạng thái | Đã kiểm và sửa cần làm |
|---|---|---|
| E1 | WRONG ở một đường dẫn; AGREE các số chính | S/exposure-check-2026-10-06.txt không tồn tại theo quy ước đường dẫn của O:388. Đúng là D/exposure-check-2026-10-06.txt:2–6. SHARE ở D/pooling-share-2026-10-06.txt:2–4 tồn tại. A:7–9,18–19 hỗ trợ số chính và tập giao. Bổ sung A:8, tử/mẫu tỷ lệ gộp, T38:111 cho trung bình ô. |
| E2 | AGREE với phạm vi | D/codex-work/R16-cap-outcomes.txt:3–11 có 8 ô, 864 yêu cầu, số phục vụ/trễ/đúng hẹn. Dự báo đang xét không hoạt động ở nhóm 12–13/11; không gán cải thiện dự báo cho nhóm này. M⁺ bị ép ở các mức có nguồn riêng W07X/LaTeX, không phải cột của CAP. |
| E3 | AGREE cho thang đã nêu; chưa đủ số nguyên trễ | LAD:2–6 tồn tại, có 16 ô và 1.728 yêu cầu. A:3–5 kiểm lại C30/60/120. LAD làm tròn tỷ lệ trễ, nên cần bảng đếm gốc để đưa số nguyên mới hoặc đúng hẹn 120 s; không nhân tỷ lệ làm tròn rồi gọi là đếm chính xác. |
| E4 | AGREE sau sửa phạm vi | A:7,10–17 và R15:87 cho 98/64.371/1.256; A:3–5,20 và R15:88–89 cho nhóm còn lại và bỏ trùng. CVP là sàng lọc lịch sử dưới các luật khác, không phải thử quỹ đạo mỗi bước một trần. |
| E5 | AGREE cho các số nguồn; thiếu mã và mẫu số | FR:36–86; tệp ví dụ ở S/optimize/report-extras/example-rider-2026-10-06.txt tồn tại. O:320 ghi report-extras/... nên cũng cần thêm tiền tố optimize/ nếu theo quy ước S. Thêm display_layer.py:36–64, promise_stretch.py:29–52, forecast_family_a.py:63–100,134–138; phân biệt 21/34 ô và phần trễ so p₀/D₀. |
| E6 | AGREE với điều kiện nhánh hoàn tất | FR:117–146 hỗ trợ 3/32 dừng và 47,6% trung bình 15 ô M⁺ hoàn tất. C còn 14 ô hoàn tất. Không so mẫu 14/15/16 mà bỏ nhãn; giữ chỗ chưa chẩn đoán ở FR:121. |
| E7 | AGREE các số; neo chưa đủ giải thích phần dư mới | SNOW:10 và RP:6–24 hỗ trợ mô tả cũ, số lượt và 601 khách. RP:5–25 chưa chứa trọn phép giải thích thêm 886,858 s; R18:327–331 có đúng phép tính và phạm vi. Thêm mã của phép phát lại; tách dữ liệu lịch sử, dữ liệu trong khung, dữ liệu trước khung và mốc neo. |
| E8 | WRONG ở số đến sớm và neo | ML:45–64 là phần kết luận, không chứa đủ bảng tỷ lệ. Thêm ML:6–7,14–15,21,25–26. Số 6,9% trong O:360 không đi cùng FREE 12,89 → 11,65%; cặp đó có đến sớm 7,1% ở ML:21. Ghi số khách từng tập 145/200,147/197 hoặc 807 khi dùng các tỷ lệ đó. |
| E9 | AGREE cho kiểm trạng thái cố định | D/codex-work/R17-portfolio-verification.txt:2–7 và R18:313–317 có các số. Thêm định nghĩa ba phép tính chi phí, số khách trong tổng 35,54 s và điều kiện kích hoạt thứ tự mục tiêu trong SEL. Không thay kiểm trạng thái cố định bằng thử quỹ đạo. |
| E10 | CANNOT CHECK kết quả hoàn chỉnh | Kế hoạch và thư mục đã có; chưa đủ 34 kết quả đã kiểm trong lượt xem. Nguồn kết quả phải là bản tính độc lập sau kiểm hoàn tất, cấu hình và liên kết đúng bản ghi. Không dùng kế hoạch làm neo số [x]/[y]. |
| E11 | WRONG về yêu cầu xin phép; CANNOT CHECK kết quả | ROUND19-CLAUDE.md:3–4 đã xác nhận chủ khóa luận chấp thuận nghiên cứu theo giai đoạn, gồm 1b. O:429 không nên ghi cần xin phép lại. Vẫn phải kiểm tương đương ở bước nền và hoàn tất kết quả trước khi đưa vào luận văn; chưa có bảng kết quả ở neo này. |
| E12 | AGREE về nội dung LaTeX; CANNOT CHECK xác minh lại kết quả cũ | Những bảng được nêu tồn tại trong T/08-chuong4.tex. Vòng này không tái tính nhóm tháng 9. Muốn đưa số vào bản mới với yêu cầu chứng cứ đã kiểm, cần ghép mỗi bảng với tệp kết quả/mã tính đã được xác minh. “README liệt kê” chưa thay phép kiểm ấy. |
| E13 | AGREE với giới hạn | BUD:2–10 tồn tại, có 32 + 116 = 148 và trung vị mức vượt nhỏ nhất 109,6 s. Đây là mức nhỏ nhất trong những bản ghi được giữ, không chứng minh mọi nguyên nhân từ chối hoặc số sẽ phục vụ nếu tăng trần. |
| E14 | AGREE với phạm vi nguồn nội bộ | D/claude-work/load-and-occupancy-2026-10-07.txt:2–3 cho trung bình có tính xe nhàn rỗi: U 0,535; C30 0,505. Ghi định nghĩa này. So với 1,33 của nghiên cứu khác cần kiểm cùng cách tính; không coi là tỷ số tải đã đối sánh. |
| E15 | AGREE cho khả năng kiểm lại bản ghi; chưa đủ tính hợp lệ ngoại suy | T38:97–113 có kiểm độc lập và ghi định nghĩa trung bình; R15:87,90–99 nêu phạm vi lỗi, chế độ chứng cứ, mục tiêu. Mã băm giúp nối đúng tệp, không chứng minh dữ liệu đại diện, nguồn thực có sẵn đúng thời điểm hoặc bảo đảm quần thể. Thêm cấu hình, tập ô và định nghĩa nhánh dừng/thiếu. |

Cần sửa thêm bốn điểm chung:

1. Định nghĩa rõ các mã còn thiếu ở O:392–405: R17, R18, FP, HZ, FAM, D03, BAN-GIAO, RUN38, WP4, WP17, DIAL17 và “R13 V”. R17 phải trỏ D/claude-work/R17-FINAL-VERDICT.md; R18 phải trỏ D/codex-work/R18-CONFIRM-CODEX.md. R17:24–39 có bảng mã phụ, nhưng người viết không nên phải lần qua nhiều bảng để tìm tệp.
2. Mỗi bảng kết quả cần một dòng ghi nhánh, danh sách ô, đơn vị, ngưỡng nghiêm “>” hay “≤”, mẫu số, cách gộp và tệp tính. “Mọi con số có neo” chưa đủ nếu không biết con số đo cái gì.
3. Chương 2 chưa có khóa đầy đủ cho bài toán nền, các ràng buộc vật lý, định nghĩa nghĩa vụ, văn liệu dự báo và giá trị khách. Thêm nhóm nguồn sơ cấp riêng; D03 là hồ sơ ranh giới nội bộ, không thay thư mục học thuật.
4. Tách số đã kiểm với số có trong bản cũ và số chưa có. Các mục chưa có kết quả được rút khỏi bảng chính; không dùng nhãn thiếu làm hàng kết quả bằng không.

## 6. Đối chiếu trực tiếp kiểm kê LaTeX

Bảng dưới kiểm **40 nhóm nhận định về vị trí/nội dung** trong mục 1 của O. AGREE ở đây xác nhận dàn ý đã mô tả đúng nội dung hiện có, không phê chuẩn tính khoa học của câu cũ. Mọi tệp được đọc trực tiếp, không dựa riêng vào lời kể trong O.

| STT | Nhận định trong dàn ý | Tệp:dòng đã đọc | Trạng thái | Nội dung thực và hệ quả |
|---:|---|---|---|---|
| 1 | Tên tiếng Việt về lời hứa có biên được chứng nhận | 00-bia.tex:15–16 | AGREE | Đúng tên đang dùng; đề nghị đổi tên ở mục 7. |
| 2 | Người hướng dẫn Việt chưa điền | 00-bia.tex:28 | AGREE | Có chỗ chờ bổ sung. Không lấy tên từ báo cáo môn học. |
| 3 | Bìa tiếng Anh và tên tương ứng | 00-bia.tex:51–52 | AGREE | Có tên tiếng Anh. |
| 4 | Người hướng dẫn Anh chưa điền | 00-bia.tex:64 | AGREE | Chỗ chưa điền đúng như O. |
| 5 | Cảm ơn nói hơn năm trăm lần chạy | 01-loi-cam-on.tex:16 | AGREE | Câu tồn tại. Đây là cận dưới, không tự mâu thuẫn với 1.991. Nên bỏ vì không giúp lời cảm ơn, không gọi số đó sai. |
| 6 | Cảm ơn nói giữ nhiều hướng từ bỏ | 01-loi-cam-on.tex:17–19 | AGREE | Câu tồn tại; phải sửa nếu các phần liên quan bị cắt. |
| 7 | Tóm tắt nói 558 + 546 | 02-tom-tat.tex:27–28 | AGREE | Không khớp bảng 558 + 685 ở Chương 4. |
| 8 | Tóm tắt có cách tường thuật thí nghiệm bị chủ khóa luận yêu cầu bỏ | 02-tom-tat.tex:33–38 | AGREE | Có cả 98/102,31/32,40/40; cần viết lại toàn đoạn theo kết quả và phạm vi. |
| 9 | Có MPS/MRP/VOT/VOR | 04-viet-tat.tex:19–22 | AGREE | Bỏ hai từ viết tắt sản xuất khi cắt phần đó; giữ từ còn thật sự dùng. |
| 10 | B đang là độ dời nhìn thấy | 04-viet-tat.tex:45–46 | AGREE | B = |p − v|; xung đột với B làm ngân sách mới. |
| 11 | β đang là trần | 04-viet-tat.tex:53 | AGREE | Đổi ký hiệu đồng bộ, không thay rời từng chương. |
| 12 | Chương 1 nói không ai tách phần quyết định khỏi tắc đường | 05-chuong1.tex:64–69 | AGREE | Câu phủ định rộng tồn tại; cần bỏ. |
| 13 | Chương 1 mô tả thước đo FAM không thể thành ràng buộc | 05-chuong1.tex:99–104 | AGREE | Câu tồn tại, không bảo vệ được cách đối chiếu văn liệu đó. |
| 14 | Ngay sau đó thừa nhận FAM đã kiểm soát | 05-chuong1.tex:106–111 | AGREE | Có 34,5 → 45,6%; đoạn trước và sau tạo cách lập luận không nhất quán. |
| 15 | Mệnh đề duy nhất/không bao giờ trong đóng góp | 05-chuong1.tex:169–182 | AGREE | Có cả danh sách và hộp. Phải sửa theo điều kiện và phạm vi đối chứng. |
| 16 | Sổ từng khách và dãy 291<300,119<120… | 05-chuong1.tex:213–217 | AGREE | Dãy số tồn tại; chuyển kiểm đúng cài đặt sang mục tính hợp lệ. |
| 17 | 89,06% được viết như quy trách nguyên nhân | 05-chuong1.tex:244–248 | AGREE | Có câu về nguyên nhân; thay bằng phép chiếu mô hình ở nhóm thời gian đi tĩnh. |
| 18 | 0,17% mức ban đầu và −7,13 điểm phần trăm | 05-chuong1.tex:250–253 | AGREE | Đây là số của nhóm/gói cũ, khác 0,17% trễ hoặc đến sớm mới. |
| 19 | Chương 2 lặp lập luận không thể ràng buộc | 06-chuong2.tex:121–127 | AGREE | Cần sửa cả nơi này, không chỉ Chương 1. |
| 20 | Chương 2 nhận tính được ranh giới pháp lý là mới | 06-chuong2.tex:184–187 | AGREE | Câu tồn tại; bỏ khẳng định đó. |
| 21 | Có bảng so với điều khiển có nhiễu | 06-chuong2.tex:225–240 | AGREE | Đúng bảng ở O; có thể cắt mà giữ định nghĩa toán học ở Chương 3. |
| 22 | Theo khách/cộng dồn/cứng được gọi là khác văn liệu | 07-chuong3.tex:168–173 | AGREE | Đúng nội dung; không giữ cách nói ưu tiên cho từng tính chất. |
| 23 | Phương án giữ nguyên có p = e | 07-chuong3.tex:193–203 | AGREE | Phát biểu tồn tại; phải giữ điều kiện ngoài ngân sách. |
| 24 | Chứng minh có điều kiện (N) | 07-chuong3.tex:292–297 | AGREE | Không được cắt điều kiện này khi rút còn nhận xét. |
| 25 | Định lý bốn họ có chuỗi công bố liên tục | 07-chuong3.tex:501–527 | AGREE | Có điều kiện quỹ đạo và chuỗi; không chép riêng thứ tự bất đẳng thức. |
| 26 | CE-2: c=0 nhưng khách vẫn thấy dời | 07-chuong3.tex:651–652 | AGREE | v=600,e=p=660; nên giữ. |
| 27 | CE-3: sửa khôi phục bị tính ngân sách | 07-chuong3.tex:653–654 | AGREE | v=p=600,e=720, C=120,V=0; nên giữ ví dụ, số 0/479 cần đúng nhóm cũ nếu còn dùng. |
| 28 | Văn bản nói chín dự án, bảng có bảy dòng | 07-chuong3.tex:699,711–717 | AGREE | Xung đột trình bày có thật. Chưa chứng minh hệ chỉ có bảy dự án; bảng có thể không liệt kê toàn bộ. Đổi thành “các thành phần chính” nếu không kiểm danh mục. |
| 29 | Bộ sinh chèn và số đếm dời sớm bằng 0 | 07-chuong3.tex:728–737 | AGREE | Đúng đoạn; không nâng thành c≥0 vô điều kiện. |
| 30 | Bảng tổng 558+685=1.243 và 79,15 GB | 08-chuong4.tex:99–111 | AGREE | Đúng nội dung hiện có. Chưa tái kiểm kích thước tệp kết quả nhóm cũ trong vòng này. |
| 31 | Bảng 89,06/1,37% cùng −154 lượt phục vụ | 08-chuong4.tex:151–171 | AGREE | Đúng các ô. Nhãn nhân quả phải sửa; B1/C1 là so gói. |
| 32 | Gọi 300 giây là điểm gãy | 08-chuong4.tex:370–372 | AGREE | Có câu đó; không dùng như kết luận chung cho tập mới. |
| 33 | Phục hồi (b)/(a)/C phục vụ 1.874/1.864/1.873 | 08-chuong4.tex:1361–1362 | AGREE | Đúng nội dung; dàn ý có thể cắt các số nhưng phải giữ định nghĩa phục hồi. |
| 34 | Bảng w07 có 660/661/666/665 và tỷ lệ bị ép | 08-chuong4.tex:1442–1461 | AGREE | Đúng các hàng 30/60/120/300 s; không phải mọi mức trung gian. |
| 35 | Bảng FAM so 54,1 lần và 49,0% | 08-chuong4.tex:1714–1731 | AGREE | 774 khách được chấm 0 chiếm 49,0% của 1.581 khách phục vụ; không phải 49% trong riêng nhóm khách bị sửa. O:382 mô tả sai mẫu số này. |
| 36 | Bảng ranh giới nhận phân rã nhân quả | 08-chuong4.tex:1810–1813 | AGREE | Có cả phủ định khả năng ràng buộc của phía 2020; cần bỏ/sửa. |
| 37 | Đệm đồng loạt bị loại với tỷ lệ 12:1 | 08-chuong4.tex:2168–2170 | AGREE | Câu tồn tại, không phù hợp đối chứng đệm mới đang cần giữ. |
| 38 | Không cho tái gán sang xe khác | 08-chuong4.tex:2269–2271 | AGREE | Đúng giới hạn bản cũ; bảng cấu hình mới cần nêu phạm vi khóa sau nhận. |
| 39 | Kết luận lại nói 558+546 và 89,06% | 09-chuong5.tex:34–37 | AGREE | Các số tồn tại; viết lại theo các nhóm thực dùng. |
| 40 | 27 mục tham khảo; tám mục chưa trích; HZ thiếu | 10-tai-lieu.tex:7–166 và lệnh trích trong các tệp nội dung | AGREE | Đếm lại 27; tám khóa là cordeau2007,toth2014,groer2009,blackburn1986,agatz2012,ortools,tlc,li2025. Không có mục HZ trong thư mục. |

**Hai sửa bổ sung cho kiểm kê:** Dàn ý O:64 chia danh sách hình ở x và danh sách bảng ở xi–xii. Mục lục của main.pdf trang vật lý 8 ghi danh sách hình bắt đầu x, danh sách bảng bắt đầu xii; vì vậy không xác nhận mốc bắt đầu xi của danh sách bảng. Tổng PDF 105 trang được đọc lại bằng bộ đọc PDF. Mốc bắt đầu không phải số trang một danh sách chiếm; không suy phân bố từ việc cộng tổng.

Việc văn bản nói “chín dự án” trong khi bảng chỉ có bảy dòng là lỗi thiếu rõ ràng, chưa phải chứng minh số chín sai. Tương tự, “hơn năm trăm” là một cận dưới còn đúng về logic. Phản biện nên sửa cách trình bày mà không tạo thêm mệnh đề sai.

## 7. Khuyến nghị cho các quyết định của chủ khóa luận

Đây là khuyến nghị cụ thể để chủ khóa luận chọn; không phải yêu cầu xin lại quyền thực hiện nghiên cứu đã được duyệt.

| Mục 4.3 của O | Khuyến nghị | Lý do |
|---|---|---|
| 1. Chương định lý | Chọn phương án (b): nhận xét khoảng một trang trong 3.3 và phụ lục B ngắn | Giữ giả thiết, chứng minh c=0 và hai phản ví dụ. Không giữ 11 trang hoặc cắt hết căn cứ toán học. Định lý không còn là đóng góp trung tâm và không bảo vệ ưu tiên toàn văn liệu. |
| 2. Người hướng dẫn | Giữ trạng thái chưa có trong hồ sơ; bổ sung khi có thông tin thật | Hai bìa chưa điền. Báo cáo môn học không xác nhận người hướng dẫn khóa luận. |
| 3. Bìa/tóm tắt Anh; lời cam đoan | Theo yêu cầu tiếng Việt hiện có: dự toán hai bìa Việt, không đưa trang tiếng Anh khi chưa có quy định chính thức buộc giữ | Báo cáo mẫu có trang Anh nhưng không phải quy định khóa luận. Khi nhận được mẫu UET áp dụng đúng khóa/ngành, ghi rõ ngoại lệ theo mẫu; không tự nhận đã kiểm yêu cầu lời cam đoan. |
| 4. Tên đề tài | Đề nghị “Kiểm soát độ dời lời hứa giờ trả trong điều phối xe đi chung” | Ngắn, mô tả đúng đối tượng bị kiểm. “Có biên được chứng nhận” dễ bị hiểu thành bảo đảm giờ đến thực hoặc chứng nhận bên ngoài; các kết quả không cho phép cách hiểu đó. |
| 5. Phụ lục | Giữ khoảng bốn trang, có điều kiện kiểm nguồn số cũ | A chứa nhóm tĩnh ngắn; B chứa căn cứ toán học; C chứa tập ô/đường dẫn kết quả/cấu hình. Không cần lịch sử toàn bộ 1.991 lần chạy nếu số đó không giúp kiểm bảng nào. |
| 6. Giai đoạn 1b | Giữ chỗ trong 4.6; đưa vào khi kiểm bước nền và hoàn tất bộ kết quả; chưa có thì dùng đoạn giới hạn ngắn | ROUND19:3–4 đã có chấp thuận. Cần kết quả phục vụ/đúng hẹn/ghép chuyến và tương tác cùng điều kiện, không riêng chi phí trạng thái cố định. Không để việc chờ số làm trì hoãn viết các phần đã có chứng cứ. Chưa có mốc nộp xác nhận; không tự dùng giữa tháng 11. |
| 7. Tên luật | C: “ngân sách dời do điều phối”; M⁺: “hạn chót từ lời hứa đầu”; V: “ngân sách dời nhìn thấy”; U: “giữ khóa, bỏ trần giờ trả”; FREE: “bỏ khóa, ưu tiên chi phí” | Tên nói được đại lượng và cấu hình. Dùng C-30/M⁺-30 trong bảng sau định nghĩa; câu giải thích bằng tiếng Việt. Thêm B1/C1/LOCKS vào bảng đối chiếu theo tập thử, không đồng nhất các nhánh qua tên. |
| 8. Cách đếm lần chạy | Đếm theo nhánh × ô × lần lặp thực dùng; tách mô phỏng khỏi phát lại báo giờ và bỏ bản lặp đúng quy tắc | Một bộ 34 ô có nhiều nhánh; số ô không phải số mô phỏng. Báo 98 với danh sách nhánh tương ứng, không đưa tổng lịch sử vào đóng góp. |
| 9. Thống kê trễ hơn một phút | Dùng đếm nguyên so với lời hứa giờ trả đầu của từng lớp và báo tỷ lệ gộp; trung bình ô ở khối riêng | A:7–9 cho số nguyên, LATE cho phân bố. Đúng hẹn / 3.672 yêu cầu tính cả từ chối trong mẫu số; tỷ lệ trễ / số phục vụ trả lời câu hỏi khác. Không dùng lẫn 8,34/3,25% với số 9,1/4,1% chưa thống nhất định nghĩa. |
| 10. Biên γ của T3.8 | Không đưa vào mạch đóng góp hiện tại | Nó thuộc câu hỏi độ phủ khác, cần thêm giả thiết và tập hiệu chỉnh. Nếu còn được viện dẫn, giữ đầy đủ 2/34 vi phạm và 7/9 ở khung 7h, không đưa thành bảo đảm ngày mới. T38:29–38; D03:224–225. |

## 8. Năm thay đổi bắt buộc trước khi viết

1. **Sửa nghĩa vụ của C và ranh giới với tiền lệ:** khách đã nhận, ngân sách cả chuyến, điều kiện trạng thái trước và phương án giữ nguyên; tách cài đặt đối chứng với tái lập bài nguồn.
2. **Sửa mạch ba phần và công thức sổ:** dùng phép phân tích theo mô hình; định nghĩa p₀/D₀, tổng có dấu/tổng trị tuyệt đối và phần khép cuối; không gọi phần dư là phần không thể biết trước.
3. **Sửa mọi mẫu số/phạm vi:** 21 so với 34 ô; tỷ lệ gộp so với trung bình ô; 98 lần chạy ở hai nhóm; 49% trên toàn bộ khách phục vụ; FREE đến sớm 7,1%, không phải 6,9%.
4. **Hoàn thiện bảng nguồn và trạng thái kết quả:** sửa đường dẫn, mã chưa định nghĩa, nguồn sơ cấp và kết quả cũ; không điền kết quả giai đoạn 1a/1b từ kế hoạch; bỏ yêu cầu xin lại chấp thuận 1b.
5. **Cân cấu trúc quanh đóng góp hẹp:** nhận xét toán học trong thân bài, phụ lục ngắn, kết luận ba trang, tên đề tài trực tiếp; dự toán khoảng 73 trang rồi kiểm số trang thật khi dàn bản mới.

Tệp này là nhận xét biên tập và kiểm chứng; không thay bản nguồn, không nhận các điểm chưa kiểm thành kết quả của khóa luận.
