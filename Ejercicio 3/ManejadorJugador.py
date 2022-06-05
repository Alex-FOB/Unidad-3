class manejadorJugador:
    __jugadores = None
    def __init__(self):
        self.__jugadores = []
    def addJugador(self, jugador): #añade un jugador a la lista
        self.__jugadores.append(jugador)
    def buscar(self, jugador): #busca un jugador y devuelve su posicion
        i = 0
        pos = -1
        band = False
        while not band and i < len(self.__jugadores):
            if(self.__jugadores[i].getNom().lower() == jugador.lower()):
                pos = i
                band = True
            i += 1
        return pos
    #NO ES NECESARIO-------------------------------
    def crearContrato(self, pos, contrato):
        self.__jugadores[pos].setContrato(contrato)
    #----------------------------------------------
    def getJugador(self, pos):
        return self.__jugadores[pos]