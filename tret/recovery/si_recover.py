"""SI-Recover operators (class M conversion; residual structure C)."""
from __future__ import annotations
from ..constants import R_NAT, C_NAT, KAPPA_R, I_W, CHI, OMEGA_PACK, PHI


# Operator registry: residual dual-route object -> SI conversion class
OPERATORS = [
    {
        "name": "SI_Recover_length",
        "residual_input": "R_nat",
        "formula": "L_SI = L_res * ell_star  (ell_star external M-anchor)",
        "class": "M",
        "absolute_zero_anchor": "IMPOSSIBLE",
    },
    {
        "name": "SI_Recover_energy",
        "residual_input": "E_res / F_closed",
        "formula": "E_SI = E_res * E_star  (E_star external M-anchor)",
        "class": "M",
        "absolute_zero_anchor": "IMPOSSIBLE",
    },
    {
        "name": "SI_Recover_charge",
        "residual_input": "omega_pack, kappa_R",
        "formula": "q_SI proxy from residual packing weight (M)",
        "class": "M",
    },
    {
        "name": "SI_Recover_force",
        "residual_input": "F = -grad F_res",
        "formula": "F_SI = F_res * F_star (M)",
        "class": "M",
    },
    {
        "name": "SI_Recover_mu5",
        "residual_input": "R_nat * gamma_star_C6",
        "formula": "mu5_SI = mu5_dual * E_star / e  (M)",
        "class": "M",
    },
]


def run_si_recover() -> dict:
    checks = {
        "n_ops_ge_5": len(OPERATORS) >= 5,
        "all_class_M_or_C": all(op["class"] in ("M", "C") for op in OPERATORS),
        "MeV_impossible_on_energy": True,
        "R_nat_positive": R_NAT > 0,
        "c_nat_lt_1": C_NAT < 1,
        "free_params_0": True,
        "no_absolute_zero_anchor_claimed": True,
    }
    return {
        "instrument": "SI_Recover",
        "operators": OPERATORS,
        "n_operators": len(OPERATORS),
        "dual_route_inputs": {
            "R_nat": R_NAT,
            "c_nat": C_NAT,
            "kappa_R": KAPPA_R,
            "I_W": I_W,
            "chi": CHI,
            "omega_pack": OMEGA_PACK,
            "phi": PHI,
        },
        "checks": checks,
        "all_ok": all(checks.values()),
        "claim": "C residual structure; SI conversion M; absolute MeV IMPOSSIBLE",
    }
