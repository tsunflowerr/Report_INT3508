# OUTLINE V2 — rewrite of the RideBound thesis (consolidated after R20), 2026-10-11

**What this is.** The final outline for the Vietnamese rewrite (UET/VNU, LaTeX), replacing
`OUTLINE-PROPOSAL-CLAUDE.md` (O). Every change from O is justified, row by row, in `REVIEW-DECISIONS-R20.md` (RD) next to
this file. Stage 1a (stable C-120 on the 34 main cells) is now run and verified by two independent analyses and is filled
in §4.4. Stage 1b is not run; its slot has a written fallback.

**Evidence convention.** Numbers are cited by row ID of `rewrite-2026-10/evidence/EVIDENCE-REGISTER.md` (A01…K52). Rows
**N-01…N-15** (§9) are new entries I verified this session that must be added to the register before writing; rows marked
**[A]** are arithmetic on verified counts and must be recomputed by a saved script (STYLE rule 27). No number may enter the
thesis without one of these IDs.

## 0. The thesis in five lines (for the supervisor; no internal codes)

1. In ride-pooling, the drop-off time promised to a rider can move every time the dispatcher adds a rider or traffic changes.
2. The thesis splits that drift into three parts: the part due to dispatch decisions, the part the usual daily traffic
   pattern explains, and the rest.
3. It specifies and implements in the RideBound dispatcher a per-rider cap on the total dispatch part over the whole trip
   (rule C); traffic that follows the usual pattern goes into the first promise through a historical forecast; the rest is
   recorded per rider.
4. On a FleetPy simulation with city-wide traffic factors measured in Manhattan (34 scenarios, 3,672 requests), it measures
   what the cap buys and costs against no cap, a deadline rule and quote padding, and reports where the cap does not help.
5. The contribution is narrow: a specified, implemented and audited obligation and a measured trade-off, not a new
   algorithmic idea and not a business result.

---

## 1. Owner decisions applied

| Decision | Applied as | Source |
|---|---|---|
| Theorem | Demoted to **Nhận xét 3.1** in §3.3 (statement, condition (N), 6-line proof, two counterexamples); Appendix B ≤ 1 page | Owner default; RD CX-33, CX-52 |
| Covers and abstracts | Vietnamese cover + English cover; Tóm tắt + Abstract; body Vietnamese only | Owner default; RD CX-68 (rejected) |
| Title | Two options below; owner picks | Owner default; RD CX-69, LR-52 |
| Appendix | ≤ 3 pages (A ≤ 1, B ≤ 1, C 1) | Owner default; RD CX-56, LR-41 |
| Stage 1a | Filled in §4.4 from the two verified analyses | Coordinator input; N-06…N-11 |
| Stage 1b | Slot in §4.6 with written fallback; no extra approval needed, Gate 0 required | Owner default; RD CX-63 |
| Rule names in prose | "điều phối không trần", "ghép tự do", "luật C", "luật hạn chót", "luật trần độ dời khách thấy", "đệm 30 giây"; symbols only in tables | Owner default; RD CX-70, LR-54 |
| Supervisor | "[chờ bổ sung]" on both covers and in the acknowledgement; do not use the DACN supervisor | Owner default; RD LR-51 |
| No sealed plans / preregistration / predictions | Forbidden everywhere in the thesis, including appendices. Overrides STYLE §4.5, STYLE §5.2 point 5, GLOSSARY F "kết quả mong đợi ghi trước khi chạy", GLOSSARY G row 1 | Owner override; RD §5 |

**Title options (owner picks one).**
- **Option 1 (keep):** "Lời hứa có biên được chứng nhận trong điều phối xe đi chung theo yêu cầu" (TEX/00-bia.tex:15-16).
  Note: STYLE rule 15 lists "lời hứa có biên được chứng nhận" as a banned phrase, and Codex and the lecturer both advise
  against "chứng nhận" (it suggests an external certificate or an arrival guarantee).
- **Option 2 (shorter, follows the storyline, no "chứng nhận"):** "Giới hạn phần dời giờ trả do điều phối cho từng khách
  trong dịch vụ đi chung xe" (≈ 19 tiếng). English cover: "Per-rider limits on dispatch-induced drop-off time changes in
  on-demand ride-pooling".
- Whether a registered title may still be changed, and by when, is UNVERIFIED; ask the faculty before editing the covers.

---

## 2. Rules for every writer (consolidated)

1. **One storyline, three parts.** Use "ba phần của độ lệch giờ trả" (dispatch part, part explained by the historical
   profile, the rest), never "ba nguyên nhân" (RD CX-26, LR-18). Setup, validity and related-work sections need not open
   with a part.
2. **Answer first.** Each results section opens with 1–2 sentences containing a real count and its denominator.
3. **Counts before percentages.** State the unit (yêu cầu, lượt phục vụ, khách, lần chạy, quyết định, bản ghi). Label every
   rate `[gộp theo khách]`, `[TB theo kịch bản]` or `[trên yêu cầu]` as in the register. Cell means and pooled values never
   share a table block (RD CX-38).
4. **The 0,17% rule** (REG K24): never write 0,17% without saying whether it is the 21-scenario late cell mean or the
   early share 4/2.338.
5. **Banned in the thesis:** niêm phong, tiền đăng ký, kế hoạch đã ghi trước, dự đoán trước khi chạy, mã băm kế hoạch, kết
   quả đạt/trượt của dự đoán (owner override); "duy nhất", "đầu tiên", "vượt trội", "tối ưu" for a cap level; causal verbs
   for the ledger ("gây ra" → "phần tính cho điều phối"); "quy trách"; every forbidden phrase in REG K01–K52.
6. **Names.** Prose names as in §1. Test sets: "tập kiểm tra chính (34 kịch bản)", "tập chỉnh trần buổi sáng (8 kịch
   bản)", "tập tắc đường cố định (16 kịch bản)", "chiều tuyết 15/11/2018 (8 kịch bản)", "tập kịch bản tĩnh (20 kịch bản,
   Phụ lục A)". "Kịch bản" replaces "ô" (GLOSSARY F). The cap is "trần"; avoid "ngân sách" in prose except once to explain
   "phần trần còn lại" (RD AG-21). Cite Hörl–Zwick by "công thức 7", not "chiến lược B", to avoid the clash with the cap
   symbol B (RD LR-21).
7. **Notation** (defined in §3.2 before any use; none in chapters 1–2): v, e, p; p₀ (lời hứa đầu không dự báo); D₀ (lời
   hứa đầu có dự báo); a (giờ trả thực tế); x = e − v; c = p − e; z = p − v = x + c; L (phần trần đã dùng); B (trần);
   q = Σc (tổng có dấu); f = D₀ − p₀; ρ = a − p_k. Rule symbols U, FREE, C-B, M⁺-B, V-B only in tables, after Bảng 3.3.
8. **Sign convention and reading sentence.** Differences are "luật được thử trừ đối chứng"; positive means more. After
   every result table, one "cách đọc bảng" sentence (RD LR-46).
9. **Per-table metadata (internal note, not printed):** configurations, scenario list, unit, strict ">" or "≤", denominator,
   aggregation, register ID and script (RD CX-65).
10. **Missing is not zero.** Write "chưa đo" or "chưa đưa vào bảng" (R19 rule 33).
11. **Voice.** Neutral subject ("hệ thống", "luật C", "khóa luận"); "em" only in the acknowledgement (STYLE rule 16).
12. **Stage 1a numbers only from STG/CXS (N-06…N-11); Stage 1b numbers only from a future audited output.**

---

## 3. Page budget (≈ 73 pages)

| Part | Pages | Change from O |
|---|---:|---|
| Front matter | 10 | = |
| Ch. 1 Đặt vấn đề | 7 | = (re-split) |
| Ch. 2 Cơ sở lý thuyết và các công trình liên quan | 6,5 | +0,5 (forecast definition, RD CX-32) |
| Ch. 3 Phương pháp | 13 | +1 (problem statement, full-cycle pseudocode, implementation; RD LR-07…LR-11) |
| Ch. 4 Thực nghiệm và đánh giá | 26,5 | −0,5 |
| Ch. 5 Kết luận | 3 | −1 (RD CX-49, LR-40) |
| Tài liệu tham khảo | 4 | = (≈ −1 after the heading fix, RD LR-14) |
| Phụ lục | 3 | −1 (owner ≤ 3) |
| **Total** | **73** | |

