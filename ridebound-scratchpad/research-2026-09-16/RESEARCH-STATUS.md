# RideBound: khảo sát và kiểm tra độc lập — 2026-09-16

Trạng thái: đang thực hiện; chưa kết luận có thuật toán mới hoặc cải thiện closed-loop. Đây là ghi chép bên ngoài repository RideBound, không thay thế `docs/18-status-and-decision-log.md`. Không sửa baseline, source, cấu hình hay kết quả cũ. Hai thay đổi có sẵn trong `docs/benchmarking/` được giữ nguyên.

## Kết quả có thể kiểm tra lại

`audit_existing_evidence.py` đọc transcript của 80 run có sẵn; `evidence-audit.json` lưu nguồn, SHA-256 và counterexample. `audit_portfolio_choices.py` đọc portfolio panel A của 40 run E1; `portfolio-choice-audit.json` lưu nguồn/hash và kết quả từng run. Đây là phân tích dữ liệu đã ghi, không phải implementation khác của RideBound và không phải thí nghiệm thuật toán mới.

### 1. Cần sửa cơ sở toán học trong bản bàn giao

Với một tọa độ ETA: `A=|p-e|`, `d=|e-v|`, `B=|p-v|`. Tổng quát chỉ có `|A-d| ≤ B ≤ A+d`. Đẳng thức `B=A+d` cần hai biến thiên cùng chiều. Ví dụ `v=100,e=110,p=105` cho `A=5,d=10,B=5`; `p=100` cho `A=10,B=0`. Trường hợp điều hành làm ETA sớm hơn vẫn bị tính bằng trị tuyệt đối trong `PromiseDeltaCalculator.cs`.

Trong 20 run H6 B1: tổng `A=74,443,002 ms`, `d=9,202,610 ms`, `B=83,587,440 ms`: chênh `A+d-B=58,172 ms`; 255 tọa độ publication có `B<A`. H6 C1: `128,020`, `9,204,481`, `9,332,101 ms`: chênh 400 ms; ba tọa độ có `B<A`. Vì vậy, ngay trong dữ liệu này đẳng thức không đúng tuyệt đối. Con số gần bằng sau làm tròn không phải chứng minh định lý. Các ví dụ nguyên bản được lưu trong JSON.

Hai tập `|p-e|≤β` và `|p-v|≤β` nói chung không bao hàm nhau khi `e≠v`; với các ledger khác lịch sử, càng không được mặc định so tập theo cùng ngân sách còn lại. Kể cả có bao hàm tại cùng một state, cũng không suy ra thứ tự tổng số khách cuối ngày của hai policy closed-loop. Tài liệu `docs/04-problem-model-and-notation.md` đã cảnh báo về phép cộng delta và giới hạn của suy luận cùng state.

No-op `p=e` tiêu 0 conduct budget trong điều kiện ledger trước đó hợp lệ. Đó là chứng minh riêng cho budget gate, không bảo đảm mọi điều kiện vật lý/execution. Một no-op trượt visible gate cũng chưa chứng minh mọi phương án phục hồi đều bất khả thi. Nới thành soft gate không tự làm mất sự tồn tại của no-op.

### 2. Có không gian để thay đổi selection

Đếm tất cả vehicle-epoch tạo cảm giác ~96% chỉ có no-op, nhưng phần lớn epoch không có request mới. H6 B1 có 2,142 epoch có pending, trong đó 1,723 có ít nhất một xe có nhiều physical candidate; C1 có 2,143 và 1,713. Đây mới chỉ là trước hard gate.

Đếm chính xác trên **eligible portfolio** E1 panel A: chọn đúng một candidate/xe, không nhận trùng request, duyệt toàn bộ tích Descartes và đối chiếu optimum acceptance với lựa chọn đã ghi. Tất cả 4,285 epoch có pending đều được duyệt; không epoch nào vượt ngưỡng 200,000 tổ hợp; tất cả optimum acceptance khớp.

