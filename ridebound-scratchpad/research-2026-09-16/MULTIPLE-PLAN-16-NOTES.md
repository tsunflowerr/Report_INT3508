# Ackermann–Rieck 2025: completed text and selected visual audit

Updated 2026-09-20. Source: `corpus/16.source.json`, local publisher PDF 35 pages, SHA-256 `059a0bffc546e8588f1d9487ddb16344e7c24c559bc54dfa104979f98e223d3c`. DOI https://doi.org/10.1007/s00291-025-00809-y . Full text pages 1–35 read before pause; rendered pages 11,14,16,21,24,28,29,30 inspected on resumption. This supersedes the earlier partial-HTML reading status. No author implementation inspected.

## Mechanisms and comparison boundary

Fixed fleet and hard windows/maximum ride time, immediate accept/reject, no later acceptance of rejected requests. Next destination fixed once vehicle leaves previous node. Initial requests include advance reservations; generated Euclidean demand uses substantial lead times. These are different operating conditions from immediate-arrival RideBound experiments.

Insertion first scans simple insertions over the pool, then applies remove/reinsert to unsuccessful plans until time limit. First feasible result permits immediate acceptance; rejection waits for the limit. Generation samples a base plan, applies an operator and retains good-enough alternatives; another phase protects agreement with the distinguished plan until estimated next arrival. Best-plan selection is the final choice; time-based consensus was tested but not clearly better. Same plan sequences with different service/departure times count as different plans.

Visual algorithms 1–2 confirm those steps. Relocation and zero-split 2-opt survive preliminary selection; additional neighborhood operators were tested. Generic repair, plan pools, future flexibility and time-based compatibility are prior art, not available novelty claims.

The proposed coverage extension already handles overlap across vehicles and complements across plans. It discretizes space/time and approximates ellipse coverage using a neural network. The paper reports no benefit in full MPA and evaluation over 100 times slower than distance. This is a negative result for that implementation/setting, not a lower bound on all future-feasibility methods.

## Printed coverage equation needs caution

Page 21, article page 801, Eq.(1) visually reads `c = 1 - (1-c1)*c2`. This is not an OCR omission. For coverage fractions as described in the adjoining text, it fails basic union properties: `(0,0)` yields 1, and swapping unequal inputs changes the answer. The text's half-plus-half example yields 0.75 under both this expression and the usual independence approximation `1-(1-c1)*(1-c2)`, so that example cannot disambiguate them.

The latter expression is a plausible intended correction, not a verified account of their code. Even that corrected expression assumes an overlap model; marginal coverage fractions alone do not determine exact geometric union. Do not invalidate the published empirical results or claim a new algorithm by correcting the printed formula without implementation evidence.

## Results checked visually

- Table 1 confirms that MPA is not best in every configuration; large/loose cases favor an SPA variant. SI+MPA can outperform RR+MPA in high-dynamism cases. Accepting a difficult request now can harm later acceptance.
- Table 5 confirms interaction between ranking and scheduling: distance plus early visits benefits from modified dynamic wait, and is worse than distance alone under the other two scheduling conventions in their averages. No general superiority of early visits follows.
- Figures 1–2 support qualitative sensitivity statements; plots were not digitized for new exact values. More improvement time can hurt SPA using distance while helping MPA. Do not treat the plotted trends as a theorem or import the paper's dynamism threshold into RideBound.

## Implication for the current research

Scheduling must be audited before interpreting route-order search completeness. RideBound's projector uses earliest service except lower pickup bounds; its origin-hold transformer only moves existing wait at the first pickup and does not invent arbitrary delay. A new timestamp audit of the 16 captured rejected states finds every known pickup window already open, including the newly arrived request. Therefore the paper's benefit from shifting forced waiting is not present at those particular states. This does not rule out advance-booking workloads, future demand anticipation, or earlier trajectory changes.
