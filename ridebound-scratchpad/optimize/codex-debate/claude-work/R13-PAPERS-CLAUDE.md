# R13: Claude-side reading of the owner's 13 PDFs (`C:/PDF/Paper/`)

This was written 2026-10-10 by a Claude-side reader for Round 13, against `ROUND13-FACT-PACK.md` (owner questions O2, O3, O6). I did not open any `codex-work/R13-*` file.

## Read this first (5 lines)
1. **No supplied PDF measures operator revenue or retention from reliable promises.** The O2 evidence is indirect: secondary citations, plus the fact that every dynamic pooling/DARP paper here protects already-accepted riders with a bound (§14, bullets 1–2).
2. **On O3, riders' sensitivity to lateness depends on the source.**
   - The 2026 meta-analysis values lateness against the expected arrival at about 2.5–3.1 minutes of in-vehicle time (WARDMAN26).
   - The one pooled-service study values small unannounced delay *below* in-vehicle time (ALONSO20).
   - Both must be reported (§4, §5).
3. **The novelty boundary is tighter than the fact pack lists.**
   - Fielbaum & Alonso-Mora (2020) already measure dispatch-caused change against the first announcement, test freeze rules, and report the stability–rejection trade-off.
   - Schulz & Pfeiffer (2026) already give each rider a communicated bound on post-acceptance slip of the drop-off time.
   - What remains defensible: cumulative two-sided |c| budget at seconds scale + dispatch/traffic ledger under measured speeds + forecast quote (§2, §3).
4. **The example UET thesis is a modest bar.** It re-implements two published insertion algorithms, adds one small greedy pruning variant, builds a system, and runs one synthetic scenario. RideBound's evidence is already stronger. What RideBound lacks relative to it is an explicit chapter that varies one pipeline step (§1).
5. **The best-matched optimization pattern** is "one pipeline step with a measured served-vs-promise trade-off". SCHULZ26's reinsertion costs accepted riders 98 s of extra slip for 1 pp fewer rejections. That maps to a budget-aware insertion/reinsertion or budget-allocation step under rule C (§1.10, §14).

## Method and conventions
- **Sources.** Plain text came from `pdftotext -layout` in `.../scratchpad/papers/<basename>.txt`.
  - The example thesis was read **visually**. All 65 pages were rendered to PNG with the built-in Windows `Windows.Data.Pdf` API (no installs) into the session scratchpad (`thesis-pages/`), and the figures were zoomed (`thesis-pages-hi/`).
  - Key tables in five papers were also rendered and checked visually (`paper-pages/`). These are temporary files in the session scratchpad, not project files.
- **Readers.** Four Claude readers (A: ALONSO20/WARDMAN26/FIELBAUM20; B: SCHULZ26/RAUH25/MOLENBRUCH15; C: AZADEH22/FIELBAUM-SCALE/HCRIDE25; D: SRIDHARAN87/KOVACS14/BREGNI11) each read their papers in full. I read the thesis and FIELBAUM20 §2–3, §6–7 myself, re-checked every anchor I kept, and checked the tables flagged "checked visually".
- **Anchor format.** `[ALIAS:line] "verbatim fragment"`.
  - The fragment is a contiguous substring of that single txt line, with whitespace collapsed.
  - Every such pair in this file was machine-checked with `scratchpad/tools/verify_quotes.py` (log in the Appendix).
  - `(PDF p.N)` means read visually on that PDF page.
  - "My arithmetic" marks derived numbers. "UNVERIFIED" marks anything I could not confirm.

| Alias | txt / PDF basename |
|---|---|
| THESIS | `21020283-3476 (1)` (example UET thesis, 2024) |
| FIELBAUM20 | `Unreliability_in_ridesharing_systems_Measuring_cha` |
| SCHULZ26 | `s00291-026-00847-0` |
| ALONSO20 | `Value_of_time_and_reliability_for_urban_pooled_on-` |
| WARDMAN26 | `1-s2.0-S0965856426000662-main` |
| AZADEH22 | `1-s2.0-S0191261522000716-main` |
| RAUH25 | `s00291-025-00812-3` |
| MOLENBRUCH15 | `OperationalEffectsofServiceLevelVariations-publication151005` |
| FIELBAUM-SCALE | `Scale_analysis_for_on-demand_ridepooling_systems_a` |
| KOVACS14 | `Networks - 2014 - Kovacs - Vehicle routing problems in which consistency considerations are important  A survey` |
| SRIDHARAN87 | `FreezingtheMPSMgtScipaper` |
| HCRIDE25 | `2508.04811v1` |
| BREGNI11 | `BregniA._DAvinoM.SchiraldiM.M` |


## 1. Example thesis (THESIS): Phạm Xuân Bách, UET 2024

I read this one visually. All 65 pages were rendered with the built-in Windows PDF API into the session scratchpad and viewed page by page. "PDF p.N" is the PDF page. The printed page number is N−1: the abstract on PDF p.2 is printed as page 1, and the list of figures, printed as page 5, is PDF p.6. Where the broken-diacritics text was still searchable, I add a txt line as well.

### 1.1 Identity
- **Title:** "NGHIÊN CỨU TỐI ƯU LỊCH TRÌNH CHO BÀI TOÁN CHIA SẺ CHUYẾN ĐI".
- **Type:** "KHÓA LUẬN TỐT NGHIỆP HỆ CHÍNH QUY", Ngành: Công nghệ thông tin, Trường Đại học Công nghệ, ĐHQG Hà Nội.
- **People:** Sinh viên Phạm Xuân Bách (lớp QH-2021-I/CQ-I-IT1). Cán bộ hướng dẫn: TS Vũ Thị Hồng Nhạn.
- **Year:** Hà Nội, 2024 (PDF p.1).
- **Grade:** the PDF does not show a grade or the committee's verdict. That it was "accepted" is UNVERIFIED from this file.

### 1.2 Problem (chapter 1)
- **Need:** real-time matching that is "nhanh, chính xác, tối ưu được chi phí". The system must also cope when there are not enough drivers, because cancelled requests "ảnh hưởng rất lớn tới trải nghiệm khi sử dụng ứng dụng, làm giảm doanh thu cũng như giảm tỉ lệ quay lại sử dụng dịch vụ" (PDF p.9). This business-value sentence cites no source.
- **Goal** (§1.2): assign each request to a taxi by computing the best insertion position. The objective is "tối ưu thời gian xử lý, tối đa hoá số lượng yêu cầu được phục vụ và tối thiểu chi phí phục vụ tất cả các yêu cầu" (PDF p.10).
- **Gap claimed** (§2.2.2): a previous UET thesis [19] (Võ Công Thành, 2023) had already implemented Linear Plain, which takes insertion from O(n³) to O(n). That approach still suffers from "First Come First Serve": the nearby taxi is gone, so another taxi must be dispatched, and taxis run short. "Từ đó, khoá luận này cải tiến Linear Plain và đề xuất thuật toán Prune Prophet vẫn giữ được độ phức tạp thời gian là O(n) và tối ưu hơn về số lượng taxi cần sử dụng bằng cách tận dụng dữ liệu dự đoán về yêu cầu đặt xe" (PDF p.14; reference [19] on PDF p.57).

### 1.3 Component optimized
- **The step:** inserting one request's pickup/drop-off pair (o_r, d_r) into one taxi's schedule, together with choosing the taxi.
- **Prediction layer:** "guidance routes" are built from predicted requests, so that idle taxis move toward predicted demand. They wait there until the predicted request appears (PDF p.11 bullet "Prophet"; PDF p.31-33).

### 1.4 Algorithms (all in §3.6)

| # | Name | Source | What it does | Complexity |
|---|---|---|---|---|
| 1 | Basic Plain (Thuật toán 1–3) | standard | Enumerates every (i, j) pair, checks feasibility (capacity and latest time, Thuật toán 2) and computes the added travel time (Thuật toán 3) | O(n³) (PDF p.25-26) |
| 2 | Linear Plain (Thuật toán 4) | Tong et al. [9] "A Unified Approach to Route Planning for Shared Mobility" (2018) (PDF p.56) | Detour det(l_i,l_j,l_k) plus arrays ddl, arr, slack, picked, and the Dio[j]/Plc[j] dynamic programme. For each drop-off position j it finds the best pickup position in O(1) | O(n) (PDF p.26-31) |
| 3 | Prophet framework (Thuật toán 5–7) | Tong et al. [10] "Unified Route Planning for Shared Mobility: An Insertion-based Framework", ACM TODS 47.1 (2022) (PDF p.56) | See steps below | O(n) per insertion (PDF p.37) |
| 4 | Prune Prophet (Thuật toán 8) | **the only algorithm the author proposes** | Two binary searches find the first and last feasible drop-off positions (deadline at l_k vs t_r; arr[mid] ≥ e_r). The Prophet scan is restricted to that range | Still O(n), but "thực tế là nhanh hơn" (PDF p.41-42) |

