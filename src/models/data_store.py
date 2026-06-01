from __future__ import annotations
import os
import yaml
from .weapon import Weapon
from .equipment import Equipment
from ..utils.paths import resource_path

_BASE = str(resource_path("data"))


class DataStore:
    _weapons: dict[str, Weapon] = {}
    _equipment: dict[str, Equipment] = {}
    _loaded: bool = False
    _by_tech: dict[str, list[Weapon]] = {}

    @classmethod
    def load(cls) -> None:
        cls._weapons = cls._load_weapons()
        cls._equipment = cls._load_equipment()
        cls._by_tech = {}
        cls._loaded = True

    @classmethod
    def _load_weapons(cls) -> dict[str, Weapon]:
        path = os.path.join(_BASE, "weapons.yaml")
        with open(path, encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        weapons: dict[str, Weapon] = {}
        for key, data in raw.items():
            if not isinstance(data, dict):
                continue
            try:
                weapons[key] = Weapon.from_dict(key, data)
            except (KeyError, TypeError) as e:
                raise ValueError(f"Invalid weapon definition '{key}': {e}") from e
        return weapons

    @classmethod
    def _load_equipment(cls) -> dict[str, Equipment]:
        path = os.path.join(_BASE, "equipment.yaml")
        with open(path, encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        equipment: dict[str, Equipment] = {}
        for key, data in raw.items():
            if not isinstance(data, dict):
                continue
            try:
                equipment[key] = Equipment.from_dict(key, data)
            except (KeyError, TypeError) as e:
                raise ValueError(f"Invalid equipment definition '{key}': {e}") from e
        return equipment

    @classmethod
    def weapon(cls, key: str) -> Weapon:
        cls._ensure_loaded()
        if key not in cls._weapons:
            raise KeyError(f"Unknown weapon key: '{key}'")
        return cls._weapons[key]

    @classmethod
    def equipment(cls, key: str) -> Equipment:
        cls._ensure_loaded()
        if key not in cls._equipment:
            raise KeyError(f"Unknown equipment key: '{key}'")
        return cls._equipment[key]

    @classmethod
    def all_weapons(cls) -> dict[str, Weapon]:
        cls._ensure_loaded()
        return cls._weapons

    @classmethod
    def all_equipment(cls) -> dict[str, Equipment]:
        cls._ensure_loaded()
        return cls._equipment

    @classmethod
    def weapons_by_tech(cls, tech: str) -> list[Weapon]:
        cls._ensure_loaded()
        if tech not in cls._by_tech:
            cls._by_tech[tech] = [w for w in cls._weapons.values() if w.tech in (tech, "Mixed")]
        return cls._by_tech[tech]

    @classmethod
    def weapons_filtered(cls, ba_only: bool | None = None) -> dict[str, Weapon]:
        """Return weapons dict, optionally filtered by baOnly flag."""
        cls._ensure_loaded()
        if ba_only is None:
            return cls._weapons
        return {k: w for k, w in cls._weapons.items() if w.baOnly == ba_only}

    @classmethod
    def _ensure_loaded(cls) -> None:
        if not cls._loaded:
            cls.load()
