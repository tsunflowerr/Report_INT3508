# Tầng 2 — Tiền đăng ký (thăm dò có đối chứng)

Trạng thái: **niêm phong** bằng `PREREGISTRATION.sha256` (SHA-256 của tệp này, `predictions.csv` và
mã, cùng giờ UTC), sau khi các stage `controls`, `smoke`, `2b-conduct`, `2a-base-conduct` xong và
**trước** khi chạy bất kỳ job nào của `2a`, `2b-rest`, `2a-base-visible`.

Cơ sở: kế hoạch `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md` T2.6–T2.9; mã
`E:\Code\RideBound-deadline` (nhánh `research/deadline-gate`, `41a4e11` + diff chưa commit, ADR-074
Proposed); runner `E:\RideBoundData\research\runner-deadline-v1` (tree SHA-256
`8fa5dd288b0ae603dc2c044825f8089116f59953c768442eabfb5d8ca261cda8`, 429 tệp).

## 0. Những gì đã biết trước khi niêm phong

Các stage chạy trước niêm phong **không** chứa kết cục của nhánh nào được dự đoán
(`dl-*`, `dl2-*`, `visible-30` trên panel phát triển):

- `controls`: `ctl-conduct-k0`, `ctl-visible-k0` × 20 ô panel A (so với `wp14/drift-v1`).
- `smoke`: `conduct-30` k=1 ô `d20181112-s10-r1-w17`.
- `2b-conduct`: `conduct-30` k=1 × 16 ô panel phát triển.
- `2a-base-conduct`: `conduct-30` k=1 × 20 ô panel A (bổ sung so với kế hoạch: artifact lỗi của
  nhánh này trong `drift-v1` không còn, nên chạy lại trên runner mới để có quỹ đạo tham chiếu và
  thời điểm chết của đủ 20 ô).

Kết quả quan sát của các stage này được chép vào mục 9 **trước** khi niêm phong.

## 1. Kiểm tra bất biến (tất định, không phải dự đoán khoa học)

- `conduct-30` và `ctl-conduct-k0` có **đúng 0** ô nhãn `commitment-*`, ở mọi panel và mọi `k`
  (Định lý 4(a)). Sai ⟹ lỗi cài đặt, dừng.
- Nhãn `selection-noop-invariant` xuất hiện ở bất kỳ job nào ⟹ lỗi cài đặt, dừng.

## 2. Dự đoán chính — theo ô, trên đủ mọi ô

Toàn bộ `predictions.csv`, sinh bởi `holdout_predict.py` (không sửa sau niêm phong):
- 2A: `dl-30`, `dl-60`, `dl-120` × k ∈ {0, 1} × 20 ô panel A;
- 2B: `visible-30`, `dl-30`, `dl-60`, `dl-120`, `dl2-30` × k = 1 × 16 ô panel phát triển.

Quy tắc (heuristic, không phải hệ quả của định lý): trên quỹ đạo tham chiếu `conduct-30` cùng ô
cùng `k` (k = 0 panel A: `ctl-conduct-k0`; k = 1: `conduct-30-k1`), với mỗi khách và chuỗi ETA trả
đã công bố, cực đại chạy `M+`, `M` và tổng chạy `V`; `τ` = thời điểm khung quyết định đầu tiên mà
một khách vượt ngưỡng `ℓ` (ngặt); `T` = thời điểm khung quyết định **cuối** của tham chiếu nếu nó
chết, ∞ nếu hoàn tất. `τ ≤ T` ⟹ vô nghiệm do cam kết; không có `τ` và hoàn tất ⟹ không vô nghiệm
do cam kết; không có `τ` trước `T` và chết ⟹ `window-wall` (*dự đoán yếu*). Vì `T` là khung cuối
còn quyết định được, `τ ≤ T` tương đương `τ <` thời điểm chết của kế hoạch. Cờ *xa dự phòng*: tổng
thành phần hành vi `C` của tham chiếu > 60 s.

## 3. Dự đoán hướng cho 2B (từ Hệ quả 4.3; viết trong kế hoạch trước mọi số liệu 2B)

Số ô **vô nghiệm do cam kết** (8 ô mỗi khung):

