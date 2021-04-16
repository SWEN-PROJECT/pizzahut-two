class Order():
    """ The Order Class"""
    def __init__(self, uid = 0):
       self.item_list = []
       self.distinct = []
       self.total = 0
       self.status = 'Pending'
       self.checkoutType = None
       self.cid = uid

    def addItem(self, item):
        if item in self.distinct:
            self.distinct.append(item)
        self.item_list.append(item)

    def getItems(self):
        return self.item_lst

    def getOrder(self):
        return self.item_list

    def getLength(self):
        return len(self.item_list)
    
    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total

    def getStatus(self):
        return self.status
        
    def setStatus(self, stat):
        self.status = stat

    def getCID(self):
        return self.cid

    def getCheckoutType(self):
        return self.checkoutType

    def setCheckoutType(self, ctype):
        if ctype == 'P':
            self.checkoutType = 'Pickup'
        elif ctype == 'D':
            self.checkoutType = 'Delivery'
        else:
            self.checkoutType = 'Undecided'   