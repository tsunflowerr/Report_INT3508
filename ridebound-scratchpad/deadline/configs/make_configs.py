"""Derive the Tier-2 arm configurations and prove each differs only where intended.

Base: benchmarks/configurations/wp14-c1-h6-reference-v1.json in the research worktree
(byte-identical to wp8-drop-eta-budget-tight-v1.json, the config of the sealed
`dr-conduct-*` drift runs; both SHA-256 d6124f3f...08beb).

Arms (plan T2.5):
  conduct-30  base unchanged (behavioural ledger cap 30 s on drop_eta_total_ms)
  visible-30  copied byte-for-byte from ridebound-scratchpad/drift/basis-customer-visible.json
  dl-30/60/120  base, drop_eta_total_ms hardLimit REMOVED, dropEtaDeadlineSlackMs added
  dl2-30      dl-30 plus dropEtaDeadlineTwoSided true
policyId stays wp6-synthetic-policy-overlay-v1 (the preflight hard-codes it).
Writes only into this folder; refuses to overwrite a file whose content differs.
"""
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = Path(r"E:/Code/RideBound-deadline/benchmarks/configurations/wp14-c1-h6-reference-v1.json")
VISIBLE = Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/drift/basis-customer-visible.json")
POLICY_ID = "wp6-synthetic-policy-overlay-v1"


def leaves(value, prefix=""):
    if isinstance(value, dict):
        for key, sub in value.items():
            yield from leaves(sub, f"{prefix}.{key}")
    elif isinstance(value, list):
        if value and isinstance(value[0], dict) and "dimension" in value[0]:
            for sub in value:
                yield from leaves(sub, f"{prefix}[{sub['dimension']}]")
        elif value and isinstance(value[0], dict):
            for index, sub in enumerate(value):
                yield from leaves(sub, f"{prefix}[{index}]")
        else:
            yield prefix, json.dumps(value, sort_keys=True)
    else:
        yield prefix, json.dumps(value)


def diff(a, b):
    la, lb = dict(leaves(a)), dict(leaves(b))
    return sorted(
        (k, la.get(k, "<absent>"), lb.get(k, "<absent>"))
        for k in set(la) | set(lb) if la.get(k) != lb.get(k))


def write(name, data=None, raw=None):
    target = HERE / f"{name}.json"
    content = raw if raw is not None else (
        json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if target.exists() and target.read_bytes() != content:
        raise SystemExit(f"{target} exists with different content; refusing to overwrite")
    target.write_bytes(content)
    return hashlib.sha256(content).hexdigest()


base_bytes = BASE.read_bytes()
base = json.loads(base_bytes)
assert [p["policyId"] for p in base["policies"]] == [POLICY_ID]


def deadline_arm(slack_ms, two_sided=False):
    arm = copy.deepcopy(base)
    policy = arm["policies"][0]
    drop = [l for l in policy["limits"] if l["dimension"] == "drop_eta_total_ms"]
    assert len(drop) == 1 and drop[0]["hardLimit"] == 30000
    del drop[0]["hardLimit"]
    policy["dropEtaDeadlineSlackMs"] = slack_ms
    if two_sided:
        policy["dropEtaDeadlineTwoSided"] = True
    return arm


arms = {
    "dl-30": deadline_arm(30000),
    "dl-60": deadline_arm(60000),
    "dl-120": deadline_arm(120000),
    "dl2-30": deadline_arm(30000, two_sided=True),
}
print("base sha256:", hashlib.sha256(base_bytes).hexdigest())
print("conduct-30:", write("conduct-30", raw=base_bytes), "(byte copy of base)")
visible_bytes = VISIBLE.read_bytes()
print("visible-30:", write("visible-30", raw=visible_bytes), "(byte copy of drift/basis-customer-visible.json)")
for key, old, new in diff(base, json.loads(visible_bytes)):
    print(f"    visible-30 differs at {key}: {old} -> {new}")
for name, data in arms.items():
    print(f"{name}:", write(name, data))
    for key, old, new in diff(base, data):
        print(f"    {name} differs at {key}: {old} -> {new}")
