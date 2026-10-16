$ErrorActionPreference = 'Stop'
$workRoot = (Get-Location).Path
$sourceRoot = 'E:/Code/Report_INT3508/ridebound-scratchpad'
$sources = [ordered]@{
 A = "$sourceRoot/rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex"
 Ch1 = "$workRoot/r30-ch1/05-chuong1-v3.tex"
 Ch2 = "$sourceRoot/rewrite-2026-10/drafts/06-chuong2-v4.tex"
 Ch3 = "$workRoot/r33-ch3v4/07-chuong3-v4-v3.tex"
 B = "$sourceRoot/rewrite-2026-10/drafts/09-chuong4-phanB-v10.tex"
 Appx = "$workRoot/r31-ch5/11-phuluc-v2.tex"
 Bib = "$workRoot/r32-bib/10-tai-lieu-draft.tex"
 TestReport = "$sourceRoot/rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md"
 TestLog = 'C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log'
 RUN38 = "$sourceRoot/tang3/t38/run_t38.py"
 T38 = "$sourceRoot/tang3/t38/T38-REPORT.md"
}
$textByKey = @{}
$labelTargets = @{}
$linesByKey = @{}
$rows = [Collections.Generic.List[string]]::new()
$rows.Add('Read-only consistency audit; all writes exclusive; no build, simulation or installation.')
foreach ($key in $sources.Keys) {
 $path = $sources[$key]
 $body = [IO.File]::ReadAllText($path, [Text.Encoding]::UTF8)
 $textByKey[$key] = $body
 $linesByKey[$key] = $body -split '\r?\n'
 $rows.Add("SOURCE $key $path SHA256=$((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash)")
 for ($i = 0; $i -lt $linesByKey[$key].Length; $i++) {
  $line = ($linesByKey[$key][$i] -split '(?<!\\)%',2)[0]
  foreach ($match in [regex]::Matches($line, '\\label\{([^}]+)\}')) {
   $label = $match.Groups[1].Value
   if (-not $labelTargets.ContainsKey($label)) { $labelTargets[$label] = [Collections.Generic.List[string]]::new() }
   $labelTargets[$label].Add("$key`:$(1+$i)")
  }
 }
}
$refUse = @{}
for ($i=0; $i -lt $linesByKey['A'].Length; $i++) {
 $line = ($linesByKey['A'][$i] -split '(?<!\\)%',2)[0]
 foreach ($match in [regex]::Matches($line, '\\(?:ref|eqref|autoref)\{([^}]+)\}')) {
  $label = $match.Groups[1].Value
  if (-not $refUse.ContainsKey($label)) { $refUse[$label] = [Collections.Generic.List[int]]::new() }
  $refUse[$label].Add(1+$i)
 }
}
$rows.Add('ALL A REFERENCE TARGETS:')
foreach ($label in ($refUse.Keys | Sort-Object)) {
 $target = if ($labelTargets.ContainsKey($label)) { $labelTargets[$label] -join ',' } else { 'MISSING' }
 $rows.Add("$label USE=A:$($refUse[$label] -join ',') TARGET=$target")
}
$rows.Add('DUPLICATE LABELS:')
$duplicates=0
foreach ($label in ($labelTargets.Keys | Sort-Object)) {
 if ($labelTargets[$label].Count -gt 1) { $rows.Add("$label $($labelTargets[$label] -join ',')"); $duplicates++ }
}
$rows.Add("TOTAL A DISTINCT TARGETS=$($refUse.Count), MISSING=$(@($refUse.Keys | Where-Object { -not $labelTargets.ContainsKey($_) }).Count), DUPLICATES=$duplicates")
$rows.Add('A TEST STATEMENTS:')
for ($i=0; $i -lt $linesByKey['A'].Length; $i++) {
 if ($linesByKey['A'][$i] -match '1\.02[45]|kiểm thử') { $rows.Add("A:$(1+$i) $($linesByKey['A'][$i])") }
}
$rows.Add('B RELEVANT RESIDUAL / RESOLVED SOURCE LINES:')
foreach ($range in @(@(191,202),@(276,288),@(355,387),@(419,430))) {
 for ($i=$range[0];$i -le $range[1];$i++) { $rows.Add("B:$i $($linesByKey['B'][$i-1])") }
}
$rows.Add('CH3 NO-OP / CALIBRATION / TEST SOURCE LINES:')
foreach ($range in @(@(366,389),@(721,740))) {
 for ($i=$range[0];$i -le $range[1];$i++) { $rows.Add("Ch3:$i $($linesByKey['Ch3'][$i-1])") }
}
$rows.Add('CALIBRATION ORIGINAL RUN SOURCE LINES:')
foreach ($key in @('RUN38','T38')) {
 foreach ($range in $(if ($key -eq 'RUN38') {@(@(1,12),@(42,58))} else {@(@(99,108))})) {
  for ($i=$range[0];$i -le $range[1];$i++) { $rows.Add("$key`:$i $($linesByKey[$key][$i-1])") }
 }
}
$rows.Add('APPENDIX TEST SOURCE LINES:')
for ($i=113;$i -le 120;$i++) { $rows.Add("Appx:$i $($linesByKey['Appx'][$i-1])") }
$rows.Add('TEST ATTEMPT4 REPORT AND LOG:')
for ($i=1;$i -le $linesByKey['TestReport'].Length;$i++) {
 if ($linesByKey['TestReport'][$i-1] -match 'Attempt|4 \(|13/10|13:39|single run|LF|marker|attempt 4') { $rows.Add("TestReport:$i $($linesByKey['TestReport'][$i-1])") }
}
for ($i=1;$i -le $linesByKey['TestLog'].Length;$i++) {
 if ($linesByKey['TestLog'][$i-1] -match 'Passed|Failed|Total tests|Test Run|passed|failed|total|Test summary|summary|git status|\?\?') { $rows.Add("TestLog:$i $($linesByKey['TestLog'][$i-1])") }
}
$rows.Add('BIBLIOGRAPHY KEYS USED BY A / B:')
foreach ($key in @('engelhardt2026','schulz2026','horl2022')) {
 for ($i=0;$i -lt $linesByKey['Bib'].Length;$i++) {
  if ($linesByKey['Bib'][$i] -match "\\bibitem\{$key\}") { $rows.Add("Bib:$(1+$i) $($linesByKey['Bib'][$i])") }
 }
}
$outputPath = Join-Path $workRoot 'r36-ch4a-v5/agent-consistency-v2-output.txt'
$stream = [IO.File]::Open($outputPath,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::Read)
$writer = [IO.StreamWriter]::new($stream,[Text.UTF8Encoding]::new($false))
try { $writer.Write(($rows -join "`n")+"`n") } finally { $writer.Dispose() }
Write-Output ($rows -join "`n")