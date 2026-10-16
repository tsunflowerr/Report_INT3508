# Phản biện hướng cumulative conduct + stochastic outcome — 21/09/2026

Nguồn đề xuất: C:/Users/quang/.codex/attachments/cdc043b4-1ed4-4ba7-a74e-1547d6d7670d/Pasted text.txt (đã đọc toàn bộ).

## Quyết định

Ưu tiên kiểm chứng hướng này trước precision-deadline và trước phát triển solver anytime lớn: tận dụng lõi hiện có và đặt đúng câu hỏi attribution. Tuy nhiên không xác nhận novelty chỉ từ tổ hợp thành phần; không nhận bất đẳng thức tam giác là định lý mới; chưa có bảo đảm xác suất từ dữ liệu. Các mức điểm 8.x/9.x trong đề xuất không có căn cứ đánh giá hội đồng.

Phân biệt: hướng định vị mô hình/kiểm chứng có cơ sở; đóng góp thuật toán mới chưa được xác lập; two-layer stochastic là nhánh có điều kiện, chưa phải tính năng triển khai.

## 1. Ba đại lượng khác nhau

Tại publication t, v_t là promise trước, e_t là chiếu lại incumbent theo snapshot hiện tại, p_t là promise mới. Với lịch công bố nhất quán v_t=p_(t-1), đặt C=sum|p-e|, X=sum|e-v|, V=sum|p-v|. C là conduct variation so với incumbent projection; V mới là total variation của chuỗi khách nhìn thấy.

D+ <= E <= V đúng cho ETA vô hướng, E=|q_T-q_0|. C<=beta không suy ra V<=beta khi X>0. Phản ví dụ đại số: v=0,e=120,p=120 cho C=0,V=X=120. Khi e=v tại mọi bước thì C=V. Không suy từ một chiều ETA sang mọi thành phần vector (material-event count có ngưỡng, stop distance không nhất thiết metric, inversion trên tập thay đổi).

Baseline initial-offer phải kiểm ở mọi update, ví dụ max_t|q_t-q0|<=beta; latest-arrival một phía là một baseline khác. Không mô tả tất cả bài hard-window như chỉ kiểm giờ cuối. Ngay với ràng buộc mọi update, chuỗi 0,beta,0,beta,0,... có V tăng theo số bước. Đây là phân biệt đúng, nhưng toán cơ bản không mới.

H=V-E>=0 là chỉ báo đảo chiều. Nếu P là tổng bước tăng và N tổng độ lớn bước giảm thì H=2min(P,N). Nó không đo toàn bộ gánh nặng thông báo: chuỗi đơn điệu nhiều update vẫn H=0; cadence phải cố định/chứng minh tương thích. Không gọi H là thước đo hài lòng đã được xác thực.

## 2. Conduct và outcome không trội nhau

Ví dụ v=0,e=120,p=0: điều phối bù lại drift, C=120, X=120, V=0. Cap C=30 có thể chặn thao tác giữ nguyên ETA công bố. Vì vậy không được giả định conduct luôn tốt hơn outcome, hoặc luôn phục vụ nhiều hơn.

Đặt s=p-e, x=e-v. Với từng bước:
|s|+|x|-|s+x| = 2min(|s|,|x|) nếu sx<0, ngược lại bằng 0.
Cộng lại C+X-V đo triệt tiêu giữa drift và quyết định trong từng bước. Nó khác H=V-E (triệt tiêu qua lịch sử publication). Hai kiểu cancellation cần tách.

Nguồn code đã đọc: PromiseDeltaCalculator.cs tính riêng ba cặp; CommitmentDecisionValidator.cs chọn charged theo BudgetBasis. PromiseDeltaCalculatorTests.cs dòng 64–73 có X=1000,C=500,V=500 và Assert.NotEqual(X+C,V). Non-additivity đã được test hiện có ghi nhận; không phải phát hiện implementation mới của lượt này. Không chạy tests vì không đổi code.

