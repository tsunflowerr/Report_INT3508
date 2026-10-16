# Round 39 — Chương 4 phần B v11, bản tiếp tục v2

**Bản giao: `09-chuong4-phanB-v11-v2.tex`; @@CHANGE_COUNT@@ vùng thay đổi so với v10.** Bản này áp R37 và các việc phần A bàn giao, theo bằng chứng mới của brief R39. Mỗi hàng ở mục 3 ghi đầy đủ dòng v10, văn bản cũ, văn bản mới và bằng chứng; số vùng sửa gồm cả siêu dữ liệu và dòng EV. Mọi ký tự ngoài các vùng khai báo được giữ nguyên sau chuẩn hóa xuống dòng LF. Đảo ngược các vùng sửa khôi phục đúng toàn bộ v10.

Các tệp đã có trước khi tiếp tục được giữ nguyên. Bản tiếp tục, ứng viên, script và kết quả kiểm mới đều dùng tên `-v2`; không sửa chương khác hoặc thư mục đầu vào. `S` = `E:/Code/Report_INT3508/ridebound-scratchpad/`; `K` = `S/rewrite-2026-10/`; `W` = `S/optimize/codex-debate/codex-work/`.

## 1. Độ dài và bố cục

Đếm “tiếng” bằng bốn hàm thuần đã đọc của `W/r33-ch3v4/patch_and_check-v3.py`, chọn bằng AST mà không thực thi phần sửa tệp. Bỏ comment, lệnh cấu trúc và công thức; đếm token có chữ hoặc số cách nhau bằng khoảng trắng. Tiêu đề không tính; chú thích thuộc bảng/hình. Dùng cùng bộ đếm cho v10 và v11-v2; bộ đếm này khác bộ đếm thất lạc của NOTES v10.

@@COUNT_TABLE@@

Không thực hiện đợt cắt khoảng 695 tiếng mà R37 đề nghị theo thước 330 tiếng/trang: brief R39 và trial build đo chương 4 **21 trang so với ngân sách 26,5 trang**. Chỉ bỏ riêng câu giả thuyết chưa kiểm theo yêu cầu R37 §1.7. Giữ bốn bảng, một hình, cấu trúc 4.6–4.11, chi tiết học máy, đoạn C-120, lưu ý ba buổi sáng dùng chung nguồn, ví dụ hai khách mỗi người 17,77 giây và hạn chế không gán lại xe.

Hai hộp tràn cũ được ghi tại `main.log:1832` (**29,17484 pt**, bảng B39–59) và `:1837` (**15,8002 pt**, hình TikZ, báo tại phần caption B170–174). Bọc toàn bộ mỗi hộp bằng `\resizebox{\linewidth}{!}{...}`; mọi nội dung tabular, tọa độ, nhãn và caption giữ nguyên. `graphicx` đã nạp ở `main.tex:9`; lề trang ở `:28` cho bề rộng 16 cm. Theo bề rộng cũ, hệ số thu tương ứng khoảng **@@TABLE_SCALE@@** và **@@FIGURE_SCALE@@**. Đây là kiểm bề rộng khai báo, chưa xác nhận bản dựng hết tràn. Chỗ thứ hai là hình, dù brief gọi chung là bảng. Số trang của bản v11-v2 chưa đo.

## 2. Kiểm số và bằng chứng bổ sung

Root đã đọc mã probe R37, các phần sửa trong `agent-numbers-v1.py`, `agent-numbers-extensions-v1.py`, `agent-numbers-summary-v1.py` và kết quả JSON. Các script chỉ đọc dữ liệu đã lưu, kiểm SHA256 của khung NDJSON và tạo báo cáo độc quyền trong thư mục này; không gọi mô phỏng, học mô hình hay kiểm thử phần mềm. Root kiểm lại phép cộng theo từng kịch bản, trung bình không trọng số và phần sổ ngày thường từ các bản ghi từng khách đã trích độc lập. Các nguồn sau được đăng ký tại đây, không giả làm mã mới của sổ chung.

