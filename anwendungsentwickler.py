class Anwendungsentwickler:
    def __init__(self, name, alter, lieblingsSprache, jahreErfahrung, firma):
        self.__name = name
        self.__alter = alter
        self.__lieblingsSprache = lieblingsSprache
        self.__jahreErfahrung = jahreErfahrung
        self.__firma = firma

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getAlter(self):
        return self.__alter

    def setAlter(self, alter):
        self.__alter = alter

    def getLieblingsSprache(self):
        return self.__lieblingsSprache

    def setLieblingsSprache(self, lieblingsSprache):
        self.__lieblingsSprache = lieblingsSprache

    def getJahreErfahrung(self):
        return self.__jahreErfahrung

    def setJahreErfahrung(self, jahreErfahrung):
        self.__jahreErfahrung = jahreErfahrung

    def getFirma(self):
        return self.__firma

    def setFirma(self, firma):
        self.__firma = firma