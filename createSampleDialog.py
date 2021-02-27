# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createSample.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from arguments import arg


class Sample_Dialog(QDialog):
    def setupUi(self):
        self.Dialog = QtWidgets.QDialog()

        self.setObjectName("Dialog")
        self.resize(int(1300 * arg.wScale), int(643 * arg.hScale))
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1261, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.infoWidget.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.infoWidget.setObjectName("infoWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.infoWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 391, 369))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.NameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.NameEdit.setObjectName("NameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NameEdit)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.AgeEdit = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.AgeEdit.setObjectName("AgeEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AgeEdit)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MaleEdit = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.MaleEdit.setObjectName("MaleEdit")
        self.horizontalLayout_2.addWidget(self.MaleEdit)
        self.FemaleEdit = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.FemaleEdit.setObjectName("FemaleEdit")
        self.horizontalLayout_2.addWidget(self.FemaleEdit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.RecorderEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.RecorderEdit.setObjectName("RecorderEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RecorderEdit)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.LocateEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.LocateEdit.setObjectName("LocateEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LocateEdit)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.RecPlanEdit = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.RecPlanEdit.setObjectName("RecPlanEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.RecPlanEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fetchInfoBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.fetchInfoBtn.setObjectName("fetchInfoBtn")
        self.horizontalLayout_3.addWidget(self.fetchInfoBtn)
        self.resetBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout_3.addWidget(self.resetBtn)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout.addWidget(self.infoWidget)
        self.visualDatWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.visualDatWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.visualDatWidget.setObjectName("visualDatWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.visualDatWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(120, 110, 561, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.layoutVisual = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.layoutVisual.setContentsMargins(0, 0, 0, 0)
        self.layoutVisual.setObjectName("layoutVisual")

        self.hLayoutVisual_RcdBtn = QtWidgets.QHBoxLayout()
        self.hLayoutVisual_RcdBtn.setContentsMargins(0, 0, 0, 0)
        self.hLayoutVisual_RcdBtn.setObjectName("hLayoutVisual_RcdBtn")
        self.verticalLayout_Timer = QtWidgets.QVBoxLayout()
        self.verticalLayout_Timer.setObjectName("verticalLayout_Timer")
        self.timerLabel = QtWidgets.QLabel()
        self.timerLabel.setObjectName("timerLabel")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timerLabel.setFont(font)
        self.verticalLayout_Timer.addWidget(self.timerLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.timerNumberLabel = QtWidgets.QLabel()
        self.timerNumberLabel.setObjectName("timerNumberLabel")
        self.timerNumberLabel.setFont(font)
        self.verticalLayout_Timer.addWidget(self.timerNumberLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hLayoutVisual_RcdBtn.addLayout(self.verticalLayout_Timer)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.hLayoutVisual_RcdBtn.addItem(spacerItem)
        self.verticalLayout_RcdMenu = QtWidgets.QVBoxLayout()
        self.verticalLayout_RcdMenu.setObjectName("verticalLayout_RcdMenu")
        self.horizontalLayout_menu = QtWidgets.QHBoxLayout()
        self.horizontalLayout_menu.setObjectName("horizontalLayout_menu")
        self.turnOnOffBtn = QtWidgets.QPushButton()
        self.turnOnOffBtn.setObjectName("turnOnOffBtn")
        self.horizontalLayout_menu.addWidget(self.turnOnOffBtn)
        self.rcdBtn = QtWidgets.QPushButton()
        self.rcdBtn.setObjectName("rcdBtn")
        self.horizontalLayout_menu.addWidget(self.rcdBtn)
        self.verticalLayout_RcdMenu.addLayout(self.horizontalLayout_menu)
        # spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout_RcdMenu.addItem(spacerItem1)
        self.horizontalLayout_event = QtWidgets.QHBoxLayout()
        self.horizontalLayout_event.setObjectName("horizontalLayout_event")
        self.type1Btn = QtWidgets.QPushButton()
        self.type1Btn.setObjectName("type1Btn")
        self.horizontalLayout_event.addWidget(self.type1Btn)
        self.type2Btn = QtWidgets.QPushButton()
        self.type2Btn.setObjectName("type2Btn")
        self.horizontalLayout_event.addWidget(self.type2Btn)
        self.type3Btn = QtWidgets.QPushButton()
        self.type3Btn.setObjectName("type3Btn")
        self.horizontalLayout_event.addWidget(self.type3Btn)
        self.verticalLayout_RcdMenu.addLayout(self.horizontalLayout_event)
        self.eventCreateBtn = QtWidgets.QPushButton()
        self.eventCreateBtn.setObjectName("eventCreateBtn")
        self.eventCreateBtn.setStyleSheet(u"border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: beige;\n"
                                          "font: bold 14px;\n"
                                          "background-color : lightblue;\n"
                                          "padding: 6px;")
        # self.verticalLayout_RcdMenu.addWidget(self.eventCreateBtn)
        self.hLayoutVisual_RcdBtn.addLayout(self.verticalLayout_RcdMenu)

        self.layoutVisual.addLayout(self.hLayoutVisual_RcdBtn, 2, 0, 1, 1)
        self.widSignal = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.widSignal.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.widSignal.setObjectName("widSignal")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widSignal)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 559, 126))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gLayoutSignal = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gLayoutSignal.setContentsMargins(0, 0, 0, 0)
        self.gLayoutSignal.setObjectName("gLayoutSignal")
        self.SignalET = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.SignalET.setEnabled(False)
        self.SignalET.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        self.SignalET.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("redBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("greenbt2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("greenbt2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("redBtn.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("redBtn.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.SignalET.setIcon(icon)
        self.SignalET.setCheckable(True)
        self.SignalET.setChecked(True)
        self.SignalET.setObjectName("SignalET")
        self.gLayoutSignal.addWidget(self.SignalET, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_CAM2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_CAM2.setFont(font)
        self.label_CAM2.setObjectName("label_CAM2")
        self.gLayoutSignal.addWidget(self.label_CAM2, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_CAM1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_CAM1.setFont(font)
        self.label_CAM1.setObjectName("label_CAM1")
        self.gLayoutSignal.addWidget(self.label_CAM1, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.SignalEEG = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.SignalEEG.setEnabled(False)
        self.SignalEEG.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        self.SignalEEG.setText("")
        self.SignalEEG.setIcon(icon)
        self.SignalEEG.setCheckable(True)
        self.SignalEEG.setChecked(True)
        self.SignalEEG.setObjectName("SignalEEG")
        self.gLayoutSignal.addWidget(self.SignalEEG, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.SignalCAM1 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.SignalCAM1.setEnabled(False)
        self.SignalCAM1.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        self.SignalCAM1.setText("")
        self.SignalCAM1.setIcon(icon)
        self.SignalCAM1.setCheckable(True)
        self.SignalCAM1.setChecked(True)
        self.SignalCAM1.setObjectName("SignalCAM1")
        self.gLayoutSignal.addWidget(self.SignalCAM1, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_ET = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ET.setFont(font)
        self.label_ET.setObjectName("label_ET")
        self.gLayoutSignal.addWidget(self.label_ET, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.SignalCAM2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.SignalCAM2.setEnabled(False)
        self.SignalCAM2.setStyleSheet("background-color: rgba(255,255,255,0);border: 0px;")
        self.SignalCAM2.setText("")
        self.SignalCAM2.setIcon(icon)
        self.SignalCAM2.setCheckable(True)
        self.SignalCAM2.setChecked(True)
        self.SignalCAM2.setObjectName("SignalCAM2")
        self.gLayoutSignal.addWidget(self.SignalCAM2, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_EEG = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_EEG.setFont(font)
        self.label_EEG.setObjectName("label_EEG")
        self.gLayoutSignal.addWidget(self.label_EEG, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.layoutVisual.addWidget(self.widSignal, 0, 0, 1, 1)
        self.hLayoutData = QtWidgets.QHBoxLayout()
        self.hLayoutData.setSpacing(0)
        self.hLayoutData.setObjectName("hLayoutData")
        self.vLayoutDataLeft = QtWidgets.QVBoxLayout()
        self.vLayoutDataLeft.setSpacing(0)
        self.vLayoutDataLeft.setObjectName("vLayoutDataLeft")
        self.CAM2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.CAM2.setStyleSheet("background-color: rgb(185, 209, 234);")
        self.CAM2.setObjectName("CAM2")
        self.vLayoutDataLeft.addWidget(self.CAM2)
        self.CAM1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.CAM1.setStyleSheet("background-color: rgb(220, 82, 70);")
        self.CAM1.setObjectName("CAM1")
        self.vLayoutDataLeft.addWidget(self.CAM1)
        self.hLayoutData.addLayout(self.vLayoutDataLeft)
        self.vLayoutDataRight = QtWidgets.QVBoxLayout()
        self.vLayoutDataRight.setSpacing(0)
        self.vLayoutDataRight.setObjectName("vLayoutDataRight")
        self.widEEG = QtWidgets.QStackedWidget(self.gridLayoutWidget_2)
        self.widEEG.setStyleSheet("background-color: rgb(178, 202, 226);")
        self.widEEG.setObjectName("widEEG")
        self.vLayoutDataRight.addWidget(self.widEEG)
        self.hLayoutWidET = QtWidgets.QHBoxLayout()
        self.hLayoutWidET.setSpacing(0)
        self.hLayoutWidET.setObjectName("hLayoutWidET")
        self.widScreen = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.widScreen.setStyleSheet("background-color: rgb(252, 202, 65);")
        self.widScreen.setObjectName("widScreen")
        self.widScreen.setFont(font)
        # self.CAM2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        # self.CAM2.setStyleSheet("background-color: rgb(185, 209, 234);")
        # self.CAM2.setObjectName("CAM2")

        self.hLayoutWidET.addWidget(self.widScreen)
        self.vLayoutETch = QtWidgets.QVBoxLayout()
        self.vLayoutETch.setObjectName("vLayoutETch")
        self.position = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.position.setFont(font)
        self.position.setStyleSheet("")
        self.position.setObjectName("position")
        self.vLayoutETch.addWidget(self.position, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.character = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.character.setFont(font)
        self.character.setObjectName("character")
        self.vLayoutETch.addWidget(self.character, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hLayoutWidET.addLayout(self.vLayoutETch)
        self.hLayoutWidET.setStretch(0, 3)
        self.hLayoutWidET.setStretch(1, 1)
        self.vLayoutDataRight.addLayout(self.hLayoutWidET)
        self.hLayoutData.addLayout(self.vLayoutDataRight)
        self.hLayoutData.setStretch(0, 1)
        self.hLayoutData.setStretch(1, 3)
        self.layoutVisual.addLayout(self.hLayoutData, 1, 0, 1, 1)
        self.layoutVisual.setRowStretch(0, 2)
        self.layoutVisual.setRowStretch(1, 7)
        self.layoutVisual.setRowStretch(2, 1)
        self.horizontalLayout.addWidget(self.visualDatWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.createEvent()

    def createEvent(self):
        self.infoWidget.setLayout(self.verticalLayout)
        self.visualDatWidget.setLayout(self.layoutVisual)
        self.widSignal.setLayout(self.gLayoutSignal)
        self.setLayout(self.horizontalLayout)
        # self.eventCreateBtn.clicked.connect(lambda: self.changeStyle(self.eventCreateBtn))
        self.recordingStt = True

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Tạo bản ghi mới"))
        self.label.setText(_translate("Dialog", "Thông tin người thu"))
        self.label_4.setText(_translate("Dialog", "Họ tên người bệnh"))
        self.label_5.setText(_translate("Dialog", "Tuổi"))
        self.label_6.setText(_translate("Dialog", "Giới tính"))
        self.MaleEdit.setText(_translate("Dialog", "Nam"))
        self.FemaleEdit.setText(_translate("Dialog", "Nữ"))
        self.label_8.setText(_translate("Dialog", "Thông tin kịch bản thu"))
        self.label_11.setText(_translate("Dialog", "Kỹ thuật viên"))
        self.label_12.setText(_translate("Dialog", "Địa điểm"))
        self.label_13.setText(_translate("Dialog", "Kịch bản"))
        self.fetchInfoBtn.setText(_translate("Dialog", "Lây thông tin cũ"))
        self.resetBtn.setText(_translate("Dialog", "Xóa thông tin"))
        self.label_CAM2.setText(_translate("Dialog", "CAM2"))
        self.label_CAM1.setText(_translate("Dialog", "CAM1"))
        self.label_ET.setText(_translate("Dialog", "ET"))
        self.label_EEG.setText(_translate("Dialog", "EEG"))
        self.position.setText(_translate("Dialog", "NONE"))
        self.character.setText(_translate("Dialog", "NONE"))
        self.timerLabel.setText(_translate("Dialog", "Timer"))
        self.timerNumberLabel.setText(_translate("Dialog", "0s"))
        self.turnOnOffBtn.setText(_translate("Dialog", "Thoát"))
        self.rcdBtn.setText(_translate("Dialog", "Record"))
        self.type1Btn.setText(_translate("Dialog", "Nghĩ"))
        self.type2Btn.setText(_translate("Dialog", "Nghĩ và Hành động"))
        self.type3Btn.setText(_translate("Dialog", "Gõ bàn phím"))
        self.eventCreateBtn.setText(_translate("Dialog", "Tạo event"))

    def closeEvent(self, event):
        print("recordingStt: ", self.recordingStt)
        if not self.recordingStt:
            print("QUIT")
            event.accept()
            self.close()
        else:
            self.showErrorPopup("Hãy ấn Tắt nếu muốn đóng cửa sổ này")
            event.ignore()

        # super(Sample_Dialog, self).quitTimer()

    def showErrorPopup(self, error):
        msg = QtWidgets.QMessageBox()
        msg.setText(str(error))
        msg.exec_()

    def forceQuit(self):
        self.recordingStt = False
        self.close()


class textSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(textSpinBox, self).__init__(parent)
        self.set_list_string()

    def set_list_string(self, strings=None):
        if strings is not None:
            self.list_text = strings
        else:
            self.list_text = ["Khỏe", "Bình thường", "Yếu"]
        self.setRange(0, len(self.list_text) - 1)

    def textFromValue(self, value):
        return self.list_text[value]


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = Sample_Dialog()
#     ui.setupUi()
#     ui.show()
#     sys.exit(app.exec_())