// Exact recorded-input replay using the original versioned E1 Runner.
// No simulator or dispatch algorithm is reimplemented here.
using System.Security.Cryptography;
using System.Text.Json;
using RideBound.Contracts.Protocol;
using RideBound.Contracts.Serialization;
using RideBound.Runner.Configuration;
using RideBound.Runner.Online;
using RideBound.Runner.Protocol;

var transcript = args[0];
var outputDirectory = args[1];
var maxPending = int.Parse(args[2]);
var rejectedOnly = args.Skip(3).Contains("rejected-only");
var repo = "E:/Code/RideBound";
var policiesPath = repo + "/benchmarks/configurations/wp8-drop-eta-budget-tight-v1.json";
var wp4Path = repo + "/benchmarks/configurations/wp13-e1-fleetpy-ridebound-hard-vector-retained-v1.json";
var policies = CommitmentPolicyConfiguration.Decode(File.ReadAllBytes(policiesPath));
var wp4 = Wp4RunnerConfiguration.Decode(File.ReadAllBytes(wp4Path), policies);
var session = new RunnerSession(RunnerDefaults.CapabilityRequirements,
    RunnerExecutionMode.OnlineCommitment,
    commitmentPolicies: policies, stopDistances: policies,
    commitmentPolicyConfigurationHash: wp4.BindToCommitmentConfiguration(policies.ContentHash),
    wp4Configuration: wp4, useManifestSolverSeed: true);
Directory.CreateDirectory(outputDirectory);
var assemblies = AppDomain.CurrentDomain.GetAssemblies()
    .Where(a => !a.IsDynamic && a.GetName().Name!.StartsWith("RideBound."))
    .Select(a => new {path=a.Location, sha256=Hash(File.ReadAllBytes(a.Location))}).ToArray();
byte[]? pendingResponse = null;
byte[]? beforeState = null;
byte[]? eventBatch = null;
var saved = new List<object>();
int matched = 0;
foreach (var line in File.ReadLines(transcript))
{
    using var record = JsonDocument.Parse(line);
    var frame = Convert.FromBase64String(record.RootElement.GetProperty("frameBase64").GetString()!);
    using var message = JsonDocument.Parse(frame);
    string type = message.RootElement.GetProperty("messageType").GetString()!;
    if (record.RootElement.GetProperty("direction").GetString() == "adapterToRunner")
    {
        if (pendingResponse is not null) throw new InvalidDataException("Unmatched response before next input");
        if (type == "eventBatch")
        {
            beforeState = OnlineStateCanonicalizer.Canonicalize(session.CommittedOnlineState!);
            eventBatch = frame;
        }
        var result = session.Process(frame);
        if (result.Response?.MessageType.Value == "error")
            throw new InvalidDataException(result.Response.Payload.GetRawText());
        pendingResponse = result.Response is null ? null : ProtocolEnvelopeCodec.Encode(result.Response);
    }
    else
    {
        if (pendingResponse is null) throw new InvalidDataException("Recorded output has no replay response");
        var expected = CanonicalJson.Canonicalize(frame);
        var actual = CanonicalJson.Canonicalize(pendingResponse);
        if (!expected.AsSpan().SequenceEqual(actual))
        {
            File.WriteAllBytes(Path.Combine(outputDirectory,"mismatch-expected.json"),expected);
            File.WriteAllBytes(Path.Combine(outputDirectory,"mismatch-actual.json"),actual);
            throw new InvalidDataException($"Exact replay mismatch at ordinal {record.RootElement.GetProperty("ordinal")}");
        }
        pendingResponse = null;
        matched++;
        if (type == "decision")
        {
            var evidence = message.RootElement.GetProperty("payload").GetProperty("solver").GetProperty("executionEvidence");
            var hasRejection = message.RootElement.GetProperty("payload").GetProperty("actions").EnumerateArray()
                .Any(a => a.GetProperty("decisionType").GetString() == "requestRejected");
            if (evidence.GetProperty("generation").GetProperty("totalPendingRequestCount").GetInt32() > 0
                && (!rejectedOnly || hasRejection))
            {
                var epoch = message.RootElement.GetProperty("epochId").GetInt64();
                var prefix = $"epoch-{epoch:D5}";
                File.WriteAllBytes(Path.Combine(outputDirectory,prefix+"-before.json"),beforeState!);
                File.WriteAllBytes(Path.Combine(outputDirectory,prefix+"-event.json"),eventBatch!);
                File.WriteAllBytes(Path.Combine(outputDirectory,prefix+"-decision.json"),actual);
                saved.Add(new {epoch, prefix, beforeSha256=Hash(beforeState!), eventSha256=Hash(eventBatch!), decisionSha256=Hash(actual)});
                Console.WriteLine($"Exact match {matched}; captured pending epoch {epoch} ({saved.Count}/{maxPending})");
                if(saved.Count >= maxPending) break;
            }
        }
    }
}
var receipt = new {kind="exact-prefix-original-runner-state-capture",transcript,rejectedOnly,
    transcriptSha256=Hash(File.ReadAllBytes(transcript)), policiesPath, wp4Path,
    policiesSha256=Hash(File.ReadAllBytes(policiesPath)),wp4Sha256=Hash(File.ReadAllBytes(wp4Path)),
    matchedResponses=matched,saved,assemblies};
File.WriteAllText(Path.Combine(outputDirectory,"receipt.json"),JsonSerializer.Serialize(receipt,new JsonSerializerOptions{WriteIndented=true}));
Console.WriteLine($"Captured {saved.Count} states after {matched} exact responses.");
static string Hash(byte[] data) => Convert.ToHexStringLower(SHA256.HashData(data));
