from unicodedata import category
from zope.interface import implementer

from Interfaz import Ejercicio5

from Docente import docente

from PersonalApoyo import personalApoyo

from Investigador import investigador

from DocenteInvestigador import docenteInvestigador

from nodo import Nodo

@implementer(Ejercicio5)

class Manejador:
    __comienzo = None
    def __init__(self):
        self.__comienzo = None
    def agregarElemento(self, elemento):
        aux = self.__comienzo
        if(self.__comienzo == None): #verifica que el primer elemento sea None
            nodo = Nodo(elemento)
            self.__comienzo = nodo
        else:
            while aux.getSiguiente() != None: #recorre la lista
                aux = aux.getSiguiente()
            nodo = Nodo(elemento)
            nodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nodo)
    def insertarElemento(self, pos, elemento):
        i = 1
        aux = self.__comienzo
        if(pos == 0): #si esta en el comienzo
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        else:
            while aux.getSiguiente() != None and i < pos: #recorre la lista hasta el final o hasta la posición anterior del pos
                i += 1
                aux = aux.getSiguiente()
            if(i == pos): #verifica que finalizó en la posición anterior
                nodo = Nodo(elemento)
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
            else:
                raise IndexError
    def mostrarElemento(self, pos):
        text = ''
        i = 0
        aux = self.__comienzo
        while aux.getSiguiente() != None and i < pos:
            i += 1
            aux = aux.getSiguiente()
        if(i == pos):
            text = '{}'.format(aux.getDato())
            return text
        else:
            raise IndexError
    #-----------------------------------------------------------------------------------------------------------------------------------
    def crearLista(self):
        lista = []
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            lista.append(dato.toJson())
            aux = aux.getSiguiente()
        return lista
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            agentes = self.crearLista()
        )
        return diccionario
    #-----------------------------------------------------------------------------------------------------------------------------------
    def antiguedad(self, dato):
        resultado = 0
        porcentaje = dato.getAntiguedad() / 100
        resultado = dato.getSueldo() * porcentaje
        return resultado
    def cargo(self, dato):
        resultado = 0
        cargo = dato.getCargo()
        if(cargo.lower() == 'simple'):
            resultado = dato.getSueldo() * 0.1 #10%
        elif(cargo.lower() == 'semiexclusivo'):
            resultado = dato.getSueldo() * 0.2 #20%
        elif(cargo.lower() == 'exclusivo'):
            resultado = dato.getSueldo() * 0.5 #50%
        return resultado
    def categoria(self, dato):
        resultado = 0
        categoria = dato.getCategoria()
        if(categoria >= 1 and categoria <= 10):
            resultado = dato.getSueldo() * 0.1 #10%
        elif(categoria >= 11 and categoria <= 20):
            resultado = dato.getSueldo() * 0.2 #20%
        elif(categoria >= 21 and categoria <= 30):
            resultado = dato.getSueldo() * 0.3 #30%
        return resultado
    def calcSueldo(self):
        sueldo = 0
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(isinstance(dato, docente) or isinstance(dato, docenteInvestigador)):
                sueldo = dato.getSueldo() + self.antiguedad(dato) + self.cargo(dato)
            elif(isinstance(dato, personalApoyo)):
                sueldo = dato.getSueldo() + self.antiguedad(dato) + self.categoria(dato)
            elif(isinstance(dato, investigador)):
                sueldo = dato.getSueldo() + self.antiguedad(dato)
            if(isinstance(dato, docenteInvestigador)):
                sueldo += dato.getImporteExtra()
            dato.setSueldo(sueldo)
            aux = aux.getSiguiente()
    def ordenarLista(self, lista):
        ordenada = lista
        ordenada.sort()
        return ordenada
    def toText(self, lista):
        text = ''
        for dato in lista:
            text += '{} {} Tipo: {} Sueldo: ${}\n'.format(dato.getApe(), dato.getNom(), type(dato), dato.getSueldoAgente())
        return text
    def listaCarrera(self, carrera):
        text = ''
        lista = []
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(isinstance(dato, docenteInvestigador)):
                if(dato.getCarrera().lower() == carrera.lower()):
                    lista.append(dato)
            aux = aux.getSiguiente()
        lista = self.ordenarLista(lista)
        text = self.toText(lista)
        return text
    def getType(self, pos):
        text = ''
        i = 0
        aux = self.__comienzo
        while aux.getSiguiente() != None and i < pos:
            i += 1
            aux = aux.getSiguiente()
        if(i == pos):
            text = '{}'.format(type(aux.getDato()))
            return text
        else:
            raise IndexError
    def contArea(self, area):
        lista = [0, 0]
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(isinstance(dato, docenteInvestigador)):
                if(dato.getArea().lower() == area.lower()):
                    lista[0] += 1
            elif(isinstance(dato, investigador)):
                if(dato.getArea().lower() == area.lower()):
                    lista[1] += 1
            aux = aux.getSiguiente()
        return lista
    def mostrarXCategoria(self, categoria):
        text = ''
        acum = 0
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(isinstance(dato, docenteInvestigador)):
                if(dato.getCategoria().lower() == categoria.lower()):
                    text += '{} {} Importe extra: ${}\n'.format(dato.getApe(), dato.getNom(), dato.getImporteExtra())
                    acum += dato.getImporteExtra()
            aux = aux.getSiguiente()
        text += 'Total de dinero: ${}'.format(acum)
        return text
    def mostrarOrdenado(self):
        text = ''
        lista = []
        aux = self.__comienzo
        while aux != None:
            lista.append(aux.getDato())
            aux = aux.getSiguiente()
        lista = self.ordenarLista(lista)
        text = self.toText(lista)
        return text
    def mostrar(self):
        text = ''
        aux = self.__comienzo
        while aux != None:
            text += '{}\n'.format(aux.getDato())
            aux = aux.getSiguiente()
        return text