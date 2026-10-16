# RideBound — Báo cáo trạng thái, 2026-09-15

Tổng hợp toàn bộ những gì đã làm, đã đo, đã thử và đã loại, cùng các hướng còn mở.
Không ghi gì vào repository; mọi kết quả nằm ở `E:/RideBoundData` và scratchpad.

---

## 1. Hệ thống này làm gì

RideBound là bộ điều phối xe đi chung (ride-pooling) được xây quanh một ý niệm:
**lời hứa có biên được chứng nhận** (certified bounded promise).

Khi nhận một khách, hệ thống **công bố** giờ đón và giờ trả. Sau đó nó vẫn liên tục
tối ưu lại khi có khách mới, nhưng mọi lần dời lời hứa đều bị **tính vào một sổ nợ
theo từng hành khách, cộng dồn và chỉ tăng**, và so với một **trần β**. Vượt trần thì
phương án bị xoá khỏi tập lựa chọn.

Phần khác biệt về kỹ thuật là **phân rã ba mốc** ở mỗi lần công bố:

| Mốc | Nghĩa |
|---|---|
| `v` previous | lời hứa đã công bố lần gần nhất |
| `e` exogenous | **chính kế hoạch cũ đó**, chiếu lại từ vị trí thật hiện tại của xe |
| `p` proposed | lời hứa mà phương án đang xét sẽ tạo ra |

Từ đó: `decisionDelta = |p − e|` (do quyết định gây ra), `exogenousDelta = |e − v|`
(trôi dạt vật lý), `visibleDelta = |p − v|` (khách nhìn thấy).

---

## 2. Trạng thái kỹ thuật

| Hạng mục | Trạng thái |
|---|---|
| Mô phỏng | FleetPy 1.0.2, Manhattan TLC công khai (CC-BY) |
| Panel | 20 ô: 5 ngày × 4 lần lặp, 108 khách/ô, 8 xe × 4 chỗ, 2 giờ |
| Cửa sổ đón | 600 s; max-ride 1.5× thời gian trực tiếp |
| Hạt giống | master-seed 7, cố định mọi arm |
| Niêm phong | `semanticHash`, `publicationDigest`, `runnerSha256`, freeze receipt |
| Runner niêm phong | `h6-confirmatory-v1` (8445f053) |
| Runner thứ cấp | `ratchet-secondary-v1` (931114e2) — kết quả để bảng riêng |
| Solver | OR-Tools, set-packing ILP |
| Tổng đã chạy | **261 run**, 18.1 GB (còn trống 93 GB) |

---

## 3. Kết quả đã có

### 3.1 Chân A — quy trách nhiệm

Trong 83,587 giây xê dịch mà hành khách nhìn thấy ở arm B1, **89.06%** (74,443 s)
là do quyết định điều phối, không phải do vật lý. Ở C1 con số này còn **1.37%**.

Tập trung chứ không dàn đều: **403 / 1,735 khách (23.2%) hứng toàn bộ**. Trung bình
mỗi người bị dời 155 s; người khổ nhất 840.9 s (~14 phút). Ở C1, **95% khách bị dời
đúng 0 giây**.

Lưu ý câu chữ: bất đẳng thức tam giác cho `B ≤ A + d`, nên 89.06% là một **tỉ số**,
không phải một phân hoạch (phần hụt 0.00–0.07%).

### 3.2 Chân B — đường cong đánh đổi (141 run)

| arm | lời hứa | phục vụ | vs B1 (pp) | xê dịch do quyết định | khổ nhất | số bị dời |
|---|---|---|---|---|---|---|
| B1 | không hứa gì | 1735 | 0 | 74,443 s | 841 s | 403 |
| nobudget | cùng xe, cùng điểm dừng | 1655 | −3.70 | 22,485 s | 595 s | 142 |
| budget300 | + trần 300 s | 1641 | −4.35 | 15,809 s | 291 s | 128 |
| budget120 | + trần 120 s | 1608 | −5.88 | 5,063 s | 119 s | 76 |
| budget60 | + trần 60 s | 1579 | −7.22 | 1,109 s | 59 s | 34 |
| **C1** | **+ trần 30 s** | **1581** | **−7.13** | **128 s** | **28 s** | **11** |
| nopickuplock | không khoá ETA đón | 1583 | −7.04 | 187 s | 34 s | 13 |
| freeze300 | khoá trong 300 s cuối | 1583 | −7.04 | 187 s | 34 s | 13 |
| freeze600 | khoá trong 600 s cuối | 1581 | −7.13 | 128 s | 28 s | 11 |

