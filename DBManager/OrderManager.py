from app import db
from app.models import Order, Item_List, Item, Customer

class OrderManager():

    def __init__(self):
        pass


    """
        Method queries the Database for Information for specific Items contained in the Item List
        paramters: item_list : Collection Of Item Objects
        returns : item_list : Modified Versio of the Collection of Item Objects 
    """
    def buildOrderItems(self, item_list):
        try:
            for i in item_list:
                query = db.session.query(Item).get(i.getNum())
                if query == [] or query == None:
                    pass
                else:
                    i.setPrice(query.item_price)
                    i.setDescription(query.item_description)
                    i.setType(query.item_tag)
                    i.setName(query.item_name)
                    i.setImagename(query.item_img)
                    i.setType(query.item_tag)
            return item_list
        except Exception as ex:
            print("{}".format(ex))
            return ex
    
    # """
    #     Method creates a New Order in the Database and Adds the Item in the List to Item List
    #     paramters: item_list : Collection Of Item Objects, order : Order object
    #     returns : String if Sucessful, Exception if Unsucessful 
    # """
    def insertOrder(self, item_list, order):
        try:
            new_order = Order('Date Created', order.getTotal(), order.getStatus(), order.getCheckoutType())
            db.session.add(new_order)

            oquery = db.session.query(Order).all()
            if oquery == [] or oquery == None:
                raise Exception("Query returned something empty")
            oquery = oquery[-1]

            for i in item_list:
                temp = Item_List(oquery.order_num, i.getNum(), i.getQty())   

            db.session.commit()
            return 'Success'
        except Exception as ex:
            print("{}".format(ex))
            return ex

    def updateRP(self, customerID, gainedrp):
        try:
           result = db.session.query(Customer).filter_by(uid=customerID).first()
           rp = result.rewards_points + gainedrp
           result.rewards_points = rp
           db.session.commit()
           return "Added"
        except Exception as ex:
            print("{}".format(ex))
            return ex