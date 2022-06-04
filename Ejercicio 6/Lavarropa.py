import json

from pathlib import Path

from Aparato import aparato

class lavarropa(aparato):
    __capacidad = None #capacidad de lavado
    __velocidad = None
    __cantidad = None #cantidad de programas
    __tipo = None #tipo de carga
    def __init__(self, marca, modelo, color, pais, precio, capacidad, velocidad, cantidad, tipo):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantidad = cantidad
        self.__tipo = tipo.capitalize()
    def __str__(self):
        return '{} {} {} {} {}'.format(super().__str__(), self.__capacidad, self.__velocidad, self.__cantidad, self.__tipo)
    def getCapacidad(self):
        return self.__capacidad
    def getCarga(self):
        return self.__tipo
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = super().getMarca(),
                modelo = super().getModelo(),
                color = super().getColor(),
                pais = super().getPais(),
                precio = super().getPrecio(),
                imp = super().getImp(),
                capacidad = self.__capacidad,
                velocidad = self.__velocidad,
                cantidad = self.__cantidad,
                tipo = self.__tipo
            )
            )
        return diccionario