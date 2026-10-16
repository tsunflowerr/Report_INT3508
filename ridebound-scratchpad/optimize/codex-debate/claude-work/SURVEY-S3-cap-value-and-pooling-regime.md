# SURVEY S3: choosing the promise-change cap, and building a high-sharing regime

Date: 2026-10-07. Claude literature agent. I created only this file. I did not read `codex-work/`.

**How I read the sources.** Quotes are verbatim from text I extracted myself (PyMuPDF or curl); I only rejoined words split by line-break hyphens. "p." means the PDF page.

**Tags.**
- [full]: I read the full text.
- [abstract only]: I read only the abstract.
- [snippet only]: I saw only a search snippet; the wording may not be verbatim.
- [prior audit]: the quote is verbatim in `business-need/SOURCES-2026-10-05.md`.
- [secondary]: the source describes another paper that I did not open.

**[ours]** marks my own arithmetic on the facts in the brief.

## Sources

### Perception, accuracy and display

- **[1] Cohen, Fiszer & Kim 2022**, Mgmt Sci 68(4), DOI 10.1287/mnsc.2021.3991 (Via) [full].
  - p.6: "the average ETA error amounts to 0.404 minutes (i.e., 24.24 seconds)".
  - p.8: "We decided to use the threshold value of 10 minutes based on riders' feedback".
- **[2] Goldszmidt et al. 2020**, NBER WP 28208, https://www.nber.org/system/files/working_papers/w28208/w28208.pdf (Lyft) [full].
  - p.18: "ETA is an estimate of the time, in minutes".
  - p.19, fn.20: "in 76.4% of sessions, the difference between the maximum and minimum ETAs shown is one minute or less."
- **[3] Gooze 2013**, Georgia Tech MS thesis, https://www.utc.gatech.edu/sites/default/files/u60/gooze_aaron_i_201305_mast.pdf [full]. This is the basis of TRR 2351:95–103, DOI 10.3141/2351-11; for that published paper I read the [abstract only].
  - Setting: OneBusAway survey, N = 5,074.
  - p.44: "74% of riders had an error tolerance of 5 minutes or less".
  - Fig. 8: the "< 1 min." bin holds 11% of respondents.
  - p.45: "the median of error tolerance from the survey was four to six minutes".
  - p.56: OneBusAway shows "'now' when it is within 2 minutes".
- **[4] Caltrans/Cal-ITP**, GTFS-RT performance metrics, https://analysis.dds.dot.ca.gov/rt_stop_metrics/ [full page].
  - "accurate if it falls within the bounds of this equation: -60ln(Time to Prediction+1.3) < Prediction Error < 60ln(Time to Prediction+1.5)".
  - "0 min -0.26 min early - 0.41 min late"; "10 min -2.42 min early - 2.44 min late".
- **[5] MBTA prediction accuracy** (mbta.getanchor.io, host unreachable) [snippet only]. Predictions 0–2:59 min ahead count as accurate "between 1 minute early to 1 minute late". Not verified.
- **[6] Alonso-González et al. 2020**, TR-C 115:102621, DOI 10.1016/j.trc.2020.102621 [full]. Stated preference, N = 1006.
  - p.1: the reliability ratio is "around 0.5".
  - p.12: "a small additional unannounced increase in time may not be fully accounted for by individuals".
  - p.18: the displacement levels tested were 0–4 min.
- **[7] König & Grippenkoven 2020**, ETRR 12:1, DOI 10.1186/s12544-019-0391-3 [full].
  - p.3: "Shift of departure was defined as the shift of the actual pick-up time caused by the ad hoc access of further passengers".
  - Levels tested: 0/10/20 min.
  - p.7: willingness to pay is "3.47 cent/min" for shopping trips and "5.52 cent/min" for a doctor's appointment.
- **[8] Schatzmann, Zwick & Axhausen**, MOIA survey (N = 4,167), https://www.moia.io/mobility_analytics/studies/2303_MOIA_survey_choice_model.pdf [full; short paper, venue not checked].
  - pp.6–7: "a larger window of arrival time (e.g. late arrival due to pooling and hence possible rerouting) is perceived as almost twice as worse than waiting for the vehicle".