Prophet framework steps:
- **Part 1** (Thuật toán 5): predicted requests are inserted into "virtual workers". A max-heap ranks the virtual routes by number or revenue of requests served. Real taxis are then assigned to the best guidance routes (PDF p.31-32).
- **Part 2** (Thuật toán 6): each real request is inserted into the guidance route of the cheapest candidate taxi. It is accepted only if the penalty p_r ≥ α·Δ*, otherwise rejected.
- **Objective:** the unified cost UC(W,R) = α Σ D(S_w) + Σ_{r∈R⁻} p_r (PDF p.33).
- **Predicted requests** are given c_r = 0 and e_r = ∞ (PDF p.33-34).
- **Prophet-insert** (Thuật toán 7) extends Linear Plain with wait[k], sumWait and a modified slack (PDF p.34-36).

What Prune Prophet costs: the author states the pruning "là tham lam và điều này làm cho kết quả tìm ra vị trí chèn cặp (o_r, d_r) không còn là tối ưu nhất nữa nhưng đổi lại hiệu năng về thời gian của thuật toán lại được cải thiện hơn" (PDF p.42). This is an explicit speed-versus-optimality trade-off.

### 1.5 Simplifying assumptions (stated)
- Constant taxi speed, so added distance equals added time (PDF p.23).
- A grid map with 250 m × 250 m cells (32 × 64 = 768 cells) and an anchor point per cell. A shortest distance is a lookup that takes O(1) (PDF p.20, p.45).
- "Để khoá luận không phức tạp thêm, tôi coi các yêu cầu dự đoán được là một phần của dữ liệu yêu cầu ban đầu" (PDF p.22). In the worked example, R̃ = R (PDF p.38).

### 1.6 Data
- **System stack:** Spring Boot (Java 17), NextJS, MySQL and the HERE Maps API, on one MacOS i7-9750H laptop with 16 GB (PDF p.43).
- **Online requests:** "Tôi sinh các yêu cầu đi chung xe trực tuyến ngẫu nhiên" (PDF p.44).
- **Predicted requests:** "Từ các yêu cầu đi chung xe trực tuyến, tôi sinh ra các yêu cầu đi chung xe dự đoán dựa trên thời gian - địa điểm (mô phỏng đầu ra của một mô hình học máy ví dụ như [8])" (PDF p.45). The prediction accuracy is set to 25% (PDF p.43, p.47; txt l.1757, l.1839).
- **No ML model is actually trained or evaluated** in chapter 4. The abstract's ML forecasting is simulated.
- **Scenario:** 200 requests and 21 taxis of different capacities in a Hanoi bounding box. Most destinations are schools or companies, between 07:00 and 08:30 (PDF p.46; txt l.1819-1824).

### 1.7 Baselines and metrics
- **Baselines:** Basic Plain and Linear Plain. Non-sharing (one passenger per car) is the reference for vehicles and cost (PDF p.46).
- **Metrics** (list of figures, PDF p.6; results PDF p.47-49):
  - served requests (Fig 4.5);
  - number of taxis or groups used (Fig 4.6);
  - cost per served request, normalised so that non-sharing = 1 (Fig 4.7);
  - total running time to serve the requests (Fig 4.8, captioned "(đơn vị: s)").
- **Load levels:** 50, 100, 150 and 200 requests.

### 1.8 Reported results
I read the values off the figures at high zoom, so each is ±1 grid step.

| Total requests | Served (Fig 4.5, PDF p.47): Basic / Linear / Prophet / Prune | Taxis used (Fig 4.6, PDF p.48) | Cost per request (Fig 4.7, PDF p.48) | Running time (Fig 4.8, PDF p.49) |
|---|---|---|---|---|
| 50 | 50 / 50 / 50 / 50 | 17 / 19 / 10 / 12 | 0.40 / 0.40 / 0.31 / 0.33 | ~121k / ~28k / ~13k / ~9k |
| 100 | 100 / 96 / 100 / 100 | 21 / 21 / 19 / 21 | 0.26 / 0.26 / 0.36 / 0.36 | ~106k / ~40k / ~50k / ~37k |
| 150 | 114 / 105 / 126 / 118 | 21 / 21 / 21 / 21 | 0.27 / 0.28 / 0.36 / 0.34 | ~154k / ~67k / ~78k / ~50k |
| 200 | 115 / 103 / 120 / 110 | 21 / 21 / 21 / 21 | 0.28 / 0.32 / 0.39 / 0.40 | ~240k / ~178k / ~117k / ~61k |

How the author reads the results (PDF p.47-49):
- Prophet is best under a limited fleet.
- Prophet needs "chỉ 9 xe taxi ... với 50 yêu cầu so với 17 taxi của thuật toán Linear Plain".
- Every algorithm cuts cost by "gần 50%" relative to non-sharing.
- The prediction algorithms cost more per request because taxis reposition.
- Prophet is "gần gấp 2 lần" better than Linear in running time at high load.
- Prune Prophet is much faster still.

Issues an examiner could raise (my reading, not stated in the thesis):
1. **The text and the figures disagree.**
   - 9 taxis in the text versus about 10 in the figure for Prophet at 50 requests.
   - The text's "17 taxi của Linear Plain" matches Basic in the figure; Linear is about 19.
   - The text says "Prophet chỉ cần 18 phương tiện" at 100 requests; the figure shows about 19.
   - The fleet is "21 xe" on PDF p.46 but "giới hạn là 20" and "nhiều nhất 20 xe" on PDF p.47.
2. **Basic and Linear give different results.** Linear Plain is presented as an exact O(n) speed-up of the same insertion, yet it serves fewer requests than Basic (105 vs 114 at 150). The pages I read do not explain this.
3. **The running-time unit is not credible.** The caption says seconds, but the values reach ~240,000. The true unit is UNVERIFIED.
4. **One synthetic scenario.** I found no repetitions, seeds or spread in §4.4.
5. **The prediction is an oracle-like subset** of the real requests at 25% "accuracy".

### 1.9 What contribution this example shows (structure)
- **(a) Re-implementation** of two published algorithm families (Tong et al. 2018 and 2022) inside one pipeline.
- **(b) One small new variant** (Prune Prophet: binary-search pruning, greedy, faster, slightly worse served count than Prophet at 150 and 200 requests).
- **(c) A working system:** use cases, database, REST API (e.g. "/insert/prune-prophet", txt l.1921-1924) and an admin web UI (§4.5-4.6, PDF p.49-54).
- **(d) A small synthetic comparison** on four operator-side metrics. There is no rider-side metric (no waiting time, lateness or reliability).
- **Assessment:** the bar it sets is "system + an existing algorithm + one modification + experiments on one component with a visible trade-off". It does not set a bar of methodological novelty.

### 1.10 Patterns that transfer to RideBound (honest)
1. **Same pipeline, one component swapped, frontier figures.** Swap one decision rule inside the same simulator and plot the operator metrics against the rider metric. RideBound already has this shape: U / C-30…C-300 / M+ / V on the same runner, with served, shared and drop-exposed share and late>1 min (fact pack l.47-48, l.73-77).
   - The thesis's Fig 4.5-4.8 format (x = load, y = metric, one line per algorithm) can be reused directly, with "budget B" or "load" as the x-axis.
2. **"Optimize one component" can mean the insertion/assignment step under the rule C budget.**
   - Under C-30, 148 requests are blocked only by a co-rider's budget, and the median overshoot is 110 s (fact pack l.51-53).
   - A budget-aware insertion is an "optimize one pipeline step" contribution of exactly this kind. It would try alternative positions or vehicles before rejecting, or choose among feasible insertions the one with the least dispatch change c to co-riders.
   - The screening already done points the same way: a budget proportional to direct trip time unblocks 11→30 at 60 s and 59→89 at 120 s, first-order (fact pack l.52-53). That is a candidate "budget-allocation policy" component.
   - Either option is T2 (core code change) unless done as an offline re-analysis.
3. **Copy its trade-off framing, not its evidence level.** Prune Prophet buys speed with optimality; RideBound's C buys reliability with served riders (−96 riders, 3.9% of U served; fact pack l.39-41).
   - RideBound's evidence is already stronger than the example: measured traffic, 34 cells, sealed ML pilot.
   - The example uses one synthetic scenario and simulated predictions.
4. **Add the example's operator metrics where they are missing:** vehicles used, cost (VKT) per served rider, and compute time per decision.
   - The repo history contains a commit "Add CandidateHotPathBenchmark project" (git log). Whether it measures what is needed is UNVERIFIED, because I did not open it.
5. **Do not copy:**
   - an "ML" claim backed by simulated predictions;
   - text numbers that contradict the figures;
   - an unexplained gap between two variants that should be equivalent.

