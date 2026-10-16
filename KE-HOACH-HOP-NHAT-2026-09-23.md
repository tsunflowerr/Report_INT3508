# RideBound — Kế hoạch hợp nhất

**Ngày lập:** 2026-09-23
**Người thực hiện:** Trần Quang Thành — 23020155 — K68I-IT2, UET/VNU
**Thay thế:** `KE-HOACH-NGHIEN-CUU-2026-09-22.md` (bản của Claude) và
`ridebound-scratchpad/conduct-outcome-plan-2026-09-22/KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md`
(bản của Codex). Hai bản cũ giữ nguyên để tra lịch sử; **khi mâu thuẫn, tệp này thắng**.
**Trạng thái:** kế hoạch, chưa authorize execution. Không tệp nào trong `E:\Code\RideBound` bị
thay đổi khi lập kế hoạch này.
**Sửa đổi 1 (2026-09-23, sau vòng phản biện ngoài):** Định lý 4 phát biểu lại có điều kiện (*"không bao
giờ là nguyên nhân"*, giả thiết (N)) và thêm Hệ quả 4.3 về chiều trôi; Tầng 2 tách thành **2A** (xác
nhận cơ chế trên panel A, đủ 20 ô) và **2B** (**tập giữ lại** — panel phát triển, ngày 12–13/11, khung
sáng và khung tối có tắc đường giảm thật); thêm nhánh hạn chót hai chiều; thêm một thay đổi mã chỉ để
chẩn đoán lý do no-op bị loại; bằng chứng chính là dự đoán theo ô đã niêm phong, giá trị p chỉ là mô tả
phụ; sổ cái "chỉ tính phần gây hại" chuyển thành hướng phát triển kèm số đo. Chi tiết ở §2.1; kiểm chứng
mới ở K17–K22.

---

## 0. Cách dùng tài liệu này

Tài liệu được viết để một lập trình viên hoặc một trợ lý AI **chưa từng đọc lịch sử hội thoại**
có thể cầm lên và làm. Mọi khẳng định về mã nguồn đều kèm `tệp:dòng` và đã được đọc trực tiếp
trong đợt lập kế hoạch này, trừ khi ghi rõ *"theo SOURCE-FINDINGS của Codex, chưa đọc lại"*.

| Ký hiệu | Nghĩa |
|---|---|
| ✅ | Đã kiểm chứng trực tiếp trong mã hoặc trên dữ liệu niêm phong trong đợt này |
| 📎 | Lấy từ `SOURCE-FINDINGS.md` của Codex; nhất quán với phần mã đã đọc nhưng chưa đọc lại từng dòng |
| ⚠️ | Cổng: rào cản kỹ thuật hoặc quản trị phải vượt trước |
| ❌ | Đã loại, kèm lý do |
| 🔬 | Cần chạy mô phỏng mới |
| ✍️ | Chỉ viết, không tốn lần chạy nào |

**Thứ tự đọc tối thiểu trước khi làm bất cứ việc gì:** §1 → §2 → §5.2 → §7.1.

---

## 1. Quyết định

### 1.1 Một câu

> Đóng góp của khóa luận **không** nằm ở chỗ "có bảo đảm lời hứa cho từng khách" (Elmi và cs.
> 2026 đã có) hay ở chỗ "chặn tổng biến thiên" (trên hệ này nó trùng với chặn hai đầu). Nó nằm
> ở chỗ: **trong các họ ràng buộc lời hứa — theo hành vi, theo hạn chót, theo kết quả nhìn thấy —
> chỉ ràng buộc theo hành vi không bao giờ tự nó là nguyên nhân làm rỗng tập phương án khi thế
> giới trôi dạt.** Tập phương án vẫn có thể rỗng hoặc lần chạy vẫn có thể hỏng vì những ràng buộc
> không thuộc cơ chế cam kết (cấu trúc lộ trình, bất biến vòng đời khi đón muộn), nhưng không bao
> giờ vì ngân sách hành vi. Đây là Định lý 4 ở §5.2. Nó phân biệt khóa luận với Schulz & Pfeiffer
> 2026 bằng một phát biểu chứng minh được, không phải bằng một thước đo khác. Chứng minh của nó
> sơ cấp; giá trị nằm ở việc đặt các họ cổng vào cùng một khung để so được, và ở kiểm chứng
> thực nghiệm.

### 1.2 Kế hoạch bốn tầng — dừng ở tầng nào cũng có một khóa luận hoàn chỉnh

| Tầng | Nội dung | Lần chạy mới | Công sức ước lượng |
|---|---|---|---|
| **0** | Sửa hồ sơ: mọi lỗi đã biết trong báo cáo LaTeX, kể cả lỗi do trợ lý gây ra | 0 | 2–4 ngày |
| **1** | Phân tích bổ sung trên 558 lần chạy đã niêm phong | 0 | 1–2 ngày |
| **2** | Thí nghiệm xác nhận rẻ: nhánh hạn chót dưới trôi dạt Manhattan thật, kiểm Định lý 4 — gồm **2A** xác nhận cơ chế (panel A) và **2B** xác nhận trên tập giữ lại (panel phát triển, sáng + tối) | ~240 | ~1,5 tuần |
| **3** | Lõi nhận biết thất bại + thế giới ngẫu nhiên có kiểm soát + hiệu chỉnh xác suất theo episode | nhiều | 4–10 tuần |
| **4** | Thiết kế lại đối tượng lời hứa (WP15, đã khóa sẵn trong kho) | — | bài báo riêng |

Công sức là **ước lượng thô** cho một người đã quen kho mã, chưa gồm thời gian chờ quyết định.

### 1.3 Nếu chỉ đọc được một bảng

| Câu hỏi hội đồng | Trả lời, kèm bằng chứng |
|---|---|
| "Elmi 2026 đã bảo đảm lời hứa cho từng khách rồi?" | Họ bảo đảm bằng cách **cấm tuyệt đối** cho một nhóm và **phân phối lại** gánh nặng (người bị đụng chịu nặng gấp 4,5 lần). Họ viết rằng bảo đảm *"would not be possible if even a single change were allowed"*. Khóa luận cho phép thay đổi mà vẫn có bảo đảm, và **xóa** 99,8% gánh nặng. Mạng của họ tĩnh nên không có phần trôi dạt để tách. |
| "Schulz 2026 cũng có trần dịch chuyển rồi?" | Trần của họ là **hạn chót tính từ lời hứa đầu**. Định lý 4: dưới trôi dạt, chính phương án giữ nguyên tuyến có thể vi phạm hạn chót, nên hạn chót có thể là nguyên nhân làm rỗng tập phương án; trần hành vi thì không bao giờ là nguyên nhân. Dự đoán hậu nghiệm từ dữ liệu sẵn có: ở trôi dạt sáng Manhattan thật, hạn chót 30 s khả thi **0/9 ô**, trần hành vi 30 s **không ô nào vô nghiệm do cam kết** (nhánh hành vi vẫn chết 11/20 ô, nhưng vì bất biến cửa sổ đón, không phải vì cam kết). Định lý còn dự đoán điều ngược lại vào **buổi tối** khi tắc đường giảm: hạn chót một chiều sẽ **an toàn**, còn cổng kết quả và hạn chót hai chiều thì không. Cả hai chiều được kiểm trên tập giữ lại chưa từng dùng (Tầng 2B). |
| "Khách đâu quan tâm lỗi do ai?" | Đúng, nên khóa luận báo cáo cả cái khách thấy: dưới trần hành vi 30 s, **99,7%** khách có tổng biến động nhìn thấy dưới 30 s, cực đại **38,7 s**. Đây là quan sát mô tả trên panel tĩnh, không phải bảo đảm xác suất (§8). |
| "`B = A + d` có đúng không?" | Không, đó là bất đẳng thức `B ≤ A + d`. Dấu bằng hỏng ở 47,9% số lần công bố mà cả hai thành phần khác 0. Phần hụt toàn cục 0,0748% — nhỏ hơn sàn diễn giải hai bậc độ lớn. Bằng chứng mạnh hơn là tính bất biến của `d` theo chính sách. |

---

## 2. Sổ kiểm chứng — mọi điểm hai bản kế hoạch mâu thuẫn hoặc khẳng định về mã

Mỗi dòng: ai khẳng định, kiểm chứng thế nào, kết luận.

| # | Khẳng định | Nguồn | Cách kiểm | Kết luận |
|---|---|---|---|---|
| K1 | `A = |p − e|` là **đối xứng**, không phải một chiều | Codex | ✅ `PromiseDeltaCalculator.cs:75-78` gọi `CalculatePair(exogenous, proposed)`; `:259-262` `AbsoluteDifference` là `|a−b|` | **Codex đúng.** Tài liệu `wp14r-013` giải thích sai. Đoạn "quy ước một chiều" Claude viết vào Chương 3 ngày 21/09 **sai** — **đã sửa** ngày 23/09 |
| K2 | Trên panel, có quyết định nào kéo lời hứa sớm hơn `e`? | Claude | ✅ `signcheck.py`: dấu `p − e` xác định hoàn toàn ở 476/476 ca `A,d>0` | **0/479** ở B1, **0/11** ở C1. Số liệu khóa luận không sai; chỉ lời giải thích sai |
| K3 | `e` chiếu trên trạng thái đã giảm **cả lô sự kiện**, nên `d` không phải giao thông thuần | Codex | ✅ `CommitmentDecisionValidator.cs:316-340` dùng `context.ReducedState.Run`, `.TravelTimes`, `.SimulationTime` | **Codex đúng.** Mọi chỗ gọi `d` là "do giao thông" phải đổi thành "phần thay đổi khi chiếu lại tuyến giữ nguyên". **Đã sửa** đoạn giả dược ở Chương 3 |
| K4 | Mô hình chọn và kiểm bằng chứng đều đòi **đúng một no-op hợp lệ mỗi xe** | Codex | ✅ `CandidateSelectionModel.cs:276-279`; ✅ `DecisionMessages.cs:1113-1121` đòi thêm `IsNoOp && IsEligible` | **Codex đúng.** Mọi cổng có thể loại no-op (kết quả, hạn chót) sẽ làm hỏng run thay vì ghi nhận vô nghiệm |
| K5 | Nhánh hạn chót dưới trôi dạt "gate 60 khách" | Claude (bản 22/09) | ✅ K4 + K2 + thông điệp lỗi tiền lệ | **Claude sai về cơ chế.** Vì bộ sinh không bao giờ kéo sớm, khi no-op vi phạm thì mọi phương án vi phạm ⟹ xe không còn ứng viên ⟹ run chết với `"C1 rejected every generated candidate for this vehicle"`. Đại lượng đo đúng là **tỉ lệ ô vô nghiệm**, không phải số khách bị chặn |
| K6 | Có thể đo nhánh hạn chót **mà không** cần viết lại lõi | tổng hợp | ✅ K5 + bộ phân loại `run_drift_frac.py:101-107` đã nhận thông điệp đó là `commitment` | **Đúng cho hạn chót một chiều.** Chỉ cần thêm luật hạn chót (T2.1 thay đổi 1–5). Không cần đổi mô hình no-op. Hạn chót hai chiều và cổng kết quả dưới trôi thuận lợi đi đường khác (K20) ⟹ thêm thay đổi 6, chỉ để chẩn đoán |
| K7 | Kiểm định DKW với `n = 1.581` khách | Claude (bản 22/09) | lập luận | **Claude sai — giả lặp.** Khách trong một ô chịu chung trạng thái đội xe và trôi dạt, không độc lập. Đơn vị độc lập là **ô/episode**. Thay bằng hiệu chỉnh conformal theo episode (§8.3) |
| K8 | "Manhattan" thực chất là đồ thị đầy đủ dựng từ snapshot OD đầu tiên | Codex | ✅ `actual_fleetpy_medium_preflight.py:113-139`: `pos_x = index*1000, pos_y = 0`, `is_stop_only = True`, `distance = seconds*10` | **Codex đúng.** Phải khai báo trong báo cáo: dữ liệu nhu cầu là thật, mạng là bao đóng metric OD trên ≤96 nút đã chọn |
| K9 | Verifier medium đòi `travelSnapshotVersion == 1` | Codex | ✅ `actual_fleetpy_medium_verify.py:1158` | **Codex đúng.** Toàn bộ các lần chạy trôi dạt **chưa qua verifier của dự án** — phải gắn nhãn thăm dò |
| K10 | Cơ chế trôi dạt có thật sự đến được runner? | Claude | ✅ docstring `preflight_drift.py:1-49`: đặt `_current_tt_factor`, xóa cache, dựng cờ `_rb_travel_dirty` ⟹ bridge phát `travelTimesUpdated` | **Có.** Mô hình thông tin là "dự báo = điều kiện hiện tại", hệ số **vô hướng toàn mạng, đơn điệu tăng** (đỉnh sáng thật +17–26%) |
| K11 | Khiếm khuyết `worst-hard-utilization-ppm` | cả hai | ✅ `HardVectorCandidateAssessor.cs:316-331` | Đồng thuận. **Kho đã ghi nhận từ 2026-08-25** (`docs/handoffs/wp14-continuation-2026-08-25.md:107-109`) |
| K12 | "Sửa ppm trước mọi cơ chế mới" | Claude (bản 22/09) | lập luận + nguyên tắc A01 của Codex | **Claude sai.** Khiếm khuyết làm mọi nhánh cùng rơi về "nhận khách → chi phí", tức hàm mục tiêu **tự nhiên khớp nhau**. Sửa nó làm thứ hạng phụ thuộc cơ sở tính của từng nhánh ⟹ tạo nhiễu so sánh. Sửa ppm là **một ablation độc lập**, không phải tiền điều kiện |
| K13 | Đổi `budgetBasis` không đổi vector xếp hạng theo hành vi | Codex | 📎 nhất quán với `SolverBackedFleetSelection.cs:300-312` | Đúng. Nhưng vì tầng `revision` khác 0 **0/7.430** lần (✅ `objorder.py`), nhiễu này gần bằng 0 trên thực tế |
| K14 | B5 không phải MPA thật (sinh một lần từ trạng thái hiện tại) | Codex | 📎 | Chấp nhận. Mục "plan pool" của bản 22/09 bị đánh giá thấp chi phí |
| K15 | Bằng chứng 160/160 của WP14R-013 có thật và đã commit? | Claude | ✅ `git show 41a4e11:…wp14r-013…md` dòng 53; JSON `designedJobCount=160, observedJobCount=160, missingJobCount=0` | **Có.** Bản prose trong cây làm việc có thêm 38 dòng chưa commit của người dùng — phải giữ nguyên |
| K16 | Runner dùng cho các lần chạy trôi dạt | Claude | ✅ `run_drift.py:59` | `E:/RideBoundData/wp9/runner/h6-confirmatory-v1` (runner niêm phong H6) |
| K17 | Có tập ô **chưa từng dùng** để dựng dự đoán trôi dạt không? | vòng phản biện ngoài | ✅ `benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1/`: 16 ô `d201811{12,13}-s10-r{1..4}-w{08,17}`; `commitmentPolicyId = wp6-synthetic-policy-overlay-v1` trong `scenario-content.json` và driver, giống panel A; `sourceWindowStartSeconds` = 28800 (`w08`) và 61200 (`w17`) trong `normalizer-configuration.json`; driver ở `benchmarks/scenarios/wp14-development/<ô>.driver.json`; hệ số giao thông ngày 12, 13/11 có sẵn | **Có.** Mọi dự đoán trôi dạt đến nay dựng từ ngày 14–18/11. Panel này đã chạy trong ma trận v6 nhưng **không có trôi dạt**, nên hành vi dưới trôi dạt chưa ai nhìn thấy. Dùng làm tập giữ lại (Tầng 2B) |
| K18 | Trôi dạt thật có đoạn không đơn điệu tăng không? | vòng phản biện ngoài | ✅ cột `travel_time_factor` của `2018-11-{12..18}_tt_factors.csv` (bước 15 phút), tỉ số cuối/đầu khung — sáng 08–10h: **×1,14 / ×1,15** (ngày 12, 13), ×1,17–1,26 (ngày 14–18); tối 17–19h: **×0,84 / ×0,87** (ngày 12, 13), ×0,82 / ×0,80 / ×0,86 (ngày 14, 15, 18), gần phẳng ×0,99 / ×1,04 (ngày 16, 17). Đầu khung tối **nhích lên nhẹ** 15–30 phút (ngày 12: 3,19 → 3,24, ≈ +1,6%; ngày 13: 3,78 → 3,80) rồi mới giảm | **Có, trong dữ liệu thật.** Không cần tạo profile giả. Hai ngày của panel phát triển đều có khung tối giảm rõ. Đoạn nhích đầu khung là lý do dự đoán buổi tối phải tính theo từng khách từ đường đi thật, không suy từ tỉ số khung |
| K19 | Sổ cái "chỉ tính phần gây hại" `h = max(0, |p−p₀| − |e−p₀|)` có khác sổ cái hiện tại trên dữ liệu không? | vòng phản biện ngoài | ✅ `harmledger.py` (chạy lại 23/09): B1 `A > 0` ở 479 lần công bố; tổng `A` 64.863,1 s vs tổng `h` 64.821,2 s; `h ≠ A` ở 158 lần (33,0%) nhưng tổng chỉ chênh **41,9 s (0,06%)**; **cùng 403 khách** bị tính | **Gần như trùng về tổng.** Vì bộ sinh không bao giờ kéo sớm (K2), không có hành động sửa chữa nào được miễn. Hướng phát triển, không cài bây giờ |
| K20 | Khi cổng loại no-op nhưng **vẫn còn** ứng viên khác thì run hỏng thế nào? | Claude | ✅ `HardVectorCandidateAssessor` vẫn trả tập đã lọc nếu `retained.Count > 0`, kể cả khi no-op bị loại; `CandidateSelectionModel.cs:276-279` trả `INVALID_CANDIDATE_SELECTION_PROBLEM` với `"Each vehicle must have candidate options and exactly one no-op option."`; `SolverBackedFleetSelection.cs:368-398, 99-101` bọc thành `SOLVER_MODEL_MAPPING_FAILED`, **không có đường lùi**; ⚠️ chặng cuối tới `failure-00.json` chưa đọc | Xảy ra với **hạn chót hai chiều** (no-op sớm quá `l`, trong khi một ứng viên chèn thêm khách làm muộn lại lọt vào cửa sổ) và với **cổng kết quả** khi trôi dạt sớm (no-op có `B = d > κ`, ứng viên làm muộn có `z = x + c ≈ 0`). Không lần chạy nào **đang thành công** đi qua đường này ⟹ biến nó thành lỗi có mã riêng (T2.1 thay đổi 6) không đổi kết quả nào hiện có |
| K21 | 9 ô dùng cho dự đoán ở k=1 có phải mẫu không thiên lệch? | Claude (vòng phản biện) | lập luận | **Không.** Đó là các ô **sống sót dưới nhánh hành vi** — chọn theo kết quả của một nhánh can thiệp. Phân tích chính phải dùng **đủ mọi ô** với kết quả phân loại |
| K22 | Buổi tối xe đến sớm có làm `Board()` hỏng ngay cả ở nhánh hành vi không? | Claude | ✅ tiếp hợp truyền `earliest_pickup_time_dict` vào `BoardingPlanStop` (`simulators/fleetpy-ridebound/ridebound_fleetpy/fleet_control.py:954`); bộ chiếu lịch chờ tới `EarliestPickup` (`RouteScheduleProjector.cs:163`) | **Phần lớn đã chặn** — FleetPy không đón trước thời điểm đón sớm nhất. Vẫn chạy thử một ô tối trước khi chạy cả panel (R11) |