| Arm | Epoch có pending | Epoch nhận ≥1 request | Epoch có ≥2 fleet assignment cùng acceptance tối đa |
|---|---:|---:|---:|
| B1 | 2,142 | 1,723 | 1,309 |
| C1 tight | 2,143 | 1,571 | 1,045 |

Như vậy C1 có lựa chọn khác ở 1,045/1,571 ≈66.5% epoch đang nhận được khách; chưa biết lựa chọn khác có giúp các epoch tương lai hay không. Không được diễn giải thành khả năng tăng thêm 1,045 khách. Kiểm tra tiếp bằng tuple `(vehicleId, newRequestIds, route, schedule)` sau khi bỏ candidate ID vẫn giữ nguyên 1,309/1,045 epoch có khác biệt. Đây là khác biệt nội dung route/schedule được ghi, chưa chứng minh khác biệt về giá trị tương lai. Tích Descartes lớn nhất là 336 tổ hợp cho B1 và 256 cho C1.

### 3. Objective utilization đang bão hòa

Trong `HardVectorCandidateAssessor.CalculateWorstUtilization`, một hard limit bằng 0 với usage bằng 0 đóng góp 1,000,000 ppm. Vì thế, một chiều khóa tuyệt đối có thể làm max utilization bằng 1,000,000 cho mọi candidate hợp lệ, che toàn bộ các chiều có ngân sách dương. Đây là semantics hiện có, không phải khẳng định regression mới.

Portfolio C1: ở cả 2,123 epoch có objective này, giá trị max trên fleet là hằng số giữa mọi assignment tối đa hóa acceptance; không có epoch nào objective này phân biệt được chúng. Dữ liệu không hỗ trợ giải thích rằng C1 đã dùng hiệu quả continuous reserve nên C2 warning không còn tác dụng.

Thứ tự objective phải lấy từ `levelIndex` của từng epoch. Khi có commitment active: acceptance → worst utilization → các revision dimension (C2 còn warning excess) → operational cost → ID. Không ghép thứ tự từ tên objective xuất hiện lần đầu: các epoch khởi động chưa có commitment có stack khác.

Sửa cách chuẩn hóa để loại chiều hard-zero khỏi ranking dương là ablation cần có, nhưng riêng thay đổi score này chưa phải đóng góp thuật toán đủ mạnh cho khóa luận.

Tài liệu thiết kế `docs/07-commitment-ledger-and-certificates.md` §6 định nghĩa usage0/limit0 thành0, trong khi implementation đang cho1,000,000ppm. Đây là chênh giữa mô tả và semantics code đã có; chưa thay code hay gọi là regression.

`docs/18-status-and-decision-log.md` phần RB-WP4-008 (line938–953) ghi rõ lựa chọn1,000,000ppm và có zero-limit test. Vì vậy đây là quyết định implementation có chủ ý, không phải lỗi phát sinh ngẫu nhiên; thay ranking chỉ là ablation nghiên cứu cần kiểm chứng.

### 4. Kiểm tra actual state làm yếu giả thuyết future coverage

`state-replay` dùng đúng Runner E1, khớp98 response canonical byte-exact rồi lưu20 pending state. `state-probe` đối chiếu eligible candidate ID khớp cả20 state và đánh giá69 accepting fleet assignments qua core/validator gốc. Với tối đa12 OD/service types từ lịch sử trước decision, union coverage chỉ phân biệt1/16 epoch có lựa chọn và mẫu; C1 đã chọn score tốt nhất tại đó. Matching trên mọi cặp mẫu phân biệt3 epoch nhưng C1 cũng đã tối ưu score cả3. Chưa thấy state nào cải thiện score so với C1, chưa có bằng chứng closed-loop. Xem `IDEA-FALSIFICATION.md`, receipt và hai JSON analysis để biết giới hạn cùng physical time, mẫu lịch sử nhỏ và điều kiện matching mỗi xe một future request.

