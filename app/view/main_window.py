# coding: utf-8
import sys
from PyQt5.QtCore import QUrl, QSize, Qt
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QSplitter
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

from qfluentwidgets import (NavigationAvatarWidget, NavigationItemPosition, MessageBox, FluentWindow, SplashScreen,
                            TreeWidget)
from qfluentwidgets import FluentIcon as FIF

from .gallery_interface import GalleryInterface
from .home_interface import HomeInterface
from .basic_input_interface import BasicInputInterface
from .date_time_interface import DateTimeInterface
from .dialog_interface import DialogInterface
from .layout_interface import LayoutInterface
from .icon_interface import IconInterface
from .material_interface import MaterialInterface
from .menu_interface import MenuInterface
from .navigation_view_interface import NavigationViewInterface
from .scroll_interface import ScrollInterface
from .status_info_interface import StatusInfoInterface
from .setting_interface import SettingInterface
from .text_interface import TextInterface
from .view_interface import ViewInterface
from ..common.config import SUPPORT_URL, cfg
from ..common.icon import Icon
from ..common.signal_bus import signalBus
from ..common.translator import Translator
from ..common import resource


class MainWindow(FluentWindow):
    def __init__(self, conf):
        super().__init__()
        self.win_conf = conf.get('windows')
        self.urls = conf.get('urls')

        self.initWindow()

        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.iconInterface = IconInterface(self)
        self.basicInputInterface = BasicInputInterface(self)
        self.dateTimeInterface = DateTimeInterface(self)
        self.dialogInterface = DialogInterface(self)
        self.layoutInterface = LayoutInterface(self)
        self.menuInterface = MenuInterface(self)
        self.materialInterface = MaterialInterface(self)
        self.navigationViewInterface = NavigationViewInterface(self)
        self.scrollInterface = ScrollInterface(self)
        self.statusInfoInterface = StatusInfoInterface(self)
        self.settingInterface = SettingInterface(self)
        self.textInterface = TextInterface(self)
        # self.viewInterface = ViewInterface(self)
        self.viewInterface = QWidget(self, objectName='viewInterface')
        gridLayout = QGridLayout()
        self.viewInterface.setLayout(gridLayout)
        # 分隔
        splitter = QSplitter(self.viewInterface)
        # 栅格布局
        gridLayout.setSpacing(4)
        gridLayout.setContentsMargins(2, 2, 2, 8)
        # 图层树
        self.tree = TreeWidget(self)
        self.tree.setIndentation(10)

        self.tree.setMaximumWidth(200)
        # gridLayout.addWidget(self.tree)
        # 浏览器
        web = QWebEngineView(objectName='webView')

        # web.load(QUrl('https://www.baidu.com/'))
        path = "file:///map.html"
        # path = path.replace('\\', '/')
        web.load(QUrl(path))

        # 添加到布局
        splitter.addWidget(self.tree)
        splitter.addWidget(web)
        gridLayout.addWidget(splitter)

        # 图层

        self.tree.setHeaderLabels(['图层'])
        for root_key in self.urls.keys():
            root = QTreeWidgetItem(self.tree)
            root.setText(0, root_key)
            for key in self.urls.get(root_key).keys():
                child = QTreeWidgetItem(root)
                # child.setCheckState(0, Qt.Unchecked)
                child.setText(0, key)

        # item1 = QTreeWidgetItem([self.tr('JoJo 1 - Phantom Blood')])
        # item1.addChildren([
        #     QTreeWidgetItem([self.tr('Jonathan Joestar')]),
        #     QTreeWidgetItem([self.tr('Dio Brando')]),
        #     QTreeWidgetItem([self.tr('Will A. Zeppeli')]),
        # ])
        # self.tree.addTopLevelItem(item1)

        # item2 = QTreeWidgetItem([self.tr('JoJo 3 - Stardust Crusaders')])
        # item21 = QTreeWidgetItem([self.tr('Jotaro Kujo')])
        # item21.addChildren([
        #     QTreeWidgetItem(['空条承太郎']),
        #     QTreeWidgetItem(['空条蕉太狼']),
        #     QTreeWidgetItem(['阿强']),
        #     QTreeWidgetItem(['卖鱼强']),
        #     QTreeWidgetItem(['那个无敌的男人']),
        # ])
        # item2.addChild(item21)
        # self.tree.addTopLevelItem(item2)
        # self.tree.expandAll()
        # self.tree.setHeaderHidden(True)

        # create sub interface
        self.connectSignalToSlot()

        # add items to navigation interface
        self.initNavigation()
        self.splashScreen.finish()

    def connectSignalToSlot(self):
        signalBus.micaEnableChanged.connect(self.setMicaEffectEnabled)
        signalBus.switchToSampleCard.connect(self.switchToSample)
        signalBus.supportSignal.connect(self.onSupport)

    def initNavigation(self):
        # add navigation items
        t = Translator()
        # self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('Home'))
        # self.addSubInterface(self.iconInterface, Icon.EMOJI_TAB_SYMBOLS, t.icons)
        # self.navigationInterface.addSeparator()

        pos = NavigationItemPosition.SCROLL
        self.addSubInterface(self.viewInterface, Icon.GRID, t.view, pos)
        self.addSubInterface(self.basicInputInterface,
                             FIF.CHECKBOX, t.basicInput, pos)
        self.addSubInterface(self.dateTimeInterface,
                             FIF.DATE_TIME, t.dateTime, pos)
        self.addSubInterface(self.dialogInterface, FIF.MESSAGE, t.dialogs, pos)
        self.addSubInterface(self.layoutInterface, FIF.LAYOUT, t.layout, pos)
        self.addSubInterface(self.materialInterface,
                             FIF.PALETTE, t.material, pos)
        self.addSubInterface(self.menuInterface, Icon.MENU, t.menus, pos)
        self.addSubInterface(self.navigationViewInterface,
                             FIF.MENU, t.navigation, pos)
        self.addSubInterface(self.scrollInterface, FIF.SCROLL, t.scroll, pos)
        self.addSubInterface(self.statusInfoInterface,
                             FIF.CHAT, t.statusInfo, pos)
        self.addSubInterface(self.textInterface, Icon.TEXT, t.text, pos)

        # add custom widget to bottom
        # self.navigationInterface.addWidget(routeKey='avatar',
        #                                    widget=NavigationAvatarWidget('zhiyiYo', ':/gallery/images/shoko.png'),
        #                                    onClick=self.onSupport,
        #                                    position=NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingInterface, FIF.SETTING, self.tr(
            'Settings'), NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(int(self.win_conf.get('width')),
                    int(self.win_conf.get('height')))
        self.setMinimumWidth(760)
        self.setWindowIcon(QIcon(':/gallery/images/logo.png'))
        self.setWindowTitle('PyQt')

        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def onSupport(self):
        w = MessageBox(
            '支持作者🥰', '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀', self)
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')
        if w.exec():
            QDesktopServices.openUrl(QUrl(SUPPORT_URL))

    def switchToSample(self, routeKey, index):
        """ switch to sample """
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == routeKey:
                self.stackedWidget.setCurrentWidget(w, False)
                w.scrollToCard(index)
