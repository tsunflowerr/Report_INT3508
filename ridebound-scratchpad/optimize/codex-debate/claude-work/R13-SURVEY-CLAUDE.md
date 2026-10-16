# R13 survey (Claude side): business value of reliable promises, promise stability as an objective, alternative promise forms, implementable algorithm directions

Date: 2026-10-10. Claude literature agent. Only this file was written in the debate folder. I did not open any `codex-work/R13-*` file.
I read `ROUND13-FACT-PACK.md`, SURVEY-S1 to S4, `business-need/SOURCES-2026-10-05.md` (headings and verdicts) and the claim boundary
(`C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md`). Sources already covered there are not repeated unless I
add a new verified fact. Temporary downloads (PDF/HTML used for grep) went only to the session scratchpad, outside the project.

**Status tags**
- `VERIFIED-full`: I extracted the full text myself (pdftotext or curl), and the quote is copied from it.
- `VERIFIED-abstract`: verbatim abstract from Crossref, OpenAlex or IDEAS/RePEc metadata. Claims beyond the abstract are not checked.
- `VERIFIED-page`: page opened with WebFetch. WebFetch passes text through a summarizer that limits quotes to about 125 characters.
  The quotes are short exact fragments, but the surrounding sentence was not seen in full.
- `UNVERIFIED (blocked)`, `UNVERIFIED (snippet only)`, `UNVERIFIED (title only)`: do not use as evidence.

Relevance lines refer to the owner's questions: O2 (what rule C gives the operator, and would others optimize it), O3 (what riders
care about, with forecast added), O6 (better direction, different promise, or algorithm optimization).

---

## (a) Business value of ETA and promise reliability

### a1. Operator guarantees: who pays when a time promise breaks

1. **Lyft, "Our on-time pickup promise"**, Lyft blog, 9 Nov 2023. https://www.lyft.com/blog/posts/our-on-time-pickup-promise
   - Quotes: "Starting today, scheduled rides to the airport will be covered by our on-time pickup promise in many major markets."; "$15 Lyft Cash if your driver is more than 10 minutes late."; "$50 Lyft Cash automatically if you're not matched with a driver 10 minutes after your scheduled pickup time."; "you'll get up to $50 more Lyft Cash – up to $100 total – even if you take a taxi or an Ub*r."
   - Relevance (O2/O6): a large operator pays automatically for a broken **pickup** promise on pre-booked rides. Nothing here covers drop-off or pooled rides.
   - Status: VERIFIED-page.
2. **Uber Reserve on-time guarantee (launch)**, TechCrunch, 10 Nov 2020. https://techcrunch.com/2020/11/10/uber-will-now-let-users-book-rides-30-days-in-advance-and-pick-a-favorite-driver/
   - Quote: "an on-time guarantee that will give users $50 in Uber Cash if their driver is even a minute late to the ride they have scheduled. That Uber Cash will come directly from Uber, not the driver's earnings".
   - Relevance (O2): a pickup-only guarantee, paid by the platform. Current terms are not verified; a 2026 consumer guide claims "max 3 credits per 30 days" [UNVERIFIED (snippet only)].
   - Status: VERIFIED-full (curl + grep of the article body).
3. **UberPOOL "Arrive by" guarantee (2016)**, PCWorld, Ian Paul, 8 Jun 2016. https://www.pcworld.com/article/415144/uberpool-guarantees-youll-arrive-on-time-or-get-a-small-portion-of-your-money-back.html
   - Quotes: "if you show up later than the estimate, you get $2 off your next UberPool ride"; Uber's time estimates are "the 'absolute latest time you'll reach your destination.'"
   - Relevance (O3/O6): **a pooled drop-off promise with compensation has existed.** Uber met it by quoting a padded latest time, which is the "padding" end of our cap-vs-pad frontier. It is news coverage of an LA test, not an Uber page.
   - Status: VERIFIED-full (curl + grep).
4. **UberX Share product page** (current, undated). https://www.uber.com/us/en/ride/uberx-share/
   - Quotes: "won't increase your estimated arrival time" (in "help make sure any additional pickups won't increase your estimated arrival time", already in S3); "UberX Share is designed to add 8 minutes to your trip on average"; "because of traffic and other possible delays, we cannot guarantee arrival times".
   - Relevance (O2, novelty): the operator **states in public the same split rule C uses**: pooling-caused ETA increases are what the matcher tries to avoid, and traffic is disclaimed. This supports business relevance. It is also a concept-level threat to novelty (see the synthesis).
   - Status: VERIFIED-page (fragments obtained in two WebFetch calls; curl was blocked).
5. **Uber One Promise (delivery)**, Uber investor press release, 17 Nov 2021. https://investor.uber.com/news-events/news/press-release-details/2021/Uber-Introduces-Uber-One-A-New-Membership-Program-Bringing-Together-the-Best-of-Uber/default.aspx
   - Quote: "members get $5 in Uber Cash on eligible deliveries if our Latest Arrival estimate (shown after an order is placed) is wrong."
   - Second page, https://www.uber.com/ec/en/u/rewards/ : "$5 credit is based on the Latest Arrival By estimate, determined once you place your order."
   - Relevance (O2/O6): a promise is **fixed at order time** (a first-promise anchor, like our v₀) and paid if broken. Delivery only.
   - Status: VERIFIED-page (both).
6. **UK rail Delay Repay 15 (Northern)**, GOV.UK news, 17 Dec 2018. https://www.gov.uk/government/news/delay-repay-15-goes-live-for-northern-passengers
   - Quotes: "Northern passengers are now eligible for extended compensation on journeys delayed by 15 minutes or more"; "regardless of the cause of delays or cancellation"; "passengers delayed by between 15 and 29 minutes can claim back compensation worth 25% of the single fare."
   - Relevance (O2): the **passenger-facing** scheme ignores cause, while the inter-operator Schedule 8 regime (prior audit) attributes delay by cause. That is the same two-layer design as "rider sees z, operator audits c vs x".
   - Status: VERIFIED-page.
7. **Instacart late-arrival credit.** https://instacart.com/help/article/quality-guarantee-terms returned "page doesn't exist". The search snippet says the credit is capped at fees.
   - Status: UNVERIFIED (404). Do not use.
