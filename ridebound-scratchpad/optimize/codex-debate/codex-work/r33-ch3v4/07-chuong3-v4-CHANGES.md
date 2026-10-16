# Chương 3 v4 — sổ thay đổi Round 33

Nguồn nền: `S/rewrite-2026-10/drafts/07-chuong3-v3.tex` (726 dòng) và `07-chuong3-v3-NOTES.md`.
S = `E:/Code/Report_INT3508/ridebound-scratchpad/`; W = `S/optimize/codex-debate/codex-work/`;
AD = `E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/`; SRC = `C:/Code/RideBound-noworse/src/`;
C120 = `C:/RideBoundData/research/tier3-t38c120-v1/`.

Có **13 thay đổi**, gồm 9 thay đổi nội dung và 4 thay đổi siêu dữ liệu/anchor. Văn bản ngoài các vùng dưới đây giữ nguyên.
Mọi tệp vòng này được tạo độc quyền trong `W/r33-ch3v4/`; không sửa bản nền, thư mục drafts, mã nguồn hay dữ liệu chạy.

## 1. Một dòng cho mỗi thay đổi

Số dòng là của v3; ô cũ/mới là toàn bộ phần thay thế, xuống dòng nguồn biểu diễn bằng `<br>`.

| # | Dòng v3 | Nội dung cũ | Nội dung mới | Bằng chứng và lý do |
|---|---|---|---|---|
| 1 | 2–6 | % Chương 3 — bản viết lại, phiên bản 3 (2026-10-11). Dùng như \input{noi-dung/07-chuong3} của main.tex.<br>% Bản 1 (07-chuong3.tex) và bản trung gian 2 (07-chuong3-v2.tex) được giữ nguyên. Lý do từng thay đổi:<br>% reviews/CH3-REVISION-LOG.md. Ghi chú cho người ghép: 07-chuong3-v3-NOTES.md.<br>% Mỗi dòng &quot;% EV:&quot; trỏ tới EVIDENCE-REGISTER.md (A01…K52), EVIDENCE-REGISTER-ADDENDUM-1.md (N-01…N-30,<br>% L1a-01…09) hoặc EVIDENCE-REGISTER-ADDENDUM-2-CH3.md (X3-01…X3-41). | % Chương 3 — bản viết lại, phiên bản 4 (2026-10-12). Dùng như \input{noi-dung/07-chuong3} của main.tex.<br>% Bản 1 (07-chuong3.tex) và bản trung gian 2 (07-chuong3-v2.tex) được giữ nguyên. Lý do từng thay đổi:<br>% reviews/CH3-REVISION-LOG.md. Ghi chú v3: 07-chuong3-v3-NOTES.md; thay đổi v4: 07-chuong3-v4-CHANGES.md.<br>% Mỗi dòng &quot;% EV:&quot; trỏ tới EVIDENCE-REGISTER.md (A01…K52), EVIDENCE-REGISTER-ADDENDUM-1.md (N-01…N-30,<br>% L1a-01…09), EVIDENCE-REGISTER-ADDENDUM-2-CH3.md (X3-01…X3-41) hoặc các nguồn R26/TESTRUN ghi tại chỗ. | Siêu dữ liệu của bản v4 và nơi tra thay đổi. ROUND33-CH3-V4-PATCH.md; tệp v3 và ghi chú v3 được giữ nguyên. |
| 2 | 63–64 | Quyết định bị ép (forced decision); luật phục hồi (recovery rule) &amp; Quyết định có xe đi theo phương án vi phạm<br>luật lời hứa vì luật đó đã loại cả phương án giữ nguyên; luật phục hồi quy định phương án nào được giữ khi đó.\\ | Quyết định bị ép (forced decision); luật phục hồi (recovery rule) &amp; Lượt quyết định có ít nhất một xe bị ép:<br>luật lời hứa đã loại cả phương án giữ nguyên kế hoạch của xe, và xe chọn phương án được giữ nhờ luật phục hồi,<br>có ít nhất một khách được miễn trừ; luật phục hồi quy định phương án nào được giữ khi đó.\\ | Định nghĩa bị ép theo mã: bị loại phương án giữ nguyên và có khách được miễn; không đòi loại hết phương án khác. GLOSSARY-VI-v2.md §E, dòng 105; Ch4A v4:204–205; X3-30; C4A-10; HardVectorCandidateAssessor.cs:244–300; RunnerSession.cs:1013–1027. |
| 3 | 74 |  | ; GLOSSARY-VI-v2.md §E (bị ép); C4A-10 | Bổ sung anchor cho định nghĩa đã sửa. Các anchor của thay đổi định nghĩa ở dòng 63–64. |
| 4 | 85–86 | Một lượt bắt đầu mỗi khi FleetPy gọi bước điều phối: bộ chuyển đổi gom các sự kiện từ lần gọi trước (yêu cầu<br>mới, xác nhận đặt xe, tiến độ xe, đón, trả, thời gian đi mới) thành một lô. Bài toán ở mỗi lượt như sau. | Bộ chạy tiến theo đồng hồ sự kiện: yêu cầu đến, xe tới mốc vật lý và mốc cập nhật tắc đường đều có thể gọi một<br>lượt quyết định. Xác nhận đặt xe và cập nhật trạng thái có thể tạo thêm lượt ở cùng thời điểm mô phỏng; không có<br>chu kỳ điều phối cố định. Bộ chuyển đổi gom các sự kiện từ lần gọi trước (yêu cầu mới, xác nhận đặt xe, tiến độ xe,<br>đón, trả, thời gian đi mới) thành một lô.<br>% EV: R26-CH3-OPEN-QUESTIONS-CODEX.md §Q1; actual_fleetpy_medium_preflight.py:528-543, 569-637; fleet_control.py:395-451; preflight_world_v1_1.py:40-58; preflight_world_v1_2.py:18-20<br><br>Khung nhu cầu dài 2 giờ, nhưng lần chạy kết thúc khi hết yêu cầu và hành trình đang hoạt động. Trong 34 lần chạy<br>luật C trần 120 giây của tập kiểm tra chính, thời lượng mô phỏng từ 118,02 đến 154,93 phút.<br>% EV: R26-CH3-OPEN-QUESTIONS-CODEX.md §Q2; round26-trace-rider.txt, Q2 C-120 MAIN-PANEL SIMULATED LENGTHS; actual_fleetpy_medium_preflight.py:580-581, 639-683<br><br>Bài toán ở mỗi lượt như sau. | Q1–Q2: cơ chế gọi lượt và thời lượng mô phỏng, phân biệt khung nhu cầu với điểm kết thúc lần chạy. R26 §Q1–Q2; round26-trace-rider.txt phần Q2; AD/actual_fleetpy_medium_preflight.py:528–543,569–637,639–683; AD/ridebound_fleetpy/fleet_control.py:395–451; S/tang3/world/preflight_world_v1_1.py:40–58, v1_2.py:18–20. |
| 5 | 204 | 9: &amp; \qquad \textbf{nếu} phương án giữ nguyên bị loại chỉ vì lỗi hạn chót hay lỗi trần \textbf{thì} &amp; xe bị ép\\ | 9: &amp; \qquad \textbf{nếu} phương án giữ nguyên bị loại chỉ vì lỗi hạn chót hay lỗi trần \textbf{thì} &amp; xét phục hồi\\ | Gọi đúng bước xét phục hồi trước khi chọn phương án và xác định quyết định bị ép. GLOSSARY-VI-v2.md §E; HVA:255–300; SolverBackedRidePoolingPolicy.cs:443–463; RunnerSession.cs:1013–1027. Luồng giả mã giữ nguyên. |
| 6 | 478–480 | phạm, trừ khi lời hứa, giai đoạn và mã lỗi không đổi so với lần trước. Tập kiểm tra chính và tập buổi sáng dùng<br>luật thứ hai; cả hai là chi tiết cài đặt, không phải đóng góp của khóa luận.<br>% EV: A17; A18 (ADR:5066-5092); X3-09 (HVA:79-99, 255-326; VALID:413-420, 475-483, 537-544, 599-638, 791-818; LOCK:42-60); A19 (RUN38:9; WP4:7); X3-10 | phạm, trừ khi lời hứa, giai đoạn và mã lỗi không đổi so với lần trước. Tập kiểm tra chính, tập buổi sáng và tám<br>lần chạy chiều tuyết dùng luật thứ hai; cả hai là chi tiết cài đặt, không phải đóng góp của khóa luận.<br>% EV: A17; A18 (ADR:5066-5092); X3-09 (HVA:79-99, 255-326; VALID:413-420, 475-483, 537-544, 599-638, 791-818; LOCK:42-60); A19 (RUN38:9; WP4:7); X3-10; R26-CH3-OPEN-QUESTIONS-CODEX.md §Q8 (tám lần chạy chiều tuyết; wp4-tier3-v2.json:7) | Q8: nêu luật phục hồi của chiều tuyết tại đoạn đã mô tả các tập dùng luật này. R26 §Q8: tám manifest và phép kiểm binding; S/tang3/configs/wp4-tier3-v2.json:7; S/optimize/run_forecast.py:73–74,94–102. |
| 7 | 558 | % EV: F03 (chỉ phần &quot;phát lại trên các lần chạy đã ghi&quot;); FR:10-11; X3-12 (FFA:84-99); F06; F07 (FR:70); F12; X3-29 (preflight_world_v1_3.py:1-26, 113-133) | Số khung lấy trung bình là $K$: các cấu hình bật dự báo dùng $K = 2$, gồm khung 15 phút hiện tại và khung kế tiếp.<br>Phép thử giả dùng $K = 1$, cho hệ số bằng 1; khi tắt dự báo không đặt $K$.<br>% EV: F03 (chỉ phần &quot;phát lại trên các lần chạy đã ghi&quot;); FR:10-11; X3-12 (FFA:84-99); F06; F07 (FR:70); F12; X3-29 (preflight_world_v1_3.py:1-26, 113-133); R26-CH3-OPEN-QUESTIONS-CODEX.md §Q9; preflight_world_v1_3.py:85-89, 99-101; run_forecast.py:67-72 | Q9: điền số khung của phép thử dự báo trong bộ điều phối đã được nhắc; không coi tắt dự báo là K = 0. R26 §Q9; S/optimize/run_forecast.py:67–72; forecast-k2-2018-11-{14,15,16}.json:1; forecast-k1-2018-11-15.json:1; S/tang3/world/preflight_world_v1_3.py:85–89,99–101,147–172. |
| 8 | Thêm sau 587 | ∅ (đoạn thêm) | <br>Trong một bản ghi mô phỏng của luật C trần 120 giây, một khách có $v$ = 17:43:46,044, $e$ = 17:43:46,283 và<br>$p$ = 17:44:01,203. Phần dời $&#124;p - e&#124; = 14{,}92$ giây làm phần trần còn lại bằng $120 - 14{,}92 = 105{,}08$ giây.<br>Cả 14 bản ghi sửa sau có $c = 0$ và $&#124;x&#124; &lt; 0{,}25$ giây, nên phần trần đã dùng không tăng.<br>% EV: round26-trace-rider.txt, Q3 SELECTED RIDER, entries 1-15; R26-CH3-OPEN-QUESTIONS-CODEX.md §Q3; C-120-d20181117-s10-r1-w17/transcript-00.ndjson, final checkpoint ordinal 1716, request rq-c48d442603e9ce8c056b029d6d50c497f4d224b8af469945692690e92a75afb0 | Ví dụ ngắn từ bản ghi mô phỏng thật ở §3.6: phần trần đã dùng và còn lại qua một lần dời, rồi 14 lần sửa c = 0. round26-trace-rider.txt, Q3 SELECTED RIDER, entries 0–15 (bản đầu không tính là sửa); R26 §Q3; C120/C-120-d20181117-s10-r1-w17/transcript-00.ndjson, checkpoint ordinal 1716. Các phép trừ được kiểm bằng số nguyên mili giây trong qa-output.json. |
| 9 | 695–698 | Khóa luận chỉ báo thời gian của cả lần chạy: trên tập tắc đường cố định (16 lần chạy mỗi cấu hình), trung vị là<br>730, 667 và 641 giây với ghép tự do, điều phối không trần và luật C trần 30 giây. Chi phí riêng của phép kiểm trần<br>không được báo, nên các số này không dùng để so chi phí tính toán.<br>% EV: H13 (EL17:2-6); X3-19; B17 | Khóa luận chỉ báo thời gian thực của cả lần chạy: trên tập tắc đường cố định (16 lần chạy mỗi cấu hình), trung vị là<br>730, 667 và 641 giây với ghép tự do, điều phối không trần và luật C trần 30 giây. Thời gian này gồm mô phỏng FleetPy<br>và thời gian chờ RideBound trả quyết định, không phải thời gian của một lượt quyết định. Chi phí riêng của phép kiểm trần<br>không được báo, nên các số này không dùng để so chi phí tính toán.<br>% EV: H13 (EL17:2-6); X3-19; B17; R26-CH3-OPEN-QUESTIONS-CODEX.md §Q6; wp14r_scientific_protocol.py:801-803, 824-829; wp14r_supervised_process.py:297, 329-330, 979-985 | Q6: các trung vị là thời gian thực của cả tiến trình, có FleetPy và thời gian chờ, không phải độ trễ mỗi lượt. H13; EL17:2–6; R26 §Q6; AD/wp14r_scientific_protocol.py:801–803,824–829 (không gồm kiểm bundle độc lập về sau); AD/wp14r_supervised_process.py:297,329–330,979–985. |
| 10 | 705–706 | \item \textbf{Kiểm thử phần mềm:} khi luật phục hồi không tệ hơn được thêm vào mã, bộ kiểm thử qua 1.025 trên<br>1.025 trường hợp; số này ghi lại lúc đó, chưa chạy lại khi viết khóa luận. | \item \textbf{Kiểm thử phần mềm:} trên đúng mã nguồn đã dựng bộ chạy, cả 1.025 kiểm thử tự động đều đạt khi chạy lại<br>ngày 12/10/2026, với kiểu xuống dòng LF và một tệp chưa ghi nhận trong cây làm việc; chi tiết ở Phụ lục~\ref{phuluc:C}. | Thay số kiểm thử lịch sử chưa chạy lại bằng kết quả chạy lại được cho phép; hai điều kiện môi trường trong một mệnh đề. evidence/TESTRUN-45f8026-2026-10-12.md, §Wording allowed in the thesis; A28. Lượt 3: 1.024/1.025; lượt 3b: kiểm thử còn lại 1/1. Không phát biểu một lần chạy toàn bộ đạt 1.025/1.025. |
| 11 | 715–717 | \item \textbf{Tái lập:} tập kiểm tra chính, tập chỉnh trần buổi sáng và các lần chạy trần 120 giây dùng cùng một bản<br>bộ chạy đã biên dịch và lưu lại; tập tắc đường cố định dùng một bản cũ hơn. Bản dựng lại, nếu có, phải cho đúng kết<br>quả cũ trên một số kịch bản trước khi dùng (Phụ lục~\ref{phuluc:C}). | \item \textbf{Tái lập:} tập kiểm tra chính, tập chỉnh trần buổi sáng, các lần chạy trần 120 giây và tám lần chạy chiều<br>tuyết dùng cùng một bản bộ chạy đã biên dịch và lưu lại; tập tắc đường cố định dùng một bản cũ hơn. Bản dựng lại, nếu có,<br>phải cho đúng kết quả cũ trên một số kịch bản trước khi dùng (Phụ lục~\ref{phuluc:C}). | Q8: thêm chiều tuyết vào danh sách dùng cùng bản bộ chạy lưu trữ; giữ yêu cầu kiểm kết quả khi dựng lại. R26 §Q8: tám manifest, DLL hash và canonical binding đều khớp; S/optimize/run_forecast.py:94–102; S/tang3/w07/run_w07.py:40–43; A28. |
| 12 | 719 | % EV (kiểm thử): A27 (ADR:5100, số lịch sử) | % EV (kiểm thử): TESTRUN-45f8026-2026-10-12.md (mã nguồn bộ chạy; lượt 3 và 3b; điều kiện LF và tệp chưa ghi nhận); A28 | Cập nhật dòng bằng chứng kiểm thử, bỏ anchor chỉ có số lịch sử. TESTRUN-45f8026-2026-10-12.md; A28. |
| 13 | 722 | % EV (tái lập): A28 (RUNW07:40-41); X3-10 (run_w07.py:8; run_w07x.py:7; run_t38c120.py:3-8); B17; NEW:13; I13 | % EV (tái lập): A28 (RUNW07:40-41); X3-10 (run_w07.py:8; run_w07x.py:7; run_t38c120.py:3-8); B17; NEW:13; I13; R26-CH3-OPEN-QUESTIONS-CODEX.md §Q8 (bản bộ chạy chiều tuyết) | Bổ sung anchor bản bộ chạy chiều tuyết cho mệnh đề tái lập. Các anchor Q8 của thay đổi dòng 715–717. |

