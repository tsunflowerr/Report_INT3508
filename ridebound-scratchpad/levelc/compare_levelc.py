"""What does the warning layer actually change?

The service counts of level C and its control came out equal on the first cells,
but the sealed semantic hashes differ -- so the warning layer is NOT inert: it
picks different plans, it just serves the same number of riders. That makes the
interesting question a different one.

The warning layer is supposed to make the dispatcher spend a rider's ETA budget
reluctantly. If it does that, then at equal service it should move promises
LESS. That would be the first free improvement in this whole line of work: same
hard cap, same riders served, quieter promises.

This compares the two arms on the nine-measure battery already used for the
sealed panel, plus the budget-utilisation distribution, and states plainly
whether any difference clears the panel's noise floor (+-7 riders, +-0.3 pp).

    control    hard-vector policy  +  120 s cap   (frontier-v1/fr-budget120-*)
    level C    soft-hybrid policy  +  120 s cap   (levelc-v1/lc-*)

Read-only.
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "measure"))

from measure_instability import percentile, scan_run  # noqa: E402

CONTROL = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")
TREAT = pathlib.Path(r"E:/RideBoundData/wp14/levelc-v1")
CELLS = [
    "d201811{}-s10-r{}".format(day, rep)
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]
REQUESTS = 108 * len(CELLS)
B1 = 1735


def gather(root: pathlib.Path, pattern: str, cells: list[str]) -> dict:
    total = {
        "linear": 0.0, "quadratic": 0.0, "step": 0.0, "proximity": 0.0,
        "count": 0, "publications": 0, "linearVisible": 0.0,
        "linearExogenous": 0.0, "accepted": 0,
    }
    per_request: list[float] = []
    for cell in cells:
        stat = scan_run(root / pattern.format(cell))
        for key in total:
            total[key] += stat[key]
        per_request.extend(stat["perRequest"])
    total["perRequest"] = sorted(per_request)
    return total


def main() -> int:
    ready = [c for c in CELLS
             if (TREAT / "lc-{}-s7".format(c) / "summary.json").exists()
             and (CONTROL / "fr-budget120-{}-s7".format(c) / "summary.json").exists()]
    print("so o ghep duoc: {}/{}".format(len(ready), len(CELLS)))
    if not ready:
        return 0
    if len(ready) < len(CELLS):
        print("CHUA DU 20 O -- con so duoi day chi de theo doi, chua ket luan")
    print()

    control = gather(CONTROL, "fr-budget120-{}-s7", ready)
    treat = gather(TREAT, "lc-{}-s7", ready)

    def row(label: str, a: float, b: float, fmt: str = "{:,.0f}") -> None:
        change = "" if a == 0 else "{:+7.2f} %".format(100.0 * (b / a - 1.0))
        same = "  giong het" if a == b else ""
        print("{:<34}{:>14}{:>14}{:>11}{}".format(
            label, fmt.format(a), fmt.format(b), change, same))

    head = "{:<34}{:>14}{:>14}{:>11}".format(
        "Dai luong", "doi chung", "muc C", "thay doi")
    print(head)
    print("-" * len(head))
    row("Khach duoc phuc vu", control["accepted"], treat["accepted"])
    row("Lan cong bo loi hua", control["publications"], treat["publications"])
    row("Lan cong bo co dich chuyen", control["count"], treat["count"])
    print("-" * len(head))
    row("Tuyen tinh (s)", control["linear"] / 1000, treat["linear"] / 1000,
        "{:,.1f}")
    row("Can bac hai cua binh phuong (s)",
        (control["quadratic"] ** 0.5) / 1000,
        (treat["quadratic"] ** 0.5) / 1000, "{:,.1f}")
    row("Co trong so buoc (s)", control["step"] / 1000, treat["step"] / 1000,
        "{:,.1f}")
    row("Co trong so ke can (s)", control["proximity"] / 1000,
        treat["proximity"] / 1000, "{:,.1f}")
    row("Khach nhin thay (s)", control["linearVisible"] / 1000,
        treat["linearVisible"] / 1000, "{:,.1f}")
    row("Ngoai sinh (s)", control["linearExogenous"] / 1000,
        treat["linearExogenous"] / 1000, "{:,.1f}")
    print("-" * len(head))
    row("Khach bi dich nang nhat (s)",
        max(control["perRequest"], default=0) / 1000,
        max(treat["perRequest"], default=0) / 1000, "{:,.1f}")
    row("Phan vi 95 moi khach (s)",
        percentile(control["perRequest"], 0.95) / 1000,
        percentile(treat["perRequest"], 0.95) / 1000, "{:,.1f}")
    row("So khach bi dich it nhat 1 lan",
        sum(1 for v in control["perRequest"] if v > 0),
        sum(1 for v in treat["perRequest"] if v > 0))
    print("-" * len(head))

    if len(ready) == len(CELLS):
        delta = treat["accepted"] - control["accepted"]
        p_c = 100.0 * (control["accepted"] - B1) / REQUESTS
        p_t = 100.0 * (treat["accepted"] - B1) / REQUESTS
        print()
        print("gia loi hua so voi B1={}:  doi chung {:+.2f} pp   muc C {:+.2f} pp"
              .format(B1, p_c, p_t))
        print("chenh lech phuc vu: {:+d} khach  ({:+.2f} pp)".format(
            delta, p_t - p_c))
        print()
        if abs(delta) <= 7:
            print("Chenh lech phuc vu nam trong san nhieu quy dao (+-7 khach).")
        movement = treat["linear"] - control["linear"]
        if control["linear"]:
            print("Xao tron do quyet dinh doi {:+.2f} %.".format(
                100.0 * movement / control["linear"]))
        hashes_differ = sum(
            1 for c in ready
            if json.loads((TREAT / "lc-{}-s7".format(c) / "summary.json")
                          .read_text(encoding="utf-8"))["semanticHash"]
            != json.loads((CONTROL / "fr-budget120-{}-s7".format(c)
                           / "summary.json").read_text(encoding="utf-8"))["semanticHash"])
        print("So o co bam ngu nghia niem phong khac nhau: {}/{}".format(
            hashes_differ, len(ready)))
        print()
        if hashes_differ and abs(delta) <= 7 and abs(movement) < 0.01 * abs(control["linear"]):
            print("Bam khac nhau KHONG co nghia la quyet dinh khac nhau: nhanh")
            print("soft-hybrid ghi them chung cu canh bao vao bang chung niem")
            print("phong va phat cac lan cong bo theo thu tu khac ben trong cung")
            print("mot khung. Xem decision_identity.py -- no so tung quyet dinh")
            print("mot va cho thay hai nhanh trung khop hoan toan.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
