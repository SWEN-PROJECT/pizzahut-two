import User
class Staff(User):
    def __init__(self, uname, pwd):
        User.__init__(self, uname, pwd, 'Staff')
    
    def viewOrder(self):
        return "Needs to be implemented"