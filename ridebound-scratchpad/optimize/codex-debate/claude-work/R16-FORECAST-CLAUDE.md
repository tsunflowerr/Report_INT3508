# R16: Q5, forecast + rule C on days with unpredictable events (Claude-side forecast and data designer)

Date 2026-10-10. Read first: `ROUND16-FACT-PACK.md` (Q5), `ROUND16-REVIEW-STANDARD.md`, `optimize/FORECAST-REPORT.md`,
`optimize/{forecast_family_a,promise_stretch,display_layer,family_snow}.py`, `codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md`,
`claude-work/R13-ML-DATA-CLAUDE.md` with `claude-work/r13-ml-data-samples/`, `tang3/world/preflight_world{,_v1_3}.py`,
the FleetPy bundle factor files (read-only), and the owner's Fielbaum & Alonso-Mora 2020 text extraction.

**Independence.** I did not open `codex-work/R16-*`, `codex-work/r16-*`, `antigravity-work/`, or the sibling
`claude-work/r16-evidence/`.

**Constraints kept.** No simulation, build, install or deletion. I wrote nothing outside `claude-work/r16-forecast/`
and this file.
- Every script output was opened with mode "x".
- Downloaded samples, all under 0.5 MB, were written once to new file names. They are small metadata, schema or CSV
  files.

**Paths and tags.**
- `F/` = `claude-work/r16-forecast/`; `S/` = `claude-work/r13-ml-data-samples/`; `O/` = `optimize/`.
- Labels: **[M]** measured by my local computation (file:line); **[S]** first-order screen; **[I]** inference;
  **[H]** hypothesis; **[O]** opinion; **[V-web]** URL plus a quote I read; **[UNVERIFIED]**.
- Everything computed below is **RETROSPECTIVE**: all 7 bundle days and all the replayed runs were inspected before
  this round. Nothing is sealed, so nothing here is confirmatory evidence.

---

## 0. Bottom line

1. **Yes, the only remaining headroom is on the event day, but it is one afternoon and it is worth about one minute
   per late rider.**
   - Weekdays: forecast + C-30 leaves **2 of 1,471** riders more than 60 s late. The oracle leaves 0
     (`F/rider-nowcast-replay-2026-10-10.txt:40,49`).
   - Snow afternoon of 15 Nov 2018: **34 of 601** riders are late (line 8).
   - Even with the naive promise, only **0.69%** of snow-day riders are more than 120 s late, and **0%** are more than
     300 s late (`O/test-snow-2026-10-06-report.txt:10`; these are the naive values, `O/family_snow.py:37`). So the
     whole headroom sits in the 60–120 s band.
2. **Headroom split on the snow afternoon** (41 riders late > 60 s against the naive promise; 3,446 late-seconds) [S]:
   - dispatch (what rule C addresses): 9 s (0.3%);
   - already anticipated by the current profile: 251 s (7.3%);
   - **(a) further knowable from traffic snapshots already delivered at quote time: about 26%** (range 8–43%, depending
     on data latency and on how aggressively trend is extrapolated);
   - **(b)+(c), not knowable from traffic history: about 67%.** The split between (b), needing a weather signal, and
     (c), not knowable at all, cannot be measured with local data (§1.5).
3. **Best fair-looking method in the screen: a regime gate plus a blended trend.**
   - Rule: keep the historical profile, but when the current level is far above the historical same-time level, switch
     to sqrt(profile × momentum).
   - Snow late riders **34 → 19**, mean quote extension +7.5 s on the snow day, and **no change on the 21 weekday
     cells**.
   - A uniform pad with the same snow-day cost gives 27.
   - **But the gate threshold (1.3) sits between the weekday maximum 1.244 and the snow minimum 1.323, which I saw
     before choosing it** (`F/factor-nowcast-screen-v2-2026-10-10.txt:219-223`). With a realistic one-bin data latency
     the gain shrinks to 34 → 29.
   - An outcome-feedback recalibration with parameters fixed a priori gives 34 → 20, at +3.5 s quote cost and +0.21 pp
     early arrivals on weekdays (`F/rider-nowcast-replay-v2-2026-10-10.txt:4-5,15-16`).
4. **The Round-12 damped-trend protocol collapses to the current method.**
   - Fitted as R12 prescribes (on 12/13 Nov), it selects alpha = 1.0, beta = 0, phi = 0.8 (`F/factor-nowcast-screen-2026-10-10.txt:2`).
   - beta = 0 means no trend, so its forecasts are identical to the current profile, and running that protocol would
     report a null by construction (§1.3).
5. **Prior work covers every method component, so there is no methodological novelty.** The components and their
   prior sources are listed in §2.
6. **Data are feasible.**
   - TLC yellow trips 2009–2020; the Syed et al. factor method; NOAA hourly LCD weather, verified for 2013 and 2018.
   - **Correction to the premise.** TLC's *current official* 2013 parquet files have **zone IDs only, no coordinates**
     (`F/parquet-footer-probe-2013-2026-10-10.txt:1-2`). Coordinates exist in the official files for 2009, and in the
     Azure Open Datasets copy of 2013 (schema verified; non-null values UNVERIFIED).
7. **Verdict on the 2013 idea.**
   - The Fielbaum & Alonso-Mora 2013 dataset itself: **REJECT for Q5.** It was chosen to *exclude* traffic variability.
     It sits on static daily-mean travel times and contains no weather event.
   - The broader 2009–2015 TLC archive: **acceptable as extra training events** in a future offline benchmark, with an
     explicit year effect. Domain shift is large: yellow trips/day **479,527 (Nov 2013) vs 271,501 (Nov 2018)**, and
     ride-hail rose from 0 to 691,379/day.
