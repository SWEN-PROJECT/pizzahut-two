class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def getFname(self):
        return self.fname
    
    @property
    def getLname(self):
        return self.lname
    
    #@Fname.setter
    def setFname(self, fname):
        self.fname = fname

    #@Lname.setter
    def setLname(self, lname):
        self.lname = lname




