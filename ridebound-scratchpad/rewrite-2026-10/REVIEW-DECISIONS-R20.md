# REVIEW-DECISIONS-R20 — consolidating the three reviews of the thesis outline (2026-10-11)

**Role.** Outline consolidator. I checked every substantive comment of the three R20 reviews against the evidence (a
comment is not true because a model wrote it), decided ACCEPT / REJECT / MODIFY, and wrote `OUTLINE-V2.md` next to this
file. No reviewer gets credit for its model name.

**What I read.** The outline under review (O, 605 lines, in full); Codex `R20-OUTLINE-REVIEW-CODEX.md` (CXR, 337 lines,
in full); Claude lecturer `R20-LECTURER-REVIEW-CLAUDE.md` (LRR, 671 lines, in full); Antigravity `R20-ANTIGRAVITY.md`
(AGR, 219 lines, in full); the evidence register (REG, 471 lines, in full); STYLE-GUIDE-VI, GLOSSARY-VI, R19-SKILLS-REVIEW
(in full); R18-CONFIRM-CODEX (in full); R17-FINAL-VERDICT §0–A2; and, for the checks, the raw files cited per row. Stage 1a
results (new input from the coordinator): Claude `R21-STAGE1A-CLAUDE.md` §0–1 and its report (STG, 86 lines, in full) and
witness check (CW21); Codex `R21B-STAGE1A-CODEX.md` (CXS) at the cited lines.

**What I ran.** Read-only shell commands only: `sed`, `grep`, `cat -n`, `wc`, `ls`, `find`, and `pdftotext` on
`main.pdf` and the DACN PDF (printed to the terminal). No simulation, build, install, deletion, or write except this file
and `OUTLINE-V2.md` (plus throw-away word counts in the session scratchpad).

**Check labels.** TRUE = the opened anchor supports the comment; FALSE = the anchor contradicts it; PARTLY = part true,
part wrong or missing a condition; OPINION = editorial judgement, no fact to check (I still say whether evidence bears on
it). **Decision** = ACCEPT (adopt as written), MODIFY (adopt with a change), REJECT (do not adopt).

## Anchor keys

Paths relative to `E:/Code/Report_INT3508/ridebound-scratchpad/` unless absolute. `DEB` = `optimize/codex-debate/`.
REG row IDs (A01…K52) refer to `rewrite-2026-10/evidence/EVIDENCE-REGISTER.md`; each row carries its own raw anchor.

| Key | File |
|---|---|
| O | `rewrite-2026-10/OUTLINE-PROPOSAL-CLAUDE.md` |
| CXR / LRR / AGR | `DEB/codex-work/R20-OUTLINE-REVIEW-CODEX.md` / `rewrite-2026-10/reviews/R20-LECTURER-REVIEW-CLAUDE.md` / `DEB/antigravity-work/R20-ANTIGRAVITY.md` |
| REG | `rewrite-2026-10/evidence/EVIDENCE-REGISTER.md` |
| A | `DEB/codex-work/R15-audit-summary.txt` (Codex reconstruction of 227 transcripts) |
| BUC | `DEB/claude-work/budget-use-check-2026-10-09.txt` |
| STG / CW21 / CXS | `DEB/claude-work/r21-stage1a/stage1a-report-2026-10-10.txt` / `DEB/claude-work/r21-stage1a/cum-witness-check-2026-10-10.txt` / `DEB/codex-work/R21B-STAGE1A-CODEX.md` |
| T38A | `tang3/t38/analysis-2026-10-02-report.txt` |
| CON | `optimize/report-extras/constraints-and-pooling-2026-10-06.txt` |
| FFA | `optimize/forecast_family_a.py` |
| EXAMPLE | `optimize/report-extras/example-rider-2026-10-06.txt` |
| CFG30 | `tang3/configs/C-30.json` |
| BE / DELTA | `C:/Code/RideBound-noworse/src/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs` / `C:/Code/RideBound-noworse/src/RideBound.Application/Promises/PromiseDeltaCalculator.cs` |
| TEX | `E:/Code/Report_INT3508/ridebound/noi-dung/` (read only) |
| PDF | `E:/Code/Report_INT3508/ridebound/main.pdf` (read with `pdftotext`) |
| DACN | `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf` (read with `pdftotext`) |
| R19C | `DEB/ROUND19-CLAUDE.md` |
| R18 / R17 | `DEB/codex-work/R18-CONFIRM-CODEX.md` / `DEB/claude-work/R17-FINAL-VERDICT.md` |
| HO | `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md` |
| STYLE / GLOS | `rewrite-2026-10/style/STYLE-GUIDE-VI.md` / `rewrite-2026-10/style/GLOSSARY-VI.md` |

---

## 1. Counts

| Reviewer | Rows | ACCEPT | MODIFY | REJECT | TRUE | PARTLY | FALSE | OPINION |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Codex (CX) | 75 | 63 | 11 | 1 | 54 | 7 | 0 | 14 |
| Claude lecturer (LR) | 55 | 37 | 18 | 0 | 26 | 9 | 0 | 20 |
| Antigravity (AG) | 29 | 9 | 8 | 12 | 5 | 7 | 6 | 11 |

(The lecturer's c ≥ 0 argument is counted inside LR-04 as PARTLY, because its observation about cumulative records is
true while its two-sided reasoning is false; see LR-04.) Counts were made by `grep` over the decision column after writing.

---

## 2. Codex (CXR)