## 2. FIELBAUM20: Fielbaum & Alonso-Mora (2020), unreliability in ridesharing (the most important prior work)

**Identity**
- Title: *Unreliability in ridesharing systems: Measuring changes in users' times due to new requests* [FIELBAUM20:8] "Unreliability in ridesharing systems: Measuring changes in users'".
- Authors: Andrés Fielbaum and Javier Alonso-Mora (TU Delft).
- Venue: [FIELBAUM20:1] "Transportation Research Part C 121 (2020) 102831".
- DOI: [FIELBAUM20:51] "https://doi.org/10.1016/j.trc.2020.102831".
- Partly funded by Didi [FIELBAUM20:1052] "This research was partially funded by Didi Udian Technology".

I read sections 2, 3, 6 and 7 myself, and the claude-side reader A read the full paper. Tables 2 and 5 were checked visually on PDF pages 10 and 17.

**What it says (O2/O3/O6)**
- **O6 / novelty: it already measures operator-caused change in a rider's times against the first announcement.**
  - [FIELBAUM20:93] "We study how the predicted times for each single request change from its first";
  - [FIELBAUM20:94] "assignment until the drop-off, and also how different realizations of the same request obtain different results.".
  - It focuses on operator-induced changes: [FIELBAUM20:191] "Definition 2. (Unreliability induced by the operators) Each time the system receives a new request, it changes how it gathers several"; [FIELBAUM20:218] "In this paper, we focus on the unreliability induced by the".
  - Only increases are counted: [FIELBAUM20:295] "In the remainder of the paper we consider the positive values for these indices, and truncate to zero those".
- **Traffic is deliberately excluded,** by choosing a period with stable travel times. This is the gap that RideBound's v/e/p ledger fills.
  - [FIELBAUM20:574] "congestion is not a very relevant problem, i.e., traveling times are somewhat stable, which allows us to disregard unreliability due to";
  - [FIELBAUM20:575] "traffic conditions, isolating the effects we are aiming to study in this paper.".
- **O6: it already tests freeze/commit rules and measures the trade-off.**
  - The rule: [FIELBAUM20:957] "Fully controlled scenario:When a passenger gets assigned to a vehicle, it is marked as non-rejectable for future assignments, and her" / [FIELBAUM20:958] "maximum waiting time is updated to the predicted one.".
  - The result: [FIELBAUM20:975] "The most relevant impact, however, is on the rejection rate, which increases dramatically due to the inflexible conditions."; [FIELBAUM20:984] "the more controlled the unreliability, the higher the average users' costs."
  - Freezing total delay is judged unworkable: [FIELBAUM20:1004] "if in-vehicle detours are not admitted, actual sharing would occur only at very specific circumstances," / [FIELBAUM20:1006] "means would turn the whole system in a (almost) non-shared one.".
- **The open problem it names is exactly the gap rule C addresses:**
  - [FIELBAUM20:1038] "There is plenty of room for future research regarding unreliability in ridesharing systems. The most relevant one is how to control it,";
  - [FIELBAUM20:1039] "i.e., studying how to alter the assignment procedures to provide more accurate times without increasing the rejection rate or pas";
  - [FIELBAUM20:688] "to provide better predictions or to make these changes less frequent is crucial for these systems.".
- **O3, asserted rather than measured:** [FIELBAUM20:87] "However, from the point of view of p1, this sudden change might be quite disturbing, a"; [FIELBAUM20:961] "Becoming rejected after being accepted might be more annoying than facing an extra waiting time.".
- **O2, a secondary citation:** [FIELBAUM20:136] "by Bansal et al. (2019), who estimate that demand could be increased by about 10% if waiting times could be better predicted.".

**Numbers**
- **Setup:**
  - [FIELBAUM20:583] "The basic scenario considers 2000 vehicles capable of carrying 4 passengers at a time";
  - [FIELBAUM20:584] "requests that have more than 4 passengers leaves a total of 19610 requests for the two hours period.";
  - [FIELBAUM20:1067] "Max. admissible waiting time 5 [min]";
  - [FIELBAUM20:1068] "Max. admissible delay 10 [min]".
- **Table 2, base scenario** (PDF p.10, checked visually):
  - 36.1% of first-accepted requests face a change [FIELBAUM20:626] "First-accepted requests that face changes 36.1% 52.6% 33.3% 41.2% 34.7% 32.8%".
  - 6.85% become rejected after acceptance [FIELBAUM20:622] "Requests that become rejected 6.85% 10.7% 5.25% 6.3% 4.83% 1.14%".
  - When the delay increases, it increases by 1.68 min on average (PDF p.10).
  - [FIELBAUM20:665] "average passenger faces 0.35 changes on the predictions, but the maximum number of changes is 6".
- **Table 5** (PDF p.17, checked visually):

  | Scenario | Waiting (min) | Detour (min) | Delay (min) | Rejected | Users' cost |
  |---|---|---|---|---|---|
  | Base | 1.01 | 0.65 | 1.66 | 34.5% | 9.56 |
  | Intermediate (accepted riders cannot be rejected, but their waiting time may grow) | 1.51 | 1.01 | 2.52 | 31.2% | 10.3 |
  | Fully controlled (no rejection, and waiting capped at the first prediction) | 0.77 | 0.94 | 1.71 | 45.6% | 11.6 |

  - Base row: [FIELBAUM20:942] "Base 1.01 0.65 1.66 34.5% 9.56". The other rows are mislabelled in the txt.
  - So freezing the pickup promise costs +11.1 pp of rejections (my arithmetic). The setting is 2000 vehicles in Manhattan, so this is not comparable to RideBound's numbers.

**Relation to RideBound.** This is **prior work that limits novelty, and also the strongest motivation.**
- **Prior work for:** measuring change against the first announcement, operator-induced versus other causes, freeze/commit rules, and the stability–service trade-off.
- **Not in the paper:**
  - a cumulative per-rider budget B on the absolute size of dispatch-caused revisions of the drop-off promise (it only tests "no change" or "no rejection");
  - a dispatch/traffic split under time-varying speeds (traffic is excluded by design);
  - a forecast first promise (it says better first announcements are an open challenge [FIELBAUM20:392] "Moreover, proposing better first-announcements (predictions) is a very complex challenge, as they depend on each").
- **Claim-boundary note.** `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md:56` already says not to claim "phát hiện unreliability, kiểm soát trước quyết định hoặc đánh đổi dịch vụ–ổn định" as new. The copy named in the fact pack (`C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md:56`) has only the weaker "Không claim việc phát hiện unreliability là mới." The stronger wording should be used.
- The fact pack's NOT-claimable list (l.58-63) does not name this paper explicitly.


## 3. SCHULZ26: Schulz & Pfeiffer (2026), the closest prior work to rule C on promises

**Identity**
- Title: *Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem* [SCHULZ26:6] "Efficient insertion and reoptimization algorithms for a".
- Authors: Arne Schulz and Christian Pfeiffer.
- Venue: [SCHULZ26:1] "OR Spectrum (2026) 48:541-586".
- DOI: [SCHULZ26:2] "https://doi.org/10.1007/s00291-026-00847-0".

**What it says (O2/O3/O6)**
- **The promise.** The offer contains a scheduled drop-off time and a latest drop-off time. Both are communicated to the rider:
  - [SCHULZ26:570] "Thus, the offer contains the scheduled arrival time Bi- as well as";
  - [SCHULZ26:575] "Only Bi- and li- are communicated to the".
- **The bound after acceptance** is a fixed deadline set at acceptance, l after the offered time:
  - [SCHULZ26:469] "to a later point in time by l. We calculate li- = Bi- + l";
  - [SCHULZ26:470] "directly after customer i accepted our offer."
  - The scheduled time may still slip because of later insertions: [SCHULZ26:487] "After acceptance the customer can be delayed because of".
  - So this is a one-sided bound on the net slip versus the first offer. It is not a cumulative budget on absolute revisions, and the paper does not separate dispatch from traffic.
- **No traffic in the model.** Travel times are fixed: [SCHULZ26:640] "Thus, visited locations in the tour as well as travel times". Every post-acceptance shift is therefore dispatch-caused.
- **O2/O3: why stable offers matter** (cited, not measured):
  - [SCHULZ26:308] "the customer can rely on the offer and knows its conditions upfront";
  - [SCHULZ26:309] "as unexpected delays are rated more negatively (Gerzinic et al. 2023)".
  - No rejection after booking, because [SCHULZ26:479] "who found that a canceled service after booking results in".
- **O6: the measured trade-off** between the allowance and rejection is exactly RideBound's B-versus-served-riders question:
  - [SCHULZ26:1494] "small maximum time shift leads to significantly higher rejection rates while a larger";
  - [SCHULZ26:1495] "maximum time shift makes the system unattractive for accepted customers."
