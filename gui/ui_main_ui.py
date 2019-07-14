# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainApplication(object):
    def setupUi(self, MainApplication):
        MainApplication.setObjectName("MainApplication")
        MainApplication.resize(581, 420)
        self.gridLayout = QtWidgets.QGridLayout(MainApplication)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(MainApplication)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(MainApplication)
        QtCore.QMetaObject.connectSlotsByName(MainApplication)

    def retranslateUi(self, MainApplication):
        _translate = QtCore.QCoreApplication.translate
        MainApplication.setWindowTitle(_translate("MainApplication", "pyFileTools"))
        self.label.setText(_translate("MainApplication", "WIP"))


