# Literature extraction: three ride-pooling papers vs. "certified bounded promises"

Locations are given as **§section / Eq.(n) / printed page**. Quotes are verbatim from the supplied text files (OCR artifacts preserved; noted where they matter).

Files:
- `C:\Users\quang\AppData\Local\Temp\claude\e--Code-RideBound\855cbacc-5124-4c6f-b581-290063997737\scratchpad\papers\Unreliability_in_ridesharing_systems_Measuring_cha.txt`
- `...\Scale_analysis_for_on-demand_ridepooling_systems_a.txt`
- `...\1-s2.0-S0191261522000716-main.txt`

---

# PAPER 1 — Fielbaum & Alonso-Mora (2020), *Unreliability in ridesharing systems: Measuring changes in users' times due to new requests*, TR-C 121:102831

## 1.1 Taxonomy (this is their causal-attribution apparatus) — §2, p.4

**Definition 1. (Unreliability induced by the users)** — "Sometimes, users will not be there when vehicles arrive at their pick-up point, forcing the vehicle to wait for some (short) time, making users that are in the vehicle face a longer delay, and increasing waiting time for future users. Some previously assigned trips might now get rejected (by the system or by the user). Similar problems arise if a user cancels her trip when the vehicle is on its way."

**Definition 2. (Unreliability induced by the operators)** — "Each time the system receives a new request, it changes how it gathers several requests together, and also how it assigns requests to vehicles. Depending on the system's rules, such changes can affect routes, which in turn might increase waiting time for passengers that are not on-board yet, and delay for passengers that are on their way but that now have to pick-up a new request. Furthermore, a request that had been previously assigned may now be rejected, in order to prioritize new ones (for instance, because they are closer or they involve more users)."

**Definition 3. (One-time unreliability)** — "When a user executes a trip, the actual delay and waiting time might be different from the ones that were predicted at the beginning of the trip. … one-time unreliability refers to changes that happen within a particular execution of a travel request."

**Definition 4. (Daily unreliability)** — "…refers to changes that happen to multiple executions of the same travel request across multiple instances of the request, e.g., across multiple days."

Traffic-caused delay is **explicitly excluded by scoping, not modelled**: "In this paper we do not discuss unreliability sources that are already present in traditional public transport systems, such as congestion or accidents on the streets, or in car-sharing systems in which rides are not shared." (§2, p.3–4, with footnotes 3–4). Reinforced empirically in §5: "During the off-peak period, congestion is not a very relevant problem, i.e., traveling times are somewhat stable, which allows us to disregard unreliability due to traffic conditions, isolating the effects we are aiming to study in this paper." (p.9)

So: **operator-caused vs. user-caused attribution exists as a taxonomy; traffic-caused is scoped out. There is no in-algorithm attribution machinery.**

## 1.2 Exact metric definitions — §3, pp.4–7

Primitives (§3 bullet list, pp.4–5): request time `t_r`; origin `o_r`, destination `d_r`; real waiting time `t_w(r)` = pick-up time − request time; **first-announced waiting time `t¹_w(r)`** = "the waiting time that would be achieved if the vehicle's itinerary remains unchanged until picking the passenger up"; real in-vehicle time `t_v(r)`; real detour `t_d(r)` = `t_v(r)` − shortest-path time; first-announced `t¹_v(r)`, `t¹_d(r)` — "they would be the achieved in-vehicle time and detour if the vehicle does not change its itinerary from the first announced assignment until the passenger is dropped-off."

Delay:
- `D(r) = t_w(r) + t_d(r)` ("the difference between the real arrival time provided by the system and the arrival time achieved if traveling by private car")
- `D¹(r) = t¹_w(r) + t¹_d(r)`

Displacement (the core quantities):
- `Δt_w(r) = t_w(r) − t¹_w(r)`
- `Δt_v(r) = t_v(r) − t¹_v(r)`
- `Δt_d(r) = t_d(r) − t¹_d(r)`
- `ΔD(r) = D(r) − D¹(r)`
- Identity: "Note that Δt_d(r) = Δt_v(r), because the difference between the detour and the in-vehicle time is the shortest distance between o_r and d_r, which is fixed"

**Truncation rule (matters for any thesis re-use):** "These indices may take negative values, which imply a better performance of the system than expected. … In the remainder of the paper we consider the positive values for these indices, and truncate to zero those that are negative, to study the unreliability effects that are negative for the users." (§3, p.5)

Zone-level aggregates, with `Q(x)` = number of requests departing from zone `x`:
- **Definition 5 (Unreliability in waiting time)**, Eq.(1): `U_tw(x) = Σ_{r:o_r=x} Δt_w(r) / Q(x)`; Eq.(2)–(3) rewrite it as `U_tw(x) = E(Δt_w(r) | Δt_w(r)>0) · P(Δt_w(r)>0)`. Two causal channels named: "(i) either new passengers are assigned to v and being picked-up before r, inducing a longer vehicle's detour that increases the waiting time faced by r; or (ii) new requests yield a reassignment process that changes the assigned vehicle to another one with a longer time to arrive at the pick-up node."
- **Definition 6 (Unreliability in detour)**, Eq.(4): `U_td(x) = Σ Δt_d(r)/Q(x)`; Eq.(5): `= E(Δt_d|Δt_d>0)·P(Δt_d>0)`.
- **Definition 7 (Unreliability in delay)**, Eq.(6): `U_D(x) = Σ ΔD(r)/Q(x)`; Eq.(7): `= E(ΔD|ΔD>0)·P(Δt_d>0)` [sic — the conditioning event is mis-typeset in the source; should be `ΔD>0`]. Dominance result stated in prose: "Δt_w(r) ⩽ ΔD(r) and Δt_d(r) ⩽ ΔD(r) for each request r, which implies that P(Δt_w(r)>0) ⩽ P(ΔD(r)>0) and P(Δt_d(r)>0) ⩽ P(ΔD(r)>0). That is to say, unreliability in delay is always the largest".
- **Definition 8 (Unreliability in rejections)**, Eq.(8): `U_R(x) = |ΔRej(x)| / Q(x)`, where `ΔRej(x)` is "the set of requests that face become rejected and whose origin is in x". Definition text: "the system might decide to reject some request(s) that had been previously accepted but not picked up yet, if this rejection(s) improves the global efficiency of the system."
- **Definition 9 (Number of changes faced per request)** — **this is the closest thing in the three papers to a ratcheting counter**: "Each request r might face several changes, as assignments are updated iteratively. For each request, we compute the expected waiting time at each assignment, since the first one until it is picked-up, and count how many times this prediction increases; analogously, we count how many times a request's expected detour and delay increase, since its first assignment until it is dropped-off. They will be denoted, respectively, `NC_tw(r)`, `NC_td(r)` and `NC_D(r)`." → **It is a purely descriptive counter; it never enters a constraint or an objective.**

