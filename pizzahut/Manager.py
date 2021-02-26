import User
class Manager(User.User):
    def __init__(self, uname, pwd):
        User.__init__(self, uname, pwd, 'M')
    
    def getMenu(self):
        return "Needs to be implemented"