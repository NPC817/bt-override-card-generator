"""
CardTab: the main editing area — left panel (form) + right panel (preview).
Live card preview debounced at 300 ms.
"""
from __future__ import annotations
import logging
from typing import Optional

from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtWidgets import (
    QComboBox, QLabel, QSizePolicy, QSplitter,
    QStackedWidget, QVBoxLayout, QWidget,
)

from ..models.unit import AbstractUnit
from ..settings.profile_manager import ProfileManager


class CardTab(QWidget):
    unit_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.unit: Optional[AbstractUnit] = None
        self._form: Optional[QWidget] = None

        self._build_ui()
        self._debounce = QTimer()
        self._debounce.setSingleShot(True)
        self._debounce.setInterval(300)
        self._debounce.timeout.connect(self._do_render)

    # ── UI ────────────────────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter()
        layout.addWidget(splitter)

        # Left panel: type selector + stacked forms
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(4, 4, 4, 4)

        self._type_combo = QComboBox()
        self._type_combo.addItems([
            "BattleMech", "Combat Vehicle", "Fighter",
            "Battle Armor", "Infantry",
        ])
        self._type_combo.currentIndexChanged.connect(self._on_type_changed)
        left_layout.addWidget(self._type_combo)

        self._form_stack = QStackedWidget()
        left_layout.addWidget(self._form_stack)

        self._build_forms()

        left.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        splitter.addWidget(left)

        # Right panel: live preview
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(4, 4, 4, 4)

        self._preview_label = QLabel("Select unit type and fill in the form.")
        self._preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._preview_label.setScaledContents(False)
        self._preview_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        right_layout.addWidget(self._preview_label)

        right.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        splitter.addWidget(right)
        splitter.setSizes([475, 1025])

    def _build_forms(self) -> None:
        from .forms.mech_form import MechForm
        from .forms.vehicle_form import VehicleForm
        from .forms.aero_form import AeroForm
        from .forms.ba_form import BattleArmorForm
        from .forms.infantry_form import InfantryForm

        self._mech_form    = MechForm();          self._mech_form.changed.connect(self._schedule_render)
        self._vehicle_form = VehicleForm();       self._vehicle_form.changed.connect(self._schedule_render)
        self._aero_form    = AeroForm();          self._aero_form.changed.connect(self._schedule_render)
        self._ba_form      = BattleArmorForm();   self._ba_form.changed.connect(self._schedule_render)
        self._inf_form     = InfantryForm();      self._inf_form.changed.connect(self._schedule_render)

        for f in [self._mech_form, self._vehicle_form,
                  self._aero_form, self._ba_form, self._inf_form]:
            self._form_stack.addWidget(f)

    # ── Type switching ────────────────────────────────────────────────────────

    def _on_type_changed(self, idx: int) -> None:
        self._form_stack.setCurrentIndex(idx)
        self.unit = None
        self._schedule_render()

    # ── Unit loading ──────────────────────────────────────────────────────────

    def load_unit(self, unit: AbstractUnit) -> None:
        from ..models.mech import BattleMech
        from ..models.vehicle import CombatVehicle
        from ..models.aero import AeroSpaceFighter
        from ..models.battle_armor import BattleArmor
        from ..models.infantry import Infantry
        from ..engine.tic_grouper import resolve_weapons, auto_assign_tics

        # Auto-assign TICs only when none are set (fresh MTF/BLK parse has tic=0).
        # Saved .ovr/.force files carry user-set TIC values — preserve them.
        if not any(w.tic for w in unit.weapons):
            try:
                tonnage = getattr(unit, "tonnage", 0)
                resolved = resolve_weapons(unit, tonnage)
                auto_assign_tics(resolved, is_ba=isinstance(unit, BattleArmor))
            except Exception as exc:
                logging.warning("TIC auto-assign failed: %s", exc)

        self.unit = unit
        type_map = {
            BattleMech: 0, CombatVehicle: 1,
            AeroSpaceFighter: 2, BattleArmor: 3, Infantry: 4,
        }
        idx = type_map.get(type(unit), 0)
        self._type_combo.blockSignals(True)
        self._type_combo.setCurrentIndex(idx)
        self._type_combo.blockSignals(False)
        self._form_stack.setCurrentIndex(idx)

        form = self._form_stack.currentWidget()
        if hasattr(form, "load_unit"):
            form.load_unit(unit)

        self.unit_changed.emit()
        self._schedule_render()

    # ── Preview rendering ─────────────────────────────────────────────────────

    def _schedule_render(self) -> None:
        self._debounce.start()

    def _do_render(self) -> None:
        # Pull unit from current form
        form = self._form_stack.currentWidget()
        if hasattr(form, "get_unit"):
            try:
                self.unit = form.get_unit()
            except Exception:
                return  # Form data incomplete; preview stays stale

        if not self.unit:
            return

        px = self.render_card()
        self._set_preview(px)
        self.unit_changed.emit()

    def render_card(self) -> QPixmap:
        from ..models.mech import BattleMech
        from ..models.vehicle import CombatVehicle
        from ..models.aero import AeroSpaceFighter
        from ..models.battle_armor import BattleArmor
        from ..models.infantry import Infantry
        from ..renderer.mech_renderer import MechCardRenderer, QuadCardRenderer
        from ..renderer.vehicle_renderer import VehicleCardRenderer
        from ..renderer.aero_renderer import AeroCardRenderer
        from ..renderer.ba_renderer import BattleArmorRenderer
        from ..engine.tic_grouper import resolve_weapons, build_tic_rows, auto_assign_tics
        from ..models.data_store import DataStore

        if not self.unit:
            return QPixmap(2100, 1500)

        profile = ProfileManager.active()

        # Build per-TIC weapon rows
        weapons_rows = []
        try:
            tonnage = getattr(self.unit, "tonnage", 0)
            resolved = resolve_weapons(self.unit, tonnage, profile=profile)
            if isinstance(self.unit, BattleArmor):
                auto_assign_tics(resolved, is_ba=True)
            weapons_rows = build_tic_rows(resolved, heat_scale_max=profile.heat_scale_max)
        except Exception:
            pass  # No weapons data; render equipment-only card

        # BA: compute per-squad-size damage arrays with full TIC grouping
        if weapons_rows and isinstance(self.unit, BattleArmor) and self.unit.squad_size > 1:
            from ..engine.tic_grouper import ba_squad_damage_strs
            dmg_strs = ba_squad_damage_strs(resolved, self.unit.squad_size)
            for i, row in enumerate(weapons_rows):
                if i < len(dmg_strs):
                    row["damage"] = dmg_strs[i]

        # Build equipment string
        eq_parts = []
        seen_ba_eq: set[tuple[str, str]] = set()   # dedup BA equipment by (key, subtype)
        seen_no_loc: set[tuple[str, str]] = set()  # dedup location-irrelevant equipment
        for eq in self.unit.equipment:
            # BA: skip duplicates (same key+subtype, location irrelevant)
            if isinstance(self.unit, BattleArmor):
                sig = (eq.equipment_key, eq.subtype)
                if sig in seen_ba_eq:
                    continue
                seen_ba_eq.add(sig)
            label = eq.equipment_key
            eq_obj = None
            try:
                eq_obj = DataStore.equipment(eq.equipment_key)
                label = eq_obj.name
            except KeyError:
                pass
            # Skip duplicates for location-irrelevant equipment (e.g. Jump Jets)
            if eq_obj is not None and not eq_obj.hasLoc:
                sig = (eq.equipment_key, eq.subtype)
                if sig in seen_no_loc:
                    continue
                seen_no_loc.add(sig)
            if eq.subtype:
                label += f" ({eq.subtype})"
            # Show location only when equipment tracks it and unit is not BA
            if not isinstance(self.unit, BattleArmor) and eq.location and (eq_obj is None or eq_obj.hasLoc):
                label += f" [{eq.location}]"
            if eq.uses:
                uses_str = str(int(eq.uses)) if eq.uses % 1 == 0 else f"{eq.uses:.1f}"
                label += f" ({uses_str})"
            eq_parts.append(label)
        equipment_str = ", ".join(eq_parts)

        if isinstance(self.unit, BattleMech):
            if self.unit.motive_type == BattleMech.QUAD:
                renderer = QuadCardRenderer()
            else:
                renderer = MechCardRenderer()
            return renderer.render(self.unit, profile, weapons_rows, equipment_str)
        elif isinstance(self.unit, CombatVehicle):
            renderer = VehicleCardRenderer()
            return renderer.render(self.unit, profile, weapons_rows, equipment_str)
        elif isinstance(self.unit, AeroSpaceFighter):
            renderer = AeroCardRenderer()
            return renderer.render(self.unit, profile, weapons_rows, equipment_str)
        elif isinstance(self.unit, BattleArmor):
            renderer = BattleArmorRenderer()
            return renderer.render(self.unit, profile, weapons_rows, equipment_str)
        elif isinstance(self.unit, Infantry):
            from ..renderer.infantry_renderer import InfantryCardRenderer
            renderer = InfantryCardRenderer()
            return renderer.render(self.unit, profile, weapons_rows, equipment_str)
        else:
            px = QPixmap(2100, 1500)
            px.fill(QColor("lightgray"))
            return px

    def _set_preview(self, pixmap: QPixmap) -> None:
        label = self._preview_label
        label_size = label.size()
        if pixmap.isNull() or label_size.isEmpty():
            label.setPixmap(pixmap)
            return
        scaled = pixmap.scaled(
            label_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        label.setPixmap(scaled)

    def refresh_preview(self) -> None:
        self._schedule_render()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        # Re-scale preview on resize
        if hasattr(self, "_preview_label") and self._preview_label.pixmap():
            self._schedule_render()
