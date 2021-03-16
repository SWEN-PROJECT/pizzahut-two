class Item:
    
    def __init__(self, name, description, itype, price, imagename, num = 0, quan = 0):
        self.num = num
        self.name = name
        self.description = description
        self.itype = itype
        self.price = price
        self.imagename = imagename
        self.quan = quan

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getType(self):
        return self.itype

    def getNum(self):
        return self.num
    
    def getImageName(self):
        return self.imagename

    def getPrice(self):
        return self.price

    def getQty(self):
        return self.quan


    #@Name.setter
    def setName(self, name):
        self.name = name

    #@Type.setter
    def setType(self, itype):
        self.itype = itype

    #@num.setter
    def setnum(self, num):
        self.num = num

    #@Price.setter
    def setPrice(self, price):
        self.price = price
    #@imagename.setter
    def setImagename(self, imagename):
        self.imangname = imangname
    #@Qty.setter
    def setQty(self, quan):
        self.quan = quan




