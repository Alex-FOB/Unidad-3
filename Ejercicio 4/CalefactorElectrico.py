from Calefactor import calefactor

class electrico(calefactor):
    __potencia = None #potencia máxima
    def __init__(self, marca, modelo, potencia, matricula, calorias):
        super().__init__(marca, modelo, potencia, matricula, calorias)
        self.__potencia = float(potencia)
    def __str__(self):
        return '{} Potencia: {} watts'.format(super().__str__(), self.__potencia)
    def getCalefactor(self):
        return super().__str__()
    def getConsumo(self):
        return self.__potencia