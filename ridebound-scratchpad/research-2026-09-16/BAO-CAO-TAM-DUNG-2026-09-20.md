# RideBound — báo cáo phân tích và mốc tạm dừng 20/09/2026

Tạm dừng theo yêu cầu người dùng, chờ tiếp tục khi có token. Chưa đạt mục tiêu tìm thuật toán khác biệt có bằng chứng cải thiện trong vận hành online liên tục (closed-loop). Kết quả hiện có là: xác định đối thủ gần, kiểm toán cách diễn giải kết quả, tìm điểm yếu có thể thử nghiệm và loại một số hướng bằng phép thử qua core gốc. Không nên gọi các kết quả này là một phương pháp mới đã thành công.

## 1. Phạm vi đã hoàn thành

- Đọc toàn bộ bản bàn giao RIDEBOUND-BAN-GIAO-CONTEXT.md.
- Đọc văn bản toàn bộ 13 PDF gốc trong C:\PDF\Paper, tổng 324 trang; kiểm tra các hình, bảng, thuật toán được chọn, không phải hình ảnh từng trang.
- Đọc thêm GTS 2012, prompt-confirmation 2026, anticipatory routing 2022 (toàn văn HTML), shareability shadows 2026 và multiple-plan DARP 2025. Bài multiple-plan đã đọc đủ 35 trang văn bản và kiểm ảnh 8 trang chọn lọc.
- Inventory docs có 195 file. Đã đọc chuỗi chunk001–050/175 sau loại đoạn trùng hoàn toàn, có ánh xạ về nguồn; bao gồm toàn bộ docs gốc 00–22. Đây không phải tỷ lệ số file đã đọc. Một số tài liệu khác đã được đọc riêng theo chủ đề. Chưa đọc hết docs.
- Đối chiếu các đường mã liên quan đến candidate generation, physical feasibility, commitment ledger, objectives, fleet selection và Runner; chưa audit toàn bộ mã nguồn.
- Phân tích lại 80 run cũ; duyệt toàn bộ fleet assignment trong 4.285 epoch có pending của 40 run E1 panel A. Chạy các probe nhỏ ngoài repo bằng DLL/core gốc, không viết lại RideBound trong một simulator khác.

## 2. Đánh giá tổng thể hiện tại

RideBound có cơ chế cam kết rõ và bằng chứng đánh đổi giữa ổn định ETA với số khách phục vụ. Tuy nhiên, chưa có bằng chứng từ đợt nghiên cứu này cho một thuật toán mới đạt mục tiêu khóa luận mà người dùng đặt ra. Giảm burden rất mạnh không tự đủ để kết luận hệ thống tốt hơn: còn mất phục vụ, khác giả định baseline, và tác động lên từng nhóm khách.

H6 rerun được đọc ghi panel A từ 1.735 xuống 1.581 khách được nhận, giảm khoảng 7,13 điểm phần trăm tỷ lệ phục vụ; panel B từ 966 xuống 860, giảm khoảng 4,91 điểm phần trăm. Decision-induced burden giảm tương ứng khoảng 99,83% và 99,23%. Đây là đánh đổi đã quan sát, không phải cải thiện đồng thời hai mặt. Rerun với adapter đã sửa khớp số tổng hợp được công bố, nhưng không còn adapter bytes nguyên bản để tuyên bố tái lập chính xác toàn bộ nguồn thực thi cũ.

## 3. Đối thủ gần nhất

Elmi et al. (2026), Improving ridepooling reliability using shareability shadows, DOI https://doi.org/10.1016/j.trc.2026.105897, là va chạm trực tiếp đáng kể. Bài chọn nhóm khách được bảo vệ khỏi tăng dự báo delay dựa trên khả năng ghép thêm chuyến. Do đó, thêm shareability score rồi bảo vệ chọn lọc không tự tạo novelty.

