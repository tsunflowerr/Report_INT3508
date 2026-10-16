# Sửa đổi sau niêm phong (Tầng 2)

Niêm phong: `PREREGISTRATION.sha256`, 2026-09-24T06:03:52Z. `predictions.csv` và quy tắc dự đoán
không bao giờ được sửa. Mọi thay đổi mã phân tích sau niêm phong được ghi ở đây.

## A6 — 2026-09-24 ~14:10Z — `figure_families.py` (chỉ trình bày)

Theo hướng dẫn trực quan hóa: hai màu đầu của bảng màu tham chiếu đã kiểm định (`#2a78d6` kết cục,
`#eb6834` dự đoán; validator: CVD ΔE 24,7, thị giác thường ΔE 33,6, tương phản ≥ 3:1), chữ màu mực, lưới
nhạt, nhãn số `k/8` trên mỗi cột, chú giải ở trên, nhãn trục ba dòng để không đè nhau. Logic đếm và dự
đoán không đổi. Bản đầu `hinh/tang2-bon-ho.pdf` (nhãn đè nhau) được giữ, không dùng; luận văn dùng
`hinh/tang2-bon-ho-v2.pdf`.

## A5 — 2026-09-24 ~10:15Z — chạy bằng pin theo yêu cầu người dùng (chỉ vận hành)

Người dùng cho phép chạy khi rút sạc ("cứ chạy đi, gần hết pin tôi tự cắm"). `run_deadline.py`: job
mới được khởi động khi có điện lưới, **hoặc** khi biến môi trường `RB_ALLOW_BATTERY_MIN_PERCENT` được đặt
và pin còn ít nhất mức đó (đặt 30). Dưới mức đó không khởi động job mới; job đang chạy chạy nốt. Thử:
ở 95% pin, không đặt biến ⇒ không chạy; ngưỡng 30 ⇒ chạy; ngưỡng 99 ⇒ không chạy. Không có giới hạn
CPU-time trong các job (chỉ timeout 60 s mỗi phản hồi), nên hạ xung khi chạy pin không đổi kết cục của
một job tất định; một job hỏng vì lý do máy chủ sẽ theo quy tắc A2.

## A4 — 2026-09-24 ~10:20Z — lỗi đặt tên log khi chạy lại (vận hành, báo trung thực)

Lần chạy lại ở A2 ghi **output** đúng vào `<job>-rerun1` và phân loại đọc đúng thư mục đó, nhưng
`run_job` ở nhánh thường vẫn trả về và ghi log bằng tên gốc. Hệ quả: (i) dòng tiến độ in tên gốc
(hiển thị); (ii) log stdout của năm lần chạy lỗi, ghi lúc 09:35:57Z, bị **ghi đè** bởi log của bản chạy
lại trong `logs/runs/<job>.log`. Thông tin lỗi gốc không mất: `failure-00.json` (thông điệp và
traceback 1.844 ký tự ở ô 14-r1) còn nguyên trong năm thư mục gốc. Đã sửa: log mang tên output và
mở ở chế độ `"x"` nên không bao giờ bị ghi đè. Không đổi kết quả, phân loại hay phân tích.

## A3 — 2026-09-24 (sau A2) — công tắc dừng (chỉ vận hành)

`run_deadline.py`: khi tệp `STOP` tồn tại, không khởi động job mới (nhãn tạm `deferred-stop`, không tạo
thư mục); job đang chạy chạy nốt; stage được báo INCOMPLETE và driver thoát. Mở lại bằng cách đổi tên
`STOP` (không xóa). Không đổi job, cấu hình, phân loại hay phân tích. Thử khô: một job đang chờ trả về
`deferred-stop` và không tạo thư mục. (Ghi chú: giờ trong tiêu đề A2 là ước lượng; mốc chính thức của A2
là `amendment-A2.sha256`, 09:37:42Z.)

## A2 — 2026-09-24T09:40Z — lỗi do máy chủ ngủ (quy tắc thay thế, chốt trước khi có kết quả chạy lại)

Sự kiện: lúc 08:31:56Z driver được tạm treo theo yêu cầu người dùng; 6 job `dl-120` k = 1 đang chạy
được để chạy nốt. Lúc 08:35:25Z máy vào Modern Standby (Kernel-Power 506), thức 08:43:14Z (507), ngủ
lại ngay, thức 09:32:47Z (507). Bốn job lỗi lúc 08:43:16–19Z và một job lúc 09:32:47Z, cả năm với
`RBWP7_RUNNER_RESPONSE_TIMEOUT at $runner: decision` (đồng hồ timeout 60 s của `runner_client` tính cả
thời gian ngủ). Một job khác hoàn tất. Không có sự kiện ngủ nào khác từ 03:00Z (chỉ có đổi nguồn
03:08, 05:11, 05:26, 08:33Z), và không có job nào khác mang nhãn `other`.

Quy tắc: một lần chạy là **lỗi do máy chủ** khi (i) `failureMessage` bắt đầu bằng
`RBWP7_RUNNER_RESPONSE_TIMEOUT` và (ii) thời điểm ghi `failure-00.json` nằm trong 60 s sau một sự kiện
Kernel-Power 507. Lỗi do máy chủ **không phải kết cục**: thư mục gốc giữ nguyên, job được chạy lại
cùng cấu hình và hạt giống vào `<job>-rerun1`, và phân tích dùng bản chạy lại. Danh sách được chốt
trong `HOST_FAILURES.txt` trước khi chạy lại; nếu bản chạy lại cũng lỗi do máy chủ, dùng `-rerun2`.

Năm job: `dl-120-k1-d20181114-s10-r1-s7`, `dl-120-k1-d20181116-s10-r4-s7`,
`dl-120-k1-d20181117-s10-r1-s7`, `dl-120-k1-d20181117-s10-r3-s7`, `dl-120-k1-d20181117-s10-r4-s7`
(đều được dự đoán "không vô nghiệm do cam kết"; quy tắc không phụ thuộc dự đoán).

Mã: `run_deadline.effective_name/effective_output` giải tên thay thế; `analyze.label_of`, `analyze.accepted`
và `figure_families.py` đọc qua `effective_output`. Mục 0 của `analyze.py` vẫn liệt kê mọi thư mục, kể
cả năm bản gốc (nhãn `other`).

Phòng ngừa: `run_deadline.py` gọi `SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)`
trong suốt lần chạy để Windows không tự ngủ khi rảnh (không đổi cấu hình máy; không chặn được việc
gập máy hay ngủ thủ công).

## A1 — 2026-09-24T07:40Z — `analyze.py` mục 2 (chỉ trình bày)

Bảng đếm nhóm theo `(arm, window, k)` nên gộp dòng panel A (2A, khung sáng) với dòng 2B cùng khung
`w08`. Nay nhóm theo `(stage, arm, window, k)`. Không đổi dự đoán, phân loại, cặp được tính, độ
chính xác hay ngưỡng. Phát hiện khi chạy phân tích tạm thời lúc 07:05Z trên 45/120 job của `2a`
(chưa có job nào của `2b-rest`).
