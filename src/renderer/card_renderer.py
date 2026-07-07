"""
Base card renderer using QPainter + PNG compositing.

Card canvas: 2100 × 1500 px (as used in card_gen.js: Ya=2100, Za=1500).
Coordinates match those in card_gen.js directly.
"""
from __future__ import annotations
import math
import os
import re
from typing import Optional

from PyQt6.QtCore import Qt, QPointF, QRectF
from PyQt6.QtGui import (
    QColor, QFont, QFontDatabase, QPainter, QPen, QBrush,
    QPixmap, QPolygonF,
)

# ── Constants (mirror card_gen.js) ───────────────────────────────────────────

CARD_W = 2100
CARD_H = 1500

# Font sizes
FS_XXLARGE = 60   # je – labels, Card name
FS_XLARGE = 48   # je – labels, header values
FS_LARGE  = 38   # je – labels, Move/TMM values Mass value
FS_MEDIUM = 28   # we – weapon rows, heat numbers
FS_SMALL  = 15   # Ee – pip radius (not a font size, but same constant)

# Heat scale color array
heat_colors = [
      '#FFFFFF',  # 0 - white
      '#FBF6E8',  # 1
      '#F9F0C9',  # 2
      '#F7E2AA',  # 3
      '#F5D48C',  # 4
      '#F3C56E',  # 5
      '#F1B651',  # 6
      '#EFAB34',  # 7
      '#ED9C16',  # 8
      '#EB8E00',  # 9
      '#E98000',  # 10
      '#E77000',  # 11
      '#E46000',  # 12
      '#E15000',  # 13
      '#DF4500',  # 14
      '#DC3D00',  # 15
      '#D83600',  # 16
      '#D43200',  # 17
      '#CF2C00',  # 18
      '#CB2900',  # 19
      '#C62600',  # 20
      '#C02300',  # 21
      '#BB2100',  # 22
      '#B51F00',  # 23
      '#AF1D00',  # 24
      '#A81C00',  # 25
      '#991B00',  # 26
      '#7F1800',  # 27
      '#4D1000',  # 28
      '#000000',  # 29 - black
]

# Pip geometry
PIP_RADIUS  = 15                               # Ee
PIP_H       = PIP_RADIUS * math.sqrt(3) + 1.5 # row spacing (~27.46)
PIP_X_MULT  = 16.5                             # column spacing

# Ammo pip constants (75% of armor pip scale)
AMMO_PIP_RADIUS   = 11        # 15 * 0.75 ≈ 11
AMMO_PIP_H        = AMMO_PIP_RADIUS * math.sqrt(3) - 2.0  # row spacing ~23
AMMO_PIP_X_MULT   = 20.0      # horizontal spacing for hex grid
AMMO_PIPS_PER_ROW = 25        # max pips per row
AMMO_PIPS_MIN_ROWS = 5         # pips before splitting to multiple rows
AMMO_MAX_PIP_SHOTS = 50       # suppress pips when total shots exceeds this

# Equipment text layout
EQUIPMENT_START_X = 60         # left edge of equipment text block
EQUIPMENT_MAX_W   = 1050         # max width of equipment text block
EQUIPMENT_PAD_LEFT = 200          # extra left padding (blank space at front)

from ..utils.paths import resource_path as _resource_path
_IMG_DIR  = str(_resource_path("images"))
_FONT_DIR = str(_resource_path("fonts"))

# ── Font loading ──────────────────────────────────────────────────────────────

class _FontState:
    loaded = False
    falcon = "Arial"
    vegas  = "Arial"


def _load_fonts() -> None:
    if _FontState.loaded:
        return
    _FontState.loaded = True

    for prefix, attr in [
        ("falcon-regular-webfont", "falcon"),
        ("falcon-bold-webfont",    "falcon"),  # same family, adds bold weight
        ("vegas-regular-webfont",  "vegas"),
    ]:
        path = os.path.join(_FONT_DIR, f"{prefix}.ttf")
        if os.path.exists(path):
            fid = QFontDatabase.addApplicationFont(path)
            if fid >= 0:
                families = QFontDatabase.applicationFontFamilies(fid)
                if families:
                    setattr(_FontState, attr, families[0])


