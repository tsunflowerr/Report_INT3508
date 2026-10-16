# tier3plan

## 1. [RQ-T3 (main question, exact)]
RQ-T3 (chính): 'Ở cùng bộ sinh, cùng hàm mục tiêu, cùng quy tắc phục hồi và cùng thế giới trôi dạt được ghép cặp, cổng hành vi C có tạo được một miền đánh đổi giữa tỉ lệ phục vụ và biến động khách nhìn thấy mà cổng kết quả V và hạn chót I (một chiều M⁺, hai chiều M) không đạt được không?'
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:25-27

## 2. [RQ-T3b (secondary question, exact)]
RQ-T3b (phụ): 'Với một chính sách C đã đóng băng, hiệu chỉnh conformal theo episode có cho một γ sao cho P(V_T ≤ β + γ) ≥ 1 − α trên tập kiểm tra, và β + γ đủ nhỏ để có ích không? Coverage đúng và bound hữu ích là hai yêu cầu khác nhau.' Also: '"C không vượt β" không phải kết quả: đó là hành vi thiết kế.'
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:29-33

## 3. [H1 exact wording]
H1 (cơ chế, từ Định lý 4): 'Dưới mọi thế giới, C không bao giờ kích hoạt phục hồi vì cam kết; V, M, M⁺ kích hoạt với tần suất phụ thuộc chiều trôi. Một episode mà C kích hoạt phục hồi vì cam kết là lỗi cài đặt, kiểm như bất biến.'
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:51-53

## 4. [H2 exact wording (the '>= delta_s pp' claim)]
H2 (đánh đổi): 'Tồn tại vùng (mức nhiễu, β) nơi C phục vụ nhiều hơn V ít nhất δ_s điểm phần trăm trong khi E2 của C không lớn hơn E2 của V quá δ_r. Bác bỏ nếu không có ô nào như vậy trên toàn ma trận khóa, hoặc nếu hiệu ứng biến mất khi đã ghép cùng hàm mục tiêu và cùng tập ứng viên.'
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:54-56

## 5. [H3 exact wording (episode-level calibrated bound)]
H3 (bound): 'γ hiệu chỉnh cho coverage ≥ 1 − α trên tập kiểm tra; gọi là hữu ích chỉ khi β + γ nhỏ hơn một ngưỡng chốt trước (đề xuất: một nửa phân vị 90 của V_r dưới U trên tập phát triển). Coverage đúng mà bound vô dụng thì báo đúng như vậy; không cắt γ cho đẹp.'
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:57-59

## 6. [Codex original H1/H2/H3]
Codex H1: conduct cap avoids spending budget just for keeping route but does not bound visible change (mechanism hypothesis, not superiority). Codex H2: 'tồn tại một miền cường độ/correlation nhiễu và ngân sách mà đánh đổi này có ý nghĩa. Nếu chỉ xuất hiện ở cấu hình cực đoan hoặc biến mất khi ghép cùng hàm mục tiêu, phải thu hẹp hoặc bác bỏ H2.' Codex H3: 'bound có thể đạt coverage mục tiêu trong phạm vi giả thiết, nhưng có thể quá rộng để hữu ích.'
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:67,73,79

## 7. [Locked components]
Unit of inference = episode = (ngày, mẫu nhu cầu, khung, hạt giống thế giới); riders only for distributions, not sample size (K7). Intervention: g ∈ {C, M⁺, M, V} at β ∈ {30, 60, 120} s on drop time. Control U (no research gate, same structural/service/lock constraints) plus paired C–V, C–M⁺ in same episode. Mandatory identity: same raw candidate set (hash before gate), same objective accepted → cost → stable id (ppm fix is separate ablation K12), same repair, same recovery rule. Endpoints: E1 = episode service rate; E2 = share of riders with V_r > 60 s (plus CVaR95 of V_r). Primary evidence: (E1,E2) frontier over β; fixed primary comparison: C-30 vs V-30 same episode. Lifecycle: starts at booking confirmation; pickup closes at actual boarding; drop closes at actual alighting; cancelled/unserved have own denominators.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:39-47

## 8. [Service floor (delta_s) definition]
Sàn phục vụ: 'không kém U quá δ_s điểm phần trăm'; δ_s chốt sau thí điểm T3.7, trước hiệu chỉnh và kiểm tra.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:44

## 9. [Owner decisions already taken (2026-09-24)]
Decided: Recovery R01 = keep route as forced action + typed commitment violation with overshoot amount; ledger never reset; theorems cover only non-recovery part. Mode = exploratory with preregistration like Tier 2 (research branch, ADR Proposed, predictions sealed before). World v1 = noise per OD pair on current 96-node network, shared RNG keyed (worldSeed, odPair, timeBin, componentId), with two-sided mode and shock recovery; must declare it is not a street network. Still open: δ_s, δ_r, α and usefulness threshold, to be fixed after pilot.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:83-91

## 10. [Owner decisions listed as open in T3.1 §7]
1) δ_s, δ_r, α, bound usefulness threshold — after pilot, before test. 2) whether recovery may increase C (R01); if so theorems must include overshoot. 3) exploratory vs official; official needs ADR + builder freeze (plan §7.2); RB-WP14R-009..012, WP15, H7 remain Unauthorized. 4) world v1 edge noise needs real edges (network is 96-node OD closure, K8). Items 2–4 were resolved by §7a; item 1 remains open.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:93-100

## 11. [Owner decisions required after pilot, before calibration/test (T3.7 plan §5)]
Owner (not assistant) must fix from pilot data: service floor δ_s; E2 usefulness threshold (δ_r); benefit margin (biên lợi ích); acceptable recovery burden; run-time budget; desired statistical precision; useful bound width. Also: 'không tệ hơn tham chiếu' rule for already-violated riders (frozen vehicle, ADR-075); world parameters for the main matrix; the fixed confirmatory comparison (proposed C-30 vs V-30).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:72-84

