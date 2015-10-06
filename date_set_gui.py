# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date_set.ui'
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

class Ui_date_set(object):
    def setupUi(self, date_set):
        date_set.setObjectName(_fromUtf8("date_set"))
        date_set.setWindowModality(QtCore.Qt.NonModal)
        date_set.resize(700, 310)
        date_set.setMinimumSize(QtCore.QSize(700, 310))
        date_set.setMaximumSize(QtCore.QSize(700, 310))
        date_set.setSizeGripEnabled(False)
        date_set.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(date_set)
        self.buttonBox.setGeometry(QtCore.QRect(500, 260, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.calendarWidget = QtGui.QCalendarWidget(date_set)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 448, 291))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.date_from = QtGui.QDateEdit(date_set)
        self.date_from.setGeometry(QtCore.QRect(500, 120, 181, 27))
        self.date_from.setObjectName(_fromUtf8("date_from"))
        self.date_to = QtGui.QDateEdit(date_set)
        self.date_to.setGeometry(QtCore.QRect(500, 166, 181, 27))
        self.date_to.setObjectName(_fromUtf8("date_to"))
        self.label = QtGui.QLabel(date_set)
        self.label.setGeometry(QtCore.QRect(470, 125, 16, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(date_set)
        self.label_2.setGeometry(QtCore.QRect(470, 170, 21, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButton = QtGui.QRadioButton(date_set)
        self.radioButton.setGeometry(QtCore.QRect(500, 20, 116, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(date_set)
        self.radioButton_2.setGeometry(QtCore.QRect(500, 70, 116, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.templateBox = QtGui.QComboBox(date_set)
        self.templateBox.setGeometry(QtCore.QRect(470, 210, 211, 27))
        self.templateBox.setObjectName(_fromUtf8("templateBox"))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))
        self.templateBox.addItem(_fromUtf8(""))

        self.retranslateUi(date_set)
        self.templateBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), date_set.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), date_set.reject)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.date_to.hide)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label.hide)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label.show)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_2.show)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.date_to.show)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_2.hide)
        QtCore.QMetaObject.connectSlotsByName(date_set)
        date_set.setTabOrder(self.buttonBox, self.date_from)
        date_set.setTabOrder(self.date_from, self.date_to)
        date_set.setTabOrder(self.date_to, self.radioButton)
        date_set.setTabOrder(self.radioButton, self.radioButton_2)
        date_set.setTabOrder(self.radioButton_2, self.calendarWidget)

    def retranslateUi(self, date_set):
        date_set.setWindowTitle(_translate("date_set", "Выбор периода", None))
        self.date_from.setDisplayFormat(_translate("date_set", "dd MMMM yyyy", None))
        self.date_to.setDisplayFormat(_translate("date_set", "dd MMMM yyyy", None))
        self.label.setText(_translate("date_set", "С", None))
        self.label_2.setText(_translate("date_set", "По", None))
        self.radioButton.setText(_translate("date_set", "Один день", None))
        self.radioButton_2.setText(_translate("date_set", "Период", None))
        self.templateBox.setItemText(0, _translate("date_set", "Вчера", None))
        self.templateBox.setItemText(1, _translate("date_set", "Сегодня", None))
        self.templateBox.setItemText(2, _translate("date_set", "Завтра", None))
        self.templateBox.setItemText(3, _translate("date_set", "Прошлая неделя", None))
        self.templateBox.setItemText(4, _translate("date_set", "Текущая неделя", None))
        self.templateBox.setItemText(5, _translate("date_set", "Следующая неделя", None))
        self.templateBox.setItemText(6, _translate("date_set", "Прошлый месяц", None))
        self.templateBox.setItemText(7, _translate("date_set", "Текущий месяц", None))
        self.templateBox.setItemText(8, _translate("date_set", "Следующий месяц", None))

