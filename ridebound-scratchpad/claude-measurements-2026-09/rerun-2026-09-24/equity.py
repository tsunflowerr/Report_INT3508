import base64,json,os
def pctl(xs,q):
    xs=sorted(xs); k=(len(xs)-1)*q/100.0; f=int(k)
    return xs[f] if f+1>=len(xs) else xs[f]+(xs[f+1]-xs[f])*(k-f)
def gini(x):
    x=sorted(x); n=len(x); s=sum(x)
    if s==0: return 0.0
    return (2*sum((i+1)*v for i,v in enumerate(x)))/(n*s) - (n+1)/n
def cvar(x,q):
    x=sorted(x,reverse=True); k=max(1,int(round(len(x)*(1-q))))
    return sum(x[:k])/k
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
out={}
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
                    r=riders.setdefault(rid,[0,0,[]])
                    r[0]+=p["decisionDelta"]["dropEtaTotalMs"]
                    r[1]+=p["visibleDelta"]["dropEtaTotalMs"]
                    r[2].append(p["promise"]["dropEtaMs"])
    A=[v[0]/1000 for v in riders.values()]; V=[v[1]/1000 for v in riders.values()]
    n=len(A); tot=sum(A)
    Ap=sorted(A,reverse=True)
    out[tag]=dict(n=n,A=A,V=V)
    print(f"=== {tag}  n={n} ===")
    print(f"  A_r (ganh nang do nha xe, giay/khach)")
    print(f"    tong={tot:,.0f}  trung binh={tot/n:.1f}  so khach = 0 : {sum(1 for a in A if a==0)} ({100*sum(1 for a in A if a==0)/n:.1f}%)")
    print(f"    p50={pctl(A,50):.1f} p90={pctl(A,90):.1f} p95={pctl(A,95):.1f} p99={pctl(A,99):.1f} max={max(A):.1f}")
    print(f"    Gini (ca dan so, ke ca so 0)        = {gini(A):.4f}")
    nz=[a for a in A if a>0]
    print(f"    Gini (chi nhom bi anh huong, n={len(nz)}) = {gini(nz):.4f}" if nz else "    (khong ai bi anh huong)")
    print(f"    CVaR_95 (trung binh 5% te nhat)     = {cvar(A,0.95):.1f} s")
    print(f"    CVaR_99                             = {cvar(A,0.99):.1f} s")
    for k in (0.01,0.05,0.10,0.20):
        m=int(n*k); print(f"    top {100*k:>4.0f}% khach ({m:>4}) ganh {100*sum(Ap[:m])/tot:>5.1f}% tong" if tot>0 else "")
    print(f"  V_r (khach nhin thay, giay/khach): p50={pctl(V,50):.1f} p90={pctl(V,90):.1f} p99={pctl(V,99):.1f} max={max(V):.1f}")
import pickle; pickle.dump(out,open("equity.pkl","wb"))
