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
            interfaz.calcSueldo()
            print('1.- Insertar\n2.- Agregar\n3.- Motrat tipo\n4.- Mostrar agentes por carrera'
                '\n5.- Contar agentes por carrera\n6.- Lista\n7.- Listar por categoria\n8.- Guardar\n9.- Salir')
            try:
                op = int(input('Opcion: '))
                interfaz.opcion(op)
                band = op == 9
            except ValueError:
                interfaz.error()