## 12. [Owner decisions required (pilot report §5)]
1) Recovery rule (mandatory before confirmatory comparison): (a) keep ADR-075 and treat recovery burden as part of V/M outcome; (b) 'không tệ hơn tham chiếu' — forced vehicle may accept new riders if no forced rider on it gets worse than kept route (needs ADR, code, test, review); (c) compare only C with M⁺ (M⁺ recovers less). 2) Use world v1.1 for main matrix (proposed yes). 3) δ_s, δ_r, α, bound usefulness threshold. 4) Narrow the claim about choice. 5) Fixed confirmatory comparison: still propose C-30 vs V-30 but only after item 1; report E2 on common riders too. 6) World parameters for main matrix (W4 v1 sigma 0.08 gives edge factor range 0.26–4.92 vs measured day W5 0.84–1.18). 7) Panel A cell d20181114-s10-r1 was seen (T3.5 smoke / T3.6 acceptance, arm conduct-30, E1 0.861 and 0.602) — at T3.8 split must be treated as seen: exclude from test or declare.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:216-246

## 13. [Reference numbers from pilot for choosing thresholds]
Gate price at W0 (no drift): 4–5 riders of 108; C-30 vs U: −5 to +1 riders; C-30 vs V-30: 0 to +10 riders; E2 difference up to 7.2 pp (W4 morning 12/94 vs 5/90). Each cell has 108 requests so 1 pp E1 ≈ 1 rider.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:7,229-233

## 14. [Pilot per-episode served counts and E2]
Served of 108 (U/C-30/V-30/M⁺-30/M-30) and E2 C-30 vs V-30: W0 m 102/97/97/97/97 (0/97 vs 0/97); W1 m 87/82/80/82/79 (15/82 vs 15/80); W2 m 85/86/79/85/79 (32/86 vs 24/79); W3 m 108 all (1/108 vs 1/108); W4 m 96/94/90/92/92 (12/94 vs 5/90); W5 m 92/90/87/90/89 (2/90 vs 2/87); W0 e 99/95/95/95/95; W1 e 83/81/78/81/78 (15/81 vs 14/78); W2 e 79/79/69/78/69 (36/79 vs 29/69); W3 e 107/107/103/107/102 (6/107 vs 7/103); W4 e 92/87/86/86/85 (12/87 vs 8/86); W5 e 100/99/97/99/97 (2/99 vs 1/97). C-30 ≥ V-30 in 12/12, > in 9/12.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:120-139

## 15. [Pilot status of H1/H2/H3]
H1: held 12/12 episodes (C-30 zero recovery decisions; max per-rider dispatch-caused drop shift 19.1 s < 30 s). H2: direction as expected but not concludable — one episode per cell; δ_s, δ_r not fixed; recovery rule confounds (V-30 serving less may be partly frozen vehicles, not budget basis); V's E2 advantage partly rider selection. H3: not measured in pilot; belongs to T3.8.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:13-20,162-163,198-203

## 16. [Pilot go-gates outcome]
Audit correct 60/60: PASS. Choice opportunity: partial (accept/reject question meaningful; insertion-choice too thin → narrow claim). Divergence explainable by mechanism: PASS. Recovery not swallowing majority of trajectories: FAIL for V-30 and M-30 (5/12 episodes each) and M⁺-30 (2/12), counted per decision. C triggers recovery ⇒ bug: PASS (0). Worlds identical across arms: PASS for factors, FAIL for switch timing (up to 131 s), fixed by v1.1 (end-to-end smoke PASS).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:205-214

## 17. [Pilot recovery burden]
Episodes with recovery in >50% of decisions: C-30 0/12, V-30 5/12, M⁺-30 2/12, M-30 5/12. Non-normal decision share (excl. W0): V-30 0.178–0.835; M-30 0.178–0.738. Rider forced-breach share V-30 0.062–0.522. Mean forced fleet share V-30 0.049–0.298. Recovery is majority of decisions but not of vehicles (max 30%).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:146-163

## 18. [Pilot paired E2 on common riders (C-30 vs V-30)]
On common riders V-30 has clearly fewer >60 s riders only at W2 morning (28 vs 21), W4 morning (11 vs 5), W4 evening (12 vs 7). W2 evening common riders equal 26/26; V's E2 advantage there comes entirely from 13 riders only C-30 served (10 of them >60 s).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:174-194

## 19. [Pilot matrix actually run]
5 arms (U, C-30, V-30, Mplus-30, M-30) × 2 dev cells (d20181112-s10-r1-w08, d20181112-s10-r1-w17; 108 requests, 8 vehicles) × 6 worlds (W0–W5) = 60 jobs; runner runner-tier3-v1 from 69512d3; WP4 wp4-tier3-v1.json (commitmentRecovery forced-reference-v1, lateBoarding record-v1); 60 jobs in 11,469 s on 6 threads; 920–1,732 s wall per job; output E:\RideBoundData\research\tier3-pilot-v1.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:37-42

## 20. [Pilot coverage gaps vs Codex P6]
Not covered in pilot (declared): corridor-correlated noise (v1 independent per OD pair) and the CE-3 regime 'C chặn một sửa chữa có lợi' (generator only inserts). Codex P6 required: zero-noise, single shock, repeated shock, corridor-correlated noise, recovering noise, and the beneficial-correction-blocked regime. Codex §17.2 also suggests later 4 arms × independent worlds at low/medium/high load; pilot used only 2 cells at one load (108 requests, 8 vehicles).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:35-40; E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:608,892; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:40

## 21. [Codex P6 go-gate items]
P6 continue gate: audit correct; candidate opportunities sufficient; curves differ explainably; service floor feasible; runtime sufficient for many worlds; recovery does not swallow most trajectories. 'Ngưỡng số cụ thể phải chốt sau pilot dựa vào precision/cost, trước calibration/test.' The pilot report's gate table (6 rows) has no row for 'service floor feasible' or 'runtime sufficient'.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:610; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:207-214

