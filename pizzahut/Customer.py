from pizzahut import User, Name, Address

class Customer():
    def __init__(self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        User.__init__(self, uname, pwd, 'C')
        self.name = Name(fname, lname)
        self.address = Address(streetname, streetnum, town, parish)
        self.email = email
        self.telenum = tele

    @property
    def getName(self):
        return self.name
    
    @property
    def getAddress(self):
        return self.address

    @property
    def getTeleNum(self):
        return self.telenum
        
    @property
    def getEmail(self):
        return self.email
    
    #@Name.setter
    def setName(self, name):
        self.name = name

    #@Address.setter
    def setAddress(self, address):
        self.address = address
    
    #@Email.setter
    def setEmail(self, email):
        self.email = email
    
    #@Telenum.setter
    def setTelenum(self, tele):
        self.telenum = tele

    #reward points need to go in 

    #calculate reward points need to go in 