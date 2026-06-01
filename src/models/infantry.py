from __future__ import annotations
import math
from .unit import AbstractUnit


class Infantry(AbstractUnit):
    MOTIVE_DATA: dict[str, dict] = {
        "Foot":               {"name": "Foot Infantry",           "walk": 1, "jump": 0, "move_suffix": "", "base_weight": 0.085},
        "Motorized":          {"name": "Motorized Infantry",      "walk": 3, "jump": 0, "move_suffix": "", "base_weight": 0.195},
        "Jump":               {"name": "Jump Infantry",           "walk": 1, "jump": 3, "move_suffix": "", "base_weight": 0.165},
        "Mechanized Hover":   {"name": "Mechanized Infantry (H)", "walk": 5, "jump": 0, "move_suffix": "h","base_weight": 1.0},
        "Mechanized Tracked": {"name": "Mechanized Infantry (T)", "walk": 3, "jump": 0, "move_suffix": "t","base_weight": 1.0},
        "Mechanized Wheeled": {"name": "Mechanized Infantry (W)", "walk": 4, "jump": 0, "move_suffix": "w","base_weight": 1.0},
    }
    WEAPON_DATA: dict[str, dict] = {
        # reduce_move: -1 walk/jump (except Mechanized Tracked) per card_gen.js
        # reduce_squads: max squad count -1 per card_gen.js
        # anti_infantry: append " (AI)" to weapon name on card per card_gen.js line 9621
        "ballistic": {"name": "Ballistic Rifle", "factor": 16, "rangePB": "+0", "rangeS": "+2", "rangeM": "--", "rangeL": "--", "use_m": False, "use_h": False, "reduce_move": False, "reduce_squads": False, "anti_infantry": False},
        "laser":     {"name": "Laser Rifle",     "factor": 8,  "rangePB": "+0", "rangeS": "+2", "rangeM": "+4", "rangeL": "--", "use_m": False, "use_h": False, "reduce_move": False, "reduce_squads": False, "anti_infantry": False},
        "mg":        {"name": "Machine Gun",     "factor": 17, "rangePB": "+0", "rangeS": "+2", "rangeM": "--", "rangeL": "--", "use_m": False, "use_h": False, "reduce_move": True,  "reduce_squads": False, "anti_infantry": True},
        "flamer":    {"name": "Flamer",          "factor": 14, "rangePB": "+0", "rangeS": "+2", "rangeM": "--", "rangeL": "--", "use_m": False, "use_h": True,  "reduce_move": True,  "reduce_squads": False, "anti_infantry": True},
        "srm":       {"name": "SRM",             "factor": 15, "rangePB": "+0", "rangeS": "+2", "rangeM": "+4", "rangeL": "--", "use_m": True,  "use_h": False, "reduce_move": True,  "reduce_squads": False, "anti_infantry": False},
        "lrm":       {"name": "LRM",             "factor": 13, "rangePB": "+0", "rangeS": "+0", "rangeM": "+2", "rangeL": "--", "use_m": True,  "use_h": False, "reduce_move": True,  "reduce_squads": True,  "anti_infantry": False},
    }

    def __init__(self):
        super().__init__()
        self.squad_size: int = 7
        self.squad_count: int = 4
        self.ground_mp: int = 1          # legacy — derived from motion_type_key now
        self.armor_per_trooper: int = 1  # legacy — not used on infantry card
        self.motion_type_key: str = "Foot"
        self.weapon_type: str = "ballistic"
        self.trooper_equipment: str = ""
        self.armor_kit: str = ""
        self.field_guns: list[str] = []

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _motive(self) -> dict:
        return self.MOTIVE_DATA.get(self.motion_type_key, self.MOTIVE_DATA["Foot"])

    @staticmethod
    def _js_round(x: float) -> int:
        """Replicate JS Math.round (round-half-up, unlike Python banker's round)."""
        return int(math.floor(x + 0.5))

    @staticmethod
    def _tmm(mp: int) -> int:
        a = 2 * mp
        if a < 5:  return 0
        if a < 9:  return 1
        if a < 13: return 2
        if a < 19: return 3
        if a < 35: return 4
        return 5

    # ── Computed properties ───────────────────────────────────────────────────

    def _weapon_reduces_move(self) -> bool:
        return self.WEAPON_DATA.get(self.weapon_type, {}).get("reduce_move", False)

    @property
    def walk_mp(self) -> int:
        base = self._motive()["walk"]
        # Mechanized Tracked ignores the move penalty per card_gen.js
        if self._weapon_reduces_move() and self.motion_type_key != "Mechanized Tracked":
            return max(base - 1, 0)
        return base

    @property
    def run_mp(self) -> int:
        return self._js_round(1.5 * self.walk_mp) or 1

    @property
    def jump_mp(self) -> int:
        base = self._motive().get("jump", 0)
        if base and self._weapon_reduces_move():
            return max(base - 1, 0)
        return base

    @property
    def has_anti_mech(self) -> bool:
        return self.motion_type_key in ("Foot", "Motorized", "Jump")

    @property
    def type_name(self) -> str:
        return self._motive()["name"]

    @property
    def tonnage(self) -> int:
        bw = self._motive().get("base_weight", 0.085)
        return math.ceil(bw * self.squad_size * self.squad_count)

    @property
    def unit_type_label(self) -> str:
        return "Infantry"

    @property
    def destiny_move(self) -> str:
        suffix = self._motive().get("move_suffix", "")
        result = f"{self.walk_mp} / {self.run_mp}"
        if self.jump_mp:
            result += f" / {self.jump_mp}j"
        if suffix:
            result += suffix
        return result

    @property
    def destiny_sinks(self) -> int:
        return 0

    @property
    def destiny_tmm(self) -> str:
        result = f"{self._tmm(self.walk_mp)} / {self._tmm(self.run_mp)}"
        if self.jump_mp:
            result += f" / {self._tmm(self.jump_mp) + 1}"
        return result

    # ── Damage calculation (ported from card_gen.js weaponDamage) ─────────────

    def weapon_damage(self, squads: int) -> str:
        """Return formatted damage string for `squads` squads remaining."""
        if not self.weapon_type or squads <= 0 or squads > self.squad_count:
            return ""
        wdata = self.WEAPON_DATA.get(self.weapon_type)
        if not wdata:
            return ""
        troops = squads * self.squad_size
        r = self._js_round(troops / 30 * wdata["factor"])
        i = math.ceil(r / 3) if r > 0 else 0
        if i == 0:
            return "0"
        result = ""
        if wdata["use_m"]:
            e = math.ceil(i / 2)
            t = math.ceil((i - e) / 3)
            result = str(e)
            if t > 0:
                result += f"+M{t} ({i})"
        else:
            pairs = i // 2
            remainder = i % 2
            for k in range(pairs):
                result += "2"
                if k < pairs - 1 or remainder:
                    result += ","
            if remainder:
                result += "1"
        if wdata["use_h"]:
            result += f"+H{max(self._js_round(r / 5), 1)}"
        return result

    # ── Serialization ─────────────────────────────────────────────────────────

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "unit_type": "Infantry",
            "squad_size": self.squad_size,
            "squad_count": self.squad_count,
            "ground_mp": self.ground_mp,
            "armor_per_trooper": self.armor_per_trooper,
            "motion_type_key": self.motion_type_key,
            "weapon_type": self.weapon_type,
            "trooper_equipment": self.trooper_equipment,
            "armor_kit": self.armor_kit,
            "field_guns": self.field_guns,
        })
        return d

    @classmethod
    def from_dict(cls, data: dict) -> Infantry:
        inf = cls()
        inf._load_common(data)
        inf.squad_size = int(data.get("squad_size", 7))
        inf.squad_count = int(data.get("squad_count", 4))
        inf.ground_mp = int(data.get("ground_mp", 1))
        inf.armor_per_trooper = int(data.get("armor_per_trooper", 1))
        inf.motion_type_key = data.get("motion_type_key", "Foot")
        inf.weapon_type = data.get("weapon_type", "ballistic")
        inf.trooper_equipment = data.get("trooper_equipment", "")
        inf.armor_kit = data.get("armor_kit", "")
        inf.field_guns = list(data.get("field_guns", []))
        return inf
