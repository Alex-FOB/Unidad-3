from datetime import datetime

from Contrato import contrato

class menu:
    __op = None
    __equipos = None #manejador de equipos
    __jugadores = None #manejador de jugadores
    __contratos = None #manejador de contratos
    #------------------
    __dim = 0 #sirve para crear nuevos contratos
    def __init__(self, equipos, jugadores, contratos):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.punto4, 5: self.punto5, 6: self.salir}
        self.__equipos = equipos
        self.__jugadores = jugadores
        self.__contratos = contratos
        #-----------------------------
        self.__dim = 0
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def punto1(self): #crear contrato
        nomJ = str(input('Ingrese nombre del jugador: '))
        pos1 = self.__jugadores.buscar(nomJ)
        if(pos1 != -1): #verifica que el jugador esté en la lista
            jugador = self.__jugadores.getJugador(pos1)
            if(jugador.getContrato() == None): #verifica que el jugador no tenga contratos
                nomE = str(input('Ingrese nombre del equipo: '))
                pos2 = self.__equipos.buscar(nomE)
                if(pos2 != -1): #verifica que el equipo esté en el arreglo
                    equipo = self.__equipos.getEquipo(pos2)
                    inicio = str(input('Fecha de inicio de contrato: '))
                    fin = str(input('Fecha de finalizacion de contrato: '))
                    try:
                        pago = float(input('Ingrese pago del contrato: $'))
                        unContrato = contrato(inicio, fin, pago, jugador, equipo) #se crea un contrato
                        #se añade el contrato al arreglo en el manejador de contratos
                        self.__dim += 1
                        self.__contratos.setDim(self.__dim)
                        self.__contratos.addContrato(unContrato)
                        #---------------------------------------
                        self.__equipos.crearContratos(pos2, unContrato)
                        self.__jugadores.crearContrato(pos1, unContrato)
                        #---------------------------------------
                        print(unContrato)
                    except ValueError:
                        self.error()
                else:
                    print('ERROR: equipo no encontrado')
            else:
                print('ERROR: este jugador ya tiene un contrato')
        else:
            print('ERROR: jugador no encontrado')
        input()
    def punto2(self): #consultar jugadores contratados
        dni = str(input('Ingrese DNI del jugador: '))
        pos = self.__contratos.buscar(dni)
        if(pos != -1):
            print(self.__contratos.punto2(pos))
        else:
            print('ERROR: este jugador no tiene contrato')
        input()
    def punto3(self): #consultar contratos
        nom = str(input('Ingrese el nombre del equipo: '))
        pos = self.__equipos.buscar(nom)
        if(pos != -1):
            fecha = datetime.
            text = self.__equipos.mostrarContratos(pos)
            if(len(text) != 0):
                print('{}'.format(text))
            else:
                print('ERROR: contrato/s no encontrado')
        else:
            print('ERROR: equipo no encontrado')
        input()
    def punto4(self): #obtener importe de contratos
        equipo = str(input('Ingrese el nombre del equipo: '))
        pos = self.__equipos.buscar(equipo)
        if(pos != -1):
            total = self.__equipos.importeTotal(pos) #MODIFICAR
            print('Equipo: {}\nImporte total de contratos: ${}'.format(self.__equipos.getEquipo(pos).getNom(), total))
        else:
            print('ERROR: equipo no encontrado')
        input()
    def punto5(self): #guardar contratos
        if(self.__contratos.saveContratos() == True): #comprueba que se hayan almacenado los contratos
            print('CONTRATOS GUARDADOS...')
        else:
            print('ERROR: no se guardo ningun contrato')
        input()
    def error(self):
        print('ERROR')
        input()
    def salir(self):
        print('FINALIZANDO')
        input()