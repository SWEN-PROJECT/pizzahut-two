from MenuManagement import Item, Order 
from DBManager import OrderManager
from flask import session

class OrderHandler():

    def __init__(self):
        self.current_order = None

    def addToOrder(self, itemid):
        if self.current_order ==  None:
            self.current_order = Order.Order()
            self.current_order.addItem(itemid)
        else:
            self.current_order.addItem(itemid)
        return self.current_order.getLength()

    def checkout(self):
        if self.current_order == None:
            return 'NOWM'
        else:
            # item_list = self.normalize(self.current_order.getOrder())
            # manager = OrderManager.OrderManager()
            # manager.insertOrder(item_list)
            self.current_order = None
            return 'CHCK'
    
    # def normalize(self, lst):
    #     seen = []
    #     result = []
    #     for i in lst:
    #         if i not in seen:
    #             quantity = lst.count(i)
    #             result.append(Item.Item('', '', '', '','', i, quantity))
    #     return result
