import argparse
from win32api import GetSystemMetrics


class arguments(argparse.Namespace):
    plans = ["nhấc chân trái", "nhấc chân phải"]
    numPlan = len(plans)
    default_res = [1920.0, 1080.0]
    w = GetSystemMetrics(0)
    h = GetSystemMetrics(1)
    wScale = w / default_res[0]
    hScale = h / default_res[1]

arg = arguments
