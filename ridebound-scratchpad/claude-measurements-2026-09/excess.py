import base64,json,os,collections
def pctl(xs,q):
    if not xs: return 0
    xs=sorted(xs); k=(len(xs)-1)*q/100.0; f=int(k)
    return xs[f] if f+1>=len(xs) else xs[f]+(xs[f+1]-xs[f])*(k-f)
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
cells=sorted(d for d in os.listdir(root) if "-c1-tight-s7" in d)
struct_dumped=False
excess=[]          # per pruned candidate: max over witnesses of (after - limit)
after_vals=[]
bycode=collections.Counter()
npruned=0; ncommit=0
for c in cells:
    p=os.path.join(root,c,"transcript-00.ndjson")
    with open(p,encoding="utf-8") as h:
        for line in h:
            fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if fr.get("messageType")!="decision": continue
            ev=fr["payload"].get("solver",{}).get("executionEvidence",{})
            for pc in ev.get("prunedCandidates",[]) or []:
                npruned+=1
                w=pc.get("commitmentWitnesses")
                if not w: continue
                ncommit+=1
                if not struct_dumped:
                    struct_dumped=True
                    print("### sample prunedCandidate with commitmentWitnesses:")
                    print(json.dumps(pc,ensure_ascii=False,indent=1)[:1600]); print()
                best=None
                for ww in w:
                    bycode[ww.get("code") or ww.get("reasonCode") or "?"]+=1
                    lim=ww.get("limit"); aft=ww.get("after")
                    if lim is None or aft is None: continue
                    e=aft-lim
                    if best is None or e<best: best=e   # smallest violation = how close it was
                if best is not None:
                    excess.append(best); after_vals.append(aft)
print(f"pruned candidates total={npruned:,}   with commitment witnesses={ncommit:,}")
print("witness codes:", dict(bycode))
if excess:
    print(f"\n=== How far OVER the 30 s cap were the vetoed candidates? (n={len(excess)}) ===")
    for q in (5,10,25,50,75,90,95,99):
        print(f"  p{q:<3}= {pctl(excess,q)/1000:>9,.1f} s")
    print(f"  max = {max(excess)/1000:,.1f} s   min = {min(excess)/1000:,.1f} s")
    for t in (1000,5000,15000,30000,60000,120000,300000):
        n=sum(1 for e in excess if e<=t)
        print(f"  would pass if the cap were raised by <= {t//1000:>3}s : {n:>5}/{len(excess)} = {100*n/len(excess):>5.1f}%")
