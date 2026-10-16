# R13 — O5 "For ML, can we find more data to train on?" (Claude-side data-source investigation)

Date 2026-10-09/10. Claude data-source agent. Read: `ROUND13-FACT-PACK.md`, `claude-work/ML-PILOT-SEALED.md`,
`claude-work/ml-pilot-report-a1-2026-10-08.txt`, `claude-work/SURVEY-S4-ml-eta-from-trips.md`, `optimize/FORECAST-REPORT.md`.
I did not open any `codex-work/R13-*` file. I ran no simulation and installed nothing. I deleted nothing. I touched no
repository, thesis or report file. Every web fact below was saved, as a schema page, dictionary PDF, parquet footer or
small CSV, into `claude-work/r13-ml-data-samples/` (below: `S/`). No row data of any trip file was downloaded.

Tags: **[V]** verified in a saved file or local file (file:line given); **[V-web]** verified from a URL whose content I
saved; **[UNVERIFIED]** not checked, or seen only in a secondary source.

---

## 0. Bottom line

1. **Yes, more data exists.** NYC TLC yellow taxi trips with second-level pickup and drop-off times and taxi zones are
   public, monthly, from 2009-01 to 2026-08. The FleetPy factor method is documented well enough to rebuild the
   15-min Manhattan factor for any of those weeks (§2, §3).
2. **But in this simulator, more training data cannot buy a measurable gain in lateness.** Under C-30 + forecast, the
   weekday residual is **2 late riders out of 1,471** (68 without the forecast). The only large residual is the snow
   afternoon of 15 Nov: **34 of 601** riders. That is one event, and Sep–Dec 2018 contains no other snow weekday (§4).
3. **What more data is good for:**
   - replacing the fragile 2-day forecast vintage (12 Nov was a federal holiday, and 13 Nov had 26.9 mm of rain) with
     a multi-week profile;
   - perhaps obtaining genuinely unseen test days.

   Both are robustness evidence for the existing storyline. Neither is an ML contribution (§5, §6).
4. **No public ride-hailing or ride-pooling trip dataset I could verify contains a quoted ETA.** The only verified
   public dataset that pairs a platform promise with the actual outcome is Meituan's food-delivery challenge data (§2.4).

---

## 1. What the simulator actually uses: the FleetPy traffic-factor files

Bundle root (below: `B/`) = `E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/`.
Script and output: `S/factor_inventory.py` → `S/factor-inventory-2026-10-09.txt`, and `S/factor_definition_checks.py` →
`S/factor-definition-checks-2026-10-09.txt`.

### 1.1 Coverage and resolution [V]

| File family (`B/networks/Manhattan_2019_corrected/`) | Days covered | Resolution | Columns |
|---|---|---|---|
| `2018-11-{12..18}_tt_factors.csv` | **12–18 Nov 2018 (7 days)**, 96 bins each | **15 min** (`simulation_time` 0…85500 s) | `simulation_time, time_interval, travel_time_factor, travel requests, average travel duration, standard error, 25%, 50%, 75%` |
| `2018-11-11_to_2018-11-18_tt_factors.csv` | 672 rows = days 1–7 after 11 Nov (86400…690300 s) | 15 min | as above; equals the 7 daily files bin by bin (7/7, inventory line 40) |
| `2018-11-{11..18}_tt_factors_hourly.csv` | **11–18 Nov (8 days)**, 24 rows each | 60 min | `simulation_time, travel_time_factor, speed, speed_nw` |
| `2018-11-{11..18}_mean_tt_factor_hourly.csv`, `2018-11-12_mean_tt_factor.csv` | one row per day | daily constant | `simulation_time, travel_time_factor` |

- **Correction to the fact pack wording ("8 days 11–18 Nov").** There are 8 days of hourly factors, but 15-min factors
  exist only for **7 days, 12–18 Nov**. `README_Manhattan.md:47` says of 11 Nov: "only used for warm-up, no tt-data
  available here".
- **Range of the 15-min factor.** Minimum 1.514 (12 Nov), maximum **7.977 (15 Nov)**. Per-day means:
  - 07–09 h: 2.71 (12 Nov), 3.34, 3.24, 3.17, 2.73 (16 Nov).
  - 14–17 h: **6.22 on 15 Nov**, against 3.16–4.17 on the other weekdays.

  Source: inventory lines 31–37.
- **Trips behind the factor.** The `travel requests` column sums to 202,568 trips on 12 Nov and 169,356 on 15 Nov
  (inventory lines 31, 34).

### 1.2 How the factor is defined [V / V-web]

