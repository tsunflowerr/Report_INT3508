# R37 agent audit — corrections, rejected comments, padding and cuts

Scope: textual verification by direct reads of R29, v10 (450 physical lines), CH4B-REVISION-LOG, both R27 reviews, NOTES, ADDENDUM-6, owner/style/outline rules, and the supplied Ch3 v4-v3. Root owns the independent numeric probes; no numeric probe is claimed here. Proposed verdict: **ACCEPT WITH CORRECTIONS**.

## 1. Every R29 row (CX-01…24)

FIXED means the underlying correction is substantively incorporated, not necessarily copied verbatim. For the two original cannot-check items, NOT means still unverifiable, not a numerical failure.

| Row | Status | v10 physical lines / finding |
|---|---|---|
| CX-01 ML calibration/profile/preview/ablation | FIXED | 190–204 distinguish calibration target 30 s from test extension; frozen 12–13/11 profile, previewed test days, two removed state variables; 206–211 restrict the unchanged result to late counts. Full fit/calibration dates may stay in Appendix C. Language repair for English “gradient” at191 is still needed. |
| CX-02 early pad result | FIXED | 104–106 show 0/0/1 on1.471 and correct the missing E_pad claim. |
| CX-03 clipped snow ledger | FIXED | 347–352 explicitly distinguish clipped addition from signed eq:so. Optional precision: spell out the lower bound0 as well as upper bound. |
| CX-04 computational-limit claim | FIXED | 364–368 only report named counters, deferred request and unchecked limits; refer to insertion-only search through muc:gioihan. Ch3 cross-file counter wording still needs synchronizing (see below). |
| CX-05 original obligation vs forecast display | PARTLY | 284–288 correctly separate replay from original nonforecast deadline, but “41,3%” at286 loses the local “trung bình theo kịch bản” printed only in EV288. Add that phrase. |
| CX-06 Ch3 test synchronization | PARTLY | B381–384 remains correct: clean1.024/1.025 plus separate remaining test. Supplied Ch3 v4-v3:723–724 now incorrectly compresses this into “cả1.025…đều đạt khi chạy lại…với…một tệp chưa ghi nhận”. NOTES137–139 has the correct integration replacement. |
| CX-07 deadline range | FIXED | 444–450 separate main30/60 from morning30–300 and paper900 s. |
| CX-08 unweighted means | FIXED | 90–92 say pooled count block versus scenario mean, each scenario weighted equally; row108 labels mean explicitly. |
| CX-09 K=2 and completed14/15 | FIXED | 181–188 explain current+next15-minute bin;3/32 stops,14 and15 complete, baseline same15 scenario IDs. |
| CX-10 pooled forced decisions | NOT | 184–188 retain only47,6/62,8 scenario means. Rejection is temporary lack of checking, not a reason these counts cannot enter after root’s fresh probe. Preferred placement is short appendix support, or one extra body sentence with both aggregation types. |
| CX-11 full re-solve anchor | FIXED | 25–29 describe separately written re-solve, actual full-order Q4/PV provenance, all recorded choices matched. |
| CX-12 five-arm scope / independence | FIXED | 27–29 say five configurations; EV29 lists FREE and explicitly says same code run twice, not two independent implementations. |
| CX-13 window counts | FIXED | 100–106 display68/22/2 and all three window rows. |
| CX-14 rounded sum | FIXED | EV177 now81,742+5.352,646+783,018=6.217,406, with independent-rounding caveat. |
| CX-15 FleetPy future pickup wording | FIXED | 183 “FleetPy tính rằng xe sẽ tới…” avoids treating failed-run projected pickup as observed arrival. |
| CX-16 w08 rounding8,4 | FIXED in corrective record | v10 does not print8,3 or8,4; EV188 points to N4B-07/06; ADD6:64 explicitly corrects8,3→8,4 and NOTES125 records8,4. |
| CX-17 ML denominators | FIXED | 206–211 contain147/197,145,200,807. |
| CX-18 no generalization to all cap/pad values | PARTLY | 295–299 drops the30-s identifiers and says padding “không kém luật C”, although290–292 gives C-1202379>padded U2366 at120 s. This is a real scope regression: specify C-30 and U+forecast+30-s pad. |
| CX-19 four thresholds / different cohorts | FIXED | 390–394 explicitly “trên hai nhóm khách khác nhau”. |
| CX-20 local ML preview | FIXED | 195–196 local preview and421–423 global caveat. |
| CX-21 register corrections | FIXED by additive supersession | v10 EV29/106/177/188/204/352/368 use N4B8 corrective rows; ADD6:58–70 names old rows superseded. Old evidence files remain unchanged as required by exclusive-create rule. N4B-02 was already five-arm accurate; its new support is N4B8-10. |
| CX-22 NOTES bookkeeping | FIXED | v10 header2 and NOTES0/1 describev10, remove obsolete497-line claim. Actual450 physical lines. |
| CX-23 Ch5 prioritizes cost-first | NOT — CANNOT CHECK | v10:71–73 still asserts Ch5 places this first. No rewritten Ch5 file found in drafts or a codex-work Ch5 directory. NOTES169–170 correctly calls this an integration obligation. Prefer remove the unverified assertion from B pending Ch5. |
| CX-24 actual pagination/layout | NOT — CANNOT CHECK | No build allowed. NOTES26–44 honestly provides only330-token ruler estimates and reports budget unmet. Syntax/cross-ref scans cannot certify rendered pagination/table collisions. |

