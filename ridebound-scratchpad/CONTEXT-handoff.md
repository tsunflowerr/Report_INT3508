# RideBound — bàn giao context (2026-09-08)

Dán file này vào session mới để hỏi về hướng đi, trùng lặp văn liệu, phương án.

---

## 1. Hệ thống

Điều phối xe đi chung với "lời hứa có chứng nhận, ràng buộc được". Khoá luận tốt
nghiệp. Lõi .NET (`src/RideBound.*`) + adapter Python cắm FleetPy 1.0.2.

| | |
|---|---|
| Repo | `E:\Code\RideBound` (nhánh `main`) |
| Dữ liệu | `E:\RideBoundData\` |
| Python | `E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe` |
| FleetPy | `E:\RideBoundData\wp7\FleetPy-1.0.2` |
| Runner H6 ghim | `E:\RideBoundData\wp9\runner\h6-confirmatory-v1` |
| Test | 437 Python · 908 .NET (solution là `RideBound.slnx`) |

**Policy đã benchmark:** `rolling-cost` (B1) · `ridebound-hard-vector` (C1 = B1 +
tầng lọc cam kết) · `commit-soft-hard-hybrid` (C2). Hai config H6 khác **đúng một
khoá `policyId`** — ablation có kiểm soát.

**Phép tách ba mốc** (`src/RideBound.Application/Promises/PromiseDeltaCalculator.cs`):

```
previous  = lời hứa lần trước
exogenous = lời hứa đó nếu KHÔNG quyết định lại
            (chiếu lại tuyến cũ + phân công cũ, từ vị trí xe THẬT, tại thời điểm hiện tại)
proposed  = lời hứa mới

decisionDelta = |proposed − exogenous|    ← quy trách nhà vận hành
visibleDelta  = |proposed − previous|     ← khách nhìn thấy
```

`budgetBasis ∈ {DecisionInduced, CustomerVisible}` chọn cái nào bị tính phí
(`CommitmentDecisionValidator.cs:393`, `CommitmentLedger.cs:285`).

## 2. Ràng buộc cấu trúc (đã xác minh trong code)

Áp cho **mọi** policy kể cả B1:

| Bất biến | Vị trí |
|---|---|
| `Reject()` chỉ từ `Pending` → không loại được khách đã nhận | `RideRequest.cs:236` |
| `PhysicalViolationCodes.Reassignment` → không đổi được xe | `PhysicalPlanValidator.cs:682` |
| `ValidateAcceptedPreservation` (vô điều kiện) | `PhysicalPlanValidator.cs:178` |
| Bộ sinh chỉ xét khách `Pending` | `InsertionCandidateGenerator.cs:54` |

⟹ B1 chỉ được **xếp lại thứ tự dừng trong xe đã gán**. Quyết định **chỉ gây hại**,
không bao giờ cải thiện khách cũ — **0 cải thiện / 421.752 lần sửa**.

Travel time **tĩnh** (`travelSnapshotVersion = 1` trên cả 50 bundle) ⟹ "ngoại
sinh" là **trôi do hiện thực hoá**, không phải tắc đường.

ILP là set-packing chuẩn (`OrToolsCandidateSelectionSolver.cs:349-365`): đúng một
option mỗi xe, mỗi request ≤ 1 lần — **giống hệt ILP của Alonso-Mora 2017**.

## 3. Kết quả

**H6** (20 cell, 2.160 khách/panel): B1 1.735 / C1 1.581 → **−154 khách
(−7,13 đpt)**, giảm gánh nặng 99,83%. Tiền đăng ký −1,00 đpt → **cổng phục vụ
FAIL**. Tái lập 18/18 chỉ số.

**WP14** (16 cell, 1.728 khách/arm):

| arm | phục vụ | experienced | attributed | exogenous | att/exp |
|---|---:|---:|---:|---:|---:|
| b1-ref | 1629 | 65.992.813 | 59.250.164 | 6.780.697 | **89,78%** |
| c1-nobudget | 1584 | 14.716.623 | 7.496.399 | 7.226.692 | 50,94% |
| c1-budget120 | 1563 | 9.656.231 | 2.554.106 | 7.105.341 | 26,45% |
| c1-budget60 | 1540 | 7.644.412 | 716.125 | 6.930.015 | 9,37% |
| c1-h6ref | 1534 | 7.102.950 | 83.373 | 7.020.625 | **1,17%** |

Ngoại sinh **bất biến theo policy** (dao động 6,6%) trong khi quy trách biến động
**711 lần** → bằng chứng nội tại phép tách đúng.

**Prunes, 20 cell, c1:** vật lý 100.076 (99,07%) vs cam kết 940 (0,93%) = 106,5:1.
`PICKUP_WINDOW` một mình 78,61%. Nhưng 940 lần loại làm mất 154 khách →
**~6 ứng viên / 1 khách**: ràng buộc **hẹp, đòn bẩy cao**.

**Tìm kiếm cạn kiệt:** 40/40 lần chạy, cap và work budget chưa từng chạm.

## 4. KẾT QUẢ MỚI 2026-09-08 — hiệu chuẩn baseline ngoài

Chạy FleetPy gốc trên **cùng** mạng (96 node/9.120 cung), **cùng** 108 khách/cell,
**cùng** 8 xe × 4 chỗ ghim đúng vị trí xuất phát, chờ ≤ 600 s, vòng ≤ 1,5× trực
tiếp (`op_max_detour_time_factor: 50`). 20 cell, 2.160 khách.

| | phục vụ | tỉ lệ | so B1 |
|---|---:|---:|---:|
| FleetPy **`AlonsoMora`** (đổi xe tự do) | **1.750** | 81,0185% | **+15** (+0,69 đpt) |
| **RideBound B1** | **1.735** | 80,3241% | — |
| FleetPy `InsertionHeuristic` | 1.724 | 79,8148% | −11 |
| RideBound C1 | 1.581 | 73,1944% | −154 |

**B1 nằm giữa hai fleet control gốc.** Phản biện "baseline bù nhìn" chết.

```
giá của khoá danh tính xe :  ≤ 0,69 đpt
giá của tầng cam kết ETA  :    7,13 đpt     ← đắt gấp ~10 lần
```

⟹ Mở khoá đổi xe có trần ~15 khách, **không đáng làm**. Và −154 **thực sự** là
giá của lời hứa về thời gian.

## 5. KẾT QUẢ MỚI 2026-09-08 — so sánh *dạng* bảo đảm

Arm `budgetBasis: customerVisible` (đã cài sẵn, chưa từng chạy), mọi thứ khác
giữ nguyên, β = 30 s:

- **16/20 cell: trùng khít** arm `decisionInduced`, chênh **0** từng cell
- **4/20 cell: KHÔNG CÓ NGHIỆM** — `C1 rejected every generated candidate for this vehicle`

**Phát biểu cấu trúc:**

```
Phương án KHÔNG LÀM GÌ  ⟹  proposed = exogenous

  cơ sở hành vi    : charged = |proposed − exogenous| = 0        → luôn hợp lệ
  cơ sở khách-thấy : charged = |exogenous − previous| = trôi     → có thể vi phạm
