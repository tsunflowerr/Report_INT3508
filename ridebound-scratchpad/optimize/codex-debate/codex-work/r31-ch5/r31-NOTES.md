# Round 31 — Chương 5 và phụ lục

Bản dùng để ghép: **10-chuong5-v2.tex** và **11-phuluc-v2.tex**. Hai tệp không hậu tố giữ nguyên làm bản đầu; không dùng để ghép. Tệp NOTES này mô tả v2.

Mọi tệp của lượt này được tạo mới bằng chế độ độc quyền trong `codex-work/r31-ch5/`; không ghi đè, không sửa nguồn, không mô phỏng, không biên dịch, không cài đặt. Brief được đọc lại ở mỗi lần tiếp tục, bản đọc cuối ngày 13/10/2026 không có phần bổ sung.

## 1. Độ dài

Đếm bằng `r31-qa-v2.py` → `r31-qa-v2.json`. “Tiếng” là đơn vị cách nhau bởi khoảng trắng sau khi bỏ chú thích, lệnh cấu trúc, trích dẫn/tham chiếu và biểu thức toán. Bảng, chú thích bảng được đếm riêng; số đếm của bảng cũng bỏ biểu thức toán nên không dùng thay cho số dòng bố cục.

| Mục | Tiếng văn xuôi | Chữ bảng, chú thích bảng | Ngân sách outline |
|---|---:|---:|---|
| Mở Chương 5 | 35 | 0 | Trong 3 trang của chương |
| 5.1 Tổng kết theo ba phần | 492 | 0 | 1,5 trang |
| 5.2 Hạn chế | 169 | 0 | 0,5 trang |
| 5.3 Hướng phát triển | 271 | 0 | 1 trang |
| **Chương 5** | **967** | **0** | **3 trang** |
| A. Phạm vi, không có bảng số liệu tĩnh | 40 | 0 | Mục giữ nhãn |
| B. Phương án giữ nguyên | 140 | 94 | Không quá 1 trang |
| C. Tái lập | 389 | 135 | Dùng phần trang A bỏ trống |
| **Phụ lục** | **569** | **229** | **Không quá 3 trang** |

Ước theo 330 tiếng văn xuôi/trang: Chương 5 khoảng 2,93 trang trước khoảng dành cho tiêu đề. Phụ lục có ba bảng, lần lượt 4, 5 và 4 hàng dữ liệu, cùng tiêu đề và các ô đường dẫn có thể xuống dòng. Tổng phụ lục dự kiến khoảng 2,6–3 trang, nhưng chưa có bố cục đo. Không thu phông hoặc đổi lề. C dài hơn ngân sách riêng 1 trang của outline để chứa các yêu cầu tái lập bổ sung; bù bằng bỏ bảng A. Người ghép cần kiểm số trang và vị trí bảng bằng bản biên dịch toàn văn.

## 2. Kiểm tra cuối

`r31-qa-v2.json`: các ngoặc, môi trường và dấu toán khớp; không trùng nhãn; không có tham chiếu chưa định nghĩa trong tổ hợp Ch3 v3 + Ch4A v4 + Ch4B v7 + hai tệp v2 của R31. Mỗi đoạn có sự kiện có dòng EV; mỗi nhóm hàng bảng có dòng EV. 5.1 có đúng ba đoạn, 5.3 đúng năm hướng. Danh sách nhóm ở phụ lục C được mở rộng và khớp chính xác với 34 mã kiểm tra và 15 mã hiệu chỉnh trong tệp chia tập, không trùng mã. Số học của ba ví dụ số cũng được tính trong output.

Hai kiểm tra độc lập tập trung vào A/B và C đã đọc bản đầu. V2 sửa ba điểm từ nhận xét: dùng các số sổ ngày thường in trực tiếp trên hình Ch4B; giới hạn thư mục cấu hình cho tập chính/buổi sáng/tuyết; nói đúng rằng tập hiệu chỉnh không dùng để lập bảng kết quả chính. Root mở lại các nguồn tương ứng và kiểm các thay đổi. Không chạy lại các kiểm thử của RideBound trong lượt này: chỉ đọc hồ sơ và log đã có.

## 3. Nhãn và ghép tệp

Định nghĩa:
- `chuong:ketluan`; `muc:c5-tongket`; `muc:c5-hanche`; `muc:c5-huongphattrien`.
- `phuluc:A`; `phuluc:B`; `phuluc:C`.
- `bang:pl-giunguyen`; `bang:pl-danhsach`; `bang:pl-goc`.

