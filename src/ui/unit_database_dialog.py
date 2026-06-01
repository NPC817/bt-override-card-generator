"""Unit Database dialog — browse bundled .ovr files from data/units.zip."""
from __future__ import annotations
import json
import zipfile
from pathlib import Path
from typing import Any

from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtWidgets import (
    QComboBox, QDialog, QDialogButtonBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMessageBox,
    QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout,
)

from ..utils.paths import resource_path as _resource_path
_ZIP_PATH = _resource_path("data", "units.zip")
_TONLESS_TYPES = {"BattleArmor", "Infantry"}

_TYPE_MAP_CACHE: dict[str, Any] = {}


def _get_type_map() -> dict[str, Any]:
    if not _TYPE_MAP_CACHE:
        from ..models.mech import BattleMech
        from ..models.vehicle import CombatVehicle
        from ..models.aero import AeroSpaceFighter
        from ..models.battle_armor import BattleArmor
        from ..models.infantry import Infantry
        _TYPE_MAP_CACHE.update({
            "BattleMech": BattleMech,
            "CombatVehicle": CombatVehicle,
            "AeroSpaceFighter": AeroSpaceFighter,
            "BattleArmor": BattleArmor,
            "Infantry": Infantry,
        })
    return _TYPE_MAP_CACHE


class _NumericItem(QTableWidgetItem):
    """QTableWidgetItem that sorts by numeric UserRole value."""
    def __lt__(self, other: QTableWidgetItem) -> bool:
        try:
            return float(self.data(Qt.ItemDataRole.UserRole)) < float(
                other.data(Qt.ItemDataRole.UserRole)
            )
        except (TypeError, ValueError):
            return super().__lt__(other)


