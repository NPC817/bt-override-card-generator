"""Categorize all unknowns into: true YAML additions, ammo prefix fixes, alias map fixes."""
import csv, sys, re
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.parsers.name_normalizer import (
    normalize_weapon, normalize_equipment, normalize_ammo,
    _ALIAS_MAP, _EQUIPMENT_MAP, _WEAPON_MAP, _munge
)
import yaml

# Load YAML keys
with open(PROJECT_ROOT / "data" / "weapons.yaml") as f:
    weapon_keys = set(yaml.safe_load(f).keys())
with open(PROJECT_ROOT / "data" / "equipment.yaml") as f:
    equip_keys = set(yaml.safe_load(f).keys())

unknown_weapons: dict[str, int] = {}
unknown_items: dict[str, int] = {}
unknown_transporters: dict[str, int] = {}

with open(PROJECT_ROOT / "parse_check_results.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if not row["warnings"]:
            continue
        for w in row["warnings"].split(" | "):
            w = w.strip()
            if "Unknown weapon:" in w:
                item = w.split("Unknown weapon:", 1)[1].strip().strip("'")
                unknown_weapons[item] = unknown_weapons.get(item, 0) + 1
            elif "Unknown BA item:" in w:
                item = w.split("Unknown BA item:", 1)[1].strip().strip("'")
                unknown_items[item] = unknown_items.get(item, 0) + 1
            elif "Unknown item in" in w and ":" in w:
                item = w.split(":", 1)[1].strip().strip("'")
                unknown_items[item] = unknown_items.get(item, 0) + 1
            elif "Unknown transporter:" in w:
                item = w.split("Unknown transporter:", 1)[1].strip().strip("'")
                unknown_transporters[item] = unknown_transporters.get(item, 0) + 1


def is_ammo(name: str) -> bool:
    return "ammo" in name.lower() or name.endswith("Ammo") or "ammo" in name


def strip_clean(name: str) -> str:
    name = re.sub(r"^\d+\s*", "", name)
    name = re.sub(r":OMNI\b", "", name, flags=re.IGNORECASE)
    name = re.sub(r":SIZE:[\d.]+", "", name)
    name = re.sub(r"\s*\(ST\)", "", name)
    name = re.sub(r"\s*\(PT\)", "", name)
    name = re.sub(r"\s*-+\s*(troopers|Half).*", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\s*\[[^\]]*\]\s*", " ", name)
    return re.sub(r"\s+", " ", name).strip()


def would_resolve_after_alias_fix(name: str, is_weapon: bool) -> str | None:
    """Check if munged name is in alias map — i.e., would resolve with an alias fix."""
    cleaned = strip_clean(name)
    from src.parsers.name_normalizer import _strip_parens
    stripped = _strip_parens(cleaned)
    for candidate in (cleaned, stripped, name):
        key = _munge(candidate)
        # Check if key maps to something in weapon/equip YAML
        for test_key in (key, key.lstrip("cl"), key.lstrip("is")):
            if test_key in _ALIAS_MAP:
                target = _ALIAS_MAP[test_key]
                if is_weapon and target in weapon_keys:
                    return target
                if not is_weapon and target in equip_keys:
                    return target
    return None


# ─── WEAPONS ────────────────────────────────────────────────────────────────
print("=" * 70)
print("WEAPONS.yaml ADDITIONS NEEDED")
print("(items from weapon slots that need new weapon entries)")
print("=" * 70)

true_weapon_additions = {}
weapon_count_prefix = {}
weapon_cargo = {}
weapon_alias_fix = {}
weapon_ammo = {}

for name, count in sorted(unknown_weapons.items(), key=lambda x: -x[1]):
    cleaned = strip_clean(name)

    # Cargo/logistics items in weapon slots
    if re.search(r"cargo|lift hoist|remote sensor|chaff pod|c3 remote|smalls shield|spikes|vib", cleaned, re.IGNORECASE):
        weapon_cargo[name] = count
        continue

    # Check if it's ammo
    if is_ammo(cleaned):
        weapon_ammo[name] = count
        continue

    # Check alias fix would help
    alias_target = would_resolve_after_alias_fix(name, is_weapon=True)
    if alias_target:
        weapon_alias_fix[name] = (alias_target, count)
        continue

    true_weapon_additions[name] = count

for name, count in sorted(true_weapon_additions.items(), key=lambda x: -x[1]):
    print(f"  {count:3d}  {name}")

print(f"\nTotal: {len(true_weapon_additions)} new weapon entries")

# ─── EQUIPMENT ──────────────────────────────────────────────────────────────
print()
print("=" * 70)
print("EQUIPMENT.yaml ADDITIONS NEEDED")
print("=" * 70)

ammo_prefix_fix = {}
equip_alias_fix = {}
true_equip_additions = {}

for name, count in sorted(unknown_items.items(), key=lambda x: -x[1]):
    cleaned = strip_clean(name)

    if is_ammo(cleaned) or is_ammo(name):
        ammo_prefix_fix[name] = count
        continue

    alias_target = would_resolve_after_alias_fix(name, is_weapon=False)
    if alias_target:
        equip_alias_fix[name] = (alias_target, count)
        continue

    true_equip_additions[name] = count

for name, count in sorted(true_equip_additions.items(), key=lambda x: -x[1]):
    print(f"  {count:3d}  {name}")

print(f"\nTotal: {len(true_equip_additions)} new equipment entries")

# ─── ALIAS MAP FIXES ─────────────────────────────────────────────────────────
print()
print("=" * 70)
print("ALIAS MAP FIXES (YAML entry exists, just mapping missing)")
print("=" * 70)
print("\nWeapons:")
for name, (target, count) in sorted(weapon_alias_fix.items(), key=lambda x: -x[1][1]):
    print(f"  {count:3d}  {name!r} → {target}")
print("\nEquipment:")
for name, (target, count) in sorted(equip_alias_fix.items(), key=lambda x: -x[1][1]):
    print(f"  {count:3d}  {name!r} → {target}")

# ─── AMMO PREFIX FIXES ───────────────────────────────────────────────────────
print()
print("=" * 70)
print("AMMO PREFIX RULES NEEDED (no new YAML entries, just parser fixes)")
print("=" * 70)
all_ammo = {**ammo_prefix_fix}
for name, count in sorted(all_ammo.items(), key=lambda x: -x[1]):
    print(f"  {count:3d}  {name}")

# ─── TRANSPORTERS ────────────────────────────────────────────────────────────
print()
print("=" * 70)
print("TRANSPORTERS (name normalization fix needed)")
print("=" * 70)
for name, count in sorted(unknown_transporters.items(), key=lambda x: -x[1]):
    print(f"  {count:3d}  {name}")

# ─── NON-WEAPON ITEMS IN WEAPON SLOTS ────────────────────────────────────────
print()
print("=" * 70)
print("CARGO/UTILITY IN WEAPON SLOTS (omit or ignore)")
print("=" * 70)
for name, count in sorted(weapon_cargo.items(), key=lambda x: -x[1]):
    print(f"  {count:3d}  {name}")
