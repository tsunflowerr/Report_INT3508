# Outline proposal for the thesis rewrite (structure editor: Claude), 2026-10-10

**Task.** Turn the current 105-page thesis (`E:/Code/Report_INT3508/ridebound/main.pdf`, files dated 30 Sep 2026)
into a ~70–79-page thesis built on the storyline agreed in rounds 13–18. That storyline is: a pooled rider's promised
drop-off time drifts for three causes, and each cause is handled in its own place. Rule C caps the dispatch part. A
forecast puts anticipated traffic into the first quote. A per-rider ledger records the rest.

**What I read.**
- In full: `main.tex`, all eleven files in `noi-dung/`, the TOC/LoF/LoT pages of `main.pdf` (via `pdftotext`).
- The R17 verdict (all of it), R18 (all), R13 (all), R15 (all), and the handoff `BAN-GIAO-PHIEN-2026-10-09.md`.
- `T38-REPORT.md`, `FORECAST-REPORT.md`, `W07X-REPORT.md` and `tang3/t38c120/C120-PLAN.md` (Stage 1a).
- The evidence files cited in §2.10, by line.
- From the owner's DACN report (`C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`, 50 pages): the
  front pages, the TOC/LoF/LoT, chapter 1 and the start of chapter 4.

**What I did not do.** No simulation, build, install, deletion, or edit. I wrote nothing except this file.

**Conventions.**
- `05:64-69` means `ridebound/noi-dung/05-chuong1.tex`, lines 64–69.
- "p. 12" is the printed (Arabic) page number. PDF page = printed page + 16.
- Anchor keys (A, T38, FR, CAP, LAD, …) are listed in §2.10.

---

## 0. Summary

| Part | Now (pages) | Proposed (pages) |
|---|---:|---:|
| Front matter (2 covers, cảm ơn, tóm tắt + abstract, mục lục, DS hình/bảng, viết tắt) | 16 (PDF 1–16) | 10 |
| Ch. 1 Đặt vấn đề | 9 (pp. 1–9) | 7 |
| Ch. 2 Cơ sở lý thuyết | 6 (pp. 10–15) | 6 |
| Ch. 3 Phương pháp | 17 (pp. 16–32) | 12 |
| Ch. 4 Thực nghiệm và đánh giá | 46 (pp. 33–78) | 27 |
| Ch. 5 Kết luận | 7 (pp. 79–85) | 4 |
| Tài liệu tham khảo | 4 (pp. 86–89) | 4 |
| Phụ lục (optional) | 0 | 4 |
| **Total** | **105** | **74** (70 without the appendix) |

These five cuts save the most pages:
1. **The four-family theorem machinery** (ch. 3 §3.5; `07:175-675`, pp. 19–29, ~11 pp.). It becomes a ~1-page remark
   in §3.3, plus an optional 1.5-page appendix.
2. **The Tier-2, drift-injection and synthetic-sweep experiments** (ch. 4 §4.7–4.9; `08:685-1556`, pp. 45–63,
   ~19 pp.). The T3.8 frontier, which the current thesis does not contain, replaces them.
3. **The side investigations** (ch. 4 §4.10–4.12 and §4.14–4.15; `08:1558-1866`, `08:1899-2206`, pp. 64–69 and
   70–76, ~13 pp.). These are the window-cap test and price surface, the FA re-measurement, the welfare break-even, the
   promise-aware generator and the abandoned directions.
4. **The static-panel apparatus** (ch. 4 §4.2–4.6; `08:140-683`, pp. 36–44, ~9 pp.). It shrinks to ≤ 0.5 page in
   §4.3, plus a 2-page appendix.
5. **The cross-domain frames in ch. 2 and the long future-work list in ch. 5.** These are MRP nervousness, the legal
   obligation of means vs result, and online control (`06:136-187`, `06:210-249`, pp. 13–15). The 10-item future-work
   list is `09:130-211`, pp. 82–83. Together ~5 pp.

---

## 1. Audit of the current thesis

### 1.0 Page map (from the PDF TOC, verified with `pdftotext`; 105 PDF pages = 16 front + 89 body)

| File | Lines | Pages |
|---|---:|---|
| 00-bia | 71 | PDF 1–2 (VN cover, EN cover) |
| 01-loi-cam-on | 24 | i |
| 02-tom-tat | 100 | ii–v (Tóm tắt ii–iii, Abstract iv–v) |
| 03-muc-luc | 10 | vi–xii (TOC vi–ix, LoF x, LoT xi–xii) |
| 04-viet-tat | 62 | xiii–xiv |
| 05-chuong1 | 314 | 1–9 |
| 06-chuong2 | 249 | 10–15 |
| 07-chuong3 | 758 | 16–32 |
| 08-chuong4 | 2,271 | 33–78 |
| 09-chuong5 | 231 | 79–85 |
| 10-tai-lieu | 168 | 86–89 |

Verdict key:
- **KEEP**: reuse with light edits.
- **REWRITE**: the topic stays but the text is replaced.
- **CUT**: drop.
- **APPX**: move to the appendix.

D# refers to the overclaim rows of R17 §D (`R17-FINAL-VERDICT.md:738-758`). X# refers to the additional problems I
found (§1.9).

### 1.1 Front matter

| Location | Pages | What it says | Verdict | Why |
|---|---|---|---|---|
| 00:1-33 VN cover | PDF 1 | Title "LỜI HỨA CÓ BIÊN ĐƯỢC CHỨNG NHẬN TRONG ĐIỀU PHỐI XE ĐI CHUNG THEO YÊU CẦU" (00:15-16). Supervisor "[chờ bổ sung]" (00:28) | KEEP | The supervisor's name is UNKNOWN. Do not fill it in; "ThS. Trần Mạnh Cường" is the supervisor of a different course, DACN. The title is an owner decision (§4.3) |
| 00:35-69 EN cover | PDF 2 | English title (00:51-52); "[to be filled]" (00:64) | KEEP or CUT | The owner's rule is "Vietnamese only", but UET templates may require an English cover (UNCONFIRMED). The DACN report has one. Decision §4.3 |
| 01:1-24 Lời cảm ơn | i | Thanks an unnamed "thầy cô hướng dẫn" (01:4). "hơn năm trăm lần chạy" (01:16). Much of the report is about abandoned directions (01:17-19) | REWRITE (light) | The run count is outdated (the inventory has 1,991 runs). After the cuts, 01:17-19 is no longer true |
| 02:4-47 Tóm tắt | ii–iii | Problem, mechanism, four-family theorem, 558 + 546 runs, 89.06%, 19/20, preregistered 98/102, deadline breaks 10–19% / 24% / 7.3%, keywords | REWRITE (complete) | Contains D1 (02:6-10), D2 (02:17-20), D3 (02:22-26), D4 (02:14-16), D9 (02:28-30), D10 (02:46-47) and D11 (02:43). Talks about preregistration (02:33-38). No T3.8 number (D18). The run count disagrees with 08:99-111 (X1) |
| 02:51-98 Abstract | iv–v | English mirror of the same text | REWRITE or CUT | The same issues (D1–D4, D9–D11 at 02:56-59, 02:66-69, 02:71-75, 02:63-66, 02:78-80, 02:94, 02:97-98). "Sealed/preregistered" at 02:78 and 02:84. Decision §4.3 |
| 03:1-10 TOC / LoF / LoT | vi–xii | Generated automatically; `tocdepth=2` (main.tex:62) | KEEP | It shrinks with the content. Expect about 2 + 2 pages |
| 04:8-27 abbreviations | xiii | ODRP … pp. Includes MPS/MRP (04:19-20), VOT/VOR (04:21-22) | REWRITE | MPS/MRP only serve the cut §2.3. Add the rule names (U, C-B, M⁺-B, V-B, FREE) |
| 04:33-60 symbols | xiii–xiv | v, e, p; d = \|e−v\|, A = \|p−e\|, B = \|p−v\|; C, X, V, E, M, M⁺, D⁺; β cap, κ, ℓ, Ω, Δ, k | REWRITE | The notation clashes with the agreed one (c = p − e, budget B; R17 FP:31-33). In the thesis "B" means \|p − v\| (04:45-46) and "β" means the cap (04:53). See X2 |

### 1.2 Chapter 1 (`05-chuong1.tex`, pp. 1–9)