### Industry and paratransit

- **[9] Uber, "Introducing Delayed Ride Guarantee"**, 3 Aug 2026, https://www.uber.com/us/en/blog/delay-ride-guarantee/ [full].
  - "if the ride runs 5 minutes or longer than the original estimate, your fare will increase".
  - The exclusions include "Matched Share Rides".
- **[10] Uber, UberX Share page**, https://www.uber.com/us/en/ride/uberx-share/ [full].
  - "help make sure any additional pickups won't increase your estimated arrival time".
- **[11] Lyft on-time pickup promise**, Fox TV Stations news article, 13 Nov 2023, https://www.fox5ny.com/news/lyft-schedule-airport-rides-on-time-or-theyll-pay-you [secondary news].
  - "more than 10 minutes late … $20 in Lyft credit". Applies to scheduled airport rides only.
- **[12] DREDF/TranSystems 2010**, https://dredf.org/ADAtg/OTP.shtml [WebFetch; matches the prior audit].
  - "A pickup window of 30 minutes or less is standard in the industry."
- **[13] NYC Comptroller 2016**, Access-A-Ride audit [prior audit].
  - "$10.00 for each trip that occurred fifteen (15) minutes or more past the Scheduled Pickup Window".
- **[14] Via, Topeka proposal 2022** [prior audit].
  - "dynamically reassign any trips that may be in jeopardy of missing a committed time window".

### DARP and simulation

- **[15] Schulz & Pfeiffer 2026**, OR Spectrum 48:541–586, DOI 10.1007/s00291-026-00847-0 [full].
  - p.10: "li− = Bi− + l sets the deadline for any delay of customer i".
  - p.22: "900 s (15 min), which is also done this way in practice"; "In preliminary tests, a factor of 0.5 was reasonable".
  - p.29: "even for a maximum time shift of 30 min the average fraction of rejected customers does not decrease below 0.38"; "A reasonable trade-off is to set the maximum time shift to a value of 10 to 15 min."
- **[16] Lu & Kühnel 2024**, TU Berlin VSP WP 24-16, https://svn.vsp.tu-berlin.de/repos/public-svn/publications/vspwp/2024/24-16/LuKuehnel2024DrtConstraintsStudy.pdf [full]. Kühnel is at MOIA.
  - p.4: "In the practice, a small buffer, such as 2 or 3 minutes can be given".
  - p.5: "we do not allow rejections"; the minimum fleet is set from the "95-percentile of waiting times".
  - Table 2, p.10 (Manhattan, 8,042 trips per day): raising wait from 300 s to 900 s takes the fleet from 101 to 82; raising γ from 300 s to 900 s takes it to 92.
- **[17] Fielbaum & Alonso-Mora 2020**, TR-C 121:102831, DOI 10.1016/j.trc.2020.102831 [full]. Numbers in S2.
- **[18] Alonso-Mora et al. 2017**, PNAS 114:462, DOI 10.1073/pnas.1611675114 [full].
  - p.6: "Ω ∈{120, 300, 420} s. The maximum trip delay ∆ is double".
  - p.6: "Lower fleet size, larger capacity and longer waiting/delay times increase the possibilities for ride-sharing".
  - p.7: "about 90% of the rides were shared … slightly increases with ∆ and decreases with the fleet size".
  - p.5: a matched request "might be rematched … as long as its waiting time does not increase".
- **[19] Zwick & Axhausen 2020**, ITSC, DOI 10.1109/ITSC45102.2020.9294289 [full]. Numbers in S2.
- **[20] Zwick, Kuehnel & Hörl 2022**, TR-A 165, DOI 10.1016/j.tra.2022.09.001 [full].
  - p.5: "The maximum wait time is set to 10 minutes to ensure a good balance between an efficient and a user-friendly service. Zwick and Axhausen (2020b) have shown…".