## Va chạm văn liệu và ứng viên còn lại

### Cập nhật 2026-09-18: hai phép thử âm và đối chiếu trực tiếp mới

Repair một cặp waiting incumbent, giữ nguyên hợp đồng và toàn bộ leading same-node block, không tạo accepting opportunity mới ở20 pending state đầu. Mở rộng sang **đủ16 rejected state của một run C1tight**, original E1 Runner khớp750response; mọi16state vẫn không có rescue. Capture/probe hashes và kiểm tra coverage ở `repair-probe-analysis.json`; giới hạn ở `IDEA-FALSIFICATION.md`. Không gọi đây là chứng minh không thể sửa tuyến nói chung.

Audit tiếp theo đã duyệt đủ mọi hoán vị incumbent suffix (thực tế≤4stop) và pending pickup/drop positions:4153route,9physical-pass,0full-contract acceptances, kể cả khi bỏ conservative head screen. Mọi physical-pass vẫn có incumbent order cũ. Cả7budget-witness cóusage trước=0 và lần chèn gây trễ thêm71.785–258.426s, lớn hơn30s;2lock-witness đều là tăng pickupETA. `all-order-probe-analysis.json` khóa phạm vi này. Lợi ích từ larger immediate route-order search/tiết kiệm budget quá khứ chưa được hỗ trợ; thay quyết định trước đó hoặc contract là phạm vi khác.

Đã đọc thêm toàn văn HTML anticipatory routing2022 và toàn văn PDF shareability shadows2026 (Elmi et al., DOI10.1016/j.trc.2026.105897). Bài2026 là đối thủ trực tiếp đáng kể: lựa chọn nhóm khách được zero-update guarantee bằng score đã có; ở rejection gần29%, fraction bị đổi delay giảm63.17→15.39% nhưng conditional magnitude tăng0.84→3.74min, conditional update count1.05→1.80. Tác giả tự nêu equity/magnitude/repeated changes là future work. `SHAREABILITY-SHADOWS-18-NOTES.md` ghi rõ model, formula approximation, denominator và những điều chưa xác minh. Chưa có phương pháp mới đủ bằng chứng tích cực; không triển khai generic shareability/repair/RL chỉ dựa vào tên gọi.

### Kiểm tra cơ chế qua core, 2026-09-17

`core-probe/Program.cs` là một chương trình .NET ngoài repo, gọi DLL Domain/Application/Algorithms hiện có để sinh candidate, kiểm tra vật lý và hard commitment, rồi dùng validator tạo ledger sau quyết định. SHA-256 của ba DLL nằm trong `core-probe.json`. Đây không phải simulator hoặc dispatcher viết lại. Chạy Release thành công, 80 fixture (4 mức budget × 20 OD hiện tại), mỗi candidate được thử độc lập với 20 OD tương lai trên cùng state.

75/80 fixture có nhiều candidate nhận khách hiện tại; 52 có số OD tương lai nhận được khác nhau. 34 fixture có cặp cùng tổng ETA usage nhưng số OD khả thi khác; 9 có cả cùng tổng ETA usage **và** cùng operational cost. Hai fixture mà mọi candidate min-cost đều có ít OD khả thi hơn phương án tốt nhất theo phép đếm này. Kết quả đầy đủ: `core-probe-analysis.json` và script `analyze_core_probe.py`.

Ví dụ budget 2,000 ms, một khách cũ 1→3 và khách hiện tại 1→0; xe bắt đầu tại node0, khoảng cách thời gian giữa hai node bằng chênh tọa độ ×1,000 ms. Hai tuyến cùng cost6,000 ms, cùng ETA usage0: (a) đón khách cũ1, trả3, đón khách mới1, trả0; (b) đón khách mới1, đón khách cũ1, trả khách cũ3, trả khách mới0. Phương án (a) còn nhận được16/20 OD thử; (b)20/20. Chúng khác thời gian đón/đi xe của khách mới và một chiều inserted-stop usage, nên đây **không phải** bằng chứng mọi chỉ tiêu khách hàng như nhau. Chứng minh hẹp là hai scalar cost/ETA reserve không đủ xác định future feasibility.

