"""
CombatVehicle (and VTOL) card renderer.

Pip layouts from card_gen.js `Ma` (tracked/wheeled/hover) and `La` (VTOL).
"""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap

from .card_renderer import (
    BaseCardRenderer, draw_pips, pip_colors, draw_text, _load_image,
    CARD_W, CARD_H, FS_MEDIUM,
)
from ..models.vehicle import CombatVehicle
from ..settings.profile import ConversionProfile

# ── Tracked / Wheeled / Hover layout (Ma in card_gen.js) ─────────────────────

_GROUND_LABELS = {
    "FR": {"x": 1610, "y": 240,  "text": "Front\n(6,7,8)"},
    "LS": {"x": 1215, "y": 800,  "text": "Left Side\n(9,10,11)"},
    "RS": {"x": 2005, "y": 800,  "text": "Right Side\n(3,4,5)"},
    "RR": {"x": 1610, "y": 1400, "text": "Rear"},
}

_TURRET_LABELS = {
    "FR": {"x": 1610, "y": 240,  "text": "Front\n(6,7,8)"},
    "TU": {"x": 1610, "y": 1137, "text": "Turret (5,9)"},
    "LS": {"x": 1215, "y": 800,  "text": "Left Side\n(10,11)"},
    "RS": {"x": 2005, "y": 800,  "text": "Right Side\n(3,4)"},
    "RR": {"x": 1610, "y": 1400, "text": "Rear"},
}

