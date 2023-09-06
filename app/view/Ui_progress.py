# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app\view\progress.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_progressDialog(object):
    def setupUi(self, progressDialog):
        progressDialog.setObjectName("progressDialog")
        progressDialog.resize(855, 778)
        progressDialog.setStyleSheet("")
        self.gridLayout_2 = QtWidgets.QGridLayout(progressDialog)
        self.gridLayout_2.setContentsMargins(0, 0, 2, 2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(progressDialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.downloading = QtWidgets.QWidget()
        self.downloading.setObjectName("downloading")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.downloading)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.proframe = QtWidgets.QFrame(self.downloading)
        self.proframe.setMinimumSize(QtCore.QSize(0, 50))
        self.proframe.setMaximumSize(QtCore.QSize(16777215, 50))
        self.proframe.setStyleSheet("background-color: rgba(227, 230, 232, 0.775);\n"
"border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border-color: rgb(230, 230, 230);")
        self.proframe.setMidLineWidth(0)
        self.proframe.setObjectName("proframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.proframe)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.proframe)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.proframe)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.PushButton_3 = PushButton(self.proframe)
        self.PushButton_3.setMinimumSize(QtCore.QSize(80, 35))
        self.PushButton_3.setMaximumSize(QtCore.QSize(80, 35))
        self.PushButton_3.setObjectName("PushButton_3")
        self.horizontalLayout.addWidget(self.PushButton_3)
        self.PushButton_2 = PushButton(self.proframe)
        self.PushButton_2.setMinimumSize(QtCore.QSize(80, 35))
        self.PushButton_2.setMaximumSize(QtCore.QSize(80, 35))
        self.PushButton_2.setObjectName("PushButton_2")
        self.horizontalLayout.addWidget(self.PushButton_2)
        self.PushButton = PushButton(self.proframe)
        self.PushButton.setMinimumSize(QtCore.QSize(80, 35))
        self.PushButton.setMaximumSize(QtCore.QSize(80, 35))
        self.PushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PushButton.setObjectName("PushButton")
        self.horizontalLayout.addWidget(self.PushButton)
        self.gridLayout_6.addWidget(self.proframe, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.downloading)
        self.widget_2.setObjectName("widget_2")
        self.downloadLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.downloadLayout.setContentsMargins(2, 2, 2, 2)
        self.downloadLayout.setObjectName("downloadLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.downloadLayout.addItem(spacerItem)
        self.gridLayout_6.addWidget(self.widget_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.downloading)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(progressDialog)
        self.listWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)

        self.retranslateUi(progressDialog)
        QtCore.QMetaObject.connectSlotsByName(progressDialog)

    def retranslateUi(self, progressDialog):
        _translate = QtCore.QCoreApplication.translate
        progressDialog.setWindowTitle(_translate("progressDialog", "Form"))
        self.label.setText(_translate("progressDialog", "下载总进度："))
        self.progressBar.setFormat(_translate("progressDialog", "%p%"))
        self.PushButton_3.setText(_translate("progressDialog", "全部开始"))
        self.PushButton_2.setText(_translate("progressDialog", "全部暂停"))
        self.PushButton.setText(_translate("progressDialog", "全部取消"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("progressDialog", "正在下载"))
        item = self.listWidget.item(1)
        item.setText(_translate("progressDialog", "已完成"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

from qfluentwidgets import PushButton
