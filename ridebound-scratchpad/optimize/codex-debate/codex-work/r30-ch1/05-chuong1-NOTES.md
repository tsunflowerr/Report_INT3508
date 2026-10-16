# Round 30 — ghi chú Chương 1

## 0. Bản dùng để ghép và phạm vi thao tác

**Bản dùng để ghép: `05-chuong1-v3.tex`.** `05-chuong1.tex` và `05-chuong1-v2.tex` được giữ nguyên. Tên NOTES không có hậu tố vì tệp này được tạo một lần, sau khi chốt v3; nội dung mô tả v3. Không ghi đè bất kỳ tệp nào.

Đã đọc lại `ROUND30-CH1-WRITER.md` sau hai lần tiếp tục; không thấy phụ lục mới. Đã đọc quy tắc song song, WRITING-BRIEF, OUTLINE-V2 §2/Chương 1/§6, REVIEW-DECISIONS-R20, STYLE-GUIDE-VI, GLOSSARY-VI-v2, sổ chính và các phụ lục 1–4; mở phụ lục 1 §0 trước khi dùng các số. Đối chiếu Chương 3 v3 và NOTES §7.8, Chương 4A v4 và NOTES, Chương 4B v7 cùng kiểm chứng R27, C120-RESULTS và Chương 1 hiện tại. Chương 2 v4 và phụ lục 5 nay có sẵn nên được đọc thêm để khép bằng chứng Elmi và Mt-KaRRi. Đọc các đoạn về cách đệm trong NOTES sửa phần B; không lấy các số mới ngoài tập bằng chứng đã ghi dưới đây.

Mọi tệp mới nằm trong `codex-work/r30-ch1/`. Không mô phỏng, biên dịch, cài đặt, sửa luận văn, sửa bản nháp chung hay ghi vào mã nguồn. Chỉ có văn bản nhỏ và script kiểm tĩnh/đếm chữ. Các script mở đầu ra bằng mode `x`.

## 1. Độ dài và ngân sách

“Từ” trong yêu cầu được đếm theo **tiếng cách nhau bởi khoảng trắng**, như hướng dẫn văn phong. Bỏ dòng chú thích, tiêu đề chương/mục, bảng, hình và các lệnh nhãn/trích dẫn/tham chiếu; giữ văn xuôi, các gạch đầu dòng và chữ trong khung. Vì vậy số trang thật còn phải tính phần hình, bảng, tiêu đề và khoảng cách.

| Phần | Ngân sách trang | Ngân sách văn xuôi xấp xỉ, 330 tiếng/trang | Tiếng v3 | Phần chiếm chỗ thêm |
|---|---:|---:|---:|---|
| Mở chương | 0,25 | 83 | 52 | Tiêu đề chương |
| 1.1 Bối cảnh | 1,50 | 495 | 332 | H1.1, hai trục thời gian |
| 1.2 Ba phần và câu hỏi | 1,25 | 413 | 381 | H1.2 và ba nhãn câu hỏi |
| 1.3 Công trình gần nhất | 1,25 | 413 | 119 | Bảng 1.1, bảy hàng nội dung |
| 1.4 Mục tiêu và đóng góp | 1,75 | 578 | 572 | Danh sách và khung; chữ đã tính trong 572 |
| 1.5 Phạm vi | 0,75 | 248 | 196 | Danh sách có nhãn |
| 1.6 Cấu trúc | 0,25 | 83 | 48 | — |
| **Tổng** | **7** | **2.310 trước khi trừ chỗ hình/bảng** | **1.700** | Hai hình, một bảng |

Ngân sách từng hàng được làm tròn riêng, nên tổng các hàng làm tròn không bằng đúng 2.310. Đoạn đóng góp, không tính nhãn in đậm, là **325 tiếng**. Nó dài hơn mục tiêu khoảng 300 tiếng vì giữ so sánh 292/2.338–289/2.338, giả thiết (N), đối chứng không trần và các vế bất lợi mà brief yêu cầu.

