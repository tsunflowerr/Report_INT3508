// Fixed-state mechanism probe. Uses original E1 Runner codec/reducer/core.
// Future probes are independent repetitions of already observed OD/service types,
// arriving immediately after a hypothetical same-time booking confirmation.
// This is neither a simulator nor a forecast/closed-loop effectiveness experiment.
using System.Diagnostics;
using System.Security.Cryptography;
using System.Text.Json;
using RideBound.Algorithms.Candidates;
using RideBound.Algorithms.Commitments;
using RideBound.Application.Commitments;
using RideBound.Application.Events;
using RideBound.Application.State;
using RideBound.Contracts.Protocol;
using RideBound.Domain.Common;
using RideBound.Domain.Requests;
using RideBound.Domain.Routes;
using RideBound.Runner.Configuration;
using RideBound.Runner.Online;
using RouteStopKind = RideBound.Domain.Routes.RouteStopKind;

var root=args[0];
var output=args[1];
var selectedEpochs=args.Skip(2).Select(long.Parse).ToHashSet();
var policies=CommitmentPolicyConfiguration.Decode(File.ReadAllBytes("E:/Code/RideBound/benchmarks/configurations/wp8-drop-eta-budget-tight-v1.json"));
var wp4=Wp4RunnerConfiguration.Decode(File.ReadAllBytes("E:/Code/RideBound/benchmarks/configurations/wp13-e1-fleetpy-ridebound-hard-vector-retained-v1.json"),policies);
var generator=new InsertionCandidateGenerator();
var assessor=new HardVectorCandidateAssessor();
var validator=new CommitmentDecisionValidator();
var reducer=new EventReducer();
var rows=new List<object>();
foreach(var stateFile in Directory.GetFiles(root,"epoch-*-before.json").Order())
{
    using var stateDoc=JsonDocument.Parse(File.ReadAllBytes(stateFile));
    var decoded=OnlineStateCheckpointCodec.Decode(stateDoc.RootElement);
    if(!decoded.IsSuccess) throw new InvalidDataException(decoded.Error);
    var before=decoded.State!;
    var epoch=before.Run.AppliedEpoch+1;
    if(selectedEpochs.Count>0 && !selectedEpochs.Contains(epoch)) continue;
    var prefix=stateFile[..^"-before.json".Length];
    var eventEnvelope=ProtocolEnvelopeCodec.Decode(File.ReadAllBytes(prefix+"-event.json")).Envelope!;
    var mapped=new OnlineEventMapper().Map(eventEnvelope);
    if(!mapped.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(mapped.Witness));
    var reducedResult=reducer.Reduce(before,mapped.Batch!);
    if(!reducedResult.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(reducedResult.Witness));
    var reduced=reducedResult.ProposedState!;
    var pending=reduced.Run.Requests.Values.Where(r=>r.Lifecycle==RequestLifecycle.Pending).ToArray();
    if(pending.Length!=1) throw new InvalidDataException("Probe requires exactly one pending request");
    var assessed=Generate(before,reduced);
    using var decision=JsonDocument.Parse(File.ReadAllBytes(prefix+"-decision.json"));
    var portfolio=decision.RootElement.GetProperty("payload").GetProperty("solver").GetProperty("executionEvidence").GetProperty("candidatePortfolio");
    var expectedIds=portfolio.GetProperty("candidates").EnumerateArray().Where(c=>c.GetProperty("policyEligibility").GetString()=="eligible").Select(c=>c.GetProperty("candidateId").GetString()!).ToHashSet();
    var actualIds=assessed.FeasibleCandidateSets.SelectMany(s=>s.Candidates).Select(c=>c.CandidateId).ToHashSet();
    if(!expectedIds.SetEquals(actualIds)) throw new InvalidDataException($"Portfolio mismatch epoch {epoch}");
    var recordedIds=portfolio.GetProperty("selectedCandidateIds").EnumerateArray().Select(v=>v.GetString()!).ToHashSet();
    var assignments=Cartesian(assessed.FeasibleCandidateSets.Select(s=>s.Candidates).ToArray())
        .Where(a=>a.SelectMany(c=>c.NewRequestIds).Count()==1).ToArray();
    // All samples existed before this decision; no suffix demand is read.
    var samples=before.Run.Requests.Values.OrderBy(r=>r.ArrivalTime.Milliseconds).ThenBy(r=>r.Id.Value,StringComparer.Ordinal)
        .GroupBy(r=>(r.OriginNodeId,r.DestinationNodeId,r.PartySize,r.LatestPickup.Milliseconds-r.EarliestPickup.Milliseconds,r.MaxRideTime.Milliseconds))
        .Select(g=>g.First()).Take(12).ToArray();
    var outcomes=new List<object>();
    int ordinal=0;
    foreach(var assignment in assignments)
    {
        var started=Stopwatch.StartNew();
        var current=assignment.Single(c=>c.NewRequestIds.Count==1);
        var run=reduced.Run;
        foreach(var c in assignment)
        {
            if(!c.IsNoOp) run=run.UpdateVehicleRoute(c.VehicleId,c.Route).Value!;
            foreach(var id in c.NewRequestIds) run=run.AcceptRequest(id,c.VehicleId).Value!;
        }
        var offered=Validate(before,reduced,reduced with {Run=run});
        var confirmation=Reduce(offered,new BookingConfirmed(offered.NextEventSequence,offered.Run.SimulationTime,pending[0].Id));
        var committed=Validate(offered,confirmation,confirmation);
        var futureResults=new List<object>();
        foreach(var sample in samples)
        {
            var clock=committed.Run.SimulationTime;
            var request=RideRequest.CreatePending(new RequestId("probe-"+sample.Id.Value),clock,sample.OriginNodeId,sample.DestinationNodeId,
                clock,new SimTime(clock.Milliseconds+sample.LatestPickup.Milliseconds-sample.EarliestPickup.Milliseconds),
                sample.MaxRideTime,sample.PartySize,sample.ServiceClass,sample.CommitmentPolicyId).Value!;
            var futureState=Reduce(committed,new RequestArrived(committed.NextEventSequence,clock,request));
            var future=Generate(committed,futureState);
            var vehicles=future.FeasibleCandidateSets.Where(s=>s.Candidates.Any(c=>c.NewRequestIds.Contains(request.Id))).Select(s=>s.VehicleId.Value).ToArray();
            futureResults.Add(new {sample=sample.Id.Value,feasible=vehicles.Length>0,vehicles});
        }
        var schedule=current.Schedule.Stops.ToDictionary(s=>s.StopId);
        var pickup=current.Route.RemainingStops.Single(s=>s.RequestId==pending[0].Id && s.Kind==RouteStopKind.Pickup);
        var drop=current.Route.RemainingStops.Single(s=>s.RequestId==pending[0].Id && s.Kind==RouteStopKind.DropOff);
        var pickupTime=schedule[pickup.StopId].ServiceStartTime.Milliseconds;
        var dropTime=schedule[drop.StopId].ServiceStartTime.Milliseconds;
        outcomes.Add(new {ordinal=ordinal++, selectedCandidateIds=assignment.Select(c=>c.CandidateId),
            isRecorded=recordedIds.SetEquals(assignment.Select(c=>c.CandidateId)),
            currentVehicle=current.VehicleId.Value,cost=assignment.Sum(c=>c.Schedule.OperationalCost),
            currentWaitMs=pickupTime-pending[0].ArrivalTime.Milliseconds,currentRideMs=dropTime-pickupTime,
            revisions=assignment.Select(c=>assessed.Assessments[c.CandidateId].DecisionInducedRevision),
            futureResults, elapsedMs=started.Elapsed.TotalMilliseconds});
    }
    rows.Add(new {epoch, pendingRequest=pending[0].Id.Value,sampleCount=samples.Length,assignmentCount=assignments.Length,
        existingRiders=before.Run.Requests.Values.Count(r=>r.IsAcceptedActive),inputStateSha256=Hash(File.ReadAllBytes(stateFile)), outcomes});
    Write();
    Console.WriteLine($"Epoch {epoch}: {assignments.Length} alternatives, {samples.Length} observed-OD probes; exact eligible portfolio matched");
}
Write();

