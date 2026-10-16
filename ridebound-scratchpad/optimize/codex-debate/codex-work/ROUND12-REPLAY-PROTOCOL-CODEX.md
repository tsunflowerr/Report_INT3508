# Round 12: exact zero-run challenger protocol

Status: proposed, retrospectively specified protocol, not an executed comparison or an unseen-outcome preregistration. These dates and incident outcomes have already been inspected. No simulation or new fitting was performed in Round 12.

## R1. Question, scope and information gate

Compare a Gardner-McKenzie damped-trend adaptation against current live-anchored historical shape, with uniform padding as a control, on the SAME saved C-30 journeys. The published recurrence is pinned in [S3](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND12-SOURCES-CODEX-v2.md:17). Its application to log factor residuals is our explicit adaptation; no claim of replicating a traffic experiment or of established superiority is made.

At each first published drop quote, use its source-ordered publication time t0, original current-snapshot ETA P0, chosen plan and the traffic snapshots already delivered to the runner. No actual arrival A, later plans, final vehicle, sharing, signed future ledger sums, future-day factor bins or unpublished simulator state are predictor inputs. Hash the effective transcript/config/world/runner files and maintain the all-first-promises population; actual-error metrics use completed riders. Do not silently discard accepted unfinished riders from quote-cost denominators.

Important: the runner receives routing snapshots, not the latent world factor ([source](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/world/preflight_world.py:15)). Estimate the observed level from those same snapshots: q_b = median over fixed positive OD pairs of T_b(i,j)/T_start(i,j). Select pairs from the first full snapshot, sorted by node IDs, discard zero initial times, and require every selected pair at each used update. q_0=1. Update once per observed 15-minute bin, through the last source-ordered snapshot preceding the quote; assert identical matrices for extra snapshots in that bin. Missing bins receive prediction-only propagation, not hidden factor observations. A failed uniform-factor/snapshot-availability assertion blocks this specified method before inspecting outcomes. Exact latent current factors from the world CSV are NOT substituted online. Historical factors are legitimate completed training records; report snapshot-proxy discrepancies separately as a retrospective diagnostic after quotes are frozen.

The historical comparator receives the same available snapshots and history but uses only current-snapshot P0 and historical growth shape. Giving the challenger a model of the causally observed prefix is permissible; giving it unreleased factor observations is not.

## R2. Fixed history and exact damped forecast

Fit-period information is November 12/13 only. Let m(k) be their arithmetic mean factor at absolute 15-minute clock bin k. For each window start s, historical normalized shape M_b=m(s+b)/m(s). Do not interpolate hourly November 11 into fictitious quarter-hour samples. Define observed log residual r_b=log(q_b/M_b).

Initialize level l_0=0 and trend v_0=0 separately at every scenario-window start; no pre-window same-day prefix is allowed. At each newly observed b use:

    l_b = alpha*r_b + (1-alpha)*(l_(b-1) + phi*v_(b-1))
    v_b = beta*(l_b-l_(b-1)) + (1-beta)*phi*v_(b-1)
    rhat_(b+h) = l_b + sum(phi**j for j=1..h)*v_b
    qhat_(b+h) = M_(b+h)*exp(rhat_(b+h))

For each unobserved intervening bin, perform l <- l+phi*v and v <- phi*v without an observation update. Predictions after a quote remain frozen even when later traffic becomes visible. Current-bin multiplier is exactly 1; future-bin multiplier is qhat_(b+h)/q_b. Once window-relative bin 8 is reached, hold that quoted forecast value through drain, matching the world contract; quotes already in drain use multiplier 1 thereafter. Use double precision, positive factors and no undocumented clipping or incident rule.

Select one triple from alpha={0.2,0.5,0.8,1.0}, beta={0,0.1,0.3}, phi={0.8,0.9,0.98} (36 candidates). Minimize squared one-step log-residual forecast error on the historical November 12/13 factor paths, separately resetting at clock starts 07,08,14,15,17. This supplies 80 correlated targets (five windows times eight transitions times two days). Training uses historical q_b=f_b/f_start, with m fixed from those same two fit days. This is in-sample parameter fitting, not forecast-validation evidence; overlap and the observed-snapshot proxy mismatch must be disclosed. Break exact loss ties lexicographically by (alpha,beta,phi). No selection on November 14/15/16 arrivals or factor outcomes.

