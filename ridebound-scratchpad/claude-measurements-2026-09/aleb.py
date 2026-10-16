import base64,json,os
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7","-c1-tight-s7"):
    n=0; agtb=0; aeqb=0; altb=0; worst=0; ex=[]
    for c in sorted(d for d in os.listdir(root) if tag in d):
        with open(os.path.join(root,c,"transcript-00.ndjson"),encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    p=a["payload"]
                    A=p["decisionDelta"]["dropEtaTotalMs"]
                    B=p["visibleDelta"]["dropEtaTotalMs"]
                    n+=1
                    if A>B:
                        agtb+=1; worst=max(worst,A-B)
                        if len(ex)<5: ex.append((A,B,p["exogenousDelta"]["dropEtaTotalMs"]))
                    elif A==B: aeqb+=1
                    else: altb+=1
    print(f"=== {tag} ===  publications={n:,}")
    print(f"   A <  B : {altb:>7,}  ({100*altb/n:6.3f}%)")
    print(f"   A == B : {aeqb:>7,}  ({100*aeqb/n:6.3f}%)")
    print(f"   A >  B : {agtb:>7,}  ({100*agtb/n:6.3f}%)   <-- VI PHAM A<=B")
    if agtb: print(f"   max (A-B) = {worst:,} ms   vi du (A,B,d) = {ex}")
