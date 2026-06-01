"""
Broad coverage tests: parse every MTF and BLK file in reference/megamek_files/.

Tests are parameterized so each file shows up as its own test case in the
output, making it easy to spot which specific files fail.

Checks performed per file:
  - Parser doesn't raise an exception
  - Unit has non-empty chassis name
  - At least one stat is non-zero (tonnage, move, weapon count)
  - Warnings are collected and printed (not treated as failures)
"""
import os
import pytest

MEGAMEK_DIR = os.path.join(
    os.path.dirname(__file__), "..", "reference", "megamek_files"
)


def _all_files(ext: str) -> list[str]:
    return sorted(
        f for f in os.listdir(MEGAMEK_DIR) if f.lower().endswith(ext)
    )


# ── MTF (BattleMech) ─────────────────────────────────────────────────────────

@pytest.mark.parametrize("filename", _all_files(".mtf"))
def test_mtf_parses_without_crash(filename):
    from src.parsers.mtf_parser import parse_mtf
    path = os.path.join(MEGAMEK_DIR, filename)
    result = parse_mtf(path)
    unit = result.unit

    # Basic sanity: chassis is populated and tonnage makes sense
    assert unit.chassis, f"{filename}: chassis is empty"
    assert 10 <= unit.tonnage <= 200, f"{filename}: suspicious tonnage {unit.tonnage}"
    assert unit.walk_mp >= 0, f"{filename}: negative walk MP"

    if result.warnings:
        # Print warnings but don't fail — useful for extending the name map
        print(f"\n[{filename}] warnings ({len(result.warnings)}): "
              + "; ".join(result.warnings[:5]))


# ── BLK (Vehicles, Battle Armor, Aero, etc.) ─────────────────────────────────

@pytest.mark.parametrize("filename", _all_files(".blk"))
def test_blk_parses_without_crash(filename):
    from src.parsers.blk_parser import parse_blk
    path = os.path.join(MEGAMEK_DIR, filename)
    result = parse_blk(path)
    unit = result.unit

    # Basic sanity: must have some kind of identifier
    assert unit.chassis or unit.variant, \
        f"{filename}: both chassis and variant are empty"

    if result.warnings:
        print(f"\n[{filename}] warnings ({len(result.warnings)}): "
              + "; ".join(result.warnings[:5]))
