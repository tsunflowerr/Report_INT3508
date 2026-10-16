$ErrorActionPreference='Stop'
$base='E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts'
$files=@(
 "$base/09-chuong4-phanB-v10.tex",
 "$base/08-chuong4-phanA-v4.tex",
 'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r33-ch3v4/07-chuong3-v4-v3.tex',
 "$base/06-chuong2-v4.tex"
)
$output=[Collections.Generic.List[string]]::new()
$labels=@{}
foreach ($path in $files) {
 $lines=[IO.File]::ReadAllLines($path,[Text.Encoding]::UTF8)
 for ($i=0; $i -lt $lines.Length; $i++) {
  if ($lines[$i].TrimStart().StartsWith('%')) {continue}
  foreach ($m in [regex]::Matches($lines[$i],'\\label\{([^}]+)\}')) {
   $label=$m.Groups[1].Value
   if (-not $labels.ContainsKey($label)) {$labels[$label]=[Collections.Generic.List[string]]::new()}
   $labels[$label].Add("$($path):$($i+1)")
  }
 }
}
$output.Add('REFERENCE AUDIT: latest specified Ch4B v10 + partA v4 + Ch3 r33 v4-v3 + Ch2 v4')
$v10=[IO.File]::ReadAllLines($files[0],[Text.Encoding]::UTF8)
for ($i=0; $i -lt $v10.Length; $i++) {
 if ($v10[$i].TrimStart().StartsWith('%')) {continue}
 foreach ($m in [regex]::Matches($v10[$i],'\\(eqref|ref|pageref|autoref|cref)\{([^}]+)\}')) {
  $label=$m.Groups[2].Value
  $where= if ($labels.ContainsKey($label)) {($labels[$label] -join ' | ')} else {'NOT IN SPECIFIED CHAPTERS'}
  $output.Add("v10:$($i+1) $($m.Groups[1].Value) {$label} -> $where")
 }
}
$output.Add('DUPLICATE LABELS:')
foreach ($label in ($labels.Keys | Sort-Object)) {if ($labels[$label].Count -gt 1) {$output.Add("$label -> $($labels[$label] -join ' | ')")}}
$output.Add('v10 LABELS:')
foreach ($label in ($labels.Keys | Sort-Object)) {foreach ($where in $labels[$label]) {if ($where.StartsWith($files[0])) {$output.Add("$label -> $where")}}}
$output.Add('FORBIDDEN-PHRASE SCAN (body only; manual interpretation required):')
for ($i=0; $i -lt $v10.Length; $i++) {
 if ($v10[$i].TrimStart().StartsWith('%')) {continue}
 if ($v10[$i] -match 'duy nhất|đầu tiên|vượt trội|đột phá|tối ưu|niêm phong|dự đoán trước|kết quả mong đợi|prereg|sealed|hash') {$output.Add("v10:$($i+1) $($v10[$i])")}
}
$out='E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r37-ch4b-verify/agent-regressions-ref-audit.txt'
$stream=[IO.File]::Open($out,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None)
$writer=[IO.StreamWriter]::new($stream,[Text.UTF8Encoding]::new($false))
try {foreach ($line in $output) {$writer.WriteLine($line)}} finally {$writer.Dispose()}
$output