**How FleetPy applies it.** `NetworkTTMatrix.py` is at `E:/RideBoundData/wp7/FleetPy-1.0.2/src/routing/`.
- It loads `travel_time_factor` keyed by `simulation_time` (:164–167).
- It switches to a new value piecewise-constantly when the simulation time passes a key (:211–220).
- It multiplies every free-flow time by the factor: `scaled_tt = tt * self.tt_factor` (:295).

So the factor is **one city-wide multiplier per 15 min**.

**Bundle README.** `README_Manhattan.md:28` [V]: "These factors have been calculated based on recorded travel times in
the NYC TLC trip record data. The factors are determined by scaling average free flow travel times to the travel times
of the reported trips." `networks/.../infos.txt:9` [V] says only "more infos ?".

**Exact formula: Syed et al. (2021), Supplementary Material §1, eq. (S1)** [V-web; excerpt saved as
`S/syed2021_DataSheet1_section1_excerpt.txt`]. Verbatim: "we sum the total duration of all trips in the data starting
within a 15-minute interval, denoted as tod data. Second, using the origins and destinations of the same trips, the
total trip duration is computed based on free-flow fastest-paths of OSM, represented as tod ff-fp. Then, for each
interval, the travel time factor … is defined as [tod data / tod ff-fp] (S1)". The same section adds that "the effect
of a winter storm on November 15th can be observed in the data".

**Filtering and node assignment: Syed et al. 2021 main text** [V-web, `S/syed2021_ffutr.txt:1189–1193`].
- "We only considered the trips originating and ending in the Manhattan borough. Furthermore, we filtered probable
  false trip records in the data with speeds below 1 m/s or above 30 m/s."
- "The NYC taxi data are disaggregated by assigning the pick-up and drop-off locations … to boarding nodes in the
  respective zones randomly."
- "the speeds of all links were scaled after every 15 min".
- Limitation stated by the authors (`:1273`): "we used simplistic scaling of travel times using the ratio of total
  travel duration … it does not represent reality."

**Provenance link** [V-web]. Engelhardt, Dandl and Bogenberger (2022), arXiv 2210.06972, `S/arxiv_2210.06972.txt:652`:
"the method described by [Syed et al., 2021] is used to compute scale factors … From 202569 overall trips". The bundle's
12 Nov `travel requests` sum is 202,568, which matches to within 1.

**My local consistency checks** [V; zero-run, bundle files only].
1. **Hourly files.** `travel_time_factor == speed_nw / speed` holds for all 192 hourly rows, with maximum relative
   difference 4.9e−16. The columns `speed` and `speed_nw` are undocumented, and so are their units.
2. **Bin alignment.** Bin b's `travel requests` matches the demand-file trips requested **in the same bin b** better
   than those in bin b−1:
   - mean |log ratio| 0.052–0.092 for the same bin, against 0.094–0.142 for the previous bin;
   - the same-bin count ratio is 0.91–0.95 per day.

   On 15 Nov the minimum is 0.78, which fits more trips being removed by the < 1 m/s filter during the snow
   (`factor-definition-checks-2026-10-09.txt:2–8`). **Implication:** a factor for bin b uses trips that *start* in b
   and finish later, so it is not fully observable in real time at the start of b (leakage note, §5).
3. **Formula check without the speed filter.** Σ(avg duration)/Σ(free-flow) over all demand-file trips of each bin,
   using `ff/tables/nn_fastest_tt.npy` (4411 × 4411), is above the published factor by a mean 4.07% (max 8.71%) on
   12 Nov and 5.37% (max 9.31%) on 15 Nov (inventory lines 61, 80). That is consistent with the published factor using
   speed-filtered trips (removing the slowest). An exact rebuild therefore needs the speed filter. Syed et al. do not
   state which distance the speed uses [UNVERIFIED].

### 1.3 Do FleetPy or its authors publish more factor days? [V-web / V]

- **Zenodo 10.5281/zenodo.15187906** ("FleetPy: Input Data for Manhattan Case Study", v1.0, 10 Apr 2025, CC BY 4.0)
  holds one file, `FleetPy_Manhattan.zip` (408.9 MB). The description reads "This data uses taxi trips in the week of
  11/11/2018 to 11/18/2018", and no other versions are listed. Read via WebFetch; the API JSON returned 403
  (`S/zenodo_15187906.json` is the 403 stub).
- **Local FleetPy 1.0.2 checkout.** It has **no factor-derivation script**: `src/preprocessing/` contains network,
  zone, demand and pubtrans tools only, and `tt_factor` appears only in the routing modules and two study configs. The
  Chicago study config names `2022-06-7_tt_factors_hourly.csv`
  (`studies/chicago_case_study/scenarios/const_cfg_chicago_case_study.yaml:6`); I did not check whether that file is
  published [UNVERIFIED].
