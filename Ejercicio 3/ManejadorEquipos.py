import numpy as np

from Equipo import equipo

class manejadorEquipos:
    __equipos = None #contedrá los datos del archivo
    __dim = 0
    __i = 0
    def __init__(self):
        self.__equipos = np.empty(self.__dim, dtype = equipo)
    def modDim(self, dimension): #redimensiona el arreglo
        self.__dim = dimension
        self.__equipos.resize(self.__dim)
    def addEquipo(self, equipo): #añade un equipo al arreglo
        self.__equipos[self.__i] = equipo
        self.__i += 1
    def buscar(self, equipo): #busca un equipo y devuelve su posicion
        i = 0
        pos = -1
        band = False
        while not band and i < len(self.__equipos):
            if(self.__equipos[i].getNom().lower() == equipo.lower()):
                pos = i
                band = True
            i += 1
        return pos
    def crearContratos(self, pos, contrato):
        self.__equipos[pos].crearContrato(contrato)
    def getEquipo(self, pos): #envía una referencia de un contrato
        return self.__equipos[pos]
    def equivalencia(self, fecha): #convierte la fecha en una lista de enteros
        lista = []
        f = fecha.split('/')
        for dato in f:
            lista.append(int(dato))
        return lista
    def mostrarContratos(self, pos, fecha): #devuelve los contratos que vencen en 6 meses
        text = ''
        contratos = self.__equipos[pos].getContratos() #obtiene los contratos del equipo
        for contrato in contratos:
            fechaInicio = self.equivalencia(fecha)
            fechaFin = self.equivalencia(contrato.getFin())
            if(fechaInicio[2] == fechaFin[2]): #compara los años
                dif = fechaFin[1] - fechaInicio[1] #hace una diferencia entre los meses
                if(dif == 6):
                    text += '{}\n'.format(contrato.getJugador())
        return text
    def importeTotal(self, pos, fecha):
        acum = 0.0
        contratos = self.__equipos[pos].getContratos() #obtiene los contratos del equipo
        for contrato in contratos:
            fechaInicio = self.equivalencia(contrato.getInicio())
            fechaFin = self.equivalencia(contrato.getFin())
            if(fechaInicio[2] == fechaFin[2]): #cuando el contrato vence en el mismo año
                acum += (fechaFin[1] - fechaInicio[1]) * contrato.getPago()
            else: #cuando el contrato vence en diferentes años
                año = (fechaFin[2] - fechaInicio[2]) * 12
                mes = fechaFin[1] + año
                acum += (mes - fechaInicio[1]) * contrato.getPago()
        return acum