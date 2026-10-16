// Same-state neighborhood audit through original versioned E1 core.
// Does not execute FleetPy, alter policies, or claim adapter conformance.
using System.Diagnostics;
using System.Security.Cryptography;
using System.Text.Json;
using RideBound.Algorithms.Candidates;
using RideBound.Algorithms.Commitments;
using RideBound.Application.Commitments;
using RideBound.Application.Events;
using RideBound.Application.State;
using RideBound.Contracts.Protocol;
using RideBound.Domain.Requests;
using RideBound.Domain.Routes;
using RideBound.Runner.Configuration;
using RideBound.Runner.Online;

var root=args[0];
var output=args[1];
var policies=CommitmentPolicyConfiguration.Decode(File.ReadAllBytes("E:/Code/RideBound/benchmarks/configurations/wp8-drop-eta-budget-tight-v1.json"));
var wp4=Wp4RunnerConfiguration.Decode(File.ReadAllBytes("E:/Code/RideBound/benchmarks/configurations/wp13-e1-fleetpy-ridebound-hard-vector-retained-v1.json"),policies);
var generator=new InsertionCandidateGenerator();
var assessor=new HardVectorCandidateAssessor();
var validator=new CommitmentDecisionValidator();
var reducer=new EventReducer();
var rows=new List<object>();
foreach(var stateFile in Directory.GetFiles(root,"epoch-*-before.json").Order())
{
    using var doc=JsonDocument.Parse(File.ReadAllBytes(stateFile));
    var decoded=OnlineStateCheckpointCodec.Decode(doc.RootElement);
    if(!decoded.IsSuccess) throw new InvalidDataException(decoded.Error);
    var before=decoded.State!;
    var prefix=stateFile[..^"-before.json".Length];
    var envelope=ProtocolEnvelopeCodec.Decode(File.ReadAllBytes(prefix+"-event.json")).Envelope!;
    var mapped=new OnlineEventMapper().Map(envelope);
    if(!mapped.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(mapped.Witness));
    var reduction=reducer.Reduce(before,mapped.Batch!);
    if(!reduction.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(reduction.Witness));
    var reduced=reduction.ProposedState!;
    var pending=reduced.Run.Requests.Values.Where(r=>r.Lifecycle==RequestLifecycle.Pending).ToArray();
    if(pending.Length!=1) throw new InvalidDataException("Audit requires one pending request");
    var epoch=reduced.Run.AppliedEpoch;
    var context=new CommitmentMechanismContext(before,reduced,policies,policies,$"repair-probe-{epoch}",reduced.NextEventSequence-1,wp4.InitialPromiseTrigger);
    var baseline=generator.Generate(reduced,wp4.CandidateGeneration);
    if(!baseline.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(baseline.Witness));
    var gated=assessor.AssessAndFilter(context,baseline.VehicleCandidates!);
    if(!gated.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(gated.Witness));
    using var decision=JsonDocument.Parse(File.ReadAllBytes(prefix+"-decision.json"));
    var portfolio=decision.RootElement.GetProperty("payload").GetProperty("solver").GetProperty("executionEvidence").GetProperty("candidatePortfolio");
    var expected=portfolio.GetProperty("candidates").EnumerateArray().Where(c=>c.GetProperty("policyEligibility").GetString()=="eligible").Select(c=>c.GetProperty("candidateId").GetString()!).ToHashSet();
    var actual=gated.Batch!.FeasibleCandidateSets.SelectMany(s=>s.Candidates).Select(c=>c.CandidateId).ToHashSet();
    if(!expected.SetEquals(actual)) throw new InvalidDataException($"Baseline candidate mismatch {epoch}");
    var baselineAccept=gated.Batch.FeasibleCandidateSets.SelectMany(s=>s.Candidates).Count(c=>c.NewRequestIds.Contains(pending[0].Id));
    var timer=Stopwatch.StartNew();
    var repair=generator.Generate(reduced,wp4.CandidateGeneration.WithRepairRequestCap(4));
    if(!repair.IsSuccess)
    {
        rows.Add(new {epoch,baselineAccept,status="generation-failure",repair.Witness});
        Write(); continue;
    }
    // Preserve the complete leading same-node block, including exact stop fields.
    // This is conservative structural screening, not a substitute for FleetPy's
    // full locked-leg signature (status, durations and earliest times included).
    var safeSets=repair.VehicleCandidates!.Select(s=>s with {
        Candidates=s.Candidates.Where(c=>PreservesHeadBlock(reduced.Run.Vehicles[c.VehicleId].Route,c.Route)).ToArray()
    }).ToArray();
    var screened=assessor.AssessAndFilter(context,safeSets);
    if(!screened.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(screened.Witness));
    var candidates=screened.Batch!.FeasibleCandidateSets.SelectMany(s=>s.Candidates).Where(c=>c.NewRequestIds.Contains(pending[0].Id)).ToArray();
    var valid=new List<object>();
    foreach(var c in candidates)
    {
        var update=reduced.Run.UpdateVehicleRoute(c.VehicleId,c.Route);
        if(!update.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(update.Failure));
        var run=update.Value!;
        foreach(var id in c.NewRequestIds) run=run.AcceptRequest(id,c.VehicleId).Value!;
        var validation=validator.Validate(new CommitmentValidationContext(before,reduced,reduced with {Run=run},policies,policies,$"repair-full-{epoch}",reduced.NextEventSequence-1,InitialPromiseTrigger:wp4.InitialPromiseTrigger));
        if(!validation.IsValid) throw new InvalidDataException(JsonSerializer.Serialize(validation.Witnesses));
        valid.Add(new {c.CandidateId,vehicle=c.VehicleId.Value,c.Schedule.OperationalCost,
            repairedRequest=c.RepairedIncumbentRequestId?.Value,
            route=c.Route.RemainingStops.Select(s=>new {stop=s.StopId.Value,node=s.NodeId.Value,kind=s.Kind.ToString(),request=s.RequestId?.Value}),
            revision=screened.Batch.Assessments[c.CandidateId].DecisionInducedRevision});
    }
    var raw=repair.VehicleCandidates!.SelectMany(s=>s.Candidates).ToArray();
    var safeCandidateIds=safeSets.SelectMany(s=>s.Candidates).Select(c=>c.CandidateId).ToHashSet();
    var hardPrunes=screened.Batch.FeasibleCandidateSets.SelectMany(s=>s.PrunedCandidates)
        .Where(p=>safeCandidateIds.Contains(p.CandidateId)).ToArray();
    rows.Add(new {epoch,status="complete",baselineAccept,rawRepairCandidateCount=raw.Count(c=>c.RepairedIncumbentRequestId is not null),
        headScreenRemoved=raw.Length-safeSets.Sum(s=>s.Candidates.Count),safeHardAccept=candidates.Length,
        generatedPhysicalPrunes=repair.VehicleCandidates!.SelectMany(s=>s.PrunedCandidates).GroupBy(p=>p.Code).ToDictionary(g=>g.Key,g=>g.Count()),
        retainedHardPrunes=hardPrunes.GroupBy(p=>p.Code).ToDictionary(g=>g.Key,g=>g.Count()),
        newAcceptOpportunity=baselineAccept==0 && candidates.Length>0,
        generationComplete=repair.Diagnostics!.IsComplete,diagnostics=repair.Diagnostics,elapsedMs=timer.Elapsed.TotalMilliseconds,
        inputStateSha256=Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(stateFile))),valid});
    Write();
    Console.WriteLine($"Epoch {epoch}: baseline {baselineAccept}; conservative-head repair {candidates.Length}; complete {repair.Diagnostics.IsComplete}");
}
Write();

static bool PreservesHeadBlock(RoutePlan before,RoutePlan after)
{
    var old=before.RemainingStops.ToArray();
    if(old.Length==0) return true;
    var proposed=after.RemainingStops.ToArray();
    return old.TakeWhile(s=>s.NodeId==old[0].NodeId)
        .SequenceEqual(proposed.TakeWhile(s=>s.NodeId==old[0].NodeId));
}
void Write()=>File.WriteAllText(output,JsonSerializer.Serialize(new {
    kind="same-state-repair-conservative-leading-block-screen-original-E1-core",
    limitation="Not executed in FleetPy; screen alone does not prove exact locked-leg equivalence; no closed-loop gain claim",
    repairRequestCap=4,rows},new JsonSerializerOptions{WriteIndented=true}));
