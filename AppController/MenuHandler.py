from DBManager import MenuManager
from MenuManagement import Item

class MenuHandler():
    def __init__(self):
        pass
    
    def addHandle(self,name, price, tag, description, imagename):
        manager = MenuManager.MenuManager()
        result = manager.queryItem(name)
        if result==None:
            item = Item.Item( name, description, tag, price, imagename)
            itemadd = manager.addItem(item)

    
    def itemobjectify(self, lst):
        result = []
        for i in lst:
            result.append(Item.Item(i.item_name, i.item_description, i.item_tag, i.item_price, i.item_img, i.item_id))
        return result
    
    def viewHandle(self):
       manager = MenuManager.MenuManager()
       result = manager.getItems()
       if (result == None) or (result == []):
           return "N"
       else:
            try:
                objects = self.itemobjectify(result)
                return objects
            except:
                return "N"