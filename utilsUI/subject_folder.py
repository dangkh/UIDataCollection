from PyQt5 import QtWidgets, QtGui, QtCore
import json

class SubjectFolder:
    def __init__ (self, path, enabled=True):
        self.subjectWidget = QtWidgets.QWidget()
        self.subjectWidget.setObjectName(str(path) + '-widget')
        self.infoBox = QtWidgets.QVBoxLayout(self.subjectWidget)
        self.infoBox.setContentsMargins(0, 0, 0, 0)
        self.infoBox.setObjectName(str(path) + '-box')
        self.button = QtWidgets.QPushButton(self.subjectWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        self.button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("folder-blue-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(50, 50))
        self.button.setObjectName(str(path) + '-btn')
        self.infoBox.addWidget(self.button)
        self.label = QtWidgets.QLabel(self.subjectWidget)
        self.label.setObjectName(str(path) + '-label')
        self.label.setText("")
        self.infoBox.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.infoBox.setStretch(0, 4)
        self.infoBox.setStretch(1, 1)

        self.subjectWidget.setEnabled(enabled)

        if enabled:
            nameSubject = str(path).split("/")[-1]
            lastDir = path + '/info.json'
            with open(lastDir, 'r', encoding='utf8') as json_file:
                data = json.load(json_file)
            nameSubject = nameSubject + " (" + data["name"] + ")"
            self.label.setText(nameSubject)
            self.dir = path

    def remove(self):
        self.button.setParent(None)
        self.label.setParent(None)