| Phép kiểm | Giá trị và cách gộp | Nguồn đã đọc / kết quả đã lưu |
|---|---|---|
| Dự báo ngày thường | Cùng 21 kịch bản: M⁺ 66→2 trên 1.471; V 66→2 trên 1.470; U 129→63 trên 1.512; khung 17 giờ U 28→28 trên 437, C 0 trên 418. | `agent-numbers-v1.json:forecast`; CELLS và bản ghi từng khách U/C trong `R19-stage1a-analysis.json`; N4B8-02. |
| Giá của dự báo và nhóm oracle | 13,7 / 27,8 / 3,2 giây là trung bình theo kịch bản của 21 kịch bản. Nhóm oracle có 2.305/2.305 khách khớp trong 2 giây trên cả 34 kịch bản. | `.json:forecast_oracle_and_price`; CELLS; F06/F10. |
| Luật C và đệm | 34×108 = 3.672; U phục vụ 2.434, C phục vụ 2.338, chênh 96. U có 174 khách bị dời, lớn nhất 590,133 giây; C lớn nhất 29,239 giây. Cận thiết kế là 30 giây dưới giả thiết (N). | `.json:padding,cohort_totals`; từng khách của bộ trích độc lập Codex; C20/N-23/N-28/A06/A22/K05. |
| Các hàng so đệm | U+đệm30 và C không đệm: không trễ60 là 2.328/2.328, không trễ120 là 2.366/2.338. Khi cùng đệm30, C có 2.336/2.338. Kéo dài lời hứa trung bình 37,183331 / 7,367123 giây, tỉ số 5,047198. | `.json:padding,cohort_totals`; tính đệm trên từng khách, ngưỡng trễ lớn hơn hẳn. Hai tập khách khác nhau. |
| Khách đi chung | U 555/2.434; C 313/2.338; chênh 242. | `.json:cohort_totals.shared_read_counts`; đọc lại `K/evidence/checks-addendum-1/recompute-addendum-1-2026-10-11.txt:136–140` rồi trừ. Đây vẫn là kết quả theo một quy tắc đếm, không phải đếm raw độc lập mới. |
| Quyết định bị ép khi đưa dự báo vào điều phối | C hoàn tất 14/16; M⁺ 15/16; 3/32 lần dừng; K=2. Cùng 15 kịch bản M⁺: có dự báo 3.849/8.496, không dự báo 5.121/8.468. Trung bình theo kịch bản là 47,61589255% / 62,77032087%; các phân số gộp đo đại lượng khác. | `.json:dispatcher`; đếm mới raw của 30 lần M⁺ và 14 lần C hoàn tất, đối chiếu từng hàng BIC và cấu hình K2. |
| Khách bị hạn chót phá lời hứa ở khung 7 giờ | Cùng tám kịch bản: không dự báo 170/442, có dự báo 45/439. Trung bình theo kịch bản 39,04771018% / 10,99224586%, khác tỉ lệ gộp 38,46% / 10,25%. | `.json:morning_promise_breaks`; 16 raw transcript, giờ tới so với lời hứa đầu của từng luật; ngưỡng >30 giây. `agent-numbers-summary-v1.json:dispatcher_morning` ghi riêng hai cách gộp. |
| Nghĩa vụ gốc trên 34 kịch bản | M⁺ bị ép 7.710/20.103, trung bình theo kịch bản 41,31136648%; 28/34 kịch bản có khách phá lời hứa. C: 0/20.101 quyết định bị ép, 0 khách vượt trần; C-120: 0/20.435; U: 0/20.760. | `.json:main_original_obligation,cohort_totals`; đọc mới 68 cache IVC và gộp bản ghi từng lần chạy; N-21/X3-16/R36-A01. |
| Số đếm học máy | Giữ 2→1/145; 1→1/200; 0/147; 0/197; 104→94/807; sớm 57/807. Các số là suy từ tỉ lệ gộp đã làm tròn. | `.json:ml`; `ml_pilot_run.py:37–42,175–176` xác nhận cách gộp và làm tròn ba chữ số. Xét mọi số nguyên tương thích, không thực thi mô hình. |
| Hình sổ ngày thường | 68 khách trễ trên 21 kịch bản; tổng 6.217,406 giây, phần dự báo 5.352,646482885 giây, tỉ số 86,09131337%→86,1%. Nhãn nguyên giây: 82+5.353+783 = 6.218 so với nhãn tổng 6.217. | `agent-numbers-summary-v1.json:forecast_ledger`; `root-qa-v2.json:weekday_ledger`; F09/N4B8-11. Sai khác nhãn là 1 giây. |
| Kiểm thử phần mềm | Một lần đầy đủ ngày 13/10/2026: 0 lỗi, 1.025 đạt, 0 bỏ qua, tổng 1.025, chín dự án, exit 0. Có điều kiện LF và tệp chưa ghi nhận. | `.json:test_attempt4`; `K/evidence/TESTRUN-45f8026-2026-10-12.md:18`, attempt 4; log `testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log`. R39 chỉ đọc log. |

