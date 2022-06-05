from zope.interface import implementer

from Interfaz import Ejercicio5

from InterfazDirector import interfazDirector

from InterfazTesorero import interfazTesorero

from Docente import docente

from PersonalApoyo import personalApoyo

from Investigador import investigador

from DocenteInvestigador import docenteInvestigador

from nodo import Nodo

@implementer(Ejercicio5)

@implementer(interfazDirector)

@implementer(interfazTesorero)

class Manejador:
    __comienzo = None
    __porcentajeCargo = None
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
    def gastosSueldoPorEmpleado(self, cuil):
        sueldo = -1
        band = False
        aux = self.__comienzo
        while aux != None and not band:
            dato = aux.getDato()
            if(dato.getCuil().lower() == cuil.lower()):
                sueldo = dato.getSueldo()
                band = True
            aux = aux.getSiguiente()
        return sueldo
    def modificarBasico(self, cuil, nuevoBasico):
        aux = self.__comienzo
        band = False
        while aux != None and not band:
            dato = aux.getDato()
            if(dato.getCuil().lower() == cuil.lower()): #compara los cuil
                dato.modSueldo(nuevoBasico)
                band = True
            aux = aux.getSiguiente()
    def modificarPorcentajePorCargo(self, cuil, nuevoPorcenaje): #DATO: en vez de modificar el porcentaje, se modificará el cargo
        aux = self.__comienzo
        band = False
        while aux != None and not band:
            dato = aux.getDato()
            if(isinstance(dato, docente) or isinstance(dato, docenteInvestigador)): #asegura que sea docente o docente investigador
                if(dato.getCuil().lower() == cuil.lower()): #compara los cuil
                    dato.modCargo(nuevoPorcenaje)
                    band = True
            aux = aux.getSiguiente()
    def modificarPorcentajePorCategoria(self, cuil, nuevoPorcentaje): #DATO: en vez de modificar el porcentaje, se modificará la categoría
        aux = self.__comienzo
        band = False
        while aux != None and not band:
            dato = aux.getDato()
            if(isinstance(dato, personalApoyo)): #se asegura que sea un personal de apoyo
                if(dato.getCuil().lower() == cuil.lower()): #se compara los cuil
                    dato.modCategoria(nuevoPorcentaje)
                    band = True
            aux = aux.getSiguiente()
    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        aux = self.__comienzo
        band = False
        while aux != None and not band:
            dato = aux.getDato()
            if(isinstance(dato, docenteInvestigador)): #se asegura que sea un docente investigador
                if(dato.getCuil().lower() == cuil.lower()): #se compara los cuil
                    dato.modImporteExtra(nuevoImporteExtra)
                    band = True
            aux = aux.getSiguiente()
    def mostrarElemento(self, cuil):
        text = ''
        aux = self.__comienzo
        band = False
        while aux != None and not band:
            dato = aux.getDato()
            if(dato.getCuil().lower() == cuil.lower()):
                text += '{}\n'.format(dato)
                band = True
            aux = aux.getSiguiente()
        return text
    def mostrar(self):
        text = ''
        aux = self.__comienzo
        while aux != None:
            text += '{}\n'.format(aux.getDato())
            aux = aux.getSiguiente()
        return text