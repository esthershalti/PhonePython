class Line():
    def __init__(self,CustomerCode,RouteCode,Phone):
        self.__LineCode=LineCode
        self.__CustomerCode=CustomerCode
        self.__RouteCode=RouteCode
        self.__Phone=Phone

    @property
    def CustomerCode(self):
        return self.__CustomerCode

    @CustomerCode.setter
    def CustomerCode(self, value):
           self.__CustomerCode=value

    @property
    def RouteCode(self):
        return self.__RouteCode

    @RouteCode.setter
    def RouteCode(self, value):
        self.__RouteCode = value

    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, value):
        self.__Phone = value

    def __str__(self):
        return " CustomerCode: " + str(self.CustomerCode) + " RouteCode: " + str(
            self.RouteCode) + " Phone: " + self.Phone