class Order():

    def __init__(self):
       self.item_list = []
       self.distinct = []

    def addItem(self, item):
        if item in self.distinct:
            self.distinct.append(item)
        self.item_list.append(item)

    def getOrder(self):
        return self.item_list

    def getLength(self):
        return len(self.item_list)
    
    def getTotal():
        pass

    def getStatus():
        pass

    def getCheckoutType():
        pass