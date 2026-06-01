from __future__ import annotations
import math
from .unit import AbstractUnit

def _r(v: float) -> int:
    return int(v + 0.5)

def _tmm(mp: int, is_vtol: bool = False) -> int:
    a = 2 * mp
    base = 0 if a < 5 else 1 if a < 9 else 2 if a < 13 else 3 if a < 19 else 4 if a < 35 else 5
    return base + (1 if is_vtol else 0)


class CombatVehicle(AbstractUnit):
    TRACKED = "Tracked"
    WHEELED = "Wheeled"
    HOVER = "Hover"
    VTOL = "VTOL"

    LOCATIONS = ["FR", "LS", "RS", "RR"]
    TURRET_LOC = "TU"
    ROTOR_LOC = "RO"

    def __init__(self):
        super().__init__()
        self.motive_type: str = self.TRACKED
        self.tonnage: float = 50.0
        self.cruise_mp: int = 4
        self.has_turret: bool = False
        self.armor: dict[str, int] = {"FR": 0, "LS": 0, "RS": 0, "RR": 0, "TU": 0, "RO": 0}

    @property
    def effective_cruise_mp(self) -> int:
        w = self.cruise_mp
        has_masc = self.is_equipped_with("masc")
        has_sc   = self.is_equipped_with("supercharger")
        if has_masc and has_sc:
            w = math.ceil(w * 1.5)
        elif has_masc or has_sc:
            w = math.ceil(w * 1.25)
        return w

    @property
    def flank_mp(self) -> int:
        return math.ceil(self.effective_cruise_mp * 1.5)

    @property
    def unit_type_label(self) -> str:
        return "Combat Vehicle"

    @property
    def destiny_move(self) -> str:
        letter = self.motive_type[0].lower() if self.motive_type else ""
        result = f"{self.effective_cruise_mp} / {self.flank_mp}{letter}"
        if self.is_equipped_with("umu"):
            result += f" / {self.cruise_mp}u"
        return result.replace(" ", "") if len(result) > 11 else result

    @property
    def destiny_sinks(self) -> int:
        return 0

    @property
    def destiny_tmm(self) -> str:
        vtol = self.motive_type == self.VTOL
        parts = [str(_tmm(self.effective_cruise_mp, vtol))]
        if self.flank_mp > 0:
            parts.append(str(_tmm(self.flank_mp, vtol)))
        if self.is_equipped_with("umu"):
            parts.append(str(_tmm(self.cruise_mp)))
        return " / ".join(parts)

    def destiny_armor(self, zone: str, divisor: float = 4.0) -> int:
        raw = self.armor.get(zone, 0)
        return max(_r(raw / divisor), 1)

    def destiny_structure(self) -> int:
        return max(_r(math.ceil(self.tonnage / 10) / 3), 1)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "unit_type": "CombatVehicle",
            "motive_type": self.motive_type,
            "tonnage": self.tonnage,
            "cruise_mp": self.cruise_mp,
            "has_turret": self.has_turret,
            "armor": dict(self.armor),
        })
        return d

    @classmethod
    def from_dict(cls, data: dict) -> CombatVehicle:
        v = cls()
        v._load_common(data)
        v.motive_type = data.get("motive_type", cls.TRACKED)
        v.tonnage = float(data.get("tonnage", 50.0))
        v.cruise_mp = int(data.get("cruise_mp", 4))
        v.has_turret = bool(data.get("has_turret", False))
        v.armor = dict(data.get("armor", {}))
        return v