## 2. Số tiếng theo mục và ngân sách 13 trang

"Tiếng" ở đây là token cách nhau bởi khoảng trắng, có chữ hoặc số. Bộ đếm mới bỏ chú thích `%`, công thức,
lệnh điều khiển, nhãn/tham chiếu/trích dẫn và tiêu đề mục; giữ chữ trong các lệnh định dạng. Bảng gồm chữ và chú thích;
hình chỉ gồm caption và nhãn node trong nguồn, không tính tọa độ, đường vẽ hay tùy chọn TikZ. Không khai triển macro
TikZ thành chữ, không đếm công thức dưới dạng tiếng. Bộ đếm và phép kiểm lưu trong `patch_and_check.py`, kết quả
trong `qa-output.json`; bộ đếm chạy y hệt trên v3 và v4.

Không tìm thấy mã `wc_ch3_v2.py` của ghi chú v3. Do đó **không nhận bộ đếm mới là cùng bộ đếm cũ**.
Hai cột lịch sử chỉ chép từ NOTES v3 để người ghép đối chiếu; các cột v3/v4 mới có thể tự tính lại.

| Mục | Ngân sách trang | Văn xuôi v3 (đếm mới) | Văn xuôi v4 | Chênh | Bảng/hình v4 | Văn xuôi v3 (NOTES) | Bảng/hình v3 (NOTES) | Văn xuôi v4 / 330 (trang ước tính, chưa cộng float) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Mở chương | 0,25 | 158 | 158 | +0 | 0 | 164 | 0 | 0,48 |
| 3.1 | 2 | 556 | 652 | +96 | 1167 | 556 | 1164 | 1,98 |
| 3.2 | 1,75 | 362 | 362 | +0 | 76 | 362 | 118 | 1,1 |
| 3.3 | 2,5 | 708 | 708 | +0 | 145 | 708 | 146 | 2,15 |
| 3.4 | 1,5 | 738 | 743 | +5 | 255 | 738 | 254 | 2,25 |
| 3.5 | 1,25 | 514 | 552 | +38 | 150 | 514 | 151 | 1,67 |
| 3.6 | 0,75 | 337 | 382 | +45 | 76 | 337 | 75 | 1,16 |
| 3.7 | 2,5 | 673 | 711 | +38 | 305 | 673 | 340 | 2,15 |
| Dự phòng | 0,5 | — | — | — | — | — | — | — |
| **Tổng** | **13** | **4046** | **4268** | **+222** | **2174** | **4.052** | **2.248** | **12,93** |

