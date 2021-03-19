from app import db
from app.models import Order, Item_List, Item
from Users import User, Customers

class OrderManager():

    def __init__(self):
        pass

    # def getModel(self, user):
    #     try:
    #         result = db.session.query(Item).all()
    #         if result == []:
    #             return None
    #         result = result[0]
    #         return result
    #     except:
    #         return None 

    # def queryUser(self, user):
    #     try:
    #         result = db.session.query(Order).all()
    #         if result == []:
    #             return None
    #         result = result[0]
    #         return User.User(result.u_name, result.password, result.u_type)
    #     except:
    #         return None 
    
    

    # def queryOrder(self, id):
    #     try:
    #         result = db.session.query(Order).all()
    #         if result == []:
    #             return None
    #         result = result[0]
    #         return Customers.Customers("","", result.fname, result.lname, result.phone_num, result.street_num, result.street_name, result.town, result.parish, result.email)
    #     except Exception as ex:
    #         print("{}".format(ex))
    #         return ex
    
    # def insertOrder(self, order):
    #         order = db.session.query(Order).all()
    #         db.session.add(Order())
    #         db.session.commit()

    #         if user != None:
    #             return "User added"
    #         else: 
    #             return "User Wrong"

    
