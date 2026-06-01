"""AeroSpace Fighter entry form."""
from __future__ import annotations

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QFormLayout, QGroupBox,
    QLineEdit, QScrollArea, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget,
)

from ...models.aero import AeroSpaceFighter


class AeroForm(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._unit: AeroSpaceFighter | None = None
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
        self._chassis.setPlaceholderText("e.g. Stingray")
        self._variant = QLineEdit()
        self._variant.setPlaceholderText("e.g. F-90")
        self._tech = QComboBox()
        self._tech.addItems(["IS", "Clan", "Mixed"])
        self._omni = QCheckBox("OmniFighter")

        id_form.addRow("Chassis:", self._chassis)
        id_form.addRow("Variant:", self._variant)
        id_form.addRow("Tech:",    self._tech)
        id_form.addRow("",         self._omni)
        layout.addWidget(id_group)

        # ── Stats ───────────────────────────────────────────────────────────
        stats_group = QGroupBox("Stats")
        stats_form = QFormLayout(stats_group)
        self._stats_form = stats_form

        self._motive = QComboBox()
        self._motive.addItems([AeroSpaceFighter.AEROSPACE, AeroSpaceFighter.CONVENTIONAL])
        self._motive.currentTextChanged.connect(self._on_motive_changed)

        self._tonnage = QSpinBox()
        self._tonnage.setRange(5, 200)
        self._tonnage.setSingleStep(5)
        self._tonnage.setValue(50)

        self._safe_thrust = QSpinBox()
        self._safe_thrust.setRange(1, 20)
        self._safe_thrust.setValue(5)

        self._max_thrust = QSpinBox()
        self._max_thrust.setRange(2, 30)
        self._max_thrust.setValue(8)

        self._sinks = QSpinBox()
        self._sinks.setRange(0, 100)
        self._sinks.setValue(10)

        self._dhs = QCheckBox("Double Heat Sinks")

        stats_form.addRow("Motive Type:", self._motive)
        stats_form.addRow("Tonnage:",     self._tonnage)
        stats_form.addRow("Safe Thrust:", self._safe_thrust)
        stats_form.addRow("Max Thrust:",  self._max_thrust)
        stats_form.addRow("Heat Sinks:",  self._sinks)
        stats_form.addRow("",             self._dhs)
        layout.addWidget(stats_group)

        # ── Armor ───────────────────────────────────────────────────────────
        armor_group = QGroupBox("Armor")
        armor_form = QFormLayout(armor_group)

        self._armor_n = QSpinBox();  self._armor_n.setRange(0, 999)
        self._armor_lw = QSpinBox(); self._armor_lw.setRange(0, 999)
        self._armor_rw = QSpinBox(); self._armor_rw.setRange(0, 999)
        self._armor_a = QSpinBox(); self._armor_a.setRange(0, 999)

        armor_form.addRow("Nose:",       self._armor_n)
        armor_form.addRow("Left Wing:",  self._armor_lw)
        armor_form.addRow("Right Wing:", self._armor_rw)
        armor_form.addRow("Aft:",        self._armor_a)
        layout.addWidget(armor_group)

        # ── Weapons & Equipment (tabbed) ────────────────────────────────────
        tabs = QTabWidget()
        from ..weapons_panel import WeaponsPanel
        from ..equipment_panel import EquipmentPanel

        self._weapons_panel = WeaponsPanel(unit_type="aero", tech=self._tech.currentText())
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
        is_aero = text == AeroSpaceFighter.AEROSPACE
        self._stats_form.setRowVisible(self._sinks, is_aero)
        self._stats_form.setRowVisible(self._dhs, is_aero)

    def _on_changed(self, *_args) -> None:
        if self._building:
            return
        self.changed.emit()

    def load_unit(self, unit: AeroSpaceFighter) -> None:
        self._building = True
        self._unit = unit

        self._chassis.setText(unit.chassis)
        self._variant.setText(unit.variant)
        self._tech.setCurrentText(unit.tech)
        self._omni.setChecked(unit.omni)
        self._motive.setCurrentText(unit.motive_type)
        self._on_motive_changed(unit.motive_type)
        self._tonnage.setValue(unit.tonnage)
        self._weapons_panel.set_tonnage(unit.tonnage)
        self._safe_thrust.setValue(unit.safe_thrust)
        self._max_thrust.setValue(unit.max_thrust)
        self._sinks.setValue(unit.sinks)
        self._dhs.setChecked(unit.has_dhs)
        self._armor_n.setValue(unit.armor.get("N", 0))
        self._armor_lw.setValue(unit.armor.get("LW", 0))
        self._armor_rw.setValue(unit.armor.get("RW", 0))
        self._armor_a.setValue(unit.armor.get("A", 0))

        # Weapons & equipment
        self._weapons_panel.load_weapons(unit.weapons)
        self._equipment_panel.load_equipment(unit.equipment)

        self._building = False

    def get_unit(self) -> AeroSpaceFighter:
        unit = self._unit or AeroSpaceFighter()
        unit.chassis = self._chassis.text().strip()
        unit.variant = self._variant.text().strip()
        unit.tech = self._tech.currentText()
        unit.omni = self._omni.isChecked()
        unit.motive_type = self._motive.currentText()
        unit.tonnage = self._tonnage.value()
        unit.safe_thrust = self._safe_thrust.value()
        unit.max_thrust = self._max_thrust.value()
        unit.sinks = self._sinks.value()
        unit.has_dhs = self._dhs.isChecked()
        unit.armor["N"] = self._armor_n.value()
        unit.armor["LW"] = self._armor_lw.value()
        unit.armor["RW"] = self._armor_rw.value()
        unit.armor["A"] = self._armor_a.value()

        unit.weapons = self._weapons_panel.get_weapons()
        unit.equipment = self._equipment_panel.get_equipment()
        return unit
