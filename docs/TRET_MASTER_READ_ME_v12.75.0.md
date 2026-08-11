# TRET Master Read File — Dual-Path Completion (v12.75.0)

**Date:** 11 August 2026  
**Spine:** SN-A0.1–A346  
**Certificates:** A339–A346 `all_ok`  
**Toolkit:** v7.6.0  

## Read order

1. This file  
2. **PRD Executive SN v2.4** (firewall + dual-path energy budget)  
3. **Dual-path claim board**  
4. **Unified SN PRD v2.5** (complete archive A0.1–A346)  
5. Insert A339–A346 for Word lineage  

## Dual-path rule (mandatory)

| Path | Domain | Status |
|------|--------|--------|
| **R** | Residual under \(H_{\rm cont}\) + soft geometry + multi-central | Inventoried residual C complete |
| **U** | Unrestricted / free \(\mathcal{A}_0\) without soft/\(H_{\rm cont}\) | Closed as **false** for unique packing Maxwell and absolute budget recovery |

Path R C ⇏ Path U C. Path U false ⇏ weaken Path R C.

## Locks

| Lock | Value |
|------|-------|
| free_params_primary | 0 |
| absolute_MeV | IMPOSSIBLE |
| unrestricted_open_system_closed | **false** |
| packing Maxwell under H_cont | **C (Path R)** |
| λ_V = e^{-3} | **C residual scale (Path R)** |
| Ω_b ≡ λ_V dual-route C | **certified obstruction** |
| path_R_U_separation | **mandatory** |

## A339–A346

| SN | Content | Path | Class |
|----|---------|------|-------|
| A339 | H_cont residual cohomology (H1=19/59/63; open flux) | R | C |
| A340 | S29 residual open completions (H1=59+\|A\|−1) | R | C |
| A341 | Dual-path architecture | R/U | C architecture |
| A342 | Residual energy budget + open recovery (L1–L3, three-band) | R | C multi-layer |
| A343 | Unrestricted energy-budget non-recovery | U | false/obstructed |
| A344 | Linkage dictionary | R/U | C dictionary |
| A345 | Soft-spot kill + dual-path completion | R/U | C board |
| A346 | Master dual-path claim board | R/U | C ledger |

## Path R residual energy budget (honest numbers)

| Quantity | Value | Class |
|----------|-------|-------|
| λ_V = e^{-3} | ≈4.9787% | C residual scale |
| p_6 soft-only | ≈52.06% | C ecology |
| Three-band (ρ_V, ρ_DM, ρ_DE) | ≈4.98 / 31.81 / 63.21% | C structure; Planck ID **X** |
| R_oc = e^3−1 | ≈19.086 | C residual ratio |
| Ω_b ≡ λ_V dual-route C | — | **obstruction** |

## Replace older files with

- `UNIFIED_SUPPLEMENTAL_NOTES_PRD_v2.5.tex`  
- `TRET_PRD_EXECUTIVE_SN_v2.4.tex`  
- `TRET_MASTER_READ_ME_v12.75.0.md`  
- `TRET_DUAL_PATH_CLAIM_BOARD_A346.tex`  

```bash
python3 scripts/run_A339_A346_verification.py  # all_ok
```