Đính chính ghi chú N4B8-03/NOTES theo R37: **Với từng dòng được dùng, phép kiểm xét mọi số nguyên từ 0 đến số khách và chỉ tìm được một số phù hợp với sai số làm tròn 0,0005 điểm phần trăm. Cận sai số của số đếm lớn nhất là 0,004035 khách ở mẫu số 807. Điều kiện cận nhỏ hơn 1, xét riêng, không đủ để kết luận về số nguyên phù hợp.** Phép kiểm này không kiểm trích đặc trưng, học hay dự đoán.

Phép cộng chiều tuyết có giới hạn giữ nguyên 886,9 giây / 25,7% và 2.299,0 giây / 66,7%; chỉ làm rõ chặn dưới 0 theo `rider_nowcast_replay.py:14–15,113–114`. Các số không biến thành thành phần có dấu của công thức sổ. Danh tính bộ chạy tuyết đã được probe đọc lại; phần A v5-v3 cũng đã bỏ lưu ý cũ về danh tính chưa kiểm.

## 3. Một hàng cho mỗi thay đổi

@@CHANGE_ROWS@@

## 4. Bao phủ nhận xét và quyết định dùng bằng chứng mới

| Yêu cầu | Xử lý |
|---|---|
| R37 §1.1 | Tách cận 30 khỏi mức đo 29,2; so phần kéo dài gần bằng; bỏ ý mức đệm bắt buộc; giới hạn kết luận ở C-30. |
| §1.2 | Khôi phục mẫu số trên 21 kịch bản; oracle thuộc 34; làm rõ phạm vi của trung bình 13,7 giây. |
| §1.3 | Nêu nguồn suy số đếm học máy, bỏ tiếng Anh ngoài ngoặc; ghi chú chứng minh làm tròn được sửa ở mục 2. |
| §1.4 | Thêm số gộp M⁺ trên 15 kịch bản; giữ 41,3% với nhãn trung bình và ghi riêng 7.710/20.103. Bảng phần A báo số gộp nên không mâu thuẫn. |
| §1.5 | Phần A mới đã sửa danh tính tuyết; Appendix C đã có nên giữ ref. Attempt 4 mới hơn R37 thay kết quả kiểm thử cũ; các chỗ ở Ch3/phụ lục giao mục 5. |
| §1.6 | Áp câu “phép thử này là một hướng phát triển còn mở”. Ch5 v2 nay tồn tại và đã đặt phép thử lên đầu, nên không lặp lý do thiếu Ch5 cũ. |
| §1.7 | Không cắt để đạt thước trang cũ; bỏ riêng câu giả thuyết được reviewer yêu cầu. Giữ đầy đủ lời về dữ liệu đã xem và thêm phạm vi thử 120 giây. |
| §1.8 | Thêm giới hạn kiểm số học học máy và thiếu phép kiểm độ nhạy theo hạt giống. |
| §1.9–10 | Nêu chặn dưới 0; sửa sai khác giữa các nhãn nguyên giây thành 1 giây. |
| R36 §5 | Cập nhật tên phần A; thêm số gộp quyết định và khách khung 7 giờ; bổ sung sổ hợp lệ và (N) ở mọi lượt; attempt 4; kể cả các phép tính thử ở 120 giây. |

