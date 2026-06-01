import sys
from PyQt6.QtCore import QEvent, QObject
from PyQt6.QtWidgets import QAbstractSpinBox, QApplication, QComboBox
from src.models.data_store import DataStore
from src.settings.profile_manager import ProfileManager
from src.ui.main_window import MainWindow
from src.ui.theme import ThemeManager
from src.version import __version__


class _WheelGuard(QObject):
    """Block wheel events on spinboxes and comboboxes.

    Redirects the wheel event to the parent widget so the surrounding
    scroll area scrolls instead of changing the field value.
    """

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Wheel and isinstance(
            obj, (QAbstractSpinBox, QComboBox)
        ):
            parent = obj.parent()
            if parent:
                QApplication.sendEvent(parent, event)
            return True
        return False


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("BT Override Card Generator")
    app.setOrganizationName("BT Override")
    app.setApplicationVersion(__version__)

    app.installEventFilter(_WheelGuard(app))

    DataStore.load()
    ProfileManager.load()

    ThemeManager.init()
    ThemeManager.apply(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