8. **Recommendation: future work, not before the deadline.**
   - Put the (a)/(b)/(c) decomposition into the planned zero-run results chapter as a labelled *diagnostic limitation*,
     about 2–3 h of writing.
   - Defer the multi-event benchmark (§4; about 35–50 h, and installs needing approval) to future work.
   - It cannot strengthen the rule-C claim either way: on the snow day, dispatch caused 9 of 3,446 late-seconds.

**For the owner, in plain words.** The forecast already fixes ordinary rush hours almost perfectly. On the snow
afternoon a smarter "is today abnormal?" switch could have saved about 15 of 34 late riders. Each of them was late by
only 1–2 minutes, and this rests on a single snowy afternoon that we already looked at. To *prove* it works, we would
need dozens of past snow days rebuilt from taxi data, and that is a new project of 1–2 weeks. Better data from 2013
does not change this, because the 2013 study deliberately avoided traffic.

---

## 1. Headroom analysis (zero-run, local files, retrospective)

### 1.1 Premise checks [M]

- **Fit days.** For the 15 Nov snow cells, the sealed primary rule `causal-no15` uses **three** source days, 12, 13
  and 14 Nov, not two (`O/display_layer.py:11-12`; `O/family_snow.py:2`). Only the Round-12 protocol fixes the vintage to
  12/13 (`codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md:19`).
- **How the forecast is built.**
  - The display layer shows D = max(p, S), where S stretches the naive remaining time along m(b)/m(b0) after the
    current bin (`O/display_layer.py:3-8,60-64`; `O/promise_stretch.py:9-11,49-52`).
  - The world and the forecast hold the factor from window-relative bin 8 (`tang3/world/preflight_world_v1_3.py:51`).
- **What the Runner sees.**
  - It sees only the current bin's snapshot, held flat (`tang3/world/preflight_world.py:13-20`).
  - The simulator reveals the current bin's factor exactly at the bin start. This is an idealisation: the bundle
    factor of bin b is built from trips that *start* in b (`S/factor-definition-checks-2026-10-09.txt:2-8`;
    `R13-ML-DATA-CLAUDE.md:100-102`), so in reality it lags. Hence the lag-1 sensitivity below.

### 1.2 What the snow afternoon looked like (factor, trips, weather) [M]

Factors and trips are from the bundle `2018-11-1{4,5,6}_tt_factors.csv`, columns `travel_time_factor` and
`travel requests`. Weather is NOAA LCD Central Park, `F/noaa-lcd-centralpark-2018-11-15-16.csv`. LCD times are
"Local Standard Time" (`F/noaa_lcd_documentation.txt:10`), which equals the clock time on 15 Nov 2018 because DST had
ended. HourlyPrecipitation is the "amount of all precipitation within the preceding hour" (`:233`).

| Time | Factor 15 Nov | Factor 14 / 16 Nov | Trips per 15-min bin, 15 Nov (14 / 16) | Weather at Central Park, 15 Nov |
|---|---|---|---|---|
| 13:00 | 4.06 | 4.39 / 3.35 | 2,870 (2,706 / 2,646) | 12:51: dry, visibility 16 km |
| 13:30 | 4.50 | 4.28 / 3.41 | 3,123 | **13:44: "-SN", visibility 4.0 km**; 13:59 "SN", 0.8 km |
| 14:00 | 4.95 | 4.16 / 3.38 | 2,903 | 14:10 "SN FG", 0.4 km |
| 15:00 | 5.42 | 4.13 / 3.44 | 2,634 | 14:43 "+SN"; 14:51 precip 1.78 mm/h |
| 15:30 | 6.49 | 4.07 / 3.37 | **2,110** (3,137 / 3,054) | 15:51 "+SN", precip 4.57 mm/h |
| 16:00 | 6.95 | 4.15 / 3.19 | 1,517 | 16:51 "+SN FZ FG", precip 6.10 mm/h, −1.7 °C |
| 17:00 | 7.90 | 4.34 / 3.25 | 830 | 17:51 "-SN", precip 4.06 mm/h |
| 18:00 | 7.62 | 4.11 / 3.34 | 947 | changes to rain about 20:00 |

Reading [I]:
- The traffic signal (factor rising from 13:30) and the observed-weather signal (snow onset at 13:44) appear **at the
  same time**. A weather feed gives no lead time on the *onset*.
- What nobody anticipated is the build-up from 15:00 to 17:00. It coincides with the precipitation-intensity increase,
  which an hourly observation reveals only as it happens.
- The official forecast that morning was far off. CBS reports that NWS Upton was "calling for only an inch of snow in
  the city", and that Thursday morning's NWS map showed "a zero percent — zero! — chance of 6-inch accumulation" [V-web,
  https://cbsnews.com/amp/news/snowstorm-nyc-traffic-port-authority-forecast-what-went-wrong; a news source, not an
  NWS product].
- The collapse in trip counts (2,110 at 15:30 against about 3,100 on normal days) is a real-time signal that a
  city-wide feed would have. The simulator's operator does not have it.

### 1.3 Factor-level screen over the bundle days

`F/factor_nowcast_screen.py` → `F/factor-nowcast-screen-2026-10-10.txt` (v1), and `F/factor_nowcast_screen_v2.py` →
`F/factor-nowcast-screen-v2-2026-10-10.txt` (v2). v1 is kept unchanged; v2 imports v1's methods.

