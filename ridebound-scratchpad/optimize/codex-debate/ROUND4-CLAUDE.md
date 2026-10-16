# Round 4 (2026-10-07): independent survey + own ideas. Then round 5 = cross-review.

## Working rules for this round (new permissions from the owner)

- You may now **write files, but only inside your working directory**
  `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work` (the sandbox enforces this; Claude
  tested it). Never delete or overwrite a file you did not create in this round. No git commands.
- You may read anything. Do **not** read `optimize/codex-debate/claude-work/` in this round: Claude is surveying the
  same questions independently, and we will compare in round 5.
- Web search is enabled. Downloading a PDF into `codex-work/pdf/` is allowed when it helps you verify a claim.
- Zero hallucination: every claim from the literature needs a URL or DOI plus a short verbatim quote and the page or
  section; if you only saw an abstract or a snippet, label it `[abstract only]` or `[snippet only]`. Every number from
  our runs needs a file path and line, or a script you wrote and ran (save script + output in `codex-work/`, output
  files opened in mode "x").
- Local material you may use: `E:/RideBoundData/literature-survey-2026-10-06/` (your earlier corpus),
  `E:/Code/RideBound/docs/research/ridepooling-service-constraints-survey-2026-10-06.md`,
  `C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md` (the thesis claim boundary: dynamic insertion,
  ETA limits, reassignment, route similarity, least-commitment, time consistency and user satisfaction are NOT novel),
  `business-need/`, `optimize/`, `tang3/`.

## The owner's questions (paraphrased from Vietnamese)

1. Why are so few riders delayed by pooling? Is it simply that our scale is too small? A paper on the same dataset
   reported a much higher sharing rate; what do studies on this dataset report, and why?
2. Has anyone already promised arrival times using a traffic forecast? Traffic forecasting is common; is our promise
   layer a contribution at all? What is our forecast algorithm, and is the "traffic" real or fabricated?
   (Facts for you: the forecast is a historical-average time-of-day profile, see `optimize/display_layer.py:1-20` and
   `optimize/promise_stretch.py:1-15`; the world traffic is FleetPy's measured citywide 15-min factor file.)
3. Should we keep promising this way, or change the promise so the ledger still **accumulates**, but counts both the
   system-caused part (c) and the traffic part (x) in one budget? Would that collide with the essence of the deadline
   rule?
4. Find a direction that **optimizes** something with a measurable trade-off (algorithm, rate, budget, padding,
   threshold...), not just "another approach".

## Your tasks (write two files in `codex-work/`)

**A. `SURVEY-CODEX.md`** (max ~2,500 words), one section per question:
- **S1. Pooling rate and scale.** Studies using the FleetPy Manhattan data (Zenodo 15187906) or NYC taxi ride-pooling
  simulations: shared-ride share or pooling rate, fleet size, demand sample, max wait, max detour. What drives the
  rate (demand density, fleet, constraints)? Place our numbers (22.8% shared under U; 108 requests, 8 vehicles,
  96 nodes, 10-min window, 1.5x ride) on that map.
- **S2. Forecast-aware promising.** Prior work that quotes or promises arrival/ETA times using traffic forecasts or
  historical time-of-day profiles: ride-hailing ETA (e.g. Uber DeepETA, DiDi), food-delivery promised times
  (Meituan, Ele.me, DoorDash), time-dependent vehicle routing and dial-a-ride, promise/quote-time optimization.
  Conclude: which parts of our display layer are known, and what (if anything) is left as a contribution.
- **S3. Budgets that combine operator-caused and exogenous delay.** On-time-performance and SLA definitions with
  excusable delays (e.g. 49 CFR 37.131 and Appendix D, transit OTP), robust or chance-constrained time windows,
  schedule slack / recovery time / buffer time in transit and airlines. Conclude on question 3.
- **S4. Optimization levers with trade-offs.** Promise padding vs conversion (quoted lead time), quantile ETAs,
  pooling reserves, time-window tightening, wait/detour constraint tuning, Pareto reporting.

**B. `IDEAS-CODEX.md`**: at most 4 optimization directions for THIS thesis, ranked. For each give:
1. what is optimized and over which decision variable;
2. the trade-off curve to report;
3. novelty status against S1–S4 and the claim boundary;
4. a zero-run test that can be done now on saved outputs (cite which files), if any;
5. the run cost (jobs) if runs are needed, reusing the existing runner, fixtures and wrappers;
6. a falsifiable prediction and a kill criterion.

Also answer question 3 directly in `IDEAS-CODEX.md`: what exactly a "combined c + x budget" would be in our notation
(x = e − v, c = p − e, z = p − v = x + c), which existing arm it is equivalent to (if any), and what changes if the
first promise is forecast-aware.

Finish with a short final message listing the files you wrote. Answer in English.
