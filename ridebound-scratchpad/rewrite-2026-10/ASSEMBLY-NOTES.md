# Assembly notes: fixes to apply when the chapters are merged into the thesis

Each row: where, what to change, why, evidence. Added as findings arrive. The thesis folder
(`E:/Code/Report_INT3508/ridebound/`) is edited only at assembly, from the backup
`ridebound-scratchpad/tex-backup-2026-10-10-before-rewrite`.

| # | Where | Change | Why / evidence |
|---|---|---|---|
| 1 | Ch3 v4 (`codex-work/r33-ch3v4/07-chuong3-v4-v3.tex`), item "Kiểm thử phần mềm" | Change "ngày 12/10/2026" to "ngày 13/10/2026". | The single full run with both conditions (1.025/1.025) was on 13/10. On 12/10 the result was 1.024 plus 1/1 run separately. Evidence: `evidence/TESTRUN-45f8026-2026-10-12.md` attempt 4. |
| 2 | Ch4B (final v10, to be confirmed), §4.10 test sentence | Use the same wording and date as row 1, with the details in Phụ lục C. | Consistency with Ch3; TESTRUN attempt 4. |
| 3 | Phụ lục C | Give the test re-run details: commit 45f8026, `core.eol=lf`, one untracked file (the test that requires a dirty tree), 1.025/1.025 on 13/10/2026; earlier attempts in TESTRUN. | TESTRUN. |
| 4 | Bibliography | Use the Hörl–Zwick decision of Codex R32 (`codex-work/r32-bib/HORL-ZWICK-RESOLUTION.md`, pending). `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf` is Sharif Azadeh et al. 2022, not Hörl–Zwick. | Ch2 writer report; R32 addendum. |
| 5 | All chapters | The forced-decision term is "quyết định bị ép", defined per glossary v2 (keep-route rejected and ≥ 1 rider exempted). | `style/GLOSSARY-VI-v2.md`; code anchors in Ch4A fact check #50. |
| 6 | Ch3 v4: the v3 line 457 equivalent | "vế cộng dồn" → "phần cộng dồn". | Ch4B reviser NOTES §7 (`drafts/09-chuong4-phanB-v8-NOTES.md`). |
| 7 | Ch3 v4: the v3 line 689 equivalent | Narrow "các bộ đếm" to "các bộ đếm của bộ sinh phương án". | Same; Codex R29 point 4 (only the generator counters were audited). |
| 8 | Ch4B v10 is final | Assemble `drafts/09-chuong4-phanB-v10.tex`, pending the Codex R37 verdict. v8 and v9 are superseded; v8 has five off-by-one `FR:` anchors. | `reviews/CH4B-REVISION-LOG.md`. |
| 9 | Ch5 §5.3 | The first future direction is the cost-first selector × cap test (Stage 1b), unless Stage 1b runs before submission. | Ch4B §4.6 says so; OUTLINE §7.2. |
| 10 | Bibliography | Add `engelhardt2026` and `horl2022`. Correct `alonsogonzalez2020`: add S. Hoogendoorn-Lanser and check S. van Cranenburgh. | Ch2 BIB; R32 (pending). |
| 11 | Page budget | Ch4B v10 ≈ 13,1 pages by the 330-word ruler (budget 11), ≈ 9,5 at part A's measured density. Decide the cuts only after a real build (Ch4B NOTES §4 lists ≈ 600 words). | Ch4B reviser report. |

## Current files to assemble (updated 2026-10-13 19:40)

| Part | File | Status |
|---|---|---|
| Ch1 | `codex-work/r30-ch1/05-chuong1-v3.tex` (Codex) | Claude review R31 running |
| Ch2 | **`drafts/06-chuong2-v6.tex`** (v5 superseded; notes `06-chuong2-v5-NOTES.md` describe v6; log `reviews/CH2-REVISION-LOG.md`) | Final. Equation split and Bảng 2.1 width fixed; ≈ 7,3 pp. Coordinator defaults for its 6 open questions: keep the cited papers' rates with their source and averaging; journal versions per R32; drop the duplicated window and ride rows from Bảng 2.2; keep "độ chùng" but name Schulz–Pfeiffer's "maximum time shift" once; keep "theo phần tóm tắt" for Yu et al.; do not restore Kovacs/Sridharan. Evidence row C2-15 is wrong: the DeeprETA PDF has 9 pages, not 3. |
| Ch3 | `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex` | Apply rows 1, 6 and 7 above at assembly |
| Ch4 part A | `codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex` (25 changes from R34) | Final unless new comments arrive |
| Ch4 part B | `drafts/09-chuong4-phanB-v10.tex` → v11 by Codex R39 (running) | R37 ACCEPT WITH CORRECTIONS |
| Ch5 + appendices | `codex-work/r31-ch5/10-chuong5-v2.tex`, `11-phuluc-v2.tex` (Codex) | Claude review pending |
| Bibliography | `codex-work/r32-bib/10-tai-lieu-draft-v2.tex` | 53 records: 45 verified / 7 corrected / 1 cannot verify; 23 entries |

### Front matter

Claude wrote these new files: `drafts/01-loi-cam-on.tex`, `drafts/02-tom-tat.tex` (Tóm tắt 295 tiếng + Abstract) and
`drafts/04-viet-tat.tex`. Notes are in `drafts/FRONT-NOTES.md`.

- **Fairness.** The Tóm tắt states that C is no better than the deadline rule on arrival (292 vs 289), the padding
  tie at one minute, and the per-rider bound.
