from MenuManagement.Item import Item

class Order():

    def __init__(self):
       self.item_list = []
       self.distinct = []
       self.length = len(self.item_list)

    def addItem(self, item):
        if item in self.distinct:
            self.distinct.append(item)
        self.item_list.append(item)
        self.length = len(self.item_list)

    def getOrder(self):
        return self.item_list
    
    def getLength(self):
        return int(self.length)
    
    # def getItem(self, num):
    #     for item in self.item_list:
    #         if item.getNum() == num:
    #             return item
    #     return None
    
    # def setQuantity(self, num):
    #     item = self.getItem(num)
    #     # if item == None:
    #     #     self.item_list.append()
    #     item.setQty(item.getQty() + 1)
        
 #write a function that query the item db for the_