Giới hạn: chỉ một xe, 5 node trên đường thẳng, các request tiết lộ lần lượt ở cùng thời điểm vật lý; policy hard pickup/drop ETA budget và hard-zero vehicle/stop switch, không phải cấu hình C1 tight đầy đủ. Không có dự báo học từ dữ liệu, không đo runtime production, không có closed-loop uplift và không suy diễn 20 OD đều có xác suất như nhau ngoài fixture. Tăng số cơ hội có thể đánh đổi thời gian đi xe hoặc số stop của khách mới; phải đo riêng.

- Schulz & Pfeiffer (2026), DOI `10.1007/s00291-026-00847-0`: precompute reinsert một rider, và potential của nhu cầu tương lai đã có. Phần potential xấp xỉ coi tour bị thay đổi bởi insertion là mất toàn bộ potential, sau đó tính lại khi rảnh. Có cả clustering, sampling và parallelization. Không nhận generic lookahead, caching hoặc repair là mới.
- Rubinstein, Smith & Barbulescu (AAAI 2012), *Incremental Management of Oversubscribed Vehicle Schedules in Dynamic Dial-a-Ride Problems*: GTS rút conflict set rồi chèn lại, rollback khi thất bại, giới hạn số moves; duy trì stability đã là động cơ. Nguồn tải từ https://www.ri.cmu.edu/pub_files/2012/7/aaai-12.pdf vào `downloads/`. Không nhận conflict-guided repair/ejection chain là mới.
- Fielbaum & Alonso-Mora (2020), DOI `10.1016/j.trc.2020.102831`: đo bất ổn và một chính sách kiểm soát đã tồn tại. Định nghĩa 9 đếm lần dự báo tăng, không phải mọi revision; metric truncation là lựa chọn đo tác hại một chiều. Model của họ có thể reassign và reject khách đã nhận, khác generator B1 hiện tại.
- Sivagnanam et al. (2026), https://arxiv.org/abs/2603.07422v2: quick insertion, anytime route optimization và học giá trị tương lai đã được kết hợp với xác nhận phục vụ. Vì vậy thêm RL để giữ khả năng nhận khách cũng không tự mới. Ablation của họ cho thấy heuristic idle time là đối chứng mạnh. Đã tải và đọc 16 trang; coverage cụ thể ở `READING-LEDGER.md`.

Ứng viên cần kiểm tra: selection theo **khả năng chèn nhu cầu tương lai còn khả thi sau chính candidate được chọn**, có ledger/lifecycle/active leg đầy đủ. Cần đánh giá cả tour vừa sửa; không mặc định tour ấy mất mọi khả năng phục vụ. Giữ nguyên hard contract. Chỉ dùng thông tin hoặc mẫu nhu cầu hợp lệ trước decision, không nhìn tương lai thực tế của test. Đây hiện là giả thuyết thiết kế, chưa chứng minh mới, chưa có kết quả closed-loop.

Đối chứng bắt buộc trước khi nói đóng góp: C1 hiện tại; C1 chỉ sửa utilization; min-cost; residual budget đơn giản; potential bỏ tour bị sửa theo bài 2026; potential tính lại đầy đủ; phiên bản tăng tốc nếu có chứng minh tương đương. So cùng constraints và ngân sách tính toán. Đo acceptance, promise violations, distribution ETA/wait/detour, p95/p99 runtime. Không dùng H6 đã xem để chọn hyperparameter rồi gọi là confirmatory.

## Phạm vi đọc và việc tiếp theo

