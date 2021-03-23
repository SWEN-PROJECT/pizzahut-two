from MenuManagement import Item, Order 
from DBManager import OrderManager
from flask import session, jsonify

class OrderHandler():

    def __init__(self):
        self.current_order = None
        self.final_order = None

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
            manager = OrderManager.OrderManager()
            m_item_list = manager.buildOrderItems(item_list)
            self.final_order = m_item_list
            return self.jsonifyItems(m_item_list)

    # def confirmed(self):
    #     manager = OrderManager.OrderManager()
    #     m_item_list = manager.buildOrderItems(item_list)
    #     return m_item_list
    #     # manager.insertOrder(m_item_list)
    #     pass
    
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
        item_list = self.normalize(self.current_order.getOrder())
        manager = OrderManager.OrderManager()
        m_item_list = manager.buildOrderItems(item_list)

        for i in m_item_list:
            total += (i.getPrice() * i.getQty())
        return total
    
    def setOrderTotal(self):
        self.current_order.setTotal(self.getOrderTotal())
    
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
        orderman = OrderManager.OrderManager()
        gainedrp = self.calculateRP()
        update = orderman.UpdateRP(customerid, gainedrp)
        if update == "Added":
            return "Y"
        else:
            return "N"
