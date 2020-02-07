# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\insta_thief\counter.ui',
# licensing of 'D:\Python\insta_thief\counter.ui' applies.
#
# Created: Fri Nov 29 17:27:22 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 371)
        self.plus_button = QtWidgets.QPushButton(Dialog)
        self.plus_button.setGeometry(QtCore.QRect(10, 80, 483, 211))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setWeight(75)
        font.setBold(True)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        self.minus_button = QtWidgets.QPushButton(Dialog)
        self.minus_button.setGeometry(QtCore.QRect(10, 300, 483, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.result_label = QtWidgets.QLabel(Dialog)
        self.result_label.setGeometry(QtCore.QRect(10, 10, 483, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result_label.setFont(font)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.set_counter = QtWidgets.QPushButton(Dialog)
        self.set_counter.setGeometry(QtCore.QRect(350, 340, 71, 21))
        self.set_counter.setObjectName("set_counter")
        self.reset_counter = QtWidgets.QPushButton(Dialog)
        self.reset_counter.setGeometry(QtCore.QRect(422, 340, 71, 21))
        self.reset_counter.setObjectName("reset_counter")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 340, 131, 16))
        self.label.setObjectName("label")
        self.set_counter_line_edit = QtWidgets.QLineEdit(Dialog)
        self.set_counter_line_edit.setGeometry(QtCore.QRect(245, 340, 100, 21))
        self.set_counter_line_edit.setObjectName("set_counter_line_edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.plus_button.setText(QtWidgets.QApplication.translate("Dialog", "+1", None, -1))
        self.minus_button.setText(QtWidgets.QApplication.translate("Dialog", "-1", None, -1))
        self.result_label.setText(QtWidgets.QApplication.translate("Dialog", "Счетчик", None, -1))
        self.set_counter.setText(QtWidgets.QApplication.translate("Dialog", "Ввести", None, -1))
        self.reset_counter.setText(QtWidgets.QApplication.translate("Dialog", "Отменить", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Установить значение:", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

