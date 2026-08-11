#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret.recovery.maxwell import run_maxwell_recovery
import json
print(json.dumps(run_maxwell_recovery(), indent=2))
