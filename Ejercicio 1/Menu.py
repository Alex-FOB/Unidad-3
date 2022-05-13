from ManejadorFacultad import manejador

class menu:
    __op = None
    __funcion = None
    __control = None
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.mostrar, 4: self.salir}
        self.__control = manejador()
        self.__control.crearArreglo() #crea el arreglo de facultades
    def opcion(self, op):
        self.__funcion = self.__op.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def punto1(self):
        try:
            cod = int(input('Ingrese codigo de la facultad: '))
            pos = self.__control.buscar(cod)
            if(pos != -1):
                print(self.__control.punto1(pos))
            else:
                print('ERROR: facultad no encontrada')
            input()
        except ValueError:
            self.error()
    def punto2(self):
        carrera = str(input('Ingrese carrera: '))
        pos = self.__control.buscarXcarrera(carrera)
        if(pos[0] != -1):
            print(self.__control.punto2(pos))
        else:
            print('ERROR: carrera no encontrada')
        input()
    def mostrar(self):
        self.__control.mostrar()
        input()
    def error(self):
        print('ERROR: valor erroneo')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()