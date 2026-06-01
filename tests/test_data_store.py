import pytest
from src.models.data_store import DataStore


@pytest.fixture(autouse=True)
def load_data():
    DataStore.load()


def test_weapons_load():
    weapons = DataStore.all_weapons()
    assert len(weapons) > 50


def test_equipment_loads():
    equipment = DataStore.all_equipment()
    assert len(equipment) > 10


def test_weapon_lookup():
    w = DataStore.weapon("ac20")
    assert w.name == "AC/20"
    assert w.damage_value() == 20
    assert w.heat_value() == 7


def test_weapon_lookup_unknown():
    with pytest.raises(KeyError):
        DataStore.weapon("not_a_real_weapon")


def test_equipment_lookup():
    e = DataStore.equipment("ams")
    assert e.name == "AMS"
    assert e.hasLoc is False


def test_equipment_lookup_unknown():
    with pytest.raises(KeyError):
        DataStore.equipment("not_real_equipment")
