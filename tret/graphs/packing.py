"""Kernel grid packing family builders (M15, K7, K10, K24, S15^(3), S29)."""
from __future__ import annotations
from typing import List, Tuple

from .ops import Edge, undirected


def build_K7() -> Tuple[int, List[Edge], dict]:
    edges: List[Edge] = []
    for i in range(6):
        edges.append((1 + i, 1 + ((i + 1) % 6)))
        edges.append((0, 1 + i))
    return 7, undirected(edges), {"n_central": 1, "equatorial_covering_n": 6, "family": "K7"}


def build_M15() -> Tuple[int, List[Edge], dict]:
    edges: List[Edge] = []
    for i in range(6):
        edges.append((1 + i, 1 + (i + 1) % 6))
    for e in range(1, 7):
        edges.append((0, e))
    edges += [(0, 7), (0, 8)]
    for d in range(9, 13):
        edges.append((0, d))
    edges += [(7, 9), (7, 10), (8, 11), (8, 12)]
    edges += [(9, 1), (9, 2), (10, 2), (10, 3), (11, 4), (11, 5), (12, 5), (12, 6)]
    edges += [(13, 0), (14, 0), (13, 7), (14, 8)]
    return 15, undirected(edges), {"n_central": 1, "equatorial_covering_n": 6, "family": "M15"}


def build_K10() -> Tuple[int, List[Edge], dict]:
    edges: List[Edge] = []
    for i in range(8):
        edges.append((2 + i, 2 + ((i + 1) % 8)))
    pairs = [(2, 3), (4, 5), (6, 7), (8, 9)]
    edges.extend(pairs)
    for e in range(2, 10):
        edges.append((0, e))
        edges.append((1, e))
    edges.append((0, 1))
    return 10, undirected(edges), {"n_central": 2, "equatorial_covering_n": 8, "family": "K10"}


def build_K24() -> Tuple[int, List[Edge], dict]:
    # K10 base + top/bot 7-caps (simplified residual vertical stack)
    n10, e10, _ = build_K10()
    edges = list(e10)
    # top cap Ct=10, Et=11..16; bot Cb=17, Eb=18..23
    Ct, Cb = 10, 17
    for i in range(6):
        edges.append((11 + i, 11 + ((i + 1) % 6)))
        edges.append((Ct, 11 + i))
        edges.append((18 + i, 18 + ((i + 1) % 6)))
        edges.append((Cb, 18 + i))
    # attach both centrals to both caps
    for c in (0, 1):
        edges.append((c, Ct))
        edges.append((c, Cb))
    # angular map 8->6 approx: each cap spoke to two equatorial
    for i in range(6):
        j = 2 + (i % 8)
        j2 = 2 + ((i + 1) % 8)
        edges.append((11 + i, j))
        edges.append((18 + i, j2))
    return 24, undirected(edges), {"n_central": 4, "equatorial_covering_n": 8, "family": "K24"}


def build_S15_3() -> Tuple[int, List[Edge], dict]:
    """3 centrals + 12 equatorial dodecagon (C3 six-neighbour rule)."""
    edges: List[Edge] = []
    # core K3
    edges += [(0, 1), (1, 2), (2, 0)]
    # dodecagon 3..14
    for i in range(12):
        edges.append((3 + i, 3 + ((i + 1) % 12)))
    # six outer neighbours per central under C3 step-4 sectors
    for i in range(3):
        for k in range(6):
            edges.append((i, 3 + ((k + 4 * i) % 12)))
    part = {
        "n_central": 3,
        "equatorial_covering_n": 12,
        "family": "S15_3",
        "C_core": 3,
        "E_dodec": 12,
    }
    return 15, undirected(edges), part


def build_S29() -> Tuple[int, List[Edge], dict]:
    """S15^(3) + K7 top + K7 bot; 5 centrals locked."""
    n15, e15, p15 = build_S15_3()
    edges = list(e15)
    # top: Ct=15, Et=16..21; bot: Cb=22, Eb=23..28
    Ct, Cb = 15, 22
    for i in range(6):
        edges.append((16 + i, 16 + ((i + 1) % 6)))
        edges.append((Ct, 16 + i))
        edges.append((23 + i, 23 + ((i + 1) % 6)))
        edges.append((Cb, 23 + i))
    # core to caps
    for c in (0, 1, 2):
        edges.append((c, Ct))
        edges.append((c, Cb))
    # angular map Z6 -> Z12, i -> 2i
    for i in range(6):
        j = 3 + ((2 * i) % 12)
        j2 = 3 + ((2 * i + 1) % 12)
        edges.append((16 + i, j))
        edges.append((16 + i, j2))
        edges.append((23 + i, j))
        edges.append((23 + i, j2))
    part = {
        "n_central": 5,
        "equatorial_covering_n": 12,
        "family": "S29",
        "layers": "S15_3 + K7 top + K7 bot",
        "C_core": 3,
        "C_caps": 2,
    }
    return 29, undirected(edges), part


def build_S29_throat() -> Tuple[int, List[Edge], dict]:
    n29, e29, p29 = build_S29()
    edges = list(e29)
    T = 29
    for c in (0, 1, 2, 15, 22):
        edges.append((T, c))
    part = {**p29, "family": "S29_throat", "throat": True, "n_central": 5}
    return 30, undirected(edges), part


FAMILY_BUILDERS = {
    "K7": build_K7,
    "M15": build_M15,
    "K10": build_K10,
    "K24": build_K24,
    "S15_3": build_S15_3,
    "S29": build_S29,
    "S29_throat": build_S29_throat,
}


def list_families() -> List[str]:
    return list(FAMILY_BUILDERS.keys())


def build_family(name: str):
    if name not in FAMILY_BUILDERS:
        raise KeyError(f"unknown family {name}; known={list_families()}")
    return FAMILY_BUILDERS[name]()
