from posixpath import basename
from Carrera import carrera

class facultad:
    __cod = None #código de la facultad
    __nom = None #nombre de la facultad
    __dir = None #dirección de la facultad
    __loc = None #localidad de la facultad
    __tel = None #teléfono de la facultad
    __carreras = []
    def __init__(self, cod = 0, nom = '', dir = '', loc = '', tel = '', i = 0, reader = None):
        self.__cod = int(cod)
        self.__nom = str(nom)
        self.__dir = str(dir)
        self.__loc = str(loc)
        self.__tel = str(tel)
        #crear las instacias de carreras para almacenarlas en "self.__carreras"
        #preguntar si se puede hacer esto ------------------------------------
        lista = []
        band = True
        fila = next(reader)
        while band and i > 0:
            unaCarrera = carrera(fila[1], fila[2], fila[4], fila[3], fila[5])
            lista.append(unaCarrera)
            i -= 1
            if(i > 0): #si no está hay ValueError en el casteo (19) en la calse manejador
                try:
                    fila = next(reader)
                except StopIteration:
                    band = False
        #---------------------------------------------------------------------
        self.__carreras = lista.copy() #luego copia el contenido de la lista
        #NOTA: se copia el contenido porque si se usa directamente "self.__carreras.append(unaCarrera)" se acumulan
    #no se pide el __del__(self)
    def __str__(self): #imprime el contenido
        text = ''
        for carrera in self.__carreras:
            text += '{}, {}'.format(self.__cod, carrera) + '\n'
        return '{}, {}, {}, {}, {}\n{}'.format(self.__cod, self.__nom, self.__dir, self.__loc, self.__tel, text)
    def getFacultad(self): #devuelve un texto con los datos requeridos de una facultad con carreras
        text = '{}:\n'.format(self.__nom)
        for carrera in self.__carreras:
            text += '{}\n'.format(carrera.getCarrera())
        return text
    def getFacultad2(self, carrera):
        return '{}/{} - {} - {}'.format(self.__cod, self.__carreras[carrera].getCod(), self.__nom, self.__loc)
    def getCod(self): #devuelve el código de la facultad
        return self.__cod
    def getCarrera(self, carrera): #devuelve la posición de la carrera 
        pos = -1
        band = False
        i = 0
        while not band and i < len(self.__carreras):
            if(self.__carreras[i].getNom().lower() == carrera.lower()):
                pos = i
                band = True
            i += 1
        return pos