import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget
from UI_mainform import Ui_mainForm
from TitleBar import *

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

    def openFile(self):
        pass
            
        
        
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = mainFrom()
    win.show()
    sys.exit(app.exec_())