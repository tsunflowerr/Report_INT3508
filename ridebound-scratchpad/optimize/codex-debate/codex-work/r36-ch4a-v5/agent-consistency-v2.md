# Round 36 consistency audit (resume, v2)

Read-only audit. No TeX file edited; no build, simulation, install or external write. Probe and output files were created exclusively in `r36-ch4a-v5`; earlier files remain unchanged. Sources and SHA256 values are listed in `agent-consistency-v2-output.txt`. Physical line numbers include blank and comment lines.

`K` = `E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10`; `S` = its parent; `W` = codex-work. A = K/drafts/08-chuong4-phanA-v4.tex; B = K/drafts/09-chuong4-phanB-v10.tex; Ch3 = W/r33-ch3v4/07-chuong3-v4-v3.tex. Required brief, parallel rules, R34 v2 report, A-v2-NOTES, B-v8-NOTES (describing v10) and current Ch2-v4 were read.

## Reference and bibliography resolution

All **40 distinct cross-reference targets used by A** resolve against the current selected documents, with **zero duplicate labels**. The complete use-to-definition mapping is saved in `agent-consistency-v2-output.txt`.

The three former missing targets are now actual sections:

| Target | Actual definition | Content check | Action in A |
|---|---|---|---|
| `muc:c1-cauhoi` | W/r30-ch1/05-chuong1-v3.tex:81 | Three research questions at 119–128, matching A's roadmap | Preserve reference at A20 |
| `phuluc:A` | W/r31-ch5/11-phuluc-v2.tex:12 | Static-scenario scope at 14 | Preserve reference at A224; no dummy label |
| `phuluc:C` | W/r31-ch5/11-phuluc-v2.tex:60 | Actual scenario list, source inventories and reproducibility details at 63–120 | Preserve reference at A148 |

A's six part-B targets resolve in B-v10: `muc:c4-vaitro` B17, `muc:c4-dubao` B77, `muc:c4-dem` B215, `muc:c4-tuyet` B304, `muc:c4-hople` B356. (Five distinct B targets, with multiple uses.) No A cross-reference directly targets Ch2; Ch2 contributes no missing or duplicate label in the selected assembly.

Bibliography draft W/r32-bib/10-tai-lieu-draft.tex defines `horl2022` at 27, `schulz2026` at 34 and `engelhardt2026` at 62. Those keys therefore do not need fabricated entries; the assembler must include the verified bibliography draft. Ch1 and appendix selections must likewise be included; A alone cannot resolve those external references.

## No-op conditions and calibration exclusion

Ch3:366–369 states (N) for the current decision: structural feasibility and identical projection inputs for the retained route and reference e. Ch3:374–375 adds the separate requirement that every promised rider has `0 <= L_r <= B`. Ch3:378–379 proves `p=e` and `L_r + |p-e| <= B`. The all-trip conclusion requires (N) **at every decision**, with `L_r=0` upon acceptance (Ch3:382–385). A's R34 replacement must preserve both the valid-ledger condition and this per-decision condition; reference to (N) alone is insufficient.

Direct code reads agree with the conditions: `InsertionCandidateGenerator.cs:171–182,213–229` treats a structurally infeasible current route or missing no-op as failure; `ServiceQualityAllowance.cs:66–77` keeps structural invariants strict while relaxing time-related service constraints against the unchanged route; `CandidatePortfolioRetainer.cs:102–113` retains the no-op; `CommitmentDecisionValidator.cs:355–360,1048–1064` uses the same schedule projector; `HardVectorCandidateAssessor.cs:144–165` applies the candidate before validation. These excerpts are saved in the supplement output. The numerical zeros are measurements consistent with this conditional result and do not establish an unconditional actual-arrival guarantee.

A107–108's old statement that all 15 calibration scenarios are unused in the thesis is false. `S/tang3/t38/run_t38.py:5–6,42–44` separates 15 C-30 calibration runs and 170 test runs; `S/tang3/t38/T38-REPORT.md:99–106` explicitly audits all 185 and 382.006 ledger revisions. Ch3:725–727 correctly includes those 15 in the ledger-consistency audit. R34 correction3's narrow exclusion from service and on-time results, while retaining their audit participation via `muc:kiemtra`, agrees with these sources.

## Snow addendum

The three requested sources agree: W/R26-CH3-OPEN-QUESTIONS-CODEX.md:253–283; K/evidence/EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md:48 (N4B8-05); K/evidence/checks-ch4b-v8/ch4b-v8-check-2026-10-12.txt:65–72. They show eight snow initializations and 51 C-30 directories with identical binary/core/policy/configuration tuples. R26:274–277 independently binds C-30 policy and WP4 inputs to the configuration hash; WP4:7 specifies `no-worse-than-reference-v1`.

