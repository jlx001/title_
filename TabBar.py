from PyQt5 import QtCore, QtGui, QtWidgets


class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()
        self.setAutoFillBackground(True)
        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
            painter.restore()


class HorizontalTabBar(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)
        
        self.setStyleSheet('QTabBar::tab{\
                                        font: 75 12pt "Arial";\
                                        width:40px;\
                                        height:100;\
                                        background-color: blue;\
                                        margin-top:5px;\
                                        margin-right:1px;\
                                        margin-left:1px;\
                                        margin-bottom:0px;}\
                            QTabBar::tab:!selected {\
                                        color:red;\
                                        background-color: blue;\
                                        }\
                            QTabBar::tab:selected {\
                                        color:blue;\
                                        background-color: red;\
                                        font: bold 14px;\
                                        ;\
                            }')
