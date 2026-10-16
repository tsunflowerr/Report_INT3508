# Rules for every parallel Codex session (rounds 30–34, 2026-10-13)

You are one of several Codex sessions working in parallel on the rewrite of a Vietnamese undergraduate thesis (UET/VNU)
about RideBound.

- **Luật C.** Rule C caps, per accepted rider, the total change dispatching may make to the promised drop-off time over
  the whole trip.
- **Forecast promise.** The thesis also uses a promise based on a historical forecast.
- **Ledger.** Each rider has a three-part ledger:
  - traffic x = e − v;
  - dispatch c = p − e;
  - total z = p − v.

Other sessions handle other chapters; Claude agents review your output afterwards.

## Paths

- Scratchpad: `E:/Code/Report_INT3508/ridebound-scratchpad/` (S/).
- Rewrite kit: `S/rewrite-2026-10/`. It contains:
  - `WRITING-BRIEF.md`, the owner rules, which override everything;
  - `OUTLINE-V2.md`;
  - `REVIEW-DECISIONS-R20.md`;
  - `style/STYLE-GUIDE-VI.md`;
  - `style/GLOSSARY-VI-v2.md`, the corrected glossary (use it, not v1);
  - the evidence register `evidence/EVIDENCE-REGISTER.md` plus addenda 1–4. Read ADDENDUM-1 §0 first.
- Current drafts, all in `S/rewrite-2026-10/drafts/`:

  | Chapter | Draft | Notes |
  |---|---|---|
  | Ch3 | `07-chuong3-v3.tex` | `07-chuong3-v3-NOTES.md` |
  | Ch4 part A, final | `08-chuong4-phanA-v4.tex` | `08-chuong4-phanA-v2-NOTES.md` (it describes v4) |
  | Ch4 part B | `09-chuong4-phanB-v7.tex` | being revised by Claude into `-v8` |

- Ch2 is being written by Claude into `drafts/06-chuong2*.tex`. It may not exist yet.
- Owner's style model: `C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf`.
- Current thesis (READ ONLY): `E:/Code/Report_INT3508/ridebound/` (`main.tex`, `noi-dung/*.tex`).
- Code (READ ONLY): `C:/Code/RideBound-noworse/src/`.
- Run outputs (READ ONLY): `C:/RideBoundData/research/`.
- Claim boundary (READ ONLY): `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`.

## Owner rules (non-negotiable)

1. **Zero fabrication.** Every factual sentence needs evidence: a register row, or a saved output / code / primary
   source you opened yourself. Anything unverified is not written; list it as missing evidence instead.
2. **Never mention sealed plans**, preregistration, plan hashes, "dự đoán trước", "niêm phong", or "kết quả mong
   đợi". This applies to the body, the appendix and footnotes alike.
3. **Language.**
   - Natural Vietnamese, written for a reader outside the field.
   - No English words inside Vietnamese sentences. A technical term appears once with its English in parentheses,
     per the glossary.
   - Academic but not overly technical. Concise and on-topic. Respect the page budget: ≈ 330 words of running text per
     page; a 10-row table with caption ≈ 0.6 page.
4. **Claims.**
   - No "duy nhất", "đầu tiên", "vượt trội", "tối ưu" for a cap, business-value or user-satisfaction claims, or causal
     verbs for the ledger split.
   - Never claim as novel: dynamic insertion, ETA limits, reassignment, route similarity, least-commitment, time
     consistency, user satisfaction.
5. **Numbers.**
   - Every rate shows its count and denominator, and whether it is "gộp theo khách" or "trung bình theo kịch bản".
   - Use Vietnamese number format: 3.672; 7,4 giây.
6. **Never paste code.** Pseudo-code tables in the style of the DACN report are allowed.
7. **LaTeX conventions.**
   - Every factual paragraph is followed by a `% EV: <IDs or anchors>` comment line.
   - Use `\label`/`\ref` for every cross-reference.
   - Use `booktabs` tables.
   - Use existing `\cite` keys; list new keys with full verified metadata.

## Sandbox rules

- Write ONLY inside `S/optimize/codex-debate/codex-work/`, in the subfolder your brief names.
- Create files exclusively and never overwrite. For a second pass use `-v2`.
- Never write to the thesis folder, the drafts folder, `E:/Code/RideBound*` or `C:/Code/*`.
- No simulations, builds or installs. Read-only Python probes are fine. Save each script and its output in your
  subfolder.
- Drive E: is nearly full, so write only small text files.
