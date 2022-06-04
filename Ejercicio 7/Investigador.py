from Agente import agente

class investigador(agente):
    __area = None #area de investigación
    __tipo = None #tipo de investigación
    def __init__(self, cuil, ape, nom, sueldo, antiguedad, area, tipo, carrera = '', cargo = '', catedra = '', categoria = '', importeExtra = 0):
        super().__init__(cuil, ape, nom, sueldo, antiguedad)
        self.__area = str(area).capitalize()
        self.__tipo = str(tipo).capitalize()
    def __str__(self):
        return '{}\n    Area: {:50} Tipo:{}'.format(super().__str__(), self.__area, self.__tipo)
    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                ape = super().getApe(),
                nom = super().getNom(),
                sueldo = super().getSueldo(),
                antiguedad = super().getAntiguedad(),
                area = self.__area,
                tipo = self.__tipo
            )
        )
        return diccionario