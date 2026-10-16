# Round 42 (Codex): revise your Chương 5 and appendices after Claude's review (v2 → v3)

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

## Inputs

- **Base:** your `codex-work/r31-ch5/10-chuong5-v2.tex`, `11-phuluc-v2.tex` and `r31-NOTES.md`.
- **Claude's review:** `S/rewrite-2026-10/reviews/R32-REVIEW-CH5-APPX-CLAUDE.md`. It has three parts (reader,
  lecturer, numbers/labels), then ranked "Bắt buộc" and "Nên làm" changes, then minor notes for assembly.
- **The fairness point from the chapter 1 review** (`S/rewrite-2026-10/reviews/R31-REVIEW-CH1-CLAUDE.md` M1) applies to
  5.1 too. On the same ruler, rule C also has riders more than 30 s late against the first promise in 28 of 34
  scenarios: 292 of 2.338, against 289 for the deadline rule (C4A-01). Do not imply that C keeps first promises
  better.
- **The test re-run:** a single run gave 1.025/1.025 on 13/10/2026 (`S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md`,
  attempt 4). Phụ lục C must give this result, its two environment conditions and the earlier attempts.
- **Current chapters,** for consistency and labels:

  | Chapter | File |
  |---|---|
  | Ch1 | `codex-work/r40-ch1-v4/05-chuong1-v4-v4.tex` |
  | Ch2 | `S/rewrite-2026-10/drafts/06-chuong2-v6.tex` |
  | Ch3 | `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex` |
  | Ch4 part A | `codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex` |
  | Ch4 part B | `codex-work/r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex` |
  | Bibliography | `codex-work/r32-bib/10-tai-lieu-draft-v2.tex` |

  Assembly notes: `S/rewrite-2026-10/ASSEMBLY-NOTES.md`.

## Do

1. **Verify each review comment before applying it.** Mark each A, M, R (with the reason and an anchor) or CANNOT
   CHECK.
2. **5.3 order.** The cost-first selector × cap test stays first. The owner has approved running it after the harness
   is ready. If it runs before submission, 5.3 will change; write 5.3 for the not-run case now.
3. **Length.** Keep chapter 5 at about 3 pages and the appendices at about 3 pages or less (≈ 500 words of running
   text per page).
4. **Checks.** Re-run your number, syntax, label and reference checks against the files above.

## Output (subfolder `codex-work/r42-ch5-v3/`)

- `10-chuong5-v3.tex`
- `11-phuluc-v3.tex`
- `r42-LOG.md`: one row per comment, giving the ID, the decision, the evidence and the change; then the words per
  section.

Final message: A/M/R counts, the rejected comments with reasons, and the words per section.
