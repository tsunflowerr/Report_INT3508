# SURVEY S1: pooling rate vs scale, and trade-off levers

Date: 2026-10-07. Claude literature agent; read-only except this file. 19 sources. Quotes are copied verbatim from PDF text that I extracted myself (PyMuPDF). Only ligatures, superscripts and, where noted, word spacing were normalised. "p." is the PDF page unless marked "jp." (journal page). `[abstract only]` means only the abstract was read; `[not checked]` means not verified. **[ours]** marks my own arithmetic, not a literature claim. I did not read `codex-work/`.

## S1. Pooling rate vs scale

### S1.1 Settings and reported pooling metrics

| # | Study | Demand / sample | Fleet × cap | Max wait | Max detour / delay | Pooling metric reported |
|---|---|---|---|---|---|---|
| 1 | Alonso-Mora 2017 | full NYC taxi, 383k–461k req/day | 1,000–3,000 × 1/2/4/10 | 2/5/7 min | total delay 2Ω | ≈90% shared rides |
| 2 | Santi 2014 | Manhattan 2011; subsampled to 1% of taxis | none (static matching) | Δ ≤ 10 min | Δ | % shareable (Oracle/Online) |
| 3 | Tachet 2017 | 4 cities, subsampled | none | Δ = 5 min | Δ | shareability S(L) |
| 4 | Simonetto 2019 | NYC 2013, 5/10/20% of demand | 150/300/600 × 4/10 | 7 min | 7 min | occupancy "rarely exceeds 2" |
| 5 | Fielbaum & Alonso-Mora 2020 | Manhattan, 2 h, ~20,000 req | 2,000 × 4 | 5 min | delay 10 min | rejection/unreliability only |
| 6 | FleetPy arXiv 2022 | Manhattan, June 2016, 10% | 380 × 4 | 360 s | +40% | none in text [figures not checked] |
| 7 | **FleetPy ETRR 2026 (Zenodo 15187906)** | **12 Nov 2018, 10%, 21,400 req/day** | **180 × 4** | **480 s** | **+40%** | **avg occupancy ≈1.33** |
| 8 | Shulika et al. (arXiv) | Manhattan 2016, 5%, 30-min batches | none (offline ExMAS) | utility | utility | 35–70% pooled at 400 trips/h |
| 9 | Lu & Kühnel 2024 | Midtown + Lower Manhattan, 8,042 trips/day | min fleet × 8 | 300–900 s | 1.5·t + γ | η_RP = PKB/VKT ≈1.00–1.12 |
| 10 | Zwick & Axhausen 2020 | Hamburg MOIA, 13,401 req/day | >100 × 6 | 15 min | 10 min + 1.5·t | time with ≥2 pax: 26.2% **[ours: sum]** |
| 11 | Fielbaum, Tirachini, Alonso-Mora 2023 | stylised circular city | endogenous | n/a | n/a | "little sharing" below ~250 pax/h |
| 12 | Molkenthin 2020 | synthetic | B buses | n/a | n/a | ⟨C⟩, ⟨O⟩ vs load x |

### S1.2 Evidence (verbatim)