**Tổng kết sổ kiểm chứng:** trong các điểm có thể kiểm trực tiếp, Codex đúng ở K1, K3, K4, K8,
K9; Claude đúng ở K2, K6, K10, K15, K16 và sai ở K5, K7, K12. Không bên nào đủ một mình. Vòng phản
biện ngoài (K17–K22) mở ra tập giữ lại và phép thử hai chiều, cả hai đều đã có sẵn trong dữ liệu.

### 2.1 Vòng phản biện ngoài (2026-09-23) — đã nhận gì, sửa gì

| Góp ý | Quyết định | Cách xử lý trong bản này |
|---|---|---|
| Định lý 4 phát biểu quá mạnh — phải có điều kiện | **Nhận, và gấp hơn góp ý nói:** chính nhánh hành vi chết 11/20 ô ở k=1 vì `window-wall`. Điều chỉnh cơ chế: ADR-045 đã **miễn** cửa sổ dịch vụ cho no-op ở bước sinh phương án, nên no-op không bị loại vì cửa sổ; cái chết nằm ở `RideRequest.Board()` khi xe đón muộn thật | §1.1, §1.3, §5.2 phát biểu lại: cổng hành vi **không bao giờ là nguyên nhân** làm rỗng tập phương án |
| Dự đoán dựng và kiểm trên cùng 9 ô ⟹ không phải kiểm định độc lập | **Nhận.** Thêm hai vấn đề: 9 ô bị chọn theo kết quả nhánh hành vi (K21); giá trị p trên kết quả gần như tất định chỉ mang tính trình diễn | Tầng 2 tách **2A** "xác nhận cơ chế có đối chứng" và **2B** "xác nhận trên tập giữ lại" (K17); phân tích chính trên đủ mọi ô; giá trị p chỉ là mô tả phụ |
| Trôi dạt đơn điệu tăng có lợi cho Định lý 4 — nên thêm profile lên-xuống | **Nhận mục tiêu, không nhận cách làm.** Profile tự tạo mời lại đúng lời phê "thiết kế thế giới cho vừa định lý" | Dùng **khung tối thật** có tắc đường giảm (K18). Định lý đoán **cả** lúc hạn chót một chiều thất bại (sáng) **lẫn** lúc nó an toàn (tối) — một phép thử phân biệt thật |
| Sổ cái chỉ tính phần gây hại, sửa được CE-3 | **Nhận là hướng phát triển.** Toán đúng: `h ≤ A` theo bất đẳng thức tam giác, no-op có `h = 0`. Nhưng đo được chênh 0,06% trên hệ hiện tại (K19). Về tính mới: `docs/03` ghi *anticipatory walking 2026* đã có cơ chế "no-worse so với lịch tham chiếu" cho một lần cập nhật | Chương 5 (T0.2.11), kèm số đo; không cài ở Tầng 2 |
| Bảo đảm hai lớp là tùy chọn | Đã đúng như vậy | Giữ ở Tầng 3 |
| Chứng minh sơ cấp | Đồng ý | Giữ tên "Định lý 4" cho nhất quán với 3.1–3.2 (cũng chứng minh một dòng); nói thẳng trong bài rằng chứng minh sơ cấp |

---

## 3. Đánh giá kế hoạch cũ của Claude (2026-09-22)

### 3.1 Cái đúng và nên giữ

1. **Nền định lượng.** Chín phép đo trên bằng chứng niêm phong — độ khít phân rã, tính không
   chia được của nhu cầu dịch chuyển, 83,8% gánh nặng rơi trước khi đón, đuôi và CVaR, bẫy Gini,
   mẫu số đúng cho độ mỏng tập lựa chọn. Kế hoạch Codex hầu như không có con số nào từ dữ liệu.
2. **Tín hiệu duy nhất cho thấy hướng này có răng.** Dưới trôi dạt k=1, 60 khách có độ lệch hai
   đầu vượt 30 s trong khi thành phần hành vi của cả 583 khách chỉ là 27 s. Đây là bằng chứng sơ
   bộ duy nhất rằng phân biệt hành vi/kết quả tạo khác biệt vận hành.
3. **Nhận thức quản trị.** WP15 đã khóa sẵn thiết kế trong `docs/tasks/47`; `docs/18` đang lạc
   hậu; chuỗi phụ thuộc WP14R → ADR → WP15; câu *"WP15 không bắt buộc phải tồn tại để bài báo
   đứng được"*.
4. **Lối đóng khóa luận không tốn lần chạy nào.** Kế hoạch Codex không có lối này.
5. **Định vị cạnh tranh sắc:** phân phối lại (Elmi) so với xóa (RideBound).

### 3.2 Cái sai — phải nói thẳng

| Lỗi | Hậu quả nếu làm theo | Sửa |
|---|---|---|
| DKW với `n = 1.581` khách (K7) | Một khoảng tin cậy hẹp giả tạo; hội đồng có chuyên môn thống kê sẽ bác | Episode là đơn vị; conformal theo episode |
| "Quy ước một chiều" của `A` (K1) | **Đã lọt vào Chương 3.** Mô tả sai mã và che mất giới hạn thật của cơ sở hành vi (có thể phạt một sửa chữa có lợi) | Đã sửa ngày 23/09 |
| Nhánh hạn chót "gate 60 khách" (K5) | Chạy xong sẽ thấy run chết thay vì số khách; kết luận sai cơ chế | Đổi đại lượng đo sang tỉ lệ ô vô nghiệm |
| "Sửa ppm trước" (K12) | Tạo nhiễu so sánh giữa các nhánh | Tách thành ablation độc lập |
| `d` = "do giao thông" (K3) | Phép thử giả dược phát biểu như định lý trong khi chỉ là tính chất thực nghiệm | Đã sửa ở Chương 3 |
| Không khai báo đồ thị đầy đủ (K8) và trôi dạt chưa qua verifier (K9) | Người đọc tưởng kết quả trên mạng đường thật và đã được kiểm chứng | Thêm vào phần hạn chế |
| Đánh giá thấp chi phí "plan pool" (K14) | Hứa một thí nghiệm không làm nổi | Hạ xuống tầng 3, kỳ vọng thấp |
| Cảnh báo "ppm làm nhánh chọn lọc không diễn giải được" | Quá mức: mọi cấu hình đều giữ trần 0 trên ba chiều switch, nên ppm hằng số với **mọi** khách | Bỏ cảnh báo đó |

### 3.3 Cái thiếu

- Phân loại trạng thái thất bại (vô nghiệm do cổng, suy thoái do thế giới, tìm kiếm chưa xong,
  quan sát sai, vật lý bất khả) — Codex §12 làm rất tốt.
- Nguyên tắc **hàm mục tiêu khớp nhau** khi so các cổng — Codex A01.
- Thiết kế **số ngẫu nhiên dùng chung** cho thế giới thí nghiệm — Codex §8.2.
- Mọi ước lượng công sức.

---

## 4. Đánh giá kế hoạch của Codex (2026-09-22)

### 4.1 Cái đúng và nên giữ

1. **Đọc mã rộng và sâu nhất.** `SOURCE-FINDINGS.md` phủ Domain, Application, Algorithms,
   Runner, Contracts, Benchmarking, adapter FleetPy và RidePy, cùng phần lớn bộ test.
2. **Thống kê đúng đơn vị** (K7). Quy tắc thứ hạng conformal chuẩn, `n ≥ 19` cho `α = 0,05`,
   và phép tính **59 episode không lỗi** mới đủ cận trên 5% — cả hai tôi đã tính lại và khớp.
3. **Hai phản ví dụ bắt buộc**, trong đó có ca "sửa để giữ lời hứa" (`v=600, e=720, p=600` ⟹
   `C=120, V=0`) — một giới hạn thật của cơ sở hành vi.
4. **Tách `x` khỏi "giao thông thuần"** (K3).
5. **Bắt được rào cản no-op** (K4) mà kế hoạch Claude bỏ sót hoàn toàn.
6. **Phân loại thất bại và máy trạng thái phục hồi** (§12): không đánh đồng "cổng loại hết" với
   `INTERNAL_ERROR`, không reset sổ cái khi phục hồi, không loại episode phục hồi sau khi xem kết
   quả rồi vẫn giữ lời bảo đảm.
7. **Thiết kế thế giới thí nghiệm:** số ngẫu nhiên khóa theo `(worldSeed, edgeId, timeBin,
   componentId)`, không phụ thuộc số lần chính sách hỏi; tách dữ liệu thật của thế giới khỏi dự
   báo; kiểm FIFO (Ichoua, Gendreau & Potvin 2003).
8. **Bảng claim trung thực** (§18.3) và **quy tắc dừng** (§17.5).

### 4.2 Cái sai hoặc yếu — phải nói thẳng

| Điểm yếu | Vì sao là vấn đề | Cách xử lý trong kế hoạch này |
|---|---|---|
| **Không có lối đóng khóa luận.** P0–P9 là một chương trình nhiều tháng | Báo cáo 66 trang đã viết xong; một khóa luận cử nhân có hạn nộp | Tầng 0–1 đóng khóa luận với 0 lần chạy |
| **Bỏ trắng 558 lần chạy hiện có.** §2.2: *"mọi kết quả số mới phải từ bản chạy mới"* | Đúng về kỷ luật nhưng bỏ qua tín hiệu duy nhất đang có (k=1) | Dùng bằng chứng cũ để **đặt giả thuyết tiền đăng ký**, không để kết luận |
| **Nhánh hạn chót buộc phải chờ viết lại lõi** (P3 đứng trước P2 về thực chất) | Với bộ sinh chèn thuần, vô nghiệm do hạn chót hiện ra đúng bằng đường fail-closed có sẵn (K6) | Tầng 2 đo được ngay, không cần lõi mới |
| **MVP chuyển sang mạng tổng hợp 3–8 nút** (§11.2) | Mất tính hợp lệ ngoài — thế mạnh "dữ liệu Manhattan công khai thật" của khóa luận | Giữ hệ số trôi dạt Manhattan đo thật làm thế giới v0; mạng nhỏ chỉ dùng cho oracle vi mô |
| **Không đụng tới thiết kế WP15 đã khóa** | Kho đã quyết định trục B (cửa sổ theo quantile) và trục C (horizon theo vòng đời) | Tầng 4 trỏ thẳng tới `docs/tasks/47` |
| **Thiếu Định lý 4** | Bỏ lỡ kết quả thống nhất ĐL 3.1/3.2 và tách khỏi Schulz | §5.2 |
| **Không có ước lượng công sức** (§19 tự thừa nhận) | Không lập lịch được | §11 |
| **Không nhắc bẫy Gini** | Chỉ số công bằng tương đối nói C1 *tệ hơn* B1 | §6.2 T1.4 |

---

## 5. Nền tảng — phải khóa trước khi viết một dòng mã nào

### 5.1 Định nghĩa

Xét một hành khách còn hoạt động và một tọa độ ETA vô hướng (mặc định: giờ trả khách). Ở mỗi
lần công bố `t`:

| Ký hiệu | Định nghĩa chính xác | Nguồn trong mã |
|---|---|---|
| `v_t` | ETA của lời hứa đang hiệu lực trước quyết định | `priorHistory.Current.PublishedPromise.Projection` |
| `e_t` | ETA khi chiếu **tuyến đang giữ** trên **trạng thái đã giảm toàn bộ lô sự kiện** của kỷ nguyên `t` | `CommitmentDecisionValidator.cs:316-340` |
| `p_t` | ETA trong phương án được chọn để công bố | `candidateProjection` |
| `p_0` | ETA của lời hứa **đầu tiên** | `history.Entries[0]` — luôn là `CommitmentLedgerEntryKind.InitialPromise` |

Ba hiệu **có dấu** và ba đại lượng **không dấu**:

```
x_t = e_t − v_t        (thay đổi khi chiếu lại tuyến giữ nguyên)     d_t = |x_t|
c_t = p_t − e_t        (thay đổi do quyết định)                       A_t = |c_t|
z_t = p_t − v_t        (thay đổi khách nhìn thấy)                     B_t = |z_t|
```

Đồng nhất có dấu, luôn đúng: `z_t = x_t + c_t`.

⚠️ **Không gọi `x_t` là "tác động của giao thông".** Nó gồm mọi thứ đổi trong lô khi giữ tuyến:
tiến độ thực của xe, độ trễ thực thi, cập nhật thời gian di chuyển, và các sự kiện vòng đời khác
(K3). Chỉ trong một ca vi mô cô lập mới được quy toàn bộ `x_t` cho một nhiễu giao thông đã biết.

Cộng dồn theo một hành khách, trên cùng lưới công bố:

```
C = Σ A_t        X = Σ d_t        V = Σ B_t
E  = |p_T − p_0|                          độ lệch hai đầu
M  = max_t |p_t − p_0|                    độ lệch cực đại so với lời hứa đầu
M⁺ = max_t max(0, p_t − p_0)              phần muộn cực đại — đúng thứ một hạn chót kiểu Schulz chặn
```

Nếu chuỗi công bố liên tục (`v_t = p_{t−1}`) thì `V` chính là tổng biến thiên của chuỗi ETA công
bố.

### 5.2 Các kết quả lý thuyết

**Mệnh đề 1 (chuỗi đại lượng).** Với mọi chuỗi lời hứa **công bố liên tục** (`v_t = p_{t−1}`, tức mỗi
lần công bố so với lần ngay trước nó — điều kiện này cần cho bước `M ≤ V`):

```
max(0, p_T − p_0)  ≤  M⁺  ≤  M  ≤  V  ≤  C + X        và        E ≤ M
```

*Chứng minh:* `max(0,·) ≤ |·|`; lấy cực đại trên tiền tố; bất đẳng thức tam giác cộng dồn cho
`|p_t − p_0| ≤ Σ_{s≤t} |z_s| ≤ V`; cộng dồn `|z_t| ≤ |c_t| + |x_t|`. ∎
Kiểm số ✅ trên bốn nhánh B1, C1, trôi dạt k0, k1 (`tvcheck.py`, `drifttv.py`).

> Bản thân các bất đẳng thức này là kiến thức cơ bản, **không** phải đóng góp. Đóng góp nằm ở
> Định lý 4, là cách *dùng* chúng.

---

**Định lý 3.1 (giữ nguyên).** Dưới cơ sở hành vi, tập phương án của một xe không bao giờ bị làm
rỗng bởi ràng buộc cam kết. *Chứng minh:* no-op có `p = e` ⟹ `A = |e − e| = 0`. ∎

**Định lý 3.2 (giữ nguyên).** Dưới cơ sở kết quả, tồn tại trạng thái mà tập phương án bị làm
rỗng. *Chứng minh:* no-op có `B = |e − v| = d`; nếu sổ cái cộng `d` vượt `β` thì no-op bị loại. ∎

**Định lý 3.3 (đã sửa ngày 21/09, có điều kiện).** Giả sử điều kiện **(H)**: `|p − e| ≤ |p − v|`
ở mọi lần công bố. Khi đó tập quỹ đạo khả thi dưới cơ sở kết quả là tập con của tập quỹ đạo khả thi
dưới cơ sở hành vi, nên **chính sách tối ưu** dưới cơ sở kết quả không phục vụ nhiều khách hơn.
Định lý **không** nói gì về bộ giải tham lam đang cài. (H) hỏng ở 0,42% số lần công bố của B1 ✅.

---

**Định lý 4 (thứ tự khả thi của các họ cổng) — MỚI, trung tâm của kế hoạch.** *Sửa đổi 1: phát
biểu lại có điều kiện; bản cũ ("chỉ cổng hành vi không bao giờ làm rỗng tập phương án") quá mạnh.*

**Phạm vi của định lý — đọc trước.** Định lý chỉ nói về **phần cam kết** của bộ lọc. Tập phương
án của một xe còn có thể rỗng, hoặc lần chạy còn có thể hỏng, vì những thứ **không** thuộc cơ chế
cam kết: cấu trúc lộ trình, sức chứa, và nhất là **bất biến vòng đời khi đón muộn thật**. Thực tế
đã xảy ra: dưới trôi dạt sáng k=1, chính nhánh hành vi 30 s chết **11/20 ô** vì `window-wall`. Cơ
chế ✅: ADR-045/047 đã **miễn** kiểm cửa sổ dịch vụ cho no-op ở bước sinh phương án
(`ServiceQualityAllowance`), nên no-op **không** bị loại vì cửa sổ; lần chạy chết muộn hơn, khi xe
tới điểm đón sau `LatestPickup` và `RideRequest.Board()` từ chối (`RideRequest.cs:266-273`,
*"Actual pickup time must remain inside the accepted pickup window."*). Đó là bất biến của miền,
không phải ràng buộc cam kết.

Vì vậy gọi **(N)** là giả thiết: *tại kỷ nguyên đang xét, no-op của xe đã qua mọi kiểm tra
không thuộc cam kết.* Định lý 4 nói về cái xảy ra **sau** (N).

Xét **quỹ đạo dự phòng**: tại mọi kỷ nguyên, xe giữ nguyên tuyến (chọn no-op). Trên quỹ đạo này
`p_t = e_t`, nên `c_t = 0` với mọi `t`, và do đó

```
C_noop = 0        z_t = x_t        V_noop = X
```

Gọi một **họ cổng** `G` với trần `κ` là "an toàn theo cấu tạo" nếu, dưới (N), nó không bao giờ
loại no-op, bất kể thế giới trôi dạt thế nào. Xét bốn họ:

| Họ cổng | Kiểm cái gì ở mỗi lần công bố | Ví dụ trong văn liệu |
|---|---|---|
| `C` — theo hành vi | sổ cái `Σ A_t ≤ κ` | RideBound C1 |
| `M⁺` — hạn chót một chiều | `p_t − p_0 ≤ κ` | Schulz & Pfeiffer 2026 (`l`) |
| `M` — hạn chót hai chiều | `|p_t − p_0| ≤ κ` | cửa sổ quanh lời hứa đầu |
| `V` — theo kết quả nhìn thấy | sổ cái `Σ B_t ≤ κ` | RideBound cơ sở `customerVisible` |

Khi đó ngưỡng nhỏ nhất bảo đảm no-op không bị loại dọc toàn quỹ đạo dự phòng là

```
κ*_C = 0   ≤   κ*_{M⁺} = M⁺_noop   ≤   κ*_M = M_noop   ≤   κ*_V = X
```

Và phát biểu chính:

> **(a) Mọi quỹ đạo.** Dưới (N), với mọi `κ ≥ 0`, trên **mọi** quỹ đạo — không riêng quỹ đạo dự
> phòng — cổng `C` không bao giờ loại no-op. Do đó cổng hành vi **không bao giờ là nguyên nhân**
> làm rỗng tập phương án của một xe.
>
> **(b) Quỹ đạo dự phòng.** Ba họ còn lại loại no-op ngay khi đại lượng được kiểm trên quỹ đạo dự
> phòng vượt `κ`; ngưỡng an toàn nhỏ nhất của chúng theo thứ tự trên, và **tăng theo độ trôi dạt**
> — với `M⁺` chỉ theo phần trôi **bất lợi** (Hệ quả 4.3).

Câu dùng trong báo cáo: *"Cổng hành vi không bao giờ là nguyên nhân khiến tập phương án rỗng."*
**Không** viết *"hệ thống dùng cổng hành vi không bao giờ kẹt"* — sai, xem 11/20 ô ở trên.

*Chứng minh.* (a) Giả sử sổ cái trước kỷ nguyên `t` thỏa `C_{t−1} ≤ κ` (đúng vì lần công bố trước
đã qua cổng). No-op có `c_t = 0` nên `C_t = C_{t−1} ≤ κ`. (b) No-op bị loại tại lần công bố đầu
tiên mà đại lượng được kiểm của quỹ đạo dự phòng vượt `κ`, nên ngưỡng nhỏ nhất đúng bằng giá trị đó
trên quỹ đạo dự phòng. Thứ tự giữa chúng là Mệnh đề 1 áp cho quỹ đạo có `C = 0`; bước `M ≤ V` cần
chuỗi công bố liên tục. ∎

Chứng minh **sơ cấp** — nói thẳng như vậy trong bài. Giá trị không nằm ở độ khó của chứng minh mà
ở hai chỗ: đặt ba họ cổng trong văn liệu vào cùng một khung để so được, và kiểm chứng rằng ranh
giới nó vạch ra đúng với hệ thật (Tầng 2).

**Bốn đường hỏng trong mã hiện tại, và vì sao hiện chưa quy được nguyên nhân cho no-op** ✅:

| Đường | Thông điệp | Nơi | Thuộc cam kết? |
|---|---|---|---|
| No-op không giữ được ở bước sinh | `"The active route could not be retained as the safety no-op candidate…"` | `InsertionCandidateGenerator.cs:212-228` | Không |
| Mọi phương án bị loại | `"C1 rejected every generated candidate for this vehicle. First rejection: …"` | `HardVectorCandidateAssessor.cs:188-216` | **Tùy** — xem dưới |
| No-op bị loại, còn phương án khác | `"Each vehicle must have candidate options and exactly one no-op option."` (mã `SOLVER_MODEL_MAPPING_FAILED`) | `CandidateSelectionModel.cs:276-279` → `SolverBackedFleetSelection.cs:368-398`, không có đường lùi | Có (K20) |
| Xe đón muộn thật | `"Actual pickup time must remain inside the accepted pickup window."` | `RideRequest.cs:266-273` | Không |

Chỗ hở: ở đường thứ hai, "First rejection" là ứng viên **đầu tiên theo thứ tự id**, mà id là băm
nội dung (`CandidateIdentity.Create`), nên đó thường **không** phải no-op. Lý do in ra có thể là lỗi
áp trạng thái (`CandidateStateApplicator`) chứ không phải mã `COMMITMENT_*`. Ở ranh giới chính sách,
witness còn bị rút gọn: `AssessmentFailure` (`SolverBackedRidePoolingPolicy.cs:484-493`) chỉ giữ
`Message, VehicleId, RequestId, CandidateId, Dimension`, bỏ `UnderlyingCode`. Vậy **từ artefact
chạy hiện tại không đọc ra được lý do no-op bị loại**. Tầng 2 sửa việc này bằng một thay đổi chỉ
để chẩn đoán (T2.1 thay đổi 6). Sau thay đổi đó, Định lý 4(a) cho một dự đoán kiểm được trên
artefact: **dưới cổng hành vi, không ô nào hỏng với lý do cam kết cho chính no-op**.

**Hệ quả 4.1 (vì sao hạn chót an toàn trong mô hình tất định).** Nếu thời điểm tới của tuyến giữ
nguyên không trôi — thời gian di chuyển và thực thi đều tất định — thì `x_t ≡ 0`, nên
`M⁺_noop = M_noop = X = 0` và **cả bốn họ đều an toàn**. Tính vô nghiệm chỉ xuất hiện khi lời hứa
của tuyến giữ nguyên trôi ngoại sinh. ⚠️ Trước khi phát biểu điều này *về bài Schulz & Pfeiffer*,
phải đối chiếu giả thiết thời gian di chuyển trong toàn văn của họ; hiện mới chắc chắn họ không có
cửa sổ đón và luôn nối được khách mới vào cuối tour.

**Hệ quả 4.2 (liên hệ với ràng buộc đã khóa của WP15).** `docs/tasks/47` §3 yêu cầu *"bất kỳ
policy v2 nào cũng phải bảo đảm tập khả thi không rỗng theo cấu tạo"*. Định lý 4 cho thấy trong
bốn họ trên, **xét riêng phần cam kết**, chỉ họ hành vi thỏa ràng buộc đó với mọi trần. Ba họ còn
lại chỉ thỏa khi trần lớn hơn một hàm của quỹ đạo trôi dạt — tức là **trần tối thiểu an toàn tăng
theo độ trôi dạt**. Ràng buộc WP15 cho toàn hệ còn cần (N) — tức là cần xử lý bất biến `Board()`
khi đón muộn, việc mà Định lý 4 không làm.

**Hệ quả 4.3 (phụ thuộc chiều trôi — cái cho phép kiểm định lý theo cả hai hướng).** Trên quỹ đạo
dự phòng với chuỗi công bố liên tục, `p_t = p_{t−1} + x_t`, nên `p_t − p_0 = Σ_{s≤t} x_s` và

```
M⁺_noop = max_t ( Σ_{s≤t} x_s )⁺        M_noop = max_t | Σ_{s≤t} x_s |        V_noop = Σ_t |x_t|
```

- Trôi **bất lợi** (mọi `x_s ≥ 0`, tắc đường tăng — sáng): `M⁺ = M = V`, **bằng nhau đúng**. Hạn chót
  một chiều, hai chiều, cổng kết quả **cùng** vô nghiệm ở cùng một ngưỡng.
- Trôi **thuận lợi** (mọi `x_s ≤ 0`, tắc đường giảm — tối): `M⁺_noop = 0` nên hạn chót một chiều
  **an toàn** với mọi `κ ≥ 0`, trong khi `M = V` vẫn lớn nên hạn chót hai chiều và cổng kết quả **vẫn**
  có thể vô nghiệm.
- Cổng hành vi: an toàn ở cả hai.

Trên hệ thật `x_s` không thuần một dấu — nó còn gồm tiến độ và độ trễ thực thi (K3) — nên các đẳng thức
trên chỉ đúng gần đúng; đó là lý do dự đoán ở Tầng 2 tính từ quỹ đạo đo được, không từ công thức.

Đây là điểm làm Định lý 4 **kiểm được**, không chỉ đúng: một nhận định thô kiểu *"hạn chót hỏng
khi có trôi dạt"* không đoán được buổi tối; Định lý 4 đoán đúng **họ nào** hỏng theo **chiều** trôi.
Khung tối thật không đơn điệu hoàn toàn: 15–30 phút đầu nhích lên ≈ +0,5–1,6% (K18), nên `M⁺_noop`
buổi tối **nhỏ nhưng không bằng 0** — dự đoán phải tính theo từng khách từ quỹ đạo thật (T2.8),
không suy từ tỉ số khung.

⚠️ **Hệ quả phụ của trôi thuận lợi, phải báo cáo chứ không giấu:** dưới hạn chót một chiều, một
phương án chèn khách làm muộn `c_t > 0` vẫn qua cổng khi `e_t − p_0` đủ âm — tức nhà điều hành được
**tiêu phần trôi thuận lợi** để dời khách. Cổng hành vi thì tính đủ `c_t`. Vì vậy buổi tối, nhánh
hạn chót có thể phục vụ **nhiều khách hơn** nhánh hành vi cùng trần, đổi lại khách thấy lời hứa đi
sớm rồi muộn lại. Đây là một đánh đổi thật giữa hai họ; ghi là **dự đoán phụ, thăm dò**.

**Bằng chứng sơ bộ đã có** ✅ (`cellpred.py`, trên bằng chứng `wp14/drift-v1`):

| Trôi dạt | Cực đại `D⁺` theo ô (s) | Hạn chót 30 s | 60 s | 120 s | Trần hành vi 30 s |
|---|---|---:|---:|---:|---:|
| k = 0 (tĩnh) | ≤ 28 ở cả 20 ô | 20/20 khả thi | 20/20 | 20/20 | 20/20 |
| **k = 1 (đỉnh sáng thật)** | 54, 60, 63, 78, 81, 85, 85, 87, 102 | **0/9** | **2/9** | 9/9 | **0 ô vô nghiệm do cam kết** |

