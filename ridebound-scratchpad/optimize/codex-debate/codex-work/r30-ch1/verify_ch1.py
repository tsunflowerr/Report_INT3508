"""Read-only prose/static LaTeX checks. Never builds; outputs are exclusive."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "05-chuong1.tex")
OUTPUT = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "05-chuong1-QA.txt")
assert SOURCE.parent == ROOT and OUTPUT.parent == ROOT
text = SOURCE.read_text(encoding="utf-8")
clean = re.sub(r"(?<!\\)%[^\n]*", "", text)

def prose(value):
    value = re.sub(r"\\begin\{(figure|table)\}[\s\S]*?\\end\{\1\}", "", value)
    value = re.sub(r"\\(?:chapter|section)\{[^}]*\}", "", value)
    value = re.sub(r"\\(?:label|ref|cite)\{[^}]*\}", "", value)
    value = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?", "", value)
    value = re.sub(r"\\item(?:\[[^\]]*\])?", "", value)
    value = value.replace(r"\%", "%")
    value = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?", "", value)
    value = re.sub(r"[{}~\\]", " ", value)
    return value

parts = re.split(r"\\section\{[^}]*\}", clean)
counts = [len(prose(part).split()) for part in parts]
labels = re.findall(r"\\label\{([^}]+)\}", clean)
refs = re.findall(r"\\ref\{([^}]+)\}", clean)
cites = sorted(set(re.findall(r"\\cite\{([^}]+)\}", clean)))
stack = []
errors = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", clean):
    if match[1] == "begin":
        stack.append(match[2])
    elif not stack or stack.pop() != match[2]:
        errors.append("environment mismatch at " + str(match.start()))
if stack:
    errors.append("unclosed environments " + repr(stack))
balance = 0
for match in re.finditer(r"(?<!\\)[{}]", clean):
    balance += 1 if match[0] == "{" else -1
    if balance < 0:
        errors.append("negative brace balance")
if balance:
    errors.append("brace balance " + str(balance))
if len(labels) != len(set(labels)):
    errors.append("duplicate labels")
banned = ["niêm phong", "tiền đăng ký", "dự đoán trước", "kết quả mong đợi", "duy nhất", "đầu tiên", "vượt trội", "tối ưu", "quy trách", "chúng tôi", "ba nguyên nhân"]
for phrase in banned:
    if phrase in clean.lower():
        errors.append("banned phrase " + phrase)
drafts = ROOT.parents[3] / "rewrite-2026-10" / "drafts"
label_sources = {}
for name in ["06-chuong2-v4.tex", "07-chuong3-v3.tex", "08-chuong4-phanA-v4.tex", "09-chuong4-phanB-v7.tex"]:
    path = drafts / name
    for label in re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8")):
        label_sources[label] = name
external_refs = sorted(set(refs) - set(labels))
pending = [ref for ref in external_refs if ref not in label_sources]
if pending != ["chuong:ketluan"]:
    errors.append("unexpected unresolved refs " + repr(pending))
contribution = clean.split(r"\noindent\textbf{Đóng góp của khóa luận.}", 1)[1].split("Các kết quả chính", 1)[0]
result = {
    "source": SOURCE.name,
    "count_method": "whitespace tokens; prose includes bullets and khungy, excludes headings/figures/tables/comments/citation and reference commands",
    "words_opening_sections_1_to_6": counts,
    "total_running_words": sum(counts),
    "contribution_words_excluding_heading": len(prose(contribution).split()),
    "labels": labels,
    "external_refs": {ref: label_sources.get(ref, "ROUND31 requires this label; draft not yet available") for ref in external_refs},
    "citation_keys": cites,
    "ev_lines": len(re.findall(r"^% EV:", text, re.M)),
    "figures": clean.count(r"\begin{figure}"),
    "tables": clean.count(r"\begin{table}"),
    "body_number_tokens": sorted(set(re.findall(r"(?<![A-Za-z])\d[\d.,:/-]*", prose(clean)))),
    "errors": errors,
    "not_checked": "No compilation or rendered layout check: brief prohibits builds. Sources are read only."
}
with OUTPUT.open("x", encoding="utf-8", newline="\n") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({key: result[key] for key in ["source", "words_opening_sections_1_to_6", "total_running_words", "contribution_words_excluding_heading", "ev_lines", "errors"]}, ensure_ascii=False))
if errors:
    raise SystemExit(1)
