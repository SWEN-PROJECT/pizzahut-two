class Order():

    def __init__(self):
       self.item_list = []
       self.distinct = []
       self.total = 0

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
        pass

    def getCheckoutType(self):
        pass