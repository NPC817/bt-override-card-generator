"""
Battle Armor card renderer.

Layout from card_gen.js `Ia` object (lines 14295-14529) and `Wa` component
(lines 14593-14979).
"""
from __future__ import annotations
import math
import textwrap

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QPen, QPixmap

from .card_renderer import (
    BaseCardRenderer, draw_text, _draw_hex, _load_image,
    PIP_RADIUS, FS_LARGE,
)
from ..models.battle_armor import BattleArmor
from ..settings.profile import ConversionProfile

# ── Layout constants (Ia in card_gen.js) ─────────────────────────────────────

_BA = {
    "unitName":        {"x": 60,  "y": 118},
    "unitDataLabel":   {"x": 60,  "y": 190},
    "typeLabel":       {"x": 60,  "y": 250},
    "type":            {"x": 170, "y": 250},
    "massLabel":       {"x": 60,  "y": 300},
    "mass":            {"x": 170, "y": 300},
    "moveLabel":       {"x": 60,  "y": 365},
    "move":            {"x": 170, "y": 365},
    "tmmLabel":        {"x": 60,  "y": 415},
    "tmm":             {"x": 170, "y": 415},
    "antimechBox":     {"x": 600, "y": 265},
    "antimech":        {"x": 605, "y": 270},
    "antimechLabel":   {"x": 660, "y": 300},
    "equipmentLabel":  {"x": 60,  "y": 485},
    "equipment":       {"x": 260, "y": 485},
    "troopsLabel":     {"x": 60,  "y": 565},
    "troopsRow":       {"yStart": 785, "yHeight": 120, "yDmgLabel": 685},
    "squadLabel":      {"x": 60,  "y": 710},
    "squadNumber":     {"x": 90,  "y": 825},
    "BA_icon":         {"x": 180, "y": 757},
    "BA_armorLabel":   {"x": 320, "y": 730},
    "BA_pips":         {"x": 300, "y": 812},
}

_BA_WEAPON_COLUMNS = [
    {"x": 560, "y": 585},
    {"x": 860, "y": 585},
    {"x": 1160, "y": 585},
    {"x": 1460, "y": 585},
    {"x": 1760, "y": 585},
]

FS_BA_LABEL = 36  # Ba in JS — most labels
FS_BA_SMALL = 28  # Pa in JS — weapon range values
FS_BA_VALUE = 32  # squad numbers, weapon names
_BA_PIP_SPACING = 33  # per-trooper horizontal pip spacing


def ba_pip_colors(unit: BattleArmor) -> tuple[str, str, int]:
    """Return (stroke, fill, stroke_width) for BA armor pips per specialization.
    Checks BA-specific equipment keys: bareflective, bareactive, bastealth,
    bafireresist, bamimetic. Fire-resistant (bafireresist) is BA-only."""
    if unit.is_equipped_with("bafireresist"):
        return ("rgba(233,116,0,1.00)",    "rgba(233,116,0,0.15)", 4)
    if unit.is_equipped_with("bareflective"):
        return ("green",                   "rgba(0,255,0,0.10)",   4)
    if unit.is_equipped_with("bareactive"):
        return ("blue",                    "rgba(0,255,255,0.15)", 4)
    if unit.is_equipped_with("bastealth"):
        return ("rgba(41,0,85,1.00)",      "rgba(127,0,255,0.10)", 4)
    if unit.is_equipped_with("bamimetic"):
        return ("black",                   "rgba(0,0,0,0.2)",      1)
    return ("black", "white", 3)


