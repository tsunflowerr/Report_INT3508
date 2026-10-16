"""Hand cases M01-M14 (Codex backlog §15.1, feasible without runner changes) and the mutations the
oracle must catch (T3.2 acceptance). Run: python -B test_accounting.py (non-zero exit on failure)."""
from __future__ import annotations

from accounting import AccountingError, AuditRow, MAX_CANONICAL, accumulate, compare

failures: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        failures.append(name)
        print("FAIL", name)


def chain(publications, request="r1", coordinate="drop", es=None):
    """Committed chain: initial p0, then (e, p) pairs with v = previous p."""
    p0 = publications[0]
    rows = [AuditRow(request, coordinate, 0, p0, p0, p0, initial=True)]
    last = p0
    for i, p in enumerate(publications[1:], start=1):
        e = es[i - 1] if es else last
        rows.append(AuditRow(request, coordinate, i, last, e, p))
        last = p
    return rows


def totals(rows):
    return accumulate(rows)[("r1", "drop")]


def raises(fn) -> bool:
    try:
        fn()
    except AccountingError:
        return True
    return False


# M01: v600,e600,p660 -> x0 c60 z60; X0 C60 V60
t = totals([AuditRow("r1", "drop", 0, 600, 600, 600, initial=True), AuditRow("r1", "drop", 1, 600, 600, 660)])
check("M01", (t.X, t.C, t.V, t.steps[0][1:]) == (0, 60, 60, (0, 60, 60)))
# M02: v600,e660,p660 -> x60 c0 z60 (the kept route moved; conduct 0)
t = totals([AuditRow("r1", "drop", 0, 600, 600, 600, initial=True), AuditRow("r1", "drop", 1, 600, 660, 660)])
check("M02", (t.X, t.C, t.V, t.steps[0][1:]) == (60, 0, 60, (60, 0, 60)))
# M03: v600,e720,p600 -> x120 c-120 z0; C120 X120 V0 (repair to keep the promise is charged)
t = totals([AuditRow("r1", "drop", 0, 600, 600, 600, initial=True), AuditRow("r1", "drop", 1, 600, 720, 600)])
check("M03", (t.X, t.C, t.V, t.steps[0][1:]) == (120, 120, 0, (120, -120, 0)))
# M04: p0 600; 660 then 600 -> E0 V120 H120 (end-to-end blind to oscillation)
t = totals(chain([600, 660, 600]))
check("M04", (t.E, t.V, t.H, t.M, t.Mplus) == (0, 120, 120, 60, 60))
# M05: p0 600; 660 then 720 -> E120 V120 H0 (monotone: chain equals endpoints)
t = totals(chain([600, 660, 720]))
check("M05", (t.E, t.V, t.H) == (120, 120, 0))
# M06: p = v but e != v: the step stays on the audit grid and keeps the cancellation (x60, c-60)
t = totals([AuditRow("r1", "drop", 0, 600, 600, 600, initial=True), AuditRow("r1", "drop", 1, 600, 660, 600)])
check("M06", (t.count, t.X, t.C, t.V) == (2, 60, 60, 0))
# M07: rejected proposal before ACK does not enter the history
rows = chain([600, 660]) + [AuditRow("r1", "drop", 2, 660, 660, 900, committed=False)]
check("M07", totals(rows).V == 60)
# M08: a retried batch appearing twice as committed is rejected, never double counted
rows = chain([600, 660]) + [AuditRow("r1", "drop", 1, 600, 600, 660)]
check("M08 duplicate committed row rejected", raises(lambda: accumulate(rows)))
# M08b: a repeated sequence number that is otherwise chain-consistent is still rejected, so the
# duplicate check is tested on its own and not only through the continuity check
rows = chain([600, 660]) + [AuditRow("r1", "drop", 1, 660, 660, 660)]
check("M08b duplicate sequence rejected even when continuous", raises(lambda: accumulate(rows)))
# One-sided vs two-sided excursion: 600 -> 540 -> 610 has M+ = 10 but M = 60
t = totals(chain([600, 540, 610]))
check("M+ counts only lateness", (t.Mplus, t.M) == (10, 60))
# M11: pickup closed at boarding; later rows do not accumulate on that coordinate
rows = chain([600, 660], coordinate="pickup") + [AuditRow("r1", "pickup", 2, 660, 700, 700, closed=True)]
check("M11", accumulate(rows)[("r1", "pickup")].V == 60)
# M11b (found on real data, 2026-09-25): the closing publication snaps the pickup to the actual
# boarding time and later closed rows publish against it. The chain stays continuous through the
# closed rows, nothing after closing accumulates, and E uses the last open value.
rows = chain([600, 660], coordinate="pickup") + [
    AuditRow("r1", "pickup", 2, 660, 640, 640, closed=True),
    AuditRow("r1", "pickup", 3, 640, 640, 640, closed=True),
]
t = accumulate(rows)[("r1", "pickup")]
check("M11b chain continues through closed rows", (t.V, t.E) == (60, 60))
broken = rows + [AuditRow("r1", "pickup", 4, 600, 640, 640, closed=True)]
check("M11b a gap after closing is still a gap", raises(lambda: accumulate(broken)))
# M12 (partial): accumulated values are kept as recorded (no erasure). Cancellation itself, its
# censoring and its denominator need lifecycle rows that the audit format does not carry yet (T3.4).
rows = chain([600, 700, 650])
check("M12 partial: no erasure", totals(rows).V == 150)
# M13: recovery beyond a cap is recorded, totals never reset (C grows past beta)
rows = chain([600, 660, 760], es=[600, 660])
check("M13", totals(rows).C == 160)
# M14: extreme canonical values are exact; out-of-range and non-integer inputs fail typed
t = totals([AuditRow("r1", "drop", 0, 0, 0, 0, initial=True),
            AuditRow("r1", "drop", 1, 0, MAX_CANONICAL, MAX_CANONICAL)])
