"""Graph ops: homology, spectrum, connectivity, stability."""
from __future__ import annotations
import math
from collections import defaultdict, deque
from typing import Dict, Iterable, List, Sequence, Set, Tuple

Edge = Tuple[int, int]


def undirected(edges: Iterable[Sequence[int]]) -> List[Edge]:
    return sorted({tuple(sorted((int(a), int(b)))) for a, b in edges if a != b})


def n_components(nV: int, edges: Sequence[Edge]) -> int:
    adj: Dict[int, List[int]] = defaultdict(list)
    for a, b in edges:
        if 0 <= a < nV and 0 <= b < nV:
            adj[a].append(b)
            adj[b].append(a)
    seen: Set[int] = set()
    c = 0
    for s in range(nV):
        if s in seen:
            continue
        c += 1
        q = deque([s])
        seen.add(s)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return c


def connected(nV: int, edges: Sequence[Edge]) -> bool:
    return n_components(nV, edges) == 1


def h1(nV: int, edges: Sequence[Edge]) -> int:
    return len(edges) - nV + n_components(nV, edges)


def degree_sequence(nV: int, edges: Sequence[Edge]) -> List[int]:
    deg = [0] * nV
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return deg


def edge_connectivity_lower(nV: int, edges: Sequence[Edge]) -> int:
    deg = degree_sequence(nV, edges)
    return min(deg) if deg else 0


def laplacian_spectrum(nV: int, edges: Sequence[Edge]) -> List[float]:
    L = [[0.0] * nV for _ in range(nV)]
    for a, b in edges:
        L[a][a] += 1.0
        L[b][b] += 1.0
        L[a][b] -= 1.0
        L[b][a] -= 1.0
    A = [row[:] for row in L]
    for _ in range(120 * max(nV, 1)):
        mval = 0.0
        p = q = 0
        for i in range(nV):
            for j in range(i + 1, nV):
                if abs(A[i][j]) > mval:
                    mval = abs(A[i][j])
                    p, q = i, j
        if mval < 1e-14:
            break
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        tau = (aqq - app) / (2 * apq) if apq != 0 else 0.0
        t = (
            math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1 + tau * tau))
            if tau != 0
            else 1.0
        )
        c = 1.0 / math.sqrt(1 + t * t)
        s = t * c
        for i in range(nV):
            if i in (p, q):
                continue
            aip, aiq = A[i][p], A[i][q]
            A[i][p] = A[p][i] = c * aip - s * aiq
            A[i][q] = A[q][i] = s * aip + c * aiq
        A[p][p] = app - t * apq
        A[q][q] = aqq + t * apq
        A[p][q] = A[q][p] = 0.0
    return sorted(A[i][i] for i in range(nV))


def algebraic_connectivity(nV: int, edges: Sequence[Edge]) -> float:
    eigs = laplacian_spectrum(nV, edges)
    return max(0.0, eigs[1] if nV > 1 else 0.0)


def spectral_weights(eigs: Sequence[float], T: float = 1.0) -> dict:
    pos = [e for e in eigs if e > 1e-10]
    Z = sum(math.exp(-lam / T) for lam in pos)
    weights = [math.exp(-lam / T) / Z for lam in pos] if Z else []
    degen = []
    if pos:
        lam2 = pos[0]
        degen = [i for i, lam in enumerate(pos) if abs(lam - lam2) < 1e-8]
    W_degen = sum(weights[i] for i in degen) if degen else 0.0
    return {
        "positive": pos,
        "Z_spec": Z,
        "weights": weights,
        "lambda2": pos[0] if pos else None,
        "degen_multiplet_size": len(degen),
        "W_degen": W_degen,
        "lowest_mode_weight": weights[0] if weights else None,
    }


def stability_score(nV: int, edges: Sequence[Edge], eq_n: int) -> dict:
    from ..soft import soft
    s = soft(eq_n)
    gap = algebraic_connectivity(nV, edges)
    kappa = edge_connectivity_lower(nV, edges)
    soft_factor = math.exp(-s) if math.isfinite(s) else 0.0
    gap_factor = gap / (1.0 + gap)
    kappa_factor = kappa / (1.0 + kappa)
    score = soft_factor * gap_factor * kappa_factor
    deg = degree_sequence(nV, edges)
    return {
        "nV": nV,
        "nE": len(edges),
        "H1": h1(nV, edges),
        "connected": connected(nV, edges),
        "min_degree": min(deg) if deg else 0,
        "max_degree": max(deg) if deg else 0,
        "mean_degree": sum(deg) / nV if nV else 0.0,
        "eq_n": eq_n,
        "soft": s if math.isfinite(s) else None,
        "lambda2": gap,
        "kappa_lower": kappa,
        "stability_score": score,
    }


def inspect_graph(name: str, nV: int, edges: Sequence[Edge], eq_n: int, part: dict | None = None) -> dict:
    st = stability_score(nV, edges, eq_n)
    eigs = laplacian_spectrum(nV, edges)
    sw = spectral_weights(eigs)
    out = {
        "name": name,
        **st,
        "partition": part or {},
        "spectrum_head": eigs[:8],
        "spectral": sw,
        "cycle_density": st["H1"] / (2 * st["nE"]) if st["nE"] else 0.0,
        "H1_mass": st["H1"] / (st["H1"] + nV) if (st["H1"] + nV) else 0.0,
    }
    return out
