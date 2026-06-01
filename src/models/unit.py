from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UnitWeapon:
    weapon_key: str
    tic: int = 0
    location: str = ""
    ammo_type: str = ""   # e.g. "Precision", "AP", "Flechette"
    one_shot: bool = False
    fcs: str | None = None  # "aiv", "av", or None


@dataclass
class UnitEquipment:
    equipment_key: str
    location: str = ""     # e.g. "LA", "RA" — only when equipment hasLoc
    subtype: str = ""      # e.g. "AC", "LRM" for ammo subtypes
    uses: float = 0.0          # remaining uses/capacity — only when equipment isLimited


class AbstractUnit(ABC):
    def __init__(self):
        self.chassis: str = ""
        self.variant: str = ""
        self.tech: str = "IS"    # "IS", "Clan", "Mixed"
        self.omni: bool = False
        self.gunnery: int = 4
        self.piloting: int = 5
        self.weapons: list[UnitWeapon] = []
        self.equipment: list[UnitEquipment] = []
        self._equipment_keys_cache: tuple[int, frozenset[str]] = (0, frozenset())

    @property
    def display_name(self) -> str:
        parts = [self.chassis, self.variant]
        return (" ".join(p for p in parts if p).strip() or "Unnamed Unit").upper()

    @property
    @abstractmethod
    def unit_type_label(self) -> str:
        """Human-readable unit type for card header."""

    @property
    @abstractmethod
    def destiny_move(self) -> str:
        """Movement string for card display, e.g. '4 / 6'."""

    @property
    @abstractmethod
    def destiny_sinks(self) -> int:
        """Heat sink value for card display."""

    @property
    @abstractmethod
    def destiny_tmm(self) -> str:
        """Target Movement Modifier string for card display, e.g. '1 / 2'."""

    def is_equipped_with(self, equipment_key: str) -> bool:
        list_id = id(self.equipment)
        cached_id, cached_keys = self._equipment_keys_cache
        if cached_id != list_id:
            cached_keys = frozenset(e.equipment_key for e in self.equipment)
            self._equipment_keys_cache = (list_id, cached_keys)
        return equipment_key in cached_keys

    def to_dict(self) -> dict:
        return {
            "chassis": self.chassis,
            "variant": self.variant,
            "tech": self.tech,
            "omni": self.omni,
            "gunnery": self.gunnery,
            "piloting": self.piloting,
            "weapons": [
                {
                    "weapon_key": w.weapon_key,
                    "tic": w.tic,
                    "location": w.location,
                    "ammo_type": w.ammo_type,
                    "one_shot": w.one_shot,
                    "fcs": w.fcs,
                }
                for w in self.weapons
            ],
            "equipment": [
                {
                    "equipment_key": e.equipment_key,
                    "location": e.location,
                    "subtype": e.subtype,
                    "uses": e.uses,
                }
                for e in self.equipment
            ],
        }

    def _load_common(self, data: dict) -> None:
        self.chassis = data.get("chassis", "")
        self.variant = data.get("variant", "")
        self.tech = data.get("tech", "IS")
        self.omni = data.get("omni", False)
        self.gunnery = int(data.get("gunnery", 4))
        self.piloting = int(data.get("piloting", 5))
        self.weapons = [
            UnitWeapon(
                weapon_key=w["weapon_key"],
                tic=w.get("tic", 1),
                location=w.get("location", ""),
                ammo_type=w.get("ammo_type", ""),
                one_shot=w.get("one_shot", False),
                fcs=w.get("fcs"),
            )
            for w in data.get("weapons", [])
        ]
        self.equipment = [
            UnitEquipment(
                equipment_key=e["equipment_key"],
                location=e.get("location", ""),
                subtype=e.get("subtype", ""),
                uses=e.get("uses", 0),
            )
            for e in data.get("equipment", [])
        ]
