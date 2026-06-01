import os
import pytest
from src.parsers.mtf_parser import parse_mtf

MTF_DIR = os.path.join(
    os.path.dirname(__file__), "..", "reference", "megamek_files"
)


def mtf_path(filename: str) -> str:
    return os.path.join(MTF_DIR, filename)


def test_hunchback_basic():
    result = parse_mtf(mtf_path("Hunchback HBK-4G.mtf"))
    mech = result.unit
    assert mech.chassis == "Hunchback"
    assert mech.variant == "HBK-4G"
    assert mech.tonnage == 50
    assert mech.walk_mp == 4
    assert mech.run_mp == 6
    assert mech.tech == "IS"


def test_hunchback_armor():
    result = parse_mtf(mtf_path("Hunchback HBK-4G.mtf"))
    mech = result.unit
    assert mech.armor["LA"] == 16
    assert mech.armor["RA"] == 16
    assert mech.armor["CT"] == 26
    assert mech.armor["HD"] == 9
    assert mech.armor["LL"] == 20
    assert mech.armor["RL"] == 20


def test_hunchback_weapons():
    result = parse_mtf(mtf_path("Hunchback HBK-4G.mtf"))
    mech = result.unit
    weapon_keys = [w.weapon_key for w in mech.weapons]
    assert "ac20" in weapon_keys
    assert "mlas" in weapon_keys   # Medium Laser
    assert "slas" in weapon_keys   # Small Laser
    assert len(mech.weapons) == 4


def test_hunchback_heat_sinks():
    result = parse_mtf(mtf_path("Hunchback HBK-4G.mtf"))
    assert result.unit.sinks == 13
    assert result.unit.has_dhs is False


def test_jenner_parses():
    result = parse_mtf(mtf_path("Jenner JR7-D.mtf"))
    assert result.unit.chassis == "Jenner"
    assert len(result.unit.weapons) > 0


def test_madcat_parses():
    result = parse_mtf(mtf_path("Mad Cat (Timber Wolf) A.mtf"))
    mech = result.unit
    assert mech.chassis != ""
    assert mech.tonnage > 0
