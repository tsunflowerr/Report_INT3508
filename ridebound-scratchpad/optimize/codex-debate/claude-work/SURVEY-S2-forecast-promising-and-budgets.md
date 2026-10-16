# Survey S2: forecast-aware promising and promise budgets

Date: 2026-10-07. Literature agent (Claude). Read-only; no code, runs or thesis edits.
Did not open `codex-work/`.

**Access tags.** [full] = I read the full text; the page is given. [abstract] = verbatim abstract from RePEc, arXiv, Crossref or the Semantic Scholar API; claims beyond it are not checked. [snippet] = search snippet only; the wording may not be verbatim. [prior audit] = verbatim quote recorded in `business-need/SOURCES-2026-10-05.md` by an earlier agent. I did not reopen these today.

**Notation check (please confirm).** The brief defines v as the first promise moved by traffic only and calls x = e − v the traffic part. If v already moves with traffic, then e − v reads like the dispatch part. I did not resolve this. Section 3 relies only on z = x + c and on the rule definitions the brief gives.

## 1. Sources

### A. ETA prediction and promise setting

| # | Source | Tag | Verbatim quote | Location |
|---|---|---|---|---|
| S01 | Hu, Binaykiya, Frank, Cirit (2022), *DeeprETA*, Uber. https://arxiv.org/abs/2206.02127 | full | "user-facing ETAs may call for a set of ETA quantiles or expectiles" (extracted as "userfacing"); "useful in ETA cases where being early is not as costly as being late"; "This post-processing step is separated from the route recommendation from the routing engine." | p1 §1; p6 §5; p3 §4 |
| S02 | Derrow-Pinion et al. (2021), *ETA Prediction with Graph Neural Networks in Google Maps*, CIKM. https://arxiv.org/abs/2108.11482 | full | "travel time is often largely dependent on the historical travel times in the given time-of-day"; baseline "Historical travel times: Summation of segment-level travel times computed using segment speeds specific to hour of day and day of week at the time of prediction, averaged across last 17 weeks." | p2 §2; p5 §4.1.2 |
| S03 | Wang, Fu, Ye (2018), *Learning to Estimate the Travel Time*, KDD. doi:10.1145/3219819.3219900 | abstract | "We also deploy the proposed solution on Didi Chuxing's platform" | abstract |
| S04 | Zhu et al. (2020), *Order Fulfillment Cycle Time Estimation for On-Demand Food Delivery*, KDD (Ele.me). doi:10.1145/3394486.3403307 | abstract | "it needs to be communicated to a customer before he/she places the order, and is considered as a service promise" | abstract |
| S05 | DoorDash Engineering (2021), "Improving ETA Prediction Accuracy for Long-tail Events". https://careersatdoordash.com/?p=4704 | snippet | Not verbatim (the page returned 403). The snippet says over-long ETAs lower conversion and late deliveries erode trust. Not checked. | — |
| S06 | Salari, Liu, Shen (2022), MSOM 24(3):1421–1436. doi:10.1287/msom.2022.1081 | abstract | "we study how to estimate and promise delivery time for new customer orders in real time"; "a new split rule for quantile regression forests that incorporates an asymmetric loss function"; "Our decision rule is proven to be optimal given certain cost structures." | abstract |
| S07 | Ulmer & Thomas (2019), *Enough Waiting for the Cable Guy*, Transp. Sci. 53(3):897–916. doi:10.1287/trsc.2018.0846 | abstract | "we present a method that anticipates future requests and their impact on arrival times in the estimation of arrival times" | abstract |
| S08 | Schmidt, Golak, Schulz, Fliedner (2026), *Optimal Service Commitments in TSPs with Stochastic Demand*. arXiv:2609.11950 | abstract | "In ridepooling services, mobility providers must communicate an expected arrival time before customers decide whether to book. An ambitious commitment attracts higher demand than a conservative one, but is correspondingly harder to fulfill." | abstract |

### B. Time-dependent and stochastic routing, DARP and ride-pooling

