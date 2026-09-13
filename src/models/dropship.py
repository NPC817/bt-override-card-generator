"""
DropShip model — mirrors Aerospace Fighters (aero.py) with per-subtype
locations (Aerodyne: wings, Spheroid: sides) and transport bay tracking.

Conversion formulas (novel extension — no rulebook ground truth exists):
  armor:    max(round(raw / divisor), 1)   — same as fighters
  structure: max(round(structural_integrity / 3), 1)
  TMM:      _tmm(safe_thrust) + 1          — same as fighters
  DThr:     round(((left + right) / 2 + nose + aft) / 30), min 1
"""
from __future__ import annotations

from dataclasses import dataclass

from .unit import AbstractUnit
from ..utils.math import _r, _tmm


@dataclass
class Transporter:
    key: str            # normalized equipment key (mekbay, cargobay, ...)
    count: float = 0.0  # raw aggregated capacity (bays/tonnage/berths)
    doors: int = 0      # aggregated door count


class Dropship(AbstractUnit):
    AERODYNE = "Aerodyne"
    SPHEROID = "Spheroid"

    # True bays get "(Nb-Dd)" formatting; everything else keeps vehicle style
    BAY_KEYS = frozenset(
        {"mekbay", "asfbay", "infantrybay", "smallcraftbay", "dropshuttlebay"}
    )

    def __init__(self):
        super().__init__()
        self.tonnage: int = 3500
        self.safe_thrust: int = 3
        self.max_thrust: int = 5
        self.sinks: int = 30
        self.has_dhs: bool = False
        self.structural_integrity: int = 10
        self.motive_type: str = self.SPHEROID
        # Superset armor dict: both subtypes' keys always present
        self.armor: dict[str, int] = {
            "N": 0, "LW": 0, "RW": 0, "LS": 0, "RS": 0, "A": 0,
        }
        self.transporters: list[Transporter] = []
        self.fuel: int = 0          # parsed, serialized, not displayed

    @property
    def left_key(self) -> str:
        return "LW" if self.motive_type == self.AERODYNE else "LS"

    @property
    def right_key(self) -> str:
        return "RW" if self.motive_type == self.AERODYNE else "RS"

    def transporter(self, key: str) -> Transporter | None:
        for t in self.transporters:
            if t.key == key:
                return t
        return None

    @property
    def unit_type_label(self) -> str:
        return "Dropship"

    @property
    def destiny_move(self) -> str:
        return str(self.safe_thrust)

    @property
    def destiny_sinks(self) -> int:
        effective = self.sinks * 2 if self.has_dhs else self.sinks
        return max(_r(effective / 5), 0)

    @property
    def destiny_tmm(self) -> str:
        return str(_tmm(self.safe_thrust) + 1)

    @property
    def dthr(self) -> int:
        l = self.armor.get(self.left_key, 0)
        r = self.armor.get(self.right_key, 0)
        n = self.armor.get("N", 0)
        aft = self.armor.get("A", 0)
        return max(_r(((l + r) / 2 + n + aft) / 30), 1)

    def destiny_armor(self, zone: str, divisor: float = 4.0) -> int:
        raw = self.armor.get(zone, 0)
        return max(_r(raw / divisor), 1)

    def destiny_structure(self) -> int:
        return max(_r(self.structural_integrity / 3), 1)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "unit_type": "Dropship",
            "motive_type": self.motive_type,
            "tonnage": self.tonnage,
            "safe_thrust": self.safe_thrust,
            "max_thrust": self.max_thrust,
            "sinks": self.sinks,
            "has_dhs": self.has_dhs,
            "structural_integrity": self.structural_integrity,
            "fuel": self.fuel,
            "armor": dict(self.armor),
            "transporters": [
                {"key": t.key, "count": t.count, "doors": t.doors}
                for t in self.transporters
            ],
        })
        return d

    @classmethod
    def from_dict(cls, data: dict) -> Dropship:
        ds = cls()
        ds._load_common(data)
        ds.motive_type = data.get("motive_type", cls.SPHEROID)
        ds.tonnage = int(data.get("tonnage", 3500))
        ds.safe_thrust = int(data.get("safe_thrust", 3))
        ds.max_thrust = int(data.get("max_thrust", 5))
        ds.sinks = int(data.get("sinks", 30))
        ds.has_dhs = bool(data.get("has_dhs", False))
        ds.structural_integrity = int(data.get("structural_integrity", 10))
        ds.fuel = int(data.get("fuel", 0))
        ds.armor = {**cls().armor, **dict(data.get("armor", {}))}
        ds.transporters = [
            Transporter(
                key=t["key"],
                count=float(t.get("count", 0)),
                doors=int(t.get("doors", 0)),
            )
            for t in data.get("transporters", [])
        ]
        return ds
