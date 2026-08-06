# TRET Engineering Design & Simulation Suite v6.0.0

**Residual-native physics (S145–S155) + multiphysics engineering design engine**

## Honesty (non-negotiable)

| Flag | Status |
|------|--------|
| `free_params_primary` | **0** |
| `absolute_recovery_P1_P7` | **OPEN** |
| `absolute_MeV_zero_anchor` | **IMPOSSIBLE** |
| Engineering modules | **class-E design proxies** |

## Quick start

```bash
unzip TRET_Engineering_Suite_v6.0.0_install.zip
cd TRET_Engineering_Suite_v6.0.0
chmod +x install.sh && ./install.sh
source .venv/bin/activate
streamlit run app/streamlit_app.py --server.port 8080 --server.address 0.0.0.0
```

CLI batteries (expected: residual 10/10 + engineering 6/6):
```bash
PYTHONPATH=. python scripts/run_all_batteries.py
```

## Modules

- Residual free-energy, multipole, cascade, Path-B (S145–S152)
- Spectral gap (S154), unification map (S151), matroid (S153)
- Design engine: materials, aerodynamics, energy, engines, structures
- Skills tree (geometric, cluster, stability, matroid kernels)
- AI protocols v4.x (claim stratification, adaptive, proofreader)

Full source is in the v6.0.0 install package (101 files).
