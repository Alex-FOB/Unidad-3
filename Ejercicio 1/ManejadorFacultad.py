import csv

import numpy as np

from Facultad import facultad

class manejador:
    __documento = None
    __arreglo = None
    def __init__(self):
        self.__documento = open('Ejercicio 1\Registros-Facultades.csv') #se abre el archivo
        self.__arreglo = np.empty(5, dtype = facultad) #se crea un arreglo para 5 facultades
    def crearArreglo(self):
        reader = csv.reader(self.__documento, delimiter = ';')
        i = 0
        band = False
        for fila in reader:
            text = fila[3] + ', ' + fila[4]
            indice = int(fila[6]) #hace un cast de la cantidad de carreras que tiene una facultad
            unaFacultad = facultad(fila[0], fila[1], fila[2], text, fila[5], indice, reader) #se crea una instancia de facultad
            self.__arreglo[i] = unaFacultad #se añade al arreglo
            i += 1      
        self.__documento.close()
    def buscar(self, cod): #busca la facultad en base al código de facultad ingresado
        band = False
        i = 0
        pos = -1
        while not band and i < len(self.__arreglo):
            if(self.__arreglo[i].getCod() == cod):
                pos = i
                band = True
            else:
                i += 1
        return pos
    def buscarXcarrera(self, carrera): #busca facultad en base a la carrera ingresada
        band = False
        i = 0
        pos = [-1, -1]
        while not band and i < len(self.__arreglo):
            x = self.__arreglo[i].getCarrera(carrera)
            if(x != -1):
                pos[0] = i
                pos[1] = x
                band = True
            i += 1
        return pos
    def punto1(self, pos):
        return self.__arreglo[pos].getFacultad()
    def punto2(self, pos):
        return self.__arreglo[pos[0]].getFacultad2(pos[1])
    def mostrar(self):
        for facu in self.__arreglo:
            print(facu)