## 22. [Required split (T3.7 plan §1)]
Pilot uses dev panel (wp14-development, days 12 and 13) with micro-worlds; free to look, changes logged. Selection / calibration / test (T3.8, T3.9) must use different episodes: different world seed, and preferably different cells. The split is fixed in the preregistration AFTER the pilot. Panel A (days 14–18) must not be touched here.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:7-12

## 23. [Required split (Codex §9.2, §17.1)]
Four roles: Development (fix code, fixtures, mechanism); Selection/validation (choose policy, β, hyperparameters, score); Calibration (only compute threshold for locked policy); Test (coverage, width, final effectiveness). A random rider split within the same day is not an independent set; synthetic can create independent episodes per seed; historical data must handle day dependence. §17.1: micro-cases; development/pilot; calibration (only γ for frozen policy; simplest is not to select policy on this set); test (confirmatory, only opened after freeze; out-of-distribution stress is a separate labeled panel). If policy/forecast/cadence/recovery changes after viewing calibration/test, it is a new research version; old set becomes development.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:304-313,881-888

## 24. [Panels available and their prior use]
Panel A = days 14–18/11, 20 cells, morning window (used in Tier 2 2A and to build the prediction method cellpred/retrodict). Development panel = days 12–13/11, 16 cells: 8 w08 morning + 8 w17 evening (Tier 2 2B held-out set). 20 cells of panel A = 5 days × 4 demand samples.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:754-755,1471

## 25. [Development panel cell IDs]
16 dev-panel drivers exist: d20181112-s10-r{1..4}-w08/w17 and d20181113-s10-r{1..4}-w08/w17. Tier 3 pilot and sweep used only d20181112-s10-r1-w08 and -w17.
SOURCE: command: Get-ChildItem E:\Code\RideBound-deadline\benchmarks\scenarios\wp14-development (output lists 16 *.driver.json); E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:20; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-PLAN.md:24

