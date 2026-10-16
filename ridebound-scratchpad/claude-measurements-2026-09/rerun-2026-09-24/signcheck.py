import base64,json,os
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7","-c1-tight-s7"):
    prev={}; n=0; pe_neg=0; pe_pos=0; amb=0; bothnz=0
    for c in sorted(d for d in os.listdir(root) if tag in d):
        with open(os.path.join(root,c,"transcript-00.ndjson"),encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    pl=a["payload"]; rid=(c,pl["promise"]["requestId"]); p=pl["promise"]["dropEtaMs"]
                    A=pl["decisionDelta"]["dropEtaTotalMs"]; d=pl["exogenousDelta"]["dropEtaTotalMs"]
                    v=prev.get(rid); prev[rid]=p
                    if v is None or A==0: continue
                    n+=1
                    z=p-v                       # signed visible change
                    if d==0:
                        s1 = 1 if z>0 else -1   # e==v, so p-e = z
                    else:
                        bothnz+=1
                        sols=[s1 for s1 in (1,-1) for s2 in (1,-1) if s1*A+s2*d==z]
                        if len(set(sols))!=1: amb+=1; continue
                        s1=sols[0]
                    if s1<0: pe_neg+=1
                    else: pe_pos+=1
    print(f"=== {tag} ===  publications with A>0 : {n}")
    print(f"   p > e (quyet dinh day MUON hon 'khong lam gi') : {pe_pos}")
    print(f"   p < e (quyet dinh keo SOM hon 'khong lam gi')  : {pe_neg}   <-- ca 'sua giu loi hua' bi conduct tinh phi")
    print(f"   khong xac dinh duoc dau                        : {amb}   (trong {bothnz} ca ca A va d khac 0)")