class BattleArmorRenderer(BaseCardRenderer):
    """Renders a Battle Armor card to a 2100×1500 QPixmap."""

    BASE_IMAGE = "card-base-ba.png"
    SILHOUETTE_IMAGE = None  # ba.png drawn inline per squad row

    def render(
        self,
        unit: BattleArmor,
        profile: ConversionProfile,
        weapons_rows: list[dict] | None = None,
        equipment_items: list[dict] | None = None,
    ) -> QPixmap:
        canvas, painter = self._build_canvas()

        # Left panel: unit identity header (same positions as all other unit types)
        self._draw_unit_header(painter, unit, mass_str=unit.mass_str)

        # Anti-Mech checkbox (computed, Bipeds only)
        if unit.motive_type == BattleArmor.BIPED:
            self._draw_ba_checkboxes(painter, unit)

        # Equipment
        self._draw_ba_equipment(painter, equipment_items)

        # Troopers & Weapons section
        self._draw_ba_troopers(painter, unit)

        # Weapon columns
        rows = weapons_rows or []
        self._draw_ba_weapons(painter, unit, rows)

        # Right panel labels
        self._draw_ba_right_panel(painter)

        painter.end()
        return canvas

    # ── Checkboxes ──────────────────────────────────────────────────────────

    def _draw_ba_checkboxes(self, painter: QPainter, unit: BattleArmor) -> None:
        # Anti-Mech Attack (Bipeds only)
        if unit.motive_type != BattleArmor.BIPED:
            return
        bx, by = _BA["antimechBox"]["x"], _BA["antimechBox"]["y"]
        painter.setPen(QPen(QColor("black"), 3))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawRect(bx, by, 40, 40)
        if unit.has_anti_mech:
            self._draw_x_mark(painter, _BA["antimech"]["x"], _BA["antimech"]["y"])
        draw_text(painter, _BA["antimechLabel"]["x"], _BA["antimechLabel"]["y"],
                  "Anti-Mech Attack", size=FS_BA_LABEL)

    # ── Equipment ───────────────────────────────────────────────────────────

    def _draw_ba_equipment(
        self, painter: QPainter, items: list[dict] | None,
    ) -> None:
        draw_text(painter, _BA["equipmentLabel"]["x"], _BA["equipmentLabel"]["y"],
                  "Equipment:", size=FS_BA_LABEL, bold=True)
        if items:
            # Build text from non-ammo items, then ammo items as a simple list
            non_ammo = [it["label"] for it in items if not it.get("is_ammo")]
            ammo = [it for it in items if it.get("is_ammo")]
            parts = non_ammo + [it["label"] for it in ammo]
            wrapped = textwrap.fill(", ".join(parts), width=65)
            draw_text(painter, _BA["equipment"]["x"], _BA["equipment"]["y"],
                      wrapped, size=FS_BA_SMALL)

    # ── Troopers ────────────────────────────────────────────────────────────

    def _draw_ba_troopers(
        self, painter: QPainter, unit: BattleArmor
    ) -> None:
        draw_text(painter, _BA["troopsLabel"]["x"], _BA["troopsLabel"]["y"] + 30,
                  "TROOPERS & WEAPONS", size=44, bold=True)

        stroke, fill, sw = ba_pip_colors(unit)
        ba_icon = _load_image("ba.png")
        a_val = unit.destiny_armor()
        ss = unit.squad_size

        for g in range(ss):
            row_y_off = g * _BA["troopsRow"]["yHeight"]
            trooper_num = ss - g  # descending: 4, 3, 2, 1

            # Trooper number
            draw_text(painter, _BA["squadNumber"]["x"],
                      _BA["squadNumber"]["y"] + row_y_off,
                      str(trooper_num), size=FS_BA_VALUE)

            # BA icon per row
            if ba_icon:
                icon_w, icon_h = ba_icon.width(), ba_icon.height()
                painter.drawPixmap(
                    _BA["BA_icon"]["x"],
                    _BA["BA_icon"]["y"] + row_y_off,
                    icon_w, icon_h, ba_icon,
                )

            # "Armor" label on first row only
            if g == 0:
                draw_text(painter, _BA["BA_armorLabel"]["x"],
                          _BA["BA_armorLabel"]["y"], "Armor", size=FS_BA_LABEL, bold=True)

            pip_x = _BA["BA_pips"]["x"]
            pip_y = _BA["BA_pips"]["y"] + row_y_off

            # Structure pip (red, first position)
            _draw_hex(painter, pip_x, pip_y, PIP_RADIUS, "red", "white", 3)

            # Reinforced structure slice
            if unit.is_equipped_with("reinforced"):
                c2 = PIP_RADIUS / 2
                u = PIP_RADIUS * math.sqrt(3) / 2
                painter.setPen(QPen(QColor("red"), 2))
                painter.drawLine(
                    round(pip_x - c2), round(pip_y - u),
                    round(pip_x + c2), round(pip_y + u),
                )

            # Armor pips per trooper
            pip_x += _BA_PIP_SPACING
            for _ in range(a_val):
                _draw_hex(painter, pip_x, pip_y, PIP_RADIUS, stroke, fill, sw)
                pip_x += _BA_PIP_SPACING

    # ── Weapons ─────────────────────────────────────────────────────────────

    def _draw_ba_weapons(
        self, painter: QPainter, unit: BattleArmor, weapon_rows: list[dict]
    ) -> None:
        cols = _BA_WEAPON_COLUMNS

        for i, w in enumerate(weapon_rows):
            if i >= len(cols):
                break
            col = cols[i]

            # Weapon name
            draw_text(painter, col["x"], col["y"] - 27,
                      w.get("name", ""), size=FS_BA_VALUE, bold=True,
                      width=300, align=Qt.AlignmentFlag.AlignCenter)

            # Range bands (PB/S/M/L) — between name and damage
            range_y = col["y"] + 30
            for offset, label in [(-90, "PB"), (-30, "S"), (30, "M"), (90, "L")]:
                key = f"range{label}"
                val = w.get(key, "—")
                draw_text(painter, col["x"] + offset, range_y,
                          f"{label}\n{val}", size=FS_BA_SMALL,
                          width=300, align=Qt.AlignmentFlag.AlignCenter)

            # Damage header label
            draw_text(painter, col["x"], _BA["troopsRow"]["yDmgLabel"],
                      "Dmg", size=FS_BA_LABEL, bold=True,
                      width=300, align=Qt.AlignmentFlag.AlignCenter)

            # Per-squad-size damage values (damage is list [dmg@N, dmg@N-1, ..., dmg@1])
            damage = w.get("damage", "")
            if isinstance(damage, list):
                for gi in range(len(damage)):
                    y = (_BA["troopsRow"]["yStart"]
                         + gi * _BA["troopsRow"]["yHeight"])
                    draw_text(painter, col["x"], y,
                              str(damage[gi]), size=FS_BA_LABEL,
                              width=300, align=Qt.AlignmentFlag.AlignCenter)
            else:
                draw_text(painter, col["x"], _BA["troopsRow"]["yStart"],
                          str(damage), size=FS_BA_VALUE,
                          width=300, align=Qt.AlignmentFlag.AlignCenter)

        # Anti-Infantry row (always 5th slot per JS lines 9060-9078)
        if len(cols) >= 5:
            col = cols[4]
            draw_text(painter, col["x"], col["y"] - 27,
                      "Anti-Infantry", size=FS_BA_VALUE, bold=True,
                      width=300, align=Qt.AlignmentFlag.AlignCenter)

            # Range bands between name and damage
            anti_range_y = col["y"] + 30
            for offset, label, val in [(-90, "PB", "+0"), (-30, "S", "+0"),
                                        (30, "M", "—"), (90, " L", "—")]:
                draw_text(painter, col["x"] + offset, anti_range_y,
                          f"{label}\n{val}", size=FS_BA_SMALL,
                          width=300, align=Qt.AlignmentFlag.AlignCenter)

            draw_text(painter, col["x"], _BA["troopsRow"]["yDmgLabel"],
                      "Dmg", size=FS_BA_LABEL, bold=True,
                      width=300, align=Qt.AlignmentFlag.AlignCenter)

            for gi in range(unit.squad_size):
                squad_row = unit.squad_size - 1 - gi
                y = (_BA["troopsRow"]["yStart"]
                     + squad_row * _BA["troopsRow"]["yHeight"])
                draw_text(painter, col["x"], y,
                          f"{gi + 1}d6", size=FS_BA_LABEL,
                          width=300, align=Qt.AlignmentFlag.AlignCenter)

    # ── Right panel ─────────────────────────────────────────────────────────

    def _draw_ba_right_panel(self, painter: QPainter) -> None:
        draw_text(painter, 1155, 45, "Gunnery", size=FS_BA_VALUE, bold=True,
                  width=180, align=Qt.AlignmentFlag.AlignCenter)
        draw_text(painter, 1300, 45, "Anti-Mech", size=FS_BA_VALUE, bold=True,
                  width=180, align=Qt.AlignmentFlag.AlignCenter)
