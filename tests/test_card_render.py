"""
Card rendering accuracy tests.

Tests are layered so that failures point to the specific problem:

  1. Destiny value tests — armor/structure pip counts, move, TMM, sinks for
     both reference units (Hunchback HBK-4G, Condor Hover Tank).  These values
     are read from reference/example_cards/ PNGs by inspection; if they're wrong
     the conversion formulas are broken.

  2. Weapon row tests — build_tic_rows() must produce rows with the correct
     weapon names, non-empty damage strings, and non-zero heat for the reference
     units.

  3. Pip-presence pixel tests — after rendering, the pixels at each zone's
     known first-pip coordinate (from _BIPED_PIPS / _GROUND_PIPS constants)
     must contain at least one dark pixel.  Catches renderer drawing regressions.

  4. Right-panel image comparison — the rendered right panel (pips area) is
     compared against the matching reference PNG at reduced resolution.  Catches
     major layout regressions (zones missing, wrong background, shifted pips)
     while tolerating font-rendering differences in the text labels.

Reference ground truth: reference/example_cards/
  btd_hunchback_hbk4g.png         — Hunchback HBK-4G, 50 t biped mech
  btd_condorheavyhovertank_liao.png — Condor Heavy Hover Tank (Liao), 50 t hover
"""
from __future__ import annotations
import io
import os

import pytest
from PIL import Image, ImageChops, ImageStat

MEGAMEK_DIR  = os.path.join(os.path.dirname(__file__), "..", "reference", "megamek_files")
REF_CARD_DIR = os.path.join(os.path.dirname(__file__), "..", "reference", "example_cards")

CARD_W = 2100
CARD_H = 1500

# Right-panel x-boundary (pip/zone art starts here)
RIGHT_PANEL_X = 1200

# Comparison scale for right-panel structural check: 90 × 150 px
_CMP_W = 90
_CMP_H = 150
# Per-channel mean-abs-diff tolerance.  Allows font-rendering differences between
# the JS reference renderer and Qt, while failing on major layout regressions.
_CMP_THRESHOLD = 35


# ── Helpers ───────────────────────────────────────────────────────────────────

def _pixmap_to_pil(pixmap) -> Image.Image:
    """Convert QPixmap → PIL RGB image (via in-memory PNG)."""
    from PyQt6.QtCore import QByteArray, QBuffer, QIODevice
    ba  = QByteArray()
    buf = QBuffer(ba)
    buf.open(QIODevice.OpenModeFlag.WriteOnly)
    pixmap.save(buf, "PNG")
    buf.close()
    return Image.open(io.BytesIO(bytes(ba))).convert("RGB")


def _has_dark_pixel_near(img: Image.Image, cx: int, cy: int, radius: int = 20) -> bool:
    """Return True if any pixel in a (radius×2) box around (cx,cy) is darker than 80 in all channels."""
    region = img.crop((max(0, cx - radius), max(0, cy - radius),
                       min(img.width,  cx + radius),
                       min(img.height, cy + radius)))
    for y in range(region.height):
        for x in range(region.width):
            r, g, b = region.getpixel((x, y))
            if r < 80 and g < 80 and b < 80:
                return True
    return False


def _right_panel_diff(pixmap, ref_filename: str) -> float:
    """
    Return mean abs per-channel difference between the rendered card's right
    panel and the matching reference PNG, both downsampled to (_CMP_W, _CMP_H).
    Skips if the reference file does not exist.
    """
    ref_path = os.path.join(REF_CARD_DIR, ref_filename)
    if not os.path.exists(ref_path):
        pytest.skip(f"Reference image not found: {ref_path}")

    rendered  = _pixmap_to_pil(pixmap)
    reference = Image.open(ref_path).convert("RGB")

    # Crop the right panel from both (same x-split, scaled if sizes differ)
    def _right(img: Image.Image) -> Image.Image:
        split_x = round(RIGHT_PANEL_X * img.width / CARD_W)
        return img.crop((split_x, 0, img.width, img.height))

    r_crop = _right(rendered).resize((_CMP_W, _CMP_H), Image.LANCZOS)
    e_crop = _right(reference).resize((_CMP_W, _CMP_H), Image.LANCZOS)

    diff = ImageChops.difference(r_crop, e_crop)
    stat = ImageStat.Stat(diff)
    return sum(stat.mean) / len(stat.mean)   # average across channels


