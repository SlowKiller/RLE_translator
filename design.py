# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import exit


class Ui_MainWindow(object):
    def __init__(self):
        self.window = None
        self._closable = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InText = QtWidgets.QTextEdit(self.centralwidget)
        self.InText.setObjectName("InText")
        self.verticalLayout.addWidget(self.InText)
        self.TransBut = QtWidgets.QPushButton(self.centralwidget)
        self.TransBut.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TransBut.setObjectName("TransBut")
        self.verticalLayout.addWidget(self.TransBut)
        self.OutText = QtWidgets.QTextEdit(self.centralwidget)
        self.OutText.setObjectName("OutText")
        self.verticalLayout.addWidget(self.OutText)
        self.Direction = QtWidgets.QComboBox(self.centralwidget)
        self.Direction.setObjectName("Direction")
        self.Direction.addItem("")
        self.Direction.addItem("")
        self.verticalLayout.addWidget(self.Direction)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RLE Code Translator"))
        self.TransBut.setText(_translate("MainWindow", "Translate"))
        self.Direction.setItemText(0, _translate("MainWindow", "Сжимать"))
        self.Direction.setItemText(1, _translate("MainWindow", "Разжимать"))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.window = exit.ExitDialog()
            self.window.show()

    def closeEvent(self, evnt):
        if self._closable:
            self.close()
        else:
            evnt.ignore()
            self.window = exit.ExitDialog()
            self.window.show()