| # | Source | Tag | Verbatim quote | Location |
|---|---|---|---|---|
| S09 | Malandraki & Daskin (1992), Transp. Sci. 26(3):185–200. doi:10.1287/trsc.26.3.185 | abstract | "depends on the distance between the points and time of day"; "treat the travel time functions as step functions" | abstract |
| S10 | Ichoua, Gendreau, Potvin (2003), EJOR 144(2):379–396. doi:10.1016/S0377-2217(02)00147-9. Also Ghiani & Guerriero (2014), Transp. Sci. 48(3):458–462. doi:10.1287/trsc.2013.0491 | snippet (2003); abstract (2014) | The 2014 note describes the 2003 model as the one "on which most of the current time-dependent vehicle-routing literature relies". | 2014 abstract |
| S11 | Schilde, Doerner, Hartl (2014), EJOR 238(1):18–30. doi:10.1016/j.ejor.2014.03.005 | abstract | "If not accounted for, time-dependent and stochastic travel speeds frequently lead to missed time windows"; "a deterministic method (average time-dependent travel speeds for planning)" | abstract |
| S12 | Spliet, Dabia, Van Woensel (2018), Transp. Sci. 52(2):261–276. doi:10.1287/trsc.2016.0705 | abstract | "assigning time windows to customers before their demand is known and creating vehicle routes adhering to these time windows"; the model includes "time-dependent travel times" | abstract |
| S13 | Ehmke, Campbell, Urban (2015), EJOR 240(2):539–550. doi:10.1016/j.ejor.2014.06.045 | abstract | "restrictions are placed on the probability that individual time window constraints are violated" | abstract |
| S14 | Jaillet, Qi, Sim (2016), Oper. Res. 64(1):186–200. doi:10.1287/opre.2015.1462 | abstract | "Requirements Violation (RV) Index, which quantifies the risk associated with the violation of requirements taking into account both the frequency of violations and their magnitudes" | abstract |
| S15 | Long, Tan, Szeto, Li (2018), TR-B 118:143–171. doi:10.1016/j.trb.2018.10.004 | abstract | "Different from the traditional models taking time windows as hard constraints"; "a feasible ride-sharing match based on deterministic travel time can become infeasible in a stochastic ride-sharing system" | abstract |
| S16 | Fielbaum & Alonso-Mora (2020), TR-C 121:102831. doi:10.1016/j.trc.2020.102831 | full (local PDF) | "The unreliability that emerges due to traffic conditions in ridesharing systems has been studied by Liu et al. (2019)"; they choose off-peak hours, "which allows us to disregard unreliability due to traffic conditions" | p3 §1; p9 |
| S17 | Schulz & Pfeiffer (2026), OR Spectrum 48:541–586. doi:10.1007/s00291-026-00847-0 | full (local PDF) | "li− = Bi− + l sets the deadline for any delay of customer i" | p9 §3.1 |

### C. Lead-time quoting

| # | Source | Tag | Verbatim quote |
|---|---|---|---|
| S18 | Duenyas & Hopp (1995), Mgmt Sci 41(1):43–57. doi:10.1287/mnsc.41.1.43 | abstract | "we derive a closed-form expression for the optimal lead time quote" |
| S19 | Keskinocak, Ravi, Tayur (2001), Mgmt Sci 47(2):264–279. doi:10.1287/mnsc.47.2.264.9836 | abstract | "coordinating scheduling with lead-time quotation"; "the quoted lead times are 100% reliable" |

Hopp & Sturgis (2001), MSOM 3(4):321–336: I saw the metadata only (the publisher withholds the abstract). Content not checked.

### D. Schedule padding, slack and buffers

| # | Source | Tag | Verbatim quote | Location |
|---|---|---|---|---|
| S20 | Furth, Hemily, Muller, Strathman (2006), *TCRP Report 113*. https://ocw.mit.edu/courses/1-259j-transit-management-fall-2006/70901041ebf48a357b97288097c4ea28_tcrp_rpt_113.pdf | full | "a feasibility criterion of 85% means setting allowed time equal to 85th-percentile observed running time; such a schedule can be completed on time 85% of the time"; "half-cycle time is based logically on a high-percentile value of running time"; "a large sample size is needed to examine variability or extreme values, such as the 90-percentile running time" | printed p30 (PDF p40) §4.4.1; p30; printed p20 (PDF p30) |
| S21 | Deshpande & Arıkan (2012), MSOM 14(3):423–440. doi:10.1287/msom.1120.0379 | abstract | "the scheduled block time allocated for a flight, a factor controlled by airlines"; "impute the overage to underage cost ratio of the newsvendor model for each flight" | abstract |
| S22 | Hao & Hansen (2014), TR-B 69:98–111. doi:10.1016/j.trb.2014.08.008 | abstract | "Poor on-time performance leads to increased SBT in the next year." | abstract |
| S23 | Kroon et al. (2008), TR-B 42(6):553–570. doi:10.1016/j.trb.2007.11.002 | abstract | "a timetable usually contains time supplements in several process times and buffer times between pairs of consecutive trains"; "allocate the time supplements and the buffer times" | abstract |

### E. Excusable delay and attribution

