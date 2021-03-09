from PyQt5 import QtWidgets, QtGui, QtCore
import json

class SampleFile:
    def __init__(self, path, enabled=True):
        self.sampleWidget = QtWidgets.QWidget()
        self.sampleWidget.setObjectName(str(path) + '-widget')
        self.infoBox = QtWidgets.QVBoxLayout(self.sampleWidget)
        self.infoBox.setContentsMargins(0, 0, 0, 0)
        self.infoBox.setObjectName(str(path) + '-box')
        self.button = QtWidgets.QPushButton(self.sampleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("mfiles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setObjectName(str(path) + '-button')
        self.infoBox.addWidget(self.button)
        self.label = QtWidgets.QLabel(self.sampleWidget)
        self.label.setObjectName(str(path) + '-label')
        self.label.setText("")
        self.infoBox.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.infoBox.setStretch(0, 4)
        self.infoBox.setStretch(1, 1)

        self.sampleWidget.setEnabled(enabled)

        if enabled:
            lastDir = path + '/scenario.json'
            with open(lastDir) as json_file:
                data = json.load(json_file)
            subjectName = str(path).split("/")[-1] + " (scenario_" + str(data["RecPlanEdit"]) + ")"

            self.label.setText(subjectName)
            self.button.setIcon(icon1)
            self.button.setIconSize(QtCore.QSize(50, 50))
            self.dir = path
        else:
            self.button.setIcon(icon2)

    def remove(self):
        self.button.setParent(None)
        self.label.setParent(None)