8. **Uber Eats Pro on-time rate**, Uber blog, 16 Sep 2025. https://www.uber.com/us/en/blog/on-time-rate-and-uber-eats-pro
   - Quote: on-time rate is "the total number of pick-up and drop-off arrivals you've completed within the estimated time displayed in the app."
   - Relevance (O2): operators score couriers against the displayed estimate. Once the promise is displayed, its reliability becomes a managed KPI.
   - Status: VERIFIED-page.

### a2. Empirical effects of (un)reliable promises on demand, retention and behaviour

9. **Cui, Lu, Sun & Golden (2023), "Sooner or Later? Promising Delivery Speed in Online Retail"**, MSOM. doi:10.1287/msom.2021.0174
   - Quote: "we exogenously varied the disclosed delivery speed estimates online while keeping the physical delivery speed unchanged"; "a faster promise increases sales and profits, but it also increases product returns and reduces customer retention".
   - Relevance (O2): **field-experiment proof of the promise trade-off.** An aggressive promise buys conversion and costs retention. This is the business form of "short quote vs late vs first promise".
   - Status: VERIFIED-abstract.
10. **Yu, Zhang & Zhou (2022), "Delay Information in Virtual Queues: A Large-Scale Field Experiment on a Major Ride-Sharing Platform"**, Management Science 68(8):5745–5757. doi:10.1287/mnsc.2022.4448
    - Quote: "randomized field experiment that included 1,425,745 rides"; "both the magnitude of the initial WTI and the update frequency of the WTI have a significant impact on customer abandonment"; "when adjusting the initial WTI by one minute, it did not impact customer abandonment"; pessimistic 4 vs 2, 5 vs 3, 8 vs 5 min raise abandonment "by 6.2%, 14.1%, and 19.6%, respectively."
    - Relevance (O2/O3/O6): ride-hailing field evidence that (i) padding the first quote costs bookings beyond about 1 min, and (ii) **how often the shown time is updated matters by itself**. This is the strongest external hook for a "revision" or "change" metric. It concerns pre-match queue waits, not pooled drop-offs.
    - Status: VERIFIED-abstract.
11. **Wang, Singh & Zhang (2025), "A Mixed-Methods Study of Wait Time Perception and Discrepancy in Technology-Mediated Mobility Systems"**, PACM HCI 9(2). doi:10.1145/3710921
    - Quote: DiDi "(i) the promised wait time shown on its mobile app ... and (ii) the actual wait time"; "wait time discrepancy causes problems and negative emotions for passengers"; "large-scale ridesharing log data from over 36.6 million rides".
    - Relevance (O3): riders notice a gap between promised and actual time (pickup side).
    - Status: VERIFIED-abstract.
12. **Wang, Liu, Yang, Wang & Ye (2020), "Customer behavioural modelling of order cancellation in coupled ride-sourcing and taxi markets"**, TR-B 132:358–378. doi:10.1016/j.trb.2019.05.016
    - Quote: "a two-month, hourly average dataset of Didi Express in Shanghai"; "highlight the potential improvement of platform profit that can be achieved by appropriately designed penalty/compensation strategies."
    - Relevance (O2): links confirmed-order cancellation to platform profit and compensation design.
    - Status: VERIFIED-abstract.
13. **Rao, Griffis & Goldsby (2011), "Failure to deliver? Linking online order fulfillment glitches with future purchase behavior"**, J. Operations Management. doi:10.1016/j.jom.2011.04.001
    - Quote: "the relationship between an operations glitch (order fulfillment delay) and subsequent shopping behavior"; "order frequency and order size decrease, while customer anxiety level increases"; "online retailers need to deliver on order fulfillment promises".
    - Relevance (O2): a missed time promise lowers future demand from loyal customers (retail).
    - Status: VERIFIED-abstract.
