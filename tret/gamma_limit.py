"""Discrete variational Γ-limit residual soft energy (A299–A300)."""
from __future__ import annotations
import math
from .soft import soft
from .constants import N_STAR_PACKING


def run_gamma_limit(census=(4, 6, 8, 10, 12)) -> dict:
    E0 = {n: soft(n) for n in census}
    soft_max = max(E0.values())
    soft_min = min(E0.values())
    diam = soft_max - soft_min
    eps_table = []
    for eps in (1.0, 0.1, 0.01, 0.001, 1e-6):
        vals = {n: soft(n) + eps * (n / 2.0) for n in census}
        argmin = min(vals, key=vals.get)
        eps_table.append({"eps": eps, "argmin": argmin, "selects_n_star": argmin == N_STAR_PACKING})
    Z = sum(math.exp(-soft(n)) for n in census)
    p_eq = {n: math.exp(-soft(n)) / Z for n in census}
    return {
        "instrument": "variational_gamma_limit",
        "E0": E0,
        "soft_min": soft_min,
        "soft_max": soft_max,
        "diam_soft": diam,
        "lambda_V": math.exp(-diam),
        "R_oc": math.exp(diam) - 1.0,
        "unique_minimizer": [n for n in census if E0[n] == soft_min],
        "eps_table": eps_table,
        "selects_n_star_small_eps": all(r["selects_n_star"] for r in eps_table if r["eps"] < 1.0),
        "p_eq_tau1": p_eq,
        "Z_soft": Z,
        "geometry_realiser": 2 * N_STAR_PACKING,
        "claim": "C discrete packing-sector; continuum Gamma beyond packing O",
        "free_params": 0,
    }
