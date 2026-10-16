# T3.2 — Kế toán tham chiếu và oracle vi mô

Trạng thái: **xong phần không cần sửa lõi** (2026-09-24). Không có mã RideBound nào bị sửa.

## Tệp

- `accounting.py`: oracle độc lập. Đầu vào là dòng audit `(request, coordinate, sequence, v, e, p,
  committed, closed, initial)` tính bằng mili-giây nguyên; đầu ra là `x, c, z` có dấu từng bước và
  `C, X, V, E, H, M⁺, M` từng khách. Nó không gọi mã sản xuất và không ra quyết định điều phối; lỗi đầu vào
  bị từ chối có kiểu (`AccountingError`), không bị ép kiểu âm thầm. `compare()` đối chiếu một sổ cái sản
  xuất với oracle và trả chẩn đoán nêu đúng khách và tọa độ.
- `test_accounting.py`: ca tính tay và phép bắt đột biến sổ cái (chạy: `python -B test_accounting.py`).
- `mutate_oracle.py`: đột biến chính oracle; mỗi đột biến phải làm bộ test đỏ.

## Kết quả

- `test_accounting.py`: 0 lỗi.
- `mutate_oracle.py`: 10/10 đột biến bị bắt. Lần chạy đầu có 2 đột biến sống sót (`M⁺` hai chiều; bỏ kiểm
  trùng lặp). Mình đã thêm hai ca `M+ counts only lateness` và `M08b`, sau đó cả 10 đều bị bắt.
- **Sửa 2026-09-25, phát hiện trên dữ liệu thật** (lần chạy `tier3-world-smoke-v1`, `../evidence/audit_vep.py`):
  - **Triệu chứng:** kiểm tính liên tục `v_t = p_{t−1}` so với giá trị `p` cuối *còn tích lũy*. Sau khi tọa độ đón
    đóng lúc lên xe, lần công bố đóng đã đưa giờ đón về giờ lên thật. Các dòng đóng tiếp theo công bố dựa trên giá
    trị đó, nên oracle báo sai là chuỗi bị đứt.
  - **Sửa:** tách `chain_p` (mọi dòng đã commit, dùng cho kiểm liên tục) khỏi `last_p` (chỉ dòng còn mở, dùng cho
    `E`).
  - **Test:** thêm ca `M11b` và đột biến "chain not advanced on closed rows". Nay 0 lỗi, và **11/11** đột biến bị
    bắt.
- Đột biến sổ cái bị bắt (nghiệm thu T3.2): sai dấu; đếm đôi; thiếu một lần công bố; reset ngân sách; nhầm
  lệch hai đầu với chuỗi; mất khách. Mọi chẩn đoán nêu `(request, coordinate)`.

## Phủ ma trận M01–M14 (Codex §15.1)

| Ca | Trạng thái |
|---|---|
| M01–M06, M11, M13, M14 | phủ bằng ca tính tay |
| M07 (bị từ chối trước ACK), M08 (thử lại) | phủ ở mức định dạng audit: dòng không `committed` bị bỏ; dòng `committed` trùng số thứ tự bị từ chối. **Việc runner chỉ ghi một lần công bố sau ACK** thuộc P06, chưa kiểm |
| M09 (đặt chỗ và lên xe cùng lô), M10 (lên xe muộn là sự thật) | **chưa phủ**: cần T3.3/T3.4 (vòng đời thật) |
| M12 (hủy trước/sau xác nhận) | **một phần**: chỉ kiểm "không xóa giá trị đã tích lũy"; kiểm duyệt dữ liệu và mẫu số cần dòng vòng đời (T3.4) |

## Phát hiện chặn việc chạy oracle trên biên bản cũ

Biên bản hiện tại (`transcript-00.ndjson`, hành động `promisePublished`) lưu `promise` (tức `p`) và ba độ lệch
**tuyệt đối** `decisionDelta`, `exogenousDelta`, `visibleDelta`; **không lưu `e`**. Vì vậy dòng audit có dấu
chỉ dựng được khi `A = 0` (khi đó `x = z`) hoặc `d = 0` (khi đó `c = z`). Khi cả hai khác 0, dấu có thể không
xác định (`signcheck.py`). Để oracle chạy trên dữ liệu mới cần một dòng audit có `v, e, p` được runner ghi ra
(ticket C02 + P03 của backlog). Đó là việc của T3.3/T3.6, có sửa lõi và hợp đồng giao thức.