| ID | CXR line | Comment (short) | Check | Decision | Change to the outline |
|---|---|---|---|---|---|
| CX-01 | 58 | Sentence 1c "tổng ≤ B, phương án vi phạm bị loại" needs conditions; not a feasibility guarantee | PARTLY. The mechanism is as stated: BE:41-104 rejects when before + delta > hardLimit in an applicable phase. Keep-route has c = 0 (REG A22), C-30 had 0 forced decisions in 49 runs (REG A21), C-120 0 forced (STG:44), 0 overshoots (BUC:37; STG:38-39). The missing part is the condition (N) and "not a guarantee that a plan exists" | MODIFY | Contribution keeps "nếu vượt, phương án bị loại"; Nhận xét 3.1 in §3.3 states (N) and the non-guarantee |
| CX-02 | 60 | "Mọi khách từ lúc đặt" wrong scope → accepted riders, from the first promise | TRUE. CFG30:17-23 phases accepted/waitingPickup/onboard; BE:107-114; REG A13 | ACCEPT | "với mỗi khách đã được nhận" |
| CX-03 | 61 | "Không phụ thuộc phần tắc đường" wrong: c is computed under current travel times | PARTLY. c uses current travel times (REG A02); what is traffic-independent is the cap B, unlike HZ's traffic-dependent relaxation (REG J05) | MODIFY | Write "phần x không cộng vào trần; mức trần không nới theo tắc đường" |
| CX-04 | 64 | "Tắc đường đoán trước được" → "phần được hồ sơ lịch sử giải thích" | TRUE. FFA:134 computes it as D₀ − p₀, i.e. the forecast stretch; REG F09 note | ACCEPT | Glossary of the three ledger parts changed |
| CX-05 | 65 | No source for the "precedent" of the three-part ledger | TRUE. O:486 anchors FR and D03 only; forecast precedent exists (REG J21, J35), ledger precedent is not shown | ACCEPT | Neither claim precedent nor novelty for the ledger |
| CX-06 | 66 | 34 cells are not 34 independent days | TRUE. REG B11, I05 | ACCEPT | §1.5, §4.1, §4.11 |
| CX-07 | 68 | M⁺ is a comparator run on RideBound, not a reproduction of Schulz–Pfeiffer (900 s) | TRUE. REG J10, J11 | ACCEPT | Fairness note in §4.2; Bảng 3.3 |
| CX-08 | 70 | Different served sets; Δtimely = Δserved − Δlate; not "127 riders saved" | TRUE. REG C04, C08; R18:243-247 | ACCEPT | Reading rule under Bảng 4.4 |
| CX-09 | 71 | C/M⁺ naive late60 76 vs 74; not "cùng mọi khách" | TRUE. A:7-8 | ACCEPT | Box and §4.2 |
| CX-10 | 72 | 41,3% is a cell mean of forced decisions; define "forced" | TRUE. T38:58; T38A:73 ("means over cells") | ACCEPT | Cell-mean block separate (Bảng 4.5) |
| CX-11 | 75 | 37,2 / 7,4 s are pooled per rider on 34 cells; do not mix with 13,7 s of 21 cells | TRUE. A:7,9 ext_sum_ms / served = 7.367 / 37.183 s; REG F06 | ACCEPT | §4.7 vs §4.8 kept apart |
| CX-12 | 76 | Early60 0,17% lacks denominator and collides with the 0,17% late cell mean | TRUE. O:474; REG K24 | ACCEPT | Write "4/2.338" |
| CX-13 | 77 | "Toàn bộ 98 lần chạy có áp luật C" → 98 measured-traffic runs (34 + 64) | TRUE. REG E01 | ACCEPT | Scope fixed; Stage 1a adds 34 C-120 runs (§4.5) |
| CX-14 | 78 | 1.256 are candidate records, not riders; B varies 30–300 s | TRUE. REG D16, K09 | ACCEPT | §4.5 wording |
| CX-15 | 79 | Fail-fast validator: no record does not mean every failure was seen | TRUE. REG A23, I08 | ACCEPT | §4.5, §4.11 |
| CX-16 | 81 | Delete sentence 8; Stage 1a incomplete (27/33 summaries) | PARTLY, now superseded. My `ls` found 34/34 `summary.json`; two independent analyses now agree (STG:4-23; CXS:3) | MODIFY | No Stage 1a sentence in the 10-number paragraph; Stage 1a goes into §4.4 slot and the §1.4 result list, from STG/CXS only |
| CX-17 | 87 | Anchor keys unclear (FP is not a line range of R17; BE path missing) | TRUE. O:484 "R17 FP:31-33"; FP = `ROUND16-FACT-PACK.md` (R17:26) | ACCEPT | V2 cites REG IDs only, plus N-rows with full paths |
| CX-18 | 88 | HZ anchor must include eqs. 9–10 (575–588) | TRUE. REG J03 | ACCEPT | §1.3, §2.3 |
| CX-19 | 89 | Ledger needs its code anchor | TRUE. FFA:91 (dispatch = Σ(p − e)), FFA:133-136 | ACCEPT | §3.6 evidence |
| CX-20 | 90-93 | Anchors for sentences 4–7 incomplete (A:8, T38:111, R15:87) | TRUE | ACCEPT | Side table of the new paragraph |
| CX-21 | 100-112 | Replacement paragraphs (1)–(7) | OPINION; every number re-checked against A:7-9 and is right | MODIFY | Scoping adopted; length cut to 321 tiếng (about 7% over ~300), 10 distinct numbers |
| CX-22 | 114 | Chapter 1 states three ideas; full numbers in ch. 4 | OPINION | ACCEPT | §1.4 |
| CX-23 | 119 | Box: HZ "việc tách phần tắc đường" can read as causal decomposition | PARTLY. HZ recompute the old route under current traffic (REG J01); REG K03 calls this "tách", Codex warns it is not a causal ledger | MODIFY | Box: "giờ trả cập nhật theo tắc đường trên tuyến cũ, và nới hạn trả dựa trên mốc đó" |
| CX-24 | 134, 185, 245 | ML: "không giúp thêm" too general; FREE early is 7,1% not 6,9%; anchor ML:45-64 lacks the table | TRUE. REG G07 (ML:21; CHK:211-212); O:360 has 6,9% | ACCEPT | §4.7 ML part |
| CX-25 | 138 | Short box text | OPINION | MODIFY | Merged with LR-25 two-column table |
| CX-26 | 150 | Do not call the three accounting parts "three causes"; drop rule O:277 | TRUE. The third part is a residual (FFA:135); REG F09 note | ACCEPT | §1.2 "Ba phần…", rule removed |
| CX-27 | 152-158 | Three research questions with "không suy ra" | OPINION | ACCEPT | End of §1.2; Bảng 4.0 |
| CX-28 | 166 | Example rider is a simulated record; give raw seconds | TRUE. EXAMPLE:1-4,60 | ACCEPT | H1.1 caption |
| CX-29 | 167 | 86,1% / 92,5% belong in ch. 4 (selected populations, HIST-dependent) | TRUE. FR:72-75 (C-30, riders late > 60 s, 21 cells); SNOW:10 | ACCEPT | Ch. 1 uses U numbers instead (REG C21, C24) |
| CX-30 | 168 | One short positioning table in ch. 1; ch. 2 explains | OPINION (same as LR-43) | ACCEPT | Bảng 1.1 short, Bảng 2.2 full |
| CX-31 | 169 | Separate theory from implementation; physical limits are test configuration | TRUE. REG B03 | ACCEPT | Bảng 2.1 caption |
| CX-32 | 170 | +0,5 page for the forecast definition (data availability, weekends) | TRUE. REG F01, F02 | ACCEPT | §2.4 = 1 p; §3.5 = 1,25 p |
| CX-33 | 171 | Keep the keep-route remark, (N) and two counterexamples | OPINION, consistent with owner default | ACCEPT | §3.3 |
| CX-34 | 172 | Rule table needs test set, phases, locks, objective order, recovery | TRUE. REG A07, A08, A14, A17-A19 | MODIFY | Bảng 3.3 with six columns (STYLE rule 20); selector order in text |
| CX-35 | 173 | Objective order has activation conditions | TRUE. REG A14 (SEL:276-280) | ACCEPT | §3.4 |
| CX-36 | 174, 198-206 | Ledger formula: q = Σc signed ≠ Σ\|c\|; p₀ vs D₀; closing term ρ | TRUE. FFA:91,133-136 | ACCEPT | §3.6 formula |
| CX-37 | 175 | Drop line counts; state generator scope | TRUE. TEX/07-chuong3.tex:699 vs 711-717 | ACCEPT | §3.7 |
| CX-38 | 176 | Split pooled and cell-mean blocks; missing ≠ 0 | TRUE. STYLE rule 20; R19 rule 33 | ACCEPT | Bảng 4.4 / 4.5 |
| CX-39 | 177 | Drop the "lượt phải bồi thường" column | PARTLY. REG C28 permits a hypothetical contract with symbolic money; real guarantees found are pickup or driver-side (REG J29, J30) | MODIFY | Column renamed "lượt trễ quá T trên 100 yêu cầu"; one hypothetical sentence only in §4.11 |
| CX-40 | 178 | Keep the 148 diagnosis with record limits | TRUE. REG D13, D14, K10, K11 | ACCEPT | §4.3 |
| CX-41 | 179 | WP14r and w07 dials are separate; no monotone claim; U not an upper bound | TRUE. REG D01 (C-120 666 > U 665), K12; on 34 cells C-120 timely120 2.366 > U 2.332 (STG:29) | ACCEPT | §4.4 |
| CX-42 | 180 | Keep the negative cumulative result with fixed-traffic and synthetic traces | TRUE. REG E03, E04 | ACCEPT | §4.5, plus the 3 new Stage 1a records (STG:44-47) |
| CX-43 | 181 | Retitle §4.6; two state populations; 35,54 s is over two riders | TRUE. REG H04, H06, K16, K17 | ACCEPT | §4.6 title and text |
| CX-44 | 182 | Separate 21-cell results from 34-cell results | TRUE. REG F04, F06 | ACCEPT | §4.7 |
| CX-45 | 183, 243 | Family B: 3/32 stopped; 47,6% over 15 completed M⁺ cells; not refuted for every implementation | TRUE. REG F12 | ACCEPT | §4.7 Family B paragraph |
| CX-46 | 184 | Snow: undelivered prefix, post-hoc threshold, exact anchor | TRUE. REG F14, K20, K21 | ACCEPT | §4.9 |
| CX-47 | 186 | Validity: report counters, generator bounded, one omitted request per arm | TRUE. A:7-9 `omitted_requests` 1, `work_exhausted` 0, `omitted_by_cap` 0; REG A24 | ACCEPT | §4.10 |
| CX-48 | 187 | 0,54 vs ≈ 1,33 not same conditions; limitations once | TRUE. REG B12 note | ACCEPT | §4.11, §5.2 |
| CX-49 | 188 | §5.3 to ~1 page; drop 80–140 h | TRUE. REG F19 is UNVERIFIED | ACCEPT | §5.3 |
| CX-50 | 189 | Appendix A needs re-anchoring; 49% is of all served riders | TRUE. TEX/08-chuong4.tex:1728 "774 (49,0%)", 08:160 "1.581" served; 774/1.581 = 48,96%; O:382 says "revised riders" | ACCEPT | Appx A conditional, denominator fixed |
| CX-51 | 190 | Appendix B 1,5 p cannot hold theorem + corollaries + six CEs; shrink | OPINION | ACCEPT | Appx B ≤ 1 p |
| CX-52 | 194 | Keep-route remark: 0 ≤ L ≤ B, option generated, non-budget checks pass; HZ variant shares it | TRUE. TEX/07-chuong3.tex:193-203,292-297; REG A22 | ACCEPT | Nhận xét 3.1 text |
| CX-53 | 196 | Comparator identities need v_t = p_{t−1}, a continuous chain and closing | TRUE. REG A12 (SPEC:50,62-63) | ACCEPT | §3.4 |
| CX-54 | 208 | c ≥ 0 is not general; keep the absolute value | TRUE. Net earlier dispatch change for 2 of 174 exposed U riders and 4 of 33 C-30 riders (BUC:34,37), 3 of 103 C-120 riders (STG:39); DELTA:139,259-262 charges \|p − e\| | ACCEPT | §3.2; also corrects O:140 ("needed to explain c ≥ 0") |
| CX-55 | 212, 230 | "70 p without appendix" is not a floor; table heights and ±2 pp are guesses | TRUE (they are layout estimates) | ACCEPT | V2 labels budgets as estimates |
| CX-56 | 216-228 | Budget 73 p: front 9, ch. 2 6,5, ch. 3 12,5, ch. 5 3, appendix 4 | PARTLY. Owner default keeps the English cover and Abstract (front 10) and caps the appendix at 3 p | MODIFY | 73 p: front 10, ch. 3 13, appendix 3 |
| CX-57 | 238 | E1: `exposure-check` path wrong | PARTLY. The file exists at `DEB/` root (`ls`); O:392 lists it ambiguously after a comma | ACCEPT | REG ID EXP used |
| CX-58 | 239 | E2: forecast inactive on 12–13/11; M⁺ forced source is W07X, not CAP | TRUE. REG D02 (CAP:2), D04 | ACCEPT | §4.4 notes |
| CX-59 | 240 | E3: LAD is rounded; use integer counts | TRUE. REG D09 (WP17 integers) | ACCEPT | Bảng 4.9a from D09 |
| CX-60 | 244 | E7: 886,858 s is not in RP:5-25 | TRUE. REG F15 anchors NEW:5 | ACCEPT | §4.9 |
| CX-61 | 246 | E9: three cost statistics need definitions | TRUE. REG H05, K15 | ACCEPT | §4.6 |
| CX-62 | 247, 249, 252 | Plan ≠ result; September numbers not re-verified; hashes ≠ representativeness | TRUE. O:594 says the static numbers were not re-audited | ACCEPT | Appx A conditional; §4.10 wording |
| CX-63 | 248 | E11: Stage 1b does not need new owner approval | TRUE. R19C:3-5 "The owner approved both steps … Stage 1b cost-first 2×2 next" | ACCEPT | Slot rules: Gate 0 + completion only |
| CX-64 | 250-251 | E13 is record-based; 0,535 includes idle vehicles | TRUE. REG D13, B12 | ACCEPT | §4.3, §4.11 |
| CX-65 | 256-259 | Four general fixes: keys, per-table metadata line, ch. 2 primary sources, verified vs old vs missing | OPINION | ACCEPT | V2 §2 writer rules 9–10 |
| CX-66 | 263-310 | 40 LaTeX inventory checks; LoT starts xii not xi | TRUE. Spot-checked #35 (above), #40 (R18 B2), LoT: PDF p. 8 shows "Danh sách bảng … xii" | ACCEPT | Inventory fixes noted |
| CX-67 | 271, 294 | "Hơn năm trăm" is a lower bound; "chín dự án" vs seven rows is unclear, not proven wrong | TRUE (logic) | ACCEPT | Drop both phrasings as unhelpful, not as false |
| CX-68 | 320 | Drop the English cover and Abstract | OPINION. Owner default keeps them; DACN has an English cover and Abstract (DACN PDF 3, 6) | REJECT | Keep both |
| CX-69 | 321 | Title "Kiểm soát độ dời lời hứa giờ trả trong điều phối xe đi chung" | OPINION | MODIFY | Basis of title option 2 |
| CX-70 | 324 | Descriptive rule names | OPINION | MODIFY | Owner-default names in prose; Codex's descriptions in Bảng 3.3 |
| CX-71 | 325 | Count runs as arm × cell × repetition actually used | OPINION | ACCEPT | Appx C |
| CX-72 | 326 | One "late > 1 min" statistic: pooled integer counts; cell means apart | TRUE. Two U figures exist: 8,34% pooled (REG C06) and 9,10% cell mean (REG C27) | ACCEPT | Bảng 4.3 rule |
| CX-73 | 327 | Leave out the γ margin | OPINION | ACCEPT | Not in V2 |
| CX-74 | 318-319 | Theorem option (b); supervisor stays unknown | OPINION, = owner default | ACCEPT | Front matter, §3.3 |
| CX-75 | 329-335 | Five mandatory changes | TRUE (each checked above: CX-01/02/03, CX-26/36, CX-11/13/24/50, CX-17/62/63, CX-56) | ACCEPT | All five applied |

