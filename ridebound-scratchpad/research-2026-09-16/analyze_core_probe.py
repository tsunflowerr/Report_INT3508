import json,itertools
from pathlib import Path
root=Path(__file__).parent
data=json.loads((root/'core-probe.json').read_text())
counts={k:0 for k in ['fixtures','multiple','different_future_counts','equal_usage_different_future','equal_usage_cost_different_future','cost_min_loses_future','equal_usage_vectors_different_future']}
witnesses={k:[] for k in counts if k not in ['fixtures','multiple']}
for fixture in data['results']:
 rows=fixture['rows']; counts['fixtures']+=1
 if len(rows)<2: continue
 counts['multiple']+=1
 found={k:None for k in witnesses}
 for a,b in itertools.combinations(rows,2):
  if a['futureFeasibleCount']==b['futureFeasibleCount']: continue
  pair={'budget':fixture['budget'],'currentRequest':fixture['currentRequest'],'a':a,'b':b}
  found['different_future_counts']=pair
  if a['etaUsageTotal']==b['etaUsageTotal']:
   found['equal_usage_different_future']=pair
   if a['cost']==b['cost']: found['equal_usage_cost_different_future']=pair
  if a['usage']==b['usage']: found['equal_usage_vectors_different_future']=pair
 mincost=min(r['cost'] for r in rows); best=max(r['futureFeasibleCount'] for r in rows)
 cheap=[r for r in rows if r['cost']==mincost]
 if max(r['futureFeasibleCount'] for r in cheap)<best:
  found['cost_min_loses_future']={'budget':fixture['budget'],'currentRequest':fixture['currentRequest'],'a':cheap[0],'b':max(rows,key=lambda r:r['futureFeasibleCount'])}
 for key,pair in found.items():
  if pair:
   counts[key]+=1
   if len(witnesses[key])<3: witnesses[key].append(pair)
out={'counts':counts,'witnesses':witnesses}
(root/'core-probe-analysis.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(counts,indent=2))
for key in ['equal_usage_vectors_different_future','equal_usage_cost_different_future','cost_min_loses_future']:
 print(key,json.dumps(witnesses[key][:1],ensure_ascii=False))