**Đánh giá ngân sách:** văn xuôi tăng 222 tiếng và bảng/hình tăng 20 tiếng theo cùng bộ đếm mới.
V3 đã được NOTES ước tính **13,5–14,5 trang**, cao hơn ngân sách 13 trang; đây là ước lượng chưa dựng.
Mật độ chủ sở hữu nêu là khoảng 330 tiếng văn xuôi/trang, còn NOTES v3 từng dùng một hệ số khác và diện tích float riêng;
không trộn hai cách để tuyên bố đủ 13 trang. Bảng trên cho phần văn xuôi theo hệ số 330, chưa gồm 8 bảng, 3 hình,
công thức và tiêu đề. **V4 chưa được xác nhận vừa 13 trang**. Không cắt câu hay float không chịu tác động của vòng này.
Ví dụ thật được đặt ngay sau bảng sổ ở §3.6, không thêm bảng/hình và không chép 15 dòng lịch sử; đó là bổ sung ngắn
phục vụ việc đọc sổ, nhưng không khẳng định đã giải quyết phần vượt trang có sẵn. Bỏ số minh họa 613/258 ở §3.1 để
tránh thêm số khi câu mô tả đã đủ giải thích nhiều lượt cùng thời điểm. Người ghép cần kiểm bố cục thật và xử lý
phần vượt trang theo NOTES v3 §1; vòng này không được build.