def _weapon_pipeline(unit):
    """Resolve + auto-assign TICs + build rows for a unit."""
    from src.engine.tic_grouper import resolve_weapons, auto_assign_tics, build_tic_rows
    resolved = resolve_weapons(unit, getattr(unit, "tonnage", 0))
    auto_assign_tics(resolved)
    return build_tic_rows(resolved)


# ── Module-scoped fixtures ────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def profile():
    from src.settings.profile import ConversionProfile
    from src.models.data_store import DataStore
    DataStore.load()
    return ConversionProfile.default()


@pytest.fixture(scope="module")
def hunchback(profile):
    from src.parsers.mtf_parser import parse_mtf
    return parse_mtf(os.path.join(MEGAMEK_DIR, "Hunchback HBK-4G.mtf")).unit


@pytest.fixture(scope="module")
def condor(profile):
    from src.parsers.blk_parser import parse_blk
    return parse_blk(os.path.join(MEGAMEK_DIR, "Condor Heavy Hover Tank (Liao).blk")).unit


@pytest.fixture(scope="module")
def hunchback_px(qapp, hunchback, profile):
    from src.renderer.mech_renderer import MechCardRenderer
    return MechCardRenderer().render(hunchback, profile, _weapon_pipeline(hunchback))


@pytest.fixture(scope="module")
def condor_px(qapp, condor, profile):
    from src.renderer.vehicle_renderer import VehicleCardRenderer
    return VehicleCardRenderer().render(condor, profile, _weapon_pipeline(condor))


# ═══════════════════════════════════════════════════════════════════════════════
# 1. Destiny value tests — values derived from btd_hunchback_hbk4g.png
# ═══════════════════════════════════════════════════════════════════════════════

class TestHunchbackDestinyValues:
    """
    All expected values read from reference/example_cards/btd_hunchback_hbk4g.png.
    If any assertion fails the conversion formula for that value is broken.
    """

    def test_move(self, hunchback):
        assert hunchback.destiny_move == "4 / 6"

    def test_tmm(self, hunchback):
        # walk 4 → 2*4=8 → TMM 1; run 6 → 2*6=12 → TMM 2
        assert hunchback.destiny_tmm == "1 / 2"

    def test_heat_sinks(self, hunchback):
        # 13 standard → round(13/5) = 3
        assert hunchback.destiny_sinks == 3

    def test_armor_left_arm(self, hunchback):
        assert hunchback.destiny_armor("LA", 3.0) == 5    # round(16/3) = 5

    def test_armor_right_arm(self, hunchback):
        assert hunchback.destiny_armor("RA", 3.0) == 5

    def test_armor_torso(self, hunchback):
        # CT=26, LT=20, RT=20 → round(66/6) = 11
        assert hunchback.destiny_armor("T", 3.0) == 11

    def test_armor_torso_rear(self, hunchback):
        # CTR=5, LTR=4, RTR=4 (from MTF: RTC=5, RTL=4, RTR=4) → round(13/6) = 2
        assert hunchback.destiny_armor("TR", 3.0) == 2

    def test_armor_head(self, hunchback):
        # HD=9 → stepped scale: >7 → 4
        assert hunchback.destiny_armor("HD", 3.0) == 4

    def test_armor_left_leg(self, hunchback):
        # LL=20 → round(20/3) = 7
        assert hunchback.destiny_armor("LL", 3.0) == 7

    def test_armor_right_leg(self, hunchback):
        assert hunchback.destiny_armor("RL", 3.0) == 7

    def test_structure_arms(self, hunchback):
        # 50 t biped: ARM=8, round(8/3) = 3
        assert hunchback.destiny_structure("LA") == 3
        assert hunchback.destiny_structure("RA") == 3

    def test_structure_torso(self, hunchback):
        # CT=16, ST=12 → round((16 + 2*12)/7) = round(40/7) = 6
        assert hunchback.destiny_structure("T") == 6

    def test_structure_legs(self, hunchback):
        # LEG=12, round(12/3) = 4
        assert hunchback.destiny_structure("LL") == 4
        assert hunchback.destiny_structure("RL") == 4

    def test_structure_head(self, hunchback):
        # HD struct=3, round(3/3) = 1
        assert hunchback.destiny_structure("HD") == 1


