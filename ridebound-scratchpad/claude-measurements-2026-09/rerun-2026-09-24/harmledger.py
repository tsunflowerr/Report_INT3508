import base64,json,os
# h_t = max(0, |p_t - p0| - |e_t - p0|); since p-e>0 in 479/479 (signcheck), e = p - A exactly
for root,tag in ((r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2","-b1-tight-s7"),
                 (r"E:/RideBoundData/wp14/drift-v1","dr-conduct-k1")):
    p0={}; sumA=0; sumH=0; n=0; diff=0; riders_h=set(); riders_a=set()
    for c in sorted(d for d in os.listdir(root) if tag in d):
        f=os.path.join(root,c,"transcript-00.ndjson")
        if not os.path.exists(f): continue
        with open(f,encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    pl=a["payload"]; rid=(c,pl["promise"]["requestId"]); p=pl["promise"]["dropEtaMs"]
                    A=pl["decisionDelta"]["dropEtaTotalMs"]
                    if rid not in p0: p0[rid]=p; continue
                    if A==0: continue
                    e=p-A; q=p0[rid]
                    hh=max(0,abs(p-q)-abs(e-q))
                    n+=1; sumA+=A; sumH+=hh
                    if hh!=A: diff+=1
                    if A>0: riders_a.add(rid)
                    if hh>0: riders_h.add(rid)
    print(f"=== {tag} ===  cong bo co A>0: {n}")
    print(f"   Tong A (so cai hanh vi hien tai)      = {sumA/1000:>10,.1f} s   khach bi tinh: {len(riders_a)}")
    print(f"   Tong h (so cai chi-tinh-phan-gay-hai) = {sumH/1000:>10,.1f} s   khach bi tinh: {len(riders_h)}")
    print(f"   so lan cong bo ma h khac A            = {diff}  ({100*diff/max(1,n):.1f}%)   chenh tong = {(sumA-sumH)/1000:,.1f} s ({100*(sumA-sumH)/max(1,sumA):.2f}%)")