| Khung | `conduct-30` | `dl-30` | `dl-120` | `dl2-30` | `visible-30` |
|---|---:|---:|---:|---:|---:|
| sáng `w08` | 0/8 | đa số (≥ 4/8) | ≤ 1/8 | ≥ `dl-30` từng ô | đa số |
| tối `w17` | 0/8 | ≤ 1/8 | 0/8 | đa số (≥ 4/8) | đa số (≥ 4/8) |

## 4. Ngưỡng xác nhận

- 2B *"xác nhận trên tập giữ lại"* khi **cả hai**: (i) dự đoán theo ô đúng ở ≥ 90% cặp (ô, nhánh)
  xác định được **trong khung tối**; (ii) hàng `w17` của bảng hướng đúng.
- 2A *"xác nhận cơ chế có đối chứng"* khi (i) dự đoán theo ô đúng ≥ 90% trên panel A và `dl-30`
  k = 1 vô nghiệm do cam kết ở đa số ô (≥ 11/20).
- Cặp "xác định được" = dự đoán không phải *dự đoán yếu*. Ca *dự đoán yếu* được báo riêng.

## 5. Điều kiện phủ định (ghi kết quả âm như kết quả dương)

- Dự đoán theo ô đúng < 75% ở khung tối ⟹ phương pháp dự đoán không chuyển được sang dữ liệu mới.
- `dl-30` tối vô nghiệm do `deadline-late` ở ≥ 3/8 ô ⟹ Hệ quả 4.3 không có răng trên khung tối này.
- `dl2-30` **và** `visible-30` tối cùng ≤ 2/8 ⟹ trôi thuận lợi của khung tối quá nhỏ để phân biệt.

## 6. Luật diễn giải khi hai loại dự đoán mâu thuẫn

Dự đoán theo ô đúng nhưng bảng hướng sai ⟹ *"Định lý 4 đúng theo ô, nhưng khung tối thật không đủ
thuận lợi để hạn chót một chiều an toàn"* — không gọi là xác nhận Hệ quả 4.3.

## 7. Phụ, thăm dò — không vào ngưỡng

Buổi tối `dl-30` nhận nhiều khách hơn `conduct-30` ở đa số ô mà cả hai hoàn tất.

## 8. Phân loại và biến nhị phân

`classify.py` (hằng thông điệp được `test_classify.py` đối chiếu với mã nguồn). "Vô nghiệm do cam
kết" = nhãn bắt đầu bằng `commitment-`. Khác tên so với kế hoạch T2.7: `noop-state-apply` đổi thành
`all-rejected/non-commitment` (cùng nghĩa: lý do được trích không phải luật cam kết); thêm
`commitment-noop-rejected/deadline-late`. Ô chết vì `window-wall` dưới nhánh hạn chót trước khi vướng
hạn chót được xếp "không vô nghiệm do cam kết" (bảo thủ, chống lại giả thuyết). Không bao giờ đếm lỗi
thay cho phân loại lỗi.

## 9. Quan sát trước niêm phong (điền trước khi niêm phong)

`repositoryInventorySha256` của worktree trong mọi run: `b54d72b58574c5aa25c76536eaa508ff9e60d54496e0dcbb4380a045bb20e8f1`.

**T2.4 đối chứng (40 job, 2026-09-24 03:20–04:41 UTC, `logs/stage-controls.log`,
`logs/compare-controls-final.log`).** So với `wp14/drift-v1` bằng `compare_controls.py`
(`levelc/decision_identity.trace`): 0 ô lệch.
- `ctl-conduct-k0`: 20/20 hoàn tất; trùng từng quyết định (kế hoạch được gán, lời hứa công bố theo
  khung, mã lý do) và số khách được nhận ở cả 20 ô (60–94 khách/ô).
- `ctl-visible-k0`: 16/20 hoàn tất, trùng từng quyết định với drift-v1; đúng 4 ô
  {16-r2, 16-r4, 17-r1, 17-r3} vô nghiệm, nhãn `commitment-all-rejected/budget`. Bộ chạy mới trích lý do
  loại của **chính no-op** ở cả bốn ô: "The candidate exceeds a hard commitment dimension."
- Pilot kiểm pipeline (`E:\RideBoundData\research\deadline-v1-pilot`, không dùng làm bằng chứng): một ô,
  trùng từng quyết định.

