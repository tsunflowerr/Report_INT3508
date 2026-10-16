# R34 Ch4A v4 — consistency and rejection audit (v2)

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

| ID | Rejection verdict | Independent check and present scope |
|---|---|---|
| D11, explain random seed again | JUSTIFIED | Ch3:687–688 already defines `hạt giống ngẫu nhiên (số khởi tạo phần ngẫu nhiên)`; A95 says fixed at 7. Repeating a glossary explanation is optional. The suggested extra promise of rerun identity is not verified by a seed value alone. |
| D-c2, reconcile `s`/`giây` | JUSTIFIED | STYLE rule26 explicitly requires prose `giây`, table units `s`. A's convention follows that split. Unit abbreviations in table captions/headings are not English-method prose. |
| G1-r2, seed sensitivity / actual rerun evidence | JUSTIFIED to decline a claim of completed reruns; limitation remains | B11/T38:90 describes deterministic setup; L1a-04 (ADDENDUM-1:143) explicitly rereads stored transcripts, not a new simulation. T38:94 refers to replacements for failed jobs, not a completed-run equivalence experiment. No source in the opened evidence establishes a seed-sensitivity study. B476–478 retains rebuilt-runner equivalence as future work. Do not imply the seed study was done. |
| G1-t, add +31 = 0,84% of requests | JUSTIFIED | A243–245 already gives +31 and −5 and their underlying timely counts; A287–291 explains why +31 is a difference of totals. 31/3.672 is redundant, and reporting it does not alter the threshold-dependent result. |

## 3. Every partially declined item in log §6

| Partial decline | Verdict | Check |
|---|---|---|
| D4 / G1-d1 / G6-5: how 108 requests are selected | JUSTIFIED to omit an unverified source-version-specific method; missing-evidence claim should be qualified | B02/J18 establish 108 from a 10% daily sample, not the actual selection procedure. A61/A84 keeps that narrow claim. I additionally opened current `FleetPyManhattanNormalizer.cs`: NORM112–125 validates a target; NORM659–666 orders by a deterministic keyed rank; NORM750–755 keeps rows with both endpoints in the chosen node pool and takes the configured target. One fixture has target108 and max96nodes. Thus the method is not wholly unknowable, but this static one-fixture check does not prove current code matches every archived fixture. If adding a method, first establish that source-version link; do not describe 108 as a simple random sample. |
| D7: why disjoint windows overlap | JUSTIFIED | T38:93 says shared source and 3–20/108 row overlap; it does not establish the mechanism for a 17-hour window. Neither the draft nor rejection substitutes a fabricated mechanism. A68–70 preserves the dependence caveat. |
| D39: `họ trễ vì đường đông` | JUSTIFIED | REG K39:392 explicitly replaces a causal statement with no recorded dispatch update; A378–381 uses 72/76 with no dispatch update and says forecast targets the predictable part. Ledger accounting cannot identify sole cause. |
| D45 / CX6: rider was already on the vehicle | JUSTIFIED | W07XM6/11/16 reports promise history and x/c, but no waiting/onboard phase. W07X54 says `khách đang có`. A440–446 uses `một khách` and projected promises, preserving the evidence rather than the review's phase conjecture. |
| D46: insert examples of other structural constraints as established reason | JUSTIFIED | BUDPY29–44 partitions rejected requests by existence of a recorded budget-pruned candidate; the residual group is merely `else`. A449–455 correctly avoids treating no recorded block as proof of structural-only rejection. |
| D57 / G6-13: add 120-second conclusion to figure caption | JUSTIFIED | STYLE rule22 disallows a caption conclusion absent from the plotted quantity. The figure A611–679 plots late60, not timely120. A686–690 gives the threshold-dependent conclusion in prose. |
| D53 / G6-7: put morning means in pooled-count table | JUSTIFIED for the placement, PARTLY for reporting | OUTLINE §2 rule3 forbids cell means sharing a pooled-count block. A520–540 is a count table; separation is correct. But omitting the constituent counts for means left in prose is the CX7 owner-rule issue, not an authorized budget exception. |
| G6-6: separate notation box | JUSTIFIED | STYLE rule7 allows at most one remembrance box for the main conclusion, not a requirement to add a notation box. A113–116 defines arms in the caption and A179–183 defines a/p0/D0/c/z; Ch3 defines L/B. An optional box need not displace these definitions. |
| G4 / G6-1 / RQ1: full padding discussion in4.2 | JUSTIFIED | OUTLINE 4.8 assigns the full question to B. A248–250 supplies the crucial equality2.328 with a cross-reference; B217–334 gives same-promise-length, early-arrival, tail, individual-bound and scope comparisons. Core caveat is present. |
| CX7: constituent count pairs in appendix | NOT JUSTIFIED as an exception to owner counts | The3page appendix bound affects presentation, not whether each displayed rate has count/denominator information. Remove unqualified means or supply count pairs without exceeding the bound; see correction2. |
| RQ2: analyze76→10 inA | JUSTIFIED as allocation; handoff implemented | A579 reports10 on all34 scenarios and explicitly labels replay/weekday coverage at A557–559. B79–82 analyzes68→2 in the21weekday subgroup; B246 reports10 in all34. The8weekend late riders are unchanged, so76−68=10−2=8. No lost forecast interpretation. |

