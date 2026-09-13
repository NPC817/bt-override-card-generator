"""
DropShip card renderer.

Mirrors AeroCardRenderer (aero_renderer.py) with per-subtype silhouettes and
zone labels (Wing vs Side). Pip layouts copied from _AERO_PIPS as a starting
point; dropship armor values (45-55 pips) exceed the aero step lists, so pips
auto-condense: full-size pips while count fits the layout, switching to a 2x2
grid of half-size pips per step (quadrupling capacity) once it doesn't.

No reference cards exist — pip coordinates are provisional values to be
tuned manually.
"""
from __future__ import annotations

import logging
import math

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPixmap

from .card_renderer import (
    BaseCardRenderer, draw_pips, draw_text, pip_colors,
    _draw_hex, PIP_H, PIP_RADIUS, PIP_X_MULT,
    PIP_DENSE_RADIUS, PIP_DENSE_QUADS,
    FS_LARGE, FS_MEDIUM,
)
from ..models.dropship import Dropship
from ..settings.profile import ConversionProfile
from ..engine.tic_grouper import DROPSHIP_TIC_SLOTS

_SILHOUETTES = {
    Dropship.AERODYNE: "dropship-aero.png",
    Dropship.SPHEROID: "dropship-shpere.png",   # intentional typo in filename
}

# Zone label positions — same base positions as _AERO_LABELS (aero_renderer.py).
_DROPSHIP_LABELS = {
    Dropship.SPHEROID: {
        "N":  {"x": 1500, "y": 200,  "text": "Nose\n(6,7,8)"},
        "LS": {"x": 1225, "y": 470,  "text": "Left\nSide\n(9,10,11)"},
        "RS": {"x": 1975, "y": 470,  "text": "Right\nSide\n(3,4,5)"},
        "A":  {"x": 1605, "y": 1415, "text": "Aft\n(2,12)"},
    },
    Dropship.AERODYNE: {
        "N":  {"x": 1300, "y": 300,  "text": "Nose\n(6,7,8)"},
        "LW": {"x": 1250, "y": 770,  "text": "Left\nWing\n(9,10,11)"},
        "RW": {"x": 1975, "y": 770,  "text": "Right\nWing\n(3,4,5)"},
        "A":  {"x": 1610, "y": 1350, "text": "Aft\n(2,12)"},
    },
}


# Debug: draw a pink hex at the cursor's end position after each zone's armor
# pips — the slot where the next pip would go. Flip to False to turn off.
_DEBUG_ARMOR_PIP = False


def _pip_cursor_pos(
    pip_cfg: dict, count: int, condense: bool = True
) -> tuple[float, float]:
    """Walk `count` pips exactly like draw_pips and return the cursor's end
    position — the slot where the next pip would be drawn."""
    steps = list(pip_cfg.get("steps", []))
    mask_fn = pip_cfg.get("mask", None)
    condensed = condense and count > len(steps)
    slots = math.ceil(count / 4) if condensed else count
    if mask_fn and slots < len(steps) and mask_fn(slots):
        steps.pop(0)
    x = float(pip_cfg["start"]["x"])
    y = float(pip_cfg["start"]["y"])
    for i, step in enumerate(steps):
        if i >= slots:
            break
        x += round(PIP_X_MULT * step["x"])
        y += round(step["y"] * PIP_H)
    # Offset of the last drawn quadrant within the final slot (row-major 2x2).
    if condensed:
        ox, oy = PIP_DENSE_QUADS[(count - 1) % 4]
        x += ox
        y += oy
    return x, y