| Location | Pages | What it says | Verdict | Why |
|---|---|---|---|---|
| 05:3-49 §1.1 Bối cảnh | 1–2 | RTV, Alonso-Mora 98%. The re-quote example 9:10 → 9:13 → 9:11 → 9:16 (05:21-24). "trong dòng bài điều phối kinh điển, chuỗi ấy không được ghi nhận" (05:24-29). Demand-side value: Alonso-González, Geržinič, Bansal (05:31-40). The guiding question (05:46-49) | REWRITE | Keep the opening idea (05:5-19) and the demand-side paragraph after trimming (05:31-40). 05:24-29 needs D1-style scoping: FA 2020 measured and controlled the drift. Replace the invented example with the real rider (§2.3) |
| 05:51-82 §1.2 Hạn chế | 2–3 | Four "systemic" limitations: passengers as constraints, with a 573 s static-panel example (05:58-62); no cause attribution, "không ai tách" (05:64-69); no conduct metric (05:71-73); MRP not transferred (05:75-82) | REWRITE → new §1.2 "Ba nguyên nhân" | D5 (05:64-69) is false given HZ-B. D6 (05:71-73, 75-82). The MRP frame is cut |
| 05:84-194 §1.3 Chỗ đứng | 3–5 | FA 2020 (05:90-113). Elmi 2026 (05:115-140). S&P 2026 (05:142-148). Other works (05:150-158). Design-space list with "cách duy nhất" (05:160-172). Box "Chỗ khác biệt chứng minh được" (05:174-182). Preregistration paragraph (05:184-188). "Tính sổ theo cái gì" (05:190-194) | REWRITE | **Hörl & Zwick 2022 is not cited** (D19, K3). D7 (05:99-104) is a strawman, which 05:106-111 itself concedes. D3 (05:169-171, 174-182). Preregistration talk violates the owner's rule. The "99,8%" comparison with Elmi is a package comparison (05:136-140, X5). Reusable facts: 05:90-97, 05:105-133, 05:142-158 |
| 05:196-271 §1.4 Mục tiêu và đóng góp | 6–7 | Three objectives (05:198-208). Six contributions: ledger + "291<300…" (05:213-217); four-family theorem + Tier-2 numbers (05:219-242); three-anchor decomposition + 89.06% (05:244-248); cost curve 0.17% / 7.13 pp (05:250-253); nine measures (05:255-259); FA 49% (05:261-264). Disclaimer (05:267-271) | REWRITE (replace with §3 of this file) | D3, D4 (05:213-217), D9 (05:244-248), D11 (05:241), D12 (05:250-253), D13 (05:261-264), D8 (05:267-271). Every listed result is on the static or Tier-2 panels. T3.8 is missing (D18) |
| 05:273-290 §1.5 Phạm vi | 8 | Static panel 08:00–10:00, 14–18 Nov; 108 requests / 8 vehicles; metric-closure network | REWRITE | The main panel is now T3.8 (34 cells, windows 7–9 / 8–10 / 17–19 h). Keep the scale caveat (05:285-290) |
| 05:292-314 §1.6 Cấu trúc | 8–9 | Chapter map; mentions MRP, legal frames, "chứng cứ niêm phong" (05:307) | REWRITE | New structure; no sealing talk |

### 1.3 Chapter 2 (`06-chuong2.tex`, pp. 10–15)

| Location | Pages | What it says | Verdict | Why |
|---|---|---|---|---|
| 06:3-10 intro | 10 | Four knowledge groups, including MRP, legal and online control | REWRITE | Those groups are cut |
| 06:14-30 §2.1.1 Phát biểu | 10 | Dynamic DARP, Ω and Δ windows | KEEP | Standard background |
| 06:32-55 §2.1.2 RTV | 10–11 | Two-stage RTV; ILP eqs. 2.1–2.3 | KEEP | Background that the owner's DACN style also has |
| 06:57-78 §2.1.3 Thiệt hại khách cũ | 11 | Fielbaum 2022 cost term (soft, marginal, aggregated); "mười bốn phút" static example (06:76-78) | REWRITE (shorten) | Keep the formula as the "soft penalty" contrast. Drop the static-panel example |
| 06:82-107 §2.2.1 Công trình gần nhất | 12 | FA 2020 definitions Δt_w, Δt_d, NC and results | KEEP (light) | Add their §6 control (see 05:106-111) |
| 06:109-134 §2.2.2 Ba giới hạn | 12–13 | (1) endpoints vs path (06:113-119); (2) "về mặt toán học không thể trở thành ràng buộc" (06:121-127); (3) traffic deliberately excluded (06:129-134) | REWRITE | (1) KEEP, with D13 wording. (2) is the D7 strawman again but is **not in R17 §D** (X3), so CUT it. (3) KEEP: FAM:571-576 confirms it |
| 06:136-160 §2.3 MRP | 13 | Production-planning nervousness, Sridharan freeze | CUT | Not in the storyline. It only supported the nine-measure robustness test, which is also cut |
| 06:162-187 §2.4 Nghĩa vụ phương tiện / kết quả | 13–14 | Legal analogy; "Điểm mới nằm ở chỗ … tính được ranh giới đó" (06:184-187) | CUT | The same overclaim as D14, again **not in R17 §D** (X4). At most one sentence of interpretation in ch. 5 (decision §4.3) |
| 06:189-208 §2.5 Giá trị độ tin cậy | 14 | VOT/VOR coefficients; 20–25 EUR/h "chưa đối chiếu được với bản gốc" (06:203-208) | REWRITE (0.5 p.) | Unverified source (D16). Replace with the R15 correction-6 wording (different constructs) |
| 06:210-249 §2.6 Điều khiển trực tuyến | 15 | Online-control vocabulary; table bang:dieukhien (06:225-240) | CUT | Supports the two-basis framing, which is no longer central |

### 1.4 Chapter 3 (`07-chuong3.tex`, pp. 16–32)

| Location | Pages | What it says | Verdict | Why |
|---|---|---|---|---|
| 07:3-6 intro | 16 | Chapter roadmap | REWRITE | New structure |
| 07:8-45 §3.1 Tổng quan + Fig. 3.1 (TikZ, 07:24-45) | 16 | Ledger, counterfactual e, decision loop | KEEP the figure with edits. REWRITE the text | Add the forecast-quote and ledger boxes; β → B. The only reusable figure besides the logo |
| 07:47-71 §3.2 Mô hình mở rộng | 17 | Open promise, three stages, ten commitment dimensions, the main config | KEEP (light) | Needed to define U (locks) and C |
| 07:76-119 §3.3.1 Định nghĩa ba mốc | 17–18 | v, e, p; A, d, B; symmetric charging (07:103-112); static stats 479/11 (07:114-119) | KEEP with the notation change | Switch to x, c, z and budget B. Drop the static statistics or move them to the appendix |
| 07:121-149 §3.3.2 Ví dụ | 18–19 | 9:10 / 9:10:40 / 9:11:10 table (07:126-140); do-nothing under the outcome basis | KEEP | A good example for an outside reader |
| 07:151-173 §3.4 Sổ cái | 19 | L_after = L_before + δ; hard filter before the ILP; "Ba đặc điểm … chỗ khác biệt so với văn liệu" (07:168-173) | REWRITE | X6: per-rider protection is prior work (D03:211-213), and HZ also uses hard routing constraints (HZ:575-588). Add R18's all-trip budget wording |
| 07:178-191 §3.5.1 Hai cơ sở | 19–20 | Conduct vs outcome basis; "nghĩa vụ phương tiện" | REWRITE | Present C and V as rules (V as a comparator) without the legal frame |
| 07:193-203 §3.5.2 Bất biến no-op | 20 | The do-nothing plan always exists; p(no-op) = e | KEEP | The base of Remark 3.1 |
| 07:205-281 §3.5.3 Phân rã cộng tính, độ khít | 20–21 | B ≤ A + d; per-publication tightness table (07:231-252); d invariance on the static panel | CUT (or APPX ≤ 0.5 p.) | Static-panel technicality. The new text uses the exact signed identity z = x + c (07:427-430) |
| 07:283-413 §3.5.4 Ba định lý | 22–24 | Th. 3.1: the conduct basis never removes the no-op (proof 07:292-297). Th. 3.2: the outcome basis can be infeasible. Th. 3.3: subset result under (H), with table 07:350-367; (H) fails 228 times (07:375-379). Corollary on the band (07:397-413) | Th. 3.1 → a Remark in §3.3. Th. 3.2 → one sentence. Th. 3.3 → CUT | D3: true by construction. Th. 3.3 is conditional on (H), which the panel violates, and the T3.8 storyline does not use it |
| 07:415-594 §3.5.5 Khung bốn họ cổng | 24–27 | Table bang:hocong (07:463-478); Proposition chain (07:440-457); Theorem 3.4 (07:501-527); corollaries on deterministic time and drift direction (07:544-594) | APPX (≤ 1.5 p.) or CUT | Outdated Tier-2 framing. An HZ-style max(p0 + B, e) shares the property [R17 R6]. Keep only the "what each rule checks" table, inside §3.4 |
| 07:596-634 §3.5.6 Chuỗi vs hai đầu | 28 | Pure-insertion proposition; static statistics | CUT | Not needed |
| 07:636-675 §3.5.7 Phản ví dụ | 29 | CE-1…CE-6 (07:641-663); preregistration talk (07:671-675) | KEEP CE-2 and CE-3 in §3.3. Rest → APPX | CE-2: C does not bound what the rider sees. CE-3: C charges a restoring correction. Both are honest limits (D03 §11). Remove the preregistration talk |
| 07:677-693 §3.6 Bảo vệ bổ sung | 30 | Hard locks, freeze horizon, ratchet | REWRITE | Keep the locks, which define U. Cut freeze and ratchet (their result is cut) |
| 07:695-724 §3.7.1 Phân tầng | 30–31 | C#/.NET layers; table bang:kientruc (07:702-720); FleetPy 1.0.2 (07:722-724) | KEEP | Fix X7: "chín dự án" (07:699) but the table lists 7 rows (07:711-717). Re-count the line numbers (UNCONFIRMED as current) |
| 07:726-737 §3.7.2 Sinh phương án chèn | 31 | Insertion only; decisionMovedEarlier = 0; delay certificate | KEEP (light) | Needed to explain c ≥ 0 |
| 07:739-758 §3.7.3 Chứng cứ niêm phong | 31–32 | Transcripts with SHA-256 per frame, semanticHash, runner hash; ratchet anecdote | REWRITE as "Tái lập và kiểm chứng" | Owner rule: no talk of sealing. Keep the hashes as reproducibility; drop the anecdote |

### 1.5 Chapter 4 (`08-chuong4.tex`, pp. 33–78)

