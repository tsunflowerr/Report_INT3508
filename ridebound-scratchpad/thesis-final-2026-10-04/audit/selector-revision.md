# Kiểm toán bổ sung bộ chọn đội xe

Ngày: 2026-10-05. Chỉ sửa source/noi-dung/07-chuong3.tex và tệp này. Không sửa
báo cáo phản biện, gói niêm phong, mã nghiên cứu, bộ thực thi, cấu hình hoặc kết quả.
Không chạy thí nghiệm hoặc xây lại bộ thực thi.

## Hướng dẫn và thuật ngữ

Đã đọc nature-writing/SKILL.md, manifest, các lớp lõi bắt buộc và các mảnh
manuscript, algorithmic, method, en, generic tại
E:/Code/Report_INT3508/ridebound-scratchpad/nature-skills-audit-2026-10-04/skills.
Đây là bổ sung phương pháp trong khóa luận tiếng Việt, không phải thư phản biện
hay hồ sơ nộp Nature. Mảnh en chỉ cung cấp kỷ luật câu/đoạn; giữ tiếng Việt theo yêu cầu.

| Dạng cố định | Nghĩa |
|---|---|
| mốc chiếu giữ tuyến | Mốc e; mã exogenous; chiếu lại tuyến đang giữ trên trạng thái sau sự kiện. |
| cơ sở thông báo nhìn thấy | CommitmentBudgetBasis.CustomerVisible, cộng abs(p-v); không đồng nhất với trải nghiệm hay hài lòng thực tế. |
| cơ sở hành vi | CommitmentBudgetBasis.DecisionInduced, cộng đối xứng abs(p-e). |
| bộ thực thi / bộ chuyển đổi | Thuật ngữ văn xuôi cho runner / adapter; giữ định danh mã và project. |
| mức dùng ngân sách lớn nhất | Ký hiệu mathcal U; tránh trùng nhãn nhánh U của T38. |

Đã đọc hướng dẫn repo: docs/00-index.md, docs/01-research-charter.md, trạng thái
hiện hành trong docs/18-status-and-decision-log.md, phần WP14R của
docs/16-roadmap-and-work-packages.md và docs/08-algorithms-baselines-and-solver.md.
Không đổi trạng thái, hợp đồng, baseline hoặc next action của repo RideBound.

## Căn cứ mã nguồn hiện tại

Nguồn: C:/Code/RideBound-noworse, HEAD
24aa747147d49db79675d170829e6f3bf3afc3cc. Không dùng HEAD này làm định danh mọi đợt chạy.
Các cây fixture chưa theo dõi của người dùng giữ nguyên.

| Tệp dưới nguồn C# và con trỏ | Điều xác nhận trực tiếp |
|---|---|
| src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271 | Hard treatment được bật nếu có assessment chứa finite hard limit áp dụng. Nếu không, C1 không thêm utilization/revision. |
| Cùng tệp, 277–304 | Khi có forced candidate C1/C2, forced-reference-count (Minimize/Sum) đứng trước accepted-request-count (Maximize/Sum). Đếm phương án xe, không đếm khách/cổng. |
| Cùng tệp, 307–360 | B2: material count rồi vector decision-induced. C1: worst utilization rồi vector. C2: worst utilization, warning-excess vector, decision-induced vector; cảnh báo tắt thì C1. |
| Cùng tệp, 365–386 | Cost là Minimize/Sum; xe theo VehicleId Ordinal có một tầng hạng CandidateId Ordinal riêng, bắt đầu từ 0. Không gom mọi hạng xe thành một tổng phá hòa duy nhất. |
| Cùng tệp, 489–520 | Vector cộng theo ứng viên; mỗi chiều CommitmentDimensionVocabulary.Ordered là một tầng Sum riêng. B2 vẫn có material count trong vector sau tầng material riêng. |
| src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:512 | Revision cộng publication.Entry.Deltas.DecisionInduced, kể cả khi ledger dùng CustomerVisible. |
| Cùng tệp, 537–635 | Utilization xét khách active có lời hứa/ledger, theo pha và từng finite hard limit; dùng history.Current.BudgetAfter, không dùng delta chia ngân sách còn lại. |
| Cùng tệp, 612–664 | Trần 0, usage 0 được đặt 1.000.000 PPM; trần dương chia UInt128 và làm tròn lên. Chuẩn hóa không quyết định khả thi. |
| Cùng tệp, 474–485, 591–608 | Giữ tuyến forced bỏ utilization toàn xe. No-worse chỉ bỏ chiều vượt trần của khách được exemption; chiều còn trong trần vẫn xếp hạng. Hard limit vẫn tính là có. |
| Cùng tệp, 719–761 | Warning excess là tổng max(0, BudgetAfter-warningLimit) theo chiều; warning phải có finite hard limit và không vượt hard limit. |
| src/RideBound.Domain/Commitments/CommitmentDimension.cs:19 | Đủ 10 chiều theo thứ tự: pickup ETA, drop ETA, material count, vehicle switch, pickup relocation, pickup switch, drop relocation, drop switch, incumbent inversion, pre-pickup insertions. |
| src/RideBound.Application/Scheduling/RouteScheduleProjector.cs:62 | Bắt đầu tại evaluation time; node hoặc phần còn lại của edge hiện tại. |
| Cùng tệp, 83–88, 123–143, 163–165 | Phần edge làm tròn lên; cộng travel, chờ earliest pickup, stop service. Cost là thời gian cuối phép chiếu trừ evaluation time; không phải distance, tiền hay marginal cost. Tuyến không còn điểm dừng vẫn có phần edge còn lại nếu đang trên edge. |
| src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:259 | Generate → assessment/filter/profile → selector → full-fleet validator. B3/B4 dùng RollingCost profile; B5 ngoài mapper này. |
| Cùng tệp, 325–351, 370–385 | C1/C2 require safety no-op, truyền recovery flags tới assessor; nghiệm qua full-fleet validation. |
| src/RideBound.Application/Optimization/CandidateSelectionExecution.cs:255 | Primary qua injected validator; fallback no-op (277–299), single-request (302–322); Unknown khi không chứng minh được lựa chọn hoặc hết validation budget (324–365). |
| Cùng tệp, 409–451 | Single-request portfolio sắp theo lexicographic objective rồi option IDs; executor không tự dựng incident. |
| src/RideBound.Solvers.OrTools/OrToolsCandidateSelectionSolver.cs:339 | Exactly-one/vehicle (351), at-most-one/request (360), Sum (382), Maximum (397); equality khóa tầng trước (406–408). |
| Cùng tệp, 253–295 | Feasible chưa proven trả ngay, không giải tầng sau, không báo Optimal. Fixed-bound thêm trước nhánh Feasible không được sử dụng cho một lượt tiếp theo. |
| src/RideBound.Runner/Protocol/RunnerSession.cs:957 | Runner kiểm lại commitment; stage tại 1036; ACK áp trạng thái tại 604. |

