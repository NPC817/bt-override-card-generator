"""Settings dialog — profile management + house rule values."""
from __future__ import annotations
import copy
import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QCheckBox, QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGroupBox, QHBoxLayout, QInputDialog, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMessageBox, QPushButton, QScrollArea, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget,
)

from ..models.data_store import DataStore
from ..settings.profile import ConversionProfile
from ..settings.profile_manager import ProfileManager, _safe_filename


_WEAPON_FIELDS: list[tuple[str, str, int, int]] = [
    ("damage",       "Damage",        0, 100),
    ("heat",         "Heat",          0,  30),
    ("rangePB",      "Range PB",     -4,   9),
    ("rangeS",       "Range S",      -4,   9),
    ("rangeM",       "Range M",      -4,   9),
    ("rangeL",       "Range L",      -4,   9),
    ("rangeX",       "Range X",      -4,   9),
    ("damageAdj",    "Damage Adj",  -20,  20),
    ("damageM",      "Damage M",      0, 100),
    ("shiftM",       "Shift M",      -4,   9),
    ("varPBSdamage", "Var PB/S Dmg",  0, 100),
    ("varMdamage",   "Var M Dmg",     0, 100),
    ("varLXdamage",  "Var L/X Dmg",   0, 100),
]

_TYPE_LABEL = {"B": "Ballistic", "E": "Energy", "M": "Missile", "P": "Physical"}
_VARIANT_FIELDS = {"damageAdj", "damageM", "shiftM", "varPBSdamage", "varMdamage", "varLXdamage"}


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("House Rule Settings")
        self.setMinimumSize(700, 540)

        # Working copies so Cancel discards everything
        self._profiles: dict[str, ConversionProfile] = {
            name: copy.deepcopy(ProfileManager.get(name) or ConversionProfile.default())
            for name in ProfileManager.all_names()
        }
        self._active_name: str = ProfileManager._active_name
        self._current_name: str | None = None
        self._current_weapon_key: str | None = None

        self._build_ui()
        self._refresh_list()

    # ── UI construction ───────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)

        # ── Profile list section ──────────────────────────────────────────────
        prof_box = QGroupBox("Profiles")
        prof_layout = QHBoxLayout(prof_box)

        self._profile_list = QListWidget()
        self._profile_list.setMaximumHeight(140)
        self._profile_list.currentTextChanged.connect(self._on_profile_selected)
        prof_layout.addWidget(self._profile_list, stretch=1)

        btn_col = QVBoxLayout()
        self._btn_new      = QPushButton("New…")
        self._btn_dup      = QPushButton("Duplicate…")
        self._btn_rename   = QPushButton("Rename…")
        self._btn_delete   = QPushButton("Delete")
        self._btn_activate = QPushButton("Set as Active")
        for b in (self._btn_new, self._btn_dup, self._btn_rename,
                  self._btn_delete, self._btn_activate):
            btn_col.addWidget(b)
        btn_col.addStretch()
        prof_layout.addLayout(btn_col)

        self._btn_new.clicked.connect(self._new_profile)
        self._btn_dup.clicked.connect(self._duplicate_profile)
        self._btn_rename.clicked.connect(self._rename_profile)
        self._btn_delete.clicked.connect(self._delete_profile)
        self._btn_activate.clicked.connect(self._set_active)

        root.addWidget(prof_box)

        # ── Value editor tabs ─────────────────────────────────────────────────
        self._editor_group = QGroupBox("Profile settings")
        editor_layout = QVBoxLayout(self._editor_group)

        self._readonly_label = QLabel("Default profile is read-only.")
        self._readonly_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._readonly_label.setStyleSheet("color: gray; font-style: italic;")
        self._readonly_label.setVisible(False)
        editor_layout.addWidget(self._readonly_label)

        self._tabs = QTabWidget()
        editor_layout.addWidget(self._tabs)

        # Armor tab
        armor_tab = QWidget()
        armor_form = QFormLayout(armor_tab)
        self._mech_div = QDoubleSpinBox()
        self._mech_div.setRange(1.0, 20.0); self._mech_div.setSingleStep(0.5)
        self._vehicle_div = QDoubleSpinBox()
        self._vehicle_div.setRange(1.0, 20.0); self._vehicle_div.setSingleStep(0.5)
        armor_form.addRow("Mech armor divisor:", self._mech_div)
        armor_form.addRow("Vehicle armor divisor:", self._vehicle_div)
        self._tabs.addTab(armor_tab, "Armor")

        # Heat tab
        heat_tab = QWidget()
        heat_form = QFormLayout(heat_tab)
        self._heat_max = QSpinBox()
        self._heat_max.setRange(1, 30)
        heat_form.addRow("Heat scale max:", self._heat_max)
        self._tabs.addTab(heat_tab, "Heat")

        # Movement tab
        move_tab = QWidget()
        move_form = QFormLayout(move_tab)
        self._move_mult = QDoubleSpinBox()
        self._move_mult.setRange(0.1, 5.0); self._move_mult.setSingleStep(0.1)
        move_form.addRow("Move scale multiplier:", self._move_mult)
        self._tabs.addTab(move_tab, "Movement")

        # Weapons tab
        self._tabs.addTab(self._build_weapons_tab(), "Weapons")

        root.addWidget(self._editor_group)

        # ── Active label ──────────────────────────────────────────────────────
        self._active_label = QLabel()
        self._active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(self._active_label)

        # ── Dialog buttons ────────────────────────────────────────────────────
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._accept)
        buttons.rejected.connect(self.reject)
        root.addWidget(buttons)

    def _build_weapons_tab(self) -> QWidget:
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)

        # Search + filter row
        filter_row = QHBoxLayout()
        self._weapon_search = QLineEdit()
        self._weapon_search.setPlaceholderText("Search weapons…")
        self._weapon_search.textChanged.connect(self._populate_weapon_list)
        self._weapon_override_only = QCheckBox("Only show overridden")
        self._weapon_override_only.toggled.connect(self._populate_weapon_list)
        filter_row.addWidget(QLabel("Search:"))
        filter_row.addWidget(self._weapon_search, stretch=1)
        filter_row.addWidget(self._weapon_override_only)
        tab_layout.addLayout(filter_row)

        # Split: list | editor
        split = QHBoxLayout()
        tab_layout.addLayout(split, stretch=1)

        # Left: weapon list
        self._weapon_list = QListWidget()
        self._weapon_list.setMinimumWidth(210)
        self._weapon_list.currentItemChanged.connect(self._on_weapon_item_changed)
        split.addWidget(self._weapon_list, stretch=1)

        # Right: editor inside scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumWidth(230)
        editor_container = QWidget()
        self._weapon_editor_layout = QFormLayout(editor_container)

        self._weapon_title_label = QLabel("Select a weapon")
        self._weapon_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._weapon_title_label.setStyleSheet("font-weight: bold; margin-bottom: 6px;")
        self._weapon_editor_layout.addRow(self._weapon_title_label)

        # Build spinboxes grouped by section
        self._weapon_spinboxes: dict[str, QSpinBox] = {}
        _combat_header_added = False
        _variant_header_added = False

        for field, label, lo, hi in _WEAPON_FIELDS:
            if not _combat_header_added and field == "damage":
                h = QLabel("Combat && Ranges")
                h.setStyleSheet("font-weight: bold; margin-top: 4px;")
                self._weapon_editor_layout.addRow(h)
                _combat_header_added = True
            if not _variant_header_added and field in _VARIANT_FIELDS:
                h = QLabel("Variant Damage")
                h.setStyleSheet("font-weight: bold; margin-top: 8px;")
                self._weapon_editor_layout.addRow(h)
                _variant_header_added = True
            sb = QSpinBox()
            sb.setRange(lo, hi)
            sb.setEnabled(False)
            self._weapon_spinboxes[field] = sb
            self._weapon_editor_layout.addRow(f"{label}:", sb)

        self._btn_reset_weapon = QPushButton("Reset to Base")
        self._btn_reset_weapon.setEnabled(False)
        self._btn_reset_weapon.clicked.connect(self._reset_weapon_override)
        self._weapon_editor_layout.addRow(self._btn_reset_weapon)

        scroll.setWidget(editor_container)
        split.addWidget(scroll, stretch=1)

        return tab

    # ── Profile list helpers ──────────────────────────────────────────────────

    def _refresh_list(self, select_name: str | None = None) -> None:
        self._profile_list.blockSignals(True)
        self._profile_list.clear()
        names = list(self._profiles.keys())
        if "Default" in names:
            names.remove("Default")
            names.insert(0, "Default")
        for name in names:
            display = name + (" ★" if name == self._active_name else "")
            self._profile_list.addItem(display)

        target = select_name or self._current_name or self._active_name
        if target:
            for suffix in ("", " ★"):
                items = self._profile_list.findItems(target + suffix, Qt.MatchFlag.MatchExactly)
                if items:
                    self._profile_list.setCurrentItem(items[0])
                    break

        self._profile_list.blockSignals(False)
        item = self._profile_list.currentItem()
        if item:
            self._on_profile_selected(item.text())

        self._active_label.setText(f"Active profile: {self._active_name}")

    def _current_raw_name(self) -> str | None:
        item = self._profile_list.currentItem()
        if not item:
            return None
        return item.text().removesuffix(" ★")

    # ── Weapon list helpers ───────────────────────────────────────────────────

    def _populate_weapon_list(self) -> None:
        p = self._profiles.get(self._current_name or "")
        overrides = p.weapon_overrides if p else {}

        search = self._weapon_search.text().strip().lower()
        only_overridden = self._weapon_override_only.isChecked()

        self._weapon_list.blockSignals(True)
        self._weapon_list.clear()

        for key, w in sorted(DataStore.all_weapons().items(), key=lambda kv: kv[1].name.lower()):
            has_override = key in overrides
            if only_overridden and not has_override:
                continue
            type_label = _TYPE_LABEL.get(w.type, w.type)
            display = f"{w.name}  ({w.tech} · {type_label})"
            if has_override:
                display += "  *"
            if search and search not in display.lower():
                continue
            item = QListWidgetItem(display)
            item.setData(Qt.ItemDataRole.UserRole, key)
            self._weapon_list.addItem(item)

        self._weapon_list.blockSignals(False)

        # Re-select previously selected weapon if still visible
        if self._current_weapon_key:
            target_key = self._current_weapon_key
            for i in range(self._weapon_list.count()):
                if self._weapon_list.item(i).data(Qt.ItemDataRole.UserRole) == target_key:
                    self._weapon_list.setCurrentRow(i)
                    return

        # Not found — clear editor
        self._current_weapon_key = None
        self._weapon_title_label.setText("Select a weapon")
        for sb in self._weapon_spinboxes.values():
            sb.setEnabled(False)
        self._btn_reset_weapon.setEnabled(False)

    def _refresh_weapon_list_item(self, key: str) -> None:
        p = self._profiles.get(self._current_name or "")
        if not p:
            return
        try:
            w = DataStore.weapon(key)
        except KeyError:
            return
        has_override = key in p.weapon_overrides
        type_label = _TYPE_LABEL.get(w.type, w.type)
        display = f"{w.name}  ({w.tech} · {type_label})"
        if has_override:
            display += "  *"
        for i in range(self._weapon_list.count()):
            item = self._weapon_list.item(i)
            if item.data(Qt.ItemDataRole.UserRole) == key:
                item.setText(display)
                return


    # ── Profile selection ─────────────────────────────────────────────────────

    def _on_profile_selected(self, display_text: str) -> None:
        if self._current_name and self._current_name in self._profiles:
            self._flush_spinboxes_to(self._current_name)

        raw = display_text.removesuffix(" ★")
        self._current_name = raw
        p = self._profiles.get(raw)
        if not p:
            return

        is_default = raw == "Default"
        self._readonly_label.setVisible(is_default)
        for w in (self._mech_div, self._vehicle_div,
                  self._heat_max, self._move_mult):
            w.setEnabled(not is_default)
        self._btn_rename.setEnabled(not is_default)
        self._btn_delete.setEnabled(not is_default)
        self._weapon_override_only.setEnabled(not is_default)

        self._mech_div.setValue(p.mech_armor_divisor)
        self._vehicle_div.setValue(p.vehicle_armor_divisor)
        self._heat_max.setValue(p.heat_scale_max)
        self._move_mult.setValue(p.move_scale_multiplier)

        self._populate_weapon_list()
        if self._current_weapon_key:
            self._load_weapon_editor(self._current_weapon_key, is_default)

    # ── Weapon selection ──────────────────────────────────────────────────────

    def _on_weapon_item_changed(self, current: QListWidgetItem, previous) -> None:
        if self._current_weapon_key and self._current_name:
            self._flush_weapon_editor_to(self._current_name)

        if current is None:
            self._current_weapon_key = None
            self._weapon_title_label.setText("Select a weapon")
            for sb in self._weapon_spinboxes.values():
                sb.setEnabled(False)
            self._btn_reset_weapon.setEnabled(False)
            return

        key = current.data(Qt.ItemDataRole.UserRole)
        self._current_weapon_key = key
        is_default = self._current_name == "Default"
        self._load_weapon_editor(key, is_default)

    def _load_weapon_editor(self, key: str, is_default: bool) -> None:
        try:
            base = DataStore.weapon(key)
        except KeyError:
            return

        p = self._profiles.get(self._current_name or "")
        overrides = p.weapon_overrides.get(key, {}) if p else {}

        type_label = _TYPE_LABEL.get(base.type, base.type)
        self._weapon_title_label.setText(f"{base.name}  ({base.tech} · {type_label})")

        editable = not is_default

        for field, _label, _lo, _hi in _WEAPON_FIELDS:
            sb = self._weapon_spinboxes[field]
            base_val = getattr(base, field, 0)
            if callable(base_val):
                sb.setValue(0)
                sb.setEnabled(False)
                sb.setToolTip("Computed from tonnage — not overridable")
            else:
                val = overrides.get(field, int(base_val))
                sb.blockSignals(True)
                sb.setValue(val)
                sb.blockSignals(False)
                sb.setEnabled(editable)
                sb.setToolTip("")

        self._btn_reset_weapon.setEnabled(editable and bool(overrides))

    def _flush_spinboxes_to(self, name: str) -> None:
        if name == "Default":
            return
        p = self._profiles.get(name)
        if not p:
            return
        p.mech_armor_divisor    = self._mech_div.value()
        p.vehicle_armor_divisor = self._vehicle_div.value()
        p.heat_scale_max        = self._heat_max.value()
        p.move_scale_multiplier = self._move_mult.value()
        self._flush_weapon_editor_to(name)

    def _flush_weapon_editor_to(self, profile_name: str) -> None:
        if not self._current_weapon_key or profile_name == "Default":
            return
        p = self._profiles.get(profile_name)
        if not p:
            return
        key = self._current_weapon_key
        try:
            base = DataStore.weapon(key)
        except KeyError:
            return

        updates: dict[str, int] = {}
        for field, _label, _lo, _hi in _WEAPON_FIELDS:
            base_val = getattr(base, field, 0)
            if callable(base_val):
                continue
            new_val = self._weapon_spinboxes[field].value()
            if new_val != int(base_val):
                updates[field] = new_val

        if updates:
            p.weapon_overrides[key] = updates
        elif key in p.weapon_overrides:
            del p.weapon_overrides[key]

        self._refresh_weapon_list_item(key)

    def _reset_weapon_override(self) -> None:
        key = self._current_weapon_key
        if not key or not self._current_name or self._current_name == "Default":
            return
        p = self._profiles.get(self._current_name)
        if not p:
            return
        p.weapon_overrides.pop(key, None)
        self._refresh_weapon_list_item(key)
        self._load_weapon_editor(key, is_default=False)
        self._btn_reset_weapon.setEnabled(False)

    # ── CRUD actions ──────────────────────────────────────────────────────────

    def _ask_name(self, title: str, default: str = "") -> str | None:
        name, ok = QInputDialog.getText(self, title, "Profile name:", text=default)
        if not ok or not name.strip():
            return None
        name = name.strip()
        if len(name) > 64:
            QMessageBox.warning(self, "Invalid name", "Profile name must be 64 characters or fewer.")
            return None
        if any(c in name for c in ("/", "\\", "..")):
            QMessageBox.warning(self, "Invalid name", "Profile name contains invalid characters.")
            return None
        if name == "Default":
            QMessageBox.warning(self, "Invalid name", "'Default' is reserved.")
            return None
        if name in self._profiles:
            QMessageBox.warning(self, "Name taken", f"A profile named '{name}' already exists.")
            return None
        return name

    def _new_profile(self) -> None:
        name = self._ask_name("New Profile")
        if not name:
            return
        self._profiles[name] = ConversionProfile(name=name)
        self._refresh_list(select_name=name)

    def _duplicate_profile(self) -> None:
        src = self._current_raw_name()
        if not src:
            return
        name = self._ask_name("Duplicate Profile", default=f"{src} Copy")
        if not name:
            return
        base = copy.deepcopy(self._profiles[src])
        base.name = name
        self._profiles[name] = base
        self._refresh_list(select_name=name)

    def _rename_profile(self) -> None:
        src = self._current_raw_name()
        if not src or src == "Default":
            return
        name = self._ask_name("Rename Profile", default=src)
        if not name:
            return
        p = self._profiles.pop(src)
        p.name = name
        self._profiles[name] = p
        if self._active_name == src:
            self._active_name = name
        self._current_name = name
        self._refresh_list(select_name=name)

    def _delete_profile(self) -> None:
        src = self._current_raw_name()
        if not src or src == "Default":
            return
        reply = QMessageBox.question(
            self, "Delete Profile",
            f"Delete profile '{src}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        self._profiles.pop(src, None)
        if self._active_name == src:
            self._active_name = "Default"
        self._current_name = None
        self._refresh_list(select_name="Default")

    def _set_active(self) -> None:
        name = self._current_raw_name()
        if not name or name not in self._profiles:
            return
        self._active_name = name
        self._refresh_list(select_name=name)

    # ── Accept ────────────────────────────────────────────────────────────────

    def _accept(self) -> None:
        if self._current_name:
            self._flush_spinboxes_to(self._current_name)

        for name in ProfileManager.all_names():
            if name not in self._profiles:
                ProfileManager.delete(name)

        for name, profile in self._profiles.items():
            if name != "Default":
                ProfileManager.save(profile)

        from ..utils.paths import user_data_path
        profiles_dir = str(user_data_path("data", "profiles"))
        existing_files = {
            f[:-5] for f in os.listdir(profiles_dir) if f.endswith(".yaml")
        } if os.path.isdir(profiles_dir) else set()
        safe_names = {
            _safe_filename(n) for n in self._profiles if n != "Default"
        }
        for stale in existing_files - safe_names:
            try:
                os.remove(os.path.join(profiles_dir, f"{stale}.yaml"))
            except OSError:
                pass

        ProfileManager.set_active(self._active_name)
        self.accept()