Not every count-and-denominator issue is repaired by CX-13/17: new body text124–125 suppresses1471 versus1470 for the two rules and437/418 for17 h; hidden EV128 does not satisfy a printed count/denominator requirement.

## 2. Rejected comments: verdict on each

| Comment | Verdict / reason |
|---|---|
| CX-10 | **Reconsider once root’s script verifies.** Counts are available from BIC and explicitly supplied in R29§2.8. R29 did not reject them; the reviser declined to check. Do not replace47,6/62,8 means with pooled rates; print the counts as a distinct aggregation on the same15 completed scenario IDs. |
| B47 | **Uphold rejection.** OUTLINE-V2:197 explicitly requests “vai trò của từng thành phần”; its authority outranks an editorial label suggestion. Current269 still uses it. The reader’s alternative “Bốn điều…” is additionally obsolete because v10 has only three numbered findings. |
| L-02 | **Uphold omission in v10.** Intermediate C-60/C-120 screening rates are also omitted from body, so table no longer lacks configurations discussed in prose. Adding two complete columns without verified cost rows would invent or leave a half table and aggravate budget. The rejection should be framed as scope/pagination, not as impossibility of ever computing the missing costs. |
| L-04 | **Uphold rejection.** STYLE§27:331–332 explicitly keeps full numbers in tables;50 retains0,3069/0,0794 while61–64 prints0,31/0,08. This follows the authoritative style rule. |
| L-15 | **Uphold, with caption qualification.** Counts and scenario-average extensions are different useful estimands and can share a table if caption labels both. v10:318–320 does. A pooled extension column need not be invented to force uniform aggregation. |
| L-23 | **Partly uphold only for adding nonexistent positive checks.** R27:640 accurately says replay/padding/ML paths lacked a separate independent check. “No saved independent check” supports a limitation, not dismissal of the critique. Current374–379 asserts checks only for main counts/7159 riders; it should expressly distinguish replay and learned-model pathways unless root independently validates them. |
| L-26 | **Partly uphold only for demanding nonexistent new sensitivity results.** No simulation may be run. But “one run each”419–420 and Ch3 seed7:704–706 support a concise missing-sensitivity caveat. Unrun experiments are legitimate limitations. |
| L-27 | **Uphold as optional editorial move.** Ch3 v4-v3:477–481 already explains saturation and references B370–372 for exact counts. Repetition near the screen could be useful but is not required for factual validity. Under page pressure conditional relocation is better than repeating. |
| L-31 | **Uphold rejection of the stale premise.** E_pad was measured; B104–106 now prints0/1471. R27’s “not measured” must not be imported as a limitation. |
| L-33/L-52 | **Reconsider as a read-only analysis request, not mandatory new simulation.** Current225–227 fairly discloses2207 common riders and different cohorts. Absence of a saved common-cohort output is not a principled reason to reject a permitted probe. Such a comparison conditions on a policy-dependent served intersection, so even if computed it is descriptive, not a causal matched control. Existing overall comparisons remain valid under their labels. |
| L-34 | **Uphold rejection.** BRIEF-CH4B-WRITER:28–29 explicitly says state four conditions without when set. Do not introduce the forbidden plan/timing discussion. Local preview/calibration wording190–204 remains required and is present. |
| L-40 | **Uphold rejection.** Naming the accounting component consistently with Ch3 eq:so is legitimate.126–127 and308–309 use “Theo sổ”; figure171–174 says the component depends on the chosen forecast and residual is not inherently unknowable. No independent causal attribution is claimed. |
| L-50 | **Uphold rejection.** Inventing a reason the full cost-first run was not performed is forbidden.19–22,71–73 and441–443 state the absence and affected conclusion. A workflow/deadline narrative adds no evidence. |
| L-60 | **Uphold rejection of a tolerance outcome.** No tolerance variant has been run.181–188 reports exact tried implementation and finishes “chỉ áp cho cách đã thử”; it does not prove all in-dispatcher forecasts fail. A new sensitivity/tolerance run may be future work, with no invented result. |

