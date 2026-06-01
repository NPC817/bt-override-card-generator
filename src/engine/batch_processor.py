"""QThread-based batch processor for bulk card export."""
from __future__ import annotations
import os
from dataclasses import dataclass, field

from PyQt6.QtCore import QThread, pyqtSignal

from ..settings.profile_manager import ProfileManager
from ..models.mech import BattleMech
from ..models.vehicle import CombatVehicle
from ..models.aero import AeroSpaceFighter
from ..models.battle_armor import BattleArmor
from ..models.data_store import DataStore
from ..renderer.mech_renderer import MechCardRenderer, QuadCardRenderer
from ..renderer.vehicle_renderer import VehicleCardRenderer
from ..renderer.aero_renderer import AeroCardRenderer
from ..renderer.ba_renderer import BattleArmorRenderer
from ..renderer.png_exporter import export_png
from ..renderer.pdf_exporter import export_pdf
from ..engine.tic_grouper import (
    resolve_weapons, build_tic_rows, auto_assign_tics, ba_squad_damage_strs,
)


@dataclass
class BatchResult:
    path: str
    success: bool
    warnings: list[str] = field(default_factory=list)
    error: str = ""


class BatchProcessor(QThread):
    """Processes a list of MTF/BLK files and exports cards.

    Signals:
        progress(current, total, filename)
        file_done(BatchResult)
        finished_all()
    """
    progress    = pyqtSignal(int, int, str)
    file_done   = pyqtSignal(object)
    finished_all = pyqtSignal()

    def __init__(
        self,
        files: list[str],
        out_dir: str,
        profile_name: str,
        fmt: str,          # "PNG", "PDF", or "All"
        parent=None,
    ):
        super().__init__(parent)
        self._files        = files
        self._out_dir      = out_dir
        self._profile_name = profile_name
        self._fmt          = fmt
        self._cancel       = False

    def cancel(self) -> None:
        self._cancel = True

    def run(self) -> None:
        ProfileManager.set_active(self._profile_name)
        profile = ProfileManager.active()
        total = len(self._files)

        for i, path in enumerate(self._files):
            if self._cancel:
                break
            fname = os.path.basename(path)
            self.progress.emit(i + 1, total, fname)

            result = BatchResult(path=path, success=False)
            try:
                ext = os.path.splitext(path)[1].lower()
                if ext == ".mtf":
                    from ..parsers.mtf_parser import parse_mtf
                    parsed = parse_mtf(path)
                elif ext == ".blk":
                    from ..parsers.blk_parser import parse_blk
                    parsed = parse_blk(path)
                else:
                    result.error = f"Unsupported file type: {ext}"
                    self.file_done.emit(result)
                    continue

                result.warnings = list(parsed.warnings)
                unit = parsed.unit

                tonnage = getattr(unit, "tonnage", 0)
                resolved = resolve_weapons(unit, tonnage, profile=profile)
                auto_assign_tics(resolved, is_ba=isinstance(unit, BattleArmor))

                if self._fmt == "OVR":
                    import json
                    base = os.path.splitext(os.path.basename(path))[0]
                    with open(os.path.join(self._out_dir, f"{base}.ovr"), "w", encoding="utf-8") as fh:
                        json.dump(unit.to_dict(), fh, indent=2)
                    result.success = True
                    self.file_done.emit(result)
                    continue
                rows = build_tic_rows(resolved)

                # BA per-squad damage arrays
                if isinstance(unit, BattleArmor) and unit.squad_size > 1:
                    dmg_strs = ba_squad_damage_strs(resolved, unit.squad_size)
                    for j, row in enumerate(rows):
                        if j < len(dmg_strs):
                            row["damage"] = dmg_strs[j]

                # Build equipment string
                eq_parts = []
                seen_ba_eq: set[tuple[str, str]] = set()   # dedup BA equipment
                seen_no_loc: set[tuple[str, str]] = set()  # dedup location-irrelevant equipment
                for eq in unit.equipment:
                    # BA: skip duplicates (same key+subtype, location irrelevant)
                    if isinstance(unit, BattleArmor):
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
                    if not isinstance(unit, BattleArmor) and eq.location and (eq_obj is None or eq_obj.hasLoc):
                        label += f" [{eq.location}]"
                    if eq.uses:
                        uses_str = str(int(eq.uses)) if eq.uses % 1 == 0 else f"{eq.uses:.1f}"
                        label += f" ({uses_str})"
                    eq_parts.append(label)
                equipment_str = ", ".join(eq_parts)

                # Render
                if isinstance(unit, BattleMech):
                    r = QuadCardRenderer() if unit.motive_type == BattleMech.QUAD else MechCardRenderer()
                    pixmap = r.render(unit, profile, rows, equipment_str)
                elif isinstance(unit, CombatVehicle):
                    pixmap = VehicleCardRenderer().render(unit, profile, rows, equipment_str)
                elif isinstance(unit, AeroSpaceFighter):
                    pixmap = AeroCardRenderer().render(unit, profile, rows, equipment_str)
                elif isinstance(unit, BattleArmor):
                    pixmap = BattleArmorRenderer().render(unit, profile, rows, equipment_str)
                else:
                    result.error = f"Unit type not yet supported for export: {type(unit).__name__}"
                    self.file_done.emit(result)
                    continue

                base = os.path.splitext(os.path.basename(path))[0]
                if self._fmt in ("PNG", "All"):
                    export_png(pixmap, os.path.join(self._out_dir, f"{base}.png"))
                if self._fmt in ("PDF", "All"):
                    export_pdf(pixmap, os.path.join(self._out_dir, f"{base}.pdf"))

                result.success = True
            except Exception as exc:
                result.error = f"{type(exc).__name__}: {exc}"

            self.file_done.emit(result)

        self.finished_all.emit()
