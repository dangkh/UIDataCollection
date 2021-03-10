# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preProcessingMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
import json
# from dialogData import Ui_Dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from utilities import *
from mnelab.mnelab.__main__ import *
from mainwindow import OtherMainWindow
from model import Model
from PyQt5.QtWidgets import QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1296, 830)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../.designer/backup/my-beautiful-life-logo-3.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 1211, 751))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layoutVisual = QtWidgets.QVBoxLayout()
        self.layoutVisual.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layoutVisual.setObjectName("layoutVisual")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layoutVisual.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.currentIdx = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.currentIdx.setText("")
        self.currentIdx.setObjectName("currentIdx")
        self.gridLayout.addWidget(self.currentIdx, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.leftIdx = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.leftIdx.setText("")
        self.leftIdx.setObjectName("leftIdx")
        self.gridLayout.addWidget(self.leftIdx, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.rightIdx = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.rightIdx.setText("")
        self.rightIdx.setObjectName("rightIdx")
        self.gridLayout.addWidget(self.rightIdx, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.defaultData = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultData.sizePolicy().hasHeightForWidth())
        self.defaultData.setSizePolicy(sizePolicy)
        self.defaultData.setObjectName("defaultData")
        self.horizontalLayout.addWidget(self.defaultData)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.layoutVisual.addLayout(self.verticalLayout)
        self.layoutVisual.setStretch(0, 600)
        self.layoutVisual.setStretch(1, 100)
        self.gridLayout_2.addLayout(self.layoutVisual, 0, 1, 1, 1)
        self.layoutMetaData = QtWidgets.QVBoxLayout()
        self.layoutMetaData.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layoutMetaData.setObjectName("layoutMetaData")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutMetaData.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.formMetaData = QtWidgets.QFormLayout()
        self.formMetaData.setObjectName("formMetaData")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formMetaData.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.NameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.NameEdit.setObjectName("NameEdit")
        self.formMetaData.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NameEdit)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formMetaData.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.AgeEdit = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.AgeEdit.setObjectName("AgeEdit")
        self.formMetaData.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AgeEdit)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formMetaData.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.layoutGender = QtWidgets.QHBoxLayout()
        self.layoutGender.setObjectName("layoutGender")
        self.MaleEdit = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.MaleEdit.setObjectName("MaleEdit")
        self.layoutGender.addWidget(self.MaleEdit)
        self.FemaleEdit = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.FemaleEdit.setObjectName("FemaleEdit")
        self.layoutGender.addWidget(self.FemaleEdit)
        self.formMetaData.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.layoutGender)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formMetaData.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.DiseaseDescEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.DiseaseDescEdit.setObjectName("DiseaseDescEdit")
        self.formMetaData.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DiseaseDescEdit)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formMetaData.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.RecorderEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.RecorderEdit.setObjectName("RecorderEdit")
        self.formMetaData.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.RecorderEdit)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formMetaData.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.LocateEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.LocateEdit.setObjectName("LocateEdit")
        self.formMetaData.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.LocateEdit)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formMetaData.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.RecPlanEdit = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.RecPlanEdit.setObjectName("RecPlanEdit")
        self.formMetaData.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.RecPlanEdit)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.formMetaData.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.sentenceIdEdit = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.sentenceIdEdit.setObjectName("sentenceIdEdit")
        self.formMetaData.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sentenceIdEdit)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formMetaData.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.formMetaData.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formMetaData.setItem(10, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formMetaData.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.layoutMetaData.addLayout(self.formMetaData)
        self.gridLayout_2.addLayout(self.layoutMetaData, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 300)
        self.gridLayout_2.setColumnStretch(1, 600)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1296, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreprocessing_Tool = QtWidgets.QMenu(self.menubar)
        self.menuPreprocessing_Tool.setObjectName("menuPreprocessing_Tool")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionScale_up = QtWidgets.QAction(MainWindow)
        self.actionScale_up.setObjectName("actionScale_up")
        self.actionScale_down = QtWidgets.QAction(MainWindow)
        self.actionScale_down.setObjectName("actionScale_down")
        self.actionUp = QtWidgets.QAction(MainWindow)
        self.actionUp.setObjectName("actionUp")
        self.actionDown = QtWidgets.QAction(MainWindow)
        self.actionDown.setObjectName("actionDown")
        self.actionICA = QtWidgets.QAction(MainWindow)
        self.actionICA.setObjectName("actionICA")
        self.actionFFT = QtWidgets.QAction(MainWindow)
        self.actionFFT.setObjectName("actionFFT")
        self.actionVisual_Left = QtWidgets.QAction(MainWindow)
        self.actionVisual_Left.setObjectName("actionVisual_Left")
        self.actionVisual_Right = QtWidgets.QAction(MainWindow)
        self.actionVisual_Right.setObjectName("actionVisual_Right")
        self.actionMove_Up = QtWidgets.QAction(MainWindow)
        self.actionMove_Up.setObjectName("actionMove_Up")
        self.actionMove_Down = QtWidgets.QAction(MainWindow)
        self.actionMove_Down.setObjectName("actionMove_Down")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        self.menuPreprocessing_Tool.addAction(self.actionICA)
        self.menuPreprocessing_Tool.addAction(self.actionFFT)
        self.menuHelp.addAction(self.actionScale_up)
        self.menuHelp.addAction(self.actionScale_down)
        self.menuHelp.addAction(self.actionUp)
        self.menuHelp.addAction(self.actionDown)
        self.menuHelp.addAction(self.actionVisual_Left)
        self.menuHelp.addAction(self.actionVisual_Right)
        self.menuHelp.addAction(self.actionMove_Up)
        self.menuHelp.addAction(self.actionMove_Down)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreprocessing_Tool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.createEvent()
        widget = QtWidgets.QWidget()
        widget.setLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(widget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HMIlab"))
        self.defaultData.setText(_translate("MainWindow", "Tùy chọn kênh"))
        self.label.setText(_translate("MainWindow", "Tên dữ liệu"))
        self.label_7.setText(_translate("MainWindow", "Họ tên người bệnh"))
        self.label_8.setText(_translate("MainWindow", "Tuổi"))
        self.label_9.setText(_translate("MainWindow", "Giới tính"))
        self.MaleEdit.setText(_translate("MainWindow", "Nam"))
        self.FemaleEdit.setText(_translate("MainWindow", "Nữ"))
        self.label_14.setText(_translate("MainWindow", "Mô tả bệnh"))
        self.label_10.setText(_translate("MainWindow", "Kỹ thuật viên"))
        self.label_11.setText(_translate("MainWindow", "Địa điểm"))
        self.label_12.setText(_translate("MainWindow", "Kịch bản"))
        self.label_21.setText(_translate("MainWindow", "Câu trong kịch bản"))
        self.label_13.setText(_translate("MainWindow", "Thời gian"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreprocessing_Tool.setTitle(_translate("MainWindow", "Preprocessing Tool"))
        self.menuHelp.setTitle(_translate("MainWindow", "Visual setups"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as "))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionScale_up.setText(_translate("MainWindow", "Scale up"))
        self.actionScale_down.setText(_translate("MainWindow", "Scale down"))
        self.actionUp.setText(_translate("MainWindow", "Visual Up"))
        self.actionDown.setText(_translate("MainWindow", "Visual Down"))
        self.actionICA.setText(_translate("MainWindow", "ICA"))
        self.actionFFT.setText(_translate("MainWindow", "FFT"))
        self.actionVisual_Left.setText(_translate("MainWindow", "Visual Left"))
        self.actionVisual_Right.setText(_translate("MainWindow", "Visual Right"))
        self.actionMove_Up.setText(_translate("MainWindow", "Move Up"))
        self.actionMove_Down.setText(_translate("MainWindow", "Move Down"))

    def createEvent(self):
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.closeApp)
        self.actionOpen_file.setShortcut("Ctrl+O")
        self.actionOpen_file.setStatusTip('Open file browser')
        self.actionOpen_file.triggered.connect(self.openFilePath)

        self.actionUp.setShortcut(QtGui.QKeySequence("Up"))
        self.actionUp.triggered.connect(self.keyUpEvent)

        self.actionDown.setShortcut(QtGui.QKeySequence("Down"))
        self.actionDown.triggered.connect(self.keyDownEvent)

        self.actionMove_Up.setShortcut(QtGui.QKeySequence("PgUp"))
        self.actionMove_Up.triggered.connect(self.keyPageUpEvent)

        self.actionMove_Down.setShortcut(QtGui.QKeySequence("PgDown"))
        self.actionMove_Down.triggered.connect(self.keyPageDownEvent)

        self.actionScale_up.setShortcut(QtGui.QKeySequence("Home"))
        self.actionScale_up.triggered.connect(self.keyScaleUpEvent)

        self.actionScale_down.setShortcut(QtGui.QKeySequence("End"))
        self.actionScale_down.triggered.connect(self.keyScaleDownEvent)

        self.actionICA.setShortcut(QtGui.QKeySequence("Ctrl+I"))
        self.actionICA.triggered.connect(self.ICAEvent)

        self.actionFFT.setShortcut(QtGui.QKeySequence("Ctrl+F"))
        self.actionFFT.triggered.connect(self.toDoEvent)
        # self.createTextSpinBox()
        # create maximum chanels can be reviewed
        self.channelSpacing = 200
        self.channelVisualLen = 1000
        self.defaultChanel = 8
        self.counter = 0
        self.horizontalSlider.hide()
        self.horizontalSlider.valueChanged.connect(self.changeValueSL)
        self.channels = (range(32))
        self.numDefaultChan = 8
        self.defaultChanel = np.copy(self.channels)
        np.random.shuffle(self.defaultChanel)
        # colors = [name for name in mcd.CSS4_COLORS if "xkcd:" + name in mcd.XKCD_COLORS]
        colors = ['aqua', 'aquamarine', 'black', 'blue', 'brown', 'chartreuse', 'chocolate', 'coral',
                  'crimson', 'cyan', 'darkblue', 'darkgreen', 'fuchsia', 'gold', 'goldenrod', 'green', 'grey', 'indigo',
                  'ivory', 'khaki', 'lavender', 'lightblue', 'lightgreen', 'lime', 'magenta', 'maroon', 'navy', 'olive',
                  'orange', 'orangered', 'orchid', 'pink', 'plum', 'purple', 'red', 'salmon', 'sienna', 'silver', 'tan',
                  'teal', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'yellow', 'yellowgreen']
        # there is loads of color not good at visualizing, eliminate some.
        # np.random.shuffle(colors)
        self.colors = colors
        self.choosedChannel = self.defaultChanel[:self.numDefaultChan]
        self.listChannel = []
        self.currentChannel = self.choosedChannel
        # self.data = readFile("exampleEEG.csv").T[:, 3:17]
        preName = "self.Ui_Dialog."
        self.signalNames = ["A1", "A2", "C3", "C4", "CP3", "CP4",
                            "CPz", "Cz", "F17", "F18", "F3", "F4",
                            "F7", "F8", "FC3", "FC4", "FCz", "FP1",
                            "Fp2", "Fz", "O1", "O2", "Oz", "P3",
                            "P4", "P7", "P8", "Pz", "T7", "T8",
                            "TP7", "TP8"]
        self.list_names = []
        for x in range(len(self.signalNames)):
            self.list_names.append(preName + "Signal_" + self.signalNames[x])
        self.defaultData.hide()
        self.defaultData.clicked.connect(self.openDialog)
        # hide preprocessing tool
        self.canvas = None
        self.existData = False
        self.channelDistCof = 100
        self.channelReduceCof = 4100

    def toDoEvent(self):
        print("completing")

    def ICAEvent(self):
        runningICA()
        self.model = Model()
        self.model.view = OtherMainWindow(self.model)
        self.model.view.show()
        print("ICA")

    def keyScaleUpEvent(self):
        if not self.existData:
            return
        print("Scale Up")
        self.channelVisualLen += 50
        plt.cla()
        self.canvas.draw()
        self.plotData()

    def keyScaleDownEvent(self):
        if not self.existData:
            return
        print("Scale Down")
        self.channelVisualLen -= 50
        self.channelVisualLen = max(200, self.channelVisualLen)
        plt.cla()
        self.canvas.draw()
        self.plotData()

    def keyPageUpEvent(self):
        if not self.existData:
            return
        print("Page Up")
        self.channelReduceCof += 50
        self.updatePlot()

    def keyPageDownEvent(self):
        if not self.existData:
            return
        print("Page Down")
        self.channelReduceCof -= 50
        self.updatePlot()

    def keyUpEvent(self):
        if not self.existData:
            return
        print("Up")
        self.channelDistCof += 10
        self.updatePlot()

    def keyDownEvent(self):
        if not self.existData:
            return
        print("Down")
        self.channelDistCof -= 10
        self.updatePlot()

    def openDialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.Ui_Dialog = Ui_Dialog()
        self.Ui_Dialog.setupUi(self.Dialog)
        self.Ui_Dialog.checkBox.stateChanged.connect(self.setCheckableSignal)
        self.list_signals = []
        for x in self.list_names:
            self.list_signals.append(eval(x))
        self.setCheckableSignal()
        for idx in range(len(self.list_signals)):
            self.list_signals[idx].clicked.connect(self.btnConnect)
        self.Ui_Dialog.saveChoosingBtn.clicked.connect(self.updateChooseBtn)
        self.Dialog.show()

    def updateChooseBtn(self):
        self.currentChannel = self.choosedChannel
        plt.cla()
        self.plotData()

    def setCheckableSignal(self):
        if self.Ui_Dialog.checkBox.isChecked():
            self.choosedChannel = self.defaultChanel[:self.numDefaultChan]
            for x in self.list_signals:
                x.setCheckable(True)
                x.setEnabled(False)
                x.setChecked(True)
            for idx in self.defaultChanel[:self.numDefaultChan]:
                x = self.list_signals[idx]
                x.setCheckable(True)
                x.setEnabled(False)
                x.setChecked(False)
        else:
            for x in self.list_signals:
                x.setCheckable(True)
                x.setEnabled(True)
                x.setChecked(True)
            self.btnConnect()
            self.choosedChannel = self.listChannel

    def btnConnect(self):
        self.listChannel = []
        for x in range(len(self.list_signals)):
            if self.list_signals[x].isChecked():
                self.listChannel.append(x)
        self.choosedChannel = self.listChannel

    def createTextSpinBox(self):
        self.spinBox_2.set_list_string(["ICA", "Threshold", "Auto"])

    def openFilePath(self):
        fname = QFileDialog.getOpenFileName(filter="Json (*.json)")
        path = fname[0]

        if path == "" or path is None:
            return
        with open(path) as json_file:
            data = json.load(json_file)

        self.NameEdit.setText(data['name'])
        self.AgeEdit.setValue(data['age'])
        if data['gender'] == 'M':
            self.MaleEdit.setChecked(True)
        else:
            self.FemaleEdit.setChecked(True)
        self.DiseaseDescEdit.setText(data['patientDesc'])
        self.RecorderEdit.setText(data['recorder'])
        self.LocateEdit.setText(data['location'])
        self.RecPlanEdit.setValue(data['recPlan'])
        self.sentenceIdEdit.setValue(data['sentenceID'])
        dataTime = QtCore.QDateTime.fromString(data['time'], 'd/M/yyyy hh:mm')
        self.dateTimeEdit.setDateTime(dataTime)
        listEditatble = [self.NameEdit, self.AgeEdit, self.MaleEdit, self.FemaleEdit, self.DiseaseDescEdit,
                         self.RecorderEdit, self.LocateEdit, self.RecPlanEdit, self.sentenceIdEdit, self.dateTimeEdit]
        for x in listEditatble:
            x.setEnabled(False)

        self.label.setText(str(path).split('/')[-1])
        dataLen = len(data['EEG'])
        dataLen = self.data.shape[0]
        self.EEG = data['EEG']
        self.displayEEG()
        self.setupSlider(dataLen, 0)
        self.defaultData.show()
        self.existData = True

    def setupSlider(self, dataLen, point=500):
        self.horizontalSlider.show()
        self.currentVisualEEG = point
        checkPoint = min(point, self.data.shape[0])
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.data.shape[0])
        self.horizontalSlider.setValue(self.currentVisualEEG)
        self.currentIdx.setText("Current position: " + str(checkPoint))
        self.leftIdx.setText(str(0))
        self.rightIdx.setText(str(self.data.shape[0]))
        self.currentSliderValue = 0

    def changeValueSL(self):
        value = self.horizontalSlider.value()
        value = min(self.data.shape[0] - self.channelVisualLen, value)
        self.currentSliderValue = value
        self.currentIdx.setText("Current position: " + str(value))
        self.updatePlot()

    def updatePlot(self):
        value = self.currentSliderValue
        for idx, channel in enumerate(self.currentChannel):
            xc = min(channel, 13)
            self.listLines[idx].set_ydata(self.data[value:self.channelVisualLen + value,
                                                    xc] - self.channelReduceCof + idx * self.channelDistCof)
        self.canvas.draw()

    def plotData(self):
        xdata = (range(self.channelVisualLen))
        self.listLines = []
        for idx, channel in enumerate(self.currentChannel):
            xc = min(channel, 13)
            line, = plt.plot(xdata, self.data[:self.channelVisualLen,
                                              xc] - self.channelReduceCof + idx * self.channelDistCof,
                             self.colors[idx], lw=1)
            self.listLines.append(line)
            plt.text(0, idx * self.channelDistCof,
                     self.signalNames[self.currentChannel[idx]], verticalalignment='bottom',
                     horizontalalignment='right', color=self.colors[idx], fontsize=10)
        ax = plt.axes()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        self.canvas.draw()

    def displayEEG(self):
        if self.canvas is None:
            fig = plt.figure(figsize=(5, 4), dpi=100)
            self.canvas = FigureCanvasQTAgg(fig)
            self.verticalLayout_2.addWidget(self.canvas)
        else:
            plt.cla()
            self.canvas.draw()
            # self.canvas = FigureCanvasQTAgg(fig)
        self.plotData()

    def closeApp(self, event):
        print("exit")
        QApplication.quit()


class textSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(textSpinBox, self).__init__(parent)
        self.set_list_string()

    def set_list_string(self, strings=None):
        if strings is not None:
            self.list_text = strings
        else:
            self.list_text = ["EEG", "ET"]
        self.setRange(0, len(self.list_text) - 1)

    def textFromValue(self, value):
        return self.list_text[value]


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("HMIlab")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
