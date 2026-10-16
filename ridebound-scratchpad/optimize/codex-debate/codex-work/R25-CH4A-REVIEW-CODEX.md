# Round 25 — Codex review of Chapter 4, part A

**Verdict: ACCEPT WITH REQUIRED CORRECTIONS.** The main outcome counts, means, overlaps, cumulative-audit totals and figure coordinates agree with the saved evidence. The important defects are interpretations and units: an unconditional no-op explanation, an inaccurate definition of the recovery counter, an unsupported “structural only” classification, a request-to-rider denominator switch, and a comparison that mixes changing the dispatcher with changing its cap. The morning run-count row also counts configurations it does not list.

Reviewed `rewrite-2026-10/drafts/08-chuong4-phanA.tex`, its NOTES, the writing brief, Chapter 4 of OUTLINE-V2, REVIEW-DECISIONS-R20 §8, the register and addendum §0, and the relevant saved outputs and source locations below. Draft line numbers below refer to the supplied file. **No `rewrite-2026-10/reviews/*CH4*` file was read.** No simulation, build, installation or thesis/draft modification occurred. This review is the only new file.

## 1. Evidence and verification boundary

Paths below are relative to `E:/Code/Report_INT3508/ridebound-scratchpad/`, except SRC.

| Key | Source |
| --- | --- |
| REG / ADD | `rewrite-2026-10/evidence/EVIDENCE-REGISTER.md` / `EVIDENCE-REGISTER-ADDENDUM-1.md` |
| A / AJ | `optimize/codex-debate/codex-work/R15-audit-summary.txt` / `R15-audit.json` |
| NEW | `optimize/codex-debate/codex-work/R18-verification.txt` |
| CXJ / CXS | `optimize/codex-debate/codex-work/R19-stage1a-analysis.json` / `R21B-STAGE1A-CODEX.md` |
| IV / IVOUT / IVC | `tang3/t38/independent/RESULT.md`, `iv_analyze.out.txt`, and `cache/*.json` in that directory |
| ADD1 / ADDJ | `rewrite-2026-10/evidence/checks-addendum-1/recompute-addendum-1-2026-10-11.txt` / corresponding `.json` |
| SNOW1 / DER1 | `rewrite-2026-10/evidence/checks-addendum-1/check-snow-c30-2026-10-11.txt` / `derive-addendum-1-2026-10-11.txt` |
| STG / CW21 / TSV | `optimize/codex-debate/claude-work/r21-stage1a/stage1a-report-2026-10-10.txt`, `cum-witness-check-2026-10-10.txt`, `stage1a-2026-10-10-riders.tsv` |
| PAD / BUD / BUDPY | `optimize/codex-debate/claude-work/cap-vs-pad-frontier-2026-10-07.txt`, `budget-block-diagnosis-2026-10-07.txt`, `budget_block_diagnosis.py` |
| LAD / WP17 / DIAL17 | `optimize/codex-debate/claude-work/wp14r-ladder-reanalysis-2026-10-08.txt`, `r17-rebuttal/r17-wp14r-check-2026-10-10.txt`, `r17-rebuttal/r17-verify-dial-2026-10-10.txt` |
| COM / CON / LATE | `optimize/codex-debate/common-riders-check-2026-10-06.txt`; `optimize/report-extras/constraints-and-pooling-2026-10-06.txt` / `lateness-distribution-2026-10-06.txt` |
| W07 / W07X / W07XM | `tang3/w07/W07-REPORT.md`; `tang3/w07x/W07X-REPORT.md` / `analysis/mechanism-2026-10-01.txt` |
| FJC / CVP | `optimize/codex-debate/claude-work/r13-final-judge/cumulative-decisive-check-2026-10-10.txt`; `r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` |
| INV / R13J | `optimize/codex-debate/claude-work/data-inventory-summary-2026-10-08.txt`; `optimize/codex-debate/codex-work/R13-raw-verification.json` |
| SRC | `C:/Code/RideBound-noworse/src/` |
| GEN / HVA / POL | SRC + `RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs`; `Commitments/HardVectorCandidateAssessor.cs`; `Policies/SolverBackedRidePoolingPolicy.cs` |

**What was recomputed in this round:** main outcomes directly from the saved CXJ per-rider rows; day/window groups from its per-run rows; cell means and own-obligation counts from the 170 test IVC extraction files selected by `split-t38-v1.json`; ledger shares and shared completions from TSV; morning recovery means from the available R13J per-run rows; derived differences, ratios, totals, and all plotted coordinates. These are independent arithmetic checks on saved extractions, **not a new full raw-transcript audit**. A/R15 and CXS/R21B retain the earlier independent transcript checks.

**Labels:** AGREE verifies the stated quantity within its stated cohort; WRONG identifies a false/unsupported definition, interpretation or scope, even when the integer is correct; CANNOT CHECK identifies an unavailable measurement. A registered statement is not automatically correct: BUDPY contradicts the interpretation of REG D13/D19.

## 2. Setup, denominator and cohort audit

