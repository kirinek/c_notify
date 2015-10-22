__author__ = 'kuroi'
from PyQt4.QtCore import QDate


def to_str(i):
    result = '0'
    if i < 10:
        result += str(i)
    else:
        result = str(i)
    return result


class Days():
    def __init__(self, d=QDate.currentDate(), p=None):
        self.date = d
        self.period = p

    def to_sql(self):
        """returns string date in yyyy-mm-dd format.
        if Days.period is set, returns a string 'BETWEEN YYYY-MM-DD AND YYYY-MM-DD'"""
        s_date = str(self.date.year()) + '-' + to_str(self.date.month()) + '-' + to_str(self.date.day())
        if self.period:
            e_date = str(self.period.year()) + '-' + to_str(self.period.month()) + '-' + to_str(self.period.day())
            return 'BETWEEN ? AND ?', s_date, e_date
        else:
            return '== ?', s_date


class CalendarTemplates():
    def __init__(self):
        self.today = Days()

        self.yesterday = Days(QDate.currentDate().addDays(-1))

        self.tomorrow = Days(QDate.currentDate().addDays(1))

        self.this_week = Days(QDate.currentDate().addDays(-(QDate.currentDate().dayOfWeek() - 1)))
        self.this_week.period = self.this_week.date.addDays(6)

        self.last_week = Days(self.this_week.date.addDays(-7))
        self.last_week.period = self.this_week.period.addDays(-7)

        self.next_week = Days(self.this_week.date.addDays(7))
        self.next_week.period = self.this_week.period.addDays(7)

        self.this_month = Days(QDate.currentDate().addDays(-(self.today.date.day() - 1)))
        self.this_month.period = self.this_month.date.addDays(self.this_month.date.daysInMonth() - 1)

        self.last_month = Days(self.this_month.date.addMonths(-1))
        self.last_month.period = self.last_month.date.addDays(self.last_month.date.daysInMonth() - 1)

        self.next_month = Days(self.this_month.date.addMonths(1))
        self.next_month.period = self.next_month.date.addDays(self.next_month.date.daysInMonth() - 1)