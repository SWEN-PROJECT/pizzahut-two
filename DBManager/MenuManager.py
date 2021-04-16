from app import db
from app.models import Item, Order

class MenuManager(): 
    
    def __init__(self):
        pass

    """Method to handle the addition of an item into the database
        return : string or None"""
    def addItem(self, item):
        try:
            name = item.getName()
            description = item.getDescription()
            itype = item.getType()
            imagename = item.getImageName()
            price = item.getPrice()

            db.session.add(Item(name, description, itype, price, imagename))
            db.session.commit()
            return "Item Added"
        except Exception as e:
            print("Error: {}".format(e))
            return None
    
    """Method to handle the editing of an item that is already in the database
        return : string, None"""
    def editItem(self, item):
        try:
            itm = db.session.query(Item).filter_by(item_id=item.getNum()).first()
            if itm == [] or itm == None:
                raise Exception("Query returned something empty")
            
            itm.item_name = item.getName()
            itm.item_description = item.getDescription()
            itm.item_tag = item.getType()
            itm.item_price = item.getPrice()
            itm.item_img  = item.getImageName()
            
            db.session.commit()
            return "Item Edited"
        except Exception as e:
            print("Error: {}".format(e))
            return None

    """Method to handle the deletion of an item from the database
        return : string or None"""
    def deleteItem(self, itemid):
        try:
            result = db.session.query(Item).filter_by(item_id=itemid).first()
            if result != None or result == []:
                db.session.delete(result)
                db.session.commit()
                return "Item Deleted"
            else:
                return "Item Not Found"
        except Exception as e:
            print("Error: {}".format(e))
            return None
    
    """Method to get all items that have a specific name
        return : obj or None"""
    def yItem(self, iname):
        try:
            result = db.session.query(Item).filter_by(item_name=iname).all()
            if result == []:
                return None
            result = result[0]
            return result
        except:
            return None 
    
    """Method to get all items from the database
        return : list or None"""
    def getItems(self):
        try:
            result = db.session.query(Item).order_by(Item.item_id).all()
            if result == []:
                return None
            else:
                return result
        except:
            return None
    
    """Method to query a specific itema nd retrieve it from the database
        return : obj or None"""
    def queryItem(self, id=None, name=None):
        try:
            if id == None:
                result = db.session.query(Item).filter_by(item_name=name).first()
            else:
                result = db.session.query(Item).filter_by(item_id=id).first()
            if result == []:
                return None
            else:
                return result
        except:
            return None