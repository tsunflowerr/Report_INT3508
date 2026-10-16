// Research fixture only: all route generation, schedules and commitment validation
// call the existing RideBound assemblies. No dispatcher or simulator is implemented.
using System.Security.Cryptography;
using System.Text.Json;
using RideBound.Algorithms.Candidates;
using RideBound.Algorithms.Commitments;
using RideBound.Application.Commitments;
using RideBound.Application.State;
using RideBound.Application.Travel;
using RideBound.Domain.Commitments;
using RideBound.Domain.Common;
using RideBound.Domain.Requests;
using RideBound.Domain.Routes;
using RideBound.Domain.Runs;
using RideBound.Domain.Validation;
using RideBound.Domain.Vehicles;

var output = args.Length > 0 ? args[0] : "core-probe.json";
var nodes = Enumerable.Range(0, 5).Select(i => new NodeId($"node-{i}")).ToArray();
var vehicleId = new VehicleId("vehicle-1");
var clock = new SimTime(1000);
var generator = new InsertionCandidateGenerator();
var validator = new CommitmentDecisionValidator();
var assessor = new HardVectorCandidateAssessor();
var results = new List<object>();

// Parameter sweep is a mechanism witness search, not a performance experiment.
foreach (long budget in new long[] {1000, 2000, 4000, 8000})
foreach (int qFrom in Enumerable.Range(0,5))
foreach (int qTo in Enumerable.Range(0,5).Where(i => i != qFrom))
{
    var policy = new CommitmentPolicy("probe-policy", CommitmentBudgetBasis.DecisionInduced,
        CommitmentDimensionVocabulary.Ordered.Select(d => new CommitmentDimensionLimit(d,
            d is CommitmentDimension.PickupEtaTotalMs or CommitmentDimension.DropEtaTotalMs
                ? budget
                : d is CommitmentDimension.VehicleSwitchCount or CommitmentDimension.PickupStopSwitchCount
                    or CommitmentDimension.DropStopSwitchCount ? 0L : null,
            CommitmentPhase.AllActive)), new MaterialRevisionRule(1000, null));
    var policies = new CommitmentPolicyCatalog([policy]);
    var arcs = (from i in Enumerable.Range(0,5) from j in Enumerable.Range(0,5) where i != j
                select new KeyValuePair<TravelArc, Duration>(new TravelArc(nodes[i],nodes[j]),
                    new Duration(Math.Abs(i-j)*1000))).ToArray();
    var travel = TravelTimeSnapshot.Create(1, new string('a',64), arcs).Value!;
    var route = RoutePlan.Create(new PlanVersion(0), 0, [], []).Value!;
    var vehicle = VehicleState.Create(vehicleId, 3, 0, new NodePosition(nodes[0]), [], [], route, 1).Value!;
    var run = RideBoundRun.Create(new RunIdentifier("probe-run"),new ScenarioIdentifier("probe-scenario"),clock);
    run = run.BootstrapVehicle(vehicle).Value!;
    var initial = new OnlineState(run,travel,1,travel.SnapshotHash,CommitmentLedger.Empty);
    var incumbent = Request("incumbent",1,3,6000);
    var reduced1 = Add(initial, incumbent);
    var first = Candidates(initial,reduced1,policies).Single(x => x.NewRequestIds.Count == 1);
    var committed1 = Commit(initial,reduced1,first,policies);
    var q = Request("current",qFrom,qTo,6000);
    var reduced2 = Add(committed1,q);
    var candidates = Candidates(committed1,reduced2,policies).Where(c => c.NewRequestIds.Count == 1).ToArray();
    var rows = new List<object>();
    foreach (var candidate in candidates)
    {
        var committed2 = Commit(committed1,reduced2,candidate,policies);
        var eligibleFuture = new List<string>();
        foreach (int fFrom in Enumerable.Range(0,5))
        foreach (int fTo in Enumerable.Range(0,5).Where(i => i != fFrom))
        {
            // Each hypothetical request is tested independently from the same post-state.
            // Arrival is simultaneous, but revealed in the following logical epoch.
            var f = Request("future",fFrom,fTo,5000);
            var reduced3 = Add(committed2,f);
            if (Candidates(committed2,reduced3,policies).Any(c => c.NewRequestIds.Count == 1))
                eligibleFuture.Add($"{fFrom}->{fTo}");
        }
        var usage = committed2.Commitments.Histories.Values
            .Select(h => new {rider=h.RequestId.Value, usage=h.Current.BudgetAfter}).ToArray();
        rows.Add(new {
            candidate.CandidateId,
            route=candidate.Route.RemainingStops.Select(s=>new {node=s.NodeId.Value,request=s.RequestId?.Value,kind=s.Kind.ToString()}),
            cost=candidate.Schedule.OperationalCost,
            etaUsageTotal=usage.Sum(x=>x.usage.PickupEtaTotalMs+x.usage.DropEtaTotalMs),
            usage, futureFeasibleCount=eligibleFuture.Count, futureFeasible=eligibleFuture
        });
    }
    results.Add(new {budget, currentRequest=$"{qFrom}->{qTo}", rows});
}
var assemblies = new [] {typeof(OnlineState).Assembly,typeof(RideBoundRun).Assembly,typeof(InsertionCandidateGenerator).Assembly}
    .Select(a=>new {path=a.Location,sha256=Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(a.Location))).ToLowerInvariant()});