Con trỏ là dòng của nguồn được đọc trong audit. Giữ nguyên các điều kiện (B), (N),
(H), giả thiết chuỗi công bố liên tục, phản ví dụ và phân biệt quỹ đạo dự phòng/thật.
Mô tả cost nêu cả stop-service theo hàm tổng quát và việc các lượt so đặt dwell bằng
không. Vì vẫn gồm chờ, cost không đồng nhất với vehicle travel time.
InsertionCandidateGenerator.cs:525 và :531 đặt ServiceDuration bằng new Duration(0)
cho điểm đón/trả được sinh.

## Phiên bản lịch sử và cấu hình niêm phong

### H6

Receipt: E:/Code/RideBound/benchmarks/scenarios/wp9-confirmatory/freeze-receipt-v5.json.
Đã tính lại SHA-256: 84f6eff31addbdd12349a19201d79c872fbd05aaf5e0aa45dd73aee6d5c3dee2.
Không thay bằng v6 hoặc receipt trước đó.

Receipt ghi DLL 8445f05399dcdab8826db7d70a4f0e4c1468433f43b3f072f03ca480a6bb93b3,
tree 81c021ddb5dd9a27ae1f6c79dc3b31f28b4883598dcf998c1aaed6588bc77b5d.
Đã tính DLL tại E:/RideBoundData/wp9/runner/h6-confirmatory-v1/RideBound.Runner.dll
và khớp. WP8-011c repin 4c297a2c...bd2a8 là mốc trước đó, không phải DLL H6 cuối.
Tree seal đọc từ receipt, không tuyên bố audit này tính lại toàn tree.

Đã đọc source lịch sử bằng git show d48b115:src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs.
Không có forced-reference-count; C1 có accepted → worst utilization → 10-vector →
cost → từng hạng xe. Diff ở commit 38d517d sau H6 chỉ thêm returned Problem để ghi
portfolio, không đổi hierarchy; commit 8d1ea4d mới thêm forced tier. Không suy định
danh DLL từ một commit source riêng.

Đã đọc wp9-fleetpy-rolling-cost-audited-v1.json và
wp9-fleetpy-ridebound-hard-vector-audited-v1.json trong benchmarks/configurations:
B1/C1 dùng cùng candidate limits/strategy, solver version/seed, không khai báo
commitmentRecovery. Mã mapper và frame thực thi xác nhận hierarchy; không chỉ suy từ tên.

### Tầng 2

deadline/PREREGISTRATION.md dưới scratchpad ghim runner-deadline-v1, tree
8fa5dd288b0ae603dc2c044825f8089116f59953c768442eabfb5d8ca261cda8.
deadline/run_deadline.py:45 và :47 truyền runner riêng và WP9 hard-vector WP4 config.
Commitment configs nằm trong deadline/configs/.
Source lịch sử git show 41a4e11:.../SolverBackedFleetSelection.cs có HardVector và
không forced tier. Kế hoạch ghi source 41a4e11 cộng diff chưa commit; không giả vờ
commit đó là toàn build niêm phong. Frame nhánh C dưới đây xác nhận hierarchy đã chạy.

