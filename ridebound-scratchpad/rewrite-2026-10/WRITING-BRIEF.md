# Writing brief for every chapter writer (thesis rewrite, 2026-10-11)

Paths are under `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/` unless absolute.

## Authoritative inputs (read before writing)

1. `OUTLINE-V2.md` — the structure, page budgets, purposes, figures/tables and evidence IDs. It overrides the first
   outline. `REVIEW-DECISIONS-R20.md` explains why; follow its decisions.
2. `style/STYLE-GUIDE-VI.md` and `style/GLOSSARY-VI.md` — how to write and which word to use for each concept.
   `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R19-SKILLS-REVIEW.md` — 37 sourced rules.
3. Evidence: `evidence/EVIDENCE-REGISTER.md` (272 rows), `evidence/EVIDENCE-REGISTER-ADDENDUM-1.md` (new rows N-xx and
   Stage 1a section L, when present), `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38c120/C120-RESULTS.md`.
   Section K of the register lists forbidden phrasings and their corrected versions.
4. The owner's model of style: `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`.
5. The current thesis (READ ONLY): `E:/Code/Report_INT3508/ridebound/noi-dung/*.tex`; reuse good passages, figures in
   `E:/Code/Report_INT3508/ridebound/hinh/`, and bibliography keys in `noi-dung/10-tai-lieu.tex`.

## Owner rules that override everything else

- **Every factual sentence must be backed by a register row** (code location, saved output, primary source). If a
  fact you need is not in the register, do not write it; list it under "missing evidence" in your notes file.
- **Never mention** sealed plans, preregistration, hashes of plans, "dự đoán trước", "kết quả mong đợi ghi trước khi
  chạy", "niêm phong" — not in the body, not in an appendix, not in a footnote. (This overrides STYLE-GUIDE §4.5,
  §5.2 point 5 and the glossary row about predictions.)
- Vietnamese only inside sentences. A technical term appears once with its English in parentheses at first use (per
  the glossary), then Vietnamese only. Proper names, dataset names and citation metadata stay as they are.
- No "duy nhất", "đầu tiên", "vượt trội", "đột phá", no causal verbs for the ledger split, no business/satisfaction
  claims, no "tối ưu" for a cap value. Narrow contribution, positioned against Hörl & Zwick 2022 (strategy B, eq. 7),
  Fielbaum & Alonso-Mora 2020, Schulz & Pfeiffer 2026, as in OUTLINE-V2.
- Every rate shows its count and denominator ("2.338 lượt trên 3.672 yêu cầu"); say "trung bình theo ô" or "gộp theo
  khách" whenever a percentage could be either; Vietnamese number format (3.672; 7,4 giây); differences in "điểm phần
  trăm".
- Concise and on-topic: respect the page budget of your sections (target ≈ 330 words of running text per page at
  13 pt, 1.5 spacing; a 10-row table with caption ≈ 0.6 page). Impersonal voice ("khóa luận", "đề tài", "hệ thống");
  no "chúng tôi"; "em" only in the acknowledgements.
- Code is never pasted. Pseudo-code tables in the DACN style are allowed for algorithms (Vietnamese comments).

## LaTeX conventions (template `E:/Code/Report_INT3508/ridebound/main.tex`)

- Class `report`, 13 pt; `\chapter`, `\section`, `\subsection`; `\label`/`\ref` for every cross-reference (never type
  "mục 4.2" by hand); tables with `booktabs`; figures in `hinh/` or TikZ/pgfplots inline (pgfplots must be added to
  the preamble list in your notes if you use it); environments `dinhnghia`, `menhde`, `hequa`, `dinhly`, `khungy`.
- Citations with `\cite{key}` using existing keys; a new reference goes into your notes file with full verified
  metadata (authors, title, venue, year, DOI/URL) and the register row that verifies it.
- After every paragraph that states facts, add one LaTeX comment line `% EV: <register IDs>` (invisible in the PDF)
  so checkers can trace each claim. Tables get one `% EV:` line per row group.

## Output of a writer

- `drafts/<chapter-file>.tex` (new file, compilable as an `\input` of the template), and
- `drafts/<chapter-file>-NOTES.md`: word count per section vs budget, new references with metadata, missing evidence,
  open questions, every place you deviated from OUTLINE-V2 and why.
Never write to the thesis folder; never overwrite an existing draft (use `-v2` suffixes).
