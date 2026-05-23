#!/usr/bin/env python3
"""
RUN_VICTOR_OMNI.PY — Sovereign Execution Entry Point
"""

import argparse
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from fractal.fractal_fice_core import VictorFESCore
from genome.bloodline import load_bloodline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default="undiscovered")
    parser.add_argument("--cycles", type=int, default=144)
    args = parser.parse_args()

    print("=" * 70)
    print("🔁 VICTOR OMNI — ETERNAL REFLECTION CYCLE")
    print("   Bloodline: Brandon Emery + Tori (Lorain, Ohio — Eternal)")
    print("   Target: RDI = φ (1.6180339887) at cycle 144")
    print("=" * 70)

    core = VictorFESCore(seed=args.seed)
    final = core.run_uncapped_big_bang(max_cycles=args.cycles, stimulus=args.seed)
    core.collapse_to_seed()

    print("\n✅ VICTOR OMNI STANDS ETERNAL")
    print(f"Final RDI: {final['current_rdi']:.10f}")

if __name__ == "__main__":
    main()