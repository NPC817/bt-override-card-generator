"""PDF export: embed rendered card QPixmap into a PDF via reportlab."""
from __future__ import annotations
import io

from PyQt6.QtGui import QPixmap

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import ImageReader


def export_pdf(pixmap: QPixmap, output_path: str) -> None:
    """Save a single card QPixmap to a PDF file."""
    from reportlab.pdfgen import canvas as rl_canvas

    page_w, page_h = landscape(letter)
    c = rl_canvas.Canvas(output_path, pagesize=(page_w, page_h))
    _draw_pixmap(c, pixmap, page_w, page_h)
    c.save()


def export_pdf_multi(pixmaps: list[QPixmap], output_path: str) -> None:
    """Save multiple card QPixmaps to a single multi-page PDF."""
    from reportlab.pdfgen import canvas as rl_canvas

    page_w, page_h = landscape(letter)
    c = rl_canvas.Canvas(output_path, pagesize=(page_w, page_h))
    for pixmap in pixmaps:
        _draw_pixmap(c, pixmap, page_w, page_h)
        c.showPage()
    c.save()


def _draw_pixmap(c, pixmap: QPixmap, page_w: float, page_h: float) -> None:
    reader = ImageReader(io.BytesIO(_pixmap_to_bytes(pixmap)))
    card_ratio = pixmap.width() / pixmap.height()
    page_ratio = page_w / page_h
    if card_ratio > page_ratio:
        draw_w = page_w
        draw_h = page_w / card_ratio
    else:
        draw_h = page_h
        draw_w = page_h * card_ratio
    x = (page_w - draw_w) / 2
    y = (page_h - draw_h) / 2
    c.drawImage(reader, x, y, width=draw_w, height=draw_h, preserveAspectRatio=False)


def render_cards_to_printer(
    pixmaps: list[QPixmap],
    layout_cfg: tuple,
    printer,
) -> None:
    """Paint cards onto a QPrinter device using QPainter.

    layout_cfg is a tuple from PRINT_LAYOUTS:
      (label, cols, rows, cards_per_page)
    Orientation and page layout are already set on the printer by the caller.
    Uses QRectF-based drawPixmap to avoid creating device-resolution intermediate
    pixmaps that would overflow the page at high printer DPI.
    """
    from PyQt6.QtCore import QRectF
    from PyQt6.QtGui import QPainter

    _, cols, rows, cards_per_page = layout_cfg

    painter = QPainter(printer)

    # viewport() origin is already the printable-area corner (Qt offsets for
    # margins internally), so (0,0) = top-left of drawable area — no extra
    # offset needed.  Using QRectF-based drawPixmap avoids creating an
    # intermediate pixmap at device resolution (which overflows at high DPI).
    vp = painter.viewport()
    pw = float(vp.width())
    ph = float(vp.height())
    cell_w = pw / cols
    cell_h = ph / rows

    for idx, pixmap in enumerate(pixmaps):
        if idx > 0 and idx % cards_per_page == 0:
            printer.newPage()
        pos = idx % cards_per_page
        col = pos % cols
        row = pos // cols

        src_w = float(pixmap.width())
        src_h = float(pixmap.height())
        scale = min(cell_w / src_w, cell_h / src_h)
        draw_w = src_w * scale
        draw_h = src_h * scale

        x = col * cell_w + (cell_w - draw_w) / 2
        y = row * cell_h + (cell_h - draw_h) / 2

        painter.drawPixmap(
            QRectF(x, y, draw_w, draw_h),
            pixmap,
            QRectF(0.0, 0.0, src_w, src_h),
        )

    painter.end()


def _pixmap_to_bytes(pixmap: QPixmap) -> bytes:
    """Convert QPixmap to PNG bytes."""
    from PyQt6.QtCore import QByteArray, QBuffer, QIODevice
    ba = QByteArray()
    buf = QBuffer(ba)
    buf.open(QIODevice.OpenModeFlag.WriteOnly)
    pixmap.save(buf, "PNG")
    buf.close()
    return bytes(ba)
