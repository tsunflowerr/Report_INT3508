# R23 — Kiểm chứng sự kiện Chương 3 (Claude, 2026-10-11)

**Đối tượng:** `rewrite-2026-10/drafts/07-chuong3.tex` (662 dòng) và `drafts/07-chuong3-NOTES.md` (X3-01…X3-19).
**Căn cứ:** `evidence/EVIDENCE-REGISTER.md` (A01…K52), `evidence/EVIDENCE-REGISTER-ADDENDUM-1.md` (mục 0, N-01…N-30,
L1a-01…09), và các anchor gốc do tôi tự mở trong phiên này: mã chỉ đọc ở `C:/Code/RideBound-noworse/src/` và `tests/`,
adapter `C:/Code/RideBound-noworse/simulators/fleetpy-ridebound/`, cấu hình `tang3/configs/`, output `STG`, `ADD1`,
`EL17`, `T38`, `T38I`, `FR`, `FFA`, `DISP`, `STRETCH`, `SPEC`, `HO`, `ADR`, `HZ`, `FLEET`, `TEX08`, `NEW` (R18-verification).
Không đọc `codex-work/R23-*` hay `reviews/R23-*` khác. Không sửa bản nháp, không chạy mô phỏng, không build.

**Phiên bản mã.** `C:/Code/RideBound-noworse` đang ở nhánh `research/tier3-no-worse`; `git diff 45f8026 HEAD -- src tests`
rỗng và `git status src` sạch. Runner lưu trữ `runner-tier3-v2` được publish từ `45f8026` (ADR:5117, REG A28), nên
mã tôi đọc trùng nguồn của runner đã dùng cho tập chính, tập buổi sáng và trần 120 giây (lưu ý core commit 1ce15e9 của
A28/I13 vẫn chỉ do Codex R15 xác nhận).

**Nhãn.** OK = câu nói đúng điều bằng chứng nói. WRONG = sai so với anchor (có câu sửa). UNSUPPORTED = không có dòng sổ
hay anchor không đỡ câu. OVERSTATED = câu nói rộng hơn bằng chứng (phạm vi, "mọi", nhân quả). Cờ **[NO-EV]** = đoạn có sự
kiện nhưng không có dòng `% EV:`. Đường dẫn mã: `SRC` = `C:/Code/RideBound-noworse/src/`; `GEN` =
`SRC/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs`; các khóa khác như sổ chính.

---

## 1. Bảng kiểm từng câu

