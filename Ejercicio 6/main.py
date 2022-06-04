from Menu import menu

from objectEncoder import ObjectEncoder

if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        pass
    else:
        band = False
        jsonF = ObjectEncoder()
        diccionario = jsonF.leerJSONArchivo('Ejercicio 6/aparatoselectricos.json')
        manejador = jsonF.decodificarDiccionario(diccionario)
        interfaz = menu(jsonF, manejador)
        while not band:
            interfaz.calculaImp()
            print('1.- Insertar\n2.- Agregar\n3.- Mostrar tipo\n4.- Mostrar cantidad\n5.- Mostrar marca de lavarropas'
                    '\n6.- Mostrar\n7.- Almacenar\n8.- Salir')
            try:
                op = int(input('Opcion: '))
                interfaz.opcion(op)
                band = op == 8
            except ValueError:
                interfaz.error()

#NOTAS: probar el IndexError para los índices incorrectos