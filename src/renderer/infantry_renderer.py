"""
Infantry card renderer.

Structured to mirror ba_renderer.py. Coordinates from card_gen.js Ia object
(lines 14295–14529) aligned with BA positions where shared.
"""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPen, QBrush, QPainter, QPixmap

import textwrap

from .card_renderer import (
    BaseCardRenderer, draw_text, _draw_hex, _load_image, PIP_RADIUS,
)
from ..models.infantry import Infantry
from ..settings.profile import ConversionProfile

# ── Layout constants (mirrors _BA in ba_renderer.py) ─────────────────────────

_IN = {
    "unitName":       {"x": 60,  "y": 34},
    "unitDataLabel":  {"x": 60,  "y": 190},
    "typeLabel":      {"x": 60,  "y": 250},
    "type":           {"x": 190, "y": 250},
    "massLabel":      {"x": 60,  "y": 300},
    "mass":           {"x": 190, "y": 300},
    "antimechBox":    {"x": 600, "y": 265},
    "antimech":       {"x": 605, "y": 270},
    "antimechLabel":  {"x": 660, "y": 300},
    "moveLabel":      {"x": 60,  "y": 365},
    "move":           {"x": 190, "y": 365},
    "tmmLabel":       {"x": 60,  "y": 415},
    "tmm":            {"x": 190, "y": 415},
    "equipmentLabel": {"x": 60,  "y": 485},
    "equipment":      {"x": 260, "y": 485},
    "troopsLabel":    {"x": 60,  "y": 565},
    "troopsRow":      {"yStart": 785, "yHeight": 120, "yDmgLabel": 685},
    "squadNumber":    {"x": 90,  "y": 825},
    "IN_icon":        {"x": 180, "y": 757},
    "IN_pips":        [
        {"x": 420, "y": 812},
        {"x": 870, "y": 812},
        {"x": 1320, "y": 812},
    ],
    "IN_platoonLabels": [
        {"x": 470, "y": 725},
        {"x": 920, "y": 725},
        {"x": 1370, "y": 725},
    ],
    "IN_platoonTracking": [
        {"x": 1430, "y": 100},
        {"x": 1430, "y": 199},
        {"x": 1430, "y": 301},
    ],
}

# Single weapon column (infantry has one weapon type, not per-TIC)
_IN_WEAPON_COLUMN = {"x": 1760, "y": 585}

# Font sizes — mirror card_renderer.py constants, prefixed _IN_
_IN_FS_XXLARGE = 60   # FS_XXLARGE — unit name base size
_IN_FS_XLARGE  = 48   # FS_XLARGE  — section headers ("UNIT DATA", "TROOPERS & WEAPONS")
_IN_FS_LARGE   = 38   # FS_LARGE   — Type/Mass/Move/TMM labels and values
_IN_FS_MEDIUM  = 28   # FS_MEDIUM  — range-band headers/values, equipment text
_IN_FS_VALUE   = 32   # squad numbers, damage values, weapon name (no base equivalent)
_IN_PIP_SPACING = 33  # horizontal gap between pips


