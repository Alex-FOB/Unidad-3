class agente:
    __cuil = None
    __ape = None
    __nom = None
    __sueldo = None #sueldo básico
    __antiguedad = None
    __sueldoAgente = 0 #AÑADIDO: es el sueldo a pagar
    def __init__(self, cuil, ape, nom, sueldo, antiguedad, area = '', tipo = '', carrera = '', cargo = '', catedra = '', categoria = '', importeExtra = 0):
        try:
            self.__cuil = str(cuil)
            self.__ape = str(ape).capitalize()
            self.__nom = str(nom).capitalize()
            self.__sueldo = float(sueldo)
            self.__antiguedad = int(antiguedad)
            self.__sueldoAgente = 0
        except ValueError:
            self.__cuil = 'unknown'
            self.__ape = 'unknown'
            self.__nom = 'unknown'
            self.__sueldo = 0
            self.__antiguedad = 0
            self.__sueldoAgente = 0
    def __str__(self):
        return '{} - {} {} - ${} Antiguedad: {}'.format(self.__cuil, self.__ape, self.__nom, self.__sueldo, self.__antiguedad)
    def __lt__(self, other):
        return self.__ape < other.getApe()
    def setSueldo(self, sueldo):
        self.__sueldoAgente = sueldo
    def getCuil(self):
        return self.__cuil
    def getApe(self):
        return self.__ape
    def getNom(self):
        return self.__nom
    def getSueldo(self):
        return self.__sueldo
    def getAntiguedad(self):
        return self.__antiguedad
    def getSueldoAgente(self):
        return self.__sueldoAgente