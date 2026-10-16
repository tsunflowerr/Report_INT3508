# R34 Ch4A v4 — consistency and rejection audit (v3)

Scope: delegated part of R34, not the master report. **Recommendation: ACCEPT WITH CORRECTIONS.** No A/B outcome count in a repeated, identical cohort was found to disagree. Two scope statements and one owner-rule refusal need correction; B-v7 also retains old terminology and a stale 120-second disclosure.

Pinned files: `drafts/08-chuong4-phanA-v4.tex` (**A**), `drafts/09-chuong4-phanB-v7.tex` (**B**, regardless of a later v8), `drafts/07-chuong3-v3.tex` (**Ch3**). All line numbers below are one-based physical file lines, including blank/comment lines. Read `CODEX-PARALLEL-RULES.md`, `WRITING-BRIEF.md`, `CH4A-REVISION-LOG-v2.md`, the R25 reader/lecturer and factcheck reviews, OUTLINE-V2, STYLE, corrected glossary, ADDENDUM-1 §0 and relevant register rows. Static scans and source reading are **not** independent recomputations of outcome counts.

## 1. Ranked corrections and exact Vietnamese replacements

### 1. Calibration scope is still too broad (A106–109; CX9/CX15)

A108 says `dành cho một phép hiệu chỉnh không dùng trong khóa luận`. The calibration procedure may indeed be unused, but the sentence invites the stronger reading that these scenarios are unused in the thesis. The revision-log justification is explicitly false: log CX9 says the 15 scenarios supply no chapter number. Ch3:707–709 includes their 15 C-30 runs in the **382.006** repair-record audit (185 = 170 + 15 runs); B414–415 invokes that audit. T38:99–106 and RUN38, as quoted by Ch3:720, support this scope. Do not call it a new count error; it is an overbroad exclusion/ambiguity and an incorrect rejection rationale.

Replace the first three sentences of A106–108 by:

> Chương này dùng bốn tập kịch bản (Bảng~\ref{bang:c4-taptu}). Từ các ngày 14--18/11/2018 dựng được 49 kịch bản, chia theo cặp ngày và mẫu để ba khung giờ của một cặp nằm cùng một phía. 34 kịch bản làm tập kiểm tra chính; 15 kịch bản còn lại không dùng để tính các kết quả phục vụ và đúng giờ của chương này. Các lần chạy trên 15 kịch bản đó chỉ tham gia phép kiểm tính nhất quán của sổ ở mục~\ref{muc:kiemtra}.

Retain the day/weekend sentence. Suggested EV: `B08; C17; A26; Ch3 mục muc:kiemtra (RUN38:1–8; T38:99–106)`.

### 2. CX7 appendix-budget refusal does not satisfy the owner rule (A546–547)

Owner rule: **every rate shows count and denominator**, plus aggregation. Appendix ≤3 pages is also an owner constraint, but it does not authorize an unsupported exception to the first constraint. `Trung bình theo kịch bản` correctly identifies the estimand; it does not supply its constituent counts. The 58,6%, 6,6%, 1,7%, and `luật C luôn 0%` at A546–547 still lack decision counts. The same issue remains for individual-cell means in the obligations/window discussion (A315–317; A335–337). A334 supplies the pooled M⁺-30 counts, which are helpful but are **not** the numerator/denominator of the 41,3% unweighted mean.

W07X:20–29 confirms the displayed morning means and the nonmonotone middle pair (6,6% at 120; 6,8% at 150). It does not print the eight constituent decision count pairs in that aggregate table. NOTES99–100 acknowledges that counts were not copied; citing the source in `% EV:` is not showing the count in the rendered thesis.

A small correction that meets both budgets is to remove the unsupported percentage sentence at A546–547 and replace it with:

> Luật C không có quyết định bị ép trong 64 lần chạy của tám mức trần này. Ở cả tám mức, hai luật phục vụ chênh nhau không quá 2 lượt.