- **[21] Santi et al. 2014**, PNAS 111:13290, DOI 10.1073/pnas.1403657111 [full].
  - p.3: "when Δ = 1 min, the Oracle model allows sharing of 94.5% of the trips, but the Online model only less than 30%".
  - p.5: "At around 100,000 trips, or 25% of the daily average, we already reach saturation".
- **[22] Tachet et al. 2017**, Sci. Rep. 7:42868, DOI 10.1038/srep42868 [full].
  - p.4: "∆/twait = λv²∆³/|Ω| = L".
  - p.3: "The greater the L, the greater the shareability."
- **[23] Molkenthin et al. 2020**, PRL 125:248302, DOI 10.1103/PhysRevLett.125.248302 [full].
  - p.2: "If x < 1, all requests can theoretically be served one by one … if x > 1 ride sharing becomes necessary". Here x = ⟨l⟩λ/(vB).
- **[24] Hyland & Mahmassani 2020**, TR-A 134:251, DOI 10.1016/j.tra.2020.02.017 [abstract only].
  - "efficiency gains stem from economies of demand density and network effects".
- **[25] Cordeau (2006) benchmark instances**, as described by:
  - **Dong et al., arXiv 2011.08993, p.22** [secondary]: "a 15-min time window … The maximum ride time L is set to be 30 minutes".
  - **Gschwind & Drexl 2016, JGU DP 1624, p.12** [full]: "at most 96 requests and 8 vehicles".

## S1. How to choose the cap

### (a) Perception and tolerance

- **No source measures whether riders notice changes of tens of seconds.**
  - Stated tolerances are minutes: the median is 4–6 min [3], and Via's frustration threshold is 10 min [1].
  - The finest bin anyone reports is "<1 min" (11% of respondents) [3].
- **Displays and accuracy norms are minute-scale.**
  - Lyft showed pickup ETAs in minutes, and they drifted by ≤1 min in 76.4% of sessions [2].
  - OneBusAway shows "now" for anything within 2 min [3].
  - Transit accuracy bands are about −0.26/+0.41 min at 0 min ahead and ±2.4 min at 10 min ahead [4], or ±1 min near term per MBTA [5].
  - Via's mean ETA error is 24 s [1]. So 30 s is about an operator's *mean* error, and about one-fifth of the 10-minute-ahead band (145 s) **[ours]**.
- **Pooling-induced arrival uncertainty is disliked, but small shifts carry little weight.**
  - MOIA respondents weigh it about 2× waiting [8].
  - Willingness to pay of 3.47–5.52 ct/min [7] values 30 s at about 1.7–2.8 ct **[ours]**.
  - Small unannounced shifts are "not fully accounted for" [6].

### (b) Industry

- **Compensation triggers at minutes, measured against the original estimate:** Uber 5 min [9]; Lyft 10 min [11]; Via 10 min [1]; NYC paratransit 15 min past the window [13].
- **Matched shared rides are excluded from Uber's guarantee [9].** Yet Uber's stated goal is that added pickups do not increase your ETA [10].
- **Practice buffers:** 2–3 min (MOIA-affiliated authors [16]); l = 15 min "in practice" [15]; paratransit windows of 30 min or less [12]; Via sells "committed time window[s]" [14].

### (c) DARP and simulation conventions

- Cordeau: 15-min windows and L = 30 min [25].
- Alonso-Mora: Ω = 2/5/7 min, with Δ = 2Ω [18].
- Fielbaum: wait 5 min and delay 10 min, inherited from Alonso-Mora [17, p.18].
- Zwick: 15 or 10 min wait, with additive-plus-multiplicative detour limits [19], [20].
- Lu & Kühnel: λ·t + γ, with a fixed latest arrival [16].
- Schulz & Pfeiffer: a deadline l from the first offer [15]. This is our closest analogue, but it is not cumulative and is 30× larger than our cap **[ours]**.

### (d) How papers justify their parameters

- **Inherited from a prior paper:** [17].
- **From an earlier sweep:** [20].
- **"Practice":** [15], [16].
- **Preliminary tests:** [15].
- **Rider feedback plus a tail quantile:** [1].
- **An explicit sweep and a stated knee:** [15] Finding 5; [19] Table IV; [16]; [18] Fig. 5. **This is the dominant and strongest pattern.**

