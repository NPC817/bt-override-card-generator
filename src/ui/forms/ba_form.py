"""Battle Armor entry form."""
from __future__ import annotations

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QComboBox, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QScrollArea, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget,
)

from ...models.battle_armor import BattleArmor


class BattleArmorForm(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._unit: BattleArmor | None = None
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
        self._chassis.setPlaceholderText("e.g. Elemental")
        self._variant = QLineEdit()
        self._variant.setPlaceholderText("e.g. Battle Armor")
        self._tech = QComboBox()
        self._tech.addItems(["IS", "Clan", "Mixed"])

        id_form.addRow("Chassis:", self._chassis)
        id_form.addRow("Variant:", self._variant)
        id_form.addRow("Tech:",    self._tech)
        layout.addWidget(id_group)

        # ── Stats ───────────────────────────────────────────────────────────
        stats_group = QGroupBox("Stats")
        stats_grid = QGridLayout(stats_group)
        stats_grid.setContentsMargins(8, 12, 8, 8)
        stats_grid.setVerticalSpacing(4)

        self._weight_class = QComboBox()
        self._weight_class.addItems([
            BattleArmor.PAL, BattleArmor.LIGHT, BattleArmor.MEDIUM,
            BattleArmor.HEAVY, BattleArmor.ASSAULT,
        ])
        self._weight_class.setCurrentText(BattleArmor.MEDIUM)

        self._squad_size = QSpinBox()
        self._squad_size.setRange(4, 6)
        self._squad_size.setValue(4)

        self._ground_mp = QSpinBox()
        self._ground_mp.setRange(1, 3)
        self._ground_mp.setValue(1)

        self._walk_mp_label = QLabel()
        self._walk_mp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._run_mp_label = QLabel()
        self._run_mp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._armor_per_trooper = QSpinBox()
        self._armor_per_trooper.setRange(0, 18)
        self._armor_per_trooper.setValue(4)

        self._mass_label = QLabel()

        # Row 0
        stats_grid.addWidget(QLabel("Weight Class:"), 0, 0)
        stats_grid.addWidget(self._weight_class,       0, 1)
        stats_grid.addWidget(QLabel("Squad Size:"),    0, 2)
        stats_grid.addWidget(self._squad_size,         0, 3)
        stats_grid.addWidget(QLabel("Ground MP:"),     0, 4)
        stats_grid.addWidget(self._ground_mp,          0, 5)
        # Row 1
        stats_grid.addWidget(QLabel("Walk MP:"),       1, 0)
        stats_grid.addWidget(self._walk_mp_label,      1, 1)
        stats_grid.addWidget(QLabel("Run MP:"),        1, 2)
        stats_grid.addWidget(self._run_mp_label,       1, 3)
        stats_grid.addWidget(QLabel("Armor/Trooper:"), 1, 4)
        stats_grid.addWidget(self._armor_per_trooper,  1, 5)
        # Row 2
        stats_grid.addWidget(QLabel("Mass:"),          2, 0)
        stats_grid.addWidget(self._mass_label,         2, 1, 1, 3)

        layout.addWidget(stats_group)

        # ── Motive ──────────────────────────────────────────────────────────
        motive_group = QGroupBox("Motive")
        motive_grid = QGridLayout(motive_group)
        motive_grid.setContentsMargins(8, 12, 8, 8)
        motive_grid.setVerticalSpacing(4)

        self._motive = QComboBox()
        self._motive.addItems([BattleArmor.BIPED, BattleArmor.QUAD])

        self._other_motive = QComboBox()
        self._jump_mp_label = QLabel()
        self._jump_mp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._other_mp = QSpinBox()
        self._other_mp.setRange(0, 7)
        self._other_mp.setValue(0)

        motive_grid.addWidget(QLabel("Motive Type:"),  0, 0)
        motive_grid.addWidget(self._motive,             0, 1)
        motive_grid.addWidget(QLabel("Other Motive:"),  0, 2)
        motive_grid.addWidget(self._other_motive,       0, 3)
        motive_grid.addWidget(QLabel("Other MP:"),      1, 0)
        motive_grid.addWidget(self._other_mp,           1, 1)
        motive_grid.addWidget(QLabel("Jump MP:"),       1, 2)
        motive_grid.addWidget(self._jump_mp_label,      1, 3)

        layout.addWidget(motive_group)

        # ── Abilities (computed, shown as info) ──────────────────────────────
        abil_group = QGroupBox("Abilities")
        abil_grid = QGridLayout(abil_group)
        abil_grid.setContentsMargins(8, 12, 8, 8)

        self._anti_mech_label = QLabel()
        self._anti_mech_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._mechanized_label = QLabel()
        self._mechanized_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        abil_grid.addWidget(QLabel("Anti-Mech:"),   0, 0)
        abil_grid.addWidget(self._anti_mech_label,   0, 1)
        abil_grid.addWidget(QLabel("Mechanized:"),   0, 2)
        abil_grid.addWidget(self._mechanized_label,  0, 3)

        layout.addWidget(abil_group)

        # ── Weapons & Equipment (tabbed) ────────────────────────────────────
        tabs = QTabWidget()
        from ..weapons_panel import WeaponsPanel
        from ..equipment_panel import EquipmentPanel

        self._weapons_panel = WeaponsPanel(unit_type="ba", tech=self._tech.currentText())
        tabs.addTab(self._weapons_panel, "Weapons")

        self._equipment_panel = EquipmentPanel(unit_type="ba")
        tabs.addTab(self._equipment_panel, "Equipment")
        layout.addWidget(tabs)

        # Connect signals
        self._motive.currentIndexChanged.connect(self._on_motive_changed)
        self._weight_class.currentIndexChanged.connect(self._on_weight_class_changed)
        self._tech.currentIndexChanged.connect(self._on_tech_changed)
        self._tech.currentIndexChanged.connect(self._on_weapon_tech_changed)
        self._other_motive.currentIndexChanged.connect(self._on_other_motive_changed)
        self._ground_mp.valueChanged.connect(self._update_computed_labels)
        self._other_mp.valueChanged.connect(self._update_computed_labels)
        self._weight_class.currentIndexChanged.connect(self._update_computed_labels)
        self._squad_size.valueChanged.connect(self._update_mass_label)

        for w in self.findChildren(QWidget):
            if w in (self._walk_mp_label, self._run_mp_label,
                     self._jump_mp_label, self._mass_label,
                     self._anti_mech_label, self._mechanized_label):
                continue
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

    def _on_motive_changed(self) -> None:
        if self._building:
            return
        # Refresh weight class list (Quad excludes PAL)
        mt = self._motive.currentText()
        current = self._weight_class.currentText()
        self._weight_class.blockSignals(True)
        self._weight_class.clear()
        wcs = [BattleArmor.LIGHT, BattleArmor.MEDIUM, BattleArmor.HEAVY, BattleArmor.ASSAULT]
        if mt == BattleArmor.BIPED:
            wcs.insert(0, BattleArmor.PAL)
        self._weight_class.addItems(wcs)
        if current in wcs:
            self._weight_class.setCurrentText(current)
        self._weight_class.blockSignals(False)
        self._refresh_other_motives()
        self._update_constraints()
        self._update_computed_labels()
        self._on_changed()

    def _on_weight_class_changed(self) -> None:
        if self._building:
            return
        self._refresh_other_motives()
        self._update_constraints()
        self._update_computed_labels()
        self._on_changed()

    def _on_weapon_tech_changed(self) -> None:
        self._weapons_panel.set_tech(self._tech.currentText())

    def _on_tech_changed(self) -> None:
        if self._building:
            return
        tech = self._tech.currentText()
        allowed = [5] if tech == "Clan" else [4, 5, 6]
        val = self._squad_size.value()
        self._squad_size.setRange(allowed[0], allowed[-1])
        if val not in allowed:
            self._squad_size.setValue(allowed[0])
        self._refresh_other_motives()
        self._update_computed_labels()
        self._on_changed()

    def _on_other_motive_changed(self) -> None:
        if self._building:
            return
        omt = self._other_motive.currentText()
        self._other_mp.setEnabled(omt != BattleArmor.OTHER_NONE)
        if omt == BattleArmor.OTHER_NONE:
            self._other_mp.setValue(0)
        self._update_constraints()
        self._update_computed_labels()
        self._on_changed()

    def _refresh_other_motives(self) -> None:
        """Rebuild other motive combo based on current state."""
        mt = self._motive.currentText()
        tech = self._tech.currentText()
        wc = self._weight_class.currentText()
        # Determine allowed types using a temp unit
        temp = BattleArmor()
        temp.motive_type = mt
        temp.tech = tech
        temp.weight_class = wc
        allowed = temp.allowed_other_motive_types
        current = self._other_motive.currentText()
        self._other_motive.blockSignals(True)
        self._other_motive.clear()
        self._other_motive.addItems(allowed)
        if current in allowed:
            self._other_motive.setCurrentText(current)
        self._other_motive.blockSignals(False)

    def _update_constraints(self) -> None:
        """Update spinbox ranges based on current model state."""
        temp = self._get_temp_unit()
        self._ground_mp.setRange(temp.min_ground_mp, temp.max_ground_mp)
        self._armor_per_trooper.setMaximum(temp.max_armor)
        omt = self._other_motive.currentText()
        if omt != BattleArmor.OTHER_NONE:
            self._other_mp.setMaximum(temp.max_other_mp)

    def _get_temp_unit(self) -> BattleArmor:
        temp = BattleArmor()
        temp.motive_type = self._motive.currentText()
        temp.weight_class = self._weight_class.currentText()
        temp.tech = self._tech.currentText()
        temp.ground_mp = self._ground_mp.value()
        temp.other_motive_type = self._other_motive.currentText()
        temp.other_mp = self._other_mp.value()
        temp.armor_per_trooper = self._armor_per_trooper.value()
        temp.squad_size = self._squad_size.value()
        temp.equipment = self._equipment_panel.get_equipment()
        return temp

    def _update_computed_labels(self) -> None:
        temp = self._get_temp_unit()
        self._walk_mp_label.setText(str(temp.walk_mp))
        self._run_mp_label.setText(str(temp.run_mp))
        self._jump_mp_label.setText(str(temp.other_display_mp))
        self._anti_mech_label.setText("Yes" if temp.has_anti_mech else "No")
        self._mechanized_label.setText("Yes" if temp.has_mechanized else "No")
        self._update_mass_label()

    def _update_mass_label(self) -> None:
        temp = self._get_temp_unit()
        self._mass_label.setText(temp.mass_str)

    def _on_changed(self, *_args) -> None:
        if self._building:
            return
        self.changed.emit()

    def load_unit(self, unit: BattleArmor) -> None:
        self._building = True
        self._unit = unit

        self._chassis.setText(unit.chassis)
        self._variant.setText(unit.variant)
        self._tech.setCurrentText(unit.tech)

        # Motive first (weight class list depends on it)
        idx = self._motive.findText(unit.motive_type)
        if idx >= 0:
            self._motive.setCurrentIndex(idx)
        else:
            self._motive.setCurrentText(BattleArmor.BIPED)

        # Weight class
        idx = self._weight_class.findText(unit.weight_class)
        if idx >= 0:
            self._weight_class.setCurrentIndex(idx)
        else:
            self._weight_class.setCurrentText(BattleArmor.MEDIUM)

        # Squad size
        tech = self._tech.currentText()
        allowed = [5] if tech == "Clan" else [4, 5, 6]
        self._squad_size.setRange(allowed[0], allowed[-1])
        self._squad_size.setValue(unit.squad_size)

        self._ground_mp.setValue(unit.ground_mp)
        self._armor_per_trooper.setValue(unit.armor_per_trooper)

        # Other motive
        self._refresh_other_motives()
        idx = self._other_motive.findText(unit.other_motive_type)
        if idx >= 0:
            self._other_motive.setCurrentIndex(idx)
        else:
            self._other_motive.setCurrentText(BattleArmor.OTHER_NONE)
        self._other_mp.setValue(unit.other_mp)

        self._weapons_panel.load_weapons(unit.weapons)
        self._equipment_panel.load_equipment(unit.equipment)

        self._update_constraints()
        self._update_computed_labels()
        self._building = False

    def get_unit(self) -> BattleArmor:
        unit = self._unit or BattleArmor()
        unit.chassis = self._chassis.text().strip()
        unit.variant = self._variant.text().strip()
        unit.tech = self._tech.currentText()
        unit.weight_class = self._weight_class.currentText()
        unit.squad_size = self._squad_size.value()
        unit.ground_mp = self._ground_mp.value()
        unit.armor_per_trooper = self._armor_per_trooper.value()
        unit.motive_type = self._motive.currentText()
        unit.other_motive_type = self._other_motive.currentText()
        unit.other_mp = self._other_mp.value()
        unit.weapons = self._weapons_panel.get_weapons()
        unit.equipment = self._dedup_equipment(self._equipment_panel.get_equipment())
        unit.reset_motives()
        unit.reset_armor()
        return unit

    @staticmethod
    def _dedup_equipment(equipment: list) -> list:
        seen: set[tuple[str, str]] = set()
        deduped = []
        for e in equipment:
            sig = (e.equipment_key, e.subtype)
            if sig not in seen:
                seen.add(sig)
                e.location = ""
                deduped.append(e)
        return deduped