Đã rút 1.4 từ 744 tiếng ở bản đầu xuống 572 ở v3. Tổng văn xuôi giảm từ 1.865 xuống 1.700. Tính theo thước brief, 1.700/330 ≈ 5,15 trang văn xuôi; phần còn lại của ngân sách dành cho hai hình, bảng và định dạng. **Chưa đo bố cục bảy trang bằng bản dựng.** Không thu nhỏ cỡ chữ thân bài hay giãn dòng. Bảng dùng cỡ chữ bảng, như các chương đã có; chưa có kiểm tra trực quan về khoảng trắng hoặc vị trí hình.

Đầu ra đúng của bộ đếm cuối: `05-chuong1-v3-QA.txt`, script `verify_ch1_v3.py`. `05-chuong1-v2-QA.txt` có lỗi ở riêng bộ đếm đoạn đóng góp: nó tìm một câu dẫn đã đổi tên nên đếm cả phần sau; giữ tệp và dùng kết quả sửa ở `05-chuong1-v2-QA-v2.txt`. Lỗi đó không tác động đến số tiếng từng mục. Không dùng số 845 trong đầu ra cũ.

## 2. Nhãn và tham chiếu

| Vai trò | Nhãn định nghĩa |
|---|---|
| Chương | `chuong:modau` |
| 1.1 | `muc:c1-boicanh` |
| 1.2, điểm đến của Chương 4A | `muc:c1-cauhoi` |
| 1.3 | `muc:c1-lienquan` |
| 1.4 | `muc:c1-donggop` |
| 1.5 | `muc:c1-phamvi` |
| 1.6 | `muc:c1-cautruc` |
| H1.1 | `hinh:c1-loihua` |
| H1.2 | `hinh:c1-baphan` |
| Bảng 1.1 | `bang:c1-chodung` |

Nhãn được kiểm có trong Chương 2 v4: `chuong:coso`. Trong Chương 3 v3: `chuong:phuongphap`, `muc:luatc`, `muc:giunguyen`, `muc:dubao`, `muc:so`. Trong Chương 4A v4: `chuong:thucnghiem`, `muc:c4-ketqua`, `muc:c4-dieuphoi`, `muc:c4-chontran`, `muc:c4-congdon`. Trong phần B v7: `muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet`, `muc:c4-hople`.

**Còn phụ thuộc khi ghép:** `chuong:ketluan` là nhãn ROUND31 yêu cầu người viết Chương 5 định nghĩa; chưa có bản Chương 5 để kiểm trong thời điểm kiểm cuối. Không gõ số chương/mục bằng tay. Các số công thức 7 của Hörl–Zwick chỉ công thức trong nguồn ngoài, không phải tham chiếu nội bộ.

## 3. Mỗi số liệu in trong chương và bằng chứng

Các ID không có tiền tố riêng thuộc EVIDENCE-REGISTER; N-xx thuộc phụ lục 1; X3-xx thuộc phụ lục 2; N4B-xx thuộc phụ lục 3; C4A-xx thuộc phụ lục 4; C2-xx thuộc phụ lục 5 mới của Chương 2. Không dùng hàng UNVERIFIED làm bằng chứng.

