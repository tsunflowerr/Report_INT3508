# Khóa luận tốt nghiệp — RideBound

**Giải pháp điều phối xe ghép trực tuyến bảo vệ với cam kết hành khách**

Trần Quang Thành — 23020155 — K68I-IT2. GVHD: ThS. Trần Mạnh Cường.

Bản hiện tại đã cập nhật phép so hai thứ tự chọn phương án: ưu tiên ổn định và
ưu tiên chi phí kế hoạch, mỗi thứ tự có trần 30 giây và không trần. Nội dung
trình bày cả phục vụ, ghép khách, điều chỉnh lời hứa, giờ đến và giới hạn của
dự báo. Tên các đợt chạy nội bộ không được dùng làm mạch trình bày trong luận văn.

## Biên dịch

Chạy trong thư mục này bằng Tectonic hiện có ở thư mục cha:

```powershell
..\tools\tectonic.exe -X compile main.tex --outdir . --keep-logs
```

Đầu ra là `main.pdf`. Cần kiểm log mới sau mỗi lần biên dịch, nhất là lỗi tràn
lề, thiếu tham chiếu và trùng nhãn. Bản biên dịch được giao cùng bộ nguồn này;
thông tin mã băm, kiểm số và kiểm trực quan ở hồ sơ `chung-cu/README.md`.

## Nội dung

`main.tex` nạp các tệp trong `noi-dung/`: ba trang bìa, lời cảm ơn, lời cam đoan,
tóm tắt song ngữ, mục lục, ký hiệu, năm chương, tài liệu tham khảo và phụ lục.
Hình vẽ phương pháp và đồ thị được viết trong LaTeX; logo ở `hinh/logo-uet.png`.

Tóm tắt và Chương 1 nêu vấn đề cùng phạm vi kết quả. Chương 2 giới thiệu cơ sở
và công trình liên quan. Chương 3 đặc tả luật C, lời hứa theo dự báo và sổ theo
khách. Chương 4 báo kết quả, gồm đánh đổi giữa hai thứ tự chọn phương án.
Chương 5 tổng hợp kết quả, hạn chế và hướng phát triển. Phụ lục giữ các phép
kiểm và phép sàng lọc bổ trợ, phân biệt với mô phỏng đầy đủ.

## Phạm vi kết luận

Trần 30 giây giới hạn tổng độ lớn phần dời giờ trả tính cho điều phối sau khi
nhận khách. Đây không phải trần thời gian chờ đón, mức đi vòng hay bảo đảm
đến thực tế trong 30 giây. Phép so có tính thăm dò trên năm ngày đã xem và
các kịch bản phụ thuộc nhau. Dự báo mới được tính lại trên hành trình đã ghi;
không suy thành cải thiện quyết định điều phối, lợi nhuận hoặc sự hài lòng.

Các đối chứng bất lợi, phép thử tích hợp dự báo chưa thành công và giới hạn
của so sánh hai bản chạy đều được giữ trong nội dung. Dữ liệu TLC theo tháng
là hướng mở rộng; khóa luận không nhận đã huấn luyện hay kiểm mô hình mới.
