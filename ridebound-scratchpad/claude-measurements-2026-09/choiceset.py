import base64,json,os,collections
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7","-c1-tight-s7"):
    cells=sorted(d for d in os.listdir(root) if tag in d)
    allep=0; activeep=0
    veh_all=collections.Counter(); veh_active=collections.Counter()
    active_multi_veh=0     # active epochs with >=1 vehicle having >=2 retained
    active_multi2=0        # active epochs with >=2 vehicles having >=1 non-noop
    for c in cells:
        p=os.path.join(root,c,"transcript-00.ndjson")
        with open(p,encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                acts=fr["payload"].get("actions",[])
                active=any(a["decisionType"] in ("requestAccepted","requestRejected") for a in acts)
                ev=fr["payload"].get("solver",{}).get("executionEvidence",{})
                losses=ev.get("generation",{}).get("vehicleLosses",[]) or []
                counts=[l.get("retainedCandidateCount",0) for l in losses]
                allep+=1
                for k in counts: veh_all[k]+=1
                if active:
                    activeep+=1
                    for k in counts: veh_active[k]+=1
                    if any(k>=2 for k in counts): active_multi_veh+=1
                    if sum(1 for k in counts if k>=2)>=2: active_multi2+=1
    tot_all=sum(veh_all.values()); tot_act=sum(veh_active.values())
    print(f"=== {tag} ===")
    print(f"  epochs total={allep:,}  active (accept/reject present)={activeep:,}  ({100*activeep/allep:.1f}%)")
    print(f"  vehicle-choice-sets ALL epochs   : {tot_all:,}   with exactly 1 candidate: {100*veh_all[1]/tot_all:.2f}%   >=2: {100*sum(v for k,v in veh_all.items() if k>=2)/tot_all:.2f}%")
    if tot_act:
        print(f"  vehicle-choice-sets ACTIVE epochs: {tot_act:,}   with exactly 1 candidate: {100*veh_active[1]/tot_act:.2f}%   >=2: {100*sum(v for k,v in veh_active.items() if k>=2)/tot_act:.2f}%")
        print(f"  ACTIVE epochs with >=1 vehicle having >=2 candidates: {active_multi_veh:,}/{activeep:,} = {100*active_multi_veh/activeep:.1f}%")
        print(f"  ACTIVE epochs with >=2 vehicles having >=2 candidates: {active_multi2:,}/{activeep:,} = {100*active_multi2/activeep:.1f}%")
    print(f"  candidate-count histogram (active): {dict(sorted(veh_active.items())[:8])}")
