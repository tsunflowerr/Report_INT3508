# Round 30 (Codex, parallel): write Chương 1 (Đặt vấn đề)

First read `CODEX-PARALLEL-RULES.md` in this folder. Its rules apply.

## Inputs

- `OUTLINE-V2.md`:
  - §5 "Chương 1" (sections 1.1–1.6, page budget 7, figures H1.1 and H1.2, research questions CH1–CH3);
  - §6 (contribution paragraph, side table, five result lines, the "không nhận là mới" box);
  - §2 (rules).
- `REVIEW-DECISIONS-R20.md`.
- Chapter 3 v3 and its notes, especially `07-chuong3-v3-NOTES.md` §7 item 8 (the lecturer's correction of the
  contribution paragraph).
- Chapter 4 part A v4 and its notes.
- Chapter 4 part B v7 (to be revised; its numbers are fact-checked in `S/rewrite-2026-10/reviews/R27-FACTCHECK-CH4B-CLAUDE.md`).
- `S/tang3/t38c120/C120-RESULTS.md`.
- The register and addenda 1–4.
- The current thesis chapter 1, `noi-dung/05-chuong1.tex` (read only).

## Corrections the contribution paragraph (OUTLINE §6.1) MUST include

1. **The deadline-rule sentence.** Replace "luật C giữ được ở mọi kịch bản, theo cấu tạo" with a fair statement. The two
   rules promise different things:
   - the 30 s deadline rule counts the traffic part too, so in 28 of 34 scenarios it had to break its own rule for at
     least one rider;
   - rule C does not count the traffic part, so it never meets that case.

   Do NOT imply rule C keeps the first promise better. Under C-30, 292 of 2.338 served riders arrived more than 30 s
   after the first promise (12,5%), against 289 riders (12,4%) broken by the deadline rule (ADDENDUM-4 row C4A-01).
   Fact check #87 adds two more limits: the "never forced" property rests on assumption (N), and U is never forced
   either (0/20.760, X3-16).
2. **The 120 s cap.** "đều ở mức trần nới rộng" becomes "đều ở trần 120 giây".
3. **The padding clause.** It must stay unfavourable-honest. The padding tie appears at one minute; padding is better at
   two minutes; the cost is 37,2 vs 7,4 s of promise extension. Never present "0 forced decisions" as C's advantage
   over U.
4. **Hörl & Zwick 2022.** Use key `horl2022`. Its venue is being verified by another session (round 32); write the
   citation text without venue details.
5. **Value for the reader.** State in plain words what a ride-pooling operator or rider gains from rule C: a per-rider
   bound on how much dispatching can move the drop-off time, which holds without a correct forecast. Also state what
   it costs. No business claim.

## Figures

- **H1.1.** Two simulated riders on time axes, drawn in TikZ, with the numbers of OUTLINE §5 row 1.1. Verify those
  numbers against D06/C31.
  - You may instead use the verified hand trace of `codex-work/round26-trace-rider.txt` (one dispatch move of 14,92 s,
    then traffic jitter under 0,25 s) if it is clearer for a lay reader. Say which you chose and why.
- **H1.2.** Three parts → three places, in TikZ.

## Labels

Define `chuong:modau` and `muc:c1-cauhoi`; chapter 4 part A references the latter. Define a section label for each of
1.1–1.6.

## Output (subfolder `codex-work/r30-ch1/`)

- `05-chuong1.tex`.
- `05-chuong1-NOTES.md`, covering:
  - words per section vs budget;
  - labels;
  - every number with its evidence ID;
  - deviations from OUTLINE;
  - missing evidence;
  - open questions.

Final message: files, words per section, and the 3 points you are least sure about.
