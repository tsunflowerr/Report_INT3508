import pickle
def pctl(xs,q):
    xs=sorted(xs); k=(len(xs)-1)*q/100.0; f=int(k)
    return xs[f] if f+1>=len(xs) else xs[f]+(xs[f+1]-xs[f])*(k-f)
import base64,json,os
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7","-c1-tight-s7"):
    riders={}
    for c in sorted(d for d in os.listdir(root) if tag in d):
        with open(os.path.join(root,c,"transcript-00.ndjson"),encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    p=a["payload"]; rid=(c,p["promise"]["requestId"])
                    riders.setdefault(rid,[]).append((p["promise"]["dropEtaMs"],
                        p["decisionDelta"]["dropEtaTotalMs"], p["exogenousDelta"]["dropEtaTotalMs"]))
    TV=E=Dp=C=X=0; Hs=[]; TVr=[]
    for rid,seq in riders.items():
        q=[s[0] for s in seq]
        tv=sum(abs(q[i]-q[i-1]) for i in range(1,len(q)))
        e=abs(q[-1]-q[0]); dp=max(0,q[-1]-q[0])
        TV+=tv; E+=e; Dp+=dp; Hs.append(tv-e); TVr.append(tv)
        C+=sum(s[1] for s in seq); X+=sum(s[2] for s in seq)
    n=len(riders)
    print(f"=== {tag}  ({n} khach) ===")
    print(f"  D+ (chi phan muon, hai dau) = {Dp/1000:>10,.0f} s")
    print(f"  E  (hai dau, tri tuyet doi) = {E/1000:>10,.0f} s")
    print(f"  V=TV (ca chuoi, khach thay) = {TV/1000:>10,.0f} s")
    print(f"  C  (conduct, ca chuoi)      = {C/1000:>10,.0f} s   <- cai ma beta CHAN")
    print(f"  X  (exogenous, ca chuoi)    = {X/1000:>10,.0f} s")
    print(f"  kiem tra D+ <= E <= V       : {Dp<=E<=TV}      V <= C+X: {TV<=C+X}")
    print(f"  H = V - E                   = {(TV-E)/1000:>10,.0f} s   ({100*(TV-E)/max(1,TV):.1f}% cua V)")
    print(f"  H so voi X                  : H/X = {(TV-E)/max(1,X):.3f}")
    print(f"  V moi khach (s): p50={pctl(TVr,50)/1000:.1f} p90={pctl(TVr,90)/1000:.1f} p99={pctl(TVr,99)/1000:.1f} max={max(TVr)/1000:.1f}")
    print(f"  so khach co V > 30s         : {sum(1 for v in TVr if v>30000)}/{n}  ({100*sum(1 for v in TVr if v>30000)/n:.1f}%)")