Trần **luôn được tôn trọng**: 291 < 300, 119 < 120, 59 < 60, 27.6 < 30.

Hai điều đáng ghi:

- **Thang khoá ETA đón sụp về đúng 2 hành vi.** freeze600 ≡ C1 trên cả 6 thước đo.
  Không phải lỗi copy config — `semanticHash` và `publicationDigest` khác nhau 20/20 ô.
  Lý do đo được: **0.0% lần công bố xảy ra sớm hơn 600 s trước giờ đón**, vì chân trời
  đặt chỗ đúng bằng 600 s. Một hàng rào 600 s không bao giờ mở.
- **Hiệu suất siết chặt là đơn điệu giảm**, dù chi phí biên thì không:
  14,043 → 10,271 → 7,024 → 3,948 giây ổn định mua được trên mỗi điểm phần trăm mất đi.

### 3.3 Chân C — hành vi so với kết quả

Hai cách tính sổ: **cách A (hành vi)** tính `|p − e|`, **cách B (kết quả)** tính `|p − v|`.

| trần | A khả thi | B khả thi | A phục vụ | B phục vụ |
|---|---|---|---|---|
| 30 s | **20/20 ô** | 16/20 ô | 1294 | 1294 |
| 120 s | **20/20 ô** | 16/20 ô | 1267 | 1266 |

Ba định lý (chứng minh, không phải đo):

1. **Cách A luôn thoả được.** Phương án no-op có `p = e`, nên `delta = 0`.
2. **Cách B có thể vô nghiệm.** No-op vẫn bị tính phí trôi dạt `d`.
3. **`B = A + d ≥ A`**, nên tập khả thi của B ⊆ của A ⟹ **B không bao giờ phục vụ
   nhiều hơn A, với mọi β.**

### 3.4 Chân D — vững với thước đo

9 thước đo (tuyến tính, bậc hai, có trọng số bậc thang, trọng số gần kề, đếm, khổ
nhất, p95, p99, số người bị dời) × 6 arm: **đơn điệu, không một ngoại lệ**.

Đối chứng: tỉ lệ phục vụ thì **vi phạm đơn điệu ở 8/20 ô** — nên thứ tự các arm theo
độ ổn định vững hơn theo dịch vụ.

### 3.5 Thí nghiệm thứ cấp — ratchet (80 run, runner riêng)

Hai arm đối chứng tái lập **chính xác** kết quả niêm phong (0/20 ô khác). Kết luận:

- `ratchet` ≡ khoá cứng trên cả 8 thước đo (`semanticHash` khác 20/20 ô)
- `freeze300ratchet` ≡ `nopickuplock` — **dự đoán trước khi chạy, đúng y hệt**

### 3.6 Chứng chỉ không do cắt xén tìm kiếm

Kết quả không phải sản phẩm của việc tìm kiếm bị cắt ngắn:

- 0% ngân sách công việc bị cạn, 0% chạm trần số ứng viên
- 0 ứng viên khả thi bị bỏ sót, 0 nhánh chưa mở rộng
- **94% số lần loại là do vật lý**: PICKUP_WINDOW 94,021 + MAX_RIDE_TIME 25,300,
  so với cam kết 454 (1.1%)
- trung vị 1 ứng viên được giữ lại trên mỗi xe

### 3.7 Mới (2026-09-15) — cửa sổ đón chặn ở đâu

Phân tích 119,560 lần loại ứng viên trên B1:

| lý do | số lần | tỉ lệ |
|---|---|---|
| PICKUP_WINDOW | 94,021 | **78.64%** |
| MAX_RIDE_TIME | 25,300 | 21.16% |
| CAPACITY | 239 | 0.20% |

Nhưng "ứng viên bị loại" khác "khách bị từ chối". Tách riêng 425 khách bị từ chối:

- **cả 425/425 đều có ứng viên chết vì cửa sổ**
- phần vượt cửa sổ **nhỏ nhất** của mỗi khách: p25 = 14.0 s, **p50 = 44.4 s**,
  p75 = 93.2 s, p90 = 174.5 s
- so với toàn bộ ứng viên bị loại thì trung vị vượt tới 309.7 s

Nghĩa là **đa số ứng viên hỏng nặng, nhưng ứng viên tốt nhất của mỗi khách bị từ chối
chỉ lỡ trong gang tấc.** Hệ thống đang vứt 425 khách để tiết kiệm trung vị 44 giây.