### Three defensible ways to pick our cap

1. **Frontier knee (primary).**
   - Sweep the cap over {0, 30, 60, 120, 180, 300 s, locks-only, fully free}. Plot served, shared, wait and detour against promise stability, and report the knee ([15], [16], [19]).
   - The old 16-cell sweep already shows the shape **[ours]**:

     | Step | Change in served |
     |---|---|
     | Fully free → locks | −2.6 pp |
     | Locks → cap 120 s | −1.2 pp |
     | Cap 120 s → cap 60 s | −1.4 pp |
     | Cap 60 s → cap 30 s | −0.3 pp |

   - Most of the cost comes from the locks and the 120 → 60 s step. Confidence intervals are needed.
2. **Display invariance (defends 30 s as the conservative end).**
   - With 1-minute display buckets, any cumulative cap below 60 s means the displayed drop time never moves more than 1 minute from the first display **[ours]**.
   - A single shift of s seconds flips the bucket with probability s/60 under a uniform sub-minute phase. So 30 s flips it at most 50% of the time **[ours]**.
   - Together with [1], [2], [4] and [5], the claim is "within platform ETA noise". It is not a perception threshold ([3], [6]).
3. **Practice anchor (sensitivity point): 120–180 s.**
   - This matches the "2 or 3 minutes" buffer [16] and stays far below the 5–10 min triggers.
   - It costs 1.2 pp served, versus 2.9 pp for 30 s, both against locks-only **[ours]**.
   - Our median move is 108.6 s, so 120 s admits roughly the lower half of moves **[ours, assuming the no-cap move distribution]**.

## S2. What raises sharing, and how commitment interacts with it

### Verified numbers

**Fielbaum & Alonso-Mora 2020 [17]**
- Setting: 19,610 requests over 2 h, 2,000 vehicles of capacity 4, wait 5 min and delay 10 min, with reassignment and post-acceptance rejection allowed (pp.8–9).
- Rejection:

  | Scenario | Rejection | Source |
  |---|---|---|
  | Base | 34.5% | Table 1, p.9 |
  | 1,000 vehicles | 48.1% | Table 1, p.9 |
  | Fully controlled (no rejection after acceptance; wait fixed to first prediction) | 45.6% | Table 5, p.17 |
  | Intermediate | 31.2% | Table 5, p.17 |

- In the intermediate scenario wait and detour rise from 1.01 to 1.51 min and from 0.65 to 1.01 min.
- Users' cost: 9.56 → 10.3 → 11.6.
- Fn.12, p.9: "a very large fleet would offer non-shared trips to almost every user".
- Fn.13, p.17: forbidding in-vehicle detours "would turn the whole system in a (almost) non-shared one".
- **No shared-ride rate is reported anywhere** (I searched the full text and Tables 1–7).
- Inconsistency: the service rate is "66.5%" in the text on p.9 but 65.5% in the arithmetic on p.10.

**Zwick & Axhausen 2020 [19]**
- Base case: 15-min wait, 10 min + 1.5·t, 13,401 requests. They report an "acceptance rate of 0.43" (p.3).
- Detour factor 1.75 or 2.0: +12.7% or +22.2% rides. Ride time rises from 19:14 to 21:22 min at 2.0.
- Wait is non-monotone: the best maximum is 10 min, at +18.6%.
  - Their explanation (pp.4–5): "Once an agent is accepted by the system, the vehicle is assigned to a certain trip and has no flexibility".
- Public-transport stop network: +11.6% rides **[ours: 6,463/5,789]**.
- Time with at least 2 passengers on board: 26.2% in the base case and 37.3% with demand and fleet tripled **[ours: sums of p.4/p.5 figures]**.

**Lu & Kühnel 2024 [16]**
- Relaxing the wait limit cuts fleet about 2× more than relaxing the ride limit (−18.8% vs −8.9%) **[ours: ratio]**.
- A longer ride limit "increases the vehicle occupancy during peak hours, this does not necessarily correspond to a more efficient service" (p.1).

