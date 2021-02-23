class Item:
    def __init__(self, name, itype, num, price, quan):
        self.name = name
        self.itype = itype
        self.num = num
        self.price = price
        self.quan = quan

    @property
    def getName(self):
        return self.name
    
    @property
    def getType(self):
        return self.itype

    @property
    def getNum(self):
        return self.num
    
    @property
    def getPrice(self):
        return self.price

    @property
    def getQty(self):
        return self.quan

    @Name.setter
    def setName(self, name):
        self.name = name

    @Type.setter
    def setType(self, itype):
        self.itype = itype

    @num.setter
    def setnum(self, num):
        self.num = num

    @Price.setter
    def setPrice(self, price):
        self.price = price

    @Qty.setter
    def setQty(self, quan):
        self.quan = quan




