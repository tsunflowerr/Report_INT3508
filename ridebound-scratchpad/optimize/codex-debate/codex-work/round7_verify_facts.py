"""Independent Round-7 source verification; no Claude-script imports.

Stream hash-checked transcripts; preserve all source files. Report and per-run
summary JSON are exclusively created with mode x inside codex-work. Python -B.
"""
from __future__ import annotations
import base64
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import statistics
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SCRATCH = HERE.parents[2]
CONFIGS = SCRATCH / "tang3/configs"
ROOTS = {
    "A": Path("E:/RideBoundData/wp9/confirmatory-h6-panela-v2"),
    "B": Path("E:/RideBoundData/wp9/confirmatory-h6-panelb-v2"),
}


def envelopes(path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            rec = json.loads(line)
            frame = base64.b64decode(rec["frameBase64"])
            if hashlib.sha256(frame).hexdigest() != rec["frameSha256"]:
                raise ValueError(f"Frame hash mismatch: {path}")
            yield rec["direction"], json.loads(frame)


def read_episode(path, budget=False):
    final, alights, minima = None, {}, {}
    for direction, env in envelopes(path):
        kind = env.get("messageType")
        if direction == "runnerToAdapter" and kind == "checkpoint":
            final = env["payload"]["content"]["onlineState"]
        elif direction == "adapterToRunner" and kind == "eventBatch":
            for event in env["payload"].get("events", []):
                if event["eventType"] == "passengerAlighted":
                    alights.setdefault(event["payload"]["requestId"], env["simTimeMs"])
        if budget and kind == "decision":
            evidence = (env.get("payload", {}).get("solver") or {}).get("executionEvidence") or {}
            for candidate in evidence.get("prunedCandidates", []):
                if candidate["code"] != "COMMITMENT_BUDGET_EXCEEDED":
                    continue
                witnesses = [w for w in candidate.get("commitmentWitnesses", [])
                             if w["code"] == "COMMITMENT_BUDGET_EXCEEDED"]
                if not witnesses:
                    continue
                excess = max(w["after"] - w["limit"] for w in witnesses)
                spent = any(w["before"] > 0 for w in witnesses)
                for rid in candidate.get("newRequestIds", []):
                    if rid not in minima or excess < minima[rid][0]:
                        minima[rid] = (excess, spent)
    if final is None:
        raise ValueError(f"No checkpoint: {path}")
    return final, alights, minima


def wp9_metrics(panel, run):
    path = run / "transcript-00.ndjson"
    state, alights, _ = read_episode(path)
    onboard = defaultdict(list)
    for r in state["requests"]:
        if r["requestId"] in alights:
            onboard[r["assignedVehicleId"]].append(
                (r["actualPickupTimeMs"], alights[r["requestId"]], r["requestId"]))
    served, shared, overlap_pairs = 0, 0, 0
    for legs in onboard.values():
        for start, end, rid in legs:
            others = sum(other != rid and other_start < end and start < other_end
                         for other_start, other_end, other in legs)
            served += 1
            shared += others > 0
            overlap_pairs += others
    exposed = set()
    for history in state["commitmentLedger"]:
        if history["requestId"] not in alights:
            continue
        if any(e["publishedPromise"]["projection"]["dropEtaMs"] != e["exogenousProjection"]["dropEtaMs"]
               for e in history["entries"][1:]):
            exposed.add(history["requestId"])
    # Full publication-action consistency was already audited by the saved WP9
    # tooling; here the signed component is extracted independently from ledger.
    return {"panel": panel, "run": run.name, "path": str(path),
            "arm": "b1" if "-b1-" in run.name else "c1",
            "primary": run.name.startswith("p-" if panel == "A" else "pb-"),
            "requests": len(state["requests"]), "served": served, "shared": shared,
            "exposed": len(exposed), "co_rider_sum": overlap_pairs}


def aggregate(rows):
    return {key: sum(r[key] for r in rows) for key in
            ("requests", "served", "shared", "exposed", "co_rider_sum")}


def format_aggregate(label, rows):
    t = aggregate(rows)
    return (f"{label}: runs={len(rows)} requests={t['requests']} served={t['served']} "
            f"served_pct={100*t['served']/t['requests']:.6f} shared={t['shared']} "
            f"shared_pct={100*t['shared']/t['served']:.6f} exposed={t['exposed']} "
            f"exposed_pct={100*t['exposed']/t['served']:.6f} co_riders_mean={t['co_rider_sum']/t['served']:.6f}")


def main():
    report = HERE / "round7-facts-verification-2026-10-07.txt"
    summary = HERE / "round7-wp9-run-records-2026-10-07.json"
    if report.exists() or summary.exists():
        raise FileExistsError("Round-7 outputs must be new")
    lines = ["# Independent Round-7 verification: own streaming parser, frame hashes checked, no Claude-script imports."]
    u_path, c_path = CONFIGS / "U.json", CONFIGS / "C-30.json"
    old_u = Path("C:/Code/RideBound-noworse/benchmarks/configurations/wp14-c1-nobudget-v1.json")
    u, c = json.loads(u_path.read_text()), json.loads(c_path.read_text())
    delta = []
    def diff(a, b, key=""):
        if isinstance(a, dict) and isinstance(b, dict):
            for k in sorted(a.keys() | b.keys()):
                if k not in a or k not in b: delta.append([key+"/"+k, a.get(k), b.get(k)])
                else: diff(a[k], b[k], key+"/"+k)
        elif isinstance(a, list) and isinstance(b, list):
            assert len(a) == len(b)
            for i, (av, bv) in enumerate(zip(a, b)): diff(av, bv, key+f"/{i}")
        elif a != b: delta.append([key, a, b])
    diff(u, c)
    lines += [f"F1 U/C30 config differences={delta}",
              f"F1 U SHA256={hashlib.sha256(u_path.read_bytes()).hexdigest()}; WP14-nobudget-byte-identical={u_path.read_bytes()==old_u.read_bytes()}",
              f"F1 locks={u['policies'][0]['finalConfirmationLocks']}; material_rule={u['policies'][0]['materialRevisionRule']}",
              "F5 config bucket width proves materiality setting, not display formatting; production-code check required.", "", "F2 MIXED INVENTORY (CLAUDE'S GLOB) AND PRIMARY-ONLY CORRECTION"]
    records = []
    for panel, root in ROOTS.items():
        runs = sorted(r for r in root.iterdir() if r.is_dir() and ("-b1-" in r.name or "-c1-" in r.name)
                      and (r / "transcript-00.ndjson").exists())
        for index, run in enumerate(runs, 1):
            records.append(wp9_metrics(panel, run))
            if index % 5 == 0 or index == len(runs):
                print(f"WP9 panel{panel} parsed {index}/{len(runs)}", flush=True)
        for arm in ("b1", "c1"):
            rows = [r for r in records if r["panel"] == panel and r["arm"] == arm]
            lines.append(format_aggregate(f"panel{panel} {arm} ALL", rows))
            primary = [r for r in rows if r["primary"]]
            lines.append(format_aggregate(f"panel{panel} {arm} PRIMARY", primary))
            extra = [r["run"] for r in rows if not r["primary"]]
            lines.append(f"panel{panel} {arm} extra_runs={extra}")
    with summary.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(records, handle, separators=(",", ":"))
    cache = json.loads((HERE / "round5-rider-records-2026-10-07.json").read_text(encoding="utf-8"))
    lines += ["", "F4 T38 DISPATCH-CHANGE DISTRIBUTION"]
    for arm in ("U", "C-30"):
        riders = [r for r in cache["records"] if r["arm"] == arm]
        values = sorted(abs(p-e)/1000 for r in riders for v,e,p in r["revisions"] if p != e)
        lines.append(f"{arm}: nonzero_revisions={len(values)} median_s={statistics.median(values):.6f} "
                     f"p90_s={values[(9*len(values))//10]:.6f} max_s={values[-1]:.6f}")
    lines += ["", "F4 C30 FINAL-REJECTED REQUESTS AND OBSERVED BUDGET-PRUNED CANDIDATES"]
    cross, excesses, spent_count = Counter(), [], 0
    for index, source in enumerate([s for s in cache["sources"] if s["arm"] == "C-30"], 1):
        stat = Path(source["path"]).stat()
        assert [stat.st_size, stat.st_mtime_ns] == source["signature"]
        state, _, candidates = read_episode(Path(source["path"]), budget=True)
        u_served = {r["rider"] for r in cache["records"] if r["arm"] == "U" and r["cell"] == source["cell"]}
        for request in state["requests"]:
            if request["lifecycle"] != "rejected": continue
            rid = request["requestId"]
            blocked = rid in candidates
            cross[("has_budget_prune" if blocked else "no_recorded_budget_prune", "U_completed" if rid in u_served else "U_not_completed")] += 1
            if blocked:
                excess, spent = candidates[rid]
                excesses.append(excess/1000)
                spent_count += spent
        if index % 5 == 0 or index == 34: print(f"T38 C30 diagnostic parsed {index}/34", flush=True)
    for category, count in sorted(cross.items()): lines.append(f"{category}: {count}")
    excesses.sort()
    lines.append(f"request_minimum_overshoot: n={len(excesses)} median_s={statistics.median(excesses):.6f} "
                 f"p25_s={excesses[len(excesses)//4]:.6f} p75_s={excesses[3*len(excesses)//4]:.6f} max_s={excesses[-1]:.6f}")
    for threshold in (30, 90, 270):
        lines.append(f"observed_overshoot_le_{threshold}s: {sum(x<=threshold for x in excesses)}/{len(excesses)} (budget-only feasibility, not rerun completions)")
    lines.append(f"selected_minimum_candidate_has_prior_spent_budget: {spent_count}/{len(excesses)}")
    lines += ["", "All episode counts are pooled, not per-cell means. Primary WP9 counts are separate from robustness.",
              "No simulation jobs executed; originals unchanged; all created numerical outputs use mode x."]
    with report.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines)+"\n")
    print(f"Wrote {report.name} and {summary.name}", flush=True)


if __name__ == "__main__":
    main()
