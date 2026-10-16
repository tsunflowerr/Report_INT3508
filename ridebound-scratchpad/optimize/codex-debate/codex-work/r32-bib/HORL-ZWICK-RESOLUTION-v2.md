# Hörl–Zwick: giải quyết nhận dạng và phiên bản

Kiểm ngày 12–13/10/2026. **Dùng `horl2022` cho bản hội nghị TRB 2022 lưu ở ETH, DOI 10.3929/ethz-b-000561639.** Chưa tìm thấy bản tạp chí được kiểm chứng của chính công trình này.

## Hai tệp được mở độc lập

1. `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf`: 22 trang. Trang đầu là **Sh. Sharif Azadeh, Bilge Atasoy, Moshe E. Ben-Akiva, M. Bierlaire, M.Y. Maknoon**, *Choice-driven dial-a-ride problem for demand responsive mobility service*, **Transportation Research Part B: Methodological 161 (2022), 128–149**, DOI **10.1016/j.trb.2022.04.008**. Tên, tác giả, số tập, trang và DOI hiện trực tiếp trên trang đầu. [Kho MIT của bản xuất bản cuối](https://dspace.mit.edu/entities/publication/024805a3-e5f5-4a58-8519-096c34e2b525) cũng ghi đúng tên tệp này. Đây là `sharifazadeh2022`, không phải Hörl–Zwick.

2. `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf`: **17 trang vật lý** gồm bìa kho ETH và **16 trang bản thảo đánh số 1–16**. Bìa ghi Sebastian Hörl, Felix Zwick, *Traffic uncertainty in on-demand high-capacity ride-pooling*, loại Conference Paper, năm 2022 và DOI trên. Trang tiêu đề bản thảo ghi ngày nộp 27/10/2021. Đã trích lại chính PDF này, không chỉ đọc `.txt` cũ. Tựa, tác giả, bìa, số trang và các công thức khớp [bản ETH chính thức đã mở](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/561639/ab1659.pdf?isAllowed=y&sequence=1).

Các đoạn trích nguyên trang và kết quả đếm nằm trong `local-elsevier-excerpts.txt` và `inventory-and-horl-probe-output-v2.txt` cùng thư mục.

## Tên hội nghị và tình trạng bản tạp chí

[ETH IVT, mục AB1659](https://www.ivt.ethz.ch/en/vpl/publications/working-papers.html) xác nhận công trình của S. Hörl và F. Zwick được trình bày tại **101st Annual Meeting of the Transportation Research Board (TRB 2022), Washington, D.C., tháng 1/2022**. [Trang nghiên cứu MATSim của ETH](https://www.ivt.ethz.ch/en/research/matsim.html) cũng ghi hội nghị này và mã TRBAM-22-01001. Mã đó là mã bài, không phải khoảng trang của kỷ yếu.

Đã tìm theo đúng tựa và cặp tác giả, đối chiếu các bản ghi ETH và bản thảo. **Không tìm được bản tạp chí có trang nhà xuất bản, DOI tạp chí hoặc quan hệ phiên bản được xác minh cho chính tựa này.** Kết luận là chưa có bản tạp chí được kiểm chứng trong vòng này; không khẳng định một tìm kiếm âm chứng minh tuyệt đối rằng không thể có bản đổi tựa. Tệp Elsevier được brief đưa ra không phải bằng chứng cho một bản tạp chí của Hörl–Zwick. Không gán tập 161 hoặc trang 128–149 của Sharif Azadeh sang `horl2022`.

## Kiểm số công thức ở phiên bản được chọn

Tất cả các mục dưới nằm ở **trang bản thảo 8, trang PDF vật lý 9** của bản ETH/local đã mở:

| Nhãn | Nội dung được kiểm |
|---|---|
| (7), chiến lược B | Giờ trả bắt buộc bằng giá trị lớn hơn giữa giờ trả cập nhật và giờ trả muộn nhất: `t_required_dropoff = max(t_updated_dropoff, t_latest_dropoff)` |
| (9) | Giờ đón của tuyến đang xét không vượt giờ đón bắt buộc |
| (10) | Giờ trả của tuyến đang xét không vượt giờ trả bắt buộc |
| (11) | Mục tiêu cộng phạt phần vượt các mốc gốc; khác với các ràng buộc trên giờ bắt buộc |

Phần giải thích chiến lược B bắt đầu ở trang bản thảo 7, trang PDF 8: mỗi lượt tính lại các giờ trên tuyến đang gán theo thời gian đi hiện tại. **Công thức (8) thuộc chiến lược C về giờ đón**, không phải công thức B về giờ trả. Vì luận văn viện dẫn chính (7), (9)–(10), bản TRB/ETH đã đọc là lựa chọn có mốc kiểm chứng đầy đủ.

## Dòng thư mục đề nghị

S. Hörl và F. Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling*. Trong *101st Annual Meeting of the Transportation Research Board*, Washington, D.C., tháng 1/2022. ETH Zurich Research Collection, 2022. DOI: 10.3929/ethz-b-000561639.

Không thêm tập, kỳ hoặc khoảng trang kỷ yếu chưa được xác nhận. Có thể mô tả “bản thảo 16 trang” trong ghi chú kiểm chứng; không dùng “1–16” như trang được nhà xuất bản gán. Năm nộp 2021 không thay năm công bố hội nghị 2022. Giữ đúng khóa `horl2022` của Ch2 và Ch3; dòng đề nghị đã có trong `10-tai-lieu-draft-v2.tex`.
