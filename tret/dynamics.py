"""Residual free-energy dynamics on kernel grids (runnable property investigation)."""
from __future__ import annotations
import math
import random
from typing import Dict, List, Sequence, Tuple

from .graphs.ops import degree_sequence, h1, algebraic_connectivity
from .graphs.packing import build_family, list_families
from .soft import soft


def residual_edge_energy(nV: int, edges: Sequence[Tuple[int, int]], positions: List[List[float]], k: float = 1.0) -> float:
    """Harmonic residual spring energy on edges + soft equatorial penalty external."""
    E = 0.0
    for a, b in edges:
        dx = positions[a][0] - positions[b][0]
        dy = positions[a][1] - positions[b][1]
        r = math.hypot(dx, dy)
        E += 0.5 * k * (r - 1.0) ** 2
    return E


def init_positions(nV: int, seed: int = 0) -> List[List[float]]:
    rng = random.Random(seed)
    return [[rng.uniform(-1, 1), rng.uniform(-1, 1)] for _ in range(nV)]


def step_gradient(
    nV: int,
    edges: Sequence[Tuple[int, int]],
    positions: List[List[float]],
    dt: float = 0.05,
    k: float = 1.0,
) -> Tuple[List[List[float]], float]:
    forces = [[0.0, 0.0] for _ in range(nV)]
    for a, b in edges:
        dx = positions[b][0] - positions[a][0]
        dy = positions[b][1] - positions[a][1]
        r = math.hypot(dx, dy) + 1e-12
        # spring to rest length 1
        f = k * (r - 1.0)
        fx, fy = f * dx / r, f * dy / r
        forces[a][0] += fx
        forces[a][1] += fy
        forces[b][0] -= fx
        forces[b][1] -= fy
    # mild centering force
    cx = sum(p[0] for p in positions) / nV
    cy = sum(p[1] for p in positions) / nV
    for i in range(nV):
        forces[i][0] -= 0.05 * (positions[i][0] - cx)
        forces[i][1] -= 0.05 * (positions[i][1] - cy)
        positions[i][0] += dt * forces[i][0]
        positions[i][1] += dt * forces[i][1]
    E = residual_edge_energy(nV, edges, positions, k=k)
    return positions, E


def run_dynamics(family: str = "S15_3", steps: int = 200, seed: int = 0) -> dict:
    nV, edges, part = build_family(family)
    eq_n = part.get("equatorial_covering_n", 6)
    pos = init_positions(nV, seed=seed)
    history = []
    for t in range(steps):
        pos, E = step_gradient(nV, edges, pos)
        if t % max(1, steps // 20) == 0 or t == steps - 1:
            history.append({"t": t, "E": E})
    # final graph properties
    props = {
        "family": family,
        "nV": nV,
        "nE": len(edges),
        "H1": h1(nV, edges),
        "lambda2": algebraic_connectivity(nV, edges),
        "soft": soft(eq_n) if eq_n else None,
        "eq_n": eq_n,
        "partition": part,
        "final_energy": history[-1]["E"] if history else None,
        "initial_energy": history[0]["E"] if history else None,
        "energy_decreased": (
            history[-1]["E"] < history[0]["E"] if len(history) >= 2 else None
        ),
        "history": history,
        "final_positions_sample": pos[: min(5, nV)],
    }
    return props


def run_all_family_dynamics(steps: int = 100) -> dict:
    out = {}
    for fam in list_families():
        if fam == "S29_throat":
            continue  # skip throat for layout dynamics (extra node)
        out[fam] = run_dynamics(fam, steps=steps)
    return out
