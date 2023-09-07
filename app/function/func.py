import os
import sys


# 窗口功能类
class WinFunc():
    # 读取qss
    def loadQss(self, style):
        with open(style, 'r') as f:
            return f.read()
            # self.setStyleSheet(f.read())