def _font(size: int, bold: bool = False, family: str = "falcon", weight: int = 0,
          italic: bool = False, underline: bool = False) -> QFont:
    if not _FontState.loaded:
        _load_fonts()
    f = QFont(getattr(_FontState, family, _FontState.falcon), size)
    f.setPixelSize(size)
    if weight:
        f.setWeight(QFont.Weight(weight))
    else:
        f.setBold(bold)
    f.setItalic(italic)
    f.setUnderline(underline)
    return f


# ── Pip drawing ───────────────────────────────────────────────────────────────

def draw_pips(
    painter: QPainter,
    pip_config: dict,
    count: int,
    stroke: str = "black",
    fill: str = "white",
    stroke_width: int = 3,
    slice_mode: str = "",
    struct_slice: bool = False,
) -> None:
    """Draw `count` hexagonal pips using the step layout from card_gen.js.

    slice_mode: "" (none), "single" (hardened armor), "double" (ferro-lamellor).
    struct_slice: draw a red diagonal line through each pip (reinforced structure).
    """
    if not pip_config or count <= 0:
        return

    steps = list(pip_config.get("steps", []))
    mask_fn = pip_config.get("mask", None)
    x = float(pip_config["start"]["x"])
    y = float(pip_config["start"]["y"])

    # Mask-based starting adjustment (shift first step when mask(count) is True)
    if mask_fn and count < len(steps) and mask_fn(count):
        steps.pop(0)

    c = PIP_RADIUS / 2
    u = PIP_RADIUS * math.sqrt(3) / 2

    drawn = 0
    for i, step in enumerate(steps):
        if drawn >= count:
            break
        x += round(PIP_X_MULT * step["x"])
        y += round(step["y"] * PIP_H)
        _draw_hex(painter, x, y, PIP_RADIUS, stroke, fill, stroke_width)

        # Reinforced structure: red diagonal line through hex
        if struct_slice:
            painter.setPen(QPen(_parse_color("red"), 2))
            painter.drawLine(
                QPointF(round(x - c), round(y - u)),
                QPointF(round(x + c), round(y + u)),
            )

        # Slice marks for special armor types
        if slice_mode == "single":
            # Hardened: diagonal line through hex
            painter.setPen(QPen(_parse_color("rgba(0, 0, 0, 0.65)"), 2))
            painter.drawLine(
                QPointF(round(x - c), round(y - u)),
                QPointF(round(x + c), round(y + u)),
            )
        elif slice_mode == "double":
            # Ferro-Lamellor: 5-line asterisk through hex
            painter.setPen(QPen(_parse_color("rgba(0, 0, 0, 0.5)"), 2))
            # Center to bottom-left vertex
            painter.drawLine(
                QPointF(round(x), round(y)),
                QPointF(round(x - c), round(y + u)),
            )
            # Center to bottom-right vertex
            painter.drawLine(
                QPointF(round(x), round(y)),
                QPointF(round(x + c), round(y + u)),
            )
            # Horizontal through center
            painter.drawLine(
                QPointF(round(x - u), round(y)),
                QPointF(round(x + u), round(y)),
            )
            # Center to top vertex
            painter.drawLine(
                QPointF(round(x), round(y)),
                QPointF(round(x), round(y - u)),
            )

        drawn += 1


def _parse_color(s: str) -> QColor:
    """Parse a color string, supporting rgba() for transparency."""
    if s.startswith("rgba("):
        parts = re.findall(r"[\d.]+", s)
        if len(parts) == 4:
            return QColor(
                int(parts[0]), int(parts[1]), int(parts[2]),
                int(float(parts[3]) * 255),
            )
    return QColor(s)


