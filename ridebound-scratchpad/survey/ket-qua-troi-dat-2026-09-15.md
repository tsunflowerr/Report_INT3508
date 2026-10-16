# Thí nghiệm bơm trôi dạt — kết quả

Ghi 2026-09-15. Thí nghiệm thứ cấp, fixture và tham số mô phỏng bị sửa,
**không trộn vào bảng niêm phong**. Không ghi gì vào repository.

---

## 0. Câu hỏi

Ba định lý về cơ sở tính sổ đúng trên giấy nhưng **rỗng trên panel niêm phong**:
đồ thị thời gian di chuyển tĩnh nên trôi dạt `d` chỉ p50 = 4.9 s, và hai cơ sở
cho gần như cùng đáp số (1294 so với 1294 khách).

Câu hỏi: **khi tắc đường là thật, hai cơ sở có tách ra không?**

Dự đoán, viết **trước** khi chạy:

1. Cơ sở hành vi (A) khả thi 20/20 ô ở **mọi** mức trôi dạt — no-op có `p = e`
   nên bị tính 0 bất kể `d` (Định lý 1). *Mất dù một ô là Định lý 1 sai.*
2. Cơ sở kết quả (B) mất dần ô khi `d` tăng — no-op vẫn bị tính `d` (Định lý 2).
3. Khoảng cách phục vụ A − B giãn theo `d`.

---

## 1. Cách bơm trôi dạt

**Không phải nhiễu nhân tạo.** Bộ dữ liệu FleetPy Manhattan có sẵn hệ số thời
gian di chuyển đo thật, 15 phút một mốc, từng ngày
(`<ngày>_tt_factors.csv`, 96 mốc/ngày). Trong khung 08:00–10:00 của mình, cao
điểm sáng làm thời gian di chuyển **tăng 17–26%** tuỳ ngày, đơn điệu.

```
factor(t) = ( f_thật(28800 + t) / f_thật(28800) ) ** k
```

- `k = 0` → hệ số luôn 1.0, tái lập chính xác baseline
- `k = 1` → đúng ngày thật
- `k = 2` → nhân đôi độ lệch (span tới 1.376×)

Chuẩn hoá theo mốc đầu khung nên `factor(0) = 1.0` tuyệt đối — cần thiết vì
preflight kiểm tra lúc khởi tạo rằng bộ định tuyến tái tạo đúng thời gian di
chuyển của fixture. Trôi dạt chỉ tích luỹ **sau** phép kiểm tra đó.

**Cơ chế đã có sẵn, không sửa repo:**
- `NetworkBasic._current_tt_factor` nhân vào mọi truy vấn định tuyến
  (`NetworkBasic.py:348, :427`); `_add_to_database` là no-op trong lớp này nên
  không có cache cũ phía FleetPy
- bridge có sẵn cờ `_rb_travel_dirty` → dựng lại snapshot → phát
  `travelTimesUpdated` (`fleet_control.py:396`)
- wrapper trong scratchpad import module thật rồi chỉnh hệ số qua
  `_trigger_and_resolve`, xoá `_rb_travel_arc_cache`, bật cờ

Xác minh cơ chế chạy: snapshot trong transcript tăng từ **1 lên 9**.

---

## 2. Trôi dạt đo được

`d` = tổng exogenousDelta cộng dồn mỗi khách (pickup + drop ETA).

| mức | khách | d p50 | d p90 | d max | **% khách mà riêng `d` đã vượt trần 30 s** |
|---|---|---|---|---|---|
| k=0 phẳng | 1581 | 4.9 s | 10.8 s | 39.9 s | **0.2%** |
| k=1 Manhattan thật | 583 | 14.1 s | 47.4 s | 150.7 s | **22.8%** |
| k=2 nhân đôi | 79 | 10.9 s | 69.9 s | 157.0 s | 20.3% |

**Cảnh báo phải ghi kèm:** k=1 và k=2 chỉ tính trên những ô sống sót qua bức
tường ở mục 4, nên có thiên lệch sống sót (ô sống có thể là ô ít tắc hơn).
Con số k=0 là trên đủ 20 ô.

---

## 3. Kết quả chính — phân loại theo **nguyên nhân thật**

Đếm hỏng thôi thì sai. Phải mở log phân loại từng run:

| arm | chạy được | **vô nghiệm do CAM KẾT** | hỏng do giao thức |
|---|---|---|---|
| conduct-k0 | 20 | **0** | 0 |
| visible-k0 | 16 | **4** | 0 |
| conduct-k1 | 9 | **0** | 11 |
| visible-k1 | 0 | **19** | 1 |
| conduct-k0 @cửa sổ 900 | 20 (=1753) | **0** | 0 |
| visible-k0 @cửa sổ 900 | 15 | **5** | 0 |
| conduct-k1 @cửa sổ 900 | 0 | **0** | 20 |

### 3.1 Định lý 1 đứng vững

**Cơ sở hành vi có đúng 0 lần vô nghiệm do cam kết, ở mọi mức trôi dạt, trên
mọi cấu hình cửa sổ.** Mọi ca hỏng của nó đều là bức tường ở mục 4 — thứ đập
vào cả hai cơ sở như nhau.

*Suýt báo sai:* thoạt nhìn "conduct hỏng 11/20 ở k=1" trông như phản ví dụ.
Chỉ khi mở log mới thấy nguyên nhân khác hẳn. Bài học: **runner phân loại hỏng
theo chuỗi khớp thô là không đủ; phải phân loại theo mã lỗi thật.**

### 3.2 Định lý 2 được xác nhận, mạnh hơn dự kiến

