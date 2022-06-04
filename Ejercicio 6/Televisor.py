import json

from pathlib import Path

from Aparato import aparato

class televisor(aparato):
    __pantalla = None #tipo de pantalla
    __pulgadas = None
    __definicion = None #tipod de definición
    __conexion =  None #conexión a internet
    def __init__(self, marca, modelo, color, pais, precio, pantalla, pulgadas, definicion, conexion):
        super().__init__(marca, modelo, color, pais, precio)
        self.__pantalla = pantalla
        self.__pulgadas = pulgadas
        self.__definicion = definicion.upper()
        if(conexion.lower() == 'verdadero'):
            self.__conexion = True
        elif(conexion.lower() == 'falso'):
            self.__conexion = False
    def __str__(self):
        return '{} {} {} {} {}'.format(super().__str__(), self.__pantalla, self.__pulgadas, self.__definicion, self.__conexion)
    def getDefinicion(self):
        return self.__definicion
    def getConexion(self):
        return self.__conexion
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
                pantalla = self.__pantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__definicion
            )
            )
        return diccionario