import pickle, statistics as st

def pct(xs,q):
    if not xs: return 0
    xs=sorted(xs); k=(len(xs)-1)*q/100.0; f=int(k)
    return xs[f] if f+1>=len(xs) else xs[f]+(xs[f+1]-xs[f])*(k-f)

all_=pickle.load(open("b1_paths.pkl","rb"))

# ---------- Q1: WHEN does decision-induced burden occur? ----------
# phase proxy: at publication time t, rider is pre-pickup if t < pickupEta_published_at_that_time
tot_pre=tot_post=0; pubs_pre=pubs_post=0
# ---------- Q3: burden vs exposure ----------
rows=[]   # (exposure_ms, burdenA_drop, exog_drop, npub)
# ---------- Q2: publication-policy counterfactual ----------
def tv(seq):  # total variation
    return sum(abs(seq[i]-seq[i-1]) for i in range(1,len(seq)))
def thresholded(times, vals, theta):
    """customer-held path if we only republish when |proposed - held| >= theta"""
    held=vals[0]; out=[held]
    for v in vals[1:]:
        if abs(v-held)>=theta:
            held=v; out.append(held)
    return out
TH=[0,1000,5000,15000,30000,60000,120000,300000]
tv_by_theta={t:0 for t in TH}
npub_by_theta={t:0 for t in TH}
endpoint=0
tvA=0  # sum of decisionDelta
tvE=0
n_riders=0
for cell,riders in all_.items():
    for rid,seq in riders.items():
        seq=sorted(seq,key=lambda r:(r[0],))
        n_riders+=1
        times=[r[0] for r in seq]; drop=[r[2] for r in seq]; pick=[r[1] for r in seq]
        expo=times[-1]-times[0]
        bA=sum(r[3] for r in seq); bE=sum(r[4] for r in seq)
        rows.append((expo,bA,bE,len(seq)))
        tvA+=bA; tvE+=bE
        endpoint+=abs(drop[-1]-drop[0])
        for th in TH:
            p=thresholded(times,drop,th)
            tv_by_theta[th]+=tv(p); npub_by_theta[th]+=len(p)
        for r in seq:
            t=r[0]; pk=r[1]
            if t<pk: tot_pre+=r[3]; pubs_pre+=1
            else:    tot_post+=r[3]; pubs_post+=1

print("=== Q1. WHEN is decision-induced drop-ETA burden charged (B1, 20 cells) ===")
print(f"riders={n_riders}  total charged A(drop) = {tvA/1000:,.0f} s")
print(f"  before own pickup   : {tot_pre/1000:>10,.1f} s  ({100*tot_pre/max(1,tot_pre+tot_post):.1f}%)  over {pubs_pre:,} publications")
print(f"  after boarding      : {tot_post/1000:>10,.1f} s  ({100*tot_post/max(1,tot_pre+tot_post):.1f}%)  over {pubs_post:,} publications")

print()
print("=== Q2. Publication policy counterfactual (routes UNCHANGED, only what we TELL the rider) ===")
print("  theta = republish drop-ETA only when it differs from the held value by >= theta")
base=tv_by_theta[0]
print(f"  {'theta':>8} {'visible TV (s)':>16} {'vs theta=0':>11} {'publications':>13} {'pub/rider':>10}")
for th in TH:
    print(f"  {th/1000:>6.0f}s {tv_by_theta[th]/1000:>15,.0f} {100*tv_by_theta[th]/base:>10.1f}% {npub_by_theta[th]:>13,} {npub_by_theta[th]/n_riders:>10.1f}")
print(f"  two-endpoint |last-first| = {endpoint/1000:,.0f} s  ({100*endpoint/base:.1f}% of theta=0 chain)")

print()
print("=== Q3. Burden vs exposure (does burden scale with time-in-system?) ===")
rows.sort()
q=[0,20,40,60,80,100]
n=len(rows)
print(f"  {'exposure quintile':>20} {'n':>5} {'median expo(s)':>15} {'mean A(s)':>11} {'mean d(s)':>11} {'A per min expo':>15}")
for i in range(5):
    lo=int(n*i/5); hi=int(n*(i+1)/5)
    ch=rows[lo:hi]
    me=st.median([r[0] for r in ch])/1000
    ma=sum(r[1] for r in ch)/len(ch)/1000
    md=sum(r[2] for r in ch)/len(ch)/1000
    rate=ma/(me/60) if me>0 else 0
    print(f"  {i+1:>20} {len(ch):>5} {me:>15,.0f} {ma:>11,.1f} {md:>11,.1f} {rate:>15,.2f}")