## 3. Nhất quán với Chương 4 phần A v4 và bảng thuật ngữ v2

Đối chiếu với `S/rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex` và nguồn/anchor đã mở trong kiểm tra độc lập.
Không có số dùng chung nào cần sửa. Ký hiệu luật vẫn chỉ ở bảng; tên trong văn xuôi và ba mốc giữ như v3.

| Đại lượng in ở cả hai chương | Ch3 v3 | Ch4A v4 | Giá trị được giữ và bằng chứng |
|---|---|---|---|
| Khung nhu cầu, yêu cầu, đội xe | 67 | 60–62,84–85 | 2 giờ; 108 yêu cầu; 8 xe × 4 chỗ. B02/B03; fixture normalizer-configuration.json: window 28.800–36.000 s, requestTarget 108, vehicleCount 8, capacity 4. Khung nhu cầu không phải độ dài mọi lần chạy. |
| Khung hệ số tắc đường và hồ sơ | 65,434,491 | 65,91 | 15 phút. B06/X3-11; promise_stretch.py:7,22 = 900.000 ms. |
| Cửa sổ đón và thời gian ngồi xe | 121–122 | 88–89 | 10 phút = 600 s; 1,5 lần đi thẳng. B03; fixture pickupWindowMs 600.000, maximumRideTimePermille 1.500. |
| Cắt số yêu cầu/phương án mỗi lượt | 194,200,359,687–689 | 93–94 | Tối đa 2 yêu cầu; 100 phương án/xe. A24/X3-17; wp4-tier3-v2.json:10–23. |
| Bộ giải và hạt giống | 642,687–689 | 93–94 | OR-Tools 9.15; hạt giống 7. X3-14; wp4-tier3-v2.json:10–23. |
| Tập kiểm tra chính | 289–290 | 124–127 | 34 kịch bản. B10; ADDENDUM-1:9. 136 lần chạy ở Ch3 là 4 cấu hình × 34; 136 ở Ch4A:129 là 17 cấu hình × 8 của tập buổi sáng, khác phạm vi. |
| Lần dời sớm đã kiểm | 290 | 428 | Mỗi lần đúng 1 mili giây; không viết nguyên nhân. N-05; ADD1:104–111. |
| Kịch bản có/không dự báo | 548–549 | 173–174,435 | 21/34 có dự báo, 13 cuối tuần không dùng dự báo; cần ít nhất 2 ngày nguồn. F02; N-16/N-28; ADD1:5–8,113–114; display_layer.py:27–51. |
| Luật C trần 120 và quyết định bị ép | 379,419 | 564–600 | Trần 120 s; 0/20.435 quyết định bị ép. N-07; STG:44; ADD1:7,121; C-120.json:17–23. |
| Điều phối không trần (anchor của Ch3) | EV 414,448 | 329–330 | 0/20.760 quyết định bị ép. X3-16; STG:42; ADD1:5,119. Ch3 chỉ in số này trong chú thích nguồn. |

