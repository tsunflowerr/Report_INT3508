"""R17 final judge: read-only spot check of Codex META:8-9 (forcedNoWorse entries in T3.8 M+-30 terminal frames).

For each given T3.8 M+-30 transcript: take the largest runnerToAdapter-or-any frame among the last 5 lines, verify its
sha256 against frameSha256, decode, and count substring occurrences of the JSON string tokens "forcedNoWorse",
"forcedReference", "exogenousServiceQuality". Also report the commitmentRecovery value found in the first frames, if any.
No simulation; read-only; output file opened with mode "x".
Usage: python -B spot_check_forced_noworse.py <out.txt> <transcript> [<transcript> ...]
"""
import base64
import hashlib
import json
import sys


def last_lines(path, n=5, chunk=64 * 1024 * 1024):
    with open(path, "rb") as fh:
        fh.seek(0, 2)
        size = fh.tell()
        start = max(0, size - chunk)
        fh.seek(start)
        data = fh.read()
    lines = data.splitlines()
    if start > 0:
        lines = lines[1:]
    return lines[-n:]


def first_frames(path, n=3):
    out = []
    with open(path, "rb") as fh:
        for _ in range(n):
            line = fh.readline()
            if not line:
                break
            env = json.loads(line)
            out.append(base64.b64decode(env["frameBase64"]))
    return out


def main():
    out_path, paths = sys.argv[1], sys.argv[2:]
    rows = []
    for p in paths:
        best = None
        for line in last_lines(p):
            env = json.loads(line)
            if best is None or env["frameLengthBytes"] > best["frameLengthBytes"]:
                best = env
        raw = base64.b64decode(best["frameBase64"])
        sha_ok = hashlib.sha256(raw).hexdigest() == best["frameSha256"] and len(raw) == best["frameLengthBytes"]
        text = raw.decode("utf-8")
        counts = {k: text.count('"' + k + '"') for k in ("forcedNoWorse", "forcedReference", "exogenousServiceQuality")}
        rec = None
        for fr in first_frames(p, 4):
            s = fr.decode("utf-8", "replace")
            i = s.find("no-worse-than-reference")
            if i >= 0:
                rec = s[max(0, i - 40): i + 30]
                break
        msg = json.loads(text).get("messageType")
        rows.append({"path": p, "ordinal": best["ordinal"], "messageType": msg, "frameBytes": best["frameLengthBytes"],
                     "sha_ok": sha_ok, "token_counts": counts, "recovery_snippet": rec})
    with open(out_path, "x", encoding="utf-8") as fh:
        fh.write("# spot_check_forced_noworse.py (R17 final judge; read-only)\n")
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
