from app import db
from app.models import Item, Order

class MenuManager(): 
    
    def __init__(self):
        pass

    def addItem(self, item):
        print('Hello There2')
        try:
            #extracting item data
            name = item.getName()
            description = item.getDescription()
            itype = item.getType()
            imagename = item.getImageName()
            price = item.getPrice()

            print('Hello There')
            db.session.add(Item(name, description, itype, price, imagename))
            print('I am here')
            db.session.commit()
            return "Item Added"
        except Exception as e:
            print("Error: {}".format(e))
            return None
    
    def editItem(self, item):
        try:
            #Get Item 
            itm = db.session.query(Item).filter_by(item_id=item.getNum()).first()
            if itm == [] or itm == None:
                raise Exception("Query returned something empty")
            
            #extracting item data
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

    def deleteItem(self, itemid):
        try:
            #extracting item data
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
  
    def yItem(self, iname):
        try:
            result = db.session.query(Item).filter_by(item_name=iname).all()
            if result == []:
                return None
            result = result[0]
            return result
        except:
            return None 
    
    def getItems(self):
        try:
            result = db.session.query(Item).all()
            if result == []:
                return None
            else:
                return result
        except:
            return None
    
    def queryItem(self, item):
        try:
            result = db.session.query(Item).filter_by(item_name=item.getName()).first()
            if result == []:
                return None
            else:
                return result
        except:
            return None