- **Conclusion.** No more Manhattan factor days are published, but the method (§1.2) is public and can be re-applied
  to other TLC weeks.

---

## 2. Data sources

### 2.1 NYC TLC trip records [V-web: dictionaries, user guide, trip-record page, parquet footers]

The data dictionaries are `S/tlc_dd_*_v2_raw.txt` (dated 18 Mar 2025). The user guide is
`S/tlc_trip_record_user_guide.txt`. Footers were read by HTTP range requests (`S/parquet_footer_probe.py` →
`S/parquet-footer-probe-2026-10-09.txt`, `S/parquet-footer-probe-older-2026-10-09.txt`). Coverage comes from the
download links on `S/tlc_trip_record_page.html`.

| Dataset | Coverage (links on page, 2026-10-09) | Timing fields | Location | Pooling fields | Size, rows (one month) |
|---|---|---|---|---|---|
| Yellow | 2009-01 … 2026-08 | `tpep_pickup_datetime` "when the meter was engaged", `tpep_dropoff_datetime` "when the meter was disengaged" (yellow raw :12–13); `trip_distance` (:15) | `PULocationID/DOLocationID` taxi zones (:31–32); **no coordinates in the current parquet even for 2015-01 and 2016-06** (older footer probe) | none | 2018-11: 117.2 MB, **8,155,449 rows**; 2018-09: 115.5 MB, 8,049,094; Sep–Dec 2018 together 477 MB |
| Green | 2013-08 … 2026-08 | `lpep_pickup/dropoff_datetime` | zones; street hails only "above W 110 St/E 96th St in Manhattan and in the boroughs" (user guide :16, :94–97) | none | 2018-11: 11.1 MB, 673,287 rows |
| FHV | 2015-01 … 2026-07 | `pickup_datetime`, `dropOff_datetime` (fhv raw :9–10); drop-off reported from 2017 (user guide :22, :117–118) | `PUlocationID/DOlocationID` | `SR_Flag`: "For shared trips, the value is 1"; Lyft "also flags rides for which a shared ride was requested but another passenger was not successfully matched" (fhv raw :13–25) | 2018-11: 208.6 MB, **22,911,479 rows**, 7 columns (no request time, no miles) |
| HVFHV | **2019-02** … 2026-08 ("This law went into effect on Feb 1, 2019", hvfhs raw :7) | `request_datetime` "when passenger requested to be picked up"; `on_scene_datetime` "(Accessible Vehicles-only)"; `pickup_datetime`; `dropoff_datetime`; `trip_time` "Total time in seconds for passenger trip"; `trip_miles` (hvfhs raw :20–29) | zones | `shared_request_flag` "agree to a shared/pooled ride, regardless of whether they were matched"; `shared_match_flag` "share the vehicle with another passenger who booked separately at any point during the trip" (:42–47) | 2019-02: 513.1 MB, **20,159,102 rows**, 24 columns; 2019-11: 561.0 MB; 2025-06: 490.8 MB. **Feb 2019 – Feb 2020: 13 files, 7.10 GB** |

**Do Oct–Nov 2018 yellow trips have exact timestamps and zones?** Zones: yes [V], from the footer and the dictionary.

Timestamps: the footer shows `tpep_*_datetime` as INT64, but I did not decode the parquet logical type. Indirect
evidence for second-level resolution [V]: in the bundle's 12 Nov demand file (derived from these trips), `rq_time` has
68,113 distinct integer values, and every second-of-minute 0–59 occurs 3,420–3,736 times. So the times were not rounded
to minutes. Contrast Chicago (§2.2).

**Volume per Manhattan day** [V]: 213,996 demand rows on 12 Nov and 185,181 on 15 Nov (inventory lines 61, 80).

**No quote or ETA field** exists in any of the four TLC dictionaries [V].

**Publication cadence** [V-web, trip-record page]: "Trip data is published monthly … typically with a two-month delay".

**Real NYC pooling volume** [V; `S/tlc_shared_share.py` on `S/tlc_data_reports_monthly.csv`, the TLC monthly
indicators, all boroughs]. Column "Trips Per Day Shared" ÷ "Trips Per Day" for FHV - High Volume:

| Month | Shared share |
|---|---|
| 2018-11 | **23.2%** (160,672 of 691,379 per day) |
| 2019-02 | 23.9% |
| 2019-11 | 14.3% |
| 2020-02 | 13.0% |
| 2021-07 | 0.1% |
| 2022-12 | 1.7% |
| 2024-12 | 2.3% |
| 2026-07 | 0.8% |

