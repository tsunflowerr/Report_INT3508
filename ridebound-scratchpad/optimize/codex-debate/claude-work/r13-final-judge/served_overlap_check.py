"""R13 final judge, read-only: overlap of the completed-rider sets of T3.8 U and C-30 (34 test cells), and of C-30 and
Mplus-30, from the last checkpoint of each transcript.  Usage: python -B served_overlap_check.py <out.txt> (mode "x")."""
import base64, json, pathlib, sys

OPT = pathlib.Path("E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402


def completed(arm, cell):
    path = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
    last = None
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            if row["direction"] != "runnerToAdapter":
                continue
            frame = base64.b64decode(row["frameBase64"])
            if b'"checkpoint"' in frame[:120]:
                last = frame
    state = json.loads(last)["payload"]["content"]["onlineState"]
    return {(cell, r.get("requestId") or r.get("id")) for r in state["requests"] if r["lifecycle"] == "completed"}


def main():
    cells = list(fa.run_t38.PHASES["test"][1])
    sets = {arm: set() for arm in ("U", "C-30", "Mplus-30")}
    for c in cells:
        for arm in sets:
            sets[arm] |= completed(arm, c)
    u, c30, m = sets["U"], sets["C-30"], sets["Mplus-30"]
    lines = ["# served_overlap_check.py (T3.8, 34 test cells)",
             f"U {len(u)}; C-30 {len(c30)}; Mplus-30 {len(m)}",
             f"U and C-30: common {len(u & c30)}; U only {len(u - c30)}; C-30 only {len(c30 - u)}",
             f"C-30 and Mplus-30: common {len(c30 & m)}; C-30 only {len(c30 - m)}; Mplus-30 only {len(m - c30)}"]
    text = "\n".join(lines) + "\n"
    with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
