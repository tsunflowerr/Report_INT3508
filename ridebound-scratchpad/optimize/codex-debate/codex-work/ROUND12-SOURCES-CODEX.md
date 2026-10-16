# Round 12 primary-source evidence

Access scope and locations are explicit. Abstract-only records are not treated as full method inspections. Expected strength on RideBound is a judgement, not an empirical result. The two unpaginated websites are identified by section rather than an invented page number.

## S1. Seasonal naive: primary textbook, not a new traffic paper

Hyndman and Athanasopoulos, Forecasting: Principles and Practice, third edition, ?5.2, Seasonal naive method (HTML is unpaginated).

[Seasonal naive: primary textbook, not a new traffic paper](https://otexts.com/fpp3/simple-methods.html). Verbatim: ?the last observed value from the same season?.

Repeats the corresponding previous seasonal observation; daily and weekly seasons are distinct modelling choices. The textbook is used for the canonical definition, not evidence that it wins on Manhattan.

## S2. Historical average, corrected profile and SARIMA

Williams and Hoel (2003), Modeling and Forecasting Vehicular Traffic Flow as a Seasonal ARIMA Process, Journal of Transportation Engineering 129:664?672; verified PDF pp.664, 667, 669, 672, equations (8)?(9) and Table 5.

[Historical average, corrected profile and SARIMA](https://www3.nd.edu/~busiforc/handouts/ARIMA%20Engineering%20Article.pdf). Verbatim: ?the ratio of the most recent observation to its corresponding historical average?.

The corrected-history forecast multiplies that ratio by the historical forecast-interval average; verified PDF page 7, equations (8)?(9). Original SARIMA uses weekly season 672, fitted on multiple weeks. Its outcomes are freeway flow, not citywide travel-time factors. PDF page 7 is the pinpoint location used here to avoid ambiguities in extracted printed-page headers.

## S3. Damped exponential smoothing: selected published challenger

Gardner and McKenzie (1985), Forecasting Trends in Time Series, Management Science 31:1237?1246; verified printed p.1237 and p.1238, equations (4)?(6), PDF pages 2?3 (JSTOR cover is page 1).

[Damped exponential smoothing: selected published challenger](https://www.bauer.uh.edu/egardner/3301H%20Operations%20Management/ESG%20Publications/1985%20Forecasting%20trends.pdf). Verbatim: ?an exponential smoothing model designed to damp erratic trends?.

The paper tests general time series, not traffic. Applying its level/trend recurrence to normalized log factor residuals is an explicit adaptation. No performance superiority on our data is claimed.

## S4. Kalman prediction

Chien and Kuchipudi (2003), Dynamic Travel Time Prediction with Real-Time and Historic Data, Journal of Transportation Engineering 129:608?616; publisher/author-repository abstract verified, full PDF not verified. Page range is bibliographic, not an asserted pinpoint PDF page.

[Kalman prediction](https://digitalcommons.njit.edu/fac_pubs/13935/). Verbatim: ?continuously updating the state variable as new observations?.

Tagged EZ-pass vehicles scanned at roadside terminals supply real-time and historical link/path travel times. The abstract reports a Kalman filter and a path/link comparison; it does not specify a directly transferable scalar-factor parameterization.

## S5. Nearest-neighbor traffic forecasting

Oswald, Scherer and Smith (2000), Traffic Flow Forecasting Using Approximate Nearest Neighbor Nonparametric Regression, UVA technical report UVA-CE-ITS_01-4; verified printed p.44, PDF p.54, ?4.4.1, and printed p.45, equation (7).

[Nearest-neighbor traffic forecasting](https://rosap.ntl.bts.gov/view/dot/15834/dot_15834_DS1.pdf). Verbatim: ?one lagged measurement?.

The freeway state vector uses current/lagged flow plus historical current/next-interval averages. A library of earlier states supplies neighbors; multi-horizon scalar-factor matching would be an adaptation.

## S6. Gradient boosting

Zhang and Haghani (2015), A gradient boosting method to improve travel time prediction, Transportation Research Part C 58:308?324; indexed publisher abstract verified, full PDF not verified.

[Gradient boosting](https://www.sciencedirect.com/science/article/pii/S0968090X15000741). Verbatim: ?travel time data provided by INRIX along two freeway sections in Maryland?.

The paper models freeway travel time using boosted regression trees. A lag-and-time feature scalar-factor model is feasible computationally but is not a replication of the study or proof of incident performance.

## S7. LSTM

Ma, Tao, Wang, Yu and Wang (2015), Long short-term memory neural network for traffic speed prediction using remote microwave sensor data, Transportation Research Part C 54:187?197; indexed publisher abstract verified, full PDF not verified.

[LSTM](https://www.sciencedirect.com/science/article/abs/pii/S0968090X15000935). Verbatim: ?travel speed data from traffic microwave detectors in Beijing?.

The observed target is traffic speed. Our factor series could feed a univariate LSTM, but the paper supplies no guarantee of useful accuracy from seven full daily series.

## S8. Graph traffic predictor

Li, Yu, Shahabi and Liu (2018), Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting, ICLR; verified PDF p.5, ?4.

[Graph traffic predictor](https://arxiv.org/pdf/1707.01926). Verbatim: ?207 sensors and collect 4 months of data?.

METR-LA and PEMS-BAY provide traffic-speed sensor networks, with 4 and 6 months of observations. A single citywide factor has no observed spatial graph; duplicating it across nodes would not recreate these data.

## S9. Road-ETA historical baseline

Derrow-Pinion et al. (2021), ETA Prediction with Graph Neural Networks in Google Maps; verified PDF p.5, ?3.2.2, Historical travel times baseline.

[Road-ETA historical baseline](https://arxiv.org/pdf/2108.11482). Verbatim: ?averaged across last 17 weeks?.

Historical hour-of-day/day-of-week segment speeds are summed into travel-time estimates; live data and traversal labels also appear in the system. Our two-day profile is much thinner and aggregated.

## S10. Fixed drop deadline

Schulz and Pfeiffer (2026), Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem, OR Spectrum 48:541?586; verified PDF p.9 / printed p.549, ?3.1; deadline equation l_i=B_i+l; default 900 s at PDF p.22 / printed p.562.

[Fixed drop deadline](https://link.springer.com/content/pdf/10.1007/s00291-026-00847-0.pdf). Verbatim: ?customers can never be rejected after acceptance?.

A fixed deadline after the accepted offered arrival is the relevant rule. Potential-based insertion, acceptance probabilities, precomputation and reassignment are additional parts of their algorithm; Mplus is not a reproduction of those parts.

## S11. Traffic-relative recovery strategy B

H?rl and Zwick (2022), Traffic Uncertainty in On-Demand High-Capacity Ride-Pooling, conference paper, manuscript p.8; verified local primary-paper extraction, ../claude-work/pdf/hoerl-zwick-2022.txt:536 and :546.

[Traffic-relative recovery strategy B](https://doi.org/10.3929/ethz-b-000561639). Verbatim: ?not dropped off later than what is the absolute minimum?.

Strategy B traverses assigned routes using current traffic, updates violated onboard drop bounds, allows new pickups subject to those bounds, and penalizes original-constraint violations. The local extraction includes the 2022 ETH metadata; public PDF text extraction through web was incomplete.

## S12. Controlled assignment scenarios

Fielbaum and Alonso-Mora (2020), Unreliability in ridesharing systems: Measuring changes in users? times due to new requests, Transportation Research Part C 121:102831; verified printed p.17 / PDF p.17, ?6.4 and Table 5.

[Controlled assignment scenarios](https://autonomousrobots.nl/assets/files/publications/20-Fielbaum-TRC.pdf). Verbatim: ?maximum waiting time is updated to the predicted one?.

Fully controlled protects assigned requests from subsequent rejection and increases in waiting time; intermediate protects against late rejection only. Reassignment remains allowed. This is not a cumulative drop-ETA budget.

## S13. Latest-pickup tightening

Alonso-Mora et al. (2017), On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment, PNAS 114:462?467; verified printed p.465 / PDF p.5 in the author copy containing a correction cover.

[Latest-pickup tightening](https://autonomousrobots.nl/assets/files/publications/17-alonsomora-ridesharing-pnas.pdf). Verbatim: ?its latest pickup time is reduced to the expected pickup time?.

Assigned requests can be rematched without increased waiting until pickup; after pickup the vehicle is fixed. This is a pickup-time condition, not a drop-promise ledger.

## S14. Industry arrival-time claim

UberX Share official rider page, FAQ about destination time, accessed 2026-10-09; unpaginated HTML, section ?Will I get to my destination later??.

[Industry arrival-time claim](https://www.uber.com/us/en/ride/uberx-share/). Verbatim: ?any additional pickups won?t increase your estimated arrival time?.

This states a matching objective/product assurance. The page does not disclose the production optimizer, initial padding, stochastic guarantee or attributed cumulative budget; those cannot be inferred from it.

