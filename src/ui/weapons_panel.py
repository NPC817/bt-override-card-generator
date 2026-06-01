"""
Weapons panel: QTableWidget with one row per weapon entry.
Columns: TIC, Weapon, Location, Ammo Type, One-Shot
"""
from __future__ import annotations
import logging

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)

from ..models.unit import UnitWeapon
from ..models.data_store import DataStore
from ..engine.tic_grouper import ResolvedWeapon, validate_tic_assignments
from .theme import ThemeManager

_MECH_LOCATIONS   = ["T","LA","RA","LL","RL","HD","(R) T","(R) LL","(R) RL","(R) HD","--"]

# Map old internal location codes to the new unified location strings
_LEGACY_LOC_MAP = {
    "LT": "T", "RT": "T", "CT": "T",
    "LTR": "(R) T", "RTR": "(R) T", "CTR": "(R) T",
}
_VEHICLE_LOCATIONS= ["FR","LS","RS","RR","TU","--"]
_AC_AMMO_OPTIONS = ("Std", "Precision", "AP", "Flak", "Flechette", "Tracer")
_BA_LOCATIONS      = ["Body","Arm","TU","DWP","--"]
_AERO_LOCATIONS    = ["N","LW","RW","A","--"]


class WeaponsPanel(QWidget):
    changed = pyqtSignal()

    def __init__(self, unit_type: str = "mech", tech: str = "IS", parent=None):
        super().__init__(parent)
        self._unit_type = unit_type
        self._tech = tech
        self._is_ba = (unit_type == "ba")
        if unit_type == "mech":
            self._locations = _MECH_LOCATIONS
        elif unit_type == "ba":
            self._locations = _BA_LOCATIONS
        elif unit_type in ("aero", "fighter"):
            self._locations = _AERO_LOCATIONS
        else:
            self._locations = _VEHICLE_LOCATIONS
        self._tonnage: int = 0
        self._build_ui()
        self.changed.connect(self._run_validation)

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Toolbar
        bar = QHBoxLayout()
        add_btn = QPushButton("Add");    add_btn.clicked.connect(self._add_row)
        bar.addWidget(add_btn)
        # Auto-Group button (mech, vehicle, aero only)
        if self._unit_type in ("mech", "vehicle", "aero"):
            grp_btn = QPushButton("Auto-Group")
            grp_btn.clicked.connect(self._auto_group)
            bar.addWidget(grp_btn)
        bar.addStretch()
        layout.addLayout(bar)

        # Table
        self._table = QTableWidget(0, 6)
        self._table.setHorizontalHeaderLabels(["TIC", "Weapon", "Location", "Ammo", "OS", ""])
        hh = self._table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        self._table.setColumnWidth(0, 50)
        self._table.setColumnWidth(2, 80)
        self._table.setColumnWidth(4, 40)
        self._table.setColumnWidth(5, 52)
        layout.addWidget(self._table)

        self._errors_label = QLabel()
        self._errors_label.setWordWrap(True)
        self._errors_label.hide()
        layout.addWidget(self._errors_label)

    def _weapon_entries(self) -> list[tuple[str, str]]:
        """Return (display_label, key) tuples for current tech and BA status."""
        from ..data.weapon_lists import WEAPON_LISTS
        return [(label, key) for key, label in WEAPON_LISTS.get((self._tech, self._is_ba), ())]

    def set_tech(self, tech: str) -> None:
        """Rebuild all weapon combos when tech base changes."""
        if self._tech == tech:
            return
        self._tech = tech

        entries = self._weapon_entries()
        for row in range(self._table.rowCount()):
            old_combo = self._table.cellWidget(row, 1)
            if old_combo is None:
                continue

            saved_key = old_combo.currentData()
            saved_fcs = old_combo.property("_fcs")

            try:
                old_combo.currentIndexChanged.disconnect(self.changed)
            except TypeError:
                pass
            try:
                old_combo.currentIndexChanged.disconnect(self._update_ammo_for_weapon)
            except TypeError:
                pass

            new_combo = QComboBox()
            for display_label, weapon_key in entries:
                new_combo.addItem(display_label, weapon_key)

            idx = new_combo.findData(saved_key)
            if idx >= 0:
                new_combo.setCurrentIndex(idx)
            elif saved_key:
                new_combo.insertItem(0, saved_key, saved_key)
                new_combo.setCurrentIndex(0)

            new_combo.setProperty("_fcs", saved_fcs)
            new_combo.currentIndexChanged.connect(self.changed)
            new_combo.currentIndexChanged.connect(self._update_ammo_for_weapon)

            self._table.setCellWidget(row, 1, new_combo)

        self.changed.emit()

    def _add_row(self, weapon: UnitWeapon | None = None, target_row: int | None = None) -> None:
        if target_row is not None:
            row = target_row
            self._table.insertRow(row)
        else:
            row = self._table.rowCount()
            self._table.insertRow(row)

        # TIC spinner
        tic = QSpinBox(); tic.setRange(1, 12)
        if weapon:
            tic.setValue(weapon.tic)
        else:
            tic.setValue(self._next_available_tic())
        tic.valueChanged.connect(self.changed)
        self._table.setCellWidget(row, 0, tic)

        # Weapon combo
        wcombo = QComboBox()
        for display_name, key in self._weapon_entries():
            wcombo.addItem(display_name, key)
        if weapon:
            idx = wcombo.findData(weapon.weapon_key)
            if idx >= 0:
                wcombo.setCurrentIndex(idx)
            else:
                # Key not in _ALLOWED_WEAPONS — add it so it isn't silently
                # replaced with the first combo entry (ac2/AC/2)
                wcombo.insertItem(0, weapon.weapon_key, weapon.weapon_key)
                wcombo.setCurrentIndex(0)
        wcombo.setProperty("_fcs", weapon.fcs if weapon else None)
        wcombo.currentIndexChanged.connect(self.changed)
        wcombo.currentIndexChanged.connect(self._update_ammo_for_weapon)
        self._table.setCellWidget(row, 1, wcombo)

        # Location combo
        lcombo = QComboBox()
        lcombo.addItems(self._locations)
        if weapon:
            loc = _LEGACY_LOC_MAP.get(weapon.location, weapon.location)
            if loc in self._locations:
                lcombo.setCurrentText(loc)
        lcombo.currentIndexChanged.connect(self.changed)
        self._table.setCellWidget(row, 2, lcombo)

        # Ammo dropdown (AC weapons only)
        ammo_key = weapon.weapon_key if weapon else (wcombo.currentData() or "")
        try:
            _w_def = DataStore.weapon(ammo_key)
            _is_ac = _w_def.useAmmo == "AC"
        except (KeyError, AttributeError):
            _is_ac = False
        ammo_combo = QComboBox()
        ammo_combo.addItems(_AC_AMMO_OPTIONS)
        _initial_ammo = (weapon.ammo_type or "Std") if weapon else "Std"
        if _is_ac:
            ammo_combo.setCurrentText(_initial_ammo)
            ammo_combo.setEnabled(True)
        else:
            ammo_combo.setCurrentIndex(0)
            ammo_combo.setEnabled(False)
        ammo_combo.currentIndexChanged.connect(self._sync_ammo)
        self._table.setCellWidget(row, 3, ammo_combo)

        # One-shot check
        os_chk = QCheckBox()
        os_chk.setChecked(weapon.one_shot if weapon else False)
        os_chk.stateChanged.connect(self.changed)
        os_widget = QWidget(); os_lay = QHBoxLayout(os_widget)
        os_lay.addWidget(os_chk); os_lay.setContentsMargins(0,0,0,0)
        os_lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._table.setCellWidget(row, 4, os_widget)

        # + / X buttons — duplicate and remove this row
        dup_btn = QPushButton("+")
        dup_btn.setFixedSize(20, 20)
        dup_btn.setStyleSheet(
            "QPushButton {"
            "  color: #00aa00;"
            "  font-weight: bold;"
            "  font-size: 18px;"
            "  border: 1px solid #00aa00;"
            "  border-radius: 3px;"
            "  background: transparent;"
            "  padding: 0px;"
            "  margin: 0px;"
            "  padding-bottom: 5px;"
            "  padding-left: 0.5px;"
            "}"
            "QPushButton:hover {"
            "  background: #00aa00;"
            "  color: white;"
            "}"
        )
        dup_btn.clicked.connect(lambda checked=False, b=dup_btn: self._duplicate_btn_row(b))
        x_btn = QPushButton("X")
        x_btn.setFixedSize(20, 20)
        x_btn.setStyleSheet(
            "QPushButton {"
            "  color: #cc0000;"
            "  font-weight: bold;"
            "  font-size: 14px;"
            "  border: 1px solid #cc0000;"
            "  border-radius: 3px;"
            "  background: transparent;"
            "  padding: 0px;"
            "  margin: 0px;"
            "  padding-bottom: 2px;"
            "}"
            "QPushButton:hover {"
            "  background: #cc0000;"
            "  color: white;"
            "}"
        )
        x_btn.clicked.connect(lambda checked=False, b=x_btn: self._remove_btn_row(b))
        act_widget = QWidget(); act_lay = QHBoxLayout(act_widget)
        act_lay.addWidget(dup_btn); act_lay.addWidget(x_btn)
        act_lay.setContentsMargins(0,0,0,0); act_lay.setSpacing(4)
        act_lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._table.setCellWidget(row, 5, act_widget)

        self.changed.emit()

    def _next_available_tic(self) -> int:
        used = set()
        for row in range(self._table.rowCount()):
            tw = self._table.cellWidget(row, 0)
            if tw:
                used.add(tw.value())
        tic = 1
        while tic in used:
            tic += 1
        return tic

    def _duplicate_btn_row(self, btn: QPushButton) -> None:
        """Duplicate the weapon row containing the given + button."""
        for src_row in range(self._table.rowCount()):
            cw = self._table.cellWidget(src_row, 5)
            if cw and btn in cw.findChildren(QPushButton):
                tic_w = self._table.cellWidget(src_row, 0)
                key_w = self._table.cellWidget(src_row, 1)
                loc_w = self._table.cellWidget(src_row, 2)
                ammo_w = self._table.cellWidget(src_row, 3)
                os_w = self._table.cellWidget(src_row, 4)

                os_chk = os_w.findChild(QCheckBox) if os_w else None
                weapon_key = key_w.currentData() if key_w else ""
                if not weapon_key:
                    return

                copy = UnitWeapon(
                    weapon_key=weapon_key,
                    tic=tic_w.value() if tic_w else 1,
                    location=loc_w.currentText() if loc_w else "",
                    ammo_type=(ammo_w.currentText() if ammo_w and ammo_w.isEnabled() else ""),
                    one_shot=os_chk.isChecked() if os_chk else False,
                    fcs=key_w.property("_fcs") if key_w else None,
                )
                self._add_row(copy, target_row=src_row + 1)
                break

    def _remove_btn_row(self, btn: QPushButton) -> None:
        """Remove the table row containing the given X button."""
        for row in range(self._table.rowCount()):
            cw = self._table.cellWidget(row, 5)
            if cw and btn in cw.findChildren(QPushButton):
                self._table.removeRow(row)
                break
        self.changed.emit()

    def _auto_group(self) -> None:
        from ..engine.tic_grouper import ResolvedWeapon, auto_assign_tics
        from ..models.data_store import DataStore

        weapons = self.get_weapons()
        if not weapons:
            return

        resolved = []
        for uw in weapons:
            try:
                w = DataStore.weapon(uw.weapon_key)
            except KeyError:
                continue
            resolved.append(ResolvedWeapon(
                unit_weapon=uw, weapon=w, tic=uw.tic,
                location=uw.location, ammo_type=uw.ammo_type,
                one_shot=uw.one_shot, tonnage=self._tonnage,
            ))

        assigned = auto_assign_tics(resolved)
        for row in range(self._table.rowCount()):
            if row >= len(assigned):
                break
            tic_w = self._table.cellWidget(row, 0)
            if tic_w:
                tic_w.setValue(assigned[row].tic)
        self.changed.emit()

    def _update_ammo_for_weapon(self) -> None:
        sender = self.sender()
        for r in range(self._table.rowCount()):
            if self._table.cellWidget(r, 1) is sender:
                key_w = self._table.cellWidget(r, 1)
                ammo_w = self._table.cellWidget(r, 3)
                if not key_w or not ammo_w:
                    break
                try:
                    w = DataStore.weapon(key_w.currentData())
                    is_ac = w.useAmmo == "AC"
                except (KeyError, AttributeError):
                    is_ac = False
                ammo_w.blockSignals(True)
                ammo_w.setEnabled(is_ac)
                if not is_ac:
                    ammo_w.setCurrentIndex(0)
                ammo_w.blockSignals(False)
                break

    def _sync_ammo(self) -> None:
        sender = self.sender()
        if not sender or not sender.isEnabled():
            self.changed.emit()
            return
        ammo = sender.currentText()
        if ammo not in ("Precision", "AP", "Flak"):
            self.changed.emit()
            return
        sender_row = -1
        sender_tic = None
        for r in range(self._table.rowCount()):
            if self._table.cellWidget(r, 3) is sender:
                sender_row = r
                tic_w = self._table.cellWidget(r, 0)
                if tic_w:
                    sender_tic = tic_w.value()
                break
        if sender_tic is None:
            self.changed.emit()
            return
        for r in range(self._table.rowCount()):
            if r == sender_row:
                continue
            tic_w = self._table.cellWidget(r, 0)
            ammo_w = self._table.cellWidget(r, 3)
            if tic_w and ammo_w and ammo_w.isEnabled() and tic_w.value() == sender_tic:
                ammo_w.blockSignals(True)
                ammo_w.setCurrentText(ammo)
                ammo_w.blockSignals(False)
        self.changed.emit()

    def get_weapons(self) -> list[UnitWeapon]:
        weapons = []
        for row in range(self._table.rowCount()):
            tic_w  = self._table.cellWidget(row, 0)
            key_w  = self._table.cellWidget(row, 1)
            loc_w  = self._table.cellWidget(row, 2)
            ammo_w  = self._table.cellWidget(row, 3)
            os_w   = self._table.cellWidget(row, 4)

            key = key_w.currentData() if key_w else ""
            if not key:
                continue

            os_chk = os_w.findChild(QCheckBox) if os_w else None
            weapons.append(UnitWeapon(
                weapon_key=key,
                tic=tic_w.value() if tic_w else 1,
                location=loc_w.currentText() if loc_w else "",
                ammo_type=(ammo_w.currentText() if ammo_w and ammo_w.isEnabled() else ""),
                one_shot=os_chk.isChecked() if os_chk else False,
                fcs=key_w.property("_fcs") if key_w else None,
            ))
        return weapons

    def set_tonnage(self, tonnage: int) -> None:
        self._tonnage = tonnage
        self._run_validation()

    def _run_validation(self) -> None:
        try:
            resolved: list[ResolvedWeapon] = []
            for uw in self.get_weapons():
                try:
                    w = DataStore.weapon(uw.weapon_key)
                except KeyError:
                    continue
                resolved.append(ResolvedWeapon(
                    unit_weapon=uw,
                    weapon=w,
                    tic=uw.tic,
                    location=uw.location,
                    ammo_type=uw.ammo_type,
                    one_shot=uw.one_shot,
                    tonnage=self._tonnage,
                ))
            errors = validate_tic_assignments(resolved)
        except Exception:
            errors = []

        if errors:
            self._errors_label.setText("\n".join(errors))
            if ThemeManager.is_dark():
                self._errors_label.setStyleSheet(
                    "color: #ff6b6b; background: #3d1f1f; border: 1px solid #cc5555; "
                    "border-radius: 3px; padding: 4px; font-size: 11px;"
                )
            else:
                self._errors_label.setStyleSheet(
                    "color: #cc0000; background: #fff0f0; border: 1px solid #cc0000; "
                    "border-radius: 3px; padding: 4px; font-size: 11px;"
                )
            self._errors_label.show()
        else:
            self._errors_label.hide()

    def load_weapons(self, weapons: list[UnitWeapon]) -> None:
        self._table.setRowCount(0)
        for w in weapons:
            self._add_row(w)