class UnitDatabaseDialog(QDialog):
    """Browseable database of pre-built .ovr units stored in data/units.zip."""

    unit_selected = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Unit Database")
        self.setMinimumSize(700, 500)

        self._records: list[dict] = []
        self._filtered: list[dict] = []

        self._build_ui()
        QTimer.singleShot(0, self._load_records)

    # ── UI construction ───────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)

        # Row 1: text search + type + tech filters
        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Search:"))
        self._search_edit = QLineEdit()
        self._search_edit.setPlaceholderText("Chassis / name…")
        row1.addWidget(self._search_edit, stretch=2)
        row1.addWidget(QLabel("Type:"))
        self._type_combo = QComboBox()
        self._type_combo.addItems([
            "All", "BattleMech", "CombatVehicle", "AeroSpaceFighter",
            "BattleArmor", "Infantry",
        ])
        row1.addWidget(self._type_combo, stretch=1)
        row1.addWidget(QLabel("Tech:"))
        self._tech_combo = QComboBox()
        self._tech_combo.addItems(["All", "IS", "Clan", "Mixed"])
        row1.addWidget(self._tech_combo, stretch=1)
        root.addLayout(row1)

        # Row 2: tonnage range
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Tonnage:"))
        self._ton_min = QSpinBox()
        self._ton_min.setRange(0, 999)
        self._ton_min.setValue(0)
        self._ton_min.setSpecialValueText("—")
        row2.addWidget(self._ton_min)
        row2.addWidget(QLabel("to"))
        self._ton_max = QSpinBox()
        self._ton_max.setRange(0, 999)
        self._ton_max.setValue(0)
        self._ton_max.setSpecialValueText("—")
        row2.addWidget(self._ton_max)
        row2.addStretch()
        root.addLayout(row2)

        # Results table
        self._table = QTableWidget(0, 4)
        self._table.setHorizontalHeaderLabels(["Name", "Type", "Tech", "Tonnage"])
        hh = self._table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        self._table.setColumnWidth(1, 130)
        self._table.setColumnWidth(2, 70)
        self._table.setColumnWidth(3, 80)
        self._table.setSortingEnabled(True)
        self._table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        root.addWidget(self._table)

        # Status label
        self._status_label = QLabel("Loading…")
        root.addWidget(self._status_label)

        # Dialog buttons
        self._button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        self._load_btn = self._button_box.addButton(
            "Load", QDialogButtonBox.ButtonRole.ActionRole
        )
        self._load_btn.setEnabled(False)
        self._load_close_btn = self._button_box.addButton(
            "Load and Close", QDialogButtonBox.ButtonRole.AcceptRole
        )
        self._load_close_btn.setEnabled(False)
        root.addWidget(self._button_box)

        # Signal wiring
        self._search_edit.textChanged.connect(self._apply_filter)
        self._type_combo.currentIndexChanged.connect(self._apply_filter)
        self._tech_combo.currentIndexChanged.connect(self._apply_filter)
        self._ton_min.valueChanged.connect(self._apply_filter)
        self._ton_max.valueChanged.connect(self._apply_filter)
        self._table.itemSelectionChanged.connect(self._on_selection_changed)
        self._table.cellActivated.connect(lambda: self._load_selected(close_after=True))
        self._load_btn.clicked.connect(lambda: self._load_selected(close_after=False))
        self._load_close_btn.clicked.connect(lambda: self._load_selected(close_after=True))
        self._button_box.rejected.connect(self.reject)

    # ── Zip loading ───────────────────────────────────────────────────────────

    def _load_records(self) -> None:
        if not _ZIP_PATH.exists():
            self._records = []
            self._update_status("data/units.zip not found — no bundled units available.")
            return

        records: list[dict] = []
        try:
            with zipfile.ZipFile(_ZIP_PATH, "r") as zf:
                for name in zf.namelist():
                    if not name.lower().endswith(".ovr"):
                        continue
                    try:
                        data = json.loads(zf.read(name).decode("utf-8"))
                        if isinstance(data, dict) and data.get("unit_type") in _get_type_map():
                            records.append(data)
                    except Exception:
                        pass
        except zipfile.BadZipFile as exc:
            self._records = []
            self._update_status(f"Could not open units.zip: {exc}")
            return

        self._records = records
        self._apply_filter()

    # ── Filtering ─────────────────────────────────────────────────────────────

    def _apply_filter(self) -> None:
        text = self._search_edit.text().strip().lower()
        selected_type = self._type_combo.currentText()
        selected_tech = self._tech_combo.currentText()
        ton_min = self._ton_min.value()
        ton_max = self._ton_max.value()

        filtered: list[dict] = []
        for rec in self._records:
            if text:
                name_lower = (
                    rec.get("chassis", "") + " " + rec.get("variant", "")
                ).lower()
                if text not in name_lower:
                    continue
            if selected_type != "All" and rec.get("unit_type", "") != selected_type:
                continue
            if selected_tech != "All" and rec.get("tech", "") != selected_tech:
                continue
            tonnage = int(rec.get("tonnage", 0))
            if ton_min > 0 and tonnage < ton_min:
                continue
            if ton_max > 0 and tonnage > ton_max:
                continue
            filtered.append(rec)

        self._filtered = filtered
        self._populate_table()

    # ── Table population ──────────────────────────────────────────────────────

    def _populate_table(self) -> None:
        self._table.setSortingEnabled(False)
        self._table.setRowCount(0)

        for idx, rec in enumerate(self._filtered):
            chassis = rec.get("chassis", "")
            variant = rec.get("variant", "")
            display_name = f"{chassis} {variant}".strip().upper() or "UNNAMED UNIT"
            unit_type = rec.get("unit_type", "")
            tech = rec.get("tech", "")
            tonnage_raw = int(rec.get("tonnage", 0))
            tonnage_str = (
                "N/A"
                if tonnage_raw == 0 and unit_type in _TONLESS_TYPES
                else str(tonnage_raw)
            )

            row = self._table.rowCount()
            self._table.insertRow(row)

            name_item = QTableWidgetItem(display_name)
            name_item.setData(Qt.ItemDataRole.UserRole, idx)
            self._table.setItem(row, 0, name_item)
            self._table.setItem(row, 1, QTableWidgetItem(unit_type))
            self._table.setItem(row, 2, QTableWidgetItem(tech))

            ton_item = _NumericItem()
            ton_item.setData(Qt.ItemDataRole.DisplayRole, tonnage_str)
            ton_item.setData(Qt.ItemDataRole.UserRole, tonnage_raw)
            self._table.setItem(row, 3, ton_item)

        self._table.setSortingEnabled(True)
        self._load_btn.setEnabled(False)
        self._load_close_btn.setEnabled(False)
        self._update_status(f"{len(self._filtered)} unit(s) found.")

    # ── Selection + load ──────────────────────────────────────────────────────

    def _on_selection_changed(self) -> None:
        has_selection = bool(self._table.selectedItems())
        self._load_btn.setEnabled(has_selection)
        self._load_close_btn.setEnabled(has_selection)

    def _load_selected(self, *_, close_after: bool = False) -> None:
        rows = self._table.selectionModel().selectedRows()
        if not rows:
            return

        name_item = self._table.item(rows[0].row(), 0)
        if name_item is None:
            return
        filtered_idx = name_item.data(Qt.ItemDataRole.UserRole)
        if filtered_idx is None or filtered_idx >= len(self._filtered):
            return

        rec = self._filtered[filtered_idx]
        unit_type = rec.get("unit_type", "")
        cls = _get_type_map().get(unit_type)
        if cls is None:
            QMessageBox.warning(
                self, "Load Error",
                f"Unknown unit_type '{unit_type}' — cannot reconstruct unit."
            )
            return

        try:
            unit = cls.from_dict(rec)
        except Exception as exc:
            QMessageBox.critical(self, "Load Error", f"Failed to load unit:\n{exc}")
            return

        self.unit_selected.emit(unit)
        if close_after:
            self.accept()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _update_status(self, text: str) -> None:
        self._status_label.setText(text)
