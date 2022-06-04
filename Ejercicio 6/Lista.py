from zope.interface import implementer

from nodo import Nodo

from Interfaz import Ejercicio5

from Televisor import televisor

from Lavarropa import lavarropa

from Heladera import heladera

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
    #-------------------------------------------------------------------------------------------------------------------
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
            aparatos = self.crearLista()
        )
        return diccionario
    #------------------------------------------------------------------------------------------------------------------
    def getLen(self):
        dim = 0
        aux = self.__comienzo
        while aux != None:
            dim += 1
            aux = aux.getSiguiente()
        return dim
    def impTelevisor(self, dato, precio): #calcula el importe de los televisores
        imp = 0
        if(dato.getDefinicion().lower() == 'sd'):
            add = precio * 0.01 #1%
            imp = precio + add
        elif(dato.getDefinicion().lower() == 'hd'):
            add = precio * 0.02 #2%
            imp = precio + add
        elif(dato.getDefinicion().lower() == 'full hd'):
            add = precio * 0.03 #3%
            imp = precio + add
        if(dato.getConexion() == True):
            add = imp * 0.1 #10%
            imp += add
        return imp
    def impLavarropa(self, dato, precio): #calcula el importe de los lavarropas
        imp = 0
        capacidad = dato.getCapacidad()
        if(capacidad <= 5): #si es menor a 5kg
            add = precio * 0.01 #1%
            imp = precio + add
        else:
            add = precio * 0.03 #3%
            imp = precio + add
        return imp
    def impHeladera(self, dato, precio): #calcula el importe de las heladeras
        imp = 0
        if(dato.getFreezer() == True):
            add = precio * 0.05 #5%
            imp = precio + add
        else:
            add = precio * 0.01 #1%
            imp = precio + add
        if(dato.getCiclica() == True):
            add = precio * 0.1 # 10%
            imp += add
        return imp
    def calcImp(self):
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(dato.getImp() == 0):
                precio = dato.getPrecio()
                if(isinstance(dato, televisor)): 
                    imp = self.impTelevisor(dato, precio)
                elif(isinstance(dato, lavarropa)): 
                    imp = self.impLavarropa(dato, precio)
                elif (isinstance(dato, heladera)): 
                    imp = self.impHeladera(dato, precio)
                dato.setImp(imp)
            aux = aux.getSiguiente()
    def validar(self, aparato): #verifica que el elemento esté en la lista
        band = False
        aux = self.__comienzo
        while aux != None:
            if(aux.getDato() == aparato):
                band = True
            aux = aux.getSiguiente()
        return band
    def getType(self, pos): #retorna el tipo de dato
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
    def getAparatos(self, marca): #retorna los aparatos de una marca
        text = ''
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(dato.getMarca().lower() == marca.lower()):
                text += '{}\n'.format(aux.getDato())
            aux = aux.getSiguiente()
        return text
    def getLavarropas(self): #retorna las marcas de los lavarropas de carga superior
        text = ''
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if(isinstance(dato,lavarropa)): #verifica que sean lavarropas
                if(dato.getCarga().lower() == 'superior'): #verifica que sean de carga superior
                    text += '{}\n'.format(dato.getMarca())
            aux = aux.getSiguiente()
        return text
    def mostrarElemento(self, pos): #muestra un solo elemento de la lista en base a su posición
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
    def mostrar(self): #muestra todos los elementos de la lista
        text = ''
        i = 0
        aux = self.__comienzo
        while aux != None: #recorre la lista
            text += '{}.- {}\n'.format(i, aux.getDato())
            i += 1
            aux = aux.getSiguiente()
        return text