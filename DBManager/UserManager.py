from app import db
from app.models import Euser, Customer
from flask import session
from Users import User, Customers
from werkzeug.security import generate_password_hash, check_password_hash

class UserManager():

    def __init__(self):
        pass

    def getModel(self, user):
        try:
            result = db.session.query(Euser).filter_by(u_name=user.getUname()).all()
            if result == []:
                return None
            result = result[0]
            return result
        except:
            return None 

    def queryUser(self, user):
        try:
            result = db.session.query(Euser).filter_by(u_name=user.getUname()).all()
            if result == []:
                return None
            result = result[0]
            return User.User(result.u_name, result.password, result.u_type)
        except:
            return None 
    
    

    def queryCustomer(self, id):
        try:
            result = db.session.query(Customer).filter_by(uid=id).all()
            if result == []:
                return None
            result = result[0]
            return Customers.Customer("","", result.fname, result.lname, result.phone_num, result.street_num, result.street_name, result.town, result.parish, result.email)
        except:
            return None 
    
    
    """
    admin = User.query.filter_by(username='admin').first()
    admin.email = 'my_new_email@example.com'
    db.session.commit()

    user = User.query.get(5)
    user.name = 'New Name'
    db.session.commit()
    """
    def insertUser(self, customer):
            hashedPass = self.encrypt_password(customer.getPassword())
            
            db.session.add(Euser(customer.getUname(), hashedPass, customer.getType()))
            user = db.session.query(Euser).filter_by(u_name=customer.getUname()).all()

            #name
            name = customer.getName()
            fname = name.getFname()
            lname = name.getLname()
            #address
            address = customer.getAddress()
            streetnum = address.getstreetnum()
            streetname = address.getstreetname()
            town = address.gettown()
            parish = address.getparish()
            #contact
            phone = customer.getTeleNum()
            email = customer.getEmail()
            #add to customer db
            db.session.add(Customer(user[0].uid, fname, lname, phone, streetnum, streetname, town, parish, email, 0))
            db.session.commit()

            if user != None:
                return "User added"
            else: 
                return "User Wrong"


    def insertManager(self, manager):
        mname = manager.getUname() 
        user = db.session.query(Euser).filter_by(u_name=mname).all()
        if user == None: 
            hashedPass = self.encrypt_password(manager.getPassword())
            mtype = manager.getType()
            db.session.add(Euser(mname, hashedPass, mtype))
            db.session.commit()
            return "Manager added"
        else: 
            return "Manager Wrong"
    

    def encrypt_password(self, password):
        return generate_password_hash(password, method='pbkdf2:sha256')
    
    def decrypt_password(self, hashed, password):
        return check_password_hash(hashed, password)
    
    def createuser(self, uname, password, utype):
        temp = User.User(uname, password, utype)
        return temp
    
    def createcust(self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        cust = Customers.Customer(uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email)
        return cust