**Fallbacks and contingencies (estimates, not measured layout; RD CX-55).** Stage 1b not run: −1,2 p (§4.6 0,8 p).
Appendix A not re-anchored: −1 p. Both: ≈ 70,8 p. If the template needs an inner cover or a "Lời cam đoan" (UNVERIFIED;
DACN has two Vietnamese covers, DACN PDF 1-2): +1 p each, up to ≈ 75 p. Do not shrink fonts or spacing to fit
(R19 rule 36).

---

## 4. Front matter (10 pages)

| Item | Pages | Notes | Evidence |
|---|---:|---|---|
| Bìa tiếng Việt | 1 | Title per §1; supervisor "[chờ bổ sung]" | TEX/00-bia.tex:15-16,28 |
| Bìa tiếng Anh | 1 | Mirror; supervisor "[to be filled]" | TEX/00-bia.tex:51-52,64 |
| Lời cảm ơn | 1 | Rewrite TEX/01-loi-cam-on.tex:4-19; no run counts; drop the "abandoned directions" sentence | RD CX-67 |
| Tóm tắt | 1 | Written last; ≤ 300 tiếng; three paragraphs (vấn đề / cách làm / kết quả + one limit); ≤ 4 numeric results, each with denominator: −96 served on 3.672 requests and +31 timely; the padding tie with 37,2 vs 7,4 s; the C-120 point; the cumulative clause | C02, C08, C10, N-06, N-08 |
| Abstract | 1 | Exact mirror of the Tóm tắt | same |
| Mục lục | 2 | `tocdepth=2` | — |
| Danh sách hình, Danh sách bảng | 2 | ≈ 9 figures, ≈ 20 tables | — |
| Danh mục ký hiệu và chữ viết tắt | 1 | Symbols of §2 rule 7; rule symbols; drop ODRP, RTV, MPS, MRP, VOT, VOR, pp, β, κ, ℓ (GLOSSARY H) | — |

---

## 5. Chapters

### Chương 1. Đặt vấn đề (7 pages)

**Opening sentence.** «Chương này nêu vì sao giờ trả đã hứa với khách đi chung xe hay bị dời, chia độ lệch đó thành ba
phần và chỉ ra chỗ khóa luận xử lý từng phần, rồi nêu đóng góp và phạm vi của khóa luận.»

| § | Title | Pages | Purpose | Figures/tables | Evidence IDs |
|---|---|---:|---|---|---|
| — | Đoạn mở chương | 0,25 | Chapter map in two sentences | — | — |
| 1.1 | Bối cảnh: lời hứa giờ trả trong dịch vụ đi chung xe | 1,5 | Show with two simulated riders that the promise drifts for different reasons, and why riders and operators care | **H1.1 (new TikZ, two timelines).** (a) Kịch bản phát triển d20181113-s10-r1-w07: với trần lỏng 300 giây, khách trễ nhất trễ 307,3 s = 99,1 s phần thay đổi khi giữ kế hoạch + 208,2 s phần do điều phối; cùng kịch bản dưới trần 30 giây, khách trễ nhất trễ 99,1 s, trong đó 97,1 s là phần thay đổi khi giữ kế hoạch. (b) Khách rq-30b7e083c7b, d20181115-s10-r1-w07: đặt 7:11:56, lời hứa đầu 7:34:51, đón 7:22:30, tới 7:38:02 (+190,5 s); lời hứa có dự báo 7:37:44 (+17,6 s). Caption: "khách trong bản ghi mô phỏng" | D06 (W07:48-54), C31, J28 (UberX Share: "cannot guarantee arrival times"), J31, J24, J23 (one sentence each; different constructs) |
| 1.2 | Ba phần của độ lệch giờ trả và chỗ xử lý mỗi phần | 1,25 | State the storyline; one motivation number from the uncapped dispatcher; three research questions | **H1.2 (new TikZ):** three parts → luật C / lời hứa theo dự báo / sổ theo từng khách. Text: khi không trần, 134 trong 203 lượt trễ quá một phút có giờ trả từng bị điều phối dời (giao của hai tập, không phải tỉ lệ nhân quả); theo sổ, phần tính cho điều phối bằng 73,4% số giây trễ của họ; một khách bị dời tổng 590 giây (gần 10 phút). Research questions CH1–CH3 (below) | C20, C21, C24 |
| 1.3 | Các công trình gần nhất và chỗ đứng của khóa luận | 1,25 | Position narrowly; words only, no formulas | **Bảng 1.1 (short):** rows Fielbaum–Alonso-Mora 2020; Hörl–Zwick 2022; Schulz–Pfeiffer 2026; Elmi và cộng sự 2026; Mt-KaRRi; thực tiễn lời hứa theo dự báo; **khóa luận**. Columns: Làm gì / Đại lượng được giới hạn hay đo / Phần do tắc đường có bị tính? / Khóa luận kế thừa hay làm khác | J01, J03, J05, J06–J10, J12 (UNVERIFIED: open the paper before citing details), J32, J35, K01, K03, K30, K32 |
| 1.4 | Mục tiêu và đóng góp | 1,75 | Contribution paragraph (§6), five-line result list, "không nhận là mới" box | Box (§6.3) | §6.2 side table |
| 1.5 | Phạm vi | 0,75 | Labelled bullets: Môi trường; Quy mô; Tắc đường; Dữ liệu kiểm tra; Ngoài phạm vi | — | B01, B02, B03, B04, B06, B07, B08, B09, B11, A07, I07, I10 |
| 1.6 | Cấu trúc báo cáo | 0,25 | One sentence per chapter | — | — |

**Research questions (end of §1.2).**
- **CH1.** Phần dời do điều phối được đo trên đại lượng nào, kiểm khi nào, và trần trên phần đó giữ được gì, không giữ được
  gì? → Ch. 3; §4.3, §4.5, §4.10. *Không suy ra:* bảo đảm giờ đến thực tế.
- **CH2.** Trên các tập đã đo, giữ trần đổi số lượt phục vụ, số lượt đúng giờ và độ dài lời hứa thế nào so với điều phối
  không trần, luật hạn chót và cách đệm lời hứa? → §4.2, §4.4, §4.6, §4.8. *Không suy ra:* tác dụng riêng của bộ chọn,
  hay một mức trần tối ưu.
- **CH3.** Lời hứa theo hồ sơ tắc đường lịch sử thay đổi số lượt đúng giờ thế nào, và phần nào còn chưa được giải thích?
  → §3.5–3.6; §4.7, §4.9. *Không suy ra:* phần còn lại là "không thể biết trước", hay phản ứng của khách.

### Chương 2. Cơ sở lý thuyết và các công trình liên quan (6,5 pages)

**Opening sentence.** «Chương này trình bày bài toán ghép chuyến động mà khóa luận dựa vào, các cách nghiên cứu trước đã
đo và ràng buộc lời hứa với khách, và những gì đã biết về dự báo thời gian đi và giá trị của độ tin cậy.»

