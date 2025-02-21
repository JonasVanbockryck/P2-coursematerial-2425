class MusicalNote:
    def __init__(self, name, pitch):
        self.__name = name
        self.__pitch = pitch
    
    @property
    def name(self):
        return self.__name
    
    @property
    def pitch(self):
        return self.__pitch
    
    # @name.setter
    # def name(self, value):
    #     if value != self.__name:
    #         raise ValueError("can't set attribute")
    #     else:
    #         self.__name = value
    
    # @pitch.setter
    # def pitch(self, value):
    #     raise ValueError("can't set attribute")