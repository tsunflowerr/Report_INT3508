"""R34 complementary independent read-only raw transcript probe.

No repository imports, simulations, build, install, or source mutations.
Only writes a small exclusively created output text beside this script.
All transcript frames are SHA256 checked. Parses event batches, the final runner
checkpoint, and (for budget group) pruned-candidate evidence. All outcome counts
are recomputed rather than read from aggregate summaries.
"""
import base64
import collections
import concurrent.futures
import hashlib
import json
import pathlib
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "extra-probe-output.txt"
FIXED = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
RESEARCH = pathlib.Path("C:/RideBoundData/research")
SCRATCH = pathlib.Path("E:/Code/Report_INT3508/ridebound-scratchpad")
LEVELS = (30, 60, 90, 120, 150, 180, 240, 300)
CELLS = tuple(f"d201811{d}-s10-r{r}-w07" for d in (12,13) for r in (1,2,3,4))

def scan(path, budget=False):
    final_bytes = None
    alight = {}
    blocked = set()
    frames = 0
    confirmed_decisions = 0
    non_normal = 0
    with path.open(encoding="utf-8") as handle:
        for line_no,line in enumerate(handle,1):
            record = json.loads(line)
            raw = base64.b64decode(record["frameBase64"])
            assert hashlib.sha256(raw).hexdigest() == record["frameSha256"], (path,line_no)
            frames += 1
            if record["direction"] == "runnerToAdapter" and b'"messageType":"checkpoint"' in raw:
                final_bytes = raw
            elif record["direction"] == "adapterToRunner" and b'"messageType":"eventBatch"' in raw:
                env = json.loads(raw)
                for ev in env["payload"].get("events",[]):
                    if ev.get("eventType") == "passengerAlighted":
                        rid = ev["payload"]["requestId"]
                        if rid in alight:
                            assert alight[rid] == env["simTimeMs"]
                        else:
                            alight[rid] = env["simTimeMs"]
            elif budget and record["direction"] == "runnerToAdapter" and b'"messageType":"decision"' in raw:
                env = json.loads(raw)
                evidence = env.get("payload",{}).get("solver",{}).get("executionEvidence",{})
                for candidate in evidence.get("prunedCandidates",[]):
                    if candidate.get("code") == "COMMITMENT_BUDGET_EXCEEDED" and any(
                        w.get("code") == "COMMITMENT_BUDGET_EXCEEDED"
                        for w in candidate.get("commitmentWitnesses",[])
                    ):
                        blocked.update(candidate.get("newRequestIds",[]))
    assert final_bytes is not None, path
    state = json.loads(final_bytes)["payload"]["content"]["onlineState"]
    life = {r["requestId"]:r["lifecycle"] for r in state["requests"]}
    assert set(alight) == {rid for rid,v in life.items() if v == "completed"}, path
    return state,alight,blocked,frames

def outcome(state,alight):
    promises = {}
    moved = set()
    for ledger in state["commitmentLedger"]:
        rid = ledger["requestId"]
        initial = [entry for entry in ledger["entries"] if entry["kind"] == "initialPromise"]
        assert len(initial) == 1, rid
        promises[rid] = initial[0]["publishedPromise"]["projection"]["dropEtaMs"]
        for entry in ledger["entries"]:
            if entry["kind"] == "revision":
                delta = (entry["publishedPromise"]["projection"]["dropEtaMs"]
                         - entry["exogenousProjection"]["dropEtaMs"])
                if delta != 0:
                    moved.add(rid)
    late60 = sum(alight[rid] - promises[rid] > 60000 for rid in alight)
    late120 = sum(alight[rid] - promises[rid] > 120000 for rid in alight)
    served = len(alight)
    shared = set()
    # Independent event sweep. Ending an interval precedes starting one at the
    # same instant, implementing half-open actual [pickup,alight) intervals.
    events = collections.defaultdict(list)
    for request in state["requests"]:
        rid = request["requestId"]
        if rid in alight:
            assert request["actualPickupTimeMs"] < alight[rid]
            events[request["assignedVehicleId"]].extend((
                (request["actualPickupTimeMs"],1,rid), (alight[rid],0,rid)))
    for evs in events.values():
        onboard = set()
        for instant,kind,rid in sorted(evs):
            if kind == 0:
                onboard.remove(rid)
            else:
                onboard.add(rid)
                if len(onboard) > 1:
                    shared.update(onboard)
        assert not onboard
    return dict(requests=len(state["requests"]),served=served,late60=late60,
                timely60=served-late60,timely120=served-late120,
                shared=len(shared),moved=len(moved & set(alight)),
                moved_all_accepted=len(moved))

def mapped(task):
    group,arm,path = task
    state,alight,_,frames = scan(path)
    return group,arm,path,outcome(state,alight),frames

