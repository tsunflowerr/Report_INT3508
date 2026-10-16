"""Relaunch the sealed task B driver (run_w07.py, unchanged) until no job is pending (W07-AMENDMENTS.md A1).

Why: at 00:22 on 2026-09-30 one power reading was not "AC" when a job finished; the driver's pool then handed every
remaining job to may_start_job() within milliseconds and all 72 were reported "deferred-on-battery" (none started,
none has a log or an output). The driver itself is sealed in W07-PLAN.sha256 and is not edited.
Loop: wait for the given driver PID to exit; then, while a job is pending: if on AC power, run `run_w07.py run` to
completion with stdout/stderr in driver-run-<n>.out/.err (new n each time, mode "x"); otherwise wait. A pending job
whose log already exists ("log-exists-pending") stops the loop, because it needs a person to look.
Usage: python -B relaunch_until_done.py <pid-of-running-driver-or-0>
"""
from __future__ import annotations

import ctypes
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "pilot"))
import run_pilot  # noqa: E402
import run_w07  # noqa: E402


def alive(pid: int) -> bool:
    if pid <= 0:
        return False
    handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
    if not handle:
        return False
    code = ctypes.c_ulong()
    ctypes.windll.kernel32.GetExitCodeProcess(handle, ctypes.byref(code))
    ctypes.windll.kernel32.CloseHandle(handle)
    return code.value == 259  # STILL_ACTIVE


def pending() -> list[str]:
    return [name for name, *_ in run_w07.jobs() if run_w07.state_of(name) == "pending"]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    pid = int(sys.argv[1])
    run_pilot.keep_awake(True)
    try:
        while alive(pid):
            time.sleep(30)
        print(f"{time.strftime('%H:%M:%S')} driver {pid} has exited; pending {len(pending())}", flush=True)
        attempt = 2
        while pending():
            if any((run_w07.LOG_ROOT / f"{name}.log").exists() for name in pending()):
                print("a pending job already has a log: stopping for a person to look", flush=True)
                return 4
            if not run_pilot.may_start_job():
                time.sleep(120)
                continue
            while (HERE / f"driver-run-{attempt}.out").exists():
                attempt += 1
            print(f"{time.strftime('%H:%M:%S')} starting driver attempt {attempt}; pending {len(pending())}", flush=True)
            with open(HERE / f"driver-run-{attempt}.out", "x", encoding="utf-8") as out, \
                    open(HERE / f"driver-run-{attempt}.err", "x", encoding="utf-8") as err:
                code = subprocess.run([str(run_pilot.PYTHON), "-B", str(HERE / "run_w07.py"), "run"], cwd=str(HERE),
                                      stdout=out, stderr=err, check=False).returncode
            print(f"{time.strftime('%H:%M:%S')} driver attempt {attempt} returned {code}; pending {len(pending())}", flush=True)
            attempt += 1
            if code not in (0, 3):
                return code
            if pending():
                time.sleep(120)
        print(f"{time.strftime('%H:%M:%S')} no job pending", flush=True)
        return 0
    finally:
        run_pilot.keep_awake(False)


if __name__ == "__main__":
    raise SystemExit(main())