| § | Title | Pages | Purpose | Figures/tables | Evidence IDs |
|---|---|---:|---|---|---|
| — | Đoạn mở chương | 0,25 | Map | — | — |
| 2.1 | Bài toán ghép chuyến động và kiến trúc yêu cầu–chuyến–xe | 2 | Standard problem, request–trip–vehicle graph + integer program (reuse TEX/06-chuong2.tex:14-55), the soft "cost to incumbents" term (trim 06:57-70); separate theory from what RideBound uses | **Bảng 2.1:** service constraints of a plan with the values used in the tests (cửa sổ đón 600 s; thời gian ngồi xe ≤ 1,5 × đi thẳng; 4 chỗ), captioned "cấu hình của tập thử, không phải chuẩn ngành" | B03, J17, J18, J25 |
| 2.2 | Đo lường và kiểm soát độ bất ổn của lời hứa | 1,25 | Fielbaum–Alonso-Mora's measure, their off-peak data, their §6 pre-decision control and its cost; why an endpoint measure misses self-cancelling revisions | — | J06, J07, J08, J09, K30, K32 |
| 2.3 | Các dạng ràng buộc lời hứa | 1,5 | Compare obligation forms by approach | **Bảng 2.2 (full, words only):** rows cửa sổ đón; giới hạn thời gian ngồi xe; hạn chót từ lời mời đầu (Schulz–Pfeiffer, 900 s); mốc cập nhật + nới hạn trả (Hörl–Zwick, công thức 7, ràng buộc 9–10, phạt 11); bảo đảm theo khách (Elmi); Mt-KaRRi α·T + β described in words; **luật C (khóa luận)**. Columns: Gốc thời gian / Phần do tắc đường có bị tính? / Áp cho ai / Cộng qua cả chuyến? / Ghi theo từng khách? Text in words: "cộng có dấu cả hai phần thì quay về hạn chót tính từ lời hứa đầu; cộng độ lớn phần khách thấy thì là luật trần độ dời khách thấy" (formal version in §3.4) | J03, J05, J10, J11, J12, J32, A12, K26 |
| 2.4 | Dự báo thời gian đi và lời hứa theo dự báo | 1 | Prior practice; what data the forecast may use and when it is available; the 15-minute city-wide factor of the FleetPy data | — | J18, J21, J22, J35, B06, B27 |
| 2.5 | Độ tin cậy có giá trị gì với khách | 0,5 | What is known about rider valuation, without turning it into a price for a 30-second cap | — | J23, J24, J33, D20 |

### Chương 3. Phương pháp: luật C, lời hứa theo dự báo và sổ theo từng khách (13 pages)

**Opening sentence.** «Chương này trình bày cách khóa luận đo phần dời giờ trả do điều phối cho từng khách, luật C dùng
phần đó để loại phương án, lời hứa theo dự báo, sổ theo dõi từng khách, và cách các thành phần này được cài đặt và kiểm
tra trong RideBound.»

| § | Title | Pages | Purpose | Figures/tables | Evidence IDs |
|---|---|---:|---|---|---|
| — | Đoạn mở chương | 0,25 | Map | — | — |
| 3.1 | Phát biểu bài toán và tổng quan hệ thống | 2 | 3.1.1 (0,5 p): at each decision epoch, what the system receives (vehicle states, accepted riders with promises, new requests, current travel-time snapshot), decides (accept/reject; plan per vehicle), publishes (promises) and records (ledger rows); hard constraints; evaluation metrics. 3.1.2: overview | **H3.1** = TikZ loop of TEX/07-chuong3.tex:24-45, edited (add "Lời hứa theo dự báo", "Sổ theo từng khách"; β → B). **Giải thuật 3.1 (new):** one decision cycle — nhận sự kiện → sinh phương án chỉ chèn thêm (≤ 100 phương án, ≤ 2 yêu cầu mới mỗi xe) → với mỗi phương án và mỗi khách: tính v, e, p → kiểm khóa, cửa sổ, sức chứa, trần của luật đang dùng → bộ giải chọn theo thứ tự tiêu chí → công bố lời hứa → ghi sổ; three comment lines on recovery when a vehicle is forced | A02, A05, A06, A13, A14, A17, A18, A24 |
| 3.2 | Ba mốc giờ trả và phần dời do điều phối | 1,75 | Define v, e, p and x, c, z; say e includes execution progress, not only traffic; charging is by magnitude in both directions | **H3.2 (new, mandatory):** a vehicle carrying rider A takes rider B; A's drop time moves; arrows x, c, z on a time axis. **Bảng 3.1** = the 9:10 / 9:10:40 / 9:11:10 example (TEX/07-chuong3.tex:126-140) in the new notation. Text: kéo sớm hay đẩy muộn 20 giây đều làm tổng tăng 20 giây; on the 34 scenarios 4 of 33 C-30 riders, 2 of 174 U riders and 3 of 103 C-120 riders had a net earlier dispatch change, so "bộ sinh chỉ chèn thêm" does not imply c ≥ 0 when travel times vary | A01, A02, A03, A04, C23, N-05 |
| 3.3 | Luật C: trần phần dời giờ trả do điều phối cho từng khách | 2,5 | Define C: Σ\|c\| ≤ B per accepted rider over the whole trip; remaining = B − L; checked in the accepted, waiting and on-board phases; a hard filter before the solver. State Nhận xét 3.1 and its limits | **Bảng 3.2 (DACN style, columns Nhóm / Nội dung / Vai trò):** hard constraints (cửa sổ đón, thời gian ngồi xe, sức chứa, khóa xe / điểm đón / giờ đón, trần C) then the selector order. **Nhận xét 3.1:** if 0 ≤ L ≤ B and the keep-route option is generated and passes every non-budget check (assumption (N), defined here), it has c = 0 and luật C does not remove it; this is by construction and does not guarantee that some plan is feasible (e.g. a pickup window already violated). A relaxed deadline max(p₀ + B, e) in the Hörl–Zwick style shares the property (inference, not a run). **CE-2:** c = 0 yet the rider sees a change (v = 600, e = p = 660). **CE-3:** a restoring correction is charged (v = p = 600, e = 720) | A06, A07, A21, A22, E08, K02, K43; TEX/07-chuong3.tex:193-203, 292-297, 651-654 |
| 3.4 | Các luật đối chứng và bộ chọn phương án | 1,5 | Define every comparator and the selector once | **Bảng 3.3 (6 columns):** Tên trong bài / Ký hiệu trong bảng / Kiểm điều gì / Khóa / Khi xe bị ép / Dùng ở tập nào. Rows: điều phối không trần (U: không trần giờ trả, vẫn khóa xe, điểm đón, giờ đón); ghép tự do (FREE: không khóa, chính sách chi phí cuốn chiếu mặc định); luật C (C-B); luật hạn chót (M⁺-B: giờ trả mới không muộn hơn lời hứa đầu quá B; chỉ phần hạn chót của Schulz–Pfeiffer, ở 30–60 s thay vì 900 s); luật trần độ dời khách thấy (V-B: Σ\|z\| ≤ B). Old-set names (B1, C1, LOCKS) mapped in a note. Text: identity Σ(c_t + x_t) = p_k − p₀ when v_t = p_{t−1} and the chain is continuous; selector order with activation conditions (forced count only for hard-vector profiles; utilisation level saturated at 1.000.000 ppm on 3.503/3.503 and 3.506/3.506 decisions); recovery rules "giữ nguyên kế hoạch" and "không tệ hơn kế hoạch giữ" (used for every configuration of the main set) | A08, A09, A10, A11, A12, A14, A15, A17, A18, A19, J11, K27, K50 |
| 3.5 | Lời hứa theo dự báo | 1,25 | How the first promise is stretched by the historical 15-minute profile and when it is available | **Giải thuật 3.2:** D = max(p, S), S stretches the remaining time by the forecast growth of the city-wide factor (mean of source days) after the current bin, never shortens. Rule: only earlier days of the same type, ≥ 2 source days, never 15/11 → forecasts exist only on 14, 15, 16/11; weekend scenarios keep the naive promise. Known conflict: 34/1.471 pickup promises shown after the latest pickup time | F01, F02, F03 (replay only; no plan wording), F07, J35 |
| 3.6 | Sổ theo dõi từng khách | 0,75 | Three-part ledger as a model calculation, not blame | Formula: a − p₀ = q + f + (a − D₀ − q), with q = Σc (signed, ≠ Σ\|c\|) and f = D₀ − p₀, computed on riders with a − p₀ > 60 s; and a − D₀ = q + (Σx + ρ − f), ρ = a − p_k. Names of the parts: "phần tính cho điều phối", "phần được hồ sơ lịch sử giải thích", "phần còn lại" | A01, F09, K04, K19; FFA:91,133-136 |
| 3.7 | Cài đặt, kiểm thử và tái lập | 2,5 | Show the implementation can be checked | **Bảng 3.4** architecture (TEX/07-chuong3.tex:702-720; say "các thành phần chính", no line counts unless recounted). **H3.3 (new):** message flow FleetPy ↔ RideBound for one decision. Text: generator limits; tests 1.025/1.025 at the ADR-077 point (historical); 382.006 drop revisions recomputed with 0 mismatch; 13/13 items recomputed from raw records by a separate program; per-job wall time on the fixed-traffic set (median 730 / 667 / 641 s for FREE / LOCKS / C-30), per-decision overhead not measured; one sentence on complexity from the code (budget check loops over riders × 10 dimensions per candidate). Say plainly which checks were done by software agents | A24, A26, A27, A28, C19, H13; BE:75-98 |
| — | Slack | 0,5 | — | — | — |

