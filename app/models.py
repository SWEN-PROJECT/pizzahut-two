from . import db
from datetime import datetime
from pytz import timezone

""""Thi file contains the database models for User, Customer, Items and Orders""" 
timezone=timezone("EST")

"""Model for the User Table in the Pizza Hut(2) Database"""
class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(20), unique=True)
    u_type = db.Column(db.String(5))
    password = db.Column(db.String(255))

    def __init__(self,u_name, password, u_type):
        self.u_name = u_name
        self.email = email
        self.password = password
        self.u_type = u_type


"""Model for the Customer Table in the Pizza Hut(2) Database"""
class Customer(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(50))
    phone_num = db.Column(db.String(14),unique = True)
    street_num = db.Column(db.String(5))
    street_name = db.Column(db.String(20))
    town = db.Column(db.String(40))
    parish = db.Column(db.String(40))
    email = db.Column(db.String(100),unique=True)
    rewards_points = db.Column(db.Integer,default=0)

    def __init__(self,fname, lname, phone_num, street_num, street_name, town, parish, email, rewards_points):
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

    def __init__(self, item_id, item_name, item_description,item_tag,item_price):
        self.item_name = item_name
        self.item_description = item_description
        self.item_tag = item_tag
        self.item_price = item_price        


"""Model for the Order Table in the Pizza Hut(2) Database"""
class Order(db.Model):
    order_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_create = db.Column(db.DateTime, default = datetime.now(timezone))    
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    item_list = db.Column(db.String(250))
    total_price = db.Column(db.Float(precision=2,asdecimal=False))
    tag = db.Column(db.String(10))
    checkout = db.Column(db.String(10))

    def __init__(self,date_create, uid,item_list,total_price,tag,checkout):
        self.date_create = date_create
        self.item_list = item_list 
        self.total_price = total_price 
        self.tag = tag
        self.checkout =checkout 