# ═══════════════════════════════════════════════════════════════════════════════
# 1b. Destiny values — btd_condorheavyhovertank_liao.png
# ═══════════════════════════════════════════════════════════════════════════════

class TestCondorDestinyValues:

    def test_move(self, condor):
        assert condor.destiny_move == "8 / 12h"

    def test_tmm(self, condor):
        # cruise 8 → 2*8=16 → TMM 3; flank 12 → 2*12=24 → TMM 4
        assert condor.destiny_tmm == "3 / 4"

    def test_no_heat_sinks(self, condor):
        assert condor.destiny_sinks == 0

    def test_armor_front(self, condor):
        # FR=38, round(38/4) = round(9.5) = 10
        assert condor.destiny_armor("FR", 4.0) == 10

    def test_armor_left_side(self, condor):
        # LS=23, round(23/4) = round(5.75) = 6
        assert condor.destiny_armor("LS", 4.0) == 6

    def test_armor_right_side(self, condor):
        assert condor.destiny_armor("RS", 4.0) == 6

    def test_armor_rear(self, condor):
        # RR=22, round(22/4) = round(5.5) = 6
        assert condor.destiny_armor("RR", 4.0) == 6

    def test_structure(self, condor):
        # 50 t vehicle: round(ceil(50/10)/3) = round(5/3) = 2
        assert condor.destiny_structure() == 2


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Weapon row pipeline
# ═══════════════════════════════════════════════════════════════════════════════

class TestHunchbackWeaponRows:

    @pytest.fixture(scope="class")
    def rows(self, hunchback):
        return _weapon_pipeline(hunchback)

    def test_produces_rows(self, rows):
        assert len(rows) >= 1, "No weapon rows produced for Hunchback"

    def test_ac20_present(self, rows):
        """AC/20 must appear in at least one row name."""
        names = " ".join(r["name"].lower() for r in rows)
        assert "ac20" in names or "ac/20" in names or "autocannon" in names, \
            f"AC/20 not found in weapon rows: {[r['name'] for r in rows]}"

    def test_damage_non_empty(self, rows):
        for r in rows:
            assert r["damage"] not in ("", None), \
                f"Row {r['name']!r} has empty damage field"

    def test_heat_present(self, rows):
        """At least one row must have non-zero, non-dash heat (AC/20 + lasers generate heat)."""
        heats = [r["heat"] for r in rows]
        assert any(h not in ("—", "0", "", None) for h in heats), \
            f"No weapon has heat > 0: {heats}"

    def test_ac20_grouped_alone(self, rows):
        """AC/20 damage budget is large enough it must occupy its own TIC row."""
        ac_rows = [r for r in rows
                   if "ac20" in r["name"].lower() or "ac/20" in r["name"].lower()
                   or "autocannon" in r["name"].lower()]
        assert len(ac_rows) >= 1, "No AC/20 TIC row found"
        # AC/20 should NOT be grouped with lasers
        for r in ac_rows:
            assert "laser" not in r["name"].lower(), \
                f"AC/20 incorrectly grouped with a laser in row: {r['name']!r}"

    def test_multiple_tic_groups(self, rows):
        """Hunchback has enough weapons that they should span at least 2 TIC groups."""
        assert len(rows) >= 2, \
            f"Expected ≥2 TIC rows for Hunchback, got {len(rows)}: {[r['name'] for r in rows]}"


class TestCondorWeaponRows:

    @pytest.fixture(scope="class")
    def rows(self, condor):
        return _weapon_pipeline(condor)

    def test_produces_rows(self, rows):
        assert len(rows) >= 1, "No weapon rows produced for Condor"

    def test_medium_laser_present(self, rows):
        names = " ".join(r["name"].lower() for r in rows)
        assert "mlas" in names or "medium laser" in names, \
            f"Medium laser not in Condor weapon rows: {[r['name'] for r in rows]}"

    def test_damage_non_empty(self, rows):
        for r in rows:
            assert r["damage"] not in ("", None), \
                f"Row {r['name']!r} has empty damage field"


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Pip-presence pixel tests
#    Start coordinates taken directly from _BIPED_PIPS / _GROUND_PIPS constants.
#    The first step in every layout is {x:0, y:0}, so first pip is at start pos.
# ═══════════════════════════════════════════════════════════════════════════════

