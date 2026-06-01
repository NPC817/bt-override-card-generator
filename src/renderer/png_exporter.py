"""PNG export: save QPixmap to a PNG file."""
from __future__ import annotations
from PyQt6.QtGui import QPixmap


def export_png(pixmap: QPixmap, output_path: str) -> None:
    """Save a card QPixmap as a PNG file."""
    if not pixmap.save(output_path, "PNG"):
        raise IOError(f"Failed to save PNG to {output_path}")
