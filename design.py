# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 436)
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
        self.OutText = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutText.setObjectName("OutText")
        self.verticalLayout.addWidget(self.OutText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Serial Code Translator", "Serial Code Translator"))
        self.TransBut.setText(_translate("Serial Code Translator", "Translate"))
