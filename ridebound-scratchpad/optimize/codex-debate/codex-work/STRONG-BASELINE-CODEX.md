# Round 12: a fair published-baseline comparison

Recommend **Gardner-McKenzie damped exponential smoothing versus current corrected historical shape on identical saved C-30 trips**, at calibrated E=30-second quote cost. This is a credible published challenger, not a demonstrated stronger method. Mplus already represents a published deadline component; replay can test promise forecasting, while changing operational deadlines requires new trajectories. No simulations or new model fitting were performed.

## Verified owner questions

**Q2: yes, among served riders, with qualifications.** C-30 has 33/2,338 riders with nonzero dispatch change (1.411%); only 29 have positive added time (1.240%), four improve. Its 33 event magnitudes have absolute median 8.295 s, p90 27.973, maximum 29.239. U has 174/2,434 exposed riders (7.149%) and 187 events, absolute median 108.636 s. Initial shared detours are already in the first promise; these statistics describe later revisions, not all sharing overhead. The 148 budget-flagged rejections, 116 served by U, and median overshoot 109.6 s reproduce the diagnostic's classification, not an isolated causal effect of removing the cap. WP14r exposure is FREE 23.818% versus C-30 0.391%, alongside service/sharing trade-offs ([F1](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:5)).

**Q3: largely correct, with two corrections.** Project the chosen remaining stop sequence from current vehicle position using one current travel snapshot; pickups start at max(arrival, earliestPickup), and promise ETAs are pickup/drop service starts. First publication is booking confirmation, not necessarily request arrival. Zero dwell is this configuration's setting, not a universal projector assumption. Conditional execution is deterministic, but rounding/discretization residuals can remain. Low lateness reflects coupled simulation, constraints and selected served riders; empirical traffic/demand inputs do not make simulated arrival labels independent real-world observations ([F2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:17)).

## A. Traffic forecasting survey

The signal contains **696 observations**: seven 96-bin days plus November 11's 24 hourly samples. Eight calendar days do not supply repeated weekly cycles or independent spatial sensors. All expected strengths below are judgments; source quotations, pinpoint pages and abstract-only limitations are in the linked index.

| Candidate / primary reference | Target and required data | Fairness, feasibility and expected strength here |
|---|---|---|
| Seasonal naive; Hyndman/Athanasopoulos ([S1](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:5), primary textbook definition) | Repeat prior same-season value; previous full day or week. | Daily version feasible after a full day; weekly version has almost no training replication. Useful cheap control; cannot anticipate a new incident. |
| Historical average / live correction; Williams/Hoel 2003 ([S2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:11)); Google Maps historical baseline ([S9](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:53)) | Time-bin flow history plus current flow; Google's segment ETA baseline averages hour/day-of-week speeds over 17 weeks. | Our current method already anchors historical growth to live travel times. Strong on regular mornings; seven daily curves cannot reproduce 17-week segment histories or distinguish weekly/holiday effects reliably. |
| Seasonal ARIMA; Williams/Hoel 2003 ([S2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:11)) | Freeway flow; original weekly period 672 and multiple weeks. | Original weekly fit is unsupported. A tightly fixed low-order ARIMA/daily-season adaptation is computable, but fragile with two chronological fit days; cannot claim the paper's strength transfers. |
| Damped exponential smoothing; Gardner/McKenzie 1985 ([S3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:17)) | General univariate level/trend series; current/past observations. | Low-dimensional scalar adaptation is feasible. Can react to persistent residual growth beyond the profile; smoothing may lag abrupt changes. Selected challenger. |
| Kalman filter; Chien/Kuchipudi 2003 ([S4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:23)) | Link/path travel times from historical and live EZ-pass roadside scans. | Small scalar state is feasible, but covariance/incident identification is weak; exact paper implementation is unverified. Live-corrected history is already represented, not a new baseline. |
| k-NN; Oswald/Scherer/Smith 2000 DOT report ([S5](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:29)) | Freeway flow states: current/lagged flow and historical present/future averages; neighbor library. | Scalar lag-pattern adaptation feasible; few distinct prior daily patterns constrain neighbor quality, particularly incidents. |
| Gradient boosting; Zhang/Haghani 2015 ([S6](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:35)) | INRIX travel time on two Maryland freeway sections. | Lag/time features are implementable; tiny chronological fit sample makes tuning/incident generalization uncertain. Many simulated riders do not create additional independent factor paths. |
| LSTM; Ma et al. 2015 ([S7](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:41)); DCRNN; Li et al. 2018 ([S8](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:47)) | Beijing microwave-detector speeds; DCRNN uses network speeds, including 207 sensors over four months. | Univariate LSTM can run but has weak sample support. Original graph model cannot be fairly reproduced from one aggregate factor without a measured spatial graph. |

