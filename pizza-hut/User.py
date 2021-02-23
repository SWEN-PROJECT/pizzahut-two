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
    
    # @property
    # def getId(self):
    #     return self.id

    
    @username.setter
    def setUname(self, uname):
        self.uname = uname

    @password.setter
    def setPassword(self, pwd):
        self.pwd = pwd




