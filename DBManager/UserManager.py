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

    """Method to query a given user by username
        return : user obj"""
    def queryUser(self, user):
        try:
            result = db.session.query(Euser).filter_by(u_name=user.getUname()).all()
            if result == []:
                return None
            result = result[0]
            return User.User(result.u_name, result.password, result.u_type)
        except:
            return None 
    
    """Method to query a given customer by id
        return : customer id"""
    def queryCustomer(self, id):
        try:
            result = db.session.query(Customer).filter_by(uid=id).all()
            if result == []:
                return None
            result = result[0]
            return Customers.Customers("","", result.fname, result.lname,result.street_name , result.street_num, result.town, result.parish, result.phone_num ,result.email)
        except Exception as ex:
            print("{}".format(ex))
            return ex
    
    """Method to handle insertion of a user into the database
        return :string"""
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

    """
    Method to handle updating a user
        parameters : uid : int , customer : Customer Object
        return : 
    """
    def updateUser(self, uid, customer):
        try:
            user = db.session.query(Euser).get(uid)
            result = db.session.query(Customer).filter_by(uid=uid).first()
            if result == [] or result == None:
                raise Exception("Query returned something empty")
            elif user == [] or result == None:
                raise Exception("Query returned something empty")
            
            # Update User Information associated with Customer 
            user.u_name = customer.getUname()
            if customer.getPassword() != "":
                user.password = self.encrypt_password(customer.getPassword())

            # Update Customer Information
            result.fname = customer.getName().getFname()
            result.lname = customer.getName().getLname()
            result.street_name = customer.getAddress().getstreetname()
            result.street_num = customer.getAddress().getstreetnum()
            result.town = customer.getAddress().gettown()
            result.parish = customer.getAddress().getparish()
            result.email = customer.getEmail()
            result.phone_num = customer.getTeleNum()
            
            db.session.commit()

            return 'A'
        except Exception as ex:
            print("{}".format(ex))
            return ex

    """Method to insert an new manager into the database
        HELPER (in)
        return : string"""
    def insertManager(self, manager):
            mname = manager.getUname() 
            hashedPass = self.encrypt_password(manager.getPassword())
            mtype = manager.getType()
            print("Manager")
            db.session.add(Euser(mname, hashedPass, mtype))
            db.session.commit()
            return "Manager added"
        
    
    """Method to insert a new staff into the database
        return : string"""
    def insertStaff(self, staff):
        try:
            sname = staff.getUname() 
            hashedPass = self.encrypt_password(staff.getPassword())
            stype = staff.getType()
            db.session.add(Euser(sname, hashedPass, stype))
            db.session.commit()
            return "Staff added"
        except Exception as e:
            print("Error: {}".format(e))
            return None

    def encrypt_password(self, password):
        return generate_password_hash(password, method='pbkdf2:sha256')
    
    def decrypt_password(self, hashed, password):
        return check_password_hash(hashed, password)
    
    def createuser(self, uname, password, utype):
        temp = User.User(uname, password, utype)
        return temp
    
    def createcust(self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        cust = Customers.Customers(uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email)
        return cust

    """Method to get the rewards points for a specific customer in the database
        return : int or None"""
    def getRP(self, id):
        try:
            result = db.session.query(Customer).filter_by(uid=id).first()
            if result == []:
                return None 
            else:
                return result.rewards_points

        except Exception as e:
            print("Error: {}".format(e))
            return None

    """Method to update the rewards points for a specific customer in the database
        return : string or None"""
    def updateRP(self, id, gained):
        try:
            result = db.session.query(Customer).filter_by(uid=id).first()
            rp = result.rewards_points + gained
            result.rewards_points = rp
            db.session.merge(result)
            db.session.commit()
            return "Points Added"
        except Exception as e:
            print("Error: {}".format(e))
            return None
    
    """Method to use/deduct the rewards points for a specific customer in the database
        return : string or None"""
    def useRP(self, id, points):
        try:
            result = db.session.query(Customer).filter_by(uid=id).first()
            result.rewards_points = points
            db.session.merge(result)
            db.session.commit()
            return "Points Used"
        except Exception as e:
            print("Error: {}".format(e))
            return None
