__author__ = 'kuroi'

import sys
import os
from PyQt4 import QtCore, QtGui
from date_set_gui import Ui_date_set
import sqlite3
from g_classes import *

periods = CalendarTemplates()
init_dict = {'NAME': '', 'PHONE': '', 'P_DATE': '', 'C_DATE': '', 'COMMENT': '',
             'INFORMED': '', 'AGREED': '', 'CONTRACT': '', 'B_B': '', 'B_A': ''}
search_dict = {'NAME': '', 'PHONE': '', 'P_DATE': '', 'C_DATE': '', 'COMMENT': '',
               'INFORMED': '', 'AGREED': '', 'CONTRACT': '', 'B_B': '', 'B_A': ''}
db_path_name = './dbs/cn.db'
input_path = './input/'


def initialize():

    from parsers import import_from_txt

    if not os.path.exists(db_path_name):                                # if there is no such file or dir
        db_connection = sqlite3.connect(db_path_name)                   # create one, connect and create a table.
        db_connection.execute('PRAGMA foreign_keys = ON')               # foreign_keys are off by default
        db_connection.execute('''CREATE TABLE NAMES (
        CUSTOMER_ID     INT     PRIMARY KEY NOT NULL,
        NAME    TEXT    NOT NULL,
        PHONE   INT,    COMMENT TEXT,
        AGREED  TEXT    NOT NULL
        )''')
        db_connection.execute('''CREATE TABLE NOTIFY (
        ID      INT     PRIMARY KEY NOT NULL,
        CUSTOMER_ID     INT         NOT NULL,
        P_DATE  TEXT    NOT NULL,   C_DATE      TEXT    NOT_NULL,
        INFORMED    TEXT    NOT NULL,
        CONTRACT    TEXT    NOT NULL,
        B_B     TEXT    NOT NULL,   B_A         TEXT    NOT NULL
        )''')
        db_connection.close()

    if not os.path.isfile(db_path_name):                                # if the given path and name exist
        print('something wrong with database file. shutting down')      # something is broken.
        return 13

    if periods.today.date.dayOfWeek() < 5:                              # setting initial period to display
        init_dict['C_DATE'] = periods.this_week.to_sql()                # whether it's current week
    else:
        init_dict['C_DATE'] = periods.next_week.to_sql()                # or next week
    init_dict['INFORMED'] = 'Нет'                                       # and of course my favorite damn flags
    init_dict['AGREED'] = 'Да'
    init_dict['B_B'] = 'Нет'
    init_dict['B_A'] = 'Нет'

    import_from_txt(db_path_name, input_path)                           # execute parsing of new text tables from 1C


def search_db(search=search_dict):                                 # TODO: unite search_strings() & run_query()
    """forms a string for SQLite db query from global 'search_dict' dictionary
    and provides a tuple of necessary arguments for sqlite3.connect().execute
    returns: query_string, (arg1, ...)"""
    query_strings = []
    query_args = []
    global search_dict
    for item_name, item in search.items():
        if item:
            if (item_name == 'NAME') or (item_name == 'PHONE') or (item_name == 'COMMENT'):
                item = '%' + item + '%'
                query_strings.append('(' + item_name + ' LIKE ?)')
                query_args.append(item)
                # search_dict[item_name] = ''
            elif (item_name == 'P_DATE') or (item_name == 'C_DATE'):
                query_strings.append('(' + item_name + ' ' + item[0] + ')')
                query_args.extend(item[1:])
                # search_dict[item_name] = ''
            else:
                query_strings.append('(' + item_name + ' == ?)')
                query_args.append(item)
    query_strings = '''SELECT NAME, PHONE, P_DATE, C_DATE, COMMENT, INFORMED, AGREED, CONTRACT, B_B, B_A, ID
                      FROM NOTIFY NATURAL JOIN NAMES WHERE ''' + ' AND '.join(str(s) for s in query_strings)
    query_args = tuple(query_args)

    db_connection = sqlite3.connect(db_path_name)
    data_rows = []
    try:
        data_rows = db_connection.execute(query_strings, query_args).fetchall()
    except ValueError:
        print('wrong SQLite query. run_query')
        exit(1)
    except sqlite3.ProgrammingError:
        print('incorrect number of SQLite arguments. run_query')
        exit(1)
    # except sqlite3.OperationalError:
    #     print('Operational Error. Seems because of empty query')
    # except sqlite3.InterfaceError
    db_connection.close()
    return data_rows


