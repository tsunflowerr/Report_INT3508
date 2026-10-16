# Round 31 (Codex, parallel): write Chương 5 (Kết luận) and the appendices

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

## Inputs

**Outline.** `OUTLINE-V2.md`:
- §5 "Chương 5" (5.1 summary by the three parts, 5.2 limitations, 5.3 future directions, 3 pages in all);
- "Phụ lục" A, B, C (≤ 3 pages);
- §7.2 (Stage 1b).

**Stage 1b status.** The cost-first selector study has not been run. Section 5.3 must put the selector × cap test
first, as the outline says for that case.

**Material moved to the appendices by the chapter writers:**
- `08-chuong4-phanA-v2-NOTES.md` (the day × window table was taken out of the body; it is proposed for Phụ lục C);
- `09-chuong4-phanB-NOTES.md`;
- `07-chuong3-v3-NOTES.md` §8 item 10 (Phụ lục C should define the "15 kịch bản hiệu chỉnh" and map LOCKS/B1/C1);
- `S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md` (the test re-run and its two environment conditions belong
  in Phụ lục C);
- `codex-work/R26-CH3-OPEN-QUESTIONS-CODEX.md`, for runner identity, event clock and simulated length;
- Chương 4 part A v4 and part B v7, for the headline numbers. Use only numbers already printed there, with the same
  evidence IDs.

## Content rules

- **5.1.** One paragraph per part (dispatch part / forecast part / ledger), each with its headline count and
  denominator. Cite Hörl & Zwick again (`horl2022`). Be unfavourable-honest: C serves 96 fewer; padding ties at one
  minute.
- **5.2.** Point to `muc:c4-thaoluan`. State the overlap with prior work in the spirit of the current thesis
  `noi-dung/09-chuong5.tex:91-102`.
- **5.3.** At most 5 items, "Thứ nhất…". No hour estimates.
- **Phụ lục A** (the static set). Include it only if each number re-anchors to its output file (E12) using the
  K29/K33/K34 wording. Otherwise write a one-line placeholder in the NOTES saying it was omitted, and why.
- **Phụ lục B** (keep-route option under each rule). Follow the outline, with no prediction tallies.
- **Phụ lục C** (reproducibility). Cover:
  - the test sets and scenario lists;
  - the configurations;
  - the runner identity;
  - the output roots;
  - the run-counting rule;
  - how numbers were recomputed;
  - the test re-run.

  No plan hashes and no sealing words.

## Labels

Define `chuong:ketluan`, `phuluc:A`, `phuluc:B` and `phuluc:C`. Chapters 3 and 4 reference A and C.

## Output (subfolder `codex-work/r31-ch5/`)

- `10-chuong5.tex`;
- `11-phuluc.tex`;
- `r31-NOTES.md`: words per section, labels, evidence per number, omitted items and why, open questions.

Final message: files, words per section, and what you omitted and why.
