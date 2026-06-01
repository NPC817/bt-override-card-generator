# BT Override Card Generator

Desktop application for converting Classic BattleTech unit files (MTF/BLK) to
[BattleTech: Override](https://dfawargaming.com) format cards — the fast-playing,
fan-made rules system by **Death From Above Wargaming**.

## About BattleTech: Override

BattleTech: Override is a fan-made rules system created by **Death From Above
Wargaming (DFA)** that blends the BattleMech combat from *MechWarrior: Destiny*
with the streamlined movement and targeting of *Alpha Strike*, plus inspiration
from *Classic BattleTech*. It hits the sweet spot — more simulation than Alpha
Strike, faster than Classic.

This application is an unofficial companion tool. It reads MegaMek MTF/BLK files
and renders Override-format cards with live preview, bulk export, and
configurable house rules — all matching the DFA Wargaming web app's output.

All credit for the Override system goes to the DFA team:

| | |
|---|---|
| Website | [dfawargaming.com](https://dfawargaming.com) |
| YouTube | [Death From Above Wargaming](https://www.youtube.com/@deathfromabovewargaming) |
| Patreon | [patreon.com/dfawargaming](https://patreon.com/dfawargaming) |
| Rules Reference | [Override Core Rules v5.2](https://archive.org/details/override-core-rules-reference-v-5.2) |

## Features

- **Parse MTF & BLK files** — BattleMechs, Combat Vehicles, AeroSpace Fighters, Battle Armor, and Infantry
- **Live card preview** — See the Override card update as you tweak loadouts
- **Configurable house rules** — Adjust armor divisors, heat scale, movement multiplier, and per-weapon overrides via profiles
- **Multi-tab editing** — Work on multiple units simultaneously
- **Weapon & equipment panels** — Search, filter, add/remove weapons and equipment with detailed stat editing
- **TIC grouping** — Auto-groups weapons into TIC slots following Override rules
- **Export formats** — PNG, PDF (single + multi-page), and OVR (Override JSON)
- **Bulk import/export** — Convert entire directories of MTF/BLK files at once
- **Unit Database Browser** — Search 100+ pre-built Override units
- **Force import/export** — Import `.force` or MegaMek `.mul` rosters, export `.force` files
- **Dark mode** — Toggleable light/dark theme
- **Print support** — Print individual cards or all open tabs
- **Check for Updates** — Notify and auto-install new releases from GitHub

## Screenshots

*Coming soon*

## Installation

### Option 1: Download Release (Windows)

1. Go to [Releases](https://github.com/NPC817/bt-override-card-generator/releases)
2. Download the latest `BT_Override_Card_Generator_vX.Y.Z.zip`
3. Extract to a folder of your choice
4. Run `BTOverrideCardGenerator.exe`

### Option 2: Run from Source

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python main.py
```

**Requirements:** Python 3.10+, PyQt6, PyYAML, reportlab, Pillow

## Usage

1. **File → Open MTF/BLK** to load a unit file
2. Tweak weapons, equipment, armor, or heat sinks in the panels
3. Adjust conversion rules via **Settings → House Rule Profiles**
4. **File → Export PNG/PDF** to save your card
5. **File → Bulk Import/Export** to convert many files at once

### Unit Database

The **Browse Unit Database** dialog (Ctrl+Shift+D) lets you search pre-built
units by name, type, or source. Double-click to open as a card.

## House Rule Profiles

Profiles let you customize the conversion math to match your table's house
rules. Adjustable settings include:

| Setting | Default | Description |
|---|---|---|
| Mech Armor Divisor | 3.0 | Divides raw armor per zone |
| Vehicle Armor Divisor | 4.0 | Divides raw vehicle armor per zone |
| Heat Scale Max | 5 | Maximum heat on the Override scale |
| Heat Sink Divisor | 5.0 | Divides total heat sinks |
| Move Scale Multiplier | 1.0 | Multiplies walk/run/jump MP |
| Weapon Overrides | — | Per-weapon damage/heat/range overrides |

Profiles are saved as YAML in `data/profiles/` and survive updates.

## Building from Source

```bash
build.bat
```

Output: `dist/BT_Override_Card_Generator/` (runnable) and
`dist/Release/BT_Override_Card_Generator_vX.Y.Z.zip` (distributable).

## Project Structure

```
src/
  models/      # Data classes — AbstractUnit, BattleMech, CombatVehicle, etc.
  engine/      # ConversionEngine, TicGrouper, BatchProcessor
  parsers/     # MtfParser, BlkParser, NameNormalizer
  renderer/    # Card renderers (QPainter), PdfExporter, PngExporter
  ui/          # MainWindow, CardTab, panels, dialogs, settings
  settings/    # ConversionProfile, ProfileManager
data/
  weapons.yaml   # 100+ weapon definitions
  equipment.yaml # 70+ equipment definitions
  units.zip      # Pre-built unit database
  profiles/      # User-saved house rule profiles (not in repo)
fonts/        # Falcon + Vegas fonts
images/       # Card base PNGs + unit silhouettes
```

## Tech Stack

Python 3.10+ | PyQt6 | PyYAML | reportlab | Pillow | PyInstaller

## Acknowledgments

- **Death From Above Wargaming** — Creators of the BattleTech: Override system
- **MegaMek** — MTF/BLK file format used as import source
- **Catalyst Game Labs & Topps** — BattleTech and MechWarrior are their trademarks

## Disclaimer

BattleTech: Override is a fan-made system. This card generator is an unofficial
community tool — not affiliated with or endorsed by Death From Above Wargaming,
Catalyst Game Labs, or The Topps Company.
