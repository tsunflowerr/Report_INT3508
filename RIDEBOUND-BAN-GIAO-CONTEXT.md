# RideBound — Bàn giao toàn bộ ngữ cảnh nghiên cứu

**Cập nhật:** 2026-09-16
**Mục đích:** nạp toàn bộ ngữ cảnh cho một trợ lý lập trình khác (Codex hoặc tương đương)
để tiếp tục công việc mà không cần đọc lại lịch sử hội thoại.
**Người dùng:** Trần Quang Thành — 23020155 — K68I-IT2, UET/VNU. Khóa luận tốt nghiệp.

Đọc hết mục 0 → 3 trước khi làm bất cứ việc gì. Mục 12 là các bẫy đã vấp; đọc trước khi
chạy thực nghiệm sẽ tiết kiệm nhiều giờ.

---

## 0. Ba câu tóm tắt

1. **RideBound** là một hệ điều phối xe đi chung (ride-pooling) có thêm một cơ chế mới:
   *lời hứa có biên được chứng nhận* — mỗi lần hệ thống công bố lại giờ đón/giờ trả cho
   khách, độ dời được ghi vào một sổ cái riêng của từng khách, cộng dồn và chỉ tăng, đối
   chiếu với một trần β; phương án nào làm vượt trần thì **bị xóa khỏi tập lựa chọn ngay
   tại thời điểm ra quyết định**.
2. Điểm mới cốt lõi so với văn liệu là **phân rã theo nguyên nhân**: tách phần dịch chuyển
   do nhà điều hành tự gây ra khỏi phần do giao thông gây ra, và chỉ tính vào sổ cái phần
   thứ nhất. Từ đó sinh ra **hai cơ sở tính sổ cái** và **ba định lý** về chúng.
3. Hiện trạng: lý thuyết đã chứng minh và xác nhận thực nghiệm; **558 lần chạy mô phỏng,
   33,62 GB** bằng chứng niêm phong; báo cáo LaTeX **66 trang** đã viết xong. Tám hướng
   cải tiến đã thử và **tất cả đều bị dữ liệu bác bỏ** — mỗi hướng vì một lý do khác nhau,
   và các lý do ấy tự chúng là kết quả.

---

## 1. Bài toán và động cơ

### 1.1 Hiện tượng

Mọi hệ ride-pooling theo yêu cầu (Uber Pool, Grab cùng chuyến, …) đều báo cho khách một
giờ đón và giờ trả dự kiến, rồi **tiếp tục tối ưu lại kế hoạch mỗi khi có khách mới**. Hệ
quả là giờ đã báo bị dời đi nhiều lần trong cùng một chuyến.

Mọi thước đo chuẩn của ngành — tỉ lệ phục vụ, thời gian chờ, độ vòng đường — **không ghi
nhận điều này**. Một khách được báo đúng một lần và một khách bị đổi giờ mười hai lần là
giống hệt nhau trong mọi hàm mục tiêu hiện hành, miễn cả hai vẫn nằm trong cửa sổ hợp lệ.

Đo được trên hệ thống này: **89,06%** lượng dịch chuyển giờ hẹn mà khách nhìn thấy trong
chế độ không cam kết là **do chính bộ điều phối gây ra**, không phải do giao thông. Khách
chịu thiệt nặng nhất bị dời tổng cộng **840,9 giây** (gần 14 phút) mà hệ thống vẫn tính là
phục vụ thành công.

### 1.2 Câu hỏi nghiên cứu

> Một hãng gọi xe chung có thể đưa ra lời hứa về giờ giấc mà hãng **thực sự giữ được** hay
> không, và cái đó **đắt bao nhiêu**?

### 1.3 Tiêu chí chấm khóa luận mà người dùng đang nhắm

- Bài toán có thật, quan trọng, đáng làm không?
- Giải pháp hợp lý không? Mới hơn đối thủ, hoặc giới hạn tốt hơn (rẻ hơn / nhanh hơn)?
- Minh chứng: định lượng (nghiên cứu) hay định tính (demo)?

---

## 2. Cơ chế RideBound

### 2.1 Phân rã ba mốc — trái tim của toàn bộ công trình

Mỗi lần hệ thống định công bố lại lời hứa cho một khách, có **ba** mốc thời gian, không
phải hai:

| Ký hiệu | Tên | Định nghĩa |
|---|---|---|
| `v` | previous | lời hứa đã công bố lần trước (khách đang nhớ con số này) |
| `e` | **exogenous** | chính lời hứa cũ ấy, **chiếu lại từ vị trí THẬT hiện tại của xe**, giữ nguyên lộ trình và phân công |
| `p` | proposed | lời hứa mới mà phương án đang xét sẽ tạo ra |

Ba đại lượng dẫn xuất:

```
A = |p − e|   "conduct"  — do quyết định của nhà điều hành gây ra
d = |e − v|   "drift"    — do thế giới vật lý gây ra (tắc đường, trễ thực thi)
B = |p − v|   "visible"  — cái khách thực sự nhìn thấy
```

**Đẳng thức trung tâm: `B = A + d`.** Vì cả ba là tổng trị tuyệt đối nên bất đẳng thức tam
giác chỉ cho `B ≤ A + d`; đo thực tế cho độ hụt tối đa **0,07%** và **đúng 0,00% ở cấu hình
C1** (bảng đầy đủ ở mục 7.3).

Ý tưởng của mốc `e`: nó là một **mốc phản thực** (counterfactual). Nó trả lời "nếu nhà điều
hành không làm gì cả thì khách vẫn bị trễ bao nhiêu?" — và đó chính là ranh giới "ngoài tầm
kiểm soát" mà luật hợp đồng xử lý bằng văn xuôi, nay **tính được bằng số**.

Trong mã: `src/RideBound.Domain/Commitments/RiderPromise.cs`
```csharp
public sealed record ThreeWayPromiseDelta(
    CommitmentVector Exogenous,
    CommitmentVector DecisionInduced,
    CommitmentVector Visible);
```

### 2.2 Sổ cái cam kết

Mỗi cặp (khách, chiều) có một sổ cái **cộng dồn, đơn điệu không giảm**, so với trần cứng
`hardLimit`. Vector cam kết có **10 chiều** (`CommitmentDimensionVocabulary.Ordered`,
`src/RideBound.Domain/Commitments/CommitmentDimension.cs`):

```
pickup_eta_total_ms          drop_eta_total_ms
material_eta_revision_count  vehicle_switch_count
pickup_stop_relocation_mm    pickup_stop_switch_count
drop_stop_relocation_mm      drop_stop_switch_count
incumbent_order_inversion_count   pre_pickup_inserted_stop_count
```

Kiểm tra xảy ra **trước khi chọn**, trong `HardVectorCandidateAssessor.AssessAndFilter`:
phương án vượt trần bị **loại khỏi tập**, không phải bị phạt điểm. Đây là điểm phân biệt
then chốt với mọi cách tiếp cận "thêm số hạng vào hàm mục tiêu".

### 2.3 Hai cơ sở tính sổ cái — đóng góp lý thuyết trung tâm

`src/RideBound.Domain/Commitments/CommitmentPolicy.cs`
```csharp
public enum CommitmentBudgetBasis { DecisionInduced, CustomerVisible }
```
JSON: `"budgetBasis": "decisionInduced" | "customerVisible"`.

| Cơ sở | Tính đại lượng | Nghĩa | Analogue pháp lý |
|---|---|---|---|
| **Hành vi** (conduct) | `A = \|p−e\|` | "tôi làm bạn trễ thêm bao nhiêu so với lẽ ra" | **obligation de moyens** (nghĩa vụ phương tiện) |
| **Kết quả** (outcome) | `B = \|p−v\|` | "bạn trễ bao nhiêu so với điều tôi đã nói" | **obligation de résultat** (nghĩa vụ kết quả) |

Điểm mới nằm ở chỗ **mốc ngoại sinh `e` tính được ranh giới "ngoài tầm kiểm soát"** mà luật
chỉ mô tả bằng lời.

---

## 3. Lý thuyết — ba định lý và một hệ quả

Bất biến nền (đã xác minh trong mã): **phương án "không làm gì" luôn tồn tại** — giữ nguyên
phân công và lộ trình, chỉ chiếu lại theo vị trí xe hiện tại; khi đó `p = e`.

**Định lý 3.1 (cơ sở hành vi luôn thỏa được).**
Dưới cơ sở hành vi, tập phương án của một xe không bao giờ bị làm rỗng bởi ràng buộc cam kết.
*Chứng minh:* với phương án không làm gì, `A = |e − e| = 0`, sổ cái không đổi, mà sổ cái
trước đã ≤ β. ∎

**Định lý 3.2 (cơ sở kết quả có thể vô nghiệm).**
Dưới cơ sở kết quả, tồn tại trạng thái mà tập phương án bị làm rỗng.
*Chứng minh:* với phương án không làm gì, `B = |e − v| = d > 0`. Nếu sổ cái + `d` > β thì
ngay cả việc không làm gì cũng bị loại. ∎

**Định lý 3.3 (cơ sở kết quả không bao giờ phục vụ nhiều hơn).**
Với **mọi** trần β, số khách phục vụ dưới cơ sở kết quả ≤ số khách dưới cơ sở hành vi.
*Chứng minh:* từ `B = A + d` và `d ≥ 0` ⟹ `B ≥ A` tại mọi lần công bố ⟹ tập khả thi của
cơ sở kết quả là **tập con** của tập khả thi cơ sở hành vi. ∎

**Hệ quả 3.4 (dải khác biệt rộng đúng `d`).**
Một phương án bị cơ sở kết quả loại mà cơ sở hành vi không loại ⟺ sổ cái rơi vào dải
`β − d ≤ A < β`. **Bề rộng dải đúng bằng `d`, độc lập với β.** Tức là **nới trần không
làm hai cơ sở gần nhau hơn** — điều này đã được kiểm chứng thực nghiệm (mục 7.4).

---

## 4. Bản đồ mã nguồn

