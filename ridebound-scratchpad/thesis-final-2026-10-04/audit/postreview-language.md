# Post-review language audit

Date: 2026-10-05. This pass edits only `source/main.tex` and the assigned prose files:
`04-viet-tat`, `05-chuong1`, `06-chuong2`, `08-thietlap-va-h6`,
`08-trongdiem-troidat`, `08-t38`, `08-hanche`, and `09-chuong5`.
Frozen review reports, the review packet, research code, result artifacts, and the
English abstract were not edited. Compilation and rendered-page verification are
handled by the main editing pass.

## Guidance and scope

Read both local skill routers:

- `E:/Code/Report_INT3508/ridebound-scratchpad/nature-skills-audit-2026-10-04/skills/nature-polishing/SKILL.md`
- `E:/Code/Report_INT3508/ridebound-scratchpad/nature-skills-audit-2026-10-04/skills/nature-writing/SKILL.md`

Loaded their manifests and shared/core guidance, the algorithmic and generic-target
fragments, relevant prose-section fragments, main-text discipline, and discussion
language calibration. The manifest's default English language fragments were read
for sentence and paragraph principles; this Vietnamese thesis was not translated.
This was a local clarity pass, not a section or argument reconstruction. Additions
replace ambiguous phrases or supply the minimum definition needed at first use.
No results were relocated or removed, and all quantitative reports remain in their
existing main-text/table locations.

## Terminology ledger

| Canonical form | Clarification and location |
|---|---|
| mốc chiếu giữ tuyến | The forecast obtained by retaining the route from the current state; clarified for `$e_t$` in the symbol list and aligned in Chapters 1, 2, and 5. |
| cơ sở thông báo nhìn thấy | The basis that records all published-promise movement; clarified for `$V$` and in Chapter 2. Mathematical notation is unchanged. |
| tập ô thực nghiệm (panel) | Introduced in Chapter 1, then shortened to tập ô in the assigned sections. |
| ô / lần chạy mô phỏng | Chapter 4 defines an ô as day, demand sample, and window; a run is an arm on a cell under a travel-time regime. The ambiguous prose word episode is removed. |
| bộ thực thi (runner) | Introduced in Chapter 1; Vietnamese form used thereafter. |
| bộ chuyển đổi (adapter) | Introduced in Chapter 1; Vietnamese form used thereafter. |
| ảnh chụp dữ liệu (snapshot) | Chapter 4 now says travel-time data are fixed from a time point. |
| băm kiểm kê kho mã (inventory) | T38 identifies the hashed object and its components; details verified below. |
| SLA | Expanded as Service Level Agreement / thỏa thuận mức dịch vụ in the glossary and at its substantive T38 use. |
| Chứng minh | `main.tex` sets `\proofname`; theorem definitions, geometry, fonts, and layout settings remain intact. |

## Specific corrections

- Chapter 1 calls the comparison an independent replication at the conceptual
  level on a separate system. It explicitly excludes reproducing the original
  papers' complete algorithms or experiments.
- Chapter 2 adds two source-verified Haferkamp sentences: accepting an offer makes
  its pickup time and assignment binding; subsequent route changes must keep
  arrival times in the service windows, with a small permitted pickup delay.
  No drop-off deadline or numerical comparison is attributed to this paper.
- Tier 2's 56 is described as runs: 20 static main runs, 20 variable main runs,
  and 16 variable development runs. It is not a count of distinct input cells.
- T38 replaces the misleading “sàn năm khách” with the planned service-cost
  ceiling of five customers per cell. The existing interval and interpretation
  boundaries are retained.

## Primary-source verification

Read `review-packet-v1/papers/haferkamp2024.pdf` directly using PyMuPDF from
`TASK/runtime`, executed with
`E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B`.

- PDF page 5: a chosen pickup-time option and assignment are binding, while
  minor deviations can permit further route stops.
- PDF page 6: pickup service windows derive from the agreed pickup time and a
  maximum-delay constant; rescheduled arrival at each stop must be within its
  service window.
- PDF page 8: the baseline pickup-deviation allowance is one minute. The revised
  thesis uses only the qualitative small-delay description, not this number or a
  cross-system performance comparison.

