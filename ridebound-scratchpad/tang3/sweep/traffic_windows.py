"""Real traffic factors and demand per time window, read-only (2026-09-29).

Replaces the hand-typed PowerShell numbers of the 2026-09-29 session (handoff §5.6 item 5, §7 errata 7-8):
- weekday of every day 12-18/11/2018;
- per day and window (07-09, 08-10, 17-19): peak rise over the window start, end ratio, largest and smallest
  15-minute step, whether the factor is monotone over the window;
- largest 60-minute cumulative rise at any start time of the day (why_similar.py part A, same definition);
- demand: requests per sample file whose rq_time falls in 07-09, 08-10 and 08-09 (the overlap of the two).

A window [s, e] uses the bins with s <= t <= e (both ends inclusive, the same as why_similar.py part A). The
"excl" variants drop the bin at e, i.e. only the bins that start inside the demand window.

Usage: python -B traffic_windows.py <new-log-path>   (the log is opened with mode "x": never overwritten)
"""
import csv
import datetime
import pathlib
import sys

ROOT = pathlib.Path(r"E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan")
NET = ROOT / "networks" / "Manhattan_2019_corrected"
DEMAND = ROOT / "demand" / "Manhattan_2018" / "matched" / "Manhattan_2019_corrected"
DAYS = [f"2018-11-{d}" for d in range(12, 19)]
WINDOWS = {"07-09": (25200, 32400), "08-10": (28800, 36000), "17-19": (61200, 68400)}


def factors(day):
    rows = list(csv.DictReader(open(NET / f"{day}_tt_factors.csv", newline="")))
    t = [int(float(r["simulation_time"])) for r in rows]
    f = [float(r["travel_time_factor"]) for r in rows]
    assert all(b - a == 900 for a, b in zip(t, t[1:])), f"{day}: bins are not 900 s apart"
    return t, f


def window_stats(t, f, start, end, inclusive_end=True):
    idx = [i for i in range(len(t)) if start <= t[i] <= end and (inclusive_end or t[i] < end)]
    base = f[idx[0]]
    vals = [f[i] for i in idx]
    steps = [(b / a - 1) for a, b in zip(vals, vals[1:])]
    peak_i = max(range(len(vals)), key=lambda k: vals[k])
    return {
        "bins": len(vals),
        "start": base,
        "peakRise": vals[peak_i] / base - 1,
        "peakAt": t[idx[peak_i]],
        "endRatio": vals[-1] / base - 1,
        "maxStep": max(steps),
        "minStep": min(steps),
        "monotoneUp": all(s >= 0 for s in steps),
    }


def hhmm(sec):
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}"


def demand_counts(day, sample):
    path = DEMAND / f"{day}_sample_10_{sample}.csv"
    if not path.exists():
        return None
    times = [int(float(r["rq_time"])) for r in csv.DictReader(open(path, newline=""))]
    return {
        "07-09": sum(1 for x in times if 25200 <= x < 32400),
        "08-10": sum(1 for x in times if 28800 <= x < 36000),
        "08-09": sum(1 for x in times if 28800 <= x < 32400),
        "all": len(times),
    }


def main(log_path):
    lines = []
    out = lines.append
    out(f"# traffic_windows.py, run {datetime.datetime.now().isoformat(timespec='seconds')}")
    out(f"# factors: {NET}")
    out(f"# demand:  {DEMAND}")
    out("")
    out("== weekday")
    for day in DAYS:
        out(f"{day} {datetime.date.fromisoformat(day).strftime('%A')}")
    out("")
    out("== factor per window (bins s <= t <= e unless marked excl)")
    out("day        window  bins start   peakRise (at)     endRatio  maxStep  minStep  monotoneUp | excl: endRatio maxStep minStep monotoneUp")
    for day in DAYS:
        t, f = factors(day)
        for name, (s, e) in WINDOWS.items():
            a = window_stats(t, f, s, e, True)
            b = window_stats(t, f, s, e, False)
            out(f"{day} {name}   {a['bins']:>3} {a['start']:.4f} {a['peakRise']:+8.1%} ({hhmm(a['peakAt'])}) "
                f"{a['endRatio']:+8.1%} {a['maxStep']:+8.1%} {a['minStep']:+8.1%} {str(a['monotoneUp']):>6} | "
                f"{b['endRatio']:+8.1%} {b['maxStep']:+8.1%} {b['minStep']:+8.1%} {str(b['monotoneUp']):>6}")
    out("")
    out("== largest cumulative rise over 60 minutes (4 bins), any start time of the day")
    for day in DAYS:
        t, f = factors(day)
        best = max(((f[i + 4] / f[i] - 1), t[i]) for i in range(len(f) - 4))
        out(f"{day} {best[0]:+.1%} starting {hhmm(best[1])}")
    out("")
    out("== largest single 15-minute step over the whole day")
    for day in DAYS:
        t, f = factors(day)
        best = max(((f[i + 1] / f[i] - 1), t[i]) for i in range(len(f) - 1))
        out(f"{day} {best[0]:+.1%} from {hhmm(best[1])}")
    out("")
    out("== demand: requests per sample_10_r file with rq_time in [07:00,09:00) / [08:00,10:00) / [08:00,09:00) / all")
    for day in DAYS:
        for sample in (1, 2, 3, 4):
            c = demand_counts(day, sample)
            if c is None:
                out(f"{day} sample_10_{sample}: missing")
            else:
                out(f"{day} sample_10_{sample}: {c['07-09']:>5} / {c['08-10']:>5} / {c['08-09']:>5} / {c['all']:>6}")
    text = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8") as fh:
        fh.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: traffic_windows.py <new-log-path>")
    main(sys.argv[1])