---

## 3. Claude lecturer (LRR)

| ID | LRR line | Comment (short) | Check | Decision | Change to the outline |
|---|---|---|---|---|---|
| LR-01 | 39 | A 5-line plain Vietnamese summary without internal codes | OPINION | ACCEPT | V2 §0 |
| LR-02 | 40-46, 133-147 | Contribution ≈ 558 tiếng, ≈ 30 numbers, symbols before definition, "chiến lược B" next to budget B, cell means mixed, 0,17% without denominator | TRUE. `wc -w` on O:452-478 = 558; 42 numeric tokens incl. 8 sentence labels and 3 years ≈ 31 | ACCEPT | New paragraph: 321 tiếng (about 7% over ~300), 10 distinct numbers, no symbols |
| LR-03 | 47, 288-302 | Strongest question: why C if forecast + 30 s padding ties at 60 s and wins at 120 s | TRUE. The outline has the numbers (O:353, 472-474) but no argument | ACCEPT | New §4.8 and the answer in §8 below |
| LR-04 | 48, 304-315 | "Cộng dồn" and "hai chiều" never acted on the data; insertion-only generator ⇒ c ≥ 0; drop both from the differences | PARTLY. Cumulative: true for the 98 earlier measured-traffic runs (REG E01), but traces exist on fixed traffic (REG E03), synthetic (REG E04) and now 3 records under C-120 on the 34 cells (STG:44-47; CW21:2-7). Two-sided: the reasoning is FALSE. Net earlier dispatch changes occurred: 4 of 33 C-30 riders, 2 of 174 U riders (BUC:34,37), 3 of 103 C-120 riders (STG:39); the code charges \|p − e\| (DELTA:139,259-262); TEX/07-chuong3.tex:730-731 ("decisionMovedEarlier = 0") is a static-panel statement. Magnitude for C-30 is small: A:7 `S_sum_exposed_ms` 359.173 and the signed mean rounding to the same 10,9 s (BUC:37, one nonzero change per rider) imply the four earlier changes total ≤ ≈ 0,56 s (derived, recount before use) | MODIFY | Keep both in the definition; do not sell either as an empirically active difference; report the counts in §3.2 and §4.5 |
| LR-05 | 49-52, 317-328 | Fairness: deadline rule at 30 s is 30× tighter than S&P's 15 min; HZ not implemented; show forced share vs B in the body | TRUE. REG J10 (l = 900 s), J11, D04, K27 | ACCEPT | Fairness note opens §4.2; forced-vs-B row in Bảng 4.9b; HZ variant in §5.3 |
| LR-06 | 53-57, 350-360 | Robustness: day × window table; lateness on the 2.207 common riders | PARTLY. Per-cell data exist (R18 NEW:4 re-derived per-cell signs from R15-audit.json; REG C30). Common-rider lateness is not in REG (REG C05 has wait/ride only) and is a post-treatment population (R18:247) | MODIFY | Bảng 4.7 per day × window via a new read-only script (fallback REG C30 sign counts); common-rider lateness optional, labelled post-treatment |
| LR-07 | 60-64, 483-506 | Missing problem statement (inputs, decisions, outputs) | TRUE. O §2.5 has no such item | ACCEPT | §3.1.1 (0,5 p) |
| LR-08 | 487-490 | Missing insertion figure; make H3.2 mandatory | TRUE | ACCEPT | H3.2 mandatory |
| LR-09 | 491-494 | Missing full decision-cycle pseudocode; a few lines on recovery | TRUE | ACCEPT | Giải thuật 3.1 |
| LR-10 | 495 | Missing complexity and runtime | PARTLY. Only per-job wall time exists (REG H13, WP14r, old runner); per-decision overhead was never measured | MODIFY | §3.7 reports H13 with caveat and a code-based complexity sentence; no invented timing |
| LR-11 | 496-501 | Implementation section 3 pages | OPINION | MODIFY | 2,5 p |
| LR-12 | 455 | Add a "luật C" row to Bảng 2.2 | OPINION | ACCEPT | Bảng 2.2 |
| LR-13 | 79 | Do not copy DACN's number-free abstract | TRUE. DACN PDF 5 opens with prose, no figures in the lines read | ACCEPT | STYLE rule 8 kept |
| LR-14 | 81, 511-514 | Blank "Tài liệu tham khảo" page then "Bibliography" | TRUE. TEX/10-tai-lieu.tex:1-4 (`\chapter*` then `thebibliography`); PDF p. 102 has only the heading, p. 103 starts "Bibliography" | ACCEPT | Fix (rename `\bibname`, drop the extra `\chapter*`); saves ≈ 1 p |
| LR-15 | 82, 107, 369-378 | Example rider illustrates the forecast, not C; the 1,3% dispatch share is measured under C | TRUE. REG C31; FR:72 is C-30 | ACCEPT | H1.1 shows two riders; ch. 1 motivation uses U (REG C21, C24) |
| LR-16 | 104-106 | Business value is a real gap; UberX Share page could open §1.1 | TRUE. REG I10; REG J28 ("we cannot guarantee arrival times", VERIFIED-by-Codex) | ACCEPT | §1.1 practice context; no business claim |
| LR-17 | 117-120 | Internal codes (T3.8, w07, WP14r, Family A/B); give Vietnamese set names | TRUE | ACCEPT | Set names in V2 §2 |
| LR-18 | 121 | "Ba nguyên nhân" is wrong: the third part is a residual | TRUE (same as CX-26) | ACCEPT | §1.2 retitled |
| LR-19 | 122-125 | Symbols before definition (Bảng 2.2 Σ(c + x); Bảng 1.1 formulas) | TRUE. O:322, O:332 precede O:341 | ACCEPT | Tables 1.1/2.2 in words; identity in §3.4 |
| LR-20 | 151-158 | Sentence 1: e is a time, not a plan; it includes execution progress | TRUE. REG A01, A02 | ACCEPT | Contribution wording |
| LR-21 | 160-169 | Sentence 2: B clash, ambiguity of "không phụ thuộc phần tắc đường", six differences | TRUE | ACCEPT | Cite HZ by equation, not "chiến lược B"; three differences only |
| LR-22 | 171-176 | Sentence 3: jargon, "phần còn lại" twice, unnamed precedent | TRUE | ACCEPT | Sentence rewritten |
| LR-23 | 178-184 | Sentence 4: define "ô"; 3.672 = 34 × 108 | TRUE. REG B09 | ACCEPT | "kịch bản" (GLOS F) |
| LR-24 | 186-192 | Sentence 5: too many numbers; 41,3% needs "x trên y quyết định" | PARTLY. No pooled forced-decision count exists in REG or T38A (T38A:73 "means over cells") | MODIFY | Paragraph uses the countable "28 trên 34 kịch bản" (T38A:77); 41,3% stays in ch. 4, labelled; pooled count only via a new script |
| LR-25 | 194-201 | Sentence 6: write 4/2.338; give padded service; state the trade-off | TRUE | ACCEPT | §1.4 list and §4.8 |
| LR-26 | 203-207 | Sentence 7 jargon | TRUE | ACCEPT | Rewritten |
| LR-27 | 209-232 | Lecturer's rewrite (~300 tiếng, 10 numbers) | PARTLY. Uses "đoán trước được" (CX-04) and describes padding as "+30 s vào mọi lời hứa" without the forecast (REG C10: the tie is U + forecast + 30 s); its cumulative sentence is now outdated by STG:44 | MODIFY | Structure adopted, three errors fixed |
| LR-28 | 234-240 | Put a "Kết quả chính" list with denominators after the paragraph | OPINION | ACCEPT | §1.4 list (5 lines) |
| LR-29 | 242-260 | Two-column "kế thừa / làm thêm" table; move most negatives to §5.2 | PARTLY. The table is better; but the unfavourable comparisons must stay in the body next to the claim (CXR:125; R17:180-188) | MODIFY | Two-column box in §1.4 + 4 non-claims there; the rest in §4.11/§5.2 |
| LR-30 | 362-367 | Q7: U and C-30 differ only in hardLimit, so C − U is the cap's effect with the selector fixed | PARTLY. Single difference confirmed (REG A08, H01). But served sets differ (REG C04), the late count moves with service (R18:243-247), and the open question is whether the effect holds under another selector (REG H02) | MODIFY | §4.6 opens with the fact in non-causal words |
| LR-31 | 380-386 | Q9: when was B = 30 s chosen? | TRUE gap. 30 s was the static-set level C1 (TEX/08-chuong4.tex:126-138) and the T3.8 arm list was fixed before the first job (REG B10) | ACCEPT | One sentence in §4.1, with no plan or sealing language |
| LR-32 | 388-391 | Q10: 2.328 on 34 cells when the forecast exists on 21 only | TRUE gap. REG F02; STG:30 "naive in inactive cells" | ACCEPT | Note under Bảng 4.12/4.13 |
| LR-33 | 393-403 | Q11: tests, FleetPy ↔ RideBound diagram, runtime | PARTLY. Tests 1.025/1.025 at ADR-077 time (REG A27, historical); runtime see LR-10 | MODIFY | H3.3 message-flow figure; §3.7 |
| LR-34 | 416-418 | Q13: one sentence on the expected direction at higher load, labelled hypothesis | OPINION | ACCEPT | §4.11 |
| LR-35 | 446 | §1.3 to 1,25 p, one table, no formulas | OPINION | ACCEPT | §1.3 |
| LR-36 | 447-450 | Research questions in ch. 1 | OPINION (= CX-27) | ACCEPT | End of §1.2 |
| LR-37 | 451 | §1.5 to 0,75 p as labelled bullets | OPINION | ACCEPT | §1.5 |
| LR-38 | 457-459 | Ch. 3 is thin at 12 p for an IT thesis | OPINION | MODIFY | 13 p |
| LR-39 | 462-466 | Ch. 4 too fragmented; group by research question; clean roadmap table | OPINION | MODIFY | Three blocks following the three parts + Bảng 4.0 |
| LR-40 | 467 | §5.2 to 0,5 p pointing to §4.11 | OPINION (Codex agrees) | ACCEPT | §5.2 |
| LR-41 | 469, 569-573 | Appendix ≤ 2 p | OPINION | MODIFY | ≤ 3 p (owner default) |
| LR-42 | 473 | ML to 2–3 lines | OPINION | MODIFY | 0,5 p inside §4.7 (keeps the guard conditions and the 7,1%) |
| LR-43 | 474, 476 | Snow to 1 p; Bảng 1.1 and 2.2 overlap | OPINION | ACCEPT | §4.9 = 1 p; one short and one full table |
| LR-44 | 475, 538-543 | Drop Appendix B | OPINION | MODIFY | Appx B ≤ 1 p: per-rule keep-route table and HZ variant only |
| LR-45 | 477-479 | Bảng 4.4 (10 × 8) too wide; split 4.4a without forecast / 4.4b with forecast and padding | TRUE. STYLE rule 20 (≤ 6 columns) | ACCEPT | Bảng 4.4 and 4.13 |
| LR-46 | 503-505 | Sign convention and a "cách đọc bảng" sentence | TRUE | ACCEPT | Writer rule 8 |
| LR-47 | 506 | Define (N) at Nhận xét 3.1 | TRUE (§3.5.5 is cut) | ACCEPT | §3.3 |
| LR-48 | 507-510 | One neutral voice | TRUE. STYLE rule 16 | ACCEPT | Writer rule |
| LR-49 | 515 | Split references by language? | OPINION (requirement UNVERIFIED) | MODIFY | Follow STYLE rule 35 unless the UET template says otherwise |
| LR-50 | 531, 547-556 | Add an inner cover if the template is like DACN | PARTLY. DACN has two Vietnamese covers + an English cover (DACN PDF 1-3); the thesis template is UNVERIFIED | MODIFY | +1 p contingency, not in the base budget |
| LR-51 | 545 | The supervisor's name must be settled before submission | TRUE | ACCEPT | Placeholder + open item |
| LR-52 | 558-567 | Short title without "chứng nhận"; ask the faculty about renaming | OPINION | MODIFY | Two options for the owner |
| LR-53 | 575-580 | Hard cutoff for Stage 1b; write the fallback first; same for 1a | OPINION | ACCEPT | Slot rules |
| LR-54 | 582-598 | Rule-name table | OPINION | MODIFY | Owner-default names; V named "luật trần độ dời khách thấy" |
| LR-55 | 601-603, 620, 625 | Run count only in Appx C; one late statistic; γ out; "vì sao đo"; call ± forecast/padding rows "vai trò từng thành phần" | OPINION | ACCEPT | Bảng 4.3 column "Vì sao đo"; §4.8 wording |