## 1.3 The algorithm and its control levers — §4, pp.7–8

Base method = Alonso-Mora et al. (2017) RTV/RGV, **with the promise-protection constraint deliberately removed**: "we will use the model proposed by Alonso-Mora et al. (2017) with a slight modification that is helpful to study unreliability: **we drop the requirement that waiting time for reassigned passengers can't increase**." (§4, p.7)

Feasibility (hard, per-user, absolute levels — *not* displacement): an arc `τv` exists "iff the group τ can be conducted by the vehicle v, without exceeding the capacity of the vehicle and **without violating constraints that deal with the maximum admissible waiting times and total delay**".

Cost of trip, **Eq.(9)** (§4, p.8) — the incumbent-externality term is the second sum (source OCR shows `Δpwtw`; from context it is `p_w Δt_w`):
```
c(τ, v) = Σ_{r∈τ} [ p_w t_w(r,τ,v) + p_v t_v(r,τ,v) ]
        + Σ_{r∈v} [ p_w Δt_w(r,τ,v) + p_v Δt_v(r,τ,v) ]
        + c_0 ΔL(τ,v)
```
"The first term stands for the waiting and in-vehicle time for the requests in τ … the second term represents the additional times for those requests that were already being served by v, and the third term represents the operators' costs".

→ **The externality on incumbents is a SOFT PENALTY inside a social-cost objective, aggregate over incumbents `r∈v`, with no per-user cap on the increment and no monetary transfer.** Footnote 10: "This definition of the costs entails that the system considers directly all the agents involved in the process, i.e., users and operators. For-profit companies might use slightly different cost functions depending on how they price each trip…".

Step 2 = ILP selecting arcs + rejections with "a corresponding penalization in the objective function"; step 3 = rebalancing. Reassignment policy: "we maximize the flexibility of the system by admitting any change, as long as it does not violate the bounds on waiting times and delay of every request. Furthermore, requests that have already been assigned but have not been picked-up yet might be reassigned to a different vehicle (maybe increasing their waiting times) or rejected, if that reduces the total cost of the system."

Parameters (Appendix Table 6, p.18): max admissible waiting time **5 min**; max admissible delay **10 min**; `p_v`=1; `p_w`=2; weight of rejecting a request **40**; `c_0`=1.5.

## 1.4 The freezing / commitment experiment — §6, pp.16–17 (most citable for your thesis)

> "1. **Fully controlled scenario:** When a passenger gets assigned to a vehicle, **it is marked as non-rejectable for future assignments, and her maximum waiting time is updated to the predicted one.** Note that we are still admitting for reassignments, if a different vehicle can pick her up in the same (or lower) time.
> 2. **Intermediate scenario:** Becoming rejected after being accepted might be more annoying than facing an extra waiting time. In this intermediate scenario, assigned passengers are also marked as non-rejectable, but their waiting time might increase (always bounded by the common maximum admissible waiting time)."

"These changes automatically make `U_R = 0` for both scenarios, and `U_tw = 0` for the fully controlled one."

This is a **hard, per-user, decision-time feasibility restriction** — but it is (i) a **zero-tolerance freeze** (the bound is reset to the announced value, i.e. zero remaining allowance), (ii) **waiting-time only** (detour/`Δt_d` is never frozen), (iii) applied as an **ex-post comparative experiment**, not the paper's operating algorithm.

Why detour is never frozen — footnote 13, p.17: "The same happens with total delay, but **if in-vehicle detours are not admitted, actual sharing would occur only at very specific circumstances**, when two passengers are matched in the same iteration, i.e., when their request times are very similar. In other words, eliminating U_D by these means would turn the whole system in a (almost) non-shared one."

Trade-off result, Table 5 (p.16), 2000 veh / cap 4:

| Scenario | Av. wait | Av. detour | Av. delay | Rejected | Av. users' cost |
|---|---|---|---|---|---|
| Base | 1.01 | 0.65 | 1.66 | 34.5% | 9.56 |
| Intermediate | 1.51 | 1.01 | 2.52 | 31.2% | 10.3 |
| Fully controlled | 0.77 | 0.94 | 1.71 | **45.6%** | 11.6 |

"The most relevant impact, however, is on the rejection rate, which increases dramatically due to the inflexible conditions." … "In all, looking at the last column of Table 5 is illuminating: the more controlled the unreliability, the higher the average users' costs. That is to say, there is indeed a trade-off between unreliability and the other traditional measures of quality of service. **This reinforces the need of more sophisticated ideas to control unreliability.**" (§6, p.17) ← *this sentence is the single best citation for motivating a graded, budgeted promise mechanism.*

## 1.5 Headline empirical magnitudes (Tables 1–3, pp.9–11)

Base scenario: rejection 34.5%, av. wait 1.01 min, av. detour 0.65, av. delay 1.66. Table 2: requests that become rejected 6.85%; `P(ΔD>0)`=19.2%; requests that face changes 26.1%; **first-accepted requests that face changes 36.1%**; `E(ΔD|ΔD>0)`=1.68 min; Av. `NC_D`=0.35; **Max `NC_D`=6** (up to **8** in the FR scenario). Table 3: `P(Δt_w>0)`=5.9%, `E(Δt_w|·)`=1.22 min, Max `NC_tw`=4; `P(Δt_d>0)`=16.1%, `E(Δt_d|·)`=1.67 min, Max `NC_td`=6.

Interpretive quotes: "if a passenger's delay increases with respect to its original prediction …, her extra delay will be (on average) as large as the average extra delay of the whole system; the average passenger faces 0.35 changes on the predictions, but **the maximum number of changes is 6, which makes any prediction barely useful**." (p.10) — "**First predictions are of little use if changes are so usual**, so developing techniques to provide better predictions or to make these changes less frequent is crucial for these systems." (p.10)

