"""Main application window with tab-based card editing."""
from __future__ import annotations
import os

from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QFileDialog, QLabel, QMainWindow, QMessageBox,
    QTabWidget,
)

from ..models.data_store import DataStore
from ..settings.profile_manager import ProfileManager
from ..parsers.mtf_parser import parse_mtf
from ..parsers.blk_parser import parse_blk
from .theme import ThemeManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BattleTech Override Card Generator")
        self.resize(1600, 900)

        DataStore._ensure_loaded()
        if not ProfileManager._profiles:
            ProfileManager.load()
        self.setAcceptDrops(True)

        self._tabs = QTabWidget()
        self._tabs.setTabsClosable(True)
        self._tabs.setMovable(True)
        self._tabs.tabCloseRequested.connect(self._close_tab)
        self.setCentralWidget(self._tabs)

        self._build_menu()
        self._build_status_bar()
        self._new_tab()

    # ── Menu ─────────────────────────────────────────────────────────────────

    def _build_menu(self) -> None:
        mb = self.menuBar()

        file_menu = mb.addMenu("&File")
        self._add_action(file_menu, "&New Card",     "Ctrl+N", self._new_tab)
        self._add_action(file_menu, "&Open MTF/BLK…","Ctrl+O", self._open_file)
        self._add_action(file_menu, "Open &Override Card…", "Ctrl+Shift+O", self._load_ovr)
        self._add_action(file_menu, "Import &Force…", "Ctrl+Shift+F", self._import_force)
        file_menu.addSeparator()
        self._add_action(file_menu, "&Save…",        "Ctrl+S", self._save)
        self._add_action(file_menu, "Export Force…", "Ctrl+Alt+F", self._export_force)
        file_menu.addSeparator()
        self._add_action(file_menu, "&Print Current Card…",  "Ctrl+P",       self._print_current)
        self._add_action(file_menu, "Print All Open Ta&bs…", "Ctrl+Shift+P", self._print_all_tabs)
        file_menu.addSeparator()
        self._add_action(file_menu, "Export &PNG…",  "Ctrl+Alt+P", self._export_png)
        self._add_action(file_menu, "Export P&DF…",  "Ctrl+D", self._export_pdf)
        self._add_action(file_menu, "Export &Form PDF…", "", self._export_form_pdf)
        self._add_action(file_menu, "Export All &Open Tabs…", "Ctrl+Shift+E",
                         self._export_all_tabs)
        file_menu.addSeparator()
        self._add_action(file_menu, "Bulk Import/Export…", "", self._bulk_import)
        file_menu.addSeparator()
        self._add_action(file_menu, "Browse Unit &Database…", "Ctrl+Shift+D", self._open_unit_database)
        file_menu.addSeparator()
        self._add_action(file_menu, "&Close Tab", "Ctrl+W",
                         lambda: self._close_tab(self._tabs.currentIndex()))
        self._add_action(file_menu, "C&lear All Tabs", "Ctrl+Shift+W", self._clear_all_tabs)
        self._add_action(file_menu, "&Quit", "Ctrl+Q", QApplication.quit)

        settings_menu = mb.addMenu("&Settings")
        self._add_action(settings_menu, "House Rule &Profiles…", "", self._open_settings)

        view_menu = mb.addMenu("&View")
        self._dark_action = QAction("&Dark Mode", self)
        self._dark_action.setCheckable(True)
        self._dark_action.setChecked(ThemeManager.is_dark())
        self._dark_action.triggered.connect(self._toggle_theme)
        view_menu.addAction(self._dark_action)

        help_menu = mb.addMenu("&Help")
        self._add_action(help_menu, "Check for &Updates…", "", self._check_for_updates)
        self._add_action(help_menu, "&About", "", self._about)

    def _add_action(self, menu, label, shortcut, slot) -> None:
        act = QAction(label, self)
        if shortcut:
            act.setShortcut(QKeySequence(shortcut))
        act.triggered.connect(slot)
        menu.addAction(act)

    # ── Status bar ────────────────────────────────────────────────────────────

    def _build_status_bar(self) -> None:
        self._status_profile = QLabel()
        self._update_profile_label()
        self.statusBar().addPermanentWidget(self._status_profile)

    def _update_profile_label(self) -> None:
        self._status_profile.setText(f"Profile: {ProfileManager.active().name}")

    # ── Tab management ────────────────────────────────────────────────────────

    def _new_tab(self, unit=None) -> None:
        from .card_tab import CardTab
        tab = CardTab()
        if unit:
            tab.load_unit(unit)
        label = unit.display_name if unit else "New Card"
        idx = self._tabs.addTab(tab, label)
        self._tabs.setCurrentIndex(idx)
        tab.unit_changed.connect(lambda: self._on_tab_unit_changed(tab))

    def _on_tab_unit_changed(self, tab) -> None:
        idx = self._tabs.indexOf(tab)
        if idx >= 0 and tab.unit:
            self._tabs.setTabText(idx, tab.unit.display_name or "New Card")

    def _close_tab(self, index: int) -> None:
        if self._tabs.count() == 1:
            return
        self._tabs.removeTab(index)

    def _clear_all_tabs(self) -> None:
        self._tabs.clear()
        self._new_tab()

    def _current_tab(self):
        return self._tabs.currentWidget()

    # ── File actions ──────────────────────────────────────────────────────────

    def _open_file(self) -> None:
        paths, _ = QFileDialog.getOpenFileNames(
            self, "Open MTF/BLK File",
            filter="MegaMek Files (*.mtf *.blk);;All Files (*)"
        )
        for path in paths:
            self._import_file(path)

    def _import_file(self, path: str) -> None:
        if os.path.getsize(path) > 5 * 1024 * 1024:
            QMessageBox.warning(self, "Import Error", "File too large (> 5 MB)")
            return
        ext = os.path.splitext(path)[1].lower()
        try:
            if ext == ".mtf":
                result = parse_mtf(path)
            elif ext == ".blk":
                result = parse_blk(path)
            else:
                QMessageBox.warning(self, "Import Error", f"Unknown file type: {ext}")
                return
        except Exception as exc:
            QMessageBox.critical(self, "Parse Error", str(exc))
            return

        # Close any unnamed/unmodified tabs before opening the imported unit
        for i in reversed(range(self._tabs.count())):
            tab = self._tabs.widget(i)
            if tab and (tab.unit is None or not tab.unit.chassis):
                self._tabs.removeTab(i)

        self._new_tab(result.unit)
        if result.warnings:
            msg = "\n".join(result.warnings[:20])
            QMessageBox.information(
                self, "Import Warnings",
                f"Imported with {len(result.warnings)} warnings:\n\n{msg}"
            )

    def _save(self) -> None:
        tab = self._current_tab()
        if not tab or not tab.unit:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Save Card", filter="Override Card (*.ovr)")
        if not path:
            return
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(tab.unit.to_dict(), f, indent=2)

    def _load_ovr(self) -> None:
        paths, _ = QFileDialog.getOpenFileNames(
            self, "Open Override Card", filter="Override Card (*.ovr);;All Files (*)"
        )
        if not paths:
            return
        import json
        from ..models.mech import BattleMech
        from ..models.vehicle import CombatVehicle
        from ..models.aero import AeroSpaceFighter
        from ..models.battle_armor import BattleArmor
        from ..models.infantry import Infantry
        _type_map = {
            "BattleMech": BattleMech,
            "CombatVehicle": CombatVehicle,
            "AeroSpaceFighter": AeroSpaceFighter,
            "BattleArmor": BattleArmor,
            "Infantry": Infantry,
        }
        for path in paths:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                unit_type = data.get("unit_type", "")
                cls = _type_map.get(unit_type)
                if cls is None:
                    QMessageBox.warning(self, "Load Error",
                                        f"Unknown unit_type '{unit_type}' in {os.path.basename(path)}")
                    continue
                unit = cls.from_dict(data)
            except Exception as exc:
                QMessageBox.critical(self, "Load Error",
                                     f"Failed to load {os.path.basename(path)}:\n{exc}")
                continue
            for i in reversed(range(self._tabs.count())):
                tab = self._tabs.widget(i)
                if tab and (tab.unit is None or not tab.unit.chassis):
                    self._tabs.removeTab(i)
            self._new_tab(unit)

    def _export_force(self) -> None:
        import json
        units = []
        for i in range(self._tabs.count()):
            tab = self._tabs.widget(i)
            if tab and tab.unit and tab.unit.chassis:
                units.append(tab.unit.to_dict())
        if not units:
            QMessageBox.information(self, "Export Force", "No units to export.")
            return
        path, _ = QFileDialog.getSaveFileName(
            self, "Export Force", filter="BattleTech Force (*.force)"
        )
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"version": 1, "units": units}, f, indent=2)

    def _import_force(self) -> None:
        import json
        from ..models.mech import BattleMech
        from ..models.vehicle import CombatVehicle
        from ..models.aero import AeroSpaceFighter
        from ..models.battle_armor import BattleArmor
        from ..models.infantry import Infantry
        _type_map = {
            "BattleMech": BattleMech,
            "CombatVehicle": CombatVehicle,
            "AeroSpaceFighter": AeroSpaceFighter,
            "BattleArmor": BattleArmor,
            "Infantry": Infantry,
        }
        path, _ = QFileDialog.getOpenFileName(
            self, "Import Force",
            filter="BattleTech Force (*.force *.mul *.csv);;All Files (*)"
        )
        if not path:
            return
        ext = os.path.splitext(path)[1].lower()
        if ext in (".mul", ".csv"):
            self._import_force_from_pairs(path, ext)
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            QMessageBox.critical(self, "Import Error", f"Failed to read force file:\n{exc}")
            return
        unit_list = data.get("units", []) if isinstance(data, dict) else data
        if not unit_list:
            QMessageBox.information(self, "Import Force", "Force file contains no units.")
            return
        for i in reversed(range(self._tabs.count())):
            tab = self._tabs.widget(i)
            if tab and (tab.unit is None or not tab.unit.chassis):
                self._tabs.removeTab(i)
        first_idx = self._tabs.count()
        loaded = 0
        errors = []
        for unit_data in unit_list:
            unit_type = unit_data.get("unit_type", "")
            cls = _type_map.get(unit_type)
            if cls is None:
                errors.append(f"Unknown unit_type '{unit_type}'")
                continue
            try:
                unit = cls.from_dict(unit_data)
                self._new_tab(unit)
                loaded += 1
            except Exception as exc:
                errors.append(f"{unit_data.get('chassis', '?')}: {exc}")
        if loaded > 0:
            self._tabs.setCurrentIndex(first_idx)
        if errors:
            msg = "\n".join(errors[:10])
            QMessageBox.warning(self, "Import Force",
                                f"Loaded {loaded} units with {len(errors)} errors:\n\n{msg}")

    def _read_zip_records(self) -> list[dict]:
        import json
        import zipfile
        from ..utils.paths import resource_path
        from .unit_database_dialog import _get_type_map
        zip_path = resource_path("data", "units.zip")
        records: list[dict] = []
        try:
            with zipfile.ZipFile(zip_path, "r") as zf:
                for name in zf.namelist():
                    if not name.lower().endswith(".ovr"):
                        continue
                    try:
                        data = json.loads(zf.read(name).decode("utf-8"))
                        if isinstance(data, dict) and data.get("unit_type") in _get_type_map():
                            records.append(data)
                    except Exception:
                        pass
        except Exception as exc:
            QMessageBox.critical(self, "Import Error", f"Could not open units.zip:\n{exc}")
        return records

    @staticmethod
    def _lookup_unit(records: list[dict], chassis: str, model: str) -> dict | None:
        chassis_l = chassis.strip().lower()
        model_l = model.strip().lower()
        for rec in records:
            if (rec.get("chassis", "").lower() == chassis_l
                    and rec.get("variant", "").lower() == model_l):
                return rec
        return None

    def _import_force_from_pairs(self, path: str, ext: str) -> None:
        import csv
        import xml.etree.ElementTree as ET
        from .unit_database_dialog import _get_type_map

        pairs: list[tuple[str, str]] = []
        try:
            if ext == ".mul":
                tree = ET.parse(path)
                for entity in tree.iter("entity"):
                    chassis = entity.get("chassis", "").strip()
                    model = entity.get("model", "").strip()
                    if chassis:
                        pairs.append((chassis, model))
            else:
                with open(path, newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        chassis = row.get("chassis", "").strip()
                        model = row.get("model", "").strip()
                        if chassis:
                            pairs.append((chassis, model))
        except Exception as exc:
            QMessageBox.critical(self, "Import Error", f"Failed to parse file:\n{exc}")
            return

        if not pairs:
            QMessageBox.information(self, "Import Force", "No units found in file.")
            return

        records = self._read_zip_records()
        if not records:
            return

        type_map = _get_type_map()
        for i in reversed(range(self._tabs.count())):
            tab = self._tabs.widget(i)
            if tab and (tab.unit is None or not tab.unit.chassis):
                self._tabs.removeTab(i)
        first_idx = self._tabs.count()

        loaded = 0
        not_found: list[str] = []
        for chassis, model in pairs:
            rec = self._lookup_unit(records, chassis, model)
            if rec is None:
                not_found.append(f"{chassis} {model}".strip())
                continue
            cls = type_map.get(rec.get("unit_type", ""))
            if cls is None:
                not_found.append(f"{chassis} {model} (unknown type)")
                continue
            try:
                unit = cls.from_dict(rec)
                for w in unit.weapons:
                    w.tic = 0
                self._new_tab(unit)
                loaded += 1
            except Exception as exc:
                not_found.append(f"{chassis} {model}: {exc}")

        if loaded > 0:
            self._tabs.setCurrentIndex(first_idx)
        if not_found:
            msg = "\n".join(not_found[:20])
            QMessageBox.warning(
                self, "Import Force",
                f"Loaded {loaded} unit(s). Not found in database ({len(not_found)}):\n\n{msg}"
            )

    def _print_current(self) -> None:
        tab = self._current_tab()
        if not tab or not tab.unit:
            return
        from .print_dialog import PrintQueueDialog
        dlg = PrintQueueDialog([(tab.unit.display_name, tab.render_card())], parent=self)
        dlg.exec()

    def _print_all_tabs(self) -> None:
        items = []
        for i in range(self._tabs.count()):
            tab = self._tabs.widget(i)
            if tab and tab.unit:
                items.append((tab.unit.display_name, tab.render_card()))
        if not items:
            return
        from .print_dialog import PrintQueueDialog
        dlg = PrintQueueDialog(items, parent=self)
        dlg.exec()

    def _export_png(self) -> None:
        tab = self._current_tab()
        if not tab or not tab.unit:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export PNG", filter="PNG Image (*.png)")
        if not path:
            return
        from ..renderer.png_exporter import export_png
        export_png(tab.render_card(), path)

    def _export_pdf(self) -> None:
        tab = self._current_tab()
        if not tab or not tab.unit:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export PDF", filter="PDF File (*.pdf)")
        if not path:
            return
        from ..renderer.pdf_exporter import export_pdf
        export_pdf(tab.render_card(), path)

    def _export_form_pdf(self) -> None:
        QMessageBox.information(self, "Form PDF", "Form-fillable PDF export not yet implemented.")

    def _export_all_tabs(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, "Export Folder")
        if not folder:
            return
        from ..renderer.png_exporter import export_png
        count = 0
        for i in range(self._tabs.count()):
            tab = self._tabs.widget(i)
            if tab and tab.unit:
                px = tab.render_card()
                name = tab.unit.display_name.replace(" ", "_").replace("/", "-")
                export_png(px, os.path.join(folder, f"{name}.png"))
                count += 1
        QMessageBox.information(self, "Done", f"Exported {count} cards to {folder}")

    def _bulk_import(self) -> None:
        from .bulk_dialog import BulkDialog
        dlg = BulkDialog(parent=self)
        dlg.exec()

    def _open_unit_database(self) -> None:
        from .unit_database_dialog import UnitDatabaseDialog
        dlg = UnitDatabaseDialog(parent=self)
        dlg.unit_selected.connect(self._load_unit_from_db)
        dlg.exec()

    def _load_unit_from_db(self, unit) -> None:
        for i in reversed(range(self._tabs.count())):
            tab = self._tabs.widget(i)
            if tab and (tab.unit is None or not tab.unit.chassis):
                self._tabs.removeTab(i)
        self._new_tab(unit)

    def _open_settings(self) -> None:
        from .settings_dialog import SettingsDialog
        dlg = SettingsDialog(parent=self)
        if dlg.exec():
            self._update_profile_label()
            for i in range(self._tabs.count()):
                tab = self._tabs.widget(i)
                if tab:
                    tab.refresh_preview()

    def _toggle_theme(self, enabled: bool) -> None:
        ThemeManager.set_dark(enabled)
        ThemeManager.apply(QApplication.instance())

    def _check_for_updates(self) -> None:
        from .update_checker import UpdateDialog
        dlg = UpdateDialog(parent=self)
        dlg.exec()

    def _about(self) -> None:
        from src.version import __version__, __app_name__, __repo_url__

        QMessageBox.about(
            self,
            f"About {__app_name__}",
            f"<h3>{__app_name__}</h3>"
            f"<p>Version <b>{__version__}</b></p>"
            f"<p>Python/PyQt6 port of the DFA Wargaming Override Card Generator.</p>"
            f"<p>Converts MegaMek MTF/BLK files to Override format cards.</p>"
            f"<hr>"
            f"<p><a href='{__repo_url__}'>GitHub Repository</a></p>",
        )

    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event) -> None:
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path.lower().endswith((".mtf", ".blk")):
                self._import_file(path)
