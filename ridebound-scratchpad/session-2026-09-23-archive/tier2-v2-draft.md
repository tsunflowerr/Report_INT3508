### Tầng 2 — Thí nghiệm xác nhận: các họ cổng dưới trôi dạt Manhattan thật, theo cả hai chiều. 🔬

**Câu hỏi.** Định lý 4 chứng minh rằng dưới (N), cổng hành vi không bao giờ là nguyên nhân làm rỗng
tập phương án, còn ba họ kia thì có thể; Hệ quả 4.3 nói **họ nào** hỏng phụ thuộc **chiều** trôi.
Trên dữ liệu thật: (i) ranh giới đó có đúng từng ô không; (ii) nó có đoán đúng trên dữ liệu **chưa
ai nhìn thấy**, kể cả chiều trôi thuận lợi, không?

| | **2A — xác nhận cơ chế có đối chứng** | **2B — xác nhận trên tập giữ lại** |
|---|---|---|
| Panel | panel A (ngày 14–18/11, 20 ô, khung sáng) | panel phát triển (ngày 12–13/11, 16 ô: 8 `w08` sáng + 8 `w17` tối) — K17 |
| Đã từng dùng để dựng phương pháp dự đoán? | **Có** (`cellpred`, `retrodict`) | **Không** |
| Chiều trôi | bất lợi (×1,17–1,26) | sáng bất lợi (×1,14–1,15); tối **thuận lợi** (×0,84–0,87) — K18 |
| Mức trôi | `k ∈ {0, 1}` | `k = 1` |
| Nhánh | `dl-30`, `dl-60`, `dl-120` + 2 đối chứng; dùng lại `conduct-30`, `visible-30` | `conduct-30`, `visible-30`, `dl-30`, `dl-120`, `dl2-30` (tùy chọn `dl-60`) |
| Lần chạy | 120 + 40 đối chứng = **160** | **80** (96 nếu có `dl-60`) |
| Kết cục chưa thấy trước khi dự đoán? | Có — chưa nhánh hạn chót nào từng chạy | Có — kể cả nhánh hành vi |
| Tên được phép dùng khi viết | *"xác nhận cơ chế có đối chứng"* | *"xác nhận trên tập giữ lại"* |

**Vì sao đây là thí nghiệm giá trị nhất trên mỗi đơn vị công sức:**
1. Nó kiểm một định lý bằng dữ liệu, không phải so hai con số.
2. Nó trả lời thẳng câu *"Schulz cũng có trần rồi, em khác gì?"*.
3. 2B là **phép thử phân biệt**: một nhận định thô *"hạn chót hỏng khi có trôi dạt"* đoán sai buổi
   tối; Định lý 4 đoán hạn chót một chiều gần như an toàn buổi tối, còn hạn chót hai chiều và cổng kết
   quả thì không. Không cần tự tạo profile trôi dạt — khung tối thật đã giảm (K18).
4. Gần như **không cần viết lại lõi**. Hạn chót một chiều hỏng theo đường fail-closed đã có (K6). Hạn
   chót hai chiều và cổng kết quả buổi tối đi vào đường K20 (no-op bị loại, còn phương án khác) — hôm nay
   đường này chết với lỗi ánh xạ chung chung. Thay đổi 6 biến nó thành lỗi có mã riêng, **không đổi kết
   quả của lần chạy nào đang thành công**.
5. Dùng lại hạ tầng trôi dạt đã có (`preflight_drift.py`, hệ số Manhattan đo thật), chỉ thêm việc đọc
   mốc giờ khung từ fixture.

#### T2.0 — Cổng trước khi bắt đầu ⚠️

| Cổng | Vì sao | Ai quyết |
|---|---|---|
| **Phá kỷ luật "kho chỉ đọc"** cho đúng 6 tệp nguồn + 6 tệp test ở T2.1–T2.2, **trong worktree riêng** | Runner được build từ mã nguồn; không có cách thêm luật hạn chót mà không sửa mã | **Người dùng** |
| **Dung lượng:** hiện 33,62 GB, mục tiêu < 30 GB; Tầng 2 thêm ~5–15 GB | Ràng buộc người dùng #2 | **Người dùng.** Hai ứng viên xóa an toàn nhất là `wp14/driftwide-v1` (1,10 GB) và `wp14/levelc-v1` (1,20 GB), nhưng `AGENTS.md` cấm xóa artifact kết quả như thao tác dọn dẹp ⟹ cần quyết định tường minh. Có thể chạy 2B trước (80 lần, ~2–5 GB) nếu phải chọn |
| **Thăm dò hay chính thức** | Chính thức thì phải qua WP14R-012 + ADR (§7.1) | **Người dùng.** Đề xuất: **thăm dò có đối chứng và tiền đăng ký**, đúng tiền lệ `wp14/drift-v1`, gắn nhãn rõ |

**Cô lập thay đổi mã:** dùng `git worktree` để **không đụng** cây làm việc chính, nơi đang có thay đổi
chưa commit của người dùng (`docs/benchmarking/wp14r-013-…md` sửa 38 dòng; `docs/benchmarking/Kết quả
benchmark.md` chưa theo dõi). `AGENTS.md`: *"Preserve user-owned and unrelated changes."*

```powershell
cd E:\Code\RideBound
git worktree add ..\RideBound-deadline -b research/deadline-gate 41a4e11
# Mọi sửa đổi Tầng 2 làm trong E:\Code\RideBound-deadline
```

⚠️ Preflight băm `repositoryInventorySha256` trên cây mà nó chạy. Chạy preflight **từ worktree** thì nó
băm worktree — nhất quán. Ghi hash đó cho mọi lần chạy.

#### T2.1 — Mã nguồn: sáu tệp

