class carrera:
    __cod = None #código de la carrera
    __nom = None #nombre de la carrera
    __dur = None #duración de la carrera
    __titulo = None #título de la carrera
    __tipo = None
    def __init__(self, cod, nom, dur, titulo, tipo):
        self.__cod = int(cod)
        self.__nom = str(nom)
        self.__dur = str(dur)
        self.__titulo = str(titulo)
        self.__tipo = str(tipo)
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.__cod, self.__nom, self.__titulo, self.__dur, self.__tipo)
    def getCarrera(self): #devuelve los datos requeridos de una carrera en str
        return '{:45} Duracion: {}'.format(self.__nom, self.__dur)
    def getNom(self):
        return self.__nom
    def getCod(self):
        return self.__cod