Perverse-incentive observation, §3.1.1, p.7 (directly motivates seniority/ratcheting): "consider a passenger p that has been waiting a long time T to be picked-up, and a passenger p′ that has just requested a trip with similar origin and destination. … With the cost function utilized in this work, which maximizes the quality of service for those requests that are satisfied, then the new request should be selected. This is because its lower real waiting time implies that she is receiving a better quality of service. **Such selection can be undesired when studying unreliability, as it implies that the chances of getting rejected are higher precisely for those passengers that have already been waiting for longer times.**"

## 1.6 Verbatim limitations / "we do not model X"

- Footnote 7, p.6: "We measure changes with respect to the first-announced indices defined above. **These indices are "naive" when assuming that no changes will take place.** … Moreover, proposing better first-announcements (predictions) is a very complex challenge, as they depend on each specific request and on the general state of the system. **Up to our knowledge, there are no public methods to provide these predictions effectively.**"
- §2, p.3–4: "In this paper we do not discuss unreliability sources that are already present in traditional public transport systems, such as congestion or accidents on the streets, or in car-sharing systems in which rides are not shared."
- §3.2, p.7: "However, in a real dataset it may be not possible to observe different realizations of the same trip, because it is unlikely that the exact same origin and destination are repeated several times every day."
- §5.2, p.16 (a policy sketch they do NOT implement): "These indices might be used by policy-makers in order to modify the assignment rules to improve reliability for all: for instance, **one might define a target waiting time and detour for each type of request, and penalize (or avoid) any assignment that yields results that are too far from that target.** Note that such penalization requires the system to pre-define a better quality of service for some types of requests …".
- §5.2, p.15: "**without policies that control uncertainty, these systems are similarly unreliable regardless of the fleet conditions.**"
- §7, p.18: "**There is plenty of room for future research regarding unreliability in ridesharing systems. The most relevant one is how to control it, i.e., studying how to alter the assignment procedures to provide more accurate times without increasing the rejection rate or passengers' average delay and waiting times.** Techniques to control unreliability are likely to be different if we aim to reduce one-time unreliability or daily unreliability."
- §7, p.18: "Some of the specific conclusions explained above might depend on the chosen scenarios, i.e., on the demand, fleet conditions and on the assignment rules."

**Theoretical results: none.** No theorem, bound, competitive ratio, or price-of-X. The only formal statements are the algebraic identities `Δt_d = Δt_v`, the decompositions Eq.(3)/(5)/(7), and the stochastic dominance `P(Δt_w>0) ⩽ P(ΔD>0)`, `P(Δt_d>0) ⩽ P(ΔD>0)`.

---

# PAPER 2 — Fielbaum, Tirachini & Alonso-Mora (2022), *Scale analysis for on-demand ridepooling systems and comparison with public transport*

## 2.1 There are no unreliability metrics of its own — it imports Paper 1's and declares them uncaptured

§4.1, p.14 — verbatim limitation, the key quote:

> "In this model, the Flex-route Effect increases waiting, walking, and in-vehicle times as vehicles increase their load. **It is noteworthy that there are other negative externalities that the model does not directly capture:**
> ● Fielbaum & Alonso-Mora (2020) identify two types of unreliability: The "one-time unreliability", defined as changes that take place while a trip is executed due to emerging requests, and the "daily unreliability", that refers to facing different conditions each time a trip is repeated. **Both types of unreliability worsen when vehicles are more loaded, i.e., the Flex-route Effect increases unreliability.** It is worth mentioning that this is not a minor issue: for instance, Alonso-González et al. (2020) have estimated the value of reliability … to be approximately a half of the value of time.
> ● Sharing the vehicle with more users can be uncomfortable by itself … the so-called "willingness to share" … complemented afterward with the increase in crowding …"

The service-quality quantities actually modelled are levels, not displacements: average waiting `t_w`, walking `t_a`, in-vehicle `t_v`, and **total delay** = "the extra time faced by a user compared to beginning her trip immediately, with no walking and following the shortest path between her origin and destination" (§3.1, p.6–7).

## 2.2 The algorithm — §3.1, pp.6–9

Receding-horizon batch assignment (δ = 1 min, Table A1). Trip `T` = (`req(T)`, `veh(T)`) feasible if the group "can be transported together by veh(T), **respecting some bounds on waiting and walking times, and on total delay (denoted, respectively, Ω_w, Ω_a and Ω_d). Such bounds affect users in req(T) and in S_veh(T)**." ← per-user **hard absolute caps applied to incumbents too**, but again on levels, not on cumulative displacement from a promise.

**Eq.(1)** (the incumbent-externality term, same structure as Paper 1 Eq.(9)):
```
cost(T, π) = Σ_{r∈req(T)} c_U(r,T,π) + Σ_{r∈S_veh(T)} Δc_U(r,T,π) + Δc_O(π)
```
"the first term represents the users' costs for passengers in trip T, defined as a weighted sum between waiting, walking, and in-vehicle times; **the second term represents the extra costs induced to the users that were being served by the vehicle prior to this assignment (because their waiting and in-vehicle times can increase)**; and the third term expresses the increase in operational costs".

**ILP, Eqs.(2)–(4)**:
```
min_{x,z∈{0,1}}  Σ_{T∈Γ} x_T cost(T) + Σ_{r∈R} p_KO z_r        (2)
s.t.  z_r + Σ_{T: r∈req(T)} x_T = 1     ∀r∈R                    (3)
      Σ_{T: veh(T)=v} x_T ≤ 1           ∀v∈V                    (4)
```
Endogenous fleet, **Eq.(5)**: `cost_A(T) = cost(T) + c_A·[1 − A(veh(T))]`, with `A(v)=1` if already activated. **Eq.(6)** replaces (3) when rejections are banned: "As we aim at comparing with public transport, we must have zero rejections. … we do not longer include variables z_r in the ILP … `Σ_{T: r∈req(T)} x_T = 1 ∀r∈R`".

Comparison bounds, §3.4, pp.11–12: `Ω_w = max{1/f, t1}`, `Ω_a = t2`, `Ω_d = max{1/f, t1} + 2t2` — i.e. the QoS allowance is **tied to the demand level via the PT frequency `f`**, so it tightens as demand grows. Footnote 2, p.12: "Such bounds ensure that users will indeed accept the assignment proposed by the system rather than searching for an alternative mode. Moreover, **without them the algorithmic burden of the problem would be unmanageable**, as every possible group of users could be feasibly served by any vehicle."

## 2.3 The externality language and the closest thing to theory — §5, pp.21–25