class ComboDelegate(QtGui.QItemDelegate):
    def __init__(self, owner, itemlist):
        QtGui.QItemDelegate.__init__(self, owner)
        self.itemslist = itemlist

    def createEditor(self, parent, option, index):
        self.editor = QtGui.QComboBox(parent)
        for i in range(0, len(self.itemslist)):
            self.editor.addItem(str(self.itemslist[i]))

        return self.editor

    def setEditorData(self, editor, index):
        value = index.data(QtCore.Qt.DisplayRole)
        editor.setCurrentIndex(self.itemslist.index(value))

    def setModelData(self, editor, model, index):
        value = self.itemslist[editor.currentIndex()]
        # print(value)
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class DateWindow(QtGui.QDialog, Ui_date_set):
    def __init__(self, parent=None):
        today = periods.today
        self.focused = True

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.calendarWidget.setDateRange(today.date.addYears(-5), today.date.addYears(20))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setFirstDayOfWeek(1)
        self.date_from.setDateRange(today.date.addYears(-5), today.date.addYears(20))
        self.date_to.setDateRange(today.date.addYears(-5), today.date.addYears(20))
        self.date_from.setDate(today.date)
        self.date_to.setDate(today.date)

        self.is_one_day()
        self.templateBox.setCurrentIndex(1)
        self.calendarWidget.selectionChanged.connect(self.set_dates)
        self.templateBox.currentIndexChanged.connect(self.choose_template)

    def set_dates(self):
        if self.radioButton.isChecked():
            self.date_from.setDate(self.calendarWidget.selectedDate())
        else:
            if self.focused:
                self.date_from.setDate(self.calendarWidget.selectedDate())
                self.focused = False
            else:
                self.date_to.setDate(self.calendarWidget.selectedDate())
                self.focused = True

    def return_period(self):
        from g_classes import Days
        if self.radioButton.isChecked():
            result = Days(self.date_from.date())
            return result.to_sql()
        else:
            if self.date_from.date() < self.date_to.date():
                result = Days(self.date_from.date(), self.date_to.date())
                return result.to_sql()
            elif self.date_from.date() > self.date_to.date():
                result = Days(self.date_to.date(), self.date_from.date())
                return result.to_sql()
            else:
                result = Days(self.date_from.date())
                return result.to_sql()

    def choose_template(self):
        date_from = self.date_from
        date_to = self.date_to
        choice = self.templateBox.currentIndex()
        if choice < 3:
            self.radioButton.setChecked(True)
            if choice == 0:
                date_from.setDate(periods.yesterday.date)
            elif choice == 1:
                date_from.setDate(periods.today.date)
            elif choice == 2:
                date_from.setDate(periods.tomorrow.date)
        else:
            self.radioButton_2.setChecked(True)
            if choice == 3:
                date_from.setDate(periods.last_week.date)
                date_to.setDate(periods.last_week.period)
            elif choice == 4:
                date_from.setDate(periods.this_week.date)
                date_to.setDate(periods.this_week.period)
            elif choice == 5:
                date_from.setDate(periods.next_week.date)
                date_to.setDate(periods.next_week.period)
            elif choice == 6:
                date_from.setDate(periods.last_month.date)
                date_to.setDate(periods.last_month.period)
            elif choice == 7:
                date_from.setDate(periods.this_month.date)
                date_to.setDate(periods.this_month.period)
            elif choice == 8:
                date_from.setDate(periods.next_month.date)
                date_to.setDate(periods.next_month.period)
        self.focused = True
        self.calendarWidget.setSelectedDate(self.date_from.date())

    def is_one_day(self):
        self.label.hide()
        self.label_2.hide()
        self.date_to.hide()