## 26. [Data restrictions]
Panel A not to be touched in pilot; one Panel A cell d20181114-s10-r1 already seen in T3.5/T3.6 smoke → must be excluded from test or declared at T3.8. Sweep plan: 'Không dùng panel A.' Risk R8: do not use H6 numbers to choose parameters of new arms (WP15 constraint #2). R13: dev panel not fully unseen — its static outcomes exist in v6 matrix; must be stated in preregistration.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:12; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:239-246; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-PLAN.md:89; E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1565,1571

## 27. [Holdout noise levels (Codex §8.3)]
Held-out test set only uses noise levels locked from the design; stress tests with distribution change are reported separately, not pooled into an average coverage.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:273-275

## 28. [Plan §8.1 unit of inference]
Cell/episode is the independent unit; riders in a cell share fleet state, drift and dispatch decisions. Solver deterministic (solverSeedsAreReplicates: false, two-seed contrast exactly 0), so replication comes from demand samples; re-running a cell with a different (solver) seed does not create an independent sample. Codex §16.2: a different solver seed does not create an extra demand/world sample; multiple solver repeats must be aggregated by a pre-locked rule.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1467-1472; E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:861

## 29. [Plan §8.3 calibration of gamma (procedure)]
No DKW on rider counts (K7). Split-conformal rank rule per episode: (1) lock π, generator, forecast, publication cadence, recovery rule, cohort before calibration; (2) score S_j = max_{r∈cohort(j)} X_{r,j} (or two scores pickup/drop with α split beforehand + union bound); (3) on n calibration episodes k = ⌈(n+1)(1−α)⌉; if k ≤ n then γ = S_(k) (k-th order statistic, 1-indexed ascending), else γ = ∞ and state bound not finite; integer arithmetic, conservative ties, no interpolating quantile (numpy.quantile default is wrong); for α = a/b use k = ((n+1)(b−a) + b − 1) div b; mandatory tests n=18⇒k=19>n⇒γ=∞, n=19⇒k=19, n=20⇒k=20, ties, k=n+1; (4) α=0.05: n=18 ⇒ γ=∞, n=19 ⇒ γ = S_(19) = maximum (finite but usually very wide); (5) under exchangeability P(S_new ≤ γ) ≥ 1−α, combined with C_r ≤ β on every trajectory gives P(∀r: V_r ≤ β+γ) ≥ 1−α; (6) test on m new episodes: count violating episodes, Clopper–Pearson; with 0 violations the one-sided 95% upper bound is 1 − 0.05^(1/m), ≤5% needs m ≥ 58.4 i.e. at least 59 non-violating episodes; (7) rider coverage is descriptive only; (8) if policy changed to reduce X, recalibrate on a new set; never use the same set to select and certify. Refs: Angelopoulos & Bates arXiv:2107.07511 App. D; Barber et al. arXiv:2202.13415.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1488-1519

## 30. [Codex §9 calibration requirements]
§9.1: episode = full demand, fleet, world traffic and policy trajectory in locked window with full drain or explicit censor rule; choose beforehand one score (max of pickup+drop, or two scores with split α + union bound); normalization scale only from pre-outcome info or training set. §9.4: an episode with no accepted riders may have score 0 but share of such episodes and service rate must be reported; achieving coverage by rejecting almost all riders fails usefulness. §9.5: incomplete lifetime — choose beforehand: drain to completion with resource cap, finite-horizon target, or score = ∞; if recovery lets C exceed cap, C≤β no longer holds on those trajectories; do not drop recovery episodes after outcome. §9.6: report episode coverage with denominator, violations and interval; distribution of γ/β and share of bounds exceeding the useful change level; cohorts accepted/completed/long trips; implementation tests on known-distribution scores incl. ties, small n, k=n, k=n+1, integer overflow; shift stress tests are outside guarantee; choose number of episodes from desired precision, cost and published pilot (not '1000 samples').
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:293-344

## 31. [Codex §4.5 two-layer bound restrictions]
If C_T ≤ β on every trajectory and P_π(X_T ≤ γ) ≥ 1−α then P_π(V_T ≤ β+γ) ≥ 1−α (no independence needed). Forbidden: γ taken after viewing test set; γ from another policy without distribution-shift testing; per-step γ called whole-trip guarantee.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:127-131

## 32. [Codex §17.3 n for conformal vs test]
α=0.05: n=19 calibration episodes is the minimum for a finite rank; it is not enough for strong empirical conclusions. 0 failures in m i.i.d. test episodes gives one-sided 95% upper bound 1−0.05^(1/m); ≤0.05 needs ≥59 failure-free test episodes. Mixed regimes: calibration/test must come from the same mixture; pooled guarantee does not cover each regime; per-regime statements need separate calibration; do not add riders to n.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:910-916

## 33. [T3.8 definition and acceptance]
T3.8 = 'Chọn chính sách, rồi hiệu chỉnh conformal theo episode' (sources Codex P7, §9; plan §8.3). Acceptance: 'Tập chọn / hiệu chỉnh / kiểm tra tách bạch, manifest bất biến'.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1364

## 34. [Codex P7 (applies to T3.8)]
Choose budget/objective/forecast on development/validation. Freeze code and hyperparameters before calibration. Compute episode score S = max X per §9; store each score and quantile rank. If bound too wide, report it as practically useless; do not trim gamma. If policy changed to reduce X, new calibration; never use same test set to select and certify. Acceptance: immutable split manifest; no episode overlap between selection/calibration/test; quantile calculation covers small n/ties/infinity; report correct marginal episode guarantee and exchangeability condition.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:612-616

## 35. [Codex selection guidance (applies to T3.8)]
β need not mean the same across I/V/C; report sweep and frontier; may compare at same service level or same risk level on validation set, then lock working point before test. A held-out selection set may be split off to choose configuration, then calibration and test on the chosen policy. Do not implement shortcut β = target − γ calibrated under an old β; select first, calibrate after, or prove simultaneous guarantee for a finite library.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:221,924,951-953

## 36. [Codex E04/E05/E06 (T3.8/T3.9 tooling)]
E04 calibration script takes frozen policy hash, split manifest and score table; integer/rational rank; returns 'infinite' when rank > n; never encode infinity as canonical ms max; checks duplicated worlds, group leakage, empty episode, incomplete active riders. E05 analysis freeze: primary comparison locked before test; episode-level paired deltas, intervals, service floor check, frontier, diagnostics; rider samples only for distributions. E06: one verify command recomputes main tables from bundle without simulator; one regenerate command in pinned simulator env; record wall time, hardware, dependency inventory, known nondeterminism.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:710-714

## 37. [Codex Q01–Q12 calibration/evidence tests]
Q01 exact conformal rank (small n, ties, rank n+1); Q02 score = episode max, independent unit = world per split spec; Q03 manifest/analysis locked before test, policy change requires new calibration; Q04 incomplete trajectories: drain/horizon/score∞ by pre-locked rule; Q05 empty/reject-all episodes: always report service floor and accepted count; Q06 recovery not excluded post hoc; Q07 infinite flag not huge number; Q08 verifier fails on timestamp/failure-file/hash tamper; Q09 oracle recomputes from transcript/actuals; Q10 paired interval clustered by episode/day; Q11 primary negative + secondary positive → keep primary conclusion; Q12 distribution shift reported as separate stress.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:777-792

## 38. [Codex §16.1 required artifacts]
Artifact tree includes specification/{research-question.md, claims-and-falsifiers.md, metric-specification.json, recovery-specification.json, analysis-plan.md, split-manifest.json, frozen-policy-manifest.json}, planned-grid.json, worlds/<world-id>/..., runs/<run-id>/... (incl. terminal-record.json), derived/{per-rider-accounting.json, per-episode-metrics.json, paired-comparisons.json, calibration-scores.json, calibrated-bound.json, failure-census.json, verification-report.json}, report/, bundle-manifest.json. Latent traffic artifact must not be readable by policy.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:796-853

## 39. [T3.9 definition and acceptance]
T3.9 = 'Xác nhận trên ma trận khóa' (source Codex P8). Acceptance: 'Tái tính được từ bundle; mọi ô kế hoạch có kết quả hoặc lý do thiếu'.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1365

## 40. [Codex P8 (applies to T3.9)]
Run locked paired matrix on test worlds, every failure recorded. Verify artifacts before analysis. Report tradeoff frontier, primary fixed comparison, group diagnostics, outcome accuracy, coverage, bound width, recovery and cost. Stress drift is a separate set; if exchangeability broken, conformal guarantee not transferred to stress. Acceptance: others can recompute tables from raw bundle; result for every planned cell or reason missing/exclusion per protocol; do not drop bad worlds after seeing results.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:618-622

## 41. [Codex E03 failure census (T3.9)]
Every planned episode×arm needs an attempt record even if an earlier arm died; resume only from verified artifacts; reruns need supersession/reason, not best-success picking; every valid-pair analysis also reports all-planned denominator and missingness.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:708

## 42. [Plan §8.4 paired effects]
Paired differences within cell: service rate / arrivals, cumulative variation, actual delay, recovery rate, decision latency. CI: paired bootstrap by cell — resample cell IDs keeping all arms and riders; lock number of iterations and analysis seed BEFORE seeing the test set. Codex §17.4 adds: if many windows in the same day, consider resampling by day or hierarchical model; common-served cohort is only a diagnostic (post-treatment selection).
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1521-1525; E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:920-922

## 43. [Plan §8.5 denominators and frontier]
Report absolute and relative change; relative change undefined if baseline 0 (never write 100%). Mean burden on accepted riders is selection-sensitive; also report on arrived riders. When sweeping β, draw descriptive frontier and pre-choose ONE confirmatory comparison; do not sweep a grid and report only the smallest p. Codex §10.5: non-inferiority claims need a justified margin and design, not 'not significant'.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1527-1534; E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:396

## 44. [Codex §17.2 go/no-go form to fill after pilot]
Thresholds to lock before test: Service floor (max pp shortfall vs baseline or absolute completion; from operational need, not equal to observed C); Outcome usefulness (acceptable V or arrival-error quantile; not derived from conduct β); Benefit margin (min service gain or V reduction worth the cost; with sensitivity); Recovery burden (episode/rider recovery share compatible with normal guarantee); Decision runtime (per epoch cadence, specific hardware, whole pipeline); Statistical precision (half-width for primary paired effect/coverage, from pilot variance and cost); Bound width (β+γ still meaningful; if wider than useful horizon, coverage not a success). Do not choose thresholds by looking at test; without stakeholder utility, present frontier and public hypothetical thresholds.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:896-908

## 45. [Plan §9 preregistered predictions for Tier 3]
'3 / ablation ppm': prediction service rate unchanged significantly; confirm if difference < noise floor ±0.3 pp; negate if tier worst-hard-utilization-ppm still ties ≥99%. '3 / hai lớp': prediction γ under drift much larger than 8.7 s of static panel (measured drift d p90 = 47.4 s, max 150.7 s at k=1); confirm: finite bound with n ≥ 19; negate: γ wider than locked usefulness level ⇒ report negative result, do not cut γ.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1550-1551

## 46. [Tier 3 work-package table]
T3.1 question lock; T3.2 reference accounting + micro-oracle; T3.3 failure-aware core; T3.4 late boarding as fact; T3.5 world and forecast separated; T3.6 research evidence (signed v/e/p audit); T3.7 pilot (acceptance: enough real choice opportunity; recovery not swallowing majority of trajectories); T3.8 selection + episode conformal; T3.9 confirmation on locked matrix. Tier 3 only starts if Tier 2 gives a signal.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1338-1365

## 47. [Plan §7.1–7.3 governance and runner]
WP14R 009..012 UNAUTHORIZED; WP15 roadmap only; H7 only after WP15–16 gates → exploratory mode. AGENTS.md: every code change runs dotnet test RideBound.slnx; update docs/18, decision entry, docs/19 when status/contract/claim/baseline changes; never delete corpora/data/artifacts. §7.2 eight-step sealed runner build mandatory for official mode; exploratory mode needs at least steps 1–3, 7 and §7.3 controls (step 1 dotnet test green; 2 Release publish outside repo; 3 stable publish root hashed; 7 repositoryInventorySha256 after commit passed via --expected-repository-inventory-sha256). §7.3: each new runner must reproduce two known arms cell-by-cell before new arms; compare decisions, not semanticHash.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1399-1440

## 48. [Plan §7.4 traps relevant to Tier 3]
N3 new arm falling into EffectivePolicies default branch silently unconstrained (keep EffectivePolicyFairnessTests red); N6 medium verifier requires travelSnapshotVersion == 1 so drift runs cannot pass it; N10 CI with riders as sample size forbidden (K7); N13 post-hoc explanation must not be called confirmation.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1450,1453,1457,1460

## 49. [Risks relevant to Tier 3 (plan §10)]
R4: v0 monotone drift inflates M⁺ vs two-sided noise; Tier 3 must have edge noise and recovery. R8: using H6 numbers to choose new-arm parameters (WP15 constraint #2). R13: dev panel static outcomes already seen in v6 matrix. R9: API session limits — save intermediate results after each step; scripts must have 'reused'. R6: disk > 30 GB is user's decision.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1562,1565,1569,1571,1572

## 50. [Timeline (plan §11)]
Tier 3: 4–10 weeks, only if Tier 2 had a signal → STOP POINT C: full research contribution. Tier 4 separate paper awaiting ADR for WP15.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1591-1594

## 51. [Claim table §5.6 (forbidden, relevant to Tier 3)]
❌ superiority in service rate ('mọi cấu hình có cam kết đều phục vụ ít hơn'); ❌ novelty of least-commitment, time consistency, dynamic insertion, ETA limit, reassignment, route similarity; ❌ CI on riders as independent samples (K7); ❌ results on 'Manhattan road network' (K8); ❌ drift results 'verified' (K9); ❌ 'hệ thống dùng cổng hành vi không bao giờ kẹt / vô nghiệm' — only 'cổng hành vi không bao giờ là nguyên nhân'; ❌ post-hoc explanations called 'xác nhận'; ❌ 'harm-only ledger' as new; ❌ Theorem 4 proof as deep. Claim 3 ('bảo đảm có mức cho mọi khách' vs Elmi) retracted 2026-09-24: difference is the bounded object (operator-caused part), not a level for all riders.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:512-535,550-558

## 52. [Tier-3 claim boundary]
No novelty claims for dynamic insertion, ETA limits, reassignment, route similarity, least-commitment, time consistency, user satisfaction; Rubinstein, Smith & Barbulescu (2012) already had incremental repair, schedule stability, constraint relaxation. Only candidate claim: v/e/p lifecycle decomposition + four-gate-family framework + (if H2 stands) a measured tradeoff region + (if H3 stands) a calibrated episode-level bound. Do not say mechanism better than Schulz & Pfeiffer or Elmi et al.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:77-81

## 53. [Codex §18.3 claim status]
'Outcome probabilistic bound có coverage' requires policy-specific exchangeable episode calibration, proof, test report — status: no empirical calibration yet. 'Tradeoff có lợi tại service/risk target' requires locked paired test, intervals, failure census, actual outcomes — status: no new result. 'Tăng hài lòng khách' and 'X là tác động thuần của giao thông' not claimable.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:957-968

## 54. [Stop / narrow conditions (T3.1 §5)]
If choice set too thin (Ch.4: only 2.48% of a vehicle's sets have ≥2 insertion positions on active epochs) and pilot shows most episodes only no-op → narrow claim about choice instead of adding seeds. If recovery swallows most trajectories → stop, fix recovery design before comparing. If question reduces to 'đặt hard bound ETA' or 'dùng MPA dưới traffic' → revise question before T3.2.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:68-73

## 55. [Do-not rules (T3.7 §6 / Codex §17.5)]
Do not call pruned-candidate differences improvement when chosen routes are the same; do not call a dead run an advantage; do not change endpoints after viewing; do not increase seeds indefinitely when C and V are near equal. Codex §17.5: rounding/cadence creating most X → fix measurement and re-version pilot; raw portfolios differing unintentionally → fix matched design; C lowers C but V/actual error rises too much → report unfavorable tradeoff, change scope or stop H2; C gain only when V crashes → finish typed recovery and baseline and rerun; C≈V → check noise/opportunity, report null; gamma coverage correct but too wide → keep as negative result, never trim gamma manually; C wins in one regime, loses in another → write conditions and frontier, no general dominance claim.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:86-91; E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:926-937

## 56. [Codex §7.3 early-stop criteria]
Stop new claim if literature has same object/decomposition/constraint/evidence; stop algorithm extension if benefit disappears with same objective/generator/recovery; stop bound-usefulness claim if γ too large vs acceptable operational ETA variation even if coverage met; stop moving to large data if late observations, no-op infeasibility and terminal accounting unsolved in micro-tests; without Pareto dominance a meaningful tradeoff can still be reported; do not reselect samples to keep direction.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:234-240

## 57. [Codex §12.3 recovery rule requirements]
Proposed recovery: no new riders in first recovery transaction; preserve membership, pickup-before-drop, capacity, traversed path, edge commitment; evaluate incumbent continuation first, same repair operator/work for all arms; record original promise, new forecast, every violated constraint, never raise old budget, reset ledger or replace initial anchor; recovery priority locked beforehand; if recovery forces exceeding conduct cap record 'conduct-cap-exceeded-in-recovery' with amount and C≤β no longer claimed for that trajectory; return to normal only on predefined predicate. Choice must be explicit: (a) absolute cap and stop trajectory counted as operational failure, or (b) recovery serves riders and cap has public exception (no lifetime hard-cap claim).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md:502-514

## 58. [Recovery option (b) implemented after pilot]
ADR-077 'no-worse-than-reference' recovery (a forced vehicle may take a changed route of its own if every gate it violates was already violated by the kept route and it is not worse on each) committed 45f8026 on branch research/tier3-no-worse (worktree C:\Code\RideBound-noworse), .NET 1025/1025, 2 independent review rounds; Runner v2 C:\RideBoundData\research\runner-tier3-v2 (tree ac251ef3…cff3f, 429 files); WP4 v2 differs from v1 only in commitmentRecovery. Status Proposed, exploratory, default-off. Evidence commit a90b4b7.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-AMENDMENTS.md:27-34; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-REPORT.md:138-140; command: git -C C:/Code/RideBound-noworse log --oneline -6 (a90b4b7, 45f8026 on top of 1ce15e9)

## 59. [Recovery (b) runs cover only M⁺ arms]
The no-worse runs were 28 jobs: 22 treatment = every Mplus-x with forced > 0 in the sweep, 6 controls = 4 C-30 and 2 Mplus-900. No V-x or M-x arm has been run under (b). Output dir C:\RideBoundData\research\tier3-sweep-noworse-v1 has 28 job dirs.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-REPORT.md:141-144; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-AMENDMENTS.md:35-36; command: Get-ChildItem C:\RideBoundData\research\tier3-sweep-noworse-v1 -Directory → 28 dirs

## 60. [C vs M⁺ sweep results relevant to an H2-style service margin]
Sweep (13 arms U, C-x, Mplus-x for x ∈ {30,60,120,300,600,900}; 6 worlds; 2 dev cells; 156 jobs; exploratory, one episode per cell). On 8 drift cells (864 requests; U serves 715): served C/M⁺(a) 697/692 @30, 699/693 @60, 703/704 @120, 714/716 @300, 715/715 @600 and @900; 'chênh ≤ 6/864, dưới 1%, và đổi chiều theo mức'. With recovery (b): C/M⁺(a)/M⁺(b) 697/692/697 @30, 699/693/699 @60, 703/704/705 @120, 714/716/714 @300. Reading: the (a) service gap is a recovery artifact; remaining difference is promise integrity (M⁺(b) own promise broken 14.1/10.8/7.8% at 30/60/120 vs C 0%) and recovery burden (M⁺(b) forced 29.5/19.2/13.6% of decisions). E2 C/M⁺(a) 19.8/18.7% @30.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-PLAN.md:22; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-REPORT.md:50-59,123,153-166,184-189

## 61. [Sweep predictions outcome]
D1, D2, D3 (C 0/72 recovery), D5 (6/8, just enough), D6 held; D4 wrong (7/8; W5 evening not forced); D7 wrong (5/8, 5/8, 7/8).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-REPORT.md:36-46

## 62. [World realism limits (for choosing world parameters)]
Large M⁺ promise breaks come from synthetic worlds W1/W2/W4; on measured day W5 (12/11) M⁺ broke only at x=30 s morning (2.2%, equal to C scored by M⁺ rule), 0% at ≥60 s. The windows run (08–10, 17–19) are after the steep ramp: 07–09h on 12–16/11 peak rise +47–66% (max 15-min step 8.3–16.2%) vs 08–10h +15–23% (max step 3.7–7.1%); 07–09h not run. Per-rider drift on real 12/11: morning 2.2% > 30 s, 0% > 60 s, max 35.2 s; evening max 7.7 s.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-REPORT.md:196-213

## 63. [Synthetic worlds not calibrated to real steps]
Real 15-min factor steps max +7.1% (12/11 morning), +16.2% (largest of week), −5.6% evening; synthetic W1 +60%, W2 +50%/−27%, W3 −15%; W4 shocks ≥0 by construction (world_v1.py:72) with two-sided noise. Worlds are same-treatment fair but not neutral.
SOURCE: C:\Users\quang\.claude\projects\e--Code-RideBound\memory\ridebound-handoff-2026-09-23.md:33

## 64. [World v1.1 timing fix]
Bin switches in v1 were applied at the first _trigger_and_resolve after bin×900 s (lag up to 265 s all bins; cross-arm up to 131 s; C-30 vs V-30 up to 130 s). v1.1 (world/preflight_world_v1_1.py) inserts bin starts into the event clock; 14 checks, 5/5 mutants; end-to-end smoke PASS. W4 morning: timing fix alone changed C-30 − V-30 from +4 to +2 riders (V-30 90→92). Sweep used v1.1; pilot used v1.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:22-28,54-77; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\sweep\SWEEP-PLAN.md:25

## 65. [Choice opportunity after gate (claim narrowing)]
Under C-30 only 4.7–18.7% of decisions with waiting riders still have a vehicle with ≥3 options (no-op + ≥2 insertions); per vehicle 0.7–3.3%. The gate removes most 'how to serve' choice; remaining differences are accept/reject and keep/change route. Proposal: narrow claim about choice.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:30-31,91-104

## 66. [No file records owner decisions on thresholds]
Searching all *.md under E:\Code\Report_INT3508 for 'δ_s|delta_s|δ_r|T3\.8|T3\.9|ngưỡng hữu ích' matched only T3.1-KHOA-CAU-HOI.md, T3.7-KE-HOACH-THI-DIEM.md, T3.7-BAO-CAO-THI-DIEM.md and KE-HOACH-HOP-NHAT-2026-09-23.md work-package rows; none records a chosen value for δ_s, δ_r, α or usefulness threshold. The thesis .tex chapters (E:\Code\Report_INT3508\ridebound\noi-dung) contain no 'conformal', 'delta_s', 'delta_r', 'H2', 'H3', 'T3.8', 'T3.9'.
SOURCE: command: Grep pattern 'δ_s|delta_s|δ_r|T3\.8|T3\.9|ngưỡng hữu ích' glob *.md path E:\Code\Report_INT3508; Grep 'delta_s|delta_r|\\delta|conformal|H2|H3|điểm phần trăm|tang3|Tầng 3|hiệu chỉnh' path E:\Code\Report_INT3508\ridebound\noi-dung (no Tier-3 matches)

## 67. [No T3.8/T3.9 outputs exist]
E:\RideBoundData\research contains deadline-v1, deadline-v1-pilot, runner-deadline-v1, runner-tier3-v1, tier3-pilot-v1, tier3-sweep-v1, tier3-world-smoke-v1, tier3-world-v11-smoke (+ pdf dirs); C:\RideBoundData\research contains runner-tier3-v2, tier3-sweep-noworse-v1. No selection/calibration/test output directory exists.
SOURCE: command: Get-ChildItem E:\RideBoundData\research and C:\RideBoundData\research (top level)

## 68. [Run budget data]
Per job ~82–86 MB (tier3-pilot-v1 60 dirs 4.82 GB; tier3-sweep-v1 168 dirs 14.08 GB; tier3-sweep-noworse-v1 28 dirs 2.26 GB). Per job 920–1,732 s wall; 60 jobs took 11,469 s on 6 threads. Free space now: C: 103.8 GB, E: 41.8 GB. Policy: keep E: ≥ 40 GB and C: ≥ 50 GB free; never delete to free space.
SOURCE: command: Get-ChildItem -Recurse size sums (output above); command: Get-PSDrive C,E; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:42; C:\Users\quang\.claude\projects\e--Code-RideBound\memory\MEMORY.md (Disk policy line)

## 69. [Git state of research branches]
Worktrees: E:/Code/RideBound 41a4e11 [main]; C:/Code/RideBound-noworse a90b4b7 [research/tier3-no-worse]; E:/Code/RideBound-deadline 1ce15e9 [research/tier3-failure-aware]; E:/Code/RideBound-py-baseline 8d1ea4d (detached). Commit 1ce15e9 records T3.5–T3.7 in docs/18 + docs/19 (§30) and states 'Không authorize RB-WP14R-009..012, WP15 hay H7'; recovery rule must be fixed by research owner before confirmatory comparison; Panel A cell d20181114-s10-r1 must be declared at T3.8.
SOURCE: command: git -C E:\Code\RideBound worktree list; git -C C:/Code/RideBound-noworse show 1ce15e9 -- docs/18-status-and-decision-log.md

## 70. [Tier 2 facts that must not be re-claimed as Tier 3 results]
C not infeasible due to commitment in 0/56 runs; one-sided 30 s deadline infeasible in 19/20 morning cells; evening held-out: one-sided 0/8, two-sided 7/8 (lower bound), outcome gate 8/8; sealed per-cell predictions correct 98/102, 31/32, 40/40 — all exploratory. Tier 2 cannot give service rates under drift because any infeasible cell stops the run, and 11/20 main-panel cells stop on pickup-window invariant even under C.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:8-16

## 71. [Mandatory counterexamples]
'C tốt hơn V': favorable drift makes V/M reject the no-op (Tier 2 evening M 7/8, V 8/8, C 0/8); pilot observed at W3 evening (C-30 107 served, 6 >60 s vs V-30 103, 7). 'C tệ hơn V': CE-2 (v=600, e=660, p=660: C=0, V=60); CE-3 (v=600, e=720, p=600): repair keeping promise is penalized by C — CE-3 regime not covered in pilot.
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.1-KHOA-CAU-HOI.md:61-66; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:140-142; E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-KE-HOACH-THI-DIEM.md:37-38

## 72. [E2 denominator used in pilot]
E2 in pilot = riders with total visible drop-time change > 60 s over riders promised by that same arm (per-arm denominator).
SOURCE: E:\Code\Report_INT3508\ridebound-scratchpad\tang3\T3.7-BAO-CAO-THI-DIEM.md:135

## 73. [Known technical barriers listed for Tier 3]
FleetPy protocol.py rejects commitmentBreachDeclared; _fleetpy_plan merges service and structural feasibility; _fleetpy_stop uses original latest pickup; passenger callback must equal batch time; change_prq_time_constraints edits FleetPy plan without event to runner (forbidden); PairedComparisonDesign rejects two arms with same policyId; DecisionInducedBurdenCalculator forbids cancellations; MechanicalMetricCalculator counts commitmentBreachDeclared actions, not incident ledger; BenchmarkSeed has no traffic-noise component.
SOURCE: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md:1367-1373

# UNVERIFIED
- Whether the research owner has decided δ_s, δ_r, α, the bound usefulness threshold, benefit margin, acceptable recovery burden, run budget, statistical precision, useful bound width, the confirmatory recovery rule ((a)/(b)/(c)), world parameters of the main matrix, or the fixed confirmatory comparison verbally in the chat — no file records a decision.
- Whether world v1.1 has been formally adopted by the owner for the main matrix (it was used in the sweep, but no decision entry was found).
- The value of the proposed H3 usefulness threshold ('một nửa phân vị 90 của V_r dưới U trên tập phát triển'): no file I read computes the p90 of V_r under U on the development set.
- Exact fixture directory/ID list of Panel A (days 14–18/11); I did not list it (main repo tree off-limits; only dev-panel drivers were listed in the E:\Code\RideBound-deadline worktree).
- Whether the seen Panel A cell 'd20181114-s10-r1' refers to one cell or several windows; the report gives the ID without a -wXX suffix.
- Whether pickup-coordinate X is also in scope for the H3 score (T3.1 E2 is on drop time; plan §8.3 allows max or two scores with split α) — no choice recorded.
- The incomplete-lifetime rule for calibration scores (drain / finite horizon / score ∞, Codex §9.5) — no choice recorded.
- Bootstrap iteration count and analysis seed for paired CIs (plan §8.4) — not locked in any file read.
- Whether V-30/M-30 recovery burden under ADR-077 (b) would still trip the pilot stop gate — not run.
- Whether 'chương 3' in the user's request means thesis Chapter 3 (07-chuong3.tex, theory) or Tầng 3 (Tier 3); Tier 3 results currently appear in thesis ch4 (muc:quet) per the handoff memory.
# WARNINGS
- The symbol δ_s means two different things in T3.1: the service floor 'không kém U quá δ_s điểm phần trăm' (T3.1-KHOA-CAU-HOI.md:44) and the H2 margin 'C phục vụ nhiều hơn V ít nhất δ_s điểm phần trăm' (T3.1-KHOA-CAU-HOI.md:54). T3.7-KE-HOACH-THI-DIEM.md:75-77 lists 'sàn phục vụ δ_s' and 'biên lợi ích' as separate items. The owner has to separate them before preregistration.
- The pilot stop gate fired: V-30 and M-30 recover in most decisions in 5/12 episodes (T3.7-BAO-CAO-THI-DIEM.md:212). The confirmatory C-30 vs V-30 comparison is blocked until the recovery rule is fixed (T3.7-BAO-CAO-THI-DIEM.md:220-225,235). Rule (b) (ADR-077) has only been run on M⁺ arms.
- The exploratory sweep shows C and M⁺ with rule (b) serving the same number of riders (697 vs 697 at 30 s on 864 requests; SWEEP-REPORT.md:161). A '≥ δ_s pp' service claim against M⁺ is therefore not supported. H2 as locked is against V, and V has not been run under (b). Part of V-30's service deficit in the pilot may come from the recovery rule (T3.7-BAO-CAO-THI-DIEM.md:162-163).
- Episode supply is short. Only 36 distinct (day, demand sample, window) cells exist: 20 Panel A morning cells plus 16 dev cells (KE-HOACH-HOP-NHAT-2026-09-23.md:754). Conformal calibration needs n ≥ 19 at α = 0.05, and the zero-violation Clopper–Pearson test needs m ≥ 59 (KE-HOACH-HOP-NHAT-2026-09-23.md:1507,1513). Selection, calibration and test therefore have to reuse demand cells across different world seeds, or new cells must be built. Reusing cells weakens independence and exchangeability (T3.7-KE-HOACH-THI-DIEM.md:11 says 'tốt nhất khác cả ô'). This is derived arithmetic; the owner must decide.
- Both panels were already used in Tier 2: Panel A in 2A and the dev panel as the 2B held-out set. d20181112-s10-r1-w08/w17 were used heavily in the pilot and the sweep, so they can only serve as development. One Panel A cell (d20181114-s10-r1) was seen during Tier 3 smoke runs.
- Disk space on E: is 41.8 GB free against a 40 GB floor. At about 82–86 MB per job, that leaves room for only about 20 more jobs on E:. C: has about 53 GB above its 50 GB floor, roughly 600+ jobs. This is derived from the measured sizes and the memory disk policy.
- The pilot has one episode per (world, cell) and no confidence intervals (T3.7-BAO-CAO-THI-DIEM.md:6,250). It gives no between-episode variance for choosing precision or run count. The v1.1 timing fix alone moved C−V by 2 riders, the same size as the effects (T3.7-BAO-CAO-THI-DIEM.md:73-77).
- E2 uses each arm's own promised riders as the denominator (T3.7-BAO-CAO-THI-DIEM.md:135), so it depends on which riders each arm accepted. Plan §8.5 requires also reporting on arrived riders. Codex §17.4 says the common-served cohort is only a diagnostic.
- The synthetic worlds W1/W2/W4 have much larger jumps than measured traffic, and real-traffic windows 07–09h were not run. The world parameters for the main matrix are still an open owner decision (T3.7-BAO-CAO-THI-DIEM.md:236-238; SWEEP-REPORT.md:196-213).
- Tier 3 runs in exploratory mode. RB-WP14R-009..012, WP15 and H7 are Unauthorized. Drift runs cannot pass the project medium verifier (travelSnapshotVersion == 1, K9), so results must not be called 'verified' or 'confirmed' beyond what the preregistered design allows.
- Codex P6 items that were not covered or not evaluated in the pilot: corridor-correlated noise, the CE-3 beneficial-correction regime, load variation, and the 'service floor feasible' and 'runtime sufficient' gates.