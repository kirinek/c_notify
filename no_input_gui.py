# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'no_input.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_no_input(object):
    def setupUi(self, no_input):
        no_input.setObjectName(_fromUtf8("no_input"))
        no_input.resize(390, 110)
        no_input.setMinimumSize(QtCore.QSize(390, 110))
        no_input.setMaximumSize(QtCore.QSize(390, 110))
        self.label = QtGui.QLabel(no_input)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(no_input)
        QtCore.QMetaObject.connectSlotsByName(no_input)

    def retranslateUi(self, no_input):
        no_input.setWindowTitle(_translate("no_input", "Dialog", None))
        self.label.setText(_translate("no_input", "Выгрузка не найдена!", None))

