$ErrorActionPreference='Stop'
$kit='E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10'
$latest=@("$kit/drafts/08-chuong4-phanA-v4.tex", "$kit/drafts/06-chuong2-v4.tex", 'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r33-ch3v4/07-chuong3-v4-v3.tex')
$output=[Collections.Generic.List[string]]::new()
$output.Add('Removed-label inbound check: bang:c4-haiphia')
$hits=Select-String -LiteralPath $latest -Pattern 'bang:c4-haiphia' -Encoding UTF8
if ($hits) {foreach ($hit in $hits) {$output.Add("$($hit.Path):$($hit.LineNumber):$($hit.Line)")}} else {$output.Add('No inbound occurrences in latest partA v4, Ch2 v4, Ch3 r33 v4-v3.')}
$output.Add('Appendix C definition check: rewrite .tex + current thesis noi-dung .tex')
$tex=@(Get-ChildItem -LiteralPath $kit -Filter '*.tex' -Recurse -File)+@(Get-ChildItem -LiteralPath 'E:/Code/Report_INT3508/ridebound/noi-dung' -Filter '*.tex' -File)
$hits=$tex | Select-String -Pattern '\\label\{phuluc:C\}' -Encoding UTF8
if ($hits) {foreach ($hit in $hits) {$output.Add("$($hit.Path):$($hit.LineNumber):$($hit.Line)")}} else {$output.Add('No phuluc:C label in either checked tree.')}
$output.Add('Known assembly dependency:')
foreach ($hit in (Select-String -LiteralPath "$kit/ASSEMBLY-NOTES.md", "$kit/drafts/09-chuong4-phanB-v8-NOTES.md" -Pattern 'phuluc:C' -Encoding UTF8)) {$output.Add("$($hit.Path):$($hit.LineNumber):$($hit.Line)")}
$output.Add('Independent integer-label arithmetic (not raw recomputation):')
$output.Add('weekday displayed labels: 82 + 5353 + 783 = 6218 versus displayed total 6217 => 1-second difference')
$output.Add('weekday source: 81.742 + 5352.646 + 783.018 = 6217.406; one-decimal components sum 6217.3 versus one-decimal total 6217.4 => 0.1-second difference')
$output.Add('snow displayed labels: 8.6 + 251.5 + 3185.9 = 3446.0 versus displayed total 3445.9 => 0.1-second difference')
$output.Add('snow shares: 0.25 + 7.3 + 92.5 = 100.05 percent; independent rounding, not a change of denominator')
$out='E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r37-ch4b-verify/agent-regressions-assembly-audit.txt'
$stream=[IO.File]::Open($out,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None)
$writer=[IO.StreamWriter]::new($stream,[Text.UTF8Encoding]::new($false))
try {foreach ($line in $output) {$writer.WriteLine($line)}} finally {$writer.Dispose()}
$output