Nhãn ngoài tệp: `muc:c4-thaoluan`, `muc:c4-taptu` (Ch4); `muc:giunguyen`, `muc:bamoc` (Ch3). Không thêm gói. Phụ lục dùng một tiêu đề chung rồi ba mục A/B/C để tránh ép mỗi phụ lục sang trang riêng; bảng được đánh B.1, C.1, C.2. Mã đích liên kết được phân biệt theo mục khi đặt lại bộ đếm bảng.

Ghép Chương 5 sau Chương 4; ghép phụ lục sau tài liệu tham khảo. Mục A chỉ giữ phạm vi và nhãn, **không có các bảng tĩnh mà tham chiếu cũ có thể hứa với người đọc**. Câu Ch3/Ch4 trỏ tới A để đọc bảng hoặc số cụ thể cần bỏ phần tham chiếu hoặc sửa ý dẫn, không đổi sang C vì C không chứa các kết quả tĩnh ấy. Câu Ch4A về nguồn gốc trần có thể tiếp tục dùng A chỉ như phạm vi của đợt thử trước.

## 4. Bằng chứng cho mọi con số của Chương 5

Nguồn headline chỉ là `drafts/08-chuong4-phanA-v4.tex` và `drafts/09-chuong4-phanB-v7.tex`. Mã dòng sổ được giữ như hai bản đó. REG là `evidence/EVIDENCE-REGISTER.md`, N/L1a ở ADDENDUM-1, X3 ở ADDENDUM-2, N4B ở ADDENDUM-3, C4A ở ADDENDUM-4.

| Mục, số in | Đơn vị/mẫu số/cách gộp | Dòng bằng chứng; nơi đã in |
|---|---|---|
| 5.1: công thức 7 | Công thức của Hörl–Zwick, không phải số kết quả | J03; Ch3 và Ch4B đã dùng `horl2022` |
| 34; 3.672 | Kịch bản; yêu cầu mỗi cấu hình | B09; Ch4A Bảng `bang:c4-taptu` |
| Trần 30; 120 giây | Tham số, không phải mức tốt nhất | A06, N-06, K36; Ch4A |
| 2.338; 2.434; ít hơn 96 | Lượt phục vụ trên 3.672 yêu cầu, chênh hai tổng | C01, C02; Ch4A `bang:c4-chinh` |
| Không khách nào trong 2.338 vượt; lớn nhất 29,2 giây | Khách phục vụ dưới C-30; tổng trị tuyệt đối do điều phối cả chuyến | C20; Ch4A `bang:c4-doidieuphoi` |
| 2.262; 2.231 | Không trễ quá 60 giây trên 3.672 yêu cầu, lời hứa đầu không dự báo | C08; Ch4A |
| 28 trong 34 | Kịch bản M+-30 có ít nhất một khách bị phá nghĩa vụ của chính luật | C13, N-21; Ch4A `bang:c4-nghiavu` |
| 2.387; 2.255; 2.366 | Phục vụ; không trễ quá 60/120 giây trên 3.672 yêu cầu, C-120 không dự báo | N-06, L1a-02; Ch4A `bang:c4-tran120` |
| 3 trong 524 | Bản ghi chặn chỉ do cộng dồn; không phải khách hay tác dụng nhân quả | N-08, L1a-06; Ch4A `bang:c4-congdon` |
| 68 → 2 trong 1.471; 21 | Khách trễ quá 60 giây, gộp theo khách; kịch bản ngày thường có dự báo | F04, F17; Ch4B `muc:c4-dubao` |
| 2.328 = 2.328 | Không trễ quá 60 giây trên 3.672 yêu cầu, C-30 dự báo vs U dự báo + đệm 30 giây | C09, C10, N-16; Ch4B `bang:c4-dem` |
| 2.366 vs 2.338 | Không trễ quá 120 giây trên 3.672 yêu cầu, cùng phép so | C10, N-16; Ch4B |
| 37,2 vs 7,4 giây | Độ dài thêm trung bình gộp theo khách được phục vụ; mỗi cấu hình có tập khách riêng | C10, N-18; Ch4B đoạn mở `muc:c4-dem` |
| 44/2.434 vs 4/2.338 | Tới sớm quá 60 giây, trong khách phục vụ | C10; Ch4B `bang:c4-haiphia` |
| 6.217; 5.353; 783 giây; 68 khách | Sổ của khách trễ quá 60 giây so lời hứa không dự báo ngày thường | F09; giá trị làm tròn in trực tiếp ở Hình `hinh:c4-so` Ch4B:152–156 |
| 41/601; 3.445,9; 8,6; 251,5; 3.185,9 giây | Khách trễ chiều tuyết; tổng giây trễ và ba phần của họ | F13, N4B-05; Ch4B `muc:c4-tuyet`, Hình `hinh:c4-so` |
| 5.2: 34 kịch bản; 5 ngày; một lần mỗi kịch bản | Phạm vi, không suy là 34 mẫu độc lập | I05, B11; Ch4B hạn chế |
| 5.3: hai thứ tự × hai cấu hình; 30 giây | Phép thử đề xuất, không có số kết quả mới | H12, H02, K18; OUTLINE-V2 §7.2; Ch4B bản dự phòng |
| Các ngưỡng “một phút”, “hai phút” | >60/>120 giây để đếm trễ, ≤ để đếm không trễ | C06, C08, C10; Ch4A định nghĩa chỉ số |

