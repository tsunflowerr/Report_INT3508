# Bổ sung đề xuất cho "Kết quả benchmark"

Soạn ngày 2026-09-08. **Đây là bản nháp rời** — không chèn thẳng vào báo cáo.
Mỗi mục độc lập, bạn lấy mục nào thì lấy. Mọi con số đều trích từ evidence đã
niêm phong hoặc từ mã nguồn, có ghi nguồn.

Ba mục đầu là **sửa lỗi** — nên làm bất kể còn lại. Bốn mục sau là bổ sung.

---

## S1. Sửa: `exogenousDelta` không phải "tắc đường"

**Báo cáo hiện gọi sai.** Travel time trong mọi lần chạy là **tĩnh**.

Bằng chứng, ba tầng:

1. `simulators/fleetpy-ridebound/ridebound_fleetpy/fleet_control.py:396` — sự kiện
   `travelTimesUpdated` chỉ phát khi cờ `_rb_travel_dirty` bật.
2. Cờ đó chỉ được bật bởi `inform_network_travel_time_update` (dòng 461), mà
   FleetPy chỉ gọi khi `NetworkBasic.update_network` tìm thấy file travel-time
   cho mốc thời gian đó — bộ dữ liệu của chúng tôi không có file nào như vậy.
3. **Kiểm chứng bằng dữ liệu:** `semantic.travelSnapshotVersion = 1` trên
   **cả 50 bundle** của H6 Panel A. Không có lần cập nhật thứ hai nào.

**Vậy `exogenousDelta` là gì?** Mốc phản thực được dựng bằng cách chiếu lại
**đúng tuyến cũ, đúng phân công cũ, từ vị trí xe thật tại thời điểm hiện tại**
(`src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:317-322`).
Nên nó bắt phần trôi tích luỹ **giữa hai lần quyết định**: xe đã đi được, thời
gian chờ và phục vụ thực tế lệch khỏi lịch `earliest-feasible` đã dự phóng.

**Cách gọi đúng: "trôi do hiện thực hoá" (realization drift)**, không phải tắc đường.

**Và nên trình bày đây là điểm mạnh, không phải điểm yếu.** Mốc phản thực được
định nghĩa **theo cơ chế** — "cùng tuyến, cùng phân công, chiếu lại lúc này" —
nên nó hấp thụ *mọi* trôi phi-quyết-định bất kể nguồn gốc, và sẽ hoạt động không
đổi nếu travel time trở thành ngẫu nhiên. Đó là định nghĩa tổng quát hơn "trừ đi
tắc đường".

> Đối chiếu: Fielbaum & Alonso-Mora (2020) xử lý cùng vấn đề bằng **thiết kế thí
> nghiệm** — họ chỉ chạy 13–15 giờ, ngoài cao điểm, để *"disregard unreliability
> due to traffic conditions"* (Mục 5). Cách đó không dùng được cho giờ cao điểm.
> WP14 của chúng tôi có khung 17:00–19:00.

---

## S2. Sửa: ghi rõ 99,86% là giảm trên đại lượng nào

Báo cáo đang nêu mức giảm gánh nặng mà không nói rõ mẫu số. Có **hai** con số,
cả hai đều đúng, và chúng khác nhau nhiều:

| | b1-ref | c1-h6ref | mức giảm |
|---|---:|---:|---:|
| Gánh nặng **quy trách cho quyết định** (ms) | 59.250.164 | 83.373 | **99,86%** |
| Gánh nặng **khách thực sự cảm nhận** (ms) | 65.992.813 | 7.102.950 | **89,24%** |

*(WP14, 16 cell, 1.728 khách/arm — `wp14r-011-v6-full-matrix-frontier-v1-summary.json`)*

**99,86%** là phần hệ thống tự gây ra. **89,24%** là phần khách cảm nhận — và đó
mới là con số so được với văn liệu. Báo cáo phải nêu cả hai và nói rõ cái nào là cái nào.

Lý do chênh: mức giảm **cảm nhận** bão hoà ở ~89% vì thành phần ngoại sinh
(~7,0 triệu ms) không policy nào xoá được. Xem S4.

---

## S3. Sửa: B1 **không phải** baseline "tái gán tự do"

Đây là điều phải nêu rõ để người đọc không hiểu nhầm phạm vi kết quả.

Ba bất biến trong mã, áp dụng cho **mọi** policy kể cả B1:

| Bất biến | Vị trí | Hệ quả |
|---|---|---|
| `Reject()` chỉ hợp lệ từ trạng thái `Pending` | `RideRequest.cs:236-238` | không thể loại khách đã nhận |
| `PhysicalViolationCodes.Reassignment` | `PhysicalPlanValidator.cs:682-693` | không thể đổi xe của khách đã nhận |
| `ValidateAcceptedPreservation` (gọi vô điều kiện) | `PhysicalPlanValidator.cs:178` | phải giữ mọi điểm dừng của khách đã nhận |

Cộng với `InsertionCandidateGenerator` chỉ xét khách `Pending`
(`InsertionCandidateGenerator.cs:54-55`).

