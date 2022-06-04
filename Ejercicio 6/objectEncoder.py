import json

from pathlib import Path

from Lista import Manejador

from Lavarropa import lavarropa

from Heladera import heladera

from Televisor import televisor

class ObjectEncoder:
    def decodificarDiccionario(self, diccionario):
        respuesta = None
        if('__class__' not in diccionario): #verifica que sea el diccionario adecuado
            respuesta = diccionario
        else:
            class_name = diccionario['__class__']
            class_ = eval(class_name)
            if(class_name == 'Manejador'):
                aparatos = diccionario['aparatos']
                manejador = class_()
                for i in range(len(aparatos)):
                    unAparato = aparatos[i]
                    #OPCIONAL------------------------------
                    class_name = unAparato.pop('__class__')
                    class_ = eval(class_name)
                    #--------------------------------------
                    dic = unAparato['__atributos__']
                    unAparato = class_(**dic) #crea la instancia de un aparato
                    manejador.agregarElemento(unAparato) #lo añade a la lista
                respuesta = manejador
        return respuesta
    def saveJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open('w', encoding = 'UTF-8') as destino:
            json.dump(diccionario, destino, indent = 4)
            destino.close()
    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding = 'UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)