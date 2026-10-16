"""Reconstruct the H6/frontier figure data from final raw ledger checkpoints."""
import ast, collections, csv, hashlib, json, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
# Reuse only the two local read-only byte-reading helpers, without executing analysis.
tree = ast.parse((HERE/'recheck_t38.py').read_text(encoding='utf-8'))
helpers = ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef)) and (not isinstance(x,ast.FunctionDef) or x.name in ('backward_lines','final_state'))],type_ignores=[])
exec(compile(helpers,'read-only-final-checkpoint-helpers','exec'))
CELLS=[f'd201811{d}-s10-r{r}' for d in (14,15,16,17,18) for r in (1,2,3,4)]
SEALED=Path(r'E:\RideBoundData\wp9\confirmatory-h6-panela-v2')
FRONTIER=Path(r'E:\RideBoundData\wp9\frontier-v1')
ARMS=['b1','nobudget','budget300','budget120','budget60','c1','nopickuplock','freeze300','freeze600']
raw_rows=[]
for arm in ARMS:
    for cell in CELLS:
        folder=SEALED/f'p-{cell}-{arm}-tight-s7' if arm in ('b1','c1') else FRONTIER/f'fr-{arm}-{cell}-s7'
        state,fh=final_state(folder/'transcript-00.ndjson')
        run=json.loads((folder/'run-00.json').read_text(encoding='utf-8'))
        life=collections.Counter(r['lifecycle'] for r in state['requests'])
        served=life.get('completed',0)
        assert served==len(run['semantic']['acceptedRequestIds'])
        rider_moves=[]
        sums={f'{a}_{d}':0 for a in ('decisionInduced','visible','exogenous') for d in ('pickupEtaTotalMs','dropEtaTotalMs')}
        peak_drop_budget=0
        publications=0
        for history in state['commitmentLedger']:
            rider=0
            for entry in history['entries']:
                publications+=1
                for a in ('decisionInduced','visible','exogenous'):
                    for d in ('pickupEtaTotalMs','dropEtaTotalMs'):
                        sums[f'{a}_{d}']+=entry['deltas'][a][d]
                rider+=sum(entry['deltas']['decisionInduced'][d] for d in ('pickupEtaTotalMs','dropEtaTotalMs'))
                peak_drop_budget=max(peak_drop_budget,entry['budgetAfter']['dropEtaTotalMs'])
            rider_moves.append(rider)
        assert publications==run['semantic']['publicationCount']
        raw_rows.append({'arm':arm,'cell':cell,'requests':run['semantic']['requestCount'],'served':served,
            'publications':publications,'decisionMs':sums['decisionInduced_pickupEtaTotalMs']+sums['decisionInduced_dropEtaTotalMs'],
            'visibleMs':sums['visible_pickupEtaTotalMs']+sums['visible_dropEtaTotalMs'],
            'unchangedMs':sums['exogenous_pickupEtaTotalMs']+sums['exogenous_dropEtaTotalMs'],
            'worstRiderDecisionMs':max(rider_moves,default=0),'movedRiders':sum(x>0 for x in rider_moves),
            'peakDropBudgetMs':peak_drop_budget,**sums,'checkpointSha256':fh,'rawPath':str(folder/'transcript-00.ndjson')})
    print(arm,'20/20 verified',flush=True)
merged=[]
for a in ARMS:
    rs=[r for r in raw_rows if r['arm']==a]
    row={'arm':a,'cells':len(rs),'requests':sum(r['requests'] for r in rs),'served':sum(r['served'] for r in rs),
        'publications':sum(r['publications'] for r in rs),'decisionMs':sum(r['decisionMs'] for r in rs),
        'visibleMs':sum(r['visibleMs'] for r in rs),'unchangedMs':sum(r['unchangedMs'] for r in rs),
        'worstRiderDecisionMs':max(r['worstRiderDecisionMs'] for r in rs),'movedRiders':sum(r['movedRiders'] for r in rs),
        'peakDropBudgetMs':max(r['peakDropBudgetMs'] for r in rs)}
    row['servicePercent']=100*row['served']/row['requests'];row['ratioDecisionVisiblePercent']=100*row['decisionMs']/row['visibleMs']
    merged.append(row)
for filename,rows in [('h6-frontier-per-cell-figure-data.csv',raw_rows),('h6-frontier-summary-figure-data.csv',merged)]:
    with (HERE/filename).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(HERE/'h6-frontier-recheck.json').write_text(json.dumps({'arms':merged,'runs':raw_rows},indent=1),encoding='utf-8')
print(json.dumps(merged,indent=2),flush=True)
