"""Root review of delegated saved arithmetic. Creates only exclusive small text output."""
from pathlib import Path
import collections, csv, json
D = Path(__file__).parent
out = []
def p(x): out.append(str(x))
def records(name):
    rr = []
    for n, line in enumerate((D/name).read_text(encoding='utf-8-sig').splitlines(), 1):
        if line.startswith('{'):
            rr.append((n, json.loads(line)))
    return rr

fixed = [(n,r) for n,r in records('extra-probe-output-v2.txt') if r.get('group')=='fixed']
assert len(fixed)==80 and len({r['source'] for n,r in fixed})==80
arms = ('b1-ref','c1-nobudget','c1-budget120','c1-budget60','c1-h6ref')
expected = [(1629,865,388),(1584,346,62),(1563,303,41),(1540,266,20),(1534,241,6)]
for arm, exp in zip(arms, expected):
    rr = [(n,r) for n,r in fixed if r['arm']==arm]
    assert len(rr)==16
    totals = tuple(sum(r[k] for n,r in rr) for k in ('served','shared','moved'))
    assert totals==exp and sum(r['requests'] for n,r in rr)==1728
    p(f'FIXED {arm}: served/shared/moved={totals}; raw output lines {rr[0][0]}..{rr[-1][0]} AGREE')

extra = records('extra-probe-output-v3.txt')
ladder = {'U':(665,50,615,656),'C-30':(660,47,613,658),'C-60':(661,47,614,659),
          'C-90':(664,50,614,660),'C-120':(666,51,615,659),'C-150':(666,51,615,659),
          'C-180':(666,51,615,659),'C-240':(665,50,615,656),'C-300':(665,50,615,656)}
for arm, exp in ladder.items():
    rr = [(n,r) for n,r in extra if r.get('group')=='morning' and r['arm']==arm]
    assert len(rr)==8 and len({r['source'] for n,r in rr})==8
    total = tuple(sum(r[k] for n,r in rr) for k in ('served','late60','timely60','timely120'))
    assert total==exp and sum(r['requests'] for n,r in rr)==864
    nn, aggregate = next((n,r) for n,r in extra if r.get('group')=='morning-total' and r['arm']==arm)
    assert tuple(aggregate[k] for k in ('served','late60','timely60','timely120'))==total
    p(f'MORNING {arm}: served/late60/timely60/timely120={total}; aggregate line {nn} AGREE')
rr = [r for n,r in extra if r.get('group')=='snow']
assert len(rr)==8 and len({r['source'] for r in rr})==8
assert sum(r['requests'] for r in rr)==864 and sum(r['served'] for r in rr)==601
p('SNOW: independent sum of 8 per-run request counts 864; served 601 AGREE')
nn, archive = next((n,r) for n,r in extra if r.get('group')=='morning-archive')
assert (archive['archived'],archive['chosen'])==(192,136)
assert len(archive['chosen_arms'])==17 and set(archive['chosen_arms'].values())=={8}
p(f'ARCHIVE: 136 of 192; 17 arms x 8; output line {nn} AGREE')
nn, budget = next((n,r) for n,r in extra if r.get('group')=='budget-rejection')
assert budget['counts']=={'has-record:completed':116,'has-record:rejected':32,
                         'no-record:completed':111,'no-record:rejected':1075}
p(f'D13: no-record 1186 = 111+1075; recorded 148=116+32; output line {nn} AGREE')

with (D/'main-obligations-v4.tsv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==170
for arm, expected in [('C-30',(2338,292,76,11,3,0,20101)),
                      ('Mplus-30',(2338,289,74,11,3,7710,20103)),
                      ('Mplus-60',(2347,302,79,11,3,4031,20163)),
                      ('V-30',(2336,289,74,11,3,10442,20090)),
                      ('U',(2434,428,203,102,7,0,20760))]:
    rr=[r for r in rows if r['arm']==arm]
    assert len(rr)==34
    total=tuple(sum(int(r[k]) for r in rr) for k in ('served','late30','late60','late120','early60','forced','acked'))
    assert total==expected
    p(f'MAIN {arm}: served/late30/late60/late120/early60/forced/acked={total} AGREE')
for n,line in enumerate((D/'main-numbers-v4.txt').read_text(encoding='utf-8-sig').splitlines(),1):
    if line.startswith(('RAW_TOTAL','WORST U:','WORST C-30:','N11','CHECK all')):
        p(f'main-numbers-v4.txt:{n}: {line}')
with (D/'root-numeric-crosscheck-output-v2.txt').open('x',encoding='utf-8',newline='\n') as f:
    f.write('\n'.join(out)+'\n')
print('\n'.join(out))
