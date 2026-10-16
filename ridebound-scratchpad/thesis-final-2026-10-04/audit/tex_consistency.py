"""Check citations, cross references, display calls and typography without compiling."""
from pathlib import Path
import re, json, argparse, collections
ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('--out',required=True)
args=ap.parse_args(); source=Path(args.source)
files=list(source.rglob('*.tex')); text={str(p.relative_to(source)):p.read_text(encoding='utf-8') for p in files}
joined='\n'.join(text.values())
labels=collections.Counter(re.findall(r'\\label\{([^}]+)\}', joined))
refs=collections.Counter(re.findall(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}',joined))
cites=collections.Counter(k.strip() for block in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',joined) for k in block.split(','))
items=collections.Counter(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',joined))
displays=[]
for name,value in text.items():
    for match in re.finditer(r'\\begin\{(figure|table|longtable)\}(.*?)\\end\{\1\}',value,re.S):
        labs=re.findall(r'\\label\{([^}]+)\}',match.group(2))
        displays.append({'file':name,'type':match.group(1),'labels':labs,'called':all(refs[l]>0 for l in labs) and len(labs)>0})
result={'fileCount':len(files),'labels':len(labels),'references':sum(refs.values()),
 'missingLabels':sorted(set(refs)-set(labels)), 'duplicateLabels':[l for l,c in labels.items() if c>1],
 'unusedLabels':sorted(set(labels)-set(refs)),
 'citedKeys':sorted(cites),'bibliographyCount':len(items),
 'missingCitations':sorted(set(cites)-set(items)), 'uncitedBibliography':sorted(set(items)-set(cites)),
 'duplicateBibitems':[k for k,c in items.items() if c>1],
 'displayCalls':displays, 'unresolvedLiteralLocations':[name for name,value in text.items() if '??' in value],
 'mainTypography':{k:k in text.get('main.tex','') for k in [r'\setmainfont{Times New Roman}',r'\onehalfspacing',r'\geometry{a4paper,left=3cm,right=2cm,top=2cm,bottom=2cm}',r'\usepackage[fontsize=13pt]{fontsize}']}}
Path(args.out).write_text(json.dumps(result,indent=1,ensure_ascii=False),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
