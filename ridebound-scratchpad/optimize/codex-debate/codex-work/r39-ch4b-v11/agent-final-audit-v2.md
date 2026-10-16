# R39 final independent audit ? v2 candidates

Verdict: PASS; no must-fix found before publication. Reviewed `candidate-v2.tex`, `candidate-CHANGES-v2.md`, `root-changes-data-v2.json` and `root-qa-v2.json` against the v10 base, R37 ?1 and R36 CHANGES-v3 ?5. Only this new report was written; candidates and existing files were untouched.

- The body applies the 30 s versus observed 29,2 s distinction, C-30-only padding scope, visible denominators, 34-scenario oracle cohort, derived ML count provenance, pooled forced-decision counts alongside separately labelled scenario means, clipping lower bound and figure-rounding correction. R36 handoff additions cover the same-eight morning riders, valid ledger at the current decision, (N) at every decision, test attempt 4, previewed 120 s calculations and the Part A filename.
- All 33 declared replacement regions match their literal old base text, reconstruct the candidate exactly, and preserve 24.392 unaffected characters after LF normalization. Four tables and one figure have unchanged content; the two affected objects only gain resize wrappers. The old log confirms 29,17484 pt and 15,8002 pt overflows; a new build remains an assembly check. The discarded hypothesis is the specific reviewer-requested sentence; there is no general page-cut pass.
- Independent checks confirm 25 ref/eqref occurrences, 21 distinct targets, no undefined target and no duplicate label in the prescribed A/Ch3/appendix set. Appendix C has a real label and content. Snow identity is already corrected in A. Attempt 4 explicitly supports one full 1.025/1.025 run dated 13/10/2026; the newer evidence appropriately supersedes R37's earlier test wording.
- The probe found all 156 explicit register IDs in EV comments in the saved register/addenda; fresh R37/R39 artifact paths exist. Each new factual passage has its local EV comment. I checked provenance existence and the application of reviewed counts, rather than claiming another fresh raw numerical extraction. Root has separately reviewed those scripts and outputs.
- CHANGES gives one old/new/evidence row for each region; its counts and reference claims match independent results. Chapter 5 v2 exists and its first development direction is the selector experiment. Remaining Ch3 test date/EV and computational-counter wording, Appendix C test history, and assembly notes are accurately handed off. The report also retains the old Ch3 terminology handoff.

Independent prose counts by section are 4.6: 345; 4.7: 1.150; 4.8: 788; 4.9: 275; 4.10: 433; 4.11: 792. Total 3.783; floats 990. The counter definition matches CHANGES. Syntax checks confirm balanced braces, properly nested environments and 26 math dollar signs.

Root's announced publication-only note adjustment changes scale decimals to Vietnamese commas; this is appropriate and does not affect this TeX audit. Publish as `09-chuong4-phanB-v11-v2.tex` and `09-chuong4-phanB-v11-CHANGES-v2.md`. No simulation, build, installation, model training or test-suite execution was performed.

## Saved read-only audit probe and output

Executed inline with the existing interpreter using `-I -B -`; the four counter helpers are loaded by AST without executing the R33 editing script. This report preserves the probe and its result without creating additional script files.

