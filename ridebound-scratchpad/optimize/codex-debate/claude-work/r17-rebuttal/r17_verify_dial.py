"""R17 rebuttal (Claude side): independent re-count of Codex R16's cap-dial and T3.8 relaxed-endpoint numbers.

Read-only on existing transcripts; no simulation, build or model fitting; outputs created with mode "x".
Own reader (not Codex's R16-cap-outcomes-v2.py, not Claude-R16's q2_cap_dial.py / forecast_family_a): paths are
built from the run folders, the frame type is read from a decoded base64 prefix, every file's SHA-256 is computed
while streaming and compared with Codex's R13-raw-verification.json list (independent file list, same files).
Per served rider (passengerAlighted with a ledger initialPromise):
  late_k = A - p0 > k s (p0 = initialPromise publishedPromise drop ETA), early60 = A - p0 < -60 s,
  timely_k (per request) = served - late_k,
  dispatch change of a later drop entry c = published drop - exogenous drop; exposed = any c != 0;
  repeated = >= 2 entries with c != 0; S = sum |c|.
Forecast quote D0 = display_layer.display(t0, p0, profile(day, window, rule)) with t0 = publishedAtMs of the
initialPromise; rules causal-no15 (primary) and loo-no15 (non-causal sensitivity; w07 only). Inactive -> D0 = p0.
Populations: w07 (8 cells, 12-13 Nov, 07-09 h) arms U, C-30..C-300; T3.8 test (34 cells) arms U, C-30.
Usage: python -B r17_verify_dial.py <out-prefix>   (1 worker process)."""
import base64
import collections
import hashlib
import json
import pathlib
import re
import sys

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import display_layer as dl  # noqa: E402

CODEX_LIST = OPT / "codex-debate" / "codex-work" / "R13-raw-verification.json"
SPLIT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/split-t38-v1.json")
W07 = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
W07X = pathlib.Path(r"C:/RideBoundData/research/tier3-w07x-v1")
T38 = pathlib.Path(r"C:/RideBoundData/research/tier3-t38-v1")
W07_ROOT = {"U": W07, "C-30": W07, "C-60": W07, "C-90": W07X, "C-120": W07, "C-150": W07X, "C-180": W07X,
            "C-240": W07X, "C-300": W07}
TYPE = re.compile(rb'"messageType":"([A-Za-z]+)"')


def frame_type(b64: str) -> bytes:
    head = base64.b64decode(b64[:400])
    m = TYPE.search(head)
    if m:
        return m.group(1)
    m = TYPE.search(base64.b64decode(b64))
    return m.group(1) if m else b"?"


def scan(path: pathlib.Path):
    digest = hashlib.sha256()
    alighted = {}
    last_ckpt = None
    with path.open("rb") as fh:
        for line in fh:
            digest.update(line)
            if not line.strip():
                continue
            rec = json.loads(line)
            t = frame_type(rec["frameBase64"])
            if t == b"eventBatch":
                env = json.loads(base64.b64decode(rec["frameBase64"]))
                for ev in env["payload"].get("events", []):
                    if ev.get("eventType") == "passengerAlighted":
                        rid = ev["payload"]["requestId"]
                        alighted.setdefault(rid, env["simTimeMs"])
            elif t == b"checkpoint" and rec["direction"] == "runnerToAdapter":
                last_ckpt = rec["frameBase64"]
    state = json.loads(base64.b64decode(last_ckpt))["payload"]["content"]["onlineState"]
    return digest.hexdigest(), alighted, state


def metrics(path, day, window, rules):
    sha, alighted, state = scan(path)
    reqs = state["requests"]
    life = collections.Counter(r["lifecycle"] for r in reqs)
    profs = {rule: dl.profile(day, window, rule) for rule in rules}
    m = collections.Counter(requests=len(reqs), completed_lifecycle=life.get("completed", 0))
    smax = 0
    for led in state["commitmentLedger"]:
        rid = led["requestId"]
        es = led["entries"]
        if not es or es[0]["kind"] != "initialPromise" or rid not in alighted:
            continue
        p0 = es[0]["publishedPromise"]["projection"]["dropEtaMs"]
        t0 = es[0]["publishedPromise"]["publishedAtMs"]
        a = alighted[rid]
        cs = [e["publishedPromise"]["projection"]["dropEtaMs"] - e["exogenousProjection"]["dropEtaMs"] for e in es[1:]]
        s = sum(abs(c) for c in cs)
        smax = max(smax, s)
        m["served"] += 1
        m["late60"] += a - p0 > 60_000
        m["late120"] += a - p0 > 120_000
        m["early60"] += a - p0 < -60_000
        m["exposed"] += s > 0
        m["repeated"] += sum(c != 0 for c in cs) >= 2
        m["S_sum_ms"] += s
        for rule, prof in profs.items():
            d0 = float(p0) if prof is None else dl.display(t0, p0, prof)
            m[f"{rule}:late60"] += a - d0 > 60_000
            m[f"{rule}:late120"] += a - d0 > 120_000
            m[f"{rule}:early60"] += a - d0 < -60_000
            m[f"{rule}:ext_ms"] += d0 - p0
            m[f"{rule}:active"] = int(prof is not None)
    m["alighted_without_promise"] = sum(1 for r in alighted if r not in {x["requestId"] for x in state["commitmentLedger"]})
    return sha, dict(m), smax