def _draw_hex(
    painter: QPainter,
    cx: float, cy: float, radius: float,
    stroke: str, fill: str, stroke_width: int,
    pointy: bool = False,
) -> None:
    """Draw a hexagon.

    Flat-top (pointy=False): vertices at multiples of 60° starting at 0°.
    Pointy-top (pointy=True): vertices at 30° + 60*i — point at bottom.
    """
    offset = 30 if pointy else 0
    points = QPolygonF([
        QPointF(cx + radius * math.cos(math.radians(60 * i + offset)),
                cy + radius * math.sin(math.radians(60 * i + offset)))
        for i in range(6)
    ])
    painter.setPen(QPen(_parse_color(stroke), stroke_width))
    painter.setBrush(QBrush(_parse_color(fill)))
    painter.drawPolygon(points)


def pip_colors(unit) -> tuple[str, str, int, str]:
    """Return (stroke, fill, stroke_width, slice_mode) for armor pips.

    slice_mode: "" (none), "single" (hardened), "double" (ferro-lamellor).
    """
    if unit.is_equipped_with("lasrefl"):
        return ("green",               "rgba(0,255,0,0.10)",   4, "")
    if unit.is_equipped_with("reactive"):
        return ("blue",                "rgba(0,255,255,0.15)", 4, "")
    if unit.is_equipped_with("ballreinf"):
        return ("rgba(127,63,0,1.00)", "rgba(127,63,0,0.15)", 4, "")
    if unit.is_equipped_with("stealth"):
        return ("rgba(41,0,85,1.00)",  "rgba(127,0,255,0.10)", 4, "")
    if unit.is_equipped_with("hardened"):
        return ("black", "white", 3, "single")
    if unit.is_equipped_with("ferolam"):
        return ("black", "white", 3, "double")
    return ("black", "white", 3, "")


# ── Text helpers ──────────────────────────────────────────────────────────────

def draw_text(
    painter: QPainter,
    x: int, y: int,
    text: str,
    size: int = FS_LARGE,
    bold: bool = False,
    align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft,
    width: int = 0,
    height: int = 0,
    color: str = "black",
    rotation: int = 0,
    family: str = "falcon",
    weight: int = 0,
    italic: bool = False,
    underline: bool = False,
) -> None:
    """Draw text at card canvas coordinates."""
    painter.save()
    painter.setPen(QColor(color))
    painter.setFont(_font(size, bold, family, weight, italic, underline))

    if rotation:
        painter.translate(x, y)
        painter.rotate(rotation)
        painter.translate(-x, -y)

    if width:
        h = height or size
        flags = int(Qt.AlignmentFlag.AlignVCenter) | int(align)
        for i, line in enumerate(text.split("\n")):
            line_rect = QRectF(x, y + i * size * 1.1, width, h * 1.5)
            painter.drawText(line_rect, flags, line)
    else:
        for i, line in enumerate(text.split("\n")):
            painter.drawText(QPointF(x, y + i * size * 1.2), line)

    painter.restore()


# ── Image loader ──────────────────────────────────────────────────────────────

def _load_image(name: str) -> Optional[QPixmap]:
    path = os.path.join(_IMG_DIR, name)
    if not os.path.exists(path):
        return None
    px = QPixmap(path)
    return px if not px.isNull() else None


# ── Base renderer ─────────────────────────────────────────────────────────────

