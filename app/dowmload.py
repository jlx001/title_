import sys
import typing
import io
import os
import math
import time
import numpy as np
from typing import Any
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from math import floor, pi, log, tan, atan, exp
from threading import Thread, Lock
import urllib.request as ur
import PIL.Image as pil
from .Ui_download import Ui_Dialog
# from downloader import *
from collections.abc import Callable, Iterable, Mapping
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Process, Queue, Pool, Manager

mutex = Lock()
# 下载器1


class Downloader(QThread):
    rangeChanged = pyqtSignal(str, int)
    updateProgress = pyqtSignal(int)
    processFinished = pyqtSignal(int)
    processInterrupted = pyqtSignal()

    def __init__(self, outPath, zoom, urls, datas) -> None:
        super().__init__()
        self.urls = urls
        self.datas = datas
        self.zoom = zoom
        self.path = outPath
        self.pool = None
        self.interrupted = False
        # self.index = index
        # self.queue = Queue()
        # self.count = count
        # self.update = update
        self.mutex = Lock()
        self.stopMe = 0

    def download(self, prom):  # sourcery skip: raise-specific-error
        url = prom[0]
        i = prom[1]
        # j = prom[2]
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}
        header = ur.Request(url, headers=HEADERS)
        err = 0
        while (err < 3):
            try:
                data = ur.urlopen(header).read()
            except Exception:
                err += 1
            else:
                return data, i
        raise Exception("Bad network link.")

    def run(self):
        # 进程池
        self.pool = Pool(10)
        result = [
            self.pool.apply_async(func=download, args=((url[2], i),))
            for i, url in enumerate(self.urls)
        ]
        self.pool.close()
        self.pool.join()
        for res in result:
            data, i = res.get()
            # self.datas[i] = [url[0], url[1], data]
            z_path = f'{self.path}/{str(self.zoom)}'
            if not os.path.exists(z_path):
                os.mkdir(z_path)
            x_path = f'{z_path}/{str(self.urls[i][0])}'
            if not os.path.exists(x_path):
                os.mkdir(x_path)
            y_path = f'{x_path}/{str(self.urls[i][1])}'

            picio = io.BytesIO(data)
            small_pic = pil.open(picio)
            small_pic.save(f'{y_path}.png', quality=100)
            # for i, data in enumerate(datas):
            #     x_path = z_path + '/' + str(data[0])
            #     if not os.path.exists(x_path):
            #         os.mkdir(x_path)
            #         for img in data[1]:
            #             y_path = x_path + '/' + str(img[0])
            #             picio = io.BytesIO(img[1])
            #             small_pic = pil.open(picio)
            #             small_pic.save(y_path+'.png', quality=100)

            self.mutex.acquire()
            # print(y_path)
            self.updateProgress.emit(self.zoom)
            s = self.stopMe
            # self.datas[i] = [self.urls[i][0], self.urls[i][1], data]
            self.mutex.release()
            if s == 1:
                self.interrupted = True
                break
        if not self.interrupted:
            self.processFinished.emit(self.zoom)
            #  self.pool.terminate()
            #  self.pool = None
        else:
            self.processInterrupted.emit()

    def stop(self):
        self.mutex.acquire()
        self.stopMe = 1
        self.mutex.release()
        QThread.wait(self)
# 下载器二
class Downloader2(Thread):
    # multiple threads downloader

    def __init__(self, index, count, urls, datas, update, mutex):
        # index represents the number of threads
        # count represents the total number of threads
        # urls represents the list of URLs nedd to be downloaded
        # datas represents the list of data need to be returned.
        super().__init__()
        self.urls = urls
        self.datas = datas
        self.index = index
        self.count = count
        self.update = update
        self.mutex = mutex

    def download(self, url):
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}
        header = ur.Request(url, headers=HEADERS)
        err = 0
        while (err < 3):
            try:
                data = ur.urlopen(header).read()
            except Exception:
                err += 1
            else:
                return data
        raise Exception("Bad network link.")

    def run(self):
        for i, url in enumerate(self.urls):
            if i % self.count != self.index:
                continue

            self.datas[i] = [self.urls[0], self.urls[1], self.download(url[2])]
            if self.mutex.acquire():
                self.update()
                self.mutex.release()


