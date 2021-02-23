class User:
    def __init__(self, uname, pwd, utype):
        self.uname = uname
        self.pwd = pwd
        self.utype = utype
        # self.id = id

    @property
    def getUname(self):
        return self.uname
    
    @property
    def getPassword(self):
        return self.pwd
    @property
    def getType(self):
        return self.utype
    
    #methods 
    #@uname.setter
    def setUname(self, uname):
        self.uname = uname

    #@pwd.setter
    def setPassword(self, pwd):
        self.pwd = pwd




