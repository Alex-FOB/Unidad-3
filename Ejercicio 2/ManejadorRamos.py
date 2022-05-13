from Ramos import ramo
class manejadorRamos:
    __lista = []
    __indice = -1
    def __init__(self):
        self.__lista = []
    def crearRamo(self, tipo = '', flor = None, cantidad = 0): #la idea, de momento, es crear un ramo vacío
        self.__indice += 1
        unRamo = ramo(tipo, flor, cantidad)
        self.__lista.append(unRamo)
        return self.__indice
    def agregarFlor(self, indice, flor, cantidad): #agrega flores al ramo
        self.__lista[indice].addFlor(flor, cantidad)
    def buscar(self, tipo): #busca el/los ramos con el mismo tipo
        text = ''
        for ramo in self.__lista:
            tamaño = ramo.getTamaño().lower()
            if(tamaño.strip() == tipo.strip()): #compara el tipo de ramo
                text += '{}'.format(ramo) + '\n'
        return text
    def mostrar(self): #muestra el contenido de los ramos
        text = ''
        for ramo in self.__lista:
            text += '{}'.format(ramo) + '\n'
        return text