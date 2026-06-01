"""Test each unknown item through the actual normalizers to see which ones fail."""
import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.parsers.name_normalizer import normalize_weapon, normalize_equipment, normalize_ammo

# Collect all unique unknown item names from warnings
unknown_weapons = {}
unknown_items = {}

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

print("=== WEAPONS: still failing after normalization ===")
still_unknown_weapons = {}
now_resolved_weapons = {}
for name, count in sorted(unknown_weapons.items(), key=lambda x: -x[1]):
    result = normalize_weapon(name)
    if result:
        now_resolved_weapons[name] = (result, count)
    else:
        still_unknown_weapons[name] = count

for name, count in sorted(still_unknown_weapons.items(), key=lambda x: -x[1]):
    print(f"  {count:4d}  {name!r}")

print()
print(f"  ({len(now_resolved_weapons)} weapons already resolve correctly)")

print()
print("=== EQUIPMENT: still failing after normalization ===")
still_unknown_items = {}
now_resolved_items = {}
ammo_resolved = {}
for name, count in sorted(unknown_items.items(), key=lambda x: -x[1]):
    ammo_result = normalize_ammo(name)
    if ammo_result:
        ammo_resolved[name] = (ammo_result, count)
        continue
    result = normalize_equipment(name)
    if result:
        now_resolved_items[name] = (result, count)
    else:
        still_unknown_items[name] = count

for name, count in sorted(still_unknown_items.items(), key=lambda x: -x[1]):
    print(f"  {count:4d}  {name!r}")

print()
print(f"  ({len(now_resolved_items)} items already resolve via equipment normalizer)")
print(f"  ({len(ammo_resolved)} items already resolve via ammo normalizer)")

print()
print("=== TRANSPORTERS ===")
transporters = {}
with open(PROJECT_ROOT / "parse_check_results.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if not row["warnings"]:
            continue
        for w in row["warnings"].split(" | "):
            w = w.strip()
            if "Unknown transporter:" in w:
                item = w.split("Unknown transporter:", 1)[1].strip().strip("'")
                transporters[item] = transporters.get(item, 0) + 1

for name, count in sorted(transporters.items(), key=lambda x: -x[1]):
    print(f"  {count:4d}  {name!r}")
