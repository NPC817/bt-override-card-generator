from __future__ import annotations
import logging
import math
from .unit import AbstractUnit

def _r(v: float) -> int:
    return int(v + 0.5)

# Standard Inner Sphere internal structure by tonnage (CT, ST, ARM, LEG, HD)
_IS_STRUCTURE = {
    20:  {"CT": 6,  "ST": 5,  "ARM": 3,  "LEG": 4,  "HD": 3},
    25:  {"CT": 8,  "ST": 6,  "ARM": 4,  "LEG": 6,  "HD": 3},
    30:  {"CT": 10, "ST": 7,  "ARM": 5,  "LEG": 7,  "HD": 3},
    35:  {"CT": 11, "ST": 8,  "ARM": 6,  "LEG": 8,  "HD": 3},
    40:  {"CT": 12, "ST": 10, "ARM": 6,  "LEG": 10, "HD": 3},
    45:  {"CT": 14, "ST": 11, "ARM": 7,  "LEG": 11, "HD": 3},
    50:  {"CT": 16, "ST": 12, "ARM": 8,  "LEG": 12, "HD": 3},
    55:  {"CT": 18, "ST": 13, "ARM": 9,  "LEG": 13, "HD": 3},
    60:  {"CT": 20, "ST": 14, "ARM": 10, "LEG": 14, "HD": 3},
    65:  {"CT": 21, "ST": 15, "ARM": 10, "LEG": 15, "HD": 3},
    70:  {"CT": 22, "ST": 15, "ARM": 11, "LEG": 15, "HD": 3},
    75:  {"CT": 23, "ST": 16, "ARM": 12, "LEG": 16, "HD": 3},
    80:  {"CT": 25, "ST": 17, "ARM": 13, "LEG": 17, "HD": 3},
    85:  {"CT": 27, "ST": 18, "ARM": 14, "LEG": 18, "HD": 3},
    90:  {"CT": 29, "ST": 19, "ARM": 15, "LEG": 19, "HD": 3},
    95:  {"CT": 30, "ST": 20, "ARM": 16, "LEG": 20, "HD": 3},
    100: {"CT": 31, "ST": 21, "ARM": 17, "LEG": 21, "HD": 3},
}

def _tmm(mp: int) -> int:
    """Override TMM formula: double the MP then threshold (per card_gen.js)."""
    a = 2 * mp
    if a < 5:  return 0
    if a < 9:  return 1
    if a < 13: return 2
    if a < 19: return 3
    if a < 35: return 4
    return 5


