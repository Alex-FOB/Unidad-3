from Calefactor import calefactor

class gas(calefactor):
    __matricula = None
    __calorias = None
    def __init__(self, marca, modelo, potencia, matricula, calorias):
        super().__init__(marca, modelo, potencia, matricula, calorias)
        self.__matricula = str(matricula)
        self.__calorias = float(calorias)
    def __str__(self):
        return '{} Matricula: {:25} Calorias: {} kcal/m^3'.format(super().__str__(), self.__matricula, self.__calorias)
    def getCalefactor(self):
        return super().__str__()
    def getConsumo(self):
        return self.__calorias