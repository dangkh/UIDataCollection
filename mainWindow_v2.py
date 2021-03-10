# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
from createSub import createSub_Dialog
import json

from createSampleDialog import SampleDialog
from ReceiveAndPlot import *
from multi import *
import csv

from detailSamDialog import *
import requests

import subprocess
import pyedflib as pyedf
from arguments import arg
import time as osTimer

from utilsUI.subject_folder import SubjectFolder
from utilsUI.sample_file import SampleFile


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        uic.loadUi('UiFiles/mainWindowRcd.ui', self)
        self.listSub = []
        self.listSam = []

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(int(1500 * arg.wScale), int(850 * arg.hScale))
        self.patientsGridLayout = self.findChild(QtWidgets.QGridLayout, 'patientsGridLayout')
        self.createEvent()

    def createEvent(self):
        self.numItem = 16
        self.currentSub = ""
        self.currentPage = 0
        self.currentSamPage = 0
        self.storeDir = "./DataVIN/"
        self.record_save = True
        self.counter = 0
        self.percent = 0
        self.newSam.hide()
        self.prevSub.hide()
        self.prevSam.hide()
        self.nextSam.hide()
        self.nextSub.hide()

        self.updateSub()

        self.updateSam(listDir=-1)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)
        widget = QtWidgets.QWidget()
        widget.setLayout(self.horizontalLayout)
        self.setCentralWidget(widget)
        self.newSam.clicked.connect(self.newSample)
        self.newSub.clicked.connect(self.newSubject)
        self.prevSub.clicked.connect(self.prevSubAction)
        self.nextSub.clicked.connect(self.nextSubAction)
        self.prevSam.clicked.connect(self.prevSamAction)
        self.nextSam.clicked.connect(self.nextSamAction)

        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(self.closeEvent)
        self.actionOpenFile.setShortcut("Ctrl+O")
        self.actionOpenFile.setStatusTip('Open file browser')
        self.actionOpenFile.triggered.connect(self.openFilePath)

    def updateSub(self, listDir=[], page=0):
        for sub in self.listSub:
            sub.remove()

        self.listSub = []
        self.listDirSub = readStorageData(self.storeDir)
        self.numPage = len(self.listDirSub) // self.numItem
        if len(self.listDirSub) % self.numItem == 0:
            self.numPage -= 1
        if len(self.listDirSub) > self.numItem:
            self.prevSub.show()
            self.nextSub.show()
        self.currentPage = page
        if self.currentPage > 0:
            self.prevSub.setText('Previous')
        else:
            self.prevSub.hide()

        if self.currentPage < self.numPage:
            self.nextSub.setText('Next')
        else:
            self.nextSub.hide()

        if page == -1:
            self.currentPage = self.numPage

        counter = 0
        showDir = self.listDirSub[self.currentPage * self.numItem:self.currentPage * self.numItem + self.numItem]

        for x in range(4):
            for y in range(4):
                if counter < len(showDir):
                    self.listSub.append(SubjectFolder(showDir[counter], True))
                else:
                    self.listSub.append(SubjectFolder('', False))
                self.patientsGridLayout.addWidget(self.listSub[-1].subjectWidget, x, y)
                counter += 1

        for x in self.listSub:
            x.button.clicked.connect(self.updateSamVisual(x))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "HMIlab"))
        self.label.setText(_translate("MainWindow", "Danh sách người bệnh"))
        self.prevSub.setText(_translate("MainWindow", "Previous"))
        self.nextSub.setText(_translate("MainWindow", "Next"))
        self.newSub.setText(_translate("MainWindow", "New Patient"))
        self.label_2.setText(_translate("MainWindow", "Danh sách bản ghi"))
        self.prevSam.setText(_translate("MainWindow", "Previous"))
        self.nextSam.setText(_translate("MainWindow", "Next"))
        self.newSam.setText(_translate("MainWindow", "New Record"))
        self.menuFile.setTitle(_translate("MainWindow", " File"))
        self.menuAbout.setTitle(_translate("MainWindow", " About"))
        self.actionOpenFile.setText(_translate("MainWindow", " OpenFile"))
        self.actionQuit.setText(_translate("MainWindow", " Quit"))

    def newSubject(self):
        self.createSubdialog = createSub(self)
        self.createSubdialog.ui.saveBtn.clicked.connect(self.createNewSub)
        self.createSubdialog.ui.exec_()

    def createNewSub(self):
        name = self.createSubdialog.ui.NameEdit.text()
        age = self.createSubdialog.ui.AgeEdit.value()
        genderG = self.createSubdialog.ui.FemaleEdit.isChecked()
        genderM = self.createSubdialog.ui.MaleEdit.isChecked()
        userID = self.createSubdialog.ui.lineEdit.text()
        missingValue = False
        if name == '' or userID == '':
            missingValue = True
        elif not genderG and not genderM:
            missingValue = True
        elif age == 0:
            missingValue = True

        if not missingValue:
            gender = "M"
            if genderG:
                gender = "Fm"
            recordID = userID
            js = {
                'id': recordID,
                'name': name,
                'age': age,
                'gender': gender,
            }
            newlink = self.storeDir + str(recordID)
            os.mkdir(newlink)
            fileName = newlink + '/' + 'info.json'
            with open(fileName, 'w') as outfile:
                json.dump(js, outfile)
            self.createSubdialog.ui.close()
            self.updateSub(page=-1)
        else:
            self.showErrorPopup("Please complete fully the form")

    def newSample(self):
        self.createSamdialog = createSam(self)
        self.createSamdialog.setInfo(self.currentSub)
        self.createSamdialog.ui.fetchInfoBtn.clicked.connect(lambda: self.updateInfoSample(reuse=True))
        self.createSamdialog.ui.resetBtn.clicked.connect(self.updateInfoSample)
        self.createSamdialog.ui.rcdBtn.clicked.connect(self.record_saveData)
        self.createSamdialog.ui.turnOnOffBtn.clicked.connect(self.samForceQuit)
        self.startEvent = False

        self.signalTimer = QtCore.QTimer()
        self.signalTimer.setInterval(500)
        self.signalTimer.timeout.connect(self.changeSignal)
        self.signalTimer.start()

        self.percentTimer = QtCore.QTimer()
        self.percentTimer.setInterval(1000)
        self.percentTimer.timeout.connect(self.changePercent)
        self.percentTimer.start()

        self.EEGPlot = EEGReceive_Plot("new")
        self.createSamdialog.ui.widEEG.addWidget(self.EEGPlot.pw)

        self.ETPlot = ETReceive("new")

        self.update_timer = QtCore.QTimer()
        self.update_timer.setInterval(60)
        self.update_timer.timeout.connect(self.EEGPlot.scroll)
        self.update_timer.start()

        # create a timer that will pull and add new data occasionally
        self.pull_timer = QtCore.QTimer()
        self.pull_timer.setInterval(500)
        self.pull_timer.timeout.connect(self.EEGPlot.update)
        self.pull_timer.start()
        # get ET

        self.ETtimer = QtCore.QTimer()
        self.ETtimer.setInterval(0)
        self.ETtimer.timeout.connect(self.ET_update)
        self.ETtimer.start()

        self.CAMth = VideoRecorder()
        self.CAMth.setLabelImage([self.createSamdialog.ui.CAM1])
        self.CAMth.beginRecord()

        self.currentEvent = None
        self.listEventBtn = [self.createSamdialog.ui.ThinkButton, self.createSamdialog.ui.ThinkActButton,
                             self.createSamdialog.ui.TypeButton, self.createSamdialog.ui.RestButton]
        for btn in self.listEventBtn:
            btn.clicked.connect(self.changeEventVisual(btn))
            btn.hide()

        self.createSamdialog.ui.exec_()

    def updateSam(self, listDir=0, page=0):
        nameSubject = str(self.currentSub).split("/")[-1]

        lastDir = self.currentSub + '/info.json'
        try:
            with open(lastDir) as json_file:
                data = json.load(json_file)
            nameSubject = nameSubject + " (" + data["name"] + ")"
        except Exception as e:
            pass

        # remove old sample widgets
        for sample in self.listSam:
            sample.remove()

        self.label_2.setText("Danh sách bản ghi: " + nameSubject)
        if listDir == -1:
            self.listDirSam = []
        else:
            self.listDirSam = readStorageData(self.currentSub + '/')
        self.currentSamPage = page
        self.numSamPage = len(self.listDirSam) // self.numItem
        counter = 0

        if len(self.listDirSam) % self.numItem == 0:
            self.numSamPage -= 1
        if len(self.listDirSam) > self.numItem:
            self.prevSam.show()
            self.nextSam.show()
        else:
            self.prevSam.hide()
            self.nextSam.hide()
        self.currentSamPage = page
        if page == -1:
            self.currentSamPage = self.numSamPage
        showDirSam = self.listDirSam[
            self.currentSamPage * self.numItem:self.currentSamPage * self.numItem + self.numItem]
        # print(showDirSam)
        self.listSam = []
        for x in range(4):
            for y in range(4):
                if counter < len(showDirSam):
                    self.listSam.append(SampleFile(showDirSam[counter], True))
                else:
                    self.listSam.append(SampleFile('', False))
                self.gridLayout_sample.addWidget(self.listSam[-1].sampleWidget, x, y)
                counter += 1

        for sampleFile in self.listSam:
            sampleFile.button.clicked.connect(self.visualSamdetail(sampleFile))

    def updateSamVisual(self, sub: SubjectFolder):
        def wrap():
            link = sub.dir
            self.currentSub = link
            if os.path.isdir(link):
                onlydir = [link + "/" + d for d in os.listdir(link) if os.path.isdir(link + "/" + d)]
            else:
                print("Error in link Sub")
            onlydir.sort(key=os.path.getctime)
            self.updateSam()
            self.newSam.show()
        return wrap

    def chooseViewSam(self, error, link):
        buttonReply = QMessageBox.question(self, 'Visual Sample', "Do you want view detail?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            self.visualSam(link)
        else:
            print('No clicked.')

    def visualSam(self, link):
        print(link)
        import os
        path = os.path.realpath(link)
        os.startfile(path)

    def visualSamdetail(self, sampleFile: SampleFile):
        def wrap():
            link = sampleFile.dir
            self.chooseViewSam("Do you want to view Sample detail at ", link)
        return wrap

    def showErrorPopup(self, error):
        msg = QtWidgets.QMessageBox()
        msg.setText(str(error))
        msg.exec_()

    def prevSubAction(self):
        newPage = self.currentPage - 1
        newPage = max(0, newPage)
        self.updateSub(page=newPage)

    def nextSubAction(self):
        newPage = self.currentPage + 1
        newPage = min(newPage, self.numPage)
        self.updateSub(page=newPage)

    def prevSamAction(self):
        newPage = self.currentSamPage - 1
        newPage = max(0, newPage)
        self.updateSam(page=newPage)

    def nextSamAction(self):
        newPage = self.currentSamPage + 1
        newPage = min(newPage, self.numSamPage)
        self.updateSam(page=newPage)

    def closeEvent(self, event):
        print("exit")
        QApplication.quit()

    def openFilePath(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        filenames = [None]
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        path = filenames[0]
        if path == "" or path is None:
            return
        self.storeDir = path + '/'
        self.currentSub = ""
        self.updateSub()

        self.updateSam(listDir=-1)

    def updateInfoSample(self, reuse=False):
        if not reuse:
            newData = {
                'RecorderEdit': "",
                'LocateEdit': "",
                'scenarioNumber': 0,
            }
            self.createSamdialog.setRecodData(newData)
        else:
            # print("ENterrrrrrrrrrrrrrrrrrrr")
            onlydir = []
            link = self.currentSub + '/'
            if os.path.isdir(link):
                onlydir = [link + d for d in os.listdir(link) if os.path.isdir(link + d)]
            onlydir.sort(key=os.path.getctime)
            if len(onlydir) == 0:
                # pop
                return
            lastDir = onlydir[-1] + '/scenario.json'
            # print(lastDir)
            with open(lastDir) as json_file:
                data = json.load(json_file)
            self.createSamdialog.setRecodData(data)

    def samForceQuit(self):
        timers = [self.update_timer, self.pull_timer, self.signalTimer]
        for t in timers:
            t.stop()
            t.deleteLater()
        self.CAMth.stopRecord()
        self.createSamdialog.ui.forceQuit()

    def record_saveData(self):
        if self.record_save:
            self.createRecord()
            return
        self.saveRecord()

    def createRecord(self):
        self.listEvent = []
        self.listEventMarker = []
        RecorderEdit = self.createSamdialog.ui.RecorderEdit.text()
        LocateEdit = self.createSamdialog.ui.LocateEdit.text()
        scenarioNumber = self.createSamdialog.ui.scenarioNumber.value()
        missingValue = False
        if RecorderEdit == '' or LocateEdit == '':
            missingValue = True
        if scenarioNumber == 0:
            missingValue = True

        if not missingValue:
            for btn in self.listEventBtn:
                btn.show()
            self.record_save = False
            self.createSamdialog.ui.recordingStt = True
            # create new sample folder
            link = self.currentSub + '/'
            if os.path.isdir(link):
                onlydir = [link + d for d in os.listdir(link) if os.path.isdir(link + "/" + d)]
            else:
                print("Error in link Sub")
            onlydir.sort(key=os.path.getctime)
            newID = len(onlydir) + 1
            newDir = link + "sample" + str(newID)
            os.mkdir(newDir)
            self.newDir = newDir
            self.CAMth.updateSavingDir(newDir + '/')
            self.CAMth.stopRecord()
            self.ETPlot.updateSaving()

            self.EEGRcv = EEGReceive("new")
            self.EEGtimer = QtCore.QTimer()
            self.EEGtimer.setInterval(10)
            self.EEGtimer.timeout.connect(self.updateEEGRcv)
            self.EEGtimer.start()

            self.timerRcd = QtCore.QTimer()
            self.timerRcd.setInterval(100)
            self.timerRcd.timeout.connect(self.updateTimerRcd)
            self.timerRcd.start()

            self.createSamdialog.ui.rcdBtn.setText("Save")
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.createSamdialog.ui.rcdBtn.setFont(font)
            timers = [self.update_timer, self.pull_timer]
            for t in timers:
                t.stop()
                t.deleteLater()

            self.recordTime = 0
            self.startTime = osTimer.time()
            cmd = "ffmpeg -y -f dshow -rtbufsize 1000M -s 1920x1080 -r 30 -i video=\"Logitech Webcam C930e\" -b:v 5M "
            outVid = '"' + str(self.newDir) + "/FaceGesture.avi" + '"'
            self.pipe = subprocess.Popen(cmd + outVid)

            self.changeStyleRcd()
        else:
            self.showErrorPopup("Please complete fully the form")

    def saveRecord(self):
        print("Enter Save")
        RecorderEdit = self.createSamdialog.ui.RecorderEdit.text()
        LocateEdit = self.createSamdialog.ui.LocateEdit.text()
        scenarioNumber = self.createSamdialog.ui.scenarioNumber.value()
        newData = {
            'RecorderEdit': RecorderEdit,
            'LocateEdit': LocateEdit,
            'scenarioNumber': scenarioNumber,
            'PlanDesc': arg.plans[scenarioNumber - 1]
        }
        self.record_save = True
        self.createSamdialog.ui.widEEG.removeWidget(self.EEGPlot.pw)
        timers = [self.ETtimer, self.signalTimer, self.EEGtimer, self.timerRcd]
        for t in timers:
            t.stop()
            t.deleteLater()
        newDir = self.newDir

        self.pipe.terminate()

        fileName = newDir + '/' + 'scenario.json'
        with open(fileName, 'w') as outfile:
            json.dump(newData, outfile)

        list_ET = self.ETPlot.getSavingData()
        fileNameET = newDir + '/' + 'ET.csv'
        with open(fileNameET, mode='w', newline='', encoding='utf-8') as ETfile:
            fieldnames = ['TimeStamp', 'Data', 'x', 'y', 'character typing', 'sentence']
            et_writer = csv.writer(ETfile)
            et_writer.writerow(fieldnames)
            for row in list_ET:
                et_writer.writerow(row)

        fileNameEEG = newDir + '/' + 'EEG.edf'
        listEEG = self.EEGRcv.getSavingData()

        channels = self.EEGRcv.getInfo()
        rate = self.EEGRcv.getRate()
        EEG_channels = channels[3:-1]
        data = np.asarray(listEEG[0])
        EEGsignals = data[:, 3:-1].T

        signalHeader = pyedf.highlevel.make_signal_headers(
            EEG_channels, dimension='mV', sample_rate=rate, physical_min=-5000.0, physical_max=5000.0,
            digital_min=-32768, digital_max=32767, transducer='', prefiler='')

        print(fileNameEEG[2:])
        f = pyedf.EdfWriter(fileNameEEG[2:], 32)

        f.setEquipment("Emotiv")
        f.setSignalHeaders(signalHeader)
        f.writeSamples(EEGsignals, digital=False)

        eventIdx = 0
        while eventIdx < len(self.listEvent):
            start = self.listEvent[eventIdx][0]
            stop = self.listEvent[eventIdx][1]
            # print(start, stop - start, self.listEventMarker[eventIdx])
            f.writeAnnotation(start - self.startTime, stop - start, self.listEventMarker[eventIdx])

            eventIdx += 1
        f.close()
        print(self.listEventMarker)
        fileName = newDir + '/' + 'eeg.json'
        js = {
            'TaskDesc': arg.plans[scenarioNumber - 1],
            'SamplingFrequence': rate,
            'EEGchannelNumber': EEGsignals.shape[0],
        }
        with open(fileName, 'w') as outfile:
            json.dump(js, outfile)

        fileName = newDir + '/' + 'EEGTimeStamp.txt'
        f = open(fileName, "w")
        for line in listEEG[1]:
            f.write(str(line) + '\n')
        f.close()

        self.createSamdialog.ui.recordingStt = False
        self.createSamdialog.close()
        self.updateSam(page=-1)

    def updateEEGRcv(self):
        self.EEGRcv.update()

    def updateTimerRcd(self):
        self.recordTime = osTimer.time() - self.startTime
        time = "{:.2f}".format(self.recordTime)
        self.createSamdialog.ui.timerNumberLabel.setText("Timer: " + str(time) + " s")

    def testEnter(self):
        print("pass")

    def ET_update(self):
        self.ETPlot.update()
        ETdata = self.ETPlot.lastSample
        if ETdata is not None:
            self.createSamdialog.ui.position.setText(str(ETdata[1]) + " " + str(ETdata[2]))
            self.createSamdialog.ui.character.setText(ETdata[3])
            self.createSamdialog.ui.widScreen.setText(ETdata[4])

    def changeSignal(self):
        counter = 0
        cam1 = True
        cam2 = True
        # print(self.CAMth.numberDevices)
        if self.CAMth.numberDevices < 2:
            cam2 = False
        if self.CAMth.numberDevices < 1:
            cam1 = False
        l1 = [self.ETPlot.signalStt(), self.EEGPlot.signalStt(), cam1, cam2]
        l2 = [self.createSamdialog.ui.SignalET,
              self.createSamdialog.ui.SignalEEG,
              self.createSamdialog.ui.SignalCAM1]
        # print(l1)
        for x in l1:
            if x:
                counter += 1
        if counter >= 1:
            self.createSamdialog.ui.rcdBtn.show()
        else:
            self.createSamdialog.ui.rcdBtn.hide()
        for x, y in zip(l1, l2):
            y.setChecked(not x)

    def changePercent(self):
        # status = requests.get("http://192.168.1.199:8080/device_status")
        self.percent = 0
        # try:
        #     infoDev = status.json()['dev']
        #     self.percent = infoDev[-1][-1]
        # except Exception as e:
        #     print(e, "error catch percent")

        self.createSamdialog.ui.label_EEG.setText("SignalEEG " + str(self.percent) + "%")

    def changeStyleRcd(self):
        self.createSamdialog.ui.turnOnOffBtn.hide()
        self.createSamdialog.ui.rcdBtn.setStyleSheet(u"border-style: outset;\n"
                                                     "border-width: 1px;\n"
                                                     "border-radius: 10px;\n"
                                                     "border-color: beige;\n"
                                                     "background-color: red;\n"
                                                     "padding: 3px;")

    def closeMarker(self, btn):
        self.currentEvent = None
        btn.setStyleSheet("")
        self.listEvent.append([self.currentEventStart, osTimer.time()])
        self.listEventMarker.append(btn.text())

    def setMarker(self, btn):
        btn.setStyleSheet("background-color: yellow")
        self.currentEvent = btn
        self.currentEventStart = osTimer.time()

    def changeEventVisual(self, btn):
        def wrap():
            if self.currentEvent is None:
                btn.setEnabled(True)
                self.setMarker(btn)
            elif self.currentEvent == btn:
                self.closeMarker(btn)
            elif btn.text() == "Resting":
                self.closeMarker(self.currentEvent)
                self.setMarker(btn)
            else:
                print("error")

            # if self.currentEvent is None:
            #     for b in self.listEventBtn:
            #         b.setEnabled(False)
            #     btn.setEnabled(True)
            #     self.listEventBtn[-1].setEnabled()
            #     btn.setStyleSheet("background-color: rgb(252, 202, 65)")
            #     self.currentEvent = btn
            #     self.currentEventStart = osTimer.time()
            # else:
            #     for b in self.listEventBtn:
            #         b.setEnabled(True)
            #         b.setStyleSheet("")
            #     self.currentEvent = None
            #     tmpTimer = osTimer.time()
            #     self.listEvent.append([self.currentEventStart, tmpTimer])
            #     self.listEventMarker.append(btn.text())
        return wrap


def readStorageData(link="./DataVIN/"):
    onlydir = []
    if os.path.isdir(link):
        onlydir = [link + d for d in os.listdir(link) if os.path.isdir(link + d)]
        onlydir.sort(key=os.path.abspath)
    else:
        print("imported link is not exist")
        print("DataVIN folder is created, run again!")
        os.mkdir(link)
    return onlydir


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
        self.ui.RecorderEdit.setText(data['RecorderEdit'])
        self.ui.LocateEdit.setText(data['LocateEdit'])
        self.ui.scenarioNumber.setValue(data['scenarioNumber'])

    def updatePlanView(self):
        text = arg.plans[self.ui.scenarioNumber.value() - 1]
        self.ui.lineEdit.setText(str(text))

    def closeEvent(self, event):
        # event.accept()
        self.ui.closeEvent(event)
        # QApplication.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
