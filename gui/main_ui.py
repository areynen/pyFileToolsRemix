import sys

from gui import set_main_app, set_main_widget

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from gui import Ui_MainApplication


class MainUi(QMainWindow):

    def __init__(self):
        super(MainUi, self).__init__()
        self.ui = Ui_MainApplication()
        self.ui.setupUi(self)


def window():
    app = QApplication(sys.argv)

    ui = MainUi()

    set_main_app(app)
    set_main_widget(ui)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
