from MenuManagement import Item, Order 
from DBManager import OrderManager
from flask import session, jsonify
from flask_login import current_user

class OrderHandler():

    def __init__(self):
        self.current_order = None
        self.final_order = None
        self.manager = OrderManager.OrderManager()

    def addToOrder(self, itemid):
        if self.current_order ==  None:
            self.current_order = Order.Order()
            self.current_order.addItem(itemid)
        else:
            self.current_order.addItem(itemid)
        return self.current_order.getLength()

    def checkout(self):
        if self.current_order == None:
            return jsonify({ 'list': 'NOWM'})
        else:
            item_list = self.normalize(self.current_order.getOrder())
            m_item_list = self.manager.buildOrderItems(item_list)
            self.final_order = m_item_list
            return self.jsonifyItems(m_item_list)

    def confirm(self, type):
        self.current_order.setCheckoutType(type)
        self.current_order.setTotal(self.getOrderTotal())
        result = self.manager.insertOrder(self.final_order, self.current_order)
        if result == 'Success':
            return 'OK'
        else:
            return 'NOK'

    def normalize(self, lst):
        seen = []
        result = []
        for i in lst:
            if i not in seen:
                quantity = lst.count(i)
                result.append(Item.Item('', '', '', '','', i, quantity))
                seen.append(i)
        return result

    def jsonifyItems(self, items):
        result = { 'list': [] }
        for i in items:
            body = {
                'name': i.getName(), \
                    'qty': str(i.getQty()), \
                        'price': str(i.getPrice()), \
                            'key' : str(i.getNum())
            }
            result['list'].append(body)
        return jsonify(result)

    # Order total functions 
    def getOrderTotal(self):
        total = 0
        for i in self.final_order:
            total += (i.getPrice() * i.getQty())
        return total
    
    def calculateRP(self):
        total = getOrderTotal()
        gained = 0
        if total >= 1500 and total <= 2999: gained = 75
        elif total >= 3000 and total <= 4999: gained = 150
        elif total >= 5000 and total <= 9999: gained = 250
        elif total >= 10000: gained = 500
        else: gained = 0
        return gained

    def updateRP(self):
        customerid = current_user.uid
        gainedrp = self.calculateRP()
        update = self.manager.updateRP(customerid, gainedrp)
        if update == "Added":
            return "Y"
        else:
            return "N"