# Coordinates from mech_renderer._BIPED_PIPS[zone]["armor"]["start"]
_MECH_ARMOR_PIP_STARTS = {
    "HD":  (1610, 330),
    "LA":  (1320, 530),
    "RA":  (1900, 530),
    "T":   (1610, 540),
    "LL":  (1470, 1020),
    "RL":  (1750, 1020),
    "TR":  (1610, 1215),
}

# Coordinates from vehicle_renderer._GROUND_PIPS[zone]["armor"]["start"]
_VEHICLE_ARMOR_PIP_STARTS = {
    "FR": (1610, 530),
    "LS": (1450, 710),
    "RS": (1770, 710),
    "RR": (1610, 1295),
}


@pytest.mark.parametrize("zone,coord", list(_MECH_ARMOR_PIP_STARTS.items()))
def test_hunchback_pip_present(qapp, hunchback_px, zone, coord):
    """A dark pip must be visible at the known first-pip position for each mech zone."""
    img = _pixmap_to_pil(hunchback_px)
    cx, cy = coord
    assert _has_dark_pixel_near(img, cx, cy), (
        f"No pip found in zone {zone!r} near ({cx},{cy}) — "
        "armor pip not drawn or coordinates shifted"
    )


@pytest.mark.parametrize("zone,coord", list(_VEHICLE_ARMOR_PIP_STARTS.items()))
def test_condor_pip_present(qapp, condor_px, zone, coord):
    """A dark pip must be visible at the known first-pip position for each vehicle zone."""
    img = _pixmap_to_pil(condor_px)
    cx, cy = coord
    assert _has_dark_pixel_near(img, cx, cy), (
        f"No pip found in vehicle zone {zone!r} near ({cx},{cy}) — "
        "armor pip not drawn or coordinates shifted"
    )


def test_hunchback_heat_scale_drawn(qapp, hunchback_px):
    """Heat scale box at top (label '5', black fill) must be visible."""
    # Position from card_renderer._draw_heat_scale: first box at (707, 181)
    img = _pixmap_to_pil(hunchback_px)
    assert _has_dark_pixel_near(img, 707, 181, radius=25), \
        "Top heat scale box (black) not found — heat scale not drawn"


def test_condor_no_heat_scale(qapp, condor_px):
    """Vehicles have no heat; the heat scale box area should be light (no dark box)."""
    img = _pixmap_to_pil(condor_px)
    # Sample a slightly larger region; if no dark box exists most pixels are light
    region = img.crop((680, 155, 740, 230))
    dark_count = sum(
        1 for y in range(region.height) for x in range(region.width)
        if all(c < 80 for c in region.getpixel((x, y)))
    )
    total = region.width * region.height
    # Allow up to 5 % dark pixels (background texture) but not a solid black box
    assert dark_count / total < 0.05, \
        f"Unexpected dark pixels in heat-scale area for vehicle card ({dark_count}/{total})"


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Right-panel structural comparison against reference PNGs
# ═══════════════════════════════════════════════════════════════════════════════

def test_hunchback_right_panel_matches_reference(qapp, hunchback_px):
    """
    The pip/zone panel of the rendered Hunchback card must be visually close to
    reference/example_cards/btd_hunchback_hbk4g.png.

    Compares at 90×150 (10× downscale from 900×1500 right panel).
    Threshold={threshold}/255 per channel — tolerates font differences, fails on
    major layout regressions (wrong zone positions, missing pips, wrong colors).
    """.format(threshold=_CMP_THRESHOLD)
    diff = _right_panel_diff(hunchback_px, "btd_hunchback_hbk4g.png")
    assert diff < _CMP_THRESHOLD, (
        f"Hunchback right-panel mean diff {diff:.1f} exceeds threshold {_CMP_THRESHOLD}. "
        "Possible regression: wrong pip layout, zone positions, or background."
    )


