import pickle
all_=pickle.load(open("b1_paths.pkl","rb"))
R=[]
for cell,riders in all_.items():
    for rid,seq in riders.items():
        seq=sorted(seq,key=lambda r:r[0])
        t0=seq[0][0]; drop0=seq[0][2]; pick0=seq[0][1]
        planned=drop0-t0                 # KNOWN AT BOOKING: promised total trip duration
        planned_wait=pick0-t0            # KNOWN AT BOOKING: promised wait
        A=sum(r[3] for r in seq); E=sum(r[4] for r in seq)
        expo=seq[-1][0]-t0
        R.append(dict(A=A,E=E,expo=expo,planned=planned,wait=planned_wait))
n=len(R); TOT=sum(r["A"] for r in R)
print(f"riders={n}  total A(drop)={TOT/1000:,.0f}s   mean={TOT/n/1000:.1f}s")

print("\n=== Is exposure PREDICTABLE at booking? (correlation of planned duration with realised burden) ===")
import math
def corr(a,b):
    ma=sum(a)/len(a); mb=sum(b)/len(b)
    na=sum((x-ma)**2 for x in a); nb=sum((x-mb)**2 for x in b)
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/math.sqrt(na*nb)
print(f"  corr(planned duration, realised exposure) = {corr([r['planned'] for r in R],[r['expo'] for r in R]):.3f}")
print(f"  corr(planned duration, charged A)         = {corr([r['planned'] for r in R],[r['A'] for r in R]):.3f}")
print(f"  corr(planned wait,     charged A)         = {corr([r['wait'] for r in R],[r['A'] for r in R]):.3f}")

print("\n=== Budget allocation efficiency: how many riders does a fixed TOTAL allowance keep un-gated? ===")
print("   (descriptive on the B1 trajectory: hypothesis-generating, NOT a service-rate estimate)")
for beta in (30000,60000,120000,300000):
    pool = beta*n
    viol_uni = sum(1 for r in R if r["A"]>beta)
    # (a) proportional to planned trip duration, same pool
    sp = sum(r["planned"] for r in R)
    viol_prop = sum(1 for r in R if r["A"] > pool*r["planned"]/sp)
    # (b) greedy water-filling upper bound: cover cheapest riders first
    costs=sorted(r["A"] for r in R); acc=0; covered=0
    for c in costs:
        if acc+c<=pool: acc+=c; covered+=1
        else: break
    viol_opt = n-covered
    # (c) how much of the uniform pool is actually usable
    used = sum(min(r["A"],beta) for r in R)
    print(f"  beta={beta//1000:>3}s pool={pool/1000:>8,.0f}s | over-cap riders: uniform {viol_uni:>4}"
          f" | prop-to-duration {viol_prop:>4} | best-possible {viol_opt:>4}"
          f" | pool actually consumed {100*used/pool:>5.1f}%")

print("\n=== Concentration: how much of the total burden sits in the tail? ===")
As=sorted((r["A"] for r in R),reverse=True)
for k in (10,25,50,100,200,400):
    print(f"  top {k:>4} riders ({100*k/n:>4.1f}%) carry {100*sum(As[:k])/TOT:>5.1f}% of all decision-induced burden")

print("\n=== Under a cap beta, what fraction of the tail's burden must be REFUSED? ===")
for beta in (30000,60000,120000,300000):
    excess=sum(max(0,r["A"]-beta) for r in R)
    print(f"  beta={beta//1000:>3}s : excess over cap = {excess/1000:>9,.0f}s  ({100*excess/TOT:>5.1f}% of total burden) borne by {sum(1 for r in R if r['A']>beta)} riders")
