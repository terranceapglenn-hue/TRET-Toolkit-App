# TRET Master Read File — Residual + Unrestricted Closures (v12.72.0)

**Date:** 11 August 2026  
**Spine:** SN-A0.1–A328  
**Certificates:** A319–A328 `all_ok` (16/16)  
**Toolkit:** extend v7.2.0 → v7.3.0 instruments  

## How to read (order)

1. **This file** — map and locks  
2. **PRD Executive SN v2.1** — firewall + load-bearing spine through A318  
3. **SN-A319–A328 insert** — new residual/unrestricted closures (full proofs)  
4. **Unified SN PRD v2.2** — complete archive including A319–A328  
5. **Toolkit batteries** — machine certificates  

## Locks (non-negotiable)

| Lock | Value |
|------|-------|
| free_params_primary | 0 |
| absolute_MeV_zero_anchor | IMPOSSIBLE |
| unrestricted_open_system_closed | **false** |
| packing Maxwell under H_cont | recovered **C** |
| λ_V = e^{-3} | residual scale **C** |
| Ω_b ≡ λ_V dual-route C | **certified obstruction** |

## What A319–A328 closes

| SN | Result | Class |
|----|--------|-------|
| A319 | Soft characterization s(n)=\|n/2-3\| unique in axiom class S | **C** |
| A320 | Multi-central uniqueness n_eq=12 under M1–M6; S15^(3)/S29 | **C** |
| A321 | Residual open/closed layers (soft_max unit + two-channel + soft-only) | **C**; Ω obstruction retained |
| A322 | H_cont drop-one minimality among inventoried weakenings | **C ledger** |
| A323 | Formal class X + meta-kill / structural soft-free obstruction | **false unrestricted** |
| A324 | Free A0 continuum non-uniqueness | **false** |
| A325 | Residual continuum F + equi-coercivity structure | **C under H_cont** |
| A326 | Chiral residual EL + spectral mass | **C residual**; ID **X** |
| A327 | Throat open flux dim 1 on S29^thr | **C under H_cont**; DE **X** |
| A328 | Residual Maxwell ledger + master positioning | **C/M/false split** |

## Two sectors

- **Residual under H_cont:** strengthened uniqueness + partition + continuum/dynamics  
- **Unrestricted:** not “opened”; **meta-closed as false** inside formal class X + free A0 non-uniqueness  
- **Absolute:** still blocked (MeV I, Ω obstruction, G_N false without M)

## Reproducibility

```bash
python3 reproducibility/scripts/run_A319_A328_verification.py
# all_ok: true
```

## Files

- `sections/SN_A319_A328_RESIDUAL_UNRESTRICTED_WORD_INSERT.tex`
- `UNIFIED_SUPPLEMENTAL_NOTES_PRD_v2.2.tex` (full archive)
- `MASTER_READ_ME.md` (this file)
