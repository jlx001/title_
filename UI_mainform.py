# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\JLX\VScode\PyQt\mainform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(947, 675)
        mainForm.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout = QtWidgets.QGridLayout(mainForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.title_widget = QtWidgets.QWidget(mainForm)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.title_widget.setObjectName("title_widget")
        self.gridLayout.addWidget(self.title_widget, 0, 0, 1, 1)
        self.centerWidget = QtWidgets.QWidget(mainForm)
        font = QtGui.QFont()
        font.setBold(True)
        self.centerWidget.setFont(font)
        self.centerWidget.setObjectName("centerWidget")
        self.gridLayout.addWidget(self.centerWidget, 1, 0, 1, 1)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Form"))

