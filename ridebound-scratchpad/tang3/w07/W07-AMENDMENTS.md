# Sửa đổi của Việc B sau khi niêm phong

`W07-PLAN.md` được niêm phong lúc 2026-09-29T14:32:27Z (`W07-PLAN.sha256`). Mục dưới đây viết sau thời điểm đó và **không**
đổi ô, nhánh, thước đo, dự đoán hay driver đã niêm phong.

## A1 — 2026-09-30 00:22 (giờ máy): một lần đọc nguồn điện không phải "cắm sạc" làm driver hoãn 72 job

- **Chuyện gì xảy ra.** Lúc job thứ 11 xong (`M-30-d20181112-s10-r1-w07`, 3365 s sau khi driver chạy), `may_start_job()`
  trả `False`. Pool của driver đưa mọi job còn lại qua phép kiểm này trong cùng khoảnh khắc, nên cả 72 job được ghi
  `deferred-on-battery` (`driver-run-1.out`). Lúc 00:22:22 máy đã báo cắm sạc, pin 100% (`Win32_Battery.BatteryStatus` 2).
  Chưa rõ sạc bị rút thật trong chốc lát hay chỉ là một lần đọc sai.
- **Không job nào bị hỏng vì việc này.** Job bị hoãn thì chưa được khởi động: không có thư mục output, không có log. 5 job đang
  chạy lúc đó (`V-30-…-r1-w07`, `C-30/Mplus-30/C-60/Mplus-60-…-r2-w07`) chạy tiếp bình thường.
- **Việc làm.** Không sửa `run_w07.py` (đã niêm phong). Thêm `relaunch_until_done.py`: chờ driver cũ thoát, rồi khởi động
  lại **đúng** driver đó mỗi khi máy cắm sạc, cho tới khi không còn job nào chưa chạy. Driver tự bỏ qua job đã có output.
  Mỗi lần khởi động có tệp `driver-run-<n>.out` riêng.
- **Kiểm sau khi xong:** mọi job có đúng một log, và không job nào có hai thư mục output.
