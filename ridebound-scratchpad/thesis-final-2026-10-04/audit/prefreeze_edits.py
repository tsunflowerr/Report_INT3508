"""Normalize existing terminology and remove labels with no document reference."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parent.parent/'source'
conclusion=root/'noi-dung'/'09-chuong5.tex'
value=conclusion.read_text(encoding='utf-8').replace('episode','ô')
conclusion.write_text(value,encoding='utf-8')
files=list(root.rglob('*.tex'))
joined='\n'.join(p.read_text(encoding='utf-8') for p in files)
refs=set(re.findall(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}',joined))
removed={}
for p in files:
    original=p.read_text(encoding='utf-8')
    labs=set(re.findall(r'\\label\{([^}]+)\}',original))
    unused=sorted(labs-refs)
    updated=original
    for label in unused:
        updated=re.sub(r'(?m)^[ \t]*'+re.escape(r'\label{'+label+'}')+r'[ \t]*\n', '', updated)
        updated=updated.replace(r'\label{'+label+'}', '')
    if updated!=original:
        p.write_text(updated,encoding='utf-8')
        removed[str(p.relative_to(root))]=unused
(Path(__file__).resolve().parent/'prefreeze-label-edits.json').write_text(json.dumps(removed,ensure_ascii=False,indent=1),encoding='utf-8')
print('Removed unused labels:',sum(map(len,removed.values())))
