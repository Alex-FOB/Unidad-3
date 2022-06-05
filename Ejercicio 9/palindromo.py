class Palindromo:
    __palabra = None
    def __init__(self, palabra):
        self.__palabra = palabra
    def esPalindromo(self):
        i = 0
        j = len(self.__palabra) - 1 #MODIFICADO: j = -len(self.palabra)
        bandera = True
        while i < abs(j) and bandera:
           if self.__palabra[i] != self.__palabra[j]: #if self.__palabra[i] != self.__palabra[i]
               bandera=False
           else:
               i += 1
               j -= 1 #j += 1
        return bandera
    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra