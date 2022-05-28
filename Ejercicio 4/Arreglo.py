import numpy as np

from Calefactor import calefactor

from CalefactorElectrico import electrico

from CalefactorGas import gas

class arreglo:
    __arreglo = None
    __dim = 0
    __i = 0
    def __init__(self):
        self.__i = 0
        self.__dim = 0
        self.__arreglo = np.empty(self.__dim, dtype = calefactor)
    def modDim(self, dim):
        self.__dim = dim
        self.__arreglo.resize(self.__dim)
    def addCalefactor(self, unCalefator):
        if(self.__i <= self.__dim - 1): #pregunta si está al final del arreglo
            self.__arreglo[self.__i] = unCalefator
            self.__i += 1
        else:
            self.__dim += 1
            self.__arreglo.resize(self.__dim)
            self.__arreglo[self.__i] = unCalefator
            self.__i += 1
    def calcular(self, pos, cantidad, costo):
        costoT = 0.0
        costoT = (self.__arreglo[pos].getConsumo()/100)*cantidad*costo
        return costoT
    def punto1(self, cantidad, costo):
        pos = -1
        min = 1000000000000
        for i in range(len(self.__arreglo)):
            if(isinstance(self.__arreglo[i], gas)):
                costo = self.calcular(i, cantidad, costo)
                if(costo < min):
                    min = costo
                    pos = i
        return pos
    def punto2(self, cantidad, costo):
        pos = -1
        min = 1000000000000
        for i in range(len(self.__arreglo)):
            if(isinstance(self.__arreglo[i], electrico)):
                costo = self.calcular(i, cantidad, costo)
                if(costo < min):
                    min = costo
                    pos = i
        return pos
    def punto3(self, cantidad, costo):
        pos = -1
        min = 1000000000000
        for i in range(len(self.__arreglo)):
            costo = self.calcular(i, cantidad, costo)
            if(costo < min):
                min = costo
                pos = i
        return pos
    def mostrar(self, pos):
        return '{}'.format(self.__arreglo[pos].getCalefactor())
    def mostrarTodo(self, pos):
        return '{}'.format(self.__arreglo[pos])