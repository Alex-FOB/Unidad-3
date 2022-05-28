class menu:
    __op = None
    __arreglo = None
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.salir}
    def setArreglo(self, arreglo):
        self.__arreglo = arreglo
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def punto1(self): #mínimo de consumo de gas 
        try:
            costo = float(input('Ingrese el costo del m^3: $'))
            cantidad = float(input('Ingrese cantidad de m^3: '))
            pos = self.__arreglo.punto1(cantidad, costo)
            if(pos != -1):
                print('CALEFACTOR A GAS: de menor consumo\n', self.__arreglo.mostrar(pos))
            else:
                print('ERROR: no hay calefactores a gas')
        except ValueError:
            self.salir()
        input()
    def punto2(self): #mínimo de consumo eléctrico
        try:
            costo = float(input('Ingrese el costo del m^3: $'))
            cantidad = float(input('Ingrese cantidad de m^3: '))
            pos = self.__arreglo.punto2(cantidad, costo)
            if(pos != -1):
                print('CALEFACTOR ELECTRICO: de menor consumo\n', self.__arreglo.mostrar(pos))
            else:
                print('ERROR: no hay calefactores electricos')
        except ValueError:
            self.error()
        input()
    def punto3(self):
        try:
            costo = float(input('Ingrese el costo del m^3: $'))
            cantidad = float(input('Ingrese cantidad de m^3: '))
            pos = self.__arreglo.punto3(cantidad, costo)
            if(pos != -1):
                print('CALFACTOR: de menor consumo\n', self.__arreglo.mostrarTodo(pos))
            else:
                print('ERROR: no hay calefactores')
        except ValueError:
            self.error()
        input()
    def error(self):
        print('ERROR: valor invalido')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()