V2 dùng 6.217/5.353/783 thay các giá trị chính xác chỉ có trong chú thích EV của v1. Không cộng các số đã làm tròn để suy lại tổng. Không thêm tỉ lệ phần trăm hoặc kết quả học máy vào tổng kết.

## 5. Bằng chứng cho con số và cấu hình phụ lục

### A

Bỏ các số liệu của Phụ lục A vì E12 mới trỏ tới bảng trong bản luận văn; chưa xác lập được ánh xạ đầy đủ tới kết quả tổng hợp đã lưu cho từng số.

E12 là khóa ở `OUTLINE-PROPOSAL-CLAUDE.md:403`, không phải một dòng số của REG. Kiểm đọc đã mở các bảng nguồn, các chương trình `measure/measure_instability.py`, `frontier/frontier_table.py`, `window/fielbaum_measure.py` và các gốc `E:/RideBoundData/wp9/confirmatory-h6-panela-v2/`, `E:/RideBoundData/wp9/frontier-v1/`. Chưa tìm được output tổng hợp đã lưu cho bảng 89,06%, thang trần, ngưỡng ±0,3 điểm phần trăm và 774/1.581. Không tự tính lại để lấp khoảng thiếu. Phép đo điểm cuối cũ còn dùng lần công bố cuối như xấp xỉ thực hiện (`fielbaum_measure.py:25–28,244–245`), nên không nhận là đo trực tiếp giờ tới thực tế.

Ngoại lệ cấu trúc: vẫn giữ mục A chỉ 40 tiếng về phạm vi, không có số kết quả, nhằm đáp ứng yêu cầu định nghĩa `phuluc:A`. Đây không phải việc khôi phục phụ lục số liệu; các câu dẫn tới bảng đã bỏ vẫn cần sửa khi ghép. Cách nói phạm vi theo K29/K33/K34.

### B

| Số/biểu thức | Vai trò | Bằng chứng |
|---|---|---|
| 0 ≤ L ≤ B; L + abs(e−e) = L | Điều kiện của sổ, chứng minh phương án giữ nguyên qua C | A06, A22; Ch3 v3:354–387; `CommitmentBudgetEvaluator.cs:51,88–104` |
| e−p0 > B | Phản ví dụ cho hạn chót | A09, A10; `CommitmentLockEvaluator.cs:156–160,186–196` |
| L(V)+abs(e−v) | Cộng cả độ dời khách thấy | A11, A01, X3-33 |
| e ≤ max(p0+B,e) | Hạn chót nới, suy luận từ hai định nghĩa, chưa chạy | A22, J03, X3-36, K02, K27; Ch3 v3:451–458 |
| 600/660; x=0, c=z=60 | CE-1, minh họa dựng tay, giây | TEX07:650; A01; `r31-qa-v2.json` |
| 600→660→600; 0/120 | CE-4, độ lệch hai đầu/tổng độ dời, giây | TEX07:655–656; A12; output QA |
| 600→660→720; 120/120 | CE-5, giây | TEX07:657–658; A12; output QA |

