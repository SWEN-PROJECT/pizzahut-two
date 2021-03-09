class User:
    def __init__(self, uname, pwd=None, utype=None):
        self.uname = uname
        self.pwd = pwd
        self.utype = utype
        # self.id = id

    def getUname(self):
        return self.uname
   
    def getPassword(self):
        return self.pwd
  
    def getType(self):
        return self.utype
    
    #methods 
    #@uname.setter
    def setUname(self, uname):
        self.uname = uname

    #@pwd.setter
    def setPassword(self, pwd):
        self.pwd = pwd




