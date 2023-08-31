# coding: utf-8

import sys
import os
import json
from PyQt5.QtCore import QUrl, QSize, Qt, QObject, pyqtSlot
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QSplitter, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel

from qfluentwidgets import (NavigationAvatarWidget, NavigationItemPosition, MessageBox, FluentWindow, SplashScreen,
                            TreeWidget)
from qfluentwidgets import FluentIcon as FIF
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.common.config import cfg
from app.common.icon import Icon
from app.common import resource

class jsSignal(QObject):
    # pyqtSlot，中文网络上大多称其为槽。作用是接收网页发起的信号
    @pyqtSlot(str, str, str, str)
    def setExtent(self, x1, y1, x2, y2):
        # 对接收到的内容进行处理，比如调用打印机进行打印等等。
        # 排序
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)
        if x1 > x2:
            x2, x1 = x1, x2
        if y1 < y2:
            y1, y2 = y2, y1
        print(x1, y1, x2, y2)


class MainWindow(FluentWindow):
    def __init__(self, conf):
        super().__init__()
        self.win_conf = conf.get('windows')
        self.urls = conf.get('urls')

        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


def windows():
    viewInterface = QWidget(objectName='viewInterface')

    gridLayout = QGridLayout()
    viewInterface.setLayout(gridLayout)
    # 分隔
    splitter = QSplitter(viewInterface)
    # 栅格布局
    gridLayout.setSpacing(4)
    gridLayout.setContentsMargins(2, 2, 2, 8)
    # 图层树
    tree = TreeWidget()
    tree.setIndentation(10)
    tree.setMaximumWidth(200)
    # gridLayout.addWidget(tree)

    # 浏览器
    # web = QWebEngineView()

    # 创建一个QWebChannel对象 # 增加一个通信中需要用到的频道
    channel = QWebChannel()
    printer = jsSignal()  # 通信过程中需要使用到的功能类

    # 将MapHandler对象注册到QWebChannel中，命名为"printer"
    channel.registerObject("printer", printer)
    web.page().setWebChannel(channel)  # 在浏览器中设置该频道
    # 设置网页在窗口中显示的位置和大小
    web.setGeometry(200, 200, 500, 500)
    # web.load(QUrl('https://www.baidu.com/'))
    path = "file:///map.html"
    # path = path.replace('\\', '/')
    web.load(QUrl(path))

    # 添加到布局
    splitter.addWidget(tree)
    splitter.addWidget(web)
    gridLayout.addWidget(splitter)

    # 图层树
    tree.setHeaderLabels(['图层'])
    for root_key in urls.keys():
        root = QTreeWidgetItem(tree)
        root.setText(0, root_key)
        for key in urls.get(root_key).keys():
            child = QTreeWidgetItem(root)
            # child.setCheckState(0, Qt.Unchecked)
            child.setText(0, key)
    tree.itemClicked.connect(select_layer)
    # initNavigation()

    pos = NavigationItemPosition.SCROLL
    win.addSubInterface(viewInterface, Icon.GRID, 'View', pos)
    win.show()
    # win.__init__(tiles,geojson)

    sys.exit(app.exec_())


def select_layer(item):
    map_name = item.text(0)
    if map_name in urls.keys():
        return
    ask = QMessageBox.question(
        win, '提示', '切换地图？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if ask == QMessageBox.No:
        return

    url = urls.get(item.parent().text(0)).get(map_name)
    # qwebengine.page().runJavaScript('url=\"'+url+'\";')
    web.page().runJavaScript('setUrl(\"' + url + '\");')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    conf = None
    urls = None
    win_conf = None
    with open("conf.json", 'r', encoding='UTF-8') as f:
        conf = json.load(f)
    urls = conf.get('urls')
    win_conf = conf.get('windows')
    web = QWebEngineView()
    win = MainWindow(conf)
    windows()