---

## 4. Antigravity (AGR)

| ID | AGR line | Comment (short) | Check | Decision | Change to the outline |
|---|---|---|---|---|---|
| AG-01 | 22 | Example rider is a "hành khách thực tế"; late "chủ yếu do tắc đường lúc 7:15 và 7:30" | PARTLY. The 7:15/7:30 jumps are real (EXAMPLE:8,43; HO:292) but not in AGR's inputs (O, main.pdf); the rider is simulated (CX-28) | MODIFY | Caption "khách trong bản ghi mô phỏng" |
| AG-02 | 25 | FA 2020 chose 13–15 h on 15/01/2013 to disregard traffic | TRUE. REG J07 | ACCEPT | §1.3, §2.2 (already in O) |
| AG-03 | 26 | HZ-B applies to at-risk on-board riders, no budget, no ledger | TRUE. REG J01, J05 | ACCEPT | Bảng 1.1 |
| AG-04 | 27 | S&P: 900 s deadline from the first offer, fixed travel times | TRUE. REG J10 | ACCEPT | Bảng 1.1 |
| AG-05 | 31-33 | "Do tắc đường bất ngờ → sổ cái ba phần v/e/p … (z = x + c)" | FALSE. The v/e/p identity is per revision (REG A01); the three-part ledger is q / f / residual (FFA:133-136) | REJECT | — |
| AG-06 | 39 | C-30 0% vs M⁺ 14,5% self-break | PARTLY. Values right (REG C13) but unlabeled cell means | MODIFY | Labelled in Bảng 4.5 |
| AG-07 | 47 | UET norm is 60–80 pages | OPINION, no source (UNVERIFIED) | REJECT | Not used as evidence |
| AG-08 | 50 | §4.4 to 2–2,5 p | OPINION | MODIFY | 3 p incl. Stage 1a |
| AG-09 | 51 | §3.3 to 1,5 p, proof to Appx B | OPINION. The proof is ≈ 6 lines (TEX/07-chuong3.tex:292-297); CX-33 and the owner default keep it in ch. 3 | REJECT | §3.3 keeps the short proof |
| AG-10 | 53 | §3.7 to 2,5–3 p | OPINION | ACCEPT | 2,5 p |
| AG-11 | 54 | Add a table of ML models | OPINION. A negative side result; REG G05-G10 fit in prose | REJECT | 0,5 p prose |
| AG-12 | 56 | Complexity table; DACN's 953 ms | PARTLY. A complexity sentence from code is possible; 953 ms belongs to a different system (DACN) | MODIFY | Code-based sentence only |
| AG-13 | 57 | Old→new notation mapping table at the start of ch. 3 | OPINION. Readers of the new thesis never see the old notation | REJECT | Internal macro file + grep check (O:581-583) instead |
| AG-14 | 66-73 | Q1 defence: "contract" bound; low load explains it; value remains at higher load; "trung vị dời giờ của U là 108,6 s; dòng 354" | FALSE. O:354 says 109,6 s = median smallest recorded overshoot of 148 rejected requests (REG D14); 108,6 s is U's median per change (CON:6), not in AGR's inputs. The higher-load claim is untested (REG B12, I04). Cumulative records now exist (STG:44) | REJECT | — |
| AG-15 | 76-83 | Q2 padding answer: 37,2 vs 7,4 (×5); 1,81 vs 0,17%; 106 vs 10 late (4,35% vs 0,43%); "triệt tiêu các ca trễ nặng do ghép xe", "lừa dối chỉ số" | PARTLY. Arithmetic right (A:7,9). Wrong: late > 60 s is not "trễ nặng" (heavy is > 300 s: 11 vs 0, A:7,9); the lateness is not attributed to pooling; the two counts are against different quotes; padded U serves 96 more and wins at 120 s (REG C10) | MODIFY | Keep the counts with labels in §4.8; drop the interpretation |
| AG-16 | 86-92 | Q3: cost-first changes "6,1% under C-30 vs 26,0% under U"; Stage 1b "sẽ trả lời dứt khoát" | FALSE. 26,0% is LOCKS on the fixed-traffic set (REG H04), two state populations (REG K16); Stage 1b cannot isolate cause alone (R18:243-247) | REJECT | — |
| AG-17 | 95-101 | Q4: M⁺ forced 41,3%, self-break 14,5%; "không thể đưa vào hợp đồng dịch vụ thực tế" | PARTLY. Numbers right (REG C13, cell means); business claim unsupported (REG I10); M⁺ at 30 s vs 900 s not noted (REG J11) | MODIFY | Numbers kept with labels; no business claim |
| AG-18 | 104-108 | Q5: simulation assumptions as limitations | OPINION, consistent with REG I01-I05 | ACCEPT | §4.11 |
| AG-19 | 111-118 | Q6 snow: 7,19% → 5,94%; "không thuật toán dự báo nào…"; "1 lần trong 4 tháng"; "sổ cái chứng minh 92,5% là do thiên tai (x)" | FALSE. 7,19/5,94% are cell means (REG F13), not in AGR's inputs; a prefix model explained 25,7% more (REG F15, K19); 5 snow spells in 9/2018–12/2019 (REG B26); 92,5% is the part not explained by the HIST forecast, a model projection (SNOW:10; REG K04) | REJECT | — |
| AG-20 | 69, 79, 98, 107, 114 | Preparedness ratings "ĐÃ CHUẨN BỊ RẤT TỐT" (Q1, Q2, Q4, Q5, Q6) | OPINION, contradicted for Q2 (LR-03 rates it "Một phần"; O has no argument) | REJECT | — |
| AG-21 | 129-131 | "Ngân sách" makes outsiders think of money | OPINION (LR agrees) | ACCEPT | Prose uses "trần"; GLOS D |
| AG-22 | 132-134 | "p − e chính là lỗi riêng của hệ thống điều phối"; e = objective traffic delay | FALSE. Blame wording is banned (REG K04; D03:222-224); e includes execution progress (REG A02) | REJECT | — |
| AG-23 | 135-137 | Two-sided: earlier and later changes are both charged | TRUE. DELTA:259-262 | ACCEPT | §3.2 plain-language sentence |
| AG-24 | 138-140 | "Phép chiếu mô hình" is jargon | OPINION (LR agrees) | ACCEPT | "phép tính theo mô hình" |
| AG-25 | 141-143 | "Phục hồi" sounds odd; forced = "chấp nhận phá vỡ cam kết để chuyến xe tiếp tục" | PARTLY. GLOS E: forced = rule removed every option, keep plan and record a breach; recovery (b) may take a no-worse plan (REG A18) | MODIFY | GLOS E definitions used |
| AG-26 | 144-146 | Always state the denominator of 0,17 / 0,43 / 3,25 / 8,34% | TRUE. REG K24 | ACCEPT | Writer rule 4 |
| AG-27 | 156-183 | Rewritten contribution statement | FALSE in meaning at 14 points (§4.1 below) | REJECT | — |
| AG-28 | 187-215 | Retitled chapters and sections | PARTLY. A few are fine; others keep "nguyên nhân", add causal "bóc tách", turn the snow limitation into "khả năng thích ứng", hide the negative ML result, use English-style capitals | MODIFY | Adopted: §2.2 and ch. 5 titles; rest rejected |
| AG-29 | 21-41 | Verdict "so sánh sòng phẳng / đối chứng công bằng" | OPINION, contradicted by LR-05 (M⁺ at 30 s; HZ not run) | REJECT | Fairness note instead |

