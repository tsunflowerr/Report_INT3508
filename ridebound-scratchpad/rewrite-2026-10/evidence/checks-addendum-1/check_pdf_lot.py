"""Evidence-register addendum 1, supplement to check_anchors_addendum_1.py: print the table-of-contents entries of
main.pdf page 8 around "Danh sách" (list of figures / list of tables and their roman page numbers), N-12.
Read-only; pdftotext prints to stdout; output mode "x".
Usage: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B check_pdf_lot.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "check-pdf-lot-2026-10-11.txt"
PDF = r"E:/Code/Report_INT3508/ridebound/main.pdf"
EXE = r"C:/Program Files/Git/mingw64/bin/pdftotext.exe"

res = subprocess.run([EXE, "-enc", "UTF-8", "-f", "8", "-l", "8", PDF, "-"], capture_output=True, check=True)
lines = [l.strip() for l in res.stdout.decode("utf-8").replace("\f", "\n").split("\n") if l.strip()]
out = ["# check_pdf_lot.py: main.pdf p.8, entries around 'Danh sách' (entry, next line = page number)"]
for i, l in enumerate(lines):
    if l.startswith("Danh s") or l.startswith("Danh m"):
        out.append(f"line {i + 1}: {l!r} -> next {lines[i + 1]!r}")
text = "\n".join(out) + "\n"
with open(OUT, "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
sys.stdout.write(text)
