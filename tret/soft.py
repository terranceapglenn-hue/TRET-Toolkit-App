"""Soft cost, soft-only abundance, soft diameter / lambda_V."""
from __future__ import annotations
import math
from typing import Dict, Iterable, List, Sequence

from .constants import N_STAR_PACKING


def soft(n: int) -> float:
    """Even soft cost |n/2 - 3|; odd coverings are non-class (inf)."""
    if n % 2 != 0:
        return float("inf")
    return abs(n / 2.0 - 3.0)


def soft_table(ns: Sequence[int] = (4, 6, 8, 10, 12)) -> Dict[int, float]:
    return {int(n): soft(int(n)) for n in ns}


def soft_only_abundance(ns: Sequence[int] = (4, 6, 8, 10, 12)) -> dict:
    weights = {n: math.exp(-soft(n)) if math.isfinite(soft(n)) else 0.0 for n in ns}
    Z = sum(weights.values())
    shares = {n: (w / Z if Z else 0.0) for n, w in weights.items()}
    return {
        "ns": list(ns),
        "weights": weights,
        "Z_soft": Z,
        "shares": shares,
        "pct": {n: 100.0 * s for n, s in shares.items()},
        "packing_max_n": max(shares, key=shares.get),
        "p_soft0": shares.get(6, 0.0),
        "p_soft_pos": 1.0 - shares.get(6, 0.0),
        "F_closed": -math.log(Z) if Z > 0 else None,
    }


def soft_diameter(ns: Sequence[int] = (4, 6, 8, 10, 12)) -> dict:
    st = soft_table(ns)
    finite = {n: s for n, s in st.items() if math.isfinite(s)}
    smin = min(finite.values())
    smax = max(finite.values())
    diam = smax - smin
    lam_V = math.exp(-diam)
    return {
        "soft_table": finite,
        "soft_min": smin,
        "soft_max": smax,
        "diam_soft": diam,
        "lambda_V": lam_V,
        "lambda_dark": 1.0 - lam_V,
        "R_oc": (1.0 - lam_V) / lam_V if lam_V > 0 else None,
        "n_star": N_STAR_PACKING,
        "n_eq_forced_C3": 2 * N_STAR_PACKING,
        "claim_structure": "C",
        "claim_Omega_ID": "X",
    }


def three_band() -> dict:
    e1, e3 = math.exp(-1.0), math.exp(-3.0)
    rho_V, rho_DM, rho_DE = e3, e1 - e3, 1.0 - e1
    return {
        "rho_V": rho_V,
        "rho_DM": rho_DM,
        "rho_DE": rho_DE,
        "sum": rho_V + rho_DM + rho_DE,
        "pct": {
            "V": 100.0 * rho_V,
            "DM": 100.0 * rho_DM,
            "DE": 100.0 * rho_DE,
        },
        "formulas": {
            "V": "e^{-3}",
            "DM": "e^{-1}-e^{-3}",
            "DE": "1-e^{-1}",
        },
        "claim_structure": "C",
        "claim_Omega_ID": "X",
    }


def combinatorial_mult(n_eq: int, n_central: int) -> int:
    # binom(n+c, c)
    from math import comb
    return comb(n_eq + n_central, n_central)


def extended_census(
    ns: Sequence[int] = (4, 6, 8, 10, 12),
    centrals: Sequence[int] = (1, 2, 3, 4, 5),
) -> dict:
    rows = []
    Z = 0.0
    for n in ns:
        for c in centrals:
            s = soft(n)
            mult = combinatorial_mult(n, c)
            w = mult * (math.exp(-s) if math.isfinite(s) else 0.0)
            Z += w
            rows.append(
                {
                    "n_eq": n,
                    "n_central": c,
                    "soft": s if math.isfinite(s) else None,
                    "mult": mult,
                    "weight": w,
                }
            )
    for r in rows:
        r["share"] = r["weight"] / Z if Z else 0.0
        r["pct"] = 100.0 * r["share"]
    soft_only = soft_only_abundance(ns)
    return {
        "rows": rows,
        "Z": Z,
        "soft_only": soft_only,
        "systems": {
            "M15_n6_c1": next(r for r in rows if r["n_eq"] == 6 and r["n_central"] == 1),
            "S15_3_n12_c3": next(r for r in rows if r["n_eq"] == 12 and r["n_central"] == 3),
            "S29_n12_c5": next(r for r in rows if r["n_eq"] == 12 and r["n_central"] == 5),
            "K10_n8_c2": next(r for r in rows if r["n_eq"] == 8 and r["n_central"] == 2),
        },
    }