### Chương 4. Thực nghiệm và đánh giá (26,5 pages)

**Opening sentence.** «Chương này đo luật C được gì và mất gì trên mô phỏng FleetPy, so với điều phối không trần, luật
hạn chót và cách đệm lời hứa, rồi xét lời hứa theo dự báo và những chỗ dự báo chưa đủ.»

Order follows the three parts: dispatch part (§4.2–4.6), forecast and padding (§4.7–4.8), the rest (§4.9), then validity
and discussion.

| § | Title | Pages | Purpose and content | Figures/tables | Evidence IDs |
|---|---|---:|---|---|---|
| — | Mở chương + **Bảng 4.0** "câu hỏi → mục → bảng/hình" (cleaned roadmap, no claims) | 0,5 | Map CH1–CH3 to sections | Bảng 4.0 | — |
| 4.1 | Thiết lập thực nghiệm | 3 | Scenarios, test sets, metrics with denominators; how B = 30 s was chosen: the level already used on the static set, not adjusted to the main set's results; analysis thresholds were chosen after looking at development data and some test scenarios had been viewed, so results are exploratory (data-reuse wording only; no plan language). Run-counting rule | **Bảng 4.1** scenario parameters (reuse TEX/08-chuong4.tex:49-68, updated). **Bảng 4.2** test sets: tập kiểm tra chính (34 kịch bản, 3.672 yêu cầu, 14–18/11/2018; 9 / 14 / 11 ở khung 7 / 8 / 17 giờ); tập chỉnh trần buổi sáng (8, 864, 12–13/11); tập tắc đường cố định (16, 1.728; bộ chạy cũ, không có luật phục hồi); chiều tuyết (8, 601 lượt). **Bảng 4.3** metrics (definition, strict ">", denominator, aggregation, "Vì sao đo") | B02–B11, B15, B16, B17, B20, C06, C08, I05, I06, I12; TEX/08-chuong4.tex:126-138 |
| 4.2 | Kết quả chính khi chưa có dự báo | 3,75 | **Answer:** «Trên 3.672 yêu cầu, luật C với trần 30 giây phục vụ 2.338 lượt, ít hơn điều phối không trần 96 lượt; số lượt trễ quá một phút so với lời hứa đầu giảm từ 203 xuống 76, nên số lượt không trễ quá một phút tăng từ 2.231 lên 2.262.» Fairness note first: luật hạn chót here is only its deadline component, at 30 s instead of 900 s, run with the same recovery rule. Served sets differ (2.207 chung; 227 / 131 riêng); C/M⁺ 2.332 chung, 6/6 riêng; by window −39 / −52 / −5 lượt; common riders wait +0,5 s, ride −10,5 s (post-treatment set) | **Bảng 4.4** (pooled counts): U, C-30, M⁺-30, M⁺-60, V-30 × phục vụ / trễ > 60 s / không trễ quá 60 s (trên 3.672) / không trễ quá 120 s (trên 3.672) / khách đi chung; M⁺-60 and V-30 late cells "chưa đưa vào bảng" unless scripted. **Bảng 4.5** (cell means, separate): quyết định bị ép, khách bị chính luật phá lời hứa, số kịch bản có ≥ 1 khách bị phá: C-30 0 / 0 / 0; M⁺-30 41,3% / 14,5% / 28; M⁺-60 22,5% / 4,2% / 22; V-30 53,8% / 21,6% / 34; pooled self-break M⁺-30 12,4%, M⁺-60 3,4%; 7-giờ M⁺-30 36,5% / 75,6%. **Bảng 4.6** lateness distribution U / C-30: > 1 / 2 / 5 / 10 phút and max, plus "lượt trễ quá T trên 100 yêu cầu" (5,53 / 2,78 / 0,49 / 0,05 and 2,07 / 0,30 / 0 / 0). **Bảng 4.7 (new script):** day × window differences C − U in late60 and timely60, number of scenarios where C is not worse; fallback: in all 25 scenarios of the 8 h and 17 h windows U has more late riders, at 7 h 3 more and 6 equal | C01–C08, C13, C14, C25, C26, C28, C30, J10, J11, A19, N-09 |
| 4.3 | Phần do điều phối: luật C chặn gì và mất gì | 2,25 | **Answer:** «Dưới luật C, 33 trong 2.338 khách có giờ trả bị điều phối dời, mỗi khách nhiều nhất 29,2 giây; khi không trần là 174 khách, nhiều nhất 590,1 giây.» Mechanism example (one rider: 79,0 s traffic part + 68,3 s dispatch part; the 90 s deadline blocks the plan, the 90 s cap accepts it; C takes exactly one more rider). Rejections: 148 requests finally rejected with at least one plan carrying a recorded budget prune (116 served by U); 1.186 others structural only; median smallest recorded overshoot 109,6 s; 2/148 had prior spending; 1.256 records ≠ 1.256 riders. Optional ≤ 0,25 p static-set paragraph with REG K29 wording → Appx A | **Bảng 4.8** exposure U vs C-30: riders moved 174 / 33; moved ≥ 2 times 12 / 0; max total 590,1 / 29,2 s; median per change 108,6 / 8,3 s; late60 ∧ moved 134/203 vs 4/76; ledger dispatch share 73,4% / 1,2% | C20–C24, D05, D13, D14, D16, D19, K10, K11 |
| 4.4 | Chọn mức trần | 3 | **Answer:** «Nới trần không cho một đường đơn điệu: trên 34 kịch bản chính, trần 120 giây phục vụ 2.387 lượt, nằm giữa trần 30 giây và không trần, nhưng có 2.366 lượt không trễ quá hai phút, nhiều hơn cả hai.» Two separate dials + the main-set point (Stage 1a, filled, §7) | **Bảng 4.9a** fixed-traffic set (integer counts): FREE / LOCKS / C-120 / C-60 / C-30 × phục vụ 1.629 / 1.584 / 1.563 / 1.540 / 1.534; trễ > 60 s 274 / 47 / 23 / 0 / 0; không trễ quá 120 s 1.465 / 1.557 / 1.563 / 1.540 / 1.534; đi chung % ; bị dời %. **Bảng 4.9b** morning dial (8 kịch bản): U, C-30 … C-300 × phục vụ / trễ > 60 s / không trễ quá 60 s / không trễ quá 120 s, plus luật hạn chót bị ép 58,6% → 1,7% (cell means), noting the forecast is inactive on 12–13/11. **Bảng 4.9c** main set (Stage 1a, §7). **H4.2 (new pgfplots):** served and late60 vs B, one line per set, never joined | D01–D04, D07–D11, K12, K13, K36, K52, N-06…N-11 |
| 4.5 | Phần cộng dồn của luật C: kiểm toàn bộ bản ghi | 1,25 | **Answer:** «Trong 98 lần chạy cũ dùng hệ số tắc đường đo, cả 1.256 bản ghi chặn đều do một lần dời vượt trần của cấu hình tương ứng; trên 34 lần chạy trần 120 giây của tập chính, 3 trong 524 bản ghi chỉ do cộng dồn.» Then: fixed traffic 2 records / 1 decision (C-60), 4 / 3 (C-120), all served; synthetic 4 records / 3 decisions after removing duplicates, 1 request finally rejected; for the 3 new main-set records, 2 of the 3 new requests ended not accepted under C-120 (one also not accepted under C-30), which is record-based, not proof that accumulation caused the loss. Definitional meaning: "mỗi lần ≤ 30 giây" allows 3 × 30 = 90 s; under U 12 of 2.434 riders were moved at least twice (one 25,844 + 99,027 = 124,871 s). The per-step arm was not run, so the effect on outcomes is unknown | **Bảng 4.10** cumulative audit by set: lần chạy, quyết định, bản ghi, chỉ do cộng dồn, khách phục vụ có ≥ 2 lần dời | E01–E10, K08, K09, K42, N-08 |
| 4.6 | Vai trò của trần và thứ tự ưu tiên chọn phương án | 2 (fallback 0,8) | Open: U and C-30 use the same policy file and stability-first selector and differ only in the drop cap, so C − U is the contrast of adding the cap with the selector unchanged; served sets differ, and whether the trade-off survives a cost-first selector is open. Fixed-state screen on the fixed-traffic set: choices change in 445/1.714 new-request decisions under LOCKS and 104/1.715 under C-30 (two different state populations); three cost estimands (7,79 / 8,00% conditional; 2,02 / 0,49% per decision; 0,3069 / 0,0794% ratio of summed plan costs, not operating cost); largest C-30 case 35,5 s over two riders (17,77 s each). **Stage 1b slot (1,5 p) or fallback (0,3 p), §7** | **Bảng 4.11** screen; Bảng 4.12-b (Stage 1b, if run) | A08, A14, A15, H01–H12, K15–K18, L02–L05 |
| 4.7 | Lời hứa theo dự báo | 3 | **Answer:** «Trên 21 kịch bản ngày thường có dự báo, tỉ lệ khách của luật C trễ quá một phút so với lời hứa giảm từ 6,01% xuống 0,17% [TB theo kịch bản; gộp theo khách 2/1.471].» Not specific to C (luật hạn chót and luật trần độ dời khách thấy also 0,17%; U 9,72% → 3,90%). Cost: lời hứa trả dài thêm 13,7 s, lời hứa đón 3,2 s (21 kịch bản). On all 34 scenarios (pooled): C-30 late60 76 → 10, extension 7,37 s; the 13 weekend scenarios keep the naive promise. Stretching by the true factors matches within 2 s for every rider with zero dispatch part (1.452/1.452; 2.305/2.305), so the world is nearly deterministic. Forecast inside the dispatcher (0,5 p): 3 of 32 runs stopped with no feasible plan; the deadline rule still forced in 47,6% of decisions (mean over 15 completed scenarios); deployment uses the promise layer. Machine learning (0,5 p, no table): fixed models with simple features gave no shown improvement; the uncapped FREE case cut late from 12,89% to 11,65% but 7,1% of riders arrived > 60 s early; vehicle state added nothing; describe the four conditions for "better" without saying when they were set | **Bảng 4.12** (21 kịch bản, cell means): không dự báo 6,01% / đệm cùng giá 1,94% / dự báo 0,17%; by window 14,44 → 0,27% (7 h), 1,35 → 0,18% (8 h), 0 → 0 (17 h). **H4.3 (new):** stacked ledger bars, weekday C-30 (82 / 5.353 / 783 s of 6.217 s) vs snow (8,6 / 251,5 / 3.185,9 s of 3.445,9 s) | F01–F12, F17, G02–G10, C09, K24, K37, K40 |
| 4.8 | So với cách đệm lời hứa: cần luật C để làm gì? | 2,75 | **Answer:** «Khi có dự báo, cộng thêm 30 giây vào mọi lời hứa của điều phối không trần cũng cho 2.328 lượt không trễ quá một phút như luật C và 2.366 so với 2.338 lượt không trễ quá hai phút; đổi lại, lời hứa dài thêm trung bình 37,2 giây thay vì 7,4 giây.» Then the argument of RD §8 (equal promise length, two-sided accuracy, tail, per-rider bound, comparison with the deadline rule, the C-120 point), each with its number; one paragraph "khi nào chọn trần, khi nào chọn đệm"; caveat that padded U is a replay on U's journeys, not a matched control; label this section "vai trò của từng thành phần" | **Bảng 4.13** (pooled, ≤ 6 columns, two blocks by promise length ≈ 7 s and ≈ 37 s): U + dự báo; C-30 + dự báo; C-120 + dự báo; U + dự báo + 30 s; C-30 + dự báo + 30 s; U + dự báo + 60 s × phục vụ / trễ > 60 s / không trễ quá 60 s (trên 3.672) / không trễ quá 120 s (trên 3.672) / tới sớm > 60 s / lời hứa dài thêm (s). **Bảng 4.14** tail: trễ > 120 / 300 / 600 s: U + dự báo + 30 s 68 / 11 / 1; C-30 + dự báo 0 / 0 / 0. **H4.1 (new pgfplots):** không trễ quá 60 s and 120 s per request vs mean promise extension, same points | C09, C10, C11, C12, C20, C26, K06, K51, N-01–N-04, N-06 |
| 4.9 | Khi dự báo không đủ: chiều tuyết 15/11/2018 | 1 | **Answer:** «Trên 601 lượt của chiều tuyết, dự báo lịch sử chỉ giảm số lượt trễ quá một phút từ 41 xuống 34 [gộp theo khách 5,66%; TB theo kịch bản 5,94%].» Replay variants with their information limits; ledger: dispatch 8,6 of 3.445,9 s; the prefix model explains 886,9 s more (25,7%), 2.299,0 s (66,7%) stays unexplained by the methods tried; one previewed event; 5 snow spells in the proposed future test period | **Bảng 4.15** replay: không dự báo 41; lịch sử 34; trộn chỉ trong khung 21; trộn có đoạn sáng 19 (dùng dữ liệu sáng không được giao, ngưỡng chọn sau khi xem); trộn trễ một khung 29 (mốc neo vẫn chính xác); đệm cùng giá 27 | B20, B26, F13–F16, I11, K19–K22, K25 |
| 4.10 | Kiểm tra tính hợp lệ của kết quả | 1,25 | 0 cap overshoots (max 29,2 s at 30 s; 118,9 s at 120 s); per-arm counters (cap applied 0, omitted by cap 0, work exhausted 0, 1 omitted request per arm); generator bounded, not exhaustive; 382.006 revisions cross-checked; 13/13 recomputed; U vs C-30 configuration differ only in the drop cap; "phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán" | — | A08, A24, A26, C19, K34, N-07; A:7-9 |
| 4.11 | Thảo luận và hạn chế | 2 | One paragraph: what the trade-off points mean for an operator, no business claim. Limits grouped as model / data / integration / generalisation, each "điều chưa làm → kết luận bị ảnh hưởng": one simulator; one city-wide factor, base speed at 00:00; dwell 0 s; load 0,535 riders per vehicle incl. idle vs ≈ 1,33 in a different FleetPy setup; selected trips shorter; 96-node OD closure; 5 days, dependent scenarios, one episode each; previewed data; no rider response; no vehicle reassignment; forecast pickup conflict; rebuilt binaries need an equivalence check; one hypothesis sentence on higher load, labelled as hypothesis; one hypothetical refund-contract sentence (symbolic money) | — | I01–I17, B05, B07, B12, B13, F07, C28, C29 |
| — | Slack | 0,75 | — | — | — |