def test_condor_right_panel_matches_reference(qapp, condor_px):
    """
    The pip/zone panel of the rendered Condor card must be visually close to
    reference/example_cards/btd_condorheavyhovertank_liao.png.
    """
    diff = _right_panel_diff(condor_px, "btd_condorheavyhovertank_liao.png")
    assert diff < _CMP_THRESHOLD, (
        f"Condor right-panel mean diff {diff:.1f} exceeds threshold {_CMP_THRESHOLD}. "
        "Possible regression: wrong pip layout, zone positions, or background."
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Canvas size — rendered cards must be exactly 2100 × 1500
# ═══════════════════════════════════════════════════════════════════════════════

def test_hunchback_canvas_size(hunchback_px):
    assert not hunchback_px.isNull()
    assert hunchback_px.width()  == CARD_W
    assert hunchback_px.height() == CARD_H


def test_condor_canvas_size(condor_px):
    assert not condor_px.isNull()
    assert condor_px.width()  == CARD_W
    assert condor_px.height() == CARD_H


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Custom profile — divisor change must produce different pip counts
# ═══════════════════════════════════════════════════════════════════════════════

def test_custom_divisor_changes_armor_pips(hunchback):
    """Changing mech_armor_divisor from 3 to 6 must halve LA pip count."""
    default_pips = hunchback.destiny_armor("LA", 3.0)  # 5
    custom_pips  = hunchback.destiny_armor("LA", 6.0)  # 3
    assert default_pips == 5
    assert custom_pips  == 3


def test_custom_profile_render_completes(qapp, hunchback, profile):
    """Custom armor divisor must not crash the renderer."""
    from src.settings.profile import ConversionProfile
    from src.renderer.mech_renderer import MechCardRenderer
    custom = ConversionProfile(name="Test", mech_armor_divisor=6.0)
    px = MechCardRenderer().render(hunchback, custom, _weapon_pipeline(hunchback))
    assert not px.isNull()


# ═══════════════════════════════════════════════════════════════════════════════
# 7. Other units — smoke tests (size + non-null) for remaining reference files
# ═══════════════════════════════════════════════════════════════════════════════

_OTHER_MECH_FILES = [
    "Jenner JR7-D.mtf",
    "Victor VTR-9A1.mtf",
    "Javelin JVN-11B.mtf",
    "Archer ARC-2R.mtf",
    "Mad Cat (Timber Wolf) A.mtf",
]

_OTHER_VEHICLE_FILES = [
    ("Demolisher Heavy Tank (Defensive).blk", "tracked"),
    ("Hetzer Wheeled Assault Gun.blk", "wheeled"),
    ("Karnov UR Transport.blk", "vtol"),
]


@pytest.mark.parametrize("filename", _OTHER_MECH_FILES)
def test_other_mech_renders(qapp, filename, profile):
    from src.parsers.mtf_parser import parse_mtf
    from src.renderer.mech_renderer import MechCardRenderer
    unit = parse_mtf(os.path.join(MEGAMEK_DIR, filename)).unit
    px = MechCardRenderer().render(unit, profile, _weapon_pipeline(unit))
    assert not px.isNull() and px.width() == CARD_W and px.height() == CARD_H


@pytest.mark.parametrize("filename,motive", _OTHER_VEHICLE_FILES)
def test_other_vehicle_renders(qapp, filename, motive, profile):
    from src.parsers.blk_parser import parse_blk
    from src.renderer.vehicle_renderer import VehicleCardRenderer
    from src.models.vehicle import CombatVehicle
    result = parse_blk(os.path.join(MEGAMEK_DIR, filename))
    if not isinstance(result.unit, CombatVehicle):
        pytest.skip(f"{filename} is not a CombatVehicle")
    px = VehicleCardRenderer().render(result.unit, profile, _weapon_pipeline(result.unit))
    assert not px.isNull() and px.width() == CARD_W and px.height() == CARD_H


# ═══════════════════════════════════════════════════════════════════════════════
# 8. PNG save regression
# ═══════════════════════════════════════════════════════════════════════════════

def test_hunchback_png_save(qapp, hunchback_px, tmp_path):
    from src.renderer.png_exporter import export_png
    out = tmp_path / "hunchback.png"
    export_png(hunchback_px, str(out))
    assert out.exists() and out.stat().st_size > 50_000


def test_condor_png_save(qapp, condor_px, tmp_path):
    from src.renderer.png_exporter import export_png
    out = tmp_path / "condor.png"
    export_png(condor_px, str(out))
    assert out.exists() and out.stat().st_size > 10_000