Three named effects (§5, p.21–23), explicitly framed as externalities: "we have identified three sources for scale analysis (**equivalently, three types of externalities caused by new users**)."
- **Mohring Effect**: "new users induce the utilization of a larger fleet, which reduces average waiting and walking times."
- **Flex-route Effect**: "the degradation in the perceived quality of service due to the increased vehicle load as a response to a larger demand. … When the demand grows, it is more likely to find users who can share the vehicles, eventually increasing their load. This increases the detours required by the system, which in turn increments waiting times. … **The Flex-route Effect gets exhausted when vehicles run at capacity** (or almost)."
- **Better-matching Effect**: "the ability to create groups whose routes are more compatible with each other when the demand grows, thanks to a larger pool of requests to choose from. … **This can be seen mathematically by noting that the optimization problem described by Eqs. (2)-(4) … exhibits a larger feasible set with larger demands, which always leads to better results.**" ← the only formal-ish argument in the paper (monotonicity of the optimal value under feasible-set inclusion). **It is not stated as a theorem and is not proved.**

Comparative-statics, §5, p.24. With `Y` = passengers, `ρ` = average vehicle load, `B` = fleet size, and `t_h` the average waiting/walking/in-vehicle times:
- **Eq.(13) (Mohring)**: `∂t_h/∂B ≤ 0` for `h = w, a`
- **Eq.(14) (Flex-route)**: `∂t_h/∂ρ ≥ 0` for `h = w, a, v`
- **Eq.(15) (Better-matching)**: `∂t_h/∂Y ≤ 0` for `h = w, a, v`
with "`B′>0, ρ′>0`" and "As B and ρ increase with Y, the combined effect of all the three sources of scale can be positive or negative (due to the chain rule)."

**Degree of Scale Economies** (§5, p.23): "the Degree of scale economies, which is formally defined for any production function as **the average costs divided by the marginal costs**: this means that there is a threshold in `DSE = 1` determining whether scale economies or diseconomies prevails."

Numerical thresholds: diseconomies appear at ≈300 pax/h ("Diseconomies of scale emerge when Y reaches about 300 passenger/h"), average delay rises to ~5 min/pax up to 1000 pax/h, then falls to ~2 min/pax at 3000 pax/h (§4.1, p.13). Optimal capacity 2 for `Y ≤ 550`, 3 thereafter (circular); ODRP cheaper than PT only for demand up to ~130 pax/h.

## 2.4 Verbatim limitations

- §1, p.3: "The single-line model has a relevant limitation when studying on-demand systems, which require that the vehicles' routes are not defined a priori but adapted to the emerging users. Such a feature cannot be captured in a single-line model in which there is only one possible route."
- §2.1, p.4 & §3.1, p.8: "In both studies the fleet is computed as if the demand was known, **an approach that we also follow here**." / "**The fleet optimization cannot be done online, so optimizing a posteriori (i.e., as we knew all the requests) is appropriate.** In this case, the receding horizon approach is not meant to represent the online optimization, but a way to manage the impossibility (due to its enormous complexity) of assigning the whole set of requests optimally at once."
- §3.1, p.8: on rebalancing — "**We do not explain the details here because we do not use such a procedure in this paper.** We do execute a simple rebalancing step when modeling a feeder model".
- §4.1, p.14: the "other negative externalities that the model does not directly capture" block quoted in §2.1 above.
- §4.1, p.18: "**How to design such an integrated system is a broad question that goes beyond the scope of this paper**".
- §6, p.25: "Moreover, introducing the spatial components, i.e., looking at the whole transit network rather than at a single line, might reveal other sources of scale that do not show up here."
- §6, p.25: "Our simulations revealed that **ODRP users induce both positive and negative externalities to the other passengers.** … the negative externalities relate with increasing the number of users per vehicle, which induces longer detours, which we call the "Flex-routes Effect"."

**No budgets, no counters, no attribution, no commitment/promise/freezing language anywhere. Grep for `promis|commit|cumulativ|freez|ratchet|budget|scarce|knapsack|primal-dual|shadow price|VCG|Lagrang|theorem` returns nothing beyond a citation to Pinto et al.'s system-level fleet budget.**

---

# PAPER 3 — Sharif Azadeh, Atasoy, Ben-Akiva, Bierlaire & Maknoon (2022), *Choice-driven dial-a-ride problem for demand responsive mobility service*, TR-B 161:128–149

## 3.1 What is offered, when, and what is "promised" — §3, pp.130–131 + §4.1, p.132

Sequential, one-at-a-time, myopic: "The operator receives N trip requests at time `τ^arr_1 < τ^arr_2 < ⋯ < τ^arr_N` … **The requests arrive one at a time (i.e., batch arrivals are excluded) and are processed sequentially, based on the first-come, first-served principle.** The operator has no prior knowledge of future demand (such as arrival rate and origins–destinations) and **any demand surge does not influence the price of alternatives**. The aim is to identify the most profitable set of alternatives to offer to each new request to maximize the expected profits **by solving a sequence of myopic problems** upon the arrival of each individual request using a rolling horizon approach."

A request = (origin, destination, preferred pickup time `τ^p_n`). **Alternative** `a ∈ A` = "a unique combination of service type (taxi, shared taxi) and pick-up time" (§4.1, p.132). Delay menu `Ω = {ΔT, 2ΔT, 3ΔT}` (ΔT = 3 min, Table 5) giving windows `[τ^p_n, τ^p_n+ΔT]`, `[τ^p_n, τ^p_n+2ΔT]`, `[τ^p_n, τ^p_n+3ΔT]`. Max ride time for shared: `t_a = min{1.5 I_taxi, I_taxi + 15}`. Six alternatives in all experiments (2 services × 3 delay slots).

**The accepted "promise" object** (§3, p.130): "Upon receiving the acceptance, we show the choice of the new customer by `Γ_n`, presented by a tuple including **origin, destination, service type, confirmed pickup time window and the maximum ride-time (`L^Max_n`)**. At this point, we adjust the routes of all vehicles in the network (i.e., re-routing…)."

**Exactly two communications to the customer** (§3, "Customer interaction sequences", p.130):
> "The system communicates information with the new customer on two occasions. **First, when the customer chooses one of the offered alternatives, she is notified about her confirmed pickup time window. Second, the moment the assigned vehicle hits the road to pick her up, she is notified about the exact time the vehicle is expected to arrive.**"

