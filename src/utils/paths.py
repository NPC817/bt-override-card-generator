"""Central path resolver — works both in development and PyInstaller frozen builds."""
from __future__ import annotations
import sys
from pathlib import Path


def _asset_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return Path(__file__).parent.parent.parent


def _user_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent.parent.parent


def resource_path(*parts: str) -> Path:
    """Path to a read-only bundled asset (data files, fonts, images)."""
    return _asset_root().joinpath(*parts)


def user_data_path(*parts: str) -> Path:
    """Path to a user-writable file (profiles, settings)."""
    return _user_root().joinpath(*parts)
