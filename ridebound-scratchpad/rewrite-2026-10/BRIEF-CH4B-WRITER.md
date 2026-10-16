# Brief: write Chương 4 part B (sections 4.6–4.11), 2026-10-12

Paths are under `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/` unless absolute.

## Read first (in this order)

1. `WRITING-BRIEF.md`: the owner rules. They override everything else. In particular, never mention sealed plans,
   preregistration, "dự đoán trước", "niêm phong" or "kết quả mong đợi".
2. `OUTLINE-V2.md`: §2 (rules), §5 Chương 4 rows 4.6–4.11 (content, page budgets, tables, evidence IDs), §7.2
   (Stage 1b slot) and §8 (figures and tables).
3. `REVIEW-DECISIONS-R20.md`, especially the honest answer to "why rule C if padding ties" (RD §8).
4. `style/STYLE-GUIDE-VI.md`, `style/GLOSSARY-VI.md`, and the owner's style model
   `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`.
5. Evidence: `evidence/EVIDENCE-REGISTER.md`; `EVIDENCE-REGISTER-ADDENDUM-1.md` (read its §0 corrections first);
   `EVIDENCE-REGISTER-ADDENDUM-2-CH3.md`; `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38c120/C120-RESULTS.md`.
6. Part A and its handoff: `drafts/08-chuong4-phanA.tex` and `drafts/08-chuong4-phanA-NOTES.md` (§7–§10: the labels
   part B must define, the numbers already printed in part A that part B only points to, and what part A has not said).
7. Chương 3 v3: `drafts/07-chuong3-v3.tex` (the terms and symbols the reader already knows; do not redefine them).
8. Codex's review of part A: `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/R25-CH4A-REVIEW-CODEX.md`.
   Read §5 (wording corrections that also apply to part B), §6 (honest padding answer and part-B handoff) and §7.

## What to write

- **4.6 Vai trò của trần và thứ tự ưu tiên chọn phương án.** Write the fallback version (OUTLINE §7.2): the cost-first
  study has not been run. Include the fixed-state screen (Bảng 4.11) with its two different state populations and the
  three cost estimands named correctly. Never write "chính trần, không phải bộ chọn, giữ lời hứa" (REG K18).
- **4.7 Lời hứa theo dự báo**, 4.8 **So với cách đệm lời hứa**, 4.9 **Chiều tuyết 15/11/2018**, 4.10 **Kiểm tra tính
  hợp lệ**, 4.11 **Thảo luận và hạn chế**, exactly as the OUTLINE rows say. In the machine-learning paragraph, state
  the four conditions for "better" without saying when they were set.
- Define the labels part A and Chương 3 reference: `muc:c4-vaitro`, `muc:c4-dubao`, `muc:c4-dem`, `muc:c4-tuyet`,
  `muc:c4-hople`, `muc:c4-thaoluan`. Use labels for every cross-reference.
- Page budget: 4.6 ≈ 1.2 (fallback plus screen), 4.7 3, 4.8 2.75, 4.9 1, 4.10 1.25, 4.11 2, so about 11 pages in
  total (≈ 330 words of running text per page; a 10-row table with caption ≈ 0.6 page).
- Write for a reader outside the field: say what each table compares, on which runs, and what to conclude, before
  the numbers. Every rate shows its count and denominator and says "gộp theo khách" or "trung bình theo kịch bản".
  Never describe a padding arm as a matched control: it is a replay on U's journeys.

## Evidence rule

Every factual sentence carries a `% EV:` line with register IDs. If a number you need is not in the register, open
its saved output read-only and check it. Then add a row to a NEW file `evidence/EVIDENCE-REGISTER-ADDENDUM-3-CH4B.md`
(ID, claim, value, source path:line, how verified). If you cannot verify it, do not write it and list it under
"missing evidence" in the notes. Do not paste code.

## Output (new files only; exclusive create; never overwrite anything)

- `drafts/09-chuong4-phanB.tex`: must compile as an `\input` right after part A;
- `drafts/09-chuong4-phanB-NOTES.md`: word count per section vs budget, labels defined, figures/tables and their data
  sources, new evidence rows, missing evidence, deviations from OUTLINE-V2 and why, open questions;
- `evidence/EVIDENCE-REGISTER-ADDENDUM-3-CH4B.md`: only if you added rows.

Never write to the thesis folder `E:/Code/Report_INT3508/ridebound/`, to `E:/Code/RideBound*`, or to other drafts.
Run no simulations or builds. Note that drive E: has little free space (≈ 41 GB, floor 40 GB): write only these text
files.
