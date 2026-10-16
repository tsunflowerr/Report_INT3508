"""Did the repaired plan move the stop the vehicle was already driving to?

The adapter locks the active leg: once a vehicle is en route to stop S, any
replacement plan must keep S as its next stop. This prints, for the vehicle
named in the failure, the mutable suffix of every publication, so we can see
whether the final (crashing) plan changed the head of that suffix.
"""
from __future__ import annotations
import base64, json, pathlib, sys

def frames(path):
    with path.open(encoding="utf-8") as h:
        for line in h:
            line = line.strip()
            if line:
                yield json.loads(base64.b64decode(json.loads(line)["frameBase64"]))

def short(stop):
    return (f"{stop.get('kind','?'):7s}"
            f" n={str(stop.get('nodeId'))[5:15]}"
            f" rq={str(stop.get('requestId'))[3:13]}")

cell = sys.argv[1] if len(sys.argv) > 1 else "x-d20181114-s10-r2-b4-tight-s7"
root = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-b4-repair-v1") / cell
decisions = [f for f in frames(root / "transcript-00.ndjson")
             if f.get("messageType") == "decision"]

target = None
history = []
for i, frame in enumerate(decisions):
    for action in frame.get("payload", {}).get("actions", []):
        if action.get("decisionType") != "vehiclePlanUpdated":
            continue
        p = action["payload"]
        if i == len(decisions) - 1:
            target = p.get("vehicleId")

for i, frame in enumerate(decisions):
    for action in frame.get("payload", {}).get("actions", []):
        if action.get("decisionType") != "vehiclePlanUpdated":
            continue
        p = action["payload"]
        if p.get("vehicleId") == target:
            history.append((i, p["route"]))

print(f"xe {str(target)[4:16]} duoc cong bo {len(history)} lan trong {len(decisions)} quyet dinh")
print()
for i, route in history[-6:]:
    fp = route.get("frozenPrefix") or []
    ms = route.get("mutableSuffix") or []
    tag = "  <-- ban cuoi, gay loi" if (i, route) == history[-1] else ""
    print(f"quyet dinh #{i}: executed={route.get('executedStopCount')} "
          f"frozen={len(fp)} mutable={len(ms)} v={route.get('planVersion')}{tag}")
    for s in ms:
        print(f"      M {short(s)}")
    if not ms:
        print("      (khong con chang nao co the thay doi)")
print()
print("Dau cua mutableSuffix qua cac lan cong bo cuoi:")
for i, route in history[-8:]:
    ms = route.get("mutableSuffix") or []
    head = short(ms[0]) if ms else "(rong)"
    print(f"  #{i:3d}  {head}")
