from ManejadorFlores import manejadorFlores

from ManejadorRamos import manejadorRamos

class menu:
    __op = None
    __flores = None
    __ramos = None
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.salir}
        self.__flores = manejadorFlores()
        self.__flores.crearArreglo()
        self.__ramos = manejadorRamos()
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
    def punto1(self): #registrar venta de ramo
        band = False
        tipo = str(input('Ingrese tipo de ramo: ')).lower()
        if(tipo.strip() == 'chico' or tipo.strip() == 'mediano' or tipo.strip() == 'grande'): #verifica el tipo de ramo
            indice = self.__ramos.crearRamo(tipo)
            print('{}'.format(self.__flores.mostrar())) #muestra la flores disponibles para armar un ramo
            print('Ingrese "finalizar" para terminar')
            while not band:
                nom = str(input('Nombre de flor: ')).lower()
                if(nom.strip() != 'finalizar'):
                    pos = self.__flores.buscarFlor(nom)
                    if(pos != -1): #verifica la flor
                        try:
                            cantidad = int(input('Ingrese la cantidad de flores: '))
                            #PREGUNTAR SI ESTÁ BIEN---------------------------------------
                            flor = self.__flores.getFlor(pos) #obtiene la flor
                            self.__ramos.agregarFlor(indice, flor, cantidad) #crea el ramo
                            #-------------------------------------------------------------
                            self.__flores.contar(pos, cantidad) #cuenta la cantidad de flores vendidas
                        except ValueError:
                            self.error()
                    else:
                        print('ERROR: flor no encontrada')
                else:
                    band = True
        else:
            print('ERROR: tipo de ramo invalido')
        print('RAMOS VENDIDOS:\n{}'.format(self.__ramos.mostrar()))
        input()
    def punto2(self): #mostrar las 5 más vendidas
        print('Flores más vendidas:\n{}'.format(self.__flores.ordenar()))
        input()
    def punto3(self): #ingresar tipo de ramo
        tipo = str(input('Ingrese tipo de ramo: ')).lower()
        if(tipo.strip() == 'chico' or tipo.strip() == 'mediano' or tipo.strip() == 'grande'): #verifica el tipo de ramo
            print(self.__ramos.buscar(tipo))
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()
    def error(self):
        print('ERROR: valor ingresado')
        input()