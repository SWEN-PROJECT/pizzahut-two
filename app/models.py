from . import db
from datetime import datetime
from pytz import timezone


""""Thi file contains the database models for User, Customer, Items and Orders""" 
timezone=timezone("EST")

"""Model for the User Table in the Pizza Hut(2) Database"""
class Euser(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(20), unique=True)
    u_type = db.Column(db.String(5))
    password = db.Column(db.String(255))

    def __init__(self,u_name, password, u_type):
        self.u_name = u_name
        self.password = password
        self.u_type = u_type
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.uid)  # python 3 support
    
    def __repr__(self):
        return '<Profile {} {} {} {}>'.format(self.uid, self.u_name, self.password , self.u_type)

"""Model for the Customer Table in the Pizza Hut(2) Database"""
class Customer(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('euser.uid'))
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(50))
    phone_num = db.Column(db.String(14),unique = True)
    street_num = db.Column(db.String(5))
    street_name = db.Column(db.String(20))
    town = db.Column(db.String(40))
    parish = db.Column(db.String(40))
    email = db.Column(db.String(100),unique=True)
    rewards_points = db.Column(db.Integer,default=0)

    def __init__(self,uid, fname, lname, phone_num, street_num, street_name, town, parish, email, rewards_points=0):
        self.uid = uid
        self.fname = fname
        self.lname = lname
        self.phone_num = phone_num
        self.street_name = street_name
        self.street_num = street_num
        self.town = town
        self.parish = parish
        self.email = email
        self.rewards_points = rewards_points

"""Model for the Item Table in the Pizza Hut(2) Database"""
class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(50))
    item_description = db.Column(db.String(255))
    item_tag = db.Column(db.String(20))
    item_price = db.Column(db.Float(precision=2,asdecimal=False))
    item_img = db.Column(db.String(255))

    def __init__(self, item_name, item_description,item_tag,item_price,item_img):
        self.item_name = item_name
        self.item_description = item_description
        self.item_tag = item_tag
        self.item_price = item_price    
        self.item_img = item_img    


"""Model for the Order Table in the Pizza Hut(2) Database"""
class Order(db.Model):

    __tablename__ = "cust_order"

    order_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_create = db.Column(db.DateTime, default = datetime.now(timezone))    
    uid = db.Column(db.Integer, db.ForeignKey('euser.uid'))
    total_price = db.Column(db.Float(precision=2,asdecimal=False))
    tag = db.Column(db.String(10))
    checkout = db.Column(db.String(10))

    def __init__(self,date_create, uid , total_price,tag,checkout):
        self.date_create = date_create
        self.uid = uid
        self.total_price = total_price 
        self.tag = tag
        self.checkout =checkout 


class ItemList(db.Model):
    order_num = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column (db.Integer)
    
    def __init__(self, order_num, item_id , quantity):
        self.order_num = order_num
        self.item_id = item_id 
        self.quantity = quantity 