Earlier factor errors, independently reproduced: **mean(max), percentage points of absolute growth-ratio error**, not ETA seconds or relative MAPE. n counts date/origin pairs ([F4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:43)).

| Window | Horizon min | n | Constant-current | Corrected history |
|---|---:|---:|---:|---:|
| 07 | 15 | 56 | 4.88(16.19) | 1.90(6.12) |
| 07 | 30 | 49 | 9.79(27.90) | 2.44(6.91) |
| 07 | 45 | 42 | 14.85(35.63) | 3.08(9.25) |
| 08 | 15 | 56 | 2.62(7.13) | 1.69(6.11) |
| 08 | 30 | 49 | 4.77(10.28) | 1.86(5.99) |
| 08 | 45 | 42 | 6.97(13.42) | 2.70(6.78) |
| 17 | 15 | 56 | 2.33(5.59) | 2.27(8.83) |
| 17 | 30 | 49 | 3.83(9.83) | 3.17(13.22) |
| 17 | 45 | 42 | 5.40(13.78) | 4.13(14.16) |

This old table uses leave-one-out profiles including future dates: it establishes shape similarity, not causal held-out performance. Evening means improve while maxima worsen. Current causal history is stronger evidence.

**Headroom:** weekday oracle stretch matches 1,452/1,452 arrivals within 2 s **only in the zero-total-dispatch cohort**. Historical display gives cell-mean late60 0.17% versus approximately zero for oracle, leaving little regular-day room. The same historical layer also gives Mplus/V 0.17%; that score is not uniquely C's achievement. Snow-afternoon lateness remains 5.94% versus raw 7.19%, with 92.5% of late seconds classified unanticipated. Incident forecasting has substantially more room ([F4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:43)).

## B. Published promise/dispatch components

The implementation audit cites exact config/code locations ([F3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-FACTS-CODEX.md:29)). Full-paper reproduction is distinct from implementing one constraint.

| Published rule | Existing representation / required changes |
|---|---|
| Schulz/Pfeiffer 2026 fixed offered-drop deadline ([S10](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:59)) | Mplus-30 already has anchor+30 s; paper's 900 s slack is config-only. Full potential/reoptimization method needs core code; common traffic recovery changes enforcement. |
| Horl/Zwick 2022 strategy B ([S11](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:65)) | Related no-worse recovery exists. Exact updated onboard bounds, added-pickup feasibility and penalties need core/adapter changes: changed plans currently retain strict physical bounds. |
| Fielbaum/Alonso-Mora 2020 controlled scenarios ([S12](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:71)) | Non-rejection component already common. Configurable pickup ratchet is partial proxy; full reassignment plus absolute accepted pickup-bound updates need core code. Current vehicle/pickup locks are stricter in some dimensions. |
| Alonso-Mora 2017 latest-pickup tightening ([S13](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:77)) | Same partial pickup-lock proxy; accepted-bound tightening with pre-pickup rematching needs core work. Not a drop-ETA budget. |
| UberX Share added-pickup arrival assurance ([S14](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:83)) | Config-only C-0 conservatively forbids absolute dispatch movement, including improvements; a one-sided drop ratchet allows improvements. Neither reproduces the undisclosed optimizer or promises traffic-proof arrival. |
| Corrected-history forecast-aware deadline | Historical forecast is already present in display and saved Mplus-30F. Integrating a new forecast into feasibility needs operational validation/new trajectories; saved forecast-aware runs include feasibility stops. |

## C. One fair comparison to seal

Use the published damped recurrence on **log residuals around a fixed November 12/13 mean profile**, initialized at each window start. Fit 36 fixed alpha/beta/phi triples only on those historical factor paths; choose one-step log-residual SSE minimum, lexicographic ties. Online observed factor is the median current/start OD-snapshot ratio: no latent or future world factors. Exact recurrence, missing-bin handling and integrator are specified in [R1](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md:5) and [R2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md:15).

Calibrate on November 14 w07/w08 r3/r4; test November 15/16 separately, w07/w08 r1/r2/r4. Snow w14/w15 r1-4 is transfer. Audit provenance, purge calibration/test source-group overlap, and keep identical quote cohorts. For each method, delta=max(stretchedETA-P0,0), rho=30/mean_cal(delta), F=P0+rho*delta; zero mean degenerates to uniform padding. Freeze coefficients/quotes before joining actual arrivals. Calibration matches cost; report realized test mean/p90, horizon, early arrivals, symmetric accuracy and pickup conflicts without test rescaling ([R3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md:32)).

Seal descriptive hypotheses: morning gain <=0.2 pp per date; incident gain >=1 pp overall and positive in both windows, requiring mean extension <=history+1 s, p90 <=history+15 s and early60 <=history+1 pp. A guarded incident win supports adaptive traffic prediction beyond corrected history; a null result limits this challenger in these worlds. Neither result establishes dispatch-policy superiority from unchanged C-30 trajectories ([R4](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md:44)).
