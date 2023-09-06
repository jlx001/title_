# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view\downloading.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_downloading(object):
    def setupUi(self, downloading):
        downloading.setObjectName("downloading")
        downloading.resize(678, 60)
        downloading.setMinimumSize(QtCore.QSize(0, 60))
        downloading.setMaximumSize(QtCore.QSize(16777215, 60))
        self.gridLayout = QtWidgets.QGridLayout(downloading)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(downloading)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setStyleSheet("QWidget#widget{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-color: rgb(230, 230, 230);\n"
"}\n"
"QWidget#widget:hover{\n"
"    background-color:rgb(230, 230, 230);\n"
"}\n"
"QWidget::Qlabel:hover{\n"
"    background-color:transparent;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.img_label = QtWidgets.QLabel(self.widget)
        self.img_label.setMinimumSize(QtCore.QSize(40, 40))
        self.img_label.setMaximumSize(QtCore.QSize(40, 40))
        self.img_label.setObjectName("img_label")
        self.gridLayout_6.addWidget(self.img_label, 0, 0, 2, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 5, 2, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 0, 6, 2, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_6.addWidget(self.pushButton_6, 0, 7, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setMinimumSize(QtCore.QSize(200, 0))
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 1, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setHorizontalSpacing(20)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_4.setMinimumSize(QtCore.QSize(200, 0))
        self.progressBar_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_8.addWidget(self.progressBar_4, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setMinimumSize(QtCore.QSize(0, 30))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 4, 2, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(downloading)
        QtCore.QMetaObject.connectSlotsByName(downloading)

    def retranslateUi(self, downloading):
        _translate = QtCore.QCoreApplication.translate
        downloading.setWindowTitle(_translate("downloading", "Form"))
        self.img_label.setText(_translate("downloading", "TextLabel"))
        self.pushButton_4.setText(_translate("downloading", "PushButton"))
        self.pushButton_5.setText(_translate("downloading", "PushButton"))
        self.pushButton_6.setText(_translate("downloading", "PushButton"))
        self.label_8.setText(_translate("downloading", "TextLabel"))
        self.label_9.setText(_translate("downloading", "TextLabel"))
        self.label_12.setText(_translate("downloading", "120/120"))
        self.label_13.setText(_translate("downloading", "TextLabel"))

