"""
Equipment panel: QTableWidget for equipment entries.
Columns: Equipment (always), Location (if hasLoc), Subtype (if subtypes), Uses (if isLimited)
"""
from __future__ import annotations
import logging

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QComboBox, QDoubleSpinBox, QHBoxLayout, QHeaderView, QPushButton,
    QTableWidget, QVBoxLayout, QWidget,
)

from ..models.unit import UnitEquipment
from ..models.data_store import DataStore
from ..models.equipment import Equipment

_LOCS = ["LA", "RA", "LL", "RL", "T", "CT", "LT", "RT", "HD", "H", "All"]


class EquipmentPanel(QWidget):
    changed = pyqtSignal()
    _EQ_ENTRIES_CACHE: list[tuple[str, str]] | None = None

    def __init__(self, parent=None, unit_type: str = "generic"):
        super().__init__(parent)
        self._unit_type = unit_type
        self._building = False
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        bar = QHBoxLayout()
        add_btn = QPushButton("Add");    add_btn.clicked.connect(self._add_row)
        bar.addWidget(add_btn); bar.addStretch()
        layout.addLayout(bar)

        self._table = QTableWidget(0, 5)
        self._table.setHorizontalHeaderLabels(["Equipment", "Loc", "Subtype", "Uses", ""])
        hh = self._table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        self._table.setColumnWidth(1, 60)
        self._table.setColumnWidth(2, 100)
        self._table.setColumnWidth(3, 60)
        self._table.setColumnWidth(4, 30)
        self._update_column_visibility()
        layout.addWidget(self._table)

    def _eq_entries(self) -> list[tuple[str, str]]:
        """Return sorted list of (fullname, key) tuples."""
        if EquipmentPanel._EQ_ENTRIES_CACHE is None:
            try:
                equipment = DataStore.all_equipment()
                entries = [(eq.fullname, key) for key, eq in equipment.items()]
                entries.sort(key=lambda e: e[0].lower())
                EquipmentPanel._EQ_ENTRIES_CACHE = entries
            except Exception as exc:
                logging.exception("Failed to load equipment entries: %s", exc)
                return []
        return EquipmentPanel._EQ_ENTRIES_CACHE

    def _eq_obj(self, key: str) -> Equipment | None:
        try:
            return DataStore.equipment(key)
        except KeyError:
            return None

    def _update_column_visibility(self) -> None:
        show_loc = False
        show_sub = False
        show_uses = False
        if self._unit_type != "ba":
            for row in range(self._table.rowCount()):
                eq_w = self._table.cellWidget(row, 0)
                if not eq_w:
                    continue
                key = eq_w.currentData()
                if not key:
                    continue
                if eq := self._eq_obj(key):
                    if eq.hasLoc:
                        show_loc = True
                    if eq.subtypes:
                        show_sub = True
                    if eq.isLimited:
                        show_uses = True
        else:
            # BA: location never shown; subtypes and uses still checked
            for row in range(self._table.rowCount()):
                eq_w = self._table.cellWidget(row, 0)
                if not eq_w:
                    continue
                key = eq_w.currentData()
                if not key:
                    continue
                if eq := self._eq_obj(key):
                    if eq.subtypes:
                        show_sub = True
                    if eq.isLimited:
                        show_uses = True
        self._table.setColumnHidden(1, not show_loc)
        self._table.setColumnHidden(2, not show_sub)
        self._table.setColumnHidden(3, not show_uses)

    def _add_row(self, eq: UnitEquipment | None = None) -> None:
        was_building = self._building
        self._building = True
        row = self._table.rowCount()
        self._table.insertRow(row)

        # Equipment combo — display fullname, store key as userData
        eq_combo = QComboBox()
        for display_name, key in self._eq_entries():
            eq_combo.addItem(display_name, key)
        if eq:
            idx = eq_combo.findData(eq.equipment_key)
            if idx >= 0:
                eq_combo.setCurrentIndex(idx)
        eq_combo.currentIndexChanged.connect(lambda: self._on_eq_changed(row))
        self._table.setCellWidget(row, 0, eq_combo)

        # Loc widget (col 1): combo for location picker
        loc_combo = QComboBox(); loc_combo.addItems([""] + _LOCS)
        loc_combo.setEditable(True)
        loc_combo.currentTextChanged.connect(self.changed.emit)
        self._table.setCellWidget(row, 1, loc_combo)

        # Subtype widget (col 2): combo populated based on equipment
        sub_combo = QComboBox()
        sub_combo.currentTextChanged.connect(self.changed.emit)
        self._table.setCellWidget(row, 2, sub_combo)

        # Uses widget (col 3): spin box (float for transporter capacities)
        uses_spin = QDoubleSpinBox(); uses_spin.setRange(0.0, 999999.0)
        uses_spin.setDecimals(1)
        uses_spin.valueChanged.connect(self.changed.emit)
        self._table.setCellWidget(row, 3, uses_spin)

        # X button — remove this row
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
        x_widget = QWidget(); x_lay = QHBoxLayout(x_widget)
        x_lay.addWidget(x_btn); x_lay.setContentsMargins(0,0,0,0)
        x_lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._table.setCellWidget(row, 4, x_widget)

        self._refresh_row(row, set_defaults=(eq is None))
        # Restore saved values after refresh populates combos
        if eq:
            loc_w = self._table.cellWidget(row, 1)
            sub_w = self._table.cellWidget(row, 2)
            uses_w = self._table.cellWidget(row, 3)
            if loc_w and eq.location:
                loc_w.setCurrentText(eq.location)
            if sub_w and eq.subtype:
                idx = sub_w.findData(eq.subtype)
                if idx >= 0:
                    sub_w.setCurrentIndex(idx)
            if uses_w:
                uses_w.setValue(eq.uses)
        self._building = was_building
        if not self._building:
            self.changed.emit()

    def _on_eq_changed(self, row: int) -> None:
        if self._building:
            return
        self._refresh_row(row, set_defaults=True)
        self.changed.emit()

    def _refresh_row(self, row: int, set_defaults: bool = False) -> None:
        eq_w = self._table.cellWidget(row, 0)
        loc_w = self._table.cellWidget(row, 1)
        sub_w = self._table.cellWidget(row, 2)
        uses_w = self._table.cellWidget(row, 3)
        if not eq_w:
            return

        key = eq_w.currentData()
        eq_obj = self._eq_obj(key) if key else None

        if self._unit_type != "ba" and eq_obj and eq_obj.hasLoc:
            loc_w.setVisible(True)
            loc_w.setEnabled(True)
            if set_defaults:
                default_loc = eq_obj.fixedLocation or ""
                loc_w.setCurrentText(default_loc)
        else:
            loc_w.setVisible(False)
            loc_w.setEnabled(False)

        if eq_obj and eq_obj.subtypes:
            sub_w.setVisible(True)
            sub_w.setEnabled(True)
            sub_w.blockSignals(True)
            sub_w.clear()
            sub_w.addItem("")
            first_key = None
            for skey, sname in eq_obj.subtypes.items():
                sub_w.addItem(sname, skey)
                if first_key is None:
                    first_key = skey
            sub_w.blockSignals(False)
            if set_defaults and first_key:
                idx = sub_w.findData(first_key)
                if idx >= 0:
                    sub_w.setCurrentIndex(idx)
        else:
            sub_w.setVisible(False)
            sub_w.setEnabled(False)

        if eq_obj and eq_obj.isLimited:
            uses_w.setVisible(True)
            uses_w.setEnabled(True)
            if set_defaults:
                uses_w.setValue(1)
        else:
            uses_w.setVisible(False)
            uses_w.setEnabled(False)

        self._update_column_visibility()

    def _remove_btn_row(self, btn: QPushButton) -> None:
        """Remove the table row containing the given X button."""
        for row in range(self._table.rowCount()):
            cw = self._table.cellWidget(row, 4)
            if cw and cw.findChild(QPushButton) is btn:
                self._table.removeRow(row)
                break
        self._update_column_visibility()
        self.changed.emit()

    def get_equipment(self) -> list[UnitEquipment]:
        result = []
        for row in range(self._table.rowCount()):
            eq_w = self._table.cellWidget(row, 0)
            loc_w = self._table.cellWidget(row, 1)
            sub_w = self._table.cellWidget(row, 2)
            uses_w = self._table.cellWidget(row, 3)

            key = eq_w.currentData() if eq_w else ""
            if not key:
                continue
            loc_val = loc_w.currentText() if loc_w else ""
            sub_val = ""
            if sub_w:
                sub_val = sub_w.currentData() or sub_w.currentText()
            result.append(UnitEquipment(
                equipment_key=key,
                location=loc_val,
                subtype=sub_val,
                uses=uses_w.value() if uses_w else 0,
            ))
        return result

    def load_equipment(self, equipment: list[UnitEquipment]) -> None:
        self._building = True
        self._table.setRowCount(0)
        for eq in equipment:
            self._add_row(eq)
        self._update_column_visibility()
        self._building = False
