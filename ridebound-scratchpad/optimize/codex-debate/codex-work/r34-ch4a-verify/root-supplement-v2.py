"""Small read-only R34 checks: sweep scope, counted obligation groups, figure coordinates.
Creates output exclusively beside this script; no imports or writes into source trees.
"""
from pathlib import Path
import csv, json, collections, statistics

S = Path('E:/Code/Report_INT3508/ridebound-scratchpad')
D = Path(__file__).parent
lines = []
def p(value):
    lines.append(str(value))

source = S / 'tang3/sweep/sweep-jobs-2026-09-26.tsv'
with source.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
chosen = [r for r in rows if r['world'] == 'W5' and r['family'] == 'C']
p('SOURCE ' + str(source))
p('Measured-traffic C sweep subset: ' + str(len(chosen)))
assert len(chosen) == 12
assert {int(r['level']) for r in chosen} == {30,60,120,300,600,900}
for r in chosen:
    summary = Path('E:/RideBoundData/research/tier3-sweep-v1') / r['output'] / 'summary.json'
    status = json.loads(summary.read_text(encoding='utf-8'))['status']
    assert status == 'pass' and r['audit'] == 'ok' and r['state'] == 'status-pass'
    p(f"C4A-08 {r['arm']} {r['cell']} requests={r['requests']} status={status} source={summary}")

source = D / 'main-obligations-v4.tsv'
with source.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == 170
p('\nSOURCE ' + str(source))
for w in ('w07','w08','w17'):
    rr = [r for r in rows if r['arm'] == 'Mplus-30' and r['cell'].endswith(w)]
    breach = sum(int(r['promise_breach']) for r in rr)
    served = sum(int(r['served']) for r in rr)
    forced = sum(int(r['forced']) for r in rr)
    acked = sum(int(r['acked']) for r in rr)
    p(f'Mplus-30 {w}: scenarios={len(rr)} breach={breach}/{served} forced={forced}/{acked} '
      f'own_mean={100*statistics.mean(int(r["promise_breach"])/int(r["served"]) for r in rr):.8f}% '
      f'forced_mean={100*statistics.mean(int(r["forced"])/int(r["acked"]) for r in rr):.8f}%')

p('\nHand example: 10/100=10%; (5/10+5/90)/2=' + str(100*(5/10+5/90)/2) + '%')
p('Morning C60 figure: x=(661-658)*0.36=' + str((661-658)*.36) + '; y=47*0.05=' + str(47*.05))
p('C30-to-C120 timely60 differences fixed/morning/main: '
  + str((1563-23)-(1534-0)) + '/' + str((666-51)-(660-47)) + '/' + str((2387-132)-(2338-76)))
with (D / 'root-supplement-output-v2.txt').open('x', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(lines)+'\n')
print('\n'.join(lines))
