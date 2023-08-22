import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget
from UI_mainform import Ui_mainForm
from TitleBar import *
from TabBar import *
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGridLayout
from qt_material import apply_stylesheet
import qdarkstyle
from qdarkstyle.light.palette import LightPalette

class mainFrom(QDialog, Ui_mainForm):
    def __init__(self) -> None:
        super(mainFrom, self).__init__()
        self.setupUi(self)
        self.InitializeViews()

    def InitializeViews(self) -> None:
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(600, 500)

        self.lay = QVBoxLayout(self)
        # 标题栏
        self.titleBar = TitleBar(self)
        self.titleBar.SetTitle('MainForm')
        self.menuBar = QMenuBar(self)
        # 菜单栏
        openMenu = self.menuBar.addMenu('文件')
        openAction = QAction('打开', self)
        openAction.triggered.connect(self.openFile)
        openMenu.addAction(openAction)
        # 添加控件
        self.lay.addWidget(self.titleBar)
        self.lay.addWidget(self.menuBar)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.title_widget.setLayout(self.lay)

        # tabWidget
        # self.tabWidget.setFont(font)
        # self.tabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.tabWidget.setObjectName("tabWidget")
        # self.tabWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.tabWidget.setTabPosition(QTabWidget.West)
        # self.tabWidget.setTabShape(QTabWidget.Rounded)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = HorizontalTabBar()
        self.tabWidget.addTab(QWidget(), 'Tab11!!11')
        self.tabWidget.addTab(QWidget(), '2222222')
        layout.addWidget(self.tabWidget, 0, 0)
        self.centerWidget.setLayout(layout)

    def openFile(self):
        pass




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = mainFrom()
    # 设置窗口样式
    # win.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    # setup stylesheet
    # apply_stylesheet(app, theme='dark_teal.xml')
    win.show()
    sys.exit(app.exec_())