**Setup.**
- **Quote grid.** For each quote time t0 (every 60 s in a 2-h window) with naive remaining time W, the arrival is
  A* = stretch along the true factors, and the displayed promise is D = max(t0 + W, stretch along the method's path).
- **Information.** A causal accessor raises an error on any bin after the quote bin (leak self-test passed, v1 line 3).
  - "-in": in-window snapshots only (the Round-12 rule);
  - "-pre": same-day bins from 06:00 (a city-wide feed);
  - "-L1": the trend uses bins ≤ k0−1 (realistic latency).
- **Methods.**
  - HIST: the current causal-no15 profile;
  - MOM: momentum, (f(k0)/f(k0−1))^h;
  - BLEND: sqrt(HIST·MOM), as in R13;
  - RTR: profile × undamped residual trend;
  - DT: R12 damped trend;
  - REGB-x: BLEND-pre if f(k0)/m(k0) ≥ x, else HIST;
  - PAD@M: uniform pad with M's mean extension on the same population, which flatters the pad;
  - ORACLE: the true factor path.

**Damped-trend fit [M].** The R12 grid fit (36 triples, 80 one-step targets on 12/13 Nov) selects
**alpha = 1.0, beta = 0.0, phi = 0.8** (v1 line 2).
- With beta = 0 the trend stays 0, so DT ≡ HIST on every population (v2 lines 7, 29, 95, 117).
- No fixed triple helps the snow afternoon without hurting weekdays. The best snow triple (1.0, 0.3, 0.98) gives snow
  late60 26.7% against HIST's 47.5% at W = 1800 s, but raises weekday-sim late60 to 2.40% from 1.98% and early60 to
  6.35% from 4.90% (v2 lines 180-217).
- **The R12 protocol, executed as written, would show zero gain by construction.**

**Main factor-level numbers [S]** (v2 lines 4-46, 136-178). Each cell is late60 % / early60 % / mean extension in s.
For scale, rider W has median 784 s and p90 about 1,150 s (`F/rider-nowcast-replay-2026-10-10.txt:36,66`).

| Method | Snow afternoon, W = 1200 s | Snow afternoon, W = 1800 s | Weekday-sim, W = 1200 s | Weekday-sim, W = 1800 s |
|---|---|---|---|---|
| NAIVE | 15.8 / 0 / 0 | 50.8 / 0 / 0 | 9.79 / 0.21 / 0 | 36.0 / 3.12 / 0 |
| HIST (current) | 14.6 / 0 / 3.8 | 47.5 / 0 / 6.8 | 0 / 0.31 / 22.0 | 1.98 / 4.90 / 48.6 |
| BLEND-in | 7.1 / 0 / 16.4 | 19.6 / 0 / 37.0 | 0 / 0.42 / 25.5 | 1.56 / 6.15 / 58.2 |
| BLEND-pre | 6.7 / 0 / 18.2 | 19.6 / 0 / 41.5 | 0 / 0.42 / 25.7 | 1.77 / 6.25 / 58.5 |
| BLEND-L1 (latency) | 12.5 / 0 / 18.5 | 33.8 / 0 / 41.4 | 0.42 / 0.31 / 27.1 | 3.23 / 6.04 / 61.5 |
| MOM-in | 6.7 / 2.9 / 33.7 | 15.0 / 23.8 / 77.7 | 0 / 1.35 / 29.9 | 1.35 / 13.0 / 70.0 |
| REGB-1.3 (post-hoc gate) | 6.7 / 0 / 18.2 | 19.6 / 0 / 41.5 | = HIST | = HIST |
| PAD@BLEND-in (equal cost) | 10.0 / 0 / 16.4 | 28.8 / 0 / 37.0 | 4.69 / 1.98 / 25.5 | 12.6 / 18.4 / 58.2 |
| PAD@ORACLE (equal cost) | 5.0 / 0 / 35.6 | 15.0 / 4.6 / 80.2 | 4.69 / 1.98 / 25.2 | 12.8 / 17.9 / 55.8 |
| ORACLE | 0 / 0 / 35.6 | 0 / 0 / 80.2 | 0 / 0.21 / 25.2 | 0 / 3.12 / 55.8 |

Facts [S]:
- On the snow afternoon, causal blends remove about a third of HIST's absolute error: 31.6–35.9% MAE (v2 lines 20-24,
  42-46). They beat an equal-cost uniform pad (19.6% vs 28.8% at W = 1800).
- One-bin latency cuts the MAE gain to 21.8–24.1%.
- On weekdays, the trend variants *cost* MAE in 9 of 10 cases on the simulated windows: −0.8% to −37.2%, with one
  exception at +1.0%, BLEND-L1 at W = 1200 (v2 lines 152-156, 174-178). The current profile is already close to the
  oracle there, and HIST shows 0% late at W = 1200 s.
- Uniform pads are much worse than the profile on weekdays (late60 4.7–12.8%).
- **The gate statistic f(k0)/m(k0)** (v2 lines 219-223): snow minimum 1.323, weekday maximum 1.244.
  - The weekday maximum sits on 14 Nov afternoons, because their history is 12 Nov (a holiday) plus 13 Nov. Those
    values run 1.13–1.24 (my inline listing, same data).
  - So the separation depends on the fragile vintage. Any threshold between 1.25 and 1.32 is tuned on the event.

### 1.4 Rider-level replay on the saved C-30 runs [S]

`F/rider_nowcast_replay.py` → `F/rider-nowcast-replay-2026-10-10.txt`, and `F/rider_nowcast_replay_v2.py` →
`F/rider-nowcast-replay-v2-2026-10-10.txt`.
- **Data.** The 8 snow runs and 21 weekday cells, read with the sealed reader `forecast_family_a.riders`.
- **Sanity check.** HIST reproduces the sealed display to **0.000 ms** (line 3). The reproduced snow and weekday
  numbers (5.94% / 34 riders; 0.17% / 2 riders) match `O/FORECAST-REPORT.md:42,103`.