| Location | Pages | What it says | Verdict | Why |
|---|---|---|---|---|
| 08:3-36 roadmap table | 33 | Claims → sections | CUT | Contains D9 (08:16-17), D3 (08:20) and preregistration talk (08:24-26). Replace with a 4-line chapter map |
| 08:41-72 §4.1.1 Dữ liệu | 33–34 | FleetPy Manhattan; 20-cell static panel; table bang:thamso (08:49-68) | KEEP the table (update). REWRITE the text | The main panel is now T3.8 |
| 08:74-124 §4.1.2 Quy mô | 34–35 | bang:quymo: 558 + 685 = 1,243 runs, 79.15 GB (08:99-111); counting rules (08:116-124) | REWRITE | X1: this disagrees with 02:27-28 and 09:34 (558 + 546). Report only the panels actually used |
| 08:126-138 §4.1.3 Cấu hình | 35 | B1 = free; C1 = 30 s + locks + fixed pickup | REWRITE → naming table | One table for U / FREE / LOCKS / B1 / C1 / C-B / M⁺-B / V-B (X8) |
| 08:140-327 §4.2 Quy trách | 36–38 | 89.06% (bang:quytrach 08:151-171); natural control (08:180-195); concentration, 840.9 s (08:197-230); tail and Gini trap (08:232-284); Elmi shape claim (08:269-272); tightness (08:286-327) | ≤ 0.5 p. in new §4.3 + APPX A (table 08:151-171 only); rest CUT | D9: static panel, so a model projection. X5 for the Elmi "shape". Gini and tightness are off-storyline |
| 08:329-464 §4.3 Đường biên | 39–40 | Budget ladder bang:thang1 (08:340-357); "Trần luôn được tôn trọng" (08:362-364); "Điểm gãy nằm ở 300 giây" (08:370-372); noise floor ±0.3 pp (08:389-408); pickup ladder (08:414-464) | APPX A (ladder + noise floor). Compliance → §4.10. Pickup ladder CUT | D4: compliance is a correctness check. X9: "break point 300 s" here conflicts with "60–120 s" on WP14r (handoff §4.3) |
| 08:466-538 §4.4 Hai cơ sở | 41–42 | Outcome basis infeasible on 4/20 cells; normative box (08:532-538) | CUT | V-30 appears in the T3.8 frontier instead (2,336 served, 53.8% forced) |
| 08:540-605 §4.5 Độ vững thước đo | 43 | Nine measures monotone | CUT (one line in §4.10) | Off-storyline |
| 08:607-683 §4.6 Ratchet | 44 | Ratchet ≡ hard lock under insertion | CUT (one line in APPX A) | Off-storyline; a neat finding to mention |
| 08:685-961 §4.7 Trôi dạt thật | 45–50 | Drift injection k ∈ {0, 0.5, 1, 2}; outcome basis infeasible on 19/20; 11 domain-invariant stops; (1−p)^n model (08:848-899); post-hoc deadline estimate; retro-check | CUT | Superseded by T3.8 (measured factors with recovery (b)). The domain invariant goes to the limitations |
| 08:963-1156 §4.8 Hạn chót có tiền đăng ký | 50–54 | Tier-2 four-family experiment; Fig. hinh:tang2 (08:1051-1057, `hinh/tang2-bon-ho-v2.pdf`); 98/102, 31/32, 40/40 (08:1109-1125) | CUT | Tier-2 framing with sealed predictions (owner rule). On T3.8, M⁺ with recovery (b) serves the same 2,338 |
| 08:1158-1312 §4.9 Quét (design, results) | 55–58 | C/M⁺ 30–900 s on 6 worlds × 2 cells (bang:quet 08:1201-1228; bang:quet-kieu 08:1249-1268) | CUT | Mostly synthetic worlds. One sentence in the limitations |
| 08:1313-1372 §4.9.4 Luật phục hồi (b) | 58–59 | Definition (08:1319-1321); 1,874 / 1,864 / 1,873 (08:1361-1362) | Definition → ch. 3 §3.4. Numbers CUT | T3.8 uses (b) for every arm (RUN38:9) |
| 08:1374-1427 §4.9.5 V-30, M-30 | 60 | V and M with both recoveries | CUT | T3.8 V-30 replaces it |
| 08:1429-1480 §4.9.6 Khung 7–9 h | 61–62 | bang:quet07 (08:1442-1461): C/M⁺ at 30/60/120/300 s on 8 cells; "C chấm theo luật M⁺ cùng tỉ lệ" (08:1471-1473) | Reuse the table in §4.4 (merged with w07x) | Measured w07 dial; matches CAP:3-11 |
| 08:1482-1556 §4.9.7 Diễn giải | 62–63 | Interpretation and limits of the sweep | CUT | Follows the cut sweep |
| 08:1558-1703 §4.10 Trần cửa sổ đón | 64–66 | Reject reasons (08:1565-1581); window 600→900 s (08:1595-1622); price surface (08:1624-1680); domain invariant (08:1682-1703) | CUT. Domain invariant → 1–2 lines in §4.11 | Off-storyline |
| 08:1705-1824 §4.11 Đối chiếu FA | 67–68 | FA measure on own data, 54× and 49% (08:1714-1731); relative cost (08:1769-1788); boundary table bang:trung (08:1794-1816) | CUT. One D13 sentence in §2.2 or APPX A | X10: 08:1810-1813 claims "Phân rã nhân quả định lượng: 2020 không / khóa luận có" and "Trần … cưỡng chế: không", against D03:54-56 |
| 08:1826-1866 §4.12 Phúc lợi | 69 | Break-even at 20–25 EUR/h | CUT | D16 (08:1852-1857); D03:236-245 |
| 08:1868-1897 §4.13 Không giả tạo | 70 | Search never truncated (bang:khonggiatao) | KEEP (short) in §4.10 | Fix D17 (08:1894-1897). Add the T3.8 retention counters (R15 row 35) |
| 08:1899-2159 §4.14 Bộ sinh biết lời hứa | 70–75 | Levels A/B/C; 96% single-candidate; reorder generator and LOCKED_LEG_MISMATCH; budget reservation inert; utilisation level saturated (08:2137-2145) | CUT. **Reuse the saturation fact (08:2137-2145) in §4.6** | Static-panel negatives. The saturation is exactly the "conservative selector" question |
| 08:2161-2206 §4.15 Hướng đã thử | 76 | Uniform ETA padding "12 trên 1. Loại bỏ" (08:2168-2170); deadline promise; soft gate; negotiated window | CUT | X11: 08:2168-2170 contradicts the padded-U comparator that is now central (2,328 = 2,328) |
| 08:2208-2271 §4.16 Hạn chế | 77–78 | Scale, metric closure, lower-bound drift, scalar traffic, small Tier-2, welfare, no reassignment | REWRITE → new §4.11 | Keep 08:2213-2220, 2228-2234 and 2269-2271. Add the newer limits (§2.6) |

### 1.6 Chapter 5 (`09-chuong5.tex`, pp. 79–85)

| Location | Pages | What it says | Verdict | Why |
|---|---|---|---|---|
| 09:3-84 §5.1 Tổng kết | 79–80 | Three components, including "hệ thống chứng cứ niêm phong" (09:15-16); four-family theorem as the "central contribution" (09:18-29); legal "điểm mới" (09:30-32); runs (09:34); 89.06% (09:36-37); sealed predictions (09:44-46); sweep (09:51-59); side results (09:62-84) | REWRITE | D3, D14, D9, D1 (09:5-7), sealing talk, no T3.8 |
| 09:86-128 §5.2 Hạn chế | 81 | Scale; overlap with FA, Elmi and S&P (09:96-102); drift lower bound; evidence level; welfare; "không tuyên bố vượt trội" + D8 (09:125-128) | REWRITE (keep the 09:91-102 spirit) | D8; the honest overlap paragraph is worth keeping |
| 09:130-211 §5.3 Hướng phát triển | 82–83 | Ten directions: Tier-2 formalisation, 7–9 h on more days, recovery, Hamburg data, harm-only ledger h_t, smaller panels, surface, negotiated window, domain invariant, frozen leg + reorder | REWRITE (≤ 5 items) | Most are obsolete. Align with R17 A3 / R18 §6 |
| 09:213-231 §5.4 Kết luận cuối | 84–85 | "cách đặt vấn đề"; D7 (09:215-218); preregistration confirms the theorem (09:226-231, D15); "chỉ trần hành vi … không bao giờ là nguyên nhân" (09:230-231) | REWRITE (0.5 p.) | D3, D7, D15 |

### 1.7 References (`10-tai-lieu.tex`, pp. 86–89)

- **Count and gaps.** There are 27 `\bibitem`s (10:7-166). Hörl & Zwick 2022 is missing (D19). Leonardi et al. 2024 and Ding,
  Dandl & Bogenberger are also missing, though the handoff requires them (BAN-GIAO:396).
- **Eight entries are never cited** (my grep of `\cite` in 05–09, X12): cordeau2007 (10:63-67), toth2014 (10:69-73),
  groer2009 (10:75-79), blackburn1986 (10:81-85), agatz2012 (10:87-91), ortools (10:93-97), tlc (10:99-102) and
  li2025 (10:104-108).
  - Either cite them where relevant (cordeau2007, agatz2012, ortools and tlc fit ch. 2–3) or drop them.
- **CUT with their sections:** sridharan1987, kovacs2014, agarwal2019, chen2018 and borodin1992.
  - Keep the bibitem if one sentence still cites it.
- **ADD (each only if the text cites it):**
  - Hörl & Zwick 2022.
  - Leonardi 2024 (arXiv 2411.11899).
  - Ding et al. (⚠ only Codex read it; BAN-GIAO:144).
  - Mt-KaRRi (arXiv 2605.11798).
  - Wardman et al. 2026.
  - The pooled VOT/VOR survey (Alonso-González, already present).
  - The FleetPy 2026 ETRR paper, for the ≈1.33 occupancy comparison (R15 row 20).
  - The UberX Share product page (fetched).
  - Cohen et al. 2022 (Via), only if cited.
- **Net result:** about the same 4 pages.

### 1.8 Where each R17 §D overclaim lands