HardVectorCandidateAssessmentBatch Generate(OnlineState before,OnlineState reduced)
{
    var generated=generator.Generate(reduced,wp4.CandidateGeneration);
    if(!generated.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(generated.Witness));
    if(generated.VehicleCandidates!.Any(s=>s.WasTruncated)) throw new InvalidDataException("Candidate set truncated: do not treat absence as exact feasibility");
    var assessed=assessor.AssessAndFilter(new CommitmentMechanismContext(before,reduced,policies,policies,
        $"research-{reduced.Run.AppliedEpoch}",reduced.NextEventSequence-1,wp4.InitialPromiseTrigger),generated.VehicleCandidates!);
    if(!assessed.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(assessed.Witness));
    return assessed.Batch!;
}
OnlineState Reduce(OnlineState state,OnlineEvent e)
{
    var result=reducer.Reduce(state,new InternalEventBatch(state.Run.Id,state.Run.ScenarioId,state.Run.AppliedEpoch+1,e.SimulationTime,[e]));
    if(!result.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(result.Witness));
    return result.ProposedState!;
}
OnlineState Validate(OnlineState before,OnlineState reduced,OnlineState candidate)
{
    var result=validator.Validate(new CommitmentValidationContext(before,reduced,candidate,policies,policies,
        $"research-{reduced.Run.AppliedEpoch}",reduced.NextEventSequence-1,InitialPromiseTrigger:wp4.InitialPromiseTrigger));
    if(!result.IsValid) throw new InvalidDataException(JsonSerializer.Serialize(result.Witnesses));
    return result.ValidatedState!;
}
void Write()=>File.WriteAllText(output,JsonSerializer.Serialize(new {kind="retained-state-independent-immediate-observed-OD-probe",rows},new JsonSerializerOptions{WriteIndented=true}));
static string Hash(byte[] data)=>Convert.ToHexStringLower(SHA256.HashData(data));
static IEnumerable<InsertionCandidate[]> Cartesian(IReadOnlyList<InsertionCandidate>[] sets)
{
    IEnumerable<InsertionCandidate[]> values=[Array.Empty<InsertionCandidate>()];
    foreach(var set in sets) values=values.SelectMany(a=>set.Select(c=>a.Append(c).ToArray()));
    return values;
}
