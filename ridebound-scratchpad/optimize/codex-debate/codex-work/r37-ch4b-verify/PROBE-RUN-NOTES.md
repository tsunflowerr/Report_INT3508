# R37 probe execution notes

All scripts and outputs are retained; no existing file was overwritten. All writes stayed in r37-ch4b-verify.

- `probe-source-schema.py` initially stopped on an adapter-to-runner checkpoint request without a `content` field. It produced no output file. Error: `KeyError: 'content'` at line 36. This was a schema-inspection error, not a source-data defect.
- `probe-source-schema-v2.py` restricts checkpoint extraction to runner-to-adapter messages. It completed and exclusive-created `probe-source-schema-v2.json`. The source snapshot was larger than intended (about 2,7 MB) because the inspected travel snapshot and first full rider ledger were included; it is preserved under the user's instruction. It is inspection material, not the final numerical evidence.
- `verify-numbers.py` was started before the session interruption. On resume its process identifier was unavailable and no final JSON/text report existed. No completion is claimed for that attempt.
- `verify-numbers-v2.py` preserves the original script, adds an exclusive incremental text log and respects the registered effective `-rerun1` directory convention for original incomplete baseline folders. It completed with all assertions passing and created `verify-numbers-v2.txt` and `verify-numbers-v2.json`.
- `verify-supplement.py` completed with all reference/cohort assertions passing and created its exclusive `.txt` and `.json` outputs.
- Agent files include a first PowerShell ref script that failed to parse before execution because of UTF-8/BOM interpretation and a separate `-v2.ps1` that completed. The root independently confirmed its substantive ref results with Python.

No simulation, installation, compilation, model fitting, test execution, source/draft edit or deletion was performed. The successful Python commands used the existing interpreter at E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe with -I -B, suppressing bytecode writes.