### 4.1 Word-by-word check of the Antigravity contribution statement (AGR:156-183)

| # | AGR wording | Problem | Evidence |
|---|---|---|---|
| 1 | (1) "mỗi hành khách khi đặt xe được cấp một quỹ … B giây" | Scope: accepted riders, from the first promise | CFG30:17-23; REG A13 |
| 2 | (1) "phần … trễ phát sinh thuần túy do quyết định ghép xe được tách riêng khỏi ảnh hưởng của kẹt xe" | "Thuần túy" and "tách riêng" overclaim: e includes execution progress; a model projection | REG A01, A02, K04 |
| 3 | (2) "mở rộng thành một cam kết hoàn chỉnh" | Self-praise; no comparison supports "hoàn chỉnh" | STYLE rule 34 |
| 4 | (2) "tính toán độc lập với mức độ tắc đường" | c is computed with current travel times; only B is traffic-independent | REG A02, J05 |
| 5 | (2) "sổ cái điện tử minh bạch" | Embellishment | STYLE rule 34 |
| 6 | (3) "ba giải pháp cho ba nguyên nhân" | The third part is a residual, not a cause | FFA:135; CX-26 |
| 7 | (3) "phần do ùn tắc bất ngờ phát sinh trên đường" | The residual is what the forecast in use does not explain | REG F09 note, K19 |
| 8 | (4) "Đánh giá thực nghiệm quy mô lớn" | 108 requests and 8 vehicles per cell; load 0,535 | REG B02, B03, B12 |
| 9 | (4) "dữ liệu giao thông thực tế tại khu vực Manhattan" | One city-wide factor from measured data, not real traffic | REG B06, K49 |
| 10 | (4a), (5) "điều phối tự do", "phương án điều phối tự do" for U | U keeps locks; "ghép tự do" is FREE | REG A08, K50 |
| 11 | (5) heading "Giữ vững cam kết mà không làm giảm số lượng phục vụ" | C serves 96 fewer than U | REG C02 |
| 12 | (5) "luật hạn chót … tự phá vỡ cam kết ở 41,3% số quyết định" | 41,3% is the forced-decision share (cell mean); self-break is 14,5% of riders (cell mean) | REG C13 |
| 13 | (6) heading "Vượt trội về độ chính xác"; "một cách không cần thiết"; "0.17%" | Banned word; padded U wins at 120 s; value judgement unsupported; English decimal point | STYLE rules 23, 34; REG C10 |
| 14 | (6) "vẫn để 106 khách thực tế bị trễ hẹn (so với chỉ 10 khách của luật C)"; (7) "toàn bộ 98 lượt chạy … có áp dụng luật C" | Counts right but simulated riders, different quotes, service difference omitted; 98 is the measured-traffic subset only | A:7,9; REG E01 |