- **Left out for space.** +31/−5, the C-120 point and the cumulative number. FRONT-NOTES §3 has swap-in sentences for
  each.

### Owner decisions on the front matter (2026-10-14 01:00)

- **Supervisor.** ThS. Trần Mạnh Cường ("thầy"). Fill in the Vietnamese and English covers and the Lời cảm ơn.
- **Lời cam đoan and bìa lót.** Both are needed, following the DACN report's format
  (`C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`). The Lời cam đoan is a template the student
  signs.
- **No AI-use disclosure.**
  - Remove or rephrase every mention of software agents, Claude, Codex or Antigravity in the chapters and appendices:
    "kiểm lại bằng chương trình đọc riêng", "tính lại độc lập bằng một chương trình khác".
  - Check Ch3 §3.7, Ch4B §4.10 and Phụ lục C especially (OUTLINE 3.7 asked to name the agents; that is now overridden).

### Antigravity R27 triage (`reviews/R33-ANTIGRAVITY-TRIAGE-CLAUDE.md`)

24 already fixed / 8 still applies and correct (7 distinct edits) / 12 wrong / 2 cannot check. The 7 edits to apply,
with the exact replacements given in the triage file:

| # | Where | Edit |
|---|---|---|
| 1 | Ch2 v6, lines 138–142 | Split the Fielbaum–Alonso-Mora paragraph. |
| 2 | Ch2 v6, lines 211–214 | Split the positioning sentence. |
| 3 | Ch3 v4-v3, lines 237–239 | Split. |
| 4 | Ch3 v4-v3, lines 298–300 | Split; drop the long parenthesis. |
| 5 | Ch4B v11-v2, lines 226–227 | Split the opening sentence of 4.8. |
| 6 | Ch3 v4-v3, lines 145–146 | Bảng 3.2, criterion 3 wording. |
| 7 | Ch3 v4-v3, lines 517–518 | The "1/g giây" wording. |

Edits 1 and 2 bring Ch2 to its +5% word cap, so recount at assembly.

### Cross-chapter consistency pass (do last, on the final files)

Findings from the front-matter writer, in FRONT-NOTES §8:

| # | Where | Problem |
|---|---|---|
| 1 | Ch3 | v, e, p, D, S, x, c, z and L_r are used in the decision-loop figure and the pseudo-code (≈ lines 175, 182–186, 222) before they are defined (≈ 244–256 and the forecast section). |
| 2 | Ch3:194 | `$a \gets b$` clashes with a, the actual drop-off time. |
| 3 | Ch2 / Ch3 / Ch4B | k means a request (Ch2), a vehicle (Ch3) and a cost per late ride (Ch4B); m and T also clash. |
| 4 | Ch4B v11:364 | NOAA is not spelled out. |
| 5 | Appendix | Internal names LOCKS, B1 and C1 are used. |

**Hörl–Zwick (R32).** Cite the ETH/TRB 2022 version. Equation 7 and constraints 9–10 match manuscript p. 8. No journal
version was verified. See `codex-work/r32-bib/HORL-ZWICK-RESOLUTION-v2.md`.

`main.tex` needs `\input{noi-dung/11-phuluc}`, inside `\appendix`, after the bibliography.

## Trial build 2026-10-13 13:45 (copy at `C:/RideBoundData/research/thesis-trial-build-2026-10-13/`; thesis folder untouched)

**Inputs.** Ch2 = `06-chuong2-v4`; Ch3 = Codex R33 `07-chuong3-v4-v3`; Ch4 = `08-chuong4-phanA-v4` + `09-chuong4-phanB-v10`
(concatenated). Ch1, Ch5 and the bibliography are still the OLD files.

**Build.** tectonic exit 0; `main.xdv` 79 pages; log in `build-2026-10-13.out` and `main.log`.

**Pages, from `main.toc`:**

| Part | Pages | Budget |
|---|---|---|
| Ch1 (old) | pp. 1–9 | — |
| Ch2 | pp. 10–16, **7 pages** | 6,5 |
| Ch3 | pp. 17–31, **15 pages** | 13 |
| Ch4 | pp. 32–52, **21 pages** | 26,5 |
| Ch5 (old) | pp. 53–59 | — |
| References | from p. 60 | — |

**Conclusion.**
- Ch4 is 5,5 pages UNDER budget, so no cuts are needed in Ch4B. The 330-word ruler overestimates pages; the real
  density is about 500 words per page.
- Ch3 is 2 pages over, which the Ch4 surplus absorbs.
- Projected total with a new Ch1 (≈ 7), a new Ch5 (≈ 3) and appendices (≈ 3): about 76 pages, inside the owner's
  "7x" range.

**Overfull boxes to fix at assembly:**

| File | Lines | Overflow |
|---|---|---|
| Ch2 v4 | equation at line 48 (`eq:c2-chon`) | 80,5 pt |
| Ch2 v4 | 76–94 | 1,9 pt |
| Ch3 v4 | 432 | 0,8 pt |
| Ch4A v4 | 119–139 | 1,5 pt |
| Ch4A v4 | 262–276 | 34,0 pt |
| Ch4A v4 | 713–730 | 60,8 pt |
| Ch4B v10 | 39–59 | 29,2 pt |
| Ch4B v10 | 170–174 | 15,8 pt |

The 80 pt and 61 pt overflows are visible; split the equation, or shrink the table with `\small` / `tabularx`.

**Undefined references (expected until Ch1, Ch5 and the appendices exist):** `phuluc:A`, `phuluc:C`,
`muc:c1-cauhoi`. The other undefined references come from the old Ch1 and Ch5.