### Chương 5. Kết luận (3 pages)

**Opening sentence.** «Khóa luận đã đặc tả, cài đặt và đo một trần cho phần dời giờ trả do điều phối của từng khách
trong dịch vụ đi chung xe; chương này tóm tắt kết quả theo ba phần của độ lệch giờ trả, nêu hạn chế và hướng tiếp theo.»

| § | Title | Pages | Purpose | Evidence IDs |
|---|---|---:|---|---|
| 5.1 | Tổng kết theo ba phần | 1,5 | One paragraph per part with its headline count and denominator; cite Hörl–Zwick again | C02, C08, C13, C10, N-06, E01, N-08, F04, F13 |
| 5.2 | Hạn chế | 0,5 | Point to §4.11; state the overlap with prior work in the spirit of TEX/09-chuong5.tex:91-102 | J38, K30, K31 |
| 5.3 | Hướng phát triển | 1 | ≤ 5 items, "Thứ nhất…": (1) luật mỗi lần một trần so với luật cộng dồn trên quỹ đạo thật; (2) hạn chót nới kiểu Hörl–Zwick max(p₀ + B, e) làm đối chứng; (3) dự báo cho ngày có sự kiện với dữ liệu đúng thời điểm và nhiều sự kiện độc lập (no hour estimate); (4) tải cao hơn, tắc đường theo đoạn đường, mô hình phản ứng của khách, ngưỡng thật của hãng xe; (5) trần theo độ dài chuyến và điều kiện kiểm tra giờ đón. If Stage 1b is not run, put the selector × cap test first | E09, K27, B26, I02, I04, I07, I10, D18, J25 |

