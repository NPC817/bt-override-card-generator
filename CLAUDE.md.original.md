# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Desktop application (Python + PyQt6) that recreates and extends the DFA Wargaming Battletech Override Card Generator. Converts Classic BattleTech unit files (MTF/BLK) into Override-format cards with configurable house rules, multi-tab editing, bulk export, and PDF output.

**Constraint:** All work must stay within this project directory — never create or reference files outside of it.

## Commands

```bash
# Setup (run once)
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt

# Run the app
python main.py

# Run all tests
pytest tests/

# Run a single test file
pytest tests/test_conversion.py -v
```

## Agents

This project has five specialized agents. Use them proactively for their domains — don't wait to be asked.

### web-page-scraper
Use when you need to analyze, extract, or understand web page content, structure, JavaScript logic, or UX/layout. Examples: scraping data from a site, reverse-engineering JavaScript behavior, auditing page layouts, extracting product names/prices.

### codebase-explorer
Use when you need to locate where specific functionality, classes, functions, or patterns exist in the codebase; identify all files that would need to be updated for a given change; or map dependencies between components. Prefer this over manual Glob/Grep for any non-trivial codebase search.

### code-reviewer
Use proactively after any significant code change — new features, refactors, or multi-file edits. Reviews for correctness, efficiency, cleanliness, and performance. Can also provide independent second opinions on migration safety or architectural decisions.

### multi-format-researcher
Use when you need to analyze or synthesize content across multiple file types — text files, markdown, PDFs, images, and other media. Ideal for cross-referencing information from the `reference/rules/` PDFs against code, or summarizing mixed-format datasets.

### battletech-unit-converter
Use for any Battletech unit construction or conversion question: Classic BattleTech → Override conversion rules, tonnage calculations, component compatibility, tech base or era conversions, and rulebook interpretation. This agent has access to the `reference/rules/` rulebooks and the `battletech_override_core_rules`.

## Architecture

```
src/
  models/      # Data classes: AbstractUnit, BattleMech, CombatVehicle, AeroSpaceFighter,
               #   BattleArmor, Infantry, Weapon, Equipment, DataStore (YAML loader)
  engine/      # ConversionEngine (armor/structure/heat/move formulas), TicGrouper, BatchProcessor
  parsers/     # MtfParser, BlkParser, NameNormalizer (MegaMek names → YAML keys)
  renderer/    # Card renderers per unit type (QPainter-based), PdfExporter, PngExporter
  ui/          # MainWindow (tabbed), CardTab, weapons/equipment panels, bulk dialog, settings dialog
  settings/    # ConversionProfile dataclass, ProfileManager (YAML persistence in data/profiles/)
data/
  weapons.yaml    # 100+ weapon definitions — source of truth
  equipment.yaml  # 70+ equipment definitions — source of truth
  profiles/       # User-saved house rule profiles
fonts/            # Falcon (regular/bold) and Vegas fonts — loaded at startup via QFontDatabase
images/           # Card base PNGs and unit silhouettes — used by card renderers
tests/
reference/
  example_js/card_gen.js     # Reference implementation to port from (588 KB, minified)
  example_cards/             # 9 PNG validation targets
  megamek_files/             # 9 MTF/BLK test files
  rules/                     # Rulebooks (PDF)
```

## TMM Formula

TMM is computed from MP using `a = 2 * mp`: `a<5→0, a<9→1, a<13→2, a<19→3, a<35→4, else 5`.
For mechs: `destinyTMM = "walkTMM / runTMM"` (add `/ jumpTMM+1` if jump > 0).
For vehicles: `destinyTMM = "cruiseTMM / flankTMM"` (VTOL gets +1 to each value).

## Card Renderer

