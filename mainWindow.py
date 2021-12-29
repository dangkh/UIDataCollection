# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import json
from arguments import arguments as arg

from utilsUI.subject_folder import SubjectFolder
from utilsUI.sample_file import SampleFile
from utilities import showErrorPopup, createSub
from createSampleDialog import SampleDialog


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        uic.loadUi('UiFiles/mainWindowRcd.ui', self)
        self.listSub = []
        self.listSam = []

    def setupUi(self):
        self.setWindowTitle("HMI")
        self.setObjectName("HMI")
        self.resize(int(1500 * arg.wScale), int(850 * arg.hScale))
        self.patientsGridLayout = self.findChild(QGridLayout, 'patientsGridLayout')
        self.createEvent()

    def createEvent(self):
        self.numItem = 16
        self.currentSub = ""
        self.currentPage = 0
        self.currentSamPage = 0
        self.storeDir = "./DataVIN/"
        self.counter = 0
        self.percent = 0
        self.newSam.hide()
        self.prevSub.hide()
        self.prevSam.hide()
        self.nextSam.hide()
        self.nextSub.hide()

        self.updateSub()

        self.updateSam(listDir=-1)

        # QtCore.QMetaObject.connectSlotsByName(self)
        widget = QWidget()
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
            with open(fileName, 'w', encoding='utf8') as outfile:
                json.dump(js, outfile, ensure_ascii=False)
            self.createSubdialog.ui.close()
            self.updateSub(page=-1)
        else:
            showErrorPopup("Please complete fully the form")

    def newSample(self):
        self.createSamdialog = SampleDialog()
        self.createSamdialog.closeEvent = self.recorderCloseEvent
        self.createSamdialog.setupUi()
        self.createSamdialog.setInfo(self.currentSub)
        self.createSamdialog.setup_connection()

    def recorderCloseEvent(self, event):
        print('Cleanup from Main Window')
        self.createSamdialog.teardown()
        event.accept()
        self.updateSam(page=-1)

    def updateSam(self, listDir=0, page=0):
        nameSubject = str(self.currentSub).split("/")[-1]

        lastDir = self.currentSub + '/info.json'
        try:
            with open(lastDir, 'r', encoding='utf8') as json_file:
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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
