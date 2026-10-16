from pathlib import Path
import csv,collections,json
OUT=Path(__file__).resolve().parent
p=OUT/'data-inventory-experiment-classification-final-2026-10-08.tsv'
with p.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
for r in rows:
    if r['experiment']=='E:/RideBoundData/wp14r/development-v6-ledger':
        r['debate_use']='partially used'
        r['usage_basis']='Round9 independently decoded five-arm80-run cap ladder, not the entire ten-arm160-run archive.'
        r['what_saved_data_answers']='Five additional16-cell controls (freeze300,freeze300ratchet,freeze600,nopickuplock,ratchet) already support alternative-constraint versus budget reanalysis; their new effects are not assumed.'
    elif r['experiment'] in ('C:/RideBoundData/research/tier3-t38-v1','C:/RideBoundData/research/tier3-forecast-v1'):
        r['debate_use']='partially used'
        r['usage_basis']='Prior debate used paired policy/forecast subsets; retained controls/copies are not all independent new evidence.'
    elif r['experiment'] in ('C:/RideBoundData/research/tier3-w07-v1','C:/RideBoundData/research/tier3-w07x-v1'):
        r['debate_use']='partially used (reports cited)'
    elif r['experiment']=='E:/RideBoundData/wp9/confirmatory-h6-panela-v2':
        r['debate_use']='partially used'
        r['usage_basis']='Round7 primary40 B1/C1 records plus15 robustness/unbounded records; C2loose5 records were not included in that independent parse.'
with (OUT/'data-inventory-experiment-classification-final-v2-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'families':len(rows),'classifications':dict(collections.Counter(r['debate_use'] for r in rows))},indent=2))
