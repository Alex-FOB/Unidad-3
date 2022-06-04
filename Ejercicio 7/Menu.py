from csv import excel_tab
from Docente import docente

from PersonalApoyo import personalApoyo

from Investigador import investigador

from DocenteInvestigador import docenteInvestigador

class menu:
    __op = None
    __manejador = None
    __json = None
    __categoria = ['I', 'II', 'III', 'IV', 'V']
    def __init__(self, manejador, json):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.punto4, 5: self.punto5, 6: self.punto6, 7: self.punto7, 8: self.punto8, 9: self.salir}
        self.__manejador = manejador
        self.__json = json
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def calcSueldo(self):
        self.__manejador.calcSueldo()
    def ingresar(self):
        unPersonal = None
        try:
            personal = str(input('Ingrese el tipo de personal: '))
            if(personal.lower() == 'docente' or personal.lower() == 'personal de apoyo' or
                personal == 'investigador' or personal.lower() == 'docente investigador'):
                cuil = str(input('Ingrese CUIL: '))
                ape = str(input('Ingrese Apellido: '))
                nom = str(input('Ingrese Nombre: '))
                sueldo = float(input('Ingrese sueldo: $'))
                antiguedad = int(input('Ingrese antiguedad: '))
                if(personal == 'docente'):
                    carrera = str(input('Carrera: '))
                    cargo = str(input('Cargo: '))
                    catedra = str(input('Catedra: '))
                    unPersonal = docente(cuil, ape, nom, sueldo, antiguedad, carrera, cargo, catedra)
                if(personal == 'personal de apoyo'):
                    categoria = int(input('Categoria: '))
                    unPersonal = personalApoyo(cuil, ape, nom, sueldo, antiguedad, categoria)
                if(personal == 'investigador'):
                    area = str(input('Area de Investigacion: '))
                    tipo = str(input('Tipo de Investigacion: '))
                    unPersonal = investigador(cuil, ape, nom, sueldo, antiguedad, area, tipo)
                if(personal == 'docente investigador'):
                    area = str(input('Area de Investigacion: '))
                    tipo = str(input('Tipo de Investigacion: '))
                    carrera = str(input('Carrera: '))
                    cargo = str(input('Cargo: '))
                    catedra = str(input('Catedra: '))
                    categoria = str(input('Categoria en el programa: '))
                    importeExtra = float(input('Importe Extra: $'))
                    unPersonal = docenteInvestigador(cuil, ape, nom, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importeExtra)
            else:
                print('ERROR: personal invalido')
        except ValueError:
            self.error() 
        return unPersonal
    def punto1(self): #----------------------INSERTAR PERSONAL----------------------------------------------------
        unPersonal = self.ingresar()
        if(unPersonal != None):
            try:
                pos = int(input('Ingrese la posicion: ')) - 1 #se resta 1 para que la lista de 1 a ...
                try:
                    self.__manejador.insertarElemento(pos, unPersonal)
                    print(self.__manejador.mostrarElemento(pos))
                except IndexError:
                    print('ERROR: posicion invalida')
            except ValueError:
                self.error()
        else:
            print('ERROR: no se creo el personal')
        input()
    def punto2(self): # --------------------AGREGAR PERSONAL------------------------------------------------------
        unPersonal = self.ingresar()
        if(unPersonal != None):
            self.__manejador.agregarElemento(unPersonal)
            print(self.__manejador.mostrar())
        else:
            print('ERROR: no se creo el personal')
        input()
    def punto3(self): #devuelve el tipo
        try:
            pos = int(input('Ingrese posicion:')) - 1
            try:
                print(self.__manejador.getType(pos))
            except IndexError:
                print('ERROR: posicion invalida')
        except ValueError:
            self.error()
        input()
    def punto4(self): #listado de docentes investigadores en un área
        carrera = str(input('Ingrese nombre de la carrera: '))
        print(self.__manejador.listaCarrera(carrera))
        input()
    def punto5(self): #contar investigadores y docentes investigadores
        area = str(input('Ingrese area de investigacion: ')).lower()
        contador = self.__manejador.contArea(area)
        print('CANTIDAD:\nDocentes investigadores: {} Investigadores: {}'.format(contador[0], contador[1]))
        input()
    def punto6(self):
        print(self.__manejador.mostrarOrdenado())
        input()
    def punto7(self):
        categoria = str(input('Ingrese la categoria: ')).upper()
        if(categoria in self.__categoria):
            print(self.__manejador.mostrarXCategoria(categoria))
        else:
            print('ERROR: categoria invalida')
        input()
    def punto8(self):
        diccionario = self.__manejador.toJson()
        try:
            self.__json.saveJSONArchivo(diccionario, 'Ejercicio 7/personal.json')
            print('Archio guardado...')
        except:
            print('ERROR: archivo no guardado')
    def error(self):
        print('ERROR: valor invalido')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()