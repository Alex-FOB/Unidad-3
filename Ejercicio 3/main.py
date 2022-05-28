import csv

from Menu import menu

from Equipo import equipo

from Jugador import jugador

from ManejadorEquipos import manejadorEquipos

from ManejadorJugador import manejadorJugador

from ManejadorContrato import manejadorContrato

def listarEquipos():
    equipos = manejadorEquipos()
    band = False
    dim = 0
    with open('Ejercicio 3/equipos.csv') as archi: #abre el archivo csv
        reader = csv.reader(archi, delimiter = ';') #lee el archivo
        for fila in reader:
            if(band == False):
                dim = int(fila[0])
                equipos.modDim(dim)
                band = True
            else:
                unEquipo = equipo(fila[0], fila[1])
                equipos.addEquipo(unEquipo)
        archi.close()
    return equipos
def listarJugadores():
    jugadores = manejadorJugador()
    band = False
    with open('Ejercicio 3/jugadores.csv') as archi: #abre el archivo csv
        reader = csv.reader(archi, delimiter = ';') #lee el archivo
        for fila in reader:
            if(band == False):
                band = True
            else:
                unJugador = jugador(fila[0], fila[1], fila[2], fila[3], fila[4])
                jugadores.addJugador(unJugador)
        archi.close()
    return jugadores
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        pass
    else:
        equipos = listarEquipos()
        jugadores = listarJugadores()
        contratos = manejadorContrato()
        interfaz = menu(equipos, jugadores, contratos)
        band = False
        while not band:
            print('1.- Crear un contrato\n2.- Consultar jugadores contratados\n3.- Consultar contratos'
                    '\n4.- Obtener importe contratos\n5.- Guardar contratos\n6.- Salir')
            try:
                op = int(input('Opcion: '))
                interfaz.opcion(op)
                band = op == 6
            except ValueError:
                interfaz.error()