| # | Dòng | Câu (rút gọn) | EV | Kết luận | Sửa / anchor đã mở |
|---|---|---|---|---|---|
| 1 | 30-31 | Bộ điều phối làm việc theo từng lượt quyết định | X3-01 | OK | `SRC/RideBound.Contracts/Protocol/EventBatchMessages.cs:42-61` |
| 2 | 33-35 | Đầu vào: trạng thái xe (vị trí, kế hoạch, sức chứa, khách trên xe, khách chờ đón); yêu cầu (đón, trả, khoảng giờ đón, ngồi xe tối đa); bảng giờ đi coi là giữ nguyên | X3-01, X3-02, A05 | OK | `OnlineEventModels.cs:143-153` (trường yêu cầu), `:172-178` (trường xe), `:181`; PREF:13-20 (A05) |
| 3 | 36-37 | Quyết định: nhận hay chưa nhận yêu cầu; mỗi xe đúng một kế hoạch | (không có ID riêng) | OK | Đúng theo `SolverBackedFleetSelection.cs:298-303` và A14; nên thêm X3-07/A14 vào dòng EV 45 |
| 4 | 38-39 | Lời hứa đầu công bố khi xác nhận đặt xe; một dòng sổ cho mỗi lần công bố | A13, A04, X3-13 | OK | WP4:5; `CommitmentDecisionValidator.cs:563-596` (dòng `revision` được thêm khi x, c hoặc z khác 0); SPEC:39-46 |
| 5 | 40-41 | Ràng buộc cứng: cửa sổ đón, ngồi xe, sức chứa, khóa, luật lời hứa | B03, A06, A07 | OK | — |
| 6 | 42-43 | Các thước đo đánh giá (trỏ sang Ch. 4) | — | OK | Chỉ là trỏ chéo |
| 7 | 50-53 | "So với một bộ điều phối ghép chuyến thông thường, RideBound thêm ba việc …" | A06, X3-04, X3-13 | **UNSUPPORTED** | Không dòng sổ nào mô tả "bộ điều phối thông thường"; bước tính lại mốc e đã có ở Hörl–Zwick (J01). Sửa: "Ngoài các bước sinh phương án và chọn bằng bộ giải, mỗi lượt của RideBound có ba bước dành cho lời hứa: tính các mốc giờ trả …, loại phương án vi phạm luật lời hứa trước khi gọi bộ giải, và ghi sổ sau khi chọn." |
| 8 | 64-77 | Hình 3.1 và chú thích ("phần thêm vào so với một bộ điều phối ghép chuyến thông thường"; "Trong thực nghiệm, lớp dự báo được tính lại trên các lần chạy đã ghi") | — | **UNSUPPORTED** **[NO-EV]** | Câu so sánh như #7. Vế dự báo đúng cho Họ A (F03) nhưng Họ B đã chạy dự báo trong bộ điều phối (F12): viết "Trong các kết quả chính, lớp dự báo …". Thêm `% EV: F03; F12` |
| 9 | 94-98 | Giả mã dòng 2–5: áp lô sự kiện; dựng phương án giữ nguyên trước; chèn tối đa 2 yêu cầu mới, giữ thứ tự điểm cũ; giữ tối đa 100 phương án | X3-01, X3-03, A24 | OK | `GEN:196-209` (no-op trước), `GEN:548-575` (chèn cặp, giữ thứ tự `baseStops`); WP4:10-11. Nhánh sửa B4 bị tắt với chính sách hard-vector (`SolverBackedRidePoolingPolicy.cs:125-139`; WP4 không có khóa `repair`) |
| 10 | 100-101 | Giả mã dòng 7: "nếu π vi phạm cửa sổ đón, thời gian ngồi xe hay sức chứa thì loại π" | X3-04 | **WRONG** (với phương án giữ nguyên) | Mã nới cho phương án giữ nguyên phần vượt **giờ đón muộn nhất** và **thời gian ngồi xe tối đa** do tắc đường (ADR-045/047): `GEN:161-164` ("relaxation is applied only to the safety no-op"), `GEN:184-209` (no-op đánh giá với `serviceQuality`), `GEN:231-246` (phương án đã đổi dùng `ServiceQualityAllowance.Strict`); `SRC/RideBound.Domain/Validation/PhysicalPlanValidator.cs:55-66` ("Structural violations are not relaxed"); `ServiceQualityAllowance.cs:85-111` (`_maxRideTimeMs`, `_latestPickupMs`). Sửa: "**nếu** π là phương án đã đổi và vi phạm cửa sổ đón, thời gian ngồi xe hay sức chứa **thì** loại π; phương án giữ nguyên chỉ bị loại khi vi phạm ràng buộc cấu trúc, còn phần vượt cửa sổ đón hay thời gian ngồi xe do tắc đường được nới và ghi lại". Cần một dòng sổ mới cho sự kiện này |
| 11 | 102-104 | Giả mã dòng 8: với mỗi khách đã nhận, tính ba mốc, loại nếu vi phạm khóa hay luật lời hứa | X3-04, A06, A07, A10 | OK | `CommitmentDecisionValidator.cs:233-239, 355-361, 397-404, 494-520` |
| 12 | 105-110 | Giả mã dòng 9–11: xe bị ép chỉ khi mọi lỗi là lỗi hạn chót/trần; giữ phương án giữ nguyên, ghi vi phạm; giữ thêm phương án không làm lỗi tệ hơn | A17, A18, X3-09 | OK | `HardVectorCandidateAssessor.cs:79-99, 257-310`. Về "ghi một vi phạm" xem #75 |
| 13 | 111-117 | Giả mã dòng 12–16: chọn bằng quy hoạch nguyên; nhận yêu cầu; công bố, ghi sổ, cập nhật phần đã dùng | A14, X3-07, A04, A06, X3-13 | OK | Bộ giải là CP-SAT trên biến Boolean, giải theo từng mức (`OrToolsCandidateSelectionSolver.cs:3, 122-125, 343-346`) — "quy hoạch nguyên 0–1" chấp nhận được |
| 14 | 126-127 | "Luật lời hứa là một bộ lọc cứng: phương án vi phạm bị bỏ trước khi bộ giải chạy, không bị phạt trong hàm mục tiêu." | A06, K43 | **OVERSTATED** | Khi xe bị ép, luật phục hồi giữ lại phương án vi phạm và bộ chọn xếp chúng bằng tiêu chí 1 `forced-reference-count` (`HardVectorCandidateAssessor.cs:257-310`; `SolverBackedFleetSelection.cs:276-293`); với luật hạn chót 30 giây điều này xảy ra ở 7.710/20.103 quyết định (N-21). Sửa: "… bị bỏ trước khi bộ giải chạy; ngoại lệ là khi xe bị ép: luật phục hồi giữ lại một số phương án vi phạm và bộ chọn chỉ chọn chúng khi xe không còn phương án khác (tiêu chí 1)." EV ghi sai: K43 nói về việc không cấp lại B, không phải "lọc cứng trước bộ giải"; thay bằng A06 và `HardVectorCandidateAssessor.cs:63-66` |
| 15 | 127-129 | Bộ sinh chỉ chèn thêm đặt đón/trả vào các cặp vị trí, giữ thứ tự cũ, nên không chuyển khách sang xe khác | X3-03, A07 | OK | `GEN:548-575`; TEX08:129-131 (chuyển khách bị cấm ở mọi cấu hình) |
| 16 | 129-131 | Luật loại cả phương án giữ nguyên → xe bị ép, luật phục hồi quyết định | A17, A18 | OK | Thuật ngữ: "xe bị ép" gắn với "(forced decision)" — nên là "quyết định bị ép (forced decision)" |
| 17 | 138-140 | Giờ trả đổi vì ghép thêm khách hay vì giữ kế hoạch mà đường đổi | A01, A02 | OK | — |
| 18 | 142-146 | Định nghĩa v, e, p | A01, A02, X3-04 | OK | `CommitmentDecisionValidator.cs:355-379` (e = kế hoạch cũ chiếu trên `ReducedState` với `ReducedState.TravelTimes`) |
| 19 | 147 | "Ba hiệu sau được tính bằng giây" | A01 | OK | Cài đặt dùng mili giây nguyên (SPEC:50; cấu hình `hardLimit` 30000); trình bày bằng giây không sai |
| 20 | 149-153 | x = e − v, c = p − e, z = p − v = x + c; dòng lời hứa đầu có v = e = p | A01, X3-13 | OK | SPEC:41-50 |
| 21 | 153 | "Luật C chỉ tính c" | A06 | OK | Cấu hình `budgetBasis: decisionInduced` (CFG C-30.json:6; VALID:512-514) |
| 22 | 153-154 | Hörl và Zwick cũng tính lại giờ trả trên tuyến đang gán theo giờ đi hiện tại | J01 | OK | HZ:531-538 |
| 23 | 157-159 | e là giờ trả mô hình tính, không phải giờ đến thật; x gồm bảng giờ đi mới, tiến độ xe, sự kiện vừa xảy ra | A01, A02, X3-04 | OK | — |
| 24 | 159-160 | "Trong các thực nghiệm, thời gian dừng đón, trả bằng 0 giây và tắc đường là một hệ số chung cho cả thành phố theo khung 15 phút." | B05, B06 | **OVERSTATED** | B05 chỉ kiểm 3 lần chạy mẫu (SERV:2-4: C-30 w07, U w08, M⁺-30 w17); B06 anchor là T3.8/w07. Sửa: "Trong ba lần chạy mẫu đã kiểm, thời gian dừng đón, trả bằng 0 giây; trên các tập dùng hệ số đo, tắc đường là một hệ số chung cho cả thành phố theo khung 15 phút." |
| 25 | 160-161 | Phép tách z = x + c là theo mô hình, không phải phép đo nhân quả | K04 | OK | — |
| 26 | 164-187, 189-215 | Ví dụ dựng tay (Bảng 3.2, Hình 3.2): 40 + 30 = 70 giây | (ví dụ dựng tay) | OK | Số học đúng; được đánh dấu là ví dụ dựng tay |
| 27 | 217-218 | Phần dời tính theo độ lớn; sớm hay muộn 20 giây đều tính 20 giây | X3-05 | OK | `SRC/RideBound.Application/Promises/PromiseDeltaCalculator.cs:139, 259-262` |
| 28 | 218-219 | Bộ sinh chỉ chèn thêm không bảo đảm c ≥ 0 theo cấu tạo, nên giữ trị tuyệt đối | ADD1 0.2 | OK | Đúng cách viết của phụ lục 0.2 |
| 29 | 219-220 | "Trên các lần chạy đã có, vế này không có tác dụng đo được: ở tập kiểm tra chính (34 kịch bản), mọi lần điều phối kéo giờ trả sớm hơn e chỉ sớm đúng 1 mili giây." | N-05, ADD1 0.1–0.2 | **OVERSTATED** (phạm vi) | Phép đếm chỉ phủ 4 cấu hình × 34 kịch bản = 136 lần chạy (U 3 lần, C-30 4, C-120 3, M⁺-30 4; ADD1:104-111); M⁺-60, V-30, tập buổi sáng, tập tắc đường cố định, chiều tuyết chưa đếm. Sửa: "Trên các lần chạy đã kiểm, vế này không có tác dụng đo được: ở bốn cấu hình của tập kiểm tra chính (điều phối không trần, luật C 30 và 120 giây, luật hạn chót 30 giây; 136 lần chạy), mọi lần điều phối kéo giờ trả sớm hơn e chỉ sớm đúng 1 mili giây." Không nêu nguyên nhân (đã đúng) |
| 30 | 229-237 | Định nghĩa luật C: B, p0, L_r = 0 lúc xác nhận; L_r + \|p − e\| ≤ B cho khách ở ba giai đoạn; cập nhật L_r | A06, A13, X3-05 | OK | `CommitmentBudgetEvaluator.cs:51, 72-104, 107-114`; CFG C-30.json:17-23; `CommitmentLedger.cs:284-287` |
| 31 | 240 | Đến hết chuyến tổng \|c\| không vượt B | A06 | OK | Theo cấu tạo; dữ liệu: lớn nhất 29,2 s / 118,9 s, 0 vượt (STG:38-39) |
| 32 | 240-241 | B như ngân sách; B − L_r là phần còn lại; không cấp lại | A06, K43 | OK | — |
| 33 | 242-244 | Một mức trần chung, không nới theo tắc đường, cộng cả chuyến; 3 × 30 = 90 giây | E08, J05 | OK | CFG C-30.json:3-5 (một chính sách cho mọi khách) |
| 34 | 244-245 | Ví dụ: \|c\| = 30 = B vẫn được giữ; phần còn lại 0 | X3-05 | OK | `CommitmentBudgetEvaluator.cs:88` (`afterValue > hardLimit` mới loại) |
| 35 | 261-263 | Bảng 3.3, ràng buộc dịch vụ: 10 phút, 1,5 lần, 4 khách; "Loại phương án không khả thi trước khi xét lời hứa" | B03, X3-04 | **OVERSTATED** | Số đúng (B03). Vế vai trò không đúng với phương án giữ nguyên: xem #10. Sửa vai trò: "Loại phương án đã đổi không khả thi trước khi xét lời hứa; với phương án giữ nguyên, phần vượt do tắc đường được nới" |
| 36 | 265-267 | Bảng 3.3, khóa: không đổi xe, điểm đón, điểm trả; giờ đón phải trùng giờ đón khi giữ nguyên; khóa so với e | A07, A08, A10, X3-06 | OK | `CommitmentLockEvaluator.cs:42-60, 112-143, 204-207`; CFG C-30.json:94-98. Ghi chú: "không đổi điểm trả" là trần 0 của chiều `drop_stop_switch_count` (CFG C-30.json:66-67), không nằm trong `finalConfirmationLocks` |
| 37 | 269-270 | Bảng 3.3, luật lời hứa: luật C hoặc luật đối chứng; bộ lọc cứng trước bộ giải | A06, A09, A11, K43 | OK | Ngoại lệ khi xe bị ép như #14. EV: K43 không đỡ vế "lọc cứng" |
| 38 | 273-280 | Bảng 3.3, tiêu chí 1–5 | A14, X3-07, A16, I09 | OK | `SolverBackedFleetSelection.cs:271-385`; `HardVectorCandidateAssessor.cs:612-626` |
| 39 | 297-302 | Bảng 3.4 dòng 2–5: duyệt khách theo thứ tự mã; e_r, p_r, c_r | X3-04 | OK | `CommitmentDecisionValidator.cs:233-239, 257-265, 355-361`; `HardVectorCandidateAssessor.cs:171` |
| 40 | 303-308 | Bảng 3.4 dòng 6–8: loại khi L + \|c\| > B, bản ghi chặn, dừng ở khách gặp trước; cập nhật L khi được chọn | X3-05, A06, A23 | OK | `CommitmentBudgetEvaluator.cs:6-12, 72-104`; `CommitmentDecisionValidator.cs:518-547` |
| 41 | 315-316 | "Phép kiểm dừng ở khách vượt trần gặp trước, nên mỗi bản ghi chặn cho một lý do …" | A23, I08 | **OVERSTATED** (phạm vi) | A23: chỉ khi không bật chế độ thu đủ bản ghi. Tập tắc đường cố định (WP14r) bật `solverExecutionEvidenceProfile: retained-portfolio-full-witness-v1` (NEW:13). Sửa: "Khi không bật chế độ thu đủ bản ghi (như ở tập kiểm tra chính và tập buổi sáng), phép kiểm dừng ở khách vượt trần gặp trước, …" (`CommitmentDecisionValidator.cs:222-231`) |
| 42 | 316-317 | Mười chiều cam kết; giờ trả có trần dương, đổi xe/điểm đón/điểm trả có trần 0 | A04, A07 | OK | `CommitmentDimension.cs:3-15`; CFG C-30.json:7-89. Chỉ 4/10 chiều có `hardLimit` nên chỉ 4 chiều thực sự bị so |
| 43 | 323-324 | Luật loại hết phương án kể cả giữ nguyên → xe bị ép, lời hứa của ít nhất một khách bị phá | A17, A18 | OK | — |
| 44 | 324-325 | Giả thiết (N) | A22 | OK | — |
| 45 | 328-338 | Nhận xét 3.1 và chứng minh (p = e cho phương án giữ nguyên; L_r ≤ B giữ qua các lượt) | A22, A06, X3-03, X3-04 | OK | Theo cấu tạo (A22, VERIFIED-by-Codex R18). Mã: phương án đã chọn và e đều chiếu trên `ReducedState` cùng bảng giờ đi (`CommitmentDecisionValidator.cs:355-361, 1048-1081`) |
| 46 | 341 | Đúng theo cấu tạo, không phải kết quả thực nghiệm; dữ liệu chỉ khớp | K28 | OK | — |
| 47 | 342-343 | 0 quyết định bị ép trong 20.101 (trần 30 giây) và 0 trong 20.435 (trần 120 giây) | A21, N-21, X3-16, N-07 | OK | STG:43-44; ADD1:120-121 |
| 48 | 346-348 | Giới hạn 1: nếu (N) không thỏa (kế hoạch đang chạy vi phạm ràng buộc vật lý) xe vẫn có thể kẹt | A22, X3-03 | OK | `GEN:171-182` |
| 49 | 348-349 | Giới hạn 2: v = 600, e = p = 660 → z = 60, c = 0 | K05 | OK | Số học đúng |
| 50 | 349-351 | Giới hạn 3: v = p = 600, e = 720 → z = 0, \|c\| = 120 | (ví dụ dựng tay) | OK | Số học đúng |
| 51 | 359-360 | "Chương 4 so luật C với bốn luật khác chạy trên cùng bộ điều phối." | — | **OVERSTATED** **[NO-EV]** | Ghép tự do dùng chính sách chi phí cuốn chiếu, không qua bộ kiểm cứng và bộ chọn của luật C (HO:109 "FREE (b1-rolling-cost)"; A17); trên tập tắc đường cố định mọi cấu hình chạy bằng bộ chạy cũ (B17). Sửa: "Chương 4 so luật C với bốn cấu hình khác. Điều phối không trần, luật hạn chót và luật trần độ dời khách thấy dùng cùng bộ sinh, bộ kiểm và bộ chọn với luật C; ghép tự do dùng chính sách chi phí cuốn chiếu." Thêm `% EV: A08; A17; B17; K50` |
| 52 | 374-376 | Bảng 3.5, U: không kiểm giờ trả; khóa xe, điểm đón, giờ đón, không đổi điểm trả; không bị ép vì khóa so với e; dùng ở tập chính, buổi sáng, tắc đường cố định (LOCKS) | A07, A08, K50, A10, X3-16, B10, B15, B17 | OK | STG:42 (0/20.760); NEW:11 (cấu hình cam kết WP14 trùng byte U.json, sha 998a0a94) |
| 53 | 378-379 | Bảng 3.5, FREE: không kiểm; chính sách chi phí cuốn chiếu mặc định; không khóa; tập tắc đường cố định | A17, K50, B17 | OK | Vế "chi phí cuốn chiếu" chỉ có ở HO:109 (anchor của K50), không phải câu của dòng sổ nào; nên ghi HO:109 vào EV |
| 54 | 381-383 | Bảng 3.5, C: Σ\|c\| ≤ B; khóa như U; không bị ép theo cấu tạo; tập chính (30, 120), buổi sáng (30–300), tắc đường cố định (30, 60, 120), chiều tuyết (30) | A06, A22, B10, L1a-01, D01, B15, B16, B17, B20, N-26 | OK | — |
| 55 | 385-386 | Bảng 3.5, M⁺: p − p0 ≤ B, chỉ phía muộn; phục hồi không tệ hơn; tập chính (30, 60), buổi sáng (30–300) | A09, A19, B10, D04, B15, B16 | OK | `CommitmentLockEvaluator.cs:186-197`; CFG Mplus-30.json:98 (một phía, không có `dropEtaDeadlineTwoSided`) |
| 56 | 388-389 | Bảng 3.5, V: Σ\|z\| ≤ B; tập chính (30), buổi sáng (30) | A11, A19, B10, B15 | OK | CFG V-30.json:6 `customerVisible` |
| 57 | 395-396 | "Luật hạn chót chỉ mượn phần hạn chót của Schulz và Pfeiffer, ở mức 30–60 giây thay vì 900 giây" | J10, J11 | **WRONG** | Mâu thuẫn với Bảng 3.5 của chính chương: luật hạn chót chạy ở 30–300 giây trên tập buổi sáng (B15, B16, D04: 30/60/90/120/150/180/240/300). J11 chỉ nói về tập chính. Sửa: "ở mức 30–300 giây (tập kiểm tra chính: 30 và 60 giây) thay vì 900 giây" |
| 58 | 396-397 | Trên tập tắc đường cố định, điều phối không trần mang tên cũ LOCKS, chạy bằng bộ chạy cũ không có luật phục hồi | B17, K33 | OK | HO:236 "LOCKS (= U)"; NEW:11 (cấu hình cam kết trùng byte U.json); NEW:13 (bộ chạy khác: `policyVersion wp14-development-v1`, không có `commitmentRecovery`) |
| 59 | 397-398 | Phụ lục A gọi B1 (không khóa, không trần) và C1 (khóa + trần 30 giây) | X3-18 | OK | TEX08:128-136 |
| 60 | 401-407 | Với chuỗi liên tục, Σ(x + c) = Σz = p_k − p0; luật hạn chót cộng có dấu, luật V cộng \|z\|, luật C cộng \|c\| | A12, A09, A11 | OK | SPEC:50, 62-63 |
| 61 | 407-410 | Ví dụ: nếu 9:10:00 là lời hứa đầu, giữ nguyên có e − p0 = \|z\| = 40 > 30 với cả hai luật, dù c = 0 | A10 | OK | `CommitmentLockEvaluator.cs:156-161`; số học đúng |
| 62 | 413 | "Gần nhất với cách đo này là Hörl và Zwick" | J01 | **OVERSTATED** (nhẹ) | So sánh bậc nhất trên toàn văn liệu, chưa có khảo sát đầy đủ (J01 gọi là "tiền lệ quyết định"). Sửa: "Tiền lệ trực tiếp của cách đo này là Hörl và Zwick" |
| 63 | 413-416 | Mỗi lượt họ duyệt tuyến đang gán theo giờ đi hiện tại; công thức 7 = max(giờ cập nhật, giờ trả muộn nhất) cho khách trên xe đang xét, kèm phạt mỗi giây vượt | J01, J03 | OK | HZ:531-543 (chiến lược B), HZ:562-606 (công thức 7, ràng buộc 9–10, phạt 11) |
| 64 | 416-417 | max(p0 + B, e) là cách viết lại của khóa luận, không phải định nghĩa trong bài | J05 | OK | — |
| 65 | 417-418 | Hạn chót nới này cũng có tính chất của Nhận xét 3.1; suy luận, chưa chạy | A22 | OK | A22 lưu ý "[suy luận, V17 R6]" |
| 66 | 418-419 | Luật C khác ở ba chỗ: một trần chung cho mọi khách đã nhận, không nới theo tắc đường, cộng cả chuyến | J05, K26 | OK | Ghi chú: "một trần chung cho mọi khách" là khác biệt so với chiến lược B gốc (chỉ nới cho khách sắp vi phạm), không so với dạng viết lại max(p0 + B, e). Nên viết "So với chiến lược B của họ, luật C …". Không dùng "cứng thay vì phạt" (K26 đạt) |
| 67 | 422-424 | Bộ chọn chọn mỗi xe đúng một phương án bằng quy hoạch nguyên, giải bằng OR-Tools, theo thứ tự tiêu chí | A14, X3-07 | OK | CP-SAT, nhiều lượt giải theo mức (`OrToolsCandidateSelectionSolver.cs:3, 92, 122-125, 184-213`) |
| 68 | 424 | Tiêu chí 1 chỉ có mặt khi có xe bị ép | A14, X3-07 | OK | `SolverBackedFleetSelection.cs:276-293` |
| 69 | 424-426 | Tiêu chí 3 bật cả khi chỉ có trần 0; phần đầu không phân biệt phương án vì chiều trần 0 tính là dùng hết | X3-07, A15 | OK | `SolverBackedFleetSelection.cs:271-272, 318-327`; `HardVectorCandidateAssessor.cs:612-626` |
| 70 | 426-428 | 1.000.000 phần triệu ở mọi lượt có mức: 3.503 / 3.506 / 3.504 | A15, N-25 | OK | ADD1:119-121 (`util_present` = `incumbent_1e6` = `bound_1e6`) |
| 71 | 431-432 | U và luật C cùng tệp chính sách, cùng bộ chọn, chỉ khác trần giờ trả | A08, H01 | OK | `diff U.json C-30.json` (chỉ `hardLimit` 30000); NEW:12 |
| 72 | 432-433 | Kết quả với bộ chọn ưu tiên chi phí chưa kiểm | H02, K18 | OK | — |
| 73 | 436-438 | Luật giữ nguyên kế hoạch: giữ làm phương án bị ép, ghi vi phạm, nếu mọi lỗi là hạn chót/trần | A17, A18, X3-09 | OK | `HardVectorCandidateAssessor.cs:79-90, 257-283` |
| 74 | 438-439 | Luật không tệ hơn: giữ phương án mắc cùng lỗi, không tệ hơn; khóa xe và khóa giai đoạn không bao giờ được miễn | A18 | OK | ADR:5080-5092 (mục 2 ở dòng 5086); `CommitmentDecisionValidator.cs:414-420` |
| 75 | 439 | "… và mỗi lần miễn được ghi thành vi phạm" | A18 | **OVERSTATED** | Mã chỉ ghi một bản ghi vi phạm mới khi lời hứa đổi, giai đoạn của khách đổi hoặc bộ mã lỗi đổi; một lần miễn lặp lại với cùng đầu vào không ghi thêm (`CommitmentDecisionValidator.cs:618-637`, cũng chú thích ở `:134`). ADR-077 mục 3 (ADR:5087) chỉ nói "miễn trừ trên tuyến đã đổi được ghi thành loại vi phạm mới ForcedNoWorse". Sửa: "… và mỗi miễn trừ được ghi thành vi phạm; một lần miễn lặp lại với cùng lời hứa, cùng giai đoạn và cùng lỗi không ghi thêm bản ghi." Cũng áp cho "ghi một vi phạm" ở Bảng 3.1 dòng 10 nếu muốn chặt |
| 76 | 439-440 | Tập chính và tập buổi sáng dùng luật không tệ hơn cho mọi cấu hình | A19, X3-10 | OK | RUN38:9; `run_w07.py:8`; `run_w07x.py:7`; `run_t38c120.py:3-8`; WP4:7 |
| 77 | 447-448 | Lời hứa không dự báo giả định bảng giờ đi giữ nguyên, nên khi đường đông dần lời hứa sớm hơn giờ đến thật | A05, F10 | OK | — |
| 78 | 448-450 | Lời hứa theo dự báo là cách làm đã có trong thực tiễn; cộng sẵn mức tăng của các ngày trước | J35, F01 | OK | J35 là VERIFIED-by-Codex R13 (web) |
| 79 | 452-463 | Công thức 3.5: ∫ dτ/g = p − t; g = 1 trong khung hiện tại, m(b)/m(b0) sau; D = max(p, S); mức hiện tại từ bảng giờ đi, ngày khác chỉ cho hình dạng | F01, X3-11 | OK | STRETCH:1-12, 25-39, 49-52; DISP:1-8, 60-64. Thiếu nhỏ: g được giữ nguyên từ khung thứ 8 (`HOLD_BIN`) trở đi (STRETCH:7-8, 45, 51) |
| 80 | 463-464 | max làm lời hứa không bao giờ bị rút ngắn | F01 | OK | DISP:64 |
| 81 | 467-469 | Ngày nguồn: cùng loại, trước ngày kịch bản, bỏ 15/11, ≥ 2 ngày; chỉ 14, 15, 16/11 có dự báo | F02 | OK | DISP:10-16, 34-52 |
| 82 | 469-470 | 21/34 kịch bản có dự báo; 13 kịch bản ngày 17, 18/11 giữ lời hứa không dự báo | F04, N-16, N-28 | OK | STG:4 ("forecast-active cells 21"); 7 + 6 = 13 kịch bản cuối tuần (bảng N-22) |
| 83 | 478-501 | Bảng 3.6 (giả mã dự báo) | F01, F02, X3-11 | OK | DISP:34-64; STRETCH:25-39, 49-52 |
| 84 | 505-506 | Phát lại: quyết định không đổi, chỉ lời hứa đổi | F03 | OK | FR:10 |
| 85 | 506-507 | D0 là lời hứa đầu có dự báo; giá = D0 − p0 | X3-12, F06 | OK | FFA:86, 93, 113 |
| 86 | 507-509 | Dưới trần 30 giây, 34 trong 1.471 khách (21 kịch bản) có lời hứa giờ đón hiển thị muộn hơn giờ đón muộn nhất; do phép kiểm khả thi dùng giờ không dự báo | F07 | OK | FR:70 (mục C-30, 21 ô, FR:36). Chính xác hơn: "lời hứa giờ đón **đầu tiên** hiển thị" (FFA:87-89, 99) |
| 87 | 509-510 | Phép thử dự báo trong bộ điều phối ở mục 4.x | F12 | OK | — |
| 88 | 517-519 | Sổ: một dòng lời hứa đầu và một dòng mỗi lần cập nhật; v, e, p; \|x\|, \|c\|, \|z\| trên 10 chiều; phần trần đã dùng; trạng thái cuối chứa toàn bộ sổ | A04, A06, X3-13 | OK | SPEC:35-46; `PromiseDeltaCalculator.cs:64-160`; `CommitmentLedger.cs:284-287` |
| 89 | 519-524 | Sau khi chạy, chia a − p0 thành q + f + phần còn lại | X3-12 | OK | FFA:91, 134-137 |
| 90 | 527-528 | q là tổng có dấu; \|q\| ≤ Σ\|c\| ≤ B dưới luật C | X3-12, A06 | OK | FFA:91 (`sum(r[5] - r[4] …)`); bất đẳng thức tam giác |
| 91 | 528-529 | f bằng 0 khi không có dự báo | X3-12 | OK | DISP:16 (kịch bản không hoạt động hiển thị D = p) |
| 92 | 529-531 | Khi chuỗi liên tục, phần còn lại = Σx + ρ − f | A12 | OK | Đại số kiểm lại: a − D0 − q = (a − p_k) + Σ(x + c) − f − Σc |
| 93 | 531-532 | Ch. 4 cộng ba phần trên khách trễ hơn lời hứa đầu quá 60 giây | F09 | OK | FFA:134 (`A − P0 > 60_000`) |
| 94 | 535-538 | Phép tính theo mô hình, không kết luận ai có lỗi; phần còn lại không phải "không thể biết trước" | K04, F09, K19 | OK | — |
| 95 | 548-549 | C# trên .NET 10, dự án theo tầng, phụ thuộc từ ngoài vào trong | X3-14 | OK | Anchor cần sửa: `Directory.Build.props` **không** có `TargetFramework`; `net10.0` nằm trong từng `.csproj` (ví dụ `RideBound.Domain.csproj:4`) |
| 96 | 549-551 | Domain không tham chiếu gì; Application → Domain; OR-Tools chỉ ở cầu nối bộ giải; bộ kiểm thử kiến trúc | X3-14 | OK | `tests/RideBound.ArchitectureTests/DependencyRuleTests.cs:8-30` (bảng phụ thuộc), `:95-135`, `:137-166` (OR-Tools 9.15.6755 chỉ ở `RideBound.Solvers.OrTools.csproj`) |
| 97 | 551-552 | Nhờ vậy phép kiểm trần, ba mốc, sổ không phụ thuộc bộ mô phỏng hay bộ giải | X3-14 | OK | Suy ra từ #96 |
| 98 | 562-576 | Bảng 3.7 (vai trò các dự án) | X3-14, X3-15, NORM, B01 | OK | Bảng bỏ qua dự án `RideBound.Infrastructure` (Runner tham chiếu nó: `RideBound.Runner.csproj:7`) — chấp nhận được vì là "thành phần chính" |
| 99 | 582 | FleetPy 1.0.2 với bộ dữ liệu chuẩn Manhattan | B01, J18 | OK | FLEET:474; `simulators/fleetpy-ridebound/README.md:1, 7-10` (tag 1.0.2 ghim) |
| 100 | 582-584 | Bộ chuyển đổi Python khởi động bộ chạy như tiến trình con, trao đổi qua stdin/stdout, mỗi bản tin một dòng JSON | X3-15 | OK | `runner_client.py:133-136`; `Program.cs:104-106`; `NdjsonReader.cs`, `NdjsonWriter.cs` |
| 101 | 585-586 | Bộ chạy từ chối lô mới khi quyết định trước chưa được báo đã áp dụng | X3-15 | OK | `RunnerSession.cs:448-455` |
| 102 | 586-587 | Bản tin của mỗi lần chạy được lưu; số ở Ch. 4 tính từ bản ghi này | X3-13, A26 | OK | SPEC:28-37 |
| 103 | 596-611 | Hình 3.3: chào hỏi, khởi tạo, đã khởi tạo, lô sự kiện, quyết định, đã áp dụng, yêu cầu trạng thái → trạng thái gồm sổ | X3-15 | OK | `RunnerSession.cs:177-208`; `runner_client.py:158, 178, 207, 235, 246-258` (thiếu nhỏ: `helloAck`) |
| 104 | 612-613 | Hình 3.3: "kết thúc lần chạy" → "tóm tắt lần chạy" | X3-15 (ProtocolPrimitives.cs:104-124) | **WRONG** | `finalizeRun` và `runSummary` chỉ được khai báo (`ProtocolPrimitives.cs:114-115`) nhưng bộ chạy không xử lý: `RunnerSession.cs:203-208` chỉ nhận `hello`, `initializeRun`, `eventBatch`, `decisionApplied`, `checkpoint`, `restore`; loại khác trả lỗi `INVALID_SESSION_STATE` (`:209-213`). Bộ chuyển đổi không gửi `finalizeRun` (`runner_client.py` chỉ có hello, initializeRun, eventBatch, decisionApplied, checkpoint, restore, shutdown; `:260-273`). Lần chạy kết thúc bằng `shutdown`, bộ chạy dừng, không trả lời (`RunnerSession.cs:177-189`). Sửa: thay hai mũi tên cuối bằng một mũi tên "kết thúc (shutdown); bộ chạy dừng" |
| 105 | 624-626 | Tối đa 100 phương án và 2 yêu cầu mới mỗi xe trong một lượt; giới hạn khối lượng; OR-Tools 9.15, hạt giống 7; không vét cạn | A24, X3-17 | OK | WP4:9-23. Chính xác hơn: giới hạn 2 yêu cầu áp cho cả lô của lượt — chỉ 2 yêu cầu đang chờ đầu tiên (theo giờ đón muộn nhất, giờ gọi, mã) được xét cho mọi xe, phần còn lại bị bỏ qua ở lượt đó (`GEN:73-94`) |
| 106 | 626 | Mục 4.x báo bộ đếm cho biết giới hạn có cắt phương án không | N-25 | OK | ADD1:119-122 |
| 107 | 626-628 | Khối lượng kiểm ở một xe tỉ lệ với số phương án × số khách × độ dài kế hoạch | X3-04, X3-05 | OK | Suy ra từ mã, chưa đo: mỗi khách chiếu lại kế hoạch cũ (`CommitmentDecisionValidator.cs:355-361` trong vòng khách `:233-239`), mỗi phương án chiếu kế hoạch của một xe (`:1048-1081`). Nên viết "tăng theo" thay "tỉ lệ với" |
| 108 | 631, 633 | "Thời gian chạy chỉ được đo cho cả lần chạy"; "Chi phí thêm của phép kiểm trần ở từng lượt quyết định chưa được đo riêng" | H13 | **UNSUPPORTED** | Không dòng sổ nào nói không có phép đo khác; kho mã có công cụ đo vi mô `tools/RideBound.CandidateHotPathBenchmark` và `tools/RideBound.Wp4Microbenchmark` mà tôi không kiểm phạm vi. Sửa: "Khóa luận chỉ báo thời gian chạy của cả lần chạy: …; chi phí thêm của phép kiểm trần ở từng lượt quyết định không được báo riêng." |
| 109 | 631-633 | Tập tắc đường cố định, 16 lần chạy mỗi cấu hình, bộ chạy cũ; trung vị 730 / 667 / 641 giây | H13, X3-19, B17 | OK | EL17:2-6 (b1-ref / c1-nobudget / c1-h6ref) |
| 110 | 641-643 | Khi thêm luật không tệ hơn, bộ kiểm thử qua 1.025/1.025; số lịch sử, không chạy lại | A27 | OK | ADR:5100 ("1025/1025, tức 1005 cũ cộng 20 test mới") |
| 111 | 644-646 | 382.006 lần cập nhật giờ trả của 185 lần chạy (170 + 15); \|x\|, \|c\|, \|z\| khớp sổ | A26, B10 | OK | T38I:68; T38:6. Từ ngữ: "170 lần chạy của **năm cấu hình**" (M⁺-30 và M⁺-60 là cùng một luật) |
| 112 | 647-648 | Một chương trình viết riêng tính lại 13 hạng mục, không hạng mục nào lệch | C19 | OK | T38I:79-97 (13 dòng "match" và một dòng "consistent" cho bất biến) |
| 113 | 648-649 | Số đếm chính được ba chương trình đọc bản ghi tính lại và khớp nhau | N-03, N-06, N-07, C04, E01 | OK | Theo K41 nên thêm "trong phạm vi đã kiểm" |
| 114 | 649-651 | Chương trình kiểm do Claude và Codex viết và chạy; cho biết số khớp bản ghi, không cho biết mô phỏng giống thực tế | A26, C19, K41, I01 | OK | — |
| 115 | 652-653 | Tập chính và tập buổi sáng dùng cùng bản chạy lưu trữ có luật phục hồi; tập tắc đường cố định dùng bản cũ không có luật phục hồi | A28, X3-10, B17 | OK | `run_w07.py:8, 39-42`; NEW:13 |
| 116 | 653-654 | Bản dựng lại phải cho đúng kết quả cũ trước khi dùng | I13 | OK | Là quy tắc quy trình, không phải kết quả |

