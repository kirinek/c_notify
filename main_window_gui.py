# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
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

class Ui_table_window(object):
    def setupUi(self, table_window):
        table_window.setObjectName(_fromUtf8("table_window"))
        table_window.resize(1280, 600)
        table_window.setMinimumSize(QtCore.QSize(1280, 600))
        self.centralwidget = QtGui.QWidget(table_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.the_table = QtGui.QTableWidget(self.centralwidget)
        self.the_table.setGeometry(QtCore.QRect(10, 60, 1031, 192))
        self.the_table.setShowGrid(True)
        self.the_table.setGridStyle(QtCore.Qt.SolidLine)
        self.the_table.setObjectName(_fromUtf8("the_table"))
        self.the_table.setColumnCount(10)
        self.the_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.the_table.setHorizontalHeaderItem(9, item)
        self.contractBox = QtGui.QComboBox(self.centralwidget)
        self.contractBox.setGeometry(QtCore.QRect(960, 10, 78, 45))
        self.contractBox.setMinimumSize(QtCore.QSize(0, 45))
        self.contractBox.setObjectName(_fromUtf8("contractBox"))
        self.contractBox.addItem(_fromUtf8(""))
        self.contractBox.addItem(_fromUtf8(""))
        self.contractBox.addItem(_fromUtf8(""))
        self.agreedBox = QtGui.QComboBox(self.centralwidget)
        self.agreedBox.setGeometry(QtCore.QRect(1050, 10, 78, 45))
        self.agreedBox.setMinimumSize(QtCore.QSize(0, 45))
        self.agreedBox.setObjectName(_fromUtf8("agreedBox"))
        self.agreedBox.addItem(_fromUtf8(""))
        self.agreedBox.addItem(_fromUtf8(""))
        self.agreedBox.addItem(_fromUtf8(""))
        self.commentEdit = QtGui.QLineEdit(self.centralwidget)
        self.commentEdit.setGeometry(QtCore.QRect(350, 10, 280, 45))
        self.commentEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.commentEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.commentEdit.setFont(font)
        self.commentEdit.setObjectName(_fromUtf8("commentEdit"))
        self.phoneEdit = QtGui.QLineEdit(self.centralwidget)
        self.phoneEdit.setGeometry(QtCore.QRect(90, 10, 20, 45))
        self.phoneEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.phoneEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.phoneEdit.setFont(font)
        self.phoneEdit.setObjectName(_fromUtf8("phoneEdit"))
        self.c_dateButton = QtGui.QPushButton(self.centralwidget)
        self.c_dateButton.setGeometry(QtCore.QRect(250, 10, 95, 44))
        self.c_dateButton.setMinimumSize(QtCore.QSize(0, 44))
        self.c_dateButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.c_dateButton.setObjectName(_fromUtf8("c_dateButton"))
        self.informedBox = QtGui.QComboBox(self.centralwidget)
        self.informedBox.setGeometry(QtCore.QRect(630, 10, 107, 45))
        self.informedBox.setMinimumSize(QtCore.QSize(0, 45))
        self.informedBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.informedBox.setObjectName(_fromUtf8("informedBox"))
        self.informedBox.addItem(_fromUtf8(""))
        self.informedBox.addItem(_fromUtf8(""))
        self.informedBox.addItem(_fromUtf8(""))
        self.p_dateButton = QtGui.QPushButton(self.centralwidget)
        self.p_dateButton.setGeometry(QtCore.QRect(130, 10, 95, 45))
        self.p_dateButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_dateButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.p_dateButton.setObjectName(_fromUtf8("p_dateButton"))
        self.nameEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameEdit.setEnabled(True)
        self.nameEdit.setGeometry(QtCore.QRect(60, 10, 20, 44))
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.nameEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.afterBox = QtGui.QComboBox(self.centralwidget)
        self.afterBox.setGeometry(QtCore.QRect(850, 10, 107, 45))
        self.afterBox.setMinimumSize(QtCore.QSize(0, 45))
        self.afterBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.afterBox.setObjectName(_fromUtf8("afterBox"))
        self.afterBox.addItem(_fromUtf8(""))
        self.afterBox.addItem(_fromUtf8(""))
        self.afterBox.addItem(_fromUtf8(""))
        self.beforeBox = QtGui.QComboBox(self.centralwidget)
        self.beforeBox.setGeometry(QtCore.QRect(740, 10, 107, 45))
        self.beforeBox.setMinimumSize(QtCore.QSize(0, 45))
        self.beforeBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.beforeBox.setObjectName(_fromUtf8("beforeBox"))
        self.beforeBox.addItem(_fromUtf8(""))
        self.beforeBox.addItem(_fromUtf8(""))
        self.beforeBox.addItem(_fromUtf8(""))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(10, 10, 45, 44))
        self.searchButton.setMinimumSize(QtCore.QSize(0, 44))
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        table_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(table_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        table_window.setMenuBar(self.menubar)
        self.status_bar = QtGui.QStatusBar(table_window)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        table_window.setStatusBar(self.status_bar)
        self.menu_refresh = QtGui.QAction(table_window)
        self.menu_refresh.setObjectName(_fromUtf8("menu_refresh"))
        self.menu_settings = QtGui.QAction(table_window)
        self.menu_settings.setObjectName(_fromUtf8("menu_settings"))
        self.menu_help = QtGui.QAction(table_window)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        self.menu_quit = QtGui.QAction(table_window)
        self.menu_quit.setObjectName(_fromUtf8("menu_quit"))
        self.menu_about = QtGui.QAction(table_window)
        self.menu_about.setObjectName(_fromUtf8("menu_about"))
        self.menu.addAction(self.menu_refresh)
        self.menu.addAction(self.menu_settings)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_help)
        self.menu.addAction(self.menu_about)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_quit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(table_window)
        QtCore.QMetaObject.connectSlotsByName(table_window)

    def retranslateUi(self, table_window):
        table_window.setWindowTitle(_translate("table_window", "Список клиентов", None))
        item = self.the_table.horizontalHeaderItem(0)
        item.setText(_translate("table_window", "ФИО", None))
        item = self.the_table.horizontalHeaderItem(1)
        item.setText(_translate("table_window", "Телефон", None))
        item = self.the_table.horizontalHeaderItem(2)
        item.setText(_translate("table_window", "Дата покупки", None))
        item = self.the_table.horizontalHeaderItem(3)
        item.setText(_translate("table_window", "Срок замены", None))
        item = self.the_table.horizontalHeaderItem(4)
        item.setText(_translate("table_window", "Комментарии", None))
        item = self.the_table.horizontalHeaderItem(5)
        item.setText(_translate("table_window", "Инофрмирован", None))
        item = self.the_table.horizontalHeaderItem(6)
        item.setText(_translate("table_window", "Согласен", None))
        item = self.the_table.horizontalHeaderItem(7)
        item.setText(_translate("table_window", "Контракт", None))
        item = self.the_table.horizontalHeaderItem(8)
        item.setText(_translate("table_window", "Купил до срока", None))
        item = self.the_table.horizontalHeaderItem(9)
        item.setText(_translate("table_window", "Купил после срока", None))
        self.contractBox.setItemText(0, _translate("table_window", "Неопределено", None))
        self.contractBox.setItemText(1, _translate("table_window", "Да", None))
        self.contractBox.setItemText(2, _translate("table_window", "Нет", None))
        self.agreedBox.setItemText(0, _translate("table_window", "Неопределено", None))
        self.agreedBox.setItemText(1, _translate("table_window", "Да", None))
        self.agreedBox.setItemText(2, _translate("table_window", "Нет", None))
        self.c_dateButton.setText(_translate("table_window", "Срок\n"
"замены", None))
        self.informedBox.setItemText(0, _translate("table_window", "Неопределено", None))
        self.informedBox.setItemText(1, _translate("table_window", "Да", None))
        self.informedBox.setItemText(2, _translate("table_window", "Нет", None))
        self.p_dateButton.setText(_translate("table_window", "Дата\n"
"покупки", None))
        self.afterBox.setItemText(0, _translate("table_window", "Неопределено", None))
        self.afterBox.setItemText(1, _translate("table_window", "Да", None))
        self.afterBox.setItemText(2, _translate("table_window", "Нет", None))
        self.beforeBox.setItemText(0, _translate("table_window", "Неопределено", None))
        self.beforeBox.setItemText(1, _translate("table_window", "Да", None))
        self.beforeBox.setItemText(2, _translate("table_window", "Нет", None))
        self.searchButton.setText(_translate("table_window", "Поиск", None))
        self.menu.setTitle(_translate("table_window", "Файл", None))
        self.menu_refresh.setText(_translate("table_window", "Обновить", None))
        self.menu_settings.setText(_translate("table_window", "Настройки", None))
        self.menu_help.setText(_translate("table_window", "Справка", None))
        self.menu_quit.setText(_translate("table_window", "Выход", None))
        self.menu_about.setText(_translate("table_window", "О программе", None))
