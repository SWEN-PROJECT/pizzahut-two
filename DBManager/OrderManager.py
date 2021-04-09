from app import db
from app.models import Order, ItemList, Item, Customer
from datetime import date

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
    
    """
        Method creates a New Order in the Database and Adds the Item in the List to Item List
        paramters: item_list : Collection Of Item Objects, order : Order object
        returns : String if Sucessful, Exception if Unsucessful 
    """
    def insertOrder(self, item_list, order):
        try:
            new_order = Order(date.today(), order.getCID(), order.getTotal(), order.getStatus(), order.getCheckoutType())
            db.session.add(new_order)

            oquery = db.session.query(Order).all()
            if oquery == [] or oquery == None:
                raise Exception("Query returned something empty")
            oquery = oquery[-1]

            for i in item_list:
                temp = ItemList(oquery.order_num, i.getNum(), i.getQty()) 
                db.session.add(temp)  
            db.session.commit()
            return 'Success'
        except Exception as ex:
            print("{}".format(ex))
            return ex

    def getRecentOrder(self, id):
        try:
            oquery =  db.session.query(Order).filter_by(uid=id).all()
            if oquery == [] or oquery == None:
                raise Exception("Query returned something empty")
            oquery = oquery[-1]
            onum = oquery.order_num

            item_qty = db.session.query(ItemList).filter_by(order_num=onum).all()
            if item_qty == [] or item_qty == None:
                raise Exception("Query returned something empty")

            result = []

            for i in item_qty:
                temp = db.session.query(Item).filter_by(item_id=i.item_id).first()
                if temp == [] or temp == None:
                    raise Exception("Query returned something empty")
                result.append({ 'name': temp.item_name, 'qty': i.quantity, 'price': temp.item_price})

            return {'item_list': result, 'order': oquery}
        except Exception as ex:
            print("{}".format(ex))
            return []

    def getAllOrders(self):
        try:
            orders = db.session.query(Order).all()
            if orders == [] or orders == None:
                raise Exception("Query returned something empty")
            
            itemLst = db.session.query(ItemList).all()
            if itemLst == [] or itemLst == None:
                raise Exception("Query returned something empty")
            
            return [orders,itemLst]
        except Exception as ex:
            print("{}".format(ex))
            return []
    
    def getAllOrders(self):
        try:
            orders = db.session.query(Order).filter_by(tag = "Pending").all()
            if orders == [] or orders == None:
                raise Exception("Query returned something empty")
            
            emptylst = [[]] * len(orders)
            ordernumlst = []
            orderlst = []
            
            for order in orders:
                itemlst = []
                ordernum = order.order_num
                ordernumlst.append(ordernum)
                itemLst = db.session.query(ItemList).filter_by(order_num = ordernum).all()
                if itemLst == [] or itemLst == None:
                    raise Exception("Query returned something empty")
                for item in itemLst: 
                    itemobj = db.session.query(Item).filter_by(item_id = item.item_id).all() 
                    currentitem = itemobj[0].item_name                     
                    itemlst.append(currentitem)
                orderlst += [itemlst]
            orderdict = dict(zip(ordernumlst, orderlst))
            return [orders, orderdict]
        except Exception as ex:
            print("{}".format(ex))
            return []
    
    def markOrderComplete(self, ordernum):
        order = db.session.query(Order).filter_by(order_num = ordernum).first()
        order.tag = "Complete"
        db.session.commit()
        return "Order Completed"
    
    def markOrderCancelled(self, ordernum):
        order = db.session.query(Order).filter_by(order_num = ordernum).first()
        order.tag = "Cancelled"
        db.session.commit()
        return "Order Cancelled"
  