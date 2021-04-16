from UserInformation import Name, Address
from . import User

"""Class to get and set all Customer data."""

class Customers(User.User):
    def __init__(self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        super().__init__(uname, pwd, 'C')
        self.name = Name.Name(fname, lname)
        self.address = Address.Address(streetname, streetnum, town, parish)
        self.email = email
        self.telenum = tele

    def getUname(self):
        return super().getUname()

    def getPassword(self):
        return super().getPassword()

    def getType(self):
        return super().getType()

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

    def getTeleNum(self):
        return self.telenum
        
    def getEmail(self):
        return self.email
    
    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address
    
    def setEmail(self, email):
        self.email = email
    
    def setTelenum(self, tele):
        self.telenum = tele