| D | Current location | Action in the new outline |
|---|---|---|
| D1 | 02:6-10, 56-59; 09:5-7 | New abstract and §1.1. Scope: "các hàm mục tiêu theo thông lượng …; FA 2020 đã đo và kiểm soát" |
| D2 | 02:17-20, 66-69 | Contribution sentence 2 (§3) cites HZ-B and states only the bounded-quantity difference |
| D3 | 02:22-26, 71-75; 05:169-182; 09:18-22, 224-231; 08:20 | Remark 3.1 in §3.3: true by construction; the HZ-style relaxed deadline shares it. No "chỉ/duy nhất" (stricter than R17 K2; see §4.4) |
| D4 | 02:14-16, 63-66; 05:202-204, 213-217 | §4.5 gets the R18 cumulative sentence. "291 < 300 …" → §4.10 validation |
| D5 | 05:64-69 | §1.3 table row "Hörl & Zwick 2022" |
| D6 | 05:71-73, 75-82 | Deleted (§1.2 replaced) |
| D7 | 05:99-104; 09:215-218 (and 06:121-127, X3) | §2.2: "thước đo hai đầu là hậu nghiệm; mục 6 của họ đã ràng buộc lời hứa đón" |
| D8 | 05:267-271; 09:125-128 | §1.4 / §5.1: "cài đặt và kiểm một dạng kiểm soát trước quyết định, và đo cái giá của nó" |
| D9 | 02:28-30, 78-80; 05:244-248; 08:16-17, 173-178; 09:36-37 | Only in §4.3 (≤ 0.5 p.) and Appx A, with the "phép chiếu mô hình trên panel thời gian đi tĩnh" wording |
| D10 | 02:46-47, 97-98 | Keywords: "quy trách theo mô hình" |
| D11 | 02:43, 94; 05:241 | Remark 3.1 wording + R18 correction (equal aggregates; naive late60 C 76 vs M⁺ 74) |
| D12 | 05:250-253 | Appx A only, labelled "gói C1 so với B1" |
| D13 | 05:261-264 | One sentence in §2.2 or Appx A |
| D14 | 09:30-32 (and 06:184-187, X4) | Deleted; legal analogy at most one interpretive sentence (decision §4.3) |
| D15 | 09:226-231 | Deleted |
| D16 | 08:1852-1859 | Welfare section cut |
| D17 | 08:1894-1897 | §4.10: "… phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán" |
| D18 | missing | §4.2–4.6 (T3.8 frontier, cumulative audit, dials, cost-first screen, snow) |
| D19 | 10-tai-lieu.tex | Add HZ 2022; cite in §1.3, §2.3, Remark 3.1 and §5.1 (K3) |

### 1.9 Additional problems found (not in R17 §D)

- **X1 — the run count disagrees across the text.**
  - 02:27-28 and 09:34 say 558 + 546 runs.
  - The table 08:99-111 says 558 + 685 = 1,243.
  - The README says 1,104 and "102 trang"; the PDF has 105 pages.
  - The handoff inventory has 1,991 runs in 51 experiments (BAN-GIAO:463).
- **X2 — notation clash.**
  - The thesis uses B = \|p − v\| and β for the cap (04:45-46, 04:53; 07:91-95).
  - The agreed text uses c = p − e and budget B.
  - This must be changed across ch. 3–4 (risk §4.4).
- **X3 — 06:121-127 repeats the D7 strawman** in ch. 2.
- **X4 — 06:184-187 repeats the D14 "điểm mới" claim** in ch. 2.
- **X5 — 05:136-140 and 08:269-272 compare the C1 package with Elmi** ("xóa 99,8%" vs "phân phối lại"). This is a package
  comparison across different systems.
- **X6 — 07:168-173 calls per-rider, cumulative and hard-constraint "chỗ khác biệt so với văn liệu".**
  - Per-rider protection is prior work (D03:211-213).
  - HZ routes under hard constraints (HZ:575-588).
- **X7 — 07:699 says "chín dự án", but the table 07:711-717 lists seven.**
- **X8 — rule names drift across panels.** B1 / C1 (static), FREE / LOCKS (WP14r) and U / C-30 (T3.8) are never put
  in one table. U is not "free pooling" (R13 D18).
- **X9 — two different "break points".** "Điểm gãy nằm ở 300 giây" (08:370-372, static panel) vs "điểm gãy giữa 60 và
  120 s" (WP14r, BAN-GIAO:241). Do not present either as general.
- **X10 — the boundary table claims a causal decomposition** (08:1810-1813) and denies FA any enforceable cap, against
  D03:54-56.
- **X11 — 08:2168-2170 dismisses uniform ETA padding.** That contradicts the new central comparator: padded U ties C
  at 60 s and beats it at 120 s (R15:163-183).
- **X12 — 8 of 27 references are uncited** (§1.7).
- **X13 — sealing/preregistration language appears throughout,** against the owner's rule: 02:33-38, 02:78, 02:84;
  05:184-188, 05:307; 07:671-675, 07:739-758; 08:24-26, 08:963-1028, 08:1180, 08:1382, 08:1437; 09:15-16, 09:44-46,
  09:226-231.
- **X14 — two different "late > 1 min" statistics are in circulation.**
  - LATE gives U 8.34% / C-30 3.25% (LATE:5,12).
  - The rider-experience report gives 9.1% / 4.1% (BAN-GIAO:183-188).
  - Use one, with its definition. I recommend LATE together with the integer counts in A:7,9.

### 1.10 Figures inventory

- `hinh/` holds three files:
  - `logo-uet.png`: KEEP.
  - `tang2-bon-ho-v2.pdf`: used once at 08:1053 (Tier-2 bars). CUT.
  - `tang2-bon-ho.pdf`: unused. CUT.
- The only other figure is the TikZ loop at 07:24-45: KEEP with edits.
- **Every other figure in the new thesis is new, but drawn from existing numbers (no runs).** See §2.

---

## 2. Proposed outline (≈ 74 pages)

### 2.1 Rules applied to every section

1. **One storyline.** Every section opens with which of the three causes it addresses.
2. **A plain answer first.** Every results section starts with a 1–2-sentence answer containing a real number and its
   denominator, in the "Kết quả tổng quan" style of the DACN report. Then the table.
3. **Counts over percentages.** Report counts per 3,672 requests or per served riders, and say which. Never write
   "0.17%" without a denominator.
   - 0.17% is the cell mean over 21 weekday cells.
   - 0.43% = 10/2,338 is the pooled figure.
   - 0.51% is the mean over all 34 cells.
   - Early60 0.171% = 4/2,338.
   - Sources: D03:267-268; R18 row 30.
4. **Banned wording.** No sealing, preregistration, "đã niêm phong", "dự đoán trước khi chạy". No "chỉ/duy nhất/đầu
   tiên/không ai". No causal words: "gây ra" for the ledger becomes "phần được tính cho quyết định điều phối"; the split
   is a "phép chiếu mô hình".
5. **Anchor every number.** Every number in the abstract, ch. 1 and ch. 5 must have an anchor in a claim–evidence table
   (R17 K1). The anchors in §2.10 are the source.
6. **Fixed glossary**, used throughout:
   - served → "lượt được phục vụ"
   - late60 → "lượt trễ quá 60 s so với lời hứa đầu"
   - timely60 → "lượt đến không trễ quá 60 s, tính trên số yêu cầu"
   - early60 → "lượt tới sớm quá 60 s"
   - quote extension → "độ dài thêm của lời hứa"
   - forced decision → "quyết định phải phục hồi"
   - own-rule break → "khách bị chính luật phá lời hứa"
   - The symbols U, FREE, C-B, M⁺-B and V-B are defined once in Bảng 3.3.
7. **Notation:** v, e, p; x = e − v; c = p − e; z = p − v = x + c; budget B; first promise p₀.

### 2.2 Front matter: 10 pages

| Item | Pages | Notes |
|---|---:|---|
| Bìa tiếng Việt | 1 | Title decision §4.3. Supervisor UNKNOWN: leave "[chờ bổ sung]" |
| Bìa tiếng Anh | 1 | Optional (decision §4.3). If a "Lời cam đoan" page is required (UNCONFIRMED; check the UET template), it takes this slot when the English cover is dropped |
| Lời cảm ơn | 1 | Rewrite 01:4-19. No run counts; no claim that the report documents abandoned directions |
| Tóm tắt | 1 | ≤ 300 words. Three causes → three places; the 4–5 headline numbers of §3 with denominators; limits in one sentence. If Stage 1a/1b exist, add one clause |
| Abstract | 1 | Optional (decision §4.3). Exact mirror of the Tóm tắt |
| Mục lục | 2 | `tocdepth=2` (main.tex:62) |
| Danh sách hình, Danh sách bảng | 2 | About 9 figures and 18 tables |
| Ký hiệu và chữ viết tắt | 1 | New symbol table (§2.1 item 7); rule names; drop MPS/MRP |

### 2.3 Chương 1. Đặt vấn đề: 7 pages

