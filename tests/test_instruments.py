#!/usr/bin/env python3
import sys, math, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tret import (
    soft, soft_only_abundance, soft_diameter, three_band,
    run_mapping_matching, run_maxwell_recovery, run_absolute_recovery,
    simulate_all_families, run_gamma_limit, run_chiral_spectral, gap_board,
    run_dynamics,
)

class TestToolkit(unittest.TestCase):
    def test_soft(self):
        self.assertEqual(soft(6), 0)
        self.assertEqual(soft(12), 3)
    def test_soft_only(self):
        s = soft_only_abundance()
        self.assertEqual(s["packing_max_n"], 6)
        self.assertGreater(s["p_soft0"], 0.5)
    def test_lambda_V(self):
        d = soft_diameter()
        self.assertAlmostEqual(d["lambda_V"], math.exp(-3))
    def test_mapping(self):
        self.assertTrue(run_mapping_matching()["all_ok"])
    def test_maxwell(self):
        self.assertTrue(run_maxwell_recovery()["all_ok"])
    def test_absolute(self):
        self.assertTrue(run_absolute_recovery()["all_ok"])
    def test_packing(self):
        sim = simulate_all_families()
        self.assertEqual(sim["families"]["S15_3"]["nE"], 33)
        self.assertEqual(sim["families"]["S29"]["nV"], 29)
        self.assertEqual(sim["families"]["S15_3"]["H1"], 19)
    def test_gamma(self):
        g = run_gamma_limit()
        self.assertTrue(g["selects_n_star_small_eps"])
        self.assertEqual(g["unique_minimizer"], [6])
    def test_chiral(self):
        c = run_chiral_spectral()
        self.assertEqual(c["graphs"]["S15_3"]["degen_multiplet_size"], 2)
    def test_dynamics(self):
        d = run_dynamics("K7", steps=40)
        self.assertTrue(d["energy_decreased"])
    def test_gaps(self):
        g = gap_board()
        self.assertTrue(len(g["next_programs"]) >= 5)
        self.assertIn("absolute_MeV_zero_anchor", g["impossible"])

if __name__ == "__main__":
    unittest.main()