check("M14 exact at 2^53-1", t.X == MAX_CANONICAL and t.C == 0)
check("M14 negative rejected", raises(lambda: accumulate([AuditRow("r1", "drop", 0, -1, -1, -1, initial=True)])))
check("M14 float rejected", raises(lambda: accumulate([AuditRow("r1", "drop", 0, 1.0, 1.0, 1.0, initial=True)])))

# Invariants: V <= C + X, with equality exactly when x and c never have opposite signs
t = totals(chain([600, 700, 650], es=[650, 720]))
check("triangle", t.V <= t.C + t.X)
check("first row must be the initial promise",
      raises(lambda: accumulate([AuditRow("r1", "drop", 0, 600, 610, 620)])))
check("chain continuity v_t = p_{t-1}",
      raises(lambda: accumulate(chain([600, 660]) + [AuditRow("r1", "drop", 2, 600, 600, 700)])))

# --- Mutations of a production ledger that the oracle must catch (T3.2 acceptance) ---
truth = accumulate(chain([600, 660, 600, 720], es=[630, 700, 650]))
good = {k: {"C": v.C, "V": v.V} for k, v in truth.items()}
check("agreement on the true ledger", compare(good, truth) == [])


def ledger_from(rows):
    return {k: {"C": v.C, "V": v.V} for k, v in accumulate(rows).items()}


base = chain([600, 660, 600, 720], es=[630, 700, 650])
# sign mutation: production uses signed c (not |c|)
signed = {("r1", "drop"): {"C": sum(s[2] for s in truth[("r1", "drop")].steps), "V": good[("r1", "drop")]["V"]}}
check("mutation: sign", compare(signed, truth) != [])
# double counting: one step counted twice
double = {("r1", "drop"): {"C": good[("r1", "drop")]["C"] + abs(truth[("r1", "drop")].steps[0][2]),
                           "V": good[("r1", "drop")]["V"]}}
check("mutation: double counting", compare(double, truth) != [])
# missing publication: production ledger skipped one committed row
missing = ledger_from(base[:-1])
check("mutation: missing publication", compare(missing, truth) != [])
# budget reset: production restarted C at a phase change (only the last step counted)
reset = {("r1", "drop"): {"C": abs(truth[("r1", "drop")].steps[-1][2]), "V": good[("r1", "drop")]["V"]}}
check("mutation: budget reset", compare(reset, truth) != [])
# initial vs lifetime: production reports the endpoint E instead of the chain V
endpoint = {("r1", "drop"): {"C": good[("r1", "drop")]["C"], "V": truth[("r1", "drop")].E}}
check("mutation: initial/lifetime confusion", compare(endpoint, truth) != [])
# a rider missing from the production ledger is reported
check("mutation: rider dropped", compare({}, truth) != [])
# every diagnostic names the request and coordinate
check("diagnostics name the rider", all("'r1'" in d for d in compare(double, truth)))

print(f"{len(failures)} failure(s)")
raise SystemExit(1 if failures else 0)