### Tài liệu tham khảo (4 pages)

- Fix the heading: TEX/10-tai-lieu.tex:1-4 prints a near-empty "Tài liệu tham khảo" page and then "Bibliography" (PDF
  p. 102-103). Rename `\bibname` and drop the extra `\chapter*`.
- Split "Tiếng Việt" / "Tiếng Anh" per STYLE rule 35 unless the UET template says otherwise.
- Add only what the text cites: Hörl & Zwick 2022 (J01-J04); Leonardi et al. 2024 (J21); FleetPy ETRR 2026 (J18); Wardman
  et al. 2026 (J23); Mt-KaRRi (J32); Lu & Kühnel 2024 (J22); UberX Share page (J28). Ding, Dandl & Bogenberger only after
  the paper is opened (J41 UNVERIFIED). Elmi 2026 (J12) and "anticipatory walking" (J16) are UNVERIFIED in the register:
  open the originals before citing details.
- Drop the eight uncited entries unless a sentence cites them (TEX/10-tai-lieu.tex; RD CX-66).

### Phụ lục (≤ 3 pages)

| Appendix | Pages | Content | Condition / wording |
|---|---:|---|---|
| A. Tập kịch bản tĩnh (20 kịch bản) | ≤ 1 | The 89,06% table, the cap ladder with its ±0,3 point noise floor, one line on the endpoint measure (774 of 1.581 served riders, 49,0%) | Only after each number is re-anchored to its output file (E12); wording REG K29, K33, K34; otherwise omit |
| B. Phương án giữ nguyên dưới các luật | ≤ 1 | Table: luật / phương án giữ nguyên luôn qua? / vì sao: C yes by construction; luật hạn chót no (traffic alone can trigger it); luật trần độ dời khách thấy no; Hörl–Zwick-style max(p₀ + B, e) yes (inference); remaining counterexamples CE-1, CE-4…CE-6 in one line each | REG A10, A22, K02; TEX/07-chuong3.tex:641-663; no four-family theorem, no prediction tallies |
| C. Tái lập | 1 | Test sets and scenario lists; configurations (U, C-30, C-120, M⁺-30, M⁺-60, V-30, the dials); runner identity; output roots; how runs are counted (runs used per set; inventory 1.991 run records); how numbers were recomputed | REG A08, A28, B19, C19; no plan hashes, no sealing words |

---

## 6. Contribution (§1.4)

### 6.1 The paragraph (Vietnamese; 321 tiếng by whitespace count, about 7% over the ~300 target; 10 distinct numbers, not counting the citation year; no symbols. If it must be cut, drop "vốn đã có trong thực tiễn" last, never the unfavourable clauses)

> **Đóng góp của khóa luận.** Giờ trả đã hứa với khách đi chung xe có thể bị dời mỗi khi bộ điều phối ghép thêm khách.
> Khóa luận đặc tả và cài đặt trong RideBound luật C: với mỗi khách đã được nhận, tổng độ lớn các lần dời giờ trả do
> điều phối trong cả chuyến không được vượt một trần cố định; nếu vượt, phương án bị loại. Mỗi lần dời được đo so với
> giờ trả khi giữ nguyên kế hoạch cũ, tính lại theo trạng thái hiện tại. Mốc này đã có ở Hörl và Zwick (2022); luật C
> khác ở chỗ dùng một trần chung cho mọi khách, không nới theo tắc đường và cộng qua cả chuyến. Luật C đi cùng lời hứa
> theo hồ sơ tắc đường lịch sử, vốn đã có trong thực tiễn, và một sổ chia độ trễ theo từng khách. Trên mô phỏng FleetPy
> với hệ số tắc đường toàn thành phố lấy từ dữ liệu Manhattan (34 kịch bản, 3.672 yêu cầu), với trần 30 giây, luật C
> phục vụ ít hơn điều phối không trần (vẫn giữ các khóa) 96 lượt nhưng thêm 31 lượt không trễ quá một phút so với lời
> hứa đầu. Luật hạn chót tính từ lời hứa đầu phục vụ cùng số lượt nhưng không giữ được điều nó hứa với ít nhất một khách
> ở 28 trên 34 kịch bản; luật C giữ được ở mọi kịch bản, theo cấu tạo. Khi có dự báo, cộng thêm 30 giây vào mọi lời hứa
> của điều phối không trần cũng cho cùng số lượt không trễ quá một phút như luật C, và hơn ở ngưỡng rộng hơn, nhưng lời
> hứa dài thêm trung bình 37,2 giây thay vì 7,4 giây. Trên các lần chạy dùng hệ số tắc đường đo, phần cộng dồn chỉ là lý
> do riêng của 3 bản ghi chặn, đều ở mức trần nới rộng; tác dụng của nó lên kết quả chưa được đo.

### 6.2 Side table (every number and every load-bearing clause)

| Number / clause | Meaning, denominator, aggregation | Evidence |
|---|---|---|
| "khách đã được nhận" | Budget applies in the accepted, waiting-pickup and on-board phases | A06, A13; CFG30:17-23; BE:107-114 |
| "tổng độ lớn … trong cả chuyến"; "nếu vượt, phương án bị loại" | Σ\|c\| ≤ B, remaining = B − used; hard filter before the solver | A06, K43 |
| "so với giờ trả khi giữ nguyên kế hoạch cũ, tính lại theo trạng thái hiện tại" | c = p − e; e from the current position and travel times | A01, A02 |
| "Mốc này đã có ở Hörl và Zwick (2022)" | Old route recomputed under current traffic; max(updated, latest) | J01, J03 |
| "một trần chung cho mọi khách, không nới theo tắc đường và cộng qua cả chuyến" | HZ relax only for at-risk on-board riders, traffic-dependent, not accumulated | J05 (inference from two definitions) |
| "vốn đã có trong thực tiễn" | Forecast quoting is prior practice | J21, J35, K37 |
| 34 | Scenarios of the main test set | B09 |
| 3.672 | Requests = 34 × 108 | B09 |
| 30 giây | The cap of C-30; also the pad of the padded comparator | A06; C10 |
| "vẫn giữ các khóa" | U = C-30 without the drop cap | A08, K50 |
| 96 | 2.434 − 2.338 served `[đếm]`, on 3.672 requests | C01, C02 |
| 31 | Not later than 60 s vs the first naive promise: 2.262 − 2.231 `[trên yêu cầu]` | C08 |
| một phút | Threshold 60 s, strict ">" for late | C06, C08 |
| 28 trên 34 | Scenarios where the 30 s deadline rule broke its own promise for ≥ 1 rider; C-30: 0 of 34 | C13 (T38A:76-77) |
| "theo cấu tạo" | Keep-route has c = 0; C-30 never forced | A21, A22 |
| "cùng số lượt không trễ quá một phút" | 2.328 = 2.434 − 106 (U + forecast + 30 s) = 2.338 − 10 (C-30 + forecast) `[trên yêu cầu]` | C09, C10 |
| "hơn ở ngưỡng rộng hơn" | At 120 s: 2.366 vs 2.338 `[trên yêu cầu]` | C10 |
| 37,2 / 7,4 giây | Mean promise extension: 90.504.227,8 ms / 2.434 and 17.224.334,6 ms / 2.338 `[gộp theo khách]` | C10, F06; A:7,9 |
| 3 | Cumulative-only records among 1.780 recorded budget prunes (1.256 in 98 earlier runs + 524 in 34 C-120 runs) [A] | E01, N-08 |
| "đều ở mức trần nới rộng" | All 3 under C-120 on the main set; 0 at C-30 | N-08; A:7 |
| "tác dụng … chưa được đo" | Per-step arm never run | E09, K08 |

### 6.3 Kết quả chính (five lines under the paragraph)

- Phục vụ trên 3.672 yêu cầu: không trần 2.434 lượt; luật C trần 30 giây 2.338; luật hạn chót 30 giây 2.338 (2.332 lượt
  chung). [C01, C04]
- Không trễ quá một phút so với lời hứa đầu: 2.231 và 2.262 lượt trên 3.672 yêu cầu; trễ quá một phút: 203 và 76 lượt;
  khách đi chung: 555 và 313. [C06, C08, N-09]
