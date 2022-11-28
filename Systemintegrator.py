class Systemintegrator:

    def __init__(self, name, alter, jahreErfahrung, firma):
        self.__name = name
        self.__alter = alter
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

    def getJahreErfahrung(self):
        return self.__jahreErfahrung

    def setJahreErfahrung(self, jahreErfahrung):
        self.__jahreErfahrung = jahreErfahrung

    def getFirma(self):
        return self.__firma

    def setFirma(self, firma):
        self.__firma = firma

    def __str__(self) -> str:
        return f'Name: {self.__name}, Alter: {self.__alter}, Jahre Erfahrung: {self.__jahreErfahrung}, Firma: {self.__firma}'

# Testen der Klasse
systemintegratoren = []
sys1 = Systemintegrator('Domagoj Smolcic', 25, 3, 'Bürstner')
sys2 = Systemintegrator('Hans Wolf', 29, 7, 'Kochler')
sys3 = Systemintegrator('Stefan Kupi', 50, 25, 'Telekom')

systemintegratoren.append(sys1)
systemintegratoren.append(sys2)
systemintegratoren.append(sys3)

for systemintegrator in systemintegratoren:
    print(systemintegrator)
