"""TRET dual-route locked constants (free_params_primary=0)."""
from __future__ import annotations
import math

PHI = (1.0 + math.sqrt(5.0)) / 2.0
CHI = PHI ** (-2)
I_W = 1.0 / math.sqrt(5.0)
SIGMA = 1.0 / PHI
KAPPA_R = I_W + CHI
R_NAT = I_W * SIGMA * CHI**6
C_NAT = 1.0 - R_NAT
LAMBDA_NAT = 2.0346272697196173  # residual orientation / P6 floor companion
LAMBDA_RES = 2.03467  # definitional P6 hybrid spectral floor
GAMMA_STAR_C6 = 0.9503155295529548  # residual C6 star (A159 lock set)
GAMMA_WORKING = 0.92048080835  # pure-exp solver of lambda_-(gamma)=Lambda_res
OMEGA_PACK = I_W * CHI

# Mapping sector ranks (A159)
R_PACK, R_EQ, R_CAP = 2, 6, 8
E_SHARP = R_PACK + R_EQ + R_CAP  # 16
N_STAR = 15
RHO_DUAL = E_SHARP - N_STAR  # 1
DEPTHS = {"pack": 0, "eq": 2, "cap": 4}
MUT_CLASS = 12000
N_STAR_PACKING = 6  # packing-Maxwell unique even covering

VERSION = "v7.2.0_A311_A318_toolkit_20260811"

LOCKS = {
    "free_params_primary": 0,
    "H_cont_open_system_closed": True,
    "packing_Maxwell_under_H_cont": "recovered_C",
    "unrestricted_open_system_closed": False,
    "absolute_closed": False,
    "absolute_MeV_zero_anchor": "IMPOSSIBLE",
    "mapping_sectors_closed": True,
    "absolute_recovery_P1_P7": "OPEN",
}