Đã inventory/extract đủ 13 PDF gốc, 324 trang, SHA-256 ở `corpus-inventory.json`. Đến2026-09-17 đã đọc đủ **văn bản** của cả13 PDF, kể cả phụ lục; các phần từng bị tool truncation đã đọc lại. Hình/thuật toán quan trọng được kiểm tra theo `READING-LEDGER.md`; không đồng nghĩa đã kiểm tra hình ảnh từng trang. GTS2012 và prompt-confirmation2026 đã tải/đọc thêm. Thư mục docs có195 file; chưa được tuyên bố đã đọc hết. Đã tạo bản đọc ngoài repo có deduplicate chính xác từng đoạn và ánh xạ dòng nguồn (`docs-reading/index.json`); progress từng chunk ở `docs-reading-progress.json`. Không tìm thấy docx; người dùng đã xác nhận phạm vi là file handoff Markdown và `RideBound/docs`.

Các điểm còn cần làm: hoàn tất coverage có ghi trang/tệp; đọc và đối chiếu các phương pháp gần nhất (multiple-plan, stochastic insertion, budget/recourse); kiểm tra candidate equivalence; xây witness nhỏ qua chính core .NET nếu cần; chốt tiêu chí bác bỏ ý tưởng trước khi chạy mới. Không thay các baseline H6 hoặc tuyên bố novelty chỉ vì tìm kiếm chưa thấy trùng.

`docs/18` có trạng thái dừng v6 ở 40/160 trong khi tài liệu benchmark sửa sẵn ngày 2026-09-05 ghi 160/160 và H6 rerun. Phải nêu nguồn cụ thể khi dùng số liệu; không tự ghi đè live status trong phiên read-only này.

## Mốc tạm dừng 2026-09-19 theo yêu cầu người dùng

Báo cáo tổng hợp và việc tiếp tục: `BAO-CAO-TAM-DUNG-2026-09-19.md`. Chưa có thuật toán mới được xác nhận có closed-loop uplift. Systematic docs đã đọc chunk001–041/175; next042. Root docs00–22 đã đọc hết trong chuỗi này.

Bổ sung paper16: đã tìm và đọc toàn bộ văn bản 35 trang PDF Ackermann–Rieck2025 trong kho cũ, SHA059a0bffc546e8588f1d9487ddb16344e7c24c559bc54dfa104979f98e223d3c; nguồn `corpus/16.source.json`. Điều này supersede ghi chú cũ chỉ đọc HTML§4.4–4.6/thiếu PDF. Đã render trang11,14,16,21,24,28,29,30 nhưng CHƯA xem các ảnh này; cần kiểm công thức/pseudocode/bảng khi tiếp tục. Chưa thêm thí nghiệm sau mốc all-order negative. Không có benchmark còn chạy. RideBound repo vẫn giữ nguyên hai thay đổi của người dùng.

## Resumed 2026-09-20

Previous turn completed a user-requested pause report; goal now active again. Read objective and current git status; same two user-owned changes only. Systematic docs now chunks001–044; next045 (long JSON source block2257 still continues). Paper16 selected images11,14,16,21,24,28,29,30 inspected; printed Eq1 confirmed inconsistent with general union coverage, but implementation unknown. See MULTIPLE-PLAN-16-NOTES.md; do not infer code error or invalidate numerical results.

New timestamp-only audit checks48 capture hashes across16 rejected states: all known pickup windows already open. With fixed snapshot travel and route order, extra waiting cannot repair their earliest-schedule pickup-window/max-ride failures; no forced downstream waiting is available to shift before pickup. See waiting-opportunity-audit.json and WAITING-OPPORTUNITY-NOTES.md. This strengthens only the existing bounded same-state negative result, not global DARP or future-anticipation claims. No benchmark process launched and no new positive algorithm result.

## Tạm dừng theo người dùng, 2026-09-20

Đã đọc systematic chunks001–050/175; next051. Hoàn tất phần promise-direction JSON, báo cáo H6 rerun, bản tổng hợp benchmark của người dùng và báo cáo tối ưu implementation; RidePy negative report còn tiếp ở chunk051. Các điểm diễn giải baseline/metric/ablation cần sửa được ghi trong DOCS-READING-CORRECTIONS.md, không sửa docs của RideBound.