**Is the promise revised after acceptance? — the authors' own answer (§4.1, p.132, the single most important passage for your (a)/(b)):**
> "We use the maximum ride time and delayed pickup times to estimate the utility associated with each alternative. **We acknowledge that utility value of each alternative is underestimated using this approach. The realized utility of the customer may exceed this estimated value.**
> The customer is informed about the exact waiting time, once the vehicle hits the road to the pickup location. Subsequently, the realized value of the ride time can be calculated as soon as the customer is dropped off at the destination. **Both maximum ride time and delayed pickup times respect the guaranteed values embedded in the alternatives. We must clarify that the users pay according to the estimated utility when the request is made. This approach may have long-term repercussions on user choices due to the fact that it is independent from the realized value of waiting time and the maximum ride time.**"

Reading: the **bounding box** (`[e_i, l_i]`, `L^Max_i`) is never revised — it becomes a hard constraint enforced at every subsequent re-optimization (Constraints (20), (24)). But **the position inside that box is re-optimized without limit, without tracking, and without price adjustment**, and the authors explicitly flag this as a weakness ("may have long-term repercussions on user choices"). There is no notion of cumulative displacement within the box.

Partial freezing exists at the arc level (§3, "Vehicle status", p.130): "An arc is defined as **executed** when a vehicle starts the journey to go to the next location. **The trip assigned to the executed arc cannot be modified.** As long as the vehicle has not departed a node (either initial or a via point), the arc is considered to be **planned**. The planned arcs are still subject to change, to accommodate a new request n." Executed iff `τ^arr_n ≥ B̄^k_i`. "Note that the maximum ride-time of the existing requests is considered in the CD-DARP model while revising the routes (i.e., re-routing)."

## 3.2 Choice model & assortment — §4.1–4.3, pp.132–133

**Eq.(1)** MNL systematic utility: `v_al = ASC_a − β_f f_al − β_t t_a − β_ω ω_a  ∀a∈A, l∈F_a`, with `u_al = v_al + ε_a`, `ε_a` Type-I EV. Opt-out `u_0` = competitor: "customers are not captive in the system, meaning that they also have the option not to choose any of alternatives being offered. In this case, we assume that the customer uses the service offered by the competitor, whose utility is identified by `u_0`."

**Eq.(2)** choice probability within assortment `s` (`b^s_al = 1` iff alt `a` offered at price level `l` in `s`; `Σ_{l∈F_a} b^s_al ≤ 1`):
```
P(a;s) = ( Σ_{l∈F_a} b^s_al e^{v_al} ) / ( Σ_{a'∈A} Σ_{l∈F_a} b^s_{a'l} e^{v_{a'l}} + e^{v_0} )
```

**Pricing — §4.2, p.132–133.** "In this problem, we assume that the operator is committed to providing attractive mobility services to the users. As a result, the price of alternatives is designed to maintain service attractiveness. **In this paper, the price is set independently of resource availability and surge demand.**" Range `[F_a, F̄_a]`; the lower limit is "the minimum price that is still profitable for the operator … based on the combination of a fixed and an expected variable cost of routing proportionately to the shortest path"; the upper limit is a cut-off purchase probability `ζ_a`, from **model Z**:
```
Z : max F̄_a   s.t.   e^{v̂_a − β_f F̄_a} / ( e^{v̂_a − β_f F̄_a} + e^{v_0} ) ≥ ζ_a,    v̂_a = ASC_a − β_t t_a − β_ω ω_a
```
"Model Z can be solved analytically." Price levels = uniform discretization of `[F_a, F̄_a]` (level 0.1 $, `ζ` = 0.05; min fare $5 + $0.5/km; Tables 4–5, p.140).

Rejection by the operator (§3, p.130): "the operator can reject a new request when: (i) there is no vehicle available to serve the new customer, and (ii) **the expected profit is negative**. In these cases, we define an empty set as the offered assortment."

## 3.3 The optimization model — §5, pp.133–136

Objective **Eq.(3)**: `max Σ_{s∈S} E_s y_s` s.t. (4)–(37).

