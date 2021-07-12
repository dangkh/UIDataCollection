import numpy as np
from createSub import createSub_Dialog
from createSampleDialog import SampleDialog
from PyQt5.QtWidgets import *
from arguments import arg
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


class createSam(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = SampleDialog()
        self.ui.setupUi()
        self.turnOnBtn = False
        self.ui.rcdBtn.hide()
        self.ui.scenarioNumber.setMaximum(arg.numPlan)
        self.ui.scenarioNumber.setMinimum(1)
        self.ui.scenarioNumber.valueChanged.connect(self.updatePlanView)
        self.updatePlanView()

    def setInfo(self, info):
        # set sample info as the info of the patient
        self.info = info
        try:
            jsonDir = info + '/info.json'
            with open(jsonDir) as json_file:
                data = json.load(json_file)
            self.ui.NameEdit.setText(data['name'])
            self.ui.AgeEdit.setValue(data['age'])
            if data['gender'] == 'M':
                self.ui.MaleEdit.setChecked(True)
            else:
                self.ui.FemaleEdit.setChecked(True)

            self.ui.NameEdit.setEnabled(False)
            self.ui.AgeEdit.setEnabled(False)
            self.ui.MaleEdit.setEnabled(False)
            self.ui.FemaleEdit.setEnabled(False)
        except Exception as e:
            print("cant find json file, subject dont have required infomation")
            print(e)

    def setRecodData(self, data):
        self.ui.RecorderEdit.setText(data['Recorder'])
        self.ui.LocateEdit.setText(data['Location'])
        self.ui.scenarioNumber.setValue(data['scenarioId'])

    def updatePlanView(self):
        text = arg.plans[self.ui.scenarioNumber.value() - 1]
        self.ui.lineEdit.setText(str(text))

    def closeEvent(self, event):
        # event.accept()
        self.ui.closeEvent(event)
        # QApplication.quit()
