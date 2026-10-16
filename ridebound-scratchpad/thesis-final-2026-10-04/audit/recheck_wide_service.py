"""Verify both pickup-window service ladders from recorded run summaries."""
from pathlib import Path
import csv, json
HERE=Path(__file__).resolve().parent
CELLS=[f'd201811{d}-s10-r{r}' for d in (14,15,16,17,18) for r in (1,2,3,4)]
base=Path(r'E:\RideBoundData')
rows=[]
for window in (600,900):
    for arm in ['b1','nobudget','budget300','budget120','budget60','c1']:
        for cell in CELLS:
            if window==600:
                folder=base/'wp9'/'confirmatory-h6-panela-v2'/f'p-{cell}-{arm}-tight-s7' if arm in ('b1','c1') else base/'wp9'/'frontier-v1'/f'fr-{arm}-{cell}-s7'
            else:
                folder=base/'wp14'/'wide-window-v1'/f'ww-{arm}-{cell}-s7' if arm in ('b1','c1') else base/'wp14'/'surface-v1'/f'sf-{arm}-{cell}-s7'
            run=json.loads((folder/'run-00.json').read_text(encoding='utf-8'))
            assert run['status']=='succeeded' and (folder/'summary.json').exists()
            rows.append({'windowSeconds':window,'arm':arm,'cell':cell,'requests':run['semantic']['requestCount'],
                'served':len(run['semantic']['acceptedRequestIds']),'runPath':str(folder/'run-00.json')})
summary=[]
for window in (600,900):
    baseline=sum(r['served'] for r in rows if r['windowSeconds']==window and r['arm']=='b1')
    for arm in ['b1','nobudget','budget300','budget120','budget60','c1']:
        rs=[r for r in rows if r['windowSeconds']==window and r['arm']==arm]
        served=sum(r['served'] for r in rs);total=sum(r['requests'] for r in rs)
        summary.append({'windowSeconds':window,'arm':arm,'cells':len(rs),'requests':total,'served':served,'baselineServed':baseline,
            'servicePercent':100*served/total,'lossPp':100*(baseline-served)/total})
for name, data in [('service-budget-per-cell.csv',rows),('service-budget-summary.csv',summary)]:
    with (HERE/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
print(json.dumps(summary,indent=2))
