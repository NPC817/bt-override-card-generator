"""
AeroSpace Fighter card renderer.

Pip layouts from card_gen.js `fa` object (lines 12740-13210).
"""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap

from .card_renderer import (
    BaseCardRenderer, draw_pips, draw_text, pip_colors,
    FS_LARGE, FS_MEDIUM,
)
from ..models.aero import AeroSpaceFighter
from ..settings.profile import ConversionProfile

# ── ASF layout constants (fa in card_gen.js) ──────────────────────────────────

_AERO_LABELS = {
    "N":  {"x": 1450, "y": 300,  "text": "Nose\n(6,7,8)"},
    "LW": {"x": 1350, "y": 770,  "text": "Left\nWing\n(9,10,11)"},
    "RW": {"x": 1875, "y": 770,  "text": "Right\nWing\n(3,4,5)"},
    "A":  {"x": 1610, "y": 1350, "text": "Aft\n(2,12)"},
}

_AERO_PIPS = {
    "FU": {
        "structure": {
            "start": {"x": 1610, "y": 800},
            "steps": [
                {"x": 0, "y": 0},
                {"x": 0, "y": 1}, {"x": 0, "y": 1}, {"x": 0, "y": 1},
                {"x": 0, "y": 1}, {"x": 0, "y": 1}, {"x": 0, "y": 1},
                {"x": 0, "y": 1}, {"x": 0, "y": 1},
            ],
        },
    },
    "N": {
        "armor": {
            "start": {"x": 1610, "y": 575},
            "steps": [
                {"x": 0,   "y": 0},  {"x": 0,   "y": -1}, {"x": -2,  "y": 0},
                {"x": 4,   "y": 0},  {"x": -4,  "y": 1},  {"x": 4,   "y": 0},
                {"x": -6,  "y": -1}, {"x": 8,   "y": 0},  {"x": -8,  "y": 1},
                {"x": 8,   "y": 0},  {"x": -10, "y": -1}, {"x": 12,  "y": 0},
                {"x": -12, "y": 1},  {"x": 12,  "y": 0},  {"x": -14, "y": -1},
                {"x": 16,  "y": 0},  {"x": -8,  "y": -1}, {"x": -2,  "y": 0},
                {"x": 4,   "y": 0},  {"x": -6,  "y": 0},  {"x": 8,   "y": 0},
                {"x": -10, "y": 0},  {"x": 12,  "y": 0},  {"x": -14, "y": 0},
                {"x": 16,  "y": 0},  {"x": -10, "y": -1}, {"x": 4,   "y": 0},
                {"x": -2,  "y": 0},
            ],
            "mask": lambda e: e % 2 != 0 if e < 17 else e % 2 == 0,
        },
    },
    "LW": {
        "armor": {
            "start": {"x": 1500, "y": 1030},
            "steps": [
                {"x": 0,   "y": 0},  {"x": 0,   "y": -1}, {"x": -2,  "y": 0},
                {"x": 0,   "y": 1},  {"x": -2,  "y": 0},  {"x": 4,   "y": 1},
                {"x": -2,  "y": 0},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": 6,   "y": 1},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": -2,  "y": 0},  {"x": -2,  "y": 0},  {"x": 7,   "y": 1},
                {"x": -2,  "y": 0},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": -2,  "y": 0},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": 11,  "y": 1},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": -2,  "y": 0},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": -2,  "y": 0},  {"x": 11,  "y": 1},  {"x": -2,  "y": 0},
                {"x": -2,  "y": 0},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                {"x": -2,  "y": 0},
            ],
        },
    },
    "RW": {
        "armor": {
            "start": {"x": 1711, "y": 1030},
            "steps": [
                {"x": 0,    "y": 0},  {"x": 0,    "y": -1}, {"x": 2,    "y": 0},
                {"x": 0,    "y": 1},  {"x": 2,    "y": 0},  {"x": -4,   "y": 1},
                {"x": 2,    "y": 0},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": -6,   "y": 1},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": 2,    "y": 0},  {"x": 2,    "y": 0},  {"x": -7,   "y": 1},
                {"x": 2,    "y": 0},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": 2,    "y": 0},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": -11,  "y": 1},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": 2,    "y": 0},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": 2,    "y": 0},  {"x": -11,  "y": 1},  {"x": 2,    "y": 0},
                {"x": 2,    "y": 0},  {"x": 2,    "y": 0},  {"x": 2,    "y": 0},
                {"x": 2,    "y": 0},
            ],
        },
    },
    "A": {
        "armor": {
            "start": {"x": 1610, "y": 1130},
            "steps": [
                {"x": 0,   "y": 0},  {"x": 0,   "y": 1},  {"x": 0,   "y": 1},
                {"x": 0,   "y": 1},  {"x": 0,   "y": 1},  {"x": -2,  "y": -4},
                {"x": 4,   "y": 0},  {"x": -4,  "y": 1},  {"x": 4,   "y": 0},
                {"x": -6,  "y": 0},  {"x": 8,   "y": 0},  {"x": -6,  "y": 1},
                {"x": 4,   "y": 0},  {"x": -6,  "y": 0},  {"x": 8,   "y": 0},
                {"x": -10, "y": 0},  {"x": 12,  "y": 0},  {"x": -4,  "y": 1},
                {"x": -4,  "y": 0},  {"x": 6,   "y": 0},  {"x": -8,  "y": 0},
                {"x": 10,  "y": 0},  {"x": -12, "y": 0},  {"x": 8,   "y": 1},
                {"x": -4,  "y": 0},  {"x": 6,   "y": 0},  {"x": -8,  "y": 0},
                {"x": 10,  "y": 0},  {"x": -12, "y": 0},
            ],
        },
    },
}