Source: output lines 27, 30, 39, 42, 56, 66, 90, 109.
- The CSV does not define "shared" [UNVERIFIED: requested or matched].
- The same file shows an implausible 99.7% for FHV - Black Car in 2018-11, so the column should be treated with care.
- Schaller Consulting, using TLC monthly data [V-web, `S/schaller_favfact7.html`]: the pooled rate "increased from
  low-teens in early 2017 to about 25 percent in early 2018. But pooling rates have essentially leveled off since then."

### 2.2 Chicago Transportation Network Providers trips [V-web]

**Release descriptions** (data.gov pages harvested from the City, `S/datagov_transportation-network-providers-trips-2018-2022.html`
and `…-2025.html`).
- 2018–2022 release (id `m6dm-c72p`): "All trips, from November 2018 to December 2022 …".
- 2025- release (id `6dvr-xwnh`): "All trips, starting January 2025 …".
- Both: "Census Tracts are suppressed in some cases, and times are rounded to the nearest 15 minutes. Fares are
  rounded to the nearest $2.50 and tips are rounded to the nearest $1.00."
- A separate 2023–2024 release exists per search snippets; its id and contents are [UNVERIFIED], and its data.gov page
  returned 404.

**Columns.** These are official descriptions from the 2025- dataset's `columns.json`, via a Wayback snapshot of
2026-09-30, decoded to `S/chicago_tnp_2025_columns_wayback_20260930_decoded.json`.
- `trip_start_timestamp`: "When the trip started, rounded to the nearest 15 minutes."
- `trip_seconds`: "Time of the trip in seconds."
- `trip_miles`.
- `pickup/dropoff_census_tract` and `…_community_area`.
- `shared_trip_authorized`: "Whether the customer agreed to a shared trip with another customer, regardless of
  whether the customer was actually matched for a shared trip."
- `shared_trip_match`: "Whether the customer was actually matched to a shared trip."
- `trips_pooled`: "how many trips, including this one, were pooled. All customer trips from the time the vehicle was
  empty until it was empty again contribute to this count".

data.cityofchicago.org returned HTTP 403 to both curl and WebFetch. Whether the 2018–2022 release also has
`shared_trip_match` is [UNVERIFIED]; a secondary listing (Du 2020, `S/arxiv_2008.06050.txt`) shows "Shared trip
(true/false)" and "Trips pooled" only.

**Suppression** [V-web, Mucci & Erhardt 2022, `S/findings_34191.txt:26`]: "when a census tract pair has two or fewer
trips within a 15-minute window, the census tract for both trip ends is suppressed".

**Use for us.** Durations are exact, but start times are only to the nearest 15 min. That is fine for pooled-vs-solo
duration comparisons. It is unusable for 15-min factor building, and Chicago is not the simulated city.

### 2.3 Rebuilding the factor series for more weeks: what it takes

**Inputs.**
- Inside the bundle (local):
  - yellow trips Manhattan→Manhattan; the zone lookup `B/zones/Manhattan_Taxi_Zones/taxi+_zone_lookup.csv`;
  - node→zone `B/zones/Manhattan_Taxi_Zones/Manhattan_2019_corrected/node_zone_info.csv`;
  - free-flow table `B/networks/.../ff/tables/nn_fastest_tt.npy`.
- Method: random boarding node per zone, speed filter 1–30 m/s, factor = Σ duration / Σ free-flow over trips starting
  in each 15-min bin (§1.2).

**Volume.**

| Span | Files | Size | Use |
|---|---|---|---|
| Sep–Dec 2018 | 4 | 0.48 GB | pilot span |
| Jul 2016 – Feb 2020 (pre-COVID, zone-ID era) | 44 | 5.35 GB | longer span |

Sizes from HEAD requests [V]. Jan 2014 – Jun 2016 is also zone-only in today's parquet; I did not sum its sizes.

**Weather events available** [V; NOAA GHCND Central Park, `S/noaa_ghcnd_centralpark_2014-2020.csv`, metric units;
`S/noaa_event_days.py` → `S/noaa-event-days-2026-10-09.txt`].
- 15 Nov 2018: SNOW 163 mm.
- **13 Nov 2018 (a sealed forecast source day): PRCP 26.9 mm**.

| Period | Weekdays | Snow ≥ 1 in | Snow ≥ 3 in | Rain ≥ 20 mm (no snow) |
|---|---|---|---|---|
| Sep–Dec 2018 | 86 | **1 (15 Nov)** | 1 | 9 |
| Jul 2016 – Feb 2020 | 956 | 16 | **7** | 49 |
| Jan 2014 – Feb 2020 | 1,608 | 34 | 19 | 79 |

Federal holidays are not removed from the weekday counts.

