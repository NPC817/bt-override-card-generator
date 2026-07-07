"""
BattleMech card renderer (biped and quad).

Coordinates and pip layouts mirrored from card_gen.js:
  - `va` (biped layout) at line 11828
  - `Aa` (quad layout) at line 12044
"""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap

from .card_renderer import (
    BaseCardRenderer, draw_pips, draw_text, pip_colors,
    FS_LARGE, FS_MEDIUM,
)
from ..engine.conversion import ConversionEngine
from ..models.mech import BattleMech
from ..utils.math import _tmm
from ..settings.profile import ConversionProfile

# ── Biped layout constants (va in card_gen.js) ────────────────────────────────

_BIPED_LABELS = {
    "HD": {"x": 1610, "y": 215,  "text": "Head (12)"},
    "LA": {"x": 1350, "y": 270,  "text": "Left Arm\n(10,11)"},
    "RA": {"x": 1870, "y": 270,  "text": "Right Arm\n(3,4)"},
    "T":  {"x": 1610, "y": 800,  "text": "Torso\n(6,7,8)"},
    "LL": {"x": 1280, "y": 1050, "text": "Left Leg\n(9)"},
    "RL": {"x": 1945, "y": 1050, "text": "Right Leg\n(5)"},
    "TR": {"x": 1610, "y": 1375, "text": "Torso Rear"},
}

