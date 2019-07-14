from PyQt5.QtWidgets import QApplication
from gui.ui_main_ui import Ui_MainApplication

_main_widget = None
_main_app = None


def set_main_widget(widget):
    global _main_widget
    _main_widget = widget


def set_main_app(app: QApplication):
    global _main_app
    _main_app = app


def get_main_widget():
    return _main_widget


def get_main_app():
    return _main_app
