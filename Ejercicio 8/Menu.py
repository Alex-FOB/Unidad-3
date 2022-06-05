from msilib.schema import CreateFolder
from zope.interface import implementer

from InterfazDirector import interfazDirector

from InterfazTesorero import interfazTesorero

@implementer(interfazDirector)

@implementer(interfazTesorero)

class menu:
    __op = None
    __manejador = None
    __json = None
    def __init__(self, manejador, json):
        self.__op = {1: self.ingresarDatos, 2: self.salir}
        self.__manejador = manejador
        self.__json = json
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
    def opcion2(self, op, manejador):
        funcion = self.__op.get(op)
        if funcion:
            funcion(manejador)
        else:
            print('ERROR: opcion invalida')
    def ingresarDatos(self):
        usuario = str(input('Usuario/Contraseña: '))
        try:
            nickname = usuario.split('/')
            password = nickname[1]
            if(nickname[0] == 'uDirector' and password == 'ufC77#!1'):
                self.director(interfazDirector(self.__manejador)) #restringimos los métodos del manejador
            elif(nickname[0] == 'uTesorero' and password == 'ag@74ck'):
                self.tesorero(interfazTesorero(self.__manejador)) #restringimos los métodos del manejador
            else:
                print('ERROR: usuario no valido')
        except IndexError:
            self.error()
        input()
    def director(self, manejadorDirector: interfazDirector):
        band = False
        self.__op = {1: self.modSueldoBasico, 2: self.modCargo, 3: self.modCategoria, 4: self.modImporteExtra, 5: self.salirMenu}
        while not band:
            print('1.- Modificar sueldo basico\n2.- Modificar cargo\n3.- Modificar categoria'
                '\n4.- Modificar importe extra\n5.- salir')
            try:
                op = int(input('Opcion: '))
                self.opcion2(op, manejadorDirector)
                band = op == 5
            except ValueError:
                self.error()
    def tesorero(self, manejadorTesorero: interfazTesorero):
        cuil = str(input('Ingrese el cuil: '))
        sueldo= manejadorTesorero.gastosSueldoPorEmpleado(cuil)
        if(sueldo != -1):
            print('Sueldo del agente: ${}'.format(sueldo))
        else:
            print('ERROR: agente no encontrado')
        input()
    def modSueldoBasico(self, manejador):
        cuil = str(input('Ingrese el cuil: '))
        try:
            sueldo = float(input('Ingrese el nuevo sueldo basico: $'))
            if(sueldo >= 0):
                manejador.modificarBasico(cuil, sueldo)
                print(self.__manejador.mostrarElemento(cuil))
            else:
                print('ERROR: sueldo negativo')
        except ValueError:
            self.error()
        input()
    def modCargo(self, manejador):
        cuil = str(input('Ingrese el cuil: '))
        cargo = str(input('Ingrese el nuevo cargo: ')).capitalize()
        if(cargo == 'Simple' or cargo == 'Semiexclusivo' or cargo == 'Exclusivo'):
            manejador.modificarPorcentajePorCargo(cuil, cargo)
            print(self.__manejador.mostrarElemento(cuil))
        else:
            print('ERROR: cargo invalido')
        input()
    def modCategoria(self, manejador):
        cuil = str(input('Ingrese el cuil: '))
        try:
            categoria = int(input('Ingrese la nueva categoria: ')).capitalize()
            if(categoria > 0 and categoria <= 22):
                manejador.modificarPorcentajePorCategoria(cuil, categoria)
                print(self.__manejador.mostrarElemento(cuil))
        except ValueError:
            self.error()
        input()
    def modImporteExtra(self, manejador):
        cuil = str(input('Ingrese el cuil: '))
        try:
            importe = float(input('Ingrese el importe extra: $'))
            if(importe >= 0):
                manejador.modificarImporteExtra(cuil, importe)
                print(self.__manejador.mostrarElemento(cuil))
            else:
                print('ERROR: importe negativo')
        except ValueError:
            self.error()
        input()
    def error(self):
        print('ERROR: valor invalido')
        input()
    def salirMenu(self, manejador):
        self.__op = {1: self.ingresarDatos, 2: self.salir}
        print('VOLVIENDO AL MENU PRINCIPAL...')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()