For the inventory sentence, traced the read-only call chain
`tang3/t38/run_t38.py` → `tang3/w07/run_w07.py` →
`tang3/world/preflight_world_v1_2.py` and its imported world wrappers →
`E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py`.
The latter's `_repository_inventory_sha256` at line 740 hashes Git HEAD and the
sorted relative paths, byte lengths, and contents of files selected by
`git ls-files --cached --others --exclude-standard`. The T38 prose states this
scope, rather than implying a demand-data or result-artifact hash. No files in
this call chain were changed.

## Preservation checks

Compared every owned source file with its corresponding frozen
`review-packet-v1/source` file using read-only extraction:

- All `$...$` expressions and equation/align environments are identical.
- All `\texttt{...}` identifiers are identical, including path/code identifiers.
- Numeric-token sequences are identical, except the explicitly requested
  insertion of `20`, `20`, and `16` explaining the existing total of 56 runs.
- No geometry, font, table-column, figure-size, or theorem-environment settings
  were changed. The only preamble change is the proof label.
- A targeted term search found the English prose terms only in their first-use
  explanations; episode, “56 ô”, and “sàn năm” no longer occur in the owned files.

Whitespace-token counts below are an auditable size measure, not natural-language
word counts; Vietnamese syllables and LaTeX tokens are counted separately.

| File | Before | After |
|---|---:|---:|
| `main.tex` | 167 | 170 |
| `04-viet-tat.tex` | 495 | 512 |
| `05-chuong1.tex` | 2,063 | 2,100 |
| `06-chuong2.tex` | 2,638 | 2,688 |
| `08-thietlap-va-h6.tex` | 3,004 | 3,047 |
| `08-trongdiem-troidat.tex` | 2,140 | 2,182 |
| `08-t38.tex` | 2,575 | 2,626 |
| `08-hanche.tex` | 944 | 946 |
| `09-chuong5.tex` | 1,756 | 1,761 |

## Chapter 5 short-tail tightening after v2 visual QA

Following the read-only v2 inspection recorded in `visual-qa-049-067.md`, only
`source/noi-dung/09-chuong5.tex` was revised to absorb the six-line chapter-end
tail through prose tightening. No font, margin, spacing, float, page-break, or
other layout command was added or changed. This pass did not compile the thesis;
the main editing pass will verify the pagination in the next build.

The Chapter 5 whitespace-token count fell from 1,761 to 1,657, a reduction of
104 tokens (5.91%). This targets approximately six to eight typeset lines without
removing a paragraph or scientific limit. All 20 paragraph units and all chapter,
section, and RQ paragraph labels remain in their original order. Direct comparison
with the source before this pass confirms identical numeric-token sequences,
inline mathematical expressions, and reference/citation commands.

Substantive-equivalence check:

- The opening still separates the conditional mechanism proof from performance
  measured in a specific simulation.
- RQ1 retains the per-passenger/per-dimension ledger, preselection gate, zero
  keep-route increment, conditional keep-route theorem, absence of an actual-arrival
  guarantee, noncausal interpretation, and prior-art/novelty boundary.
- RQ2 retains every H6 and T38 count and difference, the whole-package attribution,
  negative H6 conclusion, path-dependent budget comparison, common recovery rule,
  absence of a service advantage, and absence of a universal optimum.
- RQ3, recovery obligations, observed violation rates, the conditional visible bound,
  and the early-window/population coverage limits are unchanged.
- The limits still include the small derived network and fleet, scalar real-source
  traffic factor, one seed/domain, exploratory sealing, development-selected split
  and threshold, the 75 shared source trips, within-day dependence, cell bootstrap,
  one-cell reserve sensitivity, insertion-only generator, beneficial repairs being
  charged, and missing user-choice/acceptance/satisfaction evidence.
- All three next tests remain: independent time-varying verification with failure
  classification; transfer tests with independent groups and window-level coverage;
  aligned leg locking before generator comparison, plus a separate user study.
  The priority of independent verification and the three possible commitment-design
  choices remain explicit.
- The closing still reports an enforceable behavioral quantity with measured service
  cost, distinguishes dispatch movement from keep-route movement and visible results,
  and excludes replacing an actual-arrival guarantee at operational scale.

Cuts remove repeated framing and longer equivalents such as “kết quả cần được đọc
theo,” “câu hỏi cần trả lời là,” and “cung cấp cách phân biệt.” No numerical report,
reference, or material scientific restriction was deleted.