class BaseCardRenderer:
    """
    Base class: load PNG images, provide painter utilities.
    Subclasses implement `render(unit, profile) -> QPixmap`.
    """

    #: Filename of the card background (override in subclass)
    BASE_IMAGE = "card-base.png"
    #: Filename of the unit silhouette (override in subclass)
    SILHOUETTE_IMAGE: Optional[str] = None

    def _build_canvas(self) -> tuple[QPixmap, QPainter]:
        """Return a blank 2100×1500 canvas with base card drawn."""
        canvas = QPixmap(CARD_W, CARD_H)
        canvas.fill(QColor("white"))
        painter = QPainter(canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)

        base = _load_image(self.BASE_IMAGE)
        if base:
            painter.drawPixmap(0, 0, CARD_W, CARD_H, base)

        if self.SILHOUETTE_IMAGE:
            sil = _load_image(self.SILHOUETTE_IMAGE)
            if sil:
                painter.drawPixmap(0, 0, CARD_W, CARD_H, sil)

        return canvas, painter

    def _draw_unit_header(
        self, painter: QPainter, unit,
        move_label: str = "Move:", sinks_label: str = "Sinks:",
        move_x_offset: int = 0, tmm_x_offset: int = 0,
        mass_str: str | None = None,
        move_str: str | None = None,
        tmm_str: str | None = None,
        sinks_val: int | None = None,
        heat_scale_max: int = 5,
        jump_heat_val: int | None = None,
    ) -> None:
        """Draw unit name, type, mass, move, TMM, sinks (left panel)."""
        # Unit name (Vegas font, all uppercase per card_gen.js)
        draw_text(painter, 60, 118,  unit.display_name, size=FS_XXLARGE+12, bold=True, family="vegas")
        # Unit data label
        draw_text(painter, 60, 190, "Unit Data",        size=FS_XLARGE, bold=True)
        # Type label + value
        draw_text(painter, 60,  250, "Type:",            size=FS_LARGE, bold=True)
        draw_text(painter, 190, 250, unit.unit_type_label, size=FS_LARGE)
        # Mass label + value
        draw_text(painter, 60,  300, "Mass:",            size=FS_LARGE, bold=True)
        if mass_str is not None:
            draw_text(painter, 190, 300, mass_str, size=FS_LARGE)
        else:
            draw_text(painter, 190, 300, f"{getattr(unit, 'tonnage', '?')} tons", size=FS_LARGE)
        # Move label + value
        draw_text(painter, 60,  365, move_label,         size=FS_LARGE, bold=True)
        draw_text(painter, 190 + move_x_offset, 365, move_str if move_str is not None else unit.destiny_move, size=FS_LARGE)
        # TMM label + value
        draw_text(painter, 60,  415, "TMM:",             size=FS_LARGE, bold=True)
        draw_text(painter, 190 + tmm_x_offset, 415, tmm_str if tmm_str is not None else unit.destiny_tmm, size=FS_LARGE)
        # Sinks (only for units with heat)
        effective_sinks = sinks_val if sinks_val is not None else unit.destiny_sinks
        if effective_sinks:
            draw_text(painter, 440, 365, sinks_label,          size=FS_LARGE, bold=True)
            draw_text(painter, 545, 365, str(effective_sinks), size=FS_LARGE)
            if jump_heat_val is not None and heat_scale_max != 5:
                draw_text(painter, 400, 415, "Jump Heat:", size=FS_LARGE, bold=True)
                draw_text(painter, 600, 415, str(jump_heat_val), size=FS_LARGE)
            # Heat Scale label (rotated)
            draw_text(painter, 650, 365, "Heat Scale", size=FS_LARGE, rotation=270)
            self._draw_heat_scale(painter, heat_scale_max)

    def _draw_heat_scale(self, painter: QPainter, heat_scale_max: int = 5) -> None:
        """Draw heat scale. Legacy 6-box layout for scale<=5; grid layout for scale>5."""
        if heat_scale_max <= 5:
            self._draw_heat_scale_legacy(painter)
        else:
            self._draw_heat_scale_grid(painter, heat_scale_max)

    def _draw_heat_scale_legacy(self, painter: QPainter) -> None:
        """Original 6-box vertical heat scale for heat_scale_max <= 5."""
        boxes = [
            (707, 181, "5", "Auto Shutdown"),
            (707, 226, "4", "Ammo Explode 8+"),
            (707, 271, "3", "Shutdown 8+"),
            (707, 316, "2", "+1 Rng Attk"),
            (707, 361, "1", "-2 MP / -1 TMM"),
            (707, 406, "0", "No Effect"),
        ]
        for i, (bx, by, label, desc) in enumerate(boxes):
            if i == 0:
                fill = "#000000"
            elif i == len(boxes) - 1:
                fill = "#FFFFFF"
            else:
                idx = max(0, min(len(heat_colors) - 1, round(len(heat_colors) * (1 - (i + 1) / len(boxes)))))
                fill = heat_colors[idx]
            painter.setPen(QPen(QColor("black"), 4))
            painter.setBrush(QBrush(QColor(fill)))
            painter.drawRoundedRect(int(bx - 13), int(by - 33), 44, 44, 1, 1)
            draw_text(painter, bx, by, label, size=FS_MEDIUM, bold=True,
                      color="white" if i == 0 else "black")
            draw_text(painter, bx + 50, by, desc, size=FS_MEDIUM)

    def _draw_heat_scale_grid(self, painter: QPainter, heat_scale_max: int) -> None:
        """Grid layout for scale > 5: always 6 rows, level 0 centered at bottom."""
        ROWS     = 6
        CW       = 44
        CH       = 44
        GRID_Y   = 148
        REGION_X = 665
        REGION_W = 220         # 5 * CW — fixed horizontal region
        LABEL_X  = REGION_X + REGION_W + 14  # 904

        include_zero = heat_scale_max < 30

        # Build row layout bottom-first; greedy ceil distribution for upper rows
        if include_zero:
            row_levels_list: list[list[int]] = [[0]]
            remaining = list(range(1, heat_scale_max + 1))
            upper_rows = ROWS - 1
        else:
            row_levels_list = []
            remaining = list(range(1, heat_scale_max + 1))
            upper_rows = ROWS

        for r in range(upper_rows):
            rows_left = upper_rows - r
            cells = math.ceil(len(remaining) / rows_left)
            row_levels_list.append(remaining[:cells])
            remaining = remaining[cells:]

        thresh_labels: dict[int, str] = {
            round(i * heat_scale_max / 5): lbl
            for i, lbl in [
                (1, "-2MP / -1TMM"),
                (2, "+1 Rng Attk"),
                (3, "Shutdown 8+"),
                (4, "Ammo Explode 8+"),
                (5, "Auto Shutdown"),
            ]
        }

        for row_idx, row_lvls in enumerate(row_levels_list):
            display_row = ROWS - 1 - row_idx   # 0=top, ROWS-1=bottom
            y = GRID_Y + display_row * CH

            row_width = len(row_lvls) * CW
            x_start = REGION_X + (REGION_W - row_width) // 2

            row_thresh_lbl: str | None = None
            is_zero_row = row_lvls == [0]

            for col, lvl in enumerate(row_lvls):
                x = x_start + col * CW

                idx   = round(lvl / max(1, heat_scale_max) * 29)
                color = heat_colors[max(0, min(29, idx))]
                is_thresh = lvl in thresh_labels
                if is_thresh:
                    row_thresh_lbl = thresh_labels[lvl]

                painter.setPen(QPen(QColor("black"), 4))
                painter.setBrush(QBrush(QColor(color)))
                painter.drawRoundedRect(x, y, CW, CH, 1, 1)

                qc  = QColor(color)
                lum = 0.299 * qc.redF() + 0.587 * qc.greenF() + 0.114 * qc.blueF()
                tc  = "white" if lum < 0.55 else "black"

                draw_text(painter, x, y + 1, str(lvl), size=FS_MEDIUM, bold=True,
                          align=Qt.AlignmentFlag.AlignHCenter, width=CW, color=tc)
                if is_thresh:
                    draw_text(painter, x + 26, y + 26, "*", size=FS_MEDIUM, bold=True, color=tc)

            if row_thresh_lbl:
                draw_text(painter, LABEL_X, y + (CH + 20) // 2, f"*{row_thresh_lbl}", size=FS_MEDIUM)
            elif is_zero_row:
                draw_text(painter, LABEL_X, y + (CH + 20) // 2, "No Effect", size=FS_MEDIUM)

    def _draw_weapons_table(
        self, painter: QPainter, resolved_weapons: list, has_heat: bool = True
    ) -> None:
        """
        Draw the weapons table in the left panel.
        resolved_weapons: list of dicts with keys:
          name, damage, heat, location, rangePB, rangeS, rangeM, rangeL, rangeX
        """
        # Column x positions (from card_gen.js)
        COL_NAME  = 68
        COL_DMG   = 420
        COL_HT    = 635
        COL_LOC   = 690  # adjusted if no heat
        COL_PB    = 830
        COL_S     = 890
        COL_M     = 950
        COL_L     = 1010
        COL_X     = 1070

        Y_START   = 515  # Ye.y
        ROW_H     = 60   # ya

        # Header row
        draw_text(painter, 60, 490, "WEAPONS", size=FS_XLARGE, bold=True)
        header_y = Y_START - ROW_H  # Ye.y - ya = 445
        self._draw_weapon_row_header(painter, header_y, has_heat)

        # Weapon rows — None entries are empty slots (skip rendering)
        for i, w in enumerate(resolved_weapons):
            if w is None:
                continue
            y = Y_START + i * ROW_H
            draw_text(painter, COL_NAME, y-20, w.get("name", ""), size=FS_MEDIUM,
                      width=360, height=ROW_H)
            self._draw_centered(painter, COL_DMG, y, w.get("damage", ""), 220, FS_MEDIUM)
            if has_heat:
                self._draw_centered(painter, COL_HT, y, str(w.get("heat", "")), 50, FS_MEDIUM)
            loc_x = COL_LOC if has_heat else COL_LOC - 40
            self._draw_centered(painter, loc_x, y, w.get("location", ""), 140, FS_MEDIUM)
            self._draw_centered(painter, COL_PB, y, w.get("rangePB", "—"), 50, FS_MEDIUM)
            self._draw_centered(painter, COL_S,  y, w.get("rangeS",  "—"), 50, FS_MEDIUM)
            self._draw_centered(painter, COL_M,  y, w.get("rangeM",  "—"), 50, FS_MEDIUM)
            self._draw_centered(painter, COL_L,  y, w.get("rangeL",  "—"), 50, FS_MEDIUM)
            self._draw_centered(painter, COL_X,  y, w.get("rangeX",  "—"), 50, FS_MEDIUM)

    def _draw_weapon_row_header(
        self, painter: QPainter, y: int, has_heat: bool
    ) -> None:
        COL_DMG = 420; COL_HT = 635; COL_LOC = 690
        COL_PB = 830; COL_S = 890; COL_M = 950; COL_L = 1010; COL_X = 1070
        self._draw_centered(painter, COL_DMG, y, "Dmg", 220, FS_LARGE, True)
        if has_heat:
            self._draw_centered(painter, COL_HT, y, "Ht", 50, FS_LARGE, True)
        loc_x = COL_LOC if has_heat else COL_LOC - 40
        self._draw_centered(painter, loc_x, y, "Loc", 140, FS_LARGE, True)
        self._draw_centered(painter, COL_PB, y, "PB", 50, FS_LARGE, True)
        self._draw_centered(painter, COL_S,  y, "S",  50, FS_LARGE, True)
        self._draw_centered(painter, COL_M,  y, "M",  50, FS_LARGE, True)
        self._draw_centered(painter, COL_L,  y, "L",  50, FS_LARGE, True)
        self._draw_centered(painter, COL_X,  y, "X",  50, FS_LARGE, True)

    def _draw_x_mark(self, painter: QPainter, x: int, y: int) -> None:
        """Draw a 30×30 X mark at (x, y) — used for anti-mech checkboxes."""
        painter.setPen(QPen(QColor("black"), 3))
        painter.drawLine(x, y, x + 30, y + 30)
        painter.drawLine(x + 30, y, x, y + 30)

    def _draw_centered(
        self, painter: QPainter, x: int, y: int, text: str, width: int, size: int,
        bold: bool = False, color: str = "black",
    ) -> None:
        rect = QRectF(x, y, width, 60)
        painter.setFont(_font(size, bold=bold))
        painter.setPen(QColor(color))
        painter.drawText(rect,
                         int(Qt.AlignmentFlag.AlignHCenter) |
                         int(Qt.AlignmentFlag.AlignVCenter),
                         str(text))

    def _draw_equipment_items(
        self, painter: QPainter, items: list[dict] | None,
        show_pips: bool = True,
    ) -> None:
        """Draw equipment list with optional inline ammo pips.

        items: list of {"label": str, "is_ammo": bool, "shots": int, ...}
        show_pips: if False, ammo shows only the [N] count, no hex pips.
        Items flow left-to-right, wrapping when they exceed max width.
        Ammo items draw hex pips inline after the label, then wrap to next line.
        """
        draw_text(painter, 60, 1165, "Equipment:", size=FS_LARGE, bold=True)
        if not items:
            return

        painter.save()
        painter.setFont(_font(FS_LARGE - 4))
        painter.setPen(QColor("black"))
        painter.setBrush(Qt.BrushStyle.NoBrush)

        fm = painter.fontMetrics()
        line_h = int(fm.height() * 1.3)
        start_x = EQUIPMENT_START_X
        max_x = EQUIPMENT_START_X + EQUIPMENT_MAX_W
        x = start_x + EQUIPMENT_PAD_LEFT
        y = 1130          # top of current line
        next_y = y + line_h + 4  # where next line would start

        for i, item in enumerate(items):
            label = item["label"]
            is_ammo = item.get("is_ammo", False)
            shots = item.get("shots", 0) if is_ammo else 0
            is_last = (i == len(items) - 1)

            if y > 1450:
                break

            # Comma after each item except the last
            comma = ", " if not is_last else ""
            comma_w = fm.horizontalAdvance(comma) if comma else 0

            label_w = fm.horizontalAdvance(label)

            # Pip dimensions for ammo items (estimated for wrap check)
            pip_w = 0
            pip_total_rows = 1
            if is_ammo and shots > 0 and shots <= AMMO_MAX_PIP_SHOTS:
                per_row_max = AMMO_PIPS_PER_ROW
                min_rows = 2 if shots > AMMO_PIPS_MIN_ROWS else 1
                pip_total_rows = max(min_rows, math.ceil(shots / per_row_max))
                base = shots // pip_total_rows
                extra = shots % pip_total_rows
                max_row = base + (1 if extra > 0 else 0)
                pip_w = int(max_row * AMMO_PIP_X_MULT + 2 * AMMO_PIP_RADIUS)

            total_w = label_w + comma_w + (6 + pip_w if pip_w else 0)

            # Wrap to next line if needed
            if x > start_x and x + total_w > max_x:
                x = start_x
                y = next_y
                next_y = y + line_h + 4

            # Reset pen
            painter.setPen(QColor("black"))

            # Draw label
            painter.drawText(QPointF(x, y + fm.ascent()), label)
            x += label_w

            # Draw ammo pips (if enabled)
            if is_ammo and shots > 0 and shots <= AMMO_MAX_PIP_SHOTS and show_pips:
                x += 6
                pip_y = y + (line_h - pip_total_rows * AMMO_PIP_H) / 2
                actual_rows, actual_w = self._draw_ammo_pips_inline(
                    painter, x, pip_y, shots, max_x - x,
                    fm_height=fm.height(),
                )
                x += actual_w

            # Draw trailing comma
            if comma:
                painter.drawText(QPointF(x, y + fm.ascent()), comma)
                x += comma_w

        painter.restore()

    def _draw_ammo_pips_inline(
        self, painter: QPainter, start_x: int, y: int,
        count: int, max_width: int, fm_height: int = 28,
    ) -> tuple[int, int]:
        """Draw ammo hex pips inline, wrapping to additional rows per config.

        Returns (total_rows, first_row_width) — the pixel width consumed by
        the first row so the caller can position subsequent items correctly.
        """
        if count <= 0 or count > AMMO_MAX_PIP_SHOTS:
            return 0, 0

        radius = AMMO_PIP_RADIUS
        spacing_x = AMMO_PIP_X_MULT
        spacing_y = AMMO_PIP_H
        per_row_max = AMMO_PIPS_PER_ROW
        min_rows = 2 if count > AMMO_PIPS_MIN_ROWS else 1
        total_rows = max(min_rows, math.ceil(count / per_row_max))

        # Distribute evenly across rows
        base = count // total_rows
        extra = count % total_rows
        row_sizes = [base + 1] * extra + [base] * (total_rows - extra)

        stroke = "#555555"
        fill = "white"
        stroke_w = 1.5

        pip_y_offset = spacing_y * 0.15

        first_row_width = 0
        for row in range(total_rows):
            row_y = y + pip_y_offset + row * spacing_y
            row_offset = (spacing_x / 2) if row % 2 == 1 else 0
            row_x = start_x + row_offset
            row_count = row_sizes[row]

            for col in range(row_count):
                cx = row_x + col * spacing_x + radius
                cy = row_y
                _draw_hex(painter, cx, cy, radius, stroke, fill, stroke_w,
                          pointy=True)

            # Track width of first row
            if row == 0:
                first_row_width = int(
                    row_offset + row_count * spacing_x + 2 * radius
                )

        return total_rows, first_row_width

    def _draw_zone_label(
        self, painter: QPainter, x: int, y: int, text: str
    ) -> None:
        """Draw a zone label (multi-line, centered, bold)."""
        painter.setFont(_font(FS_MEDIUM, bold=True))
        painter.setPen(QColor("black"))
        lines = text.split("\n")
        line_h = FS_MEDIUM * 1.2
        total_h = len(lines) * line_h
        for i, line in enumerate(lines):
            ty = y - total_h / 2 + i * line_h + line_h / 2
            rect = QRectF(x - 150, ty, 300, line_h)
            painter.drawText(rect,
                             int(Qt.AlignmentFlag.AlignHCenter) |
                             int(Qt.AlignmentFlag.AlignVCenter),
                             line)


    def _draw_condition_monitor(self, painter: QPainter) -> None:
        """Draw the Condition Monitor section at bottom of card."""
        # Header label — centered over the six condition boxes
        self._draw_centered(painter, 665, 1322, "Condition Monitor", 400, FS_MEDIUM, bold=True)
        # Condition threshold labels (each centered over its pre-drawn box)
        thresholds = [
            (491, "3+",  "black"),
            (561, "5+",  "black"),
            (631, "7+",  "black"),
            (701, "9+",  "black"),
            (768, "11+", "black"),
            (840, "KIA", "white"),
        ]
        for x, label, color in thresholds:
            self._draw_centered(painter, x, 1368, label, 400, FS_MEDIUM, color=color)

    def _draw_engine_gyro_labels(self, painter: QPainter) -> None:
        """Draw Engine and Gyro section labels (BattleMech only)."""
        self._draw_centered(painter, 40,  1322, "Engine", 400, FS_MEDIUM, bold=True)
        self._draw_centered(painter, 270, 1322, "Gyro",   400, FS_MEDIUM, bold=True)
