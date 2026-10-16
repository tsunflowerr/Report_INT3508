"""R16 evidence, Q2 calibration (zero-run, read-only): on the 8 w07 cells, where C-60 ... C-300 were actually run, are
the requests that the first-order screen lets pass at B the SAME requests that C-B serves and C-30 rejects?
Screen = q2_budget_screen.py logic (imported, unchanged) on the w07 C-30 runs. Realised = requests with lifecycle
'completed' under C-B and 'rejected' under C-30 (and the reverse: served by C-30, not by C-B).
Usage: python -B q2_screen_identity_w07.py <out.txt>   (out opened with mode "x"; single process)."""
import base64
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import q2_budget_screen as qs  # noqa: E402

W07 = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
W07X = pathlib.Path(r"C:/RideBoundData/research/tier3-w07x-v1")
ARMS = ((60, W07), (90, W07X), (120, W07), (150, W07X), (180, W07X), (240, W07X), (300, W07))


def life(run):
    _, _, state = qs.fa.audit_vep.load(run / "transcript-00.ndjson")
    return {q["requestId"]: q["lifecycle"] for q in state["requests"]}


def screen_pass(cell):
    """request -> smallest max(after) over its drop-only budget-pruned candidates (acknowledged), C-30 run."""
    tc = W07 / f"C-30-{cell}" / "transcript-00.ndjson"
    rejected = {r for r, l in life(W07 / f"C-30-{cell}").items() if l == "rejected"}
    acked, best = set(), {}
    rows = []
    with open(tc, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            frame = base64.b64decode(row["frameBase64"])
            if row["direction"] == "adapterToRunner":
                if b'"decisionApplied"' in frame[:160]:
                    acked.add(json.loads(frame)["payload"]["decisionHash"])
                continue
            if b'"decision"' not in frame[:160] or b"COMMITMENT_BUDGET_EXCEEDED" not in frame:
                continue
            p = json.loads(frame)["payload"]
            for pc in (p.get("solver") or {}).get("executionEvidence", {}).get("prunedCandidates", []):
                if pc.get("code") != "COMMITMENT_BUDGET_EXCEEDED":
                    continue
                ws = [w for w in pc.get("commitmentWitnesses", []) if w.get("code") == "COMMITMENT_BUDGET_EXCEEDED"]
                if ws and all(w["dimension"] == "drop_eta_total_ms" for w in ws):
                    rows.append((p["decisionHash"], pc.get("newRequestIds", []), max(w["after"] for w in ws)))
    for h, newreq, after in rows:
        if h in acked:
            for r in newreq:
                if r in rejected:
                    best[r] = min(best.get(r, after), after)
    return best


def main():
    out = sys.argv[1]
    lines = ["# q2_screen_identity_w07.py: first-order screen vs realised C-B runs, 8 w07 cells", ""]
    tot = {b: [0, 0, 0, 0, 0] for b, _ in ARMS}
    for cell in qs.CELLS_W07:
        best = screen_pass(cell)
        l30 = life(W07 / f"C-30-{cell}")
        for b, root in ARMS:
            lb = life(root / f"C-{b}-{cell}")
            screen = {r for r, a in best.items() if a <= b * 1000}
            gained = {r for r in lb if lb[r] == "completed" and l30.get(r) == "rejected"}
            lost = {r for r in lb if lb[r] != "completed" and l30.get(r) == "completed"}
            t = tot[b]
            t[0] += len(screen); t[1] += len(gained); t[2] += len(screen & gained); t[3] += len(lost)
            t[4] += len(gained - screen)
    for b, _ in ARMS:
        s, g, both, lost, other = tot[b]
        lines.append(f"B={b:>3d} s: screen-pass {s} | realised C-{b} served & C-30 rejected {g} | in both {both} | "
                     f"realised gains not predicted by the screen {other} | C-30-served riders not served by C-{b} {lost} | net {g - lost:+d}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
