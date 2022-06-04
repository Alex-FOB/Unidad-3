from Aparato import aparato

from Televisor import televisor

from Lavarropa import lavarropa

from Heladera import heladera

class menu:
    __op = None
    __json = None
    __manejador = None
    #PARA VALIDAR LOS DATOS INGRESADOS
    __valido = ['crt', 'vga', 'svga', 'plasma', 'lcd', 'led', 'touchscreen', 'multitouch', 'sd', 'hd', 'full hd', 'verdadero', 'falso', 600, 1200, 'frontal', 'superior']
    def __init__(self, json, manejador):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.punto4, 5: self.punto5, 6: self.punto6, 7: self.punto7, 8: self.salir}
        self.__json = json
        self.__manejador = manejador
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def ingresar(self): #funciona tanto para el punto1 y punto2
        unAparato = None
        print('Ingrese los datos de un aparato:')
        try:
            tipo = str(input('¿Que aparato desea crear? '))
            if(tipo.lower() == 'televisor' or tipo.lower() == 'lavarropa' or tipo.lower() == 'heladera'):
                marca = str(input('Ingrese marca: '))
                modelo = str(input('Ingrese modelo: '))
                color = str(input('Ingrese el color: '))
                pais = str(input('Ingrese pais de fabricacion: '))
                precio = float(input('Ingrese precio base: '))
            else:
                print('ERROR: aparato no disponible')
            if(tipo.lower() == 'televisor'): #EN EL CASO DE QUE SEA UN TELEVISOR
                pantalla = str(input('Tipo de pantalla: '))
                pulgadas = int(input('Pulgadas: '))
                definicion = str(input('Tipo de definicion: '))
                conexion = str(input('Conexion a internet: '))
                #Verificar que algunos de los datos sean correctos
                if(pantalla.lower() in self.__valido and definicion.lower() in self.__valido and conexion.lower() in self.__valido):
                    #se crea la instancia
                    unAparato = televisor(marca, modelo, color, pais, precio, pantalla, pulgadas, definicion, conexion)
            if(tipo.lower() == 'lavarropa'): #EN EL CASO DE QUE SEA UN LAVARROPA
                capacidad = float(input('Capacidad de lavado (kg): '))
                velocidad = int(input('Velocidad de centrifugado: '))
                programas = int(input('Cantidad de programas: '))
                carga = str(input('Tipo de carga: '))
                #Verificar que algunos de los datos sean correctos
                if(velocidad in self.__valido and carga.lower() in self.__valido):
                    #se crea la instancia
                    unAparato = lavarropa(marca, modelo, color, pais, precio, capacidad, velocidad, programas, carga)
            if(tipo.lower() == 'heladera'): #EN EL CASODE QUE SEA UNA HELADERA
                capacidad = float(input('Capacidad en litros: '))
                freezer = str(input('Freezer: '))
                ciclica = str(input('Ciclica: '))
                #Verificar que algunos de los datos sean correctos
                if(freezer.lower() in self.__valido and ciclica.lower() in self.__valido):
                    #se crea la instancia
                    unAparato = heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
        except ValueError:
            self.error()
        return unAparato
    def calculaImp(self): #calcula los importes de los aparatos
        print('ENTRA EN MENU')
        self.__manejador.calcImp()
    def punto1(self): #-----------------------------INSERTAR------------------------------------------------------------
        unAparato = self.ingresar()
        if(isinstance(unAparato, aparato)): #verifica que los datos ingresador sean validos
            if(not self.__manejador.validar(unAparato)):
                try:
                    pos = int(input('Ingrese posicion: '))
                    #dim = self.__manejador.getLen()
                    #se añade la instancia creada a la lista
                    try:
                        self.__manejador.insertarElemento(pos, unAparato)
                        print(self.__manejador.mostrarElemento(pos)) 
                    except IndexError:
                        print('ERROR: posicion invalida')
                except ValueError:
                    self.error()
            else:
                print('ERROR: aparato ya creado')
        else:
            print('ERROR: datos invalidos')
        input()
    def punto2(self): #-----------------------------AGREGAR------------------------------------------------------------
        unAparato = self.ingresar()
        if(isinstance(unAparato, aparato)): #verifica que los datos ingresador sean validos
            if(not self.__manejador.validar(unAparato)):
                #se añade la instancia creada a la lista
                try:
                    self.__manejador.agregarElemento(unAparato)
                    print(self.__manejador.mostrar())
                except IndexError:
                    self.error()
            else:
                print('ERROR: aparato ya creado')
        else:
            print('ERROR: datos invalidos')
        input()
    def punto3(self): #en base a una posición dar el tipo de dato
        try:
            pos = int(input('Ingrese la posicion: '))
            #dim = self.__manejador.getLen()
            print(self.__manejador.getType(pos)) #imprime el tipo de dato
        except:
            self.error()
        input()
    def punto4(self): #devuelve los aparatos de marca philips
        text = self.__manejador.getAparatos('Philips') #le ingresamos la marca Philips
        if(len(text) > 0):
            print(text)
        else:
            print('ERROR: no hay aparatos de esa marca')
        input()
    def punto5(self): #muestra las marcas de lavarropas con carga superior
        text = self.__manejador.getLavarropas()
        if(len(text) > 0):
            print('Marca de lavarropa:\n', text)
        else:
            print('ERROR: no hay lavarropas de carga superior')
        input()
    def punto6(self):
        print(self.__manejador.mostrar())
        input()
    def punto7(self):
        diccionario = self.__manejador.toJson()
        self.__json.saveJSONArchivo(diccionario, 'Ejercicio 6/DatosAparatos.json')
        input()
    def error(self):
        print('ERROR: valor invalido')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()