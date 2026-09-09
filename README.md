# Báo cáo thực tập - Trần Quang Thành (23020155, K68I-IT2)

Báo cáo thực tập tại KiotViet, viết bằng LaTeX (XeLaTeX), **23 trang A4**, ngôi thứ nhất dùng "em".

## Build

Báo cáo build bằng [Tectonic](https://tectonic-typesetting.github.io/) (XeLaTeX portable, không
cần cài LaTeX vào máy). Thư mục `tools/` **không nằm trong repo** (167 MB binary, đã cho vào
`.gitignore`), nên khi clone về thì tải lại:

- `tectonic.exe` — tải ở [tectonic releases](https://github.com/tectonic-typesetting/tectonic/releases), đặt vào `tools/`
- `poppler` (chỉ cần khi muốn xuất ảnh preview) — tải ở [poppler-windows releases](https://github.com/oschwartz10612/poppler-windows/releases), giải nén vào `tools/poppler/`

```powershell
cd C:\KiotViet\bao-cao-thuc-tap
.\tools\tectonic.exe -X compile main.tex --outdir .
```

Kết quả: `main.pdf`.

## Xuất từng trang ra ảnh để soát bố cục

```powershell
.\tools\poppler\poppler-26.07.0\Library\bin\pdftoppm.exe -png -r 105 main.pdf preview\tr
```

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `main.tex` | Khung tài liệu: font, lề, định dạng đề mục I./a., mục lục |
| `noi-dung/00-bia.tex` | Trang bìa |
| `noi-dung/01-muc-luc.tex` | Mục lục (tự sinh) |
| `noi-dung/02-loi-cam-on.tex` | Lời cảm ơn |
| `noi-dung/03-gioi-thieu-chung.tex` | Phần I + Bảng 1 |
| `noi-dung/04-yeu-cau-bai-toan.tex` | Phần II + Hình 1 (kiến trúc hệ thống) |
| `noi-dung/05-giai-phap.tex` | Phần III + Hình 2 (sinh lệnh), Hình 3 (gộp khoảng) |
| `noi-dung/06-cai-dat.tex` | Phần IV |
| `noi-dung/07-ket-qua.tex` | Phần V + Hình 4 (biểu đồ tiến độ) |
| `noi-dung/08-tai-lieu-tham-khao.tex` | Tài liệu tham khảo |
| `noi-dung/09-trang-danh-gia.tex` | 2 trang đánh giá (công ty, giảng viên) |
| `hinh/` | Logo trường và logo công ty |
| `main.pdf` | Bản PDF thành phẩm |
| `tools/` | Tectonic (XeLaTeX portable) và Poppler (render PDF ra ảnh) — *không commit* |
| `preview/` | Ảnh từng trang, dùng để soát bố cục — *không commit* |

## Định dạng đang áp dụng

- Times New Roman 13pt, dãn dòng 1,5
- Lề: trái 3cm, phải 2cm, trên 2cm, dưới 2cm
- Thụt đầu dòng 1cm
- Đánh số đề mục theo mẫu: I., II., III. và a., b., c.
- Số trang bắt đầu từ phần nội dung; trang bìa, mục lục và lời cảm ơn không đánh số

## Chỗ cần điền thêm

Tìm chuỗi `[chờ bổ sung]` trong `noi-dung/00-bia.tex` để điền tên giảng viên đánh giá.

## Lưu ý khi sửa nội dung

Báo cáo đang khớp đúng 23 trang. Thêm khoảng 500 chữ là sang trang 24, nên nếu bổ sung
đoạn nào thì nên cắt bớt một đoạn khác tương đương.
