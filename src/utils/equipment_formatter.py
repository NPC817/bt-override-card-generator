"""Shared equipment item builder for card display.

Extracted from card_tab.py and batch_processor.py to avoid duplication
and to support ammo tracking with inline pips.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.unit import AbstractUnit
    from ..settings.profile import ConversionProfile

from ..models.battle_armor import BattleArmor
from ..models.data_store import DataStore


def build_equipment_items(
    unit: AbstractUnit, profile: ConversionProfile
) -> list[dict]:
    """Build list of equipment display items for a unit's card.

    Returns list of dicts:
        {"label": str, "is_ammo": bool, "shots": int, "location": str}

    When track_ammo is enabled, ammo entries with shots_per_ton > 0
    are marked is_ammo=True with shot counts for pip rendering.
    Ton count comes from eq.uses (set by parser dedup).
    """
    items: list[dict] = []
    seen_ba_eq: set[tuple[str, str, str]] = set()
    seen_no_loc: set[tuple[str, str, str]] = set()

    track_ammo = getattr(profile, "track_ammo", False)

    for eq in unit.equipment:
        # BA: deduplicate by (key, subtype, ammo_variant)
        if isinstance(unit, BattleArmor):
            sig = (eq.equipment_key, eq.subtype, eq.ammo_variant)
            if sig in seen_ba_eq:
                continue
            seen_ba_eq.add(sig)

        # Look up equipment name and data
        label = eq.equipment_key
        eq_obj = None
        try:
            eq_obj = DataStore.equipment(eq.equipment_key)
            label = eq_obj.name
        except KeyError:
            pass

        # Skip duplicates for location-irrelevant equipment
        if eq_obj is not None and not eq_obj.hasLoc:
            sig = (eq.equipment_key, eq.subtype, eq.ammo_variant)
            if sig in seen_no_loc:
                continue
            seen_no_loc.add(sig)

        # Ammo tracking: use eq.uses as ton count (set by parser dedup)
        is_ammo = (eq_obj is not None and eq_obj.shots_per_ton > 0)
        if track_ammo and is_ammo:
            tons = int(eq.uses) if eq.uses > 0 else 1
            total_shots = tons * eq_obj.shots_per_ton

            if eq.location:
                label += f" [{eq.location}]"
            label += f"[{total_shots}]"

            items.append({
                "label": label,
                "is_ammo": True,
                "shots": total_shots,
                "location": eq.location,
            })
            continue

        # Regular equipment path
        if eq.subtype and eq_obj is not None and not eq_obj.specific_subtype:
            label += f" ({eq.subtype})"
        if (not isinstance(unit, BattleArmor) and eq.location
                and (eq_obj is None or eq_obj.hasLoc)):
            label += f" [{eq.location}]"
        if eq.uses and not is_ammo:
            uses_str = (str(int(eq.uses)) if eq.uses % 1 == 0
                        else f"{eq.uses:.1f}")
            label += f" ({uses_str})"

        items.append({
            "label": label,
            "is_ammo": False,
            "shots": 0,
            "location": eq.location,
        })

    return items
