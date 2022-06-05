class jugador:
    __nom = None #nombre del jugardor
    __dni = None #dni del jugador
    __cuidad = None #ciudad natal del jugador
    __pais = None #pais de origen del jugador
    __fecha = None #fecha de nacimiento del jugador
    __contrato = None #AÑADIDO sirve para contener una refencia del contrato
    def __init__(self, nom = '', dni = '', cuidad = '', pais = '', fecha = ''):
        self.__nom = str(nom)
        self.__dni = str(dni)
        self.__cuidad = str(cuidad)
        self.__pais = str(pais)
        self.__fecha = str(fecha)
    def __str__(self):
        return '{}\nDNI: {:8} Cuidad/Pais Natal: {}/{}\nFecha de nacimiento: {}'.format(self.__nom, self.__dni, self.__cuidad, self.__pais, self.__fecha)
    def getNom(self):
        return self.__nom
    def getContrato(self):
        return self.__contrato
    def getDNI(self):
        return self.__dni
    def setContrato(self, contrato):
        self.__contrato = contrato