Trong so sánh của chính bài, rejection gần bằng nhau (29,09% và 29,21%), tỷ lệ khách bị tăng delay giảm 63,17% xuống 15,39%. Nhưng trong nhóm thực sự bị tăng, mức tăng trung bình tăng từ 0,84 lên 3,74 phút và số lần tăng trung bình từ 1,05 lên 1,80. Đây là phân phối lại gánh nặng, không phải mọi khách cùng tốt hơn. Tác giả đã nêu equity, magnitude và repeated updates trong future work; chỉ chỉ ra những vấn đề ấy chưa phải đóng góp mới. Không so trực tiếp tỷ lệ của họ với RideBound vì khác dữ liệu và vận hành.

Multiple-plan 2025 đã có nhiều kế hoạch, consensus, slack, repair và coverage có xét chồng lấn giữa xe. Future-potential, conflict-guided repair, anticipatory demand và học giá trị tương lai cũng đã xuất hiện trong các nguồn khác đã đọc. Vì vậy generic lookahead, RL, repair, least commitment hoặc ETA limits không đủ để nhận là mới.

## 4. Những phát hiện quan trọng trong RideBound

### 4.1. Sửa giới hạn của lập luận toán học

Với A=|p-e|, d=|e-v| và B=|p-v|, chỉ có |A-d| ≤ B ≤ A+d trong trường hợp tổng quát. B=A+d cần biến thiên cùng chiều. Dữ liệu H6 B1 có 255 tọa độ publication với B<A; tổng A+d-B bằng 58.172 ms. Sai khác nhỏ trong tổng số không biến đẳng thức thành định lý. Docs/04 đã cảnh báo đúng; phần bàn giao cần được diễn giải lại.

Bao hàm tập feasible tại cùng state cũng không tự chứng minh thứ tự tổng số khách của hai policy online: lựa chọn trước làm thay đổi state sau. No-op tiêu 0 conduct budget chỉ chứng minh về budget gate, không phải mọi điều kiện vật lý.

### 4.2. Có không gian lựa chọn nhưng một tầng objective bị bão hòa

C1 có 1.045/1.571 epoch đang nhận khách chứa nhiều fleet assignment cùng acceptance tối đa, khoảng 66,5%. Không gian thay selection có thật.

Nhưng objective worst utilization là hằng số giữa các assignment tối đa acceptance tại cả 2.123 epoch có objective này. Một hard dimension có limit=0 và usage=0 được quy thành 1.000.000 ppm, làm max bão hòa. Đây là lựa chọn có chủ ý trong docs/18, không phải regression mới. Thử ranking chỉ trên chiều có ngân sách dương là một ablation cần thiết; chưa có kết quả cho thấy nó tăng phục vụ và riêng nó chưa đủ thành đóng góp thuật toán mạnh.

### 4.3. Baseline và metric đang bị diễn giải rộng quá

B1 không được tùy ý đổi xe/địa điểm đón khách cũ, vẫn chịu physical windows/max-ride và dùng acceptance trước cost. B1 cũng có publication ledger để đo. Vì vậy không mô tả B1 là baseline hoàn toàn tự do hoặc không có lời hứa.

Decision burden hiện tính absolute ETA variation, không chỉ các lần ETA tăng. Biến thể nopickuplock bỏ pickup ETA lock, không phải cho phép đổi địa điểm đón. Một vài arm có kết quả giống nhau không chứng minh cơ chế của chúng luôn vô tác dụng. Các điểm này đã ghi ở DOCS-READING-CORRECTIONS.md; chưa sửa tài liệu của người dùng.

## 5. Các ý tưởng đã thử và kết quả

### Giữ khả năng nhận khách tương lai

80 fixture nhỏ qua core cho thấy cùng cost và ETA usage vẫn có thể khác future feasibility; 9 fixture có cặp thỏa cả hai điều kiện. Đây là bằng chứng hai scalar chưa mô tả hết giá trị tương lai, không phải uplift thực tế.

Trên 20 state thật, 69 accepting assignments và tối đa 12 loại OD/service từ lịch sử trước decision: union coverage chỉ phân biệt 1/16 epoch đủ điều kiện, C1 đã chọn tốt nhất. Matching các cặp mẫu phân biệt 3 epoch, C1 cũng tốt nhất cả 3. Chưa tìm được quyết định tốt hơn C1 theo các score đã thử. Phạm vi nhỏ và cùng physical time, chưa bác bỏ mọi lookahead.