| Draft location | Quantity/statement checked | Verdict and evidence |
| --- | --- | --- |
| 56–60, 79–91 | FleetPy 1.0.2; Manhattan data covering 11–18/11/2018; two-hour windows; 108 requests from a 10% demand sample; 8 vehicles × 4 seats | **AGREE** for the described experimental inputs: REG B01–B03/J18; CXJ manifests and per-run request counts. This does not turn 108 requests into 108 served riders. |
| 63–66, 79–80 | City-wide factor in 15-minute bins; ordinary windows 7–9, 8–10, 17–19; snow 14–16, 15–17; 3–20 shared requests across windows | **AGREE** as registered: B06/B08/B20/I05/K49. Overlap explicitly prevents treating scenarios as independent samples. |
| 83–89 | 96-node OD closure; pickup 600 s; ride ≤1.5 × direct; zero dwell checked on 3 examples; baseline factor at 00:00 | **AGREE** at REG B03/B05–B07/K48's scope. “Kiểm trên 3 lần chạy mẫu” correctly limits the dwell check. No claim that this is a street-level network or an industry standard. |
| 90–91 | 100 candidates per vehicle; at most 2 new requests per decision batch; OR-Tools 9.15; seed 7 | **AGREE**, with a register correction needed. GEN:74–79 truncates the pending request list **before** the vehicle loop at 98–107. The limit of 2 is global to this batch, despite the option's misleading property name. REG A24's “mỗi xe” is wrong on that point. See §7 below. |
| 103–106, 120–122 | 49 constructed scenarios = 34 main + 15 calibration; main windows 9/14/11; 3,672 requests; 170 five-arm runs + 34 C-120 | **AGREE**: IV:15–17/30–34, REG B08–B10, ADD1:5–8, CXS:3/54. Arithmetic: 9+14+11=34; 34×108=3,672; 34×5+34=204. |
| 105 | 14–16/11 weekdays, 17–18 weekend | **AGREE**. Calendar dates and REG B21; no unsupported assertion about 12/11 holiday status. |
| 124–126 | Morning: 8 scenarios, 864 requests, 12–13/11, window 7; listed U plus C/M⁺ at eight cap values; 88+104 runs | **WRONG as a row with this caption.** 88+104=192 is the full archived experiment count, not the count for the listed configurations. `run_w07.py`:33–34 includes V-30 and M-30; `run_w07x.py`:35–37 includes five more V levels. Listed U + 8 C + 8 M⁺ =17 arms, hence **136 runs**; excluded six V arms and one M arm account for **56** more. REG B15/B16's archive totals remain correct. |
| 127–129 | Fixed factor: 16 scenarios, 1,728 requests, 12–13/11, windows 8/17; 16 runs for each of five shown arms; old runner without recovery | **AGREE**: LAD:1–6, WP17:1–20, REG B17/H13. 16×108=1,728; shown five-arm subset has 80 runs. LAD's 160 archived runs include additional arms and are not the shown subset. |
| 130–132, 455–456 | Snow: 8 C-30 runs, 601 served riders; runner status “Chưa kiểm lại”; 8 exposed; max25.2 s; zero overshoots/recovery | **AGREE**: SNOW1:2–10. **601 is a served/accepted cohort, not all input requests.** INV:14–15/17–22 reports 108 input requests in each of these eight scenarios: 864 input requests. ADD N-26's “601/601 phục vụ” concerns the accepted cohort. The draft currently calls them “lượt phục vụ”, correctly. |
| 137–140 | U differs from C-30 only in the drop cap; other commitment arms share generator/validator/selector; FREE uses another policy | **AGREE** at the configured-policy level: NEW:11–13, REG A08/A17/A19/H01/K50. This makes the later FREE-to-C wording misleading, not this paragraph. |
| 143–146 | Failed original replaced by completed rerun; 1,991 run records in archive | Rerun convention **AGREE**: ADD1:6 and CXS:9–13. **1,991 AGREE as the 08/10 inventory snapshot**, INV:1. **CANNOT CHECK as a current archive count**; the supplied inventory predates the new C-120 panel. Date the sentence. |
| 151–155, 175–183 | Served-only late/early quantities; timely=served−late; timely denominator all requests; strict >T and <−60; extension pooled over each served cohort | **AGREE** with the table definitions, ADD1:10–31 and CXS:70–81. Opening “chỉ trên khách được phục vụ” needs refinement because timely-per-request uses **all requests**, while rejected requests contribute zero successes. |
| 158–162 | Frozen forecast replay; 21 active weekday scenarios, 13 inactive weekend scenarios; morning 12–13/11 inactive | **AGREE**: REG C09/F02/F03/D02, ADD1:5–8/113–114, DIAL17:3–13. Interpret “only first quote changes” as the outcome comparison against first quotes; no redispatch occurs. |
| 184–187 | Shared rider means onboard overlap; exposed rider means any nonzero dispatch change; amount Σ|c| | **AGREE**: TSV, ADD1:103–111/135–139, REG A06/C20/N-09. Accepted=served in this main panel, explicitly checked by ADD1:5–8; do not silently extend that equality to every future run. |
| 188–190 | Recovery means the rule eliminated **all** candidates of one vehicle, including no-op | **WRONG.** The measured counter is acknowledged decisions with `certificate.body.normalOperation == false`, IV:47–51/IVOUT:117–124. HVA:247–279 can enable recovery when the safety no-op is validator-pruned; it does not require every other candidate to be eliminated. POL:448–462 identifies **selected** forced options. Use the recorded-certificate definition. |
| 191–193 | C own failure Σ|c|>B; M⁺ own failure arrival−p0>B; V own failure Σ|z|>B; percentages averaged per scenario | **AGREE**: IV:53–61, `iv_analyze.py`:168–200, ADD N-21. They are different obligations; this is not a common arrival-quality criterion. |
| 205–214 | B=30 historical static-set choice; exploratory thresholds/split/C-120 choice; no population or unseen-data validation claim | **AGREE** with REG K33/B08/B10/I06/K42 and NOTES' supplied code/thesis anchors. Keep the explicit exploratory language. Some supporting facts still need actual register rows (§5, change 9). |

## 3. Complete table and numeric-result audit

### Main table, `bang:c4-chinh` (243–248)

All entries below have been checked. Counts use 3,672 input requests; late counts concern that arm's served cohort.

| Arm | Served | Late >60 s | Timely60 | Timely120 | Shared served | Verdict/source |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| U | 2,434 | 203 | 2,231 | 2,332 | 555 | **AGREE**, CXJ/TSV; A:9, ADD1:12/136 |
| C-30 | 2,338 | 76 | 2,262 | 2,327 | 313 | **AGREE**, CXJ/TSV; A:7, ADD1:17/137 |
| M⁺-30 | 2,338 | 74 | 2,264 | 2,327 | 307 | **AGREE**, IVC and ADD1:27/139; A:8 |
| M⁺-60 | 2,347 | “chưa đưa vào bảng” | same placeholder | same placeholder | same placeholder | **AGREE** served count, IV:31. Other cells explicitly unreported, not zero. OUTLINE-V2:191 permits this fallback. |
| V-30 | 2,336 | “chưa đưa vào bảng” | same placeholder | same placeholder | same placeholder | **AGREE** served count, IV:31. Same fallback applies. |

Fresh IVC arithmetic also gives M⁺-60 late60=79 and late120=11, hence timely60=2,268 and timely120=2,336; V-30 late60=74 and late120=11, hence timely60=2,262 and timely120=2,325. These **newly recomputed** values require registration before insertion. I did not verify their shared-completion counts. The existing placeholders are an authorized fallback; filling them is not a release-blocking demand in this review.

Paragraphs 220–222/254–279: **AGREE**. Recomputed:

- 2,338−2,434=−96; 76−203=−127; 2,262−2,231=+31=−96−(−127).
- 96/3,672×100=2.614379 points; 96/2,434×100=3.944125%. Draft 2.61 points/3.94% is correct.
- Windows U→C-30 served: 516→511 (−5), 1,014→975 (−39), 904→852 (−52); losses sum to −96. ADD1:150–160.
- Shared fractions 555/2,434=22.801972%, 313/2,338=13.387511%; draft 22.80%/13.39% correct. Shared count difference is 242.
- U/C-30 overlap: 2,207 common +227 U-only /+131 C-only =2,434/2,338. C-30/M⁺-30: 2,332 common +6 each =2,338 each. A:18–19, CXJ overlaps, ADD1:145–146.
- On common U/C riders, wait +0.522 s and ride −10.507 s round to +0.5/−10.5. **AGREE as saved descriptive contrasts**, COM:2–3; not a randomized/matched baseline or a population effect. Draft already warns about selection into the common cohort.
- Deadline 30/60 s versus the cited paper's 900 s default: **AGREE** as the registered adapted comparator, REG J10/J11. Paragraph 225–228 correctly disclaims reproduction of the full authors' system.

### Own-obligation table, `bang:c4-nghiavu` (294–297)

Independently recomputed from the 34 test IVC files per arm. Percentages below are **unweighted cell means**, not the pooled fractions in the next table.

| Arm | Mean recovery % | Mean own-break % | Scenarios with own break | Verdict |
| --- | ---: | ---: | ---: | --- |
| C-30 | 0 | 0 | 0/34 | **AGREE** |
| M⁺-30 | 41.311366→41.3 | 14.479634→14.5 | 28/34 | **AGREE** |
| M⁺-60 | 22.527695→22.5 | 4.231312→4.2 | 22/34 | **AGREE** |
| V-30 | 53.775777→53.8 | 21.576716→21.6 | 34/34 | **AGREE** |

IV:47–61 and IVOUT:120–153 support the published rounded values. Fresh extraction sums clarify the missing rate counts:

| Arm | Recovery count / acknowledged decisions | Own-break count / served riders |
| --- | --- | --- |
| C-30 | 0/20,101 | 0/2,338 |
| M⁺-30 | 7,710/20,103=38.352485% | 289/2,338=12.361% approximately |
| M⁺-60 | 4,031/20,163=19.992065% approximately | 79/2,347=3.366% approximately |
| V-30 | 10,442/20,090=51.976108% approximately | 456/2,336=19.521% approximately |

These pooled values **must not replace** 41.3/14.5/22.5/4.2/53.8/21.6 under a cell-mean caption. V's pooled own-break count 456 is a fresh IVC-derived result, not a value already copied into REG C13.

303–315: **AGREE numerically**. M⁺-30 pooled recovery 38.35%, pooled own-break 12.4%; morning-window means 36.53→36.5% own-break and 75.62→75.6% recovery (9/9 scenarios); evening means 1.04→1.0% and 4.99→5.0% (5/11). ADD1:189–192. **WRONG interpretation** at 308–310: the no-op proof needs its conditions, separately addressed below.

### Lateness distribution, `bang:c4-phanbotre` (338–343)

| Arm | Late >60/>120/>300/>600 s | Counts per 100 requests, same order | Maximum lateness, min | Verdict |
| --- | --- | --- | --- | --- |
| U | 203 /102 /18 /2 | 5.528322→5.53 /2.777778→2.78 /0.490196→0.49 /0.054466→0.05 | ≈11.00 | **AGREE**, CXJ recomputation, A:9, LATE:3–5; CON:4 gives 660.1 s |
| C-30 | 76 /11 /0 /0 | 2.069717→2.07 /0.299564→0.30 /0 /0 | ≈3.87 | **AGREE**, CXJ, A:7, LATE:10–12; CON:11 gives 232.3 s |

**AGREE** at 353–356: 76−4=72 late C-30 riders had no nonzero dispatch drop change. This does **not** identify “pure traffic” as their physical cause; the draft correctly leaves two ledger terms. The forecast/padding material is scheduled for part B, not absent from an allegedly complete chapter.

### Day × window table, `bang:c4-ngaykhung` (374–388)

Every cell was independently summed from CXJ and compared with ADD1:173–186 / ADD N-22. Deltas are C-30−U; the last column counts scenarios with C timely60≥U.

| Day/window | n | Δserved | Δlate60 | Δtimely60 | C not worse in timely60 | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 14/w07 | 2 | 0 | 0 | 0 | 2 | **AGREE** |
| 14/w08 | 2 | −4 | −7 | +3 | 2 | **AGREE** |
| 14/w17 | 2 | −8 | −7 | −1 | 1 | **AGREE** |
| 15/w07 | 3 | +2 | −2 | +4 | 3 | **AGREE** |
| 15/w08 | 3 | −8 | −10 | +2 | 3 | **AGREE** |
| 16/w07 | 3 | −3 | −1 | −2 | 2 | **AGREE** |
| 16/w08 | 3 | −9 | −13 | +4 | 3 | **AGREE** |
| 16/w17 | 3 | −11 | −21 | +10 | 2 | **AGREE** |
| 17/w07 | 1 | −4 | −6 | +2 | 1 | **AGREE** |
| 17/w08 | 3 | −2 | −7 | +5 | 3 | **AGREE** |
| 17/w17 | 3 | −19 | −18 | −1 | 2 | **AGREE** |
| 18/w08 | 3 | −16 | −15 | −1 | 2 | **AGREE** |
| 18/w17 | 3 | −14 | −20 | +6 | 3 | **AGREE** |
| Total | 34 | −96 | −127 | +31 | 29 | **AGREE** |

All 34 C late60 counts are ≤U; all 25 w08/w17 scenarios are strictly lower; w07 has three lower and six ties. **AGREE**, ADD1:167–169/186. Counts concern each arm's served set; 29/34 is not independent-binomial evidence because the 34 scenarios span five dates and overlap. The draft appropriately describes observed scenarios.

### Dispatch table, `bang:c4-doidieuphoi` (428–434)

