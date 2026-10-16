import base64,json,collections
p=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2/p-d20181114-s10-r1-c1-tight-s7/transcript-00.ndjson"
lvl=collections.defaultdict(collections.Counter)
nz=collections.Counter(); tot=collections.Counter()
n=0
with open(p,encoding="utf-8") as h:
    for line in h:
        fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
        if fr.get("messageType")!="decision": continue
        ev=fr["payload"].get("solver",{}).get("executionEvidence",{})
        ob=ev.get("selection",{}).get("finalSolverDiagnostics",{}).get("objectiveBounds",[])
        if not ob: continue
        n+=1
        for o in ob:
            name=o["objectiveName"].split(":")[0]
            lvl[name][o["levelIndex"]]+=1
            tot[name]+=1
            if o.get("incumbentValue",0)!=0: nz[name]+=1
print(f"decisions with objectiveBounds: {n}")
print(f"{'objective family':<32}{'levels seen (min..max)':<26}{'count':>8}{'nonzero':>9}")
for name in sorted(lvl, key=lambda k: min(lvl[k])):
    ls=sorted(lvl[name])
    print(f"{name:<32}{str(ls[0])+'..'+str(ls[-1]):<26}{tot[name]:>8}{nz[name]:>9}")
