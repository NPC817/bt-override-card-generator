"""Bulk import/export dialog with QThread-based processing and progress bar."""
from __future__ import annotations
import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QDialog, QDialogButtonBox, QFileDialog,
    QHBoxLayout, QLabel, QLineEdit, QListWidget, QMessageBox,
    QProgressDialog, QPushButton, QVBoxLayout,
)

from ..settings.profile_manager import ProfileManager


class BulkDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Bulk Import / Export")
        self.setMinimumSize(640, 440)
        self._files: list[str] = []
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)

        # File selection buttons
        file_row = QHBoxLayout()
        self._add_files_btn  = QPushButton("Add Files…")
        self._add_folder_btn = QPushButton("Add Folder…")
        self._clear_btn      = QPushButton("Clear List")
        file_row.addWidget(self._add_files_btn)
        file_row.addWidget(self._add_folder_btn)
        file_row.addWidget(self._clear_btn)
        file_row.addStretch()
        layout.addLayout(file_row)

        self._file_list = QListWidget()
        layout.addWidget(self._file_list)

        self._count_label = QLabel("0 files selected")
        layout.addWidget(self._count_label)

        # Output folder
        out_row = QHBoxLayout()
        out_row.addWidget(QLabel("Output folder:"))
        self._out_edit   = QLineEdit()
        self._out_browse = QPushButton("Browse…")
        out_row.addWidget(self._out_edit)
        out_row.addWidget(self._out_browse)
        layout.addLayout(out_row)

        # Profile
        prof_row = QHBoxLayout()
        prof_row.addWidget(QLabel("Profile:"))
        self._profile_combo = QComboBox()
        self._profile_combo.addItems(ProfileManager.all_names())
        # Pre-select active profile
        idx = self._profile_combo.findText(ProfileManager._active_name)
        if idx >= 0:
            self._profile_combo.setCurrentIndex(idx)
        prof_row.addWidget(self._profile_combo)
        prof_row.addStretch()
        layout.addLayout(prof_row)

        # Format
        fmt_row = QHBoxLayout()
        fmt_row.addWidget(QLabel("Format:"))
        self._fmt_combo = QComboBox()
        self._fmt_combo.addItems(["PNG", "PDF", "All", "OVR"])
        fmt_row.addWidget(self._fmt_combo)
        fmt_row.addStretch()
        layout.addLayout(fmt_row)

        # Dialog buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.button(QDialogButtonBox.StandardButton.Ok).setText("Start Export")
        buttons.accepted.connect(self._start)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        # Wire signals
        self._add_files_btn.clicked.connect(self._add_files)
        self._add_folder_btn.clicked.connect(self._add_folder)
        self._clear_btn.clicked.connect(self._clear)
        self._out_browse.clicked.connect(self._browse_out)

    # ── File selection ────────────────────────────────────────────────────────

    def _add_files(self) -> None:
        paths, _ = QFileDialog.getOpenFileNames(
            self, "Select Files", filter="MegaMek Files (*.mtf *.blk)"
        )
        self._add_paths(paths)

    def _add_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if not folder:
            return
        paths = []
        for root, _, files in os.walk(folder):
            for f in files:
                if f.lower().endswith((".mtf", ".blk")):
                    paths.append(os.path.join(root, f))
        self._add_paths(paths)

    def _add_paths(self, paths: list[str]) -> None:
        for p in paths:
            if p not in self._files:
                self._files.append(p)
                self._file_list.addItem(p)
        self._count_label.setText(f"{len(self._files)} files selected")

    def _clear(self) -> None:
        self._files.clear()
        self._file_list.clear()
        self._count_label.setText("0 files selected")

    def _browse_out(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, "Output Folder")
        if folder:
            self._out_edit.setText(folder)

    # ── Export ────────────────────────────────────────────────────────────────

    def _start(self) -> None:
        out_dir = self._out_edit.text().strip()
        if not out_dir or not os.path.isdir(out_dir):
            QMessageBox.warning(self, "Error", "Please select a valid output folder.")
            return
        if not self._files:
            QMessageBox.warning(self, "Error", "No files selected.")
            return

        fmt          = self._fmt_combo.currentText()
        profile_name = self._profile_combo.currentText()

        # Progress dialog
        progress = QProgressDialog(
            "Preparing…", "Cancel", 0, len(self._files), self
        )
        progress.setWindowTitle("Converting to OVR" if fmt == "OVR" else "Exporting Cards")
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.setMinimumDuration(0)
        progress.setValue(0)

        # Collect results
        results: list = []

        from ..engine.batch_processor import BatchProcessor
        worker = BatchProcessor(self._files, out_dir, profile_name, fmt, parent=self)

        def on_progress(current: int, total: int, fname: str) -> None:
            progress.setLabelText(f"Processing {fname} ({current}/{total})")
            progress.setValue(current - 1)
            QApplication.processEvents()

        def on_file_done(result) -> None:
            results.append(result)

        def on_finished() -> None:
            progress.setValue(len(self._files))

        worker.progress.connect(on_progress)
        worker.file_done.connect(on_file_done)
        worker.finished_all.connect(on_finished)
        progress.canceled.connect(worker.cancel)

        worker.start()

        # Spin until worker done (progress dialog stays responsive via processEvents)
        while worker.isRunning():
            QApplication.processEvents()

        worker.wait()
        progress.close()

        self._show_report(results, out_dir, fmt)
        self.accept()

    def _show_report(self, results: list, out_dir: str, fmt: str = "") -> None:
        succeeded  = sum(1 for r in results if r.success)
        failed     = [r for r in results if not r.success]
        warned     = [r for r in results if r.success and r.warnings]

        msg = f"Done: {succeeded} succeeded, {len(failed)} failed, {len(warned)} with warnings."

        if failed:
            msg += "\n\nErrors:\n"
            for r in failed[:15]:
                msg += f"  {os.path.basename(r.path)}: {r.error}\n"
            if len(failed) > 15:
                msg += f"  … and {len(failed) - 15} more."

        if warned:
            msg += "\n\nWarnings:\n"
            for r in warned[:10]:
                msg += f"  {os.path.basename(r.path)}: {', '.join(r.warnings[:3])}\n"

        box = QMessageBox(self)
        box.setWindowTitle("Bulk Convert Complete" if fmt == "OVR" else "Bulk Export Complete")
        box.setText(msg)
        box.addButton(QMessageBox.StandardButton.Ok)
        open_btn = box.addButton("Open Output Folder", QMessageBox.ButtonRole.ActionRole)
        box.exec()
        if box.clickedButton() == open_btn:
            from PyQt6.QtGui import QDesktopServices
            from PyQt6.QtCore import QUrl
            QDesktopServices.openUrl(QUrl.fromLocalFile(out_dir))
