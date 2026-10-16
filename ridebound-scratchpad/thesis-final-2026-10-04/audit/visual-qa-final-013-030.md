# Final visual QA: physical PDF pages 013–030

Artifact: build/main.pdf (68 pages), thesis-final-2026-10-04.
Renders reviewed: audit/final-layout-v4/page-013.png through page-030.png.
Method: inspected every individual full-page PNG using tools.view_image with detail original; no contact-sheet substitution.

SHA-256 before review: E7A4712663AD2167F2BBBFFD7330FA0C64A580964CFF558B3D3DC2ECBA14454C
SHA-256 after review: E7A4712663AD2167F2BBBFFD7330FA0C64A580964CFF558B3D3DC2ECBA14454C
Both hashes obtained with PowerShell Get-FileHash. PDF remained unchanged.

Review criteria: Vietnamese and math glyph rendering; clipping and overlap; figure and table readability, labels and rules; stranded headings and single-line widows; page-number and margin fit.

| Physical page | Printed page | Result | Visual review notes |
| --- | --- | --- | --- |
| 013 | 1 | PASS | Chapter 1 and section 1.1 headings fit; Vietnamese text and citations render clearly. Two-line italic continuation is retained across the page break; no single-line widow. |
| 014 | 2 | PASS | Italic continuation, section 1.2 and RQ1–RQ3 list are readable and clear of margins; no stranded heading or overlap. |
| 015 | 3 | PASS | Section 1.3, bold run-in contribution labels, and Vietnamese diacritics are intact; paragraph continuation is balanced across the page break. |
| 016 | 4 | PASS | Sections 1.4 and 1.5 have sufficient following text; paragraphs, citations, and footer fit without clipping. |
| 017 | 5 | PASS | Chapter 2, section 2.1 and subsections 2.1.1–2.1.2 have clear hierarchy and following body text; all glyphs are readable. |
| 018 | 6 | PASS | Equations 2.1–2.4 and their subscripts, summations, Gamma and inequalities render correctly; section 2.2 and subsection 2.2.1 fit. |
| 019 | 7 | PASS | Subsection 2.2.2, equation 2.5 and body text are readable, with no clipping, overlapping labels or isolated heading. |
| 020 | 8 | PASS | Table 2.1 caption, column headings, wrapped cells and horizontal rules are readable and contained. Section 2.3 has two following lines before the page break. |
| 021 | 9 | PASS | Inline summation and subscripts are legible; sections 2.4 and 2.5 fit. Section 2.5 has two body lines before continuing. |
| 022 | 10 | PASS | Chapter-ending continuation has clear Vietnamese glyphs and consistent margins; remaining white space is an ordinary chapter-end layout. |
| 023 | 11 | PASS | Chapter 3, sections 3.1–3.2 and subsection 3.2.1 fit with readable body text and no stranded heading. |
| 024 | 12 | PASS | Subsection 3.2.2, section 3.3, definition list and equations 3.1–3.3 are readable and correctly aligned. |
| 025 | 13 | PASS | Figure 3.1 timeline, point markers, arrows, times, labels and two-line caption are sharp and separated; surrounding math and Vietnamese text fit. |
| 026 | 14 | PASS | Sections 3.4–3.5, equation 3.4 and definitions 3.1–3.2 render correctly; long implementation identifiers remain within margins. |
| 027 | 15 | PASS | Subsections 3.5.2–3.5.3, boxed equation 3.5, run-in labels and math symbols are readable; bottom paragraph has several lines before continuing. |
| 028 | 16 | PASS | Subsection 3.5.4 and theorems 3.1–3.3 render clearly; proof-end squares are correct symbols, and theorem continuation is not a single-line widow. |
| 029 | 17 | PASS | Two-line theorem continuation, proof, inequalities, run-in labels and corollary 3.4 are readable and clear of margins; no overlap or clipping. |
| 030 | 18 | PASS | Subsection 3.5.5, equations 3.6–3.8, proposition 3.5 and proof render correctly; sums, absolute values and proof-end square are intact. |

Outcome: all 18 assigned pages PASS. Zero visual defects found in the inspected range. Only this requested audit report was written; no source, PDF, build or other audit files were modified.