class AeroCardRenderer(BaseCardRenderer):
    """Renders an AeroSpace Fighter card to a 2100×1500 QPixmap."""

    BASE_IMAGE       = "card-base.png"
    SILHOUETTE_IMAGE = "aero.png"

    def render(
        self,
        unit: AeroSpaceFighter,
        profile: ConversionProfile,
        weapons_rows: list[dict] | None = None,
        equipment_str: str = "",
    ) -> QPixmap:
        canvas, painter = self._build_canvas()

        is_conv = unit.motive_type == AeroSpaceFighter.CONVENTIONAL

        # Header — "Thrust:" instead of "Move:", +15 x-offsets per card_gen.js
        # Conventional fighters have no heat sinks → pass sinks_val=0 to suppress heat scale
        self._draw_unit_header(
            painter, unit,
            move_label="Thrust:", move_x_offset=15, tmm_x_offset=15,
            sinks_val=0 if is_conv else None,
            heat_scale_max=profile.heat_scale_max,
        )

        # Gunnery / Piloting labels
        draw_text(painter, 1155, 45, "Gunnery", size=FS_MEDIUM+4, bold=True, width=180, align=Qt.AlignmentFlag.AlignCenter)
        draw_text(painter, 1300, 45, "Piloting", size=FS_MEDIUM+4, bold=True, width=180, align=Qt.AlignmentFlag.AlignCenter)

        # DThr (damage threshold)
        draw_text(painter, 440, 415, "DThr:", size=FS_LARGE, bold=True)
        draw_text(painter, 545, 415, str(unit.dthr), size=FS_LARGE)

        # Weapons table — conventional fighters have no heat column
        rows = weapons_rows or []
        self._draw_weapons_table(painter, rows, has_heat=not is_conv)

        # Equipment
        self._draw_equipment_text(painter, equipment_str)

        # Right panel: zone labels + pips
        self._draw_aero_zones(painter, unit, profile)

        # Bottom section: condition monitor
        self._draw_condition_monitor(painter)

        painter.end()
        return canvas

    def _draw_aero_zones(
        self, painter: QPainter, unit: AeroSpaceFighter, profile: ConversionProfile
    ) -> None:
        div = profile.aero_armor_divisor
        stroke, fill, sw, slice_mode = pip_colors(unit)

        # Two-pass render: pips first so zone labels appear on top
        for zone in _AERO_LABELS:
            pip_cfg = _AERO_PIPS.get(zone, {})
            armor_pips = pip_cfg.get("armor")

            if armor_pips and unit.armor.get(zone, 0) > 0:
                a_val = unit.destiny_armor(zone, div)
                draw_pips(painter, armor_pips, a_val, stroke, fill, sw, slice_mode)

        # Fuselage structure (FU) — only structure on ASF card
        fu_pips = _AERO_PIPS.get("FU", {}).get("structure", {})
        if fu_pips:
            s_val = unit.destiny_structure()
            draw_pips(painter, fu_pips, s_val, "red", "white", 3,
                      struct_slice=unit.is_equipped_with("reinforced"))

        # Labels on top
        for zone, ldata in _AERO_LABELS.items():
            self._draw_zone_label(painter, ldata["x"], ldata["y"], ldata["text"])
