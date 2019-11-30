import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import exit_dialog


class ExitDialog(QtWidgets.QDialog, exit_dialog.Ui_ExitDialog):
    def __init__(self, parent=None):                                    # Инициализация, наследование
        super().__init__(parent)
        self.setupUi(self)
        self.NoBut.clicked.connect(self.close_exit_dialog)
        self.YesBut.clicked.connect(self.close_all)

    def close_exit_dialog(self):
        self.close()

    def close_all(self):
        self.close()
        sys.exit()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