### T38

tang3/t38/T38-PLAN.md mục 2; tang3/t38/run_t38.py:46, :90, :93 và
tang3/w07/run_w07.py:40 ghim C:/RideBoundData/research/runner-tier3-v2, tree
ac251ef32a4865ea3bd3d8d87b4b1bcaccc4462a9b80160b4d205b8d474cff3f,
WP4 66e9b59249d9491d520f3ed592e8c878a0d3b100e39432d5f4b73321617b4518.
WP4 khai báo ridebound-hard-vector, commitmentRecovery=no-worse-than-reference-v1,
lateBoarding=record-v1. Đã tính lại băm WP4 và đủ 5 commitment configs, khớp pin script:

| Config | SHA-256 |
|---|---|
| U | 998a0a94e7865c3b6e890f1bed9bf27f7f6c9e0de1f73d02a349ddc3de91c273 |
| C-30 | d6124f3f964d8385db381d53b75c142cf2ac870b22823d6675325c3808808beb |
| Mplus-30 | cc7d7838836137f432dc025b7c45aa19c10bb82010663a9fb6f1dc52ec7c8f7d |
| Mplus-60 | f8d4c74913224cdfcf13f4a1e8ebffe3e87850fd507e542c8ba333ee5d1f22cc |
| V-30 | 2462484ab8d7e61efc36de8dc1cd00054dd258e9ec0276f734e9a01212f005d5 |

U giữ trần 0 của vehicle/pickup/drop switches và final-confirmation locks; bỏ
trần thời gian không biến nó thành B1. V dùng CustomerVisible cho ledger nhưng
mapper vẫn xếp hạng vector DecisionInduced.
DLL T38 tính băm a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac.
Tree seal đọc từ pin kế hoạch/script; không tuyên bố tính lại toàn tree hoặc xây lại DLL.

### Khung trao đổi gốc

Đọc NDJSON, giải base64, tính SHA-256 chính frame trích. Cả năm frame khớp
frameSha256. Đây là kiểm hierarchy tại con trỏ cụ thể, không phải thống kê mới
hay rà toàn bộ quyết định.

| Thư mục chứa transcript-00.ndjson | Ordinal | Điều thấy |
|---|---:|---|
| E:/RideBoundData/wp9/confirmatory-h6-panela-v2/p-d20181114-s10-r1-b1-tight-s7 | 6 | Accepted → cost → 8 hạng xe. |
| Cùng root, p-d20181114-s10-r1-c1-tight-s7 | 12 | Accepted → utilization 1.000.000 → 10 revision → cost → 8 hạng xe; không forced. |
| E:/RideBoundData/research/deadline-v1/conduct-30-k1-d20181114-s10-r1-s7 | 12 | C1 hierarchy đủ 10 chiều, utilization 1.000.000. |
| C:/RideBoundData/research/tier3-t38-v1/U-d20181114-s10-r3-w07 | 12 | U vẫn có C1 hierarchy, utilization 1.000.000. |
| Cùng root, Mplus-30-d20181114-s10-r3-w07 | 147 | Forced count 1 → accepted → utilization → 10 revision → cost → 8 hạng xe. |

C1/U có thể tạm vắng utilization/revision khi chưa có hard limit áp dụng trong
assessments. Không lấy frame đầu để kết luận chúng dùng B1 suốt lần chạy.

## Thay đổi và kiểm tra

- Định nghĩa ba mốc dùng tên tiếng Việt làm chính, giữ previous/exogenous/proposed.
- Dùng cơ sở thông báo nhìn thấy, giữ CustomerVisible, công thức, label và giả thiết.
- Thêm mục muc:bochon: hai ràng buộc nhị phân, giả mã sáu bước và ACK, thứ tự mục
  tiêu, Sum/Maximum, đủ vector, quy ước trần 0, cost, phá hòa, B2/C2, forced tier và
  lịch sử H6/Tầng 2/T38.
- Không thêm ví dụ ranking, số liệu hiệu quả hay thực nghiệm mới. Frame chỉ làm căn cứ audit.

Không thay code nên không chạy lại dotnet test RideBound.slnx; baseline repo không
đổi. Biên dịch và kiểm phân trang PDF thuộc bước đóng gói chung.

Kiểm tĩnh sau sửa: 0 tham chiếu Chương 3 không có label trong cây source;
muc:bochon xuất hiện đúng một lần; môi trường LaTeX cân bằng; dấu ngoặc nhọn cân
bằng và không âm ở tiền tố; UTF-8 không BOM, LF; không ký tự thay thế hoặc chuỗi
chuyển mã hỏng đã kiểm. Nguồn Chương 3 có 7.650 đơn vị tách bằng khoảng trắng;
không diễn giải số này là đếm từ ngôn ngữ học hoặc số trang.
