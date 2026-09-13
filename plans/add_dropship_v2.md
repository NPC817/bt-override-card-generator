# Plan: Add Dropship Unit Type (v2)

> Supersedes `plans/add_dropship.md` (stale v1: references nonexistent files `src/engine/conversion_engine.py`, `src/ui/field_names.py`, `FighterCardRenderer`, and wrong BLK tags `<crew>`, `<structure>`).

## Context

The Override card generator supports BattleMechs, Combat Vehicles, Aerospace/Conventional Fighters, Battle Armor, and Infantry. Dropships are the next unit type. They are structurally closest to Aerospace Fighters: same 4-armor-zone + 1-structure layout, same armor conversion (aero divisor), same Thrust/TMM handling. Two subtypes exist, selected from the BLK `<motion_type>` tag:

- **Aerodyne** — card labels: Nose, Left Wing, Right Wing, Aft (fighter names). Note: aerodyne BLKs also use "Side" section names — map to Wing on the card.
- **Spheroid** — card labels: Nose, Left Side, Right Side, Aft.

Two silhouette images already exist: `images/dropship-aero.png` and `images/dropship-shpere.png` (filename typo "shpere" is intentional), both full 2100×1500 canvases.

Ground truth: the rulebooks (`battletech_override_core_rules.pdf`, `battletech_mechwarrior_destiny.pdf`) and the reference `card_gen.js` contain **no dropship rules** — this is a novel extension. Fighter code is the template, plus user-locked decisions below.

**Locked user decisions:**
- Structure: `max(round(structural_integrity / 3), 1)` (Union SI 11 → 4 pips, Leopard SI 7 → 2).
- Bay display: true bays (`mekbay`, `asfbay`, `infantrybay`, `smallcraftbay`, `dropshuttlebay`) render `"Mech Bay (12b-4d)"` (count + doors); cargo/quarters keep vehicle style `"Cargo Bay (75)"`, `"Crew Quarters (77)"` (ceil, no doors). BLK line format `name:size:doors[:door_type...]` — extra fields ignored. Same-name lines aggregate (Union `mekbay:4.0:2` + `mekbay:8.0:2` → 12 bays, 4 doors).
- BV: full dropship branch in `bv_calculator.py` + MUL cache lookup.
- TMM: `_tmm(safe_thrust) + 1` (same as fighter). DThr: `max(round(((L+R)/2 + N + A)/30), 1)` using LW/RW (aerodyne) or LS/RS (spheroid).
- Heat sinks: fighter formula `max(round(effective/5), 0)` (DHS ×2). Dropships show heat.

**Example files:** `reference/example_dropship_blk/` (7 BLKs: Broadsword, Buccaneer, Fortress, Leopard, Manatee, Overlord, Union). The external `D:\Dropbox\Battletech\MUL_Files\dropships\TRO3057R\IS\Union (2708).blk` / `Leopard CV (2581).blk` are for manual verification only — project constraint forbids referencing files outside the project dir in code/tests.

---

## Step 1 — `src/models/dropship.py` (new)

Mirror `src/models/aero.py`. Add a `Transporter` dataclass (the `UnitEquipment` dataclass in `src/models/unit.py:18-24` has no doors field — do not extend it):

```python
@dataclass
class Transporter:
    key: str            # normalized equipment key (mekbay, cargobay, ...)
    count: float = 0.0  # raw aggregated capacity (bays/tonnage/berths)
    doors: int = 0      # aggregated door count
```

