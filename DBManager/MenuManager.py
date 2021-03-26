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