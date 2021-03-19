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

class Orders(dict):

    def __init__(self, obj):
        dict.__init__(self, items=obj.item_list, lst=obj.distinct, length=len(obj.item_list))
    
    
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