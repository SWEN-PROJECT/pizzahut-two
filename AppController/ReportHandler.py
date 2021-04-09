from DBManager import ReportManager
from flask import jsonify
from datetime import datetime, date
import calendar

class ReportHandler():
    def __init__(self):
        pass

    def dayReport(self, day, month, year, reptype):
        manager = ReportManager.ReportManager()
        date1 = date(int(year), int(month), int(day))
        itemsdict, price = manager.genRepDay(date1, reptype)
        return itemsdict, price


    def monthReport(self, month, year, reptype):
        month = int(month)
        year = int(year)
        manager = ReportManager.ReportManager()
        num_days = calendar.monthrange(year, month)[1]
        start_date = date(year, month, 1)
        end_date = date(year, month, num_days)
        itemsdict, price = manager.genRepMonth(start_date, end_date, reptype)
        return itemsdict, price

    def yearReport(self,year, reptype):
        year = int(year)
        manager = ReportManager.ReportManager()
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        itemsdict, price = manager.genRepYear(start_date, end_date, reptype)
        return itemsdict, price