- **O3: rider acceptance is an assumed model, not data.**
  - Acceptance is e^(−β·RD), with RD = relative detour [SCHULZ26:450] "RD = Bi- - ei+ - ti".
  - The parameter was tuned informally: [SCHULZ26:1198] "In preliminary tests, a factor of 0.5 was reasonable such that not too many customers".

**Numbers**
- **Default allowance.** l = 900 s [SCHULZ26:1204] "is set to 900 s (15 min), which is also done this".
- **Sweep of l over 0–30 min** [SCHULZ26:1470] "between 0, 5, 10, 15, 20, 25, and 30 min (with 15 being the value we used for all".
- **Fig. 7, read visually on PDF p.29** (approximate). Average rejected fraction: l=0 ≈0.45; l=5 ≈0.41; l=10 ≈0.39; l=15 ≈0.39; l=30 ≈0.385.
  - Text: [SCHULZ26:1484] "for a maximum time shift of 30 min the average fraction of rejected customers does".
  - **Reading:** freezing the drop-off time completely (l=0) costs about 6 pp more rejections than a 15-min allowance, in their setting.
- **Table 2, PDF p.27** (checked visually). "Delay" is defined on PDF p.28 as how much an accepted customer's final delivery time is delayed compared to the original offered delivery time. Values: CB0 181.71 s; CB1 279.87 s; C0.5_120 273.20 s.
  - Raw line: [SCHULZ26:1377] "561.00 459.23 390.51 380.99 181.71".
  - Text: [SCHULZ26:1449] "tomer has to wait roughly three minutes longer until reaching their delivery location".
- **Table 7, PDF p.42** (checked visually). Rejection: C0.5_60 38.78%; C0.5_120 38.81%; CB1 38.92%; CB0 39.92%.
  - So reinsertion is worth about 1 pp, and the "potential" about 0.1 pp more (my arithmetic).
  - [SCHULZ26:2117] "0.5 60 38.78".
- **Scale.** 2700 instances [SCHULZ26:1215] "so that we effectively end up with a test set of 2700 instances."; 120 stops in Hamburg [SCHULZ26:1177] "There are 120 stops in total.".

**Relation to RideBound.** This is **prior work that limits novelty**. A per-rider, communicated bound on dispatch-caused slip of the drop-off time after acceptance already exists here (15 min, net, one-sided), together with an allowance-versus-rejection curve.
- What it does not have:
  - a cumulative, two-sided budget on absolute revisions of the published time (|c| summed);
  - a dispatch/traffic split under time-varying speeds;
  - a 30-s scale;
  - a forecast quote;
  - a per-rider ledger.
- It is also the natural external comparator for RideBound's B sweep. Their average post-acceptance slip is ~3–4.7 min with l = 15 min. RideBound's C-30 caps the cumulative dispatch change at 30 s.


## 4. ALONSO20: Alonso-González et al. (2020), VOT and VOR for urban pooled on-demand services

**Identity**
- Title: *Value of time and reliability for urban pooled on-demand services* [ALONSO20:8] "Value of time and reliability for urban pooled on-demand services".
- Authors: María J. Alonso-González, Niels van Oort, Oded Cats, Sascha Hoogendoorn-Lanser, Serge Hoogendoorn (TU Delft and KiM).
- Venue: [ALONSO20:1] "Transportation Research Part C 115 (2020) 102621". DOI 10.1016/j.trc.2020.102621 [ALONSO20:54].
- The currency sign is lost in the txt; it is € on PDF p.9 (checked visually).

**What it says (mainly O3)**
- **The first VOR study for pooled on-demand services.** Reliability is valued at about half of time:
  - [ALONSO20:29] "VOR to be lower than VOT: the reliability ratio (VOR/VOT ratio) for both the waiting stage and";
  - [ALONSO20:30] "the in-vehicle stage being around 0.5.".
- **Definition.** It measures spread (standard deviation) plus "displacement", the deviation from the announced time:
  - [ALONSO20:167] "we do not only consider variability as a source of unreliability, but also the deviation of the real (to be experienced)";
  - [ALONSO20:168] "waiting/in-vehicle time from the expected (announced) waiting/in-vehicle time.";
  - [ALONSO20:282] "function as the difference between the mean of the new distribution and the expected time announced in the scenario.".
  - Displacement is the closest stated-preference construct to RideBound's "actual minus first promise". It is shown before the trip and is not revised during it.
- **The key caution: small unannounced systematic delay is weighted less than announced time.**
  - [ALONSO20:641] "the distribution (ranging between 2.06 /h and 6.69 /h), and always lower than the corresponding VOT.";
  - [ALONSO20:642] "of a (small) unannounced yet systematic additional time in the utility function is lesser than that of the announced times.".
  - The authors call this "counterintuitive": [ALONSO20:643] "this seems counterintuitive and contrary to findings from previous research".
  - They also say real lateness may be valued more: [ALONSO20:979] "individual, when presented with an unexpected situation, the VOR may be higher than found in this study to avoid lateness.".
  - And the ratio should rise with experience: [ALONSO20:983] "values of reliability and values of times can be expected to somewhat increase with familiarity of these services.".
- **Lateness was not framed as lateness.** No desired arrival time was given: [ALONSO20:872] "indicated. As a result, individuals are not presented with a situation of lateness.".
- **O2, secondary citations on availability and rejection:**
  - [ALONSO20:1002] "Unguaranteed availability plays a key role in the probability of subscribing to shared mobility alternatives";
  - [ALONSO20:1005] "using the pooled on-demand service Kutsuplus (Helsinki, Finland)", following [ALONSO20:1004] "vehicle unavailability was a decisive reason for individuals of the higher income groups to stop".
- **O2: service tiers by reliability** (proposed, not tested) [ALONSO20:864] "the option to book a service with higher uncertainty and larger detours for a"; [ALONSO20:866] "Offering different services to cater for heterogeneity in preferences can additionally increase patronage".
- **O6: pooled services have no timetable, so the promise is the reference** [ALONSO20:1054] "their flexibility and the lack of clear reference values such as timetables.".

**Numbers** (Tables 4–5 checked visually on PDF p.9; values in €/h)
- Sample: [ALONSO20:25] "(N = 1006), and address commuting and leisure trips.". Netherlands, May 2018, stated preference only.
- In-vehicle VOT: [ALONSO20:452] "commuting (10.80 /h) and leisure purposes (7.88-9.94 /h)".
- Waiting VOT: [ALONSO20:523] "We find the VOT for the waiting stage to be in the range of 9.27-16.50 /h".
- In-vehicle VOR (standard deviation): 3.15 (leisure) and 5.76 (commuting).
- In-vehicle VOR (displacement): 2.06 / 4.41 (leisure, non-working / working) and 4.41 (commuting) (PDF p.9).
  - [ALONSO20:515] "VOR in-vehicle displacement (working individuals) 4.41".
- Waiting VOR: [ALONSO20:608] "the range of VOR found is a bit more spread out, 2.24-8.58 /h, with RR values ranging between 0.2".
- Literature range: [ALONSO20:607] "different studies worldwide reported a wide range of RR values, ranging from 0.1 to 2.5".
- **Displacement-to-VOT ratios (my arithmetic):**
  - in-vehicle commuting 4.41/10.80 ≈ 0.41;
  - leisure 2.06/7.88 ≈ 0.26 and 4.41/9.94 ≈ 0.44.
- **Levels shown to respondents:** 0/1/2 min (waiting) and 0/1/3 or 0/2/4 min (in-vehicle). This is reader A's visual check on PDF p.16; I did not re-check it.

**Relation to RideBound.**
- **Supports O3:** pooled riders do value reliability, at about half of VOT. This gives €/h values to monetise minutes.
- **Cautions the forecast promise.** Under this model (my inference, not stated by the authors), padding the quoted time costs more utility than the small unannounced lateness it removes. So "longer but reliable quotes" is not automatically a rider gain.
- RideBound's forecast adds only 7.4–13.7 s (fact pack l.45). That is small, but the direction of this evidence should be stated honestly.
- **Does not limit novelty.**

## 5. WARDMAN26: Wardman et al. (2026), meta-analysis of time multipliers (incl. lateness and reliability)

**Identity**
- Title: *Value of time multipliers for walk time, wait time, service headway, displacement time, reliability and congested travel time: review and meta-analysis of worldwide evidence* [WARDMAN26:8] "Value of time multipliers for walk time, wait time, service".
- Authors: [WARDMAN26:12] "Mark Wardman a,*, Paul Murphy a, Manuel Ojeda-Cabral a, Alex Mitrani b,", plus Kazuyuki Neki and Richard Martin Humphreys.
- Venue: [WARDMAN26:1] "Transportation Research Part A 207 (2026) 104925".
- DOI: [WARDMAN26:51] "https://doi.org/10.1016/j.tra.2026.104925".

