from DBManager import MenuManager
from MenuManagement import Item
from flask import jsonify

class MenuHandler():
    def __init__(self):
        pass
    
    """Method to handle the addition of items to the Menu
        return : char"""
    def addHandle(self,name, price, tag, description, imagename):
        manager = MenuManager.MenuManager()
        result = manager.queryItem(name=name)
        if result==None:
            item = Item.Item( name, description, tag, price, imagename)
            itemadd = manager.addItem(item)
            if itemadd == "Item Added":
                return "S"
            else:
                return "F"
        else:
            return "C"

    """Method to handle the editing of items that would have already been in the menu
        return : char"""
    def editHandle(self,itemid, name, price, tag, description, imagename):
        manager = MenuManager.MenuManager()
        result = manager.queryItem(id=itemid)
        if result != None:
            item = Item.Item(name, description, tag, price, imagename, num=result.item_id)
            itemadd = manager.editItem(item)
            if itemadd == "Item Edited":
                return "S"
            else:
                return "F"
        else:
            return "C"

    """HELPER
        Method to turn item information entered by the user into an item object
        return : lst of item objects"""
    def itemobjectify(self, lst):
        result = []
        for i in lst:           
            result.append(Item.Item(i.item_name, i.item_description, i.item_tag, i.item_price, i.item_img, i.item_id))
        return result
    
    """Method that handles the getting of all or all specified items being requested
        return if !NONE : lst of item objs, else return : char"""
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
    
    """Method that handles the deletion of a specified item 
        return : char"""
    def deleteHandle(self, itemid):
        manager = MenuManager.MenuManager()
        result = manager.deleteItem(itemid)
        if (result == "Item Deleted") :
            print("s")
            return "OK"
        else:
            print("f")
            return "NOK"
    
    def retrieveHandle(self, itemid):
        manager = MenuManager.MenuManager()
        result = manager.queryItem(itemid)
        if result == None:
            return jsonify({ 'result': 'NOK' })
        else:
            return self.jsonifyItems([result])

    def jsonifyItems(self, items):
        result = { 'result': [] }
        for i in items:
            body = {
                'name': i.item_name, \
                    'desc': i.item_description, \
                        'price':  i.item_price, \
                            'key' :  i.item_id, \
                                'tag': i.item_tag
            }
            result['result'].append(body)
        return jsonify(result)

