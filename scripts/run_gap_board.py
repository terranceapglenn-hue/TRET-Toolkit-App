#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret.gaps import gap_board
import json
print(json.dumps(gap_board(), indent=2))