---

## 2. Kiểm X3-01…X3-19 với mã nguồn

| ID | Kết luận | Ghi chú (anchor tôi đã mở) |
|---|---|---|
| X3-01 | OK | `EventBatchMessages.cs:42-61`: 14 loại sự kiện, gồm hai loại hủy và hai loại sự cố |
| X3-02 | OK | `OnlineEventModels.cs:143-153` (yêu cầu), `:172-178` (xe), `:181` (cạnh giờ đi) |
| X3-03 | OK, thiếu một ý | Đúng các vế đã ghi (`GEN:161-164, 171-182, 196-229, 548-575, 691-693`). Thiếu: phương án giữ nguyên được nới phần vượt giờ đón muộn nhất và thời gian ngồi xe do tắc đường, phương án đã đổi thì không (`GEN:161-164, 184-209, 231-246`; `PhysicalPlanValidator.cs:55-66`; `ServiceQualityAllowance.cs:85-111`) — xem #10, #35 |
| X3-04 | OK | `CommitmentDecisionValidator.cs:201-214, 233-239, 355-361, 404-411, 494-499, 512-520`; `HardVectorCandidateAssessor.cs:171` |
| X3-05 | OK | `CommitmentBudgetEvaluator.cs:6-12, 72-104, 107-114`; `PromiseDeltaCalculator.cs:139, 259-262` |
| X3-06 | OK | `CommitmentLockEvaluator.cs:42-60, 156-161, 186, 204-207`; CFG C-30.json:94-98 (không có `ratchetLocks`). Lưu ý: "điểm trả" là trần 0, không phải khóa |
| X3-07 | OK | `SolverBackedFleetSelection.cs:271-303, 319-330, 365-385, 510-522`; `HardVectorCandidateAssessor.cs:612-626`. Bộ giải là CP-SAT (`OrToolsCandidateSelectionSolver.cs:3`) |
| X3-09 | OK, thiếu một ý | `HardVectorCandidateAssessor.cs:79-99, 257-310`; `SolverBackedRidePoolingPolicy.cs:322-334`. Thiếu: bản ghi vi phạm không lặp lại khi đầu vào không đổi (`CommitmentDecisionValidator.cs:618-637`) — xem #75 |
| X3-10 | OK | `run_w07.py:8, 39-42`; `run_w07x.py:7`; `run_t38c120.py:3-8` |
| X3-11 | OK | DISP:1-16, 34-57, 60-64; STRETCH:1-12, 25-39, 49-52. Thiếu nhỏ: giữ hệ số từ `HOLD_BIN` |
| X3-12 | OK | FFA:86, 91, 93, 134-137 (sổ chia ba phần ở 134-137; dòng 138 là tổng) |
| X3-13 | OK | SPEC:35-37 (trạng thái cuối), 39-46 (sổ, v = e = p), 48-50, 62-63 |
| X3-14 | OK, sửa anchor | `Directory.Build.props` không chứa `net10.0`; `TargetFramework net10.0` ở từng `.csproj`. Phần phụ thuộc và kiểm thử kiến trúc đúng (`DependencyRuleTests.cs:8-30, 95-135, 137-166`) |
| X3-15 | **Một phần sai** | Danh sách loại bản tin đúng là danh sách khai báo (`ProtocolPrimitives.cs:104-124`), nhưng `finalizeRun`/`runSummary` không được bộ chạy xử lý và bộ chuyển đổi không gửi (xem #104). Các vế còn lại đúng: `RunnerSession.cs:448-455`; `Program.cs:104-106`; README:1-12; `runner_client.py:133-136` |
| X3-16 | OK | STG:42-43 (U 0/20.760; C-30 0/20.101) |
| X3-17 | OK | WP4:9-23 |
| X3-18 | OK | TEX08:128-136 |
| X3-19 | OK | EL17:2-6 |

Đề nghị thêm vào sổ (nếu giữ các câu tương ứng): (a) phương án giữ nguyên được nới phần vượt do tắc đường (#10);
(b) bản ghi vi phạm không lặp lại (#75); (c) `finalizeRun`/`runSummary` không dùng (#104); (d) bộ giải là CP-SAT
nhiều lượt (#13, #67); (e) FREE = chính sách chi phí cuốn chiếu (HO:109, #53); (f) cấu hình cam kết LOCKS trùng byte
U.json (NEW:11, #58).

---

## 3. Mẫu số và nhãn "trung bình theo ô / gộp theo khách"

Chương 3 không có tỉ lệ phần trăm nào; mọi con số là số đếm có mẫu số rõ: 0/20.101 và 0/20.435 quyết định (STG:43-44),
3.503/3.506/3.504 lượt có mức (ADD1:119-121), 21/34 kịch bản, 13 kịch bản, 34/1.471 khách (FR:70, đúng mẫu số "khách
được phục vụ của C-30 trên 21 kịch bản"), 382.006 lần cập nhật / 185 lần chạy, 13 hạng mục, 1.025/1.025, trung vị trên
16 lần chạy. Không có chỗ nào cần nhãn trung bình theo ô / gộp theo khách. Đơn vị: chương nói "giây" còn cài đặt dùng
mili giây — chấp nhận được.

## 4. Câu cấm (sổ mục K và brief)

Tôi tìm trong mọi dòng không phải chú thích các từ: duy nhất, đầu tiên, vượt trội, đột phá, tối ưu, chúng tôi, niêm phong,
dự đoán, quy trách, lần đầu, cốt lõi, không ai, hài lòng, doanh thu, khiếu nại, cấp lại, lường trước, đăng ký trước, sổ
cái, gây ra, nguyên nhân, mạng đường, tắc đường thật. **Không có lần dùng bị cấm.** "Không thể biết trước" chỉ xuất hiện
trong câu phủ định đúng K19 (dòng 538); "không phải phép đo nhân quả" (160-161) đúng K04; "luật C không bảo đảm giờ đến
thật" (349) đúng K05; "trần không được cấp lại" (241) đúng K43; "Nhận xét đúng theo cấu tạo … dữ liệu chỉ khớp" (341)
đúng K28; bảng luật ghi U vẫn khóa (K50). Không nhắc kế hoạch niêm phong, mã băm kế hoạch hay dự đoán trước. Lưu ý khi
sửa #14: không dùng "ngoại lệ duy nhất".

## 5. Dòng EV ghi sai hay thiếu (không đổi kết luận)

- Dòng 132 và 271: K43 được trích cho "lọc cứng trước bộ giải", nhưng K43 nói về việc không cấp lại B. Thay bằng A06 và
  `HardVectorCandidateAssessor.cs:63-66`.
- Dòng 45: thiếu A14/X3-07 cho vế "chọn cho mỗi xe đúng một kế hoạch".
- Dòng 553: anchor `Directory.Build.props net10.0` sai tệp (xem X3-14).
- Dòng 384: N-26 đúng nhưng chỉ nằm trong EV, không trong văn bản (đã ghi trong NOTES §4).
- Đoạn 359-360 và Hình 3.1: không có dòng EV (#8, #51).

## 6. Tổng hợp

| Kết luận | Số câu/hàng |
|---|---:|
| OK | 102 |
| WRONG | 3 (#10, #57, #104) |
| UNSUPPORTED | 3 (#7, #8, #108) |
| OVERSTATED | 8 (#14, #24, #29, #35, #41, #51, #62, #75) |
| **Tổng** | **116** |
| Cờ [NO-EV] | 2 đoạn (#8, #51) |
| X3: OK / OK thiếu ý / sửa anchor / một phần sai | 14 / 2 (X3-03, X3-09) / 1 (X3-14) / 1 (X3-15) |

**Mười chỗ cần sửa quan trọng nhất (theo thứ tự)**
1. #104 — Hình 3.3: bỏ "kết thúc lần chạy → tóm tắt lần chạy"; lần chạy kết thúc bằng `shutdown`, bộ chạy không trả lời
   (`RunnerSession.cs:177-189, 203-213`; `runner_client.py:260-273`).
2. #57 — "30–60 giây thay vì 900 giây" mâu thuẫn Bảng 3.5: luật hạn chót chạy ở 30–300 giây trên tập buổi sáng (B15, B16, D04).
3. #10, #35 — Giả mã dòng 7 và Bảng 3.3: phương án giữ nguyên không bị loại vì vượt giờ đón muộn nhất hay thời gian ngồi
   xe do tắc đường; mã nới cho nó (`GEN:161-164, 184-209, 231-246`).
4. #14 — "bộ lọc cứng … không bị phạt trong hàm mục tiêu": sai khi xe bị ép (luật phục hồi giữ phương án vi phạm, tiêu
   chí 1 xếp chúng; M⁺-30 bị ép ở 7.710/20.103 quyết định, N-21).
5. #75 — "mỗi lần miễn được ghi thành vi phạm": mã không ghi lại lần miễn lặp với cùng đầu vào
   (`CommitmentDecisionValidator.cs:618-637`).
6. #29 — "−1 mili giây" chỉ đã kiểm ở 4 cấu hình × 34 kịch bản (136 lần chạy; ADD1:104-111), không phải "các lần chạy
   đã có" hay mọi cấu hình của tập chính.
7. #51 — "bốn luật khác chạy trên cùng bộ điều phối": ghép tự do dùng chính sách chi phí cuốn chiếu (HO:109), tập tắc
   đường cố định dùng bộ chạy cũ (B17); đoạn này cũng thiếu dòng EV.
8. #7, #8 — "So với một bộ điều phối ghép chuyến thông thường …" không có bằng chứng; Hörl–Zwick đã tính mốc e (J01).
9. #108 — "Thời gian chạy chỉ được đo cho cả lần chạy": không có bằng chứng; kho mã có công cụ đo vi mô chưa kiểm. Viết
   "khóa luận chỉ báo …".
10. #24 và #41 — phạm vi: thời gian dừng 0 giây chỉ kiểm ở 3 lần chạy mẫu (SERV:2-4); "dừng ở khách gặp trước" không
    đúng cho tập tắc đường cố định, nơi bật chế độ thu đủ bản ghi (NEW:13).

Các chỗ nhỏ khác nên sửa luôn: #62 "Gần nhất" → "Tiền lệ trực tiếp"; #66 "So với chiến lược B của họ"; #105 giới hạn
2 yêu cầu áp cho cả lô; #111 "năm cấu hình"; #113 thêm "trong phạm vi đã kiểm" (K41); #86 "lời hứa giờ đón đầu tiên".

*Hết. Viết bởi Claude (fact checker R23), 2026-10-11. Chỉ tạo tệp này.*
