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
from dialogData import Ui_Dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from utility import *
import matplotlib._color_data as mcd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1296, 827)
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
        spacerItem = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formMetaData.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
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
        self.layoutMetaData.addLayout(self.formMetaData)
        self.formSelectData = QtWidgets.QFormLayout()
        self.formSelectData.setObjectName("formSelectData")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formSelectData.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBoxData = textSpinBox(self.gridLayoutWidget_2)
        self.spinBoxData.setObjectName("spinBoxData")
        self.horizontalLayout_3.addWidget(self.spinBoxData)
        self.defaultData = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultData.sizePolicy().hasHeightForWidth())
        self.defaultData.setSizePolicy(sizePolicy)
        self.defaultData.setObjectName("defaultData")
        self.horizontalLayout_3.addWidget(self.defaultData)
        self.formSelectData.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formSelectData.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox_2 = textSpinBox(self.gridLayoutWidget_2)
        self.spinBox_2.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formSelectData.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formSelectData.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.doubleSpinBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formSelectData.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setWhatsThis("")
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
                                      "    background-color: rgb(167, 192, 220);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 2px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#pushButton:pressed {\n"
                                      "    background-color: rgb(171, 196, 223);\n"
                                      "    border-style: inset;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.formSelectData.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.layoutMetaData.addLayout(self.formSelectData)
        self.gridLayout_2.addLayout(self.layoutMetaData, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 300)
        self.gridLayout_2.setColumnStretch(1, 600)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1296, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.createEvent()
        widget = QtWidgets.QWidget()
        widget.setLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(widget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Chọn loại dữ liệu"))
        self.defaultData.setText(_translate("MainWindow", "Default"))
        self.label_5.setText(_translate("MainWindow", "Chọn Phương pháp"))
        self.label_6.setText(_translate("MainWindow", "Tham số 01"))
        self.pushButton.setText(_translate("MainWindow", "Áp dụng"))
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
        self.label_7.setText(_translate("MainWindow", "Họ tên người bệnh"))
        self.label.setText(_translate("MainWindow", "Tên dữ liệu"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as "))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def createEvent(self):
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.closeApp)
        self.actionOpen_file.setShortcut("Ctrl+O")
        self.actionOpen_file.setStatusTip('Open file browser')
        self.actionOpen_file.triggered.connect(self.openFilePath)
        self.createTextSpinBox()
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
        colors = [name for name in mcd.CSS4_COLORS if "xkcd:" + name in mcd.XKCD_COLORS]
        np.random.shuffle(colors)
        self.colors = colors
        self.choosedChannel = self.defaultChanel[:self.numDefaultChan]
        self.listChannel = []
        self.currentChannel = self.choosedChannel
        self.data = readFile("exampleEEG.csv").T[:, 3:17]
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
        self.defaultData.clicked.connect(self.openDialog)
        self.canvas = None

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
        self.EEG = data['EEG']
        self.displayEEG()
        self.setupSlider(dataLen, dataLen // 2)

    def setupSlider(self, dataLen, point=500):
        self.horizontalSlider.show()
        self.currentVisualEEG = point
        minV = point - dataLen // 2
        maxV = point + dataLen // 2
        self.horizontalSlider.setMinimum(minV)
        self.horizontalSlider.setMaximum(maxV)
        self.horizontalSlider.setValue(self.currentVisualEEG)
        self.currentIdx.setText(str(self.currentVisualEEG))
        self.leftIdx.setText(str(minV))
        self.rightIdx.setText(str(maxV))

    def changeValueSL(self):
        value = self.horizontalSlider.value()
        self.currentSliderValue = value
        self.currentIdx.setText(str(value))
        self.updatePlot()

    def updatePlot(self):
        value = self.currentSliderValue
        for idx, channel in enumerate(self.currentChannel):
            xc = min(channel, 13)
            self.listLines[idx].set_ydata(self.data[value:1000 + value, xc] - 4100 + idx * 100)
        self.canvas.draw()

    def plotData(self):
        xdata = (range(1000))
        self.listLines = []
        for idx, channel in enumerate(self.currentChannel):
            xc = min(channel, 13)
            line, = plt.plot(xdata, self.data[:1000, xc] - 4100 + idx * 100, self.colors[idx], lw=1)
            self.listLines.append(line)
            plt.text(-100, self.data[0, xc] - 4100 + idx * 100, self.signalNames[self.currentChannel[idx]],
                     verticalalignment='bottom', horizontalalignment='right',
                     color=self.colors[idx], fontsize=10)
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

    def closeApp(self):
        sys.exit()


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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