| Measure | U | C-30 | C-120 | Verdict/source |
| --- | --- | --- | --- | --- |
| Exposed served riders | 174/2,434=7.15% | 33/2,338=1.41% | 103/2,387=4.32% | **AGREE**, CXJ/ADD1:104–108 |
| At least two nonzero changes | 12 | 0 | 0 | **AGREE**, CXJ; A:7/9 |
| Max Σ|c|, s | 590.133→590.1 | 29.239→29.2 | 118.938→118.9 | **AGREE** |
| Median magnitude per change, s | 108.636→108.6, 187 changes | 8.295→8.3, 33 changes | 62.544→62.5, 103 changes | **AGREE**, U recomputed from IVC revisions; ADD1:104–108. Not a median of rider totals for U. |
| Late60 and exposed / late60 | 134/203 | 4/76 | 60/132 | **AGREE**, CXJ per-run ledgers / ADD1:104–108 |
| Signed ledger dispatch contribution / total late seconds among late60 riders | 23,027.239/31,353.407=73.444136% | 81.742/6,891.526=1.186123% | 4,836.281/12,450.223=38.844935% | **AGREE** rounded 73.4/1.2/38.8; independently recomputed from TSV |

The last row sums **signed** net dispatch contribution, not Σ|c|, and divides by summed lateness seconds in the specified late cohort, not all passengers, all requests, or an average of individual ratios. This definition and these denominators should appear with the percentages.

444–450: **AGREE**: C-30's 33 exposed riders comprise 29 net-later and four earlier by exactly 1 ms each; total earlier amount 4 ms=(359,173−359,165)/2. ADD1:106–107/112, ADD §0.1–0.2. No proven explanation of those −1 ms changes is supplied. The draft correctly avoids inventing one.

453–456: **AGREE**: weekend maxima 29.239→29.2 /116.542→116.5 s on the 13 inactive scenarios, ADD1:113–114. Snow 601 served /8 exposed /max25.187→25.2 /0 overshoots /0 recovery in 5,067 acknowledged decisions, SNOW1:10. Accepted counts across eight snow runs sum 86+74+80+75+75+66+85+60=601; decision counts sum 714+626+658+634+630+570+699+536=5,067.

459–467: **AGREE numbers, WRONG arrival/projection wording.** W07XM:6/11/16 records prior model displacement 79.0 or60.9 s, prior dispatch0, proposed dispatch68.3 or61.2 s. Three first divergences at B90/120; C accepts one extra request at each, W07X:54–62. “Khoảng147” safely rounds the proposal (the new exogenous increment is also approximately0.1 s in the first example). **79.0 s is the existing predicted/published ETA displacement, not an observed completed-trip lateness for an onboard rider.** Replace “đã muộn” as specified below.

469–482: counts **AGREE**; labels need two required corrections:

- 3,672−2,338=1,334 final rejections; BUD:2–5 splits 148 with recorded budget blockers (116 U-served+32 U-rejected) and 1,186 without such a recorded blocker (111 U-served+1,075 U-rejected).
- AJ/A and REG D16: 845 records relate to 643 request-scenario pairs; 495+148=643, with 495 finally served. A record/candidate is not a customer or an exclusive rejection cause.
- **WRONG**: “1.186 ... chỉ có lý do cấu trúc.” BUDPY:29–44 merely puts a request in this residual group when it has no matching recorded budget-pruned candidate. It does not prove structural impossibility or enumerate all reasons.
- **WRONG**: “2 trong148 khách chặn.” BUDPY:22/35–42 selects one minimal-overshoot record per **finally rejected new request**; the numerator asks whether any blocking witness for that selected record has before>0. It does not count 148 distinct blocking incumbent riders.
- Median minimal recorded overshoot109.6 s and max524.8 s **AGREE**, BUD:6; B120 screen59/148 **AGREE**, BUD:8. Its condition is overshoot≤90 s because the original cap is30 s. It is not a prediction that59 requests will be served.
- All845 main C-30 reported blockers already fail a single30 s increment, so the corresponding148 request-scenario pairs have such a reported record: **AGREE**, A:7/FJC:4–6. This does not establish that prior spending was absent from all other candidates.

### Fixed-factor table, `bang:c4-codinh` (512–516)

Every displayed number agrees with WP17:2/5/9/14/19 and LAD:2–6.

| Arm | Served / requests | Late60 | Timely120 | Shared % of served | Exposed count / served → % | Verdict |
| --- | --- | ---: | ---: | ---: | --- | --- |
| FREE | 1,629/1,728 | 274 | 1,465 | 53.1 | 388/1,629→23.8 | **AGREE** |
| U (=LOCKS here) | 1,584/1,728 | 47 | 1,557 | 21.8 | 62/1,584→3.9 | **AGREE** |
| C-120 | 1,563/1,728 | 23 | 1,563 | 19.4 | 41/1,563→2.6 | **AGREE** |
| C-60 | 1,540/1,728 | 0 | 1,540 | 17.3 | 20/1,540→1.3 | **AGREE** |
| C-30 | 1,534/1,728 | 0 | 1,534 | 15.7 | 6/1,534→0.4 | **AGREE** |

Timely120 is served minus late120164/27/0/0/0 respectively. **CANNOT CHECK exact shared-count numerators from the cited rounded LAD output alone.** Do not reconstruct an integer numerator by multiplying a rounded percentage by served count. LAD's implementation defines pooled onboard overlap (`wp14r_ladder_reanalysis.py`:33–45); the percentage values themselves agree. Supply actual numerators from saved records before claiming full compliance with the writing brief's rate rule.

526–528: endpoint numbers1,629→1,534 and274→0 **AGREE**; “Siết dần từ ghép tự do...” **WRONG as a cap-only interpretation**. FREE→U changes the policy/commitment checks and selection objectives. The valid same-policy cap ladder is U/C-120/C-60/C-30. Observed C-60→C-120 adds23 served and23 late60; timely60 stays1,540. “Điểm gãy” should be the observed difference between sampled levels, not a located continuous threshold.

### Morning table and all prose cap levels (531–568)

| Arm | Served | Late60 | Timely60 | Timely120 | Verdict/source |
| --- | ---: | ---: | ---: | ---: | --- |
| U | 665 | 50 | 615 | 656 | **AGREE**, DIAL17:3 |
| C-30 | 660 | 47 | 613 | 658 | **AGREE**, DIAL17:4 |
| C-90 | 664 | 50 | 614 | 660 | **AGREE**, DIAL17:6 |
| C-120 | 666 | 51 | 615 | 659 | **AGREE**, DIAL17:7 |

Each arm has8 scenarios /864 requests. The **other prose served counts** also agree: C-60=661; C-150/C-180=666; C-240/C-300=665 (DIAL17:5/8–11; A:10–17). The span666−660=6 is correct.