def download(prom):

    url = prom[0]
    i = prom[1]
    # j = prom[2]
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}
    header = ur.Request(url, headers=HEADERS)
    err = 0
    # data = None
    while (err < 3):
        try:
            data = ur.urlopen(header).read()
        except Exception:
            err += 1
        else:
            return data, i
    raise Exception("Bad network link.")


class DownLoaderDialog(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super(DownLoaderDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('瓦片下载')
        # self.urls = None
        self.url_len = {}
        self.count = {}
        self.urls_task = None
        self.titles_task = None
        self.outPath = None
        self.tasks = []
        self.info = {"url": None,
                     "extent": None,
                     "zoom": None,
                     "outPath": None}
        self.zoom = [0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # self.mapper = QSignalMapper(self)
        self.thread_pool = QThreadPool()  # 线程池对象，用于管理多个线程
        self.allButton.clicked.connect(self.selectAll)
        self.noneButton.clicked.connect(self.selectNone)
        self.startButton.clicked.connect(self.startDownTask)
        self.foldButton.clicked.connect(self.openFold)
        # self.connect(self.checkBox1, SIGNAL("stateChanged()"), self.mapper, SLOT("selectChanged()"))
        self.checkBox1.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox1))
        self.checkBox2.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox2))
        self.checkBox3.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox3))
        self.checkBox4.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox4))
        self.checkBox5.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox5))
        self.checkBox6.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox6))
        self.checkBox7.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox7))
        self.checkBox8.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox8))
        self.checkBox9.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox9))
        self.checkBox10.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox10))
        self.checkBox11.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox11))
        self.checkBox12.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox12))
        self.checkBox13.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox13))
        self.checkBox14.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox14))
        self.checkBox15.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox15))
        self.checkBox16.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox16))
        self.checkBox17.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox17))
        self.checkBox18.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox18))
        self.checkBox19.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox19))
        self.checkBox20.stateChanged.connect(
            lambda: self.selectChanged(self.checkBox20))

    def selectChanged(self, checkbox):
        # print(e)
        if not self.info['extent']:
            return
        index = int(checkbox.objectName().split('x')[1]) - 1
        self.zoom[index] = 1 if checkbox.isChecked() else 0
        self.sum = 0
        x1 = float(self.info['extent'][0])
        y1 = float(self.info['extent'][1])
        x2 = float(self.info['extent'][2])
        y2 = float(self.info['extent'][3])
        # server = self.info['url']
        # 计算瓦片数目
        # self.urls = []
        for i in range(len(self.zoom)):
            if self.zoom[i] == 1:
                pos1x, pos1y = self.wgs_to_tile(x1, y1, (i + 1))
                pos2x, pos2y = self.wgs_to_tile(x2, y2, (i + 1))
                len_x = pos2x - pos1x + 1
                len_y = pos2y - pos1y + 1
                self.sum += len_x * len_y
        # for z_urls in self.urls:
        #     for x_urls in z_urls:
        #         sum += len(x_urls[1])
        self.num_info.setText(f'瓦片数量：{str(self.sum)}')

    def startDownTask(self):
        if not self.info['extent']:
            QMessageBox.warning(self, '警告', '请选择下载范围')
            return
        if sum(self.zoom) == 0:
            QMessageBox.warning(self, '警告', '请选择下载等级')
            return
        self.info['zoom'] = self.zoom
        self.info['outPath'] = self.pathLine.text().replace('\\', '/')
        self.progressBar.setFormat('总进度: %v / %m (%p%)')
        self.progressBar.setRange(0, self.sum)
        self.progressBar.repaint()
        self.outBrowser.append('任务开始……')
        self.outBrowser.repaint()
        self.outBrowser.append('下载源：' + self.info['url'])
        self.outBrowser.repaint()
        # start = time.time()
        for i in range(len(self.zoom)):
            if self.zoom[i] == 1:
                self.outBrowser.append('获取第{0}级url……'.format(i + 1))
                self.outBrowser.repaint()
                x1 = float(self.info['extent'][0])
                y1 = float(self.info['extent'][1])
                x2 = float(self.info['extent'][2])
                y2 = float(self.info['extent'][3])
                server = self.info['url']
                urls = self.get_urls(x1, y1, x2, y2, (i + 1), server)
                self.outBrowser.append('正在下载第{0}级瓦片'.format(i + 1))
                self.outBrowser.repaint()

                # 分配内存
                # 拉直数组
                urls_task = []
                for x_urls in urls:
                    urls_task.extend([x_urls[0], y_urls[0], y_urls[1]] for y_urls in x_urls[1])
                titles = [[None, None, None]] * len(urls_task)
                url_len = len(urls_task)
                self.outBrowser.append('下载进度：0/{0}'.format(url_len))
                self.outBrowser.repaint()
                self.url_len[(i + 1)] = url_len
                self.count[(i + 1)] = 0

                self.outPath = self.info['outPath']
                task = Downloader(self.outPath, (i + 1), urls_task, titles)
                task.updateProgress.connect(self.updateProgress)
                task.processFinished.connect(self.processFinished)
                task.processInterrupted.connect(self.processInterrupted)
                task.start()
                self.tasks.append([(i + 1), task])
                # task.wait()

        # end_time = time.time()
        # print('用时 {:.2f} 秒'.format(end_time - start))
        return titles

    def openFold(self):
        path = self.info['outPath']
        if path == '':
            path = "C:/"
        directory = QFileDialog.getExistingDirectory(None, "选取文件夹", path)  # 起始路径
        self.pathLine.setText(directory)
        self.info['outPath'] = directory
        # pass

    def download_tiles(self, urls, z, mutex, multi=10):
        global COUNT  # 声明全局变量
        COUNT = 0  # 初始化为0

        def makeupdate(s, z):
            def up():
                global COUNT
                COUNT += 1
                # print("下载中...\n\r")
                print("\r当前下载级别：{2} 下载进度：{0}/{1}".format(COUNT, s, z), end='')
            return up

        url_len = len(urls)
        datas = [[None, None, None]] * url_len
        if multi < 1 or multi > 20 or not isinstance(multi, int):
            raise Exception(
                "multi of Downloader shuold be int and between 1 to 20.")
        tasks = [Downloader2(i, multi, urls, datas, makeupdate(
            url_len, z), mutex) for i in range(multi)]
        for i in tasks:
            i.start()
        for i in tasks:
            i.join()
        return datas

    def get_urls(self, x1, y1, x2, y2, z, source=''):
        pos1x, pos1y = self.wgs_to_tile(x1, y1, z)
        pos2x, pos2y = self.wgs_to_tile(x2, y2, z)
        lenx = pos2x - pos1x + 1
        leny = pos2y - pos1y + 1
        # print("瓦片数量：{x} / {y} / {z}".format(x=lenx, y=leny, z=z))
        x_urls = []
        for x in range(pos1x, pos1x + lenx):
            y_urls = [
                [y, source.format(x=x, y=y, z=z)]
                for y in range(pos1y, pos1y + leny)
            ]
            x_urls.append([x, y_urls])

        # urls = [get_url(source, i, j, z, style) for j in range(pos1y, pos1y + leny) for i in range(pos1x, pos1x + lenx)]
        return x_urls

    def selectAll(self):
        self._extracted_from_selectNone_2(True)

    def selectNone(self):
        self._extracted_from_selectNone_2(False)

    # TODO Rename this here and in `selectAll` and `selectNone`
    def _extracted_from_selectNone_2(self, arg0):
        self.checkBox1.setChecked(arg0)
        self.checkBox2.setChecked(arg0)
        self.checkBox3.setChecked(arg0)
        self.checkBox4.setChecked(arg0)
        self.checkBox5.setChecked(arg0)
        self.checkBox6.setChecked(arg0)
        self.checkBox7.setChecked(arg0)
        self.checkBox8.setChecked(arg0)
        self.checkBox9.setChecked(arg0)
        self.checkBox10.setChecked(arg0)
        self.checkBox11.setChecked(arg0)
        self.checkBox12.setChecked(arg0)
        self.checkBox13.setChecked(arg0)
        self.checkBox14.setChecked(arg0)
        self.checkBox15.setChecked(arg0)
        self.checkBox16.setChecked(arg0)
        self.checkBox17.setChecked(arg0)
        self.checkBox18.setChecked(arg0)
        self.checkBox19.setChecked(arg0)
        self.checkBox20.setChecked(arg0)

    # Get tile coordinates in Google Maps based on latitude and longitude of WGS-84

    def wgs_to_tile(self, j, w, z):
        '''
        Get google-style tile cooridinate from geographical coordinate
        j : Longittude
        w : Latitude
        z : zoom
        '''
        def isnum(x):
            return isinstance(x, (int, float))

        if not (isnum(j) and isnum(w)):
            raise TypeError("j and w must be int or float!")

        if not isinstance(z, int) or z < 0 or z > 22:
            raise TypeError("z must be int and between 0 to 22.")

        if j < 0:
            j = 180 + j
        else:
            j += 180
        j /= 360  # make j to (0,1)

        w = 85.0511287798 if w > 85.0511287798 else w
        w = -85.0511287798 if w < -85.0511287798 else w
        w = log(tan((90 + w) * pi / 360)) / (pi / 180)
        w /= 180  # make w to (-1,1)
        w = 1 - (w + 1) / 2  # make w to (0,1) and left top is 0-point

        num = 2 ** z
        x = floor(j * num)
        y = floor(w * num)
        return x, y

    # 更新进度

    def setProgressRange(self, message, value):
        if value == -1:
            self.progressBar.setFormat(message)
        else:
            self.progressBar.setFormat(message)
            self.progressBar.setRange(0, value)

    def updateProgress(self, zoom):

        self.progressBar.setValue(self.progressBar.value() + 1)
        self.count[zoom] = int(self.count[zoom]) + 1
        lastLine = self.outBrowser.textCursor()
        text = '正在下载第{0}级瓦片'.format(zoom)
        lastLine = self.outBrowser.document().find(text, lastLine)
        lastLine.movePosition(QTextCursor.Down)
        # 选中光标所在行
        lastLine.select(QTextCursor.LineUnderCursor)
        # 移除当前行内容
        lastLine.removeSelectedText()
        # 移动光标到行首
        # self.outBrowser.moveCursor(
        #     QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
        # 重新设置值

        # print("\rDownLoading...[{0}]".format(self.count), end='')
        lastLine.insertText(
            '下载进度：{0}/{1}'.format(self.count[zoom], self.url_len[zoom]))
        self.outBrowser.setTextCursor(lastLine)
        # self.outBrowser.append('下载进度：{0}/{1}'.format())
        self.outBrowser.repaint()

    def processInterrupted(self):
        self.restoreGui()

    def processFinished(self, zoom):

        # self.count[zoom] = int(self.count[zoom]) + 1
        lastLine = self.outBrowser.textCursor()
        text = '正在下载第{0}级瓦片'.format(zoom)
        lastLine = self.outBrowser.document().find(text, lastLine)
        lastLine.movePosition(QTextCursor.Down)
        # 选中光标所在行
        lastLine.select(QTextCursor.LineUnderCursor)
        # 移除当前行内容
        lastLine.removeSelectedText()
        # 移动光标到行首
        # self.outBrowser.moveCursor(
        #     QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
        # 重新设置值

        # print("\rDownLoading...[{0}]".format(self.count), end='')
        lastLine.insertText(
            '下载进度：{0}/{1}'.format(self.url_len[zoom], self.url_len[zoom]))
        self.outBrowser.setTextCursor(lastLine)
        # self.outBrowser.append('下载进度：{0}/{1}'.format())
        self.outBrowser.repaint()

        self.stopProcessing(zoom)
        # self.restoreGui()
        # self.setProgressRange(self.tr('完成！'), -1)
        # self.progressBar.setValue(1)

    def stopProcessing(self, zoom):
        for i, workThread in self.tasks:
            if i == zoom and workThread is not None:
                workThread.stop()
                workThread = None
                # self.outBrowser.append('任务终止……')

    def restoreGui(self):
        self.progressBar.setFormat('%p%')
        self.progressBar.setRange(0, 1)
        self.progressBar.setValue(0)