**What it says**
- **O3: lateness against the expected or timetabled arrival is the most heavily weighted time component.**
  - [WARDMAN26:1364] "Late arrival time is particularly highly valued with headway and displacement time having multipliers less than one";
  - [WARDMAN26:656] "has amongst the highest multipliers, reflecting the strong dislike of lateness".
- **Definition close to RideBound's metric** [WARDMAN26:167] "Mean late arrival time at the destination relative to timetable or expected arrival time".
- **Reliability as spread** (reliability ratio) is a different measure [WARDMAN26:176] "The standard deviation of travel time, where the time multiplier is commonly referred to as the reliability ratio (RR).".
- **O6: official practice links the promise form to the metric** [WARDMAN26:247] "for the RR to be used for unscheduled modes and late time (LT) for scheduled modes.".
  - My inference: a published drop-off promise makes a pooled ride "scheduled", so late-time multipliers become the relevant ones.
- **Robustness claim** [WARDMAN26:1287] "multipliers are large and that it cannot be argued that they are large simply because they are based on SP evidence.".
- **Context.** RR fell after 2010 [WARDMAN26:1187] "As for RR, it was found to be 33.8% lower post 2010 (RR_2011+),". This is presumed due to real-time information and acceptance [WARDMAN26:1372] "The reduction in the reliability ratio over time presumably stems from greater acceptance of unreliability".

**Numbers** (multipliers relative to in-vehicle time; Table 5 on PDF p.10, Table 8 on PDF p.19 checked visually)
- Coverage: [WARDMAN26:26] "The evidence assembled covers 2872 multipliers drawn from" / [WARDMAN26:27] "606 studies across 52 countries over the years 1963 to 2023.".
- Late time:
  - MeanLate-X/Y [WARDMAN26:617] "MeanLate-X/Y 3.12 0.233 2.65-3.59 66 27 2.47";
  - MeanLate-Distn [WARDMAN26:615] "2.53 0.133 2.26-2.80 15 2 2.51" (label on l.614; only 15 observations).
- Schedule delay late: [WARDMAN26:625] "SDL-withoutRR 2.23 0.147 1.94-2.52 42 22 2.20".
- RR: [WARDMAN26:619] "RR-withoutSDE/L 0.93 0.065 0.80-1.06 149 39 0.61". Recommended [WARDMAN26:1349] "A range between 0.6 and 0.9 would seem more appropriate".
- Wait [WARDMAN26:591] "Wait 1.72 0.038 1.64-1.80 408 185 1.53". Heavy congestion [WARDMAN26:607] "Cong-hvy 2.09 0.133 1.82-2.36 69 19 1.73".
- Official guidance [WARDMAN26:248] "range 2.5 to 3.5 but, surprisingly, with larger valuations when there is lateness at the departure.".
- **Table 8, implied late-time multipliers** (PDF p.19):
  - Car/Other urban: 2.61 (stated preference) and 3.04 (revealed preference). "Other" includes taxi [WARDMAN26:1345] "Other covers the primary modes of ferry, motorcycle and taxi.".
  - Raw row: [WARDMAN26:1335] "2.53 3.50 2.81 3.04 2.44 3.01 2.41 2.61".
- **Limits:**
  - mostly stated preference [WARDMAN26:433] "RP data provided 12% of the values, with 5% from joint RP-SP models and the remaining 83% from some form of SP exercise.";
  - taxi is rare and pooling absent [WARDMAN26:862] "Taxi (25)".

**Relation to RideBound.**
- **Strong O3 support for measuring lateness against the promise.** One minute late is worth about 2.5–3.1 in-vehicle minutes, while one minute of standard deviation is worth about 0.6–0.9.
- **It conflicts with ALONSO20's displacement result.** Report both. The two plausible reasons are:
  - "displacement" there is small, pre-announced and unframed as lateness;
  - Wardman's late time is framed against a timetable or expected arrival.
- **Does not limit novelty.**
- **Illustrative cross-source arithmetic** (not a finding): a pooled commuter VOT of 10.80 €/h × late multiplier 2.5 ≈ 27 €/h ≈ 0.45 € per minute late.

## 6. AZADEH22: Sharif Azadeh et al. (2022), choice-driven DARP

**Identity**
- Title: *Choice-driven dial-a-ride problem for demand responsive mobility service* [AZADEH22:8] "Choice-driven dial-a-ride problem for demand responsive mobility".
- Authors: Sh. Sharif Azadeh, Bilge Atasoy, Moshe E. Ben-Akiva, M. Bierlaire, M.Y. Maknoon [AZADEH22:12] "Sh. Sharif Azadeh a,c,d, Bilge Atasoy b,c, Moshe E. Ben-Akiva c, M. Bierlaire d,".
- Venue: [AZADEH22:1] "Transportation Research Part B 161 (2022) 128-149".
- DOI: [AZADEH22:60] "https://doi.org/10.1016/j.trb.2022.04.008".

**What it says**
- **O6: a different form of promise.** It offers a priced menu (taxi or shared × delayed-pickup windows) instead of one quoted time [AZADEH22:88] "a menu of personalized alternatives is offered to the customer at different price levels to maximize". The objective is profit [AZADEH22:31] "Our problem extends the dynamic DARP by (i) changing its objective function to profit".
- **What is promised.** A confirmed pickup window plus a maximum ride time. Existing riders are protected by a hard ride-time guarantee, not by a budget on changes:
  - [AZADEH22:226] "confirmed pickup time window and the maximum ride-time";
  - [AZADEH22:255] "the maximum ride-time of the existing requests is considered in the CD-DARP model while revising the routes".
- **O2: realised versus promised quality has long-term consequences** (stated, not measured):
  - [AZADEH22:352] "This approach may have long-term repercussions on user choices due to the fact";
  - [AZADEH22:353] "that it is independent from the realized value of waiting time and the maximum ride time."
- **O2/O6: managerial lesson.**
  - [AZADEH22:1648] "When an operator offers only the most profitable alternatives, that will affect";
  - [AZADEH22:1649] "the customer satisfaction and service levels";
  - [AZADEH22:1650] "introducing flexible time windows (even if they are defined within a tight range) helps to save cost of routing."
- **O3: assumed rider tolerance** [AZADEH22:1295] "customers can wait up to nine minutes and arrive shortly before their preferred pickup time".

**Numbers**
- **NYC, Table 14, PDF p.20 (checked visually):**

  | Scenario | Served | Profit | Customer rejection |
  |---|---|---|---|
  | I: one alternative, no re-routing | 41.68% | 436.38 | 58.12% |
  | II: menu | 74.36% | 654.93 | 17.38% |
  | III: menu + re-routing | 76.36% | 705.13 | 15.32% |

  - Text: [AZADEH22:1608] "it can only serve 41.68%".
- **Flexible windows versus dynamic DARP, captive customers, 2 taxis:** [AZADEH22:1552] "for our test with two vehicles, there is a 7.22%" / [AZADEH22:1553] "increase in the number of customers served".
- **Trip-based versus flat pricing:**
  - [AZADEH22:1576] "The percentage of customers rejecting all offered alternatives reduces on average from 14.7% to 6.41%";
  - [AZADEH22:1577] "average profit improvement is around 9%".
- **Choice coefficients** (Table 4, from Krueger et al. 2016): delay −0.06 / −0.10 and in-vehicle time −0.792 / −0.85 (taxi / shared) [AZADEH22:1087] "Delay () -0.06 -0.10"; [AZADEH22:1086] "In-vehicle time () -0.792 -0.85". The units are not printed, so no €/h value is derived.

**Relation.**
- **Prior work for "alternative promise form"** (menus of windows at prices) **and for "optimise the offer component jointly with insertion".** It is a template for an O6 direction "promise a window/price menu instead of a point time". That direction would be a new thesis, not an extension.
- **Not a rule C competitor.** There is no budget on post-booking changes, and speed is constant [AZADEH22:1096] "Vehicle speed 50 km/h".

## 7. RAUH25: Rauh et al. (2025), DARP in primary care with flexible scheduling

**Identity**
- Title: *The dial-a-ride problem in primary care with flexible scheduling*. The hyphens are lost in extraction: [RAUH25:6] "The dialaride problem in primary care with flexible".
- Authors: Felix Rauh, Emma Ahrens, Christina Büsing, Martin Comis, Felix Engelhardt.
- Venue: OR Spectrum. DOI: [RAUH25:2] "https://doi.org/10.1007/s00291-025-00812-3". Accepted 5 February 2025 [RAUH25:12].
- Volume and pages: not printed, UNVERIFIED.

**What it says**
- **O6: alternative promise form.** Only a range is promised at booking; the exact time is fixed later:
  - [RAUH25:24] "an appointment range is fixed a priori, and the exact time is determined when the";
  - [RAUH25:74] "range. Finally, the transportation provider fixes the vehicle routes a few days".