# Pip layouts copied from _AERO_PIPS (aero_renderer.py) as starting values —
# tune manually for the larger dropship armor counts.
_DROPSHIP_PIPS = {
    Dropship.SPHEROID: {
        "FU": {
            "structure": {
                "start": {"x": 1605, "y": 805},
                "steps": [
                    {"x": 0, "y": 0},  {"x": 2, "y": 0},  {"x": -4, "y": 0},
                    {"x": 2, "y": -1}, {"x": 2, "y": 0},  {"x": -4, "y": 0},
                    {"x": 2, "y": 2},  {"x": 2, "y": 0},  {"x": -4, "y": 0},
                ],
            },
        },
        "N": {
            "armor": {
                "start": {"x": 1605, "y": 520},
                "steps": [
                    {"x": 0,   "y": -0.5}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": 1},    {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},    {"x": -20, "y": 0},
                    {"x": 10,  "y": -2},   {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,   "y": 3},    {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},    {"x": -20, "y": 0},
                    {"x": 10,  "y": -4},   {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,   "y": 5},    {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},    {"x": -20, "y": 0},  {"x": 22,  "y": 0},
                    {"x": -24, "y": 0},
                    {"x": 12,  "y": -6},   {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,   "y": 7},    {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},    {"x": -20, "y": 0},  {"x": 22,  "y": 0},
                    {"x": -24, "y": 0},
                    {"x": 12,  "y": -8},   {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},
                    {"x": 4,   "y": 9},    {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},    {"x": -20, "y": 0},  {"x": 22,  "y": 0},
                    {"x": -24, "y": 0},
                    {"x": 12,  "y": -10},  {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 2,   "y": 11},   {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},    {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},    {"x": -20, "y": 0},  {"x": 22,  "y": 0},
                    {"x": -24, "y": 0},
                    {"x": 12,  "y": -12},
                    {"x": 0,   "y": 13},   {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},    {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},
                ],
            },
        },
        "LS": {
            "armor": {
                "start": {"x": 1457, "y": 990},
                "steps": [
                    {"x": 0,   "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},
                    {"x": 12,  "y": -1},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": 2},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": -3},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": 4},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": -5},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": 6},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": -7},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": 8},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": -9},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": 10},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},
                    {"x": 8,   "y": -11},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 10,  "y": 12},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},
                    {"x": 8,   "y": -13},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},
                    {"x": 6,   "y": 14},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},
                    {"x": 8,   "y": -15},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},    {"x": -2,  "y": 0},
                    {"x": 6,   "y": 16},   {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": 6,   "y": -17},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0},
                    {"x": 4,   "y": 18},   {"x": -2,  "y": 0},
                ],
            },
        },
        "RS": {
            "armor": {
                "start": {"x": 1752, "y": 990},
                "steps": [
                    {"x": 0,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},
                    {"x": -12, "y": -1},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": 2},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": -3},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": 4},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": -5},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": 6},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": -7},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": 8},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": -9},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": 10},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},
                    {"x": -8,  "y": -11},  {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -10, "y": 12},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},
                    {"x": -8,  "y": -13},  {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},
                    {"x": -6,  "y": 14},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},
                    {"x": -8,  "y": -15},  {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},    {"x": 2,   "y": 0},
                    {"x": -6,  "y": 16},   {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": -6,  "y": -17},  {"x": 2,   "y": 0},   {"x": 2,   "y": 0},
                    {"x": 2,   "y": 0},
                    {"x": -4,  "y": 18},   {"x": 2,   "y": 0},
                ],
            },
        },
        "A": {
            "armor": {
                "start": {"x": 1605, "y": 1105},
                "steps": [
                    {"x": 0,  "y": 0},    {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -1},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 2},    {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -3},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 4},    {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},   {"x": 10, "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,  "y": -5},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 6},    {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},   {"x": 10, "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,  "y": -7},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 8},    {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},   {"x": 10, "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,  "y": -9},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 10},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},   {"x": 10, "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,  "y": -11},  {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 12},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},   {"x": 10, "y": 0},
                    {"x": -12, "y": 0},
                    {"x": 6,  "y": -13},  {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 14},   {"x": 2,  "y": 0},   {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},   {"x": 10, "y": 0},
                    {"x": -12, "y": 0},
                ],
            },
        },
    },
    Dropship.AERODYNE: {
        "FU": {
            "structure": {
                "start": {"x": 1610, "y": 752},
                "steps": [
                    {"x": 0, "y": 0},  {"x": 2, "y": 0},  {"x": -4, "y": 0},
                    {"x": 2, "y": -1}, {"x": 2, "y": 0},  {"x": -4, "y": 0},
                    {"x": 2, "y": 2},  {"x": 2, "y": 0},  {"x": -4, "y": 0},
                ],
            },
        },
        "N": {
            "armor": {
                "start": {"x": 1610, "y": 485},
                "steps": [
                    {"x": 0,   "y": 0},  {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": -1}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": 2},  {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": -3}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": 4},  {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": -5}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": 6},  {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},  {"x": -20, "y": 0},
                    {"x": 10,  "y": -7}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 8,   "y": 8},  {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},  {"x": 10,  "y": 0},
                    {"x": -12, "y": 0},  {"x": 14,  "y": 0},  {"x": -16, "y": 0},
                    {"x": 18,  "y": 0},  {"x": -20, "y": 0},
                    {"x": 10,  "y": -9}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},
                    {"x": 4,   "y": 10}, {"x": 2,   "y": 0},  {"x": -4,  "y": 0},
                    {"x": 6,   "y": 0},  {"x": -8,  "y": 0},
                ],
            },
        },
        "LW": {
            "armor": {
                "start": {"x": 1470, "y": 950},
                "steps": [
                    {"x": 0,   "y": 0},  {"x": -2,   "y": 0}, {"x": 2,  "y": -1},
                    {"x": -2,   "y": 0},  {"x": 2,   "y": -1}, {"x": -2,  "y": 0},
                    {"x": 2,   "y": 3},  {"x": -2,   "y": 0}, {"x": -2,  "y": 0},
                    {"x": 4,   "y": -4},  {"x": -2,   "y": 0}, {"x": 2,  "y": 5},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": 4,  "y": -6},
                    {"x": -2,   "y": 0},  {"x": 2,   "y": 7}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": 6,  "y": -8},
                    {"x": -2,   "y": 0},  {"x": 2,   "y": 9}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": 6,  "y": -10},
                    {"x": -2,   "y": 0},  {"x": 2,   "y": 11}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": -2,  "y": 0},
                    {"x": 8,   "y": -12},  {"x": -2,   "y": 0}, {"x": 2,  "y": 13},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": 8,   "y": -14}, {"x": -2,  "y": 0},
                    {"x": 2,   "y": 15},  {"x": -2,   "y": 0}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": 8,  "y": -16},
                    {"x": -2,   "y": 0},  {"x": 2,   "y": 17}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": -2,  "y": 0},
                    {"x": 8,   "y": 1},  {"x": -2,   "y": 0}, {"x": -2,  "y": 0},
                    {"x": -2,   "y": 0},  {"x": -2,   "y": 0}, {"x": 8,   "y": 1},
                    {"x": -2,   "y": 0},  {"x": -2,  "y": 0},  {"x": -2,  "y": 0},
                    {"x": -2,  "y": 0}
                ],
            },
        },
        "RW": {
            "armor": {
                "start": {"x": 1750, "y": 950},
                "steps": [
                    {"x": 0,  "y": 0},  {"x": 2,  "y": 0},  {"x": -2, "y": -1},
                    {"x": 2,  "y": 0},  {"x": -2, "y": -1}, {"x": 2,  "y": 0},
                    {"x": -2, "y": 3},  {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": -4, "y": -4}, {"x": 2,  "y": 0},  {"x": -2, "y": 5},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": -4, "y": -6},
                    {"x": 2,  "y": 0},  {"x": -2, "y": 7},  {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": -6, "y": -8},
                    {"x": 2,  "y": 0},  {"x": -2, "y": 9},  {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": -6, "y": -10},
                    {"x": 2,  "y": 0},  {"x": -2, "y": 11}, {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": -8, "y": -12}, {"x": 2,  "y": 0},  {"x": -2, "y": 13},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": -8, "y": -14}, {"x": 2,  "y": 0},
                    {"x": -2, "y": 15}, {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": -8, "y": -16},
                    {"x": 2,  "y": 0},  {"x": -2, "y": 17}, {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": -8, "y": 1},  {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": -8, "y": 1},
                    {"x": 2,  "y": 0},  {"x": 2,  "y": 0},  {"x": 2,  "y": 0},
                    {"x": 2,  "y": 0}
                ],
            },
        },
        "A": {
            "armor": {
                "start": {"x": 1610, "y": 1055},
                "steps": [
                    {"x": 0,  "y": -0.5}, {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 1},    {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -2},   {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 3},    {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -4},   {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 5},    {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -6},   {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 7},    {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -8},   {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 9},    {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -10},  {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 11},   {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": -12},  {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                    {"x": 4,  "y": 13},   {"x": 2,  "y": 0}, {"x": -4, "y": 0},
                    {"x": 6,  "y": 0},    {"x": -8, "y": 0},
                ],
            },
        },
    },
}


class DropshipCardRenderer(BaseCardRenderer):
    """Renders a DropShip card to a 2100×1500 QPixmap."""

    BASE_IMAGE = "card-base-dropship.png"
    # Until card-base-dropship.png is added to images/, fall back to the
    # standard base so dropship cards stay renderable.
    BASE_IMAGE_FALLBACK = "card-base.png"
    # SILHOUETTE_IMAGE is set per-unit in render() before _build_canvas().

    def render(
        self,
        unit: Dropship,
        profile: ConversionProfile,
        weapons_rows: list[dict] | None = None,
        equipment_items: list[dict] | None = None,
    ) -> QPixmap:
        self.SILHOUETTE_IMAGE = _SILHOUETTES.get(
            unit.motive_type, _SILHOUETTES[Dropship.SPHEROID])
        canvas, painter = self._build_canvas()

        # Header — "Thrust:" instead of "Move:", +15 x-offsets per card_gen.js
        self._draw_unit_header(
            painter, unit,
            move_label="Thrust:", move_x_offset=15, tmm_x_offset=15,
            sinks_val=None,
            heat_scale_max=profile.heat_scale_max,
            bv_val=unit.battle_value if profile.show_bv else 0,
        )

        # Gunnery / Piloting labels
        draw_text(painter, 1155, 45, "Gunnery", size=FS_MEDIUM+4, bold=True,
                  width=180, align=Qt.AlignmentFlag.AlignCenter)
        draw_text(painter, 1300, 45, "Piloting", size=FS_MEDIUM+4, bold=True,
                  width=180, align=Qt.AlignmentFlag.AlignCenter)

        # DThr (damage threshold)
        draw_text(painter, 440, 415, "DThr:", size=FS_LARGE, bold=True)
        draw_text(painter, 545, 415, str(unit.dthr), size=FS_LARGE)

        # Weapons table — dropships always show heat. 20 half-height rows
        # with smaller font keep the same 515–1115 band as 10 full rows.
        rows = list(weapons_rows or [])[:DROPSHIP_TIC_SLOTS]
        while len(rows) < DROPSHIP_TIC_SLOTS:
            rows.append(None)
        self._draw_weapons_table(painter, rows, has_heat=True,
                                 row_height=30, font_size=22)

        # Equipment — dropship compact: ~25% smaller text, label included
        self._draw_equipment_items(
            painter, equipment_items,
            show_pips=profile.show_tracking_pips,
            max_pip_shots=profile.ammo_max_pips,
            header_size=round(FS_LARGE * 0.75),
            item_size=round((FS_LARGE - 4) * 0.75))

        # Right panel: zone labels + pips
        self._draw_dropship_zones(painter, unit, profile)

        # Bottom section: condition monitor
        self._draw_condition_monitor(painter)

        painter.end()
        return canvas

    def _draw_dropship_zones(
        self, painter: QPainter, unit: Dropship, profile: ConversionProfile
    ) -> None:
        div = profile.aero_armor_divisor
        stroke, fill, sw, slice_mode = pip_colors(unit)
        labels = _DROPSHIP_LABELS.get(unit.motive_type,
                                      _DROPSHIP_LABELS[Dropship.SPHEROID])
        pips = _DROPSHIP_PIPS.get(unit.motive_type,
                                  _DROPSHIP_PIPS[Dropship.SPHEROID])

        # Two-pass render: pips first so zone labels appear on top.
        # Auto-condense: full-size pips while count fits the steps, 2x2
        # half-size quads past capacity — cap is 4 * len(steps). Note: mask
        # zones pop their first step when the mask fires, so true condensed
        # capacity there is 4 * (len(steps) - 1) — a 4-pip shortfall at
        # extreme counts, acceptable for provisional layouts.
        for zone in labels:
            armor_pips = pips.get(zone, {}).get("armor")
            if armor_pips and unit.armor.get(zone, 0) > 0:
                a_val = unit.destiny_armor(zone, div)
                cap = 4 * len(armor_pips["steps"])
                if a_val > cap:
                    logging.warning(
                        "Dropship zone %s armor pips %d exceed layout %d — clamping",
                        zone, a_val, cap)
                    a_val = cap
                draw_pips(painter, armor_pips, a_val, stroke, fill, sw,
                          slice_mode, condense=True)
                if _DEBUG_ARMOR_PIP:
                    ex, ey = _pip_cursor_pos(armor_pips, a_val)
                    logging.info(
                        "DEBUG zone %s: cursor at (%d, %d) after %d pips",
                        zone, round(ex), round(ey), a_val)
                    r = (PIP_DENSE_RADIUS if a_val > len(armor_pips["steps"])
                         else PIP_RADIUS)
                    _draw_hex(painter, ex, ey, r, "pink", "pink", 2)

        # Fuselage structure (FU) — only structure on dropship card
        fu_pips = pips.get("FU", {}).get("structure")
        if fu_pips:
            s_val = unit.destiny_structure()
            cap = 4 * len(fu_pips["steps"])
            if s_val > cap:
                logging.warning(
                    "Dropship structure pips %d exceed layout %d — clamping",
                    s_val, cap)
                s_val = cap
            draw_pips(painter, fu_pips, s_val, "red", "white", 3,
                      struct_slice=unit.is_equipped_with("reinforced"),
                      condense=True)

        # Labels on top
        for zone, ldata in labels.items():
            self._draw_zone_label(painter, ldata["x"], ldata["y"], ldata["text"])