### Sửa tuyến mạnh hơn ngay lúc bị từ chối

Replay đúng Runner E1 khớp 750 response canonical byte-exact; lấy đủ 16 state bị từ chối của một run C1 tight. Duyệt toàn bộ hoán vị suffix khách cũ và vị trí chèn khách mới: 4.153 route, chỉ 9 qua vật lý, 0 qua toàn bộ hợp đồng, kể cả bỏ conservative head screen. Suffix thực tế dài tối đa 4 stop.

Cả 7 budget witnesses đều chưa tiêu ngân sách trước đó nhưng lần chèn cần tăng khoảng 72–258 giây, vượt trần 30 giây. Hai witness khác vi phạm phase lock. Đây là candidate-level witnesses, không phải 9 khách riêng biệt. Tiết kiệm budget trước đó không cứu được các witness có usage trước bằng 0.

Kiểm tra bổ sung ngày20/09 xác minh 48 capture hashes và cho thấy pickup windows của mọi request đã biết đều mở tại 16 state. Với snapshot travel cố định, cùng assignment và route, thêm chờ không sửa được những failure đang thấy: không có chờ bắt buộc phía sau để chuyển ra trước pickup; ETA chỉ muộn hơn. Kết luận này không áp dụng cho thay quyết định trước, đổi assignment, tương lai có request đặt trước hoặc travel khác.

Do đó chưa có lý do tốt để chạy một ma trận lớn cho immediate repair này tại operating point đã kiểm tra. Không suy rộng thành mọi bài toán DARP vô nghiệm.

## 6. Khi tiếp tục, nên làm gì

1. Đọc tiếp docs ở chunk051; phần RidePy negative report đang tiếp. Không đọc lại từ đầu. Bản kiểm ảnh multiple-plan đã hoàn tất và không còn là việc chờ làm như báo cáo19/09.
2. Chốt bảng so sánh hợp đồng, hành động được phép và baseline với những bài gần nhất. Tách khác biệt semantics khỏi cải thiện thuật toán.
3. Thử ablation utilization nhỏ và tìm positive witness trên state thật cho một lựa chọn sớm tốt hơn. So với min-cost, idle-time, residual budget và future-potential đủ mạnh, cùng hard contract và ngân sách tính toán.
4. Chỉ mở thử nghiệm closed-loop lớn nếu phép thử nhỏ cho tín hiệu rõ. Nếu phải đổi contract, chỉ rõ lời hứa nào bị thay đổi và lợi ích nào nhận lại; không gọi đó là cải thiện miễn phí. Không dùng H6 đã xem để chọn tham số rồi gọi là holdout.

Hướng giữ future feasibility dưới cam kết còn mở, nhưng score đơn giản đã thử chưa thắng C1 và ý tưởng chung đã có trong văn liệu. Chưa chốt hướng này là đóng góp khóa luận. Mục tiêu tiếp theo phải là một cơ chế cụ thể có positive witness và khác biệt bảo vệ được, không phải thêm nhiều metric.

## 7. Bảo toàn và mốc tiếp tục

Mọi ghi chép/probe mới ở E:\Code\Report_INT3508\ridebound-scratchpad\research-2026-09-16. Không sửa source/config/raw results của RideBound. Git status vẫn chỉ hai thay đổi có sẵn: docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md bị sửa và docs/benchmarking/Kết quả benchmark.md chưa tracked. Không có benchmark mới đang chạy.

Mốc đọc: docs-reading-progress.json (001–050, next051). Bằng chứng: RESEARCH-STATUS.md, IDEA-FALSIFICATION.md, READING-LEDGER.md, DOCS-READING-CORRECTIONS.md, SHAREABILITY-SHADOWS-18-NOTES.md, MULTIPLE-PLAN-16-NOTES.md, WAITING-OPPORTUNITY-NOTES.md; cùng các JSON audit/receipt có hash. Báo cáo này cập nhật mốc tạm dừng19/09; không sửa bản lịch sử ấy.