- **O2: fixed point promises are expensive** because they prevent bundling:
  - [RAUH25:63] "requests may be widely spread in time, which prevents an efficient pooling and";
  - [RAUH25:64] "ultimately implies high transportation cost."
  - And: [RAUH25:18] "nomic sustainability of such transportation systems based on ride sharing strongly".
- **O3: what the rider gets** [RAUH25:88] "patients, it offers a key benefit: guaranteed transportation to and from appointments,". There is no cancellation after acceptance [RAUH25:111] "Once a transportation request has been accepted, it must be serviced entirely, i.e.,".
- **O6: freezing.** Online insertions may not change the already-executed part [RAUH25:424] "must remain the same for all stops before i.".
- **O6 caveat: the promise form pays only with a tailored algorithm.** [RAUH25:769] "In fact, GIHflex cannot even outperform its non-flexible".

**Numbers**
- **Rural, served requests.** MCLIH 230.1 versus GIH_TW 166.35 [RAUH25:754] "(mean: 230.1, median: 231), whereas GIHTW serves in excess of 60 requests fewer"; [RAUH25:763] "about 38% more requests can be served".
- **Served requests relative to GIH_TW:**
  - rural 1.38 [RAUH25:781] "Total Requests Served rural 1.0 0.89 1.38";
  - semi-urban 1.16 [RAUH25:782];
  - urban 1.19 [RAUH25:783].
- **Rider cost of the flexibility.** Average detour rises from 9.1% to 11.7% [RAUH25:840] "patients experience an average detour of 9.1% under"; [RAUH25:841] "rises to 11.7% with the flexible setting of MCLIH".
- **Authors' own caveat** [RAUH25:929] "Consequently, the reported 38% increase in ride".

**Relation.** **Supporting analogue for O6 ("promise a different kind of thing").** It shows that the form of the promise buys capacity: +16–38% served for about +2.6 pp detour (rural, my arithmetic). There are no real-time revisions, no traffic and no ledger, so it does not affect rule C's novelty.

## 8. MOLENBRUCH15: Molenbruch, Braekers & Caris, CEJOR (2015)

**Identity**
- Title: *Operational effects of service level variations for the dial-a-ride problem* [MOLENBRUCH15:1] "Operational effects of service level".
- Authors: Yves Molenbruch, Kris Braekers, An Caris.
- Venue: Central European Journal of Operations Research. DOI [MOLENBRUCH15:11] "DOI 10.1007/s10100-015-0422-7"; 2015 [MOLENBRUCH15:45].
- Volume and pages: not printed in this e-offprint, UNVERIFIED.

**What it says**
- **O6: a *price of service quality* study.** 78 service-level combinations [MOLENBRUCH15:52] "for 78 combinations of two service level parameters, being the maximum":
  - 13 settings of the time-window deviation, 0–60 min [MOLENBRUCH15:222];
  - 6 settings of ride-time excess, 0–100% [MOLENBRUCH15:223].
- **Diminishing returns** [MOLENBRUCH15:407] "This indicates that the marginal benefits of consecutive reductions in the quality".
- **O3: riders get a worse service while savings flatten** [MOLENBRUCH15:455] "poor, the ratio between marginal user inconvenience and marginal operational savings". Only about half of the allowed slack is actually used [MOLENBRUCH15:457] "approximately half of the deviation allowed.".
- **O2/O3: the gap it leaves open.** These are exactly the business questions the owner asks:
  - [MOLENBRUCH15:915] "providers should wonder about the elasticity of user behavior. What user losses or";
  - [MOLENBRUCH15:917] "the effect on willingness to pay?".
- **O2: service-level-differentiated pricing** [MOLENBRUCH15:938] "companies might be able to operationalize a system in which rates are differentiated".
- **Scope limit:** static and deterministic [MOLENBRUCH15:890] "assuming that solutions are equally reliable. This implies that conclusions should only".

**Numbers** (rural, Table 4). The rows were re-paired by agent B and checked by me with cost = 0.30·km + 200·fleet:
- (0,0): €2476.06, fleet 11.14 [MOLENBRUCH15:825] "(0, 0.0) e2476.06 - 11.14 826.87 0.00 0.00".
- (15,0.4): €2061.14, fleet 9.12 [MOLENBRUCH15:826] "(15, 0.4) e2061.14 9.12 790.45 7.87 0.02".
- (60,1.0): €1280.34, fleet 5.47 [MOLENBRUCH15:830] "(60, 1.0) e1280.34 e939.68 5.47 621.14 28.72 0.35".
- That is −16.8% and −48.3% cost (my arithmetic).
- Average distance over the 78 scenarios ≈90.21% of baseline [MOLENBRUCH15:540] "corresponding baseline scenario, compared to an average of 90.21 % for the global".
- Fleet size is unconstrained [MOLENBRUCH15:331] "In addition, constraints on fleet". So the cost of quality shows up as cost and fleet, not as rejected riders.

**Relation.** **Framing support.** It is the operator-side mirror of "rule C costs ~4% of U's served riders": a quantified price of tighter service, with diminishing returns. It has no promises, no revisions and no traffic.

## 9. FIELBAUM-SCALE: Fielbaum, Tirachini & Alonso-Mora, scale analysis for ODRP

**Identity**
- Title: *Scale analysis for on-demand ridepooling systems and comparison with public transport* [FIELBAUM-SCALE:1] "Scale analysis for on-demand ridepooling systems and".
- Authors: Andrés Fielbaum, Alejandro Tirachini, Javier Alonso-Mora [FIELBAUM-SCALE:4].
- **Venue, year and DOI are not printed in the PDF** (agent C grep-checked); UNVERIFIED.

**What it says**
- **O2: pooling gains accrue to the operator, while delays fall on users.**
  - [FIELBAUM-SCALE:727] "This implies that the sources of scale diseconomies that we identified for the";
  - [FIELBAUM-SCALE:728] "users, get outweighed by the sources of scale economies for the operators".
- **O2: more load means more unreliability.**
  - [FIELBAUM-SCALE:617] "Both types of unreliability worsen when vehicles are more loaded";
  - [FIELBAUM-SCALE:618] "Flex-route Effect increases unreliability. It is worth mentioning that this is not a minor issue".
- **Novelty limit: assignment cost already prices the harm to riders already on board** [FIELBAUM-SCALE:279] "the extra costs induced to the users that were being served by the vehicle prior to this".
- **O3: reliability is valued at about half the VOT** (secondary citation; the primary source is ALONSO20) [FIELBAUM-SCALE:620] "to be approximately a half of the value of time.".
- **O3: bounds stand in for acceptance** [FIELBAUM-SCALE:556] "Such bounds ensure that users will indeed accept the assignment proposed by the system".

**Numbers**
- User time values (Santiago-based):
  - in-vehicle 2.32 US$/h [FIELBAUM-SCALE:1418] "Monetary equivalent cost of one time unit spent by a user in-vehicle. 2.32 [US$/h]";
  - waiting 4.64 US$/h [FIELBAUM-SCALE:1420] "Monetary equivalent cost of one time unit spent by a user waiting. 4.64 [US$/h]".
- Zero rejections are imposed by design [FIELBAUM-SCALE:351] "we must have zero rejections.".

**Relation.** **Support for O2 framing** (users carry the cost of pooling, including unreliability), plus a **novelty limit**: insertion cost that accounts for existing riders is prior work. It has no traffic.

## 10. KOVACS14: Kovacs, Golden, Hartl & Parragh (2014), consistency in vehicle routing (survey)

**Identity**
- Title: *Vehicle Routing Problems in Which Consistency Considerations are Important: A Survey* [KOVACS14:1] "Vehicle Routing Problems in Which Consistency" / [KOVACS14:2] "Considerations are Important: A Survey".
- Authors: Attila A. Kovacs, Bruce L. Golden, Richard F. Hartl, Sophie N. Parragh.
- Venue: [KOVACS14:37] "NETWORKS, Vol. 64(3), 192-213 2014".
- DOI: [KOVACS14:47] "DOI 10.1002/net.21565".

**What it says**
- **O3: what customers want** is regular times and the same driver:
  - [KOVACS14:17] "service at regular times of the day provided by the";
  - [KOVACS14:89] "quently) want to be served by the same familiar person at".
  - Paratransit clients: [KOVACS14:135] "are particularly sensitive to changes in their daily routines.".
- **O2: the business chain is asserted, not quantified.**
  - [KOVACS14:60] "mostly driven by customer loyalty. Loyal customers generate";
  - [KOVACS14:61] "recurring revenues. So, the longer a customer stays with a";
  - [KOVACS14:145] "larger routing cost due to a focus on consistency is more than"; [KOVACS14:146] "offset by higher customer satisfaction and increased driver".
  - The survey itself says the benefit must still be quantified: [KOVACS14:93] "have to quantify the cost and benefit of this customer-first".