**Validation gate (must come first).** Rebuild 12–18 Nov from raw TLC and compare per bin with the bundle. Seal a
threshold beforehand, for example a median |relative error| ≤ 3%. Random node assignment adds noise. The speed-filter
distance definition is unknown and must be chosen by this gate, not tuned on test days.

**Tooling gap** [V]. The ML env `C:/RideBoundData/envs/ml-v1` has numpy, pandas 2.3.3, scipy and sklearn, but no
pyarrow or fastparquet. The FleetPy env also lacks pyarrow. Reading the parquet files needs an owner-approved install,
or the NYC Open Data CSV export, which I could not test (403 from this machine) [UNVERIFIED].

### 2.4 Public data with a promised or quoted time against the actual outcome

| Dataset | Promise field? | Actual field? | Scope | Verified |
|---|---|---|---|---|
| **Meituan INFORMS TSL challenge** (github.com/meituan/Meituan-INFORMS-TSL-Research-Challenge) | **Yes.** "Promise deliver time — Unix time when the order is promised to be delivered to the customer", schema `estimate_arrived_time` (`S/meituan_tsl_background_20240321.txt:189–201`) | `arrive_time`, "when the waybill is delivered by the courier" (:281–288) | Food delivery. 654,343 waybill rows (:112). "a new waybill is created when the order is refused by a courier and re-enters the assignment process" (Table 1). The supplementary doc's examples carry dt 20221017–20221018 (`S/meituan_tsl_data_report_20241015.txt:30–33`); the exact period is [UNVERIFIED]. License CC BY-NC 4.0, "without permission, the distribution of this dataset to third parties is not allowed"; acknowledgment required. Main file 38.8 MB zip (not downloaded) | [V-web] |
| **Cainiao LaDe-P** (huggingface.co/datasets/Cainiao-AI/LaDe) | Customer-required window: `time_window_start/end` "Start/End of the required time window" (`S/lade_README.md:80–81`) | `pickup_time` (:94). LaDe-D has only `delivery_time`, no window (:118) | Parcel pickup; "10,677k packages of 21k couriers over 6 months" (:19) | [V-web] |
| **Amazon Last Mile 2021** (registry.opendata.aws) | `time_window` "interval of time in which package delivery is acceptable" for some packages (`S/mit_cave_rc_cli_data_structures.md:25`) | **No arrival timestamps.** Only `departure_time_utc` (:30), the actual stop sequence, and "the average of historically realized travel times" (:36) | 9,184 routes, 2018, CC BY-NC 4.0 (`S/aws_registry_amazon_last_mile.yaml`) | [V-web] |
| **GTFS-realtime** (transit) | Predictions: `StopTimeEvent.time` "Estimated or actual event as absolute time" (`S/gtfs_rt_reference.md:187`); the static schedule is the plan | Same field for past events | Spec only. NYC archive availability [UNVERIFIED] | [V-web] (spec) |
| Olist e-commerce | `order_estimated_delivery_date` (from memory) | `order_delivered_customer_date` (from memory) | Kaggle blocked by a captcha | **[UNVERIFIED]** |
| NYC TLC (all 4) and Chicago TNP | **No** | trip times | ride-hailing | [V] |
| RideAustin, DiDi GAIA | not checked | — | — | [UNVERIFIED] |

**Honest statement.** Among the ride-hailing and ride-pooling trip datasets whose schemas I verified (TLC yellow,
green, FHV and HVFHV; Chicago TNP), **none contains a quoted ETA or a promise**. Meituan's food-delivery data is the only
verified public dataset with a platform promise next to the actual outcome. My failing to find one is not proof that
none exists.

**Found incidentally (claim-boundary relevance).** Wolf, Engelhardt, Zhang, Dandl and Bogenberger (2023), arXiv
2308.05535, FleetPy authors, Munich with Aimsun (`S/arxiv_2308.05535.txt:7`): "customers suffer from unreliable pick-up
time and travel time estimations. Allowing re-assignments … helps to restore system efficiency and reliability, but
only to a minor extent." Whether `docs/03` already cites it is [UNVERIFIED]; I did not read the repository.

---

## 3. Headroom: how much a better traffic forecast could still gain here [V]

**Weekdays.** Primary Family A rule (`optimize/test-family-a-causal-no15-2026-10-06-report.txt:8`): C-30, 21 active
weekday cells.

| Metric | No forecast | With forecast |
|---|---|---|
| Y (late > 60 s) | 6.01% | 0.17% |
| MAE | 17.1 s | 7.0 s |
| Bias | +14.2 s | +0.5 s |

The forecast adds 13.7 s mean extension (p90 33.3 s).

