$ErrorActionPreference = 'Stop'
$workRoot = (Get-Location).Path
$sourceRoot = 'E:/Code/Report_INT3508/ridebound-scratchpad'
$rows = [Collections.Generic.List[string]]::new()
function Add-SourceRange($key, $path, $first, $last) {
 $lines = [IO.File]::ReadAllLines($path,[Text.Encoding]::UTF8)
 for($i=$first; $i -le $last; $i++) { $rows.Add("$key`:$i $($lines[$i-1])") }
}
Add-SourceRange 'T38' "$sourceRoot/tang3/t38/T38-REPORT.md" 99 106
Add-SourceRange 'R26' "$workRoot/R26-CH3-OPEN-QUESTIONS-CODEX.md" 253 283
Add-SourceRange 'B' "$sourceRoot/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex" 181 187
Add-SourceRange 'ServiceQualityAllowance' 'C:/Code/RideBound-noworse/src/RideBound.Domain/Validation/ServiceQualityAllowance.cs' 66 77
Add-SourceRange 'Retainer' 'C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/CandidatePortfolioRetainer.cs' 102 113
Add-SourceRange 'VALID' 'C:/Code/RideBound-noworse/src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs' 355 360
Add-SourceRange 'VALID' 'C:/Code/RideBound-noworse/src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs' 1048 1064
Add-SourceRange 'GEN' 'C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs' 171 182
Add-SourceRange 'GEN' 'C:/Code/RideBound-noworse/src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs' 213 229
Add-SourceRange 'HVA' 'C:/Code/RideBound-noworse/src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs' 144 165
$log = [IO.File]::ReadAllText('C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log',[Text.Encoding]::UTF8)
$matches = [regex]::Matches($log,'Passed!\s+- Failed:\s+(\d+), Passed:\s+(\d+), Skipped:\s+(\d+), Total:\s+(\d+)')
$passTotal = 0
$failedTotal = 0
$skippedTotal = 0
$testTotal = 0
foreach($match in $matches) {
 $failedTotal += [int]$match.Groups[1].Value
 $passTotal += [int]$match.Groups[2].Value
 $skippedTotal += [int]$match.Groups[3].Value
 $testTotal += [int]$match.Groups[4].Value
}
$rows.Add("TEST ATTEMPT4 REAGGREGATION: project summaries=$($matches.Count); passed=$passTotal; failed=$failedTotal; skipped=$skippedTotal; total=$testTotal; exit0=$($log.Contains('exit=0'))")
$rows.Add("DLL SHA256=$((Get-FileHash -LiteralPath 'C:/RideBoundData/research/runner-tier3-v2/RideBound.Runner.dll' -Algorithm SHA256).Hash)")
$path = Join-Path $workRoot 'r36-ch4a-v5/agent-consistency-v2-supplement-output.txt'
$stream = [IO.File]::Open($path,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::Read)
$writer = [IO.StreamWriter]::new($stream,[Text.UTF8Encoding]::new($false))
try{$writer.Write(($rows -join "`n")+"`n")}finally{$writer.Dispose()}
Write-Output ($rows -join "`n")