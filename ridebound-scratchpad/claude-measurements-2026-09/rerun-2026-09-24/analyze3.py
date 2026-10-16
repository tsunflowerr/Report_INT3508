import base64,json,os,collections
def pctl(xs,q):
    if not xs: return 0
    xs=sorted(xs); k=(len(xs)-1)*q/100.0; f=int(k)
    return xs[f] if f+1>=len(xs) else xs[f]+(xs[f+1]-xs[f])*(k-f)
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
cells=sorted(d for d in os.listdir(root) if "-b1-tight-s7" in d)
moves=[]                       # individual charged move sizes (ms)
per_decision=collections.Counter()   # #riders displaced by one decision frame
per_decision_tot=[]            # total ms displaced by one decision frame
rider_moves=collections.Counter()    # #charged moves per rider
first_move_blows={30000:0,60000:0,120000:0,300000:0}
riders_with_moves=set()
for c in cells:
    p=os.path.join(root,c,"transcript-00.ndjson")
    seen_first=set()
    with open(p,encoding="utf-8") as h:
        for line in h:
            fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if fr.get("messageType")!="decision": continue
            k=0; tot=0
            for a in fr["payload"].get("actions",[]):
                if a["decisionType"]!="promisePublished": continue
                d=a["payload"]["decisionDelta"]["dropEtaTotalMs"]
                if d<=0: continue
                rid=(c,a["payload"]["promise"]["requestId"])
                moves.append(d); k+=1; tot+=d
                rider_moves[rid]+=1; riders_with_moves.add(rid)
                if rid not in seen_first:
                    seen_first.add(rid)
                    for b in first_move_blows:
                        if d>b: first_move_blows[b]+=1
            if k: per_decision[k]+=1; per_decision_tot.append(tot)

print(f"=== Individual charged drop-ETA moves (B1, 20 cells) ===")
print(f"  count = {len(moves):,}   total = {sum(moves)/1000:,.0f}s   riders touched = {len(riders_with_moves)}")
print(f"  size (s):  p10={pctl(moves,10)/1000:.1f}  p25={pctl(moves,25)/1000:.1f}  p50={pctl(moves,50)/1000:.1f}"
      f"  p75={pctl(moves,75)/1000:.1f}  p90={pctl(moves,90)/1000:.1f}  max={max(moves)/1000:.1f}")
for b in (30000,60000,120000,300000):
    n=sum(1 for m in moves if m>b)
    print(f"  moves larger than the WHOLE budget beta={b//1000:>3}s : {n:>4}/{len(moves)} = {100*n/len(moves):>5.1f}%"
          f"   | riders whose FIRST charged move alone blows beta: {first_move_blows[b]:>3}/{len(riders_with_moves)}")

print(f"\n=== Charged moves per rider ===")
h=collections.Counter(rider_moves.values())
for k in sorted(h)[:10]: print(f"  {k} move(s): {h[k]} riders")
print(f"  mean {sum(rider_moves.values())/len(rider_moves):.2f} charged moves per affected rider")

print(f"\n=== Externality footprint: how many incumbents does ONE decision displace? ===")
for k in sorted(per_decision)[:10]:
    print(f"  {k} rider(s) displaced in the same decision: {per_decision[k]} decisions")
print(f"  decisions that displace anybody: {sum(per_decision.values()):,}")
print(f"  ms displaced per such decision: p50={pctl(per_decision_tot,50)/1000:.1f}s  p90={pctl(per_decision_tot,90)/1000:.1f}s  max={max(per_decision_tot)/1000:.1f}s")
