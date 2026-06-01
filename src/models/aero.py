from __future__ import annotations
import math
from .unit import AbstractUnit
from .mech import _tmm


def _r(v: float) -> int:
    return int(v + 0.5)


class AeroSpaceFighter(AbstractUnit):
    AEROSPACE    = "Aerospace"
    CONVENTIONAL = "Conventional"

    def __init__(self):
        super().__init__()
        self.tonnage: int = 50
        self.safe_thrust: int = 5
        self.max_thrust: int = 8
        self.armor: dict[str, int] = {"N": 0, "LW": 0, "RW": 0, "A": 0}
        self.sinks: int = 10
        self.has_dhs: bool = False
        self.motive_type: str = self.AEROSPACE

    @property
    def unit_type_label(self) -> str:
        if self.motive_type == self.CONVENTIONAL:
            return "Conventional Fighter"
        return "AeroSpace Fighter"

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
        lw = self.armor.get("LW", 0)
        rw = self.armor.get("RW", 0)
        n = self.armor.get("N", 0)
        aft = self.armor.get("A", 0)
        return max(_r(((lw + rw) / 2 + n + aft) / 30), 1)

    def destiny_armor(self, zone: str, divisor: float = 4.0) -> int:
        raw = self.armor.get(zone, 0)
        return max(_r(raw / divisor), 1)

    def destiny_structure(self) -> int:
        raw = max(self.safe_thrust, math.floor(0.1 * self.tonnage))
        return max(_r(raw / 3), 1)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "unit_type": "AeroSpaceFighter",
            "motive_type": self.motive_type,
            "tonnage": self.tonnage,
            "safe_thrust": self.safe_thrust,
            "max_thrust": self.max_thrust,
            "sinks": self.sinks,
            "has_dhs": self.has_dhs,
            "armor": dict(self.armor),
        })
        return d

    @classmethod
    def from_dict(cls, data: dict) -> AeroSpaceFighter:
        a = cls()
        a._load_common(data)
        a.motive_type = data.get("motive_type", cls.AEROSPACE)
        a.tonnage = int(data.get("tonnage", 50))
        a.safe_thrust = int(data.get("safe_thrust", 5))
        a.max_thrust = int(data.get("max_thrust", 8))
        a.sinks = int(data.get("sinks", 10))
        a.has_dhs = bool(data.get("has_dhs", False))
        a.armor = dict(data.get("armor", {}))
        return a