## 3. Padding opening: fair, with one necessary repair

217–227 directly admits equality at60 s and padded U’s advantage at120 s;37,2 and7,4 are correctly **extra duration**, not total quote lengths. It states replay leaves dispatch unchanged, the174/590,1 exposure numbers are on U journeys, and serving96 fewer is the price under C-30.225–227 makes the cohort mismatch explicit. It does not claim C wins timely counts or holds the original first arrival promise.

However220–222 says “theo cách xây dựng luật…nhiều nhất29,2 giây”. Construction enforces30 s;29,2 is an observed maximum. Replace those two clauses with:

> Luật C trần 30 giây giới hạn tổng phần dời này của từng khách ở 30 giây; trên tập kiểm tra chính, mức lớn nhất ghi nhận là 29,2 giây, kể cả ở các kịch bản cuối tuần không có dự báo. Đổi lại, luật C phục vụ ít hơn 96 lượt.

Normalize spaces in the thesis numbers/units. The proof assumes its enforcement conditions; do not interpret this as a30-s guarantee on arrival lateness or original first quote.

## 4. Exact Vietnamese replacements for remaining concerns, ranked

1. **Restrict choice claim to tested C-30/pad30** (replace295–299):

> Nếu hãng xe chỉ tính số lượt không trễ quá hai phút và chấp nhận lời hứa dài hơn cùng nhiều khách tới sớm hơn, điều phối không trần có dự báo và đệm 30 giây đạt 2.366 lượt, so với 2.338 lượt của luật C trần 30 giây có dự báo, đồng thời phục vụ thêm 96 lượt. Nếu cần giới hạn phần dời do ghép thêm khách cho từng người, kể cả khi không có dự báo, luật C trần 30 giây làm được điều này, đổi lại 96 lượt phục vụ và 242 khách đi chung. Hai cách dùng chung được; chọn cách nào là quyết định của hãng xe, không phải kết luận của thực nghiệm.

2. **Separate theorem bound from observed max**: use §3 replacement for220–222.

3. **Restore visible denominator distinctions** (replace124–125; preserve126–128 ledger sentences):

> Lợi ích không riêng của luật C. Với dự báo, luật hạn chót30 giây giảm từ 66 xuống 2 khách trễ trong 1.471 khách được phục vụ; luật trần độ dời khách thấy30 giây cũng giảm từ 66 xuống 2, nhưng trong 1.470 khách. Điều phối không trần giảm từ 129 xuống 63 trong 1.512 khách. Ở khung 17 giờ, 28 khách trễ trong 437 khách của điều phối không trần không đổi sau dự báo, còn luật C không có khách trễ trong 418 khách.

4. **Repair assembly test sentence** (Ch3 v4-v3:723–724, outside this agent’s writable deliverable):

> \item \textbf{Kiểm thử phần mềm:} khi chạy lại ngày 12/10/2026 trên đúng mã nguồn đã dựng bộ chạy, với kiểu xuống dòng LF, 1.024 trong 1.025 kiểm thử tự động đạt. Kiểm thử còn lại đòi cây làm việc có tệp chưa được ghi nhận, và đạt khi chạy riêng với một tệp như vậy (Phụ lục~\ref{phuluc:C}).

5. **Restore aggregation in original-obligation contrast** (replace286–287):

> Theo nghĩa vụ đó, nó bị ép ở 41,3\% lượt quyết định, trung bình theo kịch bản, và có khách bị phá lời hứa ở 28 trong 34 kịch bản. Luật C không có quyết định bị ép hay khách vượt trần (Bảng~\ref{bang:c4-nghiavu}).