⟹ **Quyền tự do duy nhất của B1 là xếp lại thứ tự điểm dừng trong chính chiếc xe
đã gán.** Trong hệ của Fielbaum & Alonso-Mora, **6,85%** khách đã nhận bị loại về
sau; ở đây con số đó là 0 về mặt cấu trúc.

**Hệ quả cho cách diễn giải −154:** con số đó là giá của phần **đóng băng ETA thêm
vào**, trên nền một baseline vốn đã cam kết xe và đã bảo đảm không bị loại. Nó
**không** phải giá của toàn bộ cam kết.

---

## B1. Toàn bộ mất mát là **từ chối thẳng**, và mọi khách được nhận đều đến nơi

| | nhận | từ chối | tổng |
|---|---:|---:|---:|
| H6-A B1 | 1.735 | 425 | 2.160 |
| H6-A C1 | 1.581 | 579 | 2.160 |
| H6-B B1 | 966 | 1.194 | 2.160 |
| H6-B C1 | 860 | 1.300 | 2.160 |
| WP14 b1-ref | 1.629 | 99 | 1.728 |
| WP14 c1-h6ref | 1.534 | 194 | 1.728 |

**−154 nhận = +154 từ chối, khớp tuyệt đối trên cả ba panel.** Và
`lifecycle["passengerAlighted"]` bằng đúng số khách được nhận ở **cả hai** arm —
mọi khách được nhận đều thực sự xuống xe.

> **C1 không phục vụ tệ hơn B1. C1 chuyển 154 lần âm thầm làm trễ hẹn của B1
> thành 154 lần từ chối thẳng. Lời hứa nào C1 đưa ra, C1 giữ.**

Bổ trợ bằng bảng tiêu thụ ngân sách: 95% khách của C1 dùng **0 ms** ngân sách
(p95 = 0), trong khi **B1 có p95 = 185.579 ms ≈ 3,1 phút**. B1 thường xuyên đẩy
khách trễ khoảng ba phút để nhét thêm người. Khách bị C1 từ chối chính là những
khách mà muốn phục vụ thì bắt buộc phải làm ai đó trễ quá 30 giây.

---

## B2. Thành phần ngoại sinh **bất biến theo policy** — bằng chứng nội tại rằng phép tách đúng

Đây là kiểm chứng mạnh nhất của thước đo, và hiện chưa có trong báo cáo.

| arm | quy trách (ms) | **ngoại sinh (ms)** | quy trách / cảm nhận |
|---|---:|---:|---:|
| `b1-ref` | 59.250.164 | 6.780.697 | 89,78% |
| `c1-nobudget` | 7.496.399 | 7.226.692 | 50,94% |
| `c1-budget120` | 2.554.106 | 7.105.341 | 26,45% |
| `c1-budget60` | 716.125 | 6.930.015 | 9,37% |
| `c1-h6ref` | 83.373 | 7.020.625 | 1,17% |

Qua mười phương án, thành phần **quy trách** biến động **711 lần**
(59.250.164 → 83.373), trong khi thành phần **ngoại sinh** chỉ dao động
**6,6%** (6.780.697 → 7.226.692).

Một đại lượng ngoại sinh *phải* cư xử đúng như vậy: nó không phụ thuộc policy.
Đây là bằng chứng nội tại rằng phép tách hoạt động — mạnh hơn bảng đối xứng
51,03%/48,96% đang dùng, vì nó là bất biến qua **can thiệp**, không chỉ là đối
xứng của nhiễu.

**Câu tiêu đề rút ra:**

> Dưới một nhà vận hành không bị ràng buộc, **89,78%** những gì khách cảm nhận là
> "lời hứa bị phá" là do chính nhà vận hành gây ra, không phải do hoàn cảnh.
> Tầng cam kết kéo con số đó xuống **1,17%**.

Không bài nào trong văn liệu tính được con số này: Fielbaum & Alonso-Mora chỉ có
hai mốc (`Δ = thực tế − hứa lần đầu`, Mục 3), Schulz & Pfeiffer chỉ có `Delay`
so với lời hứa đầu (Bảng 2), Molenbruch không có động lực học.

---

## B3. Cam kết là ràng buộc **hẹp nhưng đòn bẩy cao** — chặn trên 0,93%

Tổng hợp mã loại bỏ ứng viên trên **20 cell H6 Panel A**:

| Mã | b1 | **c1** | tỉ trọng trong c1 |
|---|---:|---:|---:|
| `PICKUP_WINDOW` | 94.021 | 79.413 | **78,61%** |
| `MAX_RIDE_TIME` | 25.300 | 20.663 | 20,46% |
| `CAPACITY` | 239 | 0 | 0% |
| `COMMITMENT_BUDGET_EXCEEDED` | 0 | 780 | 0,77% |
| `COMMITMENT_PHASE_LOCK` | 0 | 160 | 0,16% |
| **tổng** | **119.560** | **101.016** | |

```
c1:  vật lý   100.076  (99,07%)
     cam kết      940  ( 0,93%)      tỉ lệ 106,5 : 1
```

