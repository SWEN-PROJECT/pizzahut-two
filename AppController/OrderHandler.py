from MenuManagement import Item, Order 
from DBManager import OrderManager
from flask import session

class OrderHandler():

    def __init__(self):
        self.current_order = None

    def addToOrder(self, itemid):
        # session.pop('currentOrder', None)
        if self.current_order ==  None:
            self.current_order = Order.Order()
            self.current_order.addItem(itemid)
        else:
            self.current_order.addItem(itemid)
        # print(self.current_order.item_list)
        return self.current_order.getLength()

    def checkout(self):
        if self.current_order == None:
            return 'NOWM'
        else:
            self.current_order = None
            return 'CHCK'