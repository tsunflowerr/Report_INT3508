# Hồ sơ đối chiếu bản khóa luận cập nhật

Các mã `% EV:` là chú thích trong nguồn LaTeX, không xuất hiện trong PDF.
Chúng dùng để truy vết nội bộ; nội dung luận văn gọi các cấu hình theo mục tiêu
chọn phương án, không gọi theo tên đợt chạy.

## Nguồn kết quả bổ sung

- **S15-01:** `C:/RideBoundContinuation/2026-10-15/results/stage1b-report.txt`.
  Báo cáo toàn bộ bốn cấu hình; mục 2, 4 và 5 chứa bảng gộp, theo kịch bản,
  lịch sử thay đổi lời hứa và các đánh đổi. SHA-256:
  `00e8a80eef4f7864575c71d2a5a5a3432991639cf3cb4b203cbc22d24dc46eb9`.
- **S15-02:** `C:/RideBoundContinuation/2026-10-15/evidence/analysis-independent-arithmetic-check.json`
  và `verify-stage1b-arithmetic.py`: 83/83 đối chiếu số học đạt từ bản trích
  xuất, không phải bộ giải mã transcript/dự báo độc lập thứ hai.
- **S15-03:** định nghĩa thứ tự ưu tiên trong mục 1.1 của
  `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/stage1b/harness/STAGE1B-PLAN.md`,
  kết hợp bản nguồn `dce84ec` tại `C:/Code/RideBound-costfirst` và chứng cứ
  activation `C:/RideBoundContinuation/2026-10-15/evidence/smoke-selector-confirmation.json`.
  Ưu tiên phục hồi khi kích hoạt và nhận yêu cầu vẫn đứng trước chi phí;
  bỏ các mức xếp hạng theo ổn định, không bỏ phép kiểm trần cứng.
- **S15-04:** `C:/RideBoundContinuation/2026-10-15/verify-thesis-v5.py` và
  `C:/RideBoundContinuation/2026-10-15/thesis-v5/thesis-numeric-check.json`:
  47/47 kiểm gồm toàn bộ các dòng của bảng so thứ tự ưu tiên, các chênh lệch
  chính, trung vị, mức dời tối đa, mốc sàng lọc bảy lịch sử và 13 mục inventory.
  Kiểm này dùng TSV/JSON đã khóa, không thay đặc tả phân tích hay chạy lại mô phỏng.

Nguồn bảng là `results/stage1b-riders.tsv` và `results/stage1b-runs.json` dưới
thư mục tiếp phiên trên C. Các giá trị `latePickups` đến từ JSON; phần còn lại
được kiểm từ các dòng khách trong TSV. Manifest kết quả gốc giữ nguyên:
`results/stage1b-results.sha256`.

## Nguồn cũ và giới hạn

Các mã A01–K52 và các phụ lục bằng chứng được giữ trong
`E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/evidence/`.
Bản trước cập nhật vẫn được giữ tại
`C:/RideBoundContinuation/2026-10-15/thesis-v4/`.

Phép đối chiếu hai bản chạy mới/cũ chỉ xác nhận hành vi ở bốn cặp mẫu; không
có chứng minh tương đương toàn bộ. Kiểm .NET lịch sử của bản ưu tiên chi phí
là 1.033 đạt trong 1.034 bài, exit 1 với một lỗi cây sạch đã ghi nhận; không
gọi cả bộ kiểm thử đạt. Lượt sửa luận văn này không sửa mã C#.

Đợt chạy đổi sàn C từ 45 GiB xuống 30 GiB sau 20 lượt theo quyết định của
người dùng; 48 lượt còn lại dùng chính sách tài nguyên mới, E40 GiB, AC-only
và reserve 410 MiB/job giữ nguyên. Đây là ranh giới tài nguyên đã ghi trong
amendment, không phải thay tham số phương pháp hay bỏ bớt kịch bản.

Biên nhận giao bản cuối, mã băm PDF/nguồn, vị trí sao lưu bản thật và phạm vi
kiểm trực quan được ghi tại hồ sơ tiếp phiên và receipt đi kèm bản cuối.
