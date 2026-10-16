"""Insert a UTF-8 fragment before the first \\section{ that follows a given \\label.

Usage: insert_after_label.py <tex file> <label> <fragment file>
Refuses to run twice: aborts if the fragment's first line is already present.
"""
import sys
from pathlib import Path

tex_path, label, fragment_path = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
text = tex_path.read_text(encoding="utf-8")
fragment = fragment_path.read_text(encoding="utf-8")
first_line = fragment.splitlines()[0]
if first_line in text:
    raise SystemExit(f"already inserted: {first_line!r}")
anchor = text.index("\\label{" + label + "}")
cut = text.index("\\section{", anchor + 1)
new = text[:cut] + fragment.rstrip("\n") + "\n\n" + text[cut:]
tex_path.write_text(new, encoding="utf-8", newline="\n")
print(f"inserted {len(fragment.splitlines())} lines at char {cut}")