```

> **Bảo đảm theo hành vi luôn thoả mãn được. Bảo đảm theo kết quả có thể bất khả
> thi — và thứ phá vỡ nó là sự bất động của chính nhà vận hành.**

Là **vách đá, không phải dốc**: dưới ngưỡng thì hai dạng cho kết quả y hệt; vượt
ngưỡng thì một dạng vẫn chạy, dạng kia không có nghiệm.

Điều này **giải thích cơ chế** cho Finding 5 của Schulz & Pfeiffer (`l` nhỏ → từ
chối nhiều; `l` lớn → kém hấp dẫn): thế lưỡng nan của họ là hệ quả của *dạng*
bảo đảm, không phải quy luật tự nhiên.

### Quét β trên 4 cell vô nghiệm (2026-09-09)

| cell | B1 | Δ@30s | V@60s | V@120s | V@300s | V@600s |
|---|---:|---:|---:|---:|---:|---:|
| 16-r2 | 91 | 76 | 76 | 80 | 81 | 81 |
| 16-r4 | 83 | 77 | 77 | **vô nghiệm** | 78 | 79 |
| 17-r1 | 80 | 74 | 73 | 74 | 76 | 78 |
| 17-r3 | 66 | 60 | 59 | **64** | **62** | 63 |
| **tổng** | **320** | **287** | **285** | — | **297** | **301** |

**Tỉ giá:** nội suy 60 s (285) ↔ 300 s (297) cho hoà vốn ở **≈ 100 s** ⟹ cơ sở
kết quả cần **~3–4× ngân sách** để phục vụ ngang cơ sở hành vi. Ở 600 s (20×,
tức cho phép xê dịch 10 phút) V mới đạt 301, vẫn kém B1 (320) 19 khách.

⚠ **Thiên lệch:** bốn cell này được *chọn* vì V thất bại ở 30 s — tức bốn cell
khó nhất cho V. Đang chạy đủ 20 cell ở β = 120 s để lấy tỉ giá không thiên lệch.

### Hai chỗ KHÔNG ĐƠN ĐIỆU của cơ sở kết quả

- **Khả thi:** `16-r4` khả thi ở 60 s → **vô nghiệm ở 120 s** → khả thi lại ở 300 s.
  Nới ngân sách lại gây mất nghiệm.
- **Phục vụ:** `17-r3` được 64 ở 120 s → **62 ở 300 s**. Nới ngân sách lại phục vụ ít đi.

Nguyên nhân: **phụ thuộc đường đi** — ngân sách rộng cho phép chọn tham lam sớm,
dẫn tới trạng thái sau tệ hơn.

Đối chiếu, cơ sở **hành vi** trên WP14 thì **đơn điệu tăng**:
`β=30s → 1534 · 60s → 1540 · 120s → 1563 · không ngân sách → 1584`.

⟹ **Ba phát biểu cấu trúc**, cùng bắt nguồn từ một điểm: dưới cơ sở hành vi
phương án không-làm-gì luôn hợp lệ (charged = 0), nên tập khả thi có điểm neo và
chỉ nở ra khi β tăng; dưới cơ sở kết quả không có điểm neo đó.

### Arm V ở β = 120 s trên ĐỦ 20 cell (kết quả mạnh nhất)

| | ngân sách | cell **có nghiệm** | phục vụ (16 cell chung) |
|---|---:|---:|---:|
| **Δ — cơ sở hành vi** | **30 s** | **20/20** | 1.246 |
| V — cơ sở kết quả | 120 s | **16/20** | 1.266 |

**Tập cell vô nghiệm ĐỔI CHỖ chứ không giảm:**

```
β =  30 s  →  {16-r2, 16-r4, 17-r1, 17-r3}     4/20
β = 120 s  →  {14-r4, 15-r2, 16-r4, 17-r4}     4/20
                       chỉ 16-r4 trùng