class InfantryCardRenderer(BaseCardRenderer):
    """Renders an Infantry card to a 2100×1500 QPixmap."""

    BASE_IMAGE       = "card-base-in.png"
    SILHOUETTE_IMAGE = None  # infantry.png drawn inline per squad row

    def render(
        self,
        unit: Infantry,
        profile: ConversionProfile,
        weapons_rows: list[dict] | None = None,
        equipment_items: list[dict] | None = None,
    ) -> QPixmap:
        canvas, painter = self._build_canvas()

        self._draw_in_header(painter, unit)
        self._draw_in_checkboxes(painter, unit)
        self._draw_in_equipment(painter, unit)
        self._draw_in_troopers(painter, unit)
        self._draw_in_weapons(painter, unit)
        self._draw_in_right_panel(painter)

        painter.end()
        return canvas

    # ── Header ───────────────────────────────────────────────────────────────

    def _draw_in_header(self, painter: QPainter, unit: Infantry) -> None:
        draw_text(painter, _IN["unitName"]["x"], _IN["unitName"]["y"],
                  unit.display_name, size=_IN_FS_XXLARGE + 12, bold=True, family="vegas", width=1060)

        draw_text(painter, _IN["unitDataLabel"]["x"], _IN["unitDataLabel"]["y"],
                  "Unit Data", size=_IN_FS_XLARGE, bold=True)

        draw_text(painter, _IN["typeLabel"]["x"], _IN["typeLabel"]["y"],
                  "Type:", size=_IN_FS_LARGE, bold=True)
        draw_text(painter, _IN["type"]["x"], _IN["type"]["y"],
                  unit.type_name, size=_IN_FS_LARGE)

        draw_text(painter, _IN["massLabel"]["x"], _IN["massLabel"]["y"],
                  "Mass:", size=_IN_FS_LARGE, bold=True)
        draw_text(painter, _IN["mass"]["x"], _IN["mass"]["y"],
                  f"{unit.tonnage} Tons", size=_IN_FS_LARGE)

        draw_text(painter, _IN["moveLabel"]["x"], _IN["moveLabel"]["y"],
                  "Move:", size=_IN_FS_LARGE, bold=True)
        draw_text(painter, _IN["move"]["x"], _IN["move"]["y"],
                  unit.destiny_move, size=_IN_FS_LARGE)

        draw_text(painter, _IN["tmmLabel"]["x"], _IN["tmmLabel"]["y"],
                  "TMM:", size=_IN_FS_LARGE, bold=True)
        draw_text(painter, _IN["tmm"]["x"], _IN["tmm"]["y"],
                  unit.destiny_tmm, size=_IN_FS_LARGE)

    # ── Anti-Mech checkbox (mirrors _draw_ba_checkboxes) ─────────────────────

    def _draw_in_checkboxes(self, painter: QPainter, unit: Infantry) -> None:
        bx, by = _IN["antimechBox"]["x"], _IN["antimechBox"]["y"]
        painter.setPen(QPen(QColor("black"), 3))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawRect(bx, by, 40, 40)
        if unit.has_anti_mech:
            self._draw_x_mark(painter, _IN["antimech"]["x"], _IN["antimech"]["y"])
        draw_text(painter, _IN["antimechLabel"]["x"], _IN["antimechLabel"]["y"],
                  "Anti-Mech Attack", size=_IN_FS_LARGE)

    # ── Equipment (mirrors _draw_ba_equipment) ────────────────────────────────

    def _draw_in_equipment(self, painter: QPainter, unit: Infantry) -> None:
        draw_text(painter, _IN["equipmentLabel"]["x"], _IN["equipmentLabel"]["y"],
                  "Equipment:", size=_IN_FS_LARGE, bold=True)

        parts: list[str] = []
        if unit.armor_kit:
            parts.append(unit.armor_kit)
        if unit.trooper_equipment:
            parts.append(unit.trooper_equipment)
        if unit.field_guns:
            parts.extend(unit.field_guns)
        equip_text = ", ".join(parts)
        if equip_text:
            wrapped = textwrap.fill(equip_text, width=65)
            draw_text(painter, _IN["equipment"]["x"], _IN["equipment"]["y"],
                      wrapped, size=_IN_FS_MEDIUM)

    # ── Troopers section (mirrors _draw_ba_troopers) ──────────────────────────

    def _draw_in_troopers(self, painter: QPainter, unit: Infantry) -> None:
        draw_text(painter, _IN["troopsLabel"]["x"], _IN["troopsLabel"]["y"] + 30,
                  "TROOPERS & WEAPONS", size=_IN_FS_XLARGE, bold=True)

        icon = _load_image("infantry.png")
        n    = unit.squad_count

        # Platoon column headers inside the grid
        for i, plat in enumerate(_IN["IN_platoonLabels"]):
            draw_text(painter, plat["x"], plat["y"],
                      f"Platoon {i + 1}", size=_IN_FS_LARGE, bold=True)

        for row in range(n):
            row_y_off = row * _IN["troopsRow"]["yHeight"]
            squad_num = n - row

            # Squad number
            draw_text(painter, _IN["squadNumber"]["x"],
                      _IN["squadNumber"]["y"] + row_y_off,
                      str(squad_num), size=_IN_FS_VALUE)

            # Infantry icon per row
            if icon:
                painter.drawPixmap(
                    _IN["IN_icon"]["x"],
                    _IN["IN_icon"]["y"] + row_y_off,
                    icon,
                )

        # Pip grid: 3 platoon columns × n rows × squad_size pips each
        self._draw_in_pip_grid(painter, unit, n)

    def _draw_in_pip_grid(self, painter: QPainter, unit: Infantry, n: int) -> None:
        squad_size = unit.squad_size
        x_offset = (7 - squad_size) * 16.5  # right-justify to max squad size 7

        for g, pip_start in enumerate(_IN["IN_pips"]):
            sx, sy = pip_start["x"], pip_start["y"]
            for row in range(n):
                m = sx + x_offset
                c = sy + row * _IN["troopsRow"]["yHeight"]
                for _ in range(squad_size):
                    m += _IN_PIP_SPACING
                    _draw_hex(painter, round(m), round(c),
                              PIP_RADIUS, "black", "white", 3)

    # ── Weapon column (mirrors _draw_ba_weapons) ──────────────────────────────

    def _draw_in_weapons(self, painter: QPainter, unit: Infantry) -> None:
        wdata = Infantry.WEAPON_DATA.get(unit.weapon_type)
        if not wdata:
            return

        n   = unit.squad_count
        col = _IN_WEAPON_COLUMN

        # Weapon name — append " (AI)" for anti-infantry weapons per card_gen.js line 9621
        name = wdata["name"] + (" (AI)" if wdata.get("anti_infantry") else "")
        draw_text(painter, col["x"], col["y"] - 27,
                  name, size=_IN_FS_VALUE, bold=True,
                  width=300, align=Qt.AlignmentFlag.AlignCenter)

        # Range bands PB / S / M / L
        range_y = col["y"] + 30
        for offset, label in [(-90, "PB"), (-30, "S"), (30, "M"), (90, "L")]:
            val = wdata.get(f"range{label}", "--")
            draw_text(painter, col["x"] + offset, range_y,
                      f"{label}\n{val}", size=_IN_FS_MEDIUM,
                      width=300, align=Qt.AlignmentFlag.AlignCenter)

        # "Dmg" header
        draw_text(painter, col["x"], _IN["troopsRow"]["yDmgLabel"],
                  "Dmg", size=_IN_FS_LARGE, bold=True,
                  width=300, align=Qt.AlignmentFlag.AlignCenter)

        # Damage per squad row (descending: full platoon → 1 squad)
        for row in range(n):
            squads = n - row
            dmg = unit.weapon_damage(squads)
            y   = _IN["troopsRow"]["yStart"] + row * _IN["troopsRow"]["yHeight"]
            draw_text(painter, col["x"], y,
                      dmg, size=_IN_FS_VALUE,
                      width=300, align=Qt.AlignmentFlag.AlignCenter)

    # ── Right panel (mirrors _draw_ba_right_panel) ────────────────────────────

    def _draw_in_right_panel(self, painter: QPainter) -> None:
        draw_text(painter, 1155, 45, "Gunnery",   size=_IN_FS_VALUE, bold=True,
                  width=180, align=Qt.AlignmentFlag.AlignCenter)
        draw_text(painter, 1300, 45, "Anti-Mech", size=_IN_FS_VALUE, bold=True,
                  width=180, align=Qt.AlignmentFlag.AlignCenter)

        for i, plat in enumerate(_IN["IN_platoonTracking"]):
            self._draw_centered(painter, plat["x"], plat["y"],
                                f"Platoon {i + 1}", 180, _IN_FS_VALUE, bold=True)
