"""Evidence-register addendum 1: anchor checks (file:line contains fragment) for every anchor cited in
EVIDENCE-REGISTER-ADDENDUM-1.md that is not one of my own script outputs, plus the document facts of N-12 / N-13 / N-14
(thesis TEX lines, thesis PDF pages via pdftotext to stdout, DACN PDF pages 1-6) and two ratios.
Read-only; one process (plus pdftotext child calls that print to stdout); no simulation/build/install; output mode "x".
A fragment passes if it occurs in the cited line after collapsing whitespace.
Usage: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B check_anchors_addendum_1.py
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "check-anchors-addendum-1-2026-10-11.txt"
SCR = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad")
DEB = SCR / "optimize/codex-debate"
TEX = pathlib.Path(r"E:/Code/Report_INT3508/ridebound/noi-dung")
PDF = pathlib.Path(r"E:/Code/Report_INT3508/ridebound/main.pdf")
DACN = pathlib.Path(r"C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf")
PDFTOTEXT = pathlib.Path(r"C:/Program Files/Git/mingw64/bin/pdftotext.exe")

FILES = {
    "STG": DEB / "claude-work/r21-stage1a/stage1a-report-2026-10-10.txt",
    "CW21": DEB / "claude-work/r21-stage1a/cum-witness-check-2026-10-10.txt",
    "CXS": DEB / "codex-work/R21B-STAGE1A-CODEX.md",
    "A": DEB / "codex-work/R15-audit-summary.txt",
    "BUC": DEB / "claude-work/budget-use-check-2026-10-09.txt",
    "C120R": SCR / "tang3/t38c120/C120-RESULTS.md",
    "R19C": DEB / "ROUND19-CLAUDE.md",
    "T38A": SCR / "tang3/t38/analysis-2026-10-02-report.txt",
    "W07": SCR / "tang3/w07/W07-REPORT.md",
    "SNOW": SCR / "optimize/test-snow-2026-10-06-report.txt",
    "CON": SCR / "optimize/report-extras/constraints-and-pooling-2026-10-06.txt",
    "TEX10": TEX / "10-tai-lieu.tex",
    "TEX08": TEX / "08-chuong4.tex",
}

CHECKS = [
    ("STG", 6, "C-120: runs 34; summary status {'pass': 34}"),
    ("STG", 6, "lifecycle {'completed': 2387, 'rejected': 1285}"),
    ("STG", 29, "C-120 | 2387 (65.01%) | 132 ( 5.53%) | 21 (0.88%) | 0 (0.00%) | 1 (0.04%) | 2255 (61.41%) | 2366 (64.43%)"),
    ("STG", 32, "U | 137 (5.63%) | 87 (3.57%) | 17 | 8 (0.33%) | 2297 (62.55%) | 2347 (63.92%) | 7.18 s"),
    ("STG", 33, "C-30 | 10 (0.43%) | 0 (0.00%) | 0 | 4 (0.17%) | 2328 (63.40%) | 2338 (63.67%) | 7.37 s"),
    ("STG", 34, "C-120 | 65 (2.72%) | 8 (0.34%) | 0 | 2 (0.08%) | 2322 (63.24%) | 2379 (64.79%) | 7.27 s"),
    ("STG", 37, "exposed with net signed c < 0: 2"),
    ("STG", 38, "exposed with net signed c < 0: 4"),
    ("STG", 39, "drop-exposed 103 (4.32%"),
    ("STG", 39, "max 118.9; exposed with net signed c < 0: 3; S >= 0.9 B (108 s): 9"),
    ("STG", 39, "overshoots S > B: 0"),
    ("STG", 44, "budget-pruned candidates 524 by class {'cumulative-only': 3, 'per-step-also': 521}"),
    ("STG", 44, "acknowledged decisions 20435; non-normal (forced) decisions 0"),
    ("STG", 50, "U: shared completions 555 of 2434 served (22.80%)"),
    ("STG", 51, "C-30: shared completions 313 of 2338 served (13.39%)"),
    ("STG", 52, "C-120: shared completions 428 of 2387 served (17.93%)"),
    ("STG", 55, "C-120 vs C-30: common 2266; only C-120 121; only C-30 72"),
    ("STG", 56, "C-120 vs U: common 2271; only C-120 116; only U 163"),
    ("STG", 58, "C-120-only (vs C-30) riders also served by U: 93 of 121"),
    ("STG", 63, "w07 C-120: requests 972; served 515; late>60 63"),
    ("STG", 66, "w08 C-120: requests 1512; served 1001; late>60 49"),
    ("STG", 69, "w17 C-120: requests 1188; served 871; late>60 20"),
    ("STG", 72, "C-120 vs C-30: more served in 23 cells, equal in 8, fewer in 3"),
    ("CW21", 3, "new request rq-ebccd435e2e: C-120 not accepted; C-30 served; U served"),
    ("CW21", 5, "new request rq-fe75a63d2e6: C-120 served; C-30 served; U served"),
    ("CW21", 7, "new request rq-3e358915954: C-120 not accepted; C-30 not accepted; U served"),
    ("CXS", 76, "| C-120 / naive | 2387 | 132 | 21 | 0 | 2255/3672 (61.411%) | 2366/3672 (64.434%) | 0.000000 | 1/2387 (0.042%) |"),
    ("CXS", 79, "| C-120 / causal-no15 | 2387 | 65 | 8 | 0 | 2322/3672 (63.235%) | 2379/3672 (64.788%) | 7.273885 | 2/2387 (0.084%) |"),
    ("CXS", 89, "| C-120 | 20435 | 0 | 103 | 0 | 118938 (118.938 s) | 0 | 521 | 3 |"),
    ("CXS", 91, "Budget-prune totals are C-30 845 and C-120 524 (=521 step failures +3 cumulative-only)"),
    ("CXS", 109, "| C-120 | C-30 | 2266 | 121 | 72 |"),
    ("CXS", 119, "| 07 h | U | 9 | 972 |"),
    ("CXS", 122, "| 08 h | U | 14 | 1512 |"),
    ("CXS", 125, "| 17 h | U | 11 | 1188 |"),
    ("A", 7, '"fc_pad30": {"early60": 44, "ext_sum_ms": 87364334.6159592, "late120": 0, "late300": 0, "late60": 2, "late600": 0, "served": 2338}'),
    ("A", 7, '"fc": {"early60": 4, "ext_sum_ms": 17224334.615959197, "late120": 0, "late300": 0, "late60": 10, "late600": 0, "served": 2338}'),
    ("A", 7, '"S_max_ms": 29239, "S_sum_exposed_ms": 359173, "exposed": 33'),
    ("A", 7, '"omitted_requests": 1'),
    ("A", 8, '"arm": "Mplus-30"'),
    ("A", 9, '"fc": {"early60": 8, "ext_sum_ms": 17484227.789631333, "late120": 87, "late300": 17, "late60": 137, "late600": 2, "served": 2434}'),
    ("A", 9, '"fc_pad30": {"early60": 44, "ext_sum_ms": 90504227.78963134, "late120": 68, "late300": 11, "late60": 106, "late600": 1, "served": 2434}'),
    ("A", 9, '"S_max_ms": 590133'),
    ("A", 9, '"repeated": 12'),
    ("A", 7, '"candidates": {"step-fails": 845}'),
    ("BUC", 34, "net signed c among exposed: mean 137.7 s, negative (earlier) 2"),
    ("BUC", 37, "net signed c among exposed: mean 10.9 s, negative (earlier) 4"),
    ("C120R", 10, "Runs: 34/34 `status: pass`, 2026-10-10 22:12–23:48, `C:/RideBoundData/research/tier3-t38c120-v1`."),
    ("C120R", 14, "| C-120 naive | 2,387 | 132 | 21 | 0 | 2,255 | 2,366 | 0 s | 1 |"),
    ("C120R", 15, "| C-120 forecast (causal-no15) | 2,387 | 65 | 8 | 0 | 2,322 | 2,379 | 7.27 s | 2 |"),
    ("C120R", 16, "| C-30 naive | 2,338 | 76 | 11 | 0 | 2,262 | 2,327 | 0 s | 3 |"),
    ("C120R", 17, "| C-30 forecast | 2,338 | 10 | 0 | 0 | 2,328 | 2,338 | 7.37 s | 4 |"),
    ("C120R", 18, "| U naive | 2,434 | 203 | 102 | 18 | 2,231 | 2,332 | 0 s | 7 |"),
    ("C120R", 19, "| U forecast | 2,434 | 137 | 87 | 17 | 2,297 | 2,347 | 7.18 s | 8 |"),
    ("C120R", 21, "Other C-120 facts: 0 non-normal (forced) decisions; 0 riders with Σ|c| > 120 s (max 118.9 s); 103 drop-exposed riders"),
    ("C120R", 22, "(4.32%), none with ≥ 2 nonzero changes; Σ|c| among exposed mean 55.5 s, p50 62.5 s, p90 104.9 s; 524 recorded"),
    ("C120R", 23, "drop-budget prune records = 521 single-step + 3 cumulative-only"),
    ("C120R", 24, "shared rides 428 (17.93% of served)"),
    ("C120R", 25, "served-set overlap C-120/C-30 2,266 common, 121 only C-120, 72 only C-30;"),
    ("C120R", 26, "C-120/U 2,271 / 116 / 163. Per window, C-120 serves +4 (w07), +26 (w08), +19 (w17) over C-30."),
    ("R19C", 3, "The owner approved both steps of the R17/R18 list"),
    ("R19C", 4, "Stage 1b cost-first 2×2 next"),
    ("T38A", 76, "own promise broken 0.000 (cells > 0: 0)"),
    ("T38A", 77, "Mplus-30 served 2338 | forced 0.413"),
    ("T38A", 77, "own promise broken 0.145 (cells > 0: 28)"),
    ("T38A", 83, "forced 0.756"),
    ("T38A", 83, "own promise broken 0.365 (cells > 0: 9)"),
    ("W07", 49, "khách trễ nhất có A = 307,3 s = 99,1 s do tắc đường (tổng x) + 208,2 s do chính bộ"),
    ("W07", 53, "Dưới `C-30`, cùng ô, khách trễ nhất 99,1 s, gần như toàn bộ do tắc đường (97,1 s)."),
    ("SNOW", 10, "all 8: Y naive 0.0719 disp 0.0594"),
    ("CON", 5, "73.4%"),
    ("CON", 6, "drop revisions with a pooling-caused change (c != 0): 187; |c| median 108.6 s"),
    ("CON", 12, "1.2%"),
    ("CON", 13, "drop revisions with a pooling-caused change (c != 0): 33; |c| median 8.3 s"),
    ("TEX10", 1, "\\chapter*{Tài liệu tham khảo}"),
    ("TEX10", 4, "\\begin{thebibliography}{99}"),
    ("TEX08", 160, "Hành khách được phục vụ & 1.735 & 1.581"),
    ("TEX08", 1728, "Khách bị chấm 0 dù thực tế bị dời & 663 ($38{,}2\\%$) & 774 ($\\mathbf{49{,}0\\%}$)"),
]


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def pdf_page(path: pathlib.Path, page: int) -> list[str]:
    res = subprocess.run([str(PDFTOTEXT), "-enc", "UTF-8", "-f", str(page), "-l", str(page), str(path), "-"],
                         capture_output=True, check=True)
    return [line for line in res.stdout.decode("utf-8").replace("\f", "\n").split("\n") if line.strip()]


def main() -> int:
    out = ["# check_anchors_addendum_1.py (2026-10-11)"]
    texts = {k: p.read_text(encoding="utf-8").split("\n") for k, p in FILES.items()}
    ok = fail = 0
    for key, line, frag in CHECKS:
        lines = texts[key]
        got = norm(lines[line - 1]) if line <= len(lines) else ""
        if norm(frag) in got:
            ok += 1
            out.append(f"OK   {key}:{line}  {frag[:110]}")
        else:
            fail += 1
            near = [i + 1 for i in range(max(0, line - 4), min(len(lines), line + 3)) if norm(frag) in norm(lines[i])]
            anywhere = next((i + 1 for i, l in enumerate(lines) if norm(frag) in norm(l)), None)
            out.append(f"FAIL {key}:{line}  {frag[:110]}  | near {near} | first hit {anywhere}")
    out.append(f"anchor checks: {ok} OK, {fail} FAIL")
    out.append(f"ratios: 774/1581 = {774 / 1581:.4%}; 663/1735 = {663 / 1735:.4%}")
    for label, path, pages in (("main.pdf", PDF, (8, 102, 103)), ("DACN", DACN, (1, 2, 3, 4, 5, 6))):
        for p in pages:
            lines = pdf_page(path, p)
            out.append(f"{label} p.{p}: {len(lines)} non-empty lines; first: {[norm(l)[:90] for l in lines[:6]]}")
    text = "\n".join(out) + "\n"
    with open(OUT, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