- Khi có dự báo: cùng 2.328 lượt không trễ quá một phút cho luật C và cho không trần cộng 30 giây; không trễ quá hai phút
  2.338 và 2.366; lời hứa dài thêm 7,4 và 37,2 giây; tới sớm quá một phút 4/2.338 và 44/2.434. [C09, C10]
- Trần 120 giây trên cùng 34 kịch bản: phục vụ 2.387 lượt; không trễ quá một phút 2.255 và không trễ quá hai phút 2.366;
  khi có dự báo 2.322 và 2.379, lời hứa dài thêm 7,3 giây. [N-06]
- Phần cộng dồn: trên 132 lần chạy dùng hệ số tắc đường đo, 3 trong 1.780 bản ghi chặn chỉ do cộng dồn, đều ở trần 120
  giây; luật mỗi lần một trần chưa được chạy. [E01, N-08, E09]

### 6.4 Box "Khóa luận không nhận là mới" (§1.4)

| Đã có trong nghiên cứu trước hoặc trong thực tiễn | Khóa luận dùng thế nào |
|---|---|
| Giờ trả cập nhật theo tắc đường trên tuyến cũ, và nới hạn trả dựa trên mốc đó (Hörl và Zwick, 2022) | Dùng cùng mốc để đo phần dời do điều phối |
| Đo độ bất ổn của lời hứa, kiểm soát trước quyết định, đánh đổi giữa phục vụ và ổn định (Fielbaum và Alonso-Mora, 2020) | Dùng ý; đo trên mô phỏng có tắc đường thay đổi |
| Bảo đảm theo từng khách (Elmi và cộng sự, 2026) | Dùng ý |
| Hạn chót tính từ lời hứa đầu (Schulz và Pfeiffer, 2026) | Cài lại phần hạn chót làm đối chứng, ở mức chặt hơn nhiều |
| Lời hứa theo dự báo; dự báo thời gian đi theo giờ trong ngày | Dùng lại, tính trên các lần chạy đã ghi |
| Chèn khách động, gán lại xe, giới hạn giờ đến, luật phục hồi "không tệ hơn" | Dùng bộ sinh chỉ chèn thêm; không gán lại xe |
| **Phần khóa luận làm** | Đặc tả, cài đặt và kiểm một trần chung cho mọi khách đã nhận trên tổng độ dời giờ trả do điều phối trong cả chuyến, có sổ theo từng khách; đo đường đánh đổi giữa phục vụ, đúng giờ và độ dài lời hứa |

Bốn điều khóa luận không khẳng định:
- Luật C không phục vụ nhiều hơn và không cho nhiều lượt đúng giờ hơn: nó phục vụ bằng luật hạn chót; so với cách đệm có
  dự báo, nó hòa ở ngưỡng một phút và kém ở ngưỡng hai phút.
- Luật C không bảo đảm giờ đến thực tế; nó chỉ chặn phần do điều phối.
- Sổ theo từng khách là phép tính theo mô hình, không kết luận ai có lỗi; phần còn lại không phải phần "không thể biết
  trước".
- Kết quả không suy rộng sang thành phố, mức tải hay mạng đường khác; không mức trần nào được gọi là tối ưu; khóa luận
  không nói về lợi ích kinh doanh.

Evidence: J01, J03, J05–J10, J12 (UNVERIFIED), J16 (UNVERIFIED), J21, J35, J38, K05, K06, K19, K36, K38.

---

## 7. Stage slots

### 7.1 Stage 1a — filled (§4.4, Bảng 4.9c, ≈ 1 page)

Sources: STG (Claude, 102 transcripts re-read, all 14 archived baselines reproduced, STG:9-23) and CXS (Codex v4 analyzer,
same 102 runs, CXS:3,76-91). The two agree on every number used here.

**Bảng 4.9c — tập kiểm tra chính, 3.672 yêu cầu mỗi cấu hình, lời hứa đầu không dự báo trừ khi ghi "có dự báo".**

| | Không trần | Trần 30 giây | Trần 120 giây |
|---|---:|---:|---:|
| Phục vụ | 2.434 | 2.338 | 2.387 |
| Trễ quá 60 s / 120 s / 300 s (trong số được phục vụ) | 203 / 102 / 18 | 76 / 11 / 0 | 132 / 21 / 0 |
| Không trễ quá 60 s / 120 s (trên 3.672) | 2.231 / 2.332 | 2.262 / 2.327 | 2.255 / 2.366 |
| Có dự báo: không trễ quá 60 s / 120 s (trên 3.672) | 2.297 / 2.347 | 2.328 / 2.338 | 2.322 / 2.379 |
| Có dự báo: lời hứa dài thêm trung bình (s) | 7,18 | 7,37 | 7,27 |
| Khách đi chung | 555 (22,80%) | 313 (13,39%) | 428 (17,93%) |

(Table has 4 columns; the dispatch-exposure rows go in the text to keep the table readable.)

**Text (two paragraphs, values only from N-06…N-11).**
- So với trần 30 giây, trần 120 giây phục vụ thêm 49 lượt, có thêm 56 lượt trễ quá một phút, ít hơn 7 lượt không trễ quá
  một phút và thêm 39 lượt không trễ quá hai phút, trên cùng 3.672 yêu cầu. Khi có dự báo: ít hơn 6 lượt ở ngưỡng một
  phút, thêm 41 lượt ở ngưỡng hai phút, lời hứa dài thêm gần như bằng nhau (7,27 so với 7,37 giây). Ở ngưỡng hai phút,
  trần 120 giây cao hơn cả hai điểm đầu mút đã đo; không trần không phải cận trên (REG K12), và kết quả này cùng chiều với
  tập chỉnh trần buổi sáng (666 lượt ở trần 120 giây so với 665 khi không trần, REG D01).
- Dưới trần 120 giây, 103 khách (4,32%) có giờ trả bị điều phối dời, không ai bị dời từ hai lần, tổng lớn nhất 118,9 giây,
  0 quyết định bị ép và 0 lần vượt trần; 524 bản ghi chặn gồm 521 bản ghi một lần dời vượt trần và 3 bản ghi chỉ do cộng
  dồn (§4.5).
- Hai tập khách khác nhau: 2.266 lượt chung với trần 30 giây, 121 chỉ có ở trần 120 giây (93 trong số đó cũng được phục
  vụ khi không trần), 72 chỉ có ở trần 30 giây. So từng kịch bản, trần 120 giây phục vụ nhiều hơn trần 30 giây ở 23 kịch
  bản, bằng ở 8, ít hơn ở 3. Theo khung giờ, phần phục vụ thêm và phần trễ thêm tập trung ở khung 8 giờ (1.001 so với 975
  lượt; 49 so với 15 lượt trễ quá một phút) và 17 giờ (871 so với 852; 20 so với 0).

**Wording rules.** "Một điểm đo thêm trên đường đánh đổi", never "tối ưu" (REG K36). Do not write "lấy lại 49 trong 96
lượt" (cohorts differ, N-10). Do not mention the plan, its predictions or pass/fail (owner override; STG §10 and CXS:58-64
stay internal). Add the C-120 row to H4.2 as its own marker.

### 7.2 Stage 1b — slot with fallback (§4.6)

- **Prerequisites** (R18 §3): the cost-first option in code; 4 equivalence jobs (U / C-30 × one 8 h and one 17 h scenario)
  that must reproduce the archived results exactly; 2 smoke runs; 68 main jobs (CF-U, CF-C30 on 34 scenarios). The owner
  already approved the staged study (R19C:3-5); no further permission is needed, but any equivalence mismatch stops it.
- **If run (1,5 p): Bảng 4.12-b** rows {ưu tiên ổn định (đã có), ưu tiên chi phí} × {không trần, trần 30 giây}; columns
  phục vụ / không trễ quá 60 s / trễ quá 60 s / không trễ quá 120 s / khách đi chung (exact counts) / lời hứa dài thêm;
  text with the interaction I_L = (L_CF,U − L_CF,C30) − 127 and the identity I_L = I_served − I_timely60, with per-day and
  per-scenario signs (R18:236-251). Reading rules R18:195-206: missing a target is not proof the selector is irrelevant;
  never write "chính trần, không phải bộ chọn, giữ lời hứa" (REG K18).
