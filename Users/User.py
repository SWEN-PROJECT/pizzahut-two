class User:
    def __init__(self, uname, pwd=None, utype=None):
        self.uname = uname
        self.pwd = pwd
        self.utype = utype

    def getUname(self):
        return self.uname
   
    def getPassword(self):
        return self.pwd
  
    def getType(self):
        return self.utype
    
    def setUname(self, uname):
        self.uname = uname

    def setPassword(self, pwd):
        self.pwd = pwd