- **Definitions: arrival-time consistency** is across days, for the same customer. It is the maximum arrival-time difference [KOVACS14:508] "L. The maximum arrival time difference lmax is the largest". It is not a revision of a promise within one trip.
- **O6: hard versus soft constraints.**
  - [KOVACS14:491] "while excessively tight constraints lead to a disproportional";
  - [KOVACS14:521] "however, may lead to infeasible or unreasonable solutions".
- **Forecast lineage** (future work): [KOVACS14:936] "antee stable arrival times at the customer locations despite"; [KOVACS14:937] "unforeseeable events such as traffic jams.".

**Numbers (costs of consistency)**
- ConVRP: [KOVACS14:596] "cost between 6.6% and 15%".
- Feillet et al.: [KOVACS14:599] "1% and 5.9%.".
- Over-tight bound: [KOVACS14:635] "VRP, a 60% tighter constraint on the maximum arrival time" / [KOVACS14:636] "difference increases travel cost by up to 186.16%.".

**Relation.** **Prior work that limits the words "time consistency"; conceptual lineage, not anticipation.** Its consistency is across repeated visits. Rule C bounds within-trip revisions of a published time. It supports O3 (customers value regular, unchanged times) and O2 (a cost of 1–15% for consistency, asserted to be offset by loyalty).

## 11. SRIDHARAN87: Sridharan, Berry & Udayabhanu (1987), freezing the MPS

**Identity**
- Title: *FREEZING THE MASTER PRODUCTION SCHEDULE UNDER ROLLING PLANNING HORIZONS* [SRIDHARAN87:6] "FREEZING THE MASTER PRODUCTION SCHEDULE UNDER" / [SRIDHARAN87:7] "ROLLING PLANNING HORIZONS".
- Authors: [SRIDHARAN87:9] "V. SRIDHARAN, WILLIAM L. BERRY AND V. UDAYABHANU".
- Venue: [SRIDHARAN87:1] "MANAGEMENT SCIENCE"; [SRIDHARAN87:2] "Vol. 33, No 9. September 1987". Pages 1137–1149 [SRIDHARAN87:64].
- DOI: not printed.

**What it says**
- **O2: why stability is valuable.**
  - [SRIDHARAN87:36] "ules--a phenomenon referred to as nervousness. These changes can lead to increases in";
  - [SRIDHARAN87:37] "production and inventory costs, as well as a deterioration in customer service.".
- **O6: the trade-off is named; freezing is the control** [SRIDHARAN87:154] "the trade-off between production and inventory costs and schedule stability.".
- **Why freezing costs:** new information cannot be used.
  - [SRIDHARAN87:131] "Such cost increases occur because freezing forces additional lot-sizing alterna-";
  - [SRIDHARAN87:132] "These arise when new requirements information is added on to the".
- **Convex cost of freezing.**
  - [SRIDHARAN87:527] "becomes important only when the frozen portion of the planning horizon exceeds 50%,";
  - [SRIDHARAN87:528] "and that the cost of freezing increases rapidly beyond an F value of 0.8.".
- **Stability metric deferred** [SRIDHARAN87:705] "the measurement of nervousness".

**Numbers**
- Cost error, from its Figure 2 parameters: [SRIDHARAN87:530] "Here the cost error ranges from .026%" / [SRIDHARAN87:531] "when F equals 0.5 to 143.43% when F equals 1.0".
- Order-based freezing beats period-based above F = 0.5 [SRIDHARAN87:600] "based model exceeds that for the order based model when Fexceeds 0.5.".

**Relation.** **Conceptual lineage.** Rule C is a bounded-change relaxation between a full freeze (B = 0) and free replanning. The convex cost shape supports choosing a small but non-zero B. The setting is deterministic lot-sizing, so the numbers do not transfer. It does not anticipate a per-rider cumulative budget or a dispatch/traffic split.

## 12. HCRIDE25: Jiang, Yang & Wang (2025), HCRide

**Identity**
- Title: *HCRide: Harmonizing Passenger Fairness and Driver Preference for Human-Centered Ride-Hailing* [HCRIDE25:1] "HCRide: Harmonizing Passenger Fairness and Driver Preference for".
- Authors: Lin Jiang, Yu Yang, Guang Wang [HCRIDE25:4].
- arXiv: [HCRIDE25:10] "arXiv:2508.04811v1 [cs.LG] 6 Aug 2025". Venue note: [HCRIDE25:57] "Accepted to the IJCAI 2025 (Human-Centred AI Track).".

**What it says**
- **O6 pattern:** one component (dispatch), an objective plus an operator-set, human-centred constraint (a constrained MDP, with Lagrangian actor and two critics).
  - The threshold is like budget B: [HCRIDE25:411] "we set a predetermined violation rate of 15%"; [HCRIDE25:414] "rate can also be set to other values based on operators' goals.".
- **The constraint is aggregate, not per person,** which is the key contrast with rule C:
  - [HCRIDE25:229] "the cumulative reward and cost across all agents, rather than";
  - [HCRIDE25:230] "focusing on the outcomes of individual agents.".
- **O3:** [HCRIDE25:68] "There is strong demand among passengers for equitable" / [HCRIDE25:69] "waiting times, particularly relative to others in close spatial-".
- **There is no pooling.** It reports improvements over baselines and no frontier (agent C found no sensitivity sweep).

**Numbers**
- Headline: [HCRIDE25:95] "tively improves system efficiency by 1.77% and 2.02%,".
- These percentages are relative to the best baseline's remaining room: [HCRIDE25:357] "by 1.77% = (5.48% - 3.78%)/(100% - 3.78%)".
- Data: Shenzhen, 1.07 M orders and 1,200 vehicles [HCRIDE25:389]; NYC, 800 vehicles [HCRIDE25:391].

**Relation.** **Methodological template only.** It neither competes with rule C nor limits its novelty. Its lesson: report rule C as a frontier (B versus riders served versus late share), not as a single point.

## 13. BREGNI11: Bregni, D'Avino & Schiraldi (2011)

**Identity**
- [BREGNI11:41] "Bregni, A.; D'Avino, M. & Schiraldi, M. M.: A New Approach to Lower";
- [BREGNI11:42] "MRP Nervousness, Annals of DAAAM for 2011 & Proceedings of the 22nd";
- pages [BREGNI11:44] "9679, pp 1513-1514".

**What it says**
- It is a 2-page extended abstract about MRP nervousness, not MPS freezing.
- It names freezing only as an existing remedy that adds inflexibility [BREGNI11:75] "or capacity), introducing inflexibility to the system (i.e. fixed".
- Its one claim: nervousness exists even under stable demand [BREGNI11:94] "in the known literature is that nervousness is present even".
- No metric and no numbers.

**Relation.** **Largely irrelevant.** At most, a weak analogy: instability can be self-inflicted by the planner (dispatch-caused) even without external change (traffic).

## 14. Synthesis (14 bullets)

### O2: business and operator value of reliable or stable promises
1. **There is no direct revenue or retention measurement in any of the 13 PDFs.** The strongest owner-supplied O2 lines are secondary or asserted:
   - demand +~10% if waits were better predicted (Bansal 2019, cited) [FIELBAUM20:136] "who estimate that demand could be increased by about 10% if waiting times could be better predicted.";
   - unavailability drove higher-income riders away from Kutsuplus (cited) [ALONSO20:1004] "vehicle unavailability was a decisive reason for individuals of the higher income groups to stop";
   - unexpected delays rated worse, cancellation after booking gives significant disutility (Gerzinic 2023, cited) [SCHULZ26:309] "as unexpected delays are rated more negatively (Gerzinic et al. 2023)";
   - loyalty leads to recurring revenue, asserted [KOVACS14:61] "recurring revenues. So, the longer a customer stays with a".
   - Two papers state that the business value is still to be quantified: [KOVACS14:93] "have to quantify the cost and benefit of this customer-first" and [MOLENBRUCH15:917] "the effect on willingness to pay?".
   - The example thesis's revenue/return-rate sentence is unsourced (PDF p.9).
2. **Revealed design practice is itself O2 evidence: operators pay for promise stability.** Every dynamic pooling/DARP model here protects accepted riders.
   - SCHULZ26 fixes a deadline at acceptance [SCHULZ26:470] "directly after customer i accepted our offer." and never rejects after acceptance [SCHULZ26:474] "customers can never be rejected after acceptance".
   - AZADEH22 keeps the ride-time bound of existing riders [AZADEH22:255] "the maximum ride-time of the existing requests is considered".
   - RAUH25: [RAUH25:111] "Once a transportation request has been accepted, it must be serviced entirely".
   - FIELBAUM20 tests the same through "controlled" scenarios.
   - So the question is not whether to bound changes but **how large the bound is, what it covers, and what form it takes**. Rule C is a tighter (30 s), cumulative, dispatch-only version.