Không thêm phép so 2.207 khách chung của R37 §5 vì đó là lựa chọn tùy ý. Giữ cảnh báo hai nhóm khách và số giao; lý do cũ “chưa có output” của L-33/L-52 đã được R37 giải quyết và không được dùng lại. Giữ các hạn chế về phương án chưa chạy, không nhập kết quả giả định.

## 5. Việc còn thuộc chương khác

1. **Ch3 v4-v3:706–707:** thay câu bắt đầu “Vì vậy bộ sinh…” bằng: `Vì vậy bộ sinh không xét hết mọi phương án; mục~\ref{muc:c4-hople} báo các bộ đếm đã đọc của bộ sinh. Các số này không đo mọi giới hạn của bước sinh, kiểm và giải.` Giữ câu duyệt mười chiều và đếm đảo thứ tự. R37 §1.5; N4B8-13/N-25; assembly row 7.
2. **Ch3:724:** đổi ngày 12/10 thành 13/10. **:737:** đổi bằng chứng lượt 3/3b thành attempt 4 và log đầy đủ ngày 13/10. Câu 1.025 cùng điều kiện LF/tệp chưa ghi nhận đã đúng theo attempt 4; không đổi lại thành kết quả cộng hai lượt riêng của R37 cũ.
3. **Phụ lục C r31-v2:119–120:** thay kết quả hai lượt riêng bằng: `Ngày 13/10/2026, toàn bộ 1.025 trong 1.025 kiểm thử trên \texttt{45f8026} đạt trong một lần chạy đầy đủ, với kiểu xuống dòng LF và một tệp chưa ghi nhận trong cây làm việc. Một kiểm thử đòi cây làm việc có tệp như vậy; kết quả cần cả hai điều kiện môi trường này.` Chuyển EV sang attempt 4/log đầy đủ. Giữ nhãn C ở dòng 60; nếu kể các lượt cũ thì phân biệt chúng là lịch sử.
4. **Ch3:467:** việc tồn tại trước ở assembly row 6 vẫn cần đổi “vế cộng dồn” thành “phần cộng dồn”. Không sửa Ch3 trong vòng này.
5. **Người ghép:** chọn B v11-v2 và A v5-v3, Ch3 v4-v3 với các đính chính trên, phụ lục v2 và danh mục v2. Cập nhật assembly notes về bản B, ngày kiểm thử và các nhãn phụ lục đã tồn tại; dựng kiểm lại hộp tràn. Không còn việc sửa danh tính tuyết của A hay thứ tự hướng phát triển của Ch5.
6. **Registrar:** có thể nhập các phép suy và đính chính cận làm tròn ở mục 2 vào sổ/ghi chú phụ lục. R39 không ghi đè các hồ sơ đó.

## 6. Kiểm tra và giới hạn

`root-qa-v2.json` lưu SHA256 đầu vào, phép đảo vùng sửa, kiểm ngoặc/môi trường/dấu toán, phép gộp số và từng tham chiếu. **@@REF_COUNT@@ lần ref/eqref, @@REF_TARGETS@@ target phân biệt, 0 không định nghĩa, 0 nhãn trùng** trong B v11-v2 + A v5-v3 + Ch3 v4-v3 + phụ lục v2. Giữ đủ 11 nhãn của B. Ba khóa cite cũ `engelhardt2026`, `horl2022`, `schulz2026` có trong danh mục v2; không thêm khóa.

Root kiểm đầu ra số của sub-agent trước khi áp, rồi kiểm lại ứng viên và nhật ký bằng kiểm độc lập cuối. Không chạy build, mô phỏng, học mô hình, cài đặt hay kiểm thử phần mềm mới. Chưa chứng nhận số trang v11-v2, bản ghép biên dịch, tính đúng toàn bộ quá trình học máy, độ nhạy hạt giống hoặc hiệu quả ngoài đời. Các việc bàn giao ở mục 5 cần thực hiện khi ghép.