560–563: C-120−U served=+1, so U is a measured point, not an upper bound. C-120−C-30: served+6, late60+4, timely60+2, timely120+1. **AGREE**. Worst late C-300 example307.3=99.1+208.2 s **AGREE** as model-accounting example, W07:49, ADD N-30.

566–568: M⁺ recovery **cell means**58.6/35.5/13.0/6.6/6.8/2.8/1.7/1.7% at B30/60/90/120/150/180/240/300; C zero at every shown measured level. **AGREE**, W07X:22–29. Fresh R13J means reproduced all first seven levels; B300 is supported here by the saved W07X output, not by a nonexistent fresh R13J subset. Means are not a monotone sequence (6.6→6.8). C/M⁺ service difference is0/0/+1/+2/0/0/0/0, hence never more than2. **AGREE**.

### Main C-120 table, `bang:c4-tran120` (586–599)

Every entry below independently agrees with CXJ per-rider arithmetic and ADD1:12/14/17/19/22/24/136–138.

| Metric | U | C-30 | C-120 | Verdict |
| --- | ---: | ---: | ---: | --- |
| Served | 2,434 | 2,338 | 2,387 | **AGREE** |
| Naive late60 | 203 | 76 | 132 | **AGREE** |
| Naive late120 | 102 | 11 | 21 | **AGREE** |
| Naive late300 | 18 | 0 | 0 | **AGREE** |
| Naive timely60 | 2,231 | 2,262 | 2,255 | **AGREE** |
| Naive timely120 | 2,332 | 2,327 | 2,366 | **AGREE** |
| Shared served | 555 | 313 | 428 | **AGREE** |
| Forecast late60 | 137 | 10 | 65 | **AGREE** |
| Forecast timely60 | 2,297 | 2,328 | 2,322 | **AGREE** |
| Forecast timely120 | 2,347 | 2,338 | 2,379 | **AGREE** |
| Forecast mean extension, s | 7.183331→7.18 | 7.367123→7.37 | 7.273885→7.27 | **AGREE**, pooled over2,434/2,338/2,387 served riders |

609–626: **AGREE** throughout, including denominator/cohort caveats.

- C-120−C-30: served+49; naive late60+56; timely60−7; timely120+39; forecast timely60−6/timely120+41. Extension difference−0.093239 s, so “gần như bằng nhau” is appropriately approximate, not literal equality.
- 9 riders at≥90% of the120 s cap;0 overshoots;0 non-normal in20,435 acknowledged decisions. ADD1:108/121, CXS:60/89.
- Common2,266, C-120-only121, C-30-only72; 121−72=49. Of121,93 also served by U. ADD1:143/147. The explicit rejection of “49 recovered from96” is correct.
- Window8 C-120/C-30 served1,001/975, late6049/15; window17 served871/852, late6020/0. ADD1:155–160. Remaining window7 differences+4 served/+2 late; sums+49/+56.
- Service by cell:23 greater+8 equal+3 lower=34, ADD1:162.
- Across fixed/morning/main C-30→C-120: timely60 changes+6/+2/−7; timely120 changes+29/+1/+39. All numbers at701–703 agree. The universal sentence at704 needs narrowing.

### Cumulative table, `bang:c4-congdon` (735–743)

| Dataset/arm | Runs | Recorded budget prunes | Reported cumulative-only | Served riders with≥2 changes | Verdict/source |
| --- | ---: | ---: | ---: | ---: | --- |
| Main C-30 | 34 | 845 | 0 | 0 | **AGREE**, A:7/FJC:4–6 |
| Morning C at8 levels | 64 | 411 | 0 | 0 | **AGREE**, A:10–17/NEW:1 |
| Main C-120 | 34 | 524 | 3 | 0 | **AGREE**, CXJ/STG/ADD1:127 |
| Snow C-30 | 8 | 163 | 0 | 0 | **AGREE**, SNOW1:10 |
| Total audited subset | 140 | 1,943 | 3 | 0 | **AGREE**, recomputed |

Morning record sum142+106+71+38+26+18+6+4=411. Old main+morning:98 runs,1,256 records,64,371 acknowledged decisions (20,101+44,270). Adding C-120:132 runs/1,780 records/3 cumulative-only. Adding snow:140/1,943/3. **AGREE**, NEW:1, ADD1:132–133, DER1:6.

713–779: **AGREE** on counts and the main counterfactual caveats; clarify caption scope (§5, change8).

- Definition: proposed increment≤B but prior ledger+increment>B. Recorded cumulative-only is a witness classification, not proof that every other validator condition passes. FJC:1–2, CXS:91/101–103.
- Three main C-120 records in three decisions and three w08 scenarios dated14/15/18. Prior/increment/total:25.844+99.027=124.871;58.874+91.584=150.458;105.508+99.301=204.809 s, all against120 s. ADD1:128–130/CXS:95–99.
- The corresponding new requests: rejected/completed/rejected under C-120; the third also rejected under C-30; U served all three. CW21:2–7. The first budgeted incumbent under U really has increments25,844 and99,027 ms, ADD1:115–116. **AGREE**, without equating cross-arm histories with causal identification.
- Fixed factor:2 cumulative-only records/1 decision at C-60;4/3 at C-120; associated requests all eventually served. A:3/5, FJC:34–45. The old fixed runner's full-witness collection is distinct from main fail-fast reporting; NEW:13 and REG A23.
- Synthetic:4 records/3 decisions/1 rejected associated request **after deduplication**. Raw13-run output is6/5/2 (A:6, FJC:46–54); A:20/R15:13 confirms identical repeated w08 artifacts. Draft numbers are the corrected deduplicated result. Add “sau khi bỏ bản chạy trùng” so the saved raw counts do not appear contradictory.
- Three hypothetical30 s changes total90 s: **AGREE**, a definition example, not a simulated result.
- U has12/2,434 repeated riders; cumulative-versus-step archived-trajectory difference4/2,434 at120 s and0 at30/60/300 s. **AGREE**, CVP:14–18 and CXJ. A different policy's trajectories and outcome effect remain **CANNOT CHECK** because the per-step arm was not implemented/run.
- Scope excludes15 calibration runs and16 C-30F forecast-in-dispatcher folders, ADD §0.3. The draft's explicit exclusion at753–756 is correct.

## 4. Figure audit

