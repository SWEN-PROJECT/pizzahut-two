from flask_wtf import form
from app import app, login_manager
from flask import flash
from DBManager import UserManager
from Users import Customers, User, Staff
from flask_login import login_user, current_user


"""Class to handle all UI interactions"""

class LSHandler():

    def __init__(self):
        pass
    
    """Method to handle the login of a user
    parameters : username, pasword
    return : char"""
    def loginHandle(self,uname,pwd):
        manager = UserManager.UserManager()
        temp = User.User(uname)
        result = manager.queryUser(temp)
        if (result == None):
            return "N"
        elif (manager.decrypt_password(result.getPassword(),pwd)):
            result = manager.getModel(temp)
            login_user(result)
            return "Y"
        else:
            return "C"
    
    """Method to handle the signup of a user
        parameters : (self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email
        return : char"""
    def signupHandle(self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        manager = UserManager.UserManager()
        temp = User.User(uname)
        result = manager.queryUser(temp)
        if (result == None):
            customer = Customers.Customers(uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email)
            message = manager.insertUser(customer)
            if message == "User added":
                return "S"
            else:
                return "F"
        else:
            return "T"

    """Method to handle the signup of a user
        return : char"""
    def loadCustomer(self):
        manager = UserManager.UserManager()
        result = manager.queryCustomer(current_user.uid)
        if (result == None):
            return "N"
        else:
            result.setUname(current_user.u_name)
            return result

    """Method to handle updates to a specified users information
        return : char"""
    def updateHandle(self, uname, npwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        manager = UserManager.UserManager()
        customer = manager.createcust(uname, npwd, fname, lname, streetname, streetnum, town, parish, tele, email)
        message = manager.updateUser(current_user.uid, customer)
        if message == "A":
            return "S"
        else:
            return "F"
    
    """Method to handle the adding of staff members by the manager
        return : char"""
    def staffHandle(self, uname, pwd):
        manager = UserManager.UserManager()
        temp = User.User(uname)
        result = manager.queryUser(temp)
        if (result == None):
            staff = Staff.Staff(uname, pwd)
            message = manager.insertStaff(staff)
            if message == "Staff added":
                return "S"
            else:
                return "F"
        else:
            return "T"
    
    def getRewards(self,id):
        manager = UserManager.UserManager()
        points = manager.getRP(id)
        return points