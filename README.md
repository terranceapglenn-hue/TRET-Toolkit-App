# TRET Toolkit App v7.0.0

**Residual-native computational instruments** for Toroidal Residual Energy Theory (A159–A302 lineage).

## Honesty (non-negotiable)

| Flag | Status |
|------|--------|
| `free_params_primary` | **0** |
| `H_cont_open_system_closed` | **true** |
| `packing_Maxwell_under_H_cont` | recovered **C** |
| `unrestricted_open_system_closed` | **false** |
| `absolute_MeV_zero_anchor` | **IMPOSSIBLE** |
| `absolute_recovery_P1_P7` | residual parts C; absolute **OPEN** |
| Ω identification of residual scales | **X** dictionary |

## Install

```bash
pip install -r requirements.txt   # streamlit optional for UI
```

## CLI instruments

```bash
# Full battery (certificate)
PYTHONPATH=. python scripts/run_all_instruments.py

# Individual tools
PYTHONPATH=. python scripts/run_mapping_matching.py
PYTHONPATH=. python scripts/run_absolute_recovery.py
PYTHONPATH=. python scripts/run_maxwell_recovery.py
PYTHONPATH=. python scripts/run_packing_simulator.py
PYTHONPATH=. python scripts/run_dynamics.py S15_3
PYTHONPATH=. python scripts/run_gap_board.py

# Unit tests
PYTHONPATH=. python -m unittest tests/test_instruments.py -v
```

## Streamlit dashboard

```bash
streamlit run app/streamlit_app.py --server.port 8080 --server.address 0.0.0.0
```

## Instruments

| Tool | Module | Source lineage |
|------|--------|----------------|
| Mapping / matching | `tret/mapping.py` | A159–A160 |
| Maxwell recovery | `tret/recovery/maxwell.py` | A192–A194 |
| Absolute recovery | `tret/recovery/absolute.py` | P1–P7 honest ledger |
| SI-Recover | `tret/recovery/si_recover.py` | A159/A213 M-class |
| Kernel packing simulator | `tret/packing_simulator.py` | A208–A212, A291–A298 |
| Dynamics | `tret/dynamics.py` | residual spring FE |
| Γ-limit + λ_V | `tret/gamma_limit.py` | A299–A300 |
| Chiral spectral | `tret/chiral.py` | A301–A302 |
| Gap board + next programs | `tret/gaps.py` | integrated A1–A302 |

## Packing families

K7, M15, K10, K24, S15^(3), S29, S29^throat — incidence, H1, Laplacian spectrum, soft cost, stability ranking, optional dynamics.

## Key residual scales (structure C; Ω ID = X)

- λ_V = e^{-3} ≈ **4.9787%**
- λ_dark = 1−e^{-3} ≈ **95.0213%**
- R_oc = e^3−1 ≈ **19.0855**
- Soft-only n=6 packing share ≈ **52.06%**
- Three-band V/DM/DE ≈ **4.98 / 31.81 / 63.21 %**

## Remaining gaps

See [docs/REMAINING_GAPS_AND_NEXT_STEPS.md](docs/REMAINING_GAPS_AND_NEXT_STEPS.md).
