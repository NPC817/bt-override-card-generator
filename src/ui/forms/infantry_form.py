"""Infantry entry form."""
from __future__ import annotations

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QComboBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QScrollArea, QSpinBox,
    QVBoxLayout, QWidget,
)

from ...models.infantry import Infantry


# Per-motive constraints from card_gen.js V.MOTIVE_DATA (allowedSquadSize, maxSquads, maxTroops)
# Tuple: (min_squad_size, max_squad_size, max_squads, max_troops)
_MOTIVE_LIMITS: dict[str, tuple[int, int, int, int]] = {
    "Foot":               (5, 7, 5, 30),
    "Motorized":          (5, 7, 5, 30),
    "Jump":               (5, 7, 4, 24),
    "Mechanized Hover":   (4, 5, 4, 20),
    "Mechanized Tracked": (5, 7, 4, 28),
    "Mechanized Wheeled": (5, 6, 4, 24),
}


class InfantryForm(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._unit: Infantry | None = None
        self._building = False
        self._build_ui()

    def _build_ui(self) -> None:
        outer = QVBoxLayout(self)
        outer.setContentsMargins(4, 4, 4, 4)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        outer.addWidget(scroll)

        container = QWidget()
        scroll.setWidget(container)
        layout = QVBoxLayout(container)

        # ── Identity ────────────────────────────────────────────────────────
        id_group = QGroupBox("Identity")
        id_form = QFormLayout(id_group)

        self._chassis = QLineEdit()
        self._chassis.setPlaceholderText("e.g. Foot Platoon")
        self._variant = QLineEdit()
        self._variant.setPlaceholderText("e.g. (Laser)")
        self._tech = QComboBox()
        self._tech.addItems(["IS", "Clan", "Mixed"])

        id_form.addRow("Chassis:", self._chassis)
        id_form.addRow("Unique Name:", self._variant)
        id_form.addRow("Tech:", self._tech)
        layout.addWidget(id_group)

        # ── Troop Configuration ─────────────────────────────────────────────
        troop_group = QGroupBox("Troop Configuration")
        troop_form = QFormLayout(troop_group)

        self._motive_type = QComboBox()
        self._motive_type.addItems(list(_MOTIVE_LIMITS.keys()))
        troop_form.addRow("Motive Type:", self._motive_type)

        self._squad_size = QSpinBox()
        self._squad_size.setRange(5, 7)   # updated by _update_constraints on motive change
        self._squad_size.setValue(7)
        self._squad_size_hint = QLabel("Motive allows squad size 5–7.")
        self._squad_size_hint.setStyleSheet("color: gray; font-size: 10px;")
        troop_form.addRow("Troops per Squad:", self._squad_size)
        troop_form.addRow("", self._squad_size_hint)

        self._squad_count = QSpinBox()
        self._squad_count.setRange(1, 5)  # updated by _update_constraints on motive change
        self._squad_count.setValue(4)
        self._squad_count_hint = QLabel("Motive allows max 5 squads or 30 troops.")
        self._squad_count_hint.setStyleSheet("color: gray; font-size: 10px;")
        troop_form.addRow("Squads in Platoon:", self._squad_count)
        troop_form.addRow("", self._squad_count_hint)

        layout.addWidget(troop_group)

        # ── Weapon ──────────────────────────────────────────────────────────
        weapon_group = QGroupBox("Weapon")
        weapon_form = QFormLayout(weapon_group)

        self._weapon_type = QComboBox()
        for key, wdata in Infantry.WEAPON_DATA.items():
            self._weapon_type.addItem(wdata["name"], key)
        weapon_form.addRow("Weapon Type:", self._weapon_type)

        layout.addWidget(weapon_group)

        # ── Computed Stats ──────────────────────────────────────────────────
        stats_group = QGroupBox("Computed Stats")
        stats_form = QFormLayout(stats_group)

        self._move_label    = QLabel()
        self._tmm_label     = QLabel()
        self._mass_label    = QLabel()
        self._antimech_label = QLabel()

        stats_form.addRow("Move:", self._move_label)
        stats_form.addRow("TMM:", self._tmm_label)
        stats_form.addRow("Mass:", self._mass_label)
        stats_form.addRow("Anti-Mech:", self._antimech_label)

        layout.addWidget(stats_group)
        layout.addStretch()

        # ── Signals ─────────────────────────────────────────────────────────
        self._motive_type.currentIndexChanged.connect(self._on_motive_changed)
        self._squad_size.valueChanged.connect(self._on_squad_size_changed)
        self._squad_count.valueChanged.connect(self._on_changed)
        self._weapon_type.currentIndexChanged.connect(self._on_weapon_changed)
        self._chassis.textChanged.connect(self._on_changed)
        self._variant.textChanged.connect(self._on_changed)
        self._tech.currentIndexChanged.connect(self._on_changed)

        self._update_constraints()
        self._update_computed_labels()

    # ── Constraint helpers ────────────────────────────────────────────────────

    def _on_motive_changed(self) -> None:
        self._update_constraints()
        self._update_computed_labels()
        self._on_changed()

    def _on_squad_size_changed(self) -> None:
        self._update_squad_count_limit()
        self._update_computed_labels()
        self._on_changed()

    def _on_weapon_changed(self) -> None:
        self._update_squad_count_limit()
        self._update_computed_labels()
        self._on_changed()

    def _update_constraints(self) -> None:
        """Full constraint refresh — called on motive change."""
        key = self._motive_type.currentText()
        min_sq, max_sq, _max_squads, _max_troops = _MOTIVE_LIMITS.get(key, (5, 7, 5, 30))
        self._squad_size.setRange(min_sq, max_sq)
        if self._squad_size.value() < min_sq:
            self._squad_size.setValue(min_sq)
        elif self._squad_size.value() > max_sq:
            self._squad_size.setValue(max_sq)
        self._squad_size_hint.setText(f"Motive allows squad size {min_sq}–{max_sq}.")
        self._update_squad_count_limit()

    def _update_squad_count_limit(self) -> None:
        """Recompute max squads from current squad size, troop cap, and weapon penalty."""
        key = self._motive_type.currentText()
        _min_sq, _max_sq, max_squads, max_troops = _MOTIVE_LIMITS.get(key, (5, 7, 5, 30))
        sq_size = self._squad_size.value()

        # LRM reduces max squad count by 1 per card_gen.js
        weapon_key = self._weapon_type.currentData()
        wdata = Infantry.WEAPON_DATA.get(weapon_key, {})
        if wdata.get("reduce_squads"):
            max_squads = max(max_squads - 1, 1)

        effective_max = min(max_squads, max_troops // sq_size)
        self._squad_count.setRange(1, effective_max)
        if self._squad_count.value() > effective_max:
            self._squad_count.setValue(effective_max)
        self._squad_count_hint.setText(
            f"Motive allows max {effective_max} squads or {max_troops} troops."
        )

    def _update_computed_labels(self) -> None:
        tmp = self._build_temp_unit()
        self._move_label.setText(tmp.destiny_move)
        self._tmm_label.setText(tmp.destiny_tmm)
        self._mass_label.setText(f"{tmp.tonnage} Tons")
        self._antimech_label.setText("Yes" if tmp.has_anti_mech else "No")

    def _build_temp_unit(self) -> Infantry:
        u = Infantry()
        u.motion_type_key = self._motive_type.currentText()
        u.squad_size  = self._squad_size.value()
        u.squad_count = self._squad_count.value()
        return u

    # ── Change propagation ────────────────────────────────────────────────────

    def _on_changed(self, *_args) -> None:
        if self._building:
            return
        self._update_computed_labels()
        self.changed.emit()

    # ── Public API ────────────────────────────────────────────────────────────

    def load_unit(self, unit: Infantry) -> None:
        self._building = True
        self._unit = unit

        self._chassis.setText(unit.chassis)
        self._variant.setText(unit.variant)
        self._tech.setCurrentText(unit.tech)

        idx = self._motive_type.findText(unit.motion_type_key)
        self._motive_type.setCurrentIndex(idx if idx >= 0 else 0)

        self._update_constraints()

        self._squad_size.setValue(unit.squad_size)
        self._squad_count.setValue(unit.squad_count)

        # Match weapon type by data key stored in item data
        for i in range(self._weapon_type.count()):
            if self._weapon_type.itemData(i) == unit.weapon_type:
                self._weapon_type.setCurrentIndex(i)
                break

        self._update_computed_labels()
        self._building = False

    def get_unit(self) -> Infantry:
        unit = self._unit or Infantry()
        unit.chassis = self._chassis.text().strip()
        unit.variant  = self._variant.text().strip()
        unit.tech     = self._tech.currentText()
        unit.motion_type_key = self._motive_type.currentText()
        unit.squad_size  = self._squad_size.value()
        unit.squad_count = self._squad_count.value()
        unit.weapon_type = self._weapon_type.currentData()
        return unit
