import argparse
import sys
from PyQt5.QtWidgets import QApplication

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

    app = QApplication([])
    screen_resolution = app.desktop().screenGeometry()
    w, h = screen_resolution.width(), screen_resolution.height()

    wScale = w / default_res[0]
    hScale = h / default_res[1]

arg = arguments
