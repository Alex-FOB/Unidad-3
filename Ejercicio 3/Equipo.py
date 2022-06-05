class equipo:
    __nom = None #nombre del equipo
    __ciudad = None #ciudad del equipo
    __contratos = None #añadido
    def __init__(self, nom = '', cuidad = ''):
        self.__nom = str(nom)
        self.__ciudad = str(cuidad)
        self.__contratos = []
    def __str__(self):
        return 'Equipo: {}\nCuidad:{}'.format(self.__nom, self.__ciudad)
    def getNom(self):
        return self.__nom
    def getContratos(self):
        return self.__contratos
    def crearContrato(self, contrato):
        self.__contratos.append(contrato)