## 3. Two-layer bound đúng, khó ở tiền đề

Nếu C<=beta trên mọi trajectory thuộc phạm vi chứng nhận và P_pi(X<=gamma)>=1-alpha dưới đúng policy pi/quần thể/lịch cập nhật, thì P_pi(V<=beta+gamma)>=1-alpha. Không cần C và X độc lập. Cận này có thể lỏng vì cancellation.

Những điều còn thiếu trước khi nói guarantee 95%:
- X là tổng drift suốt lifecycle, không phải sai số một đoạn đường hay một lần ETA.
- Route, thời gian chạy, số epoch và tập khách nhận do policy chọn; X phụ thuộc policy dù traffic field được sinh ngoại sinh. Gamma của baseline không mặc nhiên dùng được cho policy mới.
- Quantile thực nghiệm 95% không tự là coverage đã được chứng minh. Phải tách development/calibration/test, nêu giả thiết dữ liệu và mức bất định hữu hạn mẫu.
- Marginal coverage của khách ngẫu nhiên không có nghĩa mọi khách/nhóm có cùng coverage, hoặc cả fleet cùng được bảo vệ 95%.
- Traffic-correlated riders không phải mẫu IID độc lập. Chia theo episode/ngày/traffic field độc lập; không random-split từng update cùng hành trình.
- Gamma phải được tạo từ thông tin có trước cam kết. Không tính sau khi chuyến kết thúc rồi gọi là promise đã cung cấp.
- V nhỏ không đồng nghĩa đến đúng giờ. ETA đứng im nhưng xe đến trễ vẫn có V=0 nếu không tính terminal correction. Báo cáo arrival error/late service riêng, định nghĩa terminal event và khách không hoàn tất.