_BIPED_PIPS = {
    "HD": {
        "armor": {
            "start": {"x": 1610, "y": 330},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": 1},
                {"x": -2, "y": 0}, {"x": 4, "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
        "structure": {
            "start": {"x": 1610, "y": 415},
            "steps": [{"x": 0, "y": 0}],
        },
    },
    "LA": {
        "armor": {
            "start": {"x": 1320, "y": 530},
            "steps": [
                {"x": 0,      "y": 0},  {"x": -2,    "y": 0},
                {"x": 0.175,  "y": -1}, {"x": 2,     "y": 0},
                {"x": -0.35,  "y": 2},  {"x": -2,    "y": 0},
                {"x": 0.525,  "y": -3}, {"x": 2,     "y": 0},
                {"x": -0.7,   "y": 4},  {"x": -2,    "y": 0},
                {"x": 1.875,  "y": -5},
            ],
        },
        "structure": {
            "start": {"x": 1287, "y": 698},
            "steps": [
                {"x": 0,      "y": 0},  {"x": -0.175, "y": 1},
                {"x": 0.35,   "y": -2}, {"x": -0.525, "y": 3},
                {"x": 0.7,    "y": -4}, {"x": -0.875, "y": 5},
            ],
        },
    },
    "RA": {
        "armor": {
            "start": {"x": 1900, "y": 530},
            "steps": [
                {"x": 0,      "y": 0},  {"x": 2,     "y": 0},
                {"x": -0.175, "y": -1}, {"x": -2,    "y": 0},
                {"x": 0.35,   "y": 2},  {"x": 2,     "y": 0},
                {"x": -0.525, "y": -3}, {"x": -2,    "y": 0},
                {"x": 0.7,    "y": 4},  {"x": 2,     "y": 0},
                {"x": -1.875, "y": -5},
            ],
        },
        "structure": {
            "start": {"x": 1933, "y": 698},
            "steps": [
                {"x": 0,      "y": 0},  {"x": 0.175,  "y": 1},
                {"x": -0.35,  "y": -2}, {"x": 0.525,  "y": 3},
                {"x": -0.7,   "y": -4}, {"x": 0.875,  "y": 5},
            ],
        },
    },
    "T": {
        "armor": {
            "start": {"x": 1610, "y": 540},
            "steps": [
                {"x": 0,   "y": 0},  {"x": -1,  "y": 1},
                {"x": 2,   "y": 0},  {"x": -3,  "y": -1},
                {"x": 4,   "y": 0},  {"x": -5,  "y": 1},
                {"x": 6,   "y": 0},  {"x": -7,  "y": -1},
                {"x": 8,   "y": 0},  {"x": -9,  "y": 1},
                {"x": 10,  "y": 0},  {"x": -11, "y": -1},
                {"x": 12,  "y": 0},  {"x": -13, "y": 1},
                {"x": 14,  "y": 0},  {"x": -15, "y": -1},
                {"x": 16,  "y": 0},  {"x": -14, "y": -1},
                {"x": 12,  "y": 0},  {"x": -14, "y": 0},
                {"x": 16,  "y": 0},
            ],
            "mask": lambda e: e % 2 == 0,
        },
        "structure": {
            "start": {"x": 1610, "y": 640},
            "steps": [
                {"x": 0,  "y": 0},  {"x": 0,  "y": 1},
                {"x": -2, "y": 0},  {"x": 4,  "y": 0},
                {"x": -4, "y": -1}, {"x": 4,  "y": 0},
                {"x": -3, "y": 2},  {"x": 2,  "y": 0},
                {"x": -2, "y": 1},  {"x": 2,  "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
    },
    "LL": {
        "armor": {
            "start": {"x": 1470, "y": 1020},
            "steps": [
                {"x": 0,      "y": 0},  {"x": -2,     "y": 0},
                {"x": 0.407,  "y": -1}, {"x": 2,      "y": 0},
                {"x": -0.814, "y": 2},  {"x": -2,     "y": 0},
                {"x": 1.221,  "y": -3}, {"x": 2,      "y": 0},
                {"x": -1.628, "y": 4},  {"x": -2,     "y": 0},
                {"x": 2.035,  "y": -5}, {"x": 2,      "y": 0},
                {"x": -2.442, "y": 6},  {"x": -2,     "y": 0},
            ],
        },
        "structure": {
            "start": {"x": 1396, "y": 1246},
            "steps": [
                {"x": 0,      "y": 0},  {"x": 0.407,  "y": -1},
                {"x": -0.814, "y": 2},  {"x": 1.221,  "y": -3},
                {"x": -1.628, "y": 4},  {"x": 2.035,  "y": -5},
                {"x": -2.442, "y": 6},
            ],
        },
    },
    "RL": {
        "armor": {
            "start": {"x": 1750, "y": 1020},
            "steps": [
                {"x": 0,      "y": 0},  {"x": 2,      "y": 0},
                {"x": -0.407, "y": -1}, {"x": -2,     "y": 0},
                {"x": 0.814,  "y": 2},  {"x": 2,      "y": 0},
                {"x": -1.221, "y": -3}, {"x": -2,     "y": 0},
                {"x": 1.628,  "y": 4},  {"x": 2,      "y": 0},
                {"x": -2.035, "y": -5}, {"x": -2,     "y": 0},
                {"x": 2.442,  "y": 6},  {"x": 2,      "y": 0},
            ],
        },
        "structure": {
            "start": {"x": 1824, "y": 1246},
            "steps": [
                {"x": 0,      "y": 0},  {"x": -0.407, "y": -1},
                {"x": 0.814,  "y": 2},  {"x": -1.221, "y": -3},
                {"x": 1.628,  "y": 4},  {"x": -2.035, "y": -5},
                {"x": 2.442,  "y": 6},
            ],
        },
    },
    "TR": {
        "armor": {
            "start": {"x": 1610, "y": 1215},
            "steps": [
                {"x": 0,  "y": 0},  {"x": 0,  "y": 1},
                {"x": -2, "y": 0},  {"x": 4,  "y": 0},
                {"x": -4, "y": -1}, {"x": 4,  "y": 0},
                {"x": -3, "y": 2},  {"x": 2,  "y": 0},
                {"x": -2, "y": 1},  {"x": 2,  "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
    },
}

# ── Quad layout constants (Aa in card_gen.js) ──────────────────────────────────

_QUAD_LABELS = {
    "HD":  {"x": 1650, "y": 235,  "text": "Head (12)"},
    "LFL": {"x": 1350, "y": 1355, "text": "Left\nFront Leg\n(10,11)"},
    "RFL": {"x": 1950, "y": 1355, "text": "Right\nFront Leg\n(3,4)"},
    "T":   {"x": 1445, "y": 415,  "text": "Torso\n(6,7,8)"},
    "LRL": {"x": 1550, "y": 1303, "text": "Left\nRear Leg\n(9)"},
    "RRL": {"x": 1750, "y": 1303, "text": "Right\nRear Leg\n(5)"},
    "TR":  {"x": 1243, "y": 775,  "text": "Torso Rear"},
}

_QUAD_PIPS = {
    "HD": {
        "armor": {
            "start": {"x": 1648, "y": 344},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": 1},
                {"x": -2, "y": 0}, {"x": 4, "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
        "structure": {
            "start": {"x": 1648, "y": 433},
            "steps": [{"x": 0, "y": 0}],
        },
    },
    "T": {
        "armor": {
            "start": {"x": 1647, "y": 555},
            "steps": [
                {"x": 0, "y": 0}, {"x": -1, "y": 1},
                {"x": 2, "y": 0}, {"x": -3, "y": -1},
                {"x": 4, "y": 0}, {"x": -5, "y": 1},
                {"x": 6, "y": 0}, {"x": -7, "y": -1},
                {"x": 8, "y": 0}, {"x": -9, "y": 1},
                {"x": 10, "y": 0}, {"x": -11, "y": -1},
                {"x": 12, "y": 0}, {"x": -13, "y": 1},
                {"x": 14, "y": 0}, {"x": -15, "y": -1},
                {"x": 16, "y": 0}, {"x": -17, "y": -1},
                {"x": 18, "y": 0}, {"x": -19, "y": 1},
            ],
            "mask": lambda e: e % 2 == 0,
        },
        "structure": {
            "start": {"x": 1647, "y": 648},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": 1},
                {"x": -2, "y": 0}, {"x": 4, "y": 0},
                {"x": -4, "y": -1}, {"x": 4, "y": 0},
                {"x": -3, "y": 2}, {"x": 2, "y": 0},
                {"x": -2, "y": 1}, {"x": 2, "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
    },
    "LFL": {
        "armor": {
            "start": {"x": 1417, "y": 905},
            "steps": [
                {"x": 0, "y": 0}, {"x": -2, "y": 0},
                {"x": 0.05, "y": -1}, {"x": 2, "y": 0},
                {"x": -0.1, "y": 2}, {"x": -2, "y": 0},
                {"x": 0.15, "y": -3}, {"x": 2, "y": 0},
                {"x": -0.2, "y": 4}, {"x": -2, "y": 0},
                {"x": 0.25, "y": -5}, {"x": 2, "y": 0},
                {"x": -0.3, "y": 6},
            ],
        },
        "structure": {
            "start": {"x": 1382, "y": 1130},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0.05, "y": -1},
                {"x": -0.1, "y": 2}, {"x": 0.15, "y": -3},
                {"x": -0.2, "y": 4}, {"x": 0.25, "y": -5},
                {"x": -0.3, "y": 6},
            ],
        },
    },
    "LRL": {
        "armor": {
            "start": {"x": 1560, "y": 910},
            "steps": [
                {"x": 0, "y": 0}, {"x": -2, "y": 0},
                {"x": 0.05, "y": -1}, {"x": 2, "y": 0},
                {"x": -0.1, "y": 2}, {"x": -2, "y": 0},
                {"x": 0.15, "y": -3}, {"x": 2, "y": 0},
                {"x": -0.2, "y": 4}, {"x": -2, "y": 0},
                {"x": 0.25, "y": -5}, {"x": 2, "y": 0},
                {"x": -0.3, "y": 6},
            ],
        },
        "structure": {
            "start": {"x": 1535, "y": 1130},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0.05, "y": -1},
                {"x": -0.1, "y": 2}, {"x": 0.15, "y": -3},
                {"x": -0.2, "y": 4}, {"x": 0.25, "y": -5},
                {"x": -0.3, "y": 6},
            ],
        },
    },
    "RRL": {
        "armor": {
            "start": {"x": 1738, "y": 910},
            "steps": [
                {"x": 0, "y": 0}, {"x": 2, "y": 0},
                {"x": -0.05, "y": -1}, {"x": -2, "y": 0},
                {"x": 0.1, "y": 2}, {"x": 2, "y": 0},
                {"x": -0.15, "y": -3}, {"x": -2, "y": 0},
                {"x": 0.2, "y": 4}, {"x": 2, "y": 0},
                {"x": -0.25, "y": -5}, {"x": -2, "y": 0},
                {"x": 0.3, "y": 6},
            ],
        },
        "structure": {
            "start": {"x": 1761, "y": 1130},
            "steps": [
                {"x": 0, "y": 0}, {"x": -0.05, "y": -1},
                {"x": 0.1, "y": 2}, {"x": -0.15, "y": -3},
                {"x": 0.2, "y": 4}, {"x": -0.25, "y": -5},
                {"x": 0.3, "y": 6},
            ],
        },
    },
    "RFL": {
        "armor": {
            "start": {"x": 1879, "y": 905},
            "steps": [
                {"x": 0, "y": 0}, {"x": 2, "y": 0},
                {"x": -0.05, "y": -1}, {"x": -2, "y": 0},
                {"x": 0.1, "y": 2}, {"x": 2, "y": 0},
                {"x": -0.15, "y": -3}, {"x": -2, "y": 0},
                {"x": 0.2, "y": 4}, {"x": 2, "y": 0},
                {"x": -0.25, "y": -5}, {"x": -2, "y": 0},
                {"x": 0.3, "y": 6},
            ],
        },
        "structure": {
            "start": {"x": 1919, "y": 1130},
            "steps": [
                {"x": 0, "y": 0}, {"x": -0.05, "y": -1},
                {"x": 0.1, "y": 2}, {"x": -0.15, "y": -3},
                {"x": 0.2, "y": 4}, {"x": -0.25, "y": -5},
                {"x": 0.3, "y": 6},
            ],
        },
    },
    "TR": {
        "armor": {
            "start": {"x": 1245, "y": 615},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": 1},
                {"x": -2, "y": 0}, {"x": 4, "y": 0},
                {"x": -4, "y": -1}, {"x": 4, "y": 0},
                {"x": -3, "y": 2}, {"x": 2, "y": 0},
                {"x": -2, "y": 1}, {"x": 2, "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
    },
}


class MechCardRenderer(BaseCardRenderer):
    """Renders a BattleMech card to a 2100×1500 QPixmap."""

    BASE_IMAGE       = "card-base.png"
    SILHOUETTE_IMAGE = "mech-bp.png"

    def render(
        self,
        unit: BattleMech,
        profile: ConversionProfile,
        weapons_rows: list[dict] | None = None,
        equipment_items: list[dict] | None = None,
    ) -> QPixmap:
        """
        Render the full card.

        weapons_rows: list of dicts per weapon row:
          { name, damage, heat, location, rangePB, rangeS, rangeM, rangeL, rangeX }
        equipment_items: list of {"label", "is_ammo", "shots", ...} dicts
        """
        self.SILHOUETTE_IMAGE = "mech-qd.png" if unit.motive_type == BattleMech.QUAD else "mech-bp.png"

        canvas, painter = self._build_canvas()

        # Compute profile-scaled move / TMM / sinks for header
        engine = ConversionEngine(profile)
        _sw = engine.convert_move(unit.effective_walk_mp)
        _sr = engine.convert_move(unit.run_mp)
        _move_parts = [str(_sw), str(_sr)]
        if unit.jump_mp > 0:
            _sj = engine.convert_move(unit.jump_mp)
            _move_parts.append(f"{_sj}j")
        if unit.is_equipped_with("umu"):
            _su = engine.convert_move(unit.walk_mp)
            _move_parts.append(f"{_su}u")
        _move_str = " / ".join(_move_parts)
        if len(_move_str) > 11:
            _move_str = _move_str.replace(" ", "")
        _tmm_parts = [str(_tmm(_sw)), str(_tmm(_sr))]
        if unit.jump_mp > 0:
            _tmm_parts.append(str(_tmm(_sj) + 1))
        if unit.is_equipped_with("umu"):
            _tmm_parts.append(str(_tmm(_su)))
        _tmm_str = " / ".join(_tmm_parts)
        _sinks_val = engine.convert_heat_sinks(unit.sinks, unit.has_dhs)
        _jump_heat_val = engine.convert_jump_heat() if unit.jump_mp > 0 else None

        # Header
        self._draw_unit_header(
            painter, unit,
            move_str=_move_str, tmm_str=_tmm_str, sinks_val=_sinks_val,
            heat_scale_max=profile.heat_scale_max,
            jump_heat_val=_jump_heat_val,
        )

        # Gunnery / Piloting header labels
        self._draw_gunpil_labels(painter, unit)

        # Weapons table: 9 regular slots + melee at index 9 (10th row)
        rows = list(weapons_rows or [])[:9]
        while len(rows) < 9:
            rows.append(None)
        if unit.tonnage > 0:
            melee_row = {
                "name": "Punch / Kick",
                "damage": f"{unit.punch_damage} / {unit.kick_damage}",
                "heat": "--",
                "location": "--",
                "rangePB": "+0", "rangeS": "--", "rangeM": "--",
                "rangeL": "--", "rangeX": "--",
            }
            rows.append(melee_row)
        self._draw_weapons_table(painter, rows, has_heat=True)

        # Equipment
        self._draw_equipment_items(painter, equipment_items,
                                   show_pips=profile.show_tracking_pips)

        # Right panel: zone labels + values + pips
        self._draw_mech_zones(painter, unit, profile)

        # Bottom section: condition monitor + Engine/Gyro labels
        self._draw_condition_monitor(painter)
        self._draw_engine_gyro_labels(painter)

        painter.end()
        return canvas

    def _draw_gunpil_labels(self, painter: QPainter, unit: BattleMech) -> None:
        """Draw Gunnery / Piloting header labels (top right). Match BA label positions."""
        draw_text(painter, 1155, 45, "Gunnery", size=FS_LARGE-6, bold=True, width=180, align=Qt.AlignmentFlag.AlignCenter)
        draw_text(painter, 1300, 45, "Piloting", size=FS_LARGE-6, bold=True, width=180, align=Qt.AlignmentFlag.AlignCenter)

    def _draw_mech_zones(
        self, painter: QPainter, unit: BattleMech, profile: ConversionProfile
    ) -> None:
        self._draw_mech_zones_impl(painter, unit, profile, _BIPED_LABELS, _BIPED_PIPS)

    def _draw_mech_zones_impl(
        self, painter: QPainter, unit: BattleMech, profile: ConversionProfile,
        labels: dict, pips: dict,
    ) -> None:
        """Shared implementation for biped and quad zone rendering."""
        div = profile.mech_armor_divisor
        stroke, fill, sw, slice_mode = pip_colors(unit)

        # Pass 1: pips
        for zone, ldata in labels.items():
            pip_cfg = pips.get(zone, {})
            armor_pips = pip_cfg.get("armor")
            struct_pips = pip_cfg.get("structure")

            a_val = unit.destiny_armor(zone, div)
            if armor_pips:
                draw_pips(painter, armor_pips, a_val, stroke, fill, sw, slice_mode)

            if struct_pips and zone != "TR":
                s_val = unit.destiny_structure(zone)
                draw_pips(painter, struct_pips, s_val, "red", "white", 3,
                          struct_slice=unit.is_equipped_with("reinforced"))

        # Pass 2: zone labels on top
        for zone, ldata in labels.items():
            self._draw_zone_label(painter, ldata["x"], ldata["y"], ldata["text"])


class QuadCardRenderer(MechCardRenderer):
    """Quad mech: uses mech-qd.png silhouette; zone labels and pip layout differ."""
    SILHOUETTE_IMAGE = "mech-qd.png"

    def _draw_mech_zones(
        self, painter: QPainter, unit: BattleMech, profile: ConversionProfile
    ) -> None:
        self._draw_mech_zones_impl(painter, unit, profile, _QUAD_LABELS, _QUAD_PIPS)