Đây là **ước lượng hậu nghiệm** trên quỹ đạo đã chạy dưới cổng hành vi, dùng `D⁺` cuối làm đại
diện cho `M⁺`. Vì trôi dạt sáng đơn điệu tăng nên `D⁺ ≈ M⁺`, và vì `D⁺ ≤ M⁺` nên ước lượng **nghiêng
về phía lạc quan cho hạn chót** — thực tế có thể còn vô nghiệm nhiều hơn.

⚠️ Ba giới hạn của bảng trên, phải nói ra khi dùng:
1. **9 ô là ô sống sót** dưới nhánh hành vi ở k=1 (K21); 11 ô còn lại chết vì `window-wall` trước khi
   hết khung nên không có `D⁺` cuối. Mẫu bị chọn theo kết quả của một nhánh can thiệp.
2. Dự đoán dựng và "kiểm" trên **cùng** dữ liệu — đó là giải thích hậu nghiệm, không phải kiểm định.
3. Chỉ có trôi **bất lợi**, nên chưa phân biệt được Định lý 4 với nhận định thô *"hạn chót hỏng khi
   có trôi dạt"* (Hệ quả 4.3).

Tầng 2A giải quyết (1) bằng cách chạy đủ 20 ô và phân loại mọi kết cục. Tầng 2B giải quyết (2) và (3)
bằng tập giữ lại có cả khung sáng lẫn khung tối.

**Kiểm hồi tố — phương pháp dự đoán đã đúng trên một kết quả đã biết** ✅ (`retrodict.py`). Nếu Định
lý 4 đúng, thì dưới cơ sở kết quả với trần 30 s, một ô vô nghiệm **khi và chỉ khi** trên quỹ đạo gần
dự phòng có một khách mà biến động nhìn thấy `V` vượt 30 s. Quỹ đạo C1 (trần hành vi 30 s) là quỹ đạo
gần dự phòng vì tổng thành phần hành vi chỉ 128 s trên 1.581 khách, nên `V ≈ X`.

| | Các ô |
|---|---|
| **Dự đoán** — ô có khách `V > 30 s` dưới C1 | `d20181116-s10-r2`, `d20181116-s10-r4`, `d20181117-s10-r1`, `d20181117-s10-r3` |
| **Đã biết** — ô vô nghiệm dưới cơ sở kết quả 30 s (`exploratory-visible-basis-v1`) | `d20181116-s10-r2`, `d20181116-s10-r4`, `d20181117-s10-r1`, `d20181117-s10-r3` |
| **Khớp** | **4/4, trùng tuyệt đối** |

Cả các ô sát ngưỡng cũng đúng: cực đại `V` là 29,8 s (`14-r3`), 29,4 s (`15-r2`), 27,8 s (`14-r2`) ⟹ dự
đoán khả thi, đúng là khả thi; 32,0 / 32,5 / 34,2 / 38,7 s ⟹ dự đoán vô nghiệm, đúng là vô nghiệm.

Hai hệ quả:
1. Đây là **bằng chứng hồi tố** cho Định lý 4 ở họ `V`, không tốn lần chạy nào — đưa vào Chương 4
   ngay ở Tầng 1, ghi đúng tên: kết quả vô nghiệm đã biết **trước** khi viết quy tắc, nên đây là
   kiểm tính nhất quán, không phải kiểm định độc lập. Quy tắc thì đơn giản và không có tham số
   chỉnh, nên khó "khớp quá mức" — nhưng vẫn không được gọi là xác nhận.
2. Nó **kiểm định chính phương pháp** mà Tầng 2 dùng để dự đoán cho họ `M⁺`. Điều kiện để phương pháp
   hợp lệ: quỹ đạo tham chiếu phải **gần quỹ đạo dự phòng** (`C ≈ 0`). Điều kiện này đúng cho trần hành
   vi chặt (30 s: `C` tổng 128 s ở k0, 27 s ở k1) nhưng **không** đúng cho trần lỏng — với trần 120 s,
   nhà điều hành được phép dời đáng kể nên `V` không còn xấp xỉ `X`. Vì vậy không dùng phương pháp này
   để giải thích tập ô vô nghiệm ở trần 120 s (`{14-r4, 15-r2, 16-r4, 17-r4}`).

---

**Mệnh đề 2 (bộ sinh đơn điệu làm chuỗi trùng hai đầu).** Nếu mọi phương án bộ sinh tạo ra đều
có `p ≥ e` cho mọi khách cũ, thì thành phần hành vi của chuỗi công bố đơn điệu không giảm, và trên
mạng tĩnh một trần theo chuỗi và một trần theo hai đầu loại gần như cùng một tập khách.
Đo được ✅: dấu `p − e` dương ở 479/479 lần; trên B1, số khách vượt ngưỡng theo `D⁺` và theo `A`
khác nhau **≤ 1 trên 1.735** ở mọi ngưỡng 30/60/120/300 s.

*Ý nghĩa:* phát biểu *"chặn tổng biến thiên mạnh hơn chặn hai đầu"* đúng về toán nhưng **rỗng trên
hệ này**. Nó chỉ có hiệu lực khi bộ sinh có thể kéo sớm — tức khi có sắp xếp lại. **Đừng dùng tổng
biến thiên làm luận điểm phân biệt chính.**

---

**Mệnh đề 3 (biên hai lớp — chỉ để báo cáo).** Nếu chính sách bảo đảm tất định `C ≤ β` trên mọi
quỹ đạo và ước lượng được `P_π(X ≤ γ) ≥ 1 − α`, thì `P_π(V ≤ β + γ) ≥ 1 − α`. Không cần `C` và
`X` độc lập. ⚠️ Ràng buộc vận hành vẫn **tất định**; chỉ phần báo cáo là xác suất — nếu không sẽ
vi phạm ràng buộc #4 của WP15. ⚠️ `γ` phải hiệu chỉnh theo **episode**, dưới **đúng chính sách**
`π`, trên **tập tách riêng** (§8.3). Không lấy `γ` từ chính sách khác, không lấy sau khi xem tập
kiểm tra, không lấy theo một bước rồi gọi là bảo đảm cả chuyến.

### 5.3 Phản ví dụ bắt buộc có trong luận văn và trong bộ test

Đơn vị: giây, cho dễ đọc; fixture thật dùng mili-giây nguyên và thời điểm tuyệt đối hợp lệ.

| ID | `v, e, p` | Kết quả | Minh họa điều gì |
|---|---|---|---|
| CE-1 | 600, 600, 660 | `x=0, c=60, z=60` | Quyết định thuần gây dời |
| CE-2 | 600, 660, 660 | `x=60, c=0, z=60` | Giữ tuyến nhưng lời hứa vẫn xấu đi — **trần hành vi không chặn cái khách thấy** |
| CE-3 | 600, 720, 600 | `x=120, c=−120, z=0` ⟹ `C=120, V=0` | **Sửa để giữ lời hứa bị trần hành vi phạt** — giới hạn thật; chưa từng xảy ra trên panel (0/479) |
| CE-4 | `p_0=600`; công bố 660, 600 | `E=0, V=120` | Hai đầu mù với dao động |
| CE-5 | `p_0=600`; công bố 660, 720 | `E=120, V=120` | Đơn điệu thì chuỗi = hai đầu |
| CE-6 | `v=15:09.943, e=15:09.253, p=16:39.497` | `A=90,244; d=0,690; B=89,554` ⟹ hụt `2d=1,380` | **Ca thật** ở ô `d20181114-s10-r1`, khách `rq-acbbcd86c…` — trôi dạt thuận chiều hấp thụ một phần cú đẩy |

### 5.4 Kết nối lý thuyết — từ vựng để đặt khóa luận vào đúng họ

Đây là **tương ứng cấu trúc**, không phải một kết quả tỉ số cạnh tranh đã chứng minh.

Viết lại động học lời hứa: `p_t = v_t + x_t + c_t`, `v_{t+1} = p_t`. Đây đúng là dạng
`s_{t+1} = s_t + w_t + u_t` của **điều khiển trực tuyến với nhiễu** (Agarwal, Bullins, Hazan,
Kakade & Singh, ICML 2019), với nhiễu ngoại sinh `w_t = x_t` và tác động điều khiển `u_t = c_t`.

| RideBound | Điều khiển với nhiễu | Hệ quả |
|---|---|---|
| Cơ sở hành vi `Σ|c_t|` | phạt **nỗ lực điều khiển** `Σ‖u_t‖` | Luôn thỏa được bằng `u = 0` ⟹ Định lý 3.1 |
| Cơ sở kết quả `Σ|z_t|` | phạt **dịch chuyển trạng thái** `Σ‖s_{t+1} − s_t‖`, gồm cả nhiễu | Có thể vô nghiệm khi nhiễu một mình đã vượt ngân sách ⟹ Định lý 3.2 |

Trong **tối ưu lồi trực tuyến có làm trơn** (SOCO; Chen, Goel & Wierman, COLT 2018) và **hệ nhiệm
vụ metric** (Borodin, Linial & Saks, J. ACM 39(4), 1992), chi phí đổi hành động `Σ‖a_t − a_{t−1}‖`
chính là tổng biến thiên — nhưng ở đó người học **đặt trực tiếp** `a_t`, không có trôi dạt ngoại
sinh, nên hai cơ sở tính **trùng nhau**. Phân biệt hành vi/kết quả chỉ xuất hiện khi trạng thái
trôi ngoại sinh — và lời hứa ETA đúng là một trạng thái như vậy.

Câu dùng trong Chương 2: *"Cơ sở hành vi tương ứng với việc phạt nỗ lực điều khiển thay vì dịch
chuyển trạng thái — cấu trúc chi phí chuẩn trong điều khiển có nhiễu. Cơ sở kết quả quy nhiễu cho
bộ điều khiển, và đó là lý do nó có thể vô nghiệm."*

### 5.5 Định vị văn liệu

| Công trình | Đối tượng hứa | Sổ cái cộng dồn | Quy trách | Cổng thuộc họ nào (Định lý 4) | Tình trạng đọc |
|---|---|:-:|:-:|---|---|
| Fielbaum & Alonso-Mora 2020, TR-C 121 | điểm, chỉ đo | ✗ | định tính | kịch bản §6: đóng băng nhị phân ≈ `C` với `κ = 0` trên giờ chờ | toàn văn |
| Sharif Azadeh và cs. 2022, TR-B 161 | hộp tĩnh (cửa sổ + `L^Max`) | ✗ | ✗ | gần `M` | toàn văn |
| Haferkamp 2024 | nhiều lựa chọn giờ đón, ràng buộc sau khi chọn | ✗ | ✗ | — | tóm tắt |
| Ackermann & Rieck 2025, OR Spectrum | multiple plan, least-commitment | ✗ | ✗ | — | qua `docs/03` |
| **Schulz & Pfeiffer 2026**, OR Spectrum 48:541–586 | hạn chót `l` báo cho khách | ✗ | ✗ | **`M⁺`** | toàn văn |
| Schmidt–Golak–Schulz–Fliedner 2026 (TSP-SC) | một giờ đến, công bố một lần | ✗ | ✗ | — | tóm tắt |
| Sivagnanam và cs. 2026, ICCPS | chỉ "sẽ được phục vụ" | ✗ | ✗ | — | toàn văn |
| Zalesak và cs. 2025 | — (ổn định **bộ giải**, không phải lời hứa) | ✗ | ✗ | — | toàn văn |
| **Elmi, Moylan, Alonso-Mora & Fielbaum 2026**, TR-C 192:105897 | điểm; cấm cập nhật cho nhóm điểm thấp | ✗ | ✗ (mạng tĩnh) | `C` với `κ = 0` cho **một nhóm**, không ràng buộc nhóm còn lại | toàn văn |
| Schilde, Doerner & Hartl 2014, EJOR 238(1):18–30 | DARP động, tốc độ ngẫu nhiên phụ thuộc thời gian | ✗ | ✗ | — | 📎 Codex |
| **RideBound** | điểm + sổ cái 10 chiều | **✓** | **✓ định lượng** | **`C`**, và là họ duy nhất không bao giờ là nguyên nhân làm rỗng tập phương án (xét phần cam kết) | — |

### 5.6 Bảng claim

**Không được tuyên bố:**

- ❌ Lần đầu có bảo đảm ETA cho từng hành khách — Elmi 2026.
- ❌ Lần đầu kiểm soát bất ổn trong đi chung — Elmi 2026.
- ❌ Chặn tổng biến thiên là điểm phân biệt — Mệnh đề 2.
- ❌ `B = A + d` là đẳng thức — §5.2.
- ❌ `d` là tác động thuần của giao thông — K3.
- ❌ Trì hoãn cam kết, least-commitment, time consistency, dynamic insertion, ETA limit,
  reassignment, route similarity là mới — `docs/03`; `AGENTS.md`.
- ❌ Vượt trội về tỉ lệ phục vụ — mọi cấu hình có cam kết đều phục vụ ít hơn.
- ❌ Gini làm chỉ số công bằng cho gánh nặng có nhiều số 0 — §6.2 T1.4.
- ❌ Khoảng tin cậy tính trên số khách như mẫu độc lập — K7.
- ❌ Kết quả trên "mạng đường Manhattan" — K8.
- ❌ Kết quả trôi dạt "đã được kiểm chứng" — K9.
- ❌ Dùng "+7,1 pp của Zalesak" để bù "−7,13 pp".
- ❌ *"Hệ thống dùng cổng hành vi không bao giờ kẹt / không bao giờ vô nghiệm"* — nhánh hành vi chết
  11/20 ô ở k=1 vì `Board()`. Chỉ được nói: *cổng hành vi không bao giờ là nguyên nhân* (§5.2).
- ❌ Gọi 9 ô k=1 hay kiểm hồi tố 4/4 là *"xác nhận"* — đó là giải thích hậu nghiệm (§5.2). Chỉ Tầng 2B
  được gọi là xác nhận trên tập giữ lại.
- ❌ Giá trị p McNemar làm bằng chứng chính cho Tầng 2 — kết cục gần như tất định theo ô, giá trị p
  chỉ là mô tả phụ (§8.2).
- ❌ Sổ cái "chỉ tính phần gây hại" là mới — *anticipatory walking 2026* (`docs/03`) đã có cơ chế
  no-worse so với lịch tham chiếu cho một lần cập nhật; chưa đối chiếu toàn văn.
- ❌ Chứng minh Định lý 4 là khó hay sâu — nó sơ cấp; giá trị ở khung so sánh và kiểm chứng.

**Được tuyên bố**, theo đúng tổ hợp mà `docs/03-related-work-and-claim-boundary.md` đã khóa —
*per-passenger + path-dependent + multi-dimensional + cumulative/switch budget + multi-epoch
rolling insertion + machine-checkable certificate* — cộng thêm:

1. **Phân rã `v/e/p` bằng một phản thực khả thi**: `e` là phương án giữ nguyên tuyến, có thật
   trong tập lựa chọn, qua bộ kiểm tra vật lý, có mã định danh trong biên bản.
2. **Định lý 4**: trong bốn họ cổng, chỉ cổng hành vi **không bao giờ là nguyên nhân** làm rỗng tập
   phương án dưới trôi dạt; họ nào trong ba họ còn lại hỏng thì phụ thuộc chiều trôi (Hệ quả 4.3).
   Mức claim phụ thuộc Tầng 2: trước Tầng 2 — *"chứng minh + giải thích hậu nghiệm"*; sau 2A —
   *"xác nhận cơ chế có đối chứng"*; sau 2B — *"xác nhận trên tập giữ lại, cả hai chiều trôi"*.
