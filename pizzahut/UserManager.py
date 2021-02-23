from app import db
from app.models import User, Customer
import hashlib

class UserManager():

    def __init__(self):
        pass
    
    def queryUser(self, user):
        try:
            user = db.session.query(User).filter_by(u_name=user.getUname()).all()
            return user
        except:
            return None 
    
    def insertUser(self, customer):
        try: 
            #passwordhash 
            hashedPass = 'hello' #customer.getPassword() #encrypt_password(customer.getPassword())
            
            db.session.add(User(customer.getUname(), hashedPass, customer.getType()))
            user = db.session.query(User).filter_by(u_name=customer.getUname()).all()

            #name
            name = customer.getName()
            fname = name.getFname
            lname = name.getLname
            #address
            address = customer.getAddress
            streetnum = address.getstreetnumum()
            streetname = address.getstreetname()
            town = address.gettown()
            parish = address.getparish()
            #contact
            phone = customer.getTeleNum()
            email = customer.getEmail()
            #add to customer db
            # db.session.add(Customer(user.uid, fname, lname, phone, streetnum, streetname, town, parish, email))
            # db.session.commit()
            if user != None:
                return "User added"
            else: 
                return "User Wrong"
        except:
            return "User not added"


    def encrypt_password(self, password):
        return hashlib.md5(password.encode())
    
    def decrypt_password(self, hashed):
        return hashed.hexdigest()