| Số hoặc nhóm số in | Đơn vị, tập và cách gộp | ID / đầu ra |
|---|---|---|
| 307,3 = 99,1 + 208,2 giây; trần 300 giây | Một khách cực đại của kịch bản phát triển ngày 13/11, không phải tập kiểm tra chính | D06; N-30; W07:48–54; Q4R |
| Trần 30 giây: cực đại 99,1, phần giữ kế hoạch 97,1 giây | Khách khác trong cùng kịch bản, không phải cùng khách ở trần 300 | N-30; Q4R |
| 13/11/2018, khung 7:00–9:00 | Ngày/khung của kịch bản phát triển dùng trong hình trên | D06; N-30; W07 |
| Đặt 7:11:56; đón 7:22:30; lời hứa đầu 7:34:51; dự báo 7:37:44; tới 7:38:02 | Khách mô phỏng rq-30b7e083c7b, ngày 15/11/2018, khung 7:00–9:00; đồng hồ làm tròn tới giây | C31; EXAMPLE:1–4,60–61 |
| 190,5; 172,9; 17,6 giây | Độ trễ ban đầu; mức kéo dài bởi dự báo; độ trễ so với dự báo, tính trước làm tròn đồng hồ | C31; EXAMPLE:60–61 |
| 0 trên mỗi trục H1.1 | Mốc quy ước là lời hứa đầu của từng khách; không phải giờ tuyệt đối | Định nghĩa trục; C31; D06 |
| 134 trong 203 khách | Giao giữa nhóm trễ >60 giây và nhóm từng bị điều phối dời, trong điều phối không trần | C21; C06 |
| 73,4%; 23.027 trên 31.353 giây; 203 khách | Tỉ số hai tổng có dấu, gộp trên **toàn bộ 203 khách trễ >60 giây**, không chỉ 134 khách giao nhau | C24; C4A-03; tổng chính xác 23.027,239 / 31.353,407 giây |
| 590,1 giây, gần mười phút | Tổng độ lớn các lần dời điều phối lớn nhất của một khách không trần | C20 |
| 34 kịch bản; 3.672 yêu cầu | 108 yêu cầu mỗi kịch bản; cùng mẫu số trên yêu cầu cho mỗi cấu hình | B09 |
| Trần 30 giây; từ khi xác nhận đặt xe | Trần cả chuyến cho từng khách có lời hứa, không cấp lại mỗi lần | A06; A13; X3-20 |
| 96 lượt ít hơn | 2.434 − 2.338, số đếm trên 3.672 yêu cầu; hai tập khách khác nhau | C01; C02; C04 |
| 31 lượt thêm; 2.231 và 2.262 lượt | Không trễ >60 giây so với lời hứa đầu không dự báo, trên 3.672 yêu cầu | C08; C06 |
| 28 trong 34 kịch bản | Luật hạn chót 30 giây có ít nhất một khách tới sau lời hứa đầu không dự báo quá 30 giây | N-21; C13; C4A-01 |
| 0 trong 20.760 quyết định | Không trần, quyết định được xác nhận cho cả đội xe, không phải số khách | X3-16 |
| 292 trong 2.338 (12,5%); 289 trong 2.338 (12,4%) | Luật C và luật hạn chót; cùng ngưỡng trễ >30 giây so với lời hứa đầu **không dự báo**; gộp theo khách | C4A-01; giá trị chưa làm tròn 12,49% / 12,36%; C04 (tập khách khác nhau) |
| 2.434; 2.338; 2.338 lượt phục vụ; 2.332 lượt chung | Không trần; luật C 30 giây; hạn chót 30 giây, trên 3.672 yêu cầu; lượt chung của C và hạn chót | C01; C04 |
| 555 trong 2.434; 313 trong 2.338 khách đi chung | Không trần / C 30 giây, gộp theo khách; không đổi thành tỉ lệ trên yêu cầu | N-09 |
| Đệm 30 giây; cùng 2.328 lượt ở một phút | C 30 giây có dự báo / không trần có dự báo cộng đệm, trên 3.672 yêu cầu | C10; N-16 |
| 2.338 / 2.366 lượt ở hai phút | C có dự báo / cách đệm có dự báo; trên 3.672 yêu cầu; cách đệm nhiều hơn | C10; N-16 |
| 37,2 / 7,4 giây | Trung bình kéo dài lời hứa đầu: cách đệm / C; gộp trên 2.434 / 2.338 khách được phục vụ | C10; N-16; N-18; 37,183331 / 7,367123 giây |
| 4 trong 2.338 / 44 trong 2.434 | Khách tới sớm >60 giây: C có dự báo / cách đệm có dự báo | N-16; N4B-09 |
| Trần 120 giây; 2.387 lượt | C 120 giây, cùng 34 kịch bản, 3.672 yêu cầu | N-06 |
| 2.255 / 2.366; 2.322 / 2.379 lượt | Không trễ >60 / >120 giây, C 120: chưa dự báo / có dự báo; mẫu số trên yêu cầu là 3.672 | N-06; N-16; C120R:14–15 |
| 7,3 giây trên 2.387 khách | Mức kéo dài lời hứa đầu có dự báo của C 120, trung bình gộp | N-06; N-16; giá trị chính xác 7,273885 giây |
| 132 = 98 + 34 lần chạy; 3 trong 1.780 bản ghi; 120 giây | Tập lần chạy C đã kiểm toàn bộ bản ghi chặn; cả ba bản ghi chỉ do cộng dồn ở trần 120 | N-15; N-08; E01; phụ lục 1 §0.3 |
| FleetPy 1.0.2; 96 nút | Phiên bản mô phỏng và đồ thị cặp điểm, không phải mạng đường phố đầy đủ | B01; B03; K48 |
| 108 yêu cầu; 8 xe; 4 chỗ; 600 giây; 1,5 lần | Cấu hình thử; 600 giây kể từ lúc gọi; giới hạn ngồi xe so với đi thẳng | B02; B03 |
| 15 phút; 00:00 | Khung thay đổi hệ số chung toàn thành phố; mốc tốc độ nền | B06; B07 |
| 14–18/11/2018; năm ngày; 34 kịch bản | Phạm vi tập chính; có chồng yêu cầu, không độc lập | B08; B09; B11; I05 |
| 2020/2022/2026 và công thức 7 trong Bảng 1.1 | Năm tài liệu / số công thức ngoài; không phải số thực nghiệm | J06–J10; C2-04; C2-08; C2-09; X3-40; metadata mục 5 |

