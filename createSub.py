# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createSubject.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import *


class createSub_Dialog(QDialog):
    def setupUi(self):
        self.Dialog = QtWidgets.QDialog()
        self.setObjectName("Dialog")
        self.resize(435, 293)
        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 381, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.saveBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveBtn.setObjectName("saveBtn")
        self.verticalLayout.addWidget(self.saveBtn)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.setLayout(self.verticalLayout)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Tạo thông tin người bệnh mới"))
        self.label_4.setText(_translate("Dialog", "Họ tên người bệnh"))
        self.label_5.setText(_translate("Dialog", "Tuổi"))
        self.label_6.setText(_translate("Dialog", "Giới tính"))
        self.MaleEdit.setText(_translate("Dialog", "Nam"))
        self.FemaleEdit.setText(_translate("Dialog", "Nữ"))
        self.label_7.setText(_translate("Dialog", "ID người bệnh"))
        self.saveBtn.setText(_translate("Dialog", "Lưu"))


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
#     # Dialog = QtWidgets.QDialog()
#     ui = createSub_Dialog()
#     ui.setupUi()
#     ui.show()
#     # Dialog.show()
#     sys.exit(app.exec_())