Cảnh báo: đây là **cận trên lạc quan**. Validator dừng ở vi phạm đầu tiên, nên một
ứng viên lỡ 44 s có thể vẫn chết vì max-ride ngay sau đó (4,613 lần trên chính nhóm này).

### 3.8 Mới (2026-09-15) — thước đo của Fielbaum & Alonso-Mora 2020 trên dữ liệu mình

Cài đúng định nghĩa của họ (Δ = thực tế − lần báo đầu, cắt âm) lên transcript của mình:

| | **B1** | **C1** |
|---|---|---|
| P(ΔD > 0) | 0.2329 | 0.0076 |
| E(ΔD \| ΔD>0) | 160.4 s | 10.5 s |
| Thước hai-đầu của họ (drop) | 64,814 s | 126 s |
| Thước chuỗi của mình (drop) | 71,529 s | 6,822 s |
| **tỉ số chuỗi / hai-đầu** | **1.1×** | **54.1×** |
| khách họ chấm 0 nhưng thực tế bị dời | 663 (38.2%) | 774 (49.0%) |

Đọc kết quả này:

1. **Trên B1 hai thước gần như trùng nhau (1.1–1.2×).** Điều này **kiểm định chéo**
   thước của mình: nó không bịa ra chuyển động.
2. **Trên C1 hai thước lệch 24–54 lần.** Vì chế độ cam kết đẩy lời hứa quay về gần
   giá trị ban đầu, mà thước hai-đầu **không nhìn thấy đường đi**, chỉ nhìn hai điểm.
3. **Thước của họ chấm 0 cho 49% số khách thực sự bị dời** dưới chế độ cam kết.
4. Thước đếm của họ (Định nghĩa 9) **không phân biệt nổi B1 với C1**: 14.99 so với
   13.45 lần tăng trung bình, trong khi hai arm cách nhau 7.13 pp dịch vụ.
   *Cảnh báo:* hệ thống mình công bố lại lời hứa ~30 lần mỗi khách, còn họ cập nhật
   mỗi δ = 1 phút (~5 lần), nên **không được so con số NC này với con số trong bài họ**.
   Chỉ so B1 với C1 trong nội bộ dữ liệu mình mới hợp lệ.

---

## 4. Đã thử và đã loại — kèm lý do

| Hướng | Vì sao loại |
|---|---|
| Đệm ETA đồng loạt | cần 265,000 s đệm để tránh 22,485 s xê dịch — tỉ lệ 12:1 |
| Hứa theo hạn chót thay vì điểm | đó **chính là** Ω/Δ đã có sẵn |
| Sinh ứng viên có ý thức về cam kết | p10 phần vượt là 31 s trên trần 30 s; nới lên 60 s chỉ lấy lại 9.9% |
| Sắp xếp lại thứ tự khách cũ | **0 lần đảo thứ tự** trong toàn bộ dữ liệu; phép thử láng giềng 8.3× cho 98.63% vô nghiệm, 0 khách lấy lại |
| **Cổng mềm** (`SoftHardHybrid`) | **đã kiểm tra code hôm nay: cổng cứng KHÔNG bị gỡ.** `retained.Add()` chỉ chạy sau khi qua chặn cứng; cảnh báo chỉ đổi **thứ hạng**, không nhận lại ứng viên nào. Thêm nữa `warningLimit (60 s) > hardLimit (30 s)` là lỗi chặn cứng `INVALID_COMMITMENT_WARNING_LIMIT` → ghép với C1 sẽ **chết 20/20 ô**. Muốn chạy hợp lệ phải ghép với budget120, và khi đó nó **không** thu hẹp khoảng cách về nobudget |

### Một đính chính quan trọng về dữ liệu

Panel này có **đúng một snapshot thời gian di chuyển** cho cả 2 giờ (đã kiểm tra:
`travelSnapshots` dài 1; toàn transcript chỉ 1 định danh snapshot; 108 sự kiện đều là
`requestArrived`).

Nên trôi dạt `d` **không đến từ tắc đường** mà từ **độ trễ thực thi** (xe chạy theo bước
rời rạc, có thời gian dừng đón trả). Đó là lý do `d` nhỏ: p50 = 4.9 s, max = 39.9 s.

Hệ quả: đẳng thức `B = A + d` vẫn đúng chính xác, nhưng khẳng định "A và B gần như không
khác nhau" là **tính chất của panel này**, không phải của bài toán. Khoảng cách A–B
**không giãn theo β — nó giãn theo `d`**.

