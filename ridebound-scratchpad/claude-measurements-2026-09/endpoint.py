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
                        p["decisionDelta"]["dropEtaTotalMs"], p["visibleDelta"]["dropEtaTotalMs"]))
    n=len(riders)
    Dp=[]; Vv=[]; Aa=[]
    for rid,s in riders.items():
        q=[x[0] for x in s]
        Dp.append(max(0,q[-1]-q[0])/1000)
        Aa.append(sum(x[1] for x in s)/1000)
        Vv.append(sum(x[2] for x in s)/1000)
    print(f"=== {tag}  n={n} ===")
    print(f"  {'nguong l (s)':>12} | {'vuot D+ (endpoint)':>20} | {'vuot A (conduct chain)':>24} | {'vuot V (visible chain)':>24}")
    for l in (0,15,30,60,120,300,600,900):
        a=sum(1 for x in Dp if x>l); b=sum(1 for x in Aa if x>l); c2=sum(1 for x in Vv if x>l)
        print(f"  {l:>12} | {a:>6} ({100*a/n:>5.1f}%)       | {b:>6} ({100*b/n:>5.1f}%)           | {c2:>6} ({100*c2/n:>5.1f}%)")