**Rider counts** (computed inline from `…causal-no15-2026-10-06-cells.tsv` as Σ Y_disp × served over the 21 C-30 cells
dated 14–16 Nov; command in Appendix A): served 1,471; late > 60 s **2.00 with the forecast** (1 rider in
`d20181114-s10-r3-w07`, 1 in `d20181116-s10-r2-w08`) against **68.00 without**. A perfect forecaster can remove at most
**2 riders**. One rider is about 0.07 pp of 1,471, so no gain in Y is detectable with 21 cells over 3 mornings.

The only remaining weekday axis is promise length and two-sided error. The oracle stretch fits arrivals within 2 s for
2305/2305 dispatch-zero riders (report line 28), so roughly 5 s of MAE and some of the 13.7 s extension is the ceiling.
That is seconds, while the contract thresholds cited in FORECAST-REPORT §3 are minutes.

**Snow afternoon.** 15 Nov, w14 and w15, 8 cells; `optimize/test-snow-2026-10-06-report.txt:2–10`.
- Served Σ = 601.
- Late riders, Σ served × Y: **34 with the forecast** (1+6+6+6+5+4+0+6) against **41 without** (2+6+6+7+6+4+1+9).
- 92.5% of late seconds are "unanticipated" (line 10), and the forecast extended promises by only 2.0 s.

So the headroom is large (34 riders), but it is **one event, one afternoon, one cluster**.

**Zero-run screen of causal growth predictors** [V; EXPLORATORY, unsealed, retrospective; `S/growth_predictor_screen.py`
→ `S/growth-predictor-screen-2026-10-09.txt`]. Mean absolute % error of the predicted growth ratio f(b0+h)/f(b0).
`hist12_13` = sealed vintage; `momentum` = (f(b0)/f(b0−1))^h; `blend` = their geometric mean.

| Horizon | Days | Windows | hist12_13 | momentum | blend |
|---|---|---|---|---|---|
| 30 min | weekdays 12–16 Nov | w07, w08 | 1.11–2.69% | 1.87–6.66% | 1.32–3.76% |
| 30 min | snow day | w14 / w15 | 8.20 / 10.95% | 6.73 / 6.33% | **5.01 / 5.19%** (lines 21, 28) |
| 60 min | snow day | w14 / w15 | 14.95 / 19.66% | 13.34 / 13.70% | 12.31 / 7.68% (lines 58, 65) |

Notes on the table:
- 12 and 13 Nov are in-sample for hist12_13.
- Momentum **hurts on normal days**. At 60 min: w17 on 15 Nov, 20.41% against 4.02% for hist; w07 on 13 Nov, 19.82%
  against 1.86%.
- Momentum here is optimistic, because f(b0) is not fully observable at t0 (§1.2 check 2).

**Reading.** A learner that knows *when* to trust momentum (a regime or weather detector) could address the snow case.
Learning that needs many event days, and Sep–Dec 2018 has none besides the test event.

---

## 4. Simulator constraints that bound any data-driven forecaster

1. **One city-wide factor per 15 min** (`NetworkTTMatrix.py:295`). The learnable target is a 96-value series per day.
   Spatial or OD-level traffic models cannot be evaluated: the simulator would erase their extra information.
2. **Only bundle days are wired in.** The world wrappers read `preflight_world.FACTORS / f"{day}_tt_factors.csv"`, with
   FACTORS hard-coded to the bundle (`tang3/world/preflight_world.py:51–55, 71`; `preflight_world_v1_3.py:56`), and
   allowed window starts are whitelisted (`preflight_world.py:56`; v1.3 overrides them at :143). New days would need:
   - a new wrapper version with a new factor directory (outside the immutable bundle);
   - new `sample_10` demand files in the bundle's format (`request_id, rq_time, start, end`).

   Whether the medium preflight in `E:/Code/RideBound-deadline` accepts a different demand path without a core change
   is **[UNVERIFIED]**. That repository is off-limits for me.
3. **Size caps.** The tool caps runs at 128 requests, 32 vehicles and 96 nodes; cells hold 108 requests with 8
   vehicles, about 70 riders per cell (`claude-work/RUNTIME-ESTIMATE-2026-10-07.md`, fact 7). Late-rider events are a
   handful per cell, so new evidence needs many cells.
4. **Runtime.** About 15 min per job, 6 in parallel (same file, fact 3). For example, 12 new weekdays × 2 windows ×
   2 arms × 2 seeds = 96 jobs, about 4 h. This is an extrapolation.

---

## 5. Options evaluated

### (A) Traffic-profile forecaster trained on many weeks of Manhattan taxi speeds, tested on the FleetPy days

- **Data.**
  - Sep–Dec 2018 yellow: 0.48 GB, about 8 M rows/month citywide, about 0.19–0.25 M Manhattan trips/day. That gives
    about 86 weekday profiles × 96 bins, or about 8,300 bin values.
  - Jul 2016 – Feb 2020: 5.35 GB, 956 weekdays, 7 heavy-snow weekdays.