Kho: `E:\Code\RideBound` (git, nhánh `main`, .NET + C#).

### 4.1 Cấu trúc

```
src/
  RideBound.Domain/            <- thuần túy, không phụ thuộc hạ tầng
    Commitments/               CommitmentLedger, CommitmentPolicy, CommitmentVector,
                               CommitmentDimension, RiderPromise, CommitmentBudgetEvaluator,
                               CommitmentLockEvaluator
    Routes/RoutePlan.cs        FrozenPrefix / MutableSuffix / ExecutedStopCount
    Requests/RideRequest.cs    bất biến cửa sổ đón (xem 4.3)
    Vehicles/, Runs/, Incidents/, Common/, Validation/
  RideBound.Algorithms/
    Candidates/                8 file, 3.075 dòng
      InsertionCandidateGenerator.cs      (1.061 dòng) — bộ sinh chèn thuần
      CandidatePortfolioRetainer.cs       có maximumCandidates + Rank (đo được: KHÔNG BAO GIỜ chạm)
      WaitingIncumbentRepairSeedBuilder.cs (149 dòng) — bộ sinh SẮP XẾP LẠI (xem 8.7)
      ForwardSlackProfile.cs              (567 dòng)
      CandidateIdentity.cs, CandidateModels.cs, CandidateScheduleEvaluator.cs,
      OriginHoldCandidateTransformer.cs
    Commitments/               CommitmentCandidateAssessor, CommitmentCandidateFilter,
                               HardVectorCandidateAssessor, CommitmentWarningProfile
    Policies/                  SolverBackedRidePoolingPolicy (bộ định tuyến chính sách),
                               SolverBackedFleetSelection (hàm mục tiêu từ điển),
                               CommitmentMechanismPolicies, HardVectorPolicy,
                               SoftHardHybridPolicy, RollingCostPolicy, …
  RideBound.Solvers.OrTools/   ILP đóng gói tập hợp (set packing), OR-Tools 9.15.6755
  RideBound.Runner/            Configuration/Wp4RunnerConfiguration.cs — bộ đọc cấu hình
  RideBound.Application/, RideBound.Infrastructure/, RideBound.Contracts/,
  RideBound.Benchmarking/, RideBound.Benchmarking.Contracts/

simulators/fleetpy-ridebound/
  actual_fleetpy_medium_preflight.py   <- ĐIỂM VÀO của mọi thực nghiệm
  ridebound_fleetpy/
    fleet_control.py     cầu nối FleetPy ↔ RideBound; bất biến chặng đang chạy (4.4)
    protocol.py, runner_client.py, session.py, transcript.py, mapping.py, errors.py
  wp9_*.py, wp13_*.py, wp14_*.py       các script phân tích đã có sẵn trong kho

benchmarks/
  configurations/      27 file JSON cấu hình chính sách & cam kết
  fixtures/wp6/public/fleetpy-manhattan-v1/wp9-confirmatory-fixed-panel-v2/   panel 20 ô
  scenarios/wp9-confirmatory/          55 file driver

docs/       00-index.md … 22-glossary.md + benchmarking/ handoffs/ research/ reviews/ tasks/
AGENTS.md   hướng dẫn cho agent — ĐỌC TRƯỚC KHI SỬA GÌ
```

### 4.2 Bộ định tuyến chính sách — chỗ dễ hiểu sai nhất

`src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs`, quanh dòng 255:

```csharp
var profile = SolverBackedObjectiveProfile.RollingCost;   // mặc định
switch (policyOptions.PolicyKind)
{
    case RollingPenalty:            ... profile = RevisionPenalty; break;
    case FixedFreezeHorizon:        ... CommitmentCandidateFilter ...  break;
    case RideBoundHardVector:
    case CommitSoftHardHybrid:      ... _hardAssessor.AssessAndFilter ...
                                    profile = HardVector | SoftHardHybrid; break;
    // NoReassignmentRepair KHÔNG có nhánh -> rơi xuống mặc định
}
```

**Hệ quả quan trọng:** `NoReassignmentRepair` (nhánh b4) **không qua bộ lọc cam kết nào**.
Xác nhận ở tầng sâu hơn: `EffectivePolicies()` đưa nó qua
`MechanismCommitmentPolicyProvider.RevisionPenalty`, hàm này **dựng lại mọi chính sách với
`hardLimit: null` trên TẤT CẢ các chiều** và `finalConfirmationLocks: PromiseLock.None`
(`src/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:47` và `:81-100`).
⟹ **b4 so được với B1, KHÔNG so được với C1.**

Hàm mục tiêu từ điển (`SolverBackedFleetSelection.cs:313-324`), hồ sơ `SoftHardHybrid`:
```
accepted-request-count > operational-cost > candidate-id-rank
> worst-hard-utilization-ppm > warning-excess:<10 chiều> > revision:<10 chiều>
```
Hồ sơ `HardVector` giống hệt nhưng **không có** tầng `warning-excess`.

### 4.3 Bất biến miền #1 — cửa sổ đón

`src/RideBound.Domain/Requests/RideRequest.cs:266-273`
```csharp
if (pickupTime.Milliseconds < EarliestPickup.Milliseconds
    || pickupTime.Milliseconds > LatestPickup.Milliseconds)
{
    return DomainResult<RideRequest>.Fail(
        RequestFailureCodes.PickupTimeOutsideWindow,
        "Actual pickup time must remain inside the accepted pickup window.",
        Id.Value, "actualPickupTime");
}
```
Bắn **bất kể** cơ sở tính nào, bất kể nguyên nhân gì. Đây là thứ chặn thí nghiệm tắc đường
không cho ra kết quả về tỉ lệ phục vụ.

### 4.4 Bất biến miền #2 — chặng đang chạy (phát hiện 2026-09-16)

`simulators/fleetpy-ridebound/ridebound_fleetpy/fleet_control.py:360-370`
```python
if veh_obj.assigned_route and veh_obj.assigned_route[0].locked:
    if not new_legs or not self._leg_equivalent(veh_obj.assigned_route[0], new_legs[0]):
        raise _fail("RBWP7_LOCKED_LEG_MISMATCH",
                    f"$.vehicles[{veh_obj.vid}].activeLeg",
                    "replacement is not exact-equivalent")
```
`_leg_signature` = (status, destination_pos, boarding rids, alighting rids, locked, duration,
earliest_start_time, earliest_end_time).

Phía RideBound, `RoutePlan.AdvanceReachedStop` chuyển một điểm dừng từ `MutableSuffix` sang
`FrozenPrefix` **khi xe TỚI NƠI**. Không có chuyển trạng thái cho "xe đã xuất phát hướng
tới". FleetPy khóa chặng **khi xe LĂN BÁNH**.

⟹ Giữa xuất phát và tới nơi, điểm dừng đích nằm ở `MutableSuffix[0]` và mô hình coi là sửa
được. Bộ sinh chèn thuần hiếm khi động vào nên không lộ; bộ sinh sắp xếp lại làm sập 18/20 ô.

**Lưu ý:** `RoutePlan` **đã cho phép** trạng thái `ExecutedStopCount < FrozenPrefix.Count`
(`PendingStops => FrozenPrefix.Skip(ExecutedStopCount).Concat(MutableSuffix)`). Chỉ **thiếu
điểm gọi**. Đo được: **0 lần** đóng băng sớm trên 12.170 lần cập nhật kế hoạch của cả ba nhánh.

### 4.5 Ràng buộc cấu hình chặn tổ hợp "sắp lại + cam kết"

`src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:570-592`
```csharp
if (hasSolver == isB5 || hasFreeze != isB3 || hasRepair != isB4
    || hasMultiple != isB5 || hasWarnings != isC2)
    throw new InvalidDataException("WP4 policy variant fields do not match the selected policyId.");
```
`hasRepair != isB4` ⟹ trường `repair` **chỉ** dùng được với `no-reassignment-repair`.

---

## 5. Hạ tầng thực nghiệm

### 5.1 Các thành phần

| Thành phần | Đường dẫn |
|---|---|
| Python (conda env FleetPy) | `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe` |
| FleetPy 1.0.2 | `E:/RideBoundData/wp7/FleetPy-1.0.2` |
| Bộ chạy niêm phong chính | `E:/RideBoundData/wp9/runner/h6-confirmatory-v1` |
| Bộ chạy cho thí nghiệm ratchet | `E:/RideBoundData/wp14/runner/ratchet-secondary-v1` |
| dotnet | `C:/Program Files/dotnet/dotnet.exe` |
| Fixture panel 20 ô | `benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp9-confirmatory-fixed-panel-v2/<cell>/` |
| Driver | `benchmarks/scenarios/wp9-confirmatory/<cell>.driver.json` |
| Kết quả | `E:/RideBoundData/wp9/*` và `E:/RideBoundData/wp14/*` |

### 5.2 Panel

20 ô: `d201811{14,15,16,17,18}-s10-r{1,2,3,4}` — 5 ngày × 4 lần lặp.
Mỗi ô: **108 yêu cầu, 8 xe**. Tổng **2.160 yêu cầu**.
Dữ liệu: chuyến đi công khai Manhattan (NYC TLC), cửa sổ đón mặc định **600 giây**.
Hạt giống chủ: **7** ở mọi lần chạy.

Mỗi ô có: `scenario-content.json`, `derivative-manifest.json`, `normalization-report.json`,
`selection-frame.json` (+ `ATTRIBUTION.md`, `normalizer-configuration.json`,
`normalization-exclusions.json`).

### 5.3 Lệnh chạy một ô

```bash
E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B \
  simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py \
  --label            "<nhan>" \
  --fleetpy-root     E:/RideBoundData/wp7/FleetPy-1.0.2 \
  --runner-root      E:/RideBoundData/wp9/runner/h6-confirmatory-v1 \
  --dotnet           "C:/Program Files/dotnet/dotnet.exe" \
  --commitment-config benchmarks/configurations/<cam-ket>.json \
  --wp4-config        benchmarks/configurations/<chinh-sach>.json \
  --scenario              <fixture>/scenario-content.json \
  --derivative-manifest   <fixture>/derivative-manifest.json \
  --normalization-report  <fixture>/normalization-report.json \
  --selection-frame       <fixture>/selection-frame.json \
  --driver           benchmarks/scenarios/wp9-confirmatory/<cell>.driver.json \
  --output           E:/RideBoundData/wp14/<dot>/<nhan> \
  --repeats 1 --master-seed 7
```
Chạy từ thư mục gốc kho. `PYTHONDONTWRITEBYTECODE=1`, `PYTHONIOENCODING=utf-8`.

Thời gian: **~11 phút / ô** một luồng. Chạy 6 luồng song song thì 20 ô ≈ 45 phút.
Dung lượng: **~19–67 MB / ô** tùy cấu hình (soft-hybrid ghi nhiều chứng cứ nhất).

### 5.4 Kết quả sinh ra trong `--output`

| File | Nội dung |
|---|---|
| `summary.json` | `status`, `semanticHash`, `repositoryInventorySha256`, tài nguyên |
| `run-00.json` | `semantic.acceptedRequestIds` ← **số khách phục vụ đếm ở đây** |
| `transcript-00.ndjson` | mỗi dòng `{"frameBase64": "..."}`, base64 của một JSON frame |
| `bundle-manifest.json` | kê khai |
| `failure-00.json` | chỉ khi hỏng: `failureMessage`, `failureType`, `traceback` |

### 5.5 Đọc transcript

```python
import base64, json
with open(path, encoding="utf-8") as h:
    for line in h:
        frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
        if frame.get("messageType") != "decision":
            continue
        for action in frame["payload"]["actions"]:
            dt = action["decisionType"]     # promisePublished | vehiclePlanUpdated |
                                            # requestRejected | ...
```

Các đường dẫn hay dùng trong một frame `decision`:

| Đường dẫn | Nội dung |
|---|---|
| `payload.actions[].decisionType == "promisePublished"` | `.payload.promise{requestId,pickupEtaMs,dropEtaMs}`, `.payload.decisionDelta` (A), `.payload.exogenousDelta` (d), `.payload.visibleDelta` (B), `.payload.budgetBefore/budgetAfter` |
| `payload.actions[].decisionType == "vehiclePlanUpdated"` | `.payload.vehicleId`, `.payload.candidateId`, `.payload.route{executedStopCount, frozenPrefix[], mutableSuffix[], planVersion}` |
| `payload.actions[].decisionType == "requestRejected"` | khách bị từ chối |
| `payload.solver.executionEvidence.generation.vehicleLosses[]` | `candidateCapApplied`, `workBudgetExhausted`, `retainedCandidateCount`, `uniqueFeasibleCandidateCountBeforeCap`, `omittedFeasibleCandidateCountByCap`, `omittedUnexpandedCandidatePathCount`, `physicallyOrSchedulePrunedCount`, `evaluatedCandidatePathCount`, `eligibleRepairRequestCount`, `consideredRepairRequestCount` |
| `payload.solver.executionEvidence.selection.finalSolverDiagnostics.objectiveBounds[]` | `{objectiveName, levelIndex, incumbentValue, bestBound, isProvenOptimal}` — **các tầng mục tiêu từ điển** |
| `payload.solver.executionEvidence.prunedCandidates[]` | phương án bị loại, có `commitmentWitnesses` nếu do cam kết |
| `payload.reasonCode`, `payload.decisionHash`, `payload.stateBeforeHash/stateAfterHash`, `payload.certificate` | chuỗi chứng cứ |

**Cảnh báo về id:** `run-00.json` dùng `req-<32hex>`, transcript dùng `rq-<64hex>`. Không
so trực tiếp được — phải đối chiếu theo lực lượng (cardinality) hoặc theo thứ tự.

### 5.6 Các cấu hình quan trọng

**Chính sách (`--wp4-config`)**

| File | policyId | Vai trò |
|---|---|---|
| `wp9-fleetpy-rolling-cost-audited-v1.json` | `rolling-cost` | **B1** — không hứa gì |
| `wp9-fleetpy-ridebound-hard-vector-audited-v1.json` | `ridebound-hard-vector` | **C1** — cổng cứng |
| `wp9-fleetpy-soft-hard-hybrid-audited-v1.json` | `commit-soft-hard-hybrid` | có `warningProfiles`, `drop_eta_total_ms: warningLimit 60000` |
| (scratchpad) `wp9-fleetpy-no-reassignment-repair-explore-v1.json` | `no-reassignment-repair` | có `repair.maximumRequestsConsideredPerVehicle: 4` |

**Cam kết (`--commitment-config`)**

| File | Trần `drop_eta_total_ms` |
|---|---|
| `wp14-c1-nobudget-v1.json` | không trần (chỉ khóa xe + hai điểm dừng) |
| (scratchpad) `frontier/commit-budget300.json` | 300.000 ms |
| `wp14-c1-budget120-v1.json` | 120.000 ms |
| `wp14-c1-budget60-v1.json` | 60.000 ms |
| `wp14-c1-h6-reference-v1.json` ≡ `wp8-drop-eta-budget-tight-v1.json` | 30.000 ms (byte-tương đương, 0 lá khác) |
| `wp14-c1-f2-ratchet-v1.json`, `wp14-c1-f1-freeze300/600`, `wp14-c1-f1f2-freeze300-ratchet`, `wp14-c1-nopickuplock` | các biến thể bảo vệ giờ đón |
| (scratchpad) `drift/basis-customer-visible.json` | **chỉ khác đúng 1 lá**: `/policies[0]/budgetBasis` |

Mọi cấu hình cam kết đều có `vehicle_switch_count: 0`, `pickup_stop_switch_count: 0`,
`drop_stop_switch_count: 0` (hardLimit), và
`finalConfirmationLocks: ["vehicle","pickupStop","pickupEta"]`,
`materialRevisionRule: {rawEtaThresholdMs: 1000, displayBucketWidthMs: 60000}`.

**Ràng buộc:** runner từ chối `warningLimit > hardLimit` với `INVALID_COMMITMENT_WARNING_LIMIT`.
Nên soft-hybrid (cảnh báo 60 s) **chỉ ghép được** với trần ≥ 60 s, thực tế dùng trần 120 s.

### 5.7 Ghi đè cho thí nghiệm đặc biệt

**Nới cửa sổ đón 600 → 900 s** (`scratchpad/window/preflight_wide.py`): bọc preflight thật,
monkeypatch `_operator_settings` để đặt `op_max_wait_time = 900`; **từ chối chạy nếu giá trị
trong kho không còn là 600**. Đồng thời phải viết lại fixture
(`scratchpad/window/build_wide_fixture.py`): đổi `latestPickupMs` thành arrival+900 s trong
`requests[]` **và** trong `payloadCanonicalJsonHex` của event `requestArrived`, tính lại
`payloadSha256`, vá `sourceScenarioContentSha256` của driver. Dạng chuẩn:
`json.dumps(obj, sort_keys=True, separators=(",", ":"))` kèm bộ chặn round-trip.

**Bơm trôi dạt giao thông** (`scratchpad/drift/preflight_drift.py`): vá
`module._trigger_and_resolve`; đặt `control.routing_engine._current_tt_factor` (để `None` khi
factor == 1.0 để giữ đúng đường mã cơ sở), xóa `control._rb_travel_arc_cache`, đặt
`control._rb_travel_dirty = True`. Hệ số thật 15 phút của Manhattan, mô hình
`f_k(t) = (f_real(t0+t)/f_real(t0))^k`, chuẩn hóa để `f(0) = 1` chính xác. `k` nhận số thực.

---

## 6. Kỷ luật bằng chứng (BẮT BUỘC giữ)

1. **Không ghi gì vào kho.** Mọi script, cấu hình thử nghiệm, kết quả trung gian đi vào
   scratchpad hoặc `E:/RideBoundData/`. Kho chỉ đọc.
2. **Bằng chứng niêm phong.** Mỗi lần chạy có `semanticHash`, `repositoryInventorySha256`,
   `publicationDigest`, và băm nhị phân bộ chạy. Không trộn số liệu giữa hai bộ chạy khác
   nhau **trừ khi** đã chạy lại đối chứng và tái lập đúng từng ô (xem mục 7.5).
3. **Không so số giữa fixture gốc và fixture viết lại** (600 s vs 900 s). Chúng nằm trên hai
   thang khác nhau.
4. **Sàn nhiễu quỹ đạo: ±7 khách / ±0,3 điểm phần trăm** trên panel 20 ô. Đây **không** phải
   nhiễu thống kê — hạt giống cố định 7 ở mọi lần chạy; nó là độ nhạy quỹ đạo. Chênh lệch
   nhỏ hơn ngưỡng này **không được diễn giải**.
5. **Phân loại lỗi theo mã lỗi thật**, không theo so khớp chuỗi. Đã suýt báo "Định lý 1 sai"
   vì 11 ô hỏng, mở log ra mới thấy cả 11 là bất biến miền `RideRequest.cs:266` chứ không
   phải vô nghiệm do cam kết.

---

## 7. Toàn bộ kết quả thực nghiệm

**558 lần chạy, 33,62 GB.**

| Đợt | Lần chạy | Thư mục |
|---|---:|---|
| Panel niêm phong (B1, C1) | 60 | `wp9/confirmatory-h6-panela-v2` |
| Đường biên 9 cấu hình | 141 | `wp9/frontier-v1` |
| Cơ sở kết quả | 44 | `wp9/exploratory-visible-basis-v1`, `wp9/exploratory-visible-sweep-v1` |
| Thí nghiệm ratchet | 80 | `wp14/ratchet-secondary-v1` |
| Trần cửa sổ đón | 40 | `wp14/wide-window-v1` |
| Trôi dạt (cửa sổ 600 s) | 46 | `wp14/drift-v1` |
| Trôi dạt (cửa sổ 900 s) | 15 | `wp14/driftwide-v1` |
| Trôi dạt mức phân số k=0,5 | 12 | `wp14/drift-frac-v1` |
| Mặt cong hai chiều | 80 | `wp14/surface-v1` |
| Đặt trước ngân sách (mức C) | 20 | `wp14/levelc-v1` |
| Bộ sinh sắp xếp lại (b4) | 20 | `wp9/exploratory-b4-repair-v1` |

### 7.1 Quy trách — kết quả trung tâm

| | B1 | C1 | Chênh |
|---|---:|---:|---:|
| Khách phục vụ | 1.735 | 1.581 | −154 |
| Tỉ lệ phục vụ | 80,32% | 73,19% | **−7,13 pp** |
| Lần công bố lời hứa | 54.311 | 45.542 | −8.769 |
| Dịch chuyển khách nhìn thấy | 83.587 s | 9.332 s | −74.255 s |
| — do quyết định nhà xe (A) | **74.443 s** | **128 s** | −74.315 s |
| — do trôi dạt vật lý (d) | 9.203 s | 9.204 s | **+1 s** |
| **Tỉ lệ do nhà xe** | **89,06%** | **1,37%** | |

Nhóm chứng tự nhiên: `d` bằng nhau tới 0,02% giữa hai nhánh. Nhưng qua 6 cấu hình, `d` dao
động biên độ 5,6% và **không có xu hướng**, trong khi `A` thay đổi **580 lần**.

**Phân bố thiệt hại (tập trung, không dàn đều):**

| | B1 | C1 |
|---|---:|---:|
| Khách từng bị dời do nhà xe | 403 (23,2%) | 11 (0,7%) |
| Tổng số lần dời | 479 | 11 |
| Trung bình mỗi lần dời | 155 s | 11,6 s |
| **Khách nặng nhất** | **840,9 s** | 27,6 s |
| Phân vị 99 / 95 | 536,4 / 264,6 s | 0,0 / 0,0 s |

### 7.2 Đường biên — giá của cam kết (141 run, 9 cấu hình)

| Cấu hình | Lời hứa | Phục vụ | vs B1 (pp) | Xáo trộn A | Tệ nhất | Số bị dời |
|---|---|---:|---:|---:|---:|---:|
| B1 | không hứa gì | 1.735 | 0 | 74.443 s | 841 s | 403 |
| nobudget | khóa xe + điểm dừng | 1.655 | −3,70 | 22.485 s | 595 s | 142 |
| budget300 | + trần 300 s | 1.641 | −4,35 | 15.809 s | 291 s | 128 |
| budget120 | + trần 120 s | 1.608 | −5,88 | 5.063 s | 119 s | 76 |
| budget60 | + trần 60 s | 1.579 | −7,22 | 1.109 s | 59 s | 34 |
| **C1** | + trần 30 s | 1.581 | **−7,13** | **128 s** | 28 s | 11 |

- **Trần luôn được tôn trọng**: 291<300, 119<120, 59<60, 27,6<30.
- **Phần đắt nhất là quyết định cam kết chút nào đó**: B1→nobudget ngốn 3,70 pp, tức hơn
  nửa tổng chi phí 7,13 pp — mà chưa hứa một chữ nào về thời gian.
- Điểm gãy ở 300 s: 4,35 pp mua được "giờ trả không xê dịch quá 5 phút".

**Thang bảo vệ giờ đón — 6 cơ chế rơi vào đúng 2 hành vi:**

| Cấu hình | Phục vụ | vs B1 | Xáo trộn | Tệ nhất |
|---|---:|---:|---:|---:|
| nopickuplock / freeze300 | 1.583 | −7,04 | 187 s | 34 s |
| freeze600 / C1 (khóa khi xác nhận) | 1.581 | −7,13 | 128 s | 28 s |

Giải thích, từ 19.539 lần công bố: **0,0%** xảy ra sớm hơn 600 s trước giờ đón (tầm đặt chỗ
đúng bằng 600 s ⟹ hàng rào ≥600 s ≡ khóa vĩnh viễn); **46,4%** xảy ra sau khi khách đã lên
xe (⟹ chỉ nói về giờ trả); 36,8% trong 300 s cuối (⟹ hàng rào 300 s ≡ không khóa).

### 7.3 Độ khít của `B = A + d`

| Cấu hình | A | d | A+d | B | hụt | hụt % |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 74.443 | 9.203 | 83.646 | 83.587 | 58 | 0,07% |
| nobudget | 22.485 | 9.703 | 32.188 | 32.176 | 12 | 0,04% |
| budget300 | 15.809 | 9.641 | 25.450 | 25.441 | 9 | 0,03% |
| budget120 | 5.063 | 9.260 | 14.324 | 14.318 | 5 | 0,04% |
| budget60 | 1.109 | 9.184 | 10.293 | 10.291 | 1 | 0,01% |
| **C1** | 128 | 9.204 | 9.332 | 9.332 | **0** | **0,00%** |

### 7.4 Hai cơ sở tính

| Trần | Hành vi khả thi | Kết quả khả thi | Phục vụ trên ô chung |
|---|---:|---:|---|
| 30 s | **20/20** | 16/20 | hành vi 1.294 — kết quả 1.294 — chênh **0** |
| 120 s | **20/20** | 16/20 | hành vi 1.267 — kết quả 1.266 — chênh **−1** |

Tập ô vô nghiệm: trần 30 s = {16-r2, **16-r4**, 17-r1, 17-r3}; trần 120 s = {14-r4, 15-r2,
**16-r4**, 17-r4}. **Nới trần gấp 4 lần vẫn hỏng đúng 4 ô nhưng là tập khác, giao nhau đúng
1 ô** — dời chỗ đau, không chữa lành. Khớp Hệ quả 3.4.

### 7.5 Thí nghiệm ratchet (80 run, bộ chạy riêng)

Lý do tách: bộ chạy niêm phong dựng 22/08/2026, tính năng ratchet vào mã 04/09/2026 — bộ chạy
cũ không biết trường cấu hình, thoát ngay ở bước bắt tay. Giải pháp: dựng bộ chạy mới + chạy
**cả hai đối chứng đã biết kết quả**.

| Đối chứng | Bộ chạy mới | Bộ chạy niêm phong | Ô sai lệch |
|---|---:|---:|---:|
| reference (khóa cứng) | 1.581 | 1.581 | **0/20** |
| nopickuplock | 1.583 | 1.583 | **0/20** |

Kết quả:

| | nopickuplock | ratchet | khóa cứng |
|---|---:|---:|---:|
| Phục vụ | 1.583 | **1.581** | 1.581 |
| Xáo trộn do quyết định | 187 s | **128 s** | 128 s |
| Số lần dời | 13 | **11** | 11 |
| Khách tệ nhất | 34,4 s | **27,6 s** | 27,6 s |

> **Trong một bộ điều phối dựa trên chèn, bảo đảm một chiều ĐÚNG BẰNG khóa cứng.**
> Nó trông mềm hơn nhưng không mềm hơn chút nào.

Cơ chế: bộ sinh chỉ chèn thêm nên chỉ đẩy lùi giờ, không bao giờ kéo sớm.
`decisionMovedEarlier = 0` trên **421.752** lần sửa. Quyền "được phép cải thiện" mà ratchet
trao là quyền không bao giờ dùng được.

Ratchet chính là cơ chế Alonso-Mora và cộng sự dùng ⟹ đây là đối chiếu văn liệu trực tiếp.
Cũng dự đoán trước khi chạy: `freeze300+ratchet ≡ nopickuplock` — đúng.

### 7.6 Độ vững với cách đo — 9 thước × 6 cấu hình

| Thước đo | B1 | nobudget | 300 s | 120 s | 60 s | 30 s |
|---|---:|---:|---:|---:|---:|---:|
| Tuyến tính Σ\|δ\| | 74.443 | 22.485 | 15.809 | 5.063 | 1.109 | 128 |
| Bậc hai √Σδ² | 4.502 | 2.288 | 1.590 | 649 | 227 | 52 |
| Trọng số bậc thang | 180.824 | 58.841 | 40.943 | 13.129 | 2.975 | 300 |
| Trọng số cận kề | 41.571 | 13.618 | 9.541 | 3.214 | 728 | 77 |
| Đếm số lần dời | 479 | 155 | 135 | 79 | 34 | 11 |
| Khách tệ nhất | 841 | 595 | 291 | 119 | 59 | 28 |
| Phân vị 99 | 536 | 331 | 218 | 101 | 39 | 0 |
| Phân vị 95 | 265 | 115 | 83 | 0 | 0 | 0 |
| Số khách bị dời | 403 | 142 | 128 | 76 | 34 | 11 |

**Cả 9 đơn điệu, 0 ngoại lệ.** Nhưng **độ lớn lệch tới ~300 lần** (tuyến tính nói C1 tốt hơn
B1 585 lần; đếm số lần nói 43 lần; khách-tệ-nhất nói 30 lần) ⟹ **không được quảng cáo con số
585 lần**, phải báo cáo cả họ thước đo.

Trọng số: bậc thang = 3× nếu còn ≤300 s, 2× nếu ≤600 s, 1× ngoài ra; cận kề = 300000/(300000+r).

**Bất đối xứng ba đại lượng** (kết quả phương pháp trung tâm):

| Đại lượng | Phản ứng với chính sách |
|---|---|
| Độ ổn định lời hứa | Đơn điệu tuyệt đối, 9 thước, 0 ngoại lệ, trải 175 lần |
| Trôi dạt vật lý | Gần như bất biến, ±5,6%, không xu hướng |
| **Tỉ lệ phục vụ** | **Nhạy quỹ đạo, vi phạm đơn điệu ở 8/20 ô**, sàn nhiễu ±0,3 pp |

### 7.7 Thí nghiệm trôi dạt thật

| Mức | d p50 | d p90 | d max | % khách vượt 30 s **chỉ vì d** |
|---|---:|---:|---:|---:|
| k=0 phẳng | 4,9 s | 10,8 s | 39,9 s | 0,2% |
| k=0,5 | 9,8 s | 27,6 s | — | 7,9% |
| k=1 Manhattan thật | 14,1 s | 47,4 s | 150,7 s | **22,8%** |
| k=2 nhân đôi | 10,9 s | 69,9 s | 157,0 s | 20,3% |

**Phân loại theo nguyên nhân thật** (phải mở biên bản lỗi, không đếm suông):

| Cấu hình | Chạy được | Vô nghiệm do cam kết | Hỏng do bất biến vật lý |
|---|---:|---:|---:|
| hành vi, k=0 | 20 | **0** | 0 |
| kết quả, k=0 | 16 | **4** | 0 |
| hành vi, k=1 | 9 | **0** | 11 |
| kết quả, k=1 | 0 | **19** | 1 |

Thang 3 điểm: số ô vô nghiệm do cam kết — hành vi **0/20 ở cả ba mức**; kết quả 4 → 17 → 19.
Đơn điệu, không phải hiện tượng ngưỡng.

**Quy trách dưới trôi dạt** (9 ô chung):

| Mức | Do nhà xe | Do đường | Khách thấy | % do nhà xe |
|---|---:|---:|---:|---:|
| k=0 | 71 s | 3.984 s | 4.056 s | 1,76% |
| k=1 thật | 27 s | 12.155 s | 12.182 s | **0,22%** |

Tỉ lệ **450:1**. Tính theo cơ sở kết quả nghĩa là bắt nhà điều hành chịu trách nhiệm 12.155 s
tắc đường để kiểm soát 27 s hành vi của chính mình ⟹ cơ sở kết quả không chỉ **bất khả thi**
mà còn **bất công**.

**Vì sao không so được tỉ lệ phục vụ giữa hai cơ sở:** khả thi cấp ô sụp theo
`P(ô khả thi) ≈ (1−p)^n` với n ≈ 80 khách/ô — khớp cả ba mức trôi dạt. Không có mức trôi dạt
nào vừa cho `d` đáng kể vừa còn đủ ô chung. **Hệ quả: Định lý 3.3 biểu hiện theo kiểu phân
loại (mất nguyên cả ô) chứ không theo kiểu biên (phục vụ ít hơn vài khách).** Lối thoát là
giảm n: panel nhiều ô nhỏ hơn.

### 7.8 Phép thử trần cửa sổ đón

Nguyên nhân loại bỏ phương án (B1, 20 ô):

| Nguyên nhân | Số lần | Tỉ lệ |
|---|---:|---:|
| Quá cửa sổ đón | 94.021 | **78,64%** |
| Quá thời gian trên xe | 25.300 | 21,16% |
| Quá sức chứa | 239 | 0,20% |
| Tổng | 119.560 | |

Nhưng "phương án bị loại" ≠ "khách bị từ chối". Tách 425 khách bị từ chối: cả 425 đều có
phương án chết vì cửa sổ, và phần vượt **nhỏ nhất** của mỗi người có trung vị chỉ **44,4 s**,
trong khi trung vị trên toàn bộ phương án bị loại là 309,7 s ⟹ phương án tốt nhất của mỗi
người bị từ chối chỉ lỡ trong gang tấc.

Kết quả nới cửa sổ 600 → 900 s:

| Cấu hình | 600 s | 900 s | Chênh |
|---|---:|---:|---|
| B1 | 1.735 | 1.938 | +203 (+9,40 pp) |
| C1 | 1.581 | 1.753 | +172 (+7,96 pp) |
| **Giá của lời hứa** | **−7,13 pp** | **−8,56 pp** | |

**Bác bỏ dự đoán ban đầu.** Chi phí cam kết **nở ra** chứ không co lại. Chờ trung vị C1 tăng
407 → 636 s; mỗi khách cứu thêm tốn **2.421 s chờ cộng thêm trên toàn hệ**, trong đó chỉ
579 s là của chính người đó ⟹ món hời tồi, hướng nới cửa sổ đồng loạt bị loại.

**Mặt cong hai chiều (80 run):**

| Trần β | 600 s phục vụ | vs B1 | 900 s phục vụ | vs B1 | Chênh |
|---|---:|---:|---:|---:|---:|
| không trần | 1.655 | −3,70 | 1.837 | −4,68 | −0,97 |
| 300 s | 1.641 | −4,35 | 1.835 | −4,77 | −0,42 |
| 120 s | 1.608 | −5,88 | 1.794 | −6,67 | −0,79 |
| 60 s | 1.579 | −7,22 | 1.761 | −8,19 | −0,97 |
| 30 s | 1.581 | −7,13 | 1.753 | −8,56 | **−1,44** |
| B1 | 1.735 | — | 1.938 | — | |

> **Tự do của nhà điều hành và độ chặt của lời hứa TƯƠNG TÁC chứ không cộng độc lập.**
> Trần càng chặt thì cho thêm tự do càng đắt: −0,42 → −0,79 → −0,97 → −1,44 pp.

**Cơ chế đo được** (vì sao cửa sổ rộng làm lời hứa đắt hơn): công bố/khách **+30,2%**;
số lần cắt do cổng cam kết **+99,7%** (+83% mỗi khách); nhưng dịch chuyển mỗi khách **phẳng**
(0,050 → 0,049 s). ⟹ **β là per-khách nhưng chi tiêu là per-epoch**: cửa sổ rộng kéo dài thời
gian phơi nhiễm, nên cổng phải xóa gấp đôi để giữ cùng một mức.

### 7.9 Đối chiếu Fielbaum & Alonso-Mora (2020)

Cài đặt lại **chính thước đo của họ** (công thức 2.5) trên transcript của mình:

| | B1 | C1 |
|---|---:|---:|
| P(ΔD > 0) | 0,2329 | 0,0076 |
| E(ΔD \| ΔD > 0) | 160,4 s | 10,5 s |
| Thước hai đầu (giờ trả) | 64.814 s | 126 s |
| Thước chuỗi của ta (giờ trả) | 71.529 s | 6.822 s |
| **Tỉ số chuỗi / hai đầu** | **1,1×** | **54,1×** |
| Khách bị chấm 0 dù thực tế bị dời | 663 (38,2%) | 774 (**49,0%**) |

- Trên B1 hai thước **gần trùng** (1,1×) ⟹ kiểm định chéo: thước của ta không bịa chuyển động.
- Trên C1 lệch **54 lần** ⟹ **thước của văn liệu MÙ ĐÚNG Ở CHẾ ĐỘ mà khóa luận nghiên cứu**.
- Thước đếm của họ **không phân biệt được** B1 (14,99) với C1 (13,45), dù hai cấu hình cách
  nhau 7,13 pp dịch vụ. *Cảnh báo:* hệ của ta công bố ~30 lần/khách, hệ của họ ~5 lần/khách
  (cập nhật mỗi phút) ⟹ chỉ so B1 với C1 nội bộ, **không so trực tiếp với số in trong bài họ**.

Đối chiếu cơ chế:

| | Gốc | Siết chặt | Tuyệt đối | Tương đối |
|---|---:|---:|---:|---:|
| Fielbaum & Alonso-Mora (2020) | 34,5% | 45,6% | +11,1 pp | **1,32×** |
| Khóa luận (B1→C1) | 19,68% | 26,81% | +7,13 pp | **1,36×** |

**Đọc trung thực:** tính theo pp thì cơ chế của ta rẻ hơn; tính theo tỉ lệ thì nhỉnh hơn một
chút về phía xấu. Đây là **tái lập độc lập** trên thực thể nhỏ hơn 185 lần, **không phải
chiến thắng**.

**Ranh giới trùng / không trùng:**

| Nội dung | 2020 | Khóa luận |
|---|---|---|
| Khái niệm lời hứa công bố bị xê dịch | có | có |
| Đo độ lớn dịch chuyển từng khách | có | có |
| Đếm số lần dự báo bị đổi | có | có |
| Phân loại nguyên nhân (định tính, bằng lời) | có | có |
| Đường cong đánh đổi ổn định–phục vụ | có (3 điểm) | có (9 điểm) |
| Cơ chế ratchet trên giờ đón | có | có |
| **Trần số cưỡng chế được trên xê dịch cộng dồn** | **không** | **có** |
| **Dạng cộng dồn theo chuỗi (độ lớn × chuỗi)** | **không** | **có** |
| **Phân rã nhân quả định lượng theo từng quyết định** | **không** | **có** |
| **Phân biệt hai cơ sở tính + ba định lý** | **không** | **có** |

Chính các tác giả kết bài bằng: *"điều này càng cho thấy cần những ý tưởng tinh vi hơn để
kiểm soát bất ổn"* — họ gọi tên đúng chỗ trống khóa luận lấp vào.

### 7.10 Chứng cứ về tính không giả tạo

| Chỉ báo | Giá trị |
|---|---:|
| Tỉ lệ quyết định cạn ngân sách tìm kiếm | **0%** |
| Tỉ lệ quyết định chạm trần số ứng viên | **0%** |
| Số phương án khả thi bị bỏ sót do trần | **0** |
| Số nhánh chưa được mở rộng | **0** |
| Tỉ lệ loại bỏ do ràng buộc vật lý | 94% |
| Tỉ lệ loại bỏ do ràng buộc cam kết | **1,1%** |

Ràng buộc cam kết là **hẹp nhưng đòn bẩy cao**.

### 7.11 Phúc lợi — điểm hòa vốn

Thời gian bất ngờ tránh được: 74.255 s = 20,63 h. Số chuyến hy sinh: 154.
⟹ mỗi chuyến hy sinh đổi lấy **482 s (~8 phút)** thời gian bất ngờ tránh được cho tập thể.

| Định giá thời gian bất ngờ | Giá trị hòa vốn của một chuyến |
|---|---:|
| 7,88 EUR/h (giá trị thời gian trên xe, cận dưới) | 1,06 EUR |
| 10,80 EUR/h (cận trên) | 1,45 EUR |
| 20,00 EUR/h (chờ bất ngờ, cận dưới) | 2,68 EUR |
| 25,00 EUR/h (chờ bất ngờ, cận trên) | 3,35 EUR |

**Là một NGƯỠNG, không phải tuyên bố chiến thắng.** Ba giả định phải ghi rõ: mọi chuyến mất
có cùng thặng dư; đại lượng đo là **độ xáo trộn của lời hứa** chứ không phải **độ trễ**; hệ
số định giá từ bối cảnh địa lý khác.

---

## 8. Tám hướng đã thử và bị bác bỏ — kèm bằng chứng

### 8.1 Đệm ETA đồng loạt
Báo giờ muộn hơn thực tế để có chỗ hấp thụ. **Cần 265.000 s đệm để tránh 22.485 s xáo trộn —
tỉ lệ 12:1.** Loại.

### 8.2 Hứa theo hạn chót thay vì theo điểm
"Đón trước 9:15" thay vì "đón lúc 9:10". Phân tích: **đây chính xác là cửa sổ Ω và Δ đã có
sẵn**, không phải cơ chế mới. Loại.

### 8.3 Cổng mềm thay cổng cứng
Đọc mã bác bỏ **cả hai** kỳ vọng: (a) cổng cứng **không** bị gỡ — phương án chỉ được chấm
điểm cảnh báo **sau khi** đã qua cổng cứng (`retained.Add(candidate)` xảy ra sau các kiểm tra
cứng trong `HardVectorCandidateAssessor`); (b) ghép `warningLimit 60s > hardLimit 30s` sẽ hỏng
20/20 ô với `INVALID_COMMITMENT_WARNING_LIMIT`. Ngoài ra cổng mềm thật sự sẽ **đánh đổi mất
Định lý 3.1** — tài sản chính của khóa luận. Loại.

### 8.4 Nới cửa sổ đón đồng loạt
Đo thật: giá lời hứa **−7,13 → −8,56 pp** (tệ đi), chờ trung vị 407 → 636 s, 2.421 s chờ cộng
thêm mỗi khách cứu được. Loại (mục 7.8).

### 8.5 Mức A — xếp hạng vị trí chèn theo chi phí ngân sách
**Phép toán rỗng.** Đo trên **217.736 quyết định cấp xe** (113.064 B1 + 104.672 C1):

| Chỉ số | B1 | C1 |
|---|---:|---:|
| Chỉ có **1** ứng viên | **96,04%** | **95,87%** |
| Có ≥ 2 (tức có gì để chọn) | 3,96% | 4,13% |
| Chạm trần số ứng viên | 0 | 0 |
| Cạn ngân sách tính toán | 0 | 0 |
| Ứng viên khả thi bị bỏ do trần | 0 | 0 |
| Nhánh chưa khai triển bị bỏ | 0 | 0 |
| Trước trần / sau trần (ứng viên/xe) | 1,044 / **1,044** | 1,047 / **1,047** |

Với một ứng viên thì không có gì để sắp xếp. Xếp hạng chỉ chạm được ~4% quyết định, mà ở đó
chín phần mười trường hợp tập chỉ có đúng hai phần tử. Loại.

### 8.6 Mức B — cắt tỉa sớm bằng cận dưới ngân sách
**Phép toán rỗng.** 0 bỏ sót, 0 nhánh chưa khai triển ⟹ không có gì bị cắt để cắt sớm hơn;
0 lần cạn ngân sách ⟹ không có vấn đề tốc độ. Loại.

### 8.7 Mục 4 — bộ sinh biết sắp xếp lại
**Đã có sẵn trong kho**: `WaitingIncumbentRepairSeedBuilder`, bật qua
`repair.maximumRequestsConsideredPerVehicle`. Nó lấy một khách đang chờ, gỡ **cả cặp** đón–trả
khỏi `MutableSuffix`, chèn lại vào mọi vị trí giữ được thứ tự đón-trước-trả. Không gộp nhiều
nước đi, không đổi xe, không động vào người đã lên xe, không sửa `FrozenPrefix`.

Chạy với hạn mức 4 khách/xe, 20 ô:

| Nhánh | Ô | Cập nhật KH | Sắp lại | Đẩy chặng đầu | Đóng băng sớm |
|---|---:|---:|---:|---:|---:|
| B1 (chèn thuần) | 20 | 5.328 | **0** | 57 (1,07%) | **0** |
| C1 (chèn thuần, trần 30 s) | 20 | 4.864 | **0** | 17 (0,35%) | **0** |
| b4 (sắp lại) | 20 | 1.978 | **245** | 150 (**7,58%**) | **0** |

- Nó **thật sự sắp xếp lại**: chiều `incumbentOrderInversionCount` bị tính phí **116 lần,
  tổng 120 đơn vị** (trước nay luôn 0).
- Nó **dao động**: 167 lần một kế hoạch trùng đúng kế hoạch của hai lần công bố trước (A→B→A).
  Ví dụ xe `6eb906e5` ô `d20181114-s10-r2`, năm lần công bố liên tiếp đảo qua đảo lại rồi sập.
- **Hỏng 18/20 ô** với `RBWP7_LOCKED_LEG_MISMATCH` (1 ô lỗi protocol, 1 ô chạy trọn).
- Nguyên nhân: **bất biến miền #2** (mục 4.4).
- **Nếu đóng băng chặng đang chạy**: 102/245 (**41,6%**) lần sắp lại **vẫn hợp lệ**; 134 (54,7%)
  bị chặn; 9 (3,7%) chặng đầu vừa phục vụ xong. ⟹ bước sửa lấy đi một nửa láng giềng, **giữ
  lại một nửa**.
- Trên ô duy nhất chạy trọn (`d20181114-s10-r1`): **b4 = 99 = B1**, C1 = 92.
  ⟹ thêm quyền sắp xếp lại vào bộ điều phối vốn đã tự do hoàn toàn thu được **0 hành khách**.
  (n=1, chỉ dấu chứ chưa phải kết luận.)
- **Tổ hợp "sắp lại + cam kết" hiện không diễn đạt được** (mục 4.5).

### 8.8 Mức C — đặt trước ngân sách (chạy đủ 20 ô)
Ghép: soft-hybrid (cảnh báo 60 s) + `wp14-c1-budget120` (trần 120 s). Đối chứng:
`fr-budget120-*` đã niêm phong.

| | Đối chứng | Mức C |
|---|---:|---:|
| Khách phục vụ | 1.608 | **1.608** |
| Lần công bố lời hứa | 47.118 | **47.118** |
| Lần công bố có dịch chuyển | 79 | **79** |
| Xáo trộn tuyến tính | 5.063,3 s | **5.063,3 s** |
| Bậc hai / bậc thang / cận kề | 648,6 / 13.129,2 / 3.214,0 | **giống hệt** |
| Khách nhìn thấy / ngoại sinh | 14.318,1 / 9.260,2 | **giống hệt** |
| Khách bị dịch nặng nhất | 119,0 s | **119,0 s** |
| Số khách bị dời | 76 | **76** |

So **từng quyết định một** trên 20/20 ô: chuỗi (xe, ứng viên) được gán — **giống hệt**; tập lời
hứa công bố trong từng khung — **giống hệt**; chuỗi mã lý do — **giống hệt**.

**Tại sao** — đọc `objectiveBounds`:

| Tầng mục tiêu | Số lần | Khác 0 | Tỉ lệ |
|---|---:|---:|---:|
| `accepted-request-count` | 4.264 | 519 | 12,2% |
| `operational-cost` | 4.264 | 4.240 | 99,4% |
| **`worst-hard-utilization-ppm`** | 4.240 | **4.240** | **100,00%** |
| `warning-excess:drop_eta_total_ms` | 4.240 | **810** | **19,1%** |
| 9 chiều cảnh báo còn lại | 4.240 | 0 | 0% |
| `revision:drop_eta_total_ms` | 4.240 | 21 | 0,5% |

Ngưỡng 60 s **có** bị chạm (19,1%). Nhưng tầng ngay trên nó khác 0 trong **100%** quyết định.
Trong thứ tự từ điển, tầng dưới chỉ lên tiếng khi mọi tầng trên hòa. Tầng trên đo mức tiêu
ngân sách tệ nhất **theo phần triệu** — thang **liên tục** của đúng đại lượng mà ngưỡng chỉ
chia hai bậc.

> **Ý tưởng đặt trước ngân sách KHÔNG SAI — nó ĐÃ NẰM SẴN trong hệ thống ở dạng mạnh hơn.**
> Một tầng ngưỡng đặt dưới một tầng liên tục cùng ý nghĩa là **dư thừa về cấu trúc**.

**Cảnh báo cho người đọc tiếp:** `semanticHash` của hai nhánh **có khác nhau trên cả 20 ô**,
nhưng đó **không** phải bằng chứng quyết định khác nhau — nhánh soft-hybrid ghi thêm chứng cứ
cảnh báo và phát các lần công bố theo thứ tự khác **bên trong cùng một khung**. Đây là bẫy đã
vấp (mục 12.7).

---

## 9. Phát hiện hợp nhất — thứ biến đống kết quả âm thành một quan sát

Hai bất biến chặn hai hướng cải tiến thực ra là **cùng một câu hỏi, đặt trên hai trục**:

| | Ranh giới "cái gì đã ngoài tầm kiểm soát" |
|---|---|
| **Theo thời gian** | Phép phân rã ba mốc — mốc ngoại sinh `e` tính chính xác kế hoạch cũ sẽ ra sao nếu không ai can thiệp |
| **Theo cấu trúc lộ trình** | Tiền tố đóng băng — điểm dừng nào đã hết sửa được |

Và **hệ thống đang vạch ranh giới thứ hai SAI CHỖ**: ở lúc xe *tới* thay vì lúc xe *xuất phát*.
Sai lệch này vô hại với bộ sinh chèn thuần và chỉ lộ ra khi có cơ chế thật sự muốn sắp xếp lại.

Đồng thời: **cả bốn hạng mục cải tiến bị loại bởi chính các phép đo mà cơ chế lời hứa sinh ra.**
Sổ cái cam kết ghi đủ chi tiết để biết trước rằng sắp xếp lại không có chỗ tác động, **trước
khi** bỏ ngày nào ra chạy benchmark. Đó cũng là một kiểu giá trị của cơ chế, dù không phải kiểu
được nêu trong phát biểu vấn đề.

---

## 10. Điều còn mở — năm hướng phát triển đã viết vào chương 5

1. **Đo Định lý 3.3 trên panel có ít khách hơn mỗi ô.** Vì `P(ô khả thi) ≈ (1−p)^n` với n≈80,
   lối thoát là giảm n: nhiều ô nhỏ, mỗi ô vài chục khách ⟹ giữ được nhiều ô khả thi ở cùng
   mức trôi dạt ⟹ có tập ô chung để so tỉ lệ phục vụ. **Thay đổi thiết kế panel, không phải hệ
   thống. Chi phí thấp. Ưu tiên cao nhất.**
2. **Mở rộng mặt cong sang chiều tự do thứ ba.** Đã có 2 chiều (β × cửa sổ đón). Hai chiều tự
   nhiên tiếp theo: **cỡ đội xe** và **mật độ nhu cầu**. Nếu quy luật giữ nguyên trên cả ba
   chiều thì rút ra được quy tắc chọn β theo mức tự do.
3. **Cửa sổ đón thương lượng CÓ CHỌN LỌC.** Chưa bị bác bỏ. Bài toán đã đặt đúng, trần và kiểu
   hỏng đều đã đo: lấy được bao nhiêu trong **172 khách** mà vẫn giữ chờ trung vị quanh 407 s.
   Đòi hỏi sửa mã nguồn + mở rộng phát biểu vấn đề sang **kiểm soát tiếp nhận** (admission
   control) ⟹ cần cân nhắc kỹ về phạm vi.
4. **Nới lỏng bất biến miền về cửa sổ đón** (mục 4.3). Cơ chế nới theo mốc ngoại sinh đã tồn
   tại cho bộ sinh phương án; mở rộng sang tầng kiểm tra trạng thái sẽ cho phép nghiên cứu chế
   độ cao điểm đầy đủ.
5. **Đóng băng chặng đang chạy, rồi mới mở khóa bộ sinh sắp xếp lại.** Ba bước, đúng thứ tự:
   - (a) **Miền**: thêm chuyển trạng thái đóng băng chặng đang bay — chuyển `MutableSuffix[0]`
     vào `FrozenPrefix` **mà không tăng** `ExecutedStopCount`. Kiểu dữ liệu đã hỗ trợ, chỉ
     thiếu điểm gọi. **Không có bước này thì mọi thứ sau đều hỏng 18/20 ô.**
   - (b) **Chính sách**: cho `RideBoundHardVector` nhận
     `MaximumRepairRequestsConsideredPerVehicle` (hiện chỉ nhánh `NoReassignmentRepair` truyền
     tham số này vào `generationOptions.WithRepairRequestCap`).
   - (c) **Cấu hình**: nới `hasRepair != isB4` trong `RequireVariantFields`.
   - Cộng một bản dựng runner mới + hai nhánh đối chứng theo kỷ luật mục 7.5.
   - **Kỳ vọng nên đặt thấp**: ô duy nhất chạy trọn cho b4 = B1.

**Liên hệ văn liệu cho hướng 5:** prefix-freezing trong LRP (arXiv:2504.10649, 2025) là đúng ý
tưởng "đóng băng tiền tố"; xem thêm mục 11.

---

## 11. Vị trí trong văn liệu

**Hàng xóm gần nhất:** Fielbaum & Alonso-Mora (2020), *"On the unreliability of
ride-pooling"*. Trùng 6 hạng mục, khác 4 (bảng ở 7.9).

**Các khối xây dựng đã tìm được (chưa ai ghép lại thành cơ chế của ta):**

| Nguồn | Nội dung |
|---|---|
| arXiv:2003.05175 | reassignment-budget, competitive ratio `1 − 2/(k+2)` |
| arXiv:1811.08238, arXiv:1912.10769 | δ-commitment |
| arXiv:2504.10649 (2025) | LRP prefix-freezing + heuristic H5 + Definition 6.1 stability |
| Schulz & Pfeiffer, *OR Spectrum* 48:541-586 (2026) | potential-based insertion |
| arXiv:2609.11950 | TSP-SC |
| arXiv:1911.08842 | NeurADP |
| Sridharan, Berry & Udayabhanu (1987), *Management Science* 33(9) | họ thước đo bất ổn lịch trình (nguồn của 9 thước đo) |

**Tài liệu tham khảo trong báo cáo (17 mục):** `alonsomora2017`, `fielbaum2020`,
`fielbaum2022scale`, `alonsogonzalez2020`, `gerzinic2023`, `bansal2019`, `sridharan1987`,
`kovacs2014`, `fleetpy2022`, `cordeau2007`, `toth2014`, `groer2009`, `blackburn1986`,
`agatz2012`, `ortools`, `tlc`, `li2025`.

---

## 12. Bẫy đã vấp — đọc trước khi chạy gì

### 12.1 Chọn sai bộ cấu hình cho bộ chạy
Dùng `wp13-e1-*-retained` (build cho runner wp13) trên runner h6 ⟹
`RBWP7_RUNNER_EOF at $runner: helloAck`. **Luôn dùng `wp9-*-audited` với `h6-confirmatory-v1`.**

### 12.2 `op_max_wait_time` kẹp cửa sổ
Viết lại fixture lên 900 s mà không vá simulator ⟹
`FleetPy PlanRequest scalar round-trip drift`. Phải dùng `preflight_wide.py`.

### 12.3 Id không khớp giữa run và transcript
`run-00.json` dùng `req-<32hex>`, transcript dùng `rq-<64hex>`. Một script đếm khách bị từ
chối trả về 0/425 vì lý do này. Phải đọc `requestRejected` từ `frame["payload"]["actions"]`
và đối chiếu lực lượng.

### 12.4 Đếm lỗi thay vì phân loại lỗi
Suýt báo "Định lý 1 bị bác bỏ" khi cơ sở hành vi hỏng 11/20 ô ở k=1. Mở log ra: **cả 11 là
bất biến miền `RideRequest.cs:266`**, không phải vô nghiệm do cam kết. **Luôn phân loại theo
mã lỗi thật.**

### 12.5 Đoán tên trường trong bằng chứng
`why_wider_costs_more.py` đoán khóa `vehicleAssessments` — **không tồn tại**. Đường dẫn đúng
là `payload.solver.executionEvidence.generation.vehicleLosses[]`. **Dump cấu trúc trước khi
viết bộ phân tích.**

### 12.6 Heredoc bash làm hỏng chuỗi tiếng Việt
Sửa file Python/LaTeX có tiếng Việt bằng heredoc trong bash gây lỗi so khớp trên các neo nhìn
rõ ràng là có. **Dùng công cụ ghi/sửa file trực tiếp cho văn bản tiếng Việt.**

### 12.7 `semanticHash` khác nhau ≠ quyết định khác nhau
Đã suy luận sai một lần. Hồ sơ soft-hybrid ghi thêm chứng cứ cảnh báo và phát các lần công bố
theo **thứ tự khác trong cùng một khung**. Muốn biết quyết định có khác không, phải so
**chuỗi (xe, ứng viên) được gán** và **tập lời hứa đã sắp xếp trong từng khung**.

### 12.8 Tiến trình mồ côi
Giết tiến trình cha đã tách rời để lại 5 worker mồ côi. Xác minh dòng lệnh bằng
`Get-CimInstance Win32_Process` trước khi dừng, rồi dọn thư mục kết quả dở dang.
**Thư mục kết quả dở dang (có `transcript-00.ndjson` nhưng không có `summary.json`) sẽ chặn
lần chạy lại** — phải xóa trước khi resume.

### 12.9 Đánh số mục viết tay trong LaTeX
Các tham chiếu "mục 4.x" viết tay đã lệch (phúc lợi là 4.10 bị dẫn là 4.8; Fielbaum là 4.9
bị dẫn là 4.8; …). **Đã chuyển toàn bộ sang `\label`/`\ref`.** Giữ nguyên quy ước này.

### 12.10 Dự đoán sai đã ghi nhận (giữ tính trung thực)
- Dự đoán nới cửa sổ làm lời hứa **rẻ** hơn → thực tế **đắt** hơn (−7,13 → −8,56 pp).
- Dự đoán mức k≈0,5 sẽ "lấp lỗ hổng cuối cùng" → chứng minh được là **không thể** bằng
  `(1−p)^80`.
- Dự đoán cổng mềm sẽ thu hồi khách → đọc mã bác bỏ cả hai giả định.
- Dự đoán mức C sẽ đổi quyết định vì hash khác → sai (12.7).

---

## 13. Ràng buộc do người dùng đặt ra (còn hiệu lực)

1. *"Nếu thiếu về mặt ram thì có thể xóa 1 vài chương trình ngầm k dùng tới không làm ảnh
   hưởng hại đến máy."*
2. *"Không dùng quá nhiều (<30gb) dung lượng ổ cứng."* — **hiện đang là 33,62 GB, đã vượt.**
   `E:` còn ~79 GB trống nên không hại máy. **Chưa xóa gì.** Hai ứng viên an toàn nhất nếu
   cần giảm: `wp14/driftwide-v1` (1,10 GB) và `wp14/levelc-v1` (1,20 GB) — kết luận của cả
   hai đã trích xuất đầy đủ, nhưng xóa thì mất bằng chứng niêm phong.
3. *"Không tùy tiện xóa file quan trọng gây hư hại máy."*
4. *"đảm bảo tốt cho hệ thống"*
5. **Báo tiến độ mỗi 1 giờ** khi có job dài đang chạy.
6. **Người dùng đã tự xóa các mục 4–7 trong bản báo cáo tiếng Việt cũ của họ — TUYỆT ĐỐI
   KHÔNG thêm lại.** (Ràng buộc này áp cho tài liệu cũ, không phải bản LaTeX mới ở mục 14.)
7. **Không ghi gì vào kho** (`E:\Code\RideBound`). Kho chỉ đọc. Mọi thứ đi vào scratchpad hoặc
   `E:/RideBoundData/`.
8. `AGENTS.md` của kho yêu cầu: đọc `docs/00-index.md`, `docs/01-research-charter.md`,
   `docs/18-status-and-decision-log.md`, work package đang hoạt động trong
   `docs/16-roadmap-and-work-packages.md` **trước khi sửa bất cứ gì**; chạy
   `dotnet test RideBound.slnx` cho mọi thay đổi mã; **không bao giờ xóa research corpora,
   dữ liệu tải về, vendor checkout, artifact kết quả** như thao tác dọn dẹp.

---

## 14. Báo cáo LaTeX

**Vị trí:** `E:\Code\Report_INT3508\ridebound\`
**Build:** `cd E:\Code\Report_INT3508\ridebound && ..\tools\tectonic.exe -X compile main.tex --outdir .`
**Hiện trạng:** 66 trang A4, ~28.000 từ, biên dịch sạch, 0 tham chiếu treo.

Định dạng: Times New Roman 13pt, giãn dòng 1,5, lề T3/P2/T2/D2 cm, `\chaptername{Chương}`,
`\cftchappresnum{Chương }`. Môi trường định lý:
```latex
\newtheorem{dinhly}{Định lý}[chapter]
\newtheorem{hequa}[dinhly]{Hệ quả}
\theoremstyle{definition}
\newtheorem{dinhnghia}{Định nghĩa}[chapter]   % bộ đếm RIÊNG, đừng gộp với dinhly
```

| File | Nội dung |
|---|---|
| `main.tex` | khung tài liệu |
| `noi-dung/00-bia.tex` | bìa VN + EN — **còn `[chờ bổ sung]` chỗ tên cán bộ hướng dẫn** |
| `noi-dung/01-loi-cam-on.tex` | lời cảm ơn |
| `noi-dung/02-tom-tat.tex` | Tóm tắt + Abstract |
| `noi-dung/03-muc-luc.tex` | mục lục tự sinh |
| `noi-dung/04-viet-tat.tex` | từ viết tắt & ký hiệu |
| `noi-dung/05-chuong1.tex` | Chương 1 — Đặt vấn đề (có §1.3 "Chỗ đứng so với công trình gần nhất") |
| `noi-dung/06-chuong2.tex` | Chương 2 — Cơ sở lý thuyết |
| `noi-dung/07-chuong3.tex` | Chương 3 — Phương pháp + 3 định lý + hình tikz |
| `noi-dung/08-chuong4.tex` | Chương 4 — Thực nghiệm (13 mục, 34 bảng) |
| `noi-dung/09-chuong5.tex` | Chương 5 — Kết luận + 5 hướng phát triển |
| `noi-dung/10-tai-lieu.tex` | 17 tài liệu tham khảo |

**Cấu trúc chương 4** (số mục là số thật sau khi đã dùng `\label`):

| Mục | Nhãn | Nội dung |
|---|---|---|
| 4.1 | `muc:thietlap` | Thiết lập thực nghiệm |
| 4.2 | `muc:quytrach` | Quy trách: ai gây ra xáo trộn |
| 4.3 | `muc:duongbien` | Đường biên: giá của cam kết |
| 4.4 | `muc:haicoso` | So sánh hai cơ sở tính |
| 4.5 | `muc:dovung` | Độ vững với cách đo |
| 4.6 | `muc:ratchet` | Thí nghiệm phụ: bảo đảm một chiều |
| 4.7 | `muc:troidat` | Thí nghiệm trôi dạt thật |
| 4.8 | `muc:cuaso` | Phép thử trần cửa sổ đón (+ `muc:matcong`, `muc:batbien`) |
| 4.9 | `muc:doichieu` | Đối chiếu Fielbaum & Alonso-Mora (2020) |
| 4.10 | `muc:phucloi` | Phúc lợi: điểm hòa vốn |
| 4.11 | `muc:chungcu` | Chứng cứ về tính không giả tạo |
| 4.12 | `muc:bosinh` | **Bộ sinh phương án biết đến lời hứa** (mới, 2026-09-16) |
| 4.13 | `muc:dathu` | Các hướng đã thử và lý do từ bỏ |
| 4.14 | `muc:hanche` | Hạn chế của thực nghiệm |

**Chỗ cần điền:** `[chờ bổ sung]` trong `noi-dung/00-bia.tex` — tên cán bộ hướng dẫn.

---

## 15. Script phân tích đã viết (scratchpad)

**Đã sao chép ra chỗ bền vững:** `E:\Code\Report_INT3508\ridebound-scratchpad\`
(121 file, 2,8 MB — toàn bộ script `.py`, ghi chép `.md`, cấu hình `.json`, `.sh`, `.txt`;
log và `__pycache__` đã lược bỏ). Bản gốc nằm trong thư mục tạm của phiên làm việc và sẽ mất
khi phiên kết thúc.

Các script dùng đường dẫn tuyệt đối tới `E:/RideBoundData/...` và `E:/Code/RideBound/...` nên
chạy được ngay từ vị trí mới; riêng `compare_levelc.py` cần thư mục `measure/` nằm cùng cây
(nó `sys.path.insert` theo đường dẫn tương đối `../measure`).

| Thư mục | Script | Chức năng |
|---|---|---|
| `measure/` | `measure_instability.py` | 9 thước đo bất ổn (`scan_run`, `percentile`, `DIMS`) |
| `welfare/` | `extract_promise_movement.py`, `aggregate.py` | bóc tách ba mốc, điểm hòa vốn |
| `frontier/` | `run_frontier.py`, `run_ratchet.py`, `frontier_table.py` | đường biên 9 cấu hình, ratchet |
| `window/` | `measure_window.py` | phân tích ràng buộc cửa sổ đón |
| | `build_wide_fixture.py` | viết lại fixture 600 → 900 s |
| | `preflight_wide.py` | ghi đè `op_max_wait_time` |
| | `run_window.py`, `run_surface.py` | phép thử trần, mặt cong 2 chiều |
| | `fielbaum_measure.py` | cài đặt thước đo của văn liệu trên dữ liệu ta |
| | `service_quality.py` | chờ/trên xe thực tế |
| | `why_wider_costs_more.py` | kiểm định H1/H2/H3 cho hiệu ứng cửa sổ |
| `drift/` | `preflight_drift.py`, `preflight_drift_wide.py` | bơm trôi dạt giao thông |
| | `run_drift.py`, `run_drift_frac.py`, `run_driftwide.py` | thang trôi dạt (`classify()` tách commitment / window-wall / other) |
| | `basis-customer-visible.json` | cấu hình cơ sở kết quả (khác đúng 1 lá) |
| `b4/` | `choice_set_census.py` | độ mỏng tập lựa chọn toàn panel |
| | `reorder_census.py`, `head_census.py` | hành vi bộ sinh sắp xếp lại |
| | `survivable_reorders.py` | bao nhiêu sắp-lại sống sót nếu đóng băng chặng đầu |
| | `diag_locked_leg.py`, `diag2.py`, `diag3.py` | chẩn đoán `LOCKED_LEG_MISMATCH` |
| `levelc/` | `run_levelc.py` | chạy + báo cáo mức C |
| | `decision_identity.py` | so **từng quyết định** giữa hai nhánh (sắp xếp trong khung!) |
| | `compare_levelc.py` | 9 thước đo, điều trị vs đối chứng |
| | `warning_layer.py` | đọc các tầng `objectiveBounds` |
| `report/` | `patch_bosinh.py` | vá chương 4/5 + chuyển tham chiếu sang `\label`/`\ref` |
| `survey/` | `muc-3-va-4-sinh-ung-vien-2026-09-16.md` | ghi chép đầy đủ mục 3 & 4 (350 dòng) |
| | `dinh-ly-conduct-vs-outcome.md` | định lý + đo đạc hai cơ sở (473 dòng) |
| | `ket-qua-A-C-D.md` | kết quả chân A, C, D (766 dòng) |
| | `ket-qua-troi-dat-2026-09-15.md` | thí nghiệm trôi dạt (186 dòng) |
| | `bao-cao-trang-thai-2026-09-15.md` | báo cáo trạng thái (332 dòng) |
| | `khao-sat-van-lieu.md` | khảo sát 14 trục văn liệu (170 dòng) |
| | `huong-di-v2.md` | phân tích hướng đi sau khi đọc 6 bài (271 dòng) |
| `salvage/` | 12 file `design-*.md`, `lit-*.md` | các thiết kế/khảo sát đã cân nhắc |

---

## 16. Việc tiếp theo đề xuất, theo thứ tự

1. **Điền tên cán bộ hướng dẫn** vào `noi-dung/00-bia.tex`, build lại.
2. **Quyết định dung lượng**: giữ 33,62 GB hay xóa `driftwide-v1` + `levelc-v1` để về ~31,3 GB.
3. **Sao chép scratchpad ra chỗ bền vững** — nó nằm trong thư mục tạm.
4. **Hướng nghiên cứu ưu tiên số 1**: panel nhiều ô nhỏ (mục 10.1). Chi phí thấp nhất, trả
   lời được câu hỏi duy nhất mà Định lý 3.3 chưa đo được trên panel hiện tại.
5. Nếu muốn theo mục 4: làm **đúng thứ tự (a) → (b) → (c)** ở mục 10.5, và nhớ dựng runner mới
   + chạy hai đối chứng theo kỷ luật 7.5.

---

## 17. Những gì KHÔNG được tuyên bố

Để tránh người đọc tiếp nói quá:

- ❌ Khóa luận **không** tuyên bố vượt trội về tỉ lệ phục vụ. **Mọi** cấu hình có cam kết đều
  phục vụ ít khách hơn cấu hình không cam kết.
- ❌ **Không** tuyên bố mạnh hơn Fielbaum & Alonso-Mora (2020). Phép so là **tái lập độc lập**
  trên thực thể nhỏ hơn 185 lần; tính theo tỉ lệ thì cơ chế của ta còn nhỉnh hơn một chút về
  phía xấu (1,36× so với 1,32×).
- ❌ **Không** quảng cáo "tốt hơn 585 lần" — con số đó chỉ đúng với một thước đo trong chín.
- ❌ **Không** so số tuyệt đối với văn liệu: panel 108 yêu cầu/8 xe nhỏ hơn nhiều so với các
  thực nghiệm quy mô Manhattan.
- ❌ Lập luận phúc lợi là **một ngưỡng**, không phải kết luận.
- ❌ Trôi dạt trên panel chính chỉ là **cận dưới** (đồ thị thời gian di chuyển tĩnh, trôi dạt
  đến từ độ trễ thực thi chứ không từ tắc đường).
- ✅ **Được** tuyên bố: biến một đại lượng trước nay chỉ đo được **sau sự việc** thành một ràng
  buộc **cưỡng chế được trước khi quyết định**; và chỉ ra rằng **cách tính sổ cái quyết định
  hệ thống có vận hành nổi hay không**.

---

## 18. Một đoạn để dán vào đầu phiên mới

> Tôi đang làm khóa luận về RideBound — hệ điều phối xe đi chung có cơ chế "lời hứa có biên
> được chứng nhận". Kho ở `E:\Code\RideBound` (chỉ đọc, không ghi gì vào kho). Kết quả thực
> nghiệm ở `E:\RideBoundData\`. Báo cáo LaTeX ở `E:\Code\Report_INT3508\ridebound\`.
> Đã có 558 lần chạy mô phỏng, 3 định lý đã chứng minh và xác nhận, báo cáo 66 trang.
> Tám hướng cải tiến đã thử và tất cả đều bị dữ liệu bác bỏ. Đọc file
> `E:\Code\Report_INT3508\RIDEBOUND-BAN-GIAO-CONTEXT.md` để nạp toàn bộ ngữ cảnh trước khi
> đề xuất bất cứ điều gì — đặc biệt là mục 8 (những hướng đã chết và vì sao) và mục 12
> (các bẫy kỹ thuật).
