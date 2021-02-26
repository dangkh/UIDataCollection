# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuBottomLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Dialog(QDialog):
    def setupUi(self):
        self.Dialog = QtWidgets.QDialog()
        
        self.setObjectName("Dialog")
        self.resize(800, 256)
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 30, 581, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")


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
        self.verticalLayout_Timer.addWidget(self.timerLabel)
        self.timerNumberLabel = QtWidgets.QLabel()
        self.timerNumberLabel.setObjectName("timerNumberLabel")
        self.timerNumberLabel.setFont(font)
        self.verticalLayout_Timer.addWidget(self.timerNumberLabel)
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
        # self.eventCreateBtn.setStyleSheet(
        #                     "QPushButton"
        #                      "{"
        #                      "background-color : lightblue;"
        #                      "}"
        #                      )
        self.verticalLayout_RcdMenu.addWidget(self.eventCreateBtn)
        self.hLayoutVisual_RcdBtn.addLayout(self.verticalLayout_RcdMenu)
        self.eventCreateBtn.clicked.connect(lambda: self.changeStyle(self.eventCreateBtn))
        self.hLayoutVisual_RcdBtn.setStretch(0, 4)
        self.hLayoutVisual_RcdBtn.setStretch(10, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        self.setLayout(self.hLayoutVisual_RcdBtn)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.timerLabel.setText(_translate("Dialog", "Timer"))
        self.timerNumberLabel.setText(_translate("Dialog", "0s"))
        self.turnOnOffBtn.setText(_translate("Dialog", "Thoát"))
        self.rcdBtn.setText(_translate("Dialog", "Record"))
        self.type1Btn.setText(_translate("Dialog", "Nghĩ"))
        self.type2Btn.setText(_translate("Dialog", "Nghĩ và Hành động"))
        self.type3Btn.setText(_translate("Dialog", "Gõ bàn phím"))
        self.eventCreateBtn.setText(_translate("Dialog", "Tạo event"))

    def changeStyle(self, btn):
        btn.setStyleSheet("QPushButton"
                             "{"
                             "background-color : red;"
                             "}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())