File.WriteAllText(output,JsonSerializer.Serialize(new {kind="fixed-state-core-mechanism-probe", assemblies, results},new JsonSerializerOptions {WriteIndented=true}));
Console.WriteLine($"Wrote {results.Count} fixed-state fixtures to {output}");

RideRequest Request(string id,int from,int to,long latest) => RideRequest.CreatePending(
    new RequestId(id),clock,nodes[from],nodes[to],clock,new SimTime(latest),new Duration(12000),1,"standard","probe-policy").Value!;

OnlineState Add(OnlineState before,RideRequest request)
{
    var r=before.Run.AddRequest(request);
    if (!r.IsSuccess) throw new InvalidOperationException(r.Failure!.Message);
    var advanced=r.Value!.AdvanceEpoch(before.Run.AppliedEpoch+1,clock);
    if (!advanced.IsSuccess) throw new InvalidOperationException(advanced.Failure!.Message);
    return before with {Run=advanced.Value!,NextEventSequence=before.NextEventSequence+1};
}

IReadOnlyList<InsertionCandidate> Candidates(OnlineState before,OnlineState reduced,ICommitmentPolicyProvider policies)
{
    var generated=generator.Generate(reduced,CandidateGenerationOptions.ExactSmall);
    if (!generated.IsSuccess) throw new InvalidOperationException(generated.Witness!.Message);
    var assessed=assessor.AssessAndFilter(new CommitmentMechanismContext(before,reduced,policies,
        NoDistances.Instance,$"probe-{reduced.Run.AppliedEpoch}",before.NextEventSequence),generated.VehicleCandidates!);
    if (!assessed.IsSuccess) throw new InvalidOperationException(assessed.Witness!.Message);
    return assessed.Batch!.FeasibleCandidateSets.Single().Candidates;
}

OnlineState Commit(OnlineState before,OnlineState reduced,InsertionCandidate candidate,ICommitmentPolicyProvider policies)
{
    var updated=reduced.Run.UpdateVehicleRoute(candidate.VehicleId,candidate.Route);
    if (!updated.IsSuccess) throw new InvalidOperationException(updated.Failure!.Message);
    var r=updated.Value!;
    foreach(var requestId in candidate.NewRequestIds)
    {
        var accepted=r.AcceptRequest(requestId,candidate.VehicleId);
        if (!accepted.IsSuccess) throw new InvalidOperationException(accepted.Failure!.Message);
        r=accepted.Value!;
    }
    var validated=validator.Validate(new CommitmentValidationContext(before,reduced,reduced with {Run=r},policies,
        NoDistances.Instance,$"probe-{reduced.Run.AppliedEpoch}",before.NextEventSequence));
    if (!validated.IsValid) throw new InvalidOperationException(JsonSerializer.Serialize(validated.Witnesses));
    return validated.ValidatedState!;
}

sealed class NoDistances : IStopDistanceLookup
{
    public static readonly NoDistances Instance=new();
    public bool TryGetDistanceMillimeters(NodeId fromNodeId,NodeId toNodeId,out long distanceMillimeters)
    {distanceMillimeters=0;return fromNodeId==toNodeId;}
}