For `hinh:c4-tran` (629–699), all data points, tick values, axis mappings and the out-of-frame FREE annotation agree. These are counts, not percentages.

| Panel / point | Measured (served,late60) | Recomputed local coordinate (cm) | Verdict |
| --- | --- | --- | --- |
| (a) C-30 | (1,534,0) | (0.24,0) | **AGREE** |
| (a) C-60 | (1,540,0) | (0.60,0) | **AGREE** |
| (a) C-120 | (1,563,23) | (1.98,1.15) | **AGREE** |
| (a) U | (1,584,47) | (3.24,2.35) | **AGREE** |
| (a) FREE, annotation only | (1,629,274) | would be(5.94,13.70), outside panel | **AGREE**, caption discloses omission |
| (b) C-30 | (660,47) | (0.72,2.35) | **AGREE** |
| (b) C-90 | (664,50) | (2.16,2.50) | **AGREE** |
| (b) C-120 | (666,51) | (2.88,2.55) | **AGREE** |
| (b) U | (665,50) | (2.52,2.50) | **AGREE** |
| (c) C-30 | (2,338,76) | (0.54,0.95) | **AGREE** |
| (c) C-120 | (2,387,132) | (2.01,1.65) | **AGREE** |
| (c) U | (2,434,203) | (3.42,2.5375), drawn2.54 | **AGREE**, harmless plotted rounding |

Panel(a): x=(served−1,530)×0.06, y=late×0.05; ticks1,530/1,550/1,570/1,590 and0/20/40/60. Panel(b): x=(served−658)×0.36; ticks658/660/662/664/666/668 and0/20/40/60. Panel(c): x=(served−2,320)×0.03, y=late×0.0125; ticks2,320/2,360/2,400/2,440 and0/80/160/240. All agree. Offsets5.3/10.6 cm affect layout, not measurements.

Separate panels/scales correctly prevent pooling different experimental sets. Panel(b)'s four selected points do not show all tested levels. Its caption already says this; add that connecting lines are visual guides between measured points, not a continuous response or a Pareto frontier.

**CANNOT CHECK:** rendered widths, labels colliding, page placement, page budgets, bibliography/reference resolution after assembly, or compile success. No build/render was authorized. NOTES' page estimates are explicitly estimates; no statement here certifies their12.9–14.2-page projection or actual typesetting.

## 5. Ranked required changes — exact Vietnamese replacements

### 1. Restore the conditions of the no-op argument and fix the recovery metric

**308–311:** observed zero recovery is correct; “luôn qua” without N and admissible prior ledger is not. A zero added dispatch amount cannot repair an already-invalid ledger or a physically invalid reference route. Keep observed and proved statements separate.

Replace the relevant passage with:

> Trên cả 34 kịch bản đã chạy, luật C không có quyết định nào phải phục hồi và không khách nào vượt trần. Theo Nhận xét~\ref{nx:giunguyen}, nếu phương án giữ nguyên được bộ sinh dựng ra và qua mọi kiểm tra không thuộc luật C (điều kiện N), đồng thời phần trần đã dùng của mọi khách đã nhận nằm từ 0 đến giới hạn B, phương án này không làm tăng phần dời do điều phối nên vẫn qua kiểm tra trần của luật C. Kết quả đo ở đây phù hợp với tính chất có điều kiện đó; nó không bảo đảm giờ trả thực tế hay tính khả thi vật lý trong mọi tình huống. Luật hạn chót so giờ trả mới với lời hứa đầu, nên riêng phần thay đổi khi giữ nguyên kế hoạch cũng có thể làm phương án giữ nguyên không qua kiểm tra hạn chót.

**188–190:** replace the definition and aggregation cells with:

> Lượt quyết định được bộ chạy xác nhận có chứng thư ghi nhận việc chọn phương án phục hồi, ngoài chế độ vận hành bình thường (mục~\ref{muc:doichung}).

> Trong từng kịch bản, chia số lượt quyết định này cho tổng số lượt quyết định được bộ chạy xác nhận; sau đó lấy trung bình không trọng số theo kịch bản. Số gộp ghi riêng.

Evidence: REG A10/A21/A22 and draft Chapter3:324–338's conditional statement; HVA:247–279; POL:448–462; IV:47–51. Do not say “the rule rejects all plans” as the operational definition.

### 2. Remove the unsupported exclusive “structural only” explanation

**469–474:** replace with:

> Dưới trần 30 giây, 1.334 yêu cầu bị từ chối. Trong số đó, 148 yêu cầu cuối cùng bị từ chối có ít nhất một phương án mang bản ghi chặn do trần giờ trả của một khách đã nhận; điều phối không trần phục vụ 116 trong 148 yêu cầu này. Với 1.186 yêu cầu còn lại, không tìm thấy bản ghi chặn do trần trong các phương án được ghi lại. Nhóm này không chứng minh rằng mọi cách ghép đều không khả thi hay rằng yêu cầu chỉ bị từ chối vì các ràng buộc cấu trúc. Các số đếm theo yêu cầu ở đây tính theo từng cặp kịch bản và yêu cầu. Trên tập chính, 845 bản ghi chặn liên quan đến 643 cặp như vậy; 495 cặp cuối cùng vẫn được phục vụ bằng phương án khác.

Evidence: BUD:2–5; BUDPY:29–44; REG D16/K10. Correct REG D13 and NOTES §3 item8 as well; merely repeating the register's label is not sufficient.

### 3. Correct the unit of “2 of148” and disclose the selected-record rule

**477–481:** replace with:

> Với 148 yêu cầu bị từ chối có bản ghi chặn, mức vượt trần nhỏ nhất được ghi có trung vị 109,6 giây và lớn nhất 524,8 giây. Với mỗi yêu cầu, phép phân tích chọn bản ghi có mức vượt nhỏ nhất; ở 2 trong 148 bản ghi được chọn, ít nhất một khách đã nhận được nêu trong bản ghi đã dùng một phần trần trước quyết định đó. Đây là số đếm theo yêu cầu mới, không phải số khách đang trên xe khác nhau. Trong các bản ghi chặn được kiểm ở mức 30 giây, lần dời đơn lẻ đã vượt trần. Nếu chỉ đổi giới hạn của phép sàng lọc thành 120 giây, 59 trong 148 yêu cầu có ngưỡng ghi lại không vượt giới hạn mới. Vì bộ kiểm dừng ở lỗi gặp trước và quỹ đạo sẽ đổi khi trần đổi, phép sàng lọc này không cho biết 59 yêu cầu đó có được phục vụ hay không.