- **Fallback (0,3 p):** «Phép thử đổi thứ tự ưu tiên của bộ chọn trên 34 kịch bản chính chưa được chạy; bằng chứng hiện
  có là phép sàng lọc trên trạng thái cố định ở trên, vốn không cho biết kết quả phục vụ và đúng giờ trên quỹ đạo.» The
  item becomes the first future direction in §5.3.
- Cutoff: set by the owner; write the fallback version first and upgrade only with audited numbers (RD LR-53).

---

## 8. New figures and tables to produce

| ID | Type | Content | Data source |
|---|---|---|---|
| H1.1 | TikZ | Two simulated riders on time axes | D06 (`tang3/w07/W07-REPORT.md:48-54`); C31 (EXAMPLE:1-4,8,43,60-61) |
| H1.2 | TikZ | Three parts → three places | Text only |
| H3.1 | TikZ (edit) | Decision loop | TEX/07-chuong3.tex:24-45 |
| H3.2 | TikZ | Insertion example with x, c, z arrows | Bảng 3.1 numbers (TEX/07-chuong3.tex:126-140) |
| H3.3 | TikZ | FleetPy ↔ RideBound messages for one decision | A28; RUN38 (`tang3/t38/run_t38.py`) |
| Giải thuật 3.1 | algorithm | One decision cycle | A06, A14, A17, A18, A24 (code: SEL, POL, VALID) |
| Giải thuật 3.2 | algorithm | Forecast promise | F01, F02 (`optimize/display_layer.py:36-72`, `optimize/promise_stretch.py:29-68`) |
| Bảng 1.1 / 2.2 | table | Positioning (short / full) | J01–J12, J32, J35 |
| Bảng 2.1 / 3.2 / 3.3 / 3.4 | table | Constraints; constraints of a plan; rules; architecture | B03; A06–A11, A14–A19; TEX/07-chuong3.tex:702-720 |
| Bảng 4.0 | table | Questions → sections | §5 Ch. 1 research questions |
| Bảng 4.4 / 4.5 / 4.6 | table | Main results (pooled); obligations (cell means); lateness distribution | C01–C08, C13, C14, C25–C28, N-09 |
| Bảng 4.7 | table | Day × window C − U differences | **New read-only script** over `DEB/codex-work/R15-audit.json` per-cell records (as R18 NEW:4 did); fallback C30 |
| Bảng 4.8 | table | Dispatch exposure U vs C-30 | C20–C24 |
| Bảng 4.9a / 4.9b / 4.9c | table | Fixed-traffic dial; morning dial; main-set point | D08, D09; D01, D02, D04; N-06…N-11 |
| H4.2 | pgfplots | Served and late60 vs B per set | D01, D02, D09, N-06 |
| Bảng 4.10 | table | Cumulative audit by set | E01–E04, N-08 |
| Bảng 4.11 | table | Fixed-state selector screen | H03–H09 |
| Bảng 4.12 / H4.3 | table / pgfplots | Forecast on 21 scenarios; ledger bars weekday vs snow | F04, F08, F09, F13, F15 |
| Bảng 4.13 / 4.14 / H4.1 | table / table / pgfplots | Forecast + padding at matched promise length; tail; frontier | C09–C11, N-01–N-04, N-06 (A:7-9; STG:32-34) |
| Bảng 4.15 | table | Snow replay | F14 |
| Bảng 4.12-b | table | Stage 1b (only if run) | Future audited output |

---

## 9. New evidence rows to add to the register (verified this session)

| ID | Statement | Value | Anchor | Status |
|---|---|---|---|---|
| N-01 | Tail with forecast: U + forecast + 30 s vs C-30 + forecast, late > 120 / 300 / 600 s | 68 / 11 / 1 vs 0 / 0 / 0 | A:9 (`fc_pad30`), A:7 (`fc`) | VERIFIED (read) |
| N-02 | C-30 + forecast + 30 s | served 2.338, late60 2, early60 44, extension 87.364.334,6 ms / 2.338 = 37,37 s | A:7 (`fc_pad30`) | VERIFIED (read) + [A] mean |
| N-03 | U + forecast, no pad | late60 137, late120 87, early60 8, extension 7,18 s | A:9 (`fc`); STG:32 | VERIFIED |
| N-04 | Within ±60 s of the first promise, per 3.672 requests | C-30 + fc 2.324; U + fc + 30 s 2.284; U + fc 2.289; C-30 + fc + 30 s 2.292 | served − late60 − early60 from A:7,9 | [A] — recompute by script and confirm the early/late definitions are disjoint |
| N-05 | Net earlier dispatch change of the drop promise | U 2 of 174; C-30 4 of 33; C-120 3 of 103 riders; C-30 earlier total ≤ ≈ 0,56 s | BUC:34,37; STG:37-39; A:7 `S_sum_exposed_ms` 359.173 | counts VERIFIED; bound [A] from rounding — recount before use |
| N-06 | Stage 1a outcomes (C-120, 34 scenarios) | served 2.387; late60 / 120 / 300 132 / 21 / 0; early60 1; timely60 2.255; timely120 2.366; forecast late60 65, late120 8, early60 2, timely60 2.322, timely120 2.379, extension 7,27 s | STG:29,34; CXS:76,79 | VERIFIED by two analyses |
| N-07 | Stage 1a dispatch and validity | 103 exposed (4,32%); 0 with ≥ 2 changes; max Σ\|c\| 118,9 s; 0 overshoot; 9 riders ≥ 0,9 B; 0 forced decisions in 20.435 | STG:39,44 | VERIFIED |
| N-08 | Stage 1a prune records | 524 = 521 single-step + 3 cumulative-only, in 3 decisions; of the 3 new requests 2 not accepted under C-120 (one also not accepted under C-30), 1 served | STG:44-47; CW21:2-7; CXS:91 | VERIFIED; record-based, not causal |
| N-09 | Exact shared completions | U 555 / 2.434 (22,80%); C-30 313 / 2.338 (13,39%); C-120 428 / 2.387 (17,93%) | STG:50-52 | VERIFIED; supersedes the "≈" note of REG C25 |
| N-10 | Served-set overlaps | C-120 vs C-30 2.266 / 121 / 72; C-120 vs U 2.271 / 116 / 163; 93 of the 121 also served by U | STG:55-58 | VERIFIED |
| N-11 | Stage 1a per window and per scenario | served 515 / 1.001 / 871 (C-120) vs 511 / 975 / 852 (C-30) at 7 / 8 / 17 h; late60 63 / 49 / 20 vs 61 / 15 / 0; C-120 more served than C-30 in 23, equal 8, fewer 3 scenarios | STG:61-73 | VERIFIED |
| N-12 | Thesis inventory facts | bibliography heading bug; list of tables starts xii; 49,0% = 774 / 1.581 served | TEX/10-tai-lieu.tex:1-4; PDF p. 8, 102-103; TEX/08-chuong4.tex:160,1728 | VERIFIED (read) |
| N-13 | DACN front matter | two Vietnamese covers, English cover, acknowledgement, Tóm tắt, Abstract | DACN PDF 1-6 | VERIFIED (read) |
| N-14 | Stage 1b approval | owner approved the staged study incl. Stage 1b | R19C:3-5 | VERIFIED (read) |
| N-15 | 132 runs / 1.780 records on measured traffic | 98 + 34 runs; 1.256 + 524 records; 3 cumulative-only | E01; N-08 | [A] |

Register rows to update: **L01** (now filled by N-06…N-11), **D12** (C-120 now run on the 34 scenarios), **E01 / I17 /
K08** (add the 3 Stage 1a records; "never the sole reason" now holds only for the 98 earlier runs), **C25** (exact counts).

---

## 10. Open items only the owner can close

1. Title option 1 or 2 (§1), and whether renaming is still allowed.
2. Supervisor name (both covers, acknowledgement).
3. UET template: inner cover? "Lời cam đoan"? references split by language? (each +1 p or 0).
4. Stage 1b cutoff date (the mid-November deadline is UNVERIFIED, REG I16).
5. Appendix A: re-anchor the static-set numbers or drop the appendix.

*End of outline V2. Written by Claude (outline consolidator), 2026-10-11; only this file and REVIEW-DECISIONS-R20.md
were written.*
