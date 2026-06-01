from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication


class ThemeManager:
    """Singleton theme manager. Persists dark/light preference via QSettings."""

    _theme: str = "dark"
    _initialized: bool = False

    @classmethod
    def init(cls) -> None:
        if cls._initialized:
            return
        settings = QSettings()
        cls._theme = settings.value("theme", "dark")
        cls._initialized = True

    @classmethod
    def current(cls) -> str:
        return cls._theme

    @classmethod
    def is_dark(cls) -> bool:
        return cls._theme == "dark"

    @classmethod
    def toggle(cls) -> None:
        cls._theme = "light" if cls._theme == "dark" else "dark"
        QSettings().setValue("theme", cls._theme)

    @classmethod
    def set_dark(cls, enabled: bool) -> None:
        cls._theme = "dark" if enabled else "light"
        QSettings().setValue("theme", cls._theme)

    @classmethod
    def apply(cls, app: QApplication) -> None:
        if cls._theme == "dark":
            cls._apply_dark(app)
        else:
            cls._apply_light(app)

    @classmethod
    def _apply_dark(cls, app: QApplication) -> None:
        app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(43, 43, 43))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 80, 80))
        palette.setColor(QPalette.ColorRole.Link, QColor(66, 155, 248))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(66, 133, 244))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        # Disabled colors
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(128, 128, 128))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(128, 128, 128))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(128, 128, 128))
        app.setPalette(palette)

    @classmethod
    def _apply_light(cls, app: QApplication) -> None:
        app.setStyle("Fusion")
        app.setPalette(QApplication.style().standardPalette())