Evidence: BUDPY:22/35–42/51–52; BUD:6–10. “Before>0” is for a witness in the selected minimal-overshoot candidate, not every possible blocking candidate. Correct REG D19 and its downstream wording.

### 4. Separate FREE's policy change from the cap ladder

**526–528:** replace with:

> Ghép tự do và điều phối không trần ở bảng này khác chính sách chọn phương án và việc kiểm tra cam kết, nên chênh lệch giữa hai cấu hình không chỉ là tác động của mức trần. Trong nhóm giữ cùng chính sách cam kết, giảm trần từ 120 xuống 60 giây làm số lượt phục vụ giảm từ 1.563 xuống 1.540 và số lượt trễ quá 60 giây giảm từ 23 xuống 0; hai mức 60 và 30 giây đều không có lượt trễ quá 60 giây trên tập này. Tập tắc đường cố định dùng bộ chạy cũ không có luật phục hồi, nên các số đo này không chuyển sang tập kiểm tra chính.

Evidence: 137–140's already-correct distinction; NEW:11–13, LAD:2–6, WP17:9/14/19, REG A17/B17/K50. Avoid implying that FREE is C at an infinite cap or locating an unmeasured threshold between60 and120.

### 5. Make the morning configuration list and run count refer to the same subset

**124–126:** use this table row (the existing “Như tập chính” runner cell can remain):

> Tập chỉnh trần buổi sáng & 8 kịch bản, 864 yêu cầu & 12--13/11/2018; khung 7 giờ & U; C và M$^{+}$ ở 30, 60, 90, 120, 150, 180, 240 và 300 giây & Như tập chính & 136 trong 192 lần chạy lưu trữ\\

Add after the table:

> Tập buổi sáng có 192 lần chạy lưu trữ, gồm cả các cấu hình không được so ở đây; 136 lần chạy tương ứng với điều phối không trần và hai luật C, hạn chót ở tám mức trần được liệt kê.

Evidence: `run_w07.py`:33–34; `run_w07x.py`:35–37; 8×(1+8+8)=136; 88+104=192. Alternatively list all24 arms and label192 as the whole experiment, but do not leave the current inconsistent row.

### 6. State that the mechanism example concerns an ETA projection

**459–466:** replace the start with:

> Một ví dụ trên tập chỉnh trần buổi sáng cho thấy hai luật khác nhau ở đâu. Ngay trước quyết định ghép thêm, giờ trả đang được dự kiến của một khách trên xe muộn hơn lời hứa đầu 79,0 giây; theo sổ, độ dời này hoàn toàn thuộc phần thay đổi khi giữ nguyên kế hoạch, còn phần đã dời do điều phối bằng 0. Phương án ghép thêm đề xuất một lần dời do điều phối 68,3 giây. Ở mức 90 giây, luật hạn chót loại phương án vì giờ trả dự kiến mới muộn hơn lời hứa đầu khoảng 147 giây; luật C cho qua kiểm tra trần giờ trả vì phần do điều phối là 68,3 giây.

Keep the existing three-divergence and same-state/model caveats after that. W07XM:6/11/16 measures ledger/projected ETA displacement; it is not an observed arrival-time difference while a rider is still onboard.

### 7. Finish rate reporting without turning cell means into pooled percentages

The caption of `bang:c4-nghiavu` already labels the means correctly. Add counts/denominators separately; show the per-scenario numerator/denominator pairs in the evidence appendix if retaining every cell-mean rate under the brief's literal rule. A single pooled count pair is **not** the numerator/denominator of an unweighted mean.

Exact explanatory text:

> Hai cột tỉ lệ lấy trung bình không trọng số của tỉ lệ từng kịch bản; mẫu số trong từng kịch bản lần lượt là số lượt quyết định được xác nhận và số khách được phục vụ. Các số đếm gộp được trình bày riêng và không được dùng thay cho trung bình theo kịch bản.

For the existing M⁺-30 pooled paragraph, keep7,710/20,103 and289/2,338. Newly verified M⁺-60/V counts in §3 need register rows before inclusion.

For the last dispatch-table row add:

> Với nhóm khách trễ quá 60 giây, tỉ lệ cuối bảng bằng tổng phần dời có dấu do điều phối chia tổng số giây trễ của chính nhóm đó. Hai tổng lần lượt là 23.027,239 trên 31.353,407 giây khi không trần; 81,742 trên 6.891,526 giây ở trần 30 giây; và 4.836,281 trên 12.450,223 giây ở trần 120 giây.

For fixed-factor exposed rates, add actual counts388/1,629,62/1,584,41/1,563,20/1,540,6/1,534. For shared rates obtain actual numerators; do not infer them from rounded53.1/21.8/19.4/17.3/15.7%. Morning M⁺ rates also need per-scenario count support or a referenced appendix. Do not pretend the percentage rounding is a numerical error.

Replace151–152's first sentence with:

> Các lượt trễ và tới sớm được đếm trong nhóm khách được phục vụ, so với lời hứa đầu. Số lượt không trễ bằng số lượt phục vụ trừ số lượt trễ; tỉ lệ không trễ trên yêu cầu chia số này cho toàn bộ yêu cầu, kể cả yêu cầu bị từ chối.

### 8. Put the audited scope in the cumulative table's caption and disclose deduplication

**726–727:** replace caption with:

> Kiểm toàn bộ bản ghi chặn do trần trên 140 lần chạy có luật C đã được kiểm, dùng hệ số tắc đường đo và thuộc bốn nhóm liệt kê dưới đây. Một bản ghi ứng với một phương án bị loại, không phải một khách. Kết quả không bao gồm các lần chạy hiệu chỉnh và các lần đưa dự báo vào bộ điều phối chưa được kiểm.

Keep the exclusions at753–756. Title “kiểm toàn bộ” must mean all recorded prunes **within these audited runs**, not all C runs or every possible blocker.

**770–771:** replace the synthetic sentence with:

> Ở một kiểu tắc đường tự tạo, sau khi bỏ bản chạy trùng, có 4 bản ghi chỉ do cộng dồn trong 3 lượt quyết định ở trần 120 giây; 1 yêu cầu mới liên quan cuối cùng bị từ chối.

Evidence: ADD §0.3/SNOW1:10/DER1:6; A:6/20 and R15:13. Do not switch back to raw6/5/2 or imply the cumulative part caused a rejection.