**Smoke** `conduct-30-k1-d20181112-s10-r1-w17-s7` (745 s): hoàn tất. Chín hệ số áp trong mô phỏng
trùng từng giá trị với `2018-11-12_tt_factors.csv` cột `travel_time_factor` chia cho giá trị tại
61200 s (1,0000; 1,0153; 1,0030; 0,9686; 0,9603; 0,9293; 0,8915; 0,8547; 0,8368), áp ở epoch quyết
định đầu tiên sau mỗi mốc 900 s; không có lỗi đến sớm. Job này là một phần tử của `2b-conduct`.

**`2b-conduct`** (16 ô, k = 1, `logs/stage-reference.log`): 13 hoàn tất, 3 `window-wall` (đều khung sáng:
12-r3-w08, 12-r4-w08, 13-r1-w08); **0** nhãn `commitment-*` (bất biến mục 1 đạt).

**`2a-base-conduct`** (20 ô panel A, k = 1): 9 hoàn tất, 11 `window-wall`; **0** `commitment-*`. So với
`wp14/drift-v1` `dr-conduct-k1` (`compare_k1.py`, `logs/compare-reference.log`): đúng 9 ô ấy hoàn tất ở cả
hai và trùng từng quyết định cùng số khách được nhận; 11 ô kia cũng đã dừng ở drift-v1 (không còn
artifact). Không có `selection-noop-invariant` ở bất kỳ job nào.

**Kiểm bộ đọc quỹ đạo** (`test_holdout.py`, cả 36 tham chiếu k = 1, `logs/test-holdout-references.log`):
`V` dựng từ chuỗi ETA trùng tổng `visibleDelta` của runner cho mọi khách; tổng `C` trùng tổng
`decisionDelta`; 0 sai lệch.

**Lỗi phát hiện trước niêm phong.** Bản `predictions.csv` đầu tiên (v0) có lỗi `inf <= inf` trong
`predict()`: ô tham chiếu hoàn tất mà không vượt ngưỡng bị đoán "vô nghiệm do cam kết". Phát hiện vì nó
đoán `dl-120` vô nghiệm ở 20/20 ô k = 0, trái với `V` tối đa 38,7 s trên panel tĩnh. Bản v0 được giữ
nguyên dưới tên `predictions-v0-BUGGY-tau-inf.csv`, **không** niêm phong và không dùng. Đã sửa, thêm
`test_predict.py` (0 lỗi), rồi sinh lại `predictions.csv` (v1, 200 dòng). Chưa có kết cục nào của nhánh
được dự đoán tồn tại khi sửa.

**Tóm tắt dự đoán v1** (số ô; `window-wall` = dự đoán yếu):

| Stage | Khung | k | Nhánh | vô nghiệm do cam kết | không | yếu |
|---|---|---:|---|---:|---:|---:|
| 2A | sáng | 0 | dl-30 / dl-60 / dl-120 | 0 / 0 / 0 | 20 / 20 / 20 | 0 |
| 2A | sáng | 1 | dl-30 | 19 | 0 | 1 |
| 2A | sáng | 1 | dl-60 | 13 | 1 | 6 |
| 2A | sáng | 1 | dl-120 | 0 | 9 | 11 |
| 2B | sáng | 1 | dl-30 / dl2-30 | 4 / 4 | 3 / 3 | 1 / 1 |
| 2B | sáng | 1 | dl-60 / dl-120 | 0 / 0 | 5 / 5 | 3 / 3 |
| 2B | sáng | 1 | visible-30 | 8 | 0 | 0 |
| 2B | tối | 1 | dl-30 / dl-60 / dl-120 | 0 / 0 / 0 | 8 / 8 / 8 | 0 |
| 2B | tối | 1 | dl2-30 | 7 | 1 | 0 |
| 2B | tối | 1 | visible-30 | 8 | 0 | 0 |

Không ô nào *xa dự phòng* (mọi tham chiếu có `C ≤ 60 s`).

**Niêm phong** gồm SHA-256 của tệp này, `predictions.csv`, và mã dùng để chạy/phân loại/phân tích
(`run_deadline.py`, `classify.py`, `holdout_predict.py`, `analyze.py`, `figure_families.py`). Nếu sau niêm
phong phải sửa `analyze.py`/`figure_families.py`, mọi thay đổi được ghi thành bản sửa có ghi ngày và lý
do; `predictions.csv` và quy tắc dự đoán không bao giờ được sửa.
