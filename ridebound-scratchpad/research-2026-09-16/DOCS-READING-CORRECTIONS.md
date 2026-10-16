# Corrections found during systematic docs reading

2026-09-18. Research notes only; RideBound repository remains read-only. These are observations and proposed wording corrections, not edits to historical evidence.

- `docs/19-requirement-traceability.md:596` table, baseline-strength row: forbidding reassignment gives a restricted action set at the same state. This alone does not prove the observed closed-loop service deficit is a lower bound relative to a different online baseline with reassignment. Earlier actions alter later states; a heuristic can use the larger action set poorly. A same-state optimality bound needs a fixed objective/state; a closed-loop comparison needs a matched experiment or a policy-dominance proof. Retain the weaker defensible claim: baseline capability is restricted, and published results with reassignment/rebalancing are not directly comparable.
- `docs/21-paper-to-design-evidence.md:326` table incorrectly attaches DOI `10.1002/net.22063` to an Ackermann–Rieck multiple-plan paper. Wiley identifies that DOI as Tellez et al., *The time-consistent dial-a-ride problem*, Networks 79(4), 452–478, 2022 (online 2021): https://onlinelibrary.wiley.com/doi/10.1002/net.22063 . The root document's opening table correctly gives the 2025 multiple-plan DARP DOI `10.1007/s00291-025-00809-y`; do not merge those distinct papers or infer the intended replacement for every historical citation without checking its title.
- `docs/21` section 26 points to an already available full 35-page publisher PDF for Ackermann et al. 2025. Reusing that local file closes the earlier web-download gap without redownloading it. Exact SHA-256: `059a0bffc546e8588f1d9487ddb16344e7c24c559bc54dfa104979f98e223d3c`. Extraction alone is not full reading; record page coverage separately.

Systematic reading through chunk 041 covers root documents 00–22 and the first evidence JSON records. It does not yet cover all 195 documents.

## Bổ sung từ chunk045–050, ngày 2026-09-20

Các nhận xét dưới đây đề xuất sửa diễn giải, không sửa tệp của người dùng:

- `docs/benchmarking/Kết quả benchmark.md:63`: B1 không được tùy ý đổi xe/điểm đón khách đã nhận. B1 dùng chung generator và mô hình tuyến, còn physical windows/max-ride; acceptance đứng trước cost. Vì vậy không mô tả baseline là tự do hoàn toàn hoặc chỉ tối thiểu chi phí.
- Các diễn giải burden chỉ là ETA tăng (line31/91) không khớp định nghĩa absolute variation trong PromiseDeltaCalculator. Dữ liệu một panel chỉ có late revisions không thay đổi định nghĩa của metric. B1 vẫn có publication ledger để đo, không phải “không hứa gì” (line329).
- Line250 quy phần lớn service loss cho ba khóa xe/điểm đón/pickup ETA là suy luận vượt bằng chứng: hạn chế xe/điểm đón đã chung với B1, còn objective cũng khác. Cần thí nghiệm kiểm soát để tách nguyên nhân.
- Line321: biến thể nopickuplock bỏ khóa pickup ETA, không phải cho phép thay địa điểm đón. Kết quả các arm giống nhau chỉ cho thấy chưa phân biệt tại những cấu hình và dữ liệu đã thử; không chứng minh các cơ chế ấy nói chung vô tác dụng.
- Pickup sớm hơn không tự động tốt hơn cho hành khách (line301): có thể đụng lịch sẵn sàng của họ. Không gán lợi ích hành vi khi chưa có giả định và dữ liệu.

H6 rerun với adapter đã sửa khớp các số tổng hợp được công bố. Adapter bytes nguyên bản không còn để tái dựng, nên không tuyên bố tái lập byte-exact toàn bộ bản chạy gốc. Baseline B1 vẫn là đối chứng nội bộ có giới hạn, không đại diện tối ưu mạnh nhất của văn liệu.
