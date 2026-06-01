"""CombatVehicle entry form."""
from __future__ import annotations
import math

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QScrollArea, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget,
)

from ...models.vehicle import CombatVehicle


class VehicleForm(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
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

        # ── Identity ──────────────────────────────────────────────────────────
        id_group = QGroupBox("Identity")
        id_form = QFormLayout(id_group)

        self._chassis = QLineEdit(); self._chassis.setPlaceholderText("e.g. Condor")
        self._variant = QLineEdit(); self._variant.setPlaceholderText("e.g. Heavy Hover Tank")
        self._tech    = QComboBox(); self._tech.addItems(["IS", "Clan", "Mixed"])
        self._motive  = QComboBox()
        self._motive.addItems(["Tracked", "Wheeled", "Hover", "VTOL"])
        self._turret  = QCheckBox("Has Turret")

        id_form.addRow("Chassis:", self._chassis)
        id_form.addRow("Variant:", self._variant)
        id_form.addRow("Tech:",    self._tech)
        id_form.addRow("Motive:",  self._motive)
        id_form.addRow("",         self._turret)
        layout.addWidget(id_group)

        # ── Stats ─────────────────────────────────────────────────────────────
        stats_group = QGroupBox("Stats")
        stats_form = QFormLayout(stats_group)

        self._tonnage   = QComboBox()
        self._tonnage.addItems([str(t) for t in range(5, 105, 5)])
        self._tonnage.setCurrentText("50")
        self._cruise_mp = QSpinBox(); self._cruise_mp.setRange(1, 30); self._cruise_mp.setValue(4)
        self._flank_label = QLabel("6")

        stats_form.addRow("Tonnage:",   self._tonnage)
        stats_form.addRow("Cruise MP:", self._cruise_mp)
        stats_form.addRow("Flank MP:",  self._flank_label)
        layout.addWidget(stats_group)

        # ── Weapons, Equipment & Armor ────────────────────────────────────────
        from ..weapons_panel import WeaponsPanel
        from ..equipment_panel import EquipmentPanel
        from ..armor_panel import ArmorPanel

        sub_tabs = QTabWidget()
        sub_tabs.setMinimumHeight(250)
        self._weapons_panel   = WeaponsPanel(unit_type="vehicle", tech=self._tech.currentText())
        self._equipment_panel = EquipmentPanel()
        self._armor_panel     = ArmorPanel()
        self._armor_panel.set_unit_type("CombatVehicle", "Tracked")

        sub_tabs.addTab(self._weapons_panel,   "Weapons")
        sub_tabs.addTab(self._equipment_panel, "Equipment")
        sub_tabs.addTab(self._armor_panel,     "Armor")
        layout.addWidget(sub_tabs)

        # ── Connect signals ───────────────────────────────────────────────────
        for w in [self._chassis, self._variant]:
            w.textChanged.connect(self._emit)
        for w in [self._tech, self._motive]:
            w.currentIndexChanged.connect(self._emit)
        self._tech.currentIndexChanged.connect(self._on_weapon_tech_changed)
        self._turret.stateChanged.connect(self._emit)
        self._turret.stateChanged.connect(self._update_armor_layout)
        self._motive.currentIndexChanged.connect(self._update_armor_layout)
        self._tonnage.currentIndexChanged.connect(self._emit)
        self._tonnage.currentIndexChanged.connect(self._sync_tonnage)
        self._cruise_mp.valueChanged.connect(self._update_flank)
        self._cruise_mp.valueChanged.connect(self._emit)
        self._weapons_panel.changed.connect(self._emit)
        self._equipment_panel.changed.connect(self._emit)
        self._armor_panel.changed.connect(self._emit)

    def _on_weapon_tech_changed(self) -> None:
        self._weapons_panel.set_tech(self._tech.currentText())

    def _sync_tonnage(self, *_) -> None:
        try:
            self._weapons_panel.set_tonnage(int(self._tonnage.currentText()))
        except (ValueError, AttributeError):
            pass

    def _update_flank(self) -> None:
        self._flank_label.setText(str(math.floor(self._cruise_mp.value() * 1.5)))

    def _update_armor_layout(self) -> None:
        self._armor_panel.set_unit_type(
            "CombatVehicle",
            self._motive.currentText(),
            self._turret.isChecked(),
        )

    def _emit(self, *_) -> None:
        if not self._building:
            self.changed.emit()

    # ── Data in/out ───────────────────────────────────────────────────────────

    def get_unit(self) -> CombatVehicle:
        v = CombatVehicle()
        v.chassis     = self._chassis.text().strip()
        v.variant     = self._variant.text().strip()
        v.tech        = self._tech.currentText()
        v.motive_type = self._motive.currentText()
        v.has_turret  = self._turret.isChecked()
        v.tonnage     = int(self._tonnage.currentText())
        v.cruise_mp   = self._cruise_mp.value()
        v.armor       = self._armor_panel.get_armor()
        v.weapons     = self._weapons_panel.get_weapons()
        v.equipment   = self._equipment_panel.get_equipment()
        return v

    def load_unit(self, unit: CombatVehicle) -> None:
        self._building = True
        try:
            self._chassis.setText(unit.chassis)
            self._variant.setText(unit.variant)
            self._tech.setCurrentText(unit.tech)
            self._motive.setCurrentText(unit.motive_type)
            self._turret.setChecked(unit.has_turret)
            self._tonnage.setCurrentText(str(int(unit.tonnage)))
            self._cruise_mp.setValue(unit.cruise_mp)
            self._armor_panel.set_unit_type("CombatVehicle", unit.motive_type, unit.has_turret)
            self._armor_panel.load_armor(unit.armor)
            self._weapons_panel.load_weapons(unit.weapons)
            self._weapons_panel.set_tonnage(int(unit.tonnage))
            self._equipment_panel.load_equipment(unit.equipment)
            self._update_flank()
        finally:
            self._building = False