```
d p50 = 4.9 s    →  cơ sở kết quả vô nghiệm  4/20 ô
tắc đường thật   →  cơ sở kết quả vô nghiệm 19/20 ô
```

Dưới tắc đường Manhattan **có thật, chưa khuếch đại**, cơ sở kết quả sụp trên
**19/20 ô**: điều phối viên không còn *bất kỳ* quyết định hợp lệ nào, kể cả
không làm gì. Cùng điều kiện, cơ sở hành vi: **0**.

Cơ chế, bằng số: ở k=1, **22.8% khách tích luỹ hơn 30 giây trôi dạt thuần tuý
do giao thông**. Dưới cơ sở kết quả, ngân sách của họ thủng vì thời tiết —
nhà xe bị tính phí cho việc không làm gì. Dưới cơ sở hành vi, cùng những khách
đó tốn 0.

### 3.3 Nối vào Fielbaum & Alonso-Mora (2020)

Kịch bản "fully controlled" của họ **chính là** cơ sở kết quả với β = 0, và nó
làm tỉ lệ từ chối nhảy 34.5% → 45.6% (+11.1 pp). Kết quả trên giải thích vì sao,
và chỉ ra phần nào của cái giá đó **tránh được bằng cách đổi cơ sở tính**.

*Giới hạn:* kịch bản của họ siết hai thứ cùng lúc (ratchet **và** cấm huỷ), nên
đây là **cơ chế có bằng chứng**, không phải quy kết định lượng đã chứng minh.

### 3.4 Điều KHÔNG lấy được

**So sánh số khách phục vụ A − B dưới trôi dạt.** Bức tường ở mục 4 giết quá
nhiều ô của cơ sở hành vi nên không còn tập ô chung đủ lớn. Kết quả ở mục 3 là
về **tính khả thi**, không phải về tỉ lệ phục vụ. Phải nói rõ điều này.

---

## 4. Phát hiện phụ: một bất biến miền chặn tắc đường

```
RBWP7_RUNNER_PROTOCOL_ERROR: SCHEMA_VALIDATION_FAILED:
Actual pickup time must remain inside the accepted pickup window.
```

Nguồn: `src/RideBound.Domain/Requests/RideRequest.cs:266-273` — khi hành khách
lên xe, nếu `pickupTime` nằm ngoài `[EarliestPickup, LatestPickup]` thì thất bại.

Đây là **bất biến miền**, không phải chính sách: nó bắn bất kể cơ sở nào, bất kể
nguyên nhân gì. Khi tắc đường làm xe đang trên đường đón đến muộn hơn cửa sổ đã
chấp nhận lúc nhận khách, run chết.

**Nới cửa sổ không cứu được.** Thử lại toàn bộ trên fixture cửa sổ 900 s: hỏng
**20/20**, vẫn đúng lỗi đó. Lý do khớp với phép đo chất lượng dịch vụ hôm nay:
bộ tối ưu **tiêu hết phần nới** (chờ trung vị 407 → 636 s), nên khoảng đệm tuyệt
đối không tăng.

Phát biểu tổng quát:

> **Một cửa sổ đón cố định, chấp nhận trước khi cao điểm hình thành, thì sau đó
> không giữ nổi — bất kể điều phối làm gì. Và nới cửa sổ không tạo ra đệm, vì
> bộ tối ưu lập kế hoạch sát mép bất kỳ cửa sổ nào được cho.**

ADR-045 trong repo đã ghi nhận lớp vấn đề này từng "chặn WP9". Thí nghiệm này
định vị chính xác dòng code và định lượng được nó.

Hệ quả cho mô hình: **RideBound hiện không biểu diễn được trạng thái mà riêng
giao thông đã phá vỡ một cửa sổ đón đã chấp nhận.** Đây là ranh giới của hệ
thống, đáng viết thành một mục trong khoá luận.

---

## 5. Cái gì chứng minh, cái gì đo

| | trạng thái |
|---|---|
| Định lý 1: cơ sở hành vi luôn thoả | chứng minh + **đo, 0 vi phạm trên 69 run có trôi dạt** |
| Định lý 2: cơ sở kết quả có thể vô nghiệm | chứng minh + **đo, 4/20 → 19/20 khi `d` tăng** |
| Định lý 3: B ≥ A nên B phục vụ ≤ A | chứng minh; **đo được về khả thi, chưa đo được về tỉ lệ phục vụ dưới trôi dạt** |
| Cửa sổ cố định không sống qua cao điểm | **đo, 31/40 run** |

---

## 6. Nguồn dữ liệu

| | |
|---|---|
| Hệ số tắc đường thật | `E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f.../FleetPy_Manhattan/networks/Manhattan_2019_corrected/<ngày>_tt_factors.csv` |
| Thang trôi dạt, cửa sổ 600 s | `E:/RideBoundData/wp14/drift-v1` (46 run hoàn chỉnh) |
| Thang trôi dạt, cửa sổ 900 s | `E:/RideBoundData/wp14/driftwide-v1` (15 run hoàn chỉnh) |
| Wrapper bơm trôi dạt | `scratchpad/drift/preflight_drift.py` |
| Wrapper trôi dạt + cửa sổ rộng | `scratchpad/drift/preflight_drift_wide.py` |
| Cấu hình cơ sở kết quả | `scratchpad/drift/basis-customer-visible.json` (khác cấu hình gốc **đúng 1 lá**: `budgetBasis`) |
| Runner | `scratchpad/drift/run_drift.py`, `run_driftwide.py` |
| Đối chứng | `conduct-k0` = 1581 = C1 niêm phong; `visible-k0` hỏng đúng bộ ô cũ `{16-r2, 16-r4, 17-r1, 17-r3}` |