| Method (C-30 runs) | Snow: Y60 / E60 / ext / late riders (of 601) | Weekday: Y60 / E60 / ext / late riders (of 1,471) |
|---|---|---|
| NAIVE | 7.19% / 0 / 0.0 s / 41 | 6.01% / 0 / 0.0 s / 68 |
| HIST (current sealed layer) | 5.94% / 0 / 2.0 s / 34 | 0.17% / 0.08% / 13.7 s / 2 |
| BLEND-in (strict snapshots) | 3.59% / 0 / 8.5 s / 21 | 0.17% / 0.19% / 15.7 s / 2 |
| BLEND-L1 (one-bin latency) | 5.04% / 0 / 9.0 s / 29 | 0.29% / 0.14% / 16.5 s / 3 |
| REGB-1.2/1.3 (post-hoc gate) | 3.21% / 0 / 9.5 s / **19** | 0.17% / 0.08% / 13.7 s / 2 |
| RTR-pre (aggressive trend) | 1.31% / 2.12% / 19.1 s / 8 | 0.66% / 0.66% / 15.7 s / 7 |
| PAD@REGB (equal snow cost) | 4.66% / 0 / 9.4 s / 27 | — |
| PAD-wk@BLEND-in (weekday k on snow) | 4.45% / 0 / 13.3 s / 26 | PAD@BLEND-in: 2.94% / 0.21% / 13.5 s / 32 |
| FB80@HIST (own-outcome feedback) | 3.38% / 0.75% / 21.0 s / 20 | 0.17% / 0.29% / 17.2 s / 2 |
| FB80@BLEND-in | 2.60% / 0.62% / 22.0 s / 15 | 0.17% / 0.73% / 18.5 s / 2 |
| ORACLE | 0 / 0 / 18.8 s / 0 | 0 / 0 / 15.6 s / 0 |

Sources: v1 lines 7-23 and 39-53; v2 lines 4-23.
- FB = rolling q-quantile of completed riders' relative error, with q and minimum count fixed before the first run
  (v2 docstring). It is *not* the exact Gibbs–Candès recursion.
- Pads use k computed from promises only (v1 line 4).

### 1.5 The (a)/(b)/(c) split for the snow afternoon [S + I]

The ledger covers the 41 riders more than 60 s late against the naive promise, 3,446 s in total
(`F/rider-nowcast-replay-2026-10-10.txt:24-35`). "Explained" means Σ clip(D − P0, 0, A − P0 − dispatch).

