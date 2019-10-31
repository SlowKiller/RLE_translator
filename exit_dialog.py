# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExitDialog(object):
    def setupUi(self, ExitDialog):
        ExitDialog.setObjectName("ExitDialog")
        ExitDialog.setWindowModality(QtCore.Qt.NonModal)
        ExitDialog.resize(299, 242)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExitDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextLabel = QtWidgets.QLabel(ExitDialog)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TextLabel.setFont(font)
        self.TextLabel.setTextFormat(QtCore.Qt.AutoText)
        self.TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel.setWordWrap(True)
        self.TextLabel.setObjectName("TextLabel")
        self.verticalLayout.addWidget(self.TextLabel)
        self.ButLayout = QtWidgets.QHBoxLayout()
        self.ButLayout.setObjectName("ButLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ButLayout.addItem(spacerItem)
        self.NoBut = QtWidgets.QPushButton(ExitDialog)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.NoBut.setFont(font)
        self.NoBut.setObjectName("NoBut")
        self.ButLayout.addWidget(self.NoBut)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ButLayout.addItem(spacerItem1)
        self.YesBut = QtWidgets.QPushButton(ExitDialog)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.YesBut.setFont(font)
        self.YesBut.setObjectName("YesBut")
        self.ButLayout.addWidget(self.YesBut)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ButLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.ButLayout)

        self.retranslateUi(ExitDialog)
        QtCore.QMetaObject.connectSlotsByName(ExitDialog)

    def retranslateUi(self, ExitDialog):
        _translate = QtCore.QCoreApplication.translate
        ExitDialog.setWindowTitle(_translate("ExitDialog", "Выход из приложения"))
        self.TextLabel.setText(_translate("ExitDialog", "Вы точно хотите выйти из приложения?"))
        self.NoBut.setText(_translate("ExitDialog", "Нет"))
        self.YesBut.setText(_translate("ExitDialog", "Да"))