3. **Bảo đảm có mức cho mọi khách** — trái với khẳng định của Elmi và cs. rằng bảo đảm chỉ tồn tại
   khi cấm tuyệt đối.

   > **Đính chính 2026-09-24 (claim 3 SAI, không dùng).** Đọc lại toàn văn Elmi và cs. 2026
   > (`session-2026-09-23-archive/papers-text/elmi2026.txt`, mục 2.1.4 và 2.4.1): mọi lần chèn khách
   > mới đều không được vượt độ chùng còn lại của bất kỳ khách nào đã gán, và đối chứng *ordinary
   > control* cấp cho **mọi** khách cùng một tỉ lệ độ chùng — tức đã có một trần có mức cho mọi khách
   > (kiểu `M⁺`, so với lúc gán). Câu *"would not be possible if even a single change were allowed"*
   > nói về bảo đảm **không đổi giờ**, không phải về mọi bảo đảm. Khác biệt đúng là **đối tượng bị
   > chặn**: khóa luận chỉ chặn phần do nhà điều hành gây ra, tách khỏi phần thay đổi khi giữ nguyên kế
   > hoạch (CE-2). Luận văn đã sửa theo cách này (Chương 1 và Chương 5). Dòng 70 và 506 ở trên cũng
   > cần đọc theo đính chính này.

---

## 6. Kế hoạch bốn tầng

### Tầng 0 — Sửa hồ sơ. ✍️ 0 lần chạy. Bắt buộc.

**Mục tiêu:** báo cáo LaTeX không còn một phát biểu nào sai so với mã nguồn hoặc dữ liệu, và định
vị đúng trước Elmi 2026 / Schulz 2026.