class WindowMain(QtGui.QMainWindow):
    resize_signal = QtCore.pyqtSignal()                                 # new signal for window resize

    def __init__(self, parent=None):
        from main_window_gui import Ui_table_window
        QtGui.QMainWindow.__init__(self, parent)

        self.ui = Ui_table_window()                                     # setting form
        self.ui.setupUi(self)

        itemlist = ['Да', 'Нет']
        self.ui.the_table.setItemDelegateForColumn(5, ComboDelegate(self.ui.the_table, itemlist))
        self.ui.the_table.setItemDelegateForColumn(6, ComboDelegate(self.ui.the_table, itemlist))

        self.ui.informedBox.setCurrentIndex(2)
        self.ui.beforeBox.setCurrentIndex(2)
        self.ui.afterBox.setCurrentIndex(2)
        self.ui.agreedBox.setCurrentIndex(0)
        self.ui.contractBox.setCurrentIndex(0)

        self.status_bar_refresh(init_dict)                              # setting initial period in status bar
        self.fill_in_table(search_db(init_dict))                        # initial table filling with init period's data

        self.connections()                                              # setting connections for this window

    def connections(self):
        form = self.ui

        self.ui.menu_quit.setShortcut('Ctrl+Q')
        self.ui.menu_quit.triggered.connect(self.hide_window)

        search_button_press = QtGui.QAction(self)                           # This is a piece of magic
        search_button_press.setShortcut(QtGui.QKeySequence('Ctrl+return'))  # dunno how it works it's just a prayer
        self.connect(search_button_press, QtCore.SIGNAL("activated()"),     # of a lonely Cargo-cult adept
                     self.ui.searchButton, QtCore.SLOT("animateClick()"))   # this code just makes a search_button
        # search_button_press.connect(self.read_data)                       # TODO: find out why it's not working
        self.addAction(search_button_press)                                 # be clickable by a 'return' shortcut

        self.resize_signal.connect(self.align)
        form.searchButton.clicked.connect(self.read_data)
        form.p_dateButton.clicked.connect(lambda: self.set_search_period('p'))
        form.c_dateButton.clicked.connect(lambda: self.set_search_period('c'))
        form.informedBox.currentIndexChanged.connect(lambda: self.set_flags(form.informedBox.currentIndex(),
                                                                            'INFORMED'))
        form.beforeBox.currentIndexChanged.connect(lambda: self.set_flags(form.beforeBox.currentIndex(),
                                                                          'B_B'))
        form.afterBox.currentIndexChanged.connect(lambda: self.set_flags(form.afterBox.currentIndex(),
                                                                         'B_A'))
        form.agreedBox.currentIndexChanged.connect(lambda: self.set_flags(form.agreedBox.currentIndex(),
                                                                          'AGREED'))
        form.contractBox.currentIndexChanged.connect(lambda: self.set_flags(form.contractBox.currentIndex(),
                                                                            'CONTRACT'))
        form.the_table.itemChanged.connect(lambda: self.change_db_value(form.the_table.currentRow(),
                                                                        form.the_table.currentColumn()))
        form.the_table.horizontalHeader().sectionResized.connect(self.resize_widgets)

    def disconnections(self, b=True):
        form = self.ui
        if b:
            form.the_table.itemChanged.disconnect()
            form.informedBox.currentIndexChanged.disconnect()
            form.beforeBox.currentIndexChanged.disconnect()
            form.afterBox.currentIndexChanged.disconnect()
            form.agreedBox.currentIndexChanged.disconnect()
            form.contractBox.currentIndexChanged.disconnect()
        else:
            form.the_table.itemChanged.connect(lambda: self.change_db_value(self.ui.the_table.currentRow(),
                                                                            self.ui.the_table.currentColumn()))
            form.informedBox.currentIndexChanged.connect(lambda: self.set_flags(form.informedBox.currentIndex(),
                                                                                'INFORMED'))
            form.beforeBox.currentIndexChanged.connect(lambda: self.set_flags(form.beforeBox.currentIndex(),
                                                                              'B_B'))
            form.afterBox.currentIndexChanged.connect(lambda: self.set_flags(form.afterBox.currentIndex(),
                                                                             'B_A'))
            form.agreedBox.currentIndexChanged.connect(lambda: self.set_flags(form.agreedBox.currentIndex(),
                                                                             'agreed'))
            form.contractBox.currentIndexChanged.connect(lambda: self.set_flags(form.contractBox.currentIndex(),
                                                                                'CONTRACT'))

    def read_data(self):
        """sets global 'search_dict' values with current values of lineEdits"""
        global search_dict

        # without this every cell will be filled with random and written to the db:
        self.disconnections()
        # connecting this back in the end of method

        search_dict['NAME'] = self.ui.nameEdit.text()               # getting data from edit lines
        search_dict['PHONE'] = self.ui.phoneEdit.text()
        search_dict['COMMENT'] = self.ui.commentEdit.text()

        for k, i in search_dict.items():                            # looking through the dict
            if i:                                                   # if there is anything in the search_dict,
                self.fill_in_table(search_db())                     # then run a search in db and fill the table
                self.status_bar_refresh()                           # update status bar period

                self.ui.nameEdit.setText('')                        # return all our widgets
                self.ui.phoneEdit.setText('')                       # to primordial state
                self.ui.commentEdit.setText('')
                self.ui.informedBox.setCurrentIndex(2)
                self.ui.beforeBox.setCurrentIndex(2)
                self.ui.afterBox.setCurrentIndex(2)
                self.ui.agreedBox.setCurrentIndex(1)
                self.ui.contractBox.setCurrentIndex(0)
                self.change_button_text()
                self.status_bar_refresh()

                # now we need to connect table and db again and then exit method
                self.disconnections(False)

                # noinspection PyAssignmentToLoopOrWithParameter
                for k, i in search_dict.items():                    # this loop clears the search_dict of previous data
                    if i:
                        search_dict[k] = ''
                return
        # if the search_dict is empty, we use init_dict instead
        self.fill_in_table(search_db(init_dict))                    # fill the table with init period's data
        self.status_bar_refresh(init_dict)                          # update status bar with init period
        # and connect the table and db back again
        self.disconnections(False)

    def fill_in_table(self, data_rows):
        """takes a list as an arg and fills the table with its rows and columns"""
        from parsers import date_transform

        self.ui.the_table.setRowCount(len(data_rows))                       # setting row number by number of strings
        list_of_ids = []                                                    # the list is for table's vertical header
        # query_strings = '''SELECT NAME, PHONE, P_DATE, C_DATE, COMMENT, INFORMED, AGREED, CONTRACT, B_B, B_A, ID
        #               FROM NOTIFY NATURAL JOIN NAMES WHERE ''' + ' AND '.join(str(s) for s in query_strings)
        for row in range(0, len(data_rows)):                                # from first to last row:
            list_of_ids.append(str(data_rows[row][-1]))                     # add new purchase-id from current row
            data_rows[row] = [f for f in data_rows[row]]                    # changing the row from tuple to list TODO: use list()?
            data_rows[row][2] = date_transform(data_rows[row][2], '.', 0)   # transforming dates from SQLite format
            data_rows[row][3] = date_transform(data_rows[row][3], '.', 0)   # to human-readable format (dd-mm-yyyy)
            for column in range(0, 10):                                     # filling table loop
                item = QtGui.QTableWidgetItem(str(data_rows[row][column]))  # creating new item with text from db
                if (column < 4) or (column > 6):                            # setting columns 0-3 and 6-9
                    item.setFlags(QtCore.Qt.ItemIsEnabled)                  # user read-only
                self.ui.the_table.setItem(row, column, item)                # inserting a new item in a cell
        self.ui.the_table.setVerticalHeaderLabels(list_of_ids)              # filling vertical headers labels

    def change_db_value(self, row, column):
        if self.ui.the_table.selectedIndexes():
            try:
                id_number = self.ui.the_table.verticalHeaderItem(row).text()
                value = self.ui.the_table.item(row, column).text()
            except AttributeError:
                print('cell is not selected')
                return
            db_connection = sqlite3.connect(db_path_name)
            if column == 5:
                query_string = 'UPDATE NOTIFY SET INFORMED = ? WHERE ID == ?'
            else:
                id_number = db_connection.execute('SELECT CUSTOMER_ID FROM NOTIFY WHERE ID == ?',
                                                  (id_number,)).fetchone()[0]
                if column == 4:
                    query_string = 'UPDATE NAMES SET COMMENT = ? WHERE CUSTOMER_ID == ?'
                else:
                    query_string = 'UPDATE NAMES SET AGREED = ? WHERE CUSTOMER_ID == ?'
            db_connection.execute(query_string, (str(value), str(id_number)))
            db_connection.commit()
            db_connection.close()

    def set_search_period(self, date_type):
        """takes 'p' or 'c' as second argument, calls the date_set dialog
        and sets corresponding global 'search_dict' date values and button text"""
        global search_dict
        period_dlg = DateWindow(self)
        if period_dlg.exec_():
            values = period_dlg.return_period()
            if date_type == 'p':
                search_dict['P_DATE'] = values
                self.change_button_text('P_DATE')
            elif date_type == 'c':
                search_dict['C_DATE'] = values
                self.change_button_text('C_DATE')

    def resize_widgets(self):

        # calculating space left after resizing first five columns
        space_left = self.ui.the_table.geometry().width()
        for i in range(0, 5):
            space_left -= self.ui.the_table.columnWidth(i)
        # and dividing it on left five columns
        space_left /= 5
        for i in range(5, 10):
            self.ui.the_table.setColumnWidth(i, space_left - 20)    # without this '- 20' crutch last column runs away

        # setting widgets up accordingly to the corresponding column
        self.ui.nameEdit.setGeometry(self.ui.searchButton.geometry().right() + 5, 10,
                                     self.ui.the_table.columnWidth(0) - 5, 45)
        self.ui.phoneEdit.setGeometry(self.ui.nameEdit.geometry().right() + 6, 10,
                                      self.ui.the_table.columnWidth(1) - 5, 45)
        self.ui.p_dateButton.setGeometry(self.ui.phoneEdit.geometry().right() + 6, 10,
                                         self.ui.the_table.columnWidth(2) - 5, 45)
        self.ui.c_dateButton.setGeometry(self.ui.p_dateButton.geometry().right() + 6, 10,
                                         self.ui.the_table.columnWidth(3) - 5, 45)
        self.ui.commentEdit.setGeometry(self.ui.c_dateButton.geometry().right() + 6, 10,
                                        self.ui.the_table.columnWidth(4) - 5, 45)
        self.ui.informedBox.setGeometry(self.ui.commentEdit.geometry().right() + 6, 10,
                                        self.ui.the_table.columnWidth(5) - 5, 45)
        self.ui.agreedBox.setGeometry(self.ui.informedBox.geometry().right() + 6, 10,
                                      self.ui.the_table.columnWidth(6) - 5, 45)
        self.ui.contractBox.setGeometry(self.ui.agreedBox.geometry().right() + 6, 10,
                                        self.ui.the_table.columnWidth(7) - 5, 45)
        self.ui.beforeBox.setGeometry(self.ui.contractBox.geometry().right() + 6, 10,
                                      self.ui.the_table.columnWidth(8) - 5, 45)
        self.ui.afterBox.setGeometry(self.ui.beforeBox.geometry().right() + 6, 10,
                                     self.ui.the_table.columnWidth(9) - 5, 45)

    def status_bar_refresh(self, s_dict=search_dict):
        """Updates status bar text with chosen period"""
        from parsers import date_transform
        p = ''
        c = ''
        if s_dict['P_DATE']:
            l = list(s_dict['P_DATE'][1:])
            for i in range(0, len(l)):
                l[i] = date_transform(l[i], '.', 0)
            if len(l) == 2:
                p = 'период покупок c ' + l[0] + ' по ' + l[1]
            else:
                p = 'период покупок: ' + l[0]
        if s_dict['C_DATE']:
            l = list(s_dict['C_DATE'][1:])
            for i in range(0, len(l)):
                l[i] = date_transform(l[i], '.', 0)
            if len(l) == 2:
                c = 'период замены c ' + l[0] + ' по ' + l[1]
            else:
                c = 'период замены: ' + l[0]
        if p and c:
            self.setStatusTip('Выбран ' + p + ' и ' + c + '.')
        elif p:
            self.setStatusTip('Выбран ' + p + '.')
        elif c:
            self.setStatusTip('Выбран ' + c + '.')
        else:
            self.setStatusTip('Период не выбран')

    def align(self):
        """method aligns table geometry with window """

        self.ui.the_table.setGeometry(10, 60, self.geometry().width() - 20, self.geometry().height() - 90)
        self.ui.the_table.resizeColumnsToContents()
        self.ui.the_table.horizontalHeader().setStretchLastSection(True)
        self.ui.searchButton.setGeometry(10, 10, self.ui.the_table.verticalHeader().sectionSize(0) + 10, 45)
        # the last string is here just because i'm too lazy to find the button size. TODO: find this out

    def change_button_text(self, date=''):
        """changes text on date buttons depending on what period or date is set"""
        from parsers import date_transform
        if date:
            l = list(search_dict[date][1:])
            for i in range(0, len(l)):
                l[i] = date_transform(l[i], '.', 0)
            caption = '\n'.join(l)
            if date == 'P_DATE':
                self.ui.p_dateButton.setText(caption)
            elif date == 'C_DATE':
                self.ui.c_dateButton.setText(caption)
        else:
            self.ui.p_dateButton.setText('Дата\nпокупки')
            self.ui.c_dateButton.setText('Дата\nзамены')

    @staticmethod
    def set_flags(box_value, flag):
        if box_value == 0:
            search_dict[flag] = ''
        elif box_value == 1:
            search_dict[flag] = 'Да'
        else:
            search_dict[flag] = 'Нет'

    def hide_window(self):
        # kinda self-commenting method ;-)
        # but the only thing we need to do here is to keep tray icon's 'show\hide' menu in adorable condition
        self.parent().tray.menu.actions()[0].setChecked(False)
        self.hide()

    def closeEvent(self, event):
        self.hide_window()                              # redefined because we don't need it to actually be closed
        # self.deleteLater()                            # uncomment in case of strange behavior
        event.ignore()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:             # hiding window on a minimize action
            if self.isMinimized():                                      # TODO: look for a better way
                self.hide_window()

    def resizeEvent(self, event):
        self.resize_signal.emit()                           # emitting our shiny brand new signal ;-)


class SysTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):

        QtGui.QSystemTrayIcon.__init__(self, icon, parent)      # init my brand new tray icon

        self.startTimer(1800000)                                # This stands for a half an hour
        self.startTimer(60000)                                  # TODO: left in testing purpose. delete on compile.

        self.menu = QtGui.QMenu(parent)                         # create a menu for tray icon
        self.menu.addAction(QtGui.QAction("Показать / скрыть основное окно", self.menu, checkable=True))

        # insert new menu actions here TODO: new actions.

        self.menu.addAction(QtGui.QAction("Выход", self.menu))
        self.setContextMenu(self.menu)                          # and assign it to the tray icon

        self.connections()                                      # setting new connections

    def timerEvent(self, timer_event=None):
        number_of_clients = len(search_db(init_dict))
        string_one = 'Внимание'
        print(QtCore.QTime.currentTime().toString())            # TODO: left in testing purpose. delete on compile.

        # setting a message box string in accordance with language:
        if number_of_clients < 1:
            return
        elif (str(number_of_clients)[-1] == 1) and (number_of_clients != 11):
            string_two = 'Осталось еще ' + str(number_of_clients) + 'неоповещенный клиент'
        elif ((number_of_clients < 5) or (number_of_clients > 15)) and ((str(number_of_clients)[-1] == 2)
                                                                        or (str(number_of_clients)[-1] == 3)
                                                                        or (str(number_of_clients)[-1] == 4)):
            string_two = 'Осталось еще ' + str(number_of_clients) + 'неоповещенных клиента'
        else:
            string_two = 'Осталось еще ' + str(number_of_clients) + ' неоповещенных клиентов'

        self.showMessage(string_one, string_two, msecs=100000)

    def show_hide(self):
        if self.menu.actions()[0].isChecked():
            if self.parent().main_form.isMinimized():           # TODO: find out how it works
                self.parent().main_form.showNormal()
                self.parent().setFocus()
            else:
                self.parent().main_form.show()
        else:
            self.parent().main_form.hide()

    def connections(self):
        self.connect(self.menu.actions()[-1], QtCore.SIGNAL('triggered()'), self.parent().close_app)
        self.connect(self.menu.actions()[0], QtCore.SIGNAL('triggered()'), self.show_hide)


class MyWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.tray = SysTrayIcon(QtGui.QIcon("./art/tray_icon.png"), self)
        self.tray.show()
        self.main_form = WindowMain(self)                                       # creating main window with table

    def close_app(self):
        self.main_form.hide()                                                   # it doesn't exit if main window
        self.close()                                                            # is on the screen. dunno why.


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    initialize()                                    # setting initial dictionaries, creating db and parsing new txt's
    widget = MyWidget()
    sys.exit(app.exec_())

# TODO: write that delegate QComboBox at last!!!
# TODO: make it work in damn windows
# TODO: icons
#
