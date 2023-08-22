import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TitleBar(QWidget):
    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.win = parent
        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setFixedHeight(35)
        self.InitializeViews()

    def InitializeViews(self):
        self.iconLabel = QLabel(self)
        self.titleLabel = QLabel(self)

        self.minButton = QPushButton(self)
        self.restoreButton = QPushButton(self)
        self.closeButton = QPushButton(self)

        self.minButton.setFixedSize(25, 25)
        self.restoreButton.setFixedSize(25, 25)
        self.closeButton.setFixedSize(25, 25)

        self.iconLabel.setFixedSize(25, 25)
        self.titleLabel.setFixedHeight(25)

        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # self.minButton.setIcon(QIcon(TITLE_MIN_ICON))
        # self.restoreButton.setIcon(QIcon(TITLE_RESTORE_ICON))
        # self.closeButton.setIcon(QIcon(TITLE_CLS_ICON))

        self.minButton.clicked.connect(self.ShowMininizedWindow)
        self.restoreButton.clicked.connect(self.ShowRestoreWindow)
        self.closeButton.clicked.connect(self.CloseWindow)

        self.lay = QHBoxLayout(self)
        self.setLayout(self.lay)

        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)

        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

    def ShowMininizedWindow(self):
        self.win.showMinimized()

    def ShowMaximizedWindow(self):
        self.win.showMaximized()

    def ShowRestoreWindow(self):
        if self.win.isMaximized():
            self.win.showNormal()
        else:
            self.win.showMaximized()

    def CloseWindow(self):
        self.win.close()

    def SetTitle(self, str):
        self.titleLabel.setText(str)

    def SetIcon(self, pix):
        # self.iconLabel.setPixmap(pix.scaled(self.iconLabel.size() - QSize(TITLE_ICON_MAG, TITLE_ICON_MAG)))
        pass

    def mouseDoubleClickEvent(self, event):
        self.ShowRestoreWindow()
        return QWidget().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPos()
        return QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.isPressed:
            if self.win.isMaximized:
                self.win.showNormal()

            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.win.move(self.win.pos() + movePos)

        return QWidget().mouseMoveEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TitleBar(None)
    win.show()
    sys.exit(app.exec_())
    pass
