# Round 36 (Codex): apply your R34 corrections to Chương 4 part A (v4 → v5)

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

## Inputs

- **Base:** `S/rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex` and its notes `08-chuong4-phanA-v2-NOTES.md`.
- **Your review:** `codex-work/r34-ch4a-verify/R34-CH4A-V4-VERIFY-CODEX-v2.md`. Verdict ACCEPT WITH CORRECTIONS; it
  gives exact Vietnamese replacements. Top five:
  1. full no-op conditions;
  2. missing counts and denominators;
  3. a narrower calibration-data exclusion;
  4. part B's 120 s disclosure;
  5. three missing reference targets.
- **Consistency:**
  - chapter 3 is now `codex-work/r33-ch3v4/07-chuong3-v4-v3.tex` (your R33 output);
  - chapter 2 is `S/rewrite-2026-10/drafts/06-chuong2-v4.tex`;
  - part B is being finished by Claude in `S/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex`, which may still change.
  Labels must resolve against these.

## Do

1. Make a TARGETED revision: apply each correction of your R34 v2 review and keep every unaffected sentence.
2. If a correction belongs to part B, not part A, do NOT edit part B. List it in your notes for the part-B reviser.
3. For each missing reference target, define it if it belongs in part A. Otherwise record which chapter must define
   it.
4. Re-run your own read-only checks on every changed number, and check the syntax. Keep the page budget of 4.1–4.5
   at about 13.5 pages; the word counts should not grow by more than 3%.

## Addendum (2026-10-13 14:00): items from the part-B reviser

Part B is final at `S/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex`; its notes are in
`09-chuong4-phanB-v8-NOTES.md` (which describes v10) §8. Apply these to part A as well, after verifying each:

1. **Snow runner is now verified.** Part A v4 still says "chưa kiểm lại" in the scenario-set table and on lines 142
   and 435. The 8 snow runs used the same archived runner and no-worse recovery as the main set; the DLL hash
   matches. Evidence: your R26 Q8; `S/rewrite-2026-10/evidence/EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md` N4B8-05;
   `evidence/checks-ch4b-v8/ch4b-v8-check-2026-10-12.txt` lines 65-72. Confirm all of it, then remove the caveat.
2. **Line 66:** drop "Thế giới". Part B uses no such term.
3. **Line 231:** "phép sàng lọc" clashes with part B's use of that name (the fixed-state selector screen in 4.6). Rename
   part A's use.
4. **The test re-run sentence,** if part A has one: all 1.025 tests pass in a single run on 13/10/2026 (see
   `S/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md`, attempt 4).
5. **Every reference target** must resolve against part B v10's labels.
6. **Fix the overfull boxes.** A trial build of part A v4 (`C:/RideBoundData/research/thesis-trial-build-2026-10-13/main.log`)
   reports three:
   - v4 lines 713–730: 60,8 pt, a table;
   - lines 262–276: 34,0 pt;
   - lines 119–139: 1,5 pt.

   Shrink the tables without changing content: `\small`, column widths, or a shorter header. The build also showed
   chapter 4 at 21 pages against a budget of 26,5, so there is no need to cut text.

## Output (subfolder `codex-work/r36-ch4a-v5/`)

- `08-chuong4-phanA-v5.tex`
- `08-chuong4-phanA-v5-CHANGES.md`: one row per change, with the v4 line, old text, new text and evidence. Also list
  the items for part B and other chapters.

Final message: the number of changes, the word counts per section, and the items left for other chapters.