| # | Source | Tag | Verbatim quote | Location |
|---|---|---|---|---|
| S24 | 49 CFR 37.131, current eCFR (last substantive amendment 2016-10-17). https://www.ecfr.gov/current/title-49/section-37.131 | full | "weather or traffic conditions affecting all vehicular traffic that were not anticipated at the time a trip was scheduled) shall not be a basis for determining that such a pattern or practice exists" | (f)(3)(ii) |
| S25 | 49 CFR Part 37, Appendix D, current eCFR | full | "scheduling practices fail to take into account regularly occurring traffic conditions (e.g., rush hour traffic jams)" | interpretation of §37.131 |
| S26 | Uber (2026-08-03), *Delayed Ride Guarantee* | prior audit, SOURCES:243–256 | "if the ride runs 5 minutes or longer than the original estimate, your fare will increase"; "If a rider adds stops after pickup, those minutes do not count toward the guarantee"; the product exclusions include "Matched Share Rides" | :250–253 |
| S27 | ORR (2021), Schedule 8 factsheet | prior audit, SOURCES:268–280 | "if a party causes more delay than its benchmarked amount, it pays an amount equal to the excess delay multiplied by a payment rate" | :275 |
| S28 | DREDF/TranSystems (2010), paratransit OTP topic guide; NYC Comptroller (2016) Access-A-Ride audit; EU 261/2004 | prior audit, SOURCES:155–189, 258–266 | "minimum on-time performance standard (for example, 92 percent)"; NYC excuses late pickups "not due to circumstances beyond its control"; EU Art. 5(3) "extraordinary circumstances" | :185, :167, :264 |

Internal facts used: `optimize/FORECAST-REPORT.md` lines 42, 59–60, 65, 68, 70, 73–75, and `literature-survey-2026-10-06/notes/local-audit.md:69`.

## 2. S1: forecast-aware promising, prior art

Each part of the display layer, mapped to prior work:

1. **Forecast from same-time-of-day history.** A textbook baseline: Google Maps names an hour-of-day × day-of-week average over 17 weeks as a baseline (S02 p5). Time-of-day step functions go back to S09; the S10 model underlies most time-dependent VRP work; dynamic DARP already plans with "average time-dependent travel speeds" (S11). Our version (2–3 prior days, 15-min bins, one citywide factor) is a weaker case of the same idea.

2. **Using the forecast to set what the customer is told.** Known in food delivery (S04), e-commerce (S06), service routing (S07), time-window assignment (S12) and lead-time quoting (S18, S19). Transit schedules (S20) and airline block times (S21, S22) are set from historical time-of-day percentiles.

3. **One-sided, asymmetric padding: max(p, stretched p).**
   - The principle is known: late costs more than early (S01 p6). Related forms are newsvendor block times (S21), cost-sensitive quantile promises (S06) and percentile feasibility (S20).
   - I found no source that uses exactly the max() floor. It is a trivial design choice, not a claim.

4. **A display layer separate from dispatch (open loop).**
   - DeeprETA (Uber) is a post-processing layer "separated from the route recommendation" (S01 p3). So separating promise display from routing is not new.

5. **Three-way split: dispatch, anticipated traffic, unanticipated traffic.**
   - The concept comes from regulation. Lateness from traffic "not anticipated at the time a trip was scheduled" is excused (S24). Scheduling that ignores "regularly occurring traffic" is not excused (S25).
   - Research already separates traffic-induced unreliability from request-induced unreliability (S16 p3, p9).
   - Industry attributes delay by cause (S26, S27).
   - I found no per-rider, cumulative ledger that splits traffic into anticipated and unanticipated relative to the forecast in force at commitment. That fits the existing claim boundary: per-rider, path-dependent, cumulative ledger, with traffic and decision changes separated.

**Defensible residual claim (narrow).** In a per-rider promise ledger, a forecast display layer turns anticipated traffic into an explicit ledger entry at commitment time. This makes 37.131-style attribution auditable per rider. In the 21-cell replay, the layer cut riders more than 60 s late against their first promise from 6.01% to 0.17% (FORECAST-REPORT.md:42). The cost was +13.7 s mean drop promise (:68; the brief says +14 s).

The claim must also state four caveats:

- **Not specific to rule C.** The same layer gives 0.17% for Mplus-30 and V-30 (:65; local-audit.md:69).
- **Fragile against a flat pad.** The comparison with an equal-cost flat pad has a cluster-t interval of [−3.62, +0.07] percentage points (:60). That is the "time-of-day pad beats flat pad" effect, which transit scheduling already expects (S20).
- **Display and feasibility disagree.** 34 of 1,471 displayed first pickup promises exceed the latest pickup time (:70).
- **Unclear attribution.** The traffic forecaster is near-oracle in this one-multiplier world (local-audit.md:72).

