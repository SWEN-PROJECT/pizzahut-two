class Address:
    def __init__(self, streetname, streetnum, town, parish):
        self.streetname = streetname
        self.streetnum = streetnum
        self.town = town
        self.parish = parish

   
    def getstreetname(self):
        return self.streetname
    
   
    def getstreetnum(self):
        return self.streetnum
    
   
    def getparish(self):
        return self.parish
    
   
    def gettown(self):
        return self.town
    
    def setstreetname(self, streetname):
        self.streetname = streetname

    def setstreetnum(self, streetnum):
        self.streetnum = streetnum

    def settown(self, town):
        self.town = town
    

    def setparish(self, parish):
        self.parish = parish



