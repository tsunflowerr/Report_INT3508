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
using RideBound.Domain.Validation;
using RideBound.Runner.Configuration;
using RideBound.Runner.Online;
using RouteStopKind = RideBound.Domain.Routes.RouteStopKind;

var root=args[0]; var output=args[1];
var allOrders=args.Length>2 && args[2]=="all-orders";
var auditHead=args.Length>3 && args[3]=="audit-head";
var policies=CommitmentPolicyConfiguration.Decode(File.ReadAllBytes("E:/Code/RideBound/benchmarks/configurations/wp8-drop-eta-budget-tight-v1.json"));
var wp4=Wp4RunnerConfiguration.Decode(File.ReadAllBytes("E:/Code/RideBound/benchmarks/configurations/wp13-e1-fleetpy-ridebound-hard-vector-retained-v1.json"),policies);
var physical=new PhysicalPlanValidator();
var validator=new CommitmentDecisionValidator();
var rows=new List<object>();
// Use the pinned assembly's identity implementation without copying its framing.
var identity=typeof(InsertionCandidateGenerator).Assembly.GetType("RideBound.Algorithms.Candidates.CandidateIdentity",true)!;
var stopId=identity.GetMethod("CreateStopId")!.CreateDelegate<Func<RequestId,RouteStopKind,StopId>>();
var fingerprint=identity.GetMethod("CreateRouteFingerprint")!.CreateDelegate<Func<RoutePlan,string>>();
foreach(var file in Directory.GetFiles(root,"epoch-*-before.json").Order())
{
    using var doc=JsonDocument.Parse(File.ReadAllBytes(file));
    var decode=OnlineStateCheckpointCodec.Decode(doc.RootElement);
    if(!decode.IsSuccess) throw new InvalidDataException(decode.Error);
    var before=decode.State!; var prefix=file[..^"-before.json".Length];
    var envelope=ProtocolEnvelopeCodec.Decode(File.ReadAllBytes(prefix+"-event.json")).Envelope!;
    var mapped=new OnlineEventMapper().Map(envelope);
    if(!mapped.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(mapped.Witness));
    var reduction=new EventReducer().Reduce(before,mapped.Batch!);
    if(!reduction.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(reduction.Witness));
    var reduced=reduction.ProposedState!; var epoch=reduced.Run.AppliedEpoch;
    var request=reduced.Run.Requests.Values.Single(r=>r.Lifecycle==RequestLifecycle.Pending);
    var context=new CommitmentMechanismContext(before,reduced,policies,policies,$"drop-audit-{epoch}",reduced.NextEventSequence-1,wp4.InitialPromiseTrigger);
    var baseline=new InsertionCandidateGenerator().Generate(reduced,wp4.CandidateGeneration);
    if(!baseline.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(baseline.Witness));
    var gated=new HardVectorCandidateAssessor().AssessAndFilter(context,baseline.VehicleCandidates!);
    if(!gated.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(gated.Witness));
    using var decision=JsonDocument.Parse(File.ReadAllBytes(prefix+"-decision.json"));
    var portfolio=decision.RootElement.GetProperty("payload").GetProperty("solver").GetProperty("executionEvidence").GetProperty("candidatePortfolio");
    var expected=portfolio.GetProperty("candidates").EnumerateArray().Where(c=>c.GetProperty("policyEligibility").GetString()=="eligible").Select(c=>c.GetProperty("candidateId").GetString()!).ToHashSet();
    var actual=gated.Batch!.FeasibleCandidateSets.SelectMany(s=>s.Candidates).Select(c=>c.CandidateId).ToHashSet();
    if(!expected.SetEquals(actual)) throw new InvalidDataException("Original baseline identity mismatch");
    var baselineAccept=gated.Batch.FeasibleCandidateSets.SelectMany(s=>s.Candidates).Count(c=>c.NewRequestIds.Contains(request.Id));
    var pickup=new RouteStop(stopId(request.Id,RouteStopKind.Pickup),request.OriginNodeId,RouteStopKind.Pickup,request.Id,new Duration(0));
    var drop=new RouteStop(stopId(request.Id,RouteStopKind.DropOff),request.DestinationNodeId,RouteStopKind.DropOff,request.Id,new Duration(0));
    var counts=new Dictionary<string,int>(); var valid=new List<object>(); var hardRejectedRoutes=new List<object>();
    var watch=Stopwatch.StartNew(); var controlAccept=0; var total=0; var screenRemoved=0; var physicalPass=0; var expectedAllOrders=0; var maxSuffix=0;
    foreach(var vehicle in reduced.Run.Vehicles.Values.OrderBy(v=>v.Id.Value,StringComparer.Ordinal))
    {
        var original=vehicle.Route.MutableSuffix.ToArray();
        maxSuffix=Math.Max(maxSuffix,original.Length);
        if(allOrders && original.Length>6) throw new InvalidDataException("All-orders audit bound exceeded; no silent omission");
        expectedAllOrders+=Factorial(original.Length)*(original.Length+1)*(original.Length+2)/2;
        var seeds=new List<(RouteStop[] Stops,RequestId? Moved,bool Control)>{(original,null,true)};
        if(allOrders)
        {
            seeds.AddRange(Permutations(original).Where(p=>!p.SequenceEqual(original)).Select(p=>(p,(RequestId?)null,false)));
        }
        else
        for(var i=0;i<original.Length;i++)
        {
            if(original[i].Kind!=RouteStopKind.DropOff) continue;
            var without=original.Where((_,j)=>j!=i).ToList();
            for(var j=0;j<=without.Count;j++)
            {
                var moved=without.ToList(); moved.Insert(j,original[i]);
                if(!moved.SequenceEqual(original)) seeds.Add((moved.ToArray(),original[i].RequestId,false));
            }
        }
        var seen=new HashSet<string>(StringComparer.Ordinal);
        foreach(var seed in seeds)
        for(var pi=0;pi<=seed.Stops.Length;pi++)
        for(var di=pi+1;di<=seed.Stops.Length+1;di++)
        {
            var stops=seed.Stops.ToList(); stops.Insert(pi,pickup); stops.Insert(di,drop);
            var route=vehicle.Route.ReplaceMutableSuffix(stops).Value!;
            if(!seen.Add(fingerprint(route))) continue;
            total++;
            var oldHead=vehicle.Route.RemainingStops.ToArray();
            var preservesHead=oldHead.Length==0 || oldHead.TakeWhile(s=>s.NodeId==oldHead[0].NodeId).SequenceEqual(route.RemainingStops.TakeWhile(s=>s.NodeId==oldHead[0].NodeId));
            if(!preservesHead)
            {screenRemoved++; if(!auditHead) continue;}
            var p=physical.Validate(new PhysicalValidationContext(reduced.Run,vehicle.Id,route,reduced.TravelTimes!,reduced.Run.SimulationTime));
            if(!p.IsFeasible){Add("physical:"+p.Witness!.Code);continue;}
            physicalPass++;
            var changed=reduced.Run.UpdateVehicleRoute(vehicle.Id,route);
            if(!changed.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(changed.Failure));
            var accepted=changed.Value!.AcceptRequest(request.Id,vehicle.Id);
            if(!accepted.IsSuccess) throw new InvalidDataException(JsonSerializer.Serialize(accepted.Failure));
            var result=validator.Validate(new CommitmentValidationContext(before,reduced,reduced with {Run=accepted.Value!},policies,policies,$"drop-full-{epoch}",reduced.NextEventSequence-1,InitialPromiseTrigger:wp4.InitialPromiseTrigger));
            if(!result.IsValid)
            {
                Add("commitment:"+result.Witnesses[0].Code);
                var evaluator=new CandidateScheduleEvaluator();
                var oldSchedule=evaluator.Evaluate(reduced,vehicle,vehicle.Route,reduced.TravelTimes!,reduced.Run.SimulationTime);
                var newSchedule=evaluator.Evaluate(reduced,vehicle,route,reduced.TravelTimes!,reduced.Run.SimulationTime);
                if(!oldSchedule.IsSuccess || !newSchedule.IsSuccess) throw new InvalidDataException("Physical-pass schedule projection failed");
                hardRejectedRoutes.Add(new {vehicle=vehicle.Id.Value,preservesHead,seed.Control,
                    route=stops.Select(s=>new {stop=s.StopId.Value,node=s.NodeId.Value,kind=s.Kind.ToString(),request=s.RequestId?.Value}),
                    beforeSchedule=oldSchedule.Schedule,afterSchedule=newSchedule.Schedule,witnesses=result.Witnesses});
                continue;
            }
            if(seed.Control) controlAccept++;
            var schedule=new CandidateScheduleEvaluator().Evaluate(reduced,vehicle,route,reduced.TravelTimes!,reduced.Run.SimulationTime);
            if(!schedule.IsSuccess) throw new InvalidDataException(schedule.Message);
            valid.Add(new {vehicle=vehicle.Id.Value,seed.Control,preservesHead,moved=seed.Moved?.Value,movedLifecycle=seed.Moved is {} id?reduced.Run.Requests[id].Lifecycle.ToString():null,
                route=stops.Select(s=>new {stop=s.StopId.Value,node=s.NodeId.Value,kind=s.Kind.ToString(),request=s.RequestId?.Value}),schedule=schedule.Schedule});
        }
    }
    // All selected states were rejected by the recorded baseline. The independent
    // unchanged-order control must also find zero acceptances under the screen.
    if(baselineAccept!=0 || controlAccept!=0) throw new InvalidDataException("Unexpected control acceptance in rejected-state audit");
    if(allOrders && total!=expectedAllOrders) throw new InvalidDataException("Permutation/insertion count does not match combinatorial bound");
    rows.Add(new {epoch,baselineAccept,controlAccept,total,expectedAllOrders,maxSuffix,screenRemoved,physicalPass,firstWitnessCounts=counts,validCount=valid.Count,valid,hardRejectedRoutes,elapsedMs=watch.Elapsed.TotalMilliseconds,inputStateSha256=Hash(file)});
    Write(); Console.WriteLine($"Epoch {epoch}: {total} unique routes; {physicalPass} physical passes; {valid.Count} full-contract acceptances");
    void Add(string key)=>counts[key]=counts.GetValueOrDefault(key)+1;
}
Write();
void Write()=>File.WriteAllText(output,JsonSerializer.Serialize(new {
    kind=allOrders?"all-incumbent-orders-same-state-original-E1-validator-audit":"single-incumbent-drop-relocation-same-state-original-E1-validator-audit",
    allOrders,
    auditHead,
    limitation="No closed-loop or exact FleetPy locked-leg claim; generic local search is prior art",
    rows},new JsonSerializerOptions{WriteIndented=true}));
static string Hash(string path)=>Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(path)));
static int Factorial(int n)=>n<2?1:checked(n*Factorial(n-1));
static IEnumerable<RouteStop[]> Permutations(RouteStop[] stops)
{
    if(stops.Length==0){yield return [];yield break;}
    for(var i=0;i<stops.Length;i++)
    foreach(var tail in Permutations(stops.Where((_,j)=>j!=i).ToArray()))
        yield return new[]{stops[i]}.Concat(tail).ToArray();
}
