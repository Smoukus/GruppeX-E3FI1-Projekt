class Systemintegrator:

    def __init__(self, name, alter, jahreErfahrung):
        self.__name = name
        self.__alter = alter
        self.__jahreErfahrung = jahreErfahrung

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def getAlter(self):
        return self.__alter

    def setAlter(self, alter):
        self.__alter = alter

    def getJahreErfahrung(self):
        return self.__jahreErfahrung

    def setJahreErfahrung(self, jahreErfahrung):
        self.__jahreErfahrung = jahreErfahrung

    def __str__(self) -> str:
        return f"Name: {self.__name}, Alter: {self.__alter}, Jahre Erfahrung: {self.__jahreErfahrung}"