| Component | Seconds | Share | Status |
|---|---|---|---|
| Dispatch (rule C's target) | 9 | 0.3% | measured |
| Anticipated by the current profile | 251 | 7.3% | measured; matches sealed `O/test-snow-2026-10-06-report.txt:10` |
| **(a) further knowable from delivered snapshots** | **887** (REGB / BLEND-pre); 822 strict in-window; 274 with one-bin latency; up to 1,496 with an aggressive trend that overshoots 277 s and makes 2.1% early | **25.7%** (range 8.0–43.4%) | retrospective screen |
| **(b) + (c) not knowable from traffic history** | **2,299** (range 1,691–2,912) | **66.7%** | residual |

**Splitting (b) from (c)** cannot be measured locally, because there is no second snow day in the bundle. Inference
from the evidence:
- **(b) has a small level part.** All quotes on the snow afternoon come after snow onset (13:44), and the live anchor
  already absorbs any *level* effect at t0. Published weather effects are level effects:
  - heavy snow raises London travel times by "7.4% to 11.4%" (Tsapakis et al. 2013, §2);
  - the realised build-up after quote times here was +60% (4.95 → 7.90, 14:00 → 17:00).

  A weather model adds value only if it predicts the *build-up*. That needs a model learned on past NYC storms, which
  can be large: Donovan & Work report that the "blizzard of December 2010 … added four minutes of travel time to each
  mile at its peak".
- **The weather forecast was wrong that day** (§1.2), so only *observed* weather would have been usable. Observed
  weather arrives together with the traffic signal.
- [H] With observed weather, (b) is mostly a better-calibrated *gate* plus a typical storm build-up curve. Its size is
  unknown, plausibly a minority of the 67%. (c), the network breakdown 15:30–17:00 with trips collapsing to about 30%
  of normal, is plausibly the larger part.
- Measuring this split is exactly what the offline benchmark of §4 is for.

**What a strict reviewer takes from §1** [O]: the headroom is real, but it is (i) one event and one cluster, (ii) worth
60–120 s per rider, and (iii) partly an artefact of the simulator revealing the current factor with zero latency.

---

## 2. Method survey: what is prior work

| Idea used or considered | Closest primary source | Quote I read | Status for the thesis |
|---|---|---|---|
| Damped trend | Gardner & McKenzie (1985), *Management Science* 31(10):1237–1246, https://www.bauer.uh.edu/egardner/3301H%20Operations%20Management/ESG%20Publications/1985%20Forecasting%20trends.pdf (`F/gardner_mckenzie_1985.txt:3,39-41`) | "This paper develops an exponential smoothing model designed to damp erratic trends." | Prior; in our data the fit chooses no trend (§1.3) |
| Kalman filtering of real-time plus historic travel times | Chien & Kuchipudi (2003), *J. Transp. Eng.*, https://digitalcommons.njit.edu/fac_pubs/13935/ | "The Kalman filtering algorithm is applied for travel time prediction"; "continuously updating the state variable as new observations" | Prior |
| Regime / change-point adaptive forecasting under incidents and weather | Cetin & Comert (2006), *TRR* 1965:23–31, https://profiles.ncat.edu/en/publications/short-term-traffic-flow-prediction-with-regime-switching-models-5/ | "Traffic flow is subject to abrupt disturbances because of various unexpected events" "(e.g., accidents, weather-induced disruption)"; "The intercept of the forecasting models is updated on the basis of the detected shifts in the mean level" | Prior; REGB is a crude instance |
| Weather effect on urban travel times | Tsapakis, Cheng & Bolbol (2013), *J. Transport Geography* 28:204–211, https://ideas.repec.org/a/eee/jotrge/v28y2013icp204-211.html | heavy snow "spanning from 7.4% to 11.4%"; rain "0.1–2.1%, 1.5–3.8%, and 4.0–6.0%" | Prior; level effects only |
| NYC taxi-derived travel-time anomalies in extreme events, 2010–2013 data | Donovan & Work (2017), *TR Part C* 79:333–346; arXiv 1507.06011, https://arxiv.org/abs/1507.06011 and https://ar5iv.arxiv.org/html/1507.06011 | "Hurricane Sandy impacted traffic conditions for more than five days"; "The blizzard of December 2010, while shorter, added four minutes of travel time to each mile at its peak."; "it could potentially be used as an online monitoring tool"; data "New York City taxi data (2010–2013)", FOIL | **Closest prior work** to the owner's idea (same city, same years, same data family) |
| Weather-fused traffic prediction | Koesdwiady (2018), PhD thesis, Waterloo, https://uwspace.uwaterloo.ca/handle/10012/13168 | "a novel deep-learning-based approach that predicts traffic flow by fusing the traffic history and weather data" | Prior. The IEEE TVT 2016 paper is seen only as a bibliographic record [UNVERIFIED content] |
| Coverage-preserving widening under shift | Gibbs & Candès (2021), arXiv 2106.00170, https://arxiv.org/abs/2106.00170 | "the data generating distribution is allowed to vary over time in an unknown fashion"; "provably achieves the desired coverage frequency over long-time intervals" | Prior; FB80 is a simpler cousin |
| Industry: recency reweighting after a regime change, history plus live data | Google Maps blog, J. Lau, 3 Sep 2020, https://blog.google/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/ | "automatically prioritizing historical traffic patterns from the last two to four weeks"; "We then combine this database of historical traffic patterns with live traffic conditions"; road conditions can change "due to mudslides, snowstorms, or other forces of nature" | Industry practice |
| Industry: post-processing the routing ETA | Uber DeeprETA, Hu et al. (2022), arXiv 2206.02127, https://arxiv.org/abs/2206.02127 | "refines naive ETAs produced by a route planning algorithm" | The same architecture as our display layer (prior) |
| Fair forecast evaluation | Hyndman & Athanasopoulos, FPP3 §5.10, https://otexts.com/fpp3/tscv.html | "evaluation on a rolling forecasting origin"; "no future observations can be used in constructing the forecast" | Evaluation standard used in §4 |

**What remains defensible** [O].
- No method in Q5 is new, and the strict claim boundary already forbids claiming forecast quoting or ML ETA
  (`E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md:56,83`; `ROUND16-FACT-PACK.md:91-93`).
- The only thing a reviewer could accept is a **measurement**: inside the existing v/e/p promise ledger, a five-part
  lateness decomposition on a measured incident (dispatch / anticipated / nowcastable / weather-or-unknowable). It shows
  that the incident residual is traffic and not dispatch. That extends the thesis's existing three-part ledger
  (`O/FORECAST-REPORT.md:72-77,102-105`). It is incremental, and it is diagnostic only while n = 1 event.

---

## 3. Data feasibility

### 3.1 NYC TLC yellow trips

| Era | What the official files contain (my parquet-footer probes) | Size | Note |
|---|---|---|---|
| 2009 | `Start_Lon, Start_Lat, End_Lon, End_Lat`, string datetimes, 18 columns (`F/parquet-footer-probe-2013-2026-10-10.txt:4`) | 5.72 GB/yr (2010: 5.65) (`F/tlc-yellow-sizes-2009-2015-2026-10-10.tsv`) | Coordinates in the official files |
| **2013** | **`PULocationID, DOLocationID`, no coordinates**, INT64 timestamps, 19 columns; 2013-01: 14,776,617 rows, 184.7 MB; 2013-11: 14,388,451 rows (`F/parquet-footer-probe-2013-2026-10-10.txt:1-2`) | **2.14 GB/yr** (monthly 148–195 MB) | **Premise corrected:** the current official release has no lat/lon for 2013 |
| 2013, Azure Open Datasets copy | `startLon, startLat, endLon, endLat` and `puLocationId` columns, INT96 timestamps; 2013-01 = 20 parts, 487 MB (`F/parquet-footer-probe-azure-2013-01-2026-10-10.txt:1`; `F/azure-nyctlc-yellow-2013-01-listing.xml`) | about 0.49 GB/month | Schema verified; **non-null 2013 coordinates UNVERIFIED** |
| 2014–2016 H1 | zones (2014-01, 2015-01, 2016-06 probes) | 2.15 + 2.03 + 0.97 GB | — |
| 2016-07 – 2020-02 | zones; 2018-11: 8,155,449 rows, 117.2 MB | 5.35 GB, 44 files (`R13-ML-DATA-CLAUDE.md:219-223`) | — |

- **Totals.** 2014-01 → 2020-02 ≈ **10.5 GB**; 2009–2013 ≈ **17.9 GB**.
- **The "zone IDs from July 2016" date** for the original CSV switch is **UNVERIFIED** from a primary source.
  Irrelevant for factors: Syed et al. built the bundle factors from *zones*, assigning random boarding nodes
  (`S/syed2021_ffutr.txt:1189-1193`).
- **Tooling.** pyarrow is absent in both local environments (`R13-ML-DATA-CLAUDE.md:243-245`). Reading the parquet
  files needs an owner-approved install; none was done.

### 3.2 Rebuilding the 15-min factor (Syed et al. 2021) [V, from saved files]

- **Formula.** Supplement eq. S1: "we sum the total duration of all trips in the data starting within a 15-minute
  interval … the total trip duration is computed based on free-flow fastest-paths of OSM … the travel time factor … is
  defined as [tod_data / tod_ff-fp]" (`S/syed2021_DataSheet1_section1_excerpt.txt:12-16`).
- **Filter.** Speeds 1–30 m/s, Manhattan to Manhattan (`S/syed2021_ffutr.txt:1189`).
- **Local inputs** (R13 §2.3): the bundle's `nn_fastest_tt.npy` and `node_zone_info.csv`.
- **Validation gate, mandatory before any use.** Rebuild 12–18 Nov 2018 and require, for example, median |relative
  error| ≤ 3% per bin. The speed-distance definition is unknown and must be fixed by this gate alone.
- **Latency.** The factor of bin b uses trips starting in b (`S/factor-definition-checks-2026-10-09.txt:2-8`), so it
  is fully known only after those trips end (about +15–30 min) [I].

### 3.3 NOAA weather [M / V-web]

- **Hourly LCD for Central Park (station 72505394728) is available** through the NCEI access service, verified for
  15–16 Nov 2018 (86 rows) and 8 Feb 2013 (59 rows) (`F/noaa-lcd-centralpark-*.csv`).
- **Causal hourly features:**
  - `HourlyPrecipitation` ("preceding hour", `F/noaa_lcd_documentation.txt:233`);
  - `HourlyPresentWeatherType` (SN, +SN, −SN; "+ = heavy", `:309,332-333`);
  - `HourlyVisibility`;
  - temperature.
- **Not causal, labels only.** `DailySnowfall` and `DailyPrecipitation` are summary-of-day rows stamped 23:59 (15 Nov:
  16.3 cm, 29.46 mm, in my CSV), and the GHCND daily totals. They may only define *which days are events*.
- **Event counts** (GHCND Central Park, weekdays, holidays not removed):

  | Period | Snow ≥ 1 in | Snow ≥ 3 in | Rain ≥ 20 mm |
  |---|---|---|---|
  | 2009–2013 | 26 | 15 | 72 |
  | 2014-01 – 2020-02 | 34 | 19 | 79 |
  | 2013 alone | — | 2 (8 Feb, 8 Mar) | — |

  Sources: `F/noaa-event-days-2009-2013-2026-10-10.txt:2-5`; `S/noaa-event-days-2026-10-09.txt:6`.
  - **That gives 34 heavy-snow weekdays in 2009–Feb 2020** (one of them the bundle test day) and about 151 heavy-rain
    weekdays.
- **The Fielbaum & Alonso-Mora window (14–25 Jan 2013)** had no snow on Monday–Thursday; there was 17.5 mm of rain on
  16 Jan and 38 mm of snow on Friday 25 Jan, which they excluded (`F/noaa-event-days-2009-2013-2026-10-10.txt:6`).

### 3.4 Domain shift 2013 → 2018 [M, TLC monthly indicators saved in R13]

| Measure | 2013-11 | 2015-11 | 2016-11 | 2017-11 | 2018-11 |
|---|---|---|---|---|---|
| Yellow trips per day | 479,527 | 377,076 | 336,737 | 309,471 | **271,501** |
| HVFHV (app) trips per day | — (none reported) | 163,178 | 318,664 | 517,191 | **691,379** |
| Yellow avg minutes per trip | 12.9 | (20.4, suspicious) | 15.9 | 14.8 | 15.2 |

Sources: `S/tlc_data_reports_monthly.csv:860,772,768,700,696,628,624,556,552`.

- Yellow trips fell 43% and app trips appeared. A yellow-only factor in 2013 samples a different traffic mix.
- Use: within-day *growth* (log-residual) models with a year effect. Never mix absolute levels across years.
- 2013 days could also not be simulated without new demand and fixtures, on a 2019 network (§4.4).

---

## 4. A fair evaluation design (what a strict reviewer would accept)

### 4.1 Information at quote time (the leakage rules)

**Allowed:**
- same-day factors of bins finished at least L bins before t0. L = 1 is primary (realistic); L = 0 is the simulator
  idealisation, reported as a sensitivity;
- historical factors from training days only;
- METAR/LCD hourly rows with timestamp ≤ t0 − 10 min;
- calendar (weekday, federal holiday);
- for the outcome-feedback variant, alights already observed by the operator.

**Forbidden:**
- any bin after t0 of the test day;
- daily totals of the test day (GHCND SNOW/PRCP, LCD DailySnowfall);
- test days inside any profile vintage;
- any threshold, quantile or parameter tuned with test outcomes;
- NWS forecasts, unless archived with issuance time ≤ t0 [UNVERIFIED availability].

### 4.2 Stage 1, the offline factor-forecast benchmark (the only way to get many incident days)

- **Units.** Event days are the independent clusters, not riders or cells.
- **Splits.**
  - Primary: rolling origin by winter, following FPP3. Train on all earlier seasons, test on the next one.
  - Seasons: 2014-15 … 2019-20 from the official zone data, optionally preceded by 2009-13.
  - The bundle week 12–18 Nov 2018 is **excluded from training and from Stage-1 testing**. It is reserved for the
    validation gate and Stage 2.
  - Expected test events, if 2009-13 is used for training only: about 18 heavy-snow and about 60 heavy-rain weekdays
    in 2014–2020, against about 1,300 normal weekdays.
- **Quotes.** Every 15-min origin from 06:00 to 20:00. W ∈ {600, 900, 1,200, 1,800} s. Truth = stretch along the
  rebuilt factors. The simulator's hold rule is not needed offline.
- **Baselines (all sealed).**
  - NAIVE;
  - HIST-k: k-week same-weekday mean profile, plus the bundle's 2/3-day vintage for continuity;
  - damped trend with parameters chosen on training folds;
  - uniform pad;
  - ORACLE.
- **Candidates (at most 3, specified before any test factor is computed).**
  1. REGB-q: the gate threshold is the **99th percentile of f/m over normal training weekdays**, not chosen on any event.
  2. W-gate: switch to BLEND when METAR shows SN/+SN, or visibility ≤ 1 km.
  3. A weather-conditioned growth regressor, e.g. ridge or boosting on log-growth with time of day, current residual,
     residual trend at lag L, precipitation rate, visibility, snow flag and minutes since onset, with a 0.9-quantile
     version for lateness control.
- **Metric at equal quote cost.**
  - Primary: late60 on incident days, with each method scaled (D = P0 + c·(D_M − P0)) so that its mean extension on
    *normal training* days equals HIST's.
  - Also: early60, MAE, the cost–lateness frontier over c, and late120/late300.
  - Non-inferiority on normal test days: Δlate60 ≤ +0.1 pp and Δext ≤ +1 s.
- **Uncertainty.** Cluster bootstrap over event days; a per-event forest plot; event-type strata (snow / rain).
- **Sealed predictions (examples).**
  - P1: the validation gate passes.
  - P2: REGB-q is non-inferior on normal days.
  - P3: REGB-q cuts incident late60 by ≥ 25% relative in ≥ 60% of snow events, with a CI excluding 0.
  - P4: the W-gate adds ≤ 1 pp beyond REGB-q. This is the test of "(b) small".
  - P5: the regressor cuts 60-min growth MAE on incident days by ≥ 10% relative to REGB-q. This measures (b).
- **Kill rules.**
  - P1 fails → stop; no factor claims.
  - P2 fails → drop the candidate.
  - P3 fails for all candidates → report a negative result and do not go to the simulator.

### 4.3 Stage 2, a frozen transfer check in the simulator (zero runs)

- Apply the Stage-1 winner, frozen and trained without any 2018-11 data, to the 8 saved snow runs and the 21 weekday
  cells, with the existing replay (`F/rider_nowcast_replay.py`; sanity check 0.000 ms).
- Metrics: Y60 / E60 / ext against the first displayed promise, at equal quote cost against HIST, a uniform pad and the
  oracle.
- Label: "transfer check on an already-seen event". It is n = 1 and **not confirmatory**.
- Example prediction: snow late riders 34 → ≤ 25; weekday ≤ 3; snow ext ≤ +10 s; weekday ext ≤ +1 s.

### 4.4 Stage 3 (optional), new simulated incident days

- **Needs:**
  - a new world-wrapper version: today's wrappers read factors only from the bundle
    (`tang3/world/preflight_world.py:51-55,71`), whitelist window starts (`:56`; v1.3 `:49,143`), and guard the base day
    against the scenario (`preflight_world_v1_3.py:145`);
  - new demand files in FleetPy format;
  - new fixtures through the normalizer, which wrote the panel-A extras **into `C:/Code/RideBound-noworse`**
    (`tang3/calib/panelA/prepare_panelA.py:4-7`) and drops cells at the 96-node cap (11 of 49 were dropped, `:1-2,6,38`).

  That is repository work in a worktree, off-limits in this round. Whether the preflight accepts external demand is
  **UNVERIFIED** (`R13-ML-DATA-CLAUDE.md:331-332`).
- **Runs**, for example 4 extra snow weekdays in 2017–2018 (2017-03-14, 2018-01-04, 2018-03-07, 2018-03-21) × 2 windows
  × 4 samples × {C-30, U} = **64 jobs**. At about 15 min per job with 6 in parallel, that is about 3 h of compute
  (`claude-work/RUNTIME-ESTIMATE-2026-10-07.md:24-25`), plus fixture building.
- **Structural limit.** The simulator has one city-wide factor and 2-h windows, so storm effects remain in the
  1–2 minute band (§0.1). Spatial closures cannot be represented (`R13-ML-DATA-CLAUDE.md:323-324`).

### 4.5 Effort (my estimates; undergraduate, with tests)

| Stage | Hours | Simulator runs | Blocking dependency |
|---|---|---|---|
| S0: put §1.5 into the results chapter as a labelled limitation | 2–3 | 0 | none |
| S1: offline benchmark (download about 10.5 GB [+ 17.9 GB optional], factor builder + gate 8–12 h, LCD features 3–4 h, harness and bootstrap 8–12 h, sealed plan + independent check + write-up 8–12 h, environment and setup 2–4 h) | **35–50** | 0 | pyarrow install approval; disk (E: ≥ 40 GB free) |
| S2: frozen transfer replay | 3–4 | 0 | S1 |
| S3: new simulated days | 30–45 + risk | about 64 | repository worktree, normalizer, demand pipeline |

---

## 5. Verdicts

### 5.1 The owner's 2013 idea

**The Fielbaum & Alonso-Mora 2020 data as such: REJECT for Q5.**
- They chose 13–15 h so that "traveling times are somewhat stable, which allows us to disregard unreliability due to
  traffic conditions" (owner PDF text extraction lines 573-575).
- They used 15/01/2013 and ten weekdays from 14/01/2013 (lines 572-573), with no snow day in the window (§3.3).
- Their model is Alonso-Mora et al. 2017, where edge times are "given by the daily mean travel time estimate", and
  "Shortest paths and travel times between all nodes are then precomputed and stored in a lookup table" [V-web,
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5255617]. There is no traffic dynamic to learn from.

**The raw 2009–2015 TLC archive: MAJOR REVISION**, i.e. usable only as extra training *events* for the Stage-1
benchmark:
- it adds 15 heavy-snow weekdays in 2009–2013;
- year effects are needed (§3.4);
- coordinates are not required (zones suffice), and the official 2013 files no longer have them.

It is the same data family as Donovan & Work's 2010–2013 study, so there is no novelty in it.

### 5.2 Q5 direction as a thesis component, scored by the strict-reviewer standard

| Criterion | Score | One-line reason |
|---|---|---|
| Novelty | 1/5 | Change-point/regime forecasting, weather fusion, NYC taxi anomaly detection, conformal widening and routing-ETA post-processing are all prior (§2) |
| Significance | 2/5 | In this simulator, incident lateness is 60–120 s (0.69% > 120 s even naive), and rule C is unaffected (9 s dispatch) |
| Technical soundness | 3/5 | Causal accessor, leak test and exact reproduction of the sealed layer; but the simulator reveals the current factor with zero latency, and the gate is post hoc |
| Experimental rigor | 1/5 now (3–4/5 with S1) | One event and one cluster, retrospective, threshold seen |
| Reproducibility | 4/5 | Scripts plus mode-"x" outputs plus a 0.000 ms sanity check; no seal |
| Feasibility before mid-November | 2/5 (S1) / 1/5 (S3) | S1 is 35–50 h plus an install approval, competing with the results chapter |

- **Verdict: MAJOR REVISION, i.e. future work.** It is not ready for the thesis before the deadline. S0, the
  diagnostic paragraph, is **ACCEPT**.
- **The most damaging reviewer question:** "With a single incident afternoon, and a gate threshold that sits between
  the weekday maximum (1.244) and the snow minimum (1.323) you had already seen, why is the 34 → 19 gain not tuning on
  the test event, and how much survives realistic data latency?"
- **Can the current evidence answer it?** Only partly. Latency is answered (34 → 29 with one-bin lag). The tuning
  question is not: only the multi-event benchmark (S1) answers it.

### 5.3 Overall recommendation for Q5 [O]

1. **Keep the single storyline** (rule C + promise-layer forecast, zero-run results chapter).
2. **Answer Q5 in the thesis with one honest paragraph and a small table**, labelled retrospective:
   - forecast + C fixes ordinary rush hours (2/1,471 late);
   - on the one measured storm, 7% of late-seconds were anticipated;
   - a causal snapshot nowcast would have added about 26%, mostly lost with realistic latency;
   - about 67% is not knowable from traffic history;
   - dispatch caused 0.3%, so rule C is not implicated.
3. **List the S1 benchmark as future work**, with the exact protocol of §4: rolling-origin by winter, event-day
   clusters, normal-day-calibrated gate, equal-cost metric, sealed predictions and kill rules. This answers "can it be
   done FAIRLY?" with a concrete yes, without spending the remaining weeks on it.
4. Do **not** run the Round-12 damped-trend protocol: as specified, it returns the current method (beta = 0).

---

## 6. Unverified, failed, and disclosures

- **UNVERIFIED:**
  - non-null 2013 coordinates in the Azure copy;
  - the month of TLC's coordinate → zone switch;
  - the content of Koesdwiady et al. 2016 (TVT);
  - NWS forecast archives;
  - whether the preflight accepts external demand;
  - the exact definition of TLC's "Avg Minutes Per Trip", including the suspicious 20.4 in 2015-11;
  - DoorDash ETA posts (403; not used).
- **Failed fetches:** PNAS (403; the PMC copy was used); the Illinois Databank, ICPSR and Princeton DSS (403 or a bot
  wall); INFORMS (403; the author-hosted PDF was used).
- **Disclosure 1, the first Azure footer probe.** My first try reused the R13 footer probe on an Azure blob. Azure
  ignored the open-ended byte range and returned the whole 23 MB object into memory. My script saved nothing, but the
  tool harness stored the 63 MB console capture at
  `C:/Users/quang/.claude/projects/e--Code-RideBound/4f238113-…/tool-results/bgjqhdjkm.txt`, outside the project. I did
  not delete it. `F/azure_footer_probe.py` uses closed ranges and refuses any response above 2 MB.
- **Disclosure 2, copied PDFs.** Two PDFs cached by WebFetch were copied into `F/` for text extraction: the NOAA LCD
  documentation (436 KB) and Gardner & McKenzie 1985 (author-hosted copy, about 0.3 MB).
- **Files in `F/`:**
  - scripts: `factor_nowcast_screen{,_v2}.py`, `rider_nowcast_replay{,_v2}.py`, `azure_footer_probe.py`,
    `noaa_event_days_2009_2013.py`;
  - outputs: `factor-nowcast-screen{,-v2}-2026-10-10.txt`, `rider-nowcast-replay{,-v2}-2026-10-10.txt`,
    `parquet-footer-probe-2013-2026-10-10.txt`, `parquet-footer-probe-azure-2013-01-2026-10-10.txt`,
    `tlc-yellow-sizes-{2009-2015,2016h1}-2026-10-10.tsv`, `noaa-event-days-2009-2013-2026-10-10.txt`;
  - data samples: `noaa-lcd-centralpark-2018-11-15-16.csv`, `noaa-lcd-centralpark-2013-02-08.csv`,
    `noaa-ghcnd-centralpark-2009-2013.csv`, `azure-nyctlc-yellow-2013-01-listing.xml`;
  - documents: `noaa_lcd_documentation.{pdf,txt}`, `gardner_mckenzie_1985.{pdf,txt}`;
  - empty stderr logs: `v2.err`, `replay.err`, `replay2.err`.
- **Re-run commands** (FleetPy environment, `PYTHONIOENCODING=utf-8`, new output names):
  `python -B factor_nowcast_screen_v2.py <out>` (about 13 min) and `python -B rider_nowcast_replay.py <out>` (about
  5 min; reads 29 saved transcripts read-only).
