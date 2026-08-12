# TRET Submission-Ready Reproducibility Package v12.77.0

**Date:** 11 August 2026  
**Spine:** Unified SN-A0.1–A351 · Expanded SN-A1–A20 · Technical Notes (TN)  
**Status:** Submission-oriented residual dual-path package  

## Contents

| Path | Description |
|------|-------------|
| `docs/UNIFIED_SUPPLEMENTAL_NOTES_PRD_v2.7.tex` | Complete unified SN-A0.1–A351 |
| `docs/SN_A1_A20_EXPANDED_PRD.tex` | Expanded residual foundations A1–A20 |
| `docs/TN_TECHNICAL_NOTES_PRD.tex` | Technical Notes (taxonomy, firewalls, reproducibility) |
| `docs/executive/TRET_PRD_EXECUTIVE_SN_v2.5.tex` | PRD executive spine |
| `docs/claim_boards/` | Machine claim boards A333/A338/A346 |
| `docs/sections/` | Word inserts A319–A351 |
| `reproducibility/scripts/` | Certificate batteries + `run_all_certificates.py` |
| `reproducibility/results/` | JSON data + certificates |
| `certificates/` | Master certificate copies |
| `MANIFEST.md` | File inventory |
| `LOCKS.json` | Dual-path locks |

## Read order (submission)

1. `README.md` (this file)  
2. `docs/TN_TECHNICAL_NOTES_PRD.tex`  
3. `docs/executive/TRET_PRD_EXECUTIVE_SN_v2.5.tex`  
4. `docs/SN_A1_A20_EXPANDED_PRD.tex`  
5. `docs/UNIFIED_SUPPLEMENTAL_NOTES_PRD_v2.7.tex`  

## Locks

```json
{
  "free_params_primary": 0,
  "absolute_MeV_zero_anchor": "IMPOSSIBLE",
  "unrestricted_open_system_closed": false,
  "Omega_b_equals_lambda_V_dual_route_C": "CERTIFIED_OBSTRUCTION",
  "path_R_U_separation": "mandatory",
  "packing_Maxwell_under_H_cont": "recovered_C"
}
```

## Reproduce

```bash
cd TRET_SUBMISSION_READY_v12.77.0
python3 reproducibility/scripts/run_all_certificates.py
# expect all_ok: true
```

Requires: Python ≥ 3.10, `numpy`.

## Dual-path rule

- **Path R:** residual under \(H_{\rm cont}\) — dual-route C where certified  
- **Path U:** unrestricted — packing Maxwell unique selection **false**  
- Path R C ⇏ Path U C  

## Not claimed

Absolute MeV · \(\Omega_b=\lambda_V\) dual-route C · unrestricted free-\(\mathcal{A}_0\) Maxwell · classical Serre SS · Tate main programme · particle species dual-route C  
