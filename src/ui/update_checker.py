"""Check for Updates — GitHub Releases API + auto-update installer."""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Fix SSL certificate path for PyInstaller frozen builds
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
except ImportError:
    pass

from PyQt6.QtCore import QThread, pyqtSignal, QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QHBoxLayout,
)

from src.version import __version__, __releases_api_url__, __repo_url__


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_version(tag: str) -> tuple[int, ...]:
    """Parse 'v1.2.3' or '1.2.3' into (1, 2, 3)."""
    m = re.search(r"(\d+(?:\.\d+)*)", tag)
    if not m:
        return (0,)
    return tuple(int(x) for x in m.group(1).split("."))


def _format_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} B"
    if n_bytes < 1024 * 1024:
        return f"{n_bytes / 1024:.1f} KB"
    return f"{n_bytes / (1024 * 1024):.1f} MB"


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

@dataclass
class ReleaseInfo:
    tag_name: str
    html_url: str
    body: str
    published_at: str
    zip_download_url: str = ""
    zip_size: int = 0


# ---------------------------------------------------------------------------
# Thread: GitHub API query (keeps UI responsive)
# ---------------------------------------------------------------------------

class UpdateCheckThread(QThread):
    """Query GitHub Releases API in background."""

    finished = pyqtSignal(object)  # ReleaseInfo | None
    error = pyqtSignal(str)

    def run(self) -> None:
        try:
            req = urllib.request.Request(
                __releases_api_url__,
                headers={"User-Agent": f"BTOverrideCardGenerator/{__version__}"},
                method="GET",
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            tag = data.get("tag_name", "")
            current_tuple = _parse_version(__version__)
            latest_tuple = _parse_version(tag)

            info = ReleaseInfo(
                tag_name=tag,
                html_url=data.get("html_url", ""),
                body=data.get("body", ""),
                published_at=data.get("published_at", ""),
            )

            # Find first .zip asset
            for asset in data.get("assets", []):
                name = asset.get("name", "")
                if name.endswith(".zip"):
                    info.zip_download_url = asset.get("browser_download_url", "")
                    info.zip_size = asset.get("size", 0)
                    break

            if latest_tuple > current_tuple:
                self.finished.emit(info)
            else:
                self.finished.emit(None)

        except urllib.error.URLError as e:
            self.error.emit(f"Network error: {e.reason}")
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            self.error.emit(f"Parse error: {e}")


# ---------------------------------------------------------------------------
# Dialog 1: Check result ("up to date" or "new version available")
# ---------------------------------------------------------------------------

class UpdateDialog(QDialog):
    """Modal dialog: runs the version check, then shows result."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Check for Updates")
        self.setMinimumSize(520, 420)
        self._release_info: ReleaseInfo | None = None
        self._build_ui()
        self._start_check()

    # -- UI ----------------------------------------------------------------

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)

        self._status_label = QLabel("Checking for updates…")
        self._status_label.setWordWrap(True)
        layout.addWidget(self._status_label)

        self._progress = QProgressBar()
        self._progress.setRange(0, 0)  # indeterminate
        layout.addWidget(self._progress)

        self._notes = QTextBrowser()
        self._notes.setOpenExternalLinks(True)
        self._notes.setVisible(False)
        layout.addWidget(self._notes, stretch=1)

        btn_layout = QHBoxLayout()
        self._download_btn = QPushButton("Download & Install")
        self._download_btn.setVisible(False)
        self._download_btn.clicked.connect(self._start_download)

        self._view_btn = QPushButton("View on GitHub")
        self._view_btn.setVisible(False)
        self._view_btn.clicked.connect(self._open_release_page)

        self._close_btn = QPushButton("Close")
        self._close_btn.clicked.connect(self.accept)

        btn_layout.addStretch()
        btn_layout.addWidget(self._download_btn)
        btn_layout.addWidget(self._view_btn)
        btn_layout.addWidget(self._close_btn)
        layout.addLayout(btn_layout)

    # -- Check logic -------------------------------------------------------

    def _start_check(self) -> None:
        self._thread = UpdateCheckThread()
        self._thread.finished.connect(self._on_check_finished)
        self._thread.error.connect(self._on_check_error)
        self._thread.start()

    def _on_check_finished(self, info: ReleaseInfo | None) -> None:
        self._progress.setVisible(False)

        if info is None:
            self._status_label.setText(
                f"You are running the latest version (<b>{__version__}</b>)."
            )
            return

        self._release_info = info
        self._status_label.setText(
            f"A new version is available: <b>{info.tag_name}</b> "
            f"(you have <b>{__version__}</b>)"
        )
        self._notes.setVisible(True)
        self._notes.setHtml(
            f"<h3>Release Notes</h3>"
            f"<p><b>Published:</b> {info.published_at[:10]}</p>"
            f"<hr>"
            f"{self._md_to_html(info.body)}"
        )
        self._download_btn.setVisible(True)
        self._view_btn.setVisible(True)

    def _on_check_error(self, msg: str) -> None:
        self._progress.setVisible(False)
        self._status_label.setText("Could not check for updates.")
        self._notes.setVisible(True)
        self._notes.setHtml(
            f"<p><b>Error:</b> {msg}</p>"
            f"<p>Visit the repository to check manually:</p>"
            f"<p><a href='{__repo_url__}'>{__repo_url__}</a></p>"
        )

    @staticmethod
    def _md_to_html(md: str) -> str:
        """Crude markdown → HTML for GitHub release notes."""
        # Convert `code`
        md = re.sub(r"`([^`]+)`", r"<code>\1</code>", md)
        # Convert **bold**
        md = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", md)
        # Convert *italic*
        md = re.sub(r"\*(.+?)\*", r"<i>\1</i>", md)
        # Convert ## headers
        md = re.sub(r"^## (.+)$", r"<h4>\1</h4>", md, flags=re.MULTILINE)
        # Convert # headers
        md = re.sub(r"^# (.+)$", r"<h3>\1</h3>", md, flags=re.MULTILINE)
        # Convert bullet lists
        md = re.sub(r"^- (.+)$", r"• \1<br>", md, flags=re.MULTILINE)
        # Preserve newlines as <br>
        md = md.replace("\n\n", "<br><br>")
        return md

    # -- Actions -----------------------------------------------------------

    def _start_download(self) -> None:
        if not self._release_info or not self._release_info.zip_download_url:
            QMessageBox.warning(
                self, "No Download",
                "No downloadable asset found for this release.\n"
                "Please visit the GitHub release page to download manually."
            )
            return
        self.accept()
        dlg = DownloadInstallDialog(self._release_info, self.parent())
        dlg.exec()

    def _open_release_page(self) -> None:
        if self._release_info:
            QDesktopServices.openUrl(QUrl(self._release_info.html_url))


# ---------------------------------------------------------------------------
# Dialog 2: Download + Install progress
# ---------------------------------------------------------------------------

class DownloadInstallDialog(QDialog):
    """Downloads the release zip and triggers the updater."""

    def __init__(self, info: ReleaseInfo, parent=None):
        super().__init__(parent)
        self._info = info
        self._reply: QNetworkReply | None = None
        self._file: object = None
        self._file_path = ""
        self._bytes_received = 0
        self._cancelled = False

        self.setWindowTitle("Download Update")
        self.setMinimumSize(480, 180)
        self._build_ui()
        self._start_download()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)

        self._status_label = QLabel(
            f"Downloading <b>{self._info.tag_name}</b>…"
        )
        self._status_label.setWordWrap(True)
        layout.addWidget(self._status_label)

        self._size_label = QLabel()
        layout.addWidget(self._size_label)

        self._progress_bar = QProgressBar()
        self._progress_bar.setRange(0, 100)
        layout.addWidget(self._progress_bar)

        btn_layout = QHBoxLayout()
        self._cancel_btn = QPushButton("Cancel")
        self._cancel_btn.clicked.connect(self._cancel)
        btn_layout.addStretch()
        btn_layout.addWidget(self._cancel_btn)
        layout.addLayout(btn_layout)

    # -- Download ----------------------------------------------------------

    def _start_download(self) -> None:
        url = QUrl(self._info.zip_download_url)
        req = QNetworkRequest(url)
        req.setRawHeader(
            b"User-Agent",
            f"BTOverrideCardGenerator/{__version__}".encode(),
        )

        self._manager = QNetworkAccessManager(self)
        self._reply = self._manager.get(req)
        self._reply.downloadProgress.connect(self._on_progress)
        self._reply.finished.connect(self._on_finished)
        self._reply.errorOccurred.connect(self._on_error)

        # Write to temp file as data arrives
        fd, self._file_path = tempfile.mkstemp(suffix=".zip", prefix="bt_update_")
        self._file = open(self._file_path, "wb")
        self._reply.readyRead.connect(self._on_ready_read)

    def _on_ready_read(self) -> None:
        if self._reply:
            self._file.write(self._reply.readAll().data())

    def _on_progress(self, received: int, total: int) -> None:
        self._bytes_received = received
        if total > 0:
            pct = int(received / total * 100)
            self._progress_bar.setValue(pct)
            self._size_label.setText(
                f"{_format_size(received)} / {_format_size(total)}"
            )
        else:
            self._size_label.setText(_format_size(received))

    def _on_finished(self) -> None:
        self._file.close()

        if self._cancelled:
            self._cleanup_file()
            self.accept()
            return

        self._status_label.setText("Installing update…")
        self._size_label.setText("The application will restart automatically.")
        self._progress_bar.setRange(0, 0)  # indeterminate
        self._cancel_btn.setEnabled(False)

        # Spawn updater batch script and quit
        self._launch_updater()

    def _on_error(self, error: QNetworkReply.NetworkError) -> None:
        self._file.close()
        self._cleanup_file()

        self._status_label.setText("Download failed.")
        msg = self._reply.errorString() if self._reply else "Unknown error"
        self._size_label.setText(msg)
        self._progress_bar.setVisible(False)

        retry = QMessageBox.question(
            self,
            "Download Failed",
            f"Could not download the update.\n\n{msg}\n\nTry again?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if retry == QMessageBox.StandardButton.Yes:
            self._progress_bar.setVisible(True)
            self._progress_bar.setRange(0, 100)
            self._progress_bar.setValue(0)
            self._size_label.clear()
            self._start_download()
        else:
            self.accept()

    def _cancel(self) -> None:
        self._cancelled = True
        if self._reply:
            self._reply.abort()
        self.accept()

    # -- Updater -----------------------------------------------------------

    def _launch_updater(self) -> None:
        app_dir = str(Path(sys.executable).parent)

        # Write updater .bat to temp
        fd, bat_path = tempfile.mkstemp(suffix=".bat", prefix="bt_updater_")
        os.close(fd)

        pid = os.getpid()
        bat_content = _UPDATER_BAT_TEMPLATE.format(
            pid=pid,
            zip_path=self._file_path,
            app_dir=app_dir,
        )
        with open(bat_path, "w") as f:
            f.write(bat_content)

        # Spawn detached
        os.startfile(bat_path)

        # Quit the app so files are unlocked
        QApplication.quit()

    def _cleanup_file(self) -> None:
        try:
            os.unlink(self._file_path)
        except OSError:
            pass

    def closeEvent(self, event) -> None:
        self._cancel()
        super().closeEvent(event)


# ---------------------------------------------------------------------------
# Updater batch script template
# ---------------------------------------------------------------------------

_UPDATER_BAT_TEMPLATE = r"""@echo off
setlocal enabledelayedexpansion
set PID={pid}
set ZIP={zip_path}
set APPDIR={app_dir}

echo Waiting for application to close...
REM Wait for parent process to exit (max 30s)
set COUNT=0
:wait
tasklist /FI "PID eq %PID%" 2>NUL | find "%PID%" >NUL
if errorlevel 1 goto proceed
timeout /t 1 /nobreak >NUL
set /a COUNT+=1
if %COUNT% LSS 30 goto wait

:proceed
echo Extracting update...
set TEMPDIR=%TEMP%\bt_update_%RANDOM%
mkdir "%TEMPDIR%"
powershell -Command "Expand-Archive -Path '%ZIP%' -DestinationPath '%TEMPDIR%' -Force"
if errorlevel 1 goto cleanup

echo Installing update...
REM Try folder-in-zip structure first (current builds), then legacy flat-zip
if exist "%TEMPDIR%\BT_Override_Card_Generator" (
    robocopy "%TEMPDIR%\BT_Override_Card_Generator" "%APPDIR%" /E /IS /IT /NP
) else (
    robocopy "%TEMPDIR%" "%APPDIR%" /E /IS /IT /NP
)
if errorlevel 8 goto cleanup

echo.

:cleanup
echo Cleaning up...
rmdir /S /Q "%TEMPDIR%" 2>NUL
del "%ZIP%" 2>NUL

echo Restarting application...
start "" "%APPDIR%\BTOverrideCardGenerator.exe"

REM Self-delete
(goto) 2>NUL & del "%~f0"
"""
