class ramo:
    __tamaño = None
    __flores = []
    def __init__(self, tamaño = '', flor = None, cantidad = 1):
        self.__tamaño = str(tamaño)
        self.__flores = []
        if(flor != None):
            self.addFlor(flor, cantidad)
    def __str__(self):
        text = 'Ramo de tamaño {}:\n'.format(self.__tamaño)
        for flor in self.__flores:
            text += '{}'.format(flor) + '\n'
        return text
    def addFlor(self, flor, cantidad): #se añade flores al ramo
        for i in range(cantidad):
            self.__flores.append(flor) 
    def getTamaño(self):
        return self.__tamaño