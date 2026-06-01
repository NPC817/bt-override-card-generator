from __future__ import annotations
import math
import re
from .unit import AbstractUnit
from .mech import _tmm


def _r(v: float) -> int:
    return int(v + 0.5)


class BattleArmor(AbstractUnit):
    # Motive type
    BIPED = "Biped"
    QUAD  = "Quad"

    # Weight classes
    PAL     = "PA(L) / Exoskeleton"
    LIGHT   = "Light"
    MEDIUM  = "Medium"
    HEAVY   = "Heavy"
    ASSAULT = "Assault"

    # Other motive types
    OTHER_NONE = "--None--"
    OTHER_JUMP = "Jump Jets"
    OTHER_VTOL = "VTOL"
    OTHER_UMU  = "UMU"

    _WEIGHTS     = {PAL: 0.4, LIGHT: 0.75, MEDIUM: 1.0, HEAVY: 1.5, ASSAULT: 2.0}
    _SUFFIX      = {OTHER_JUMP: "j", OTHER_VTOL: "v", OTHER_UMU: "u"}
    _WC_ORDER    = [PAL, LIGHT, MEDIUM, HEAVY, ASSAULT]

    # maxGroundMP: {motive: {weight_class: max}}
    _MAX_GROUND_MP = {
        BIPED: {PAL: 3, LIGHT: 3, MEDIUM: 3, HEAVY: 2, ASSAULT: 2},
        QUAD:  {LIGHT: 5, MEDIUM: 5, HEAVY: 4, ASSAULT: 4},
    }
    # maxOtherMP: {weight_class: {other_motive: max}}
    _MAX_OTHER_MP = {
        PAL:     {OTHER_JUMP: 3, OTHER_VTOL: 7, OTHER_UMU: 5},
        LIGHT:   {OTHER_JUMP: 3, OTHER_VTOL: 6, OTHER_UMU: 5},
        MEDIUM:  {OTHER_JUMP: 3, OTHER_VTOL: 5, OTHER_UMU: 4},
        HEAVY:   {OTHER_JUMP: 2, OTHER_VTOL: 0, OTHER_UMU: 3},
        ASSAULT: {OTHER_JUMP: 2, OTHER_VTOL: 0, OTHER_UMU: 2},
    }
    # maxArmor by weight class
    _MAX_ARMOR = {PAL: 2, LIGHT: 6, MEDIUM: 10, HEAVY: 14, ASSAULT: 18}

    def __init__(self):
        super().__init__()
        self.squad_size: int = 4
        self.ground_mp: int = 1
        self.armor_per_trooper: int = 4
        self.weight_class: str = self.MEDIUM
        self.motive_type: str = self.BIPED
        self.other_motive_type: str = self.OTHER_NONE
        self.other_mp: int = 0

    # ── Computed MP ──────────────────────────────────────────────────────

    @property
    def walk_mp(self) -> int:
        mp = self.ground_mp
        if self.is_equipped_with("myomerboost"):
            if self.weight_class in (self.HEAVY, self.ASSAULT):
                mp += 1
            else:
                mp += 2
        return mp

    @property
    def run_mp(self) -> int:
        # 1.5 * walk_mp always ends in .0 or .5; math.ceil matches
        # JS Math.round (half-up) for those two cases.
        return max(math.ceil(1.5 * self.walk_mp), 0)

    @property
    def other_display_mp(self) -> int:
        if self.other_motive_type == self.OTHER_NONE:
            return 0
        mp = self.other_mp
        if self.other_motive_type == self.OTHER_JUMP:
            if self.is_equipped_with("partwing") or self.is_equipped_with("jumpbooster"):
                mp += 1
        return mp

    # ── MP constraints ───────────────────────────────────────────────────

    @property
    def min_ground_mp(self) -> int:
        return 1 if self.motive_type == self.BIPED else 2

    @property
    def max_ground_mp(self) -> int:
        return self._MAX_GROUND_MP.get(self.motive_type, {}).get(self.weight_class, 0)

    @property
    def max_other_mp(self) -> int:
        return self._MAX_OTHER_MP.get(self.weight_class, {}).get(self.other_motive_type, 0)

    @property
    def allowed_other_motive_types(self) -> list[str]:
        if self.motive_type == self.QUAD:
            return [self.OTHER_NONE]
        if self.tech == "IS":
            return [self.OTHER_NONE, self.OTHER_JUMP]
        # Clan
        if self.weight_class in (self.HEAVY, self.ASSAULT):
            return [self.OTHER_NONE, self.OTHER_JUMP, self.OTHER_UMU]
        return [self.OTHER_NONE, self.OTHER_JUMP, self.OTHER_VTOL, self.OTHER_UMU]

    @property
    def allowed_squad_size(self) -> list[int]:
        if self.tech == "Clan":
            return [5]
        return [4, 5, 6]

    @property
    def max_armor(self) -> int:
        return self._MAX_ARMOR.get(self.weight_class, 0)

    # ── Booleans ─────────────────────────────────────────────────────────

    @property
    def has_anti_mech(self) -> bool:
        return (self.motive_type == self.BIPED
                and self.weight_class not in (self.HEAVY, self.ASSAULT))

    @property
    def has_mechanized(self) -> bool:
        return self.motive_type == self.BIPED and self.weight_class != self.ASSAULT

    @property
    def type_name(self) -> str:
        base = "Battle Armor"
        if self.motive_type == self.QUAD:
            base += " (Quad)"
        return base

    @property
    def display_name(self) -> str:
        name = super().display_name
        return self._shorten_ba_name(name)

    @staticmethod
    def _shorten_ba_name(name: str) -> str:
        """Shorten BA name to ≤30 chars: 1) 'Battle Armor'→'BA', 2) strip (),
           3) strip '' and \"\"."""
        if len(name) <= 30:
            return name
        # Step 1: "Battle Armor" or "BattleArmor" → "BA"
        name = re.sub(r'\bBATTLE\s*ARMOR\b', 'BA', name, flags=re.IGNORECASE)
        if len(name) <= 30:
            return name
        # Step 2: Remove () and their contents
        name = re.sub(r'\([^)]*\)', '', name)
        name = re.sub(r'\s+', ' ', name).strip()
        if len(name) <= 30:
            return name
        # Step 3: Remove '' and "" and their contents
        name = re.sub(r"'[^']*'", '', name)
        name = re.sub(r'"[^"]*"', '', name)
        name = re.sub(r'\s+', ' ', name).strip()
        return name

    # ── Weight / mass ────────────────────────────────────────────────────

    @property
    def weight(self) -> float:
        return self._WEIGHTS.get(self.weight_class, 1.0)

    @property
    def tonnage(self) -> float:
        # Rounded to nearest 0.5 per JS
        return _r(self.weight * self.squad_size * 2) / 2

    @property
    def mass_str(self) -> str:
        w = _r(self.weight * 2) / 2
        t = _r(self.weight * self.squad_size * 2) / 2
        w_str = str(int(w)) if w == int(w) else str(w)
        t_str = str(int(t)) if t == int(t) else str(t)
        return f"{w_str} ea. ({t_str} total)"

    # ── Destiny overrides ────────────────────────────────────────────────

    @property
    def unit_type_label(self) -> str:
        return self.type_name

    @property
    def destiny_move(self) -> str:
        parts = []
        if self.walk_mp > 0:
            parts.append(str(self.walk_mp))
            if self.run_mp > 0:
                parts.append(str(self.run_mp))
        omp = self.other_display_mp
        if omp > 0:
            suffix = self._SUFFIX.get(self.other_motive_type, "")
            parts.append(f"{omp}{suffix}")
        if self.is_equipped_with("umu") and self.walk_mp > 0:
            parts.append(f"{self.walk_mp}u")
        result = " / ".join(parts)
        return result.replace(" ", "") if len(result) > 11 else result

    @property
    def destiny_sinks(self) -> int:
        return 0

    @property
    def destiny_tmm(self) -> str:
        parts = []
        if self.walk_mp > 0:
            parts.append(str(_tmm(self.walk_mp) + 1))
            if self.run_mp > 0:
                parts.append(str(_tmm(self.run_mp) + 1))
        omp = self.other_display_mp
        if omp > 0:
            bonus = 0 if self.other_motive_type == self.OTHER_UMU else 1
            parts.append(str(_tmm(omp) + 1 + bonus))
        if self.is_equipped_with("umu") and self.other_motive_type != self.OTHER_UMU and self.walk_mp > 0:
            parts.append(str(_tmm(self.walk_mp) + 1))
        return " / ".join(parts)

    def tmm(self, mp: int) -> int:
        return _tmm(mp) + 1

    def destiny_armor(self, divisor: float | None = None) -> int:
        return max(math.ceil(self.armor_per_trooper / 4), 1)

    def destiny_structure(self) -> int:
        return 1

    # ── Reset helpers ────────────────────────────────────────────────────

    def reset_motives(self) -> None:
        allowed_ground = list(range(self.min_ground_mp, self.max_ground_mp + 1))
        if self.ground_mp not in allowed_ground:
            self.ground_mp = allowed_ground[0]
        if self.other_motive_type not in self.allowed_other_motive_types:
            self.other_motive_type = self.OTHER_NONE
        allowed_other = list(range(0, self.max_other_mp + 1))
        if self.other_mp not in allowed_other:
            self.other_mp = allowed_other[0]

    def reset_armor(self) -> None:
        if self.armor_per_trooper > self.max_armor:
            self.armor_per_trooper = self.max_armor

    def reset_locations(self) -> None:
        locs = {"Body"}
        if self.is_equipped_with("turret"):
            locs.add("TU")
        if self.is_equipped_with("dwp"):
            locs.add("DWP")
        if self.motive_type == self.BIPED:
            locs.add("Arm")
        self._locations = list(locs)

    # ── Serialization ────────────────────────────────────────────────────

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "unit_type": "BattleArmor",
            "squad_size": self.squad_size,
            "ground_mp": self.ground_mp,
            "armor_per_trooper": self.armor_per_trooper,
            "weight_class": self.weight_class,
            "motive_type": self.motive_type,
            "other_motive_type": self.other_motive_type,
            "other_mp": self.other_mp,
        })
        return d

    @classmethod
    def from_dict(cls, data: dict) -> BattleArmor:
        ba = cls()
        ba._load_common(data)
        ba.squad_size = int(data.get("squad_size", 4))
        gmp = int(data.get("ground_mp", data.get("walk_mp", data.get("walkingMP", 1))))
        ba.ground_mp = gmp
        ba.armor_per_trooper = int(data.get("armor_per_trooper",
                                   data.get("armor", 4)))
        wc = data.get("weight_class", cls.MEDIUM)
        # Map old string formats
        if wc == "PA(L)/Exoskeleton":
            wc = cls.PAL
        ba.weight_class = wc
        mt = data.get("motive_type", cls.BIPED)
        if mt in ("Standard", "Leg"):
            mt = cls.BIPED
        elif mt == "Quad":
            mt = cls.QUAD
        ba.motive_type = mt
        omt = data.get("other_motive_type", cls.OTHER_NONE)
        if omt == "None":
            omt = cls.OTHER_NONE
        elif omt == "Jump Jet":
            omt = cls.OTHER_JUMP
        ba.other_motive_type = omt
        ba.other_mp = int(data.get("other_mp", 0))
        return ba