## 4. Remaining M rows: exhaustive completeness check

Together this section and §3 cover **all39 M rows** listed in log§5, including editorial modifications that have no separate declined clause in log§6.

| IDs | Verdict | v4 location / reason |
|---|---|---|
| CX6 | JUSTIFIED | See§3; A440–446. |
| CX7 | PARTLY / correction required | Numeric ledger-share and fixed-set counts supplied (A400–418, A482–501); per-scenario count refusal inadequate. |
| CX9, CX15 | PARTLY / correction required | Date inventory supplied A148, generator anchor corrected A101, register corrections documented; calibration wording still broad atA108. |
| FC#75, D33 | JUSTIFIED editorial omission | Common-rider wait/ride sentence removed entirely, so no unlabelled mean survives. A287–291 retains distinct served cohorts and +31 caveat. |
| FC K-6 | PARTLY / assembly pending | Local author cannot manufacture external contents. Missing-label/citation dependencies are honestly noted; they still need actual assembly fixes before a complete thesis. See§1.5. |
| D1, D2 | JUSTIFIED | A15–20,31–43 explain padding, retain three accounting parts rather than three causes, and use corrected forced name. |
| D4–D7 | JUSTIFIED with evidence scope | A60–70 fixes day-level sample wording and terminology, avoids untested rerun equivalence and overlap mechanism; details§3. D5's1.2example already exists inCh3 terminology table, so omitting duplication is editorial. |
| D13, D14 | JUSTIFIED | A113–116 defines arms; A127–145 fixes morning run count, snow request count and runner distinctions. Renaming the column / a separate prose list is optional. |
| D17 | JUSTIFIED | A157–159 cross-references the threshold reversal whose exact+31/−5 is atA244–245. |
| D24 | JUSTIFIED | A201–205 uses glossary `Khách bị phá lời hứa` and defines what each law promises. |
| D25 | JUSTIFIED | A223–227 defines static time, gives ref dependency, and omits an unregistered20scenario count. The outline alone is insufficient numeric evidence. |
| D30, G6-3 | JUSTIFIED | A270–274 fills measured79/74 and timely counts; only uncounted sharing cells remain `chưa đếm`. A337–339 interprets V with the accounting inequality rather than a causal claim. |
| D35 | PARTLY concerning theorem scope | Ch3 theorem has0≤L≤B and(N). A327–331 cites(N) but gives abbreviated c=0argument; parent/root is checking the separate no-op-scope requirement. Declining a new duplicate40second example is justified because Ch3 already has it. |
| D39, D45, D46, D53, D57, D62 | JUSTIFIED except denominator issue | See§3 for first five. D62: A751–756 identifies fixed and synthetic scope; the old sweep is used to delimit the audit, not as a fifth outcome set, so no extra outcome-table row is needed. |
| RQ1, RQ2 | JUSTIFIED | See§3. |
| G1-d1, G1-d3 | JUSTIFIED | G1-d1 selection scope above; G1-d3 outcome-vs-audit scope stated A148–150 and A736–740. CalibrationA108is the exception needing correction. |
| G3-h1 | JUSTIFIED | A451–455 says116of148without claiming all116would be lost because of the cap, then explains what the record does not prove. A458–461 adds the explicit counterfactual caveat for59. |
| G4, G6-1, G6-3, G6-5, G6-6, G6-7, G6-8, G6-13 | JUSTIFIED except identified issues | Full-padding handoff / V interpretation / bounded selection / no optional box / separate means / no invented1mscause / figure-caption discipline all checked above. G6-5dwell0is carried toB449–451. G6-8 overshoot explanation is corrected A457–462;1mscause remains explicitly unverified atA428 andC4A-19. |

D42/RQ4 are CC rather than M/R. Keeping33moved riders while specifying29late shifts and4early shifts of1ms atA426–428 is consistent with the stated `c != 0` definition; changing33to29would silently change the cohort. No verified rounding cause was added.

## 5. A/B numerical differences: same values, different cohorts, or actual conflict

The comparison below exhausts the differing quantities in repeated A/B topics, not every unrelated literal in the files (software version digits, TikZ coordinates and entirely B-only estimates are not paired claims). Shared same-cohort table entries agree. No outcome number correction is indicated solely by this comparison.

