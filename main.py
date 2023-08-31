# coding:utf-8
import os
import sys
import json
from PyQt5.QtCore import Qt, QTranslator, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QSplitter, QMessageBox, QLabel, QLineEdit, QPushButton, QFileDialog, QInputDialog
from qfluentwidgets import FluentTranslator, TreeWidget, NavigationItemPosition

from app.common.config import cfg
from app.common.icon import Icon
from app.view.main_window import MainWindow
from app.common.signal_bus import jsSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel
from app.dowmload import DownLoaderDialog


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

    # 图层
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

    downloader = DownLoaderDialog()

    pos = NavigationItemPosition.SCROLL
    win.addSubInterface(viewInterface, Icon.GRID, '影像', pos)
    win.addSubInterface(downloader, Icon.GRID, '下載', pos)
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
    # enable dpi scale
    if cfg.get(cfg.dpiScale) == "Auto":
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    else:
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # create application
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    # internationalization
    locale = cfg.get(cfg.language).value
    translator = FluentTranslator(locale)
    galleryTranslator = QTranslator()
    galleryTranslator.load(locale, "gallery", ".", ":/gallery/i18n")

    app.installTranslator(translator)
    app.installTranslator(galleryTranslator)

    # create main window

    conf = None
    urls = None
    win_conf = None
    # extent = None
    with open("conf.json", 'r', encoding='UTF-8') as f:
        conf = json.load(f)
    urls = conf.get('urls')
    win_conf = conf.get('windows')
    web = QWebEngineView()
    win = MainWindow(conf)
    windows()

