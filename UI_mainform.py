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
        mainForm.resize(1009, 675)
        mainForm.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout = QtWidgets.QGridLayout(mainForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainform = QtWidgets.QFrame(mainForm)
        self.mainform.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainform.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainform.setObjectName("mainform")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.mainform)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 530, 1009, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.minButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.minButton.setMinimumSize(QtCore.QSize(30, 30))
        self.minButton.setMaximumSize(QtCore.QSize(30, 30))
        self.minButton.setObjectName("minButton")
        self.horizontalLayout.addWidget(self.minButton)
        self.maxButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.maxButton.setMinimumSize(QtCore.QSize(30, 30))
        self.maxButton.setMaximumSize(QtCore.QSize(30, 30))
        self.maxButton.setObjectName("maxButton")
        self.horizontalLayout.addWidget(self.maxButton)
        self.closeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.gridLayout.addWidget(self.mainform, 1, 0, 1, 1)
        self.title_widget = QtWidgets.QWidget(mainForm)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 35))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.title_widget.setObjectName("title_widget")
        self.gridLayout.addWidget(self.title_widget, 0, 0, 1, 1)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Form"))
        self.title_label.setText(_translate("mainForm", "TextLabel"))
        self.minButton.setText(_translate("mainForm", "-"))
        self.maxButton.setText(_translate("mainForm", "▭"))
        self.closeButton.setText(_translate("mainForm", "×"))

