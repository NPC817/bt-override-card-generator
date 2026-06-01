"""Analyze parse_check_results.csv and show specific unknown item names."""
import csv
from collections import Counter

unknown_items = Counter()
unknown_weapons = Counter()
unknown_transporters = Counter()
files_with_warnings = Counter()

with open("parse_check_results.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if not row["warnings"]:
            continue
        folder = row["folder"]
        for w in row["warnings"].split(" | "):
            w = w.strip()
            if "Unknown weapon:" in w:
                item = w.split("Unknown weapon:", 1)[1].strip().strip("'")
                unknown_weapons[item] += 1
            elif "Unknown BA item:" in w:
                item = w.split("Unknown BA item:", 1)[1].strip().strip("'")
                unknown_items[item] += 1
            elif "Unknown item in" in w and ":" in w:
                item = w.split(":", 1)[1].strip().strip("'")
                unknown_items[item] += 1
            elif "Unknown transporter:" in w:
                item = w.split("Unknown transporter:", 1)[1].strip().strip("'")
                unknown_transporters[item] += 1
        files_with_warnings[folder] += 1

print("=== UNKNOWN WEAPONS (top 50) ===")
for name, count in unknown_weapons.most_common(50):
    print(f"  {count:4d}  {name}")

print()
print("=== UNKNOWN EQUIPMENT/BA ITEMS (top 60) ===")
for name, count in unknown_items.most_common(60):
    print(f"  {count:4d}  {name}")

print()
print("=== UNKNOWN TRANSPORTERS ===")
for name, count in unknown_transporters.most_common():
    print(f"  {count:4d}  {name}")

print()
print("=== ALL UNIQUE UNKNOWN WEAPONS ===")
for name, count in sorted(unknown_weapons.items()):
    print(f"  {count:4d}  {name}")

print()
print("=== ALL UNIQUE UNKNOWN ITEMS (sorted) ===")
for name, count in sorted(unknown_items.items()):
    print(f"  {count:4d}  {name}")
