"""Read-only checks of numbers, EV coverage, syntax, citations and every ref."""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
WORK = ROOT.parent
SCRATCH = WORK.parents[2]
SOURCE = ROOT / "05-chuong1-v4-v3.tex"
OUTPUT = ROOT / "05-chuong1-v4-QA.json"
text = SOURCE.read_text(encoding="utf-8")
clean = re.sub(r"(?<!\\)%[^\n]*", "", text)
errors = []

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

counts = [len(prose(part).split()) for part in re.split(r"\\section\{[^}]*\}", clean)]
labels = re.findall(r"\\label\{([^}]+)\}", clean)
refs = sorted(set(re.findall(r"\\ref\{([^}]+)\}", clean)))
required = ["chuong:modau", "muc:c1-boicanh", "muc:c1-cauhoi", "muc:c1-lienquan", "muc:c1-donggop", "muc:c1-phamvi", "muc:c1-cautruc"]
if not set(required) <= set(labels):
    errors.append("missing required labels")
if len(labels) != len(set(labels)):
    errors.append("duplicate labels")
targets = [
    SCRATCH / "rewrite-2026-10/drafts/06-chuong2-v4.tex",
    WORK / "r33-ch3v4/07-chuong3-v4-v3.tex",
    WORK / "r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex",
    SCRATCH / "rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex",
    WORK / "r31-ch5/10-chuong5-v2.tex",
]
ref_map = {label: SOURCE.name for label in labels}
target_labels = {}
for path in targets:
    value = path.read_text(encoding="utf-8")
    found = re.findall(r"\\label\{([^}]+)\}", value)
    target_labels[str(path)] = len(found)
    for label in found:
        ref_map.setdefault(label, str(path))
for ref in refs:
    if ref not in ref_map:
        errors.append("undefined ref " + ref)
bibpath = WORK / "r32-bib/10-tai-lieu-draft-v2.tex"
bibkeys = set(re.findall(r"\\bibitem\{([^}]+)\}", bibpath.read_text(encoding="utf-8")))
cites = sorted({key for group in re.findall(r"\\cite\{([^}]+)\}", clean) for key in group.split(",")})
for cite in cites:
    if cite not in bibkeys:
        errors.append("undefined cite " + cite)
stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", clean):
    if match[1] == "begin":
        stack.append(match[2])
    elif not stack or stack.pop() != match[2]:
        errors.append("environment mismatch")
if stack:
    errors.append("unclosed environment " + repr(stack))
balance = 0
for match in re.finditer(r"(?<!\\)[{}]", clean):
    balance += 1 if match[0] == "{" else -1
    if balance < 0:
        errors.append("negative brace balance")
if balance:
    errors.append("unbalanced braces")
for phrase in ["niêm phong", "tiền đăng ký", "dự đoán trước", "kết quả mong đợi", "duy nhất", "đầu tiên", "vượt trội", "tối ưu", "quy trách", "chúng tôi", "ba nguyên nhân"]:
    if phrase in text.lower():
        errors.append("forbidden phrase " + phrase)
numeric_paragraphs = 0
for paragraph in re.split(r"\n\s*\n", text):
    visible = re.sub(r"(?<!\\)%[^\n]*", "", paragraph)
    visible = re.sub(r"\\(?:label|ref|cite)\{[^}]*\}", "", visible)
    visible = re.sub(r"\\item\[CH[123]\.\]", "", visible)
    if re.search(r"\d", visible):
        numeric_paragraphs += 1
        if "% EV:" not in paragraph:
            errors.append("numeric block lacks EV: " + visible[:80])
flat = " ".join(clean.split())
must = [
    "Mỗi luật đều có khách như vậy ở 28 trong 34 kịch bản",
    "292 khách tới muộn trong 2.338 khách được phục vụ",
    "luật hạn chót có 289 trong 2.338",
    "thêm 31 ở ngưỡng một phút, mất 5 ở hai phút",
    "0 trong 20.760 quyết định được xác nhận",
    "37,2 thay vì 7,4 giây",
    "3 trong 1.780 bản ghi loại phương án",
    "không có bản ghi như vậy ở trần 30 giây trong tập đó",
    "giờ trả của phương án đó được tính bằng đúng cách tính mốc so sánh",
    "phần đã dùng chưa vượt trần",
    "khách đang chờ đón",
    "trong ba lần chạy mẫu đã kiểm",
]
for claim in must:
    if claim not in flat:
        errors.append("missing expected qualified claim " + claim)

def pct(n, d):
    return str((Decimal(n) * 100 / Decimal(d)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
arithmetic = {
    "C02_service_difference": 2434 - 2338,
    "C08_timely60_difference": 2262 - 2231,
    "C08_timely120_difference": 2327 - 2332,
    "C4A01_C_pooled_pct": pct(292, 2338),
    "C4A01_deadline_pooled_pct": pct(289, 2338),
    "C4A03_dispatch_share_pct": pct("23027.239", "31353.407"),
    "N16_C_forecast_timely60": 2338 - 10,
    "N16_pad_forecast_timely60": 2434 - 106,
    "N16_pad_forecast_timely120": 2434 - 68,
    "N06_C120_forecast_timely60": 2387 - 65,
    "N06_C120_forecast_timely120": 2387 - 8,
    "N15_audited_runs": 98 + 34,
    "N15_record_count": 1256 + 524,
}
expected = [96, 31, -5, "12.5", "12.4", "73.4", 2328, 2328, 2366, 2322, 2379, 132, 1780]
if list(arithmetic.values()) != expected:
    errors.append("arithmetic mismatch")
for value in ["0.239", "0.191"]:
    pass
questions = clean.split(r"\begin{description}", 1)[1].split(r"\end{description}", 1)[0]
if r"\ref{" in questions:
    errors.append("research question pointers were not removed")
if "Kết quả chính gộp" in clean:
    errors.append("duplicated result list retained")
result = {
    "final_source": SOURCE.name,
    "words_opening_sections_1_to_6": counts,
    "total_running_words": sum(counts),
    "budget_basis": "ROUND40: about 500 running whitespace tokens/page; no build permitted",
    "running_pages_at_500": round(sum(counts) / 500, 3),
    "labels": labels,
    "every_ref": {ref: ref_map.get(ref) for ref in refs},
    "consistency_target_files": target_labels,
    "citation_keys": cites,
    "bibliography_target": str(bibpath),
    "numeric_EV_blocks": numeric_paragraphs,
    "EV_lines": len(re.findall(r"^% EV:", text, re.M)),
    "arithmetic": arithmetic,
    "figures": clean.count(r"\begin{figure}"),
    "tables": clean.count(r"\begin{table}"),
    "body_number_tokens": sorted(set(re.findall(r"(?<![A-Za-z])\d[\d.,:/-]*", prose(clean)))),
    "errors": errors,
    "not_checked": "No compilation/render; page estimate includes separately estimated floats in LOG. Raw simulations were not rerun.",
}
with OUTPUT.open("x", encoding="utf-8", newline="\n") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({key: result[key] for key in ["final_source", "words_opening_sections_1_to_6", "total_running_words", "running_pages_at_500", "numeric_EV_blocks", "errors"]}, ensure_ascii=False))
raise SystemExit(bool(errors))
