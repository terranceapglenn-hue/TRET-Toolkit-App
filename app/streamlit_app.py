#!/usr/bin/env python3
"""TRET Toolkit App v7 — Streamlit dashboard for residual instruments."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import streamlit as st
from tret import (
    VERSION, LOCKS,
    run_mapping_matching, run_maxwell_recovery, run_absolute_recovery, run_si_recover,
    simulate_all_families, simulate_family, run_dynamics,
    run_gamma_limit, run_chiral_spectral, gap_board,
    soft_only_abundance, soft_diameter, three_band,
)

st.set_page_config(page_title="TRET Toolkit v7", layout="wide", page_icon="◈")
st.title(f"TRET Toolkit App {VERSION}")
st.caption("Residual-native computational instruments · free_params_primary=0")

with st.sidebar:
    st.header("Honesty locks")
    st.json(LOCKS)
    tool = st.radio(
        "Instrument",
        [
            "Gap board",
            "Mapping / matching",
            "Maxwell recovery",
            "Absolute recovery",
            "SI-Recover",
            "Packing simulator",
            "Γ-limit + λ_V",
            "Chiral spectral",
            "Dynamics",
            "Soft abundance",
        ],
    )

if tool == "Gap board":
    g = gap_board()
    st.subheader("Open gaps")
    st.write(g["open_gaps"])
    st.subheader("Impossible")
    st.write(g["impossible"])
    st.subheader("Next solid programs")
    for p in g["next_programs"]:
        with st.expander(f"{p['id']}: {p['title']} [{p['status']}]"):
            st.write("Closes:", p["closes"])
            st.write("Steps:")
            for s in p["concrete_steps"]:
                st.markdown(f"- {s}")
    st.subheader("Soft spots")
    st.json(g["soft_spots"])

elif tool == "Mapping / matching":
    r = run_mapping_matching()
    st.success(f"all_ok={r['all_ok']}")
    st.json(r)

elif tool == "Maxwell recovery":
    r = run_maxwell_recovery()
    st.success(f"all_ok={r['all_ok']}")
    st.info(r["verdict"])
    st.json(r)

elif tool == "Absolute recovery":
    r = run_absolute_recovery()
    st.success(f"all_ok={r['all_ok']}")
    st.warning(r["honest_verdict"])
    st.subheader("P1–P7")
    st.json(r["P1_P7"])
    st.subheader("Residual recoverable ledger")
    st.json(r["residual_recoverable_ledger"])

elif tool == "SI-Recover":
    r = run_si_recover()
    st.success(f"all_ok={r['all_ok']}")
    st.json(r)

elif tool == "Packing simulator":
    with st.spinner("Simulating families…"):
        r = simulate_all_families()
    st.subheader("Stability ranking")
    st.table([{"family": n, "score": s} for n, s in r["ranking"]])
    fam = st.selectbox("Family detail", list(r["families"].keys()))
    st.json(r["families"][fam])
    st.subheader("Soft-only abundance %")
    st.json(r["soft_only"]["pct"])

elif tool == "Γ-limit + λ_V":
    g = run_gamma_limit()
    d = soft_diameter()
    b = three_band()
    st.metric("λ_V", f"{100*d['lambda_V']:.4f}%")
    st.metric("R_oc", f"{d['R_oc']:.4f}")
    st.json({"gamma": g, "diameter": d, "three_band": b})

elif tool == "Chiral spectral":
    c = run_chiral_spectral()
    st.json(c)

elif tool == "Dynamics":
    fam = st.selectbox("Family", ["K7", "M15", "K10", "S15_3", "S29", "K24"])
    steps = st.slider("Steps", 20, 400, 120)
    if st.button("Run dynamics"):
        d = run_dynamics(fam, steps=steps)
        st.write(f"Energy: {d['initial_energy']:.4f} → {d['final_energy']:.4f} (decreased={d['energy_decreased']})")
        st.line_chart({h["t"]: h["E"] for h in d["history"]})
        st.json({k: d[k] for k in d if k not in ("history", "final_positions_sample")})

elif tool == "Soft abundance":
    st.json(soft_only_abundance())
    st.json(three_band())