**Vị trí:** `E:\Code\Report_INT3508\ridebound\` — kho git riêng của người dùng, **không phải**
kho `RideBound`. Sửa ở đây không vi phạm kỷ luật "kho RideBound chỉ đọc".

**Công cụ bắt buộc:** dùng công cụ ghi/sửa tệp trực tiếp, **không dùng heredoc bash** cho văn bản
tiếng Việt (bẫy 12.6 của tài liệu bàn giao — chính kế hoạch này đã vấp lại bẫy đó khi soạn).

**Lệnh biên dịch:** `cd E:\Code\Report_INT3508\ridebound && ..\tools\tectonic.exe -X compile main.tex --outdir .`

**Điều kiện hoàn thành chung:** biên dịch sạch; `pdftotext main.pdf - | grep -c "\[?\]"` trả 0;
không câu nào trong danh sách ❌ ở §5.6 xuất hiện trong bản in.

#### T0.1 — Đã làm

| Tệp | Thay đổi | Ngày |
|---|---|---|
| `noi-dung/07-chuong3.tex` | "Đẳng thức trung tâm" → "Phân rã cộng tính và độ khít"; `B = A + d` → `B ≤ A + d`; bảng độ khít từng lần công bố | 21/09 |
| `noi-dung/07-chuong3.tex` | Viết lại ĐL 3.3 trên tập quỹ đạo + chính sách tối ưu; điều kiện (H) có đo; hệ quả "tối đa bằng `d`" | 21/09 |
| `noi-dung/08-chuong4.tex` | Sửa tiêu đề bảng độ khít; nối sang kết quả mịn | 21/09 |
| `noi-dung/07-chuong3.tex` | **Sửa lỗi của trợ lý:** bỏ "quy ước một chiều của `A`" (K1); thay bằng "`A` đối xứng", phản ví dụ CE-3, và số đo 0/479 | 23/09 |
| `noi-dung/07-chuong3.tex` | Đoạn giả dược: bỏ "chính sách không thể tác động lên giao thông"; `d` là thay đổi khi chiếu lại tuyến giữ nguyên, tính bất biến là tính chất thực nghiệm (K3) | 23/09 |

Sau lần sửa 23/09: biên dịch sạch, 0 tham chiếu treo.

#### T0.2 — Còn phải làm, theo thứ tự ưu tiên

**T0.2.1 — Định vị Chương 1 quanh Elmi 2026 và Định lý 4.** Tệp `noi-dung/05-chuong1.tex`, mục
`\section{Chỗ đứng so với công trình gần nhất}` (dòng ~82).

- Bỏ mọi câu dạng *"Fielbaum & Alonso-Mora 2020 kêu gọi ý tưởng tinh vi hơn — khóa luận trả lời"*.
  Chính nhóm đó đã trả lời bằng Elmi và cs. 2026.
- Dựng không gian thiết kế bằng **Định lý 4**:
  - cấm tuyệt đối cho mọi khách (Fielbaum 2020 §6) — từ chối tăng +11,1 pp;
  - cấm tuyệt đối cho một nhóm chọn lọc (Elmi 2026) — phân phối lại gánh nặng;
  - hạn chót tính từ lời hứa đầu (Schulz & Pfeiffer 2026) — họ `M⁺`, **có thể vô nghiệm dưới trôi dạt
    bất lợi**;
  - trần hành vi có mức cho mọi khách (khóa luận) — họ `C`, **họ duy nhất không bao giờ là nguyên nhân
    làm rỗng tập phương án** (xét phần cam kết). Không viết "an toàn tuyệt đối" hay "không bao giờ kẹt".
- Nêu mốc thời gian: Elmi nhận 16/01/2026, chấp nhận 24/07/2026, trực tuyến 04/08/2026 — khóa luận
  viết song song, không phải sau.

**T0.2.2 — Thêm Định lý 4, Mệnh đề 2, và bảng phản ví dụ vào Chương 3.** Tệp
`noi-dung/07-chuong3.tex`, ngay sau `\begin{hequa}[Dải khác biệt rộng tối đa $d$]…\end{hequa}`.
Dùng nguyên văn §5.2 và bảng §5.3. Môi trường: `dinhly` / `hequa` (bộ đếm chung, đã khai báo trong
`main.tex`); định nghĩa dùng `dinhnghia` (bộ đếm **riêng** — đừng gộp). Dùng `\label`/`\ref`,
không đánh số tay (bẫy 12.9).
Dùng **bản Sửa đổi 1** của Định lý 4, bắt buộc có đủ bốn thứ:
1. giả thiết (N) và đoạn "Phạm vi của định lý", kèm sự thật 11/20 ô chết vì `Board()` dưới nhánh hành vi;
2. phát biểu (a) *"không bao giờ là nguyên nhân"* tách khỏi (b) thứ tự ngưỡng trên quỹ đạo dự phòng;
3. Hệ quả 4.3 (phụ thuộc chiều trôi);
4. một câu nói thẳng rằng chứng minh sơ cấp.

Bảng `cellpred` và kiểm hồi tố 4/4 đưa vào Chương 4 với nhãn *"giải thích hậu nghiệm"* / *"bằng chứng
hồi tố"*, kèm ba giới hạn ở §5.2.

**T0.2.3 — Kết nối lý thuyết vào Chương 2.** Tệp `noi-dung/06-chuong2.tex`. Một mục ngắn dùng bảng
§5.4. Ghi rõ đây là tương ứng cấu trúc, không phải một kết quả tỉ số cạnh tranh.

**T0.2.4 — Khai báo hạn chế mới vào Chương 4, mục `muc:hanche`.**
1. Mạng là **bao đóng metric OD** trên ≤ 96 nút đã chọn, tọa độ tổng hợp (K8). Nhu cầu là dữ liệu thật.
2. Panel chính có **một snapshot thời gian di chuyển duy nhất**; trôi dạt đến từ độ trễ thực thi.
3. Các lần chạy trôi dạt dùng hệ số **vô hướng toàn mạng** (đơn điệu tăng ở khung sáng đã chạy; khung
   tối của Tầng 2B giảm), mô hình thông tin "dự báo = điều kiện hiện tại", và **chưa qua verifier** của
   dự án vì verifier đòi `travelSnapshotVersion == 1` (K9). Gắn nhãn thăm dò.
4. Dưới trôi dạt sáng k=1, **chính nhánh hành vi** chết 11/20 ô vì bất biến cửa sổ đón của `Board()`.
   Nói ra như một giới hạn của hệ, không giấu sau Định lý 4.

**T0.2.5 — Sửa bảng thứ tự hàm mục tiêu và lời giải thích §8.8.** Tệp `noi-dung/08-chuong4.tex`, mục
`muc:dathu`. Thứ tự thật (✅ `objorder.py`): `accepted-request-count` (L0) →
`worst-hard-utilization-ppm` (L1, **hằng số 1.000.000**) → `revision:*` (L2–11, khác 0 **0/7.430**) →
`operational-cost` → `candidate-id-rank`. Giải thích đúng cho "mức C trơ": tầng ngay trên là hằng số
nên luôn hòa; tầng cảnh báo lên tiếng được nhưng không đổi được quyết định. Ghi nguồn gốc khiếm khuyết:
kho đã ghi nhận ngày 2026-08-25.

**T0.2.6 — Đổi khung §8.5/8.6** thành *"phép đo độ mỏng tập lựa chọn dưới ràng buộc ổn định"*, dùng
**mẫu số đúng** (✅ `choiceset.py`): **73,84%** tập lựa chọn xe chỉ một ứng viên **trên các epoch hoạt
động** (2.142 / 14.133 = 15,2% số epoch có nhận hoặc từ chối khách), không phải 96,04% trên mọi epoch.
80,4% epoch hoạt động có ít nhất một xe với ≥ 2 ứng viên. Khảo sát Kovacs và cs. 2014 xác nhận chưa ai
công bố phân bố này.

**T0.2.7 — Bỏ chữ "cận dưới"** khi so với baseline cho đổi xe (cùng lý do ĐL 3.3).

**T0.2.8 — Sửa trích dẫn.** `noi-dung/09-chuong5.tex`, `noi-dung/10-tai-lieu.tex`:
- arXiv:2504.10649 là Zalesak, Hu & Samaranayake 2025, *"Ride-pool Assignment Algorithms: Modern
  Implementation and Swapping Heuristics"*. "LRP" = *Limit and Recall Prefix*, heuristic cho CTSP
  oracle; Định nghĩa 6.1 là ổn định **của bộ giải**. `freez`/`frozen` xuất hiện 0 lần trong bài.
- DOI bị hoán giữa time-consistent DARP (`10.1002/net.22063`) và multiple-plan DARP
  (`10.1007/s00291-025-00809-y`).
- ⚠️ Mục `gerzinic2023` đang mang tiêu đề *"Operational effects of service level variations for
  on-demand mobility"* — trùng mẫu với bài của **Molenbruch, Braekers & Caris** (CEJOR) trong
  `C:\PDF\Paper`. Đối chiếu lại tác giả – tiêu đề – nơi đăng trước khi in.

**T0.2.9 — Thêm tài liệu tham khảo.** Tối thiểu: Elmi và cs. 2026; Schulz & Pfeiffer 2026;
Sivagnanam và cs. 2026; Haferkamp 2024; Schmidt và cs. 2026 (TSP-SC); Zalesak và cs. 2025; Agarwal
và cs. 2019; Chen, Goel & Wierman 2018; Borodin, Linial & Saks 1992.

**T0.2.10 — Điền tên cán bộ hướng dẫn** ở `noi-dung/00-bia.tex` (đang `[chờ bổ sung]`).
⚠️ Chỉ người dùng biết tên này.

**T0.2.11 — Sổ cái "chỉ tính phần gây hại" vào hướng phát triển.** Tệp `noi-dung/09-chuong5.tex`.
Một đoạn, đủ bốn ý:
1. định nghĩa `h_t = max(0, |p_t − p_0| − |e_t − p_0|)` — chỉ tính phần quyết định làm lời hứa **xa
   lời hứa đầu hơn** so với giữ tuyến;
2. `0 ≤ h_t ≤ A_t` (bất đẳng thức tam giác) và no-op có `h = 0`, nên Định lý 4(a) còn nguyên; nó
   **sửa CE-3** (hành động kéo lời hứa về gần `p_0` được miễn);
3. số đo (K19): trên B1 hiện tại chênh **0,06%** tổng, cùng 403 khách — vì bộ sinh chèn thuần không
   bao giờ kéo sớm, nên chỉ có giá trị khi có sắp xếp lại;
4. đối chiếu *anticipatory walking 2026* (cơ chế no-worse so với lịch tham chiếu) trước khi nói gì về
   tính mới.

---

### Tầng 1 — Phân tích bổ sung trên dữ liệu niêm phong. ✍️ 0 lần chạy.

**Vị trí script:** `E:\Code\Report_INT3508\ridebound-scratchpad\claude-measurements-2026-09\` (18 tệp).
**Trình thông dịch:** `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B <script>.py`. Mọi script
chỉ **đọc** `E:/RideBoundData/...`, không ghi gì vào kho.

**Đọc transcript:** mỗi dòng `{"frameBase64": "..."}` → giải mã base64 → JSON; lọc
`messageType == "decision"`; thời điểm ở **cấp khung** `frame["simTimeMs"]`; hành động ở
`frame["payload"]["actions"][]`. Bẫy 12.3: `run-00.json` dùng `req-<32hex>`, transcript dùng
`rq-<64hex>` — không so trực tiếp.

| # | Phân tích | Script | Kết quả | Vào báo cáo ở đâu |
|---|---|---|---|---|
| T1.1 | Độ khít phân rã từng lần công bố | `identity.py` | §5.2 | Ch.3 — đã đưa |
| T1.2 | Điều kiện (H) | `aleb.py` | 0,42% hỏng | Ch.3 — đã đưa |
| T1.3 | Dấu của `p − e` | `signcheck.py` | 0/479 kéo sớm | Ch.3 — đã đưa |
| T1.4 | Đuôi, CVaR, bẫy Gini | `equity.py` | bảng dưới | Ch.4, mục mới |
| T1.5 | Biến động nhìn thấy theo khách | `tvcheck.py` | `V_max` C1 = 38,7 s | Ch.4, mục mới |
| T1.6 | Dự đoán khả thi theo ô cho hạn chót | `cellpred.py` | bảng §5.2 — 9 ô sống sót, hậu nghiệm (K21) | Ch.4, nhãn "giải thích hậu nghiệm" + cơ sở cho tiền đăng ký Tầng 2 |
| T1.7 | Hai đầu / chuỗi / hành vi, tĩnh và trôi dạt | `endpoint.py`, `drifttv.py` | Mệnh đề 2 | Ch.4 |
| T1.8 | Thời điểm gánh nặng | `analyze1.py` | 83,8% trước khi đón | Ch.4 |
| T1.9 | Tính không chia được | `analyze3.py`, `excess.py` | trung vị 115,6 s / lần | Ch.4 |
| T1.10 | Mẫu số đúng cho độ mỏng tập lựa chọn | `choiceset.py` | 73,84% | Ch.4 §8.5 |
| T1.11 | Thứ tự hàm mục tiêu thật | `objorder.py` | T0.2.5 | Ch.4 §8.8 |
| **T1.13** | **Kiểm hồi tố Định lý 4 (họ `V`)** | `retrodict.py` | **4/4 khớp** | **Ch.4 — bằng chứng hồi tố** (không gọi là xác nhận, §5.2) |
| T1.14 | Sổ cái "chỉ tính phần gây hại" so với sổ cái hiện tại | `harmledger.py` | chênh 0,06%, cùng 403 khách (K19) | Ch.5 — T0.2.11 |
| **T1.12** | **Phủ định C1 của WP15** | *chưa viết* | — | quyết định trục C |

**T1.4 — Bảng đuôi và bẫy Gini** (✅ `equity.py`, panel A, chiều giờ trả):

| `A_r` mỗi khách (giây) | B1 | C1 |
|---|---:|---:|
| Tổng | 64.863 | 128 |
| Số khách `A_r = 0` | 1.332 (76,8%) | 1.570 (99,3%) |
| p90 / p95 / p99 | 155,5 / 235,3 / 421,9 | 0 / 0 / 0 |
| **Cực đại** | **573,5** | **27,6** |
| **CVaR₉₅** | **336,5** | **1,6** |
| CVaR₉₉ | 473,4 | 8,0 |
| Top 5% / 10% / 20% gánh | 44,8% / 70,6% / 97,7% | — |
| Gini toàn dân số | 0,8569 | **0,9963** |

> **Bẫy Gini:** Gini **tăng** khi đi từ B1 sang C1 — chỉ số bất bình đẳng tương đối nói C1 *tệ hơn*,
> trong khi C1 tốt hơn cho **mọi** khách. Nguyên nhân: 99,3% giá trị bằng 0. Báo cáo bằng **đo tuyệt
> đối ở đuôi** (cực đại, p95, p99, CVaR); nếu in Gini thì in kèm cảnh báo này.

So sánh **hình dạng** với Elmi 2026 (không so số tuyệt đối): họ giảm số người bị đụng 4,1 lần nhưng
gánh nặng của người bị đụng **tăng** 4,5 lần; RideBound giảm CVaR₉₅ khoảng **210 lần** và tổng gánh
nặng **99,8%**, trả bằng 7,13 pp tỉ lệ phục vụ.

**T1.5 — Quan sát mô tả, không phải bảo đảm.** Dưới C1, `V` mỗi khách: p90 = 8,1 s, p99 = 21,0 s, cực
đại 38,7 s; 4/1.581 khách (0,3%) vượt 30 s. Viết *"trên panel tĩnh, quan sát được"*; **không** viết
*"bảo đảm với xác suất …"* — muốn có câu đó phải làm §8.3 trên dữ liệu có trôi dạt.

**T1.12 — Phủ định C1 của WP15** (bắt buộc theo `docs/tasks/47` §2 trước khi cài trục C):
- Đọc `payload.solver.executionEvidence.prunedCandidates[].commitmentWitnesses[]` có
  `code == "COMMITMENT_PHASE_LOCK"`; lấy `simTimeMs` của khung và `promise.pickupEtaMs` của khách bị
  witness; vẽ phân bố `pickupEta − simTime`.
- Chạy trên bundle **WP14R development panel** (`wp14-development-panel-v1`), **không** trên panel H6
  (ràng buộc WP15 #2).
- Nếu prune do khóa không tập trung gần giờ đón ⟹ trục C vô hiệu; ghi kết quả âm.

**Bàn giao:** chép cả thư mục script sang không gian làm việc của Codex để tái lập độc lập.

---

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
| **Dung lượng:** hiện 33,62 GB, mục tiêu < 30 GB; Tầng 2 thêm ~5–15 GB | Ràng buộc người dùng #2 | **Người dùng.** Hai ứng viên xóa an toàn nhất là `wp14/driftwide-v1` (1,10 GB) và `wp14/levelc-v1` (1,20 GB), nhưng `AGENTS.md` cấm xóa artifact kết quả như thao tác dọn dẹp ⟹ cần quyết định tường minh. Nếu phải chọn: đối chứng + 2B trước (120 lần, ~2–8 GB) |
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

### Tầng 3 — Lõi nhận biết thất bại, thế giới ngẫu nhiên có kiểm soát, hiệu chỉnh theo episode. 🔬

**Chỉ bắt đầu khi Tầng 2 cho tín hiệu.** Nếu `dl-30` không vô nghiệm đáng kể ở k=1 (2A), hoặc dự đoán
theo ô không chuyển được sang tập giữ lại (2B), câu hỏi của Tầng 3 yếu đi nhiều và nên dừng ở Tầng 2.

**Nguồn chi tiết:** backlog của Codex (§14–15 trong tệp của Codex: ticket C01–C08, A01–A07, P01–P08,
S01–S07, E01–E06; ma trận test M01–M14, G01–G14, W01–W12, Q01–Q12). Kế hoạch này **dùng backlog đó**,
với các điều chỉnh:

| Điều chỉnh so với Codex | Lý do |
|---|---|
| **Thế giới v0 = hệ số Manhattan đo thật** (`preflight_drift.py`), không phải mạng tổng hợp 3–8 nút | Giữ tính hợp lệ ngoài. Mạng nhỏ chỉ dùng cho oracle vi mô (tầng T0–T2 của Codex §7.2) |
| **Thế giới v1 = nhiễu theo cạnh, số ngẫu nhiên dùng chung** khóa theo `(worldSeed, edgeId, timeBin, componentId)` | Theo Codex §8.2. Bắt buộc thêm chế độ **hai chiều** và **hồi phục sau cú sốc** — khung sáng của v0 đơn điệu tăng nên thổi phồng `M⁺`; khung tối của 2B chỉ cho **một** hướng thuận lợi, vô hướng toàn mạng |
| **Nhánh hạn chót `I` lấy từ Tầng 2** | Không viết lại (Codex A03) |
| **Sửa ppm (`HardVectorCandidateAssessor.cs:329`) là một ablation một yếu tố có đối chứng** | K12 |
| **Plan pool ra khỏi đóng góp chính** | K14 |

**Thứ tự gói việc** (phụ thuộc từ trên xuống):

| Gói | Nội dung | Nguồn | Nghiệm thu |
|---|---|---|---|
| T3.1 | Khóa câu hỏi: quần thể, can thiệp, đối chứng, điểm cuối chính, sàn phục vụ, đơn vị suy luận | Codex R00, P0 | Có tình huống bác bỏ giả thuyết |
| T3.2 | Kế toán tham chiếu + oracle vi mô đọc bằng chứng gốc | Codex P1, M01–M14 | Oracle bắt được đột biến dấu, đếm đôi, thiếu một lần công bố, reset sổ cái |
| T3.3 | **Lõi nhận biết thất bại:** no-op là *tham chiếu vật lý*, không bắt buộc hợp lệ; vô nghiệm do cổng là trạng thái có kiểu, không phải `INTERNAL_ERROR` | Codex A04–A06, P02, P07, §12 | No-op bị cổng loại không làm hỏng mô hình; `CandidateSelectionModel.cs:276-279` và `DecisionMessages.cs:1113-1121` có phiên bản mới, bản cũ giữ nguyên |
| T3.4 | **Lên xe muộn là sự thật:** `RideRequest.Board`/`Rehydrate` ghi nhận + vi phạm dịch vụ riêng, không nới cửa sổ gốc | Codex C06, §12.5; mở rộng ADR-045 | Lên xe muộn round-trip qua checkpoint; FleetPy `_fleetpy_stop` có bound hiệu lực có bằng chứng |
| T3.5 | Thế giới và dự báo tách rời | Codex S01–S06, §11.3 | Kiểm rò rỉ: đổi tương lai giữ quá khứ ⟹ dự báo không đổi; truy vấn đảo thứ tự ⟹ thế giới không đổi |
| T3.6 | Hồ sơ bằng chứng nghiên cứu: audit `v/e/p` có dấu, thống kê thất bại đủ mẫu số | Codex E01–E06, §16 | Verifier độc lập tái tính bảng chính từ bằng chứng gốc |
| T3.7 | Thí điểm để bác bỏ sớm | Codex P6, §17.2 | Đủ cơ hội lựa chọn thật; phục hồi không nuốt đa số quỹ đạo |
| T3.8 | Chọn chính sách, rồi hiệu chỉnh conformal theo episode | Codex P7, §9; kế hoạch này §8.3 | Tập chọn / hiệu chỉnh / kiểm tra tách bạch, manifest bất biến |
| T3.9 | Xác nhận trên ma trận khóa | Codex P8 | Tái tính được từ bundle; mọi ô kế hoạch có kết quả hoặc lý do thiếu |

**Rào cản kỹ thuật đã biết của Tầng 3** (📎 theo SOURCE-FINDINGS, nhất quán với phần đã đọc):
FleetPy `protocol.py` từ chối `commitmentBreachDeclared`; `_fleetpy_plan` gộp khả thi dịch vụ và cấu
trúc; `_fleetpy_stop` dùng giờ đón muộn nhất gốc; callback hành khách phải trùng đúng thời điểm lô;
`change_prq_time_constraints` sửa kế hoạch FleetPy mà không phát sự kiện sang runner (cấm dùng);
`PairedComparisonDesign` từ chối hai nhánh cùng `policyId`; `DecisionInducedBurdenCalculator` cấm hủy
chuyến; `MechanicalMetricCalculator` đếm hành động `commitmentBreachDeclared` chứ không đọc sổ sự cố;
`BenchmarkSeed` chưa có thành phần cho nhiễu giao thông.

---

### Tầng 4 — Thiết kế lại đối tượng lời hứa (WP15). Bài báo riêng.

**Không đề xuất lại như ý tưởng mới** — kho đã khóa thiết kế ở
`docs/tasks/47-wp15-lifecycle-commitment-refinement.md`:

- **Trục B** — lời hứa là cửa sổ; theo Hosseini, Rostami & Araghi (2025, arXiv:2508.01032), cửa sổ tối
  ưu là quantile của phân phối thời điểm tới ở mức bằng tỷ số penalty:
  `Pr(τ ≤ ℓ) = a_w/a_ℓ`, `Pr(τ ≤ u) = 1 − a_w/a_u`. Phủ định B1 (độ rộng vượt 600.000 ms hoặc vượt p90
  biến động 154.821 ms tới mức mất nghĩa) và B2 (không ước lượng tất định được phân phối).
- **Trục C** — horizon phụ thuộc vòng đời. Phủ định C1 = T1.12.
- **Trục D** — giảm phương sai bằng gộp điểm dừng; ngoài phạm vi, cần ADR riêng.
- **Ràng buộc đã khóa:** anchor là lời hứa khách đã chấp nhận; mọi policy v2 phải bảo đảm tập khả thi
  không rỗng theo cấu tạo. **Định lý 4 cho biết, xét phần cam kết, trong bốn họ cổng chỉ họ hành vi làm
  được điều đó với mọi trần** — mọi thiết kế cửa sổ ở trục B phải được kiểm đúng tính chất này trước
  tiên. Một cửa sổ ở trục B là họ `M` nếu neo vào lời hứa đầu, nên theo Hệ quả 4.3 nó hỏng **cả hai
  chiều** trôi; phần bất biến `Board()` là việc của T3.4.
- **Cổng:** WP14R đóng `012` với frontier verified và có ADR riêng.

---

## 7. Kỷ luật thực thi

### 7.1 Cổng quản trị

| Tình trạng | Nguồn | Hệ quả |
|---|---|---|
| `docs/18` (cập nhật 2026-08-28) ghi `009_MATRIX_HALTED_40_OF_160` | `docs/18-status-and-decision-log.md` §1 | **Lạc hậu.** Bằng chứng đã commit (`41a4e11`) ghi 160/160 |
| WP14R `009..012` `UNAUTHORIZED`; WP15 chỉ ở mức roadmap; H7 chỉ mở khi WP15–16 đạt cổng | `docs/16`, `docs/tasks/47` §5 | Tầng 2 chạy ở chế độ **thăm dò**; Tầng 4 chờ ADR |
| `AGENTS.md`: mọi thay đổi mã chạy `dotnet test RideBound.slnx`; cập nhật `docs/18`, decision entry, `docs/19` khi đổi trạng thái/hợp đồng/claim/baseline; không xóa corpus/dữ liệu/artifact như dọn dẹp; giữ thay đổi của người dùng | `AGENTS.md` | Áp cho mọi tầng có sửa mã |

**Việc quản trị đầu tiên** (chỉ khi người dùng đồng ý sửa tài liệu sống của kho): đồng bộ `docs/18` và
`docs/19` với bằng chứng WP14R-013 **đã commit** — 160/160 job `terminalSuccess`, verifier độc lập
160/160, defect entered-edge đã sửa, H6 tái lập tới từng mili-giây, ba factor F1/F2/pickup-lock trơ.
**Không** dựa vào 38 dòng chưa commit trong bản prose; giữ nguyên chúng.

### 7.2 Dựng runner niêm phong — tám bước

Dẫn xuất từ tiền lệ `docs/benchmarking/wp8-011c-pre-outcome-runner-artifact-repin.md` và các builder
`wp14_freeze_v2.py`, `wp14r_freeze_v6.py`. Bắt buộc cho **chế độ chính thức**; ở chế độ thăm dò (Tầng 2)
làm tối thiểu bước 1–3, 7 và đối chứng §7.3.

1. `dotnet test RideBound.slnx` xanh.
2. Publish **Release** ra gốc **ngoài kho**, framework-dependent nhiều tệp, có `RideBound.Runner.dll`.
3. Gốc publish ổn định: mọi tệp bị băm (`runner_client.py:481-491`) và niêm phong cây.
4. Cấu hình nhánh mới vào `benchmarks/configurations/`, driver/grid, dòng nhánh trong `ARMS` /
   `WP4_CONFIG_BY_POLICY`.
5. Module freeze mới **tự niêm phong** — đường dẫn của chính nó và test của chính nó nằm trong
   `STATIC_REPOSITORY_FILES` (`Wp14FreezeV2SelfSealTests` bắt buộc). **Không bao giờ sửa receipt cũ**:
   `write_exclusive` từ chối.
6. Chạy builder với `--write --frozen-at-utc <Z>`, rồi chạy lại **không** `--write` để `verify_receipt`
   dựng lại và so **từng byte**.
7. Lấy `repositoryInventorySha256` **sau khi** commit, truyền vào mọi lần chạy qua
   `--expected-repository-inventory-sha256`.
8. Chạy ma trận qua `wp14_run_matrix.py`, nó kiểm lại các SHA cấu hình/driver/scenario trước khi chạy.

`repositoryInventorySha256` phủ **toàn bộ cây làm việc Git nhìn thấy được** — cả tracked lẫn
untracked-không-ignore — qua `git ls-files -z --cached --others --exclude-standard`. **Mọi tệp mới trong
kho đều đổi hash này.**

### 7.3 Đối chứng khi đổi runner

Mỗi runner mới phải tái lập **đúng từng ô** hai nhánh đã biết kết quả trước khi chạy nhánh mới. Tiền
lệ: reference 1.581/1.581, sai lệch 0/20 ô; nopickuplock 1.583/1.583, sai lệch 0/20 ô. So **quyết định**
chứ không so `semanticHash` (bẫy 12.7).

### 7.4 Bẫy — đã vấp và mới phát hiện

Giữ nguyên mười bẫy ở mục 12 tài liệu bàn giao. Thêm:

| # | Bẫy | Cách tránh |
|---|---|---|
| N1 | Tin lời giải thích "`decisionDelta` một chiều" trong `wp14r-013` | Mã tính `|p − e|` (K1). Luôn đọc mã, không đọc prose |
| N2 | Gọi `d` là "do giao thông" | `e` chiếu trên trạng thái đã giảm cả lô (K3) |
| N3 | Nhánh mới rơi vào nhánh mặc định của `EffectivePolicies` và âm thầm chạy không ràng buộc | `SolverBackedRidePoolingPolicy.cs:396-410`; `EffectivePolicyFairnessTests.cs` tự liệt kê enum — giữ nó đỏ khi thêm kind |
| N4 | Cổng có thể loại no-op làm hỏng run thay vì ghi nhận vô nghiệm | K4; hạn chót một chiều hỏng qua fail-closed `HardVectorCandidateAssessor.cs:188-216`; hạn chót hai chiều và cổng kết quả dưới trôi thuận lợi hỏng qua đường K20 — T2.1(6) |
| N5 | Đổi `policyId` của cấu hình cam kết | Preflight hard-code `wp6-synthetic-policy-overlay-v1` (`:189`, `:234`) |
| N6 | Chạy verifier medium lên lần chạy có trôi dạt | Verifier đòi `travelSnapshotVersion == 1` (`:1158`) |
| N7 | `dotnet test` đỏ trên worktree sạch vì một test kỳ vọng `GitDirty = true` | 📎 Xác nhận trên cây chính trước, không sửa test |
| N8 | Heredoc bash cho văn bản tiếng Việt dài | Hỏng so khớp và vượt giới hạn dòng lệnh (`ENAMETOOLONG`) — đã vấp khi soạn chính tệp này |
| N9 | Dùng Gini cho gánh nặng nhiều số 0 | §6 T1.4 |
| N10 | Tính khoảng tin cậy với số khách làm cỡ mẫu | K7 |
| N11 | Đọc "First rejection" trong thông điệp fail-closed như lý do của no-op | Đó là ứng viên đầu tiên theo **id băm**, và lý do có thể không phải cam kết (§5.2). Dùng T2.1(6) |
| N12 | Chạy ô khung tối bằng `preflight_drift.py` gốc | Mốc `WINDOW_START_SECONDS = 28800` hard-code (dòng 73) ⟹ áp hệ số khung sáng lên ô tối, **không báo lỗi**. Dùng `preflight_drift_v2.py` (T2.6) |
| N13 | Gọi giải thích hậu nghiệm là "xác nhận" | Chỉ 2B được gọi là xác nhận trên tập giữ lại (§5.6) |
| N14 | Suy dự đoán buổi tối từ tỉ số cuối/đầu khung | Đầu khung tối nhích lên (K18); dùng cực đại chạy theo từng khách (T2.8) |

---

## 8. Thiết kế thống kê

### 8.1 Đơn vị suy luận

**Ô / episode là đơn vị độc lập.** Khách trong cùng một ô chịu chung trạng thái đội xe, chung trôi dạt,
chung quyết định điều phối — không độc lập. Bộ giải tất định (`solverSeedsAreReplicates: false`, hai
seed contrast đo được đúng 0), nên lặp lại đến từ **mẫu nhu cầu**: 20 ô = 5 ngày × 4 mẫu. Chạy lại một ô
với seed khác **không** tạo thêm mẫu độc lập.

### 8.2 Tầng 2 — biến nhị phân theo ô

- **Bằng chứng chính là dự đoán theo ô đã niêm phong so với kết cục** (T2.8–T2.9), không phải một giá
  trị p. Khi trôi dạt và mẫu nhu cầu đã cố định, kết cục của một (ô, nhánh) gần như **tất định** — bộ giải
  tất định, lặp seed cho đúng 0 khác biệt (§8.1). Câu hỏi đúng là *"quy tắc có đoán trúng từng ô không"*.
- Tỉ lệ ô vô nghiệm do cam kết: báo kèm **khoảng Clopper–Pearson chính xác** (không dùng xấp xỉ chuẩn,
  vì tỉ lệ ở gần 0 hoặc 1). Với 8 ô một khung ở 2B, khoảng rất rộng — in ra để người đọc thấy, đừng
  diễn giải quá.
- So ghép cặp `dl-l` với `conduct-30`: **McNemar chính xác** trên các ô bất đồng, **chỉ mô tả phụ**. Với
  `b` ô chỉ `dl` vô nghiệm và `c` ô chỉ `conduct` vô nghiệm, `p = 2 · P(Bin(b+c, ½) ≤ min(b,c))`. Theo
  Định lý 4(a), `c = 0`.
- Ngưỡng xác nhận và điều kiện phủ định (≥ 90% / < 75% cặp đúng) được **chốt trước** trong
  `PREREGISTRATION.md`; không đổi sau khi xem kết cục.

### 8.3 Tầng 3 — hiệu chỉnh `γ` cho biên hai lớp

**Không dùng DKW trên số khách** (K7). Dùng **quy tắc thứ hạng conformal tách tập** theo episode:

1. Khóa chính sách `π`, bộ sinh, dự báo, nhịp công bố, quy tắc phục hồi, cohort — trước khi hiệu chỉnh.
2. Điểm mỗi episode: `S_j = max_{r ∈ cohort(j)} X_{r,j}` — cực đại theo khách, nên câu phát biểu đồng
   thời cho mọi khách trong episode. (Hoặc: hai điểm cho giờ đón và giờ trả với `α` chia trước, dùng
   bất đẳng thức hợp.)
3. Trên `n` episode hiệu chỉnh: `k = ⌈(n + 1)(1 − α)⌉`. Nếu `k ≤ n` thì `γ = S_(k)` (thống kê thứ tự thứ
   `k`, đánh số từ 1, sắp tăng); nếu `k > n` thì `γ = ∞` và **ghi rõ biên không hữu hạn**. Cài bằng số
   nguyên, xử lý trùng giá trị bảo thủ, **không** dùng hàm quantile nội suy của thư viện.
   ⚠️ **Bẫy thật là hàm quantile có nội suy**, không phải phép làm tròn: ví dụ `numpy.quantile` mặc định
   nội suy tuyến tính giữa hai thống kê thứ tự, nên trả một giá trị **nằm giữa** `S_(k−1)` và `S_(k)` —
   không phải `S_(k)` — và làm mất bảo đảm. Phải lấy đúng phần tử thứ `k` của mảng đã sắp.
   Về làm tròn: đã kiểm `ceil((n+1)*(1−α))` bằng dấu phẩy động với `α ∈ {0,01; 0,02; 0,05; 0,1; 0,15;
   0,2; 0,25; 0,3; 0,4}` và `n ≤ 5.000` — **không có ca nào lệch** so với số học chính xác. Dù vậy vẫn nên
   tính bằng số nguyên cho chắc: với `α = a/b` thì `k = ((n+1)(b−a) + b − 1) div b`; ví dụ `α = 1/20` cho
   `k = (19(n+1) + 19) div 20`. Test bắt buộc: `n = 18 ⟹ k = 19 > n ⟹ γ = ∞`; `n = 19 ⟹ k = 19`;
   `n = 20 ⟹ k = 20`; có giá trị trùng; `k = n + 1`.
4. Với `α = 0,05`: `n = 18` ⟹ `k = 19 > 18` ⟹ `γ = ∞`; `n = 19` ⟹ `k = 19` ⟹ `γ = S_(19)` = cực đại.
   Hữu hạn ở `n = 19` **không** có nghĩa đã đủ tin cậy — `γ` khi đó là cực đại, thường rất rộng.
5. Bảo đảm: dưới giả thiết các episode **có thể hoán đổi**, `P(S_new ≤ γ) ≥ 1 − α`. Kết hợp với
   `C_r ≤ β` với mọi `r` trên mọi quỹ đạo: `P(∀r: V_r ≤ β + γ) ≥ 1 − α`.
6. **Kiểm tra trên `m` episode mới:** đếm số episode vi phạm, báo khoảng Clopper–Pearson. Nếu 0 vi phạm
   trong `m` episode, cận trên một phía 95% là `1 − 0,05^(1/m)`. Để cận này ≤ 5% cần
   `m ≥ ln 0,05 / ln 0,95 ≈ 58,4`, tức **ít nhất 59 episode không vi phạm**. (Đã tính lại, khớp Codex.)
7. Độ phủ theo khách chỉ là **mô tả**, không thay được bảo đảm theo episode.
8. Nếu thay chính sách để giảm `X` thì phải hiệu chỉnh lại trên tập mới; không dùng cùng tập để chọn và
   để chứng nhận.

Tham khảo: Angelopoulos & Bates, arXiv:2107.07511, Phụ lục D; về giới hạn khi mất tính hoán đổi: Barber,
Candès, Ramdas & Tibshirani, arXiv:2202.13415.

### 8.4 Hiệu ứng ghép cặp

Tính hiệu ghép cặp trong cùng ô: tỉ lệ phục vụ / số khách đến, biến động tích lũy, trễ thực tế, tỉ lệ
phục hồi, độ trễ quyết định. Khoảng tin cậy: **bootstrap ghép cặp theo ô** — lấy mẫu lại mã ô, giữ nguyên
mọi nhánh và mọi khách trong ô đã chọn; khóa số lần lặp và seed phân tích **trước** khi xem tập kiểm tra.

### 8.5 Mẫu số và đường biên

- Báo cả thay đổi tuyệt đối và tương đối; nếu baseline bằng 0 thì thay đổi tương đối **không xác định**,
  không ghi 100%.
- Gánh nặng trung bình trên khách **được nhận** là đại lượng nhạy chọn mẫu: một cơ chế nhận ít khách hơn
  có thể làm trung bình đẹp lên. Báo thêm trên khách **đến**.
- Quét nhiều `β` thì vẽ đường biên mô tả, và **chọn trước** một phép so xác nhận; không quét lưới rồi chỉ
  báo điểm có `p` nhỏ nhất.

---

## 9. Dự đoán tiền đăng ký theo tầng

| Tầng | Dự đoán | Tiêu chí xác nhận | Tiêu chí phủ định |
|---|---|---|---|
| 1 / T1.12 | Prune do khóa tập trung gần giờ đón | Phần lớn prune có `pickupEta − now` nhỏ | Rải đều ⟹ **trục C vô hiệu** |
| 2 / bất biến | `conduct-30`: 0 ô `commitment-*` ở mọi panel, mọi `k`; `selection-noop-invariant` không xuất hiện ở nhánh nào | Đúng 0 | Khác 0 ⟹ **lỗi cài đặt**, dừng |
| 2A / chính | Dự đoán theo ô (`predictions.csv`), đủ 20 ô × `dl-30/60/120` × k∈{0,1} | ≥ 90% cặp đúng, và `dl-30` k=1 vô nghiệm do cam kết ở đa số ô | < 75% ⟹ phương pháp dự đoán sai ngay trên panel đã dùng để dựng |
| 2A / tham khảo | Theo bảng hậu nghiệm 9 ô sống sót: `dl-30` 9/9, `dl-60` 7/9, `dl-120` 0/9 ở k=1; mọi `dl-*` 0/20 ở k=0 | — (đã thay bằng dự đoán theo ô) | — |
| 2B / chính | Dự đoán theo ô, 16 ô × 4–5 nhánh, k=1 | ≥ 90% cặp đúng **ở khung tối** + hàng `w17` của bảng hướng đúng | < 75% ở khung tối |
| 2B / hướng, tối | `dl-30` ≤ 1/8, `dl-120` 0/8; `dl2-30` ≥ 4/8; `visible-30` ≥ 4/8 | Cả bốn đúng | `dl-30` ≥ 3/8 do `deadline-late` ⟹ Hệ quả 4.3 không có răng ở khung này; `dl2-30` và `visible-30` cùng ≤ 2/8 ⟹ trôi thuận lợi quá nhỏ |
| 2B / hướng, sáng | `dl-30` ≥ 4/8; `dl2-30` ≥ `dl-30` từng ô; `visible-30` ≥ 4/8 | Đúng | — (tham khảo; sáng đã có 2A) |
| 2B / phụ | Buổi tối `dl-30` nhận nhiều khách hơn `conduct-30` ở đa số ô cùng hoàn tất | Thăm dò | — |
| 3 / ablation ppm | Tỉ lệ phục vụ không đổi đáng kể | Chênh < sàn nhiễu ±0,3 pp | Tầng `worst-hard-utilization-ppm` vẫn hòa ≥ 99% ⟹ không cứu được |
| 3 / hai lớp | `γ` dưới trôi dạt lớn hơn nhiều 8,7 s của panel tĩnh (trôi dạt đo được: `d` p90 = 47,4 s, cực đại 150,7 s ở k=1) | Có biên hữu hạn với `n ≥ 19` | `γ` rộng hơn mức hữu ích đã chốt ⟹ báo **kết quả âm**, không cắt `γ` |

---

## 10. Rủi ro

| # | Rủi ro | Mức | Giảm thiểu |
|---|---|---|---|
| R1 | Bẫy `EffectivePolicies` (N3) | Cao × Cao | `EffectivePolicyFairnessTests` tự liệt kê enum; thêm test cho mỗi kind mới |
| R2 | Đối chứng T2.4 không tái lập | Trung bình × Cao | Dừng; so từng quyết định bằng `decision_identity.py`; không chạy nhánh mới |
| R3 | 11/20 ô ở k=1 chết vì `window-wall` dưới nhánh hành vi | Chắc chắn × Trung bình | **Không** thu mẫu về 9 ô sống sót (K21): quy tắc dự đoán T2.8 có nhánh riêng cho ô chết (so `τ` với `T`), phân tích trên đủ 20 ô; tùy chọn `k = 0,5`; sửa triệt để ở Tầng 3 (T3.4) |
| R4 | Trôi dạt v0 đơn điệu tăng thổi phồng `M⁺` so với nhiễu hai chiều | Chắc chắn × Trung bình | 2B có khung tối thuận lợi thật (K18). Vẫn chỉ là hệ số vô hướng toàn mạng; Tầng 3 bắt buộc có nhiễu theo cạnh và hồi phục |
| R11 | Khung tối xe đến sớm làm `Board()` hỏng cả nhánh hành vi | Thấp × Cao | K22: FleetPy chờ tới giờ đón sớm nhất. Vẫn chạy thử một ô tối (T2.6 bước 2) trước khi chạy cả panel |
| R12 | Đường K20 lần đầu được đi qua trên dữ liệu thật; thay đổi 6 có lỗi | Trung bình × Cao | Test T2.2 ca (a)–(d); nhãn `selection-noop-invariant` xuất hiện ⟹ dừng; đối chứng T2.4 so nhãn và tập ô, không so văn bản thông điệp |
| R13 | Panel phát triển không hoàn toàn "chưa ai nhìn": kết cục **tĩnh** đã có trong ma trận v6 | Chắc chắn × Thấp | Không có kết cục **dưới trôi dạt** nào; bảng hướng 2B viết từ Hệ quả 4.3 và hệ số giao thông, không từ kết cục v6. Ghi rõ trong tiền đăng ký. T1.12 cũng chỉ đọc kết cục tĩnh |
| R14 | Đoạn nhích 15–30 phút đầu khung tối làm `dl-30` tối vô nghiệm ở nhiều ô | Trung bình × Trung bình | Dự đoán theo ô đã tính đến (cực đại chạy); luật diễn giải số 6 của T2.8 quyết định cách viết. Không đổi khung, không cắt 30 phút đầu sau khi xem kết quả |
| R15 | Nhánh `dl2-30` bị chê là cơ chế không ai dùng | Trung bình × Thấp | Trình bày là **đầu dò họ `M`**, không phải đối thủ; đối thủ thật ở buổi tối là `visible-30` (cơ sở `customerVisible` đã có) |
| R5 | Tầng 2 cho kết quả âm | Trung bình × Cao | Đã khai báo trước là hợp lệ (ràng buộc WP15 #7). Khóa luận vẫn đứng trên Tầng 0–1 |
| R6 | Dung lượng vượt 30 GB | Chắc chắn × Thấp | Quyết định của người dùng ở T2.0 |
| R7 | Sửa mã kho làm hỏng thay đổi chưa commit của người dùng | Thấp × Cao | `git worktree` riêng (T2.0) |
| R8 | Dùng số H6 để chọn tham số nhánh mới | Trung bình × Cao | Ràng buộc WP15 #2; mức Tầng 2 lấy từ dữ liệu trôi dạt, không từ H6 |
| R9 | Giới hạn phiên API cắt ngang công việc dài | Cao × Thấp | Lưu kết quả trung gian ra tệp sau mỗi bước; mọi script đều có `"reused"` |
| R10 | Phát biểu về bài Schulz vượt quá những gì đã đọc | Trung bình × Trung bình | Hệ quả 4.1 viết có điều kiện; đối chiếu giả thiết thời gian di chuyển trong toàn văn trước khi in |

---

## 11. Lịch trình và điểm dừng

```
Tầng 0 (2–4 ngày) ──┐
                     ├──► ĐIỂM DỪNG A: khóa luận hoàn chỉnh, 0 lần chạy mới
