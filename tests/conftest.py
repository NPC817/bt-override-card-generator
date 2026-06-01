"""Shared pytest fixtures — includes a QApplication for GUI/renderer tests."""
import os
import pytest

# Force offscreen rendering before any PyQt6 import
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")


@pytest.fixture(scope="session")
def qapp():
    """Session-scoped QApplication (offscreen)."""
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication([])
    yield app
