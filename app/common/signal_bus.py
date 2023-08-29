# coding: utf-8
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class SignalBus(QObject):
    """ Signal bus """

    switchToSampleCard = pyqtSignal(str, int)
    micaEnableChanged = pyqtSignal(bool)
    supportSignal = pyqtSignal()


signalBus = SignalBus()

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