Correct parts kept: 96 / 127 / 31 / 2.338 / 2.332 / 2.328 / 2.366 / 37,2 / 7,4 / 1,81% (REG C02, C04, C06, C08, C10)
and the 98 / 1.256 / single-step facts within scope (REG E01).

---

## 5. Owner override versus the style documents

The owner forbids any mention of sealed plans, preregistration or predictions written before running, anywhere in the
thesis (not one sentence, not an appendix). Four places in the style documents contradict this and are overridden:

1. STYLE §4.5 rewrite («Kết quả mong đợi được ghi lại trước khi chạy (bản ghi để ở Phụ lục C) … 98 trên 102 …»).
2. STYLE §5.2 point 5 (one ordinary sentence in the setup + hashes in an appendix).
3. GLOS F row "kết quả mong đợi ghi trước khi chạy" and GLOS G first row.
4. REG rows whose notes mention plans or predictions (B10, C18, F03, F14 "Chưa niêm phong", G01, L01-L05 notes), and
   STG §10 / CXS:58-64 (Stage 1a P1–P5 verdicts). Writers may use the **measured values** of those rows, never the plan,
   hash, prediction or pass/fail language. Previewed-data limits stay, stated as data reuse (REG I06), not as protocol.

---

## 6. Side findings while checking (errors in the inputs)