class BattleMech(AbstractUnit):
    BIPED = "Biped"
    QUAD = "Quad"

    # Armor location keys
    LOCATIONS_BIPED = ["LA", "RA", "LT", "RT", "CT", "HD", "LL", "RL"]
    LOCATIONS_QUAD  = ["FLL", "FRL", "LT", "RT", "CT", "HD", "RLL", "RRL"]
    REAR_LOCATIONS = ["LTR", "RTR", "CTR"]

    def __init__(self):
        super().__init__()
        self.motive_type: str = self.BIPED
        self.tonnage: int = 50
        self.walk_mp: int = 4
        self.jump_mp: int = 0
        self.sinks: int = 10
        self.has_dhs: bool = False
        # Armor by location key
        self.armor: dict[str, int] = {loc: 0 for loc in self.LOCATIONS_BIPED + self.REAR_LOCATIONS}

    @property
    def effective_walk_mp(self) -> int:
        w = self.walk_mp
        has_masc = self.is_equipped_with("masc")
        has_sc   = self.is_equipped_with("supercharger")
        if has_masc and has_sc:
            w = math.ceil(w * 1.5)
        elif has_masc or has_sc:
            w = math.ceil(w * 1.25)
        return w

    @property
    def run_mp(self) -> int:
        return math.ceil(self.effective_walk_mp * 1.5)

    @property
    def punch_damage(self) -> int:
        return max(math.ceil(self.tonnage / 30), 1)

    @property
    def kick_damage(self) -> int:
        return max(math.ceil(self.tonnage / 15), 1)

    @property
    def unit_type_label(self) -> str:
        return "OmniMech" if self.omni else "BattleMech"

    @property
    def destiny_move(self) -> str:
        parts = [str(self.effective_walk_mp), str(self.run_mp)]
        if self.jump_mp > 0:
            parts.append(f"{self.jump_mp}j")
        if self.is_equipped_with("umu"):
            parts.append(f"{self.walk_mp}u")
        result = " / ".join(parts)
        return result.replace(" ", "") if len(result) > 11 else result

    @property
    def destiny_sinks(self) -> int:
        effective = self.sinks * 2 if self.has_dhs else self.sinks
        return max(_r(effective / 5), 0)

    @property
    def destiny_tmm(self) -> str:
        parts = [str(_tmm(self.effective_walk_mp)), str(_tmm(self.run_mp))]
        if self.jump_mp > 0:
            parts.append(str(_tmm(self.jump_mp) + 1))
        if self.is_equipped_with("umu"):
            parts.append(str(_tmm(self.walk_mp)))
        return " / ".join(parts)

    def structure(self) -> dict[str, int]:
        if self.tonnage not in _IS_STRUCTURE:
            logging.warning("Unknown mech tonnage %s, defaulting to 50t structure", self.tonnage)
        base = _IS_STRUCTURE.get(self.tonnage, _IS_STRUCTURE[50])
        return {
            "LA": base["ARM"], "RA": base["ARM"],
            "LT": base["ST"],  "RT": base["ST"],
            "CT": base["CT"],
            "HD": base["HD"],
            "LL": base["LEG"], "RL": base["LEG"],
        }

    # Map card layout zone keys → model armor keys (JS uses LFL/RFL/LRL; MTF uses FLL/FRL/RLL)
    _CARD_TO_ARMOR = {"LFL": "FLL", "RFL": "FRL", "LRL": "RLL", "RRL": "RRL"}

    def destiny_armor(self, zone: str, divisor: float = 3.0) -> int:
        """Convert Classic BT armor value to Override value for the given zone."""
        if zone == "HD":
            raw = self.armor.get("HD", 0)
            return self._head_armor_stepped(raw)
        if zone == "T":
            # Combined torso zone on card
            raw = self.armor.get("CT", 0) + self.armor.get("LT", 0) + self.armor.get("RT", 0)
            return max(_r(raw / (divisor * 2)), 1)
        if zone == "TR":
            # Combined rear torso zone on card
            raw = self.armor.get("CTR", 0) + self.armor.get("LTR", 0) + self.armor.get("RTR", 0)
            return max(_r(raw / (divisor * 2)), 1)
        armor_key = self._CARD_TO_ARMOR.get(zone, zone)
        raw = self.armor.get(armor_key, 0)
        return max(_r(raw / divisor), 1)

    def destiny_structure(self, zone: str) -> int:
        struct = self.structure()
        if zone == "T":
            ct = struct.get("CT", 0)
            st = struct.get("LT", 0)
            raw = ct + 2 * st
            val = max(_r(raw / 7), 1)
        elif zone in ("LA", "RA"):
            raw = struct.get("LA", 0)
            val = max(_r(raw / 3), 1)
        elif zone in ("LL", "RL", "RLL", "RRL", "LRL", "FLL", "FRL", "LFL", "RFL"):
            raw = struct.get("LL", 0)
            val = max(_r(raw / 3), 1)
        elif zone == "HD":
            raw = struct.get("HD", 0)
            val = max(_r(raw / 3), 1)
        else:
            raw = struct.get(zone, 0)
            val = max(_r(raw / 3), 1)

        if self.is_equipped_with("composite"):
            val = max(_r(val / 2), 1)
        return val

    @staticmethod
    def _head_armor_stepped(raw: int) -> int:
        if raw <= 2:
            return 1
        if raw <= 5:
            return 2
        if raw <= 7:
            return 3
        return 4

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "unit_type": "BattleMech",
            "motive_type": self.motive_type,
            "tonnage": self.tonnage,
            "walk_mp": self.walk_mp,
            "jump_mp": self.jump_mp,
            "sinks": self.sinks,
            "has_dhs": self.has_dhs,
            "armor": dict(self.armor),
        })
        return d

    @classmethod
    def from_dict(cls, data: dict) -> BattleMech:
        m = cls()
        m._load_common(data)
        m.motive_type = data.get("motive_type", cls.BIPED)
        m.tonnage = int(data.get("tonnage", 50))
        m.walk_mp = int(data.get("walk_mp", 4))
        m.jump_mp = int(data.get("jump_mp", 0))
        m.sinks = int(data.get("sinks", 10))
        m.has_dhs = bool(data.get("has_dhs", False))
        m.armor = dict(data.get("armor", {}))
        return m
