import argparse
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class arguments(argparse.Namespace):
    plans = ["Nâng tay trái",
             "Nâng tay phải",
             "Nâng chân trái",
             "Nâng chân phải",
             "Há miệng",
             "Gật đầu",
             "Lắc đầu",
             "tôi muốn uống nước",
             "tôi muốn vệ sinh"]
    numPlan = len(plans)

    default_res = [1920.0, 1080.0]
    # desktop = QApplication.desktop()
    # screenRect = desktop.screenGeometry()
    # h = screenRect.height()
    # w = screenRect.width()
    # print('W-H', w, h)

    # if sys.platform == "darwin":
    #     from AppKit import NSScreen
    #     w = NSScreen.mainScreen().frame().size.width
    #     h = NSScreen.mainScreen().frame().size.height
    # else:
    #     from win32api import GetSystemMetrics
    #     w = GetSystemMetrics(0)
    #     h = GetSystemMetrics(1)

    w = 1368.0
    h = 768.0

    wScale = w / default_res[0]
    hScale = h / default_res[1]


arg = arguments