Tầng 1 (1–2 ngày) ──┘
        │
        └── T1.12 ──► quyết định trục C của WP15

Tầng 2 (~1,5 tuần: mã 1,5–2 ngày, test 1–1,5 ngày, runner + đối chứng 0,5–1 ngày,
        2B conduct + dự đoán + niêm phong 0,5 ngày, chạy 5–8 giờ tính toán, phân tích 1–1,5 ngày)
        ├──► ĐIỂM DỪNG B1 (sau 2A): định lý + xác nhận cơ chế có đối chứng
        └──► ĐIỂM DỪNG B2 (sau 2B): định lý + xác nhận trên tập giữ lại, cả hai chiều trôi

Tầng 3 (4–10 tuần, chỉ khi Tầng 2 có tín hiệu)
        └──► ĐIỂM DỪNG C: đóng góp nghiên cứu đầy đủ

Tầng 4 — bài báo riêng, chờ ADR mở WP15
```

**Đường găng của Tầng 2:** T2.0 (người dùng quyết ba cổng) → T2.1 → T2.2 → T2.3 → T2.4 (đối chứng phải
khớp) → T2.6 bước 2–3 (chạy thử ô tối; `conduct-30` trên panel phát triển) → T2.8 (dự đoán theo ô +
niêm phong) → T2.6 bước 5–6 → T2.7 → T2.9.

**Nếu dung lượng hoặc thời gian chỉ đủ một nửa:** làm **2B trước** — 40 đối chứng T2.4 (vẫn bắt buộc) +
80 lần chạy 2B = **120 lần**, ~2–8 GB.
Nó là phần mới và phân biệt; 2A chủ yếu biến giải thích hậu nghiệm sẵn có thành dự đoán đầy đủ.

**Nếu thời gian rất ngắn:** chỉ Tầng 0 và Tầng 1. Chúng không tốn một lần chạy nào và bịt đúng những lỗ
mà một phản biện đọc kỹ sẽ chọc vào.

---

## 12. Phụ lục

### 12.1 Script đo

`E:\Code\Report_INT3508\ridebound-scratchpad\claude-measurements-2026-09\` — 18 tệp:

| Script | Đo gì |
|---|---|
| `promise_paths.py` | Trích quỹ đạo lời hứa từ transcript |
| `identity.py` | Độ khít `A + d = B` từng lần công bố |
| `aleb.py` | Điều kiện (H) `A ≤ B` |
| `signcheck.py` | Dấu của `p − e` (K2) |
| `tvcheck.py` | Chuỗi đại lượng; phân bố `V` theo khách |
| `endpoint.py` | So ngưỡng `D⁺` / `A` / `V` trên panel tĩnh |
| `drifttv.py` | So dưới trôi dạt k0/k1 |
| `cellpred.py` | **Dự đoán khả thi theo ô cho nhánh hạn chót** |
| `equity.py` | Đuôi, CVaR, Gini, tập trung |
| `analyze1.py` | Thời điểm gánh nặng, chính sách công bố, phơi nhiễm |
| `analyze2.py` | Hiệu quả phân bổ ngân sách (cận hậu nghiệm — không phải thuật toán trực tuyến) |
| `analyze3.py` | Độ lớn từng lần dời, dấu chân ngoại ứng |
| `excess.py` | Phần vượt trần của phương án bị loại |
| `choiceset.py` | Độ mỏng tập lựa chọn, mẫu số đúng |
| `objorder.py` | Thứ tự tầng mục tiêu thật |
| `realcase.py` | Trích ca `v/e/p` thật để minh họa |
| `retrodict.py` | **Kiểm hồi tố Định lý 4 cho họ `V`: 4/4 ô khớp tuyệt đối** (bằng chứng hồi tố) |
| `harmledger.py` | Sổ cái "chỉ tính phần gây hại" so với sổ cái hiện tại (K19) |

**Sẽ viết ở Tầng 2**, trong `ridebound-scratchpad/deadline/` (chưa tồn tại):

| Script | Việc |
|---|---|
| `preflight_drift_v2.py` | Bản sao `drift/preflight_drift.py`, đọc mốc khung từ `RB_DRIFT_WINDOW_START_SECONDS` (T2.6) |
| `check_preflight_v2.py` | Lịch hệ số v2 trùng v1 ở mốc 28800; đúng ở mốc 61200 |
| `run_deadline.py` | Trình điều khiển ma trận 2A + 2B |
| `holdout_predict.py` | Dự đoán theo ô từ quỹ đạo `conduct-30` (T2.8) |
| `classify.py` + test | Bộ phân loại T2.7, hỏng nếu hằng thông điệp trong mã đổi |

### 12.2 Bản đồ mã nguồn đã kiểm chứng

| Tệp:dòng | Nội dung | Dùng ở |
|---|---|---|
| `src/RideBound.Application/Promises/PromiseDeltaCalculator.cs:64-98`, `:259-262` | Ba cặp chiếu; `AbsoluteDifference` | K1 |
| `src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:316-340` | `e` từ `ReducedState` | K3 |
| `…/CommitmentDecisionValidator.cs:346-367` | Gọi bộ đánh giá khóa; ánh xạ witness | T2.1(4) |
| `src/RideBound.Domain/Commitments/CommitmentLockEvaluator.cs:13-85` | Chữ ký, luật khóa, so với `exogenous` | T2.1(3) |
| `src/RideBound.Domain/Commitments/CommitmentPolicy.cs:129-137` | Hàm dựng 8 tham số | T2.1(2) |
| `src/RideBound.Domain/Common/DomainPrimitives.cs:138-144` | `Duration` nhận `0 ≤ ms ≤ 2^53−1` | T2.1(2) |
| `src/RideBound.Runner/Configuration/CommitmentPolicyConfiguration.cs:20-28`, `:143-184` | `PolicyFields`; `ReadPolicy` | T2.1(5) |
| `src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:188-216`, `:205` | Fail-closed và thông điệp | K5, T2.7 |
| `…/HardVectorCandidateAssessor.cs:316-331` | Khiếm khuyết ppm | K11, K12 |
| `src/RideBound.Application/Optimization/CandidateSelectionModel.cs:276-279` | Đúng một no-op mỗi xe; mã `INVALID_CANDIDATE_SELECTION_PROBLEM` | K4, K20 |
| `src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:99-101`, `:368-398` | Bọc lỗi mô hình thành `SOLVER_MODEL_MAPPING_FAILED`, không có đường lùi | K20 |
| `src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:484-493` | `AssessmentFailure`: giữ `Message`, `CandidateId`, `Dimension`; bỏ `UnderlyingCode` | §5.2, T2.1(6) |
| `src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs:196-228` | Id no-op là băm (`CandidateIdentity.Create`); lỗi `ActiveRouteInfeasible` khi không giữ được no-op | §5.2, T2.7 |
| `src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:79-186` | Vòng lặp ứng viên; `hardPruned`, `hardValidationWitnesses` | T2.1(6) |
| `src/RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs:131-142` | `CommitmentAssessmentWitness` và các trường có kiểu | T2.1(6) |
| `src/RideBound.Domain/Commitments/CommitmentVector.cs:135-153` | `CommitmentFailureCodes` | T2.1(1) |
| `tests/RideBound.Algorithms.Tests/Oracle/ExactSmallCommitmentDifferentialTests.cs:584`, `:624-633`, `:637` | Hai test fail-closed; quy ước "trường có kiểu, không parse văn bản" | T2.2 |
| `src/RideBound.Application/Scheduling/RouteScheduleProjector.cs:163` | Bộ chiếu lịch chờ tới `EarliestPickup` | K22 |
| `simulators/fleetpy-ridebound/ridebound_fleetpy/fleet_control.py:954` | `earliest_pickup_time_dict` vào `BoardingPlanStop` | K22 |
| `src/RideBound.Contracts/Protocol/DecisionMessages.cs:1113-1121` | Đúng một no-op **hợp lệ** mỗi xe | K4 |
| `src/RideBound.Domain/Requests/RideRequest.cs:266-273` | Bất biến cửa sổ đón trong `Board()` | T2.7, T3.4 |
| `src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:396-410` | `EffectivePolicies`, nhánh mặc định xóa trần | N3 |
| `simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py:113-139`, `:189`, `:234` | Đồ thị đầy đủ tổng hợp; `policyId` hard-code | K8, N5 |
| `simulators/fleetpy-ridebound/actual_fleetpy_medium_verify.py:1158` | `travelSnapshotVersion == 1` | K9 |
| `ridebound-scratchpad/drift/preflight_drift.py:1-49`, `:129-152` | Cơ chế bơm trôi dạt | K10 |
| `ridebound-scratchpad/drift/preflight_drift.py:65-66`, `:73`, `:86`, `:93` | `REPO`/`TARGET` trỏ cứng; `WINDOW_START_SECONDS = 28800` và hai chỗ dùng | T2.6, N12 |
| `<fixture>/normalizer-configuration.json` | `sourceWindowStartSeconds` (28800 / 61200), `drainDurationMs` = 7.200.000 | T2.6 |
| `ridebound-scratchpad/drift/run_drift.py:59` | Runner của các lần chạy trôi dạt | K16 |
| `ridebound-scratchpad/drift/run_drift_frac.py:101-107` | Bộ phân loại lỗi hiện có | T2.7 |

### 12.3 Lệnh chạy một ô có trôi dạt

```bash
cd E:/Code/RideBound-deadline
export PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8
export RB_DRIFT_DAY=2018-11-14 RB_DRIFT_EXPONENT=1
E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B \
  E:/Code/Report_INT3508/ridebound-scratchpad/drift/preflight_drift.py \
  --label "dl-30-k1-d20181114-s10-r1-s7" \
  --fleetpy-root E:/RideBoundData/wp7/FleetPy-1.0.2 \
  --runner-root  E:/RideBoundData/research/runner-deadline-v1 \
  --dotnet "C:/Program Files/dotnet/dotnet.exe" \
  --commitment-config E:/Code/Report_INT3508/ridebound-scratchpad/deadline/dl-30.json \
  --wp4-config benchmarks/configurations/wp9-fleetpy-ridebound-hard-vector-audited-v1.json \
  --scenario             <fixture>/scenario-content.json \
  --derivative-manifest  <fixture>/derivative-manifest.json \
  --normalization-report <fixture>/normalization-report.json \
  --selection-frame      <fixture>/selection-frame.json \
  --driver benchmarks/scenarios/wp9-confirmatory/d20181114-s10-r1.driver.json \
  --output E:/RideBoundData/research/deadline-v1/dl-30-k1-d20181114-s10-r1-s7 \
  --repeats 1 --master-seed 7
