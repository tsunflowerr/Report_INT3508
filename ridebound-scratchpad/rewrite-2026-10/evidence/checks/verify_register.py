"""Evidence-register helper (rewrite-2026-10). Read-only; one process; no simulation, build or install.

1. Anchor checks: for each (key, file, line, fragment) the fragment must occur in that line after collapsing
   whitespace; if not, the nearest line within +-3 and the first whole-file hit are reported.
2. Arithmetic re-derivations from the cited output files (R15 audit summary, R18 verification, W07/WP14r outputs).
3. Page-1 identity extracts of two owner/corpus PDFs that have no text extraction.
Output: verify-register-v2-2026-10-10.txt next to this script (v1 output kept: it counted form feeds as line breaks), created with mode "x" (never overwritten).
Usage: python -B -I verify_register.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "verify-register-v2-2026-10-10.txt"

SCR = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad")
DEB = SCR / "optimize/codex-debate"
CW = DEB / "claude-work"
XW = DEB / "codex-work"
PAP = pathlib.Path(r"C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/papers")
SRC = pathlib.Path(r"C:/Code/RideBound-noworse/src")
D03 = pathlib.Path(r"E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md")
ADR = pathlib.Path(r"C:/Code/RideBound-noworse/docs/18-status-and-decision-log.md")
CFG = SCR / "tang3/configs"

FILES = {
    "HZ": CW / "pdf/hoerl-zwick-2022.txt",
    "FAM": PAP / "Unreliability_in_ridesharing_systems_Measuring_cha.txt",
    "SP": PAP / "s00291-026-00847-0.txt",
    "FLEET": CW / "pdf/fleetpy-etrr-2026.txt",
    "LEO": CW / "pdf/leonardi-2024.txt",
    "LUK": CW / "pdf/lu-kuehnel-2024.txt",
    "GM": CW / "pdf/gardner-1985.txt",
    "WAR": PAP / "1-s2.0-S0965856426000662-main.txt",
    "AGZ": PAP / "Value_of_time_and_reliability_for_urban_pooled_on-.txt",
    "MOL": PAP / "OperationalEffectsofServiceLevelVariations-publication151005.txt",
    "SYED": CW / "r13-ml-data-samples/syed2021_ffutr.txt",
    "TLC": CW / "r13-ml-data-samples/tlc_data_reports_monthly.csv",
    "NOAA13": CW / "r16-forecast/noaa-event-days-2009-2013-2026-10-10.txt",
    "D03": D03,
    "ADR": ADR,
    "DELTA": SRC / "RideBound.Application/Promises/PromiseDeltaCalculator.cs",
    "BUDGET": SRC / "RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs",
    "VALID": SRC / "RideBound.Application/Commitments/CommitmentDecisionValidator.cs",
    "LEDGER": SRC / "RideBound.Domain/Commitments/CommitmentLedger.cs",
    "LOCK": SRC / "RideBound.Domain/Commitments/CommitmentLockEvaluator.cs",
    "POLICY": SRC / "RideBound.Domain/Commitments/CommitmentPolicy.cs",
    "PROJ": SRC / "RideBound.Application/Scheduling/RouteScheduleProjector.cs",
    "PPROJ": SRC / "RideBound.Application/Promises/PromiseProjector.cs",
    "SEL": SRC / "RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs",
    "HVA": SRC / "RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs",
    "POL": SRC / "RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs",
    "CCA": SRC / "RideBound.Algorithms/Commitments/CommitmentCandidateAssessor.cs",
    "CSE": SRC / "RideBound.Algorithms/Candidates/CandidateScheduleEvaluator.cs",
    "NORM": SRC / "RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs",
    "DIM": SRC / "RideBound.Domain/Commitments/CommitmentDimension.cs",
    "C30": CFG / "C-30.json",
    "MP30": CFG / "Mplus-30.json",
    "WP4": CFG / "wp4-tier3-v2.json",
    "RUN38": SCR / "tang3/t38/run_t38.py",
    "RUNW07": SCR / "tang3/w07/run_w07.py",
    "AUDIT": SCR / "tang3/evidence/audit_vep.py",
    "SPEC": SCR / "tang3/evidence/METRICS-SPEC.md",
    "DISP": SCR / "optimize/display_layer.py",
    "STRETCH": SCR / "optimize/promise_stretch.py",
    "DIALPY": CW / "r17-rebuttal/r17_verify_dial.py",
    "PREF": SCR / "tang3/world/preflight_world.py",
    "FIX": pathlib.Path(r"C:/RideBoundData/research/fixtures-panelA-v1/d20181114-s10-r3-w08/normalizer-configuration.json"),
    "SERV": DEB / "service-duration-check-2026-10-06.txt",
}

CHECKS = [
    # Hoerl & Zwick 2022
    ("HZ", 507, "To overcome the issue of undefined system states, a simple policy is proposed"),
    ("HZ", 529, "The second strategy (B) is less restrictive"),
    ("HZ", 535, "calculate an updated drop-off time"),
    ("HZ", 535, "for on-board requests that would otherwise violate their constraints"),
    ("HZ", 539, "not dropped off later than what is the absolute"),
    ("HZ", 541, "minimum, given current traffic conditions"),
    ("HZ", 541, "a penalty is added for every"),
    ("HZ", 567, "For strategy (B), for all requests that are assigned to the currently evaluated vehicle"),
    ("HZ", 569, "tk,dropoff required = max tk,dropoff updated , tk,dropoff latest (7)"),
    ("HZ", 575, "The constraints that are evaluated in the routing function are then"),
    ("HZ", 584, "The objective is modified such that it contains a penalty term for constraint violations"),
    # Fielbaum & Alonso-Mora 2020
    ("FAM", 93, "We study how the predicted times for each single request change from its first"),
    ("FAM", 191, "Definition 2. (Unreliability induced by the operators)"),
    ("FAM", 218, "In this paper, we focus on the unreliability induced by the"),
    ("FAM", 295, "In the remainder of the paper we consider the positive values for these indices, and truncate to zero those"),
    ("FAM", 571, "(4091 nodes"),
    ("FAM", 572, "and 9453 edges"),
    ("FAM", 572, "between 1 and 3 pm on 15/01/2013"),
    ("FAM", 573, "we consider ten weekdays starting on Monday 14/01/2013"),
    ("FAM", 574, "traveling times are somewhat stable, which allows us to disregard unreliability due to"),
    ("FAM", 578, "not considered as a weekday"),
    ("FAM", 583, "2000 vehicles capable of carrying 4 passengers"),
    ("FAM", 584, "19610 requests for the two hours period"),
    ("FAM", 957, "it is marked as non-rejectable for future assignments"),
    ("FAM", 958, "maximum waiting time is updated to the predicted one"),
    ("FAM", 975, "The most relevant impact, however, is on the rejection rate, which increases dramatically"),
    ("FAM", 984, "the more controlled the unreliability, the higher the average users' costs"),
    ("FAM", 1038, "The most relevant one is how to control it,"),
    ("FAM", 1039, "to provide more accurate times without increasing the rejection rate"),
    ("FAM", 942, "Base 1.01 0.65 1.66 34.5% 9.56"),
    # Schulz & Pfeiffer 2026
    ("SP", 468, "we limit the maximum time shift in the arrival"),
    ("SP", 469, "We calculate li- = Bi- + l"),
    ("SP", 470, "directly after customer i accepted our offer"),
    ("SP", 487, "After acceptance the customer can be delayed because of"),
    ("SP", 575, "Only Bi- and li- are communicated to the"),
    ("SP", 640, "visited locations in the tour as well as travel times"),
    ("SP", 1197, "was set to 0.5 in our experiments"),
    ("SP", 1204, "is set to 900 s (15 min), which is also done this"),
    ("SP", 1470, "between 0, 5, 10, 15, 20, 25, and 30 min"),
    ("SP", 1494, "small maximum time shift leads to significantly higher rejection rates while a larger"),
    ("SP", 1496, "set the maximum time shift to a value of 10 to 15 min"),
    # FleetPy 2026 (two-column extraction)
    ("FLEET", 346, "4, 410"),
    ("FLEET", 347, "nodes and 9, 574 edges"),
    ("FLEET", 360, "The taxi data set for the week of 11/11/2018 to"),
    ("FLEET", 363, "ing the trips that start and end in Manhattan, 1, 807, 255"),
    ("FLEET", 370, "the day, a scaling factor is calculated for the fastest path"),
    ("FLEET", 423, "Boarding and"),
    ("FLEET", 424, "alighting times are set to 30s per passenger"),
    ("FLEET", 433, "The vehicle fleet consists of 180"),
    ("FLEET", 434, "vehicles, each with a capacity of four passengers"),
    ("FLEET", 448, "rate for all vehicles throughout the day is approximately"),
    ("FLEET", 449, "1.33, compared to 1.31 for both IH and LA"),
    ("FLEET", 474, "For this study, we used FleetPy version 1.0.2"),
    ("FLEET", 477, "on a 10% sample of trip requests (21,400 requests) from"),
    ("FLEET", 478, "12 November 2018"),
    # Other literature
    ("LEO", 1101, "the level of predictability of DRT can be seen as a design parameter of the service"),
    ("LUK", 47, "a small buffer, such as 2 or 3 minutes can be given"),
    ("LUK", 47, "tbuffer is the maximum delay allowed from the initially scheduled pickup time"),
    ("GM", 11, "This paper develops an exponential smoothing model designed to damp erratic trends"),
    ("GM", 70, "the trend is damped and the forecasts approach an asymptote"),
    ("WAR", 615, "2.53 0.133"),
    ("WAR", 617, "MeanLate-X/Y 3.12 0.233"),
    ("AGZ", 25, "(N = 1006)"),
    ("AGZ", 30, "the in-vehicle stage being around 0.5"),
    ("AGZ", 642, "is lesser than that of the announced times"),
    ("AGZ", 872, "individuals are not presented with a situation of lateness"),
    ("MOL", 52, "tional costs for 78 combinations of two service level parameters"),
    ("MOL", 149, "expressed as a fraction of this direct ride time"),
    ("TLC", 552, '2018-11,FHV - High Volume,"691,379"'),
    ("TLC", 556, '2018-11,Yellow,"271,501"'),
    ("TLC", 860, '2013-11,Yellow,"479,527"'),
    ("NOAA13", 4, "2013 only: weekdays 261; snow >= 1 in: 6; snow >= 3 in: 2 ['2013-02-08', '2013-03-08']"),
    # Owner claim boundary (read only)
    ("D03", 7, "per-passenger + path-dependent + multi-dimensional + cumulative/switch budget"),
    ("D03", 56, "Không claim việc phát hiện unreliability, kiểm soát trước quyết định hoặc đánh đổi dịch vụ–ổn định là mới"),
    ("D03", 211, "[Elmi và cộng sự 2026]"),
    ("D03", 215, "dùng hạn chót trả từ thông báo đầu, với độ chùng 900 giây trong thiết lập đã đọc"),
    ("D03", 222, "Phần giữ tuyến là phép chiếu mô hình tại cùng trạng thái, không nhận diện đầy đủ"),
    ("D03", 236, "Không nhận giảm C là tăng hài lòng, giảm trễ thực, tăng doanh thu hoặc giảm công"),
    ("D03", 243, "người vận hành có vấn đề, chi phí và ngưỡng chấp nhận cụ thể"),
    ("D03", 260, "Ngân sách C 30 giây chưa có căn cứ WTP/ROI bên ngoài"),
    ("D03", 267, "0,17% là mean"),
    ("D03", 268, "21 cell active; all34 là 0,51%"),
    # Code
    ("DELTA", 64, "var exogenousDelta = CalculatePair("),
    ("DELTA", 75, "var decisionDelta = CalculatePair("),
    ("DELTA", 86, "var visibleDelta = CalculatePair("),
    ("DELTA", 139, "AbsoluteDifference(before.DropEta, after.DropEta),"),
    ("BUDGET", 51, "var added = before.Add(delta);"),
    ("BUDGET", 88, "if (afterValue > hardLimit)"),
    ("VALID", 222, "// RB-WP14-003. Fail-fast is correct on the hot path"),
    ("VALID", 355, "var oldSchedule = _scheduleProjector.Project("),
    ("VALID", 359, "context.ReducedState.TravelTimes!,"),
    ("VALID", 373, "var exogenousProjection = _promiseProjector.Project("),
    ("VALID", 512, "var charged = policy.BudgetBasis == CommitmentBudgetBasis.DecisionInduced"),
    ("VALID", 518, "priorHistory.Current.BudgetAfter,"),
    ("LEDGER", 285, "var charged = budgetBasis == CommitmentBudgetBasis.DecisionInduced"),
    ("LEDGER", 288, "var after = current.BudgetAfter.Add(charged);"),
    ("LOCK", 158, "exogenous drift never trips a lock"),
    ("LOCK", 186, "var shift = candidate.DropEta.Milliseconds - anchor.DropEta.Milliseconds;"),
    ("LOCK", 188, "if (shift > slack.Milliseconds)"),
    ("POLICY", 243, "Deadline on the drop ETA, measured from the rider's FIRST published promise"),
    ("PROJ", 123, "arrival = time + travelTime;"),
    ("PROJ", 125, "departure = serviceStart + stop.ServiceDuration;"),
    ("PROJ", 143, "var cost = time.Milliseconds - evaluationTime.Milliseconds;"),
    ("PROJ", 163, "return arrival.Milliseconds < request.EarliestPickup.Milliseconds"),
    ("PPROJ", 79, "pickupEta = pickupSchedule.ServiceStartTime;"),
    ("PPROJ", 131, "dropSchedule.ServiceStartTime,"),
    ("SEL", 290, '"forced-reference-count",'),
    ("SEL", 300, '"accepted-request-count",'),
    ("SEL", 323, '"worst-hard-utilization-ppm",'),
    ("SEL", 367, '"operational-cost",'),
    ("SEL", 381, '$"candidate-id-rank:{set.VehicleId.Value}",'),
    ("HVA", 94, "Exploratory no-worse-than-reference recovery"),
    ("HVA", 612, "if (hardLimit == 0)"),
    ("HVA", 625, "worst = PartsPerMillion;"),
    ("POL", 287, "var profile = SolverBackedObjectiveProfile.RollingCost;"),
    ("POL", 325, "var assessed = _hardAssessor.AssessAndFilter("),
    ("CCA", 103, "hardLimit: null,"),
    ("CCA", 108, "finalConfirmationLocks: PromiseLock.None);"),
    ("CSE", 83, "projection.Schedule.OperationalCost));"),
    ("NORM", 326, "configuration.RequestTarget > 128"),
    ("NORM", 327, "configuration.VehicleCount > 32"),
    ("NORM", 328, "configuration.MaximumNodeCount > 96"),
    ("NORM", 444, "checked(arrival + configuration.PickupWindowMs),"),
    ("NORM", 445, "Math.Max(direct, maxRide),"),
    ("DIM", 23, "CommitmentDimension.DropEtaTotalMs,"),
    ("ADR", 5066, "### ADR-077 — 2026-09-26 — Proposed"),
    ("ADR", 5078, 'commitmentRecovery: "no-worse-than-reference-v1"'),
    ("ADR", 5081, "cũng mắc cùng lỗi đó"),
    ("ADR", 5085, "chiều ngân sách: tổng sau ≤ tổng sau của tuyến giữ."),
    ("ADR", 5086, "Khóa pha và khóa xe không bao giờ được miễn."),
    ("ADR", 5124, "no-worse 1874, `forced-reference-v1` 1864, `C` 1873"),
    ("C30", 6, '"budgetBasis": "decisionInduced",'),
    ("C30", 23, '"hardLimit": 30000'),
    ("C30", 91, '"rawEtaThresholdMs": 1000,'),
    ("C30", 94, '"finalConfirmationLocks": ['),
    ("MP30", 98, '"dropEtaDeadlineSlackMs": 30000'),
    ("WP4", 3, '"policyId": "ridebound-hard-vector",'),
    ("WP4", 5, '"initialPromiseTrigger": "booking-confirmation",'),
    ("WP4", 7, '"commitmentRecovery": "no-worse-than-reference-v1",'),
    ("WP4", 10, '"maximumCandidatesPerVehicle": 100,'),
    ("WP4", 11, '"maximumNewRequestsPerVehicle": 2,'),
    ("WP4", 15, '"retentionStrategy": "service-set-stability-portfolio-v1"'),
    ("WP4", 23, '"randomSeed": 7'),
    ("RUN38", 8, "sigma ="),
    ("RUN38", 9, "shockRate = 0) through world wrapper v1.2; recovery rule (b) for every arm"),
    ("RUNW07", 40, 'RUNNER = pathlib.Path(r"C:/RideBoundData/research/runner-tier3-v2")'),
    ("AUDIT", 112, 'for name, value in (("exogenous", abs(e - v)), ("decisionInduced", abs(p - e)),'),
    ("SPEC", 50, "x_t = e_t − v_t c_t = p_t − e_t z_t = p_t − v_t"),
    ("SPEC", 60, "C = Σ|c_t| X = Σ|x_t| V = Σ|z_t|"),
    ("DISP", 5, "D = max(p, S(t, p - t))"),
    ("DISP", 11, "causal-no15 (PRIMARY): prior same-kind days only, 15/11 (documented snowstorm) never a source"),
    ("STRETCH", 6, "integral_{t0}^{t0+D} 1 / g(tau) dtau = W."),
    ("STRETCH", 10, "forecast: g(tau) = 1 in the current bin, m(b(tau)) / m(b(t0)) after it, m = mean of the source days"),
    ("DIALPY", 8, "late_k = A - p0 > k s (p0 = initialPromise publishedPromise drop ETA), early60 = A - p0 < -60 s,"),
    ("DIALPY", 9, "timely_k (per request) = served - late_k,"),
    ("PREF", 6, "96-node OD closure"),
    ("PREF", 15, "FleetPy moves vehicles in the world. The Runner never reads the world"),
    ("PREF", 17, "and it holds them flat into the future"),
    ("FIX", 1, '"pickupWindowMs":600000'),
    ("FIX", 1, '"maximumRideTimePermille":1500'),
    ("FIX", 1, '"vehicleCapacity":4'),
    ("FIX", 1, '"vehicleCount":8'),
    ("FIX", 1, '"requestTarget":108'),
    ("FIX", 1, '"maximumNodeCount":96'),
    ("FIX", 1, '"travelFactorAtSeconds":0'),
    ("SERV", 2, "serviceDurationMs values {0: 16062}"),
]


def collapse(text):
    return re.sub(r"\s+", " ", text).strip()


def load_lines(path):
    # split on LF only, as cat -n / grep -n do; v1 used splitlines(), which also breaks at form feeds
    return [t.rstrip(chr(13)) for t in path.read_text(encoding="utf-8", errors="replace").split(chr(10))]


def anchor_checks(out):
    cache = {}
    ok = fail = 0
    for key, line, frag in CHECKS:
        path = FILES[key]
        if key not in cache:
            cache[key] = load_lines(path) if path.exists() else None
        lines = cache[key]
        target = collapse(frag)
        if lines is None:
            out.append(f"FAIL {key}:{line} file missing {path}")
            fail += 1
            continue
        here = collapse(lines[line - 1]) if 0 < line <= len(lines) else ""
        if target in here:
            out.append(f"OK   {key}:{line} | {frag}")
            ok += 1
            continue
        near = [n for n in range(max(1, line - 3), min(len(lines), line + 3) + 1) if target in collapse(lines[n - 1])]
        anywhere = next((n for n, text in enumerate(lines, 1) if target in collapse(text)), None)
        out.append(f"FAIL {key}:{line} | {frag} | nearby {near} | first hit {anywhere}")
        fail += 1
    out.append(f"anchor checks: {ok} OK, {fail} FAIL; files: " + "; ".join(f"{k}={FILES[k]}" for k in sorted(cache)))
    return ok, fail


def parse_a(out):
    """R15 independent audit summary: one JSON object per line 3-19 (keyed by pop/arm)."""
    lines = load_lines(XW / "R15-audit-summary.txt")
    rows = {}
    for number, text in enumerate(lines, 1):
        if text.startswith("{"):
            row = json.loads(text)
            if "arm" in row:
                rows[(row["pop"], row["arm"])] = (number, row)
    t = {arm: rows[("t38", arm)] for arm in ("U", "C-30", "Mplus-30")}
    req = 3672
    out.append(f"A: 34 cells x 108 requests = {34 * 108} (requests field {t['U'][1]['requests']})")
    for arm, (number, row) in t.items():
        served = row["ledger"]["served"]
        for mode in ("naive", "fc", "fc_pad30", "fc_pad60"):
            f = row["frontier"][mode]
            out.append(
                f"A:{number} {arm} {mode}: served {f['served']} late60 {f['late60']} late120 {f['late120']} "
                f"timely60/req {f['served'] - f['late60']}/{req} = {100 * (f['served'] - f['late60']) / req:.2f}% "
                f"timely120 {f['served'] - f['late120']} late60/served {100 * f['late60'] / f['served']:.3f}% "
                f"early60 {f['early60']} ({100 * f['early60'] / f['served']:.3f}%) mean ext {f['ext_sum_ms'] / f['served'] / 1000:.3f} s")
        led = row["ledger"]
        out.append(f"A:{number} {arm} ledger: exposed {led['exposed']} ({100 * led['exposed'] / served:.2f}%) repeated "
                   f"{led['repeated']} S_max {led['S_max_ms'] / 1000:.3f} s late60_and_exposed {led.get('late60_and_exposed')} "
                   f"util incumbent/bound/present {row['objective']['incumbent_1e6']}/{row['objective']['bound_1e6']}/"
                   f"{row['objective']['util_present']} with_new {row['objective']['with_new']}")
    u, c = t["U"][1]["ledger"]["served"], t["C-30"][1]["ledger"]["served"]
    out.append(f"A: U - C-30 served {u - c}; /3672 = {100 * (u - c) / req:.2f} pp; /U served = {100 * (u - c) / u:.2f}%")
    measured = [r for (pop, arm), (n, r) in rows.items() if pop in ("t38", "w07") and arm.startswith("C-")]
    runs = sum(r["runs"] for r in measured)
    acked = sum(r["acknowledged"] for r in measured)
    rec = sum(sum(r["candidates"].values()) for r in measured)
    step = sum(r["candidates"].get("step-fails", 0) for r in measured)
    cum = sum(r["candidates"].get("cumulative-reported", 0) for r in measured)
    rep = sum(r["ledger"]["repeated"] for r in measured)
    out.append(f"A measured C arms: runs {runs} acknowledged {acked} budget records {rec} step-fails {step} "
               f"cumulative-reported {cum} repeated riders {rep}")
    for pop in ("fixed", "synthetic"):
        for (p, arm), (n, r) in sorted(rows.items()):
            if p == pop:
                out.append(f"A:{n} {pop} {arm}: candidates {r['candidates']} cum_decisions {r['cum_decisions']} "
                           f"cum_finally_rejected {r['cum_finally_rejected']} served {r['ledger']['served']} "
                           f"repeated {r['ledger']['repeated']} S_max {r['ledger']['S_max_ms'] / 1000:.3f} s")


def misc_arithmetic(out):
    out.append(f"C-30 rejected 3672-2338 = {3672 - 2338}; budget-blocked 148 + structural 1075 + 111 = {148 + 1075 + 111}")
    out.append(f"budget records 845 + w07 (142+106+71+38+26+18+6+4) = {845 + 142 + 106 + 71 + 38 + 26 + 18 + 6 + 4}")
    out.append(f"acknowledged 20101 + w07 (5510+5515+5530+5545*3+5540*2) = {20101 + 5510 + 5515 + 5530 + 5545 * 3 + 5540 * 2}")
    out.append(f"807/973 = {100 * 807 / 973:.1f}%; 148 overshoot median 109.6 -> B {30 + 109.6:.1f}; max 524.8 -> B {30 + 524.8:.1f}")
    out.append(f"snow 34/601 = {100 * 34 / 601:.3f}%; 41/601 = {100 * 41 / 601:.3f}%; 886.858/3445.933 = "
               f"{100 * 886.858 / 3445.933:.2f}%; 2299.012/3445.933 = {100 * 2299.012 / 3445.933:.2f}%; "
               f"8.566/3445.933 = {100 * 8.566 / 3445.933:.2f}%")
    out.append(f"weekday forecast-late pooled 2/1471 = {100 * 2 / 1471:.3f}%; C-30 fc pooled 10/2338 = {100 * 10 / 2338:.3f}%")
    wp = {"FREE": (1629, 274, 164), "LOCKS": (1584, 47, 27), "C-120": (1563, 23, 0), "C-60": (1540, 0, 0), "C-30": (1534, 0, 0)}
    out.append("WP14r timely60/timely120 = served - late: " + ", ".join(
        f"{k} {s - l6}/{s - l12}" for k, (s, l6, l12) in wp.items()) +
        f"; C-30 -> C-120 served +{1563 - 1534} late60 +23 timely60 +{(1563 - 23) - 1534}")
    w07 = {"U": (665, 50, 9), "C-30": (660, 47, 2), "C-120": (666, 51, 7)}
    out.append("w07 C-30 -> C-120: served +%d late60 +%d late120 +%d timely60 +%d timely120 +%d" % (
        666 - 660, 51 - 47, 7 - 2, (666 - 51) - (660 - 47), (666 - 7) - (660 - 2)))
    out.append(f"T38 window gaps U-C: w08 {1014 - 975}, w17 {904 - 852}, w07 {516 - 511}")
    out.append(f"FREE gate split: 325/401 = {100 * 325 / 401:.1f}%; 33555.398/(14953.481+33555.398) = "
               f"{100 * 33555.398 / (14953.481 + 33555.398):.2f}%")
    out.append(f"cost-first: 445/1714 = {100 * 445 / 1714:.2f}%; 104/1715 = {100 * 104 / 1715:.2f}%; tie-like 445-433 = {445 - 433}, 104-95 = {104 - 95}")
    out.append(f"shared approx: 0.228*2434 = {0.228 * 2434:.0f}; 0.134*2338 = {0.134 * 2338:.0f} (rounded-percentage approximations)")
    out.append(f"per-100-requests exposure (late60/late120/late300/late600 naive): U {[round(100 * x / 3672, 2) for x in (203, 102, 18, 2)]}, "
               f"C-30 {[round(100 * x / 3672, 2) for x in (76, 11, 0, 0)]}, C-30+fc {[round(100 * x / 3672, 2) for x in (10, 0, 0, 0)]}")
    out.append(f"U late60 & exposed 134/174 = {100 * 134 / 174:.2f}%; 134/203 = {100 * 134 / 203:.1f}%; C-30 4/76; 72 = {76 - 4}")
    out.append(f"C-30 later-pushed riders (exposed 33 - earlier 4)/2338 = {100 * (33 - 4) / 2338:.2f}%")
    out.append(f"DiD baseline (203-76) = {203 - 76}; served gap 96; timely gap {2231 - 2262}")
    # factor anchor: f(0)/f(start) for the 34 test cells
    fa = {"2018-11-14": (0.862, 0.597, 0.473), "2018-11-15": (0.924, 0.652, 0.276), "2018-11-16": (1.142, 0.887, 0.773),
          "2018-11-17": (1.307, 1.228, 0.726), "2018-11-18": (1.550, 1.462, 0.766)}
    scope = json.loads(load_lines(XW / "R16-scope-inventory.txt")[13].split("All34 T38 keys: ", 1)[1])
    used = {}
    for key in scope:
        day = f"{key[1:5]}-{key[5:7]}-{key[7:9]}"
        w = {"w07": 0, "w08": 1, "w17": 2}[key[-3:]]
        used.setdefault(key[-3:], []).append((day, fa[day][w]))
    for w, vals in sorted(used.items()):
        uniq = sorted(set(vals))
        out.append(f"factor-anchor f(0)/f(start) over T3.8 test cells {w}: {uniq}")
    ml_a1 = load_lines(CW / "ml-pilot-report-a1-2026-10-08.txt")
    ml_0 = load_lines(CW / "ml-pilot-report-2026-10-08.txt")
    cal = lambda lines: [int(re.search(r"cal (\d+)", t).group(1)) for t in lines if t.startswith("== static")]
    out.append(f"ML pilot static calibration n: original {cal(ml_0)} vs A1 {cal(ml_a1)}; dropped {sum(cal(ml_0)) - sum(cal(ml_a1))}")
    out.append(f"ML FREE E30 test13 line 21: original | {collapse(ml_0[20])[:200]}")
    out.append(f"ML FREE E30 test13 line 21: A1       | {collapse(ml_a1[20])[:200]}")


def pdf_identity(out):
    try:
        import pypdf
    except ImportError:
        out.append("pypdf not available; PDF identity skipped")
        return
    base = pathlib.Path(r"E:/RideBoundData/literature-survey-2026-10-06/pdf")
    for name in ("alonso-mora-pnas2017.pdf", "cohen-fiszer-kim-2022-frustration.pdf"):
        path = base / name
        try:
            reader = pypdf.PdfReader(str(path))
            text = collapse(reader.pages[0].extract_text() or "")
            out.append(f"PDF {name}: pages {len(reader.pages)}; page-1 text[:700] | {text[:700]}")
        except Exception as error:  # report, never hide
            out.append(f"PDF {name}: ERROR {type(error).__name__}: {error}")


def main():
    out = ["# verify_register.py (evidence register, rewrite-2026-10); read-only; one process"]
    anchor_checks(out)
    parse_a(out)
    misc_arithmetic(out)
    pdf_identity(out)
    with OUT.open("x", encoding="utf-8") as handle:
        handle.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