This replaces `Tỉ lệ lượt quyết định ... luật C luôn 0\%. Ở cả tám mức ...` through the end of A548. Keep the preceding served/timely count comparisons. The 64 = 8 scenarios × 8 levels is already A722 and E01/D04; this is a count of runs and a statement of zero events, not a made-up pooled percentage. If the morning means are retained instead, add **verified constituent decision counts** in a separate compact block; do not invent one pooled pair that supposedly equals a cell mean. The analogous obligation/window means need either the corresponding count information or an editorial reduction to the already verified count statements.

### 3. B-v7's limitation contradicts A's corrected main-set reuse disclosure (B460–461)

A229–233 correctly says the 120-second level followed U/C-30 results **on the main set**, including 120-second screens. B460 says thresholds, split and 120-second level were selected after development data. It omits the material main-set reuse and restores the understatement that A just fixed (C4A-11; factcheck #57/#176).

Replace B460–461 with:

> \item Ngưỡng phân tích và cách chia tập được chọn sau khi đã xem tập buổi sáng và các đợt chạy thử trước đó. Mức 120 giây được chọn sau khi đã xem kết quả của điều phối không trần và luật C trần 30 giây trên chính tập kiểm tra chính, kể cả các phép sàng lọc ở 120 giây. Chiều tuyết cũng là sự kiện đã xem; mọi kết quả là thăm dò.

Suggested EV: `I06; C4A-11; K42; I11`. This uses data-reuse wording only.

### 4. B-v7 must use A/Ch3's corrected event name (B188–190, B319–320, B393–394)

A196–200 defines `quyết định bị ép`. Corrected glossary v2:105 and Ch3 use this name. B still reports the very same counter as `phải phục hồi`, although A-NOTES128–130 explicitly told B to change it. This is a terminology regression, not a disagreement between 0, 41,3 or 47,6 and the recorded event counts.

Exact replacements:

- B188–189: `Ở các lần chạy xong, luật C không có quyết định bị ép. Với luật hạn chót, tỉ lệ quyết định bị ép là 47,6\%, so với 62,8\% khi không đưa dự báo vào (trung bình trên 15 kịch bản).`
- B319–320: `Khác biệt là luật hạn chót có 41,3\% lượt quyết định bị ép (trung bình theo kịch bản) và phá lời hứa của chính nó ở 28 trong 34 kịch bản, còn luật C không lần nào (Bảng~\ref{bang:c4-nghiavu}).`
- B393–394, after the two maxima: `Không có quyết định bị ép: 0 trong 20.101 lượt với trần 30 giây và 0 trong 20.435 lượt với trần 120 giây.`

The first two retain B's existing mean rates only for term consistency. They still inherit the owner count/denominator issue; apply correction 2's rule if editing those paragraphs too. Update the hidden B432 EV wording to `0 quyết định bị ép` as well.

### 5. Three unresolved references remain (A20, A148, A224)

Static scan: A+B+Ch3 has no duplicate label, but misses `muc:c1-cauhoi` (A20), `phuluc:C` (A148), and `phuluc:A` (A224). A scan of all top-level draft `.tex` files and current thesis `noi-dung/*.tex` found no definitions either. A→B references are otherwise resolved; B does not refer to the removed `bang:c4-ngaykhung`.

Preferred assembly correction: define these labels on the actual research-question section and the actual appendices; do **not** create dummy anchors to unrelated content. This is an assembly obligation already noted in A-NOTES66; it is not evidence of a new v4 deletion.

If appendices are not assembled, precise fallback wording is available without a broken ref:

- A20: `Bảng~\ref{bang:c4-lotrinh} nối ba câu hỏi nghiên cứu với các mục trả lời chúng.`
- A147–149: `Lần chạy hỏng vì lỗi hạ tầng (một lần ở tập kiểm tra chính) được thay bằng bản chạy lại hoàn tất. Bản kiểm kê ngày 08/10/2026 ghi 1.991 bản ghi lần chạy; kết quả của chương chỉ lấy từ bốn tập trên, các đợt chạy khác chỉ được nhắc khi nêu phạm vi kiểm tra (mục~\ref{muc:c4-congdon}).`
- A223–224: `Trần chính $B$ = 30 giây là trần giờ trả của cấu hình có trần ở tập kịch bản tĩnh của đợt thử trước, nơi thời gian đi không đổi.`

These fallback sentences remove the external cross-references; they do not assert that the missing material was supplied.

### 6. Minor language issue in B409–410

No hard forbidden owner phrase was found in A/B, including comments: no restricted plan/disclosure vocabulary and no uniqueness/optimal-cap claim. B409 contains `byte` inside Vietnamese prose. It is avoidable, with no lost precision.

Replace by:

> Nội dung các tệp chính sách cam kết của điều phối không trần và luật C trần 30, 120 giây trùng khớp hoàn toàn giữa tập kiểm tra chính và tập tắc đường cố định.

B's first-use `(gradient boosting)` at B196 is the allowed one-time technical-English parenthesis. `LF` at B416 is an unexpanded line-ending abbreviation (minor clarity issue), not a prohibited novelty claim. If retained, use `với kiểu xuống dòng LF (ký tự kết thúc dòng)` once. Software/product names and symbols in tables are allowed.

## 2. The four outright rejected comments

| ID | Rejection verdict | Independent check and scope |
|---|---|---|
| D11, explain random seed again | JUSTIFIED | Ch3:687–688 already defines `hạt giống ngẫu nhiên (số khởi tạo phần ngẫu nhiên)`; A says fixed at 7. Repeating the glossary explanation is optional. A seed value alone does not verify the suggested rerun-equivalence promise. |
| D-c2, reconcile `s`/`giây` | JUSTIFIED | STYLE rule 26 explicitly requires prose `giây`, table units `s`. Unit abbreviations in tables are allowed. |
| G1-r2, seed sensitivity / actual rerun evidence | JUSTIFIED to decline a claim of completed reruns; limitation remains | B11/T38:90 describes the deterministic setup; L1a-04 (ADDENDUM-1:143) explicitly rereads stored transcripts. T38:94 refers to replacements for failed jobs, not completed-run equivalence testing. No opened source establishes a seed-sensitivity study. B's integration limitations retain rebuilt-runner equivalence as future work. |
| G1-t, add +31 = 0,84% of requests | JUSTIFIED | A243–245 already gives +31 and −5 with the timely counts; A287–291 explains the different served cohorts. 31/3.672 is redundant and does not alter the threshold-dependent result. |

## 3. Every partially declined item in log §6

| Partial decline | Verdict | Check |
|---|---|---|
| D4 / G1-d1 / G6-5: how 108 requests are selected | JUSTIFIED to omit an unverified archived-source method; qualify the missing-evidence claim | B02/J18 establish 108 from a 10% daily sample. Current `FleetPyManhattanNormalizer.cs` exposes a method: NORM112–125 validates a target; NORM659–666 orders by a keyed deterministic rank; NORM750–755 keeps rows with both endpoints in the node pool and takes the configured target. One fixture has target 108 and maximum 96 nodes. This static one-fixture check does not prove current code matches every archived fixture. If adding a selection paragraph, establish that source-version link first. Do not describe the 108 as a simple random sample. |
| D7: why disjoint windows overlap | JUSTIFIED | T38:93 says shared source and 3–20 of 108 row overlap. It does not establish the mechanism for the 17-hour window. A68–70 preserves the dependence caveat without inventing a mechanism. |
| D39: `họ trễ vì đường đông` | JUSTIFIED | REG K39:392 replaces a causal claim with no recorded dispatch update. A378–381 uses 72 of 76 with no dispatch update and says forecast targets the predictable part. Ledger accounting cannot identify sole cause. |
| D45 / CX6: rider was already on the vehicle | JUSTIFIED | W07XM6/11/16 reports promise history and x/c, without waiting/onboard phase. W07X54 says `khách đang có`. A440–446 uses `một khách` and projected promises. |
| D46: examples of structural constraints as established rejection reason | JUSTIFIED | BUDPY29–44 partitions rejected requests by a recorded budget-pruned candidate; the residual group is merely the `else` branch. A449–455 avoids treating absence of a recorded block as structural-only proof. |
| D57 / G6-13: 120-second conclusion in the figure caption | JUSTIFIED | STYLE rule 22 disallows a conclusion absent from the plotted quantity. The figure plots late60, not timely120. A686–690 gives the threshold-dependent conclusion in prose. |
| D53 / G6-7: morning means in the pooled-count table | JUSTIFIED for placement, PARTLY for reporting | OUTLINE §2 rule 3 forbids cell means sharing a pooled-count block. A520–540 is a count table. Omitting constituent counts for means left in prose is the CX7 owner-rule issue. |
| G6-6: separate notation box | JUSTIFIED | STYLE rule 7 allows at most one box for the main conclusion; no notation box is required. A113–116 defines arms, A179–183 defines a/p0/D0/c/z, and Ch3 defines L/B. |
| G4 / G6-1 / RQ1: full padding discussion in 4.2 | JUSTIFIED | OUTLINE 4.8 assigns it to B. A248–250 supplies the crucial equality 2.328 with a cross-reference. B217–334 gives promise-length, early-arrival, tail, individual-bound and scope comparisons. |
| CX7: constituent count pairs in the appendix | NOT JUSTIFIED as an exception to owner counts | The three-page appendix limit constrains presentation; it does not waive count/denominator information for displayed rates. Supply verified pairs or remove unsupported rates. See correction 2. |
| RQ2: analyze 76→10 in A | JUSTIFIED as allocation; handoff implemented | A578 reports 10 across all 34 scenarios and labels replay/weekday coverage at A557–559. B79–82 analyzes 68→2 in the 21 weekdays; B246 reports 10 across all 34. Eight weekend late riders remain: 76−68 = 10−2 = 8. |

## 4. Remaining M rows: exhaustive completeness check

This section and §3 cover all **39 M rows** listed in log §5, including editorial changes with no distinct declined clause in log §6.

| IDs | Verdict | v4 location / reason |
|---|---|---|
| CX6 | JUSTIFIED | Projected-promise/phase distinction; A440–446. |
| CX7 | PARTLY; correction required | Ledger-share and fixed-set counts supplied at A400–418 and A482–501; constituent-count refusal remains inadequate. |
| CX9, CX15 | PARTLY; correction required | Inventory date supplied at A148, generator anchor corrected at A101, register corrections documented; calibration exclusion at A108 remains broad. |
| FC#75, D33 | JUSTIFIED editorial omission | Entire common-rider wait/ride sentence removed, so no unlabelled mean survives. A287–291 retains served cohorts and the +31 interpretation. |
| FC K-6 | PARTLY; assembly pending | Missing external contents cannot be manufactured. Honest NOTES disclosure does not resolve missing labels/citation keys for the assembled thesis. |
| D1, D2 | JUSTIFIED | A15–20 and A31–43 explain padding, retain three accounting parts rather than three causes, and use the corrected forced name. |
| D4–D7 | JUSTIFIED with source scope | A60–70 fixes day-level sample wording and terminology; avoids untested rerun equivalence and an overlap mechanism. D5's omitted 1,2 example already appears in Ch3's terminology table. |
| D13, D14 | JUSTIFIED | A113–116 defines arms; A127–145 corrects morning run count, snow request count and runner distinctions. Column renaming and a separate prose list are optional. |
| D17 | JUSTIFIED | A157–159 references the reversal whose exact +31/−5 appears at A244–245. |
| D24 | JUSTIFIED | A201–205 retains glossary `Khách bị phá lời hứa` and defines the different obligations. |
| D25 | JUSTIFIED | A223–227 defines static travel time and omits an unregistered 20-scenario count. The appendix reference remains an assembly dependency. |
| D30, G6-3 | JUSTIFIED | A270–274 fills late 79/74 and timely counts; only sharing is uncounted. A337–339 interprets V through the accounting inequality. |
| D35 | PARTLY concerning theorem scope | Ch3's theorem explicitly requires 0≤L≤B and (N). A327–331 cites (N) but abbreviates the c=0 argument; root is checking this separate scope issue. Declining a duplicate 40-second example is justified. |
| D39, D45, D46, D53, D57, D62 | JUSTIFIED except the denominator issue | First five are in §3. D62: A751–756 identifies fixed/synthetic audit scope; the old sweep is not a fifth outcome set, so an extra outcome-table row is unnecessary. |
| RQ1, RQ2 | JUSTIFIED | Full padding and forecast interpretation are handed to B; §3. |
| G1-d1, G1-d3 | JUSTIFIED | Selection scope above; outcome-vs-audit distinction at A148–150 and A736–740. Calibration A108 remains the exception needing correction. |
| G3-h1 | PARTLY; omission tolerable, log rationale incomplete | The caveat at A459 applies to the 59-of-148 screen, not directly to U serving 116 of 148 at A451. A289–291 already gives 227 U-only and 131 C-only riders, net 96, so the necessary global cohort warning exists. A single local sentence would be clearer; replacement below. |
| G4, G6-1, G6-3, G6-5, G6-6, G6-7, G6-8, G6-13 | JUSTIFIED except identified issues | Padding allocation, V interpretation, bounded selection, optional box, separate means, no invented 1-ms cause, and caption discipline checked above. The zero-dwell limitation is carried to B. G6-8 overshoot explanation is corrected at A457–462; cause of the 1-ms shifts stays unverified. |

Optional G3-h1 sentence immediately after U serving 116 at A451, evidence C01/C04/D13:

> Con số 116 chỉ xét nhóm 148 yêu cầu này; chênh lệch số lượt phục vụ trên toàn tập là 96, vì hai cấu hình nhận những khách khác nhau (mục~\ref{muc:c4-ketqua}).

D42/RQ4 are CC, not M/R. Keeping 33 moved riders while specifying 29 later shifts and four earlier shifts of 1 ms at A426–428 matches `c != 0`. Changing 33 to 29 silently changes the cohort. No verified rounding cause was added.

## 5. A/B numerical differences and scopes

This compares differing quantities in repeated topics. Unrelated software digits, TikZ coordinates and wholly B-only estimates are not paired outcome claims. Common same-cohort entries agree; this comparison identifies no outcome count requiring correction.

| Topic | A vs B | Classification |
|---|---|---|
| C-30 late60 without forecast | A268: 76 of 2.338 across 34; B79–80: 68 of 1.471 across 21 weekdays | Different cohort; eight weekend late riders. |
| C-30 late60 with forecast | A578: 10 of 2.338 across 34; B79–80: two of 1.471 across 21 | Different cohort; eight weekend riders unchanged. B246 repeats 10. |
| Mean late rates | A344–345: 14,6% at the 30-second threshold across 34; B81: 6,01%→0,17% at 60 seconds across 21 | Different threshold/cohort; no contradiction. |
| Early60 counts | A571 raw: 7/3/1; A578 forecast: 8/4/2; B296–298 forecast: 8/4/2 | Raw vs forecast promises differ; repeated forecast counts agree. |
| C-30 weekday early60 | A has three raw or four forecast early riders across 34; B107: raw 0%, forecast 0,08% mean across 21 | Different cohort/aggregation; four is not the numerator of that mean. |
| Forecast extension | A582: 7,18/7,37/7,27 seconds pooled across all served riders in 34; B129–132: C-30 drop extension 13,7, morning 27,8, pickup 3,2 seconds, means across 21 | Different cohort/aggregation and pickup vs drop dimension. B explains 7,37 explicitly. |
| Padding extension rounding | A582: 7,18/7,37; B220: 37,2 vs 7,4; B245–252: exact 7,18/7,37/7,27/37,18/37,37 | Rounding/padding; 7,18+30=37,18 and 7,37+30=37,37. |
| C-30 ledger late cohort | A403: 82/6.892 seconds for 76 late riders across 34; B155–156: 82/6.217 seconds for 68 late weekdays across 21 | Different cohort. A418 precise: 81,742/6.891,526; B182 precise: 81,7/6.217,4. |
| C-30 dispatch share | A417: 1,2%; B155: 1,3% | Different denominator/cohort above; no changed ledger definition. |
| Dispatch sum/displacement | A401–403 signed sum among late riders, A411–414 absolute cumulative displacement per rider; B174–180 signed ledger share, B312–315 individual cumulative bound | Different metric. Do not substitute signed q with sum of absolute c. |
| Snow requests/served/late | A134: 864 requests; A436: 601 served; B339: 601 served, 41→34 late | Different units/replay; same snow set. |
| Snow/global C-30 maxima | A435–437: snow 25,2 seconds; main maximum at A393 and B313: 29,2; B315 extends cap-validity claim to snow | Different cohort. A global bound 29,2 still covers snow, whose exact maximum is 25,2. |
| Fixed FREE vs ML test | A492: 1.629 served across all 16 fixed scenarios; B210: 807 ML test customers | Different cohort; B199–200 says comparison uses days excluded from learning. |
| M⁺-30 forced mean | A315 and B319: 41,3% mean across 34 | Numeric agreement; B's old event name needs correction. |
| M⁺-30 pooled vs mean | A334: 7.710/20.103 = 38,4%; B319: 41,3% mean across 34 | Different aggregation; do not force equality. |
| Forecast inside dispatcher | A315: 41,3% full-set M⁺-30 forced mean; B188–189: 47,6% with forecast vs 62,8% without, means over 15 completed scenarios | Different experiment/cohort; not a replacement of the 34-scenario replay result. |
| M⁺-30 promise failure | A315: 14,5% mean across 34; B190: 39,0%→11,0% mean across eight morning scenarios with forecast inside dispatcher | Different cohort/experiment. |
| Forced count denominators | A600: C-120 0/20.435; B393–394: C-30 0/20.101 and C-120 0/20.435; A329: U 0/20.760 | Agreement; different arms have different decision counts. |
| Rider-identity totals | A288: U/C-30 2.207 common +227/131 private; A603: C-30/C-120 2.266 common +121/72 private; B414: 7.159 served arm-records | Different units: 7.159 = 2.434+2.338+2.387; not unique people across arms. |
| Run/repair scopes | A129: 136 of 192 archived morning runs; A723: 64 morning C runs; A736: 132/140 cap-audit runs; B415: 382.006 repair records in 185 runs (Ch3) | Different cohort/unit. The real conflict is the broad calibration exclusion, not these counts. |
| Morning forced ladder | A546–547: 58,6→6,6→1,7%; absent from B | A-only. W07X has intermediate 6,8% at 150; A does not claim a fully monotone ladder. Constituent counts remain missing. |
| Equal timely120 value | A574: 2.366 for raw C-120; B251: 2.366 for U forecast plus 30-second padding | Coincidental equal value, different configuration; cross-references do not switch the two. |
| 120-second selection | A229–233: main-set results/screens viewed; B460: development data only | Real scope conflict; correction 3. |

Common same-cohort quantities agree: 34 scenarios, 3.672 requests; 2.434/2.338/2.387 served; forecast late60 137/10/65; timely60 2.297/2.328/2.322; timely120 2.347/2.338/2.379; forecast early60 8/4/2; extension 7,18/7,37/7,27 seconds; −96 served and −242 sharing; maximum dispatch shift 590,1/29,2/118,9 seconds; C-30/C-120 zero forced events; M⁺-30 mean 41,3% and 28 of 34 scenarios with promise failure; 601 snow customers. B-only selector costs, confidence intervals, ML, nowcast and software-test values have no matching A claim to disagree with.

## 6. Terms and cross-references

| Term | A vs B | Assessment |
|---|---|---|
| Forced event | A196–200 `quyết định bị ép`; B188/319/393 `phải phục hồi` | Real terminology mismatch; correction 4. |
| Aggregation | Both use `trung bình theo kịch bản` and `gộp theo khách` | Definitions agree; count omissions are separate. |
| Replay | A172–175 recomputes displayed promises with schedule unchanged; B84–89/229–233 agrees, with a separate dispatch experiment at B185–192 | Consistent; experiments are distinguished. |
| Measured traffic | `hệ số tắc đường đo được`; B's future-information replay calls its future factors `hệ số thật` | Different information time, not conflicting world labels. |
| Ledger | `phần tính cho điều phối`, `phần được hồ sơ lịch sử giải thích`, `phần còn lại` in both | Consistent; residual remains dependent on the forecast rather than inherently unknowable. |
| Promise failure | Law-specific definition in A201–205; same name in B | Consistent; thresholds/promises depend on law/experiment. |
| Uncapped/FREE | Separate definitions at A113–116 and A142–145; A507–511 says FREE changes selector and validation; B keeps its distinct screens/ML cases | Consistent; no cap-only interpretation of U vs FREE. |
| Bound | Both use `trần`; B323 uses the optional metaphor `núm vặn` | No factual mismatch; minor style choice. |
| Calibration | A108 broad exclusion; B415 invokes an audit including 15 calibration runs | Clarify scope; correction 1. |

All A→B section labels (`muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet`, `muc:c4-hople`) resolve in pinned B-v7. All B→A table labels resolve. Ch3 labels used by A resolve. The three unresolved external labels are listed in correction 5; no duplicate label was found in A+B+Ch3, and no B reference uses the removed day/window table.

Bibliography static check of `.tex` definitions: current thesis has `schulz2026` at `10-tai-lieu.tex:116`; no `engelhardt2026` or `horl2022` bibitem was found in scanned top-level draft/current-thesis `.tex` files. This is an assembly dependency, not absence of registered metadata. `engelhardt2026` was already noted by log FC K-6 and A-NOTES66–67. No build was run.

## 7. Saved probes and limits

- `consistency-audit.py` and `consistency-audit-output.txt`: static label/forbidden-word/cohort/rate/log/style scan. First invocation failed because `python` was absent from PATH. The pinned interpreter wrote the complete UTF-8 output before its console print failed on cp1252. The output was preserved and read; no retry overwrote it.
- `consistency-source-probe-v2.py` and `consistency-source-probe-output-v2.txt`: exact numbered source paragraphs, T38/W07X/W07XM/BUDPY/BUD/NOTES, relevant register rows and bibliography definitions; exit 0 with `-X utf8 -B -I`.
- `consistency-normalizer-probe-v3.py` and `consistency-normalizer-probe-output-v3.txt`: current selection source plus one fixture's nonsecret settings; exit 0. No regeneration or archived-version equivalence was established.
- `consistency-probe-run-log-v2.txt`: invocation failures/statuses, including `rg` unavailable on PATH. PowerShell/Python read-only fallback was used.

These probes independently check text/source scopes, not the numerical outcome counts handled by other R34 agents. No simulations, builds, installs, source edits or writes outside `codex-work/r34-ch4a-verify/` occurred. Files were created exclusively and prior outputs preserved. This v3 is the readable, G3-h1-corrected deliverable; retain v2 as the prior pass.