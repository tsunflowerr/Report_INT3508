"""Independent Round-5 replay; never imports or executes Claude's scripts.

Read repository transcript/profile readers only. Cache and report are created
exclusively with mode 'x' in this directory. Run with Python -B.
"""
from __future__ import annotations

import argparse
import collections
import json
import math
from pathlib import Path
import statistics
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OPT = Path("E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
import display_layer as dl


def local_path(name):
    path = (HERE / name).resolve()
    if path.parent != HERE:
        raise ValueError("All outputs must be directly inside codex-work")
    return path


def signature(path):
    stat = path.stat()
    return [stat.st_size, stat.st_mtime_ns]


def extract(arm, cell):
    path = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
    last_state = None
    arrivals = {}
    for direction, envelope in fa.audit_vep.read_frames(path):
        if direction == "runnerToAdapter" and envelope.get("messageType") == "checkpoint":
            last_state = envelope["payload"]["content"]["onlineState"]
        if direction == "adapterToRunner" and envelope.get("messageType") == "eventBatch":
            for event in envelope["payload"].get("events", []):
                if event.get("eventType") == "passengerAlighted":
                    arrivals.setdefault(event["payload"]["requestId"], envelope["simTimeMs"])
    if last_state is None:
        raise ValueError(f"Missing checkpoint: {path}")
    requests = {r["requestId"]: r for r in last_state["requests"]}
    profile = dl.profile(fa.day_of(cell), cell[-3:], "causal-no15")
    records = []
    for history in last_state["commitmentLedger"]:
        rid = history["requestId"]
        if rid not in arrivals:
            continue
        entries = history["entries"]
        first = entries[0]
        if first["kind"] != "initialPromise":
            raise ValueError(f"Not initial: {cell}/{rid}")
        published = first["publishedPromise"]
        proj = published["projection"]
        t0, p0, pick0 = published["publishedAtMs"], proj["dropEtaMs"], proj["pickupEtaMs"]
        req = requests[rid]
        revisions = []
        pickup_c, pickup_x = False, False
        for entry in entries[1:]:
            prev = entry["previousPromise"]["projection"]
            ref = entry["exogenousProjection"]
            pub = entry["publishedPromise"]
            chosen = pub["projection"]
            v, e, p = prev["dropEtaMs"], ref["dropEtaMs"], chosen["dropEtaMs"]
            revisions.append([v, e, p])
            actual_pick = req.get("actualPickupTimeMs")
            if actual_pick is None or pub["publishedAtMs"] < actual_pick:
                pickup_c |= chosen["pickupEtaMs"] != ref["pickupEtaMs"]
                pickup_x |= ref["pickupEtaMs"] != prev["pickupEtaMs"]
        records.append({
            "arm": arm, "cell": cell, "day": fa.day_of(cell), "window": cell[-3:],
            "rider": rid, "t0": t0, "p0": p0, "pick0": pick0,
            "fc": dl.display(t0, p0, profile), "a": arrivals[rid],
            "room": pick0 + req["maxRideTimeMs"] - p0,
            "max_ride": req["maxRideTimeMs"], "revisions": revisions,
            "exposed": any(p != e for v, e, p in revisions),
            "pickup_c": pickup_c, "pickup_x": pickup_x,
        })
    return records, {
        "arm": arm, "cell": cell, "requests": len(requests),
        "path": str(path), "signature": signature(path),
        "request_fields": sorted(next(iter(requests.values())).keys()),
    }


def statistics_for(records, promise, tau=60000):
    shown = [promise(r) for r in records]
    residuals = [r["a"] - d for r, d in zip(records, shown)]
    extension = sorted(d - r["p0"] for r, d in zip(records, shown))
    n = len(records)
    late = sum(x > tau for x in residuals)
    early = sum(x < -60000 for x in residuals)
    return {
        "n": n, "late": late, "y": 100 * late / n,
        "ext": statistics.fmean(extension) / 1000,
        "p90": extension[(90 * n) // 100] / 1000,
        "early": 100 * early / n, "timely": n - late,
        "symmetric60": sum(abs(x) <= 60000 for x in residuals),
        "mean_horizon": statistics.fmean(d - r["t0"] for r, d in zip(records, shown)) / 1000,
    }


def metric_line(name, records, promise, tau=60000):
    m = statistics_for(records, promise, tau)
    return (f"{name}: riders={m['n']} late={m['late']} Y{tau//1000}={m['y']:.6f}% "
            f"extension_mean_s={m['ext']:.6f} extension_p90_s={m['p90']:.6f} "
            f"early60={m['early']:.6f}% timely={m['timely']} "
            f"symmetric60={m['symmetric60']} quote_horizon_mean_s={m['mean_horizon']:.6f}")


def room_pad(record, b, a):
    return record["fc"] + min(b, a * max(0, record["room"]))


def cost_matched_candidates(records, budget_s):
    """Match mean cost using promises only; selecting the winner is in-sample."""
    base_cost = statistics.fmean(r["fc"] - r["p0"] for r in records)
    target = budget_s * 1000
    if target < base_cost:
        return [("naive+uniform", lambda r, target=target: r["p0"] + target)]
    extra = target - base_cost
    candidates = [("fc+uniform", lambda r, extra=extra: r["fc"] + extra)]
    horizon = statistics.fmean(r["fc"] - r["t0"] for r in records)
    alpha = extra / horizon if horizon > 0 else 0
    candidates.append(("fc+proportional", lambda r, alpha=alpha:
                       r["fc"] + alpha * (r["fc"] - r["t0"])))
    for a in (0.25, 0.5, 1.0):
        cap = [a * max(0, r["room"]) for r in records]
        low, high = 0.0, max(cap, default=0.0)
        for _ in range(60):
            b = (low + high) / 2
            if statistics.fmean(min(b, c) for c in cap) < extra:
                low = b
            else:
                high = b
        b = high
        candidates.append((f"fc+room_a={a:g},b_s={b/1000:.6f}",
                           lambda r, b=b, a=a: room_pad(r, b, a)))
    return candidates


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="round5-reproduction-2026-10-07.txt")
    parser.add_argument("--cache", default="round5-rider-records-2026-10-07.json")
    args = parser.parse_args()
    report, cache = local_path(args.report), local_path(args.cache)
    if report.exists():
        raise FileExistsError(report)
    if cache.exists():
        data = json.loads(cache.read_text(encoding="utf-8"))
        for source in data["sources"]:
            if source["signature"] != signature(Path(source["path"])):
                raise ValueError("Stale source cache")
    else:
        data = {"records": [], "sources": []}
        cells = fa.run_t38.PHASES["test"][1]
        for arm in ("U", "C-30"):
            for index, cell in enumerate(cells, 1):
                rows, source = extract(arm, cell)
                data["records"].extend(rows)
                data["sources"].append(source)
                if index % 4 == 0 or index == len(cells):
                    print(f"Read {arm}: {index}/{len(cells)} transcripts", flush=True)
        with cache.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, separators=(",", ":"))
    groups = {arm: [r for r in data["records"] if r["arm"] == arm] for arm in ("U", "C-30")}
    totals = {arm: sum(s["requests"] for s in data["sources"] if s["arm"] == arm) for arm in groups}
    lines = ["# Independent round5_reproduce.py; source readers only; no Claude script imports.",
             "# Raw frame hashes checked by audit_vep.read_frames; final checkpoint and first alight event extracted independently.",
             f"Sources={len(data['sources'])}; request totals={totals}; served={ {a:len(rs) for a,rs in groups.items()} }",
             "# Percentages below pool served riders; timely is an integer count, not rounded rate arithmetic.",
             "", "REQUIRED U ROOM BUCKETS"]
    u = groups["U"]
    for low, high in ((0, 60000), (60000, 120000), (120000, 240000), (240000, math.inf)):
        rows = [r for r in u if low <= r["room"] < high]
        exposed = sum(r["exposed"] for r in rows)
        late = sum(r["a"] - r["p0"] > 60000 for r in rows)
        lines.append(f"room=[{low/1000:g},{high/1000:g})s riders={len(rows)} "
                     f"exposed={exposed} share={100*exposed/len(rows):.6f}% "
                     f"naive_late60={late} Y60={100*late/len(rows):.6f}%")
    lines += ["", "REQUIRED POLICY REPRODUCTION",
              metric_line("U fc+uniform120", u, lambda r: r["fc"] + 120000),
              metric_line("U fc+min180,0.50room", u, lambda r: room_pad(r, 180000, 0.5)),
              metric_line("C-30 fc", groups["C-30"], lambda r: r["fc"])]
    room_extra = statistics.fmean(min(180000, 0.5*max(0, r["room"])) for r in u)
    lines += ["", "ADDITIONAL MATCHED-COST / METRIC DIAGNOSTICS",
              metric_line("U fc+uniform matched to room180a0.5 mean", u, lambda r: r["fc"] + room_extra),
              metric_line("U fc+prop0.05", u, lambda r: r["fc"] + .05*(r["fc"]-r["t0"])),
              metric_line("U fc+min120,0.25room", u, lambda r: room_pad(r, 120000, .25)),
              metric_line("C-30 fc+uniform30", groups["C-30"], lambda r: r["fc"] + 30000)]
    for arm, records in groups.items():
        lines.append(f"{arm}: negative_room={sum(r['room']<0 for r in records)} "
                     f"pickup_dispatch_exposed_before_board={sum(r['pickup_c'] for r in records)} "
                     f"pickup_exogenous_exposed_before_board={sum(r['pickup_x'] for r in records)}")
    for tau in (30000, 60000, 120000):
        lines.append(metric_line(f"U room180a0.5 tolerance={tau//1000}", u,
                                 lambda r: room_pad(r, 180000, .5), tau))
        lines.append(metric_line(f"C-30 fc tolerance={tau//1000}", groups["C-30"], lambda r: r["fc"], tau))
    lines += ["", "ROOM / HORIZON CONFOUNDING DIAGNOSTIC (DESCRIPTIVE)"]
    for low, high in ((0, 60000), (60000, 120000), (120000, 240000), (240000, math.inf)):
        rows = [r for r in u if low <= r["room"] < high]
        lines.append(f"room=[{low/1000:g},{high/1000:g})s "
                     f"mean_initial_drop_horizon_s={statistics.fmean(r['p0']-r['t0'] for r in rows)/1000:.6f} "
                     f"mean_max_ride_s={statistics.fmean(r['max_ride'] for r in rows)/1000:.6f}")
    lines += ["", "EXPLORATORY IN-SAMPLE COST-MATCHED ENVELOPE (NOT HELD-OUT)"]
    for budget in (0, 15, 30, 40, 50, 60):
        for arm, records in groups.items():
            scored = [(statistics_for(records, f), name, f)
                      for name, f in cost_matched_candidates(records, budget)]
            m, name, f = min(scored, key=lambda t: (-t[0]["timely"], t[0]["early"], t[0]["ext"]))
            lines.append(f"E<={budget}s {arm} best={name}: timely={m['timely']} "
                         f"extension_mean_s={m['ext']:.6f} early60={m['early']:.6f}%")
    lines += ["", "HYBRID SCREEN REPRODUCTION AND REVISION-LEVEL DIAGNOSTIC"]
    for arm, records in groups.items():
        for slack in (30, 60, 120, 180, 240):
            hit = [r for r in records if max([0]+[p-r["p0"] for v,e,p in r["revisions"]]) > slack*1000]
            traffic_only = sum(not r["exposed"] for r in hit)
            categories = collections.Counter()
            for r in records:
                h = r["p0"] + slack*1000
                for v, e, p in r["revisions"]:
                    if e <= h < p:
                        categories["chosen_new_violation"] += 1
                    elif p <= h < e:
                        categories["chosen_rescue"] += 1
                    elif e > h and p > h:
                        categories["both_fail"] += 1
            lines.append(f"{arm} S={slack}s: riders_hit={len(hit)} traffic_only={traffic_only} "
                         f"ever_dispatch={len(hit)-traffic_only} revisions={dict(sorted(categories.items()))}")
    lines += ["", "DAY COUNTS AND REPRESENTATIVE SOURCE RESOLUTION"]
    for arm, records in groups.items():
        days = collections.Counter(r["day"] for r in records)
        lines.append(f"{arm} served by day: {dict(sorted(days.items()))}")
    for source in data["sources"]:
        lines.append(f"SOURCE {source['arm']} {source['cell']} requests={source['requests']} {source['path']}")
    lines.append("Analysis only: no dispatcher execution, no source-file mutation, all created outputs use mode x.")
    with report.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")
    print(f"Wrote {report.name} and independently extracted cache {cache.name}", flush=True)


if __name__ == "__main__":
    main()