Một phút và hai phút trong chương lần lượt là ngưỡng **60** và **120** giây. Khách trễ khi độ lệch **lớn hơn** ngưỡng; không trễ khi **không lớn hơn**, không loại khách tới sớm. Các số trên yêu cầu bao gồm cái giá của việc không phục vụ; không phải tỉ lệ chỉ trên khách được chở.

**Khóa nguồn mở trực tiếp:**

- `Q4R`: `S/tang3/w07/analysis/q4-rider-2026-09-30.txt`, kịch bản d20181113-s10-r1-w07. Cực đại C-300: rq-a019727097c; cực đại C-30: rq-f33d8bc2f39. W07-REPORT trỏ đúng tệp này. Vì vậy không vẽ hai cực đại như một người.
- `EXAMPLE`: `S/optimize/report-extras/example-rider-2026-10-06.txt`, khách rq-30b7e083c7b của d20181115-s10-r1-w07.
- `C120R`: `S/tang3/t38c120/C120-RESULTS.md`, chỉ dùng bảng số đo và thông tin đã kiểm của N-06; không đưa phần lịch sử tổ chức nghiên cứu vào chương.
- `CK4A`: `S/rewrite-2026-10/evidence/checks-ch4a-v2/`, đặc biệt `ledger-share-sums-2026-10-12.txt` và `check-ch4a-v2-2026-10-12.txt`, theo C4A-01/C4A-03.

Các tọa độ thập phân trong TikZ là thông số vẽ, không phải số liệu mới. H1.1 dùng hai tỉ lệ riêng: hình trên khoảng 0,031 cm/giây, hình dưới khoảng 0,046 cm/giây; làm tròn tọa độ tới 0,001 cm. Hình ghi rõ tỉ lệ riêng và số giây. Các đoạn hình trên là **tổng các phần**, không phải giờ của một phép chiếu đơn lẻ hay tuyến phản thực tế của cả chuyến.