- **What to train.** In increasing ambition:
  - A1: a k-week same-weekday mean profile, the standard 17-week-style historical average (S4, E4);
  - A2: a quantile or conformal growth model (standard, S4 D1–D5);
  - A3: a gradient-boosted growth model with time-of-day, day-of-week, holiday, lagged growth and weather.
- **Leakage risks.**
  1. f(b) is built from trips that start in b and end later. A causal model may use only lags ≥ 1–2 bins; the sealed
     design's anchor at f(b0) is already optimistic.
  2. Daily NOAA totals are known only after the fact. Weather features need hourly observations or archived forecasts
     [UNVERIFIED availability].
  3. The test week (12–18 Nov) must be excluded from training, including its rebuilt copy, which is for validation
     only.
  4. All 7 bundle days were already inspected, so results stay "retrospective" unless new days are used.
  5. 12 Nov is a federal holiday (FORECAST-REPORT line 97) and 13 Nov had 26.9 mm of rain. The sealed vintage was
     atypical, so the comparison must be sealed before rebuilt data are examined.
- **Metric that would show a gain.**
  - Primary, no simulation: growth-ratio error at 15–60 min on held-out weeks against the 12+13 Nov vintage.
  - Secondary, zero-run replay on the existing 21 weekday cells via `promise_stretch` / `display_layer`: Y60, early60,
    MAE, and mean/p90 extension at matched mean extension.
- **What would kill it.**
  - The validation gate fails (§2.3).
  - The multi-week profile does not reduce held-out growth error against the 2-day vintage.
  - Replay cannot beat 2 late riders, or does so only by a longer promise.
- **Effort (my estimate).**
  - A1 with replay: about 1–1.5 weeks (T3 data pipeline plus T0 replay), including the pyarrow decision.
  - A3 with weather over multiple years: 2–3 weeks or more, and it still has 1 snow test event (15 Nov).
- **Headroom.** Weekdays ≤ 2 riders (§3). Snow 34 riders, but n = 1 event. **A cannot show a lateness gain here.** It
  can show a *more defensible forecast* (no dependence on a holiday and a rainy day).

### (A+) Unseen test days, the most valuable use of more data

Build new measured worlds (factor and demand) for, for example, 10–15 unseen weekdays in Sep–Dec 2018. Seal the
predictions. Run U and C-30, then replay the forecast layer.
- This directly addresses the FORECAST-REPORT limitations "already previewed" and "few clusters" (§6 there).
- **Kill:** the forecast-layer ΔY is not replicated on the unseen days.
- **Blocker:** item 2 of §4, unverified and possibly T2.
- **Effort:** +1–2 weeks on top of A1.

### (B) Pooled-trip duration inflation, shared against solo, from HVFHV shared flags

