# Round 32 (Codex, parallel): verify every reference and draft the new bibliography

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply. You may use web search and fetch.

## Scope

1. **Collect the citation keys.** Gather every `\cite{...}` key used in the current drafts:
   - `S/rewrite-2026-10/drafts/07-chuong3-v3.tex`;
   - `08-chuong4-phanA-v4.tex`;
   - `09-chuong4-phanB-v7.tex`;
   - any `06-chuong2*.tex` that exists when you start (Ch2 is being written now; re-scan it at the end).

   Gather also every key planned in `OUTLINE-V2.md` §5 "Tài liệu tham khảo" and §5 rows for Ch1–Ch2 (register rows
   J01–J42 and their keys), and every `\bibitem` in the current `E:/Code/Report_INT3508/ridebound/noi-dung/10-tai-lieu.tex`
   (27 items).
2. **Verify each reference** on its DOI page, the publisher's page, arXiv or the official working-paper page. Check
   authors in order, exact title, venue, year, volume, issue, pages or article number, DOI or URL. Mark each row one of:
   - VERIFIED (with the URL you opened);
   - CORRECTED (old → new);
   - CANNOT VERIFY.

   Never invent a DOI or page.
3. **Resolve Hörl & Zwick 2022 carefully.** Round 26 found a TRB 2022 working paper from the ETH IVT site (eq. 7,
   manuscript pp. 1–16). But the local PDF `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf` is an Elsevier
   journal-style file.
   - Open it and say which paper it is.
   - Say whether a journal version of Hörl & Zwick exists.
   - Say which version the thesis should cite, given that the thesis quotes strategy B, eq. 7, and constraints 9–10.
     Check that those numbers match the version you recommend.
4. **Also verify:**
   - `engelhardt2026` (FleetPy, ETRR 2026);
   - `schulz2026`;
   - `fielbaum2020`;
   - `alonsomora2017`;
   - `ortools`;
   - Elmi et al. 2026 (J12; register says UNVERIFIED);
   - "anticipatory walking" 2026 (J16, UNVERIFIED);
   - Ding, Dandl & Bogenberger (J41, UNVERIFIED; open it or mark it CANNOT VERIFY);
   - Mt-KaRRi (J32);
   - Wardman et al. 2026 (J23);
   - Alonso-González et al. 2020 (J24);
   - Lu & Kühnel 2024 (J22);
   - Leonardi et al. 2024 (J21);
   - the UberX Share page (J28; record the access date).
5. **Fix the bibliography heading.** The current `10-tai-lieu.tex` prints a near-empty "Tài liệu tham khảo" page and
   then "Bibliography". Propose the LaTeX fix: rename `\bibname`, drop the extra `\chapter*`.
   - Check whether the UET template wants the references split into Vietnamese and English groups. Look at the
     current `main.tex` and the owner's DACN PDF; report what you find.
6. **Draft the new bibliography.** List only the keys the drafts cite or the outline plans. List the existing keys
   nothing cites any more separately, as candidates to drop.

## Addendum (2026-10-12 23:40, from Claude)

1. **Wrong file.** The Claude chapter-2 writer found that `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf` is Sharif
   Azadeh et al. 2022, not Hörl & Zwick. The Hörl–Zwick PDF it used is
   `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf` (plus a
   `.txt`). Confirm both claims yourself.
2. **Chapter 2 is written.** It is `S/rewrite-2026-10/drafts/06-chuong2-v4.tex` and cites 15 keys. The writer's
   metadata is in `drafts/06-chuong2-BIB.md`, and its verification rows are in
   `evidence/EVIDENCE-REGISTER-ADDENDUM-5-CH2.md` (C2-01…24).
   - Cross-check every key there independently.
   - The writer says the existing `alonsogonzalez2020` entry lists "S. van Cranenburgh" and leaves out
     "S. Hoogendoorn-Lanser"; verify that.
   - The writer replaced a dead DeepETA blog link with `hu2022` (DeeprETA, arXiv); verify that too.
   - Include all chapter-2 keys in the bibliography draft.

## Output (subfolder `codex-work/r32-bib/`)

- `BIB-VERIFICATION.md`: one row per key, with key, status, final metadata, URL opened and notes.
- `10-tai-lieu-draft.tex`: the new `thebibliography` in the current format, with the heading fix.
- `HORL-ZWICK-RESOLUTION.md`.

Final message: counts per status, every CORRECTED or CANNOT VERIFY item, and the Hörl–Zwick decision.
