# Elmi et al. 2026: direct comparator and remaining questions

Primary publication: *Improving ridepooling reliability using shareability shadows*, Transportation Research Part C 192, 105897. DOI https://doi.org/10.1016/j.trc.2026.105897. Published online 4 August 2026; November issue date is not the availability date. Public repository: https://repository.tudelft.nl/record/uuid%3A8d4faffb-7e75-425b-9e53-1ac78e70e2a5.

Local PDF `downloads/elmi-2026-shareability-shadows.pdf`: 33 PDF pages (cover plus32 article pages), SHA-256 `5a68817ab7d231c0875686d9b468d924d80695621379902756efd5b4cfe728a5`. All text pages read; formulas6–9 and Table2/3 visually checked on PDF pages11/20. Other figures have not all been visually examined.

## Mechanism and actual boundary

The paper addresses operator-induced changes to an already-assigned rider's time on a static travel-time network. It preserves incumbent stop order, does not reassign accepted waiting riders, and does not retry rejected riders. Thus its baseline is closer to RideBound's current insertion setting than the more permissive 2020 baseline.

Pickup/dropoff shadow regions approximate possible future sharing. Pickup and dropoff locations are not checked as a jointly feasible OD insertion; the new rider's delay is omitted from the dropoff region (footnote8). The implementation replaces joint OD rates and product coverage fractions (Eq8) with a sum of origin and destination marginal rates (Eq9) for runtime. Consequently the implemented score is a proxy, not an exact expected number of feasible jointly shareable requests. It also omits competitor vehicles. These are admitted approximations, not demonstrated bugs.

Demand rates use recent observed10-minute counts with exponential smoothing and spatial clusters. The score is integrated over the planned route at initial assignment. Recomputing it later is discussed but avoided because changing exposure would change the initial guarantee. Protection after a first change is also mentioned as an extension; generic rolling protection is not an unoccupied novelty claim.

Ordinary control keeps a common fraction of each rider's initial waiting/delay slack. Shadow control gives low-score riders zero slack and high-score riders full slack. The method already chooses which riders receive a no-update guarantee. How an online percentile threshold is estimated for the control policy is not fully resolved by this reading; do not assert future leakage. The separate informing policy explicitly learns a threshold from recently served riders. Data/code are available on request, not reproduced here.

## Exact comparison in Table2, articlep19 / PDFp20

| Metric | Ordinary control | Shadow control |
|---|---:|---:|
| Rejection percent |29.09|29.21|
| Fraction with increased total delay, percent |63.17|15.39|
| Conditional mean increase among affected riders, minutes |0.84|3.74|
| Conditional mean number of increases |1.05|1.80|
| Maximum number of increases |2|5|
| Mean waiting time, minutes |2.85|3.24|
| Mean detour time, minutes |2.08|1.39|
| Mean total delay, minutes |4.93|4.64|
| Vehicle-minutes statistic as reported |67.02|70.26|

The reduction63.17−15.39=47.78 is **percentage points**, not a47.78% relative reduction. The reported83.85% guarantee corresponds to100−16.15% allowed an increase. Conditional burden increases markedly. Multiplying rounded conditional mean by affected fraction gives approximate population mean added delay0.531 vs0.576minutes, consistent with the paper's statement that its primary improvement concerns how many riders are affected, not eliminating aggregate added delay. These derived numbers are not independent experimental results.

Utrecht one-day TableB9 also concentrates burden: fraction52.88→23.64%, conditional magnitude1.41→3.66minutes, population mean approximately0.75→0.87minutes. Large-fleet, high-capacity and more-tolerance appendices show the same qualitative concentration. No direct quantitative comparison with RideBound is valid without matching demand, constraints, fleet, stop service, and denominators.

## Research implication

This paper explicitly lists magnitude prediction, competitor vehicles, equity, repeated updates and alternative routes as future work. It is therefore incorrect to present 'fair shareability', 'protect low-risk customers', or 'account for the second update' as a novel idea solely because this implementation omits them. A thesis would need a concrete algorithm, stated service contract, and measured improvement under that contract.

One useful distinction to investigate is **post-acceptance route optimization under an unchanged per-rider budget**, versus assigning heterogeneous initial slack. The former cannot obtain apparent gains simply by exposing selected riders to larger changes, but might have little feasible room. Current original-core probes show no coverage-ranking gain in20 actual states and no repair rescue in the initial20-state probe. Strong evidence is required before implementation.

Potential comparator experiment, not executed: same initial offer/windows and rider-specific maximum additional delay for all arms; compare fixed shadow control, a magnitude-capped shadow variant, current C1, and any proposed route method. Report acceptance together with conditional and unconditional burden, fraction affected, upper tails, repeated updates, runtime, and initial wait/detour. This is a test design, not an asserted new method or positive result.
