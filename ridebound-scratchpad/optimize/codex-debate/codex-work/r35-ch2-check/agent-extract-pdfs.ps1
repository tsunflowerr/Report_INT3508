$ErrorActionPreference = 'Stop'
$base = 'E:\Code\Report_INT3508\ridebound-scratchpad\optimize\codex-debate\codex-work\r35-ch2-check'
$inputs = @{
  'hz' = 'E:\Code\Report_INT3508\ridebound-scratchpad\optimize\codex-debate\claude-work\pdf\hoerl-zwick-2022.pdf'
  'sp' = 'C:\PDF\Paper\s00291-026-00847-0.pdf'
  'elmi' = 'C:\Users\quang\AppData\Local\Temp\claude\e--Code-RideBound\4f238113-dd3b-4bd1-b13f-53613b57f0e6\scratchpad\ch2\dl-elmi\elmi2026.pdf'
  'mtkarri' = 'C:\Users\quang\AppData\Local\Temp\claude\e--Code-RideBound\4f238113-dd3b-4bd1-b13f-53613b57f0e6\scratchpad\judge-dl-mtkarri\mtkarri.pdf'
}
foreach ($key in $inputs.Keys) {
  $content = & 'C:\Program Files\Git\mingw64\bin\pdftotext.exe' -enc UTF-8 -layout $inputs[$key] -
  if ($LASTEXITCODE -ne 0) { throw "pdftotext failed: $key" }
  $path = Join-Path $base ('agent-' + $key + '-extract.txt')
  $file = [System.IO.File]::Open($path, [System.IO.FileMode]::CreateNew)
  $writer = [System.IO.StreamWriter]::new($file, [System.Text.UTF8Encoding]::new($false))
  try { $writer.Write(($content -join "`n")) } finally { $writer.Dispose() }
  Write-Output "$key : $($inputs[$key]) : $path"
}