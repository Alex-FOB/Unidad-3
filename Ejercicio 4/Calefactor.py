class calefactor:
    __marca = None
    __modelo = None
    def __init__(self, marca, modelo, potencia, matricula, calorias):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
    def __str__(self):
        return 'Marca/Modelo: {}/{:20}'.format(self.__marca, self.__modelo)