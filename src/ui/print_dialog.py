"""Print queue dialog: reordering, layout selection, QPrintPreviewDialog."""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QCheckBox, QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QToolButton,
    QVBoxLayout,
)

# (label, cols, rows, cards_per_page)
PRINT_LAYOUTS: list[tuple[str, int, int, int]] = [
    ("1 per page",  1, 1, 1),
    ("2 per page",  1, 2, 2),
    ("3 per page",  1, 3, 3),
    ("4 per page",  2, 2, 4),
    ("6 per page",  2, 3, 6),
    ("8 per page",  2, 4, 8),
]

ORIENTATIONS: list[str] = ["Portrait", "Landscape"]

# (label, key)
PAGE_SIZES: list[tuple[str, str]] = [
    ("Letter", "Letter"),
    ("A4",     "A4"),
    ("A5",     "A5"),
    ("A6",     "A6"),
]



class PrintQueueDialog(QDialog):
    """Print queue with drag-free reordering and multi-card layout selection."""

    def __init__(self, items: list[tuple[str, QPixmap]], parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Print Queue")
        self.setMinimumWidth(440)
        self.setMinimumHeight(360)
        self._build_ui()
        for name, pixmap in items:
            item = QListWidgetItem(name)
            item.setData(Qt.ItemDataRole.UserRole, pixmap)
            self._list.addItem(item)
        if self._list.count():
            self._list.setCurrentRow(0)
        self._update_buttons()

    # ── UI construction ───────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)

        root.addWidget(QLabel("Selected Units:"))

        # List + reorder buttons side by side
        row = QHBoxLayout()

        btn_col = QVBoxLayout()
        self._btn_top  = self._make_btn("⇑", "Move to top",    btn_col)
        self._btn_up   = self._make_btn("↑", "Move up",        btn_col)
        self._btn_dn   = self._make_btn("↓", "Move down",      btn_col)
        self._btn_bot  = self._make_btn("⇓", "Move to bottom", btn_col)
        btn_col.addStretch()
        row.addLayout(btn_col)

        self._list = QListWidget()
        self._list.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self._list.currentRowChanged.connect(self._update_buttons)
        row.addWidget(self._list, 1)
        root.addLayout(row)

        # Layout (cards per page)
        layout_row = QHBoxLayout()
        layout_row.addWidget(QLabel("Layout:"))
        self._combo = QComboBox()
        for cfg in PRINT_LAYOUTS:
            self._combo.addItem(cfg[0])
        layout_row.addWidget(self._combo, 1)
        root.addLayout(layout_row)

        # Orientation
        orient_row = QHBoxLayout()
        orient_row.addWidget(QLabel("Orientation:"))
        self._orient_combo = QComboBox()
        self._orient_combo.addItems(ORIENTATIONS)
        orient_row.addWidget(self._orient_combo, 1)
        root.addLayout(orient_row)

        # Page size
        size_row = QHBoxLayout()
        size_row.addWidget(QLabel("Page Size:"))
        self._size_combo = QComboBox()
        for label, _ in PAGE_SIZES:
            self._size_combo.addItem(label)
        size_row.addWidget(self._size_combo, 1)
        root.addLayout(size_row)

        # Card size
        card_size_row = QHBoxLayout()
        card_size_row.addWidget(QLabel("Card Size:"))
        self._card_w_spin = QDoubleSpinBox()
        self._card_w_spin.setRange(0.5, 20.0)
        self._card_w_spin.setSingleStep(0.25)
        self._card_w_spin.setDecimals(2)
        self._card_w_spin.setSuffix(" in")
        self._card_w_spin.setValue(6.0)
        card_size_row.addWidget(self._card_w_spin)
        card_size_row.addWidget(QLabel("×"))
        self._card_h_spin = QDoubleSpinBox()
        self._card_h_spin.setRange(0.5, 20.0)
        self._card_h_spin.setSingleStep(0.25)
        self._card_h_spin.setDecimals(2)
        self._card_h_spin.setSuffix(" in")
        self._card_h_spin.setValue(4.0)
        card_size_row.addWidget(self._card_h_spin)
        self._fill_check = QCheckBox("Fill")
        self._fill_check.setChecked(True)
        self._fill_check.toggled.connect(self._on_fill_toggled)
        card_size_row.addWidget(self._fill_check)
        card_size_row.addStretch()
        root.addLayout(card_size_row)
        self._on_fill_toggled(True)

        # Cut lines toggle
        self._cut_lines_check = QCheckBox("Show Cut Lines")
        root.addWidget(self._cut_lines_check)

        # Buttons
        bb = QDialogButtonBox()
        bb.addButton("Print…", QDialogButtonBox.ButtonRole.AcceptRole)
        bb.addButton(QDialogButtonBox.StandardButton.Cancel)
        bb.accepted.connect(self._do_print)
        bb.rejected.connect(self.reject)
        root.addWidget(bb)

        self._btn_top.clicked.connect(self._move_top)
        self._btn_up.clicked.connect(self._move_up)
        self._btn_dn.clicked.connect(self._move_down)
        self._btn_bot.clicked.connect(self._move_bottom)

    @staticmethod
    def _make_btn(text: str, tooltip: str, layout: QVBoxLayout) -> QToolButton:
        b = QToolButton()
        b.setText(text)
        b.setToolTip(tooltip)
        b.setFixedSize(28, 28)
        layout.addWidget(b)
        return b

    # ── Reorder logic ─────────────────────────────────────────────────────────

    def _update_buttons(self) -> None:
        r = self._list.currentRow()
        n = self._list.count()
        self._btn_top.setEnabled(r > 0)
        self._btn_up.setEnabled(r > 0)
        self._btn_dn.setEnabled(0 <= r < n - 1)
        self._btn_bot.setEnabled(0 <= r < n - 1)

    def _move_top(self) -> None:
        r = self._list.currentRow()
        if r > 0:
            self._jump(r, 0)

    def _move_up(self) -> None:
        r = self._list.currentRow()
        if r > 0:
            self._jump(r, r - 1)

    def _move_down(self) -> None:
        r = self._list.currentRow()
        if 0 <= r < self._list.count() - 1:
            self._jump(r, r + 1)

    def _move_bottom(self) -> None:
        r = self._list.currentRow()
        n = self._list.count()
        if 0 <= r < n - 1:
            self._jump(r, n - 1)

    def _jump(self, src: int, dst: int) -> None:
        item = self._list.takeItem(src)
        self._list.insertItem(dst, item)
        self._list.setCurrentRow(dst)

    def _on_fill_toggled(self, checked: bool) -> None:
        """Disable W/H fields when Fill is checked."""
        self._card_w_spin.setEnabled(not checked)
        self._card_h_spin.setEnabled(not checked)

    # ── Print ─────────────────────────────────────────────────────────────────

    def _do_print(self) -> None:
        from PyQt6.QtCore import QMarginsF
        from PyQt6.QtGui import QPageLayout, QPageSize
        from PyQt6.QtPrintSupport import QPrinter, QPrintPreviewDialog
        from ..renderer.pdf_exporter import render_cards_to_printer

        layout_cfg = PRINT_LAYOUTS[self._combo.currentIndex()]

        # Orientation
        landscape = self._orient_combo.currentIndex() == 1
        orientation = QPageLayout.Orientation.Landscape if landscape else QPageLayout.Orientation.Portrait

        # Page size — use Qt/IANA PPD key strings for named sizes so the
        # printer driver receives a recognized ID rather than a custom dimension
        size_key = PAGE_SIZES[self._size_combo.currentIndex()][1]
        page_size_map: dict[str, QPageSize] = {
            "Letter": QPageSize(QPageSize.PageSizeId.Letter),
            "A4":     QPageSize(QPageSize.PageSizeId.A4),
            "A5":     QPageSize(QPageSize.PageSizeId.A5),
            "A6":     QPageSize(QPageSize.PageSizeId.A6),
        }
        page_size = page_size_map.get(size_key, QPageSize(QPageSize.PageSizeId.Letter))

        pixmaps = [
            self._list.item(i).data(Qt.ItemDataRole.UserRole)
            for i in range(self._list.count())
        ]

        # Set size + orientation + margins atomically via QPageLayout
        page_layout = QPageLayout(
            page_size,
            orientation,
            QMarginsF(6.0, 6.0, 6.0, 6.0),
            QPageLayout.Unit.Millimeter,
        )

        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setPageLayout(page_layout)

        preview = QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(
            lambda p: render_cards_to_printer(
                pixmaps, layout_cfg, p,
                show_cut_lines=self._cut_lines_check.isChecked(),
                card_size_inches=None if self._fill_check.isChecked()
                else (self._card_w_spin.value(), self._card_h_spin.value()),
            )
        )
        preview.exec()
