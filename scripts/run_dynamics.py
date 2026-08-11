#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret.dynamics import run_dynamics
import json, sys
fam=sys.argv[1] if len(sys.argv)>1 else 'S15_3'
print(json.dumps(run_dynamics(fam, steps=120), indent=2, default=str))
