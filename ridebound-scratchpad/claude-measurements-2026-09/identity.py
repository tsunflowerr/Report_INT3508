import base64,json,os,collections
def pctl(xs,q):
    if not xs: return 0
    xs=sorted(xs); k=(len(xs)-1)*q/100.0; f=int(k)
    return xs[f] if f+1>=len(xs) else xs[f]+(xs[f+1]-xs[f])*(k-f)
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7","-c1-tight-s7"):
    cells=sorted(d for d in os.listdir(root) if tag in d)
    n=0; exact=0; gaps=[]; sumA=sumD=sumB=0
    both_nonzero=0; strict_when_both=0
    for c in cells:
        with open(os.path.join(root,c,"transcript-00.ndjson"),encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    p=a["payload"]
                    A=p["decisionDelta"]["dropEtaTotalMs"]
                    d=p["exogenousDelta"]["dropEtaTotalMs"]
                    B=p["visibleDelta"]["dropEtaTotalMs"]
                    n+=1; sumA+=A; sumD+=d; sumB+=B
                    g=(A+d)-B
                    if g==0: exact+=1
                    else: gaps.append(g)
                    if A>0 and d>0:
                        both_nonzero+=1
                        if g>0: strict_when_both+=1
    print(f"=== {tag} ===")
    print(f"  publications                 : {n:,}")
    print(f"  A + d == B  EXACTLY          : {exact:,}  ({100*exact/n:.4f}%)")
    print(f"  A + d >  B  (strict)         : {len(gaps):,}  ({100*len(gaps)/n:.4f}%)")
    print(f"  both A>0 and d>0             : {both_nonzero:,}  -> strict in {strict_when_both:,} ({100*strict_when_both/max(1,both_nonzero):.1f}%)")
    if gaps:
        print(f"  gap when strict (ms)         : p50={pctl(gaps,50):.0f}  p90={pctl(gaps,90):.0f}  max={max(gaps):,}  total={sum(gaps):,}")
    print(f"  totals: A={sumA:,}  d={sumD:,}  A+d={sumA+sumD:,}  B={sumB:,}  deficit={sumA+sumD-sumB:,} ({100*(sumA+sumD-sumB)/max(1,sumA+sumD):.4f}%)")