CE-6 giữ bằng tính chất đại số khi hai phần trái dấu. Bỏ số và cách gọi là một sự kiện quan sát của CE-6 vì chưa đối chiếu lại bản ghi nguồn. CE-2/CE-3 đã có ở Ch3 nên không lặp. Không có số kiểm chứng dự báo hoặc định lý theo bốn họ.

### C

| Nhóm số/nhận dạng | Bằng chứng và phép kiểm |
|---|---|
| 34/15, ngày 14–18/11/2018, từng mẫu/khung ở bảng | B08, B09; mở trực tiếp `tang3/t38/split-t38-v1.json:15–65`; phép mở rộng danh sách trong `r31-qa-v2.py` khớp cả hai tập |
| Mã mẫu s10, r1–r4, w07/w08/w17 | Cùng tệp chia tập; ký hiệu là định danh, không phải số thống kê |
| 15 lần C-30 hiệu chỉnh khoảng dự phòng | C17; `run_t38.py:42–43`; T38I:15–22; không dùng để lập bảng kết quả chính, có trong phạm vi kiểm tính nhất quán cũ |
| Buổi sáng 12–13/11, r1–r4, khung 7; cố định cùng ngày, khung 8/17 | B15, B16, B17; `run_w07.py:3–8,33–34`; LAD:1–6 |
| Tuyết 15/11, r1–r4, khung 14/15 | B20, N-26; `optimize/run_forecast.py:73–74` |
| U/C-30/M+-30/M+-60/V-30 và C-120 | B10, L1a-01; `run_t38.py:42–55`; `run_t38c120.py:22–26` |
| Dãy 30/60/90/120/150/180/240/300 | B15, B16, X3-28; `run_w07.py:33–43`; `run_w07x.py:35–40` |
| FREE/U/C-30/C-60/C-120 ở tập cố định | B17, LAD:1–6; `claude-work/wp14r_ladder_reanalysis.py:1–13` |
| Tên LOCKS/B1/C1 | A08, X3-19, X3-38; `E:/Code/RideBound/docs/08-algorithms-baselines-and-solver.md:20–29`; C1 là họ chính sách, không đồng nhất một mức trần |
| runner-tier3-v2; nguồn 45f8026; lõi 1ce15e92; FleetPy 1.0.2; hạt giống 7 | A28, X3-10; R26 Q8; bản tin khởi tạo của tám lần tuyết; nguồn dựng theo ADR:5117–5118 |
| Khung nhu cầu hai tiếng, không có độ dài lần chạy cố định | R26 Q1–Q2; `actual_fleetpy_medium_preflight.py:528–581,595–637`; `preflight_world_v1_1.py:40–58`, v1_2:18–20 |
| 170 + 34; 136 trong 192; 16 mỗi cấu hình; 8 tuyết | B10, L1a-01, C4A-07, B17, H13, B20; Ch4A bảng tập thử |
| Bản thay thế C-30-d20181114-s10-r3-w17-rerun1 | C4A-17, ADD1:6; thay đúng bản hỏng hạ tầng, không tính cả hai |
| 1.991, kiểm kê 08/10/2026 | B19, C4A-20; INV:1; không cộng thêm các đợt mới để tạo một tổng hiện tại |
| 12/10/2026; 1.024/1.025; 1/1 | N4B-13; `TESTRUN-45f8026-2026-10-12.md:14–17,34–47`; mở log eollf và dirtycheck, không suy một lượt toàn bộ đạt hết |

Gốc kết quả trong bảng được mở lại từ các chương trình chạy (chỉ đọc). Tập cố định lưu dưới `<tên lần chạy>/attempt-01/output/`; ánh xạ các tên là `b1-ref`→FREE, `c1-nobudget`→U, `c1-h6ref`→C-30, `c1-budget60`→C-60, `c1-budget120`→C-120. Tệp FREE/B1 không được nhận là nằm ở `tang3/configs/`.

Đầu vào để truy lại: chính tại `C:/RideBoundData/research/fixtures-panelA-v1/<mã>/` và `S/tang3/calib/panelA/drivers/`, `worlds/`; buổi sáng tại `fixtures-w07-v1/`, `S/tang3/w07/drivers/`, `worlds/`; tuyết tại `fixtures-snow-v1/`, `S/optimize/snow/drivers/`, `worlds/`. S là thư mục scratchpad. Nguồn: RUN38:39,54–56; RUNW07:35–39; `run_forecast.py:85–87`.

