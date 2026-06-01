# CLAUDE.md

Guidance for Claude Code (claude.ai/code) working in this repository.

## Project

Desktop app (Python + PyQt6). Recreates + extends DFA Wargaming Battletech Override Card Generator. Converts Classic BattleTech unit files (MTF/BLK) → Override-format cards with configurable house rules, multi-tab editing, bulk export, PDF output.

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

Five specialized agents. Use proactively — don't wait to be asked.

### web-page-scraper
Analyze/extract web page content, structure, JS logic, UX/layout. Examples: scrape data, reverse-engineer JS behavior, audit layouts, extract product names/prices.

### codebase-explorer
Locate functionality, classes, functions, patterns in codebase. Identify files needing update for given change. Map dependencies between components. Prefer over manual Glob/Grep for non-trivial searches.

### code-reviewer
Use after significant code change: new features, refactors, multi-file edits. Reviews correctness, efficiency, cleanliness, performance. Independent second opinions on migration safety, architectural decisions.

### multi-format-researcher
Analyze/synthesize content across file types: text, markdown, PDFs, images, media. Cross-reference `reference/rules/` PDFs against code. Summarize mixed-format datasets.

### battletech-unit-converter
Battletech unit construction/conversion: Classic BattleTech → Override rules, tonnage calculations, component compatibility, tech base/era conversions, rulebook interpretation. Has access to `reference/rules/` rulebooks and `battletech_override_core_rules`.

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

TMM computed from MP using `a = 2 * mp`: `a<5→0, a<9→1, a<13→2, a<19→3, a<35→4, else 5`.
Mechs: `destinyTMM = "walkTMM / runTMM"` (add `/ jumpTMM+1` if jump > 0).
Vehicles: `destinyTMM = "cruiseTMM / flankTMM"` (VTOL gets +1 to each value).

## Card Renderer

Canvas: 2100 × 1500 px. Coordinates match `card_gen.js` directly.
- `src/renderer/card_renderer.py` — base class: pip drawing, text helpers, image loading; font state via `_FontState` class
- `src/renderer/mech_renderer.py` — `MechCardRenderer` (biped + `QuadCardRenderer` subclass)
- `src/renderer/vehicle_renderer.py` — `VehicleCardRenderer` (tracked/wheeled/hover/VTOL)
- `src/renderer/pdf_exporter.py` — reportlab PDF export (`export_pdf` single-page, `export_pdf_multi` multi-page)
- `src/renderer/png_exporter.py` — `QPixmap.save()` PNG export

Form-fillable PDF export **not yet implemented** (stub in `MainWindow._export_form_pdf`).

Pips: hexagons drawn via `x += round(16.5 * step.x)`, `y += round(step.y * h)` where `h = 15*sqrt(3)+1.5`. Armor pips black/white; structure pips red outline.

Font size constants (in `card_renderer.py`):
- `FS_XXLARGE = 60` — unit name
- `FS_XLARGE  = 48` — section headers, column headers
- `FS_LARGE   = 38` — stat labels and values
- `FS_MEDIUM  = 28` — weapon rows, heat numbers
- `FS_SMALL   = 15` — pip radius (not font size)

## Key Conversion Formulas

Reverse-engineered from `reference/example_js/card_gen.js`. Match DFA web app:

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

Profiles stored as YAML in `data/profiles/`. Built-in "Default" profile never persisted to disk, cannot be deleted.

## Key Code Patterns

**Parsers:** `src/parsers/blk_parser.py` uses module-level `_tag(content, name)` and `_tag_lines(content, name)` helpers. Both `parse_blk()` and `_parse_ba()` bind local alias `tag = lambda n: _tag(content, n)` for readability.

**Weapon TIC grouping:** `TicGroup` in `src/engine/tic_grouper.py` implements `__getattr__` for dynamic `use_<flag>` boolean checks (e.g. `use_srm`, `use_lrm`) for all flags in `_SPECIAL_FLAGS`. `use_tc` and `use_os` are explicit `@property` methods (different logic). `_score_weapon_for_tic` uses `getattr(tig, f"use_{flag}")` to check compatibility.

**Font loading:** `_FontState` class in `src/renderer/card_renderer.py` holds `loaded`, `falcon`, `vegas` as class attributes. `_load_fonts()` sets them once; `_font(size, bold)` calls it on every use.

## Testing

Only run tests when requested.

469 tests in `tests/`. Three test categories:

### Parse-all coverage (`test_parse_all_files.py`)
Every MTF and BLK file in `reference/megamek_files/` is parameterized as its own test case. Validates parser doesn't crash, chassis is non-empty, tonnage/MP are sane. Warnings printed but not treated as failures.

When testing infantry pick files from this folder at random D:\Dropbox\Battletech\MUL_Files\infantry.

### Card render validation (`test_card_render.py`)
Random-sampled: picks 3 files from `reference/megamek_files/` and 3 matching files from `reference/example_cards/` on each run. Files chosen via `random.sample()` — different set every test run. Validates:
1. Destiny values (armor/structure pips, move, TMM, sinks) — read from reference PNGs by inspection
2. Weapon rows (correct names, non-empty damage, non-zero heat)
3. Pip-presence pixel tests (dark pixels at known first-pip coordinates)
4. Right-panel image comparison (reduced-resolution structural check, tolerance=35)

Reference ground truth directories:
- `reference/megamek_files/` — 100+ MTF/BLK source files
- `reference/example_cards/` — 100+ PNG reference cards
