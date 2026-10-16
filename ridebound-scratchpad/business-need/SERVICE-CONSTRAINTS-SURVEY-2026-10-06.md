# Service-constraint survey: pickup window, ride-time limit, capacity, fleet/demand (2026-10-06)

Purpose: prepare the answer to the examiner question *"Why a 10-minute pickup window, a maximum in-vehicle (ride) time of 1.5 x direct travel time, capacity 4, and 8 vehicles for 108 requests per 2 hours? How do other papers set these?"*

## 0. Scope, method and reading rules

**RideBound values being defended** (verified in code, read-only):

- Pickup window `[arrival, arrival + 600 000 ms]`: `src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs:444`.
- Max ride time: `max(direct, round_half_even(direct x 1500/1000))`, at `FleetPyManhattanNormalizer.cs:429-445`. It is checked as *drop-off time minus actual pickup time*, at `src/RideBound.Domain/Validation/PhysicalPlanValidator.cs:594`. So it is an **in-vehicle** limit of 1.5 x the direct time. Waiting time is not included in it.
- Capacity 4, 8 vehicles, 108 requests in a 2 h window: these come from the caller's question and the 2026-10-06 provenance note (`constraint-provenance-2026-10-06.txt`). Derived load: 54 requests/h, **6.75 requests per vehicle-hour**, mean inter-arrival time about **67 s** (my arithmetic).

**Method:**

- I only cite sources that I opened in this session.
- Access routes were WebFetch, and Europe PMC full-text XML for PMC papers.
- I extracted text from PDFs with `pypdf`. Some PDFs were open-access copies already stored locally under `E:/RideBoundData/...`; each such case is noted.
- Quotes are verbatim. Ligatures (fi/fl) and line-break hyphenation are normalized. Symbols lost in PDF extraction are shown in `[brackets]`.
- Anything I saw only in a search snippet is listed in section 7 and **not used**.

**Evidence levels used:** simulation; optimization study (benchmark); empirical-network analysis; survey / stated preference (SP); field data / field experiment; product policy; vendor claim; regulation; contract / audit; agency policy / guidance; software default.

**Comparing constraints:** papers define the "same" constraint in different ways, so they cannot be compared one-to-one.

| Family | Definition | Who uses it |
|---|---|---|
| A | Absolute max wait Ω plus absolute max **total** delay Δ. Δ includes the wait. | Alonso-Mora 2017 (Δ = 2Ω); Simonetto 2019; Fielbaum 2020/2021; Santi 2014 / Tachet 2017 (one Δ for pickup and delivery delay) |
| B | Max wait plus a **relative in-vehicle** limit: ride ≤ (1 + f) x direct | FleetPy (f = 40 %, i.e. 1.4 x (direct + boarding)); Engelhardt et al.; **RideBound (1.5 x)** |
| C | Max wait plus **total travel time** (wait + ride) ≤ α x direct + β, or detour ≤ min(β + α x direct, cap) | MATSim DRT: Bischoff 2017; Zwick 2020/2022; Mahfouz 2026 |
| D | DARP: pickup/arrival **time windows** (e.g. 15 min wide) plus an **absolute** max ride time L | Cordeau 2006 benchmark; paratransit practice |
| E | Deadline / time-shift: once accepted, the arrival may slip by at most *l* | Schulz & Pfeiffer 2026 (*l* = 15 min) |
| F | Utility-based acceptance with no hard cap | ExMAS (Kucharski & Cats 2020) |

---

## 1. Q1: Parameter values in the literature

### 1.1 Summary table

Abbreviations: "req" = requests, "veh" = vehicles, "n.v." = not verified (value not found in what I could open).

| # | Paper (year, venue) | City / data | Max wait | Max detour / delay / ride | Capacity | Fleet vs demand | Stated justification | Evidence |
|---|---|---|---|---|---|---|---|---|
| R | **RideBound** | FleetPy Manhattan (Nov 2018) derived | **10 min** window from request | **in-vehicle ≤ 1.5 x direct** | **4** | **8 veh / 108 req / 2 h** (6.75 req/veh-h) | to be argued | n/a |
| 1 | Santi et al. (2014, PNAS; arXiv 1310.2963 opened) | NYC taxi 2011 | (folded into Δ) | Δ = max delay at pickup and delivery. Network built with Δ up to 10 min; results at Δ = 1, 2, 5 min | k = 2, 3 trips per shared ride | no fleet; network-level | absolute delay "more valuable than percent"; Δ = 2 min called "low and reasonable" | empirical-network analysis |
| 2 | Ma, Zheng & Wolfson (2013, ICDE, T-share) | Beijing GPS, 33,000 taxis | pickup window 5 min | delivery window = pickup late bound + average OD travel time | n.v. | 2,980 taxis, 9:00–9:30 am; query/taxi ratio up to about 6 | "e.g. 5 minutes" (none) | simulation |
| 3 | Tachet et al. (2017, Sci. Rep.) | NYC, SF, Singapore, Vienna | (folded into Δ) | Δ = 5 min headline | pairs of trips | no fleet | none explicit | empirical-network analysis |
| 4 | Alonso-Mora et al. (2017, PNAS) | Manhattan, 1 week of May 2013; 382,779–460,700 req/day | Ω ∈ {2, 5, 7} min | Δ = 2Ω total delay incl. wait (4/10/14 min) | {1, 2, 4, 10} | {1,000; 2,000; 3,000} veh vs 13,586 active taxis | none ("for example, 2 min") | simulation + optimization |
| 5 | Simonetto, Monteil & Gambella (2019, TR-C) | Same NYC week (+ Melbourne) | δ = 7 min | detour Δ = 7 min | C = 4 or 10 | 150/300/600 veh with 5/10/20 % of requests; also 2,000/3,000 veh with full demand | none | simulation |
| 6 | Fielbaum & Alonso-Mora (2020, TR-C) | Manhattan, weekdays 1–3 pm, 19,610 req / 2 h | 5 min | 10 min total delay | 4 (also 3, 5, mixed) | base 2,000 veh (1,000; 1,600; 5,000 variants) | "taken from Alonso-Mora et al. (2017)" | simulation |
| 7 | Fielbaum, Bai & Alonso-Mora (2021, TR-C) | Manhattan, 9,970 req / 1 h | Ωw = 5 min | Ωd = 10 | 6 (also 9) | 3,000 (or 2,000) veh | "(from Alonso-Mora et al., 2017)", "(from Ota et al., 2016)" | simulation |
| 8 | Ota et al. (2016/17, IEEE T-BigData, STaRS) | NYC 2011–12, 360 M trips | n.v. | n.v. (Fielbaum 2021 cites Ωd = 10 from Ota) | n.v. | 13,000 taxis (abstract) | n.v. | simulation |
| 9 | Cordeau (2006, Oper. Res.) DARP benchmark, read via Ropke, Cordeau & Laporte (2007, Networks) | random Euclidean | 15-min time windows | L = 30 min (Q = 3) / 45 min (Q = 6), absolute | 3 or 6 | 2–8 veh, 16–96 req, horizon 480–720 min (e.g. a8-96: 8 veh, 96 req) | n.v. in the opened source | optimization benchmark |
| 10 | Bischoff, Maciejewski & Nagel (2017, IEEE ITSC) | Berlin taxi, 27,336 req/day | 15 min | total travel ≤ α x direct + β; α 1.1–2.1, β 0–1080 s; best α = 1.5/β = 240 s or α = 1.7/β = 120 s | 2, 3, 4 | base case 4,212 taxis (varying shifts) | runs kept only if service not worse than non-shared base | simulation |
| 11 | Zwick & Axhausen (2020, STRC) | Hamburg, MOIA one day, 12,427 req | 10 and 15 min | detour 5 min + 50 % of direct | 4 seats (MOIA runs 6-seaters) | 50–300 veh | scenario design | simulation |
| 12 | Zwick, Kuehnel & Hörl (2022, TR-A) | Hamburg, MOIA historic requests | 10 min | detour = min(5 min + 0.5 x direct, 15 min) | 6-seaters | 254 (autonomous) / 280 (shifts) veh | "good balance between an efficient and a user-friendly service" | simulation |
| 13 | Mahfouz et al. (2026, J. Urban Mobility) | Leeds, MATSim, 24 h | 10 min | total travel ≤ 1.5 x direct + 5 min | 4 | 50/100/200/500 veh | TfL (2021) trials; Avermann & Schlüter (2019); Zwick et al. (2022) | simulation |
| 14 | Engelhardt, Dandl & Bogenberger (2020, arXiv 2007.14877) | Munich private-car OD, 1.2 M trips/day, adoption 1–15 % | 8 min (min wait 2 min) | detour ratio 40 % | 4 | fleet = 200 x D | none | simulation |
| 15 | Engelhardt, Dandl, Syed et al. (2022, arXiv 2207.14246, FleetPy) | Manhattan taxi June 2016, 10 % sample | 360 s | relative detour 40 % | 4 | 380 veh | none | simulation |
| 16 | Engelhardt, Malcolm, Dandl & Bogenberger (2022, arXiv 2205.04319) | Manhattan taxi Nov 11–18, 2018 (same source as the FleetPy Zenodo data), 10 % penetration | 6 min | +40 % travel time vs direct | 4 | sweep 75–250 veh per operator; 190 needed each | none | simulation |
| 17 | Engelhardt, Mahmassani & Bogenberger (2023, arXiv 2308.05507) | Chicago TNC 2023-06-07, 20 % of 127,528 trips | 6 min | 40 % | 4 | 300 veh (about 90 % served with repositioning) | none | simulation |
| 18 | FleetPy repo (TUM-VT; local commit 053aa9d, 2026-03-13) + Zenodo 15187906 | Manhattan example (Nov 2018 data); also Chicago, Munich, generic example | Manhattan/Chicago/Munich 480 s; example 300 s; SoD 900 s; documented default "very large" | `op_max_detour_time_factor` 40 (in-vehicle ≤ 1.4 x (direct + boarding)); SoD 150 + 300 s; documented default "None (Infinity)" | default vehicle type 4 | Manhattan: 80 veh for a 5 % sample, 180 veh for a 10 % sample | none | software default/config |
| 19 | Schulz & Pfeiffer (2026, OR Spectrum) | Hamburg district, 120 virtual stops, average direct 8.5 min | no hard wait cap (acceptance = e^(−0.5·RD)) | delivery-deadline shift l = 15 min (varied 0–30) | 6 | k ∈ {6, 8, 10} veh; n = 100–1000 req; inter-arrival 30/60/90 s | "also done this way in practice"; 10–15 min recommended | optimization + simulation |
| 20 | Kucharski & Cats (2020, TR-B, ExMAS) | Amsterdam (repo default config: Delft) | no hard cap: utility-based | utility: discount 0.3, WtS 1.3 (default config) | not stated as a cap | 3,000 travellers become 1,900 rides | behavioural utility | strategic matching (offline) |