Canvas: 2100 × 1500 px. Coordinates match `card_gen.js` directly.
- `src/renderer/card_renderer.py` — base class with pip drawing, text helpers, image loading; font state managed via `_FontState` class
- `src/renderer/mech_renderer.py` — `MechCardRenderer` (biped + `QuadCardRenderer` subclass)
- `src/renderer/vehicle_renderer.py` — `VehicleCardRenderer` (tracked/wheeled/hover/VTOL)
- `src/renderer/pdf_exporter.py` — reportlab PDF export (`export_pdf` single-page, `export_pdf_multi` multi-page)
- `src/renderer/png_exporter.py` — `QPixmap.save()` PNG export

Form-fillable PDF export is **not yet implemented** (stub in `MainWindow._export_form_pdf`).

Pips are hexagons drawn with: `x += round(16.5 * step.x)`, `y += round(step.y * h)` where `h = 15*sqrt(3)+1.5`. Armor pips are black/white; structure pips are red outline.

Font size constants (in `card_renderer.py`):
- `FS_XXLARGE = 60` — unit name
- `FS_XLARGE  = 48` — section headers, column headers
- `FS_LARGE   = 38` — stat labels and values
- `FS_MEDIUM  = 28` — weapon rows, heat numbers
- `FS_SMALL   = 15` — pip radius (not a font size)

## Key Conversion Formulas

These were reverse-engineered from `reference/example_js/card_gen.js` and match the DFA web app:

| Value | Formula |
|---|---|
| Mech armor (most zones) | `max(round(raw / 3), 1)` — divisor configurable |
| Mech torso combined (CT+LT+RT on card) | `max(round(total / 6), 1)` |
| Mech head armor | Stepped: ≤2→1, ≤5→2, ≤7→3, else 4 |
| Vehicle armor per zone | `max(round(raw / 4), 1)` — divisor configurable |
| Vehicle structure | `max(round(ceil(tonnage/10) / 3), 1)` |
| Heat sinks (Sinks on card) | `round(sinks / 5)` standard; `round((2*sinks) / 5)` DHS |
| Movement | 1:1 copy of walk/run/jump MP — multiplier configurable |

## House Rules System

`ConversionProfile` (in `src/settings/profile.py`) stores all adjustable scales:
- `mech_armor_divisor` (default 3.0)
- `vehicle_armor_divisor` (default 4.0)
- `heat_scale_max` (default 5, range 1–30)
- `heat_sink_divisor` (default 5.0)
- `move_scale_multiplier` (default 1.0)
- `weapon_overrides` — dict of per-weapon stat overrides

Profiles are stored as YAML files under `data/profiles/`. The built-in "Default" profile is never persisted to disk and cannot be deleted.

## Key Code Patterns

**Parsers:** `src/parsers/blk_parser.py` uses module-level `_tag(content, name)` and `_tag_lines(content, name)` helpers. Both `parse_blk()` and `_parse_ba()` bind a local alias `tag = lambda n: _tag(content, n)` for readability.

**Weapon TIC grouping:** `TicGroup` in `src/engine/tic_grouper.py` implements `__getattr__` to handle dynamic `use_<flag>` boolean checks (e.g. `use_srm`, `use_lrm`) for all flags in `_SPECIAL_FLAGS`. `use_tc` and `use_os` are explicit `@property` methods since they use different logic. The scoring function `_score_weapon_for_tic` uses `getattr(tig, f"use_{flag}")` to check compatibility.

**Font loading:** `_FontState` class in `src/renderer/card_renderer.py` holds `loaded`, `falcon`, and `vegas` as class attributes. `_load_fonts()` sets them once; `_font(size, bold)` calls it on every use.

## Testing

469 tests in `tests/`. Validation reference files:
- `reference/megamek_files/Hunchback HBK-4G.mtf` — biped mech, 50t, walkMP 4
- `reference/megamek_files/Condor Heavy Hover Tank (Liao).blk` — hover vehicle, 50t, cruiseMP 8
- `reference/example_cards/btd_hunchback_hbk4g.png` — expected card output for Hunchback