| § | Title | Pages | Purpose (one sentence) | Figures/tables | Evidence |
|---|---|---:|---|---|---|
| 1.1 | Bối cảnh: lời hứa giờ trả trong xe đi chung | 1.5 | Show with one real rider that a promised drop-off time drifts, and why riders and operators care | **H1.1 (new TikZ):** the timeline of rider rq-30b7e083c7b, cell d20181115-s10-r1-w07. Booked 7:11:56, first promise 7:34:51, picked up 7:22:30, alighted 7:38:02 (+190.5 s). The forecast quote would have been 7:37:44 (+17.6 s) | `report-extras/example-rider-2026-10-06.txt:2-3,60`. Reuse 05:5-19 (RTV) and 05:31-40 (demand-side value, trimmed) |
| 1.2 | Ba nguyên nhân làm lời hứa lệch và chỗ xử lý mỗi nguyên nhân | 1.5 | State the single storyline: the dispatch part is capped by rule C, anticipated traffic goes into the first quote, the rest is recorded per rider | **H1.2 (new TikZ):** three causes → three places. Teaser numbers, labelled as a model projection: on 21 weekday cells, 86.1% of late seconds were anticipated traffic; on the snow afternoon, 92.5% were not | BAN-GIAO:88-122; FR:72-75, 103-104 |
| 1.3 | Các công trình gần nhất và chỗ đứng của khóa luận | 2 | Position the work narrowly against FA 2020, **HZ 2022 strategy B (eq. 7)**, S&P 2026 and Elmi 2026 (plus Mt-KaRRi and forecast-based ETA practice) | **Bảng 1.1 (positioning, DACN style).** Columns: what the work does / quantity bounded or measured / traffic part charged? / where this thesis differs or borrows. Rows FA 2020 (measure + §6 control; rejections 34.5 → 45.6%), HZ 2022 (max(updated, latest) for at-risk on-board riders; hard constraints + penalty), Elmi 2026 (per-rider guarantee; fixed travel times), S&P 2026 (deadline from first offer; 900 s; fixed travel times), Mt-KaRRi (α·T_accepted + β), forecast ETA (prior practice) | HZ:507,529-543,567-569,575-588; FAM:571-576; D03:54-56,205-221; R13 V:150-158; R15 rows 62-63, 72, 75. Reuse the facts at 05:90-97, 05:105-133, 05:142-158 |
| 1.4 | Mục tiêu và đóng góp | 1.5 | State the contribution narrowly (§3 of this file) and list what is not claimed | Box "Không nhận là mới / không khẳng định" | R17:140-152 decisive table; R18:263-279 |
| 1.5 | Phạm vi và cấu trúc báo cáo | 0.5 | Scope (one simulator, one city-wide factor, 108 requests / 8 vehicles, 34 cells over 5 days) and the chapter map | — | T38:29-33,46; reuse 05:285-290 |

### 2.4 Chương 2. Cơ sở lý thuyết: 6 pages

| § | Title | Pages | Purpose | Figures/tables | Evidence |
|---|---|---:|---|---|---|
| 2.1 | Bài toán ghép chuyến động và kiến trúc RTV | 2 | Give the standard problem, the RTV + ILP selection, and the soft "cost to incumbents" term that does not bound one rider's drift | **Bảng 2.1:** service constraints of a plan (pickup window Ω = 600 s, ride time ≤ 1.5 × direct, capacity 4). Eqs. 2.1–2.3 reused | Reuse 06:14-55; shortened 06:57-70; 08:49-68 |
| 2.2 | Lời hứa công bố và độ bất ổn: đo và kiểm soát | 1.5 | Present FA 2020's measure **and** their §6 pre-decision control, and why an endpoint measure misses self-cancelling revisions | — | Reuse 06:84-119 and 06:129-134; drop 06:121-127. D13 sentence |
| 2.3 | Các dạng nghĩa vụ lời hứa | 1.5 | Compare the obligation forms in the literature, and show that "count both parts" just gives back the old rules | **Bảng 2.2.** Rows: pickup window; ride-time cap; deadline from first offer (S&P); HZ-B relaxed required time; Elmi guarantee; Mt-KaRRi. Columns: time origin / is traffic charged? / who it applies to / cumulative? / per-rider ledger? Plus the identity: signed sum Σ(c + x) is the deadline M⁺, absolute sum Σ\|c + x\| is V | HZ; D03:205-221 and §12; BAN-GIAO:113-114; R15 rows 72, 75 |
| 2.4 | Dự báo thời gian đi và hứa theo dự báo | 0.5 | Show that time-of-day forecasting and forecast-based quoting are prior practice, and describe the data used (15-minute city-wide factors) | — | BAN-GIAO:139-147 (Leonardi 2024; industry ETA); FR:11, 36 |
| 2.5 | Độ tin cậy có giá trị gì với khách | 0.5 | State what is known about rider valuation, without converting it into WTP for a 30 s ledger | — | R15:281-297 (correction 6); D03 §12; BAN-GIAO:255-258 |

### 2.5 Chương 3. Phương pháp: luật C, hứa theo dự báo và sổ cái theo từng khách: 12 pages

| § | Title | Pages | Purpose | Figures/tables | Evidence |
|---|---|---:|---|---|---|
| 3.1 | Tổng quan hệ thống RideBound | 1.5 | Show the decision loop and where the three components sit | **H3.1** = the TikZ at 07:24-45, edited: add "Lời hứa theo dự báo" and "Sổ cái v/e/p"; β → B. Optional pipeline strip | Reuse 07:10-22 (rewritten), 07:722-724 |
| 3.2 | Lời hứa và ba mốc v, e, p | 2 | Define v, e, p and the exact signed split z = x + c, and say what e includes (execution progress, not pure traffic) | **Bảng 3.1** = the 9:10 example (07:126-140) in the new notation. Optional H3.2: x, c, z arrows on a time axis | 07:79-101, 07:267-274, 07:427-430; `tang3/evidence/audit_vep.py:99-125` (BAN-GIAO:97); D03:222-224 |
| 3.3 | Luật C: ngân sách dời giờ trả do điều phối cho từng khách | 2.5 | Define C (Σ\|c\| ≤ B over the whole trip; remaining allowance = B − spent) as a hard filter before the ILP, and state its by-construction property and its limits | **Bảng 3.2 (DACN style):** constraints of a candidate plan — hard: Ω, ride time, capacity, locks (vehicle, stops, pickup time), budget C; then the objective order. **Giải thuật 3.1:** budget check per rider: before + \|c\| = after; reject if after > B; record a witness. **Nhận xét 3.1:** C never removes the do-nothing plan, under assumption (N); 6-line proof. A literal HZ-style max(p₀ + B, e) shares this property. CE-2 (C does not bound what the rider sees) and CE-3 (C charges a restoring correction) | 07:163-166, 193-203, 292-297, 480-492, 650-654; `CommitmentBudgetEvaluator.cs:6-12,86-98` (R15 row 29); `CommitmentDecisionValidator.cs:222-239` (R18 row 25); U vs C-30 configs differ only in hardLimit 30000 (R18 row 18); R17 R6 |
| 3.4 | Các luật đối chứng và bộ chọn phương án | 1.5 | Define every comparator and the selector order once, so ch. 4 needs no re-definitions | **Bảng 3.3:** rules U (locks, no drop cap), FREE (no locks, cost-first), C-B, M⁺-B (deadline from the first promise; the deadline component of S&P, not their method), V-B (Σ\|z\| ≤ B); which panels use each. Recovery (b) "không tệ hơn tham chiếu". Selector order: forced → accepted → stability levels → operational cost → id | 08:1319-1321; RUN38:9; WP4:7; SEL:271-303,319-331,365-385; BAN-GIAO:103-114; R17 B16-B20 |
| 3.5 | Hứa theo dự báo | 1.5 | Show how the first quote is stretched by a historical 15-minute profile from earlier days, and its known operational conflict | **Giải thuật 3.2:** forecast quote (the causal profile; one-sided display; no source day at weekends) | FR:36-70, 97-100; `display_layer.py:36-72`, `promise_stretch.py:29-68` (R15:11); 34/1,471 pickup conflict (FR:70) |
| 3.6 | Sổ cái ba phần cho từng khách | 1 | Split lateness into dispatch / anticipated / remainder, and state that this is a model projection, not blame | Formula: arrival − first quote = Σc + (Σx − forecast allowance) | R15:161 (W5); R13 V:495; FR:72-77; BAN-GIAO:95, 385-389 |
| 3.7 | Cài đặt, kiểm thử và tái lập | 2 | Show that the implementation and the numbers can be checked | **Bảng 3.4** = architecture (07:702-720; fix 07:699; re-count lines). Insertion generator (07:728-737). Transcripts and hashes (07:744-758, without sealing words). Independent recomputation | T38:10-15, 97-113; R15:11-13 (227 transcripts, 458,477 frames); W07X:74-85; FR:179-195 |

### 2.6 Chương 4. Thực nghiệm và đánh giá: 27 pages