- **Data.**
  - HVFHV Feb 2019 – Feb 2020: 7.10 GB, about 20 M rows/month; shared share 23.9% falling to 13.0% (§2.1, all
    boroughs; Manhattan share not computed).
  - After 2020 the shared share is ≤ 2.3%, too sparse.
  - FHV Nov 2018 (the bundle's own month) has `SR_Flag` and pickup/drop-off, but no miles or request time, and Lyft
    over-flags.
- **What could be learned.** The ratio of trip_time for shared-matched trips against solo trips, by zone pair × 15-min
  bin. Better: requested-and-matched against requested-unmatched, which holds self-selection fixed.
- **Leakage and identification.**
  - `shared_match_flag` is ex post ("at any point during the trip") and cannot be a feature at quote time.
  - trip_time mixes the detour planned at match time with later insertions, so it **cannot isolate the thesis's c**
    (dispatch change after the first promise).
  - There are no quotes, so promise error cannot be measured.
  - Flag reliability by provider is [UNVERIFIED]; a license × flag crosstab is the first gate.
- **Metric.** Nothing inside the simulator. Simulated pooled durations come from FleetPy itself (0 s dwell, one factor,
  about 0.54 riders per vehicle against 13–24% shared in real 2019 NYC), so a real-data inflation model cannot be
  plugged in. Used as a pad in the simulator, it would measure real-to-simulator transfer, not ML skill. Its only use
  is **external validity**: compare simulated pooled ride-time inflation with real 2019 inflation.
- **Kill.** The flags are inconsistent, or the Manhattan matched sample is too noisy at zone level.
- **Effort.** A 1-month pilot (about 0.5 GB) takes 3–4 days; 13 months take 1–2 weeks. Pyarrow is needed.
- **Claim boundary.** Learning pooled outcomes or ETAs from trips is not novel (fact pack line 58–61; S4 §6(a)).

### (C) Other options

1. **Meituan promise-vs-actual (external motivation, not ML for the simulator).**
   - It gives the real share of orders delivered after `estimate_arrived_time`, and whether orders whose waybill was
     re-created (courier refusal, a system-caused change) are late more often.
   - This is a real-data analogue for O2/O3, not ride-pooling evidence.
   - About 56 MB of files; terms forbid redistribution. Effort 3–5 days.
   - **Kill:** the promise field is unusable (zeros or missing), or the reassignment link is absent.
2. **Chicago TNP cross-check of (B).** Exact `trip_seconds`, shared/matched flags, `trips_pooled`. Same identification
   limits as (B). Different city.
3. **Use the TLC shared-share numbers as a cited limitation (zero effort).** Real NYC high-volume FHV trips in
   Nov 2018 were about 23% shared (TLC indicator, definition unstated), against the simulation's low pooling density.

---

## 6. Recommendation

- **For "ML that beats the current forecast inside this simulator": NO.**
  - Weekday headroom is 2 riders out of 1,471.
  - The snow residual (34 of 601) is a single event, and Sep–Dec 2018 has no second snow weekday to learn from.
  - Going to Jul 2016 – Feb 2020 (5.35 GB, 7 heavy-snow weekdays) still leaves 1 snow test event unless new worlds are
    simulated, and that depends on an unverified input-path change.
  - A learned profile is standard practice (S4), so it cannot become a contribution.
- **Narrow, optional YES, if about 1–1.5 weeks can be spared.** Do (A1):
  1. rebuild the Sep–Dec 2018 factors with the documented Syed et al. method (0.48 GB);
  2. pass the 12–18 Nov validation gate;
  3. replace the 2-day vintage (holiday plus rainy day) with a sealed multi-week same-weekday profile;
  4. report held-out growth error and the zero-run replay.

  Frame it as robustness of the existing storyline ("C plus forecast"), not as an ML contribution. Do (A+) only if the
  preflight accepts new days without core changes.
- **Skip (B)** as a work package. At most, cite the TLC shared-share numbers as a limitation.

---

## 7. Not verified, or failed

- Parquet timestamp logical type: not decoded; second resolution is inferred from the bundle.
- Speed-filter distance definition in Syed et al.
- Medium-preflight input configurability (repository not read).
- NYC Open Data / Socrata, data.cityofchicago.org and the Kaggle API: all blocked (403 or captcha).
- Chicago 2018–2022 `shared_trip_match`; the 2023–2024 release id.
- Meituan exact period.
- Olist, RideAustin, DiDi GAIA fields.
- GTFS-RT archives for NYC.
- Definition of the TLC "Trips Per Day Shared" column.
- HVFHV flag reliability; Manhattan-internal shared share.
- Whether Wolf et al. 2023 is cited in `docs/03`.
- The Chicago FleetPy factor file.

**Failed-fetch stubs** kept in `S/`, not deleted:
- `tlc_dd_{yellow,green,fhv,hvfhs}.pdf` (403 HTML; the `_v2` files are the real ones);
- `chicago_tnp_2025_columns_wayback_20260930.json` and `_try2.json` (429);
- `meituan_tsl_README_{main,master}.md` (404);
- `zenodo_15187906.json` (403);
- `chicago_dev_blog_tnp_privacy.html` (403);
- `socrata_foundry_*.html` (a JavaScript shell with no metadata);
- `datagov_transportation-network-providers-trips-2023.html` (a 404 page);
- `datagov_harvest_*.json` (these are Chicago *Taxi* 2024-, irrelevant).

**Disclosure.** The WebFetch tool itself cached Syed et al.'s 7.6 MB supplementary PDF in
`C:/Users/quang/.claude/projects/e--Code-RideBound/4f238113-…/tool-results/`, outside the project. I did not copy it,
because it is above the 5 MB cap; only a text excerpt is in `S/`.

## Appendix A: inline count of weekday late riders (re-runnable, read-only)

```
python -I -B -c "import csv; R=[r for r in csv.DictReader(open('E:/Code/Report_INT3508/ridebound-scratchpad/optimize/test-family-a-causal-no15-2026-10-06-cells.tsv',encoding='utf-8'),delimiter='\t') if r['arm']=='C-30' and r['cell'][1:9] in ('20181114','20181115','20181116')]; print(len(R), sum(int(r['served']) for r in R), sum(float(r['Y_disp'])*int(r['served']) for r in R), sum(float(r['Y_naive'])*int(r['served']) for r in R))"
```

Output observed (FleetPy env Python, 2026-10-10): `21 1471 2.0 68.0`.
