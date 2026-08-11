"""Chiral mode spectral weights + I_W DM-band mix (A301–A302)."""
from __future__ import annotations
import math
from .constants import I_W
from .graphs.packing import build_S15_3, build_S29
from .graphs.ops import laplacian_spectrum, spectral_weights, h1
from .soft import three_band


def run_chiral_spectral() -> dict:
    results = {}
    for name, builder in [("S15_3", build_S15_3), ("S29", build_S29)]:
        nV, edges, part = builder()
        eigs = laplacian_spectrum(nV, edges)
        sw = spectral_weights(eigs)
        H1 = h1(nV, edges)
        results[name] = {
            "nV": nV,
            "nE": len(edges),
            "H1": H1,
            "cycle_density": H1 / (2 * len(edges)),
            "H1_mass": H1 / (H1 + nV),
            **{k: sw[k] for k in ("lambda2", "degen_multiplet_size", "W_degen", "Z_spec", "lowest_mode_weight")},
            "spectrum_head": eigs[:8],
            "partition": part,
        }
    band = three_band()
    rho_DM = band["rho_DM"]
    split = {
        "rho_DM": rho_DM,
        "rho_chi": rho_DM * I_W,
        "rho_DM_nonchi": rho_DM * (1 - I_W),
        "pct": {
            "V": band["pct"]["V"],
            "DM_nonchi": 100 * rho_DM * (1 - I_W),
            "DM_chi": 100 * rho_DM * I_W,
            "DE": band["pct"]["DE"],
        },
        "sum_pct": band["pct"]["V"] + 100 * rho_DM + band["pct"]["DE"],
    }
    return {
        "instrument": "chiral_spectral_weights",
        "graphs": results,
        "I_W": I_W,
        "DM_band_split": split,
        "claim_spectral": "C residual",
        "claim_particle_ID": "X",
        "free_params": 0,
    }
