#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret.packing_simulator import simulate_all_families
import json
print(json.dumps(simulate_all_families(), indent=2, default=str))