### 9. Resolve factual register gaps and date the archive count

WRITING-BRIEF requires a register row for **every factual sentence**. NOTES:59–69 acknowledges external-code facts being used before they have rows. A correct fact-check or `X3-xx` comment is evidence, but it is not compliance with that explicit register rule.

Register GEN's batch limit; archived runner/recovery identities; the historical30 s anchor; fixed full-witness collection; and the mechanism interpretation. Correct A24, D13 and D19. Keep snow runner identity unverified unless it is independently established; the current “Chưa kiểm lại” cell is honest.

**143–145:** replace with:

> Mỗi lần chạy là một cặp kịch bản và cấu hình; lần chạy hỏng được thay bằng bản chạy lại hoàn tất (Phụ lục~\ref{phuluc:C}). Bản kiểm kê ngày 08/10/2026 ghi nhận 1.991 bản ghi lần chạy trong kho dữ liệu; chương này chỉ dùng các tập được liệt kê ở Bảng~\ref{bang:c4-taptu}.

At105, prefer “không dùng để tính các kết quả chính dưới đây” to “không dùng ở đây”: the later full chapter may cite audits/calibration quantities involving those15 scenarios. This is a scope clarification, not an instruction to mix calibration outcomes into main results.

### 10. Narrow the universal cap conclusion and mark discrete plotted points

**704–706:** replace with:

> Giữa hai mức 30 và 120 giây, mức 120 phục vụ nhiều hơn nhưng cũng có nhiều lượt trễ quá 60 giây hơn trên cả ba tập. Số lượt không trễ phụ thuộc ngưỡng và tập kịch bản. Mức 120 giây được chọn sau khi xem các tập phát triển, nên kết quả trên tập chính là một điểm đo thêm trên đường đánh đổi, chưa xác định được mức trần tốt nhất theo một tiêu chí chung.

Evidence: the three endpoint differences in §3. The original “Không mức trần nào tốt hơn ở mọi tiêu chí” quantifies beyond the demonstrated pair/criteria; different levels can tie and some measured metrics need not trade off.

At the figure caption add:

> Đường nối chỉ giúp theo dõi các điểm đã đo được chọn để vẽ; không biểu diễn kết quả ở các mức trần chưa chạy.

This preserves the verified figure and its separate panels without presenting a continuous or optimal frontier.

## 6. Honest padding answer and part-B handoff

The specified draft is **part A**, so I do not require it to duplicate §4.8's padding table. Its links to `muc:c4-dem` are appropriate. I checked the underlying PAD/A/ADD1 values to make sure part A's trade-off argument can connect to the required honest answer.

| Quote replay, all34 scenarios | Served | Late60 | Timely60 /3,672 | Timely120 /3,672 | Early60 /served | Mean extension, s |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| U + forecast | 2,434 | 137 | 2,297 | 2,347 | 8/2,434 | 7.183331 |
| C-30 + forecast | 2,338 | 10 | 2,328 | 2,338 | 4/2,338 | 7.367123 |
| C-120 + forecast | 2,387 | 65 | 2,322 | 2,379 | 2/2,387 | 7.273885 |
| U + forecast +30 s | 2,434 | 106 | 2,328 | 2,366 | 44/2,434 | 37.183331 |
| C-30 + forecast +30 s | 2,338 | 2 | 2,336 | 2,338 | 44/2,338 | 37.367123 |
| U + forecast +60 s | 2,434 | 87 | 2,347 | 2,386 | 1,033/2,434 | 67.183331 |

**AGREE**, A:7–9, CXJ, PAD:12–15/33–36, ADD1:14–16/19–21/24.

Recomputed: padded U ties C-30 timely60 at2,328, exceeds timely120 by28, and serves96 more. Its extension is37.183331/7.367123=5.047198 times the C-30 extension. Within±60 s: C-30 forecast2,338−10−4=2,324; padded U2,434−106−44=2,284. Padded-U late120/300/600=68/11/1 versus C-30 forecast0/0/0. C-120 forecast timely120 exceeds padded U by13 while serving47 fewer and extending quotes7.273885 s versus37.183331 s. These are comparisons of **different served cohorts**, not the effect of quote padding on a common randomized population.

Part B must retain these limits from R15/R18/R21B/RD §8:

- Padding is a competitive option; C does not beat it in timely-per-request at every threshold.
- Padded U replays U's trajectories and retains its174 exposed riders/12 repeated riders/max590.133 s; quote padding does not enforce C's dispatch ledger.
- “Same quote extension” should mean **similar measured mean extension** or the same added padding rule, not literally identical rider-level promises. The two served cohorts and original promises differ.
- No evidence values shorter promises or the ledger bound enough to justify96 fewer rides or242 fewer shared completions economically.
- Stability-first selection remains part of the measured dispatcher; no cost-first full-trajectory experiment establishes that these findings survive a different selector.
- The ledger's terms are model accounting; no physical traffic-causality or unconditional arrival-time guarantee follows.

The current part-A text correctly preserves most of these caveats. They should survive editing.

## 7. My own correction and remaining unverified claims

**I withdraw my earlier R23 acceptance of “2 new requests per vehicle.”** Reading GEN:74–79 and98–107 confirms the cap applies once to the pending batch, before looping over vehicles. The supplied Round25 line90 is correct; REG A24 and my earlier acceptance need correction. I did not alter either old file.

I retain the R15/R18/R21B distinctions between counts of non-normal acknowledged certificates, typed incident entries, rider counts, candidate-prune records, and request-scenario associations. In particular7710 is not the number of incident entries or affected riders;3 cumulative-only records are not three proved lost trips.

**CANNOT CHECK / not demonstrated:** full-counterfactual rejection causes; all constraints for every unrecorded candidate; outcome effects of replacing cumulative C with a per-step cap; an optimal/business-valued B; an upper bound from U; safety on unaudited C runs; current1,991-file inventory completeness; snow runner/recovery identity; exact fixed shared-count numerators in the cited rounded output; final rendered page/figure layout. None of these gaps requires new simulations to make the wording honest. The required corrections can be made using the existing evidence.

**Top five required changes:** (1) conditional no-op proof and recorded recovery definition; (2) remove “structural only”; (3) make2/148 a selected-record count per rejected request; (4) separate FREE's policy change from varying C's cap; (5) distinguish136 listed morning runs from192 archived runs.
