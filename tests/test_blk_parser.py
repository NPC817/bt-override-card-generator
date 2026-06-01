import os
import pytest
from src.parsers.blk_parser import parse_blk
from src.models.vehicle import CombatVehicle

BLK_DIR = os.path.join(
    os.path.dirname(__file__), "..", "reference", "megamek_files"
)


def blk_path(filename: str) -> str:
    return os.path.join(BLK_DIR, filename)


def test_condor_basic():
    result = parse_blk(blk_path("Condor Heavy Hover Tank (Liao).blk"))
    v = result.unit
    assert isinstance(v, CombatVehicle)
    assert "Condor" in v.chassis
    assert v.tonnage == 50.0
    assert v.motive_type == CombatVehicle.HOVER
    assert v.cruise_mp == 8


def test_condor_armor():
    result = parse_blk(blk_path("Condor Heavy Hover Tank (Liao).blk"))
    v = result.unit
    assert v.armor["FR"] == 38
    assert v.armor["LS"] == 23
    assert v.armor["RS"] == 23
    assert v.armor["RR"] == 22


def test_condor_weapons():
    result = parse_blk(blk_path("Condor Heavy Hover Tank (Liao).blk"))
    v = result.unit
    assert len(v.weapons) == 4
    assert all(w.weapon_key == "mlas" for w in v.weapons)


def test_demolisher_parses():
    result = parse_blk(blk_path("Demolisher Heavy Tank (Defensive).blk"))
    assert result.unit.chassis != ""


def test_drillson_parses():
    result = parse_blk(blk_path("Drillson Heavy Hover Tank.blk"))
    assert result.unit.tonnage > 0


def test_hetzer_parses():
    result = parse_blk(blk_path("Hetzer Wheeled Assault Gun.blk"))
    v = result.unit
    assert v.motive_type == CombatVehicle.WHEELED


def test_karnov_parses():
    result = parse_blk(blk_path("Karnov UR Transport.blk"))
    v = result.unit
    # VTOL
    assert v.motive_type == CombatVehicle.VTOL


def test_warrior_parses():
    result = parse_blk(blk_path("Warrior H-7A Attack Helicopter.blk"))
    assert result.unit.chassis != ""