## 4. Bảng phụ cho các mệnh đề chịu lực của đoạn đóng góp

| Mệnh đề | Bằng chứng và giới hạn |
|---|---|
| Trần từ lúc xác nhận, cả chuyến, phương án vượt bị loại | A06; A13; X3-20: khách được nhận nhưng chưa xác nhận chưa có lời hứa, nên chưa được kiểm trần |
| So với tuyến cũ tính lại ở cùng trạng thái | A01; A02; X3-27; không suy ra quan hệ nhân quả |
| Kế thừa Hörl–Zwick; trần chung không nới theo giao thông | J01; J03; J05; C2-04; phần đối chiếu khác biệt là suy luận từ hai định nghĩa |
| Luật C không bị ép dưới (N) và phần đã dùng ≤ trần | A22; X3-27; Chương 3 mục `muc:giunguyen`; không bảo đảm mọi ràng buộc cấu trúc đều hợp lệ |
| Không trần cũng không bị ép | X3-16; không trình bày 0 quyết định bị ép như lợi thế của C trước không trần |
| Hạn chót tính cả giao thông; C không tính | A09; A10; N-21; hai nghĩa vụ khác nhau, không dùng 0 vi phạm trần C làm bằng chứng giữ giờ đến tốt hơn |
| C không hơn ở lời hứa đầu +30 giây trên tập đã đo | C4A-01: 292/2.338 và 289/2.338; không khái quát sang mọi ngưỡng hay mọi tập |
| Đệm hòa một phút, hơn hai phút và kéo dài lời hứa hơn | C10; N-16; N-18; phát lại lời hứa trên chuyến cố định, hai tập khách khác nhau |
| Cộng dồn có ba bản ghi riêng ở trần 120 | N-15; N-08; 132 lần chạy là tập đã kiểm, không phải mọi lần chạy có hệ số đo được |
| Tác dụng riêng lên kết quả chưa đo | E09; chưa có đối chứng cấp lại trần mỗi lần |
| Giá trị cho người đọc: giới hạn điều phối riêng từng khách, không cần dự báo đúng | A06; A22; X3-12; giới hạn này vẫn cần các giả thiết triển khai đã nêu; cái giá đo được là C02 |

## 5. Trích dẫn và siêu dữ liệu

Các khóa có trong luận văn hiện tại: `fielbaum2020`, `schulz2026`, `elmi2026`, `alonsogonzalez2020`. Các khóa mới dưới đây dùng chung với Chương 2/3, **không tạo bản ghi thứ hai** khi ghép. Metadata kiểm trong `06-chuong2-BIB.md`, phụ lục 5 và X3-40.

| Khóa mới | Siêu dữ liệu đã kiểm | Bằng chứng |
|---|---|---|
| `horl2022` | S. Hörl, F. Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling*. 2022. Conference paper, ETH Zurich Research Collection. DOI: https://doi.org/10.3929/ethz-b-000561639. **Tên hội nghị chưa xác nhận ở bộ nguồn dùng; không điền.** | X3-40; C2-01; PDF HZ và DataCite theo BIB |
| `laupichler2026` | M. Laupichler, R. Andre, K. Kandler, P. Sanders, P. Vortisch. *Advancing dynamic ride-pooling simulation – a highly scalable dispatcher*. arXiv:2605.11798v1, 2026. DOI: https://doi.org/10.48550/arXiv.2605.11798. Bản tiền ấn, không có tên tạp chí đã kiểm. | C2-09; arXiv và PDF MTK |
| `hu2022` | X. Hu, T. Binaykiya, E. Frank, O. Cirit. *DeeprETA: An ETA post-processing system at scale*. arXiv:2206.02127v1, 2022. DOI: https://doi.org/10.48550/arXiv.2206.02127. Bản tiền ấn. | C2-15; arXiv và PDF DRE |
| `wardman2026` | M. Wardman, P. Murphy, M. Ojeda-Cabral, A. Mitrani, K. Neki, R. M. Humphreys. *Value of time multipliers for walk time, wait time, service headway, displacement time, reliability and congested travel time: review and meta-analysis of worldwide evidence*. Transportation Research Part A: Policy and Practice 207:104925, 2026. DOI: https://doi.org/10.1016/j.tra.2026.104925. | C2-17; PDF WAR và Crossref theo BIB |

