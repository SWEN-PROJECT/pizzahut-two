from app import db
from app.models import Order, ItemList, Item, Customer
from sqlalchemy import extract
from datetime import date
from datetime import datetime
import calendar

class ReportManager():

    def __init__(self):
        pass
    
    """
        Method creates a query and runs it in order to find all orders on a specific day in a specific year
        paramters: date, reptype
        returns : total price and dictionary of results
    """
    def genRepDay(self, date, reptype):
        totprice = 0
        results = db.session.query(Order).filter(Order.date_create == date, Order.tag==reptype).all() 
        price, itemsdict = self.gettotalprice(results)
        return itemsdict, price
    
    """
        Method creates a query and runs it in order to find all orders in a specific month in a specific year
        paramters: date1, date2, reptype
        returns : total price and dictionary of items
    """
    def genRepMonth(self, date1, date2, reptype): 
        results = db.session.query(Order).filter(Order.date_create.between(date1,date2), Order.tag==reptype).all() 
        price, itemsdict = self.gettotalprice(results)
        return itemsdict, price

    """
        Method creates a query and runs it in order to find all orders in a specific year
        paramters: date1, date2, reptype
        returns : total price and dictionary of items
    """
    def genRepYear(self, date1, date2, reptype):
        results = db.session.query(Order).filter(Order.date_create.between(date1,date2), Order.tag==reptype).all() 
        price, itemsdict = self.gettotalprice(results)
        return itemsdict, price
    

    """
        Method creates a query and runs it in order to calculate the total price
        paramters: results 
        returns : total price and dictionary of items 
    """
    def gettotalprice(self, results):
        totprice = 0
        itemsdict = {}
        for order in results:
            totprice += order.total_price
            itemlst = []
            ordernum = order.order_num
            itemLst = db.session.query(ItemList).filter_by(order_num = ordernum).all()
            if itemLst == [] or itemLst == None:
                raise Exception("Query returned something empty")
            for item in itemLst: 
                itemobj = db.session.query(Item).filter_by(item_id = item.item_id).all() 
                currentitem = itemobj[0].item_name 
                if currentitem not in itemsdict:
                    itemsdict[currentitem] = item.quantity 
                else:
                    itemsdict[currentitem] += item.quantity 
        return totprice, itemsdict