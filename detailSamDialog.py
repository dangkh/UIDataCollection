# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDetailSam.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class detailSam_Dialog(QDialog):
    def setupUi(self):
        self.Dialog = QtWidgets.QDialog()
        self.setObjectName("Dialog")
        self.resize(615, 193)
        self.sampleWidget = QtWidgets.QWidget()
        self.sampleWidget.setGeometry(QtCore.QRect(20, 10, 551, 361))
        self.sampleWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sampleWidget.setObjectName("sampleWidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.sampleWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 60, 481, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalSample = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalSample.setContentsMargins(0, 0, 0, 0)
        self.verticalSample.setObjectName("verticalSample")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalSample.addWidget(self.label_2)
        self.gridLayout_sample = QtWidgets.QGridLayout()
        self.gridLayout_sample.setObjectName("gridLayout_sample")
        self.verticalSample.addLayout(self.gridLayout_sample)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalSample.addItem(spacerItem)
        self.horizontalLayout_sample = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sample.setObjectName("horizontalLayout_sample")
        self.verticalSample.addLayout(self.horizontalLayout_sample)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setLayout(self.verticalSample)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Chi tiết bản ghi"))
        self.label_2.setText(_translate("Dialog", "Bản ghi"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = detailSam_Dialog()
#     ui.setupUi()
#     ui.show()
#     sys.exit(app.exec_())
