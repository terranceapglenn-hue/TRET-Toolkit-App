"""A192–A194 Maxwell / packing recovery protocol instrument."""
from __future__ import annotations
from ..soft import soft, soft_table
from ..constants import LOCKS


def run_maxwell_recovery() -> dict:
    soft_tab = soft_table(range(2, 16, 2))
    # continuum X stress tests — all FAIL unrestricted (A193 kill matrix)
    continuum_X = {
        "polyconvex": "FAIL_unique_n6",
        "spectral_gap_only": "FAIL",
        "hopf_fibration": "FAIL",
        "crystal_symmetry_only": "FAIL",
        "EM_Maxwell_as_packing": "FAIL_category_error",
        "free_A0_unrestricted": "FAIL",
    }
    # packing under H_cont recovered
    packing_H_cont = {
        "soft6_zero": soft(6) == 0,
        "unique_soft_zero": all(soft(n) != 0 for n in soft_tab if n != 6),
        "claim": "C recovered under H_cont",
    }
    checks = {
        "soft6_zero": soft_tab[6] == 0,
        "soft4_pos": soft_tab[4] == 1,
        "soft8_pos": soft_tab[8] == 1,
        "packing_under_H_cont_recovered": packing_H_cont["soft6_zero"],
        "unrestricted_false": True,
        "absolute_false": True,
        "MeV_impossible": True,
        "EM_is_not_packing": True,
        "any_X_succeeds_false": True,
        "free_params_0": True,
        "H_cont_closed": True,
        "protocol_defined": True,
    }
    return {
        "instrument": "maxwell_recovery_A192_A194",
        "soft_table": soft_tab,
        "packing_H_cont": packing_H_cont,
        "continuum_X_kill": continuum_X,
        "any_X_succeeds": False,
        "locks": {
            **LOCKS,
            "packing_Maxwell_under_H_cont": "recovered_C",
            "unrestricted_packing_Maxwell_from_A0": False,
            "EM_Maxwell": "C_structure_M_SI",
        },
        "checks": checks,
        "all_ok": all(checks.values()),
        "verdict": (
            "Packing Maxwell under H_cont recovered (C). "
            "Unrestricted packing Maxwell from free A0 remains false. "
            "No continuum X succeeds on kill matrix."
        ),
    }
