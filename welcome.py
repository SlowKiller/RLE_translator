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
        Welcome_Page.resize(340, 211)
        Welcome_Page.setMouseTracking(False)
        Welcome_Page.setAutoFillBackground(False)
        Welcome_Page.setStyleSheet("background-color: rgb(255, 255, 207);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Welcome_Page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Welcome_Layoyt = QtWidgets.QVBoxLayout()
        self.Welcome_Layoyt.setObjectName("Welcome_Layoyt")
        self.Welcome_Text = QtWidgets.QLabel(Welcome_Page)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Welcome_Text.setFont(font)
        self.Welcome_Text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Welcome_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_Text.setObjectName("Welcome_Text")
        self.Welcome_Layoyt.addWidget(self.Welcome_Text)
        self.verticalLayout_3.addLayout(self.Welcome_Layoyt)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.Choose_layout = QtWidgets.QVBoxLayout()
        self.Choose_layout.setObjectName("Choose_layout")
        self.Choose_Text = QtWidgets.QLabel(Welcome_Page)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.Choose_Text.setFont(font)
        self.Choose_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Choose_Text.setObjectName("Choose_Text")
        self.Choose_layout.addWidget(self.Choose_Text)
        self.verticalLayout_3.addLayout(self.Choose_layout)
        self.Buttons_layout = QtWidgets.QHBoxLayout()
        self.Buttons_layout.setSpacing(20)
        self.Buttons_layout.setObjectName("Buttons_layout")
        self.Code_But = QtWidgets.QPushButton(Welcome_Page)
        self.Code_But.setObjectName("Code_But")
        self.Buttons_layout.addWidget(self.Code_But)
        self.Uncode_But = QtWidgets.QPushButton(Welcome_Page)
        self.Uncode_But.setObjectName("Uncode_But")
        self.Buttons_layout.addWidget(self.Uncode_But)
        self.verticalLayout_3.addLayout(self.Buttons_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)

        self.retranslateUi(Welcome_Page)
        QtCore.QMetaObject.connectSlotsByName(Welcome_Page)

    def retranslateUi(self, Welcome_Page):
        _translate = QtCore.QCoreApplication.translate
        Welcome_Page.setWindowTitle(_translate("Welcome_Page", "Welcome to RTL code translator"))
        self.Welcome_Text.setText(_translate("Welcome_Page", "ДОБРО ПОЖАЛОВАТЬ"))
        self.Choose_Text.setText(_translate("Welcome_Page", "Выберете режим работы"))
        self.Code_But.setText(_translate("Welcome_Page", "Сжимать"))
        self.Uncode_But.setText(_translate("Welcome_Page", "Разжимать"))