| Repeated topic | A vs B | Classification |
|---|---|---|
| C-30late60withoutforecast | A268:76of2.338on34; B79–80:68of1.471on21weekdays | DIFFERENT COHORT.8weekend late riders. |
| C-30late60withforecast | A578:10of2.338on34; B79–80:2of1.471on21 | DIFFERENT COHORT.8weekend riders unchanged. B246 repeats10exactly. |
| C-30late60meanweekday | A pooled counts, plus14.6%mean at30second threshold A344–345; B81:6.01%→0.17%means at60second threshold | DIFFERENT THRESHOLD/COHORT/AGGREGATION, not contradiction. Never reuse14.6as the weekday60smean. |
| Raw vs forecast early60counts | A571raw7/3/1; A578forecast8/4/2; B296–298forecast8/4/2 | DIFFERENT PROMISE where raw-vs-forecast; identical forecast counts. |
| C-30early60weekdaymean | A raw3or forecast4all34; B107weekday raw0%, forecast0.08%mean21 | DIFFERENT COHORT/AGGREGATION.4totalforecast early are not the numerator of0.08%weekdaymean. |
| Forecast promise extension | A582 U/C30/C1207.18/7.37/7.27s pooled allserved34; B129–132 C30drop13.7s, morning27.8s, pickup3.2s means21 | DIFFERENT COHORT/AGGREGATION and pickup/dropdimension. B130–132 explicitly explains7.37. |
| Padding extension rounding | A5827.37/7.18; B22037.2instead of7.4; B245–252exact7.18/7.37/7.27/37.18/37.37 | ROUNDING plus padding amount;7.37+30=37.37 and7.18+30=37.18. No numeric conflict. |
| C-30ledger late cohort | A403:82/6.892s (76late riders all34); B155–156:82/6.217s (68late weekdays21) | DIFFERENT COHORT. Same rounded dispatch numerator can recur because remaining8late riders have no dispatch share. A418precise81.742/6,891.526; B182precise81.7/6,217.4. |
| C-30ledger percentage | A4171.2%; B1551.3% | DIFFERENT COHORT/denominator above, not changed ledger definition. |
| Dispatch sum vs dispatch displacement | A401–403signedsumforlatecohort; A411–414absolute cumulative perrider; B174–180ledger signedshare andB312–315maxcumulative bound | DIFFERENT METRIC. Do not replace signedqwithsumabs(c). |
| Snow requests/served/late | A134864requests; A436601served; B339601served,41→34late | DIFFERENT UNITS/REPLAY, same snow set.864is not a disagreement with601. |
| Snow max vs global C30max | A435–437snow25.2s; A393/B313main29.2s; B315extends cap-validity claim to snow | DIFFERENT COHORT. B's29.2global bound remains true, but exact snow max is25.2, not29.2. |
| Fixed FREEserved vs MLheldoutFREE | A4921.629servedall16fixedscenarios; B210807MLtestcustomers | DIFFERENT COHORT. Bdescribes days excluded from training atB199–200; do not use807as fullfixedservedtotal. |
| M30forceddecision mean | A31541.3%mean34; B31941.3%mean34 | AGREES numerically; old term inBneeds correction. |
| M30pooledforced vs mean | A3347.710/20.103=38.4%; B31941.3%mean34 | DIFFERENT AGGREGATION; do not force38.4and41.3to agree. |
| M30forecast-inside-dispatcher forced | A31541.3%full34; B188–18947.6%withforecastvs62.8%withoutmean15completedsubset | DIFFERENT EXPERIMENT/COHORT. Bnot a replacement of the34scenario replay result. |
| M30brokenpromise | A31514.5%mean34; B19039.0%→11.0%mean8morningforecast-inside-dispatcher | DIFFERENT COHORT/EXPERIMENT. |
| Forced counts C30/C120 | A600C1200/20.435; B393–394C300/20.101andC1200/20.435; A329U0/20.760 | AGREES; three denominator values belong to different arms. |
| Rideridentitycounts | A2882.207commonU/C30plus227/131private; A6032.266commonC30/C120plus121/72private; B4147.159servedrecords | DIFFERENT UNITS.7.159=2.434+2.338+2.387 arm-records, not7.159unique people acrossarms. |
| Run/repair scope | A129136of192morningarchivedruns; A72364Cmorningruns; A736132/140Ccap-auditruns; B415382.006repairrecords(in185runs,Ch3) | DIFFERENT COHORT/UNIT. Theactual conflict is A108's broadunused-calibrationscope, not these numbers. |
| Morning forced ladder | A546–54758.6→6.6→1.7; Bnone | A-only, noBcontradiction. W07Xhas intermediate6.8at150;Adoesnot claimfullmonotonicity. Missing constituent counts remain correction2. |
| Raw C120 timely120 vs padded Uforecast timely120 | A570/A5742.366forC120withoutforecast; B2512.366forUforecast+30padding | COINCIDENTAL EQUAL VALUE, not identical configuration. A/Bcrossrefs don't switchtheseconfigurations. |
| Main-set 120second selection disclosure | A229–233mainsetresults/screensviewed; B460developmentdataonly | REAL SCOPE CONFLICT; correction3. |