---

## 5. Đối chiếu văn liệu — điều quan trọng nhất tuần này

Lấy được toàn văn **Fielbaum & Alonso-Mora (2020)**, *"Unreliability in ridesharing
systems"*, TR-C 121:102831. Đây là bài trùng với mình, và trùng nhiều.

**Họ đã làm (mình không được nhận là mới):** khái niệm lời hứa bị xê dịch (Def 3);
phân loại nguyên nhân khách/nhà-điều-hành (Def 1/2, định tính); đo độ lớn mỗi khách
(Δt_w, Δt_d, ΔD); đếm số lần đổi (Def 9); phân bố theo vùng; **đường cong đánh đổi**
(§6, Table 5); **ratchet trên ETA đón** ("fully controlled"); cấm huỷ-sau-nhận
("intermediate").

**Table 5 của họ:** Base 34.5% từ chối → Intermediate 31.2% → **Fully controlled 45.6%**.

**So tương đối với mình:**

| | Gốc | Siết chặt | Tuyệt đối | **Tương đối** |
|---|---|---|---|---|
| Họ | 34.5% | 45.6% | +11.1 pp | **1.32×** |
| Mình (B1→C1) | 19.68% | 26.81% | +7.13 pp | **1.36×** |

Đọc trung thực: tính theo pp mình rẻ hơn, nhưng **theo tỉ lệ thì mình nhỉnh về phía
xấu**. Đây là **tái lập độc lập trên instance nhỏ hơn 185 lần**, không phải chiến thắng.

**Mã nguồn của họ:** đã tìm — không bài nào có tuyên bố công bố mã nguồn, không có
repo GitHub. Chỉ tìm thấy các bản cài đặt **không chính thức** của Alonso-Mora 2017
(`Starcutter/RideSharing`, `matsim-org/alonso-mora`), không phải bài 2020.
⟹ **Không chạy head-to-head được.** Cách so sánh khả dĩ duy nhất là cài **thước đo**
và **cơ chế** của họ lên dữ liệu của mình — cả hai đã làm xong (§3.8 và arm `ratchet`).

**Còn lại là của mình:**

1. **Trần số β** trên xê dịch cộng dồn. Họ chỉ có 3 chế độ bật/tắt. Câu cuối §6 của
   họ: *"This reinforces the need of more sophisticated ideas to control unreliability."*
2. **Dạng cộng dồn theo chuỗi** — điều kiện cần để đặt trần được, và §3.8 vừa cho thấy
   nó bắt được thứ thước hai-đầu bỏ sót 24–54 lần.
3. **Câu hỏi cơ sở A/B và ba định lý.** Không diễn đạt được trong mô hình họ.
4. **Bảo đảm khả thi** (Định lý 1) — và nó **giải thích** con số 45.6% của họ:
   "fully controlled" chính là cơ sở B với β = 0, mà cơ sở B có thể vô nghiệm.
   *Giới hạn:* kịch bản của họ siết hai thứ cùng lúc, nên đây là **cơ chế có bằng chứng**,
   không phải quy kết đã chứng minh.

**Bài Scale analysis** (bài được gửi lại) **không trùng**: đó là kinh tế học quy mô,
không có lời hứa công bố nào, chỉ chung cỗ máy RTV/ILP. Nó tự khai chỗ trống ở §4.1 và
chỉ sang bài 2020.

---

## 6. Chiếu vào ba tiêu chí KLTN

| Tiêu chí | Trạng thái | Căn cứ |
|---|---|---|
| Bài toán thực tế, quan trọng, đáng làm | ✅ **vững** | Alonso-Mora: *"this is not a minor issue"*; Alonso-González 2020 định giá độ tin cậy bằng tiền |
| Giải pháp mới hơn / giới hạn tốt hơn | ⚠️ **chỗ yếu nhất** | đo đạc trùng bài 2020; cái mới còn lại là trần β, dạng cộng dồn, và định lý A/B |
| Minh chứng định lượng | ✅ **rất mạnh** | 261 run, niêm phong, 9 thước đo, chứng chỉ không cắt xén, tái lập được kết quả của bài 2020 |

Tiêu chí 1 và 3 đạt. **Tiêu chí 2 là việc còn lại phải làm.**

---

## 7. Đang chạy và sẽ làm

### Đang chạy

