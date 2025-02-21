class LengthConverter:
    def __init__(self):
        self.meters = 0
        self.feet = 0
        self.inch = 0
    
    @property
    def meters(self):
        return self.__meters
    
    @property
    def feet(self):
        return self.__feet
    
    @property
    def inch(self):
        return self.__inch
    
    @meters.setter
    def meters(self, value):
        self.__meters = value
        self.__feet = (value * 3.281)
        self.__inch = (value * 39.37)
    
    @feet.setter
    def feet(self, value):
        self.__feet = value
        self.__meters = (value / 3.281)
        self.__inch = (value * 12)
    
    @inch.setter
    def inch(self, value):
        self.__inch = value
        self.__feet = (value / 12)
        self.__meters = (value / 39.37)