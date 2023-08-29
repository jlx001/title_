# coding:utf-8
import os
import sys
import json
from PyQt5.QtCore import Qt, QTranslator, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

from app.common.config import cfg
from app.view.main_window import MainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

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

<<<<<<< HEAD
w.show()
=======
conf = None
urls = None
win_conf = None
#extent = None
with open("conf.json", 'r', encoding='UTF-8') as f:
    conf = json.load(f)
urls = conf.get('urls')
win_conf = conf.get('windows')
win = MainWindow(conf)

win.show()

>>>>>>> e28805dd45e3581caa8f0ebf4df7b92aefb225ff
app.exec_()
