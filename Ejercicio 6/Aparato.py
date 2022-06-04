class aparato:
    __marca = None
    __modelo = None
    __color = None
    __pais = None #país de fabricación
    __precio = None #precio base
    __imp = None #añadido
    def __init__(self, marca, modelo, color, pais, precio):
        self.__marca = marca.capitalize()
        self.__modelo = modelo
        self.__color = color.capitalize()
        self.__pais = pais.capitalize()
        self.__precio = precio
        self.__imp = 0 #AÑADIDO
    def __str__(self):
        return '{}/{} - Color: {} - Pais: {} - Importe: ${:.2f}:\n'.format(self.__marca, self.__modelo, self.__color, self.__pais, self.__imp)
    def __eq__(self, other):
        band = False
        if(self.__marca.lower() == other.getMarca().lower() and self.__modelo.lower() == other.getModelo().lower()):
            band = True
        return band
    def setImp(self, imp):
        self.__imp = imp 
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getColor(self):
        return self.__color
    def getPais(self):
        return self.__pais
    def getPrecio(self):
        return self.__precio
    def getImp(self):
        return self.__imp