Báo cáo cập nhật: BAO-CAO-TAM-DUNG-2026-09-20.md. Không có positive algorithm result mới, không chạy full matrix mới. Người dùng yêu cầu báo cáo và sẽ tiếp tục khi có token; dừng nghiên cứu tại đây. Git status RideBound giữ đúng hai thay đổi có sẵn. Bản báo cáo 19/09 là snapshot lịch sử, mốc tiếp tục 20/09 supersede mốc cũ.

## Nghiên cứu tiếp theo yêu cầu mới của người dùng, 2026-09-20

User cung cấp bản Claude và yêu cầu tự phát triển/kiểm chứng hướng khác. Đã đọc bản đó, tìm thêm primary sources (Woop nested slot refinement, Oracle communicated windows, Hosseini window design, TSP-SC metadata). Không coi nesting hay generic joint routing-window design là mới. Không tái lập các số Đ1–Đ4 của Claude khi thiếu scripts/provenance.

Đã đề xuất precision-deadline constrained dispatch: initial drop interval, immutable refinement deadline anchored initial lower bound, terminal width cap, shared feasible fallback, optional exact distinct-scenario interval placement. Bài toán con sweep-line đã đối chiếu1.000 integer cases với exhaustive oracle, có duplicate-color và infeasible fallback tests; đây là math prototype, không phải simulator/RideBound viết lại.

Core E1 original probe kiểm lại16 rejected states/4.153routes/9physicalpasses. Gỡ riêng old drop cumulative limit, giữ remaining full validator + conservative head screen, rồi kiểm hypothetical initial drop interval±150s và deadline lower−180s: opportunities ở epochs304,374,394. Không có closed-loop result, chưa chạy refinement deadline/whole-fleet new contract. Simple budget relaxation có thể giải thích toàn bộ early opportunity; là comparator bắt buộc. Các baseline count/state hash khớp audit trước16/16. Program/output/DLL hashes lưu interval-deadline-probe-receipt.json.

Chi tiết và next experiment: HUONG-MO-RONG-CLAUDE-2026-09-20.md. Repo vẫn read-only, hai user changes giữ nguyên. Systematic docs vẫn through050; vòng này chỉ topic-specific reading thêm, không nâng coverage toàn thư mục. Không mở WP15/H7 chính thức hay nhận novel algorithm đã xác nhận.

## Literature novelty audit requested by user, 2026-09-20
See KIEM-DINH-TINH-MOI-2026-09-20.md. New close prior art: Celik2026 delayed window assignment; H-SARA2021 two-stage narrowing/nesting objective; Bekker et al.2026 dynamic advance-notice window update; Paradiso2025 future-scenario window assignment; Dalmeijer2019 dynamic adjustment; Yu2023 rolling-horizon joint routing/windows. These lower novelty confidence materially. No confirmed new algorithm; do not commit to large implementation. Hard nested per-customer precision deadlines during online pickup/drop execution remain an unverified narrow problem hypothesis. Feasible fallback induction and standard interval sweep are insufficient method novelty by themselves. No new benchmark or repository changes. Fulltext coverage limitations and decision gates are recorded in report.


## Review of user-provided conduct/stochastic proposal, 2026-09-21
Read complete attachment cdc043b4 and verified current delta calculator/validator/test semantics plus primary literature. See DANH-GIA-CONDUCT-STOCHASTIC-2026-09-21.md. Prioritize bounded attribution/endpoint/outcome/conduct mechanism audit before large anytime solver or precision-deadline expansion. Cumulative conduct is not visible TV under drift; conduct can charge corrective actions with V=0. Two-layer probability implication is elementary and valid without independence, but lifetime X calibration is policy-dependent and not established. No new algorithm/95% guarantee/A+ prediction endorsed. No code, benchmark or repository changes.