Số riêng của Ch3 là 0/20.101 quyết định bị ép dưới trần 30 giây (v3:379); STG:43, ADD1:6,120 xác nhận.
Các số runtime 730/667/641 s, 382.006/185 bản ghi/lần chạy và 1.025 kiểm thử không nằm trong phần A đang đối chiếu;
giữ phạm vi nguồn tương ứng, không ép thành số của một tập khác.

Mọi chỗ dùng "bị ép" đã xét: v3:63–64,132,204,225–226,375,379,388,409–425,434–435,447.
Định nghĩa nay gồm việc loại phương án giữ nguyên và ít nhất một khách được miễn; không yêu cầu loại hết phương án khác.
Ô giả mã dòng 204 đổi thành "xét phục hồi" vì mới là bước xét điều kiện trước khi chọn. Những chỗ còn lại không nói
các phương án khác đều bị loại và phù hợp X3-30/C4A-10. "Luật phục hồi không tệ hơn", "lượt quyết định", "bản ghi chặn",
"phần dời do điều phối", "phần thay đổi khi giữ nguyên kế hoạch" và "phần khách thấy" dùng cùng nghĩa với phần A v4.

## 4. Chi tiết kiểm thử để đưa vào Phụ lục C

Nguồn: `S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md`. Không chạy lại kiểm thử trong vòng 33.
Mã nguồn là commit `45f80261a1946f1318c99ac9d1007b50d908ecf9`, đúng nguồn đã dựng runner-tier3-v2 (A28).
Lượt 3 dùng core.autocrlf=false và core.eol=lf: **1.024/1.025** đạt. Lượt 3b thêm một tệp chưa được Git ghi nhận
và chạy riêng kiểm thử còn lại: **1/1** đạt. Câu "cả 1.025 … đều đạt" lấy đúng cách viết được tệp TESTRUN cho phép;
không diễn giải thành một lần chạy toàn bộ trên cây sạch đạt 1.025/1.025.

