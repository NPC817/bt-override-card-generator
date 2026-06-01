"""Print feature tests — no actual printing occurs.

render_cards_to_printer is exercised via QPrinter in PDF output mode,
which writes to a temp file without opening any dialog or sending to a printer.
PrintQueueDialog is instantiated (not exec'd) to verify it builds without error.
"""
from __future__ import annotations
import os

import pytest

MEGAMEK_DIR = os.path.join(
    os.path.dirname(__file__), "..", "reference", "megamek_files"
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def two_pixmaps(qapp):
    """Two rendered card pixmaps for multi-card layout tests."""
    from src.models.data_store import DataStore
    from src.settings.profile import ConversionProfile
    from src.parsers.mtf_parser import parse_mtf
    from src.renderer.mech_renderer import MechCardRenderer
    from src.engine.tic_grouper import resolve_weapons, sort_weapons

    DataStore.load()
    profile = ConversionProfile.default()
    pixmaps = []
    for fname in ("Hunchback HBK-4G.mtf", "Jenner JR7-D.mtf"):
        result = parse_mtf(os.path.join(MEGAMEK_DIR, fname))
        unit = result.unit
        resolved = sort_weapons(resolve_weapons(unit, unit.tonnage))
        rows = [
            {
                "name": rw.display_name, "damage": rw.damage_str,
                "heat": rw.heat_str,     "location": rw.location,
                "rangePB": rw.range_pb,  "rangeS": rw.range_s,
                "rangeM": rw.range_m,    "rangeL": rw.range_l,
                "rangeX": rw.range_x,
            }
            for rw in resolved
        ]
        pixmaps.append(MechCardRenderer().render(unit, profile, rows))
    return pixmaps


def _make_pdf_printer(path: str):
    """QPrinter configured to write PDF to path — no actual printer used."""
    from PyQt6.QtPrintSupport import QPrinter
    p = QPrinter(QPrinter.PrinterMode.ScreenResolution)
    p.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
    p.setOutputFileName(path)
    return p


# ── render_cards_to_printer ───────────────────────────────────────────────────

@pytest.mark.parametrize("layout_idx,n_cards", [
    (0, 1),  # Half page – 1 card
    (1, 2),  # 2 per page – Portrait
    (2, 1),  # Full page – 1 card
    (3, 3),  # 3 per page – Portrait
    (4, 4),  # 4 per page – Landscape
    (5, 6),  # 6 per page – Portrait
    (6, 8),  # 8 per page – Portrait
])
def test_render_layout_produces_pdf(qapp, two_pixmaps, tmp_path, layout_idx, n_cards):
    from src.ui.print_dialog import PRINT_LAYOUTS
    from src.renderer.pdf_exporter import render_cards_to_printer
    from PyQt6.QtGui import QPageLayout

    layout_cfg = PRINT_LAYOUTS[layout_idx]
    _, orientation, _cols, _rows, _cpp = layout_cfg

    # Repeat the two pixmaps to fill n_cards
    pixmaps = (two_pixmaps * ((n_cards // 2) + 1))[:n_cards]

    out = str(tmp_path / f"layout_{layout_idx}.pdf")
    printer = _make_pdf_printer(out)
    page_layout = printer.pageLayout()
    page_layout.setOrientation(
        QPageLayout.Orientation.Landscape if orientation == "landscape"
        else QPageLayout.Orientation.Portrait
    )
    printer.setPageLayout(page_layout)

    render_cards_to_printer(pixmaps, layout_cfg, printer)

    assert os.path.exists(out), "PDF file not created"
    assert os.path.getsize(out) > 5_000, "PDF suspiciously small"


def test_render_single_card_half_page(qapp, two_pixmaps, tmp_path):
    from src.ui.print_dialog import PRINT_LAYOUTS
    from src.renderer.pdf_exporter import render_cards_to_printer
    from PyQt6.QtGui import QPageLayout

    layout_cfg = PRINT_LAYOUTS[0]  # Half page – 1 card
    out = str(tmp_path / "half_page.pdf")
    printer = _make_pdf_printer(out)
    page_layout = printer.pageLayout()
    page_layout.setOrientation(QPageLayout.Orientation.Portrait)
    printer.setPageLayout(page_layout)

    render_cards_to_printer([two_pixmaps[0]], layout_cfg, printer)

    assert os.path.exists(out)
    assert os.path.getsize(out) > 5_000


def test_render_multi_page(qapp, two_pixmaps, tmp_path):
    """More cards than cards_per_page → multiple pages written without error."""
    from src.ui.print_dialog import PRINT_LAYOUTS
    from src.renderer.pdf_exporter import render_cards_to_printer
    from PyQt6.QtGui import QPageLayout

    layout_cfg = PRINT_LAYOUTS[1]  # 2 per page Portrait
    pixmaps = two_pixmaps * 3  # 6 cards → 3 pages
    out = str(tmp_path / "multi_page.pdf")
    printer = _make_pdf_printer(out)
    page_layout = printer.pageLayout()
    page_layout.setOrientation(QPageLayout.Orientation.Portrait)
    printer.setPageLayout(page_layout)

    render_cards_to_printer(pixmaps, layout_cfg, printer)
    assert os.path.getsize(out) > 5_000


# ── Reorder logic ─────────────────────────────────────────────────────────────

def _reorder(items: list, op: str, row: int) -> list:
    """Apply a reorder operation to a plain list (mirrors QListWidget logic)."""
    items = list(items)
    n = len(items)
    if op == "top" and row > 0:
        items.insert(0, items.pop(row))
    elif op == "up" and row > 0:
        items[row - 1], items[row] = items[row], items[row - 1]
    elif op == "down" and row < n - 1:
        items[row], items[row + 1] = items[row + 1], items[row]
    elif op == "bot" and row < n - 1:
        items.append(items.pop(row))
    return items


def test_move_top():
    assert _reorder(["A", "B", "C", "D"], "top", 2) == ["C", "A", "B", "D"]


def test_move_up():
    assert _reorder(["A", "B", "C"], "up", 2) == ["A", "C", "B"]


def test_move_down():
    assert _reorder(["A", "B", "C"], "down", 0) == ["B", "A", "C"]


def test_move_bottom():
    assert _reorder(["A", "B", "C", "D"], "bot", 1) == ["A", "C", "D", "B"]


def test_move_top_noop_at_zero():
    assert _reorder(["A", "B", "C"], "top", 0) == ["A", "B", "C"]


def test_move_bottom_noop_at_last():
    assert _reorder(["A", "B", "C"], "bot", 2) == ["A", "B", "C"]


# ── Dialog construction ───────────────────────────────────────────────────────

def test_dialog_constructs_single_item(qapp, two_pixmaps):
    from src.ui.print_dialog import PrintQueueDialog
    dlg = PrintQueueDialog([("Hunchback HBK-4G", two_pixmaps[0])])
    assert dlg._list.count() == 1
    assert dlg._list.item(0).text() == "Hunchback HBK-4G"
    # Reorder buttons disabled for single item
    assert not dlg._btn_top.isEnabled()
    assert not dlg._btn_bot.isEnabled()
    dlg.destroy()


def test_dialog_constructs_multiple_items(qapp, two_pixmaps):
    from src.ui.print_dialog import PrintQueueDialog
    items = [("Hunchback", two_pixmaps[0]), ("Jenner", two_pixmaps[1])]
    dlg = PrintQueueDialog(items)
    assert dlg._list.count() == 2
    assert dlg._combo.count() == 7  # 7 layout options
    dlg.destroy()


def test_dialog_reorder_via_buttons(qapp, two_pixmaps):
    from src.ui.print_dialog import PrintQueueDialog
    items = [("A", two_pixmaps[0]), ("B", two_pixmaps[1]), ("C", two_pixmaps[0])]
    dlg = PrintQueueDialog(items)
    dlg._list.setCurrentRow(2)
    dlg._move_top()
    assert dlg._list.item(0).text() == "C"
    assert dlg._list.item(1).text() == "A"
    dlg.destroy()