def main():
    with OUT.open("x",encoding="utf-8",newline="\n") as output:
        def emit(value):
            line = value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,sort_keys=True)
            output.write(line+"\n");output.flush();print(line,flush=True)
        emit("R34 complementary raw probe; SHA256 verified frames; no source imports; strict A-p0 thresholds; half-open sharing.")
        tasks = []
        fixed_arms = ("b1-ref","c1-nobudget","c1-budget120","c1-budget60","c1-h6ref")
        for arm in fixed_arms:
            runs = sorted(FIXED.glob(f"w14-*-{arm}-s7"))
            assert len(runs) == 16, (arm,len(runs))
            tasks.extend(("fixed",arm,run/"attempt-01/output/transcript-00.ndjson") for run in runs)
        for arm in ("U",)+tuple(f"C-{x}" for x in LEVELS):
            family = "tier3-w07-v1" if arm == "U" or int(arm[2:]) in (30,60,120,300) else "tier3-w07x-v1"
            tasks.extend(("morning",arm,RESEARCH/family/f"{arm}-{cell}/transcript-00.ndjson") for cell in CELLS)
        snow_runs=sorted((RESEARCH/"tier3-forecast-v1").glob("C-30-d20181115-s10-r*-w1[45]"))
        assert len(snow_runs) == 8, ("snow",len(snow_runs))
        tasks.extend(("snow","C-30",p/"transcript-00.ndjson") for p in snow_runs)
        counts = collections.defaultdict(collections.Counter)
        run_counts = collections.Counter()
        frames_total = 0
        # Two read-only workers, bounded memory; no subprocesses except this probe.
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            for group,arm,path,stats,frames in pool.map(mapped,tasks):
                counts[(group,arm)].update(stats)
                run_counts[(group,arm)] += 1
                frames_total += frames
                if group == "snow":
                    emit(dict(group=group,arm=arm,source=str(path),**stats))
        for arm in fixed_arms:
            emit(dict(group="fixed",arm=arm,runs=run_counts[("fixed",arm)],**counts[("fixed",arm)]))
        for arm in ("U",)+tuple(f"C-{x}" for x in LEVELS):
            emit(dict(group="morning",arm=arm,runs=run_counts[("morning",arm)],**counts[("morning",arm)]))
        emit(dict(group="snow-total",runs=run_counts[("snow","C-30")],**counts[("snow","C-30")]))
        emit(dict(raw_frames_sha256_verified=frames_total))
        archived=[]
        chosen=[]
        other=[]
        for family in ("tier3-w07-v1","tier3-w07x-v1"):
            roots=sorted((RESEARCH/family).iterdir())
            valid = [p for p in roots if p.is_dir() and (p/"summary.json").exists()]
            statuses=collections.Counter(json.loads((p/"summary.json").read_text(encoding="utf-8"))["status"] for p in valid)
            emit(dict(group="archive-root",source=str(RESEARCH/family),run_directories=len(valid),summary_statuses=dict(statuses)))
            for run in valid:
                arm=run.name.split("-d201811",1)[0]
                archived.append(run)
                if arm=="U" or arm in {f"{f}-{x}" for f in ("C","Mplus") for x in LEVELS}:
                    chosen.append(run)
                else:
                    other.append(arm)
        emit(dict(group="morning-archive",archived=len(archived),chosen=len(chosen),
                  chosen_arms=dict(collections.Counter(p.name.split("-d201811",1)[0] for p in chosen)),
                  other_arms=dict(collections.Counter(other))))
        # Own raw budget-block probe on test cells; explicit rerun selection.
        split=json.loads((SCRATCH/"tang3/t38/split-t38-v1.json").read_text(encoding="utf-8"))
        emit(dict(split_keys=list(split)))
        cells=split["test"] if isinstance(split["test"],list) else split["test"]["cells"]
        budget_tot=collections.Counter()
        for cell in cells:
            run_c=RESEARCH/"tier3-t38-v1"/f"C-30-{cell}"
            if cell == "d20181114-s10-r3-w17":
                run_c=RESEARCH/"tier3-t38-v1"/f"C-30-{cell}-rerun1"
            state_c,_,blocked,frames_c=scan(run_c/"transcript-00.ndjson",budget=True)
            state_u,_,_,frames_u=scan(RESEARCH/"tier3-t38-v1"/f"U-{cell}/transcript-00.ndjson")
            life_u={r["requestId"]:r["lifecycle"] for r in state_u["requests"]}
            rejected={r["requestId"] for r in state_c["requests"] if r["lifecycle"]=="rejected"}
            for rid in rejected:
                recorded=rid in blocked
                budget_tot[("has-record" if recorded else "no-record")+":"+life_u[rid]]+=1
            frames_total += frames_c+frames_u
        emit(dict(group="budget-rejection",runs=len(cells),counts=dict(budget_tot)))
        emit(dict(all_raw_frames_sha256_verified=frames_total))

if __name__ == "__main__":
    main()
