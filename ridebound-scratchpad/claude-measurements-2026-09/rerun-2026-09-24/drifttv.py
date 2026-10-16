import base64,json,os
root=r"E:/RideBoundData/wp14/drift-v1"
for arm in ("dr-conduct-k0","dr-conduct-k1"):
    cells=[d for d in sorted(os.listdir(root)) if d.startswith(arm+"-d")]
    riders={}
    for c in cells:
        p=os.path.join(root,c,"transcript-00.ndjson")
        if not os.path.exists(p): continue
        with open(p,encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    pl=a["payload"]; rid=(c,pl["promise"]["requestId"])
                    riders.setdefault(rid,[]).append((pl["promise"]["dropEtaMs"],
                        pl["decisionDelta"]["dropEtaTotalMs"],
                        pl["exogenousDelta"]["dropEtaTotalMs"],
                        pl["visibleDelta"]["dropEtaTotalMs"]))
    n=len(riders)
    if n==0: print(f"{arm}: khong co du lieu"); continue
    TV=E=Dp=C=X=0; nsame=0
    gateD=set(); gateA=set(); gateV=set()
    for rid,s in riders.items():
        q=[x[0] for x in s]
        tv=sum(abs(q[i]-q[i-1]) for i in range(1,len(q)))
        e=abs(q[-1]-q[0]); dp=max(0,q[-1]-q[0])
        A=sum(x[1] for x in s); Xr=sum(x[2] for x in s); Vr=sum(x[3] for x in s)
        TV+=tv; E+=e; Dp+=dp; C+=A; X+=Xr
        if dp>30000: gateD.add(rid)
        if A >30000: gateA.add(rid)
        if Vr>30000: gateV.add(rid)
    print(f"=== {arm}  ({len(cells)} o, {n} khach) ===")
    print(f"  D+={Dp/1000:>9,.0f}s  E={E/1000:>9,.0f}s  V(chuoi)={TV/1000:>9,.0f}s   C={C/1000:>9,.0f}s  X={X/1000:>9,.0f}s")
    print(f"  ti so V/E = {TV/max(1,E):.2f}")
    print(f"  Khach vuot nguong 30s theo: D+ = {len(gateD)},  A(conduct chain) = {len(gateA)},  V(visible chain) = {len(gateV)}")
    print(f"  |gateD \ gateA| = {len(gateD-gateA)},  |gateA \ gateD| = {len(gateA-gateD)}   <- neu >0 thi hai co che KHAC nhau")
