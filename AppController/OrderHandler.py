from MenuManagement import Item, Order 
from DBManager import OrderManager
from flask import session
import json 

class OrderHandler():

    def __init__(self):
        pass

    def addToOrder(self, itemid):
        if 'currentOrder' not in session:
            session['currentOrder'] = Order.Order()
            session['currentOrder'].addItem(itemid)
        else:
            session['currentOrder'].addItem(itemid)
        length = list([session['currentOrder'].getLength(), 0])
        return length[0]

    # def checkoutOrder(self):
    #     order = session['currentOrder'].getOrder()
    #     return order