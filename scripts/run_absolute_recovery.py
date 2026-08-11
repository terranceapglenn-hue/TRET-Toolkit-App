#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret.recovery.absolute import run_absolute_recovery
import json
print(json.dumps(run_absolute_recovery(), indent=2, default=str))
