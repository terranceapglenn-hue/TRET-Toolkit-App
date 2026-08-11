#!/usr/bin/env python3
"""Run all TRET toolkit instruments; write certificates."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tret import (
    VERSION, LOCKS,
    run_mapping_matching, run_maxwell_recovery, run_absolute_recovery, run_si_recover,
    simulate_all_families, run_gamma_limit, run_chiral_spectral, gap_board,
    run_dynamics,
)


def main() -> int:
    out_dir = ROOT / "data" / "results"
    cert_dir = ROOT / "data" / "certificates"
    out_dir.mkdir(parents=True, exist_ok=True)
    cert_dir.mkdir(parents=True, exist_ok=True)

    results = {
        "version": VERSION,
        "locks": LOCKS,
        "mapping_matching": run_mapping_matching(),
        "maxwell_recovery": run_maxwell_recovery(),
        "si_recover": run_si_recover(),
        "absolute_recovery": run_absolute_recovery(),
        "packing_simulator": simulate_all_families(),
        "gamma_limit": run_gamma_limit(),
        "chiral_spectral": run_chiral_spectral(),
        "dynamics_S15_3": run_dynamics("S15_3", steps=80),
        "dynamics_S29": run_dynamics("S29", steps=80),
        "gap_board": gap_board(),
    }

    checks = {
        "mapping": results["mapping_matching"]["all_ok"],
        "maxwell": results["maxwell_recovery"]["all_ok"],
        "si": results["si_recover"]["all_ok"],
        "absolute": results["absolute_recovery"]["all_ok"],
        "soft6_unique": results["packing_simulator"]["soft_only"]["packing_max_n"] == 6,
        "lambda_V": abs(results["gamma_limit"]["lambda_V"] - __import__("math").exp(-3)) < 1e-12,
        "S15_3_nE": results["packing_simulator"]["families"]["S15_3"]["nE"] == 33,
        "S29_nV": results["packing_simulator"]["families"]["S29"]["nV"] == 29,
        "S15_3_H1": results["packing_simulator"]["families"]["S15_3"]["H1"] == 19,
        "dynamics_energy_down_S15": results["dynamics_S15_3"]["energy_decreased"] is True,
        "gamma_selects_n6": results["gamma_limit"]["selects_n_star_small_eps"],
        "chiral_S15_degen2": results["chiral_spectral"]["graphs"]["S15_3"]["degen_multiplet_size"] == 2,
        "MeV_impossible": LOCKS["absolute_MeV_zero_anchor"] == "IMPOSSIBLE",
        "unrestricted_false": LOCKS["unrestricted_open_system_closed"] is False,
        "free_params_0": LOCKS["free_params_primary"] == 0,
    }
    all_ok = all(checks.values())
    results["checks"] = checks
    results["all_ok"] = all_ok

    (out_dir / "all_instruments.json").write_text(json.dumps(results, indent=2, default=str))
    # individual
    for key in ("mapping_matching", "maxwell_recovery", "absolute_recovery", "si_recover",
                "packing_simulator", "gamma_limit", "chiral_spectral", "gap_board"):
        (out_dir / f"{key}.json").write_text(json.dumps(results[key], indent=2, default=str))

    cert = {
        "package": "TRET-Toolkit-App",
        "version": VERSION,
        "all_ok": all_ok,
        "n_checks": len(checks),
        "n_pass": sum(1 for v in checks.values() if v),
        "failed": [k for k, v in checks.items() if not v],
        "locks": LOCKS,
        "ranking": results["packing_simulator"]["ranking"],
        "lambda_V": results["gamma_limit"]["lambda_V"],
        "three_band_pct": results["packing_simulator"]["three_band"]["pct"],
        "next_programs": [p["id"] for p in results["gap_board"]["next_programs"]],
    }
    (cert_dir / "MASTER_toolkit_certificate.json").write_text(json.dumps(cert, indent=2))

    print(json.dumps({
        "all_ok": all_ok,
        "n_checks": len(checks),
        "failed": cert["failed"],
        "ranking": cert["ranking"],
        "lambda_V": cert["lambda_V"],
        "three_band_pct": cert["three_band_pct"],
        "next_programs": cert["next_programs"],
    }, indent=2))
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
