from audioop import reverse
import csv

import numpy as np

from Flores import flor

class manejadorFlores:
    __arreglo = None
    __documento = None
    __dim = 0 #dimensión del arreglo
    def __init__(self):
        self.__arreglo = np.empty(self.__dim, dtype = flor) #se crea el archivo de flores
        self.__documento = open('Ejercicio 2/flores.csv') #abre el archivo
    def crearArreglo(self):
        reader = csv.reader(self.__documento, delimiter = ';') #se lee el archivo
        band = False
        i = 0
        for fila in reader:
            if(band == False):
                band = True
            else:
                unaFlor = flor(fila[0], fila[1], fila[2], fila[3])
                self.__dim += 1 #aplia en 1 la dimensión del arreglo
                self.__arreglo.resize(self.__dim) #redimensiona el arreglo
                self.__arreglo[i] = unaFlor #añade una flor al arreglo
                i += 1
        self.__documento.close()
    def buscarFlor(self, nom): #en base al nombre de la flor, la busca en el arreglo y devuelve su posición
        band = False
        i = 0
        pos = -1
        while not band and i < len(self.__arreglo):
            nomFlor = self.__arreglo[i].getNom().lower() #obtenemos el nombre en minuscula
            if(nomFlor.strip() == nom.strip()): #.strip() quita los espacios
                pos = i
                band = True
            i += 1
        return pos
    def getFlor(self, pos): #devuelve una flor
        return self.__arreglo[pos]
    def contar(self, pos, cantidad): #cuenta cada venta de una flor
        self.__arreglo[pos].vendido(cantidad)
    def ordenar(self): #devuelve las 5 flores más vendidas
        text = ''
        lista = np.sort(self.__arreglo)[::-1] #ordena el arreglo de mayor a menor
        for i in range(5): #selecciona las 5 primeras
            text += '{}°.- {}'.format(i+1, lista[i].getNom()) + '\n'
        return text
    def mostrar(self): #muestra el contenido del arreglo
        text = ''
        for flor in self.__arreglo:
            text += '{}'.format(flor) + '\n'
        return text