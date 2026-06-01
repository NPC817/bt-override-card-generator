"""
BattleMech entry form.

Fields:
  - Chassis, Variant, Tech base, Motive type (Biped/Quad), OmniMech
  - Tonnage, Walk MP, Jump MP, Heat Sinks, DHS
  - Armor table (one row per location)
  - Weapons panel + Equipment panel
"""
from __future__ import annotations
import math

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget,
)

from ...models.mech import BattleMech


class MechForm(QWidget):
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

        self._chassis = QLineEdit();  self._chassis.setPlaceholderText("e.g. Hunchback")
        self._variant = QLineEdit();  self._variant.setPlaceholderText("e.g. HBK-4G")
        self._tech    = QComboBox();  self._tech.addItems(["IS", "Clan", "Mixed"])
        self._motive  = QComboBox();  self._motive.addItems(["Biped", "Quad"])
        self._omni    = QCheckBox("OmniMech")

        id_form.addRow("Chassis:", self._chassis)
        id_form.addRow("Variant:", self._variant)
        id_form.addRow("Tech:",    self._tech)
        id_form.addRow("Config:", self._motive)
        id_form.addRow("",        self._omni)
        layout.addWidget(id_group)

        # ── Stats ─────────────────────────────────────────────────────────────
        stats_group = QGroupBox("Stats")
        stats_form = QFormLayout(stats_group)

        self._tonnage  = QComboBox()
        self._tonnage.addItems([str(t) for t in range(20, 105, 5)])
        self._tonnage.setCurrentText("50")

        self._walk_mp = QSpinBox(); self._walk_mp.setRange(1, 20)
        self._walk_mp.setValue(4)
        self._run_mp_label = QLabel("6")

        self._jump_mp = QSpinBox(); self._jump_mp.setRange(0, 20)

        self._sinks   = QSpinBox(); self._sinks.setRange(0, 100); self._sinks.setValue(10)
        self._dhs     = QCheckBox("Double Heat Sinks")

        run_row = QHBoxLayout()
        run_row.addWidget(QLabel("Run MP:"))
        run_row.addWidget(self._run_mp_label)
        run_row.addStretch()

        stats_form.addRow("Tonnage:", self._tonnage)
        stats_form.addRow("Walk MP:", self._walk_mp)
        stats_form.addRow("", _wrap(run_row))
        stats_form.addRow("Jump MP:", self._jump_mp)
        stats_form.addRow("Heat Sinks:", self._sinks)
        stats_form.addRow("", self._dhs)
        layout.addWidget(stats_group)

        # ── Weapons, Equipment & Armor ────────────────────────────────────────
        from ..weapons_panel import WeaponsPanel
        from ..equipment_panel import EquipmentPanel
        from ..armor_panel import ArmorPanel

        sub_tabs = QTabWidget()
        sub_tabs.setMinimumHeight(250)
        self._weapons_panel   = WeaponsPanel(unit_type="mech", tech=self._tech.currentText())
        self._equipment_panel = EquipmentPanel()
        self._armor_panel     = ArmorPanel()
        self._armor_panel.set_unit_type("BattleMech", "Biped")

        sub_tabs.addTab(self._weapons_panel,   "Weapons")
        sub_tabs.addTab(self._equipment_panel, "Equipment")
        sub_tabs.addTab(self._armor_panel,     "Armor")
        layout.addWidget(sub_tabs)

        # ── Connect all signals ───────────────────────────────────────────────
        for w in [self._chassis, self._variant]:
            w.textChanged.connect(self._emit_changed)
        for w in [self._tech, self._motive]:
            w.currentIndexChanged.connect(self._emit_changed)
        self._tech.currentIndexChanged.connect(self._on_weapon_tech_changed)
        self._tonnage.currentIndexChanged.connect(self._emit_changed)
        self._tonnage.currentIndexChanged.connect(self._sync_tonnage)
        for w in [self._omni, self._dhs]:
            w.stateChanged.connect(self._emit_changed)
        for w in [self._walk_mp, self._jump_mp, self._sinks]:
            w.valueChanged.connect(self._emit_changed)
        self._walk_mp.valueChanged.connect(self._update_run_mp)
        self._motive.currentIndexChanged.connect(self._on_motive_changed)
        self._weapons_panel.changed.connect(self._emit_changed)
        self._equipment_panel.changed.connect(self._emit_changed)
        self._armor_panel.changed.connect(self._emit_changed)

    def _on_weapon_tech_changed(self) -> None:
        self._weapons_panel.set_tech(self._tech.currentText())

    def _sync_tonnage(self, *_) -> None:
        try:
            self._weapons_panel.set_tonnage(int(self._tonnage.currentText()))
        except (ValueError, AttributeError):
            pass

    def _update_run_mp(self) -> None:
        run = math.ceil(self._walk_mp.value() * 1.5)
        self._run_mp_label.setText(str(run))

    def _on_motive_changed(self) -> None:
        motive = self._motive.currentText()
        self._armor_panel.set_unit_type("BattleMech", motive)
        self._emit_changed()

    def _emit_changed(self, *_) -> None:
        if not self._building:
            self.changed.emit()

    # ── Data in/out ───────────────────────────────────────────────────────────

    def get_unit(self) -> BattleMech:
        m = BattleMech()
        m.chassis    = self._chassis.text().strip()
        m.variant    = self._variant.text().strip()
        m.tech       = self._tech.currentText()
        m.motive_type = BattleMech.QUAD if self._motive.currentText() == "Quad" else BattleMech.BIPED
        m.omni       = self._omni.isChecked()
        m.tonnage    = int(self._tonnage.currentText())
        m.walk_mp    = self._walk_mp.value()
        m.jump_mp    = self._jump_mp.value()
        m.sinks      = self._sinks.value()
        m.has_dhs    = self._dhs.isChecked()
        m.armor      = self._armor_panel.get_armor()
        m.weapons    = self._weapons_panel.get_weapons()
        m.equipment  = self._equipment_panel.get_equipment()
        return m

    def load_unit(self, unit: BattleMech) -> None:
        self._building = True
        try:
            self._chassis.setText(unit.chassis)
            self._variant.setText(unit.variant)
            self._tech.setCurrentText(unit.tech)
            self._motive.setCurrentText(unit.motive_type)
            self._omni.setChecked(unit.omni)
            self._tonnage.setCurrentText(str(unit.tonnage))
            self._walk_mp.setValue(unit.walk_mp)
            self._jump_mp.setValue(unit.jump_mp)
            self._sinks.setValue(unit.sinks)
            self._dhs.setChecked(unit.has_dhs)
            self._armor_panel.load_armor(unit.armor)
            self._weapons_panel.load_weapons(unit.weapons)
            self._weapons_panel.set_tonnage(unit.tonnage)
            self._equipment_panel.load_equipment(unit.equipment)
            self._update_run_mp()
        finally:
            self._building = False


def _wrap(layout) -> QWidget:
    w = QWidget()
    w.setLayout(layout)
    return w
