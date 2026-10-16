# R23 — Chapter 3 method review by Codex

Reviewed: 2026-10-11. **Verdict: ACCEPT WITH REQUIRED CHANGES; do not integrate the present draft unchanged.** The scalar definition of C, its remaining allowance, the conditional keep-route argument, and the two ledger identities are sound. Several descriptions of the executed method are inaccurate or incomplete.

## 1. Scope and evidence standard

I read ROUND23-CLAUDE.md, the 662-line draft and NOTES, WRITING-BRIEF, the Chapter 3/4 outline, REVIEW-DECISIONS-R20, and the relevant register entries, including Addendum §0 before relying on the corrected numbers. I opened the cited implementation files read-only and checked all X3 identifiers; X3-08 is explicitly merged into X3-07. I consulted the two DOI records, primary publisher/repository metadata, and the existing bibliography.

No simulations, builds, installations, thesis edits, or draft edits were performed. I did not read rewrite-2026-10/reviews/R23-*. This file is the only deliverable.

**AGREE** means the assertion follows from the definition, inspected code, or the saved output cited here, within its stated scope. It does not mean I freshly recomputed every raw transcript this round. **WRONG** includes a false scope or an omitted condition that changes the stated method. **CANNOT CHECK** identifies a genuine evidence or integration limit.

Paths below:

- **DRAFT** = S/rewrite-2026-10/drafts/07-chuong3.tex; **NOTES** = the adjacent 07-chuong3-NOTES.md.
- **S/** = E:/Code/Report_INT3508/ridebound-scratchpad/.
- **SRC/** = C:/Code/RideBound-noworse/src/; **R/** = C:/Code/RideBound-noworse/.
- **REG** = S/rewrite-2026-10/evidence/EVIDENCE-REGISTER.md; **ADD** = EVIDENCE-REGISTER-ADDENDUM-1.md in that directory.
- **ADD1** = its checks-addendum-1/recompute-addendum-1-2026-10-11.txt.
- **STG** = S/optimize/codex-debate/claude-work/r21-stage1a/stage1a-report-2026-10-10.txt.
- **T38I** = S/tang3/t38/independent/RESULT.md.
- **HZ** = S/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.txt.
- **SEL**, **POL**, **HVA** = SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs, SolverBackedRidePoolingPolicy.cs, and SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs.
- **VALID**, **DELTA**, **PROJ** = SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs, Promises/PromiseDeltaCalculator.cs, and Scheduling/RouteScheduleProjector.cs.
- **BE**, **LEDGER**, **LOCK** = SRC/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs, CommitmentLedger.cs, and CommitmentLockEvaluator.cs.
- **GEN** = SRC/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs.

References to local extracted PDFs use newline-delimited physical lines, not splitlines() across form-feed characters.

## 2. Ranked required changes, with replacement text

### 1. Correct the decision procedure, its physical checks, and promise lifecycle

**DRAFT:96–115, 126–131, 231–232, 261–270, 293–307.**

The implementation probes the existing route for exogenous service-quality overruns and permits those overruns on the safety keep-route candidate. Changed candidates use strict service-quality bounds. Capacity and other structural failures remain fatal. A blanket “reject whenever the pickup window or maximum ride time is violated” does not reproduce the implementation.

Sources: GEN:161–244, 734–754; SRC/RideBound.Domain/Validation/ServiceQualityAllowance.cs:61–93. This exception is distinct from commitment recovery (a)/(b).

The selected plans must also satisfy **at most one vehicle per new request**. The present pseudocode only specifies one plan per vehicle. Source: SRC/RideBound.Solvers.OrTools/OrToolsCandidateSelectionSolver.cs:348–364. This omission can make the pseudocode accept the same request twice.

A provisional Accepted booking has no published promise yet under booking-confirmation mode; VALID:272–301 explicitly skips its commitment check. Initial publication and L=0 begin on confirmation, not on the provisional offer. WP4:5 selects that mode. A plan being evaluated must not consume the actual ledger or create an actual breach merely because it was considered.

Replace the physical-check description with:

> Các phương án đổi kế hoạch phải thỏa cửa sổ đón, thời gian ngồi xe tối đa và sức chứa. Riêng phương án giữ nguyên được kiểm với phần nới cho những vi phạm thời gian dịch vụ mà kế hoạch đang chạy đã có trên trạng thái và bảng giờ đi hiện tại; phần nới này không áp dụng cho phương án đổi kế hoạch. Sức chứa và các ràng buộc cấu trúc vẫn được kiểm nghiêm ngặt. Việc nới này khác với luật phục hồi vi phạm lời hứa ở mục~\ref{muc:doichung}.

Replace the scope sentence in the C definition, and propagate it to both pseudocode inputs:

> Phép kiểm áp dụng cho khách đã có lời hứa ban đầu và còn hoạt động trên xe đang xét. Trong cấu hình dùng ở đây, lời hứa ban đầu được mở khi khách xác nhận đặt xe và khi đó \(L_r=0\); một khách mới chỉ nhận lời mời nhưng chưa xác nhận chưa có sổ lời hứa để kiểm trần.

Retain the configured phase list, but distinguish **phase applicability in the configuration** from **existence of an initialized ledger**.

Use this corrected abstract decision procedure; it is a method description, not source code to paste:

1. Áp lô sự kiện và lấy trạng thái cùng bảng giờ đi dùng cho lượt này.
2. Với mỗi xe, thăm dò kế hoạch đang chạy; nếu có lỗi cấu trúc không thể xử lý thì trả lỗi.
3. Dựng phương án giữ nguyên với phần nới thời gian dịch vụ đã xác định; sinh các phương án đổi kế hoạch theo kiểm tra dịch vụ nghiêm ngặt, với tối đa 2 yêu cầu mới và 100 phương án giữ lại.
4. Kiểm từng phương án và các khách đã có lời hứa còn hoạt động trên xe: chiếu lịch, kiểm khóa, tính ba hiệu và kiểm luật đang dùng.
5. Nếu phương án giữ nguyên bị loại vì hạn chót hoặc trần và chế độ phục hồi được bật, đánh giá lại nó với các miễn trừ được phép.
6. Chỉ ở chế độ (b), xét giữ thêm phương án đổi kế hoạch không làm các vi phạm được miễn tệ hơn kế hoạch giữ; không miễn lỗi khóa hay lỗi vật lý.
7. Chọn theo thứ tự tiêu chí, với đúng một phương án mỗi xe và mỗi yêu cầu mới thuộc nhiều nhất một phương án được chọn.
8. Kiểm lại lựa chọn của cả đội xe; nếu không có lựa chọn hợp lệ thì báo lỗi hoặc dùng nhánh dự phòng đã được kiểm hợp lệ.
9. Hoàn tất quyết định được chọn, mở hoặc sửa lời hứa theo đúng thời điểm khởi tạo, cập nhật sổ và ghi vi phạm theo quy tắc ghi nhận.
10. Trả quyết định để bộ mô phỏng áp dụng và xác nhận.

The final fleet validation is visible at POL:370–400. Do not promise a successful decision on the error branch or invent an unvalidated fallback.

The draft also treats pickup windows as continuously guaranteed although NOTES:99 deliberately omits lateBoarding. This omission is material: WP4:8 sets record-v1, RunnerSession.cs:1088 passes it to the reducer, and SRC/RideBound.Application/State/EventReducer.cs:15–18, 262–274 accepts and records an observed late boarding without widening the original window. Add this fact to the register first, then add:

> Cửa sổ đón là điều kiện kiểm phương án, không phải bảo đảm rằng mọi lần đón thực tế đều đúng hạn. Cấu hình thực nghiệm ghi nhận sự kiện khách lên xe muộn hơn hạn đón thay vì dừng lần chạy; hạn đón ban đầu không được đổi.

### 2. Make the forecast formula and diagram reproduce the replay method

**DRAFT:69–77, 453–464, 488–497, 505–510.**

The current formula leaves m(b) undefined beyond the sampled profile or suggests that it keeps reading later historical bins. The implementation holds the profile at **bin 8**. It also uses time relative to the scenario window, not an unexplained wall-clock bin number.

Sources: S/optimize/display_layer.py:3–8, 55–64; S/optimize/promise_stretch.py:25–39, 49–52; S/tang3/world/preflight_world_v1_3.py:51, 54–82.

Define the quantities exactly:

> Các thời điểm \(t,p,\tau,S\) được đổi về giây tính từ đầu cửa sổ của kịch bản. Đặt \(b(\tau)=\lfloor\tau/900\rfloor\). Hồ sơ \(m_j\) là trung bình hệ số của các ngày nguồn ở các khung \(j=0,\ldots,8\); từ khung 8 trở đi giữ giá trị cuối. Viết \(\widetilde m(b)=m_{\min(b,8)}\). Khi đó \(g(\tau)=1\) trong khung chứa \(t\), còn ngoài khung đó \(g(\tau)=\widetilde m(b(\tau))/\widetilde m(b(t))\). Phép tính áp dụng riêng cho giờ đón và giờ trả.

Use \(\widetilde m\) in both the integral definition and pseudocode lines 4/7. State the positive-factor premise when presenting the integral as a general mathematical definition. The implementation receives milliseconds; converting **all** times and bin widths to seconds preserves the stated equation.

Replace “không bao giờ bị rút ngắn” and the return-line comment with:

> Phép lấy \(\max(p,S)\) bảo đảm \(D\ge p\) tại cùng lần công bố; nó không bảo đảm lời hứa hiển thị tăng đơn điệu qua các lần cập nhật.

The integral and segment arithmetic are otherwise correct: h/g is the remaining work covered in the current bin, and the final segment ends at tau+Wg.

The diagram currently places a “forecast layer” between selection and the actual ledger. A caption mentioning replay does not make that dataflow accurate. The archived core ledger contains naive p. The replay derives D afterward; it does not feed D back into the original ledger, the old v, or the C gate.

Replace the node “Công bố lời hứa (lớp dự báo)” with **“Công bố lời hứa p”**; show a separate branch from the saved record to **“Phát lại lớp dự báo: D=max(p,S)”**, outside the dispatch feedback loop. Suggested caption:

> Một lượt quyết định của bộ điều phối ghi lời hứa không dự báo \(p\) và sổ theo từng khách. Trong phép đánh giá bằng phát lại, lớp dự báo tính lời hứa hiển thị \(D\) từ các bản ghi đã lưu; \(D\) không quay lại làm đầu vào của những quyết định đã chạy.

At DRAFT:447–448, replace the categorical arrival claim with:

> Vì bộ điều phối dùng bảng giờ đi hiện tại cho phần đường còn lại, khi giờ đi tăng sau lúc công bố, lời hứa có thể sớm hơn giờ trả thực tế ngay cả khi xe giữ nguyên kế hoạch.

Keep the already correct source-day exclusions and inactive-weekend handling.

The mention of a separate dispatcher forecast experiment at line 510 is legitimate, but the reader needs to know it is a different intervention. After registering its code anchor, a compact bridge is:

> Phép thử đưa dự báo vào bộ điều phối thay đổi bản sao bảng giờ đi mà RideBound dùng để tính phương án, còn FleetPy vẫn di chuyển theo hệ số đo. Phép thử đó khác với phát lại lời hứa trên quyết định đã có và được trình bày riêng ở mục~\ref{muc:c4-dubao}.

For that experiment, the transformation also needs its own recipe:

> Với số khung dự báo \(K\), bản sao của bảng giờ đi gửi cho RideBound được nhân với \(r_b=\bigl(\sum_{j=0}^{K-1}\widetilde m(b+j)\bigr)/(K\,\widetilde m(b))\). Thiết lập thực nghiệm phải ghi giá trị \(K\) dùng ở từng cấu hình. Khi \(K=1\), hệ số này bằng 1.

Source: preflight_world_v1_3.py:15–24, 85–89, 113–133. Register this source fact before inserting it. Do not apply the integral recipe to that experiment as though it were its dispatcher transformation.

### 3. Correct the ten-dimensional ledger description and identify the late cohort

**DRAFT:517–532.**

v/e/p are projections containing several fields. The signed scalar x/c/z defined in §3.2 are ETA differences. The other dimensions include counts, relocations and order changes; they are not ten copies of these signed time differences and do not all satisfy z=x+c. DELTA:137–153 makes this explicit.

Replace lines 517–520 with:

> Sổ theo từng khách do RideBound ghi trong lúc chạy gồm bản ghi lời hứa ban đầu và các bản ghi sửa lời hứa. Mỗi lần sửa lưu lời hứa trước đó, phép chiếu khi giữ kế hoạch và lời hứa mới, cùng ba véc-tơ thay đổi và phần trần đã dùng. Các tọa độ giờ đón và giờ trả của các véc-tơ là độ lớn của hiệu giữa các mốc giờ tương ứng; các tọa độ còn lại đo những thay đổi như đổi xe, đổi điểm dừng hay thứ tự phục vụ. Các ký hiệu \(x,c,z\) ở đây chỉ các hiệu có dấu của giờ trả. Trạng thái cuối lưu sổ; phép tính sau khi chạy kết hợp sổ với giờ trả thực tế và lời hứa hiển thị có dự báo.

Sources: DELTA:64–97, 137–153; LEDGER:285–314; SPEC:35–63. “Mỗi lần cập nhật” should mean a **published revision**, not every epoch: VALID:562–597 does not append a revision when all three delta vectors are zero.

The ledger algebra is AGREE. Preserve q as signed, not a commitment-vector absolute total. Specify the cohort:

> Chương~\ref{chuong:thucnghiem} cộng ba phần trên các khách có \(a-p_0>60\) giây, trong đó \(p_0\) là lời hứa giờ trả ban đầu không dự báo. Điều kiện chọn khách này không dùng \(D_0\).

Source: S/optimize/forecast_family_a.py:134–138. This matters because a reader could otherwise select the ten late-with-forecast riders instead of the naive-late cohort.

### 4. Repair the rules table and forced/recovery terminology; retain the conditional proof

**DRAFT:323–338, 374–389, 395–398, 424–428, 436–440.**

The proof has the right hypotheses. The table removes those hypotheses when it says C “never” forces by construction, and U cannot force simply because locks compare against e. The code may fail for nonrecoverable reasons; the theorem proves only that the **C gate does not remove the keep-route option under (N) and L≤B**. It is not an unconditional total-feasibility theorem.

Replace the C forced-cell text with:

> Luật C không loại phương án giữ nguyên nếu (N) và \(0\le L_r\le B\); không bảo đảm có phương án hợp lệ khi điều kiện này không thỏa.

Replace the U forced-cell text with:

> Không có hạn chót hay trần giờ trả làm phương án giữ nguyên bị ép; lỗi kiểm tra khác vẫn có thể làm lượt quyết định thất bại.

Replace the introductory paragraph at lines 323–325 with:

> Phương án giữ nguyên có thể được đưa vào nhánh phục hồi khi bị loại bởi hạn chót hoặc trần, nếu mọi lỗi thuộc các loại được phép miễn. Một quyết định được ghi là bị ép khi phương án được chọn là phương án được giữ nhờ miễn trừ đó. Gọi (N) là giả thiết: phương án giữ nguyên được dựng thành công và qua mọi kiểm tra khác ngoài phép kiểm trần giờ trả của luật C.

Sources: HVA:247–318; POL:448–462; VALID:413–419. Recovery is triggered by rejection of the **reference**; it does not require all other candidates to have been rejected. A normal changed candidate can still win. Keep the distinction between a recoverable reference and a selected forced option.

Replace lines 436–440 with:

> Luật phục hồi (a) giữ phương án giữ nguyên khi các lỗi được miễn chỉ là lỗi hạn chót hoặc trần. Luật (b) còn xét phương án đổi kế hoạch, nhưng chỉ miễn những vi phạm trên cùng khách và cùng chiều mà phương án giữ nguyên cũng có, và không cho mức vi phạm tệ hơn. Lỗi khóa theo giai đoạn và lỗi vật lý không được miễn. Vi phạm được ghi khi hoàn tất quyết định được chọn; nếu lời hứa, giai đoạn và mã lỗi không đổi so với vi phạm bị ép gần nhất, cài đặt không ghi thêm một bản ghi trùng.

Sources: VALID:791–811 (deadline side), 537–539 (budget witnesses), 618–637 (deduplication). “Mỗi lần miễn được ghi thành vi phạm” is literally wrong without that last qualification. It would incorrectly predict the breach count.

The V row omits five morning-extension caps: w07x runs **90, 120, 150, 180, 240 seconds** in addition to w07's 30. Correct its last cell to:

> Tập chính (30); buổi sáng (30, 90, 120, 150, 180, 240).

Sources: S/tang3/w07/run_w07.py:5; w07x/run_w07x.py:3–5, 35–36. Register B16 must be extended to cover that V portion before the corrected body uses it.

Likewise, distinguish the deadline levels by set:

> Luật hạn chót chỉ mượn thành phần hạn chót của Schulz và Pfeiffer, không tái lập toàn bộ thuật toán của họ. Tập chính dùng độ chùng 30 và 60 giây; tập chỉnh trần buổi sáng dùng các mức từ 30 đến 300 giây đã liệt kê trong thiết lập thực nghiệm. Bài của họ dùng mặc định 900 giây.

If listing the C/M+ morning levels explicitly, they are 30, 60, 90, 120, 150, 180, 240, 300, rather than every value in a continuous interval. M-30 also exists in the morning driver: if Chapter 4 reports it, define \(|p-p_0|\le B\) as a separate two-sided deadline row. It is not the C rule or V rule. LOCK:186–197 verifies the two sides.

State selector activation precisely:

> Mức giảm số phương án bị ép chỉ có trong hồ sơ véc-tơ cứng hoặc hồ sơ kết hợp khi tập phương án chứa phương án được giữ nhờ miễn trừ. Hai mức ưu tiên mức dùng trần và sửa lời hứa được bật khi có chiều trần cứng áp dụng. Với chiều trần 0 được đưa vào xếp hạng, mức dùng 0 được biểu diễn bằng 1.000.000 phần triệu.

Sources: SEL:271–280, 319–330; HVA:554–558, 596–626. Do not generalize the zero-limit convention to riders awaiting an initial promise or exempted dimensions excluded from ranking. The observed saturation counts can stay.

### 5. Remove the unsupported linear route-length complexity claim

**DRAFT:627–628.**

WRONG as a description of the full validator. The budget comparison itself visits ten coordinates, but DELTA:190–215 counts incumbent inversions with nested loops over pairs of common stops. The sentence \(P\times R\times L\) omits that work.

Replace it with:

> Riêng phép so trần duyệt 10 chiều cho mỗi khách cần kiểm trong mỗi phương án, nên số phép so ở một xe là \(O(P\,R)\), với \(P\) là số phương án và \(R\) là số khách đã có lời hứa cần kiểm trên xe. Đây chưa phải độ phức tạp của toàn bộ bước kiểm: bước tính véc-tơ còn có phép đếm đảo thứ tự xét các cặp điểm dừng, nên không thể coi toàn bộ khối lượng kiểm là tuyến tính theo độ dài kế hoạch.

Sources: BE:72–104; VALID:233–239; DELTA:190–215. This avoids claiming an unproved tight bound for the whole pipeline or CP-SAT runtime. Also do not describe the scalar pseudocode table itself as if it were the ten-coordinate loop.

### 6. Close the register compliance gap before integration

NOTES:50 explicitly says X3-01…19 are facts not in the register, yet DRAFT uses them. That conflicts with WRITING-BRIEF:20–21:

> Every factual sentence must be backed by a register row … If a fact you need is not in the register, do not write it.

A source verified in NOTES is useful evidence, but it is not an exception to this rule. Register the checked X3 entries, the physical/late-boarding distinctions, V extension levels, and new bibliography metadata; then retarget EV comments. Alternatively remove the corresponding assertions until registered. This review does not edit or extend the register.

Correct two anchor details during registration: net10.0 occurs in the project files, **not** Directory.Build.props; FFA's calculation lines are 134–138, already correctly corrected in NOTES. X3-18's C1 description needs TEX/08-chuong4.tex:136–138, not an anchor ending at 136 alone.

### 7. Narrow the −1 ms and dwell assertions; describe independent checks accurately

**DRAFT:159–160, 219–220, 647–650.**

The −1 ms correction is applied correctly in spirit. But “không có tác dụng đo được” is too absolute: the saved audit measures exactly 4 ms of earlier changes for C-30. What is unshown is a practically meaningful benefit of the two-sided gate. Also, the correction covers U, C-30, C-120 and M+-30, not all possible arms or all runs ever conducted.

Replace lines 217–220 with:

> Phần dời do điều phối được tính theo độ lớn: sớm hơn hay muộn hơn \(e\) 20 giây đều tính 20 giây. Bộ sinh chỉ chèn thêm không bảo đảm \(c\ge0\) theo cấu tạo. Trên 34 kịch bản chính của bốn cấu hình đã kiểm về phần dời sớm — điều phối không trần, trần 30 giây, trần 120 giây và hạn chót 30 giây — mỗi lần dời sớm đều chỉ là 1 mili giây. Các số liệu này không chứng minh lợi ích thực nghiệm đáng kể của vế hai chiều; trị tuyệt đối vẫn thuộc định nghĩa.

ADD1:104–112: earlier changes are 3/4/3/4 respectively; C-30 earlier total = 4 ms = 0,004 s. Neither this draft nor the corrected passage should attribute the cause to rounding without checking it.

REG B05's saved check inspects **three sample runs**, S/optimize/codex-debate/service-duration-check-2026-10-06.txt:2–4. It does not establish the universal statement at DRAFT:159. Either add whole-set/configuration evidence or use the narrower text:

> Trong ba lần chạy mẫu đã kiểm, thời gian dừng ghi trong kế hoạch bằng 0 giây. Hệ số giờ đi dùng cho thành phố được cập nhật theo khung 15 phút.

Do not equate this sampled field check with a fresh audit of every FleetPy boarding duration.

T38I:82–94 has 13 numerical comparison rows; line 95 is a separate invariant check. Thus 13 numerical items agree, while “all checks = 13” would obscure a fourteenth row. Clarify:

> Một chương trình viết riêng từ đặc tả chỉ số tính lại 13 hạng mục số liệu và kiểm thêm một bất biến; các đối chiếu số liệu không có sai lệch. Những kiểm tra này xác nhận sự khớp với bản ghi trong phạm vi đã kiểm, không xác nhận mô phỏng giống thực tế.

Keep the honest statement that Claude/Codex wrote the verification programs. Do not present the three agreeing readers as three independent implementations: ADD:15–19 explicitly distinguishes independent Codex readers from Claude's reuse of an existing reader.

### 8. Complete citations without conflating the 2022 and 2026 FleetPy papers

Both proposed reference metadata records are substantively correct; see §6 below. Add the new keys before integration. Prefer engelhardt2026 for the framework description at line 582 and the documented use of FleetPy 1.0.2. The existing fleetpy2022 is a real, different seven-author paper, not merely the same ten-author article with an old year. Replace citations where the claim is the current framework description; retain the 2022 entry if discussing that publication/history. Do not silently overwrite its title and author list while leaving its year/key unchanged.

### 9. Reconcile cross-references, algorithm numbering and page budget

All 31 labels within this draft are unique. The **nine external labels listed in NOTES** are absent from the existing thesis label inventory, and there are no other rewritten chapter drafts in drafts/ yet. This is a pending integration issue, not proof of bad intended names.

OUTLINE-V2 uses “Giải thuật 3.x” and table numbers that differ from NOTES:134–136. The pseudocode-as-table choice is acceptable within the stated DACN-style permission, but Chapter 4 and appendices must reference labels rather than the outline's stale numbers.

The 13-page target is not verified. NOTES reports incompatible estimates of approximately 12 and 15,8 pages; neither is a rendered result. Do not declare the chapter within budget before the permitted integration build. Cut duplication first: the example is explained in prose, table and figure; the selector order appears in both table and prose; the forecast/recovery explanations can be shortened after corrections.

## 3. Definition, formula, claim and number verification table

This table covers the substantive prose and numerical/formal content; the three pseudocode tables are checked line by line in §4. Formatting commands are not technical claims.

| Draft lines / item | Verdict | Checked value or qualification; evidence |
|---|---|---|
| 30–39: state, current snapshot, new requests, initial publication at confirmation | AGREE | Contracts EventBatchMessages.cs:42–61, OnlineEventModels.cs:144–153,172–183; WP4:5; VALID:272–301. “Nhận hay chưa nhận” is an abstraction; the selected request must be unique fleet-wide. |
| 40–41: all service constraints described as always hard | WRONG | Distinguish changed-plan feasibility, relief on the keep-route candidate, and recorded observed late boarding. See required edit 1. |
| 42–43: evaluation quantities | AGREE | REG/OUTLINE define service, lateness, early arrival, extension and revised-rider counts. Actual rates/denominators belong in Chapter 4. |
| 50–54,75–77: core computes projections, filters, records | AGREE with scope | Describes the implemented components. It is not a claim that all ordinary pooling systems lack ledgers; do not use the caption as novelty evidence. VALID/HVA/LEDGER. |
| 69–73: forecast publication feeds the core ledger | WRONG | In the replay method D is derived after the run; original ledger and dispatch use p. DISP:60–64; FFA:84–93; FR:11. |
| 126: hard rejection rather than objective penalty | WRONG as unconditional wording | Ordinary gate failures reject candidates, but configured recovery retains qualified exceptions. HVA:257–318; VALID:413–419,522–552. |
| 127–129: bounded insertion preserves incumbent stop order and assignments | AGREE | GEN:548–575; maximums in WP4:10–15. The generator's bounded search is not a guarantee of exhaustive exploration. |
| 129–131,323–324: rejected reference equals forced final decision; all options must disappear | WRONG | Recovery examines reference rejection; forced final status depends on the selected assessment. HVA:247–318; POL:448–462. |
| 142–153: v/e/p; x=e−v, c=p−e, z=p−v=x+c; initial v=e=p | AGREE | VALID:355–379; DELTA:64–97; SPEC:41–50. Signed scalar formulas are for ETA fields, in seconds after conversion. |
| 157–161: e is a model projection incorporating progress/events, not a causal attribution | AGREE | VALID:355–361 uses the reduced state; PROJ:62–140 uses current position/progress. This does not establish each event's physical causal effect. |
| 159: dwell=0 in every experiment | CANNOT CHECK | B05/SERV:2–4 establish only three inspected sample runs. Supply wider evidence or narrow the sentence. |
| 160: common city factor, 15-minute bins | AGREE | REG B06; world v1.3:19–24,51–77; no claim that this represents all spatial congestion. |
| 164–213: hand-made 9:10:00/9:10:40/9:11:10 example | AGREE | Differences are 40/30/70 seconds; diagram/table values match. Illustrative, not measured. |
| 217–218: both ±20 seconds charged as 20; insertion does not prove c≥0 | AGREE | DELTA:139,259–262; this does not establish substantial earlier revisions in the data. |
| 219–220: all measured earlier moves are −1 ms; no measurable effect | WRONG in scope/interpretation | ADD §0.1–0.2, ADD1:104–112 cover four named arms; C-30's earlier total is measured at 0,004 s. Cause and outcome benefit are unverified. |
| 229–237: C gate L+abs(p−e)≤B; L initially zero; update only for actual publication | AGREE after lifecycle correction | BE:51–104; LEDGER:285–314; VALID:272–301,562–597. Equality passes; hypothetical candidate evaluation does not consume the actual allowance. |
| 231–232,269,294,298: every Accepted rider has L and is checked | WRONG | Provisional Accepted bookings awaiting confirmation without history are skipped. VALID:272–280; HVA:554–558. |
| 240–243: full-trip sum bounded; remainder B−L; no reset; same cap | AGREE under normal C enforcement | Induction from zero with accepted updates satisfying the gate. Generic recovery can exempt budget failures; do not infer a universal guarantee for every possible configuration/error state. LEDGER:285–288; VALID:537–543. |
| 243–245: three 30-second per-step allowances allow 90; C-30 equality leaves 0 | AGREE | Arithmetic from the definitions; other feasibility checks still apply. |
| 261–263: pickup window 10 minutes, max ride 1,5× direct, capacity 4 | AGREE for configured values; WRONG if universal realized service guarantee | Fixture normalizer-configuration.json:1 gives 600000 ms/1500 permille/4; NORM:429–445 fixes request bounds. GEN/service-quality relief and record-v1 qualify their enforcement. |
| 265–267: assignment/stops preserved, pickup ETA lock compares with e | AGREE with phase scope | LOCK:42–84,156–161,204–207; C-30 config:34–72,94–98. Drop-stop preservation also follows the zero switch budget; it is not a new DropStop bit in the listed final-confirmation locks. |
| 273–280: forced min; acceptance max; worst usage then revision; cost; IDs | AGREE after activation clarification | SEL:271–330,365–385. Global objectives operate over selected fleet options, not independently greedy per vehicle. |
| 278–279: plan cost is remaining route duration, not real operating cost | AGREE | PROJ:143; SEL:365–368; REG A16/I09. Fleet objective sums selected option costs. |
| 280: ID rank makes outcomes repeatable | AGREE in deterministic execution context | SEL:370–385; seed/budgets/configuration also matter. ID tie-breaking alone is not a reproducibility guarantee across binaries. |
| 315–317: fail-fast, ten dimensions, positive drop cap and three zero switch caps | AGREE with qualification | VALID:222–239; BE:72–104; C-30 config. The first failing rider may have multiple dimension witnesses; retained evidence is not an exhaustive enumeration of all possible reasons. |
| 324–338: N, keep-route proposition, p=e proof, invariant L≤B | AGREE conditionally | Same route/state/snapshot and projection rule give c=0, so gate passes. Retain N, initialized promises, and normal C updates; see GEN:196–229, VALID:355–379, LEDGER:285–288. |
| 341–343: empirical zero forced C decisions, 0/20.101 and 0/20.435 | AGREE | STG:43–44; ADD1:120–121. Counts are acknowledged decisions, not a proof that N is universally true. |
| 346–347: non-C physical failures can defeat feasibility | AGREE with corrected example scope | Structural active-route failure is fatal, GEN:171–182. A pickup-window overrun alone does not necessarily eliminate the no-op because of the allowance. |
| 348–350: v=600,e=p=660 yields c=0,z=60 | AGREE | Arithmetic; projected visible drift, not a claimed guarantee of actual a. |
| 350–351: v=p=600,e=720 yields z=0,abs(c)=120 | AGREE | Arithmetic; restorative action is still charged. |
| 374–376: U removes drop-hour gate, retains locks; LOCKS alias | AGREE for configuration; WRONG for unconditional cannot-force claim | REG A08/K50/B17; LOCK. FREE is the distinct cost-oriented no-commitment arm. |
| 378–379: FREE, RollingCost, no commitment locks, fixed-traffic set | AGREE within stated scope | REG A17/B17/K50. No explicit commitment locks does not establish permission to reassign accepted riders. |
| 381–383: C law, cap sets, never forced by construction | AGREE for law/cap sets; WRONG for unconditional guarantee | Keep N and L≤B. Tested morning C/M+ caps are discrete. |
| 385–386: M+ p−p0≤B, one-sided; 30/60 main, morning range | AGREE | LOCK:186–197; configuration and w07/w07x arm lists. Only borrows the deadline component, not the original S&P algorithm. |
| 388–389: V sum abs(z), recovery (b), main 30/morning only30 | WRONG for morning set | V-90/120/150/180/240 also run in w07x:3–5,35–36. Definition itself agrees with visible budget basis. |
| 395–396: S&P default 900 seconds; this study uses only30–60 | AGREE for main; WRONG as whole-study scope | Morning extends M+ to300. REG J10/J11; w07/w07x driver lists. |
| 396–398: old fixed-traffic runner lacks commitment recovery; static B1/C1 mapping | AGREE | REG B17; TEX/08-chuong4.tex:128–138; separate test sets must remain distinct. |
| 401–410: telescoping identity and M+/V example 40>30 | AGREE | Requires continuous v_t=p_(t−1); SPEC:62–63. Bounded signed total, total variation, and sum abs(c) are different. |
| 413–419: HZ updated-route reference and eq7 max; p0+B substitution is author's inference | AGREE with explicit scope | HZ:529–543,567–606. Their hard updated bound and original-bound penalties coexist. Relaxed deadline shares the conditional keep-route gate property; no run of this variant is claimed. |
| 419: C differs by common fixed cap/all promised accepted riders/whole-trip accumulation | AGREE as narrow definition comparison | REG J05/K02. These are differences in obligation, not a claim of unique feasibility or superior real service. |
| 422–428: lexicographic selection; forced activation; zero usage at zero cap | AGREE for mechanism, WRONG if read universally | Conditions and ranking exclusions in SEL:271–280/319–330, HVA:554–626. See edit4. |
| 426–428: saturation 3.503/3.503;3.506/3.506;3.504/3.504 | AGREE | ADD1:119–121. Denominator is decisions with the utilization level, not all20.760/20.101/20.435 decisions. |
| 431–433: U/C share selector/config except drop cap; cost-first result not yet measured | AGREE for the stated experiment | REG H01/H02/A08/K18; the draft does not claim a cost-first result. This comparison holds the selector fixed but does not isolate outcomes on identical served cohorts. |
| 436–440: recovery a/b, locks never exempt, every exemption writes breach | AGREE for eligibility; WRONG for record frequency/selection timing | VALID:537–539,618–637,791–811; POL:448–462. Preserve per-rider/per-dimension and side-of-deadline conditions. |
| 447–464: forecast integral, max, meaning of m/b | WRONG as complete implemented recipe | Correct segment arithmetic but missing hold-bin8/relative clock; D≥p at one publication is not temporal monotonicity. STRETCH:25–52; world v1.3:51–82. |
| 467–470: causal same-kind sources; exclude15/11;≥2; active14/15/16;21/34 active,13inactive | AGREE | DISP:27–57; FA:1; ADD1/ADD N-16/N-28. Weekend source count is insufficient. |
| 505–507: replay changes displayed quotes only; D0−p0 is extension | AGREE | FR:11; FFA:84–93. It does not change C's original ledger or served cohort. |
| 508–509:34/1.471 displayed pickups after latest pickup | AGREE | FR:69–70; REG F07; FA:29. Scope is C-30,21 active cells, served riders; not observed late boardings or a new rider-loss estimate. |
| 510: a separate in-dispatcher forecast test exists | AGREE, method bridge missing | REG F12; world v1.3:15–24,113–133. Not the same transformation as replay. |
| 517–519: signed ETA differences on all ten commitment dimensions; row every update | WRONG | DELTA:137–153; VALID:562–597. Non-time coordinates have other meanings; zero-delta epochs need not publish revisions. |
| 522: a−p0=q+f+(a−D0−q),q=sum signed c,f=D0−p0 | AGREE | Exact algebra; FFA:91,93,134–138. It is a post-run computation combining ledger, alighting and replayed quote. |
| 528: abs(q)≤sum abs(c)≤B | AGREE under enforced C bound | Triangle inequality and normal C gate. Does not hold automatically after generic exempted budget failures. |
| 529–532: no forecast f=0; residual=sumx+rho−f | AGREE | Continuous publication chain and rho=a−pk; group late riders using naive p0, FFA:134. |
| 535–538: model accounting, no blame, residual not “unforeseeable” | AGREE | REG K04/K19; no real-world causal claim. |
| 548–552,564–575: architecture, C#/.NET10, ORTools bridge, normalizer, adapter | AGREE with dependency wording | Project files give net10.0; no external PackageReference/ProjectReference in Domain. .NET standard library is implicit, so prefer “không tham chiếu dự án khác hay gói thư viện ngoài” over literally no libraries. Architecture tests inspect rules, not proof that they were freshly run. |
| 570,625: ORTools9.15; exact package9.15.6755 | AGREE | Solvers.OrTools.csproj and WP4:18. Version is proved by local configuration, not by the generic2024 bibliography entry. |
| 582–587: FleetPy1.0.2, Python subprocess, NDJSON, ACK serialization, saved messages | AGREE | README:1–12; runner_client.py:133–138; Program.cs:103–106; NdjsonReader/Writer; RunnerSession:448–455; T38I:9–15. Pin/tag and adapter evidence are more direct than a general framework citation. |
| 600–613: abstract message flow | AGREE as simplified flow | ProtocolPrimitives:108–120; eventBatch→decision→decisionApplied. Handshake hides helloAck; ending exchange refers to finalizeRun→runSummary, not shutdown. Label this as simplified; a checkpoint is outside the repeated decision frame. |
| 624–626: max100,2; budgeted search, seed7, no exhaustive guarantee | AGREE | WP4:9–23. Exploration/generation/validation budgets10000 each, solver work100000, deterministic time1000000µs. Budget units are not measured per-decision wall seconds. |
| 627–628: complete checking work proportional P×R×route length | WRONG | Pair loop in DELTA:190–215; isolate ten-dimensional budget comparison instead. |
| 631–633: median total runtime730/667/641s,16 runs each, no isolated overhead | AGREE | S/optimize/codex-debate/claude-work/r17-rebuttal/r17-wp14r-elapsed-2026-10-10.txt:2–6. Rounded saved medians for old fixed-traffic jobs. Cannot infer that adding C makes each decision faster. |
| 641–643: historic1025/1025 tests at recovery addition | AGREE as historical report | R/docs/18-status-and-decision-log.md:5100–5107. No current test run performed here. |
| 644–646:382.006 revisions,185=170+15 runs,0 field mismatches | AGREE | T38I:15,68; acknowledged revision field comparisons, not validation of all physical events/real-world fidelity. Does not include the later34 C-120 runs. |
| 647–650:13 items and independent readers, software-agent disclosure | AGREE with scope clarification | T38I:82–94 gives13 numeric rows,95 another invariant. ADD:15–19 gives independent-reader/reused-reader distinction. Keep agent provenance and limits. |
| 652–654: same archived recovery runner main/morning; older fixed runner | AGREE for specified sets | run_w07.py:8; run_w07x.py:7–10; run_t38.py:9,90–93; run_t38c120.py:3–8; REG B17. Snow runner identity remains unverified in NOTES and is not asserted here. |
| 654: rebuilt runner must reproduce old behavior before use | AGREE as process requirement | REG I13. Specify behavior on tested scenarios, not equality of rebuilt binary hashes or uncontrolled transport salt. It is not a claimed successful rebuild. |
| 661–662: Chapter4 comparison roadmap | AGREE | Matches intended outline; external chapter/section labels still require integration. |

## 4. Every pseudocode line

### Decision cycle, DRAFT:93–117

| Algorithm line | Verdict | Required interpretation/change |
|---|---|---|
| 1 | AGREE | Abstract function entry. |
| 2 | AGREE | Apply batch before projecting schedules. Record-late-boarding mode should be explained; edit1. |
| 3 | AGREE | Candidate sets are per vehicle. |
| 4 | AGREE conditionally | Keep-route is attempted first; structural failure can return an error. “Always generated successfully” would be false, GEN:171–229. |
| 5 | AGREE | ≤2 new requests and≤100 retained candidates; ordered incumbent stops preserved, bounded exploration. |
| 6 | AGREE | Per-candidate evaluation before solver. |
| 7 | WRONG | Blanket rejection loses the keep-route service-quality allowance; do not relax changed candidates or capacity. |
| 8 | WRONG in lifecycle scope | Check active riders with initialized promises; provisional accepted bookings have no history. Check physical projection/locks before gate. |
| 9 | WRONG in forced label/activation detail | Check reference rejection with recovery enabled and only eligible failures; not all options empty; selected forced status comes later. |
| 10 | WRONG | Keep eligible recovery candidate; do not persist a real breach just for evaluating it. |
| 11 | WRONG if unconditional | Only when recovery(b) enabled; same rider/dimension/side no-worse conditions. Physical/lock failures remain excluded. |
| 12 | WRONG as complete selection constraints | Add each new request at most once across vehicles, final fleet validation, and failure behavior. |
| 13 | AGREE | Selected new requests are accepted/offered according to lifecycle; this is not automatic initial promise publication before confirmation. |
| 14 | AGREE after corrections | Final selected publications update actual ledger; no update for hypothetical rejected candidates or zero-delta no-publication epochs. Distinct breach recording is conditional/deduplicated. |
| 15 | AGREE | Success output; explicitly handle failed selection/validation earlier. |
| 16 | AGREE | End. |

Sources are GEN:161–244, VALID:201–239/272–301/562–637, HVA:247–318, POL:370–400/448–462 and OrToolsCandidateSelectionSolver.cs:348–364.

### Scalar C check, DRAFT:297–308

| Algorithm line | Verdict | Required interpretation/change |
|---|---|---|
| 1 | AGREE | L/state/snapshot are implicit inputs in the header; make initialized ledger explicit. |
| 2 | WRONG in scope | “Accepted” alone includes provisional bookings; iterate active customers with initial history. Stable request-ID order agrees with VALID:233–239. |
| 3 | AGREE | Old remaining route, current reduced state and snapshot, VALID:355–361. |
| 4 | AGREE | Candidate schedule with same snapshot; non-ETA validation belongs outside this scalar helper. |
| 5 | AGREE | Signed c=p−e. |
| 6 | AGREE after scope correction | Applicable phase and L+abs(c)>B; equalB passes. BE:72–114. |
| 7 | AGREE as scalar witness | First failing rider and one drop-cap reason. Full vector witness also names dimension; this table is not the complete ten-dimensional validation. |
| 8 | AGREE with publication condition | Return allowed; commit the increment only when selected, validated and published. If no revision is published, no new ledger increment is needed. |
| 9 | AGREE | End. |

### Forecast display, DRAFT:484–498

| Algorithm line | Verdict | Required interpretation/change |
|---|---|---|
| 1 | AGREE | t,p refer to one published pickup or drop ETA, converted consistently. |
| 2 | AGREE | Earlier same-kind days, exclude15/11; source universe12–18/11 is explicit in DISP. |
| 3 | AGREE | Fewer than2 sources or p≤t returns p, DISP:60–64. |
| 4 | WRONG as full recipe | Construct profile bins0…8 relative to window start and hold final value thereafter. |
| 5 | AGREE | W=p−t, tau=t, b0=floor(t/900) in relative seconds. |
| 6 | AGREE as abstract loop | Concrete implementation limits to10000 iterations and errors if it cannot finish; not a measured simulation-time limit. |
| 7 | WRONG as written unless m has held-tail definition | g=1 in current raw bin, held-profile ratio otherwise; clamp **both** profile indices to8. |
| 8 | AGREE | h to next raw15-minute bin boundary; do not clamp the clock/boundary counter to8. |
| 9 | AGREE | h/g≥W ends at tau+Wg. |
| 10 | AGREE | Subtract covered work then advance tau. |
| 11 | AGREE for max; WRONG if comment means temporal monotonicity | D≥p at this publication only. |
| 12 | AGREE | End. |

## 5. Verification of all X3 entries

| ID | Verdict | Primary check / correction |
|---|---|---|
| X3-01 | AGREE | EventBatchMessages.cs:42–61 contains the listed event collections. This lists supported events, not proof each occurred in each experiment. |
| X3-02 | AGREE | OnlineEventModels.cs:144–153,172–183 contains request, vehicle and travel-snapshot fields; travel snapshot is183 as well as arc data181. |
| X3-03 | AGREE with omitted qualifier | GEN:161–244,548–575,691–693 verifies keep-first, structural failure and insertion order. NOTES/body must also preserve no-op service-quality relief versus changed-plan strictness. |
| X3-04 | AGREE after lifecycle scope correction | VALID:201–239,272–301,355–379,404–411,494–520; HVA:171 scopes vehicle. |
| X3-05 | AGREE | BE:6–12,51–114; DELTA:139,259–262. Actual witness contains dimension; the scalar pseudocode can be explicitly reduced. |
| X3-06 | AGREE | LOCK:42–84,156–161,186–207; C-30.json:94–98. Final confirmation names Vehicle/PickupStop/PickupEta; drop-stop zero switch cap is a separate mechanism. |
| X3-07 | AGREE with activation/ranking qualifications | SEL:271–330,365–385,510–522; HVA:554–626,638–659. Zero limit maps to1000000ppm for eligible ranked dimensions; exclude skipped provisional/exempt cases. |
| X3-08 | AGREE as merged identifier | NOTES:75 says merged into07; no separate fact to invent. |
| X3-09 | AGREE for eligibility; WRONG if interpreted as immediate/unconditional breach logging | HVA:79–99,247–318; POL:322–334/448–462; VALID:618–637 deduplicates repeated identical breaches. |
| X3-10 | AGREE | w07:8, w07x:7–10, t38c120:3–8 reuse the main runner/WP4/recovery settings; run_t38:9,90–93 links to run_w07's runner/WP4. Does not establish snow identity. |
| X3-11 | AGREE for inspected code, draft incomplete | DISP:3–8,34–64; STRETCH:25–52; world v1.3:51–82 confirms bin8 hold. Need include tail and relative clock in method. |
| X3-12 | AGREE | FFA:86,91,93,134–138: D0, signed q, naive-late cohort and residual. NOTES' corrected134–138 lines are right. |
| X3-13 | AGREE | SPEC:35–63: final checkpoint, initial/revision records, initial equality, continuity. VALID:562–597 qualifies when revisions are actually appended. |
| X3-14 | AGREE; one anchor WRONG | All project files target net10.0 and show stated ProjectReferences; solver PackageReference=9.15.6755. Architecture DependencyRuleTests.cs:11–29,95–166 checks dependencies. Directory.Build.props itself has LangVersion14.0 and no target-framework declaration. |
| X3-15 | AGREE | ProtocolPrimitives:108–120; RunnerSession:448–455/543; Program:103–106; NdjsonReader/Writer; adapter README:1–12; runner_client:133–138. End summary follows finalizeRun, not shutdown. |
| X3-16 | AGREE against saved counts | STG:42–43: U0/20760 and C-30 0/20101 acknowledged decisions; independent ADD1:119–120 agrees. |
| X3-17 | AGREE | WP4:9–23:100/2 candidates/requests; exploration10000, generation10000, validation10000, solver100000, deterministic1000000µs, seed7. |
| X3-18 | AGREE; extend anchor | Existing TEX/08-chuong4.tex:128–138 distinguishes static B1/C1; C1's pickup lock finishes at138. Does not automatically identify every later FREE/B1 treatment. |
| X3-19 | AGREE | EL17:2–6 lists b1-ref730, c1-nobudget667, c1-h6ref641, n16 each; REG H13 maps these to the fixed-traffic treatments. |

## 6. Citation and DOI audit

| Citation | Verdict | Primary evidence / limit |
|---|---|---|
| horl2022 title, two authors,2022, DOI10.3929/ethz-b-000561639, Conference Paper | AGREE | [DataCite DOI metadata](https://api.datacite.org/dois/10.3929/ethz-b-000561639) gives these fields and publisher ETH Zurich; local HZ:1–15 agrees. |
| HZ submission27/10/2021 | AGREE from PDF, not the DOI publication-year field | HZ:15. Optional bibliography detail; it does not change the2022 citation year. |
| HZ specific conference name, conference pages | CANNOT CHECK | No event/page metadata in the inspected DOI record. Do not write “TRB2022” on the tentative note alone. |
| HZ eq7/penalties and author's relaxed-deadline variant | AGREE | HZ:567–606: max(updated,latest), constraints9–10, penalties11. On-board/assigned-vehicle positioning must remain explicit. The p0+B substitution and no-op observation are this thesis's inference, not their stated C law or a reproduced experiment. |
| engelhardt2026 metadata | AGREE | [Publisher article](https://link.springer.com/article/10.1186/s12544-026-00823-3) and [Crossref DOI record](https://api.crossref.org/works/10.1186/s12544-026-00823-3): ten authors as NOTES:108 lists, European Transport Research Review18, issue1, **article52**, published15/07/2026.52 is not a page number. |
| FleetPy1.0.2 citation | AGREE | Publisher's study section and local FLEET:474 document1.0.2; adapter pin is separately proved by R/simulators/fleetpy-ridebound/README.md:9–10. Cite the article for framework; cite configuration evidence for this study's actual installation. |
| existing fleetpy2022 | AGREE as a genuine separate publication | [arXiv2207.14246](https://arxiv.org/abs/2207.14246) matches existing TEX/10-tai-lieu.tex:57–61, with different title and seven authors. Replace framework-description citations intentionally; do not claim bibliographic identity with2026. |
| schulz2026 | AGREE | Existing bibliography:116–121 gives OR Spectrum48:541–586 and DOI10.1007/s00291-026-00847-0. Local primary SP:466–490 establishes first-offer deadline; REG J10 anchors default900s and fixed-time method. Cited as a borrowed component, not reproduced algorithm. |
| ortools | AGREE as existing generic software citation; CANNOT CHECK its2024 as a release date | TEX/10-tai-lieu.tex:93–97 names Google software/docs. Exact used package9.15.6755 comes from csproj/WP4. Do not infer its release year from that entry. |

Minimal proposed entries for the coordinator, **not written to the thesis**:

~~~tex
\bibitem{horl2022}
S.~Hörl and F.~Zwick.
\newblock Traffic uncertainty in on-demand high-capacity ride-pooling.
\newblock Conference paper, ETH Zurich Research Collection, 2022.
\newblock \url{https://doi.org/10.3929/ethz-b-000561639}

\bibitem{engelhardt2026}
R.~Engelhardt, F.~Dandl, A.~A.~Syed, C.~Ding,
S.~Alvarez-Ossorio Martinez, Y.~Zhang, H.~Hamdy,
J.~Brodersen, Z.~Chen, and K.~Bogenberger.
\newblock FleetPy: an open source simulator for reproducible research on mobility-on-demand services.
\newblock \emph{European Transport Research Review}, 18, article 52, 2026.
\newblock \url{https://doi.org/10.1186/s12544-026-00823-3}
~~~

The HZ metadata leaves the event unspecified rather than inventing one. Publication metadata does not establish the experimental runner binary.

## 7. Strict examiner assessment and integration limits

The chapter now has the required seven-section structure, an explicit problem, three-time example, C definition, short conditional proof, law comparison, forecast recipe, ledger accounting and implementation/verification section. I would keep that structure and the short proof. I would not replace it with a stronger theorem or remove the two counterexamples.

The questions the present wording cannot yet answer cleanly are:

1. **Why does the run continue when old service deadlines are already violated?** The draft rejects all such candidates, whereas the actual safety option receives specific relief and observed late boarding is recorded.
2. **Can the solver assign one new request to two vehicles?** The code prevents it; the pseudocode omits the constraint.
3. **What exactly is called a forced decision?** Recoverable reference, retained recovery option, selected forced option and a new breach record are different objects. The current text merges them.
4. **Where does D enter the actual run?** For quote replay it enters only postprocessing; the overview diagram suggests a different feedback mechanism.
5. **What is m(b) after two hours, and what clock starts bin0?** The implementation answers both; the method currently does not.
6. **Are ten commitment dimensions all time shifts?** No; only ETA coordinates use those scalar formulas. Without this distinction, the reader cannot reconstruct the ledger.
7. **Which first promise defines “late” in the ledger sum?** Naive p0, not displayed D0. The draft needs that explicit condition.
8. **Why claim total validation is linear in route length?** The inspected inversion calculation examines pairs; the sentence has no support.
9. **Which V values and deadline variants were actually tested?** Morning V extensions are missing. Define M-30 if its results remain in Chapter4, or omit those results consistently.
10. **What does independent agreement validate?** Saved counts and fields within their audited scope; neither a fresh current test run nor real-world validity.

Cross-chapter checks:

| Item | Status / action |
|---|---|
| Ch3 seven sections and subject order | AGREE with OUTLINE-V2:161–178. |
| Scalar proof under N in body; HZ comparison in§3.4 | AGREE; moving HZ paragraph after comparator definitions is readable and does not change the argument. |
| Chapter4 selector question§4.6 | Correct external label intention; retain “not yet measured” unless that experiment is actually completed. |
| Chapter4 forecast§4.7 | Needs the two interventions distinguished and a shared p0/D0 convention. |
| Chapter4 validity§4.10 | Needs diagnostic denominators: utilization-present decisions versus all acknowledged decisions; bounded search versus actual cap hits. |
| Appendix law/runner maps | Needs distinction among static B1/C1, fixed-traffic FREE/LOCKS, and dynamic U/C; no inferred snow runner identity. |
| External labels | All9 absent from existing thesis: chuong:thucnghiem, muc:c2-dubao, muc:c4-thietlap, muc:c4-vaitro, muc:c4-dubao, muc:c4-hople, phuluc:A/B/C. Define them in rewritten chapters/appendices or retarget during integration. |
| Internal labels |31 unique; no duplicate within the draft in this read-only check. |
| Citation keys | horl2022 and engelhardt2026 need entries; ortools/schulz2026 already exist. |
| Algorithm/table numbering | NOTES documents a consistent local scheme, but outline prose/table numbering must be reconciled. Use labels in later chapters. |
| LaTeX dependencies | Existing main.tex has amsthm, TikZ positioning/arrows.meta and the named gray colors; conditional nhanxet definition is plausible. Compilation, pagination, float placement and final rendered layout are CANNOT CHECK here because builds are prohibited. |
| Page budget | CANNOT CHECK actual13 pages; NOTES' estimates disagree. Treat as an estimate, cut repetition before integration if needed. |
| Owner forbidden claims | No need to add novelty, business value, causal blame or forbidden plan language. The narrow HZ positioning and residual limitation should remain. |
| Evidence rule | Not satisfied while new source facts live only in NOTES. Required edit6 is an integration gate, not a reason to invent facts or ask the owner to waive the rule. |

**What I would retain unchanged in substance:** absolute C accounting and B−L; equality at the cap; fixed cap versus traffic-conditioned reference; N and the two counterexamples; signed q; the exact three-part ledger identity and its noncausal interpretation; causal source-day exclusions; reported pickup-display conflict; historical test-count wording; whole-job runtime with unmeasured per-decision overhead; explicit software-agent verification provenance.

**What I would not accept as established:** unconditional keep-route feasibility, universal no-forcing without hypotheses, measurable large benefits from earlier revisions, independent real-world validation, linear full-validator complexity, temporal monotonicity of D, or bibliography details not present in the primary records.
