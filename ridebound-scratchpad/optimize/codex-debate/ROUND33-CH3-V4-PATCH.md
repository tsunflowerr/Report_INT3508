# Round 33 (Codex, parallel): bring Chương 3 from v3 to v4 with the newly verified facts

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

## Base

Base text: `S/rewrite-2026-10/drafts/07-chuong3-v3.tex` and its notes `07-chuong3-v3-NOTES.md`. Those notes list the
open questions (§8) and the missing evidence (§9).

Make a TARGETED revision, not a rewrite: keep every sentence that is not affected.

## Apply

1. **Your round 26 answers** (`codex-work/R26-CH3-OPEN-QUESTIONS-CODEX.md`):
   - Q1: the event-clock sentence, i.e. what triggers a decision round. Use one real count only if it helps the reader,
     e.g. 613 rounds at 258 distinct times in one scenario.
   - Q2: the simulated length of a run.
   - Q6: what the run times measure. They are whole-run wall time, not the cost of one decision.
   - Q8 and Q9, only where chapter 3 mentions them.
   - Q4, Q5 and Q7 were CANNOT ANSWER, so keep the text silent on them.
2. **A worked real example**, if it fits the ledger section (3.6) or the three-time section (3.2) within budget. Use the
   hand trace of one real rider from `codex-work/round26-trace-rider.txt`: one dispatch move of 14,92 s, remaining
   allowance 105,08 of 120 s, then 14 traffic-only revisions under 0,25 s. A lay reader gains a lot from a short real
   example. Decide where it fits best.
3. **The test re-run** (`S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md`). Ch3 lines 705-706 still say the
   1.025 tests were not re-run.
   - Replace that with the allowed wording in the TESTRUN file: all 1.025 pass on the runner's source.
   - Mention the two environment conditions in one clause at most. Details go to Phụ lục C.
4. **Terms of the corrected glossary** `style/GLOSSARY-VI-v2.md`.
   - Rows 92–93 define "quyết định bị ép" per the code: the keep-route option was rejected and at least one rider was
     exempted. Other options need not all be rejected.
   - Check every use in chapter 3 against this definition.
5. **Consistency with chapter 4 part A v4** (`08-chuong4-phanA-v4.tex`): the same terms for the same things. Note
   any number printed in both chapters, and make it agree with the source.
6. **Hörl & Zwick.** Keep the key `horl2022`. Do not add venue details; round 32 resolves the venue.

## Output (subfolder `codex-work/r33-ch3v4/`)

- `07-chuong3-v4.tex`.
- `07-chuong3-v4-CHANGES.md`: one row per change, giving the line in v3, the old text, the new text and the evidence.
  Also give the words per section vs the 13-page budget.

Final message: the number of changes, the words per section, and anything you could not verify.