```

Gấp **bốn lần** ngân sách **không làm giảm** tỉ lệ vô nghiệm — vẫn 20%, chỉ chuyển
sang instance khác. Ba cell chạy tốt ở 30 s trở nên vô nghiệm ở 120 s. Đây là bằng
chứng trực tiếp của **phụ thuộc đường đi**.

Đổi chác thật: ở 4× ngân sách, trên instance còn chạy được, cơ sở kết quả phục vụ
hơn **1,6%** — đổi lấy lời hứa **yếu đi 4 lần** và **20% instance không có phương
án nào**. Không phải đánh đổi; là hỏng.

### BA PHÁT BIỂU — trạng thái cuối

| # | Phát biểu | Bằng chứng |
|---|---|---|
| ① | Hành vi **luôn có nghiệm**; kết quả **có thể vô nghiệm** | định nghĩa + 20/20 vs 16/20 |
| ② | Tăng ngân sách **không sửa được** vô nghiệm — nó **đổi chỗ** | 4/20 ở cả 30 s và 120 s, 1 cell trùng |
| ③ | Hành vi ở 1× ngân sách **trội** kết quả ở 2× | 287 vs 285 (4 cell khó) |

② là phát biểu mạnh nhất và bất ngờ nhất. Dự đoán ban đầu (tăng β sẽ dần chữa
được vô nghiệm) **sai**.

## 6. Văn liệu — ai sở hữu gì

| Bài | Sở hữu | Thiếu |
|---|---|---|
| **Fielbaum & Alonso-Mora 2020**, TR-C 121:102831 | `Δ = thực tế − hứa lần đầu` (**hai mốc**); cấm tái gán → từ chối tăng (Bảng 5: 34,5%→45,6%); detour xấu đi 0,65→0,94 phút | mốc phản thực; giờ cao điểm (né bằng cách chỉ chạy 13–15h); đo danh tính xe |
| **Schulz & Pfeiffer 2026**, OR Spectrum 48:541 | `l` = trượt tối đa giờ đến sau khi nhận, báo trước; quét `l` 0–30 phút; Finding 5 | phân rã quy trách; khoá xe |
| **Sharif Azadeh et al. 2022**, TR-B 161:128 | **menu** {taxi/shared}×{ΔT,2ΔT,3ΔT} + giá; assortment optimization | bảo đảm chống sửa về sau |
| **Molenbruch et al. 2015**, CEJOR | 78 kịch bản mức dịch vụ | **tĩnh**; **không có từ chối trong mô hình** |
| **Alonso-Mora 2017** PNAS, pt (9) | Δ biên gây cho khách cũ, **chi phí mềm một quyết định** | tích luỹ trọn đời; ràng buộc cứng; mốc phản thực |
| Köhler, Ehmke & Campbell 2020, Omega | độ chặt cửa sổ theo trạng thái tuyến | |
| Haferkamp 2024, EJTL | menu nhiều lựa chọn giờ đón | |
| Vallée 2019 / Luo & Schonfeld 2011 | repair, chèn lại giữa các xe | |

## 7. Tám ứng viên ĐÃ BỊ LOẠI (đừng đề xuất lại)

1. **Repair bảo toàn cam kết** — thí nghiệm riêng: 98,63% vùng lân cận bất khả
   thi vật lý, **0 khách thu hồi**; 2 lỗi (`RBWP7_LOCKED_LEG_MISMATCH` 18/20 cell,
   vỡ ngân sách tầng 1/20). Và đã có Vallée/Schulz.
2. **Menu lời hứa phân tầng** — CD-DARP sở hữu.
3. **Độ chặt riêng theo trạng thái** — Köhler 2020 sở hữu.
4. **Công bố ETA có đệm** — sụp vào `l` của Schulz; ngân sách đặt trên *độ lệch*
   nên đệm mức không nới gì.
5. **Định giá slack / nhìn trước** — Schulz "potential", Haferkamp, Ulmer.
6. **Quét tham số mức dịch vụ toàn cục** — Molenbruch + Schulz.
7. **Tỉ lệ vòng so chuyến trực tiếp** — phổ biến.
8. **Sổ cái có dấu (ghi có từ quyết định)** — chết bằng dữ liệu: 0 cải thiện /
   421.752 lần, bất khả về cấu trúc.

**Và mới hôm nay: mở khoá đổi xe** — trần 15 khách, không đáng.

## 8. Ngách còn sống

> Tích luỹ trọn đời của thiệt hại biên, đo so với **mốc phản thực chiếu lại tại
> thời điểm hiện tại**, coi như **quyền lợi có trần** của từng khách, và **công bố**
> như một lời hứa.

Tiền lệ liên ngành: **SLA đa thuê bao** dùng đúng cấu trúc baseline phản thực
(US 9311376 — baseline "nếu được cấp tài nguyên riêng"). Xe đi chung **chính là**
đa thuê bao của một chiếc xe. Trong giao thông: chưa ai.

Cộng với phát biểu ở §5, câu chuyện hoàn chỉnh gồm hai nửa, **cả hai đều chưa ai có**.

## 9. Câu hỏi mở

- Phát biểu "bất động phá vỡ bảo đảm theo kết quả" đã có ai nêu chưa, ngành nào?
- SLA neo-baseline đám mây có ai hình thức hoá thành ràng buộc tối ưu chưa?
- Quy mô 8 xe / 108 khách — vá thế nào cho thuyết phục?
- Định vị: "price of X" (Bertsimas 2011) hay "service guarantee design"?

## 10. Việc đang chạy / còn lại

| Việc | Trạng thái |
|---|---|
| Quét β cho arm V (4 cell × 4 β) | đang chạy |
| Arm V có đường lui (từ chối thay vì sập) để đo *mức* thiệt hại | chưa làm, ~3 ngày |
| Trộn `bo-sung-bao-cao.md` vào báo cáo | chờ người dùng duyệt |
| Quy mô lớn hơn (nhiều xe / nhiều khách) | chưa làm |

## 11. Ghi chú vận hành

- **Không ghi gì vào repo** trong mọi thí nghiệm khám phá — config vào scratchpad,
  output vào `E:\RideBoundData\`. Seal WP9/WP14 không trôi.
- **Không chạy song song** thí nghiệm FleetPy với preflight RideBound: preflight
  có cổng tài nguyên chặn ở 20% CPU.
- Đã cài `gurobipy 13.0.3` vào env FleetPy (license hạn chế đủ cho AlonsoMora ở
  quy mô này). **437/437 test Python vẫn xanh.** Bản lui:
  `scratchpad/env/pip-freeze-before.txt`.
- Console cp1252 → luôn đặt `PYTHONIOENCODING=utf-8`.
- Heredoc làm hỏng `\n` → dùng công cụ Write cho script.