```

`<fixture>` = `benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp9-confirmatory-fixed-panel-v2/d20181114-s10-r1`.
⚠️ `preflight_drift.py` đang trỏ cứng `REPO = E:/Code/RideBound` (dòng 65) và
`TARGET = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"` (dòng 66). Chạy từ
worktree thì phải sửa hai hằng này trong **bản sao** của script, không sửa bản gốc. `preflight_drift_v2.py`
là bản sao đó.

**Một ô khung tối của panel phát triển (2B):** cùng lệnh, khác bốn chỗ.

```bash
export RB_DRIFT_DAY=2018-11-12 RB_DRIFT_EXPONENT=1 RB_DRIFT_WINDOW_START_SECONDS=61200
E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B \
  E:/Code/Report_INT3508/ridebound-scratchpad/deadline/preflight_drift_v2.py \
  --label "conduct-30-k1-d20181112-s10-r1-w17-s7" \
  … (các đối số runner/FleetPy/cấu hình như trên) … \
  --scenario             <dev>/scenario-content.json \
  --derivative-manifest  <dev>/derivative-manifest.json \
  --normalization-report <dev>/normalization-report.json \
  --selection-frame      <dev>/selection-frame.json \
  --driver benchmarks/scenarios/wp14-development/d20181112-s10-r1-w17.driver.json \
  --output E:/RideBoundData/research/deadline-v1/conduct-30-k1-d20181112-s10-r1-w17-s7 \
  --repeats 1 --master-seed 7
```

`<dev>` = `benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1/d20181112-s10-r1-w17`.
`RB_DRIFT_WINDOW_START_SECONDS` phải bằng `sourceWindowStartSeconds` trong `<dev>/normalizer-configuration.json`;
`run_deadline.py` đọc tệp đó và đặt biến, không gõ tay. ⚠️ Chưa chạy thử lệnh này — tên đối số lấy theo
lệnh panel A ở trên; kiểm lại bằng `--help` của preflight trước lần chạy đầu.

### 12.4 Nguồn đã xác minh trong đợt lập kế hoạch này

- Elmi, Moylan, Alonso-Mora & Fielbaum (2026), *Improving ridepooling reliability using shareability
  shadows*, TR-C 192:105897 — PDF cục bộ, SHA-256 `5a68817a…fe728a5`, toàn văn đã đọc các mục §1.3,
  §2.1.3, §2.1.4, §2.4.1, §4.
- Schulz & Pfeiffer (2026), OR Spectrum 48:541–586 — toàn văn (qua báo cáo trích xuất).
- Sivagnanam, Mukhopadhyay, Samaranayake, Dubey & Laszka (2026), ICCPS — toàn văn.
- Zalesak, Hu & Samaranayake (2025), arXiv:2504.10649 — toàn văn.
- Schilde, Doerner & Hartl (2014), EJOR 238(1):18–30 — xác minh tồn tại và phạm vi.
- Haferkamp (2024), *Design of multi-optional pickup time offers in ride-sharing systems* — xác minh.
- Fu (2002), TR-B 36(6):485–506 — xác minh.
- Chen, Goel & Wierman (2018), COLT, PMLR v75 — SOCO, Online Balanced Descent.
- Agarwal, Bullins, Hazan, Kakade & Singh (2019), ICML, PMLR v97 — điều khiển trực tuyến với nhiễu.
- Borodin, Linial & Saks (1992), J. ACM 39(4):745–763 — hệ nhiệm vụ metric.
- Angelopoulos & Bates, arXiv:2107.07511; Barber, Candès, Ramdas & Tibshirani, arXiv:2202.13415 — theo
  Codex, không đọc lại.
- *Where should the last passenger be dropped off? Anticipatory walking in ridepooling* (TR-C 2026,
  S0968090X26001336) — chỉ qua mục ở `docs/03-related-work-and-claim-boundary.md:58-66`; **chưa đọc toàn
  văn**. Phải đọc trước khi viết T0.2.11.
- Hệ số giao thông `2018-11-{12..18}_tt_factors.csv` (FleetPy Manhattan, bản giải nén trong
  `E:/RideBoundData/wp6/extracted/…/Manhattan_2019_corrected/`) — đọc trực tiếp cột `travel_time_factor`
  ngày 23/09 (K18).

### 12.5 Những gì tài liệu này không làm

- Không authorize `RB-WP14R-009..012`, không authorize WP15, không mở H7.
- Không sửa `docs/18`, `docs/19` hay bất kỳ tệp nào trong kho `RideBound`.
- Không đổi margin, panel, denominator, factor level hay failure treatment nào đã tiền đăng ký.
- Không lấy tham số số học nào từ văn liệu để đặt mức cho nhánh.
- Không tuyên bố RideBound tốt hơn, nhanh hơn hay tương đương bất kỳ công trình nào.