**Thiết kế:** một **luật** mới, không phải chiều thứ 11 của vector cam kết. Chiều thứ 11 tốn ~30 điểm
sửa (15 tệp cấu hình, schema, adapter Python, ~10 test) và làm mất hiệu lực mọi hash đã ghi. Luật mới
mặc định **tắt** (ràng buộc WP15 #3). Thay đổi 6 chỉ để chẩn đoán.

⚠️ **Khác biệt ngữ nghĩa, phải chú thích trong mã:** mọi khóa hiện có so ứng viên với **mốc ngoại sinh
`e`** (`CommitmentLockEvaluator.cs:68-78` truyền `exogenous` vào vị trí tham chiếu), nên trôi dạt
**không bao giờ** làm vướng khóa. Luật hạn chót so ứng viên với **lời hứa đầu `p_0`**, nên trôi dạt
**có thể** làm vướng — đúng điều Định lý 4 nói. Nó là một **cổng**, dù được cài cạnh bộ đánh giá khóa.

**(1) `src/RideBound.Domain/Commitments/CommitmentVector.cs`** — thêm hai mã vào `CommitmentFailureCodes`
(dòng 135–153, cạnh `VehicleHasNoFeasibleCandidate` ở dòng 151):

```csharp
public const string DeadlineExceeded = "COMMITMENT_DEADLINE_EXCEEDED";
public const string SafetyNoOpRejected = "COMMITMENT_SAFETY_NOOP_REJECTED";
```

**(2) `src/RideBound.Domain/Commitments/CommitmentPolicy.cs`** — hàm dựng hiện có 8 tham số, 4 cuối tùy
chọn (dòng 129–137). Thêm tham số thứ 9 và 10, **tùy chọn, ở cuối**, để hai nơi gọi trong `src/`
(`CommitmentCandidateAssessor.cs`, `CommitmentPolicyConfiguration.cs`) không phải đổi. Kiểm tra mới theo
đúng mẫu `"Freeze-horizon locks require a freeze horizon."` đã có trong hàm dựng:

```csharp
public CommitmentPolicy(
    string policyId,
    CommitmentBudgetBasis budgetBasis,
    IEnumerable<CommitmentDimensionLimit> limits,
    MaterialRevisionRule materialRevisionRule,
    Duration? freezeHorizon = null,
    PromiseLock freezeHorizonLocks = PromiseLock.None,
    PromiseLock finalConfirmationLocks = PromiseLock.None,
    PromiseLock ratchetLocks = PromiseLock.None,
    Duration? dropEtaDeadlineSlack = null,          // MỚI
    bool dropEtaDeadlineTwoSided = false)           // MỚI
{
    // … giữ nguyên toàn bộ kiểm tra hiện có …

    if (dropEtaDeadlineTwoSided && dropEtaDeadlineSlack is null)
    {
        throw new ArgumentException(
            "A two-sided deadline requires a deadline slack.",
            nameof(dropEtaDeadlineTwoSided));
    }

    // … các phép gán hiện có …
    DropEtaDeadlineSlack = dropEtaDeadlineSlack;
    DropEtaDeadlineTwoSided = dropEtaDeadlineTwoSided;
}

/// <summary>
/// Deadline on the drop ETA measured from the rider's FIRST published promise
/// (Schulz &amp; Pfeiffer 2026 style). Unlike every lock, this compares the candidate with the
/// initial promise rather than with the exogenous projection, so exogenous drift CAN trip it.
/// Null disables the rule.
/// </summary>
public Duration? DropEtaDeadlineSlack { get; }

/// <summary>
/// When true the deadline is a window: the drop ETA may not move earlier than the initial
/// promise by more than the slack either. Research probe for the two-sided family.
/// </summary>
public bool DropEtaDeadlineTwoSided { get; }
```

`Duration` (`src/RideBound.Domain/Common/DomainPrimitives.cs:138-144`) đã từ chối `< 0` và
`> MaxCanonicalInteger`, **chấp nhận 0** — không cần kiểm thêm ở đây.

`MechanismCommitmentPolicyProvider` (`CommitmentCandidateAssessor.cs:97-108`) dựng lại chính sách cho
B1–B4 **không truyền** tham số mới ⟹ `null`/`false` ⟹ baseline không bị ràng buộc. Đúng ý định; T2.2 có
test.

**(3) `src/RideBound.Domain/Commitments/CommitmentLockEvaluator.cs`** — thêm tham số `anchor` **tùy chọn
ở cuối** chữ ký `Evaluate` (dòng 13–19), nên 6 nơi gọi trong test (`CommitmentLockEvaluatorTests.cs`
×4, `CommitmentRatchetLockTests.cs` ×2) không vỡ. Nhưng **ném lỗi** nếu chính sách có hạn chót mà thiếu
`anchor` — bài học từ bẫy `EffectivePolicies`: cấu hình sai phải hỏng to, không được im lặng.

```csharp
public IReadOnlyList<CommitmentLockWitness> Evaluate(
    RideRequest request,
    PublishedPromise previous,
    PromiseProjection exogenous,
    PromiseProjection candidate,
    SimTime evaluationTime,
    CommitmentPolicy policy,
    PromiseProjection? anchor = null)                // MỚI: lời hứa đầu tiên p_0
{
    // … giữ nguyên toàn bộ phần hiện có, đến ngay trước câu return …

    if (policy.DropEtaDeadlineSlack is Duration slack)
    {
        if (anchor is null)
        {
            throw new ArgumentException(
                "A drop ETA deadline requires the initial promise anchor.",
                nameof(anchor));
        }

        if (anchor.RequestId != request.Id)
        {
            throw new ArgumentException(
                "Deadline anchor identity must match the request.",
                nameof(anchor));
        }

        // Compared with the INITIAL promise, not with the exogenous projection.
        var shift = candidate.DropEta.Milliseconds - anchor.DropEta.Milliseconds;

        if (shift > slack.Milliseconds)
        {
            witnesses.Add(new CommitmentLockWitness(
                request.Id, "drop_eta_ms", "deadline_cap"));
        }
        else if (policy.DropEtaDeadlineTwoSided && -shift > slack.Milliseconds)
        {
            witnesses.Add(new CommitmentLockWitness(
                request.Id, "drop_eta_ms", "deadline_floor"));
        }
    }

    return witnesses
        .Distinct()
        .OrderBy(value => value.Dimension, StringComparer.Ordinal)
        .ThenBy(value => value.Rule, StringComparer.Ordinal)
        .ToArray();
}
```

Phép trừ và đổi dấu an toàn: cả hai giá trị ≤ `MaxCanonicalInteger = 2^53 − 1`, hiệu nằm gọn trong
`long`.

**(4) `src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs`** — tại nơi gọi duy nhất
(dòng 346–352) truyền lời hứa đầu; tại khối ánh xạ witness (dòng 354–367) dùng mã và thông điệp riêng
cho từng phía của hạn chót:

```csharp
var initialEntry = priorHistory.Entries[0];
if (initialEntry.Kind != CommitmentLedgerEntryKind.InitialPromise)
{
    throw new InvalidOperationException(
        "The first ledger entry must be the initial promise.");
}

var lockWitnesses = _lockEvaluator.Evaluate(
    request,
    priorHistory.Current.PublishedPromise,
    exogenousProjection.Value!,
    candidateProjection.Value!,
    context.CandidateState.Run.SimulationTime,
    policy,
    anchor: initialEntry.PublishedPromise.Projection);   // MỚI

if (lockWitnesses.Count != 0)
{
    var lockFailures = lockWitnesses.Select(
        value => value.Rule switch
        {
            "deadline_cap" => new CommitmentValidationWitness(
                CommitmentValidationStage.Lock,
                CommitmentFailureCodes.DeadlineExceeded,
                "The candidate delays the drop ETA beyond the initial-promise deadline.",
                request.AssignedVehicleId, value.RequestId, value.Dimension, value.Rule),
            "deadline_floor" => new CommitmentValidationWitness(
                CommitmentValidationStage.Lock,
                CommitmentFailureCodes.DeadlineExceeded,
                "The candidate moves the drop ETA outside the initial-promise window.",
                request.AssignedVehicleId, value.RequestId, value.Dimension, value.Rule),
            _ => new CommitmentValidationWitness(
                CommitmentValidationStage.Lock,
                CommitmentFailureCodes.PhaseLock,
                "The candidate changes a phase-locked promise field.",
                request.AssignedVehicleId, value.RequestId, value.Dimension, value.Rule),
        });
    // … phần còn lại giữ nguyên …
}
```

`RiderCommitmentHistory.Entries` có sẵn (`CommitmentLedger.cs:81-115`); `Entries[0]` luôn là entry
`InitialPromise` được mở ở `CommitmentLedger.cs:189-195`.

**(5) `src/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs`** — thêm hai khóa vào
`PolicyFields` (dòng 20–28), rồi truyền vào hàm dựng trong `ReadPolicy` (dòng 143–184), theo đúng mẫu
`freezeHorizonMs` ở dòng 178–180. Tệp không có bộ đọc bool; lỗi cấu hình của tệp dùng
`InvalidDataException`:

```csharp
// PolicyFields: thêm "dropEtaDeadlineSlackMs", "dropEtaDeadlineTwoSided"

return new CommitmentPolicy(
    /* … 8 đối số hiện có giữ nguyên … */,
    ReadLocks(element, "ratchetLocks"),
    element.TryGetProperty("dropEtaDeadlineSlackMs", out var deadline)
        ? new Duration(PositiveInteger(deadline, "dropEtaDeadlineSlackMs"))
        : null,
    element.TryGetProperty("dropEtaDeadlineTwoSided", out var twoSided)
        && twoSided.ValueKind switch
        {
            JsonValueKind.True => true,
            JsonValueKind.False => false,
            _ => throw new InvalidDataException(
                "'dropEtaDeadlineTwoSided' must be a boolean."),
        });
```

`PositiveInteger` từ chối 0, đủ cho các mức ở Tầng 2 (30.000 / 60.000 / 120.000 ms). Muốn thử trần 0
như Schulz thì phải thêm bộ đọc số nguyên không âm.

**(6) `src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs` — chỉ để chẩn đoán.** Hai
chỗ hở đã nêu ở §5.2: thông điệp fail-closed báo ứng viên đầu tiên theo id băm chứ không phải no-op, và
đường K20 chết muộn với lỗi ánh xạ chung chung. Sửa cả hai **ngay sau vòng lặp ứng viên** (vòng lặp kết
thúc ở dòng ~186, khối fail-closed ở dòng 188–216):

```csharp
var noOp = set.Candidates.SingleOrDefault(value => value.IsNoOp);
var noOpPrune = noOp is null
    ? null
    : hardPruned.SingleOrDefault(
        value => value.CandidateId == noOp.CandidateId);

if (retained.Count == 0)
{
    // Report the safety no-op's own rejection when there is one, so the cause
    // of an empty set is attributable. Otherwise keep the old ordinal choice.
    var first = noOpPrune ?? hardPruned
        .OrderBy(value => value.CandidateId, StringComparer.Ordinal)
        .FirstOrDefault();
    // … phần còn lại của khối hiện có giữ nguyên …
}

if (noOpPrune is not null)
{
    // A commitment rule removed the no-op but kept another candidate. Today this
    // state dies later in CandidateSelectionProblem.Create with a generic mapping
    // failure, so failing here changes no successful run.
    var noOpValidation = hardValidationWitnesses.TryGetValue(
        noOpPrune.CandidateId,
        out var noOpWitness)
        ? noOpWitness
        : null;
    return HardVectorCandidateAssessmentResult.Failure(
        new CommitmentAssessmentWitness(
            CommitmentFailureCodes.SafetyNoOpRejected,
            "C1 rejected the safety no-op while other candidates survived. " +
            $"No-op rejection: {noOpPrune.Message}",
            noOpPrune.CandidateId,
            set.VehicleId,
            noOpValidation?.RequestId,
            noOpValidation?.Dimension,
            noOpPrune.Code,
            noOpValidation?.Before,
            noOpValidation?.After,
            set.Candidates.Count,
            hardPruned.Count));
}
```

Thông điệp chứa `noOpPrune.Message` theo đúng thành ngữ `"First rejection: {first.Message}"` đã có;
**không** thêm tiền tố kiểu `firstCode=` — test `ExactSmallCommitmentDifferentialTests.cs:624-633` cấm
điều đó (*"Every diagnostic field must be typed rather than parsed out of prose"*). Ở ranh giới chính
sách, `AssessmentFailure` (`SolverBackedRidePoolingPolicy.cs:484-493`) giữ `Message` và `CandidateId`, nên
bộ phân loại đọc được cả hai từ artefact.

Nhờ các thông điệp riêng, artefact lỗi sẽ có dạng:
- `"C1 rejected every generated candidate for this vehicle. First rejection: The candidate delays the drop
  ETA beyond the initial-promise deadline."` — hạn chót một chiều, no-op vi phạm, mọi phương án vi phạm;
- `"C1 rejected the safety no-op while other candidates survived. No-op rejection: The candidate moves the
  drop ETA outside the initial-promise window."` — hạn chót hai chiều, trôi thuận lợi;
- `"C1 rejected the safety no-op while other candidates survived. No-op rejection: <thông điệp ngân sách>"`
  — cổng kết quả, trôi thuận lợi.

⚠️ **Kiểm tra bằng grep trước khi build:** `CommitmentPolicy` có được tuần tự hóa vào checkpoint hay
canonical state không (`src/RideBound.Runner/Online/OnlineStateCanonicalizer.cs`,
`OnlineStateCheckpointCodec.cs`)? Nếu có, thêm hai trường mới vào cả hai và vào test round-trip. Theo khảo
sát, trạng thái chỉ giữ `commitmentPolicyId`, còn chính sách đến từ catalog cấu hình và được băm vào
`policyConfigurationHash` — nhưng phải xác nhận, không được giả định.

#### T2.2 — Test: sáu tệp

Chạy lệnh baseline của `AGENTS.md` sau mỗi bước: `dotnet test RideBound.slnx`.

⚠️ Theo Codex (📎), `StrictBagItBundleTests` có một test trên kho thật **mặc định kỳ vọng
`GitDirty = true`**. Trên worktree sạch nó có thể đỏ. Nếu đỏ đúng test đó: chạy nó trên cây chính để xác
nhận là hiện tượng có sẵn, ghi lại, rồi tiếp tục. **Không** sửa test cho xanh.

| Tệp test | Ca bắt buộc |
|---|---|
| `tests/RideBound.Domain.Tests/Commitments/CommitmentLockEvaluatorTests.cs` | (a) `DropEtaDeadlineSlack = null` ⟹ không witness mới (hồi quy). (b) `candidate = anchor + slack` ⟹ **không** witness (ranh giới dùng `>`). (c) `candidate = anchor + slack + 1` ⟹ witness `("drop_eta_ms", "deadline_cap")`. (d) một chiều, `candidate = anchor − slack − 1` ⟹ **không** witness. (e) **Ca Định lý 4:** `candidate == exogenous` (no-op) nhưng cả hai `> anchor + slack` ⟹ **có** witness — chính no-op bị bắt. (f) Có hạn chót mà `anchor = null` ⟹ `ArgumentException`. (g) `anchor.RequestId` khác ⟹ `ArgumentException`. (h) hai chiều, `candidate = anchor − slack` ⟹ không witness. (i) hai chiều, `candidate = anchor − slack − 1` ⟹ witness `deadline_floor`. (j) hai chiều, `candidate = anchor + slack + 1` ⟹ **chỉ** `deadline_cap`. (k) **Ca Hệ quả 4.3:** hai chiều, no-op có `exogenous = anchor − slack − 1` ⟹ no-op bị bắt; cùng trạng thái, một chiều ⟹ không bị bắt. |
| `tests/RideBound.Domain.Tests/Commitments/CommitmentPolicyTests.cs` | Hàm dựng nhận hai tham số mới; mặc định `null` / `false`; `twoSided = true` mà thiếu slack ⟹ `ArgumentException`. |
| `tests/RideBound.Runner.Tests/Configuration/CommitmentPolicyConfigurationTests.cs` | `dropEtaDeadlineSlackMs: 30000` ⟹ `Duration(30000)`; vắng ⟹ `null`; `0` bị từ chối; số âm bị từ chối; `dropEtaDeadlineTwoSided: true` đọc được; giá trị không phải bool ⟹ `InvalidDataException`; `twoSided` mà thiếu slack ⟹ lỗi (cùng kiểu ngoại lệ mà tệp đang kỳ vọng cho `freezeHorizonLocks` thiếu `freezeHorizonMs`); khóa lạ vẫn bị từ chối. |
| `tests/RideBound.Algorithms.Tests/Policies/EffectivePolicyFairnessTests.cs` | Chính sách B1–B4 sau `MechanismCommitmentPolicyProvider` có `DropEtaDeadlineSlack == null` và `DropEtaDeadlineTwoSided == false` dù chính sách nguồn có hạn chót. |
| Tệp test của `CommitmentDecisionValidator` (tầng Application) | Chính sách có hạn chót, trạng thái mà `e > p_0 + slack` ⟹ no-op bị witness với `DeadlineExceeded` và thông điệp `"…beyond the initial-promise deadline."`; hai chiều, `e < p_0 − slack` ⟹ `DeadlineExceeded` với thông điệp `"…outside the initial-promise window."`. |
| `tests/RideBound.Algorithms.Tests/Oracle/ExactSmallCommitmentDifferentialTests.cs` (dùng lại `CreateState`, `MechanismContext` của tệp) | (a) **Đường K20:** no-op bị loại bởi luật cam kết, còn ít nhất một phương án ⟹ `Code == SafetyNoOpRejected`, `CandidateId` là id no-op, `UnderlyingCode` là mã của no-op, `GeneratedCandidateCount > RejectedCandidateCount`. (b) **Fail-closed có no-op:** mọi phương án bị loại ⟹ vẫn `VehicleHasNoFeasibleCandidate`, nhưng `CandidateId` là id no-op. (c) Hồi quy: hai test fail-closed hiện có (`C1_fails_closed_with_a_typed_witness_when_a_vehicle_loses_every_candidate`, dòng 584; `C1_fails_closed_when_a_vehicle_set_carries_no_candidate_at_all`, dòng 637) vẫn xanh. (d) **Không đổi ca thành công:** chạy lại các test differential hiện có của tệp, tập giữ lại không đổi. Nếu khó dựng trôi dạt trong fixture, dựng ca (a) bằng hạn chót hai chiều với `anchor` đặt lệch sớm so với `exogenous`. |

**Hoàn thành T2.2:** `dotnet test RideBound.slnx` xanh, trừ đúng test đã biết ở trên nếu có, đã xác nhận
là hiện tượng có sẵn.

#### T2.3 — Build runner mới

```powershell
cd E:\Code\RideBound-deadline
dotnet publish src\RideBound.Runner\RideBound.Runner.csproj -c Release `
  -o E:\RideBoundData\research\runner-deadline-v1
```

Đối chiếu danh sách tệp với runner tiền lệ `E:\RideBoundData\wp9\runner\h6-confirmatory-v1`: cùng bố
cục framework-dependent nhiều tệp, có `RideBound.Runner.dll`, cùng phiên bản .NET runtime. Gốc publish
phải **ổn định** — `runner_client.py:481-491` băm mọi tệp trong đó ở đầu và cuối mỗi lần chạy, lệch là
`RBWP7_RUNNER_ARTIFACT_DRIFT`.

#### T2.4 — Hai đối chứng đã biết kết quả. Bắt buộc trước mọi nhánh mới.

Theo kỷ luật của thí nghiệm ratchet (tài liệu bàn giao §7.5). Chạy trên runner mới:

| Đối chứng | Cấu hình | Phải tái lập **đúng từng ô** |
|---|---|---|
| `ctl-conduct-k0` | cấu hình hành vi của `dr-conduct-k0`, k = 0 | 20/20 hoàn tất; số khách được nhận từng ô trùng `wp14/drift-v1` |
| `ctl-visible-k0` | `ridebound-scratchpad/drift/basis-customer-visible.json`, k = 0 | 16/20 hoàn tất; **đúng** 4 ô vô nghiệm `{d20181116-s10-r2, d20181116-s10-r4, d20181117-s10-r1, d20181117-s10-r3}`, nhãn `commitment-*` |

Vì luật mới mặc định tắt và hai cấu hình này không có khóa mới, **quyết định** phải trùng hoàn toàn.
`semanticHash` có thể khác vì `binarySha256` đổi (bẫy 12.7) — so **quyết định** bằng
`ridebound-scratchpad/levelc/decision_identity.py` (chuỗi `(xe, ứng viên)` và tập lời hứa đã sắp xếp
trong từng khung). Ở 4 ô vô nghiệm, **văn bản** thông điệp có thể khác bản cũ vì thay đổi 6 đổi ứng viên
được trích; so **nhãn** và **tập ô**, không so chuỗi thông điệp. Nếu một ô trong 4 ô chuyển sang
`SafetyNoOpRejected` thay vì fail-closed, đó là thông tin mới về đường K20 ở k=0, không phải lệch — ghi lại.

**Lệch quyết định dù một ô: dừng, điều tra, không chạy nhánh mới.**

#### T2.5 — Cấu hình các nhánh

Đặt trong `ridebound-scratchpad/deadline/` (ngoài kho), theo tiền lệ `drift/basis-customer-visible.json`.

⚠️ `policyId` **phải giữ** `"wp6-synthetic-policy-overlay-v1"` — preflight hard-code id này ở
`actual_fleetpy_medium_preflight.py:189` và `:234`; `_require_declared_commitment_policy`
(`ridebound_fleetpy/session.py:103-126`) báo `RBWP7_COMMITMENT_POLICY_UNDECLARED` nếu không thấy. Panel
phát triển dùng đúng id này (K17), nên **cùng một bộ cấu hình** chạy được cả hai panel.

Nhánh hạn chót `dl-<l>`: sao chép `benchmarks/configurations/wp14-c1-h6-reference-v1.json`, rồi
- **bỏ** `hardLimit` của `drop_eta_total_ms` (cô lập đúng một cổng);
- giữ nguyên mọi thứ khác: ba chiều switch `hardLimit = 0`, `finalConfirmationLocks`,
  `materialRevisionRule`, `budgetBasis: "decisionInduced"`;
- thêm `"dropEtaDeadlineSlackMs": <l>` vào đối tượng chính sách.

Nhánh `dl2-<l>`: như `dl-<l>`, thêm `"dropEtaDeadlineTwoSided": true`.

| Nhánh | Cổng trên giờ trả | Họ (Định lý 4) | Vai trò |
|---|---|---|---|
| `conduct-30` | trần hành vi 30.000 ms | `C` | cơ chế của khóa luận; kiểm bất biến |
| `visible-30` | trần kết quả 30.000 ms | `V` | cơ sở `customerVisible` đã có |
| `dl-30`, `dl-60`, `dl-120` | hạn chót một chiều 30.000 / 60.000 / 120.000 ms | `M⁺` | đối thủ kiểu Schulz |
| `dl2-30` | hạn chót hai chiều 30.000 ms | `M` | **đầu dò** cho họ `M` (Hệ quả 4.3); gần "hộp tĩnh" của Sharif Azadeh 2022. **Không** khẳng định nhà vận hành dùng cửa sổ hai chiều cho giờ trả — đến sớm thường vô hại |

Mọi nhánh dùng **cùng** `--wp4-config` (`wp9-fleetpy-ridebound-hard-vector-audited-v1.json`), cùng bộ
sinh, cùng khóa, cùng hàm mục tiêu. Vì tầng `worst-hard-utilization-ppm` là hằng số và tầng `revision`
gần như luôn hòa, mọi nhánh **thực chất cùng xếp hạng "nhận khách → chi phí"** — hàm mục tiêu khớp nhau
đúng nguyên tắc A01 của Codex. **Không sửa khiếm khuyết ppm trong Tầng 2** (K12).

#### T2.6 — Chạy

**Đọc mốc giờ khung từ fixture.** `preflight_drift.py` hard-code `WINDOW_START_SECONDS = 28800` (dòng
73, dùng ở dòng 86 và 93), đúng cho khung sáng nhưng **sai cho `w17`** (mốc 61200). Tạo
`ridebound-scratchpad/deadline/preflight_drift_v2.py` là bản sao, chỉ khác:
- đọc mốc từ biến môi trường `RB_DRIFT_WINDOW_START_SECONDS`, **bắt buộc** (thiếu thì dừng), chỉ nhận
  `28800` hoặc `61200`;
- trình điều khiển đặt biến đó từ `sourceWindowStartSeconds` trong `<fixture>/normalizer-configuration.json`
  của ô đang chạy, và kiểm `drainDurationMs == 7200000` khớp `WINDOW_SECONDS = 7200`;
- kèm `check_preflight_v2.py`: với mốc 28800, lịch hệ số của v2 **trùng từng phần tử** với v1 cho cả 7
  ngày; với mốc 61200, phần tử đầu đúng 1,0 và thời điểm lệch đúng 61200 s. Không tốn lần chạy nào.

Không sửa `preflight_drift.py` gốc — các lần chạy cũ tham chiếu nó.

**Trình điều khiển:** `ridebound-scratchpad/deadline/run_deadline.py` theo khuôn `drift/run_drift_frac.py`:
- danh sách panel × nhánh × mức × ô; song song 6 luồng;
- bỏ qua ô đã có `summary.json` (`"reused"`);
- **báo và dừng** nếu gặp thư mục dở dang không có `summary.json` (bẫy 12.8: thư mục dở dang chặn lần
  chạy lại, phải xóa có chủ đích);
- đặt `RB_DRIFT_DAY` (từ tên ô, như `day_of()` ở `run_drift_frac.py:90-92`), `RB_DRIFT_EXPONENT`,
  `RB_DRIFT_WINDOW_START_SECONDS`;
- `PYTHONDONTWRITEBYTECODE=1`, `PYTHONIOENCODING=utf-8`;
- `--runner-root E:/RideBoundData/research/runner-deadline-v1`;
- fixture 2B: `benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1/<ô>/`, driver
  `benchmarks/scenarios/wp14-development/<ô>.driver.json` (§12.3);
- đầu ra dưới `E:/RideBoundData/research/deadline-v1/<job>` — `--output` dùng `mkdir(exist_ok=False)`,
  không bao giờ dùng lại thư mục.

**Thứ tự chạy — quan trọng cho tiền đăng ký:**

| Bước | Việc | Lần chạy |
|---|---|---:|
| 1 | T2.4 hai đối chứng | 40 |
| 2 | **Chạy thử một ô tối** `d20181112-s10-r1-w17`, nhánh `conduct-30`, k=1: kiểm hệ số áp đúng khung, không có lỗi `Board()` vì đến sớm (K22) | (1, tính trong 2B) |
| 3 | 2B nhánh `conduct-30`, 16 ô, k=1 | 16 |
| 4 | Dựng **dự đoán theo ô** cho cả 2A và 2B bằng `holdout_predict.py` (T2.8), niêm phong | 0 |
| 5 | 2A: `dl-30/60/120` × k∈{0,1} × 20 ô | 120 |
| 6 | 2B: `visible-30`, `dl-30`, `dl-120`, `dl2-30` (± `dl-60`) × 16 ô | 64 (80) |

Bước 3 phải xong **trước** bước 4 vì dự đoán 2B cần quỹ đạo gần dự phòng của chính các ô đó. Bước 4 phải
niêm phong **trước** bước 5–6. `conduct-30` và `visible-30` ở panel A, k0/k1, đã có trong `wp14/drift-v1`
⟹ dùng lại cho 2A.

**Tổng:** 40 + 16 + 120 + 64 = **240** lần chạy (256 nếu có `dl-60` ở 2B; +40 nếu thêm `dl2-30` ở 2A —
không cần, vì buổi sáng Hệ quả 4.3 đoán `dl2` ≈ `dl`).
**Thời gian:** ~11 phút/ô một luồng, 6 luồng; nhiều ô chết sớm ⟹ ước lượng **5–8 giờ** tính toán.
**Dung lượng:** ~19–67 MB/ô ⟹ **~5–15 GB** (xem cổng T2.0).
**Báo tiến độ mỗi giờ** khi job dài đang chạy (ràng buộc người dùng #5).

#### T2.7 — Phân loại lỗi theo hằng thông điệp trong mã

Nâng cấp `classify()` của `drift/run_drift_frac.py:101-107` (đang so chuỗi mơ hồ) thành so **đúng hằng
thông điệp trong mã nguồn**, kèm một test nhỏ trong scratchpad đọc lại các tệp nguồn để hỏng nếu hằng đổi.
Nhãn gồm hai phần: **đường hỏng** và **luật của no-op**.

| Nhãn | So khớp | Nguồn hằng |
|---|---|---|
| `commitment-all-rejected/deadline-late` | `"rejected every generated candidate"` + `"beyond the initial-promise deadline"` | `HardVectorCandidateAssessor.cs:205` + T2.1(4) |
| `commitment-all-rejected/budget` | `"rejected every generated candidate"` + thông điệp ngân sách | `HardVectorCandidateAssessor.cs:205` |
| `commitment-noop-rejected/deadline-window` | `"rejected the safety no-op while other candidates survived"` + `"outside the initial-promise window"` | T2.1(6) + T2.1(4) |
| `commitment-noop-rejected/budget` | `"rejected the safety no-op while other candidates survived"` + thông điệp ngân sách | T2.1(6) |
| `commitment-*/other` | hai tiền tố trên, lý do không khớp | — **đọc tay** |
| `noop-state-apply` | `"rejected every generated candidate"`, lý do **không** phải `COMMITMENT_*` (no-op hỏng khi áp trạng thái) | T2.1(6) |
| `generation-noop` | `"could not be retained as the safety no-op candidate"` | `InsertionCandidateGenerator.cs:212-228` |
| `window-wall` | `"Actual pickup time must remain inside the accepted pickup window."` | `RideRequest.cs:271` |
| `selection-noop-invariant` | `"exactly one no-op option"` | `CandidateSelectionModel.cs:279` — **sau thay đổi 6 không được xuất hiện**; xuất hiện ⟹ lỗi cài đặt, dừng |
| `other` | còn lại — **mở `failure-00.json` đọc tay từng ca** | — |

Biến nhị phân dùng trong phân tích: **"vô nghiệm do cam kết"** = nhãn bắt đầu bằng `commitment-`.
Bẫy 12.4: **không bao giờ** đếm lỗi thay cho phân loại lỗi.

#### T2.8 — Tiền đăng ký: viết và niêm phong **trước bước 5 của T2.6**

Tạo `ridebound-scratchpad/deadline/PREREGISTRATION.md` và `predictions.csv`; ghi SHA-256 của cả hai và
thời điểm UTC vào `PREREGISTRATION.sha256`. Bước 1–3 của T2.6 được chạy trước vì chúng **không** chứa kết
cục nào của các nhánh được dự đoán.

**Quy tắc dự đoán theo ô — một script, dùng cho cả 2A và 2B.** `holdout_predict.py` (mở rộng
`cellpred.py` + `retrodict.py`) đọc quỹ đạo `conduct-30` k=1 của từng ô (panel A: `wp14/drift-v1`; panel
phát triển: bước 3), và cho mỗi khách tính trên chuỗi ETA trả đã công bố:
- `M⁺_r = max_t (p_t − p_0)⁺`, `M_r = max_t |p_t − p_0|`, `V_r = Σ_t |p_t − p_{t−1}|` — **cực đại chạy**,
  không dùng `D⁺` cuối, vì khung tối không đơn điệu (K18);
- thời điểm đầu tiên mỗi đại lượng vượt `l ∈ {30, 60, 120}` s.

Với mỗi (ô, nhánh), gọi `τ` là thời điểm vượt sớm nhất của đại lượng tương ứng (`dl` → `M⁺`, `dl2` →
`M`, `visible` → `V`), và `T` là thời điểm chết của `conduct-30` ở ô đó (∞ nếu hoàn tất):
- `τ < T` ⟹ dự đoán **vô nghiệm do cam kết**;
- không có `τ` và ô hoàn tất ⟹ dự đoán **không vô nghiệm do cam kết**;
- không có `τ` trước `T` và ô chết ⟹ dự đoán **`window-wall`** (hạn chót không kịp cắn trước khi xe đón
  muộn), ghi riêng là *dự đoán yếu*.

Đây là dự đoán **xấp xỉ**: quỹ đạo nhánh hạn chót tách khỏi quỹ đạo `conduct-30` sau lần cắt đầu tiên.
Điều kiện hợp lệ như kiểm hồi tố (§5.2): quỹ đạo tham chiếu gần dự phòng — ghi `C` từng ô; ô có `C > 60 s`
gắn cờ *"xa dự phòng"*.

**Nội dung tiền đăng ký:**
1. **Kiểm tra bất biến (tất định):** `conduct-30` có **đúng 0** ô nhãn `commitment-*` ở mọi panel, mọi
   `k`. Đây là Định lý 4(a); sai thì có lỗi cài đặt, không phải phát hiện khoa học. `selection-noop-invariant`
   xuất hiện ở bất kỳ nhánh nào ⟹ lỗi cài đặt.
2. **Dự đoán chính — theo ô, trên đủ mọi ô** (20 ô 2A × 3 nhánh × 2 mức; 16 ô 2B × 4–5 nhánh): toàn bộ
   `predictions.csv`. **Không** giới hạn ở 9 ô sống sót (K21).
3. **Dự đoán hướng cho 2B, từ Hệ quả 4.3** (viết trước khi chạy `holdout_predict.py`, nên không phụ
   thuộc số liệu của bước 3):

   | Khung | `conduct-30` | `dl-30` | `dl-120` | `dl2-30` | `visible-30` |
   |---|---:|---:|---:|---:|---:|
   | sáng `w08` (8 ô) | 0/8 | **đa số** (≥ 4/8) | ≤ 1/8 | ≥ `dl-30` từng ô | đa số |
   | tối `w17` (8 ô) | 0/8 | **≤ 1/8** | 0/8 | **đa số** (≥ 4/8) | **đa số** (≥ 4/8) |

   Số đếm là số ô **vô nghiệm do cam kết**. Ngày 12, 13/11 sáng tăng ít hơn panel A (×1,14–1,15 so với
   ×1,17–1,26), nên ngưỡng buổi sáng đặt thấp hơn 2A.
4. **Ngưỡng xác nhận.** 2B được gọi *"xác nhận trên tập giữ lại"* khi **cả hai**: (i) dự đoán theo ô đúng
   ở ≥ 90% cặp (ô, nhánh) xác định được, **tính riêng cho khung tối**; (ii) hàng `w17` của bảng hướng
   đúng. 2A được gọi *"xác nhận cơ chế có đối chứng"* khi (i) đúng trên panel A và `dl-30` k=1 vô nghiệm
   do cam kết ở đa số ô.
5. **Điều kiện phủ định**, ghi kết quả âm như kết quả dương:
   - dự đoán theo ô đúng < 75% ở khung tối ⟹ phương pháp dự đoán không chuyển được sang dữ liệu mới;
   - `dl-30` tối vô nghiệm do **`deadline-late`** ở ≥ 3/8 ô ⟹ Hệ quả 4.3 không có răng trên khung tối này;
   - `dl2-30` **và** `visible-30` tối cùng ≤ 2/8 ⟹ trôi thuận lợi của khung tối quá nhỏ để phân biệt các họ.
6. **Luật diễn giải khi hai loại dự đoán mâu thuẫn.** Nếu dự đoán theo ô đúng nhưng bảng hướng sai (ví dụ
   đoạn nhích 15–30 phút đầu khung tối làm `M⁺` vượt 30 s ở nhiều ô), kết luận là *"Định lý 4 đúng theo
   ô, nhưng khung tối thật không đủ thuận lợi để hạn chót một chiều an toàn"* — **không** được gọi là xác
   nhận Hệ quả 4.3.
7. **Phụ, thăm dò — không vào ngưỡng xác nhận:** buổi tối `dl-30` nhận **nhiều khách hơn** `conduct-30` ở
   đa số ô hoàn tất cả hai (nhà điều hành tiêu trôi thuận lợi, Hệ quả 4.3).

#### T2.9 — Phân tích

**Bằng chứng chính: bảng dự đoán – kết cục** theo (panel, khung, nhánh, ô): dự đoán, nhãn kết cục, đúng/sai,
cờ *"xa dự phòng"*, cờ *"dự đoán yếu"*. Liệt kê **từng** ca sai kèm lý do đọc từ artefact. Không gộp trước
khi in bảng đầy đủ.

**Bằng chứng thứ hai: trần khả thi nhỏ nhất theo ô.** Ở 2A, với mỗi ô, `l` nhỏ nhất trong {30, 60, 120} mà
`dl-l` không vô nghiệm do cam kết; đặt cạnh `max_r M⁺_r` dự đoán. Ở 2B chỉ có {30, 120} (thêm 60 nếu chạy
`dl-60`).

**Bảng đếm:** nhánh × khung × `k` × {`hoàn tất`, `commitment-all-rejected/*`, `commitment-noop-rejected/*`,
`noop-state-apply`, `generation-noop`, `window-wall`, `other`}.

**McNemar chính xác — chỉ mô tả phụ.** Ghép cặp theo ô, `dl-30` so với `conduct-30`, biến "vô nghiệm do
cam kết". Nếu 9/9 ô bất đồng một chiều thì `p = 2 × 0,5⁹ ≈ 0,0039`. Nhưng kết cục gần như **tất định theo
ô** khi đã cố định trôi dạt, nên giá trị p không thêm gì ngoài số đếm — không được dùng làm bằng chứng
chính. Đơn vị là **ô**, không phải khách (K7).

Ô chết vì `window-wall` dưới nhánh hạn chót **trước khi** vướng hạn chót được xếp là "không vô nghiệm do
cam kết" — cách xếp **bảo thủ, chống lại** giả thuyết.

**Phép so phụ:** trên các ô hai nhánh cùng hoàn tất — số khách được nhận, `C`, `V`, `M⁺` theo khách; và dự
đoán phụ số 7.

**Hình trung tâm:** hai bảng cạnh nhau, **sáng** và **tối**. Trục ngang là bốn họ `C, M⁺, M, V` ở trần
30 s; trục dọc là tỉ lệ ô vô nghiệm do cam kết; chấm là dự đoán, cột là kết cục. Buổi sáng ba họ sau cùng
cao; buổi tối `M⁺` tụt xuống còn `M, V` giữ cao; `C` bằng 0 ở cả hai. Đây là Định lý 4 và Hệ quả 4.3 thành
hình. Hình phụ cho 2A: tỉ lệ vô nghiệm theo trần `l` của `dl`.

#### T2.10 — Kết quả dự tính và cách viết

Nếu 2A đạt ngưỡng, câu cho Chương 4:

> *Dưới trôi dạt đo thật của đỉnh sáng Manhattan, một hạn chót 30 giây tính từ lời hứa đầu — đúng kiểu
> cơ chế của Schulz & Pfeiffer (2026) — vô nghiệm do cam kết ở X/20 ô, vì chính phương án giữ nguyên tuyến
> đã vượt hạn chót. Muốn khả thi trên mọi ô, hạn chót phải nới tới Y giây. Trần hành vi 30 giây không làm
> vô nghiệm ô nào do cam kết, đúng như Định lý 4 dự đoán; nhánh này vẫn hỏng ở Z/20 ô, nhưng vì bất biến
> cửa sổ đón, không phải vì cam kết. Dự đoán theo từng ô, niêm phong trước khi chạy, đúng ở W% số cặp.*

Nếu 2B đạt ngưỡng, thêm:

> *Trên tập giữ lại chưa từng dùng để dựng phương pháp (ngày 12–13/11), dự đoán theo ô đúng ở W′%. Vào
> buổi tối, khi tắc đường giảm, hạn chót một chiều vô nghiệm ở chỉ U/8 ô, trong khi hạn chót hai chiều và
> cổng kết quả vô nghiệm ở P/8 và Q/8 ô — đúng chiều mà Định lý 4 dự đoán cho từng họ.*

Nếu 2B không đạt, viết đúng như luật diễn giải số 6 hoặc điều kiện phủ định tương ứng, và hạ claim ở §5.6
về mức *"xác nhận cơ chế có đối chứng"*.

**Không** viết *"cơ chế của chúng tôi tốt hơn của Schulz"*. Viết: *"hai cơ chế ràng buộc hai đại lượng
khác nhau; dưới trôi dạt, chỉ đại lượng hành vi không bao giờ là nguyên nhân làm rỗng tập phương án."* Nói
rõ trần hạn chót và trần hành vi **không cùng ý nghĩa** dù cùng đơn vị giây — so bằng đường cong theo trần,
không so ở "cùng β". Và nói rõ cái giá: buổi tối hạn chót một chiều có thể phục vụ nhiều khách hơn trần
hành vi, vì nó được tiêu phần trôi thuận lợi.

---