**Do not claim:** forecast-aware promising, ETA padding, quantile promises, separating display from dispatch, or excusing unanticipated traffic.

## 3. S2: budgets that combine operator-caused and exogenous delay

**Algebra (uses only z = x + c, with z₀ = 0 at the first promise).**

- Over revisions k: Σₖ Δzₖ = z_t and |z_t| ≤ Σₖ |Δzₖ|.
- A budget that charges both c and x is therefore, by definition, the visible-change cap Σ|Δz| ≤ B.
- Its signed, lateness-only form telescopes to z_t ≤ B, which is the fixed deadline measured from the first promise (S17's l = 15 min is a deadline of this kind).
- The absolute form is a total-variation bound. It implies that deadline, so it is stricter.

**Answer: yes.** A joint c + x budget is the visible-change rule, or the deadline in its signed form. It differs from rule C only because it charges traffic to the budget.

The only principled middle ground I found is the 37.131 structure: charge c plus anticipated x, and excuse unanticipated x (S24, S25). That concept is regulatory prior art. It could be a rule variant, not a novelty.

**What the literature does when exogenous delay exceeds the buffer.**

1. **Excuse after the fact:** the paratransit test (S24, S25), the NYC contract (S28), EU 261 "extraordinary circumstances" (S28; its extension to delays rests on case law, not checked). Lateness is always measured against the promise (z-type) and exogenous causes are removed afterwards. Nothing caps operator-caused change while the trip runs.
2. **Statistical tolerance instead of attribution:** a 92% on-time standard (S28), an 85% feasibility criterion (S20), chance constraints (S13), the RV index (S14), soft schedule-delay costs (S15).
3. **Recovery buffers and recalibration:** recovery time at the 95th percentile (S20), allocated supplements and buffers (S23), block times raised after poor punctuality (S22).
4. **Compensation.**
   - Uber pays drivers when a ride runs ≥ 5 min over the *original estimate*. This is a deadline-type z trigger. Rider-added stops are carved out, and matched shared rides are excluded (S26).
   - UK rail charges attributed delay above a per-party benchmark (S27). This is the closest analogue to a "c budget", but it applies between organisations, not per rider.
5. **Renegotiating a promise after commitment.** Not found in the sources checked. Under 37.131(b)(2), negotiation happens at booking only (prior audit, SOURCES:131).

## 4. S3: conclusions

- **Novelty boundary.** Prior art covers time-of-day forecasting (S02, S09–S11), promises quoted from forecasts or distributions (S04, S06, S07, S12, S18–S20), asymmetric or percentile padding (S01, S06, S20, S21), an ETA layer separated from routing (S01) and excusing unanticipated traffic (S24, S25). "Forecast-aware promising" is not a thesis contribution.
- **Residual claim.** The integration remains open: a per-rider cumulative ledger that records dispatch, anticipated-traffic and unanticipated-traffic parts relative to the forecast at commitment, mirroring 37.131(f)(3)(ii). Present the 6.01% → 0.17% result as rule-agnostic, small-sample replay evidence with the four caveats above.
- **Safest framing.** Call it "an attribution and display layer complementary to rule C", evaluated in replay. Keep the negative closed-loop result. Do not credit C for the reliability gain.
- **Joint c + x budget.** Treat it as the visible-change or deadline comparator, not a new rule. If a middle rule is wanted, the 37.131-style excusable budget (c + anticipated x) is the principled option, cited to S24 and S25.
- **Optimization direction A: quantile (newsvendor) padding.**
  - Display the q-quantile of the predicted drop time, with q = cost_late / (cost_late + cost_early). The precedents are S21 (newsvendor block time), S06 (cost-sensitive quantile rule) and S20 (percentile allowed time).
  - Trade-off: late-vs-promise probability against promise length. Longer promises cost demand (S08: ambitious commitments attract demand but are harder to keep).
  - Limitation: 2–3 history days are too few for tail quantiles (S20 p20 on sample size).
- **Optimization direction B: buffer allocation under a fixed padding budget.**
  - Spread a fixed mean pad (for example the current 13.7 s) across time bins and riders to minimise late-vs-promise. The precedents are S23 (allocating supplements and buffers) and S20 (running-time periods).
  - This generalises the forecast-vs-flat-pad test (A3).
  - Trade-off: reliability against promise length at equal mean cost.
- **Optional direction C: risk-based feasibility.** Check feasibility against the displayed promise with chance constraints or the RV index (S13, S14); this removes the 34/1,471 inconsistency. Trade-off: served riders against reliability. Closed loop was rejected internally, so this needs pre-registration as new work.
