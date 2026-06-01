"""Placeholder form for unit types not yet implemented."""
from __future__ import annotations
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class GenericForm(QWidget):
    changed = pyqtSignal()

    def __init__(self, unit_type: str, parent=None):
        super().__init__(parent)
        self._unit = None
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"{unit_type} form coming soon."))
        layout.addStretch()

    def load_unit(self, unit) -> None:
        self._unit = unit

    def get_unit(self):
        return self._unit