**Schulz & Pfeiffer 2026 [15]**
- Acceptance stays at or below 62% for every l **[ours: 1 − 0.38]**.

### Levers

| Lever | Evidence | Cost |
|---|---|---|
| Load x = λτ/B | [17], [18], [23]. Ours: 50.1% → 58.4% shared going from 8 to 4 vehicles | Rejections. Ours: 44.7% served |
| Density at constant load | [21], [22] (L ∝ λ/\|Ω\|), [19] §IV.D, [24] | Needs more requests per area |
| Detour slack | [18]; [19] +22.2% | About +2 min ride time |
| Wait slack | [16]; non-monotone under greedy commitment [19] | Wait |
| Information or batching horizon | [21] | Pre-booking or delayed commitment |
| Stop consolidation | [19] | Walking |
| Commitment and locks | [17] fn.13 and Table 5; [19] §IV.C; [15]. Ours: 50.1% → 22.8% (not same batch) | Sharing and service |

### Small-sim levers (≤128 requests, ≤32 vehicles, ≤96 nodes)

- **Load.** λ = 54 requests per hour, so 8 vehicles carry 6.75 requests per vehicle-hour. The load x crosses 1 at a mean direct trip time τ of 8.9 min with 8 vehicles and 4.4 min with 4 vehicles **[ours]**. Compute τ from the logs.
- **Raise x.** Sweep B ∈ {4, 5, 6, 8}, or compress the 108 requests into 1 h.
  - Published base cases run at 43% [19], about 65% [17] and at most 62% [15] acceptance. So a 45–65% served stress regime has precedent.
- **Raise density.** Use up to 128 requests, and place the nodes in a smaller area ([22], 1/|Ω|).
- **Loosen the ride cap.** Use an additive form such as 1.5·t + 5 min ([16], [19]) or 2.0·t. The cost is about 2 min of ride time.
- **Use a fixed-demand minimum-fleet design** at a p95 wait target with no rejections [16]. Sharing then comes from load rather than from rejection.
- **Scale is not an objection for algorithms, but it is for rates.** Classic DARP benchmarks are our size [25], but sharing rates are scale-dependent ([21]–[23]).

## S3. Recommendations

1. **Present the cap as an experimental parameter chosen at the knee of a sweep** ([15], [16], [19]). Report the whole frontier with confidence intervals.
2. **Defend 30 s only as the conservative, display-invariant end.** Below 60 s, the displayed drop time moves by at most 1 minute **[ours]**. That is about Via's mean ETA error [1]. Never claim riders perceive 30 s ([3], [6]).
3. **Report 120–180 s as the practice-anchored alternative** [16]. In the old sweep it costs 1.2 pp served, versus 2.9 pp for 30 s **[ours]**.
4. **Call no value an industry standard.**
   - Industry thresholds of 5 and 10 min, and windows of 15–30 min, compensate lateness against the original estimate. They are not dispatch-change caps.
   - Uber excludes matched shared rides from its guarantee ([9], [11]–[13]).
5. **Name Schulz & Pfeiffer's deadline l [15] and Lu & Kühnel's fixed latest arrival [16] as the nearest prior art.** Our difference is a cumulative budget that is about 30× tighter.
6. **Build the high-sharing regime by raising load and density, not slack alone.** Pre-register regimes by x (for example ≈1, 1.5 and 2), and report served, shared, wait and detour for every arm.
7. **Keep one 45–65% served stress regime,** which mirrors published base cases ([17], [19], [15]). Add a fixed-demand minimum-fleet regime [16], so sharing is not bought with rejections.
8. **Run the commitment ladder (free → locks → caps) inside each regime.** Commitment is known to suppress sharing ([17] fn.13, [19] §IV.C), so our 50.1% → 22.8% must be shown within one batch.
9. **Define sharing as Alonso-Mora do:** passengers who shared, divided by passengers picked up [18]. Cite no sharing rate from [17], because it reports none.
