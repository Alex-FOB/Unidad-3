class flor:
    __num = None #número de flor
    __nom = None #nombre de la flor
    __color = None #color de la flor
    __des = None #descripción de la flor
    __venta = None #AÑADIDO: cuenta cuantas veces se vendió esta flor
    def __init__(self, num, nom, color, des):
        try:
            self.__num = int(num)
            self.__nom = str(nom)
            self.__color = str(color)
            self.__des = str(des)
            self.__venta = 0
        except ValueError:
            self.__num = 0
            self.__nom = 'unknown'
            self.__color = 'unknown'
            self.__des = 'unknown'
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__num, self.__nom, self.__color, self.__des)
    def __gt__(self, other): #se sobrecarga el operador > para ordenar el arreglo
        return self.__venta > other.getVenta()
    def getNom(self):
        return self.__nom
    def vendido(self, cantidad):
        self.__venta += cantidad
    def getVenta(self):
        return self.__venta