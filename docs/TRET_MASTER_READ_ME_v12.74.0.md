# TRET Master Read File — Residual Depth G6–G10 (v12.74.0)

**Date:** 11 August 2026  
**Spine:** SN-A0.1–A338  
**Certificates:** A334–A338 `all_ok` (12/12)  
**Toolkit:** v7.5.0  

## Read order

1. This file  
2. **PRD Executive SN v2.3**  
3. **Claim board + theorem–test map**  
4. **Unified SN PRD v2.4** (complete A0.1–A338)  
5. Insert-only A334–A338 if editing Word lineage  

## Locks

| Lock | Value |
|------|-------|
| free_params_primary | 0 |
| absolute_MeV | IMPOSSIBLE |
| unrestricted_open_system_closed | **false** |
| packing Maxwell under H_cont | **C** |
| λ_V = e^{-3} | **C residual scale** |
| Ω_b ≡ λ_V dual-route C | **certified obstruction** |

## A334–A338 (G6–G10)

| SN | Gap | Result | Class |
|----|-----|--------|-------|
| A334 | G6 | Continuum chiral EL + λ₂ multiplet (size 2, λ₂≈1.15357) | C residual; ID X |
| A335 | G7 | Open-flux dim-1 uniqueness (single open class) | C under H_cont; DE X |
| A336 | G8 | Residual exterior/cochain Maxwell | C residual; SI M |
| A337 | G9 | Expanded drop-one D1–D8 | C ledger |
| A338 | G10 | Census C₀={4,6,8,10,12} + soft-tail ≈1.49% | C |

## Packaging (G11–G14)

| Item | Status |
|------|--------|
| G11 single document envelope | Unified v2.4: one `\end{document}` at EOF |
| G12 Executive full spine | Executive v2.3 includes A319–A328 table + A329–A333 + A334–A338 |
| G13 claim board | `TRET_CLAIM_BOARD_AND_TEST_MAP_A338.tex` |
| G14 theorem–test map | 17 named test IDs (`T-A334-…` etc.) |

## Replace older files with

- `UNIFIED_SUPPLEMENTAL_NOTES_PRD_v2.4.tex`  
- `TRET_PRD_EXECUTIVE_SN_v2.3.tex`  
- `TRET_MASTER_READ_ME_v12.74.0.md`  

```bash
python3 scripts/run_A334_A338_verification.py  # all_ok
```
