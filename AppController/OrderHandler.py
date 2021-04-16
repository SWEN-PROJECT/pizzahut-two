from MenuManagement import Item, Order 
from DBManager import OrderManager, UserManager
from flask import session, jsonify
from flask_login import current_user

class OrderHandler():

    def __init__(self):
        self.current_order = None
        self.final_order = None
        self.manager = OrderManager.OrderManager()

    """Method to handle the addition of items to a customer's order
        return : int"""
    def addToOrder(self, itemid):
        if self.current_order ==  None:
            self.current_order = Order.Order(current_user.uid)
            self.current_order.addItem(itemid)
        else:
            self.current_order.addItem(itemid)
        return self.current_order.getLength()

    """Method to handle the checkout of a customer after the have finished adding items
        return : "jsonified" list"""
    def checkout(self):
        if self.current_order == None:
            return jsonify({ 'list': 'NOWM'})
        else:
            item_list = self.normalize(self.current_order.getOrder())
            m_item_list = self.manager.buildOrderItems(item_list)
            self.final_order = m_item_list
            return self.jsonifyItems(m_item_list)

    """Method to handle the confirmation of a users order and
        calculations regarding rewards points.
        return : string"""
    def confirm(self, type, points):
        self.current_order.setCheckoutType(type)
        if points == "U":
            rp = self.getPoints()
            if rp == 0:
                self.current_order.setTotal(self.getOrderTotal())
                pointsleft = 0
            elif rp > self.getOrderTotal():
                self.current_order.setTotal(0)
                pointsleft = rp - self.getOrderTotal()
            else:
                self.current_order.setTotal(self.getOrderTotal() - rp )
                pointsleft = 0

            if pointsleft > 0:
                self.usePoints(pointsleft)
            else: 
                self.usePoints(0)
        else:
            self.current_order.setTotal(self.getOrderTotal())
        result = self.manager.insertOrder(self.final_order, self.current_order)
        self.updatePoints()
        if result == 'Success':
            self.final_order = None
            self.current_order = None
            return 'OK'
        else:
            return 'NOK'

    """HELPER"""
    def normalize(self, lst):
        seen = []
        result = []
        for i in lst:
            if i not in seen:
                quantity = lst.count(i)
                result.append(Item.Item('', '', '', '','', i, quantity))
                seen.append(i)
        return result

    """HELPER"""
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

    """Method to calculate the order total of a given order
        return : int"""
    def getOrderTotal(self):
        total = 0
        for i in self.final_order:
            total += (i.getPrice() * i.getQty())
        return total
    
    """Method to calculate the amount of rewards points a customer may gain having
            spent a specific amount of money.
        return : int"""
    def calculateRP(self):
        total = self.getOrderTotal()
        gained = 0
        if total >= 1500 and total <= 2999: gained = 75
        elif total >= 3000 and total <= 4999: gained = 150
        elif total >= 5000 and total <= 9999: gained = 250
        elif total >= 10000: gained = 500
        else: gained = 0
        return gained

    """Method to update the rewards points for a customer
        return : -"""
    def updatePoints(self):
        customerid = current_user.uid
        gainedrp = self.calculateRP()
        mymanager = UserManager.UserManager()
        update = mymanager.updateRP(customerid, gainedrp)

    """Method to retrieve the rewards points of a given customer
        return : int"""
    def getPoints(self):
        customerid = current_user.uid
        mymanager = UserManager.UserManager()
        rp = mymanager.getRP(customerid)
        return rp

    """Method to handle the usage/deduction of rewards points form a customer's account
        return : -"""
    def usePoints(self, points):
        customerid = current_user.uid
        mymanager = UserManager.UserManager()
        update = mymanager.useRP(customerid, points)    


    def completion(self):
        result = self.manager.getRecentOrder(current_user.uid)
        if result != []:    
            order = self.buildOrder(result['order'])
            items = []
            for i in result['item_list']:
                items.append(Item.Item(i.get('name'), '', '', i.get('price'), '', quan=i.get('qty')))
            return (order, items)
        else:
            return None

    """Method to handle the creation of an order based on user input
        return : order object"""
    def buildOrder(self, order):
        obj = Order.Order(current_user.uid)
        obj.setTotal(order.total_price)
        obj.setCheckoutType(order.checkout)
        obj.setStatus(order.tag)
        return  obj

    """Method to handle the display of all order to a staff viewer
        return : list"""
    def assembleAll(self):
        try:
            result = self.manager.getAllOrders()
            orders = result[0] 
            orderdict = result[1] 
            return [orders, orderdict]
        except:
            return []
        
    """Method to handle marking an order complete
        return : string"""
    def markComplete(self, ordernum):
        result = self.manager.markOrderComplete(ordernum)
        return result
    """Method to handle marking an orer cancelled
        return : string"""
    def markCancelled(self, ordernum):
        result = self.manager.markOrderCancelled(ordernum)
        return result