6. **ML term** (191–192): “cây quyết định tăng cường theo độ dốc (gradient boosting)”.

7. **Missing validation scope**, append before381 if checks remain absent:

> Các phép kiểm này chưa kiểm độc lập toàn bộ cách phát lại lời hứa, cách đệm và đường tính của mô hình học máy.

8. **Missing seed sensitivity**, append to419–420:

> Chưa kiểm độ nhạy theo hạt giống của bộ giải, nên chưa biết các chênh lệch có giữ nguyên khi đổi hạt giống.

9. **Remove unverified Ch5 arrangement**, replace72 with:

> Khóa luận vì vậy chưa tách được phần của trần và phần của bộ chọn; phép thử này là một hướng phát triển còn mở.

10. **Precise clipped rule**, replace347–348:

> Phép phát lại này tách số giây trễ theo cách cộng có giới hạn, khác phần có dấu của công thức~\eqref{eq:so}. Phần kéo dài của mỗi khách được chặn trong khoảng từ 0 đến phần trễ còn lại sau khi trừ phần tính cho điều phối.

11. **Ch3 counter scope**, replace Ch3 v4-v3:706–707 lead-in:

> Vì vậy bộ sinh không xét hết mọi phương án; mục~\ref{muc:c4-hople} báo các bộ đếm đã đọc của bộ sinh. Các số này không đo mọi giới hạn của bước sinh, kiểm và giải.

These are replacement content; typesetting spaces should be normal Vietnamese (e.g. “trần 30 giây”, “trong 1.471 khách”) in the integrated review.

## 5. Rank NOTES §4 cuts by least argumentative loss

NOTES groups several unequal-risk cuts together; split them before choosing. Listed savings sum approximately **540**, not600 tokens, and nominal13,1→11 pages would need roughly693 text tokens if table/figure allowance stays unchanged. These are ruler estimates, not rendered pages.

1. **Drop the untested hypothesis410–411** (NOTES4.1,≈30): limitations408–410 retain the actual scope. Lowest loss.
2. **Merge “Tích hợp” into “Mô hình mô phỏng”** (4.1,≈25) while retaining432–435. Mostly organization.
3. **Conditional relocation of saturation370–372** (4.5,≈30): move exact3503/3506/3504 to Ch3:477–479, keep a direct pointer at screen. Do not delete now: Ch3 refers here, so deleting makes the count support circular/missing.
4. **Shorten in-dispatcher forecast181–188** (4.2,≈80), preserving K=2,3/32,completed14/15,same15 baseline, aggregation and implementation-only caveat. Details/values belong in an actually assembled appendix.
5. **Move detailed ML feature/split/calibration exposition to Appendix C** (4.2,≈170), preserving locally fixed12–13 profile, calibration target30,test days already seen, four conditions (or an unambiguous appendix pointer), negative result and count denominators. Do not reduce to an unqualified “ML added nothing”.
6. **Compress C-120 interpretation290–293** (4.3,≈45): row250 retains the point, but retain one sentence “Trần120 giây cho kết quả khác theo hai ngưỡng; hàng này đo trên một nhóm khách khác.” This prevents the final choice paragraph appearing to claim C-30 dominates.
7. **Shorten snow blend definition312–314** (4.4,≈35) rather than delete: table rows332–335 state inputs, not the geometric-combination rule. Keep “Cách trộn dùng trung bình nhân của dự báo lịch sử và mức tăng tắc đường cùng ngày.”
8. **Replace main-set data-reuse details421–423 with Part A pointer** (4.1,≈45) only if retain local “Chiều tuyết và các ngày kiểm học máy cũng đã được xem, nên các kết quả là thăm dò.” Part A’s main-set caveat does not cover these local experiments automatically.
9. **Shorten unchanged-accepted-count explanation66–69** (4.6,≈40): lower priority; the hierarchy explanation answers examiner Q2. Never remove35,5=sum of two17,77-s riders while leaving table55: otherwise it looks like violating30-s cap.
10. **Do not cut the shared-source/three-previewed-morning CI caveat121** (4.2,≈25) merely because global limitations exist; it limits these particular confidence intervals and shared source12/11.
11. **Do not cut no-reassignment applicability412–413** (4.1,≈15); it states a material model restriction distinct from rider response.

A safe budget repair needs edits beyond blunt deletion of all NOTES items, or explicit owner acceptance of the approximately13,1-page ruler estimate. No build or render was performed.