| § | Title | Pages | Purpose | Figures/tables | Evidence |
|---|---|---:|---|---|---|
| 4.1 | Thiết lập thực nghiệm | 3 | Give the cells, panels and metric definitions with their denominators | **Bảng 4.1** = cell parameters (reuse 08:49-68, updated). **Bảng 4.2** = panels used: T3.8 main (34 test cells, 3,672 requests, 14–18 Nov; windows 7–9 h: 9, 8–10 h: 14, 17–19 h: 11); w07 dial (8 cells, 864 requests, 12–13 Nov); WP14r fixed traffic (16 cells, 1,728 requests); snow (8 cells, 15 Nov, 601 served); static panel (20 cells; Appx A). **Bảng 4.3** = metric glossary (§2.1 item 6) | T38:29-33,46; CAP:3; LAD:2; RP:5; SNOW:10 |
| 4.2 | Kết quả chính: phục vụ, đúng giờ và độ dài lời hứa trên 34 ô | 5 | Answer "what does C buy and cost?" on the main panel, against U, M⁺ and padding | **Bảng 4.4 (frontier).** Rows: U; U + dự báo; U + dự báo + đệm 30 s; U + dự báo + đệm 60 s; C-30; C-30 + dự báo; M⁺-30; M⁺-30 + dự báo; V-30 and M⁺-60 (served and forced only). Columns: served, late60, timely60 / 3,672, timely120, early60, quote extension, forced %, own-rule breaks %. **H4.1 (new pgfplots):** timely60 per request vs quote extension (or vs served). **Bảng 4.5:** lateness > 1 / 2 / 5 / 10 min and max (U, C-30, C-30 + dự báo), with a "lượt phải bồi thường / 100 yêu cầu" column (symbolic money, R15 correction 3). Text: C vs U (−96, −127, +31); served sets 2,207 common, 227 / 131 unique; by window −39 / −52 / −5; shared 22.8 → 13.4%. C vs M⁺: 2,338 = 2,338, 2,332 common; forced 0 vs 41.3% (cell mean); breaks 0 vs 14.5% (12.4% pooled). Padded U ties at 2,328 and wins at 120 s (2,366 vs 2,338), at 37.2 vs 7.4 s and early60 1.81 vs 0.17% | E1: A:7-9,18-19; T38:46-64,111; PAD; LATE:3-26; SHARE:2-4; R15:163-183; R18 rows 27-31 |
| 4.3 | Phần do điều phối: luật C chặn được gì và mất gì | 2.5 | Show the mechanism (one real decision), how few C riders are dispatch-exposed, and why C rejects | Real example: 79.0 s traffic + 68.3 s dispatch = 147 s > 90 s, so M⁺ blocks and C accepts. **Bảng 4.6** exposure: U 174 exposed / 12 repeated / max S 590.1 s / late ∧ exposed 134 of 203; C-30 33 / 0 / 29.2 s / 4 of 76. Rejections: 148 requests with recorded budget prunes; median smallest overshoot 109.6 s (record-based wording). One static-panel paragraph (≤ 0.5 p.): 89.06% model projection with D9 wording → Appx A | W07X:54-62; A:7,9; EXP:2-6; BUD:2-10; R18 rows 33, 37, 47; 08:151-171 |
| 4.4 | Chọn mức trần B | 3.5 | Show the dial: what loosening B buys and costs, with no "optimum" | **Bảng 4.7:** (a) WP14r ladder FREE / LOCKS / C-120 / C-60 / C-30: served, shared, exposed, late60, timely120; (b) w07 dial C-30 … C-300 and U: served, late60, late120, timely60, timely120, plus M⁺ forced by B (58.6 → 1.7%). **H4.2 (new pgfplots):** served and late60 vs B. Cohort "price per step" ratios. **[Stage 1a slot, ~1 p., §2.11]** | E2 (CAP:3-11; W07X:20-29; 08:1442-1461); E3 (LAD:2-6; WP17 timely120; A:3-5); R13 V:133-142 |
| 4.5 | Phần cộng dồn của luật C: kiểm toàn bộ bản ghi | 1.5 | Report exactly what the cumulative clause did on recorded traffic, and what was not run | **Bảng 4.8:** 98 runs, 64,371 decisions, 1,256 = 845 + 411 records, all single-step > branch-specific B, 0 cumulative-only. Fixed traffic: 4 decisions. Synthetic: 3 decisions after dedup. The R18 Vietnamese paragraph (R18:301-307). Definitional meaning: under U, 12 / 2,434 riders were moved ≥ 2 times; the maximum sum was 590 s | E4: A:3-17,20; R18:297-309; CVP:5-8,17,22,32 |
| 4.6 | Độ tin cậy đến từ trần hay từ bộ chọn ổn định? | 2.5 | Face the committee's strongest question with the existing screen, and reserve space for the matched test | Selector order and the saturated utilisation level (3,503 / 3,503; 3,506 / 3,506). **Bảng 4.9** fixed-state screen: 445 / 1,714 = 26.0% (LOCKS) vs 104 / 1,715 = 6.1% (C-30) of new-request decisions change. Three cost statistics: 7.79 / 8.00% conditional; 2.02 / 0.49% per new-request decision; 0.307 / 0.079% ratio of summed plan costs (not realised cost). Max 35.5 s summed over 2 riders. "Different state populations". **[Stage 1b slot, ~1.5 p., §2.11]** | E9: PV:2-9; R18 rows 51-54 and :313-317; SEL; A:7,9; 08:2137-2145 |
| 4.7 | Hứa theo dự báo | 3 | Show what the forecast removes, that it is not specific to C, and that C and the forecast act on different causes | **Bảng 4.10** Family A (21 weekday cells, cell means): naive 6.01% / equal-cost pad 1.94% / forecast 0.17%; 7 h 14.44 → 0.27%; +13.7 s; U 9.72 → 3.90%; M⁺ and V also 0.17%; pooled 10 / 2,338. **H4.3 (new):** ledger stacked bars, weekday (1.3 / 86.1 / 12.6%) vs snow (9 / 251 / 3,186 s). Family B (forecast inside the dispatcher) in 0.5 p.: 3 / 32 PLAN_INFEASIBLE; M⁺ still forced 47.6%. The real rider again (+17.6 s) | E5: FR:36-86, 65, 70, 72-77, 103-104; E6: FR:117-146; LATE:24-26 |
| 4.8 | Khi dự báo không đủ: buổi chiều tuyết 15/11/2018 | 1.5 | Report the one incident afternoon honestly, as an exploratory limitation | **Bảng 4.11** replay (601 served): naive 41, HIST 34 (5.66% pooled; 5.94% is a cell mean), in-window blend 21, prefix blend 19 (uses an undelivered morning prefix and a post-hoc threshold), lagged blend 29 (exact anchor), equal-cost pad 27. Ledger: dispatch 8.6 of 3,445.9 s; the prefix model explains ~26% more; ~two-thirds stays unexplained by the methods tried | E7: SNOW:10; RP:5-25; R17:413-431; R18:327-331 |
| 4.9 | Học máy có giúp thêm không? | 0.75 | Report the negative ML pilot in one table-free half page | — (text: ML1 true; ML2 +0.69 / +0.00 pp with guards failed; FREE 12.89 → 11.65% with +6.9% early; vehicle state adds nothing; weekday headroom 2 / 1,471) | E8: ML-A1:45-64; BAN-GIAO:322-347; R15:299-313 |
| 4.10 | Kiểm tra tính hợp lệ của kết quả | 1.25 | Show that the numbers are correct and not artefacts | Budget compliance (0 overshoots; max 29.2 s; the static ladder 291 < 300 … from 08:362-364). Search not truncated (T3.8 retention counters; 08:1875-1892 shortened, D17 fixed). v/e/p audit. Independent recomputation | T38:10-15; R15 row 35; R15:11-13; 08:1868-1897 |
| 4.11 | Thảo luận và hạn chế của thực nghiệm | 2 | Say plainly what the results mean for an operator and where they stop | Limitations list: scale and low load (0.54 riders per vehicle vs ≈ 1.33 in FleetPy 2026); 0 s dwell; one city-wide factor; base speed at 00:00; shorter selected trips; metric-closure network; 5 days, 34 dependent cells, one seed; previewed cells; no rider response; forecast pickup conflict; domain invariant on the pickup window (from 08:1682-1703); static package cost −7.13 pp; no reassignment (08:2269-2271); business value unconfirmed | BAN-GIAO:198-227, 368-381; R15 row 20; D03 §11; 08:2213-2234 |

Sum: 3 + 5 + 2.5 + 3.5 + 1.5 + 2.5 + 3 + 1.5 + 0.75 + 1.25 + 2 = **26.5**, leaving 0.5 p. of slack inside 27.

### 2.7 Chương 5. Kết luận: 4 pages

| § | Title | Pages | Purpose | Evidence |
|---|---|---:|---|---|
| 5.1 | Tổng kết theo ba nguyên nhân | 1.5 | One paragraph per cause, each with its headline number and denominator; HZ cited (K3) | A:7-9; FR; R18:263-279 |
| 5.2 | Hạn chế | 1 | Plain list pointing to §4.11, plus the overlap with prior work (in the spirit of 09:96-102) | D03 §10–11 |
| 5.3 | Hướng phát triển | 1.5 | At most 5 items, each one sentence + cost: (1) per-step vs cumulative trajectory comparison (Stage 2); (2) literal HZ relaxed deadline max(p₀ + B, e) as a baseline; (3) multi-event incident forecasting with as-of data (80–140 h); (4) higher load, per-segment traffic, rider-response model, real operator thresholds; (5) pickup-window domain invariant and trip-length-proportional budgets | R17:313-326; R18:255-261, 361-366 |

### 2.8 Tài liệu tham khảo: 4 pages

The changes are in §1.7.

### 2.9 Phụ lục (optional): 4 pages

| Appendix | Pages | Content (reused) | Wording fixes |
|---|---:|---|---|
| A. Panel thời gian đi tĩnh (20 ô, 2,160 yêu cầu) | 2 | bang:quytrach (08:151-171); bang:thang1 (08:340-357) + noise floor (08:389-408); one line: ratchet ≡ hard lock (08:643-663); one line: an endpoint measure scores 49% of revised C1 riders as zero (08:1714-1731) | D9 (model projection), D12 (C1 vs B1 is a package), D13 |
| B. Tính chất phương án giữ nguyên dưới bốn luật | 1.5 | Theorem 3.4 restated as a remark (07:501-527), the corollaries (07:544-572), CE-1…CE-6 (07:641-663) | D3: by construction; HZ variant; no "only" |
| C. Kiểm kê lần chạy và nơi lưu kết quả | 0.5 | Runs per panel used; output roots; inventory 1,991 runs / 51 experiments | One counting rule (X1) |

### 2.10 Evidence key (where the writers take every number)

Paths are relative to `E:/Code/Report_INT3508/ridebound-scratchpad/` unless absolute.

