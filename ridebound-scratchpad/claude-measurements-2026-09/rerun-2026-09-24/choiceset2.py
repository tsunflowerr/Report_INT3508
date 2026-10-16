"""Choice-set thinness counted in INSERTION candidates (retained count minus the no-op).

retainedCandidateCount includes the safety no-op (every vehicle has count 1 in epochs
without a new request). Ranking insertion positions (level A) needs >= 2 insertion
candidates, i.e. retainedCandidateCount >= 3. Read-only.
"""
import base64
import collections
import json
import os

ROOT = r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7", "-c1-tight-s7"):
    active_epochs = 0
    sets = collections.Counter()      # insertion-candidate count per vehicle set, active epochs
    epochs_with_rankable = 0          # active epochs with >= 1 vehicle having >= 2 insertions
    epochs_with_any_insertion = 0     # active epochs with >= 1 vehicle having >= 1 insertion
    for cell in sorted(d for d in os.listdir(ROOT) if tag in d):
        with open(os.path.join(ROOT, cell, "transcript-00.ndjson"), encoding="utf-8") as handle:
            for line in handle:
                frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if frame.get("messageType") != "decision":
                    continue
                actions = frame["payload"].get("actions", [])
                if not any(a["decisionType"] in ("requestAccepted", "requestRejected") for a in actions):
                    continue
                active_epochs += 1
                losses = (frame["payload"].get("solver", {}).get("executionEvidence", {})
                          .get("generation", {}).get("vehicleLosses", []) or [])
                insertions = [max(0, l.get("retainedCandidateCount", 0) - 1) for l in losses]
                for count in insertions:
                    sets[count] += 1
                if any(count >= 2 for count in insertions):
                    epochs_with_rankable += 1
                if any(count >= 1 for count in insertions):
                    epochs_with_any_insertion += 1
    total = sum(sets.values())
    print(f"=== {tag}: active epochs {active_epochs}, vehicle sets {total}")
    for count in sorted(sets):
        print(f"  {count} insertion candidate(s): {sets[count]:6d}  ({100*sets[count]/total:5.2f}%)")
    print(f"  sets with >= 2 insertions: {sum(v for k, v in sets.items() if k >= 2)} "
          f"({100*sum(v for k, v in sets.items() if k >= 2)/total:.2f}%)")
    print(f"  active epochs with >= 1 vehicle having >= 1 insertion: {epochs_with_any_insertion} "
          f"({100*epochs_with_any_insertion/active_epochs:.1f}%)")
    print(f"  active epochs with >= 1 vehicle having >= 2 insertions: {epochs_with_rankable} "
          f"({100*epochs_with_rankable/active_epochs:.1f}%)")
