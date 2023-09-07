from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog, QWidget

import os
import sys
from PyQt5 import QtCore
o_path = os.getcwd()
sys.path.append(o_path)
from app.function.func import WinFunc
from app.view.UI_title import Ui_title

class Title(QWidget, Ui_title):
    def __init__(self, parent=None):
        super(Title, self).__init__(parent)
        self.setupUi(self)
        self.win = parent
        self.label.setObjectName('imageLabel')
        self.label.setText('')
        self.label_2.setObjectName('titleLabel')
        self.closeButton.clicked.connect(self.close)
        self.initWindows()

    def initWindows(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # winFunc = WinFunc()
        self.setQss()

    def setWindowTitle(self, title):
        pass

    def close(self):
        self.close()
        # self.titleLabel.setText(title)

    def setQss(self):
        # theme = 'dark' if isDarkTheme() else 'light'
        with open('app/resource/style/title.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    # 1.鼠标点击事件
    def mousePressEvent(self, evt):
        # 获取鼠标当前的坐标
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()

        # 获取窗体当前坐标
        self.origin_x = self.x()
        self.origin_y = self.y()

    # 2.鼠标移动事件
    def mouseMoveEvent(self, evt):
        # 计算鼠标移动的x，y位移
        move_x = evt.globalX() - self.mouse_x
        move_y = evt.globalY() - self.mouse_y

        # 计算窗体更新后的坐标：更新后的坐标 = 原本的坐标 + 鼠标的位移
        dest_x = self.origin_x + move_x
        dest_y = self.origin_y + move_y

        # 移动窗体
        self.move(dest_x, dest_y)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Title()
    window.show()
    sys.exit(app.exec_())
