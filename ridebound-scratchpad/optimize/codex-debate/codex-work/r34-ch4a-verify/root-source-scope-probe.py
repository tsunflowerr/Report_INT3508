"""R34 read-only source/scope probe. Output is exclusively created beside this script.
No imports from the simulation, no build, and no external writes.
"""
from pathlib import Path
import re

SCR = Path('E:/Code/Report_INT3508/ridebound-scratchpad')
SRC = Path('C:/Code/RideBound-noworse/src')
KIT = SCR / 'rewrite-2026-10'
OUT = Path(__file__).with_name('root-source-scope-output.txt')
items = [
    (SRC / 'RideBound.Runner/Protocol/RunnerSession.cs', [(1012, 1027), (1090, 1108)]),
    (SRC / 'RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs', [(244, 301)]),
    (SRC / 'RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs', [(443, 463)]),
    (KIT / 'drafts/07-chuong3-v3.tex', [(353, 381), (682, 722)]),
    (KIT / 'drafts/08-chuong4-phanA-v4.tex', [(106, 109), (302, 305), (327, 332), (440, 446), (546, 549)]),
]
out = ['R34 root source/scope probe; all source inputs read-only.']
for path, ranges in items:
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    out.append('\nSOURCE ' + str(path))
    for low, high in ranges:
        for index in range(low - 1, min(high, len(lines))):
            out.append(f'{index+1}: {lines[index]}')

a = KIT / 'drafts/08-chuong4-phanA-v4.tex'
body = '\n'.join(line.split('%', 1)[0] if '%' in line and '\\%' not in line else line
                 for line in a.read_text(encoding='utf-8-sig').splitlines()
                 if not line.lstrip().startswith('%'))
out.append('\nBODY WORD SCAN (comments excluded):')
for term in ('niêm phong', 'tiền đăng ký', 'dự đoán trước', 'kết quả mong đợi',
             'duy nhất', 'đầu tiên', 'vượt trội', 'tối ưu', 'đột phá', 'chúng tôi',
             'phải phục hồi', 'không dùng trong khóa luận'):
    matches = [str(i) for i, line in enumerate(a.read_text(encoding='utf-8-sig').splitlines(), 1)
               if not line.lstrip().startswith('%') and term.casefold() in line.casefold()]
    out.append(f'{term}: {", ".join(matches) or "NONE"}')
out.append('\nSYNTAX INVENTORY (read-only, not a compile):')
for token in ('table', 'tabular', 'figure', 'tikzpicture', 'scope'):
    out.append(f'{token}: begin={body.count(chr(92)+"begin{"+token+"}")} '
               f'end={body.count(chr(92)+"end{"+token+"}")}')
labels = re.findall(r'\\label\{([^}]+)\}', body)
out.append('duplicate labels in A: ' + repr(sorted({label for label in labels if labels.count(label) > 1})))
with OUT.open('x', encoding='utf-8', newline='\n') as file:
    file.write('\n'.join(out) + '\n')
print(str(OUT))