```python
from pathlib import Path
import ast,json,re
w=Path.cwd(); o=w/'r39-ch4b-v11'; k=w.parents[2]/'rewrite-2026-10'
b=(k/'drafts/09-chuong4-phanB-v10.tex').read_text(encoding='utf-8-sig'); bl=b.splitlines(keepends=True)
t=(o/'candidate-v2.tex').read_text(encoding='utf-8-sig'); c=json.loads((o/'root-changes-data-v2.json').read_text(encoding='utf-8'))
parts=[]; pos=0; chars=0
for row in c:
 assert ''.join(bl[row['first']-1:row['last']])==row['old']
 chunk=''.join(bl[pos:row['first']-1]); parts.extend((chunk,row['new'])); chars+=len(chunk); pos=max(pos,row['last'])
parts.append(''.join(bl[pos:]));chars+=len(parts[-1]);assert ''.join(parts)==t
f=lambda x: re.sub(r'(?<!\\)%[^\n]*','',x)
oldfloats=re.findall(r'\\begin\{(table|figure)\}(.*?)\\end\{\1\}',f(b),re.S)
newfloats=re.findall(r'\\begin\{(table|figure)\}(.*?)\\end\{\1\}',f(t),re.S)
for (a,ob),(z,nb) in zip(oldfloats,newfloats):
 assert a==z
 assert nb.replace('\\resizebox{\\linewidth}{!}{\n','').replace('\n}\n','\n')==ob
files=[o/'candidate-v2.tex',w/'r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex',w/'r33-ch3v4/07-chuong3-v4-v3.tex',w/'r31-ch5/11-phuluc-v2.tex']
labels=[]
for p in files:labels.extend(re.findall(r'\\label\{([^}]+)\}',f(p.read_text(encoding='utf-8-sig'))))
refs=re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',f(t));assert len(labels)==len(set(labels));assert not(set(refs)-set(labels))
mod=ast.parse((w/'r33-ch3v4/patch_and_check-v3.py').read_text(encoding='utf-8'))
funcs=[x for x in mod.body if isinstance(x,ast.FunctionDef) and x.name in ['comments_removed','brace_arg','figure_words_text','count_words']]
ns={'re':re};exec(compile(ast.Module(body=funcs,type_ignores=[]),'pure counters','exec'),ns)
sections=re.split(r'\\section\{',f(t))[1:];counts=[]
for n,s in enumerate(sections,6):
 s='\\section{'+s
 floats=re.findall(r'\\begin\{(table|figure)\}(.*?)\\end\{\1\}',s,re.S)
 prose=re.sub(r'\\begin\{(table|figure)\}.*?\\end\{\1\}','',s,flags=re.S)
 counts.append([str(n),ns['count_words'](prose),sum(ns['count_words'](z if a=='table' else ns['figure_words_text'](z)) for a,z in floats)])
qa=json.loads((o/'root-qa-v2.json').read_text(encoding='utf-8'));assert [x[1] for x in counts]==[x['prose'] for x in qa['new_counts']]
evs='\n'.join(x for x in t.splitlines() if x.startswith('% EV'))
pat=r'(?<![\w-])(?:[A-K]\d\d|N-\d\d|L1a-\d\d|X3-\d\d|C4A-\d\d|N4B-\d\d|N4B8-\d\d)(?![\w-])'
ids=set(re.findall(pat,evs));regs='\n'.join(p.read_text(encoding='utf-8-sig') for p in (k/'evidence').glob('EVIDENCE-REGISTER*.md'))
missing=sorted(ids-set(re.findall(pat,regs)));assert not missing,missing
assert (o/'agent-numbers-v1.py').is_file() and (o/'agent-numbers-v1.json').is_file() and (w/'r37-ch4b-verify/verify-numbers-v2.json').is_file()
print(json.dumps({'changes':len(c),'unchanged_chars':chars,'float_blocks':len(oldfloats),'refs':len(refs),'targets':len(set(refs)),'duplicates':0,'undefined':0,'words_prose_floats':counts,'explicit_EV_ids_found':len(ids),'missing_EV_ids':missing,'reconstructed_candidate_exact':True},ensure_ascii=False))
```

```json
{"changes":33,"unchanged_chars":24392,"float_blocks":5,"refs":25,"targets":21,"duplicates":0,"undefined":0,"words_prose_floats":[["6",345,204],["7",1150,317],["8",788,225],["9",275,244],["10",433,0],["11",792,0]],"explicit_EV_ids_found":156,"missing_EV_ids":[],"reconstructed_candidate_exact":true}
```

Second read-only syntax probe:

```python
from pathlib import Path
import re,json
p=Path.cwd()/'r39-ch4b-v11/candidate-v2.tex';t=p.read_text(encoding='utf-8-sig');t=re.sub(r'(?<!\\)%[^\n]*','',t)
stack=[]
for m in re.finditer(r'(?<!\\)[{}]',t):
 if m[0]=='{':stack.append(m.start())
 else:assert stack;stack.pop()
assert not stack
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
 if m[1]=='begin':envs.append(m[2])
 else:assert envs and envs.pop()==m[2]
assert not envs
assert len(re.findall(r'(?<!\\)\$',t))%2==0
print(json.dumps({'brace_balance':True,'environment_nesting':True,'math_dollars':len(re.findall(r'(?<!\\)\$',t))}))
```

```json
{"brace_balance":true,"environment_nesting":true,"math_dollars":26}
```