This audit additionally recalculated the DLL SHA256 and obtained `a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac`, matching the recorded manifest hash. Therefore replacing A135 `Chưa kiểm lại` with `Như tập chính`, dropping the caveats in A142 and A435, and updating accompanying EV comments to N4B8-05 is supported. The wording that the archived runner is shared should now include the snow set. This does not demonstrate that a rebuilt binary yields identical trajectories.

## R34 part-B correction status against v10

| R34 item | Current B-v10 | Status / remaining action for B reviser |
|---|---|---|
| Correct 120-second data reuse disclosure (correction4) | B421–423 says selection followed viewing U/C-30 on the main set | Main disclosure fixed. R34's explicit clause about earlier 120-second calculation screens is absent; add equivalent `kể cả các phép tính thử ở 120 giây` if requiring the full replacement. |
| Forced-decision event name (correction8) | B184,286,359 use `bị ép` | Fixed; no old `phải phục hồi` phrase remains. |
| Obligation table reference, if A switches to pooled pairs | B285–288 still says 41,3% mean and points at `bang:c4-nghiavu` | Residual. Replace by 7.710/20.103 and preserve 28/34, with clarification that replay does not change original counters. A pooled table must not be represented as supplying the constituent pairs for the 41,3% mean. |
| Forecast-inside-dispatch means needing constituent counts | B184–185 retains 47,6/62,8% and 39,0/11,0%, means over scenarios | Residual count/denominator obligation; B reviser must verify and show constituent pairs or remove unaccompanied means. Pooled pairs cannot be attached to unchanged scenario means. |
| C-30/C-120 observed zero counts | B359–361 gives 0/20.101, 0/20.435 and U0/20.760 | Count terminology fixed. The conditional no-op sentence at B360 still omits the valid-ledger condition and the requirement for (N) at each decision; align with complete Ch3 conditions. |
| Cap-only contrast | B19–21 says policies differ only in drop cap; B364–368 narrows generation counters | Fixed; the former whole-commitment-package inference is gone. |
| Policy-byte vs runner distinction | Old paragraph removed; B376–379 gives verified snow identity | No erroneous identical-byte cross-set inference remains; no need to reinsert a deleted paragraph. |
| Assembly comment (correction9) | B7 names A-v4 | Correct for the old base; assembler should point to the selected new A-v5 deliverable. |
| Test re-run addendum | B381–384 says 1.024/1.025 plus separately passing final test | Residual; update to single attempt4, 13/10/2026. |

Part B remains read-only in this round. The table records required handoffs and avoids asking A to repair B's body.

## Attempt4 verification and other-chapter handoffs

A-v4 contains **no test re-run sentence**, so do not add one solely for the addendum.

`K/evidence/TESTRUN-45f8026-2026-10-12.md:18` records attempt4 on 13/10/2026 13:39–13:42 as a single full run. The raw log `C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log` confirms date/start at line1, source commit at line3, LF settings at line4, untracked marker at line6, nine passing project summaries at 27,33,39,46,48,60,62,66,69 and exit0 at line70. Independent reaggregation gives **1.025 passed / 1.025 total, 0 failed, 0 skipped**.

Use the actual attempt4 date despite the obsolete example sentence in TestReport:58 (still 12/10/2026). Suggested body wording for B reviser: `Trên đúng mã nguồn đã dựng bộ chạy, cả 1.025 kiểm thử tự động đều đạt trong một lần chạy lại ngày 13/10/2026 (Phụ lục~\\ref{phuluc:C}).` Appendix/notes should retain LF and untracked-file conditions. This is test verification, not proof of binary/trajectory reproduction.

Other-chapter corrections to list without editing them:

- Ch3 W/r33-ch3v4/07-chuong3-v4-v3.tex:724: change date 12/10/2026 to 13/10/2026; line737 change evidence from attempts3+3b to attempt4. Its 1.025 count and environmental conditions already agree.
- Appendix W/r31-ch5/11-phuluc-v2.tex:119–120: update the historical split-run statement to attempt4 single-run result dated 13/10/2026, preserve both environment conditions and use the new log. Earlier attempts may remain as history if desired.
- Include real Ch1 research-question section, real appendix sections and verified bibliography in assembly. All three old missing targets and both previously missing bibliography keys have now been supplied in codex-work.

Probe artifacts: `agent-consistency-v2.ps1`, `agent-consistency-v2-output.txt`, `agent-consistency-v2-supplement.ps1`, `agent-consistency-v2-supplement-output.txt`. The first probe's intended T38 selected-range print was skipped by PowerShell array unrolling; the supplement prints the actual T38:99–106 explicitly. This is a probe-output issue, not an evidence discrepancy.