Phép kế toán khớp tuyệt đối trên cả hai arm: `physicallyOrSchedulePrunedCount`
bằng đúng tổng các mã vật lý (119.560 và 100.076).

**Đọc ra hai điều:**

1. **Chặn trên.** 940 ứng viên là toàn bộ dư địa của mọi cơ chế can thiệp vào
   tầng cam kết. Không cơ chế nào chỉ nới cam kết có thể chạm quá 0,93% không
   gian bị loại.
2. **Đòn bẩy.** 940 lần loại bỏ làm mất 154 khách — **khoảng 6 ứng viên bị loại
   cho mỗi khách bị mất**. Cam kết không phải bức tường rộng; nó là cái chốt nhỏ
   ở đúng chỗ hiểm.

Điểm 2 giải thích một nghịch lý trong dữ liệu: ngân sách gần như **không bao giờ
được tiêu** (p95 = 0 ở mọi arm C1) nhưng vẫn tốn 95–154 khách. Vì ràng buộc
**loại ứng viên** chứ không **phạt** chúng, những phương án tiêu ngân sách bị gạt
trước khi được chọn — nên thống kê tiêu thụ trên phương án đã chọn luôn gần 0.
Cái giá nằm hoàn toàn trong phần phản thực và **không để lại dấu vết trong số
liệu hiện thực**.

---

## B4. Tìm kiếm cạn kiệt — xác minh trên **40/40** lần chạy

Trên toàn bộ 40 bundle (20 cell × 2 arm) của H6 Panel A:

```
candidateCapApplied                 : 0 frame
workBudgetExhausted                 : 0 frame
omittedFeasibleCandidateCountByCap  : 0
omittedUnexpandedCandidatePathCount : 0
omissionCountWasSaturated           : 0 frame

consumedGenerationWorkUnits (tổng)  : 15.955 (b1) / 12.055 (c1)
```

Trần 100 ứng viên/xe chưa từng chạm; ngân sách công việc chưa từng cạn; không
một ứng viên khả thi nào bị bỏ vì trần.

> **Cái giá đo được phản ánh ràng buộc, không phải chất lượng cài đặt.**

Trước đây tuyên bố này chỉ dựa vào số tổng. Giờ nó được xác minh trên từng lần chạy.

---

## B5. Quyết định của nhà vận hành là quá trình gây hại **một chiều**

Trên 160 bundle và **421.752 lần sửa lời hứa** (`wp14r-012-v6-promise-direction`):

| | sớm hơn | muộn hơn | bằng |
|---|---:|---:|---:|
| Có quy trách — giờ trả | **0** | 604 | 0 |
| Có quy trách — giờ đón | **0** | 79 | 0 |
| Chỉ ngoại sinh — giờ trả | 214.924 | 206.224 | — |
| Chỉ ngoại sinh — giờ đón | 102.949 | 107.307 | — |

**Không một lần nào trong 421.752 lần** quyết định của hệ thống làm ETA khách cũ
tốt lên. Đây không phải hiện tượng thống kê mà là **hệ quả cấu trúc**: bộ sinh
chỉ **chèn** khách mới vào tuyến sẵn có, không xoá cũng không xáo lại thứ tự;
chèn thêm một điểm dừng chỉ có thể đẩy khách cũ muộn hơn hoặc giữ nguyên.

Hệ quả: **quyền lợi cam kết của khách là tài nguyên chỉ bị bào mòn, không bao
giờ được nạp lại.** Mọi bảo đảm trong văn liệu đều có tính chất này, vì cùng lý
do — tất cả đều dựa trên chèn/chèn lại.

*(Ghi chú kỹ thuật: `PromiseDeltaCalculator` dùng `AbsoluteDifference`, nên một
cải thiện nếu xảy ra sẽ bị tính là gánh nặng. Bảng trên cho thấy tình huống đó
không xảy ra lần nào, nên lựa chọn cài đặt này không ảnh hưởng kết quả.)*

---

## Ghi chú về đối chiếu văn liệu

Nếu viết phần định vị, ba mốc cần trích chính xác:

- **Fielbaum & Alonso-Mora (2020)**, *Transportation Research Part C* 121:102831.
  Đo `Δ = thực tế − hứa lần đầu` (hai mốc, Mục 3). Bảng 5: base 34,5% từ chối →
  "fully controlled" 45,6%; nhưng detour trung bình tăng 0,65 → 0,94 phút — họ
  bịt lời hứa giờ đón và tổn hại chảy sang thời gian ngồi xe.
- **Schulz & Pfeiffer (2026)**, *OR Spectrum* 48:541–586. Tham số `l` = độ trượt
  tối đa của giờ đến sau khi nhận, có báo trước. Finding 5: `l` nhỏ → từ chối
  nhiều; `l` lớn → kém hấp dẫn; khuyến nghị 10–15 phút.
- **Molenbruch, Braekers & Caris (2015)**, *CEJOR*. 78 kịch bản mức dịch vụ,
  **tĩnh**, và **không có từ chối trong mô hình** (họ bỏ ràng buộc đội xe) — chi
  phí của họ là quãng đường, không phải khách bị mất.
