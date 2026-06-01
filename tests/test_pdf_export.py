"""
Phase 9.6 — PDF export smoke tests.

Verifies:
  - Single-card PDF is created and non-empty
  - Multi-card PDF is created and has more bytes than a single-card PDF
  - PNG export works and produces correct file size
"""
from __future__ import annotations
import os

import pytest

MEGAMEK_DIR = os.path.join(
    os.path.dirname(__file__), "..", "reference", "megamek_files"
)


@pytest.fixture(scope="module")
def hunchback_pixmap(qapp):
    from src.models.data_store import DataStore
    from src.settings.profile import ConversionProfile
    from src.parsers.mtf_parser import parse_mtf
    from src.renderer.mech_renderer import MechCardRenderer
    from src.engine.tic_grouper import resolve_weapons, sort_weapons

    DataStore.load()
    result = parse_mtf(os.path.join(MEGAMEK_DIR, "Hunchback HBK-4G.mtf"))
    unit = result.unit
    profile = ConversionProfile.default()
    resolved = sort_weapons(resolve_weapons(unit, unit.tonnage))
    rows = [
        {
            "name":    rw.display_name, "damage": rw.damage_str,
            "heat":    rw.heat_str,     "location": rw.location,
            "rangePB": rw.range_pb,     "rangeS":  rw.range_s,
            "rangeM":  rw.range_m,      "rangeL":  rw.range_l,
            "rangeX":  rw.range_x,
        }
        for rw in resolved
    ]
    return MechCardRenderer().render(unit, profile, rows)


@pytest.fixture(scope="module")
def jenner_pixmap(qapp):
    from src.settings.profile import ConversionProfile
    from src.parsers.mtf_parser import parse_mtf
    from src.renderer.mech_renderer import MechCardRenderer
    from src.engine.tic_grouper import resolve_weapons, sort_weapons

    result = parse_mtf(os.path.join(MEGAMEK_DIR, "Jenner JR7-D.mtf"))
    unit = result.unit
    profile = ConversionProfile.default()
    resolved = sort_weapons(resolve_weapons(unit, unit.tonnage))
    rows = [
        {
            "name": rw.display_name, "damage": rw.damage_str,
            "heat": rw.heat_str,     "location": rw.location,
            "rangePB": rw.range_pb,  "rangeS": rw.range_s,
            "rangeM":  rw.range_m,   "rangeL": rw.range_l,
            "rangeX":  rw.range_x,
        }
        for rw in resolved
    ]
    return MechCardRenderer().render(unit, profile, rows)


# ── PDF export ────────────────────────────────────────────────────────────────

def test_pdf_single_card_created(qapp, hunchback_pixmap, tmp_path):
    from src.renderer.pdf_exporter import export_pdf
    out = tmp_path / "hunchback.pdf"
    export_pdf(hunchback_pixmap, str(out))
    assert out.exists(), "PDF file not created"
    assert out.stat().st_size > 10_000, "PDF suspiciously small"


def test_pdf_multi_card_larger_than_single(qapp, hunchback_pixmap, jenner_pixmap, tmp_path):
    from src.renderer.pdf_exporter import export_pdf, export_pdf_multi

    single = tmp_path / "single.pdf"
    multi  = tmp_path / "multi.pdf"

    export_pdf(hunchback_pixmap, str(single))
    export_pdf_multi([hunchback_pixmap, jenner_pixmap], str(multi))

    assert multi.stat().st_size > single.stat().st_size, \
        "Multi-card PDF should be larger than single-card PDF"


def test_pdf_vehicle_card(qapp, tmp_path):
    from src.settings.profile import ConversionProfile
    from src.parsers.blk_parser import parse_blk
    from src.renderer.vehicle_renderer import VehicleCardRenderer
    from src.renderer.pdf_exporter import export_pdf
    from src.engine.tic_grouper import resolve_weapons, sort_weapons
    from src.models.vehicle import CombatVehicle

    result = parse_blk(os.path.join(MEGAMEK_DIR, "Condor Heavy Hover Tank (Liao).blk"))
    unit = result.unit
    assert isinstance(unit, CombatVehicle)

    profile = ConversionProfile.default()
    resolved = sort_weapons(resolve_weapons(unit, unit.tonnage))
    rows = [
        {
            "name": rw.display_name, "damage": rw.damage_str,
            "heat": rw.heat_str,     "location": rw.location,
            "rangePB": rw.range_pb,  "rangeS": rw.range_s,
            "rangeM":  rw.range_m,   "rangeL": rw.range_l,
            "rangeX":  rw.range_x,
        }
        for rw in resolved
    ]
    px = VehicleCardRenderer().render(unit, profile, rows)
    out = tmp_path / "condor.pdf"
    export_pdf(px, str(out))
    assert out.exists()
    assert out.stat().st_size > 10_000


# ── PNG export ────────────────────────────────────────────────────────────────

def test_png_export_mech(qapp, hunchback_pixmap, tmp_path):
    from src.renderer.png_exporter import export_png
    out = tmp_path / "hunchback.png"
    export_png(hunchback_pixmap, str(out))
    assert out.exists()
    assert out.stat().st_size > 50_000


def test_png_export_preserves_dimensions(qapp, hunchback_pixmap, tmp_path):
    from src.renderer.png_exporter import export_png
    from PyQt6.QtGui import QPixmap

    out = tmp_path / "hunchback_dims.png"
    export_png(hunchback_pixmap, str(out))

    reloaded = QPixmap(str(out))
    assert reloaded.width() == 2100
    assert reloaded.height() == 1500