### 1.2 Source notes with verbatim evidence

**[1] Santi, Resta, Szell, Sobolevsky, Strogatz, Ratti. "Quantifying the benefits of vehicle pooling with shareability networks." PNAS 2014.**
- Opened: arXiv PDF https://arxiv.org/abs/1310.2963 (full text).
- Evidence: empirical-network analysis (simulation of sharing).
- Quote: "the quality of service parameter ∆, which stands for the maximum delay a customer tolerates in a shared taxi service trip, mathematically equivalent to the notion of "time window" used in other approaches"
- Quote: "The choice of defining the quality of service parameter as an absolute time, instead of as a percentage increase of the travel time, is in line with similar realizations in the literature [17], and is motivated by the fact that absolute delay information is likely more valuable than percent estimation of travel time increase for potential customers of a shared taxi service."
- Quote: "Using a maximum value of ∆ = 10 min and all trips performed in New York City in the year 2011" … "even with the low and reasonable value of ∆ = 2 min, the average percentage of shareable trips is close to 100%" (Oracle model).

**[2] Ma, Zheng, Wolfson. "T-Share: A Large-Scale Dynamic Taxi Ridesharing Service." ICDE 2013.**
- Opened: camera-ready PDF https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICDE13_conf_camera-ready_clean.pdf
- Evidence: simulation.
- Quote: "[l_pickup] can be easily obtained by adding a fixed value, e.g. 5 minutes, to [birth time]."
- Table II: "The number of taxis 2,980"; "The pickup window size 5 minute"; simulation 9 am to 9:30 am.
- Delivery window, quote: "[late bound of the delivery window] equals to the sum of the late bound of the pickup time window and the average travel time between the origin and destination pair learned from the GPS trajectory dataset."
- Capacity: n.v.
- Note: the camera-ready abstract says "serves 25% additional taxi users while saving 13% travel distance compared with no-ridesharing (when the ratio of the number of queries to that of taxis is 6)". The MSR landing page (https://www.microsoft.com/en-us/research/publication/t-share-a-large-scale-dynamic-taxi-ridesharing-service/) instead says "40% additional taxi users while saving 15% travel distance". Cite the camera-ready numbers.

**[3] Tachet, Sagarra, Santi, Resta, Szell, Strogatz, Ratti. "Scaling law of urban ride sharing." Scientific Reports 7:42868 (2017).**
- Opened: Europe PMC full text PMC5337932 (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5337932/fullTextXML).
- Evidence: empirical-network analysis.
- Quote: "taxi trips in New York City offer a shareability well above 95% for Δ = 5 min"
- Quote: "Even for low trip density, and allowing delays no longer than Δ = 5 minutes, the potential for sharing is massive."
- Justification of 5 min: none explicit.

**[4] Alonso-Mora, Samaranayake, Wallar, Frazzoli, Rus. "On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment." PNAS 114(3):462–467 (2017).**
- Opened: Europe PMC full text PMC5255617, plus the local PDF copy `E:/RideBoundData/research/pdf-20260824-wp14/alonso-mora-2017-pnas.pdf`.
- Evidence: simulation + optimization.
- Quote: "maximum waiting time Ω, for example, 2 min" … "a maximum travel delay ∆, for example, 4 min"
- Quote: "We analyze several metrics, with different vehicle fleet sizes (m∈{1,000, 2,000, 3,000} vehicles), vehicle capacities (χ∈{1, 2, 4, 10} passengers), and maximum waiting times (Ω ∈{120, 300, 420} s). The maximum trip delay ∆ is double the maximum waiting time and includes both the waiting time ω and the inside-the-vehicle travel delay."
- Quote: "This dataset contains for each day the time and location of all of the pickups and drop-offs executed by each of the 13,586 active taxis"
- Justification: none beyond "for example".

**[5] Simonetto, Monteil, Gambella. "Real-time city-scale ridesharing via linear assignment problems." TR-C 2019.**
- Opened: arXiv HTML https://arxiv.org/html/1902.10676, plus the local PDF `E:/RideBoundData/literature-survey-2026-10-06/pdf/simonetto-trc2019-arxiv.pdf`.
- Evidence: simulation.
- Quote: "We consider that each trip has constraints on the maximum delay δ and detour time ∆, with δ = 7 minutes, and ∆ = 7 minutes."
- Quote: "Numerical simulations with 150, 300, and 600 vehicles, which correspond to 5%, 10%, and 20% of the maximum fleet size considered in Alonso-Mora … For each fleet size, we consider the same percentage of ride requests"
- Capacity: "(either C = 4, or C = 10)".

**[6] Fielbaum, Alonso-Mora. "Unreliability in ridesharing systems: Measuring changes in users' times due to new requests." TR-C 121:102831 (2020), CC BY.**
- Opened: local open-access PDF `E:/RideBoundData/literature-survey-2026-10-06/pdf/fielbaum-alonso-mora-2020-unreliability.pdf` (DOI https://doi.org/10.1016/j.trc.2020.102831).
- Evidence: simulation.
- Table 6, quote: "Max. waiting times and delay are taken from Alonso-Mora et al. (2017)." … "Max. admissible waiting time 5 [min]"; "Max. admissible delay 10 [min]".
- Quote: "The basic scenario considers 2000 vehicles capable of carrying 4 passengers at a time, as in Alonso-Mora et al. (2017). Removing all requests that have more than 4 passengers leaves a total of 19610 requests for the two hours period."

**[7] Fielbaum, Bai, Alonso-Mora. "On-demand ridesharing with optimized pick-up and drop-off walking locations." TR-C 126:103061 (2021).**
- Opened: TU Delft repository PDF https://repository.tudelft.nl/file/File_f943215b-d52e-49fe-ab9d-0bd74250566d
- Evidence: simulation.
- Quote: "Regarding the restrictions, we take Ωw = 5 [min] (from Alonso-Mora et al., 2017), Ωd = 10 (from Ota et al., 2016), and we define Ωa = 12 [min]."
- Quote: "(i) 3000 vehicles of capacity 6 (considered as the base scenario …). (ii) 2000 vehicles of capacity 9."
- Quote: "a real dataset of Manhattan taxi trips (9970 requests during one hour)".
- This paper shows the **citation-chain** practice: values are inherited from earlier papers, not derived from users.

**[8] Ota, Vo, Silva, Freire. "STaRS: Simulating Taxi Ride Sharing at Scale." IEEE Trans. Big Data (DOI 10.1109/TBDATA.2016.2627223).**
- Opened: abstract only, via the OpenAlex record https://api.openalex.org/works/doi:10.1109/tbdata.2016.2627223
- Quote: "We evaluate our framework through a study that uses data about 360 million trips taken by 13,000 taxis in New York City during 2011 and 2012."
- **Parameter values: not verified** (full text not opened). The only trace is the secondary statement in [7] above.

**[9] Cordeau (2006), "A branch-and-cut algorithm for the dial-a-ride problem," Operations Research. Instance description read in Røpke, Cordeau, Laporte (2007), "Models and branch-and-cut algorithms for pickup and delivery problems with time windows," Networks 49(4):258–272.**
- Opened: DTU Orbit PDF https://backend.orbit.dtu.dk/ws/portalfiles/portal/3154678/ (reference [6] there = Cordeau 2006).
- Evidence: optimization benchmark.
- Quote: "These instances have narrow time windows of 15 minutes. In the first set ('a' instances), qi = 1 for every request i and the vehicle capacity is Q = 3. In the second set ('b' instances), qi belongs to the interval [1, 6] and Q = 6. These data are described in detail in [6] … Finally, L denotes the maximum ride time."
- Table 5 rows, e.g.: "a8-96 8 96 720 3 30" and "b8-96 8 96 720 6 45" (|K| vehicles, n requests, H minutes, Q, L minutes).

**[10] Bischoff, Maciejewski, Nagel. "City-wide shared taxis: A simulation study in Berlin." IEEE ITSC 2017.**
- Opened: DepositOnce PDF https://depositonce.tu-berlin.de/handle/11303/8600
- Evidence: simulation (MATSim DRT).
- Quote: "The overall time spent on traveling (waiting, boarding and riding) must not exceed tr = α t_direct_r + β"
- Quote: "An overall of 180 simulation runs were conducted: 60 runs per capacity (2, 3 or 4) with the maximum travel time defined by α ranging between 1.1 and 2.1 and β between 0 and 1080 seconds. Furthermore, we set the maximum wait time twait to 15 minutes."
- Quote: "we assume that the overall service quality indicators, namely TW, TW95 and ρ, should not be worse than in the non-shared one."
- Base case, quote: "A total of 27 336 requests are handled by 4 212 vehicles (all of them have different service times)."

**[11] Zwick, Axhausen. "Analysis of ridepooling strategies with MATSim." STRC 2020.**
- Opened: https://www.strc.ch/2020/Zwick_Axhausen.pdf
- Evidence: simulation with MOIA demand.
- Quote: "In this work we analyse scenarios with a maximum wait time of 10 and 15 minutes and a maximum detour of 5 minutes + 50% of the direct ride time."
- Quote: "We take 12,427 requests that MOIA had on a particular day … and serve it with different fleet sizes from 50 to 300." … "define the size of the vehicles to have 4 seats although MOIA operates with 6-seaters in Hamburg."

**[12] Zwick, Kuehnel, Hörl. "Shifts in perspective: Operational aspects in (non-)autonomous ride-pooling simulations." TR-A 165:300–320 (2022), CC BY.**
- Opened: local open-access PDF `E:/RideBoundData/literature-survey-2026-10-06/pdf/zwick-kuehnel-hoerl-2022-operational-aspects.pdf`.
- Evidence: simulation calibrated on MOIA (first author affiliated with MOIA GmbH).
- Quote: "The maximum wait time is set to 10 minutes to ensure a good balance between an efficient and a user-friendly service. Zwick and Axhausen (2020b) have shown for a similar historic MOIA scenario in Hamburg that a further increase of the maximum wait time leads to higher average wait times but does not increase the system efficiency substantially."
- Quote: "t_detour = min(t_constant + α·t_direct, t_max)". Table 2: "Max. wait time 10 min", "Absolute detour time t_constant 5 min", "Relative detour factor α 0.5", "Maximum absolute detour t_max 15 min".
- Quote: "the entire fleet of 254 6-seater vehicles".

**[13] Mahfouz, Balac, Morgan, Lovelace, Heinen. "Assessing trade-offs in demand-responsive transport service area design." Journal of Urban Mobility 9:100219 (2026), CC BY.**
- Opened: local open-access PDF `E:/RideBoundData/literature-survey-2026-10-06/pdf/mahfouz-et-al-2026-service-area.pdf` (DOI https://doi.org/10.1016/j.urbmob.2026.100219).
- Evidence: simulation (MATSim, Leeds).
- Quote: "Following Zwick et al. (2022), maxWaitTime is set to 10 min to balance efficiency with user friendliness. This threshold aligns with user tolerance levels observed in empirical trials (TfL, 2021) and satisfaction studies (Avermann & Schlüter, 2019), which show acceptance dropping significantly beyond 10 min. For maxTravelTime, we adopt the scaling values from Zwick et al. (2022) (αtravel = 1.5 and βtravel = 5 min) to implicitly limit detours."
- Quote: "fleet sizes: 50, 100, 200, and 500 vehicles, each with a capacity of four passengers."
- This is the **closest published parallel to RideBound's 10 min / 1.5 x / capacity 4**. Note that its 1.5 x bounds wait + ride and adds 5 min.

**[14] Engelhardt, Dandl, Bogenberger. "Speed-up heuristic for an on-demand ride-pooling algorithm." arXiv:2007.14877 (2020).**
- Opened: local PDF `E:/RideBoundData/research/pdf-20260820/engelhardt-dandl-bogenberger-2020-speed-up-heuristic.pdf`.
- Evidence: simulation (Munich).
- Table 1, quote: "minimal waiting time tmin_wait 2 minute", "maximal waiting time tmax_wait 8 minute", "acceptable detour ratio ∆detour 40 %", "vehicle capacity µ 4 pax", "fleet size m 200·D vehicle".
- Quote: "We assume that the maximum detour time δ is related to the travel time of the direct route … δ = ∆detour·t_direct".

**[15] Engelhardt, Dandl, Syed, Zhang, Fehn, Wolf, Bogenberger. "FleetPy: A modular open-source simulation tool for mobility on-demand services." arXiv:2207.14246 (2022).**
- Opened: arXiv PDF.
- Evidence: simulation.
- Quote: "The service provider operates a fleet of 380 vehicles with capacity 4 … Schedules have to fulfill a maximum waiting time constraint of 360s and a maximum relative detour constraint of 40%."
- Quote: "only a 10% subsample of all resulting trips are used to generate the MoD customers in the simulation".

**[16] Engelhardt, Malcolm, Dandl, Bogenberger. "Competition and cooperation of autonomous ridepooling services: Game-based simulation of a broker concept." arXiv:2205.04319 (2022).**
- Opened: arXiv HTML.
- Evidence: simulation.
- Quote: "the operators employ vehicles with maximum traveler capacity c_v = 4. Additionally, they only offer trips to customers that do not exceed (i) a maximum waiting time of t_wait^max = 6 min and (ii) a relative increase in travel time Δ = 40% compared to the duration of a direct trip."
- Quote: "Conducting simulations for fleet sizes ranging from 75 to 250 reveals 190 vehicles are needed for each operator to achieve this service rate."
- Demand: NYC taxi trips inside Manhattan, Nov 11–18, 2018, subsampled to "a 10% market penetration".

**[17] Engelhardt, Mahmassani, Bogenberger. "Predictive vehicle repositioning for on-demand ride-pooling services." arXiv:2308.05507 (2023).**
- Opened: arXiv PDF.
- Evidence: simulation (FleetPy, Chicago).
- Quote: "The operator employs vehicles with capacity c_v = 4. The maximum waiting time constraint is set to t_wait^max = 6min, while a maximum relative detour of ∆det_max = 40% is used. In the base case 300 vehicles are used that serve around 90% of the demand when repositioning is applied."

**[18] FleetPy repository and Manhattan data.**
- Opened sources:
  - https://raw.githubusercontent.com/TUM-VT/FleetPy/main/studies/manhattan_case_study/scenarios/const_cfg_manhattan_case_study.yaml
  - Local checkout `E:/RideBoundData/wp7/FleetPy-1.0.2` (commit 053aa9d, 2026-03-13): `Input_Parameters.md` lines 69–75; `src/fleetctrl/planning/PlanRequest.py:86-88`; `src/fleetctrl/planning/VehiclePlan.py:356-366`; `data/vehicles/default_vehtype.csv`; `studies/*/scenarios/*`.
  - Zenodo record https://zenodo.org/records/15187906
- Evidence: software default/config.
- Upstream config (verbatim): `op_min_wait_time: 0`, `op_max_wait_time: 480`, `op_max_detour_time_factor: 40`.
- Documentation (verbatim):
  - `op_max_wait_time … maximum waiting time for request [s] … very large`
  - `op_max_detour_time_factor … maximum detour time factor in % … None (Infinity)`
- Code (verbatim): `max_trip_time = (100 + max_detour_time_factor) * max_trip_time / 100`, where max_trip_time starts as `self.init_direct_tt + boarding_time`. It is checked from boarding: `pax_infos[rid][0] + self.max_trip_time_dict[rid]`, documented as `(boarding_time, deboarding time)`. So **FleetPy's 40 % means in-vehicle time ≤ 1.4 x (direct + boarding)**, the same family as RideBound's 1.5 x.
- Vehicle type: `maximum_passengers,4`.
- Manhattan scenarios: `default_vehtype:80` with `2018-11-12_sample_5_*.csv`.
- paper_2025_applications: `default_vehtype:180` with `2018-11-12_sample_10_1.csv`, also with 480 s / 40.
- Other shipped configs: generic examples `op_max_wait_time,300` / `op_max_detour_time_factor,40`; SoD example `900` / `150` / `op_add_constant_detour_time,300`; Chicago and Munich case studies `480` / `40`.
- Zenodo: "FleetPy: Input Data for Manhattan Case Study", Engelhardt & Dandl, 2025-04-10. The record states no service constraints.

**[19] Schulz, Pfeiffer. "Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem." OR Spectrum 48:541–586 (2026).**
- Opened: local PDF `E:/RideBoundData/literature-survey-2026-10-06/pdf/schulz-pfeiffer-2026-customer-oriented-darp.pdf` (DOI https://doi.org/10.1007/s00291-026-00847-0).
- Evidence: optimization + stochastic simulation.
- Quote: "The vehicle capacity Q is assumed to be 6, which is in line with practical applications."
- Quote: "The number of customers was set to n ∈ {100, 250, 500, 750, 1000} and the number of vehicles to k ∈ {6, 8, 10}." … inter-arrival "90, 60 and 30 s".
- Quote: "The maximum allowed shift of a customer's time window l, i.e. the length of the delivery node's time window, is set to 900 s (15 min), which is also done this way in practice."
- Quote: "A factor of 0.5 means that a relative detour of 100% is accepted with a probability of roughly 60%." (RD includes waiting.)
- Note: with k = 8 and a 60 s inter-arrival time this is almost the **same load as RideBound** (8 veh, about 67 s).

**[20] Kucharski, Cats. "Exact matching of attractive shared rides (ExMAS) for system-wide strategic evaluations." TR-B 139:285–310 (2020).**
- Opened: TU Delft repository abstract https://repository.tudelft.nl/record/uuid:7602da0f-44f0-46e7-834a-7a80ed1ae63f and the default config https://raw.githubusercontent.com/RafalKucharskiPK/ExMAS/master/ExMAS/data/configs/default.json
- Evidence: strategic offline matching.
- Abstract, quote: "The premise of ride-sharing is that service providers can offer a discount, so that travellers are compensated for prolonged travel times and induced discomfort".
- Config (verbatim): `"shared_discount": 0.3`, `"WtS": 1.3`, `"pax_delay": 15`, `"horizon": 1200`.

---

## 2. Q2: Studies that vary the parameters, and the trade-offs they report

**Santi et al. 2014 (Δ and k).** Source [1].
- Quote: "when ∆ = 1 min, the Oracle model allows sharing of 94.5% of the trips, but the Online model only less than 30%."
- Quote: "When ∆ = 5 min, the Online model can exploit virtually all available trip sharing opportunities"
- Quote: "When ∆ = 5 min, we can save 32% of total travel time with the Online model, compared to 40% savings in the optimal Oracle model."
- Quote: "increasing the number k of shareable trips provides noticeable benefits only when the quality of service parameter ∆ crosses a threshold around ∆crit≈ 150 sec" … "When ∆ = 300 sec, the number of saved taxi trips is increased from about 50% with k = 2 to about 60% with k = 3".
- Lesson: the gain from looser delay saturates by about 5 min in dense NYC. Capacity above 2 only helps once delay tolerance is large enough.

**Alonso-Mora et al. 2017 (Ω, capacity, fleet).** Source [4].
- Quote: "a fleet of 1,000 vehicles with a capacity of 10 can satisfy almost 80% of the requests with Ω = 420 s, compared with below 30% for a single-rider taxi, for a net gain of over 50%. However, with a larger fleet of 3,000 vehicles and Ω = 120 s, the benefit is only about 15%."
- Quote: "if longer waiting times and delays are allowed, Ω = 420 s, a fleet of 3,000 vehicles with a capacity of 2, 4, and 10 could serve 94, 98, and 99% of the demand."
- Quote: "3,000 vehicles with a capacity of 2 and 4 could serve 94 and 98% of the demand, with a mean waiting time of 3.2 and 2.7 min and a mean delay of 1.5 and 2.3 min, respectively."
- Quote: "the in-car travel delay does increase with the increase in vehicle capacity … Nonetheless, that increase seems practically negligible—well below 100 s—once ride-sharing is allowed."
- Quote: "increasing the vehicle capacity not only increases the service rate but also reduces the mean distance traveled by the vehicles in the fleet"
- Quote: "The number of shared rides slightly increases with ∆ and decreases with the fleet size"
- Quote: "Lower fleet size, larger capacity and longer waiting/delay times increase the possibilities for ride-sharing and lead to higher mean vehicle occupancy."

**Bischoff, Maciejewski, Nagel 2017 (α, β, capacity; Berlin).** Source [10], Table I.
- Rows: C, α, β, mean wait T_W, P95 wait, mean ride T_R, …, total km d_T, …, λ. λ is fleet km divided by the sum of direct km.
  - Non-shared base: "1 base case 04:32 11:51 15:08 … 233 040 … 1.17".
  - C = 4, α = 1.5, β = 240 s: "4 1.5 240 03:52 10:08 18:21 … 195 764 … 0.98".
  - C = 4, α = 1.7, β = 360 s: "4 1.7 360 04:27 11:55 20:35 … 190 082 … 0.94".
- Looser limits therefore lower fleet-km (−16 % to −18 % vs base, my arithmetic from those rows) at the cost of longer rides (18:21 to 20:35 mean ride vs 15:08 non-shared).
- Quote: "The actual savings vary between 15 and 22%, with less rejected requests than in the base case." … "while these values may be preferable from an operators perspective, they tend to create longer overall travel times. This indicates once more the need for an operator to weight out between passenger comfort and fleet performance."
- On capacity, quote: "the differences between capacity 3 and 4 are not very high" … "the chance of carrying four requests at the same time are slim, mostly due to tight time constraints".

**Schulz & Pfeiffer 2026 (deadline shift l = 0…30 min).** Source [19].
- Quote: "We varied the time shift between 0, 5, 10, 15, 20, 25, and 30 min (with 15 being the value we used for all other tests)."
- Quote: "While the difference between l = 0 and l = 5 is fairly large, the difference between l = 10 and l = 15 is already much smaller." … "even for a maximum time shift of 30 min the average fraction of rejected customers does not decrease below 0.38."
- Quote (Finding 5): "A small maximum time shift leads to significantly higher rejection rates while a larger maximum time shift makes the system unattractive for accepted customers. A reasonable trade-off is to set the maximum time shift to a value of 10 to 15 min."

**Fielbaum & Alonso-Mora 2020 (fleet and capacity at fixed 5/10 min).** Source [6], Table 1.

| Scenario | Rejection rate | Avg. wait (min) | Avg. detour (min) | Avg. delay (min) |
|---|---|---|---|---|
| 2,000 x 4 (base) | 34.5 % | 1.01 | 0.65 | 1.66 |
| 1,000 x 4 | 48.1 % | 1.21 | 0.73 | 1.94 |
| 2,000 x 3 | 37.8 % | 1 | 0.52 | 1.52 |
| 1,600 x 5 | 36.8 % | 1.12 | 0.82 | 1.95 |
| 5,000 + double rejection penalty | 2.29 % | 1.42 | 1.39 | 2.8 |

- Unreliability, abstract quote: "more than one third of the requests that are not immediately rejected face some change" … "not allowing for reassignments may increase the number of rejected requests."

**Fielbaum, Bai & Alonso-Mora 2021.** Source [7].
- Quote: the waiting-time histogram "decreases towards the maximum waiting time (5 [min]) but slowly" … "This suggests that Ωw plays the most relevant role determining the rejected requests."
- So the **wait cap, not the delay cap, is the binding constraint** in their Manhattan runs.

**Zwick (MOIA) 2020/2022 (max wait 10 vs 15 min).**
- In [12], quote: "a further increase of the maximum wait time leads to higher average wait times but does not increase the system efficiency substantially." This is a secondary statement of Zwick & Axhausen 2020b.
- In [11] (opened), quote: "All pooling strategies can provide shorter wait times with a bigger fleet size" … "All other strategies are able to serve more than 80% of the requests with fleet sizes above 200 vehicles."
- The numeric 10-vs-15-min differences are in figures that I could not read as text: **n.v.**

**Tachet et al. 2017 (density).** Source [3].
- Shareability depends mainly on trip density. Quote: "Even for low trip density, and allowing delays no longer than Δ = 5 minutes, the potential for sharing is massive."

**T-share 2013 (demand/fleet ratio, fixed 5-min window).** Source [2].
- Quote: "all ridesharing methods have a considerably higher satisfaction rate (about 25% higher on average) than the NR method for all delta values" … "ridesharing methods save up to 13% in travel distance, depending on delta".
- Here "delta" is the *query inflation multiplier* (demand/fleet ratio), not a delay.

**Simonetto et al. 2019 (scaled fleet and demand).** Source [5].
- Quote: "These results show that, even for small fleet sizes, if the number of customers is scaled accordingly, then the performance of the service is almost not affected."
- This supports using a *scaled-down* instance (such as 8 veh / 108 req) **if** the demand/fleet ratio is kept comparable.

**ExMAS (utility instead of caps).** Sources [20] and [21].
- [20] abstract, quote: "In the case of Amsterdam, 3000 travellers offered a 30% discount form 1900 rides achieving an average occupancy of 1.67 and yielding a 30% vehicle-hours reduction at the cost of halving service provider revenues and a 17% increase in passenger-hours."
- [21] Soza-Parra, Kucharski, Cats, "The shareability potential of ride-pooling under alternative spatial demand patterns," Transportmetrica A (Europe PMC PMC10898289, opened).
  - Simulation, 1,000 req/h, Amsterdam.
  - Reports vehicle-hour reductions "18 and 59%" depending on demand pattern and trip length (WebFetch extraction; only the numbers were checked).

**FleetPy paper (behavioural acceptance of wait).** Source [15], simulation assumption, not evidence.
- Quote: "the offer is always accepted if the offered waiting time is lower than 240s, from 240s to 360s the acceptance probability decreases linearly, and waiting times longer than 360s are never accepted. As expected, Fig. 5a shows that less customers are served in the latter scenario".

**Summary of directions (consistent across studies):**
- Looser wait or detour limits raise the served share and pooling (occupancy, shared-ride share) and lower fleet-km per passenger.
- The same looser limits raise mean wait and ride time.
- Gains show diminishing returns: Santi at Δ ≈ 5 min; Schulz & Pfeiffer between 10 and 15 min.
- Larger capacity matters mainly when the fleet is small and the limits are loose.
- The wait cap usually drives rejections (Fielbaum 2021).

---

## 3. Q3: Practice, regulation and stated/revealed preferences

### 3.1 Product policies (ride-hailing pooling)

- **UberX Share product page**: https://www.uber.com/us/en/ride/uberx-share/ (product policy).
  - "Designed to add 8 minutes to your trip on average."
  - "Your driver will only wait for 2 minutes at your pickup spot."
  - "You can only request one seat on UberX Share."
  - "Because of traffic and other possible delays, we cannot guarantee arrival times."
- **Uber Newsroom, "Introducing UberX Share" (2022)**: https://www.uber.com/us/en/newsroom/uberx-share/ (product announcement).
  - "we'll only match riders heading in the same direction."
  - "riders arrive no more than 8 minutes later than an UberX ride."
  - "riders will receive an upfront discount … get up to 20% off the total fare, if matched with a co-rider along the way."
- **Lyft exit from pooling**: The Spokesman-Review, reprinting Bloomberg, 2023-05-11, https://www.spokesman.com/stories/2023/may/11/lyft-will-discontinue-pooled-rides/ (news quoting the company CEO).
  - "The problem with shared trips is that they take people out of their way" … "At some point, you have to pay attention to what your customers want."
- **Via, proposal to Topeka Metro (RFP TM-22-01, 2022)**: https://www.topekametro.org/uploads/8JyQTWqA/Proposal-ViaMobilityLLCforPosting.pdf (vendor claim).
  - "Via aggregates riders in real time, so new trips may be added along the way, but no one will ever be taken on a detour of more than a few minutes."
  - "a rolling optimization occurs to dynamically reassign any trips that may be in jeopardy of missing a committed time window."

### 3.2 Microtransit agency policy, procurement and guidance

- **LA Metro, 2025 Transit Service Policies & Standards (adopted 2025-07-17), Section 5 "Metro Micro"**: https://busstophub.metro.net/wp-content/uploads/2025/10/TSP-2025-Adopted-7-17-2025.pdf (agency policy).
  - "each rider would have to wait no more than 15 minutes from the time a reservation is made to when they are picked up at a designated pickup location, to facilitate pickup within a 10-minute window"
  - "Metro Micro generally serves short trips of approximately 20 minutes in vehicle time and 1-5 miles in distance on average."
  - "The largest vehicles have a seating capacity for up to 10 passengers"
  - "Microtransit works best with zones 20 square miles or smaller".
  - This is a public operator using a **10-minute pickup window**.
- **N-CATT guidebook "When to choose microtransit?"**: https://n-catt.org/guidebooks/on-demand-transit-and-microtransit-where-and-why/when-to-choose-microtransit/ (guidance).
  - "Microtransit buses could be defined as having an 'on-time' arrival if they arrive within 15 minutes of the projected pick-up time."
- **Yolo County Transportation District, RFP 22-01 Microtransit Technology Platform (2022-02-15)**: https://yolobus.com/wp-content/uploads/2022/03/YCTD-RFP-22-01-Microtransit-Technology-Platform.pdf (procurement document).
  - Lists among the parameters to be set per zone: "Wait time parameters" and "Maximum detour time parameters".
  - Asks bidders whether "wait time, maximum detour time, fares" "can be configured or customized for each zone".
  - Shows that agencies treat these as **tunable policy parameters**, not fixed constants.

### 3.3 Paratransit regulation, guidance, contract and audit

- **49 CFR 37.131 (ADA complementary paratransit service criteria)**, LII text: https://www.law.cornell.edu/cfr/text/49/37.131 (regulation).
  - (b): "The entity may negotiate pickup times with the individual, but the entity shall not require an ADA paratransit eligible individual to schedule a trip to begin more than one hour before or after the individual's desired departure time."
  - (f), prohibited capacity constraints: "Substantial numbers of significantly untimely pickups for initial or return trips; Substantial numbers of trip denials or missed trips; Substantial numbers of trips with excessive trip lengths."
- **National RTAP ADA toolkit**: https://www.nationalrtap.org/Toolkits/ADA-Toolkit/Service-Type-Requirements/ADA-Complementary-Paratransit-Requirements (guidance).
  - "they may not, however, require any eligible rider to schedule a trip for more than one hour before or after their desired trip time."
  - "trips with excessive trip lengths (time on board the vehicle in comparison to the length of a similar trip using the fixed route system)".
- **DREDF, ADA Topic Guide on On-Time Performance**: https://dredf.org/ADAtg/OTP.shtml (guidance by a disability-rights organization).
  - "A pickup window of 30 minutes or less is standard in the industry."
  - "FTA has accepted pickup windows up to that length, and found 60 minutes to be too long."
  - Examples: Chicago "a 20-minute on-time window, from the scheduled pickup time to 20 minutes after"; Baltimore "a vehicle as on time if it arrives by 30 minutes after the scheduled pickup"; Miami-Dade "10 minutes before or 20 minutes after the scheduled pickup (-10/+20)".
- **NYC Comptroller, Audit FK15-098A, "Audit Report of the MTA's Oversight of the Access-A-Ride Program" (2016-05-17)**: https://comptroller.nyc.gov/wp-content/uploads/documents/FK15_098A.pdf (contract and audit).
  - "DSCs must pick up customers within 30 minutes of scheduled times, and BCSCs must pick up customers within 5 minutes of scheduled times."
  - "in a minimum of 92 percent of scheduled trips"
  - Liquidated damages: "the Contractor shall pay the Authority the sum of $10.00 for each trip that occurred fifteen (15) minutes or more past the Scheduled Pickup Window."
  - Incentive: "in any month in which the Contractor exceeds 95% On Time Performance, the Contractor will be paid an incentive payment of ten (10) cents per completed trip".
  - Ride time: "Maximum Ride Times: For each trip, Contractors must ensure that ride times fall within specified parameters which are based on trip mileage."
  - Note: the paratransit **ride-time limits are absolute and depend on mileage** (DARP family D), not a fixed factor.

### 3.4 Stated and revealed preference on waiting and detours

- **Alonso-González, van Oort, Cats, Hoogendoorn-Lanser, Hoogendoorn (2020), "Value of time and reliability for urban pooled on-demand services," TR-C 115:102621.**
  - Opened: TU Delft portal abstract https://research.tudelft.nl/en/publications/value-of-time-and-reliability-for-urban-pooled-on-demand-services
  - Evidence: SP, N = 1006, Netherlands.
  - "Results show in-vehicle VOT for pooled on-demand services to amount to 7.88–10.80 €/h."
  - "We also find waiting VOT (both before the trip and during the transfer stage) to be lower than values previously reported in literature."
  - "the reliability ratio (VOR/VOT ratio) for both the waiting stage and the in-vehicle stage being around 0.5."
- **Geržinič, van Oort, Hoogendoorn-Lanser, Cats, Hoogendoorn, "Potential of on-demand services for urban travel," Transportation (2022/2023).**
  - Opened: arXiv PDF https://arxiv.org/abs/2107.00882
  - Evidence: SP, N = 1,063, Netherlands.
  - Attribute levels (Table 2), on-demand "Flex": "Waiting time (min) … 1, 5, 9"; "In-vehicle time (min) … 8, 12, 16"; "Type of ride … Shared, private".
  - Quote: "respondents are willing to pay up to €1.45 (Sharing [FLEX] / Cost) more for a private trip" … "or travel up to 20 min longer in a private ride as opposed to a shared ride".
  - The Flex waiting-time parameter "turns out insignificant in all estimated MNL models". This is weak evidence that, within 1–9 min, waiting at home is not strongly penalized.
- **König & Grippenkoven (2020), "Travellers' willingness to share rides in autonomous mobility on demand systems depending on travel distance and detour," Travel Behaviour and Society 21:188–202.**
  - Opened: abstract only, OpenAlex record https://api.openalex.org/works/doi:10.1016/j.tbs.2020.06.010
  - Evidence: online SP, N = 150, Germany.
  - "The findings indicate that 90% of respondents would prefer to share a ride of 10 min if the discount was 50% or more compared to a private ride. A higher discount is needed to attract travelers to share rides if travel time and detour factor increase."
  - The detour-factor levels are **not verified** (full text not opened).
- **Cohen, Fiszer, Kim (2022), "Frustration-based promotions: Field experiments in ride-sharing," Management Science 68(4):2432–2464.**
  - Opened: local PDF `E:/RideBoundData/literature-survey-2026-10-06/pdf/cohen-fiszer-kim-2022-frustration.pdf`.
  - Evidence: field data and field experiment, Via NYC.
  - VGR = Via duration / Google car duration. Quote: "we decided to set a threshold of 2.0 on the VGR to define a frustrated experience. The occurrences where the VGR is greater than 2.0 are also very rare in our data set".
  - "We select a 10-minute threshold for ETA error for a ride to qualify as a frustration" … "ETA errors greater than 10 minutes occur in less than 0.34% of the rides".
  - Via describes its algorithm as "optimized to increase the utilization of vehicles while keeping detour levels minimal for all passengers".
- **Goldszmidt, List, Metcalfe, Muir, Smith, Wang (2020), "The value of time in the United States: Estimates from nationwide natural field experiments," NBER WP 28208.**
  - Opened: abstract page https://www.nber.org/papers/w28208
  - Evidence: field experiment with Lyft.
  - The experiments use "random variation in both wait times and prices to estimate a consumer's VOT with a data set of more than 14 million observations"; "the VOT is roughly $19 per hour".
- **Secondary only:** Mahfouz et al. [13] cite TfL (2021) trials and Avermann & Schlüter (2019) as showing "acceptance dropping significantly beyond 10 min". I did not open those primary sources.

---

## 4. Q4: Where RideBound's values sit

**Pickup window (10 min from request).**

- Car-pooling simulations on NYC taxi data use **2–8 min**:
  - 2/5/7 min (Alonso-Mora); 7 min (Simonetto); 5 min (Fielbaum; T-share window).
  - 6–8 min (Engelhardt et al.; FleetPy Manhattan/Chicago/Munich examples at 480 s).
- DRT/microtransit studies and MOIA-calibrated work use **10 min** (Zwick 2020/2022; Mahfouz 2026). Bischoff uses 15 min.
- LA Metro Micro uses a **10-minute pickup window** (and a 15-minute maximum wait from reservation).
- Paratransit uses **20–30 min windows**, with negotiation up to ±60 min (49 CFR 37.131; DREDF; Access-A-Ride contracts).
- **Verdict:** 10 min is within the common range. It is **looser than the dominant NYC ride-pooling simulations**, **equal to the microtransit/DRT convention**, and **much tighter than paratransit**.
  - The most-cited simulation papers are tighter: 5–7 min.
  - Operator practice for shared shuttles is 10–15 min.

**Ride-time limit (in-vehicle ≤ 1.5 x direct).**

- Relative in-vehicle limits nearby:
  - FleetPy 1.4 x (40 %) in all TUM/FleetPy studies (Engelhardt 2020–2023; FleetPy repo). Its SoD example uses 2.5 x + 300 s.
  - MATSim/MOIA: detour ≤ min(5 min + 0.5 x direct, 15 min) (Zwick 2022), i.e. **1.5 x + 5 min**, capped.
  - Mahfouz: wait + ride ≤ 1.5 x direct + 5 min.
  - Bischoff's best combinations were α = 1.5–1.7 with β = 120–240 s.
- Revealed frustration threshold: Via used **2.0 x** (door-to-door duration vs car) as "frustrated".
- **Verdict:** 1.5 x is **mid-range**: slightly looser than FleetPy's 1.4 x, but **tighter than the MOIA/MATSim convention**, because RideBound has no +5 min allowance.
  - Example (my arithmetic): direct 10 min gives RideBound a max ride of 15 min. Zwick allows 20 min, and Mahfouz allows wait + ride of 20 min.
- Absolute-delay papers (Δ = 4–14 min incl. wait) are tighter for long trips and looser for short trips; there is no single ordering.
- Paratransit/DARP uses absolute L (30/45 min in Cordeau) or mileage-based tables.

**Capacity 4.**

- **The modal value** for car-based pooling: Alonso-Mora base, Fielbaum 2020, all FleetPy/TUM papers, Zwick & Axhausen 2020, Mahfouz 2026; UberX Share sells one seat per request in cars.
- Van-based services use 6–10: MOIA 6; Schulz & Pfeiffer 6 "in line with practical applications"; LA Metro Micro up to 10. Classic DARP uses Q = 3/6.
- Bischoff found four simultaneous requests "slim" under tight time limits. With 10 min / 1.5 x, capacity 4 is unlikely to be the binding constraint, but this should be measured.

**Fleet vs demand (8 veh, 108 req / 2 h = 6.75 req/veh-h, inter-arrival about 67 s).** My arithmetic from the cited counts:

| Study | Load |
|---|---|
| Schulz & Pfeiffer 2026 | k = 8 with 60 s inter-arrival = 7.5 req/veh-h (range 5–15) |
| Alonso-Mora 2017 | about 5.3 to about 19 req/veh-h (day averages, 3,000 down to 1,000 veh) |
| Fielbaum & Alonso-Mora 2020 | 4.9 req/veh-h at 66.5 % service rate |
| Cordeau a8-96 | about 1 req/veh-h (planning horizon, paratransit-style) |

- RideBound's load is **ordinary for dynamic ride-pooling studies** and almost identical to the Schulz & Pfeiffer k = 8 / 60 s setting. Simonetto shows that small fleets behave similarly if demand is scaled proportionally.
- Caveat: req/veh-h ignores trip length and area.
- Most papers **sweep fleet size** (Alonso-Mora 1,000–3,000; Engelhardt 75–250; Mahfouz 50–500; Zwick 50–300). A single fixed 8-vehicle point is weaker than a small sweep.

**How the literature justifies values.**

- Most papers **give no justification**, or inherit values by citation chain:
  - Alonso-Mora "for example"; Fielbaum "taken from Alonso-Mora"; Mahfouz "Following Zwick".
- The few that justify, do so in two ways:
  - User-friendliness/efficiency balance: Zwick 2022; Mahfouz via TfL and satisfaction studies.
  - Practice: Schulz & Pfeiffer, "also done this way in practice".
- Santi argues for absolute rather than relative limits on communication grounds.
- So a defensible answer is:
  1. Our values sit inside the published range: they match MOIA/MATSim microtransit practice and LA Metro's 10-minute window, and sit between FleetPy's 1.4 x and MATSim's 1.5 x + 5 min.
  2. Values in this literature are conventions.
  3. We therefore report sensitivity (section 6).

---

## 5. Short answer for the examiner (draft)

"We follow the microtransit/DRT convention rather than the taxi-replacement convention:

- **10 min maximum wait.** This is used by MOIA-calibrated simulations (Zwick et al. 2022; Mahfouz et al. 2026) and is the pickup window in LA Metro Micro's service standard. Taxi-pooling studies on NYC use 2–8 min (Alonso-Mora 2017; FleetPy 6–8 min). Paratransit allows 20–30 min windows.
- **In-vehicle time ≤ 1.5 x direct.** This lies between FleetPy's 1.4 x and the MOIA/MATSim 1.5 x + 5 min. It is below the 2.0 x ratio Via treated as a frustrated ride.
- **Capacity 4.** This is the standard car-pooling value (Alonso-Mora base case; FleetPy default vehicle).
- **Load: 8 vehicles for 108 requests in 2 h (6.75 requests per vehicle-hour).** This is the same order as Schulz & Pfeiffer (8 vehicles, one request per minute).

Because the literature shows that served share, pooling and fleet-km depend strongly on these limits (Santi 2014; Alonso-Mora 2017; Bischoff 2017; Schulz & Pfeiffer 2026), we report a sensitivity analysis instead of claiming that one value is correct."

---

## 6. What trade-off experiments the literature suggests

| Parameter to vary | Suggested grid | Anchors in the literature |
|---|---|---|
| Max wait / pickup window | 5, 7, 10, 15 min | Alonso-Mora (2/5/7 min), FleetPy (6–8 min), MOIA (10 vs 15 min), Bischoff (15 min) |
| Max in-vehicle factor | 1.25, 1.4, 1.5, 1.75, 2.0 x, plus one "1.5 x + 5 min" (MATSim-style) variant | FleetPy (1.4 x), Bischoff (α 1.1–2.1), Via frustration (2.0) |
| Coupled tightening | (5 min, 1.4 x) / (10 min, 1.5 x) / (15 min, 1.75 x), in the spirit of Alonso-Mora's Δ = 2Ω | Separates wait-driven from detour-driven rejections; Fielbaum 2021 found wait dominates |
| Capacity | 2, 3, 4, 6 | Alonso-Mora, Bischoff (gain from 3 to 4 small), van services at 6 |
| Fleet size at fixed demand (or demand scaling at fixed fleet) | e.g. 6, 8, 10, 12 vehicles for 108 req / 2 h | Alonso-Mora, Engelhardt, Zwick, Mahfouz sweeps; Simonetto proportional scaling |
| Deadline / promise slack after acceptance | l = 0, 5, 10, 15 min | Schulz & Pfeiffer's l |

On the deadline/promise slack row:
- RideBound's commitment caps (tens of seconds) are a far tighter version of the same lever.
- Reporting rejection vs slack makes the cost of tight promises visible.
- Fielbaum & Alonso-Mora 2020 add that restricting reassignment raises rejections.

**Outcomes to report.** These are the standard set in the opened papers. Report each as a curve or Pareto front over the grid, with replications and seeds.

- **Service:** served share / rejection rate (all papers).
- **Waiting:** mean and P95 wait (Bischoff reports P95).
- **Ride time:** mean and P95 realized ride time, as minutes and as the ratio to direct. Also report the share of rides above 1.5 x and above 2.0 x (Via's VGR threshold).
- **Delay:** mean total delay = wait + extra in-vehicle time (Alonso-Mora, Fielbaum).
- **Pooling:** pooled-ride share and mean occupancy (Alonso-Mora, Zwick).
- **Fleet efficiency:**
  - vehicle-km;
  - empty-km share e_D;
  - λ = fleet-km / Σ direct-km (Bischoff; λ < 1 means more efficient than private cars);
  - passengers per vehicle-hour.
- **Reliability / promise stability:** share of requests whose promised times change, and the magnitude of change (Fielbaum & Alonso-Mora 2020).
- **Compute time per decision:** Alonso-Mora reports it grows with Ω.

---

## 7. Seen in search but not opened (NOT used as evidence)

- Lavieri & Bhat (2019), "Modeling individuals' willingness to share trips with strangers in an autonomous vehicle future," TR-A 124:242–261. Not open access; no abstract retrievable via Crossref or OpenAlex.
- König & Grippenkoven (2020): full text. A search snippet claimed a "20-minute ride with a 1.5-fold detour" acceptance of 85 %. **Not used**; only the abstract (section 3.4) was opened.
- Engelhardt, Dandl, Bilali, Bogenberger (2019), "Quantifying the benefits of autonomous on-demand ride-pooling: A simulation study for Munich," IEEE ITSC. The snippet says detour times were varied; not opened.
- Bilali, Engelhardt, Dandl, Fastenrath, Bogenberger (2020), TRR, "Analytical and agent-based model to evaluate ride-pooling impact factors"; Bilali's TUM dissertation (mediaTUM blocked access).
- Cordeau & Laporte (2003), TR-B tabu search. The snippet mentions MTC-based "realistic assumptions" and a max ride time "computed by using a maximum deviation factor". Not opened.
- Cordeau (2006), Operations Research, original article. Instance values were taken from Røpke–Cordeau–Laporte (2007) instead.
- Cordeau & Laporte (2007), Annals of OR, "The dial-a-ride problem: models and algorithms": Springer authorization redirect.
- Ho et al. (2018), TR-B DARP survey; Molenbruch et al. (2017), Annals of OR; Paquette et al. (2012), Transportation. All not open access.
- Ota et al., STaRS: full text (parameter values n.v.).
- MTA Access-A-Ride pages, MTA press release about moving from a 30- to a 20-minute window, and the MTA 2024 paratransit guide (HTTP 403).
- FTA Circular C 4710.1 PDF (HTTP 403). DREDF and National RTAP were used instead.
- Jackson (WY) START microtransit RFP: snippet "10-minute response time for at least 95 percent"; HTTP 404.
- Woburn (MA) RFP 26-20: snippet "average wait time not to exceed 20 minutes"; blocked.
- Green Bay Metro performance standards: snippet; HTTP 403.
- MOIA user statistics (Auto Bild / tourism pages): snippet only.
- Avermann & Schlüter (2019); TfL (2021) DRT trials. Cited by Mahfouz; not opened.
- König, Wirth, Grippenkoven (2021), Sustainability (MDPI 403). Frontiers (2023) secondary citation, not used.