Hai điều kiện: (1) xuống dòng LF để bốn kiểm thử golden/fixture không gặp CRLF;
(2) một kiểm thử Source_inventory_binds_dirty_worktree_files_not_only_base_commit đòi cây có tệp chưa ghi nhận.
Phụ lục C nên giữ các điều kiện và diễn tiến hai lượt cuối, kèm đường dẫn log có trong TESTRUN. Vòng này chỉ giao
chương và sổ thay đổi, không chỉnh Phụ lục C ngoài thư mục được phép. Không mở rộng kết luận sang mã bộ chọn ưu tiên chi phí.

## 5. Kiểm tra, điều chưa xác minh và phạm vi giữ im lặng

- `qa-output.json`: 13 vùng thay đổi tường minh; phần nguồn bên ngoài giữ nguyên; ngoặc và môi trường cân;
  dấu toán chẵn; 34 nhãn không trùng; tập nhãn, tham chiếu và khóa cite giống v3. `horl2022` giữ nguyên,
  không thêm tên hội nghị hay khóa trích dẫn mới.
- Tính lại ví dụ thật từ 16 dòng chính xác (1 bản đầu + 15 sửa) trong output R26: p−e = 14.920 ms;
  120.000−14.920 = 105.080 ms; 14 sửa sau c = 0, |x| lớn nhất 213 ms, đều dưới 250 ms.
  Không gọi x là tác động vật lý thuần của tắc đường và không ẩn bản ghi để rút lịch sử thành ba dòng.
- R26 Q4 (lý do đặt tên luật), Q5 (lý do chọn thứ tự tiêu chí), Q7 (nguyên nhân các dời sớm −1 ms) vẫn thiếu bằng chứng;
  không thêm lời giải thích. Các nghĩa vận hành/thứ tự đã có bằng chứng giữ nguyên.
- Chưa phục hồi được cấu hình CPU/RAM và đầy đủ phiên bản hệ điều hành của máy chạy lịch sử. Không thay bằng máy hiện tại.
- Chưa xác minh bố cục/trang thật, chưa biên dịch LaTeX do brief cấm build; không tuyên bố chương đã vừa 13 trang.
  Bộ đếm cũ không có mã để tái lập. Các nhãn bên ngoài chương vẫn cần người ghép kiểm trong bản luận văn đầy đủ.
- Thông tin nơi công bố Hörl–Zwick thuộc vòng 32; vòng 33 không sửa hay thêm chi tiết đó.
