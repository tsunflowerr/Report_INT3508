"""Build a wider-pickup-window copy of the sealed panel, outside the repository.

The measurement in measure_window.py says every one of the 425 rejected requests
had a candidate killed by PICKUP_WINDOW, and that the median one missed by only
44 s. That is suggestive, but it is an OPTIMISTIC bound: it ignores the ride-time
bound behind the window, and it ignores that serving a rescued rider consumes
vehicle time that some other rider was going to get.

The only way to settle that is to let the window stop binding and see what the
fleet actually does. This builds that instance: every request keeps its arrival,
origin, destination and ride-time bound, and only latestPickup moves out from
arrival + 600 s to arrival + WINDOW_MS.

This is a CEILING test, not the proposed mechanism. A selective, negotiated
widening can only ever use a subset of the freedom a uniform widening grants, so
if the uniform version buys little, the negotiated version cannot buy more.
(The converse does not hold: uniform widening also lets the optimiser delay
incumbents, which selective widening would not.)

Two files must stay consistent or the preflight refuses the run:
  * scenario-content.json  -- requests[] and the requestArrived event payloads,
    each of which carries its own payloadSha256 over canonical JSON
  * <cell>.driver.json     -- carries sourceScenarioContentSha256

Both copies are written to the scratchpad. The repository is never touched, and
is in fact hash-checked by the preflight, so it must not be.

Usage:  build_wide_fixture.py [window_seconds]     (default 900)
"""

from __future__ import annotations

import binascii
import hashlib
import json
import pathlib
import shutil
import sys

REPO = pathlib.Path(r"E:/Code/RideBound")
FIXTURE_ROOT = REPO / (
    "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/"
    "wp9-confirmatory-fixed-panel-v2"
)
DRIVER_ROOT = REPO / "benchmarks/scenarios/wp9-confirmatory"
OUT_ROOT = pathlib.Path(
    r"E:/RideBoundData/wp14/wide-window-fixture"
)

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]

# Files copied through untouched; only scenario-content.json is rewritten.
PASSTHROUGH = [
    "derivative-manifest.json",
    "normalization-report.json",
    "selection-frame.json",
    "normalizer-configuration.json",
]


def canonical(obj) -> bytes:
    """The fixture's canonical JSON: sorted keys, no whitespace, UTF-8."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rewrite_cell(cell: str, window_ms: int) -> dict:
    source_dir = FIXTURE_ROOT / cell
    target_dir = OUT_ROOT / cell
    target_dir.mkdir(parents=True, exist_ok=True)

    raw = (source_dir / "scenario-content.json").read_text(encoding="utf-8")
    scenario = json.loads(raw)

    # 1. requests[]
    changed_requests = 0
    for request in scenario["requests"]:
        wanted = request["arrivalTimeMs"] + window_ms
        if request["latestPickupMs"] != wanted:
            request["latestPickupMs"] = wanted
            changed_requests += 1

    # 2. event payloads, each with its own hash over canonical JSON
    changed_events = 0
    for event in scenario["events"]:
        payload_bytes = binascii.unhexlify(event["payloadCanonicalJsonHex"])
        if hashlib.sha256(payload_bytes).hexdigest() != event["payloadSha256"]:
            raise SystemExit(f"{cell}: source event payload hash already wrong")
        payload = json.loads(payload_bytes)
        # Refuse to touch anything whose canonical form we cannot reproduce
        # byte-for-byte, otherwise the rewrite would silently corrupt it.
        if canonical(payload) != payload_bytes:
            raise SystemExit(
                f"{cell}: canonical JSON round-trip differs; refusing to rewrite"
            )
        if event["eventType"] != "requestArrived":
            continue
        request = payload["request"]
        wanted = request["arrivalTimeMs"] + window_ms
        if request["latestPickupMs"] == wanted:
            continue
        request["latestPickupMs"] = wanted
        new_bytes = canonical(payload)
        event["payloadCanonicalJsonHex"] = binascii.hexlify(new_bytes).decode()
        event["payloadSha256"] = hashlib.sha256(new_bytes).hexdigest()
        changed_events += 1

    # The scenario file itself is not canonicalised by the harness -- it is
    # hashed verbatim -- so match the source file's own formatting.
    indent = 1 if raw.startswith("{\n ") else None
    target_scenario = target_dir / "scenario-content.json"
    target_scenario.write_text(
        json.dumps(scenario, indent=indent, sort_keys=True,
                   separators=(",", ": ") if indent else (",", ":")),
        encoding="utf-8",
        newline="\n",
    )

    for name in PASSTHROUGH:
        source_file = source_dir / name
        if source_file.exists():
            shutil.copy2(source_file, target_dir / name)

    # 3. driver, carrying the scenario hash
    driver = json.loads(
        (DRIVER_ROOT / f"{cell}.driver.json").read_text(encoding="utf-8")
    )
    new_hash = sha256_file(target_scenario)
    driver["sourceScenarioContentSha256"] = new_hash
    (OUT_ROOT / f"{cell}.driver.json").write_text(
        json.dumps(driver, indent=2, sort_keys=True),
        encoding="utf-8",
        newline="\n",
    )

    # 4. read back and verify the two invariants the preflight checks
    check = json.loads(target_scenario.read_text(encoding="utf-8"))
    for request in check["requests"]:
        if request["latestPickupMs"] - request["arrivalTimeMs"] != window_ms:
            raise SystemExit(f"{cell}: request window not applied")
    for event in check["events"]:
        payload_bytes = binascii.unhexlify(event["payloadCanonicalJsonHex"])
        if hashlib.sha256(payload_bytes).hexdigest() != event["payloadSha256"]:
            raise SystemExit(f"{cell}: rewritten event hash mismatch")
        payload = json.loads(payload_bytes)
        if event["eventType"] == "requestArrived":
            request = payload["request"]
            if request["latestPickupMs"] - request["arrivalTimeMs"] != window_ms:
                raise SystemExit(f"{cell}: event window not applied")
    if sha256_file(target_scenario) != new_hash:
        raise SystemExit(f"{cell}: scenario hash unstable")
    if check["validationSummary"] != json.loads(raw)["validationSummary"]:
        raise SystemExit(f"{cell}: validationSummary changed; cardinality drift")

    return {
        "cell": cell,
        "requests": changed_requests,
        "events": changed_events,
        "sha256": new_hash,
    }


def main() -> int:
    window_seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 900
    window_ms = window_seconds * 1000
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    print(f"target pickup window: {window_seconds} s "
          f"(sealed panel uses 600 s)")
    for cell in CELLS:
        result = rewrite_cell(cell, window_ms)
        print(f"  {result['cell']:<22} requests={result['requests']:>4} "
              f"events={result['events']:>4}  {result['sha256'][:16]}")
    print(f"\nwritten to {OUT_ROOT}")
    print("repository untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
