"""Compare the last two published plans of the offending vehicle in a b4 cell."""
from __future__ import annotations
import base64, json, pathlib, sys

def frames(path):
    with path.open(encoding="utf-8") as h:
        for line in h:
            line = line.strip()
            if line:
                yield json.loads(base64.b64decode(json.loads(line)["frameBase64"]))

cell = sys.argv[1] if len(sys.argv) > 1 else "x-d20181114-s10-r2-b4-tight-s7"
root = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-b4-repair-v1") / cell
decisions = [f for f in frames(root / "transcript-00.ndjson")
             if f.get("messageType") == "decision"]
print(f"{len(decisions)} quyet dinh")

# collect, per vehicle, the sequence of published plans
history: dict[str, list] = {}
for i, frame in enumerate(decisions):
    for action in frame.get("payload", {}).get("actions", []):
        if action.get("decisionType") != "vehiclePlanUpdated":
            continue
        p = action["payload"]
        vid = p.get("vehicleId")
        history.setdefault(vid, []).append((i, p))

print(f"{len(history)} xe co cap nhat ke hoach")
last = decisions[-1]
upd = [a["payload"] for a in last.get("payload", {}).get("actions", [])
       if a.get("decisionType") == "vehiclePlanUpdated"]
print(f"quyet dinh cuoi cap nhat {len(upd)} xe")
for p in upd:
    vid = p.get("vehicleId")
    print(f"\n=== xe {vid} ===")
    print(f"keys: {sorted(p.keys())}")
    route = p.get("route", {})
    print(f"route keys: {sorted(route.keys())}")
    print(f"executedStopCount: {route.get('executedStopCount')}")
    fp = route.get("frozenPrefix") or []
    print(f"frozenPrefix ({len(fp)} chang):")
    for s in fp:
        print(f"   {s.get('kind'):8s} node={str(s.get('nodeId'))[5:17]} rq={str(s.get('requestId'))[3:15]}")
    st = route.get("stops") or route.get("plannedStops") or []
    print(f"stops ({len(st)}):")
    for s in st:
        print(f"   {s.get('kind'):8s} node={str(s.get('nodeId'))[5:17]} rq={str(s.get('requestId'))[3:15]}")
    # previous publication for this vehicle
    hist = history.get(vid, [])
    if len(hist) >= 2:
        prev = hist[-2][1]
        proute = prev.get("route", {})
        pst = proute.get("stops") or proute.get("plannedStops") or []
        pfp = proute.get("frozenPrefix") or []
        print(f"-- lan cong bo truoc (quyet dinh #{hist[-2][0]}): "
              f"executed={proute.get('executedStopCount')} frozen={len(pfp)} stops={len(pst)}")
        for s in pst:
            print(f"   {s.get('kind'):8s} node={str(s.get('nodeId'))[5:17]} rq={str(s.get('requestId'))[3:15]}")
