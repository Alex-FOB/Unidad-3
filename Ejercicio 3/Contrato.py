class contrato:
    __fechaInicio = None
    __fechaFin = None
    __pago = None
    #----------------
    __jugador = None
    __equipo = None
    def __init__(self, inicio = '', fin = '', pago = 0.0, jugador = None, equipo = None):
        self.__fechaInicio = str(inicio)
        self.__fechaFin = str(fin)
        self.__pago = float(pago)
        self.__jugador = jugador
        self.__equipo = equipo
    def __str__(self):
        text = 'EQUIPO:\n{}\nJUGADOR: {}\nCONTRATO:\n'.format(self.__equipo, self.__jugador)
        text += 'Fecha de inicio: {:8} Fecha de finalizacion: {}\nImporte de contrato: ${}'.format(self.__fechaInicio, self.__fechaFin, self.__pago)
        return text
    def getInicio(self): #devuelve la fecha de inicio del contrato
        return self.__fechaInicio
    def getFin(self): #devuelve la fecha de finalización del contrato
        return self.__fechaFin
    def getPago(self): #devuelve el importe del contrato
        return self.__pago
    def getJugador(self): #devuelve una referencia del jugador
        return self.__jugador
    def getEquipo(self): #devuelve una referencia del equipo
        return self.__equipo