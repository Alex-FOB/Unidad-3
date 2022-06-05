from Menu import menu

from objectEncoder import ObjectEncoder

if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        pass
    else:
        band = False
        jsonF = ObjectEncoder()
        diccionario = jsonF.leerJSONArchivo('Ejercicio 7/personal.json')
        manejador = jsonF.decodificarDiccionario(diccionario)
        interfaz = menu(manejador, jsonF)
        while not band:
            print('1.- Ingresar datos de usuario\n2.- Salir')
            try:
                op = int(input('Opcion: '))
                interfaz.opcion(op)
                band = op == 2
            except ValueError:
                interfaz.error()