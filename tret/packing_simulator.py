"""Kernel grid packing simulator — census, stability ranking, dynamics hooks."""
from __future__ import annotations
from .graphs.packing import FAMILY_BUILDERS, list_families, build_family
from .graphs.ops import inspect_graph
from .soft import extended_census, soft_only_abundance, soft_diameter, three_band
from .dynamics import run_dynamics
from .gamma_limit import run_gamma_limit
from .chiral import run_chiral_spectral


def simulate_all_families() -> dict:
    reports = {}
    for name in list_families():
        nV, edges, part = build_family(name)
        eq_n = part.get("equatorial_covering_n", 6)
        reports[name] = inspect_graph(name, nV, edges, eq_n, part)
    # ranking by stability score
    ranking = sorted(
        ((n, r["stability_score"]) for n, r in reports.items()),
        key=lambda x: -x[1],
    )
    return {
        "instrument": "kernel_grid_packing_simulator",
        "families": reports,
        "ranking": ranking,
        "census": extended_census(),
        "soft_only": soft_only_abundance(),
        "soft_diameter": soft_diameter(),
        "three_band": three_band(),
        "gamma_limit": run_gamma_limit(),
        "chiral": run_chiral_spectral(),
    }


def simulate_family(name: str, with_dynamics: bool = True, steps: int = 100) -> dict:
    nV, edges, part = build_family(name)
    eq_n = part.get("equatorial_covering_n", 6)
    report = inspect_graph(name, nV, edges, eq_n, part)
    out = {"graph": report}
    if with_dynamics and name != "S29_throat":
        out["dynamics"] = run_dynamics(name, steps=steps)
    return out