_GROUND_PIPS = {
    "FR": {
        "armor": {
            "start": {"x": 1610, "y": 530},
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
            "mask": lambda e: (e < 17 and e % 2 != 0) or (e >= 17 and e % 2 == 0),
        },
        "structure": {
            "start": {"x": 1610, "y": 607},
            "steps": [
                {"x": 0, "y": 0}, {"x": -2, "y": 0}, {"x": 4, "y": 0},
            ],
            "mask": lambda e: e % 2 == 0,
        },
    },
    "LS": {
        "armor": {
            "start": {"x": 1450, "y": 710},
            "steps": [
                {"x": 0,    "y": 0},  {"x": 0.2,  "y": -1}, {"x": -0.4, "y": 2},
                {"x": 0.6,  "y": -3}, {"x": -0.8, "y": 4},  {"x": -1.6, "y": -2},
                {"x": 0.2,  "y": -1}, {"x": -0.4, "y": 2},  {"x": 0.6,  "y": -3},
                {"x": -0.8, "y": 4},  {"x": 1,    "y": -5}, {"x": -1.2, "y": 6},
                {"x": 1.4,  "y": -7}, {"x": -2.8, "y": 4},  {"x": 0.2,  "y": -1},
                {"x": -0.4, "y": 2},  {"x": 0.6,  "y": -3}, {"x": -0.8, "y": 4},
                {"x": 1,    "y": -5}, {"x": -1.2, "y": 6},  {"x": 1.4,  "y": -7},
                {"x": -1.6, "y": 8},  {"x": 1.8,  "y": -9},
            ],
        },
        "structure": {
            "start": {"x": 1422, "y": 918},
            "steps": [
                {"x": 0,    "y": 0},  {"x": 0.35, "y": -1}, {"x": -0.7, "y": 2},
            ],
            "mask": lambda e: e % 2 == 0,
        },
    },
    "RS": {
        "armor": {
            "start": {"x": 1770, "y": 710},
            "steps": [
                {"x": 0,    "y": 0},  {"x": -0.2, "y": -1}, {"x": 0.4,  "y": 2},
                {"x": -0.6, "y": -3}, {"x": 0.8,  "y": 4},  {"x": 1.6,  "y": -2},
                {"x": -0.2, "y": -1}, {"x": 0.4,  "y": 2},  {"x": -0.6, "y": -3},
                {"x": 0.8,  "y": 4},  {"x": -1,   "y": -5}, {"x": 1.2,  "y": 6},
                {"x": -1.4, "y": -7}, {"x": 2.8,  "y": 4},  {"x": -0.2, "y": -1},
                {"x": 0.4,  "y": 2},  {"x": -0.6, "y": -3}, {"x": 0.8,  "y": 4},
                {"x": -1,   "y": -5}, {"x": 1.2,  "y": 6},  {"x": -1.4, "y": -7},
                {"x": 1.6,  "y": 8},  {"x": -1.8, "y": -9},
            ],
        },
        "structure": {
            "start": {"x": 1798, "y": 918},
            "steps": [
                {"x": 0,    "y": 0},  {"x": -0.35,"y": -1}, {"x": 0.7,  "y": 2},
            ],
            "mask": lambda e: e % 2 == 0,
        },
    },
    "RR": {
        "armor": {
            "start": {"x": 1610, "y": 1295},
            "steps": [
                {"x": 0,   "y": 0},  {"x": -2,  "y": 0},  {"x": 4,   "y": 0},
                {"x": -6,  "y": 0},  {"x": 8,   "y": 0},  {"x": -10, "y": 0},
                {"x": 12,  "y": 0},  {"x": -12, "y": -1}, {"x": 12,  "y": 0},
                {"x": -14, "y": 0},  {"x": 16,  "y": 0},  {"x": -18, "y": 0},
                {"x": 20,  "y": 0},  {"x": -16, "y": -1}, {"x": 12,  "y": 0},
                {"x": -14, "y": 0},  {"x": 16,  "y": 0},
            ],
            "mask": lambda e: e % 2 == 0,
        },
        "structure": {
            "start": {"x": 1610, "y": 1225},
            "steps": [
                {"x": 0, "y": 0}, {"x": -2, "y": 0}, {"x": 4, "y": 0},
            ],
            "mask": lambda e: e % 2 == 0,
        },
    },
    "TU": {
        "armor": {
            "start": {"x": 1610, "y": 860},
            "steps": [
                {"x": 0,  "y": 0},  {"x": 0,  "y": 1},  {"x": -2, "y": 0},
                {"x": 4,  "y": 0},  {"x": -3, "y": 1},  {"x": 2,  "y": 0},
                {"x": -4, "y": 0},  {"x": 6,  "y": 0},  {"x": -4, "y": 1},
                {"x": 2,  "y": 0},  {"x": -4, "y": 0},  {"x": 6,  "y": 0},
                {"x": -4, "y": 1},  {"x": 2,  "y": 0},  {"x": -4, "y": 0},
                {"x": 6,  "y": 0},  {"x": -4, "y": 1},  {"x": 2,  "y": 0},
                {"x": -4, "y": 0},  {"x": 6,  "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
        "structure": {
            "start": {"x": 1610, "y": 1060},
            "steps": [
                {"x": 0, "y": 0}, {"x": -2, "y": 0}, {"x": 4, "y": 0},
            ],
            "mask": lambda e: e % 2 == 0,
        },
    },
}

# ── VTOL layout (La in card_gen.js) ──────────────────────────────────────────

_VTOL_LABELS = {
    "FR": {"x": 1610, "y": 275,  "text": "Front (6,7,8)"},
    "LS": {"x": 1390, "y": 500,  "text": "Left\nSide\n(10,11)"},
    "RS": {"x": 1830, "y": 500,  "text": "Right\nSide\n(3,4)"},
    "RR": {"x": 1500, "y": 1120, "text": "Rear"},
    "RO": {"x": 1300, "y": 780,  "text": "Rotor\n(5,9)"},
}

# ── VTOL pip layout (La in card_gen.js) ──────────────────────────────────────

_VTOL_PIPS = {
    "FR": {
        "armor": {
            "start": {"x": 1609, "y": 430},
            "steps": [
                {"x": 0,  "y": 0}, {"x": 0,  "y": -1}, {"x": -2, "y": 0},
                {"x": 4,  "y": 0}, {"x": -4, "y": 1},  {"x": 4,  "y": 0},
                {"x": -6, "y": 0}, {"x": 8,  "y": 0},
            ],
            "mask": lambda e: e % 2 != 0,
        },
        "structure": {
            "start": {"x": 1609, "y": 500},
            "steps": [{"x": 0, "y": 0}],
        },
    },
    "LS": {
        "armor": {
            "start": {"x": 1519, "y": 590},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": 2},
                {"x": 0, "y": -3}, {"x": 0, "y": 4},
            ],
        },
        "structure": {
            "start": {"x": 1531, "y": 800},
            "steps": [{"x": 0, "y": 0}],
        },
    },
    "RS": {
        "armor": {
            "start": {"x": 1699, "y": 590},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": -1}, {"x": 0, "y": 2},
                {"x": 0, "y": -3}, {"x": 0, "y": 4},
            ],
        },
        "structure": {
            "start": {"x": 1687, "y": 800},
            "steps": [{"x": 0, "y": 0}],
        },
    },
    "RR": {
        "armor": {
            "start": {"x": 1613, "y": 1130},
            "steps": [
                {"x": 0, "y": 0}, {"x": 0, "y": 1}, {"x": 0, "y": 1}, {"x": 0, "y": 1},
            ],
        },
        "structure": {
            "start": {"x": 1613, "y": 1060},
            "steps": [{"x": 0, "y": 0}],
        },
    },
    "RO": {
        "armor": {
            "start": {"x": 1609, "y": 698},
            "steps": [{"x": 0, "y": 0}],
        },
        "structure": {
            "start": {"x": 1609, "y": 740},
            "steps": [{"x": 0, "y": 0}],
        },
    },
}


class VehicleCardRenderer(BaseCardRenderer):
    """Renders a CombatVehicle card to a 2100×1500 QPixmap."""

    BASE_IMAGE       = "card-base.png"
    SILHOUETTE_IMAGE = "vehicle.png"

    def render(
        self,
        unit: CombatVehicle,
        profile: ConversionProfile,
        weapons_rows: list[dict] | None = None,
        equipment_str: str = "",
    ) -> QPixmap:
        if unit.motive_type == CombatVehicle.VTOL:
            self.SILHOUETTE_IMAGE = "vtol.png"

        # Build base canvas via base class (skip silhouette — we insert motive
        # overlays between base and silhouette for correct layering)
        saved_sil = self.SILHOUETTE_IMAGE
        self.SILHOUETTE_IMAGE = None
        canvas, painter = self._build_canvas()
        self.SILHOUETTE_IMAGE = saved_sil

        # Motive-type overlays BELOW silhouette
        if unit.motive_type == CombatVehicle.TRACKED:
            treads = _load_image("vehicle-treads.png")
            if treads:
                painter.drawPixmap(0, 0, CARD_W, CARD_H, treads)
        elif unit.motive_type == CombatVehicle.WHEELED:
            wheels = _load_image("vehicle-wheels.png")
            if wheels:
                painter.drawPixmap(0, 0, CARD_W, CARD_H, wheels)

        # Silhouette ON TOP of motive-type overlay
        if saved_sil:
            sil = _load_image(saved_sil)
            if sil:
                painter.drawPixmap(0, 0, CARD_W, CARD_H, sil)

        # Turret ON TOP of silhouette
        if unit.has_turret:
            turret_img = _load_image("vehicle-turret.png")
            if turret_img:
                painter.drawPixmap(0, 0, CARD_W, CARD_H, turret_img)

        # Header
        self._draw_unit_header(painter, unit, move_label="Move:",
                               heat_scale_max=profile.heat_scale_max)

        # Gunnery / Piloting labels
        draw_text(painter, 1155, 45, "Gunnery", size=FS_MEDIUM+4, bold=True, width=180, align=Qt.AlignmentFlag.AlignCenter)
        draw_text(painter, 1300, 45, "Piloting", size=FS_MEDIUM+4, bold=True, width=180, align=Qt.AlignmentFlag.AlignCenter)

        # Weapons table (no heat for vehicles)
        rows = weapons_rows or []
        self._draw_weapons_table(painter, rows, has_heat=False)

        # Equipment
        self._draw_equipment_text(painter, equipment_str)

        # Right panel: zone labels, values, pips
        self._draw_vehicle_zones(painter, unit, profile)

        # Bottom section: condition monitor
        self._draw_condition_monitor(painter)

        painter.end()
        return canvas

    def _draw_vehicle_zones(
        self, painter, unit: CombatVehicle, profile: ConversionProfile
    ) -> None:
        div = profile.vehicle_armor_divisor
        s_val = unit.destiny_structure()
        stroke, fill, sw, slice_mode = pip_colors(unit)

        if unit.motive_type == CombatVehicle.VTOL:
            labels = _VTOL_LABELS
            pips  = _VTOL_PIPS
        elif unit.has_turret:
            labels = _TURRET_LABELS
            pips  = _GROUND_PIPS
        else:
            labels = _GROUND_LABELS
            pips  = _GROUND_PIPS

        # Two-pass render: pips first so zone labels appear on top
        for zone, ldata in labels.items():
            pip_cfg = pips.get(zone, {})
            armor_pips = pip_cfg.get("armor")
            struct_pips = pip_cfg.get("structure")

            if zone in unit.armor and unit.armor[zone] > 0:
                a_val = unit.destiny_armor(zone, div)
                if armor_pips:
                    draw_pips(painter, armor_pips, a_val, stroke, fill, sw, slice_mode)

            if struct_pips:
                draw_pips(painter, struct_pips, s_val, "red", "white", 3, struct_slice=unit.is_equipped_with("reinforced"))

        for zone, ldata in labels.items():
            lx, ly = ldata["x"], ldata["y"]
            self._draw_zone_label(painter, lx, ly, ldata["text"])
