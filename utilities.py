import numpy as np
from createSub import createSub_Dialog
from PyQt5.QtWidgets import QMessageBox, QDialog
from arguments import arguments as arg
import json


def readFile(data_dir):
    Data = []
    f = open(data_dir, 'r')
    counter = 0
    for line in f:
        if counter > 0:
            elements = line.split(',')
            # print(elements)
            if (elements[-1] == '\n'):
                elements = elements[:-1]
            # print(elements)
            Data.append(list(map(float, elements)))
        counter += 1
    f.close()

    Data = np.array(Data)  # list can not read by index while arr can be
    Data = np.squeeze(Data)
    Data = Data.T
    print("Finished eading Data at {}  with shape:".format(str(data_dir)), Data.shape)
    return Data


def exportMatrix(matrix, dir):
    f = open(dir, "w")
    for x in range(matrix.shape[0]):
        line = ""
        frame = matrix[x]
        for i in range(len(frame) - 1):
            line += str(frame[i]) + ", "
        line += str(frame[-1])
        line += "\n"
        f.write(line)
    print(f.close())


class createSub(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = createSub_Dialog()
        self.ui.setupUi()

def showErrorPopup(error):
    msg = QMessageBox()
    msg.setText(str(error))
    msg.exec_()
