# Full-page visual QA: PDF pages 031–048

Audit date: 2026-10-05. Source PDF: `build/main.pdf` (70 pages, as supplied for this QA). Exact SHA-256, checked both before and after inspection:

`2837147ab187bb837cbe080a41583240cdf64f19d7a175550ed7d9a077d3b0ef`

Each of the 18 individual full PNGs in `audit/final-layout-v2/page-031.png` through `page-048.png` was opened with `view_image` at original detail. Each image is 1075 × 1521 pixels. This ledger is based on those individual visual inspections, not text extraction or a contact sheet. No source, PDF or rendered page was edited.

Across these pages, Vietnamese diacritics, italic/bold text, mathematical sums/subscripts/superscripts, inequality signs, monospace identifiers, table cells, headings and footers are legible. No clipping, margin overflow, unintended missing-glyph boxes, overlapping text or cut-off figure/caption was detected. Hollow squares at proof endings are intentional QED symbols. One chapter-end whitespace issue remains on page 039.

| PDF page | Printed page | Visual ledger | Result |
|---|---:|---|---|
| 031 | 19 | Table 3.1: four gate families, formula column and wrapped example text fit inside rules; no cell collision. Theorem 3.6, inline symbols and displayed threshold equation are clear. Body margins and footer are consistent. | Pass |
| 032 | 20 | Proof continuation and QED square render correctly. Corollaries 3.7/3.8, large summation displays and positive-part superscripts remain legible and within margins. Paragraph continuation at page end is ordinary. | Pass |
| 033 | 21 | Proposition 3.9 and proof fit; section 3.6 begins with enough body content below it. No heading orphan, equation clipping or excessive interior whitespace. | Pass |
| 034 | 22 | Sections 3.7.1/3.7.2 and recovery-rule paragraphs are clear. `normalOperation=false` and `validationWorkUnits` fit without clipping. Lower whitespace is moderate and the following subsection starts on the next page. | Pass |
| 035 | 23 | Conditional inequality (3.9) and calibration expression render cleanly. Table 3.2 has readable responsibility rows and consistent rules. Long component identifiers in the closing paragraph remain within the body. | Pass |
| 036 | 24 | New selector subsection 3.8.2: assignment constraints are centered and readable; both summations and index conditions render clearly. Numbered procedure items 1–3 fit and continue normally on the following page. | Pass |
| 037 | 25 | Procedure items 4–6 follow correctly. Selector objective equations, U/R definitions, scaled utilization formula and the explicit zero-stop-duration statement are clear. Dense text remains readable with normal line spacing. | Pass |
| 038 | 26 | Objective/recovery exception paragraphs and sealed-evidence subsection render without overflow. Final paragraph spills to page 039 after the phrase “lỗi hạ”; see the following row for the resulting layout issue. | Pass, with continuation-related issue on 039 |
| 039 | 27 | Only two continuation lines appear at the top: “tầng phải theo quy tắc đã ghi, giữ thư mục lỗi và chỉ rõ bản dùng. Các kiểm tra này hỗ” and “trợ tái lập; giới hạn dữ liệu và suy luận thống kê vẫn còn.” The rest of the chapter-end page is blank except its footer. This is no longer a single word, but it is still an isolated two-line tail rather than a complete closing paragraph. | **Layout issue: excessive chapter-end whitespace** |
| 040 | 28 | Chapter 4 opening, section 4.1 and subsection 4.1.1 have proper hierarchy and spacing. Main input/network description and the new normalization subsection start clearly. No heading or body clipping. | Pass |
| 041 | 29 | Table 4.1: four columns and wrapped row cells remain readable with no overlap. The new node-selection/HMAC/normalization recipe is clear. Long filenames fit in the body. Initial-fleet paragraph and subsection 4.1.3 begin normally. | Pass |
| 042 | 30 | New self-contained Table 4.2 is readable; ride-limit, zero-dwell, horizon/drain and solver rows fit. `service-set-stability-portfolio-v1` stays inside its cell. Table 4.3 also fits fully, with distinct H6/Tier 2/T38 rows and readable abbreviated hashes. Captions and lower explanatory paragraph are intact. | Pass |
| 043 | 31 | Provenance paragraph, policy comparison and metric definitions render cleanly. Hash prefixes/`reproducibility-config.json` fit. Strict > versus ≥ inequality glyphs are distinct. No bad whitespace or orphan heading. | Pass |
| 044 | 32 | Table 4.4: all quantity labels, B1/C1 totals and decimal separators are legible and separated; final long label does not collide with numeric values. Caption and subsequent interpretation fit within margins. | Pass |
| 045 | 33 | Concentration and absolute-value discussion is clear; A+d>B and related math render properly. RQ2 heading and subsection 4.3.1 have sufficient following content. | Pass |
| 046 | 34 | Table 4.5 is centered and fully contained; configuration labels, five headers and numeric columns are readable. Caption, paragraphs and bottom spacing are balanced. | Pass |
| 047 | 35 | Figure 4.1 is crisp and fully visible. Both legend entries, circle/square markers, line styles, y-axis ticks/title, x-axis labels/title and caption are readable. No cropped axis, overlapping caption or figure overflow. Text beneath the figure fits. | Pass |
| 048 | 36 | Section transitions 4.3.4 → 4.4 → 4.4.1 are clean. Drift-factor expression, M+/M notation and the 19/20 versus 0/20 comparison remain legible. No margin or glyph issue. | Pass |

Suggested correction for the sole issue: fit the complete final 3.8.3 closing paragraph onto page 038, or move enough preceding content to page 039 to make it a substantive closing page. After any correction, the resulting PDF must be re-rendered and inspected under its new hash; this ledger applies only to the exact PDF hash above.

Verdict for the assigned range: 18/18 full individual pages inspected; no clipping/overlap/glyph/table/figure defect found; one precise page-break/whitespace issue on PDF page 039 (printed 27), communicated to the parent agent.
