"""Remaining soft spots / open gaps + concrete next-step recovery programs."""
from __future__ import annotations
from .constants import LOCKS, VERSION

# Concrete next programs — what to implement next for maximal rigor closure
NEXT_PROGRAMS = [
    {
        "id": "NP1_dual_route_open_closed_homogeneity",
        "title": "Residual free-energy homogeneity theorem for packing vs throat weight",
        "closes": "Omega_b = lambda_V as C (if successful) or strengthens X→O obstruction",
        "status": "CLOSED_OBSTRUCTION_A303",
        "concrete_steps": [
            "Write residual free-energy functional F[pack, throat, chiral] with dual-route moduli only",
            "Prove Gamma-limit / EL stationarity selects weight ratio without free params",
            "If free param appears, certify obstruction (honest X/O, not forced C)",
            "Extend run_absolute_recovery with NP1 certificate checks",
        ],
        "related": ["A297", "A300", "A302"],
    },
    {
        "id": "NP2_continuum_Gamma_beyond_packing",
        "title": "Continuum Gamma-limit beyond discrete packing census",
        "closes": "continuum_Gamma_beyond_packing O → C or certified obstruction",
        "status": "CLOSED_SPLIT_A304",
        "concrete_steps": [
            "Define continuum residual energy on torus/hex domain with soft density",
            "Prove or disprove Gamma-convergence to soft-zero hex packing measure",
            "Link to P6 spectral floor Lambda_res without new free params",
        ],
        "related": ["A299", "A174", "P6"],
    },
    {
        "id": "NP3_G_N_dual_route",
        "title": "G_N dual-route absolute theorem attempt",
        "closes": "G_N dual-route OPEN",
        "status": "CLOSED_KILL_A305",
        "concrete_steps": [
            "Inventory residual geometric candidates for Newton constant",
            "Apply kill-matrix protocol (A193) to each candidate",
            "Do not claim C unless free_params=0 and all countermodels die",
        ],
        "related": ["A192", "A284"],
    },
    {
        "id": "NP4_LQCD_S1_S5_bridges",
        "title": "LQCD residual bridges S1–S5 (w0/t0/fπ dictionary M)",
        "closes": "S1–S5 M-class dictionary rigor",
        "status": "CLOSED_M_A306",
        "concrete_steps": [
            "Formalize residual→LQCD scale-setting map as M operators",
            "Add chi_t residual witnesses; OOS nuclear chart checks",
            "Keep absolute continuum ≡ free A0 as false/I",
        ],
        "related": ["A281", "A283"],
    },
    {
        "id": "NP5_atomic_spectroscopic_nl",
        "title": "Atomic spectroscopic nℓ dual-route C attempt",
        "closes": "atomic nℓ as C or certified O",
        "status": "CLOSED_KILLED_A307",
        "concrete_steps": [
            "Map residual shell ranks (2,6,8) to spectroscopic shells carefully",
            "Kill overclaim of absolute spectroscopic recovery",
            "M-class residual shell dictionary only unless free_params=0 proof",
        ],
        "related": ["A231", "A235"],
    },
    {
        "id": "NP6_chiral_dynamics_PDE",
        "title": "Runnable residual chiral PDE on S15^(3)/S29 with mu5",
        "closes": "dynamics property investigation depth",
        "status": "CLOSED_OPERATIONAL_A309",
        "concrete_steps": [
            "Couple dynamics.py springs to residual mu5 orientation field on core K3",
            "Evolve CME/CVE residual currents under H_cont (structure C)",
            "Do not assign PQ-axion particle ID (X)",
        ],
        "related": ["A184", "A301", "A302"],
    },
    {
        "id": "NP7_OOS_abundance_nature_table",
        "title": "Out-of-sample nature correlation table with fixed residual dictionary",
        "closes": "nature correlation rigor (still X for particle ID)",
        "status": "CLOSED_FROZEN_A310",
        "concrete_steps": [
            "Freeze soft-only + multi-central census weights",
            "Map families to material/crystal/quasi classes as X dictionary only",
            "Report calibration vs OOS separately",
        ],
        "related": ["A208", "A295"],
    },
]

CLOSED_STRUCTURE = [
    "mapping_sectors A159–A160",
    "Maxwell packing under H_cont A192–A194",
    "multi-central K10/K24/S15_3/S29",
    "soft_max selection + lambda_V residual scale",
    "R_oc open/closed residual ratio",
    "three-band residual ladder structure",
    "discrete packing-sector Gamma-limit",
    "chiral spectral weights + I_W mix structure",
    "throat open channel under H_cont",
    "U1–U8 unrestricted kill battery",
]

OPEN_GAPS = [
    "unrestricted_open_system_closed = false (by evidence)",
    "G_N dual-route absolute theorem",
    "atomic spectroscopic nℓ as dual-route C",
    "absolute confinement theorem (area law free-A0)",
    "S1–S5 LQCD bridges (M dictionary rigor)",
    "Omega_b ≡ lambda_V absolute dual-route C",
    "continuum Gamma beyond packing sector",
]

IMPOSSIBLE = [
    "absolute_MeV_zero_anchor",
    "residual-only unrestricted packing Maxwell from free A0",
    "exact α / α_s dual-route monomial",
    "LQCD continuum ≡ free residual A0",
    "residual adjacency ≡ Bell entanglement theorem",
]


def gap_board() -> dict:
    return {
        "version": VERSION,
        "locks": LOCKS,
        "closed_structure": CLOSED_STRUCTURE,
        "open_gaps": OPEN_GAPS,
        "impossible": IMPOSSIBLE,
        "next_programs": NEXT_PROGRAMS,
        "soft_spots": [
            {
                "spot": "Absolute cosmology identification of residual scales",
                "severity": "Numerology risk if Omega forced equal to lambda_V without dual-route theorem",
                "next": "NP1",
            },
            {
                "spot": "Continuum extension of discrete Gamma-limit",
                "severity": "Overclaiming packing-sector C as continuum C",
                "next": "NP2",
            },
            {
                "spot": "Particle ID for residual light/chiral modes",
                "severity": "Neutrino/ALP dictionary is X not C",
                "next": "NP6 + honesty firewall",
            },
            {
                "spot": "SI conversion anchors",
                "severity": "External M anchors required; zero-anchor MeV impossible",
                "next": "SI_Recover only as M",
            },
        ],
    }