Khóa `alonsogonzalez2020` có lỗi tác giả ở danh mục cũ. Danh sách đúng đã kiểm: M. J. Alonso-González, N. van Oort, O. Cats, S. Hoogendoorn-Lanser, S. Hoogendoorn. *Value of time and reliability for urban pooled on-demand services*. Transportation Research Part C: Emerging Technologies 115:102621, 2020. DOI: https://doi.org/10.1016/j.trc.2020.102621 (C2-18). Người ghép dùng đính chính của Chương 2/vòng 32; chương này không sửa danh mục gốc.

Elmi: A. Elmi, E. Moylan, J. Alonso-Mora, A. Fielbaum. *Improving ridepooling reliability using shareability shadows*. Transportation Research Part C: Emerging Technologies 192:105897, 2026. DOI: https://doi.org/10.1016/j.trc.2026.105897. C2-08 mở bản xuất bản cuối ở kho TU Delft và nâng J12 khỏi UNVERIFIED. Dùng mệnh đề định tính về bảo đảm cho khách được chọn; không dùng các tỉ lệ từ tóm tắt.

Hörl–Zwick chỉ xuất hiện dưới tên tác giả/năm và khóa `horl2022` trong chương; không có chi tiết nơi công bố. Không trích nhầm `fleetpy2022` thành bài FleetPy năm 2026. Tên dịch vụ UberX Share/MOIA Express là ví dụ định tính theo J28/J31, không phải khẳng định về tình trạng sản phẩm hiện tại hay hợp đồng có hiệu lực.

## 6. Lệch so với OUTLINE và lý do

1. **H1.1 giữ hai khách của OUTLINE, không dùng lần tay R26.** Hai ví dụ cho thấy phần điều phối và vai trò dự báo bằng các độ lệch đủ lớn để người đọc ngoài ngành thấy rõ. Lần tay R26 rất tốt cho Chương 3 nhưng nhiễu dưới 0,25 giây khó minh họa vấn đề lời hứa ở Chương 1. Chỉ vẽ cực đại C-300 trong hình trên; cực đại C-30 viết trong đoạn dẫn vì đó là người khác.
2. **H1.1 dùng trục tương đối và giờ đồng hồ làm tròn.** Tránh phép trừ 7:38:02 − 7:34:51 cho 191 giây rồi hiểu nhầm số chính xác 190,5. Các số 172,9/17,6 lấy trước làm tròn. Không diễn giải tổng phần giữ kế hoạch như giờ của một tuyến phản thực tế duy nhất.
3. **Bảng 1.1 giữ bảy hàng nhưng rút chữ.** Cột làm gì và đại lượng gộp vào một cột, giữ bốn cột như OUTLINE. Elmi và Mt-KaRRi được giữ vì phụ lục 5 nay có bằng chứng sơ cấp. Mức trần/độ chùng của các bài để Chương 2 giải thích.
4. **Đoạn đóng góp dài 325 thay vì khoảng 300 tiếng.** Giữ mọi đính chính R30. Câu về không bị ép có điều kiện và đối chứng không trần; số tới sau lời hứa đầu dùng cùng thước cho C và hạn chót. Không quảng bá tính chất này như lợi thế giữ giờ đến.
5. **Bảng phụ §6.2 ở NOTES, không in trong chương.** Nó là bảng truy bằng chứng; in trong thân bài sẽ thêm mã nội bộ và lặp nội dung. Bảng đối chiếu nghiên cứu vẫn có trong chương.
6. **Khung “không nhận là mới” viết ngắn bằng văn xuôi.** Các hàng kế thừa/làm khác đã có ở Bảng 1.1 nên không lặp lại bảng thứ hai trong khung. Giữ phủ định về giờ đến, kinh doanh và hài lòng.
7. **Năm dòng kết quả được rút chữ và số lặp.** Không lặp lại 203/76 khách trễ trong danh sách vì số không trễ/đánh đổi và phần phân tích được giữ; chi tiết đầy đủ thuộc Chương 4. Vẫn giữ phục vụ, số lượt chung, đi chung, hai ngưỡng khi có dự báo, tới sớm, C-120 và tập kiểm cộng dồn.
8. **Tập cộng dồn chọn 132/1.780/3 của OUTLINE**, mô tả rõ tập đã kiểm. Không thay bằng 140/1.943/3 có chiều tuyết vì không cần mở rộng phạm vi câu mở chương; không nói đây là mọi lần chạy dùng hệ số đo.
9. **Giá trị cho hãng xe/khách là một giới hạn kiểm được**, có cái giá phục vụ, không chuyển thành kết quả kinh doanh hoặc hài lòng. Ba phần là phép tính theo mô hình, không phải ba nguyên nhân.

