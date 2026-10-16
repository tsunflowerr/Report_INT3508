# Sổ bác bỏ ý tưởng — đang mở, 2026-09-17

Tài liệu này ghi cả kết quả âm để tránh biến một cơ chế hợp lý thành tuyên bố novelty hoặc hiệu quả chưa đo.

## Hướng A: giữ khả năng chèn chuyến tiếp theo dưới ledger hiện tại

**Cơ sở thực nghiệm nhỏ:** `core-probe-analysis.json` cho thấy cost và tổng ETA reserve không xác định đủ khả năng chèn future OD. 9/80 fixture có cặp cùng hai scalar đó nhưng khác số OD khả thi. Đây là witness, không phải ước lượng hiệu quả trên nhu cầu thực.

**Va chạm mạnh mới tìm thấy:** Ackermann & Rieck (2025), *Multiple plan approach for a dynamic dial-a-ride problem*, DOI [10.1007/s00291-025-00809-y](https://link.springer.com/article/10.1007/s00291-025-00809-y), §4.4–4.6 đã đọc trực tiếp trên Browser của trang nhà xuất bản. Bài so distance, time slack, double horizon, distance + early visits. §4.6 thử dự đoán nhiều scenario và độ phủ slack trong không gian/thời gian, có xử lý chồng lấn giữa xe. Cả hai extension không cải thiện MPA; coverage tốn thời gian đánh giá hơn100 lần và xấp xỉ một location làm yếu mô hình pickup–dropoff. Vì vậy **đếm độ phủ future opportunities, khử trùng giữa xe và thêm dự báo không được coi là ý tưởng mới riêng của RideBound**. PDF tải trực tiếp trả HTML thay vì PDF; lưu rõ file response.html, chưa tính là PDF đã đọc toàn bộ.

**Tác động tới lựa chọn hướng:** chỉ nên giữ ứng viên nếu chứng minh được phần tính toán đáp ứng được online và có giá trị tăng thêm so với distance + early visits, idle-time heuristic, utilization đã sửa và potential của Schulz–Pfeiffer2026. Nếu chi phí đánh giá triệt tiêu cơ hội tối ưu hoặc chỉ tái tạo ranking đơn giản thì bác bỏ.

## Phiên bản còn đáng kiểm tra, chưa phải đóng góp đã xác nhận

Dùng mẫu pickup–dropoff đầy đủ cùng arrival time được ấn định trước; với mỗi candidate hiện tại, tạo post-state bằng validator thực, kiểm tra future insertions bằng core thực. Ledger sau publication, phase lock và active leg đều phải nằm trong input. Chỉ ưu tiên future coverage trong tập candidate đạt acceptance tối đa và qua các giới hạn dịch vụ đã định trước.

Cơ chế tăng tốc có thể kiểm chứng: tái dùng feasibility của các xe thật sự không đổi; dùng cận dưới/cận trên trên phần sample chưa kiểm tra để loại candidate không thể thắng. Đếm một future request tối đa một lần trên fleet. Đây là ứng dụng của incremental evaluation/bounding đã biết; novelty phải nằm ở phương pháp cụ thể xử lý commitment state và lợi ích được đo, không phải tên gọi.

Với tập mẫu cố định Q, trọng số không âm w(q), `I(v,a,q)` là predicate có insertion hợp lệ trên xe v sau action a. Điểm `F(a)=sum_q w(q)*max_v I(v,a,q)`. Nếu C(a) là tập xe thay đổi và một xe ngoài C(a) đã phục vụ được q, contribution của q đã biết, không cần kiểm tra xe thay đổi. Nếu chưa biết contribution q, cận [0,w(q)] hợp lệ. Khi mọi cận trên của đối thủ nhỏ hơn cận dưới của incumbent tốt nhất, có thể dừng mà vẫn chọn đúng optimum của **score trên tập Q**, với xử lý tie-break thống nhất. Đây không bảo đảm optimum số khách cả ngày, và không biến rejection từ một insertion generator hạn chế thành chứng minh vô nghiệm DARP.

Điều kiện tái dùng phải bao gồm route, vehicle execution position, onboard/lifecycle, travel snapshot, request windows, ledger/budget basis, policy version, probe arrival time và generator options. Chỉ route hash là không đủ. Với reassign/repair nhiều xe hoặc trạng thái chuyển phase, phải cập nhật dependency set tương ứng. Mẫu nhu cầu tương lai không được lấy từ phần test chưa đến; score của các request giả định được tính độc lập, không giả định nhận được đồng thời tất cả.

**Cửa kiểm chứng tiếp theo:** actual retained state → score disagreement với các baseline đơn giản → kiểm tra runtime theo cùng compute budget → replay phát triển qua cùng versioned runner → held-out evaluation. Bất kỳ tầng nào thất bại đều phải ghi âm và dừng hướng đó; không chạy cả matrix để tìm một ô đẹp.

## Kết quả trên state E1 thật: union coverage yếu, 2026-09-17

`state-replay` gọi đúng DLL Runner E1 đã dùng trong transcript, đối chiếu98 phản hồi canonical byte-exact và lưu20 state trước các epoch có pending. `retained-states-e1-prefix/receipt.json` chứa hashnguồn/config/DLL và từng state. Không sửa source hay publish lại baseline.

`state-probe` decode bằng checkpoint codec gốc, apply event bằng reducer gốc, sinh và hard-filter bằng core gốc. Tập eligible candidate ID khớp E1 tại cả20 epoch. Với mỗi fleet assignment nhận được khách hiện tại, giả định booking confirmation ngay cùng simulation time, mở ledger bằng validator thật, rồi thử độc lập tối đa12 OD/service types đã xuất hiện **trước** decision. Không đọc suffix nhu cầu để tạo mẫu. Mỗi mẫu là request mới, không phải tái nhận request cũ.

Kết quả `retained-state-probe-analysis.json`:69 assignment;16 epoch có từ2 assignment và ít nhất1 mẫu. Chỉ1/16 có khác số mẫu khả thi (epoch55:9hoặc10/12); C1 đã chọn10/12. 15/16 còn lại cả tập mẫu được phủ cũng giống nhau. Vì vậy **chưa có một state nào ở phép thử này cho thấy đổi sang maximization union coverage cải thiện score so với C1**. Chưa đủ cơ sở chạy full replay cho biến thể này. Một fixture không nhận được currentrequest nên không có accepting assignment; không xóa nó khỏi tổng20.

Giới hạn: đây là20 pending epoch đầu của một run đã xem, phép thử cấu trúc ở cùng thời điểm vật lý với mẫu lịch sử nhỏ, không phải forecast/closed-loop/held-out. Thời gian mỗi assignment chỉ là đo một lần trong process, không phải latency benchmark. Không phủ định mọi lookahead, nhưng bác bỏ việc lấy toy witness làm lý do triển khai ngay score này.

Ở16/16 epoch nói trên, **xe nào phục vụ được mẫu** lại khác nhau. Câu hỏi tiếp theo có phạm vi hẹp: cùng phủ từng request nhưng cùng tranh một xe có làm giảm khả năng phục vụ một batch gồm2 request không? Matching trên feasibility graph cho lower bound có điều kiện (mỗi xe nhận nhiều nhất1 request giả định); pooling thực có thể phục vụ cả2 trên một xe nên matching không phải optimum chung. Đây là kiến thức matching/lookahead đã biết, phải đối chiếu prior art và kiểm chứng bằng batch insertion thật trước khi dùng làm thuật toán.

### Kiểm tra cạnh tranh theo cặp: vẫn chưa có uplift trên score, 2026-09-18

`analyze_pair_competition.py` duyệt mọi cặp OD/service types khác nhau trong đúng các graph đã ghi, cho mỗi xe nhận tối đa một request giả định. `pair-competition-analysis.json` cho thấy score tổng số request ghép được phân biệt candidate ở3 epoch (55,68,96), nhưng **C1 đã đạt score cao nhất ở cả3**, và không thấp hơn optimum ở bất kỳ epoch nào trong20 state. Đây là phân tích offline của feasibility graph, không phải dispatch hay kiểm tra joint pooling. Chưa có lý do thực nghiệm để trả thêm chi phí batch lookahead trên mẫu này. Mẫu12 loại đầu lịch sử và cùng physical time là hạn chế lớn; không kết luận forecast nói chung vô ích.

### Prior art anticipatory routing đã đối chiếu thêm

Fielbaum, Kronmueller & Alonso-Mora, *Anticipatory routing methods for an on-demand ridepooling mobility system*, Transportation49 (2022), DOI10.1007/s11116-021-10232-1 (online2021): đã đọc toàn văn HTML trên Browser, gồm kết quả âm và sensitivity. Reward theo vùng nhu cầu và chèn request giả định từ dữ liệu vừa quan sát đều đã có; joint assignment đã xử lý cạnh tranh xe và tránh cấp hai xe cho một request tương lai. Không lấy những ý này làm novelty. Download publisher trả HTML3038byte; bản arXiv2106.14685v1 tải hợp lệ33trang, SHA-256f974a29edd335815eab42abcdf4dd3712ff8a3b808534964cb00bee9c49f35e0; chưa tự coi bảnPDF là đã đọc riêng/đồng nhất hoàn toàn với bản xuất bản.

Trong Manhattan của bài này, artificial requests phải kèm pruning mạnh hơn vì tăng chi phí; service trade-off gồm cả tác động pruning. Ghép reward+artificial request còn tệ hơn. Shenzhen nhỏ lại cải thiện rejection nhờ không cần pruning và nhiều epoch không có real request. Vì thế không suy ra một loại lookahead luôn tốt/xấu từ một quy mô. Model cho phép rút lại một số assignment và có rebalancing, khác C1 hiện tại. Các số trong bài chỉ là kết quả của bài, không phải so sánh trực tiếp với RideBound.

## Hướng B: kiểm tra lại repair với hợp đồng giữ nguyên

Handoff gọi repair đã bị loại, nhưng18/20 B4 run hỏng vì adapter lock là implementation evidence, còn một run B4=B1 không bác bỏ neighborhood này trên C1. Kiểm tra tiếp theo được giới hạn ở core gốc và state đã capture: sinh same-vehicle one-pair repair bằng `WithRepairRequestCap(4)`, giữ exact điểm dừng kế tiếp cho mọi xe đang có tuyến (điều kiện bảo thủ hơn chỉ active leg), chạy hard-vector và full validator. Không tuyên bố đây là repair mới: GTS2012, MPA2025, potential-based2026 và source hiện tại đã có nhiều thành phần. Mục tiêu của phép thử là xác định có cơ hội phục hồi feasibility dưới hard contract trước khi thiết kế cách tìm hiệu quả.

Kết quả đầu: cả20 pending state đầu đều có số accepting candidate sau conservative head-block screen + hard validator bằng baseline; không có rescue. `retained-repair-probe.json` lưu đủ input hashes/generation diagnostics/validated routes. Chỉ1state trong20 bị từ chối, nên cần mở rộng có mục tiêu.

Đợt mở rộng hoàn tất trên cùng run C1tight r1 qua original E1 Runner:750response canonical byte-exact,16state bị từ chối, có receipt nguồn/config/DLL. `retained-repair-rejected-probe.json` và `repair-probe-analysis.json`: không rescue ở cả16, generation complete ở cả16; eligible ID baseline khớp tại từng state. Chỉepoch275 còn1raw repair candidate vật lý hợp lệ, bị phase lock. First-witness counts vật lý1169pickup-window/486max-ride; sau head screen có2phase-lock/3budget witnesses. Đây là candidate-level fail-fast counts, không phải số khách hay nguyên nhân tối thiểu. Không lấy số raw repair candidate làm số cấu hình đã xét: phần lớn phương án bị loại trước retention. Neighborhood chỉ chuyển một cặp waiting incumbent, không thử joint moves/onboard drop reordering/reassignment. Giữ toàn bộ leading same-node block là screen bảo thủ, chưa chứng minh exact FleetPy locked-leg signature. Kết quả âm này không chứng minh DARP vô nghiệm hoặc loại trừ lợi ích từ quyết định ở epoch trước.

## Va chạm trực tiếp mới: shareability shadows2026

### Mở rộng repair đến toàn bộ thứ tự trong bound thực,2026-09-18

`drop-relocation-probe` trước hết thử dời một dropoff (kể cả onboard), rồi thử **mọi hoán vị suffix khách cũ và mọi vị trí pickup/drop của pending request** trên từng xe, giữ vehicle assignment/frozen prefix và schedule earliest-feasible. Các suffix thực dài tối đa4stop; count được kiểm bằng `n!*(n+1)*(n+2)/2` trên từng vehicle-state. Sau lần có head screen, phép audit riêng bỏ hẳn screen bảo thủ đó để nó không che một route core-valid. Không route nào được gửi vào FleetPy.

`all-order-probe-analysis.json`:16state,4153route,9physical-pass,0full-contract acceptance. Tất cả9physical-pass vẫn giữ thứ tự khách cũ; permutation không mở thêm physical option.7budget-witness và2phase-lock. Quan trọng: cả7budget-witness có `BudgetBefore=0`, signed drop delay dương71785–258426ms, lớn hơn limit30000ms. Hai lock-witness cũng là pickup trễ thêm215355/229712ms. Vì vậy trên9route này, tiết kiệm cumulative budget từ epoch trước hoặc thêm waiting không xóa blocker đầu tiên. Không suy từ9route thành toàn bộ80run, không gọi đây là global DARP infeasibility; đổi trajectory trước đó, assignment, contract hay schedule family vẫn là câu hỏi khác.

Kết luận thực dụng cho vòng ý tưởng: **không triển khai larger same-state repair vào C1 chỉ với hy vọng hết rejection trên run này**. Bằng chứng không còn dừng ở failure của một heuristic; đã duyệt đủ route-order family nêu trên. Nếu quay lại repair phải có positive witness ở một operating point khác hoặc một thay đổi có cơ sở ở decision trước đó. Không biến negative audit thành đóng góp thuật toán tích cực.

Elmi et al.2026 đã bảo vệ nhóm khách ít có khả năng ghép thêm bằng cách gán zero slack ngay lúc nhận chuyến. Vì vậy bảo vệ chọn lọc bằng shareability score không phải khác biệt mới. Đọc toàn văn và kiểm ảnhTable2 cho thấy số khách bị thay đổi giảm mạnh nhưng gánh nặng có điều kiện tăng; bài cũng tự đề xuất equity, magnitude và repeated updates làm future work. Xem SHAREABILITY-SHADOWS-18-NOTES.md để tránh nhầm phần trăm với điểm phần trăm và conditional với population mean.

Không tự biến khoảng trống equity thành tuyên bố thuật toán mới. Trước hết cần một phương pháp giữ cùng initial offer và giới hạn từng khách mà phục hồi được một phần service loss, hoặc một contract khác có cơ sở người dùng rõ ràng. Các probe hiện tại chưa xác nhận được điều này; chưa có ứng viên đủ bằng chứng để triển khai vào RideBound.

## Mốc tạm dừng 2026-09-19 theo yêu cầu người dùng

Báo cáo tổng hợp và việc tiếp tục: `BAO-CAO-TAM-DUNG-2026-09-19.md`. Chưa có thuật toán mới được xác nhận có closed-loop uplift. Systematic docs đã đọc chunk001–041/175; next042. Root docs00–22 đã đọc hết trong chuỗi này.

Bổ sung paper16: đã tìm và đọc toàn bộ văn bản 35 trang PDF Ackermann–Rieck2025 trong kho cũ, SHA059a0bffc546e8588f1d9487ddb16344e7c24c559bc54dfa104979f98e223d3c; nguồn `corpus/16.source.json`. Điều này supersede ghi chú cũ chỉ đọc HTML§4.4–4.6/thiếu PDF. Đã render trang11,14,16,21,24,28,29,30 nhưng CHƯA xem các ảnh này; cần kiểm công thức/pseudocode/bảng khi tiếp tục. Chưa thêm thí nghiệm sau mốc all-order negative. Không có benchmark còn chạy. RideBound repo vẫn giữ nguyên hai thay đổi của người dùng.
