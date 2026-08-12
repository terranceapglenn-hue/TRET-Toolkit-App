#!/usr/bin/env python3
"""Run all residual dual-route certificate batteries A303–A351."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "run_A303_A310_gap_closure.py",
    "run_A311_A318_strengthening.py",
    "run_A319_A328_verification.py",
    "run_A329_A333_verification.py",
    "run_A334_A338_verification.py",
    "run_A339_A346_verification.py",
    "run_A347_A351_verification.py",
]

def main() -> int:
    here = Path(__file__).resolve().parent
    results = {}
    ok_all = True
    for name in SCRIPTS:
        path = here / name
        if not path.exists():
            results[name] = {"exists": False, "ok": False}
            ok_all = False
            print(f"MISSING {name}")
            continue
        print(f"=== RUN {name} ===")
        r = subprocess.run([sys.executable, str(path)], cwd=str(here), capture_output=True, text=True)
        text = (r.stdout or "") + (r.stderr or "")
        ok = r.returncode == 0 and ("all_ok" not in text or "true" in text.lower() or r.returncode == 0)
        # prefer parsing last JSON-looking all_ok
        all_ok = r.returncode == 0
        if '"all_ok": false' in text or '"all_ok":false' in text:
            all_ok = False
        if '"all_ok": true' in text or '"all_ok":true' in text:
            all_ok = True
        results[name] = {"exists": True, "returncode": r.returncode, "all_ok": all_ok}
        ok_all = ok_all and all_ok
        print(text[-800:] if len(text) > 800 else text)
        print(f"=== DONE {name} all_ok={all_ok} ===\n")
    out = {"package": "TRET_SUBMISSION_READY_v12.77.0", "results": results, "all_ok": ok_all}
    out_path = here.parents[0] / "results" / "certificates" / "MASTER_ALL_CERTIFICATES.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
    return 0 if ok_all else 1

if __name__ == "__main__":
    raise SystemExit(main())
