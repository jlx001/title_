# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\JLX\VScode\title_\app\view\title.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_title(object):
    def setupUi(self, title):
        title.setObjectName("title")
        title.resize(783, 30)
        title.setMinimumSize(QtCore.QSize(0, 30))
        title.setMaximumSize(QtCore.QSize(16777215, 32))
        title.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(title)
        self.gridLayout.setContentsMargins(8, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(title)
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setStyleSheet("image: url(:/title_/icon/icon.svg);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(title)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(321, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.closeButton = QtWidgets.QPushButton(title)
        self.closeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.closeButton.setStyleSheet("")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 1, 1, 1)
        self.maxButton = QtWidgets.QPushButton(title)
        self.maxButton.setMinimumSize(QtCore.QSize(30, 30))
        self.maxButton.setMaximumSize(QtCore.QSize(30, 30))
        self.maxButton.setStyleSheet("")
        self.maxButton.setText("")
        self.maxButton.setObjectName("maxButton")
        self.gridLayout_2.addWidget(self.maxButton, 0, 2, 1, 1)
        self.minButton = QtWidgets.QPushButton(title)
        self.minButton.setMinimumSize(QtCore.QSize(30, 30))
        self.minButton.setMaximumSize(QtCore.QSize(30, 30))
        self.minButton.setStyleSheet("")
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.gridLayout_2.addWidget(self.minButton, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 4, 1, 1)

        self.retranslateUi(title)
        QtCore.QMetaObject.connectSlotsByName(title)

    def retranslateUi(self, title):
        _translate = QtCore.QCoreApplication.translate
        title.setWindowTitle(_translate("title", "Form"))
        self.label.setText(_translate("title", "TextLabel"))
        self.label_2.setText(_translate("title", "title"))

from ..resource import resource_rc
