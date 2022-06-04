from Agente import agente

class docente(agente):
    __carrera = None
    __cargo = None
    __catedra = None
    def __init__(self, cuil, ape, nom, sueldo, antiguedad, area = '', tipo = '', carrera = '', cargo = '', catedra = '', categoria = '', importeExtra = 0):
        super().__init__(cuil, ape, nom, sueldo, antiguedad, area, tipo)
        self.__carrera = str(carrera).capitalize()
        self.__cargo = str(cargo).capitalize()
        self.__catedra = str(catedra).capitalize()
    def __str__(self):
        return '{}\n    Carrera: {:30} Cargo: {:10} Catedra: {}'.format(super().__str__(), self.__carrera, self.__cargo, self.__catedra)
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                ape = super().getApe(),
                nom = super().getNom(),
                sueldo = super().getSueldo(),
                antiguedad = super().getAntiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra
            )
        )
        return diccionario