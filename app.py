from PyQt5.QtCore import QObject, pyqtSlot, QUrl, Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QTreeWidget, QGridLayout, QAction,
                             QApplication, QSplitter, QTreeWidgetItem, QMessageBox, QAbstractItemView)
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtNetwork import QNetworkProxy

# from windows.dowmload import DownLoaderDialog
import json
import sys
import os
import io


# urls = {
#     '谷歌': {
#     '谷歌影像-84': 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s&x={x}&y={y}&z={z}',
#     '谷歌影像带标注-84': 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s,m&x={x}&y={y}&z={z}',
#     '谷歌影像-02': 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s&gl=CN&x={x}&y={y}&z={z}',
#     '谷歌影像带标注-02': 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s,m&gl=CN&x={x}&y={y}&z={z}',
#     '谷歌地图-02': 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=m&x={x}&y={y}&z={z}'
#     }
#     }

# with open("urls.json", "w", encoding='utf-8') as f:
#     # json.dump(dict_, f)  # 写为一行
#     json.dump(urls, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行


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
        win.extent = [x1, y1, x2, y2]
        print(win.extent)


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.extent = None
        self.initUi()

    def initUi(self):
        self.setWindowTitle('地图显示')
        self.resize(1000, 640)

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu("文件")
        toolMenu = menubar.addMenu("工具")

        downMenu = QAction("下载", self)
        menubar.addAction(downMenu)
        opMenu = menubar.addMenu("选项")
        # 添加一个打开动作
        openAction = QAction("打开", self)
        # 将打开动作添加到文件菜单
        fileMenu.addAction(openAction)
        # 添加一个退出动作
        exitAction = QAction("退出", self)
        # 将退出动作添加到文件菜单
        fileMenu.addAction(exitAction)
        downMenu.triggered.connect(openDownLoadForm)
        # qwebengine.show()
    # 重写关闭事件保存设置

    def closeEvent(self, event):
        path = '' if downloder.info['outPath'] is None else downloder.info['outPath']
        conf = {
            "windows": {
                "width": self.width(),
                "height": self.height(),
                "outPath": path
            },
            "urls": urls,

        }
        with open("conf.json", "w", encoding='utf-8') as f:
            # json.dump(dict_, f)  # 写为一行
            json.dump(conf, f, indent=2, sort_keys=True,
                      ensure_ascii=False)  # 写为多行
        # reply = QMessageBox.question(self, '提示',
        #             "退出?",
        #             QMessageBox.Yes | QMessageBox.No,
        #             QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     event.accept()
        #     sys.exit(0)   # 退出程序
        # else:
        #     event.ignore()


def openDownLoadForm():
    if listWidget.currentItem() is None:
        QMessageBox.warning(win, '警告', '未选择下载图层！')
        return
    if not win.extent:
        QMessageBox.warning(win, '警告', '未选择下载范围！')
        return
    if listWidget.currentItem().parent() is None:
        return
    url = urls.get(listWidget.currentItem().parent().text(0)
                   ).get(listWidget.currentItem().text(0))
    # extent = None
    downloder.url_info.setText('瓦片来源：' + listWidget.currentItem().text(0))
    downloder.extent_info.setText('下载范围：' + str(win.extent))
    downloder.info['url'] = url
    downloder.info['extent'] = win.extent
    downloder.info['outPath'] = win_conf['outPath']
    downloder.pathLine.setText(downloder.info['outPath'])
    downloder.setModal(True)
    downloder.show()



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
    qwebengine.page().runJavaScript('setUrl(\"' + url + '\");')
    #    'url=\"https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}\"'+';')


def Windows(win_conf):

    # proxy = QNetworkProxy()
    # proxy.setType=QNetworkProxy.Socks5Proxy
    # #(QNetworkProxy.Socks5Proxy)
    # proxy.setHostName("43.134.172.85")
    # proxy.setPort(3303)
    # proxy.setUser("jialianxing")
    # proxy.setPassword("jlx01154032")
    # QNetworkProxy.setApplicationProxy(proxy)
    win.resize(int(win_conf.get('width')), int(win_conf.get('height')))
    widget = QWidget()
    splitter = QSplitter(widget)
    win.setCentralWidget(widget)
    gridout = QGridLayout()
    gridout.setSpacing(4)
    gridout.setContentsMargins(2, 2, 2, 8)
    widget.setLayout(gridout)

    listWidget.setMinimumWidth(100)
    listWidget.setMaximumWidth(200)

    splitter.addWidget(listWidget)

    # 新建一个QWebEngineView()对象

    # 创建一个QWebChannel对象 # 增加一个通信中需要用到的频道
    channel = QWebChannel()
    printer = jsSignal()  # 通信过程中需要使用到的功能类

    # 将MapHandler对象注册到QWebChannel中，命名为"printer"
    channel.registerObject("printer", printer)
    qwebengine.page().setWebChannel(channel)  # 在浏览器中设置该频道
    # 设置网页在窗口中显示的位置和大小
    qwebengine.setGeometry(200, 200, widget.width(), widget.height())

    path = "file:///map.html"
    # path = path.replace('\\', '/')
    qwebengine.load(QUrl(path))
    splitter.addWidget(qwebengine)
    gridout.addWidget(splitter)
    listWidget.setHeaderLabels(['图层'])
    for root_key in urls.keys():
        root = QTreeWidgetItem(listWidget)
        root.setText(0, root_key)
        for key in urls.get(root_key).keys():
            child = QTreeWidgetItem(root)
            child.setCheckState(0, Qt.Unchecked)
            child.setText(0, key)
    # 信号
    listWidget.itemClicked.connect(select_layer)

    win.show()
    # win.__init__(tiles,geojson)

    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    # setup stylesheet
    # apply_stylesheet(app, theme='dark_amber.xml')
    # downloder = DownLoaderDialog()
    listWidget = QTreeWidget()
    # listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)#设置item可以多选
    qwebengine = QWebEngineView(win)
    conf = None
    urls = None
    win_conf = None
    # extent = None
    with open("conf.json", 'r', encoding='UTF-8') as f:
        conf = json.load(f)
    urls = conf.get('urls')
    win_conf = conf.get('windows')
    Windows(win_conf)
