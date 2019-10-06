# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Welcome_Page(object):
    def setupUi(self, Welcome_Page):
        Welcome_Page.setObjectName("Welcome_Page")
        Welcome_Page.setWindowModality(QtCore.Qt.NonModal)
        Welcome_Page.resize(340, 183)
        Welcome_Page.setMouseTracking(False)
        Welcome_Page.setAutoFillBackground(False)
        Welcome_Page.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Welcome_Page)
        self.label_2.setGeometry(QtCore.QRect(9, 66, 120, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Welcome_text = QtWidgets.QLabel(Welcome_Page)
        self.Welcome_text.setGeometry(QtCore.QRect(9, 9, 97, 16))
        self.Welcome_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_text.setObjectName("Welcome_text")
        self.Uncode_But = QtWidgets.QPushButton(Welcome_Page)
        self.Uncode_But.setGeometry(QtCore.QRect(9, 122, 75, 23))
        self.Uncode_But.setObjectName("Uncode_But")
        self.Code_But = QtWidgets.QPushButton(Welcome_Page)
        self.Code_But.setGeometry(QtCore.QRect(9, 151, 75, 23))
        self.Code_But.setObjectName("Code_But")

        self.retranslateUi(Welcome_Page)
        QtCore.QMetaObject.connectSlotsByName(Welcome_Page)

    def retranslateUi(self, Welcome_Page):
        _translate = QtCore.QCoreApplication.translate
        Welcome_Page.setWindowTitle(_translate("Welcome_Page", "Welcome to RTL code translator"))
        self.label_2.setText(_translate("Welcome_Page", "Выберете кодирование"))
        self.Welcome_text.setText(_translate("Welcome_Page", "Добро пожаловать"))
        self.Uncode_But.setText(_translate("Welcome_Page", "Разжимать"))
        self.Code_But.setText(_translate("Welcome_Page", "Сжимать"))