| Key | Evidence | Anchor |
|---|---|---|
| E1 | **T3.8 frontier** (U / C-30 / M⁺-30 ± forecast ± pad; served sets; lateness; sharing; exposure) | A = `optimize/codex-debate/codex-work/R15-audit-summary.txt:7-9,18-19`; T38 = `tang3/t38/T38-REPORT.md:46-64,111`; PAD = `optimize/codex-debate/claude-work/cap-vs-pad-frontier-2026-10-07.txt`; LATE = `optimize/report-extras/lateness-distribution-2026-10-06.txt:3-26`; SHARE / EXP = `optimize/codex-debate/pooling-share-2026-10-06.txt:2-4`, `exposure-check-2026-10-06.txt:2-6`; R15:163-183 (padded-U table); R18 rows 26-37 |
| E2 | **w07 cap dial** (8 cells, 864 requests) and M⁺ forced by B; mechanism example | CAP = `optimize/codex-debate/codex-work/R16-cap-outcomes.txt:3-11`; `tang3/w07x/W07X-REPORT.md:20-29,54-62`; thesis 08:1442-1461 |
| E3 | **WP14r ladder** (fixed traffic, 16 cells) | LAD = `optimize/codex-debate/claude-work/wp14r-ladder-reanalysis-2026-10-08.txt:2-6`; R17 B45 (timely120); A:3-5 |
| E4 | **Cumulative audit** | A:3-17,20; R17 §R3 (R17:371-387); corrected Vietnamese text R18:297-309; CVP = `optimize/codex-debate/claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` |
| E5 | **Forecast Family A**, three-part ledger, example rider | FR = `optimize/FORECAST-REPORT.md:36-86`; `optimize/report-extras/example-rider-2026-10-06.txt:2-3,60` |
| E6 | Forecast Family B (rejected) | FR:117-146 |
| E7 | **Snow replay** | SNOW = `optimize/test-snow-2026-10-06-report.txt:10`; RP = `optimize/codex-debate/claude-work/r16-forecast/rider-nowcast-replay-2026-10-10.txt:5-25`; R17:413-431; R18:327-331 |
| E8 | **ML pilot negative** | ML-A1 = `optimize/codex-debate/claude-work/ml-pilot-report-a1-2026-10-08.txt:45-64`; BAN-GIAO:322-347 |
| E9 | **Fixed-state cost-first screen** | PV = `optimize/codex-debate/codex-work/R17-portfolio-verification.txt:2-9`; R18 rows 50-54 and :313-317; SEL = `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271-303,319-331,365-385` |
| E10 | **Stage 1a** (stability-first C-120 on the 34 T3.8 cells): **pending** | `tang3/t38c120/C120-PLAN.md`; output `C:/RideBoundData/research/tier3-t38c120-v1` |
| E11 | **Stage 1b** (selector order {stability-first, cost-first} × {U, C-30}): **pending, not run** | R17:195-310 (A2); R18:220-253 |
| E12 | Static panel (Appx A) | thesis 08:151-171, 08:340-357, 08:389-408, 08:643-663 |
| E13 | Rejections by budget | BUD = `optimize/codex-debate/claude-work/budget-block-diagnosis-2026-10-07.txt:2-10`; R17 §R2; R18:283-293 |
| E14 | Simulation limits | `optimize/codex-debate/claude-work/load-and-occupancy-2026-10-07.txt:2`; BAN-GIAO:198-227, 368-381; R15 row 20 |
| E15 | Validity and reproducibility | T38:10-15,97-113; R15:11-13; W07X:74-85; FR:179-195 |

### 2.11 Stage 1a / Stage 1b slots (space reserved; fill rules; fallback)

**Stage 1a: C-120 on the 34 cells** (running now; plan `tang3/t38c120/C120-PLAN.md`). Slot ≈ 1 page in §4.4.

- **Bảng 4.7 block (c) "T3.8, 34 ô".** Rows:
  - U: 2,434 served / 203 late60 / 2,231 timely60 / 2,332 timely120.
  - C-30: 2,338 / 76 / 2,262 / 2,327.
  - C-120: [điền].
- **Columns:** served; naive late60; timely60 / 3,672; timely120 / 3,672; forecast late60; riders exposed; max Σ\|c\|;
  cumulative-only records; forced decisions.
- **H4.2** gets one new point.
- **Two paragraphs**, compared with w07 (C-120 666 vs U 665) and WP14r (+29 served, +23 late60).
- **Wording rules:** no "optimum". U is a measured endpoint, not a bound (R18:287). Report the result even if it is
  surprising. Do not talk about the plan's predictions.
- **Also update:**
  - contribution sentence 8 (§3);
  - §5.1;
  - one clause of the abstract.
- **Fallback** (no data by the cutoff): keep the WP14r and w07 dials and add one sentence, "trần 120 s chưa được đo trên
  34 ô chính" (+0 page). The item moves to §5.3.

**Stage 1b: selector order × cap (2×2)** (not run; needs code, a Gate 0 equivalence check and owner approval).
Slot ≈ 1.5 pages in §4.6.

- **Bảng 4.12.** Rows: {ưu tiên ổn định (archived), ưu tiên chi phí} × {U, C-30}. Columns:
  - served; rejected; timely60; late60; timely120;
  - absolute shared completions; exposed riders;
  - forced / no-worse counts; budget prunings; quote extension.
- **The interaction:** I_L = (L_CF,U − L_CF,C30) − 127, together with the identity I_L = I_served − I_timely60, and
  per-cell / per-day signs (R18:236-251).
- **Reading rules:** R18:195-206. Missing a materiality target does not prove the selector is irrelevant. Never write
  "chính trần, không phải bộ chọn, giữ lời hứa".
- **Fallback** (not run or Gate 0 fails): 0.3 page. "Phép thử chưa chạy; bằng chứng hiện có là phép sàng lọc trên trạng
  thái cố định ở trên." The item moves to §5.3.

**Contribution sentence 8 (placeholder):**
- Variant A (data exists): "Thêm điểm trần 120 s trên 34 ô cho [x] lượt phục vụ và [y] lượt trễ quá 60 s; đổi bộ chọn
  sang ưu tiên chi phí dưới trần 30 s cho [z]."
- Variant B: delete the sentence.

---

## 3. Contribution statement (draft, Vietnamese; consistent with R17 A1 and R18 corrections)

> **Đóng góp của khóa luận.**
> (1) Khóa luận đặc tả, cài đặt trong hệ điều phối RideBound và kiểm chứng trên bản ghi một ngân sách dời giờ trả cho
> từng khách (luật C). Ở mỗi lần sửa lời hứa, phần dời được tính cho quyết định điều phối là c = p − e, với e là kế
> hoạch cũ tính lại theo tốc độ hiện tại. Tổng |c| của mỗi khách qua cả chuyến không được vượt B, và phương án vi phạm
> bị loại trước khi chọn.
> (2) Mốc e tiếp nối chiến lược B của Hörl và Zwick (2022), vốn đã dùng giờ trả cập nhật theo tắc đường trên tuyến
> cũ. Điểm khác nằm ở đại lượng bị chặn: luật C áp cho mọi khách từ lúc đặt cùng một ngân sách B cho cả chuyến, không
> phụ thuộc phần tắc đường, tính trị tuyệt đối theo cả hai chiều, cộng dồn qua các lần sửa và ghi vào sổ cái v/e/p
> kiểm được theo từng khách.
> (3) Luật này được ghép với hai thành phần đã có tiền lệ. Một là hứa theo dự báo, dùng hồ sơ tắc đường lịch sử theo
> khung 15 phút cho lời hứa đầu. Hai là một sổ cái tách phần trễ còn lại theo phép chiếu mô hình thành phần tính cho
> điều phối, phần tắc đường đoán trước được và phần còn lại.
> (4) Khóa luận đo đường đánh đổi giữa số lượt phục vụ, số lượt đến đúng hẹn và độ dài lời hứa. Phép đo chạy trên mô
> phỏng FleetPy dùng hệ số tắc đường toàn thành phố lấy từ dữ liệu đo ở Manhattan, gồm 34 ô, 3.672 yêu cầu trong 5
> ngày. Luật C được so với ba cách: điều phối không trần; luật hạn chót tính từ lời hứa đầu, là thành phần hạn chót
> kiểu Schulz và Pfeiffer (2026), có phục hồi "không tệ hơn"; và cách đệm lời hứa.
> (5) Với B = 30 s, so với không trần, luật C phục vụ ít hơn 96 lượt (2,6 điểm phần trăm số yêu cầu). Nó có ít hơn
> 127 lượt trễ quá 60 s và thêm 31 lượt đến không trễ quá 60 s trên cùng 3.672 yêu cầu. So với luật hạn chót cùng mức,
> nó phục vụ cùng số lượt (2.338, trong đó 2.332 lượt chung). Luật C không có quyết định nào phải phục hồi, còn luật
> hạn chót phải phục hồi ở 41,3% quyết định (trung bình theo ô).
> (6) Khi thêm dự báo, luật C và luật hạn chót cùng đạt 2.328 lượt đến không trễ quá 60 s. Cách không trần có dự báo
> và đệm 30 s cũng đạt 2.328 lượt, và hơn ở ngưỡng 120 s (2.366 so với 2.338). Đổi lại, lời hứa của cách này dài thêm
> 37,2 s thay vì 7,4 s, và 1,81% thay vì 0,17% số khách tới sớm quá 60 s.
> (7) Kiểm toàn bộ 98 lần chạy có áp luật C cho thấy cả 1.256 bản ghi chặn do ngân sách đều do một lần dời vượt B của
> nhánh tương ứng. Phần cộng dồn chưa từng là lý do riêng của một lần chặn được ghi nhận. Khóa luận chưa chạy đối chứng
> với luật mỗi bước một trần.
> (8) [Câu dành cho Stage 1a/1b, §2.11; xóa nếu không có số liệu.]

Anchors for each sentence:

| Sentence | Anchors |
|---|---|
| (1) | R17 FP:31-33; R18:181; SEL; `CommitmentBudgetEvaluator.cs` |
| (2) | HZ:529-541,567-569; R17 R6; BAN-GIAO:145-147; R13 D19 |
| (3) | FR; D03:222-224 |
| (4) | T38:46; RUN38:9 |
| (5) | A:7-9,18-19; T38:58; DIAL17:12-13 |
| (6) | A:7,9; R15:167-171 |
| (7) | A:3-17; R18:301-305 |

Not claimed. The list goes into §1.4 as a short box, in Vietnamese:
- **Không nhận là mới:**
  - mốc giờ trả cập nhật theo tắc đường và việc tách phần tắc đường (Hörl–Zwick 2022);
  - kiểm soát trước quyết định và đánh đổi phục vụ–ổn định (Fielbaum–Alonso-Mora 2020);
  - bảo đảm theo từng khách (Elmi 2026);
  - hạn chót tính từ lời hứa đầu (Schulz–Pfeiffer 2026);
  - hứa theo dự báo và dự báo giờ đi theo giờ trong ngày;
  - chèn động, gán lại, giới hạn ETA (D03:1-12).
- **Không nói luật C phục vụ nhiều hơn**, hay cho nhiều lượt đúng hẹn hơn, luật hạn chót hoặc cách đệm lời hứa. Không
  nói hai luật "cùng mọi khách": C có 76 lượt trễ quá 60 s khi không dự báo, M⁺ có 74.
- **Tính chất "không tự loại phương án giữ nguyên" là đúng theo cấu tạo,** không phải ưu thế riêng. Hạn chót nới kiểu
  Hörl–Zwick cũng có tính chất này.
- **Không phân biệt bằng "cổng cứng thay vì phạt mềm":** Hörl–Zwick cũng có ràng buộc cứng.
- **Không quy trách nhân quả:** sổ cái là phép chiếu mô hình, và phần còn lại không mặc nhiên được "miễn trách".
- **Không khẳng định phần cộng dồn là cần thiết hay vô dụng** về mặt thực nghiệm. Không nói "không bao giờ đổi quyết
  định".
- **Không nói về lợi ích kinh doanh,** sự hài lòng, doanh thu hay việc giữ khách. Chi phí kế hoạch của bộ giải không
  phải chi phí vận hành thực.
- **Không suy rộng** sang thành phố, mức tải hay mạng đường khác. 34 ô không độc lập (chỉ 5 ngày).
- **Không gọi mức B = 30 s hay 120 s là tối ưu,** và 30 s không phải ngưỡng cảm nhận của khách.
- **Không dùng "0,17%" mà không ghi mẫu số.** Không gọi phần còn lại ở ngày tuyết là "không thể biết trước".
- **Không nói học máy không thể giúp.** Chỉ nói các mô hình đã thử không giúp thêm trên mẫu này.

---

## 4. Risks

### 4.1 Where the page budget is tight

- **§4.2 (5 pp.)** carries Bảng 4.4 (10 rows × 8 columns), H4.1 and Bảng 4.5, plus the mandatory caveats on
  denominators, served sets and padding.
  - At 13 pt with 1.5 spacing, a 10-row table with a caption takes ~0.6 p.
  - If it overflows, move the per-window breakdown and the V-30 / M⁺-60 rows into the text.
- **§4.6 (2.5 pp.)** holds the 1.5-page Stage 1b slot.
  - If Stage 1b runs and also produces sharing and witness results, it will want 2.5 pp.
  - Pay for that by moving §4.9 (ML, 0.75 p.) to Appx C and trimming Appx A to 1.5 pp.
- **Ch. 3 (12 pp.)** has 2 pseudo-code tables, 4 tables and 1–2 figures in the DACN style. The notation migration
  (X2) adds re-explanation.
  - Hold §3.7 to 2 pp.; no line-count table if the counts cannot be re-verified.
- **Chapter openings** each waste ~0.5 p. on a new page (`report` class). The budgets above include this; expect ±2
  pp. overall.
- **Front matter.**
  - If both the English cover and abstract are kept **and** a Lời cam đoan is required, front matter becomes 11 pp.
  - Dropping the appendix still keeps the total ≥ 70.
- **Totals:**
  - 74 with the appendix; 70 without it.
  - The owner's 79-page ceiling leaves 5 pp. of headroom. The most likely draws on it are Stage 1b and the front matter.

### 4.2 Content the owner may miss after the cuts

| Content | Location | Proposed fate |
|---|---|---|
| Four-family theorem, the drift-direction corollaries, prediction accuracy 98/102, 31/32, 40/40, and its figure | 07:415-594; 08:1030-1125; `hinh/tang2-bon-ho-v2.pdf` | Appx B (theorem only); predictions dropped (owner rule) |
| Drift-injection experiment: 19/20 outcome-basis infeasible; the (1 − p)^n argument | 08:757-899 | Dropped |
| Static panel: 89.06%, nine-measure robustness, Gini trap, ratchet ≡ hard lock, "break point 300 s" | 08:140-683 | Appx A keeps 89.06%, the ladder and the ratchet line |
| Window-cap test (+172 riders); "promise cost grows with operator freedom"; price surface | 08:1590-1680 | Dropped (one line in §4.11 if wanted) |
| Promise-aware generator: 96% single-candidate decisions; LOCKED_LEG_MISMATCH invariant; inert budget reservation | 08:1899-2159 | Dropped; the saturation fact is reused in §4.6 |
| FA-measure re-implementation (54×, 49%) and the relative-cost table | 08:1705-1824 | One sentence (§2.2 / Appx A) |
| Welfare break-even | 08:1826-1866 | Dropped (D16) |
| Synthetic-world sweep and the two-sided M family | 08:1158-1427 | Dropped |
| Legal analogy (obligation of means vs result) | 06:162-187 | At most one interpretive sentence (decision) |
| "Hướng đã thử và lý do từ bỏ", which the acknowledgement says the owner values (01:17-19) | 08:2161-2206 | Dropped; 2–3 lines in §5.3 if wanted |
| T3.8 H3 conformal margin γ = 222.3 s (2 / 34 cells exceed it) | T38:17-38 (never in the thesis) | Not included (decision) |

### 4.3 Decisions only the owner can make

1. **Theorem chapter.**
   - (a) Keep the current §3.5 (≈ 11 pp.; it does not fit the budget).
   - (b) **Demote** to Remark 3.1 (~1 p.) + Appx B (1.5 p.). This is my recommendation, per R17 A1.5.
   - (c) Cut it entirely.
2. **Supervisor name: UNKNOWN** (00:28, 00:64, 01:4). Leave the placeholders. Do not use "ThS. Trần Mạnh Cường" from
   the DACN course.
3. **English cover and Abstract** (00:35-69; 02:51-98) vs the owner's "Vietnamese only" rule.
   - Check the UET template, and whether a Lời cam đoan page is required (UNCONFIRMED).
4. **Title.**
   - Keep "Lời hứa có biên được chứng nhận trong điều phối xe đi chung theo yêu cầu".
   - Or retitle to the storyline, e.g. "Giữ lời hứa giờ trả cho khách đi chung: giới hạn phần dời do điều phối, hứa
     theo dự báo và sổ cái theo từng khách".
5. **Appendix yes/no.** Without it, the static-panel and theorem material disappears entirely (70 pp.).
6. **Stage 1b.** Include it only if it finishes by a cutoff date that the owner sets. The deadline (mid-November) is
   UNCONFIRMED.
7. **Rule names for outside readers.** For example "không trần" (U) vs "ghép tự do" (FREE), "luật C", "luật hạn chót";
   and whether to keep "C-30" style symbols in prose.
8. **One run-count convention** (X1), e.g. "số lần chạy dùng trong khóa luận, theo bộ ô".
9. **Which "late > 1 min" statistic to use** (X14).
10. **Whether to mention the T3.8 γ margin at all** (§4.2 table above).

### 4.4 Other risks

- **The notation migration can break things** (A / d / B / β → \|c\| / \|x\| / \|z\| / B). Every reused equation,
  table header and symbol-table row must change together. Reused 07:* text carries the old letters.
  - Mitigation: a single macro file, and a final grep for `\beta` and for `A =`, `B =`.
- **The owner's "no only/first" rule is stricter than R17 K2,** which allows "chỉ …" with an explicit scope. Use the
  stricter rule. Remark 3.1 then states C's property and the other rules' failure modes without "chỉ".
- **Stage 1a may change the cap narrative.** For example, C-120 could recover many riders at a small lateness cost.
  - §4.4 frames B as a dial and 30 s as a conservative point. This holds whatever the result, provided nobody adds
    "optimum" language afterwards.
- **Stage 1b may weaken a sentence.** If CF-C30 loses reliability, it shows the selector does reliability work.
  - The contribution statement (§3) does not depend on Stage 1b. Only sentence 8 and §4.6 change.
- **Inherited inconsistencies** (X1, X7, X9, X11, X12) survive if old paragraphs are pasted unread. Check each reused
  block against §1.9.
- **Number provenance.**
  - The static-panel numbers (Appx A) come from the 2026-09 runs and were not re-audited in rounds 13–18. Mark them so,
    or re-anchor them to their scripts (README.md lists them).
  - The architecture line counts (07:711-717) are UNCONFIRMED as current.
- **Cell means vs pooled values.** The 14.5% / 41.3% (T3.8) and the forecast 0.17% / 5.94% are cell means. Their pooled
  counterparts are 12.4%, 0.43% and 5.66%. Mixing them is the most likely factual error in the rewrite.
- **The R17 K4 adversarial pass** (Codex on the contribution paragraph) is still planned. Sentences it falsifies must be
  deleted, not rescued.

---

*End of proposal. File created by Claude (structure editor) on 2026-10-10; no other file was written or modified.*
