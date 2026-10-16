# Brief: write Chương 2 (Cơ sở lý thuyết và các công trình liên quan), 2026-10-12

Paths are under `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/` unless absolute.

## Read first

1. `WRITING-BRIEF.md`: the owner rules, which override everything else.
2. `OUTLINE-V2.md`, specifically:
   - §2 (rules);
   - §5 Chương 2 rows 2.1–2.5 (content, page budget 6,5 pages, Bảng 2.1 and Bảng 2.2, evidence IDs);
   - §6.4 (what the thesis does not claim as new);
   - §5 "Tài liệu tham khảo" (which references to add, which are unverified, and which to drop).
3. `REVIEW-DECISIONS-R20.md`.
4. Style:
   - `style/STYLE-GUIDE-VI.md`;
   - `style/GLOSSARY-VI-v2.md` (the corrected glossary; use it, not v1);
   - the owner's style model `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`.
5. Evidence:
   - `evidence/EVIDENCE-REGISTER.md`, section J (literature, J01–J42) and section K (forbidden phrasings);
   - `EVIDENCE-REGISTER-ADDENDUM-1.md` (§0 corrections);
   - `EVIDENCE-REGISTER-ADDENDUM-2-CH3.md`.
6. Chương 3 v3, `drafts/07-chuong3-v3.tex`, and its notes `drafts/07-chuong3-v3-NOTES.md`. Chapter 2 must use the same
   terms and must not repeat chapter 3's formal definitions. The notes carry the verified metadata for `horl2022` and
   `engelhardt2026`.
7. The claim boundary `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (READ ONLY). Never claim as novel:
   dynamic insertion, ETA limits, reassignment, route similarity, least-commitment, time consistency, user
   satisfaction.
8. The current thesis chapter 2 `E:/Code/Report_INT3508/ridebound/noi-dung/06-chuong2.tex` and the bibliography
   `noi-dung/10-tai-lieu.tex` (READ ONLY). Reuse good passages and existing citation keys.

## Sources must be opened, not assumed

- Local PDFs are in `C:/PDF/Paper/`, including:
  - Hörl & Zwick 2022: `1-s2.0-S0191261522000716-main.pdf`;
  - Fielbaum & Alonso-Mora: `Unreliability_in_ridesharing_systems_Measuring_cha.pdf`;
  - the value-of-reliability paper;
  - Kovacs 2014;
  - two OR Spectrum papers `s00291-*.pdf`;
  - arXiv `2508.04811v1.pdf`;
  - others.

  Read the pages you cite.
- A register row marked UNVERIFIED (e.g. J12 Elmi 2026, J13, J15, J16, J36, J41) may be cited for a detail only after
  you open the original, from the local PDF or the DOI/publisher page via web fetch. Then record what you verified.
  Otherwise cite it only for what is verified, or leave it out.
- Every reference you cite needs full verified metadata: authors, title, venue, year, volume/pages, DOI or URL. Check
  it on the DOI or publisher page. Never invent a DOI or a page number.

## What to write

- The five sections 2.1–2.5 with the tables of the outline:
  - Bảng 2.1: service constraints with the values used in the tests, captioned as the test configuration, not an
    industry standard;
  - Bảng 2.2: obligation forms by approach, words only.
- Separate clearly what is theory or prior work from what RideBound uses.
- Write natural Vietnamese for a reader outside the field, with no English inside sentences. A technical term appears
  once with its English in parentheses, per the glossary.
- Keep it concise and on-topic: about 6,5 pages, at about 330 words of running text per page; a 10-row table with
  caption is about 0,6 page.
- No "duy nhất", "đầu tiên", "vượt trội". Position the thesis narrowly against:
  - Hörl & Zwick 2022 (strategy B, eq. 7, constraints 9–10);
  - Fielbaum & Alonso-Mora 2020;
  - Schulz & Pfeiffer 2026;
  - Elmi et al. 2026 (only after opening it);
  - Mt-KaRRi.
- Every factual paragraph is followed by a `% EV:` line with register IDs, or with your new verification rows.
- Labels to define: `chuong:coso`, plus the section labels `muc:c2-baitoan`, `muc:c2-dolech`, `muc:c2-rangbuoc`,
  `muc:c2-dubao` and `muc:c2-giatri`. Chapters 3 and 4 may reference the first four.
- Use `\cite{key}`. Reuse existing keys where they exist; list new keys with full metadata.

## Output (new files only; exclusive create; never overwrite, even your own files: use -v2, -v3)

- `drafts/06-chuong2.tex`: compilable as an `\input` of the template `E:/Code/Report_INT3508/ridebound/main.tex`.
- `drafts/06-chuong2-NOTES.md`, containing:
  - word count per section vs budget;
  - labels defined;
  - deviations from the outline and why;
  - missing evidence;
  - open questions.
- `drafts/06-chuong2-BIB.md`, one row per cited key:
  - key, full metadata, where verified (file:page or URL), and whether it is new or existing;
  - also the existing keys of `10-tai-lieu.tex` that nothing cites any more.
- `evidence/EVIDENCE-REGISTER-ADDENDUM-5-CH2.md`: new verification rows for anything you opened (ID, claim, source
  page, how verified).

Never write to the thesis folder, `E:/Code/RideBound*`, `C:/Code/*`, or other drafts. Run no builds or installs.
Drive E: is nearly full, so write only these text files.

## Final message

- files written;
- word count per section;
- the references you verified and how;
- the references you dropped or could not verify;
- the 3 points you are least sure about.