## 7. Bằng chứng còn thiếu và câu hỏi mở

- **Bố cục thật:** chưa có bản dựng để xác nhận đúng bảy trang, vị trí hình/bảng, dòng tràn và tham chiếu sau khi ghép. Brief cấm build; người ghép cần kiểm sau cùng. Không có gói mới phải thêm; TikZ `arrows.meta`, booktabs, enumitem và khungy đều đã có trong main.tex.
- **Cộng dồn:** chưa có nhánh mỗi lần một trần, nên không biết ba bản ghi riêng làm đổi kết quả cuối như thế nào. Không viết thêm tác dụng chưa đo.
- **Giá trị thực tế:** chưa có dữ liệu về hãng xe/khách coi trọng giới hạn này đến mức nào hoặc chấp nhận mất phục vụ bao nhiêu (I07/I10). Không quy ra tiền hay mức hài lòng.
- **Tên hội nghị của Hörl–Zwick:** còn chờ vòng 32 ở bộ nguồn dùng. Không có chi tiết đó trong chương.
- **Nhãn Chương 5:** người viết ROUND31 phải định nghĩa `chuong:ketluan` khi ghép.
- **Dự báo trong bộ điều phối và thứ tự bộ chọn khác:** không dùng kết quả của chúng để củng cố đóng góp mở đầu. Dự báo chính ở đây là phát lại lời hứa, không đổi các chuyến đã ghi; tác dụng riêng của một thứ tự chọn khác chưa được suy ra.

Ba điểm còn ít chắc nhất: (1) khớp đúng bảy trang sau khi dựng; (2) tác dụng riêng của cộng dồn lên số lượt cuối; (3) mức hãng xe/khách đánh giá giới hạn riêng từng người so với cái giá phục vụ. Hai điểm sau là giới hạn bằng chứng đã nêu, không phải nghi ngờ các số đã kiểm.

## 8. Kiểm cuối

`verify_ch1_v3.py` đọc tệp, không biên dịch: ngoặc và môi trường khớp; không nhãn trùng; không có cụm bị cấm; có đủ hai hình, một bảng và 35 dòng `% EV:`. Mọi tham chiếu ngoài được tìm thấy trong các chương hiện có trừ nhãn kết luận đã được brief ROUND31 quy định. Bộ đếm in đúng 52/332/381/119/572/196/48; tổng 1.700; đoạn đóng góp 325.

Các lượt kiểm đọc riêng của người hỗ trợ đã đối chiếu số deadline, cách đệm, giả thiết (N), nguồn nghiên cứu và chiều rộng hình/bảng. Người viết kiểm lại các đính chính trước khi đưa vào v3. Không coi kiểm tĩnh là kiểm bố cục trực quan.