**[1] Alonso-Mora et al., PNAS 114:462–467, DOI 10.1073/pnas.1611675114** (corrected author PDF https://autonomousrobots.nl/assets/files/publications/17-alonsomora-ridesharing-pnas.pdf).
- jp.467: "with our online method, about 90% of the rides were shared. The number of shared rides slightly increases with ∆ and decreases with the fleet size (Fig. 5E)."
- Fig. 5 caption, jp.466: "percentage of shared rides (number of passengers who shared a ride divided by the total number of picked-up passengers)". Whether "shared" means co-onboard is defined in the SI, which is [not checked].
- jp.466: "Lower fleet size, larger capacity and longer waiting/delay times increase the possibilities for ride-sharing and lead to higher mean vehicle occupancy."

**[2] Santi et al., PNAS 111:13290–13294, DOI 10.1073/pnas.1403657111** (https://steven-strogatz.squarespace.com/s/quantifying-the-benefits-of-vehicle-pooling.pdf).
- jp.13292: "when Δ = 1 min, the Oracle model allows sharing of 94.5% of the trips, but the Online model only less than 30%."
- jp.13294: "At around 100,000 trips, or 25% of the daily average, we already reach saturation and near-maximum shareability." This curve is computed in the **Oracle** model; the Fig. 3C caption says "in the Oracle model".
- SI p.17: "We varied c from 95% down to 1%, generating a number of trips per day as low as 1,962."

**[3] Tachet et al., Sci. Rep. 7:42868, DOI 10.1038/srep42868** (https://senseable.mit.edu/papers/pdf/20170306_Tachet_etal_ScalingLaw_NatureScientific.pdf). This is the scaling law.
- Article p.3: "∆/twait = λv²∆³/|Ω| = L". Article p.2: "The greater the L, the greater the shareability."
- Article p.1: "Two trips are defined to be shareable if they would incur a sharing delay of no more than ∆ minutes, relative to a single ride". This measures potential pairing. Whether it uses the Oracle or the Online model is [not checked] (SI).
- Table 2 caption, article p.4: "344.12 trips/h/km2 in New York … 0.95 in Vienna … generating a shareability of almost 100% for the first three and of 83% for Vienna." In Table 2 (Δ = 5 min, eight cities), the 0.5 trips/h/km² row runs 17–59% and the 2.5 row runs 60–97%.

**[4] Simonetto et al., TR-C 101:208–232, DOI 10.1016/j.trc.2019.01.019** (arXiv 1902.10676v1).
- p.14: 150/300/600 vehicles "correspond to 5%, 10%, and 20% of the maximum fleet size … For each fleet size, we consider the same percentage of ride requests".
- p.15: "the more vehicles we consider (and correspondingly the more customers), the more the service rate increases. This is because requests spatial density increases".
- p.17: "the average occupancy of the vehicles rarely exceeds 2".

**[5] Fielbaum & Alonso-Mora, TR-C 121:102831, DOI 10.1016/j.trc.2020.102831** (https://autonomousrobots.nl/assets/files/publications/20-Fielbaum-TRC.pdf).
- p.2: "during two hours (about 20,000 requests) in Manhattan."
- p.18: "Smaller fleets provide a much more unreliable service."

**[6] Engelhardt et al. 2022, arXiv 2207.14246.** p.11: "only a 10% subsample of all resulting trips are used". This run uses June 2016 data, not the Zenodo set.

**[7] Engelhardt et al., Eur. Transp. Res. Rev. 18:52 (2026), DOI 10.1186/s12544-026-00823-3.** This is the only study found on **our dataset**. p.14: "The input data are from the FleetPy Manhattan data set https://zenodo.org/records/15187906". The Zenodo record is by Engelhardt & Dandl, dated 10 Apr 2025.
- p.10: "The taxi data set for the week of 11/11/2018 to 11/18/2018 is used to create demand files."
- p.11: "based on a 10% sample of trip requests (21,400 requests) from 12 November 2018"; "The vehicle fleet consists of 180 vehicles, each with a capacity of four passengers."
- p.11: "the AM approach achieves the highest percentage of served users (90%)"; "The average occupancy rate for all vehicles throughout the day is approximately 1.33, compared to 1.31 for both IH and LA." Whether empty time is in the denominator is [not checked]. No shared-ride share is given.

**[8] Shulika, Bujak, Ghasemi, Kucharski, arXiv 2312.07191** (preprint; journal status [not checked]).
- p.4: "ExMAS is an open-source Python algorithm that solves the offline ride-pooling problem for rational travellers". There is no fleet constraint, so results are pooling potential.
- p.5: "trips per hour in Manhattan, which has an area of 60km2".
- pp.6–7: "intensive growth at initial phase of low demand values and gradual stabilisation as the demand goes beyond the levels of 200 trips per hour."
- p.7: "For the same demand level of 400 trip requests per hour … 35% to 70% of trips are pooled".

**[11] Fielbaum, Tirachini, Alonso-Mora, arXiv 2106.15270.** Published as Econ. Transp. 34:100313 (2023); the journal version was not read. p.13, word spacing restored: "reaches about 250 passengers/h. Until that point, the system operates almost as a private service, i.e., there is little sharing because it is difficult to find compatible users". This is a stylised model.

**[12] Molkenthin, Schröder, Timme, PRL 125:248302, DOI 10.1103/PhysRevLett.125.248302** (https://grk2767.tu-dresden.de/files/user/chair_nd/CFND_Publications/Molkenthin_PRL_2020.pdf).
- p.2: x is "the ratio of requested trip distance ⟨l⟩λ per unit time and the total bus driving distance vB per unit time"; "If x < 1, all requests can theoretically be served one by one".
- Fig. 2(c) caption: "At constant normalized load x the number of requests increases proportionally to the number of buses, thus also increasing the number of similar trips that can be shared efficiently."
- p.4: "the average occupancy related to the driving time as ⟨O⟩ = (x/τ)⟨Δtd⟩". This is equivalent to λ⟨Δt_d⟩/B.

**[10] Zwick & Axhausen, ITSC 2020, DOI 10.1109/ITSC45102.2020.9294289** (local PDF; https://www.moia.io/mobility_analytics/studies/2006_Impact_of_service_design_on_ride-pooling.pdf).
- p.5 §IV.D: "Doubling or tripling the number of requested rides and the vehicle fleet respectively leads to more than the double or triple of served rides in the system, because the demand density in the study area grows and the likelihood that trips are poolable increases."

**Excluded.** Vazifeh et al., Nature 557:534–538, DOI 10.1038/s41586-018-0095-1. I saw only metadata (IDEAS). It is a minimum-fleet study; I obtained no verbatim abstract, so it is [not checked] and not used.

### S1.3 Drivers of the pooling rate, per the sources

1. **Demand density, with fast saturation.** See Tachet, Santi, Shulika, Simonetto p.15, Zwick §IV.D and Fielbaum 2023.
2. **Load per vehicle.** Molkenthin's x. Alonso-Mora: sharing "decreases with the fleet size".
3. **Absolute size at the same load.** Molkenthin Fig. 2(c); Fielbaum 2020 on small fleets.
4. **Slack Δ/Ω.** Santi Fig. 3B; Alonso-Mora Fig. 5E.
5. **Online vs offline information.** Santi: 94.5% vs <30%.
6. **Dispatcher.** Mahfouz 2026, p.15: "batch-based algorithms generally achieve higher pooling rates". FleetPy 2026: occupancy 1.33 vs 1.31.

### S1.4 Placing our cell (all **[ours]**)

- **Request rate.** 108 requests / 2 h = **54 req/h**.
- **Against FleetPy 2026, same data.** 21,400 req/day ≈ **892 req/h** as a day average, about 16.5× ours; by sample fraction (10% vs 0.4%) about 25×. Requests per vehicle-hour are 6.75 for us vs ≈4.95 for FleetPy. **Per-vehicle load is similar, density is 16–25× lower.** That points to density/scale, not an oversized fleet.
- **Against Shulika.** 54 trips/h is about ¼ of their ~200/h stabilisation level, so we sit in the steep part. The value at 54/h was not read off their figure.
- **Against Tachet.** *If* our 96 nodes span ~60 km² (coverage not verified), density ≈ 0.9 trips/h/km², about 1/380 of NYC 2011 and near Vienna (83% potential). That is an upper bound on pairing, not a realised share.
- **Against Santi and Fielbaum 2020.** Our 0.4% is below Santi's lowest 1% subsample, and Fielbaum 2020 has about 185× our requests per 2 h.
- **To compute.** x = λτ/B, with τ the mean direct time. Check ⟨O⟩ = λ⟨Δt_d⟩/B against our logs.
- **Definitions.** Our "another rider on board" may differ from Alonso-Mora's definition, and FleetPy's 1.33 is occupancy, not a share of riders.

## S2. Trade-off levers and how they are reported

### (a) Wait and detour tuning

- **Zwick & Axhausen.** p.1: "The adjustment of the maximum waiting time or the maximum allowed detour can increase or decrease the pooling efficiency by around 20 %." p.4: "Decreasing the value to 10 minutes, 6,868 passengers (+ 18.6 %) can be transported". The response is non-monotone (Table IV); they explain it by greedy commitment.
- **Lu & Kühnel 2024**, TU Berlin VSP WP 24-16 (https://svn.vsp.tu-berlin.de/repos/public-svn/publications/vspwp/2024/24-16/LuKuehnel2024DrtConstraintsStudy.pdf; journal status [not checked]). p.1: "increasing permissible waiting time is more effective in reducing the required fleet size … compared to allowing a longer permissible ride duration." In their Manhattan Table 2 (p.10), raising wait from 300 s to 900 s cuts the minimum fleet from 101 to 82 (−18.8%); raising γ from 300 s to 900 s cuts it to 92 (−8.9%).
- **Bilali et al. 2020**, TRR 2674(6), DOI 10.1177/0361198120917666. I saw it only as cited by Zwick 2020, p.1: "the maximum waiting time and detour time have the highest impact". The primary paper is [not checked].
- **Ke et al. 2021**, TR-C 124:102922, DOI 10.1016/j.trc.2020.102922 [abstract only]: "pool-matching probability … and number of passengers in the matching pool … can be fitted by some simple curves".
- **Lobel & Martin 2025**, Mgmt Sci 71(2):1716–1736, DOI 10.1287/mnsc.2020.03125 [abstract only, IDEAS]: "the density of ride requests is far more important than detours".

### (b) Frontier reporting

- **Explicit Pareto frontier.** Lobel & Martin [abstract only]: "a tight bound on the Pareto frontier of values and detours … including one based on ride-sharing data from commute hours in Manhattan."
- **Multi-metric grid.** Alonso-Mora Fig. 5 plots service rate, delay, wait, distance, % shared and compute over fleet × capacity × Ω.
- **Policy table.** Fielbaum 2020 Table 5, p.17: rejection goes from 34.5% (Base) to 45.6% (Fully controlled), and "the more controlled the unreliability, the higher the average users' costs."
- **Fixed demand.** Lu & Kühnel, p.5: "we do not allow rejections"; "minimum required fleet size is determined based on the 95-percentile of waiting times". They also fix wait + γ at 1,200 s and vary the split.
- **Distance efficiency.** Mahfouz 2026, J. Urban Mobility 9:100219, DOI 10.1016/j.urbmob.2026.100219, p.9 defines OSE as "the ratio of Passenger Kilometres Booked (direct distance) to Vehicle Kilometres Travelled". Mahfouz is in the corpus but is about **service-area design, not commitment**.
- **Dispatcher trade-off.** FleetPy 2026, p.11: "strategies that achieve higher service rates may do so at the cost of longer waiting times."

### (c) Time-window tightening and commitment

- **Alonso-Mora**, jp.465: "its latest pickup time is reduced to the expected pickup time by that vehicle … A request might be rematched … as long as its waiting time does not increase".
- **Fielbaum 2020**, p.17: "her maximum waiting time is updated to the predicted one." Footnote 13: "if in-vehicle detours are not admitted, actual sharing would occur only at very specific circumstances … eliminating UD by these means would turn the whole system in a (almost) non-shared one."
- **Lu & Kühnel**, p.5: "the latest arrival time t*arrival,latest will also remain fixed."

### (d) Slack in promised times

- **Schulz & Pfeiffer 2026**, OR Spectrum 48:541–586, DOI 10.1007/s00291-026-00847-0.
  - jp.550: "li− = Bi− + l sets the deadline for any delay of customer i".
  - jp.551: "the offer contains the scheduled arrival time Bi− as well as the latest possible arrival time li−."
  - jp.569: "the effect quickly diminishes as the time shift increases"; "even for a maximum time shift of 30 min the average fraction of rejected customers does not decrease below 0.38".
  - Finding 5: "A reasonable trade-off is to set the maximum time shift to a value of 10 to 15 min." This is their model's choice.
- **Lu & Kühnel.** The wait/ride buffer split is a form of promise slack.
- Among these 19 sources I found no "pooling reserve" placed inside a *displayed* ETA. This is a search result, not a claim of absence.

## S3. Conclusions

- **Our low sharing rate is broadly explained by scale/density.** Every density-scaling source reports steep growth and then saturation. Our cell is 16–25× sparser than FleetPy 2026 on the same data and about 185× sparser than Fielbaum 2020 **[ours]**. Alonso-Mora's ~90% is a full-demand figure with 1,000–3,000 vehicles, not a benchmark for a 0.4% cell.
- **No source gives a number for our regime.** Santi stops at 1%, Tachet is a potential bound, and FleetPy 2026 reports occupancy only. So 22.8% is "consistent with", not "validated by", the literature.
- **Small fleet size is a separate handicap.** Molkenthin Fig. 2(c) and Fielbaum 2020 point to it. We should report x = λτ/B and check ⟨O⟩ = λ⟨Δt_d⟩/B.
- **The 22.8% → 13% drop under caps is the expected direction.** Fielbaum 2020 (Table 5, footnote 13) and Schulz & Pfeiffer (Fig. 7) show that protecting announced times shrinks the feasible set. Reviewers will read it as a trade-off if it is shown explicitly.
- **Expected frontier.** Sweep the promise allowance (no cap plus several caps, like Schulz & Pfeiffer's l) and ideally the wait cap. Plot promise stability (late-vs-promise, ETA revisions, ledger burden) against efficiency: served share or rejections, shared-ride share, PKB/VKT, wait and ride delay.
- **Add a fixed-demand run.** A Lu & Kühnel-style run (no rejections, minimum fleet at a p95 wait target) turns the cost of promises into vehicles.
- **Add a scale-sensitivity row.** Scale demand and fleet together (e.g. 0.4%, 1%, 2.5%, 10%), as Simonetto and Zwick §IV.D do. Otherwise reviewers can attribute every result to toy scale.
- **Claim boundary.** Post-assignment tightening, first-offer protection, fixed deadlines and announced latest arrival plus l all already exist (Alonso-Mora, Fielbaum 2020, Lu & Kühnel, Schulz & Pfeiffer). Do not present them as novel, and define each metric explicitly.