| # | Where | Finding | Evidence |
|---|---|---|---|
| S1 | O:140 | "Needed to explain c ≥ 0" is wrong for T3.8 (same error as LR-04) | BUC:34,37; STG:39 |
| S2 | O:382 | "49% of revised C1 riders" — denominator is all 1.581 served | TEX/08-chuong4.tex:160,1728 |
| S3 | O:64 | List of tables starts at xii, not xi | PDF p. 8 |
| S4 | O:356, O:475-477, LR-27, REG E01/I17 | "Cumulative never the sole reason on measured traffic" is no longer true once Stage 1a is included: 3 cumulative-only records under C-120 on the 34 cells, the first on measured traffic; 2 of the 3 new requests ended not accepted (one of them also not accepted under C-30) | STG:44-47; CW21:2-7; CXS:91 |
| S5 | HO:110 | "M⁺-B … không cộng tắc đường" is misleading: the deadline compares with the first promise, so traffic drift alone can trigger it | REG A09, A10 |
| S6 | REG L01, D12 | Marked "chưa chạy"; Stage 1a is now run and doubly analysed | STG:1-23; CXS:3 |
| S7 | R18 B32 | Shared counts "≈ 555 / 313" were approximations; exact counts now exist: U 555, C-30 313, C-120 428 | STG:50-52 |
| S8 | AGR:73 | 108,6 s misread from O:354 (109,6 s, a different quantity) | O:354; REG D14; CON:6 |
| S9 | CW21:2 | One C-120 cumulative-only witness has the same 25.844 + 99.027 = 124.871 ms pattern as the U example of REG E07 | CW21:2; REG E07 |

---

## 7. Where the reviewers disagreed, and how I resolved it

