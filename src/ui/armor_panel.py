"""
Armor panel: diagram-style armor editing per unit type.
Stacked layouts for biped, quad, vehicle (no turret), vehicle (turret),
VTOL, fighter, and simple (BA/infantry).
"""
from __future__ import annotations

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QFormLayout, QGridLayout, QLabel, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget,
)


class ArmorPanel(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._building = False
        self._spinboxes: dict[str, dict[str, QSpinBox]] = {}
        self._layout_index: dict[str, int] = {}
        self._layout_keys: dict[str, list[str]] = {}
        self._current_layout: str = "biped"
        self._build_ui()

    def _build_ui(self) -> None:
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        self._stack = QStackedWidget()
        outer.addWidget(self._stack)

        # Build all layout variants
        self._build_biped()
        self._build_quad()
        self._build_vehicle_no_turret()
        self._build_vehicle_turret()
        self._build_vtol()
        self._build_fighter()
        self._build_simple()

    # ── Biped BattleMech ────────────────────────────────────────────────────────

    def _build_biped(self) -> None:
        self._spinboxes["biped"] = {}
        page = QWidget()
        grid = QGridLayout(page)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(4)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        front_locs = [
            (0, "HD", 1, 300),
            (2, "LA", 0, 300), (2, "RA", 2, 300),
            (4, "LT", 0, 300), (4, "CT", 1, 300), (4, "RT", 2, 300),
            (6, "LL", 0, 300), (6, "RL", 2, 300),
        ]
        rear_locs = [
            (9, "LTR", 0, 100), (9, "CTR", 1, 100), (9, "RTR", 2, 100),
        ]

        for row, key, col, rng in front_locs:
            self._add_loc_cell("biped", grid, key, row, col, 0, rng)

        # Rear separator
        sep = QLabel("--- Rear ---")
        sep.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(sep, 8, 0, 1, 3)

        for row, key, col, rng in rear_locs:
            self._add_loc_cell("biped", grid, key, row, col, 0, rng)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["biped"] = idx
        self._layout_keys["biped"] = ["HD", "LA", "RA", "LT", "CT", "RT", "LL", "RL",
                                       "LTR", "CTR", "RTR"]

    # ── Quad BattleMech ─────────────────────────────────────────────────────────

    def _build_quad(self) -> None:
        self._spinboxes["quad"] = {}
        page = QWidget()
        grid = QGridLayout(page)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(4)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        front_locs = [
            (0, "HD", 0, 300),
            (2, "FLL", 0, 300), (2, "FRL", 2, 300),
            (4, "LT", 0, 300),  (4, "CT", 1, 300),  (4, "RT", 2, 300),
            (6, "RLL", 0, 300), (6, "RRL", 2, 300),
        ]
        rear_locs = [
            (9, "LTR", 0, 100), (9, "CTR", 1, 100), (9, "RTR", 2, 100),
        ]

        for row, key, col, rng in front_locs:
            self._add_loc_cell("quad", grid, key, row, col, 0, rng)

        sep = QLabel("--- Rear ---")
        sep.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(sep, 8, 0, 1, 3)

        for row, key, col, rng in rear_locs:
            self._add_loc_cell("quad", grid, key, row, col, 0, rng)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["quad"] = idx
        self._layout_keys["quad"] = ["HD", "FLL", "FRL", "LT", "CT", "RT", "RLL", "RRL",
                                      "LTR", "CTR", "RTR"]

    # ── Vehicle (no turret) ─────────────────────────────────────────────────────

    def _build_vehicle_no_turret(self) -> None:
        self._spinboxes["vehicle_no_turret"] = {}
        page = QWidget()
        grid = QGridLayout(page)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(4)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        locs = [
            (0, "FR", 1, 500), (2, "LS", 0, 500), (2, "RS", 3, 500),
            (4, "RR", 1, 500),
        ]

        for row, key, col, rng in locs:
            self._add_loc_cell("vehicle_no_turret", grid, key, row, col, 0, rng)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["vehicle_no_turret"] = idx
        self._layout_keys["vehicle_no_turret"] = ["FR", "LS", "RS", "RR"]

    # ── Vehicle (with turret) ───────────────────────────────────────────────────

    def _build_vehicle_turret(self) -> None:
        self._spinboxes["vehicle_turret"] = {}
        page = QWidget()
        grid = QGridLayout(page)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(4)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        locs = [
            (0, "FR", 1, 500), (2, "LS", 0, 500), (2, "TU", 1, 500), (2, "RS", 2, 500),
            (4, "RR", 1, 500),
        ]

        for row, key, col, rng in locs:
            self._add_loc_cell("vehicle_turret", grid, key, row, col, 0, rng)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["vehicle_turret"] = idx
        self._layout_keys["vehicle_turret"] = ["FR", "LS", "TU", "RS", "RR"]

    # ── VTOL ────────────────────────────────────────────────────────────────────

    def _build_vtol(self) -> None:
        self._spinboxes["vtol"] = {}
        page = QWidget()
        grid = QGridLayout(page)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(4)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        locs = [
            (0, "FR", 1, 500), (2, "LS", 0, 500), (2, "RS", 3, 500),
            (4, "RR", 1, 500), (2, "RO", 1, 500),
        ]

        for row, key, col, rng in locs:
            self._add_loc_cell("vtol", grid, key, row, col, 0, rng)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["vtol"] = idx
        self._layout_keys["vtol"] = ["FR", "LS", "RS", "RR", "RO"]

    # ── AeroSpace Fighter ───────────────────────────────────────────────────────

    def _build_fighter(self) -> None:
        self._spinboxes["fighter"] = {}
        page = QWidget()
        grid = QGridLayout(page)
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(4)
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        locs = [
            (0, "N", 1, 500), (2, "LW", 0, 500), (2, "RW", 3, 500),
            (4, "AFT", 1, 500),
        ]

        for row, key, col, rng in locs:
            self._add_loc_cell("fighter", grid, key, row, col, 0, rng)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["fighter"] = idx
        self._layout_keys["fighter"] = ["N", "LW", "RW", "AFT"]

    # ── Simple (BattleArmor / Infantry) ─────────────────────────────────────────

    def _build_simple(self) -> None:
        self._spinboxes["simple"] = {}
        page = QWidget()
        form = QFormLayout(page)

        sp = QSpinBox()
        sp.setRange(0, 20)
        sp.valueChanged.connect(self._emit)
        self._spinboxes["simple"]["TROOPER"] = sp
        form.addRow("Armor Per Trooper:", sp)

        self._stack.addWidget(page)
        idx = self._stack.count() - 1
        self._layout_index["simple"] = idx
        self._layout_keys["simple"] = ["TROOPER"]

    # ── Helper ───────────────────────────────────────────────────────────────────

    _LOC_LABELS: dict[str, str] = {
        "HD": "Head",
        "LA": "Left Arm",    "RA": "Right Arm",
        "LT": "Left Torso",  "CT": "Center Torso", "RT": "Right Torso",
        "LL": "Left Leg",    "RL": "Right Leg",
        "FLL": "Front Left Leg",   "FRL": "Front Right Leg",
        "RLL": "Rear Left Leg",    "RRL": "Rear Right Leg",
        "LTR": "Rear Left Torso",  "CTR": "Rear Center Torso", "RTR": "Rear Right Torso",
        "FR": "Front",       "LS": "Left Side",    "RS": "Right Side",
        "RR": "Rear",        "TU": "Turret",       "RO": "Rotor",
        "N": "Nose",         "LW": "Left Wing",    "RW": "Right Wing",
        "AFT": "Aft",
    }

    def _add_loc_cell(self, layout: str, grid: QGridLayout, key: str,
                      row: int, col: int, col_span: int, rng: int) -> None:
        w = QWidget()
        vb = QVBoxLayout(w)
        vb.setContentsMargins(4, 2, 4, 2)
        vb.setSpacing(1)

        label = QLabel(self._LOC_LABELS.get(key, key))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vb.addWidget(label)

        sp = QSpinBox()
        sp.setRange(1, rng)
        sp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sp.setFixedWidth(50)
        sp.valueChanged.connect(self._emit)
        vb.addWidget(sp, alignment=Qt.AlignmentFlag.AlignCenter)

        self._spinboxes[layout][key] = sp
        grid.addWidget(w, row, col, 1, col_span + 1, Qt.AlignmentFlag.AlignCenter)

    # ── Public API ───────────────────────────────────────────────────────────────

    def set_unit_type(self, unit_type: str, motive_type: str = "",
                      has_turret: bool = False) -> None:
        """Switch the stacked layout based on unit type and configuration."""
        self._building = True
        try:
            if unit_type == "BattleMech":
                self._current_layout = "quad" if motive_type == "Quad" else "biped"
            elif unit_type == "CombatVehicle":
                if motive_type == "VTOL":
                    self._current_layout = "vtol"
                elif has_turret:
                    self._current_layout = "vehicle_turret"
                else:
                    self._current_layout = "vehicle_no_turret"
            elif unit_type in ("AeroSpace Fighter", "Conventional Fighter"):
                self._current_layout = "fighter"
            else:
                self._current_layout = "simple"
            self._stack.setCurrentIndex(self._layout_index[self._current_layout])
        finally:
            self._building = False

    def get_armor(self) -> dict[str, int]:
        """Return the armor dict for the currently visible layout."""
        keys = self._layout_keys.get(self._current_layout, [])
        boxes = self._spinboxes.get(self._current_layout, {})
        return {key: boxes[key].value() for key in keys}

    def load_armor(self, armor: dict[str, int]) -> None:
        self._building = True
        try:
            keys = self._layout_keys.get(self._current_layout, [])
            boxes = self._spinboxes.get(self._current_layout, {})
            for key in keys:
                boxes[key].setValue(armor.get(key, 0))
        finally:
            self._building = False

    def _emit(self, *_) -> None:
        if not self._building:
            self.changed.emit()
