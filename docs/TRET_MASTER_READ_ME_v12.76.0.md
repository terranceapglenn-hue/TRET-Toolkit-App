# TRET Master Read File — Early-Spine Fortification (v12.76.0)

**Date:** 11 August 2026  
**Spine:** SN-A0.1–A351  
**Certificates:** A347–A351 `all_ok`  
**Toolkit:** v7.7.0  

## Read order

1. This file  
2. **PRD Executive SN v2.5**  
3. **Unified SN PRD v2.6** (complete A0.1–A351)  
4. SN-A347–A351 insert for Word lineage  
5. Dual-path board A346 still authoritative for energy budget  

## What this package closes

| SN | Closure |
|----|---------|
| A347 | Thin residual filtration SS: gr H1 = (19,40,4) → 63; not Serre |
| A348 | A0–A100 Path R/U/M/X/I claim register (40 entries) |
| A349 | Nomenclature: S15 / S15^(3) / S29 / MKG / H_cont |
| A350 | Dedup A5.3→A16.4; A29–A84 mapped reserved; index map |
| A351 | A98–A99 refresh; AF C6 unique up to sign; **no Tate programme** |

## Locks (unchanged)

free_params=0 · MeV IMPOSSIBLE · unrestricted false · Ω dual-route C obstruction · Path R/U separation mandatory · Tate not main track  

## Replace older files with

- `UNIFIED_SUPPLEMENTAL_NOTES_PRD_v2.6.tex`  
- `TRET_PRD_EXECUTIVE_SN_v2.5.tex`  
- `TRET_MASTER_READ_ME_v12.76.0.md`  

```bash
python3 scripts/run_A347_A351_verification.py  # all_ok
```
