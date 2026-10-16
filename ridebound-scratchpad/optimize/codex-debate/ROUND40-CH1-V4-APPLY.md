# Round 40 (Codex): revise your Chương 1 after Claude's review (v3 → v4)

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

## Inputs

- **Base:** your `codex-work/r30-ch1/05-chuong1-v3.tex` and `05-chuong1-NOTES.md`.
- **Claude's review:** `S/rewrite-2026-10/reviews/R31-REVIEW-CH1-CLAUDE.md`. It found:
  - 54 hard-to-read places;
  - no wrong number across 49 number lines;
  - ranked changes M1–M5 and S6–S10, with full Vietnamese replacement text.

  Its most important point (M1): "28 trong 34 kịch bản" for the deadline rule is not a fair contrast. Measured with the
  same ruler, rule C also has riders more than 30 s late against the first promise in 28 of 34 scenarios (C4A-01;
  part A v5-v3:357–358). The text must say the two rules promise different things and must not imply C is better at
  keeping first promises.
- **Consistency targets:**
  - Ch2: `S/rewrite-2026-10/drafts/06-chuong2-v4.tex`. Claude is revising it to v5; labels `muc:c2-*` stay.
  - Ch3: `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex`.
  - Ch4: part A `codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex`; part B `S/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex`
    (your R39 is producing v11).
  - Bibliography: `codex-work/r32-bib/10-tai-lieu-draft-v2.tex`. It contains `uberxshare` and `moiaexpress` if you add
    them.

## Do

1. **Verify each review comment before applying it** (owner rule: reviewers can be wrong). Decide each as A, M, R
   (with the reason and an anchor) or CANNOT CHECK.
2. **Page budget.** The reviewer estimates that the changes add about 800 words, while the budget is 7 pages (the real
   build measures about 500 words of running text per page). Compensate as the reviewer suggests: drop the five-line
   result list whose numbers are now in the text, and the section pointers inside the three research questions.
   Target at most 7,5 pages. If the text cannot fit, say what you would cut next. Do not exceed the budget silently.
3. **Keep the owner rules.**
   - No mention of sealed plans or predictions.
   - No "duy nhất", "đầu tiên" or "tối ưu".
   - No business claim.
   - Vietnamese only inside sentences.
   - Every number carries a `% EV:` anchor.
4. Re-run your number and syntax checks, and check every `\ref` against the files above.

## Output (subfolder `codex-work/r40-ch1-v4/`)

- `05-chuong1-v4.tex`
- `05-chuong1-v4-LOG.md`: one row per review comment (ID, decision, evidence, change), plus the words per section.

Final message: A/M/R counts, the rejected comments with reasons, and the words per section.
