import csv

import numpy as np

from Contrato import contrato

class manejadorContrato:
    __contratos = None
    __dim = 0
    __i = 0
    def __init__(self):
        self.__dim = 0
        self.__i = 0
        self.__contratos = np.empty(self.__dim, dtype = contrato)
    def setDim(self, dim): #redimensiona el arreglo que contrandrá las instancias de los contratos
        self.__dim = dim
        self.__contratos.resize(self.__dim)
    def addContrato(self, contrato): #añade un contrato al arreglo
        self.__contratos[self.__i] = contrato
        self.__i += 1
    def buscar(self, dni): #busca un contrato en base al dni del jugador
        band = False
        pos = -1
        i = 0
        while not band and i < len(self.__contratos):
            jugador = self.__contratos[i].getJugador()
            if(jugador.getDNI() == dni):
                pos = i
                band = True
            i += 1
        return pos
    def punto2(self, pos): #verifica que el jugador haya sido contratado
        equipo = self.__contratos[pos].getEquipo()
        text = 'JUGADOR CONTRATADO\nEquipo: {:20}\n'.format(equipo.getNom())
        text += 'Fecha de finalizacion del contrato: {}'.format(self.__contratos[pos].getFin())
        return text
    def saveContratos(self): #guarda los contratos realizados
        band = False
        with open('Ejercicio 3/contratos.csv', 'w', newline = '') as archi:
            writer = csv.writer(archi, delimiter = ',')
            writer.writerow(['DNI del jugador', 'Nombre del equipo', 'Fecha de inicio', 'Fecha final', 'Pago mensual'])
            for contrato in self.__contratos:
                if(contrato is not None):
                    jugador = contrato.getJugador()
                    equipo = contrato.getEquipo()
                    writer.writerow([jugador.getDNI(), equipo.getNom(), contrato.getInicio(), contrato.getFin(), contrato.getPago()])
                    if(band == False):
                        band = True
        archi.close()
        return band