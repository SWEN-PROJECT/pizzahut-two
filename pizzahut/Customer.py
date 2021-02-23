from pizzahut import User, Address, Name

class Customer(User.User):
    def __init__(self, uname, pwd, fname, lname, streetname, streetnum, town, parish, tele, email):
        super().__init__(self,uname, pwd, 'C')
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