3. **The price of stability has the same shape everywhere, at very different sizes.** The settings are not comparable, so this is shape only.
   - FIELBAUM20: freezing the pickup promise raises rejections from 34.5% to 45.6% (Table 5, PDF p.17).
   - SCHULZ26: l = 0 gives about 6 pp more rejections than l = 15 min (Fig. 7, PDF p.29).
   - MOLENBRUCH15: (15 min, 0.4) costs 16.8% less than taxi-like service (my arithmetic, Table 4).
   - KOVACS14: consistency costs 1–15%, up to +186% when over-tight [KOVACS14:636] "difference increases travel cost by up to 186.16%.".
   - SRIDHARAN87: freezing up to 50% is nearly free, then steep [SRIDHARAN87:528] "and that the cost of freezing increases rapidly beyond an F value of 0.8.".
   - RideBound's C-30 cost is −96 riders, 2.6 pp of requests (fact pack l.41). That is at the cheap end, but it was measured at low load (about 0.54 riders per vehicle, fact pack l.54).
   - **Credibility needs the frontier at a denser pooling level** (the WP14r FREE arm is 23.8% drop-exposed, fact pack l.47).
4. **Who bears pooling's costs.** Users carry the diseconomies and unreliability, while the operator captures the economies:
   - [FIELBAUM-SCALE:728] "users, get outweighed by the sources of scale economies for the operators";
   - [FIELBAUM-SCALE:617] "Both types of unreliability worsen when vehicles are more loaded".
   - This supports a business framing: rule C protects the side that does not capture the pooling gain, which matters for adoption.

### O3: what riders care about
5. **Lateness against the expected arrival is the heaviest-weighted time component.**
   - Meta-analysis means are 2.53 and 3.12 times in-vehicle time, with medians around 2.5 [WARDMAN26:617] "MeanLate-X/Y 3.12 0.233 2.65-3.59 66 27 2.47". Official guidance is 2.5–3.5. Urban car/other (taxi) is 2.61 (stated preference) and 3.04 (revealed preference) (PDF p.19).
   - Spread (RR) is weighted only 0.6–0.9 [WARDMAN26:1349] "A range between 0.6 and 0.9 would seem more appropriate".
   - So RideBound's metric (late versus first promise) targets the economically heavier quantity.
6. **Counter-evidence for pooled services specifically.**
   - In the Dutch stated-preference study, RR is about 0.5, and small unannounced systematic delay is valued *below* in-vehicle time [ALONSO20:642] "of a (small) unannounced yet systematic additional time in the utility function is lesser than that of the announced times.".
   - The authors flag this as counterintuitive and as possibly understated for real lateness [ALONSO20:979] "the VOR may be higher than found in this study to avoid lateness.".
   - The thesis must cite both. It must also accept that longer quotes have a rider cost under this model; the forecast adds 7.4–13.7 s (fact pack l.45).
7. **What a rider-facing claim can say.**
   - In published simulators, promises move by minutes:
     - FIELBAUM20 base: 36.1% of first-accepted riders see a change [FIELBAUM20:626] "First-accepted requests that face changes 36.1% 52.6% 33.3% 41.2% 34.7% 32.8%", +1.68 min when the delay grows, up to 6 changes;
     - SCHULZ26: average slip against the offered drop-off is 182–280 s with l = 15 min (Table 2, PDF p.27).
   - Under rule C, the dispatch part of a rider's drop-off promise moves by at most B = 30 s in total, while traffic is reported separately. The settings differ, so this is not a head-to-head comparison.

### O6: novelty boundary, optimization patterns, alternative promises
8. **Novelty update (decision-relevant).** FIELBAUM20 and SCHULZ26 together pre-empt:
   - measuring change against the first announcement;
   - an operator-induced focus;
   - freeze/commit rules with a measured trade-off;
   - a per-rider communicated bound on post-acceptance drop-off slip, with an allowance-versus-rejection curve.
   - Still defensible: a **cumulative, two-sided, seconds-scale budget on |dispatch-caused revisions|**, **separated from traffic by the v/e/p ledger under measured time-varying speeds**, plus a forecast quote, plus the finding that C, unlike deadline M+, never forces a broken promise.
   - FIELBAUM20's stated open problem is the citation hook [FIELBAUM20:1038] "The most relevant one is how to control it,".
   - Use the stronger wording at `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md:56`.
9. **The example thesis's pattern** (PDF p.10-14, p.41-49):
   - Same pipeline, one step varied, operator metrics plotted against load.
   - The new piece is a small greedy variant, Prune Prophet, which trades optimality for speed (PDF p.42).
   - The results themselves show trade-offs: Prophet serves 126 versus Basic 114 at 150 requests, but costs 0.36 versus 0.27 per served request (PDF p.47-48).
   - RideBound could add a comparable "one pipeline step" chapter without changing its storyline.
10. **The closest literature analogue to such a chapter is in SCHULZ26.**
    - Reinsertion lowers rejection from 39.92% to 38.92% (Table 7, PDF p.42), but raises accepted riders' average slip from 181.71 s to 279.87 s (Table 2, PDF p.27).
    - RideBound candidates:
      - (a) a budget-aware insertion/reinsertion that tries other positions or vehicles before rejecting a request blocked by a co-rider's budget. 148 such requests exist, with median overshoot 110 s (fact pack l.51-52);
      - (b) budget allocation as the optimized component: a proportional budget unblocks 11→30 (60 s) and 59→89 (120 s) as a first-order screen (fact pack l.52-53).
    - Both are T2 or offline T0 screens. Either way, report a frontier (served versus budget used versus late share).
11. **Alternative promise forms exist and are prior work.**
    - RAUH25: a range now, the exact time later, giving +38% served in the rural case, but only with a tailored algorithm [RAUH25:769] "In fact, GIHflex cannot even outperform its non-flexible". The rider cost is detour 9.1% → 11.7%.
    - AZADEH22: a priced menu of windows, served 41.68% → 74.36% and profit 436 → 655 (Table 14, PDF p.20).
    - SCHULZ26: a point time plus a communicated latest time.
    - Switching the thesis to window or menu promises would be a new project. A cheap reframing that stays in scope: present rule C's promise as "point + ≤30 s dispatch tolerance", i.e. SCHULZ26's form with a cumulative two-sided l.
12. **Freezing lineage, cited as analogy, not anticipation.**
    - SRIDHARAN87: a convex freezing cost; order-based beats period-based above 50%.
    - KOVACS14: consistency is across days; tight hard constraints are disproportionately costly.
    - Rule C is the bounded-change middle between a full freeze (B = 0, RideBound baseline B3 `fixed-freeze-horizon`, `E:/Code/RideBound/docs/08-algorithms-baselines-and-solver.md:25`) and free replanning.
13. **Reporting lesson from HCRIDE25.** It uses an operator-set threshold on a human-centred constraint, but the constraint is aggregate over all agents [HCRIDE25:229] "the cumulative reward and cost across all agents, rather than". It reports no frontier.
    - Rule C's per-rider budget is a clean contrast ("why per rider": the aggregate can hide individuals).
    - RideBound should show B as an operator dial with its curve.
14. **Low value for the decision:** BREGNI11 (no data); FIELBAUM-SCALE (useful framing, venue not printed); MOLENBRUCH15 (no rejections modelled, static).

## Appendix: verification log
- `verify_quotes.py` was run on this file: 249 quoted fragments, each found on its cited line (±2), 0 wrapped and 0 failed.
- The 12 anchors without a quote (DOI, dates, table rows and so on) were listed with their txt lines and checked by eye.
- These tables were checked visually against the rendered PDF pages:
  - FIELBAUM20 Table 2 (p.10) and Table 5 (p.17);
  - SCHULZ26 Tables 1–2 (p.27), Fig. 7 (p.29) and Table 7 (p.42);
  - ALONSO20 Tables 4–5 (p.9);
  - WARDMAN26 Table 8 (p.19);
  - AZADEH22 Table 14 (p.20);
  - THESIS Figs 4.5–4.8 (p.47-49).
- Not checked visually, and relying on reader re-pairing confirmed by arithmetic: MOLENBRUCH15 Table 4 (cost = 0.30·km + 200·fleet holds for the three rows used) and RAUH25 Table 4.
- UNVERIFIED items:
  - RAUH25 and MOLENBRUCH15 volume and pages;
  - FIELBAUM-SCALE venue and year;
  - HCRIDE25 pages;
  - the units of Fig 4.8 running time in THESIS;
  - AZADEH22 Sec. 8.3 average-row column mapping;
  - whether THESIS was accepted, and with what grade.