Cách tái tính đã đọc: `tang3/evidence/METRICS-SPEC.md:28–63`; ADDENDUM-1 phần phương pháp; `checks-addendum-1/recompute_addendum_1.py`; các bộ đọc độc lập `R15-audit.py` và `R19-stage1a-analyze-v4.py`. A26/C19/N4B-14 xác nhận các phạm vi so khớp; đây là đọc lại bản ghi, không phải chạy lại mô phỏng. EV ở C không nhận có người xác nhận nếu phép đối chiếu do công cụ tạo.

Hai điều kiện kiểm thử: kiểu xuống dòng LF, và một tệp chưa ghi nhận để kiểm thử bắt trạng thái cây làm việc. Full suite mới đạt 1.024/1.025; kiểm thử còn lại đạt riêng 1/1. Không đưa năm lỗi ở các lần thử dùng kiểu xuống dòng khác thành lỗi sản phẩm.

## 6. Trích dẫn

Dùng các khóa đã có ở bản chương hoặc luận văn: `fielbaum2020`, `schulz2026`, `horl2022`; không đề xuất khóa khác. `horl2022` được Ch3/Ch4B dùng nhưng còn phải có ở danh mục tài liệu của bản ghép. Metadata đã kiểm qua X3-40 và R26 Q10:

Sebastian Hörl; Felix Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling*. Bài tại Hội nghị thường niên lần thứ 101 của Transportation Research Board (TRB 2022), Washington, D.C., tháng 1/2022. ETH Zurich Research Collection. DOI: 10.3929/ethz-b-000561639. Không gán tên tạp chí hoặc số trang kỷ yếu chưa xác minh. R26 đã đối chiếu danh sách xuất bản IVT và bản lưu chính thức của ETH.

## 7. Nội dung bỏ và lý do

- Các bảng số liệu tĩnh của A: thiếu ánh xạ tới output tổng hợp cho từng số; xem dòng placeholder ở §5.
- Bảng kết quả ngày × khung: không chép lại để giữ tổng phụ lục không quá 3 trang. Dữ liệu đủ vẫn ở N-22, ADD1:173–186; bảng danh sách C chỉ là danh sách kịch bản, không thay bảng kết quả này.
- CE-6 dưới dạng khách thực nghiệm và các số cụ thể: chưa kiểm lại bản ghi gốc; giữ tính chất đại số.
- Khoảng độ dài mô phỏng và các thời gian chạy thực: không cần cho kết luận; C vẫn giải thích đúng điều kiện kết thúc. Không suy khung nhu cầu thành thời lượng lần chạy.
- Cấu hình CPU/RAM lịch sử: R26 Q6 chưa khôi phục được đầy đủ; không lấy cấu hình máy hiện tại làm máy của các lần chạy cũ.
- Số của bộ chọn ưu tiên chi phí trên quỹ đạo: chưa có kết quả; hướng này đứng đầu 5.3.
- Không đưa chi tiết hiệu quả học máy vào 5.1 vì ba đoạn đã trả lời ba phần chính và phải giữ ngân sách chương.

## 8. Điểm cần xử lý khi ghép / câu hỏi mở

1. Kiểm bố cục toàn văn: Chương 5 mục 5.2 nhỉnh hơn 0,5 trang theo thước 330 tiếng; phụ lục C dùng phần trang A bỏ trống. Chưa có phép biên dịch trong lượt này.
2. Rà các tham chiếu A: nhãn tồn tại, nhưng bảng số liệu đã bỏ. Không để câu dẫn hứa nội dung không có.
3. Cập nhật câu cũ Ch4A/Ch4B và X3-10 về bộ chạy tuyết “chưa kiểm”: R26 Q8 đã đối chiếu tám bản tin và liên kết cấu hình, xác nhận runner-tier3-v2 và luật phục hồi không tệ hơn. Điều này không tự xác nhận mọi thuộc tính thế giới tuyết.
4. Bảo đảm danh mục tài liệu của bản ghép định nghĩa `horl2022` theo metadata trên.
5. Nếu muốn khôi phục A hoặc bảng ngày × khung, cần bằng chứng/tổng ngân sách trang mới; không tự thêm vào bản hiện tại.

Không có câu hỏi cần trả lời để dùng hai tệp v2 này làm bản ghép; các điểm trên là kiểm tra tích hợp và các khoảng thiếu đã nêu đúng phạm vi.