`class Dropship(AbstractUnit)`:
- Constants: `AERODYNE = "Aerodyne"`, `SPHEROID = "Spheroid"`, `BAY_KEYS = frozenset({"mekbay", "asfbay", "infantrybay", "smallcraftbay", "dropshuttlebay"})`.
- Fields: `tonnage: int = 3500`, `safe_thrust: int = 3`, `max_thrust: int = 5`, `sinks: int = 30`, `has_dhs: bool = False`, `structural_integrity: int = 10`, `motive_type: str = SPHEROID`, `armor: dict = {"N": 0, "LW": 0, "RW": 0, "LS": 0, "RS": 0, "A": 0}` (superset dict — both subtypes' keys always present), `transporters: list[Transporter] = []`, `fuel: int = 0` (parsed/serialized, not displayed).
- Helpers: `left_key`/`right_key` properties → `"LW"/"RW"` if aerodyne else `"LS"/"RS"`; `transporter(key) -> Transporter | None`.
- Destiny properties (mirror `aero.py`):
  - `unit_type_label` → `"Dropship"`
  - `destiny_move` → `str(self.safe_thrust)`
  - `destiny_sinks` → `max(_r(effective / 5), 0)` (DHS ×2)
  - `destiny_tmm` → `str(_tmm(self.safe_thrust) + 1)`
  - `dthr` → `max(_r(((left + right) / 2 + nose + aft) / 30), 1)` using `left_key`/`right_key`
  - `destiny_armor(zone, divisor=4.0)` → `max(_r(raw / divisor), 1)`
  - `destiny_structure()` → `max(_r(self.structural_integrity / 3), 1)`
- `to_dict`/`from_dict` with `unit_type="Dropship"`; serialize `motive_type`, `structural_integrity`, `fuel`, `armor`, `transporters` (list of `{key, count, doors}`).

Reference values for tests: Union safe_thrust 3 → `_tmm(3)` = 1 → destiny_tmm "2"; dthr = round((180+180+284)/30) = 15; sinks 90 → 18; structure 11 → 4. Leopard CV: dthr = round((130+130+240)/30) = 12; structure 7 → 2.

## Step 2 — `src/parsers/blk_parser.py`

1. Import `from ..models.dropship import Dropship, Transporter`.
2. Extend `ParseResult` union (lines 13-16): `CombatVehicle | BattleArmor | AeroSpaceFighter | Infantry | Dropship`.
3. Dispatch in `parse_blk` — insert after the infantry branch (line 79), before the vehicle fallback:
   ```python
   if "dropship" in unit_type_raw:
       return _parse_dropship(content, warnings)
   ```
   No conflict with the `"aero"` check — dropship BLKs have `UnitType: Dropship` (verified in all 7 reference files).
4. `_parse_dropship(content, warnings)` — mirror `_parse_aero` (lines 452-596) with these deltas:
   - `chassis`/`variant` from `Name`/`Model`.
   - **Tonnage is float** in dropship BLKs (3600.0): `int(float(tag("tonnage")))` with try/except + warning.
   - `motion_type` lowercased: `"aerodyne"` → AERODYNE, else SPHEROID (default).
   - `safe_thrust` from `SafeThrust` tag; `max_thrust = ceil(safe_thrust * 1.5)` (no MaxThrust tag).
   - `sinks` from `heatsinks`; `has_dhs` from `sink_type == 1`; `structural_integrity` from `structural_integrity` tag; `fuel` from `fuel`. All try/except int.
   - `_detect_tech(tag, ds)` (same as aero).
   - **Transporters with door aggregation**: for each line in `tag_lines("transporters")`: split on `":"`, `name = parts[0]`, `amount = float(parts[1])` (skip ≤ 0 — sentinels and 0.0 quarters lines), `doors = int(float(parts[2]))` if `len(parts) > 2` else 0 (fields 4+ ignored). `normalize_equipment(name)` → key; unknown → warning + skip. Aggregate per key into `[amount, doors]`. Then append `UnitEquipment(equipment_key=ekey, uses=math.ceil(amount))` to `ds.equipment` AND `Transporter(key=ekey, count=amount, doors=doors)` to `ds.transporters`. Track keys in `_ds_transporter_keys` set.
   - **Armor**: `tag_lines("armor")` 4 positional lines → keys `["N","LW","RW","A"]` (aerodyne) or `["N","LS","RS","A"]` (spheroid).
   - **Equipment sections**: read `Nose Equipment`, `Left Side Equipment`, `Right Side Equipment`, `Aft Equipment`, `Hull Equipment`, `Wings Equipment`, `Fuselage Equipment` → locations `"N"`, `left_key`, `right_key`, `"A"`, `""`, `""`, `""` respectively. Copy the aero per-item loop (ammo → weapon → equipment, `_link_fcs_to_weapon`) and the dedup block (aero lines 558-594), substituting `_ds_transporter_keys` for the aero transporter key set so aggregated transporter `uses` survive dedup.
   - Do not parse `armor_type` (fighter parser ignores it too — parity).

## Step 3 — `src/parsers/name_normalizer.py`

Add one line in the transporter folding block (~line 980, next to `"lightvehiclebay": "cargobay"`):
```python
"heavyvehiclebay": "cargobay",
```
Without this, Fortress (2613).blk drops its 12 heavy-vehicle bays with "Unknown transporter" warnings. Vehicle bays fold into cargo → "Cargo Bay (416)" style (locked decision).

## Step 4 — `src/utils/equipment_formatter.py`

Keep the generic path; extract the uses suffix so dropship bays can override it. Import `Dropship` (no cycle — `dropship.py` imports only `unit.py` and `utils.math`).

```python
def _uses_suffix(unit, eq) -> str:
    if not eq.uses:
        return ""
    if isinstance(unit, Dropship) and eq.equipment_key in Dropship.BAY_KEYS:
        t = unit.transporter(eq.equipment_key)
        if t is not None:
            return f" ({int(eq.uses)}b-{t.doors}d)"
    uses_str = str(int(eq.uses)) if eq.uses % 1 == 0 else f"{eq.uses:.1f}"
    return f" ({uses_str})"
```

Replace the `label += f" ({uses_str})"` block (lines 83-86) with `label += _uses_suffix(unit, eq)`.

Expected card labels: Union → "Mech Bay (12b-4d)", "ASF Bay (2b-2d)", "Cargo Bay (75)", "1st Class Quarters (30)", "Crew Quarters (77)". Fortress → "Mech Bay (12b-1d)", "Infantry Bay (3b-1d)", "Cargo Bay (416)". Buccaneer → "Cargo Bay (565)" (lightvehiclebay + cargobay all fold to cargobay). Manatee → "Mech Bay (3b-3d)", "Steerage Quarters (65)".

## Step 5 — `src/renderer/dropship_renderer.py` (new)

Mirror `src/renderer/aero_renderer.py` with per-subtype silhouette, labels, and new pip layouts.

- `_SILHOUETTES = {AERODYNE: "dropship-aero.png", SPHEROID: "dropship-shpere.png"}` — set `self.SILHOUETTE_IMAGE` per unit in `render()` before `_build_canvas()` (base class reads the class attribute, `card_renderer.py:342-345`).
- `_DROPSHIP_LABELS`: per-subtype dict; start from `_AERO_LABELS` positions (`aero_renderer.py:20-25`); spheroid text "Left\nSide"/"Right\nSide", aerodyne "Left\nWing"/"Right\nWing".
- **Pip layouts (critical):** `draw_pips` (`card_renderer.py:161-165`) silently under-draws when `count > len(steps)`. Aero step lists max at 37; dropship armor is far larger — Union 180/4 = 45 pips, Fortress/Overlord N 220/4 = 55. Solution: a `_spiral_steps(count)` generator — rectangular spiral of `{"x","y"}` deltas out from a start point (`draw_pips` applies `x * 16.5 px` and `y * PIP_H ≈ 27.5 px` per step). 64 steps ≈ 10 rings ≈ 330×275 px, fits inside both silhouettes (spheroid sphere ~500 px diameter; aerodyne hull band ~300 px tall). Per-zone `start` coordinates are **provisional first-pass** (spheroid: N ≈ (1610, 560), LS ≈ (1450, 900), RS ≈ (1770, 900), A ≈ (1610, 1160); aerodyne hull: N ≈ (1830, 800), LW ≈ (1600, 620), RW ≈ (1600, 1000), A ≈ (1400, 800); FU structure ≈ (1610, 800) with a `[{"x":0,"y":1}] * 40` chain) — tuned in the visual-verification loop (Step 15).
- In `_draw_dropship_zones`: clamp `a_val` to `len(steps)` with a `logging.warning` (replaces silent truncation; reference max is 55 < 64).
- `render()`: `_draw_unit_header(..., move_label="Thrust:", move_x_offset=15, tmm_x_offset=15, sinks_val=None, heat_scale_max=profile.heat_scale_max, bv_val=...)`; Gunnery/Piloting labels at (1155/1300, 45); DThr at (440, 415); `_draw_weapons_table(..., has_heat=True)`; `_draw_equipment_items`; zones (two-pass: pips then labels, like aero); `_draw_condition_monitor`. Use `profile.aero_armor_divisor` (no new profile field; `settings_dialog` doesn't expose aero divisor today and needs no change).

## Step 6 — `src/ui/forms/dropship_form.py` (new)

Mirror `src/ui/forms/aero_form.py` (14-195):
- Identity: chassis, variant, tech combo.
- Stats: `_motive` combo [Aerodyne, Spheroid] → `_on_motive_changed`; `_tonnage` QSpinBox range (100, 100000) step 100; `_safe_thrust` (1-20); `_max_thrust` (2-30); `_sinks` (0-2000 — Union has 90, aero's 0-100 too small); `_dhs` checkbox; `_si` (1-200) labeled "Structural Integrity:".
- Armor: 4 spinboxes range (0, 9999) with explicit `QLabel`s (`_armor_lw_lbl` etc.) so text can swap.
- Tabs: `WeaponsPanel(unit_type="dropship", tech=...)` + `EquipmentPanel()`.
- `_on_motive_changed(text)`: swap armor labels "Left Wing:"↔"Left Side:" / "Right Wing:"↔"Right Side:"; remap existing weapon locations (`{"LS":"LW","RS":"RW"}` or reverse) via `get_weapons()` → mutate → `load_weapons()`.
- `load_unit`: armor reads `unit.armor.get(unit.left_key, 0)` / `unit.right_key`.
- `get_unit()` — **must be idempotent** (runs on every debounced preview render): build/update `Dropship`, read all widgets, then re-sync transporters from editable equipment rows preserving doors by key:
  ```python
  prev = {t.key: t.doors for t in unit.transporters}
  unit.transporters = [
      Transporter(key=eq.equipment_key, count=float(eq.uses or 1),
                  doors=prev.get(eq.equipment_key, 0))
      for eq in unit.equipment if eq.equipment_key in Dropship.BAY_KEYS]
  ```
  Round-trip behavior: bays are ordinary `UnitEquipment` rows in the EquipmentPanel (uses spinbox visible — all bay YAML entries are `isLimited: true`); doors survive edits; manually added bay rows get 0 doors; deleted rows drop their transporter.

## Step 7 — `src/ui/weapons_panel.py`

- Add `_DROPSHIP_LOCATIONS = ["N", "LW", "RW", "LS", "RS", "A", "--"]` (both sets so units keep valid entries across subtype switches; `tic_grouper` already maps LW/LS → left arc, RW/RS → right arc, AFT → rear — no engine change).
- `__init__` branch: `elif unit_type == "dropship": self._locations = _DROPSHIP_LOCATIONS` (near lines 53-60).
- Include `"dropship"` in the Auto-Group button condition (line 76).

## Step 8 — `src/ui/card_tab.py`

- Combo (48-52): insert `"Dropship"` after `"Fighter"` → `["BattleMech", "Combat Vehicle", "Fighter", "Dropship", "Battle Armor", "Infantry"]`.
- `_build_forms` (81-96): instantiate `DropshipForm`, wire `changed`, add to stack at index 3 (between aero and BA).
- `load_unit` type_map (126-129): `Dropship: 3` (shift BattleArmor→4, Infantry→5).
- `render_card` (172-240): add after aero branch: `elif isinstance(self.unit, Dropship): renderer = DropshipCardRenderer()` then render with same `weapons_rows`/`equipment_items` pipeline.

## Step 9 — `src/ui/main_window.py`

Add `"Dropship": Dropship` + local import to both `_type_map` dicts: `_load_ovr` (287-293) and `_import_force` (340-346). No other changes (`_import_file` already calls `parse_blk` + `calculate_bv` generically).

## Step 10 — `src/ui/unit_database_dialog.py`

- `_get_type_map()` (23-37): add `"Dropship": Dropship`.
- Type filter combo (80-83): add `"Dropship"` after `"AeroSpaceFighter"`.
- Tonnage filter spinboxes (94-103): raise max 999 → 99999 (dropships are 1900-3600 t; would be unselectable under range filters otherwise).

## Step 11 — `src/engine/batch_processor.py`

Import `Dropship` + `DropshipCardRenderer`; add `elif isinstance(unit, Dropship):` branch to the render dispatch (124-140) after the aero branch.

## Step 12 — `src/engine/bv_calculator.py`

- Dispatch (230-250): `elif isinstance(unit, Dropship): return _calculate_dropship_bv(unit)`.
- MUL cache: no code change — `_lookup_bv` (214-223) keys `f"{chassis}|{variant}|{unit_type_label}".upper()` → `UNION|(2708)|DROPSHIP`. `data/bv_lookup.yaml` has 0 dropship entries; misses cleanly, entries can be added later in existing format.
- New branch mirroring `_calculate_aero_bv` (694-800):
  - `_dropship_defensive_br`: `total_armor * 2.5 * armor_mod` + `structural_integrity * 2.0` (SI instead of aero's thrust-based SI) + `_defensive_equipment_bv` − ammo penalty; type modifier 1.2 aerodyne / 1.1 spheroid (+0.3 stealth).
  - `_dropship_offensive_br`: reuse `_aero_offensive_br` with a new optional `weight_divisor` param (adds `tonnage / weight_divisor` before speed factor; aero callers unaffected); dropships use 10.0 (3600t/10 = 360 before SF — `/2` like vehicles would dwarf weapon BV).
  - Small refactor: extract the per-ammo-type −15 penalty loop from `_aero_defensive_br` (720-734) into `_aero_style_ammo_penalty(unit)` shared by both.
- `calculate_bv` returns `max(round(dbr + obr), 1)`.

## Step 13 — `src/version.py`

Bump `__version__` "0.1.8" → "0.1.9".

## Step 14 — Tests

Constraint: tests reference only `reference/example_dropship_blk/` (external MUL_Files paths are manual verification only).

**`tests/test_dropship_parser.py`** (new):
- Parameterized parse-all over `reference/example_dropship_blk/*.blk`: isinstance Dropship, non-empty chassis, tonnage > 0.
- Union (2708) specifics (re-verify values against the example-folder file when writing tests): SPHEROID; armor N/LS/RS/A = 180/180/180/104; safe_thrust 3, max_thrust 5, SI 11, sinks 90, not DHS; Left Side Equipment weapons → location "LS"; `transporter("mekbay")` = 12.0 count / 4 doors (two lines aggregated); `transporter("asfbay")` = 2.0 / 2; equipment mekbay uses 12.0, cargobay uses 75.0 (ceil of 74.5); destiny: armor N = 45, structure 4, sinks 18, tmm "2", dthr 15; `build_equipment_items` labels contain "Mech Bay (12b-4d)", "ASF Bay (2b-2d)", "Cargo Bay (75)", "Crew Quarters (77)".
- Leopard (2537): AERODYNE; armor LW/RW; Left Side Equipment weapons → "LW"; SI 7 → structure 2; dthr 12.
- Fortress: `transporter("infantrybay")` 3.0/1; heavyvehiclebay folds to cargobay (equipment cargobay uses 416.0); no "Unknown transporter" warnings.
- Buccaneer: cargobay uses 565.0 (lightvehiclebay fold-in).
- Round-trip: `Dropship.from_dict(unit.to_dict())` preserves motive_type, SI, armor keys, transporter counts/doors, weapons, equipment.

**`tests/test_dropship_render.py`** (new):
- Render Union + Leopard via `DropshipCardRenderer` (using the same weapon-row/equipment pipeline as `card_tab.render_card`); assert 2100×1500 non-null.
- Pip-presence pixel checks (reuse `_has_dark_pixel_near` pattern from `test_card_render.py`) at each zone's `start` coordinate from `_DROPSHIP_PIPS` — pins the layout constants.
- Save both renders to `tmp_path` PNGs for the visual-verification loop.

**`tests/test_batch.py`**: add a dedicated dropship test (don't touch `ALL_SUPPORTED` to avoid disturbing count-based assertions): batch-export Union + Leopard BLKs to PNG via `BatchProcessor`, assert 2 PNGs.

**`tests/test_bv_calculator.py`**: smoke test `calculate_bv(parsed_union) > 0` and int (cache misses by design).

**`tests/test_parse_all_files.py`**: no change (scans `reference/megamek_files/` only).

## Step 15 — Visual-verification loop (mandatory — no reference cards exist)

1. Run `pytest tests/test_dropship_render.py`; open the two PNGs dumped to tmp.
2. Per zone: pip spiral inside silhouette? label not colliding with spiral? FU structure chain centered on hull?
3. Adjust `_DROPSHIP_PIPS` start coordinates (and label positions if needed). Expected first-pass corrections: aerodyne N/A spirals flanking nose/tail at y≈800, LW/RW spirals over upper/lower wings.
4. Re-run render test (pixel assertions track the constants automatically).

## Step 16 — Manual app verification

1. `python main.py` → open `reference/example_dropship_blk/Union (2708).blk`: tab type "Dropship"; header Thrust 3, TMM 2, Sinks 18, DThr 15, heat column present; spheroid silhouette; Nose 45 / Left Side 45 / Right Side 45 / Aft 26 pips; FU 4 red pips; equipment "Mech Bay (12b-4d), ASF Bay (2b-2d), Cargo Bay (75), 1st Class Quarters (30), Crew Quarters (77)". Also open the external MUL `Union (2708).blk` and `Leopard CV (2581).blk` manually.
2. Leopard (2537).blk: aerodyne silhouette, "Left Wing/Right Wing" labels, structure 2.
3. Form: switch Motive Type Spheroid↔Aerodyne — armor labels and weapon locations remap.
4. Save `.ovr` → reopen; export `.force` → re-import; Unit Database type filter shows "Dropship".
5. Batch export both BLKs to PNG/PDF.
6. `pytest` full suite green.

## Step 17 — Edge cases

| Case | Handling |
|---|---|
| Unknown transporter name | warning + skip (existing convention); `heavyvehiclebay` now mapped |
| 2-field transporter line (no doors) | doors = 0 |
| `amount <= 0` lines (`2ndclassquarters:0.0:0`) | skipped (existing convention) |
| 4th/5th fields (`:3:Foot`) | ignored |
| Missing `structural_integrity` tag | default 10 → 3 pips |
| Aerodyne BLK using "Side" section names | mapped to LW/RW |
| Armor pips > 64 (raw > 256) | clamped + `logging.warning` |
| Manual bay edit in EquipmentPanel | doors preserved by key in `get_unit()` sync; new rows 0 doors; deleted rows drop transporter |
| Bay row with no transporter entry | falls back to generic "(N)" suffix |
| Huge tonnage in header | "3600 tons" fits at FS_LARGE before BV column |
| Aft "A" arc in tic_grouper | inherits existing fighter behavior — parity, out of scope |

## Implementation order

1. `src/models/dropship.py` (new)
2. `src/parsers/blk_parser.py` + `src/parsers/name_normalizer.py`
3. `src/utils/equipment_formatter.py`
4. `src/renderer/dropship_renderer.py` (new)
5. `src/ui/forms/dropship_form.py` (new) + `src/ui/weapons_panel.py`
6. `src/ui/card_tab.py`
7. `src/ui/main_window.py` + `src/ui/unit_database_dialog.py`
8. `src/engine/batch_processor.py` + `src/engine/bv_calculator.py`
9. `src/version.py`
10. Tests → full suite → visual loop → manual verification

**Key files:** `src/models/aero.py` (model template), `src/parsers/blk_parser.py` (`_parse_aero` 452-596 template), `src/renderer/aero_renderer.py` (renderer template), `src/ui/forms/aero_form.py` (form template), `src/ui/card_tab.py`, `src/engine/bv_calculator.py`.