The historical comparator uses g=1 in the current bin and g=M_future/M_current thereafter, held at bin 8. Its profile vintage is also fixed to November 12/13; this is a new fair comparison, not a reproduction of the expanding-vintage published score.

## R3. Quote conversion, chronological calibration and exact cost rule

Apply the existing [piecewise work integrator](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/promise_stretch.py:25): solve integral(1/g) from t0 to S equal to P0-t0. For each method j let delta_j=max(S_j-P0,0), preserving one-sided extension. A whole-horizon stretch is the existing promise-layer approximation, not a generic route predictor with dwell/driver noise.

Calibration: saved C-30 November 14, w07/w08, replicas 3 and 4. Primary tests: November 15 and 16 SEPARATELY, w07/w08, replicas 1,2,4. Incident transfer diagnostic: November 15 w14/w15, replicas 1-4. Seal exact available run keys before outcomes; a missing specified cell is reported as missing rather than replaced. Keep matched methods on identical quotes/cohorts.

Recover original source-trip IDs and exact source-row hashes. There are no trip labels in factor-model fitting. Audit calibration-to-test original-trip overlap and purge overlapping groups from calibration before cost fitting; selection may inspect IDs, not A. Report removals, effective calibration size and grouping. If calibration becomes empty or provenance cannot be recovered, stop. Do not import an unpurged ML pilot split as already certified; [Round 11](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/ROUND11-CODEX.md:13) documents a prior gate failure. Replicas/windows using the same original trips are grouped repetitions, not independent riders/dates.

For E=30 seconds, over ALL remaining calibration first drop promises compute mu_j=mean(delta_j). If mu_j>0, freeze rho_j=30/mu_j and quote F_j=P0+rho_j*delta_j. If mu_j=0, use uniform F_j=P0+30 and mark the method degenerate. The control always uses P0+30. Calibration costs match exactly; test costs can drift and must NOT be rescaled from test outcomes. Freeze coefficients, method code, parameters, input hashes, splits and all test quotes before joining A.

Use the same frozen rule for later displayed drop quotes when measuring churn. Apply it to pickup ETA only as a separately reported feasibility diagnostic: count displayed pickups later than the unchanged accepted latest-pickup limit; do not change dispatcher bounds in this replay.

## R4. Sealed descriptive predictions and decision rule

The following are hypotheses to seal before running this comparison, NOT scores obtained here. Gain means historical Y60 minus damped Y60, in percentage points. Y60 is A-F>60 seconds; early60 is A-F<-60; symmetric accuracy includes both endpoints at +/-60.

1. Weekday/morning gain is at most 0.2 pp on each test date: an intentionally low-headroom prediction, not an equivalence claim.
2. Incident-afternoon gain is at least 1 pp over historical shape in the combined panel, and positive separately in both w14 and w15.
3. A qualifying incident win additionally requires test all-quote mean extension <= historical+1 s, nearest-rank p90 extension <= historical+15 s, and completed early60 <= historical+1 pp. No test-cost retuning is allowed. Report symmetric accuracy alongside the three guards.

Report per-date/window n, coverage, all-quote mean/p90 extension, mean promised horizon, completed Y60/early60/symmetric accuracy/MAE, later-quote churn, and pickup feasibility conflicts. Report completion/pairing filters and source-group counts. Few dates and correlated replicas prevent a population-superiority claim; any uncertainty analysis must keep date/window/source-group clustering explicit.

A guarded incident gain would show additional value of a published adaptive traffic component beyond current corrected history at comparable realized quote cost. A failure or null gain means no demonstrated gain for THIS method, inputs and simulated worlds. It does not show ML is useless or that fewer changes universally dominates prediction. Dispatch coverage, insertion selection and existing deadline violations remain those of saved C-30. Replaying altered quotes cannot evaluate the counterfactual acceptances/forced-reference rates of a newly forecast-aware Mplus or C dispatcher; that policy test needs new trajectories outside this round.
