import pytest
from src.engine.conversion import ConversionEngine
from src.settings.profile import ConversionProfile


@pytest.fixture
def engine():
    return ConversionEngine(ConversionProfile.default())


# ── Mech armor ────────────────────────────────────────────────────────────────

def test_mech_arm_armor(engine):
    # Hunchback LA armor = 16 → round(16/3) = 5
    assert engine.convert_armor(16) == 5


def test_mech_torso_combined(engine):
    # Hunchback CT=26, LT=20, RT=20 → round((26+20+20)/6) = round(66/6) = round(11) = 11
    assert engine.convert_mech_torso_armor(26, 20, 20) == 11


def test_mech_head_armor_stepped(engine):
    # Hunchback HD = 9 → >7 → 4
    assert engine.convert_head_armor(9) == 4
    assert engine.convert_head_armor(2) == 1
    assert engine.convert_head_armor(3) == 2
    assert engine.convert_head_armor(6) == 3   # ≤7 → 3
    assert engine.convert_head_armor(7) == 3


def test_mech_leg_armor(engine):
    # Hunchback LL = 20 → round(20/3) = 7
    assert engine.convert_armor(20) == 7


# ── Vehicle armor ─────────────────────────────────────────────────────────────

def test_vehicle_armor_front(engine):
    # Condor FR = 38 → round(38/4) = 10 (round 9.5 = 10 in Python)
    result = engine.convert_vehicle_armor(38)
    assert result == 10


def test_vehicle_armor_side(engine):
    # Condor LS = 23 → round(23/4) = round(5.75) = 6
    assert engine.convert_vehicle_armor(23) == 6


# ── Structure ─────────────────────────────────────────────────────────────────

def test_vehicle_structure(engine):
    # 50t vehicle → round(ceil(50/10)/3) = round(5/3) = round(1.67) = 2
    assert engine.convert_vehicle_structure(50.0) == 2


# ── Heat sinks ────────────────────────────────────────────────────────────────

def test_heat_sinks_standard(engine):
    # Hunchback 13 single → round(13/5) = round(2.6) = 3
    assert engine.convert_heat_sinks(13, is_dhs=False) == 3


def test_heat_sinks_double(engine):
    # 10 DHS → round(20/5) = 4
    assert engine.convert_heat_sinks(10, is_dhs=True) == 4


# ── House rules ───────────────────────────────────────────────────────────────

def test_custom_armor_divisor():
    profile = ConversionProfile(name="Test", mech_armor_divisor=4.0)
    eng = ConversionEngine(profile)
    # Same raw 16 → round(16/4) = 4
    assert eng.convert_armor(16) == 4


def test_custom_vehicle_armor_divisor():
    profile = ConversionProfile(name="Test", vehicle_armor_divisor=3.0)
    eng = ConversionEngine(profile)
    # Condor FR 38 → round(38/3) = round(12.67) = 13
    assert eng.convert_vehicle_armor(38) == 13


def test_heat_scale_pips_default(engine):
    # Default heat_scale_max=5; heat 5 → pips = round(5*5/5) = 5
    assert engine.heat_scale_pips(5) == 5
    # heat 0 → pips = 0
    assert engine.heat_scale_pips(0) == 0


def test_heat_scale_pips_extended():
    profile = ConversionProfile(name="Test", heat_scale_max=10)
    eng = ConversionEngine(profile)
    # heat 5 on 0-10 scale → round_half_up(5*5/10) = round_half_up(2.5) = 3
    assert eng.heat_scale_pips(5) == 3


def test_move_scale_multiplier():
    profile = ConversionProfile(name="Test", move_scale_multiplier=2.0)
    eng = ConversionEngine(profile)
    assert eng.convert_move(4) == 8
