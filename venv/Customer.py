class Customer():
    def __init__(self,CustomerId ,CustomerName,CustomerLast,CustomerAddress,CustomerCountry):

        self.__CustomerId=CustomerId
        self.__CustomerName=CustomerName
        self.__CustomerLast=CustomerLast
        self.__CustomerAddress=CustomerAddress
        self.__CustomerCountry=CustomerCountry





    @property
    def CustomerId(self):
        return self.__CustomerId

    @CustomerId.setter
    def CustomerId(self, value):
        if(len(value)==9):
           self.__CustomerId=value

    @property
    def CustomerName(self):
        return self.__CustomerName

    @CustomerName.setter
    def CustomerName(self, value):
        self.__CustomerName = value

    @property
    def  CustomerLast(self):
        return self.__CustomerLast

    @CustomerLast.setter
    def  CustomerLast(self, value):
        self.__CustomerLast = value

    @property
    def  CustomerAddress(self):
        return self.__CustomerAddress

    @CustomerAddress.setter
    def  CustomerAddress(self, value):
        self.__CustomerAddress = value


    @property
    def  CustomerCountry(self):
        return self.__CustomerCountry

    @CustomerCountry.setter
    def  CustomerCountry(self, value):
        self.__CustomerCountry = value



    def __str__(self):
        return " id: "+str(self.CustomerId)+" name: "+self.CustomerName+" last: "+self.CustomerLast+" address: "+self.CustomerAddress+" country: "+self.CustomerCountry

