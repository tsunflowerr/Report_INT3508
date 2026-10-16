# R35 independent paper-definition audit (sub-agent)

Scope: `06-chuong2-v4.tex` claims involving Hörl–Zwick, Schulz–Pfeiffer, Elmi et al. and Mt-KaRRi; relevant cells of Tables 2.1/2.2; narrow rule-C positioning against Ch3 v3. Overall verdict for this scope: **ACCEPT WITH CORRECTIONS**.

I read the actual local PDFs, freshly extracted with system Poppler rather than relying on the writer's BIB or pre-existing text. Source PDF pages below are physical PDF pages; printed pages are given separately where different. No source or draft was modified. The PDF skill was read; this is read-only PDF work, with no authoring marker, rendering, build, installation or simulation. The owner permits small text files only, so the new outputs are the extraction script, four extracts and this report, all created exclusively in the authorized folder.

## Sources opened independently

- HZ: `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf`. Printed pp.4–5,7–10,14 (PDF pp.5–6,8–11,15) and cover/title pages. The actual HZ title is *Traffic uncertainty in on-demand high-capacity ride-pooling*. Authors Sebastian Hörl and Felix Zwick; ETH Research Collection cover identifies Conference Paper, 2022, DOI 10.3929/ethz-b-000561639. Title page has submission date 27 October 2021. No conference name independently verified.
- SP: `C:/PDF/Paper/s00291-026-00847-0.pdf`. Printed pp.549–551,562,569 (PDF pp.9–11,22,29), plus title page. Arne Schulz, Christian Pfeiffer, *Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem*, OR Spectrum 48:541–586 (2026), DOI 10.1007/s00291-026-00847-0. Published online 2 February 2026 according to title page. Issue number not checked by this sub-agent.
- ELMI: `C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/ch2/dl-elmi/elmi2026.pdf`. Printed pp.1–2,5–7,12–13,15–19 (PDF pp.2–3,6–8,13–14,16–20). Amir Elmi, Emily Moylan, Javier Alonso-Mora, Andres Fielbaum, *Improving ridepooling reliability using shareability shadows*, Transportation Research Part C 192 (2026), article 105897, DOI 10.1016/j.trc.2026.105897. Cover specifies final published version; article first page available online 4 August 2026.
- MTK: `C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/judge-dl-mtkarri/mtkarri.pdf`. pp.1,4–5,13,26–27. Moritz Laupichler, Robin Andre, Kim Kandler, Peter Sanders, Peter Vortisch, *Advancing Dynamic Ride-Pooling Simulation – A Highly Scalable Dispatcher*, arXiv:2605.11798v1, 12 May 2026, DOI 10.48550/arXiv.2605.11798. Independently corroborated on the [official arXiv record](https://arxiv.org/abs/2605.11798). DOI pages for HZ, SP and ELMI were attempted but inaccessible in the web tool; their metadata above comes from the opened PDFs, not those failed web calls.

Additional read-only inputs: brief, parallel rules, WRITING-BRIEF, GLOSSARY-VI-v2, evidence register rows A01/A02/A06/A13/B03/J01–J05/J10/J12/J32/K01/K03/K26/K43/K47, addendum-1 §0, addendum-5, Ch3 v3 §§3.3–3.4 and `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`. B03 configuration and normalizer/physical-validator code were opened directly. Bibliographic claims above are independently read from source headers; they do not assert that the writer's bibliography has all these fields correct (the root agent handles that comparison).

## Per-item verdicts

AGREE means the source supports the stated claim. OVERSTATED means retain with the qualification or replacement below. CANNOT CHECK is a missing-evidence item; no rate counts were invented from rounded percentages.

| ID | Draft item / clause | Paper verdict | Evidence and reasoning | Deliverable verdict |
|---|---|---|---|---|
| TD-01 | §2.1: dynamic requests only become known on arrival, citing SP | AGREE | SP printed p.549 explicitly says request details not known beforehand; p.550 decision epochs occur at receipt of a new request. | ACCEPT |
| TD-02 | §2.1: HZ uses Alonso-Mora algorithm | AGREE | HZ printed p.4 contribution and algorithm overview; p.9 MATSim implementation and joint 30-second batches. | ACCEPT |
| TD-03 | Table 2.1: Elmi maximum pickup waiting 5 minutes | AGREE | ELMI printed p.15, Base setup; waiting defined on p.5 as pickup minus request time. | ACCEPT |
| TD-04 | Table 2.1: Elmi maximum total delay 10 minutes | AGREE | ELMI printed p.15 setup; p.5 delay = waiting + detour, so this is not 10 minutes of in-vehicle detour alone. Draft identifies total delay correctly. | ACCEPT |
| TD-05 | Table 2.1: SP six-seat vehicles | AGREE | SP printed p.562 §6.1: Q = 6; number of people per request capped at capacity. | ACCEPT |
| TD-06 | Table 2.1: thesis pickup window 600 seconds from calling | AGREE | B03; fixture normalizer-configuration `pickupWindowMs:600000`; normalizer lines 444–445 constructs earliest = request arrival and latest = arrival + pickup window. | ACCEPT |
| TD-07 | Table 2.1: thesis ride time at most 1.5 direct | AGREE | B03; fixture `maximumRideTimePermille:1500`; normalizer scales direct by 1500/1000; physical validator subtracts pickup from dropoff to compute ride time. This is candidate feasibility and its configured bound, not unconditional realized service guarantee under traffic. | ACCEPT |
| TD-08 | Table 2.1: thesis four seats and eight vehicles per scenario | AGREE | B03 and same fixture `vehicleCapacity:4`, `vehicleCount:8`. | ACCEPT |
| TD-09 | §2.2: Elmi continues the reliability-control direction for individual customers | AGREE | ELMI printed p.1 passenger-specific predictive model and targeted operational rules; pp.12–13 shadow control. | ACCEPT |
| TD-10 | §2.2: slack = maximum waiting/delay minus value expected at assignment | AGREE | ELMI printed p.5 Eq.(2): waiting slack Ω_r − initial waiting; delay slack Φ_r − initial delay. No allowance reset at each new insertion is defined. | ACCEPT |
| TD-11 | §2.2: low-score customers get zero slack and no time updates | AGREE | ELMI printed pp.12–13 zero slack for low-score passengers; interpretation controls first increase; algorithm pp.6–7 preserves existing stop order, static arc times p.5. To avoid conflating arbitrary early changes with the reliability metric, optional precision is “không bị tăng thời gian chờ hoặc độ trễ”. | ACCEPT |
| TD-12 | §2.2: other customers keep their full slack | AGREE | ELMI printed p.12 Shadow Control sets low to 0% and high to 100% of their assignment slack. Score fixed once at assignment, p.13. | ACCEPT |
| TD-13 | §2.2: “Ở cùng tỉ lệ từ chối 29%” | OVERSTATED | Abstract rounds both to 29%, but printed p.19 Table 2 has 29.09% ordinary vs 29.21% shadow. Printed pp.17–18 explicitly describe similar/approximately same inefficiency, not identical rates. These are averages of ten daily simulations (p.15/Fig.10), not an identified pooled count. Use R3 below. | ACCEPT WITH CORRECTIONS |
| TD-14 | §2.2: guarantees no-update trip to 83.9% at assignment | AGREE | Abstract p.1 gives 83.9%; printed p.18 gives 83.85%, based on Table 2 P_allowed(delay) = 16.15% (p.19). This is guaranteed-at-assignment, not just observed no-update fraction. It is within their Base scenario and ten-day average. | ACCEPT |
| TD-15 | Exact numerator/denominator needed for Elmi rates under owner rules | CANNOT CHECK | Printed p.15 has 226,676 input requests over ten days but says only about 62% remain after simulation/result filters. No exact retained-request count or raw per-day denominators accompany Table 2. 83.85% concerns passengers allowed delay changes, not all original requests. Do not infer counts from percentages or 226,676. Cut numeric rates using R3 unless raw tables are obtained. | ACCEPT WITH CORRECTIONS |
| TD-16 | §2.2: Elmi assumes each edge travel time fixed and excludes traffic unreliability | AGREE | ELMI printed p.5 arc travel time constant; printed p.2 explicitly excludes unreliability caused by users/network. | ACCEPT |
| TD-17 | §2.3: SP latest dropoff = accepted offered dropoff + slack | AGREE | SP printed pp.549–550: l_i− = B_i− + l calculated directly after customer accepts; p.551 communicates both scheduled and latest possible arrival. | ACCEPT |
| TD-18 | §2.3: SP default slack 900 seconds | AGREE | SP printed p.562 §6.2 sets l = 900 s. | ACCEPT |
| TD-19 | §2.3: SP concludes 10–15 minute slack reasonable after sweep up to 30 minutes | AGREE | SP printed p.569 Finding 5 and preceding discussion; p.568 §6.3.5 sweep context. Interpret as conclusion for the paper's tested setting, not universal customer preference. Optional “trong các thí nghiệm của bài” prevents a universal reading. | ACCEPT |
| TD-20 | §2.3: Mt-KaRRi caps trip time relative to accepted tentative trip time | AGREE | MTK p.5: insertion infeasible if new trip time exceeds α·T_t + β for an existing rider; p.26 B.2 defines same threshold for total trip time relative to accepted ride. Do not reinterpret T_t as direct time or as RideBound's in-vehicle cap. | ACCEPT |
| TD-21 | §2.3 / Table 2.2: Mt-KaRRi α = 1.4, β = 10 minutes | AGREE | MTK p.27 B.2 explicitly chooses α = 1.4, β = 10 min. | ACCEPT |
| TD-22 | §2.3: HZ is nearest to C in processing variable travel time | AGREE | Defensible writer's comparison, not a paper result: HZ updates ETA on retained route; Ch3 v3 directly contrasts its max(updated, latest) with C. Do not make this a literature-wide priority claim. | ACCEPT |
| TD-23 | §2.3: HZ MATSim simulation with real MOIA demand in Hamburg | AGREE | HZ printed p.9 MATSim; p.10 MOIA network and historical requests. Simulation is distinct from actual MOIA operations (p.10 warning), which draft does not confuse. | ACCEPT |
| TD-24 | §2.3: HZ traverses assigned routes at beginning of each epoch using current times | AGREE | HZ printed p.7 lines 31–35. This is an updated ETA for the current assigned route, not a globally minimum dropoff time. | ACCEPT |
| TD-25 | §2.3: Eq.7 applies to “các yêu cầu trên xe đang xét” | OVERSTATED | HZ printed p.8 lines 8–9 says all requests assigned to the currently evaluated vehicle. Vietnamese “trên xe” can be read onboard-only; narrative p.7 motivates onboard requests, but the formal quantifier is assigned requests. Replace with “các yêu cầu đã gán cho xe đang xét”. | ACCEPT WITH CORRECTIONS |
| TD-26 | §2.3: HZ required dropoff = max(updated, latest) | AGREE | HZ printed p.8 Eq.(7). Latest is original allowed dropoff (p.4–5), not necessarily offered initial dropoff plus a scalar budget. Ch3 labels substitution p_0+B as its own inference, correctly. | ACCEPT |
| TD-27 | §2.3: routing uses required pickup/dropoff as hard feasibility constraints | AGREE | HZ printed p.8 Eqs.(9)–(10). Correctly avoids claiming hard gate versus soft penalty as novelty. | ACCEPT |
| TD-28 | §2.3: Eq.11 penalizes each second beyond original latest dropoff | AGREE | HZ printed p.8 Eq.(11): α times positive pickup/dropoff excess over original active/latest times, plus β if any violation. Dropoff statement is correct; optional mention pickup and fixed penalty would make the full objective clearer but is not needed. | ACCEPT |
| TD-29 | §2.3: new pickups allowed provided onboard customer not dropped later than “mức sớm nhất có thể” | OVERSTATED | HZ p.7 prose uses this wording in context of customers whose dropoff already violates original limit. Eq.7 does not cap dispatch delay at zero for all customers: when updated ETA < original latest, further delay until original latest remains feasible. Also updated ETA is computed on assigned route, not optimized globally. Replace sentence using R2. | ACCEPT WITH CORRECTIONS |
| TD-30 | §2.3: HZ policy avoids no-feasible-dropoff-order state | AGREE | HZ printed p.7 lines 8–17 identifies undefined onboard state; B motivates avoiding it, lines31–40. Full robust request handling also involves pickup Eq.8 and retained-route safeguard p.8 lines24–27. | ACCEPT |
| TD-31 | §2.3: pickup times treated analogously by Eq.8 | AGREE | HZ printed p.8 Eq.(8), with current-vehicle assignment condition; p.7 lines41–44 and p.8 lines1–4 explain C. This is a distinct added pickup relaxation, not implied by Eq.7 alone. | ACCEPT |
| TD-32 | §2.3: under underestimated travel time must trade late rejection and violating communicated times | AGREE | HZ printed p.14 conclusion lines12–15. | ACCEPT |
| TD-33 | §2.3: impact minor for realistic travel-time scenario | AGREE | HZ printed p.14 conclusion immediately following tradeoff. Draft says actual travel times; safer faithful wording “trong kịch bản dùng thời gian đi thực tế” or “gần thực tế”, since this was still simulation. | ACCEPT |
| TD-34 | §2.4: HZ current speeds updated every 60 minutes from GPS data | AGREE | HZ printed p.10 lines11–14: TomTom GPS speed data for weekdays November 2019, network speeds updated each 60 min. It is not 60-minute updates of a historical forecast model. | ACCEPT |
| TD-35 | Table 2.2 SP: offered deadline +900; applies all accepted; compare current dropoff to original offer | AGREE | SP printed pp.549–551 per accepted request deadline, never later rejected; default p.562. No sum of absolute inter-epoch ETA revisions in this definition. “Không” is valid only with the table's explicit magnitude-sum meaning. | ACCEPT |
| TD-36 | Table 2.2 SP traffic: given travel time, “khi thời gian đi đổi thì có” | OVERSTATED | SP supplies t_jj′ and triangle inequality at p.549, and exogenous information only requests/customer acceptance p.551. It does not analyze time-varying road travel times. The extra phrase is a hypothetical extension of fixed deadline logic, not a finding from this paper; Ch3 v3 correctly identifies traffic stress as thesis comparator only. Use R4. | ACCEPT WITH CORRECTIONS |
| TD-37 | Table 2.2 HZ baseline and affected riders: original latest and updated ETA; effect when updated > limit | AGREE | HZ printed p.8 Eq.7. Binding relaxation indeed starts only when updated exceeds original latest. “Khách của xe đang xét” means currently assigned requests. | ACCEPT |
| TD-38 | Table 2.2 HZ traffic: “riêng tắc đường không làm tuyến bị loại” | OVERSTATED | Eq.7 guarantees the retained route's dropoff constraint after recalculation; it alone does not relax pickup Eq.9 (requires Eq.8), nor stop requests disappearing from request graph (requires forced retained route, p.8 lines24–27). Current row cites Eq.7/9/10/11 only. Restrict to dropoff using R5 or add Eq.8/full safeguard if claiming whole route. | ACCEPT WITH CORRECTIONS |
| TD-39 | Table 2.2 HZ cumulative magnitude: No | AGREE | HZ Eq.7 compares a fresh candidate ETA to max of current-route ETA and original latest; Eq.11 penalizes original-reference excess. No per-customer sum of absolute inter-epoch revisions in those definitions. The paper's “cumulative delay” in Eq.3 sums across riders, not over one rider's revision history. | ACCEPT |
| TD-40 | Table 2.2 Elmi baseline / applies / no cumulative magnitude | AGREE | ELMI p.5 Eq.2 defines initial-assignment slacks; pp.12–13 low/high score control; p.13 explicitly computes score once for entire trip. This restricts residual slack across future insertions, so do not misdescribe it as renewed allowance per update. It does not sum absolute revision magnitudes. | ACCEPT |
| TD-41 | Table 2.2 Elmi traffic excluded | AGREE | ELMI printed pp.2,5 explicitly excludes network uncertainty and has constant arc times. | ACCEPT |
| TD-42 | Table 2.2 MTK baseline / applies / no cumulative magnitude | AGREE | MTK pp.5,26–27: every existing accepted rider is constrained by original accepted trip time; fixed threshold, not reset at update. No explicit sum of |inter-epoch change| appears. This still limits the net additional trip time throughout the ride. | ACCEPT |
| TD-43 | Table 2.2 MTK fixed edge times | AGREE | MTK p.4 Road Network associates fixed ℓ(e) with every edge. “Ngoài phạm vi: thời gian đi trên mỗi cạnh cố định” would answer the column more consistently. | ACCEPT |
| TD-44 | Table 2.2 last column: all prior methods “Không”, headed “Ghi riêng cho từng khách?” | OVERSTATED | SP has per-request deadline; HZ per-request updated/required ETA; ELMI per-request slack and score; MTK per-rider accepted time/threshold. Those are individually stored quantities. The meaningful distinction is an explicit per-rider accumulated absolute-change total, not passenger-specific data. Rename heading and replace cells using R1. | ACCEPT WITH CORRECTIONS |
| TD-45 | Table 2.2 caption: “Không” means comparing one ETA to an anchor, not summing magnitudes | AGREE | Consistent with the listed equations; it does not claim fixed deadlines lack lifetime/net-shift limits. Rename cumulative heading to “Cộng độ lớn các lần dời?” for immediate clarity. | ACCEPT |
| TD-46 | Rule C row: old-plan recalculated ETA; excludes old-plan change; applies confirmed promises; absolute cumulative rider ledger | AGREE | A01/A02/A06/A13, Ch3 v3 three anchors and C definition. Scope matches waiting and onboard promised riders; same state/time basis avoids causal claims. “Tắc đường” is shorthand: Ch3 says x also includes actual progress and recent events. Optional column wording should acknowledge old-plan change, not only congestion. | ACCEPT |
| TD-47 | §2.3 positioning: uses HZ updated anchor; distinct dispatch-change magnitude accumulated over trip with common cap and no traffic relaxation | AGREE | HZ Eq.7 and Ch3 v3 eq.(C) support the narrow comparison. It does not claim updated ETA, customer protection, hard constraint or insertion as novel. Mathematical distinction may not produce different outcomes in every fixed-time monotone insertion setting; no such universal effect is claimed. | ACCEPT |
| TD-48 | §2.3: signed total old-plan + dispatch changes returns initial-promise endpoint deadline; absolute customer-visible changes form other comparator | AGREE | Ch3 v3 telescoping identity v_j = p_(j−1), Σz = p_n−p_0; C accumulates |c|, other comparator |z|. Do not attribute these three-law identities to HZ/SP/ELMI/MTK as their measured results. | ACCEPT |
| TD-49 | §2.3: per-customer protection, arrival limits, dynamic insertion, reassignment already exist | AGREE | ELMI pp.6–7 explicitly uses insertion preserving old stop order; SP reoptimization can shift customers to another tour (fulltext p.554+); HZ p.8 explicitly permits reassignment under original pickup condition; MTK p.4–5 online insertion and accepted-rider limits. Matches claim-boundary prohibitions. | ACCEPT |

## Ranked exact Vietnamese corrections

### R1 — make the rider-ledger comparison narrow and accurate (TD-44)

Replace the last Table 2.2 heading:

> `\textbf{Lưu tổng độ lớn các lần dời cho từng khách?}`

Replace each prior-paper cell in that column with:

> `Bài không mô tả sổ này`

Replace the rule-C cell with:

> `Có: lưu tổng phần dời do điều phối của từng khách`

Also replace the cumulative heading with:

> `\textbf{Cộng độ lớn các lần dời?}`

To make the two columns' connection explicit, add this sentence to the caption:

> `Cột cuối hỏi về sổ cộng độ lớn các lần sửa, không hỏi liệu nghiên cứu có lưu giờ hẹn hay ràng buộc riêng của từng khách.`

SP, HZ, ELMI and MTK all explicitly associate their anchors/limits with individual requests. The new heading avoids a false contrast while preserving C's narrower ledger definition. “Bài không mô tả sổ này” does not assert anything about unpublished production code.

### R2 — qualify HZ no-further-delay rule by the actual max equation (TD-25, TD-29)

Replace “các yêu cầu trên xe đang xét” with:

> `các yêu cầu đã gán cho xe đang xét`

Replace the sentence beginning “Xe vẫn được đón thêm khách...” with:

> `Khi giờ trả cập nhật đã vượt hạn gốc, xe vẫn được đón thêm khách nếu phương án mới không trả khách đó muộn hơn giờ trên tuyến cũ đã tính lại; khi chưa vượt hạn, phương án vẫn được dùng phần thời gian còn lại tới hạn gốc. Cách nới hạn trả này tránh tình huống không còn thứ tự trả khách khả thi; giờ đón được nới tương tự theo công thức 8.`

This follows Eq.7: candidate ≤ max(updated, original latest). It does not identify current-route ETA with a globally earliest possible arrival. The zero-extra-delay behavior applies in the updated>latest region, which Ch3 v3 already explains correctly.

### R3 — remove unsupported precision and unreported denominators in Elmi result (TD-13, TD-15)

Under the owner rule requiring counts and denominators, replace the full sentence beginning “Ở cùng tỉ lệ từ chối 29%...” with:

> `Trong thí nghiệm cơ sở, khi hai cách có mức từ chối xấp xỉ nhau, cách phân độ chùng theo điểm bảo đảm ngay lúc gán rằng phần lớn khách không bị tăng thời gian chuyến.`

Evidence: printed p.19 Table 2 gives 29.09 vs29.21 (two slightly different mean rejection rates); printed p.18 gives 83.85% guaranteed, abstract rounds to83.9%. Figure10/p.15 use averages across ten days. Exact counts absent from opened article tables, so neither the input total226,676 nor “about62% remained” can legally supply a denominator. If root has independent raw per-day result counts, preserve the result only with proper mean/pooled scope and those counts.

Optional precision for the prior sentence, if editing it too:

> `Khách có điểm khả năng đi chung thấp nhận độ chùng 0, tức không bị tăng thời gian chờ hoặc độ trễ; khách khác giữ toàn bộ độ chùng lúc gán.`

### R4 — keep traffic extension separate from SP's tested problem (TD-36)

Replace SP's traffic cell with:

> `Ngoài phạm vi: thời gian đi giữa các điểm được cho trước`

The paper defines given t_jj′, fixed accepted deadline and request/acceptance uncertainty. Ch3 correctly says the thesis deadline comparator borrows just that deadline component and adds changing traffic. Do not present its traffic failure as a result for SP's full method.

### R5 — state exactly which HZ feasibility condition is preserved (TD-38)

Replace HZ's traffic cell with:

> `Hạn trả được nới tới giờ trên tuyến cũ đã tính lại, nên phần đổi này không làm vi phạm điều kiện hạn trả`

Optional shortening:

> `Nới hạn trả tới giờ cập nhật trên tuyến cũ`

If retaining the stronger whole-route claim, the row must mention Eq.8 and the forced retained-route safeguard, and must be explicit that both protections are applied. The existing Eq.7-only label cannot justify a blanket statement about pickup constraints or requests disappearing from the graph.

## Positioning conclusion for root

Accept the narrow contribution in §2.3 once R1–R5 are addressed. It correctly credits HZ for the refreshed retained-route ETA; recognizes accepted initial-offer/trip anchors in SP/MTK; recognizes personalized slack guarantees in ELMI; and uses a per-rider sum of dispatch-change magnitudes rather than claiming a new generic ETA cap. Keep “Không” in the cumulative column only with magnitude-sum wording: SP/MTK/ELMI do constrain net delay through the trip and do not renew allowance on each update. Ch3 v3 is more precise than Ch2 on the HZ hinge updated>latest and on SP traffic being a thesis extension; the replacements restore consistency.

One further optional wording refinement is to replace traffic-column heading “Phần do tắc đường có bị tính?” with “Phần đổi khi giữ kế hoạch cũ có bị tính?”. Ch3 explains that this component also includes vehicle progress and new events. For historical papers with fixed travel times use “Ngoài phạm vi”, and for C use “Không: chỉ tính phần dời so với kế hoạch cũ đã tính lại”. This is a terminology improvement, not an additional novel causal decomposition claim.

Probe script: `agent-extract-pdfs.ps1`; primary-source outputs: `agent-hz-extract.txt`, `agent-sp-extract.txt`, `agent-elmi-extract.txt`, `agent-mtkarri-extract.txt`. None of the files was overwritten. The extracted relevant pages can be re-opened by splitting each output at form feed; the source PDFs have not been changed.