Common same-cohort facts repeated in B and agreeing with A:34scenarios/3.672requests;2.434/2.338/2.387served;137/10/65late60underforecast;2.297/2.328/2.322timely60;2.347/2.338/2.379timely120;8/4/2early60forecast;7.18/7.37/7.27sextension;−96served/−242sharing;590.1/29.2/118.9smaxdispatch;C30/C1200forcedcounts;M30mean41.3and28/34broken-scenarios;601snowserved. Bonly selector-cost, confidence-interval, ML, nowcast and software-test figures have no corresponding claiminAto disagreewith.

## 6. Terms and cross-reference status

| Term | A | B | Assessment |
|---|---|---|---|
| Forced event | `quyết định bị ép`, explicitdefinitionA196–200 | `phải phục hồi`at188/319/393 | REAL terminology mismatch; correction4. |
| Aggregation | `trung bình theo kịch bản`, `gộp theo khách` | same, with explicit forecast-extension distinction | Consistent definitions; percentage count omissions discussed separately. |
| Replay | all displayed promises recomputed, scheduleunchangedA172–175 | same atB84–89/229–233; separateforecast-inside-dispatcher experimentB185–192 | Consistent; different experiments properly separated. |
| Measured traffic | `hệ số tắc đường đo được` | same in validity; `hệ số thật`in future-information replay | Different informationtime, not inconsistent deterministicworldlabel. |
| Ledger | `phần tính cho điều phối`, `phần được hồ sơ lịch sử giải thích`, `phần còn lại` | same figurelegend/caption | No causal ledger split or lost residual caveat found. |
| Promise failure | `khách bị phá lời hứa`, law-specificdefinition | same wording | Consistent; its threshold/promise changes bylaw/experiment. |
| Uncapped/FREE | separatearmdefinitionsA113–116,142–145; FreechangesselectorandvalidatorA507–511 | separatesuncappedandFreeML / fixedscreen | Consistent, not an all-effects-cap-only claim. |
| Bound | `trần`, `phần trần đã dùng` | `trần`, metaphor`núm vặn`B323 | No factual mismatch; metaphor is optional stylecleanup. |
| calibration | narrowerintendedunusedprocedurebutbroadA108phrase | B415citesrepairauditincluding15runs | Needs clearer scope; correction1. |

All A→Blabels (`muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet`, `muc:c4-hople`) resolveinB-v7. All B→Atable labels resolve. Ch3labelsAuses resolve. Thethreeunresolvedexternallabels arelistedabove.

Bibliography staticcheck of `.tex`definitions: currentthesis has `schulz2026`at`10-tai-lieu.tex:116`; no `engelhardt2026`or`horl2022`bibitem wasfoundinthe scanned top-leveldraft/currentthesistexfiles. This is a bibliographyassembly dependency, not evidence that the papers lack registered metadata. `engelhardt2026`is already called out bylogFC K6/A-NOTES66–67. No build wasrun.

## 7. Saved probes and execution notes

- `consistency-audit.py` and `consistency-audit-output.txt`: label/references, forbiddenterm, numberedcohort/rate/log/style scan. Firstshellattempt failed because ordinary`python`is absent. Reinvoking with pinnedinterpreter generatedtheUTF8output; exit1came onlyafterwritingit because printingVietnamese throughcp1252failed. The writtenoutputiscomplete. Nooverwrite/retry againsttheexistingoutput.
- `consistency-source-probe-v2.py` and `consistency-source-probe-output-v2.txt`: exact numberedsourceparagraphs, T38/W07X/W07XM/BUDPY/BUD/NOTES, relevantregisterrows, bibliographydefinitions; exit0with`-X utf8 -B -I`.
- `consistency-normalizer-probe-v3.py` and `consistency-normalizer-probe-output-v3.txt`: currentnormalizerselection plusonefixture's nonsecret selectionsettings; exit0. No regeneration/version-equivalenceclaim.
- `consistency-probe-run-log-v2.txt`: invocationfailuresandfinalstatuses, includingattempted`rg`whichisnotonPATH.

No simulations, builds, installs, source edits orwritesoutside`codex-work/r34-ch4a-verify/`wereperformed. Files werecreatedexclusively; priorfileswerepreserved.