Tham khảo nền: Fu2002 trực tiếp xét stochastic time-varying congestion (https://doi.org/10.1016/S0191-2615(01)00014-5). Dong2022 (https://doi.org/10.1016/j.tre.2021.102601) chủ yếu có chance constraint gắn utilities/lựa chọn mode qua Logit; không lấy nó làm bằng chứng đã kiểm cho lifetime traffic-drift calibration. Feedback/dependent selection là vấn đề thật của uncertainty quantification: https://pmc.ncbi.nlm.nih.gov/articles/PMC9618043/ (đọc phần mô hình/abstract; không suy định lý biomolecular sang routing tự động).

## 4. Attribution không phải miễn trách nhiệm nhân quả

e là incumbent-plan projection từ cùng physical state, cùng traffic/forecast snapshot và information set với p. Không phải toàn bộ thế giới nếu operator chưa từng chọn những tuyến trước đó. Một quyết định quá khứ có thể đưa xe vào vùng hay tắc rồi phần drift tương lai vẫn nằm ở X theo quy ước local này.

Nên gọi model-based one-step counterfactual accounting hoặc quy trách thay đổi trực tiếp so với incumbent, không khẳng định tách mọi nguyên nhân ngoại sinh và nội sinh ngoài đời. Kiểm soát version projector, active leg, waiting, forecast timestamps, incident override và publication. Chỉ charge quyết định thực sự commit; không charge lần thử plan.

C<=beta bảo đảm ngân sách hành vi trong phạm vi mô hình, không bảo đảm physical feasibility khi có sự cố bất kỳ. Baseline outcome/endpoint bị traffic làm vượt hứa phải ghi breach và có cùng incident semantics, không cho crash/ẩn số liệu để tạo chiến thắng giả cho conduct.

## 5. Multiple-plan và fairness

Pool phải chia sẻ một lịch sử publication/ledger thật. Khi chuyển sang plan khác phải tính chi phí chuyển từ incumbent thật; hypothetical ledger riêng không cho phép quay về lịch sử rẻ hơn. Các plan phải còn tương thích executed prefix/active leg tại thời điểm dùng. K lớn mà không cải thiện không chứng minh price of commitment tối thiểu. K lớn cải thiện cho thấy policy thử tốt hơn comparator, chưa phân rã được service deficit thành các phần nhân quả cộng được.

Existing audit 16 reject states/4153 routes/9 physical-pass/0 old-contract-pass là bằng chứng phạm vi nhỏ chống kỳ vọng cứu bằng đổi suffix tại đúng state. Các trajectory sớm hơn vẫn là câu hỏi mở; không triển khai beam chỉ dựa ví dụ giả định -7.13pp thành -4pp.

Fairness-tail là phân tích phụ, không mặc nhiên novelty. Cần báo rejected/accepted cohort: loại khách khó có thể làm burden và Gini thấp giả tạo. Beta=0 không có A/beta hữu hạn. Mean=0 cần quy ước Gini; p99 với mẫu ít rất không ổn định.

## 6. Thứ tự làm cụ thể

A. Audit dữ liệu hiện có: C,X,V,E,H, cancellation, số publication và dấu từng bước theo lifecycle/cohort; xác định tỷ lệ có X>0 hoặc đổi chiều. Nếu hiện tại ETA gần đơn điệu/X=0, dữ liệu ấy chưa phân biệt được cơ chế, không ép kể câu chuyện oscillation.

B. Đặc tả cùng candidate generator/objective/publication cadence và các policy: không cap commitment (vẫn physical constraints); cap so initial offer tại mỗi update; outcome cumulative; conduct cumulative; no voluntary update. Phân biệt baseline cơ chế với reproduction Schulz/Elmi đầy đủ. Elmi targeted cần selection thật nếu muốn claim so trực tiếp paper, không lấy freeze toàn fleet để thay thế.

C. Ba panel có mục đích: không drift; drift mà no-op không thể ngăn; drift có repair/cancellation khả thi. Thêm case biết trước cả điểm yếu của conduct. Dùng physical simulator/runner thật để xác nhận ví dụ đại số có thể xảy ra, không gọi toy arithmetic là kết quả routing.

D. Traffic field nhất quán theo edge/time và FIFO/travel contract, không rung ETA độc lập tùy epoch. Các policy dùng cùng field/ngày, có thể đi route khác. Tất cả traffic regimes giả lập ghi rõ synthetic; dữ liệu nhu cầu thật không biến stochastic traffic giả lập thành dữ liệu thực.

E. Sau khi có khác biệt có ích mới calibration gamma dưới policy đã khóa; báo coverage held-out, uncertainty, theo nhóm và độ chặt beta+gamma-V. Nếu cận quá rộng để khách dùng được, chỉ nhận accounting contribution; không quảng cáo customer guarantee hữu ích.

Không mở full matrix mới trước A–C. Không thay đổi code hoặc docs RideBound trong lượt đánh giá. Không chuyển ngay sang xây solver anytime; đây là ưu tiên nghiên cứu so với đề xuất trước, không phải bằng chứng nó đã thắng.

## 7. Claim phù hợp

Ứng viên đóng góp: mô hình và cơ chế kiểm soát biến thiên ETA tích lũy dưới một quy tắc quy trách counterfactual được định nghĩa rõ, kèm characterization khi conduct/outcome khác nhau và kiểm chứng dịch vụ dưới nhiễu. Mở rộng: chuyển bảo đảm conduct thành bound outcome có coverage đã kiểm/được chứng minh dưới giả thiết rõ.

Không claim: total variation, triangle inequality, generic counterfactual, chance constraint, personalized reliability, beam search hoặc Gini là mới; không claim theorem đơn giản đủ A+; không claim chưa tìm thấy exact counterpart là novelty toàn cầu.

Lượt này đọc toàn bộ đề xuất, kiểm code/test định nghĩa, kiểm nguồn primary Fu2002/Dong2022/Schulz2026/Elmi2026 metadata và nghiên cứu feedback covariate shift; query targeted cumulative variation/decision-induced/exogenous/counterfactual promises chưa cho exact counterpart đã xác minh. Không phải systematic review hoàn tất. Không có positive closed-loop result mới.
