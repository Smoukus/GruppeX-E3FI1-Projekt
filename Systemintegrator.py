class Systemintegrator:

    def __init__(self, name, alter, jahreErfahrung):
        self.name = name
        self.alter = alter
        self.jahreErfahrung = jahreErfahrung

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def getAlter(self):
        return self.alter

    def setAlter(self, alter):
        self.alter = alter

    def getJahreErfahrung(self):
        return self.jahreErfahrung

    def setJahreErfahrung(self, jahreErfahrung):
        self.jahreErfahrung = jahreErfahrung

    def __str__(self) -> str:
        return f"Name: {self.name}, Alter: {self.alter}, Jahre Erfahrung: {self.getJahreErfahrung}"

