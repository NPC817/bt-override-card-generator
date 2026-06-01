"""
Phase 9.7 — Batch processor tests.

BatchProcessor is a QThread subclass; we call run() directly to avoid
needing a running Qt event loop in tests.  Output files are checked
in a temporary directory.
"""
from __future__ import annotations
import os

import pytest

MEGAMEK_DIR = os.path.join(
    os.path.dirname(__file__), "..", "reference", "megamek_files"
)

# Representative files: 2 mechs + 2 vehicles (known to parse cleanly)
MECH_FILES = [
    "Hunchback HBK-4G.mtf",
    "Jenner JR7-D.mtf",
]
VEHICLE_FILES = [
    "Condor Heavy Hover Tank (Liao).blk",
    "Hetzer Wheeled Assault Gun.blk",
]
ALL_SUPPORTED = MECH_FILES + VEHICLE_FILES


@pytest.fixture(scope="module", autouse=True)
def load_data():
    from src.models.data_store import DataStore
    from src.settings.profile_manager import ProfileManager
    DataStore.load()
    ProfileManager.load()


# ── PNG batch export ──────────────────────────────────────────────────────────

def test_batch_png_all_succeed(qapp, tmp_path):
    from src.engine.batch_processor import BatchProcessor

    files = [os.path.join(MEGAMEK_DIR, f) for f in ALL_SUPPORTED]
    worker = BatchProcessor(files, str(tmp_path), "Default", "PNG")
    worker.run()  # run synchronously (no QThread.start)

    pngs = list(tmp_path.glob("*.png"))
    assert len(pngs) == len(ALL_SUPPORTED), \
        f"Expected {len(ALL_SUPPORTED)} PNGs, got {len(pngs)}: {[p.name for p in pngs]}"
    for p in pngs:
        assert p.stat().st_size > 10_000, f"{p.name} is suspiciously small"


# ── PDF batch export ──────────────────────────────────────────────────────────

def test_batch_pdf_all_succeed(qapp, tmp_path):
    from src.engine.batch_processor import BatchProcessor

    files = [os.path.join(MEGAMEK_DIR, f) for f in ALL_SUPPORTED]
    worker = BatchProcessor(files, str(tmp_path), "Default", "PDF")
    worker.run()

    pdfs = list(tmp_path.glob("*.pdf"))
    assert len(pdfs) == len(ALL_SUPPORTED), \
        f"Expected {len(ALL_SUPPORTED)} PDFs, got {len(pdfs)}"
    for p in pdfs:
        assert p.stat().st_size > 10_000, f"{p.name} is suspiciously small"


# ── All-format batch export ───────────────────────────────────────────────────

def test_batch_all_format(qapp, tmp_path):
    from src.engine.batch_processor import BatchProcessor

    files = [os.path.join(MEGAMEK_DIR, f) for f in MECH_FILES]
    worker = BatchProcessor(files, str(tmp_path), "Default", "All")
    worker.run()

    pngs = list(tmp_path.glob("*.png"))
    pdfs = list(tmp_path.glob("*.pdf"))
    assert len(pngs) == len(MECH_FILES)
    assert len(pdfs) == len(MECH_FILES)


# ── Cancel support ────────────────────────────────────────────────────────────

def test_batch_cancel_stops_early(qapp, tmp_path):
    from src.engine.batch_processor import BatchProcessor

    # Use many files so cancelling after first actually skips something
    files = [os.path.join(MEGAMEK_DIR, f) for f in ALL_SUPPORTED * 3]
    worker = BatchProcessor(files, str(tmp_path), "Default", "PNG")

    # Cancel immediately before run starts
    worker.cancel()
    worker.run()

    # Should have produced zero files (cancelled before first iteration)
    pngs = list(tmp_path.glob("*.png"))
    assert len(pngs) == 0, "Expected no output after immediate cancel"


# ── BatchResult structure ─────────────────────────────────────────────────────

def test_batch_result_fields():
    from src.engine.batch_processor import BatchResult
    r = BatchResult(path="foo.mtf", success=True, warnings=["w1"], error="")
    assert r.path == "foo.mtf"
    assert r.success is True
    assert r.warnings == ["w1"]
    assert r.error == ""


# ── Unsupported unit type skipped gracefully ──────────────────────────────────

def test_batch_ba_renders_successfully(qapp, tmp_path):
    """Battle Armor BLK files parse and render without error."""
    from src.engine.batch_processor import BatchProcessor

    ba_files = [
        os.path.join(MEGAMEK_DIR, "Elemental BA (Headhunter) (Sqd6).blk"),
    ]
    results = []

    worker = BatchProcessor(ba_files, str(tmp_path), "Default", "PNG")
    worker.file_done.connect(lambda r: results.append(r))
    worker.run()

    assert len(results) == 1
    assert results[0].success, results[0].error
    assert results[0].error == ""


# ── Profile is applied during batch ──────────────────────────────────────────

def test_batch_uses_requested_profile(qapp, tmp_path):
    """BatchProcessor sets the active profile before rendering."""
    from src.engine.batch_processor import BatchProcessor
    from src.settings.profile_manager import ProfileManager
    from src.settings.profile import ConversionProfile

    custom = ConversionProfile(name="BatchTest", mech_armor_divisor=6.0)
    ProfileManager.save(custom)

    files = [os.path.join(MEGAMEK_DIR, "Hunchback HBK-4G.mtf")]
    worker = BatchProcessor(files, str(tmp_path), "BatchTest", "PNG")
    worker.run()

    # Clean up
    ProfileManager.delete("BatchTest")

    assert any(tmp_path.glob("*.png")), "PNG should have been created with custom profile"
