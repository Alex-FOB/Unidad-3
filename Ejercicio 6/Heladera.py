import json

from pathlib import Path

from Aparato import aparato

class heladera(aparato):
    __capacidad = None
    __freezer = None
    __ciclica = None
    def __init__(self, marca, modelo, color, pais, precio, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        if(freezer.lower() == 'verdadero'):
            self.__freezer = True
        else:
            self.__freezer = False
        if(ciclica.lower() == 'verdadero'):
            self.__ciclica = True
        else:
            self.__ciclica = False
    def __str__(self):
        return '{} {} {} {}'.format(super().__str__(), self.__capacidad, self.__freezer, self.__ciclica)
    def getFreezer(self):
        return self.__freezer
    def getCiclica(self):
        return self.__ciclica
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
                freezer = self.__freezer,
                ciclica = self.__ciclica
            )
            )
        return diccionario