#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret.mapping import run_mapping_matching
import json
print(json.dumps(run_mapping_matching(), indent=2))