**Phép thử trần cửa sổ.** Fixture viết lại với cửa sổ 900 s thay vì 600 s (20 ô, mọi
tự kiểm tra qua), cùng runner niêm phong, cùng cấu hình, cùng hạt giống. Hai arm B1 và
C1, 40 run, ~1.5 h, ~2.2 GB.

Phải vượt hai chỗ chặn kỹ thuật:
- driver giữ `sourceScenarioContentSha256` → vá cả hai, bản sao trong scratchpad
- `op_max_wait_time = 600` **hard-code trong preflight** → FleetPy kẹp cửa sổ về 600 và
  bắn `PlanRequest scalar round-trip drift`. Xử lý bằng wrapper trong scratchpad
  import module thật rồi thay đúng một giá trị; **repository không bị sửa**

Bốn con số sẽ có:

```
B1@600 = 1735 (niêm phong)      C1@600 = 1581 (niêm phong)
B1@900 = ?                      C1@900 = ?
```

- **C1@900 > B1@600 ⟹ RideBound thắng trên cả hai trục cùng lúc** (vừa phục vụ nhiều
  hơn vừa giữ lời hứa). Cần lấy lại > 154 khách.
- **B1@900 ≈ B1@600 ⟹ đội xe mới là chặn thật, không phải cửa sổ.** Hướng này chết rẻ.

Đây là **phép thử trần**, không phải cơ chế. Nới đồng loạt cho optimizer nhiều tự do
hơn mọi cách nới có chọn lọc, nên nếu trần không đủ cao thì thương lượng cũng vô ích.

### Sẽ làm nếu trần đủ cao

**Cửa sổ thương lượng một lần.** Khi một khách sắp bị từ chối vì lỡ cửa sổ δ giây,
không từ chối và cũng không nới cửa sổ cho cả hệ thống: báo giờ đón thật (trễ hơn δ),
rồi **khoá lời hứa đó bằng trần β**.

Vì sao hướng này hợp với luận điểm, còn cổng mềm thì phá nó:

| | Cổng mềm | Cửa sổ thương lượng |
|---|---|---|
| Lời hứa sau khi công bố | **có thể vỡ** | vẫn cứng, vẫn khoá bằng β |
| Định lý 1 | **mất** | **giữ** |
| Thương lượng xảy ra | liên tục, sau lưng khách | **một lần, trước khi cam kết** |
| Cần sửa code | có | không |

### Còn mở, chưa xin phép

**Bơm trôi dạt giao thông.** `d` trên panel này nhỏ vì đồ thị tĩnh. Dự đoán kiểm chứng
được: tăng biên độ trôi dạt thì số ô **vô nghiệm dưới cơ sở B** tăng, còn cơ sở A giữ
**20/20** ở mọi biên độ (hệ quả trực tiếp của Định lý 1). Đây là dự đoán **trước khi đo**;
sai thì Định lý 1 sai. Cần sửa fixture ⟹ thí nghiệm thứ cấp riêng.

### Còn thiếu từ phía anh

- **Đề cương / tiêu chí chấm chi tiết** (số chương, độ dài) — để biết nên tách
  "tái lập bài 2020" thành mục riêng hay gộp vào chương khảo sát văn liệu.

---

## 8. Nguồn dữ liệu

| Hạng mục | Vị trí |
|---|---|
| Panel niêm phong | `E:/RideBoundData/wp9/confirmatory-h6-panela-v2` (61 run, 3.39 GB) |
| Frontier | `E:/RideBoundData/wp9/frontier-v1` (141 run, 7.77 GB) |
| Ratchet thứ cấp | `E:/RideBoundData/wp14/ratchet-secondary-v1` (80 run, 4.30 GB) |
| Cơ sở B thăm dò | `exploratory-visible-basis-v1`, `exploratory-visible-sweep-v1` (52 run, 2.58 GB) |
| Fixture cửa sổ rộng | `E:/RideBoundData/wp14/wide-window-fixture` |
| Kết quả cửa sổ rộng | `E:/RideBoundData/wp14/wide-window-v1` |
| Toàn văn 2 bài Alonso-Mora | `scratchpad/survey/unreliability.txt`, `scale.txt` |
| Script đo | `scratchpad/measure/`, `scratchpad/welfare/`, `scratchpad/window/`, `scratchpad/frontier/` |
| Tài liệu định lý | `scratchpad/survey/dinh-ly-conduct-vs-outcome.md` |
| Kết quả A/C/D | `scratchpad/survey/ket-qua-A-C-D.md` |