**Marginal routing cost** (this is the paper's one real internalization device), **Eq.(4)**: with `C̄^k` = routing cost of vehicle `k` *before* request `n`,
```
σ^k = Σ_{i∈N} Σ_{j∈N} c_ij x^k_ij − C̄^k        ∀k∈K        (4)
```
**Eq.(6)**: `δ_a = Σ_{k∈K} σ^k z^k_a  ∀a∈A` — "if vehicle k is assigned to alternative a …, the cost of this alternative is equal to the marginal routing cost of the assigned vehicle."
**Eq.(8)**: `Δ^k = σ^k (1 − Σ_{j∈N} x^k_nj)  ∀k∈K` — the marginal re-routing cost of vehicles *not* serving the newcomer: "when vehicle k is not assigned to serve one of the alternatives offered in the assortment, **its marginal routing cost still has an impact on the overall expected profit of the assortment and must be addressed**."

**Expected profit, Eq.(10)** (with `r_a = f_al − δ_a`):
```
E_s = Σ_{a∈A} r_a P(a;s) − Σ_{a∈A} P(a;s) Σ_{k∈K} Δ^k      ∀s∈S
```
"the first term presents the expected profit of offering assortment s summed over all its alternatives, while **the second term shows the expected cost related to the re-routing of vehicles that are not used to offer any of these alternatives**. … This value is calculated once prior the decision being made to determine the optimal assortment s\*, and once after the choice has been made to modify the vehicles' routes according to the customer's decision."
Rearranged as **Eq.(47)**, §6.1, p.137: `E_s = Σ_a P(a;s) f_al − Σ_a P(a;s)(δ_a + Σ_k Δ^k)`, the bracket being "assortment cost".

**Critical for (b):** `σ^k`, `δ_a`, `Δ^k` are **vehicle-kilometre / operator routing costs only**. The newcomer's price is compared against the marginal *routing* cost; **the incumbents' extra waiting/ride time never enters the objective with any weight.** Incumbent inconvenience appears only as hard constraints:

- **Eq.(11)**: `Σ_k Σ_j x^k_ij = 1  ∀i∈P\{n}` — "all confirmed requests … are visited by exactly one vehicle".
- **Eq.(20)**: `e_i ≤ B^k_i ≤ l_i  ∀i ∈ N\{n,2n}, k∈K` — confirmed requests' pickup windows are inviolable.
- **Eq.(21)**: `e_ia − M_l(1−z^k_a) ≤ B^k_i ≤ l_ia + M_u(1−z^k_a)` for `i∈{n,2n}` — the newcomer's window is enforced only for the alternative actually assigned.
- **Eq.(23)**: `L^k_i = B^k_{n+i} − (B^k_i + d_i)`; **Eq.(24)**: `L^k_i ≤ L^Max_i  ∀i∈P, k∈K` — **per-user hard maximum ride time, for every already-confirmed passenger, re-imposed at every subsequent decision.**
- Load: Eqs.(26)–(32), `q_i = Q` for taxi (monopolizes the vehicle), `q_i = 1` for shared.
- Assortment linking: **Eq.(33)** `Σ_s y_s = 1`; **Eq.(34)** `Σ_k z^k_a = Σ_s γ^s_a y_s`; **Eqs.(35)–(36)** link vehicle assignment to routing.
Linearization: Eqs.(38)–(46), with `M̂^k = C̄^k` (§6.4, p.138).

Schedule/dispatch LP, §7.2, **Eqs.(50)–(54)**: `max Σ_{i,k} W^k_i` s.t. `W^k_i + d_i = B̄^k_i − B^k_i` (51), `B^k_{i+n} − B^k_i − d_i ≤ L^Max_i` (52), `e_i ≤ B^k_i ≤ l_i` (53), `W^k_i = 0` when `Q^k_i ≠ 0` (54) — "**Constraints (54) prohibit additional waiting time with passengers on board.**"

## 3.4 Theoretical results — §6.1, pp.136–137 (the only ones in the three papers)

Assortment space size: `Π_{a∈A}(|F_a|+1)`, "which is computationally cumbersome."

**Policy I** — drop assortment cost from Eq.(47) and maximize revenue over comparable assortments (same alternatives, different prices) via fractional binary program **model J** (Eq.(48)):
> "Model J shares two similar properties with the optimal line selection problem discussed by Chen and Hausman (2000): (i) **the objective function is both strictly quasi-convex and strictly quasi-concave**, and (ii) **the coefficient matrix is completely unimodular. As such, for this model, any local maximum solution is the global maximum and the optimal solution of its relaxation (by dropping the integrality constraints) is integral.** … By using Charnes–Cooper transformation, we can easily transform the relaxation counterpart into a linear programming (LP) model".

**Policy II** — efficient-set/fixed-point characterization: `max{λ∈R : Σ_{l∈F_a} h_al = 1, and Σ_l Σ_a h_al e^{v_al}(f_al − δ_a − Σ_k Δ^k − λ) ≥ λ}`, with lines `η_al(λ) = e^{v_al}(f_al − δ_a − Σ_k Δ^k − λ)`, `η^0_al(λ)=0`:
> "following from **Proposition 1 in Talluri and van Ryzin (2004)**, we need to determine the non-dominated set of assortment for every λ. As discussed in Section 2.1 of **Rusmevichientong et al. (2010)**, instead of finding the non-dominated set for every value of λ, **we can limit our evaluations to the intersection points among all lines defined by function η_al(λ)**." Efficient set via Eq.(49). "**for any Σ_k Δ^k ≥ 0, all the intersection points will be shifted by Σ_k Δ^k.**"

No competitive ratio, no regret bound, no price-of-anarchy. Global optimality is explicitly disclaimed: "we solve this dynamic problem in a myopic fashion, and **we cannot guarantee the global optimality based on the profit performance**" (§8.2, p.141).

## 3.5 Verbatim limitations / "we do not model X"

- §1, p.129: "**In our case, choice parameters are estimated outside the optimization problem.**"
- §3, p.130: "The operator **has no prior knowledge of future demand** (such as arrival rate and origins–destinations) and **any demand surge does not influence the price of alternatives**."
- §3, p.130: "**Relocating and re-balancing idle vehicles fall outside of scope of this paper.**"
- §4.1, p.132: "**We acknowledge that utility value of each alternative is underestimated using this approach. The realized utility of the customer may exceed this estimated value.**" … "**We must clarify that the users pay according to the estimated utility when the request is made. This approach may have long-term repercussions on user choices due to the fact that it is independent from the realized value of waiting time and the maximum ride time.**"
- §4.2, p.132: "In this paper, **the price is set independently of resource availability and surge demand**."
- §7.1, p.139: "**the routing decision of solving CD-DARP may violate the optimal route assumption after the choice is made.** As a result, we solve the inherit DARP model to modify the vehicle routes."
- §8.2, p.141: "we solve this dynamic problem in a myopic fashion, and we cannot guarantee the global optimality…"
- §8.2, p.143: "The CD-DARP is the combination of assortment optimization and dial-a-ride problems, both of which were proven to be NP-Hard. … the computational time is sensitive to the number of offered assortments and the number of active users … **This limitation calls for the introduction of an efficient heuristic approach … This part has been left out of the scope of this paper and will be tackled in future research.**" (worst case 97.41 s/request with 6 vehicles; 600 s cap hit on Cordeau instances; avg. time jumps to 236.58 s at 20 vehicles with 1/8 inter-arrival multiplier, Table 9)
- §8.3, p.143–144: "for a fair comparison between scenarios, **we assume that only the operator can reject a request due to infeasibility, while customers are captive (no opt-out option)**. The utility of the opt-out option is still used to determine the price of alternatives."
- §9 conclusion, p.147: "In the CD-DARP, **no prior knowledge about future demand is assumed**. … the computational limitations of this model call for the introduction of an efficient heuristic method to solve larger instances. In this case, we will need to incorporate the knowledge involving future demand into the model. It would also be interesting to **develop algorithms that would allow for learning the choice parameters on a continuous basis which would also partly address the issue of perceived impact of the maximum ride time assumptions.** Another extension that to consider is to combining the existing framework with rebalancing the empty fleet in the network".

## 3.6 Selected results (for calibration/benchmarking)

- §8.3 (scenarios **P** = preferred time only ≙ classic dynamic DARP; **A** = assortment; **D** = maximum-deviation only): taxi service, 2 vehicles, `P→D` served-passenger improvement **+7.22%** on average (Table 12); shared taxi, 6 vehicles, `P→D` **routing cost −7.65%** average, served passengers `P→D` **+9.09%** average (Table 13). "For taxi services, by delaying passenger pick-up time (i.e., P→D), the number of customers served increases. This improvement is more significant when there is a clear demand-supply mismatch."
- §8.4, p.145: trip-based vs flat pricing — "The percentage of customers rejecting all offered alternatives reduces on average from 14.7% to 6.41%. … average profit improvement is around 9%."
- §8.5, NYC green-cab, 379 trips, 25 vehicles, Table 14 (p.146): Scenario I (one alternative, no re-routing — "mimics the conventional taxi dispatching system") serves 41.68%, profit 436.38, customer rejection 58.12%, satisfaction −55.06; Scenario II (menu, no re-routing) 74.36%, 654.93, 17.38%, −19.99; Scenario III (menu + re-routing) **76.36%, 705.13, 15.32%, −19.38**. Satisfaction metric: "We quantify satisfaction by using **the logarithm of the denominator of offered choices** (see, Train (2009)…)" — i.e. the MNL logsum.
- Cordeau (2006) instances: 60-min advance → 41.85 served, 0.46 operator-rejected, 1.69 customer-rejected, 12.66 active requests, rev. 435.27, cost 269.86; 120-min advance → 42.34 served, 20.61 active requests, rev. 439.43, cost 269.37. "we observe that **advance arrival information slightly impacts the number of served requests (41.85 compared to 42.34)**."

---

# ANSWERS TO (a), (b), (c)

## (a) Does any of these three papers enforce a per-passenger bound on **cumulative promise displacement** as a **hard feasibility constraint at decision time**?

**No — none of the three.** All three enforce per-passenger hard bounds, but on **absolute service levels fixed once**, never on **accumulated drift away from what was announced**. Evidence:

1. **Fielbaum & Alonso-Mora (2020)** enforce absolute caps only: a trip is feasible "without exceeding the capacity of the vehicle and **without violating constraints that deal with the maximum admissible waiting times and total delay**" (§4, p.7; 5 min / 10 min, Table 6 p.18). Those caps are absolute levels, not displacement. They *measure* displacement (`Δt_w, Δt_d, ΔD`, Definitions 5–7) and even *count* repeated degradations (`NC_tw, NC_td, NC_D`, **Definition 9**) — but the counter is never a constraint. Explicit statement that flexibility is unrestricted: "here we maximize the flexibility of the system by admitting any change, **as long as it does not violate the bounds on waiting times and delay of every request**" (§4, p.7). The one exception is the **§6 "Fully controlled scenario"**: "When a passenger gets assigned to a vehicle, it is marked as non-rejectable for future assignments, and **her maximum waiting time is updated to the predicted one**" (p.16). That is a hard, per-user, decision-time constraint on promise displacement — but with **budget exactly zero** (a freeze, not a budget), **waiting time only** (detour deliberately excluded, footnote 13 p.17: eliminating `U_D` this way "would turn the whole system in a (almost) non-shared one"), and presented as a **comparative experiment, not a mechanism**. Its cost is severe: rejections 34.5% → **45.6%**, users' cost 9.56 → 11.6 (Table 5, p.16). Their own verdict: "the more controlled the unreliability, the higher the average users' costs. … **This reinforces the need of more sophisticated ideas to control unreliability.**"
2. **Fielbaum, Tirachini & Alonso-Mora (2022)** likewise: "respecting some bounds on waiting and walking times, and on total delay (denoted, respectively, `Ω_w, Ω_a` and `Ω_d`). **Such bounds affect users in `req(T)` and in `S_veh(T)`**" (§3.1, p.6–7). Absolute levels, applied to incumbents too, but no displacement quantity exists in the model at all; they explicitly say displacement-type unreliability is **not captured**: "**It is noteworthy that there are other negative externalities that the model does not directly capture:** … the "one-time unreliability", defined as changes that take place while a trip is executed due to emerging requests" (§4.1, p.14).
3. **Sharif Azadeh et al. (2022)** come closest in *spirit* — Constraints **(20)** `e_i ≤ B^k_i ≤ l_i` and **(24)** `L^k_i ≤ L^Max_i` are hard per-user constraints re-imposed at every re-optimization on every already-confirmed passenger, with `L^Max_i` and the window fixed at acceptance inside `Γ_n` ("confirmed pickup time window and the maximum ride-time (`L^Max_n`)", §3, p.130). But that is a **static bounding box**, not a cumulative displacement budget: inside the box the schedule may be reshuffled arbitrarily often at zero modelled cost, and the authors state the resulting gap themselves: "**Both maximum ride time and delayed pickup times respect the guaranteed values embedded in the alternatives. We must clarify that the users pay according to the estimated utility when the request is made. This approach may have long-term repercussions on user choices due to the fact that it is independent from the realized value of waiting time and the maximum ride time.**" (§4.1, p.132) and "**We acknowledge that utility value of each alternative is underestimated using this approach. The realized utility of the customer may exceed this estimated value.**" The only genuine irreversibility is arc-level, not passenger-level: "**The trip assigned to the executed arc cannot be modified.**" (§3, p.130)

→ **Thesis gap statement is safe:** no paper carries a per-passenger *cumulative* displacement ledger that is checked as a feasibility condition when a new request is admitted.

## (b) Does any price or internalize the externality a NEW request imposes on INCUMBENT passengers?

**Internalized as a soft penalty in a social-cost objective: yes (Papers 1 & 2). Priced / charged / mechanism-designed: no, in all three. Nothing resembling VCG, Lagrangian/shadow price, or congestion price appears in any of the three.**

- **Paper 1, Eq.(9)** (§4, p.8): `c(τ,v) = Σ_{r∈τ}[p_w t_w + p_v t_v] + Σ_{r∈v}[p_w Δt_w(r,τ,v) + p_v Δt_v(r,τ,v)] + c_0 ΔL(τ,v)` — "**the second term represents the additional times for those requests that were already being served by v**". This is a Pigouvian-style term inside the *assignment cost*, aggregate over incumbents, soft (tradeable against `p_KO`-style rejection weight 40 and operator cost), with **no monetary transfer and no per-user cap on the increment**. Footnote 10 concedes the pricing link is not modelled: "For-profit companies might use slightly different cost functions depending on how they price each trip, but they are also interested in minimizing their own costs…".
- **Paper 2, Eq.(1)** (§3.1, p.7): `cost(T,π) = Σ_{r∈req(T)} c_U + Σ_{r∈S_veh(T)} Δc_U(r,T,π) + Δc_O(π)` — "**the second term represents the extra costs induced to the users that were being served by the vehicle prior to this assignment (because their waiting and in-vehicle times can increase)**". Same structure, same status: an objective term, not a price. The paper *names* the externality in economic language — "ODRP users induce both positive and negative externalities to the other passengers" (§6, p.25); "three sources for scale analysis (equivalently, three types of externalities caused by new users)" (§5, p.21) — and reports **DSE = average cost / marginal cost** (§5, p.23), but it never converts marginal cost into a charge, a toll, or an admission price. There are **no fares at all** in the ODRP model; the objective is total (users' + operators') cost.
- **Paper 3** internalizes only the **operator's marginal routing cost**, not incumbent inconvenience. **Eq.(4)** `σ^k = Σ_i Σ_j c_ij x^k_ij − C̄^k`; **Eq.(6)** `δ_a = Σ_k σ^k z^k_a`; profit `r_a = f_al − δ_a`; **Eq.(8)/(10)** add `Δ^k` = "the expected cost related to the re-routing of vehicles that are not used to offer any of these alternatives". The newcomer's fare must clear that marginal **vehicle-km** cost — but the incumbents' additional waiting/ride minutes carry **zero weight in the objective**; they appear only as the hard constraints (20)/(24). And the paper *rules out* congestion/scarcity pricing by construction: "**In this paper, the price is set independently of resource availability and surge demand**" (§4.2, p.132) and "**any demand surge does not influence the price of alternatives**" (§3, p.130). The price ceiling comes from a behavioural cut-off probability (model **Z**, `≥ ζ_a`), not from an opportunity cost.

→ **The strongest true statement for your thesis:** the incumbent externality is internalized *only* as an unweighted-by-promise, aggregate, soft term in a central planner's cost function (Papers 1–2), or not at all on the user side while the *operator's* marginal routing cost is internalized into the newcomer's profit margin (Paper 3). **No paper makes the newcomer pay (in money or in priority) for the stability it destroys.**

## (c) Does any treat the promise-stability allowance as a SCARCE RESOURCE allocated over time (budget / knapsack / primal-dual / threshold policy)?

**No — none of the three. Grep across all three files for `budget|cumulativ|ratchet|allowance|scarce|knapsack|primal-dual|shadow price|threshold polic|VCG|Lagrang` returns nothing on point.** Evidence for the negative:

- **Paper 1:** the allowance is a **constant per-request cap** re-supplied fresh to every request (5 min wait / 10 min delay, Table 6) with **no consumption accounting across the trip**, and a rejection penalty of 40 that is a *fixed* weight, not a dual variable. The only "allowance-management" idea in the whole paper is floated and left undone (§5.2, p.16): "**one might define a target waiting time and detour for each type of request, and penalize (or avoid) any assignment that yields results that are too far from that target.** Note that such penalization requires the system to pre-define a better quality of service for some types of requests…". And the closing gap statement (§7, p.18): "**The most relevant one is how to control it, i.e., studying how to alter the assignment procedures to provide more accurate times without increasing the rejection rate or passengers' average delay and waiting times.**" Its §6 experiment shows the binary corner of this design space (all-or-nothing freeze) and its price; it never explores the interior.
- **Paper 2:** the bounds *do* vary with system state — `Ω_w = max{1/f, t1}`, `Ω_d = max{1/f, t1} + 2t2` (§3.4, p.12) — so the allowance tightens as demand `Y` (hence frequency `f`) grows. **But this is an exogenous calibration for comparability with public transport, not an allocation:** "To make a fair comparison, we adapt the bounds depending on the total number of users. Note that this mimics what passengers usually face…". Footnote 2, p.12 gives the second, purely computational motive: "**without them the algorithmic burden of the problem would be unmanageable**, as every possible group of users could be feasibly served by any vehicle." There is no dual price on the allowance, no budget consumed over time, and the model is explicitly **offline/a-posteriori**: "the fleet is computed as if the demand was known, an approach that we also follow here"; "**The fleet optimization cannot be done online, so optimizing a posteriori … is appropriate.**"
- **Paper 3:** explicitly and repeatedly myopic and scarcity-blind. "solving **a sequence of myopic problems** upon the arrival of each individual request"; "The operator **has no prior knowledge of future demand**"; "**the price is set independently of resource availability and surge demand**"; "we solve this dynamic problem in a myopic fashion, and we cannot guarantee the global optimality". The only opportunity-cost-like object is `Δ^k` (re-routing cost of *unused* vehicles), which is a realized routing cost within the current decision, not a value-function/shadow price on future capacity. The threshold-like machinery that *is* present — the `λ`-parameterized efficient-set construction of **Policy II**, Eq.(49), and the shift result "for any `Σ_k Δ^k ≥ 0`, all the intersection points will be shifted by `Σ_k Δ^k`" — is a **revenue-management assortment device (Talluri & van Ryzin 2004; Rusmevichientong et al. 2010), not a capacity/stability bid-price.** They flag the missing piece themselves in §9: "we will need to **incorporate the knowledge involving future demand into the model**."

---

# ONE-PARAGRAPH SYNTHESIS FOR THE THESIS POSITIONING

Fielbaum & Alonso-Mora (2020) supply the **measurement layer** you need (`Δt_w`, `Δt_d`, `ΔD` against a first announcement `t¹`; `NC_D` change counters; `U_R` rejection reversal; the operator-caused vs. user-caused taxonomy, Definitions 1–2, with traffic-caused explicitly scoped out) and prove empirically that displacement is large and repeated (36.1% of first-accepted requests change; `E(ΔD|ΔD>0)` ≈ the whole system's average delay; up to 6–8 successive degradations per user), but their only control lever is a **binary freeze** whose cost they document as a rejection-rate jump 34.5%→45.6%, ending with an explicit call for "more sophisticated ideas to control unreliability". Fielbaum, Tirachini & Alonso-Mora (2022) give you the **economics vocabulary** (Flex-route / Mohring / Better-matching as externalities of new users; `∂t_h/∂ρ ≥ 0` Eq.(14); DSE = AC/MC) and an explicit admission that displacement-unreliability is "a negative externality that the model does not directly capture". Sharif Azadeh et al. (2022) give you the **commitment interface** — a menu of priced (service type × pickup-window) alternatives with an MNL opt-out, a `Γ_n` tuple that fixes a confirmed pickup window and `L^Max_n` at acceptance and re-imposes them as hard constraints (20)/(24) at every subsequent re-optimization — plus the exact statement of the residual gap: the customer "pay[s] according to the estimated utility when the request is made … independent from the realized value of waiting time and the maximum ride time", which "may have long-term repercussions on user choices". **None of the three: (a) budgets cumulative displacement per passenger as a hard admission test, (b) charges the newcomer for incumbent destabilization, or (c) allocates stability as a scarce resource over time.**
