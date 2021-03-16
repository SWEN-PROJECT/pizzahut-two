from . import User

class Manager(User.User):
    def __init__(self, uname, pwd):
       super().__init__(uname, pwd, 'M')
    
    def getUname(self):
        return super().getUname()

    def getPassword(self):
        return super().getPassword()

    def getType(self):
        return super().getType()