| Topic | Codex | Lecturer | Antigravity | Resolution and reason |
|---|---|---|---|---|
| English cover + Abstract | Drop (Vietnamese-only rule) | Keep until the template is checked | — | **Keep** (owner default; DACN PDF 3, 6 has both) |
| Appendix size | ≈ 4 p (A 1,5; B 1,5; C 1) | ≤ 2 p, drop B | Move the proof to B | **≤ 3 p**: A ≤ 1 (only if re-anchored), B ≤ 1 (table + HZ variant), C 1; proof stays in ch. 3 |
| Theorem material | Remark + conditions + 2 CEs in body | "Nhận xét", drop B | Shorter §3.3 | Owner default; Codex's conditions (N) kept because they are needed for the claim to be true |
| "Hai chiều" | Keep \|·\|; do not claim c ≥ 0 | Remove; claims c ≥ 0 | Explains it as a feature | **Codex**: the data show earlier changes (BUC:37; STG:39); keep in the definition, do not sell it |
| "Cộng dồn" | Keep, scope the negative audit | Remove from differences | "Contract" defence + high-load speculation | Keep as definition (REG E08); report 0 records in 98 runs and 3 records under C-120; effect on outcomes not measured (REG E09) |
| ML section | Keep, fix 7,1% | 2–3 lines | Add a table | **0,5 p prose** in §4.7: enough for the guard conditions and the 7,1% |
| Cap dial pages | Keep both panels | — | 2–2,5 p | 3 p incl. Stage 1a (now filled) |
| Implementation pages | 2 p, no line counts | 3 p with runtime | 2,5–3 p | 2,5 p; runtime only as measured (REG H13) |
| Ch. 3 / Ch. 5 | 12,5 / 3 | ≥ 12 / 4 with §5.2 0,5 | — | 13 / 3 |
| Compensation column | Drop | — | — | Rename; hypothetical sentence only in §4.11 (REG C28) |
| Title | "Kiểm soát độ dời lời hứa giờ trả…" | Three short options | — | Two options; owner picks |
| Rule names | Long descriptive names | Descriptive Vietnamese | — | Owner-default names in prose; descriptions in Bảng 3.3 |
| Q1 preparedness | — | "Một phần" | "Rất tốt" | **Lecturer**: O had numbers, no argument |
| Bảng 4.4 | Split pooled / cell mean | Split without / with forecast | — | Both splits (Bảng 4.4, 4.5, 4.13) |
| "Ba nguyên nhân" | "Ba phần của phép phân tích" | "Ba phần" | Keeps "nguyên nhân" | **Codex + lecturer**: the residual is not a cause |

---

## 8. The strongest examiner question

> «Cần luật C để làm gì, khi không trần + dự báo + đệm 30 s đạt cùng 2.328 lượt đúng giờ ở 60 s và hơn ở 120 s?»

**What the thesis can argue (every number from A:7,9 or STG; derived ones marked [A] and to be recomputed by script
before use).**

1. **At equal promise length, the cap wins at 60 s and loses at 120 s.** With the forecast and no padding (mean
   extension 7,4 s for C-30, 7,2 s for U), C-30 has 2.328 vs 2.297 lượt không trễ quá 60 s per 3.672 requests, and
   2.338 vs 2.347 at 120 s (A:7,9; STG:32-33). Padding both by 30 s (≈ 37,2–37,4 s): C-30 2.336 vs U 2.328 at 60 s,
   2.338 vs 2.366 at 120 s (A:7 `fc_pad30` late60 2; A:9 late60 106, late120 68). The padded U only ties C by making
   every promise about five times longer (37,2 vs 7,4 s).
2. **Promise accuracy is two-sided.** Early by > 60 s: 4/2.338 for C-30 + forecast vs 44/2.434 for padded U (A:7,9).
   Within ±60 s of the first promise, per request: 2.324 vs 2.284 [A: served − late60 − early60].
3. **Tail among served riders.** Late > 120 / 300 / 600 s: 0 / 0 / 0 for C-30 + forecast vs 68 / 11 / 1 for padded U
   (A:7,9). Padded U's timely120 lead (+28 per request) comes with 96 more served riders, not with fewer late ones.
4. **A per-rider bound on the dispatch part that does not depend on traffic or on the forecast being right.** Under
   C-30 the largest dispatch-attributed total is 29,2 s and 33 riders were moved; under U (and so under padded U, which
   replays U's journeys) 590,1 s, 174 riders, 12 moved at least twice (A:7,9; STG:37-38). The bound held on weekend cells
   with no forecast and on the snow afternoon (dispatch 8,6 of 3.445,9 late seconds, REG F13).
5. **Against the deadline rule, the difference is which obligation can be kept.** Same 2.338 served and same 2.328
   timely with forecast, but C was never forced (0%), while the deadline rule was forced in 41,3% of decisions (cell
   mean) and broke its own promise for at least one rider in 28/34 cells (REG C13; T38A:76-77). By construction (REG A22).
6. **The cap is a dial, and padding can be layered on top.** C-120 + forecast reaches 2.322 timely60 and 2.379
   timely120 per request at 7,27 s extension (STG:34), i.e. more on-time at 120 s than padded U (2.366) with one fifth of
   its quote extension, while serving 2.387 (47 fewer than U). Cohorts differ (STG:55-56); this is one more measured
   point, not an optimum.

**What the thesis cannot claim.**
- That C is more reliable per request than padding: it ties at 60 s and loses at 120 s at C-30 (REG C10, K06).
- That shorter promises, fewer early arrivals or a per-rider dispatch bound are worth 96 lost rides or 242 lost shared
  completions (555 → 313, STG:50-51): there is no willingness-to-pay, rider-response or operator evidence (REG D20, I07,
  I10, C29).
- That C guarantees arrival times (counter-example CE-2; REG A22, K05).
- That the cap rather than the stability-first selector produces the reliability (REG H02, K18; Stage 1b not run).
- That padded U is a matched control: it is a quote replay on U's journeys (R18:249; REG C10 note).
- Anything beyond this testbed: one simulator, one city-wide factor, 5 days, dependent cells (REG I01-I06).

**Draft Vietnamese paragraph for §4.8 (the writer may use it after the [A] numbers are scripted).**

> Khi có dự báo, cộng thêm 30 giây vào mọi lời hứa của điều phối không trần cũng cho 2.328 lượt không trễ quá một phút
> trên 3.672 yêu cầu, bằng luật C, và cho 2.366 lượt không trễ quá hai phút, hơn luật C 28 lượt. Hai cách này không
> cùng độ dài lời hứa: cách đệm kéo dài lời hứa trung bình 37,2 giây, luật C 7,4 giây. Khi cùng độ dài lời hứa, luật C
> hơn ở ngưỡng một phút (2.328 so với 2.297 khi không đệm, 2.336 so với 2.328 khi cùng đệm 30 giây) và kém ở ngưỡng hai
> phút (2.338 so với 2.347 và 2.366). Trong số khách được phục vụ, cách đệm có 44 khách tới sớm quá một phút và 68 khách
> trễ quá hai phút; luật C có dự báo có 4 và 0. Ngoài ra, luật C giới hạn phần dời do điều phối của từng khách ở 29,2
> giây, còn khi không trần phần này lên tới 590,1 giây cho một khách. Đổi lại, luật C phục vụ ít hơn 96 lượt. Trên dữ
> liệu này, cách đệm là một lựa chọn cạnh tranh; khóa luận không có bằng chứng khách hay hãng xe coi trọng lời hứa ngắn
> hơn hoặc giới hạn theo từng khách đến mức nào.

*End of file. Written by Claude (outline consolidator), 2026-10-11. No other file was written or modified.*
