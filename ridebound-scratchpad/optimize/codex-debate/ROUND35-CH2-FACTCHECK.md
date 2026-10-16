# Round 35 (Codex): fact-check Chương 2 (background and related work)

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply. You may use web search.

## Inputs

- **Draft:** `S/rewrite-2026-10/drafts/06-chuong2-v4.tex`. Ignore v1–v3.
- **Writer's notes:** `drafts/06-chuong2-NOTES.md` and `drafts/06-chuong2-BIB.md`. Both name v3, but v4 has the same
  citations and the same 33 `% EV` lines.
- **Writer's new evidence:** `evidence/EVIDENCE-REGISTER-ADDENDUM-5-CH2.md` (C2-01…24).
- **Register:** section J (literature) and section K (forbidden phrasings) of `evidence/EVIDENCE-REGISTER.md`.

**Sources:**
- local PDFs in `C:/PDF/Paper/` and `S/optimize/codex-debate/claude-work/pdf/`. The Hörl–Zwick paper is
  `hoerl-zwick-2022.pdf`; `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf` is Sharif Azadeh et al. 2022, not Hörl &
  Zwick;
- publisher, DOI and arXiv pages on the web.

## Do

1. **Check every sentence about a paper against the paper itself:**
   - what it did;
   - which data it used;
   - what it measured;
   - which equation or section it is;
   - any number.

   Give each one a verdict: AGREE / WRONG (correct statement + page) / OVERSTATED / CANNOT CHECK. Pay special
   attention to:
   - the Bảng 2.2 judgements, in the columns "Phần do tắc đường có bị tính?" and "Cộng qua cả chuyến?". The writer
     says the Schulz–Pfeiffer and Hörl–Zwick rows are the shakiest. Check them against the equations and definitions
     in each paper.
   - Bảng 2.1. Its test values must match the code or register (B03):
     - pickup window 600 s;
     - ride time ≤ 1,5 × direct;
     - 4 seats.
   - The 2.4 sentence flagged by the writer as their own inference (TLC publishes about two months late). Is it
     supported? If not, give a safe replacement or say it should be cut.
   - The claim boundary. No novelty claim on dynamic insertion, ETA limits, reassignment, route similarity,
     least-commitment, time consistency or user satisfaction (`E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`).
2. **Check every cited key's metadata.** Do this independently of the writer's BIB file.
3. **Check the positioning.** Does chapter 2 position rule C fairly and narrowly against Hörl & Zwick 2022, Schulz &
   Pfeiffer 2026, Fielbaum & Alonso-Mora 2020, Elmi et al. 2026 and Mt-KaRRi, with terms consistent with chapter 3
   v3?

## Output (subfolder `codex-work/r35-ch2-check/`)

`R35-CH2-FACTCHECK-CODEX.md`, containing:
- one row per item;
- a verdict: ACCEPT / ACCEPT WITH CORRECTIONS / REJECT;
- a ranked list of corrections with exact Vietnamese replacements.

Final message: the counts per verdict and the top 5 corrections.