14. **Suzuki (2000), "The relationship between on-time performance and airline market share: a new approach"**, TR-E 36(2):139–154. doi:10.1016/s1366-5545(99)00026-5 (DOI from OpenAlex; abstract from IDEAS https://ideas.repec.org/a/eee/transe/v36y2000i2p139-154.html)
    - Quote: "once experiencing flight delays, passengers are more likely to switch airlines"; "on-time performance affects a carrier's market share primarily through the passengers' experience, and not though the 'advertisement' of performance."
    - Relevance (O2/O3): reliability pays through each customer's own experienced lateness. That argues for per-rider guarantees, not fleet averages.
    - Status: VERIFIED-abstract.
15. **Suzuki, Tyworth & Novack (2001), "Airline market share and customer service quality: a reference-dependent model"**, TR-A 35(9):773–788. IDEAS https://ideas.repec.org/a/eee/transa/v35y2001i9p773-788.html
    - Quote: "the relationship is characterized by a non-smooth curve".
    - Relevance (O3): demand reacts to service quality non-smoothly around a reference point, consistent with a threshold-type promise.
    - Status: VERIFIED-abstract.
16. **Du, Fan & Chen (2023), "Implications of on-time delivery service with compensation for an online food delivery platform and a restaurant"**, Int. J. Production Economics 262. IDEAS https://ideas.repec.org/a/eee/proeco/v262y2023ics0925527323001287.html (DOI not checked)
    - Quote: "several online food delivery platforms have launched on-time delivery (OTD) services with compensation"; "the compensation fee and the probability of delivery delay are the key factors affecting the decisions of the platform".
    - Relevance (O2): an analytical model in which a lower **probability of breaking the promise** decides whether a paid guarantee is profitable. This is the direct business translation of rule C's reliability gain.
    - Status: VERIFIED-abstract.
17. **Salari, Liu & Shen (2022)**, MSOM, doi:10.1287/msom.2022.1081. Already in S2; one new verified fact:
    - Quote: "the proposed delivery time promise policy can improve the sales volume by 6.1% over the current policy" (simulation, JD.com data); "Simply overpromising or underpromising is undesirable because of the negative impacts on short-/long-term sales."
    - Status: VERIFIED-abstract.
18. **Sarkar & Comar (2025), "SPEEDY: Framework for Sharpening Promise Time Estimates in Sub-Same Day Delivery"**, ACM SIGSPATIAL, Amazon. doi:10.1145/3748636.3764604; https://www.amazon.science/publications/speedy-framework-for-sharpening-promise-time-estimates-in-sub-same-day-delivery
    - Quote: "predict narrower slots for 60%+ eligible orders"; "During a 21 day online A/B test, the treatment recorded a significant gain of +17 bps in units, +21 bps for views and +19 bps increase in search interactions".
    - Relevance (O6): narrower (sharper) promise windows raise demand measurably but modestly, in an Amazon A/B test.
    - Status: VERIFIED-abstract.
19. **Liu, He & Shen (2021), "On-Time Last-Mile Delivery: Order Assignment with Travel-Time Predictors"**, Management Science 67(7):4095–4119. doi:10.1287/mnsc.2020.3741
    - Quote: "improve the on-time performance of last-mile delivery services"; "integrates travel-time predictors with order-assignment optimization".
    - Relevance (O6, also b): on-time performance against a promise as the **assignment objective**. Precedent for making promise-keeping an optimization target.
    - Status: VERIFIED-abstract.
20. **Xu, Yan & Tong (2021), "Longer waiting, more cancellation?"**, J. Business Research 126:162–169. doi:10.1016/j.jbusres.2020.12.035
    - Quote: "consumers' longer waiting time for service production, but not for delivery, increases cancellation".
    - Relevance (O3): which phase of the wait drives cancellation is not obvious. Food delivery, so a caution against assuming every minute weighs the same.
    - Status: VERIFIED-abstract.
21. **Amorim, Eng-Larsson & Rooderkerk (2025)**, J. Retailing, doi:10.1016/j.jretai.2025.04.008.
    - Quote: "failures significantly delay the time to the next order by 7.22% on average".
    - Relevance (weak): the failures are stockouts and substitutions, not lateness. Cite only as adjacent.
    - Status: VERIFIED-abstract.

### a3. What riders value: value of reliability and attitudes

22. **Klinkhardt, Kandler, Kagerbauer & Vortisch (2026), "Reliability of Public Transportation Systems with Autonomous First-/Last-Mile Services in a Stated Mode Choice Experiment"**, Transportation Research Procedia 97:744–753. doi:10.1016/j.trpro.2026.04.212 (open access PDF via KIT)
    - Quote: "net sample of 859 respondents"; "the mean delay rated 3.7 times more negatively than travel time itself"; "For on-demand services, the study indicates that displaying slightly longer expected travel times with early arrivals is preferable to promising shorter times that result in delays."
    - Relevance (O3): direct support for **forecast or padded quotes in on-demand service** and for measuring lateness against the shown promise. Stated preference, Germany, public transport plus shuttles.
    - Status: VERIFIED-full.
23. **Bailey (2022), "Dynamic Ridesharing under Travel Time Uncertainty: Passenger Preference and Optimal Assignment Methods"**, MIT PhD thesis (advisor J. Zhao). https://dspace.mit.edu/handle/1721.1/144538
    - Quote: survey of "1,600 Singapore residents"; "travelers' decisions to use DRS are driven much more by their attitudes towards time uncertainty"; "passengers' lack of trust in DRS reliability is a significant barrier to greater adoption and use"; the proposed assignment method reduces "average passenger delay and the variance of passenger arrival times."
    - Relevance (O3/O6): reliability trust is a pooled-ride adoption barrier, and arrival-time variance can be an optimization target.
    - Status: VERIFIED-page (abstract on DSpace).
24. **Kucharski, Fielbaum, Alonso-Mora & Cats (2021), "If you are late, everyone is late"**, Transportmetrica A 17(4):1077–1100. doi:10.1080/23249935.2020.1829170
    - Quote: "when lateness increases passengers refrain from sharing and eventually opt-out."
    - Relevance (O3): in pooling, unreliability feeds back into demand. Here the lateness is passengers', not traffic or dispatch.
    - Status: VERIFIED-abstract.
25. **Watkins, Ferris, Borning, Rutherford & Layton (2011), "Where Is My Bus?"**, TR-A 45(8):839–848. doi:10.1016/j.tra.2011.06.010
    - Quote: "The addition of real-time information decreases the perceived wait time by 0.7 min (about 13%)"; "mobile real-time information reduces not only the perceived wait time, but also the actual wait time".
    - Relevance (O3): honest live information has its own value. Do not argue that never updating is optimal.
    - Status: VERIFIED-abstract.
26. **Carrión & Levinson (2012), "Value of travel time reliability: A review of current evidence"**, TR-A 46(4):720–741. doi:10.1016/j.tra.2012.01.003
    - Quote: "a meta-analysis is performed in order to determine the reasons behind the discrepancy among the reliability estimates."
    - No ratio values were seen.
    - Status: VERIFIED-abstract.
27. **Li, Hensher & Rose (2010)**, TR-E 46(3):384–403. doi:10.1016/j.tre.2009.12.005
    - Quote: they "derive values of reliability, scheduling costs and reliability ratios"; "the important influence of the way that trip time variability is included in stated preference studies".
    - Status: VERIFIED-abstract (no numbers).
28. **Transport Scotland, "Improving the evidence base on journey time reliability on the Trunk Road Network in Scotland"** (undated). https://www.transport.gov.scot/publication/improving-the-evidence-base-on-journey-time-reliability-on-the-trunk-road-network-in-scotland/j375468-09
    - Quote: "STAG should recommend the use of the central value found in the literature, taken to be 0.8"; "together with a lower value, 0.4, closer to the value found in the NF survey, 0.3."
    - Relevance (O3): an appraisal reliability ratio for car trips. Together with Alonso-González 2020 (about 0.5, pooled, in S3) and Klinkhardt (3.7 for mean delay, public transport), the plausible range is wide. Do not cite a single number for riders.
    - Status: VERIFIED-page.

---

## (b) Research that treats promise stability, consistency or commitment as an objective or constraint

29. **Hörl & Zwick (2022), "Traffic Uncertainty in On-Demand High-Capacity Ride-Pooling"**, TRB 2022. doi:10.3929/ethz-b-000561639; https://www.moia.io/mobility_analytics/studies/2201_Traffic_uncertainty_in_ride-pooling.pdf
    - I re-extracted the strategy text today. Quote (p.7): strategy (B) "calculate an updated drop-off time ... which is used instead of the latest drop-off time for on-board requests that would otherwise violate their constraints. Effectively, this means that the algorithm is allowed to construct routes in which new pick-up tasks are added to a vehicle as long as the on-board requests are not dropped off later than what is the absolute minimum, given current traffic conditions. To favor feasible solutions, a penalty is added for every second of violating a drop-off constraint."
    - Formally (p.8): t_required = max(t_updated, t_latest).
    - Traffic split: yes, implicitly. Traffic moves t_updated, and dispatch is not allowed to add to it for at-risk riders only. For other riders the binding constraint is the original latest drop-off (deadline type).
    - What it lacks relative to rule C: no per-rider cumulative budget, no ledger, and a soft penalty rather than a hard cap.
    - Relevance: still the **closest published algorithm to rule C**.
    - Status: VERIFIED-full.
30. **Laupichler, Andre, Kandler, Sanders & Vortisch (2026), "Advancing Dynamic Ride-Pooling Simulation – A Highly Scalable Dispatcher" (Mt-KaRRi)**, arXiv:2605.11798 (12 May 2026).
    - Quotes:
      - p.~6: "every rider is guaranteed a latest possible arrival time relative to the trip time they originally accepted"; "we use constraints relative to the pickup time and trip time of the accepted ride, which ensures that some detours are always possible".
      - Appendix B: "We choose to use [α] = 1.4 and [β] = 10min"; "A value of max wait = 0 ... makes too many insertions infeasible, and we actually see longer wait times and a slightly smaller modal share"; "We choose [max wait] = 10min".
      - Results: "almost two thirds of rides experience additional detours that are not expected at the time of accepting the ride offer" (urban-rural and rural-urban categories); "in about 90% of all rides, the additional detour stays below half the direct car travel time"; "Our mode choice model ignores wait times and ride detours added after accepting a ride, but riders would come to expect the additional inconvenience in a production system."
    - What it is: a **2026 accepted-offer-relative, proportional deadline** (α·t_accepted + β). It counts all changes, is not cumulative over |c|, and has no traffic split (none seen in the passages read).
    - Relevance (O2/O4): it narrows "bound relative to the first accepted offer" further as prior art. It also shows that **at city scale, post-acceptance additions are common**, which answers the fact pack's worry that accumulation is rarely exercised in our 108-request cells.
    - Status: VERIFIED-full.
31. **Schmidt, Golak, Schulz & Fliedner (2026), "Optimal Service Commitments in Traveling Salesman Problems with Stochastic Demand"**, arXiv:2609.11950. The abstract is in S2; new full-text facts:
    - Quotes:
      - Intro: the expected arrival time "together with the price of the trip -- is the customer's primary basis for accepting and rejecting the offered ride"; the problem "has not gathered much attention".
      - Conclusion: "the revenue-maximizing policy settles into a regime in which the provider turns away roughly one in three accepting customers"; "pushing beyond roughly 80-90% service, however, becomes disproportionately costly"; "dynamic settings with sequentially arriving requests and personalized commitments are natural extensions."
    - Relevance (O2): researchers in the field explicitly name **dynamic, personalized commitments** as an open extension. This is evidence that "others would want to optimize it".
    - Status: VERIFIED-full.
32. **Kovacs, Golden, Hartl & Parragh (2014), "Vehicle routing problems in which consistency considerations are important: A survey"**, Networks 64(3):192–213. doi:10.1002/net.21565 (owner-supplied)
    - Quote: "Customers appreciate service at regular times of the day provided by the same driver each time"; three features: "arrival time consistency, person-oriented consistency, and delivery consistency"; they "examine the increase in cost of improving service consistency."
    - Relevance (O2): consistency costs are a recognized research objective, measured across days rather than within a trip. Already bounded by Tellez TC-DARP in docs/03.
    - Status: VERIFIED-abstract.
33. **Sridharan, Berry & Udayabhanu (1987), "Freezing the Master Production Schedule Under Rolling Planning Horizons"**, Management Science 33(9). doi:10.1287/mnsc.33.9.1137. Likely the owner's "FreezingtheMPS" PDF (not opened).
    - Quote: "While freezing the MPS can limit the number of schedule changes, it can also produce an increase in production and inventory costs"; "freezing up to 50% of the planning horizon has a marginal effect on production and inventory cost under a wide range of operating conditions."
    - Relevance (O2/O6): the classic **stability-vs-cost** result. It parallels "C-30 costs 2.6 pp of requests".
    - Status: VERIFIED-abstract.
34. **Sridharan, Berry & Udayabhanu (1988), "Measuring Master Production Schedule Stability Under Rolling Planning Horizons"**, Decision Sciences. doi:10.1111/j.1540-5915.1988.tb00259.x
    - Quote: "This paper is concerned with the problem of measuring MPS stability".
    - Relevance: a precedent for a dedicated *instability* metric under rolling re-planning, the analogue of the per-rider S = Σ|c|. Not novel as a metric family.
    - Status: VERIFIED-abstract.
35. **Bent & Van Hentenryck, "The price of commitment in online stochastic vehicle routing"**. OSTI biblio 956696 (https://www.osti.gov/biblio/956696); OpenAlex lists 2009 (UNT record).
    - Quote: "Motivated by real applications that require stability in the decision making"; "this constraint severely degrades the performance of existing algorithms"; "resource augmentation quantifies precisely the cost of commitment".
    - Relevance (O6): a method precedent to **price** C-30 in fleet units ("how many extra vehicles make C-30 cost-free?").
    - Status: VERIFIED-abstract.
36. **Vareias, Repoussis & Tarantilis, "Assessing Customer Service Reliability in Route Planning with Self-Imposed Time Windows and Stochastic Travel Times"**, Transportation Science. doi:10.1287/trsc.2017.0748 (OpenAlex year 2017)
    - Quote: "chance constraints to model the probability of serving each customer within the assigned time window"; "to study the trade-off between service reliability and routing costs".
    - Relevance (O6): the operator **chooses the promise window** under stochastic travel times and reports reliability-vs-cost trade-offs. Static, no dispatch-change budget.
    - Status: VERIFIED-abstract.
37. **Jabali, Leus, Van Woensel & de Kok, "Self-imposed time windows in vehicle routing problems"**, OR Spectrum. doi:10.1007/s00291-013-0348-1
    - Status: UNVERIFIED (title and metadata only; no abstract retrieved).
38. **Ardali & Knapp (2026), "Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer–DRL and Rolling-Horizon Benchmarking"**, arXiv:2608.13799.
    - Quote: "fixed-prefix/flexible-suffix route commitments protect completed, active, and near-term decisions"; they "separately measure vehicle reassignment and resequencing"; "No single method was best across routing efficiency, service responsiveness, stability, and online computation."
    - Relevance: 2026 work reports **stability as a separate evaluation axis**. Supports reporting C's trade-off as a multi-axis frontier.
    - Status: VERIFIED-page (abstract).
39. **Çelik, ERIM seminar "Advancing time window assignment and vehicle routing in last-mile logistics"**, 20 Feb 2026. https://esb.nu/agenda/erim-seminar-advancing-time-window-assignment-and-vehicle-routing-inlast-mile-logistics/
    - Quote: providers "must decide when to communicate commitments"; "Early commitments can improve customer experience but restrict routing flexibility"; "delayed communication allows for more efficient planning but risks frustrating customers."
    - Relevance (O6): the commitment-timing trade-off is an active 2026 topic.
    - Status: VERIFIED-page (seminar abstract only).
40. **TCRP Synthesis 168 (2023), "Dynamic Optimization on ADA Paratransit Service"** (Texas A&M TI for TRB). TRID https://trid.trb.org/View/1854186
    - Quote: optimization "results in improving the efficiency of the route schedule and the overall productivity of the on-demand service" "without affecting the customer's confirmed pickup time window."
    - Relevance (O2): in practice, agencies run continuous re-optimization **under a promise-preserving invariant**. This is the industrial analogue of "C with B = 0 on a wide window".
    - Status: VERIFIED-page (TRID abstract; report not read).
41. **Liu, He & Shen (2021)**, item 19: on-time performance as the assignment objective. **Mao et al. (2025)** (already in business-need Q1-5): dispatch that maximizes future orders beats minimizing delay.
42. **Patents** (descriptions grepped from Google Patents HTML; claims not analysed).
    - **Lyft, US12182741B2 "Systems and methods for enhanced transportation dispatch"** (application filed by Lyft Inc; priority 2020-06-05 per page). https://patents.google.com/patent/US12182741B2/en
      - Quote: "Applying and enforcing these constraints may result in a more predictable ride experience"; the system "may reject matches that would add a detour greater than X minutes (e.g., 5 minutes), or may reject matches that would increase the pickup ETA by more than Y minutes (e.g., 7 minutes), and/or may reject matches that would increase an ETA ratio (i.e., the remaining ETA minutes in a ride over the total ETA minutes initially quoted ...) by Z (e.g., by a ratio of 0.25)."
      - Relevance (novelty): a **per-match limit relative to the initially quoted ETA, inside a special "predictable" ride mode**. That is prior art for (i) tier-specific promise constraints and (ii) proportional (ratio) limits. No cumulative budget and no traffic split seen.
      - Status: VERIFIED-full (curl + grep of the description).
    - **Transit Labs, US10248913B1 "Systems, devices, and methods for searching and booking ride-shared trips"** (priority 2016-01-13; granted 2019-04-02). https://patents.google.com/patent/US10248913B1/en
      - Quote: "a plurality of relative delay tolerance metrics, each reflective of tolerance for delay caused by ride-sharing of a particular passenger"; "based on traffic conditions or delays by other passengers, the estimated or real drop-off time may be 9:10, which would result in a drop-off time violation of 10 minutes"; "Summed drop-off time violation is defined as the sum of each trip/individual's violation of drop-off time".
      - Relevance (novelty): a per-passenger tolerance, with **traffic and co-rider causes lumped together**. Not a cumulative dispatch-only budget.
      - Status: VERIFIED-full (curl + grep).
    - **Via, US11674811B2** (already in docs/03; filed 2020-07-02).
      - Quote: "If the estimated delay that may occur to the user is more than ten minutes, ridesharing management server 150 may assign the subsequent ride request to other available vehicles."
      - Relevance: a per-insertion threshold.
      - Status: VERIFIED-full (grep).

---

## (c) Alternative promise forms and how customers respond

### c1. Window and precision promises
43. **Amorim, DeHoratius, Eng-Larsson & Martins (2024), "Customer Preferences for Delivery Service Attributes in Attended Home Delivery"**, Management Science. doi:10.1287/mnsc.2020.01274
    - Quote: "precision as the duration of the offered time slot"; "precision and timing are also key drivers of the customer's time slot selection process"; "substantial customer heterogeneity in the willingness of customers to pay"; tailoring slots can "generate approximately 9% more shipping revenue".
    - Relevance (O6): **the best field evidence that a narrower promise is a priced attribute**, with heterogeneous willingness to pay. It argues for a promise menu or tiers.
    - Status: VERIFIED-abstract.
44. **SPEEDY (Amazon, 2025)**, item 18: narrower windows give +17 bps units in an A/B test. VERIFIED-abstract.
45. **Sivagnanam, Kadir, Mukhopadhyay, Pugliese, Dubey, Samaranayake & Laszka (2022), "Offline Vehicle Routing Problem with Online Bookings"**, IJCAI-22. https://www.ijcai.org/proceedings/2022/0546.pdf
    - Quote: "booking trips with flexible pickup windows (e.g., 3 hours) in advance (e.g., the day before) and confirming tight pickup windows (e.g., 30 minutes) at the time of booking"; passengers "do strongly prefer to know in advance when they will be picked up".
    - Relevance (O6): selecting the promised window online is an established, implementable optimization problem (paratransit, pickup side).
    - Status: VERIFIED-full (first page).
46. **Bharti, Bekker, Levering & Mandjes (2026), "A framework for window design in delivery schedules"**, arXiv:2601.19601.
    - Quote: customers are "promised a time window in which the provider will arrive"; windows are revised "only when the remaining time until the window's start falls below a predefined threshold"; "communication-efficient scheduling while substantially improving delivery accuracy".
    - Relevance (O6): a **revision-limited window promise** (threshold rule). Close in spirit to a revision budget, but the trigger is time to window, not cumulative change.
    - Status: VERIFIED-page (abstract).
47. **Song, Li, Chung & Ye (2025), "Balancing Confidence and Precision: ... Bus Arrival Time Prediction with Uncertainty Quantification" (UncertBAT)**, hEART 2025. https://transp-or.epfl.ch/heart/2025/abstracts/hEART_2025_shortpaper_176.pdf
    - Quote: "provides not only the predicted BAT but also an arrival time window with a high degree of confidence. The model incorporates conformalized quantile regression and a grouping calibration mechanism".
    - Relevance (O6): a **conformal arrival-window promise** exists for buses. I found no conformal ETA paper for ride-pooling.
    - Status: VERIFIED-full (abstract and intro).
48. **Mao et al. (2024/2025), "DutyTTE"**, arXiv:2408.12809.
    - Quote: "Uncertainty quantification in travel time estimation (TTE) aims to estimate the confidence interval for travel time"; calibration with "Hoeffding's upper-confidence bound".
    - Relevance: interval travel-time estimation; not conformal.
    - Status: VERIFIED-page (abstract).

### c2. How people read intervals and probabilistic forecasts
49. **Joslyn & LeClerc (2012; OpenAlex year 2011), "Uncertainty forecasts improve weather-related decisions and attenuate the effects of forecast error"**, J. Exp. Psych.: Applied. doi:10.1037/a0025185
    - Quote: "uncertainty information improved decision quality overall and increased trust in the forecast"; "When error in the forecast increased, participants with conventional forecasts were reluctant to act. However, this effect was attenuated by uncertainty forecasts."
    - Relevance (O6): supports showing a range or probability rather than a single point.
    - Status: VERIFIED-abstract.
50. **Du, Budescu, Shelly & Omer (2011), "The appeal of vague financial forecasts"**, OBHDP 114(2):179–189. doi:10.1016/j.obhdp.2010.10.005
    - Quote: "the preference for (im)precision is non-monotonic - it peaks for low levels of imprecision and diminishes when the range gets wider"; people "favor forecasts that are as precise as warranted by the information available, but not more precise."
    - Relevance (O6): narrow ranges beat both point estimates and wide ranges. Fits a minute-scale window.
    - Status: VERIFIED-abstract.
51. **Løhre & Teigen (2017), "Probabilities Associated with Precise and Vague Forecasts"**, J. Behavioral Decision Making. doi:10.1002/bdm.2021
    - Quote: "people often trust precise forecasts more than vague forecasts"; two readings, "distributional (wide intervals seen as more probable than narrow intervals) and associative (wide intervals seen as more uncertain than narrow intervals)".
    - Relevance: a caution that wide windows can read as incompetence.
    - Status: VERIFIED-abstract.
52. **Yaniv & Foster (1995), "Graininess of judgment under uncertainty: An accuracy-informativeness trade-off"**, J. Exp. Psych.: General 124(4). doi:10.1037/0096-3445.124.4.424
    - Status: UNVERIFIED (title only; cited by UncertBAT for the confidence-precision trade-off).

### c3. Revision and notification design
53. **Yu, Zhang & Zhou (2022)**, item 10: update frequency itself affects abandonment, and a ±1 min initial change had no effect because the two effects cancel. VERIFIED-abstract.
54. **Allon, Bassamboo & Gurvich (2011), "We Will Be Right with You: Managing Customer Expectations with Vague Promises and Cheap Talk"**, Operations Research 59(6):1382–1394. doi:10.1287/opre.1110.0976
    - Quote: "even though the information provided to customers is nonverifiable, it improves the profits of the firm and the expected utility of the customers"; "firms may choose to shade some of the truth by using intentional vagueness to lure customers."
    - Relevance (O6): theory of announcement design. A coarse, credible promise can beat a precise one.
    - Status: VERIFIED-abstract.
55. **Ibrahim (2018), "Sharing delay information in service systems: a literature survey"**, Queueing Systems. doi:10.1007/s11134-018-9577-y
    - Quote: "Service providers routinely share information about upcoming waiting times with their customers, through delay announcements."
    - Relevance: the entry point to the delay-announcement literature.
    - Status: VERIFIED-abstract.
56. **Industry notification caps.** OptimoRoute ("Maximum notifications per order") and Mobilus (re-notify only if the ETA moves by more than 10 min).
    - Status: UNVERIFIED (blocked, 403). Do not cite; at most "industry tools reportedly cap re-notifications".

### c4. Tiered products and promise menus
57. **MOIA Express** (ride-pooling, Hamburg/Hannover). https://ride.moia.io/en/express
    - Quote: "an optional upgrade to your ride"; "We will give you a shorter arrival window before you book."; "We take a more direct route to your destination."
    - Relevance (O6): **a live ride-pooling operator sells a tighter arrival promise as a paid tier.** This is the single most direct precedent for a "promise tier" storyline.
    - Status: VERIFIED-page.
58. **MOIA standard booking.** https://ride.moia.io/en
    - Quote: "up to six different offers, including price, pickup and arrival time"; "you can place a binding booking".
    - Relevance (O6): **a promise menu already exists in pooling.** Each offer carries an arrival time.
    - Status: VERIFIED-page.
59. **Lyft Priority Pickup / Wait & Save.** https://www.lyft.com/business/resources/product-updates/introducing-3-new-ride-options
    - Quote: "Upgrade to Priority Pickup for a faster pickup when you're in a hurry."; "Wait & Save availability depends on how many drivers are nearby."
    - Status: VERIFIED-page (undated).
    - A Jan 2026 Law360 report says a proposed class action alleges Lyft "frequently fails to deliver" the faster pickup. UNVERIFIED (snippet only, paywalled).
60. **Uber Priority (India)**, Uber blog, 28 May 2025. https://www.uber.com/en-IN/blog/uber-priority-rides-during-peak-hours
    - Quote: "Uber Priority moves you ahead in the driver queue to help you get picked up faster"; "Slightly higher fare than Uber Go in exchange for speed and reduced wait time"; "it's not guaranteed every time."
    - Relevance (O6): a paid speed tier with **no** guarantee. That contrasts with MOIA Express, whose upgrade is a tighter promise.
    - Status: VERIFIED-page.
61. **Lyft US12182741B2 "ephemeral ride mode"**, item 42: a tier defined by tighter constraints relative to the initially quoted ETA. VERIFIED-full.

### c5. Pickup-only vs drop-off promises
- Every compensated rider-facing guarantee found is pickup-side (Lyft, Uber Reserve) or delivery-side (Uber One), with one exception: the **2016 UberPOOL "Arrive by"** (item 3).
- Current UberX Share disclaims arrival times "because of traffic and other possible delays" (item 4).
- Paratransit confirms pickup windows (items 40, 45).
- So a **drop-off** promise in pooling is the uncommon, harder form. That is a gap, but also a sign operators avoid it.

---

## (d) Algorithm-optimization directions linked to promise reliability (3–4 weeks on an insertion dispatcher)

For each direction: closest papers, and whether a per-rider cumulative budget on system-caused changes (rule C) appears.

| # | Direction (tie to promise) | Closest sources (this file and prior) | Rule C present? | Undergrad feasibility |
|---|---|---|---|---|
| D1 | **Tier-specific budgets** ("Express" riders B = 0–30 s with a tight quote; "standard" riders a larger B or deadline). Trade-off: served and shared rides vs late-vs-promise per tier. | MOIA Express (57); Lyft ephemeral mode (42); Amorim 2024 willingness-to-pay heterogeneity (43); SPEEDY (18) | No. Lyft has per-match, initial-quote-relative limits per tier; MOIA's algorithm is not public. | T2: rider attribute plus per-rider B already fits rule C. Few days of code, then T1 runs. |
| D2 | **Proportional budget** B_i = κ·t_direct,i (+β), at equal mean B. | Mt-KaRRi α·t_accepted + β (30); Lyft ETA ratio 0.25 (42); Lu & Kühnel λt + γ (S3); internal screen (fact pack §1: 60 s unblocks 11 → 30) | No. Ratio and deadline forms exist; a cumulative dispatch-only form was not found. **Do not claim proportionality as new.** | T2, small. |
| D3 | **Soft, budget-aware insertion cost**: add a penalty w·(c_i / remaining B_i) instead of only a hard cap, and sweep w. | Hörl & Zwick per-second penalty (29); soft time-window literature; price of commitment (35) | Hörl & Zwick: a per-epoch penalty for at-risk riders, not cumulative. | T2, small; gives a smooth frontier instead of one point. |
| D4 | **Price C in fleet units** (resource augmentation): how many extra vehicles make C-30 serve as many riders as U? | Bent & Van Hentenryck (35); Sridharan freezing cost (33) | n/a (evaluation method) | T1 (config only). Business-legible: "C-30 costs X vehicles". |
| D5 | **Quote design**: forecast or quantile quote vs padded latest time vs tight point. Rider metric: late-vs-first-promise; booking-side cost: quote length. | Klinkhardt (22); UberPOOL "absolute latest time" (3); Yu et al. (10); Cui et al. (9); Salari (17); S2 directions A/B | n/a (display layer) | Mostly T0/T1 with existing forecast layer. |
| D6 | **Revision-limited promises**: count revisions per rider, deadband re-display (show a new time only if it moves more than d s), or threshold-in-time rules. | Yu et al. update-frequency effect (10); Bharti et al. 2026 (46); Sridharan 1988 stability metric (34) | No. Revision counts are measured, but no cumulative per-rider cap on dispatch changes was found. | T0 (re-analyse transcripts) or T2 (display rule only). |
| D7 | **Matching timing / batching** to reduce post-acceptance insertions. | Bao et al. 2026 TR-C, doi:10.1016/j.trc.2026.105644: "reduces total waiting time by 3.1% in ride-hailing and 20.1% in ride-pooling, and detour delay by 36.1% in pooling" (VERIFIED-abstract) | No. | T2, medium; the promise link is indirect. **Lower priority.** |
| D8 | **Early, honest rejection** (state C's rejections at request time, not later). | Dandl, Engelhardt & Bogenberger 2021 ITSC, doi:10.1109/itsc48978.2021.9564918: an operator "can communicate a rejection to users after the first iteration" (VERIFIED-abstract); Schmidt et al. 1-in-3 rejection optimum (31) | No. | Probably already true in our runner (immediate decision); a reporting point only. |
| D9 | **Variance-reducing assignment or stop pooling**. | Bailey 2022 (23); Lotze, Marszal, Schröder & Timme 2024 J. Phys. Complexity, doi:10.1088/2632-072x/ad370a: "travel time fluctuations may be drastically reduced by stop pooling" (VERIFIED-abstract) | No. | Stop pooling needs a network change (T3). **Not recommended.** |
| D10 | **Anticipatory rebalancing**. | Wang & Fielbaum 2026 TR-C, doi:10.1016/j.trc.2026.105898: "reducing both rejection rates and user costs" (VERIFIED-abstract) | No. | Could recover riders C rejects, but needs demand learning (T3). **Not recommended in 5 weeks.** |

Two items seen but not used:
- Sundt et al. (arXiv 2107.11318): "individual customers may experience substantial service quality degradation" under throughput-maximizing pooling (VERIFIED-abstract). It is a general motivation only.
- Hu et al. 2026 (arXiv 2607.24336), "Unequal Trips, Unequal Places": "pervasive trip-length inequity" in fleet delay, with a method that "explicitly bounds online route updates" (VERIFIED-page, abstract). Possibly useful for justifying D2 on fairness grounds; not read beyond the abstract.

**Rule C novelty check (2024–2026 emphasis).**
- No source found applies a **per-rider, cumulative bound on system-caused (dispatch) promise changes, separated from traffic, with a per-rider ledger**.
- Closest items, nearest first:
  1. Hörl & Zwick 2022 strategy B (29): traffic-separated, zero extra dispatch delay, but only for at-risk riders, per epoch, and with a soft penalty.
  2. UberX Share product statement (4): the same split stated as a product goal, with the algorithm undisclosed.
  3. Lyft US12182741B2 (42): per-match limits relative to the initially quoted ETA, including a ratio, in a "predictable" tier.
  4. Mt-KaRRi 2026 (30): a proportional deadline relative to the accepted offer.
  5. Transit Labs patent (42): per-passenger tolerance, with traffic and co-riders lumped together.
  6. Schulz & Pfeiffer 2026 and the Via patent: already in the boundary.
- Nothing found is closer than Hörl & Zwick B in algorithmic form. The **concept** "pooling must not push your ETA, traffic is excused" is publicly stated by Uber.

---

## Synthesis (15 bullets)

1. **Operators already pay for broken time promises.** Examples: Lyft airport pickups, $15–$100 (1); Uber Reserve, $50 (2); UberPOOL in 2016, $2 (3); Uber One, $5 (5); UK rail Delay Repay, 25% (6). A lower probability of breaking a promise directly lowers the cost of such a guarantee (16). This is the cleanest O2 business answer for rule C: it makes a **drop-off guarantee for pooled riders affordable to offer**. It is not "C improves revenue" by itself.
2. **Aggressive promises buy conversion and cost retention.** Shown causally by Cui et al. (9). Missed promises reduce future purchases (13, Mao et al. in prior SOURCES). Airline delays cause switching through each customer's own experience (14). So the operator gains from **per-rider** reliability, the level at which rule C works.
3. **Ride-hailing field evidence:** padding the initial wait by more than 1 min raises abandonment by 6.2–19.6%, and the update frequency of the shown time matters independently (10). So the rule-C-plus-forecast design (quote only about 7–14 s longer, few revisions) sits in the region that the experiment suggests is cheap.
4. **Uber states rule C's split as a product goal.** UberX Share aims that "additional pickups won't increase your estimated arrival time" and disclaims arrival times "because of traffic" (4). Uber also excludes Matched Share rides from its Delayed Ride Guarantee (S3). Industry therefore wants the property but **does not guarantee pooled drop-offs today**. That is a business gap rule C can address, and also a reason not to claim the concept as new.
5. **What riders value is lateness against the shown time, not the size of the internal change S.**
   - Mean delay is valued 3.7× travel time in public transport and on-demand shuttles (22).
   - Riders prefer a slightly longer quote with early arrival (22).
   - Lack of reliability trust is a pooled-ride adoption barrier (23).
   - Lateness pushes riders out of sharing (24).
   - **For O3:** present S = Σ|c| as the operator's control and audit quantity. Present late-vs-first-promise (8.34% → 3.25% → 0.43% in the fact pack) as the rider outcome.
6. **Reliability ratios vary too much to monetize S:** about 0.5 for pooled services (S3), 0.3–0.8 for car appraisal (28), 3.7 for public-transport delay (22). Report ranges only, never one euro value.
7. **Others would want to optimize it.**
   - Schmidt et al. 2026 call "dynamic settings with sequentially arriving requests and personalized commitments" a natural extension (31).
   - Commitment timing is an active 2026 topic (39).
   - 2026 routing benchmarks report stability as its own axis (38).
   - The stability-vs-cost question has a long history (33–35).
   - So "a per-rider commitment budget with a measured frontier" is a recognisable research object. The defensible claim is the narrow integration, not the idea of commitment.
8. **Scale matters for the cumulative part.** At city scale, Mt-KaRRi reports that in urban-rural and rural-urban trips "almost two thirds of rides experience additional detours not expected at the time of accepting" (30). This counters the fact-pack worry that accumulation is rarely exercised: it is rare in **our** 0.54-riders-per-vehicle cells, not in dense pooling. A denser regime (S3) is needed before claiming anything about accumulation.
9. **Best-evidenced alternative promise form: a precision tier or menu.**
   - Customers value narrower windows and their willingness to pay varies (about +9% shipping revenue from tailoring) (43).
   - Amazon's sharper windows gained +17 bps in units (18).
   - **MOIA already sells a shorter arrival window as a paid ride-pooling upgrade** (57) and offers up to six offers with arrival times (58).
   - This is the strongest O6 lead: "rule C with tier-specific budgets" (D1) turns the thesis into "which riders get which promise at what fleet cost".
10. **Interval and probabilistic promises have lab evidence but mixed perception.** Uncertainty information improves decisions and trust (49). Moderately narrow ranges are preferred over points and wide ranges (50). But wide intervals can read as uncertainty (51). Conformal arrival windows exist for buses (47), and I found none for ride-pooling ETA. This is a promising display variant, not a better storyline on its own evidence.
11. **Guaranteed arrival with compensation** is widespread for pickup and delivery, rare for pooled drop-off (only UberPOOL 2016). In pooling it was implemented by quoting the "absolute latest time" (3), the padding corner that our data show makes 97–99.5% of riders arrive more than 1 min early. Rule C plus forecast is a way to offer such a guarantee **without** heavy padding. That is a usable framing, not a novelty claim.
12. **Revision and notification budgets** are supported by the update-frequency effect (10), threshold-revision windows (46) and MPS stability metrics (34). Industry notification caps are UNVERIFIED (56). A deadband display rule is a cheap add-on (D6), not a thesis core.
13. **Undergraduate-feasible optimizations with a measurable trade-off, in order:**
    - D1, tier-specific B: served or shared vs late per tier.
    - D2, proportional B: rejections vs fairness, at equal mean B.
    - D3, soft budget penalty: a smooth frontier.
    - D4, price C in vehicles: business-legible.
    - D7–D10 are weaker links to promises or need T3 work.
14. **Novelty threats to rule C, closest first:**
    - Hörl & Zwick 2022 B: algorithmic, traffic-separated, not cumulative.
    - The UberX Share product statement: conceptual.
    - Lyft US12182741B2: per-match, initial-quote-relative ratio limits in a "predictable" tier. This **threatens claims about proportional or tiered limits**, less so the cumulative ledger.
    - Mt-KaRRi 2026: accepted-offer-relative proportional deadline.
    - The Transit Labs patent: per-passenger tolerance, causes lumped together.
    - Nothing found states a cumulative per-rider |c| budget with a v/e/p ledger. Patents were read from their descriptions, not their claims.
15. **Recommendation for the debate (my reading, not a source claim).** Keep the current storyline (rule C plus forecast, rider metric = late vs first promise) and **reframe the business value as "makes a pooled drop-off guarantee or promise tier affordable"**. Use the Lyft/Uber/MOIA precedents and the Du et al. model as anchors.
    - If one algorithmic extension is added, D1 (tier-specific budgets) has the best external evidence (43, 57, 18) and reuses rule C directly.
    - Its novelty must be stated as an *evaluation* of tiers under a cumulative dispatch budget, not as tiered promises themselves, because Lyft and MOIA precede it.
