"""DropShip entry form."""
from __future__ import annotations

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QScrollArea, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget,
)

from ...models.dropship import Dropship, Transporter


class DropshipForm(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._unit: Dropship | None = None
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
        self._chassis.setPlaceholderText("e.g. Union")
        self._variant = QLineEdit()
        self._variant.setPlaceholderText("e.g. (2708)")
        self._tech = QComboBox()
        self._tech.addItems(["IS", "Clan", "Mixed"])

        id_form.addRow("Chassis:", self._chassis)
        id_form.addRow("Variant:", self._variant)
        id_form.addRow("Tech:",    self._tech)
        layout.addWidget(id_group)

        # ── Stats ───────────────────────────────────────────────────────────
        stats_group = QGroupBox("Stats")
        self._stats_form = QFormLayout(stats_group)

        self._motive = QComboBox()
        self._motive.addItems([Dropship.AERODYNE, Dropship.SPHEROID])
        self._motive.currentTextChanged.connect(self._on_motive_changed)

        self._tonnage = QSpinBox()
        self._tonnage.setRange(100, 100000)
        self._tonnage.setSingleStep(100)
        self._tonnage.setValue(3500)

        self._safe_thrust = QSpinBox()
        self._safe_thrust.setRange(1, 20)
        self._safe_thrust.setValue(3)

        self._max_thrust = QSpinBox()
        self._max_thrust.setRange(2, 30)
        self._max_thrust.setValue(5)

        self._sinks = QSpinBox()
        self._sinks.setRange(0, 2000)
        self._sinks.setValue(30)

        self._dhs = QCheckBox("Double Heat Sinks")

        self._si = QSpinBox()
        self._si.setRange(1, 200)
        self._si.setValue(10)

        self._stats_form.addRow("Motive Type:", self._motive)
        self._stats_form.addRow("Tonnage:",     self._tonnage)
        self._stats_form.addRow("Safe Thrust:", self._safe_thrust)
        self._stats_form.addRow("Max Thrust:",  self._max_thrust)
        self._stats_form.addRow("Heat Sinks:",  self._sinks)
        self._stats_form.addRow("",             self._dhs)
        self._stats_form.addRow("Structural Integrity:", self._si)
        layout.addWidget(stats_group)

        # ── Armor ───────────────────────────────────────────────────────────
        armor_group = QGroupBox("Armor")
        armor_form = QFormLayout(armor_group)

        self._armor_n = QSpinBox();  self._armor_n.setRange(0, 9999)
        self._armor_lw = QSpinBox(); self._armor_lw.setRange(0, 9999)
        self._armor_rw = QSpinBox(); self._armor_rw.setRange(0, 9999)
        self._armor_a = QSpinBox();  self._armor_a.setRange(0, 9999)

        # Explicit labels so they can swap Wing ↔ Side with the motive type
        self._armor_lw_lbl = QLabel("Left Wing:")
        self._armor_rw_lbl = QLabel("Right Wing:")

        armor_form.addRow("Nose:", self._armor_n)
        armor_form.addRow(self._armor_lw_lbl, self._armor_lw)
        armor_form.addRow(self._armor_rw_lbl, self._armor_rw)
        armor_form.addRow("Aft:",  self._armor_a)
        layout.addWidget(armor_group)

        # ── Weapons & Equipment (tabbed) ────────────────────────────────────
        tabs = QTabWidget()
        from ..weapons_panel import WeaponsPanel
        from ..equipment_panel import EquipmentPanel

        self._weapons_panel = WeaponsPanel(unit_type="dropship", tech=self._tech.currentText())
        tabs.addTab(self._weapons_panel, "Weapons")

        self._equipment_panel = EquipmentPanel()
        tabs.addTab(self._equipment_panel, "Equipment")
        layout.addWidget(tabs)

        # Tonnage → weapons panel for auto-group
        self._tonnage.valueChanged.connect(
            lambda v: self._weapons_panel.set_tonnage(int(v)))

        self._tech.currentIndexChanged.connect(self._on_weapon_tech_changed)
        # Connect signals
        for w in self.findChildren(QWidget):
            if hasattr(w, "textChanged"):
                w.textChanged.connect(self._on_changed)
            if hasattr(w, "currentIndexChanged"):
                w.currentIndexChanged.connect(self._on_changed)
            if hasattr(w, "toggled"):
                w.toggled.connect(self._on_changed)
            if hasattr(w, "valueChanged"):
                w.valueChanged.connect(self._on_changed)
            if hasattr(w, "changed"):
                w.changed.connect(self._on_changed)

        layout.addStretch()

    def _on_weapon_tech_changed(self) -> None:
        self._weapons_panel.set_tech(self._tech.currentText())

    def _on_motive_changed(self, text: str) -> None:
        aero = text == Dropship.AERODYNE
        self._armor_lw_lbl.setText("Left Wing:" if aero else "Left Side:")
        self._armor_rw_lbl.setText("Right Wing:" if aero else "Right Side:")
        # Remap existing weapon locations so stored keys match the card labels
        remap = {"LS": "LW", "RS": "RW"} if aero else {"LW": "LS", "RW": "RS"}
        weapons = self._weapons_panel.get_weapons()
        if weapons and any(w.location in remap for w in weapons):
            for w in weapons:
                if w.location in remap:
                    w.location = remap[w.location]
            self._weapons_panel.load_weapons(weapons)

    def _on_changed(self, *_args) -> None:
        if self._building:
            return
        self.changed.emit()

    def load_unit(self, unit: Dropship) -> None:
        self._building = True
        self._unit = unit

        self._chassis.setText(unit.chassis)
        self._variant.setText(unit.variant)
        self._tech.setCurrentText(unit.tech)
        self._motive.setCurrentText(unit.motive_type)   # fires _on_motive_changed
        self._tonnage.setValue(unit.tonnage)
        self._weapons_panel.set_tonnage(unit.tonnage)
        self._safe_thrust.setValue(unit.safe_thrust)
        self._max_thrust.setValue(unit.max_thrust)
        self._sinks.setValue(unit.sinks)
        self._dhs.setChecked(unit.has_dhs)
        self._si.setValue(unit.structural_integrity)
        self._armor_n.setValue(unit.armor.get("N", 0))
        self._armor_lw.setValue(unit.armor.get(unit.left_key, 0))
        self._armor_rw.setValue(unit.armor.get(unit.right_key, 0))
        self._armor_a.setValue(unit.armor.get("A", 0))

        # Weapons & equipment
        self._weapons_panel.load_weapons(unit.weapons)
        self._equipment_panel.load_equipment(unit.equipment)

        self._building = False

    def get_unit(self) -> Dropship:
        """Build/update the Dropship from the widgets (idempotent — runs on
        every debounced preview render)."""
        unit = self._unit or Dropship()
        unit.chassis = self._chassis.text().strip()
        unit.variant = self._variant.text().strip()
        unit.tech = self._tech.currentText()
        unit.motive_type = self._motive.currentText()
        unit.tonnage = self._tonnage.value()
        unit.safe_thrust = self._safe_thrust.value()
        unit.max_thrust = self._max_thrust.value()
        unit.sinks = self._sinks.value()
        unit.has_dhs = self._dhs.isChecked()
        unit.structural_integrity = self._si.value()
        unit.armor["N"] = self._armor_n.value()
        unit.armor["A"] = self._armor_a.value()
        # Write the active key pair, zero the inactive one (no phantom values
        # when toggling Aerodyne ↔ Spheroid back and forth)
        if unit.motive_type == Dropship.AERODYNE:
            unit.armor["LW"] = self._armor_lw.value()
            unit.armor["RW"] = self._armor_rw.value()
            unit.armor["LS"] = unit.armor["RS"] = 0
        else:
            unit.armor["LS"] = self._armor_lw.value()
            unit.armor["RS"] = self._armor_rw.value()
            unit.armor["LW"] = unit.armor["RW"] = 0

        unit.weapons = self._weapons_panel.get_weapons()
        unit.equipment = self._equipment_panel.get_equipment()

        # Re-sync transporters from the editable equipment rows, preserving
        # door counts by key (new rows get 0 doors; deleted rows drop theirs).
        # Cargo/quarters transporters also live in the equipment rows — keep
        # them so raw counts survive .ovr/.force round-trips.
        prev = {t.key: t for t in unit.transporters}
        known = set(prev) | set(Dropship.BAY_KEYS)
        unit.transporters = [
            Transporter(
                key=eq.equipment_key,
                count=float(eq.uses or 0),
                doors=(prev.get(eq.equipment_key).doors
                       if prev.get(eq.equipment_key) else 0),
            )
            for eq in unit.equipment
            if eq.equipment_key in known
        ]
        return unit