def jobs():
    split = json.loads(SPLIT.read_text(encoding="utf-8"))
    out = []
    for arm, root in W07_ROOT.items():
        for d in ("12", "13"):
            for r in (1, 2, 3, 4):
                cell = f"d201811{d}-s10-r{r}-w07"
                out.append(("w07", arm, cell, root / f"{arm}-{cell}" / "transcript-00.ndjson", f"2018-11-{d}", "w07",
                            ("causal-no15", "loo-no15")))
    for arm in ("U", "C-30"):
        for cell in split["test"]:
            name = f"{arm}-{cell}"
            folder = T38 / name
            if not (folder / "summary.json").exists() and (T38 / f"{name}-rerun1").exists():
                folder = T38 / f"{name}-rerun1"
            out.append(("t38", arm, cell, folder / "transcript-00.ndjson", f"2018-11-{cell[7:9]}", cell[-3:],
                        ("causal-no15",)))
    return out


def main():
    prefix = sys.argv[1]
    codex = json.loads(CODEX_LIST.read_text(encoding="utf-8"))
    ref = {(r["population"], r["arm"], r["cell"]): r for r in codex["runs"]}
    js = jobs()
    assert len(js) == 72 + 68, len(js)
    rows = []
    for i, (pop, arm, cell, path, day, window, rules) in enumerate(js, 1):
        sha, m, smax = metrics(path, day, window, rules)
        r = ref[(pop, arm, cell)]
        rows.append(dict(pop=pop, arm=arm, cell=cell, path=str(path), sha256=sha, sha_matches_codex_list=sha == r["sha256"],
                         path_matches_codex_list=pathlib.Path(r["transcript"]) == path,
                         completed_matches_codex_list=m["served"] == r["completed"], S_max_ms=smax, m=m))
        if i % 10 == 0:
            print(f"{i}/{len(js)} transcripts read", flush=True)
    groups = collections.OrderedDict()
    for row in rows:
        g = groups.setdefault((row["pop"], row["arm"]), dict(cells=0, S_max_ms=0, m=collections.Counter(),
                                                            sha_ok=0, path_ok=0, completed_ok=0))
        g["cells"] += 1
        g["S_max_ms"] = max(g["S_max_ms"], row["S_max_ms"])
        g["m"].update(row["m"])
        g["sha_ok"] += row["sha_matches_codex_list"]
        g["path_ok"] += row["path_matches_codex_list"]
        g["completed_ok"] += row["completed_matches_codex_list"]
    lines = ["# r17_verify_dial.py: independent re-count (Claude R17 rebuttal); read-only; lateness vs FIRST drop promise",
             "# cols: cells req served late60 late120 early60 timely60 timely120 exposed repeated meanS_exposed_s maxS_s | "
             "forecast rule: late60 late120 timely60 timely120 early60 mean_ext_s active_cells | sha/path/completed vs Codex list"]
    for (pop, arm), g in groups.items():
        m = g["m"]
        n = m["served"]
        mean_s = m["S_sum_ms"] / m["exposed"] / 1000 if m["exposed"] else 0.0
        s = (f"{pop:4s} {arm:6s} cells {g['cells']:2d} req {m['requests']:5d} served {n:5d} late60 {m['late60']:4d} "
             f"late120 {m['late120']:4d} early60 {m['early60']:3d} timely60 {n - m['late60']:5d} timely120 {n - m['late120']:5d} "
             f"exposed {m['exposed']:4d} repeated {m['repeated']:3d} meanS_exp {mean_s:6.1f} maxS {g['S_max_ms'] / 1000:6.1f}")
        for rule in ("causal-no15", "loo-no15"):
            if f"{rule}:ext_ms" in m or f"{rule}:active" in m:
                s += (f" | {rule}: late60 {m[f'{rule}:late60']:4d} late120 {m[f'{rule}:late120']:4d} "
                      f"timely60 {n - m[f'{rule}:late60']:5d} timely120 {n - m[f'{rule}:late120']:5d} "
                      f"early60 {m[f'{rule}:early60']:3d} ext {m[f'{rule}:ext_ms'] / n / 1000:5.1f}s active {m[f'{rule}:active']:2d}")
        s += f" | sha_ok {g['sha_ok']}/{g['cells']} path_ok {g['path_ok']}/{g['cells']} completed_ok {g['completed_ok']}/{g['cells']}"
        lines.append(s)
    text = "\n".join(lines) + "\n"
    with open(prefix + ".txt", "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(prefix + ".json", "x", encoding="utf-8", newline="\n") as fh:
        json.dump(dict(rows=rows), fh, indent=1)
    print(text, flush=True)


if __name__ == "__main__":
    main()
