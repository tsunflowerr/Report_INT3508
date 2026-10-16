$ErrorActionPreference = 'Stop'
$taskPdf = 'C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/ch2/dl-elmi/elmi2026.pdf'
$taskText = & 'C:/Program Files/Git/mingw64/bin/pdftotext.exe' -layout -f 6 -l 6 $taskPdf - 2>&1
$taskText += & 'C:/Program Files/Git/mingw64/bin/pdftotext.exe' -layout -f 13 -l 14 $taskPdf - 2>&1
$taskResult = ($taskText | Out-String)
$taskOutPath = Join-Path $PSScriptRoot 'core-body-probe-output-v2.txt'
$taskStream = [System.IO.File]::Open($taskOutPath,[System.IO.FileMode]::CreateNew,[System.IO.FileAccess]::Write)
$taskWriter = New-Object System.IO.StreamWriter($taskStream,(New-Object System.Text.UTF8Encoding($false)))
try { $taskWriter.Write($taskResult) } finally { $taskWriter.Dispose() }
$taskResult

